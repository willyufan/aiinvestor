from __future__ import annotations

import functools
import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backtest_marketcap_etf import CORE_ACTIVE_FAMILY_BASE_IDS

RESULTS_DIR = ROOT / "results"
HK_RESULTS_DIR = ROOT / "results_hkconnect"
LIVE_DIR = RESULTS_DIR / "live"
TRACKED_WINNERS_JSON = RESULTS_DIR / "weighted_track_winners.json"
DAILY_CACHE_DIR = ROOT / "data_cache" / "daily"
HK_DAILY_CACHE_DIR = ROOT / "data_cache" / "hkconnect" / "daily_adj"
A_SHARE_TRADE_CALENDAR_PATH = ROOT / "data_cache" / "trade_calendar.csv"
HK_TRADE_CALENDAR_PATH = ROOT / "data_cache" / "hkconnect" / "basic" / "trade_calendar_hk.csv"

SAMPLE_LABELS = {
    "since_2017_only": "2017-window winner",
    "since_2020_only": "2020-window winner",
    "since_2023_only": "2023-window winner",
    "since_2025_only": "2025-window winner",
    "robust_candidate": "robust candidate",
}
HISTORY_WINDOW_SNAPSHOTS = 12
SAMPLE_TAGS = ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]
SAMPLE_TAG_LABELS = {
    "since_2017_01": "2017窗口",
    "since_2020_01": "2020窗口",
    "since_2023_01": "2023窗口",
    "since_2025_01": "2025窗口",
    "since_2026_01": "2026观察窗",
}


def infer_adjustment_style(strategy_id: str, rebalance_frequency: str) -> str:
    strategy_id = str(strategy_id or "")
    rebalance_frequency = str(rebalance_frequency or "monthly")
    if "__port_weekly_exposure_buffered" in strategy_id:
        return "月度换股 + 周度总仓位（双周确认）"
    if "__port_weekly_exposure_asym" in strategy_id:
        return "月度换股 + 周度总仓位（快减慢加）"
    if "__port_weekly_exposure" in strategy_id:
        return "月度换股 + 周度总仓位"
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
                {
                    "ts_code": str(row.get("ts_code")),
                    "name": str(row.get("name", "")),
                    "weight": exposure * base_weight / non_cash_total,
                    "latest_price": latest_price_map.get(str(row.get("ts_code"))),
                }
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
            {
                "ts_code": str(row["ts_code"]),
                "name": str(row["name"]),
                "weight": float(row["weight"]),
            }
            for row in sub.sort_values("weight", ascending=False).to_dict("records")
        ]
    return snapshot_map


def attach_latest_prices(rows: list[dict[str, Any]], latest_price_map: dict[str, float | None]) -> list[dict[str, Any]]:
    attached = []
    for row in rows:
        ts_code = str(row.get("ts_code"))
        latest_price = latest_price_map.get(ts_code)
        if latest_price is None and ts_code != "CASH":
            latest_price = find_latest_price(ts_code)
        attached.append(
            {
                "ts_code": ts_code,
                "name": str(row.get("name", "")),
                "weight": float(row.get("weight", 0.0)),
                "latest_price": latest_price,
            }
        )
    return attached


def pick_preferred_sample_tag(base_id: str, *, market_scope: str = "a_share") -> str:
    path_builder = build_hk_result_path if market_scope == "hkconnect" else build_result_path
    for sample_tag in ("since_2020_01", "since_2017_01", "since_2023_01", "since_2025_01", "since_2026_01"):
        if path_builder(base_id, sample_tag, "summary.json").exists():
            return sample_tag
    return "since_2020_01"


def build_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return RESULTS_DIR / f"{base_id}__{sample_tag}" / filename


def build_hk_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return HK_RESULTS_DIR / f"{base_id}__{sample_tag}" / filename


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


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


def _build_weight_history_windows(snapshot_map: dict[str, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    if not snapshot_map:
        return []
    snapshot_dates = sorted(snapshot_map.keys(), reverse=True)
    windows: list[dict[str, Any]] = []
    for idx in range(0, len(snapshot_dates), HISTORY_WINDOW_SNAPSHOTS):
        chunk_dates = snapshot_dates[idx : idx + HISTORY_WINDOW_SNAPSHOTS]
        if not chunk_dates:
            continue
        snapshots: list[dict[str, Any]] = []
        for snapshot_date in chunk_dates:
            snapshots.append(
                {
                    "date": snapshot_date,
                    "holdings": snapshot_map.get(snapshot_date, []),
                }
            )
        snapshots.sort(key=lambda item: item["date"], reverse=True)
        window_end = snapshots[0]["date"]
        window_start = snapshots[-1]["date"]
        windows.append(
            {
                "window_index": len(windows),
                "label": f"{window_start} → {window_end}",
                "start_date": window_start,
                "end_date": window_end,
                "snapshot_count": len(snapshots),
                "snapshots": snapshots,
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


def guess_sample_tag(track_key: str) -> str:
    if track_key == "since_2017_only":
        return "since_2017_01"
    if track_key == "since_2020_only":
        return "since_2020_01"
    if track_key == "since_2023_only":
        return "since_2023_01"
    if track_key == "since_2025_only":
        return "since_2025_01"
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
                {
                    "ts_code": ts_code,
                    "name": str(row["name"]),
                    "weight": float(row["weight"]),
                    "latest_price": latest_price,
                }
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
    schedule_kind = str(formal_schedule.get("schedule_kind") or "")
    latest_price_map = {str(row["ts_code"]): row.get("latest_price") for row in latest_weights}
    split_view: dict[str, Any] = {}

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
    elif schedule_kind == "portfolio_weekly_overlay":
        basket_date = str(formal_schedule.get("basket_effective_date") or "")
        if basket_date and basket_date in history_snapshot_map:
            latest_weights = normalize_holdings_with_cash(
                attach_latest_prices(history_snapshot_map[basket_date], latest_price_map),
                target_exposure=target_exposure,
            )
    elif schedule_kind == "satellite_weekly_overlay":
        basket_date = str(formal_schedule.get("basket_effective_date") or "")
        basket_weights: list[dict[str, Any]] = []
        if basket_date and basket_date in history_snapshot_map:
            basket_weights = attach_latest_prices(history_snapshot_map[basket_date], latest_price_map)
        overlay_summary = {
            "risk_state": risk_state,
            "target_total_exposure": target_exposure,
            "core_exposure_target": float(last["core_exposure_target"]) if monthly_path.exists() and not monthly.empty and "core_exposure_target" in monthly.columns else None,
            "satellite_exposure_target": float(last["satellite_exposure_target"]) if monthly_path.exists() and not monthly.empty and "satellite_exposure_target" in monthly.columns else None,
            "market_risk_off": bool(last["market_risk_off"]) if monthly_path.exists() and not monthly.empty and "market_risk_off" in monthly.columns else None,
            "market_12_1_momentum": float(last["market_12_1_momentum"]) if monthly_path.exists() and not monthly.empty and "market_12_1_momentum" in monthly.columns else None,
            "weekly_overlay_trade_count": int(last["weekly_overlay_trade_count"]) if monthly_path.exists() and not monthly.empty and "weekly_overlay_trade_count" in monthly.columns and pd.notna(last["weekly_overlay_trade_count"]) else 0,
        }
        split_view = {
            "mode": "satellite_weekly_overlay",
            "basket_weights": basket_weights,
            "overlay_summary": overlay_summary,
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
        "history_windows": _build_weight_history_windows(history_snapshot_map),
        "equity_curve_points": _load_equity_curve_points(equity_curve_path),
        "formal_schedule": formal_schedule,
        "split_view": split_view,
        "summary_meta": {
            "sample_start": summary.get("sample_start"),
            "sample_end": summary.get("sample_end"),
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
        "summary_meta": sample_view["summary_meta"],
        "market_scope": market_scope,
    }


def load_strategy_snapshot(base_id: str, sample_tag: str, *, market_scope: str = "a_share") -> dict[str, Any]:
    return build_strategy_detail_payload(base_id, sample_tag, market_scope=market_scope)


def _pick_hk_robust_candidate(df: pd.DataFrame, path_name: str) -> str | None:
    subset = df[df["path"] == path_name].copy()
    if subset.empty:
        return None
    metrics_rows: list[dict[str, Any]] = []
    for strategy_id, sub in subset.groupby("strategy_id"):
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
        ["avg_cagr", "min_cagr", "avg_sharpe", "worst_dd", "avg_turn"],
        ascending=[False, False, False, False, True],
    )
    return str(ranked.iloc[0]["strategy_id"]) if not ranked.empty else None


def load_hkconnect_registry() -> list[dict[str, Any]]:
    comparison_path = HK_RESULTS_DIR / "strategy_comparison_hkconnect.csv"
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
            return
        snapshot = load_strategy_snapshot(strategy_id, sample_tag, market_scope="hkconnect")
        snapshot["path"] = path_name
        snapshot["winner_type"] = winner_type
        snapshot["winner_tags"] = [f"hkconnect:{path_name}:{winner_type}"]
        snapshot["market_scope"] = "hkconnect"
        dedup[strategy_id] = snapshot

    for sample_tag, winner_type in [
        ("since_2017_01", "2017-window winner"),
        ("since_2020_01", "2020-window winner"),
        ("since_2023_01", "2023-window winner"),
        ("since_2025_01", "2025-window winner"),
    ]:
        sample_df = df[df["sample_tag"] == sample_tag]
        for path_name in ("path1", "path2"):
            sub = sample_df[sample_df["path"] == path_name].sort_values(["cagr", "sharpe_ratio"], ascending=[False, False])
            if sub.empty:
                continue
            add_entry(
                path_name=path_name,
                winner_type=winner_type,
                strategy_id=str(sub.iloc[0]["strategy_id"]),
                sample_tag=sample_tag,
            )

    for path_name in ("path1", "path2"):
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
    }


def export_live_data() -> dict[str, Any]:
    payload = load_json(TRACKED_WINNERS_JSON)
    strategies_map: dict[str, Any] = payload["strategies"]

    registry: list[dict[str, Any]] = []
    dedup: dict[str, dict[str, Any]] = {}

    def add_entry(*, path_name: str, winner_type: str, strategy_id: str, sample_tag: str) -> None:
        if strategy_id in dedup:
            dedup[strategy_id]["winner_tags"].append(f"{path_name}:{winner_type}")
            return
        tracked_info = strategies_map[strategy_id]
        snapshot = load_strategy_snapshot(strategy_id, sample_tag, market_scope="a_share")
        snapshot["path"] = path_name
        snapshot["winner_type"] = winner_type
        snapshot["winner_tags"] = [f"{path_name}:{winner_type}"]
        snapshot["windows"] = tracked_info["windows"]
        snapshot["market_scope"] = "a_share"
        dedup[strategy_id] = snapshot

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

    registry = list(dedup.values())
    registry.extend(load_hkconnect_registry())
    registry = sorted(
        registry,
        key=lambda item: (
            item.get("market_scope", "a_share"),
            item["path"],
            item["winner_type"],
            -float(item["summary_metrics"].get("cagr", 0.0)),
        ),
    )

    path2_known_ids = {
        str(meta["winner"]) for meta in payload["path2"]["tracks"].values()
    }
    if payload["path2"].get("strategy_base_id"):
        path2_known_ids.add(str(payload["path2"]["strategy_base_id"]))

    core_active_registry: list[dict[str, Any]] = []
    for strategy_id in CORE_ACTIVE_FAMILY_BASE_IDS:
        if strategy_id in dedup:
            continue
        try:
            sample_tag = pick_preferred_sample_tag(strategy_id, market_scope="a_share")
            snapshot = load_strategy_snapshot(strategy_id, sample_tag, market_scope="a_share")
        except Exception:
            continue
        snapshot["path"] = "path2" if strategy_id in path2_known_ids or "equal_weight_winner_core" in strategy_id else "path1"
        snapshot["winner_type"] = "core active"
        snapshot["winner_tags"] = []
        snapshot["market_scope"] = "a_share"
        core_active_registry.append(snapshot)

    core_active_registry = sorted(
        core_active_registry,
        key=lambda item: (
            item["path"],
            -float(item["summary_metrics"].get("cagr", 0.0)),
            item["strategy_id"],
        ),
    )

    LIVE_DIR.mkdir(parents=True, exist_ok=True)
    (LIVE_DIR / "strategies").mkdir(parents=True, exist_ok=True)
    snapshot_items: dict[str, dict[str, Any]] = {item["strategy_id"]: item for item in registry}
    for item in core_active_registry:
        snapshot_items.setdefault(item["strategy_id"], item)
    for item in snapshot_items.values():
        strategy_path = LIVE_DIR / "strategies" / f"{item['strategy_id']}.json"
        strategy_path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    registry_payload = {
        "as_of": payload["as_of"],
        "strategies": [_registry_item(item) for item in registry],
        "core_active_strategies": [_registry_item(item) for item in core_active_registry],
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
