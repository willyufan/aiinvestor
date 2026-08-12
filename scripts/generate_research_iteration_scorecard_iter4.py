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

P1_REF = "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_risk20_port_fast_crash_pulse55_1w_v3"
P2_REF = "core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn"
P3_REF = "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly"
P4_REF = "core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn"

A_FILES = [
    "crash_resilience_strategy_comparison.csv",
    "crash_resilience_strategy_comparison_iter4.csv",
    "crash_resilience_strategy_comparison_iter4_batch2.csv",
    "crash_resilience_strategy_comparison_iter4_batch3.csv",
    "crash_resilience_strategy_comparison_iter4_batch4.csv",
    "crash_resilience_strategy_comparison_iter4_batch5.csv",
    "strategy_comparison_base_method.csv",
]

A_DECISIONS = {
    "pulse55_confirm2_v5": "reject",
    "pulse65_40_retrigger_v6": "reject",
    "pulse55_1w_cd8_v7": "archive",
    "pulse55_2w_v8": "reject",
    "pulse50_1w_v9": "archive",
    "pulse60_1w_v10": "reject",
    "pulse55_sparse35_v11": "reject",
    "pulse55_sensitive25_v12": "archive",
    "pulse0_1w_v13": "keep_watch",
    "pulse15_1w_v14": "keep_watch",
    "pulse25_1w_v15": "keep_watch",
    "pulse30_1w_v16": "keep_watch",
    "pulse40_1w_v17": "promote",
    "pulse45_1w_v18": "keep_watch",
    "pulse475_1w_v19": "keep_watch",
    "pulse325_1w_v20": "keep_watch",
    "pulse35_1w_v21": "keep_watch",
    "pulse375_1w_v22": "keep_watch",
    "pulse425_1w_v23": "keep_watch",
    "pulse075_1w_v24": "keep_watch",
    "pulse10_1w_v25": "keep_watch",
    "pulse125_1w_v26": "keep_watch",
    "v81_midcycle_lowturn_confirm": "reject",
    "v82_2023_quality_repair": "reject",
    "weekly_return_recovery_v6_weekly": "reject",
    "weekly_return_recovery_v7_weekly": "reject",
    "risk_control_v5": "reject",
    "capacity_v2": "robust_observation",
}

HK_IDS = [
    "hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair",
    "hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36",
    "hkconnect_path1_biweekly_lowvol",
    "hkconnect_path2_theme_biweekly_cost_guard_v32_breakout_repair",
    "hkconnect_path2_theme_biweekly_cost_guard_v34_breakout_cost_repair",
    "hkconnect_path2_theme_biweekly_cost_guard_v29_breakout_turnover_cap",
    "hkconnect_path2_theme_biweekly_cost_guard_v31_breakout_lowturn_repair",
    "hkconnect_path2_theme_fast_monthly",
    "hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff40_turnover0_exit56_v20_turnover_reduction",
    "hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff42_turnover0_exit58_v21_defensive_overlay",
    "hkconnect_path3_equal_elastic_cashoff_weekly",
    "hkconnect_path4_quality_momentum_monthly_lowdraw_v37_quality_momentum_ytd_guard",
    "hkconnect_path4_quality_momentum_monthly_ytd_positive_v34_ytd_guard",
    "hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality",
    "hkconnect_path5_pullback_continuation_monthly_quality_retest_v34_pullback_definition_rewrite",
    "hkconnect_path5_pullback_continuation_monthly_quality_retest_v25_pullback_definition_lowturn",
    "hkconnect_path5_pullback_continuation_monthly_quality_retest_v35_ytd_repair",
    "hkconnect_path6_large_liquid_core_monthly_ytd_positive_v32_large_liquid_ytd_repair",
    "hkconnect_path6_large_liquid_core_monthly_smoke",
    "hkconnect_path6_lowvol_liquid_biweekly_smoke",
    "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_turnover_control_v34_turnover_control",
    "hkconnect_path7_barbell_monthly_quality_sleeve_v37_barbell_trigger_repair",
    "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3",
]

HK_REFS = {
    "path1": "hkconnect_path1_biweekly_lowvol",
    "path2": "hkconnect_path2_theme_fast_monthly",
    "path3": "hkconnect_path3_equal_elastic_cashoff_weekly",
    "path4": "hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality",
    "path5": "hkconnect_path5_pullback_continuation_monthly_quality_retest_v35_ytd_repair",
    "path6": "hkconnect_path6_lowvol_liquid_biweekly_smoke",
    "path7": "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3",
}

HK_DECISIONS = {
    "path1": ["keep_watch", "keep_watch", "promote"],
    "path2": ["reject", "reject", "reject", "reject", "promote"],
    "path3": ["keep_watch", "keep_watch", "robust_observation"],
    "path4": ["keep_watch", "reject", "robust_observation"],
    "path5": ["keep_watch", "reject", "robust_observation"],
    "path6": ["reject", "keep_watch", "promote"],
    "path7": ["reject", "reject", "promote"],
}

FOCUS = {
    "ashare_path1": "2026急跌CAGR与MaxDD，同时守住相邻2025窗口及换手",
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
    frame = frame[frame["sample_tag"].isin(WINDOWS)].copy()
    return frame.drop_duplicates(["strategy_base_id", "sample_tag"], keep="last")


def metrics(frame: pd.DataFrame, strategy_id: str, sample_tag: str) -> dict[str, float | None]:
    row = frame[(frame["strategy_base_id"] == strategy_id) & (frame["sample_tag"] == sample_tag)]
    if row.empty:
        raise RuntimeError(f"缺少指标: {strategy_id} / {sample_tag}")
    record = row.iloc[-1]
    return {metric: (float(record[metric]) if pd.notna(record[metric]) else None) for metric in METRICS}


def decision_reason(decision: str, d25: dict[str, float | None], d26: dict[str, float | None]) -> str:
    summary = (
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
        "reason": decision_reason(
            decision,
            window_payload["since_2025_01"]["delta"],
            window_payload["since_2026_01"]["delta"],
        ),
        "windows": window_payload,
        "winner_or_robust_changed": False,
        "tracked_payload_changed": False,
    }


def main() -> None:
    a_frames = [pd.read_csv(A_DIR / name) for name in A_FILES]
    a = latest(pd.concat(a_frames, ignore_index=True))
    hk_raw = pd.read_csv(HK_DIR / "strategy_comparison_hkconnect.csv")
    hk = latest(hk_raw.rename(columns={"strategy_id": "strategy_base_id"}))

    cards: list[dict[str, Any]] = []
    a_candidates: list[tuple[str, str, str]] = []
    for key, decision in A_DECISIONS.items():
        rows = a[a["strategy_base_id"].str.contains(key, regex=False, na=False)]
        if key.startswith("v8"):
            rows = rows[rows["strategy_base_id"].str.contains("_total_mv_", regex=False, na=False)]
        elif "weekly_return_recovery" in key:
            rows = rows[rows["strategy_base_id"].str.contains("_equal_weight_", regex=False, na=False)]
        elif key in {"risk_control_v5", "capacity_v2"}:
            rows = rows[rows["strategy_base_id"].str.startswith("core_explore_80_20_total_mv_")]
        ids = sorted(rows["strategy_base_id"].unique())
        if len(ids) != 1:
            raise RuntimeError(f"候选 key 不唯一: {key}: {ids}")
        candidate_id = ids[0]
        if "weekly_return_recovery" in key:
            path, reference = "ashare_path3", P3_REF
        elif key in {"risk_control_v5", "capacity_v2"}:
            path, reference = "ashare_path4", P4_REF
        elif key.startswith("v8"):
            path, reference = "ashare_path2", P2_REF
        else:
            path, reference = "ashare_path1", P1_REF
        a_candidates.append((path, candidate_id, decision))
        cards.append(make_card(a, path, candidate_id, reference, decision))

    path_offsets = {path: 0 for path in HK_DECISIONS}
    for candidate_id in HK_IDS:
        path = candidate_id.split("_")[1]
        index = path_offsets[path]
        decision = HK_DECISIONS[path][index]
        path_offsets[path] += 1
        cards.append(make_card(hk, f"hkconnect_{path}", candidate_id, HK_REFS[path], decision))

    counts = {key: sum(card["decision"] == key for card in cards) for key in ["promote", "keep_watch", "robust_observation", "reject", "archive"]}
    payload = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "data_endpoint": "2026-08-11",
        "candidate_count": len(cards),
        "budget_note": "51 个实际 security/base ids；为定位暴跌脉冲稳定性膝点，缓存完备且 coverage 无阻塞时比48软上限多3个终端点。",
        "winner_validation_policy": "窗口winner使用相邻窗口；本轮2026专项以2025为直接相邻窗，五窗口阈值用于robust二次判断。",
        "delta_definition": "candidate minus current_winner_or_robust; MaxDD positive means improvement",
        "stopping_rule": "触发、确认、持续、冷却与暴露强度均已覆盖；最后两组边界点未形成比pulse40_1w_v17显著更优的稳定性膝点，停止同形扩参。",
        "summary": counts,
        "scorecards": cards,
    }
    output = A_DIR / "research_iteration_scorecard_20260812_iter4.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)
    print(json.dumps(counts, ensure_ascii=False))


if __name__ == "__main__":
    main()
