from __future__ import annotations

from typing import Any

from scripts.results_layout import (
    A_SHARE_SCOPE,
    HKCONNECT_SCOPE,
    RESULTS_LIVE_DIR,
    existing_research_file,
    normalize_market_scope,
)
from scripts.winner_id_utils import collect_csv_topn, collect_ids, load_json


def _collect_live_registry_ids(market_scope: str, target: set[str]) -> None:
    payload = load_json(RESULTS_LIVE_DIR / "strategy_registry.json")
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
        collect_ids(leaderboards.get(market_scope) or {}, target)


def _collect_core_active_ids(target: set[str]) -> None:
    payload = load_json(existing_research_file("core_active_registry.json"))
    if not isinstance(payload, dict):
        return
    for key in ("current_winner_ids", "current_refresh_only_ids"):
        for value in payload.get(key) or []:
            if value:
                target.add(str(value))
    collect_ids(payload.get("strategies") or [], target)
    collect_ids(payload.get("refresh_only_strategies") or [], target)


def collect_ashare_refresh_active_ids(*, include_top_n: int = 5) -> set[str]:
    strategy_ids: set[str] = set()
    collect_ids(load_json(existing_research_file("weighted_track_winners.json")), strategy_ids)
    _collect_core_active_ids(strategy_ids)
    _collect_live_registry_ids(A_SHARE_SCOPE, strategy_ids)
    collect_csv_topn(
        existing_research_file("strategy_comparison_base_method.csv"),
        id_col="strategy_base_id",
        target=strategy_ids,
        top_n=include_top_n,
    )
    return {strategy_id for strategy_id in strategy_ids if strategy_id}


def collect_hkconnect_refresh_active_ids(*, include_top_n: int = 5) -> set[str]:
    strategy_ids: set[str] = set()
    collect_ids(
        load_json(existing_research_file("tracked_winners_hkconnect.json", market_scope=HKCONNECT_SCOPE)),
        strategy_ids,
    )
    _collect_live_registry_ids(HKCONNECT_SCOPE, strategy_ids)
    collect_csv_topn(
        existing_research_file("strategy_comparison_hkconnect.csv", market_scope=HKCONNECT_SCOPE),
        id_col="strategy_id",
        target=strategy_ids,
        top_n=include_top_n,
    )
    return {strategy_id for strategy_id in strategy_ids if strategy_id}
