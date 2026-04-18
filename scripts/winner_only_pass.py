from __future__ import annotations

import argparse
import ast
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
DEFAULT_COMPARISON_CSV = RESULTS_DIR / "strategy_comparison_base_method.csv"
DEFAULT_TRACKED_WINNERS_JSON = RESULTS_DIR / "weighted_track_winners.json"

WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01")

WEIGHTS_SHORT_CYCLE = {"since_2017_01": 0.30, "since_2020_01": 0.30, "since_2023_01": 0.40}
WEIGHTS_MID_CYCLE = {"since_2017_01": 0.30, "since_2020_01": 0.40, "since_2023_01": 0.30}


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
    consts = _parse_python_constants(backtest_path, ["WINNER_ONLY_STRATEGY_ID", "WINNER_CORE_VARIANTS"])
    base = str(consts["WINNER_ONLY_STRATEGY_ID"])
    variants = consts["WINNER_CORE_VARIANTS"]
    if not isinstance(variants, list):
        raise TypeError("WINNER_CORE_VARIANTS is not a list")
    base_ids = [base]
    for variant in variants:
        if not isinstance(variant, dict) or "variant_id" not in variant:
            raise TypeError("WINNER_CORE_VARIANTS item missing variant_id")
        base_ids.append(f"{base}__{variant['variant_id']}")
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
    parser.add_argument("--min-cagr-improvement", type=float, default=0.0010, help="Absolute CAGR improvement threshold (e.g. 0.001 = 0.10%).")
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
    latest = _latest_per_strategy_window(frame)
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

    required_tags = set(WINDOW_TAGS)
    by_id: dict[str, pd.DataFrame] = {base_id: group for base_id, group in latest.groupby("strategy_base_id")}

    def group_or_empty(base_id: str) -> pd.DataFrame:
        group = by_id.get(base_id, pd.DataFrame())
        tags = set(group["sample_tag"].astype(str)) if not group.empty else set()
        if not required_tags.issubset(tags):
            return pd.DataFrame()
        return group

    short_candidates: list[tuple[str, TrackMetrics]] = []
    mid_candidates: list[tuple[str, TrackMetrics]] = []
    window_2020_candidates: list[tuple[str, TrackMetrics]] = []

    for base_id in base_ids:
        group = group_or_empty(base_id)
        if group.empty:
            continue
        short_candidates.append((base_id, _compute_weighted_metrics(group, WEIGHTS_SHORT_CYCLE)))
        mid_candidates.append((base_id, _compute_weighted_metrics(group, WEIGHTS_MID_CYCLE)))
        window_2020_candidates.append((base_id, _compute_single_window_metrics(group, "since_2020_01")))

    short_ranked = _rank_candidates(short_candidates)
    mid_ranked = _rank_candidates(mid_candidates)
    window_2020_ranked = _rank_candidates(window_2020_candidates)

    def winner_metrics(track_key: str, weights: dict[str, float] | None) -> tuple[str, TrackMetrics]:
        winner_id = tracked_winners.get(track_key, "")
        if not winner_id:
            raise RuntimeError(f"tracked winners missing key: {track_key}")
        group = group_or_empty(winner_id)
        if group.empty:
            raise RuntimeError(f"tracked winner {winner_id} missing complete windows in comparison CSV")
        if weights is None:
            return winner_id, _compute_single_window_metrics(group, "since_2020_01")
        return winner_id, _compute_weighted_metrics(group, weights)

    short_winner_id, short_winner_metrics = winner_metrics("short_cycle_30_30_40", WEIGHTS_SHORT_CYCLE)
    mid_winner_id, mid_winner_metrics = winner_metrics("mid_cycle_30_40_30", WEIGHTS_MID_CYCLE)
    window_2020_winner_id, window_2020_winner_metrics = winner_metrics("since_2020_only", None)

    def best_of(ranked: list[tuple[str, TrackMetrics]]) -> tuple[str, TrackMetrics] | None:
        return ranked[0] if ranked else None

    best_short = best_of(short_ranked)
    best_mid = best_of(mid_ranked)
    best_2020 = best_of(window_2020_ranked)

    improvements: dict[str, dict[str, Any]] = {}

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
        improved = _is_clear_improvement(candidate=best_metrics, current=current_metrics, thresholds=thresholds)
        improvements[track_key] = {
            "status": "clear_improvement" if improved else "no_clear_improvement",
            "current": {"strategy_base_id": current_id, "metrics": asdict(current_metrics)},
            "best": {"strategy_base_id": best_id, "metrics": asdict(best_metrics)},
            "top5": [{"strategy_base_id": sid, "metrics": asdict(m)} for sid, m in ranked[:5]],
        }

    eval_track("short_cycle_30_30_40", short_winner_id, short_winner_metrics, best_short, short_ranked)
    eval_track("mid_cycle_30_40_30", mid_winner_id, mid_winner_metrics, best_mid, mid_ranked)
    eval_track("since_2020_only", window_2020_winner_id, window_2020_winner_metrics, best_2020, window_2020_ranked)

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

    print(f"[OK] as_of={as_of} family={family_label} candidates={len(base_ids)} evaluated={len(short_ranked)}")
    print(f"[OK] thresholds: min_cagr={thresholds.min_cagr_improvement:.4f} min_sharpe={thresholds.min_sharpe_improvement:.4f} "
          f"max_dd_worsen={thresholds.max_drawdown_worsen_abs:.4f} max_turnover_inc={thresholds.max_turnover_increase:.2f}")
    print("")

    print(f"[Track] short_cycle_30_30_40 current={short_winner_id} {_render_metrics(short_winner_metrics)}")
    if best_short:
        best_id, best_metrics = best_short
        print(f"        best={best_id} {_render_metrics(best_metrics)} "
              f"ΔCAGR={_fmt_pct(best_metrics.cagr - short_winner_metrics.cagr)} "
              f"ΔSharpe={best_metrics.sharpe - short_winner_metrics.sharpe:+.4f}")
    print("")

    print(f"[Track] mid_cycle_30_40_30   current={mid_winner_id} {_render_metrics(mid_winner_metrics)}")
    if best_mid:
        best_id, best_metrics = best_mid
        print(
            f"        best={best_id} {_render_metrics(best_metrics)} "
            f"ΔCAGR={_fmt_pct(best_metrics.cagr - mid_winner_metrics.cagr)} "
            f"ΔSharpe={best_metrics.sharpe - mid_winner_metrics.sharpe:+.4f}"
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

    clear = [k for k, v in improvements.items() if isinstance(v, dict) and v.get("status") == "clear_improvement"]
    if clear:
        print("")
        print(f"[Result] CLEAR improvements found for tracks: {', '.join(clear)}")
        raise SystemExit(2)

    print("")
    print("[Result] No clear improvements vs tracked winners.")


if __name__ == "__main__":
    main()
