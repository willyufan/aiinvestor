from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import math
import os
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Tuple

os.environ.setdefault("MPLCONFIGDIR", str(Path("data_cache") / "mplconfig"))

import matplotlib
import numpy as np
import pandas as pd
import tushare as ts

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from scripts.results_layout import (
    RESULTS_DIR,
    ensure_results_layout,
    existing_research_file,
    research_file,
    strategy_result_dir,
)
from scripts.active_strategy_scope import collect_ashare_refresh_active_ids
from scripts.comparison_merge import merge_latest_rows


def _load_token() -> str:
    t = os.environ.get("TUSHARE_TOKEN_DAILY", "")
    if not t:
        try:
            import importlib
            import config as _cfg
            importlib.reload(_cfg)
            t = getattr(_cfg, "TUSHARE_TOKEN_DAILY", "") or ""
        except Exception:
            pass
    return t

TOKEN = _load_token()
PRIMARY_SAMPLE_START = pd.Timestamp("2020-01-01")
ROBUSTNESS_SAMPLE_START = pd.Timestamp("2017-01-01")
SHORT_SAMPLE_START = pd.Timestamp("2023-01-01")
VERY_SHORT_SAMPLE_START = pd.Timestamp("2025-01-01")
YTD_SAMPLE_START = pd.Timestamp("2026-01-01")
BACKTEST_SAMPLE_WINDOWS = [
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
        "sample_label": "2026-01 起",
        "sample_short_label": "2026-01",
        "sample_start": YTD_SAMPLE_START,
        "is_primary_sample": False,
    },
]
BUY_COMMISSION = 0.0003
SELL_COMMISSION = 0.0003
STAMP_DUTY_PRE_20230828 = 0.001
STAMP_DUTY_POST_20230828 = 0.0005
STAMP_DUTY_CHANGE_DATE = pd.Timestamp("2023-08-28")
WEIGHT_CAP = 0.25
MIN_LISTING_MONTHS = 12
SEED_MIN_LISTING_MONTHS = 6
ENHANCEMENT_BUCKET_PCT = 0.20
BUY_ENTRY_PERCENTILE = 0.15
SELL_EXIT_PERCENTILE = 0.25
MIN_WEIGHT_TRADE_THRESHOLD = 0.01
RISK_EVAL_FREQUENCY_MONTHLY = "monthly"
RISK_EVAL_FREQUENCY_WEEKLY = "weekly"
SAT_WEEKLY_RISK_SUFFIX = "__sat_weekly_risk"
SAT_THREE_STAGE_SUFFIX = "__sat_three_stage_risk"
SAT_THREE_STAGE_BUFFERED_SUFFIX = "__sat_three_stage_buffered"
SAT_THREE_STAGE_BUFFERED_COST_GUARD_SUFFIX = "__sat_three_stage_buffered_cost_guard"
SAT_THREE_STAGE_BUFFERED_COST_GUARD_CASHGUARD_SUFFIX = "__sat_three_stage_buffered_cost_guard_cashguard"
# Asymmetric stage-transition confirmation (Phase 2):
#   risk_off_confirm_weeks = 1 (降仓快: confirm in 1 week)
#   risk_on_confirm_weeks  = 3 (加仓慢: require 3 weeks of confirmation)
# Distinct from `__port_weekly_exposure_asym` which controls portfolio-level
# ramp-up speed; this suffix controls the buffer's directional confirmation.
SAT_THREE_STAGE_BUFFERED_ASYM13_SUFFIX = "__sat_three_stage_buffered_asym13"
PORT_WEEKLY_EXPOSURE_SUFFIX = "__port_weekly_exposure"
PORT_WEEKLY_EXPOSURE_BUFFERED_SUFFIX = "__port_weekly_exposure_buffered"
PORT_WEEKLY_EXPOSURE_BUFFERED_ASYM13_SUFFIX = "__port_weekly_exposure_buffered_asym13"
PORT_WEEKLY_EXPOSURE_ASYM_SUFFIX = "__port_weekly_exposure_asym"
WEEKLY_OVERLAY_SUFFIXES = (
    SAT_WEEKLY_RISK_SUFFIX,
    SAT_THREE_STAGE_SUFFIX,
    SAT_THREE_STAGE_BUFFERED_SUFFIX,
    SAT_THREE_STAGE_BUFFERED_COST_GUARD_SUFFIX,
    SAT_THREE_STAGE_BUFFERED_COST_GUARD_CASHGUARD_SUFFIX,
    SAT_THREE_STAGE_BUFFERED_ASYM13_SUFFIX,
    PORT_WEEKLY_EXPOSURE_SUFFIX,
    PORT_WEEKLY_EXPOSURE_BUFFERED_SUFFIX,
    PORT_WEEKLY_EXPOSURE_BUFFERED_ASYM13_SUFFIX,
    PORT_WEEKLY_EXPOSURE_ASYM_SUFFIX,
)
# Default asymmetric confirmation periods (Phase 2 _asym13 line):
RISK_OFF_CONFIRM_WEEKS_ASYM13 = 1
RISK_ON_CONFIRM_WEEKS_ASYM13 = 3
CORE_RISK_OFF_EXPOSURE = 0.60
CORE_RISK_ON_EXPOSURE = 1.00
CORE_CAUTION_EXPOSURE = 0.85
SATELLITE_RISK_OFF_EXPOSURE = 0.30
SATELLITE_RISK_ON_EXPOSURE = 1.00
SATELLITE_CAUTION_EXPOSURE = 0.60
MONTHLY_MOMENTUM_LOOKBACK = 12
MONTHLY_MOMENTUM_SKIP = 1
MONTHLY_MA_LOOKBACK = 10
WEEKLY_MOMENTUM_LOOKBACK = 52
WEEKLY_MOMENTUM_SKIP = 4
WEEKLY_MA_LOOKBACK = 40
WEEKLY_STAGE_CONFIRM_WEEKS = 2
WEEKLY_PORTFOLIO_RAMP_UP = 0.15

# Phase 3: Path 4-lite multi-factor presets (A 股 only)
#
# `multi_factor` core_signal_mode reuses already-computed factor caches and
# combines them via configurable weights. Compared with the existing `theme`
# mode, the main new ingredient is `quality_scores` — until now quality has
# only acted as a screening floor (`core_quality_quantile`), not as part of
# the scoring blend. Adding it lets us test whether quality contributes
# orthogonal information on top of the existing momentum/industry/growth
# signals.
DEFAULT_MULTI_FACTOR_WEIGHTS = {
    "momentum_6_1": 0.30,
    "momentum_3_1": 0.10,
    "quality": 0.15,
    "growth_acceleration": 0.20,
    "industry_strength": 0.10,
    "industry_leader": 0.10,
    "liquidity_surge": 0.05,
}

MULTI_FACTOR_PRESETS = {
    "balanced": DEFAULT_MULTI_FACTOR_WEIGHTS,
    # quality_tilt: emphasise the unused dimension; reduce price-momentum weight.
    "quality_tilt": {
        "momentum_6_1": 0.20,
        "momentum_3_1": 0.10,
        "quality": 0.30,
        "growth_acceleration": 0.15,
        "industry_strength": 0.10,
        "industry_leader": 0.10,
        "liquidity_surge": 0.05,
    },
    # momentum_quality: keep momentum dominant but add quality as orthogonal filter.
    "momentum_quality": {
        "momentum_6_1": 0.40,
        "momentum_3_1": 0.10,
        "quality": 0.20,
        "growth_acceleration": 0.10,
        "industry_strength": 0.10,
        "industry_leader": 0.10,
        "liquidity_surge": 0.00,
    },
    "growth_quality": {
        "momentum_6_1": 0.25,
        "momentum_3_1": 0.10,
        "quality": 0.25,
        "growth_acceleration": 0.25,
        "industry_strength": 0.05,
        "industry_leader": 0.05,
        "liquidity_surge": 0.05,
    },
    "industry_quality": {
        "momentum_6_1": 0.25,
        "momentum_3_1": 0.05,
        "quality": 0.25,
        "growth_acceleration": 0.10,
        "industry_strength": 0.20,
        "industry_leader": 0.10,
        "liquidity_surge": 0.05,
    },
    "quality_defense": {
        "momentum_6_1": 0.20,
        "momentum_3_1": 0.05,
        "quality": 0.35,
        "growth_acceleration": 0.05,
        "industry_strength": 0.20,
        "industry_leader": 0.10,
        "liquidity_surge": 0.05,
    },
    "trend_quality_defense": {
        "momentum_6_1": 0.30,
        "momentum_3_1": 0.08,
        "quality": 0.28,
        "growth_acceleration": 0.07,
        "industry_strength": 0.15,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "trend_lowvol_quality": {
        "momentum_6_1": 0.24,
        "momentum_3_1": 0.10,
        "quality": 0.32,
        "growth_acceleration": 0.05,
        "industry_strength": 0.17,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "trend_momentum_quality": {
        "momentum_6_1": 0.34,
        "momentum_3_1": 0.10,
        "quality": 0.22,
        "growth_acceleration": 0.08,
        "industry_strength": 0.16,
        "industry_leader": 0.08,
        "liquidity_surge": 0.02,
    },
    "trend_industry_momentum": {
        "momentum_6_1": 0.32,
        "momentum_3_1": 0.12,
        "quality": 0.12,
        "growth_acceleration": 0.08,
        "industry_strength": 0.22,
        "industry_leader": 0.08,
        "liquidity_surge": 0.06,
    },
    "industry_momentum_lowvol": {
        "momentum_6_1": 0.28,
        "momentum_3_1": 0.10,
        "quality": 0.18,
        "growth_acceleration": 0.06,
        "industry_strength": 0.24,
        "industry_leader": 0.10,
        "liquidity_surge": 0.04,
    },
    "industry_momentum_quality": {
        "momentum_6_1": 0.30,
        "momentum_3_1": 0.10,
        "quality": 0.22,
        "growth_acceleration": 0.05,
        "industry_strength": 0.22,
        "industry_leader": 0.08,
        "liquidity_surge": 0.03,
    },
    "trend_quality_rebalance": {
        "momentum_6_1": 0.26,
        "momentum_3_1": 0.12,
        "quality": 0.30,
        "growth_acceleration": 0.04,
        "industry_strength": 0.18,
        "industry_leader": 0.08,
        "liquidity_surge": 0.02,
    },
    "profitability_lowvol_rebalance": {
        "momentum_6_1": 0.22,
        "momentum_3_1": 0.10,
        "quality": 0.34,
        "growth_acceleration": 0.04,
        "industry_strength": 0.18,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_lowvol_reconfirm": {
        "momentum_6_1": 0.24,
        "momentum_3_1": 0.08,
        "quality": 0.36,
        "growth_acceleration": 0.03,
        "industry_strength": 0.17,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_lowvol_cashguard_reconfirm": {
        "momentum_6_1": 0.22,
        "momentum_3_1": 0.08,
        "quality": 0.38,
        "growth_acceleration": 0.02,
        "industry_strength": 0.18,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_lowvol_trend_reconfirm": {
        "momentum_6_1": 0.25,
        "momentum_3_1": 0.09,
        "quality": 0.36,
        "growth_acceleration": 0.02,
        "industry_strength": 0.16,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_trend_reconfirm": {
        "momentum_6_1": 0.26,
        "momentum_3_1": 0.10,
        "quality": 0.34,
        "growth_acceleration": 0.03,
        "industry_strength": 0.17,
        "industry_leader": 0.08,
        "liquidity_surge": 0.02,
    },
    "quality_trend_cashguard_reconfirm": {
        "momentum_6_1": 0.24,
        "momentum_3_1": 0.09,
        "quality": 0.36,
        "growth_acceleration": 0.02,
        "industry_strength": 0.17,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_value_trend_cost_guard_reconfirm": {
        "momentum_6_1": 0.23,
        "momentum_3_1": 0.10,
        "quality": 0.40,
        "growth_acceleration": 0.01,
        "industry_strength": 0.14,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_value_industry_cost_guard_reconfirm": {
        "momentum_6_1": 0.21,
        "momentum_3_1": 0.09,
        "quality": 0.42,
        "growth_acceleration": 0.01,
        "industry_strength": 0.16,
        "industry_leader": 0.10,
        "liquidity_surge": 0.01,
    },
    "quality_lowvol_value_reconfirm": {
        "momentum_6_1": 0.21,
        "momentum_3_1": 0.08,
        "quality": 0.42,
        "growth_acceleration": 0.01,
        "industry_strength": 0.16,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "profitability_value_cashguard_reconfirm": {
        "momentum_6_1": 0.20,
        "momentum_3_1": 0.08,
        "quality": 0.44,
        "growth_acceleration": 0.01,
        "industry_strength": 0.15,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "profitability_industry_reconfirm": {
        "momentum_6_1": 0.24,
        "momentum_3_1": 0.08,
        "quality": 0.30,
        "growth_acceleration": 0.04,
        "industry_strength": 0.22,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_industry_reconfirm": {
        "momentum_6_1": 0.22,
        "momentum_3_1": 0.08,
        "quality": 0.34,
        "growth_acceleration": 0.03,
        "industry_strength": 0.21,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_industry_cashguard_reconfirm": {
        "momentum_6_1": 0.20,
        "momentum_3_1": 0.08,
        "quality": 0.36,
        "growth_acceleration": 0.02,
        "industry_strength": 0.22,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_profitability_cashguard_reconfirm": {
        "momentum_6_1": 0.21,
        "momentum_3_1": 0.08,
        "quality": 0.38,
        "growth_acceleration": 0.06,
        "industry_strength": 0.15,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_defense_cashguard_reconfirm": {
        "momentum_6_1": 0.20,
        "momentum_3_1": 0.07,
        "quality": 0.42,
        "growth_acceleration": 0.02,
        "industry_strength": 0.15,
        "industry_leader": 0.12,
        "liquidity_surge": 0.02,
    },
    "quality_growth_signal_reconfirm": {
        "momentum_6_1": 0.24,
        "momentum_3_1": 0.10,
        "quality": 0.34,
        "growth_acceleration": 0.10,
        "industry_strength": 0.14,
        "industry_leader": 0.06,
        "liquidity_surge": 0.02,
    },
    "profitability_industry_signal_reconfirm": {
        "momentum_6_1": 0.22,
        "momentum_3_1": 0.09,
        "quality": 0.36,
        "growth_acceleration": 0.06,
        "industry_strength": 0.18,
        "industry_leader": 0.07,
        "liquidity_surge": 0.02,
    },
    "profitability_growth_signal_reconfirm": {
        "momentum_6_1": 0.22,
        "momentum_3_1": 0.10,
        "quality": 0.34,
        "growth_acceleration": 0.12,
        "industry_strength": 0.14,
        "industry_leader": 0.06,
        "liquidity_surge": 0.02,
    },
    "quality_industry_signal_cashguard_reconfirm": {
        "momentum_6_1": 0.20,
        "momentum_3_1": 0.08,
        "quality": 0.40,
        "growth_acceleration": 0.04,
        "industry_strength": 0.18,
        "industry_leader": 0.08,
        "liquidity_surge": 0.02,
    },
    "quality_growth_industry_cost_guard_reconfirm": {
        "momentum_6_1": 0.22,
        "momentum_3_1": 0.10,
        "quality": 0.36,
        "growth_acceleration": 0.08,
        "industry_strength": 0.16,
        "industry_leader": 0.06,
        "liquidity_surge": 0.02,
    },
    "quality_lowvol_industry_cost_guard_reconfirm": {
        "momentum_6_1": 0.19,
        "momentum_3_1": 0.08,
        "quality": 0.43,
        "growth_acceleration": 0.01,
        "industry_strength": 0.18,
        "industry_leader": 0.10,
        "liquidity_surge": 0.01,
    },
    "quality_profitability_industry_defense_reconfirm": {
        "momentum_6_1": 0.18,
        "momentum_3_1": 0.07,
        "quality": 0.42,
        "growth_acceleration": 0.04,
        "industry_strength": 0.17,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_profitability_signal_cost_guard_reconfirm": {
        "momentum_6_1": 0.20,
        "momentum_3_1": 0.09,
        "quality": 0.38,
        "growth_acceleration": 0.07,
        "industry_strength": 0.14,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_profitability_lowvol_signal_cost_guard_reconfirm": {
        "momentum_6_1": 0.18,
        "momentum_3_1": 0.07,
        "quality": 0.43,
        "growth_acceleration": 0.05,
        "industry_strength": 0.15,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_profitability_value_lowvol_industry_cost_guard_reconfirm": {
        "momentum_6_1": 0.17,
        "momentum_3_1": 0.07,
        "quality": 0.44,
        "growth_acceleration": 0.03,
        "industry_strength": 0.17,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_profitability_value_lowvol_trend_cost_guard_reconfirm": {
        "momentum_6_1": 0.19,
        "momentum_3_1": 0.09,
        "quality": 0.43,
        "growth_acceleration": 0.03,
        "industry_strength": 0.15,
        "industry_leader": 0.09,
        "liquidity_surge": 0.02,
    },
    "quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm": {
        "momentum_6_1": 0.18,
        "momentum_3_1": 0.07,
        "quality": 0.43,
        "growth_acceleration": 0.04,
        "industry_strength": 0.16,
        "industry_leader": 0.10,
        "liquidity_surge": 0.02,
    },
    "quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm": {
        "momentum_6_1": 0.20,
        "momentum_3_1": 0.10,
        "quality": 0.42,
        "growth_acceleration": 0.03,
        "industry_strength": 0.14,
        "industry_leader": 0.09,
        "liquidity_surge": 0.02,
    },
    "quality_profitability_growth_trend_signal_cashguard_reconfirm": {
        "momentum_6_1": 0.21,
        "momentum_3_1": 0.10,
        "quality": 0.38,
        "growth_acceleration": 0.10,
        "industry_strength": 0.12,
        "industry_leader": 0.07,
        "liquidity_surge": 0.02,
    },
}

VALID_MULTI_FACTOR_KEYS = frozenset(DEFAULT_MULTI_FACTOR_WEIGHTS.keys())
WEEKLY_ALPHA_SIGNAL_MODES = {
    "weekly_alpha_balanced",
    "weekly_alpha_breakout",
    "weekly_alpha_pullback",
}
EMERGENT_THEME_SIGNAL_MODE = "emergent_theme"
ALPHA_POOL_PROFILE_CORE_EXPLORE_SEED = "core_explore_seed"
ALPHA_POOL_PROFILE_GROWTH_ELASTIC = "growth_elastic"
ALPHA_POOL_PROFILE_EMERGENT_THEME = "emergent_theme"
ALPHA_POOL_PROFILE_EVENT_KG_BASKET = "event_kg_basket"
ALPHA_POOL_NAMES = {
    ALPHA_POOL_PROFILE_CORE_EXPLORE_SEED: "Path1/3 核心-探索-种子共用池",
    ALPHA_POOL_PROFILE_GROWTH_ELASTIC: "Path2 高弹性赢家池",
    ALPHA_POOL_PROFILE_EMERGENT_THEME: "Path4 新兴主题发现池",
    ALPHA_POOL_PROFILE_EVENT_KG_BASKET: "Path5 事件知识图谱冻结篮子",
}
MARKET_INDEX_CODE = "000300.SH"
BENCHMARK_INDEX_CODE = "000001.SH"
CORE_INDEX_CODES = ["000300.SH", "000688.SH"]
EXPLORE_INDEX_CODES = ["000905.SH", "000698.SH", "000699.SH"]
FACTOR_MIN_LISTING_MONTHS = 1
PATH4_CORE_MIN_LISTING_MONTHS = MIN_LISTING_MONTHS
PATH4_SEED_MIN_LISTING_MONTHS = SEED_MIN_LISTING_MONTHS
CORE_BUY_ENTRY_PERCENTILE = 0.10
CORE_SELL_EXIT_PERCENTILE = 0.20
EXPLORE_BUY_ENTRY_PERCENTILE = 0.12
EXPLORE_SELL_EXIT_PERCENTILE = 0.20
SEED_BUY_ENTRY_PERCENTILE = 0.20
SEED_SELL_EXIT_PERCENTILE = 0.35
PROMOTED_CORE_SELL_EXIT_PERCENTILE = 0.35
CORE_QUALITY_QUANTILE = 0.60
EXPLORE_QUALITY_QUANTILE = 0.50
SEED_QUALITY_QUANTILE = 0.35
ROLLING_AMOUNT_WINDOW = 60
CORE_AMOUNT_THRESHOLD = 300000.0
EXPLORE_AMOUNT_THRESHOLD = 50000.0
SEED_AMOUNT_THRESHOLD = 25000.0
SEED_MAX_PORTFOLIO_RATIO = 0.10
SEED_BREAKOUT_LOOKBACK_DAYS = 20
DATA_HISTORY_MONTHS = 18
PROMOTION_MIN_STREAK = 3
DEMOTION_MIN_STREAK = 2
PROMOTED_CORE_DEMOTION_MIN_STREAK = 3
FAST_PROMOTION_MIN_STREAK = 2
FAST_PROMOTION_PERCENTILE = 0.08
FAST_PROMOTION_AMOUNT_SURGE_RATIO = 1.05
CORE_MAX_HOLDINGS = 10
EXPLORE_MAX_HOLDINGS = 12
SEED_MAX_HOLDINGS = 6
WINNER_CORE_STABLE_SHARE = 0.20
WINNER_CORE_PROMOTED_SHARE = 0.80
STABLE_CORE_MAX_HOLDINGS = 4
PROMOTED_CORE_MAX_HOLDINGS = 6
PROMOTED_CORE_STAGE_RAMP = {1: 0.75, 2: 1.00}
TOTAL_PORTFOLIO_MAX_HOLDINGS = 18
TOTAL_PORTFOLIO_MIN_WEIGHT = 0.005
FORCE_EXIT_WEIGHT_THRESHOLD = 0.0005
MAX_RETRIES = 5
RETRY_BASE_DELAY = 1.5
DNS_RETRY_ATTEMPTS = 10
DNS_RETRY_BASE_DELAY = 30.0
DNS_RETRY_MAX_DELAY = 300.0
CACHE_REFRESH_MAX_WORKERS = 5
FLOAT_FORMAT = "%.8f"
TUSHARE_OFFLINE_MODE = os.getenv("AIINVESTOR_FORCE_OFFLINE", "").strip().lower() in {"1", "true", "yes", "y"}
_CACHE_WORKER_STATE = threading.local()

WINNER_CORE_VARIANTS = [
    {
        "variant_id": "share_15_85_hold_4_6",
        "variant_name": "比例15/85",
        "winner_core_stable_share": 0.15,
        "winner_core_promoted_share": 0.85,
        "stable_core_max_holdings": 4,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_10_90_fast_ramp",
        "variant_name": "进攻10/90 快速加仓",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_10_90_hold_4_6",
        "variant_name": "进攻10/90(4+6)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 4,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_10_90_prom6",
        "variant_name": "进攻10/90 晋升6只",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_10_90_prom5",
        "variant_name": "进攻10/90 晋升5只",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 5,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_10_90_prom7",
        "variant_name": "进攻10/90 晋升7只",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_10_90_prom7_ramp90",
        "variant_name": "进攻10/90 晋升7只(分步加仓)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 0.90, 2: 1.00},
    },
    {
        "variant_id": "aggr_08_92_prom6",
        "variant_name": "进攻8/92 晋升6只",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_05_95_prom7",
        "variant_name": "进攻5/95 晋升7只",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_cashguard_light",
        "variant_name": "进攻5/95 晋升7只(卫星三档轻现金成本防守)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.52,
        "satellite_risk_off_exposure": 0.10,
        "promoted_core_sell_exit_percentile": 0.57,
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk30_reconfirm",
        "variant_name": "进攻5/95 晋升7只(卫星三档风险30成本再确认)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.48,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.55,
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm",
        "variant_name": "进攻5/95 晋升7只(卫星三档风险25成本再确认)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.46,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.53,
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm",
        "variant_name": "进攻5/95 晋升7只(卫星三档风险20成本再确认)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.44,
        "satellite_risk_off_exposure": 0.20,
        "promoted_core_sell_exit_percentile": 0.52,
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm",
        "variant_name": "进攻5/95 晋升7只(卫星三档风险18成本再确认)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.43,
        "satellite_risk_off_exposure": 0.18,
        "promoted_core_sell_exit_percentile": 0.51,
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk15_reconfirm",
        "variant_name": "进攻5/95 晋升7只(卫星三档风险15成本再确认)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.42,
        "satellite_risk_off_exposure": 0.15,
        "promoted_core_sell_exit_percentile": 0.50,
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm",
        "variant_name": "进攻5/95 晋升7只(卫星三档风险14成本再确认)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.41,
        "satellite_risk_off_exposure": 0.14,
        "promoted_core_sell_exit_percentile": 0.495,
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm",
        "variant_name": "进攻5/95 晋升7只(卫星三档风险16成本再确认)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.425,
        "satellite_risk_off_exposure": 0.16,
        "promoted_core_sell_exit_percentile": 0.505,
    },
    {
        "variant_id": "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk12_reconfirm",
        "variant_name": "进攻5/95 晋升7只(卫星三档风险12成本再确认)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
        "risk_staging_mode": "three_stage",
        "risk_overlay_scope": "satellite_only",
        "risk_stage_buffered": True,
        "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
        "satellite_caution_exposure": 0.40,
        "satellite_risk_off_exposure": 0.12,
        "promoted_core_sell_exit_percentile": 0.49,
    },
    {
        "variant_id": "aggr_08_92_prom6_ramp90",
        "variant_name": "进攻8/92 晋升6只(分步加仓)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 0.90, 2: 1.00},
    },
    {
        "variant_id": "aggr_08_92_prom7",
        "variant_name": "进攻8/92 晋升7只",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_08_92_prom7_ramp90",
        "variant_name": "进攻8/92 晋升7只(分步加仓)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 0.90, 2: 1.00},
    },
    {
        "variant_id": "aggr_07_93_prom8",
        "variant_name": "进攻7/93 晋升8只",
        "winner_core_stable_share": 0.07,
        "winner_core_promoted_share": 0.93,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_07_93_prom8_ramp85",
        "variant_name": "进攻7/93 晋升8只(分步加仓)",
        "winner_core_stable_share": 0.07,
        "winner_core_promoted_share": 0.93,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
    },
    {
        "variant_id": "aggr_08_92_hold_3_6",
        "variant_name": "进攻8/92(3+6)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 3,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_08_92_hold_3_6_ramp90",
        "variant_name": "进攻8/92(3+6 分步加仓)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 3,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 0.90, 2: 1.00},
    },
    {
        "variant_id": "aggr_07_93_hold_3_7_ramp90",
        "variant_name": "进攻7/93(3+7 分步加仓)",
        "winner_core_stable_share": 0.07,
        "winner_core_promoted_share": 0.93,
        "stable_core_max_holdings": 3,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 0.90, 2: 1.00},
    },
    {
        "variant_id": "share_10_90_hold_3_7",
        "variant_name": "比例10/90(3+7)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 3,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "share_10_90_hold_3_7_ramp80_cost_guard",
        "variant_name": "比例10/90(3+7 分步加仓80成本防守)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 3,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 0.80, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.22,
    },
    {
        "variant_id": "share_08_92_hold_3_7_ramp90_cost_guard",
        "variant_name": "比例8/92(3+7 分步加仓成本防守)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 3,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 0.90, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.22,
    },
    {
        "variant_id": "share_12_88_hold_3_7_ramp85_cost_guard",
        "variant_name": "比例12/88(3+7 分步加仓85成本防守)",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 3,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.24,
    },
    {
        "variant_id": "share_06_94_hold_2_8_ramp85",
        "variant_name": "比例6/94(2+8 分步加仓)",
        "winner_core_stable_share": 0.06,
        "winner_core_promoted_share": 0.94,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
    },
    {
        "variant_id": "share_06_94_hold_2_8_ramp85_cost_guard",
        "variant_name": "比例6/94(2+8 分步加仓成本防守)",
        "winner_core_stable_share": 0.06,
        "winner_core_promoted_share": 0.94,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "share_06_94_hold_2_8_ramp80_cost_guard",
        "variant_name": "比例6/94(2+8 分步加仓80成本防守)",
        "winner_core_stable_share": 0.06,
        "winner_core_promoted_share": 0.94,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.80, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "share_06_94_hold_2_8_ramp75_cost_guard",
        "variant_name": "比例6/94(2+8 分步加仓75成本防守)",
        "winner_core_stable_share": 0.06,
        "winner_core_promoted_share": 0.94,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.75, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "share_04_96_hold_2_8_ramp75_cost_guard",
        "variant_name": "比例4/96(2+8 分步加仓75成本防守)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.75, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.16,
    },
    {
        "variant_id": "share_08_92_hold_2_8_ramp85_cost_guard",
        "variant_name": "比例8/92(2+8 分步加仓成本防守)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.20,
    },
    {
        "variant_id": "share_08_92_hold_2_8_ramp80_cost_guard",
        "variant_name": "比例8/92(2+8 分步加仓80成本防守)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.80, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.20,
    },
    {
        "variant_id": "share_08_92_hold_2_8_ramp75_cost_guard",
        "variant_name": "比例8/92(2+8 分步加仓75成本防守)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.75, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.20,
    },
    {
        "variant_id": "share_10_90_hold_2_8_ramp85_cost_guard",
        "variant_name": "比例10/90(2+8 分步加仓成本防守)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.22,
    },
    {
        "variant_id": "share_10_90_hold_2_8_ramp80_cost_guard",
        "variant_name": "比例10/90(2+8 分步加仓80成本防守)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.80, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.22,
    },
    {
        "variant_id": "share_12_88_hold_2_8_ramp80_cost_guard",
        "variant_name": "比例12/88(2+8 分步加仓80成本防守)",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.80, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.24,
    },
    {
        "variant_id": "share_12_88_hold_2_8_ramp75_cost_guard",
        "variant_name": "比例12/88(2+8 分步加仓75成本防守)",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.75, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.22,
    },
    {
        "variant_id": "share_14_86_hold_2_8_ramp75_cost_guard",
        "variant_name": "比例14/86(2+8 分步加仓75成本防守)",
        "winner_core_stable_share": 0.14,
        "winner_core_promoted_share": 0.86,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.75, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.22,
    },
    {
        "variant_id": "share_16_84_hold_2_8_ramp70_cost_guard",
        "variant_name": "比例16/84(2+8 分步加仓70成本防守)",
        "winner_core_stable_share": 0.16,
        "winner_core_promoted_share": 0.84,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.70, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.20,
    },
    {
        "variant_id": "share_18_82_hold_2_8_ramp68_cost_guard",
        "variant_name": "比例18/82(2+8 分步加仓68成本防守)",
        "winner_core_stable_share": 0.18,
        "winner_core_promoted_share": 0.82,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.68, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "share_20_80_hold_2_8_ramp66_cost_guard",
        "variant_name": "比例20/80(2+8 分步加仓66成本防守)",
        "winner_core_stable_share": 0.20,
        "winner_core_promoted_share": 0.80,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.66, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.16,
    },
    {
        "variant_id": "share_22_78_hold_2_8_ramp64_cost_guard",
        "variant_name": "比例22/78(2+8 分步加仓64成本防守)",
        "winner_core_stable_share": 0.22,
        "winner_core_promoted_share": 0.78,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 0.64, 2: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.14,
    },
    {
        "variant_id": "share_12_88_hold_4_6",
        "variant_name": "比例12/88",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 4,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "share_12_88_hold_3_7",
        "variant_name": "比例12/88(3+7)",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 3,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_09_91_prom7",
        "variant_name": "进攻9/91 晋升7只",
        "winner_core_stable_share": 0.09,
        "winner_core_promoted_share": 0.91,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
    },
    # Phase 3 (Path 4-lite): multi_factor core signal variants.
    # Three base shapes (08_92_prom6 / 10_90_prom6 / 05_95_prom7) × three
    # presets (balanced / quality_tilt / momentum_quality). Each variant
    # only swaps the core signal scoring; satellite/promotion/winner-core
    # ratios match the corresponding non-multifactor sibling so the
    # comparison isolates the value of adding `quality_scores` and
    # configurable factor weights to the core blend.
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_balanced",
        "variant_name": "进攻8/92 晋升6只(多因子均衡)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["balanced"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_tilt",
        "variant_name": "进攻8/92 晋升6只(多因子偏质量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_tilt"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_momentum_quality",
        "variant_name": "进攻8/92 晋升6只(多因子动量+质量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["momentum_quality"],
    },
    {
        "variant_id": "aggr_10_90_prom6_core_multifactor_balanced",
        "variant_name": "进攻10/90 晋升6只(多因子均衡)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["balanced"],
    },
    {
        "variant_id": "aggr_10_90_prom6_core_multifactor_quality_tilt",
        "variant_name": "进攻10/90 晋升6只(多因子偏质量)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_tilt"],
    },
    {
        "variant_id": "aggr_10_90_prom6_core_multifactor_momentum_quality",
        "variant_name": "进攻10/90 晋升6只(多因子动量+质量)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["momentum_quality"],
    },
    {
        "variant_id": "aggr_05_95_prom7_core_multifactor_balanced",
        "variant_name": "进攻5/95 晋升7只(多因子均衡)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["balanced"],
    },
    {
        "variant_id": "aggr_05_95_prom7_core_multifactor_quality_tilt",
        "variant_name": "进攻5/95 晋升7只(多因子偏质量)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_tilt"],
    },
    {
        "variant_id": "aggr_05_95_prom7_core_multifactor_momentum_quality",
        "variant_name": "进攻5/95 晋升7只(多因子动量+质量)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["momentum_quality"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_growth_quality",
        "variant_name": "进攻8/92 晋升6只(多因子成长+质量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["growth_quality"],
    },
    {
        "variant_id": "aggr_10_90_prom6_core_multifactor_growth_quality",
        "variant_name": "进攻10/90 晋升6只(多因子成长+质量)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["growth_quality"],
    },
    {
        "variant_id": "aggr_05_95_prom7_core_multifactor_growth_quality",
        "variant_name": "进攻5/95 晋升7只(多因子成长+质量)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["growth_quality"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_industry_quality",
        "variant_name": "进攻8/92 晋升6只(多因子行业+质量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["industry_quality"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_defense",
        "variant_name": "进攻8/92 晋升6只(多因子质量防守)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_defense"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_trend_quality_defense",
        "variant_name": "进攻8/92 晋升6只(多因子趋势质量防守)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["trend_quality_defense"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_trend_lowvol_quality",
        "variant_name": "进攻8/92 晋升6只(多因子趋势低波质量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["trend_lowvol_quality"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_trend_momentum_quality",
        "variant_name": "进攻8/92 晋升6只(多因子趋势动量质量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["trend_momentum_quality"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_trend_industry_momentum",
        "variant_name": "进攻8/92 晋升6只(多因子趋势行业动量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["trend_industry_momentum"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol",
        "variant_name": "进攻8/92 晋升6只(多因子行业动量低波)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["industry_momentum_lowvol"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_industry_momentum_quality",
        "variant_name": "进攻8/92 晋升6只(多因子行业动量质量)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["industry_momentum_quality"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_trend_quality_rebalance",
        "variant_name": "进攻8/92 晋升6只(多因子趋势质量再平衡)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["trend_quality_rebalance"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance",
        "variant_name": "进攻8/92 晋升6只(多因子盈利低波再平衡)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["profitability_lowvol_rebalance"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_lowvol_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量低波再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_lowvol_reconfirm"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量低波现金防守再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_lowvol_cashguard_reconfirm"],
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_trend_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量趋势再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_trend_reconfirm"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量低波趋势再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_lowvol_trend_reconfirm"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_trend_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量趋势现金防守再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_trend_cashguard_reconfirm"],
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子盈利行业再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["profitability_industry_reconfirm"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_industry_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量行业再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_industry_reconfirm"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_industry_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量行业现金防守再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_industry_cashguard_reconfirm"],
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利现金防守再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_cashguard_reconfirm"],
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量防守现金再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_defense_cashguard_reconfirm"],
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量估值趋势成本守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_value_trend_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_lowvol_value_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量低波估值再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_lowvol_value_reconfirm"],
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_profitability_value_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子盈利估值现金防守再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["profitability_value_cashguard_reconfirm"],
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量成长信号再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_growth_signal_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_profitability_industry_signal_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子盈利行业信号再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["profitability_industry_signal_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_profitability_growth_signal_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子盈利成长信号再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["profitability_growth_signal_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.32,
        "satellite_risk_off_exposure": 0.32,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_industry_signal_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量行业信号现金再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_industry_signal_cashguard_reconfirm"],
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_growth_industry_cost_guard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量成长行业成本守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_growth_industry_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.32,
        "satellite_risk_off_exposure": 0.32,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量价值行业成本守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_value_industry_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量低波行业成本守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_lowvol_industry_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.68,
        "satellite_caution_exposure": 0.48,
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利行业防守再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_industry_defense_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.22,
        "satellite_risk_off_exposure": 0.22,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利信号成本守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_signal_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.68,
        "satellite_caution_exposure": 0.48,
        "core_risk_off_exposure": 0.28,
        "satellite_risk_off_exposure": 0.28,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利低波信号成本守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_lowvol_signal_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.24,
        "satellite_risk_off_exposure": 0.24,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_cost_guard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利价值低波行业成本守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_value_lowvol_industry_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.22,
        "satellite_risk_off_exposure": 0.22,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利价值低波趋势成本守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_value_lowvol_trend_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.65,
        "satellite_caution_exposure": 0.45,
        "core_risk_off_exposure": 0.22,
        "satellite_risk_off_exposure": 0.22,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利价值低波行业信号现金守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.64,
        "satellite_caution_exposure": 0.44,
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利价值低波趋势信号现金守门再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.63,
        "satellite_caution_exposure": 0.43,
        "core_risk_off_exposure": 0.18,
        "satellite_risk_off_exposure": 0.18,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利价值低波趋势信号现金守门风险20再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk18_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利信号现金守门风险18再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_signal_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.18,
        "satellite_risk_off_exposure": 0.18,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利信号现金守门风险16再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_signal_cost_guard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.61,
        "satellite_caution_exposure": 0.41,
        "core_risk_off_exposure": 0.16,
        "satellite_risk_off_exposure": 0.16,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk16_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利成长信号现金守门风险16再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["profitability_growth_signal_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.61,
        "satellite_caution_exposure": 0.41,
        "core_risk_off_exposure": 0.16,
        "satellite_risk_off_exposure": 0.16,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk16_reconfirm",
        "variant_name": "进攻8/92 晋升6只(多因子质量盈利成长趋势信号现金守门风险16再确认)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "multi_factor",
        "factor_weights": MULTI_FACTOR_PRESETS["quality_profitability_growth_trend_signal_cashguard_reconfirm"],
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.61,
        "satellite_caution_exposure": 0.41,
        "core_risk_off_exposure": 0.16,
        "satellite_risk_off_exposure": 0.16,
    },
    {
        "variant_id": "aggr_10_90_prom6_core_6_1",
        "variant_name": "进攻10/90 晋升6只(核心6-1动量)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off",
        "variant_name": "进攻8/92 晋升6只(熊市空仓)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
    },
    {
        "variant_id": "aggr_10_90_prom6_cash_off",
        "variant_name": "进攻10/90 晋升6只(熊市空仓)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
    },
    {
        "variant_id": "aggr_10_90_fast_ramp_cash_off",
        "variant_name": "进攻10/90 快速加仓(熊市空仓)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and",
        "variant_name": "进攻8/92 晋升6只(熊市空仓, and 规则)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
    },
    {
        "variant_id": "aggr_08_92_prom6_satellite_cost_guard",
        "variant_name": "进攻8/92 晋升6只(卫星成本防守)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "core_caution_exposure": 0.80,
        "satellite_risk_off_exposure": 0.25,
        "satellite_caution_exposure": 0.55,
        "promoted_core_sell_exit_percentile": 0.55,
    },
    {
        "variant_id": "aggr_10_90_fast_ramp_cash_off_and",
        "variant_name": "进攻10/90 快速加仓(熊市空仓, and 规则)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
    },
    {
        "variant_id": "aggr_08_92_prom6_full_risk",
        "variant_name": "进攻8/92 晋升6只(关闭熊市降仓)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_3_1_full_risk_cap40",
        "variant_name": "进攻8/92 晋升6只(核心3-1动量, 关闭熊市降仓, 单票40%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1_full_risk",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量, 关闭熊市降仓)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1_full_risk_cap40",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量, 关闭熊市降仓, 单票40%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1_full_risk_cap60",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量, 关闭熊市降仓, 单票60%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.60,
    },
    {
        "variant_id": "aggr_05_95_prom7_core_6_1_full_risk",
        "variant_name": "进攻5/95 晋升7只(核心6-1动量, 关闭熊市降仓)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
    },
    {
        "variant_id": "aggr_05_95_prom7_core_6_1_full_risk_cap40",
        "variant_name": "进攻5/95 晋升7只(核心6-1动量, 关闭熊市降仓, 单票40%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_05_95_prom7_core_3_1_full_risk_cap40",
        "variant_name": "进攻5/95 晋升7只(核心3-1动量, 关闭熊市降仓, 单票40%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_full_risk",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 关闭熊市降仓)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_full_risk_cap60",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 关闭熊市降仓, 单票60%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.60,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_full_risk_cap80",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 关闭熊市降仓, 单票80%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cap60",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 单票60%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "weight_cap": 0.60,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_cap60",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市空仓 and, 单票60%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.60,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_cap80",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市空仓 and, 单票80%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市降到30% and, 单票80%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市降到50% and, 单票80%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_04_96_prom3_core_6_1_cash_off_and_cap70",
        "variant_name": "进攻4/96 晋升3只(核心6-1动量, 熊市空仓 and, 单票70%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70",
        "variant_name": "进攻4/96 晋升3只(核心6-1动量, 熊市降到50% and, 单票70%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_06_94_prom4_core_6_1_full_risk_cap70",
        "variant_name": "进攻6/94 晋升4只(核心6-1动量, 关闭熊市降仓, 单票70%)",
        "winner_core_stable_share": 0.06,
        "winner_core_promoted_share": 0.94,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_06_94_prom4_core_6_1_cash_off_and_cap70",
        "variant_name": "进攻6/94 晋升4只(核心6-1动量, 熊市空仓 and, 单票70%)",
        "winner_core_stable_share": 0.06,
        "winner_core_promoted_share": 0.94,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap80",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票80%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_risk30_cap80",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市降到30% and, 单票80%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市降到50% and, 单票80%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_full_risk_cap80",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 关闭熊市降仓, 单票80%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_cash_off_and_cap90",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_cash_off_and_risk30_cap90",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 熊市降到30% and, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 熊市降到50% and, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_full_risk_cap90",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 关闭熊市降仓, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_cash_off_and_risk30_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 熊市降到30% and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_cash_off_and_risk50_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 熊市降到50% and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_full_risk_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 关闭熊市降仓, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_cash_off_and_cap90",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_cash_off_and_cap100",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_cash_off_and_cap100",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm80",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 6-1确认80)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.15,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 6-1确认80)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.15,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 6-1确认85+量能130)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_amount_surge_ratio": 1.30,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 6-1确认85+量能130)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_amount_surge_ratio": 1.30,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp70",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 首月70%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 0.70, 2: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 首月70%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 0.70, 2: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp85",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 首月85%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp85",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 首月85%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_biweekly",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 双周)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_biweekly",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 双周)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_weekly",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_03_97_prom1_core_6_1_cash_off_and_cap100",
        "variant_name": "进攻3/97 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_04_96_prom1_core_6_1_cash_off_and_cap100",
        "variant_name": "进攻4/96 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_cash_off_and_risk50_cap100",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 熊市降到50% and, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_cash_off_and_risk50_cap100",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 熊市降到50% and, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_full_risk_cap100",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 关闭熊市降仓, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_full_risk_cap100",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 关闭熊市降仓, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_3_1_cash_off_and_cap100",
        "variant_name": "进攻1/99 晋升1只(核心3-1动量, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_3_1_cash_off_and_cap100",
        "variant_name": "进攻2/98 晋升1只(核心3-1动量, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_3_1_full_risk_cap100",
        "variant_name": "进攻1/99 晋升1只(核心3-1动量, 关闭熊市降仓, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_3_1_full_risk_cap100",
        "variant_name": "进攻2/98 晋升1只(核心3-1动量, 关闭熊市降仓, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_theme_cash_off_and_cap100",
        "variant_name": "进攻1/99 晋升1只(核心主题强度, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "theme",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_theme_cash_off_and_cap100",
        "variant_name": "进攻2/98 晋升1只(核心主题强度, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "theme",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_theme_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升2只(核心主题强度, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "theme",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_theme_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(核心主题强度, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "theme",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom1_industry_trend_cash_off_and_cap100",
        "variant_name": "进攻1/99 晋升1只(行业趋势领涨, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "industry_trend",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_industry_trend_cash_off_and_cap100",
        "variant_name": "进攻2/98 晋升1只(行业趋势领涨, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "industry_trend",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom2_industry_trend_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升2只(行业趋势领涨, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "industry_trend",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_industry_trend_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(行业趋势领涨, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "industry_trend",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100",
        "variant_name": "进攻1/99 晋升1只(中周期量价动量, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "midcycle_momentum",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "fast_promotion_percentile": 0.12,
        "fast_promotion_min_amount_surge_ratio": 1.10,
    },
    {
        "variant_id": "aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100",
        "variant_name": "进攻2/98 晋升1只(中周期量价动量, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "midcycle_momentum",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
        "fast_promotion_percentile": 0.12,
        "fast_promotion_min_amount_surge_ratio": 1.10,
    },
    {
        "variant_id": "aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升2只(中周期量价动量, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "midcycle_momentum",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
        "fast_promotion_percentile": 0.12,
        "fast_promotion_min_amount_surge_ratio": 1.10,
    },
    {
        "variant_id": "aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(中周期量价动量, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "midcycle_momentum",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
        "fast_promotion_percentile": 0.12,
        "fast_promotion_min_amount_surge_ratio": 1.10,
    },
    {
        "variant_id": "aggr_01_99_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100",
        "variant_name": "进攻1/99 晋升1只(核心6-1动量, 6-1晋升前15%, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "momentum_6_1",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_02_98_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100",
        "variant_name": "进攻2/98 晋升1只(核心6-1动量, 6-1晋升前15%, 熊市空仓 and, 单票100%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 1,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "momentum_6_1",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 1.00,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前10%, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.10,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前10%, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.10,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前20%, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.12,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前20%, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.12,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留30%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留30%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留30%, 晋升保留前80%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留30%, 晋升保留前80%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留30%, 晋升保留前60%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留30%, 晋升保留前60%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm75_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 熊市保留30%, 晋升保留前60%, 恢复确认75, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm75_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 熊市保留30%, 晋升保留前60%, 恢复确认75, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm80_amt110_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 熊市保留30%, 晋升保留前60%, 恢复确认80+量能110, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm80_amt110_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 熊市保留30%, 晋升保留前60%, 恢复确认80+量能110, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard",
        "variant_name": "进攻2/98 晋升2只(量价前15%, 动量三档40%, 恢复75, 单票80%, 成本防守)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.75,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard_v2",
        "variant_name": "进攻2/98 晋升2只(量价前15%, 动量三档40%, 恢复75, 单票80%, 严格成本防守v2)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.78,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.15,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.38,
        "satellite_risk_off_exposure": 0.38,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard",
        "variant_name": "进攻2/98 晋升2只(量价前15%, 动量三档40%, 恢复75, 谨慎仓80/55, 单票80%, 成本防守)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard",
        "variant_name": "进攻2/98 晋升2只(量价前15%, 动量三档35%, 出场55%, 恢复80, 谨慎仓80/55, 单票80%, 成本防守)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit58_reconfirm80_cap80_cost_guard_v3",
        "variant_name": "进攻2/98 晋升2只(量价前15%, 动量三档35%, 出场58%, 恢复80, 单票80%, 成本防守v3)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.58,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.89,
        "fast_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.15,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.58,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution75_cap75_cost_guard_v4",
        "variant_name": "进攻2/98 晋升2只(量价前15%, 动量三档35%, 出场55%, 恢复82, 谨慎75%, 单票75%, 成本防守v4)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.82,
        "standard_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.90,
        "fast_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.15,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.75,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.75,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution70_cap70_cost_guard_v5",
        "variant_name": "进攻2/98 晋升2只(量价前15%, 动量三档35%, 出场55%, 恢复82, 谨慎70%, 单票70%, 成本防守v5)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.82,
        "standard_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.90,
        "fast_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.15,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.48,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution70_cap65_cost_guard_v6",
        "variant_name": "进攻2/98 晋升2只(量价前12%, 动量三档35%, 出场55%, 恢复85, 谨慎70%, 单票65%, 成本防守v6)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.85,
        "standard_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.18,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.48,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.65,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution65_cap60_cost_guard_v7",
        "variant_name": "进攻2/98 晋升2只(量价前12%, 动量三档35%, 出场55%, 恢复85, 谨慎65%, 单票60%, 成本防守v7)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.85,
        "standard_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.18,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.65,
        "satellite_caution_exposure": 0.45,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.60,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk32_mom_exit52_reconfirm88_caution60_cap55_cost_guard_v8",
        "variant_name": "进攻2/98 晋升2只(量价前10%, 动量三档32%, 出场52%, 恢复88, 谨慎60%, 单票55%, 成本防守v8)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.10,
        "standard_promotion_min_momentum_6_1_rank": 0.88,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_momentum_6_1_rank": 0.93,
        "fast_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.20,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.60,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.32,
        "satellite_risk_off_exposure": 0.32,
        "promoted_core_sell_exit_percentile": 0.52,
        "weight_cap": 0.55,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk34_mom_exit54_reconfirm86_caution62_cap58_cost_guard_v9",
        "variant_name": "进攻2/98 晋升2只(量价前10%, 动量三档34%, 出场54%, 恢复86, 谨慎62%, 单票58%, 成本防守v9)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.10,
        "standard_promotion_min_momentum_6_1_rank": 0.86,
        "standard_promotion_min_momentum_3_1_rank": 0.63,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_momentum_6_1_rank": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.67,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.18,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.44,
        "core_risk_off_exposure": 0.34,
        "satellite_risk_off_exposure": 0.34,
        "promoted_core_sell_exit_percentile": 0.54,
        "weight_cap": 0.58,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk36_mom_exit54_reconfirm84_caution64_cap55_cost_guard_v10",
        "variant_name": "进攻2/98 晋升2只(量价前10%, 动量三档36%, 出场54%, 恢复84, 谨慎64%, 单票55%, 成本防守v10)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.10,
        "standard_promotion_min_momentum_6_1_rank": 0.84,
        "standard_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_momentum_6_1_rank": 0.91,
        "fast_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.18,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.64,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.36,
        "satellite_risk_off_exposure": 0.36,
        "promoted_core_sell_exit_percentile": 0.54,
        "weight_cap": 0.55,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk36_mom_exit54_reconfirm84_caution66_cap50_cost_guard_v11",
        "variant_name": "进攻2/98 晋升2只(量价前12%, 动量三档36%, 出场54%, 恢复84, 谨慎66%, 单票50%, 成本防守v11)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.84,
        "standard_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.91,
        "fast_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.18,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.47,
        "core_risk_off_exposure": 0.36,
        "satellite_risk_off_exposure": 0.36,
        "promoted_core_sell_exit_percentile": 0.54,
        "weight_cap": 0.50,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk34_mom_exit52_reconfirm86_caution64_cap48_cost_guard_v12",
        "variant_name": "进攻2/98 晋升2只(量价前12%, 动量三档34%, 出场52%, 恢复86, 谨慎64%, 单票48%, 成本防守v12)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.86,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.20,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.64,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.34,
        "satellite_risk_off_exposure": 0.34,
        "promoted_core_sell_exit_percentile": 0.52,
        "weight_cap": 0.48,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm88_caution62_cap50_cost_guard_v13",
        "variant_name": "进攻2/98 晋升2只(量价前12%, 动量三档32%, 出场52%, 恢复88, 谨慎62%, 单票50%, 成本防守v13)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.88,
        "standard_promotion_min_momentum_3_1_rank": 0.65,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.93,
        "fast_promotion_min_momentum_3_1_rank": 0.69,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.20,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.44,
        "core_risk_off_exposure": 0.32,
        "satellite_risk_off_exposure": 0.32,
        "promoted_core_sell_exit_percentile": 0.52,
        "weight_cap": 0.50,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm90_caution60_cap45_cost_guard_v14",
        "variant_name": "进攻2/98 晋升2只(量价前12%, 动量三档30%, 出场50%, 恢复90, 谨慎60%, 单票45%, 成本防守v14)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.90,
        "standard_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.94,
        "fast_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.22,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.60,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.50,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk32_mom_exit52_reconfirm88_caution62_cap40_cost_guard_v15",
        "variant_name": "进攻3/97 晋升3只(量价前14%, 动量三档32%, 出场52%, 恢复88, 谨慎62%, 单票40%, 成本防守v15)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.14,
        "standard_promotion_min_momentum_6_1_rank": 0.88,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.09,
        "fast_promotion_min_momentum_6_1_rank": 0.93,
        "fast_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.18,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.44,
        "core_risk_off_exposure": 0.32,
        "satellite_risk_off_exposure": 0.32,
        "promoted_core_sell_exit_percentile": 0.52,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk34_mom_exit54_reconfirm86_caution64_cap42_cost_guard_v16",
        "variant_name": "进攻3/97 晋升3只(量价前14%, 动量三档34%, 出场54%, 恢复86, 谨慎64%, 单票42%, 成本防守v16)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.14,
        "standard_promotion_min_momentum_6_1_rank": 0.86,
        "standard_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_percentile": 0.09,
        "fast_promotion_min_momentum_6_1_rank": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.18,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.64,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.34,
        "satellite_risk_off_exposure": 0.34,
        "promoted_core_sell_exit_percentile": 0.54,
        "weight_cap": 0.42,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17",
        "variant_name": "进攻3/97 晋升3只(量价前14%, 动量三档30%, 出场50%, 恢复92, 谨慎60%, 单票40%, 成本防守v17)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.14,
        "standard_promotion_min_momentum_6_1_rank": 0.92,
        "standard_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_percentile": 0.09,
        "fast_promotion_min_momentum_6_1_rank": 0.95,
        "fast_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.20,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.60,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.50,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap32_cost_guard_v18",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档28%, 出场48%, 恢复94, 谨慎58%, 单票32%, 成本防守v18)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.94,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.96,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.22,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.58,
        "satellite_caution_exposure": 0.40,
        "core_risk_off_exposure": 0.28,
        "satellite_risk_off_exposure": 0.28,
        "promoted_core_sell_exit_percentile": 0.48,
        "weight_cap": 0.32,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档26%, 出场46%, 恢复96, 谨慎56%, 单票28%, 成本防守v19)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.96,
        "standard_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.97,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.24,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.56,
        "satellite_caution_exposure": 0.38,
        "core_risk_off_exposure": 0.26,
        "satellite_risk_off_exposure": 0.26,
        "promoted_core_sell_exit_percentile": 0.46,
        "weight_cap": 0.28,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution54_cap24_cost_guard_v20",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档24%, 出场44%, 恢复97, 谨慎54%, 单票24%, 成本防守v20)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.97,
        "standard_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_percentile": 0.075,
        "fast_promotion_min_momentum_6_1_rank": 0.98,
        "fast_promotion_min_momentum_3_1_rank": 0.76,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.26,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.54,
        "satellite_caution_exposure": 0.36,
        "core_risk_off_exposure": 0.24,
        "satellite_risk_off_exposure": 0.24,
        "promoted_core_sell_exit_percentile": 0.44,
        "weight_cap": 0.24,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution52_cap22_cost_guard_v21",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档22%, 出场42%, 恢复98, 谨慎52%, 单票22%, 成本防守v21)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.98,
        "standard_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_momentum_6_1_rank": 0.985,
        "fast_promotion_min_momentum_3_1_rank": 0.78,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.28,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.52,
        "satellite_caution_exposure": 0.34,
        "core_risk_off_exposure": 0.22,
        "satellite_risk_off_exposure": 0.22,
        "promoted_core_sell_exit_percentile": 0.42,
        "weight_cap": 0.22,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档26%, 出场46%, 恢复96, 谨慎56%, 单票28%, 成本防守v22收益修复)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.96,
        "standard_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.97,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.24,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.56,
        "satellite_caution_exposure": 0.38,
        "core_risk_off_exposure": 0.26,
        "satellite_risk_off_exposure": 0.26,
        "promoted_core_sell_exit_percentile": 0.46,
        "weight_cap": 0.28,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档28%, 出场48%, 恢复94, 谨慎58%, 单票30%, 成本防守v23风险确认)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.94,
        "standard_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.96,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.24,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.58,
        "satellite_caution_exposure": 0.40,
        "core_risk_off_exposure": 0.28,
        "satellite_risk_off_exposure": 0.28,
        "promoted_core_sell_exit_percentile": 0.48,
        "weight_cap": 0.30,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm98_caution54_cap24_cost_guard_v36_risk_reconfirm",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档24%, 出场44%, 恢复98, 谨慎54%, 单票24%, 成本防守v36风险确认)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.98,
        "standard_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_percentile": 0.075,
        "fast_promotion_min_momentum_6_1_rank": 0.985,
        "fast_promotion_min_momentum_3_1_rank": 0.78,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.28,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.54,
        "satellite_caution_exposure": 0.36,
        "core_risk_off_exposure": 0.24,
        "satellite_risk_off_exposure": 0.24,
        "promoted_core_sell_exit_percentile": 0.44,
        "weight_cap": 0.24,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm92_caution60_cap32_cost_guard_v24_medium_cycle",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档30%, 出场50%, 恢复92, 谨慎60%, 单票32%, 成本防守v24中周期)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.92,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.95,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.22,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.60,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.50,
        "weight_cap": 0.32,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle",
        "variant_name": "进攻3/97 晋升3只(量价前12%, 动量三档32%, 出场52%, 恢复90, 谨慎62%, 单票28%, 成本防守v25中周期)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.90,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.94,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.22,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.44,
        "core_risk_off_exposure": 0.32,
        "satellite_risk_off_exposure": 0.32,
        "promoted_core_sell_exit_percentile": 0.52,
        "weight_cap": 0.28,
    },
    {
        "variant_id": "aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm95_caution62_cap28_cost_guard_v26_medium_cycle",
        "variant_name": "进攻4/96 晋升4只(量价前14%, 动量三档30%, 出场50%, 恢复95, 谨慎62%, 单票28%, 成本防守v26中周期)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.14,
        "standard_promotion_min_momentum_6_1_rank": 0.90,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.09,
        "fast_promotion_min_momentum_6_1_rank": 0.94,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.22,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.44,
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.50,
        "weight_cap": 0.28,
    },
    {
        "variant_id": "aggr_04_96_prom4_core_6_1_promo_liqmom_top13_risk28_mom_exit48_reconfirm96_caution64_cap24_cost_guard_v27_medium_cycle",
        "variant_name": "进攻4/96 晋升4只(量价前13%, 动量三档28%, 出场48%, 恢复96, 谨慎64%, 单票24%, 成本防守v27中周期)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.13,
        "standard_promotion_min_momentum_6_1_rank": 0.96,
        "standard_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.97,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.24,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.64,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.28,
        "satellite_risk_off_exposure": 0.28,
        "promoted_core_sell_exit_percentile": 0.48,
        "weight_cap": 0.24,
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk28_exit46_cap24_cost_guard_v28",
        "variant_name": "进攻3/97 晋升3只(量价弹性双周, 风险28%, 出场46%, 单票24%, 成本防守v28)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.14,
        "standard_promotion_min_momentum_6_1_rank": 0.92,
        "standard_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_percentile": 0.09,
        "fast_promotion_min_momentum_6_1_rank": 0.95,
        "fast_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.18,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.48,
        "core_risk_off_exposure": 0.28,
        "satellite_risk_off_exposure": 0.28,
        "promoted_core_sell_exit_percentile": 0.46,
        "weight_cap": 0.24,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29",
        "variant_name": "进攻3/97 晋升3只(量价弹性双周, 风险24%, 出场44%, 单票20%, 成本防守v29)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.14,
        "standard_promotion_min_momentum_6_1_rank": 0.93,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.09,
        "fast_promotion_min_momentum_6_1_rank": 0.96,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.20,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.64,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.24,
        "satellite_risk_off_exposure": 0.24,
        "promoted_core_sell_exit_percentile": 0.44,
        "weight_cap": 0.20,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn",
        "variant_name": "进攻3/97 晋升3只(量价弹性双周, 风险22%, 出场42%, 单票18%, 成本防守v35低换手)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.14,
        "standard_promotion_min_momentum_6_1_rank": 0.94,
        "standard_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_percentile": 0.09,
        "fast_promotion_min_momentum_6_1_rank": 0.97,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.22,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.44,
        "core_risk_off_exposure": 0.22,
        "satellite_risk_off_exposure": 0.22,
        "promoted_core_sell_exit_percentile": 0.42,
        "weight_cap": 0.18,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle",
        "variant_name": "进攻4/96 晋升4只(量价前12%, 动量三档26%, 出场46%, 恢复96, 谨慎58%, 单票22%, 成本防守v30中周期)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.96,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.97,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_recent_1m_return": 0.015,
        "fast_promotion_min_amount_surge_ratio": 1.22,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.58,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.26,
        "satellite_risk_off_exposure": 0.26,
        "promoted_core_sell_exit_percentile": 0.46,
        "weight_cap": 0.22,
    },
    {
        "variant_id": "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v31_medium_cycle",
        "variant_name": "进攻4/96 晋升4只(量价前12%, 动量三档24%, 出场44%, 恢复97, 谨慎56%, 单票20%, 成本防守v31中周期)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.97,
        "standard_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.98,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_recent_1m_return": 0.015,
        "fast_promotion_min_amount_surge_ratio": 1.24,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.56,
        "satellite_caution_exposure": 0.40,
        "core_risk_off_exposure": 0.24,
        "satellite_risk_off_exposure": 0.24,
        "promoted_core_sell_exit_percentile": 0.44,
        "weight_cap": 0.20,
    },
    {
        "variant_id": "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v32_capacity_stress",
        "variant_name": "进攻4/96 晋升4只(量价前12%, 动量三档22%, 出场42%, 恢复98, 谨慎54%, 单票18%, 成本防守v32容量压力)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.98,
        "standard_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.99,
        "fast_promotion_min_momentum_3_1_rank": 0.76,
        "fast_promotion_min_recent_1m_return": 0.015,
        "fast_promotion_min_amount_surge_ratio": 1.26,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.54,
        "satellite_caution_exposure": 0.38,
        "core_risk_off_exposure": 0.22,
        "satellite_risk_off_exposure": 0.22,
        "promoted_core_sell_exit_percentile": 0.42,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap18_cost_guard_v33_medium_cycle_repair",
        "variant_name": "进攻4/96 晋升4只(量价前10%, 动量三档24%, 出场44%, 恢复97, 谨慎56%, 单票18%, 成本防守v33中周期修复)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.10,
        "standard_promotion_min_momentum_6_1_rank": 0.97,
        "standard_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_momentum_6_1_rank": 0.98,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_recent_1m_return": 0.015,
        "fast_promotion_min_amount_surge_ratio": 1.24,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.56,
        "satellite_caution_exposure": 0.40,
        "core_risk_off_exposure": 0.24,
        "satellite_risk_off_exposure": 0.24,
        "promoted_core_sell_exit_percentile": 0.44,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v34_reconfirm_balance",
        "variant_name": "进攻4/96 晋升4只(量价前10%, 动量三档26%, 出场46%, 恢复96, 谨慎58%, 单票18%, 成本防守v34确认平衡)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.10,
        "standard_promotion_min_momentum_6_1_rank": 0.96,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_momentum_6_1_rank": 0.97,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_recent_1m_return": 0.012,
        "fast_promotion_min_amount_surge_ratio": 1.22,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.58,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.26,
        "satellite_risk_off_exposure": 0.26,
        "promoted_core_sell_exit_percentile": 0.46,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复75, 单票80%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 单票80%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 谨慎仓80/55, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 谨慎仓80/55, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_caution80_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 谨慎仓80/55, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_caution80_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 谨慎仓80/55, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留45%, 晋升保留前60%, 恢复确认70, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.45,
        "satellite_risk_off_exposure": 0.45,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm70_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前55%, 恢复确认70, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认65, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认65, 谨慎仓70/50, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留35%, 晋升保留前60%, 恢复确认75, 谨慎仓70/50, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认80, 谨慎仓70/50, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留30%, or, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留30%, or, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_mom_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 动量触发保留30%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_mom_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 动量触发保留30%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_ma_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 均线触发保留30%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "below_ma",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_ma_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 均线触发保留30%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "below_ma",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk50_mom_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前12%, 动量三档保留50%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk50_mom_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前12%, 动量三档保留50%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top18_risk50_mom_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前18%, 动量三档保留50%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.11,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top18_risk50_mom_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前18%, 动量三档保留50%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.11,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 晋升保留前80%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 晋升保留前80%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution80_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 谨慎仓80/55, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution80_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 谨慎仓80/55, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution75_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 谨慎仓75/50, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.75,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution75_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 谨慎仓75/50, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.75,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认75, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认75, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认70, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认70, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认65, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认65, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档50%, 恢复65, 单票80%, 成本防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.78,
        "satellite_caution_exposure": 0.58,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.65,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档50%, 恢复65, 单票80%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档50%, 恢复65, 单票85%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.85,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档50%, 恢复70, 单票85%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.85,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档50%, 恢复65, 单票70%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档50%, 恢复65, 单票75%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.75,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档45%, 恢复70, 单票75%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.75,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档50%, 恢复65, 谨慎仓75/50, 单票70%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.75,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档50%, 恢复65, 谨慎仓80/55, 单票70%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.65,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.80,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档45%, 出场55%, 恢复70, 谨慎仓80/55, 单票80%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档45%, 出场55%, 恢复75, 谨慎仓85/58, 单票75%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.86,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.015,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.85,
        "satellite_caution_exposure": 0.58,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.75,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档45%, 出场55%, 恢复75, 谨慎仓85/58, 单票65%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.86,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.015,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.85,
        "satellite_caution_exposure": 0.58,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.65,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档45%, 出场55%, 恢复75, 谨慎仓85/58, 单票60%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.86,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.015,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.85,
        "satellite_caution_exposure": 0.58,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.60,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前12%, 动量三档45%, 出场55%, 恢复80, 谨慎仓85/58, 单票70%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.12,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.58,
        "fast_promotion_percentile": 0.08,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_min_recent_1m_return": 0.015,
        "fast_promotion_min_amount_surge_ratio": 1.12,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.85,
        "satellite_caution_exposure": 0.58,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档35%, 出场55%, 恢复75, 谨慎仓75/50, 单票80%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.75,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档35%, 出场55%, 恢复75, 谨慎仓80/55, 单票70%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档40%, 出场55%, 恢复75, 谨慎仓80/55, 单票75%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.55,
        "weight_cap": 0.75,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档40%, 出场50%, 恢复75, 谨慎仓80/55, 单票75%, 现金防守)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "and",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.50,
        "weight_cap": 0.75,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认75, 谨慎仓80/55, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认75, 谨慎仓80/55, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.80,
        "satellite_caution_exposure": 0.55,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution75_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认75, 谨慎仓75/50, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.75,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution75_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认75, 谨慎仓75/50, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.75,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm80_amt110_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认80+量能110, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm80_amt110_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认80+量能110, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution70_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 谨慎仓70/50, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution70_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 谨慎仓70/50, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution60_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 谨慎仓60/50, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.60,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution60_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 谨慎仓60/50, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.60,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm75_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升确认75, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm75_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升确认75, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.75,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.85,
        "fast_promotion_min_recent_1m_return": 0.01,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm80_amt110_cap95",
        "variant_name": "进攻1/99 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升确认80+量能110, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm80_amt110_cap95",
        "variant_name": "进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升确认80+量能110, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_min_recent_1m_return": 0.02,
        "fast_promotion_min_amount_surge_ratio": 1.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 均线三档保留50%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "below_ma",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 均线三档保留50%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "below_ma",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap80",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 单票80%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap70",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 单票70%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_ramp85_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 首月85%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 0.85, 2: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_ramp70_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 首月70%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 0.70, 2: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit80_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 晋升保留前80%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit80_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 晋升保留前80%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit60_cap95",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 晋升保留前60%, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit60_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 熊市保留50%, or, 晋升保留前60%, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_amount_surge_ratio": 1.05,
        "market_risk_off_rule": "or",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_cash_off_and_cap90",
        "variant_name": "进攻1/99 晋升2只(默认动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_01_99_prom2_full_risk_cap90",
        "variant_name": "进攻1/99 晋升2只(默认动量, 关闭熊市降仓, 单票90%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_02_98_prom2_cash_off_and_cap90",
        "variant_name": "进攻2/98 晋升2只(默认动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_02_98_prom2_full_risk_cap90",
        "variant_name": "进攻2/98 晋升2只(默认动量, 关闭熊市降仓, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_01_99_prom3_core_6_1_cash_off_and_cap90",
        "variant_name": "进攻1/99 晋升3只(核心6-1动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_01_99_prom3_core_6_1_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升3只(核心6-1动量, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_6_1_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_3_1_cash_off_and_cap90",
        "variant_name": "进攻1/99 晋升2只(核心3-1动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_3_1_cash_off_and_cap95",
        "variant_name": "进攻1/99 晋升2只(核心3-1动量, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_3_1_cash_off_and_cap90",
        "variant_name": "进攻2/98 晋升2只(核心3-1动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_3_1_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(核心3-1动量, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_3_1_cash_off_and_risk50_cap95",
        "variant_name": "进攻1/99 晋升2只(核心3-1动量, 熊市降到50% and, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_3_1_full_risk_cap95",
        "variant_name": "进攻1/99 晋升2只(核心3-1动量, 关闭熊市降仓, 单票95%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_3_1_cash_off_and_risk50_cap95",
        "variant_name": "进攻2/98 晋升2只(核心3-1动量, 熊市降到50% and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_core_3_1_full_risk_cap95",
        "variant_name": "进攻2/98 晋升2只(核心3-1动量, 关闭熊市降仓, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "3_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom3_core_6_1_cash_off_and_cap90",
        "variant_name": "进攻2/98 晋升3只(核心6-1动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_02_98_prom3_core_6_1_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升3只(核心6-1动量, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap90",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap90",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市降到50% and, 单票90%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_04_96_prom2_core_6_1_cash_off_and_cap90",
        "variant_name": "进攻4/96 晋升2只(核心6-1动量, 熊市空仓 and, 单票90%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_04_96_prom2_core_6_1_cash_off_and_cap80",
        "variant_name": "进攻4/96 晋升2只(核心6-1动量, 熊市空仓 and, 单票80%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_04_96_prom2_core_6_1_cash_off_and_risk30_cap80",
        "variant_name": "进攻4/96 晋升2只(核心6-1动量, 熊市降到30% and, 单票80%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_04_96_prom2_core_6_1_cash_off_and_risk50_cap80",
        "variant_name": "进攻4/96 晋升2只(核心6-1动量, 熊市降到50% and, 单票80%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.80,
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_full_risk_cap80_biweekly",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 满风险, 单票80%, 双周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.80,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_full_risk_cap80_weekly",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 满风险, 单票80%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.80,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap80_biweekly",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票80%, 双周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.80,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票70%, 双周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.70,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票75%, 双周成本守门)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.86,
        "weight_cap": 0.75,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly_cost_guard",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票70%, 双周成本守门)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.84,
        "weight_cap": 0.70,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap65_biweekly_cost_guard",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票65%, 双周成本守门)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.82,
        "weight_cap": 0.65,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票60%, 双周成本守门)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.60,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票60%, 双周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.60,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_cap80_weekly",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市空仓 and, 单票80%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.80,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80_biweekly",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市降到50% and, 单票80%, 双周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.80,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80_weekly",
        "variant_name": "进攻3/97 晋升2只(核心6-1动量, 熊市降到50% and, 单票80%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.80,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_cash_off_and_cap90_biweekly",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票90%, 双周)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_cash_off_and_cap90_weekly",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票90%, 单周)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.90,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_cash_off_and_cap95_biweekly",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%, 双周)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly",
        "variant_name": "进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%, 单周)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.95,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_full_risk_cap80_biweekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 满风险, 单票80%, 双周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.80,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_full_risk_cap80_weekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 满风险, 单票80%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.80,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_biweekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市空仓 and, 单票60%, 双周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.60,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_cap50_biweekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市空仓 and, 单票50%, 双周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.50,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_weekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市空仓 and, 单票60%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_biweekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市降到50% and, 单票80%, 双周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.80,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市降到50% and, 单票80%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "weight_cap": 0.80,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1_full_risk_cap40_biweekly",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量, 满风险, 单票40%, 双周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.40,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量, 满风险, 单票40%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.40,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1_full_risk_cap60_biweekly",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 双周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.60,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_full_risk_cap60_biweekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 满风险, 单票60%, 双周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.60,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_biweekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓, and 规则, 双周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "rebalance_frequency": "biweekly",
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_full_risk_cap60_weekly",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 满风险, 单票60%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓, and 规则, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "rebalance_frequency": "weekly",
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit90_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票50%, 持有2周, 换手12%, 出场90%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.50,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.12,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap55_hold2_turn10_exit92_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票55%, 持有2周, 换手10%, 出场92%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有2周, 换手12%, 出场92%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.12,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有2周, 换手12%, 出场90%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.12,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手8%, 出场92%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 3,
        "weekly_turnover_cap": 0.08,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 3,
        "weekly_turnover_cap": 0.05,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn06_exit92_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手6%, 出场92%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 3,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap55_hold3_turn06_exit92_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票55%, 持有3周, 换手6%, 出场92%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 3,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap55_hold3_turn04_exit94_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票55%, 持有3周, 换手4%, 出场94%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 3,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有4周, 换手6%, 出场94%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap58_hold4_turn03_exit96_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市空仓and, 单票58%, 持有4周, 换手3%, 出场96%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.96,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly",
        "variant_name": "进攻8/92 晋升6只(熊市25%, 单票58%, 持有4周, 换手4%, 出场94%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit92_risk25_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市25%, 单票58%, 持有4周, 换手4%, 出场92%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市25%, 单票58%, 持有5周, 换手3%, 出场94%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap58_hold6_turn02_exit96_risk25_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市25%, 单票58%, 持有6周, 换手2%, 出场96%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.96,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.02,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市25%, 单票58%, 持有5周, 换手4%, 出场95%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.95,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk20_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市20%, 单票58%, 持有5周, 换手4%, 出场95%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "promoted_core_sell_exit_percentile": 0.95,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap56_hold6_turn03_exit96_risk20_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市20%, 单票56%, 持有6周, 换手3%, 出场96%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "promoted_core_sell_exit_percentile": 0.96,
        "weight_cap": 0.56,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap56_hold5_turn04_exit94_risk20_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市20%, 单票56%, 持有5周, 换手4%, 出场94%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.56,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市20%, 单票56%, 持有5周, 换手5%, 出场96%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "promoted_core_sell_exit_percentile": 0.96,
        "weight_cap": 0.56,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.05,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk18_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市18%, 单票54%, 持有5周, 换手5%, 出场96%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.18,
        "satellite_risk_off_exposure": 0.18,
        "promoted_core_sell_exit_percentile": 0.96,
        "weight_cap": 0.54,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.05,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit96_risk18_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市18%, 单票52%, 持有6周, 换手4%, 出场96%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.18,
        "satellite_risk_off_exposure": 0.18,
        "promoted_core_sell_exit_percentile": 0.96,
        "weight_cap": 0.52,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap52_hold5_turn05_exit98_risk18_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市18%, 单票52%, 持有5周, 换手5%, 出场98%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.18,
        "satellite_risk_off_exposure": 0.18,
        "promoted_core_sell_exit_percentile": 0.98,
        "weight_cap": 0.52,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.05,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit98_risk16_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市16%, 单票50%, 持有5周, 换手5%, 出场98%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.16,
        "satellite_risk_off_exposure": 0.16,
        "promoted_core_sell_exit_percentile": 0.98,
        "weight_cap": 0.50,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.05,
    },
    {
        "variant_id": "aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly",
        "variant_name": "进攻8/92 晋升6只(成本压力熊市16%, 单票50%, 持有6周, 换手4%, 出场98%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.16,
        "satellite_risk_off_exposure": 0.16,
        "promoted_core_sell_exit_percentile": 0.98,
        "weight_cap": 0.50,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_weekly_alpha_balanced_risk50_cap40_hold2_turn40_weekly",
        "variant_name": "进攻8/92 晋升6只(周频Alpha均衡, 熊市50%, 单票40%, 持有2周, 换手40%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_balanced",
        "promotion_signal_mode": "weekly_alpha_balanced",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.40,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.40,
    },
    {
        "variant_id": "aggr_05_95_prom3_weekly_alpha_balanced_risk50_cap60_hold2_turn30_weekly",
        "variant_name": "进攻5/95 晋升3只(周频Alpha均衡, 熊市50%, 单票60%, 持有2周, 换手30%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_balanced",
        "promotion_signal_mode": "weekly_alpha_balanced",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.30,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_balanced_cashoff_cap80_hold3_turn25_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha均衡, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_balanced",
        "promotion_signal_mode": "weekly_alpha_balanced",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.80,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 3,
        "weekly_turnover_cap": 0.25,
    },
    {
        "variant_id": "aggr_08_92_prom6_weekly_alpha_breakout_risk50_cap40_hold2_turn40_weekly",
        "variant_name": "进攻8/92 晋升6只(周频Alpha突破, 熊市50%, 单票40%, 持有2周, 换手40%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_breakout",
        "promotion_signal_mode": "weekly_alpha_breakout",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.40,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.40,
    },
    {
        "variant_id": "aggr_05_95_prom3_weekly_alpha_breakout_risk50_cap60_hold2_turn30_weekly",
        "variant_name": "进攻5/95 晋升3只(周频Alpha突破, 熊市50%, 单票60%, 持有2周, 换手30%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_breakout",
        "promotion_signal_mode": "weekly_alpha_breakout",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.30,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_breakout_cashoff_cap80_hold3_turn25_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha突破, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_breakout",
        "promotion_signal_mode": "weekly_alpha_breakout",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.80,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 3,
        "weekly_turnover_cap": 0.25,
    },
    {
        "variant_id": "aggr_08_92_prom6_weekly_alpha_pullback_risk50_cap40_hold2_turn40_weekly",
        "variant_name": "进攻8/92 晋升6只(周频Alpha回踩, 熊市50%, 单票40%, 持有2周, 换手40%, 单周)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.40,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.40,
    },
    {
        "variant_id": "aggr_05_95_prom3_weekly_alpha_pullback_risk50_cap60_hold2_turn30_weekly",
        "variant_name": "进攻5/95 晋升3只(周频Alpha回踩, 熊市50%, 单票60%, 持有2周, 换手30%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 2,
        "weekly_turnover_cap": 0.30,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.80,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 3,
        "weekly_turnover_cap": 0.25,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票70%, 持有4周, 换手20%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.70,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.20,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn15_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票65%, 持有5周, 换手15%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.65,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.15,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有6周, 换手12%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.12,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold7_turn10_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票55%, 持有7周, 换手10%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.82,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold8_turn08_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票50%, 持有8周, 换手8%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.85,
        "weight_cap": 0.50,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.08,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票45%, 持有9周, 换手6%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.88,
        "weight_cap": 0.45,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 9,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票50%, 持有10周, 换手6%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.88,
        "weight_cap": 0.50,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 10,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold9_turn08_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票55%, 持有9周, 换手8%, 宽出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 9,
        "weekly_turnover_cap": 0.08,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有8周, 换手10%, 宽出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn10_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市30%, 单票60%, 持有8周, 换手10%, 宽出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold6_turn12_exit85_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票60%, 持有6周, 换手12%, 出场85%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "promoted_core_sell_exit_percentile": 0.85,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.12,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票65%, 持有5周, 换手10%, 出场85%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.85,
        "weight_cap": 0.65,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn08_exit85_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有7周, 换手8%, 出场85%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.85,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.08,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票62%, 持有6周, 换手10%, 出场88%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.00,
        "satellite_risk_off_exposure": 0.00,
        "promoted_core_sell_exit_percentile": 0.88,
        "weight_cap": 0.62,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap55_hold4_turn18_weekly",
        "variant_name": "进攻5/95 晋升3只(周频Alpha回踩, 熊市40%, 单票55%, 持有4周, 换手18%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.75,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.18,
    },
    {
        "variant_id": "aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap50_hold4_turn18_exit85_weekly",
        "variant_name": "进攻5/95 晋升3只(周频Alpha回踩, 熊市40%, 单票50%, 持有4周, 换手18%, 出场85%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.85,
        "weight_cap": 0.50,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.18,
    },
    {
        "variant_id": "aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap50_hold5_turn14_exit85_weekly",
        "variant_name": "进攻5/95 晋升3只(周频Alpha回踩, 成本防守, 单票50%, 持有5周, 换手14%, 出场85%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.45,
        "satellite_risk_off_exposure": 0.45,
        "promoted_core_sell_exit_percentile": 0.85,
        "weight_cap": 0.50,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.14,
    },
    {
        "variant_id": "aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap45_hold5_turn12_exit90_weekly",
        "variant_name": "进攻5/95 晋升3只(周频Alpha回踩, 成本防守, 单票45%, 持有5周, 换手12%, 出场90%, 单周)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.45,
        "satellite_risk_off_exposure": 0.45,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.45,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.12,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold4_turn16_exit85_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票75%, 持有4周, 换手16%, 出场85%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.85,
        "weight_cap": 0.75,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.16,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn14_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票70%, 持有4周, 换手14%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.70,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 4,
        "weekly_turnover_cap": 0.14,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票75%, 持有5周, 换手12%, 出场88%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.88,
        "weight_cap": 0.75,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.12,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票68%, 持有5周, 换手10%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.68,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk35_cap70_hold5_turn10_exit88_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市35%, 单票70%, 持有5周, 换手10%, 出场88%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.88,
        "weight_cap": 0.70,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票55%, 持有6周, 换手10%, 出场88%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "promoted_core_sell_exit_percentile": 0.88,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票68%, 持有5周, 换手10%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.68,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 5,
        "weekly_turnover_cap": 0.10,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold6_turn08_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票68%, 持有6周, 换手8%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.68,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.08,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票65%, 持有6周, 换手8%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.65,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.08,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap65_hold6_turn08_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市30%, 单票65%, 持有6周, 换手8%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.65,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.08,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap65_hold6_turn08_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票65%, 持有6周, 换手8%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.65,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.08,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有7周, 换手6%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有7周, 换手6%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold7_turn06_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票60%, 持有7周, 换手6%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn05_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票55%, 持有8周, 换手5%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.05,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold7_turn05_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票58%, 持有7周, 换手5%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.05,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn06_exit88_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票58%, 持有6周, 换手6%, 出场88%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.88,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票58%, 持有6周, 换手6%, 出场88%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.88,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.06,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票58%, 持有6周, 换手4%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn04_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票58%, 持有6周, 换手4%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 6,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn04_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票55%, 持有8周, 换手4%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn04_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有8周, 换手4%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn04_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市30%, 单票60%, 持有8周, 换手4%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold8_turn04_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票60%, 持有8周, 换手4%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有9周, 换手3%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 9,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold9_turn03_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市30%, 单票60%, 持有9周, 换手3%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_caution_exposure": 0.74,
        "satellite_caution_exposure": 0.54,
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 9,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn03_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票60%, 持有9周, 换手3%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.72,
        "satellite_caution_exposure": 0.52,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 9,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold10_turn03_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有10周, 换手3%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 10,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold10_turn03_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票55%, 持有10周, 换手3%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 10,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold10_turn03_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票55%, 持有10周, 换手3%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.70,
        "satellite_caution_exposure": 0.50,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.55,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 10,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold10_turn02_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票58%, 持有10周, 换手2%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 10,
        "weekly_turnover_cap": 0.02,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap58_hold10_turn02_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 风险25, 单票58%, 持有10周, 换手2%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.58,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.58,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 10,
        "weekly_turnover_cap": 0.02,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn02_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票60%, 持有9周, 换手2%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.68,
        "satellite_caution_exposure": 0.48,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.60,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 9,
        "weekly_turnover_cap": 0.02,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold9_turn02_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 现金防守, 单票62%, 持有9周, 换手2%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.62,
        "satellite_caution_exposure": 0.45,
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.62,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 9,
        "weekly_turnover_cap": 0.02,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap62_hold9_turn02_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 风险25%, 单票62%, 持有9周, 换手2%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.58,
        "satellite_caution_exposure": 0.42,
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.62,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 9,
        "weekly_turnover_cap": 0.02,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap64_hold8_turn03_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票64%, 持有8周, 换手3%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.64,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap64_hold8_turn03_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 现金防守, 单票64%, 持有8周, 换手3%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.64,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 风险25%, 单票64%, 持有8周, 换手3%, 出场92%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.60,
        "satellite_caution_exposure": 0.44,
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "promoted_core_sell_exit_percentile": 0.92,
        "weight_cap": 0.64,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 8,
        "weekly_turnover_cap": 0.03,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 成本防守, 单票66%, 持有7周, 换手4%, 出场90%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.32,
        "satellite_risk_off_exposure": 0.32,
        "promoted_core_sell_exit_percentile": 0.90,
        "weight_cap": 0.66,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 现金防守, 单票66%, 持有7周, 换手4%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.66,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit96_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 现金防守, 单票66%, 持有7周, 换手4%, 出场96%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "promoted_core_sell_exit_percentile": 0.96,
        "weight_cap": 0.66,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_03_97_prom2_weekly_alpha_pullback_risk20_cap66_hold7_turn04_exit94_weekly",
        "variant_name": "进攻3/97 晋升2只(周频Alpha回踩, 熊市20%, 单票66%, 持有7周, 换手4%, 出场94%, 单周)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "weekly_alpha_pullback",
        "promotion_signal_mode": "weekly_alpha_pullback",
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "and",
        "core_caution_exposure": 0.66,
        "satellite_caution_exposure": 0.46,
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "promoted_core_sell_exit_percentile": 0.94,
        "weight_cap": 0.66,
        "rebalance_frequency": "weekly",
        "weekly_min_hold_periods": 7,
        "weekly_turnover_cap": 0.04,
    },
    {
        "variant_id": "aggr_08_92_prom6_cash_off_dd_guard50",
        "variant_name": "进攻8/92 晋升6只(熊市空仓, 日级回撤防守50%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "portfolio_drawdown_guard_enabled": True,
        "portfolio_drawdown_guard_trigger": 0.08,
        "portfolio_drawdown_guard_release": 0.03,
        "portfolio_drawdown_guard_exposure": 0.50,
        "portfolio_drawdown_guard_max_days": 20,
    },
    {
        "variant_id": "aggr_08_92_prom6_core_6_1_dd_guard35",
        "variant_name": "进攻8/92 晋升6只(核心6-1动量, 日级回撤防守35%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": "6_1",
        "portfolio_drawdown_guard_enabled": True,
        "portfolio_drawdown_guard_trigger": 0.04,
        "portfolio_drawdown_guard_release": 0.015,
        "portfolio_drawdown_guard_exposure": 0.35,
        "portfolio_drawdown_guard_max_days": 12,
    },
    {
        "variant_id": "aggr_05_95_prom7_core_6_1_full_risk_dd_guard35",
        "variant_name": "进攻5/95 晋升7只(核心6-1动量, 关闭熊市降仓, 日级回撤防守35%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 7,
        "core_signal_mode": "6_1",
        "core_risk_off_exposure": 1.0,
        "satellite_risk_off_exposure": 1.0,
        "portfolio_drawdown_guard_enabled": True,
        "portfolio_drawdown_guard_trigger": 0.04,
        "portfolio_drawdown_guard_release": 0.015,
        "portfolio_drawdown_guard_exposure": 0.35,
        "portfolio_drawdown_guard_max_days": 12,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard50",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市空仓 and, 单票60%, 日级回撤防守50%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.60,
        "portfolio_drawdown_guard_enabled": True,
        "portfolio_drawdown_guard_trigger": 0.045,
        "portfolio_drawdown_guard_release": 0.02,
        "portfolio_drawdown_guard_exposure": 0.50,
        "portfolio_drawdown_guard_max_days": 10,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard30_fast",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市空仓 and, 单票60%, 日级回撤防守30%快恢复)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.60,
        "portfolio_drawdown_guard_enabled": True,
        "portfolio_drawdown_guard_trigger": 0.10,
        "portfolio_drawdown_guard_release": 0.06,
        "portfolio_drawdown_guard_exposure": 0.30,
        "portfolio_drawdown_guard_max_days": 5,
    },
    {
        "variant_id": "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard0_fast",
        "variant_name": "进攻5/95 晋升3只(核心6-1动量, 熊市空仓 and, 单票60%, 日级回撤空仓快恢复)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "weight_cap": 0.60,
        "portfolio_drawdown_guard_enabled": True,
        "portfolio_drawdown_guard_trigger": 0.12,
        "portfolio_drawdown_guard_release": 0.08,
        "portfolio_drawdown_guard_exposure": 0.0,
        "portfolio_drawdown_guard_max_days": 5,
    },
    {
        "variant_id": "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50",
        "variant_name": "进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)",
        "winner_core_stable_share": 0.01,
        "winner_core_promoted_share": 0.99,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": "6_1",
        "promotion_signal_mode": "liquidity_momentum",
        "standard_promotion_percentile": 0.15,
        "standard_promotion_min_momentum_6_1_rank": 0.70,
        "fast_promotion_percentile": 0.10,
        "fast_promotion_min_momentum_6_1_rank": 0.82,
        "fast_promotion_min_recent_1m_return": 0.005,
        "fast_promotion_min_amount_surge_ratio": 1.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.95,
        "portfolio_drawdown_guard_enabled": True,
        "portfolio_drawdown_guard_trigger": 0.10,
        "portfolio_drawdown_guard_release": 0.04,
        "portfolio_drawdown_guard_exposure": 0.50,
        "portfolio_drawdown_guard_max_days": 8,
    },
    {
        "variant_id": "aggr_02_98_prom2_emergent_theme_cash_off_and_cap95",
        "variant_name": "进攻2/98 晋升2只(强主题涌现, 熊市空仓 and, 单票95%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.12,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "and",
        "core_risk_off_exposure": 0.0,
        "satellite_risk_off_exposure": 0.0,
        "core_quality_quantile": 0.35,
        "promoted_core_quality_quantile": 0.25,
        "explore_quality_quantile": 0.30,
        "seed_quality_quantile": 0.20,
        "promoted_core_sell_exit_percentile": 0.70,
        "weight_cap": 0.95,
    },
    {
        "variant_id": "aggr_02_98_prom2_emergent_theme_risk40_cap90",
        "variant_name": "进攻2/98 晋升2只(强主题涌现, 熊市40%, 单票90%)",
        "winner_core_stable_share": 0.02,
        "winner_core_promoted_share": 0.98,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.12,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.35,
        "promoted_core_quality_quantile": 0.25,
        "explore_quality_quantile": 0.30,
        "seed_quality_quantile": 0.20,
        "promoted_core_sell_exit_percentile": 0.70,
        "weight_cap": 0.90,
    },
    {
        "variant_id": "aggr_05_95_prom3_emergent_theme_risk40_cap70",
        "variant_name": "进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.35,
        "promoted_core_quality_quantile": 0.25,
        "explore_quality_quantile": 0.30,
        "seed_quality_quantile": 0.20,
        "promoted_core_sell_exit_percentile": 0.75,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70",
        "variant_name": "进攻5/95 晋升3只(强主题涌现, 质量门槛, 熊市40%, 单票70%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.70,
    },
    {
        "variant_id": "aggr_08_92_prom6_emergent_theme_risk50_cap50",
        "variant_name": "进攻8/92 晋升6只(强主题涌现, 熊市50%, 单票50%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.12,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.50,
        "satellite_risk_off_exposure": 0.50,
        "core_quality_quantile": 0.40,
        "promoted_core_quality_quantile": 0.30,
        "explore_quality_quantile": 0.35,
        "seed_quality_quantile": 0.25,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.50,
    },
    {
        "variant_id": "aggr_08_92_prom6_emergent_theme_risk30_cap50",
        "variant_name": "进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.12,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.40,
        "promoted_core_quality_quantile": 0.30,
        "explore_quality_quantile": 0.35,
        "seed_quality_quantile": 0.25,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.50,
    },
    {
        "variant_id": "aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50",
        "variant_name": "进攻8/92 晋升6只(强主题涌现, 质量门槛, 熊市30%, 单票50%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.12,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.48,
        "promoted_core_quality_quantile": 0.34,
        "explore_quality_quantile": 0.42,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.50,
    },
    {
        "variant_id": "aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45",
        "variant_name": "进攻8/92 晋升6只(强主题涌现, 质量门槛, 熊市30%, 单票45%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.12,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.48,
        "promoted_core_quality_quantile": 0.34,
        "explore_quality_quantile": 0.42,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap45",
        "variant_name": "进攻8/92 晋升6只(强主题涌现, 质量门槛, 熊市35%, 单票45%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.12,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.48,
        "promoted_core_quality_quantile": 0.34,
        "explore_quality_quantile": 0.42,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40",
        "variant_name": "进攻8/92 晋升6只(强主题涌现, 质量门槛, 熊市35%, 单票40%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.12,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.48,
        "promoted_core_quality_quantile": 0.34,
        "explore_quality_quantile": 0.42,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35",
        "variant_name": "进攻8/92 晋升6只(强主题涌现, 质量门槛, 熊市35%, 单票35%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 6,
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.12,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.48,
        "promoted_core_quality_quantile": 0.34,
        "explore_quality_quantile": 0.42,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.35,
    },
    {
        "variant_id": "aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65",
        "variant_name": "进攻5/95 晋升3只(强主题涌现, 质量门槛, 熊市35%, 单票65%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.65,
    },
    {
        "variant_id": "aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65",
        "variant_name": "进攻5/95 晋升3只(强主题涌现, 质量门槛, 熊市30%, 单票65%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.65,
    },
    {
        "variant_id": "aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60",
        "variant_name": "进攻5/95 晋升3只(强主题涌现, 质量门槛, 熊市30%, 单票60%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 3,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.60,
    },
    {
        "variant_id": "aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60",
        "variant_name": "进攻3/97 晋升2只(强主题涌现, 质量门槛, 熊市30%, 单票60%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.60,
    },
    {
        "variant_id": "aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50",
        "variant_name": "进攻4/96 晋升2只(强主题涌现, 质量门槛, 熊市30%, 单票50%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.50,
    },
    {
        "variant_id": "aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45",
        "variant_name": "进攻4/96 晋升2只(强主题涌现, 质量门槛, 熊市35%, 单票45%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40",
        "variant_name": "进攻4/96 晋升2只(强主题涌现, 质量门槛, 熊市35%, 单票40%)",
        "winner_core_stable_share": 0.04,
        "winner_core_promoted_share": 0.96,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50",
        "variant_name": "进攻5/95 晋升4只(强主题涌现, 质量门槛, 熊市35%, 单票50%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.50,
    },
    {
        "variant_id": "aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82",
        "variant_name": "进攻5/95 晋升4只(强主题涌现, 质量门槛, 熊市35%, 单票45%, 出场82%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.82,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82",
        "variant_name": "进攻5/95 晋升4只(强主题涌现, 质量门槛, 熊市35%, 单票40%, 出场82%)",
        "winner_core_stable_share": 0.05,
        "winner_core_promoted_share": 0.95,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 4,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.82,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82",
        "variant_name": "进攻6/94 晋升5只(强主题涌现, 质量门槛, 熊市35%, 单票45%, 出场82%)",
        "winner_core_stable_share": 0.06,
        "winner_core_promoted_share": 0.94,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 5,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.16,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.82,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_07_93_prom6_emergent_theme_quality_gate_risk35_cap45_exit82",
        "variant_name": "进攻7/93 晋升6只(强主题涌现, 质量门槛, 熊市35%, 单票45%, 出场82%)",
        "winner_core_stable_share": 0.07,
        "winner_core_promoted_share": 0.93,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.17,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.82,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82",
        "variant_name": "进攻7/93 晋升6只(强主题涌现, 质量门槛, 熊市40%, 单票45%, 出场82%)",
        "winner_core_stable_share": 0.07,
        "winner_core_promoted_share": 0.93,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.17,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.82,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80",
        "variant_name": "进攻7/93 晋升6只(强主题涌现, 质量门槛, 熊市45%, 单票40%, 出场80%)",
        "winner_core_stable_share": 0.07,
        "winner_core_promoted_share": 0.93,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.17,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.45,
        "satellite_risk_off_exposure": 0.45,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80",
        "variant_name": "进攻7/93 晋升6只(强主题涌现, 质量门槛, 熊市45%, 单票35%, 出场80%)",
        "winner_core_stable_share": 0.07,
        "winner_core_promoted_share": 0.93,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 6,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.17,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.45,
        "satellite_risk_off_exposure": 0.45,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.35,
    },
    {
        "variant_id": "aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80",
        "variant_name": "进攻8/92 晋升7只(强主题涌现, 质量门槛, 熊市45%, 单票35%, 出场80%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.45,
        "satellite_risk_off_exposure": 0.45,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.80,
        "weight_cap": 0.35,
    },
    {
        "variant_id": "aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78",
        "variant_name": "进攻8/92 晋升7只(强主题涌现, 质量门槛, 熊市40%, 单票35%, 出场78%)",
        "winner_core_stable_share": 0.08,
        "winner_core_promoted_share": 0.92,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 7,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.35,
    },
    {
        "variant_id": "aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78",
        "variant_name": "进攻9/91 晋升8只(强主题涌现, 质量门槛, 熊市40%, 单票35%, 出场78%)",
        "winner_core_stable_share": 0.09,
        "winner_core_promoted_share": 0.91,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.19,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.35,
    },
    {
        "variant_id": "aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76",
        "variant_name": "进攻9/91 晋升8只(强主题涌现, 质量门槛, 熊市35%, 单票35%, 出场76%)",
        "winner_core_stable_share": 0.09,
        "winner_core_promoted_share": 0.91,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.19,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.76,
        "weight_cap": 0.35,
    },
    {
        "variant_id": "aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76",
        "variant_name": "进攻9/91 晋升8只(强主题涌现, 质量门槛, 熊市35%, 单票30%, 出场76%)",
        "winner_core_stable_share": 0.09,
        "winner_core_promoted_share": 0.91,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 8,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.19,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.76,
        "weight_cap": 0.30,
    },
    {
        "variant_id": "aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76",
        "variant_name": "进攻10/90 晋升9只(强主题涌现, 质量门槛, 熊市35%, 单票30%, 出场76%)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 9,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.76,
        "weight_cap": 0.30,
    },
    {
        "variant_id": "aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78",
        "variant_name": "进攻10/90 晋升9只(强主题涌现, 质量门槛, 熊市40%, 单票30%, 出场78%)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 9,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.30,
    },
    {
        "variant_id": "aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78",
        "variant_name": "进攻10/90 晋升9只(强主题涌现, 严格信号18%, 熊市40%, 单票30%, 出场78%)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 9,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.55,
        "promoted_core_quality_quantile": 0.40,
        "explore_quality_quantile": 0.50,
        "seed_quality_quantile": 0.35,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.30,
    },
    {
        "variant_id": "aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78",
        "variant_name": "进攻11/89 晋升10只(强主题涌现, 严格信号18%, 熊市40%, 单票30%, 出场78%)",
        "winner_core_stable_share": 0.11,
        "winner_core_promoted_share": 0.89,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 10,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.18,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.55,
        "promoted_core_quality_quantile": 0.40,
        "explore_quality_quantile": 0.50,
        "seed_quality_quantile": 0.35,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.30,
    },
    {
        "variant_id": "aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78",
        "variant_name": "进攻10/90 晋升9只(强主题涌现, 严格信号20%, 熊市40%, 单票28%, 出场78%)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 9,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.58,
        "promoted_core_quality_quantile": 0.42,
        "explore_quality_quantile": 0.52,
        "seed_quality_quantile": 0.36,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.28,
    },
    {
        "variant_id": "aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78",
        "variant_name": "进攻10/90 晋升9只(强主题涌现, 严格信号20%, 熊市40%, 单票25%, 出场78%)",
        "winner_core_stable_share": 0.10,
        "winner_core_promoted_share": 0.90,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 9,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.58,
        "promoted_core_quality_quantile": 0.42,
        "explore_quality_quantile": 0.52,
        "seed_quality_quantile": 0.36,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.25,
    },
    {
        "variant_id": "aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78",
        "variant_name": "进攻11/89 晋升10只(强主题涌现, 严格信号20%, 熊市40%, 单票25%, 出场78%)",
        "winner_core_stable_share": 0.11,
        "winner_core_promoted_share": 0.89,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 10,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.40,
        "satellite_risk_off_exposure": 0.40,
        "core_quality_quantile": 0.58,
        "promoted_core_quality_quantile": 0.42,
        "explore_quality_quantile": 0.52,
        "seed_quality_quantile": 0.36,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.25,
    },
    {
        "variant_id": "aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76",
        "variant_name": "进攻11/89 晋升10只(强主题涌现, 严格信号20%, 熊市35%, 单票25%, 出场76%)",
        "winner_core_stable_share": 0.11,
        "winner_core_promoted_share": 0.89,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 10,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.58,
        "promoted_core_quality_quantile": 0.42,
        "explore_quality_quantile": 0.52,
        "seed_quality_quantile": 0.36,
        "promoted_core_sell_exit_percentile": 0.76,
        "weight_cap": 0.25,
    },
    {
        "variant_id": "aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74",
        "variant_name": "进攻11/89 晋升10只(强主题涌现, 严格信号20%, 熊市35%, 单票20%, 出场74%)",
        "winner_core_stable_share": 0.11,
        "winner_core_promoted_share": 0.89,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 10,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.20,
        "fast_promotion_percentile": 0.08,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.58,
        "promoted_core_quality_quantile": 0.42,
        "explore_quality_quantile": 0.52,
        "seed_quality_quantile": 0.36,
        "promoted_core_sell_exit_percentile": 0.74,
        "weight_cap": 0.20,
    },
    {
        "variant_id": "aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74",
        "variant_name": "进攻11/89 晋升10只(强主题涌现, 严格信号22%, 熊市35%, 单票20%, 出场74%)",
        "winner_core_stable_share": 0.11,
        "winner_core_promoted_share": 0.89,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 10,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.22,
        "fast_promotion_percentile": 0.07,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.60,
        "promoted_core_quality_quantile": 0.44,
        "explore_quality_quantile": 0.54,
        "seed_quality_quantile": 0.38,
        "promoted_core_sell_exit_percentile": 0.74,
        "weight_cap": 0.20,
    },
    {
        "variant_id": "aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk30_cap20_exit72",
        "variant_name": "进攻11/89 晋升10只(强主题涌现, 严格信号22%, 熊市30%, 单票20%, 出场72%)",
        "winner_core_stable_share": 0.11,
        "winner_core_promoted_share": 0.89,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 10,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.22,
        "fast_promotion_percentile": 0.07,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.60,
        "promoted_core_quality_quantile": 0.44,
        "explore_quality_quantile": 0.54,
        "seed_quality_quantile": 0.38,
        "promoted_core_sell_exit_percentile": 0.72,
        "weight_cap": 0.20,
    },
    {
        "variant_id": "aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72",
        "variant_name": "进攻12/88 晋升11只(强主题涌现, 严格信号22%, 熊市30%, 单票18%, 出场72%)",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 11,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.22,
        "fast_promotion_percentile": 0.07,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.60,
        "promoted_core_quality_quantile": 0.44,
        "explore_quality_quantile": 0.54,
        "seed_quality_quantile": 0.38,
        "promoted_core_sell_exit_percentile": 0.72,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72",
        "variant_name": "进攻12/88 晋升11只(强主题涌现, 严格信号24%, 熊市30%, 单票18%, 出场72%)",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 11,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.24,
        "fast_promotion_percentile": 0.07,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.62,
        "promoted_core_quality_quantile": 0.46,
        "explore_quality_quantile": 0.56,
        "seed_quality_quantile": 0.40,
        "promoted_core_sell_exit_percentile": 0.72,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70",
        "variant_name": "进攻12/88 晋升11只(强主题涌现, 严格信号24%, 熊市25%, 单票18%, 出场70%)",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 11,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.24,
        "fast_promotion_percentile": 0.07,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "core_quality_quantile": 0.62,
        "promoted_core_quality_quantile": 0.46,
        "explore_quality_quantile": 0.56,
        "seed_quality_quantile": 0.40,
        "promoted_core_sell_exit_percentile": 0.70,
        "weight_cap": 0.18,
    },
    {
        "variant_id": "aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap16_exit70",
        "variant_name": "进攻12/88 晋升11只(强主题涌现, 严格信号24%, 熊市25%, 单票16%, 出场70%)",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 11,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.24,
        "fast_promotion_percentile": 0.07,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "core_quality_quantile": 0.62,
        "promoted_core_quality_quantile": 0.46,
        "explore_quality_quantile": 0.56,
        "seed_quality_quantile": 0.40,
        "promoted_core_sell_exit_percentile": 0.70,
        "weight_cap": 0.16,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 严格信号24%, 熊市25%, 单票16%, 出场70%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.24,
        "fast_promotion_percentile": 0.07,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "core_quality_quantile": 0.62,
        "promoted_core_quality_quantile": 0.46,
        "explore_quality_quantile": 0.56,
        "seed_quality_quantile": 0.40,
        "promoted_core_sell_exit_percentile": 0.70,
        "weight_cap": 0.16,
    },
    {
        "variant_id": "aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55",
        "variant_name": "进攻3/97 晋升2只(强主题涌现, 质量门槛, 熊市35%, 单票55%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.55,
    },
    {
        "variant_id": "aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45",
        "variant_name": "进攻3/97 晋升2只(强主题涌现, 质量门槛, 熊市30%, 单票45%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45",
        "variant_name": "进攻3/97 晋升2只(强主题涌现, 质量门槛, 熊市35%, 单票45%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.35,
        "satellite_risk_off_exposure": 0.35,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.45,
    },
    {
        "variant_id": "aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40",
        "variant_name": "进攻3/97 晋升2只(强主题涌现, 质量门槛, 熊市30%, 单票40%)",
        "winner_core_stable_share": 0.03,
        "winner_core_promoted_share": 0.97,
        "stable_core_max_holdings": 1,
        "promoted_core_max_holdings": 2,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.15,
        "fast_promotion_percentile": 0.10,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.30,
        "satellite_risk_off_exposure": 0.30,
        "core_quality_quantile": 0.50,
        "promoted_core_quality_quantile": 0.35,
        "explore_quality_quantile": 0.45,
        "seed_quality_quantile": 0.30,
        "promoted_core_sell_exit_percentile": 0.78,
        "weight_cap": 0.40,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 信号24%, 龙头68%, 熊市25%, 单票16%, 出场70%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.24,
        "standard_promotion_min_industry_leader": 0.68,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_industry_leader": 0.82,
        "fast_promotion_min_momentum_3_1_rank": 0.65,
        "fast_promotion_min_amount_surge_ratio": 1.25,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "core_quality_quantile": 0.62,
        "promoted_core_quality_quantile": 0.46,
        "explore_quality_quantile": 0.56,
        "seed_quality_quantile": 0.40,
        "promoted_core_sell_exit_percentile": 0.70,
        "weight_cap": 0.16,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 信号24%, 龙头68%, 熊市20%, 单票16%, 出场68%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.24,
        "standard_promotion_min_industry_leader": 0.68,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_industry_leader": 0.82,
        "fast_promotion_min_momentum_3_1_rank": 0.65,
        "fast_promotion_min_amount_surge_ratio": 1.25,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "core_quality_quantile": 0.62,
        "promoted_core_quality_quantile": 0.46,
        "explore_quality_quantile": 0.56,
        "seed_quality_quantile": 0.40,
        "promoted_core_sell_exit_percentile": 0.68,
        "weight_cap": 0.16,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 信号24%, 龙头68%, 熊市20%, 单票12%, 出场68%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.24,
        "standard_promotion_min_industry_leader": 0.68,
        "standard_promotion_min_momentum_3_1_rank": 0.55,
        "fast_promotion_percentile": 0.07,
        "fast_promotion_min_industry_leader": 0.82,
        "fast_promotion_min_momentum_3_1_rank": 0.65,
        "fast_promotion_min_amount_surge_ratio": 1.25,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "core_quality_quantile": 0.62,
        "promoted_core_quality_quantile": 0.46,
        "explore_quality_quantile": 0.56,
        "seed_quality_quantile": 0.40,
        "promoted_core_sell_exit_percentile": 0.68,
        "weight_cap": 0.12,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk25_cap16_exit70",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 信号26%, 龙头72%, 熊市25%, 单票16%, 出场70%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.26,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.58,
        "fast_promotion_percentile": 0.06,
        "fast_promotion_min_industry_leader": 0.84,
        "fast_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_min_amount_surge_ratio": 1.28,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.25,
        "satellite_risk_off_exposure": 0.25,
        "core_quality_quantile": 0.64,
        "promoted_core_quality_quantile": 0.48,
        "explore_quality_quantile": 0.58,
        "seed_quality_quantile": 0.42,
        "promoted_core_sell_exit_percentile": 0.70,
        "weight_cap": 0.16,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap16_exit68",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 信号26%, 龙头72%, 熊市20%, 单票16%, 出场68%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.26,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.58,
        "fast_promotion_percentile": 0.06,
        "fast_promotion_min_industry_leader": 0.84,
        "fast_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_min_amount_surge_ratio": 1.28,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "core_quality_quantile": 0.64,
        "promoted_core_quality_quantile": 0.48,
        "explore_quality_quantile": 0.58,
        "seed_quality_quantile": 0.42,
        "promoted_core_sell_exit_percentile": 0.68,
        "weight_cap": 0.16,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 信号26%, 龙头72%, 熊市20%, 单票12%, 出场68%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.26,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.58,
        "fast_promotion_percentile": 0.06,
        "fast_promotion_min_industry_leader": 0.84,
        "fast_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_min_amount_surge_ratio": 1.28,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "core_quality_quantile": 0.64,
        "promoted_core_quality_quantile": 0.48,
        "explore_quality_quantile": 0.58,
        "seed_quality_quantile": 0.42,
        "promoted_core_sell_exit_percentile": 0.68,
        "weight_cap": 0.12,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号26%, 龙头72%, 熊市20%, 单票12%, 出场68%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 14,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.26,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_percentile": 0.06,
        "fast_promotion_min_industry_leader": 0.86,
        "fast_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_min_amount_surge_ratio": 1.32,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.20,
        "satellite_risk_off_exposure": 0.20,
        "core_quality_quantile": 0.66,
        "promoted_core_quality_quantile": 0.50,
        "explore_quality_quantile": 0.60,
        "seed_quality_quantile": 0.44,
        "promoted_core_sell_exit_percentile": 0.68,
        "weight_cap": 0.10,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap12_exit66",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号26%, 龙头72%, 熊市15%, 单票12%, 出场66%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 14,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.26,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_percentile": 0.06,
        "fast_promotion_min_industry_leader": 0.86,
        "fast_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_min_amount_surge_ratio": 1.32,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.15,
        "satellite_risk_off_exposure": 0.15,
        "core_quality_quantile": 0.66,
        "promoted_core_quality_quantile": 0.50,
        "explore_quality_quantile": 0.60,
        "seed_quality_quantile": 0.44,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.10,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号26%, 龙头72%, 熊市12%, 单票10%, 出场64%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.26,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_percentile": 0.06,
        "fast_promotion_min_industry_leader": 0.86,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_amount_surge_ratio": 1.34,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.12,
        "satellite_risk_off_exposure": 0.12,
        "core_quality_quantile": 0.68,
        "promoted_core_quality_quantile": 0.52,
        "explore_quality_quantile": 0.62,
        "seed_quality_quantile": 0.46,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.10,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号27%, 龙头72%, 熊市15%, 单票12%, 出场64%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.27,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_percentile": 0.055,
        "fast_promotion_min_industry_leader": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_amount_surge_ratio": 1.34,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.15,
        "satellite_risk_off_exposure": 0.15,
        "core_quality_quantile": 0.68,
        "promoted_core_quality_quantile": 0.52,
        "explore_quality_quantile": 0.62,
        "seed_quality_quantile": 0.46,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.12,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 信号26%, 龙头72%, 熊市15%, 单票12%, 出场66%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.26,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.58,
        "fast_promotion_percentile": 0.06,
        "fast_promotion_min_industry_leader": 0.84,
        "fast_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_min_amount_surge_ratio": 1.28,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.15,
        "satellite_risk_off_exposure": 0.15,
        "core_quality_quantile": 0.64,
        "promoted_core_quality_quantile": 0.48,
        "explore_quality_quantile": 0.58,
        "seed_quality_quantile": 0.42,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.12,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 信号28%, 龙头72%, 熊市15%, 单票12%, 出场64%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 12,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.28,
        "standard_promotion_min_industry_leader": 0.72,
        "standard_promotion_min_momentum_3_1_rank": 0.60,
        "fast_promotion_percentile": 0.06,
        "fast_promotion_min_industry_leader": 0.86,
        "fast_promotion_min_momentum_3_1_rank": 0.70,
        "fast_promotion_min_amount_surge_ratio": 1.32,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.15,
        "satellite_risk_off_exposure": 0.15,
        "core_quality_quantile": 0.66,
        "promoted_core_quality_quantile": 0.50,
        "explore_quality_quantile": 0.60,
        "seed_quality_quantile": 0.44,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.12,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号28%, 龙头74%, 熊市15%, 单票12%, 出场64%)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.28,
        "standard_promotion_min_industry_leader": 0.74,
        "standard_promotion_min_momentum_3_1_rank": 0.62,
        "fast_promotion_percentile": 0.055,
        "fast_promotion_min_industry_leader": 0.88,
        "fast_promotion_min_momentum_3_1_rank": 0.72,
        "fast_promotion_min_amount_surge_ratio": 1.34,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.15,
        "satellite_risk_off_exposure": 0.15,
        "core_quality_quantile": 0.68,
        "promoted_core_quality_quantile": 0.52,
        "explore_quality_quantile": 0.62,
        "seed_quality_quantile": 0.46,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.12,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号29%, 龙头76%, 熊市15%, 单票12%, 出场64%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.29,
        "standard_promotion_min_industry_leader": 0.76,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.05,
        "fast_promotion_min_industry_leader": 0.90,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_amount_surge_ratio": 1.36,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.15,
        "satellite_risk_off_exposure": 0.15,
        "core_quality_quantile": 0.70,
        "promoted_core_quality_quantile": 0.54,
        "explore_quality_quantile": 0.64,
        "seed_quality_quantile": 0.48,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.12,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号29%, 龙头76%, 熊市18%, 单票14%, 出场66%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.29,
        "standard_promotion_min_industry_leader": 0.76,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.05,
        "fast_promotion_min_industry_leader": 0.90,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_amount_surge_ratio": 1.36,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.18,
        "satellite_risk_off_exposure": 0.18,
        "core_quality_quantile": 0.70,
        "promoted_core_quality_quantile": 0.54,
        "explore_quality_quantile": 0.64,
        "seed_quality_quantile": 0.48,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.14,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头78%, 熊市18%, 单票14%, 出场66%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.30,
        "standard_promotion_min_industry_leader": 0.78,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.05,
        "fast_promotion_min_industry_leader": 0.91,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_amount_surge_ratio": 1.36,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.18,
        "satellite_risk_off_exposure": 0.18,
        "core_quality_quantile": 0.70,
        "promoted_core_quality_quantile": 0.54,
        "explore_quality_quantile": 0.64,
        "seed_quality_quantile": 0.48,
        "promoted_core_sell_exit_percentile": 0.66,
        "weight_cap": 0.14,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市16%, 单票10%, 出场64%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.28,
        "standard_promotion_min_industry_leader": 0.76,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.05,
        "fast_promotion_min_industry_leader": 0.90,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_amount_surge_ratio": 1.36,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.16,
        "satellite_risk_off_exposure": 0.16,
        "core_quality_quantile": 0.70,
        "promoted_core_quality_quantile": 0.54,
        "explore_quality_quantile": 0.64,
        "seed_quality_quantile": 0.48,
        "promoted_core_sell_exit_percentile": 0.64,
        "weight_cap": 0.10,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市14%, 单票10%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.28,
        "standard_promotion_min_industry_leader": 0.76,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.05,
        "fast_promotion_min_industry_leader": 0.90,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_amount_surge_ratio": 1.36,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.70,
        "promoted_core_quality_quantile": 0.54,
        "explore_quality_quantile": 0.64,
        "seed_quality_quantile": 0.48,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.10,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap10_exit60_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市12%, 单票10%, 出场60%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 15,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.28,
        "standard_promotion_min_industry_leader": 0.76,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.05,
        "fast_promotion_min_industry_leader": 0.90,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_amount_surge_ratio": 1.36,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.12,
        "satellite_risk_off_exposure": 0.12,
        "core_quality_quantile": 0.70,
        "promoted_core_quality_quantile": 0.54,
        "explore_quality_quantile": 0.64,
        "seed_quality_quantile": 0.48,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.10,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap08_exit60_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市12%, 单票8%, 出场60%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 18,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.28,
        "standard_promotion_min_industry_leader": 0.76,
        "standard_promotion_min_momentum_3_1_rank": 0.64,
        "fast_promotion_percentile": 0.05,
        "fast_promotion_min_industry_leader": 0.90,
        "fast_promotion_min_momentum_3_1_rank": 0.74,
        "fast_promotion_min_amount_surge_ratio": 1.36,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.12,
        "satellite_risk_off_exposure": 0.12,
        "core_quality_quantile": 0.70,
        "promoted_core_quality_quantile": 0.54,
        "explore_quality_quantile": 0.64,
        "seed_quality_quantile": 0.48,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市12%, 单票8%, 出场58%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 18,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.30,
        "standard_promotion_min_industry_leader": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_percentile": 0.045,
        "fast_promotion_min_industry_leader": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.76,
        "fast_promotion_min_amount_surge_ratio": 1.38,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.12,
        "satellite_risk_off_exposure": 0.12,
        "core_quality_quantile": 0.72,
        "promoted_core_quality_quantile": 0.56,
        "explore_quality_quantile": 0.66,
        "seed_quality_quantile": 0.50,
        "promoted_core_sell_exit_percentile": 0.58,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
        "variant_name": "进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市14%, 单票8%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 18,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.30,
        "standard_promotion_min_industry_leader": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_percentile": 0.045,
        "fast_promotion_min_industry_leader": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.76,
        "fast_promotion_min_amount_surge_ratio": 1.38,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.72,
        "promoted_core_quality_quantile": 0.56,
        "explore_quality_quantile": 0.66,
        "seed_quality_quantile": 0.50,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom14_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
        "variant_name": "进攻13/87 晋升14只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市14%, 单票8%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 20,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.30,
        "standard_promotion_min_industry_leader": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_percentile": 0.045,
        "fast_promotion_min_industry_leader": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.76,
        "fast_promotion_min_amount_surge_ratio": 1.38,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.72,
        "promoted_core_quality_quantile": 0.56,
        "explore_quality_quantile": 0.66,
        "seed_quality_quantile": 0.50,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom16_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
        "variant_name": "进攻13/87 晋升16只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市14%, 单票8%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 22,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.30,
        "standard_promotion_min_industry_leader": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_percentile": 0.045,
        "fast_promotion_min_industry_leader": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.76,
        "fast_promotion_min_amount_surge_ratio": 1.38,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.72,
        "promoted_core_quality_quantile": 0.56,
        "explore_quality_quantile": 0.66,
        "seed_quality_quantile": 0.50,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk12_cap08_exit60_lowturn",
        "variant_name": "进攻13/87 晋升16只(强主题涌现, 覆盖惩罚, 信号32%, 龙头82%, 熊市12%, 单票8%, 出场60%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 22,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.32,
        "standard_promotion_min_industry_leader": 0.82,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.04,
        "fast_promotion_min_industry_leader": 0.94,
        "fast_promotion_min_momentum_3_1_rank": 0.78,
        "fast_promotion_min_amount_surge_ratio": 1.40,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.12,
        "satellite_risk_off_exposure": 0.12,
        "core_quality_quantile": 0.74,
        "promoted_core_quality_quantile": 0.58,
        "explore_quality_quantile": 0.68,
        "seed_quality_quantile": 0.52,
        "promoted_core_sell_exit_percentile": 0.60,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn",
        "variant_name": "进攻13/87 晋升16只(强主题涌现, 覆盖惩罚, 信号32%, 龙头82%, 熊市14%, 单票8%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 22,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.32,
        "standard_promotion_min_industry_leader": 0.82,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.04,
        "fast_promotion_min_industry_leader": 0.94,
        "fast_promotion_min_momentum_3_1_rank": 0.78,
        "fast_promotion_min_amount_surge_ratio": 1.40,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.74,
        "promoted_core_quality_quantile": 0.58,
        "explore_quality_quantile": 0.68,
        "seed_quality_quantile": 0.52,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom18_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn",
        "variant_name": "进攻13/87 晋升18只(强主题涌现, 覆盖惩罚, 信号32%, 龙头82%, 熊市14%, 单票8%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 24,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.32,
        "standard_promotion_min_industry_leader": 0.82,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.04,
        "fast_promotion_min_industry_leader": 0.94,
        "fast_promotion_min_momentum_3_1_rank": 0.78,
        "fast_promotion_min_amount_surge_ratio": 1.40,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.74,
        "promoted_core_quality_quantile": 0.58,
        "explore_quality_quantile": 0.68,
        "seed_quality_quantile": 0.52,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
        "variant_name": "进攻13/87 晋升18只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市14%, 单票8%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 24,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.30,
        "standard_promotion_min_industry_leader": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.04,
        "fast_promotion_min_industry_leader": 0.94,
        "fast_promotion_min_momentum_3_1_rank": 0.78,
        "fast_promotion_min_amount_surge_ratio": 1.40,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.74,
        "promoted_core_quality_quantile": 0.58,
        "explore_quality_quantile": 0.68,
        "seed_quality_quantile": 0.52,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
        "variant_name": "进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市14%, 单票8%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 26,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.30,
        "standard_promotion_min_industry_leader": 0.80,
        "standard_promotion_min_momentum_3_1_rank": 0.68,
        "fast_promotion_percentile": 0.04,
        "fast_promotion_min_industry_leader": 0.94,
        "fast_promotion_min_momentum_3_1_rank": 0.78,
        "fast_promotion_min_amount_surge_ratio": 1.40,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.74,
        "promoted_core_quality_quantile": 0.58,
        "explore_quality_quantile": 0.68,
        "seed_quality_quantile": 0.52,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.08,
    },
    {
        "variant_id": "aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn",
        "variant_name": "进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号28%, 龙头78%, 熊市14%, 单票8%, 出场62%, 低换手)",
        "winner_core_stable_share": 0.13,
        "winner_core_promoted_share": 0.87,
        "stable_core_max_holdings": 2,
        "promoted_core_max_holdings": 26,
        "promoted_core_stage_ramp": {1: 1.00},
        "core_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "promotion_signal_mode": EMERGENT_THEME_SIGNAL_MODE,
        "standard_promotion_percentile": 0.28,
        "standard_promotion_min_industry_leader": 0.78,
        "standard_promotion_min_momentum_3_1_rank": 0.66,
        "fast_promotion_percentile": 0.045,
        "fast_promotion_min_industry_leader": 0.92,
        "fast_promotion_min_momentum_3_1_rank": 0.76,
        "fast_promotion_min_amount_surge_ratio": 1.36,
        "market_risk_off_rule": "negative_mom",
        "risk_staging_mode": "three_stage",
        "core_risk_off_exposure": 0.14,
        "satellite_risk_off_exposure": 0.14,
        "core_quality_quantile": 0.72,
        "promoted_core_quality_quantile": 0.56,
        "explore_quality_quantile": 0.66,
        "seed_quality_quantile": 0.50,
        "promoted_core_sell_exit_percentile": 0.62,
        "weight_cap": 0.08,
    },
]

PATH1_FAST_PASS_DIRECTION_GROUPS = {
    "promotion_ramp": [
        "aggr_10_90_fast_ramp",
        "aggr_10_90_prom5",
        "aggr_10_90_prom6",
        "aggr_10_90_prom7",
        "aggr_10_90_prom7_ramp90",
    ],
    "satellite_defense": [
        "aggr_08_92_prom6_cash_off",
        "aggr_08_92_prom6_cash_off_and",
        "aggr_10_90_prom6_cash_off",
        "aggr_10_90_fast_ramp_cash_off",
        "aggr_10_90_fast_ramp_cash_off_and",
        "aggr_08_92_prom6_satellite_cost_guard",
        "aggr_08_92_prom6__sat_three_stage_buffered_cost_guard_cashguard",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_cashguard_light",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk30_reconfirm",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk15_reconfirm",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm",
        "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk12_reconfirm",
    ],
    "signal_variants": [
        "aggr_08_92_prom6_core_6_1",
        "aggr_10_90_prom6_core_6_1",
    ],
    "core_multifactor": [
        "aggr_08_92_prom6_core_multifactor_balanced",
        "aggr_08_92_prom6_core_multifactor_quality_tilt",
        "aggr_08_92_prom6_core_multifactor_momentum_quality",
        "aggr_10_90_prom6_core_multifactor_balanced",
        "aggr_10_90_prom6_core_multifactor_quality_tilt",
        "aggr_10_90_prom6_core_multifactor_momentum_quality",
        "aggr_05_95_prom7_core_multifactor_balanced",
        "aggr_05_95_prom7_core_multifactor_quality_tilt",
        "aggr_05_95_prom7_core_multifactor_momentum_quality",
        "aggr_08_92_prom6_core_multifactor_growth_quality",
        "aggr_10_90_prom6_core_multifactor_growth_quality",
        "aggr_05_95_prom7_core_multifactor_growth_quality",
        "aggr_08_92_prom6_core_multifactor_industry_quality",
        "aggr_08_92_prom6_core_multifactor_quality_defense",
        "aggr_08_92_prom6_core_multifactor_trend_quality_defense",
        "aggr_08_92_prom6_core_multifactor_trend_lowvol_quality",
        "aggr_08_92_prom6_core_multifactor_trend_momentum_quality",
        "aggr_08_92_prom6_core_multifactor_trend_industry_momentum",
        "aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol",
        "aggr_08_92_prom6_core_multifactor_industry_momentum_quality",
        "aggr_08_92_prom6_core_multifactor_trend_quality_rebalance",
        "aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance",
        "aggr_08_92_prom6_core_multifactor_quality_lowvol_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_trend_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_trend_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_industry_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_industry_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_lowvol_value_reconfirm",
        "aggr_08_92_prom6_core_multifactor_profitability_value_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_profitability_industry_signal_reconfirm",
        "aggr_08_92_prom6_core_multifactor_profitability_growth_signal_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_industry_signal_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_growth_industry_cost_guard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_cost_guard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk18_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk16_reconfirm",
        "aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk16_reconfirm",
    ],
    "holding_shape": [
        "share_15_85_hold_4_6",
        "aggr_10_90_hold_4_6",
        "share_12_88_hold_4_6",
        "aggr_09_91_prom7",
        "aggr_08_92_hold_3_6",
        "aggr_08_92_hold_3_6_ramp90",
        "aggr_07_93_hold_3_7_ramp90",
        "share_10_90_hold_3_7",
        "share_10_90_hold_3_7_ramp80_cost_guard",
        "share_08_92_hold_3_7_ramp90_cost_guard",
        "share_12_88_hold_3_7_ramp85_cost_guard",
        "share_06_94_hold_2_8_ramp85",
        "share_06_94_hold_2_8_ramp85_cost_guard",
        "share_06_94_hold_2_8_ramp80_cost_guard",
        "share_06_94_hold_2_8_ramp75_cost_guard",
        "share_08_92_hold_2_8_ramp85_cost_guard",
        "share_08_92_hold_2_8_ramp80_cost_guard",
        "share_08_92_hold_2_8_ramp75_cost_guard",
        "share_10_90_hold_2_8_ramp85_cost_guard",
        "share_10_90_hold_2_8_ramp80_cost_guard",
        "share_12_88_hold_2_8_ramp80_cost_guard",
        "share_12_88_hold_2_8_ramp75_cost_guard",
        "share_14_86_hold_2_8_ramp75_cost_guard",
        "share_16_84_hold_2_8_ramp70_cost_guard",
        "share_18_82_hold_2_8_ramp68_cost_guard",
        "share_20_80_hold_2_8_ramp66_cost_guard",
        "share_22_78_hold_2_8_ramp64_cost_guard",
        "aggr_05_95_prom7",
    ],
    "supporting_variants": [
        "aggr_08_92_prom6",
        "aggr_08_92_prom6_ramp90",
        "aggr_08_92_prom7",
        "aggr_08_92_prom7_ramp90",
    ],
    "drawdown_guard": [
        "aggr_08_92_prom6_cash_off_dd_guard50",
        "aggr_08_92_prom6_core_6_1_dd_guard35",
        "aggr_05_95_prom7_core_6_1_full_risk_dd_guard35",
        "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard50",
        "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard30_fast",
        "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard0_fast",
        "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50",
    ],
}

PATH1_FAST_PASS_VARIANT_IDS = [
    "share_15_85_hold_4_6",
    "aggr_10_90_fast_ramp",
    "aggr_10_90_hold_4_6",
    "aggr_10_90_prom5",
    "aggr_10_90_prom6",
    "aggr_10_90_prom7",
    "aggr_10_90_prom7_ramp90",
    "aggr_08_92_prom6",
    "aggr_08_92_prom6_ramp90",
    "aggr_08_92_prom7",
    "aggr_08_92_prom7_ramp90",
    "aggr_08_92_prom6_cash_off",
    "aggr_08_92_prom6_cash_off_and",
    "aggr_10_90_prom6_cash_off",
    "aggr_10_90_fast_ramp_cash_off",
    "aggr_10_90_fast_ramp_cash_off_and",
    "aggr_08_92_prom6_satellite_cost_guard",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_cashguard_light",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk30_reconfirm",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk15_reconfirm",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm",
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk12_reconfirm",
    "aggr_08_92_prom6_core_6_1",
    "aggr_10_90_prom6_core_6_1",
    "aggr_08_92_prom6_core_multifactor_balanced",
    "aggr_08_92_prom6_core_multifactor_quality_tilt",
    "aggr_08_92_prom6_core_multifactor_momentum_quality",
    "aggr_10_90_prom6_core_multifactor_balanced",
    "aggr_10_90_prom6_core_multifactor_quality_tilt",
    "aggr_10_90_prom6_core_multifactor_momentum_quality",
    "aggr_05_95_prom7_core_multifactor_balanced",
    "aggr_05_95_prom7_core_multifactor_quality_tilt",
    "aggr_05_95_prom7_core_multifactor_momentum_quality",
    "aggr_08_92_prom6_core_multifactor_growth_quality",
    "aggr_10_90_prom6_core_multifactor_growth_quality",
    "aggr_05_95_prom7_core_multifactor_growth_quality",
    "aggr_08_92_prom6_core_multifactor_industry_quality",
    "aggr_08_92_prom6_core_multifactor_quality_defense",
    "aggr_08_92_prom6_core_multifactor_trend_quality_defense",
    "aggr_08_92_prom6_core_multifactor_trend_lowvol_quality",
    "aggr_08_92_prom6_core_multifactor_trend_momentum_quality",
    "aggr_08_92_prom6_core_multifactor_trend_industry_momentum",
    "aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol",
    "aggr_08_92_prom6_core_multifactor_industry_momentum_quality",
    "aggr_08_92_prom6_core_multifactor_trend_quality_rebalance",
    "aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_trend_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_trend_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_industry_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_industry_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_value_reconfirm",
    "aggr_08_92_prom6_core_multifactor_profitability_value_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_profitability_industry_signal_reconfirm",
    "aggr_08_92_prom6_core_multifactor_profitability_growth_signal_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_industry_signal_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_growth_industry_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk18_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk16_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk16_reconfirm",
    "aggr_09_91_prom7",
    "share_12_88_hold_4_6",
    "aggr_08_92_hold_3_6",
    "aggr_08_92_hold_3_6_ramp90",
    "aggr_07_93_hold_3_7_ramp90",
    "share_10_90_hold_3_7",
    "share_10_90_hold_3_7_ramp80_cost_guard",
    "share_08_92_hold_3_7_ramp90_cost_guard",
    "share_12_88_hold_3_7_ramp85_cost_guard",
    "share_06_94_hold_2_8_ramp85",
    "share_06_94_hold_2_8_ramp85_cost_guard",
    "share_06_94_hold_2_8_ramp80_cost_guard",
    "share_06_94_hold_2_8_ramp75_cost_guard",
    "share_08_92_hold_2_8_ramp85_cost_guard",
    "share_08_92_hold_2_8_ramp80_cost_guard",
    "share_08_92_hold_2_8_ramp75_cost_guard",
    "share_10_90_hold_2_8_ramp85_cost_guard",
    "share_10_90_hold_2_8_ramp80_cost_guard",
    "share_12_88_hold_2_8_ramp80_cost_guard",
    "share_12_88_hold_2_8_ramp75_cost_guard",
    "share_14_86_hold_2_8_ramp75_cost_guard",
    "share_16_84_hold_2_8_ramp70_cost_guard",
    "share_18_82_hold_2_8_ramp68_cost_guard",
    "share_20_80_hold_2_8_ramp66_cost_guard",
    "share_22_78_hold_2_8_ramp64_cost_guard",
    "aggr_05_95_prom7",
    "aggr_08_92_prom6_cash_off_dd_guard50",
    "aggr_08_92_prom6_core_6_1_dd_guard35",
    "aggr_05_95_prom7_core_6_1_full_risk_dd_guard35",
    "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard50",
    "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard30_fast",
    "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard0_fast",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50",
]

PATH4_THEME_DISCOVERY_BASE_IDS = [
    "core_explore_80_20_total_mv_winner_core",
    "core_explore_90_10_equal_weight_winner_core",
    "core_explore_90_10_total_mv_winner_core",
]

PATH4_THEME_DISCOVERY_VARIANT_IDS = [
    "aggr_08_92_prom6_emergent_theme_risk30_cap50",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap10_exit60_lowturn",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap08_exit60_lowturn",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn",
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
    "aggr_13_87_prom14_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
    "aggr_13_87_prom16_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
    "aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk12_cap08_exit60_lowturn",
    "aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn",
    "aggr_13_87_prom18_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn",
    "aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
    "aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn",
    "aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn",
]

PATH2_SCAN_BASE_PREFIXES = [
    "core_explore_95_05_equal_weight_winner_core",
    "core_explore_95_05_total_mv_winner_core",
    "core_explore_90_10_equal_weight_winner_core",
    "core_explore_90_10_total_mv_winner_core",
    "core_explore_80_20_equal_weight_winner_core",
    "core_explore_70_30_equal_weight_winner_core",
    "core_explore_60_40_equal_weight_winner_core",
    "core_explore_40_60_equal_weight_winner_core",
    "core_explore_20_80_equal_weight_winner_core",
    "satellite_mom_0_100_equal_weight_winner_core",
    "momentum_top_",
]

PATH2_SCAN_FAMILY_RULES = {
    "high_concentration_breakout": {
        "prefixes": [
            "core_explore_80_20_equal_weight_winner_core",
            "core_explore_70_30_equal_weight_winner_core",
            "core_explore_60_40_equal_weight_winner_core",
            "core_explore_80_20_total_mv_winner_core",
        ],
        "variant_ids": [
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap80",
            "aggr_03_97_prom2_core_6_1_cash_off_and_risk30_cap80",
            "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80",
            "aggr_03_97_prom2_core_6_1_full_risk_cap80",
            "aggr_02_98_prom2_core_6_1_cash_off_and_cap90",
            "aggr_02_98_prom2_core_6_1_cash_off_and_risk30_cap90",
            "aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90",
            "aggr_02_98_prom2_core_6_1_full_risk_cap90",
            "aggr_01_99_prom2_core_6_1_cash_off_and_cap95",
            "aggr_01_99_prom2_core_6_1_cash_off_and_risk30_cap95",
            "aggr_01_99_prom2_core_6_1_cash_off_and_risk50_cap95",
            "aggr_01_99_prom2_core_6_1_full_risk_cap95",
            "aggr_01_99_prom2_core_6_1_cash_off_and_cap90",
            "aggr_01_99_prom1_core_6_1_cash_off_and_cap100",
            "aggr_02_98_prom1_core_6_1_cash_off_and_cap100",
            "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm80",
            "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80",
            "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130",
            "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130",
            "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp70",
            "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70",
            "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp85",
            "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp85",
            "aggr_03_97_prom1_core_6_1_cash_off_and_cap100",
            "aggr_04_96_prom1_core_6_1_cash_off_and_cap100",
            "aggr_01_99_prom1_core_6_1_cash_off_and_risk50_cap100",
            "aggr_02_98_prom1_core_6_1_cash_off_and_risk50_cap100",
            "aggr_01_99_prom1_core_6_1_full_risk_cap100",
            "aggr_02_98_prom1_core_6_1_full_risk_cap100",
            "aggr_01_99_prom1_core_3_1_cash_off_and_cap100",
            "aggr_02_98_prom1_core_3_1_cash_off_and_cap100",
            "aggr_01_99_prom1_core_3_1_full_risk_cap100",
            "aggr_02_98_prom1_core_3_1_full_risk_cap100",
            "aggr_01_99_prom2_cash_off_and_cap90",
            "aggr_01_99_prom2_full_risk_cap90",
            "aggr_02_98_prom2_cash_off_and_cap90",
            "aggr_02_98_prom2_full_risk_cap90",
            "aggr_02_98_prom2_core_6_1_cash_off_and_cap95",
            "aggr_01_99_prom3_core_6_1_cash_off_and_cap90",
            "aggr_01_99_prom3_core_6_1_cash_off_and_cap95",
            "aggr_02_98_prom3_core_6_1_cash_off_and_cap90",
            "aggr_02_98_prom3_core_6_1_cash_off_and_cap95",
            "aggr_01_99_prom2_core_3_1_cash_off_and_cap90",
            "aggr_01_99_prom2_core_3_1_cash_off_and_cap95",
            "aggr_02_98_prom2_core_3_1_cash_off_and_cap90",
            "aggr_02_98_prom2_core_3_1_cash_off_and_cap95",
            "aggr_01_99_prom2_core_3_1_cash_off_and_risk50_cap95",
            "aggr_01_99_prom2_core_3_1_full_risk_cap95",
            "aggr_02_98_prom2_core_3_1_cash_off_and_risk50_cap95",
            "aggr_02_98_prom2_core_3_1_full_risk_cap95",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap90",
            "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap90",
            "aggr_04_96_prom2_core_6_1_cash_off_and_cap90",
            "aggr_04_96_prom2_core_6_1_cash_off_and_cap80",
            "aggr_04_96_prom2_core_6_1_cash_off_and_risk30_cap80",
            "aggr_04_96_prom2_core_6_1_cash_off_and_risk50_cap80",
            "aggr_05_95_prom3_core_6_1_full_risk",
            "aggr_05_95_prom3_core_6_1_full_risk_cap60",
            "aggr_05_95_prom3_core_6_1_full_risk_cap80",
            "aggr_05_95_prom3_core_6_1_cap60",
            "aggr_05_95_prom3_core_6_1_cash_off_and_cap60",
            "aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80",
            "aggr_05_95_prom3_core_6_1_cash_off_and_cap80",
            "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80",
            "aggr_04_96_prom3_core_6_1_cash_off_and_cap70",
            "aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70",
            "aggr_05_95_prom7_core_6_1_full_risk",
            "aggr_05_95_prom7_core_6_1_full_risk_cap40",
            "aggr_05_95_prom7_core_3_1_full_risk_cap40",
            "aggr_05_95_prom7",
            "aggr_06_94_prom7",
            "aggr_08_92_prom6_conc35_10",
            "aggr_10_90_prom6_conc35_10",
            "aggr_12_88_prom7",
            "aggr_15_85_prom7",
            "share_12_88_hold_3_7",
        ],
        "target_candidates": 6,
    },
    "decorrelated_defensive_mix": {
        "prefixes": [
            "core_explore_80_20_equal_weight_winner_core",
            "core_explore_80_20_total_mv_winner_core",
            "core_explore_90_10_equal_weight_winner_core",
            "core_explore_90_10_total_mv_winner_core",
        ],
        "variant_ids": [
            "aggr_08_92_prom6_core_multifactor_industry_quality",
            "aggr_08_92_prom6_core_multifactor_quality_defense",
            "aggr_08_92_prom6_core_multifactor_trend_quality_defense",
            "aggr_08_92_prom6_core_multifactor_trend_lowvol_quality",
            "aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol",
            "aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance",
            "aggr_08_92_prom6_core_multifactor_quality_lowvol_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_trend_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm",
            "aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm",
            "aggr_08_92_prom6_core_multifactor_profitability_value_cashguard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_cost_guard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm",
            "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm",
            "share_08_92_hold_2_8_ramp85_cost_guard",
            "share_08_92_hold_2_8_ramp80_cost_guard",
            "share_08_92_hold_2_8_ramp75_cost_guard",
            "share_10_90_hold_2_8_ramp85_cost_guard",
            "share_10_90_hold_2_8_ramp80_cost_guard",
            "share_12_88_hold_2_8_ramp80_cost_guard",
            "share_12_88_hold_2_8_ramp75_cost_guard",
            "share_12_88_hold_3_7_ramp85_cost_guard",
            "share_08_92_hold_3_7_ramp90_cost_guard",
        ],
        "target_candidates": 8,
    },
    "high_growth_theme": {
        "prefixes": [
            "core_explore_95_05_equal_weight_winner_core",
            "core_explore_95_05_total_mv_winner_core",
            "core_explore_90_10_equal_weight_winner_core",
            "core_explore_90_10_total_mv_winner_core",
            "core_explore_80_20_equal_weight_winner_core",
            "core_explore_20_80_equal_weight_winner_core",
            "core_explore_40_60_equal_weight_winner_core",
            "core_explore_80_20_total_mv_winner_core",
        ],
        "variant_ids": [
            "aggr_08_92_prom6_full_risk",
            "aggr_08_92_prom6_core_6_1_full_risk",
            "aggr_08_92_prom6_core_6_1_full_risk_cap40",
            "aggr_08_92_prom6_core_6_1_full_risk_cap60",
            "aggr_08_92_prom6_core_3_1_full_risk_cap40",
            "aggr_10_90_fast_ramp_cash_off",
            "aggr_10_90_fast_ramp_cash_off_and",
            "aggr_07_93_prom6",
            "aggr_07_93_prom8",
            "aggr_07_93_prom8_ramp85",
            "aggr_10_90_prom6_ramp85",
            "aggr_10_90_prom6_ramp90",
            "balance_15_85_fast_ramp",
            "balance_20_80_step_ramp",
            "mid_15_85_prom7",
            "aggr_01_99_prom1_core_theme_cash_off_and_cap100",
            "aggr_02_98_prom1_core_theme_cash_off_and_cap100",
            "aggr_01_99_prom2_core_theme_cash_off_and_cap95",
            "aggr_02_98_prom2_core_theme_cash_off_and_cap95",
            "aggr_01_99_prom1_industry_trend_cash_off_and_cap100",
            "aggr_02_98_prom1_industry_trend_cash_off_and_cap100",
            "aggr_01_99_prom2_industry_trend_cash_off_and_cap95",
            "aggr_02_98_prom2_industry_trend_cash_off_and_cap95",
            "aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100",
            "aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100",
            "aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95",
            "aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95",
            "aggr_01_99_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100",
            "aggr_02_98_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm75_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm75_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm80_amt110_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm80_amt110_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard_v2",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit58_reconfirm80_cap80_cost_guard_v3",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk32_mom_exit52_reconfirm88_caution60_cap55_cost_guard_v8",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk34_mom_exit54_reconfirm86_caution62_cap58_cost_guard_v9",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk36_mom_exit54_reconfirm84_caution64_cap55_cost_guard_v10",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk36_mom_exit54_reconfirm84_caution66_cap50_cost_guard_v11",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk34_mom_exit52_reconfirm86_caution64_cap48_cost_guard_v12",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm88_caution62_cap50_cost_guard_v13",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm90_caution60_cap45_cost_guard_v14",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk32_mom_exit52_reconfirm88_caution62_cap40_cost_guard_v15",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk34_mom_exit54_reconfirm86_caution64_cap42_cost_guard_v16",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap32_cost_guard_v18",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution54_cap24_cost_guard_v20",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution52_cap22_cost_guard_v21",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm98_caution54_cap24_cost_guard_v36_risk_reconfirm",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm92_caution60_cap32_cost_guard_v24_medium_cycle",
            "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle",
            "aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm95_caution62_cap28_cost_guard_v26_medium_cycle",
            "aggr_04_96_prom4_core_6_1_promo_liqmom_top13_risk28_mom_exit48_reconfirm96_caution64_cap24_cost_guard_v27_medium_cycle",
            "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle",
            "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v31_medium_cycle",
            "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v32_capacity_stress",
            "aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap18_cost_guard_v33_medium_cycle_repair",
            "aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v34_reconfirm_balance",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_caution80_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_caution80_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_mom_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_mom_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_ma_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_ma_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk50_mom_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk50_mom_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top18_risk50_mom_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top18_risk50_mom_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution80_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution80_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution75_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution75_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution75_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution75_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm80_amt110_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm80_amt110_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution70_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution60_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution60_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm75_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm75_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm80_amt110_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm80_amt110_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap80",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap70",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_ramp85_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_ramp70_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit80_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit80_cap95",
            "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit60_cap95",
            "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit60_cap95",
            "aggr_06_94_prom4_core_6_1_full_risk_cap70",
            "aggr_06_94_prom4_core_6_1_cash_off_and_cap70",
        ],
        "target_candidates": 4,
    },
    "momentum_equal_weight_elastic": {
        "prefixes": [
            "core_explore_80_20_equal_weight_winner_core",
            "core_explore_80_20_total_mv_winner_core",
        ],
        "prefix_only_prefixes": [
            "momentum_top_",
            "satellite_mom_0_100_equal_weight_winner_core",
        ],
        "variant_ids": [
            "aggr_08_92_prom6_cash_off",
            "aggr_08_92_prom6_cash_off_and",
            "aggr_08_92_prom6_core_6_1",
            "aggr_10_90_prom6_core_6_1",
            "aggr_08_92_prom6_core_multifactor_balanced",
            "aggr_10_90_prom6_core_multifactor_balanced",
            "aggr_08_92_prom6_core_multifactor_growth_quality",
            "aggr_10_90_prom6_core_multifactor_growth_quality",
            "aggr_05_95_prom7_core_multifactor_growth_quality",
            "aggr_08_92_prom6_core_multifactor_quality_defense",
            "aggr_08_92_prom6_core_multifactor_trend_quality_defense",
            "aggr_08_92_prom6_core_multifactor_trend_lowvol_quality",
            "aggr_08_92_prom6_core_multifactor_trend_momentum_quality",
            "aggr_08_92_prom6_core_multifactor_trend_industry_momentum",
            "aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol",
            "aggr_08_92_prom6_core_multifactor_industry_momentum_quality",
            "aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance",
            "aggr_10_90_prom6",
            "aggr_10_90_fast_ramp_cash_off",
            "aggr_10_90_fast_ramp_cash_off_and",
            "aggr_08_92_prom6_risk_on",
            "aggr_10_90_prom6_risk_on",
        ],
        "target_candidates": 6,
    },
    "biweekly_rebalance_aggressive": {
        "prefixes": [
            "core_explore_80_20_equal_weight_winner_core",
            "core_explore_70_30_equal_weight_winner_core",
            "core_explore_60_40_equal_weight_winner_core",
            "core_explore_40_60_equal_weight_winner_core",
            "core_explore_20_80_equal_weight_winner_core",
        ],
        "variant_ids": [
            "aggr_03_97_prom2_core_6_1_full_risk_cap80_biweekly",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap80_biweekly",
            "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80_biweekly",
            "aggr_01_99_prom2_core_6_1_cash_off_and_cap90_biweekly",
            "aggr_01_99_prom2_core_6_1_cash_off_and_cap95_biweekly",
            "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_biweekly",
            "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_biweekly",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly",
            "aggr_05_95_prom3_core_6_1_full_risk_cap80_biweekly",
            "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_biweekly",
            "aggr_05_95_prom3_core_6_1_cash_off_and_cap50_biweekly",
            "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_biweekly",
            "aggr_08_92_prom6_core_6_1_full_risk_cap40_biweekly",
            "aggr_08_92_prom6_core_6_1_full_risk_cap60_biweekly",
            "aggr_05_95_prom3_core_6_1_full_risk_cap60_biweekly",
            "aggr_08_92_prom6_cash_off_and_biweekly",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly_cost_guard",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap65_biweekly_cost_guard",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard",
            "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk28_exit46_cap24_cost_guard_v28",
            "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29",
            "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn",
        ],
        "target_candidates": 6,
    },
    "weekly_rebalance_aggressive": {
        "prefixes": [
            "core_explore_80_20_equal_weight_winner_core",
            "core_explore_70_30_equal_weight_winner_core",
            "core_explore_60_40_equal_weight_winner_core",
            "core_explore_40_60_equal_weight_winner_core",
            "core_explore_20_80_equal_weight_winner_core",
        ],
        "variant_ids": [
            "aggr_03_97_prom2_core_6_1_full_risk_cap80_weekly",
            "aggr_03_97_prom2_core_6_1_cash_off_and_cap80_weekly",
            "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80_weekly",
            "aggr_01_99_prom2_core_6_1_cash_off_and_cap90_weekly",
            "aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly",
            "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly",
            "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_weekly",
            "aggr_05_95_prom3_core_6_1_full_risk_cap80_weekly",
            "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_weekly",
            "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly",
            "aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly",
            "aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly",
            "aggr_05_95_prom3_core_6_1_full_risk_cap60_weekly",
            "aggr_08_92_prom6_cash_off_and_weekly",
            "aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit90_weekly",
            "aggr_08_92_prom6_cash_off_and_cap55_hold2_turn10_exit92_weekly",
            "aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly",
            "aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly",
            "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly",
            "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly",
            "aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly",
            "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn06_exit92_weekly",
            "aggr_08_92_prom6_cash_off_and_cap55_hold3_turn06_exit92_weekly",
            "aggr_08_92_prom6_cash_off_and_cap55_hold3_turn04_exit94_weekly",
            "aggr_08_92_prom6_cash_off_and_cap58_hold4_turn03_exit96_weekly",
            "aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly",
            "aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly",
            "aggr_08_92_prom6_cost_guard_cap58_hold6_turn02_exit96_risk25_weekly",
            "aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly",
            "aggr_08_92_prom6_weekly_alpha_balanced_risk50_cap40_hold2_turn40_weekly",
            "aggr_05_95_prom3_weekly_alpha_balanced_risk50_cap60_hold2_turn30_weekly",
            "aggr_03_97_prom2_weekly_alpha_balanced_cashoff_cap80_hold3_turn25_weekly",
            "aggr_08_92_prom6_weekly_alpha_breakout_risk50_cap40_hold2_turn40_weekly",
            "aggr_05_95_prom3_weekly_alpha_breakout_risk50_cap60_hold2_turn30_weekly",
            "aggr_03_97_prom2_weekly_alpha_breakout_cashoff_cap80_hold3_turn25_weekly",
            "aggr_08_92_prom6_weekly_alpha_pullback_risk50_cap40_hold2_turn40_weekly",
            "aggr_05_95_prom3_weekly_alpha_pullback_risk50_cap60_hold2_turn30_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn15_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold7_turn10_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold8_turn08_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold9_turn08_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn10_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn08_exit85_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly",
            "aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap55_hold4_turn18_weekly",
            "aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap50_hold4_turn18_exit85_weekly",
            "aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap50_hold5_turn14_exit85_weekly",
            "aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap45_hold5_turn12_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold4_turn16_exit85_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn14_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk35_cap70_hold5_turn10_exit88_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold6_turn08_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap65_hold6_turn08_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold7_turn06_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn05_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold7_turn05_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn06_exit88_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn04_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn04_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn04_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn04_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold8_turn04_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold9_turn03_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn03_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold10_turn03_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold10_turn03_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold10_turn02_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap58_hold10_turn02_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn02_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold9_turn02_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap62_hold9_turn02_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap64_hold8_turn03_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap64_hold8_turn03_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit94_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit96_weekly",
            "aggr_03_97_prom2_weekly_alpha_pullback_risk20_cap66_hold7_turn04_exit94_weekly",
        ],
        "target_candidates": 6,
    },
}

PATH2_SCAN_VARIANT_IDS = [
    "aggr_08_92_prom6_cash_off",
    "aggr_08_92_prom6_cash_off_and",
    "aggr_10_90_fast_ramp_cash_off",
    "aggr_10_90_fast_ramp_cash_off_and",
    "aggr_10_90_prom6",
    "aggr_08_92_prom6_core_6_1",
    "aggr_10_90_prom6_core_6_1",
    "aggr_08_92_prom6_core_multifactor_balanced",
    "aggr_10_90_prom6_core_multifactor_balanced",
    "aggr_08_92_prom6_core_multifactor_growth_quality",
    "aggr_10_90_prom6_core_multifactor_growth_quality",
    "aggr_05_95_prom7_core_multifactor_growth_quality",
    "aggr_08_92_prom6_core_multifactor_industry_quality",
    "aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_defense",
    "aggr_08_92_prom6_core_multifactor_trend_quality_defense",
    "aggr_08_92_prom6_core_multifactor_trend_lowvol_quality",
    "aggr_08_92_prom6_core_multifactor_trend_momentum_quality",
    "aggr_08_92_prom6_core_multifactor_trend_industry_momentum",
    "aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol",
    "aggr_08_92_prom6_core_multifactor_industry_momentum_quality",
    "aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_trend_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm",
    "aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm",
    "aggr_08_92_prom6_core_multifactor_profitability_value_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_growth_industry_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_cost_guard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm",
    "aggr_08_92_prom6_core_multifactor_quality_industry_reconfirm",
    "share_08_92_hold_3_7_ramp90_cost_guard",
    "share_12_88_hold_3_7_ramp85_cost_guard",
    "share_08_92_hold_2_8_ramp85_cost_guard",
    "share_08_92_hold_2_8_ramp80_cost_guard",
    "share_08_92_hold_2_8_ramp75_cost_guard",
    "share_10_90_hold_2_8_ramp85_cost_guard",
    "share_10_90_hold_2_8_ramp80_cost_guard",
    "share_12_88_hold_2_8_ramp75_cost_guard",
    "aggr_08_92_prom6_full_risk",
    "aggr_08_92_prom6_core_3_1_full_risk_cap40",
    "aggr_08_92_prom6_core_6_1_full_risk",
    "aggr_08_92_prom6_core_6_1_full_risk_cap40",
    "aggr_08_92_prom6_core_6_1_full_risk_cap60",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap80",
    "aggr_03_97_prom2_core_6_1_cash_off_and_risk30_cap80",
    "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80",
    "aggr_03_97_prom2_core_6_1_full_risk_cap80",
    "aggr_02_98_prom2_core_6_1_cash_off_and_cap90",
    "aggr_02_98_prom2_core_6_1_cash_off_and_risk30_cap90",
    "aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90",
    "aggr_02_98_prom2_core_6_1_full_risk_cap90",
    "aggr_01_99_prom2_core_6_1_cash_off_and_cap95",
    "aggr_01_99_prom2_core_6_1_cash_off_and_risk30_cap95",
    "aggr_01_99_prom2_core_6_1_cash_off_and_risk50_cap95",
    "aggr_01_99_prom2_core_6_1_full_risk_cap95",
    "aggr_01_99_prom2_core_6_1_cash_off_and_cap90",
    "aggr_01_99_prom1_core_6_1_cash_off_and_cap100",
    "aggr_02_98_prom1_core_6_1_cash_off_and_cap100",
    "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm80",
    "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80",
    "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130",
    "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130",
    "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp70",
    "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70",
    "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp85",
    "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp85",
    "aggr_03_97_prom1_core_6_1_cash_off_and_cap100",
    "aggr_04_96_prom1_core_6_1_cash_off_and_cap100",
    "aggr_01_99_prom1_core_6_1_cash_off_and_risk50_cap100",
    "aggr_02_98_prom1_core_6_1_cash_off_and_risk50_cap100",
    "aggr_01_99_prom1_core_6_1_full_risk_cap100",
    "aggr_02_98_prom1_core_6_1_full_risk_cap100",
    "aggr_01_99_prom1_core_3_1_cash_off_and_cap100",
    "aggr_02_98_prom1_core_3_1_cash_off_and_cap100",
    "aggr_01_99_prom1_core_3_1_full_risk_cap100",
    "aggr_02_98_prom1_core_3_1_full_risk_cap100",
    "aggr_01_99_prom1_core_theme_cash_off_and_cap100",
    "aggr_02_98_prom1_core_theme_cash_off_and_cap100",
    "aggr_01_99_prom2_core_theme_cash_off_and_cap95",
    "aggr_02_98_prom2_core_theme_cash_off_and_cap95",
    "aggr_01_99_prom1_industry_trend_cash_off_and_cap100",
    "aggr_02_98_prom1_industry_trend_cash_off_and_cap100",
    "aggr_01_99_prom2_industry_trend_cash_off_and_cap95",
    "aggr_02_98_prom2_industry_trend_cash_off_and_cap95",
    "aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100",
    "aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100",
    "aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95",
    "aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95",
    "aggr_01_99_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100",
    "aggr_02_98_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm75_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm75_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm80_amt110_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm80_amt110_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_caution80_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_caution80_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_mom_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_mom_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_ma_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_ma_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk50_mom_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk50_mom_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top18_risk50_mom_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top18_risk50_mom_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution80_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution80_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution75_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution75_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution75_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution75_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm80_amt110_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm80_amt110_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution70_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution60_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_caution60_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm75_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm75_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm80_amt110_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm80_amt110_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap80",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap70",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_ramp85_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_ramp70_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit80_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit80_cap95",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit60_cap95",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit60_cap95",
    "aggr_01_99_prom2_cash_off_and_cap90",
    "aggr_01_99_prom2_full_risk_cap90",
    "aggr_02_98_prom2_cash_off_and_cap90",
    "aggr_02_98_prom2_full_risk_cap90",
    "aggr_02_98_prom2_core_6_1_cash_off_and_cap95",
    "aggr_01_99_prom3_core_6_1_cash_off_and_cap90",
    "aggr_01_99_prom3_core_6_1_cash_off_and_cap95",
    "aggr_02_98_prom3_core_6_1_cash_off_and_cap90",
    "aggr_02_98_prom3_core_6_1_cash_off_and_cap95",
    "aggr_01_99_prom2_core_3_1_cash_off_and_cap90",
    "aggr_01_99_prom2_core_3_1_cash_off_and_cap95",
    "aggr_02_98_prom2_core_3_1_cash_off_and_cap90",
    "aggr_02_98_prom2_core_3_1_cash_off_and_cap95",
    "aggr_01_99_prom2_core_3_1_cash_off_and_risk50_cap95",
    "aggr_01_99_prom2_core_3_1_full_risk_cap95",
    "aggr_02_98_prom2_core_3_1_cash_off_and_risk50_cap95",
    "aggr_02_98_prom2_core_3_1_full_risk_cap95",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap90",
    "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap90",
    "aggr_04_96_prom2_core_6_1_cash_off_and_cap90",
    "aggr_04_96_prom2_core_6_1_cash_off_and_cap80",
    "aggr_04_96_prom2_core_6_1_cash_off_and_risk30_cap80",
    "aggr_04_96_prom2_core_6_1_cash_off_and_risk50_cap80",
    "aggr_03_97_prom2_core_6_1_full_risk_cap80_biweekly",
    "aggr_03_97_prom2_core_6_1_full_risk_cap80_weekly",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap80_biweekly",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap65_biweekly_cost_guard",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap80_weekly",
    "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80_biweekly",
    "aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80_weekly",
    "aggr_01_99_prom2_core_6_1_cash_off_and_cap90_biweekly",
    "aggr_01_99_prom2_core_6_1_cash_off_and_cap90_weekly",
    "aggr_01_99_prom2_core_6_1_cash_off_and_cap95_biweekly",
    "aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly",
    "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_biweekly",
    "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_biweekly",
    "aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly",
    "aggr_02_98_prom1_core_6_1_cash_off_and_cap100_weekly",
    "aggr_05_95_prom3_core_6_1_full_risk",
    "aggr_05_95_prom3_core_6_1_full_risk_cap60",
    "aggr_05_95_prom3_core_6_1_full_risk_cap80",
    "aggr_05_95_prom3_core_6_1_full_risk_cap80_biweekly",
    "aggr_05_95_prom3_core_6_1_full_risk_cap80_weekly",
    "aggr_05_95_prom3_core_6_1_cap60",
    "aggr_05_95_prom3_core_6_1_cash_off_and_cap60",
    "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_biweekly",
    "aggr_05_95_prom3_core_6_1_cash_off_and_cap50_biweekly",
    "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_weekly",
    "aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80",
    "aggr_05_95_prom3_core_6_1_cash_off_and_cap80",
    "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80",
    "aggr_04_96_prom3_core_6_1_cash_off_and_cap70",
    "aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70",
    "aggr_06_94_prom4_core_6_1_full_risk_cap70",
    "aggr_06_94_prom4_core_6_1_cash_off_and_cap70",
    "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_biweekly",
    "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly",
    "aggr_05_95_prom7_core_6_1_full_risk",
    "aggr_05_95_prom7_core_6_1_full_risk_cap40",
    "aggr_05_95_prom7_core_3_1_full_risk_cap40",
    "aggr_05_95_prom7",
    "aggr_06_94_prom7",
    "aggr_07_93_prom6",
    "aggr_07_93_prom8",
    "aggr_07_93_prom8_ramp85",
    "aggr_08_92_prom6_conc35_10",
    "aggr_08_92_prom6_risk_on",
    "aggr_10_90_prom6_conc35_10",
    "aggr_10_90_prom6_ramp85",
    "aggr_10_90_prom6_ramp90",
    "aggr_10_90_prom6_risk_on",
    "aggr_12_88_prom7",
    "aggr_15_85_prom7",
    "balance_15_85_fast_ramp",
    "balance_20_80_step_ramp",
    "mid_15_85_prom7",
    "share_12_88_hold_3_7",
    "aggr_08_92_prom6_core_6_1_full_risk_cap40_biweekly",
    "aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly",
    "aggr_08_92_prom6_core_6_1_full_risk_cap60_biweekly",
    "aggr_05_95_prom3_core_6_1_full_risk_cap60_biweekly",
    "aggr_08_92_prom6_cash_off_and_biweekly",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly_cost_guard",
    "aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard",
    "aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly",
    "aggr_05_95_prom3_core_6_1_full_risk_cap60_weekly",
    "aggr_08_92_prom6_cash_off_and_weekly",
    "aggr_08_92_prom6_weekly_alpha_balanced_risk50_cap40_hold2_turn40_weekly",
    "aggr_05_95_prom3_weekly_alpha_balanced_risk50_cap60_hold2_turn30_weekly",
    "aggr_03_97_prom2_weekly_alpha_balanced_cashoff_cap80_hold3_turn25_weekly",
    "aggr_08_92_prom6_weekly_alpha_breakout_risk50_cap40_hold2_turn40_weekly",
    "aggr_05_95_prom3_weekly_alpha_breakout_risk50_cap60_hold2_turn30_weekly",
    "aggr_03_97_prom2_weekly_alpha_breakout_cashoff_cap80_hold3_turn25_weekly",
    "aggr_08_92_prom6_weekly_alpha_pullback_risk50_cap40_hold2_turn40_weekly",
    "aggr_05_95_prom3_weekly_alpha_pullback_risk50_cap60_hold2_turn30_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn15_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold7_turn10_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold8_turn08_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold9_turn08_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn10_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn08_exit85_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly",
    "aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap55_hold4_turn18_weekly",
    "aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap50_hold4_turn18_exit85_weekly",
    "aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap50_hold5_turn14_exit85_weekly",
    "aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap45_hold5_turn12_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold4_turn16_exit85_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn14_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk35_cap70_hold5_turn10_exit88_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap65_hold6_turn08_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap65_hold6_turn08_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold7_turn06_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn05_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold7_turn05_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn06_exit88_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn04_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn04_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn04_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold8_turn04_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold9_turn03_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn03_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold10_turn03_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold10_turn03_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap58_hold10_turn02_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn02_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold9_turn02_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap62_hold9_turn02_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap64_hold8_turn03_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap64_hold8_turn03_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit94_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit96_weekly",
    "aggr_03_97_prom2_weekly_alpha_pullback_risk20_cap66_hold7_turn04_exit94_weekly",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard_v2",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit58_reconfirm80_cap80_cost_guard_v3",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk32_mom_exit52_reconfirm88_caution60_cap55_cost_guard_v8",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk34_mom_exit54_reconfirm86_caution62_cap58_cost_guard_v9",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk36_mom_exit54_reconfirm84_caution64_cap55_cost_guard_v10",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk36_mom_exit54_reconfirm84_caution66_cap50_cost_guard_v11",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk34_mom_exit52_reconfirm86_caution64_cap48_cost_guard_v12",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm88_caution62_cap50_cost_guard_v13",
    "aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm90_caution60_cap45_cost_guard_v14",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk32_mom_exit52_reconfirm88_caution62_cap40_cost_guard_v15",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk34_mom_exit54_reconfirm86_caution64_cap42_cost_guard_v16",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap32_cost_guard_v18",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution54_cap24_cost_guard_v20",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution52_cap22_cost_guard_v21",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm98_caution54_cap24_cost_guard_v36_risk_reconfirm",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm92_caution60_cap32_cost_guard_v24_medium_cycle",
    "aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle",
    "aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm95_caution62_cap28_cost_guard_v26_medium_cycle",
    "aggr_04_96_prom4_core_6_1_promo_liqmom_top13_risk28_mom_exit48_reconfirm96_caution64_cap24_cost_guard_v27_medium_cycle",
    "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk28_exit46_cap24_cost_guard_v28",
    "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29",
    "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn",
    "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle",
    "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v31_medium_cycle",
    "aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v32_capacity_stress",
    "aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap18_cost_guard_v33_medium_cycle_repair",
    "aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v34_reconfirm_balance",
    "aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard",
    "aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit90_weekly",
    "aggr_08_92_prom6_cash_off_and_cap55_hold2_turn10_exit92_weekly",
    "aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly",
    "aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly",
    "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly",
    "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly",
    "aggr_08_92_prom6_cash_off_and_cap60_hold3_turn06_exit92_weekly",
    "aggr_08_92_prom6_cash_off_and_cap55_hold3_turn06_exit92_weekly",
    "aggr_08_92_prom6_cash_off_and_cap55_hold3_turn04_exit94_weekly",
    "aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly",
    "aggr_08_92_prom6_cash_off_and_cap58_hold4_turn03_exit96_weekly",
    "aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly",
    "aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit92_risk25_weekly",
    "aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly",
    "aggr_08_92_prom6_cost_guard_cap58_hold6_turn02_exit96_risk25_weekly",
    "aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly",
    "aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk20_weekly",
    "aggr_08_92_prom6_cost_guard_cap56_hold6_turn03_exit96_risk20_weekly",
    "aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly",
    "aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk18_weekly",
    "aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit96_risk18_weekly",
    "aggr_08_92_prom6_cost_guard_cap52_hold5_turn05_exit98_risk18_weekly",
    "aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit98_risk16_weekly",
    "aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly",
]

PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS = [
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold5_turn05_exit98_risk18_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit96_risk18_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk18_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn04_exit94_risk20_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold6_turn03_exit96_risk20_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk20_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold6_turn02_exit96_risk25_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit92_risk25_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_balanced_risk50_cap60_hold2_turn30_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold6_turn12_exit85_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn10_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold9_turn08_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn08_exit85_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap50_hold4_turn18_exit85_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap50_hold5_turn14_exit85_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap45_hold5_turn12_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn14_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk35_cap70_hold5_turn10_exit88_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap65_hold6_turn08_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap65_hold6_turn08_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold7_turn06_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn05_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold7_turn05_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn06_exit88_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn04_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn04_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn04_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold8_turn04_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn04_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold9_turn03_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn03_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold10_turn03_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold10_turn03_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold10_turn03_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold10_turn02_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly",
    "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap58_hold10_turn02_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn02_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold9_turn02_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap62_hold9_turn02_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap64_hold8_turn03_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap64_hold8_turn03_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit96_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk20_cap66_hold7_turn04_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold6_turn08_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold2_turn10_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit90_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold4_turn16_exit85_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn06_exit92_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn04_exit94_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn03_exit96_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly",
]

FACTOR_CACHE_VERSION = "v3"
WINNER_ONLY_STRATEGY_ID = "core_explore_80_20_total_mv_winner_core"
INDEX_CORE_BASE_ID = "core_explore_80_20_total_mv_index_core"
ACTIVE_FAMILY_BASE_PREFIXES = [
    "core_explore_80_20_total_mv_index_core",
    "core_explore_80_20_total_mv_winner_core",
]
CORE_ACTIVE_REGISTRY_PATH = research_file("core_active_registry.json")
CORE_ACTIVE_MAX_SIZE = 128
CORE_ACTIVE_STALE_TRADING_DAYS = 30
# Legacy import alias; core_active is now loaded from CORE_ACTIVE_REGISTRY_PATH.
CORE_ACTIVE_FAMILY_BASE_IDS = []
ARCHIVE_FAMILY_BASE_PREFIXES = [
    "core_explore_70_30_",
    "core_explore_60_40_",
    "core_explore_80_20_index_weight_",
    "core_explore_80_20_equal_weight_",
    "pure_core_growth_",
]

CORE_EXPLORE_RATIO_CONFIGS = [
    {"strategy_id": "core_explore_95_05", "strategy_name": "核心95_探索05", "core_ratio": 0.95, "explore_ratio": 0.05},
    {"strategy_id": "core_explore_90_10", "strategy_name": "核心90_探索10", "core_ratio": 0.90, "explore_ratio": 0.10},
    {"strategy_id": "core_explore_80_20", "strategy_name": "核心80_探索20", "core_ratio": 0.80, "explore_ratio": 0.20},
    {"strategy_id": "core_explore_70_30", "strategy_name": "核心70_探索30", "core_ratio": 0.70, "explore_ratio": 0.30},
    {"strategy_id": "core_explore_60_40", "strategy_name": "核心60_探索40", "core_ratio": 0.60, "explore_ratio": 0.40},
    {
        "strategy_id": "pure_core_growth_5",
        "strategy_name": "纯核心成长5",
        "strategy_kind": "pure_core_growth",
        "pure_core_max_holdings": 5,
        "core_ratio": 1.00,
        "explore_ratio": 0.00,
        "weight_cap": 0.35,
    },
    {
        "strategy_id": "pure_core_growth_8",
        "strategy_name": "纯核心成长8",
        "strategy_kind": "pure_core_growth",
        "pure_core_max_holdings": 8,
        "core_ratio": 1.00,
        "explore_ratio": 0.00,
        "weight_cap": 0.35,
    },
    {
        "strategy_id": "pure_core_growth_12",
        "strategy_name": "纯核心成长12",
        "strategy_kind": "pure_core_growth",
        "pure_core_max_holdings": 12,
        "core_ratio": 1.00,
        "explore_ratio": 0.00,
        "weight_cap": 0.30,
    },
]

BASE_WEIGHT_METHODS = [
    {"base_weight_method": "total_mv", "base_weight_name": "总市值底座"},
    {"base_weight_method": "index_weight", "base_weight_name": "指数权重底座"},
    {"base_weight_method": "equal_weight", "base_weight_name": "等权底座"},
]

CORE_SOURCE_MODES = [
    {"core_source_mode": "index_core", "core_source_name": "指数核心"},
    {"core_source_mode": "winner_core", "core_source_name": "胜出者核心"},
    {"core_source_mode": "pure_core_growth", "core_source_name": "纯核心成长"},
]


def strip_weekly_overlay_suffix(strategy_base_id: str) -> str:
    base_id = str(strategy_base_id or "")
    for suffix in WEEKLY_OVERLAY_SUFFIXES:
        if base_id.endswith(suffix):
            return base_id[: -len(suffix)]
    return base_id


def extract_winner_variant_id(strategy_base_id: str) -> str | None:
    base_id = strip_weekly_overlay_suffix(strategy_base_id)
    if "__" not in base_id:
        return None
    return base_id.rsplit("__", 1)[1]


def is_path2_scan_strategy_base_id(strategy_base_id: str) -> bool:
    base_id = strip_weekly_overlay_suffix(strategy_base_id)
    variant_id = extract_winner_variant_id(base_id)
    if any(base_id.startswith(str(prefix)) for prefix in PATH2_SCAN_BASE_PREFIXES):
        return True
    if variant_id is not None and variant_id in PATH2_SCAN_VARIANT_IDS:
        return True
    for family_meta in PATH2_SCAN_FAMILY_RULES.values():
        prefixes = family_meta.get("prefixes") or []
        prefix_only_prefixes = family_meta.get("prefix_only_prefixes") or []
        variant_ids = family_meta.get("variant_ids") or []
        prefix_ok = not prefixes or any(base_id.startswith(str(prefix)) for prefix in prefixes)
        variant_match = bool(variant_id and variant_id in variant_ids and prefix_ok)
        prefix_only_match = any(base_id.startswith(str(prefix)) for prefix in prefix_only_prefixes)
        if variant_match or prefix_only_match:
            return True
    return False


def get_strategy_alpha_pool_profile(strategy_config: Dict[str, object]) -> str:
    explicit = str(strategy_config.get("alpha_pool_profile", "") or "").strip()
    if explicit:
        return explicit
    strategy_kind = str(strategy_config.get("strategy_kind", "core_explore") or "core_explore")
    if strategy_kind == "pure_core_growth":
        return ALPHA_POOL_PROFILE_GROWTH_ELASTIC
    core_signal_mode = str(strategy_config.get("core_signal_mode", "") or "").strip()
    promotion_signal_mode = str(strategy_config.get("promotion_signal_mode", "") or "").strip()
    variant_id = extract_winner_variant_id(str(strategy_config.get("strategy_base_id", "") or ""))
    if (
        core_signal_mode == EMERGENT_THEME_SIGNAL_MODE
        or promotion_signal_mode == EMERGENT_THEME_SIGNAL_MODE
        or (variant_id is not None and variant_id in PATH4_THEME_DISCOVERY_VARIANT_IDS)
    ):
        return ALPHA_POOL_PROFILE_EMERGENT_THEME
    if (
        promotion_signal_mode == "liquidity_momentum"
        or is_path2_scan_strategy_base_id(str(strategy_config.get("strategy_base_id", "") or ""))
    ):
        return ALPHA_POOL_PROFILE_GROWTH_ELASTIC
    return ALPHA_POOL_PROFILE_CORE_EXPLORE_SEED


def get_strategy_listing_months(strategy_config: Dict[str, object]) -> Tuple[int, int]:
    profile = get_strategy_alpha_pool_profile(strategy_config)
    default_core_months = PATH4_CORE_MIN_LISTING_MONTHS if profile == ALPHA_POOL_PROFILE_EMERGENT_THEME else MIN_LISTING_MONTHS
    default_seed_months = PATH4_SEED_MIN_LISTING_MONTHS if profile == ALPHA_POOL_PROFILE_EMERGENT_THEME else SEED_MIN_LISTING_MONTHS
    core_months = int(float(strategy_config.get("core_min_listing_months", default_core_months) or default_core_months))
    seed_months = int(float(strategy_config.get("seed_min_listing_months", default_seed_months) or default_seed_months))
    return max(0, core_months), max(0, seed_months)


def filter_codes_by_listing_months(
    *,
    prepared: PreparedData,
    signal_date: pd.Timestamp,
    available_codes: Iterable[str],
    min_listing_months: int,
) -> List[str]:
    cutoff = signal_date - pd.DateOffset(months=max(0, int(min_listing_months)))
    eligible: List[str] = []
    for code in available_codes:
        list_date = prepared.code_to_list_date.get(str(code), pd.NaT)
        if pd.notna(list_date) and list_date <= cutoff:
            eligible.append(str(code))
    return sorted(set(eligible))


def resolve_strategy_listing_eligible_codes(
    *,
    prepared: PreparedData,
    signal_date: pd.Timestamp,
    strategy_config: Dict[str, object],
    default_standard_eligible_codes: Iterable[str],
    default_seed_eligible_codes: Iterable[str],
    available_codes: Iterable[str],
) -> Tuple[List[str], List[str]]:
    core_months, seed_months = get_strategy_listing_months(strategy_config)
    if core_months == MIN_LISTING_MONTHS and seed_months == SEED_MIN_LISTING_MONTHS:
        return list(default_standard_eligible_codes), list(default_seed_eligible_codes)
    available = set(map(str, available_codes))
    return (
        filter_codes_by_listing_months(
            prepared=prepared,
            signal_date=signal_date,
            available_codes=available,
            min_listing_months=core_months,
        ),
        filter_codes_by_listing_months(
            prepared=prepared,
            signal_date=signal_date,
            available_codes=available,
            min_listing_months=seed_months,
        ),
    )


def filter_alpha_pool_by_signal(
    codes: Set[str],
    signal_scores: pd.Series,
    percentile: float,
) -> Set[str]:
    if not codes or signal_scores.empty or percentile >= 1.0:
        return set(codes)
    percentile = min(1.0, max(0.0001, float(percentile)))
    aligned = signal_scores.reindex(sorted(codes)).dropna()
    if aligned.empty:
        return set()
    threshold = aligned.quantile(1.0 - percentile)
    return set(aligned[aligned >= threshold].index)


def resolve_alpha_pool_universes(
    *,
    prepared: PreparedData,
    signal_date: pd.Timestamp,
    strategy_config: Dict[str, object],
    standard_eligible_codes: Iterable[str],
    seed_eligible_codes: Iterable[str],
    pool_signal_scores: pd.Series,
) -> Tuple[Set[str], Set[str], str]:
    profile = get_strategy_alpha_pool_profile(strategy_config)
    if profile == ALPHA_POOL_PROFILE_CORE_EXPLORE_SEED:
        return (
            set(prepared.core_members_by_date.get(signal_date, set())),
            set(prepared.explore_members_by_date.get(signal_date, set())),
            profile,
        )

    standard_pool = set(map(str, standard_eligible_codes))
    seed_pool = set(map(str, seed_eligible_codes))
    raw_percentile = strategy_config.get("alpha_pool_signal_percentile", 1.0)
    try:
        signal_percentile = float(raw_percentile)
    except (TypeError, ValueError):
        signal_percentile = 1.0
    standard_pool = filter_alpha_pool_by_signal(standard_pool, pool_signal_scores, signal_percentile)
    seed_pool = filter_alpha_pool_by_signal(seed_pool, pool_signal_scores, signal_percentile)
    return standard_pool, seed_pool, profile


def apply_alpha_pool_summary(summary: Dict[str, object], strategy_config: Dict[str, object]) -> None:
    profile = get_strategy_alpha_pool_profile(strategy_config)
    summary["pool_id"] = profile
    summary["pool_name"] = ALPHA_POOL_NAMES.get(profile, profile)
    summary["alpha_pool_profile"] = profile

PURE_CORE_AMOUNT_THRESHOLD = 50000.0
PURE_CORE_BUY_BUFFER_MULTIPLIER = 1.0
PURE_CORE_KEEP_BUFFER_MULTIPLIER = 2.0
PURE_CORE_OBSERVATION_BUFFER_MULTIPLIER = 3.0
PURE_CORE_OBSERVATION_MIN_STREAK = 2
PURE_CORE_BASE_WEIGHT_SHARE = 0.15
PURE_CORE_TOP3_MULTIPLIERS = [2.4, 1.8, 1.35]

CACHE_DIR = Path("data_cache")
DAILY_DIR = CACHE_DIR / "daily"
ADJ_DIR = CACHE_DIR / "adj_factor"
DAILY_BASIC_DIR = CACHE_DIR / "daily_basic"
FINA_DIR = CACHE_DIR / "fina_indicator"
INDEX_DIR = CACHE_DIR / "index_daily"
INDEX_WEIGHT_DIR = CACHE_DIR / "index_weight"
FACTOR_PANEL_DIR = CACHE_DIR / "monthly_factor_cache"
PREPARED_PANEL_DIR = CACHE_DIR / "prepared_panel_cache"
PREPARED_CACHE_VERSION = "v2"


@dataclass
class MonthlyFactorCache:
    standard_eligible_codes_by_date: Dict[pd.Timestamp, List[str]]
    seed_eligible_codes_by_date: Dict[pd.Timestamp, List[str]]
    signal_mvs_by_date: Dict[pd.Timestamp, pd.Series]
    avg_daily_amount_by_date: Dict[pd.Timestamp, pd.Series]
    amount_surge_ratio_by_date: Dict[pd.Timestamp, pd.Series]
    recent_1m_returns_by_date: Dict[pd.Timestamp, pd.Series]
    core_signal_scores_by_date: Dict[pd.Timestamp, pd.Series]
    momentum_6_1_by_date: Dict[pd.Timestamp, pd.Series]
    momentum_3_1_by_date: Dict[pd.Timestamp, pd.Series]
    breakout_signal_by_date: Dict[pd.Timestamp, pd.Series]
    quality_scores_by_date: Dict[pd.Timestamp, pd.Series]
    growth_quality_scores_by_date: Dict[pd.Timestamp, pd.Series]
    growth_acceleration_scores_by_date: Dict[pd.Timestamp, pd.Series]
    industry_strength_scores_by_date: Dict[pd.Timestamp, pd.Series]
    industry_leader_scores_by_date: Dict[pd.Timestamp, pd.Series]


@dataclass
class PreparedData:
    stock_basic: pd.DataFrame
    price_exact: pd.DataFrame
    price_ffill: pd.DataFrame
    total_mv: pd.DataFrame
    daily_amount: pd.DataFrame
    financials_by_code: Dict[str, pd.DataFrame]
    month_end_dates: List[pd.Timestamp]
    monthly_period_end_dates: List[pd.Timestamp]
    month_start_dates: List[pd.Timestamp]
    week_end_dates: List[pd.Timestamp]
    code_to_name: Dict[str, str]
    code_to_list_date: Dict[str, pd.Timestamp]
    code_to_industry: Dict[str, str]
    market_monthly_close: pd.Series
    market_weekly_close: pd.Series
    core_members_by_date: Dict[pd.Timestamp, Set[str]]
    explore_members_by_date: Dict[pd.Timestamp, Set[str]]
    core_index_weights_by_date: Dict[pd.Timestamp, pd.Series]
    explore_index_weights_by_date: Dict[pd.Timestamp, pd.Series]
    data_warnings: List[str]
    monthly_factor_cache: MonthlyFactorCache | None = None


def normalize_codes(raw_codes: Iterable[str]) -> List[str]:
    normalized: List[str] = []
    errors: List[str] = []

    for raw in raw_codes:
        code = str(raw).strip()
        if not code.isdigit() or len(code) != 6:
            errors.append(f"{raw}: 不是 6 位数字代码")
            continue

        if code.startswith(("60", "68", "90", "50")):
            normalized.append(f"{code}.SH")
        elif code.startswith(("00", "30", "20")):
            normalized.append(f"{code}.SZ")
        else:
            errors.append(f"{raw}: 无法根据前缀判断交易所，请手动确认")

    if errors:
        raise ValueError("股票代码规范化失败：\n" + "\n".join(errors))

    return normalized


def ensure_directories() -> None:
    for path in [CACHE_DIR, DAILY_DIR, ADJ_DIR, DAILY_BASIC_DIR, FINA_DIR, INDEX_DIR, INDEX_WEIGHT_DIR, FACTOR_PANEL_DIR, PREPARED_PANEL_DIR, RESULTS_DIR]:
        path.mkdir(parents=True, exist_ok=True)
    ensure_results_layout()


def _is_dns_resolution_error(exc: Exception) -> bool:
    error_text = str(exc).lower()
    dns_markers = (
        "failed to resolve",
        "nameresolutionerror",
        "temporary failure in name resolution",
        "nodename nor servname provided",
        "name or service not known",
        "getaddrinfo failed",
        "eai_again",
    )
    return any(marker in error_text for marker in dns_markers)


def call_tushare_with_retry(api_callable, **kwargs) -> pd.DataFrame:
    if TUSHARE_OFFLINE_MODE:
        raise RuntimeError(f"Tushare 离线模式已启用，跳过在线请求: {kwargs}")
    last_error: Exception | None = None
    attempt = 1
    dns_attempt = 0
    while attempt <= MAX_RETRIES:
        try:
            df = api_callable(**kwargs)
            if df is None:
                raise RuntimeError("Tushare 返回了空对象")
            time.sleep(0.12)
            return df
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if _is_dns_resolution_error(exc):
                dns_attempt += 1
                if dns_attempt >= DNS_RETRY_ATTEMPTS:
                    break
                sleep_seconds = min(DNS_RETRY_MAX_DELAY, DNS_RETRY_BASE_DELAY * (2 ** (dns_attempt - 1)))
                print(
                    f"[Retry] Tushare DNS 解析失败，第 {dns_attempt}/{DNS_RETRY_ATTEMPTS} 次，"
                    f"{sleep_seconds:.1f} 秒后重试。参数: {kwargs}，错误: {exc}"
                )
                time.sleep(sleep_seconds)
                continue
            if attempt == MAX_RETRIES:
                break
            sleep_seconds = RETRY_BASE_DELAY * (2 ** (attempt - 1))
            print(
                f"[Retry] 调用 Tushare 失败，第 {attempt}/{MAX_RETRIES} 次，"
                f"{sleep_seconds:.1f} 秒后重试。参数: {kwargs}，错误: {exc}"
            )
            time.sleep(sleep_seconds)
            attempt += 1

    if last_error and _is_dns_resolution_error(last_error):
        raise RuntimeError(f"Tushare DNS 解析失败，已重试 {dns_attempt}/{DNS_RETRY_ATTEMPTS} 次: {kwargs}") from last_error
    raise RuntimeError(f"Tushare 请求失败，已重试 {MAX_RETRIES} 次: {kwargs}") from last_error


def read_cached_csv(path: Path, date_columns: Iterable[str] | None = None) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()
    for column in date_columns or []:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column])
    return df


def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, float_format=FLOAT_FORMAT)


def _latest_index_date(frame: pd.DataFrame) -> pd.Timestamp | None:
    if frame.empty:
        return None
    dates = pd.to_datetime(frame.index, errors="coerce")
    latest = dates.max()
    if pd.isna(latest):
        return None
    return pd.Timestamp(latest).normalize()


def prepared_cache_covers_target(prepared: PreparedData, cache_target_date: pd.Timestamp) -> bool:
    target = pd.Timestamp(cache_target_date).normalize()
    price_latest = _latest_index_date(prepared.price_exact)
    if price_latest is None or price_latest < target:
        print(
            f"[Cache] prepared panel cache stale: price_exact latest="
            f"{price_latest.date() if price_latest is not None else 'None'} < target={target.date()}"
        )
        return False
    mv_latest = _latest_index_date(prepared.total_mv)
    if mv_latest is None or mv_latest < target:
        print(
            f"[Cache] prepared panel cache stale: total_mv latest="
            f"{mv_latest.date() if mv_latest is not None else 'None'} < target={target.date()}"
        )
        return False
    return True


def load_or_fetch_stock_basic(pro) -> pd.DataFrame:
    cache_path = CACHE_DIR / "stock_basic.csv"
    cached = read_cached_csv(cache_path, date_columns=["list_date", "delist_date"])
    if not cached.empty:
        return cached

    frames = []
    for list_status in ["L", "D", "P"]:
        frame = call_tushare_with_retry(
            pro.stock_basic,
            exchange="",
            list_status=list_status,
            fields="ts_code,symbol,name,area,industry,market,list_date,delist_date,list_status",
        )
        frames.append(frame)

    stock_basic = pd.concat(frames, ignore_index=True).drop_duplicates(subset=["ts_code"])
    stock_basic["list_date"] = pd.to_datetime(stock_basic["list_date"], format="%Y%m%d", errors="coerce")
    stock_basic["delist_date"] = pd.to_datetime(stock_basic["delist_date"], format="%Y%m%d", errors="coerce")
    stock_basic = stock_basic.sort_values("ts_code").reset_index(drop=True)
    save_csv(stock_basic, cache_path)
    return stock_basic


def load_or_fetch_trade_calendar(pro, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = CACHE_DIR / "trade_calendar.csv"
    cached = read_cached_csv(cache_path, date_columns=["cal_date"])
    required_end_date = max(end_date.normalize(), (end_date + pd.offsets.MonthEnd(0)).normalize())

    if not cached.empty:
        cached = cached.sort_values("cal_date").drop_duplicates(subset=["cal_date"])
        cached_start = cached["cal_date"].min()
        cached_end = cached["cal_date"].max()
        if cached_start <= start_date and cached_end >= required_end_date:
            return cached[(cached["cal_date"] >= start_date) & (cached["cal_date"] <= required_end_date)].reset_index(drop=True)

    if not cached.empty and TUSHARE_OFFLINE_MODE:
        return cached[(cached["cal_date"] >= start_date) & (cached["cal_date"] <= required_end_date)].reset_index(drop=True)

    try:
        fetched = call_tushare_with_retry(
            pro.trade_cal,
            exchange="SSE",
            start_date=start_date.strftime("%Y%m%d"),
            end_date=required_end_date.strftime("%Y%m%d"),
            fields="exchange,cal_date,is_open,pretrade_date",
        )
    except RuntimeError:
        if not cached.empty:
            print("[Warn] trade_calendar 增量更新失败，回退使用本地缓存。")
            return cached[(cached["cal_date"] >= start_date) & (cached["cal_date"] <= required_end_date)].reset_index(drop=True)
        raise
    fetched["cal_date"] = pd.to_datetime(fetched["cal_date"], format="%Y%m%d", errors="coerce")
    calendar = fetched.sort_values("cal_date").drop_duplicates(subset=["cal_date"]).reset_index(drop=True)
    save_csv(calendar, cache_path)
    return calendar[(calendar["cal_date"] >= start_date) & (calendar["cal_date"] <= required_end_date)].reset_index(drop=True)


def build_pool_output_dir(pool_id: str, sample_tag: str | None = None) -> Path:
    return strategy_result_dir(pool_id, sample_tag, market_scope="a_share")


def load_or_fetch_daily(pro, ts_code: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = DAILY_DIR / f"{ts_code}.csv"
    cached = read_cached_csv(cache_path, date_columns=["trade_date"])
    if "trade_date" in cached.columns:
        cached = cached.sort_values("trade_date").drop_duplicates(subset=["trade_date"])
    else:
        cached = pd.DataFrame(columns=["ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol", "amount"])

    fetch_from = start_date
    if not cached.empty:
        latest_cached = cached["trade_date"].max()
        if latest_cached >= end_date:
            return cached.reset_index(drop=True)
        fetch_from = latest_cached + pd.Timedelta(days=1)

    if not cached.empty and TUSHARE_OFFLINE_MODE:
        return cached.reset_index(drop=True)

    try:
        fetched = call_tushare_with_retry(
            pro.daily,
            ts_code=ts_code,
            start_date=fetch_from.strftime("%Y%m%d"),
            end_date=end_date.strftime("%Y%m%d"),
        )
    except RuntimeError:
        if not cached.empty:
            print(f"[Warn] {ts_code} daily 增量更新失败，回退使用本地缓存。")
            return cached.reset_index(drop=True)
        raise

    if not fetched.empty:
        fetched["trade_date"] = pd.to_datetime(fetched["trade_date"], format="%Y%m%d", errors="coerce")

    daily = pd.concat([cached, fetched], ignore_index=True)
    if "trade_date" in daily.columns:
        daily["trade_date"] = pd.to_datetime(daily["trade_date"], errors="coerce")
    if "close" in daily.columns:
        daily["close"] = pd.to_numeric(daily["close"], errors="coerce")
    daily = daily.sort_values("trade_date").drop_duplicates(subset=["trade_date"]).reset_index(drop=True)
    save_csv(daily, cache_path)
    return daily


def load_or_fetch_adj_factor(pro, ts_code: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = ADJ_DIR / f"{ts_code}.csv"
    cached = read_cached_csv(cache_path, date_columns=["trade_date"])
    if "trade_date" in cached.columns:
        cached = cached.sort_values("trade_date").drop_duplicates(subset=["trade_date"])
    else:
        cached = pd.DataFrame(columns=["ts_code", "trade_date", "adj_factor"])

    fetch_from = start_date
    if not cached.empty:
        latest_cached = cached["trade_date"].max()
        if latest_cached >= end_date:
            return cached.reset_index(drop=True)
        fetch_from = latest_cached + pd.Timedelta(days=1)

    if not cached.empty and TUSHARE_OFFLINE_MODE:
        return cached.reset_index(drop=True)

    try:
        fetched = call_tushare_with_retry(
            pro.adj_factor,
            ts_code=ts_code,
            start_date=fetch_from.strftime("%Y%m%d"),
            end_date=end_date.strftime("%Y%m%d"),
        )
    except RuntimeError:
        if not cached.empty:
            print(f"[Warn] {ts_code} adj_factor 增量更新失败，回退使用本地缓存。")
            return cached.reset_index(drop=True)
        raise

    if not fetched.empty:
        fetched["trade_date"] = pd.to_datetime(fetched["trade_date"], format="%Y%m%d", errors="coerce")

    adj_factor = pd.concat([cached, fetched], ignore_index=True)
    if "trade_date" in adj_factor.columns:
        adj_factor["trade_date"] = pd.to_datetime(adj_factor["trade_date"], errors="coerce")
    if "adj_factor" in adj_factor.columns:
        adj_factor["adj_factor"] = pd.to_numeric(adj_factor["adj_factor"], errors="coerce")
    adj_factor = adj_factor.sort_values("trade_date").drop_duplicates(subset=["trade_date"]).reset_index(drop=True)
    save_csv(adj_factor, cache_path)
    return adj_factor


def load_or_fetch_daily_basic(pro, ts_code: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = DAILY_BASIC_DIR / f"{ts_code}.csv"
    cached = read_cached_csv(cache_path, date_columns=["trade_date"])
    if "trade_date" in cached.columns:
        cached = cached.sort_values("trade_date").drop_duplicates(subset=["trade_date"])
    else:
        cached = pd.DataFrame(columns=["ts_code", "trade_date", "total_mv"])

    fetch_from = start_date
    if not cached.empty:
        latest_cached = cached["trade_date"].max()
        if latest_cached >= end_date:
            return cached.reset_index(drop=True)
        fetch_from = latest_cached + pd.Timedelta(days=1)

    if not cached.empty and TUSHARE_OFFLINE_MODE:
        return cached.reset_index(drop=True)

    try:
        fetched = call_tushare_with_retry(
            pro.daily_basic,
            ts_code=ts_code,
            start_date=fetch_from.strftime("%Y%m%d"),
            end_date=end_date.strftime("%Y%m%d"),
            fields="ts_code,trade_date,total_mv",
        )
    except RuntimeError:
        if not cached.empty:
            print(f"[Warn] {ts_code} daily_basic 增量更新失败，回退使用本地缓存。")
            return cached.reset_index(drop=True)
        raise

    if not fetched.empty:
        fetched["trade_date"] = pd.to_datetime(fetched["trade_date"], format="%Y%m%d", errors="coerce")

    daily_basic = pd.concat([cached, fetched], ignore_index=True)
    if "trade_date" in daily_basic.columns:
        daily_basic["trade_date"] = pd.to_datetime(daily_basic["trade_date"], errors="coerce")
    if "total_mv" in daily_basic.columns:
        daily_basic["total_mv"] = pd.to_numeric(daily_basic["total_mv"], errors="coerce")
    daily_basic = daily_basic.sort_values("trade_date").drop_duplicates(subset=["trade_date"]).reset_index(drop=True)
    save_csv(daily_basic, cache_path)
    return daily_basic


def get_cache_worker_tushare_client(default_pro):
    if TUSHARE_OFFLINE_MODE or not TOKEN:
        return default_pro
    client = getattr(_CACHE_WORKER_STATE, "pro", None)
    if client is None:
        client = ts.pro_api(TOKEN)
        _CACHE_WORKER_STATE.pro = client
    return client


def prepare_single_stock_cache_data(
    default_pro,
    ts_code: str,
    data_start_date: pd.Timestamp,
    end_date: pd.Timestamp,
) -> Tuple[str, Dict[str, pd.DataFrame], pd.DataFrame]:
    worker_pro = get_cache_worker_tushare_client(default_pro)
    daily = load_or_fetch_daily(worker_pro, ts_code, data_start_date, end_date)
    adj_factor = load_or_fetch_adj_factor(worker_pro, ts_code, data_start_date, end_date)
    daily_basic = load_or_fetch_daily_basic(worker_pro, ts_code, data_start_date, end_date)
    fina_indicator = load_or_fetch_fina_indicator(worker_pro, ts_code, data_start_date - pd.DateOffset(years=2), end_date)
    price = build_forward_adjusted_prices(daily, adj_factor)
    return (
        ts_code,
        {
            "daily": daily,
            "adj_factor": adj_factor,
            "daily_basic": daily_basic,
            "price": price,
        },
        fina_indicator,
    )


def load_or_fetch_fina_indicator(pro, ts_code: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = FINA_DIR / f"{ts_code}.csv"
    cached = read_cached_csv(cache_path, date_columns=["ann_date", "end_date"])
    if "ann_date" not in cached.columns:
        cached = pd.DataFrame(
            columns=[
                "ts_code",
                "ann_date",
                "end_date",
                "roe",
                "grossprofit_margin",
                "debt_to_assets",
                "ocf_to_or",
                "q_dtprofit_yoy",
            ]
        )

    if cached.empty:
        if not cached.empty and TUSHARE_OFFLINE_MODE:
            return cached.reset_index(drop=True)
        try:
            fetched = call_tushare_with_retry(
                pro.fina_indicator,
                ts_code=ts_code,
                start_date=start_date.strftime("%Y%m%d"),
                end_date=end_date.strftime("%Y%m%d"),
                fields="ts_code,ann_date,end_date,roe,grossprofit_margin,debt_to_assets,ocf_to_or,q_dtprofit_yoy",
            )
        except RuntimeError:
            if not cached.empty:
                print(f"[Warn] {ts_code} fina_indicator 增量更新失败，回退使用本地缓存。")
                return cached.reset_index(drop=True)
            raise
        if not fetched.empty:
            fetched["ann_date"] = pd.to_datetime(fetched["ann_date"], format="%Y%m%d", errors="coerce")
            fetched["end_date"] = pd.to_datetime(fetched["end_date"], format="%Y%m%d", errors="coerce")
        fina = fetched
        for column in ["roe", "grossprofit_margin", "debt_to_assets", "ocf_to_or", "q_dtprofit_yoy"]:
            if column in fina.columns:
                fina[column] = pd.to_numeric(fina[column], errors="coerce")
        fina = fina.sort_values(["ann_date", "end_date"]).drop_duplicates(subset=["ann_date", "end_date"], keep="last").reset_index(drop=True)
        save_csv(fina, cache_path)
        return fina

    cached["ann_date"] = pd.to_datetime(cached["ann_date"], errors="coerce")
    cached["end_date"] = pd.to_datetime(cached["end_date"], errors="coerce")
    for column in ["roe", "grossprofit_margin", "debt_to_assets", "ocf_to_or", "q_dtprofit_yoy"]:
        if column in cached.columns:
            cached[column] = pd.to_numeric(cached[column], errors="coerce")
    cached = cached.sort_values(["ann_date", "end_date"]).drop_duplicates(subset=["ann_date", "end_date"], keep="last").reset_index(drop=True)
    save_csv(cached, cache_path)
    return cached


def load_or_fetch_index_daily(pro, ts_code: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = INDEX_DIR / f"{ts_code}.csv"
    cached = read_cached_csv(cache_path, date_columns=["trade_date"])
    if "trade_date" in cached.columns:
        cached = cached.sort_values("trade_date").drop_duplicates(subset=["trade_date"])
    else:
        cached = pd.DataFrame(columns=["ts_code", "trade_date", "close"])

    fetch_from = start_date
    if not cached.empty:
        latest_cached = cached["trade_date"].max()
        if latest_cached >= end_date:
            return cached.reset_index(drop=True)
        fetch_from = latest_cached + pd.Timedelta(days=1)

    if not cached.empty and TUSHARE_OFFLINE_MODE:
        return cached.reset_index(drop=True)

    try:
        fetched = call_tushare_with_retry(
            pro.index_daily,
            ts_code=ts_code,
            start_date=fetch_from.strftime("%Y%m%d"),
            end_date=end_date.strftime("%Y%m%d"),
        )
    except RuntimeError:
        if not cached.empty:
            print(f"[Warn] {ts_code} index_daily 增量更新失败，回退使用本地缓存。")
            return cached.reset_index(drop=True)
        raise
    if not fetched.empty:
        fetched["trade_date"] = pd.to_datetime(fetched["trade_date"], format="%Y%m%d", errors="coerce")
        if "close" in fetched.columns:
            fetched["close"] = pd.to_numeric(fetched["close"], errors="coerce")

    index_df = pd.concat([cached, fetched], ignore_index=True)
    if "trade_date" in index_df.columns:
        index_df["trade_date"] = pd.to_datetime(index_df["trade_date"], errors="coerce")
    if "close" in index_df.columns:
        index_df["close"] = pd.to_numeric(index_df["close"], errors="coerce")
    index_df = index_df.sort_values("trade_date").drop_duplicates(subset=["trade_date"]).reset_index(drop=True)
    save_csv(index_df, cache_path)
    return index_df


def load_or_fetch_index_weight(pro, index_code: str, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    cache_path = INDEX_WEIGHT_DIR / f"{index_code}.csv"
    cached = read_cached_csv(cache_path, date_columns=["trade_date"])
    required_end_date = end_date if end_date.is_month_end else (end_date - pd.offsets.MonthEnd(1))

    if not cached.empty and "trade_date" in cached.columns:
        cached = cached.sort_values(["trade_date", "con_code"]).drop_duplicates(subset=["trade_date", "con_code"])
        cached_max = pd.to_datetime(cached["trade_date"]).max()
        # 指数成分权重通常按月更新；若缓存已经覆盖到目标结束月份，就直接复用。
        # 对于晚于回测起点才成立的指数（如科创50/100/200），也不强制补抓其成立前不存在的数据。
        if cached_max.to_period("M") >= required_end_date.to_period("M"):
            return cached.reset_index(drop=True)

    frames: List[pd.DataFrame] = []
    cursor = pd.Timestamp(start_date.year, 1, 1)
    if not cached.empty and "trade_date" in cached.columns:
        cached_max = pd.to_datetime(cached["trade_date"]).max()
        cursor = max(cursor, (cached_max + pd.Timedelta(days=1)).normalize())
    while cursor <= required_end_date:
        chunk_end = min(pd.Timestamp(cursor.year, 12, 31), required_end_date)
        if not cached.empty and TUSHARE_OFFLINE_MODE:
            return cached.reset_index(drop=True)
        try:
            fetched = call_tushare_with_retry(
                pro.index_weight,
                index_code=index_code,
                start_date=cursor.strftime("%Y%m%d"),
                end_date=chunk_end.strftime("%Y%m%d"),
            )
        except RuntimeError:
            if not cached.empty:
                print(f"[Warn] {index_code} index_weight 增量更新失败，回退使用本地缓存。")
                return cached.reset_index(drop=True)
            raise
        if not fetched.empty:
            fetched["trade_date"] = pd.to_datetime(fetched["trade_date"], format="%Y%m%d", errors="coerce")
            frames.append(fetched)
        cursor = chunk_end + pd.Timedelta(days=1)

    if frames or not cached.empty:
        index_weight = pd.concat([cached] + frames, ignore_index=True)
        if "weight" in index_weight.columns:
            index_weight["weight"] = pd.to_numeric(index_weight["weight"], errors="coerce")
        index_weight = (
            index_weight.sort_values(["trade_date", "con_code"])
            .drop_duplicates(subset=["trade_date", "con_code"], keep="last")
            .reset_index(drop=True)
        )
    else:
        index_weight = pd.DataFrame(columns=["index_code", "con_code", "trade_date", "weight"])

    save_csv(index_weight, cache_path)
    return index_weight


def build_month_boundaries(
    calendar: pd.DataFrame,
    formal_calendar: pd.DataFrame | None = None,
) -> Tuple[List[pd.Timestamp], List[pd.Timestamp], List[pd.Timestamp], pd.Index, List[pd.Timestamp]]:
    open_calendar = calendar.loc[calendar["is_open"] == 1, ["cal_date"]].copy()
    open_calendar = open_calendar.sort_values("cal_date").reset_index(drop=True)
    open_calendar["month"] = open_calendar["cal_date"].dt.to_period("M")
    open_calendar["week"] = open_calendar["cal_date"].dt.to_period("W-FRI")
    latest_usable_date = pd.Timestamp(open_calendar["cal_date"].max()) if not open_calendar.empty else None
    if formal_calendar is not None and latest_usable_date is not None:
        formal_open_calendar = formal_calendar.loc[formal_calendar["is_open"] == 1, ["cal_date"]].copy()
        formal_open_calendar = formal_open_calendar.sort_values("cal_date").reset_index(drop=True)
        formal_open_calendar["month"] = formal_open_calendar["cal_date"].dt.to_period("M")
        formal_calendar_end = pd.Timestamp(formal_open_calendar["cal_date"].max()).normalize()
        formal_month_end_table = formal_open_calendar.groupby("month")["cal_date"].max().sort_index()
        month_end_dates = []
        for month, date in formal_month_end_table.items():
            calendar_month_end = pd.Period(month, freq="M").to_timestamp(how="end").normalize()
            if calendar_month_end <= formal_calendar_end and pd.Timestamp(date) <= latest_usable_date:
                month_end_dates.append(pd.Timestamp(date))
    else:
        month_end_dates = open_calendar.groupby("month")["cal_date"].max().sort_values().tolist()
    monthly_period_end_dates = list(month_end_dates)
    if latest_usable_date is not None and (
        not monthly_period_end_dates or latest_usable_date > monthly_period_end_dates[-1]
    ):
        monthly_period_end_dates.append(latest_usable_date)
    month_start_dates = open_calendar.groupby("month")["cal_date"].min().sort_values().tolist()
    week_end_dates = open_calendar.groupby("week")["cal_date"].max().sort_values().tolist()
    full_calendar_index = pd.Index(open_calendar["cal_date"], name="trade_date")
    return month_end_dates, month_start_dates, week_end_dates, full_calendar_index, monthly_period_end_dates


def build_index_memberships_for_dates(index_weight_df: pd.DataFrame, signal_dates: List[pd.Timestamp]) -> Dict[pd.Timestamp, Set[str]]:
    memberships: Dict[pd.Timestamp, Set[str]] = {}
    if index_weight_df.empty:
        return {signal_date: set() for signal_date in signal_dates}

    grouped = [
        (pd.Timestamp(trade_date), set(group["con_code"].astype(str)))
        for trade_date, group in index_weight_df.groupby("trade_date")
    ]
    grouped.sort(key=lambda item: item[0])

    pointer = -1
    current_members: Set[str] = set()
    for signal_date in sorted(signal_dates):
        while pointer + 1 < len(grouped) and grouped[pointer + 1][0] <= signal_date:
            pointer += 1
            current_members = grouped[pointer][1]
        memberships[signal_date] = set(current_members)

    return memberships


def build_index_weight_lookup_for_dates(index_weight_df: pd.DataFrame, signal_dates: List[pd.Timestamp]) -> Dict[pd.Timestamp, pd.Series]:
    weights_by_date: Dict[pd.Timestamp, pd.Series] = {}
    if index_weight_df.empty:
        return {signal_date: pd.Series(dtype=float) for signal_date in signal_dates}

    grouped = []
    for trade_date, group in index_weight_df.groupby("trade_date"):
        series = group.set_index("con_code")["weight"].astype(float)
        grouped.append((pd.Timestamp(trade_date), series))
    grouped.sort(key=lambda item: item[0])

    pointer = -1
    current_weights = pd.Series(dtype=float)
    for signal_date in sorted(signal_dates):
        while pointer + 1 < len(grouped) and grouped[pointer + 1][0] <= signal_date:
            pointer += 1
            current_weights = grouped[pointer][1]
        weights_by_date[signal_date] = current_weights.copy()

    return weights_by_date


def combine_index_weight_series(series_list: List[pd.Series], exclude_codes: Set[str] | None = None) -> pd.Series:
    valid_series = [series.astype(float) for series in series_list if series is not None and not series.empty]
    if not valid_series:
        return pd.Series(dtype=float)

    combined = pd.concat(valid_series).groupby(level=0).sum()
    if exclude_codes:
        combined = combined.drop(labels=list(exclude_codes & set(combined.index)), errors="ignore")
    combined = combined[combined > 0]
    total = float(combined.sum())
    if total <= 0:
        return pd.Series(dtype=float)
    return (combined / total).sort_values(ascending=False)


def build_dynamic_pool_maps(
    index_weights_by_code: Dict[str, pd.DataFrame],
    signal_dates: List[pd.Timestamp],
) -> Tuple[Dict[pd.Timestamp, Set[str]], Dict[pd.Timestamp, Set[str]], Dict[pd.Timestamp, pd.Series], Dict[pd.Timestamp, pd.Series], Set[str]]:
    members_by_index = {
        index_code: build_index_memberships_for_dates(index_weight_df, signal_dates)
        for index_code, index_weight_df in index_weights_by_code.items()
    }
    weights_by_index = {
        index_code: build_index_weight_lookup_for_dates(index_weight_df, signal_dates)
        for index_code, index_weight_df in index_weights_by_code.items()
    }

    core_members_by_date: Dict[pd.Timestamp, Set[str]] = {}
    explore_members_by_date: Dict[pd.Timestamp, Set[str]] = {}
    core_index_weights_by_date: Dict[pd.Timestamp, pd.Series] = {}
    explore_index_weights_by_date: Dict[pd.Timestamp, pd.Series] = {}
    all_codes: Set[str] = set()

    for signal_date in signal_dates:
        core_weight_series = combine_index_weight_series(
            [weights_by_index.get(index_code, {}).get(signal_date, pd.Series(dtype=float)) for index_code in CORE_INDEX_CODES]
        )
        core_members = set(core_weight_series.index)
        explore_weight_series = combine_index_weight_series(
            [weights_by_index.get(index_code, {}).get(signal_date, pd.Series(dtype=float)) for index_code in EXPLORE_INDEX_CODES],
            exclude_codes=core_members,
        )
        explore_members = set(explore_weight_series.index)
        # 若某只股票同时出现在核心和探索指数中，则优先归入核心池，避免双重计权。

        core_members_by_date[signal_date] = core_members
        explore_members_by_date[signal_date] = explore_members
        core_index_weights_by_date[signal_date] = core_weight_series
        explore_index_weights_by_date[signal_date] = explore_weight_series
        all_codes.update(core_members)
        all_codes.update(explore_members)

    return core_members_by_date, explore_members_by_date, core_index_weights_by_date, explore_index_weights_by_date, all_codes


def build_forward_adjusted_prices(daily_df: pd.DataFrame, adj_factor_df: pd.DataFrame) -> pd.DataFrame:
    if daily_df.empty or adj_factor_df.empty:
        return pd.DataFrame(columns=["trade_date", "close", "adj_factor", "forward_adj_close"])

    merged = daily_df[["trade_date", "close"]].merge(
        adj_factor_df[["trade_date", "adj_factor"]],
        on="trade_date",
        how="inner",
    )
    merged = merged.sort_values("trade_date").reset_index(drop=True)
    latest_adj_factor = merged["adj_factor"].iloc[-1]

    # 使用“close * 当日复权因子 / 最新复权因子”的方式构造前复权价格，
    # 使得最新一个交易日的价格与原始收盘价一致。
    merged["forward_adj_close"] = merged["close"] * merged["adj_factor"] / latest_adj_factor
    return merged


def build_monthly_panel(
    normalized_codes: List[str],
    stock_basic: pd.DataFrame,
    calendar: pd.DataFrame,
    formal_calendar: pd.DataFrame | None,
    per_stock_frames: Dict[str, Dict[str, pd.DataFrame]],
    financials_by_code: Dict[str, pd.DataFrame],
    market_index_df: pd.DataFrame,
    core_members_by_date: Dict[pd.Timestamp, Set[str]],
    explore_members_by_date: Dict[pd.Timestamp, Set[str]],
    core_index_weights_by_date: Dict[pd.Timestamp, pd.Series],
    explore_index_weights_by_date: Dict[pd.Timestamp, pd.Series],
    data_warnings: List[str],
) -> PreparedData:
    (
        month_end_dates,
        month_start_dates,
        week_end_dates,
        full_calendar_index,
        monthly_period_end_dates,
    ) = build_month_boundaries(calendar, formal_calendar=formal_calendar)

    price_frames = []
    mv_frames = []
    amount_frames = []
    for ts_code in normalized_codes:
        merged_price = per_stock_frames[ts_code]["price"].copy()
        if not merged_price.empty:
            merged_price["ts_code"] = ts_code
            price_frames.append(merged_price[["trade_date", "ts_code", "forward_adj_close"]])

        merged_mv = per_stock_frames[ts_code]["daily_basic"].copy()
        if not merged_mv.empty:
            merged_mv["ts_code"] = ts_code
            mv_frames.append(merged_mv[["trade_date", "ts_code", "total_mv"]])

        merged_daily = per_stock_frames[ts_code]["daily"].copy()
        if not merged_daily.empty and "amount" in merged_daily.columns:
            merged_daily["ts_code"] = ts_code
            amount_frames.append(merged_daily[["trade_date", "ts_code", "amount"]])

    if not price_frames:
        raise RuntimeError("没有成功构造任何股票的前复权价格序列。")

    price_exact = pd.concat(price_frames, ignore_index=True).pivot(
        index="trade_date",
        columns="ts_code",
        values="forward_adj_close",
    )
    price_exact = price_exact.sort_index()

    price_ffill = price_exact.reindex(full_calendar_index).ffill()

    if mv_frames:
        total_mv = pd.concat(mv_frames, ignore_index=True).pivot(
            index="trade_date",
            columns="ts_code",
            values="total_mv",
        )
        total_mv = total_mv.sort_index()
    else:
        total_mv = pd.DataFrame(index=price_exact.index)

    if amount_frames:
        daily_amount = pd.concat(amount_frames, ignore_index=True).pivot(
            index="trade_date",
            columns="ts_code",
            values="amount",
        )
        daily_amount = daily_amount.sort_index().reindex(full_calendar_index)
    else:
        daily_amount = pd.DataFrame(index=full_calendar_index)

    selected_basic = stock_basic.loc[stock_basic["ts_code"].isin(normalized_codes)].copy()
    selected_basic["industry"] = selected_basic["industry"].fillna("").replace("", "未知行业")
    code_to_name = dict(zip(selected_basic["ts_code"], selected_basic["name"]))
    code_to_list_date = dict(zip(selected_basic["ts_code"], selected_basic["list_date"]))
    code_to_industry = dict(zip(selected_basic["ts_code"], selected_basic["industry"]))
    market_monthly_table = (
        market_index_df[["trade_date", "close"]]
        .dropna()
        .sort_values("trade_date")
        .assign(month=lambda df: df["trade_date"].dt.to_period("M"))
        .groupby("month")
        .tail(1)
        .set_index("trade_date")["close"]
    )
    market_monthly_close = market_monthly_table.reindex(pd.Index(month_end_dates)).ffill()
    market_weekly_table = (
        market_index_df[["trade_date", "close"]]
        .dropna()
        .sort_values("trade_date")
        .assign(week=lambda df: df["trade_date"].dt.to_period("W-FRI"))
        .groupby("week")
        .tail(1)
        .set_index("trade_date")["close"]
    )
    market_weekly_close = market_weekly_table.reindex(pd.Index(week_end_dates)).ffill()

    return PreparedData(
        stock_basic=selected_basic,
        price_exact=price_exact,
        price_ffill=price_ffill,
        total_mv=total_mv,
        daily_amount=daily_amount,
        financials_by_code=financials_by_code,
        month_end_dates=month_end_dates,
        monthly_period_end_dates=monthly_period_end_dates,
        month_start_dates=month_start_dates,
        week_end_dates=week_end_dates,
        code_to_name=code_to_name,
        code_to_list_date=code_to_list_date,
        code_to_industry=code_to_industry,
        market_monthly_close=market_monthly_close,
        market_weekly_close=market_weekly_close,
        core_members_by_date=core_members_by_date,
        explore_members_by_date=explore_members_by_date,
        core_index_weights_by_date=core_index_weights_by_date,
        explore_index_weights_by_date=explore_index_weights_by_date,
        data_warnings=data_warnings,
    )


def get_stamp_duty_rate(trade_date: pd.Timestamp) -> float:
    # 印花税仅对卖出成交额征收，且 2023-08-28 起税率由 0.10% 下调至 0.05%。
    if trade_date < STAMP_DUTY_CHANGE_DATE:
        return STAMP_DUTY_PRE_20230828
    return STAMP_DUTY_POST_20230828


def safe_percentile_rank(series: pd.Series, ascending: bool) -> pd.Series:
    if series.empty:
        return pd.Series(dtype=float)
    ranks = series.rank(method="average", ascending=ascending, pct=True)
    return ranks.fillna(0.5)


def normalize_positive_weights(series: pd.Series) -> pd.Series:
    cleaned = series.astype(float).replace([np.inf, -np.inf], np.nan).fillna(0.0).clip(lower=0.0)
    total = float(cleaned.sum())
    if total <= 0:
        if cleaned.empty:
            return cleaned
        return pd.Series(1.0 / len(cleaned), index=cleaned.index)
    return cleaned / total


def blend_ranked_components(components: List[Tuple[pd.Series, float]]) -> pd.Series:
    valid_components = [(series.astype(float), weight) for series, weight in components if weight > 0 and not series.empty]
    if not valid_components:
        return pd.Series(dtype=float)

    union_index = pd.Index([])
    for series, _weight in valid_components:
        union_index = union_index.union(series.index)

    weighted_sum = pd.Series(0.0, index=union_index, dtype=float)
    available_weight = pd.Series(0.0, index=union_index, dtype=float)
    for series, weight in valid_components:
        aligned = series.reindex(union_index)
        mask = aligned.notna()
        weighted_sum.loc[mask] = weighted_sum.loc[mask] + aligned.loc[mask] * weight
        available_weight.loc[mask] = available_weight.loc[mask] + weight

    blended = weighted_sum / available_weight.replace(0.0, np.nan)
    return blended.dropna().sort_values(ascending=False)


def _validated_multi_factor_weights(weights: object) -> Dict[str, float]:
    """Sanitise ``factor_weights`` for the ``multi_factor`` core-signal mode.

    Filters to known keys, drops non-finite or negative entries, and falls
    back to ``DEFAULT_MULTI_FACTOR_WEIGHTS`` when the input is missing,
    malformed, or sums to zero. Without this guard a misconfigured automation
    preset could silently produce an all-zero/all-NaN core score, which
    ``blend_ranked_components`` would happily return as an empty series and
    push every candidate into the same untied bucket.
    """
    if not isinstance(weights, dict):
        return dict(DEFAULT_MULTI_FACTOR_WEIGHTS)
    cleaned: Dict[str, float] = {}
    total = 0.0
    for key, value in weights.items():
        key_str = str(key)
        if key_str not in VALID_MULTI_FACTOR_KEYS:
            continue
        try:
            weight = float(value)
        except (TypeError, ValueError):
            continue
        if not np.isfinite(weight) or weight < 0.0:
            continue
        cleaned[key_str] = weight
        total += weight
    if total <= 0.0:
        return dict(DEFAULT_MULTI_FACTOR_WEIGHTS)
    return cleaned


def build_weekly_alpha_scores(
    signal_mode: str,
    momentum_6_1: pd.Series,
    momentum_3_1: pd.Series,
    recent_1m_returns: pd.Series,
    amount_surge_ratio: pd.Series,
    breakout_signal: pd.Series,
    quality_scores: pd.Series,
    industry_strength_scores: pd.Series,
    industry_leader_scores: pd.Series,
) -> pd.Series:
    mode = str(signal_mode or "").strip().lower()
    if mode not in WEEKLY_ALPHA_SIGNAL_MODES:
        return pd.Series(dtype=float)

    if mode == "weekly_alpha_breakout":
        return blend_ranked_components(
            [
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.22),
                (safe_percentile_rank(recent_1m_returns, ascending=True), 0.20),
                (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.20),
                (breakout_signal.astype(float), 0.18),
                (industry_strength_scores, 0.12),
                (industry_leader_scores, 0.08),
            ]
        )
    if mode == "weekly_alpha_pullback":
        return blend_ranked_components(
            [
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.28),
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.18),
                (industry_strength_scores, 0.18),
                (industry_leader_scores, 0.12),
                (quality_scores, 0.12),
                (safe_percentile_rank(recent_1m_returns, ascending=False), 0.12),
            ]
        )
    return blend_ranked_components(
        [
            (safe_percentile_rank(momentum_6_1, ascending=True), 0.20),
            (safe_percentile_rank(momentum_3_1, ascending=True), 0.20),
            (safe_percentile_rank(recent_1m_returns, ascending=True), 0.15),
            (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.15),
            (industry_strength_scores, 0.12),
            (industry_leader_scores, 0.10),
            (quality_scores, 0.08),
        ]
    )


def build_emergent_theme_scores(
    *,
    momentum_6_1: pd.Series,
    momentum_3_1: pd.Series,
    recent_1m_returns: pd.Series,
    amount_surge_ratio: pd.Series,
    breakout_signal: pd.Series,
    industry_strength_scores: pd.Series,
    industry_leader_scores: pd.Series,
) -> pd.Series:
    return blend_ranked_components(
        [
            (industry_strength_scores, 0.32),
            (industry_leader_scores, 0.24),
            (safe_percentile_rank(momentum_3_1, ascending=True), 0.16),
            (safe_percentile_rank(recent_1m_returns, ascending=True), 0.12),
            (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.10),
            (breakout_signal.astype(float), 0.06),
        ]
    )


def compute_core_signal_scores(
    *,
    core_signal_mode: str,
    cached_default: pd.Series,
    strategy_config: Dict[str, object],
    momentum_6_1: pd.Series,
    momentum_3_1: pd.Series,
    recent_1m_returns: pd.Series,
    amount_surge_ratio: pd.Series,
    breakout_signal: pd.Series,
    quality_scores: pd.Series,
    growth_acceleration_scores: pd.Series,
    industry_strength_scores: pd.Series,
    industry_leader_scores: pd.Series,
) -> pd.Series:
    """Resolve the per-date core signal scores from the configured signal mode.

    Centralises the dispatch so the live ``run_backtest`` path and the
    diagnostic ``build_month_end_preview_payload`` path share one source
    of truth. When the mode is unset or unrecognised the function returns
    the cached default unchanged, preserving prior behaviour for variants
    that rely on the precomputed factor cache.
    """
    mode = str(core_signal_mode or "").strip()
    if mode == "6_1":
        return momentum_6_1.copy()
    if mode == "3_1":
        return momentum_3_1.copy()
    if mode == "theme":
        return blend_ranked_components(
            [
                (growth_acceleration_scores, 0.30),
                (industry_strength_scores, 0.25),
                (industry_leader_scores, 0.20),
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.15),
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.10),
            ]
        )
    if mode == "industry_trend":
        return blend_ranked_components(
            [
                (industry_strength_scores, 0.30),
                (industry_leader_scores, 0.25),
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.25),
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.15),
                (breakout_signal.astype(float), 0.05),
            ]
        )
    if mode == "midcycle_momentum":
        return blend_ranked_components(
            [
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.40),
                (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.20),
                (safe_percentile_rank(recent_1m_returns, ascending=True), 0.15),
                (industry_leader_scores, 0.15),
                (breakout_signal.astype(float), 0.10),
            ]
        )
    if mode == EMERGENT_THEME_SIGNAL_MODE:
        return build_emergent_theme_scores(
            momentum_6_1=momentum_6_1,
            momentum_3_1=momentum_3_1,
            recent_1m_returns=recent_1m_returns,
            amount_surge_ratio=amount_surge_ratio,
            breakout_signal=breakout_signal,
            industry_strength_scores=industry_strength_scores,
            industry_leader_scores=industry_leader_scores,
        )
    if mode == "multi_factor":
        factor_weights = _validated_multi_factor_weights(strategy_config.get("factor_weights"))
        return blend_ranked_components(
            [
                (safe_percentile_rank(momentum_6_1, ascending=True),       factor_weights.get("momentum_6_1", 0.0)),
                (safe_percentile_rank(momentum_3_1, ascending=True),       factor_weights.get("momentum_3_1", 0.0)),
                (quality_scores,                                            factor_weights.get("quality", 0.0)),
                (growth_acceleration_scores,                                factor_weights.get("growth_acceleration", 0.0)),
                (industry_strength_scores,                                  factor_weights.get("industry_strength", 0.0)),
                (industry_leader_scores,                                    factor_weights.get("industry_leader", 0.0)),
                (safe_percentile_rank(amount_surge_ratio, ascending=True), factor_weights.get("liquidity_surge", 0.0)),
            ]
        )
    if mode in WEEKLY_ALPHA_SIGNAL_MODES:
        return build_weekly_alpha_scores(
            mode,
            momentum_6_1=momentum_6_1,
            momentum_3_1=momentum_3_1,
            recent_1m_returns=recent_1m_returns,
            amount_surge_ratio=amount_surge_ratio,
            breakout_signal=breakout_signal,
            quality_scores=quality_scores,
            industry_strength_scores=industry_strength_scores,
            industry_leader_scores=industry_leader_scores,
        )
    return cached_default


def get_latest_financial_snapshot(financials_df: pd.DataFrame, signal_date: pd.Timestamp) -> pd.Series:
    if financials_df.empty:
        return pd.Series(dtype=float)
    available = financials_df.loc[financials_df["ann_date"] <= signal_date].copy()
    if available.empty:
        return pd.Series(dtype=float)
    latest = available.sort_values(["ann_date", "end_date"]).iloc[-1]
    return latest


def compute_quality_scores(prepared: PreparedData, eligible_codes: List[str], signal_date: pd.Timestamp) -> Tuple[pd.Series, pd.DataFrame]:
    snapshots: List[Dict[str, float | str]] = []
    for ts_code in eligible_codes:
        snapshot = get_latest_financial_snapshot(prepared.financials_by_code.get(ts_code, pd.DataFrame()), signal_date)
        if snapshot.empty:
            continue
        snapshots.append(
            {
                "ts_code": ts_code,
                "roe": snapshot.get("roe", np.nan),
                "grossprofit_margin": snapshot.get("grossprofit_margin", np.nan),
                "debt_to_assets": snapshot.get("debt_to_assets", np.nan),
                "ocf_to_or": snapshot.get("ocf_to_or", np.nan),
                "q_dtprofit_yoy": snapshot.get("q_dtprofit_yoy", np.nan),
            }
        )

    if not snapshots:
        return pd.Series(dtype=float), pd.DataFrame()

    quality_df = pd.DataFrame(snapshots).set_index("ts_code")
    quality_score = (
        safe_percentile_rank(quality_df["roe"], ascending=True)
        + safe_percentile_rank(quality_df["grossprofit_margin"], ascending=True)
        + safe_percentile_rank(quality_df["ocf_to_or"], ascending=True)
        + safe_percentile_rank(quality_df["q_dtprofit_yoy"], ascending=True)
        + safe_percentile_rank(quality_df["debt_to_assets"], ascending=False)
    ) / 5.0
    quality_df["quality_score"] = quality_score
    return quality_score, quality_df


def compute_growth_quality_scores(quality_df: pd.DataFrame) -> pd.Series:
    if quality_df.empty:
        return pd.Series(dtype=float)
    return blend_ranked_components(
        [
            (safe_percentile_rank(quality_df["q_dtprofit_yoy"], ascending=True), 0.35),
            (safe_percentile_rank(quality_df["roe"], ascending=True), 0.20),
            (safe_percentile_rank(quality_df["grossprofit_margin"], ascending=True), 0.15),
            (safe_percentile_rank(quality_df["ocf_to_or"], ascending=True), 0.15),
            (safe_percentile_rank(quality_df["debt_to_assets"], ascending=False), 0.15),
        ]
    )


def compute_growth_acceleration_scores(quality_df: pd.DataFrame) -> pd.Series:
    if quality_df.empty:
        return pd.Series(dtype=float)
    return blend_ranked_components(
        [
            (safe_percentile_rank(quality_df["q_dtprofit_yoy"], ascending=True), 0.55),
            (safe_percentile_rank(quality_df["roe"], ascending=True), 0.15),
            (safe_percentile_rank(quality_df["grossprofit_margin"], ascending=True), 0.10),
            (safe_percentile_rank(quality_df["ocf_to_or"], ascending=True), 0.10),
            (safe_percentile_rank(quality_df["debt_to_assets"], ascending=False), 0.10),
        ]
    )


def compute_industry_relative_strength_scores(
    code_to_industry: Dict[str, str],
    candidate_codes: Iterable[str],
    momentum_6_1: pd.Series,
    momentum_3_1: pd.Series,
    amount_surge_ratio: pd.Series,
    breakout_signal: pd.Series,
    growth_acceleration_scores: pd.Series,
) -> Tuple[pd.Series, pd.Series]:
    candidate_index = pd.Index(sorted(set(candidate_codes)))
    if candidate_index.empty:
        return pd.Series(dtype=float), pd.Series(dtype=float)

    industry_labels = pd.Series(
        {code: code_to_industry.get(code, "未知行业") or "未知行业" for code in candidate_index},
        dtype="object",
    )
    industry_momentum_6: Dict[str, float] = {}
    industry_momentum_3: Dict[str, float] = {}
    industry_breakout_breadth: Dict[str, float] = {}
    industry_growth: Dict[str, float] = {}
    industry_leader_scores = pd.Series(index=candidate_index, dtype=float)
    for industry_name, member_codes in industry_labels.groupby(industry_labels).groups.items():
        member_index = pd.Index(list(member_codes))
        member_mom_6 = momentum_6_1.reindex(member_index).dropna()
        member_mom_3 = momentum_3_1.reindex(member_index).dropna()
        member_breakout = breakout_signal.reindex(member_index).fillna(False).astype(float)
        member_growth = growth_acceleration_scores.reindex(member_index).dropna()
        if member_mom_6.empty and member_mom_3.empty and member_growth.empty:
            continue
        industry_momentum_6[str(industry_name)] = float(member_mom_6.mean()) if not member_mom_6.empty else np.nan
        industry_momentum_3[str(industry_name)] = float(member_mom_3.mean()) if not member_mom_3.empty else np.nan
        industry_breakout_breadth[str(industry_name)] = float(member_breakout.mean()) if not member_breakout.empty else 0.0
        industry_growth[str(industry_name)] = float(member_growth.median()) if not member_growth.empty else np.nan
        leader_composite = blend_ranked_components(
            [
                (safe_percentile_rank(momentum_6_1.reindex(member_index), ascending=True), 0.35),
                (safe_percentile_rank(momentum_3_1.reindex(member_index), ascending=True), 0.25),
                (growth_acceleration_scores.reindex(member_index), 0.20),
                (safe_percentile_rank(amount_surge_ratio.reindex(member_index), ascending=True), 0.10),
                (breakout_signal.reindex(member_index).fillna(False).astype(float), 0.10),
            ]
        )
        if not leader_composite.empty:
            industry_leader_scores.loc[leader_composite.index] = safe_percentile_rank(leader_composite, ascending=True)

    industry_strength_rank = blend_ranked_components(
        [
            (safe_percentile_rank(pd.Series(industry_momentum_6, dtype=float), ascending=True), 0.45),
            (safe_percentile_rank(pd.Series(industry_momentum_3, dtype=float), ascending=True), 0.25),
            (pd.Series(industry_breakout_breadth, dtype=float), 0.15),
            (safe_percentile_rank(pd.Series(industry_growth, dtype=float), ascending=True), 0.15),
        ]
    )
    industry_strength_scores = industry_labels.map(industry_strength_rank).astype(float)
    industry_strength_scores = industry_strength_scores.reindex(candidate_index).dropna()
    industry_leader_scores = industry_leader_scores.dropna()
    return industry_strength_scores, industry_leader_scores


def compute_market_exposure(
    market_close: pd.Series,
    signal_date: pd.Timestamp,
    *,
    risk_off_rule: str = "or",
    risk_staging_mode: str = "two_stage",
    core_risk_off_exposure: float = CORE_RISK_OFF_EXPOSURE,
    core_risk_on_exposure: float = CORE_RISK_ON_EXPOSURE,
    core_caution_exposure: float = CORE_CAUTION_EXPOSURE,
    satellite_risk_off_exposure: float = SATELLITE_RISK_OFF_EXPOSURE,
    satellite_risk_on_exposure: float = SATELLITE_RISK_ON_EXPOSURE,
    satellite_caution_exposure: float = SATELLITE_CAUTION_EXPOSURE,
    momentum_lookback: int = MONTHLY_MOMENTUM_LOOKBACK,
    momentum_skip: int = MONTHLY_MOMENTUM_SKIP,
    ma_lookback: int = MONTHLY_MA_LOOKBACK,
) -> Dict[str, float | bool]:
    if signal_date not in market_close.index:
        return {
            "risk_off": False,
            "risk_stage": "risk_on",
            "market_12_1_momentum": np.nan,
            "market_below_10m_ma": False,
            "core_target_exposure": core_risk_on_exposure,
            "satellite_target_exposure": satellite_risk_on_exposure,
            "portfolio_target_exposure": core_risk_on_exposure,
        }

    history = market_close.loc[:signal_date].dropna()
    required_history = max(momentum_lookback + momentum_skip, ma_lookback)
    if len(history) < required_history:
        return {
            "risk_off": False,
            "risk_stage": "risk_on",
            "market_12_1_momentum": np.nan,
            "market_below_10m_ma": False,
            "core_target_exposure": core_risk_on_exposure,
            "satellite_target_exposure": satellite_risk_on_exposure,
            "portfolio_target_exposure": core_risk_on_exposure,
        }

    current_close = float(history.iloc[-1])
    prior_skip_close = float(history.iloc[-1 - momentum_skip]) if len(history) > momentum_skip else np.nan
    prior_lookback_close = float(history.iloc[-1 - momentum_lookback]) if len(history) > momentum_lookback else np.nan
    moving_average = float(history.iloc[-ma_lookback:].mean()) if len(history) >= ma_lookback else np.nan
    market_12_1_momentum = (
        prior_skip_close / prior_lookback_close - 1.0
        if prior_lookback_close > 0 and not np.isnan(prior_skip_close)
        else np.nan
    )
    below_ma = current_close < moving_average if not np.isnan(moving_average) else False
    negative_mom = not np.isnan(market_12_1_momentum) and market_12_1_momentum < 0
    rule = str(risk_off_rule or "or").strip().lower()
    if rule == "and":
        risk_off = negative_mom and below_ma
        caution = negative_mom ^ below_ma
    elif rule in {"mom", "negative_mom"}:
        risk_off = negative_mom
        caution = below_ma and not negative_mom
    elif rule in {"ma", "below_ma"}:
        risk_off = below_ma
        caution = negative_mom and not below_ma
    else:
        risk_off = negative_mom and below_ma
        caution = negative_mom ^ below_ma

    staging_mode = str(risk_staging_mode or "two_stage").strip().lower()
    risk_stage = "risk_on"
    if staging_mode == "three_stage":
        if risk_off:
            risk_stage = "risk_off"
        elif caution:
            risk_stage = "caution"
    else:
        risk_off = risk_off or caution
        risk_stage = "risk_off" if risk_off else "risk_on"

    if risk_stage == "risk_off":
        core_target_exposure = core_risk_off_exposure
        satellite_target_exposure = satellite_risk_off_exposure
    elif risk_stage == "caution":
        core_target_exposure = core_caution_exposure
        satellite_target_exposure = satellite_caution_exposure
    else:
        core_target_exposure = core_risk_on_exposure
        satellite_target_exposure = satellite_risk_on_exposure
    return {
        "risk_off": risk_stage == "risk_off",
        "risk_stage": risk_stage,
        "market_12_1_momentum": market_12_1_momentum,
        "market_below_10m_ma": below_ma,
        "core_target_exposure": core_target_exposure,
        "satellite_target_exposure": satellite_target_exposure,
        "portfolio_target_exposure": core_target_exposure,
    }


def build_factor_cache_path(prepared: PreparedData) -> Path:
    latest_signal_date = max(
        [pd.Timestamp(date) for date in list(prepared.month_end_dates) + list(prepared.week_end_dates)]
    )
    cache_key = "_".join(
        [
            FACTOR_CACHE_VERSION,
            prepared.month_end_dates[0].strftime("%Y%m%d"),
            prepared.month_end_dates[-1].strftime("%Y%m%d"),
            latest_signal_date.strftime("%Y%m%d"),
            str(len(prepared.code_to_name)),
        ]
    )
    return FACTOR_PANEL_DIR / f"{cache_key}.pkl"


def get_factor_signal_dates(prepared: PreparedData) -> List[pd.Timestamp]:
    return sorted(set(prepared.month_end_dates) | set(prepared.week_end_dates))


def get_rebalance_signal_dates(prepared: PreparedData, rebalance_frequency: str) -> List[pd.Timestamp]:
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


def get_latest_available_trading_day(trading_dates: pd.Index, target_date: pd.Timestamp) -> pd.Timestamp | None:
    position = int(trading_dates.searchsorted(target_date, side="right")) - 1
    if position < 0:
        return None
    return pd.Timestamp(trading_dates[position])


def build_prepared_cache_path(
    normalized_codes: List[str],
    start_date: pd.Timestamp,
    end_date: pd.Timestamp,
) -> Path:
    digest = hashlib.md5(",".join(normalized_codes).encode("utf-8")).hexdigest()[:16]
    cache_key = "_".join(
        [
            PREPARED_CACHE_VERSION,
            start_date.strftime("%Y%m%d"),
            end_date.strftime("%Y%m%d"),
            str(len(normalized_codes)),
            digest,
        ]
    )
    return PREPARED_PANEL_DIR / f"{cache_key}.pkl"


def load_prepared_cache(path: Path) -> PreparedData | None:
    if not path.exists():
        return None
    try:
        payload = pd.read_pickle(path)
    except Exception as exc:  # noqa: BLE001
        print(f"[Cache] prepared panel cache 读取失败，将重建: {path} ({exc})")
        return None
    if not isinstance(payload, dict) or payload.get("version") != PREPARED_CACHE_VERSION:
        return None
    prepared = payload.get("prepared")
    if not isinstance(prepared, PreparedData):
        return None
    required_attrs = [
        "week_end_dates",
        "market_weekly_close",
        "month_end_dates",
        "monthly_period_end_dates",
        "price_exact",
        "price_ffill",
        "total_mv",
    ]
    if any(not hasattr(prepared, attr) for attr in required_attrs):
        return None
    prepared.monthly_factor_cache = None
    return prepared


def save_prepared_cache(prepared: PreparedData, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    prepared_to_save = PreparedData(
        stock_basic=prepared.stock_basic,
        price_exact=prepared.price_exact,
        price_ffill=prepared.price_ffill,
        total_mv=prepared.total_mv,
        daily_amount=prepared.daily_amount,
        financials_by_code=prepared.financials_by_code,
        month_end_dates=prepared.month_end_dates,
        monthly_period_end_dates=prepared.monthly_period_end_dates,
        month_start_dates=prepared.month_start_dates,
        week_end_dates=prepared.week_end_dates,
        code_to_name=prepared.code_to_name,
        code_to_list_date=prepared.code_to_list_date,
        code_to_industry=prepared.code_to_industry,
        market_monthly_close=prepared.market_monthly_close,
        market_weekly_close=prepared.market_weekly_close,
        core_members_by_date=prepared.core_members_by_date,
        explore_members_by_date=prepared.explore_members_by_date,
        core_index_weights_by_date=prepared.core_index_weights_by_date,
        explore_index_weights_by_date=prepared.explore_index_weights_by_date,
        data_warnings=prepared.data_warnings,
        monthly_factor_cache=None,
    )
    pd.to_pickle({"version": PREPARED_CACHE_VERSION, "prepared": prepared_to_save}, path)


def load_monthly_factor_cache(path: Path) -> MonthlyFactorCache | None:
    if not path.exists():
        return None
    payload = pd.read_pickle(path)
    if not isinstance(payload, dict) or "version" not in payload or payload["version"] != FACTOR_CACHE_VERSION:
        return None
    return MonthlyFactorCache(**payload["cache"])


def monthly_factor_cache_covers_prepared(cache: MonthlyFactorCache, prepared: PreparedData) -> bool:
    signal_dates = get_factor_signal_dates(prepared)
    if not signal_dates:
        return True
    required_maps = [
        cache.standard_eligible_codes_by_date,
        cache.seed_eligible_codes_by_date,
        cache.signal_mvs_by_date,
        cache.avg_daily_amount_by_date,
        cache.amount_surge_ratio_by_date,
        cache.recent_1m_returns_by_date,
        cache.core_signal_scores_by_date,
        cache.momentum_6_1_by_date,
        cache.momentum_3_1_by_date,
        cache.breakout_signal_by_date,
        cache.quality_scores_by_date,
        cache.growth_quality_scores_by_date,
        cache.growth_acceleration_scores_by_date,
        cache.industry_strength_scores_by_date,
        cache.industry_leader_scores_by_date,
    ]
    if any(any(signal_date not in mapping for signal_date in signal_dates) for mapping in required_maps):
        return False

    latest_signal_date = signal_dates[-1]
    if latest_signal_date in prepared.price_exact.index and latest_signal_date in prepared.total_mv.index:
        has_price = bool(prepared.price_exact.loc[latest_signal_date].notna().any())
        has_mv = bool(prepared.total_mv.loc[latest_signal_date].notna().any())
        if has_price and has_mv:
            latest_mvs = cache.signal_mvs_by_date.get(latest_signal_date, pd.Series(dtype=float))
            return bool(cache.seed_eligible_codes_by_date.get(latest_signal_date)) and bool(latest_mvs.notna().any())
    return True


def save_monthly_factor_cache(cache: MonthlyFactorCache, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "version": FACTOR_CACHE_VERSION,
        "cache": {
            "standard_eligible_codes_by_date": cache.standard_eligible_codes_by_date,
            "seed_eligible_codes_by_date": cache.seed_eligible_codes_by_date,
            "signal_mvs_by_date": cache.signal_mvs_by_date,
            "avg_daily_amount_by_date": cache.avg_daily_amount_by_date,
            "amount_surge_ratio_by_date": cache.amount_surge_ratio_by_date,
            "recent_1m_returns_by_date": cache.recent_1m_returns_by_date,
            "core_signal_scores_by_date": cache.core_signal_scores_by_date,
            "momentum_6_1_by_date": cache.momentum_6_1_by_date,
            "momentum_3_1_by_date": cache.momentum_3_1_by_date,
            "breakout_signal_by_date": cache.breakout_signal_by_date,
            "quality_scores_by_date": cache.quality_scores_by_date,
            "growth_quality_scores_by_date": cache.growth_quality_scores_by_date,
            "growth_acceleration_scores_by_date": cache.growth_acceleration_scores_by_date,
            "industry_strength_scores_by_date": cache.industry_strength_scores_by_date,
            "industry_leader_scores_by_date": cache.industry_leader_scores_by_date,
        },
    }
    pd.to_pickle(payload, path)


def build_monthly_factor_cache(prepared: PreparedData) -> MonthlyFactorCache:
    price_exact = prepared.price_exact
    price_ffill = prepared.price_ffill
    total_mv = prepared.total_mv
    month_end_price_panel = price_ffill.reindex(pd.Index(prepared.month_end_dates))
    month_end_index = pd.Index(prepared.month_end_dates)
    month_end_set = set(prepared.month_end_dates)
    factor_signal_dates = get_factor_signal_dates(prepared)

    standard_eligible_codes_by_date: Dict[pd.Timestamp, List[str]] = {}
    seed_eligible_codes_by_date: Dict[pd.Timestamp, List[str]] = {}
    signal_mvs_by_date: Dict[pd.Timestamp, pd.Series] = {}
    avg_daily_amount_by_date: Dict[pd.Timestamp, pd.Series] = {}
    amount_surge_ratio_by_date: Dict[pd.Timestamp, pd.Series] = {}
    recent_1m_returns_by_date: Dict[pd.Timestamp, pd.Series] = {}
    core_signal_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}
    momentum_6_1_by_date: Dict[pd.Timestamp, pd.Series] = {}
    momentum_3_1_by_date: Dict[pd.Timestamp, pd.Series] = {}
    breakout_signal_by_date: Dict[pd.Timestamp, pd.Series] = {}
    quality_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}
    growth_quality_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}
    growth_acceleration_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}
    industry_strength_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}
    industry_leader_scores_by_date: Dict[pd.Timestamp, pd.Series] = {}

    for signal_date in factor_signal_dates:
        signal_prices = price_exact.loc[signal_date] if signal_date in price_exact.index else pd.Series(dtype=float)
        signal_mvs = total_mv.loc[signal_date] if signal_date in total_mv.index else pd.Series(dtype=float)

        standard_eligible_codes: List[str] = []
        seed_eligible_codes: List[str] = []
        factor_eligible_codes: List[str] = []
        for ts_code in prepared.code_to_name:
            list_date = prepared.code_to_list_date[ts_code]
            if pd.isna(list_date):
                continue
            if ts_code not in signal_prices.index or pd.isna(signal_prices.get(ts_code)):
                continue
            if ts_code not in signal_mvs.index or pd.isna(signal_mvs.get(ts_code)):
                continue
            if list_date <= signal_date - pd.DateOffset(months=FACTOR_MIN_LISTING_MONTHS):
                factor_eligible_codes.append(ts_code)
            if list_date <= signal_date - pd.DateOffset(months=SEED_MIN_LISTING_MONTHS):
                seed_eligible_codes.append(ts_code)
            if list_date <= signal_date - pd.DateOffset(months=MIN_LISTING_MONTHS):
                standard_eligible_codes.append(ts_code)

        eligible_codes = factor_eligible_codes
        standard_eligible_codes_by_date[signal_date] = standard_eligible_codes
        seed_eligible_codes_by_date[signal_date] = seed_eligible_codes
        signal_mvs_by_date[signal_date] = signal_mvs.reindex(eligible_codes).dropna().astype(float)

        amount_history = prepared.daily_amount.reindex(columns=eligible_codes).loc[:signal_date]
        liquidity_window = amount_history.tail(ROLLING_AMOUNT_WINDOW)
        avg_daily_amount = liquidity_window.mean(skipna=True)
        prior_liquidity_window = amount_history.iloc[:-ROLLING_AMOUNT_WINDOW].tail(ROLLING_AMOUNT_WINDOW)
        prior_avg_daily_amount = prior_liquidity_window.mean(skipna=True)
        amount_surge_ratio = (avg_daily_amount / prior_avg_daily_amount.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)
        avg_daily_amount_by_date[signal_date] = avg_daily_amount
        amount_surge_ratio_by_date[signal_date] = amount_surge_ratio

        recent_1m_returns = pd.Series(dtype=float)
        core_signal_scores = pd.Series(dtype=float)
        momentum_6_1 = pd.Series(dtype=float)
        momentum_3_1 = pd.Series(dtype=float)

        month_anchor_pos = int(month_end_index.searchsorted(signal_date, side="right")) - 1
        if month_anchor_pos >= 0:
            current_signal_prices = price_ffill.loc[signal_date, eligible_codes]
            if signal_date in month_end_set:
                current_signal_prices = month_end_price_panel.loc[signal_date, eligible_codes]
            if month_anchor_pos >= 1:
                prev_1m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes]
                valid_recent = prev_1m_prices.notna() & current_signal_prices.notna() & (prev_1m_prices > 0)
                if valid_recent.any():
                    recent_1m_returns = (current_signal_prices.loc[valid_recent] / prev_1m_prices.loc[valid_recent]) - 1.0
            if signal_date in month_end_set:
                if month_anchor_pos >= 12:
                    prev_12m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 12], eligible_codes]
                    prev_1m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes]
                    valid_mom = prev_12m_prices.notna() & prev_1m_prices.notna() & (prev_12m_prices > 0)
                    if valid_mom.any():
                        core_signal_scores = (prev_1m_prices.loc[valid_mom] / prev_12m_prices.loc[valid_mom]) - 1.0
                elif month_anchor_pos >= 6:
                    prev_6m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 6], eligible_codes]
                    prev_1m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes]
                    valid_mom = prev_6m_prices.notna() & prev_1m_prices.notna() & (prev_6m_prices > 0)
                    if valid_mom.any():
                        core_signal_scores = (prev_1m_prices.loc[valid_mom] / prev_6m_prices.loc[valid_mom]) - 1.0
                        momentum_6_1 = core_signal_scores.copy()
                if month_anchor_pos >= 6 and momentum_6_1.empty:
                    prev_6m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 6], eligible_codes]
                    prev_1m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes]
                    valid_mom_6 = prev_6m_prices.notna() & prev_1m_prices.notna() & (prev_6m_prices > 0)
                    if valid_mom_6.any():
                        momentum_6_1 = (prev_1m_prices.loc[valid_mom_6] / prev_6m_prices.loc[valid_mom_6]) - 1.0
                if month_anchor_pos >= 3:
                    prev_3m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 3], eligible_codes]
                    prev_1m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 1], eligible_codes]
                    valid_mom_3 = prev_3m_prices.notna() & prev_1m_prices.notna() & (prev_3m_prices > 0)
                    if valid_mom_3.any():
                        momentum_3_1 = (prev_1m_prices.loc[valid_mom_3] / prev_3m_prices.loc[valid_mom_3]) - 1.0
            else:
                if month_anchor_pos >= 12:
                    prev_12m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 12], eligible_codes]
                    valid_mom = prev_12m_prices.notna() & current_signal_prices.notna() & (prev_12m_prices > 0)
                    if valid_mom.any():
                        core_signal_scores = (current_signal_prices.loc[valid_mom] / prev_12m_prices.loc[valid_mom]) - 1.0
                elif month_anchor_pos >= 6:
                    prev_6m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 6], eligible_codes]
                    valid_mom = prev_6m_prices.notna() & current_signal_prices.notna() & (prev_6m_prices > 0)
                    if valid_mom.any():
                        core_signal_scores = (current_signal_prices.loc[valid_mom] / prev_6m_prices.loc[valid_mom]) - 1.0
                        momentum_6_1 = core_signal_scores.copy()
                if month_anchor_pos >= 6 and momentum_6_1.empty:
                    prev_6m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 6], eligible_codes]
                    valid_mom_6 = prev_6m_prices.notna() & current_signal_prices.notna() & (prev_6m_prices > 0)
                    if valid_mom_6.any():
                        momentum_6_1 = (current_signal_prices.loc[valid_mom_6] / prev_6m_prices.loc[valid_mom_6]) - 1.0
                if month_anchor_pos >= 3:
                    prev_3m_prices = month_end_price_panel.loc[prepared.month_end_dates[month_anchor_pos - 3], eligible_codes]
                    valid_mom_3 = prev_3m_prices.notna() & current_signal_prices.notna() & (prev_3m_prices > 0)
                    if valid_mom_3.any():
                        momentum_3_1 = (current_signal_prices.loc[valid_mom_3] / prev_3m_prices.loc[valid_mom_3]) - 1.0

        recent_1m_returns_by_date[signal_date] = recent_1m_returns
        core_signal_scores_by_date[signal_date] = core_signal_scores
        momentum_6_1_by_date[signal_date] = momentum_6_1
        momentum_3_1_by_date[signal_date] = momentum_3_1

        breakout_signal = pd.Series(False, index=pd.Index(eligible_codes), dtype=bool)
        rolling_window = SEED_BREAKOUT_LOOKBACK_DAYS + 1
        price_history = price_ffill.reindex(columns=eligible_codes).loc[:signal_date].tail(rolling_window)
        if len(price_history) >= 2:
            prior_high = price_history.iloc[:-1].max()
            current_price = price_history.iloc[-1]
            breakout_signal = (current_price >= prior_high.fillna(np.inf) * 0.995).fillna(False)
        breakout_signal_by_date[signal_date] = breakout_signal

        quality_scores, quality_df = compute_quality_scores(prepared, eligible_codes, signal_date)
        growth_quality_scores = compute_growth_quality_scores(quality_df)
        growth_acceleration_scores = compute_growth_acceleration_scores(quality_df)
        industry_strength_scores, industry_leader_scores = compute_industry_relative_strength_scores(
            code_to_industry=prepared.code_to_industry,
            candidate_codes=eligible_codes,
            momentum_6_1=momentum_6_1,
            momentum_3_1=momentum_3_1,
            amount_surge_ratio=amount_surge_ratio,
            breakout_signal=breakout_signal,
            growth_acceleration_scores=growth_acceleration_scores,
        )
        quality_scores_by_date[signal_date] = quality_scores
        growth_quality_scores_by_date[signal_date] = growth_quality_scores
        growth_acceleration_scores_by_date[signal_date] = growth_acceleration_scores
        industry_strength_scores_by_date[signal_date] = industry_strength_scores
        industry_leader_scores_by_date[signal_date] = industry_leader_scores

    return MonthlyFactorCache(
        standard_eligible_codes_by_date=standard_eligible_codes_by_date,
        seed_eligible_codes_by_date=seed_eligible_codes_by_date,
        signal_mvs_by_date=signal_mvs_by_date,
        avg_daily_amount_by_date=avg_daily_amount_by_date,
        amount_surge_ratio_by_date=amount_surge_ratio_by_date,
        recent_1m_returns_by_date=recent_1m_returns_by_date,
        core_signal_scores_by_date=core_signal_scores_by_date,
        momentum_6_1_by_date=momentum_6_1_by_date,
        momentum_3_1_by_date=momentum_3_1_by_date,
        breakout_signal_by_date=breakout_signal_by_date,
        quality_scores_by_date=quality_scores_by_date,
        growth_quality_scores_by_date=growth_quality_scores_by_date,
        growth_acceleration_scores_by_date=growth_acceleration_scores_by_date,
        industry_strength_scores_by_date=industry_strength_scores_by_date,
        industry_leader_scores_by_date=industry_leader_scores_by_date,
    )


def build_single_sleeve_weights(
    base_weights: pd.Series,
    signal_scores: pd.Series,
    recent_1m_returns: pd.Series,
    quality_scores: pd.Series,
    currently_held_codes: Set[str],
    target_exposure: float,
    buy_entry_percentile: float,
    sell_exit_percentile: float,
    quality_quantile: float,
    max_holdings: int,
    protected_hold_codes: Set[str] | None = None,
    protected_sell_exit_percentile: float | None = None,
    allow_missing_quality: bool = False,
    require_breakout_for_buy: bool = False,
    breakout_signal: pd.Series | None = None,
    base_weight_mode: str = "base",
) -> Tuple[pd.Series, Dict[str, object]]:
    if base_weights.empty:
        return pd.Series(dtype=float), {
            "selected_count": 0,
            "buy_candidate_count": 0,
            "keep_candidate_count": 0,
            "quality_pass_count": 0,
            "selected_codes": set(),
            "buy_candidates": set(),
            "keep_candidates": set(),
            "protected_keep_candidates": set(),
        }

    common_codes = base_weights.index.intersection(signal_scores.dropna().index)
    if len(common_codes) == 0:
        return pd.Series(dtype=float), {
            "selected_count": 0,
            "buy_candidate_count": 0,
            "keep_candidate_count": 0,
            "quality_pass_count": 0,
            "selected_codes": set(),
            "buy_candidates": set(),
            "keep_candidates": set(),
            "protected_keep_candidates": set(),
        }

    weight_base = base_weights.loc[common_codes].astype(float)
    signal_score = signal_scores.loc[common_codes].astype(float)
    short_term = recent_1m_returns.reindex(common_codes).astype(float)
    quality = quality_scores.reindex(common_codes).astype(float)
    if allow_missing_quality:
        fill_value = float(quality.dropna().median()) if not quality.dropna().empty else 0.5
        quality = quality.fillna(fill_value)
    else:
        valid_quality = quality.notna()
        weight_base = weight_base.loc[valid_quality]
        signal_score = signal_score.loc[valid_quality]
        short_term = short_term.loc[valid_quality]
        quality = quality.loc[valid_quality]
        common_codes = quality.index
    if len(common_codes) == 0:
        return pd.Series(dtype=float), {
            "selected_count": 0,
            "buy_candidate_count": 0,
            "keep_candidate_count": 0,
            "quality_pass_count": 0,
            "selected_codes": set(),
            "buy_candidates": set(),
            "keep_candidates": set(),
            "protected_keep_candidates": set(),
        }

    signal_rank = signal_score.rank(method="first", ascending=False, pct=True)
    quality_cutoff = quality.quantile(quality_quantile)
    quality_pass = quality >= quality_cutoff
    short_term_pass = short_term > 0
    breakout_pass = breakout_signal.reindex(common_codes).fillna(False).astype(bool) if breakout_signal is not None else pd.Series(True, index=common_codes)

    buy_mask = (signal_rank <= buy_entry_percentile) & quality_pass & short_term_pass
    if require_breakout_for_buy:
        buy_mask = buy_mask & breakout_pass
    buy_candidates = set(signal_rank[buy_mask].index)
    keep_candidates = set(signal_rank[(signal_rank <= sell_exit_percentile) & quality_pass].index)
    protected_keep_candidates: Set[str] = set()
    if protected_hold_codes and protected_sell_exit_percentile is not None:
        protected_mask = signal_rank.index.isin(list(protected_hold_codes))
        protected_keep_candidates = set(
            signal_rank[(signal_rank <= protected_sell_exit_percentile) & quality_pass & protected_mask].index
        )
        keep_candidates |= protected_keep_candidates
    selected_codes = sorted((currently_held_codes & keep_candidates) | buy_candidates)

    if not selected_codes:
        return pd.Series(dtype=float), {
            "selected_count": 0,
            "buy_candidate_count": len(buy_candidates),
            "keep_candidate_count": len(keep_candidates),
            "quality_pass_count": int(quality_pass.sum()),
            "selected_codes": set(),
            "buy_candidates": buy_candidates,
            "keep_candidates": keep_candidates,
            "protected_keep_candidates": protected_keep_candidates,
        }

    signal_strength = safe_percentile_rank(signal_score.loc[selected_codes], ascending=True)
    quality_strength = safe_percentile_rank(quality.loc[selected_codes], ascending=True)
    breakout_strength = breakout_pass.reindex(selected_codes).astype(float)
    base_norm = normalize_positive_weights(weight_base.loc[selected_codes])
    signal_norm = normalize_positive_weights(0.70 * signal_strength + 0.30 * quality_strength + 0.10 * breakout_strength)

    if base_weight_mode == "signal":
        equal_norm = pd.Series(1.0 / len(selected_codes), index=selected_codes, dtype=float)
        adjusted_raw = 0.20 * equal_norm + 0.80 * signal_norm
    elif base_weight_mode == "hybrid":
        adjusted_raw = 0.35 * base_norm + 0.65 * signal_norm
    else:
        score_multiplier = (0.60 + 0.80 * signal_strength + 0.60 * quality_strength + 0.15 * breakout_strength).clip(lower=0.25)
        adjusted_raw = base_norm * score_multiplier
    if max_holdings > 0 and len(adjusted_raw) > max_holdings:
        adjusted_raw = adjusted_raw.sort_values(ascending=False).head(max_holdings)
        selected_codes = adjusted_raw.index.tolist()
    normalized_weights = normalize_positive_weights(adjusted_raw)
    target_weights = normalized_weights * target_exposure

    return target_weights.sort_values(ascending=False), {
        "selected_count": len(selected_codes),
        "buy_candidate_count": len(buy_candidates),
        "keep_candidate_count": len(keep_candidates),
        "quality_pass_count": int(quality_pass.sum()),
        "selected_codes": set(selected_codes),
        "buy_candidates": buy_candidates,
        "keep_candidates": keep_candidates,
        "protected_keep_candidates": protected_keep_candidates,
    }


SELECTION_DIAGNOSTIC_COLUMNS = [
    "selection_bucket",
    "selection_status",
    "target_weight_rank",
    "target_weight_count",
    "signal_rank",
    "signal_universe_count",
    "selection_score",
    "momentum_12_1",
    "momentum_6_1",
    "momentum_3_1",
    "recent_1m_return",
    "avg_daily_amount",
    "amount_surge_ratio",
    "liquidity_score",
    "quality_score",
    "industry_strength_score",
    "industry_leader_score",
    "breakout_signal",
    "buy_candidate",
    "keep_candidate",
    "protected_keep",
    "selected_by_model",
    "risk_stage",
    "raw_risk_stage",
    "market_risk_off",
    "market_momentum",
    "target_total_exposure",
    "risk_trigger",
]


def _diagnostic_float(value: object) -> float | None:
    try:
        number = float(value)
    except Exception:
        return None
    if not np.isfinite(number):
        return None
    return number


def _series_value(series: pd.Series | None, code: str) -> float | None:
    if series is None or series.empty or code not in series.index:
        return None
    return _diagnostic_float(series.loc[code])


def _series_bool(series: pd.Series | None, code: str) -> bool | None:
    if series is None or series.empty or code not in series.index:
        return None
    value = series.loc[code]
    if pd.isna(value):
        return None
    return bool(value)


def _rank_desc(series: pd.Series | None, code: str) -> tuple[int | None, int]:
    if series is None or series.empty:
        return None, 0
    valid = series.replace([np.inf, -np.inf], np.nan).dropna().astype(float)
    if valid.empty:
        return None, 0
    ordered_codes = [str(item) for item in valid.sort_values(ascending=False).index]
    if code not in ordered_codes:
        return None, len(ordered_codes)
    return ordered_codes.index(code) + 1, len(ordered_codes)


def _put_optional(row: Dict[str, object], key: str, value: object) -> None:
    if value is None:
        return
    if isinstance(value, float) and not np.isfinite(value):
        return
    row[key] = value


def build_stock_selection_diagnostics(
    *,
    codes: Iterable[str],
    target_weights: pd.Series,
    signal_scores: pd.Series,
    selected_codes: Set[str],
    buy_candidates: Set[str],
    keep_candidates: Set[str],
    protected_keep_candidates: Set[str] | None = None,
    bucket_by_code: Dict[str, str] | None = None,
    momentum_12_1: pd.Series | None = None,
    momentum_6_1: pd.Series | None = None,
    momentum_3_1: pd.Series | None = None,
    recent_1m_returns: pd.Series | None = None,
    avg_daily_amount: pd.Series | None = None,
    amount_surge_ratio: pd.Series | None = None,
    liquidity_scores: pd.Series | None = None,
    quality_scores: pd.Series | None = None,
    industry_strength_scores: pd.Series | None = None,
    industry_leader_scores: pd.Series | None = None,
    breakout_signal: pd.Series | None = None,
    risk_stage: str = "",
    raw_risk_stage: str = "",
    market_risk_off: bool | None = None,
    market_momentum: float | None = None,
    target_total_exposure: float | None = None,
    risk_trigger: str = "",
) -> Dict[str, Dict[str, object]]:
    target_ranked_codes = [str(item) for item in target_weights.sort_values(ascending=False).index]
    selected_codes = {str(code) for code in selected_codes}
    buy_candidates = {str(code) for code in buy_candidates}
    keep_candidates = {str(code) for code in keep_candidates}
    protected_keep_candidates = {str(code) for code in (protected_keep_candidates or set())}
    bucket_by_code = {str(code): str(bucket) for code, bucket in (bucket_by_code or {}).items()}
    diagnostics: Dict[str, Dict[str, object]] = {}
    for raw_code in codes:
        code = str(raw_code)
        selected = code in selected_codes or code in target_ranked_codes
        signal_rank, signal_count = _rank_desc(signal_scores, code)
        status = "selected" if selected else "not_selected"
        if code in buy_candidates:
            status = "buy_candidate" if selected else "buy_candidate_not_selected"
        elif code in keep_candidates:
            status = "keep_candidate" if selected else "keep_candidate_not_selected"
        row: Dict[str, object] = {
            "selection_status": status,
            "buy_candidate": code in buy_candidates,
            "keep_candidate": code in keep_candidates,
            "protected_keep": code in protected_keep_candidates,
            "selected_by_model": selected,
        }
        _put_optional(row, "selection_bucket", bucket_by_code.get(code))
        if code in target_ranked_codes:
            row["target_weight_rank"] = target_ranked_codes.index(code) + 1
            row["target_weight_count"] = len(target_ranked_codes)
        _put_optional(row, "signal_rank", signal_rank)
        _put_optional(row, "signal_universe_count", signal_count or None)
        _put_optional(row, "selection_score", _series_value(signal_scores, code))
        _put_optional(row, "momentum_12_1", _series_value(momentum_12_1, code))
        _put_optional(row, "momentum_6_1", _series_value(momentum_6_1, code))
        _put_optional(row, "momentum_3_1", _series_value(momentum_3_1, code))
        _put_optional(row, "recent_1m_return", _series_value(recent_1m_returns, code))
        _put_optional(row, "avg_daily_amount", _series_value(avg_daily_amount, code))
        _put_optional(row, "amount_surge_ratio", _series_value(amount_surge_ratio, code))
        _put_optional(row, "liquidity_score", _series_value(liquidity_scores, code))
        _put_optional(row, "quality_score", _series_value(quality_scores, code))
        _put_optional(row, "industry_strength_score", _series_value(industry_strength_scores, code))
        _put_optional(row, "industry_leader_score", _series_value(industry_leader_scores, code))
        _put_optional(row, "breakout_signal", _series_bool(breakout_signal, code))
        _put_optional(row, "risk_stage", risk_stage or None)
        _put_optional(row, "raw_risk_stage", raw_risk_stage or None)
        _put_optional(row, "market_risk_off", market_risk_off)
        _put_optional(row, "market_momentum", market_momentum)
        _put_optional(row, "target_total_exposure", target_total_exposure)
        _put_optional(row, "risk_trigger", risk_trigger or None)
        diagnostics[code] = row
    return diagnostics


def enrich_with_selection_diagnostics(row: Dict[str, object], diagnostics: Dict[str, Dict[str, object]], ts_code: str) -> Dict[str, object]:
    detail = diagnostics.get(str(ts_code))
    if not detail:
        return row
    for key in SELECTION_DIAGNOSTIC_COLUMNS:
        if key in detail:
            row[key] = detail[key]
    return row


def build_core_explore_target_weights(
    base_weights: pd.Series,
    avg_daily_amount: pd.Series,
    core_signal_scores: pd.Series,
    explore_signal_scores: pd.Series,
    seed_signal_scores: pd.Series,
    recent_1m_returns: pd.Series,
    quality_scores: pd.Series,
    breakout_signal: pd.Series,
    currently_held_codes: Set[str],
    core_ratio: float,
    explore_ratio: float,
    core_target_exposure: float,
    satellite_target_exposure: float,
    core_universe_codes: Set[str],
    actual_core_members: Set[str],
    explore_universe_codes: Set[str],
    promoted_core_codes: Set[str],
    promoted_core_ages: Dict[str, int],
    core_source_mode: str,
    standard_eligible_codes: Set[str],
    seed_eligible_codes: Set[str],
    winner_core_stable_share: float = WINNER_CORE_STABLE_SHARE,
    winner_core_promoted_share: float = WINNER_CORE_PROMOTED_SHARE,
    stable_core_max_holdings: int = STABLE_CORE_MAX_HOLDINGS,
    promoted_core_max_holdings: int = PROMOTED_CORE_MAX_HOLDINGS,
    promoted_core_stage_ramp: Dict[int, float] | None = None,
    promoted_core_sell_exit_percentile: float = 1.0,
    core_quality_quantile: float = CORE_QUALITY_QUANTILE,
    promoted_core_quality_quantile: float = 0.40,
    explore_quality_quantile: float = EXPLORE_QUALITY_QUANTILE,
    seed_quality_quantile: float = SEED_QUALITY_QUANTILE,
) -> Tuple[pd.Series, Dict[str, object]]:
    liquidity = avg_daily_amount.reindex(base_weights.index)
    core_eligible_codes = seed_eligible_codes if core_source_mode == "winner_core" else standard_eligible_codes
    if core_source_mode == "winner_core":
        # 胜出者核心：核心仓可以直接从整个动态发现池里提拔强势赢家，
        # 允许更早在中证500/科创100/200 的胜出者上重仓，而不是只限于沪深300/科创50。
        core_candidate_codes = set(core_universe_codes) | set(explore_universe_codes)
        core_codes = liquidity[
            (liquidity >= EXPLORE_AMOUNT_THRESHOLD)
            & liquidity.index.isin(core_candidate_codes)
            & liquidity.index.isin(core_eligible_codes)
        ].index
    else:
        core_codes = liquidity[
            (liquidity >= CORE_AMOUNT_THRESHOLD)
            & liquidity.index.isin(core_universe_codes)
            & liquidity.index.isin(standard_eligible_codes)
        ].index
    explore_codes = liquidity[
        (liquidity >= EXPLORE_AMOUNT_THRESHOLD)
        & liquidity.index.isin(explore_universe_codes)
        & liquidity.index.isin(standard_eligible_codes)
    ].index
    seed_codes = liquidity[
        (liquidity >= SEED_AMOUNT_THRESHOLD)
        & liquidity.index.isin(explore_universe_codes)
        & liquidity.index.isin(seed_eligible_codes)
    ].index

    core_raw = base_weights.reindex(core_codes).dropna()
    stable_core_raw = core_raw.reindex(sorted(set(core_raw.index) & set(actual_core_members))).dropna()
    promoted_core_raw = core_raw.reindex(sorted(set(core_raw.index) & set(promoted_core_codes))).dropna()
    explore_raw = base_weights.reindex(explore_codes).dropna()
    seed_raw = base_weights.reindex(seed_codes).dropna()

    if stable_core_raw.empty and promoted_core_raw.empty and explore_raw.empty and seed_raw.empty:
        return pd.Series(dtype=float), {
            "core_selected_count": 0,
            "stable_core_selected_count": 0,
            "promoted_core_selected_count": 0,
            "explore_selected_count": 0,
            "seed_selected_count": 0,
            "core_buy_candidate_count": 0,
            "stable_core_buy_candidate_count": 0,
            "promoted_core_buy_candidate_count": 0,
            "explore_buy_candidate_count": 0,
            "seed_buy_candidate_count": 0,
            "core_keep_candidate_count": 0,
            "stable_core_keep_candidate_count": 0,
            "promoted_core_keep_candidate_count": 0,
            "explore_keep_candidate_count": 0,
            "seed_keep_candidate_count": 0,
            "core_quality_pass_count": 0,
            "stable_core_quality_pass_count": 0,
            "promoted_core_quality_pass_count": 0,
            "explore_quality_pass_count": 0,
            "seed_quality_pass_count": 0,
            "core_available_count": 0,
            "stable_core_available_count": 0,
            "promoted_core_available_count": 0,
            "explore_available_count": 0,
            "seed_available_count": 0,
            "core_selected_codes": set(),
            "stable_core_selected_codes": set(),
            "promoted_core_selected_codes": set(),
            "explore_selected_codes": set(),
            "seed_selected_codes": set(),
            "core_keep_candidates": set(),
            "stable_core_keep_candidates": set(),
            "promoted_core_keep_candidates": set(),
            "explore_keep_candidates": set(),
            "seed_keep_candidates": set(),
            "core_buy_candidates": set(),
            "stable_core_buy_candidates": set(),
            "promoted_core_buy_candidates": set(),
            "explore_buy_candidates": set(),
            "seed_buy_candidates": set(),
            "core_protected_keep_candidates": set(),
        }
    satellite_bucket_ratio = explore_ratio
    seed_internal_ratio = min(satellite_bucket_ratio, SEED_MAX_PORTFOLIO_RATIO)
    explore_internal_ratio = max(0.0, satellite_bucket_ratio - seed_internal_ratio)
    explore_target_exposure = 0.0
    seed_target_exposure = 0.0
    if not explore_raw.empty or not seed_raw.empty:
        satellite_active_weight = 0.0
        if not explore_raw.empty:
            satellite_active_weight += explore_internal_ratio
        if not seed_raw.empty:
            satellite_active_weight += seed_internal_ratio
        if satellite_active_weight > 0:
            if not explore_raw.empty:
                explore_target_exposure = satellite_target_exposure * explore_internal_ratio / satellite_active_weight
            if not seed_raw.empty:
                seed_target_exposure = satellite_target_exposure * seed_internal_ratio / satellite_active_weight
            explore_target_exposure *= satellite_bucket_ratio
            seed_target_exposure *= satellite_bucket_ratio
    core_target_weight = core_ratio * core_target_exposure if not core_raw.empty else 0.0
    stable_target_weight = 0.0
    promoted_target_weight = 0.0
    if core_target_weight > 0:
        if not stable_core_raw.empty and not promoted_core_raw.empty and core_source_mode == "winner_core":
            share_sum = float(winner_core_stable_share) + float(winner_core_promoted_share)
            if share_sum <= 0:
                stable_share = WINNER_CORE_STABLE_SHARE
                promoted_share = WINNER_CORE_PROMOTED_SHARE
            else:
                stable_share = float(winner_core_stable_share) / share_sum
                promoted_share = float(winner_core_promoted_share) / share_sum
            stable_target_weight = core_target_weight * stable_share
            promoted_target_weight = core_target_weight * promoted_share
        elif not stable_core_raw.empty:
            stable_target_weight = core_target_weight
        elif not promoted_core_raw.empty:
            promoted_target_weight = core_target_weight

    stable_core_weights, stable_core_stats = build_single_sleeve_weights(
        base_weights=stable_core_raw,
        signal_scores=core_signal_scores,
        recent_1m_returns=recent_1m_returns,
        quality_scores=quality_scores,
        currently_held_codes=currently_held_codes,
        target_exposure=stable_target_weight,
        buy_entry_percentile=CORE_BUY_ENTRY_PERCENTILE,
        sell_exit_percentile=CORE_SELL_EXIT_PERCENTILE,
        quality_quantile=float(core_quality_quantile),
        max_holdings=int(stable_core_max_holdings),
        breakout_signal=breakout_signal,
        base_weight_mode="hybrid",
    ) if not stable_core_raw.empty else (
        pd.Series(dtype=float),
        {
            "selected_count": 0,
            "buy_candidate_count": 0,
            "keep_candidate_count": 0,
            "quality_pass_count": 0,
            "selected_codes": set(),
            "buy_candidates": set(),
            "keep_candidates": set(),
            "protected_keep_candidates": set(),
        },
    )

    promoted_base_scaled = promoted_core_raw.copy()
    for code in promoted_base_scaled.index:
        promoted_base_scaled.loc[code] = promoted_base_scaled.loc[code] * get_promoted_core_ramp(
            promoted_core_ages.get(code, 0),
            stage_ramp=promoted_core_stage_ramp,
        )
    promoted_currently_held = set(currently_held_codes) - set(stable_core_stats["selected_codes"])
    promoted_core_sell_exit_percentile = min(1.0, max(0.0001, float(promoted_core_sell_exit_percentile)))
    promoted_core_weights, promoted_core_stats = build_single_sleeve_weights(
        base_weights=promoted_base_scaled,
        signal_scores=core_signal_scores,
        recent_1m_returns=recent_1m_returns,
        quality_scores=quality_scores,
        currently_held_codes=promoted_currently_held,
        target_exposure=promoted_target_weight,
        buy_entry_percentile=1.0,
        sell_exit_percentile=promoted_core_sell_exit_percentile,
        quality_quantile=float(promoted_core_quality_quantile),
        max_holdings=int(promoted_core_max_holdings),
        protected_hold_codes=set(promoted_core_raw.index),
        protected_sell_exit_percentile=promoted_core_sell_exit_percentile,
        breakout_signal=breakout_signal,
        base_weight_mode="signal",
    ) if not promoted_core_raw.empty and promoted_base_scaled.sum() > 0 else (
        pd.Series(dtype=float),
        {
            "selected_count": 0,
            "buy_candidate_count": 0,
            "keep_candidate_count": 0,
            "quality_pass_count": 0,
            "selected_codes": set(),
            "buy_candidates": set(),
            "keep_candidates": set(),
            "protected_keep_candidates": set(),
        },
    )

    core_weights = pd.concat([stable_core_weights, promoted_core_weights]).groupby(level=0).sum().sort_values(ascending=False)
    core_stats = {
        "selected_count": len(set(stable_core_stats["selected_codes"]) | set(promoted_core_stats["selected_codes"])),
        "buy_candidate_count": stable_core_stats["buy_candidate_count"] + promoted_core_stats["buy_candidate_count"],
        "keep_candidate_count": stable_core_stats["keep_candidate_count"] + promoted_core_stats["keep_candidate_count"],
        "quality_pass_count": stable_core_stats["quality_pass_count"] + promoted_core_stats["quality_pass_count"],
        "selected_codes": set(stable_core_stats["selected_codes"]) | set(promoted_core_stats["selected_codes"]),
        "buy_candidates": set(stable_core_stats["buy_candidates"]) | set(promoted_core_stats["buy_candidates"]),
        "keep_candidates": set(stable_core_stats["keep_candidates"]) | set(promoted_core_stats["keep_candidates"]),
        "protected_keep_candidates": set(promoted_core_stats["protected_keep_candidates"]),
    }

    explore_currently_held = set(currently_held_codes) - set(core_stats["selected_codes"])
    if not explore_raw.empty and core_stats["selected_codes"]:
        explore_raw = explore_raw.drop(labels=list(set(explore_raw.index) & set(core_stats["selected_codes"])), errors="ignore")
    if not seed_raw.empty and core_stats["selected_codes"]:
        seed_raw = seed_raw.drop(labels=list(set(seed_raw.index) & set(core_stats["selected_codes"])), errors="ignore")

    explore_weights, explore_stats = build_single_sleeve_weights(
        base_weights=explore_raw,
        signal_scores=explore_signal_scores,
        recent_1m_returns=recent_1m_returns,
        quality_scores=quality_scores,
        currently_held_codes=explore_currently_held,
        target_exposure=explore_target_exposure,
        buy_entry_percentile=EXPLORE_BUY_ENTRY_PERCENTILE,
        sell_exit_percentile=EXPLORE_SELL_EXIT_PERCENTILE,
        quality_quantile=float(explore_quality_quantile),
        max_holdings=EXPLORE_MAX_HOLDINGS,
        breakout_signal=breakout_signal,
        base_weight_mode="hybrid",
    ) if not explore_raw.empty else (
        pd.Series(dtype=float),
        {
            "selected_count": 0,
            "buy_candidate_count": 0,
            "keep_candidate_count": 0,
            "quality_pass_count": 0,
            "selected_codes": set(),
            "buy_candidates": set(),
            "keep_candidates": set(),
            "protected_keep_candidates": set(),
        },
    )

    seed_currently_held = set(currently_held_codes) - set(core_stats["selected_codes"]) - set(explore_stats["selected_codes"])
    if not seed_raw.empty and explore_stats["selected_codes"]:
        seed_raw = seed_raw.drop(labels=list(set(seed_raw.index) & set(explore_stats["selected_codes"])), errors="ignore")

    seed_weights, seed_stats = build_single_sleeve_weights(
        base_weights=seed_raw,
        signal_scores=seed_signal_scores,
        recent_1m_returns=recent_1m_returns,
        quality_scores=quality_scores,
        currently_held_codes=seed_currently_held,
        target_exposure=seed_target_exposure,
        buy_entry_percentile=SEED_BUY_ENTRY_PERCENTILE,
        sell_exit_percentile=SEED_SELL_EXIT_PERCENTILE,
        quality_quantile=float(seed_quality_quantile),
        max_holdings=SEED_MAX_HOLDINGS,
        allow_missing_quality=True,
        require_breakout_for_buy=True,
        breakout_signal=breakout_signal,
        base_weight_mode="signal",
    ) if not seed_raw.empty else (
        pd.Series(dtype=float),
        {
            "selected_count": 0,
            "buy_candidate_count": 0,
            "keep_candidate_count": 0,
            "quality_pass_count": 0,
            "selected_codes": set(),
            "buy_candidates": set(),
            "keep_candidates": set(),
            "protected_keep_candidates": set(),
        },
    )

    combined = pd.concat([core_weights, explore_weights, seed_weights]).groupby(level=0).sum().sort_values(ascending=False)
    combined = enforce_total_portfolio_constraints(
        combined_weights=combined,
        protected_codes=set(core_stats["selected_codes"]),
        max_holdings=TOTAL_PORTFOLIO_MAX_HOLDINGS,
        min_weight=TOTAL_PORTFOLIO_MIN_WEIGHT,
    )
    final_selected_codes = set(combined.index)
    final_core_selected_codes = set(core_stats["selected_codes"]) & final_selected_codes
    final_stable_core_selected_codes = set(stable_core_stats["selected_codes"]) & final_selected_codes
    final_promoted_core_selected_codes = set(promoted_core_stats["selected_codes"]) & final_selected_codes
    final_explore_selected_codes = set(explore_stats["selected_codes"]) & final_selected_codes
    final_seed_selected_codes = set(seed_stats["selected_codes"]) & final_selected_codes
    return combined, {
        "core_selected_count": len(final_core_selected_codes),
        "stable_core_selected_count": len(final_stable_core_selected_codes),
        "promoted_core_selected_count": len(final_promoted_core_selected_codes),
        "explore_selected_count": len(final_explore_selected_codes),
        "seed_selected_count": len(final_seed_selected_codes),
        "core_buy_candidate_count": core_stats["buy_candidate_count"],
        "stable_core_buy_candidate_count": stable_core_stats["buy_candidate_count"],
        "promoted_core_buy_candidate_count": promoted_core_stats["buy_candidate_count"],
        "explore_buy_candidate_count": explore_stats["buy_candidate_count"],
        "seed_buy_candidate_count": seed_stats["buy_candidate_count"],
        "core_keep_candidate_count": core_stats["keep_candidate_count"],
        "stable_core_keep_candidate_count": stable_core_stats["keep_candidate_count"],
        "promoted_core_keep_candidate_count": promoted_core_stats["keep_candidate_count"],
        "explore_keep_candidate_count": explore_stats["keep_candidate_count"],
        "seed_keep_candidate_count": seed_stats["keep_candidate_count"],
        "core_quality_pass_count": core_stats["quality_pass_count"],
        "stable_core_quality_pass_count": stable_core_stats["quality_pass_count"],
        "promoted_core_quality_pass_count": promoted_core_stats["quality_pass_count"],
        "explore_quality_pass_count": explore_stats["quality_pass_count"],
        "seed_quality_pass_count": seed_stats["quality_pass_count"],
        "core_available_count": int(len(core_raw)),
        "stable_core_available_count": int(len(stable_core_raw)),
        "promoted_core_available_count": int(len(promoted_core_raw)),
        "explore_available_count": int(len(explore_raw)),
        "seed_available_count": int(len(seed_raw)),
        "core_selected_codes": final_core_selected_codes,
        "stable_core_selected_codes": final_stable_core_selected_codes,
        "promoted_core_selected_codes": final_promoted_core_selected_codes,
        "explore_selected_codes": final_explore_selected_codes,
        "seed_selected_codes": final_seed_selected_codes,
        "core_keep_candidates": core_stats["keep_candidates"],
        "stable_core_keep_candidates": stable_core_stats["keep_candidates"],
        "promoted_core_keep_candidates": promoted_core_stats["keep_candidates"],
        "explore_keep_candidates": explore_stats["keep_candidates"],
        "seed_keep_candidates": seed_stats["keep_candidates"],
        "core_buy_candidates": core_stats["buy_candidates"],
        "stable_core_buy_candidates": stable_core_stats["buy_candidates"],
        "promoted_core_buy_candidates": promoted_core_stats["buy_candidates"],
        "explore_buy_candidates": explore_stats["buy_candidates"],
        "seed_buy_candidates": seed_stats["buy_candidates"],
        "core_protected_keep_candidates": core_stats["protected_keep_candidates"],
    }


def build_pure_core_growth_weights(
    base_weights: pd.Series,
    avg_daily_amount: pd.Series,
    pure_core_signal_scores: pd.Series,
    growth_quality_scores: pd.Series,
    recent_1m_returns: pd.Series,
    breakout_signal: pd.Series,
    currently_held_codes: Set[str],
    core_watch_streaks: Dict[str, int],
    max_holdings: int,
) -> Tuple[pd.Series, Dict[str, object]]:
    if base_weights.empty or pure_core_signal_scores.empty:
        return pd.Series(dtype=float), {
            "core_selected_count": 0,
            "explore_selected_count": 0,
            "seed_selected_count": 0,
            "core_buy_candidate_count": 0,
            "explore_buy_candidate_count": 0,
            "seed_buy_candidate_count": 0,
            "core_keep_candidate_count": 0,
            "explore_keep_candidate_count": 0,
            "seed_keep_candidate_count": 0,
            "core_quality_pass_count": 0,
            "explore_quality_pass_count": 0,
            "seed_quality_pass_count": 0,
            "core_available_count": 0,
            "explore_available_count": 0,
            "seed_available_count": 0,
            "core_selected_codes": set(),
            "explore_selected_codes": set(),
            "seed_selected_codes": set(),
            "core_keep_candidates": set(),
            "explore_keep_candidates": set(),
            "seed_keep_candidates": set(),
            "core_buy_candidates": set(),
            "explore_buy_candidates": set(),
            "seed_buy_candidates": set(),
            "core_protected_keep_candidates": set(),
            "core_watch_candidates": set(),
            "core_watch_ready_candidates": set(),
            "pure_core_top3_weight_pre_cap": 0.0,
        }

    liquidity = avg_daily_amount.reindex(base_weights.index).fillna(0.0)
    eligible = base_weights.index.intersection(pure_core_signal_scores.dropna().index)
    eligible = eligible.intersection(growth_quality_scores.dropna().index)
    eligible = eligible[liquidity.reindex(eligible).fillna(0.0) >= PURE_CORE_AMOUNT_THRESHOLD]
    if len(eligible) == 0:
        return build_pure_core_growth_weights(
            pd.Series(dtype=float),
            avg_daily_amount,
            pure_core_signal_scores,
            growth_quality_scores,
            recent_1m_returns,
            breakout_signal,
            currently_held_codes,
            core_watch_streaks,
            max_holdings,
        )

    composite_scores = blend_ranked_components(
        [
            (pure_core_signal_scores.reindex(eligible), 0.70),
            (growth_quality_scores.reindex(eligible), 0.30),
        ]
    )
    if composite_scores.empty:
        return build_pure_core_growth_weights(
            pd.Series(dtype=float),
            avg_daily_amount,
            pure_core_signal_scores,
            growth_quality_scores,
            recent_1m_returns,
            breakout_signal,
            currently_held_codes,
            core_watch_streaks,
            max_holdings,
        )

    ranked_scores = composite_scores.sort_values(ascending=False)
    buy_pool = ranked_scores[
        (recent_1m_returns.reindex(ranked_scores.index).fillna(-1.0) > 0)
        | breakout_signal.reindex(ranked_scores.index).fillna(False)
    ]
    if buy_pool.empty:
        buy_pool = ranked_scores
    watch_candidates = set(ranked_scores.head(max(1, math.ceil(max_holdings * PURE_CORE_OBSERVATION_BUFFER_MULTIPLIER))).index)
    watch_ready_candidates = {
        code for code in watch_candidates if core_watch_streaks.get(code, 0) >= PURE_CORE_OBSERVATION_MIN_STREAK
    }
    buy_candidates = set(
        code
        for code in buy_pool.head(max(1, math.ceil(max_holdings * PURE_CORE_BUY_BUFFER_MULTIPLIER))).index
        if code in watch_ready_candidates
    )
    keep_candidates = set(ranked_scores.head(max(1, math.ceil(max_holdings * PURE_CORE_KEEP_BUFFER_MULTIPLIER))).index)
    selected_codes = sorted((currently_held_codes & keep_candidates) | buy_candidates)
    selected_scores = ranked_scores.reindex(selected_codes).dropna().sort_values(ascending=False).head(max_holdings)
    if selected_scores.empty:
        return build_pure_core_growth_weights(
            pd.Series(dtype=float),
            avg_daily_amount,
            pure_core_signal_scores,
            growth_quality_scores,
            recent_1m_returns,
            breakout_signal,
            currently_held_codes,
            core_watch_streaks,
            max_holdings,
        )

    base_norm = normalize_positive_weights(base_weights.reindex(selected_scores.index).fillna(0.0))
    score_norm = normalize_positive_weights(selected_scores)
    concentration = pd.Series(np.exp(-0.60 * np.arange(len(selected_scores))), index=selected_scores.index, dtype=float)
    for idx, multiplier in enumerate(PURE_CORE_TOP3_MULTIPLIERS):
        if idx < len(concentration):
            concentration.iloc[idx] *= multiplier
    concentrated_norm = normalize_positive_weights(score_norm * concentration)
    blended = normalize_positive_weights(PURE_CORE_BASE_WEIGHT_SHARE * base_norm + (1.0 - PURE_CORE_BASE_WEIGHT_SHARE) * concentrated_norm)

    return blended.sort_values(ascending=False), {
        "core_selected_count": len(selected_scores),
        "explore_selected_count": 0,
        "seed_selected_count": 0,
        "core_buy_candidate_count": len(buy_candidates),
        "explore_buy_candidate_count": 0,
        "seed_buy_candidate_count": 0,
        "core_keep_candidate_count": len(keep_candidates),
        "explore_keep_candidate_count": 0,
        "seed_keep_candidate_count": 0,
        "core_quality_pass_count": int(growth_quality_scores.reindex(eligible).notna().sum()),
        "explore_quality_pass_count": 0,
        "seed_quality_pass_count": 0,
        "core_available_count": int(len(eligible)),
        "explore_available_count": 0,
        "seed_available_count": 0,
        "core_selected_codes": set(selected_scores.index),
        "explore_selected_codes": set(),
        "seed_selected_codes": set(),
        "core_keep_candidates": keep_candidates,
        "explore_keep_candidates": set(),
        "seed_keep_candidates": set(),
        "core_buy_candidates": buy_candidates,
        "explore_buy_candidates": set(),
        "seed_buy_candidates": set(),
        "core_protected_keep_candidates": set(),
        "core_watch_candidates": watch_candidates,
        "core_watch_ready_candidates": watch_ready_candidates,
        "pure_core_top3_weight_pre_cap": float(blended.head(3).sum()),
    }


def apply_weight_cap_with_redistribution(raw_weights: pd.Series, cap: float = WEIGHT_CAP) -> Tuple[pd.Series, float]:
    if raw_weights.empty:
        return raw_weights.copy(), 1.0

    weights = raw_weights.fillna(0.0).clip(lower=0.0)
    target_total = float(weights.sum())
    if target_total <= 0:
        return weights * 0.0, 1.0

    weights = weights / target_total
    adjusted = weights.copy()

    # 迭代把超过上限的股票压到单票上限，超额部分再按未封顶股票的相对权重继续分配。
    while True:
        over = adjusted > cap + 1e-12
        if not over.any():
            break

        excess = float((adjusted.loc[over] - cap).sum())
        adjusted.loc[over] = cap

        under = adjusted < cap - 1e-12
        if not under.any() or excess <= 1e-12:
            break

        base = adjusted.loc[under]
        base_sum = float(base.sum())
        if base_sum <= 0:
            break
        adjusted.loc[under] = adjusted.loc[under] + excess * base / base_sum

    adjusted = adjusted.clip(lower=0.0) * target_total
    cash_weight = max(0.0, 1.0 - float(adjusted.sum()))
    return adjusted[adjusted > 1e-12].sort_values(ascending=False), cash_weight


def apply_weekly_rebalance_constraints(
    target_weights: pd.Series,
    current_weights: pd.Series,
    holding_ages: Dict[str, int],
    strategy_config: Dict[str, object],
) -> Tuple[pd.Series, float, Dict[str, object]]:
    try:
        min_hold_periods = int(max(0, float(strategy_config.get("weekly_min_hold_periods", 0) or 0)))
    except (TypeError, ValueError):
        min_hold_periods = 0
    raw_turnover_cap = strategy_config.get("weekly_turnover_cap", None)
    turnover_cap = np.nan
    if raw_turnover_cap is not None:
        try:
            turnover_cap = float(raw_turnover_cap)
        except (TypeError, ValueError):
            turnover_cap = np.nan
    if not np.isfinite(turnover_cap) or turnover_cap <= 0:
        turnover_cap = np.nan

    stats: Dict[str, object] = {
        "weekly_min_hold_periods": min_hold_periods,
        "weekly_min_hold_protected_count": 0,
        "weekly_turnover_cap": turnover_cap,
        "weekly_turnover_cap_applied": False,
        "weekly_turnover_cap_scale": 1.0,
        "weekly_target_one_way_turnover_before_cap": 0.0,
        "weekly_constraint_deleveraging_bypass": False,
    }
    if min_hold_periods <= 0 and not np.isfinite(turnover_cap):
        # Match the post-constraint return shape: sorted by weight desc so
        # downstream consumers (turnover accounting, weight diff rendering)
        # see a consistent order regardless of whether constraints fired.
        passthrough = (
            target_weights.astype(float)
            .replace([np.inf, -np.inf], np.nan)
            .dropna()
            .clip(lower=0.0)
        )
        passthrough = passthrough[passthrough > 1e-12].sort_values(ascending=False)
        cash_weight = max(0.0, 1.0 - float(passthrough.sum()))
        return passthrough, cash_weight, stats

    constrained = target_weights.astype(float).replace([np.inf, -np.inf], np.nan).dropna().clip(lower=0.0)
    current = current_weights.astype(float).replace([np.inf, -np.inf], np.nan).dropna().clip(lower=0.0)
    current = current[current > 1e-12]
    constrained = constrained[constrained > 1e-12]

    current_total = float(current.sum())
    target_total = float(constrained.sum())
    deleveraging = target_total < current_total - 1e-8
    if deleveraging:
        stats["weekly_constraint_deleveraging_bypass"] = True
        cash_weight = max(0.0, 1.0 - float(constrained.sum()))
        return constrained.sort_values(ascending=False), cash_weight, stats

    protected_codes: Set[str] = set()
    if min_hold_periods > 0 and not current.empty:
        for code, current_weight in current.items():
            if holding_ages.get(str(code), min_hold_periods) >= min_hold_periods:
                continue
            target_weight = float(constrained.get(code, 0.0))
            if float(current_weight) > target_weight + 1e-12:
                constrained.loc[code] = float(current_weight)
                protected_codes.add(str(code))
        stats["weekly_min_hold_protected_count"] = len(protected_codes)

    total_after_hold = float(constrained.sum())
    if total_after_hold > 1.0 + 1e-12:
        protected_mask = constrained.index.map(lambda code: str(code) in protected_codes)
        protected_sum = float(constrained.loc[protected_mask].sum()) if protected_mask.any() else 0.0
        if protected_sum >= 1.0:
            constrained = constrained.loc[protected_mask] / protected_sum
        else:
            free = constrained.loc[~protected_mask]
            free_sum = float(free.sum())
            if free_sum > 0:
                constrained.loc[~protected_mask] = free * max(0.0, 1.0 - protected_sum) / free_sum

    if np.isfinite(turnover_cap) and not current.empty:
        union_index = current.index.union(constrained.index)
        current_aligned = current.reindex(union_index).fillna(0.0)
        target_aligned = constrained.reindex(union_index).fillna(0.0)
        delta = target_aligned - current_aligned
        one_way_turnover = 0.5 * float(delta.abs().sum())
        stats["weekly_target_one_way_turnover_before_cap"] = one_way_turnover
        if one_way_turnover > turnover_cap + 1e-12:
            scale = max(0.0, min(1.0, turnover_cap / one_way_turnover))
            constrained = (current_aligned + delta * scale).clip(lower=0.0)
            constrained = constrained[constrained > 1e-12]
            stats["weekly_turnover_cap_applied"] = True
            stats["weekly_turnover_cap_scale"] = scale

    total = float(constrained.sum())
    if total > 1.0 + 1e-12:
        constrained = constrained / total
        total = 1.0
    cash_weight = max(0.0, 1.0 - total)
    return constrained[constrained > 1e-12].sort_values(ascending=False), cash_weight, stats


def enforce_total_portfolio_constraints(
    combined_weights: pd.Series,
    protected_codes: Set[str],
    max_holdings: int,
    min_weight: float,
) -> pd.Series:
    if combined_weights.empty:
        return combined_weights

    positive = combined_weights[combined_weights > 1e-12].sort_values(ascending=False)
    if positive.empty:
        return positive

    protected_series = positive.loc[positive.index.isin(protected_codes)].sort_values(ascending=False)
    non_protected = positive.loc[~positive.index.isin(protected_codes)].sort_values(ascending=False)
    non_protected = non_protected[non_protected >= min_weight]

    remaining_slots = max(0, max_holdings - len(protected_series))
    kept = pd.concat([protected_series, non_protected.head(remaining_slots)]).groupby(level=0).sum()
    kept = kept.sort_values(ascending=False)

    total_target = float(positive.sum())
    if kept.empty or total_target <= 0:
        return pd.Series(dtype=float)
    return normalize_positive_weights(kept) * total_target


def compute_rebalance_trades(
    current_values: pd.Series,
    current_cash: float,
    target_weights: pd.Series,
    rebalance_date: pd.Timestamp,
    tradable_codes: Iterable[str],
    *,
    buy_commission: float = BUY_COMMISSION,
    sell_commission_rate: float = SELL_COMMISSION,
    stamp_rate_override: float | None = None,
) -> Tuple[pd.Series, float, pd.Series, float, Dict[str, Any]]:
    def _normalize_position_series(values: pd.Series) -> pd.Series:
        if values.empty:
            return pd.Series(dtype=float)
        cleaned = values[values.abs() > 1e-12].copy()
        valid_mask = pd.Index(cleaned.index).notna()
        cleaned = cleaned.loc[valid_mask]
        if cleaned.empty:
            return pd.Series(dtype=float)
        # Some aggressive path variants can transiently emit duplicate or NaN-coded holdings.
        # Collapse duplicates by code and drop invalid labels before trade accounting.
        cleaned = cleaned.groupby(cleaned.index).sum()
        return cleaned[cleaned.abs() > 1e-12].sort_index()

    current_values = _normalize_position_series(current_values)
    tradable_list = sorted(set(tradable_codes))
    tradable_set = set(tradable_list)
    locked_codes = [code for code in current_values.index if code not in tradable_set]

    locked_values = current_values.loc[locked_codes] if locked_codes else pd.Series(dtype=float)
    locked_value = float(locked_values.sum())
    pre_trade_nav = float(current_values.sum() + current_cash)

    target_weights = target_weights[target_weights > 1e-12].copy()
    tradable_target = target_weights[target_weights.index.isin(tradable_set)].copy()

    available_weight_budget = max(0.0, 1.0 - locked_value / pre_trade_nav) if pre_trade_nav > 0 else 0.0
    target_tradable_weight = float(tradable_target.sum())
    if target_tradable_weight > available_weight_budget and target_tradable_weight > 0:
        tradable_target = tradable_target * (available_weight_budget / target_tradable_weight)
        target_tradable_weight = float(tradable_target.sum())

    target_cash_weight = max(0.0, 1.0 - locked_value / pre_trade_nav - target_tradable_weight) if pre_trade_nav > 0 else 1.0
    free_weight = target_tradable_weight + target_cash_weight

    if free_weight <= 1e-12:
        tradable_allocation_shares = pd.Series(dtype=float)
        cash_share = 0.0
    else:
        tradable_allocation_shares = tradable_target / free_weight
        cash_share = target_cash_weight / free_weight

    current_tradable_values = current_values.reindex(tradable_list, fill_value=0.0)
    current_tradable_values = current_tradable_values.loc[
        sorted(set(current_tradable_values.index) | set(tradable_allocation_shares.index))
    ].fillna(0.0)

    stamp_rate = get_stamp_duty_rate(rebalance_date) if stamp_rate_override is None else float(stamp_rate_override)
    post_trade_nav_guess = pre_trade_nav
    desired_tradable_values = pd.Series(dtype=float)
    desired_cash = current_cash
    gross_positions = pd.Series(dtype=float)
    gross_cash = current_cash
    buy_amount = 0.0
    sell_amount = 0.0
    trading_cost = 0.0

    for _ in range(10):
        free_capital = max(0.0, post_trade_nav_guess - locked_value)
        desired_tradable_values = tradable_allocation_shares.reindex(current_tradable_values.index, fill_value=0.0) * free_capital
        desired_cash = cash_share * free_capital
        trade_deltas = desired_tradable_values - current_tradable_values
        # 调仓缓冲：目标权重变化不足 1% 的持仓不交易，避免高频小额换手。
        if pre_trade_nav > 0:
            current_weight = current_tradable_values / pre_trade_nav
            desired_weight = desired_tradable_values / pre_trade_nav
            force_exit = (desired_weight <= 1e-12) & (current_weight >= FORCE_EXIT_WEIGHT_THRESHOLD)
            frozen = ((trade_deltas.abs() / pre_trade_nav) < MIN_WEIGHT_TRADE_THRESHOLD) & (~force_exit)
        else:
            frozen = trade_deltas * 0 == 0
        trade_deltas.loc[frozen] = 0.0
        desired_tradable_values = current_tradable_values + trade_deltas
        desired_cash = pre_trade_nav - locked_value - float(desired_tradable_values.sum())
        buy_amount = float(trade_deltas[trade_deltas > 0].sum())
        sell_amount = float((-trade_deltas[trade_deltas < 0]).sum())

        buy_cost = buy_amount * buy_commission
        sell_commission = sell_amount * sell_commission_rate
        sell_stamp_duty = sell_amount * stamp_rate
        trading_cost = buy_cost + sell_commission + sell_stamp_duty
        new_guess = pre_trade_nav - trading_cost

        if abs(new_guess - post_trade_nav_guess) < 1e-12:
            break
        post_trade_nav_guess = new_guess

    post_trade_nav = pre_trade_nav - trading_cost
    desired_cash = desired_cash - trading_cost
    gross_positions = current_tradable_values + trade_deltas
    gross_cash = pre_trade_nav - locked_value - float(gross_positions.sum())

    post_trade_positions = _normalize_position_series(pd.concat([locked_values, desired_tradable_values]))
    gross_positions = _normalize_position_series(pd.concat([locked_values, gross_positions]))

    two_way_turnover = (buy_amount + sell_amount) / pre_trade_nav if pre_trade_nav > 0 else 0.0
    one_way_turnover = two_way_turnover / 2.0

    trade_details: List[Dict[str, object]] = []
    if pre_trade_nav > 0:
        for ts_code, delta in trade_deltas[trade_deltas.abs() > 1e-12].sort_index().items():
            current_value = float(current_tradable_values.get(ts_code, 0.0))
            target_value = float(desired_tradable_values.get(ts_code, 0.0))
            trade_value = float(delta)
            side = "buy" if trade_value > 0 else "sell"
            gross_amount = abs(trade_value)
            fee = gross_amount * buy_commission if side == "buy" else gross_amount * (sell_commission_rate + stamp_rate)
            trade_details.append(
                {
                    "ts_code": str(ts_code),
                    "side": side,
                    "current_weight": current_value / pre_trade_nav,
                    "target_weight": target_value / pre_trade_nav,
                    "post_trade_weight": target_value / post_trade_nav if post_trade_nav > 0 else 0.0,
                    "diff_weight": trade_value / pre_trade_nav,
                    "gross_amount": gross_amount,
                    "gross_amount_pct_nav": gross_amount / pre_trade_nav,
                    "fee": fee,
                    "fee_pct_nav": fee / pre_trade_nav,
                }
            )

    stats = {
        "buy_amount": buy_amount,
        "sell_amount": sell_amount,
        "buy_cost": buy_amount * buy_commission,
        "sell_commission": sell_amount * sell_commission_rate,
        "sell_stamp_duty": sell_amount * stamp_rate,
        "trading_cost": trading_cost,
        "one_way_turnover": one_way_turnover,
        "two_way_turnover": two_way_turnover,
        "pre_trade_nav": pre_trade_nav,
        "post_trade_nav": post_trade_nav,
        "locked_value": locked_value,
        "locked_weight": locked_value / pre_trade_nav if pre_trade_nav > 0 else 0.0,
        "cash_after_trade": desired_cash,
        "trade_details": trade_details,
    }
    return post_trade_positions, float(desired_cash), gross_positions, float(gross_cash), stats


def build_satellite_overlay_target_weights(
    positions: pd.Series,
    cash_value: float,
    *,
    core_codes: Set[str],
    satellite_codes: Set[str],
    satellite_total_weight: float,
) -> pd.Series:
    nav = float(positions.sum() + cash_value)
    if nav <= 0:
        return pd.Series(dtype=float)

    core_values = positions.reindex(sorted(core_codes), fill_value=0.0)
    core_values = core_values[core_values > 1e-12]
    satellite_values = positions.reindex(sorted(satellite_codes), fill_value=0.0)
    satellite_values = satellite_values[satellite_values > 1e-12]

    parts: List[pd.Series] = []
    if not core_values.empty:
        parts.append(core_values / nav)
    if not satellite_values.empty and satellite_total_weight > 0:
        available_sat_weight = max(0.0, 1.0 - float(core_values.sum()) / nav)
        target_sat_weight = min(float(satellite_total_weight), available_sat_weight)
        satellite_internal = satellite_values / float(satellite_values.sum())
        parts.append(satellite_internal * target_sat_weight)
    if not parts:
        return pd.Series(dtype=float)
    return pd.concat(parts).groupby(level=0).sum().sort_values(ascending=False)


def build_portfolio_overlay_target_weights(
    base_target_weights: pd.Series,
    *,
    portfolio_total_weight: float,
) -> pd.Series:
    target = base_target_weights[base_target_weights > 1e-12].copy()
    if target.empty:
        return pd.Series(dtype=float)
    base_total_weight = float(target.sum())
    if base_total_weight <= 0:
        return pd.Series(dtype=float)
    portfolio_total_weight = max(0.0, min(1.0, float(portfolio_total_weight)))
    return (target / base_total_weight * portfolio_total_weight).sort_values(ascending=False)


def _risk_stage_rank(stage: str) -> int:
    mapping = {"risk_on": 0, "caution": 1, "risk_off": 2}
    return mapping.get(str(stage), 0)


def _risk_stage_from_rank(rank: int) -> str:
    mapping = {0: "risk_on", 1: "caution", 2: "risk_off"}
    return mapping.get(int(rank), "risk_on")


def apply_buffered_stage_transition(
    *,
    raw_stage: str,
    state: Dict[str, object],
    confirm_weeks: int,
    risk_off_confirm_weeks: int | None = None,
    risk_on_confirm_weeks: int | None = None,
    stepwise: bool = True,
) -> Tuple[str, Dict[str, object]]:
    """Confirm a stage transition only after the raw signal persists for N weeks.

    When ``risk_off_confirm_weeks`` and/or ``risk_on_confirm_weeks`` are
    provided, the effective confirmation period is chosen by direction:

    - Transitioning toward a MORE defensive stage (higher risk-stage rank,
      e.g. ``risk_on -> caution`` or ``caution -> risk_off``) uses
      ``risk_off_confirm_weeks`` — set this lower than ``confirm_weeks`` to
      react faster to deteriorating markets (降仓快).
    - Transitioning toward a MORE aggressive stage (lower rank) uses
      ``risk_on_confirm_weeks`` — set this higher than ``confirm_weeks`` to
      avoid prematurely re-engaging during a dead-cat bounce (加仓慢).

    When neither directional override is supplied, the behaviour is
    unchanged from the symmetric baseline.
    """
    confirmed_stage = str(state.get("confirmed_stage", "risk_on"))
    pending_stage = state.get("pending_stage")
    pending_count = int(state.get("pending_count", 0))

    if raw_stage == confirmed_stage:
        return confirmed_stage, {"confirmed_stage": confirmed_stage, "pending_stage": None, "pending_count": 0}

    if raw_stage == pending_stage:
        pending_count += 1
    else:
        pending_stage = raw_stage
        pending_count = 1

    raw_rank = _risk_stage_rank(raw_stage)
    current_rank = _risk_stage_rank(confirmed_stage)
    if raw_rank > current_rank and risk_off_confirm_weeks is not None:
        effective_confirm_weeks = int(risk_off_confirm_weeks)
    elif raw_rank < current_rank and risk_on_confirm_weeks is not None:
        effective_confirm_weeks = int(risk_on_confirm_weeks)
    else:
        effective_confirm_weeks = int(confirm_weeks)
    effective_confirm_weeks = max(1, effective_confirm_weeks)

    if pending_count >= effective_confirm_weeks:
        target_rank = raw_rank
        if stepwise and abs(target_rank - current_rank) > 1:
            next_rank = current_rank + 1 if target_rank > current_rank else current_rank - 1
            confirmed_stage = _risk_stage_from_rank(next_rank)
        else:
            confirmed_stage = raw_stage
        return confirmed_stage, {"confirmed_stage": confirmed_stage, "pending_stage": None, "pending_count": 0}

    return confirmed_stage, {"confirmed_stage": confirmed_stage, "pending_stage": pending_stage, "pending_count": pending_count}


def apply_weekly_satellite_risk_overlay(
    *,
    prepared: PreparedData,
    positions: pd.Series,
    cash_value: float,
    gross_positions: pd.Series,
    gross_cash_value: float,
    rebalance_date: pd.Timestamp,
    holding_month_end: pd.Timestamp,
    base_target_weights: pd.Series,
    core_codes: Set[str],
    satellite_codes: Set[str],
    strategy_config: Dict[str, object],
    overlay_state: Dict[str, object],
) -> Tuple[pd.Series, float, pd.Series, float, List[Dict[str, object]], Dict[str, float], Dict[str, object]]:
    risk_frequency = str(strategy_config.get("risk_evaluation_frequency", RISK_EVAL_FREQUENCY_MONTHLY) or RISK_EVAL_FREQUENCY_MONTHLY)
    overlay_scope = str(strategy_config.get("risk_overlay_scope", "") or "")
    if risk_frequency != RISK_EVAL_FREQUENCY_WEEKLY or overlay_scope not in {"satellite_only", "portfolio_only"}:
        return positions, cash_value, gross_positions, gross_cash_value, [], {
            "weekly_overlay_trade_count": 0,
            "weekly_overlay_trading_cost": 0.0,
            "weekly_overlay_avg_one_way_turnover": 0.0,
        }, overlay_state

    trading_dates = prepared.price_ffill.index
    overlay_dates = [date for date in prepared.week_end_dates if rebalance_date < date < holding_month_end]
    if not overlay_dates:
        return positions, cash_value, gross_positions, gross_cash_value, [], {
            "weekly_overlay_trade_count": 0,
            "weekly_overlay_trading_cost": 0.0,
            "weekly_overlay_avg_one_way_turnover": 0.0,
        }, overlay_state
    if overlay_scope == "satellite_only" and not satellite_codes:
        return positions, cash_value, gross_positions, gross_cash_value, [], {
            "weekly_overlay_trade_count": 0,
            "weekly_overlay_trading_cost": 0.0,
            "weekly_overlay_avg_one_way_turnover": 0.0,
        }, overlay_state

    explore_ratio = float(strategy_config.get("explore_ratio", 0.0))
    core_ratio = float(strategy_config.get("core_ratio", 0.0))
    market_risk_off_rule = str(strategy_config.get("market_risk_off_rule", "or") or "or").strip().lower()
    risk_staging_mode = str(strategy_config.get("risk_staging_mode", "two_stage") or "two_stage").strip().lower()
    use_buffered_stage = bool(strategy_config.get("risk_stage_buffered", False))
    confirm_weeks = int(strategy_config.get("risk_stage_confirm_weeks", WEEKLY_STAGE_CONFIRM_WEEKS))
    risk_off_confirm_weeks_cfg = strategy_config.get("risk_off_confirm_weeks")
    risk_on_confirm_weeks_cfg = strategy_config.get("risk_on_confirm_weeks")
    risk_off_confirm_weeks = int(risk_off_confirm_weeks_cfg) if risk_off_confirm_weeks_cfg is not None else None
    risk_on_confirm_weeks = int(risk_on_confirm_weeks_cfg) if risk_on_confirm_weeks_cfg is not None else None
    satellite_risk_off_exposure = float(strategy_config.get("satellite_risk_off_exposure", SATELLITE_RISK_OFF_EXPOSURE))
    satellite_risk_on_exposure = float(strategy_config.get("satellite_risk_on_exposure", SATELLITE_RISK_ON_EXPOSURE))
    satellite_caution_exposure = float(strategy_config.get("satellite_caution_exposure", SATELLITE_CAUTION_EXPOSURE))
    portfolio_ramp_up = float(strategy_config.get("weekly_portfolio_ramp_up", WEEKLY_PORTFOLIO_RAMP_UP))
    use_asymmetric_portfolio_ramp = bool(strategy_config.get("weekly_portfolio_asymmetric", False))

    overlay_turnover_rows: List[Dict[str, object]] = []
    overlay_count = 0
    cumulative_cost = 0.0
    overlay_turnovers: List[float] = []
    prev_date = rebalance_date

    for overlay_date in overlay_dates:
        overlay_trade_date = get_next_trading_day(trading_dates, overlay_date)
        if overlay_trade_date is None or overlay_trade_date > holding_month_end or overlay_trade_date <= prev_date:
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
            risk_off_rule=market_risk_off_rule,
            risk_staging_mode=risk_staging_mode,
            core_risk_off_exposure=CORE_RISK_OFF_EXPOSURE,
            core_risk_on_exposure=CORE_RISK_ON_EXPOSURE,
            core_caution_exposure=CORE_CAUTION_EXPOSURE,
            satellite_risk_off_exposure=satellite_risk_off_exposure,
            satellite_risk_on_exposure=satellite_risk_on_exposure,
            satellite_caution_exposure=satellite_caution_exposure,
            momentum_lookback=WEEKLY_MOMENTUM_LOOKBACK,
            momentum_skip=WEEKLY_MOMENTUM_SKIP,
            ma_lookback=WEEKLY_MA_LOOKBACK,
        )
        effective_stage = str(regime["risk_stage"])
        if use_buffered_stage and risk_staging_mode == "three_stage":
            effective_stage, overlay_state = apply_buffered_stage_transition(
                raw_stage=str(regime["risk_stage"]),
                state=overlay_state,
                confirm_weeks=confirm_weeks,
                risk_off_confirm_weeks=risk_off_confirm_weeks,
                risk_on_confirm_weeks=risk_on_confirm_weeks,
                stepwise=True,
            )
        else:
            overlay_state = {"confirmed_stage": effective_stage, "pending_stage": None, "pending_count": 0}

        if effective_stage == "risk_off":
            satellite_target_exposure = satellite_risk_off_exposure
        elif effective_stage == "caution":
            satellite_target_exposure = satellite_caution_exposure
        else:
            satellite_target_exposure = satellite_risk_on_exposure
        if overlay_scope == "satellite_only":
            target_weights = build_satellite_overlay_target_weights(
                positions,
                cash_value,
                core_codes=core_codes,
                satellite_codes=satellite_codes,
                satellite_total_weight=float(explore_ratio) * satellite_target_exposure,
            )
        else:
            raw_total_exposure = float(core_ratio) * float(regime["core_target_exposure"]) + float(explore_ratio) * satellite_target_exposure
            if use_asymmetric_portfolio_ramp:
                nav_now = float(positions.sum() + cash_value)
                current_total_exposure = float(positions.sum()) / nav_now if nav_now > 0 else 0.0
                target_total_exposure = raw_total_exposure
                if raw_total_exposure > current_total_exposure:
                    target_total_exposure = min(raw_total_exposure, current_total_exposure + portfolio_ramp_up)
            else:
                target_total_exposure = raw_total_exposure
            target_weights = build_portfolio_overlay_target_weights(
                base_target_weights,
                portfolio_total_weight=target_total_exposure,
            )
        tradable_codes = []
        if overlay_trade_date in prepared.price_exact.index:
            exact_prices = prepared.price_exact.loc[overlay_trade_date]
            tradable_codes = exact_prices[exact_prices.notna()].index.tolist()

        positions, cash_value, _, _, trade_stats = compute_rebalance_trades(
            current_values=positions,
            current_cash=cash_value,
            target_weights=target_weights,
            rebalance_date=overlay_trade_date,
            tradable_codes=tradable_codes,
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
            detail_row["risk_stage"] = effective_stage
            detail_row["raw_risk_stage"] = str(regime["risk_stage"])
            detail_row["target_total_exposure"] = float(target_weights.sum()) if not target_weights.empty else 0.0
            detail_row["market_momentum"] = _diagnostic_float(regime.get("market_12_1_momentum"))
            detail_row["market_risk_off"] = bool(regime.get("risk_off"))
            detail_row["risk_trigger"] = "weekly_overlay"
            trade_details.append(detail_row)
        overlay_turnover_rows.append(
            {
                "date": overlay_date,
                "signal_date": overlay_date,
                "evaluation_date": overlay_date,
                "trade_date": overlay_trade_date,
                "one_way_turnover": trade_stats["one_way_turnover"],
                "two_way_turnover": trade_stats["two_way_turnover"],
                "buy_amount": trade_stats["buy_amount"],
                "sell_amount": trade_stats["sell_amount"],
                "buy_amount_pct_nav": trade_stats["buy_amount"] / trade_stats["pre_trade_nav"] if trade_stats["pre_trade_nav"] > 0 else 0.0,
                "sell_amount_pct_nav": trade_stats["sell_amount"] / trade_stats["pre_trade_nav"] if trade_stats["pre_trade_nav"] > 0 else 0.0,
                "trading_cost": trade_stats["trading_cost"],
                "trading_cost_pct_nav": trade_stats["trading_cost"] / trade_stats["pre_trade_nav"] if trade_stats["pre_trade_nav"] > 0 else 0.0,
                "pre_trade_nav": trade_stats["pre_trade_nav"],
                "buy_cost": trade_stats["buy_cost"],
                "sell_commission": trade_stats["sell_commission"],
                "sell_stamp_duty": trade_stats["sell_stamp_duty"],
                "event_type": "weekly_satellite_overlay",
                "risk_stage": effective_stage,
                "raw_risk_stage": str(regime["risk_stage"]),
                "trade_details_json": json.dumps(trade_details, ensure_ascii=False) if trade_details else "",
            }
        )
        prev_date = overlay_trade_date

    if not positions.empty:
        final_prev = prepared.price_ffill.loc[prev_date, positions.index]
        final_now = prepared.price_ffill.loc[holding_month_end, positions.index]
        positions = positions * (final_now / final_prev)
    if not gross_positions.empty:
        gross_final_prev = prepared.price_ffill.loc[prev_date, gross_positions.index]
        gross_final_now = prepared.price_ffill.loc[holding_month_end, gross_positions.index]
        gross_positions = gross_positions * (gross_final_now / gross_final_prev)

    return positions, cash_value, gross_positions, gross_cash_value, overlay_turnover_rows, {
        "weekly_overlay_trade_count": overlay_count,
        "weekly_overlay_trading_cost": cumulative_cost,
        "weekly_overlay_avg_one_way_turnover": float(np.mean(overlay_turnovers)) if overlay_turnovers else 0.0,
    }, overlay_state


def apply_portfolio_drawdown_guard(
    *,
    prepared: PreparedData,
    positions: pd.Series,
    cash_value: float,
    gross_positions: pd.Series,
    gross_cash_value: float,
    rebalance_date: pd.Timestamp,
    holding_period_end: pd.Timestamp,
    base_target_weights: pd.Series,
    strategy_config: Dict[str, object],
    guard_state: Dict[str, object],
) -> Tuple[pd.Series, float, pd.Series, float, List[Dict[str, object]], Dict[str, float], Dict[str, object]]:
    if not bool(strategy_config.get("portfolio_drawdown_guard_enabled", False)):
        if not positions.empty:
            rebalance_prices = prepared.price_ffill.loc[rebalance_date, positions.index]
            month_end_prices = prepared.price_ffill.loc[holding_period_end, positions.index]
            positions = positions * (month_end_prices / rebalance_prices)
        if not gross_positions.empty:
            gross_rebalance_prices = prepared.price_ffill.loc[rebalance_date, gross_positions.index]
            gross_month_end_prices = prepared.price_ffill.loc[holding_period_end, gross_positions.index]
            gross_positions = gross_positions * (gross_month_end_prices / gross_rebalance_prices)
        return positions, cash_value, gross_positions, gross_cash_value, [], {
            "portfolio_guard_trade_count": 0,
            "portfolio_guard_trading_cost": 0.0,
            "portfolio_guard_avg_one_way_turnover": 0.0,
        }, guard_state

    trigger = max(0.0, float(strategy_config.get("portfolio_drawdown_guard_trigger", 0.08)))
    release = max(0.0, float(strategy_config.get("portfolio_drawdown_guard_release", trigger * 0.5)))
    guard_exposure = max(0.0, min(1.0, float(strategy_config.get("portfolio_drawdown_guard_exposure", 0.50))))
    max_days = max(1, int(strategy_config.get("portfolio_drawdown_guard_max_days", 20)))
    trading_dates = prepared.price_ffill.index
    guard_rows: List[Dict[str, object]] = []
    guard_turnovers: List[float] = []
    trade_count = 0
    cumulative_cost = 0.0

    peak_scope = str(strategy_config.get("portfolio_drawdown_guard_peak_scope", "global") or "global").strip().lower()
    nav_at_rebalance = float(positions.sum() + cash_value)
    if peak_scope == "period":
        peak_nav = nav_at_rebalance if nav_at_rebalance > 0 else 1.0
        guard_active = False
        active_days = 0
    else:
        peak_nav = float(guard_state.get("peak_nav", 1.0) or 1.0)
        guard_active = bool(guard_state.get("active", False))
        active_days = int(guard_state.get("active_days", 0) or 0)
    prev_date = rebalance_date

    def mark_to_market(to_date: pd.Timestamp) -> None:
        nonlocal positions, gross_positions, prev_date
        if to_date <= prev_date:
            return
        if not positions.empty:
            prev_prices = prepared.price_ffill.loc[prev_date, positions.index]
            now_prices = prepared.price_ffill.loc[to_date, positions.index]
            positions = positions * (now_prices / prev_prices)
        if not gross_positions.empty:
            gross_prev_prices = prepared.price_ffill.loc[prev_date, gross_positions.index]
            gross_now_prices = prepared.price_ffill.loc[to_date, gross_positions.index]
            gross_positions = gross_positions * (gross_now_prices / gross_prev_prices)
        prev_date = to_date

    def trade_to_exposure(trade_date: pd.Timestamp, exposure: float, event_reason: str, evaluation_date: pd.Timestamp, drawdown: float) -> None:
        nonlocal positions, cash_value, gross_positions, gross_cash_value, trade_count, cumulative_cost
        target_weights = build_portfolio_overlay_target_weights(base_target_weights, portfolio_total_weight=exposure)
        tradable_codes: List[str] = []
        if trade_date in prepared.price_exact.index:
            exact_prices = prepared.price_exact.loc[trade_date]
            tradable_codes = exact_prices[exact_prices.notna()].index.tolist()
        positions, cash_value, _, _, trade_stats = compute_rebalance_trades(
            current_values=positions,
            current_cash=cash_value,
            target_weights=target_weights,
            rebalance_date=trade_date,
            tradable_codes=tradable_codes,
        )
        gross_positions, gross_cash_value, _, _, _ = compute_rebalance_trades(
            current_values=gross_positions,
            current_cash=gross_cash_value,
            target_weights=target_weights,
            rebalance_date=trade_date,
            tradable_codes=tradable_codes,
            buy_commission=0.0,
            sell_commission_rate=0.0,
            stamp_rate_override=0.0,
        )
        if trade_stats["two_way_turnover"] > 1e-12:
            trade_count += 1
            cumulative_cost += float(trade_stats["trading_cost"])
            guard_turnovers.append(float(trade_stats["one_way_turnover"]))
        guard_rows.append(
            {
                "date": evaluation_date,
                "signal_date": evaluation_date,
                "evaluation_date": evaluation_date,
                "trade_date": trade_date,
                "one_way_turnover": trade_stats["one_way_turnover"],
                "two_way_turnover": trade_stats["two_way_turnover"],
                "buy_amount": trade_stats["buy_amount"],
                "sell_amount": trade_stats["sell_amount"],
                "buy_amount_pct_nav": trade_stats["buy_amount"] / trade_stats["pre_trade_nav"] if trade_stats["pre_trade_nav"] > 0 else 0.0,
                "sell_amount_pct_nav": trade_stats["sell_amount"] / trade_stats["pre_trade_nav"] if trade_stats["pre_trade_nav"] > 0 else 0.0,
                "trading_cost": trade_stats["trading_cost"],
                "trading_cost_pct_nav": trade_stats["trading_cost"] / trade_stats["pre_trade_nav"] if trade_stats["pre_trade_nav"] > 0 else 0.0,
                "pre_trade_nav": trade_stats["pre_trade_nav"],
                "buy_cost": trade_stats["buy_cost"],
                "sell_commission": trade_stats["sell_commission"],
                "sell_stamp_duty": trade_stats["sell_stamp_duty"],
                "event_type": "portfolio_drawdown_guard",
                "risk_stage": "guard_on" if exposure < 1.0 else "guard_off",
                "raw_risk_stage": event_reason,
                "drawdown": drawdown,
                "trade_details_json": "",
            }
        )

    if guard_active:
        trade_to_exposure(rebalance_date, guard_exposure, "carry_active", rebalance_date, 0.0)

    evaluation_dates = [date for date in trading_dates if rebalance_date < date < holding_period_end]
    for evaluation_date in evaluation_dates:
        if evaluation_date <= prev_date:
            continue
        mark_to_market(evaluation_date)
        nav_now = float(positions.sum() + cash_value)
        if nav_now <= 0:
            continue
        peak_nav = max(peak_nav, nav_now)
        drawdown = nav_now / peak_nav - 1.0 if peak_nav > 0 else 0.0
        if guard_active:
            active_days += 1

        target_active = guard_active
        reason = ""
        if not guard_active and drawdown <= -trigger:
            target_active = True
            reason = "trigger"
        elif guard_active and (drawdown >= -release or active_days >= max_days):
            target_active = False
            reason = "release" if drawdown >= -release else "max_days"
        if target_active == guard_active:
            continue

        trade_date = get_next_trading_day(trading_dates, evaluation_date)
        if trade_date is None or trade_date > holding_period_end:
            guard_active = target_active
            break
        mark_to_market(trade_date)
        guard_active = target_active
        active_days = 0
        trade_to_exposure(trade_date, guard_exposure if guard_active else 1.0, reason, evaluation_date, drawdown)

    mark_to_market(holding_period_end)
    nav_end = float(positions.sum() + cash_value)
    if nav_end > 0:
        peak_nav = max(peak_nav, nav_end)
    next_guard_state = {"peak_nav": peak_nav, "active": guard_active, "active_days": active_days}
    if peak_scope == "period":
        next_guard_state = {"peak_nav": 1.0, "active": False, "active_days": 0}
    return positions, cash_value, gross_positions, gross_cash_value, guard_rows, {
        "portfolio_guard_trade_count": trade_count,
        "portfolio_guard_trading_cost": cumulative_cost,
        "portfolio_guard_avg_one_way_turnover": float(np.mean(guard_turnovers)) if guard_turnovers else 0.0,
    }, next_guard_state


def compute_metrics(
    equity_curve: pd.DataFrame,
    monthly_returns: pd.DataFrame,
    turnover: pd.DataFrame,
    *,
    rebalance_frequency: str = "monthly",
) -> Dict[str, float]:
    nav = equity_curve["nav"].astype(float)
    period_net = monthly_returns["net_return"].astype(float)
    periods_per_year = 12.0
    if str(rebalance_frequency).strip().lower() == "weekly":
        periods_per_year = 52.0
    elif str(rebalance_frequency).strip().lower() == "biweekly":
        periods_per_year = 26.0

    total_return = float(nav.iloc[-1] - 1.0)
    periods = len(period_net)
    years = periods / periods_per_year if periods > 0 else np.nan
    cagr = float(nav.iloc[-1] ** (1 / years) - 1) if periods > 0 and nav.iloc[-1] > 0 else np.nan
    max_drawdown = float(equity_curve["drawdown"].min())
    win_rate = float((period_net > 0).mean()) if periods > 0 else np.nan
    annual_volatility = float(period_net.std(ddof=1) * math.sqrt(periods_per_year)) if periods > 1 else np.nan
    sharpe_ratio = float((period_net.mean() / period_net.std(ddof=1)) * math.sqrt(periods_per_year)) if periods > 1 and period_net.std(ddof=1) > 0 else np.nan
    average_annual_turnover = (
        float(turnover["one_way_turnover"].astype(float).sum() / years)
        if not turnover.empty and periods > 0 and years > 0
        else np.nan
    )
    cumulative_trading_cost = float(turnover["trading_cost"].sum()) if not turnover.empty else 0.0

    return {
        "total_return": total_return,
        "cagr": cagr,
        "max_drawdown": max_drawdown,
        "monthly_win_rate": win_rate,
        "annual_volatility": annual_volatility,
        "sharpe_ratio": sharpe_ratio,
        "average_annual_turnover": average_annual_turnover,
        "cumulative_trading_cost": cumulative_trading_cost,
    }


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

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={"height_ratios": [3, 1]})
    axes[0].plot(equity_curve["date"], equity_curve["nav"], color="#0B7285", linewidth=2)
    axes[0].set_title("Market-Cap Weighted Basket Backtest")
    axes[0].set_ylabel("NAV")
    axes[0].grid(alpha=0.3)

    axes[1].fill_between(
        equity_curve["date"],
        equity_curve["drawdown"],
        0.0,
        color="#D9480F",
        alpha=0.35,
    )
    axes[1].set_ylabel("Drawdown")
    axes[1].grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / "equity_curve.png", dpi=160)
    plt.close(fig)


def prepare_data(pro, start_date: pd.Timestamp, end_date: pd.Timestamp) -> PreparedData:
    data_start_date = start_date - pd.DateOffset(months=DATA_HISTORY_MONTHS)
    stock_basic = load_or_fetch_stock_basic(pro)
    calendar = load_or_fetch_trade_calendar(pro, data_start_date, end_date)
    usable_calendar = calendar.loc[pd.to_datetime(calendar["cal_date"]) <= end_date].copy()
    open_dates = pd.to_datetime(
        usable_calendar.loc[usable_calendar["is_open"] == 1, "cal_date"],
        errors="coerce",
    ).dropna()
    if open_dates.empty:
        raise RuntimeError("A股可用交易日历为空，无法准备缓存。")
    cache_target_date = pd.Timestamp(open_dates.max()).normalize()
    month_end_dates, _, week_end_dates, _, monthly_period_end_dates = build_month_boundaries(
        usable_calendar,
        formal_calendar=calendar,
    )
    signal_dates = sorted(
        {
            date
            for date in list(month_end_dates) + list(week_end_dates)
            if date >= start_date - pd.DateOffset(months=1)
        }
    )
    market_index_df = load_or_fetch_index_daily(pro, MARKET_INDEX_CODE, data_start_date, end_date)
    load_or_fetch_index_daily(pro, BENCHMARK_INDEX_CODE, data_start_date, end_date)

    index_weights_by_code = {
        index_code: load_or_fetch_index_weight(pro, index_code, data_start_date, end_date)
        for index_code in sorted(set(CORE_INDEX_CODES + EXPLORE_INDEX_CODES))
    }
    (
        core_members_by_date,
        explore_members_by_date,
        core_index_weights_by_date,
        explore_index_weights_by_date,
        universe_codes,
    ) = build_dynamic_pool_maps(index_weights_by_code, signal_dates)
    data_warnings: List[str] = []

    missing_codes = sorted(universe_codes - set(stock_basic["ts_code"]))
    if missing_codes:
        warning = "以下指数成分 ts_code 未在 Tushare stock_basic 中找到，已从动态池剔除：\n" + "\n".join(missing_codes)
        print(f"[Warn] {warning}")
        data_warnings.append(warning)
        missing_code_set = set(missing_codes)
        core_members_by_date = {
            signal_date: members - missing_code_set for signal_date, members in core_members_by_date.items()
        }
        explore_members_by_date = {
            signal_date: members - missing_code_set for signal_date, members in explore_members_by_date.items()
        }
        universe_codes = universe_codes - missing_code_set

    normalized_codes = sorted(universe_codes)
    if not normalized_codes:
        raise RuntimeError("动态指数池为空，无法继续回测。")

    prepared_cache_path = build_prepared_cache_path(normalized_codes, data_start_date, end_date)
    prepared_cached = load_prepared_cache(prepared_cache_path)
    if prepared_cached is not None:
        if prepared_cache_covers_target(prepared_cached, cache_target_date):
            print(f"[Cache] 已加载 prepared panel cache: {prepared_cache_path}")
            prepared_cached.core_members_by_date = core_members_by_date
            prepared_cached.explore_members_by_date = explore_members_by_date
            prepared_cached.core_index_weights_by_date = core_index_weights_by_date
            prepared_cached.explore_index_weights_by_date = explore_index_weights_by_date
            prepared_cached.month_end_dates = month_end_dates
            prepared_cached.monthly_period_end_dates = monthly_period_end_dates
            prepared_cached.week_end_dates = week_end_dates
            factor_cache_path = build_factor_cache_path(prepared_cached)
            monthly_factor_cache = load_monthly_factor_cache(factor_cache_path)
            if monthly_factor_cache is None or not monthly_factor_cache_covers_prepared(monthly_factor_cache, prepared_cached):
                print("[Cache] 月度因子缓存不存在、失效或未覆盖最新信号日，开始构建。")
                monthly_factor_cache = build_monthly_factor_cache(prepared_cached)
                save_monthly_factor_cache(monthly_factor_cache, factor_cache_path)
                print(f"[Cache] 月度因子缓存已写入: {factor_cache_path}")
            else:
                print(f"[Cache] 已加载月度因子缓存: {factor_cache_path}")
            prepared_cached.monthly_factor_cache = monthly_factor_cache
            return prepared_cached
        else:
            print(f"[Cache] prepared panel cache 未覆盖目标交易日 {cache_target_date.date()}，将重建: {prepared_cache_path}")

    per_stock_frames: Dict[str, Dict[str, pd.DataFrame]] = {}
    financials_by_code: Dict[str, pd.DataFrame] = {}
    worker_count = min(CACHE_REFRESH_MAX_WORKERS, len(normalized_codes))
    print(f"[Data] 使用 {worker_count} 个 worker 并行准备 {len(normalized_codes)} 只股票缓存。")
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        futures = {
            executor.submit(prepare_single_stock_cache_data, pro, ts_code, data_start_date, end_date): ts_code
            for ts_code in normalized_codes
        }
        for completed, future in enumerate(as_completed(futures), start=1):
            ts_code = futures[future]
            code, stock_frames, fina_indicator = future.result()
            per_stock_frames[code] = stock_frames
            financials_by_code[code] = fina_indicator
            print(f"[Data] ({completed}/{len(normalized_codes)}) 已完成 {ts_code}")

    prepared = build_monthly_panel(
        normalized_codes,
        stock_basic,
        usable_calendar,
        calendar,
        per_stock_frames,
        financials_by_code,
        market_index_df,
        core_members_by_date,
        explore_members_by_date,
        core_index_weights_by_date,
        explore_index_weights_by_date,
        data_warnings,
    )
    if not prepared_cache_covers_target(prepared, cache_target_date):
        raise RuntimeError(
            f"A股原始行情缓存未覆盖目标交易日 {cache_target_date.date()}，"
            "拒绝写入或使用 stale prepared cache；请先补齐 daily/daily_basic/adj_factor。"
        )
    save_prepared_cache(prepared, prepared_cache_path)
    print(f"[Cache] prepared panel cache 已写入: {prepared_cache_path}")
    factor_cache_path = build_factor_cache_path(prepared)
    monthly_factor_cache = load_monthly_factor_cache(factor_cache_path)
    if monthly_factor_cache is None or not monthly_factor_cache_covers_prepared(monthly_factor_cache, prepared):
        print("[Cache] 月度因子缓存不存在、失效或未覆盖最新信号日，开始构建。")
        monthly_factor_cache = build_monthly_factor_cache(prepared)
        save_monthly_factor_cache(monthly_factor_cache, factor_cache_path)
        print(f"[Cache] 月度因子缓存已写入: {factor_cache_path}")
    else:
        print(f"[Cache] 已加载月度因子缓存: {factor_cache_path}")
    prepared.monthly_factor_cache = monthly_factor_cache
    return prepared


def save_pool_comparison(
    comparison_rows: List[Dict[str, object]],
    comparison_csv: Path | None = None,
    *,
    merge_existing: bool = False,
) -> None:
    if not comparison_rows:
        return

    comparison_df = pd.DataFrame(comparison_rows)
    if comparison_csv is None:
        output_paths = [research_file("strategy_comparison.csv"), research_file("strategy_comparison_base_method.csv")]
        for output_path in output_paths:
            output_df = (
                merge_latest_rows(
                    comparison_df,
                    output_path,
                    key_cols=["strategy_base_id", "sample_tag"],
                    sort_cols=["sample_start", "strategy_kind", "pool_id", "cagr"],
                )
                if merge_existing
                else comparison_df
            )
            save_csv(output_df, output_path)
        return

    output_df = (
        merge_latest_rows(
            comparison_df,
            comparison_csv,
            key_cols=["strategy_base_id", "sample_tag"],
            sort_cols=["sample_start", "strategy_kind", "pool_id", "cagr"],
        )
        if merge_existing
        else comparison_df
    )
    save_csv(output_df, comparison_csv)


def append_comparison_row(comparison_rows: List[Dict[str, object]], summary: Dict[str, object]) -> None:
    metrics = summary["metrics"]
    comparison_rows.append(
        {
            "strategy_id": summary["strategy_id"],
            "strategy_base_id": summary.get("strategy_base_id", summary["strategy_id"]),
            "strategy_name": summary["strategy_name"],
            "strategy_base_name": summary.get("strategy_base_name", summary["strategy_name"]),
            "strategy_kind": summary.get("strategy_kind", "core_explore"),
            "pool_id": summary["pool_id"],
            "pool_name": summary["pool_name"],
            "sample_start": summary["sample_start"],
            "sample_end": summary["sample_end"],
            "sample_tag": summary.get("sample_tag", ""),
            "sample_label": summary.get("sample_label", ""),
            "sample_short_label": summary.get("sample_short_label", ""),
            "is_primary_sample": summary.get("is_primary_sample", False),
            "stock_count": summary["stock_count"],
            "base_weight_method": summary["base_weight_method"],
            "base_weight_name": summary["base_weight_name"],
            "core_source_mode": summary["core_source_mode"],
            "core_source_name": summary["core_source_name"],
            "core_ratio": summary["core_ratio"],
            "explore_ratio": summary["explore_ratio"],
            "pure_core_max_holdings": summary.get("pure_core_max_holdings", 0),
            "total_return": metrics["total_return"],
            "cagr": metrics["cagr"],
            "max_drawdown": metrics["max_drawdown"],
            "annual_volatility": metrics["annual_volatility"],
            "sharpe_ratio": metrics["sharpe_ratio"],
            "monthly_win_rate": metrics["monthly_win_rate"],
            "average_annual_turnover": metrics["average_annual_turnover"],
            "cumulative_trading_cost": metrics["cumulative_trading_cost"],
        }
    )


def update_streak_map(
    streak_map: Dict[str, int],
    positive_codes: Set[str],
    tracked_codes: Set[str],
) -> Dict[str, int]:
    updated: Dict[str, int] = {}
    for code in tracked_codes:
        if code in positive_codes:
            updated[code] = streak_map.get(code, 0) + 1
        else:
            updated[code] = 0
    return updated


def get_promoted_core_ramp(age: int, stage_ramp: Dict[int, float] | None = None) -> float:
    stage_ramp = stage_ramp or PROMOTED_CORE_STAGE_RAMP
    if age <= 0:
        return 0.0
    if age in stage_ramp:
        return float(stage_ramp[age])
    return 1.0


def update_promoted_core_state(
    promoted_core_codes: Set[str],
    promoted_core_ages: Dict[str, int],
    promotion_streaks: Dict[str, int],
    demotion_streaks: Dict[str, int],
    standard_promotion_candidates: Set[str],
    core_selected_codes: Set[str],
    avg_daily_amount: pd.Series,
    actual_core_members: Set[str],
    fast_promotion_candidates: Set[str],
) -> Tuple[Set[str], Dict[str, int], Dict[str, int], Dict[str, int], Dict[str, int]]:
    promotable_candidates = {
        code
        for code in standard_promotion_candidates
        if float(avg_daily_amount.get(code, np.nan)) >= CORE_AMOUNT_THRESHOLD
    }
    fast_promotable_candidates = {
        code
        for code in fast_promotion_candidates
        if float(avg_daily_amount.get(code, np.nan)) >= EXPLORE_AMOUNT_THRESHOLD
    }
    promotion_track_codes = set(promotion_streaks) | standard_promotion_candidates | promoted_core_codes
    promotion_streaks = update_streak_map(promotion_streaks, promotable_candidates, promotion_track_codes)

    standard_newly_promoted = {
        code
        for code, streak in promotion_streaks.items()
        if streak >= PROMOTION_MIN_STREAK and code not in actual_core_members
    }
    fast_newly_promoted = {
        code
        for code in fast_promotable_candidates
        if promotion_streaks.get(code, 0) >= FAST_PROMOTION_MIN_STREAK and code not in actual_core_members
    }
    newly_promoted = standard_newly_promoted | fast_newly_promoted
    next_promoted_core_codes = set(promoted_core_codes) | newly_promoted

    demotion_track_codes = set(demotion_streaks) | next_promoted_core_codes
    demotion_streaks = {
        code: 0 if code in core_selected_codes else demotion_streaks.get(code, 0) + 1
        for code in demotion_track_codes
    }

    demoted_codes = {
        code
        for code in list(next_promoted_core_codes)
        if code not in actual_core_members and demotion_streaks.get(code, 0) >= PROMOTED_CORE_DEMOTION_MIN_STREAK
    }
    next_promoted_core_codes -= demoted_codes

    next_promoted_core_ages: Dict[str, int] = {}
    for code in next_promoted_core_codes:
        if code in newly_promoted and code not in promoted_core_codes:
            next_promoted_core_ages[code] = 1
        else:
            next_promoted_core_ages[code] = promoted_core_ages.get(code, 0) + 1

    for code in demoted_codes:
        promotion_streaks[code] = 0
        demotion_streaks[code] = 0
        promoted_core_ages.pop(code, None)
    for code in actual_core_members:
        demotion_streaks.pop(code, None)

    status = {
        "promoted_core_count": len(next_promoted_core_codes),
        "newly_promoted_count": len(newly_promoted - promoted_core_codes),
        "fast_promoted_count": len(fast_newly_promoted - promoted_core_codes),
        "demoted_count": len(demoted_codes),
    }
    return next_promoted_core_codes, next_promoted_core_ages, promotion_streaks, demotion_streaks, status


def _weights_to_preview_holdings(
    weights: pd.Series,
    cash_weight: float,
    *,
    price_ffill: pd.DataFrame,
    signal_date: pd.Timestamp,
    code_to_name: Dict[str, str],
    selection_diagnostics: Dict[str, Dict[str, object]] | None = None,
) -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    price_row = price_ffill.loc[signal_date] if signal_date in price_ffill.index else pd.Series(dtype=float)
    for ts_code, weight in weights.sort_values(ascending=False).items():
        latest_price = price_row.get(ts_code, np.nan)
        rows.append(
            enrich_with_selection_diagnostics(
                {
                    "ts_code": str(ts_code),
                    "name": str(code_to_name.get(str(ts_code), "")),
                    "weight": float(weight),
                    "latest_price": float(latest_price) if pd.notna(latest_price) else None,
                },
                selection_diagnostics or {},
                str(ts_code),
            )
        )
    if cash_weight > 1e-12:
        rows.append({"ts_code": "CASH", "name": "现金", "weight": float(cash_weight), "latest_price": None})
    return rows


def build_month_end_preview_payload(
    *,
    prepared: PreparedData,
    strategy_config: Dict[str, object],
    signal_date: pd.Timestamp,
    formal_signal_date: pd.Timestamp | None,
    positions: pd.Series,
    promoted_core_codes: Set[str],
    promoted_core_ages: Dict[str, int],
    pure_core_watch_streaks: Dict[str, int],
) -> Dict[str, object] | None:
    factor_cache = prepared.monthly_factor_cache
    if factor_cache is None:
        return None
    default_standard_eligible_codes = factor_cache.standard_eligible_codes_by_date.get(signal_date, [])
    default_seed_eligible_codes = factor_cache.seed_eligible_codes_by_date.get(signal_date, [])
    raw_weights = factor_cache.signal_mvs_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    standard_eligible_codes, seed_eligible_codes = resolve_strategy_listing_eligible_codes(
        prepared=prepared,
        signal_date=signal_date,
        strategy_config=strategy_config,
        default_standard_eligible_codes=default_standard_eligible_codes,
        default_seed_eligible_codes=default_seed_eligible_codes,
        available_codes=raw_weights.index,
    )
    if not standard_eligible_codes and not seed_eligible_codes:
        return None

    eligible_codes = seed_eligible_codes
    avg_daily_amount = factor_cache.avg_daily_amount_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    amount_surge_ratio = factor_cache.amount_surge_ratio_by_date.get(signal_date, pd.Series(dtype=float)).copy()

    core_signal_scores = factor_cache.core_signal_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    momentum_6_1 = factor_cache.momentum_6_1_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    momentum_3_1 = factor_cache.momentum_3_1_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    recent_1m_returns = factor_cache.recent_1m_returns_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    breakout_signal = factor_cache.breakout_signal_by_date.get(signal_date, pd.Series(dtype=bool)).copy()
    quality_scores = factor_cache.quality_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    growth_quality_scores = factor_cache.growth_quality_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    growth_acceleration_scores = factor_cache.growth_acceleration_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    industry_strength_scores = factor_cache.industry_strength_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
    industry_leader_scores = factor_cache.industry_leader_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()

    core_signal_scores = compute_core_signal_scores(
        core_signal_mode=str(strategy_config.get("core_signal_mode", "") or "").strip(),
        cached_default=core_signal_scores,
        strategy_config=strategy_config,
        momentum_6_1=momentum_6_1,
        momentum_3_1=momentum_3_1,
        recent_1m_returns=recent_1m_returns,
        amount_surge_ratio=amount_surge_ratio,
        breakout_signal=breakout_signal,
        quality_scores=quality_scores,
        growth_acceleration_scores=growth_acceleration_scores,
        industry_strength_scores=industry_strength_scores,
        industry_leader_scores=industry_leader_scores,
    )

    explore_signal_scores = blend_ranked_components(
        [
            (industry_strength_scores, 0.40),
            (industry_leader_scores, 0.25),
            (safe_percentile_rank(momentum_6_1, ascending=True), 0.20),
            (safe_percentile_rank(momentum_3_1, ascending=True), 0.10),
            (breakout_signal.astype(float), 0.05),
        ]
    )
    seed_signal_scores = blend_ranked_components(
        [
            (industry_strength_scores, 0.30),
            (industry_leader_scores, 0.30),
            (safe_percentile_rank(momentum_3_1, ascending=True), 0.15),
            (safe_percentile_rank(recent_1m_returns, ascending=True), 0.10),
            (breakout_signal.astype(float), 0.10),
            (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.05),
        ]
    )
    actual_core_members, actual_explore_members, _alpha_pool_profile = resolve_alpha_pool_universes(
        prepared=prepared,
        signal_date=signal_date,
        strategy_config=strategy_config,
        standard_eligible_codes=standard_eligible_codes,
        seed_eligible_codes=seed_eligible_codes,
        pool_signal_scores=core_signal_scores,
    )
    core_universe_codes = set(actual_core_members) | set(promoted_core_codes)
    explore_universe_codes = set(actual_explore_members) - set(promoted_core_codes)

    strategy_kind = str(strategy_config.get("strategy_kind", "core_explore"))
    market_close_series = prepared.market_monthly_close.copy()
    if signal_date not in market_close_series.index and signal_date in prepared.market_weekly_close.index:
        market_close_series.loc[signal_date] = float(prepared.market_weekly_close.loc[signal_date])
        market_close_series = market_close_series.sort_index()
    market_regime = compute_market_exposure(
        market_close_series,
        signal_date,
        risk_off_rule=strategy_config.get("market_risk_off_rule", "or"),
        risk_staging_mode=strategy_config.get("risk_staging_mode", "two_stage"),
        core_risk_off_exposure=float(strategy_config.get("core_risk_off_exposure", CORE_RISK_OFF_EXPOSURE)),
        core_risk_on_exposure=float(strategy_config.get("core_risk_on_exposure", CORE_RISK_ON_EXPOSURE)),
        core_caution_exposure=float(strategy_config.get("core_caution_exposure", CORE_CAUTION_EXPOSURE)),
        satellite_risk_off_exposure=float(strategy_config.get("satellite_risk_off_exposure", SATELLITE_RISK_OFF_EXPOSURE)),
        satellite_risk_on_exposure=float(strategy_config.get("satellite_risk_on_exposure", SATELLITE_RISK_ON_EXPOSURE)),
        satellite_caution_exposure=float(strategy_config.get("satellite_caution_exposure", SATELLITE_CAUTION_EXPOSURE)),
    )
    if strategy_kind == "pure_core_growth":
        market_regime = {
            "risk_off": False,
            "risk_stage": "risk_on",
            "market_12_1_momentum": np.nan,
            "market_below_10m_ma": False,
            "core_target_exposure": 1.0,
            "satellite_target_exposure": 0.0,
            "portfolio_target_exposure": 1.0,
        }

    currently_held_codes = set(positions.index)
    base_weight_method = str(strategy_config["base_weight_method"])
    if base_weight_method == "index_weight":
        base_weights = pd.concat(
            [
                prepared.core_index_weights_by_date.get(signal_date, pd.Series(dtype=float)),
                prepared.explore_index_weights_by_date.get(signal_date, pd.Series(dtype=float)),
            ]
        ).groupby(level=0).sum()
        base_weights = base_weights.reindex(eligible_codes).dropna()
    elif base_weight_method == "equal_weight":
        base_weights = pd.Series(1.0, index=pd.Index(eligible_codes, name="ts_code"), dtype=float)
    else:
        base_weights = raw_weights.copy()

    if strategy_kind == "pure_core_growth":
        pure_core_signal_scores = blend_ranked_components(
            [
                (growth_acceleration_scores, 0.30),
                (industry_strength_scores, 0.20),
                (industry_leader_scores, 0.20),
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.10),
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.10),
                (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.05),
                (breakout_signal.astype(float), 0.05),
            ]
        )
        preview_watch_streaks = dict(pure_core_watch_streaks)
        watch_pool = set(
            pure_core_signal_scores.sort_values(ascending=False).head(
                max(1, math.ceil(int(strategy_config["pure_core_max_holdings"]) * PURE_CORE_OBSERVATION_BUFFER_MULTIPLIER))
            ).index
        )
        preview_watch_streaks = update_streak_map(
            preview_watch_streaks,
            positive_codes=watch_pool,
            tracked_codes=set(preview_watch_streaks) | watch_pool | currently_held_codes,
        )
        raw_target_weights, selection_stats = build_pure_core_growth_weights(
            base_weights=base_weights.reindex(seed_eligible_codes).dropna(),
            avg_daily_amount=avg_daily_amount,
            pure_core_signal_scores=pure_core_signal_scores,
            growth_quality_scores=growth_quality_scores,
            recent_1m_returns=recent_1m_returns,
            breakout_signal=breakout_signal,
            currently_held_codes=currently_held_codes,
            core_watch_streaks=preview_watch_streaks,
            max_holdings=int(strategy_config["pure_core_max_holdings"]),
        )
    else:
        raw_target_weights, selection_stats = build_core_explore_target_weights(
            base_weights=base_weights,
            avg_daily_amount=avg_daily_amount,
            core_signal_scores=core_signal_scores,
            explore_signal_scores=explore_signal_scores,
            seed_signal_scores=seed_signal_scores,
            recent_1m_returns=recent_1m_returns,
            quality_scores=quality_scores,
            breakout_signal=breakout_signal,
            currently_held_codes=currently_held_codes,
            core_ratio=float(strategy_config["core_ratio"]),
            explore_ratio=float(strategy_config["explore_ratio"]),
            core_target_exposure=float(market_regime["core_target_exposure"]),
            satellite_target_exposure=float(market_regime["satellite_target_exposure"]),
            core_universe_codes=core_universe_codes,
            actual_core_members=actual_core_members,
            explore_universe_codes=explore_universe_codes,
            promoted_core_codes=set(promoted_core_codes),
            promoted_core_ages=dict(promoted_core_ages),
            core_source_mode=str(strategy_config["core_source_mode"]),
            standard_eligible_codes=set(standard_eligible_codes),
            seed_eligible_codes=set(seed_eligible_codes),
            winner_core_stable_share=float(strategy_config.get("winner_core_stable_share", WINNER_CORE_STABLE_SHARE)),
            winner_core_promoted_share=float(strategy_config.get("winner_core_promoted_share", WINNER_CORE_PROMOTED_SHARE)),
            stable_core_max_holdings=int(strategy_config.get("stable_core_max_holdings", STABLE_CORE_MAX_HOLDINGS)),
            promoted_core_max_holdings=int(strategy_config.get("promoted_core_max_holdings", PROMOTED_CORE_MAX_HOLDINGS)),
            promoted_core_stage_ramp=strategy_config.get("promoted_core_stage_ramp", None),
            promoted_core_sell_exit_percentile=float(strategy_config.get("promoted_core_sell_exit_percentile", 1.0)),
            core_quality_quantile=float(strategy_config.get("core_quality_quantile", CORE_QUALITY_QUANTILE)),
            promoted_core_quality_quantile=float(strategy_config.get("promoted_core_quality_quantile", 0.40)),
            explore_quality_quantile=float(strategy_config.get("explore_quality_quantile", EXPLORE_QUALITY_QUANTILE)),
            seed_quality_quantile=float(strategy_config.get("seed_quality_quantile", SEED_QUALITY_QUANTILE)),
        )
    weight_cap = float(strategy_config.get("weight_cap", WEIGHT_CAP))
    if not np.isfinite(weight_cap) or weight_cap <= 0:
        weight_cap = WEIGHT_CAP
    target_weights, target_cash_weight = apply_weight_cap_with_redistribution(raw_target_weights, cap=min(1.0, weight_cap))
    candidate_code_sets = [
        set(selection_stats.get(key, set()) or set())
        for key in (
            "core_buy_candidates",
            "stable_core_buy_candidates",
            "promoted_core_buy_candidates",
            "explore_buy_candidates",
            "seed_buy_candidates",
            "core_keep_candidates",
            "stable_core_keep_candidates",
            "promoted_core_keep_candidates",
            "explore_keep_candidates",
            "seed_keep_candidates",
        )
    ]
    buy_candidate_codes = set().union(
        *[
            set(selection_stats.get(key, set()) or set())
            for key in (
                "core_buy_candidates",
                "stable_core_buy_candidates",
                "promoted_core_buy_candidates",
                "explore_buy_candidates",
                "seed_buy_candidates",
            )
        ]
    )
    keep_candidate_codes = set().union(
        *[
            set(selection_stats.get(key, set()) or set())
            for key in (
                "core_keep_candidates",
                "stable_core_keep_candidates",
                "promoted_core_keep_candidates",
                "explore_keep_candidates",
                "seed_keep_candidates",
            )
        ]
    )
    diagnostic_codes = set(map(str, target_weights.index)) | set(map(str, currently_held_codes)) | set().union(*candidate_code_sets)
    bucket_by_code: Dict[str, str] = {}
    for bucket_name, keys in (
        ("稳定核心", ("stable_core_selected_codes", "stable_core_buy_candidates", "stable_core_keep_candidates")),
        ("晋升核心", ("promoted_core_selected_codes", "promoted_core_buy_candidates", "promoted_core_keep_candidates")),
        ("探索仓", ("explore_selected_codes", "explore_buy_candidates", "explore_keep_candidates")),
        ("种子仓", ("seed_selected_codes", "seed_buy_candidates", "seed_keep_candidates")),
        ("核心仓", ("core_selected_codes", "core_buy_candidates", "core_keep_candidates")),
    ):
        for key in keys:
            for code in selection_stats.get(key, set()) or set():
                bucket_by_code.setdefault(str(code), bucket_name)
    signal_components = [core_signal_scores, explore_signal_scores, seed_signal_scores]
    if strategy_kind == "pure_core_growth":
        signal_components = [pure_core_signal_scores]
    diagnostic_signal_scores = (
        pd.concat([series for series in signal_components if not series.empty]).groupby(level=0).max()
        if any(not series.empty for series in signal_components)
        else pd.Series(dtype=float)
    )
    selection_diagnostics = build_stock_selection_diagnostics(
        codes=diagnostic_codes,
        target_weights=target_weights,
        signal_scores=diagnostic_signal_scores,
        selected_codes=set(map(str, target_weights.index)),
        buy_candidates=buy_candidate_codes,
        keep_candidates=keep_candidate_codes,
        protected_keep_candidates=set(selection_stats.get("core_protected_keep_candidates", set()) or set()),
        bucket_by_code=bucket_by_code,
        momentum_6_1=momentum_6_1,
        momentum_3_1=momentum_3_1,
        recent_1m_returns=recent_1m_returns,
        avg_daily_amount=avg_daily_amount,
        amount_surge_ratio=amount_surge_ratio,
        liquidity_scores=safe_percentile_rank(avg_daily_amount, ascending=True),
        quality_scores=quality_scores,
        industry_strength_scores=industry_strength_scores,
        industry_leader_scores=industry_leader_scores,
        breakout_signal=breakout_signal,
        risk_stage=str(market_regime.get("risk_stage") or ("risk_off" if market_regime.get("risk_off") else "risk_on")),
        raw_risk_stage=str(market_regime.get("raw_risk_stage") or ""),
        market_risk_off=bool(market_regime.get("risk_off")),
        market_momentum=_diagnostic_float(market_regime.get("market_12_1_momentum")),
        target_total_exposure=float(target_weights.sum()) if not target_weights.empty else 0.0,
    )
    preview_detail_codes = set(map(str, target_weights.index)) | set(map(str, currently_held_codes))
    return {
        "mode": "month_end_preview",
        "status": "available",
        "preview_as_of": signal_date.strftime("%Y-%m-%d"),
        "formal_signal_date": formal_signal_date.strftime("%Y-%m-%d") if formal_signal_date is not None else None,
        "note": "月中观察口径：使用当日收盘数据模拟“如果今天是月末”的候选组合，不进入正式回测收益、winner 或 core_active 规则。",
        "target_total_exposure": float(max(0.0, 1.0 - target_cash_weight)),
        "risk_state": str(market_regime.get("risk_stage") or ("risk_off" if market_regime.get("risk_off") else "risk_on")),
        "market_momentum": float(market_regime["market_12_1_momentum"]) if pd.notna(market_regime.get("market_12_1_momentum")) else None,
        "selected_count": int(len(target_weights)),
        "selection_counts": {
            key: int(value)
            for key, value in selection_stats.items()
            if key.endswith("_count") and isinstance(value, (int, np.integer))
        },
        "selection_diagnostics": {
            code: selection_diagnostics[code]
            for code in sorted(preview_detail_codes)
            if code in selection_diagnostics
        },
        "holdings": _weights_to_preview_holdings(
            target_weights,
            target_cash_weight,
            price_ffill=prepared.price_ffill,
            signal_date=signal_date,
            code_to_name=prepared.code_to_name,
            selection_diagnostics=selection_diagnostics,
        ),
    }


def run_backtest(
    prepared: PreparedData,
    strategy_config: Dict[str, object],
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, Dict[str, object]]:
    sample_start = pd.Timestamp(strategy_config.get("sample_start", PRIMARY_SAMPLE_START))
    sample_tag = str(strategy_config.get("sample_tag", "since_2020_01"))
    sample_label = str(strategy_config.get("sample_label", "2020-01 起"))
    sample_short_label = str(strategy_config.get("sample_short_label", "2020-01"))
    is_primary_sample = bool(strategy_config.get("is_primary_sample", sample_start == PRIMARY_SAMPLE_START))
    price_exact = prepared.price_exact
    price_ffill = prepared.price_ffill
    total_mv = prepared.total_mv
    rebalance_frequency = str(strategy_config.get("rebalance_frequency", "monthly") or "monthly").strip().lower()
    signal_schedule = get_rebalance_signal_dates(prepared, rebalance_frequency)
    trading_dates = price_ffill.index

    if len(signal_schedule) < 2:
        raise RuntimeError("交易日历不足以构造回测。")

    report_start_idx = None
    for idx in range(len(signal_schedule) - 1):
        if signal_schedule[idx + 1] >= sample_start:
            report_start_idx = idx
            break
    if report_start_idx is None:
        raise RuntimeError("设定的回测起点晚于当前可用调仓数据。")

    positions = pd.Series(dtype=float)
    cash_value = 1.0
    nav_at_signal_date = 1.0
    warnings: List[str] = list(prepared.data_warnings)
    promoted_core_codes: Set[str] = set()
    promoted_core_ages: Dict[str, int] = {}
    promotion_streaks: Dict[str, int] = {}
    demotion_streaks: Dict[str, int] = {}
    pure_core_watch_streaks: Dict[str, int] = {}
    holding_ages: Dict[str, int] = {}
    risk_evaluation_frequency = str(strategy_config.get("risk_evaluation_frequency", RISK_EVAL_FREQUENCY_MONTHLY) or RISK_EVAL_FREQUENCY_MONTHLY)
    risk_staging_mode = str(strategy_config.get("risk_staging_mode", "two_stage") or "two_stage").strip().lower()
    overlay_state: Dict[str, object] = {"confirmed_stage": "risk_on", "pending_stage": None, "pending_count": 0}
    drawdown_guard_state: Dict[str, object] = {"peak_nav": 1.0, "active": False, "active_days": 0}

    monthly_rows: List[Dict[str, object]] = []
    turnover_rows: List[Dict[str, object]] = []
    weights_history_rows: List[Dict[str, object]] = []
    equity_rows: List[Dict[str, object]] = [
        {"date": sample_start, "portfolio_return": 0.0, "nav": 1.0, "drawdown": 0.0, "trading_cost": 0.0}
    ]
    realized_schedule_end = signal_schedule[report_start_idx]

    for idx in range(report_start_idx, len(signal_schedule) - 1):
        signal_date = signal_schedule[idx]
        holding_month_end = signal_schedule[idx + 1]
        holding_period_end = get_latest_available_trading_day(trading_dates, holding_month_end)
        if holding_period_end is None or holding_period_end < signal_date:
            continue
        rebalance_date = get_next_trading_day(trading_dates, signal_date)
        if rebalance_date is None or rebalance_date > holding_period_end:
            continue

        factor_cache = prepared.monthly_factor_cache
        if factor_cache is None:
            raise RuntimeError("PreparedData 缺少 monthly_factor_cache，无法运行回测。")
        default_standard_eligible_codes = factor_cache.standard_eligible_codes_by_date.get(signal_date, [])
        default_seed_eligible_codes = factor_cache.seed_eligible_codes_by_date.get(signal_date, [])
        raw_weights = factor_cache.signal_mvs_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        standard_eligible_codes, seed_eligible_codes = resolve_strategy_listing_eligible_codes(
            prepared=prepared,
            signal_date=signal_date,
            strategy_config=strategy_config,
            default_standard_eligible_codes=default_standard_eligible_codes,
            default_seed_eligible_codes=default_seed_eligible_codes,
            available_codes=raw_weights.index,
        )
        eligible_codes = seed_eligible_codes
        avg_daily_amount = factor_cache.avg_daily_amount_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        amount_surge_ratio = factor_cache.amount_surge_ratio_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        core_signal_scores = factor_cache.core_signal_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        momentum_6_1 = factor_cache.momentum_6_1_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        momentum_3_1 = factor_cache.momentum_3_1_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        recent_1m_returns = factor_cache.recent_1m_returns_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        breakout_signal = factor_cache.breakout_signal_by_date.get(signal_date, pd.Series(dtype=bool)).copy()
        quality_scores = factor_cache.quality_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        growth_quality_scores = factor_cache.growth_quality_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        growth_acceleration_scores = factor_cache.growth_acceleration_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        industry_strength_scores = factor_cache.industry_strength_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        industry_leader_scores = factor_cache.industry_leader_scores_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        core_signal_scores = compute_core_signal_scores(
            core_signal_mode=str(strategy_config.get("core_signal_mode", "") or "").strip(),
            cached_default=core_signal_scores,
            strategy_config=strategy_config,
            momentum_6_1=momentum_6_1,
            momentum_3_1=momentum_3_1,
            recent_1m_returns=recent_1m_returns,
            amount_surge_ratio=amount_surge_ratio,
            breakout_signal=breakout_signal,
            quality_scores=quality_scores,
            growth_acceleration_scores=growth_acceleration_scores,
            industry_strength_scores=industry_strength_scores,
            industry_leader_scores=industry_leader_scores,
        )
        promotion_signal_mode = str(strategy_config.get("promotion_signal_mode", "") or "").strip()
        if promotion_signal_mode == "momentum_6_1":
            promotion_signal_scores = safe_percentile_rank(momentum_6_1, ascending=True)
        elif promotion_signal_mode == "liquidity_momentum":
            promotion_signal_scores = blend_ranked_components(
                [
                    (safe_percentile_rank(momentum_6_1, ascending=True), 0.50),
                    (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.20),
                    (safe_percentile_rank(recent_1m_returns, ascending=True), 0.15),
                    (industry_leader_scores, 0.10),
                    (breakout_signal.astype(float), 0.05),
                ]
            )
        elif promotion_signal_mode in WEEKLY_ALPHA_SIGNAL_MODES:
            promotion_signal_scores = build_weekly_alpha_scores(
                promotion_signal_mode,
                momentum_6_1=momentum_6_1,
                momentum_3_1=momentum_3_1,
                recent_1m_returns=recent_1m_returns,
                amount_surge_ratio=amount_surge_ratio,
                breakout_signal=breakout_signal,
                quality_scores=quality_scores,
                industry_strength_scores=industry_strength_scores,
                industry_leader_scores=industry_leader_scores,
            )
        elif promotion_signal_mode == EMERGENT_THEME_SIGNAL_MODE:
            promotion_signal_scores = build_emergent_theme_scores(
                momentum_6_1=momentum_6_1,
                momentum_3_1=momentum_3_1,
                recent_1m_returns=recent_1m_returns,
                amount_surge_ratio=amount_surge_ratio,
                breakout_signal=breakout_signal,
                industry_strength_scores=industry_strength_scores,
                industry_leader_scores=industry_leader_scores,
            )
        else:
            promotion_signal_scores = pd.Series(dtype=float)
        explore_signal_scores = blend_ranked_components(
            [
                (industry_strength_scores, 0.40),
                (industry_leader_scores, 0.25),
                (safe_percentile_rank(momentum_6_1, ascending=True), 0.20),
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.10),
                (breakout_signal.astype(float), 0.05),
            ]
        )
        seed_signal_scores = blend_ranked_components(
            [
                (industry_strength_scores, 0.30),
                (industry_leader_scores, 0.30),
                (safe_percentile_rank(momentum_3_1, ascending=True), 0.15),
                (safe_percentile_rank(recent_1m_returns, ascending=True), 0.10),
                (breakout_signal.astype(float), 0.10),
                (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.05),
            ]
        )
        pool_signal_scores = promotion_signal_scores if not promotion_signal_scores.empty else core_signal_scores
        actual_core_members, actual_explore_members, alpha_pool_profile = resolve_alpha_pool_universes(
            prepared=prepared,
            signal_date=signal_date,
            strategy_config=strategy_config,
            standard_eligible_codes=standard_eligible_codes,
            seed_eligible_codes=seed_eligible_codes,
            pool_signal_scores=pool_signal_scores,
        )
        core_universe_codes = set(actual_core_members) | set(promoted_core_codes)
        explore_universe_codes = set(actual_explore_members) - set(promoted_core_codes)
        strategy_kind = str(strategy_config.get("strategy_kind", "core_explore"))
        market_risk_off_rule = str(strategy_config.get("market_risk_off_rule", "or") or "or").strip().lower()
        core_risk_off_exposure = float(strategy_config.get("core_risk_off_exposure", CORE_RISK_OFF_EXPOSURE))
        core_risk_on_exposure = float(strategy_config.get("core_risk_on_exposure", CORE_RISK_ON_EXPOSURE))
        core_caution_exposure = float(strategy_config.get("core_caution_exposure", CORE_CAUTION_EXPOSURE))
        satellite_risk_off_exposure = float(strategy_config.get("satellite_risk_off_exposure", SATELLITE_RISK_OFF_EXPOSURE))
        satellite_risk_on_exposure = float(strategy_config.get("satellite_risk_on_exposure", SATELLITE_RISK_ON_EXPOSURE))
        satellite_caution_exposure = float(strategy_config.get("satellite_caution_exposure", SATELLITE_CAUTION_EXPOSURE))
        market_close_series = prepared.market_monthly_close if rebalance_frequency == "monthly" else prepared.market_weekly_close
        market_regime = compute_market_exposure(
            market_close_series,
            signal_date,
            risk_off_rule=market_risk_off_rule,
            risk_staging_mode=risk_staging_mode,
            core_risk_off_exposure=core_risk_off_exposure,
            core_risk_on_exposure=core_risk_on_exposure,
            core_caution_exposure=core_caution_exposure,
            satellite_risk_off_exposure=satellite_risk_off_exposure,
            satellite_risk_on_exposure=satellite_risk_on_exposure,
            satellite_caution_exposure=satellite_caution_exposure,
            momentum_lookback=MONTHLY_MOMENTUM_LOOKBACK if rebalance_frequency == "monthly" else WEEKLY_MOMENTUM_LOOKBACK,
            momentum_skip=MONTHLY_MOMENTUM_SKIP if rebalance_frequency == "monthly" else WEEKLY_MOMENTUM_SKIP,
            ma_lookback=MONTHLY_MA_LOOKBACK if rebalance_frequency == "monthly" else WEEKLY_MA_LOOKBACK,
        )
        if strategy_kind == "pure_core_growth":
            market_regime = {
                "risk_off": False,
                "market_12_1_momentum": np.nan,
                "market_below_10m_ma": False,
                "core_target_exposure": 1.0,
                "satellite_target_exposure": 0.0,
                "portfolio_target_exposure": 1.0,
            }
        currently_held_codes = set(positions.index)
        base_weight_method = str(strategy_config["base_weight_method"])
        if base_weight_method == "index_weight":
            base_weights = pd.concat(
                [
                    prepared.core_index_weights_by_date.get(signal_date, pd.Series(dtype=float)),
                    prepared.explore_index_weights_by_date.get(signal_date, pd.Series(dtype=float)),
                ]
            ).groupby(level=0).sum()
            base_weights = base_weights.reindex(eligible_codes).dropna()
        elif base_weight_method == "equal_weight":
            base_weights = pd.Series(1.0, index=pd.Index(eligible_codes, name="ts_code"), dtype=float)
        else:
            base_weights = raw_weights.copy()
        if strategy_kind == "pure_core_growth":
            pure_core_signal_scores = blend_ranked_components(
                [
                    (growth_acceleration_scores, 0.30),
                    (industry_strength_scores, 0.20),
                    (industry_leader_scores, 0.20),
                    (safe_percentile_rank(momentum_6_1, ascending=True), 0.10),
                    (safe_percentile_rank(momentum_3_1, ascending=True), 0.10),
                    (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.05),
                    (breakout_signal.astype(float), 0.05),
                ]
            )
            watch_pool = set(
                pure_core_signal_scores.sort_values(ascending=False).head(
                    max(1, math.ceil(int(strategy_config["pure_core_max_holdings"]) * PURE_CORE_OBSERVATION_BUFFER_MULTIPLIER))
                ).index
            )
            watch_track_codes = set(pure_core_watch_streaks) | watch_pool | currently_held_codes
            pure_core_watch_streaks = update_streak_map(
                pure_core_watch_streaks,
                positive_codes=watch_pool,
                tracked_codes=watch_track_codes,
            )
            raw_target_weights, selection_stats = build_pure_core_growth_weights(
                base_weights=base_weights.reindex(seed_eligible_codes).dropna(),
                avg_daily_amount=avg_daily_amount,
                pure_core_signal_scores=pure_core_signal_scores,
                growth_quality_scores=growth_quality_scores,
                recent_1m_returns=recent_1m_returns,
                breakout_signal=breakout_signal,
                currently_held_codes=currently_held_codes,
                core_watch_streaks=pure_core_watch_streaks,
                max_holdings=int(strategy_config["pure_core_max_holdings"]),
            )
        else:
            raw_target_weights, selection_stats = build_core_explore_target_weights(
                base_weights=base_weights,
                avg_daily_amount=avg_daily_amount,
                core_signal_scores=core_signal_scores,
                explore_signal_scores=explore_signal_scores,
                seed_signal_scores=seed_signal_scores,
                recent_1m_returns=recent_1m_returns,
                quality_scores=quality_scores,
                breakout_signal=breakout_signal,
                currently_held_codes=currently_held_codes,
                core_ratio=float(strategy_config["core_ratio"]),
                explore_ratio=float(strategy_config["explore_ratio"]),
                core_target_exposure=float(market_regime["core_target_exposure"]),
                satellite_target_exposure=float(market_regime["satellite_target_exposure"]),
                core_universe_codes=core_universe_codes,
                actual_core_members=actual_core_members,
                explore_universe_codes=explore_universe_codes,
                promoted_core_codes=promoted_core_codes,
                promoted_core_ages=promoted_core_ages,
                core_source_mode=str(strategy_config["core_source_mode"]),
                standard_eligible_codes=set(standard_eligible_codes),
                seed_eligible_codes=set(seed_eligible_codes),
                winner_core_stable_share=float(strategy_config.get("winner_core_stable_share", WINNER_CORE_STABLE_SHARE)),
                winner_core_promoted_share=float(strategy_config.get("winner_core_promoted_share", WINNER_CORE_PROMOTED_SHARE)),
                stable_core_max_holdings=int(strategy_config.get("stable_core_max_holdings", STABLE_CORE_MAX_HOLDINGS)),
                promoted_core_max_holdings=int(strategy_config.get("promoted_core_max_holdings", PROMOTED_CORE_MAX_HOLDINGS)),
                promoted_core_stage_ramp=strategy_config.get("promoted_core_stage_ramp", None),
                promoted_core_sell_exit_percentile=float(strategy_config.get("promoted_core_sell_exit_percentile", 1.0)),
                core_quality_quantile=float(strategy_config.get("core_quality_quantile", CORE_QUALITY_QUANTILE)),
                promoted_core_quality_quantile=float(strategy_config.get("promoted_core_quality_quantile", 0.40)),
                explore_quality_quantile=float(strategy_config.get("explore_quality_quantile", EXPLORE_QUALITY_QUANTILE)),
                seed_quality_quantile=float(strategy_config.get("seed_quality_quantile", SEED_QUALITY_QUANTILE)),
            )
        weight_cap = float(strategy_config.get("weight_cap", WEIGHT_CAP))
        if not np.isfinite(weight_cap) or weight_cap <= 0:
            weight_cap = WEIGHT_CAP
        weight_cap = min(1.0, weight_cap)
        target_weights, target_cash_weight = apply_weight_cap_with_redistribution(raw_target_weights, cap=weight_cap)
        core_bucket_codes = set(selection_stats.get("core_selected_codes", set())) & set(target_weights.index)
        satellite_bucket_codes = (
            set(selection_stats.get("explore_selected_codes", set())) | set(selection_stats.get("seed_selected_codes", set()))
        ) & set(target_weights.index)

        satellite_signal_ranks = blend_ranked_components(
            [
                (safe_percentile_rank(explore_signal_scores, ascending=True), 0.60),
                (safe_percentile_rank(seed_signal_scores, ascending=True), 0.40),
            ]
        )
        if not promotion_signal_scores.empty:
            satellite_signal_ranks = promotion_signal_scores
        promotion_momentum_6_1_rank = safe_percentile_rank(momentum_6_1, ascending=True).reindex(satellite_signal_ranks.index).fillna(0.0)
        promotion_momentum_3_1_rank = safe_percentile_rank(momentum_3_1, ascending=True).reindex(satellite_signal_ranks.index).fillna(0.0)
        standard_promotion_min_industry_strength = float(strategy_config.get("standard_promotion_min_industry_strength", 0.60))
        standard_promotion_min_industry_leader = float(strategy_config.get("standard_promotion_min_industry_leader", 0.60))
        standard_promotion_min_momentum_6_1_rank = float(strategy_config.get("standard_promotion_min_momentum_6_1_rank", 0.0))
        standard_promotion_min_momentum_3_1_rank = float(strategy_config.get("standard_promotion_min_momentum_3_1_rank", 0.0))
        standard_promotion_percentile = float(strategy_config.get("standard_promotion_percentile", 1.0))
        standard_promotion_percentile = min(1.0, max(0.0001, standard_promotion_percentile))
        standard_promotion_rank_threshold = satellite_signal_ranks.quantile(1.0 - standard_promotion_percentile)
        fast_promotion_percentile = float(strategy_config.get("fast_promotion_percentile", FAST_PROMOTION_PERCENTILE))
        fast_promotion_percentile = min(1.0, max(0.0001, fast_promotion_percentile))
        fast_promotion_min_industry_strength = float(strategy_config.get("fast_promotion_min_industry_strength", 0.75))
        fast_promotion_min_industry_leader = float(strategy_config.get("fast_promotion_min_industry_leader", 0.75))
        fast_promotion_min_momentum_6_1_rank = float(strategy_config.get("fast_promotion_min_momentum_6_1_rank", 0.0))
        fast_promotion_min_momentum_3_1_rank = float(strategy_config.get("fast_promotion_min_momentum_3_1_rank", 0.0))
        fast_promotion_min_recent_1m_return = float(strategy_config.get("fast_promotion_min_recent_1m_return", 0.0))
        fast_promotion_min_amount_surge_ratio = float(
            strategy_config.get("fast_promotion_min_amount_surge_ratio", FAST_PROMOTION_AMOUNT_SURGE_RATIO)
        )
        standard_promotion_candidates = set(
            satellite_signal_ranks[
                (satellite_signal_ranks >= standard_promotion_rank_threshold)
                &
                (industry_strength_scores.reindex(satellite_signal_ranks.index).fillna(0.0) >= standard_promotion_min_industry_strength)
                & (industry_leader_scores.reindex(satellite_signal_ranks.index).fillna(0.0) >= standard_promotion_min_industry_leader)
                & (promotion_momentum_6_1_rank >= standard_promotion_min_momentum_6_1_rank)
                & (promotion_momentum_3_1_rank >= standard_promotion_min_momentum_3_1_rank)
            ].index
        )
        fast_promotion_candidates = set(
            satellite_signal_ranks[
                (satellite_signal_ranks >= satellite_signal_ranks.quantile(1.0 - fast_promotion_percentile))
                & (industry_strength_scores.reindex(satellite_signal_ranks.index).fillna(0.0) >= fast_promotion_min_industry_strength)
                & (industry_leader_scores.reindex(satellite_signal_ranks.index).fillna(0.0) >= fast_promotion_min_industry_leader)
                & (promotion_momentum_6_1_rank >= fast_promotion_min_momentum_6_1_rank)
                & (promotion_momentum_3_1_rank >= fast_promotion_min_momentum_3_1_rank)
                & breakout_signal.reindex(satellite_signal_ranks.index).fillna(False)
                & (recent_1m_returns.reindex(satellite_signal_ranks.index).fillna(-1.0) > fast_promotion_min_recent_1m_return)
                & (amount_surge_ratio.reindex(satellite_signal_ranks.index).fillna(0.0) >= fast_promotion_min_amount_surge_ratio)
            ].index
        )

        if strategy_kind == "pure_core_growth":
            promotion_status = {"promoted_core_count": 0, "newly_promoted_count": 0, "fast_promoted_count": 0, "demoted_count": 0}
        else:
            promoted_core_codes, promoted_core_ages, promotion_streaks, demotion_streaks, promotion_status = update_promoted_core_state(
                promoted_core_codes=promoted_core_codes,
                promoted_core_ages=promoted_core_ages,
                promotion_streaks=promotion_streaks,
                demotion_streaks=demotion_streaks,
                standard_promotion_candidates=standard_promotion_candidates,
                core_selected_codes=set(selection_stats["core_selected_codes"]),
                avg_daily_amount=avg_daily_amount,
                actual_core_members=actual_core_members,
                fast_promotion_candidates=fast_promotion_candidates,
            )

        nav_at_signal_date = float(positions.sum() + cash_value)
        weekly_constraint_stats: Dict[str, object] = {
            "weekly_min_hold_periods": 0,
            "weekly_min_hold_protected_count": 0,
            "weekly_turnover_cap": np.nan,
            "weekly_turnover_cap_applied": False,
            "weekly_turnover_cap_scale": 1.0,
            "weekly_target_one_way_turnover_before_cap": 0.0,
            "weekly_constraint_deleveraging_bypass": False,
        }
        if rebalance_frequency == "weekly":
            current_weights_at_signal = positions / nav_at_signal_date if nav_at_signal_date > 0 and not positions.empty else pd.Series(dtype=float)
            target_weights, target_cash_weight, weekly_constraint_stats = apply_weekly_rebalance_constraints(
                target_weights=target_weights,
                current_weights=current_weights_at_signal,
                holding_ages=holding_ages,
                strategy_config=strategy_config,
            )

        candidate_code_sets = [
            set(selection_stats.get(key, set()) or set())
            for key in (
                "core_buy_candidates",
                "stable_core_buy_candidates",
                "promoted_core_buy_candidates",
                "explore_buy_candidates",
                "seed_buy_candidates",
                "core_keep_candidates",
                "stable_core_keep_candidates",
                "promoted_core_keep_candidates",
                "explore_keep_candidates",
                "seed_keep_candidates",
            )
        ]
        buy_candidate_codes = set().union(
            *[
                set(selection_stats.get(key, set()) or set())
                for key in (
                    "core_buy_candidates",
                    "stable_core_buy_candidates",
                    "promoted_core_buy_candidates",
                    "explore_buy_candidates",
                    "seed_buy_candidates",
                )
            ]
        )
        keep_candidate_codes = set().union(
            *[
                set(selection_stats.get(key, set()) or set())
                for key in (
                    "core_keep_candidates",
                    "stable_core_keep_candidates",
                    "promoted_core_keep_candidates",
                    "explore_keep_candidates",
                    "seed_keep_candidates",
                )
            ]
        )
        diagnostic_codes = set(map(str, target_weights.index)) | set(map(str, currently_held_codes)) | set().union(*candidate_code_sets)
        bucket_by_code: Dict[str, str] = {}
        for bucket_name, keys in (
            ("稳定核心", ("stable_core_selected_codes", "stable_core_buy_candidates", "stable_core_keep_candidates")),
            ("晋升核心", ("promoted_core_selected_codes", "promoted_core_buy_candidates", "promoted_core_keep_candidates")),
            ("探索仓", ("explore_selected_codes", "explore_buy_candidates", "explore_keep_candidates")),
            ("种子仓", ("seed_selected_codes", "seed_buy_candidates", "seed_keep_candidates")),
            ("核心仓", ("core_selected_codes", "core_buy_candidates", "core_keep_candidates")),
        ):
            for key in keys:
                for code in selection_stats.get(key, set()) or set():
                    bucket_by_code.setdefault(str(code), bucket_name)
        signal_components = [core_signal_scores, explore_signal_scores, seed_signal_scores]
        if strategy_kind == "pure_core_growth":
            signal_components = [pure_core_signal_scores]
        elif not promotion_signal_scores.empty:
            signal_components.append(promotion_signal_scores)
        diagnostic_signal_scores = (
            pd.concat([series for series in signal_components if not series.empty]).groupby(level=0).max()
            if any(not series.empty for series in signal_components)
            else pd.Series(dtype=float)
        )
        selection_diagnostics = build_stock_selection_diagnostics(
            codes=diagnostic_codes,
            target_weights=target_weights,
            signal_scores=diagnostic_signal_scores,
            selected_codes=set(map(str, target_weights.index)),
            buy_candidates=buy_candidate_codes,
            keep_candidates=keep_candidate_codes,
            protected_keep_candidates=set(selection_stats.get("core_protected_keep_candidates", set()) or set()),
            bucket_by_code=bucket_by_code,
            momentum_6_1=momentum_6_1,
            momentum_3_1=momentum_3_1,
            recent_1m_returns=recent_1m_returns,
            avg_daily_amount=avg_daily_amount,
            amount_surge_ratio=amount_surge_ratio,
            liquidity_scores=safe_percentile_rank(avg_daily_amount, ascending=True),
            quality_scores=quality_scores,
            industry_strength_scores=industry_strength_scores,
            industry_leader_scores=industry_leader_scores,
            breakout_signal=breakout_signal,
            risk_stage=str(market_regime.get("risk_stage") or ("risk_off" if market_regime.get("risk_off") else "risk_on")),
            raw_risk_stage=str(market_regime.get("raw_risk_stage") or ""),
            market_risk_off=bool(market_regime.get("risk_off")),
            market_momentum=_diagnostic_float(market_regime.get("market_12_1_momentum")),
            target_total_exposure=float(target_weights.sum()) if not target_weights.empty else 0.0,
        )

        if not positions.empty:
            current_price_rebalance = price_ffill.loc[rebalance_date, positions.index]
            signal_price_for_positions = price_ffill.loc[signal_date, positions.index]
            gap_growth = current_price_rebalance / signal_price_for_positions
            positions = positions * gap_growth

        tradable_codes = []
        if rebalance_date in price_exact.index:
            exact_rebalance_prices = price_exact.loc[rebalance_date]
            tradable_codes = exact_rebalance_prices[exact_rebalance_prices.notna()].index.tolist()
        else:
            warnings.append(f"{rebalance_date.date()} 不在价格面板中，当月视为无法交易，仅按持仓估值。")

        positions, cash_value, gross_positions, gross_cash_value, trade_stats = compute_rebalance_trades(
            current_values=positions,
            current_cash=cash_value,
            target_weights=target_weights,
            rebalance_date=rebalance_date,
            tradable_codes=tradable_codes,
        )
        positions, cash_value, gross_positions, gross_cash_value, weekly_overlay_turnover_rows, weekly_overlay_stats, overlay_state = apply_weekly_satellite_risk_overlay(
            prepared=prepared,
            positions=positions,
            cash_value=cash_value,
            gross_positions=gross_positions,
            gross_cash_value=gross_cash_value,
            rebalance_date=rebalance_date,
            holding_month_end=holding_period_end,
            base_target_weights=target_weights,
            core_codes=core_bucket_codes,
            satellite_codes=satellite_bucket_codes,
            strategy_config=strategy_config,
            overlay_state=overlay_state,
        )
        if risk_evaluation_frequency != RISK_EVAL_FREQUENCY_WEEKLY:
            positions, cash_value, gross_positions, gross_cash_value, drawdown_guard_turnover_rows, drawdown_guard_stats, drawdown_guard_state = apply_portfolio_drawdown_guard(
                prepared=prepared,
                positions=positions,
                cash_value=cash_value,
                gross_positions=gross_positions,
                gross_cash_value=gross_cash_value,
                rebalance_date=rebalance_date,
                holding_period_end=holding_period_end,
                base_target_weights=target_weights,
                strategy_config=strategy_config,
                guard_state=drawdown_guard_state,
            )
        else:
            drawdown_guard_turnover_rows = []
            drawdown_guard_stats = {
                "portfolio_guard_trade_count": 0,
                "portfolio_guard_trading_cost": 0.0,
                "portfolio_guard_avg_one_way_turnover": 0.0,
            }

        nav_end = float(positions.sum() + cash_value)
        holding_ages = {str(code): holding_ages.get(str(code), 0) + 1 for code in positions.index}
        if nav_end > 0:
            if not positions.empty:
                month_weights = (positions / nav_end).sort_values(ascending=False)
                for ts_code, weight in month_weights.items():
                    weights_history_rows.append(
                        enrich_with_selection_diagnostics(
                            {
                                "date": holding_period_end,
                                "ts_code": ts_code,
                                "name": prepared.code_to_name.get(ts_code, ""),
                                "weight": float(weight),
                            },
                            selection_diagnostics,
                            str(ts_code),
                        )
                    )
            cash_weight = float(cash_value / nav_end)
            if cash_weight > 1e-12:
                weights_history_rows.append(
                    {
                        "date": holding_period_end,
                        "ts_code": "CASH",
                        "name": "现金",
                        "weight": cash_weight,
                    }
                )
        gross_nav = float(gross_positions.sum() + gross_cash_value)
        gross_return = gross_nav / nav_at_signal_date - 1 if nav_at_signal_date > 0 else np.nan
        net_return = nav_end / nav_at_signal_date - 1 if nav_at_signal_date > 0 else np.nan

        monthly_rows.append(
            {
                "date": holding_period_end,
                "portfolio_return": net_return,
                "gross_return": gross_return,
                "net_return": net_return,
                "trading_cost": trade_stats["trading_cost"],
                "eligible_count": len(eligible_codes),
                "base_weight_method": str(strategy_config["base_weight_method"]),
                "core_source_mode": str(strategy_config["core_source_mode"]),
                "core_index_member_count": len(actual_core_members),
                "explore_index_member_count": len(actual_explore_members),
                "promoted_core_count": promotion_status["promoted_core_count"],
                "newly_promoted_count": promotion_status["newly_promoted_count"],
                "fast_promoted_count": promotion_status["fast_promoted_count"],
                "demoted_count": promotion_status["demoted_count"],
                "core_available_count": selection_stats["core_available_count"],
                "stable_core_available_count": selection_stats.get("stable_core_available_count", 0),
                "promoted_core_available_count": selection_stats.get("promoted_core_available_count", 0),
                "explore_available_count": selection_stats["explore_available_count"],
                "seed_available_count": selection_stats["seed_available_count"],
                "core_selected_count": selection_stats["core_selected_count"],
                "stable_core_selected_count": selection_stats.get("stable_core_selected_count", 0),
                "promoted_core_selected_count": selection_stats.get("promoted_core_selected_count", 0),
                "explore_selected_count": selection_stats["explore_selected_count"],
                "seed_selected_count": selection_stats["seed_selected_count"],
                "core_buy_candidate_count": selection_stats["core_buy_candidate_count"],
                "stable_core_buy_candidate_count": selection_stats.get("stable_core_buy_candidate_count", 0),
                "promoted_core_buy_candidate_count": selection_stats.get("promoted_core_buy_candidate_count", 0),
                "explore_buy_candidate_count": selection_stats["explore_buy_candidate_count"],
                "seed_buy_candidate_count": selection_stats["seed_buy_candidate_count"],
                "core_keep_candidate_count": selection_stats["core_keep_candidate_count"],
                "stable_core_keep_candidate_count": selection_stats.get("stable_core_keep_candidate_count", 0),
                "promoted_core_keep_candidate_count": selection_stats.get("promoted_core_keep_candidate_count", 0),
                "explore_keep_candidate_count": selection_stats["explore_keep_candidate_count"],
                "seed_keep_candidate_count": selection_stats["seed_keep_candidate_count"],
                "core_protected_keep_candidate_count": len(selection_stats["core_protected_keep_candidates"]),
                "core_quality_pass_count": selection_stats["core_quality_pass_count"],
                "stable_core_quality_pass_count": selection_stats.get("stable_core_quality_pass_count", 0),
                "promoted_core_quality_pass_count": selection_stats.get("promoted_core_quality_pass_count", 0),
                "explore_quality_pass_count": selection_stats["explore_quality_pass_count"],
                "seed_quality_pass_count": selection_stats["seed_quality_pass_count"],
                "core_watch_candidate_count": len(selection_stats.get("core_watch_candidates", set())),
                "core_watch_ready_count": len(selection_stats.get("core_watch_ready_candidates", set())),
                "market_exposure_target": float(market_regime["core_target_exposure"]) * float(strategy_config["core_ratio"])
                + float(market_regime["satellite_target_exposure"]) * float(strategy_config["explore_ratio"]),
                "core_exposure_target": market_regime["core_target_exposure"],
                "satellite_exposure_target": market_regime["satellite_target_exposure"],
                "pure_core_top3_weight_pre_cap": selection_stats.get("pure_core_top3_weight_pre_cap", np.nan),
                "market_risk_off": bool(market_regime["risk_off"]),
                "market_12_1_momentum": market_regime["market_12_1_momentum"],
                "cash_weight_target": target_cash_weight,
                "weekly_min_hold_periods": weekly_constraint_stats["weekly_min_hold_periods"],
                "weekly_min_hold_protected_count": weekly_constraint_stats["weekly_min_hold_protected_count"],
                "weekly_turnover_cap": weekly_constraint_stats["weekly_turnover_cap"],
                "weekly_turnover_cap_applied": weekly_constraint_stats["weekly_turnover_cap_applied"],
                "weekly_turnover_cap_scale": weekly_constraint_stats["weekly_turnover_cap_scale"],
                "weekly_target_one_way_turnover_before_cap": weekly_constraint_stats["weekly_target_one_way_turnover_before_cap"],
                "weekly_constraint_deleveraging_bypass": weekly_constraint_stats["weekly_constraint_deleveraging_bypass"],
                "cash_after_trade": trade_stats["cash_after_trade"],
                "weekly_overlay_trade_count": weekly_overlay_stats["weekly_overlay_trade_count"],
                "weekly_overlay_trading_cost": weekly_overlay_stats["weekly_overlay_trading_cost"],
                "weekly_overlay_avg_one_way_turnover": weekly_overlay_stats["weekly_overlay_avg_one_way_turnover"],
                "portfolio_guard_trade_count": drawdown_guard_stats["portfolio_guard_trade_count"],
                "portfolio_guard_trading_cost": drawdown_guard_stats["portfolio_guard_trading_cost"],
                "portfolio_guard_avg_one_way_turnover": drawdown_guard_stats["portfolio_guard_avg_one_way_turnover"],
            }
        )
        trade_details = []
        for detail in trade_stats.get("trade_details", []):
            detail_row = dict(detail)
            ts_code = str(detail_row.get("ts_code") or "")
            detail_row["name"] = prepared.code_to_name.get(ts_code, "")
            enrich_with_selection_diagnostics(detail_row, selection_diagnostics, ts_code)
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
                "event_type": "monthly_rebalance",
                "trade_details_json": json.dumps(trade_details, ensure_ascii=False) if trade_details else "",
            }
        )
        turnover_rows.extend(weekly_overlay_turnover_rows)
        turnover_rows.extend(drawdown_guard_turnover_rows)
        equity_rows.append(
            {
                "date": holding_period_end,
                "portfolio_return": net_return,
                "nav": nav_end,
                "drawdown": 0.0,
                "trading_cost": trade_stats["trading_cost"],
            }
        )
        realized_schedule_end = holding_period_end

    equity_curve = pd.DataFrame(equity_rows)
    equity_curve["date"] = pd.to_datetime(equity_curve["date"])
    equity_curve["nav"] = equity_curve["nav"].astype(float)
    equity_curve["cummax"] = equity_curve["nav"].cummax()
    equity_curve["drawdown"] = equity_curve["nav"] / equity_curve["cummax"] - 1.0
    equity_curve = equity_curve.drop(columns=["cummax"])

    monthly_returns = pd.DataFrame(monthly_rows)
    monthly_returns["date"] = pd.to_datetime(monthly_returns["date"])
    turnover = pd.DataFrame(turnover_rows)
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
    )

    metrics = compute_metrics(equity_curve, monthly_returns, turnover, rebalance_frequency=rebalance_frequency)
    latest_formal_signal_date = None
    if rebalance_frequency == "monthly":
        formal_signal_dates = [date for date in prepared.month_end_dates if date <= realized_schedule_end]
        latest_formal_signal_date = formal_signal_dates[-1] if formal_signal_dates else None
    is_provisional_period_end = (
        rebalance_frequency == "monthly"
        and latest_formal_signal_date is not None
        and realized_schedule_end > latest_formal_signal_date
    )
    month_end_preview = (
        build_month_end_preview_payload(
            prepared=prepared,
            strategy_config=strategy_config,
            signal_date=realized_schedule_end,
            formal_signal_date=latest_formal_signal_date,
            positions=positions,
            promoted_core_codes=promoted_core_codes,
            promoted_core_ages=promoted_core_ages,
            pure_core_watch_streaks=pure_core_watch_streaks,
        )
        if is_provisional_period_end
        else None
    )

    latest_weights = pd.DataFrame(columns=["ts_code", "name", "weight"])
    latest_nav = float(positions.sum() + cash_value)
    if latest_nav > 0 and not positions.empty:
        latest_weights = (
            (positions / latest_nav)
            .sort_values(ascending=False)
            .rename("weight")
            .reset_index()
            .rename(columns={"index": "ts_code"})
        )
        latest_weights["name"] = latest_weights["ts_code"].map(prepared.code_to_name)
        extra_cols = [col for col in SELECTION_DIAGNOSTIC_COLUMNS if col in weights_history.columns]
        if extra_cols and not weights_history.empty:
            latest_date = weights_history["date"].max()
            latest_diag = weights_history.loc[weights_history["date"] == latest_date, ["ts_code", *extra_cols]]
            latest_weights = latest_weights.merge(latest_diag, on="ts_code", how="left")
        latest_weights = latest_weights[["ts_code", "name", "weight", *[col for col in extra_cols if col in latest_weights.columns]]]

    strategy_kind = str(strategy_config.get("strategy_kind", "core_explore"))
    alpha_pool_profile = get_strategy_alpha_pool_profile(strategy_config)
    core_min_listing_months, seed_min_listing_months = get_strategy_listing_months(strategy_config)
    if strategy_kind == "pure_core_growth":
        selection_overlay = (
            "纯核心成长模式：关闭市场风控与探索/种子层，直接在动态发现池内做核心股优选；"
            "允许上市满6个月、流动性达标的股票进入候选，核心信号更强调业绩加速、行业相对强度、行业内龙头地位与持续放量突破；"
            "新增候选核心观察期，先连续观察再正式纳入核心，核心持仓数收敛到少数股票，前3大显著集中，目标是更早、更重地抓住高速成长股。"
        )
        listing_filter = "上市满 6 个月"
        momentum_lookback_rule = "使用业绩加速、行业相对强度、行业内龙头、6-1/3-1 动量与持续放量突破的复合信号"
    elif alpha_pool_profile == ALPHA_POOL_PROFILE_GROWTH_ELASTIC:
        selection_overlay = (
            "Path2 高弹性赢家池：不再沿用 Path1/3 的指数核心-探索池，改在可交易 A 股范围内按上市与流动性过滤后，"
            "用 6-1/3-1 动量、放量、突破、行业强度与龙头分筛选高弹性赢家；探索/种子胜出者再通过晋升状态机进入核心仓。"
        )
        listing_filter = f"核心/探索层上市满 {core_min_listing_months} 个月；种子层上市满 {seed_min_listing_months} 个月"
        momentum_lookback_rule = "高弹性池优先使用 6-1、3-1、近 1 月收益、放量和突破信号，晋升核心侧重流动性动量确认"
    elif alpha_pool_profile == ALPHA_POOL_PROFILE_EMERGENT_THEME:
        selection_overlay = (
            "Path4 新兴主题发现池：不再受 Path1/3 的核心/探索指数成员限制，先在可交易 A 股中用行业强度、主题内龙头、"
            "3-1 动量、近 1 月收益、放量和突破构造主题涌现信号，再分配到稳定核心、探索、种子与晋升核心。"
        )
        listing_filter = f"核心/探索层上市满 {core_min_listing_months} 个月；种子层上市满 {seed_min_listing_months} 个月"
        momentum_lookback_rule = "主题池优先使用行业强度、行业内龙头、3-1 动量、近 1 月收益、放量与突破的 emergent_theme 信号"
    else:
        selection_overlay = (
            "核心池=沪深300+科创50，探索池=中证500+科创100+科创200；在探索层内再切出种子层做更早期发现。"
            "核心层用 12-1 动量，探索/种子层加入行业强度、行业内龙头、6-1 + 3-1 与突破信号，种子层允许 6 个月以上上市且质量缺口按中性处理；"
            "探索/种子胜出者通过普通晋升和快速晋升双轨进入 winner_core，晋升后按阶段逐步加仓；核心仓再拆成稳定核心和晋升核心。"
        )
        listing_filter = f"核心/探索层上市满 {core_min_listing_months} 个月；种子层上市满 {seed_min_listing_months} 个月"
        momentum_lookback_rule = "核心层优先使用 12-1 动量；探索/种子层使用 6-1、3-1 与 20 日突破的组合信号"

    summary = {
        "sample_start": sample_start.strftime("%Y-%m-%d"),
        "sample_end": realized_schedule_end.strftime("%Y-%m-%d"),
        "latest_valuation_date": realized_schedule_end.strftime("%Y-%m-%d"),
        "latest_formal_signal_date": latest_formal_signal_date.strftime("%Y-%m-%d") if latest_formal_signal_date is not None else None,
        "is_provisional_period_end": bool(is_provisional_period_end),
        "month_end_preview": month_end_preview or {},
        "sample_tag": sample_tag,
        "sample_label": sample_label,
        "sample_short_label": sample_short_label,
        "is_primary_sample": is_primary_sample,
        "stock_count": len(prepared.code_to_name),
        "strategy_name": str(strategy_config["strategy_name"]),
        "strategy_id": str(strategy_config["strategy_id"]),
        "strategy_base_name": str(strategy_config.get("strategy_base_name", strategy_config["strategy_name"])),
        "strategy_base_id": str(strategy_config.get("strategy_base_id", strategy_config["strategy_id"])),
        "strategy_kind": strategy_kind,
        "alpha_pool_profile": alpha_pool_profile,
        "base_weight_method": str(strategy_config["base_weight_method"]),
        "base_weight_name": str(strategy_config["base_weight_name"]),
        "core_source_mode": str(strategy_config["core_source_mode"]),
        "core_source_name": str(strategy_config["core_source_name"]),
        "rebalance_frequency": rebalance_frequency,
        "weekly_min_hold_periods": int(strategy_config.get("weekly_min_hold_periods", 0) or 0),
        "weekly_turnover_cap": float(strategy_config.get("weekly_turnover_cap", np.nan) or np.nan),
        "signal_date_rule": (
            "正式月度信号仅使用完整月份的最后一个交易日；若回测截止在月中，最新交易日只作为估值终点，不产生新的月度换股信号"
            if rebalance_frequency == "monthly"
            else ("使用每两周最后一个交易日的信号点与最新前复权价格" if rebalance_frequency == "biweekly" else "使用每周最后一个交易日的信号点与最新前复权价格")
        ),
        "execution_rule": (
            "在下一个交易月第一个交易日扣除交易费用并切换到目标权重"
            if rebalance_frequency == "monthly"
            else "在信号日后的下一个交易日扣除交易费用并切换到目标权重"
        ),
        "weekly_overlay_execution_rule": "周度 overlay 使用周度收盘状态生成信号，并在信号日后的下一个交易日扣除交易费用并切换到目标仓位",
        "selection_overlay": selection_overlay,
        "price_rule": "前复权收盘价 = close * adj_factor / latest_adj_factor",
        "listing_filter": listing_filter,
        "core_min_listing_months": core_min_listing_months,
        "seed_min_listing_months": seed_min_listing_months,
        "weight_cap": float(strategy_config.get("weight_cap", WEIGHT_CAP)),
        "enhancement_bucket_pct": ENHANCEMENT_BUCKET_PCT,
        "momentum_lookback_rule": momentum_lookback_rule,
        "core_ratio": float(strategy_config["core_ratio"]),
        "explore_ratio": float(strategy_config["explore_ratio"]),
        "seed_max_portfolio_ratio": SEED_MAX_PORTFOLIO_RATIO,
        "seed_ratio": min(float(strategy_config["explore_ratio"]), SEED_MAX_PORTFOLIO_RATIO),
        "explore_main_ratio": max(
            0.0,
            float(strategy_config["explore_ratio"]) - min(float(strategy_config["explore_ratio"]), SEED_MAX_PORTFOLIO_RATIO),
        ),
        "pure_core_max_holdings": int(strategy_config.get("pure_core_max_holdings", 0)),
        "core_index_codes": CORE_INDEX_CODES,
        "explore_index_codes": EXPLORE_INDEX_CODES,
        "core_amount_threshold": CORE_AMOUNT_THRESHOLD,
        "explore_amount_threshold": EXPLORE_AMOUNT_THRESHOLD,
        "seed_amount_threshold": SEED_AMOUNT_THRESHOLD,
        "rolling_amount_window": ROLLING_AMOUNT_WINDOW,
        "promotion_min_streak": PROMOTION_MIN_STREAK,
        "demotion_min_streak": DEMOTION_MIN_STREAK,
        "promoted_core_demotion_min_streak": PROMOTED_CORE_DEMOTION_MIN_STREAK,
        "fast_promotion_min_streak": FAST_PROMOTION_MIN_STREAK,
        "fast_promotion_percentile": FAST_PROMOTION_PERCENTILE,
        "fast_promotion_amount_surge_ratio": FAST_PROMOTION_AMOUNT_SURGE_RATIO,
        "promoted_core_sell_exit_percentile": PROMOTED_CORE_SELL_EXIT_PERCENTILE,
        "core_quality_quantile": float(strategy_config.get("core_quality_quantile", CORE_QUALITY_QUANTILE)),
        "promoted_core_quality_quantile": float(strategy_config.get("promoted_core_quality_quantile", 0.40)),
        "explore_quality_quantile": float(strategy_config.get("explore_quality_quantile", EXPLORE_QUALITY_QUANTILE)),
        "seed_quality_quantile": float(strategy_config.get("seed_quality_quantile", SEED_QUALITY_QUANTILE)),
        "core_max_holdings": CORE_MAX_HOLDINGS,
        "explore_max_holdings": EXPLORE_MAX_HOLDINGS,
        "seed_max_holdings": SEED_MAX_HOLDINGS,
        "winner_core_stable_share": float(strategy_config.get("winner_core_stable_share", WINNER_CORE_STABLE_SHARE)),
        "winner_core_promoted_share": float(strategy_config.get("winner_core_promoted_share", WINNER_CORE_PROMOTED_SHARE)),
        "stable_core_max_holdings": int(strategy_config.get("stable_core_max_holdings", STABLE_CORE_MAX_HOLDINGS)),
        "promoted_core_max_holdings": int(strategy_config.get("promoted_core_max_holdings", PROMOTED_CORE_MAX_HOLDINGS)),
        "promoted_core_stage_ramp": strategy_config.get("promoted_core_stage_ramp", PROMOTED_CORE_STAGE_RAMP),
        "promoted_core_sell_exit_percentile": float(strategy_config.get("promoted_core_sell_exit_percentile", 1.0)),
        "promotion_signal_mode": str(strategy_config.get("promotion_signal_mode", "") or ""),
        "standard_promotion_percentile": float(strategy_config.get("standard_promotion_percentile", 1.0)),
        "total_portfolio_max_holdings": TOTAL_PORTFOLIO_MAX_HOLDINGS,
        "total_portfolio_min_weight": TOTAL_PORTFOLIO_MIN_WEIGHT,
        "force_exit_weight_threshold": FORCE_EXIT_WEIGHT_THRESHOLD,
        "pure_core_observation_min_streak": PURE_CORE_OBSERVATION_MIN_STREAK,
        "pure_core_observation_buffer_multiplier": PURE_CORE_OBSERVATION_BUFFER_MULTIPLIER,
        "market_index_code": MARKET_INDEX_CODE,
        "market_risk_off_rule": str(strategy_config.get("market_risk_off_rule", "or") or "or").strip().lower(),
        "core_risk_off_exposure": float(strategy_config.get("core_risk_off_exposure", CORE_RISK_OFF_EXPOSURE)),
        "core_risk_on_exposure": float(strategy_config.get("core_risk_on_exposure", CORE_RISK_ON_EXPOSURE)),
        "satellite_risk_off_exposure": float(strategy_config.get("satellite_risk_off_exposure", SATELLITE_RISK_OFF_EXPOSURE)),
        "satellite_risk_on_exposure": float(strategy_config.get("satellite_risk_on_exposure", SATELLITE_RISK_ON_EXPOSURE)),
        "buy_entry_percentile": BUY_ENTRY_PERCENTILE,
        "sell_exit_percentile": SELL_EXIT_PERCENTILE,
        "min_weight_trade_threshold": MIN_WEIGHT_TRADE_THRESHOLD,
        "buy_commission": BUY_COMMISSION,
        "sell_commission": SELL_COMMISSION,
        "stamp_duty_before_2023_08_28": STAMP_DUTY_PRE_20230828,
        "stamp_duty_after_2023_08_28": STAMP_DUTY_POST_20230828,
        "transaction_cost_timing": "费用在调仓时点真实扣除；印花税仅对卖出成交额征收",
        "metrics": metrics,
        "warnings": warnings,
    }

    return equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary


def print_summary(summary: Dict[str, object], latest_weights: pd.DataFrame) -> None:
    metrics = summary["metrics"]
    print("\n===== Backtest Summary =====")
    print(f"股票池: {summary['pool_name']} ({summary['pool_id']})")
    print(f"策略名称: {summary['strategy_name']}")
    print(f"底座权重: {summary['base_weight_name']}")
    print(f"核心来源: {summary['core_source_name']}")
    print(f"样本区间: {summary['sample_start']} -> {summary['sample_end']}")
    print(f"股票数量: {summary['stock_count']}")
    print(f"最终累计收益率: {metrics['total_return']:.2%}")
    print(f"CAGR: {metrics['cagr']:.2%}")
    print(f"最大回撤: {metrics['max_drawdown']:.2%}")
    print(f"年化波动率: {metrics['annual_volatility']:.2%}")
    print(f"夏普比率: {metrics['sharpe_ratio']:.4f}")
    print(f"累计交易费用: {metrics['cumulative_trading_cost']:.6f}")
    print(f"年均换手率: {metrics['average_annual_turnover']:.2%}")
    print("\n最近一期前 20 大持仓:")
    if latest_weights.empty:
        print("无持仓，组合当前为现金。")
    else:
        print(latest_weights.head(20).to_string(index=False, float_format=lambda value: f"{value:.4%}" if value <= 1 else f"{value:.6f}"))


def _parse_csv_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def get_winner_only_base_ids() -> Set[str]:
    winner_base_ids = {WINNER_ONLY_STRATEGY_ID}
    for variant in WINNER_CORE_VARIANTS:
        winner_base_ids.add(f"{WINNER_ONLY_STRATEGY_ID}__{variant['variant_id']}")
    return winner_base_ids


def _matches_family_prefix(base_id: str, prefixes: Iterable[str]) -> bool:
    base_id = str(base_id)
    for prefix in prefixes:
        prefix_str = str(prefix)
        if base_id == prefix_str or base_id.startswith(f"{prefix_str}__"):
            return True
    return False


def get_all_generated_strategy_base_ids() -> Set[str]:
    generated_ids: Set[str] = set()
    for ratio_config in CORE_EXPLORE_RATIO_CONFIGS:
        strategy_id = str(ratio_config["strategy_id"])
        strategy_kind = str(ratio_config.get("strategy_kind", "core_explore"))
        for base_weight_config in BASE_WEIGHT_METHODS:
            base_weight_method = str(base_weight_config["base_weight_method"])
            for core_source_config in CORE_SOURCE_MODES:
                core_source_mode = str(core_source_config["core_source_mode"])
                if strategy_kind == "pure_core_growth":
                    if core_source_mode != "pure_core_growth":
                        continue
                else:
                    if core_source_mode == "pure_core_growth":
                        continue
                generated_ids.add(f"{strategy_id}_{base_weight_method}_{core_source_mode}")
    return generated_ids


def get_active_strategy_base_ids() -> Set[str]:
    active_ids = {
        base_id
        for base_id in get_all_generated_strategy_base_ids()
        if _matches_family_prefix(base_id, ACTIVE_FAMILY_BASE_PREFIXES)
    }
    winner_variant_ids = get_winner_only_base_ids()
    active_ids |= {
        base_id
        for base_id in winner_variant_ids
        if _matches_family_prefix(base_id, ACTIVE_FAMILY_BASE_PREFIXES)
    }
    active_ids |= {
        f"{base_id}{suffix}"
        for base_id in winner_variant_ids
        for suffix in WEEKLY_OVERLAY_SUFFIXES
        if _matches_family_prefix(base_id, ACTIVE_FAMILY_BASE_PREFIXES)
    }
    return active_ids


def _collect_tracked_winner_ids(payload: Dict[str, object]) -> Set[str]:
    winner_ids: Set[str] = set()

    def add_tracks(section: object) -> None:
        if not isinstance(section, dict):
            return
        tracks = section.get("tracks")
        if not isinstance(tracks, dict):
            return
        for meta in tracks.values():
            if not isinstance(meta, dict):
                continue
            strategy_id = meta.get("winner") or meta.get("strategy_base_id")
            if strategy_id:
                winner_ids.add(str(strategy_id))

    add_tracks(payload)
    for path_key in ("path2", "path3"):
        path_payload = payload.get(path_key)
        add_tracks(path_payload)
        if isinstance(path_payload, dict) and path_payload.get("strategy_base_id"):
            winner_ids.add(str(path_payload["strategy_base_id"]))
    return winner_ids


def _load_core_active_registry_ids(path: Path = CORE_ACTIVE_REGISTRY_PATH) -> Set[str]:
    if not path.exists():
        return set()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return set()
    if not isinstance(payload, dict):
        return set()
    strategy_ids: Set[str] = set()
    for bucket_key in ("strategies", "refresh_only_strategies"):
        strategies = payload.get(bucket_key, [])
        if not isinstance(strategies, list):
            continue
        strategy_ids.update(
            str(item["strategy_id"])
            for item in strategies
            if isinstance(item, dict)
            and item.get("strategy_id")
            and (item.get("active", True) or item.get("refresh_only"))
        )
    return strategy_ids


def _load_weighted_tracked_winner_ids(path: Path = existing_research_file("weighted_track_winners.json")) -> Set[str]:
    if not path.exists():
        return set()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return set()
    return _collect_tracked_winner_ids(payload if isinstance(payload, dict) else {})


def get_core_active_strategy_base_ids() -> Set[str]:
    registry_ids = _load_core_active_registry_ids()
    if registry_ids:
        return registry_ids
    return _load_weighted_tracked_winner_ids()


def get_refresh_active_strategy_base_ids() -> Set[str]:
    refresh_ids = collect_ashare_refresh_active_ids()
    if refresh_ids:
        return refresh_ids
    return get_core_active_strategy_base_ids() | _load_weighted_tracked_winner_ids()


def get_research_active_strategy_base_ids() -> Set[str]:
    return get_active_strategy_base_ids()


def get_archive_strategy_base_ids() -> Set[str]:
    active_ids = get_active_strategy_base_ids()
    archive_ids = get_all_generated_strategy_base_ids() - active_ids
    archive_ids |= {
        base_id
        for base_id in archive_ids
        if _matches_family_prefix(base_id, ARCHIVE_FAMILY_BASE_PREFIXES)
    }
    winner_variant_ids = get_winner_only_base_ids()
    archive_ids |= {
        f"{base_id}{suffix}"
        for base_id in winner_variant_ids
        for suffix in WEEKLY_OVERLAY_SUFFIXES
        if not _matches_family_prefix(base_id, ACTIVE_FAMILY_BASE_PREFIXES)
    }
    return archive_ids


def build_satellite_overlay_variants(base_id: str, base_name: str, base_config: Dict[str, object]) -> List[Dict[str, object]]:
    if str(base_config.get("strategy_kind", "core_explore")) != "core_explore":
        return []
    if str(base_config.get("core_source_mode", "")) != "winner_core":
        return []
    if str(base_config.get("base_weight_method", "")) != "total_mv":
        return []
    variants = [
        {
            **base_config,
            "strategy_base_id": f"{base_id}{SAT_WEEKLY_RISK_SUFFIX}",
            "strategy_base_name": f"{base_name}__卫星周频两档风控",
            "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_staging_mode": "two_stage",
            "risk_overlay_scope": "satellite_only",
        },
        {
            **base_config,
            "strategy_base_id": f"{base_id}{SAT_THREE_STAGE_SUFFIX}",
            "strategy_base_name": f"{base_name}__卫星周频三档风控",
            "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_staging_mode": "three_stage",
            "risk_overlay_scope": "satellite_only",
            "satellite_caution_exposure": SATELLITE_CAUTION_EXPOSURE,
        },
        {
            **base_config,
            "strategy_base_id": f"{base_id}{SAT_THREE_STAGE_BUFFERED_SUFFIX}",
            "strategy_base_name": f"{base_name}__卫星周频三档风控(双周确认)",
            "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_staging_mode": "three_stage",
            "risk_overlay_scope": "satellite_only",
            "risk_stage_buffered": True,
            "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
            "satellite_caution_exposure": SATELLITE_CAUTION_EXPOSURE,
        },
        {
            **base_config,
            "strategy_base_id": f"{base_id}{SAT_THREE_STAGE_BUFFERED_ASYM13_SUFFIX}",
            "strategy_base_name": f"{base_name}__卫星周频三档风控(快减1慢加3)",
            "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_staging_mode": "three_stage",
            "risk_overlay_scope": "satellite_only",
            "risk_stage_buffered": True,
            "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
            "risk_off_confirm_weeks": RISK_OFF_CONFIRM_WEEKS_ASYM13,
            "risk_on_confirm_weeks": RISK_ON_CONFIRM_WEEKS_ASYM13,
            "satellite_caution_exposure": SATELLITE_CAUTION_EXPOSURE,
        },
        {
            **base_config,
            "strategy_base_id": f"{base_id}{PORT_WEEKLY_EXPOSURE_SUFFIX}",
            "strategy_base_name": f"{base_name}__月度选股_周度仓位调整",
            "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_staging_mode": "three_stage",
            "risk_overlay_scope": "portfolio_only",
            "satellite_caution_exposure": SATELLITE_CAUTION_EXPOSURE,
        },
        {
            **base_config,
            "strategy_base_id": f"{base_id}{PORT_WEEKLY_EXPOSURE_BUFFERED_SUFFIX}",
            "strategy_base_name": f"{base_name}__月度选股_周度仓位调整(双周确认)",
            "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_staging_mode": "three_stage",
            "risk_overlay_scope": "portfolio_only",
            "risk_stage_buffered": True,
            "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
            "satellite_caution_exposure": SATELLITE_CAUTION_EXPOSURE,
        },
        {
            **base_config,
            "strategy_base_id": f"{base_id}{PORT_WEEKLY_EXPOSURE_BUFFERED_ASYM13_SUFFIX}",
            "strategy_base_name": f"{base_name}__月度选股_周度仓位调整(快减1慢加3)",
            "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_staging_mode": "three_stage",
            "risk_overlay_scope": "portfolio_only",
            "risk_stage_buffered": True,
            "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
            "risk_off_confirm_weeks": RISK_OFF_CONFIRM_WEEKS_ASYM13,
            "risk_on_confirm_weeks": RISK_ON_CONFIRM_WEEKS_ASYM13,
            "satellite_caution_exposure": SATELLITE_CAUTION_EXPOSURE,
        },
        {
            **base_config,
            "strategy_base_id": f"{base_id}{PORT_WEEKLY_EXPOSURE_ASYM_SUFFIX}",
            "strategy_base_name": f"{base_name}__月度选股_周度仓位调整(快减慢加)",
            "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
            "risk_staging_mode": "three_stage",
            "risk_overlay_scope": "portfolio_only",
            "weekly_portfolio_asymmetric": True,
            "weekly_portfolio_ramp_up": WEEKLY_PORTFOLIO_RAMP_UP,
            "satellite_caution_exposure": SATELLITE_CAUTION_EXPOSURE,
        },
    ]
    if str(base_config.get("variant_id", "")) in {"aggr_08_92_prom6", "aggr_10_90_prom6", "aggr_05_95_prom7"}:
        variants.append(
            {
                **base_config,
                "strategy_base_id": f"{base_id}{SAT_THREE_STAGE_BUFFERED_COST_GUARD_SUFFIX}",
                "strategy_base_name": f"{base_name}__卫星周频三档风控(成本防守)",
                "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
                "risk_staging_mode": "three_stage",
                "risk_overlay_scope": "satellite_only",
                "risk_stage_buffered": True,
                "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
                "satellite_caution_exposure": 0.55,
                "satellite_risk_off_exposure": 0.25,
                "promoted_core_sell_exit_percentile": 0.58,
            }
        )
        variants.append(
            {
                **base_config,
                "strategy_base_id": f"{base_id}{SAT_THREE_STAGE_BUFFERED_COST_GUARD_CASHGUARD_SUFFIX}",
                "strategy_base_name": f"{base_name}__卫星周频三档风控(现金成本防守)",
                "risk_evaluation_frequency": RISK_EVAL_FREQUENCY_WEEKLY,
                "risk_staging_mode": "three_stage",
                "risk_overlay_scope": "satellite_only",
                "risk_stage_buffered": True,
                "risk_stage_confirm_weeks": WEEKLY_STAGE_CONFIRM_WEEKS,
                "market_risk_off_rule": "and",
                "satellite_caution_exposure": 0.50,
                "satellite_risk_off_exposure": 0.0,
                "promoted_core_sell_exit_percentile": 0.56,
            }
        )
    return variants


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run aiinvestor backtests (supports offline cached runs).")
    parser.add_argument(
        "--sample-tags",
        default="",
        help="Comma-separated sample tags to run (default: all). Example: since_2020_01,since_2023_01",
    )
    parser.add_argument(
        "--only-base-ids",
        default="",
        help="Comma-separated strategy_base_id values to run (default: all). "
        "Example: core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp",
    )
    parser.add_argument(
        "--comparison-csv",
        default="",
        help="Optional output CSV path. When omitted, writes the standard results/*.csv files.",
    )
    parser.add_argument(
        "--end-date",
        default=pd.Timestamp.today().strftime("%Y-%m-%d"),
        help="Backtest data end date in YYYY-MM-DD format (default: today).",
    )
    parser.add_argument(
        "--winner-only",
        action="store_true",
        help="只运行当前 winner_core 候选家族（80/20 + total_mv + winner_core 及其变体）。",
    )
    parser.add_argument(
        "--family-scope",
        choices=["refresh_active", "core_active", "research_active", "active", "archive", "all"],
        default="research_active",
        help=(
            "策略家族范围：refresh_active 跑 winners/top5/core_active/live 活跃刷新集合，"
            "research_active 跑更宽的研究活跃家族，"
            "core_active 只跑动态 winner 观察池，"
            "active 作为 research_active 的兼容别名，"
            "archive 只跑归档家族，all 跑全部历史家族。"
        ),
    )
    args = parser.parse_args(argv)

    pd.options.display.float_format = lambda value: f"{value:.8f}"
    ensure_directories()
    selected_sample_tags = set(_parse_csv_list(args.sample_tags)) if args.sample_tags else set()
    selected_base_ids = set(_parse_csv_list(args.only_base_ids)) if args.only_base_ids else set()
    explicit_selected_base_ids = bool(selected_base_ids)
    if args.winner_only and not selected_base_ids:
        selected_base_ids = get_winner_only_base_ids()
    elif not selected_base_ids and args.family_scope == "refresh_active":
        selected_base_ids = get_refresh_active_strategy_base_ids()
    elif not selected_base_ids and args.family_scope == "core_active":
        selected_base_ids = get_core_active_strategy_base_ids()
    elif not selected_base_ids and args.family_scope in {"research_active", "active"}:
        selected_base_ids = get_research_active_strategy_base_ids()
    elif not selected_base_ids and args.family_scope == "archive":
        selected_base_ids = get_archive_strategy_base_ids()

    end_date = pd.Timestamp(args.end_date).normalize()
    pro = ts.pro_api(TOKEN)
    comparison_rows: List[Dict[str, object]] = []
    data_start = min(window["sample_start"] for window in BACKTEST_SAMPLE_WINDOWS)
    prepared = prepare_data(pro, data_start, end_date)
    comparison_csv = Path(args.comparison_csv).expanduser() if args.comparison_csv else None

    sample_windows = (
        [window for window in BACKTEST_SAMPLE_WINDOWS if window["sample_tag"] in selected_sample_tags]
        if selected_sample_tags
        else list(BACKTEST_SAMPLE_WINDOWS)
    )

    for sample_window in sample_windows:
        for core_source_config in CORE_SOURCE_MODES:
            for base_weight_config in BASE_WEIGHT_METHODS:
                for ratio_config in CORE_EXPLORE_RATIO_CONFIGS:
                    ratio_strategy_kind = str(ratio_config.get("strategy_kind", "core_explore"))
                    if ratio_strategy_kind == "pure_core_growth" and core_source_config["core_source_mode"] != "pure_core_growth":
                        continue
                    if ratio_strategy_kind != "pure_core_growth" and core_source_config["core_source_mode"] == "pure_core_growth":
                        continue
                    strategy_base_id = f"{ratio_config['strategy_id']}_{base_weight_config['base_weight_method']}_{core_source_config['core_source_mode']}"
                    strategy_base_name = f"{ratio_config['strategy_name']}_{base_weight_config['base_weight_name']}_{core_source_config['core_source_name']}"
                    winner_core_variants = [
                        f"{strategy_base_id}__{variant['variant_id']}"
                        for variant in WINNER_CORE_VARIANTS
                    ]
                    satellite_overlay_variant_ids = {
                        f"{strategy_base_id}{SAT_WEEKLY_RISK_SUFFIX}",
                        f"{strategy_base_id}{SAT_THREE_STAGE_SUFFIX}",
                        f"{strategy_base_id}{SAT_THREE_STAGE_BUFFERED_SUFFIX}",
                        f"{strategy_base_id}{SAT_THREE_STAGE_BUFFERED_ASYM13_SUFFIX}",
                        f"{strategy_base_id}{PORT_WEEKLY_EXPOSURE_SUFFIX}",
                        f"{strategy_base_id}{PORT_WEEKLY_EXPOSURE_BUFFERED_SUFFIX}",
                        f"{strategy_base_id}{PORT_WEEKLY_EXPOSURE_BUFFERED_ASYM13_SUFFIX}",
                        f"{strategy_base_id}{PORT_WEEKLY_EXPOSURE_ASYM_SUFFIX}",
                    }
                    for suffix in WEEKLY_OVERLAY_SUFFIXES:
                        satellite_overlay_variant_ids.update({f"{variant_id}{suffix}" for variant_id in winner_core_variants})
                    should_consider_base = not selected_base_ids or (
                        strategy_base_id in selected_base_ids
                        or any(variant_id in selected_base_ids for variant_id in winner_core_variants)
                        or any(overlay_id in selected_base_ids for overlay_id in satellite_overlay_variant_ids)
                    )
                    if not should_consider_base:
                        continue
                    strategy_config = {
                        **ratio_config,
                        **base_weight_config,
                        **core_source_config,
                        **sample_window,
                        "strategy_base_id": strategy_base_id,
                        "strategy_base_name": strategy_base_name,
                        "strategy_id": f"{strategy_base_id}__{sample_window['sample_tag']}",
                        "strategy_name": f"{strategy_base_name} ({sample_window['sample_label']})",
                    }
                    if not selected_base_ids or strategy_base_id in selected_base_ids:
                        equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary = run_backtest(prepared, strategy_config)
                        apply_alpha_pool_summary(summary, strategy_config)
                        output_dir = build_pool_output_dir(strategy_base_id, str(sample_window["sample_tag"]))
                        save_outputs(equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary, output_dir)
                        print_summary(summary, latest_weights)
                        append_comparison_row(comparison_rows, summary)
                    for overlay_config in build_satellite_overlay_variants(strategy_base_id, strategy_base_name, strategy_config):
                        overlay_base_id = str(overlay_config["strategy_base_id"])
                        if selected_base_ids and overlay_base_id not in selected_base_ids:
                            continue
                        overlay_run_config = {
                            **overlay_config,
                            "strategy_id": f"{overlay_base_id}__{sample_window['sample_tag']}",
                            "strategy_name": f"{overlay_config['strategy_base_name']} ({sample_window['sample_label']})",
                        }
                        equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary = run_backtest(prepared, overlay_run_config)
                        apply_alpha_pool_summary(summary, overlay_run_config)
                        output_dir = build_pool_output_dir(overlay_base_id, str(sample_window["sample_tag"]))
                        save_outputs(equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary, output_dir)
                        print_summary(summary, latest_weights)
                        append_comparison_row(comparison_rows, summary)

                    variants_requested = any(
                        f"{strategy_base_id}__{variant['variant_id']}" in selected_base_ids
                        for variant in WINNER_CORE_VARIANTS
                    ) or any(
                        f"{strategy_base_id}__{variant['variant_id']}{suffix}" in selected_base_ids
                        for variant in WINNER_CORE_VARIANTS
                        for suffix in WEEKLY_OVERLAY_SUFFIXES
                    )
                    should_run_winner_core_variants = (
                        core_source_config["core_source_mode"] == "winner_core"
                        and (
                            (
                                not selected_base_ids
                                and base_weight_config["base_weight_method"] == "total_mv"
                                and ratio_config["strategy_id"] == "core_explore_80_20"
                            )
                            or variants_requested
                        )
                    )
                    if should_run_winner_core_variants:
                        for variant in WINNER_CORE_VARIANTS:
                            variant_base_id = f"{strategy_base_id}__{variant['variant_id']}"
                            variant_overlay_ids = {
                                f"{variant_base_id}{suffix}"
                                for suffix in WEEKLY_OVERLAY_SUFFIXES
                            }
                            if selected_base_ids and variant_base_id not in selected_base_ids and not any(
                                overlay_id in selected_base_ids for overlay_id in variant_overlay_ids
                            ):
                                continue
                            variant_base_name = f"{strategy_base_name}__{variant['variant_name']}"
                            variant_config = {
                                **strategy_config,
                                **variant,
                                "strategy_base_id": variant_base_id,
                                "strategy_base_name": variant_base_name,
                                "strategy_id": f"{variant_base_id}__{sample_window['sample_tag']}",
                                "strategy_name": f"{variant_base_name} ({sample_window['sample_label']})",
                            }
                            equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary = run_backtest(prepared, variant_config)
                            apply_alpha_pool_summary(summary, variant_config)
                            output_dir = build_pool_output_dir(variant_base_id, str(sample_window["sample_tag"]))
                            save_outputs(equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary, output_dir)
                            print_summary(summary, latest_weights)
                            append_comparison_row(comparison_rows, summary)
                            for overlay_config in build_satellite_overlay_variants(variant_base_id, variant_base_name, variant_config):
                                overlay_base_id = str(overlay_config["strategy_base_id"])
                                if selected_base_ids and overlay_base_id not in selected_base_ids:
                                    continue
                                overlay_run_config = {
                                    **overlay_config,
                                    "strategy_id": f"{overlay_base_id}__{sample_window['sample_tag']}",
                                    "strategy_name": f"{overlay_config['strategy_base_name']} ({sample_window['sample_label']})",
                                }
                                equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary = run_backtest(prepared, overlay_run_config)
                                apply_alpha_pool_summary(summary, overlay_run_config)
                                output_dir = build_pool_output_dir(overlay_base_id, str(sample_window["sample_tag"]))
                                save_outputs(equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary, output_dir)
                                print_summary(summary, latest_weights)
                                append_comparison_row(comparison_rows, summary)

    merge_existing = bool(
        explicit_selected_base_ids
        or selected_sample_tags
        or args.winner_only
        or args.family_scope in {"refresh_active", "core_active", "archive"}
    )
    save_pool_comparison(comparison_rows, comparison_csv=comparison_csv, merge_existing=merge_existing)


if __name__ == "__main__":
    main()
