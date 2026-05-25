from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

import numpy as np
import pandas as pd

from scripts.results_layout import A_SHARE_SCOPE, candidate_strategy_result_dirs


@dataclass(frozen=True)
class ConcentrationStats:
    sample_tag: str
    avg_top1_weight: float
    avg_top3_weight: float
    max_top1_weight: float
    max_top3_weight: float
    latest_top1_weight: float
    latest_top3_weight: float
    observations: int


DEFAULT_CONCENTRATION_STATS = ConcentrationStats(
    sample_tag="",
    avg_top1_weight=0.0,
    avg_top3_weight=0.0,
    max_top1_weight=0.0,
    max_top3_weight=0.0,
    latest_top1_weight=0.0,
    latest_top3_weight=0.0,
    observations=0,
)

PROMOTION_SCORE_POLICY: dict[str, float | str] = {
    "version": "promotion_score_v1",
    "cagr_weight": 1.00,
    "sharpe_weight": 0.06,
    "max_drawdown_weight": 0.28,
    "turnover_penalty_weight": 0.012,
    "ytd_negative_cagr_penalty_weight": 0.75,
    "ytd_drawdown_penalty_weight": 0.35,
    "ytd_drawdown_penalty_floor": 0.12,
    "top1_weight_threshold": 0.35,
    "top3_weight_threshold": 0.62,
    "top1_concentration_penalty_weight": 0.22,
    "top3_concentration_penalty_weight": 0.36,
}

ROBUST_SCORE_POLICY: dict[str, float | str] = {
    **PROMOTION_SCORE_POLICY,
    "version": "robust_score_v1",
    "cagr_min_weight": 1.20,
    "cagr_mean_weight": 0.55,
    "sharpe_mean_weight": 0.06,
    "max_drawdown_worst_weight": 0.32,
    "turnover_mean_penalty_weight": 0.010,
}


def _safe_float(value: object, default: float = 0.0) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return default
    if np.isnan(result):
        return default
    return result


def _first_existing_weights_history(strategy_id: str, sample_tag: str) -> Path | None:
    for result_dir in candidate_strategy_result_dirs(strategy_id, sample_tag, market_scope=A_SHARE_SCOPE):
        path = result_dir / "weights_history.csv"
        if path.exists():
            return path
    return None


@lru_cache(maxsize=8192)
def load_concentration_stats(
    strategy_id: str,
    preferred_sample_tag: str = "since_2026_01",
) -> ConcentrationStats:
    """Compute simple concentration diagnostics from cached weights history.

    We prefer the 2026 observation window because the current problem is
    recent-return fragility and single-name concentration. If that cache is
    unavailable, fall back to progressively longer windows.
    """
    for sample_tag in (preferred_sample_tag, "since_2025_01", "since_2023_01", "since_2020_01", "since_2017_01"):
        path = _first_existing_weights_history(strategy_id, sample_tag)
        if path is None:
            continue
        try:
            frame = pd.read_csv(path, usecols=["date", "weight"])
        except Exception:
            continue
        if frame.empty or "date" not in frame.columns or "weight" not in frame.columns:
            continue
        frame["weight"] = pd.to_numeric(frame["weight"], errors="coerce").fillna(0.0)
        grouped_top = (
            frame.sort_values(["date", "weight"], ascending=[True, False])
            .groupby("date")["weight"]
            .apply(lambda values: list(values.head(3)))
        )
        if grouped_top.empty:
            continue
        top1_values: list[float] = []
        top3_values: list[float] = []
        for values in grouped_top:
            top1_values.append(float(values[0]) if values else 0.0)
            top3_values.append(float(sum(values[:3])))
        latest_values = grouped_top.iloc[-1]
        return ConcentrationStats(
            sample_tag=sample_tag,
            avg_top1_weight=float(np.mean(top1_values)),
            avg_top3_weight=float(np.mean(top3_values)),
            max_top1_weight=float(np.max(top1_values)),
            max_top3_weight=float(np.max(top3_values)),
            latest_top1_weight=float(latest_values[0]) if latest_values else 0.0,
            latest_top3_weight=float(sum(latest_values[:3])),
            observations=int(len(top1_values)),
        )
    return DEFAULT_CONCENTRATION_STATS


def concentration_to_dict(stats: ConcentrationStats) -> dict[str, Any]:
    return {
        "sample_tag": stats.sample_tag,
        "avg_top1_weight": stats.avg_top1_weight,
        "avg_top3_weight": stats.avg_top3_weight,
        "max_top1_weight": stats.max_top1_weight,
        "max_top3_weight": stats.max_top3_weight,
        "latest_top1_weight": stats.latest_top1_weight,
        "latest_top3_weight": stats.latest_top3_weight,
        "observations": stats.observations,
    }


def _ytd_penalty(ytd_metrics: Mapping[str, object] | None, policy: Mapping[str, object]) -> float:
    if not ytd_metrics:
        return 0.0
    ytd_cagr = _safe_float(ytd_metrics.get("cagr"))
    ytd_max_drawdown = _safe_float(ytd_metrics.get("max_drawdown"))
    negative_cagr_penalty = max(0.0, -ytd_cagr) * _safe_float(policy.get("ytd_negative_cagr_penalty_weight"))
    drawdown_floor = _safe_float(policy.get("ytd_drawdown_penalty_floor"))
    drawdown_penalty = max(0.0, abs(ytd_max_drawdown) - drawdown_floor) * _safe_float(
        policy.get("ytd_drawdown_penalty_weight")
    )
    return negative_cagr_penalty + drawdown_penalty


def _concentration_penalty(stats: ConcentrationStats, policy: Mapping[str, object]) -> float:
    if stats.observations <= 0:
        return 0.0
    top1_excess = max(0.0, stats.latest_top1_weight - _safe_float(policy.get("top1_weight_threshold")))
    top3_excess = max(0.0, stats.avg_top3_weight - _safe_float(policy.get("top3_weight_threshold")))
    return (
        top1_excess * _safe_float(policy.get("top1_concentration_penalty_weight"))
        + top3_excess * _safe_float(policy.get("top3_concentration_penalty_weight"))
    )


def score_single_window_candidate(
    *,
    metrics: Mapping[str, object],
    strategy_id: str,
    ytd_metrics: Mapping[str, object] | None = None,
    policy: Mapping[str, object] = PROMOTION_SCORE_POLICY,
) -> dict[str, Any]:
    concentration = load_concentration_stats(strategy_id)
    base_score = (
        _safe_float(metrics.get("cagr")) * _safe_float(policy.get("cagr_weight"))
        + _safe_float(metrics.get("sharpe")) * _safe_float(policy.get("sharpe_weight"))
        + _safe_float(metrics.get("max_drawdown")) * _safe_float(policy.get("max_drawdown_weight"))
        - _safe_float(metrics.get("turnover")) * _safe_float(policy.get("turnover_penalty_weight"))
    )
    ytd_penalty = _ytd_penalty(ytd_metrics, policy)
    concentration_penalty = _concentration_penalty(concentration, policy)
    score = base_score - ytd_penalty - concentration_penalty
    return {
        "policy": str(policy.get("version") or "promotion_score"),
        "score": float(score),
        "base_score": float(base_score),
        "ytd_penalty": float(ytd_penalty),
        "concentration_penalty": float(concentration_penalty),
        "concentration": concentration_to_dict(concentration),
    }


def score_robust_candidate(
    *,
    summary: Mapping[str, object],
    strategy_id: str,
    ytd_metrics: Mapping[str, object] | None = None,
    policy: Mapping[str, object] = ROBUST_SCORE_POLICY,
) -> dict[str, Any]:
    concentration = load_concentration_stats(strategy_id)
    base_score = (
        _safe_float(summary.get("cagr_min")) * _safe_float(policy.get("cagr_min_weight"))
        + _safe_float(summary.get("cagr_mean")) * _safe_float(policy.get("cagr_mean_weight"))
        + _safe_float(summary.get("sharpe_mean")) * _safe_float(policy.get("sharpe_mean_weight"))
        + _safe_float(summary.get("max_drawdown_worst")) * _safe_float(policy.get("max_drawdown_worst_weight"))
        - _safe_float(summary.get("turnover_mean")) * _safe_float(policy.get("turnover_mean_penalty_weight"))
    )
    ytd_penalty = _ytd_penalty(ytd_metrics, policy)
    concentration_penalty = _concentration_penalty(concentration, policy)
    score = base_score - ytd_penalty - concentration_penalty
    return {
        "policy": str(policy.get("version") or "robust_score"),
        "score": float(score),
        "base_score": float(base_score),
        "ytd_penalty": float(ytd_penalty),
        "concentration_penalty": float(concentration_penalty),
        "concentration": concentration_to_dict(concentration),
    }
