from __future__ import annotations

import argparse
import ast
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd

from update_weighted_winners import _augment_with_synthetic_windows


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
DEFAULT_COMPARISON_CSV = RESULTS_DIR / "strategy_comparison_base_method.csv"
DEFAULT_TRACKED_WINNERS_JSON = RESULTS_DIR / "weighted_track_winners.json"

WEIGHTED_WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01")

WEIGHTS_2017_ONLY = {"since_2017_01": 1.00}
WEIGHTS_2023_ONLY = {"since_2023_01": 1.00}


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


def _compute_weighted_metrics(group: pd.DataFrame, weights: dict[str, float]) -> TrackMetrics:
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


def _is_nan_metrics(metrics: TrackMetrics) -> bool:
    return any(np.isnan(v) for v in (metrics.cagr, metrics.sharpe, metrics.max_drawdown, metrics.turnover))


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


def load_winner_core_family_ids(backtest_path: Path) -> list[str]:
    consts = _parse_python_constants(
        backtest_path,
        ["WINNER_ONLY_STRATEGY_ID", "WINNER_CORE_VARIANTS", "PATH1_FAST_PASS_VARIANT_IDS"],
    )
    base = str(consts["WINNER_ONLY_STRATEGY_ID"])
    variants = consts["WINNER_CORE_VARIANTS"]
    fast_pass_variant_ids = set(map(str, consts.get("PATH1_FAST_PASS_VARIANT_IDS") or []))
    if not isinstance(variants, list):
        raise TypeError("WINNER_CORE_VARIANTS is not a list")
    base_ids = [base]
    for variant in variants:
        if not isinstance(variant, dict) or "variant_id" not in variant:
            raise TypeError("WINNER_CORE_VARIANTS item missing variant_id")
        variant_id = str(variant["variant_id"])
        if fast_pass_variant_ids and variant_id not in fast_pass_variant_ids:
            continue
        base_ids.append(f"{base}__{variant_id}")
    return sorted(set(map(str, base_ids)))


def _load_tracked_winners(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    tracks = payload.get("tracks", {}) if isinstance(payload, dict) else {}
    winners: dict[str, str] = {}
    for track_key, meta in tracks.items():
        if not isinstance(meta, dict):
            continue
        winner = meta.get("winner")
        if winner:
            winners[str(track_key)] = str(winner)
    return winners


def _is_clear_improvement(
    *,
    candidate: TrackMetrics,
    current: TrackMetrics,
    thresholds: ImprovementThresholds,
) -> bool:
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


def _fmt_pct(value: float, digits: int = 2) -> str:
    return f"{value * 100:.{digits}f}%"


def _render_metrics(metrics: TrackMetrics) -> str:
    return f"CAGR={_fmt_pct(metrics.cagr)} Sharpe={metrics.sharpe:.4f} MaxDD={_fmt_pct(metrics.max_drawdown)} Turn={metrics.turnover:.2f}"


def _rank_candidates(candidates: list[tuple[str, TrackMetrics]]) -> list[tuple[str, TrackMetrics]]:
    ranked = [item for item in candidates if not _is_nan_metrics(item[1])]
    ranked.sort(key=lambda item: (item[1].cagr, item[1].sharpe, item[1].max_drawdown, -item[1].turnover), reverse=True)
    return ranked


def main() -> None:
    parser = argparse.ArgumentParser(description="Fast winner-only pass: evaluate current winner_core candidate family.")
    parser.add_argument("--comparison-csv", type=Path, default=DEFAULT_COMPARISON_CSV)
    parser.add_argument("--backtest-script", type=Path, default=ROOT / "backtest_marketcap_etf.py")
    parser.add_argument("--tracked-winners-json", type=Path, default=DEFAULT_TRACKED_WINNERS_JSON)
    parser.add_argument(
        "--scan-prefix",
        default="",
        help="Optional: scan ALL cached strategies in comparison CSV that start with this prefix (ignores backtest-script family list).",
    )
    parser.add_argument("--min-cagr-improvement", type=float, default=0.0010, help="Absolute CAGR improvement threshold (e.g. 0.001 = 0.10%%).")
    parser.add_argument("--min-sharpe-improvement", type=float, default=0.0050, help="Sharpe ratio improvement threshold.")
    parser.add_argument("--max-dd-worsen", type=float, default=0.0050, help="Max drawdown can worsen by at most this absolute amount.")
    parser.add_argument("--max-turnover-increase", type=float, default=0.15, help="Turnover can increase by at most this amount.")
    parser.add_argument("--write-json", type=Path, default=RESULTS_DIR / "winner_only_pass.json")
    args = parser.parse_args()

    thresholds = ImprovementThresholds(
        min_cagr_improvement=float(args.min_cagr_improvement),
        min_sharpe_improvement=float(args.min_sharpe_improvement),
        max_drawdown_worsen_abs=float(args.max_dd_worsen),
        max_turnover_increase=float(args.max_turnover_increase),
    )

    frame = pd.read_csv(args.comparison_csv)
    latest = _augment_with_synthetic_windows(_latest_per_strategy_window(frame))
    latest["strategy_base_id"] = latest["strategy_base_id"].astype(str)
    latest["sample_tag"] = latest["sample_tag"].astype(str)

    tracked_winners = _load_tracked_winners(args.tracked_winners_json)
    if not tracked_winners:
        raise SystemExit(f"[Error] Missing tracked winners JSON at {args.tracked_winners_json}. Run scripts/update_weighted_winners.py first.")

    if args.scan_prefix:
        base_ids = sorted({bid for bid in latest["strategy_base_id"].unique() if str(bid).startswith(str(args.scan_prefix))})
        family_label = f"scan_prefix={args.scan_prefix}"
    else:
        base_ids = load_winner_core_family_ids(args.backtest_script)
        family_label = "winner_core_family"

    by_id: dict[str, pd.DataFrame] = {base_id: group for base_id, group in latest.groupby("strategy_base_id")}

    def group_or_empty(base_id: str, required_tags: set[str]) -> pd.DataFrame:
        group = by_id.get(base_id, pd.DataFrame())
        tags = set(group["sample_tag"].astype(str)) if not group.empty else set()
        if not required_tags.issubset(tags):
            return pd.DataFrame()
        return group

    window_2017_candidates: list[tuple[str, TrackMetrics]] = []
    window_2023_candidates: list[tuple[str, TrackMetrics]] = []
    window_2020_candidates: list[tuple[str, TrackMetrics]] = []
    window_2025_candidates: list[tuple[str, TrackMetrics]] = []

    weighted_required = set(WEIGHTED_WINDOW_TAGS)
    for base_id in base_ids:
        weighted_group = group_or_empty(base_id, weighted_required)
        if not weighted_group.empty:
            window_2017_candidates.append((base_id, _compute_single_window_metrics(weighted_group, "since_2017_01")))
            window_2023_candidates.append((base_id, _compute_single_window_metrics(weighted_group, "since_2023_01")))
            window_2020_candidates.append((base_id, _compute_single_window_metrics(weighted_group, "since_2020_01")))
        window_2025_group = group_or_empty(base_id, {"since_2025_01"})
        if not window_2025_group.empty:
            window_2025_candidates.append((base_id, _compute_single_window_metrics(window_2025_group, "since_2025_01")))

    window_2017_ranked = _rank_candidates(window_2017_candidates)
    window_2023_ranked = _rank_candidates(window_2023_candidates)
    window_2020_ranked = _rank_candidates(window_2020_candidates)
    window_2025_ranked = _rank_candidates(window_2025_candidates)

    def winner_metrics(track_key: str, *, weights: dict[str, float] | None, sample_tag: str | None, required_tags: set[str]) -> tuple[str, TrackMetrics]:
        winner_id = tracked_winners.get(track_key, "")
        if not winner_id:
            raise RuntimeError(f"tracked winners missing key: {track_key}")
        group = group_or_empty(winner_id, required_tags)
        if group.empty:
            raise RuntimeError(f"tracked winner {winner_id} missing required windows in comparison CSV: {sorted(required_tags)}")
        if weights is not None:
            return winner_id, _compute_weighted_metrics(group, weights)
        if not sample_tag:
            raise ValueError(f"sample_tag is required for single-window track {track_key}")
        return winner_id, _compute_single_window_metrics(group, sample_tag)

    window_2017_winner_id, window_2017_winner_metrics = winner_metrics(
        "since_2017_only", weights=None, sample_tag="since_2017_01", required_tags=weighted_required
    )
    window_2023_winner_id, window_2023_winner_metrics = winner_metrics(
        "since_2023_only", weights=None, sample_tag="since_2023_01", required_tags=weighted_required
    )
    window_2020_winner_id, window_2020_winner_metrics = winner_metrics(
        "since_2020_only", weights=None, sample_tag="since_2020_01", required_tags=weighted_required
    )
    window_2025_winner_id, window_2025_winner_metrics = winner_metrics(
        "since_2025_only", weights=None, sample_tag="since_2025_01", required_tags={"since_2025_01"}
    )

    def best_of(ranked: list[tuple[str, TrackMetrics]]) -> tuple[str, TrackMetrics] | None:
        return ranked[0] if ranked else None

    best_2017 = best_of(window_2017_ranked)
    best_2023 = best_of(window_2023_ranked)
    best_2020 = best_of(window_2020_ranked)
    best_2025 = best_of(window_2025_ranked)

    improvements: dict[str, dict[str, Any]] = {}

    def best_clear_improvement(
        ranked: list[tuple[str, TrackMetrics]],
        current: TrackMetrics,
    ) -> tuple[str, TrackMetrics] | None:
        for base_id, metrics in ranked:
            if _is_clear_improvement(candidate=metrics, current=current, thresholds=thresholds):
                return base_id, metrics
        return None

    def eval_track(
        track_key: str,
        current_id: str,
        current_metrics: TrackMetrics,
        best: tuple[str, TrackMetrics] | None,
        ranked: list[tuple[str, TrackMetrics]],
    ) -> None:
        if best is None:
            improvements[track_key] = {"status": "no_candidates"}
            return
        best_id, best_metrics = best
        clear_best = best_clear_improvement(ranked, current_metrics)
        improvements[track_key] = {
            "status": "clear_improvement" if clear_best else "no_clear_improvement",
            "current": {"strategy_base_id": current_id, "metrics": asdict(current_metrics)},
            "best": {"strategy_base_id": best_id, "metrics": asdict(best_metrics)},
            "best_clear": (
                {"strategy_base_id": clear_best[0], "metrics": asdict(clear_best[1])} if clear_best else None
            ),
            "top5": [{"strategy_base_id": sid, "metrics": asdict(m)} for sid, m in ranked[:5]],
        }

    eval_track("since_2017_only", window_2017_winner_id, window_2017_winner_metrics, best_2017, window_2017_ranked)
    eval_track("since_2023_only", window_2023_winner_id, window_2023_winner_metrics, best_2023, window_2023_ranked)
    eval_track("since_2020_only", window_2020_winner_id, window_2020_winner_metrics, best_2020, window_2020_ranked)
    eval_track("since_2025_only", window_2025_winner_id, window_2025_winner_metrics, best_2025, window_2025_ranked)

    as_of = str(pd.to_datetime(latest["sample_end"].max(), errors="coerce").date())
    out = {
        "as_of": as_of,
        "family": family_label,
        "thresholds": asdict(thresholds),
        "tracked_winners": tracked_winners,
        "improvements": improvements,
    }
    args.write_json.parent.mkdir(parents=True, exist_ok=True)
    args.write_json.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"[OK] as_of={as_of} family={family_label} candidates={len(base_ids)} evaluated={len(window_2017_ranked)}")
    print(f"[OK] thresholds: min_cagr={thresholds.min_cagr_improvement:.4f} min_sharpe={thresholds.min_sharpe_improvement:.4f} "
          f"max_dd_worsen={thresholds.max_drawdown_worsen_abs:.4f} max_turnover_inc={thresholds.max_turnover_increase:.2f}")
    print("")

    print(f"[Track] since_2017_only      current={window_2017_winner_id} {_render_metrics(window_2017_winner_metrics)}")
    if best_2017:
        best_id, best_metrics = best_2017
        print(f"        best={best_id} {_render_metrics(best_metrics)} "
              f"ΔCAGR={_fmt_pct(best_metrics.cagr - window_2017_winner_metrics.cagr)} "
              f"ΔSharpe={best_metrics.sharpe - window_2017_winner_metrics.sharpe:+.4f}")
    clear_2017 = best_clear_improvement(window_2017_ranked, window_2017_winner_metrics)
    if clear_2017:
        clear_id, clear_metrics = clear_2017
        print(f"        clear={clear_id} {_render_metrics(clear_metrics)} "
              f"ΔCAGR={_fmt_pct(clear_metrics.cagr - window_2017_winner_metrics.cagr)} "
              f"ΔSharpe={clear_metrics.sharpe - window_2017_winner_metrics.sharpe:+.4f}")
    print("")

    print(f"[Track] since_2023_only      current={window_2023_winner_id} {_render_metrics(window_2023_winner_metrics)}")
    if best_2023:
        best_id, best_metrics = best_2023
        print(
            f"        best={best_id} {_render_metrics(best_metrics)} "
            f"ΔCAGR={_fmt_pct(best_metrics.cagr - window_2023_winner_metrics.cagr)} "
            f"ΔSharpe={best_metrics.sharpe - window_2023_winner_metrics.sharpe:+.4f}"
        )
    clear_2023 = best_clear_improvement(window_2023_ranked, window_2023_winner_metrics)
    if clear_2023:
        clear_id, clear_metrics = clear_2023
        print(
            f"        clear={clear_id} {_render_metrics(clear_metrics)} "
            f"ΔCAGR={_fmt_pct(clear_metrics.cagr - window_2023_winner_metrics.cagr)} "
            f"ΔSharpe={clear_metrics.sharpe - window_2023_winner_metrics.sharpe:+.4f}"
        )
    print("")

    print(f"[Track] since_2020_only      current={window_2020_winner_id} {_render_metrics(window_2020_winner_metrics)}")
    if best_2020:
        best_id, best_metrics = best_2020
        print(
            f"        best={best_id} {_render_metrics(best_metrics)} "
            f"ΔCAGR={_fmt_pct(best_metrics.cagr - window_2020_winner_metrics.cagr)} "
            f"ΔSharpe={best_metrics.sharpe - window_2020_winner_metrics.sharpe:+.4f}"
        )
    clear_2020 = best_clear_improvement(window_2020_ranked, window_2020_winner_metrics)
    if clear_2020:
        clear_id, clear_metrics = clear_2020
        print(
            f"        clear={clear_id} {_render_metrics(clear_metrics)} "
            f"ΔCAGR={_fmt_pct(clear_metrics.cagr - window_2020_winner_metrics.cagr)} "
            f"ΔSharpe={clear_metrics.sharpe - window_2020_winner_metrics.sharpe:+.4f}"
        )
    print("")

    print(f"[Track] since_2025_only      current={window_2025_winner_id} {_render_metrics(window_2025_winner_metrics)}")
    if best_2025:
        best_id, best_metrics = best_2025
        print(
            f"        best={best_id} {_render_metrics(best_metrics)} "
            f"ΔCAGR={_fmt_pct(best_metrics.cagr - window_2025_winner_metrics.cagr)} "
            f"ΔSharpe={best_metrics.sharpe - window_2025_winner_metrics.sharpe:+.4f}"
        )
    clear_2025 = best_clear_improvement(window_2025_ranked, window_2025_winner_metrics)
    if clear_2025:
        clear_id, clear_metrics = clear_2025
        print(
            f"        clear={clear_id} {_render_metrics(clear_metrics)} "
            f"ΔCAGR={_fmt_pct(clear_metrics.cagr - window_2025_winner_metrics.cagr)} "
            f"ΔSharpe={clear_metrics.sharpe - window_2025_winner_metrics.sharpe:+.4f}"
        )

    clear = [k for k, v in improvements.items() if isinstance(v, dict) and v.get("status") == "clear_improvement"]
    if clear:
        print("")
        print(f"[Result] CLEAR improvements found for tracks: {', '.join(clear)}")
        raise SystemExit(2)

    print("")
    print("[Result] No clear improvements vs tracked winners.")


if __name__ == "__main__":
    main()
