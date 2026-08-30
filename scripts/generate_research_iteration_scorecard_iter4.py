#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
A_DIR = ROOT / "results" / "research" / "a_share"
HK_DIR = ROOT / "results" / "research" / "hkconnect"
WINDOWS = ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]
METRICS = ["cagr", "sharpe_ratio", "max_drawdown", "average_annual_turnover"]

P1_REF = "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm"
P2_REF = "core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn"
P3_REF = "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly"
P4_REF = "core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn"

A_CANDIDATES = [
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm",
        P1_REF,
        "reject",
    ),
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm",
        P1_REF,
        "reject",
    ),
    ("ashare_path1", P1_REF, P1_REF, "promote"),
    (
        "ashare_path2",
        "core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn",
        P2_REF,
        "keep_watch",
    ),
    (
        "ashare_path2",
        "core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn",
        P2_REF,
        "reject",
    ),
    (
        "ashare_path2",
        P2_REF,
        P2_REF,
        "robust_observation",
    ),
    (
        "ashare_path3",
        "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly",
        P3_REF,
        "reject",
    ),
    ("ashare_path3", P3_REF, P3_REF, "promote"),
    (
        "ashare_path4",
        "core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5",
        P4_REF,
        "reject",
    ),
    (
        "ashare_path4",
        "core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4",
        P4_REF,
        "reject",
    ),
    ("ashare_path4", P4_REF, P4_REF, "robust_observation"),
]

HK_CANDIDATES = [
    ("hkconnect_path1_biweekly_hybrid", "keep_watch"),
    ("hkconnect_path2_quality_liquidity_momentum_monthly_v1", "keep_watch"),
    ("hkconnect_path3_theme_fast_weekly_buffered", "keep_watch"),
    ("hkconnect_path4_quality_momentum_monthly_smoke", "reject"),
    ("hkconnect_path5_pullback_continuation_monthly_quality_retest_v10_definition_repair", "reject"),
    ("hkconnect_path6_large_liquid_core_monthly_smoke", "promote"),
    ("hkconnect_path7_barbell_quality_growth_biweekly_core_defensive_lowturn_v10", "keep_watch"),
]

HK_REFS = {
    "path1": "hkconnect_path1_biweekly_lowvol",
    "path2": "hkconnect_path2_theme_fast_monthly",
    "path3": "hkconnect_path3_equal_elastic_weekly",
    "path4": "hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality",
    "path5": "hkconnect_path5_pullback_continuation_monthly_quality_retest_v35_ytd_repair",
    "path6": "hkconnect_path6_lowvol_liquid_biweekly_smoke",
    "path7": "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3",
}

WINNER_OR_ROBUST_CHANGED: set[str] = {
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly",
    "core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5",
}

TRACKED_PAYLOAD_REFRESHED: set[str] = set()

ROUTE_MISMATCH_CANDIDATES: set[str] = {
    "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm",
    "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm",
}

FOCUS = {
    "ashare_path1": "多因子风险边界、路由一致性与中窗收益",
    "ashare_path2": "风险再确认敏感性、换手成本与2026恢复",
    "ashare_path3": "周频减换手、收益与回撤平衡",
    "ashare_path4": "强主题信号质量、风险控制与年内恢复",
    "hkconnect_path1": "低波月频周风控与双周年内守门",
    "hkconnect_path2": "弹性成本控制的收益、回撤与短窗恢复",
    "hkconnect_path3": "周频防守、收益与换手平衡",
    "hkconnect_path4": "质量与流动性动量的收益回撤平衡",
    "hkconnect_path5": "回踩续涨定义与确认质量",
    "hkconnect_path6": "大市值高流动核心的多窗收益、回撤与容量",
    "hkconnect_path7": "杠铃两袖结构的短窗收益与换手",
}


def latest(frame: pd.DataFrame) -> pd.DataFrame:
    frame = frame[
        frame["sample_tag"].isin(WINDOWS)
        & (frame["sample_end"].astype(str) == "2026-08-28")
    ].copy()
    return frame.drop_duplicates(["strategy_base_id", "sample_tag"], keep="last")


def metrics(frame: pd.DataFrame, strategy_id: str, sample_tag: str) -> dict[str, float | None]:
    row = frame[(frame["strategy_base_id"] == strategy_id) & (frame["sample_tag"] == sample_tag)]
    if row.empty:
        raise RuntimeError(f"缺少指标: {strategy_id} / {sample_tag}")
    record = row.iloc[-1]
    return {metric: (float(record[metric]) if pd.notna(record[metric]) else None) for metric in METRICS}


def decision_reason(decision: str, windows: dict[str, Any]) -> str:
    d20 = windows["since_2020_01"]["delta"]
    d23 = windows["since_2023_01"]["delta"]
    d25 = windows["since_2025_01"]["delta"]
    d26 = windows["since_2026_01"]["delta"]
    fmt = lambda value: "null" if value is None else f"{value:.4f}"
    summary = (
        f"相对参考，2020 CAGR/Sharpe/MaxDD差分为 {fmt(d20['cagr'])}/"
        f"{fmt(d20['sharpe_ratio'])}/{fmt(d20['max_drawdown'])}，"
        f"2023为 {fmt(d23['cagr'])}/{fmt(d23['sharpe_ratio'])}/"
        f"{fmt(d23['max_drawdown'])}；"
        f"相对参考，2025 CAGR/MaxDD/turnover差分为 {fmt(d25['cagr'])}/"
        f"{fmt(d25['max_drawdown'])}/{fmt(d25['average_annual_turnover'])}，"
        f"2026为 {fmt(d26['cagr'])}/{fmt(d26['max_drawdown'])}/"
        f"{fmt(d26['average_annual_turnover'])}。"
    )
    suffix = {
        "promote": "形成关键风险收益前沿且未破坏相邻窗口，支持假设。",
        "keep_watch": "存在专项改善，但相邻窗口、绝对收益或成本尚未同时满足晋级条件。",
        "robust_observation": "仅进入路径内部观察位，不是强稳定 winner。",
        "reject": "相邻窗口、风险或成本明显退化，假设不获支持。",
        "archive": "被新前沿或等价形态支配，退出 active 并保留历史快照。",
    }[decision]
    return summary + suffix


def make_event_card() -> dict[str, Any]:
    event_path = A_DIR / "event_theme_backtest_entry_ai_datacenter_power_grid_202607_v0_path4_risk_control_v5_20260831_mature.json"
    event = json.loads(event_path.read_text(encoding="utf-8"))
    gap = "event runner 只产出事件 horizon，不生成连续组合 CAGR、Sharpe、MaxDD、turnover"
    return {
        "path": "ashare_path5",
        "candidate_id": event["basket_id"],
        "reference_id": event["path4_reference_overlap"]["strategy_id"],
        "decision": "keep_watch",
        "hypothesis": "相对 Path4 risk-control-v5 观察位复核已审计冻结数据中心电力篮子的成熟期，预期 20/40/60D 保持正收益且低 overlap。",
        "reason": "20D 收益保持正值并与 Path4 低 overlap；40/60D仍未成熟，且事件 runner 缺连续风险指标，只能 keep_watch。",
        "windows": {
            window: {
                "candidate_metrics": {metric: None for metric in METRICS},
                "current_winner_or_robust_metrics": None,
                "delta": None,
                "gap_reason": gap,
            }
            for window in WINDOWS
        },
        "event_horizons": event["portfolio_returns"],
        "path4_overlap": event["path4_reference_overlap"],
        "source_status": "source_audited",
        "frozen": True,
        "stability_guard_hits": [],
        "winner_or_robust_changed": False,
        "tracked_payload_changed": False,
    }


def make_card(
    frame: pd.DataFrame,
    path: str,
    candidate_id: str,
    reference_id: str,
    decision: str,
) -> dict[str, Any]:
    name_row = frame[frame["strategy_base_id"] == candidate_id]
    candidate_name = str(name_row.iloc[-1].get("strategy_name", candidate_id)) if not name_row.empty else candidate_id
    window_payload: dict[str, Any] = {}
    for window in WINDOWS:
        cand = metrics(frame, candidate_id, window)
        ref = metrics(frame, reference_id, window)
        delta = {
            key: (cand[key] - ref[key] if cand[key] is not None and ref[key] is not None else None)
            for key in METRICS
        }
        window_payload[window] = {
            "candidate_metrics": cand,
            "current_winner_or_robust_metrics": ref,
            "delta": delta,
        }
    guard_hits: list[str] = []
    for window in ("since_2020_01", "since_2023_01"):
        delta = window_payload[window]["delta"]
        if delta["cagr"] is not None and delta["cagr"] < -0.03:
            guard_hits.append(f"{window}:cagr")
        if delta["max_drawdown"] is not None and delta["max_drawdown"] < -0.05:
            guard_hits.append(f"{window}:max_drawdown")
        if delta["sharpe_ratio"] is not None and delta["sharpe_ratio"] < -0.30:
            guard_hits.append(f"{window}:sharpe_ratio")
    card = {
        "path": path,
        "candidate_id": candidate_id,
        "candidate_name": candidate_name,
        "reference_id": reference_id,
        "decision": decision,
        "hypothesis": f"相对 {reference_id} 采用候选参数形态“{candidate_name}”，预期改善{FOCUS[path]}。",
        "reason": decision_reason(decision, window_payload),
        "stability_guard_hits": guard_hits,
        "windows": window_payload,
        "winner_or_robust_changed": candidate_id in WINNER_OR_ROBUST_CHANGED,
        "tracked_payload_changed": candidate_id in TRACKED_PAYLOAD_REFRESHED,
    }
    if candidate_id in ROUTE_MISMATCH_CANDIDATES:
        card["validation_gap"] = "only-base-id 实跑落入 growth_elastic，而 winner-only 内存评估属于 Path1 core_explore_seed；不同池结果不可作为同池晋级证据。"
        card["reason"] = "候选落盘路由与 Path1 参考池不一致，不能形成同窗口同池确认，判定 reject；需先修复 selector 路由后再评估。"
    return card


def main() -> None:
    a = latest(pd.read_csv(A_DIR / "strategy_comparison_base_method.csv"))
    hk_raw = pd.read_csv(HK_DIR / "strategy_comparison_hkconnect.csv")
    hk = latest(hk_raw.rename(columns={"strategy_id": "strategy_base_id"}))

    cards: list[dict[str, Any]] = []
    for path, candidate_id, reference, decision in A_CANDIDATES:
        cards.append(make_card(a, path, candidate_id, reference, decision))

    for candidate_id, decision in HK_CANDIDATES:
        path = candidate_id.split("_")[1]
        cards.append(make_card(hk, f"hkconnect_{path}", candidate_id, HK_REFS[path], decision))
    cards.append(make_event_card())

    counts = {key: sum(card["decision"] == key for card in cards) for key in ["promote", "keep_watch", "robust_observation", "reject", "archive"]}
    payload = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "data_endpoint": "2026-08-28",
        "candidate_count": len(cards),
        "budget_note": "Path2 coverage blocker 首批20个base ids四窗口补齐后缺口由752降至732，v70五窗确认再顺带补齐1条，最终缺731、剩余37批。另完成A股11个、HK7个五窗口确认与1个Path5事件篮子，共19卡；Path2所有新排序因blocking不得promote。",
        "coverage_blocker": {
            "scope_id": "ashare_path2_candidate_universe",
            "missing_before": 752,
            "missing_after_first_batch": 732,
            "missing_after_all_runs": 731,
            "remaining_rerun_batches": 37,
            "promotion_deferred": True,
        },
        "winner_validation_policy": "窗口winner使用相邻窗口；本轮2026专项以2025为直接相邻窗，五窗口阈值用于robust二次判断。",
        "delta_definition": "candidate minus current_winner_or_robust; MaxDD positive means improvement",
        "stopping_rule": "任一候选触发2020/2023 CAGR、Sharpe或MaxDD稳定性护栏即不得promote；短窗转负、绝对收益弱或换手成本不可接受时降为keep_watch、robust_observation或reject。",
        "summary": counts,
        "scorecards": cards,
    }
    output = A_DIR / "research_iteration_scorecard_20260831.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
