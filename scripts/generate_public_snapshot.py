"""
generate_public_snapshot.py

为 valselee.com/strategy.html 生成公开可读的策略快照。
输出：results/research/a_share/public_snapshot.json

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
    LIVE_DIR,
    _load_sample_view,
    build_strategy_detail_payload,
    guess_sample_tag,
    HK_EXPERIMENTAL_PATH_NAMES,
    HK_TRACKED_PATH_NAMES,
    latest_market_data_as_of,
    SAMPLE_LABELS,
    load_json,
    pick_preferred_sample_tag,
)
from scripts.results_layout import existing_research_file, market_research_dir, research_file

TRACKED_WINNERS_JSON = existing_research_file("weighted_track_winners.json")
HK_TRACKED_WINNERS_JSON = existing_research_file("tracked_winners_hkconnect.json", market_scope="hkconnect")
STRATEGY_REGISTRY_JSON = LIVE_DIR / "strategy_registry.json"
OUTPUT_PATH = research_file("public_snapshot.json")
STRATEGIES_DIR = market_research_dir("a_share") / "strategies"

WINDOW_TRACK_KEYS = ["since_2017_only", "since_2020_only", "since_2023_only", "since_2025_only", "since_2026_only"]
WINDOW_LABELS = {
    "since_2017_only": "2017 窗口",
    "since_2020_only": "2020 窗口",
    "since_2023_only": "2023 窗口",
    "since_2025_only": "2025 窗口",
    "since_2026_only": "2026 窗口",
    "since_2026_01": "2026 窗口",
}
SAMPLE_TAG_MAP = {
    "since_2017_only": "since_2017_01",
    "since_2020_only": "since_2020_01",
    "since_2023_only": "since_2023_01",
    "since_2025_only": "since_2025_01",
    "since_2026_only": "since_2026_01",
}
SAMPLE_TAG_DISPLAY = {
    "since_2017_01": "2017",
    "since_2020_01": "2020",
    "since_2023_01": "2023",
    "since_2025_01": "2025",
    "since_2026_01": "2026",
}


def _float_metric(metrics: dict[str, Any], keys: tuple[str, ...]) -> float:
    for key in keys:
        value = metrics.get(key)
        if value is None:
            continue
        try:
            return float(value)
        except (TypeError, ValueError):
            continue
    return 0.0


def _public_leaderboard_metrics(metrics: dict[str, Any]) -> dict[str, float]:
    """Normalize A-share weighted metrics and HK raw metrics into the public shape."""
    if not metrics:
        return {}
    return {
        "weighted_cagr": round(_float_metric(metrics, ("weighted_cagr", "cagr")), 4),
        "weighted_sharpe": round(_float_metric(metrics, ("weighted_sharpe", "sharpe_ratio", "sharpe")), 4),
        "weighted_max_drawdown": round(_float_metric(metrics, ("weighted_max_drawdown", "max_drawdown")), 4),
    }


def build_leaderboards() -> dict[str, Any]:
    """Export winner_leaderboards from strategy_registry.json for public consumption."""
    if not STRATEGY_REGISTRY_JSON.exists():
        return {}
    registry = load_json(STRATEGY_REGISTRY_JSON)
    raw = registry.get("winner_leaderboards", {})
    result: dict[str, Any] = {}
    for market_key, paths in raw.items():  # "a_share", "hkconnect"
        result[market_key] = {}
        for path_key, tracks in paths.items():  # "path1", "path2", ...
            result[market_key][path_key] = {}
            for track_key, track_data in tracks.items():  # "since_2017_only", ...
                entries_out = []
                for e in (track_data.get("entries") or []):
                    entries_out.append({
                        "rank": int(e.get("rank", 0)),
                        "strategy_base_id": str(e.get("strategy_base_id", "")),
                        "strategy_base_name": str(e.get("strategy_base_name", "")),
                        "is_official_winner": bool(e.get("is_official_winner", False)),
                        "metrics": _public_leaderboard_metrics(e.get("metrics") or {}),
                    })
                result[market_key][path_key][track_key] = {
                    "label": WINDOW_LABELS.get(track_key, track_key),
                    "sample_tag": str(track_data.get("sample_tag", "")),
                    "entries": entries_out,
                }
    return result


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
    experimental: bool = False,
    tracked_only: bool = False,
    frequency: str = "",
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
        "experimental":          experimental,
        "tracked_only":          tracked_only,
        "frequency":             frequency,
        "metrics":               metrics,
        "window_metrics":        build_window_metrics(strategy_id, strategies_map),
        "latest_weights":        latest_weights,
    }


def build_hk_entries(hk_payload: dict[str, Any]) -> list[dict]:
    """Build HK Connect strategy entries.
    HK JSON structure: tracks.path1.since_2017_01.winner / tracks.path2.since_2017_01.winner / ...
    """
    entries = []
    strategies_map = hk_payload.get("strategies", {})
    seen: set[str] = set()
    for path_name in HK_TRACKED_PATH_NAMES:
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
            strategy_meta = strategies_map.get(strategy_id, {})
            base_name = strategy_meta.get("strategy_base_name") or strategy_meta.get("strategy_name") or strategy_id
            is_experimental = path_name in HK_EXPERIMENTAL_PATH_NAMES
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
                "experimental":          is_experimental,
                "tracked_only":          is_experimental,
                "frequency":             str(strategy_meta.get("rebalance_frequency") or ""),
            })
    return entries


def flatten_snapshots(history_windows: list[dict]) -> list[dict]:
    """Deduplicate and sort all historical snapshots from history_windows."""
    seen: set[str] = set()
    all_snaps: list[dict] = []
    for window in history_windows:
        for snap in window.get("snapshots", []):
            date = str(snap.get("date", ""))
            event_type = str(snap.get("event_type") or "holding_snapshot")
            history_key = f"{date}:{event_type}"
            if not date or history_key in seen:
                continue
            seen.add(history_key)
            out = {
                "date": date,
                "event_type": event_type,
                "holdings": [
                    {"ts_code": str(r["ts_code"]), "name": str(r["name"]), "weight": round(float(r["weight"]), 6)}
                    for r in snap.get("holdings", [])
                ],
            }
            if snap.get("overlay_event"):
                event = snap["overlay_event"]
                out["overlay_event"] = {
                    "signal_date": str(event.get("signal_date") or event.get("date") or ""),
                    "trade_date": str(event.get("trade_date") or event.get("date") or ""),
                    "risk_stage": str(event.get("risk_stage") or ""),
                    "raw_risk_stage": str(event.get("raw_risk_stage") or ""),
                    "one_way_turnover": round(float(event.get("one_way_turnover") or 0.0), 6),
                    "two_way_turnover": round(float(event.get("two_way_turnover") or 0.0), 6),
                    "buy_amount": round(float(event.get("buy_amount") or 0.0), 6),
                    "sell_amount": round(float(event.get("sell_amount") or 0.0), 6),
                    "buy_amount_pct_nav": round(float(event.get("buy_amount_pct_nav") or 0.0), 6),
                    "sell_amount_pct_nav": round(float(event.get("sell_amount_pct_nav") or 0.0), 6),
                    "trading_cost": round(float(event.get("trading_cost") or 0.0), 6),
                    "trading_cost_pct_nav": round(float(event.get("trading_cost_pct_nav") or 0.0), 6),
                    "is_trade": bool(event.get("is_trade")),
                    "trade_details": [
                        {
                            "ts_code": str(item.get("ts_code") or ""),
                            "name": str(item.get("name") or ""),
                            "side": str(item.get("side") or ""),
                            "current_weight": round(float(item.get("current_weight") or 0.0), 6),
                            "post_trade_weight": round(float(item.get("post_trade_weight") or 0.0), 6),
                            "diff_weight": round(float(item.get("diff_weight") or 0.0), 6),
                            "gross_amount_pct_nav": round(float(item.get("gross_amount_pct_nav") or 0.0), 6),
                            "fee_pct_nav": round(float(item.get("fee_pct_nav") or 0.0), 6),
                        }
                        for item in event.get("trade_details", [])
                        if isinstance(item, dict)
                    ],
                }
            all_snaps.append(out)
    all_snaps.sort(key=lambda x: x["date"])
    return all_snaps


def _export_preview(preview: dict) -> dict:
    """Slim down month_end_preview for public JSON."""
    if not preview or not preview.get("holdings"):
        return {}
    return {
        "preview_as_of":        str(preview.get("preview_as_of") or ""),
        "formal_signal_date":   str(preview.get("formal_signal_date") or ""),
        "risk_state":           str(preview.get("risk_state") or ""),
        "target_total_exposure": round(float(preview.get("target_total_exposure") or 0.0), 4),
        "market_momentum":      round(float(preview.get("market_momentum")), 4) if preview.get("market_momentum") is not None else None,
        "holdings": [
            {"ts_code": str(r["ts_code"]), "name": str(r["name"]), "weight": round(float(r["weight"]), 6)}
            for r in (preview.get("holdings") or [])
            if r.get("ts_code") and str(r["ts_code"]) != "CASH"
        ],
    }


def export_strategy_detail(
    strategy_id: str,
    display_name: str,
    market_scope: str,
    path: str,
    winner_type: str,
    experimental: bool = False,
    tracked_only: bool = False,
    frequency: str = "",
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
        raw_split = view.get("split_view") or {}
        split_view_out: dict[str, Any] = {}
        if raw_split.get("mode") == "satellite_weekly_overlay":
            overlay_summary = raw_split.get("overlay_summary") or {}
            split_view_out = {
                "mode": "satellite_weekly_overlay",
                "basket_weights": [
                    {"ts_code": str(r["ts_code"]), "name": str(r["name"]), "weight": round(float(r["weight"]), 6)}
                    for r in (raw_split.get("basket_weights") or [])
                ],
                "overlay_summary": {
                    "risk_state":                str(overlay_summary.get("risk_state") or ""),
                    "target_total_exposure":     round(float(overlay_summary.get("target_total_exposure") or 0.0), 4),
                    "core_exposure_target":      round(float(overlay_summary.get("core_exposure_target") or 0.0), 4),
                    "satellite_exposure_target": round(float(overlay_summary.get("satellite_exposure_target") or 0.0), 4),
                    "market_12_1_momentum":      round(float(overlay_summary.get("market_12_1_momentum") or 0.0), 4) if overlay_summary.get("market_12_1_momentum") is not None else None,
                    "weekly_overlay_trade_count": int(overlay_summary.get("weekly_overlay_trade_count") or 0),
                    "latest_overlay_trade_date": str(overlay_summary.get("latest_overlay_trade_date") or ""),
                    "latest_overlay_date":       str(overlay_summary.get("latest_overlay_date") or ""),
                },
                "overlay_history": [
                    {
                        "date":                  str(row.get("date") or ""),
                        "signal_date":           str(row.get("signal_date") or row.get("date") or ""),
                        "trade_date":            str(row.get("trade_date") or row.get("date") or ""),
                        "risk_stage":            str(row.get("risk_stage") or ""),
                        "is_trade":              bool(row.get("is_trade")),
                        "one_way_turnover":      round(float(row.get("one_way_turnover") or 0.0), 6),
                        "two_way_turnover":      round(float(row.get("two_way_turnover") or 0.0), 6),
                        "buy_amount_pct_nav":    round(float(row.get("buy_amount_pct_nav") or 0.0), 6),
                        "sell_amount_pct_nav":   round(float(row.get("sell_amount_pct_nav") or 0.0), 6),
                        "trading_cost_pct_nav":  round(float(row.get("trading_cost_pct_nav") or 0.0), 6),
                        "trade_details": [
                            {
                                "ts_code":             str(item.get("ts_code") or ""),
                                "name":                str(item.get("name") or ""),
                                "side":                str(item.get("side") or ""),
                                "current_weight":      round(float(item.get("current_weight") or 0.0), 6),
                                "post_trade_weight":   round(float(item.get("post_trade_weight") or 0.0), 6),
                                "diff_weight":         round(float(item.get("diff_weight") or 0.0), 6),
                                "gross_amount_pct_nav":round(float(item.get("gross_amount_pct_nav") or 0.0), 6),
                            }
                            for item in (row.get("trade_details") or [])
                            if isinstance(item, dict)
                        ],
                    }
                    for row in (raw_split.get("overlay_history") or [])
                ],
            }
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
            "split_view": split_view_out,
            "month_end_preview": _export_preview(view.get("month_end_preview") or {}),
        }

    if not sample_views_out:
        return

    out = {
        "strategy_id": detail.get("strategy_id", strategy_id),
        "display_name": detail.get("display_name", display_name),
        "market_scope": detail.get("market_scope", market_scope),
        "path": path,
        "winner_type": winner_type,
        "experimental": experimental,
        "tracked_only": tracked_only,
        "frequency": frequency,
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

    # ── A股 Path 3 ──
    path3_entries: list[dict] = []
    path3_payload = payload.get("path3") or {}
    for track_key in WINDOW_TRACK_KEYS:
        track = (path3_payload.get("tracks") or {}).get(track_key)
        if not track:
            continue
        entry = build_strategy_entry(track["winner"], track_key, "path3", strategies_map)
        path3_entries.append(entry)

    # ── A股 Path 4：强主题涌现观察路径 ──
    path4_entries: list[dict] = []
    path4_payload = payload.get("path4") or {}
    path4_experimental = bool(path4_payload.get("experimental", True))
    path4_tracked_only = bool(path4_payload.get("tracked_only", True))
    path4_frequency = str(path4_payload.get("frequency") or "monthly")
    for track_key in WINDOW_TRACK_KEYS:
        track = (path4_payload.get("tracks") or {}).get(track_key)
        if not track:
            continue
        entry = build_strategy_entry(
            track["winner"],
            track_key,
            "path4",
            strategies_map,
            experimental=path4_experimental,
            tracked_only=path4_tracked_only,
            frequency=path4_frequency,
        )
        path4_entries.append(entry)

    # ── 沪港通 ──
    hk_entries: list[dict] = []
    hk_strategy_meta: dict[str, Any] = {}
    if HK_TRACKED_WINNERS_JSON.exists():
        hk_payload = load_json(HK_TRACKED_WINNERS_JSON)
        hk_strategy_meta = hk_payload.get("strategies", {})
        hk_entries = build_hk_entries(hk_payload)

    leaderboards = build_leaderboards()

    snapshot = {
        "as_of": as_of,
        "path1": path1_entries,
        "path2": path2_entries,
        "path3": path3_entries,
        "path4": path4_entries,
        "hkconnect": hk_entries,
        "leaderboards": leaderboards,
    }

    OUTPUT_PATH.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total = len(path1_entries) + len(path2_entries) + len(path3_entries) + len(path4_entries) + len(hk_entries)
    print(f"✓ Exported {len(path1_entries)} path1 + {len(path2_entries)} path2 + {len(path3_entries)} path3 + {len(path4_entries)} path4 + {len(hk_entries)} hkconnect entries → {OUTPUT_PATH}")

    # ── Per-strategy detail files ──
    all_entries = path1_entries + path2_entries + path3_entries + path4_entries + hk_entries
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
            experimental=bool(entry.get("experimental", False)),
            tracked_only=bool(entry.get("tracked_only", False)),
            frequency=str(entry.get("frequency", "")),
        )
        detail_count += 1
    for market_scope, path_payload in leaderboards.items():
        if not isinstance(path_payload, dict):
            continue
        for path_name, tracks in path_payload.items():
            if not isinstance(tracks, dict):
                continue
            for track_key, leaderboard in tracks.items():
                if not isinstance(leaderboard, dict):
                    continue
                for entry in leaderboard.get("entries") or []:
                    strategy_id = str(entry.get("strategy_base_id") or entry.get("strategy_id") or "")
                    if not strategy_id or strategy_id in seen_ids:
                        continue
                    experimental = False
                    tracked_only = False
                    frequency = ""
                    if str(market_scope) == "a_share" and str(path_name) == "path4":
                        experimental = path4_experimental
                        tracked_only = path4_tracked_only
                        frequency = path4_frequency
                    elif str(market_scope) == "hkconnect" and str(path_name) in HK_EXPERIMENTAL_PATH_NAMES:
                        experimental = True
                        tracked_only = True
                        frequency = str((hk_strategy_meta.get(strategy_id) or {}).get("rebalance_frequency") or "")
                    export_strategy_detail(
                        strategy_id=strategy_id,
                        display_name=str(entry.get("strategy_base_name") or strategy_id),
                        market_scope=str(market_scope),
                        path=str(path_name),
                        winner_type="leaderboard candidate",
                        experimental=experimental,
                        tracked_only=tracked_only,
                        frequency=frequency,
                    )
                    seen_ids.add(strategy_id)
                    detail_count += 1
    for stale_path in STRATEGIES_DIR.glob("*.json"):
        if stale_path.stem not in seen_ids:
            stale_path.unlink()
    print(f"✓ Exported {detail_count} strategy detail files → {STRATEGIES_DIR}/")


if __name__ == "__main__":
    main()
