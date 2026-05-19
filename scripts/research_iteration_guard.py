from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import pandas as pd

# sys.path manipulation must happen BEFORE any `scripts.*` or sibling-module
# imports so the script works both when run directly (python scripts/foo.py)
# and when imported as a module (python -m scripts.foo) — previously the
# `path2_candidate_pass` import below relied on Python's implicit add of
# the script's own directory to sys.path, which only fires under the first
# invocation pattern.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.path2_candidate_pass import _parse_python_constants
from scripts.results_layout import existing_research_file, research_file
from scripts.winner_id_utils import load_json as _shared_load_json

BACKTEST_SCRIPT_PATH = ROOT / "backtest_marketcap_etf.py"

DEFAULT_COMPARISON_CSV = existing_research_file("strategy_comparison.csv")
DEFAULT_PATH2_PASS_JSON = existing_research_file("path2_candidate_pass.json")
DEFAULT_WINNER_PASS_JSON = existing_research_file("winner_only_pass.json")
DEFAULT_WEIGHTED_WINNERS_JSON = existing_research_file("weighted_track_winners.json")
DEFAULT_HK_COMPARISON_CSV = existing_research_file("strategy_comparison_hkconnect.csv", market_scope="hkconnect")
DEFAULT_HK_TRACKED_JSON = existing_research_file("tracked_winners_hkconnect.json", market_scope="hkconnect")

DEFAULT_REPORT_JSON = research_file("research_iteration_report.json")
DEFAULT_STATE_JSON = research_file("research_iteration_state.json")
DEFAULT_EXPERIMENT_LOG = research_file("research_experiments.jsonl")

A_SHARE_REQUIRED_WINDOWS = ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01")
A_SHARE_OBSERVATION_WINDOWS = (*A_SHARE_REQUIRED_WINDOWS, "since_2026_01")
HK_REQUIRED_WINDOWS = (*A_SHARE_REQUIRED_WINDOWS, "since_2026_01")

PATH1_MIN_DIRECTION_COUNTS = {
    "promotion_ramp": 4,
    "satellite_defense": 4,
    "signal_variants": 2,
    "core_multifactor": 9,
    "holding_shape": 4,
    "supporting_variants": 4,
}

PATH_FOCUS_ROTATION = {
    "ashare_path1": [
        "core_multifactor_coverage",
        "signal_quality",
        "satellite_risk_cost",
        "holding_shape",
    ],
    "ashare_path2": [
        "medium_cycle_growth",
        "risk_reconfirm_sensitivity",
        "underrepresented_families",
        "capacity_and_cost_stress",
    ],
    "ashare_path3": [
        "turnover_reduction",
        "weekly_exit_buffer",
        "risk_downshift",
        "cost_stress",
    ],
    "ashare_path4": [
        "emergent_theme_coverage",
        "theme_signal_quality",
        "theme_risk_control",
        "theme_capacity_cost",
    ],
    "hkconnect_path1": [
        "monthly_weekly_overlay",
        "biweekly_buffer",
        "risk_overlay_cost",
    ],
    "hkconnect_path2": [
        "high_return_monthly",
        "biweekly_breakout",
        "elasticity_cost_control",
    ],
    "hkconnect_path3": [
        "weekly_turnover_reduction",
        "weekly_defensive_overlay",
        "cost_stress",
    ],
}


def _load_json(path: Path, default: Any) -> Any:
    """Thin wrapper around :func:`scripts.winner_id_utils.load_json`.

    Kept for call-site stability — the shared helper signature accepts an
    optional default while local callers always pass one explicitly, so
    we forward through unchanged.
    """
    return _shared_load_json(path, default)


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _read_latest_csv(path: Path, id_col: str) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    frame = pd.read_csv(path)
    if frame.empty or id_col not in frame.columns or "sample_tag" not in frame.columns:
        return pd.DataFrame()
    latest = frame.copy()
    latest[id_col] = latest[id_col].astype(str)
    latest["sample_tag"] = latest["sample_tag"].astype(str)
    if "sample_end" in latest.columns:
        latest["sample_end"] = pd.to_datetime(latest["sample_end"], errors="coerce")
        latest = latest.sort_values([id_col, "sample_tag", "sample_end"])
        latest = latest.groupby([id_col, "sample_tag"], as_index=False).tail(1)
    return latest


def _window_map(frame: pd.DataFrame, id_col: str) -> dict[str, set[str]]:
    if frame.empty:
        return {}
    result: dict[str, set[str]] = {}
    for strategy_id, group in frame.groupby(id_col):
        result[str(strategy_id)] = set(group["sample_tag"].astype(str))
    return result


def _metrics_for(frame: pd.DataFrame, id_col: str, strategy_id: str, sample_tag: str) -> dict[str, float]:
    if frame.empty:
        return {}
    row = frame.loc[(frame[id_col].astype(str) == strategy_id) & (frame["sample_tag"].astype(str) == sample_tag)]
    if row.empty:
        return {}
    last = row.iloc[-1]
    metrics: dict[str, float] = {}
    for src, dst in (
        ("cagr", "cagr"),
        ("sharpe_ratio", "sharpe"),
        ("max_drawdown", "max_drawdown"),
        ("average_annual_turnover", "turnover"),
        ("total_return", "total_return"),
    ):
        if src in row.columns and pd.notna(last.get(src)):
            metrics[dst] = float(last[src])
    return metrics


def _stable_key(parts: Iterable[Any]) -> str:
    payload = json.dumps(list(parts), sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:20]


def _chunked(values: list[str], size: int) -> Iterable[list[str]]:
    for index in range(0, len(values), size):
        yield values[index : index + size]


def _build_rerun_commands(
    *,
    market: str,
    missing: list[dict[str, Any]],
    max_ids_per_command: int = 20,
) -> list[str]:
    grouped: dict[tuple[str, ...], list[str]] = {}
    for item in missing:
        windows = tuple(item.get("missing_windows") or [])
        if not windows:
            continue
        grouped.setdefault(windows, []).append(str(item["strategy_id"]))

    commands: list[str] = []
    for windows, strategy_ids in sorted(grouped.items(), key=lambda item: (item[0], item[1])):
        sample_tags = ",".join(windows)
        for chunk in _chunked(sorted(set(strategy_ids)), max_ids_per_command):
            if market == "hkconnect":
                commands.append(
                    ".venv/bin/python backtest_hkconnect.py "
                    f"--sample-tags {sample_tags} --only-strategy-ids {','.join(chunk)}"
                )
            else:
                commands.append(
                    ".venv/bin/python backtest_marketcap_etf.py "
                    f"--sample-tags {sample_tags} --only-base-ids {','.join(chunk)}"
                )
    return commands


def _coverage_scope(
    *,
    scope_id: str,
    market: str,
    path: str,
    candidates: Iterable[str],
    required_windows: Iterable[str],
    windows_by_id: dict[str, set[str]],
    blocking: bool,
    description: str,
) -> dict[str, Any]:
    required = tuple(required_windows)
    candidate_ids = sorted({str(candidate) for candidate in candidates if str(candidate).strip()})
    missing: list[dict[str, Any]] = []
    complete_count = 0
    for strategy_id in candidate_ids:
        available = windows_by_id.get(strategy_id, set())
        missing_windows = [window for window in required if window not in available]
        if missing_windows:
            missing.append(
                {
                    "strategy_id": strategy_id,
                    "available_windows": sorted(available),
                    "missing_windows": missing_windows,
                }
            )
        else:
            complete_count += 1

    coverage_ratio = (complete_count / len(candidate_ids)) if candidate_ids else 1.0
    return {
        "scope_id": scope_id,
        "market": market,
        "path": path,
        "description": description,
        "blocking": bool(blocking),
        "required_windows": list(required),
        "candidate_count": len(candidate_ids),
        "complete_count": complete_count,
        "missing_count": len(missing),
        "coverage_ratio": coverage_ratio,
        "status": "pass" if not missing else ("block" if blocking else "warn"),
        "missing": missing[:200],
        "missing_truncated": max(0, len(missing) - 200),
        "rerun_commands": _build_rerun_commands(market=market, missing=missing),
    }


def _load_backtest_constants() -> dict[str, Any]:
    return _parse_python_constants(
        BACKTEST_SCRIPT_PATH,
        [
            "WINNER_ONLY_STRATEGY_ID",
            "PATH1_FAST_PASS_DIRECTION_GROUPS",
            "PATH1_FAST_PASS_VARIANT_IDS",
            "PATH2_SCAN_FAMILY_RULES",
            "PATH4_THEME_DISCOVERY_BASE_IDS",
            "PATH4_THEME_DISCOVERY_VARIANT_IDS",
        ],
    )


def _extract_path1_candidates(constants: dict[str, Any]) -> tuple[dict[str, list[str]], list[str]]:
    base = str(constants.get("WINNER_ONLY_STRATEGY_ID") or "").strip()
    direction_groups_raw = constants.get("PATH1_FAST_PASS_DIRECTION_GROUPS") or {}
    direction_groups: dict[str, list[str]] = {}
    full_fast_ids: list[str] = []
    for group_name, variant_ids in direction_groups_raw.items():
        variants = [str(item) for item in variant_ids]
        full_ids = [f"{base}__{variant_id}" for variant_id in variants]
        direction_groups[str(group_name)] = full_ids
        full_fast_ids.extend(full_ids)
    if base:
        full_fast_ids.append(base)
    return direction_groups, sorted(set(full_fast_ids))


def _extract_path2_family_counts(path2_pass: dict[str, Any], constants: dict[str, Any]) -> dict[str, dict[str, Any]]:
    family_counts = path2_pass.get("family_candidate_counts") or {}
    family_rules = constants.get("PATH2_SCAN_FAMILY_RULES") or {}
    result: dict[str, dict[str, Any]] = {}
    for family_name in sorted(set(family_counts) | set(family_rules)):
        rule = family_rules.get(family_name) or {}
        result[str(family_name)] = {
            "current_count": int(family_counts.get(family_name) or 0),
            "target_representatives": int(rule.get("target_candidates") or 0),
        }
    return result


def _extract_path4_theme_candidates(constants: dict[str, Any]) -> list[str]:
    base_ids = [str(item) for item in constants.get("PATH4_THEME_DISCOVERY_BASE_IDS") or []]
    variant_ids = [str(item) for item in constants.get("PATH4_THEME_DISCOVERY_VARIANT_IDS") or []]
    return sorted(
        {
            f"{base_id}__{variant_id}"
            for base_id in base_ids
            for variant_id in variant_ids
            if base_id and variant_id
        }
    )


def _strategy_signature(weighted: dict[str, Any], hk_tracked: dict[str, Any]) -> dict[str, str]:
    signatures: dict[str, str] = {}

    path_sources = {
        "ashare_path1": weighted.get("tracks") or {},
        "ashare_path2": (weighted.get("path2") or {}).get("tracks") or {},
        "ashare_path3": (weighted.get("path3") or {}).get("tracks") or {},
    }
    for path_key, tracks in path_sources.items():
        winners: list[str] = []
        for track_key, meta in sorted(tracks.items()):
            if isinstance(meta, dict):
                winners.append(f"{track_key}:{meta.get('winner') or meta.get('strategy_base_id') or ''}")
        robust = weighted.get("tracks", {}).get("robust_candidate", {}) if path_key == "ashare_path1" else {}
        if path_key == "ashare_path2":
            robust = weighted.get("path2") or {}
        if path_key == "ashare_path3":
            robust = weighted.get("path3") or {}
        winners.append(f"robust:{robust.get('strategy_base_id') or ''}")
        signatures[path_key] = _stable_key(winners)

    hk_tracks = hk_tracked.get("tracks") or {}
    for path_name in ("path1", "path2", "path3"):
        path_meta = hk_tracks.get(path_name) or {}
        winners = []
        for track_key, meta in sorted(path_meta.items()):
            if track_key == "robust_candidate":
                winners.append(f"robust:{meta.get('strategy_id') or ''}")
            elif isinstance(meta, dict):
                winners.append(f"{track_key}:{meta.get('winner') or ''}")
        signatures[f"hkconnect_{path_name}"] = _stable_key(winners)

    return signatures


def _update_state(
    *,
    previous_state: dict[str, Any],
    signatures: dict[str, str],
    quotas: dict[str, Any],
    as_of: str,
    stagnation_threshold: int,
) -> dict[str, Any]:
    previous_paths = previous_state.get("paths") if isinstance(previous_state.get("paths"), dict) else {}
    paths: dict[str, Any] = {}
    for path_key, signature in sorted(signatures.items()):
        previous_raw = previous_paths.get(path_key) if isinstance(previous_paths, dict) else {}
        previous = previous_raw if isinstance(previous_raw, dict) else {}
        previous_signature = str(previous.get("signature") or "")
        unchanged = previous_signature == signature
        stagnation_runs = int(previous.get("stagnation_runs") or 0) + 1 if unchanged else 0
        rotation = PATH_FOCUS_ROTATION.get(path_key, ["review"])
        rotation_index = (stagnation_runs // max(1, stagnation_threshold)) % len(rotation)
        paths[path_key] = {
            "signature": signature,
            "changed": not unchanged,
            "stagnation_runs": stagnation_runs,
            "stagnation_threshold": stagnation_threshold,
            "recommended_focus": rotation[rotation_index],
            "rotation_status": "rotate" if stagnation_runs >= stagnation_threshold else "continue",
            "last_changed_at": (
                previous.get("last_changed_at")
                if unchanged and previous.get("last_changed_at")
                else datetime.now().astimezone().isoformat(timespec="seconds")
            ),
        }
    return {
        "updated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "as_of": as_of,
        "paths": paths,
        "quotas": quotas,
    }


def _metric_payload(metrics: dict[str, Any]) -> dict[str, float]:
    payload: dict[str, float] = {}
    for key, value in metrics.items():
        if isinstance(value, (int, float)) and pd.notna(value):
            payload[str(key)] = float(value)
    return payload


def _build_experiment_entries(
    *,
    as_of: str,
    winner_pass: dict[str, Any],
    path2_pass: dict[str, Any],
    weighted: dict[str, Any],
    hk_tracked: dict[str, Any],
) -> list[dict[str, Any]]:
    recorded_at = datetime.now().astimezone().isoformat(timespec="seconds")
    entries: list[dict[str, Any]] = []

    def add_entry(
        *,
        market: str,
        path: str,
        source: str,
        candidate_id: str,
        sample_tag: str,
        outcome: str,
        reason: str,
        metrics: dict[str, Any] | None = None,
        family: str = "",
        rank: int | None = None,
    ) -> None:
        if not candidate_id:
            return
        key = _stable_key([as_of, market, path, source, family, sample_tag, candidate_id, outcome])
        entry = {
            "entry_key": key,
            "recorded_at": recorded_at,
            "as_of": as_of,
            "market": market,
            "path": path,
            "source": source,
            "family": family,
            "candidate_id": candidate_id,
            "sample_tag": sample_tag,
            "rank": rank,
            "outcome": outcome,
            "reason": reason,
            "metrics": _metric_payload(metrics or {}),
        }
        entries.append(entry)

    for track_key, meta in (winner_pass.get("improvements") or {}).items():
        current_id = ((meta.get("current") or {}).get("strategy_base_id") or "")
        clear_id = ((meta.get("best_clear") or {}).get("strategy_base_id") or "")
        for rank, item in enumerate(meta.get("top5") or [], start=1):
            candidate_id = str(item.get("strategy_base_id") or "")
            if candidate_id == current_id:
                outcome = "current_winner"
                reason = "already_current_path1_winner"
            elif clear_id and candidate_id == clear_id:
                outcome = "fast_pass_clear_candidate"
                reason = "passes_fast_pass_threshold_pending_weighted_validation"
            else:
                outcome = "candidate_not_promoted"
                reason = str(meta.get("status") or "not_top_clear_candidate")
            add_entry(
                market="ashare",
                path="path1",
                source="winner_only_pass_top5",
                candidate_id=candidate_id,
                sample_tag=track_key,
                outcome=outcome,
                reason=reason,
                metrics=item.get("metrics") or {},
                rank=rank,
            )

    for sample_tag, item in (path2_pass.get("window_winners") or {}).items():
        add_entry(
            market="ashare",
            path="path2",
            source="path2_window_winner",
            candidate_id=str(item.get("strategy_base_id") or ""),
            sample_tag=str(sample_tag),
            outcome="window_winner",
            reason="path2_candidate_pass_window_leader",
            metrics=item.get("metrics") or {},
        )

    robust = path2_pass.get("robust_candidate") or {}
    add_entry(
        market="ashare",
        path="path2",
        source="path2_robust_candidate",
        candidate_id=str(robust.get("strategy_base_id") or ""),
        sample_tag="four_window",
        outcome="robust_candidate",
        reason="path2_candidate_pass_robust_leader",
        metrics=robust.get("metrics") or robust,
    )

    for family, items in (path2_pass.get("family_ranked_candidates") or {}).items():
        for rank, item in enumerate((items or [])[:5], start=1):
            candidate_id = str(item.get("strategy_base_id") or "")
            outcome = "family_ranked_candidate" if rank == 1 else "family_candidate_not_promoted"
            add_entry(
                market="ashare",
                path="path2",
                source="path2_family_ranked",
                family=str(family),
                candidate_id=candidate_id,
                sample_tag="family_score",
                rank=rank,
                outcome=outcome,
                reason="family_ranked_observation",
                metrics=item,
            )

    weighted_sources = {
        "path1": weighted.get("tracks") or {},
        "path2": (weighted.get("path2") or {}).get("tracks") or {},
        "path3": (weighted.get("path3") or {}).get("tracks") or {},
    }
    for path_name, tracks in weighted_sources.items():
        for track_key, meta in tracks.items():
            if not isinstance(meta, dict):
                continue
            winner_id = str(meta.get("winner") or "")
            add_entry(
                market="ashare",
                path=path_name,
                source="weighted_track_winner",
                candidate_id=winner_id,
                sample_tag=str(track_key),
                outcome="validated_winner",
                reason="weighted_winner_output",
                metrics=meta.get("metrics") or {},
            )
            raw_id = str(meta.get("raw_winner") or "")
            if raw_id and raw_id != winner_id:
                add_entry(
                    market="ashare",
                    path=path_name,
                    source="weighted_raw_displaced",
                    candidate_id=raw_id,
                    sample_tag=str(track_key),
                    outcome="rejected_by_adjacent_validation",
                    reason="raw_winner_displaced_by_validation_guard",
                    metrics=meta.get("raw_metrics") or {},
                )

    for path_name, tracks in (hk_tracked.get("tracks") or {}).items():
        for track_key, meta in (tracks or {}).items():
            if not isinstance(meta, dict):
                continue
            if track_key == "robust_candidate":
                candidate_id = str(meta.get("strategy_id") or "")
                outcome = "robust_candidate"
            else:
                candidate_id = str(meta.get("winner") or "")
                outcome = "validated_winner"
            add_entry(
                market="hkconnect",
                path=str(path_name),
                source="hkconnect_tracked_winner",
                candidate_id=candidate_id,
                sample_tag=str(track_key),
                outcome=outcome,
                reason="hkconnect_tracked_output",
                metrics=meta.get("metrics") or {},
            )

    return entries


def _append_experiment_log(path: Path, entries: list[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing_keys: set[str] = set()
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                existing = json.loads(line)
            except json.JSONDecodeError:
                continue
            key = str(existing.get("entry_key") or "")
            if key:
                existing_keys.add(key)
    new_entries = [entry for entry in entries if str(entry.get("entry_key") or "") not in existing_keys]
    if not new_entries:
        return 0
    with path.open("a", encoding="utf-8") as handle:
        for entry in new_entries:
            handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
    return len(new_entries)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build iteration coverage gate, experiment log, and path rotation state."
    )
    parser.add_argument("--comparison-csv", type=Path, default=DEFAULT_COMPARISON_CSV)
    parser.add_argument("--path2-pass-json", type=Path, default=DEFAULT_PATH2_PASS_JSON)
    parser.add_argument("--winner-pass-json", type=Path, default=DEFAULT_WINNER_PASS_JSON)
    parser.add_argument("--weighted-winners-json", type=Path, default=DEFAULT_WEIGHTED_WINNERS_JSON)
    parser.add_argument("--hk-comparison-csv", type=Path, default=DEFAULT_HK_COMPARISON_CSV)
    parser.add_argument("--hk-tracked-json", type=Path, default=DEFAULT_HK_TRACKED_JSON)
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT_JSON)
    parser.add_argument("--state-json", type=Path, default=DEFAULT_STATE_JSON)
    parser.add_argument("--experiment-log", type=Path, default=DEFAULT_EXPERIMENT_LOG)
    parser.add_argument("--stagnation-threshold", type=int, default=3)
    parser.add_argument("--fail-on-blocking-missing", action="store_true")
    args = parser.parse_args(argv)

    constants = _load_backtest_constants()
    direction_groups, path1_fast_ids = _extract_path1_candidates(constants)
    core_multifactor_ids = direction_groups.get("core_multifactor", [])
    path4_theme_ids = _extract_path4_theme_candidates(constants)

    ashare_latest = _read_latest_csv(args.comparison_csv, "strategy_base_id")
    hk_latest = _read_latest_csv(args.hk_comparison_csv, "strategy_id")
    ashare_windows = _window_map(ashare_latest, "strategy_base_id")
    hk_windows = _window_map(hk_latest, "strategy_id")

    path2_pass = _load_json(args.path2_pass_json, {})
    winner_pass = _load_json(args.winner_pass_json, {})
    weighted = _load_json(args.weighted_winners_json, {})
    hk_tracked = _load_json(args.hk_tracked_json, {})
    previous_state = _load_json(args.state_json, {})

    path2_ids = sorted((path2_pass.get("candidate_family_membership") or {}).keys())
    path3_ids = sorted(
        strategy_id
        for strategy_id in ashare_windows
        if str(strategy_id).endswith("_weekly")
    )
    hk_ids = sorted(hk_windows)

    coverage_scopes = [
        _coverage_scope(
            scope_id="ashare_path1_core_multifactor",
            market="ashare",
            path="path1",
            candidates=core_multifactor_ids,
            required_windows=A_SHARE_OBSERVATION_WINDOWS,
            windows_by_id=ashare_windows,
            blocking=True,
            description="Path 4-lite multi-factor candidates must be fully observed before judging them.",
        ),
        _coverage_scope(
            scope_id="ashare_path1_fast_family",
            market="ashare",
            path="path1",
            candidates=path1_fast_ids,
            required_windows=A_SHARE_REQUIRED_WINDOWS,
            windows_by_id=ashare_windows,
            blocking=False,
            description="Path 1 fast-pass family coverage; warnings keep the search surface honest.",
        ),
        _coverage_scope(
            scope_id="ashare_path2_candidate_universe",
            market="ashare",
            path="path2",
            candidates=path2_ids,
            required_windows=A_SHARE_REQUIRED_WINDOWS,
            windows_by_id=ashare_windows,
            blocking=True,
            description="Path 2 candidate pass universe must have comparable four-window results.",
        ),
        _coverage_scope(
            scope_id="ashare_path3_weekly_universe",
            market="ashare",
            path="path3",
            candidates=path3_ids,
            required_windows=A_SHARE_REQUIRED_WINDOWS,
            windows_by_id=ashare_windows,
            blocking=True,
            description="Path 3 pure weekly candidates must have comparable four-window results.",
        ),
        _coverage_scope(
            scope_id="ashare_path4_emergent_theme",
            market="ashare",
            path="path4",
            candidates=path4_theme_ids,
            required_windows=A_SHARE_OBSERVATION_WINDOWS,
            windows_by_id=ashare_windows,
            blocking=True,
            description="Path 4 emergent-theme candidates use no manual theme labels and must be observed before judging theme-capture quality.",
        ),
        _coverage_scope(
            scope_id="hkconnect_all_candidates",
            market="hkconnect",
            path="all",
            candidates=hk_ids,
            required_windows=HK_REQUIRED_WINDOWS,
            windows_by_id=hk_windows,
            blocking=True,
            description="HK-connect candidates are expected to be evaluated on all five windows.",
        ),
    ]
    blocking_missing = sum(scope["missing_count"] for scope in coverage_scopes if scope["blocking"])
    warning_missing = sum(scope["missing_count"] for scope in coverage_scopes if not scope["blocking"])

    signatures = _strategy_signature(weighted, hk_tracked)
    quotas = {
        "path1": {
            "minimum_direction_counts": PATH1_MIN_DIRECTION_COUNTS,
            "current_direction_counts": winner_pass.get("direction_candidate_counts") or {},
        },
        "path2": {
            "family_counts": _extract_path2_family_counts(path2_pass, constants),
            "next_run_new_candidate_quota": {
                "emergent_theme_discovery": 3,
                "high_concentration_breakout": 2,
                "high_growth_theme": 2,
                "momentum_equal_weight_elastic": 2,
                "biweekly_rebalance_aggressive": 2,
                "weekly_rebalance_aggressive": 2,
            },
        },
        "path3": {
            "current_weekly_candidate_count": len(path3_ids),
            "next_run_new_candidate_quota": {
                "turnover_reduction": 4,
                "weekly_exit_buffer": 3,
                "risk_downshift": 3,
                "cost_stress": 2,
            },
        },
        "path4": {
            "emergent_theme_candidate_count": len(path4_theme_ids),
            "next_run_new_candidate_quota": {
                "emergent_theme_coverage": 4,
                "theme_signal_quality": 3,
                "theme_risk_control": 3,
                "theme_capacity_cost": 2,
            },
        },
        "hkconnect": {
            "candidate_count": len(hk_ids),
            "next_run_new_candidate_quota": {
                "path1": 2,
                "path2": 3,
                "path3": 3,
            },
        },
    }
    as_of = str(weighted.get("as_of") or winner_pass.get("as_of") or "")
    state = _update_state(
        previous_state=previous_state,
        signatures=signatures,
        quotas=quotas,
        as_of=as_of,
        stagnation_threshold=max(1, int(args.stagnation_threshold)),
    )

    experiment_entries = _build_experiment_entries(
        as_of=as_of,
        winner_pass=winner_pass,
        path2_pass=path2_pass,
        weighted=weighted,
        hk_tracked=hk_tracked,
    )
    appended = _append_experiment_log(args.experiment_log, experiment_entries)

    report = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "as_of": as_of,
        "coverage_gate": {
            "status": "block" if blocking_missing else ("warn" if warning_missing else "pass"),
            "blocking_missing_count": blocking_missing,
            "warning_missing_count": warning_missing,
            "scopes": coverage_scopes,
        },
        "experiment_log": {
            "path": str(args.experiment_log.relative_to(ROOT)),
            "candidate_entries": len(experiment_entries),
            "appended_entries": appended,
        },
        "rotation": state["paths"],
        "quotas": quotas,
    }
    _write_json(args.write_report, report)
    _write_json(args.state_json, state)

    print(f"[OK] Wrote {args.write_report}")
    print(f"[OK] Wrote {args.state_json}")
    print(f"[OK] Appended {appended} entries to {args.experiment_log}")
    print(
        f"[Gate] status={report['coverage_gate']['status']} "
        f"blocking_missing={blocking_missing} warning_missing={warning_missing}"
    )
    for scope in coverage_scopes:
        if scope["missing_count"]:
            print(
                f"[Gate] {scope['scope_id']}: {scope['missing_count']}/"
                f"{scope['candidate_count']} missing ({scope['status']})"
            )
            for command in scope["rerun_commands"][:3]:
                print(f"       rerun: {command}")
            if len(scope["rerun_commands"]) > 3:
                print(f"       ... {len(scope['rerun_commands']) - 3} more command(s)")
    for path_key, meta in state["paths"].items():
        print(
            f"[Rotate] {path_key}: {meta['rotation_status']} "
            f"stagnation_runs={meta['stagnation_runs']} focus={meta['recommended_focus']}"
        )

    if args.fail_on_blocking_missing and blocking_missing:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
