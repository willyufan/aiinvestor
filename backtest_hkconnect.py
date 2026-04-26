from __future__ import annotations

import argparse
import json
import os
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

HK_RESULTS_DIR = Path("results_hkconnect")
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
HK_BUY_COMMISSION = BUY_COMMISSION
HK_SELL_COMMISSION = SELL_COMMISSION

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


def ensure_hk_directories() -> None:
    for path in [HK_RESULTS_DIR, HK_CACHE_DIR, HK_BASIC_DIR, HK_PRICE_DIR, HK_FACTOR_DIR]:
        path.mkdir(parents=True, exist_ok=True)


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
    return sorted(set(prepared.month_end_dates) | set(prepared.week_end_dates))


def get_rebalance_signal_dates(prepared: HKPreparedData, rebalance_frequency: str) -> List[pd.Timestamp]:
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
    month_end_dates, month_start_dates, week_end_dates, full_calendar_index = build_month_boundaries(calendar)
    now_local = pd.Timestamp.now(tz="Asia/Shanghai").tz_localize(None)
    today_local = now_local.normalize()
    if len(full_calendar_index) == 0:
        raise RuntimeError("港股交易日历为空，无法准备缓存。")
    if end_date.normalize() >= today_local:
        # Nightly runs happen after the close; allow using today's HK close once the
        # post-close data window has passed instead of always falling back to T-1.
        hk_post_close_ready = now_local >= (today_local + pd.Timedelta(hours=18))
        if hk_post_close_ready:
            eligible_cache_dates = [date for date in full_calendar_index if date <= today_local]
        else:
            eligible_cache_dates = [date for date in full_calendar_index if date < today_local]
        cache_target_date = eligible_cache_dates[-1] if eligible_cache_dates else full_calendar_index[-1]
    else:
        eligible_cache_dates = [date for date in full_calendar_index if date <= end_date.normalize()]
        cache_target_date = eligible_cache_dates[-1] if eligible_cache_dates else full_calendar_index[-1]

    price_frames: List[pd.DataFrame] = []
    mv_frames: List[pd.DataFrame] = []
    amount_frames: List[pd.DataFrame] = []
    fresh_codes: List[str] = []
    pending_codes: List[str] = []
    new_fetch_count = 0
    stopped_early = False
    last_attempted: str | None = None

    for idx, ts_code in enumerate(connect_codes, start=1):
        is_fresh, _latest_cached = get_hk_daily_cache_status(ts_code, cache_target_date)
        if is_fresh:
            fresh_codes.append(ts_code)
            if not warm_cache_only:
                daily = read_cached_csv(HK_PRICE_DIR / f"{ts_code}.csv", date_columns=["trade_date"])
                if not daily.empty and "forward_adj_close" in daily.columns:
                    price_frames.append(
                        daily[["trade_date", "forward_adj_close"]]
                        .rename(columns={"forward_adj_close": ts_code})
                        .set_index("trade_date")
                    )
                    if "total_mv" in daily.columns:
                        mv_frames.append(daily[["trade_date", "total_mv"]].rename(columns={"total_mv": ts_code}).set_index("trade_date"))
                    if "amount" in daily.columns:
                        amount_frames.append(daily[["trade_date", "amount"]].rename(columns={"amount": ts_code}).set_index("trade_date"))
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
        if daily.empty:
            warnings.append(f"{ts_code} 缺少 hk_daily_adj 数据，已跳过。")
            continue
        if "forward_adj_close" not in daily.columns:
            warnings.append(f"{ts_code} 无法构造前复权价格，已跳过。")
            continue
        fresh_codes.append(ts_code)
        price_frames.append(
            daily[["trade_date", "forward_adj_close"]]
            .rename(columns={"forward_adj_close": ts_code})
            .set_index("trade_date")
        )
        if "total_mv" in daily.columns:
            mv_frames.append(daily[["trade_date", "total_mv"]].rename(columns={"total_mv": ts_code}).set_index("trade_date"))
        if "amount" in daily.columns:
            amount_frames.append(daily[["trade_date", "amount"]].rename(columns={"amount": ts_code}).set_index("trade_date"))
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

        if not positions.empty:
            rebalance_prices = prepared.price_ffill.loc[rebalance_date, positions.index]
            period_end_prices = prepared.price_ffill.loc[period_end, positions.index]
            positions = positions * (period_end_prices / rebalance_prices)
        if not gross_positions.empty:
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
            }
        )
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
            }
        )
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
        "sample_tag": sample_tag,
        "sample_label": sample_label,
        "sample_short_label": sample_short_label,
        "stock_count": len(prepared.code_to_name),
        "strategy_name": str(strategy_config["strategy_name"]),
        "strategy_id": str(strategy_config["strategy_id"]),
        "path": str(strategy_config["path"]),
        "candidate_family": str(strategy_config["candidate_family"]),
        "rebalance_frequency": rebalance_frequency,
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
    return HK_RESULTS_DIR / f"{strategy_id}__{sample_tag}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="回测独立沪港通策略线（Path 1 / Path 2）")
    parser.add_argument("--start-date", default="2017-01-01")
    parser.add_argument("--end-date", default=pd.Timestamp.today().strftime("%Y-%m-%d"))
    parser.add_argument("--sample-tags", type=str, default="")
    parser.add_argument("--only-strategy-ids", type=str, default="")
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
    strategy_variants = HK_PATH1_VARIANTS + HK_PATH2_VARIANTS
    if selected_strategy_ids:
        strategy_variants = [variant for variant in strategy_variants if variant["strategy_id"] in selected_strategy_ids]

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

    comparison_df = pd.DataFrame(comparison_rows).sort_values(["sample_start", "path", "cagr"], ascending=[True, True, False])
    save_csv(comparison_df, HK_RESULTS_DIR / "strategy_comparison_hkconnect.csv")
    if skipped_runs:
        print(f"[HK] Skipped {len(skipped_runs)} runs due to insufficient observation-window rebalance points.")
    print("\n===== HK Connect Strategy Summary =====")
    print(comparison_df[["sample_tag", "path", "strategy_name", "cagr", "max_drawdown", "sharpe_ratio"]].head(20).to_string(index=False))


if __name__ == "__main__":
    main()
