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

WEIGHTED_WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01")
SAMPLE_TAG_STARTS = {
    "since_2017_01": pd.Timestamp("2017-01-01"),
    "since_2020_01": pd.Timestamp("2020-01-01"),
    "since_2023_01": pd.Timestamp("2023-01-01"),
    "since_2025_01": pd.Timestamp("2025-01-01"),
}
STATIC_BASE_IDS = {"large_cap_pool", "kechuang_xuangu"}

WEIGHTS_SHORT_CYCLE = {"since_2017_01": 0.30, "since_2020_01": 0.30, "since_2023_01": 0.40}
WEIGHTS_MID_CYCLE = {"since_2017_01": 0.30, "since_2020_01": 0.40, "since_2023_01": 0.30}
WEIGHTS_2020_ONLY = {"since_2020_01": 1.00}
WEIGHTS_2025_ONLY = {"since_2025_01": 1.00}


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


def _pick_winner(latest: pd.DataFrame, weights: dict[str, float]) -> tuple[str, TrackMetrics]:
    candidates: list[tuple[str, TrackMetrics]] = []
    for base_id, group in latest.groupby("strategy_base_id"):
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


def _pick_single_window_winner(latest: pd.DataFrame, sample_tag: str) -> tuple[str, TrackMetrics]:
    candidates: list[tuple[str, TrackMetrics]] = []
    for base_id, group in latest.groupby("strategy_base_id"):
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
    return f"{value * 100:.{digits}f}%"


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
    else:
        candidate_dirs = [
            RESULTS_DIR / f"{base_id}__since_2025_01",
            RESULTS_DIR / f"{base_id}__since_2023_01",
            RESULTS_DIR / f"{base_id}__since_2020_01",
            RESULTS_DIR / f"{base_id}__since_2017_01",
        ]

    for result_dir in candidate_dirs:
        equity_path = result_dir / "equity_curve.csv"
        monthly_path = result_dir / "monthly_returns.csv"
        turnover_path = result_dir / "turnover.csv"
        if not (equity_path.exists() and monthly_path.exists() and turnover_path.exists()):
            continue
        equity = pd.read_csv(equity_path, parse_dates=["date"])
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
    for base_id in sorted(set(existing["strategy_base_id"].astype(str)) | STATIC_BASE_IDS):
        if (base_id, "since_2025_01") in existing_keys:
            continue
        metrics = _slice_window_from_existing_results(base_id, "since_2025_01")
        if metrics is None:
            continue
        needed_rows.append(
            {
                "strategy_base_id": base_id,
                "strategy_base_name": base_name_map.get(base_id, base_id),
                "sample_tag": "since_2025_01",
                "sample_label": "2025-01 起",
                "sample_short_label": "2025-01",
                "sample_start": SAMPLE_TAG_STARTS["since_2025_01"],
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


def _render_block(
    strategies: dict[str, dict],
    short_winner_id: str,
    short_metrics: TrackMetrics,
    mid_winner_id: str,
    mid_metrics: TrackMetrics,
    window_2020_winner_id: str,
    window_2020_metrics: TrackMetrics,
    window_2025_winner_id: str,
    window_2025_metrics: TrackMetrics,
    sample_end: str,
) -> str:
    def render_track(title: str, weights: dict[str, float], winner_id: str, metrics: TrackMetrics) -> str:
        info = strategies[winner_id]
        windows = info["windows"]
        weight_str = ", ".join(f"{k.replace('since_', '').replace('_', '-')}={int(v*100)}%" for k, v in weights.items())
        def render_window(tag: str) -> str:
            if tag not in windows:
                return f"- `{SAMPLE_TAG_STARTS[tag].date()}` window: n/a"
            return (
                f"- `{SAMPLE_TAG_STARTS[tag].date()}` → `{sample_end}`: CAGR `{_fmt_pct(windows[tag]['cagr'])}`, "
                f"Max DD `{_fmt_pct(windows[tag]['max_drawdown'])}`, Sharpe `{windows[tag]['sharpe']:.4f}`"
            )
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
                render_window("since_2017_01"),
                render_window("since_2020_01"),
                render_window("since_2023_01"),
                render_window("since_2025_01"),
                "",
            ]
        )

    parts = [
        "This repo tracks *three winners in parallel* using weighted multi-window scoring across the three validation windows:",
        "",
        "- `since_2017_01` (long window)",
        "- `since_2020_01` (mid window)",
        "- `since_2023_01` (short window)",
        "- `since_2025_01` (very short window)",
        "",
        render_track("Short-cycle Winner (30/30/40)", WEIGHTS_SHORT_CYCLE, short_winner_id, short_metrics),
        render_track("Mid-cycle Winner (30/40/30)", WEIGHTS_MID_CYCLE, mid_winner_id, mid_metrics),
        render_track("2020-Window Winner (2020-only checkpoint)", WEIGHTS_2020_ONLY, window_2020_winner_id, window_2020_metrics),
        render_track("2025-Window Winner (2025-only checkpoint)", WEIGHTS_2025_ONLY, window_2025_winner_id, window_2025_metrics),
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
    latest = _augment_with_synthetic_windows(_latest_per_strategy_window(frame))
    strategies = _build_strategy_map(latest)
    if not strategies:
        raise RuntimeError("No strategies with complete 2017/2020/2023 windows found in comparison CSV.")

    short_id, short_metrics = _pick_winner(latest, WEIGHTS_SHORT_CYCLE)
    mid_id, mid_metrics = _pick_winner(latest, WEIGHTS_MID_CYCLE)
    window_2020_id, window_2020_metrics = _pick_single_window_winner(latest, "since_2020_01")
    window_2025_id, window_2025_metrics = _pick_single_window_winner(latest, "since_2025_01")
    sample_end = max(info["sample_end"] for info in strategies.values())

    payload = {
        "as_of": sample_end,
        "window_tags": list(SAMPLE_TAG_STARTS),
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
        },
        "strategies": {
            sid: {
                "strategy_base_name": info["strategy_base_name"],
                "windows": info["windows"],
            }
            for sid, info in strategies.items()
            if sid in {short_id, mid_id, window_2020_id, window_2025_id}
        },
    }
    args.write_json.parent.mkdir(parents=True, exist_ok=True)
    args.write_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    block = _render_block(
        strategies,
        short_id,
        short_metrics,
        mid_id,
        mid_metrics,
        window_2020_id,
        window_2020_metrics,
        window_2025_id,
        window_2025_metrics,
        sample_end,
    )
    update_readme(args.readme, block)

    print(f"[OK] Updated {args.readme}")
    print(f"[OK] Wrote {args.write_json}")
    print(f"[OK] Short-cycle winner: {short_id} (wCAGR={_fmt_pct(short_metrics.cagr)}, wSharpe={short_metrics.sharpe:.4f})")
    print(f"[OK] Mid-cycle winner:   {mid_id} (wCAGR={_fmt_pct(mid_metrics.cagr)}, wSharpe={mid_metrics.sharpe:.4f})")
    print(f"[OK] 2020-window winner: {window_2020_id} (CAGR={_fmt_pct(window_2020_metrics.cagr)}, Sharpe={window_2020_metrics.sharpe:.4f})")
    print(f"[OK] 2025-window winner: {window_2025_id} (CAGR={_fmt_pct(window_2025_metrics.cagr)}, Sharpe={window_2025_metrics.sharpe:.4f})")


if __name__ == "__main__":
    main()
