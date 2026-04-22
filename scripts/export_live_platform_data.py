from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RESULTS_DIR = ROOT / "results"
HK_RESULTS_DIR = ROOT / "results_hkconnect"
LIVE_DIR = RESULTS_DIR / "live"
TRACKED_WINNERS_JSON = RESULTS_DIR / "weighted_track_winners.json"
DAILY_CACHE_DIR = ROOT / "data_cache" / "daily"
HK_DAILY_CACHE_DIR = ROOT / "data_cache" / "hkconnect" / "daily_adj"

SAMPLE_LABELS = {
    "since_2017_only": "2017-window winner",
    "since_2020_only": "2020-window winner",
    "since_2023_only": "2023-window winner",
    "since_2025_only": "2025-window winner",
    "robust_candidate": "robust candidate",
}
HISTORY_WINDOW_SNAPSHOTS = 12
SAMPLE_TAGS = ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]
SAMPLE_TAG_LABELS = {
    "since_2017_01": "2017窗口",
    "since_2020_01": "2020窗口",
    "since_2023_01": "2023窗口",
    "since_2025_01": "2025窗口",
    "since_2026_01": "2026观察窗",
}


def build_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return RESULTS_DIR / f"{base_id}__{sample_tag}" / filename


def build_hk_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return HK_RESULTS_DIR / f"{base_id}__{sample_tag}" / filename


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _collect_windows(base_id: str, *, market_scope: str = "a_share") -> dict[str, Any]:
    path_builder = build_hk_result_path if market_scope == "hkconnect" else build_result_path
    windows: dict[str, Any] = {}
    for sample_tag in SAMPLE_TAGS:
        summary_path = path_builder(base_id, sample_tag, "summary.json")
        if not summary_path.exists():
            continue
        try:
            summary = load_json(summary_path)
            metrics = summary.get("metrics", {})
            windows[sample_tag] = {
                "total_return": float(metrics.get("total_return", 0.0)),
                "cagr": float(metrics.get("cagr", 0.0)),
                "max_drawdown": float(metrics.get("max_drawdown", 0.0)),
                "sharpe": float(metrics.get("sharpe_ratio", 0.0)),
                "turnover": float(metrics.get("average_annual_turnover", 0.0)),
                "sample_start": summary.get("sample_start"),
                "sample_end": summary.get("sample_end"),
            }
        except Exception:
            continue
    return windows


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


def _load_equity_curve_points(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    try:
        frame = pd.read_csv(path)
    except Exception:
        return []
    required = {"date", "nav"}
    if frame.empty or not required.issubset(frame.columns):
        return []
    points: list[dict[str, Any]] = []
    for row in frame.to_dict("records"):
        try:
            points.append(
                {
                    "date": str(row["date"]),
                    "nav": float(row["nav"]),
                    "drawdown": float(row.get("drawdown", 0.0)),
                }
            )
        except Exception:
            continue
    return points


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
    cache_dir = HK_DAILY_CACHE_DIR if ts_code.endswith(".HK") else DAILY_CACHE_DIR
    path = cache_dir / f"{ts_code}.csv"
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


def _load_sample_view(base_id: str, sample_tag: str, *, market_scope: str = "a_share") -> dict[str, Any] | None:
    path_builder = build_hk_result_path if market_scope == "hkconnect" else build_result_path
    summary_path = path_builder(base_id, sample_tag, "summary.json")
    if not summary_path.exists():
        return None
    summary = load_json(summary_path)

    latest_weights_path = path_builder(base_id, sample_tag, "latest_weights.csv")
    monthly_path = path_builder(base_id, sample_tag, "monthly_returns.csv")
    weight_history_path = path_builder(base_id, sample_tag, "weights_history.csv")
    equity_curve_path = path_builder(base_id, sample_tag, "equity_curve.csv")

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
        "sample_tag": sample_tag,
        "sample_tag_label": SAMPLE_TAG_LABELS.get(sample_tag, sample_tag),
        "updated_at": summary.get("sample_end"),
        "rebalance_frequency": summary.get("rebalance_frequency", "monthly"),
        "summary_metrics": summary.get("metrics", {}),
        "target_total_exposure": target_exposure,
        "risk_state": risk_state,
        "latest_weights": latest_weights,
        "history_windows": _build_weight_history_windows(weight_history_path),
        "equity_curve_points": _load_equity_curve_points(equity_curve_path),
        "summary_meta": {
            "sample_start": summary.get("sample_start"),
            "sample_end": summary.get("sample_end"),
            "sample_label": summary.get("sample_label"),
            "sample_short_label": summary.get("sample_short_label"),
            "strategy_name": summary.get("strategy_name"),
            "strategy_base_name": summary.get("strategy_base_name"),
            "path": summary.get("strategy_id"),
            "strategy_kind": summary.get("strategy_kind"),
            "base_weight_method": summary.get("base_weight_method"),
            "core_source_mode": summary.get("core_source_mode"),
            "rebalance_frequency": summary.get("rebalance_frequency", "monthly"),
        },
    }


def load_strategy_snapshot(base_id: str, sample_tag: str, *, market_scope: str = "a_share") -> dict[str, Any]:
    sample_view = _load_sample_view(base_id, sample_tag, market_scope=market_scope)
    if sample_view is None:
        raise FileNotFoundError(f"Missing summary for {base_id} / {sample_tag}")
    sample_views: dict[str, Any] = {}
    for tag in SAMPLE_TAGS:
        view = _load_sample_view(base_id, tag, market_scope=market_scope)
        if view is not None:
            sample_views[tag] = view

    display_name = (
        sample_view.get("summary_meta", {}).get("strategy_base_name")
        or sample_view.get("summary_meta", {}).get("strategy_name")
        or base_id
    )
    return {
        "strategy_id": base_id,
        "display_name": display_name,
        "sample_tag": sample_tag,
        "updated_at": sample_view["updated_at"],
        "rebalance_frequency": sample_view["rebalance_frequency"],
        "summary_metrics": sample_view["summary_metrics"],
        "windows": _collect_windows(base_id, market_scope=market_scope),
        "sample_views": sample_views,
        "target_total_exposure": sample_view["target_total_exposure"],
        "risk_state": sample_view["risk_state"],
        "latest_weights": sample_view["latest_weights"],
        "history_windows": sample_view["history_windows"],
        "equity_curve_points": sample_view["equity_curve_points"],
        "summary_meta": sample_view["summary_meta"],
        "market_scope": market_scope,
    }


def _pick_hk_robust_candidate(df: pd.DataFrame, path_name: str) -> str | None:
    subset = df[df["path"] == path_name].copy()
    if subset.empty:
        return None
    metrics_rows: list[dict[str, Any]] = []
    for strategy_id, sub in subset.groupby("strategy_id"):
        metrics_rows.append(
            {
                "strategy_id": strategy_id,
                "avg_cagr": float(sub["cagr"].mean()),
                "min_cagr": float(sub["cagr"].min()),
                "avg_sharpe": float(sub["sharpe_ratio"].mean()),
                "worst_dd": float(sub["max_drawdown"].min()),
                "avg_turn": float(sub["average_annual_turnover"].mean()),
            }
        )
    ranked = pd.DataFrame(metrics_rows).sort_values(
        ["avg_cagr", "min_cagr", "avg_sharpe", "worst_dd", "avg_turn"],
        ascending=[False, False, False, False, True],
    )
    return str(ranked.iloc[0]["strategy_id"]) if not ranked.empty else None


def load_hkconnect_registry() -> list[dict[str, Any]]:
    comparison_path = HK_RESULTS_DIR / "strategy_comparison_hkconnect.csv"
    if not comparison_path.exists():
        return []
    try:
        df = pd.read_csv(comparison_path)
    except Exception:
        return []
    required = {"sample_tag", "path", "strategy_id", "cagr", "max_drawdown", "sharpe_ratio", "average_annual_turnover"}
    if df.empty or not required.issubset(df.columns):
        return []

    dedup: dict[str, dict[str, Any]] = {}

    def add_entry(*, path_name: str, winner_type: str, strategy_id: str, sample_tag: str) -> None:
        if strategy_id in dedup:
            dedup[strategy_id]["winner_tags"].append(f"hkconnect:{path_name}:{winner_type}")
            return
        snapshot = load_strategy_snapshot(strategy_id, sample_tag, market_scope="hkconnect")
        snapshot["path"] = path_name
        snapshot["winner_type"] = winner_type
        snapshot["winner_tags"] = [f"hkconnect:{path_name}:{winner_type}"]
        snapshot["market_scope"] = "hkconnect"
        dedup[strategy_id] = snapshot

    for sample_tag, winner_type in [
        ("since_2017_01", "2017-window winner"),
        ("since_2020_01", "2020-window winner"),
        ("since_2023_01", "2023-window winner"),
        ("since_2025_01", "2025-window winner"),
    ]:
        sample_df = df[df["sample_tag"] == sample_tag]
        for path_name in ("path1", "path2"):
            sub = sample_df[sample_df["path"] == path_name].sort_values(["cagr", "sharpe_ratio"], ascending=[False, False])
            if sub.empty:
                continue
            add_entry(
                path_name=path_name,
                winner_type=winner_type,
                strategy_id=str(sub.iloc[0]["strategy_id"]),
                sample_tag=sample_tag,
            )

    for path_name in ("path1", "path2"):
        robust_id = _pick_hk_robust_candidate(df, path_name)
        if robust_id:
            add_entry(
                path_name=path_name,
                winner_type="robust candidate",
                strategy_id=robust_id,
                sample_tag="since_2020_01",
            )

    return list(dedup.values())


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
        snapshot = load_strategy_snapshot(strategy_id, sample_tag, market_scope="a_share")
        snapshot["path"] = path_name
        snapshot["winner_type"] = winner_type
        snapshot["winner_tags"] = [f"{path_name}:{winner_type}"]
        snapshot["windows"] = tracked_info["windows"]
        snapshot["market_scope"] = "a_share"
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

    registry = list(dedup.values())
    registry.extend(load_hkconnect_registry())
    registry = sorted(
        registry,
        key=lambda item: (
            item.get("market_scope", "a_share"),
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
                "market_scope": item.get("market_scope", "a_share"),
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
