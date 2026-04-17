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


STRATEGIES = [
    {
        "label": "Large Cap Static",
        "summary": RESULTS_DIR / "large_cap_pool" / "summary.json",
        "equity": RESULTS_DIR / "large_cap_pool" / "equity_curve.csv",
        "color": "#0f766e",
    },
    {
        "label": "Kechuang Static",
        "summary": RESULTS_DIR / "kechuang_xuangu" / "summary.json",
        "equity": RESULTS_DIR / "kechuang_xuangu" / "equity_curve.csv",
        "color": "#1d4ed8",
    },
    {
        "label": "80/20 Index Core",
        "summary": RESULTS_DIR / "core_explore_80_20_total_mv_index_core" / "summary.json",
        "equity": RESULTS_DIR / "core_explore_80_20_total_mv_index_core" / "equity_curve.csv",
        "color": "#94a3b8",
    },
    {
        "label": "80/20 Winner Core (Aggressive)",
        "summary": RESULTS_DIR / "core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp" / "summary.json",
        "equity": RESULTS_DIR / "core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp" / "equity_curve.csv",
        "color": "#dc2626",
    },
    {
        "label": "Pure Core 6",
        "summary": RESULTS_DIR / "pure_core_growth_6" / "summary.json",
        "equity": RESULTS_DIR / "pure_core_growth_6" / "equity_curve.csv",
        "color": "#7c3aed",
    },
]


def load_summary(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_comparison_frame() -> pd.DataFrame:
    rows: list[dict] = []
    for config in STRATEGIES:
        summary = load_summary(config["summary"])
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


def plot_nav_curves(ax: plt.Axes) -> None:
    for config in STRATEGIES:
        equity = pd.read_csv(config["equity"], parse_dates=["date"])
        ax.plot(
            equity["date"],
            equity["nav"],
            label=config["label"],
            color=config["color"],
            linewidth=2.6 if config["label"] == "80/20 Winner Core (Aggressive)" else 1.8,
            alpha=1.0 if config["label"] == "80/20 Winner Core (Aggressive)" else 0.9,
        )

    ax.set_title("NAV Comparison (2020-01-01 to 2026-04-16)", fontsize=14, fontweight="bold")
    ax.set_ylabel("NAV")
    ax.grid(alpha=0.25)
    ax.legend(loc="upper left", ncol=2, frameon=False)


def plot_risk_return(ax: plt.Axes, frame: pd.DataFrame) -> None:
    for _, row in frame.iterrows():
        ax.scatter(
            row["cagr"] * 100,
            row["max_drawdown"] * 100,
            s=220 if row["label"] == "80/20 Winner Core (Aggressive)" else 140,
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
            fontsize=9,
        )

    ax.axvline(0, color="#cbd5e1", linewidth=1)
    ax.set_title("Risk / Return Positioning", fontsize=14, fontweight="bold")
    ax.set_xlabel("CAGR (%)")
    ax.set_ylabel("Max Drawdown (%)")
    ax.grid(alpha=0.25)


def plot_metric_table(ax: plt.Axes, frame: pd.DataFrame) -> None:
    table_frame = frame.copy()
    table_frame["total_return"] = (table_frame["total_return"] * 100).map(lambda x: f"{x:.2f}%")
    table_frame["cagr"] = (table_frame["cagr"] * 100).map(lambda x: f"{x:.2f}%")
    table_frame["max_drawdown"] = (table_frame["max_drawdown"] * 100).map(lambda x: f"{x:.2f}%")
    table_frame["sharpe_ratio"] = table_frame["sharpe_ratio"].map(lambda x: f"{x:.3f}")
    table_frame = table_frame[["label", "total_return", "cagr", "max_drawdown", "sharpe_ratio"]]
    table_frame.columns = ["Strategy", "Total Return", "CAGR", "Max DD", "Sharpe"]

    ax.axis("off")
    table = ax.table(
        cellText=table_frame.values,
        colLabels=table_frame.columns,
        cellLoc="center",
        colLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.4)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#cbd5e1")
        if row == 0:
            cell.set_facecolor("#e2e8f0")
            cell.set_text_props(weight="bold")


def main() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    frame = build_comparison_frame()

    plt.style.use("seaborn-v0_8-whitegrid")
    fig = plt.figure(figsize=(14, 10), constrained_layout=True)
    grid = fig.add_gridspec(3, 1, height_ratios=[2.0, 1.4, 1.2])

    ax_nav = fig.add_subplot(grid[0, 0])
    ax_scatter = fig.add_subplot(grid[1, 0])
    ax_table = fig.add_subplot(grid[2, 0])

    plot_nav_curves(ax_nav)
    plot_risk_return(ax_scatter, frame)
    plot_metric_table(ax_table, frame)

    fig.suptitle("aiinvestor Strategy Comparison", fontsize=18, fontweight="bold")
    fig.savefig(OUTPUT_PATH, dpi=180, bbox_inches="tight")


if __name__ == "__main__":
    main()
