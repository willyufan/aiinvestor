from __future__ import annotations

from collections.abc import Collection

import numpy as np
import pandas as pd


HK_METRIC_COLUMNS = (
    "cagr",
    "sharpe_ratio",
    "max_drawdown",
    "average_annual_turnover",
    "total_return",
)
MAX_SAMPLE_END_STALENESS_DAYS = 21


def latest_per_strategy_window(frame: pd.DataFrame) -> pd.DataFrame:
    typed = frame.copy()
    typed["sample_end"] = pd.to_datetime(typed["sample_end"], errors="coerce")
    typed = typed.dropna(subset=["sample_end"])
    typed = typed.sort_values(["strategy_id", "sample_tag", "sample_end"])
    return typed.groupby(["strategy_id", "sample_tag"], as_index=False).tail(1)


def valid_hk_leaderboard_row(row: pd.Series) -> bool:
    try:
        metrics = [float(row.get(column, np.nan)) for column in HK_METRIC_COLUMNS]
    except (TypeError, ValueError):
        return False
    if not all(np.isfinite(value) for value in metrics):
        return False
    cagr, _sharpe, max_drawdown, turnover, total_return = metrics
    inactive = (
        abs(cagr) < 1e-12
        and abs(max_drawdown) < 1e-12
        and abs(turnover) < 1e-12
        and abs(total_return) < 1e-12
    )
    return not inactive


def valid_hk_leaderboard_rows(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return frame.copy()
    return frame[frame.apply(valid_hk_leaderboard_row, axis=1)].copy()


def prepare_hk_candidate_frames(
    frame: pd.DataFrame,
    *,
    archived_strategy_ids: Collection[str],
    max_staleness_days: int = MAX_SAMPLE_END_STALENESS_DAYS,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Timestamp, int]:
    """Return valid active catalog rows and the fresh subset used for ranking."""
    latest = latest_per_strategy_window(frame)
    latest["sample_tag"] = latest["sample_tag"].astype(str)
    latest["strategy_id"] = latest["strategy_id"].astype(str)
    latest["path"] = latest["path"].astype(str)
    latest = latest[~latest["strategy_id"].isin(archived_strategy_ids)].copy()
    if latest.empty:
        raise ValueError("no active HK Connect strategy-window rows")

    latest = valid_hk_leaderboard_rows(latest)
    if latest.empty:
        raise ValueError("no valid active HK Connect strategy-window rows")
    newest_sample_end = pd.Timestamp(latest["sample_end"].max())
    freshness_cutoff = newest_sample_end - pd.Timedelta(days=max_staleness_days)
    stale_row_count = int((latest["sample_end"] < freshness_cutoff).sum())
    ranking_latest = latest[latest["sample_end"] >= freshness_cutoff].copy()
    return latest, ranking_latest, freshness_cutoff, stale_row_count
