from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backtest_hkconnect import HK_ARCHIVED_STRATEGY_IDS, HK_PATH8_VARIANTS
from backtest_marketcap_etf import PATH6_SHORT_WINDOW_BASE_IDS
from scripts.results_layout import existing_research_file, research_file


WINDOWS = ("since_2025_01", "since_2026_01")
A_COMPARISON = existing_research_file("strategy_comparison_base_method.csv")
HK_COMPARISON = existing_research_file("strategy_comparison_hkconnect.csv", market_scope="hkconnect")
A_OUTPUT = research_file("path6_short_window_scorecard.json")
HK_OUTPUT = research_file("path8_short_window_scorecard.json", market_scope="hkconnect")
METRIC_COLUMNS = ("cagr", "sharpe_ratio", "max_drawdown", "average_annual_turnover")


def _latest_rows(frame: pd.DataFrame, id_column: str) -> pd.DataFrame:
    typed = frame.copy()
    typed["sample_end"] = pd.to_datetime(typed["sample_end"], errors="coerce")
    typed = typed.dropna(subset=["sample_end"])
    return (
        typed.sort_values([id_column, "sample_tag", "sample_end"])
        .groupby([id_column, "sample_tag"], as_index=False)
        .tail(1)
    )


def _metrics(row: pd.Series) -> dict[str, Any]:
    payload = {column: float(row[column]) for column in METRIC_COLUMNS}
    payload["cumulative_trading_cost"] = float(row.get("cumulative_trading_cost", 0.0))
    payload["sample_start"] = str(pd.Timestamp(row["sample_start"]).date())
    payload["sample_end"] = str(pd.Timestamp(row["sample_end"]).date())
    return payload


def _delta(candidate: dict[str, Any], benchmark: dict[str, Any]) -> dict[str, float]:
    return {
        column: float(candidate[column]) - float(benchmark[column])
        for column in (*METRIC_COLUMNS, "cumulative_trading_cost")
    }


def _hypothesis(candidate_id: str) -> str:
    if "weekly_breakout" in candidate_id:
        return "提高调仓频率并集中到短动量/突破标的，预期同时抬升 2025 与 2026 CAGR。"
    if "weekly_balanced" in candidate_id:
        return "用周频均衡信号替代单一突破，预期在保留 2026 弹性的同时降低回撤。"
    if "weekly_pullback" in candidate_id:
        return "用周频回踩与熊市空仓捕捉短窗反弹，预期改善 2025 CAGR 并控制回撤。"
    if "monthly_3_1" in candidate_id:
        return "用月频 3-1 动量和两只集中仓降低交易噪声，预期改善 2025 收益并保留 2026 正收益。"
    if "monthly_midcycle" in candidate_id:
        return "用月频中周期动量和三只集中仓平衡短窗收益与换手成本。"
    if "monthly_top6" in candidate_id:
        return "用月频短动量六只集中仓降低周频噪声，预期在 2025/2026 两窗保持正收益。"
    if "monthly_top10_fullrisk" in candidate_id:
        return "用月频短动量与全风险敞口提高上行捕获，预期抬升 2025/2026 CAGR。"
    if "biweekly" in candidate_id:
        return "用双周短动量在收益与换手间折中，预期优于既有 HK Path4-7 的 2026 表现。"
    if "weekly" in candidate_id:
        return "用周频短动量快速追踪领涨股，预期挑战现有 HK 短窗收益冠军。"
    return "以短动量、突破和集中持仓挑战现有 2025/2026 收益冠军。"


def _decision(candidate_windows: dict[str, dict[str, Any]], benchmark_windows: dict[str, dict[str, Any]]) -> tuple[str, str]:
    cagrs = [float(candidate_windows[window]["cagr"]) for window in WINDOWS]
    turnovers = [float(candidate_windows[window]["average_annual_turnover"]) for window in WINDOWS]
    drawdowns = [float(candidate_windows[window]["max_drawdown"]) for window in WINDOWS]
    beats_both = all(
        candidate_windows[window]["cagr"] > benchmark_windows[window]["cagr"]
        for window in WINDOWS
    )
    if beats_both and min(drawdowns) >= -0.50:
        return "promote", "两个目标窗口 CAGR 均超过同截止日现有冠军，且最大回撤未触及灾难性下限。"
    if min(cagrs) > 0.0:
        return "keep_watch", "两个目标窗口均为正收益，但 CAGR 尚未同时超过现有短窗冠军。"
    if max(cagrs) >= 0.35 and min(cagrs) >= -0.15 and max(turnovers) <= 12.0:
        return "keep_watch", "一个目标窗口有明显弹性，另一窗口小幅为负且换手尚可；保留至下一轮修复。"
    return "reject", "未能在两个目标窗口形成可持续正收益，或高换手/回撤代价不支持继续同形扩参。"


def _build_scorecard(
    *,
    frame: pd.DataFrame,
    id_column: str,
    candidate_ids: list[str],
    archived_ids: set[str],
    market: str,
    path: str,
) -> dict[str, Any]:
    latest = _latest_rows(frame, id_column)
    candidates = latest[
        latest[id_column].astype(str).isin(candidate_ids)
        & latest["sample_tag"].astype(str).isin(WINDOWS)
    ].copy()
    missing = {
        candidate_id: sorted(set(WINDOWS) - set(candidates.loc[candidates[id_column] == candidate_id, "sample_tag"].astype(str)))
        for candidate_id in candidate_ids
    }
    missing = {candidate_id: windows for candidate_id, windows in missing.items() if windows}
    if missing:
        raise RuntimeError(f"{path} scorecard coverage incomplete: {missing}")

    candidate_as_of_values = sorted(pd.Timestamp(value) for value in candidates["sample_end"].unique())
    if len(candidate_as_of_values) != 1:
        candidate_dates = {
            candidate_id: sorted(
                str(pd.Timestamp(value).date())
                for value in candidates.loc[
                    candidates[id_column].astype(str) == candidate_id,
                    "sample_end",
                ].unique()
            )
            for candidate_id in candidate_ids
        }
        raise RuntimeError(f"{path} scorecard candidates have mixed sample_end dates: {candidate_dates}")
    candidate_as_of = candidate_as_of_values[0]
    benchmark_pool = latest[
        ~latest[id_column].astype(str).isin(set(candidate_ids) | set(archived_ids))
        & latest["sample_tag"].astype(str).isin(WINDOWS)
        & (latest["sample_end"] == candidate_as_of)
    ].copy()
    benchmark_rows: dict[str, pd.Series] = {}
    for window in WINDOWS:
        window_rows = benchmark_pool[benchmark_pool["sample_tag"].astype(str) == window]
        if window_rows.empty:
            raise RuntimeError(f"No same-as-of benchmark for {market} {window} at {candidate_as_of.date()}")
        benchmark_rows[window] = window_rows.sort_values(
            ["cagr", "sharpe_ratio", "max_drawdown", "average_annual_turnover", id_column],
            ascending=[False, False, False, True, True],
        ).iloc[0]
    benchmark_windows = {window: _metrics(row) for window, row in benchmark_rows.items()}

    scorecards = []
    for candidate_id in candidate_ids:
        group = candidates[candidates[id_column].astype(str) == candidate_id]
        candidate_windows = {
            window: _metrics(group[group["sample_tag"].astype(str) == window].iloc[0])
            for window in WINDOWS
        }
        decision, reason = _decision(candidate_windows, benchmark_windows)
        scorecards.append(
            {
                "candidate_id": candidate_id,
                "hypothesis": _hypothesis(candidate_id),
                "windows": list(WINDOWS),
                "candidate_metrics": candidate_windows,
                "current_winner_or_robust": {
                    window: {
                        "candidate_id": str(benchmark_rows[window][id_column]),
                        "metrics": benchmark_windows[window],
                    }
                    for window in WINDOWS
                },
                "delta": {
                    window: _delta(candidate_windows[window], benchmark_windows[window])
                    for window in WINDOWS
                },
                "decision": decision,
                "reason": reason,
            }
        )

    window_winners = {}
    for window in WINDOWS:
        row = candidates[candidates["sample_tag"].astype(str) == window].sort_values(
            ["cagr", "sharpe_ratio", "max_drawdown", "average_annual_turnover", id_column],
            ascending=[False, False, False, True, True],
        ).iloc[0]
        window_winners[window] = {"candidate_id": str(row[id_column]), "metrics": _metrics(row)}
    return {
        "market": market,
        "path": path,
        "objective": "maximize_cagr_on_since_2025_01_and_since_2026_01",
        "as_of": str(candidate_as_of.date()),
        "window_winners": window_winners,
        "scorecards": scorecards,
        "interpretation_guard": "路径内短窗领先不等于跨窗口 robust winner；未跑 2017/2020/2023 时不得作强稳定性结论。",
    }


def main() -> None:
    a_payload = _build_scorecard(
        frame=pd.read_csv(A_COMPARISON),
        id_column="strategy_base_id",
        candidate_ids=list(PATH6_SHORT_WINDOW_BASE_IDS),
        archived_ids=set(),
        market="ashare",
        path="path6",
    )
    hk_payload = _build_scorecard(
        frame=pd.read_csv(HK_COMPARISON),
        id_column="strategy_id",
        candidate_ids=[str(item["strategy_id"]) for item in HK_PATH8_VARIANTS],
        archived_ids=set(HK_ARCHIVED_STRATEGY_IDS),
        market="hkconnect",
        path="path8",
    )
    for output, payload in ((A_OUTPUT, a_payload), (HK_OUTPUT, hk_payload)):
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
        print(f"[OK] wrote {output}")


if __name__ == "__main__":
    main()
