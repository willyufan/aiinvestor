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

WEIGHTS_2017_ONLY = {"since_2017_01": 1.00}
WEIGHTS_2023_ONLY = {"since_2023_01": 1.00}
WEIGHTS_2020_ONLY = {"since_2020_01": 1.00}
WEIGHTS_2025_ONLY = {"since_2025_01": 1.00}


@dataclass(frozen=True)
class TrackMetrics:
    cagr: float
    sharpe: float
    max_drawdown: float
    turnover: float


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
            RESULTS_DIR / f"{base_id}__since_2020_01",
            RESULTS_DIR / f"{base_id}__since_2017_01",
            RESULTS_DIR / f"{base_id}__since_2023_01",
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

    def render_path2(title: str, base_id: str, summary: dict[str, float]) -> str:
        info = strategies[base_id]
        windows = info["windows"]
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
                f"- Strategy: `{base_id}` ({info['strategy_base_name']})",
                f"- Robust (mean CAGR / min CAGR / mean Sharpe / worst Max DD / mean Turnover): "
                f"`{_fmt_pct(summary['cagr_mean'])}` / `{_fmt_pct(summary['cagr_min'])}` / `{summary['sharpe_mean']:.4f}` / "
                f"`{_fmt_pct(summary['max_drawdown_worst'])}` / `{summary['turnover_mean']:.2f}`",
                "",
                "Window metrics:",
                "",
                render_window("since_2017_01"),
                render_window("since_2020_01"),
                render_window("since_2023_01"),
                render_window("since_2025_01"),
                "",
            ]
        )

    parts = [
        "This repo tracks **two research paths**:",
        "",
        "- **Path 1 (winner-core family constrained):** 4 tracked winners across multi-window + checkpoint scoring.",
        "- **Path 2 (unconstrained max-return):** 4 tracked single-window winners plus a separate best robust candidate ranked across all 4 windows.",
        "",
        "Validation windows:",
        "",
        "- `since_2017_01` (long window)",
        "- `since_2020_01` (mid window)",
        "- `since_2023_01` (short window)",
        "- `since_2025_01` (very short window)",
        "",
        "## Path 1 — Winner-Core Tracked Winners",
        "",
        render_track("2017-Window Winner", WEIGHTS_2017_ONLY, window_2017_winner_id, window_2017_metrics),
        render_track("2023-Window Winner", WEIGHTS_2023_ONLY, window_2023_winner_id, window_2023_metrics),
        render_track("2020-Window Winner (2020-only checkpoint)", WEIGHTS_2020_ONLY, window_2020_winner_id, window_2020_metrics),
        render_track("2025-Window Winner (2025-only checkpoint)", WEIGHTS_2025_ONLY, window_2025_winner_id, window_2025_metrics),
        "## Path 2 — Unconstrained Window Winners",
        "",
        render_track("2017-Window Winner (Path 2)", WEIGHTS_2017_ONLY, path2_window_2017_id, path2_window_2017_metrics),
        render_track("2023-Window Winner (Path 2)", WEIGHTS_2023_ONLY, path2_window_2023_id, path2_window_2023_metrics),
        render_track("2020-Window Winner (Path 2)", WEIGHTS_2020_ONLY, path2_window_2020_id, path2_window_2020_metrics),
        render_track("2025-Window Winner (Path 2)", WEIGHTS_2025_ONLY, path2_window_2025_id, path2_window_2025_metrics),
        "## Path 2 — Max-Return Candidate",
        "",
        render_path2("Best Robust Candidate (4-window)", path2_id, path2_summary),
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

    prefix = load_winner_core_prefix()
    winner_core_ids = {str(bid) for bid in latest["strategy_base_id"].astype(str).unique() if str(bid).startswith(prefix)}
    if not winner_core_ids:
        raise RuntimeError(f"No winner-core strategies found with prefix={prefix!r}")

    window_2017_id, window_2017_metrics = _pick_single_window_winner(
        latest, "since_2017_01", allowed_base_ids=winner_core_ids
    )
    window_2023_id, window_2023_metrics = _pick_single_window_winner(
        latest, "since_2023_01", allowed_base_ids=winner_core_ids
    )
    window_2020_id, window_2020_metrics = _pick_single_window_winner(latest, "since_2020_01", allowed_base_ids=winner_core_ids)
    window_2025_id, window_2025_metrics = _pick_single_window_winner(latest, "since_2025_01", allowed_base_ids=winner_core_ids)
    path2_window_2017_id, path2_window_2017_metrics = _pick_single_window_winner(latest, "since_2017_01")
    path2_window_2023_id, path2_window_2023_metrics = _pick_single_window_winner(latest, "since_2023_01")
    path2_window_2020_id, path2_window_2020_metrics = _pick_single_window_winner(latest, "since_2020_01")
    path2_window_2025_id, path2_window_2025_metrics = _pick_single_window_winner(latest, "since_2025_01")
    path2_id, path2_summary = _pick_path2_candidate(latest)
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

    print(f"[OK] Updated {args.readme}")
    print(f"[OK] Wrote {args.write_json}")
    print(f"[OK] 2017-window winner: {window_2017_id} (CAGR={_fmt_pct(window_2017_metrics.cagr)}, Sharpe={window_2017_metrics.sharpe:.4f})")
    print(f"[OK] 2023-window winner: {window_2023_id} (CAGR={_fmt_pct(window_2023_metrics.cagr)}, Sharpe={window_2023_metrics.sharpe:.4f})")
    print(f"[OK] 2020-window winner: {window_2020_id} (CAGR={_fmt_pct(window_2020_metrics.cagr)}, Sharpe={window_2020_metrics.sharpe:.4f})")
    print(f"[OK] 2025-window winner: {window_2025_id} (CAGR={_fmt_pct(window_2025_metrics.cagr)}, Sharpe={window_2025_metrics.sharpe:.4f})")
    print(f"[OK] Path2 2017-window winner: {path2_window_2017_id} (CAGR={_fmt_pct(path2_window_2017_metrics.cagr)}, Sharpe={path2_window_2017_metrics.sharpe:.4f})")
    print(f"[OK] Path2 2023-window winner: {path2_window_2023_id} (CAGR={_fmt_pct(path2_window_2023_metrics.cagr)}, Sharpe={path2_window_2023_metrics.sharpe:.4f})")
    print(f"[OK] Path2 2020-window winner: {path2_window_2020_id} (CAGR={_fmt_pct(path2_window_2020_metrics.cagr)}, Sharpe={path2_window_2020_metrics.sharpe:.4f})")
    print(f"[OK] Path2 2025-window winner: {path2_window_2025_id} (CAGR={_fmt_pct(path2_window_2025_metrics.cagr)}, Sharpe={path2_window_2025_metrics.sharpe:.4f})")
    print(f"[OK] Path 2 candidate:   {path2_id} (meanCAGR={_fmt_pct(path2_summary['cagr_mean'])}, minCAGR={_fmt_pct(path2_summary['cagr_min'])})")


if __name__ == "__main__":
    main()
