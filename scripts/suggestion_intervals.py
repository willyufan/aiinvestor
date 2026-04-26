from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import pandas as pd

HISTORY_WINDOW_SNAPSHOTS = 12
SUGGESTION_INTERVAL_LIMIT = 200
INTERVAL_FILENAME = "suggestion_intervals.json"


def _normalize_holdings_for_signature(holdings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized: list[dict[str, Any]] = []
    for row in holdings or []:
        ts_code = str(row.get("ts_code") or "").strip()
        if not ts_code:
            continue
        normalized.append(
            {
                "ts_code": ts_code,
                "name": str(row.get("name") or ts_code),
                "weight": round(float(row.get("weight", 0.0)), 8),
            }
        )
    normalized.sort(key=lambda item: item["ts_code"])
    return normalized


def canonicalize_holdings_for_exposure(holdings: list[dict[str, Any]], target_total_exposure: float) -> list[dict[str, Any]]:
    normalized = _normalize_holdings_for_signature(holdings)
    if normalized:
        return normalized
    if float(target_total_exposure) <= 1e-6:
        return [{"ts_code": "CASH", "name": "现金", "weight": 1.0}]
    return normalized


def build_suggestion_content_hash(target_total_exposure: float, holdings: list[dict[str, Any]]) -> str:
    holdings = canonicalize_holdings_for_exposure(holdings, target_total_exposure)
    payload = {
        "target_total_exposure": round(float(target_total_exposure), 8),
        "holdings": holdings,
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def target_exposure_from_holdings(holdings: list[dict[str, Any]]) -> float:
    if not holdings:
        return 0.0
    cash_weight = 0.0
    for row in holdings or []:
        if str(row.get("ts_code")) == "CASH":
            cash_weight = float(row.get("weight", 0.0))
            break
    return max(0.0, min(1.0, 1.0 - cash_weight))


def _build_weight_history_windows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        frame = pd.read_csv(path)
    except Exception:
        return []
    required = {"date", "ts_code", "name", "weight"}
    if frame.empty or not required.issubset(frame.columns):
        return []
    frame = frame.copy()
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame = frame.dropna(subset=["date"])
    if frame.empty:
        return []
    frame = frame.sort_values(["date", "weight"], ascending=[False, False])
    snapshot_dates = sorted(frame["date"].drop_duplicates().tolist(), reverse=True)
    windows: list[dict[str, Any]] = []
    for idx in range(0, len(snapshot_dates), HISTORY_WINDOW_SNAPSHOTS):
        chunk_dates = snapshot_dates[idx : idx + HISTORY_WINDOW_SNAPSHOTS]
        if not chunk_dates:
            continue
        chunk_rows = frame[frame["date"].isin(chunk_dates)].copy()
        snapshots: list[dict[str, Any]] = []
        for snapshot_date, sub in chunk_rows.groupby("date", sort=False):
            holdings = [
                {
                    "ts_code": str(row["ts_code"]),
                    "name": str(row["name"]),
                    "weight": float(row["weight"]),
                }
                for row in sub.sort_values("weight", ascending=False).to_dict("records")
            ]
            snapshots.append(
                {
                    "date": pd.Timestamp(snapshot_date).strftime("%Y-%m-%d"),
                    "holdings": holdings,
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


def _bootstrap_suggestion_intervals(weight_history_path: Path) -> list[dict[str, Any]]:
    history_windows = _build_weight_history_windows(weight_history_path)
    snapshots: list[dict[str, Any]] = []
    seen_dates: set[str] = set()
    for window in history_windows:
        for snapshot in window.get("snapshots", []):
            date = str(snapshot.get("date") or "")
            if not date or date in seen_dates:
                continue
            seen_dates.add(date)
            snapshots.append(snapshot)
    snapshots.sort(key=lambda item: str(item.get("date", "")))
    intervals: list[dict[str, Any]] = []
    for snapshot in snapshots:
        holdings = _normalize_holdings_for_signature(snapshot.get("holdings", []))
        target_total_exposure = target_exposure_from_holdings(holdings)
        holdings = canonicalize_holdings_for_exposure(holdings, target_total_exposure)
        content_hash = build_suggestion_content_hash(target_total_exposure, holdings)
        date = str(snapshot.get("date") or "")
        if intervals and intervals[-1]["content_hash"] == content_hash:
            intervals[-1]["last_confirmed_date"] = date
            intervals[-1]["updated_at"] = date
            intervals[-1]["holdings"] = holdings
            intervals[-1]["target_total_exposure"] = target_total_exposure
            continue
        intervals.append(
            {
                "first_effective_date": date,
                "last_confirmed_date": date,
                "updated_at": date,
                "target_total_exposure": target_total_exposure,
                "holdings": holdings,
                "content_hash": content_hash,
                "source": "snapshot_backfill",
            }
        )
    return intervals[-SUGGESTION_INTERVAL_LIMIT:]


def _collapse_intervals(intervals: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = [item for item in intervals if item.get("first_effective_date") and item.get("last_confirmed_date")]
    normalized.sort(key=lambda item: (str(item["first_effective_date"]), str(item["last_confirmed_date"])))
    deduped: list[dict[str, Any]] = []
    for item in normalized:
        same_range = (
            deduped
            and deduped[-1]["first_effective_date"] == item["first_effective_date"]
            and deduped[-1]["last_confirmed_date"] == item["last_confirmed_date"]
        )
        if same_range:
            deduped[-1] = item
            continue
        deduped.append(item)
    collapsed: list[dict[str, Any]] = []
    for item in deduped:
        if collapsed and collapsed[-1]["content_hash"] == item["content_hash"]:
            collapsed[-1]["last_confirmed_date"] = max(str(collapsed[-1]["last_confirmed_date"]), str(item["last_confirmed_date"]))
            collapsed[-1]["updated_at"] = max(str(collapsed[-1]["updated_at"]), str(item["updated_at"]))
            collapsed[-1]["target_total_exposure"] = item["target_total_exposure"]
            collapsed[-1]["holdings"] = item["holdings"]
            collapsed[-1]["source"] = "persisted"
            continue
        collapsed.append(item)
    return collapsed[-SUGGESTION_INTERVAL_LIMIT:]


def load_interval_archive(result_dir: Path) -> list[dict[str, Any]]:
    path = result_dir / INTERVAL_FILENAME
    if not path.exists():
        return []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    intervals = payload.get("intervals") if isinstance(payload, dict) else payload
    if not isinstance(intervals, list):
        return []
    normalized: list[dict[str, Any]] = []
    for interval in intervals:
        if not isinstance(interval, dict):
            continue
        target_total_exposure = float(interval.get("target_total_exposure", 0.0))
        holdings = canonicalize_holdings_for_exposure(interval.get("holdings") or [], target_total_exposure)
        content_hash = build_suggestion_content_hash(target_total_exposure, holdings)
        normalized.append(
            {
                "first_effective_date": str(interval.get("first_effective_date") or ""),
                "last_confirmed_date": str(interval.get("last_confirmed_date") or ""),
                "updated_at": str(interval.get("updated_at") or interval.get("last_confirmed_date") or ""),
                "target_total_exposure": target_total_exposure,
                "holdings": holdings,
                "content_hash": content_hash,
                "source": str(interval.get("source") or "persisted"),
            }
        )
    return _collapse_intervals(normalized)


def _load_latest_holdings(latest_weights_path: Path) -> list[dict[str, Any]]:
    if not latest_weights_path.exists():
        return []
    try:
        frame = pd.read_csv(latest_weights_path)
    except Exception:
        return []
    holdings: list[dict[str, Any]] = []
    for row in frame.to_dict("records"):
        ts_code = str(row.get("ts_code") or "").strip()
        if not ts_code:
            continue
        holdings.append(
            {
                "ts_code": ts_code,
                "name": str(row.get("name") or ts_code),
                "weight": float(row.get("weight", 0.0)),
            }
        )
    return holdings


def sync_interval_archive(result_dir: Path) -> list[dict[str, Any]]:
    summary_path = result_dir / "summary.json"
    if not summary_path.exists():
        return []
    try:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    sample_end = str(summary.get("sample_end") or "")
    if not sample_end:
        return []
    latest_holdings = _load_latest_holdings(result_dir / "latest_weights.csv")
    target_total_exposure = target_exposure_from_holdings(latest_holdings)
    current_holdings = canonicalize_holdings_for_exposure(latest_holdings, target_total_exposure)
    current_hash = build_suggestion_content_hash(target_total_exposure, current_holdings)

    intervals = load_interval_archive(result_dir)
    if not intervals:
        intervals = _bootstrap_suggestion_intervals(result_dir / "weights_history.csv")
    if intervals and intervals[-1]["content_hash"] == current_hash:
        intervals[-1]["last_confirmed_date"] = max(str(intervals[-1]["last_confirmed_date"]), sample_end)
        intervals[-1]["updated_at"] = max(str(intervals[-1]["updated_at"]), sample_end)
        intervals[-1]["target_total_exposure"] = target_total_exposure
        intervals[-1]["holdings"] = current_holdings
        intervals[-1]["source"] = "persisted"
    else:
        intervals.append(
            {
                "first_effective_date": sample_end,
                "last_confirmed_date": sample_end,
                "updated_at": sample_end,
                "target_total_exposure": target_total_exposure,
                "holdings": current_holdings,
                "content_hash": current_hash,
                "source": "persisted",
            }
        )
    intervals = _collapse_intervals(intervals)
    payload = {
        "sample_end": sample_end,
        "intervals": intervals,
    }
    (result_dir / INTERVAL_FILENAME).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return intervals


def sync_interval_archives_from_frame(frame: pd.DataFrame, result_root: Path, id_column: str) -> int:
    if frame.empty or id_column not in frame.columns or "sample_tag" not in frame.columns:
        return 0
    updated = 0
    dedup = frame[[id_column, "sample_tag"]].dropna().drop_duplicates()
    for row in dedup.to_dict("records"):
        strategy_id = str(row[id_column])
        sample_tag = str(row["sample_tag"])
        result_dir = result_root / f"{strategy_id}__{sample_tag}"
        if not (result_dir / "summary.json").exists():
            continue
        sync_interval_archive(result_dir)
        updated += 1
    return updated
