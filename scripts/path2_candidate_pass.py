from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd

from update_weighted_winners import _augment_with_synthetic_windows


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
DEFAULT_COMPARISON_CSV = RESULTS_DIR / "strategy_comparison_base_method.csv"
BACKTEST_SCRIPT_PATH = ROOT / "backtest_marketcap_etf.py"
DEFAULT_WRITE_JSON = RESULTS_DIR / "path2_candidate_pass.json"

WINDOW_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01")


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
    missing = wanted - set(result)
    if missing:
        raise RuntimeError(f"Unable to extract constants from {path}: {sorted(missing)}")
    return result


def load_path2_scan_rules(backtest_path: Path) -> tuple[list[str], list[str]]:
    consts = _parse_python_constants(backtest_path, ["PATH2_SCAN_BASE_PREFIXES", "PATH2_SCAN_VARIANT_IDS"])
    prefixes = [str(item) for item in consts.get("PATH2_SCAN_BASE_PREFIXES") or []]
    variant_ids = [str(item) for item in consts.get("PATH2_SCAN_VARIANT_IDS") or []]
    return prefixes, variant_ids


def _latest_per_strategy_window(frame: pd.DataFrame) -> pd.DataFrame:
    typed = frame.copy()
    typed["sample_end"] = pd.to_datetime(typed["sample_end"], errors="coerce")
    typed = typed.dropna(subset=["sample_end"])
    typed = typed.sort_values(["strategy_base_id", "sample_tag", "sample_end"])
    return typed.groupby(["strategy_base_id", "sample_tag"], as_index=False).tail(1)


def _matches_path2(base_id: str, prefixes: list[str], variant_ids: list[str]) -> bool:
    if any(base_id.startswith(prefix) for prefix in prefixes):
        return True
    return any(base_id.endswith(f"__{variant_id}") for variant_id in variant_ids)


def _compute_single_window_metrics(group: pd.DataFrame, sample_tag: str) -> dict[str, float]:
    row = group.loc[group["sample_tag"] == sample_tag]
    if row.empty:
        return {}
    return {
        "cagr": float(row["cagr"].iloc[0]),
        "sharpe": float(row["sharpe_ratio"].iloc[0]),
        "max_drawdown": float(row["max_drawdown"].iloc[0]),
        "turnover": float(row["average_annual_turnover"].iloc[0]),
        "total_return": float(row["total_return"].iloc[0]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Fast Path 2 candidate pass: scan independent Path 2 candidate universe.")
    parser.add_argument("--comparison-csv", type=Path, default=DEFAULT_COMPARISON_CSV)
    parser.add_argument("--backtest-script", type=Path, default=BACKTEST_SCRIPT_PATH)
    parser.add_argument("--write-json", type=Path, default=DEFAULT_WRITE_JSON)
    args = parser.parse_args()

    prefixes, variant_ids = load_path2_scan_rules(args.backtest_script)
    frame = pd.read_csv(args.comparison_csv)
    latest = _augment_with_synthetic_windows(_latest_per_strategy_window(frame))
    latest["strategy_base_id"] = latest["strategy_base_id"].astype(str)
    latest["sample_tag"] = latest["sample_tag"].astype(str)

    candidate_ids = sorted(
        {
            base_id
            for base_id in latest["strategy_base_id"].unique()
            if _matches_path2(str(base_id), prefixes, variant_ids)
        }
    )

    by_id = {str(base_id): group for base_id, group in latest.groupby("strategy_base_id")}
    window_winners: dict[str, dict[str, Any]] = {}
    ranked_candidates: dict[str, list[dict[str, Any]]] = {}

    for sample_tag in WINDOW_TAGS:
        candidates: list[tuple[str, dict[str, float]]] = []
        for base_id in candidate_ids:
            group = by_id.get(base_id, pd.DataFrame())
            tags = set(group["sample_tag"].astype(str)) if not group.empty else set()
            if sample_tag not in tags:
                continue
            metrics = _compute_single_window_metrics(group, sample_tag)
            if not metrics:
                continue
            candidates.append((base_id, metrics))
        candidates.sort(
            key=lambda item: (
                item[1]["cagr"],
                item[1]["sharpe"],
                item[1]["max_drawdown"],
                -item[1]["turnover"],
            ),
            reverse=True,
        )
        ranked_candidates[sample_tag] = [
            {"strategy_base_id": base_id, "metrics": metrics} for base_id, metrics in candidates[:10]
        ]
        if candidates:
            best_id, best_metrics = candidates[0]
            window_winners[sample_tag] = {
                "strategy_base_id": best_id,
                "metrics": best_metrics,
            }

    required_tags = set(WINDOW_TAGS)
    robust_candidates: list[tuple[str, dict[str, float]]] = []
    for base_id in candidate_ids:
        group = by_id.get(base_id, pd.DataFrame())
        tags = set(group["sample_tag"].astype(str)) if not group.empty else set()
        if not required_tags.issubset(tags):
            continue
        metrics_by_tag = {tag: _compute_single_window_metrics(group, tag) for tag in WINDOW_TAGS}
        cagr_values = [metrics_by_tag[tag]["cagr"] for tag in WINDOW_TAGS]
        sharpe_values = [metrics_by_tag[tag]["sharpe"] for tag in WINDOW_TAGS]
        maxdd_values = [metrics_by_tag[tag]["max_drawdown"] for tag in WINDOW_TAGS]
        turn_values = [metrics_by_tag[tag]["turnover"] for tag in WINDOW_TAGS]
        robust_candidates.append(
            (
                base_id,
                {
                    "cagr_mean": float(np.mean(cagr_values)),
                    "cagr_min": float(np.min(cagr_values)),
                    "sharpe_mean": float(np.mean(sharpe_values)),
                    "max_drawdown_worst": float(np.min(maxdd_values)),
                    "turnover_mean": float(np.mean(turn_values)),
                },
            )
        )
    robust_candidates.sort(
        key=lambda item: (
            item[1]["cagr_mean"],
            item[1]["cagr_min"],
            item[1]["sharpe_mean"],
            item[1]["max_drawdown_worst"],
            -item[1]["turnover_mean"],
        ),
        reverse=True,
    )

    payload = {
        "candidate_prefixes": prefixes,
        "candidate_variant_ids": variant_ids,
        "candidate_count": len(candidate_ids),
        "window_winners": window_winners,
        "robust_candidate": (
            {"strategy_base_id": robust_candidates[0][0], "metrics": robust_candidates[0][1]}
            if robust_candidates
            else None
        ),
        "ranked_candidates": ranked_candidates,
    }
    args.write_json.parent.mkdir(parents=True, exist_ok=True)
    args.write_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"[OK] path2 candidates={len(candidate_ids)} prefixes={prefixes} variants={variant_ids}")
    for sample_tag, winner in window_winners.items():
        metrics = winner["metrics"]
        print(
            f"[OK] {sample_tag}: {winner['strategy_base_id']} "
            f"(CAGR={metrics['cagr']*100:.2f}%, Sharpe={metrics['sharpe']:.4f}, "
            f"MaxDD={metrics['max_drawdown']*100:.2f}%, Turn={metrics['turnover']:.2f})"
        )
    if robust_candidates:
        rid, rmetrics = robust_candidates[0]
        print(
            f"[OK] robust: {rid} "
            f"(meanCAGR={rmetrics['cagr_mean']*100:.2f}%, minCAGR={rmetrics['cagr_min']*100:.2f}%)"
        )


if __name__ == "__main__":
    main()
