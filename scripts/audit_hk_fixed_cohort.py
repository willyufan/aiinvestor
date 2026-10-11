#!/usr/bin/env python3
"""显式隔离重放：冻结父策略每个信号日目标集合，只改变集合内配权。"""
from __future__ import annotations

import argparse
import inspect
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import backtest_hkconnect as engine

PARENT = "hkconnect_path2_theme_entry10_20261006"
CANDIDATE = "hkconnect_path2_fixed_cohort_base_20261012"


def reweight_cohort(parent_weights, base_weights, signal_scores, quality_scores, breakout, ranking_codes=None):
    """复用引擎base公式；冻结截断后的父集合和原始目标总敞口。"""
    pd = engine.pd
    if parent_weights.empty:
        return pd.Series(dtype=float)
    codes = parent_weights.index
    population = codes if ranking_codes is None else sorted(ranking_codes)
    base = base_weights.reindex(population)
    signal = signal_scores.reindex(population)
    quality = quality_scores.reindex(population)
    if base.isna().any() or signal.isna().any() or quality.isna().any():
        raise RuntimeError("固定集合的配权输入缺失，禁止填补或换股")
    # 保留父策略max_holdings截断前的百分位母体，避免暗中改变评分尺度。
    from backtest_marketcap_etf import normalize_positive_weights, safe_percentile_rank
    signal_strength = safe_percentile_rank(signal, ascending=True)
    quality_strength = safe_percentile_rank(quality, ascending=True)
    breakout_strength = breakout.reindex(population).fillna(False).astype(float)
    multiplier = (0.60 + 0.80 * signal_strength + 0.60 * quality_strength
                  + 0.15 * breakout_strength).clip(lower=0.25)
    adjusted = normalize_positive_weights(base) * multiplier
    weights = normalize_positive_weights(adjusted.reindex(codes))
    result = weights * float(parent_weights.sum())
    if set(result.index) != set(codes) or (result <= 0).any():
        raise RuntimeError("固定集合配权改变股票集合")
    return result.sort_values(ascending=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--sample-tags", required=True)
    parser.add_argument("--reference-id", required=True)
    parser.add_argument("--only-strategy-ids", default="",
                        help="可显式指定父、固定集合候选及正式参照，拒绝扩大集合")
    args = parser.parse_args()
    selected_ids = set(filter(None, args.only_strategy_ids.split(",")))
    expected_ids = {PARENT, CANDIDATE, args.reference_id}
    if selected_ids and selected_ids != expected_ids:
        raise RuntimeError("只允许父、固定集合候选及指定正式参照三个ID")
    output = Path(args.output_dir).resolve()
    if output.is_relative_to(ROOT) and not output.is_relative_to(ROOT / "results/research/hkconnect/experiments"):
        raise RuntimeError("仓库内输出必须位于隔离experiments目录")
    output.mkdir(parents=True, exist_ok=True)
    variants = engine.HK_PATH1_VARIANTS + engine.HK_PATH2_VARIANTS + engine.HK_PATH3_VARIANTS + engine.HK_EXPANSION_VARIANTS
    parent = next(v for v in variants if v["strategy_id"] == PARENT)
    if parent.get("risk_overlay_scope") == engine.HK_RISK_OVERLAY_SCOPE_PORTFOLIO:
        raise RuntimeError("当前runner不支持额外周度overlay")
    candidate = {**parent, "strategy_id": CANDIDATE,
                 "strategy_name": "固定entry10父目标集合的base配权诊断",
                 "archive_only": True}
    # 保证每窗先父、后候选；定义只存在于此隔离进程。
    engine.HK_PATH1_VARIANTS = []
    engine.HK_PATH2_VARIANTS = [parent, candidate] + [v for v in variants if v["strategy_id"] == args.reference_id and v["strategy_id"] != PARENT]
    engine.HK_PATH3_VARIANTS = []
    engine.HK_EXPANSION_VARIANTS = []
    original_run = engine.run_hk_backtest
    original_build = engine.build_single_sleeve_weights
    original_trade = engine.compute_rebalance_trades
    original_cap = engine.apply_weight_cap_with_redistribution
    trade_signature = inspect.signature(original_trade)
    context = {}
    frozen = {}
    audit = []
    counters = {"rebalance_calls": 0, "cash_violations": 0, "capital_identity_violations": 0,
                "buy_fee": 0., "sell_fee": 0., "completed": False}

    def build(**kwargs):
        caller = inspect.currentframe().f_back
        local = caller.f_locals
        scope = caller.f_code.co_name
        key = (context["window"], scope, str(local["signal_date"]))
        if context["id"] == PARENT:
            weights, stats = original_build(**kwargs)
            population = (kwargs["currently_held_codes"] & stats["keep_candidates"]) | stats["buy_candidates"]
            frozen[key] = (weights.copy(), dict(stats), population)
            return weights, stats
        if context["id"] != CANDIDATE:
            return original_build(**kwargs)
        if key not in frozen:
            raise RuntimeError("缺少同窗口同信号日父目标")
        parent_weights, stats, population = frozen[key]
        weights = reweight_cohort(parent_weights, kwargs["base_weights"], kwargs["signal_scores"],
                                 kwargs["quality_scores"], kwargs["breakout_signal"], population)
        audit.append({"sample_tag": key[0], "scope": scope, "signal_date": key[2],
                      "rebalance_date": str(local["rebalance_date"]) if "rebalance_date" in local else None,
                      "cohort": sorted(map(str, parent_weights.index)),
                      "cohort_equal": set(weights.index) == set(parent_weights.index),
                      "parent_raw_exposure": float(parent_weights.sum()),
                      "candidate_raw_exposure": float(weights.sum())})
        if "rebalance_date" in local and engine.pd.Timestamp(local["signal_date"]) >= engine.pd.Timestamp(local["rebalance_date"]):
            raise RuntimeError("信号日必须早于实际执行日")
        if abs(float(weights.sum() - parent_weights.sum())) > 1e-10:
            raise RuntimeError("固定集合配权改变父原始目标敞口")
        return weights, dict(stats)

    def cap(weights, **kw):
        result, cash = original_cap(weights, **kw)
        if context["id"] == CANDIDATE:
            row = audit[-1]
            key = (context["window"], row["scope"], row["signal_date"])
            parent_result, _ = original_cap(frozen[key][0], **kw)
            row["capped_cohort_equal"] = set(result.index) == set(parent_result.index)
            row["parent_capped_exposure"] = float(parent_result.sum())
            row["candidate_capped_exposure"] = float(result.sum())
            if not row["capped_cohort_equal"] or abs(result.sum() - parent_result.sum()) > 1e-10:
                raise RuntimeError("单票cap处理改变固定集合或父目标敞口")
            if not result.empty and float(result.max()) > float(kw["cap"]) + 1e-10:
                raise RuntimeError("候选超过单票cap")
        return result, cash

    def trade(*a, **kw):
        bound = trade_signature.bind(*a, **kw)
        bound.apply_defaults()
        initial = float(bound.arguments["current_values"].sum() + bound.arguments["current_cash"])
        result = original_trade(*a, **kw)
        positions, cash, _, _, stats = result
        counters["rebalance_calls"] += 1
        counters["buy_fee"] += float(stats["buy_cost"])
        counters["sell_fee"] += float(stats["sell_commission"] + stats["sell_stamp_duty"])
        fee = float(stats["trading_cost"])
        tolerance = max(1e-8, abs(initial) * 1e-9)
        if cash < -tolerance:
            counters["cash_violations"] += 1
            raise RuntimeError("资金审计发现负现金")
        if abs(float(positions.sum() + cash + fee - initial)) > tolerance:
            counters["capital_identity_violations"] += 1
            raise RuntimeError("资金与费用恒等式不成立")
        return result

    def run(prepared, config):
        context.update(id=config["strategy_id"], window=config["sample_tag"])
        result = original_run(prepared, config)
        if config["strategy_id"] == CANDIDATE:
            result[-1]["fixed_cohort_audit"] = {"parent_id": PARENT, "affects_official_winners": False,
                "scope": "父原始目标集合；实际执行持仓允许因交易缓冲不同"}
        return result

    engine.build_single_sleeve_weights = build
    engine.compute_rebalance_trades = trade
    engine.apply_weight_cap_with_redistribution = cap
    engine.run_hk_backtest = run
    engine.build_output_dir = lambda strategy_id, sample_tag: output / (strategy_id + "__" + sample_tag)
    original_research_file = engine.research_file
    engine.research_file = lambda name, **kw: output / name if name == "strategy_comparison_hkconnect.csv" else original_research_file(name, **kw)
    sys.argv = [sys.argv[0], "--end-date", args.end_date, "--sample-tags", args.sample_tags,
                "--only-strategy-ids", ",".join(dict.fromkeys([PARENT, CANDIDATE, args.reference_id]))]
    try:
        engine.main()
        counters["completed"] = True
    finally:
        (output / "audit.json").write_text(json.dumps({"candidate_id": CANDIDATE,
            "parent_id": PARENT, "counters": counters, "signals": audit,
            "affects_official_winners": False}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
