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
DEFAULT_PATH4_STRATEGY_DIR = ROOT / "results/research/a_share/strategies"
DEFAULT_PATH4_REFERENCE_STRATEGY_ID = (
    "core_explore_80_20_total_mv_winner_core__"
    "aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn"
)
DAILY_DIR = ROOT / "data_cache/daily"
ADJ_DIR = ROOT / "data_cache/adj_factor"
AUDITED_STATUSES = {"approved", "source_audited"}
DEFAULT_HORIZONS = (20, 40, 60)


@dataclass
class PricePoint:
    trade_date: str
    adj_close: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--basket-id", required=True)
    parser.add_argument("--sample-tags", default="since_2025_01,since_2026_01")
    parser.add_argument("--horizons", default=",".join(str(horizon) for horizon in DEFAULT_HORIZONS))
    parser.add_argument("--registry-json", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--candidates-jsonl", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--path4-reference-strategy-id", default=DEFAULT_PATH4_REFERENCE_STRATEGY_ID)
    parser.add_argument("--path4-sample-tag", default="since_2026_01")
    return parser.parse_args()


def parse_horizons(raw: str) -> tuple[int, ...]:
    horizons = tuple(int(item) for item in raw.split(",") if item.strip())
    if not horizons or any(horizon <= 0 for horizon in horizons):
        raise SystemExit("--horizons must contain positive integer trading-day windows")
    return horizons


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


def stock_returns(candidate: dict, event_date: str, horizons: tuple[int, ...]) -> dict:
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
    for horizon in horizons:
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


def normalize_date(raw_date: object) -> str:
    return str(raw_date or "").strip()[:10]


def load_path4_weights_as_of(strategy_id: str, sample_tag: str, event_date: str) -> dict:
    path = DEFAULT_PATH4_STRATEGY_DIR / f"{strategy_id}.json"
    if not path.exists():
        return {
            "status": "missing_reference_strategy",
            "strategy_id": strategy_id,
            "sample_tag": sample_tag,
            "event_date": event_date,
            "reference_as_of": None,
            "path": str(path.relative_to(ROOT)),
            "weights": [],
        }
    payload = json.loads(path.read_text(encoding="utf-8"))
    sample_view = payload.get("sample_views", {}).get(sample_tag, {})
    event_day = normalize_date(event_date)
    snapshots = [
        snapshot
        for snapshot in sample_view.get("snapshots", [])
        if normalize_date(snapshot.get("date"))
        and normalize_date(snapshot.get("date")) <= event_day
        and snapshot.get("holdings")
    ]
    if not snapshots:
        return {
            "status": "missing_reference_snapshot",
            "strategy_id": strategy_id,
            "sample_tag": sample_tag,
            "event_date": event_date,
            "reference_as_of": None,
            "path": str(path.relative_to(ROOT)),
            "weights": [],
        }
    reference_snapshot = max(snapshots, key=lambda snapshot: normalize_date(snapshot.get("date")))
    reference_as_of = normalize_date(reference_snapshot.get("date"))
    if reference_as_of > event_day:
        raise SystemExit(f"Path4 reference snapshot {reference_as_of} is after event date {event_day}")
    weights = [
        row
        for row in reference_snapshot.get("holdings", [])
        if row.get("ts_code") and row.get("ts_code") != "CASH"
    ]
    if not weights:
        return {
            "status": "missing_reference_weights",
            "strategy_id": strategy_id,
            "sample_tag": sample_tag,
            "event_date": event_date,
            "reference_as_of": reference_as_of,
            "path": str(path.relative_to(ROOT)),
            "weights": [],
        }
    return {
        "status": "ok",
        "strategy_id": strategy_id,
        "sample_tag": sample_tag,
        "event_date": event_date,
        "reference_as_of": reference_as_of,
        "path": str(path.relative_to(ROOT)),
        "weights": weights,
    }


def path4_reference_overlap(candidates: list[dict], strategy_id: str, sample_tag: str, event_date: str) -> dict:
    reference = load_path4_weights_as_of(strategy_id, sample_tag, event_date)
    if reference["status"] != "ok":
        return reference

    candidate_by_code = {row["ts_code"]: row for row in candidates}
    path4_by_code = {row["ts_code"]: row for row in reference["weights"]}
    overlap_codes = sorted(set(candidate_by_code) & set(path4_by_code))
    seed_total = sum(float(row.get("weight_seed", 0.0)) for row in candidates)
    path4_overlap_weight = sum(float(path4_by_code[code].get("weight", 0.0)) for code in overlap_codes)
    seed_overlap_weight = (
        sum(float(candidate_by_code[code].get("weight_seed", 0.0)) for code in overlap_codes) / seed_total
        if seed_total > 0
        else None
    )
    return {
        "status": "ok",
        "strategy_id": strategy_id,
        "sample_tag": sample_tag,
        "event_date": event_date,
        "reference_as_of": reference["reference_as_of"],
        "candidate_count": len(candidates),
        "path4_holding_count": len(path4_by_code),
        "overlap_count": len(overlap_codes),
        "overlap_ratio_of_basket": len(overlap_codes) / len(candidates) if candidates else 0.0,
        "overlap_ratio_of_path4": len(overlap_codes) / len(path4_by_code) if path4_by_code else 0.0,
        "path4_overlap_weight": path4_overlap_weight,
        "seed_overlap_weight": seed_overlap_weight,
        "overlap_holdings": [
            {
                "ts_code": code,
                "name": candidate_by_code[code].get("name") or path4_by_code[code].get("name"),
                "role": candidate_by_code[code].get("role"),
                "seed_weight": candidate_by_code[code].get("weight_seed"),
                "path4_weight": path4_by_code[code].get("weight"),
            }
            for code in overlap_codes
        ],
    }


def main() -> None:
    args = parse_args()
    horizons = parse_horizons(args.horizons)
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

    stock_rows = [stock_returns(candidate, event_date, horizons) for candidate in candidates]
    portfolio = {
        str(horizon): {
            "equal_weight": weighted_return(stock_rows, horizon, "equal_weight"),
            "seed_weight": weighted_return(stock_rows, horizon, "seed_weight"),
        }
        for horizon in horizons
    }
    output = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "basket_id": args.basket_id,
        "alpha_pool_profile": "event_kg_basket",
        "pool_id": "path5_event_kg_basket",
        "pool_name": "Path5 事件知识图谱冻结篮子",
        "theme_name": basket.get("theme_name"),
        "event_date": event_date,
        "sample_tags": [tag for tag in args.sample_tags.split(",") if tag],
        "candidate_count": len(candidates),
        "horizons_trading_days": list(horizons),
        "portfolio_returns": portfolio,
        "candidate_returns": stock_rows,
        "path4_reference_overlap": path4_reference_overlap(
            candidates,
            args.path4_reference_strategy_id,
            args.path4_sample_tag,
            event_date,
        ),
        "notes": "Entry probe only; computes post-event basket returns from audited frozen candidates and does not update official winners.",
    }
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] Wrote {args.output_json}")


if __name__ == "__main__":
    main()
