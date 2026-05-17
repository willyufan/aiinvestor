from __future__ import annotations

from pathlib import Path

import pandas as pd


def merge_latest_rows(
    new_frame: pd.DataFrame,
    output_path: Path,
    *,
    key_cols: list[str],
    sort_cols: list[str],
) -> pd.DataFrame:
    if new_frame.empty:
        return new_frame

    frames: list[pd.DataFrame] = []
    if output_path.exists():
        try:
            existing = pd.read_csv(output_path)
        except Exception:
            existing = pd.DataFrame()
        if not existing.empty:
            existing = existing.copy()
            existing["_merge_order"] = 0
            frames.append(existing)

    fresh = new_frame.copy()
    fresh["_merge_order"] = 1
    frames.append(fresh)

    merged = pd.concat(frames, ignore_index=True, sort=False)
    for col in key_cols:
        if col not in merged.columns:
            raise ValueError(f"Missing comparison key column: {col}")
        merged[col] = merged[col].astype(str)
    if "sample_end" in merged.columns:
        merged["_sample_end_sort"] = pd.to_datetime(merged["sample_end"], errors="coerce")
    else:
        merged["_sample_end_sort"] = pd.NaT

    merged = merged.sort_values(key_cols + ["_sample_end_sort", "_merge_order"])
    merged = merged.drop_duplicates(key_cols, keep="last")
    merged = merged.drop(columns=["_merge_order", "_sample_end_sort"], errors="ignore")

    existing_sort_cols = [col for col in sort_cols if col in merged.columns]
    if existing_sort_cols:
        ascending = [False if col in {"cagr", "sharpe_ratio", "max_drawdown"} else True for col in existing_sort_cols]
        merged = merged.sort_values(existing_sort_cols, ascending=ascending, na_position="last")
    return merged.reset_index(drop=True)
