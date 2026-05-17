from __future__ import annotations

import argparse
import ast
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.results_layout import (
    candidate_strategy_result_dirs,
    existing_research_file,
    research_file,
)

DEFAULT_COMPARISON_CSV = existing_research_file("strategy_comparison_base_method.csv")
README_PATH = ROOT / "README.md"
BACKTEST_SCRIPT_PATH = ROOT / "backtest_marketcap_etf.py"
TRACKED_HISTORY_JSON_PATH = research_file("tracked_winner_history.json")
TRACKED_HISTORY_MD_PATH = ROOT / "HISTORY.md"
CORE_ACTIVE_REGISTRY_JSON_PATH = research_file("core_active_registry.json")
TRADE_CALENDAR_PATH = ROOT / "data_cache" / "trade_calendar.csv"
CORE_ACTIVE_MAX_SIZE = 128
CORE_ACTIVE_STALE_TRADING_DAYS = 30
TRACK_LEADERBOARD_LIMIT = 5

AUTO_START = "<!-- AUTO:WEIGHTED-WINNERS:START -->"
AUTO_END = "<!-- AUTO:WEIGHTED-WINNERS:END -->"

WEIGHTED_WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01")
SAMPLE_TAG_STARTS = {
    "since_2017_01": pd.Timestamp("2017-01-01"),
    "since_2020_01": pd.Timestamp("2020-01-01"),
    "since_2023_01": pd.Timestamp("2023-01-01"),
    "since_2025_01": pd.Timestamp("2025-01-01"),
    "since_2026_01": pd.Timestamp("2026-01-01"),
}
STATIC_BASE_IDS = {"large_cap_pool", "kechuang_xuangu"}

WEIGHTS_2017_ONLY = {"since_2017_01": 1.00}
WEIGHTS_2023_ONLY = {"since_2023_01": 1.00}
WEIGHTS_2020_ONLY = {"since_2020_01": 1.00}
WEIGHTS_2025_ONLY = {"since_2025_01": 1.00}
TRACK_SEQUENCE = [
    ("since_2017_only", "since_2017_01", "2017 窗口"),
    ("since_2020_only", "since_2020_01", "2020 窗口"),
    ("since_2023_only", "since_2023_01", "2023 窗口"),
    ("since_2025_only", "since_2025_01", "2025 窗口"),
]
ROBUST_TRACK_KEY = "robust_candidate"

# Phase 1: Adjacent-window validation
#
# When picking a window winner, validate the candidate's CAGR in an "adjacent" window
# against the incumbent winner of that adjacent window. This filters out candidates
# that look great in the target window but collapse in the validation window
# (typical sign of overfitting to a specific regime).
#
# The validation_window for each target_window is chosen to be the "next more recent"
# window, except for since_2025_01 which goes back to since_2023_01 (since 2026 is
# observation-only and not used for validation).
ADJACENT_VALIDATION_WINDOW = {
    "since_2017_01": "since_2020_01",
    "since_2020_01": "since_2023_01",
    "since_2023_01": "since_2025_01",
    "since_2025_01": "since_2023_01",
}

# Threshold is keyed by the VALIDATION window (i.e., the window we check against).
# Shorter validation windows have higher CAGR variance, so we use looser thresholds
# to avoid rejecting healthy candidates that simply did not bet on the same theme as
# a short-window outlier.
ADJACENT_VALIDATION_THRESHOLDS = {
    "since_2017_01": 0.75,
    "since_2020_01": 0.75,
    "since_2023_01": 0.70,
    "since_2025_01": 0.60,
}

# Absolute floor: required CAGR = max(threshold * effective_incumbent_cagr, ABSOLUTE_FLOOR).
# Keeps the rule sensible when incumbent CAGR is near zero or negative — a candidate
# must at least break even in the validation window, regardless of how the percentage
# threshold scales.
ADJACENT_VALIDATION_ABSOLUTE_FLOOR = 0.0

# Cap on the incumbent CAGR used for the threshold computation, keyed by validation
# window. Without this cap, an outlier incumbent (e.g., a 2025 winner with 181% CAGR)
# would inflate the required CAGR to an unrealistic level (60% × 181% = 108%), creating
# a bistable system: the only candidate that meets the bar is the same overfit
# strategy, which produces a self-perpetuating state. Capping the effective incumbent
# CAGR at a reasonable level for the window's typical universe disarms outliers and
# allows the validation to converge on healthy candidates.
#
# Caps reflect "what counts as a healthy upper-end CAGR" for that window:
#   2017 (long, 9 years): 30% — sustained 30%+ over 9 years is exceptional
#   2020 (medium, 6 years): 35%
#   2023 (medium-short, 3 years): 50%
#   2025 (short, 1.4 years): 70% — short windows can legitimately show high CAGR,
#       but >70% is typically outlier territory
ADJACENT_VALIDATION_INCUMBENT_CAP = {
    "since_2017_01": 0.30,
    "since_2020_01": 0.35,
    "since_2023_01": 0.50,
    "since_2025_01": 0.70,
}

WINDOW_TAG_TO_TRACK_KEY = {
    "since_2017_01": "since_2017_only",
    "since_2020_01": "since_2020_only",
    "since_2023_01": "since_2023_only",
    "since_2025_01": "since_2025_only",
}
TRACK_KEY_TO_WINDOW_TAG = {track_key: sample_tag for sample_tag, track_key in WINDOW_TAG_TO_TRACK_KEY.items()}


@dataclass(frozen=True)
class TrackMetrics:
    cagr: float
    sharpe: float
    max_drawdown: float
    turnover: float


@dataclass(frozen=True)
class ImprovementThresholds:
    min_cagr_improvement: float
    min_sharpe_improvement: float
    max_drawdown_worsen_abs: float
    max_turnover_increase: float


PATH1_IMPROVEMENT_THRESHOLDS = ImprovementThresholds(
    min_cagr_improvement=0.0010,
    min_sharpe_improvement=0.0050,
    max_drawdown_worsen_abs=0.0050,
    max_turnover_increase=0.15,
)


def _metrics_to_dict(metrics: TrackMetrics) -> dict[str, float]:
    """Render a TrackMetrics tuple as the standard payload dict."""
    return {
        "weighted_cagr": metrics.cagr,
        "weighted_sharpe": metrics.sharpe,
        "weighted_max_drawdown": metrics.max_drawdown,
        "weighted_turnover": metrics.turnover,
    }


def _metrics_from_track_payload(payload: dict[str, Any]) -> TrackMetrics:
    return TrackMetrics(
        cagr=float(payload.get("weighted_cagr", float("nan"))),
        sharpe=float(payload.get("weighted_sharpe", float("nan"))),
        max_drawdown=float(payload.get("weighted_max_drawdown", float("nan"))),
        turnover=float(payload.get("weighted_turnover", float("nan"))),
    )


def _load_tracked_payload(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def _build_track_section(
    *,
    weights: dict[str, float],
    validated_winner_id: str,
    validated_metrics: TrackMetrics,
    raw_winner_id: str | None = None,
    raw_metrics: TrackMetrics | None = None,
    leaderboard: list[dict[str, Any]] | None = None,
) -> dict[str, object]:
    """Build a single track entry for the payload.

    The validated winner is the post-validation pick that is the official
    output for active family / live trading. The raw winner is the
    unvalidated top-rank pick kept for diagnostics: when validation displaces
    a candidate (typically because it is overfit to the target window),
    raw_winner records what would have been chosen without the guard.
    """
    section: dict[str, object] = {
        "weights": weights,
        "winner": validated_winner_id,
        "metrics": _metrics_to_dict(validated_metrics),
    }
    if leaderboard:
        section["leaderboard"] = leaderboard
    if raw_winner_id is None or raw_metrics is None:
        return section
    section["raw_winner"] = raw_winner_id
    section["raw_metrics"] = _metrics_to_dict(raw_metrics)
    section["raw_displaced"] = raw_winner_id != validated_winner_id
    return section


def _is_nan_metrics(metrics: TrackMetrics) -> bool:
    return any(np.isnan(v) for v in (metrics.cagr, metrics.sharpe, metrics.max_drawdown, metrics.turnover))


def _is_clear_improvement(*, candidate: TrackMetrics, current: TrackMetrics, thresholds: ImprovementThresholds) -> bool:
    if _is_nan_metrics(candidate) or _is_nan_metrics(current):
        return False
    if (candidate.cagr - current.cagr) < thresholds.min_cagr_improvement:
        return False
    if (candidate.sharpe - current.sharpe) < thresholds.min_sharpe_improvement:
        return False
    # Max drawdown is negative. Less-negative is better. Allow a small worsening.
    drawdown_worsen = current.max_drawdown - candidate.max_drawdown
    if drawdown_worsen > thresholds.max_drawdown_worsen_abs:
        return False
    if (candidate.turnover - current.turnover) > thresholds.max_turnover_increase:
        return False
    return True


def _eval_python_constant(node: ast.AST, env: dict[str, Any]) -> Any:
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.List):
        return [_eval_python_constant(item, env) for item in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(_eval_python_constant(item, env) for item in node.elts)
    if isinstance(node, ast.Set):
        return {_eval_python_constant(item, env) for item in node.elts}
    if isinstance(node, ast.Dict):
        return {
            _eval_python_constant(key, env): _eval_python_constant(value, env)
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _eval_python_constant(node.operand, env)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.Name):
        return env[node.id]
    if isinstance(node, ast.Subscript):
        value = _eval_python_constant(node.value, env)
        key = _eval_python_constant(node.slice, env)
        return value[key]
    raise ValueError(f"Unsupported constant expression: {ast.dump(node)}")


def _parse_python_constants(path: Path, names: Iterable[str]) -> dict[str, Any]:
    wanted = set(names)
    result: dict[str, Any] = {}
    env: dict[str, Any] = {}
    node = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for stmt in node.body:
        if not isinstance(stmt, ast.Assign):
            continue
        if len(stmt.targets) != 1 or not isinstance(stmt.targets[0], ast.Name):
            continue
        target = stmt.targets[0].id
        try:
            value = _eval_python_constant(stmt.value, env)
        except Exception:
            continue
        env[target] = value
        if target not in wanted:
            continue
        result[target] = value
        if len(result) == len(wanted):
            break
    missing = wanted - set(result)
    if missing:
        raise RuntimeError(f"Unable to extract constants from {path}: {sorted(missing)}")
    return result


def load_winner_core_prefix(backtest_path: Path = BACKTEST_SCRIPT_PATH) -> str:
    try:
        consts = _parse_python_constants(backtest_path, ["WINNER_ONLY_STRATEGY_ID"])
    except Exception:
        return "core_explore_80_20_total_mv_winner_core"
    prefix = str(consts.get("WINNER_ONLY_STRATEGY_ID") or "").strip()
    return prefix or "core_explore_80_20_total_mv_winner_core"


def load_winner_core_family_ids(backtest_path: Path = BACKTEST_SCRIPT_PATH) -> set[str]:
    try:
        consts = _parse_python_constants(backtest_path, ["WINNER_ONLY_STRATEGY_ID", "WINNER_CORE_VARIANTS"])
    except Exception:
        prefix = load_winner_core_prefix(backtest_path)
        return {prefix}
    base = str(consts.get("WINNER_ONLY_STRATEGY_ID") or "").strip() or load_winner_core_prefix(backtest_path)
    variants = consts.get("WINNER_CORE_VARIANTS")
    if not isinstance(variants, list):
        return {base}
    ids = {base}
    for variant in variants:
        if not isinstance(variant, dict):
            continue
        variant_id = variant.get("variant_id")
        if not variant_id:
            continue
        ids.add(f"{base}__{variant_id}")
    return set(map(str, ids))


def load_path1_family_ids(backtest_path: Path = BACKTEST_SCRIPT_PATH) -> set[str]:
    try:
        consts = _parse_python_constants(
            backtest_path,
            [
                "WINNER_ONLY_STRATEGY_ID",
                "WINNER_CORE_VARIANTS",
                "PATH1_FAST_PASS_VARIANT_IDS",
                "SAT_WEEKLY_RISK_SUFFIX",
                "SAT_THREE_STAGE_SUFFIX",
                "SAT_THREE_STAGE_BUFFERED_SUFFIX",
                "SAT_THREE_STAGE_BUFFERED_ASYM13_SUFFIX",
                "PORT_WEEKLY_EXPOSURE_SUFFIX",
                "PORT_WEEKLY_EXPOSURE_BUFFERED_SUFFIX",
                "PORT_WEEKLY_EXPOSURE_BUFFERED_ASYM13_SUFFIX",
                "PORT_WEEKLY_EXPOSURE_ASYM_SUFFIX",
            ],
        )
        winner_base = str(consts.get("WINNER_ONLY_STRATEGY_ID") or "").strip() or load_winner_core_prefix(backtest_path)
        variants = consts.get("WINNER_CORE_VARIANTS") or []
        fast_pass_variant_ids = {str(item) for item in consts.get("PATH1_FAST_PASS_VARIANT_IDS") or []}
        winner_ids = {winner_base}
        if isinstance(variants, list):
            for variant in variants:
                if not isinstance(variant, dict):
                    continue
                variant_id = str(variant.get("variant_id") or "").strip()
                if not variant_id:
                    continue
                if fast_pass_variant_ids and variant_id not in fast_pass_variant_ids:
                    continue
                winner_ids.add(f"{winner_base}__{variant_id}")
        overlay_suffixes = [
            str(consts.get("SAT_WEEKLY_RISK_SUFFIX") or "__sat_weekly_risk"),
            str(consts.get("SAT_THREE_STAGE_SUFFIX") or "__sat_three_stage_risk"),
            str(consts.get("SAT_THREE_STAGE_BUFFERED_SUFFIX") or "__sat_three_stage_buffered"),
            str(consts.get("SAT_THREE_STAGE_BUFFERED_ASYM13_SUFFIX") or "__sat_three_stage_buffered_asym13"),
            str(consts.get("PORT_WEEKLY_EXPOSURE_SUFFIX") or "__port_weekly_exposure"),
            str(consts.get("PORT_WEEKLY_EXPOSURE_BUFFERED_SUFFIX") or "__port_weekly_exposure_buffered"),
            str(consts.get("PORT_WEEKLY_EXPOSURE_BUFFERED_ASYM13_SUFFIX") or "__port_weekly_exposure_buffered_asym13"),
            str(consts.get("PORT_WEEKLY_EXPOSURE_ASYM_SUFFIX") or "__port_weekly_exposure_asym"),
        ]
    except Exception:
        winner_ids = load_winner_core_family_ids(backtest_path)
        overlay_suffixes = [
            "__sat_weekly_risk",
            "__sat_three_stage_risk",
            "__sat_three_stage_buffered",
            "__sat_three_stage_buffered_asym13",
            "__port_weekly_exposure",
            "__port_weekly_exposure_buffered",
            "__port_weekly_exposure_buffered_asym13",
            "__port_weekly_exposure_asym",
        ]
    path1_ids = set(winner_ids)
    path1_ids |= {f"{base_id}{suffix}" for base_id in winner_ids for suffix in overlay_suffixes}
    return path1_ids


def load_active_family_ids(backtest_path: Path = BACKTEST_SCRIPT_PATH) -> set[str]:
    try:
        consts = _parse_python_constants(
            backtest_path,
            [
                "ACTIVE_FAMILY_BASE_PREFIXES",
                "WINNER_ONLY_STRATEGY_ID",
                "WINNER_CORE_VARIANTS",
                "SAT_WEEKLY_RISK_SUFFIX",
                "SAT_THREE_STAGE_SUFFIX",
                "SAT_THREE_STAGE_BUFFERED_SUFFIX",
                "SAT_THREE_STAGE_BUFFERED_ASYM13_SUFFIX",
                "PORT_WEEKLY_EXPOSURE_SUFFIX",
                "PORT_WEEKLY_EXPOSURE_BUFFERED_SUFFIX",
                "PORT_WEEKLY_EXPOSURE_BUFFERED_ASYM13_SUFFIX",
                "PORT_WEEKLY_EXPOSURE_ASYM_SUFFIX",
            ],
        )
    except Exception:
        return {
            "core_explore_80_20_total_mv_index_core",
            "core_explore_80_20_total_mv_winner_core",
        }

    prefixes = [str(item) for item in consts.get("ACTIVE_FAMILY_BASE_PREFIXES", [])]
    winner_base = str(consts.get("WINNER_ONLY_STRATEGY_ID") or "").strip()
    variants = consts.get("WINNER_CORE_VARIANTS", [])
    overlay_suffixes = [
        str(consts.get("SAT_WEEKLY_RISK_SUFFIX") or "__sat_weekly_risk"),
        str(consts.get("SAT_THREE_STAGE_SUFFIX") or "__sat_three_stage_risk"),
        str(consts.get("SAT_THREE_STAGE_BUFFERED_SUFFIX") or "__sat_three_stage_buffered"),
        str(consts.get("SAT_THREE_STAGE_BUFFERED_ASYM13_SUFFIX") or "__sat_three_stage_buffered_asym13"),
        str(consts.get("PORT_WEEKLY_EXPOSURE_SUFFIX") or "__port_weekly_exposure"),
        str(consts.get("PORT_WEEKLY_EXPOSURE_BUFFERED_SUFFIX") or "__port_weekly_exposure_buffered"),
        str(consts.get("PORT_WEEKLY_EXPOSURE_BUFFERED_ASYM13_SUFFIX") or "__port_weekly_exposure_buffered_asym13"),
        str(consts.get("PORT_WEEKLY_EXPOSURE_ASYM_SUFFIX") or "__port_weekly_exposure_asym"),
    ]

    active_ids: set[str] = set()
    for prefix in prefixes:
        active_ids.add(prefix)
    if winner_base and any(winner_base == prefix or winner_base.startswith(prefix) for prefix in prefixes):
        active_ids.add(winner_base)
    if isinstance(variants, list) and winner_base:
        for variant in variants:
            if not isinstance(variant, dict) or not variant.get("variant_id"):
                continue
            base_id = f"{winner_base}__{variant['variant_id']}"
            if not any(base_id == prefix or base_id.startswith(f"{prefix}__") for prefix in prefixes):
                continue
            active_ids.add(base_id)
            for suffix in overlay_suffixes:
                active_ids.add(f"{base_id}{suffix}")
    return active_ids


def load_path2_scan_rules(backtest_path: Path = BACKTEST_SCRIPT_PATH) -> tuple[list[str], list[str]]:
    try:
        consts = _parse_python_constants(backtest_path, ["PATH2_SCAN_BASE_PREFIXES", "PATH2_SCAN_VARIANT_IDS"])
    except Exception:
        return ([], [])
    prefixes = [str(item) for item in consts.get("PATH2_SCAN_BASE_PREFIXES") or []]
    variant_ids = [str(item) for item in consts.get("PATH2_SCAN_VARIANT_IDS") or []]
    return prefixes, variant_ids


def _matches_path2(base_id: str, prefixes: list[str], variant_ids: list[str]) -> bool:
    if any(base_id.startswith(prefix) for prefix in prefixes):
        return True
    return any(base_id.endswith(f"__{variant_id}") for variant_id in variant_ids)


def _matches_path3(base_id: str) -> bool:
    return str(base_id).endswith("_weekly")


def _load_existing_path1_winners(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    if not isinstance(payload, dict):
        return {}
    tracks = payload.get("tracks")
    if not isinstance(tracks, dict):
        return {}
    winners: dict[str, str] = {}
    for track_key, meta in tracks.items():
        if not isinstance(meta, dict):
            continue
        winner = meta.get("winner")
        if winner:
            winners[str(track_key)] = str(winner)
    return winners


def _load_existing_winners_all_paths(path: Path) -> dict[str, dict[str, str]]:
    """Load existing path1/path2/path3 winners as anchors for adjacent-window validation.

    Returns a dict keyed by path name ("path1"/"path2"/"path3"), each mapping
    track_key -> winner_base_id. Empty mappings are returned when the file
    does not exist or cannot be parsed.
    """
    result: dict[str, dict[str, str]] = {"path1": {}, "path2": {}, "path3": {}}
    if not path.exists():
        return result
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return result
    if not isinstance(payload, dict):
        return result

    tracks = payload.get("tracks")
    if isinstance(tracks, dict):
        for track_key, meta in tracks.items():
            if isinstance(meta, dict) and meta.get("winner"):
                result["path1"][str(track_key)] = str(meta["winner"])

    for path_key in ("path2", "path3"):
        sub = payload.get(path_key)
        if not isinstance(sub, dict):
            continue
        sub_tracks = sub.get("tracks")
        if not isinstance(sub_tracks, dict):
            continue
        for track_key, meta in sub_tracks.items():
            if isinstance(meta, dict) and meta.get("winner"):
                result[path_key][str(track_key)] = str(meta["winner"])
    return result


def _latest_per_strategy_window(frame: pd.DataFrame) -> pd.DataFrame:
    required_cols = {"strategy_base_id", "strategy_base_name", "sample_tag", "sample_end"}
    missing = required_cols - set(frame.columns)
    if missing:
        raise ValueError(f"comparison csv missing columns: {sorted(missing)}")

    typed = frame.copy()
    typed["sample_end"] = pd.to_datetime(typed["sample_end"], errors="coerce")
    typed = typed.dropna(subset=["sample_end"])
    typed = typed.sort_values(["strategy_base_id", "sample_tag", "sample_end"])
    return typed.groupby(["strategy_base_id", "sample_tag"], as_index=False).tail(1)


def _filter_to_current_as_of(latest: pd.DataFrame) -> pd.DataFrame:
    typed = latest.copy()
    typed["sample_end"] = pd.to_datetime(typed["sample_end"], errors="coerce")
    typed = typed.dropna(subset=["sample_end"])
    if typed.empty:
        return latest
    current_as_of = typed["sample_end"].max()
    fresh = typed[typed["sample_end"] == current_as_of].copy()
    return fresh if not fresh.empty else typed


def _filter_ids_to_current_as_of(latest: pd.DataFrame, allowed_base_ids: set[str]) -> pd.DataFrame:
    subset = latest[latest["strategy_base_id"].astype(str).isin(allowed_base_ids)].copy()
    return _filter_to_current_as_of(subset)


def _weighted_metric(group: pd.DataFrame, weights: dict[str, float], column: str) -> float:
    total = 0.0
    for sample_tag, weight in weights.items():
        value_series = group.loc[group["sample_tag"] == sample_tag, column]
        if value_series.empty:
            return float("nan")
        total += weight * float(value_series.iloc[0])
    return float(total)


def _build_strategy_map(latest: pd.DataFrame) -> dict[str, dict]:
    strategies: dict[str, dict] = {}
    for base_id, group in latest.groupby("strategy_base_id"):
        strategies[str(base_id)] = {
            "strategy_base_id": str(base_id),
            "strategy_base_name": str(group["strategy_base_name"].iloc[0]),
            "sample_end": str(group["sample_end"].max().date()),
            "windows": {
                tag: {
                    "cagr": float(group.loc[group["sample_tag"] == tag, "cagr"].iloc[0]),
                    "sharpe": float(group.loc[group["sample_tag"] == tag, "sharpe_ratio"].iloc[0]),
                    "max_drawdown": float(group.loc[group["sample_tag"] == tag, "max_drawdown"].iloc[0]),
                    "turnover": float(group.loc[group["sample_tag"] == tag, "average_annual_turnover"].iloc[0]),
                    "total_return": float(group.loc[group["sample_tag"] == tag, "total_return"].iloc[0]),
                }
                for tag in SAMPLE_TAG_STARTS
                if tag in set(group["sample_tag"].astype(str))
            },
        }
    return strategies


def _compute_track_metrics(group: pd.DataFrame, weights: dict[str, float]) -> TrackMetrics:
    return TrackMetrics(
        cagr=_weighted_metric(group, weights, "cagr"),
        sharpe=_weighted_metric(group, weights, "sharpe_ratio"),
        max_drawdown=_weighted_metric(group, weights, "max_drawdown"),
        turnover=_weighted_metric(group, weights, "average_annual_turnover"),
    )


def _compute_single_window_metrics(group: pd.DataFrame, sample_tag: str) -> TrackMetrics:
    row = group.loc[group["sample_tag"] == sample_tag]
    if row.empty:
        return TrackMetrics(cagr=float("nan"), sharpe=float("nan"), max_drawdown=float("nan"), turnover=float("nan"))
    return TrackMetrics(
        cagr=float(row["cagr"].iloc[0]),
        sharpe=float(row["sharpe_ratio"].iloc[0]),
        max_drawdown=float(row["max_drawdown"].iloc[0]),
        turnover=float(row["average_annual_turnover"].iloc[0]),
    )


def _window_sort_key(item: tuple[str, TrackMetrics]) -> tuple[float, float, float, float]:
    metrics = item[1]
    return (metrics.cagr, metrics.sharpe, metrics.max_drawdown, -metrics.turnover)


def _rank_single_window_candidates(
    latest: pd.DataFrame,
    sample_tag: str,
    *,
    allowed_base_ids: set[str] | None = None,
) -> list[tuple[str, TrackMetrics]]:
    candidates: list[tuple[str, TrackMetrics]] = []
    for base_id, group in latest.groupby("strategy_base_id"):
        if allowed_base_ids is not None and str(base_id) not in allowed_base_ids:
            continue
        tags = set(group["sample_tag"].astype(str))
        if sample_tag != "since_2025_01" and not set(WEIGHTED_WINDOW_TAGS).issubset(tags):
            continue
        if sample_tag not in tags:
            continue
        metrics = _compute_single_window_metrics(group, sample_tag)
        if _is_nan_metrics(metrics):
            continue
        candidates.append((str(base_id), metrics))
    candidates.sort(key=_window_sort_key, reverse=True)
    return candidates


def _pick_winner(
    latest: pd.DataFrame,
    weights: dict[str, float],
    *,
    allowed_base_ids: set[str] | None = None,
) -> tuple[str, TrackMetrics]:
    candidates: list[tuple[str, TrackMetrics]] = []
    for base_id, group in latest.groupby("strategy_base_id"):
        if allowed_base_ids is not None and str(base_id) not in allowed_base_ids:
            continue
        tags = set(group["sample_tag"].astype(str))
        if not set(WEIGHTED_WINDOW_TAGS).issubset(tags):
            continue
        metrics = _compute_track_metrics(group, weights)
        if any(np.isnan(v) for v in (metrics.cagr, metrics.sharpe, metrics.max_drawdown, metrics.turnover)):
            continue
        candidates.append((str(base_id), metrics))
    if not candidates:
        raise RuntimeError("No strategies have all three windows to compute weighted winners.")

    # Multi-objective preference:
    # - primarily maximize weighted CAGR
    # - then maximize weighted Sharpe
    # - then prefer less negative weighted max drawdown
    # - then prefer lower weighted turnover
    candidates.sort(key=_window_sort_key, reverse=True)
    return candidates[0]


def _pick_single_window_winner(
    latest: pd.DataFrame,
    sample_tag: str,
    *,
    allowed_base_ids: set[str] | None = None,
) -> tuple[str, TrackMetrics]:
    candidates = _rank_single_window_candidates(latest, sample_tag, allowed_base_ids=allowed_base_ids)
    if not candidates:
        raise RuntimeError(f"No strategies have {sample_tag} window to compute the single-window winner.")
    return candidates[0]


def _passes_adjacent_window_check(
    *,
    candidate_id: str,
    target_window: str,
    by_id: dict[str, pd.DataFrame],
    incumbent_winners: dict[str, str],
) -> tuple[bool, dict[str, Any]]:
    """Validate a candidate's performance in its adjacent window.

    For the candidate competing for the ``target_window`` slot, find the
    designated validation window, look up the incumbent winner of that
    validation window, and require:

        candidate_cagr >= max(threshold * incumbent_cagr, ABSOLUTE_FLOOR)

    Returns a ``(passes, detail)`` tuple where ``detail`` carries diagnostic
    fields used for logging.

    Degrades gracefully (returns ``passes=True``) when:
        - target_window has no adjacent validation mapping
        - no incumbent winner is recorded for the validation window
        - incumbent metrics are missing in the validation window
    Fails closed (returns ``passes=False``) when the candidate itself has
    no metrics in the validation window — that is suspicious enough that
    we'd rather skip the candidate.
    """
    detail: dict[str, Any] = {
        "candidate_id": candidate_id,
        "target_window": target_window,
    }
    validation_window = ADJACENT_VALIDATION_WINDOW.get(target_window)
    detail["validation_window"] = validation_window
    if not validation_window:
        detail["reason"] = "no_adjacent_window"
        return True, detail

    threshold = ADJACENT_VALIDATION_THRESHOLDS.get(validation_window, 0.70)
    detail["threshold"] = threshold
    detail["absolute_floor"] = ADJACENT_VALIDATION_ABSOLUTE_FLOOR

    incumbent_track_key = WINDOW_TAG_TO_TRACK_KEY.get(validation_window)
    incumbent_id = incumbent_winners.get(incumbent_track_key) if incumbent_track_key else None
    detail["incumbent_id"] = incumbent_id

    if not incumbent_id:
        detail["reason"] = "no_incumbent"
        return True, detail

    candidate_group = by_id.get(candidate_id)
    if candidate_group is None or candidate_group.empty:
        detail["reason"] = "candidate_missing_data"
        return False, detail
    candidate_metrics = _compute_single_window_metrics(candidate_group, validation_window)
    detail["candidate_cagr"] = candidate_metrics.cagr
    if _is_nan_metrics(candidate_metrics) or pd.isna(candidate_metrics.cagr):
        detail["reason"] = "candidate_missing_validation_metrics"
        return False, detail

    incumbent_group = by_id.get(incumbent_id)
    if incumbent_group is None or incumbent_group.empty:
        detail["reason"] = "incumbent_missing_data"
        return True, detail
    incumbent_metrics = _compute_single_window_metrics(incumbent_group, validation_window)
    detail["incumbent_cagr"] = incumbent_metrics.cagr
    if pd.isna(incumbent_metrics.cagr):
        detail["reason"] = "incumbent_missing_validation_metrics"
        return True, detail

    incumbent_cagr = float(incumbent_metrics.cagr)
    cap = ADJACENT_VALIDATION_INCUMBENT_CAP.get(validation_window)
    if cap is not None and incumbent_cagr > cap:
        effective_incumbent_cagr = cap
        detail["effective_incumbent_cagr"] = effective_incumbent_cagr
    else:
        effective_incumbent_cagr = incumbent_cagr

    required_cagr = max(threshold * effective_incumbent_cagr, ADJACENT_VALIDATION_ABSOLUTE_FLOOR)
    detail["required_cagr"] = required_cagr
    detail["reason"] = "threshold_check"
    return float(candidate_metrics.cagr) >= required_cagr, detail


def _fmt_validation_detail(detail: dict[str, Any]) -> str:
    parts: list[str] = []
    for key in ("validation_window", "threshold", "incumbent_id", "incumbent_cagr", "required_cagr", "candidate_cagr", "reason"):
        if key not in detail:
            continue
        value = detail[key]
        if isinstance(value, float):
            parts.append(f"{key}={value:.4f}")
        else:
            parts.append(f"{key}={value}")
    return ", ".join(parts)


def _pick_single_window_winner_with_validation(
    latest: pd.DataFrame,
    sample_tag: str,
    *,
    allowed_base_ids: set[str] | None,
    by_id: dict[str, pd.DataFrame],
    incumbent_winners: dict[str, str],
    enable_validation: bool,
    log_prefix: str = "",
) -> tuple[str, TrackMetrics]:
    """Pick the best-ranked candidate for ``sample_tag`` that also passes the
    adjacent-window check against ``incumbent_winners``.

    When validation is enabled and at least one candidate passes, return the
    top-ranked passing candidate. When all candidates fail validation, fall
    back to the existing incumbent (if any) to preserve stability — this is
    the safe choice during transient overfit incumbent situations.
    Otherwise fall back to the absolute top-ranked candidate.
    """
    candidates = _rank_single_window_candidates(latest, sample_tag, allowed_base_ids=allowed_base_ids)
    if not candidates:
        raise RuntimeError(f"No strategies have {sample_tag} window to compute the single-window winner.")

    if not enable_validation:
        return candidates[0]

    rejected_count = 0
    for candidate_id, candidate_metrics in candidates:
        passes, detail = _passes_adjacent_window_check(
            candidate_id=candidate_id,
            target_window=sample_tag,
            by_id=by_id,
            incumbent_winners=incumbent_winners,
        )
        if passes:
            return candidate_id, candidate_metrics
        rejected_count += 1
        if rejected_count <= 3:
            print(f"[validation]{log_prefix} rejected {candidate_id} for {sample_tag}: {_fmt_validation_detail(detail)}")

    # All candidates rejected — fall back to incumbent if available, else top-ranked.
    incumbent_track_key = WINDOW_TAG_TO_TRACK_KEY.get(sample_tag)
    incumbent_id = incumbent_winners.get(incumbent_track_key) if incumbent_track_key else None
    if incumbent_id and incumbent_id in by_id:
        incumbent_metrics = _compute_single_window_metrics(by_id[incumbent_id], sample_tag)
        if not _is_nan_metrics(incumbent_metrics):
            print(
                f"[validation]{log_prefix} no candidate passed for {sample_tag}; "
                f"keeping incumbent {incumbent_id}"
            )
            return incumbent_id, incumbent_metrics

    print(
        f"[validation]{log_prefix} no candidate passed for {sample_tag} and no incumbent fallback; "
        f"using top-ranked {candidates[0][0]}"
    )
    return candidates[0]


def _resolve_path_window_winners_with_convergence(
    *,
    latest: pd.DataFrame,
    allowed_base_ids: set[str],
    by_id: dict[str, pd.DataFrame],
    initial_incumbents: dict[str, str],
    enable_validation: bool,
    log_prefix: str,
    max_iterations: int = 3,
) -> dict[str, tuple[str, TrackMetrics]]:
    """Pick the four window winners for a single path with iterative convergence.

    Each iteration uses the previous iteration's winners as incumbents for
    adjacent-window validation. This breaks the circular dependency that arises
    when a JSON-loaded incumbent is itself an overfit outlier (e.g., an old
    2025 winner with extreme CAGR forces an unrealistically high validation bar
    that only the same overfit strategy can clear). Within 2-3 iterations the
    assignments stabilize on a self-consistent set.
    """
    target_windows = ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01")
    incumbents = dict(initial_incumbents)
    last_winners: dict[str, tuple[str, TrackMetrics]] = {}
    for iteration in range(max_iterations):
        iter_log_prefix = f"{log_prefix}[iter{iteration + 1}]" if enable_validation else log_prefix
        winners: dict[str, tuple[str, TrackMetrics]] = {}
        for tag in target_windows:
            winners[tag] = _pick_single_window_winner_with_validation(
                latest,
                tag,
                allowed_base_ids=allowed_base_ids,
                by_id=by_id,
                incumbent_winners=incumbents,
                enable_validation=enable_validation,
                log_prefix=iter_log_prefix,
            )
        if not enable_validation:
            return winners
        new_id_map = {tag: winner[0] for tag, winner in winners.items()}
        if last_winners and {tag: w[0] for tag, w in last_winners.items()} == new_id_map:
            return last_winners
        incumbents = {WINDOW_TAG_TO_TRACK_KEY[tag]: winner[0] for tag, winner in winners.items()}
        last_winners = winners
    return last_winners


def _leaderboard_entry(
    *,
    rank: int,
    strategy_id: str,
    metrics: TrackMetrics | dict[str, float],
    strategies: dict[str, dict],
    official_winner_id: str | None = None,
    raw_winner_id: str | None = None,
    validation_detail: dict[str, Any] | None = None,
) -> dict[str, Any]:
    metric_payload = _metrics_to_dict(metrics) if isinstance(metrics, TrackMetrics) else dict(metrics)
    entry: dict[str, Any] = {
        "rank": rank,
        "strategy_base_id": strategy_id,
        "strategy_base_name": str(strategies.get(strategy_id, {}).get("strategy_base_name") or strategy_id),
        "metrics": metric_payload,
        "is_official_winner": strategy_id == official_winner_id,
        "is_raw_winner": strategy_id == raw_winner_id,
    }
    if validation_detail:
        entry["validation"] = {
            "passed": bool(validation_detail.get("passed")),
            "validation_window": validation_detail.get("validation_window"),
            "required_cagr": validation_detail.get("required_cagr"),
            "candidate_cagr": validation_detail.get("candidate_cagr"),
            "incumbent_id": validation_detail.get("incumbent_id"),
            "reason": validation_detail.get("reason"),
        }
    return entry


def _build_single_window_leaderboard(
    latest: pd.DataFrame,
    sample_tag: str,
    *,
    allowed_base_ids: set[str] | None,
    by_id: dict[str, pd.DataFrame],
    incumbent_winners: dict[str, str],
    enable_validation: bool,
    official_winner_id: str,
    raw_winner_id: str | None,
    strategies: dict[str, dict],
    limit: int = TRACK_LEADERBOARD_LIMIT,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for rank, (candidate_id, metrics) in enumerate(
        _rank_single_window_candidates(latest, sample_tag, allowed_base_ids=allowed_base_ids)[:limit],
        start=1,
    ):
        validation_detail: dict[str, Any] | None = None
        if enable_validation:
            passed, detail = _passes_adjacent_window_check(
                candidate_id=candidate_id,
                target_window=sample_tag,
                by_id=by_id,
                incumbent_winners=incumbent_winners,
            )
            validation_detail = {**detail, "passed": passed}
        rows.append(
            _leaderboard_entry(
                rank=rank,
                strategy_id=candidate_id,
                metrics=metrics,
                strategies=strategies,
                official_winner_id=official_winner_id,
                raw_winner_id=raw_winner_id,
                validation_detail=validation_detail,
            )
        )
    return rows


def _fmt_pct(value: float, digits: int = 2) -> str:
    if pd.isna(value):
        return "n/a"
    return f"{value * 100:.{digits}f}%"


def _metrics_close(a: float, b: float, tol: float = 1e-12) -> bool:
    if pd.isna(a) and pd.isna(b):
        return True
    return abs(float(a) - float(b)) <= tol


def _load_history(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"path1": {}, "path2": {}, "path3": {}}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"path1": {}, "path2": {}, "path3": {}}
    if not isinstance(payload, dict):
        return {"path1": {}, "path2": {}, "path3": {}}
    payload.setdefault("path1", {})
    payload.setdefault("path2", {})
    payload.setdefault("path3", {})
    return payload


def _window_metrics_for_strategy(strategies: dict[str, dict], winner_id: str, sample_tag: str) -> dict[str, float]:
    info = strategies[winner_id]
    window = info["windows"].get(sample_tag, {})
    return {
        "total_return": float(window.get("total_return", float("nan"))),
        "cagr": float(window.get("cagr", float("nan"))),
        "max_drawdown": float(window.get("max_drawdown", float("nan"))),
        "sharpe": float(window.get("sharpe", float("nan"))),
        "turnover": float(window.get("turnover", float("nan"))),
    }


def _build_history_entry(
    *,
    as_of: str,
    winner_id: str,
    strategy_name: str,
    sample_tag: str,
    metrics: dict[str, float],
    raw_winner_id: str | None = None,
    raw_strategy_name: str | None = None,
    raw_metrics: dict[str, float] | None = None,
) -> dict[str, Any]:
    entry: dict[str, Any] = {
        "as_of": as_of,
        "sample_tag": sample_tag,
        "winner": winner_id,
        "strategy_base_name": strategy_name,
        "total_return": metrics["total_return"],
        "cagr": metrics["cagr"],
        "max_drawdown": metrics["max_drawdown"],
        "sharpe": metrics["sharpe"],
        "turnover": metrics["turnover"],
    }
    if raw_winner_id and raw_metrics:
        entry.update(
            {
                "raw_winner": raw_winner_id,
                "raw_strategy_base_name": raw_strategy_name or raw_winner_id,
                "raw_total_return": raw_metrics["total_return"],
                "raw_cagr": raw_metrics["cagr"],
                "raw_max_drawdown": raw_metrics["max_drawdown"],
                "raw_sharpe": raw_metrics["sharpe"],
                "raw_turnover": raw_metrics["turnover"],
            }
        )
    return entry


def _history_entry_changed(old_entry: dict[str, Any], new_entry: dict[str, Any]) -> bool:
    if not old_entry:
        return True
    if str(old_entry.get("winner", "")) != str(new_entry.get("winner", "")):
        return True
    if str(old_entry.get("strategy_base_name", "")) != str(new_entry.get("strategy_base_name", "")):
        return True
    if str(old_entry.get("raw_winner", "")) != str(new_entry.get("raw_winner", "")):
        return True
    if str(old_entry.get("raw_strategy_base_name", "")) != str(new_entry.get("raw_strategy_base_name", "")):
        return True
    for key in (
        "total_return",
        "cagr",
        "max_drawdown",
        "sharpe",
        "turnover",
        "raw_total_return",
        "raw_cagr",
        "raw_max_drawdown",
        "raw_sharpe",
        "raw_turnover",
    ):
        if not _metrics_close(old_entry.get(key, float("nan")), new_entry.get(key, float("nan"))):
            return True
    return False


def _dedupe_entries_by_as_of(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not entries:
        return entries
    seen: set[str] = set()
    kept_reversed: list[dict[str, Any]] = []
    for entry in reversed(entries):
        key = str(entry.get("as_of", ""))
        if key in seen:
            continue
        seen.add(key)
        kept_reversed.append(entry)
    return list(reversed(kept_reversed))


def render_history_markdown(history: dict[str, Any]) -> str:
    lines: list[str] = [
        "# 跟踪赢家历史",
        "",
        "这个文档记录三条研究路径在四个窗口下的赢家变化历史。",
        "仅当赢家策略或关键指标发生变化时，才会追加新记录。",
        "",
    ]
    path_titles = {
        "path1": "Path 1：渐进优化路径",
        "path2": "Path 2：无约束上限探索",
        "path3": "Path 3：周度高频路径",
    }
    for path_key in ("path1", "path2", "path3"):
        lines.extend([f"## {path_titles[path_key]}", ""])
        path_bucket = history.get(path_key, {})
        for track_key, _, track_label in TRACK_SEQUENCE:
            lines.extend([f"### {track_label}", ""])
            entries = list(path_bucket.get(track_key, []))
            if not entries:
                lines.extend(["暂无记录。", ""])
                continue
            lines.append("| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |")
            lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")
            for entry in reversed(entries):
                raw_winner = str(entry.get("raw_winner") or "")
                raw_cell = f"`{raw_winner}`" if raw_winner else ""
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            str(entry.get("as_of", "")),
                            f"`{entry.get('winner', '')}`",
                            str(entry.get("strategy_base_name", "")),
                            raw_cell,
                            _fmt_pct(float(entry.get("total_return", float("nan")))),
                            _fmt_pct(float(entry.get("cagr", float("nan")))),
                            _fmt_pct(float(entry.get("max_drawdown", float("nan")))),
                            f"{float(entry.get('sharpe', float('nan'))):.4f}",
                            f"{float(entry.get('turnover', float('nan'))):.2f}",
                        ]
                    )
                    + " |"
                )
            lines.append("")
        robust_entries = list(path_bucket.get(ROBUST_TRACK_KEY, []))
        lines.extend(["### 鲁棒候选", ""])
        if not robust_entries:
            lines.extend(["暂无记录。", ""])
        else:
            lines.append("| 日期 | 策略ID | 策略名称 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |")
            lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
            for entry in reversed(robust_entries):
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            str(entry.get("as_of", "")),
                            f"`{entry.get('winner', '')}`",
                            str(entry.get("strategy_base_name", "")),
                            _fmt_pct(float(entry.get("total_return", float("nan")))),
                            _fmt_pct(float(entry.get("cagr", float("nan")))),
                            _fmt_pct(float(entry.get("max_drawdown", float("nan")))),
                            f"{float(entry.get('sharpe', float('nan'))):.4f}",
                            f"{float(entry.get('turnover', float('nan'))):.2f}",
                        ]
                    )
                    + " |"
                )
            lines.append("")
    return "\n".join(lines).strip() + "\n"


def update_history(
    *,
    history_path: Path,
    markdown_path: Path,
    as_of: str,
    strategies: dict[str, dict],
    path1_winners: dict[str, str],
    path2_winners: dict[str, str],
    path3_winners: dict[str, str] | None = None,
    path1_robust_id: str | None = None,
    path2_robust_id: str | None = None,
    path3_robust_id: str | None = None,
    raw_winners_by_path: dict[str, dict[str, tuple[str, TrackMetrics]]] | None = None,
) -> dict[str, Any]:
    history = _load_history(history_path)
    raw_winners_by_path = raw_winners_by_path or {}
    for path_key, winners in (("path1", path1_winners), ("path2", path2_winners), ("path3", path3_winners or {})):
        path_bucket = history.setdefault(path_key, {})
        for track_key, sample_tag, _ in TRACK_SEQUENCE:
            winner_id = winners.get(track_key, "")
            if not winner_id or winner_id not in strategies:
                continue
            strategy_name = str(strategies[winner_id]["strategy_base_name"])
            metrics = _window_metrics_for_strategy(strategies, winner_id, sample_tag)
            raw_winner_id = None
            raw_strategy_name = None
            raw_metrics = None
            raw_entry = raw_winners_by_path.get(path_key, {}).get(sample_tag)
            if raw_entry:
                raw_candidate_id = raw_entry[0]
                if raw_candidate_id and raw_candidate_id != winner_id and raw_candidate_id in strategies:
                    raw_winner_id = raw_candidate_id
                    raw_strategy_name = str(strategies[raw_candidate_id]["strategy_base_name"])
                    raw_metrics = _window_metrics_for_strategy(strategies, raw_candidate_id, sample_tag)
            new_entry = _build_history_entry(
                as_of=as_of,
                winner_id=winner_id,
                strategy_name=strategy_name,
                sample_tag=sample_tag,
                metrics=metrics,
                raw_winner_id=raw_winner_id,
                raw_strategy_name=raw_strategy_name,
                raw_metrics=raw_metrics,
            )
            entries = _dedupe_entries_by_as_of(list(path_bucket.get(track_key, [])))
            last_entry = entries[-1] if entries else {}
            if entries and str(last_entry.get("as_of", "")) == str(as_of):
                if _history_entry_changed(last_entry, new_entry):
                    entries[-1] = new_entry
            else:
                if _history_entry_changed(last_entry, new_entry):
                    entries.append(new_entry)
            path_bucket[track_key] = entries
    for path_key, robust_id in (
        ("path1", path1_robust_id),
        ("path2", path2_robust_id),
        ("path3", path3_robust_id),
    ):
        if not robust_id or robust_id not in strategies:
            continue
        path_bucket = history.setdefault(path_key, {})
        strategy_name = str(strategies[robust_id]["strategy_base_name"])
        metrics = _window_metrics_for_strategy(strategies, robust_id, "since_2020_01")
        new_entry = _build_history_entry(
            as_of=as_of,
            winner_id=robust_id,
            strategy_name=strategy_name,
            sample_tag="since_2020_01",
            metrics=metrics,
        )
        entries = _dedupe_entries_by_as_of(list(path_bucket.get(ROBUST_TRACK_KEY, [])))
        last_entry = entries[-1] if entries else {}
        if entries and str(last_entry.get("as_of", "")) == str(as_of):
            if _history_entry_changed(last_entry, new_entry):
                entries[-1] = new_entry
        else:
            if _history_entry_changed(last_entry, new_entry):
                entries.append(new_entry)
        path_bucket[ROBUST_TRACK_KEY] = entries
    history_path.parent.mkdir(parents=True, exist_ok=True)
    history_path.write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    markdown_path.parent.mkdir(parents=True, exist_ok=True)
    markdown_path.write_text(render_history_markdown(history), encoding="utf-8")
    return history


def _parse_date(value: object) -> pd.Timestamp | None:
    parsed = pd.to_datetime(value, errors="coerce")
    if pd.isna(parsed):
        return None
    return pd.Timestamp(parsed).normalize()


def _load_open_trade_dates(calendar_path: Path, as_of: str) -> list[pd.Timestamp]:
    as_of_ts = _parse_date(as_of)
    if as_of_ts is None or not calendar_path.exists():
        return []
    try:
        frame = pd.read_csv(calendar_path)
    except Exception:
        return []
    if "cal_date" not in frame.columns or "is_open" not in frame.columns:
        return []
    opened = frame[frame["is_open"].astype(str).isin({"1", "1.0", "true", "True"})].copy()
    dates = pd.to_datetime(opened["cal_date"], errors="coerce")
    dates = dates.dropna().map(lambda value: pd.Timestamp(value).normalize())
    return sorted({date for date in dates if date <= as_of_ts})


def _trading_days_since(last_win_date: object, as_of: str, open_trade_dates: list[pd.Timestamp]) -> int:
    last_win_ts = _parse_date(last_win_date)
    as_of_ts = _parse_date(as_of)
    if last_win_ts is None or as_of_ts is None or last_win_ts >= as_of_ts:
        return 0
    if open_trade_dates:
        return sum(1 for date in open_trade_dates if last_win_ts < date <= as_of_ts)
    return len(pd.bdate_range(last_win_ts + pd.offsets.BDay(1), as_of_ts))


def _metric_value(metrics: dict[str, Any], *keys: str, default: float = 0.0) -> float:
    for key in keys:
        if key in metrics and metrics[key] is not None:
            try:
                return float(metrics[key])
            except (TypeError, ValueError):
                continue
    return default


def _core_active_sort_key(item: dict[str, Any], current_winner_ids: set[str]) -> tuple[object, ...]:
    metrics = item.get("last_metrics") if isinstance(item.get("last_metrics"), dict) else {}
    last_win_ts = _parse_date(item.get("last_win_date")) or pd.Timestamp("1900-01-01")
    return (
        str(item.get("strategy_id", "")) in current_winner_ids,
        last_win_ts,
        int(item.get("win_count") or 0),
        _metric_value(metrics, "cagr_mean", "weighted_cagr", "cagr"),
        _metric_value(metrics, "sharpe_mean", "weighted_sharpe", "sharpe"),
        _metric_value(metrics, "max_drawdown_worst", "weighted_max_drawdown", "max_drawdown", default=-1.0),
        -_metric_value(metrics, "turnover_mean", "weighted_turnover", "turnover", default=999.0),
        str(item.get("strategy_id", "")),
    )


def _build_core_active_winner_entries(payload: dict[str, Any], strategies: dict[str, dict]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    sample_tag_by_track = {track_key: sample_tag for track_key, sample_tag, _ in TRACK_SEQUENCE}

    def add_entry(
        *,
        path_key: str,
        track_key: str,
        strategy_id: object,
        metrics: object,
        sample_tag: str,
        kind: str = "validated",
        refresh_only: bool = False,
    ) -> None:
        if not strategy_id:
            return
        sid = str(strategy_id)
        strategy_info = strategies.get(sid, {})
        entries.append(
            {
                "strategy_id": sid,
                "strategy_name": str(strategy_info.get("strategy_base_name") or sid),
                "path": path_key,
                "track": track_key,
                "sample_tag": sample_tag,
                "metrics": metrics if isinstance(metrics, dict) else {},
                "kind": kind,
                "refresh_only": bool(refresh_only),
            }
        )

    def add_track_pair(*, path_key: str, track_key: str, track_meta: dict[str, Any]) -> None:
        sample_tag = sample_tag_by_track.get(str(track_key), "")
        validated_id = track_meta.get("winner")
        add_entry(
            path_key=path_key,
            track_key=str(track_key),
            strategy_id=validated_id,
            metrics=track_meta.get("metrics"),
            sample_tag=sample_tag,
            kind="validated",
        )
        # Raw winner is observation-only: keep it in the registry so its
        # forward-looking performance keeps being tracked even when
        # adjacent-window validation displaces it from the official slot.
        raw_id = track_meta.get("raw_winner")
        if raw_id and raw_id != validated_id:
            add_entry(
                path_key=path_key,
                track_key=str(track_key),
                strategy_id=raw_id,
                metrics=track_meta.get("raw_metrics"),
                sample_tag=sample_tag,
                kind="raw",
                refresh_only=True,
            )

    for track_key, track_meta in (payload.get("tracks") or {}).items():
        if not isinstance(track_meta, dict):
            continue
        if track_key == ROBUST_TRACK_KEY:
            add_entry(
                path_key="path1",
                track_key=ROBUST_TRACK_KEY,
                strategy_id=track_meta.get("strategy_base_id"),
                metrics=track_meta.get("robust_metrics"),
                sample_tag="since_2020_01",
                kind="robust",
            )
        else:
            add_track_pair(path_key="path1", track_key=str(track_key), track_meta=track_meta)

    for path_key in ("path2", "path3"):
        path_payload = payload.get(path_key) or {}
        if not isinstance(path_payload, dict):
            continue
        for track_key, track_meta in (path_payload.get("tracks") or {}).items():
            if not isinstance(track_meta, dict):
                continue
            add_track_pair(path_key=path_key, track_key=str(track_key), track_meta=track_meta)
        add_entry(
            path_key=path_key,
            track_key=ROBUST_TRACK_KEY,
            strategy_id=path_payload.get("strategy_base_id"),
            metrics=path_payload.get("robust_metrics"),
            sample_tag="since_2020_01",
            kind="robust",
        )
    return entries


def _core_active_metrics_from_history(entry: dict[str, Any], *, prefix: str = "") -> dict[str, float]:
    metrics: dict[str, float] = {}
    for key in ("total_return", "cagr", "max_drawdown", "sharpe", "turnover"):
        source_key = f"{prefix}{key}" if prefix else key
        if source_key not in entry:
            continue
        try:
            metrics[key] = float(entry[source_key])
        except (TypeError, ValueError):
            continue
    return metrics


def _build_core_active_history_entry_groups(
    *,
    history_path: Path,
    as_of: str,
    stale_trading_days: int,
    calendar_path: Path = TRADE_CALENDAR_PATH,
) -> list[tuple[str, list[dict[str, Any]]]]:
    history = _load_history(history_path)
    open_trade_dates = _load_open_trade_dates(calendar_path, as_of)
    track_sample_tags = {track_key: sample_tag for track_key, sample_tag, _ in TRACK_SEQUENCE}
    track_sample_tags[ROBUST_TRACK_KEY] = "since_2020_01"
    grouped: dict[str, list[dict[str, Any]]] = {}

    for path_key in ("path1", "path2", "path3"):
        path_bucket = history.get(path_key, {})
        if not isinstance(path_bucket, dict):
            continue
        for track_key, default_sample_tag in track_sample_tags.items():
            entries = path_bucket.get(track_key, [])
            if not isinstance(entries, list):
                continue
            for entry in entries:
                if not isinstance(entry, dict):
                    continue
                entry_as_of = str(entry.get("as_of") or "")
                strategy_id = str(entry.get("winner") or "").strip()
                if not entry_as_of or not strategy_id:
                    continue
                if _trading_days_since(entry_as_of, as_of, open_trade_dates) >= stale_trading_days:
                    continue
                kind = "robust" if track_key == ROBUST_TRACK_KEY else "validated"
                grouped.setdefault(entry_as_of, []).append(
                    {
                        "strategy_id": strategy_id,
                        "strategy_name": str(entry.get("strategy_base_name") or strategy_id),
                        "path": path_key,
                        "track": track_key,
                        "sample_tag": str(entry.get("sample_tag") or default_sample_tag),
                        "metrics": _core_active_metrics_from_history(entry),
                        "kind": kind,
                        "refresh_only": False,
                    }
                )
                raw_strategy_id = str(entry.get("raw_winner") or "").strip()
                if raw_strategy_id:
                    grouped.setdefault(entry_as_of, []).append(
                        {
                            "strategy_id": raw_strategy_id,
                            "strategy_name": str(entry.get("raw_strategy_base_name") or raw_strategy_id),
                            "path": path_key,
                            "track": track_key,
                            "sample_tag": str(entry.get("sample_tag") or default_sample_tag),
                            "metrics": _core_active_metrics_from_history(entry, prefix="raw_"),
                            "kind": "raw",
                            "refresh_only": True,
                        }
                    )
    return [(entry_as_of, grouped[entry_as_of]) for entry_as_of in sorted(grouped)]


def backfill_core_active_registry_from_history(
    *,
    path: Path,
    history_path: Path,
    as_of: str,
    max_size: int,
    stale_trading_days: int,
    calendar_path: Path = TRADE_CALENDAR_PATH,
) -> dict[str, int]:
    as_of_ts = _parse_date(as_of)
    groups = _build_core_active_history_entry_groups(
        history_path=history_path,
        as_of=as_of,
        stale_trading_days=stale_trading_days,
        calendar_path=calendar_path,
    )
    if groups:
        try:
            path.unlink()
        except FileNotFoundError:
            pass
    backfilled_dates = 0
    backfilled_entries = 0
    backfilled_strategy_ids: set[str] = set()
    for entry_as_of, entries in groups:
        entry_ts = _parse_date(entry_as_of)
        if as_of_ts is not None and entry_ts is not None and entry_ts >= as_of_ts:
            continue
        update_core_active_registry(
            path=path,
            as_of=entry_as_of,
            winner_entries=entries,
            max_size=max_size,
            stale_trading_days=stale_trading_days,
            calendar_path=calendar_path,
        )
        backfilled_dates += 1
        backfilled_entries += len(entries)
        backfilled_strategy_ids.update(str(entry.get("strategy_id") or "") for entry in entries)
    return {
        "dates": backfilled_dates,
        "entries": backfilled_entries,
        "strategies": len({strategy_id for strategy_id in backfilled_strategy_ids if strategy_id}),
    }


def _load_core_active_registry(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    registry: dict[str, dict[str, Any]] = {}
    if not isinstance(payload, dict):
        return registry
    for bucket_key in ("refresh_only_strategies", "strategies"):
        strategies = payload.get(bucket_key, [])
        if not isinstance(strategies, list):
            continue
        for item in strategies:
            if not isinstance(item, dict) or not item.get("strategy_id"):
                continue
            registry[str(item["strategy_id"])] = dict(item)
    return registry


def update_core_active_registry(
    *,
    path: Path,
    as_of: str,
    winner_entries: list[dict[str, Any]],
    max_size: int,
    stale_trading_days: int,
    calendar_path: Path = TRADE_CALENDAR_PATH,
) -> dict[str, Any]:
    as_of_str = str(pd.Timestamp(as_of).date())
    max_size = max(1, int(max_size))
    stale_trading_days = max(1, int(stale_trading_days))
    registry = _load_core_active_registry(path)
    current_by_id: dict[str, list[dict[str, Any]]] = {}
    for entry in winner_entries:
        strategy_id = str(entry.get("strategy_id") or "").strip()
        if not strategy_id:
            continue
        current_by_id.setdefault(strategy_id, []).append(entry)

    def is_refresh_only_role(role: dict[str, Any]) -> bool:
        return bool(role.get("refresh_only")) or str(role.get("kind", "")).strip().lower() == "raw"

    for strategy_id, roles in current_by_id.items():
        roles_sorted = sorted(
            roles,
            key=lambda r: (
                is_refresh_only_role(r),
                0 if str(r.get("kind", "validated")) in {"validated", "robust"} else 1,
            ),
        )
        primary = roles_sorted[0]
        refresh_only = all(is_refresh_only_role(role) for role in roles_sorted)
        item = registry.get(strategy_id, {"strategy_id": strategy_id})
        win_dates = [str(value) for value in item.get("win_dates", []) if str(value)]
        if as_of_str not in win_dates:
            win_dates.append(as_of_str)
        win_dates = sorted(set(win_dates))
        first_win_date = min(win_dates)
        last_win_date = max(win_dates)
        is_latest_win = as_of_str == last_win_date
        if is_latest_win:
            strategy_name = primary.get("strategy_name") or item.get("strategy_name") or strategy_id
            last_path = primary.get("path", "")
            last_track = primary.get("track", "")
            last_sample_tag = primary.get("sample_tag", "")
            last_metrics = primary.get("metrics", {})
        else:
            strategy_name = item.get("strategy_name") or primary.get("strategy_name") or strategy_id
            last_path = item.get("last_path", "")
            last_track = item.get("last_track", "")
            last_sample_tag = item.get("last_sample_tag", "")
            last_metrics = item.get("last_metrics", {})
        item.update(
            {
                "strategy_id": strategy_id,
                "strategy_name": strategy_name,
                "first_win_date": first_win_date,
                "last_win_date": last_win_date,
                "win_dates": win_dates,
                "win_count": len(win_dates),
                "last_path": last_path,
                "last_track": last_track,
                "last_sample_tag": last_sample_tag,
                "last_metrics": last_metrics,
                "current_winner_roles": [
                    {
                        "path": role.get("path", ""),
                        "track": role.get("track", ""),
                        "sample_tag": role.get("sample_tag", ""),
                        "kind": role.get("kind", "validated"),
                        "refresh_only": is_refresh_only_role(role),
                    }
                    for role in roles_sorted
                ],
                "refresh_only": refresh_only,
                "active": not refresh_only,
                "days_since_last_win": 0,
            }
        )
        registry[strategy_id] = item

    current_ids = set(current_by_id)
    current_winner_ids = {
        strategy_id
        for strategy_id, roles in current_by_id.items()
        if any(not is_refresh_only_role(role) for role in roles)
    }
    current_refresh_only_ids = current_ids - current_winner_ids
    open_trade_dates = _load_open_trade_dates(calendar_path, as_of_str)
    active_items: list[dict[str, Any]] = []
    refresh_only_items: list[dict[str, Any]] = []
    expired_strategy_ids: list[str] = []
    for strategy_id, item in registry.items():
        if strategy_id not in current_ids:
            days_since = _trading_days_since(item.get("last_win_date"), as_of_str, open_trade_dates)
            item["current_winner_roles"] = []
            item["days_since_last_win"] = days_since
            if days_since >= stale_trading_days:
                expired_strategy_ids.append(strategy_id)
                continue
        refresh_only = bool(item.get("refresh_only"))
        item["active"] = not refresh_only
        if refresh_only:
            refresh_only_items.append(item)
        else:
            active_items.append(item)

    active_items.sort(key=lambda item: _core_active_sort_key(item, current_winner_ids), reverse=True)
    refresh_only_items.sort(key=lambda item: _core_active_sort_key(item, current_refresh_only_ids), reverse=True)
    kept_items = active_items[:max_size]
    kept_refresh_only_items = refresh_only_items[:max_size]
    trimmed_strategy_ids = [
        str(item.get("strategy_id", ""))
        for item in active_items[max_size:]
        if str(item.get("strategy_id", "")) not in current_winner_ids
    ]
    trimmed_refresh_only_strategy_ids = [
        str(item.get("strategy_id", ""))
        for item in refresh_only_items[max_size:]
        if str(item.get("strategy_id", "")) not in current_refresh_only_ids
    ]

    registry_payload = {
        "as_of": as_of_str,
        "max_size": max_size,
        "stale_trading_days": stale_trading_days,
        "current_winner_ids": sorted(current_winner_ids),
        "current_refresh_only_ids": sorted(current_refresh_only_ids),
        "expired_strategy_ids": sorted(expired_strategy_ids),
        "trimmed_strategy_ids": sorted(set(trimmed_strategy_ids)),
        "trimmed_refresh_only_strategy_ids": sorted(set(trimmed_refresh_only_strategy_ids)),
        "strategies": kept_items,
        "refresh_only_strategies": kept_refresh_only_items,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(registry_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return registry_payload


def _compute_window_metrics(
    equity: pd.DataFrame,
    monthly_returns: pd.DataFrame,
    turnover: pd.DataFrame,
    *,
    rebalance_frequency: str = "monthly",
) -> dict[str, float]:
    nav = equity["nav"].astype(float)
    monthly_net = monthly_returns["net_return"].astype(float)
    periods_per_year = 12.0
    if str(rebalance_frequency).strip().lower() == "weekly":
        periods_per_year = 52.0
    elif str(rebalance_frequency).strip().lower() == "biweekly":
        periods_per_year = 26.0
    total_return = float(nav.iloc[-1] - 1.0)
    periods = len(monthly_net)
    years = periods / periods_per_year if periods > 0 else np.nan
    cagr = float(nav.iloc[-1] ** (1 / years) - 1) if periods > 0 and nav.iloc[-1] > 0 else np.nan
    max_drawdown = float(equity["drawdown"].min())
    annual_volatility = float(monthly_net.std(ddof=1) * np.sqrt(periods_per_year)) if periods > 1 else np.nan
    sharpe_ratio = (
        float((monthly_net.mean() / monthly_net.std(ddof=1)) * np.sqrt(periods_per_year))
        if periods > 1 and monthly_net.std(ddof=1) > 0
        else np.nan
    )
    average_annual_turnover = (
        float(turnover["one_way_turnover"].astype(float).sum() / years)
        if not turnover.empty and periods > 0 and years > 0
        else np.nan
    )
    return {
        "total_return": total_return,
        "cagr": cagr,
        "max_drawdown": max_drawdown,
        "annual_volatility": annual_volatility,
        "sharpe_ratio": sharpe_ratio,
        "average_annual_turnover": average_annual_turnover,
    }


def _slice_window_from_existing_results(base_id: str, sample_tag: str) -> dict[str, float] | None:
    sample_start = SAMPLE_TAG_STARTS.get(sample_tag)
    if sample_start is None:
        return None

    candidate_dirs: list[Path] = []
    if base_id in STATIC_BASE_IDS:
        candidate_dirs = candidate_strategy_result_dirs(base_id, market_scope="a_share")
    elif sample_tag == "since_2025_01":
        # since_2025 is a dedicated tracked window in this project: prefer its dedicated run.
        candidate_dirs = candidate_strategy_result_dirs(base_id, "since_2025_01", market_scope="a_share")
    elif sample_tag == "since_2026_01":
        # since_2026 is a display-only YTD window: derive from the shortest available recent run first.
        candidate_dirs = []
        for fallback_tag in ("since_2025_01", "since_2023_01", "since_2020_01", "since_2017_01"):
            candidate_dirs.extend(candidate_strategy_result_dirs(base_id, fallback_tag, market_scope="a_share"))
    else:
        # Prefer a dedicated run for the requested window when available.
        candidate_dirs = []
        for fallback_tag in (sample_tag, "since_2025_01", "since_2023_01", "since_2020_01", "since_2017_01"):
            for path in candidate_strategy_result_dirs(base_id, fallback_tag, market_scope="a_share"):
                if path not in candidate_dirs:
                    candidate_dirs.append(path)

    for result_dir in candidate_dirs:
        equity_path = result_dir / "equity_curve.csv"
        monthly_path = result_dir / "monthly_returns.csv"
        turnover_path = result_dir / "turnover.csv"
        summary_path = result_dir / "summary.json"
        if not (equity_path.exists() and monthly_path.exists() and turnover_path.exists()):
            continue
        rebalance_frequency = "monthly"
        if summary_path.exists():
            try:
                summary_payload = json.loads(summary_path.read_text(encoding="utf-8"))
                rebalance_frequency = str(summary_payload.get("rebalance_frequency") or "monthly")
            except Exception:
                rebalance_frequency = "monthly"
        equity = pd.read_csv(equity_path, parse_dates=["date"])
        if equity.empty or "date" not in equity.columns:
            continue
        earliest_date = pd.to_datetime(equity["date"], errors="coerce").min()
        if pd.isna(earliest_date) or earliest_date > sample_start:
            # The cached result doesn't cover the requested start date; don't mislabel it as a shorter/earlier window.
            continue
        monthly_returns = pd.read_csv(monthly_path, parse_dates=["date"])
        turnover = pd.read_csv(turnover_path, parse_dates=["date"])
        equity_window = equity[equity["date"] >= sample_start].copy()
        if equity_window.empty:
            continue
        start_nav = float(equity_window.iloc[0]["nav"])
        if start_nav <= 0:
            continue
        equity_window["nav"] = equity_window["nav"] / start_nav
        equity_window["drawdown"] = equity_window["nav"] / equity_window["nav"].cummax() - 1.0
        monthly_window = monthly_returns[monthly_returns["date"] >= sample_start].copy()
        turnover_window = turnover[turnover["date"] >= sample_start].copy()
        return _compute_window_metrics(
            equity_window,
            monthly_window,
            turnover_window,
            rebalance_frequency=rebalance_frequency,
        )
    return None


def _augment_with_synthetic_windows(latest: pd.DataFrame) -> pd.DataFrame:
    existing = latest.copy()
    needed_rows: list[dict[str, object]] = []
    existing_keys = {
        (str(row.strategy_base_id), str(row.sample_tag))
        for row in existing[["strategy_base_id", "sample_tag"]].itertuples(index=False)
    }
    base_name_map = (
        existing.sort_values(["strategy_base_id", "sample_end"])
        .drop_duplicates(subset=["strategy_base_id"], keep="last")
        .set_index("strategy_base_id")["strategy_base_name"]
        .astype(str)
        .to_dict()
    )
    sample_end_map = (
        existing.groupby("strategy_base_id")["sample_end"]
        .max()
        .to_dict()
    )
    fallback_sample_end = existing["sample_end"].max()
    sample_labels = {
        "since_2017_01": ("2017-01 起", "2017-01"),
        "since_2020_01": ("2020-01 起", "2020-01"),
        "since_2023_01": ("2023-01 起", "2023-01"),
        "since_2025_01": ("2025-01 起", "2025-01"),
        "since_2026_01": ("2026-01 起", "2026-01"),
    }
    for base_id in sorted(set(existing["strategy_base_id"].astype(str)) | STATIC_BASE_IDS):
        # Only synthesize short windows that are derived from existing longer runs:
        # since_2025 is part of tracking, while since_2026 is a display-only "this year" window.
        for sample_tag in ("since_2025_01", "since_2026_01"):
            if (base_id, sample_tag) in existing_keys:
                continue
            metrics = _slice_window_from_existing_results(base_id, sample_tag)
            if metrics is None:
                continue
            sample_start = SAMPLE_TAG_STARTS[sample_tag]
            sample_label, sample_short_label = sample_labels[sample_tag]
            needed_rows.append(
                {
                    "strategy_base_id": base_id,
                    "strategy_base_name": base_name_map.get(base_id, base_id),
                    "sample_tag": sample_tag,
                    "sample_label": sample_label,
                    "sample_short_label": sample_short_label,
                    "sample_start": sample_start,
                    "sample_end": sample_end_map.get(base_id, fallback_sample_end),
                    "cagr": metrics["cagr"],
                    "sharpe_ratio": metrics["sharpe_ratio"],
                    "max_drawdown": metrics["max_drawdown"],
                    "average_annual_turnover": metrics["average_annual_turnover"],
                    "total_return": metrics["total_return"],
                }
            )
    if not needed_rows:
        return existing
    return pd.concat([existing, pd.DataFrame(needed_rows)], ignore_index=True)


def _pick_path2_candidate(latest: pd.DataFrame) -> tuple[str, dict[str, float]]:
    required_tags = {"since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01"}
    candidates: list[tuple[str, dict[str, float]]] = []
    for base_id, group in latest.groupby("strategy_base_id"):
        tags = set(group["sample_tag"].astype(str))
        if not required_tags.issubset(tags):
            continue
        metrics_by_tag = {tag: _compute_single_window_metrics(group, tag) for tag in sorted(required_tags)}
        if any(any(np.isnan(v) for v in (m.cagr, m.sharpe, m.max_drawdown, m.turnover)) for m in metrics_by_tag.values()):
            continue
        cagr_values = [m.cagr for m in metrics_by_tag.values()]
        sharpe_values = [m.sharpe for m in metrics_by_tag.values()]
        maxdd_values = [m.max_drawdown for m in metrics_by_tag.values()]
        turn_values = [m.turnover for m in metrics_by_tag.values()]
        summary = {
            "cagr_mean": float(np.mean(cagr_values)),
            "cagr_min": float(np.min(cagr_values)),
            "sharpe_mean": float(np.mean(sharpe_values)),
            "max_drawdown_worst": float(np.min(maxdd_values)),
            "turnover_mean": float(np.mean(turn_values)),
        }
        candidates.append((str(base_id), summary))

    if not candidates:
        raise RuntimeError("No strategies have all four windows to compute Path 2 candidate.")

    candidates.sort(key=lambda item: _robust_sort_key(item[1]), reverse=True)
    return candidates[0]


def _robust_sort_key(summary: dict[str, float]) -> tuple[float, float, float, float, float]:
    return (
        float(summary["cagr_min"]),
        float(summary["max_drawdown_worst"]),
        float(summary["sharpe_mean"]),
        float(summary["cagr_mean"]),
        -float(summary["turnover_mean"]),
    )


def _rank_robust_candidates(latest: pd.DataFrame, *, allowed_base_ids: set[str] | None = None) -> list[tuple[str, dict[str, float]]]:
    required_tags = {"since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01"}
    candidates: list[tuple[str, dict[str, float]]] = []
    for base_id, group in latest.groupby("strategy_base_id"):
        base_id_str = str(base_id)
        if allowed_base_ids is not None and base_id_str not in allowed_base_ids:
            continue
        tags = set(group["sample_tag"].astype(str))
        if not required_tags.issubset(tags):
            continue
        metrics_by_tag = {tag: _compute_single_window_metrics(group, tag) for tag in sorted(required_tags)}
        if any(any(np.isnan(v) for v in (m.cagr, m.sharpe, m.max_drawdown, m.turnover)) for m in metrics_by_tag.values()):
            continue
        cagr_values = [m.cagr for m in metrics_by_tag.values()]
        sharpe_values = [m.sharpe for m in metrics_by_tag.values()]
        maxdd_values = [m.max_drawdown for m in metrics_by_tag.values()]
        turn_values = [m.turnover for m in metrics_by_tag.values()]
        summary = {
            "cagr_mean": float(np.mean(cagr_values)),
            "cagr_min": float(np.min(cagr_values)),
            "sharpe_mean": float(np.mean(sharpe_values)),
            "max_drawdown_worst": float(np.min(maxdd_values)),
            "turnover_mean": float(np.mean(turn_values)),
        }
        candidates.append((base_id_str, summary))
    candidates.sort(key=lambda item: _robust_sort_key(item[1]), reverse=True)
    return candidates


def _pick_robust_candidate(latest: pd.DataFrame, *, allowed_base_ids: set[str] | None = None) -> tuple[str, dict[str, float]]:
    candidates = _rank_robust_candidates(latest, allowed_base_ids=allowed_base_ids)
    if not candidates:
        raise RuntimeError("No strategies have all four windows to compute robust candidate.")
    return candidates[0]


def _render_block(
    strategies: dict[str, dict],
    window_2017_winner_id: str,
    window_2017_metrics: TrackMetrics,
    window_2023_winner_id: str,
    window_2023_metrics: TrackMetrics,
    window_2020_winner_id: str,
    window_2020_metrics: TrackMetrics,
    window_2025_winner_id: str,
    window_2025_metrics: TrackMetrics,
    path1_robust_id: str,
    path1_summary: dict[str, float],
    path2_window_2017_id: str,
    path2_window_2017_metrics: TrackMetrics,
    path2_window_2023_id: str,
    path2_window_2023_metrics: TrackMetrics,
    path2_window_2020_id: str,
    path2_window_2020_metrics: TrackMetrics,
    path2_window_2025_id: str,
    path2_window_2025_metrics: TrackMetrics,
    path2_id: str,
    path2_summary: dict[str, float],
    path3_window_2017_id: str,
    path3_window_2017_metrics: TrackMetrics,
    path3_window_2023_id: str,
    path3_window_2023_metrics: TrackMetrics,
    path3_window_2020_id: str,
    path3_window_2020_metrics: TrackMetrics,
    path3_window_2025_id: str,
    path3_window_2025_metrics: TrackMetrics,
    path3_id: str,
    path3_summary: dict[str, float],
    sample_end: str,
    raw_winners_lookup: dict[tuple[str, str], tuple[str, TrackMetrics]] | None = None,
) -> str:
    raw_winners_lookup = raw_winners_lookup or {}

    def render_track(
        title: str,
        weights: dict[str, float],
        winner_id: str,
        metrics: TrackMetrics,
        *,
        path_key: str | None = None,
        sample_tag: str | None = None,
    ) -> str:
        info = strategies[winner_id]
        windows = info["windows"]
        weight_str = ", ".join(f"{k.replace('since_', '').replace('_', '-')}={int(v*100)}%" for k, v in weights.items())
        def render_window(tag: str) -> str:
            if tag not in windows:
                return f"- `{SAMPLE_TAG_STARTS[tag].date()}` 窗口：n/a"
            return (
                f"- `{SAMPLE_TAG_STARTS[tag].date()}` → `{sample_end}`: "
                f"Total Return `{_fmt_pct(windows[tag]['total_return'])}`, "
                f"CAGR `{_fmt_pct(windows[tag]['cagr'])}`, "
                f"Max DD `{_fmt_pct(windows[tag]['max_drawdown'])}`, "
                f"Sharpe `{windows[tag]['sharpe']:.4f}`, "
                f"Turnover `{windows[tag]['turnover']:.2f}`"
            )

        lines = [
            f"### {title}",
            "",
            f"- 鲁棒赢家：`{winner_id}`（{info['strategy_base_name']}）",
            f"- 加权指标（CAGR / Sharpe / Max DD / Turnover）："
            f"`{_fmt_pct(metrics.cagr)}` / `{metrics.sharpe:.4f}` / `{_fmt_pct(metrics.max_drawdown)}` / `{metrics.turnover:.2f}`",
        ]

        raw_entry = raw_winners_lookup.get((path_key or "", sample_tag or ""))
        if raw_entry and raw_entry[0] and raw_entry[0] != winner_id:
            raw_id, raw_metrics_obj = raw_entry
            raw_info = strategies.get(raw_id)
            raw_name = raw_info["strategy_base_name"] if raw_info else raw_id
            lines.extend([
                f"- 单窗口最高收益（被鲁棒检验过滤）：`{raw_id}`（{raw_name}）",
                f"  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）："
                f"`{_fmt_pct(raw_metrics_obj.cagr)}` / `{raw_metrics_obj.sharpe:.4f}` / "
                f"`{_fmt_pct(raw_metrics_obj.max_drawdown)}` / `{raw_metrics_obj.turnover:.2f}`",
            ])

        lines.extend([
            "",
            f"窗口指标（截至 `{sample_end}`，权重：{weight_str}）：",
            "",
            render_window("since_2017_01"),
            render_window("since_2020_01"),
            render_window("since_2023_01"),
            render_window("since_2025_01"),
            render_window("since_2026_01"),
            "",
        ])
        return "\n".join(lines)

    def render_path2(title: str, base_id: str, summary: dict[str, float]) -> str:
        info = strategies[base_id]
        windows = info["windows"]
        def render_window(tag: str) -> str:
            if tag not in windows:
                return f"- `{SAMPLE_TAG_STARTS[tag].date()}` 窗口：n/a"
            return (
                f"- `{SAMPLE_TAG_STARTS[tag].date()}` → `{sample_end}`: "
                f"Total Return `{_fmt_pct(windows[tag]['total_return'])}`, "
                f"CAGR `{_fmt_pct(windows[tag]['cagr'])}`, "
                f"Max DD `{_fmt_pct(windows[tag]['max_drawdown'])}`, "
                f"Sharpe `{windows[tag]['sharpe']:.4f}`, "
                f"Turnover `{windows[tag]['turnover']:.2f}`"
            )
        return "\n".join(
            [
                f"### {title}",
                "",
                f"- 策略：`{base_id}`（{info['strategy_base_name']}）",
                f"- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）："
                f"`{_fmt_pct(summary['cagr_mean'])}` / `{_fmt_pct(summary['cagr_min'])}` / `{summary['sharpe_mean']:.4f}` / "
                f"`{_fmt_pct(summary['max_drawdown_worst'])}` / `{summary['turnover_mean']:.2f}`",
                "",
                "窗口指标：",
                "",
                render_window("since_2017_01"),
                render_window("since_2020_01"),
                render_window("since_2023_01"),
                render_window("since_2025_01"),
                render_window("since_2026_01"),
                "",
            ]
        )

    parts = [
        "项目当前维护 **三条研究路线**：",
        "",
        "- **Path 1（胜出者核心主线）**：渐进优化路线，目标是在保持当前 winner-core 框架可交易、可控回撤的前提下，把长期 CAGR 持续推向 `25%~30%+`。",
        "- **Path 2（无约束上限探索）**：追求更高收益上限的独立路线，可以脱离当前框架自由试验；近期重点是优先把 `2020` 与 `2023` 两个窗口推向 `40%+ CAGR`。Path 2 会独立记录自己的窗口赢家与鲁棒候选，不需要先超过 Path 1 才更新。",
        "- **Path 3（周度高频调仓）**：专门跟踪纯周度换股候选，和“月度选股 + 周度仓位 overlay”分开评估，用于观察更高交易频率是否能带来可持续优势。",
        "",
        "当前验证窗口：",
        "",
        "- `since_2017_01`：长窗口",
        "- `since_2020_01`：中窗口",
        "- `since_2023_01`：短窗口",
        "- `since_2025_01`：超短窗口",
        "- `since_2026_01`：今年窗口（只用于展示当前四个窗口赢家今年以来表现，不单独评选 winner）",
        "",
        "## Path 1：窗口跟踪赢家",
        "",
        render_track("2017 窗口赢家", WEIGHTS_2017_ONLY, window_2017_winner_id, window_2017_metrics, path_key="path1", sample_tag="since_2017_01"),
        render_track("2023 窗口赢家", WEIGHTS_2023_ONLY, window_2023_winner_id, window_2023_metrics, path_key="path1", sample_tag="since_2023_01"),
        render_track("2020 窗口赢家", WEIGHTS_2020_ONLY, window_2020_winner_id, window_2020_metrics, path_key="path1", sample_tag="since_2020_01"),
        render_track("2025 窗口赢家", WEIGHTS_2025_ONLY, window_2025_winner_id, window_2025_metrics, path_key="path1", sample_tag="since_2025_01"),
        "## Path 1：鲁棒候选",
        "",
        render_path2("四窗口鲁棒候选", path1_robust_id, path1_summary),
        "## Path 2：窗口跟踪赢家",
        "",
        render_track("2017 窗口赢家（Path 2）", WEIGHTS_2017_ONLY, path2_window_2017_id, path2_window_2017_metrics, path_key="path2", sample_tag="since_2017_01"),
        render_track("2023 窗口赢家（Path 2）", WEIGHTS_2023_ONLY, path2_window_2023_id, path2_window_2023_metrics, path_key="path2", sample_tag="since_2023_01"),
        render_track("2020 窗口赢家（Path 2）", WEIGHTS_2020_ONLY, path2_window_2020_id, path2_window_2020_metrics, path_key="path2", sample_tag="since_2020_01"),
        render_track("2025 窗口赢家（Path 2）", WEIGHTS_2025_ONLY, path2_window_2025_id, path2_window_2025_metrics, path_key="path2", sample_tag="since_2025_01"),
        "## Path 2：鲁棒候选",
        "",
        render_path2("四窗口鲁棒候选", path2_id, path2_summary),
        "## Path 3：窗口跟踪赢家",
        "",
        render_track("2017 窗口赢家（Path 3）", WEIGHTS_2017_ONLY, path3_window_2017_id, path3_window_2017_metrics, path_key="path3", sample_tag="since_2017_01"),
        render_track("2023 窗口赢家（Path 3）", WEIGHTS_2023_ONLY, path3_window_2023_id, path3_window_2023_metrics, path_key="path3", sample_tag="since_2023_01"),
        render_track("2020 窗口赢家（Path 3）", WEIGHTS_2020_ONLY, path3_window_2020_id, path3_window_2020_metrics, path_key="path3", sample_tag="since_2020_01"),
        render_track("2025 窗口赢家（Path 3）", WEIGHTS_2025_ONLY, path3_window_2025_id, path3_window_2025_metrics, path_key="path3", sample_tag="since_2025_01"),
        "## Path 3：鲁棒候选",
        "",
        render_path2("四窗口鲁棒候选", path3_id, path3_summary),
    ]
    return "\n".join(parts).strip() + "\n"


def update_readme(readme_path: Path, new_block: str) -> None:
    content = readme_path.read_text(encoding="utf-8")
    if AUTO_START not in content or AUTO_END not in content:
        raise RuntimeError(
            f"README is missing automation markers. Add both {AUTO_START} and {AUTO_END} where the block should go."
        )
    before, rest = content.split(AUTO_START, 1)
    _, after = rest.split(AUTO_END, 1)
    updated = before + AUTO_START + "\n\n" + new_block + "\n" + AUTO_END + after
    readme_path.write_text(updated, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Update README weighted winners block from latest backtest CSV.")
    parser.add_argument("--comparison-csv", type=Path, default=DEFAULT_COMPARISON_CSV)
    parser.add_argument("--readme", type=Path, default=README_PATH)
    parser.add_argument("--write-json", type=Path, default=research_file("weighted_track_winners.json"))
    parser.add_argument("--history-json", type=Path, default=TRACKED_HISTORY_JSON_PATH)
    parser.add_argument("--history-md", type=Path, default=TRACKED_HISTORY_MD_PATH)
    parser.add_argument("--core-active-json", type=Path, default=CORE_ACTIVE_REGISTRY_JSON_PATH)
    parser.add_argument("--core-active-max-size", type=int, default=CORE_ACTIVE_MAX_SIZE)
    parser.add_argument("--core-active-stale-trading-days", type=int, default=CORE_ACTIVE_STALE_TRADING_DAYS)
    parser.add_argument(
        "--disable-adjacent-validation",
        action="store_true",
        help="Disable the adjacent-window validation guard (Phase 1). Use for debugging or "
        "rollback. By default, candidates must pass the asymmetric multi-window threshold "
        "check before being accepted as a window winner.",
    )
    args = parser.parse_args()
    enable_adjacent_validation = not args.disable_adjacent_validation
    existing_payload_path = args.write_json
    if not existing_payload_path.exists():
        fallback_payload_path = existing_research_file(existing_payload_path.name)
        if fallback_payload_path.exists():
            existing_payload_path = fallback_payload_path
    existing_payload = _load_tracked_payload(existing_payload_path)

    frame = pd.read_csv(args.comparison_csv)
    latest_all = _augment_with_synthetic_windows(_latest_per_strategy_window(frame))
    prefix = load_winner_core_prefix()
    path1_family_ids = load_path1_family_ids()
    active_family_ids = load_active_family_ids()
    if not path1_family_ids:
        raise RuntimeError(f"No winner-core strategies found with prefix={prefix!r}")
    path1_allowed_ids = path1_family_ids & active_family_ids

    path2_prefixes, path2_variant_ids = load_path2_scan_rules()
    path2_allowed_ids = {
        str(base_id)
        for base_id in set(latest_all["strategy_base_id"].astype(str).unique())
        if _matches_path2(str(base_id), path2_prefixes, path2_variant_ids)
    } - STATIC_BASE_IDS
    if not path2_allowed_ids:
        raise RuntimeError(
            "Path 2 candidate universe is empty. "
            "Check PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS in backtest_marketcap_etf.py."
        )

    path3_allowed_ids = {
        str(base_id)
        for base_id in set(latest_all["strategy_base_id"].astype(str).unique())
        if _matches_path3(str(base_id))
    } - STATIC_BASE_IDS
    path3_available = bool(path3_allowed_ids)
    if not path3_available:
        print("[path3] no pure weekly candidates in comparison CSV; preserving existing Path 3 winners.")

    # Enforce same as-of within each research path without letting a freshly
    # refreshed path hide still-current winners from another path.
    path1_latest = _filter_ids_to_current_as_of(latest_all, path1_allowed_ids)
    path2_latest = _filter_ids_to_current_as_of(latest_all, path2_allowed_ids)
    path3_latest = _filter_ids_to_current_as_of(latest_all, path3_allowed_ids)
    path1_available = not path1_latest.empty
    path2_available = not path2_latest.empty
    if not path1_available:
        print("[path1] no active winner-core rows in comparison CSV; preserving existing Path 1 winners.")
    if not path2_available:
        print("[path2] no scan rows in comparison CSV; preserving existing Path 2 winners.")
    latest = pd.concat([path1_latest, path2_latest, path3_latest], ignore_index=True).drop_duplicates(
        ["strategy_base_id", "sample_tag"],
        keep="last",
    )
    strategies = _build_strategy_map(latest)
    for strategy_id, info in (existing_payload.get("strategies") or {}).items():
        if isinstance(info, dict):
            copied = dict(info)
            copied.setdefault("sample_end", existing_payload.get("as_of", ""))
            strategies.setdefault(str(strategy_id), copied)
    if not strategies:
        raise RuntimeError("No strategies with complete 2017/2020/2023 windows found in comparison CSV.")

    existing_path1_winners = _load_existing_path1_winners(existing_payload_path)
    existing_winners_all_paths = _load_existing_winners_all_paths(existing_payload_path)
    path1_by_id: dict[str, pd.DataFrame] = {str(base_id): group for base_id, group in path1_latest.groupby("strategy_base_id")}
    path2_by_id: dict[str, pd.DataFrame] = {str(base_id): group for base_id, group in path2_latest.groupby("strategy_base_id")}
    path3_by_id: dict[str, pd.DataFrame] = {str(base_id): group for base_id, group in path3_latest.groupby("strategy_base_id")}

    def metrics_for(base_id: str, sample_tag: str) -> TrackMetrics:
        group = path1_by_id.get(str(base_id), pd.DataFrame())
        if group.empty or "sample_tag" not in group.columns:
            return TrackMetrics(cagr=float("nan"), sharpe=float("nan"), max_drawdown=float("nan"), turnover=float("nan"))
        return _compute_single_window_metrics(group, sample_tag)

    def existing_path_window_map(path_key: str, *, raw: bool = False) -> dict[str, tuple[str, TrackMetrics]]:
        tracks = existing_payload.get("tracks") if path_key == "path1" else (existing_payload.get(path_key) or {}).get("tracks")
        if not isinstance(tracks, dict):
            raise RuntimeError(f"No existing {path_key} tracks available for fallback.")
        id_key = "raw_winner" if raw else "winner"
        metrics_key = "raw_metrics" if raw else "metrics"
        result: dict[str, tuple[str, TrackMetrics]] = {}
        for track_key, sample_tag, _label in TRACK_SEQUENCE:
            meta = tracks.get(track_key)
            if not isinstance(meta, dict) or not meta.get(id_key) or not isinstance(meta.get(metrics_key), dict):
                raise RuntimeError(f"Existing {path_key} track {track_key} is missing {id_key}/{metrics_key}.")
            result[sample_tag] = (str(meta[id_key]), _metrics_from_track_payload(meta[metrics_key]))
        return result

    def existing_path_robust(path_key: str) -> tuple[str, dict[str, float]]:
        if path_key == "path1":
            robust = (existing_payload.get("tracks") or {}).get("robust_candidate")
        else:
            robust = existing_payload.get(path_key)
        if not isinstance(robust, dict):
            raise RuntimeError(f"No existing {path_key} robust candidate available for fallback.")
        strategy_id = robust.get("strategy_base_id")
        metrics = robust.get("robust_metrics")
        if not strategy_id or not isinstance(metrics, dict):
            raise RuntimeError(f"Existing {path_key} robust candidate is incomplete.")
        return str(strategy_id), dict(metrics)

    def existing_path_leaderboards(path_key: str) -> dict[str, list[dict[str, Any]]]:
        tracks = existing_payload.get("tracks") if path_key == "path1" else (existing_payload.get(path_key) or {}).get("tracks")
        if not isinstance(tracks, dict):
            return {}
        result: dict[str, list[dict[str, Any]]] = {}
        for track_key, sample_tag, _label in TRACK_SEQUENCE:
            leaderboard = (tracks.get(track_key) or {}).get("leaderboard")
            if isinstance(leaderboard, list) and leaderboard:
                result[sample_tag] = leaderboard
        return result

    def existing_robust_leaderboard(path_key: str) -> list[dict[str, Any]]:
        robust = (existing_payload.get("tracks") or {}).get("robust_candidate") if path_key == "path1" else existing_payload.get(path_key)
        if not isinstance(robust, dict):
            return []
        leaderboard = robust.get("leaderboard") if path_key == "path1" else robust.get("robust_leaderboard")
        return leaderboard if isinstance(leaderboard, list) else []

    def resolve_path1_winner(
        track_key: str,
        sample_tag: str,
        path1_incumbents: dict[str, str],
        log_prefix: str = "[path1]",
    ) -> tuple[str, TrackMetrics]:
        current_id = existing_path1_winners.get(track_key)
        current_id_str = str(current_id) if current_id else ""

        def build_ranked_candidates() -> list[tuple[str, TrackMetrics]]:
            candidates: list[tuple[str, TrackMetrics]] = []
            for base_id, group in path1_latest.groupby("strategy_base_id"):
                base_id_str = str(base_id)
                if base_id_str not in path1_family_ids or base_id_str not in active_family_ids:
                    continue
                tags = set(group["sample_tag"].astype(str))
                if sample_tag != "since_2025_01" and not set(WEIGHTED_WINDOW_TAGS).issubset(tags):
                    continue
                if sample_tag not in tags:
                    continue
                metrics = _compute_single_window_metrics(group, sample_tag)
                if _is_nan_metrics(metrics):
                    continue
                candidates.append((base_id_str, metrics))
            candidates.sort(
                key=lambda item: (item[1].cagr, item[1].sharpe, item[1].max_drawdown, -item[1].turnover),
                reverse=True,
            )
            return candidates

        ranked = build_ranked_candidates()
        if not ranked:
            raise RuntimeError(f"No winner-core strategies found for sample_tag={sample_tag!r}")

        def candidate_passes_validation(candidate_id: str) -> bool:
            if not enable_adjacent_validation:
                return True
            passes, detail = _passes_adjacent_window_check(
                candidate_id=candidate_id,
                target_window=sample_tag,
                by_id=path1_by_id,
                incumbent_winners=path1_incumbents,
            )
            if not passes:
                print(f"[validation]{log_prefix} rejected {candidate_id} for {sample_tag}: {_fmt_validation_detail(detail)}")
            return passes

        if not current_id_str or current_id_str not in path1_family_ids or current_id_str not in active_family_ids:
            for candidate_id, candidate_metrics in ranked:
                if candidate_passes_validation(candidate_id):
                    return candidate_id, candidate_metrics
            print(
                f"[validation]{log_prefix} no candidate passed for {sample_tag} and no incumbent fallback; "
                f"using top-ranked {ranked[0][0]}"
            )
            return ranked[0]

        current_metrics = metrics_for(current_id_str, sample_tag)
        if _is_nan_metrics(current_metrics):
            for candidate_id, candidate_metrics in ranked:
                if candidate_passes_validation(candidate_id):
                    return candidate_id, candidate_metrics
            print(
                f"[validation]{log_prefix} no candidate passed for {sample_tag} and incumbent has no metrics; "
                f"using top-ranked {ranked[0][0]}"
            )
            return ranked[0]

        for candidate_id, candidate_metrics in ranked:
            if not _is_clear_improvement(
                candidate=candidate_metrics,
                current=current_metrics,
                thresholds=PATH1_IMPROVEMENT_THRESHOLDS,
            ):
                continue
            if not candidate_passes_validation(candidate_id):
                continue
            return candidate_id, candidate_metrics

        return current_id_str, current_metrics

    def resolve_path1_winners_with_convergence(max_iterations: int = 3) -> dict[str, tuple[str, TrackMetrics]]:
        """Iterate Path 1 picking until winner assignments stabilize.

        Mirrors the convergence loop used for Path 2/3 so adjacent-window
        validation anchors are the freshly-resolved winners, not stale JSON
        values. Path 1 also has the improvement-stickiness check, so in
        practice convergence usually happens in one round; the loop is
        defense-in-depth against transient mismatch when a Path 1 winner
        does change.
        """
        track_specs = [
            ("since_2017_only", "since_2017_01"),
            ("since_2020_only", "since_2020_01"),
            ("since_2023_only", "since_2023_01"),
            ("since_2025_only", "since_2025_01"),
        ]
        incumbents = dict(existing_winners_all_paths.get("path1", {}))
        last_winners: dict[str, tuple[str, TrackMetrics]] = {}
        for iteration in range(max_iterations):
            iter_log_prefix = f"[path1][iter{iteration + 1}]" if enable_adjacent_validation else "[path1]"
            winners: dict[str, tuple[str, TrackMetrics]] = {}
            for track_key, sample_tag in track_specs:
                winners[sample_tag] = resolve_path1_winner(
                    track_key, sample_tag, incumbents, log_prefix=iter_log_prefix
                )
            if not enable_adjacent_validation:
                return winners
            new_id_map = {tag: winner[0] for tag, winner in winners.items()}
            if last_winners and {tag: w[0] for tag, w in last_winners.items()} == new_id_map:
                return last_winners
            incumbents = {WINDOW_TAG_TO_TRACK_KEY[tag]: winner[0] for tag, winner in winners.items()}
            last_winners = winners
        return last_winners

    if path1_available:
        path1_winners = resolve_path1_winners_with_convergence()
        path1_raw_winners = {
            tag: _pick_single_window_winner(path1_latest, tag, allowed_base_ids=path1_allowed_ids)
            for tag in ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01")
        }
        path1_robust_id, path1_summary = _pick_robust_candidate(
            path1_latest[path1_latest["strategy_base_id"].astype(str).isin(path1_allowed_ids)]
        )
    else:
        path1_winners = existing_path_window_map("path1")
        path1_raw_winners = existing_path_window_map("path1", raw=True)
        path1_robust_id, path1_summary = existing_path_robust("path1")
    window_2017_id, window_2017_metrics = path1_winners["since_2017_01"]
    window_2020_id, window_2020_metrics = path1_winners["since_2020_01"]
    window_2023_id, window_2023_metrics = path1_winners["since_2023_01"]
    window_2025_id, window_2025_metrics = path1_winners["since_2025_01"]

    if path2_available:
        path2_winners = _resolve_path_window_winners_with_convergence(
            latest=path2_latest,
            allowed_base_ids=path2_allowed_ids,
            by_id=path2_by_id,
            initial_incumbents=existing_winners_all_paths.get("path2", {}),
            enable_validation=enable_adjacent_validation,
            log_prefix="[path2]",
        )
        path2_raw_winners = {
            tag: _pick_single_window_winner(path2_latest, tag, allowed_base_ids=path2_allowed_ids)
            for tag in ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01")
        }
        path2_id, path2_summary = _pick_path2_candidate(
            path2_latest[path2_latest["strategy_base_id"].astype(str).isin(path2_allowed_ids)]
        )
    else:
        path2_winners = existing_path_window_map("path2")
        path2_raw_winners = existing_path_window_map("path2", raw=True)
        path2_id, path2_summary = existing_path_robust("path2")
    path2_window_2017_id, path2_window_2017_metrics = path2_winners["since_2017_01"]
    path2_window_2020_id, path2_window_2020_metrics = path2_winners["since_2020_01"]
    path2_window_2023_id, path2_window_2023_metrics = path2_winners["since_2023_01"]
    path2_window_2025_id, path2_window_2025_metrics = path2_winners["since_2025_01"]
    if path3_available:
        path3_winners = _resolve_path_window_winners_with_convergence(
            latest=path3_latest,
            allowed_base_ids=path3_allowed_ids,
            by_id=path3_by_id,
            initial_incumbents=existing_winners_all_paths.get("path3", {}),
            enable_validation=enable_adjacent_validation,
            log_prefix="[path3]",
        )
        path3_raw_winners = {
            tag: _pick_single_window_winner(path3_latest, tag, allowed_base_ids=path3_allowed_ids)
            for tag in ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01")
        }
        path3_id, path3_summary = _pick_robust_candidate(path3_latest, allowed_base_ids=path3_allowed_ids)
    else:
        path3_winners = existing_path_window_map("path3")
        path3_raw_winners = existing_path_window_map("path3", raw=True)
        path3_id, path3_summary = existing_path_robust("path3")
    path3_window_2017_id, path3_window_2017_metrics = path3_winners["since_2017_01"]
    path3_window_2020_id, path3_window_2020_metrics = path3_winners["since_2020_01"]
    path3_window_2023_id, path3_window_2023_metrics = path3_winners["since_2023_01"]
    path3_window_2025_id, path3_window_2025_metrics = path3_winners["since_2025_01"]
    raw_winners_by_path = {
        "path1": path1_raw_winners,
        "path2": path2_raw_winners,
        "path3": path3_raw_winners,
    }

    def _final_incumbents(path_winners_map: dict[str, tuple[str, TrackMetrics]]) -> dict[str, str]:
        return {
            WINDOW_TAG_TO_TRACK_KEY[tag]: winner_id
            for tag, (winner_id, _metrics) in path_winners_map.items()
            if tag in WINDOW_TAG_TO_TRACK_KEY
        }

    def _window_leaderboards_for(
        *,
        latest_for_path: pd.DataFrame,
        by_id_for_path: dict[str, pd.DataFrame],
        path_winners_map: dict[str, tuple[str, TrackMetrics]],
        raw_map: dict[str, tuple[str, TrackMetrics]],
        allowed_base_ids: set[str],
    ) -> dict[str, list[dict[str, Any]]]:
        incumbents = _final_incumbents(path_winners_map)
        return {
            tag: _build_single_window_leaderboard(
                latest_for_path,
                tag,
                allowed_base_ids=allowed_base_ids,
                by_id=by_id_for_path,
                incumbent_winners=incumbents,
                enable_validation=enable_adjacent_validation,
                official_winner_id=path_winners_map[tag][0],
                raw_winner_id=raw_map[tag][0],
                strategies=strategies,
            )
            for tag in ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01")
        }

    def _robust_leaderboard_for(latest_for_path: pd.DataFrame, allowed_base_ids: set[str], official_id: str) -> list[dict[str, Any]]:
        return [
            _leaderboard_entry(
                rank=rank,
                strategy_id=strategy_id,
                metrics=summary,
                strategies=strategies,
                official_winner_id=official_id,
            )
            for rank, (strategy_id, summary) in enumerate(
                _rank_robust_candidates(latest_for_path, allowed_base_ids=allowed_base_ids)[:TRACK_LEADERBOARD_LIMIT],
                start=1,
            )
        ]

    leaderboards_by_path = {
        "path1": (
            _window_leaderboards_for(
                latest_for_path=path1_latest,
                by_id_for_path=path1_by_id,
                path_winners_map=path1_winners,
                raw_map=path1_raw_winners,
                allowed_base_ids=path1_allowed_ids,
            )
            if path1_available
            else existing_path_leaderboards("path1")
        ),
        "path2": _window_leaderboards_for(
            latest_for_path=path2_latest,
            by_id_for_path=path2_by_id,
            path_winners_map=path2_winners,
            raw_map=path2_raw_winners,
            allowed_base_ids=path2_allowed_ids,
        ),
        "path3": (
            _window_leaderboards_for(
                latest_for_path=path3_latest,
                by_id_for_path=path3_by_id,
                path_winners_map=path3_winners,
                raw_map=path3_raw_winners,
                allowed_base_ids=path3_allowed_ids,
            )
            if path3_available
            else existing_path_leaderboards("path3")
        ),
    }
    robust_leaderboards_by_path = {
        "path1": (
            _robust_leaderboard_for(path1_latest, path1_allowed_ids, path1_robust_id)
            if path1_available
            else existing_robust_leaderboard("path1")
        ),
        "path2": _robust_leaderboard_for(path2_latest, path2_allowed_ids, path2_id),
        "path3": (
            _robust_leaderboard_for(path3_latest, path3_allowed_ids, path3_id)
            if path3_available
            else existing_robust_leaderboard("path3")
        ),
    }
    sample_end = max(info["sample_end"] for info in strategies.values())

    def _track_for(
        path_key: str,
        path_winners_map: dict[str, tuple[str, TrackMetrics]],
        raw_map: dict[str, tuple[str, TrackMetrics]],
        sample_tag: str,
        weights: dict[str, float],
    ) -> dict[str, object]:
        validated_id, validated_metrics = path_winners_map[sample_tag]
        raw_id, raw_metrics = raw_map[sample_tag]
        return _build_track_section(
            weights=weights,
            validated_winner_id=validated_id,
            validated_metrics=validated_metrics,
            raw_winner_id=raw_id,
            raw_metrics=raw_metrics,
            leaderboard=leaderboards_by_path.get(path_key, {}).get(sample_tag),
        )

    payload = {
        "as_of": sample_end,
        "window_tags": list(SAMPLE_TAG_STARTS),
        "winner_core_prefix": prefix,
        "tracks": {
            "since_2017_only": _track_for("path1", path1_winners, path1_raw_winners, "since_2017_01", WEIGHTS_2017_ONLY),
            "since_2023_only": _track_for("path1", path1_winners, path1_raw_winners, "since_2023_01", WEIGHTS_2023_ONLY),
            "since_2020_only": _track_for("path1", path1_winners, path1_raw_winners, "since_2020_01", WEIGHTS_2020_ONLY),
            "since_2025_only": _track_for("path1", path1_winners, path1_raw_winners, "since_2025_01", WEIGHTS_2025_ONLY),
            "robust_candidate": {
                "strategy_base_id": path1_robust_id,
                "robust_metrics": path1_summary,
                "leaderboard": robust_leaderboards_by_path["path1"],
            },
        },
        "path2": {
            "tracks": {
                "since_2017_only": _track_for("path2", path2_winners, path2_raw_winners, "since_2017_01", WEIGHTS_2017_ONLY),
                "since_2023_only": _track_for("path2", path2_winners, path2_raw_winners, "since_2023_01", WEIGHTS_2023_ONLY),
                "since_2020_only": _track_for("path2", path2_winners, path2_raw_winners, "since_2020_01", WEIGHTS_2020_ONLY),
                "since_2025_only": _track_for("path2", path2_winners, path2_raw_winners, "since_2025_01", WEIGHTS_2025_ONLY),
            },
            "strategy_base_id": path2_id,
            "robust_metrics": path2_summary,
            "robust_leaderboard": robust_leaderboards_by_path["path2"],
        },
        "path3": {
            "tracks": {
                "since_2017_only": _track_for("path3", path3_winners, path3_raw_winners, "since_2017_01", WEIGHTS_2017_ONLY),
                "since_2023_only": _track_for("path3", path3_winners, path3_raw_winners, "since_2023_01", WEIGHTS_2023_ONLY),
                "since_2020_only": _track_for("path3", path3_winners, path3_raw_winners, "since_2020_01", WEIGHTS_2020_ONLY),
                "since_2025_only": _track_for("path3", path3_winners, path3_raw_winners, "since_2025_01", WEIGHTS_2025_ONLY),
            },
            "strategy_base_id": path3_id,
            "robust_metrics": path3_summary,
            "robust_leaderboard": robust_leaderboards_by_path["path3"],
        },
        "strategies": {
            sid: {
                "strategy_base_name": info["strategy_base_name"],
                "windows": info["windows"],
            }
            for sid, info in strategies.items()
            if sid
            in (
                {
                    window_2017_id,
                    window_2023_id,
                    window_2020_id,
                    window_2025_id,
                    path1_robust_id,
                    path2_window_2017_id,
                    path2_window_2023_id,
                    path2_window_2020_id,
                    path2_window_2025_id,
                    path2_id,
                    path3_window_2017_id,
                    path3_window_2023_id,
                    path3_window_2020_id,
                    path3_window_2025_id,
                    path3_id,
                }
                | {raw_id for raw_map in raw_winners_by_path.values() for raw_id, _ in raw_map.values()}
            )
        },
    }
    args.write_json.parent.mkdir(parents=True, exist_ok=True)
    args.write_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    raw_winners_lookup = {
        (path_key, sample_tag): raw_entry
        for path_key, raw_map in raw_winners_by_path.items()
        for sample_tag, raw_entry in raw_map.items()
    }
    block = _render_block(
        strategies,
        window_2017_id,
        window_2017_metrics,
        window_2023_id,
        window_2023_metrics,
        window_2020_id,
        window_2020_metrics,
        window_2025_id,
        window_2025_metrics,
        path1_robust_id,
        path1_summary,
        path2_window_2017_id,
        path2_window_2017_metrics,
        path2_window_2023_id,
        path2_window_2023_metrics,
        path2_window_2020_id,
        path2_window_2020_metrics,
        path2_window_2025_id,
        path2_window_2025_metrics,
        path2_id,
        path2_summary,
        path3_window_2017_id,
        path3_window_2017_metrics,
        path3_window_2023_id,
        path3_window_2023_metrics,
        path3_window_2020_id,
        path3_window_2020_metrics,
        path3_window_2025_id,
        path3_window_2025_metrics,
        path3_id,
        path3_summary,
        sample_end,
        raw_winners_lookup=raw_winners_lookup,
    )
    update_readme(args.readme, block)
    path1_winners = {
        "since_2017_only": window_2017_id,
        "since_2020_only": window_2020_id,
        "since_2023_only": window_2023_id,
        "since_2025_only": window_2025_id,
    }
    path2_winners = {
        "since_2017_only": path2_window_2017_id,
        "since_2020_only": path2_window_2020_id,
        "since_2023_only": path2_window_2023_id,
        "since_2025_only": path2_window_2025_id,
    }
    path3_winners = {
        "since_2017_only": path3_window_2017_id,
        "since_2020_only": path3_window_2020_id,
        "since_2023_only": path3_window_2023_id,
        "since_2025_only": path3_window_2025_id,
    }
    update_history(
        history_path=args.history_json,
        markdown_path=args.history_md,
        as_of=sample_end,
        strategies=strategies,
        path1_winners=path1_winners,
        path2_winners=path2_winners,
        path3_winners=path3_winners,
        path1_robust_id=path1_robust_id,
        path2_robust_id=path2_id,
        path3_robust_id=path3_id,
        raw_winners_by_path=raw_winners_by_path,
    )
    core_active_backfill = backfill_core_active_registry_from_history(
        path=args.core_active_json,
        history_path=args.history_json,
        as_of=sample_end,
        max_size=args.core_active_max_size,
        stale_trading_days=args.core_active_stale_trading_days,
    )
    core_active_payload = update_core_active_registry(
        path=args.core_active_json,
        as_of=sample_end,
        winner_entries=_build_core_active_winner_entries(payload, strategies),
        max_size=args.core_active_max_size,
        stale_trading_days=args.core_active_stale_trading_days,
    )

    print(f"[OK] Updated {args.readme}")
    print(f"[OK] Wrote {args.write_json}")
    print(f"[OK] Wrote {args.history_json}")
    print(f"[OK] Wrote {args.history_md}")
    print(
        f"[OK] Backfilled core_active from winner history "
        f"({core_active_backfill['dates']} dates, "
        f"{core_active_backfill['strategies']} strategies, "
        f"{core_active_backfill['entries']} entries)"
    )
    print(
        f"[OK] Wrote {args.core_active_json} "
        f"({len(core_active_payload['strategies'])}/{core_active_payload['max_size']} active, "
        f"{len(core_active_payload.get('refresh_only_strategies', []))} refresh-only)"
    )
    print(f"[OK] 2017-window winner: {window_2017_id} (CAGR={_fmt_pct(window_2017_metrics.cagr)}, Sharpe={window_2017_metrics.sharpe:.4f})")
    print(f"[OK] 2023-window winner: {window_2023_id} (CAGR={_fmt_pct(window_2023_metrics.cagr)}, Sharpe={window_2023_metrics.sharpe:.4f})")
    print(f"[OK] 2020-window winner: {window_2020_id} (CAGR={_fmt_pct(window_2020_metrics.cagr)}, Sharpe={window_2020_metrics.sharpe:.4f})")
    print(f"[OK] 2025-window winner: {window_2025_id} (CAGR={_fmt_pct(window_2025_metrics.cagr)}, Sharpe={window_2025_metrics.sharpe:.4f})")
    print(f"[OK] Path 1 candidate:   {path1_robust_id} (meanCAGR={_fmt_pct(path1_summary['cagr_mean'])}, minCAGR={_fmt_pct(path1_summary['cagr_min'])})")
    print(f"[OK] Path2 2017-window winner: {path2_window_2017_id} (CAGR={_fmt_pct(path2_window_2017_metrics.cagr)}, Sharpe={path2_window_2017_metrics.sharpe:.4f})")
    print(f"[OK] Path2 2023-window winner: {path2_window_2023_id} (CAGR={_fmt_pct(path2_window_2023_metrics.cagr)}, Sharpe={path2_window_2023_metrics.sharpe:.4f})")
    print(f"[OK] Path2 2020-window winner: {path2_window_2020_id} (CAGR={_fmt_pct(path2_window_2020_metrics.cagr)}, Sharpe={path2_window_2020_metrics.sharpe:.4f})")
    print(f"[OK] Path2 2025-window winner: {path2_window_2025_id} (CAGR={_fmt_pct(path2_window_2025_metrics.cagr)}, Sharpe={path2_window_2025_metrics.sharpe:.4f})")
    print(f"[OK] Path 2 candidate:   {path2_id} (meanCAGR={_fmt_pct(path2_summary['cagr_mean'])}, minCAGR={_fmt_pct(path2_summary['cagr_min'])})")
    print(f"[OK] Path3 2017-window winner: {path3_window_2017_id} (CAGR={_fmt_pct(path3_window_2017_metrics.cagr)}, Sharpe={path3_window_2017_metrics.sharpe:.4f})")
    print(f"[OK] Path3 2023-window winner: {path3_window_2023_id} (CAGR={_fmt_pct(path3_window_2023_metrics.cagr)}, Sharpe={path3_window_2023_metrics.sharpe:.4f})")
    print(f"[OK] Path3 2020-window winner: {path3_window_2020_id} (CAGR={_fmt_pct(path3_window_2020_metrics.cagr)}, Sharpe={path3_window_2020_metrics.sharpe:.4f})")
    print(f"[OK] Path3 2025-window winner: {path3_window_2025_id} (CAGR={_fmt_pct(path3_window_2025_metrics.cagr)}, Sharpe={path3_window_2025_metrics.sharpe:.4f})")
    print(f"[OK] Path 3 candidate:   {path3_id} (meanCAGR={_fmt_pct(path3_summary['cagr_mean'])}, minCAGR={_fmt_pct(path3_summary['cagr_min'])})")


if __name__ == "__main__":
    main()
