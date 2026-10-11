#!/usr/bin/env python3
"""同窗口冻结策略的风险阶段收益/费用描述性归因，不作因果推断。"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


def compare_periods(candidate, reference):
    required = ["date", "gross_return", "net_return", "trading_cost", "market_risk_off"]
    a, b = candidate[required].copy(), reference[required].copy()
    if a.date.duplicated().any() or b.date.duplicated().any():
        raise ValueError("收益日期重复")
    if set(a.date) != set(b.date):
        raise ValueError("候选和参照收益日期不一致")
    merged = a.merge(b, on="date", suffixes=("_candidate", "_reference"), validate="one_to_one")
    if not merged.market_risk_off_candidate.equals(merged.market_risk_off_reference):
        raise ValueError("风险阶段不同，不能按共同风险组归因")
    groups = {}
    for risk_off, group in merged.groupby("market_risk_off_reference"):
        row = {"period_count": len(group)}
        for role in ["candidate", "reference"]:
            for kind in ["gross", "net"]:
                values = group[f"{kind}_return_{role}"]
                if not np.isfinite(values).all() or (values <= -1).any():
                    raise ValueError("无效收益")
                row[f"{role}_{kind}_log_return"] = float(np.log1p(values).sum())
            row[f"{role}_cost_log_drag"] = row[f"{role}_gross_log_return"] - row[f"{role}_net_log_return"]
            row[f"{role}_recorded_trading_cost_sum"] = float(group[f"trading_cost_{role}"].sum())
        for kind in ["gross_log_return", "net_log_return", "cost_log_drag"]:
            row[f"delta_{kind}"] = row[f"candidate_{kind}"] - row[f"reference_{kind}"]
        groups["risk_off" if risk_off else "risk_on_or_caution"] = row
    return {"matched_periods": len(merged), "risk_groups": groups,
            "interpretation": "各组可加总的对数收益贡献；不是各阶段独立CAGR，也不是因果识别"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--backtest-root", required=True, type=Path)
    parser.add_argument("--candidate-id", required=True)
    parser.add_argument("--reference-id", required=True)
    parser.add_argument("--sample-tags", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--output-json", required=True, type=Path)
    args = parser.parse_args()
    output = {"candidate_id": args.candidate_id, "reference_id": args.reference_id,
              "end_date": args.end_date, "windows": {}}
    for window in args.sample_tags.split(","):
        frames = {}
        exposure = {}
        for role, sid in [("candidate", args.candidate_id), ("reference", args.reference_id)]:
            directory = args.backtest_root / (sid + "__" + window)
            summary = json.loads((directory / "summary.json").read_text())
            if pd.Timestamp(summary["sample_end"]) != pd.Timestamp(args.end_date):
                raise ValueError("归因策略截止日不一致")
            frames[role] = pd.read_csv(directory / "monthly_returns.csv")
            weights = pd.read_csv(directory / "weights_history.csv")
            dates = weights.date.unique()
            stocks = weights[weights.ts_code != "CASH"]
            daily = stocks.groupby("date").weight.sum().reindex(dates, fill_value=0.)
            exposure[role] = {"recorded_stock_weight_mean": float(daily.mean()),
                              "recorded_stock_weight_max": float(daily.max())}
        output["windows"][window] = {**compare_periods(frames["candidate"], frames["reference"]),
                                     "recorded_exposure": exposure}
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(output, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


if __name__ == "__main__":
    main()
