from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "data_cache" / "mplconfig"))

import matplotlib
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt


RESULTS_DIR = ROOT / "results"
DOCS_DIR = ROOT / "docs"
OUTPUT_PATH = DOCS_DIR / "strategy_comparison.png"

SAMPLE_WINDOWS = [
    {"sample_tag": "since_2017_01", "title": "9Y Window (Since 2017-01)", "short_label": "2017-01"},
    {"sample_tag": "since_2020_01", "title": "6Y Window (Since 2020-01)", "short_label": "2020-01"},
    {"sample_tag": "since_2023_01", "title": "3Y Window (Since 2023-01)", "short_label": "2023-01"},
]

STRATEGIES = [
    {"base_id": "core_explore_80_20_total_mv_index_core", "label": "80/20 Index Core", "color": "#94a3b8"},
    {"base_id": "core_explore_80_20_total_mv_winner_core", "label": "80/20 Winner Core", "color": "#2563eb"},
    {
        "base_id": "core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp",
        "label": "80/20 Winner Core (Aggressive)",
        "color": "#dc2626",
    },
    {"base_id": "pure_core_growth_6", "label": "Pure Core 6", "color": "#7c3aed"},
]


def load_summary(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return RESULTS_DIR / f"{base_id}__{sample_tag}" / filename


def build_comparison_frame(sample_tag: str) -> pd.DataFrame:
    rows: list[dict] = []
    for config in STRATEGIES:
        summary = load_summary(build_result_path(config["base_id"], sample_tag, "summary.json"))
        metrics = summary["metrics"]
        rows.append(
            {
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
        equity = pd.read_csv(build_result_path(config["base_id"], sample_tag, "equity_curve.csv"), parse_dates=["date"])
        highlight = config["label"] == "80/20 Winner Core (Aggressive)"
        ax.plot(
            equity["date"],
            equity["nav"],
            label=config["label"],
            color=config["color"],
            linewidth=2.8 if highlight else 1.8,
            alpha=1.0 if highlight else 0.9,
        )

    ax.set_title(title, fontsize=13, fontweight="bold")
    ax.set_ylabel("NAV")
    ax.grid(alpha=0.25)


def plot_risk_return(ax: plt.Axes, frame: pd.DataFrame, title: str) -> None:
    for _, row in frame.iterrows():
        highlight = row["label"] == "80/20 Winner Core (Aggressive)"
        ax.scatter(
            row["cagr"] * 100,
            row["max_drawdown"] * 100,
            s=220 if highlight else 140,
            color=row["color"],
            alpha=0.95,
            edgecolors="white",
            linewidths=1.2,
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
    table_frame = table_frame[["label", "total_return", "cagr", "max_drawdown", "sharpe_ratio"]]
    table_frame.columns = ["Strategy", "Total Return", "CAGR", "Max DD", "Sharpe"]

    ax.axis("off")
    ax.set_title(f"{title} Metrics", fontsize=12, fontweight="bold", pad=8)
    table = ax.table(
        cellText=table_frame.values,
        colLabels=table_frame.columns,
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
    fig.legend(handles, labels, loc="upper center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.02))
    fig.suptitle("aiinvestor Strategy Comparison Across 9Y / 6Y / 3Y Windows", fontsize=18, fontweight="bold")
    fig.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")


if __name__ == "__main__":
    main()
