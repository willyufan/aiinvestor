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
WEIGHTED_REQUIRED_TAGS = ("since_2017_01", "since_2020_01", "since_2023_01")
PATH2_PROMOTION_SCORE_POLICY = {
    "cagr_2020_weight": 0.70,
    "cagr_2023_weight": 0.30,
    "sharpe_2020_weight": 0.07,
    "sharpe_2023_weight": 0.03,
}


def _eval_python_constant(node: ast.AST, env: dict[str, Any]) -> Any:
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.List):
        return [_eval_python_constant(item, env) for item in node.elts]
    if isinstance(node, ast.Tuple):
        return tuple(_eval_python_constant(item, env) for item in node.elts)
    if isinstance(node, ast.Set):
        return {_eval_python_constant(item, env) for item in node.elts}
    if isinstance(node, ast.Dict):
        return {
            _eval_python_constant(key, env): _eval_python_constant(value, env)
            for key, value in zip(node.keys, node.values)
        }
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _eval_python_constant(node.operand, env)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.Name):
        return env[node.id]
    if isinstance(node, ast.Subscript):
        value = _eval_python_constant(node.value, env)
        key = _eval_python_constant(node.slice, env)
        return value[key]
    raise ValueError(f"Unsupported constant expression: {ast.dump(node)}")


def _parse_python_constants(path: Path, names: Iterable[str]) -> dict[str, Any]:
    wanted = set(names)
    result: dict[str, Any] = {}
    env: dict[str, Any] = {}
    node = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    for stmt in node.body:
        if not isinstance(stmt, ast.Assign):
            continue
        if len(stmt.targets) != 1 or not isinstance(stmt.targets[0], ast.Name):
            continue
        target = stmt.targets[0].id
        try:
            value = _eval_python_constant(stmt.value, env)
        except Exception:
            continue
        env[target] = value
        if target not in wanted:
            continue
        result[target] = value
    missing = wanted - set(result)
    if missing:
        raise RuntimeError(f"Unable to extract constants from {path}: {sorted(missing)}")
    return result


def load_path2_scan_rules(backtest_path: Path) -> tuple[list[str], list[str], dict[str, dict[str, Any]]]:
    consts = _parse_python_constants(
        backtest_path,
        ["PATH2_SCAN_BASE_PREFIXES", "PATH2_SCAN_VARIANT_IDS", "PATH2_SCAN_FAMILY_RULES"],
    )
    prefixes = [str(item) for item in consts.get("PATH2_SCAN_BASE_PREFIXES") or []]
    variant_ids = [str(item) for item in consts.get("PATH2_SCAN_VARIANT_IDS") or []]
    family_rules_raw = consts.get("PATH2_SCAN_FAMILY_RULES") or {}
    family_rules: dict[str, dict[str, Any]] = {}
    for family_name, family_meta in family_rules_raw.items():
        family_rules[str(family_name)] = {
            "prefixes": [str(item) for item in family_meta.get("prefixes") or []],
            "prefix_only_prefixes": [str(item) for item in family_meta.get("prefix_only_prefixes") or []],
            "variant_ids": [str(item) for item in family_meta.get("variant_ids") or []],
            "target_candidates": int(family_meta.get("target_candidates") or 0),
        }
    return prefixes, variant_ids, family_rules


def _latest_per_strategy_window(frame: pd.DataFrame) -> pd.DataFrame:
    typed = frame.copy()
    typed["sample_end"] = pd.to_datetime(typed["sample_end"], errors="coerce")
    typed = typed.dropna(subset=["sample_end"])
    typed = typed.sort_values(["strategy_base_id", "sample_tag", "sample_end"])
    return typed.groupby(["strategy_base_id", "sample_tag"], as_index=False).tail(1)


def _filter_to_current_as_of(latest: pd.DataFrame) -> pd.DataFrame:
    # sample_end is the strategy's actual signal/rebalance point. Monthly,
    # biweekly, and weekly candidates can legitimately have different latest
    # signal dates under the same market cache, so keep each strategy/window's
    # own latest row instead of applying a global max-date filter.
    return latest.copy()


def _robust_sort_key(metrics: dict[str, float]) -> tuple[float, float, float, float, float]:
    return (
        float(metrics["cagr_min"]),
        float(metrics["max_drawdown_worst"]),
        float(metrics["sharpe_mean"]),
        float(metrics["cagr_mean"]),
        -float(metrics["turnover_mean"]),
    )


def _matches_path2(base_id: str, prefixes: list[str], variant_ids: list[str]) -> bool:
    if any(base_id.startswith(prefix) for prefix in prefixes):
        return True
    return any(base_id.endswith(f"__{variant_id}") for variant_id in variant_ids)


def _extract_variant_id(base_id: str) -> str | None:
    if "__" not in base_id:
        return None
    return base_id.rsplit("__", 1)[1]


def _match_families(base_id: str, family_rules: dict[str, dict[str, Any]]) -> list[str]:
    matched: list[str] = []
    variant_id = _extract_variant_id(base_id)
    for family_name, family_meta in family_rules.items():
        prefixes = family_meta.get("prefixes") or []
        prefix_only_prefixes = family_meta.get("prefix_only_prefixes") or []
        variant_ids = family_meta.get("variant_ids") or []
        prefix_ok = not prefixes or any(base_id.startswith(prefix) for prefix in prefixes)
        variant_match = bool(variant_id and variant_id in variant_ids and prefix_ok)
        prefix_only_match = any(base_id.startswith(prefix) for prefix in prefix_only_prefixes)
        if variant_match or prefix_only_match:
            matched.append(family_name)
    return matched


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

    prefixes, variant_ids, family_rules = load_path2_scan_rules(args.backtest_script)
    frame = pd.read_csv(args.comparison_csv)
    latest = _filter_to_current_as_of(_augment_with_synthetic_windows(_latest_per_strategy_window(frame)))
    latest["strategy_base_id"] = latest["strategy_base_id"].astype(str)
    latest["sample_tag"] = latest["sample_tag"].astype(str)

    candidate_ids = sorted(
        {
            base_id
            for base_id in latest["strategy_base_id"].unique()
            if _matches_path2(str(base_id), prefixes, variant_ids)
        }
    )
    family_candidates: dict[str, list[str]] = {family_name: [] for family_name in family_rules}
    candidate_family_membership: dict[str, list[str]] = {}
    for base_id in candidate_ids:
        matched_families = _match_families(base_id, family_rules)
        candidate_family_membership[base_id] = matched_families
        for family_name in matched_families:
            family_candidates.setdefault(family_name, []).append(base_id)

    by_id = {str(base_id): group for base_id, group in latest.groupby("strategy_base_id")}
    window_winners: dict[str, dict[str, Any]] = {}
    ranked_candidates: dict[str, list[dict[str, Any]]] = {}

    for sample_tag in WINDOW_TAGS:
        candidates: list[tuple[str, dict[str, float]]] = []
        for base_id in candidate_ids:
            group = by_id.get(base_id, pd.DataFrame())
            tags = set(group["sample_tag"].astype(str)) if not group.empty else set()
            # For comparable window winners, require the strategy to also have the other long windows,
            # except for the synthetic short window (since_2025_01) which is tracked independently.
            if sample_tag != "since_2025_01" and not set(WEIGHTED_REQUIRED_TAGS).issubset(tags):
                continue
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
    robust_candidates.sort(key=lambda item: _robust_sort_key(item[1]), reverse=True)

    family_ranked_candidates: dict[str, list[dict[str, Any]]] = {}
    for family_name, family_ids in family_candidates.items():
        ranked: list[tuple[str, float, float, float, float]] = []
        for base_id in sorted(set(family_ids)):
            group = by_id.get(base_id, pd.DataFrame())
            tags = set(group["sample_tag"].astype(str)) if not group.empty else set()
            if not set(WEIGHTED_REQUIRED_TAGS).issubset(tags):
                continue
            metrics_2020 = _compute_single_window_metrics(group, "since_2020_01")
            metrics_2023 = _compute_single_window_metrics(group, "since_2023_01")
            if not metrics_2020 or not metrics_2023:
                continue
            score = (
                PATH2_PROMOTION_SCORE_POLICY["cagr_2020_weight"] * metrics_2020["cagr"]
                + PATH2_PROMOTION_SCORE_POLICY["cagr_2023_weight"] * metrics_2023["cagr"]
                + PATH2_PROMOTION_SCORE_POLICY["sharpe_2020_weight"] * metrics_2020["sharpe"]
                + PATH2_PROMOTION_SCORE_POLICY["sharpe_2023_weight"] * metrics_2023["sharpe"]
            )
            ranked.append(
                (
                    base_id,
                    score,
                    metrics_2020["cagr"],
                    metrics_2023["cagr"],
                    min(metrics_2020["max_drawdown"], metrics_2023["max_drawdown"]),
                )
            )
        ranked.sort(key=lambda item: (item[1], item[2], item[3], item[4]), reverse=True)
        family_ranked_candidates[family_name] = [
            {
                "strategy_base_id": base_id,
                "score": score,
                "cagr_2020": cagr_2020,
                "cagr_2023": cagr_2023,
                "worst_max_drawdown": worst_max_drawdown,
            }
            for base_id, score, cagr_2020, cagr_2023, worst_max_drawdown in ranked[
                : max(1, family_rules.get(family_name, {}).get("target_candidates", 0))
            ]
        ]

    payload = {
        "candidate_prefixes": prefixes,
        "candidate_variant_ids": variant_ids,
        "candidate_families": family_rules,
        "promotion_score_policy": PATH2_PROMOTION_SCORE_POLICY,
        "candidate_count": len(candidate_ids),
        "family_candidate_counts": {family_name: len(sorted(set(ids))) for family_name, ids in family_candidates.items()},
        "candidate_family_membership": candidate_family_membership,
        "window_winners": window_winners,
        "robust_candidate": (
            {"strategy_base_id": robust_candidates[0][0], "metrics": robust_candidates[0][1]}
            if robust_candidates
            else None
        ),
        "ranked_candidates": ranked_candidates,
        "family_ranked_candidates": family_ranked_candidates,
    }
    args.write_json.parent.mkdir(parents=True, exist_ok=True)
    args.write_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"[OK] path2 candidates={len(candidate_ids)} prefixes={prefixes} variants={variant_ids}")
    if family_rules:
        print("[OK] path2 candidate families:")
        for family_name, family_meta in family_rules.items():
            family_size = len(sorted(set(family_candidates.get(family_name, []))))
            target = int(family_meta.get("target_candidates") or 0)
            print(
                f"       - {family_name}: {family_size} candidates "
                f"(target {target}, prefixes={family_meta.get('prefixes') or []}, "
                f"prefix_only={family_meta.get('prefix_only_prefixes') or []}, "
                f"variants={family_meta.get('variant_ids') or []})"
            )
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
