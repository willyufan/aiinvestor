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

P1_REF = "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm"
P1_2017_REF = "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm"
P1_2023_REF = "core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6"
P1_2025_REF = "core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard"
P2_REF = "core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn"
P3_REF = "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly"
P4_REF = "core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn"

A_CANDIDATES = [
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_industry_signal_cashguard_reconfirm",
        P1_REF,
        "reject",
    ),
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_signal_reconfirm",
        P1_REF,
        "reject",
    ),
    ("ashare_path1", P1_REF, P1_REF, "promote"),
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm",
        P1_REF,
        "promote",
    ),
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__aggr_08_92_hold_3_6",
        P1_2017_REF,
        "reject",
    ),
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered_cost_guard_cashguard",
        P1_2017_REF,
        "reject",
    ),
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__share_12_88_hold_4_6__sat_three_stage_buffered_asym13",
        P1_2023_REF,
        "reject",
    ),
    (
        "ashare_path1",
        "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__sat_three_stage_buffered_asym13",
        P1_2025_REF,
        "reject",
    ),
    (
        "ashare_path2",
        "core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top13_risk28_mom_exit48_reconfirm96_caution64_cap24_cost_guard_v27_medium_cycle",
        P2_REF,
        "keep_watch",
    ),
    (
        "ashare_path2",
        "core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle",
        P2_REF,
        "keep_watch",
    ),
    ("ashare_path2", P2_REF, P2_REF, "promote"),
    (
        "ashare_path3",
        "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly",
        P3_REF,
        "reject",
    ),
    (
        "ashare_path3",
        "core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly",
        P3_REF,
        "reject",
    ),
    ("ashare_path3", P3_REF, P3_REF, "promote"),
    (
        "ashare_path4",
        "core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn",
        P4_REF,
        "reject",
    ),
    (
        "ashare_path4",
        "core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn",
        P4_REF,
        "reject",
    ),
    ("ashare_path4", P4_REF, P4_REF, "robust_observation"),
]

HK_CANDIDATES = [
    ("hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32", "reject"),
    ("hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34", "reject"),
    ("hkconnect_path1_biweekly_lowvol", "promote"),
    ("hkconnect_path2_high_return_monthly_quality_liquidity_v27_cost_guard", "keep_watch"),
    ("hkconnect_path2_quality_liquidity_momentum_monthly_v2_cost_guard", "keep_watch"),
    ("hkconnect_path2_theme_fast_monthly", "promote"),
    ("hkconnect_path3_stable_weekly_equal_buffered_v36_return_recovery", "reject"),
    ("hkconnect_path3_stable_weekly_lowvol_buffered_v38_return_recovery", "keep_watch"),
    ("hkconnect_path3_equal_elastic_weekly", "promote"),
    ("hkconnect_path4_quality_momentum_monthly_v49_capacity_guard", "keep_watch"),
    ("hkconnect_path4_quality_momentum_monthly_ytd_guard_v3", "reject"),
    ("hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality", "robust_observation"),
    ("hkconnect_path5_pullback_continuation_monthly_quality_retest_v34_pullback_definition_rewrite", "keep_watch"),
    ("hkconnect_path5_pullback_continuation_monthly_quality_retest_v10_definition_repair", "reject"),
    ("hkconnect_path5_pullback_continuation_monthly_quality_retest_v35_ytd_repair", "robust_observation"),
    ("hkconnect_path6_large_liquid_core_biweekly_liquidity_mix_v3", "keep_watch"),
    ("hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_mix_v8", "keep_watch"),
    ("hkconnect_path6_lowvol_liquid_biweekly_smoke", "promote"),
    ("hkconnect_path7_barbell_quality_growth_biweekly_lowturn_dual_sleeve_v9", "promote"),
    ("hkconnect_path7_barbell_quality_growth_biweekly_core_defensive_lowturn_v10", "keep_watch"),
    ("hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3", "promote"),
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

FOCUS = {
    "ashare_path1": "多因子行业信号的中窗收益、回撤与换手",
    "ashare_path2": "中周期CAGR与2026恢复，避免高换手和深回撤",
    "ashare_path3": "周频收益恢复、MaxDD与换手平衡",
    "ashare_path4": "强主题信号质量、风险控制与容量成本",
    "hkconnect_path1": "月频周风控与双周低波的短窗响应",
    "hkconnect_path2": "双周突破的收益、回撤与成本",
    "hkconnect_path3": "周频防守、收益与换手平衡",
    "hkconnect_path4": "质量与流动性动量的收益回撤平衡",
    "hkconnect_path5": "回踩续涨定义与确认质量",
    "hkconnect_path6": "大市值高流动核心的短窗收益与容量",
    "hkconnect_path7": "杠铃两袖结构的短窗收益与换手",
}


def latest(frame: pd.DataFrame) -> pd.DataFrame:
    frame = frame[
        frame["sample_tag"].isin(WINDOWS)
        & (frame["sample_end"].astype(str) == "2026-08-14")
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
    summary = (
        f"相对参考，2020 CAGR/Sharpe/MaxDD差分为 {d20['cagr']:.4f}/"
        f"{d20['sharpe_ratio']:.4f}/{d20['max_drawdown']:.4f}，"
        f"2023为 {d23['cagr']:.4f}/{d23['sharpe_ratio']:.4f}/"
        f"{d23['max_drawdown']:.4f}；"
        f"相对参考，2025 CAGR/MaxDD/turnover差分为 {d25['cagr']:.4f}/"
        f"{d25['max_drawdown']:.4f}/{d25['average_annual_turnover']:.4f}，"
        f"2026为 {d26['cagr']:.4f}/{d26['max_drawdown']:.4f}/"
        f"{d26['average_annual_turnover']:.4f}。"
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
    event_path = A_DIR / "event_theme_backtest_entry_ai_glasses_edge_terminal_20260424_v0_path4_signal29_20260816_short.json"
    event = json.loads(event_path.read_text(encoding="utf-8"))
    gap = "event runner 只产出事件 horizon，不生成连续组合 CAGR、Sharpe、MaxDD、turnover"
    return {
        "path": "ashare_path5",
        "candidate_id": event["basket_id"],
        "reference_id": event["path4_reference_overlap"]["strategy_id"],
        "decision": "keep_watch",
        "hypothesis": "相对 Path4 signal29 robust 复核已审计冻结篮子的短窗独立收益，预期 5/10/20D 逐级增强且 overlap 保持低位。",
        "reason": "5/10/20D 等权收益为 2.67%/15.79%/21.80%，与 Path4 overlap 为 0/6；短窗独立收益假设获支持，但缺连续风险指标，不能 promote。",
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
    return {
        "path": path,
        "candidate_id": candidate_id,
        "candidate_name": candidate_name,
        "reference_id": reference_id,
        "decision": decision,
        "hypothesis": f"相对 {reference_id} 采用候选参数形态“{candidate_name}”，预期改善{FOCUS[path]}。",
        "reason": decision_reason(decision, window_payload),
        "windows": window_payload,
        "winner_or_robust_changed": False,
        "tracked_payload_changed": False,
    }


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
        "data_endpoint": "2026-08-14",
        "candidate_count": len(cards),
        "budget_note": "A股 17 个、HK 21 个五窗口 security/base ids，加 1 个 Path5 事件篮子，共 39 卡；coverage 无阻塞且离线缓存精确命中，因 winner-only 新增 4 条 clear signal 将证券实验从 34 放宽到 38，仍低于 48 个上限。",
        "winner_validation_policy": "窗口winner使用相邻窗口；本轮2026专项以2025为直接相邻窗，五窗口阈值用于robust二次判断。",
        "delta_definition": "candidate minus current_winner_or_robust; MaxDD positive means improvement",
        "stopping_rule": "Path1 core_multifactor 行业信号继续失稳，4 条 winner-only clear signal 精确路由后均触发稳定性护栏；A股 Path4 signal30/risk04 与 robust 几乎等价，停止同形阈值扩参；HK Path2 质量流动性月频只保留差异化观察。",
        "summary": counts,
        "scorecards": cards,
    }
    output = A_DIR / "research_iteration_scorecard_20260816.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
