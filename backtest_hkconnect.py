from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Set, Tuple

os.environ.setdefault("MPLCONFIGDIR", str(Path("data_cache") / "mplconfig"))

import matplotlib
import numpy as np
import pandas as pd
import tushare as ts

matplotlib.use("Agg")

from scripts.results_layout import ensure_results_layout, market_backtests_dir, research_file, strategy_result_dir
from scripts.active_strategy_scope import collect_hkconnect_refresh_active_ids
from scripts.comparison_merge import merge_latest_rows

from backtest_marketcap_etf import (
    BUY_COMMISSION,
    SELL_COMMISSION,
    FLOAT_FORMAT,
    VERY_SHORT_SAMPLE_START,
    SHORT_SAMPLE_START,
    PRIMARY_SAMPLE_START,
    ROBUSTNESS_SAMPLE_START,
    MONTHLY_MOMENTUM_LOOKBACK,
    MONTHLY_MOMENTUM_SKIP,
    MONTHLY_MA_LOOKBACK,
    WEEKLY_MOMENTUM_LOOKBACK,
    WEEKLY_MOMENTUM_SKIP,
    WEEKLY_MA_LOOKBACK,
    CACHE_REFRESH_MAX_WORKERS,
    call_tushare_with_retry,
    read_cached_csv,
    save_csv,
    build_month_boundaries,
    safe_percentile_rank,
    blend_ranked_components,
    build_single_sleeve_weights,
    compute_market_exposure,
    compute_rebalance_trades,
    apply_weight_cap_with_redistribution,
    compute_metrics,
)


def _load_tokens() -> Tuple[str, str]:
    daily = os.environ.get("TUSHARE_TOKEN_DAILY", "")
    minute = os.environ.get("TUSHARE_TOKEN_MINUTE", "")
    if daily and minute:
        return daily, minute
    try:
        import importlib
        import config as _cfg

        importlib.reload(_cfg)
        daily = daily or getattr(_cfg, "TUSHARE_TOKEN_DAILY", "") or ""
        minute = minute or getattr(_cfg, "TUSHARE_TOKEN_MINUTE", "") or ""
        return daily, minute
    except Exception:
        return daily, minute


TUSHARE_DAILY_TOKEN, TUSHARE_MINUTE_TOKEN = _load_tokens()
_HK_CACHE_WORKER_STATE = threading.local()

HK_RESULTS_DIR = market_backtests_dir("hkconnect")
HK_CACHE_DIR = Path("data_cache") / "hkconnect"
HK_BASIC_DIR = HK_CACHE_DIR / "basic"
HK_PRICE_DIR = HK_CACHE_DIR / "daily_adj"
HK_FACTOR_DIR = HK_CACHE_DIR / "factor_cache"
HK_MANUAL_CONNECT_PATH = HK_BASIC_DIR / "stock_hsgt_manual.csv"
HK_PROGRESS_PATH = HK_BASIC_DIR / "prepare_progress.json"

CONNECT_UNIVERSE_START = pd.Timestamp("2025-08-12")
HK_DATA_HISTORY_MONTHS = 18
HK_MIN_LISTING_MONTHS = 12
HK_ROLLING_AMOUNT_WINDOW = 60
HK_BREAKOUT_LOOKBACK_DAYS = 20
HK_WEIGHT_CAP = 0.30
HK_MIN_WEIGHT_TRADE_THRESHOLD = 0.005
# HKEX closing auction random close ends by 16:10 local time. Keep the
# upstream daily_adj availability guard separate from the market close.
HK_MARKET_CLOSE_TIME = pd.Timedelta(hours=16, minutes=10)
HKCONNECT_DAILY_ADJ_READY_BUFFER = pd.Timedelta(hours=1, minutes=50)
HK_BUY_COMMISSION = BUY_COMMISSION
HK_SELL_COMMISSION = SELL_COMMISSION
HK_RISK_EVAL_FREQUENCY_MONTHLY = "monthly"
HK_RISK_EVAL_FREQUENCY_WEEKLY = "weekly"
HK_RISK_OVERLAY_SCOPE_PORTFOLIO = "portfolio_only"

HK_SAMPLE_WINDOWS = [
    {
        "sample_tag": "since_2020_01",
        "sample_label": "2020-01 起",
        "sample_short_label": "2020-01",
        "sample_start": PRIMARY_SAMPLE_START,
        "is_primary_sample": True,
    },
    {
        "sample_tag": "since_2017_01",
        "sample_label": "2017-01 起",
        "sample_short_label": "2017-01",
        "sample_start": ROBUSTNESS_SAMPLE_START,
        "is_primary_sample": False,
    },
    {
        "sample_tag": "since_2023_01",
        "sample_label": "2023-01 起",
        "sample_short_label": "2023-01",
        "sample_start": SHORT_SAMPLE_START,
        "is_primary_sample": False,
    },
    {
        "sample_tag": "since_2025_01",
        "sample_label": "2025-01 起",
        "sample_short_label": "2025-01",
        "sample_start": VERY_SHORT_SAMPLE_START,
        "is_primary_sample": False,
    },
    {
        "sample_tag": "since_2026_01",
        "sample_label": "2026-01 起（观察窗）",
        "sample_short_label": "2026-01",
        "sample_start": pd.Timestamp("2026-01-01"),
        "is_primary_sample": False,
    },
]


@dataclass
class HKFactorCache:
    eligible_codes_by_date: Dict[pd.Timestamp, List[str]]
    signal_mvs_by_date: Dict[pd.Timestamp, pd.Series]
    avg_daily_amount_by_date: Dict[pd.Timestamp, pd.Series]
    amount_surge_ratio_by_date: Dict[pd.Timestamp, pd.Series]
    recent_1m_returns_by_date: Dict[pd.Timestamp, pd.Series]
    momentum_12_1_by_date: Dict[pd.Timestamp, pd.Series]
    momentum_6_1_by_date: Dict[pd.Timestamp, pd.Series]
    momentum_3_1_by_date: Dict[pd.Timestamp, pd.Series]
    breakout_signal_by_date: Dict[pd.Timestamp, pd.Series]
    liquidity_quality_scores_by_date: Dict[pd.Timestamp, pd.Series]
    low_vol_scores_by_date: Dict[pd.Timestamp, pd.Series]
    small_cap_scores_by_date: Dict[pd.Timestamp, pd.Series]


@dataclass
class HKPreparedData:
    stock_basic: pd.DataFrame
    connect_basic: pd.DataFrame
    price_exact: pd.DataFrame
    price_ffill: pd.DataFrame
    total_mv: pd.DataFrame
    daily_amount: pd.DataFrame
    month_end_dates: List[pd.Timestamp]
    monthly_period_end_dates: List[pd.Timestamp]
    month_start_dates: List[pd.Timestamp]
    week_end_dates: List[pd.Timestamp]
    code_to_name: Dict[str, str]
    code_to_list_date: Dict[str, pd.Timestamp]
    market_monthly_close: pd.Series
    market_weekly_close: pd.Series
    data_warnings: List[str]
    factor_cache: HKFactorCache


HK_PATH1_VARIANTS: List[Dict[str, object]] = [
    {
        "strategy_id": "hkconnect_path1_monthly_hybrid",
        "strategy_name": "沪港通Path1 月度稳健(混合权重)",
        "path": "path1",
        "candidate_family": "monthly_moderate",
        "rebalance_frequency": "monthly",
        "base_weight_method": "total_mv",
        "base_weight_mode": "hybrid",
        "signal_family": "path1_moderate",
        "risk_off_rule": "or",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.50,
        "risk_caution_exposure": 0.80,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.18,
        "sell_exit_percentile": 0.32,
        "max_holdings": 14,
        "weight_cap": 0.18,
    },
    {
        "strategy_id": "hkconnect_path1_monthly_cashoff",
        "strategy_name": "沪港通Path1 月度稳健(熊市空仓)",
        "path": "path1",
        "candidate_family": "monthly_cashoff",
        "rebalance_frequency": "monthly",
        "base_weight_method": "total_mv",
        "base_weight_mode": "hybrid",
        "signal_family": "path1_moderate",
        "risk_off_rule": "or",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.00,
        "risk_caution_exposure": 0.70,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.18,
        "sell_exit_percentile": 0.32,
        "max_holdings": 14,
        "weight_cap": 0.18,
    },
    {
        "strategy_id": "hkconnect_path1_monthly_equal_buffered",
        "strategy_name": "沪港通Path1 月度等权缓冲",
        "path": "path1",
        "candidate_family": "monthly_equal_buffered",
        "rebalance_frequency": "monthly",
        "base_weight_method": "equal_weight",
        "base_weight_mode": "hybrid",
        "signal_family": "path1_moderate",
        "risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.60,
        "risk_caution_exposure": 0.85,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.20,
        "sell_exit_percentile": 0.35,
        "max_holdings": 12,
        "weight_cap": 0.16,
    },
    {
        "strategy_id": "hkconnect_path1_monthly_lowvol",
        "strategy_name": "沪港通Path1 月度低波偏稳",
        "path": "path1",
        "candidate_family": "monthly_lowvol",
        "rebalance_frequency": "monthly",
        "base_weight_method": "total_mv",
        "base_weight_mode": "base",
        "signal_family": "path1_lowvol",
        "risk_off_rule": "or",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.55,
        "risk_caution_exposure": 0.80,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.18,
        "sell_exit_percentile": 0.30,
        "max_holdings": 16,
        "weight_cap": 0.15,
    },
]

_HK_PATH1_TEMPLATE_BY_ID = {str(variant["strategy_id"]): variant for variant in HK_PATH1_VARIANTS}
HK_PATH1_VARIANTS.extend(
    [
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_hybrid"],
            "strategy_id": "hkconnect_path1_monthly_hybrid_weekly_overlay",
            "strategy_name": "沪港通Path1 月度稳健(混合权重+周度风控)",
            "candidate_family": "monthly_hybrid_weekly_overlay",
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_cashoff"],
            "strategy_id": "hkconnect_path1_monthly_cashoff_weekly_overlay",
            "strategy_name": "沪港通Path1 月度稳健(熊市空仓+周度风控)",
            "candidate_family": "monthly_cashoff_weekly_overlay",
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度风控)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻风控)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_exposure": 0.70,
            "risk_caution_exposure": 0.90,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_defensive",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度深防守)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.78,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_lowvol"],
            "strategy_id": "hkconnect_path1_monthly_lowvol_weekly_overlay_soft",
            "strategy_name": "沪港通Path1 月度低波偏稳(周度轻风控)",
            "candidate_family": "monthly_lowvol_weekly_overlay",
            "risk_off_exposure": 0.65,
            "risk_caution_exposure": 0.88,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波成本防守)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_exposure": 0.55,
            "risk_caution_exposure": 0.82,
            "sell_exit_percentile": 0.40,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度现金防守)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.72,
            "sell_exit_percentile": 0.42,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit45",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻风控+现金防守45)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.78,
            "sell_exit_percentile": 0.45,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波现金防守45)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.76,
            "sell_exit_percentile": 0.45,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻现金防守45)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.82,
            "sell_exit_percentile": 0.45,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻风控42)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_exposure": 0.62,
            "risk_caution_exposure": 0.86,
            "sell_exit_percentile": 0.42,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻风控38)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_exposure": 0.58,
            "risk_caution_exposure": 0.88,
            "sell_exit_percentile": 0.38,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻风控36)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_exposure": 0.56,
            "risk_caution_exposure": 0.90,
            "sell_exit_percentile": 0.36,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻风控40)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_exposure": 0.58,
            "risk_caution_exposure": 0.88,
            "sell_exit_percentile": 0.40,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit38",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻风控38)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_exposure": 0.56,
            "risk_caution_exposure": 0.90,
            "sell_exit_percentile": 0.38,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻风控36)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_exposure": 0.54,
            "risk_caution_exposure": 0.92,
            "sell_exit_percentile": 0.36,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻风控34)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_exposure": 0.52,
            "risk_caution_exposure": 0.94,
            "sell_exit_percentile": 0.34,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻风控34)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_exposure": 0.54,
            "risk_caution_exposure": 0.92,
            "sell_exit_percentile": 0.34,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻风控32)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_exposure": 0.52,
            "risk_caution_exposure": 0.94,
            "sell_exit_percentile": 0.32,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻风控32)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.95,
            "sell_exit_percentile": 0.32,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻风控34浅现金)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.88,
            "sell_exit_percentile": 0.34,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit32",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻现金32)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.86,
            "sell_exit_percentile": 0.32,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻成本32)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.82,
            "sell_exit_percentile": 0.32,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻成本30)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.80,
            "sell_exit_percentile": 0.30,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit28",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度低波轻成本28)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.78,
            "sell_exit_percentile": 0.28,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻成本34)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.84,
            "sell_exit_percentile": 0.34,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻成本32)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.82,
            "sell_exit_percentile": 0.32,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30",
            "strategy_name": "沪港通Path1 月度等权缓冲(周度轻成本30)",
            "candidate_family": "monthly_equal_buffered_weekly_overlay",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.80,
            "sell_exit_percentile": 0.30,
            "max_holdings": 14,
            "weight_cap": 0.14,
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_lowvol"],
            "strategy_id": "hkconnect_path1_monthly_lowvol_weekly_overlay",
            "strategy_name": "沪港通Path1 月度低波偏稳(周度风控)",
            "candidate_family": "monthly_lowvol_weekly_overlay",
            "risk_evaluation_frequency": HK_RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_overlay_scope": HK_RISK_OVERLAY_SCOPE_PORTFOLIO,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_hybrid"],
            "strategy_id": "hkconnect_path1_biweekly_hybrid",
            "strategy_name": "沪港通Path1 双周稳健(混合权重)",
            "candidate_family": "biweekly_moderate",
            "rebalance_frequency": "biweekly",
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.30,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_hybrid"],
            "strategy_id": "hkconnect_path1_weekly_hybrid",
            "strategy_name": "沪港通Path1 单周稳健(混合权重)",
            "candidate_family": "weekly_moderate",
            "rebalance_frequency": "weekly",
            "risk_off_exposure": 0.55,
            "risk_caution_exposure": 0.82,
            "buy_entry_percentile": 0.14,
            "sell_exit_percentile": 0.28,
            "max_holdings": 12,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_cashoff"],
            "strategy_id": "hkconnect_path1_biweekly_cashoff",
            "strategy_name": "沪港通Path1 双周稳健(熊市空仓)",
            "candidate_family": "biweekly_cashoff",
            "rebalance_frequency": "biweekly",
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.30,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_cashoff"],
            "strategy_id": "hkconnect_path1_weekly_cashoff",
            "strategy_name": "沪港通Path1 单周稳健(熊市空仓)",
            "candidate_family": "weekly_cashoff",
            "rebalance_frequency": "weekly",
            "risk_caution_exposure": 0.75,
            "buy_entry_percentile": 0.14,
            "sell_exit_percentile": 0.28,
            "max_holdings": 12,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered",
            "strategy_name": "沪港通Path1 双周等权缓冲",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.32,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_wide_exit",
            "strategy_name": "沪港通Path1 双周等权缓冲(宽出场)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.38,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_defensive",
            "strategy_name": "沪港通Path1 双周等权缓冲(防守降仓)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.35,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_cost_guard",
            "strategy_name": "沪港通Path1 双周等权缓冲(成本防守)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "risk_off_exposure": 0.55,
            "risk_caution_exposure": 0.82,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.40,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_cashguard",
            "strategy_name": "沪港通Path1 双周等权缓冲(现金防守)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.42,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45",
            "strategy_name": "沪港通Path1 双周等权缓冲(轻现金防守45)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.45,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cashguard_exit45",
            "strategy_name": "沪港通Path1 双周等权缓冲(低波轻现金防守45)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.82,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.45,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit42",
            "strategy_name": "沪港通Path1 双周等权缓冲(低波轻风控42)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.58,
            "risk_caution_exposure": 0.86,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.42,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40",
            "strategy_name": "沪港通Path1 双周等权缓冲(低波轻风控40)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.58,
            "risk_caution_exposure": 0.86,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.40,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_soft_exit40",
            "strategy_name": "沪港通Path1 双周等权缓冲(轻风控40)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.60,
            "risk_caution_exposure": 0.86,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.40,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38",
            "strategy_name": "沪港通Path1 双周等权缓冲(低波轻风控38)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.58,
            "risk_caution_exposure": 0.86,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.38,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36",
            "strategy_name": "沪港通Path1 双周等权缓冲(低波轻成本36)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.40,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.36,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34",
            "strategy_name": "沪港通Path1 双周等权缓冲(低波轻成本34)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.40,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.34,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit32",
            "strategy_name": "沪港通Path1 双周等权缓冲(低波轻成本32)",
            "candidate_family": "biweekly_equal_buffered",
            "rebalance_frequency": "biweekly",
            "signal_family": "path1_lowvol",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.40,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.32,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_equal_buffered"],
            "strategy_id": "hkconnect_path1_weekly_equal_buffered",
            "strategy_name": "沪港通Path1 单周等权缓冲",
            "candidate_family": "weekly_equal_buffered",
            "rebalance_frequency": "weekly",
            "risk_off_exposure": 0.65,
            "risk_caution_exposure": 0.88,
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.30,
            "max_holdings": 10,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_lowvol"],
            "strategy_id": "hkconnect_path1_biweekly_lowvol",
            "strategy_name": "沪港通Path1 双周低波偏稳",
            "candidate_family": "biweekly_lowvol",
            "rebalance_frequency": "biweekly",
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.28,
            "max_holdings": 14,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH1_TEMPLATE_BY_ID["hkconnect_path1_monthly_lowvol"],
            "strategy_id": "hkconnect_path1_weekly_lowvol",
            "strategy_name": "沪港通Path1 单周低波偏稳",
            "candidate_family": "weekly_lowvol",
            "rebalance_frequency": "weekly",
            "risk_off_exposure": 0.60,
            "risk_caution_exposure": 0.85,
            "buy_entry_percentile": 0.14,
            "sell_exit_percentile": 0.26,
            "max_holdings": 12,
            "weight_cap": 0.18,
        },
    ]
)


HK_PATH2_VARIANTS: List[Dict[str, object]] = [
    {
        "strategy_id": "hkconnect_path2_breakout_monthly",
        "strategy_name": "沪港通Path2 月度高集中突破",
        "path": "path2",
        "candidate_family": "high_concentration_breakout",
        "rebalance_frequency": "monthly",
        "base_weight_method": "equal_weight",
        "base_weight_mode": "signal",
        "signal_family": "path2_breakout",
        "risk_off_rule": "or",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.60,
        "risk_caution_exposure": 0.85,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.10,
        "sell_exit_percentile": 0.22,
        "max_holdings": 6,
        "weight_cap": 0.28,
    },
    {
        "strategy_id": "hkconnect_path2_breakout_biweekly",
        "strategy_name": "沪港通Path2 双周高集中突破",
        "path": "path2",
        "candidate_family": "biweekly_rebalance_aggressive",
        "rebalance_frequency": "biweekly",
        "base_weight_method": "equal_weight",
        "base_weight_mode": "signal",
        "signal_family": "path2_breakout",
        "risk_off_rule": "or",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.60,
        "risk_caution_exposure": 0.85,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.10,
        "sell_exit_percentile": 0.22,
        "max_holdings": 6,
        "weight_cap": 0.28,
    },
    {
        "strategy_id": "hkconnect_path2_breakout_weekly",
        "strategy_name": "沪港通Path2 单周高集中突破",
        "path": "path2",
        "candidate_family": "weekly_rebalance_aggressive",
        "rebalance_frequency": "weekly",
        "base_weight_method": "equal_weight",
        "base_weight_mode": "signal",
        "signal_family": "path2_breakout",
        "risk_off_rule": "or",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.65,
        "risk_caution_exposure": 0.90,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.08,
        "sell_exit_percentile": 0.18,
        "max_holdings": 5,
        "weight_cap": 0.32,
    },
    {
        "strategy_id": "hkconnect_path2_theme_monthly",
        "strategy_name": "沪港通Path2 月度高成长主线",
        "path": "path2",
        "candidate_family": "high_growth_theme",
        "rebalance_frequency": "monthly",
        "base_weight_method": "equal_weight",
        "base_weight_mode": "signal",
        "signal_family": "path2_theme",
        "risk_off_rule": "or",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.65,
        "risk_caution_exposure": 0.90,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.12,
        "sell_exit_percentile": 0.24,
        "max_holdings": 8,
        "weight_cap": 0.24,
    },
    {
        "strategy_id": "hkconnect_path2_theme_biweekly",
        "strategy_name": "沪港通Path2 双周高成长主线",
        "path": "path2",
        "candidate_family": "high_growth_theme",
        "rebalance_frequency": "biweekly",
        "base_weight_method": "equal_weight",
        "base_weight_mode": "signal",
        "signal_family": "path2_theme",
        "risk_off_rule": "or",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.65,
        "risk_caution_exposure": 0.90,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.10,
        "sell_exit_percentile": 0.22,
        "max_holdings": 7,
        "weight_cap": 0.26,
    },
    {
        "strategy_id": "hkconnect_path2_equal_elastic_monthly",
        "strategy_name": "沪港通Path2 月度等权高弹性",
        "path": "path2",
        "candidate_family": "momentum_equal_weight_elastic",
        "rebalance_frequency": "monthly",
        "base_weight_method": "equal_weight",
        "base_weight_mode": "signal",
        "signal_family": "path2_elastic",
        "risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.70,
        "risk_caution_exposure": 0.90,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.12,
        "sell_exit_percentile": 0.24,
        "max_holdings": 10,
        "weight_cap": 0.20,
    },
    {
        "strategy_id": "hkconnect_path2_equal_elastic_weekly",
        "strategy_name": "沪港通Path2 单周等权高弹性",
        "path": "path2",
        "candidate_family": "momentum_equal_weight_elastic",
        "rebalance_frequency": "weekly",
        "base_weight_method": "equal_weight",
        "base_weight_mode": "signal",
        "signal_family": "path2_elastic",
        "risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "risk_off_exposure": 0.70,
        "risk_caution_exposure": 0.92,
        "risk_on_exposure": 1.00,
        "buy_entry_percentile": 0.10,
        "sell_exit_percentile": 0.20,
        "max_holdings": 8,
        "weight_cap": 0.24,
    },
]

_HK_PATH2_TEMPLATE_BY_ID = {str(variant["strategy_id"]): variant for variant in HK_PATH2_VARIANTS}
HK_PATH2_VARIANTS.extend(
    [
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_biweekly"],
            "strategy_id": "hkconnect_path2_theme_weekly",
            "strategy_name": "沪港通Path2 单周高成长主线",
            "rebalance_frequency": "weekly",
            "buy_entry_percentile": 0.08,
            "sell_exit_percentile": 0.18,
            "max_holdings": 6,
            "weight_cap": 0.28,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_equal_elastic_biweekly",
            "strategy_name": "沪港通Path2 双周等权高弹性",
            "rebalance_frequency": "biweekly",
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.22,
            "max_holdings": 9,
            "weight_cap": 0.22,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_monthly"],
            "strategy_id": "hkconnect_path2_breakout_concentrated_monthly",
            "strategy_name": "沪港通Path2 月度极集中突破",
            "buy_entry_percentile": 0.06,
            "sell_exit_percentile": 0.14,
            "max_holdings": 4,
            "weight_cap": 0.40,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_concentrated_biweekly",
            "strategy_name": "沪港通Path2 双周极集中突破",
            "buy_entry_percentile": 0.06,
            "sell_exit_percentile": 0.14,
            "max_holdings": 4,
            "weight_cap": 0.40,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_weekly"],
            "strategy_id": "hkconnect_path2_breakout_concentrated_weekly",
            "strategy_name": "沪港通Path2 单周极集中突破",
            "buy_entry_percentile": 0.05,
            "sell_exit_percentile": 0.12,
            "max_holdings": 4,
            "weight_cap": 0.40,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_monthly"],
            "strategy_id": "hkconnect_path2_breakout_cashoff_monthly",
            "strategy_name": "沪港通Path2 月度突破(熊市空仓)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.70,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cashoff_biweekly",
            "strategy_name": "沪港通Path2 双周突破(熊市空仓)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.70,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_weekly"],
            "strategy_id": "hkconnect_path2_breakout_cashoff_weekly",
            "strategy_name": "沪港通Path2 单周突破(熊市空仓)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.75,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_risk50_biweekly",
            "strategy_name": "沪港通Path2 双周突破(熊市50%)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.80,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_buffered_biweekly",
            "strategy_name": "沪港通Path2 双周突破(宽出场)",
            "sell_exit_percentile": 0.26,
            "max_holdings": 6,
            "weight_cap": 0.28,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_defensive_biweekly",
            "strategy_name": "沪港通Path2 双周突破(防守降仓)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.40,
            "risk_caution_exposure": 0.75,
            "sell_exit_percentile": 0.24,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_balanced_biweekly",
            "strategy_name": "沪港通Path2 双周突破(五持仓)",
            "buy_entry_percentile": 0.08,
            "sell_exit_percentile": 0.20,
            "max_holdings": 5,
            "weight_cap": 0.32,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly",
            "strategy_name": "沪港通Path2 双周突破(成本防守)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.09,
            "sell_exit_percentile": 0.30,
            "max_holdings": 7,
            "weight_cap": 0.24,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_exit35",
            "strategy_name": "沪港通Path2 双周突破(成本防守宽出场35)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.09,
            "sell_exit_percentile": 0.35,
            "max_holdings": 7,
            "weight_cap": 0.24,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_risk50",
            "strategy_name": "沪港通Path2 双周突破(成本防守熊市50)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.76,
            "buy_entry_percentile": 0.09,
            "sell_exit_percentile": 0.35,
            "max_holdings": 7,
            "weight_cap": 0.24,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_cashguard_exit35_risk50",
            "strategy_name": "沪港通Path2 双周突破(现金防守35谨慎50)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.50,
            "buy_entry_percentile": 0.09,
            "sell_exit_percentile": 0.35,
            "max_holdings": 7,
            "weight_cap": 0.24,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit40_risk45",
            "strategy_name": "沪港通Path2 双周突破(防守现金40谨慎45)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.45,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.40,
            "max_holdings": 8,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit38_risk40",
            "strategy_name": "沪港通Path2 双周突破(防守现金38谨慎40)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.40,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.38,
            "max_holdings": 8,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit36_risk35",
            "strategy_name": "沪港通Path2 双周突破(防守现金36谨慎35)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.35,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.36,
            "max_holdings": 8,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit34_risk35",
            "strategy_name": "沪港通Path2 双周突破(防守现金34谨慎35)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.35,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.34,
            "max_holdings": 8,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit32_risk30",
            "strategy_name": "沪港通Path2 双周突破(防守现金32谨慎30)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.30,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.32,
            "max_holdings": 8,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_biweekly"],
            "strategy_id": "hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit30_risk25",
            "strategy_name": "沪港通Path2 双周突破(防守现金30谨慎25)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.25,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.30,
            "max_holdings": 8,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_breakout_weekly"],
            "strategy_id": "hkconnect_path2_breakout_risk50_weekly",
            "strategy_name": "沪港通Path2 单周突破(熊市50%)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.82,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_fast_monthly",
            "strategy_name": "沪港通Path2 月度快速主线",
            "buy_entry_percentile": 0.08,
            "sell_exit_percentile": 0.18,
            "max_holdings": 6,
            "weight_cap": 0.28,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_biweekly"],
            "strategy_id": "hkconnect_path2_theme_fast_biweekly",
            "strategy_name": "沪港通Path2 双周快速主线",
            "buy_entry_percentile": 0.08,
            "sell_exit_percentile": 0.18,
            "max_holdings": 6,
            "weight_cap": 0.28,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_biweekly"],
            "strategy_id": "hkconnect_path2_theme_fast_weekly",
            "strategy_name": "沪港通Path2 单周快速主线",
            "rebalance_frequency": "weekly",
            "buy_entry_percentile": 0.07,
            "sell_exit_percentile": 0.16,
            "max_holdings": 5,
            "weight_cap": 0.32,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_equal_elastic_cashoff_biweekly",
            "strategy_name": "沪港通Path2 双周等权高弹性(熊市空仓)",
            "rebalance_frequency": "biweekly",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.75,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.22,
            "max_holdings": 9,
            "weight_cap": 0.22,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_weekly"],
            "strategy_id": "hkconnect_path2_equal_elastic_cashoff_weekly",
            "strategy_name": "沪港通Path2 单周等权高弹性(熊市空仓)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.78,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly",
            "strategy_name": "沪港通Path2 月度逆市值高弹性",
            "base_weight_method": "inverse_mv",
            "max_holdings": 10,
            "weight_cap": 0.22,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_equal_elastic_monthly_defensive",
            "strategy_name": "沪港通Path2 月度等权高弹性(低成本防守)",
            "risk_off_exposure": 0.55,
            "risk_caution_exposure": 0.82,
            "sell_exit_percentile": 0.28,
            "max_holdings": 10,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_equal_elastic_monthly_cost_guard_v2",
            "strategy_name": "沪港通Path2 月度等权高弹性(成本防守v2)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.76,
            "sell_exit_percentile": 0.34,
            "max_holdings": 12,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_equal_elastic_monthly_cost_guard_v3",
            "strategy_name": "沪港通Path2 月度等权高弹性(成本防守v3)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.72,
            "sell_exit_percentile": 0.38,
            "max_holdings": 12,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_equal_elastic_monthly_cost_guard_v4",
            "strategy_name": "沪港通Path2 月度等权高弹性(成本防守v4)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.30,
            "risk_caution_exposure": 0.70,
            "sell_exit_percentile": 0.42,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_equal_elastic_monthly_cashguard_v3",
            "strategy_name": "沪港通Path2 月度等权高弹性(现金防守v3)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.70,
            "sell_exit_percentile": 0.36,
            "max_holdings": 12,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_cost_guard_v2",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(成本防守v2)",
            "base_weight_method": "inverse_mv",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.42,
            "risk_caution_exposure": 0.74,
            "sell_exit_percentile": 0.34,
            "max_holdings": 12,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_cashguard_v3",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(现金防守v3)",
            "base_weight_method": "inverse_mv",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.70,
            "sell_exit_percentile": 0.36,
            "max_holdings": 12,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_cost_guard_v3",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(成本防守v3)",
            "base_weight_method": "inverse_mv",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.72,
            "sell_exit_percentile": 0.38,
            "max_holdings": 12,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_cost_guard_v4",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(成本防守v4)",
            "base_weight_method": "inverse_mv",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.30,
            "risk_caution_exposure": 0.70,
            "sell_exit_percentile": 0.42,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_cost_guard_v5",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(成本防守v5)",
            "base_weight_method": "inverse_mv",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.32,
            "risk_caution_exposure": 0.74,
            "buy_entry_percentile": 0.12,
            "sell_exit_percentile": 0.30,
            "max_holdings": 10,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_cost_guard_v6",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(成本防守v6)",
            "base_weight_method": "inverse_mv",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.34,
            "risk_caution_exposure": 0.72,
            "buy_entry_percentile": 0.13,
            "sell_exit_percentile": 0.34,
            "max_holdings": 12,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_cost_guard_v7",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(成本防守v7)",
            "base_weight_method": "inverse_mv",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.36,
            "risk_caution_exposure": 0.76,
            "buy_entry_percentile": 0.12,
            "sell_exit_percentile": 0.36,
            "max_holdings": 14,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_cost_guard_v8",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(成本防守v8)",
            "base_weight_method": "inverse_mv",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.28,
            "risk_caution_exposure": 0.68,
            "buy_entry_percentile": 0.14,
            "sell_exit_percentile": 0.44,
            "max_holdings": 16,
            "weight_cap": 0.12,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_monthly_defensive",
            "strategy_name": "沪港通Path2 月度逆市值高弹性(低成本防守)",
            "base_weight_method": "inverse_mv",
            "risk_off_exposure": 0.55,
            "risk_caution_exposure": 0.82,
            "sell_exit_percentile": 0.28,
            "max_holdings": 10,
            "weight_cap": 0.22,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_cost_control",
            "strategy_name": "沪港通Path2 月度高成长主线(成本约束)",
            "sell_exit_percentile": 0.28,
            "max_holdings": 10,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_cost_control_v2",
            "strategy_name": "沪港通Path2 月度高成长主线(成本约束v2)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.78,
            "sell_exit_percentile": 0.32,
            "max_holdings": 12,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_cost_control_lowturn",
            "strategy_name": "沪港通Path2 月度高成长主线(低换手成本约束)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.42,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.13,
            "sell_exit_percentile": 0.36,
            "max_holdings": 14,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_reconfirm_cost_control",
            "strategy_name": "沪港通Path2 月度高成长主线(再确认成本约束)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.76,
            "buy_entry_percentile": 0.11,
            "sell_exit_percentile": 0.34,
            "max_holdings": 12,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control",
            "strategy_name": "沪港通Path2 月度高成长主线(高收益再确认成本约束)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.40,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.30,
            "max_holdings": 10,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_high_return_lowturn_reconfirm",
            "strategy_name": "沪港通Path2 月度高成长主线(高收益低换手再确认)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.38,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.34,
            "max_holdings": 12,
            "weight_cap": 0.17,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_high_return_cost_control_v2",
            "strategy_name": "沪港通Path2 月度高成长主线(高收益成本约束v2)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.36,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.32,
            "max_holdings": 11,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_high_return_cost_control_v3",
            "strategy_name": "沪港通Path2 月度高成长主线(高收益成本约束v3)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.34,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.34,
            "max_holdings": 12,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_monthly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_biweekly",
            "strategy_name": "沪港通Path2 双周逆市值高弹性",
            "base_weight_method": "inverse_mv",
            "rebalance_frequency": "biweekly",
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.22,
            "max_holdings": 9,
            "weight_cap": 0.24,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_high_return_cost_control_v4",
            "strategy_name": "沪港通Path2 月度高成长主线(高收益成本约束v4)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.38,
            "risk_caution_exposure": 0.82,
            "buy_entry_percentile": 0.09,
            "sell_exit_percentile": 0.30,
            "max_holdings": 10,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v5",
            "strategy_name": "沪港通Path2 月度高成长主线(再确认高收益成本约束v5)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.40,
            "risk_caution_exposure": 0.84,
            "buy_entry_percentile": 0.08,
            "sell_exit_percentile": 0.28,
            "max_holdings": 9,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v6",
            "strategy_name": "沪港通Path2 月度高成长主线(再确认高收益成本约束v6)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.42,
            "risk_caution_exposure": 0.82,
            "buy_entry_percentile": 0.09,
            "sell_exit_percentile": 0.30,
            "max_holdings": 10,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v7",
            "strategy_name": "沪港通Path2 月度高成长主线(再确认高收益成本约束v7)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.44,
            "risk_caution_exposure": 0.84,
            "buy_entry_percentile": 0.08,
            "sell_exit_percentile": 0.28,
            "max_holdings": 11,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_theme_monthly"],
            "strategy_id": "hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v8",
            "strategy_name": "沪港通Path2 月度高成长主线(再确认高收益成本约束v8)",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.40,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.09,
            "sell_exit_percentile": 0.32,
            "max_holdings": 12,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH2_TEMPLATE_BY_ID["hkconnect_path2_equal_elastic_weekly"],
            "strategy_id": "hkconnect_path2_inverse_elastic_weekly",
            "strategy_name": "沪港通Path2 单周逆市值高弹性",
            "base_weight_method": "inverse_mv",
            "max_holdings": 8,
            "weight_cap": 0.26,
        },
    ]
)


def clone_hk_weekly_variant_for_path3(variant: Dict[str, object]) -> Dict[str, object]:
    strategy_id = str(variant["strategy_id"])
    if strategy_id.startswith("hkconnect_path1_weekly_"):
        path3_id = strategy_id.replace("hkconnect_path1_weekly_", "hkconnect_path3_stable_weekly_", 1)
    elif strategy_id.startswith("hkconnect_path2_"):
        path3_id = strategy_id.replace("hkconnect_path2_", "hkconnect_path3_", 1)
    else:
        path3_id = strategy_id.replace("hkconnect_", "hkconnect_path3_", 1)

    strategy_name = str(variant["strategy_name"])
    strategy_name = strategy_name.replace("沪港通Path1 单周", "沪港通Path3 单周稳健")
    strategy_name = strategy_name.replace("沪港通Path2 单周", "沪港通Path3 单周")
    strategy_name = strategy_name.replace("单周稳健稳健", "单周稳健")

    candidate_family = str(variant.get("candidate_family", "weekly"))
    if not candidate_family.startswith("weekly_"):
        candidate_family = f"weekly_{candidate_family}"

    return {
        **variant,
        "strategy_id": path3_id,
        "strategy_name": strategy_name,
        "path": "path3",
        "candidate_family": candidate_family,
        "rebalance_frequency": "weekly",
    }


HK_PATH3_VARIANTS: List[Dict[str, object]] = [
    clone_hk_weekly_variant_for_path3(variant)
    for variant in [*HK_PATH1_VARIANTS, *HK_PATH2_VARIANTS]
    if str(variant.get("rebalance_frequency", "")).lower() == "weekly"
]
_HK_PATH3_TEMPLATE_BY_ID = {str(variant["strategy_id"]): variant for variant in HK_PATH3_VARIANTS}
HK_PATH3_VARIANTS.extend(
    [
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_buffered",
            "strategy_name": "沪港通Path3 单周快速主线(宽出场)",
            "candidate_family": "weekly_high_growth_theme_buffered",
            "sell_exit_percentile": 0.22,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive",
            "strategy_name": "沪港通Path3 单周快速主线(降仓)",
            "candidate_family": "weekly_high_growth_theme_defensive",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.80,
            "sell_exit_percentile": 0.18,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_balanced6",
            "strategy_name": "沪港通Path3 单周快速主线(六持仓)",
            "candidate_family": "weekly_high_growth_theme_balanced",
            "risk_off_exposure": 0.60,
            "risk_caution_exposure": 0.85,
            "buy_entry_percentile": 0.08,
            "sell_exit_percentile": 0.22,
            "max_holdings": 6,
            "weight_cap": 0.28,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive_wide",
            "strategy_name": "沪港通Path3 单周快速主线(降仓宽出场)",
            "candidate_family": "weekly_high_growth_theme_defensive",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.80,
            "sell_exit_percentile": 0.24,
            "max_holdings": 6,
            "weight_cap": 0.28,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive_cap26",
            "strategy_name": "沪港通Path3 单周快速主线(降仓限额)",
            "candidate_family": "weekly_high_growth_theme_defensive",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.80,
            "buy_entry_percentile": 0.08,
            "sell_exit_percentile": 0.22,
            "max_holdings": 6,
            "weight_cap": 0.26,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cashguard",
            "strategy_name": "沪港通Path3 单周快速主线(强防守)",
            "candidate_family": "weekly_high_growth_theme_defensive",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "sell_exit_percentile": 0.22,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_turnover20",
            "strategy_name": "沪港通Path3 单周快速主线(宽出场降换手)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_exposure": 0.55,
            "risk_caution_exposure": 0.82,
            "buy_entry_percentile": 0.09,
            "sell_exit_percentile": 0.26,
            "max_holdings": 7,
            "weight_cap": 0.24,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_turnover_guard",
            "strategy_name": "沪港通Path3 单周快速主线(防守降换手)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.76,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.28,
            "max_holdings": 7,
            "weight_cap": 0.24,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive_turnover18",
            "strategy_name": "沪港通Path3 单周快速主线(防守低换手18)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.74,
            "buy_entry_percentile": 0.11,
            "sell_exit_percentile": 0.30,
            "max_holdings": 8,
            "weight_cap": 0.22,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cashguard_turnover20",
            "strategy_name": "沪港通Path3 单周快速主线(现金防守低换手20)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.72,
            "buy_entry_percentile": 0.10,
            "sell_exit_percentile": 0.30,
            "max_holdings": 8,
            "weight_cap": 0.22,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover18_exit42",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守18出场42)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.11,
            "sell_exit_percentile": 0.42,
            "max_holdings": 8,
            "weight_cap": 0.20,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover14_exit45",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守14出场45)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.12,
            "sell_exit_percentile": 0.45,
            "max_holdings": 8,
            "weight_cap": 0.18,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover16_exit45",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守16出场45)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.115,
            "sell_exit_percentile": 0.45,
            "max_holdings": 8,
            "weight_cap": 0.19,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover12_exit48",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守12出场48)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.13,
            "sell_exit_percentile": 0.48,
            "max_holdings": 9,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive_turnover12_exit48",
            "strategy_name": "沪港通Path3 单周快速主线(防守12出场48)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.68,
            "buy_entry_percentile": 0.13,
            "sell_exit_percentile": 0.48,
            "max_holdings": 9,
            "weight_cap": 0.16,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover10_exit50",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守10出场50)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.14,
            "sell_exit_percentile": 0.50,
            "max_holdings": 10,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover8_exit52",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守8出场52)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.15,
            "sell_exit_percentile": 0.52,
            "max_holdings": 12,
            "weight_cap": 0.12,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover6_exit54",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守6出场54)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.54,
            "max_holdings": 14,
            "weight_cap": 0.10,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover5_exit56",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守5出场56)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.17,
            "sell_exit_percentile": 0.56,
            "max_holdings": 15,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover4_exit58",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守4出场58)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.58,
            "max_holdings": 16,
            "weight_cap": 0.08,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover3_exit60",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守3出场60)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.19,
            "sell_exit_percentile": 0.60,
            "max_holdings": 18,
            "weight_cap": 0.07,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit62",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守2出场62)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.20,
            "sell_exit_percentile": 0.62,
            "max_holdings": 20,
            "weight_cap": 0.06,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit64",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守2出场64)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.21,
            "sell_exit_percentile": 0.64,
            "max_holdings": 22,
            "weight_cap": 0.055,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit66",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守1出场66)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.22,
            "sell_exit_percentile": 0.66,
            "max_holdings": 24,
            "weight_cap": 0.045,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit68",
            "strategy_name": "沪港通Path3 单周快速主线(成本防守1出场68)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.35,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.23,
            "sell_exit_percentile": 0.68,
            "max_holdings": 26,
            "weight_cap": 0.04,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive_turnover3_exit60",
            "strategy_name": "沪港通Path3 单周快速主线(防守3出场60)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.64,
            "buy_entry_percentile": 0.19,
            "sell_exit_percentile": 0.60,
            "max_holdings": 18,
            "weight_cap": 0.07,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive_turnover10_exit50",
            "strategy_name": "沪港通Path3 单周快速主线(防守10出场50)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.66,
            "buy_entry_percentile": 0.14,
            "sell_exit_percentile": 0.50,
            "max_holdings": 10,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive_turnover8_exit52",
            "strategy_name": "沪港通Path3 单周快速主线(防守8出场52)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.66,
            "buy_entry_percentile": 0.15,
            "sell_exit_percentile": 0.52,
            "max_holdings": 12,
            "weight_cap": 0.12,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_theme_fast_weekly"],
            "strategy_id": "hkconnect_path3_theme_fast_weekly_defensive_turnover6_exit54",
            "strategy_name": "沪港通Path3 单周快速主线(防守6出场54)",
            "candidate_family": "weekly_high_growth_theme_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.66,
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.54,
            "max_holdings": 14,
            "weight_cap": 0.10,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cost_guard",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(成本防守)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.55,
            "risk_caution_exposure": 0.82,
            "sell_exit_percentile": 0.36,
            "max_holdings": 12,
            "weight_cap": 0.14,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(成本防守低换手8)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.46,
            "max_holdings": 16,
            "weight_cap": 0.10,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit40",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(成本防守低换手6出场40)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.48,
            "risk_caution_exposure": 0.76,
            "buy_entry_percentile": 0.22,
            "sell_exit_percentile": 0.40,
            "max_holdings": 20,
            "weight_cap": 0.08,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover7_exit45",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(成本防守低换手7出场45)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.20,
            "sell_exit_percentile": 0.45,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit42",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(成本防守低换手8出场42)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.42,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit40",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(成本防守低换手8出场40)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.40,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover9_exit40",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(成本防守低换手9出场40)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.17,
            "sell_exit_percentile": 0.40,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(成本防守低换手10出场38)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.50,
            "risk_caution_exposure": 0.78,
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.38,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover9_exit42",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(防守低换手9出场42)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.72,
            "buy_entry_percentile": 0.17,
            "sell_exit_percentile": 0.42,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover10_exit36",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(防守低换手10出场36)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.72,
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.36,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover8_exit38",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(防守低换手8出场38)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.72,
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.38,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover6_exit38",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(防守低换手6出场38)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.45,
            "risk_caution_exposure": 0.72,
            "buy_entry_percentile": 0.16,
            "sell_exit_percentile": 0.38,
            "max_holdings": 18,
            "weight_cap": 0.09,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_cashguard_turnover9",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(现金防守低换手9)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_rule": "and",
            "risk_off_exposure": 0.00,
            "risk_caution_exposure": 0.70,
            "buy_entry_percentile": 0.18,
            "sell_exit_percentile": 0.48,
            "max_holdings": 16,
            "weight_cap": 0.10,
        },
        {
            **_HK_PATH3_TEMPLATE_BY_ID["hkconnect_path3_stable_weekly_equal_buffered"],
            "strategy_id": "hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard",
            "strategy_name": "沪港通Path3 单周稳健等权缓冲(宽出场成本防守)",
            "candidate_family": "weekly_equal_buffered_cost_control",
            "risk_off_exposure": 0.60,
            "risk_caution_exposure": 0.85,
            "sell_exit_percentile": 0.42,
            "max_holdings": 14,
            "weight_cap": 0.12,
        },
    ]
)
HK_PATH1_VARIANTS = [
    variant
    for variant in HK_PATH1_VARIANTS
    if str(variant.get("rebalance_frequency", "")).lower() != "weekly"
]
HK_PATH2_VARIANTS = [
    variant
    for variant in HK_PATH2_VARIANTS
    if str(variant.get("rebalance_frequency", "")).lower() != "weekly"
]


def ensure_hk_directories() -> None:
    for path in [HK_RESULTS_DIR, HK_CACHE_DIR, HK_BASIC_DIR, HK_PRICE_DIR, HK_FACTOR_DIR]:
        path.mkdir(parents=True, exist_ok=True)
    ensure_results_layout()


def load_or_fetch_hk_trade_calendar(pro, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = HK_BASIC_DIR / "trade_calendar_hk.csv"
    cached = read_cached_csv(cache_path, date_columns=["cal_date"])
    required_end_date = max(end_date.normalize(), (end_date + pd.offsets.MonthEnd(0)).normalize())
    if not cached.empty:
        cached = cached.sort_values("cal_date").drop_duplicates(subset=["cal_date"])
        if cached["cal_date"].min() <= start_date and cached["cal_date"].max() >= required_end_date:
            return cached[(cached["cal_date"] >= start_date) & (cached["cal_date"] <= required_end_date)].reset_index(drop=True)

    try:
        fetched = call_tushare_with_retry(
            pro.hk_tradecal,
            start_date=start_date.strftime("%Y%m%d"),
            end_date=required_end_date.strftime("%Y%m%d"),
        )
    except RuntimeError:
        if not cached.empty:
            print("[Warn] 港股 trade_calendar 更新失败，回退使用本地缓存。")
            return cached[(cached["cal_date"] >= start_date) & (cached["cal_date"] <= required_end_date)].reset_index(drop=True)
        raise

    if "exchange" not in fetched.columns:
        fetched["exchange"] = "XHKG"
    fetched["cal_date"] = pd.to_datetime(fetched["cal_date"], format="%Y%m%d", errors="coerce")
    calendar = fetched.sort_values("cal_date").drop_duplicates(subset=["cal_date"]).reset_index(drop=True)
    save_csv(calendar, cache_path)
    return calendar[(calendar["cal_date"] >= start_date) & (calendar["cal_date"] <= required_end_date)].reset_index(drop=True)


def extend_hk_calendar_with_cached_price_dates(
    calendar: pd.DataFrame,
    price_frames: List[pd.DataFrame],
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
) -> pd.DataFrame:
    if not price_frames:
        return calendar
    price_dates: Set[pd.Timestamp] = set()
    start_date = start_date.normalize()
    end_date = end_date.normalize()
    for frame in price_frames:
        for raw_date in frame.index:
            trade_date = pd.Timestamp(raw_date).normalize()
            if start_date <= trade_date <= end_date:
                price_dates.add(trade_date)
    if not price_dates:
        return calendar

    typed = calendar.copy()
    typed["cal_date"] = pd.to_datetime(typed["cal_date"], errors="coerce")
    typed["is_open"] = pd.to_numeric(typed.get("is_open", 0), errors="coerce").fillna(0).astype(int)
    typed = typed.dropna(subset=["cal_date"])
    open_dates = set(typed.loc[typed["is_open"] == 1, "cal_date"].dt.normalize())
    combined_open_dates = sorted(open_dates | price_dates)
    if not combined_open_dates:
        return calendar

    extended = pd.DataFrame({"cal_date": combined_open_dates, "is_open": 1})
    extended["pretrade_date"] = extended["cal_date"].shift(1).dt.strftime("%Y%m%d")
    extended["pretrade_date"] = extended["pretrade_date"].fillna("")
    extended["exchange"] = "XHKG"
    return extended


def load_or_fetch_hk_basic(pro) -> pd.DataFrame:
    cache_path = HK_BASIC_DIR / "hk_basic.csv"
    cached = read_cached_csv(cache_path, date_columns=["list_date", "delist_date"])
    if not cached.empty:
        return cached

    frames: List[pd.DataFrame] = []
    for list_status in ["L", "D", "P"]:
        try:
            frame = call_tushare_with_retry(pro.hk_basic, list_status=list_status)
            frames.append(frame)
        except Exception:
            if list_status == "L":
                raise
    hk_basic = pd.concat(frames, ignore_index=True).drop_duplicates(subset=["ts_code"])
    hk_basic["list_date"] = pd.to_datetime(hk_basic["list_date"], format="%Y%m%d", errors="coerce")
    hk_basic["delist_date"] = pd.to_datetime(hk_basic["delist_date"], format="%Y%m%d", errors="coerce")
    hk_basic = hk_basic.sort_values("ts_code").reset_index(drop=True)
    save_csv(hk_basic, cache_path)
    return hk_basic


def load_or_fetch_stock_hsgt_latest(pro, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = HK_BASIC_DIR / "stock_hsgt.csv"
    cached = read_cached_csv(cache_path, date_columns=["trade_date"])
    manual = read_cached_csv(HK_MANUAL_CONNECT_PATH)
    if not manual.empty:
        required_cols = {"ts_code"}
        if not required_cols.issubset(set(manual.columns)):
            raise RuntimeError("手工沪港通标的文件缺少必需列：ts_code")
        manual = manual.copy()
        if "type" not in manual.columns:
            manual["type"] = "MANUAL"
        if "name" not in manual.columns:
            manual["name"] = ""
        return manual.sort_values(["type", "ts_code"]).drop_duplicates(subset=["ts_code"]).reset_index(drop=True)

    fetch_needed = cached.empty
    if not cached.empty and "trade_date" in cached.columns:
        latest_cached = pd.to_datetime(cached["trade_date"]).max()
        fetch_needed = latest_cached < end_date.normalize()

    if fetch_needed:
        frames: List[pd.DataFrame] = []
        for connect_type in ["SH_HK", "SZ_HK"]:
            try:
                fetched = call_tushare_with_retry(
                    pro.stock_hsgt,
                    type=connect_type,
                    start_date=CONNECT_UNIVERSE_START.strftime("%Y%m%d"),
                    end_date=end_date.strftime("%Y%m%d"),
                )
                if not fetched.empty:
                    fetched["trade_date"] = pd.to_datetime(fetched["trade_date"], format="%Y%m%d", errors="coerce")
                    frames.append(fetched)
            except RuntimeError:
                continue
        if frames:
            raw = pd.concat([cached] + frames, ignore_index=True)
            raw = raw.sort_values(["trade_date", "type", "ts_code"]).drop_duplicates(
                subset=["trade_date", "type", "ts_code"], keep="last"
            ).reset_index(drop=True)
            save_csv(raw, cache_path)
            cached = raw

    if cached.empty:
        raise RuntimeError(
            "无法获取沪港通标的列表（stock_hsgt）。请先准备本地缓存或检查 Tushare 权限；"
            f"也可手工提供 {HK_MANUAL_CONNECT_PATH}。"
        )

    latest_date = pd.to_datetime(cached["trade_date"]).max()
    latest = cached.loc[
        (pd.to_datetime(cached["trade_date"]) == latest_date) & cached["type"].isin(["SH_HK", "SZ_HK"])
    ].copy()
    latest = latest.sort_values(["type", "ts_code"]).drop_duplicates(subset=["ts_code"]).reset_index(drop=True)
    return latest


def load_or_fetch_hk_daily_adj(pro, ts_code: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = HK_PRICE_DIR / f"{ts_code}.csv"
    cached = read_cached_csv(cache_path, date_columns=["trade_date"])
    if "trade_date" in cached.columns:
        cached = cached.sort_values("trade_date").drop_duplicates(subset=["trade_date"])
    else:
        cached = pd.DataFrame()

    fetch_from = start_date
    if not cached.empty:
        latest_cached = cached["trade_date"].max()
        if latest_cached >= end_date:
            return cached.reset_index(drop=True)
        fetch_from = latest_cached + pd.Timedelta(days=1)

    try:
        fetched = call_tushare_with_retry(
            pro.hk_daily_adj,
            ts_code=ts_code,
            start_date=fetch_from.strftime("%Y%m%d"),
            end_date=end_date.strftime("%Y%m%d"),
        )
    except RuntimeError as exc:
        error_text = str(exc)
        cause_text = str(exc.__cause__) if exc.__cause__ else ""
        combined_text = f"{error_text} | {cause_text}"
        if any(keyword in combined_text for keyword in ["频率超限", "每分钟最多访问", "每小时最多访问", "每分钟最多访问该接口", "每小时"]):
            raise RuntimeError(f"{ts_code} hk_daily_adj 触发频率限制") from exc
        if not cached.empty:
            print(f"[Warn] {ts_code} hk_daily_adj 更新失败，回退使用本地缓存。")
            return cached.reset_index(drop=True)
        raise

    if not fetched.empty:
        fetched["trade_date"] = pd.to_datetime(fetched["trade_date"], format="%Y%m%d", errors="coerce")

    daily = pd.concat([cached, fetched], ignore_index=True)
    if "trade_date" in daily.columns:
        daily["trade_date"] = pd.to_datetime(daily["trade_date"], errors="coerce")
    for column in ["close", "adj_factor", "amount", "total_mv", "vol"]:
        if column in daily.columns:
            daily[column] = pd.to_numeric(daily[column], errors="coerce")
    if "close" in daily.columns and "adj_factor" in daily.columns:
        daily["forward_adj_close"] = daily["close"] * daily["adj_factor"]
    elif "close" in daily.columns:
        daily["forward_adj_close"] = pd.to_numeric(daily["close"], errors="coerce")
    if "amount" not in daily.columns and {"vol", "close"}.issubset(set(daily.columns)):
        daily["amount"] = pd.to_numeric(daily["vol"], errors="coerce") * pd.to_numeric(daily["close"], errors="coerce")
    daily = daily.sort_values("trade_date").drop_duplicates(subset=["trade_date"]).reset_index(drop=True)
    save_csv(daily, cache_path)
    return daily


def get_hk_daily_cache_status(
    ts_code: str,
    cache_target_date: pd.Timestamp,
) -> Tuple[bool, pd.Timestamp | None]:
    cache_path = HK_PRICE_DIR / f"{ts_code}.csv"
    cached = read_cached_csv(cache_path, date_columns=["trade_date"])
    if cached.empty or "trade_date" not in cached.columns:
        return False, None
    latest_cached = pd.to_datetime(cached["trade_date"], errors="coerce").max()
    if pd.isna(latest_cached):
        return False, None
    return pd.Timestamp(latest_cached) >= cache_target_date, pd.Timestamp(latest_cached)


def hk_daily_frame_covers_target(daily: pd.DataFrame, cache_target_date: pd.Timestamp) -> bool:
    if daily.empty or "trade_date" not in daily.columns:
        return False
    latest_cached = pd.to_datetime(daily["trade_date"], errors="coerce").max()
    if pd.isna(latest_cached):
        return False
    return pd.Timestamp(latest_cached).normalize() >= pd.Timestamp(cache_target_date).normalize()


def get_hk_cache_worker_daily_client(default_pro):
    if not TUSHARE_DAILY_TOKEN:
        return default_pro
    client = getattr(_HK_CACHE_WORKER_STATE, "pro_daily", None)
    if client is None:
        client = ts.pro_api(TUSHARE_DAILY_TOKEN)
        _HK_CACHE_WORKER_STATE.pro_daily = client
    return client


def prepare_single_hk_daily_cache(
    default_pro,
    ts_code: str,
    data_start_date: pd.Timestamp,
    end_date: pd.Timestamp,
) -> Tuple[str, pd.DataFrame]:
    worker_pro = get_hk_cache_worker_daily_client(default_pro)
    daily = load_or_fetch_hk_daily_adj(worker_pro, ts_code, data_start_date, end_date)
    return ts_code, daily


def append_hk_daily_frames(
    *,
    ts_code: str,
    daily: pd.DataFrame,
    price_frames: List[pd.DataFrame],
    mv_frames: List[pd.DataFrame],
    amount_frames: List[pd.DataFrame],
) -> None:
    price_frames.append(
        daily[["trade_date", "forward_adj_close"]]
        .rename(columns={"forward_adj_close": ts_code})
        .set_index("trade_date")
    )
    if "total_mv" in daily.columns:
        mv_frames.append(daily[["trade_date", "total_mv"]].rename(columns={"total_mv": ts_code}).set_index("trade_date"))
    if "amount" in daily.columns:
        amount_frames.append(daily[["trade_date", "amount"]].rename(columns={"amount": ts_code}).set_index("trade_date"))


def save_hk_prepare_progress(
    *,
    total_codes: int,
    fresh_codes: List[str],
    pending_codes: List[str],
    last_attempted: str | None,
    end_date: pd.Timestamp,
) -> None:
    HK_PROGRESS_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "end_date": end_date.strftime("%Y-%m-%d"),
        "total_codes": total_codes,
        "fresh_count": len(fresh_codes),
        "pending_count": len(pending_codes),
        "completion_ratio": len(fresh_codes) / total_codes if total_codes > 0 else 0.0,
        "last_attempted": last_attempted,
        "fresh_codes": fresh_codes,
        "pending_codes": pending_codes,
        "updated_at": pd.Timestamp.now(tz="Asia/Shanghai").isoformat(),
    }
    try:
        with open(HK_PROGRESS_PATH, "w", encoding="utf-8") as fp:
            json.dump(payload, fp, ensure_ascii=False, indent=2)
    except OSError as exc:
        print(f"[Warn] 无法写入港股准备进度文件 {HK_PROGRESS_PATH}: {exc}")


def build_hk_market_series(price_ffill: pd.DataFrame) -> pd.Series:
    daily_returns = price_ffill.pct_change().replace([np.inf, -np.inf], np.nan)
    ew_returns = daily_returns.mean(axis=1, skipna=True).fillna(0.0)
    return (1.0 + ew_returns).cumprod()


def get_factor_signal_dates(prepared: HKPreparedData) -> List[pd.Timestamp]:
    signal_dates = set(prepared.month_end_dates) | set(prepared.week_end_dates)
    if not prepared.price_ffill.empty:
        signal_dates.add(pd.Timestamp(prepared.price_ffill.index.max()))
    return sorted(signal_dates)


def get_rebalance_signal_dates(prepared: HKPreparedData, rebalance_frequency: str) -> List[pd.Timestamp]:
    freq = str(rebalance_frequency or "monthly").strip().lower()
    if freq == "weekly":
        return list(prepared.week_end_dates)
    if freq == "biweekly":
        return [date for idx, date in enumerate(prepared.week_end_dates) if idx % 2 == 1]
    return list(prepared.monthly_period_end_dates)


def get_next_trading_day(trading_dates: pd.Index, signal_date: pd.Timestamp) -> pd.Timestamp | None:
    position = int(trading_dates.searchsorted(signal_date, side="right"))
    if position >= len(trading_dates):
        return None
    return pd.Timestamp(trading_dates[position])


def compute_hk_factor_cache(prepared: HKPreparedData) -> HKFactorCache:
    month_end_price_panel = prepared.price_ffill.reindex(pd.Index(prepared.month_end_dates))
    month_end_index = pd.Index(prepared.month_end_dates)
    month_end_set = set(prepared.month_end_dates)

    eligible_codes_by_date: Dict[pd.Timestamp, List[str]] = {}
    signal_mvs_by_date: Dict[pd.Timestamp, pd.Series] = {}
    avg_daily_amount_by_date: Dict[pd.Timestamp, pd.Series] = {}
    amount_surge_ratio_by_date: Dict[pd.Timestamp, pd.Series] = {}
    recent_1m_returns_by_date: Dict[pd.Timestamp, pd.Series] = {}
    momentum_12_1_by_date: Dict[pd.Timestamp, pd.Series] = {}
    momentum_6_1_by_date: Dict[pd.Timestamp, pd.Series] = {}
    momentum_3_1_by_date: Dict[pd.Timestamp, pd.Series] = {}
    breakout_signal_by_date: Dict[pd.Timestamp, pd.Series] = {}
    liquidity_quality_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}
    low_vol_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}
    small_cap_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}

    for signal_date in get_factor_signal_dates(prepared):
        signal_prices = prepared.price_exact.loc[signal_date] if signal_date in prepared.price_exact.index else pd.Series(dtype=float)
        signal_mvs = prepared.total_mv.loc[signal_date] if signal_date in prepared.total_mv.index else pd.Series(dtype=float)

        eligible_codes: List[str] = []
        for ts_code, list_date in prepared.code_to_list_date.items():
            if pd.isna(list_date):
                continue
            if list_date > signal_date - pd.DateOffset(months=HK_MIN_LISTING_MONTHS):
                continue
            if ts_code not in signal_prices.index or pd.isna(signal_prices.get(ts_code)):
                continue
            if ts_code not in signal_mvs.index or pd.isna(signal_mvs.get(ts_code)):
                continue
            eligible_codes.append(ts_code)

        eligible_codes_by_date[signal_date] = eligible_codes
        signal_mvs_by_date[signal_date] = signal_mvs.reindex(eligible_codes).dropna().astype(float)

        amount_history = prepared.daily_amount.reindex(columns=eligible_codes).loc[:signal_date]
        liquidity_window = amount_history.tail(HK_ROLLING_AMOUNT_WINDOW)
        avg_daily_amount = liquidity_window.mean(skipna=True)
        prior_liquidity_window = amount_history.iloc[:-HK_ROLLING_AMOUNT_WINDOW].tail(HK_ROLLING_AMOUNT_WINDOW)
        prior_avg_daily_amount = prior_liquidity_window.mean(skipna=True)
        amount_surge_ratio = (avg_daily_amount / prior_avg_daily_amount.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)
        avg_daily_amount_by_date[signal_date] = avg_daily_amount
        amount_surge_ratio_by_date[signal_date] = amount_surge_ratio

        recent_1m_returns = pd.Series(dtype=float)
        momentum_12_1 = pd.Series(dtype=float)
        momentum_6_1 = pd.Series(dtype=float)
        momentum_3_1 = pd.Series(dtype=float)

        month_anchor_pos = int(month_end_index.searchsorted(signal_date, side="right")) - 1
        if month_anchor_pos >= 0:
            current_signal_prices = prepared.price_ffill.loc[signal_date, eligible_codes]
            if signal_date in month_end_set:
                current_signal_prices = month_end_price_panel.loc[signal_date, eligible_codes]
            if month_anchor_pos >= 1:
                prev_1m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes]
                valid_recent = prev_1m_prices.notna() & current_signal_prices.notna() & (prev_1m_prices > 0)
                if valid_recent.any():
                    recent_1m_returns = (current_signal_prices.loc[valid_recent] / prev_1m_prices.loc[valid_recent]) - 1.0
            if month_anchor_pos >= 12:
                prev_12m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 12], eligible_codes]
                compare_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes] if signal_date in month_end_set else current_signal_prices
                valid_12 = prev_12m_prices.notna() & compare_prices.notna() & (prev_12m_prices > 0)
                if valid_12.any():
                    momentum_12_1 = (compare_prices.loc[valid_12] / prev_12m_prices.loc[valid_12]) - 1.0
            if month_anchor_pos >= 6:
                prev_6m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 6], eligible_codes]
                compare_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes] if signal_date in month_end_set else current_signal_prices
                valid_6 = prev_6m_prices.notna() & compare_prices.notna() & (prev_6m_prices > 0)
                if valid_6.any():
                    momentum_6_1 = (compare_prices.loc[valid_6] / prev_6m_prices.loc[valid_6]) - 1.0
            if month_anchor_pos >= 3:
                prev_3m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 3], eligible_codes]
                compare_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes] if signal_date in month_end_set else current_signal_prices
                valid_3 = prev_3m_prices.notna() & compare_prices.notna() & (prev_3m_prices > 0)
                if valid_3.any():
                    momentum_3_1 = (compare_prices.loc[valid_3] / prev_3m_prices.loc[valid_3]) - 1.0

        recent_1m_returns_by_date[signal_date] = recent_1m_returns
        momentum_12_1_by_date[signal_date] = momentum_12_1
        momentum_6_1_by_date[signal_date] = momentum_6_1
        momentum_3_1_by_date[signal_date] = momentum_3_1

        breakout_signal = pd.Series(False, index=pd.Index(eligible_codes), dtype=bool)
        price_history = prepared.price_ffill.reindex(columns=eligible_codes).loc[:signal_date].tail(HK_BREAKOUT_LOOKBACK_DAYS + 1)
        if len(price_history) >= 2:
            prior_high = price_history.iloc[:-1].max()
            current_price = price_history.iloc[-1]
            breakout_signal = (current_price >= prior_high.fillna(np.inf) * 0.995).fillna(False)
        breakout_signal_by_date[signal_date] = breakout_signal

        returns_window = prepared.price_ffill.reindex(columns=eligible_codes).pct_change().loc[:signal_date].tail(HK_ROLLING_AMOUNT_WINDOW)
        vol_score = returns_window.std(ddof=1)
        low_vol_scores = safe_percentile_rank(vol_score, ascending=False)
        low_vol_scores_by_date[signal_date] = low_vol_scores

        liquidity_quality_scores = blend_ranked_components(
            [
                (safe_percentile_rank(signal_mvs_by_date[signal_date], ascending=True), 0.45),
                (safe_percentile_rank(avg_daily_amount, ascending=True), 0.35),
                (low_vol_scores, 0.20),
            ]
        )
        liquidity_quality_scores_by_date[signal_date] = liquidity_quality_scores
        small_cap_scores_by_date[signal_date] = safe_percentile_rank(signal_mvs_by_date[signal_date], ascending=False)

    return HKFactorCache(
        eligible_codes_by_date=eligible_codes_by_date,
        signal_mvs_by_date=signal_mvs_by_date,
        avg_daily_amount_by_date=avg_daily_amount_by_date,
        amount_surge_ratio_by_date=amount_surge_ratio_by_date,
        recent_1m_returns_by_date=recent_1m_returns_by_date,
        momentum_12_1_by_date=momentum_12_1_by_date,
        momentum_6_1_by_date=momentum_6_1_by_date,
        momentum_3_1_by_date=momentum_3_1_by_date,
        breakout_signal_by_date=breakout_signal_by_date,
        liquidity_quality_scores_by_date=liquidity_quality_scores_by_date,
        low_vol_scores_by_date=low_vol_scores_by_date,
        small_cap_scores_by_date=small_cap_scores_by_date,
    )


def prepare_hkconnect_data(
    pro_daily,
    pro_connect,
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
    *,
    max_new_codes: int | None = None,
    warm_cache_only: bool = False,
    sleep_between_codes: float = 0.0,
    max_runtime_minutes: float | None = None,
) -> HKPreparedData | None:
    started_at = time.monotonic()
    data_start_date = start_date - pd.DateOffset(months=HK_DATA_HISTORY_MONTHS)
    warnings: List[str] = []
    hk_basic = load_or_fetch_hk_basic(pro_daily)
    latest_connect = load_or_fetch_stock_hsgt_latest(pro_connect, end_date)
    connect_codes = sorted(latest_connect["ts_code"].astype(str).unique().tolist())
    connect_basic = hk_basic.loc[hk_basic["ts_code"].isin(connect_codes)].copy()
    if connect_basic.empty:
        raise RuntimeError("最新沪港通静态标的池为空，无法构建港股策略研究。")

    warnings.append(
        "沪港通历史标的列表受 Tushare stock_hsgt 接口限制（仅 2025-08-12 起可取），"
        "当前研究使用最新可得沪港通名单作为静态回测池。"
    )

    calendar = load_or_fetch_hk_trade_calendar(pro_daily, data_start_date, end_date)
    month_end_dates, month_start_dates, week_end_dates, full_calendar_index, monthly_period_end_dates = build_month_boundaries(
        calendar,
        formal_calendar=calendar,
    )
    now_local = pd.Timestamp.now(tz="Asia/Shanghai").tz_localize(None)
    today_local = now_local.normalize()
    if len(full_calendar_index) == 0:
        raise RuntimeError("港股交易日历为空，无法准备缓存。")
    if end_date.normalize() >= today_local:
        # Nightly runs happen after the HK close; use today's HK cache only after
        # the configured upstream data availability buffer has elapsed.
        hk_data_ready_at = today_local + HK_MARKET_CLOSE_TIME + HKCONNECT_DAILY_ADJ_READY_BUFFER
        hk_post_close_ready = now_local >= hk_data_ready_at
        if hk_post_close_ready:
            eligible_cache_dates = [date for date in full_calendar_index if date <= today_local]
        else:
            eligible_cache_dates = [date for date in full_calendar_index if date < today_local]
        cache_target_date = eligible_cache_dates[-1] if eligible_cache_dates else full_calendar_index[-1]
    else:
        eligible_cache_dates = [date for date in full_calendar_index if date <= end_date.normalize()]
        cache_target_date = eligible_cache_dates[-1] if eligible_cache_dates else full_calendar_index[-1]
    full_calendar_index = [date for date in full_calendar_index if date <= cache_target_date]
    month_end_dates = [date for date in month_end_dates if date <= cache_target_date]
    monthly_period_end_dates = [date for date in monthly_period_end_dates if date <= cache_target_date]
    month_start_dates = [date for date in month_start_dates if date <= cache_target_date]
    week_end_dates = [date for date in week_end_dates if date <= cache_target_date]
    if len(full_calendar_index) == 0:
        raise RuntimeError("港股可用交易日历为空，无法准备缓存。")

    price_frames: List[pd.DataFrame] = []
    mv_frames: List[pd.DataFrame] = []
    amount_frames: List[pd.DataFrame] = []
    fresh_codes: List[str] = []
    pending_codes: List[str] = []
    new_fetch_count = 0
    stopped_early = False
    last_attempted: str | None = None
    can_parallel_refresh = (
        max_new_codes is None
        and sleep_between_codes <= 0
        and max_runtime_minutes is None
    )

    if can_parallel_refresh:
        stale_codes: List[Tuple[int, str]] = []
        for idx, ts_code in enumerate(connect_codes, start=1):
            is_fresh, _latest_cached = get_hk_daily_cache_status(ts_code, cache_target_date)
            if is_fresh:
                fresh_codes.append(ts_code)
                if not warm_cache_only:
                    daily = read_cached_csv(HK_PRICE_DIR / f"{ts_code}.csv", date_columns=["trade_date"])
                    if not daily.empty and "forward_adj_close" in daily.columns:
                        append_hk_daily_frames(
                            ts_code=ts_code,
                            daily=daily,
                            price_frames=price_frames,
                            mv_frames=mv_frames,
                            amount_frames=amount_frames,
                        )
                continue
            stale_codes.append((idx, ts_code))

        if stale_codes:
            worker_count = min(CACHE_REFRESH_MAX_WORKERS, len(stale_codes))
            print(f"[HK Data] 使用 {worker_count} 个 worker 并行准备 {len(stale_codes)} 只待更新股票缓存。")
            with ThreadPoolExecutor(max_workers=worker_count) as executor:
                futures = {
                    executor.submit(prepare_single_hk_daily_cache, pro_daily, ts_code, data_start_date, end_date): (idx, ts_code)
                    for idx, ts_code in stale_codes
                }
                for completed, future in enumerate(as_completed(futures), start=1):
                    _idx, ts_code = futures[future]
                    last_attempted = ts_code
                    try:
                        code, daily = future.result()
                        new_fetch_count += 1
                    except RuntimeError as exc:
                        pending_codes.append(ts_code)
                        stopped_early = True
                        if any(keyword in str(exc) for keyword in ["频率限制", "频率超限", "每分钟最多访问", "每小时最多访问"]):
                            warnings.append(f"{ts_code} 触发 hk_daily_adj 频率限制，本轮先停止，后续可继续断点续跑。")
                            continue
                        raise
                    if not hk_daily_frame_covers_target(daily, cache_target_date):
                        pending_codes.append(code)
                        stopped_early = True
                        warnings.append(f"{code} hk_daily_adj 未覆盖目标交易日 {cache_target_date.date()}，本轮不使用 stale 缓存回测。")
                        continue
                    if daily.empty:
                        warnings.append(f"{code} 缺少 hk_daily_adj 数据，已跳过。")
                        continue
                    if "forward_adj_close" not in daily.columns:
                        warnings.append(f"{code} 无法构造前复权价格，已跳过。")
                        continue
                    fresh_codes.append(code)
                    if not warm_cache_only:
                        append_hk_daily_frames(
                            ts_code=code,
                            daily=daily,
                            price_frames=price_frames,
                            mv_frames=mv_frames,
                            amount_frames=amount_frames,
                        )
                    print(f"[HK Data] ({completed}/{len(stale_codes)}) 已完成 {code}")

    else:
        for idx, ts_code in enumerate(connect_codes, start=1):
            is_fresh, _latest_cached = get_hk_daily_cache_status(ts_code, cache_target_date)
            if is_fresh:
                fresh_codes.append(ts_code)
                if not warm_cache_only:
                    daily = read_cached_csv(HK_PRICE_DIR / f"{ts_code}.csv", date_columns=["trade_date"])
                    if not daily.empty and "forward_adj_close" in daily.columns:
                        append_hk_daily_frames(
                            ts_code=ts_code,
                            daily=daily,
                            price_frames=price_frames,
                            mv_frames=mv_frames,
                            amount_frames=amount_frames,
                        )
                continue
            if max_new_codes is not None and new_fetch_count >= max_new_codes:
                pending_codes.append(ts_code)
                stopped_early = True
                continue
            if max_runtime_minutes is not None and (time.monotonic() - started_at) >= max_runtime_minutes * 60.0:
                pending_codes.append(ts_code)
                stopped_early = True
                warnings.append(
                    f"达到本轮最长运行时间 {max_runtime_minutes:.1f} 分钟，已停止并保留进度。"
                )
                break
            print(f"[HK Data] ({idx}/{len(connect_codes)}) 正在准备 {ts_code}")
            last_attempted = ts_code
            try:
                daily = load_or_fetch_hk_daily_adj(pro_daily, ts_code, data_start_date, end_date)
                new_fetch_count += 1
            except RuntimeError as exc:
                pending_codes.append(ts_code)
                stopped_early = True
                if any(keyword in str(exc) for keyword in ["频率限制", "频率超限", "每分钟最多访问", "每小时最多访问"]):
                    warnings.append(f"{ts_code} 触发 hk_daily_adj 频率限制，本轮先停止，后续可继续断点续跑。")
                    break
                raise
            if not hk_daily_frame_covers_target(daily, cache_target_date):
                pending_codes.append(ts_code)
                stopped_early = True
                warnings.append(f"{ts_code} hk_daily_adj 未覆盖目标交易日 {cache_target_date.date()}，本轮不使用 stale 缓存回测。")
                continue
            if daily.empty:
                warnings.append(f"{ts_code} 缺少 hk_daily_adj 数据，已跳过。")
                continue
            if "forward_adj_close" not in daily.columns:
                warnings.append(f"{ts_code} 无法构造前复权价格，已跳过。")
                continue
            fresh_codes.append(ts_code)
            append_hk_daily_frames(
                ts_code=ts_code,
                daily=daily,
                price_frames=price_frames,
                mv_frames=mv_frames,
                amount_frames=amount_frames,
            )
            if sleep_between_codes > 0 and new_fetch_count < len(connect_codes):
                print(f"[HK Warmup] {ts_code} 完成，等待 {sleep_between_codes:.0f} 秒后继续下一只。")
                time.sleep(sleep_between_codes)

    for ts_code in connect_codes:
        if ts_code not in fresh_codes and ts_code not in pending_codes:
            pending_codes.append(ts_code)
    save_hk_prepare_progress(
        total_codes=len(connect_codes),
        fresh_codes=sorted(set(fresh_codes)),
        pending_codes=sorted(set(pending_codes)),
        last_attempted=last_attempted,
        end_date=end_date,
    )

    if warm_cache_only:
        print(
            f"[HK Warmup] 已完成 {len(set(fresh_codes))}/{len(connect_codes)} 只股票缓存，"
            f"剩余 {len(set(pending_codes))} 只。进度文件：{HK_PROGRESS_PATH}"
        )
        return None

    if stopped_early and len(set(fresh_codes)) < len(connect_codes):
        raise RuntimeError(
            f"港股缓存尚未准备完成：已完成 {len(set(fresh_codes))}/{len(connect_codes)} 只，"
            f"剩余 {len(set(pending_codes))} 只。请继续运行 backtest_hkconnect.py 断点续跑，"
            f"或先用 --warm-cache-only 预热缓存。进度文件：{HK_PROGRESS_PATH}"
        )

    if not price_frames:
        raise RuntimeError("沪港通静态池没有可用价格数据，无法回测。")

    calendar = extend_hk_calendar_with_cached_price_dates(calendar, price_frames, data_start_date, cache_target_date)
    month_end_dates, month_start_dates, week_end_dates, full_calendar_index, monthly_period_end_dates = build_month_boundaries(
        calendar,
        formal_calendar=calendar,
    )
    full_calendar_index = [date for date in full_calendar_index if date <= cache_target_date]
    month_end_dates = [date for date in month_end_dates if date <= cache_target_date]
    monthly_period_end_dates = [date for date in monthly_period_end_dates if date <= cache_target_date]
    month_start_dates = [date for date in month_start_dates if date <= cache_target_date]
    week_end_dates = [date for date in week_end_dates if date <= cache_target_date]
    if len(full_calendar_index) == 0:
        raise RuntimeError("港股缓存价格日期无法构造交易日历，无法准备缓存。")

    price_exact = pd.concat(price_frames, axis=1).sort_index()
    price_exact = price_exact.reindex(full_calendar_index)
    price_ffill = price_exact.ffill()
    total_mv = pd.concat(mv_frames, axis=1).sort_index().reindex(full_calendar_index).ffill() if mv_frames else pd.DataFrame(index=full_calendar_index)
    daily_amount = pd.concat(amount_frames, axis=1).sort_index().reindex(full_calendar_index).ffill() if amount_frames else pd.DataFrame(index=full_calendar_index)

    market_daily = build_hk_market_series(price_ffill)
    market_monthly_close = market_daily.reindex(month_end_dates).dropna()
    market_weekly_close = market_daily.reindex(week_end_dates).dropna()

    connect_basic = connect_basic.loc[connect_basic["ts_code"].isin(price_ffill.columns)].copy()
    code_to_name = dict(zip(connect_basic["ts_code"], connect_basic["name"]))
    code_to_list_date = dict(zip(connect_basic["ts_code"], pd.to_datetime(connect_basic["list_date"], errors="coerce")))

    prepared = HKPreparedData(
        stock_basic=hk_basic,
        connect_basic=connect_basic,
        price_exact=price_exact,
        price_ffill=price_ffill,
        total_mv=total_mv,
        daily_amount=daily_amount,
        month_end_dates=month_end_dates,
        monthly_period_end_dates=monthly_period_end_dates,
        month_start_dates=month_start_dates,
        week_end_dates=week_end_dates,
        code_to_name=code_to_name,
        code_to_list_date=code_to_list_date,
        market_monthly_close=market_monthly_close,
        market_weekly_close=market_weekly_close,
        data_warnings=warnings,
        factor_cache=None,  # type: ignore[arg-type]
    )
    prepared.factor_cache = compute_hk_factor_cache(prepared)
    return prepared


def build_hk_signal_scores(prepared: HKPreparedData, signal_date: pd.Timestamp, signal_family: str) -> pd.Series:
    factor_cache = prepared.factor_cache
    momentum_12_1 = factor_cache.momentum_12_1_by_date.get(signal_date, pd.Series(dtype=float))
    momentum_6_1 = factor_cache.momentum_6_1_by_date.get(signal_date, pd.Series(dtype=float))
    momentum_3_1 = factor_cache.momentum_3_1_by_date.get(signal_date, pd.Series(dtype=float))
    amount_surge_ratio = factor_cache.amount_surge_ratio_by_date.get(signal_date, pd.Series(dtype=float))
    breakout_signal = factor_cache.breakout_signal_by_date.get(signal_date, pd.Series(dtype=bool))
    liquidity_quality = factor_cache.liquidity_quality_scores_by_date.get(signal_date, pd.Series(dtype=float))
    low_vol_scores = factor_cache.low_vol_scores_by_date.get(signal_date, pd.Series(dtype=float))
    small_cap_scores = factor_cache.small_cap_scores_by_date.get(signal_date, pd.Series(dtype=float))
    recent_1m = factor_cache.recent_1m_returns_by_date.get(signal_date, pd.Series(dtype=float))

    if signal_family == "path1_lowvol":
        return blend_ranked_components(
            [
                (safe_percentile_rank(momentum_12_1, ascending=True), 0.35),
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.20),
                (liquidity_quality, 0.20),
                (low_vol_scores, 0.25),
            ]
        )
    if signal_family == "path2_breakout":
        return blend_ranked_components(
            [
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.35),
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.20),
                (breakout_signal.astype(float), 0.20),
                (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.15),
                (safe_percentile_rank(recent_1m, ascending=True), 0.10),
            ]
        )
    if signal_family == "path2_theme":
        return blend_ranked_components(
            [
                (safe_percentile_rank(momentum_12_1, ascending=True), 0.30),
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.25),
                (liquidity_quality, 0.20),
                (breakout_signal.astype(float), 0.10),
                (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.10),
                (low_vol_scores, 0.05),
            ]
        )
    if signal_family == "path2_elastic":
        return blend_ranked_components(
            [
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.30),
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.20),
                (small_cap_scores, 0.20),
                (breakout_signal.astype(float), 0.10),
                (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.10),
                (safe_percentile_rank(recent_1m, ascending=True), 0.10),
            ]
        )
    return blend_ranked_components(
        [
            (safe_percentile_rank(momentum_12_1, ascending=True), 0.40),
            (safe_percentile_rank(momentum_6_1, ascending=True), 0.20),
            (liquidity_quality, 0.25),
            (low_vol_scores, 0.15),
        ]
    )


def build_hk_base_weights(
    prepared: HKPreparedData,
    signal_date: pd.Timestamp,
    eligible_codes: List[str],
    base_weight_method: str,
) -> pd.Series:
    if base_weight_method == "equal_weight":
        return pd.Series(1.0, index=pd.Index(eligible_codes, name="ts_code"), dtype=float)
    signal_mvs = prepared.factor_cache.signal_mvs_by_date.get(signal_date, pd.Series(dtype=float)).reindex(eligible_codes).dropna()
    if base_weight_method == "inverse_mv":
        inv = 1.0 / signal_mvs.replace(0.0, np.nan)
        inv = inv.replace([np.inf, -np.inf], np.nan).dropna()
        return inv
    return signal_mvs


def build_hk_month_end_preview_payload(
    *,
    prepared: HKPreparedData,
    strategy_config: Dict[str, object],
    signal_date: pd.Timestamp,
    formal_signal_date: pd.Timestamp | None,
    positions: pd.Series,
) -> Dict[str, object] | None:
    eligible_codes = prepared.factor_cache.eligible_codes_by_date.get(signal_date, [])
    if not eligible_codes:
        return None
    signal_scores = build_hk_signal_scores(prepared, signal_date, str(strategy_config["signal_family"]))
    base_weights = build_hk_base_weights(prepared, signal_date, eligible_codes, str(strategy_config["base_weight_method"]))
    recent_1m_returns = prepared.factor_cache.recent_1m_returns_by_date.get(signal_date, pd.Series(dtype=float))
    quality_scores = prepared.factor_cache.liquidity_quality_scores_by_date.get(signal_date, pd.Series(dtype=float))
    breakout_signal = prepared.factor_cache.breakout_signal_by_date.get(signal_date, pd.Series(dtype=bool))
    market_close = prepared.market_monthly_close.copy()
    if signal_date not in market_close.index:
        market_daily = build_hk_market_series(prepared.price_ffill)
        if signal_date in market_daily.index:
            market_close.loc[signal_date] = float(market_daily.loc[signal_date])
        elif signal_date in prepared.market_weekly_close.index:
            market_close.loc[signal_date] = float(prepared.market_weekly_close.loc[signal_date])
        market_close = market_close.sort_index()
    regime = compute_market_exposure(
        market_close,
        signal_date,
        risk_off_rule=str(strategy_config.get("risk_off_rule", "or")),
        risk_staging_mode=str(strategy_config.get("risk_staging_mode", "three_stage")),
        core_risk_off_exposure=float(strategy_config.get("risk_off_exposure", 0.6)),
        core_risk_on_exposure=float(strategy_config.get("risk_on_exposure", 1.0)),
        core_caution_exposure=float(strategy_config.get("risk_caution_exposure", 0.85)),
        satellite_risk_off_exposure=float(strategy_config.get("risk_off_exposure", 0.6)),
        satellite_risk_on_exposure=float(strategy_config.get("risk_on_exposure", 1.0)),
        satellite_caution_exposure=float(strategy_config.get("risk_caution_exposure", 0.85)),
        momentum_lookback=MONTHLY_MOMENTUM_LOOKBACK,
        momentum_skip=MONTHLY_MOMENTUM_SKIP,
        ma_lookback=MONTHLY_MA_LOOKBACK,
    )
    raw_target_weights, selection_stats = build_single_sleeve_weights(
        base_weights=base_weights,
        signal_scores=signal_scores,
        recent_1m_returns=recent_1m_returns,
        quality_scores=quality_scores,
        currently_held_codes=set(positions.index),
        target_exposure=float(regime["portfolio_target_exposure"]),
        buy_entry_percentile=float(strategy_config["buy_entry_percentile"]),
        sell_exit_percentile=float(strategy_config["sell_exit_percentile"]),
        quality_quantile=0.50,
        max_holdings=int(strategy_config["max_holdings"]),
        require_breakout_for_buy=str(strategy_config["signal_family"]).startswith("path2_breakout"),
        breakout_signal=breakout_signal,
        base_weight_mode=strategy_config.get("base_weight_mode", "base"),
    )
    target_weights, target_cash_weight = apply_weight_cap_with_redistribution(
        raw_target_weights,
        cap=float(strategy_config.get("weight_cap", HK_WEIGHT_CAP)),
    )
    price_row = prepared.price_ffill.loc[signal_date] if signal_date in prepared.price_ffill.index else pd.Series(dtype=float)
    holdings: List[Dict[str, object]] = []
    for ts_code, weight in target_weights.sort_values(ascending=False).items():
        latest_price = price_row.get(ts_code, np.nan)
        holdings.append(
            {
                "ts_code": str(ts_code),
                "name": str(prepared.code_to_name.get(str(ts_code), "")),
                "weight": float(weight),
                "latest_price": float(latest_price) if pd.notna(latest_price) else None,
            }
        )
    if target_cash_weight > 1e-12:
        holdings.append({"ts_code": "CASH", "name": "现金", "weight": float(target_cash_weight), "latest_price": None})
    return {
        "mode": "month_end_preview",
        "status": "available",
        "preview_as_of": signal_date.strftime("%Y-%m-%d"),
        "formal_signal_date": formal_signal_date.strftime("%Y-%m-%d") if formal_signal_date is not None else None,
        "note": "月中观察口径：使用当日收盘数据模拟“如果今天是月末”的沪港通候选组合，不进入正式回测收益或 winner 规则。",
        "target_total_exposure": float(max(0.0, 1.0 - target_cash_weight)),
        "risk_state": str(regime.get("risk_stage") or ("risk_off" if regime.get("risk_off") else "risk_on")),
        "market_momentum": float(regime["market_12_1_momentum"]) if pd.notna(regime.get("market_12_1_momentum")) else None,
        "selected_count": int(len(target_weights)),
        "selection_counts": {
            key: int(value)
            for key, value in selection_stats.items()
            if key.endswith("_count") and isinstance(value, (int, np.integer))
        },
        "holdings": holdings,
    }


def build_hk_portfolio_overlay_target_weights(base_weights: pd.Series, target_exposure: float, weight_cap: float) -> pd.Series:
    weights = base_weights.astype(float).replace([np.inf, -np.inf], np.nan).dropna()
    weights = weights[weights > 0]
    if weights.empty:
        return pd.Series(dtype=float)
    target_exposure = min(1.0, max(0.0, float(target_exposure)))
    if target_exposure <= 0:
        return pd.Series(dtype=float)
    normalized = weights / float(weights.sum())
    capped, _cash = apply_weight_cap_with_redistribution(normalized * target_exposure, cap=float(weight_cap))
    return capped


def apply_hk_weekly_portfolio_overlay(
    *,
    prepared: HKPreparedData,
    positions: pd.Series,
    cash_value: float,
    gross_positions: pd.Series,
    gross_cash_value: float,
    rebalance_date: pd.Timestamp,
    period_end: pd.Timestamp,
    base_target_weights: pd.Series,
    strategy_config: Dict[str, object],
) -> Tuple[pd.Series, float, pd.Series, float, List[Dict[str, object]], Dict[str, float]]:
    risk_frequency = str(strategy_config.get("risk_evaluation_frequency", HK_RISK_EVAL_FREQUENCY_MONTHLY) or HK_RISK_EVAL_FREQUENCY_MONTHLY)
    overlay_scope = str(strategy_config.get("risk_overlay_scope", "") or "")
    if risk_frequency != HK_RISK_EVAL_FREQUENCY_WEEKLY or overlay_scope != HK_RISK_OVERLAY_SCOPE_PORTFOLIO:
        return positions, cash_value, gross_positions, gross_cash_value, [], {
            "weekly_overlay_trade_count": 0,
            "weekly_overlay_trading_cost": 0.0,
            "weekly_overlay_avg_one_way_turnover": 0.0,
        }

    overlay_dates = [date for date in prepared.week_end_dates if rebalance_date < date < period_end]
    if not overlay_dates or base_target_weights.empty:
        if not positions.empty:
            rebalance_prices = prepared.price_ffill.loc[rebalance_date, positions.index]
            period_end_prices = prepared.price_ffill.loc[period_end, positions.index]
            positions = positions * (period_end_prices / rebalance_prices)
        if not gross_positions.empty:
            gross_rebalance_prices = prepared.price_ffill.loc[rebalance_date, gross_positions.index]
            gross_period_end_prices = prepared.price_ffill.loc[period_end, gross_positions.index]
            gross_positions = gross_positions * (gross_period_end_prices / gross_rebalance_prices)
        return positions, cash_value, gross_positions, gross_cash_value, [], {
            "weekly_overlay_trade_count": 0,
            "weekly_overlay_trading_cost": 0.0,
            "weekly_overlay_avg_one_way_turnover": 0.0,
        }

    trading_dates = prepared.price_ffill.index
    overlay_rows: List[Dict[str, object]] = []
    overlay_turnovers: List[float] = []
    overlay_count = 0
    cumulative_cost = 0.0
    prev_date = rebalance_date

    for overlay_date in overlay_dates:
        overlay_trade_date = get_next_trading_day(trading_dates, overlay_date)
        if overlay_trade_date is None or overlay_trade_date > period_end or overlay_trade_date <= prev_date:
            continue

        if not positions.empty:
            prices_prev = prepared.price_ffill.loc[prev_date, positions.index]
            prices_now = prepared.price_ffill.loc[overlay_trade_date, positions.index]
            positions = positions * (prices_now / prices_prev)
        if not gross_positions.empty:
            gross_prices_prev = prepared.price_ffill.loc[prev_date, gross_positions.index]
            gross_prices_now = prepared.price_ffill.loc[overlay_trade_date, gross_positions.index]
            gross_positions = gross_positions * (gross_prices_now / gross_prices_prev)

        regime = compute_market_exposure(
            prepared.market_weekly_close,
            overlay_date,
            risk_off_rule=str(strategy_config.get("risk_off_rule", "or")),
            risk_staging_mode=str(strategy_config.get("risk_staging_mode", "three_stage")),
            core_risk_off_exposure=float(strategy_config.get("risk_off_exposure", 0.6)),
            core_risk_on_exposure=float(strategy_config.get("risk_on_exposure", 1.0)),
            core_caution_exposure=float(strategy_config.get("risk_caution_exposure", 0.85)),
            satellite_risk_off_exposure=float(strategy_config.get("risk_off_exposure", 0.6)),
            satellite_risk_on_exposure=float(strategy_config.get("risk_on_exposure", 1.0)),
            satellite_caution_exposure=float(strategy_config.get("risk_caution_exposure", 0.85)),
            momentum_lookback=WEEKLY_MOMENTUM_LOOKBACK,
            momentum_skip=WEEKLY_MOMENTUM_SKIP,
            ma_lookback=WEEKLY_MA_LOOKBACK,
        )
        target_weights = build_hk_portfolio_overlay_target_weights(
            base_target_weights,
            target_exposure=float(regime["portfolio_target_exposure"]),
            weight_cap=float(strategy_config.get("weight_cap", HK_WEIGHT_CAP)),
        )

        tradable_codes: Iterable[str] = []
        if overlay_trade_date in prepared.price_exact.index:
            exact_prices = prepared.price_exact.loc[overlay_trade_date]
            tradable_codes = exact_prices[exact_prices.notna()].index.tolist()

        positions, cash_value, _, _, trade_stats = compute_rebalance_trades(
            current_values=positions,
            current_cash=cash_value,
            target_weights=target_weights,
            rebalance_date=overlay_trade_date,
            tradable_codes=tradable_codes,
            buy_commission=HK_BUY_COMMISSION,
            sell_commission_rate=HK_SELL_COMMISSION,
            stamp_rate_override=0.0,
        )
        gross_positions, gross_cash_value, _, _, _ = compute_rebalance_trades(
            current_values=gross_positions,
            current_cash=gross_cash_value,
            target_weights=target_weights,
            rebalance_date=overlay_trade_date,
            tradable_codes=tradable_codes,
            buy_commission=0.0,
            sell_commission_rate=0.0,
            stamp_rate_override=0.0,
        )
        if trade_stats["two_way_turnover"] > 1e-12:
            overlay_count += 1
            cumulative_cost += float(trade_stats["trading_cost"])
            overlay_turnovers.append(float(trade_stats["one_way_turnover"]))

        trade_details = []
        for detail in trade_stats.get("trade_details", []):
            detail_row = dict(detail)
            ts_code = str(detail_row.get("ts_code") or "")
            detail_row["name"] = prepared.code_to_name.get(ts_code, "")
            trade_details.append(detail_row)
        overlay_rows.append(
            {
                "date": overlay_date,
                "signal_date": overlay_date,
                "evaluation_date": overlay_date,
                "trade_date": overlay_trade_date,
                "one_way_turnover": trade_stats["one_way_turnover"],
                "two_way_turnover": trade_stats["two_way_turnover"],
                "buy_amount": trade_stats["buy_amount"],
                "sell_amount": trade_stats["sell_amount"],
                "trading_cost": trade_stats["trading_cost"],
                "buy_cost": trade_stats["buy_cost"],
                "sell_commission": trade_stats["sell_commission"],
                "sell_stamp_duty": trade_stats["sell_stamp_duty"],
                "event_type": "weekly_portfolio_overlay",
                "risk_stage": str(regime["risk_stage"]),
                "trade_details_json": json.dumps(trade_details, ensure_ascii=False) if trade_details else "",
            }
        )
        prev_date = overlay_trade_date

    if not positions.empty:
        final_prev = prepared.price_ffill.loc[prev_date, positions.index]
        final_now = prepared.price_ffill.loc[period_end, positions.index]
        positions = positions * (final_now / final_prev)
    if not gross_positions.empty:
        gross_final_prev = prepared.price_ffill.loc[prev_date, gross_positions.index]
        gross_final_now = prepared.price_ffill.loc[period_end, gross_positions.index]
        gross_positions = gross_positions * (gross_final_now / gross_final_prev)

    return positions, cash_value, gross_positions, gross_cash_value, overlay_rows, {
        "weekly_overlay_trade_count": overlay_count,
        "weekly_overlay_trading_cost": cumulative_cost,
        "weekly_overlay_avg_one_way_turnover": float(np.mean(overlay_turnovers)) if overlay_turnovers else 0.0,
    }


def run_hk_backtest(
    prepared: HKPreparedData,
    strategy_config: Dict[str, object],
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, Dict[str, object]]:
    requested_sample_start = pd.Timestamp(strategy_config["sample_start"])
    sample_start = requested_sample_start
    sample_tag = str(strategy_config["sample_tag"])
    sample_label = str(strategy_config["sample_label"])
    sample_short_label = str(strategy_config["sample_short_label"])
    rebalance_frequency = str(strategy_config.get("rebalance_frequency", "monthly") or "monthly").strip().lower()
    risk_evaluation_frequency = str(
        strategy_config.get("risk_evaluation_frequency", rebalance_frequency) or rebalance_frequency
    ).strip().lower()
    risk_overlay_scope = str(strategy_config.get("risk_overlay_scope", "") or "")
    weekly_portfolio_overlay_enabled = (
        risk_evaluation_frequency == HK_RISK_EVAL_FREQUENCY_WEEKLY
        and risk_overlay_scope == HK_RISK_OVERLAY_SCOPE_PORTFOLIO
    )
    signal_schedule = get_rebalance_signal_dates(prepared, rebalance_frequency)
    trading_dates = prepared.price_ffill.index

    if len(signal_schedule) < 2:
        raise RuntimeError("港股交易日历不足以构造回测。")

    report_start_idx = None
    for idx in range(len(signal_schedule) - 1):
        if signal_schedule[idx] >= sample_start:
            report_start_idx = idx
            break
    if report_start_idx is None:
        raise RuntimeError("设定的回测起点晚于当前可用调仓数据。")

    positions = pd.Series(dtype=float)
    cash_value = 1.0
    nav_at_signal_date = 1.0
    warnings = list(prepared.data_warnings)
    monthly_rows: List[Dict[str, object]] = []
    turnover_rows: List[Dict[str, object]] = []
    weights_history_rows: List[Dict[str, object]] = []
    equity_rows: List[Dict[str, object]] = []
    effective_sample_start: pd.Timestamp | None = None

    for idx in range(report_start_idx, len(signal_schedule) - 1):
        signal_date = signal_schedule[idx]
        period_end = signal_schedule[idx + 1]
        rebalance_date = get_next_trading_day(trading_dates, signal_date)
        if rebalance_date is None or rebalance_date > period_end:
            continue

        eligible_codes = prepared.factor_cache.eligible_codes_by_date.get(signal_date, [])
        if not eligible_codes:
            continue

        if effective_sample_start is None:
            effective_sample_start = pd.Timestamp(rebalance_date)
            if effective_sample_start > requested_sample_start:
                warnings.append(
                    "回测起点被后移："
                    f"requested={requested_sample_start.strftime('%Y-%m-%d')} "
                    f"effective={effective_sample_start.strftime('%Y-%m-%d')} "
                    "(受可用调仓点/数据覆盖影响)"
                )
            equity_rows.append(
                {
                    "date": effective_sample_start,
                    "portfolio_return": 0.0,
                    "nav": nav_at_signal_date,
                    "drawdown": 0.0,
                    "trading_cost": 0.0,
                }
            )

        signal_scores = build_hk_signal_scores(prepared, signal_date, str(strategy_config["signal_family"]))
        base_weights = build_hk_base_weights(prepared, signal_date, eligible_codes, str(strategy_config["base_weight_method"]))
        recent_1m_returns = prepared.factor_cache.recent_1m_returns_by_date.get(signal_date, pd.Series(dtype=float))
        quality_scores = prepared.factor_cache.liquidity_quality_scores_by_date.get(signal_date, pd.Series(dtype=float))
        breakout_signal = prepared.factor_cache.breakout_signal_by_date.get(signal_date, pd.Series(dtype=bool))

        market_close = prepared.market_monthly_close if rebalance_frequency == "monthly" else prepared.market_weekly_close
        regime = compute_market_exposure(
            market_close,
            signal_date,
            risk_off_rule=str(strategy_config.get("risk_off_rule", "or")),
            risk_staging_mode=str(strategy_config.get("risk_staging_mode", "three_stage")),
            core_risk_off_exposure=float(strategy_config.get("risk_off_exposure", 0.6)),
            core_risk_on_exposure=float(strategy_config.get("risk_on_exposure", 1.0)),
            core_caution_exposure=float(strategy_config.get("risk_caution_exposure", 0.85)),
            satellite_risk_off_exposure=float(strategy_config.get("risk_off_exposure", 0.6)),
            satellite_risk_on_exposure=float(strategy_config.get("risk_on_exposure", 1.0)),
            satellite_caution_exposure=float(strategy_config.get("risk_caution_exposure", 0.85)),
            momentum_lookback=MONTHLY_MOMENTUM_LOOKBACK if rebalance_frequency == "monthly" else WEEKLY_MOMENTUM_LOOKBACK,
            momentum_skip=MONTHLY_MOMENTUM_SKIP if rebalance_frequency == "monthly" else WEEKLY_MOMENTUM_SKIP,
            ma_lookback=MONTHLY_MA_LOOKBACK if rebalance_frequency == "monthly" else WEEKLY_MA_LOOKBACK,
        )
        target_exposure = float(regime["portfolio_target_exposure"])
        currently_held_codes = set(positions.index)
        raw_target_weights, selection_stats = build_single_sleeve_weights(
            base_weights=base_weights,
            signal_scores=signal_scores,
            recent_1m_returns=recent_1m_returns,
            quality_scores=quality_scores,
            currently_held_codes=currently_held_codes,
            target_exposure=target_exposure,
            buy_entry_percentile=float(strategy_config["buy_entry_percentile"]),
            sell_exit_percentile=float(strategy_config["sell_exit_percentile"]),
            quality_quantile=0.50,
            max_holdings=int(strategy_config["max_holdings"]),
            require_breakout_for_buy=str(strategy_config["signal_family"]).startswith("path2_breakout"),
            breakout_signal=breakout_signal,
            base_weight_mode=str(strategy_config.get("base_weight_mode", "base")),
        )
        target_weights, target_cash_weight = apply_weight_cap_with_redistribution(
            raw_target_weights, cap=float(strategy_config.get("weight_cap", HK_WEIGHT_CAP))
        )
        base_overlay_target_weights = target_weights
        if weekly_portfolio_overlay_enabled:
            full_raw_target_weights, _full_selection_stats = build_single_sleeve_weights(
                base_weights=base_weights,
                signal_scores=signal_scores,
                recent_1m_returns=recent_1m_returns,
                quality_scores=quality_scores,
                currently_held_codes=currently_held_codes,
                target_exposure=1.0,
                buy_entry_percentile=float(strategy_config["buy_entry_percentile"]),
                sell_exit_percentile=float(strategy_config["sell_exit_percentile"]),
                quality_quantile=0.50,
                max_holdings=int(strategy_config["max_holdings"]),
                require_breakout_for_buy=str(strategy_config["signal_family"]).startswith("path2_breakout"),
                breakout_signal=breakout_signal,
                base_weight_mode=str(strategy_config.get("base_weight_mode", "base")),
            )
            base_overlay_target_weights, _overlay_cash = apply_weight_cap_with_redistribution(
                full_raw_target_weights,
                cap=float(strategy_config.get("weight_cap", HK_WEIGHT_CAP)),
            )

        nav_at_signal_date = float(positions.sum() + cash_value)
        if not positions.empty:
            current_price_rebalance = prepared.price_ffill.loc[rebalance_date, positions.index]
            signal_price_for_positions = prepared.price_ffill.loc[signal_date, positions.index]
            positions = positions * (current_price_rebalance / signal_price_for_positions)

        tradable_codes: Iterable[str] = []
        if rebalance_date in prepared.price_exact.index:
            exact_rebalance_prices = prepared.price_exact.loc[rebalance_date]
            tradable_codes = exact_rebalance_prices[exact_rebalance_prices.notna()].index.tolist()

        positions, cash_value, gross_positions, gross_cash_value, trade_stats = compute_rebalance_trades(
            current_values=positions,
            current_cash=cash_value,
            target_weights=target_weights,
            rebalance_date=rebalance_date,
            tradable_codes=tradable_codes,
            buy_commission=HK_BUY_COMMISSION,
            sell_commission_rate=HK_SELL_COMMISSION,
            stamp_rate_override=0.0,
        )

        positions, cash_value, gross_positions, gross_cash_value, weekly_overlay_turnover_rows, weekly_overlay_stats = apply_hk_weekly_portfolio_overlay(
            prepared=prepared,
            positions=positions,
            cash_value=cash_value,
            gross_positions=gross_positions,
            gross_cash_value=gross_cash_value,
            rebalance_date=rebalance_date,
            period_end=period_end,
            base_target_weights=base_overlay_target_weights,
            strategy_config=strategy_config,
        )

        if not weekly_portfolio_overlay_enabled and not positions.empty:
            rebalance_prices = prepared.price_ffill.loc[rebalance_date, positions.index]
            period_end_prices = prepared.price_ffill.loc[period_end, positions.index]
            positions = positions * (period_end_prices / rebalance_prices)
        if not weekly_portfolio_overlay_enabled and not gross_positions.empty:
            gross_rebalance_prices = prepared.price_ffill.loc[rebalance_date, gross_positions.index]
            gross_period_end_prices = prepared.price_ffill.loc[period_end, gross_positions.index]
            gross_positions = gross_positions * (gross_period_end_prices / gross_rebalance_prices)

        nav_end = float(positions.sum() + cash_value)
        if nav_end > 0:
            if not positions.empty:
                month_weights = (positions / nav_end).sort_values(ascending=False)
                for ts_code, weight in month_weights.items():
                    weights_history_rows.append(
                        {"date": period_end, "ts_code": ts_code, "name": prepared.code_to_name.get(ts_code, ""), "weight": float(weight)}
                    )
            cash_weight = float(cash_value / nav_end)
            if cash_weight > 1e-12:
                weights_history_rows.append({"date": period_end, "ts_code": "CASH", "name": "现金", "weight": cash_weight})

        gross_nav = float(gross_positions.sum() + gross_cash_value)
        gross_return = gross_nav / nav_at_signal_date - 1 if nav_at_signal_date > 0 else np.nan
        net_return = nav_end / nav_at_signal_date - 1 if nav_at_signal_date > 0 else np.nan

        monthly_rows.append(
            {
                "date": period_end,
                "portfolio_return": net_return,
                "gross_return": gross_return,
                "net_return": net_return,
                "trading_cost": trade_stats["trading_cost"],
                "eligible_count": len(eligible_codes),
                "candidate_family": str(strategy_config["candidate_family"]),
                "market_risk_off": bool(regime["risk_off"]),
                "risk_stage": str(regime["risk_stage"]),
                "market_momentum": regime["market_12_1_momentum"],
                "cash_weight_target": target_cash_weight,
                "cash_after_trade": trade_stats["cash_after_trade"],
                "selected_count": selection_stats["selected_count"],
                "buy_candidate_count": selection_stats["buy_candidate_count"],
                "keep_candidate_count": selection_stats["keep_candidate_count"],
                "weekly_overlay_trade_count": weekly_overlay_stats["weekly_overlay_trade_count"],
                "weekly_overlay_trading_cost": weekly_overlay_stats["weekly_overlay_trading_cost"],
                "weekly_overlay_avg_one_way_turnover": weekly_overlay_stats["weekly_overlay_avg_one_way_turnover"],
            }
        )
        trade_details = []
        for detail in trade_stats.get("trade_details", []):
            detail_row = dict(detail)
            ts_code = str(detail_row.get("ts_code") or "")
            detail_row["name"] = prepared.code_to_name.get(ts_code, "")
            trade_details.append(detail_row)
        turnover_rows.append(
            {
                "date": rebalance_date,
                "one_way_turnover": trade_stats["one_way_turnover"],
                "two_way_turnover": trade_stats["two_way_turnover"],
                "buy_amount": trade_stats["buy_amount"],
                "sell_amount": trade_stats["sell_amount"],
                "trading_cost": trade_stats["trading_cost"],
                "buy_cost": trade_stats["buy_cost"],
                "sell_commission": trade_stats["sell_commission"],
                "sell_stamp_duty": trade_stats["sell_stamp_duty"],
                "event_type": "rebalance",
                "trade_details_json": json.dumps(trade_details, ensure_ascii=False) if trade_details else "",
            }
        )
        turnover_rows.extend(weekly_overlay_turnover_rows)
        equity_rows.append({"date": period_end, "portfolio_return": net_return, "nav": nav_end, "drawdown": 0.0, "trading_cost": trade_stats["trading_cost"]})

    if effective_sample_start is None or len(equity_rows) < 2:
        raise RuntimeError("设定的回测起点晚于当前可用调仓数据。")

    equity_curve = pd.DataFrame(equity_rows)
    equity_curve["date"] = pd.to_datetime(equity_curve["date"])
    equity_curve["nav"] = equity_curve["nav"].astype(float)
    equity_curve["cummax"] = equity_curve["nav"].cummax()
    equity_curve["drawdown"] = equity_curve["nav"] / equity_curve["cummax"] - 1.0
    equity_curve = equity_curve.drop(columns=["cummax"])

    monthly_returns = pd.DataFrame(monthly_rows)
    if not monthly_returns.empty:
        monthly_returns["date"] = pd.to_datetime(monthly_returns["date"])
    turnover = pd.DataFrame(turnover_rows)
    if not turnover.empty:
        turnover["date"] = pd.to_datetime(turnover["date"])
    weights_history = pd.DataFrame(weights_history_rows)
    if not weights_history.empty:
        weights_history["date"] = pd.to_datetime(weights_history["date"])
        weights_history = weights_history.sort_values(["date", "weight"], ascending=[True, False]).reset_index(drop=True)

    annual_returns = (
        monthly_returns.assign(year=monthly_returns["date"].dt.year)
        .groupby("year")["net_return"]
        .apply(lambda series: (1.0 + series).prod() - 1.0)
        .reset_index(name="annual_return")
        if not monthly_returns.empty
        else pd.DataFrame(columns=["year", "annual_return"])
    )

    metrics = compute_metrics(equity_curve, monthly_returns, turnover, rebalance_frequency=rebalance_frequency)
    official_backtest_end = pd.Timestamp(equity_curve["date"].iloc[-1])
    latest_valuation_date = official_backtest_end
    if rebalance_frequency == "monthly" and not prepared.price_ffill.empty:
        latest_valuation_date = max(official_backtest_end, pd.Timestamp(prepared.price_ffill.index.max()))
    latest_formal_signal_date = None
    if rebalance_frequency == "monthly":
        formal_signal_dates = [date for date in prepared.month_end_dates if date <= latest_valuation_date]
        latest_formal_signal_date = formal_signal_dates[-1] if formal_signal_dates else None
    is_provisional_period_end = (
        rebalance_frequency == "monthly"
        and latest_formal_signal_date is not None
        and latest_valuation_date > latest_formal_signal_date
    )
    month_end_preview = (
        build_hk_month_end_preview_payload(
            prepared=prepared,
            strategy_config=strategy_config,
            signal_date=latest_valuation_date,
            formal_signal_date=latest_formal_signal_date,
            positions=positions,
        )
        if is_provisional_period_end
        else None
    )

    latest_weights = pd.DataFrame(columns=["ts_code", "name", "weight"])
    latest_nav = float(positions.sum() + cash_value)
    if latest_nav > 0 and not positions.empty:
        latest_weights = (
            (positions / latest_nav).sort_values(ascending=False).rename("weight").reset_index().rename(columns={"index": "ts_code"})
        )
        latest_weights["name"] = latest_weights["ts_code"].map(prepared.code_to_name)
        latest_weights = latest_weights[["ts_code", "name", "weight"]]

    summary = {
        "pool_id": "hkconnect_static_latest",
        "pool_name": "沪港通静态标的池（最新可得名单）",
        "sample_start": equity_curve["date"].iloc[0].strftime("%Y-%m-%d"),
        "sample_end": equity_curve["date"].iloc[-1].strftime("%Y-%m-%d"),
        "latest_valuation_date": latest_valuation_date.strftime("%Y-%m-%d"),
        "latest_formal_signal_date": latest_formal_signal_date.strftime("%Y-%m-%d") if latest_formal_signal_date is not None else None,
        "is_provisional_period_end": bool(is_provisional_period_end),
        "month_end_preview": month_end_preview or {},
        "sample_tag": sample_tag,
        "sample_label": sample_label,
        "sample_short_label": sample_short_label,
        "stock_count": len(prepared.code_to_name),
        "strategy_name": str(strategy_config["strategy_name"]),
        "strategy_id": str(strategy_config["strategy_id"]),
        "path": str(strategy_config["path"]),
        "candidate_family": str(strategy_config["candidate_family"]),
        "rebalance_frequency": rebalance_frequency,
        "risk_evaluation_frequency": risk_evaluation_frequency,
        "risk_overlay_scope": risk_overlay_scope,
        "signal_family": str(strategy_config["signal_family"]),
        "base_weight_method": str(strategy_config["base_weight_method"]),
        "selection_overlay": "独立沪港通策略线：仅限最新可得沪港通（SH_HK/SZ_HK）名单内的港股，基于动量、突破、流动性与仓位风控做优胜劣汰。",
        "universe_note": "受 Tushare stock_hsgt 历史覆盖限制，当前使用最新可得沪港通名单作为静态回测池。",
        "transaction_cost_note": "当前港股交易成本采用近似双边佣金模型（无印花税建模），仅用于研究比较。",
        "metrics": metrics,
        "warnings": warnings,
    }
    return equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary


def save_outputs(
    equity_curve: pd.DataFrame,
    monthly_returns: pd.DataFrame,
    annual_returns: pd.DataFrame,
    latest_weights: pd.DataFrame,
    weights_history: pd.DataFrame,
    turnover: pd.DataFrame,
    summary: Dict[str, object],
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    save_csv(equity_curve, output_dir / "equity_curve.csv")
    save_csv(monthly_returns, output_dir / "monthly_returns.csv")
    save_csv(annual_returns, output_dir / "annual_returns.csv")
    save_csv(latest_weights, output_dir / "latest_weights.csv")
    save_csv(weights_history, output_dir / "weights_history.csv")
    save_csv(turnover, output_dir / "turnover.csv")
    with open(output_dir / "summary.json", "w", encoding="utf-8") as fp:
        json.dump(summary, fp, ensure_ascii=False, indent=2)


def build_output_dir(strategy_id: str, sample_tag: str) -> Path:
    return strategy_result_dir(strategy_id, sample_tag, market_scope="hkconnect")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="回测独立沪港通策略线（Path 1 / Path 2 / Path 3）")
    parser.add_argument("--start-date", default="2017-01-01")
    parser.add_argument("--end-date", default=pd.Timestamp.today().strftime("%Y-%m-%d"))
    parser.add_argument("--sample-tags", type=str, default="")
    parser.add_argument("--only-strategy-ids", type=str, default="")
    parser.add_argument(
        "--family-scope",
        choices=["tracked_active", "research_active", "active", "all"],
        default="research_active",
        help=(
            "Strategy family scope: tracked_active runs HK tracked/top5/live active ids; "
            "research_active/all run all configured HK Path 1/2/3 variants. "
            "active is a compatibility alias for tracked_active."
        ),
    )
    parser.add_argument("--warm-cache-only", action="store_true")
    parser.add_argument("--max-new-codes", type=int, default=None)
    parser.add_argument("--sleep-between-codes", type=float, default=0.0)
    parser.add_argument("--max-runtime-minutes", type=float, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not TUSHARE_DAILY_TOKEN:
        raise RuntimeError("未找到 TUSHARE_TOKEN_DAILY，请先配置环境变量或本地 config.py。")

    ensure_hk_directories()
    pro_daily = ts.pro_api(TUSHARE_DAILY_TOKEN)
    pro_connect = ts.pro_api(TUSHARE_MINUTE_TOKEN or TUSHARE_DAILY_TOKEN)
    start_date = pd.Timestamp(args.start_date)
    end_date = pd.Timestamp(args.end_date)
    selected_sample_tags = {tag.strip() for tag in str(args.sample_tags).split(",") if tag.strip()}
    selected_strategy_ids = {sid.strip() for sid in str(args.only_strategy_ids).split(",") if sid.strip()}
    explicit_selected_strategy_ids = bool(selected_strategy_ids)
    if not selected_strategy_ids and args.family_scope in {"tracked_active", "active"}:
        selected_strategy_ids = collect_hkconnect_refresh_active_ids()
        if not selected_strategy_ids:
            raise SystemExit("[HK] No tracked_active strategy IDs found; refusing to fall back to a full HK run.")

    prepared = prepare_hkconnect_data(
        pro_daily,
        pro_connect,
        start_date,
        end_date,
        max_new_codes=args.max_new_codes,
        warm_cache_only=bool(args.warm_cache_only),
        sleep_between_codes=float(args.sleep_between_codes or 0.0),
        max_runtime_minutes=args.max_runtime_minutes,
    )
    if prepared is None:
        return
    selected_windows = (
        [window for window in HK_SAMPLE_WINDOWS if window["sample_tag"] in selected_sample_tags]
        if selected_sample_tags
        else list(HK_SAMPLE_WINDOWS)
    )
    strategy_variants = HK_PATH1_VARIANTS + HK_PATH2_VARIANTS + HK_PATH3_VARIANTS
    if selected_strategy_ids:
        strategy_variants = [variant for variant in strategy_variants if variant["strategy_id"] in selected_strategy_ids]
        known_ids = {str(variant["strategy_id"]) for variant in strategy_variants}
        missing_ids = sorted(selected_strategy_ids - known_ids)
        if missing_ids:
            print(f"[HK] Skip {len(missing_ids)} selected ids that are not generated by the current HK variant set.")

    comparison_rows: List[Dict[str, object]] = []
    skipped_runs: List[str] = []
    for sample_window in selected_windows:
        for variant in strategy_variants:
            strategy_config = {**variant, **sample_window}
            print(
                f"[HK] Running {strategy_config['strategy_id']} | "
                f"{sample_window['sample_tag']} | {strategy_config['rebalance_frequency']}"
            )
            try:
                equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary = run_hk_backtest(prepared, strategy_config)
            except RuntimeError as exc:
                if "设定的回测起点晚于当前可用调仓数据" in str(exc):
                    skipped_runs.append(f"{strategy_config['strategy_id']}|{sample_window['sample_tag']}")
                    print(f"[HK] Skip {strategy_config['strategy_id']} | {sample_window['sample_tag']}：观察窗可用调仓点不足")
                    continue
                raise
            output_dir = build_output_dir(str(strategy_config["strategy_id"]), str(sample_window["sample_tag"]))
            save_outputs(equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary, output_dir)
            metrics = summary["metrics"]
            comparison_rows.append(
                {
                    "pool_id": summary["pool_id"],
                    "pool_name": summary["pool_name"],
                    "strategy_id": summary["strategy_id"],
                    "strategy_name": summary["strategy_name"],
                    "path": summary["path"],
                    "candidate_family": summary["candidate_family"],
                    "rebalance_frequency": summary["rebalance_frequency"],
                    "risk_evaluation_frequency": summary["risk_evaluation_frequency"],
                    "risk_overlay_scope": summary["risk_overlay_scope"],
                    "sample_tag": summary["sample_tag"],
                    "sample_label": summary["sample_label"],
                    "sample_start": summary["sample_start"],
                    "sample_end": summary["sample_end"],
                    "total_return": metrics["total_return"],
                    "cagr": metrics["cagr"],
                    "max_drawdown": metrics["max_drawdown"],
                    "sharpe_ratio": metrics["sharpe_ratio"],
                    "annual_volatility": metrics["annual_volatility"],
                    "average_annual_turnover": metrics["average_annual_turnover"],
                    "cumulative_trading_cost": metrics["cumulative_trading_cost"],
                }
            )

    if not comparison_rows:
        print("[HK] No HK Connect strategy rows were generated.")
        return

    comparison_df = pd.DataFrame(comparison_rows).sort_values(["sample_start", "path", "cagr"], ascending=[True, True, False])
    comparison_path = research_file("strategy_comparison_hkconnect.csv", market_scope="hkconnect")
    merge_existing = bool(
        explicit_selected_strategy_ids
        or selected_sample_tags
        or args.family_scope in {"tracked_active", "active"}
    )
    if merge_existing:
        comparison_df = merge_latest_rows(
            comparison_df,
            comparison_path,
            key_cols=["strategy_id", "sample_tag"],
            sort_cols=["sample_start", "path", "cagr"],
        )
    save_csv(comparison_df, comparison_path)
    if skipped_runs:
        print(f"[HK] Skipped {len(skipped_runs)} runs due to insufficient observation-window rebalance points.")
    print("\n===== HK Connect Strategy Summary =====")
    print(comparison_df[["sample_tag", "path", "strategy_name", "cagr", "max_drawdown", "sharpe_ratio"]].head(20).to_string(index=False))


if __name__ == "__main__":
    main()
