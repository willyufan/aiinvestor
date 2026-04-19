from __future__ import annotations

import argparse
import ast
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
DEFAULT_COMPARISON_CSV = RESULTS_DIR / "strategy_comparison_base_method.csv"
README_PATH = ROOT / "README.md"
BACKTEST_SCRIPT_PATH = ROOT / "backtest_marketcap_etf.py"
TRACKED_HISTORY_JSON_PATH = RESULTS_DIR / "tracked_winner_history.json"
TRACKED_HISTORY_MD_PATH = ROOT / "HISTORY.md"

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


def _parse_python_constants(path: Path, names: Iterable[str]) -> dict[str, Any]:
    wanted = set(names)
    result: dict[str, Any] = {}
    node = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for stmt in node.body:
        if not isinstance(stmt, ast.Assign):
            continue
        if len(stmt.targets) != 1 or not isinstance(stmt.targets[0], ast.Name):
            continue
        target = stmt.targets[0].id
        if target not in wanted:
            continue
        result[target] = ast.literal_eval(stmt.value)
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
    winner_ids = load_winner_core_family_ids(backtest_path)
    try:
        consts = _parse_python_constants(
            backtest_path,
            ["SAT_WEEKLY_RISK_SUFFIX", "SAT_THREE_STAGE_SUFFIX", "SAT_THREE_STAGE_BUFFERED_SUFFIX"],
        )
        overlay_suffixes = [
            str(consts.get("SAT_WEEKLY_RISK_SUFFIX") or "__sat_weekly_risk"),
            str(consts.get("SAT_THREE_STAGE_SUFFIX") or "__sat_three_stage_risk"),
            str(consts.get("SAT_THREE_STAGE_BUFFERED_SUFFIX") or "__sat_three_stage_buffered"),
        ]
    except Exception:
        overlay_suffixes = ["__sat_weekly_risk", "__sat_three_stage_risk", "__sat_three_stage_buffered"]
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
    candidates.sort(key=lambda item: (item[1].cagr, item[1].sharpe, item[1].max_drawdown, -item[1].turnover), reverse=True)
    return candidates[0]


def _pick_single_window_winner(
    latest: pd.DataFrame,
    sample_tag: str,
    *,
    allowed_base_ids: set[str] | None = None,
) -> tuple[str, TrackMetrics]:
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
        if any(np.isnan(v) for v in (metrics.cagr, metrics.sharpe, metrics.max_drawdown, metrics.turnover)):
            continue
        candidates.append((str(base_id), metrics))

    if not candidates:
        raise RuntimeError(f"No strategies have {sample_tag} window to compute the single-window winner.")

    candidates.sort(key=lambda item: (item[1].cagr, item[1].sharpe, item[1].max_drawdown, -item[1].turnover), reverse=True)
    return candidates[0]


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
        return {"path1": {}, "path2": {}}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"path1": {}, "path2": {}}
    if not isinstance(payload, dict):
        return {"path1": {}, "path2": {}}
    payload.setdefault("path1", {})
    payload.setdefault("path2", {})
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


def _build_history_entry(*, as_of: str, winner_id: str, strategy_name: str, sample_tag: str, metrics: dict[str, float]) -> dict[str, Any]:
    return {
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


def _history_entry_changed(old_entry: dict[str, Any], new_entry: dict[str, Any]) -> bool:
    if not old_entry:
        return True
    if str(old_entry.get("winner", "")) != str(new_entry.get("winner", "")):
        return True
    if str(old_entry.get("strategy_base_name", "")) != str(new_entry.get("strategy_base_name", "")):
        return True
    for key in ("total_return", "cagr", "max_drawdown", "sharpe", "turnover"):
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
        "这个文档记录两条研究路径在四个窗口下的赢家变化历史。",
        "仅当赢家策略或关键指标发生变化时，才会追加新记录。",
        "",
    ]
    path_titles = {
        "path1": "Path 1：渐进优化路径",
        "path2": "Path 2：无约束上限探索",
    }
    for path_key in ("path1", "path2"):
        lines.extend([f"## {path_titles[path_key]}", ""])
        path_bucket = history.get(path_key, {})
        for track_key, _, track_label in TRACK_SEQUENCE:
            lines.extend([f"### {track_label}", ""])
            entries = list(path_bucket.get(track_key, []))
            if not entries:
                lines.extend(["暂无记录。", ""])
                continue
            lines.append("| 日期 | 策略ID | 策略名称 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |")
            lines.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
            for entry in reversed(entries):
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
    path1_robust_id: str | None = None,
    path2_robust_id: str | None = None,
) -> dict[str, Any]:
    history = _load_history(history_path)
    for path_key, winners in (("path1", path1_winners), ("path2", path2_winners)):
        path_bucket = history.setdefault(path_key, {})
        for track_key, sample_tag, _ in TRACK_SEQUENCE:
            winner_id = winners.get(track_key, "")
            if not winner_id or winner_id not in strategies:
                continue
            strategy_name = str(strategies[winner_id]["strategy_base_name"])
            metrics = _window_metrics_for_strategy(strategies, winner_id, sample_tag)
            new_entry = _build_history_entry(
                as_of=as_of,
                winner_id=winner_id,
                strategy_name=strategy_name,
                sample_tag=sample_tag,
                metrics=metrics,
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
    for path_key, robust_id in (("path1", path1_robust_id), ("path2", path2_robust_id)):
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


def _compute_window_metrics(equity: pd.DataFrame, monthly_returns: pd.DataFrame, turnover: pd.DataFrame) -> dict[str, float]:
    nav = equity["nav"].astype(float)
    monthly_net = monthly_returns["net_return"].astype(float)
    total_return = float(nav.iloc[-1] - 1.0)
    periods = len(monthly_net)
    years = periods / 12.0 if periods > 0 else np.nan
    cagr = float(nav.iloc[-1] ** (1 / years) - 1) if periods > 0 and nav.iloc[-1] > 0 else np.nan
    max_drawdown = float(equity["drawdown"].min())
    annual_volatility = float(monthly_net.std(ddof=1) * np.sqrt(12)) if periods > 1 else np.nan
    sharpe_ratio = (
        float((monthly_net.mean() / monthly_net.std(ddof=1)) * np.sqrt(12))
        if periods > 1 and monthly_net.std(ddof=1) > 0
        else np.nan
    )
    average_annual_turnover = float(turnover["one_way_turnover"].mean() * 12) if not turnover.empty else np.nan
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
        candidate_dirs = [RESULTS_DIR / base_id]
    elif sample_tag == "since_2025_01":
        # since_2025 is a dedicated tracked window in this project: prefer its dedicated run.
        candidate_dirs = [RESULTS_DIR / f"{base_id}__since_2025_01"]
    elif sample_tag == "since_2026_01":
        # since_2026 is a display-only YTD window: derive from the shortest available recent run first.
        candidate_dirs = [
            RESULTS_DIR / f"{base_id}__since_2025_01",
            RESULTS_DIR / f"{base_id}__since_2023_01",
            RESULTS_DIR / f"{base_id}__since_2020_01",
            RESULTS_DIR / f"{base_id}__since_2017_01",
        ]
    else:
        # Prefer a dedicated run for the requested window when available.
        preferred = RESULTS_DIR / f"{base_id}__{sample_tag}"
        fallbacks = [
            RESULTS_DIR / f"{base_id}__since_2025_01",
            RESULTS_DIR / f"{base_id}__since_2023_01",
            RESULTS_DIR / f"{base_id}__since_2020_01",
            RESULTS_DIR / f"{base_id}__since_2017_01",
        ]
        candidate_dirs = [preferred] + [path for path in fallbacks if path != preferred]

    for result_dir in candidate_dirs:
        equity_path = result_dir / "equity_curve.csv"
        monthly_path = result_dir / "monthly_returns.csv"
        turnover_path = result_dir / "turnover.csv"
        if not (equity_path.exists() and monthly_path.exists() and turnover_path.exists()):
            continue
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
        return _compute_window_metrics(equity_window, monthly_window, turnover_window)
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
                    "sample_end": sample_end_map.get(base_id, pd.Timestamp.today().normalize()),
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

    candidates.sort(
        key=lambda item: (
            item[1]["cagr_mean"],
            item[1]["cagr_min"],
            item[1]["sharpe_mean"],
            item[1]["max_drawdown_worst"],
            -item[1]["turnover_mean"],
        ),
        reverse=True,
    )
    return candidates[0]


def _pick_robust_candidate(latest: pd.DataFrame, *, allowed_base_ids: set[str] | None = None) -> tuple[str, dict[str, float]]:
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
    if not candidates:
        raise RuntimeError("No strategies have all four windows to compute robust candidate.")
    candidates.sort(
        key=lambda item: (
            item[1]["cagr_mean"],
            item[1]["cagr_min"],
            item[1]["sharpe_mean"],
            item[1]["max_drawdown_worst"],
            -item[1]["turnover_mean"],
        ),
        reverse=True,
    )
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
    sample_end: str,
) -> str:
    def render_track(title: str, weights: dict[str, float], winner_id: str, metrics: TrackMetrics) -> str:
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
        return "\n".join(
            [
                f"### {title}",
                "",
                f"- 策略：`{winner_id}`（{info['strategy_base_name']}）",
                f"- 加权指标（CAGR / Sharpe / Max DD / Turnover）："
                f"`{_fmt_pct(metrics.cagr)}` / `{metrics.sharpe:.4f}` / `{_fmt_pct(metrics.max_drawdown)}` / `{metrics.turnover:.2f}`",
                "",
                f"窗口指标（截至 `{sample_end}`，权重：{weight_str}）：",
                "",
                render_window("since_2017_01"),
                render_window("since_2020_01"),
                render_window("since_2023_01"),
                render_window("since_2025_01"),
                render_window("since_2026_01"),
                "",
            ]
        )

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
        "项目当前维护 **两条研究路线**：",
        "",
        "- **Path 1（胜出者核心主线）**：渐进优化路线，目标是在保持当前 winner-core 框架可交易、可控回撤的前提下，把长期 CAGR 持续推向 `25%~30%+`。",
        "- **Path 2（无约束上限探索）**：追求更高收益上限的独立路线，可以脱离当前框架自由试验；近期重点是优先把 `2020` 与 `2023` 两个窗口推向 `40%+ CAGR`。Path 2 会独立记录自己的窗口赢家与鲁棒候选，不需要先超过 Path 1 才更新。",
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
        render_track("2017 窗口赢家", WEIGHTS_2017_ONLY, window_2017_winner_id, window_2017_metrics),
        render_track("2023 窗口赢家", WEIGHTS_2023_ONLY, window_2023_winner_id, window_2023_metrics),
        render_track("2020 窗口赢家", WEIGHTS_2020_ONLY, window_2020_winner_id, window_2020_metrics),
        render_track("2025 窗口赢家", WEIGHTS_2025_ONLY, window_2025_winner_id, window_2025_metrics),
        "## Path 1：鲁棒候选",
        "",
        render_path2("四窗口鲁棒候选", path1_robust_id, path1_summary),
        "## Path 2：窗口跟踪赢家",
        "",
        render_track("2017 窗口赢家（Path 2）", WEIGHTS_2017_ONLY, path2_window_2017_id, path2_window_2017_metrics),
        render_track("2023 窗口赢家（Path 2）", WEIGHTS_2023_ONLY, path2_window_2023_id, path2_window_2023_metrics),
        render_track("2020 窗口赢家（Path 2）", WEIGHTS_2020_ONLY, path2_window_2020_id, path2_window_2020_metrics),
        render_track("2025 窗口赢家（Path 2）", WEIGHTS_2025_ONLY, path2_window_2025_id, path2_window_2025_metrics),
        "## Path 2：鲁棒候选",
        "",
        render_path2("四窗口鲁棒候选", path2_id, path2_summary),
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
    parser.add_argument("--write-json", type=Path, default=RESULTS_DIR / "weighted_track_winners.json")
    parser.add_argument("--history-json", type=Path, default=TRACKED_HISTORY_JSON_PATH)
    parser.add_argument("--history-md", type=Path, default=TRACKED_HISTORY_MD_PATH)
    args = parser.parse_args()

    frame = pd.read_csv(args.comparison_csv)
    latest = _augment_with_synthetic_windows(_latest_per_strategy_window(frame))
    strategies = _build_strategy_map(latest)
    if not strategies:
        raise RuntimeError("No strategies with complete 2017/2020/2023 windows found in comparison CSV.")

    prefix = load_winner_core_prefix()
    path1_family_ids = load_path1_family_ids()
    active_family_ids = load_active_family_ids()
    if not path1_family_ids:
        raise RuntimeError(f"No winner-core strategies found with prefix={prefix!r}")

    existing_path1_winners = _load_existing_path1_winners(args.write_json)
    by_id: dict[str, pd.DataFrame] = {str(base_id): group for base_id, group in latest.groupby("strategy_base_id")}

    def metrics_for(base_id: str, sample_tag: str) -> TrackMetrics:
        group = by_id.get(str(base_id), pd.DataFrame())
        if group.empty or "sample_tag" not in group.columns:
            return TrackMetrics(cagr=float("nan"), sharpe=float("nan"), max_drawdown=float("nan"), turnover=float("nan"))
        return _compute_single_window_metrics(group, sample_tag)

    def resolve_path1_winner(track_key: str, sample_tag: str) -> tuple[str, TrackMetrics]:
        current_id = existing_path1_winners.get(track_key)
        current_id_str = str(current_id) if current_id else ""

        def build_ranked_candidates() -> list[tuple[str, TrackMetrics]]:
            candidates: list[tuple[str, TrackMetrics]] = []
            for base_id, group in latest.groupby("strategy_base_id"):
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

        if not current_id_str or current_id_str not in path1_family_ids or current_id_str not in active_family_ids:
            return ranked[0]

        current_metrics = metrics_for(current_id_str, sample_tag)
        if _is_nan_metrics(current_metrics):
            return ranked[0]

        for candidate_id, candidate_metrics in ranked:
            if _is_clear_improvement(
                candidate=candidate_metrics,
                current=current_metrics,
                thresholds=PATH1_IMPROVEMENT_THRESHOLDS,
            ):
                return candidate_id, candidate_metrics

        return current_id_str, current_metrics

    window_2017_id, window_2017_metrics = resolve_path1_winner("since_2017_only", "since_2017_01")
    window_2023_id, window_2023_metrics = resolve_path1_winner("since_2023_only", "since_2023_01")
    window_2020_id, window_2020_metrics = resolve_path1_winner("since_2020_only", "since_2020_01")
    window_2025_id, window_2025_metrics = resolve_path1_winner("since_2025_only", "since_2025_01")
    path1_robust_id, path1_summary = _pick_robust_candidate(
        latest[latest["strategy_base_id"].astype(str).isin(path1_family_ids & active_family_ids)]
    )
    path2_prefixes, path2_variant_ids = load_path2_scan_rules()
    path2_allowed_ids = {
        str(base_id)
        for base_id in set(latest["strategy_base_id"].astype(str).unique())
        if _matches_path2(str(base_id), path2_prefixes, path2_variant_ids)
    } - STATIC_BASE_IDS
    if not path2_allowed_ids:
        raise RuntimeError(
            "Path 2 candidate universe is empty. "
            "Check PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS in backtest_marketcap_etf.py."
        )
    path2_window_2017_id, path2_window_2017_metrics = _pick_single_window_winner(
        latest, "since_2017_01", allowed_base_ids=path2_allowed_ids
    )
    path2_window_2023_id, path2_window_2023_metrics = _pick_single_window_winner(
        latest, "since_2023_01", allowed_base_ids=path2_allowed_ids
    )
    path2_window_2020_id, path2_window_2020_metrics = _pick_single_window_winner(
        latest, "since_2020_01", allowed_base_ids=path2_allowed_ids
    )
    path2_window_2025_id, path2_window_2025_metrics = _pick_single_window_winner(
        latest, "since_2025_01", allowed_base_ids=path2_allowed_ids
    )
    path2_id, path2_summary = _pick_path2_candidate(
        latest[latest["strategy_base_id"].astype(str).isin(path2_allowed_ids)]
    )
    sample_end = max(info["sample_end"] for info in strategies.values())

    payload = {
        "as_of": sample_end,
        "window_tags": list(SAMPLE_TAG_STARTS),
        "winner_core_prefix": prefix,
        "tracks": {
            "since_2017_only": {
                "weights": WEIGHTS_2017_ONLY,
                "winner": window_2017_id,
                "metrics": {
                    "weighted_cagr": window_2017_metrics.cagr,
                    "weighted_sharpe": window_2017_metrics.sharpe,
                    "weighted_max_drawdown": window_2017_metrics.max_drawdown,
                    "weighted_turnover": window_2017_metrics.turnover,
                },
            },
            "since_2023_only": {
                "weights": WEIGHTS_2023_ONLY,
                "winner": window_2023_id,
                "metrics": {
                    "weighted_cagr": window_2023_metrics.cagr,
                    "weighted_sharpe": window_2023_metrics.sharpe,
                    "weighted_max_drawdown": window_2023_metrics.max_drawdown,
                    "weighted_turnover": window_2023_metrics.turnover,
                },
            },
            "since_2020_only": {
                "weights": WEIGHTS_2020_ONLY,
                "winner": window_2020_id,
                "metrics": {
                    "weighted_cagr": window_2020_metrics.cagr,
                    "weighted_sharpe": window_2020_metrics.sharpe,
                    "weighted_max_drawdown": window_2020_metrics.max_drawdown,
                    "weighted_turnover": window_2020_metrics.turnover,
                },
            },
            "since_2025_only": {
                "weights": WEIGHTS_2025_ONLY,
                "winner": window_2025_id,
                "metrics": {
                    "weighted_cagr": window_2025_metrics.cagr,
                    "weighted_sharpe": window_2025_metrics.sharpe,
                    "weighted_max_drawdown": window_2025_metrics.max_drawdown,
                    "weighted_turnover": window_2025_metrics.turnover,
                },
            },
            "robust_candidate": {
                "strategy_base_id": path1_robust_id,
                "robust_metrics": path1_summary,
            },
        },
        "path2": {
            "tracks": {
                "since_2017_only": {
                    "weights": WEIGHTS_2017_ONLY,
                    "winner": path2_window_2017_id,
                    "metrics": {
                        "weighted_cagr": path2_window_2017_metrics.cagr,
                        "weighted_sharpe": path2_window_2017_metrics.sharpe,
                        "weighted_max_drawdown": path2_window_2017_metrics.max_drawdown,
                        "weighted_turnover": path2_window_2017_metrics.turnover,
                    },
                },
                "since_2023_only": {
                    "weights": WEIGHTS_2023_ONLY,
                    "winner": path2_window_2023_id,
                    "metrics": {
                        "weighted_cagr": path2_window_2023_metrics.cagr,
                        "weighted_sharpe": path2_window_2023_metrics.sharpe,
                        "weighted_max_drawdown": path2_window_2023_metrics.max_drawdown,
                        "weighted_turnover": path2_window_2023_metrics.turnover,
                    },
                },
                "since_2020_only": {
                    "weights": WEIGHTS_2020_ONLY,
                    "winner": path2_window_2020_id,
                    "metrics": {
                        "weighted_cagr": path2_window_2020_metrics.cagr,
                        "weighted_sharpe": path2_window_2020_metrics.sharpe,
                        "weighted_max_drawdown": path2_window_2020_metrics.max_drawdown,
                        "weighted_turnover": path2_window_2020_metrics.turnover,
                    },
                },
                "since_2025_only": {
                    "weights": WEIGHTS_2025_ONLY,
                    "winner": path2_window_2025_id,
                    "metrics": {
                        "weighted_cagr": path2_window_2025_metrics.cagr,
                        "weighted_sharpe": path2_window_2025_metrics.sharpe,
                        "weighted_max_drawdown": path2_window_2025_metrics.max_drawdown,
                        "weighted_turnover": path2_window_2025_metrics.turnover,
                    },
                },
            },
            "strategy_base_id": path2_id,
            "robust_metrics": path2_summary,
        },
        "strategies": {
            sid: {
                "strategy_base_name": info["strategy_base_name"],
                "windows": info["windows"],
            }
            for sid, info in strategies.items()
            if sid
            in {
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
            }
        },
    }
    args.write_json.parent.mkdir(parents=True, exist_ok=True)
    args.write_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

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
        sample_end,
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
    update_history(
        history_path=args.history_json,
        markdown_path=args.history_md,
        as_of=sample_end,
        strategies=strategies,
        path1_winners=path1_winners,
        path2_winners=path2_winners,
        path1_robust_id=path1_robust_id,
        path2_robust_id=path2_id,
    )

    print(f"[OK] Updated {args.readme}")
    print(f"[OK] Wrote {args.write_json}")
    print(f"[OK] Wrote {args.history_json}")
    print(f"[OK] Wrote {args.history_md}")
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


if __name__ == "__main__":
    main()
