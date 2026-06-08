#!/usr/bin/env python3
"""Minimal Path5 event basket return probe."""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "results/research/a_share/event_theme_registry.json"
DEFAULT_CANDIDATES = ROOT / "results/research/a_share/event_theme_candidates.jsonl"
DEFAULT_OUTPUT = ROOT / "results/research/a_share/event_theme_backtest_entry.json"
DAILY_DIR = ROOT / "data_cache/daily"
ADJ_DIR = ROOT / "data_cache/adj_factor"
AUDITED_STATUSES = {"approved", "source_audited"}
HORIZONS = (20, 60, 120)


@dataclass
class PricePoint:
    trade_date: str
    adj_close: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--basket-id", required=True)
    parser.add_argument("--sample-tags", default="since_2025_01,since_2026_01")
    parser.add_argument("--registry-json", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--candidates-jsonl", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def load_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_registry(path: Path, basket_id: str) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    for basket in payload.get("baskets", []):
        if basket.get("basket_id") == basket_id:
            return basket
    raise SystemExit(f"basket_id not found: {basket_id}")


def load_adjusted_series(ts_code: str) -> list[PricePoint]:
    daily_path = DAILY_DIR / f"{ts_code}.csv"
    adj_path = ADJ_DIR / f"{ts_code}.csv"
    if not daily_path.exists() or not adj_path.exists():
        raise FileNotFoundError(f"missing daily or adj_factor cache for {ts_code}")

    adj_by_date: dict[str, float] = {}
    with adj_path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            adj_by_date[row["trade_date"]] = float(row["adj_factor"])
    if not adj_by_date:
        raise ValueError(f"empty adj_factor cache for {ts_code}")
    latest_adj = adj_by_date[max(adj_by_date)]

    points: list[PricePoint] = []
    with daily_path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            trade_date = row["trade_date"]
            if trade_date not in adj_by_date:
                continue
            close = float(row["close"])
            adj_close = close * adj_by_date[trade_date] / latest_adj
            points.append(PricePoint(trade_date=trade_date, adj_close=adj_close))
    return sorted(points, key=lambda point: point.trade_date)


def first_index_on_or_after(points: Iterable[PricePoint], event_date: str) -> int | None:
    for idx, point in enumerate(points):
        if point.trade_date >= event_date:
            return idx
    return None


def stock_returns(candidate: dict, event_date: str) -> dict:
    ts_code = candidate["ts_code"]
    points = load_adjusted_series(ts_code)
    start_idx = first_index_on_or_after(points, event_date)
    if start_idx is None:
        return {
            "ts_code": ts_code,
            "name": candidate["name"],
            "role": candidate["role"],
            "weight_seed": candidate["weight_seed"],
            "status": "no_price_after_event",
            "returns": {},
        }

    start_point = points[start_idx]
    returns: dict[str, dict] = {}
    for horizon in HORIZONS:
        end_idx = start_idx + horizon
        if end_idx >= len(points):
            returns[str(horizon)] = {
                "status": "insufficient_data",
                "available_trading_days": len(points) - start_idx - 1,
            }
            continue
        end_point = points[end_idx]
        returns[str(horizon)] = {
            "status": "ok",
            "start_date": start_point.trade_date,
            "end_date": end_point.trade_date,
            "return": end_point.adj_close / start_point.adj_close - 1.0,
        }

    return {
        "ts_code": ts_code,
        "name": candidate["name"],
        "role": candidate["role"],
        "weight_seed": candidate["weight_seed"],
        "source_url": candidate.get("source_url"),
        "status": "ok",
        "returns": returns,
    }


def weighted_return(rows: list[dict], horizon: int, weight_key: str) -> dict:
    usable = [
        row
        for row in rows
        if row.get("returns", {}).get(str(horizon), {}).get("status") == "ok"
    ]
    if not usable:
        return {"status": "insufficient_data", "eligible_count": 0}

    if weight_key == "equal_weight":
        weights = {row["ts_code"]: 1.0 / len(usable) for row in usable}
    else:
        total = sum(float(row.get("weight_seed", 0.0)) for row in usable)
        weights = {row["ts_code"]: float(row.get("weight_seed", 0.0)) / total for row in usable}

    value = sum(
        weights[row["ts_code"]] * row["returns"][str(horizon)]["return"]
        for row in usable
    )
    return {
        "status": "ok",
        "eligible_count": len(usable),
        "return": value,
        "weights": weights,
    }


def main() -> None:
    args = parse_args()
    basket = load_registry(args.registry_json, args.basket_id)
    event_date = basket.get("event_time") or basket.get("report_date")
    if not event_date:
        raise SystemExit("basket missing event_time/report_date")

    candidates = [
        row
        for row in load_jsonl(args.candidates_jsonl)
        if row.get("basket_id") == args.basket_id
        and row.get("audit_status") in AUDITED_STATUSES
        and row.get("include_in_backtest") is True
    ]
    if not candidates:
        raise SystemExit("no audited candidates selected for event basket")

    stock_rows = [stock_returns(candidate, event_date) for candidate in candidates]
    portfolio = {
        str(horizon): {
            "equal_weight": weighted_return(stock_rows, horizon, "equal_weight"),
            "seed_weight": weighted_return(stock_rows, horizon, "seed_weight"),
        }
        for horizon in HORIZONS
    }
    output = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "basket_id": args.basket_id,
        "theme_name": basket.get("theme_name"),
        "event_date": event_date,
        "sample_tags": [tag for tag in args.sample_tags.split(",") if tag],
        "candidate_count": len(candidates),
        "horizons_trading_days": list(HORIZONS),
        "portfolio_returns": portfolio,
        "candidate_returns": stock_rows,
        "notes": "Entry probe only; computes post-event basket returns from audited frozen candidates and does not update official winners.",
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] Wrote {args.output_json}")


if __name__ == "__main__":
    main()
