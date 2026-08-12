#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_DIR = ROOT / "results" / "research" / "a_share"
BACKTEST_DIR = ROOT / "results" / "backtests" / "a_share"
WINDOWS = ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]
METRICS = ["cagr", "sharpe_ratio", "max_drawdown", "average_annual_turnover"]

PATH1_REFERENCE = (
    "core_explore_80_20_total_mv_winner_core__"
    "aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm"
)
PATH2_REFERENCE = (
    "core_explore_60_40_equal_weight_winner_core__"
    "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn"
)
PATH7_REFERENCE = (
    "core_explore_80_20_equal_weight_winner_core__"
    "aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly"
)

CANDIDATES: list[dict[str, str]] = [
    {
        "path": "ashare_path1",
        "candidate_id": "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_risk20_port_fast_crash_drawdown_v1",
        "reference_id": PATH1_REFERENCE,
        "hypothesis": "仅用5周回撤或单周急跌触发全组合20%仓位，预期显著缩小2026年7月回撤。",
        "decision": "reject",
        "reason": "2026回撤改善但since_2020 CAGR下降超过3个百分点，长期稳定性被破坏。",
    },
    {
        "path": "ashare_path1",
        "candidate_id": "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_risk20_port_fast_crash_breadth_v1",
        "reference_id": PATH1_REFERENCE,
        "hypothesis": "仅用20日市场宽度弱化触发全组合降仓，预期比价格信号更早识别内部退潮。",
        "decision": "reject",
        "reason": "弱宽度在正常震荡期频繁触发，五窗口CAGR和Sharpe全面退化。",
    },
    {
        "path": "ashare_path1",
        "candidate_id": "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_risk20_port_fast_crash_combined_v1",
        "reference_id": PATH1_REFERENCE,
        "hypothesis": "短期价格破位与弱宽度同时出现才降到20%，预期减少宽度单信号误报。",
        "decision": "reject",
        "reason": "误报少于宽度单信号，但since_2020 CAGR仍下降超过3个百分点。",
    },
    {
        "path": "ashare_path1",
        "candidate_id": "core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_risk20_port_fast_crash_early_balanced_v2",
        "reference_id": PATH1_REFERENCE,
        "hypothesis": "把联合触发提前到3%短回撤并仅降到40%，恢复缩短到2周，预期改善7月回撤同时减少长期收益损失。",
        "decision": "reject",
        "reason": "2026 CAGR和MaxDD均改善，但2020/2023 CAGR下降远超稳定性阈值，提前触发仍过度交易。",
    },
    {
        "path": "ashare_path2",
        "candidate_id": "core_explore_60_40_equal_weight_winner_core__growth_elastic_v70_port_fast_crash_drawdown_v1",
        "reference_id": PATH2_REFERENCE,
        "hypothesis": "把快跌全组合20%仓位移植到v70，预期控制高弹性池7月尾部风险。",
        "decision": "reject",
        "reason": "触发时间晚且降仓过深，2020与2026 CAGR显著退化，回撤没有改善。",
    },
    {
        "path": "ashare_path2",
        "candidate_id": "core_explore_60_40_equal_weight_winner_core__growth_elastic_v70_port_fast_crash_combined_v1",
        "reference_id": PATH2_REFERENCE,
        "hypothesis": "v70仅在价格破位且市场宽度弱时降到20%，预期降低单信号误报。",
        "decision": "reject",
        "reason": "结果与回撤单信号近似，2020与2026稳定性均被破坏。",
    },
    {
        "path": "ashare_path2",
        "candidate_id": "core_explore_60_40_equal_weight_winner_core__growth_elastic_v70_port_fast_crash_early_balanced_v2",
        "reference_id": PATH2_REFERENCE,
        "hypothesis": "v70在3%短回撤和弱宽度联合出现时降到45%，预期提前一周并保留反弹参与度。",
        "decision": "keep_watch",
        "reason": "2023/2026 CAGR、Sharpe与MaxDD改善，但since_2020 CAGR下降4.65个百分点，尚未通过稳定性护栏。",
    },
    {
        "path": "ashare_path7_crash_resilience",
        "candidate_id": "core_explore_80_20_equal_weight_winner_core__path7_crash_resilience_cash70_weekly30_fast_combined_v1_defbar",
        "reference_id": PATH7_REFERENCE,
        "hypothesis": "70%现金加30%周频进攻形成极防守杠铃，预期把全窗口最大回撤压到10%附近。",
        "decision": "reject",
        "reason": "回撤目标达到，但绝对CAGR过低且2026为负，长期固定低仓位不可用。",
    },
    {
        "path": "ashare_path7_crash_resilience",
        "candidate_id": "core_explore_80_20_equal_weight_winner_core__path7_crash_resilience_cash50_weekly50_fast_combined_v2_defbar",
        "reference_id": PATH7_REFERENCE,
        "hypothesis": "50%现金加50%周频进攻提高收益参与度，同时保留一半防守仓。",
        "decision": "reject",
        "reason": "相对70/30没有形成足够收益补偿，2026仍为负且回撤更差。",
    },
    {
        "path": "ashare_path7_crash_resilience",
        "candidate_id": "core_explore_80_20_equal_weight_winner_core__path7_crash_resilience_cash50_static_fast_pulse_v3_defbar",
        "reference_id": PATH7_REFERENCE,
        "hypothesis": "常态固定50%周频进攻，仅快跌时脉冲降到15%，预期去除慢趋势长期压仓影响。",
        "decision": "keep_watch",
        "reason": "五窗口MaxDD约8%-11%，但CAGR仍弱且2026略负；保留用于下一步加入质量低波防守资产，不进入winner。",
    },
]


def _latest_rows(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    frame = frame[frame["sample_tag"].isin(WINDOWS)].copy()
    return frame.drop_duplicates(["strategy_base_id", "sample_tag"], keep="last")


def _finite_float(value: Any) -> float | None:
    parsed = float(value)
    return parsed if pd.notna(parsed) else None


def _metrics(frame: pd.DataFrame, strategy_id: str, sample_tag: str) -> dict[str, float | None]:
    row = frame[(frame["strategy_base_id"] == strategy_id) & (frame["sample_tag"] == sample_tag)]
    if row.empty:
        raise RuntimeError(f"缺少 scorecard 指标: {strategy_id} / {sample_tag}")
    record = row.iloc[-1]
    return {metric: _finite_float(record[metric]) for metric in METRICS}


def _stress_metrics(strategy_id: str) -> dict[str, Any]:
    base = BACKTEST_DIR / f"{strategy_id}__since_2026_01"
    curve = pd.read_csv(base / "equity_curve.csv", parse_dates=["date"])

    def nav_at(date: str) -> float | None:
        scoped = curve[curve["date"] <= pd.Timestamp(date)]
        return float(scoped.iloc[-1]["nav"]) if not scoped.empty else None

    june_nav = nav_at("2026-06-30")
    july_nav = nav_at("2026-07-31")
    last_nav = float(curve.iloc[-1]["nav"])
    result: dict[str, Any] = {
        "june_30_nav": june_nav,
        "july_31_nav": july_nav,
        "latest_nav": last_nav,
        "july_return": july_nav / june_nav - 1.0 if june_nav and july_nav else None,
        "post_july_recovery": last_nav / july_nav - 1.0 if july_nav else None,
        "peak_to_trough_max_drawdown_2026": float(curve["drawdown"].min()),
    }
    turnover_path = base / "turnover.csv"
    if turnover_path.exists():
        turnover = pd.read_csv(turnover_path)
        if "fast_crash_triggered" in turnover.columns:
            triggered = turnover[turnover["fast_crash_triggered"].astype(str).str.lower() == "true"]
            result["fast_crash_trigger_dates"] = list(map(str, triggered.get("date", [])))
    return result


def main() -> None:
    candidates = _latest_rows(RESEARCH_DIR / "crash_resilience_strategy_comparison.csv")
    references = _latest_rows(RESEARCH_DIR / "strategy_comparison.csv")
    scorecards: list[dict[str, Any]] = []
    for definition in CANDIDATES:
        candidate_id = definition["candidate_id"]
        reference_id = definition["reference_id"]
        windows: dict[str, Any] = {}
        for sample_tag in WINDOWS:
            candidate_metrics = _metrics(candidates, candidate_id, sample_tag)
            reference_metrics = _metrics(references, reference_id, sample_tag)
            windows[sample_tag] = {
                "candidate_metrics": candidate_metrics,
                "current_winner_or_robust_metrics": reference_metrics,
                "delta": {
                    metric: (
                        candidate_metrics[metric] - reference_metrics[metric]
                        if candidate_metrics[metric] is not None and reference_metrics[metric] is not None
                        else None
                    )
                    for metric in METRICS
                },
            }
        scorecards.append(
            {
                **definition,
                "windows": windows,
                "stress_2026": _stress_metrics(candidate_id),
                "winner_or_robust_changed": False,
                "tracked_payload_changed": False,
            }
        )

    payload = {
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "data_endpoint": "2026-08-11",
        "delta_definition": "candidate minus current_winner_or_robust; MaxDD positive means improvement",
        "stability_thresholds": {
            "since_2020_or_2023_cagr_drop": -0.03,
            "since_2020_or_2023_max_drawdown_worsening": -0.05,
            "since_2020_or_2023_sharpe_drop": -0.30,
        },
        "summary": {
            "candidate_count": len(scorecards),
            "promote": 0,
            "keep_watch": sum(item["decision"] == "keep_watch" for item in scorecards),
            "reject": sum(item["decision"] == "reject" for item in scorecards),
            "official_winner_changed": False,
        },
        "scorecards": scorecards,
    }
    output = RESEARCH_DIR / "crash_resilience_scorecard_20260812.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
