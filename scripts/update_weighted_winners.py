from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
DEFAULT_COMPARISON_CSV = RESULTS_DIR / "strategy_comparison_base_method.csv"
README_PATH = ROOT / "README.md"

AUTO_START = "<!-- AUTO:WEIGHTED-WINNERS:START -->"
AUTO_END = "<!-- AUTO:WEIGHTED-WINNERS:END -->"

WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01")

WEIGHTS_SHORT_CYCLE = {"since_2017_01": 0.30, "since_2020_01": 0.30, "since_2023_01": 0.40}
WEIGHTS_MID_CYCLE = {"since_2017_01": 0.30, "since_2020_01": 0.40, "since_2023_01": 0.30}


@dataclass(frozen=True)
class TrackMetrics:
    cagr: float
    sharpe: float
    max_drawdown: float
    turnover: float


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
        tags = set(group["sample_tag"].astype(str))
        if not set(WINDOW_TAGS).issubset(tags):
            continue
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
                for tag in WINDOW_TAGS
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


def _pick_winner(latest: pd.DataFrame, weights: dict[str, float]) -> tuple[str, TrackMetrics]:
    candidates: list[tuple[str, TrackMetrics]] = []
    for base_id, group in latest.groupby("strategy_base_id"):
        tags = set(group["sample_tag"].astype(str))
        if not set(WINDOW_TAGS).issubset(tags):
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


def _fmt_pct(value: float, digits: int = 2) -> str:
    return f"{value * 100:.{digits}f}%"


def _render_block(
    strategies: dict[str, dict],
    short_winner_id: str,
    short_metrics: TrackMetrics,
    mid_winner_id: str,
    mid_metrics: TrackMetrics,
    sample_end: str,
) -> str:
    def render_track(title: str, weights: dict[str, float], winner_id: str, metrics: TrackMetrics) -> str:
        info = strategies[winner_id]
        windows = info["windows"]
        weight_str = ", ".join(f"{k.replace('since_', '').replace('_', '-')}={int(v*100)}%" for k, v in weights.items())
        return "\n".join(
            [
                f"### {title}",
                "",
                f"- Strategy: `{winner_id}` ({info['strategy_base_name']})",
                f"- Weighted (CAGR / Sharpe / Max DD / Turnover): "
                f"`{_fmt_pct(metrics.cagr)}` / `{metrics.sharpe:.4f}` / `{_fmt_pct(metrics.max_drawdown)}` / `{metrics.turnover:.2f}`",
                "",
                f"Window metrics (as of `{sample_end}`, weights: {weight_str}):",
                "",
                f"- `2017-01-01` → `{sample_end}`: CAGR `{_fmt_pct(windows['since_2017_01']['cagr'])}`, "
                f"Max DD `{_fmt_pct(windows['since_2017_01']['max_drawdown'])}`, Sharpe `{windows['since_2017_01']['sharpe']:.4f}`",
                f"- `2020-01-01` → `{sample_end}`: CAGR `{_fmt_pct(windows['since_2020_01']['cagr'])}`, "
                f"Max DD `{_fmt_pct(windows['since_2020_01']['max_drawdown'])}`, Sharpe `{windows['since_2020_01']['sharpe']:.4f}`",
                f"- `2023-01-01` → `{sample_end}`: CAGR `{_fmt_pct(windows['since_2023_01']['cagr'])}`, "
                f"Max DD `{_fmt_pct(windows['since_2023_01']['max_drawdown'])}`, Sharpe `{windows['since_2023_01']['sharpe']:.4f}`",
                "",
            ]
        )

    parts = [
        "This repo tracks *two winners in parallel* using weighted multi-window scoring across the three validation windows:",
        "",
        "- `since_2017_01` (long window)",
        "- `since_2020_01` (mid window)",
        "- `since_2023_01` (short window)",
        "",
        render_track("Short-cycle Winner (30/30/40)", WEIGHTS_SHORT_CYCLE, short_winner_id, short_metrics),
        render_track("Mid-cycle Winner (30/40/30)", WEIGHTS_MID_CYCLE, mid_winner_id, mid_metrics),
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
    args = parser.parse_args()

    frame = pd.read_csv(args.comparison_csv)
    latest = _latest_per_strategy_window(frame)
    strategies = _build_strategy_map(latest)
    if not strategies:
        raise RuntimeError("No strategies with complete 2017/2020/2023 windows found in comparison CSV.")

    short_id, short_metrics = _pick_winner(latest, WEIGHTS_SHORT_CYCLE)
    mid_id, mid_metrics = _pick_winner(latest, WEIGHTS_MID_CYCLE)
    sample_end = max(info["sample_end"] for info in strategies.values())

    payload = {
        "as_of": sample_end,
        "window_tags": list(WINDOW_TAGS),
        "tracks": {
            "short_cycle_30_30_40": {
                "weights": WEIGHTS_SHORT_CYCLE,
                "winner": short_id,
                "metrics": {
                    "weighted_cagr": short_metrics.cagr,
                    "weighted_sharpe": short_metrics.sharpe,
                    "weighted_max_drawdown": short_metrics.max_drawdown,
                    "weighted_turnover": short_metrics.turnover,
                },
            },
            "mid_cycle_30_40_30": {
                "weights": WEIGHTS_MID_CYCLE,
                "winner": mid_id,
                "metrics": {
                    "weighted_cagr": mid_metrics.cagr,
                    "weighted_sharpe": mid_metrics.sharpe,
                    "weighted_max_drawdown": mid_metrics.max_drawdown,
                    "weighted_turnover": mid_metrics.turnover,
                },
            },
        },
        "strategies": {
            sid: {
                "strategy_base_name": info["strategy_base_name"],
                "windows": info["windows"],
            }
            for sid, info in strategies.items()
            if sid in {short_id, mid_id}
        },
    }
    args.write_json.parent.mkdir(parents=True, exist_ok=True)
    args.write_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    block = _render_block(strategies, short_id, short_metrics, mid_id, mid_metrics, sample_end)
    update_readme(args.readme, block)

    print(f"[OK] Updated {args.readme}")
    print(f"[OK] Wrote {args.write_json}")
    print(f"[OK] Short-cycle winner: {short_id} (wCAGR={_fmt_pct(short_metrics.cagr)}, wSharpe={short_metrics.sharpe:.4f})")
    print(f"[OK] Mid-cycle winner:   {mid_id} (wCAGR={_fmt_pct(mid_metrics.cagr)}, wSharpe={mid_metrics.sharpe:.4f})")


if __name__ == "__main__":
    main()

