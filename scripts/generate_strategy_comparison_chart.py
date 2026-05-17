from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "data_cache" / "mplconfig"))

import matplotlib
import pandas as pd
import numpy as np

matplotlib.use("Agg")
from matplotlib import font_manager
from matplotlib import colors as mcolors

from scripts.results_layout import existing_research_file, existing_strategy_result_dir, existing_strategy_result_file


def _configure_matplotlib_fonts() -> None:
    candidates = [
        "PingFang SC",
        "Heiti SC",
        "Songti SC",
        "STHeiti",
        "Noto Sans CJK SC",
        "Noto Sans SC",
        "Microsoft YaHei",
        "SimHei",
        "Arial Unicode MS",
    ]
    available = {font.name for font in font_manager.fontManager.ttflist}
    chosen = next((name for name in candidates if name in available), None)
    if chosen:
        matplotlib.rcParams["font.family"] = "sans-serif"
        matplotlib.rcParams["font.sans-serif"] = [chosen, "DejaVu Sans"]
    matplotlib.rcParams["axes.unicode_minus"] = False


import matplotlib.pyplot as plt


DOCS_DIR = ROOT / "docs"
OUTPUT_PATHS = {
    "since_2017_01": DOCS_DIR / "strategy_comparison_since_2017_01.png",
    "since_2020_01": DOCS_DIR / "strategy_comparison_since_2020_01.png",
    "since_2023_01": DOCS_DIR / "strategy_comparison_since_2023_01.png",
    "since_2025_01": DOCS_DIR / "strategy_comparison_since_2025_01.png",
    "since_2026_01": DOCS_DIR / "strategy_comparison_since_2026_01.png",
}
SUMMARY_OUTPUT_PATH = DOCS_DIR / "strategy_tracked_winners_summary.png"
FAMILY_OUTPUT_PATHS = {
    "since_2017_01": DOCS_DIR / "strategy_family_since_2017_01.png",
    "since_2020_01": DOCS_DIR / "strategy_family_since_2020_01.png",
    "since_2023_01": DOCS_DIR / "strategy_family_since_2023_01.png",
    "since_2025_01": DOCS_DIR / "strategy_family_since_2025_01.png",
}
COMPARISON_CSV = existing_research_file("strategy_comparison_base_method.csv")
WEIGHTED_WINNERS_JSON = existing_research_file("weighted_track_winners.json")
CORE_ACTIVE_REGISTRY_JSON = existing_research_file("core_active_registry.json")
BACKTEST_SCRIPT_PATH = ROOT / "backtest_marketcap_etf.py"

SAMPLE_WINDOWS = [
    {"sample_tag": "since_2017_01", "title": "9Y Window (Since 2017-01)", "short_label": "2017-01"},
    {"sample_tag": "since_2020_01", "title": "6Y Window (Since 2020-01)", "short_label": "2020-01"},
    {"sample_tag": "since_2023_01", "title": "3Y Window (Since 2023-01)", "short_label": "2023-01"},
    {"sample_tag": "since_2025_01", "title": "1Y Window (Since 2025-01)", "short_label": "2025-01"},
    {"sample_tag": "since_2026_01", "title": "YTD Window (Since 2026-01)", "short_label": "2026-01"},
]

TRACK_WEIGHTS = {
    "since_2017_only": {"since_2017_01": 1.00},
    "since_2023_only": {"since_2023_01": 1.00},
    "since_2020_only": {"since_2020_01": 1.00},
    "since_2025_only": {"since_2025_01": 1.00},
}

SAMPLE_STARTS = {
    "since_2017_01": pd.Timestamp("2017-01-01"),
    "since_2020_01": pd.Timestamp("2020-01-01"),
    "since_2023_01": pd.Timestamp("2023-01-01"),
    "since_2025_01": pd.Timestamp("2025-01-01"),
    "since_2026_01": pd.Timestamp("2026-01-01"),
}

STATIC_STRATEGIES = [
    {
        "base_id": "sse_benchmark",
        "label": "SSE Composite",
        "color": "#111827",
        "kind": "benchmark",
        "available_sample_tags": {"since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"},
    },
    {
        "base_id": "large_cap_pool",
        "label": "Large Cap Static",
        "color": "#0f766e",
        "kind": "static",
        "available_sample_tags": {"since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"},
    },
    {
        "base_id": "kechuang_xuangu",
        "label": "Kechuang Static",
        "color": "#1d4ed8",
        "kind": "static",
        "available_sample_tags": {"since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"},
    },
]

COMPACT_STRATEGIES = [
    {"base_id": "core_explore_80_20_total_mv_index_core", "label": "80/20 Index Core", "color": "#94a3b8"},
    {"base_id": "core_explore_80_20_total_mv_winner_core", "label": "80/20 Winner Core", "color": "#2563eb"},
    {
        "base_id": "core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp",
        "label": "80/20 Winner Core (Aggressive)",
        "color": "#dc2626",
    },
]

STRATEGY_LABEL_BY_ID = {item["base_id"]: item["label"] for item in STATIC_STRATEGIES + COMPACT_STRATEGIES}


def _collect_winner_ids_from_payload(payload: dict) -> set[str]:
    winner_ids: set[str] = set()

    def add_tracks(section: object) -> None:
        if not isinstance(section, dict):
            return
        tracks = section.get("tracks")
        if not isinstance(tracks, dict):
            return
        for meta in tracks.values():
            if not isinstance(meta, dict):
                continue
            strategy_id = meta.get("winner") or meta.get("strategy_base_id")
            if strategy_id:
                winner_ids.add(str(strategy_id))

    add_tracks(payload)
    for path_key in ("path2", "path3"):
        path_payload = payload.get(path_key)
        add_tracks(path_payload)
        if isinstance(path_payload, dict) and path_payload.get("strategy_base_id"):
            winner_ids.add(str(path_payload["strategy_base_id"]))
    return winner_ids


def load_core_active_dynamic_family_ids() -> set[str]:
    if CORE_ACTIVE_REGISTRY_JSON.exists():
        try:
            payload = json.loads(CORE_ACTIVE_REGISTRY_JSON.read_text(encoding="utf-8"))
            strategies = payload.get("strategies") if isinstance(payload, dict) else []
            if isinstance(strategies, list):
                return {
                    str(item["strategy_id"])
                    for item in strategies
                    if isinstance(item, dict) and item.get("strategy_id") and item.get("active", True)
                }
        except Exception:
            pass
    if WEIGHTED_WINNERS_JSON.exists():
        try:
            payload = json.loads(WEIGHTED_WINNERS_JSON.read_text(encoding="utf-8"))
            return _collect_winner_ids_from_payload(payload if isinstance(payload, dict) else {})
        except Exception:
            pass
    return set()


CORE_ACTIVE_DYNAMIC_FAMILY_IDS = load_core_active_dynamic_family_ids()


def _fmt_pct(value: float, digits: int = 2) -> str:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "n/a"
    return f"{value * 100:.{digits}f}%"


def load_weighted_winners() -> dict:
    if WEIGHTED_WINNERS_JSON.exists():
        with WEIGHTED_WINNERS_JSON.open("r", encoding="utf-8") as f:
            return json.load(f)

    if not COMPARISON_CSV.exists():
        return {}

    frame = pd.read_csv(COMPARISON_CSV)
    frame["sample_end"] = pd.to_datetime(frame["sample_end"], errors="coerce")
    frame = frame.dropna(subset=["sample_end"])
    frame = frame.sort_values(["strategy_base_id", "sample_tag", "sample_end"])
    latest = frame.groupby(["strategy_base_id", "sample_tag"], as_index=False).tail(1)

    required_tags = {"since_2017_01", "since_2020_01", "since_2023_01"}

    def weighted(group: pd.DataFrame, weights: dict[str, float], column: str) -> float:
        total = 0.0
        for tag, w in weights.items():
            s = group.loc[group["sample_tag"] == tag, column]
            if s.empty:
                return float("nan")
            total += w * float(s.iloc[0])
        return float(total)

    def pick(weights: dict[str, float]) -> tuple[str, dict] | None:
        candidates: list[tuple[str, float, float, float, float]] = []
        for base_id, group in latest.groupby("strategy_base_id"):
            tags = set(group["sample_tag"].astype(str))
            if not required_tags.issubset(tags):
                continue
            cagr = weighted(group, weights, "cagr")
            sharpe = weighted(group, weights, "sharpe_ratio")
            maxdd = weighted(group, weights, "max_drawdown")
            turnover = weighted(group, weights, "average_annual_turnover")
            if any(np.isnan(v) for v in (cagr, sharpe, maxdd, turnover)):
                continue
            candidates.append((str(base_id), cagr, sharpe, maxdd, turnover))
        if not candidates:
            return None
        candidates.sort(key=lambda r: (r[1], r[2], r[3], -r[4]), reverse=True)
        base_id, cagr, sharpe, maxdd, turnover = candidates[0]
        return base_id, {
            "weighted_cagr": cagr,
            "weighted_sharpe": sharpe,
            "weighted_max_drawdown": maxdd,
            "weighted_turnover": turnover,
        }

    window_2017 = pick(TRACK_WEIGHTS["since_2017_only"])
    window_2023 = pick(TRACK_WEIGHTS["since_2023_only"])
    window_2020 = pick(TRACK_WEIGHTS["since_2020_only"])
    window_2025 = pick(TRACK_WEIGHTS["since_2025_only"])
    if not window_2017 or not window_2023 or not window_2020 or not window_2025:
        return {}
    return {
        "as_of": str(latest["sample_end"].max().date()),
        "tracks": {
            "since_2017_only": {"weights": TRACK_WEIGHTS["since_2017_only"], "winner": window_2017[0], "metrics": window_2017[1]},
            "since_2023_only": {"weights": TRACK_WEIGHTS["since_2023_only"], "winner": window_2023[0], "metrics": window_2023[1]},
            "since_2020_only": {"weights": TRACK_WEIGHTS["since_2020_only"], "winner": window_2020[0], "metrics": window_2020[1]},
            "since_2025_only": {"weights": TRACK_WEIGHTS["since_2025_only"], "winner": window_2025[0], "metrics": window_2025[1]},
        },
    }


WEIGHTED_WINNERS = load_weighted_winners()
WINDOW_2017_WINNER_ID = WEIGHTED_WINNERS.get("tracks", {}).get("since_2017_only", {}).get("winner")
WINDOW_2023_WINNER_ID = WEIGHTED_WINNERS.get("tracks", {}).get("since_2023_only", {}).get("winner")
WINDOW_2020_WINNER_ID = WEIGHTED_WINNERS.get("tracks", {}).get("since_2020_only", {}).get("winner")
WINDOW_2025_WINNER_ID = WEIGHTED_WINNERS.get("tracks", {}).get("since_2025_only", {}).get("winner")
PATH2_WINDOW_2017_WINNER_ID = WEIGHTED_WINNERS.get("path2", {}).get("tracks", {}).get("since_2017_only", {}).get("winner")
PATH2_WINDOW_2023_WINNER_ID = WEIGHTED_WINNERS.get("path2", {}).get("tracks", {}).get("since_2023_only", {}).get("winner")
PATH2_WINDOW_2020_WINNER_ID = WEIGHTED_WINNERS.get("path2", {}).get("tracks", {}).get("since_2020_only", {}).get("winner")
PATH2_WINDOW_2025_WINNER_ID = WEIGHTED_WINNERS.get("path2", {}).get("tracks", {}).get("since_2025_only", {}).get("winner")
PATH2_CANDIDATE_ID = WEIGHTED_WINNERS.get("path2", {}).get("strategy_base_id")

PATH2_WINDOW_WINNER_IDS = {
    base_id
    for base_id in [
        PATH2_WINDOW_2017_WINNER_ID,
        PATH2_WINDOW_2023_WINNER_ID,
        PATH2_WINDOW_2020_WINNER_ID,
        PATH2_WINDOW_2025_WINNER_ID,
    ]
    if base_id
}


def load_base_name_map() -> dict[str, str]:
    if not COMPARISON_CSV.exists():
        return {}
    frame = pd.read_csv(COMPARISON_CSV)
    if frame.empty:
        return {}
    latest = (
        frame.assign(sample_end=pd.to_datetime(frame["sample_end"], errors="coerce"))
        .dropna(subset=["sample_end"])
        .sort_values(["strategy_base_id", "sample_end"])
        .groupby(["strategy_base_id"], as_index=False)
        .tail(1)
    )
    return (
        latest.set_index("strategy_base_id")["strategy_base_name"]
        .fillna("")
        .astype(str)
        .to_dict()
    )


BASE_NAME_MAP = load_base_name_map()


def strategy_label(base_id: str) -> str:
    return STRATEGY_LABEL_BY_ID.get(base_id) or BASE_NAME_MAP.get(base_id) or base_id


def is_2017_winner(base_id: str) -> bool:
    return bool(WINDOW_2017_WINNER_ID) and base_id == WINDOW_2017_WINNER_ID and base_id != WINDOW_2023_WINNER_ID


def is_2023_winner(base_id: str) -> bool:
    return bool(WINDOW_2023_WINNER_ID) and base_id == WINDOW_2023_WINNER_ID and base_id != WINDOW_2017_WINNER_ID


def is_2017_2023_winner(base_id: str) -> bool:
    return bool(base_id) and base_id == WINDOW_2017_WINNER_ID and base_id == WINDOW_2023_WINNER_ID


def is_2020_winner(base_id: str) -> bool:
    return bool(WINDOW_2020_WINNER_ID) and base_id == WINDOW_2020_WINNER_ID


def is_2025_winner(base_id: str) -> bool:
    return bool(WINDOW_2025_WINNER_ID) and base_id == WINDOW_2025_WINNER_ID


def is_path2_candidate(base_id: str) -> bool:
    return bool(PATH2_CANDIDATE_ID) and base_id == PATH2_CANDIDATE_ID


def is_path2_window_winner(base_id: str) -> bool:
    return bool(base_id) and base_id in PATH2_WINDOW_WINNER_IDS and base_id != PATH2_CANDIDATE_ID


def winner_tags(base_id: str) -> set[str]:
    tags: set[str] = set()
    if base_id == WINDOW_2017_WINNER_ID:
        tags.add("2017")
    if base_id == WINDOW_2023_WINNER_ID:
        tags.add("2023")
    if base_id == WINDOW_2020_WINNER_ID:
        tags.add("2020")
    if base_id == WINDOW_2025_WINNER_ID:
        tags.add("2025")
    if is_path2_window_winner(base_id):
        tags.add("path2_window")
    if base_id == PATH2_CANDIDATE_ID:
        tags.add("path2")
    return tags


def load_tracked_comparison_strategies() -> list[dict]:
    # Keep this list compact and readable: a few baselines + tracked winners + Path 2.
    base_ids: list[str] = [
        "core_explore_80_20_total_mv_index_core",
        "core_explore_80_20_total_mv_winner_core",
        "core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp",
    ]

    track_winners = [
        WINDOW_2017_WINNER_ID,
        WINDOW_2023_WINNER_ID,
        WINDOW_2020_WINNER_ID,
        WINDOW_2025_WINNER_ID,
        PATH2_WINDOW_2017_WINNER_ID,
        PATH2_WINDOW_2023_WINNER_ID,
        PATH2_WINDOW_2020_WINNER_ID,
        PATH2_WINDOW_2025_WINNER_ID,
        PATH2_CANDIDATE_ID,
    ]
    for winner_id in track_winners:
        if winner_id:
            base_ids.append(str(winner_id))

    seen: set[str] = set()
    deduped: list[str] = []
    for base_id in base_ids:
        if base_id in seen:
            continue
        seen.add(base_id)
        deduped.append(base_id)

    color_by_id = {
        "core_explore_80_20_total_mv_index_core": "#94a3b8",
        "core_explore_80_20_total_mv_winner_core": "#2563eb",
        "core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp": "#dc2626",
    }
    for base_id in deduped:
        if is_path2_candidate(base_id):
            color_by_id.setdefault(base_id, "#7c3aed")
        elif is_path2_window_winner(base_id):
            color_by_id.setdefault(base_id, "#a855f7")
        elif is_2025_winner(base_id):
            color_by_id.setdefault(base_id, "#16a34a")
        elif is_2020_winner(base_id):
            color_by_id.setdefault(base_id, "#f59e0b")
        elif is_2017_2023_winner(base_id) or is_2023_winner(base_id):
            color_by_id.setdefault(base_id, "#2563eb")
        elif is_2017_winner(base_id):
            color_by_id.setdefault(base_id, "#60a5fa")

    cmap = plt.get_cmap("tab20")
    dynamic: list[dict] = []
    for idx, base_id in enumerate(deduped):
        label = strategy_label(base_id)
        if is_path2_window_winner(base_id):
            label = f"Path 2: {label}"
        elif is_path2_candidate(base_id):
            label = f"Path 2 robust: {label}"
        dynamic.append(
            {
                "base_id": base_id,
                "label": label,
                "color": color_by_id.get(base_id, mcolors.to_hex(cmap(idx % 20))),
            }
        )
        STRATEGY_LABEL_BY_ID.setdefault(base_id, strategy_label(base_id))

    return list(STATIC_STRATEGIES) + dynamic


def _maybe_add_tracked_winners() -> None:
    existing = {item["base_id"] for item in COMPACT_STRATEGIES}
    winners = [
        ("2017", WINDOW_2017_WINNER_ID, "#60a5fa"),
        ("2023", WINDOW_2023_WINNER_ID, "#2563eb"),
        ("2020", WINDOW_2020_WINNER_ID, "#f59e0b"),
        ("2025", WINDOW_2025_WINNER_ID, "#10b981"),
    ]
    strategy_meta = WEIGHTED_WINNERS.get("strategies", {}) if isinstance(WEIGHTED_WINNERS, dict) else {}
    for _, base_id, color in winners:
        if not base_id or base_id in existing:
            continue
        strategy_name = ""
        if isinstance(strategy_meta, dict):
            strategy_name = str(strategy_meta.get(base_id, {}).get("strategy_base_name") or "")
        COMPACT_STRATEGIES.append(
            {
                "base_id": base_id,
                "label": strategy_name or base_id,
                "color": color,
            }
        )
        existing.add(base_id)
        STRATEGY_LABEL_BY_ID[base_id] = strategy_name or base_id


_maybe_add_tracked_winners()

def load_summary(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def build_result_path(base_id: str, sample_tag: str, filename: str) -> Path:
    return existing_strategy_result_file(base_id, sample_tag, filename, market_scope="a_share")


def compute_window_metrics(equity: pd.DataFrame, monthly_returns: pd.DataFrame, turnover: pd.DataFrame) -> dict:
    nav = equity["nav"].astype(float)
    monthly_net = monthly_returns["net_return"].astype(float)
    total_return = float(nav.iloc[-1] - 1.0)
    periods = len(monthly_net)
    years = periods / 12.0 if periods > 0 else np.nan
    cagr = float(nav.iloc[-1] ** (1 / years) - 1) if periods > 0 and nav.iloc[-1] > 0 else np.nan
    max_drawdown = float(equity["drawdown"].min())
    annual_volatility = float(monthly_net.std(ddof=1) * np.sqrt(12)) if periods > 1 else np.nan
    sharpe_ratio = (
        float((monthly_net.mean() / monthly_net.std(ddof=1)) * np.sqrt(12))
        if periods > 1 and monthly_net.std(ddof=1) > 0
        else np.nan
    )
    return {
        "total_return": total_return,
        "cagr": cagr,
        "max_drawdown": max_drawdown,
        "annual_volatility": annual_volatility,
        "sharpe_ratio": sharpe_ratio,
        "average_annual_turnover": float(turnover["one_way_turnover"].mean() * 12) if not turnover.empty else np.nan,
    }


def slice_equity_window(
    equity: pd.DataFrame,
    monthly_returns: pd.DataFrame,
    turnover: pd.DataFrame,
    sample_start: pd.Timestamp,
) -> tuple[pd.DataFrame, dict]:
    equity_window = equity[equity["date"] >= sample_start].copy()
    if equity_window.empty:
        raise FileNotFoundError(f"No data for window starting {sample_start.date()}")
    start_nav = float(equity_window.iloc[0]["nav"])
    equity_window["nav"] = equity_window["nav"] / start_nav
    equity_window["drawdown"] = equity_window["nav"] / equity_window["nav"].cummax() - 1.0
    monthly_window = monthly_returns[monthly_returns["date"] >= sample_start].copy()
    turnover_window = turnover[turnover["date"] >= sample_start].copy()
    return equity_window, compute_window_metrics(equity_window, monthly_window, turnover_window)


def load_benchmark_window(sample_tag: str) -> tuple[pd.DataFrame, dict]:
    cache_path = ROOT / "data_cache" / "index_daily" / "000001.SH.csv"
    if not cache_path.exists():
        raise FileNotFoundError("SSE benchmark cache missing: 000001.SH.csv")
    sample_start = SAMPLE_STARTS[sample_tag]
    benchmark = pd.read_csv(cache_path, parse_dates=["trade_date"]).sort_values("trade_date")
    benchmark = benchmark[benchmark["trade_date"] >= sample_start].copy()
    if benchmark.empty:
        raise FileNotFoundError(f"SSE benchmark unavailable for {sample_tag}")
    benchmark["nav"] = benchmark["close"].astype(float) / float(benchmark["close"].iloc[0])
    benchmark["drawdown"] = benchmark["nav"] / benchmark["nav"].cummax() - 1.0
    equity = benchmark.rename(columns={"trade_date": "date"})[["date", "nav", "drawdown"]].copy()
    monthly = (
        equity.assign(month=equity["date"].dt.to_period("M"))
        .groupby("month", as_index=False)
        .tail(1)
        .sort_values("date")
    )
    monthly["net_return"] = monthly["nav"].pct_change().fillna(0.0)
    monthly["portfolio_return"] = monthly["net_return"]
    monthly["gross_return"] = monthly["net_return"]
    monthly["trading_cost"] = 0.0
    turnover = pd.DataFrame(columns=["date", "one_way_turnover"])
    return equity, compute_window_metrics(equity, monthly[["date", "net_return", "portfolio_return", "gross_return", "trading_cost"]], turnover)


def load_static_window(base_id: str, sample_tag: str) -> tuple[pd.DataFrame, dict]:
    result_dir = existing_strategy_result_dir(base_id, market_scope="a_share")
    summary_path = result_dir / "summary.json"
    equity_path = result_dir / "equity_curve.csv"
    monthly_path = result_dir / "monthly_returns.csv"
    turnover_path = result_dir / "turnover.csv"

    summary = load_summary(summary_path)
    equity = pd.read_csv(equity_path, parse_dates=["date"])
    monthly_returns = pd.read_csv(monthly_path, parse_dates=["date"])
    turnover = pd.read_csv(turnover_path, parse_dates=["date"])

    if sample_tag == "since_2020_01":
        return equity, summary["metrics"]

    if sample_tag not in {"since_2023_01", "since_2025_01", "since_2026_01"}:
        raise FileNotFoundError(f"Static strategy {base_id} does not support {sample_tag}")
    return slice_equity_window(equity, monthly_returns, turnover, SAMPLE_STARTS[sample_tag])


def load_strategy_window(config: dict, sample_tag: str) -> tuple[pd.DataFrame, dict]:
    if sample_tag not in config.get("available_sample_tags", {sample_tag}):
        raise FileNotFoundError(f"{config['label']} unavailable for {sample_tag}")
    if config.get("kind") == "benchmark":
        return load_benchmark_window(sample_tag)
    if config.get("kind") == "static":
        return load_static_window(config["base_id"], sample_tag)

    target_dir = build_result_path(config["base_id"], sample_tag, "summary.json")
    if target_dir.exists():
        summary = load_summary(target_dir)
        equity = pd.read_csv(build_result_path(config["base_id"], sample_tag, "equity_curve.csv"), parse_dates=["date"])
        return equity, summary["metrics"]

    if sample_tag not in {"since_2025_01", "since_2026_01"}:
        raise FileNotFoundError(f"{config['label']} missing {sample_tag}")

    for fallback_tag in ("since_2025_01", "since_2020_01", "since_2017_01", "since_2023_01"):
        summary_path = build_result_path(config["base_id"], fallback_tag, "summary.json")
        equity_path = build_result_path(config["base_id"], fallback_tag, "equity_curve.csv")
        monthly_path = build_result_path(config["base_id"], fallback_tag, "monthly_returns.csv")
        turnover_path = build_result_path(config["base_id"], fallback_tag, "turnover.csv")
        if not (summary_path.exists() and equity_path.exists() and monthly_path.exists() and turnover_path.exists()):
            continue
        equity = pd.read_csv(equity_path, parse_dates=["date"])
        monthly_returns = pd.read_csv(monthly_path, parse_dates=["date"])
        turnover = pd.read_csv(turnover_path, parse_dates=["date"])
        return slice_equity_window(equity, monthly_returns, turnover, SAMPLE_STARTS[sample_tag])
    raise FileNotFoundError(f"{config['label']} missing {sample_tag}")


def load_active_family_strategies() -> list[dict]:
    strategies = list(STATIC_STRATEGIES)
    if not COMPARISON_CSV.exists():
        return strategies + list(COMPACT_STRATEGIES)

    frame = pd.read_csv(COMPARISON_CSV)
    if frame.empty:
        return strategies + list(COMPACT_STRATEGIES)

    latest = (
        frame.assign(sample_end=pd.to_datetime(frame["sample_end"], errors="coerce"))
        .dropna(subset=["sample_end"])
        .sort_values(["strategy_base_id", "sample_tag", "sample_end"])
        .groupby(["strategy_base_id", "sample_tag"], as_index=False)
        .tail(1)
    )
    grouped = (
        latest.sort_values(["strategy_base_name", "strategy_base_id"])
        .drop_duplicates(subset=["strategy_base_id"])
        [["strategy_base_id", "strategy_base_name"]]
    )
    dynamic_ids = [str(item) for item in grouped["strategy_base_id"].tolist()]
    cmap = plt.get_cmap("tab20")
    dynamic_strategies: list[dict] = []
    tracked_winner_ids = {
        base_id
        for base_id in [WINDOW_2017_WINNER_ID, WINDOW_2023_WINNER_ID, WINDOW_2020_WINNER_ID, WINDOW_2025_WINNER_ID]
        if base_id
    }
    for idx, row in enumerate(grouped.itertuples(index=False)):
        base_id = str(row.strategy_base_id)
        if base_id not in CORE_ACTIVE_DYNAMIC_FAMILY_IDS and base_id not in tracked_winner_ids:
            continue
        label = str(row.strategy_base_name) if pd.notna(row.strategy_base_name) and str(row.strategy_base_name).strip() else base_id
        color = mcolors.to_hex(cmap(idx % 20))
        dynamic_strategies.append({"base_id": base_id, "label": label, "color": color})
        STRATEGY_LABEL_BY_ID.setdefault(base_id, label)

    priority_ids = [
        base_id
        for base_id in [WINDOW_2017_WINNER_ID, WINDOW_2023_WINNER_ID, WINDOW_2020_WINNER_ID, WINDOW_2025_WINNER_ID]
        if base_id in dynamic_ids
    ]
    priority_set = set(priority_ids)
    prioritized = [item for item in dynamic_strategies if item["base_id"] in priority_set]
    remaining = [item for item in dynamic_strategies if item["base_id"] not in priority_set]
    return strategies + prioritized + remaining


def build_comparison_frame(sample_tag: str, strategies: list[dict]) -> pd.DataFrame:
    rows: list[dict] = []
    for config in strategies:
        try:
            _, metrics = load_strategy_window(config, sample_tag)
        except FileNotFoundError:
            continue
        rows.append(
            {
                "base_id": config["base_id"],
                "label": config["label"],
                "color": config["color"],
                "total_return": metrics["total_return"],
                "cagr": metrics["cagr"],
                "max_drawdown": metrics["max_drawdown"],
                "sharpe_ratio": metrics["sharpe_ratio"],
            }
        )
    return pd.DataFrame(rows)


def plot_nav_curves(ax: plt.Axes, sample_tag: str, title: str, strategies: list[dict]) -> None:
    for config in strategies:
        try:
            equity, _ = load_strategy_window(config, sample_tag)
        except FileNotFoundError:
            continue
        base_id = config["base_id"]
        tags = winner_tags(base_id)
        highlight = bool(tags)
        if "2020" in tags and ("2017" in tags or "2023" in tags):
            linestyle = "-."
        elif "2025" in tags and ("2017" in tags or "2023" in tags or "2020" in tags):
            linestyle = (0, (5, 2, 1, 2))
        elif "path2" in tags:
            linestyle = (0, (2, 2))
        elif "2023" in tags or is_2017_2023_winner(base_id):
            linestyle = "-"
        elif "2017" in tags:
            linestyle = "--"
        elif "2020" in tags:
            linestyle = ":"
        elif "2025" in tags:
            linestyle = (0, (3, 2))
        else:
            linestyle = "-"
        ax.plot(
            equity["date"],
            equity["nav"],
            label=config["label"],
            color=config["color"],
            linewidth=2.8 if highlight else 1.4,
            alpha=1.0 if highlight else 0.9,
            linestyle=linestyle,
        )

    ax.set_title("NAV Curves", fontsize=13, fontweight="bold", pad=10)
    ax.set_ylabel("NAV")
    ax.grid(alpha=0.25)


def plot_risk_return(ax: plt.Axes, frame: pd.DataFrame, title: str) -> None:
    for _, row in frame.iterrows():
        base_id = row.get("base_id", "")
        tags = winner_tags(str(base_id))
        highlight = bool(tags)
        marker = "o"
        if len(tags) > 1:
            marker = "X"
        elif "path2" in tags:
            marker = "H"
        elif "2023" in tags:
            marker = "*"
        elif "2017" in tags:
            marker = "D"
        elif "2020" in tags:
            marker = "^"
        elif "2025" in tags:
            marker = "P"
        ax.scatter(
            row["cagr"] * 100,
            row["max_drawdown"] * 100,
            s=260 if highlight else 140,
            color=row["color"],
            alpha=0.95,
            edgecolors="white",
            linewidths=1.2,
            marker=marker,
        )
        ax.annotate(
            row["label"],
            (row["cagr"] * 100, row["max_drawdown"] * 100),
            xytext=(8, 6),
            textcoords="offset points",
            fontsize=8.5,
        )

    ax.axvline(0, color="#cbd5e1", linewidth=1)
    ax.set_title(f"{title} Risk / Return", fontsize=12, fontweight="bold")
    ax.set_xlabel("CAGR (%)")
    ax.set_ylabel("Max DD (%)")
    ax.grid(alpha=0.25)


def plot_metric_table(ax: plt.Axes, frame: pd.DataFrame, title: str) -> None:
    table_frame = frame.copy()
    table_frame["total_return"] = (table_frame["total_return"] * 100).map(lambda x: f"{x:.1f}%")
    table_frame["cagr"] = (table_frame["cagr"] * 100).map(lambda x: f"{x:.2f}%")
    table_frame["max_drawdown"] = (table_frame["max_drawdown"] * 100).map(lambda x: f"{x:.2f}%")
    table_frame["sharpe_ratio"] = table_frame["sharpe_ratio"].map(lambda x: f"{x:.3f}")
    base_ids = table_frame["base_id"].astype(str).tolist()
    display_frame = table_frame[["label", "total_return", "cagr", "max_drawdown", "sharpe_ratio"]]
    display_frame.columns = ["Strategy", "Total Return", "CAGR", "Max DD", "Sharpe"]

    ax.axis("off")
    ax.set_title(f"{title} Metrics", fontsize=12, fontweight="bold", pad=8)
    table = ax.table(
        cellText=display_frame.values,
        colLabels=display_frame.columns,
        cellLoc="center",
        colLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.35)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#cbd5e1")
        if row == 0:
            cell.set_facecolor("#e2e8f0")
            cell.set_text_props(weight="bold")
        else:
            base_id = base_ids[row - 1] if 0 <= row - 1 < len(base_ids) else ""
            tags = winner_tags(base_id)
            if len(tags) > 1:
                cell.set_facecolor("#e9d5ff")
            elif "path2" in tags:
                cell.set_facecolor("#f3e8ff")
            elif "2023" in tags:
                cell.set_facecolor("#fee2e2")
            elif "2017" in tags:
                cell.set_facecolor("#dbeafe")
            elif "2020" in tags:
                cell.set_facecolor("#fef3c7")
            elif "2025" in tags:
                cell.set_facecolor("#dcfce7")


def build_winner_note() -> str | None:
    if not (WEIGHTED_WINNERS and WINDOW_2017_WINNER_ID and WINDOW_2023_WINNER_ID and WINDOW_2020_WINNER_ID):
        return None
    window_2017_metrics = WEIGHTED_WINNERS["tracks"]["since_2017_only"]["metrics"]
    window_2023_metrics = WEIGHTED_WINNERS["tracks"]["since_2023_only"]["metrics"]
    window_2020_metrics = WEIGHTED_WINNERS["tracks"]["since_2020_only"]["metrics"]
    window_2025_metrics = WEIGHTED_WINNERS["tracks"]["since_2025_only"]["metrics"]
    path2_window_2017_metrics = WEIGHTED_WINNERS.get("path2", {}).get("tracks", {}).get("since_2017_only", {}).get("metrics", {})
    path2_window_2023_metrics = WEIGHTED_WINNERS.get("path2", {}).get("tracks", {}).get("since_2023_only", {}).get("metrics", {})
    path2_window_2020_metrics = WEIGHTED_WINNERS.get("path2", {}).get("tracks", {}).get("since_2020_only", {}).get("metrics", {})
    path2_window_2025_metrics = WEIGHTED_WINNERS.get("path2", {}).get("tracks", {}).get("since_2025_only", {}).get("metrics", {})
    window_2017_label = STRATEGY_LABEL_BY_ID.get(WINDOW_2017_WINNER_ID, WINDOW_2017_WINNER_ID)
    window_2023_label = STRATEGY_LABEL_BY_ID.get(WINDOW_2023_WINNER_ID, WINDOW_2023_WINNER_ID)
    window_2020_label = STRATEGY_LABEL_BY_ID.get(WINDOW_2020_WINNER_ID, WINDOW_2020_WINNER_ID)
    window_2025_label = STRATEGY_LABEL_BY_ID.get(WINDOW_2025_WINNER_ID, WINDOW_2025_WINNER_ID)
    path2_window_2017_label = STRATEGY_LABEL_BY_ID.get(PATH2_WINDOW_2017_WINNER_ID, PATH2_WINDOW_2017_WINNER_ID)
    path2_window_2023_label = STRATEGY_LABEL_BY_ID.get(PATH2_WINDOW_2023_WINNER_ID, PATH2_WINDOW_2023_WINNER_ID)
    path2_window_2020_label = STRATEGY_LABEL_BY_ID.get(PATH2_WINDOW_2020_WINNER_ID, PATH2_WINDOW_2020_WINNER_ID)
    path2_window_2025_label = STRATEGY_LABEL_BY_ID.get(PATH2_WINDOW_2025_WINNER_ID, PATH2_WINDOW_2025_WINNER_ID)
    path2_label = STRATEGY_LABEL_BY_ID.get(PATH2_CANDIDATE_ID, PATH2_CANDIDATE_ID) if PATH2_CANDIDATE_ID else None
    as_of = WEIGHTED_WINNERS.get("as_of", "n/a")
    note = (
        "Weighted winners (as of {as_of})\n"
        "Path 1 | 2017-window winner: {w17_label} | CAGR {w17cagr}, Sharpe {w17sharpe:.3f}, MaxDD {w17dd}, Turn {w17turn:.2f}\n"
        "Path 1 | 2023-window winner: {w23_label} | CAGR {w23cagr}, Sharpe {w23sharpe:.3f}, MaxDD {w23dd}, Turn {w23turn:.2f}\n"
        "Path 1 | 2020-window winner: {w20_label} | CAGR {w20cagr}, Sharpe {w20sharpe:.3f}, MaxDD {w20dd}, Turn {w20turn:.2f}\n"
        "Path 1 | 2025-window winner: {w25_label} | CAGR {w25cagr}, Sharpe {w25sharpe:.3f}, MaxDD {w25dd}, Turn {w25turn:.2f}\n"
        "Path 2 | 2017-window winner: {p17_label} | CAGR {p17cagr}, Sharpe {p17sharpe:.3f}, MaxDD {p17dd}, Turn {p17turn:.2f}\n"
        "Path 2 | 2023-window winner: {p23_label} | CAGR {p23cagr}, Sharpe {p23sharpe:.3f}, MaxDD {p23dd}, Turn {p23turn:.2f}\n"
        "Path 2 | 2020-window winner: {p20_label} | CAGR {p20cagr}, Sharpe {p20sharpe:.3f}, MaxDD {p20dd}, Turn {p20turn:.2f}\n"
        "Path 2 | 2025-window winner: {p25_label} | CAGR {p25cagr}, Sharpe {p25sharpe:.3f}, MaxDD {p25dd}, Turn {p25turn:.2f}"
    ).format(
        as_of=as_of,
        w17_label=window_2017_label,
        w17cagr=_fmt_pct(window_2017_metrics.get("weighted_cagr")),
        w17sharpe=float(window_2017_metrics.get("weighted_sharpe")),
        w17dd=_fmt_pct(window_2017_metrics.get("weighted_max_drawdown")),
        w17turn=float(window_2017_metrics.get("weighted_turnover")),
        w23_label=window_2023_label,
        w23cagr=_fmt_pct(window_2023_metrics.get("weighted_cagr")),
        w23sharpe=float(window_2023_metrics.get("weighted_sharpe")),
        w23dd=_fmt_pct(window_2023_metrics.get("weighted_max_drawdown")),
        w23turn=float(window_2023_metrics.get("weighted_turnover")),
        w20_label=window_2020_label,
        w20cagr=_fmt_pct(window_2020_metrics.get("weighted_cagr")),
        w20sharpe=float(window_2020_metrics.get("weighted_sharpe")),
        w20dd=_fmt_pct(window_2020_metrics.get("weighted_max_drawdown")),
        w20turn=float(window_2020_metrics.get("weighted_turnover")),
        w25_label=window_2025_label,
        w25cagr=_fmt_pct(window_2025_metrics.get("weighted_cagr")),
        w25sharpe=float(window_2025_metrics.get("weighted_sharpe")),
        w25dd=_fmt_pct(window_2025_metrics.get("weighted_max_drawdown")),
        w25turn=float(window_2025_metrics.get("weighted_turnover")),
        p17_label=path2_window_2017_label,
        p17cagr=_fmt_pct(path2_window_2017_metrics.get("weighted_cagr")),
        p17sharpe=float(path2_window_2017_metrics.get("weighted_sharpe", float("nan"))),
        p17dd=_fmt_pct(path2_window_2017_metrics.get("weighted_max_drawdown")),
        p17turn=float(path2_window_2017_metrics.get("weighted_turnover", float("nan"))),
        p23_label=path2_window_2023_label,
        p23cagr=_fmt_pct(path2_window_2023_metrics.get("weighted_cagr")),
        p23sharpe=float(path2_window_2023_metrics.get("weighted_sharpe", float("nan"))),
        p23dd=_fmt_pct(path2_window_2023_metrics.get("weighted_max_drawdown")),
        p23turn=float(path2_window_2023_metrics.get("weighted_turnover", float("nan"))),
        p20_label=path2_window_2020_label,
        p20cagr=_fmt_pct(path2_window_2020_metrics.get("weighted_cagr")),
        p20sharpe=float(path2_window_2020_metrics.get("weighted_sharpe", float("nan"))),
        p20dd=_fmt_pct(path2_window_2020_metrics.get("weighted_max_drawdown")),
        p20turn=float(path2_window_2020_metrics.get("weighted_turnover", float("nan"))),
        p25_label=path2_window_2025_label,
        p25cagr=_fmt_pct(path2_window_2025_metrics.get("weighted_cagr")),
        p25sharpe=float(path2_window_2025_metrics.get("weighted_sharpe", float("nan"))),
        p25dd=_fmt_pct(path2_window_2025_metrics.get("weighted_max_drawdown")),
        p25turn=float(path2_window_2025_metrics.get("weighted_turnover", float("nan"))),
    )
    if path2_label:
        note += f"\nPath 2 robust candidate: {path2_label}"
    return note


def render_summary_card() -> None:
    note = build_winner_note()
    if not note:
        return
    line_count = note.count("\n") + 1
    fig_height = max(2.8, 0.42 * line_count + 0.8)
    fig, ax = plt.subplots(figsize=(12, fig_height))
    ax.axis("off")
    ax.text(
        0.01,
        0.96,
        note,
        va="top",
        ha="left",
        fontsize=11,
        transform=ax.transAxes,
        bbox={"boxstyle": "round,pad=0.45", "facecolor": "white", "edgecolor": "#cbd5e1", "alpha": 0.96},
    )
    fig.tight_layout()
    fig.savefig(SUMMARY_OUTPUT_PATH, dpi=180, bbox_inches="tight")
    plt.close(fig)


def render_window_chart(
    sample_window: dict,
    strategies: list[dict],
    output_path: Path,
    *,
    family_mode: bool = False,
) -> None:
    frame = build_comparison_frame(sample_window["sample_tag"], strategies)
    fig, axes = plt.subplots(
        3 if not family_mode else 2,
        1,
        figsize=(12, 12 if not family_mode else 9.5),
        constrained_layout=False,
        gridspec_kw={"height_ratios": [2.2, 1.5, 1.7] if not family_mode else [2.5, 1.8]},
    )
    plot_nav_curves(axes[0], sample_window["sample_tag"], sample_window["title"], strategies)
    plot_risk_return(axes[1], frame, sample_window["short_label"])
    if not family_mode:
        plot_metric_table(axes[2], frame, sample_window["short_label"])

    handles, labels = axes[0].get_legend_handles_labels()
    legend_cols = 3 if not family_mode else 4
    title_prefix = "aiinvestor Strategy Comparison" if not family_mode else "aiinvestor Core Active Strategy Family"
    fig.suptitle(f"{title_prefix}: {sample_window['title']}", fontsize=18, fontweight="bold", y=0.985)
    fig.legend(handles, labels, loc="upper center", ncol=legend_cols, frameon=False, bbox_to_anchor=(0.5, 0.955))
    fig.tight_layout(rect=(0.03, 0.03, 0.97, 0.88 if not family_mode else 0.89))
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    _configure_matplotlib_fonts()
    render_summary_card()
    comparison_strategies = load_tracked_comparison_strategies()
    active_family_strategies = load_active_family_strategies()
    for sample_window in SAMPLE_WINDOWS:
        sample_tag = sample_window["sample_tag"]
        render_window_chart(sample_window, comparison_strategies, OUTPUT_PATHS[sample_tag], family_mode=False)
        if sample_tag in FAMILY_OUTPUT_PATHS:
            render_window_chart(sample_window, active_family_strategies, FAMILY_OUTPUT_PATHS[sample_tag], family_mode=True)


if __name__ == "__main__":
    main()
