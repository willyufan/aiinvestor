from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
DEFAULT_OUTPUT_PATH = RESULTS_DIR / "strategy_comparison_base_method.csv"


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        payload = json.load(f)
    if not isinstance(payload, dict):
        raise ValueError(f"Unexpected JSON shape in {path}")
    return payload


def _safe_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return float("nan")


def _build_row(summary: dict[str, Any]) -> dict[str, Any] | None:
    sample_tag = summary.get("sample_tag")
    if not sample_tag:
        return None

    metrics = summary.get("metrics") or {}
    if not isinstance(metrics, dict):
        metrics = {}

    return {
        "strategy_id": summary.get("strategy_id", ""),
        "strategy_base_id": summary.get("strategy_base_id", summary.get("strategy_id", "")),
        "strategy_name": summary.get("strategy_name", ""),
        "strategy_base_name": summary.get("strategy_base_name", summary.get("strategy_name", "")),
        "strategy_kind": summary.get("strategy_kind", "core_explore"),
        "pool_id": summary.get("pool_id", ""),
        "pool_name": summary.get("pool_name", ""),
        "sample_start": summary.get("sample_start", ""),
        "sample_end": summary.get("sample_end", ""),
        "sample_tag": summary.get("sample_tag", ""),
        "sample_label": summary.get("sample_label", ""),
        "sample_short_label": summary.get("sample_short_label", ""),
        "is_primary_sample": bool(summary.get("is_primary_sample", False)),
        "stock_count": int(summary.get("stock_count", 0) or 0),
        "base_weight_method": summary.get("base_weight_method", ""),
        "base_weight_name": summary.get("base_weight_name", ""),
        "core_source_mode": summary.get("core_source_mode", ""),
        "core_source_name": summary.get("core_source_name", ""),
        "core_ratio": _safe_float(summary.get("core_ratio")),
        "explore_ratio": _safe_float(summary.get("explore_ratio")),
        "pure_core_max_holdings": int(summary.get("pure_core_max_holdings", 0) or 0),
        "total_return": _safe_float(metrics.get("total_return")),
        "cagr": _safe_float(metrics.get("cagr")),
        "max_drawdown": _safe_float(metrics.get("max_drawdown")),
        "annual_volatility": _safe_float(metrics.get("annual_volatility")),
        "sharpe_ratio": _safe_float(metrics.get("sharpe_ratio")),
        "monthly_win_rate": _safe_float(metrics.get("monthly_win_rate")),
        "average_annual_turnover": _safe_float(metrics.get("average_annual_turnover")),
        "cumulative_trading_cost": _safe_float(metrics.get("cumulative_trading_cost")),
    }


def rebuild(*, windows: set[str]) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for summary_path in RESULTS_DIR.rglob("summary.json"):
        summary = _load_json(summary_path)
        sample_tag = str(summary.get("sample_tag") or "")
        if sample_tag not in windows:
            continue
        row = _build_row(summary)
        if row is None:
            continue
        rows.append(row)

    frame = pd.DataFrame(rows)
    if frame.empty:
        return frame

    frame["sample_end"] = pd.to_datetime(frame["sample_end"], errors="coerce")
    frame = frame.dropna(subset=["sample_end"])
    frame = frame.sort_values(["strategy_base_id", "sample_tag", "sample_end"])
    return frame.reset_index(drop=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild strategy comparison CSV from cached summary.json outputs.")
    parser.add_argument(
        "--windows",
        nargs="+",
        default=["since_2017_01", "since_2020_01", "since_2023_01"],
        help="Which sample_tag windows to include.",
    )
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    parser.add_argument("--also-write", type=Path, nargs="*", default=[RESULTS_DIR / "strategy_comparison.csv"])
    args = parser.parse_args()

    frame = rebuild(windows=set(map(str, args.windows)))
    if frame.empty:
        raise SystemExit("[Error] No summary.json found for the requested windows.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output, index=False)
    for extra in args.also_write:
        extra.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(extra, index=False)

    unique_base = frame["strategy_base_id"].astype(str).nunique()
    print(f"[OK] Wrote {args.output} ({len(frame)} rows, {unique_base} base strategies)")
    for extra in args.also_write:
        print(f"[OK] Wrote {extra}")


if __name__ == "__main__":
    main()

