from __future__ import annotations

import functools
import json
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.results_layout import (
    RESULTS_LIVE_DIR,
    existing_research_file,
    existing_strategy_result_file,
)

LIVE_DIR = RESULTS_LIVE_DIR
TRACKED_WINNERS_JSON = existing_research_file("weighted_track_winners.json")
CORE_ACTIVE_REGISTRY_JSON = existing_research_file("core_active_registry.json")
DAILY_CACHE_DIR = ROOT / "data_cache" / "daily"
HK_DAILY_CACHE_DIR = ROOT / "data_cache" / "hkconnect" / "daily_adj"
PREPARED_PANEL_CACHE_DIR = ROOT / "data_cache" / "prepared_panel_cache"
A_SHARE_TRADE_CALENDAR_PATH = ROOT / "data_cache" / "trade_calendar.csv"
HK_TRADE_CALENDAR_PATH = ROOT / "data_cache" / "hkconnect" / "basic" / "trade_calendar_hk.csv"

SAMPLE_LABELS = {
    "since_2017_only": "2017-window winner",
    "since_2020_only": "2020-window winner",
    "since_2023_only": "2023-window winner",
    "since_2025_only": "2025-window winner",
    "since_2026_only": "2026-window winner",
    "robust_candidate": "robust candidate",
}
HISTORY_WINDOW_SNAPSHOTS = 12
SAMPLE_TAGS = ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]
A_SHARE_TRACKED_PATH_NAMES = ("path1", "path2", "path3", "path4")
A_SHARE_2026_TRACK_KEY = "since_2026_only"
A_SHARE_2026_SAMPLE_TAG = "since_2026_01"
HK_TRACKED_WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01")
HK_LEADERBOARD_WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01")
HK_TRACKED_PATH_NAMES = ("path1", "path2", "path3", "path4", "path5", "path6", "path7")
HK_EXPERIMENTAL_PATH_NAMES = ("path4", "path5", "path6", "path7")
NIGHTLY_REFRESH_SAMPLE_TAGS = {"since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"}
SAMPLE_TAG_LABELS = {
    "since_2017_01": "2017窗口",
    "since_2020_01": "2020窗口",
    "since_2023_01": "2023窗口",
    "since_2025_01": "2025窗口",
    "since_2026_01": "2026观察窗",
}
SELECTION_DIAGNOSTIC_FIELDS = [
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


def infer_adjustment_style(strategy_id: str, rebalance_frequency: str) -> str:
    strategy_id = str(strategy_id or "")
    rebalance_frequency = str(rebalance_frequency or "monthly")
    if "weekly_overlay" in strategy_id:
        return "月度换股 + 周度总仓位"
    # asym13 must be checked BEFORE the plain _buffered suffix, since it is
    # `__port_weekly_exposure_buffered_asym13` (a longer match that contains
    # the buffered prefix as a substring).
    if "__port_weekly_exposure_buffered_asym13" in strategy_id:
        return "月度换股 + 周度总仓位（快减1慢加3）"
    if "__port_weekly_exposure_buffered" in strategy_id:
        return "月度换股 + 周度总仓位（双周确认）"
    if "__port_weekly_exposure_asym" in strategy_id:
        return "月度换股 + 周度总仓位（快减慢加）"
    if "__port_weekly_exposure" in strategy_id:
        return "月度换股 + 周度总仓位"
    if "__sat_three_stage_buffered_asym13" in strategy_id:
        return "月度换股 + 周度卫星仓位（快减1慢加3）"
    if "__sat_three_stage_buffered" in strategy_id:
        return "月度换股 + 周度卫星仓位（双周确认）"
    if "__sat_three_stage_risk" in strategy_id:
        return "月度换股 + 周度卫星仓位（三档风控）"
    if "__sat_weekly_risk" in strategy_id:
        return "月度换股 + 周度卫星仓位"
    if rebalance_frequency == "biweekly":
        return "双周换股"
    if rebalance_frequency == "weekly":
        return "单周换股"
    return "月度换股"


def infer_schedule_kind(strategy_id: str, rebalance_frequency: str) -> str:
    strategy_id = str(strategy_id or "")
    rebalance_frequency = str(rebalance_frequency or "monthly")
    if "__port_weekly_exposure" in strategy_id:
        return "portfolio_weekly_overlay"
    if "__sat_" in strategy_id:
        return "satellite_weekly_overlay"
    if rebalance_frequency == "biweekly":
        return "biweekly"
    if rebalance_frequency == "weekly":
        return "weekly"
    return "monthly"


def copy_selection_diagnostics(source: dict[str, Any], target: dict[str, Any]) -> dict[str, Any]:
    for key in SELECTION_DIAGNOSTIC_FIELDS:
        if key not in source:
            continue
        value = source.get(key)
        if value is None:
            continue
        try:
            if pd.isna(value):
                continue
        except Exception:
            pass
        if hasattr(value, "item"):
            try:
                value = value.item()
            except Exception:
                pass
        target[key] = value
    return target


def is_path3_weekly_strategy(strategy_id: str) -> bool:
    return str(strategy_id or "").endswith("_weekly")


@functools.lru_cache(maxsize=4)
def load_open_trade_dates(market_scope: str) -> list[pd.Timestamp]:
    calendar_path = HK_TRADE_CALENDAR_PATH if market_scope == "hkconnect" else A_SHARE_TRADE_CALENDAR_PATH
    if not calendar_path.exists():
        return []
    try:
        frame = pd.read_csv(calendar_path)
    except Exception:
        return []
    if frame.empty or "cal_date" not in frame.columns:
        return []
    frame = frame.copy()
    frame["cal_date"] = pd.to_datetime(frame["cal_date"], errors="coerce")
    frame = frame.dropna(subset=["cal_date"])
    if "is_open" in frame.columns:
        frame = frame[frame["is_open"] == 1]
    frame = frame.sort_values("cal_date").drop_duplicates(subset=["cal_date"])
    return [pd.Timestamp(value) for value in frame["cal_date"].tolist()]


@functools.lru_cache(maxsize=4)
def build_formal_trade_boundaries(market_scope: str) -> tuple[list[pd.Timestamp], list[pd.Timestamp]]:
    open_dates = load_open_trade_dates(market_scope)
    if not open_dates:
        return [], []
    frame = pd.DataFrame({"cal_date": pd.to_datetime(open_dates)})
    frame["month"] = frame["cal_date"].dt.to_period("M")
    frame["week"] = frame["cal_date"].dt.to_period("W-FRI")
    month_end_dates = [pd.Timestamp(value) for value in frame.groupby("month")["cal_date"].max().sort_values().tolist()]
    week_end_dates = [pd.Timestamp(value) for value in frame.groupby("week")["cal_date"].max().sort_values().tolist()]
    return month_end_dates, week_end_dates


def last_date_on_or_before(dates: list[pd.Timestamp], as_of: pd.Timestamp) -> str | None:
    chosen: pd.Timestamp | None = None
    for value in dates:
        if value <= as_of:
            chosen = value
        else:
            break
    return chosen.strftime("%Y-%m-%d") if chosen is not None else None


def build_formal_schedule_meta(
    *,
    strategy_id: str,
    rebalance_frequency: str,
    sample_end: str | None,
    market_scope: str,
) -> dict[str, Any]:
    if not sample_end:
        return {}
    as_of = pd.Timestamp(sample_end)
    month_end_dates, week_end_dates = build_formal_trade_boundaries(market_scope)
    schedule_kind = infer_schedule_kind(strategy_id, rebalance_frequency)
    data_as_of = as_of.strftime("%Y-%m-%d")
    basket_effective_date = last_date_on_or_before(month_end_dates, as_of)
    weekly_effective_date = last_date_on_or_before(week_end_dates, as_of)
    biweekly_dates = [date for idx, date in enumerate(week_end_dates) if idx % 2 == 1]
    biweekly_effective_date = last_date_on_or_before(biweekly_dates, as_of)

    if schedule_kind == "monthly":
        suggestion_effective_date = basket_effective_date
        exposure_effective_date = basket_effective_date
    elif schedule_kind == "portfolio_weekly_overlay":
        suggestion_effective_date = weekly_effective_date or basket_effective_date
        exposure_effective_date = weekly_effective_date or basket_effective_date
    elif schedule_kind == "satellite_weekly_overlay":
        suggestion_effective_date = weekly_effective_date or basket_effective_date
        exposure_effective_date = weekly_effective_date or basket_effective_date
    elif schedule_kind == "biweekly":
        suggestion_effective_date = biweekly_effective_date
        basket_effective_date = biweekly_effective_date
        exposure_effective_date = biweekly_effective_date
    else:
        suggestion_effective_date = weekly_effective_date
        basket_effective_date = weekly_effective_date
        exposure_effective_date = weekly_effective_date

    return {
        "data_as_of": data_as_of,
        "schedule_kind": schedule_kind,
        "suggestion_effective_date": suggestion_effective_date,
        "basket_effective_date": basket_effective_date,
        "exposure_effective_date": exposure_effective_date,
    }


def normalize_holdings_with_cash(holdings: list[dict[str, Any]], target_exposure: float | None = None) -> list[dict[str, Any]]:
    if not holdings:
        return []
    exposure = float(target_exposure if target_exposure is not None else 1.0)
    exposure = max(0.0, min(1.0, exposure))
    non_cash = [row for row in holdings if str(row.get("ts_code")) != "CASH"]
    non_cash_total = sum(max(0.0, float(row.get("weight", 0.0))) for row in non_cash)
    latest_price_map = {str(row.get("ts_code")): row.get("latest_price") for row in holdings}
    normalized: list[dict[str, Any]] = []
    if non_cash_total > 0 and exposure > 0:
        for row in sorted(non_cash, key=lambda item: float(item.get("weight", 0.0)), reverse=True):
            base_weight = max(0.0, float(row.get("weight", 0.0)))
            normalized.append(
                copy_selection_diagnostics(
                    row,
                    {
                        "ts_code": str(row.get("ts_code")),
                        "name": str(row.get("name", "")),
                        "weight": exposure * base_weight / non_cash_total,
                        "latest_price": latest_price_map.get(str(row.get("ts_code"))),
                    },
                )
            )
    cash_weight = max(0.0, 1.0 - exposure)
    if cash_weight > 1e-12:
        normalized.append({"ts_code": "CASH", "name": "现金", "weight": cash_weight, "latest_price": None})
    return normalized


def load_weight_history_snapshot_map(path: Path) -> dict[str, list[dict[str, Any]]]:
    if not path.exists():
        return {}
    try:
        frame = pd.read_csv(path)
    except Exception:
        return {}
    required = {"date", "ts_code", "name", "weight"}
    if frame.empty or not required.issubset(frame.columns):
        return {}
    frame = frame.copy()
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame = frame.dropna(subset=["date"])
    if frame.empty:
        return {}
    snapshot_map: dict[str, list[dict[str, Any]]] = {}
    for snapshot_date, sub in frame.groupby("date", sort=False):
        snapshot_map[pd.Timestamp(snapshot_date).strftime("%Y-%m-%d")] = [
            copy_selection_diagnostics(
                row,
                {
                    "ts_code": str(row["ts_code"]),
                    "name": str(row["name"]),
                    "weight": float(row["weight"]),
                },
            )
            for row in sub.sort_values("weight", ascending=False).to_dict("records")
        ]
    return snapshot_map


def filter_snapshot_map_on_or_before(
    snapshot_map: dict[str, list[dict[str, Any]]],
    cutoff_date: str | None,
) -> dict[str, list[dict[str, Any]]]:
    if not cutoff_date:
        return dict(snapshot_map)
    try:
        cutoff = pd.Timestamp(cutoff_date)
    except Exception:
        return dict(snapshot_map)
    filtered: dict[str, list[dict[str, Any]]] = {}
    for snapshot_date, holdings in snapshot_map.items():
        try:
            if pd.Timestamp(snapshot_date) <= cutoff:
                filtered[snapshot_date] = holdings
        except Exception:
            continue
    return filtered


def attach_latest_prices(rows: list[dict[str, Any]], latest_price_map: dict[str, float | None]) -> list[dict[str, Any]]:
    attached = []
    for row in rows:
        ts_code = str(row.get("ts_code"))
        latest_price = latest_price_map.get(ts_code)
        if latest_price is None and ts_code != "CASH":
            latest_price = find_latest_price(ts_code)
        attached.append(
            copy_selection_diagnostics(
                row,
                {
                    "ts_code": ts_code,
                    "name": str(row.get("name", "")),
                    "weight": float(row.get("weight", 0.0)),
                    "latest_price": latest_price,
                },
            )
        )
    return attached


def pick_preferred_sample_tag(base_id: str, *, market_scope: str = "a_share") -> str:
    path_builder = build_hk_result_path if market_scope == "hkconnect" else build_result_path
    for sample_tag in ("since_2020_01", "since_2017_01", "since_2023_01", "since_2025_01", "since_2026_01"):
        if path_builder(base_id, sample_tag, "summary.json").exists():
            return sample_tag
    return "since_2020_01"


def build_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return existing_strategy_result_file(base_id, sample_tag, filename, market_scope="a_share")


def build_hk_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return existing_strategy_result_file(base_id, sample_tag, filename, market_scope="hkconnect")


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def live_spec(
    *,
    market_scope: str,
    path_name: str,
    winner_type: str,
    strategy_id: str,
    sample_tag: str,
    winner_tag: str,
    experimental: bool = False,
    tracked_only: bool = False,
    frequency: str = "",
    core_active: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "market_scope": market_scope,
        "path": path_name,
        "winner_type": winner_type,
        "strategy_id": strategy_id,
        "sample_tag": sample_tag,
        "winner_tags": [winner_tag],
        "experimental": experimental,
        "tracked_only": tracked_only,
        "frequency": frequency,
        "core_active": core_active,
    }


def _summary_metrics_for_spec(spec: dict[str, Any]) -> dict[str, Any]:
    market_scope = str(spec.get("market_scope") or "a_share")
    path_builder = build_hk_result_path if market_scope == "hkconnect" else build_result_path
    summary_path = path_builder(str(spec["strategy_id"]), str(spec["sample_tag"]), "summary.json")
    try:
        summary = load_json(summary_path)
    except Exception:
        return {}
    metrics = summary.get("metrics")
    return metrics if isinstance(metrics, dict) else {}


def _spec_sort_key(spec: dict[str, Any]) -> tuple[str, str, str, float]:
    metrics = _summary_metrics_for_spec(spec)
    return (
        str(spec.get("market_scope") or "a_share"),
        str(spec.get("path") or ""),
        str(spec.get("winner_type") or ""),
        -float(metrics.get("cagr", 0.0) or 0.0),
    )


def load_core_active_registry_entries() -> list[dict[str, Any]]:
    if not CORE_ACTIVE_REGISTRY_JSON.exists():
        return []
    try:
        payload = load_json(CORE_ACTIVE_REGISTRY_JSON)
    except Exception:
        return []
    strategies = payload.get("strategies") if isinstance(payload, dict) else []
    if not isinstance(strategies, list):
        return []
    return [
        item
        for item in strategies
        if isinstance(item, dict) and item.get("strategy_id") and item.get("active", True)
    ]


def _collect_windows(base_id: str, *, market_scope: str = "a_share") -> dict[str, Any]:
    path_builder = build_hk_result_path if market_scope == "hkconnect" else build_result_path
    windows: dict[str, Any] = {}
    for sample_tag in SAMPLE_TAGS:
        summary_path = path_builder(base_id, sample_tag, "summary.json")
        if not summary_path.exists():
            continue
        try:
            summary = load_json(summary_path)
            metrics = summary.get("metrics", {})
            windows[sample_tag] = {
                "total_return": float(metrics.get("total_return", 0.0)),
                "cagr": float(metrics.get("cagr", 0.0)),
                "max_drawdown": float(metrics.get("max_drawdown", 0.0)),
                "sharpe": float(metrics.get("sharpe_ratio", 0.0)),
                "turnover": float(metrics.get("average_annual_turnover", 0.0)),
                "sample_start": summary.get("sample_start"),
                "sample_end": summary.get("sample_end"),
            }
        except Exception:
            continue
    return windows


def _build_weight_history_windows(
    snapshot_map: dict[str, list[dict[str, Any]]],
    weekly_overlay_history: list[dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    history_items: list[dict[str, Any]] = []
    for snapshot_date, holdings in snapshot_map.items():
        history_items.append(
            {
                "date": snapshot_date,
                "event_type": "holding_snapshot",
                "holdings": holdings,
            }
        )
    for event in weekly_overlay_history or []:
        if not event.get("is_trade"):
            continue
        event_date = str(event.get("date") or event.get("signal_date") or "")
        history_items.append(
            {
                "date": event_date,
                "event_type": "weekly_satellite_overlay",
                "event_label": "周度卫星仓实际调仓",
                "holdings": [],
                "overlay_event": event,
            }
        )
    history_items = [item for item in history_items if str(item.get("date") or "")]
    if not history_items:
        return []
    history_items.sort(key=lambda item: str(item.get("date", "")), reverse=True)
    windows: list[dict[str, Any]] = []
    for idx in range(0, len(history_items), HISTORY_WINDOW_SNAPSHOTS):
        chunk = history_items[idx : idx + HISTORY_WINDOW_SNAPSHOTS]
        if not chunk:
            continue
        chunk.sort(key=lambda item: str(item.get("date", "")), reverse=True)
        window_end = str(chunk[0]["date"])
        window_start = str(chunk[-1]["date"])
        windows.append(
            {
                "window_index": len(windows),
                "label": f"{window_start} → {window_end}",
                "start_date": window_start,
                "end_date": window_end,
                "snapshot_count": len(chunk),
                "snapshots": chunk,
            }
        )
    return windows


def _load_equity_curve_points(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        frame = pd.read_csv(path)
    except Exception:
        return []
    required = {"date", "nav"}
    if frame.empty or not required.issubset(frame.columns):
        return []
    points: list[dict[str, Any]] = []
    for row in frame.to_dict("records"):
        try:
            points.append(
                {
                    "date": str(row["date"]),
                    "nav": float(row["nav"]),
                    "drawdown": float(row.get("drawdown", 0.0)),
                }
            )
        except Exception:
            continue
    return points


def _load_weekly_overlay_history(path: Path, limit: int = 24) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        frame = pd.read_csv(path)
    except Exception:
        return []
    required = {"date", "event_type", "one_way_turnover", "two_way_turnover", "buy_amount", "sell_amount", "trading_cost"}
    if frame.empty or not required.issubset(frame.columns):
        return []
    frame = frame[frame["event_type"].astype(str) == "weekly_satellite_overlay"].copy()
    if frame.empty:
        return []
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame = frame.dropna(subset=["date"]).sort_values("date", ascending=False)
    if "signal_date" in frame.columns:
        frame["signal_date"] = pd.to_datetime(frame["signal_date"], errors="coerce").fillna(frame["date"])
    else:
        frame["signal_date"] = frame["date"]
    if "trade_date" in frame.columns:
        frame["trade_date"] = pd.to_datetime(frame["trade_date"], errors="coerce").fillna(frame["date"])
    else:
        frame["trade_date"] = frame["date"]
    frame = frame.sort_values(["signal_date", "trade_date"], ascending=[False, False])
    rows: list[dict[str, Any]] = []
    for row in frame.head(limit).to_dict("records"):
        two_way_turnover = float(row.get("two_way_turnover", 0.0) or 0.0)
        trade_date = pd.Timestamp(row.get("trade_date") or row["date"]).strftime("%Y-%m-%d")
        signal_date = pd.Timestamp(row.get("signal_date") or row["date"]).strftime("%Y-%m-%d")
        trade_details: list[dict[str, Any]] = []
        trade_details_raw = row.get("trade_details_json")
        if pd.notna(trade_details_raw) and str(trade_details_raw).strip():
            try:
                parsed = json.loads(str(trade_details_raw))
            except Exception:
                parsed = []
            if isinstance(parsed, list):
                for item in parsed:
                    if not isinstance(item, dict):
                        continue
                    trade_details.append(
                        {
                            "ts_code": str(item.get("ts_code") or ""),
                            "name": str(item.get("name") or ""),
                            "side": str(item.get("side") or ""),
                            "current_weight": float(item.get("current_weight") or 0.0),
                            "target_weight": float(item.get("target_weight") or 0.0),
                            "post_trade_weight": float(item.get("post_trade_weight") or 0.0),
                            "diff_weight": float(item.get("diff_weight") or 0.0),
                            "gross_amount": float(item.get("gross_amount") or 0.0),
                            "gross_amount_pct_nav": float(item.get("gross_amount_pct_nav") or 0.0),
                            "fee": float(item.get("fee") or 0.0),
                            "fee_pct_nav": float(item.get("fee_pct_nav") or 0.0),
                        }
                    )
        rows.append(
            {
                "date": signal_date,
                "signal_date": signal_date,
                "trade_date": trade_date,
                "risk_stage": str(row.get("risk_stage") or ""),
                "raw_risk_stage": str(row.get("raw_risk_stage") or ""),
                "one_way_turnover": float(row.get("one_way_turnover", 0.0) or 0.0),
                "two_way_turnover": two_way_turnover,
                "buy_amount": float(row.get("buy_amount", 0.0) or 0.0),
                "sell_amount": float(row.get("sell_amount", 0.0) or 0.0),
                "buy_amount_pct_nav": float(row.get("buy_amount_pct_nav", 0.0) or 0.0),
                "sell_amount_pct_nav": float(row.get("sell_amount_pct_nav", 0.0) or 0.0),
                "trading_cost": float(row.get("trading_cost", 0.0) or 0.0),
                "trading_cost_pct_nav": float(row.get("trading_cost_pct_nav", 0.0) or 0.0),
                "pre_trade_nav": float(row.get("pre_trade_nav", 0.0) or 0.0),
                "is_trade": abs(two_way_turnover) > 1e-12,
                "trade_details": trade_details,
            }
        )
    return rows


def _load_trade_events(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        frame = pd.read_csv(path)
    except Exception:
        return []
    required = {"date", "event_type", "buy_amount", "sell_amount"}
    if frame.empty or not required.issubset(frame.columns):
        return []
    frame = frame.copy()
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame = frame.dropna(subset=["date"]).sort_values("date", ascending=False)
    events: list[dict[str, Any]] = []
    for row in frame.to_dict("records"):
        details: list[dict[str, Any]] = []
        raw_details = row.get("trade_details_json")
        if pd.notna(raw_details) and str(raw_details).strip():
            try:
                parsed = json.loads(str(raw_details))
            except Exception:
                parsed = []
            if isinstance(parsed, list):
                for item in parsed:
                    if not isinstance(item, dict):
                        continue
                    details.append(
                        copy_selection_diagnostics(
                            item,
                            {
                                "ts_code": str(item.get("ts_code") or ""),
                                "name": str(item.get("name") or ""),
                                "side": str(item.get("side") or ""),
                                "current_weight": float(item.get("current_weight") or 0.0),
                                "target_weight": float(item.get("target_weight") or 0.0),
                                "post_trade_weight": float(item.get("post_trade_weight") or 0.0),
                                "diff_weight": float(item.get("diff_weight") or 0.0),
                                "gross_amount_pct_nav": float(item.get("gross_amount_pct_nav") or 0.0),
                                "fee_pct_nav": float(item.get("fee_pct_nav") or 0.0),
                            },
                        )
                    )
        buy_amount = float(row.get("buy_amount") or 0.0)
        sell_amount = float(row.get("sell_amount") or 0.0)
        has_trade = bool(details) or buy_amount > 1e-12 or sell_amount > 1e-12
        if not has_trade:
            continue
        event_date = pd.Timestamp(row["date"]).strftime("%Y-%m-%d")
        signal_date = row.get("signal_date")
        trade_date = row.get("trade_date")
        events.append(
            {
                "date": event_date,
                "signal_date": pd.Timestamp(signal_date).strftime("%Y-%m-%d") if pd.notna(signal_date) else event_date,
                "trade_date": pd.Timestamp(trade_date).strftime("%Y-%m-%d") if pd.notna(trade_date) else event_date,
                "event_type": str(row.get("event_type") or ""),
                "buy_amount": buy_amount,
                "sell_amount": sell_amount,
                "has_trade_details": bool(details),
                "trade_details": details,
            }
        )
    return events


def guess_sample_tag(track_key: str) -> str:
    if track_key == "since_2017_only":
        return "since_2017_01"
    if track_key == "since_2020_only":
        return "since_2020_01"
    if track_key == "since_2023_only":
        return "since_2023_01"
    if track_key == "since_2025_only":
        return "since_2025_01"
    if track_key == "since_2026_only":
        return "since_2026_01"
    return "since_2020_01"


def find_latest_price(ts_code: str) -> float | None:
    cache_dir = HK_DAILY_CACHE_DIR if ts_code.endswith(".HK") else DAILY_CACHE_DIR
    path = cache_dir / f"{ts_code}.csv"
    if not path.exists():
        return None
    try:
        frame = pd.read_csv(path)
    except Exception:
        return None
    if frame.empty or "close" not in frame.columns:
        return None
    try:
        return float(frame.iloc[-1]["close"])
    except Exception:
        return None


def _parse_date_text(value: object) -> pd.Timestamp | None:
    parsed = pd.to_datetime(value, errors="coerce")
    if pd.isna(parsed):
        return None
    return pd.Timestamp(parsed).normalize()


def _validate_monthly_preview_freshness(
    *,
    base_id: str,
    sample_tag: str,
    market_scope: str,
    market_data_as_of: str | None,
    month_end_preview: dict[str, Any],
) -> None:
    if sample_tag not in NIGHTLY_REFRESH_SAMPLE_TAGS or not market_data_as_of or not month_end_preview:
        return
    if str(month_end_preview.get("status") or "available") != "available":
        return
    preview_date = _parse_date_text(month_end_preview.get("preview_as_of"))
    market_date = _parse_date_text(market_data_as_of)
    if preview_date is None or market_date is None:
        return
    if preview_date < market_date:
        raise RuntimeError(
            f"{market_scope} {base_id}/{sample_tag} month_end_preview.preview_as_of="
            f"{preview_date.date()} 早于 raw data_as_of={market_date.date()}；"
            "请先用最新 raw cache 重跑对应策略回测，拒绝导出 stale preview。"
        )


def _load_sample_view(base_id: str, sample_tag: str, *, market_scope: str = "a_share") -> dict[str, Any] | None:
    path_builder = build_hk_result_path if market_scope == "hkconnect" else build_result_path
    summary_path = path_builder(base_id, sample_tag, "summary.json")
    if not summary_path.exists():
        return None
    summary = load_json(summary_path)

    latest_weights_path = path_builder(base_id, sample_tag, "latest_weights.csv")
    monthly_path = path_builder(base_id, sample_tag, "monthly_returns.csv")
    weight_history_path = path_builder(base_id, sample_tag, "weights_history.csv")
    equity_curve_path = path_builder(base_id, sample_tag, "equity_curve.csv")
    turnover_path = path_builder(base_id, sample_tag, "turnover.csv")
    history_snapshot_map = load_weight_history_snapshot_map(weight_history_path)

    latest_weights: list[dict[str, Any]] = []
    target_exposure = 1.0
    risk_state = "risk_on"

    if latest_weights_path.exists():
        frame = pd.read_csv(latest_weights_path)
        for row in frame.to_dict("records"):
            ts_code = str(row["ts_code"])
            latest_price = find_latest_price(ts_code)
            latest_weights.append(
                copy_selection_diagnostics(
                    row,
                    {
                        "ts_code": ts_code,
                        "name": str(row["name"]),
                        "weight": float(row["weight"]),
                        "latest_price": latest_price,
                    },
                )
            )

    if monthly_path.exists():
        monthly = pd.read_csv(monthly_path)
        if not monthly.empty:
            last = monthly.iloc[-1]
            if "market_exposure_target" in monthly.columns:
                target_exposure = float(last["market_exposure_target"])
            if target_exposure >= 0.999:
                risk_state = "risk_on"
            elif target_exposure <= 0.001:
                risk_state = "risk_off"
            else:
                risk_state = "caution"

    formal_schedule = build_formal_schedule_meta(
        strategy_id=base_id,
        rebalance_frequency=str(summary.get("rebalance_frequency", "monthly")),
        sample_end=str(summary.get("sample_end") or ""),
        market_scope=market_scope,
    )
    market_data_as_of = latest_market_data_as_of(market_scope)
    if market_data_as_of:
        formal_schedule = {**formal_schedule, "data_as_of": market_data_as_of}
    schedule_kind = str(formal_schedule.get("schedule_kind") or "")
    latest_price_map = {str(row["ts_code"]): row.get("latest_price") for row in latest_weights}
    official_history_snapshot_map = history_snapshot_map
    month_end_preview = summary.get("month_end_preview") if isinstance(summary.get("month_end_preview"), dict) else {}
    if month_end_preview:
        preview_rows = month_end_preview.get("holdings")
        if isinstance(preview_rows, list):
            month_end_preview = {
                **month_end_preview,
                "holdings": attach_latest_prices(preview_rows, latest_price_map),
            }
    _validate_monthly_preview_freshness(
        base_id=base_id,
        sample_tag=sample_tag,
        market_scope=market_scope,
        market_data_as_of=market_data_as_of,
        month_end_preview=month_end_preview,
    )
    split_view: dict[str, Any] = {}
    weekly_overlay_history: list[dict[str, Any]] = []

    if schedule_kind == "monthly":
        basket_date = str(formal_schedule.get("basket_effective_date") or "")
        if basket_date and basket_date in history_snapshot_map:
            latest_weights = attach_latest_prices(history_snapshot_map[basket_date], latest_price_map)
            cash_weight = sum(float(row["weight"]) for row in latest_weights if row["ts_code"] == "CASH")
            target_exposure = max(0.0, 1.0 - cash_weight)
            if target_exposure >= 0.999:
                risk_state = "risk_on"
            elif target_exposure <= 0.001:
                risk_state = "risk_off"
            else:
                risk_state = "caution"
        official_history_snapshot_map = filter_snapshot_map_on_or_before(history_snapshot_map, basket_date)
    elif schedule_kind == "portfolio_weekly_overlay":
        basket_date = str(formal_schedule.get("basket_effective_date") or "")
        if basket_date and basket_date in history_snapshot_map:
            latest_weights = normalize_holdings_with_cash(
                attach_latest_prices(history_snapshot_map[basket_date], latest_price_map),
                target_exposure=target_exposure,
            )
        official_history_snapshot_map = filter_snapshot_map_on_or_before(history_snapshot_map, basket_date)
    elif schedule_kind == "satellite_weekly_overlay":
        basket_date = str(formal_schedule.get("basket_effective_date") or "")
        basket_weights: list[dict[str, Any]] = []
        if basket_date and basket_date in history_snapshot_map:
            basket_weights = attach_latest_prices(history_snapshot_map[basket_date], latest_price_map)
        official_history_snapshot_map = filter_snapshot_map_on_or_before(history_snapshot_map, basket_date)
        weekly_overlay_history = _load_weekly_overlay_history(turnover_path)
        latest_overlay_trade = next((row for row in weekly_overlay_history if row.get("is_trade")), None)
        overlay_summary = {
            "risk_state": risk_state,
            "target_total_exposure": target_exposure,
            "core_exposure_target": float(last["core_exposure_target"]) if monthly_path.exists() and not monthly.empty and "core_exposure_target" in monthly.columns else None,
            "satellite_exposure_target": float(last["satellite_exposure_target"]) if monthly_path.exists() and not monthly.empty and "satellite_exposure_target" in monthly.columns else None,
            "market_risk_off": bool(last["market_risk_off"]) if monthly_path.exists() and not monthly.empty and "market_risk_off" in monthly.columns else None,
            "market_12_1_momentum": float(last["market_12_1_momentum"]) if monthly_path.exists() and not monthly.empty and "market_12_1_momentum" in monthly.columns else None,
            "weekly_overlay_trade_count": int(last["weekly_overlay_trade_count"]) if monthly_path.exists() and not monthly.empty and "weekly_overlay_trade_count" in monthly.columns and pd.notna(last["weekly_overlay_trade_count"]) else 0,
            "latest_overlay_date": weekly_overlay_history[0]["signal_date"] if weekly_overlay_history else None,
            "latest_overlay_trade_date": latest_overlay_trade["trade_date"] if latest_overlay_trade else None,
        }
        if overlay_summary["latest_overlay_date"]:
            formal_schedule["suggestion_effective_date"] = overlay_summary["latest_overlay_date"]
            formal_schedule["exposure_effective_date"] = overlay_summary["latest_overlay_date"]
        split_view = {
            "mode": "satellite_weekly_overlay",
            "basket_weights": basket_weights,
            "overlay_summary": overlay_summary,
            "overlay_history": weekly_overlay_history,
        }

    return {
        "sample_tag": sample_tag,
        "sample_tag_label": SAMPLE_TAG_LABELS.get(sample_tag, sample_tag),
        "updated_at": summary.get("sample_end"),
        "rebalance_frequency": summary.get("rebalance_frequency", "monthly"),
        "summary_metrics": summary.get("metrics", {}),
        "target_total_exposure": target_exposure,
        "risk_state": risk_state,
        "latest_weights": latest_weights,
        "history_windows": _build_weight_history_windows(official_history_snapshot_map, weekly_overlay_history),
        "trade_events": _load_trade_events(turnover_path),
        "equity_curve_points": _load_equity_curve_points(equity_curve_path),
        "formal_schedule": formal_schedule,
        "split_view": split_view,
        "month_end_preview": month_end_preview,
        "summary_meta": {
            "sample_start": summary.get("sample_start"),
            "sample_end": summary.get("sample_end"),
            "latest_valuation_date": summary.get("latest_valuation_date"),
            "latest_formal_signal_date": summary.get("latest_formal_signal_date"),
            "is_provisional_period_end": summary.get("is_provisional_period_end"),
            "sample_label": summary.get("sample_label"),
            "sample_short_label": summary.get("sample_short_label"),
            "strategy_name": summary.get("strategy_name"),
            "strategy_base_name": summary.get("strategy_base_name"),
            "path": summary.get("strategy_id"),
            "strategy_kind": summary.get("strategy_kind"),
            "base_weight_method": summary.get("base_weight_method"),
            "core_source_mode": summary.get("core_source_mode"),
            "rebalance_frequency": summary.get("rebalance_frequency", "monthly"),
        },
    }


def build_strategy_detail_payload(base_id: str, sample_tag: str, *, market_scope: str = "a_share") -> dict[str, Any]:
    sample_view = _load_sample_view(base_id, sample_tag, market_scope=market_scope)
    if sample_view is None:
        raise FileNotFoundError(f"Missing summary for {base_id} / {sample_tag}")
    sample_views: dict[str, Any] = {}
    for tag in SAMPLE_TAGS:
        view = _load_sample_view(base_id, tag, market_scope=market_scope)
        if view is not None:
            sample_views[tag] = view

    display_name = (
        sample_view.get("summary_meta", {}).get("strategy_base_name")
        or sample_view.get("summary_meta", {}).get("strategy_name")
        or base_id
    )
    return {
        "strategy_id": base_id,
        "display_name": display_name,
        "sample_tag": sample_tag,
        "updated_at": sample_view["updated_at"],
        "rebalance_frequency": sample_view["rebalance_frequency"],
        "adjustment_style": infer_adjustment_style(base_id, str(sample_view["rebalance_frequency"])),
        "summary_metrics": sample_view["summary_metrics"],
        "windows": _collect_windows(base_id, market_scope=market_scope),
        "sample_views": sample_views,
        "target_total_exposure": sample_view["target_total_exposure"],
        "risk_state": sample_view["risk_state"],
        "latest_weights": sample_view["latest_weights"],
        "history_windows": sample_view["history_windows"],
        "equity_curve_points": sample_view["equity_curve_points"],
        "formal_schedule": sample_view.get("formal_schedule", {}),
        "split_view": sample_view.get("split_view", {}),
        "month_end_preview": sample_view.get("month_end_preview", {}),
        "summary_meta": sample_view["summary_meta"],
        "market_scope": market_scope,
    }


def load_strategy_snapshot(base_id: str, sample_tag: str, *, market_scope: str = "a_share") -> dict[str, Any]:
    return build_strategy_detail_payload(base_id, sample_tag, market_scope=market_scope)


def build_snapshot_from_live_spec(spec: dict[str, Any]) -> dict[str, Any]:
    market_scope = str(spec.get("market_scope") or "a_share")
    strategy_id = str(spec["strategy_id"])
    sample_tag = str(spec["sample_tag"])
    snapshot = load_strategy_snapshot(strategy_id, sample_tag, market_scope=market_scope)
    snapshot["path"] = str(spec.get("path") or "")
    snapshot["winner_type"] = str(spec.get("winner_type") or "")
    snapshot["winner_tags"] = list(spec.get("winner_tags") or [])
    snapshot["market_scope"] = market_scope
    snapshot["experimental"] = bool(spec.get("experimental", False))
    snapshot["tracked_only"] = bool(spec.get("tracked_only", False))
    if spec.get("frequency"):
        snapshot["frequency"] = str(spec.get("frequency") or "")
    if spec.get("core_active"):
        snapshot["core_active"] = spec["core_active"]
    return snapshot


def _pick_hk_robust_candidate(df: pd.DataFrame, path_name: str) -> str | None:
    subset = df[(df["path"] == path_name) & (df["sample_tag"].isin(HK_TRACKED_WINDOW_TAGS))].copy()
    if subset.empty:
        return None
    metrics_rows: list[dict[str, Any]] = []
    for strategy_id, sub in subset.groupby("strategy_id"):
        if not set(HK_TRACKED_WINDOW_TAGS).issubset(set(sub["sample_tag"].astype(str))):
            continue
        metrics_rows.append(
            {
                "strategy_id": strategy_id,
                "avg_cagr": float(sub["cagr"].mean()),
                "min_cagr": float(sub["cagr"].min()),
                "avg_sharpe": float(sub["sharpe_ratio"].mean()),
                "worst_dd": float(sub["max_drawdown"].min()),
                "avg_turn": float(sub["average_annual_turnover"].mean()),
            }
        )
    ranked = pd.DataFrame(metrics_rows).sort_values(
        ["min_cagr", "worst_dd", "avg_sharpe", "avg_cagr", "avg_turn"],
        ascending=[False, False, False, False, True],
    )
    return str(ranked.iloc[0]["strategy_id"]) if not ranked.empty else None


def _metrics_from_row(row: pd.Series) -> dict[str, float]:
    return {
        "cagr": float(row.get("cagr", 0.0)),
        "sharpe_ratio": float(row.get("sharpe_ratio", 0.0)),
        "max_drawdown": float(row.get("max_drawdown", 0.0)),
        "average_annual_turnover": float(row.get("average_annual_turnover", 0.0)),
        "total_return": float(row.get("total_return", 0.0)),
    }


def _is_ashare_path2_leaderboard_excluded(strategy_id: str, path4_theme_ids: set[str]) -> bool:
    return strategy_id in path4_theme_ids or "emergent_theme" in strategy_id


def _build_ashare_leaderboards(payload: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {"path1": {}, "path2": {}, "path3": {}, "path4": {}}
    try:
        from scripts.update_weighted_winners import load_path4_theme_ids

        path4_theme_ids = load_path4_theme_ids()
    except Exception:
        path4_theme_ids = set()

    def add_window(path_name: str, track_key: str, track_meta: dict[str, Any]) -> None:
        entries = track_meta.get("leaderboard") if isinstance(track_meta, dict) else None
        if not isinstance(entries, list) or not entries:
            return
        if path_name == "path2":
            entries = [
                entry
                for entry in entries
                if not _is_ashare_path2_leaderboard_excluded(
                    str(entry.get("strategy_base_id") or entry.get("strategy_id") or ""),
                    path4_theme_ids,
                )
            ]
            if not entries:
                return
        out.setdefault(path_name, {})[track_key] = {
            "track_key": track_key,
            "label": SAMPLE_LABELS.get(track_key, track_key),
            "sample_tag": guess_sample_tag(track_key),
            "entries": entries,
        }

    for track_key, track_meta in (payload.get("tracks") or {}).items():
        if track_key == "robust_candidate":
            continue
        add_window("path1", track_key, track_meta)
    for path_name in ("path2", "path3", "path4"):
        path_payload = payload.get(path_name) or {}
        for track_key, track_meta in (path_payload.get("tracks") or {}).items():
            add_window(path_name, track_key, track_meta)
    return {path: tracks for path, tracks in out.items() if tracks}


def _build_ashare_2026_leaderboards() -> dict[str, Any]:
    """Build display-only 2026 winners for each A-share research path."""
    comparison_path = existing_research_file("strategy_comparison_base_method.csv")
    if not comparison_path.exists():
        comparison_path = existing_research_file("strategy_comparison.csv")
    if not comparison_path.exists():
        return {}
    try:
        from scripts.update_weighted_winners import (
            STATIC_BASE_IDS,
            TRACK_LEADERBOARD_LIMIT,
            _augment_with_synthetic_windows,
            _build_strategy_map,
            _filter_ids_to_current_as_of,
            _latest_per_strategy_window,
            _leaderboard_entry,
            _matches_path2,
            _matches_path3,
            _rank_single_window_candidates,
            load_active_family_ids,
            load_path1_family_ids,
            load_path2_scan_rules,
            load_path4_theme_ids,
        )

        frame = pd.read_csv(comparison_path)
        latest_all = _augment_with_synthetic_windows(_latest_per_strategy_window(frame))
        if latest_all.empty:
            return {}
        all_base_ids = set(latest_all["strategy_base_id"].astype(str).unique())
        path2_prefixes, path2_variant_ids = load_path2_scan_rules()
        path4_allowed_ids = (load_path4_theme_ids() & all_base_ids) - STATIC_BASE_IDS
        path2_excluded_ids = {
            str(base_id)
            for base_id in all_base_ids
            if _is_ashare_path2_leaderboard_excluded(str(base_id), path4_allowed_ids)
        }
        path_ids: dict[str, set[str]] = {
            "path1": (load_path1_family_ids() & load_active_family_ids() & all_base_ids) - STATIC_BASE_IDS,
            "path2": {
                str(base_id)
                for base_id in all_base_ids
                if _matches_path2(str(base_id), path2_prefixes, path2_variant_ids)
            }
            - STATIC_BASE_IDS
            - path2_excluded_ids,
            "path3": {str(base_id) for base_id in all_base_ids if _matches_path3(str(base_id))} - STATIC_BASE_IDS,
            "path4": path4_allowed_ids,
        }
        strategies = _build_strategy_map(latest_all)
        out: dict[str, Any] = {}
        for path_name in A_SHARE_TRACKED_PATH_NAMES:
            allowed_ids = path_ids.get(path_name, set())
            if not allowed_ids:
                continue
            latest_for_path = _filter_ids_to_current_as_of(latest_all, allowed_ids)
            if latest_for_path.empty:
                continue
            ranked = _rank_single_window_candidates(
                latest_for_path,
                A_SHARE_2026_SAMPLE_TAG,
                allowed_base_ids=allowed_ids,
            )[:TRACK_LEADERBOARD_LIMIT]
            if not ranked:
                continue
            winner_id = ranked[0][0]
            entries = [
                _leaderboard_entry(
                    rank=rank,
                    strategy_id=strategy_id,
                    metrics=metrics,
                    strategies=strategies,
                    official_winner_id=winner_id,
                    raw_winner_id=winner_id,
                )
                for rank, (strategy_id, metrics) in enumerate(ranked, start=1)
            ]
            out[path_name] = {
                A_SHARE_2026_TRACK_KEY: {
                    "track_key": A_SHARE_2026_TRACK_KEY,
                    "label": SAMPLE_LABELS[A_SHARE_2026_TRACK_KEY],
                    "sample_tag": A_SHARE_2026_SAMPLE_TAG,
                    "entries": entries,
                }
            }
        return out
    except Exception:
        return {}


def _build_hkconnect_leaderboards(df: pd.DataFrame) -> dict[str, Any]:
    out: dict[str, Any] = {path_name: {} for path_name in HK_TRACKED_PATH_NAMES}
    for path_name in HK_TRACKED_PATH_NAMES:
        for sample_tag in HK_LEADERBOARD_WINDOW_TAGS:
            subset = df[(df["path"] == path_name) & (df["sample_tag"] == sample_tag)].copy()
            if subset.empty:
                continue
            subset = subset.sort_values(
                ["cagr", "sharpe_ratio", "max_drawdown", "average_annual_turnover"],
                ascending=[False, False, False, True],
            ).head(5)
            entries = []
            for rank, (_idx, row) in enumerate(subset.iterrows(), start=1):
                strategy_id = str(row["strategy_id"])
                entries.append(
                    {
                        "rank": rank,
                        "strategy_base_id": strategy_id,
                        "strategy_base_name": str(row.get("strategy_name") or row.get("strategy_id") or strategy_id),
                        "metrics": _metrics_from_row(row),
                        "is_official_winner": rank == 1,
                        "is_raw_winner": rank == 1,
                    }
                )
            track_key = sample_tag
            out.setdefault(path_name, {})[track_key] = {
                "track_key": track_key,
                "label": SAMPLE_TAG_LABELS.get(sample_tag, sample_tag),
                "sample_tag": sample_tag,
                "entries": entries,
            }
    return {path: tracks for path, tracks in out.items() if tracks}


def load_hkconnect_registry() -> list[dict[str, Any]]:
    comparison_path = existing_research_file("strategy_comparison_hkconnect.csv", market_scope="hkconnect")
    if not comparison_path.exists():
        return []
    try:
        df = pd.read_csv(comparison_path)
    except Exception:
        return []
    required = {"sample_tag", "path", "strategy_id", "cagr", "max_drawdown", "sharpe_ratio", "average_annual_turnover"}
    if df.empty or not required.issubset(df.columns):
        return []

    dedup: dict[str, dict[str, Any]] = {}

    def add_entry(*, path_name: str, winner_type: str, strategy_id: str, sample_tag: str) -> None:
        if strategy_id in dedup:
            dedup[strategy_id]["winner_tags"].append(f"hkconnect:{path_name}:{winner_type}")
            dedup[strategy_id]["experimental"] = (
                bool(dedup[strategy_id].get("experimental")) or path_name in HK_EXPERIMENTAL_PATH_NAMES
            )
            dedup[strategy_id]["tracked_only"] = (
                bool(dedup[strategy_id].get("tracked_only")) or path_name in HK_EXPERIMENTAL_PATH_NAMES
            )
            return
        meta_rows = df[df["strategy_id"].astype(str) == strategy_id].copy()
        frequency = ""
        if not meta_rows.empty and "rebalance_frequency" in meta_rows.columns:
            frequency = str(meta_rows.iloc[-1].get("rebalance_frequency") or "")
        dedup[strategy_id] = live_spec(
            market_scope="hkconnect",
            path_name=path_name,
            winner_type=winner_type,
            strategy_id=strategy_id,
            sample_tag=sample_tag,
            winner_tag=f"hkconnect:{path_name}:{winner_type}",
            experimental=path_name in HK_EXPERIMENTAL_PATH_NAMES,
            tracked_only=path_name in HK_EXPERIMENTAL_PATH_NAMES,
            frequency=frequency,
        )

    for sample_tag, winner_type in [
        ("since_2017_01", "2017-window winner"),
        ("since_2020_01", "2020-window winner"),
        ("since_2023_01", "2023-window winner"),
        ("since_2025_01", "2025-window winner"),
        ("since_2026_01", "2026-window winner"),
    ]:
        sample_df = df[df["sample_tag"] == sample_tag]
        for path_name in HK_TRACKED_PATH_NAMES:
            sub = sample_df[sample_df["path"] == path_name].sort_values(["cagr", "sharpe_ratio"], ascending=[False, False])
            if sub.empty:
                continue
            add_entry(
                path_name=path_name,
                winner_type=winner_type,
                strategy_id=str(sub.iloc[0]["strategy_id"]),
                sample_tag=sample_tag,
            )

    for path_name in HK_TRACKED_PATH_NAMES:
        robust_id = _pick_hk_robust_candidate(df, path_name)
        if robust_id:
            add_entry(
                path_name=path_name,
                winner_type="robust candidate",
                strategy_id=robust_id,
                sample_tag="since_2020_01",
            )

    return list(dedup.values())


@functools.lru_cache(maxsize=4)
def latest_market_data_as_of(market_scope: str) -> str | None:
    if market_scope != "hkconnect":
        prepared_as_of = latest_prepared_panel_as_of()
        if prepared_as_of:
            return prepared_as_of
    cache_dir = HK_DAILY_CACHE_DIR if market_scope == "hkconnect" else DAILY_CACHE_DIR
    if not cache_dir.exists():
        return None
    latest: pd.Timestamp | None = None
    for path in cache_dir.glob("*.csv"):
        try:
            frame = pd.read_csv(path, usecols=["trade_date"])
            if frame.empty:
                continue
            parsed = pd.to_datetime(frame["trade_date"], errors="coerce").max()
            if pd.isna(parsed):
                continue
            latest = pd.Timestamp(parsed) if latest is None else max(latest, pd.Timestamp(parsed))
        except (OSError, ValueError, pd.errors.EmptyDataError):
            continue
    return latest.strftime("%Y-%m-%d") if latest is not None else None


@functools.lru_cache(maxsize=1)
def latest_prepared_panel_as_of() -> str | None:
    if not PREPARED_PANEL_CACHE_DIR.exists():
        return None
    latest: pd.Timestamp | None = None
    for path in PREPARED_PANEL_CACHE_DIR.glob("v*_*.pkl"):
        match = re.search(r"_([0-9]{8})_([0-9]{8})_", path.name)
        if not match:
            continue
        parsed = pd.to_datetime(match.group(2), format="%Y%m%d", errors="coerce")
        if pd.isna(parsed):
            continue
        latest = pd.Timestamp(parsed) if latest is None else max(latest, pd.Timestamp(parsed))
    return latest.strftime("%Y-%m-%d") if latest is not None else None


def _registry_item(item: dict[str, Any]) -> dict[str, Any]:
    formal_schedule = item.get("formal_schedule") or {}
    market_scope = item.get("market_scope", "a_share")
    data_as_of = latest_market_data_as_of(str(market_scope)) or formal_schedule.get("data_as_of") or item.get("updated_at")
    signal_effective_date = formal_schedule.get("suggestion_effective_date") or item.get("updated_at")
    basket_effective_date = formal_schedule.get("basket_effective_date") or signal_effective_date
    exposure_effective_date = formal_schedule.get("exposure_effective_date") or signal_effective_date
    return {
        "strategy_id": item["strategy_id"],
        "display_name": item["display_name"],
        "path": item["path"],
        "market_scope": market_scope,
        "winner_type": item["winner_type"],
        "winner_tags": item["winner_tags"],
        "adjustment_style": item["adjustment_style"],
        "target_total_exposure": item["target_total_exposure"],
        "risk_state": item["risk_state"],
        "summary_metrics": item["summary_metrics"],
        "updated_at": item["updated_at"],
        "data_as_of": data_as_of,
        "signal_effective_date": signal_effective_date,
        "basket_effective_date": basket_effective_date,
        "exposure_effective_date": exposure_effective_date,
        "schedule_kind": formal_schedule.get("schedule_kind", ""),
        "frequency": item.get("frequency", ""),
        "experimental": bool(item.get("experimental", False)),
        "tracked_only": bool(item.get("tracked_only", False)),
    }


def export_live_data() -> dict[str, Any]:
    payload = load_json(TRACKED_WINNERS_JSON)
    strategies_map: dict[str, Any] = payload["strategies"]
    ashare_leaderboards = _build_ashare_leaderboards(payload)
    for path_name, tracks in _build_ashare_2026_leaderboards().items():
        ashare_leaderboards.setdefault(path_name, {}).update(tracks)
    winner_leaderboards: dict[str, Any] = {"a_share": ashare_leaderboards}
    hk_comparison_path = existing_research_file("strategy_comparison_hkconnect.csv", market_scope="hkconnect")
    if hk_comparison_path.exists():
        try:
            hk_df = pd.read_csv(hk_comparison_path)
            if not hk_df.empty:
                winner_leaderboards["hkconnect"] = _build_hkconnect_leaderboards(hk_df)
        except Exception:
            pass

    dedup: dict[str, dict[str, Any]] = {}

    def add_entry(
        *,
        path_name: str,
        winner_type: str,
        strategy_id: str,
        sample_tag: str,
        experimental: bool = False,
        tracked_only: bool = False,
        frequency: str = "",
    ) -> None:
        if strategy_id in dedup:
            dedup[strategy_id]["winner_tags"].append(f"{path_name}:{winner_type}")
            dedup[strategy_id]["experimental"] = bool(dedup[strategy_id].get("experimental")) or experimental
            dedup[strategy_id]["tracked_only"] = bool(dedup[strategy_id].get("tracked_only")) or tracked_only
            if frequency and not dedup[strategy_id].get("frequency"):
                dedup[strategy_id]["frequency"] = frequency
            return
        dedup[strategy_id] = live_spec(
            market_scope="a_share",
            path_name=path_name,
            winner_type=winner_type,
            strategy_id=strategy_id,
            sample_tag=sample_tag,
            winner_tag=f"{path_name}:{winner_type}",
            experimental=experimental,
            tracked_only=tracked_only,
            frequency=frequency,
        )

    for track_key, track_meta in payload["tracks"].items():
        if track_key == "robust_candidate":
            continue
        strategy_id = str(track_meta["winner"])
        add_entry(
            path_name="path1",
            winner_type=SAMPLE_LABELS.get(track_key, track_key),
            strategy_id=strategy_id,
            sample_tag=guess_sample_tag(track_key),
        )

    robust_meta = payload["tracks"].get("robust_candidate")
    if robust_meta:
        add_entry(
            path_name="path1",
            winner_type="robust candidate",
            strategy_id=str(robust_meta["strategy_base_id"]),
            sample_tag="since_2020_01",
        )

    for track_key, track_meta in payload["path2"]["tracks"].items():
        strategy_id = str(track_meta["winner"])
        add_entry(
            path_name="path2",
            winner_type=SAMPLE_LABELS.get(track_key, track_key),
            strategy_id=strategy_id,
            sample_tag=guess_sample_tag(track_key),
        )

    path2_robust = payload["path2"].get("strategy_base_id")
    if path2_robust:
        add_entry(
            path_name="path2",
            winner_type="robust candidate",
            strategy_id=str(path2_robust),
            sample_tag="since_2020_01",
        )

    path3_payload = payload.get("path3") or {}
    for track_key, track_meta in (path3_payload.get("tracks") or {}).items():
        strategy_id = str(track_meta["winner"])
        add_entry(
            path_name="path3",
            winner_type=SAMPLE_LABELS.get(track_key, track_key),
            strategy_id=strategy_id,
            sample_tag=guess_sample_tag(track_key),
        )

    path3_robust = path3_payload.get("strategy_base_id")
    if path3_robust:
        add_entry(
            path_name="path3",
            winner_type="robust candidate",
            strategy_id=str(path3_robust),
            sample_tag="since_2020_01",
        )

    path4_payload = payload.get("path4") or {}
    path4_experimental = bool(path4_payload.get("experimental", True))
    path4_tracked_only = bool(path4_payload.get("tracked_only", True))
    path4_frequency = str(path4_payload.get("frequency") or "monthly")
    for track_key, track_meta in (path4_payload.get("tracks") or {}).items():
        strategy_id = str(track_meta["winner"])
        add_entry(
            path_name="path4",
            winner_type=SAMPLE_LABELS.get(track_key, track_key),
            strategy_id=strategy_id,
            sample_tag=guess_sample_tag(track_key),
            experimental=path4_experimental,
            tracked_only=path4_tracked_only,
            frequency=path4_frequency,
        )

    path4_robust = path4_payload.get("strategy_base_id")
    if path4_robust:
        add_entry(
            path_name="path4",
            winner_type="robust candidate",
            strategy_id=str(path4_robust),
            sample_tag="since_2020_01",
            experimental=path4_experimental,
            tracked_only=path4_tracked_only,
            frequency=path4_frequency,
        )

    for path_name in A_SHARE_TRACKED_PATH_NAMES:
        leaderboard = (
            ((winner_leaderboards.get("a_share") or {}).get(path_name) or {}).get(A_SHARE_2026_TRACK_KEY) or {}
        )
        entries = leaderboard.get("entries") if isinstance(leaderboard, dict) else []
        if not entries:
            continue
        strategy_id = str(entries[0].get("strategy_base_id") or "")
        if not strategy_id:
            continue
        try:
            add_entry(
                path_name=path_name,
                winner_type=SAMPLE_LABELS[A_SHARE_2026_TRACK_KEY],
                strategy_id=strategy_id,
                sample_tag=A_SHARE_2026_SAMPLE_TAG,
                experimental=path_name == "path4" and path4_experimental,
                tracked_only=path_name == "path4" and path4_tracked_only,
                frequency=path4_frequency if path_name == "path4" else "",
            )
        except (FileNotFoundError, KeyError):
            continue

    registry_specs = list(dedup.values())
    registry_specs.extend(load_hkconnect_registry())
    registry_specs = sorted(registry_specs, key=_spec_sort_key)

    path2_known_ids = {
        str(meta["winner"]) for meta in payload["path2"]["tracks"].values()
    }
    if payload["path2"].get("strategy_base_id"):
        path2_known_ids.add(str(payload["path2"]["strategy_base_id"]))
    path3_known_ids = {
        str(meta["winner"]) for meta in (payload.get("path3") or {}).get("tracks", {}).values()
    }
    if (payload.get("path3") or {}).get("strategy_base_id"):
        path3_known_ids.add(str((payload.get("path3") or {})["strategy_base_id"]))
    path4_known_ids = {
        str(meta["winner"]) for meta in (payload.get("path4") or {}).get("tracks", {}).values()
    }
    if (payload.get("path4") or {}).get("strategy_base_id"):
        path4_known_ids.add(str((payload.get("path4") or {})["strategy_base_id"]))

    core_active_specs: list[dict[str, Any]] = []
    core_active_entries = load_core_active_registry_entries()
    for registry_entry in core_active_entries:
        strategy_id = str(registry_entry["strategy_id"])
        if strategy_id in dedup:
            continue
        try:
            sample_tag = pick_preferred_sample_tag(strategy_id, market_scope="a_share")
        except Exception:
            continue
        registry_path = str(registry_entry.get("last_path") or "")
        if registry_path:
            path_name = registry_path
        elif strategy_id in path4_known_ids:
            path_name = "path4"
        elif strategy_id in path3_known_ids or is_path3_weekly_strategy(strategy_id):
            path_name = "path3"
        elif strategy_id in path2_known_ids or "equal_weight_winner_core" in strategy_id:
            path_name = "path2"
        else:
            path_name = "path1"
        winner_tags = [
            f"{role.get('path', '')}:{role.get('track', '')}".strip(":")
            for role in registry_entry.get("current_winner_roles", [])
            if isinstance(role, dict)
        ]
        spec = live_spec(
            market_scope="a_share",
            path_name=path_name,
            winner_type="core active",
            strategy_id=strategy_id,
            sample_tag=sample_tag,
            winner_tag=winner_tags[0] if winner_tags else f"{path_name}:core_active",
            core_active={
                "first_win_date": registry_entry.get("first_win_date"),
                "last_win_date": registry_entry.get("last_win_date"),
                "win_count": registry_entry.get("win_count"),
                "days_since_last_win": registry_entry.get("days_since_last_win"),
            },
        )
        spec["winner_tags"] = winner_tags
        core_active_specs.append(spec)

    core_active_specs = sorted(
        core_active_specs,
        key=lambda item: (
            item["path"],
            _spec_sort_key(item)[3],
            item["strategy_id"],
        ),
    )

    LIVE_DIR.mkdir(parents=True, exist_ok=True)
    (LIVE_DIR / "strategies").mkdir(parents=True, exist_ok=True)
    written_strategy_ids: set[str] = set()

    def write_strategy_snapshot(item: dict[str, Any]) -> None:
        strategy_id = str(item["strategy_id"])
        if strategy_id in written_strategy_ids:
            return
        strategy_path = LIVE_DIR / "strategies" / f"{strategy_id}.json"
        strategy_path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written_strategy_ids.add(strategy_id)

    registry_items: list[dict[str, Any]] = []
    for spec in registry_specs:
        try:
            snapshot = build_snapshot_from_live_spec(spec)
        except Exception:
            continue
        write_strategy_snapshot(snapshot)
        registry_items.append(_registry_item(snapshot))
        del snapshot

    core_active_items: list[dict[str, Any]] = []
    for spec in core_active_specs:
        try:
            snapshot = build_snapshot_from_live_spec(spec)
        except Exception:
            continue
        write_strategy_snapshot(snapshot)
        core_active_items.append(_registry_item(snapshot))
        del snapshot
    for market_scope, path_payload in winner_leaderboards.items():
        if not isinstance(path_payload, dict):
            continue
        for path_name, tracks in path_payload.items():
            if not isinstance(tracks, dict):
                continue
            for track_key, leaderboard in tracks.items():
                entries = leaderboard.get("entries") if isinstance(leaderboard, dict) else []
                sample_tag = str((leaderboard or {}).get("sample_tag") or guess_sample_tag(str(track_key)))
                for entry in entries or []:
                    strategy_id = str(entry.get("strategy_base_id") or entry.get("strategy_id") or "")
                    if not strategy_id or strategy_id in written_strategy_ids:
                        continue
                    try:
                        snapshot = load_strategy_snapshot(strategy_id, sample_tag, market_scope=str(market_scope))
                    except Exception:
                        continue
                    snapshot["path"] = str(path_name)
                    snapshot["winner_type"] = "leaderboard candidate"
                    snapshot["winner_tags"] = [f"{market_scope}:{path_name}:{track_key}:top{entry.get('rank')}"]
                    snapshot["market_scope"] = str(market_scope)
                    if str(market_scope) == "a_share" and str(path_name) == "path4":
                        snapshot["experimental"] = path4_experimental
                        snapshot["tracked_only"] = path4_tracked_only
                        snapshot["frequency"] = path4_frequency
                    if str(market_scope) == "hkconnect" and str(path_name) in HK_EXPERIMENTAL_PATH_NAMES:
                        snapshot["experimental"] = True
                        snapshot["tracked_only"] = True
                    write_strategy_snapshot(snapshot)

    registry_payload = {
        "as_of": payload["as_of"],
        "strategies": registry_items,
        "core_active_strategies": core_active_items,
        "winner_leaderboards": winner_leaderboards,
    }
    (LIVE_DIR / "strategy_registry.json").write_text(
        json.dumps(registry_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return registry_payload


def main() -> None:
    payload = export_live_data()
    print(f"[OK] Exported {len(payload['strategies'])} live strategies to {LIVE_DIR}")


if __name__ == "__main__":
    main()
