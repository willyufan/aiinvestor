from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "data_cache" / "mplconfig"))

import matplotlib
import pandas as pd
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


RESULTS_DIR = ROOT / "results"
DOCS_DIR = ROOT / "docs"
OUTPUT_PATH = DOCS_DIR / "strategy_comparison.png"
COMPARISON_CSV = RESULTS_DIR / "strategy_comparison_base_method.csv"
WEIGHTED_WINNERS_JSON = RESULTS_DIR / "weighted_track_winners.json"

SAMPLE_WINDOWS = [
    {"sample_tag": "since_2017_01", "title": "9Y Window (Since 2017-01)", "short_label": "2017-01"},
    {"sample_tag": "since_2020_01", "title": "6Y Window (Since 2020-01)", "short_label": "2020-01"},
    {"sample_tag": "since_2023_01", "title": "3Y Window (Since 2023-01)", "short_label": "2023-01"},
]

TRACK_WEIGHTS = {
    "short_cycle_30_30_40": {"since_2017_01": 0.30, "since_2020_01": 0.30, "since_2023_01": 0.40},
    "mid_cycle_30_40_30": {"since_2017_01": 0.30, "since_2020_01": 0.40, "since_2023_01": 0.30},
}

STRATEGIES = [
    {
        "base_id": "large_cap_pool",
        "label": "Large Cap Static",
        "color": "#0f766e",
        "kind": "static",
        "available_sample_tags": {"since_2020_01", "since_2023_01"},
    },
    {
        "base_id": "kechuang_xuangu",
        "label": "Kechuang Static",
        "color": "#1d4ed8",
        "kind": "static",
        "available_sample_tags": {"since_2020_01", "since_2023_01"},
    },
    {"base_id": "core_explore_80_20_total_mv_index_core", "label": "80/20 Index Core", "color": "#94a3b8"},
    {"base_id": "core_explore_80_20_total_mv_winner_core", "label": "80/20 Winner Core", "color": "#2563eb"},
    {
        "base_id": "core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp",
        "label": "80/20 Winner Core (Aggressive)",
        "color": "#dc2626",
    },
    {"base_id": "pure_core_growth_6", "label": "Pure Core 6", "color": "#7c3aed"},
]

STRATEGY_LABEL_BY_ID = {item["base_id"]: item["label"] for item in STRATEGIES}


def _fmt_pct(value: float, digits: int = 2) -> str:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "n/a"
    return f"{value * 100:.{digits}f}%"


def load_weighted_winners() -> dict:
    if WEIGHTED_WINNERS_JSON.exists():
        with WEIGHTED_WINNERS_JSON.open("r", encoding="utf-8") as f:
            return json.load(f)

    if not COMPARISON_CSV.exists():
        return {}

    frame = pd.read_csv(COMPARISON_CSV)
    frame["sample_end"] = pd.to_datetime(frame["sample_end"], errors="coerce")
    frame = frame.dropna(subset=["sample_end"])
    frame = frame.sort_values(["strategy_base_id", "sample_tag", "sample_end"])
    latest = frame.groupby(["strategy_base_id", "sample_tag"], as_index=False).tail(1)

    required_tags = {"since_2017_01", "since_2020_01", "since_2023_01"}

    def weighted(group: pd.DataFrame, weights: dict[str, float], column: str) -> float:
        total = 0.0
        for tag, w in weights.items():
            s = group.loc[group["sample_tag"] == tag, column]
            if s.empty:
                return float("nan")
            total += w * float(s.iloc[0])
        return float(total)

    def pick(weights: dict[str, float]) -> tuple[str, dict] | None:
        candidates: list[tuple[str, float, float, float, float]] = []
        for base_id, group in latest.groupby("strategy_base_id"):
            tags = set(group["sample_tag"].astype(str))
            if not required_tags.issubset(tags):
                continue
            cagr = weighted(group, weights, "cagr")
            sharpe = weighted(group, weights, "sharpe_ratio")
            maxdd = weighted(group, weights, "max_drawdown")
            turnover = weighted(group, weights, "average_annual_turnover")
            if any(np.isnan(v) for v in (cagr, sharpe, maxdd, turnover)):
                continue
            candidates.append((str(base_id), cagr, sharpe, maxdd, turnover))
        if not candidates:
            return None
        candidates.sort(key=lambda r: (r[1], r[2], r[3], -r[4]), reverse=True)
        base_id, cagr, sharpe, maxdd, turnover = candidates[0]
        return base_id, {
            "weighted_cagr": cagr,
            "weighted_sharpe": sharpe,
            "weighted_max_drawdown": maxdd,
            "weighted_turnover": turnover,
        }

    short = pick(TRACK_WEIGHTS["short_cycle_30_30_40"])
    mid = pick(TRACK_WEIGHTS["mid_cycle_30_40_30"])
    if not short or not mid:
        return {}
    return {
        "as_of": str(latest["sample_end"].max().date()),
        "tracks": {
            "short_cycle_30_30_40": {"weights": TRACK_WEIGHTS["short_cycle_30_30_40"], "winner": short[0], "metrics": short[1]},
            "mid_cycle_30_40_30": {"weights": TRACK_WEIGHTS["mid_cycle_30_40_30"], "winner": mid[0], "metrics": mid[1]},
        },
    }


WEIGHTED_WINNERS = load_weighted_winners()
SHORT_WINNER_ID = WEIGHTED_WINNERS.get("tracks", {}).get("short_cycle_30_30_40", {}).get("winner")
MID_WINNER_ID = WEIGHTED_WINNERS.get("tracks", {}).get("mid_cycle_30_40_30", {}).get("winner")


def is_short_winner(base_id: str) -> bool:
    return bool(SHORT_WINNER_ID) and base_id == SHORT_WINNER_ID and base_id != MID_WINNER_ID


def is_mid_winner(base_id: str) -> bool:
    return bool(MID_WINNER_ID) and base_id == MID_WINNER_ID and base_id != SHORT_WINNER_ID


def is_both_winner(base_id: str) -> bool:
    return bool(base_id) and base_id == SHORT_WINNER_ID and base_id == MID_WINNER_ID


def load_summary(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return RESULTS_DIR / f"{base_id}__{sample_tag}" / filename


def compute_window_metrics(equity: pd.DataFrame, monthly_returns: pd.DataFrame, turnover: pd.DataFrame) -> dict:
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
    return {
        "total_return": total_return,
        "cagr": cagr,
        "max_drawdown": max_drawdown,
        "annual_volatility": annual_volatility,
        "sharpe_ratio": sharpe_ratio,
        "average_annual_turnover": float(turnover["one_way_turnover"].mean() * 12) if not turnover.empty else np.nan,
    }


def load_static_window(base_id: str, sample_tag: str) -> tuple[pd.DataFrame, dict]:
    summary_path = RESULTS_DIR / base_id / "summary.json"
    equity_path = RESULTS_DIR / base_id / "equity_curve.csv"
    monthly_path = RESULTS_DIR / base_id / "monthly_returns.csv"
    turnover_path = RESULTS_DIR / base_id / "turnover.csv"

    summary = load_summary(summary_path)
    equity = pd.read_csv(equity_path, parse_dates=["date"])
    monthly_returns = pd.read_csv(monthly_path, parse_dates=["date"])
    turnover = pd.read_csv(turnover_path, parse_dates=["date"])

    if sample_tag == "since_2020_01":
        return equity, summary["metrics"]

    if sample_tag != "since_2023_01":
        raise FileNotFoundError(f"Static strategy {base_id} does not support {sample_tag}")

    sample_start = pd.Timestamp("2023-01-01")
    equity_window = equity[equity["date"] >= sample_start].copy()
    if equity_window.empty:
        raise FileNotFoundError(f"Static strategy {base_id} has no data for {sample_tag}")
    start_nav = float(equity_window.iloc[0]["nav"])
    equity_window["nav"] = equity_window["nav"] / start_nav
    equity_window["drawdown"] = equity_window["nav"] / equity_window["nav"].cummax() - 1.0
    monthly_window = monthly_returns[monthly_returns["date"] >= sample_start].copy()
    turnover_window = turnover[turnover["date"] >= sample_start].copy()
    return equity_window, compute_window_metrics(equity_window, monthly_window, turnover_window)


def load_strategy_window(config: dict, sample_tag: str) -> tuple[pd.DataFrame, dict]:
    if sample_tag not in config.get("available_sample_tags", {sample_tag}):
        raise FileNotFoundError(f"{config['label']} unavailable for {sample_tag}")
    if config.get("kind") == "static":
        return load_static_window(config["base_id"], sample_tag)

    summary = load_summary(build_result_path(config["base_id"], sample_tag, "summary.json"))
    equity = pd.read_csv(build_result_path(config["base_id"], sample_tag, "equity_curve.csv"), parse_dates=["date"])
    return equity, summary["metrics"]


def build_comparison_frame(sample_tag: str) -> pd.DataFrame:
    rows: list[dict] = []
    for config in STRATEGIES:
        try:
            _, metrics = load_strategy_window(config, sample_tag)
        except FileNotFoundError:
            continue
        rows.append(
            {
                "base_id": config["base_id"],
                "label": config["label"],
                "color": config["color"],
                "total_return": metrics["total_return"],
                "cagr": metrics["cagr"],
                "max_drawdown": metrics["max_drawdown"],
                "sharpe_ratio": metrics["sharpe_ratio"],
            }
        )
    return pd.DataFrame(rows)


def plot_nav_curves(ax: plt.Axes, sample_tag: str, title: str) -> None:
    for config in STRATEGIES:
        try:
            equity, _ = load_strategy_window(config, sample_tag)
        except FileNotFoundError:
            continue
        base_id = config["base_id"]
        highlight = base_id in {SHORT_WINNER_ID, MID_WINNER_ID}
        if is_mid_winner(base_id):
            linestyle = "-"
        elif is_short_winner(base_id):
            linestyle = "--"
        elif is_both_winner(base_id):
            linestyle = "-"
        else:
            linestyle = "-"
        ax.plot(
            equity["date"],
            equity["nav"],
            label=config["label"],
            color=config["color"],
            linewidth=2.8 if highlight else 1.8,
            alpha=1.0 if highlight else 0.9,
            linestyle=linestyle,
        )

    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_ylabel("NAV")
    ax.grid(alpha=0.25)


def plot_risk_return(ax: plt.Axes, frame: pd.DataFrame, title: str) -> None:
    for _, row in frame.iterrows():
        base_id = row.get("base_id", "")
        highlight = base_id in {SHORT_WINNER_ID, MID_WINNER_ID}
        marker = "o"
        if is_mid_winner(base_id) or is_both_winner(base_id):
            marker = "*"
        elif is_short_winner(base_id):
            marker = "D"
        ax.scatter(
            row["cagr"] * 100,
            row["max_drawdown"] * 100,
            s=260 if highlight else 140,
            color=row["color"],
            alpha=0.95,
            edgecolors="white",
            linewidths=1.2,
            marker=marker,
        )
        ax.annotate(
            row["label"],
            (row["cagr"] * 100, row["max_drawdown"] * 100),
            xytext=(8, 6),
            textcoords="offset points",
            fontsize=8.5,
        )

    ax.axvline(0, color="#cbd5e1", linewidth=1)
    ax.set_title(f"{title} Risk / Return", fontsize=12, fontweight="bold")
    ax.set_xlabel("CAGR (%)")
    ax.set_ylabel("Max DD (%)")
    ax.grid(alpha=0.25)


def plot_metric_table(ax: plt.Axes, frame: pd.DataFrame, title: str) -> None:
    table_frame = frame.copy()
    table_frame["total_return"] = (table_frame["total_return"] * 100).map(lambda x: f"{x:.1f}%")
    table_frame["cagr"] = (table_frame["cagr"] * 100).map(lambda x: f"{x:.2f}%")
    table_frame["max_drawdown"] = (table_frame["max_drawdown"] * 100).map(lambda x: f"{x:.2f}%")
    table_frame["sharpe_ratio"] = table_frame["sharpe_ratio"].map(lambda x: f"{x:.3f}")
    base_ids = table_frame["base_id"].astype(str).tolist()
    display_frame = table_frame[["label", "total_return", "cagr", "max_drawdown", "sharpe_ratio"]]
    display_frame.columns = ["Strategy", "Total Return", "CAGR", "Max DD", "Sharpe"]

    ax.axis("off")
    ax.set_title(f"{title} Metrics", fontsize=12, fontweight="bold", pad=8)
    table = ax.table(
        cellText=display_frame.values,
        colLabels=display_frame.columns,
        cellLoc="center",
        colLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.35)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#cbd5e1")
        if row == 0:
            cell.set_facecolor("#e2e8f0")
            cell.set_text_props(weight="bold")
        else:
            base_id = base_ids[row - 1] if 0 <= row - 1 < len(base_ids) else ""
            if base_id == MID_WINNER_ID:
                cell.set_facecolor("#fee2e2")
            if base_id == SHORT_WINNER_ID and SHORT_WINNER_ID != MID_WINNER_ID:
                cell.set_facecolor("#dbeafe")


def main() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    fig, axes = plt.subplots(
        3,
        len(SAMPLE_WINDOWS),
        figsize=(18, 12),
        constrained_layout=True,
        gridspec_kw={"height_ratios": [2.0, 1.4, 1.6]},
    )

    for col_idx, sample_window in enumerate(SAMPLE_WINDOWS):
        frame = build_comparison_frame(sample_window["sample_tag"])
        plot_nav_curves(axes[0, col_idx], sample_window["sample_tag"], sample_window["title"])
        plot_risk_return(axes[1, col_idx], frame, sample_window["short_label"])
        plot_metric_table(axes[2, col_idx], frame, sample_window["short_label"])

    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.02))
    fig.suptitle("aiinvestor Strategy Comparison Across 9Y / 6Y / 3Y Windows", fontsize=18, fontweight="bold")
    if WEIGHTED_WINNERS and SHORT_WINNER_ID and MID_WINNER_ID:
        short_metrics = WEIGHTED_WINNERS["tracks"]["short_cycle_30_30_40"]["metrics"]
        mid_metrics = WEIGHTED_WINNERS["tracks"]["mid_cycle_30_40_30"]["metrics"]
        short_label = STRATEGY_LABEL_BY_ID.get(SHORT_WINNER_ID, SHORT_WINNER_ID)
        mid_label = STRATEGY_LABEL_BY_ID.get(MID_WINNER_ID, MID_WINNER_ID)
        as_of = WEIGHTED_WINNERS.get("as_of", "n/a")
        note = (
            "Weighted multi-window winners (as of {as_of})\\n"
            "Short-cycle (30/30/40): {short_label}  "
            "wCAGR {scagr}, wSharpe {ssharpe:.3f}, wMaxDD {sdd}, wTurn {sturn:.2f}\\n"
            "Mid-cycle (30/40/30): {mid_label}  "
            "wCAGR {mcagr}, wSharpe {msharpe:.3f}, wMaxDD {mdd}, wTurn {mturn:.2f}"
        ).format(
            as_of=as_of,
            short_label=short_label,
            scagr=_fmt_pct(short_metrics.get("weighted_cagr")),
            ssharpe=float(short_metrics.get("weighted_sharpe")),
            sdd=_fmt_pct(short_metrics.get("weighted_max_drawdown")),
            sturn=float(short_metrics.get("weighted_turnover")),
            mid_label=mid_label,
            mcagr=_fmt_pct(mid_metrics.get("weighted_cagr")),
            msharpe=float(mid_metrics.get("weighted_sharpe")),
            mdd=_fmt_pct(mid_metrics.get("weighted_max_drawdown")),
            mturn=float(mid_metrics.get("weighted_turnover")),
        )
        fig.text(
            0.01,
            0.995,
            note,
            va="top",
            ha="left",
            fontsize=9.5,
            bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": "#cbd5e1", "alpha": 0.92},
        )
    fig.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")


if __name__ == "__main__":
    main()
