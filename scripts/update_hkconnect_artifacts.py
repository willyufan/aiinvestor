from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "data_cache" / "mplconfig"))

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle


RESULTS_DIR = ROOT / "results_hkconnect"
DOCS_DIR = ROOT / "docs"
COMPARISON_CSV = RESULTS_DIR / "strategy_comparison_hkconnect.csv"
TRACKED_JSON = RESULTS_DIR / "tracked_winners_hkconnect.json"
OUTPUT_PATHS = {
    "path1": DOCS_DIR / "strategy_comparison_hkconnect_path1.png",
    "path2": DOCS_DIR / "strategy_comparison_hkconnect_path2.png",
    "path3": DOCS_DIR / "strategy_comparison_hkconnect_path3.png",
}
PATH_NAMES = ("path1", "path2", "path3")

WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01")
WINDOW_LABELS = {
    "since_2017_01": "2017",
    "since_2020_01": "2020",
    "since_2023_01": "2023",
    "since_2025_01": "2025",
}
PATH_TITLES = {
    "path1": "HK Connect Path 1 Comparison",
    "path2": "HK Connect Path 2 Comparison",
    "path3": "HK Connect Path 3 Comparison",
}


def _configure_matplotlib_fonts() -> None:
    candidates = [
        "PingFang SC",
        "Heiti SC",
        "Songti SC",
        "STHeiti",
        "Noto Sans CJK SC",
        "Noto Sans SC",
        "Microsoft YaHei",
        "SimHei",
        "Arial Unicode MS",
    ]
    available = {font.name for font in font_manager.fontManager.ttflist}
    chosen = next((name for name in candidates if name in available), None)
    if chosen:
        matplotlib.rcParams["font.family"] = "sans-serif"
        matplotlib.rcParams["font.sans-serif"] = [chosen, "DejaVu Sans"]
    matplotlib.rcParams["axes.unicode_minus"] = False


def _date_text(value: Any) -> str:
    parsed = pd.to_datetime(value, errors="coerce")
    if pd.isna(parsed):
        return str(value)
    return str(parsed.date())


def _latest_per_strategy_window(frame: pd.DataFrame) -> pd.DataFrame:
    typed = frame.copy()
    typed["sample_end"] = pd.to_datetime(typed["sample_end"], errors="coerce")
    typed = typed.dropna(subset=["sample_end"])
    typed = typed.sort_values(["strategy_id", "sample_tag", "sample_end"])
    return typed.groupby(["strategy_id", "sample_tag"], as_index=False).tail(1)


def _metric_row(row: pd.Series) -> dict[str, Any]:
    return {
        "sample_start": _date_text(row.get("sample_start")),
        "sample_end": _date_text(row.get("sample_end")),
        "total_return": float(row["total_return"]),
        "cagr": float(row["cagr"]),
        "max_drawdown": float(row["max_drawdown"]),
        "sharpe_ratio": float(row["sharpe_ratio"]),
        "average_annual_turnover": float(row["average_annual_turnover"]),
    }


def _short_label(strategy_id: str) -> str:
    label = strategy_id
    for prefix in ("hkconnect_path1_", "hkconnect_path2_", "hkconnect_path3_"):
        if label.startswith(prefix):
            label = label[len(prefix) :]
    return label.replace("_", "\n")


def _pick_winner(subset: pd.DataFrame) -> pd.Series:
    ranked = subset.sort_values(
        ["cagr", "sharpe_ratio", "max_drawdown", "average_annual_turnover"],
        ascending=[False, False, False, True],
    )
    return ranked.iloc[0]


def _pick_robust(subset: pd.DataFrame) -> tuple[str, dict[str, float]]:
    rows: list[tuple[str, dict[str, float]]] = []
    for strategy_id, group in subset.groupby("strategy_id"):
        tags = set(group["sample_tag"].astype(str))
        if not set(WINDOW_TAGS).issubset(tags):
            continue
        tracked = group[group["sample_tag"].isin(WINDOW_TAGS)].copy()
        rows.append(
            (
                str(strategy_id),
                {
                    "cagr_mean": float(tracked["cagr"].mean()),
                    "cagr_min": float(tracked["cagr"].min()),
                    "sharpe_mean": float(tracked["sharpe_ratio"].mean()),
                    "max_drawdown_worst": float(tracked["max_drawdown"].min()),
                    "turnover_mean": float(tracked["average_annual_turnover"].mean()),
                },
            )
        )
    if not rows:
        raise RuntimeError("No HK Connect strategy has all tracked windows.")
    rows.sort(
        key=lambda item: (
            item[1]["cagr_mean"],
            item[1]["cagr_min"],
            item[1]["sharpe_mean"],
            item[1]["max_drawdown_worst"],
            -item[1]["turnover_mean"],
        ),
        reverse=True,
    )
    return rows[0]


def _build_payload(latest: pd.DataFrame) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "as_of": _date_text(latest["sample_end"].max()),
        "window_tags": list(WINDOW_TAGS),
        "tracks": {path_name: {} for path_name in PATH_NAMES},
        "strategies": {},
    }

    for strategy_id, group in latest.groupby("strategy_id"):
        last_row = group.sort_values("sample_end").iloc[-1]
        payload["strategies"][str(strategy_id)] = {
            "strategy_name": str(last_row["strategy_name"]),
            "path": str(last_row["path"]),
            "candidate_family": str(last_row["candidate_family"]),
            "rebalance_frequency": str(last_row["rebalance_frequency"]),
            "short_label": _short_label(str(strategy_id)),
            "windows": {
                str(row["sample_tag"]): _metric_row(row)
                for _, row in group.sort_values("sample_tag").iterrows()
            },
        }

    for path_name in PATH_NAMES:
        subset = latest[latest["path"] == path_name].copy()
        if subset.empty:
            continue
        for sample_tag in WINDOW_TAGS:
            sample_df = subset[subset["sample_tag"] == sample_tag]
            if sample_df.empty:
                continue
            row = _pick_winner(sample_df)
            payload["tracks"][path_name][sample_tag] = {
                "winner": str(row["strategy_id"]),
                "metrics": _metric_row(row),
            }
        robust_id, robust_metrics = _pick_robust(subset)
        payload["tracks"][path_name]["robust_candidate"] = {
            "strategy_id": robust_id,
            "metrics": robust_metrics,
        }

    return payload


def _score_for_order(frame: pd.DataFrame, strategy_id: str) -> tuple[float, float, float]:
    row = frame.loc[strategy_id]
    cagr_2020 = float(row.get("since_2020_01", np.nan))
    cagr_2023 = float(row.get("since_2023_01", np.nan))
    cagr_2017 = float(row.get("since_2017_01", np.nan))
    score = (
        (0.60 * cagr_2020 if np.isfinite(cagr_2020) else 0.0)
        + (0.30 * cagr_2023 if np.isfinite(cagr_2023) else 0.0)
        + (0.10 * cagr_2017 if np.isfinite(cagr_2017) else 0.0)
    )
    return score, cagr_2020 if np.isfinite(cagr_2020) else -999.0, cagr_2023 if np.isfinite(cagr_2023) else -999.0


def _render_chart(latest: pd.DataFrame, payload: dict[str, Any], path_name: str) -> None:
    subset = latest[(latest["path"] == path_name) & (latest["sample_tag"].isin(WINDOW_TAGS))].copy()
    if subset.empty:
        return

    pivot = subset.pivot(index="strategy_id", columns="sample_tag", values="cagr").reindex(columns=WINDOW_TAGS) * 100.0
    strategy_ids = sorted(pivot.index.tolist(), key=lambda sid: _score_for_order(pivot, sid), reverse=True)
    pivot = pivot.loc[strategy_ids]

    values = pivot.to_numpy(dtype=float)
    finite_values = values[np.isfinite(values)]
    vmin = float(np.min(finite_values)) if finite_values.size else 0.0
    vmax = float(np.max(finite_values)) if finite_values.size else 1.0
    if np.isclose(vmin, vmax):
        vmax = vmin + 1.0

    fig_height = max(4.8, 1.05 * len(strategy_ids) + 2.0)
    fig, ax = plt.subplots(figsize=(11.0, fig_height))
    heatmap = ax.imshow(values, aspect="auto", cmap="YlGnBu", vmin=vmin, vmax=vmax)

    ax.set_xticks(range(len(WINDOW_TAGS)), [WINDOW_LABELS[tag] for tag in WINDOW_TAGS])
    ax.set_yticks(
        range(len(strategy_ids)),
        [payload["strategies"][strategy_id]["short_label"] for strategy_id in strategy_ids],
    )
    ax.set_title(f"{PATH_TITLES[path_name]} (cell = CAGR, %)", pad=14)

    threshold = vmin + (vmax - vmin) * 0.55
    for row_idx, strategy_id in enumerate(strategy_ids):
        for col_idx, sample_tag in enumerate(WINDOW_TAGS):
            value = values[row_idx, col_idx]
            text = "--" if not np.isfinite(value) else f"{value:.1f}%"
            color = "white" if np.isfinite(value) and value >= threshold else "#111827"
            is_winner = payload["tracks"][path_name].get(sample_tag, {}).get("winner") == strategy_id
            ax.text(
                col_idx,
                row_idx,
                text,
                ha="center",
                va="center",
                fontsize=10,
                color=color,
                fontweight="bold" if is_winner else "normal",
            )
            if is_winner:
                ax.add_patch(
                    Rectangle(
                        (col_idx - 0.5, row_idx - 0.5),
                        1.0,
                        1.0,
                        fill=False,
                        edgecolor="#dc2626",
                        linewidth=2.2,
                    )
                )

    cbar = fig.colorbar(heatmap, ax=ax, fraction=0.025, pad=0.02)
    cbar.set_label("CAGR (%)")

    robust = payload["tracks"][path_name]["robust_candidate"]
    robust_text = (
        f"Robust: {payload['strategies'][robust['strategy_id']]['short_label'].replace(chr(10), ' / ')} | "
        f"mean CAGR {robust['metrics']['cagr_mean'] * 100:.2f}% | "
        f"min CAGR {robust['metrics']['cagr_min'] * 100:.2f}%"
    )
    winners_text = "; ".join(
        f"{WINDOW_LABELS[tag]}={payload['strategies'][payload['tracks'][path_name][tag]['winner']]['short_label'].replace(chr(10), '/')}"
        for tag in WINDOW_TAGS
        if tag in payload["tracks"][path_name]
    )
    footnote = (
        f"{robust_text}\n"
        f"Winners: {winners_text}\n"
        "2026 window is observation-only and is omitted from the tracked-winner heatmap."
    )
    fig.text(0.02, 0.02, footnote, ha="left", va="bottom", fontsize=9)
    fig.tight_layout(rect=(0.0, 0.08, 1.0, 1.0))
    OUTPUT_PATHS[path_name].parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATHS[path_name], dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    if not COMPARISON_CSV.exists():
        raise FileNotFoundError(f"Missing HK Connect comparison CSV: {COMPARISON_CSV}")

    _configure_matplotlib_fonts()
    frame = pd.read_csv(COMPARISON_CSV)
    latest = _latest_per_strategy_window(frame)
    latest["sample_tag"] = latest["sample_tag"].astype(str)
    latest["strategy_id"] = latest["strategy_id"].astype(str)
    latest["path"] = latest["path"].astype(str)

    payload = _build_payload(latest)
    TRACKED_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for path_name in PATH_NAMES:
        _render_chart(latest, payload, path_name)

    print(f"[OK] wrote {TRACKED_JSON}")
    for path_name, output_path in OUTPUT_PATHS.items():
        print(f"[OK] wrote {path_name} chart: {output_path}")


if __name__ == "__main__":
    main()
