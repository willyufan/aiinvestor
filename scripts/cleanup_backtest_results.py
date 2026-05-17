from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.results_layout import (
    A_SHARE_SCOPE,
    HKCONNECT_SCOPE,
    LEGACY_A_SHARE_RESULTS_DIR,
    LEGACY_HKCONNECT_RESULTS_DIR,
    RESULTS_LIVE_DIR,
    existing_research_file,
    market_backtests_dir,
    normalize_market_scope,
)

ID_KEYS = {"winner", "raw_winner", "strategy_id", "strategy_base_id"}
SAMPLE_TAG_PREFIX = "__since_"


def _load_json(path: Path) -> Any:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
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


def _collect_core_active_ids(path: Path, target: set[str]) -> None:
    payload = _load_json(path)
    if not isinstance(payload, dict):
        return
    for key in ("current_winner_ids", "current_refresh_only_ids"):
        for value in payload.get(key) or []:
            if value:
                target.add(str(value))
    _collect_ids(payload.get("strategies") or [], target)
    _collect_ids(payload.get("refresh_only_strategies") or [], target)


def _collect_weighted_ids(path: Path, target: set[str]) -> None:
    payload = _load_json(path)
    if not isinstance(payload, dict):
        return
    for key in ("tracks", "path2", "path3"):
        _collect_ids(payload.get(key) or {}, target)


def _collect_hk_tracked_ids(path: Path, target: set[str]) -> None:
    payload = _load_json(path)
    if not isinstance(payload, dict):
        return
    _collect_ids(payload.get("tracks") or {}, target)


def _collect_live_registry_ids(path: Path, by_scope: dict[str, set[str]]) -> None:
    payload = _load_json(path)
    if not isinstance(payload, dict):
        return

    def add_items(items: Any) -> None:
        if not isinstance(items, list):
            return
        for item in items:
            if not isinstance(item, dict):
                continue
            scope = normalize_market_scope(str(item.get("market_scope") or A_SHARE_SCOPE))
            strategy_id = str(item.get("strategy_id") or item.get("strategy_base_id") or "")
            if strategy_id:
                by_scope[scope].add(strategy_id)

    add_items(payload.get("strategies"))
    add_items(payload.get("core_active_strategies"))
    leaderboards = payload.get("winner_leaderboards") or {}
    if isinstance(leaderboards, dict):
        _collect_ids(leaderboards.get("a_share") or {}, by_scope[A_SHARE_SCOPE])
        _collect_ids(leaderboards.get("hkconnect") or {}, by_scope[HKCONNECT_SCOPE])


def _collect_csv_top5(path: Path, *, id_col: str, by_scope: set[str]) -> None:
    if not path.exists():
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
    ascending = [False if col != "max_drawdown" else False for col in sort_cols]
    for _, group in working.groupby(group_cols, dropna=False):
        ranked = group.sort_values(sort_cols, ascending=ascending, na_position="last").head(5)
        for value in ranked[id_col].dropna().astype(str):
            if value:
                by_scope.add(value)


def collect_protected_strategy_ids() -> dict[str, set[str]]:
    protected = {A_SHARE_SCOPE: set(), HKCONNECT_SCOPE: set()}
    _collect_live_registry_ids(RESULTS_LIVE_DIR / "strategy_registry.json", protected)
    _collect_weighted_ids(existing_research_file("weighted_track_winners.json"), protected[A_SHARE_SCOPE])
    _collect_core_active_ids(existing_research_file("core_active_registry.json"), protected[A_SHARE_SCOPE])
    _collect_hk_tracked_ids(
        existing_research_file("tracked_winners_hkconnect.json", market_scope=HKCONNECT_SCOPE),
        protected[HKCONNECT_SCOPE],
    )
    _collect_csv_top5(
        existing_research_file("strategy_comparison_base_method.csv"),
        id_col="strategy_base_id",
        by_scope=protected[A_SHARE_SCOPE],
    )
    _collect_csv_top5(
        existing_research_file("strategy_comparison_hkconnect.csv", market_scope=HKCONNECT_SCOPE),
        id_col="strategy_id",
        by_scope=protected[HKCONNECT_SCOPE],
    )
    return protected


def parse_result_dir(path: Path) -> tuple[str, str] | None:
    name = path.name
    if SAMPLE_TAG_PREFIX not in name:
        return None
    base_id, sample_tail = name.rsplit(SAMPLE_TAG_PREFIX, 1)
    sample_tag = f"since_{sample_tail}"
    if not base_id or not sample_tail:
        return None
    if not (path / "summary.json").exists():
        return None
    return base_id, sample_tag


def candidate_roots(scopes: list[str]) -> list[tuple[str, Path]]:
    roots: list[tuple[str, Path]] = []
    for scope in scopes:
        roots.append((scope, market_backtests_dir(scope)))
        if scope == A_SHARE_SCOPE:
            roots.append((scope, LEGACY_A_SHARE_RESULTS_DIR))
        elif scope == HKCONNECT_SCOPE:
            roots.append((scope, LEGACY_HKCONNECT_RESULTS_DIR))
    deduped: list[tuple[str, Path]] = []
    seen: set[Path] = set()
    for scope, root in roots:
        resolved = root.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        deduped.append((scope, root))
    return deduped


def iter_candidate_dirs(scopes: list[str]) -> list[tuple[str, Path, str, str]]:
    candidates: list[tuple[str, Path, str, str]] = []
    for scope, root in candidate_roots(scopes):
        if not root.exists():
            continue
        for path in root.iterdir():
            if not path.is_dir() or path.is_symlink():
                continue
            parsed = parse_result_dir(path)
            if parsed is None:
                continue
            base_id, sample_tag = parsed
            candidates.append((scope, path, base_id, sample_tag))
    return sorted(candidates, key=lambda item: str(item[1]))


def newest_mtime(path: Path) -> float:
    latest = path.stat().st_mtime
    for child in path.iterdir():
        try:
            latest = max(latest, child.stat().st_mtime)
        except FileNotFoundError:
            continue
    return latest


def dir_size(path: Path) -> int:
    total = 0
    for child in path.rglob("*"):
        try:
            if child.is_file():
                total += child.stat().st_size
        except FileNotFoundError:
            continue
    return total


def tracked_result_dirs(candidates: list[tuple[str, Path, str, str]]) -> set[Path]:
    try:
        proc = subprocess.run(
            ["git", "ls-files", "-z", "--", "results", "results_hkconnect"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
    except Exception:
        return set()
    tracked = [item for item in proc.stdout.decode("utf-8", errors="ignore").split("\0") if item]
    candidate_by_rel = {str(path.relative_to(ROOT)): path for _, path, _, _ in candidates if path.is_relative_to(ROOT)}
    tracked_dirs: set[Path] = set()
    for rel in tracked:
        for candidate_rel, candidate_path in candidate_by_rel.items():
            if rel.startswith(candidate_rel + "/"):
                tracked_dirs.add(candidate_path)
                break
    return tracked_dirs


def fmt_size(value: int) -> str:
    size = float(value)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024 or unit == "GB":
            return f"{size:.1f}{unit}"
        size /= 1024
    return f"{size:.1f}GB"


def rel_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Safely remove stale backtest result directories while keeping winners, top5, "
            "core_active, and recent experiments."
        )
    )
    parser.add_argument("--market-scope", choices=["all", A_SHARE_SCOPE, HKCONNECT_SCOPE], default="all")
    parser.add_argument("--recent-days", type=int, default=7)
    parser.add_argument("--delete", action="store_true", help="Actually delete. Without this flag the script only prints a dry-run.")
    parser.add_argument(
        "--include-tracked",
        action="store_true",
        help="Allow deleting result dirs that contain git-tracked files. Default skips them.",
    )
    parser.add_argument(
        "--allow-empty-protection",
        action="store_true",
        help="Allow deletion even if no protected strategy ids were found.",
    )
    parser.add_argument("--max-list", type=int, default=60, help="Maximum stale directories to list.")
    args = parser.parse_args()

    scopes = [A_SHARE_SCOPE, HKCONNECT_SCOPE] if args.market_scope == "all" else [normalize_market_scope(args.market_scope)]
    protected = collect_protected_strategy_ids()
    protected_count = sum(len(protected[scope]) for scope in scopes)
    if protected_count == 0 and not args.allow_empty_protection:
        print("[ABORT] No protected winner/top5/core_active ids were found. Re-run with --allow-empty-protection if intentional.")
        return 2

    cutoff = datetime.now().astimezone() - timedelta(days=max(0, int(args.recent_days)))
    cutoff_ts = cutoff.timestamp()
    roots = candidate_roots(scopes)
    result_dirs = iter_candidate_dirs(scopes)
    tracked_dirs = tracked_result_dirs(result_dirs)
    unique_strategy_ids = {(scope, base_id) for scope, _path, base_id, _sample_tag in result_dirs}
    unique_strategy_windows = {(scope, base_id, sample_tag) for scope, _path, base_id, sample_tag in result_dirs}
    duplicate_strategy_window_dirs = len(result_dirs) - len(unique_strategy_windows)

    keep_protected: list[Path] = []
    keep_recent: list[Path] = []
    keep_tracked: list[Path] = []
    delete_items: list[tuple[Path, int]] = []

    for scope, path, base_id, _sample_tag in result_dirs:
        if base_id in protected[scope]:
            keep_protected.append(path)
            continue
        if newest_mtime(path) >= cutoff_ts:
            keep_recent.append(path)
            continue
        if path in tracked_dirs and not args.include_tracked:
            keep_tracked.append(path)
            continue
        delete_items.append((path, dir_size(path)))

    total_size = sum(size for _, size in delete_items)
    mode = "DELETE" if args.delete else "DRY-RUN"
    print(
        f"[{mode}] result_dirs={len(result_dirs)} unique_strategy_ids={len(unique_strategy_ids)} "
        f"duplicate_strategy_window_dirs={duplicate_strategy_window_dirs} protected={len(keep_protected)} "
        f"recent={len(keep_recent)} tracked_skip={len(keep_tracked)} "
        f"stale_result_dirs={len(delete_items)} reclaim={fmt_size(total_size)}"
    )
    print("[Info] Scan roots: " + ", ".join(rel_path(root) for _scope, root in roots if root.exists()))
    print(f"[Info] Protected ids: a_share={len(protected[A_SHARE_SCOPE])} hkconnect={len(protected[HKCONNECT_SCOPE])}; recent cutoff={cutoff.isoformat(timespec='seconds')}")

    for path, size in delete_items[: max(0, int(args.max_list))]:
        print(f"  stale {fmt_size(size):>8} {rel_path(path)}")
    if len(delete_items) > args.max_list:
        print(f"  ... {len(delete_items) - args.max_list} more stale dirs")
    if keep_tracked:
        print(f"[Info] Skipped {len(keep_tracked)} stale dirs with git-tracked files. Add --include-tracked to include them.")

    if not args.delete:
        print("[DRY-RUN] No files deleted. Add --delete to apply.")
        return 0

    for path, _size in delete_items:
        shutil.rmtree(path)
    print(f"[OK] Deleted {len(delete_items)} stale backtest result dirs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
