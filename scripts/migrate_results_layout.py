from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.cleanup_backtest_results import parse_result_dir
from scripts.results_layout import (
    A_SHARE_SCOPE,
    HKCONNECT_SCOPE,
    LEGACY_A_SHARE_RESULTS_DIR,
    LEGACY_HKCONNECT_RESULTS_DIR,
    ensure_results_layout,
    market_backtests_dir,
    market_research_dir,
)

A_SHARE_RESEARCH_FILES = (
    "core_active_registry.json",
    "path2_candidate_pass.json",
    "public_snapshot.json",
    "research_experiments.jsonl",
    "research_iteration_report.json",
    "research_iteration_state.json",
    "strategy_comparison.csv",
    "strategy_comparison_base_method.csv",
    "tracked_winner_history.json",
    "weighted_track_winners.json",
    "winner_only_pass.json",
)
HKCONNECT_RESEARCH_FILES = (
    "strategy_comparison_hkconnect.csv",
    "tracked_winners_hkconnect.json",
)


def _remove(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


def _move(src: Path, dst: Path, *, apply: bool, replace: bool, prune_source: bool = False) -> str:
    if not src.exists():
        return "missing"
    if dst.exists():
        if not replace:
            if prune_source:
                if apply:
                    _remove(src)
                return "pruned"
            return "exists"
        if apply:
            _remove(dst)
    if apply:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
    return "moved"


def _migrate_research_files(*, apply: bool, replace: bool, prune_legacy: bool) -> dict[str, int]:
    counts = {"moved": 0, "exists": 0, "missing": 0, "pruned": 0}
    for filename in A_SHARE_RESEARCH_FILES:
        status = _move(
            LEGACY_A_SHARE_RESULTS_DIR / filename,
            market_research_dir(A_SHARE_SCOPE) / filename,
            apply=apply,
            replace=replace,
            prune_source=prune_legacy,
        )
        counts[status] = counts.get(status, 0) + 1
    status = _move(
        LEGACY_A_SHARE_RESULTS_DIR / "strategies",
        market_research_dir(A_SHARE_SCOPE) / "strategies",
        apply=apply,
        replace=replace,
        prune_source=prune_legacy,
    )
    counts[status] = counts.get(status, 0) + 1

    for filename in HKCONNECT_RESEARCH_FILES:
        status = _move(
            LEGACY_HKCONNECT_RESULTS_DIR / filename,
            market_research_dir(HKCONNECT_SCOPE) / filename,
            apply=apply,
            replace=replace,
            prune_source=prune_legacy,
        )
        counts[status] = counts.get(status, 0) + 1
    return counts


def _migrate_backtests(*, apply: bool, replace: bool, market_scope: str) -> dict[str, int]:
    source = LEGACY_HKCONNECT_RESULTS_DIR if market_scope == HKCONNECT_SCOPE else LEGACY_A_SHARE_RESULTS_DIR
    dest_root = market_backtests_dir(market_scope)
    counts = {"moved": 0, "exists": 0, "missing": 0, "skipped": 0}
    if not source.exists():
        counts["missing"] += 1
        return counts
    for path in sorted(source.iterdir(), key=lambda item: item.name):
        if not path.is_dir() or path.is_symlink():
            continue
        if parse_result_dir(path) is None:
            counts["skipped"] += 1
            continue
        status = _move(path, dest_root / path.name, apply=apply, replace=replace)
        counts[status] = counts.get(status, 0) + 1
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Move results into the three-layer layout: backtests, research, and live."
    )
    parser.add_argument("--apply", action="store_true", help="Actually move files. Default is dry-run.")
    parser.add_argument("--replace", action="store_true", help="Replace existing destination files or dirs.")
    parser.add_argument(
        "--prune-legacy-research",
        action="store_true",
        help="When the new research file already exists, remove the legacy source instead of leaving a duplicate.",
    )
    parser.add_argument(
        "--market-scope",
        choices=["all", A_SHARE_SCOPE, HKCONNECT_SCOPE],
        default="all",
        help="Which market backtest directories to migrate. Research files are handled separately.",
    )
    parser.add_argument("--skip-backtests", action="store_true", help="Only migrate research files.")
    args = parser.parse_args()

    ensure_results_layout()
    mode = "APPLY" if args.apply else "DRY-RUN"
    research = _migrate_research_files(
        apply=args.apply,
        replace=args.replace,
        prune_legacy=args.prune_legacy_research,
    )
    print(f"[{mode}] research: {research}")
    if not args.skip_backtests:
        if args.market_scope in ("all", A_SHARE_SCOPE):
            ashare = _migrate_backtests(apply=args.apply, replace=args.replace, market_scope=A_SHARE_SCOPE)
            print(f"[{mode}] backtests/a_share: {ashare}")
        if args.market_scope in ("all", HKCONNECT_SCOPE):
            hkconnect = _migrate_backtests(apply=args.apply, replace=args.replace, market_scope=HKCONNECT_SCOPE)
            print(f"[{mode}] backtests/hkconnect: {hkconnect}")
    if not args.apply:
        print("[DRY-RUN] No files moved. Add --apply to apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
