"""Shared helpers for collecting strategy ids from pipeline JSON / CSV files.

These three patterns were previously duplicated across:

- ``scripts/active_strategy_scope.py`` — feeds the refresh-only registry
- ``scripts/cleanup_backtest_results.py`` — protected-id list for safe deletes
- ``scripts/research_iteration_guard.py`` — coverage gate input

Centralising them avoids drift between live tracking, cleanup safety
nets, and the iteration guard. The contract intentionally stays small:
load JSON tolerantly, recursively pull strategy ids out of nested
structures, and rank a comparison CSV by the standard metric trio.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd


# Keys recognised when walking a nested JSON payload for strategy ids.
# Keeping this as a frozenset doc'd in one place ensures all collectors
# agree on which fields contribute (winner / raw_winner / strategy_id /
# strategy_base_id) — adding a new key here flows to every caller.
ID_KEYS = frozenset({"winner", "raw_winner", "strategy_id", "strategy_base_id"})


def load_json(path: Path, default: Any = None) -> Any:
    """Read a JSON file, returning ``default`` (or ``{}``) on any failure.

    Used by callers that need to merge several optional artifacts (some
    files may not exist yet on a fresh checkout). Swallowing
    JSONDecodeError matches the pre-existing scripts' behaviour where a
    partially-written file should not abort an entire refresh pass.
    """
    if default is None:
        default = {}
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return default


def collect_ids(obj: Any, target: set[str]) -> None:
    """Walk ``obj`` and add string values that appear under ``ID_KEYS``.

    Pure side-effect on ``target`` so callers can accumulate ids from
    multiple sources into one set. Non-string and empty values are
    silently skipped to avoid corrupting downstream lookups.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in ID_KEYS and isinstance(value, str) and value:
                target.add(value)
            else:
                collect_ids(value, target)
    elif isinstance(obj, list):
        for item in obj:
            collect_ids(item, target)


def collect_csv_topn(
    path: Path,
    *,
    id_col: str,
    target: set[str],
    top_n: int = 5,
) -> None:
    """Read a comparison CSV and add the top ``top_n`` ``id_col`` values
    per (path / strategy_kind / pool_id when present) + sample_tag group
    into ``target``.

    Sort order is descending on (cagr, sharpe_ratio, max_drawdown). All
    three benefit from descending — higher CAGR / Sharpe is better, and
    less-negative max_drawdown sorts higher under descending order. The
    function is a no-op when ``top_n <= 0``, the file is missing, or the
    CSV lacks the required ``id_col`` / ``sample_tag`` columns, so
    callers can use it unconditionally during pipeline init.
    """
    if top_n <= 0 or not path.exists():
        return
    try:
        frame = pd.read_csv(path)
    except Exception:
        return
    if frame.empty or id_col not in frame.columns or "sample_tag" not in frame.columns:
        return

    group_cols = ["sample_tag"]
    for optional in ("path", "strategy_kind", "pool_id"):
        if optional in frame.columns:
            group_cols.insert(0, optional)

    sort_cols = [col for col in ("cagr", "sharpe_ratio", "max_drawdown") if col in frame.columns]
    if not sort_cols:
        return
    working = frame.copy()
    for col in sort_cols:
        working[col] = pd.to_numeric(working[col], errors="coerce")
    ascending = [False] * len(sort_cols)
    for _, group in working.groupby(group_cols, dropna=False):
        ranked = group.sort_values(sort_cols, ascending=ascending, na_position="last").head(top_n)
        for value in ranked[id_col].dropna().astype(str):
            if value:
                target.add(value)
