from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

from scripts.results_layout import (
    A_SHARE_SCOPE,
    HKCONNECT_SCOPE,
    RESULTS_LIVE_DIR,
    existing_research_file,
    normalize_market_scope,
)


ID_KEYS = {"winner", "raw_winner", "strategy_id", "strategy_base_id"}


def _load_json(path: Path) -> Any:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _collect_ids(obj: Any, target: set[str]) -> None:
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in ID_KEYS and isinstance(value, str) and value:
                target.add(value)
            else:
                _collect_ids(value, target)
    elif isinstance(obj, list):
        for item in obj:
            _collect_ids(item, target)


def _collect_live_registry_ids(market_scope: str, target: set[str]) -> None:
    payload = _load_json(RESULTS_LIVE_DIR / "strategy_registry.json")
    if not isinstance(payload, dict):
        return

    def add_items(items: Any) -> None:
        if not isinstance(items, list):
            return
        for item in items:
            if not isinstance(item, dict):
                continue
            scope = normalize_market_scope(str(item.get("market_scope") or A_SHARE_SCOPE))
            if scope != market_scope:
                continue
            strategy_id = str(item.get("strategy_id") or item.get("strategy_base_id") or "")
            if strategy_id:
                target.add(strategy_id)

    add_items(payload.get("strategies"))
    add_items(payload.get("core_active_strategies"))
    leaderboards = payload.get("winner_leaderboards") or {}
    if isinstance(leaderboards, dict):
        _collect_ids(leaderboards.get(market_scope) or {}, target)


def _collect_csv_topn(path: Path, *, id_col: str, target: set[str], top_n: int = 5) -> None:
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
    ascending = [False for _ in sort_cols]
    for _, group in working.groupby(group_cols, dropna=False):
        ranked = group.sort_values(sort_cols, ascending=ascending, na_position="last").head(top_n)
        target.update(value for value in ranked[id_col].dropna().astype(str) if value)


def _collect_core_active_ids(target: set[str]) -> None:
    payload = _load_json(existing_research_file("core_active_registry.json"))
    if not isinstance(payload, dict):
        return
    for key in ("current_winner_ids", "current_refresh_only_ids"):
        for value in payload.get(key) or []:
            if value:
                target.add(str(value))
    _collect_ids(payload.get("strategies") or [], target)
    _collect_ids(payload.get("refresh_only_strategies") or [], target)


def collect_ashare_refresh_active_ids(*, include_top_n: int = 5) -> set[str]:
    strategy_ids: set[str] = set()
    _collect_ids(_load_json(existing_research_file("weighted_track_winners.json")), strategy_ids)
    _collect_core_active_ids(strategy_ids)
    _collect_live_registry_ids(A_SHARE_SCOPE, strategy_ids)
    _collect_csv_topn(
        existing_research_file("strategy_comparison_base_method.csv"),
        id_col="strategy_base_id",
        target=strategy_ids,
        top_n=include_top_n,
    )
    return {strategy_id for strategy_id in strategy_ids if strategy_id}


def collect_hkconnect_refresh_active_ids(*, include_top_n: int = 5) -> set[str]:
    strategy_ids: set[str] = set()
    _collect_ids(
        _load_json(existing_research_file("tracked_winners_hkconnect.json", market_scope=HKCONNECT_SCOPE)),
        strategy_ids,
    )
    _collect_live_registry_ids(HKCONNECT_SCOPE, strategy_ids)
    _collect_csv_topn(
        existing_research_file("strategy_comparison_hkconnect.csv", market_scope=HKCONNECT_SCOPE),
        id_col="strategy_id",
        target=strategy_ids,
        top_n=include_top_n,
    )
    return {strategy_id for strategy_id in strategy_ids if strategy_id}
