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
}

VALID_MULTI_FACTOR_KEYS = frozenset(DEFAULT_MULTI_FACTOR_WEIGHTS.keys())
MARKET_INDEX_CODE = "000300.SH"
BENCHMARK_INDEX_CODE = "000001.SH"
CORE_INDEX_CODES = ["000300.SH", "000688.SH"]
EXPLORE_INDEX_CODES = ["000905.SH", "000698.SH", "000699.SH"]
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
        "variant_id": "share_12_88_hold_4_6",
        "variant_name": "比例12/88",
        "winner_core_stable_share": 0.12,
        "winner_core_promoted_share": 0.88,
        "stable_core_max_holdings": 4,
        "promoted_core_max_holdings": 6,
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
    ],
    "holding_shape": [
        "share_15_85_hold_4_6",
        "aggr_10_90_hold_4_6",
        "share_12_88_hold_4_6",
        "aggr_09_91_prom7",
        "aggr_08_92_hold_3_6",
        "aggr_08_92_hold_3_6_ramp90",
        "aggr_05_95_prom7",
    ],
    "supporting_variants": [
        "aggr_08_92_prom6",
        "aggr_08_92_prom6_ramp90",
        "aggr_08_92_prom7",
        "aggr_08_92_prom7_ramp90",
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
    "aggr_09_91_prom7",
    "share_12_88_hold_4_6",
    "aggr_08_92_hold_3_6",
    "aggr_08_92_hold_3_6_ramp90",
    "aggr_05_95_prom7",
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
        "target_candidates": 6,
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
            "aggr_05_95_prom3_core_6_1_full_risk_cap80_biweekly",
            "aggr_05_95_prom3_core_6_1_cash_off_and_cap60_biweekly",
            "aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_biweekly",
            "aggr_08_92_prom6_core_6_1_full_risk_cap40_biweekly",
            "aggr_08_92_prom6_core_6_1_full_risk_cap60_biweekly",
            "aggr_05_95_prom3_core_6_1_full_risk_cap60_biweekly",
            "aggr_08_92_prom6_cash_off_and_biweekly",
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
    "aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly",
    "aggr_05_95_prom3_core_6_1_full_risk_cap60_weekly",
    "aggr_08_92_prom6_cash_off_and_weekly",
]

FACTOR_CACHE_VERSION = "v2"
WINNER_ONLY_STRATEGY_ID = "core_explore_80_20_total_mv_winner_core"
INDEX_CORE_BASE_ID = "core_explore_80_20_total_mv_index_core"
ACTIVE_FAMILY_BASE_PREFIXES = [
    "core_explore_80_20_total_mv_index_core",
    "core_explore_80_20_total_mv_winner_core",
]
CORE_ACTIVE_REGISTRY_PATH = Path("results") / "core_active_registry.json"
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

PURE_CORE_AMOUNT_THRESHOLD = 50000.0
PURE_CORE_BUY_BUFFER_MULTIPLIER = 1.0
PURE_CORE_KEEP_BUFFER_MULTIPLIER = 2.0
PURE_CORE_OBSERVATION_BUFFER_MULTIPLIER = 3.0
PURE_CORE_OBSERVATION_MIN_STREAK = 2
PURE_CORE_BASE_WEIGHT_SHARE = 0.15
PURE_CORE_TOP3_MULTIPLIERS = [2.4, 1.8, 1.35]

CACHE_DIR = Path("data_cache")
RESULTS_DIR = Path("results")
DAILY_DIR = CACHE_DIR / "daily"
ADJ_DIR = CACHE_DIR / "adj_factor"
DAILY_BASIC_DIR = CACHE_DIR / "daily_basic"
FINA_DIR = CACHE_DIR / "fina_indicator"
INDEX_DIR = CACHE_DIR / "index_daily"
INDEX_WEIGHT_DIR = CACHE_DIR / "index_weight"
FACTOR_PANEL_DIR = CACHE_DIR / "monthly_factor_cache"
PREPARED_PANEL_DIR = CACHE_DIR / "prepared_panel_cache"
PREPARED_CACHE_VERSION = "v1"


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
    df = pd.read_csv(path)
    for column in date_columns or []:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column])
    return df


def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, float_format=FLOAT_FORMAT)


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
    if sample_tag:
        return RESULTS_DIR / f"{pool_id}__{sample_tag}"
    return RESULTS_DIR / pool_id


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


def build_month_boundaries(calendar: pd.DataFrame) -> Tuple[List[pd.Timestamp], List[pd.Timestamp], List[pd.Timestamp], pd.Index]:
    open_calendar = calendar.loc[calendar["is_open"] == 1, ["cal_date"]].copy()
    open_calendar = open_calendar.sort_values("cal_date").reset_index(drop=True)
    open_calendar["month"] = open_calendar["cal_date"].dt.to_period("M")
    open_calendar["week"] = open_calendar["cal_date"].dt.to_period("W-FRI")
    month_end_dates = open_calendar.groupby("month")["cal_date"].max().sort_values().tolist()
    month_start_dates = open_calendar.groupby("month")["cal_date"].min().sort_values().tolist()
    week_end_dates = open_calendar.groupby("week")["cal_date"].max().sort_values().tolist()
    full_calendar_index = pd.Index(open_calendar["cal_date"], name="trade_date")
    return month_end_dates, month_start_dates, week_end_dates, full_calendar_index


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
    per_stock_frames: Dict[str, Dict[str, pd.DataFrame]],
    financials_by_code: Dict[str, pd.DataFrame],
    market_index_df: pd.DataFrame,
    core_members_by_date: Dict[pd.Timestamp, Set[str]],
    explore_members_by_date: Dict[pd.Timestamp, Set[str]],
    core_index_weights_by_date: Dict[pd.Timestamp, pd.Series],
    explore_index_weights_by_date: Dict[pd.Timestamp, pd.Series],
    data_warnings: List[str],
) -> PreparedData:
    month_end_dates, month_start_dates, week_end_dates, full_calendar_index = build_month_boundaries(calendar)

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
    cache_key = "_".join(
        [
            FACTOR_CACHE_VERSION,
            prepared.month_end_dates[0].strftime("%Y%m%d"),
            prepared.month_end_dates[-1].strftime("%Y%m%d"),
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
    return list(prepared.month_end_dates)


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
    payload = pd.read_pickle(path)
    if not isinstance(payload, dict) or payload.get("version") != PREPARED_CACHE_VERSION:
        return None
    prepared = payload.get("prepared")
    if not isinstance(prepared, PreparedData):
        return None
    required_attrs = ["week_end_dates", "market_weekly_close", "month_end_dates", "price_exact", "price_ffill", "total_mv"]
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
        for ts_code in prepared.code_to_name:
            list_date = prepared.code_to_list_date[ts_code]
            if pd.isna(list_date):
                continue
            if ts_code not in signal_prices.index or pd.isna(signal_prices.get(ts_code)):
                continue
            if ts_code not in signal_mvs.index or pd.isna(signal_mvs.get(ts_code)):
                continue
            if list_date <= signal_date - pd.DateOffset(months=SEED_MIN_LISTING_MONTHS):
                seed_eligible_codes.append(ts_code)
            if list_date <= signal_date - pd.DateOffset(months=MIN_LISTING_MONTHS):
                standard_eligible_codes.append(ts_code)

        eligible_codes = seed_eligible_codes
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
        quality_quantile=CORE_QUALITY_QUANTILE,
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
        quality_quantile=0.40,
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
        quality_quantile=EXPLORE_QUALITY_QUANTILE,
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
        quality_quantile=SEED_QUALITY_QUANTILE,
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
    month_end_dates, _, week_end_dates, _ = build_month_boundaries(usable_calendar)
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
        print(f"[Cache] 已加载 prepared panel cache: {prepared_cache_path}")
        prepared_cached.core_members_by_date = core_members_by_date
        prepared_cached.explore_members_by_date = explore_members_by_date
        prepared_cached.core_index_weights_by_date = core_index_weights_by_date
        prepared_cached.explore_index_weights_by_date = explore_index_weights_by_date
        prepared_cached.month_end_dates = month_end_dates
        prepared_cached.week_end_dates = week_end_dates
        factor_cache_path = build_factor_cache_path(prepared_cached)
        monthly_factor_cache = load_monthly_factor_cache(factor_cache_path)
        if monthly_factor_cache is None:
            print("[Cache] 月度因子缓存不存在或失效，开始构建。")
            monthly_factor_cache = build_monthly_factor_cache(prepared_cached)
            save_monthly_factor_cache(monthly_factor_cache, factor_cache_path)
            print(f"[Cache] 月度因子缓存已写入: {factor_cache_path}")
        else:
            print(f"[Cache] 已加载月度因子缓存: {factor_cache_path}")
        prepared_cached.monthly_factor_cache = monthly_factor_cache
        return prepared_cached

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
        per_stock_frames,
        financials_by_code,
        market_index_df,
        core_members_by_date,
        explore_members_by_date,
        core_index_weights_by_date,
        explore_index_weights_by_date,
        data_warnings,
    )
    save_prepared_cache(prepared, prepared_cache_path)
    print(f"[Cache] prepared panel cache 已写入: {prepared_cache_path}")
    factor_cache_path = build_factor_cache_path(prepared)
    monthly_factor_cache = load_monthly_factor_cache(factor_cache_path)
    if monthly_factor_cache is None:
        print("[Cache] 月度因子缓存不存在或失效，开始构建。")
        monthly_factor_cache = build_monthly_factor_cache(prepared)
        save_monthly_factor_cache(monthly_factor_cache, factor_cache_path)
        print(f"[Cache] 月度因子缓存已写入: {factor_cache_path}")
    else:
        print(f"[Cache] 已加载月度因子缓存: {factor_cache_path}")
    prepared.monthly_factor_cache = monthly_factor_cache
    return prepared


def save_pool_comparison(comparison_rows: List[Dict[str, object]], comparison_csv: Path | None = None) -> None:
    if not comparison_rows:
        return

    comparison_df = pd.DataFrame(comparison_rows)
    if comparison_csv is None:
        save_csv(comparison_df, RESULTS_DIR / "strategy_comparison.csv")
        save_csv(comparison_df, RESULTS_DIR / "strategy_comparison_base_method.csv")
        return

    save_csv(comparison_df, comparison_csv)


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
    risk_evaluation_frequency = str(strategy_config.get("risk_evaluation_frequency", RISK_EVAL_FREQUENCY_MONTHLY) or RISK_EVAL_FREQUENCY_MONTHLY)
    risk_staging_mode = str(strategy_config.get("risk_staging_mode", "two_stage") or "two_stage").strip().lower()
    overlay_state: Dict[str, object] = {"confirmed_stage": "risk_on", "pending_stage": None, "pending_count": 0}

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
        standard_eligible_codes = factor_cache.standard_eligible_codes_by_date.get(signal_date, [])
        seed_eligible_codes = factor_cache.seed_eligible_codes_by_date.get(signal_date, [])
        eligible_codes = seed_eligible_codes
        raw_weights = factor_cache.signal_mvs_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        avg_daily_amount = factor_cache.avg_daily_amount_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        amount_surge_ratio = factor_cache.amount_surge_ratio_by_date.get(signal_date, pd.Series(dtype=float)).copy()
        actual_core_members = prepared.core_members_by_date.get(signal_date, set())
        actual_explore_members = prepared.explore_members_by_date.get(signal_date, set())
        core_universe_codes = set(actual_core_members) | set(promoted_core_codes)
        explore_universe_codes = set(actual_explore_members) - set(promoted_core_codes)
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
        core_signal_mode = str(strategy_config.get("core_signal_mode", "") or "").strip()
        if core_signal_mode == "6_1":
            core_signal_scores = momentum_6_1.copy()
        elif core_signal_mode == "3_1":
            core_signal_scores = momentum_3_1.copy()
        elif core_signal_mode == "theme":
            core_signal_scores = blend_ranked_components(
                [
                    (growth_acceleration_scores, 0.30),
                    (industry_strength_scores, 0.25),
                    (industry_leader_scores, 0.20),
                    (safe_percentile_rank(momentum_6_1, ascending=True), 0.15),
                    (safe_percentile_rank(momentum_3_1, ascending=True), 0.10),
                ]
            )
        elif core_signal_mode == "industry_trend":
            core_signal_scores = blend_ranked_components(
                [
                    (industry_strength_scores, 0.30),
                    (industry_leader_scores, 0.25),
                    (safe_percentile_rank(momentum_6_1, ascending=True), 0.25),
                    (safe_percentile_rank(momentum_3_1, ascending=True), 0.15),
                    (breakout_signal.astype(float), 0.05),
                ]
            )
        elif core_signal_mode == "midcycle_momentum":
            core_signal_scores = blend_ranked_components(
                [
                    (safe_percentile_rank(momentum_6_1, ascending=True), 0.40),
                    (safe_percentile_rank(amount_surge_ratio, ascending=True), 0.20),
                    (safe_percentile_rank(recent_1m_returns, ascending=True), 0.15),
                    (industry_leader_scores, 0.15),
                    (breakout_signal.astype(float), 0.10),
                ]
            )
        elif core_signal_mode == "multi_factor":
            factor_weights = _validated_multi_factor_weights(strategy_config.get("factor_weights"))
            core_signal_scores = blend_ranked_components(
                [
                    (safe_percentile_rank(momentum_6_1, ascending=True),     factor_weights.get("momentum_6_1", 0.0)),
                    (safe_percentile_rank(momentum_3_1, ascending=True),     factor_weights.get("momentum_3_1", 0.0)),
                    (quality_scores,                                          factor_weights.get("quality", 0.0)),
                    (growth_acceleration_scores,                              factor_weights.get("growth_acceleration", 0.0)),
                    (industry_strength_scores,                                factor_weights.get("industry_strength", 0.0)),
                    (industry_leader_scores,                                  factor_weights.get("industry_leader", 0.0)),
                    (safe_percentile_rank(amount_surge_ratio, ascending=True), factor_weights.get("liquidity_surge", 0.0)),
                ]
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
            if not positions.empty:
                rebalance_prices = price_ffill.loc[rebalance_date, positions.index]
                month_end_prices = price_ffill.loc[holding_period_end, positions.index]
                holding_growth = month_end_prices / rebalance_prices
                positions = positions * holding_growth
            if not gross_positions.empty:
                gross_rebalance_prices = price_ffill.loc[rebalance_date, gross_positions.index]
                gross_month_end_prices = price_ffill.loc[holding_period_end, gross_positions.index]
                gross_holding_growth = gross_month_end_prices / gross_rebalance_prices
                gross_positions = gross_positions * gross_holding_growth

        nav_end = float(positions.sum() + cash_value)
        if nav_end > 0:
            if not positions.empty:
                month_weights = (positions / nav_end).sort_values(ascending=False)
                for ts_code, weight in month_weights.items():
                    weights_history_rows.append(
                        {
                            "date": holding_period_end,
                            "ts_code": ts_code,
                            "name": prepared.code_to_name.get(ts_code, ""),
                            "weight": float(weight),
                        }
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
                "cash_after_trade": trade_stats["cash_after_trade"],
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
                "event_type": "monthly_rebalance",
                "trade_details_json": json.dumps(trade_details, ensure_ascii=False) if trade_details else "",
            }
        )
        turnover_rows.extend(weekly_overlay_turnover_rows)
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
        latest_weights = latest_weights[["ts_code", "name", "weight"]]

    strategy_kind = str(strategy_config.get("strategy_kind", "core_explore"))
    if strategy_kind == "pure_core_growth":
        selection_overlay = (
            "纯核心成长模式：关闭市场风控与探索/种子层，直接在动态发现池内做核心股优选；"
            "允许上市满6个月、流动性达标的股票进入候选，核心信号更强调业绩加速、行业相对强度、行业内龙头地位与持续放量突破；"
            "新增候选核心观察期，先连续观察再正式纳入核心，核心持仓数收敛到少数股票，前3大显著集中，目标是更早、更重地抓住高速成长股。"
        )
        listing_filter = "上市满 6 个月"
        momentum_lookback_rule = "使用业绩加速、行业相对强度、行业内龙头、6-1/3-1 动量与持续放量突破的复合信号"
    else:
        selection_overlay = (
            "核心池=沪深300+科创50，探索池=中证500+科创100+科创200；在探索层内再切出种子层做更早期发现。"
            "核心层用 12-1 动量，探索/种子层加入行业强度、行业内龙头、6-1 + 3-1 与突破信号，种子层允许 6 个月以上上市且质量缺口按中性处理；"
            "探索/种子胜出者通过普通晋升和快速晋升双轨进入 winner_core，晋升后按阶段逐步加仓；核心仓再拆成稳定核心和晋升核心。"
        )
        listing_filter = "核心/探索层上市满 12 个月；种子层上市满 6 个月"
        momentum_lookback_rule = "核心层优先使用 12-1 动量；探索/种子层使用 6-1、3-1 与 20 日突破的组合信号"

    summary = {
        "sample_start": sample_start.strftime("%Y-%m-%d"),
        "sample_end": realized_schedule_end.strftime("%Y-%m-%d"),
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
        "base_weight_method": str(strategy_config["base_weight_method"]),
        "base_weight_name": str(strategy_config["base_weight_name"]),
        "core_source_mode": str(strategy_config["core_source_mode"]),
        "core_source_name": str(strategy_config["core_source_name"]),
        "rebalance_frequency": rebalance_frequency,
        "signal_date_rule": (
            "使用每个月最后一个交易日的 total_mv 与前复权价格"
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


def _load_weighted_tracked_winner_ids(path: Path = RESULTS_DIR / "weighted_track_winners.json") -> Set[str]:
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
    return [
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
        choices=["core_active", "research_active", "active", "archive", "all"],
        default="research_active",
        help=(
            "策略家族范围：research_active 跑更宽的研究活跃家族，"
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
    if args.winner_only and not selected_base_ids:
        selected_base_ids = get_winner_only_base_ids()
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
                        summary["pool_id"] = "dynamic_index_core_explore_universe"
                        summary["pool_name"] = "动态指数池(核心:沪深300+科创50, 探索:中证500+科创100+科创200)"
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
                        summary["pool_id"] = "dynamic_index_core_explore_universe"
                        summary["pool_name"] = "动态指数池(核心:沪深300+科创50, 探索:中证500+科创100+科创200)"
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
                            summary["pool_id"] = "dynamic_index_core_explore_universe"
                            summary["pool_name"] = "动态指数池(核心:沪深300+科创50, 探索:中证500+科创100+科创200)"
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
                                summary["pool_id"] = "dynamic_index_core_explore_universe"
                                summary["pool_name"] = "动态指数池(核心:沪深300+科创50, 探索:中证500+科创100+科创200)"
                                output_dir = build_pool_output_dir(overlay_base_id, str(sample_window["sample_tag"]))
                                save_outputs(equity_curve, monthly_returns, annual_returns, latest_weights, weights_history, turnover, summary, output_dir)
                                print_summary(summary, latest_weights)
                                append_comparison_row(comparison_rows, summary)

    save_pool_comparison(comparison_rows, comparison_csv=comparison_csv)


if __name__ == "__main__":
    main()
