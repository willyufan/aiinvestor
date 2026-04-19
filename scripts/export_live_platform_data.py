from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
LIVE_DIR = RESULTS_DIR / "live"
TRACKED_WINNERS_JSON = RESULTS_DIR / "weighted_track_winners.json"
DAILY_CACHE_DIR = ROOT / "data_cache" / "daily"

SAMPLE_LABELS = {
    "since_2017_only": "2017-window winner",
    "since_2020_only": "2020-window winner",
    "since_2023_only": "2023-window winner",
    "since_2025_only": "2025-window winner",
    "robust_candidate": "robust candidate",
}
HISTORY_WINDOW_SNAPSHOTS = 12


def build_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return RESULTS_DIR / f"{base_id}__{sample_tag}" / filename


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _build_weight_history_windows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        frame = pd.read_csv(path)
    except Exception:
        return []
    required = {"date", "ts_code", "name", "weight"}
    if frame.empty or not required.issubset(frame.columns):
        return []
    frame = frame.copy()
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame = frame.dropna(subset=["date"])
    if frame.empty:
        return []
    frame = frame.sort_values(["date", "weight"], ascending=[False, False])
    snapshot_dates = sorted(frame["date"].drop_duplicates().tolist(), reverse=True)
    windows: list[dict[str, Any]] = []
    for idx in range(0, len(snapshot_dates), HISTORY_WINDOW_SNAPSHOTS):
        chunk_dates = snapshot_dates[idx : idx + HISTORY_WINDOW_SNAPSHOTS]
        if not chunk_dates:
            continue
        chunk_rows = frame[frame["date"].isin(chunk_dates)].copy()
        snapshots: list[dict[str, Any]] = []
        for snapshot_date, sub in chunk_rows.groupby("date", sort=False):
            holdings = [
                {
                    "ts_code": str(row["ts_code"]),
                    "name": str(row["name"]),
                    "weight": float(row["weight"]),
                }
                for row in sub.sort_values("weight", ascending=False).to_dict("records")
            ]
            snapshots.append(
                {
                    "date": pd.Timestamp(snapshot_date).strftime("%Y-%m-%d"),
                    "holdings": holdings,
                }
            )
        snapshots.sort(key=lambda item: item["date"], reverse=True)
        window_end = snapshots[0]["date"]
        window_start = snapshots[-1]["date"]
        windows.append(
            {
                "window_index": len(windows),
                "label": f"{window_start} → {window_end}",
                "start_date": window_start,
                "end_date": window_end,
                "snapshot_count": len(snapshots),
                "snapshots": snapshots,
            }
        )
    return windows


def guess_sample_tag(track_key: str) -> str:
    if track_key == "since_2017_only":
        return "since_2017_01"
    if track_key == "since_2020_only":
        return "since_2020_01"
    if track_key == "since_2023_only":
        return "since_2023_01"
    if track_key == "since_2025_only":
        return "since_2025_01"
    return "since_2020_01"


def find_latest_price(ts_code: str) -> float | None:
    path = DAILY_CACHE_DIR / f"{ts_code}.csv"
    if not path.exists():
        return None
    try:
        frame = pd.read_csv(path)
    except Exception:
        return None
    if frame.empty or "close" not in frame.columns:
        return None
    try:
        return float(frame.iloc[-1]["close"])
    except Exception:
        return None


def load_strategy_snapshot(base_id: str, sample_tag: str) -> dict[str, Any]:
    summary_path = build_result_path(base_id, sample_tag, "summary.json")
    if not summary_path.exists():
        raise FileNotFoundError(f"Missing summary for {base_id} / {sample_tag}")
    summary = load_json(summary_path)

    latest_weights_path = build_result_path(base_id, sample_tag, "latest_weights.csv")
    monthly_path = build_result_path(base_id, sample_tag, "monthly_returns.csv")
    weight_history_path = build_result_path(base_id, sample_tag, "weights_history.csv")

    latest_weights: list[dict[str, Any]] = []
    target_exposure = 1.0
    risk_state = "risk_on"

    if latest_weights_path.exists():
        frame = pd.read_csv(latest_weights_path)
        for row in frame.to_dict("records"):
            ts_code = str(row["ts_code"])
            latest_price = find_latest_price(ts_code)
            latest_weights.append(
                {
                    "ts_code": ts_code,
                    "name": str(row["name"]),
                    "weight": float(row["weight"]),
                    "latest_price": latest_price,
                }
            )

    if monthly_path.exists():
        monthly = pd.read_csv(monthly_path)
        if not monthly.empty:
            last = monthly.iloc[-1]
            if "market_exposure_target" in monthly.columns:
                target_exposure = float(last["market_exposure_target"])
            if target_exposure >= 0.999:
                risk_state = "risk_on"
            elif target_exposure <= 0.001:
                risk_state = "risk_off"
            else:
                risk_state = "caution"

    return {
        "strategy_id": base_id,
        "display_name": summary.get("strategy_base_name", base_id),
        "sample_tag": sample_tag,
        "updated_at": summary.get("sample_end"),
        "summary_metrics": summary.get("metrics", {}),
        "windows": {},
        "target_total_exposure": target_exposure,
        "risk_state": risk_state,
        "latest_weights": latest_weights,
        "history_windows": _build_weight_history_windows(weight_history_path),
        "summary_meta": {
            "path": summary.get("strategy_id"),
            "strategy_kind": summary.get("strategy_kind"),
            "base_weight_method": summary.get("base_weight_method"),
            "core_source_mode": summary.get("core_source_mode"),
        },
    }


def export_live_data() -> dict[str, Any]:
    payload = load_json(TRACKED_WINNERS_JSON)
    strategies_map: dict[str, Any] = payload["strategies"]

    registry: list[dict[str, Any]] = []
    dedup: dict[str, dict[str, Any]] = {}

    def add_entry(*, path_name: str, winner_type: str, strategy_id: str, sample_tag: str) -> None:
        if strategy_id in dedup:
            dedup[strategy_id]["winner_tags"].append(f"{path_name}:{winner_type}")
            return
        tracked_info = strategies_map[strategy_id]
        snapshot = load_strategy_snapshot(strategy_id, sample_tag)
        snapshot["path"] = path_name
        snapshot["winner_type"] = winner_type
        snapshot["winner_tags"] = [f"{path_name}:{winner_type}"]
        snapshot["windows"] = tracked_info["windows"]
        dedup[strategy_id] = snapshot

    for track_key, track_meta in payload["tracks"].items():
        if track_key == "robust_candidate":
            continue
        strategy_id = str(track_meta["winner"])
        add_entry(
            path_name="path1",
            winner_type=SAMPLE_LABELS.get(track_key, track_key),
            strategy_id=strategy_id,
            sample_tag=guess_sample_tag(track_key),
        )

    robust_meta = payload["tracks"].get("robust_candidate")
    if robust_meta:
        add_entry(
            path_name="path1",
            winner_type="robust candidate",
            strategy_id=str(robust_meta["strategy_base_id"]),
            sample_tag="since_2020_01",
        )

    for track_key, track_meta in payload["path2"]["tracks"].items():
        strategy_id = str(track_meta["winner"])
        add_entry(
            path_name="path2",
            winner_type=SAMPLE_LABELS.get(track_key, track_key),
            strategy_id=strategy_id,
            sample_tag=guess_sample_tag(track_key),
        )

    path2_robust = payload["path2"].get("strategy_base_id")
    if path2_robust:
        add_entry(
            path_name="path2",
            winner_type="robust candidate",
            strategy_id=str(path2_robust),
            sample_tag="since_2020_01",
        )

    registry = sorted(
        dedup.values(),
        key=lambda item: (
            item["path"],
            item["winner_type"],
            -float(item["summary_metrics"].get("cagr", 0.0)),
        ),
    )

    LIVE_DIR.mkdir(parents=True, exist_ok=True)
    (LIVE_DIR / "strategies").mkdir(parents=True, exist_ok=True)
    for item in registry:
        strategy_path = LIVE_DIR / "strategies" / f"{item['strategy_id']}.json"
        strategy_path.write_text(json.dumps(item, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    registry_payload = {
        "as_of": payload["as_of"],
        "strategies": [
            {
                "strategy_id": item["strategy_id"],
                "display_name": item["display_name"],
                "path": item["path"],
                "winner_type": item["winner_type"],
                "winner_tags": item["winner_tags"],
                "target_total_exposure": item["target_total_exposure"],
                "risk_state": item["risk_state"],
                "summary_metrics": item["summary_metrics"],
                "updated_at": item["updated_at"],
            }
            for item in registry
        ],
    }
    (LIVE_DIR / "strategy_registry.json").write_text(
        json.dumps(registry_payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return registry_payload


def main() -> None:
    payload = export_live_data()
    print(f"[OK] Exported {len(payload['strategies'])} live strategies to {LIVE_DIR}")


if __name__ == "__main__":
    main()
