from __future__ import annotations

from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]

RESULTS_DIR = ROOT / "results"
RESULTS_BACKTESTS_DIR = RESULTS_DIR / "backtests"
RESULTS_RESEARCH_DIR = RESULTS_DIR / "research"
RESULTS_LIVE_DIR = RESULTS_DIR / "live"

A_SHARE_SCOPE = "a_share"
HKCONNECT_SCOPE = "hkconnect"
MARKET_SCOPES = (A_SHARE_SCOPE, HKCONNECT_SCOPE)

LEGACY_A_SHARE_RESULTS_DIR = RESULTS_DIR
LEGACY_HKCONNECT_RESULTS_DIR = ROOT / "results_hkconnect"


def normalize_market_scope(market_scope: str | None) -> str:
    scope = str(market_scope or A_SHARE_SCOPE)
    return scope if scope in MARKET_SCOPES else A_SHARE_SCOPE


def market_backtests_dir(market_scope: str | None = A_SHARE_SCOPE) -> Path:
    return RESULTS_BACKTESTS_DIR / normalize_market_scope(market_scope)


def market_research_dir(market_scope: str | None = A_SHARE_SCOPE) -> Path:
    return RESULTS_RESEARCH_DIR / normalize_market_scope(market_scope)


def legacy_market_results_dir(market_scope: str | None = A_SHARE_SCOPE) -> Path:
    return LEGACY_HKCONNECT_RESULTS_DIR if normalize_market_scope(market_scope) == HKCONNECT_SCOPE else LEGACY_A_SHARE_RESULTS_DIR


def strategy_result_dir(strategy_id: str, sample_tag: str | None = None, *, market_scope: str | None = A_SHARE_SCOPE) -> Path:
    leaf = f"{strategy_id}__{sample_tag}" if sample_tag else str(strategy_id)
    return market_backtests_dir(market_scope) / leaf


def legacy_strategy_result_dir(strategy_id: str, sample_tag: str | None = None, *, market_scope: str | None = A_SHARE_SCOPE) -> Path:
    leaf = f"{strategy_id}__{sample_tag}" if sample_tag else str(strategy_id)
    return legacy_market_results_dir(market_scope) / leaf


def candidate_strategy_result_dirs(
    strategy_id: str,
    sample_tag: str | None = None,
    *,
    market_scope: str | None = A_SHARE_SCOPE,
) -> list[Path]:
    new_dir = strategy_result_dir(strategy_id, sample_tag, market_scope=market_scope)
    legacy_dir = legacy_strategy_result_dir(strategy_id, sample_tag, market_scope=market_scope)
    if new_dir == legacy_dir:
        return [new_dir]
    return [new_dir, legacy_dir]


def existing_strategy_result_dir(
    strategy_id: str,
    sample_tag: str | None = None,
    *,
    market_scope: str | None = A_SHARE_SCOPE,
) -> Path:
    for path in candidate_strategy_result_dirs(strategy_id, sample_tag, market_scope=market_scope):
        if path.exists():
            return path
    return strategy_result_dir(strategy_id, sample_tag, market_scope=market_scope)


def strategy_result_file(
    strategy_id: str,
    sample_tag: str,
    filename: str,
    *,
    market_scope: str | None = A_SHARE_SCOPE,
) -> Path:
    return strategy_result_dir(strategy_id, sample_tag, market_scope=market_scope) / filename


def existing_strategy_result_file(
    strategy_id: str,
    sample_tag: str,
    filename: str,
    *,
    market_scope: str | None = A_SHARE_SCOPE,
) -> Path:
    for result_dir in candidate_strategy_result_dirs(strategy_id, sample_tag, market_scope=market_scope):
        path = result_dir / filename
        if path.exists():
            return path
    return strategy_result_file(strategy_id, sample_tag, filename, market_scope=market_scope)


def research_file(filename: str, *, market_scope: str | None = A_SHARE_SCOPE) -> Path:
    return market_research_dir(market_scope) / filename


def legacy_research_file(filename: str, *, market_scope: str | None = A_SHARE_SCOPE) -> Path:
    return legacy_market_results_dir(market_scope) / filename


def existing_research_file(filename: str, *, market_scope: str | None = A_SHARE_SCOPE) -> Path:
    path = research_file(filename, market_scope=market_scope)
    if path.exists():
        return path
    legacy_path = legacy_research_file(filename, market_scope=market_scope)
    if legacy_path.exists():
        return legacy_path
    return path


def iter_summary_paths(*, market_scope: str | None = None, include_legacy: bool = True) -> Iterable[Path]:
    scopes = MARKET_SCOPES if market_scope is None else (normalize_market_scope(market_scope),)
    seen: set[Path] = set()
    for scope in scopes:
        roots = [market_backtests_dir(scope)]
        if include_legacy:
            roots.append(legacy_market_results_dir(scope))
        for root in roots:
            if not root.exists():
                continue
            for path in root.rglob("summary.json"):
                if root == LEGACY_A_SHARE_RESULTS_DIR:
                    try:
                        path.relative_to(RESULTS_BACKTESTS_DIR)
                        continue
                    except ValueError:
                        pass
                resolved = path.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                yield path


def ensure_results_layout() -> None:
    for path in (
        RESULTS_BACKTESTS_DIR,
        RESULTS_BACKTESTS_DIR / A_SHARE_SCOPE,
        RESULTS_BACKTESTS_DIR / HKCONNECT_SCOPE,
        RESULTS_RESEARCH_DIR,
        RESULTS_RESEARCH_DIR / A_SHARE_SCOPE,
        RESULTS_RESEARCH_DIR / HKCONNECT_SCOPE,
        RESULTS_LIVE_DIR,
    ):
        path.mkdir(parents=True, exist_ok=True)
