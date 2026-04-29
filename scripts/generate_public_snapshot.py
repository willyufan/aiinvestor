"""
generate_public_snapshot.py

为 valselee.com/strategy.html 生成公开可读的策略快照。
输出：results/public_snapshot.json

使用方法：
    python scripts/generate_public_snapshot.py

每次更新策略后运行，然后 git push 即可。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.export_live_platform_data import (
    _load_sample_view,
    build_strategy_detail_payload,
    guess_sample_tag,
    latest_market_data_as_of,
    SAMPLE_LABELS,
    SAMPLE_TAGS,
    load_json,
    pick_preferred_sample_tag,
)

RESULTS_DIR = ROOT / "results"
HK_RESULTS_DIR = ROOT / "results_hkconnect"
TRACKED_WINNERS_JSON = RESULTS_DIR / "weighted_track_winners.json"
HK_TRACKED_WINNERS_JSON = HK_RESULTS_DIR / "tracked_winners_hkconnect.json"
OUTPUT_PATH = RESULTS_DIR / "public_snapshot.json"
STRATEGIES_DIR = RESULTS_DIR / "strategies"

WINDOW_TRACK_KEYS = ["since_2017_only", "since_2020_only", "since_2023_only", "since_2025_only"]
WINDOW_LABELS = {
    "since_2017_only": "2017 窗口",
    "since_2020_only": "2020 窗口",
    "since_2023_only": "2023 窗口",
    "since_2025_only": "2025 窗口",
}
SAMPLE_TAG_MAP = {
    "since_2017_only": "since_2017_01",
    "since_2020_only": "since_2020_01",
    "since_2023_only": "since_2023_01",
    "since_2025_only": "since_2025_01",
}
SAMPLE_TAG_DISPLAY = {
    "since_2017_01": "2017",
    "since_2020_01": "2020",
    "since_2023_01": "2023",
    "since_2025_01": "2025",
    "since_2026_01": "2026",
}


def build_window_metrics(strategy_id: str, strategies_map: dict[str, Any]) -> list[dict]:
    """Multi-window CAGR/Sharpe/MaxDD for chart display."""
    windows = strategies_map.get(strategy_id, {}).get("windows", {})
    result = []
    for tag, label in SAMPLE_TAG_DISPLAY.items():
        if tag not in windows:
            continue
        w = windows[tag]
        result.append({
            "tag":          tag,
            "label":        label,
            "cagr":         round(float(w.get("cagr", 0)), 4),
            "sharpe":       round(float(w.get("sharpe", 0)), 4),
            "max_drawdown": round(float(w.get("max_drawdown", 0)), 4),
            "total_return": round(float(w.get("total_return", 0)), 4),
        })
    return result


def build_strategy_entry(
    strategy_id: str,
    track_key: str,
    path_name: str,
    strategies_map: dict[str, Any],
    market_scope: str = "a_share",
) -> dict[str, Any]:
    sample_tag = SAMPLE_TAG_MAP.get(track_key, guess_sample_tag(track_key))
    view = _load_sample_view(strategy_id, sample_tag, market_scope=market_scope)

    base_name = strategies_map.get(strategy_id, {}).get("strategy_base_name", strategy_id)
    metrics = {}
    if view:
        m = view.get("summary_metrics", {})
        metrics = {
            "cagr":         round(m.get("cagr", 0.0), 4),
            "sharpe":       round(m.get("sharpe_ratio", 0.0), 4),
            "max_drawdown": round(m.get("max_drawdown", 0.0), 4),
            "total_return": round(m.get("total_return", 0.0), 4),
            "turnover":     round(m.get("average_annual_turnover", 0.0), 4),
        }

    latest_weights: list[dict] = []
    if view:
        for row in view.get("latest_weights", []):
            latest_weights.append({
                "ts_code": row["ts_code"],
                "name":    row["name"],
                "weight":  round(float(row["weight"]), 6),
            })

    sched = view.get("formal_schedule", {}) if view else {}
    market_data_as_of = latest_market_data_as_of(market_scope)
    return {
        "strategy_id":           strategy_id,
        "display_name":          base_name,
        "path":                  path_name,
        "market_scope":          market_scope,
        "winner_type":           SAMPLE_LABELS.get(track_key, track_key),
        "window_label":          WINDOW_LABELS.get(track_key, track_key),
        "sample_tag":            sample_tag,
        "risk_state":            view.get("risk_state", "unknown") if view else "unknown",
        "target_exposure":       round(float(view.get("target_total_exposure", 1.0)), 4) if view else 1.0,
        "updated_at":            view.get("updated_at", "") if view else "",
        "data_as_of":            market_data_as_of or sched.get("data_as_of") or (view.get("updated_at", "") if view else ""),
        "signal_effective_date": sched.get("suggestion_effective_date") or (view.get("updated_at", "") if view else ""),
        "metrics":               metrics,
        "window_metrics":        build_window_metrics(strategy_id, strategies_map),
        "latest_weights":        latest_weights,
    }


def build_hk_entries(hk_payload: dict[str, Any]) -> list[dict]:
    """Build HK Connect strategy entries.
    HK JSON structure: tracks.path1.since_2017_01.winner / tracks.path2.since_2017_01.winner
    """
    entries = []
    strategies_map = hk_payload.get("strategies", {})
    seen: set[str] = set()
    for path_name in ["path1", "path2"]:
        path_tracks = hk_payload.get("tracks", {}).get(path_name, {})
        for sample_tag, track_data in path_tracks.items():
            if not isinstance(track_data, dict):
                continue
            strategy_id = str(track_data.get("winner", ""))
            if not strategy_id or strategy_id in seen:
                continue
            seen.add(strategy_id)
            # derive track_key from sample_tag for window label
            track_key = next((k for k, v in SAMPLE_TAG_MAP.items() if v == sample_tag), sample_tag)
            view = _load_sample_view(strategy_id, sample_tag, market_scope="hkconnect")
            base_name = strategies_map.get(strategy_id, {}).get("strategy_base_name", strategy_id)
            # Use metrics from JSON if view unavailable
            raw_metrics = track_data.get("metrics", {})
            metrics: dict = {}
            if view:
                m = view.get("summary_metrics", {})
                metrics = {
                    "cagr":         round(m.get("cagr", 0.0), 4),
                    "sharpe":       round(m.get("sharpe_ratio", 0.0), 4),
                    "max_drawdown": round(m.get("max_drawdown", 0.0), 4),
                    "total_return": round(m.get("total_return", 0.0), 4),
                    "turnover":     round(m.get("average_annual_turnover", 0.0), 4),
                }
            elif raw_metrics:
                metrics = {
                    "cagr":         round(float(raw_metrics.get("cagr", 0)), 4),
                    "sharpe":       round(float(raw_metrics.get("sharpe_ratio", 0)), 4),
                    "max_drawdown": round(float(raw_metrics.get("max_drawdown", 0)), 4),
                    "total_return": round(float(raw_metrics.get("total_return", 0)), 4),
                    "turnover":     round(float(raw_metrics.get("average_annual_turnover", 0)), 4),
                }
            latest_weights: list[dict] = []
            if view:
                for row in view.get("latest_weights", []):
                    latest_weights.append({
                        "ts_code": row["ts_code"],
                        "name":    row["name"],
                        "weight":  round(float(row["weight"]), 6),
                    })
            sched = view.get("formal_schedule", {}) if view else {}
            market_data_as_of = latest_market_data_as_of("hkconnect")
            entries.append({
                "strategy_id":           strategy_id,
                "display_name":          base_name,
                "path":                  path_name,
                "market_scope":          "hkconnect",
                "winner_type":           SAMPLE_LABELS.get(track_key, sample_tag),
                "window_label":          WINDOW_LABELS.get(track_key, sample_tag),
                "sample_tag":            sample_tag,
                "risk_state":            view.get("risk_state", "unknown") if view else "unknown",
                "target_exposure":       round(float(view.get("target_total_exposure", 1.0)), 4) if view else 1.0,
                "updated_at":            view.get("updated_at", "") if view else "",
                "data_as_of":            market_data_as_of or sched.get("data_as_of") or (view.get("updated_at", "") if view else ""),
                "signal_effective_date": sched.get("suggestion_effective_date") or (view.get("updated_at", "") if view else ""),
                "metrics":               metrics,
                "window_metrics":        build_window_metrics(strategy_id, strategies_map),
                "latest_weights":        latest_weights,
            })
    return entries


def flatten_snapshots(history_windows: list[dict]) -> list[dict]:
    """Deduplicate and sort all historical snapshots from history_windows."""
    seen: set[str] = set()
    all_snaps: list[dict] = []
    for window in history_windows:
        for snap in window.get("snapshots", []):
            date = str(snap.get("date", ""))
            if not date or date in seen:
                continue
            seen.add(date)
            all_snaps.append({
                "date": date,
                "holdings": [
                    {"ts_code": str(r["ts_code"]), "name": str(r["name"]), "weight": round(float(r["weight"]), 6)}
                    for r in snap.get("holdings", [])
                ],
            })
    all_snaps.sort(key=lambda x: x["date"])
    return all_snaps


def export_strategy_detail(
    strategy_id: str,
    display_name: str,
    market_scope: str,
    path: str,
    winner_type: str,
) -> None:
    """Export per-strategy detail JSON for strategy.html detail tab."""
    preferred_tag = pick_preferred_sample_tag(strategy_id, market_scope=market_scope)
    try:
        detail = build_strategy_detail_payload(strategy_id, preferred_tag, market_scope=market_scope)
    except FileNotFoundError:
        return
    sample_views_out: dict[str, Any] = {}
    market_data_as_of = latest_market_data_as_of(market_scope)
    for tag, view in (detail.get("sample_views") or {}).items():
        formal_schedule = dict(view.get("formal_schedule", {}))
        if market_data_as_of:
            formal_schedule["data_as_of"] = market_data_as_of
        sample_views_out[tag] = {
            "sample_tag": tag,
            "sample_tag_label": view.get("sample_tag_label", tag),
            "summary_meta": view.get("summary_meta", {}),
            "risk_state": view.get("risk_state", "unknown"),
            "target_total_exposure": round(float(view.get("target_total_exposure", 1.0)), 4),
            "latest_weights": [
                {"ts_code": str(r["ts_code"]), "name": str(r["name"]), "weight": round(float(r["weight"]), 6)}
                for r in (view.get("latest_weights") or [])
            ],
            "formal_schedule": formal_schedule,
            "equity_curve_points": [
                {"date": str(p["date"]), "nav": round(float(p["nav"]), 6)}
                for p in (view.get("equity_curve_points") or [])
            ],
            "snapshots": flatten_snapshots(view.get("history_windows") or []),
        }

    if not sample_views_out:
        return

    out = {
        "strategy_id": detail.get("strategy_id", strategy_id),
        "display_name": detail.get("display_name", display_name),
        "market_scope": detail.get("market_scope", market_scope),
        "path": path,
        "winner_type": winner_type,
        "sample_views": sample_views_out,
    }
    STRATEGIES_DIR.mkdir(parents=True, exist_ok=True)
    dest = STRATEGIES_DIR / f"{strategy_id}.json"
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    payload = load_json(TRACKED_WINNERS_JSON)
    strategies_map: dict[str, Any] = payload.get("strategies", {})
    as_of: str = payload.get("as_of", "")

    # ── A股 Path 1 ──
    path1_entries: list[dict] = []
    for track_key in WINDOW_TRACK_KEYS:
        track = payload["tracks"].get(track_key)
        if not track:
            continue
        entry = build_strategy_entry(track["winner"], track_key, "path1", strategies_map)
        path1_entries.append(entry)

    # ── A股 Path 2 ──
    path2_entries: list[dict] = []
    for track_key in WINDOW_TRACK_KEYS:
        track = payload["path2"]["tracks"].get(track_key)
        if not track:
            continue
        entry = build_strategy_entry(track["winner"], track_key, "path2", strategies_map)
        path2_entries.append(entry)

    # ── 沪港通 ──
    hk_entries: list[dict] = []
    if HK_TRACKED_WINNERS_JSON.exists():
        hk_payload = load_json(HK_TRACKED_WINNERS_JSON)
        hk_entries = build_hk_entries(hk_payload)

    snapshot = {
        "as_of":   as_of,
        "path1":   path1_entries,
        "path2":   path2_entries,
        "hkconnect": hk_entries,
    }

    OUTPUT_PATH.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total = len(path1_entries) + len(path2_entries) + len(hk_entries)
    print(f"✓ Exported {len(path1_entries)} path1 + {len(path2_entries)} path2 + {len(hk_entries)} hkconnect entries → {OUTPUT_PATH}")

    # ── Per-strategy detail files ──
    all_entries = path1_entries + path2_entries + hk_entries
    seen_ids: set[str] = set()
    detail_count = 0
    for entry in all_entries:
        sid = entry["strategy_id"]
        if sid in seen_ids:
            continue
        seen_ids.add(sid)
        export_strategy_detail(
            strategy_id=sid,
            display_name=entry["display_name"],
            market_scope=entry["market_scope"],
            path=entry["path"],
            winner_type=entry["winner_type"],
        )
        detail_count += 1
    for stale_path in STRATEGIES_DIR.glob("*.json"):
        if stale_path.stem not in seen_ids:
            stale_path.unlink()
    print(f"✓ Exported {detail_count} strategy detail files → {STRATEGIES_DIR}/")


if __name__ == "__main__":
    main()
