from __future__ import annotations

import csv
import html
import json
import mimetypes
import os
import sqlite3
from datetime import datetime, timedelta
from functools import lru_cache
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, urlparse
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
RESULTS_DIR = ROOT / "results"
HK_RESULTS_DIR = ROOT / "results_hkconnect"
LIVE_DIR = RESULTS_DIR / "live"
DB_PATH = ROOT / "data" / "live_platform.db"
STOCK_BASIC_PATH = ROOT / "data_cache" / "stock_basic.csv"
DAILY_CACHE_DIR = ROOT / "data_cache" / "daily"

DEFAULT_ACCOUNT_NAME = "模拟账户A"
DEFAULT_ACCOUNT_BROKER = "手工测试"
DEFAULT_CAPITAL = 1_000_000.0
DEFAULT_TRACKED_WINNER_KEY = "since_2020_only"

def _load_tushare_tokens() -> tuple[str, str]:
    daily  = os.environ.get("TUSHARE_TOKEN_DAILY",  "")
    minute = os.environ.get("TUSHARE_TOKEN_MINUTE", "")
    if not daily or not minute:
        try:
            import importlib
            import config as _cfg
            importlib.reload(_cfg)
            daily  = daily  or getattr(_cfg, "TUSHARE_TOKEN_DAILY",  "") or ""
            minute = minute or getattr(_cfg, "TUSHARE_TOKEN_MINUTE", "") or ""
        except Exception:
            pass
    return daily, minute

TUSHARE_DAILY_TOKEN, TUSHARE_MINUTE_TOKEN = _load_tushare_tokens()

BUY_COMMISSION = 0.0003
SELL_COMMISSION = 0.0003
SELL_STAMP_DUTY = 0.0005
CHINA_TZ = ZoneInfo("Asia/Shanghai")


def now_str() -> str:
    return datetime.now(CHINA_TZ).strftime("%Y-%m-%d %H:%M:%S")


def shanghai_now() -> datetime:
    return datetime.now(CHINA_TZ)


def is_cn_market_open(now_dt: datetime | None = None) -> bool:
    now_dt = now_dt or shanghai_now()
    if now_dt.weekday() >= 5:
        return False
    current = now_dt.time()
    return (current >= datetime.strptime("09:30", "%H:%M").time() and current < datetime.strptime("11:30", "%H:%M").time()) or (
        current >= datetime.strptime("13:00", "%H:%M").time() and current < datetime.strptime("15:00", "%H:%M").time()
    )


def _today_trade_tag(now_dt: datetime | None = None) -> str:
    now_dt = now_dt or shanghai_now()
    return now_dt.strftime("%Y%m%d")


def _price_cache_bucket(now_dt: datetime | None = None) -> tuple[str, bool]:
    now_dt = now_dt or shanghai_now()
    if is_cn_market_open(now_dt):
        return now_dt.strftime("%Y%m%d%H%M"), True
    return now_dt.strftime("%Y%m%d"), False


def describe_price_source(source: str) -> str:
    mapping = {
        "tushare_minute_live": "实时价（分钟线，盘中每分钟刷新）",
        "tushare_daily_prev_close": "昨收价（日线，非交易时段展示）",
        "daily_cache_prev_close": "昨收价（本地缓存，非交易时段展示）",
        "tushare_daily_latest": "最近收盘价（日线）",
        "daily_cache_latest": "最近收盘价（本地缓存）",
        "minute_failed": "实时价获取失败，已回退",
        "daily_failed": "收盘价获取失败，已回退",
        "missing": "暂无价格数据",
        "unknown": "价格来源未知",
    }
    return mapping.get(source, source)


def market_scope_label(scope: str) -> str:
    mapping = {
        "a_share": "A股",
        "hkconnect": "沪港通",
    }
    return mapping.get(scope, scope)


def rebalance_frequency_label(freq: str) -> str:
    mapping = {
        "monthly": "月度",
        "biweekly": "双周",
        "weekly": "单周",
    }
    return mapping.get(str(freq or "monthly"), str(freq or "monthly"))


def adjustment_style_label(item: dict) -> str:
    return str(item.get("adjustment_style") or "月度换股")


def schedule_kind_label(schedule_kind: str) -> str:
    mapping = {
        "monthly": "纯月度",
        "portfolio_weekly_overlay": "月度换股 + 周度总仓位",
        "satellite_weekly_overlay": "月度换股 + 周度卫星仓位",
        "biweekly": "双周换股",
        "weekly": "单周换股",
    }
    return mapping.get(str(schedule_kind or ""), "未识别")


def strategy_detail_explanation_html(item: dict, active_view: dict, schedule_kind: str, active_sample_label: str) -> str:
    strategy_id = str(item.get("strategy_id") or "")
    display_name = str(item.get("display_name") or strategy_id)
    market_scope = str(item.get("market_scope") or "a_share")
    path_name = str(item.get("path") or "")
    winner_type = str(item.get("winner_type") or "")
    adjustment_style = adjustment_style_label(item)
    windows_label = winner_windows_label(item.get("winner_tags") or [])
    identity_label = winner_identity_label(item.get("winner_tags") or [])
    metrics = active_view.get("summary_metrics") or {}

    role_bits = [
        market_scope_label(market_scope),
        path_name.upper() if path_name else "",
        identity_label or winner_type,
        f"胜出窗口：{windows_label}" if windows_label else "",
    ]
    role_text = " / ".join(bit for bit in role_bits if bit)

    universe = "沪港通标的池" if market_scope == "hkconnect" else "A股全市场研究池"
    if "total_mv" in strategy_id:
        core_source = "核心底座偏向总市值/大市值胜出者核心。"
    elif "equal_weight" in strategy_id:
        core_source = "核心底座采用等权胜出者核心，更强调弹性与分散。"
    elif "index_core" in strategy_id:
        core_source = "核心底座采用指数核心，更偏防守与市场代表性。"
    elif market_scope == "hkconnect":
        core_source = "策略仅在沪港通可交易标的内做优胜劣汰。"
    else:
        core_source = "核心底座采用当前策略族定义的胜出者核心。"

    selection_lines: list[str] = []
    if path_name == "path1":
        selection_lines.append("Path 1 是主攻稳健线：优先在回撤、换手、Sharpe 和实盘可执行性之间做平衡。")
    elif path_name == "path2":
        selection_lines.append("Path 2 是高收益探索线：更重视 CAGR 上限突破，同时继续监控回撤和换手。")
    elif path_name == "path3":
        selection_lines.append("Path 3 是周度高频线：专门跟踪纯周度换股候选，和月度选股叠加周度仓位风控分开评估。")
    if "aggr_10_90" in strategy_id:
        selection_lines.append("进攻仓位配置约为 10/90，探索侧更积极。")
    elif "aggr_08_92" in strategy_id:
        selection_lines.append("进攻仓位配置约为 8/92，在进攻与风控之间相对折中。")
    elif "aggr_05_95" in strategy_id:
        selection_lines.append("进攻仓位配置约为 5/95，属于更集中、更高弹性的探索结构。")
    elif "aggr_03_97" in strategy_id:
        selection_lines.append("进攻仓位配置约为 3/97，属于高度集中、高弹性的探索结构。")
    if "prom6" in strategy_id:
        selection_lines.append("晋升池规模为 6 只，个股分散度高于 prom2/prom3 版本。")
    elif "prom3" in strategy_id:
        selection_lines.append("晋升池规模为 3 只，收益弹性更集中。")
    elif "prom2" in strategy_id:
        selection_lines.append("晋升池规模为 2 只，属于高集中度候选。")
    if "core_6_1" in strategy_id:
        selection_lines.append("包含核心 6-1 动量过滤，偏向保留中期趋势更强的标的。")
    if "theme" in strategy_id:
        selection_lines.append("沪港通高成长主线候选，偏向成长/主题强势标的。")
    if "breakout" in strategy_id:
        selection_lines.append("沪港通高集中突破候选，偏向强势突破与高弹性标的。")
    if "equal_elastic" in strategy_id:
        selection_lines.append("沪港通等权高弹性候选，强调弹性分散和等权暴露。")
    if not selection_lines:
        selection_lines.append("策略按当前研究配置从候选池中选择相对胜出的股票组合。")

    risk_lines: list[str] = []
    if "cash_off" in strategy_id:
        risk_lines.append("包含熊市空仓/降风险逻辑，风险关闭时可以显著降低总仓位。")
    if "risk30" in strategy_id:
        risk_lines.append("熊市风险状态下目标仓位可降至约 30%。")
    elif "risk50" in strategy_id:
        risk_lines.append("熊市风险状态下目标仓位可降至约 50%。")
    if "full_risk" in strategy_id:
        risk_lines.append("关闭熊市降仓，风险暴露更高，收益弹性也更强。")
    if "cap80" in strategy_id:
        risk_lines.append("单票权重上限约 80%，允许高集中但保留上限约束。")
    elif "cap60" in strategy_id:
        risk_lines.append("单票权重上限约 60%，集中度略低于 cap80。")
    if "sat_three_stage" in strategy_id:
        risk_lines.append("卫星仓位采用周频三档风控，股票池不必月中重选，但卫星暴露会随周度状态变化。")
    if "port_weekly_exposure" in strategy_id:
        risk_lines.append("采用月度选股 + 周度总仓位调整，月中主要调整总暴露而不是重新换股。")
    if "buffered" in strategy_id:
        risk_lines.append("带 buffered 确认，降低单周信号噪声导致的来回切换。")
    if "asym" in strategy_id:
        risk_lines.append("采用快减慢加的不对称仓位路径，风险变差时更快降仓，恢复时更慢加仓。")
    if not risk_lines:
        risk_lines.append("风险控制主要来自策略自身的趋势、动量、仓位或调仓频率约束。")

    schedule_lines = {
        "monthly": "当前建议按真实月末换股生成；数据截止日可以每天推进，但月度股票池本身不应被临时月末提前改写。",
        "portfolio_weekly_overlay": "股票池按真实月末确定；周度只更新总仓位/风险暴露，因此实盘上可能不等到月末就先降仓或加仓。",
        "satellite_weekly_overlay": "月末确定股票池和目标权重；周度只调整卫星仓位状态，因此页面会把月末股票池与周度卫星暴露拆开看。",
        "biweekly": "策略按双周评估点换股，当前建议会在双周信号日更新。",
        "weekly": "策略按周评估点换股，当前建议会在周度信号日更新。",
    }
    schedule_text = schedule_lines.get(str(schedule_kind or ""), "当前建议按策略定义的实际评估点更新。")

    metric_parts = []
    for key, label in (
        ("total_return", "Total Return"),
        ("cagr", "CAGR"),
        ("max_drawdown", "MaxDD"),
        ("sharpe_ratio", "Sharpe"),
        ("average_annual_turnover", "Turnover"),
    ):
        if key not in metrics:
            continue
        value = float(metrics[key])
        if key in {"sharpe_ratio", "average_annual_turnover"}:
            formatted = f"{value:.2f}"
        else:
            formatted = fmt_pct(value)
        metric_parts.append(f"{label} {formatted}")
    metrics_text = " | ".join(metric_parts) if metric_parts else "暂无窗口指标。"

    def list_html(lines: list[str]) -> str:
        return "<ul>" + "".join(f"<li>{html.escape(line)}</li>" for line in lines) + "</ul>"

    return (
        "<details class='card' style='margin-top:16px'>"
        "<summary style='cursor:pointer;font-size:20px;font-weight:700'>策略详细说明</summary>"
        f"<p><strong>{html.escape(display_name)}</strong></p>"
        f"<p class='muted'>{html.escape(role_text)}</p>"
        f"<p>当前查看窗口：{html.escape(active_sample_label)}；{html.escape(metrics_text)}</p>"
        "<h3>策略定位</h3>"
        + list_html([f"标的范围：{universe}。", core_source])
        + "<h3>选股与组合结构</h3>"
        + list_html(selection_lines)
        + "<h3>仓位与风控</h3>"
        + list_html(risk_lines)
        + "<h3>调仓/生效规则</h3>"
        + list_html([f"实际调整类型：{adjustment_style}。", f"当前判定口径：{schedule_kind_label(schedule_kind)}。", schedule_text])
        + "</details>"
    )


def winner_windows_label(winner_tags: list[str] | None) -> str:
    if not winner_tags:
        return ""
    label_map = {
        "2017-window winner": "2017",
        "2020-window winner": "2020",
        "2023-window winner": "2023",
        "2025-window winner": "2025",
        "2026-window winner": "2026",
    }
    windows: list[str] = []
    for tag in winner_tags:
        winner_type = str(tag).split(":")[-1]
        label = label_map.get(winner_type)
        if label and label not in windows:
            windows.append(label)
    ordered = [key for key in ("2017", "2020", "2023", "2025", "2026") if key in windows]
    return " / ".join(ordered)


def winner_identity_label(winner_tags: list[str] | None) -> str:
    if not winner_tags:
        return ""
    labels: list[str] = []
    for tag in winner_tags:
        winner_type = str(tag).split(":")[-1]
        if winner_type.endswith("window winner"):
            label = "窗口赢家"
        elif winner_type == "robust candidate":
            label = "鲁棒候选"
        else:
            label = winner_type
        if label not in labels:
            labels.append(label)
    return " / ".join(labels)


def _select_previous_close(rows: list[dict[str, str]], today_tag: str) -> float | None:
    eligible = [row for row in rows if str(row.get("trade_date") or "") < today_tag]
    candidate = eligible[-1] if eligible else (rows[-1] if rows else None)
    if candidate is None:
        return None
    try:
        return float(candidate["close"])
    except Exception:
        return None


def ensure_live_data() -> None:
    registry_path = LIVE_DIR / "strategy_registry.json"
    if registry_path.exists():
        return
    from scripts.export_live_platform_data import export_live_data

    export_live_data()


def load_registry() -> dict:
    ensure_live_data()
    return json.loads((LIVE_DIR / "strategy_registry.json").read_text(encoding="utf-8"))


def load_strategy_snapshot(strategy_id: str) -> dict:
    ensure_live_data()
    return json.loads((LIVE_DIR / "strategies" / f"{strategy_id}.json").read_text(encoding="utf-8"))


def load_default_strategy_id() -> str:
    tracked = json.loads((RESULTS_DIR / "weighted_track_winners.json").read_text(encoding="utf-8"))
    return str(tracked["tracks"][DEFAULT_TRACKED_WINNER_KEY]["winner"])


def connect_db() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    conn = connect_db()
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            broker TEXT NOT NULL,
            note TEXT DEFAULT '',
            initial_capital REAL NOT NULL DEFAULT 0,
            total_assets REAL NOT NULL,
            cash REAL NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS account_holdings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            ts_code TEXT NOT NULL,
            name TEXT NOT NULL,
            shares REAL NOT NULL,
            cost_price REAL NOT NULL DEFAULT 0,
            last_price REAL NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS account_strategy_bindings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL UNIQUE,
            strategy_id TEXT NOT NULL,
            effective_date TEXT NOT NULL,
            enable_switch_suggestion INTEGER NOT NULL DEFAULT 1,
            manual_exposure_override REAL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS rebalance_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            strategy_id TEXT NOT NULL,
            task_type TEXT NOT NULL,
            status TEXT NOT NULL,
            target_snapshot_json TEXT NOT NULL,
            current_snapshot_json TEXT NOT NULL,
            diff_json TEXT NOT NULL,
            estimated_buy_amount REAL NOT NULL,
            estimated_sell_amount REAL NOT NULL,
            estimated_cost REAL NOT NULL,
            note TEXT DEFAULT '',
            actual_execution_json TEXT,
            created_at TEXT NOT NULL,
            executed_at TEXT
        );

        CREATE TABLE IF NOT EXISTS account_trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER NOT NULL,
            task_id INTEGER,
            ts_code TEXT NOT NULL,
            name TEXT NOT NULL,
            side TEXT NOT NULL,
            shares REAL NOT NULL,
            price REAL NOT NULL,
            gross_amount REAL NOT NULL,
            fee REAL NOT NULL,
            net_cash_change REAL NOT NULL,
            realized_pnl REAL,
            note TEXT DEFAULT '',
            executed_at TEXT NOT NULL
        );
        """
    )
    columns = {row["name"] for row in cur.execute("PRAGMA table_info(account_holdings)").fetchall()}
    if "cost_price" not in columns:
        try:
            cur.execute("ALTER TABLE account_holdings ADD COLUMN cost_price REAL NOT NULL DEFAULT 0")
        except sqlite3.OperationalError as exc:
            if "duplicate column name" not in str(exc).lower():
                raise
    account_columns = {row["name"] for row in cur.execute("PRAGMA table_info(accounts)").fetchall()}
    if "initial_capital" not in account_columns:
        try:
            cur.execute("ALTER TABLE accounts ADD COLUMN initial_capital REAL NOT NULL DEFAULT 0")
            cur.execute("UPDATE accounts SET initial_capital = total_assets WHERE initial_capital = 0")
        except sqlite3.OperationalError as exc:
            if "duplicate column name" not in str(exc).lower():
                raise
    task_columns = {row["name"] for row in cur.execute("PRAGMA table_info(rebalance_tasks)").fetchall()}
    if "actual_execution_json" not in task_columns:
        try:
            cur.execute("ALTER TABLE rebalance_tasks ADD COLUMN actual_execution_json TEXT")
        except sqlite3.OperationalError as exc:
            if "duplicate column name" not in str(exc).lower():
                raise
    conn.commit()
    conn.close()


def seed_demo_data() -> None:
    init_db()
    conn = connect_db()
    cur = conn.cursor()
    account_count = cur.execute("SELECT COUNT(*) FROM accounts").fetchone()[0]
    if account_count == 0:
        ts = now_str()
        cur.execute(
            "INSERT INTO accounts (name, broker, note, initial_capital, total_assets, cash, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (DEFAULT_ACCOUNT_NAME, DEFAULT_ACCOUNT_BROKER, "默认测试账户，100万本金", DEFAULT_CAPITAL, DEFAULT_CAPITAL, DEFAULT_CAPITAL, ts),
        )
        account_id = int(cur.lastrowid)
        strategy_id = load_default_strategy_id()
        cur.execute(
            """
            INSERT INTO account_strategy_bindings
            (account_id, strategy_id, effective_date, enable_switch_suggestion, manual_exposure_override, updated_at)
            VALUES (?, ?, ?, 1, NULL, ?)
            """,
            (account_id, strategy_id, ts[:10], ts),
        )
        conn.commit()
    conn.close()


def get_accounts() -> list[sqlite3.Row]:
    conn = connect_db()
    rows = conn.execute("SELECT * FROM accounts ORDER BY id").fetchall()
    conn.close()
    return rows


def create_account(*, name: str, broker: str, note: str, initial_cash: float, strategy_id: str) -> int:
    ts = now_str()
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO accounts (name, broker, note, initial_capital, total_assets, cash, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name, broker, note, float(initial_cash), float(initial_cash), float(initial_cash), ts),
    )
    account_id = int(cur.lastrowid)
    cur.execute(
        """
        INSERT INTO account_strategy_bindings
        (account_id, strategy_id, effective_date, enable_switch_suggestion, manual_exposure_override, updated_at)
        VALUES (?, ?, ?, 1, NULL, ?)
        """,
        (account_id, strategy_id, ts[:10], ts),
    )
    conn.commit()
    conn.close()
    return account_id


def get_account(account_id: int) -> sqlite3.Row | None:
    conn = connect_db()
    row = conn.execute("SELECT * FROM accounts WHERE id = ?", (account_id,)).fetchone()
    conn.close()
    return row


def get_binding(account_id: int) -> sqlite3.Row | None:
    conn = connect_db()
    row = conn.execute("SELECT * FROM account_strategy_bindings WHERE account_id = ?", (account_id,)).fetchone()
    conn.close()
    return row


def update_binding_strategy(account_id: int, strategy_id: str) -> None:
    ts = now_str()
    conn = connect_db()
    conn.execute(
        """
        UPDATE account_strategy_bindings
        SET strategy_id = ?, effective_date = ?, updated_at = ?
        WHERE account_id = ?
        """,
        (strategy_id, ts[:10], ts, account_id),
    )
    conn.commit()
    conn.close()


def get_holdings(account_id: int) -> list[sqlite3.Row]:
    conn = connect_db()
    rows = conn.execute(
        "SELECT * FROM account_holdings WHERE account_id = ? ORDER BY ts_code",
        (account_id,),
    ).fetchall()
    conn.close()
    return rows


@lru_cache(maxsize=1)
def load_name_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    if not STOCK_BASIC_PATH.exists():
        return mapping
    with STOCK_BASIC_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts_code = str(row.get("ts_code") or "").strip()
            name = str(row.get("name") or "").strip()
            if ts_code and name:
                mapping[ts_code] = name
    return mapping


def infer_name(ts_code: str) -> str:
    return load_name_map().get(ts_code, ts_code)


def _latest_price_from_daily_cache(ts_code: str) -> tuple[float | None, str]:
    path = DAILY_CACHE_DIR / f"{ts_code}.csv"
    if not path.exists():
        return None, "missing"
    try:
        with path.open("r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except Exception:
        return None, "cache_error"
    if not rows:
        return None, "empty"
    try:
        return float(rows[-1]["close"]), "daily_cache_latest"
    except Exception:
        return None, "parse_error"


def _previous_close_from_daily_cache(ts_code: str) -> tuple[float | None, str]:
    path = DAILY_CACHE_DIR / f"{ts_code}.csv"
    if not path.exists():
        return None, "missing"
    try:
        with path.open("r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
    except Exception:
        return None, "cache_error"
    if not rows:
        return None, "empty"
    previous_close = _select_previous_close(rows, _today_trade_tag())
    if previous_close is None:
        return None, "parse_error"
    return previous_close, "daily_cache_prev_close"


def _latest_price_from_tushare_minute(ts_code: str) -> tuple[float | None, str]:
    try:
        import tushare as ts
    except Exception:
        return None, "no_tushare"
    try:
        end_dt = datetime.now()
        start_dt = end_dt - timedelta(days=2)
        frame = ts.pro_bar(
            ts_code=ts_code,
            asset="E",
            freq="1min",
            start_date=start_dt.strftime("%Y-%m-%d %H:%M:%S"),
            end_date=end_dt.strftime("%Y-%m-%d %H:%M:%S"),
            adj=None,
            token=TUSHARE_MINUTE_TOKEN,
        )
        if frame is not None and not frame.empty:
            frame = frame.sort_values(frame.columns[0] if "trade_time" not in frame.columns else "trade_time")
            return float(frame.iloc[-1]["close"]), "tushare_minute_live"
    except Exception:
        return None, "minute_failed"
    return None, "minute_empty"


def _latest_price_from_tushare_daily(ts_code: str) -> tuple[float | None, str]:
    try:
        import tushare as ts
    except Exception:
        return None, "no_tushare"
    try:
        pro = ts.pro_api(TUSHARE_DAILY_TOKEN)
        end_dt = datetime.now()
        start_dt = end_dt - timedelta(days=10)
        frame = pro.daily(
            ts_code=ts_code,
            start_date=start_dt.strftime("%Y%m%d"),
            end_date=end_dt.strftime("%Y%m%d"),
        )
        if frame is not None and not frame.empty:
            frame = frame.sort_values("trade_date")
            return float(frame.iloc[-1]["close"]), "tushare_daily_latest"
    except Exception:
        return None, "daily_failed"
    return None, "daily_empty"


def _previous_close_from_tushare_daily(ts_code: str) -> tuple[float | None, str]:
    try:
        import tushare as ts
    except Exception:
        return None, "no_tushare"
    try:
        pro = ts.pro_api(TUSHARE_DAILY_TOKEN)
        end_dt = shanghai_now()
        start_dt = end_dt - timedelta(days=15)
        frame = pro.daily(
            ts_code=ts_code,
            start_date=start_dt.strftime("%Y%m%d"),
            end_date=end_dt.strftime("%Y%m%d"),
        )
        if frame is not None and not frame.empty:
            frame = frame.sort_values("trade_date")
            rows = frame.to_dict("records")
            previous_close = _select_previous_close(rows, _today_trade_tag(end_dt))
            if previous_close is not None:
                return previous_close, "tushare_daily_prev_close"
    except Exception:
        return None, "daily_failed"
    return None, "daily_empty"


@lru_cache(maxsize=4096)
def _get_latest_price_cached(ts_code: str, bucket: str, market_open: bool) -> tuple[float | None, str]:
    if market_open:
        price, source = _latest_price_from_tushare_minute(ts_code)
        if price is not None:
            return price, source
        price, source = _previous_close_from_tushare_daily(ts_code)
        if price is not None:
            return price, source
        return _previous_close_from_daily_cache(ts_code)

    price, source = _previous_close_from_tushare_daily(ts_code)
    if price is not None:
        return price, source
    return _previous_close_from_daily_cache(ts_code)


def get_latest_price(ts_code: str) -> tuple[float | None, str]:
    bucket, market_open = _price_cache_bucket()
    return _get_latest_price_cached(ts_code, bucket, market_open)


def save_account_snapshot(account_id: int, *, cash: float, holdings: list[dict[str, float | str]]) -> None:
    ts = now_str()
    total_market_value = 0.0
    normalized_holdings: list[dict[str, float | str]] = []
    for item in holdings:
        ts_code = str(item["ts_code"])
        latest_price, _ = get_latest_price(ts_code)
        latest_price = float(latest_price or 0.0)
        total_market_value += float(item["shares"]) * latest_price
        normalized_holdings.append(
            {
                "ts_code": ts_code,
                "name": str(item["name"]),
                "shares": float(item["shares"]),
                "cost_price": float(item["cost_price"]),
                "last_price": latest_price,
            }
        )
    total_assets = float(cash) + total_market_value
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE accounts SET cash = ?, total_assets = ?, updated_at = ? WHERE id = ?",
        (float(cash), float(total_assets), ts, account_id),
    )
    cur.execute("DELETE FROM account_holdings WHERE account_id = ?", (account_id,))
    for item in normalized_holdings:
        cur.execute(
            """
            INSERT INTO account_holdings (account_id, ts_code, name, shares, cost_price, last_price, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                account_id,
                str(item["ts_code"]),
                str(item["name"]),
                float(item["shares"]),
                float(item["cost_price"]),
                float(item["last_price"]),
                ts,
            ),
        )
    conn.commit()
    conn.close()


def reconcile_manual_snapshot_trades(
    account_id: int,
    previous_rows: list[sqlite3.Row],
    new_holdings: list[dict[str, float | str]],
    *,
    note: str = "manual_snapshot_sync",
) -> None:
    if not previous_rows:
        return

    previous_map: dict[str, dict[str, float | str]] = {
        str(row["ts_code"]): {
            "ts_code": str(row["ts_code"]),
            "name": str(row["name"]),
            "shares": float(row["shares"]),
            "cost_price": float(row["cost_price"]),
            "last_price": float(row["last_price"]),
        }
        for row in previous_rows
    }
    new_map: dict[str, dict[str, float | str]] = {
        str(item["ts_code"]): {
            "ts_code": str(item["ts_code"]),
            "name": str(item["name"]),
            "shares": float(item["shares"]),
            "cost_price": float(item["cost_price"]),
        }
        for item in new_holdings
    }

    all_codes = sorted(set(previous_map) | set(new_map))
    for ts_code in all_codes:
        prev = previous_map.get(ts_code)
        new = new_map.get(ts_code)
        old_shares = float(prev["shares"]) if prev else 0.0
        new_shares = float(new["shares"]) if new else 0.0
        delta = new_shares - old_shares
        if abs(delta) <= 1e-8:
            continue

        name = str((new or prev or {}).get("name") or infer_name(ts_code))
        if delta > 0:
            old_cost_amount = (float(prev["cost_price"]) * old_shares) if prev else 0.0
            new_cost_amount = float(new["cost_price"]) * new_shares if new else 0.0
            inferred_price = (new_cost_amount - old_cost_amount) / delta if delta > 0 else float((new or {}).get("cost_price") or 0.0)
            if inferred_price <= 0:
                inferred_price = float((new or {}).get("cost_price") or 0.0)
            gross_amount = delta * inferred_price
            _record_account_trade(
                account_id=account_id,
                task_id=None,
                ts_code=ts_code,
                name=name,
                side="buy",
                shares=delta,
                price=inferred_price,
                gross_amount=gross_amount,
                fee=0.0,
                net_cash_change=-gross_amount,
                realized_pnl=None,
                note=note,
            )
        else:
            sell_shares = abs(delta)
            inferred_price, _ = get_latest_price(ts_code)
            price = float(inferred_price or (prev["last_price"] if prev else 0.0) or (prev["cost_price"] if prev else 0.0))
            gross_amount = sell_shares * price
            prev_cost = float(prev["cost_price"]) if prev else 0.0
            realized_pnl = sell_shares * (price - prev_cost)
            _record_account_trade(
                account_id=account_id,
                task_id=None,
                ts_code=ts_code,
                name=name,
                side="sell",
                shares=sell_shares,
                price=price,
                gross_amount=gross_amount,
                fee=0.0,
                net_cash_change=gross_amount,
                realized_pnl=realized_pnl,
                note=note,
            )


def get_tasks(account_id: int | None = None) -> list[sqlite3.Row]:
    conn = connect_db()
    if account_id is None:
        rows = conn.execute("SELECT * FROM rebalance_tasks ORDER BY id DESC").fetchall()
    else:
        rows = conn.execute("SELECT * FROM rebalance_tasks WHERE account_id = ? ORDER BY id DESC", (account_id,)).fetchall()
    conn.close()
    return rows


def get_account_trades(account_id: int, limit: int = 50) -> list[sqlite3.Row]:
    conn = connect_db()
    rows = conn.execute(
        "SELECT * FROM account_trades WHERE account_id = ? ORDER BY id DESC LIMIT ?",
        (account_id, limit),
    ).fetchall()
    conn.close()
    return rows


def get_trade(trade_id: int) -> sqlite3.Row | None:
    conn = connect_db()
    row = conn.execute("SELECT * FROM account_trades WHERE id = ?", (trade_id,)).fetchone()
    conn.close()
    return row


def get_task(task_id: int) -> sqlite3.Row | None:
    conn = connect_db()
    row = conn.execute("SELECT * FROM rebalance_tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    return row


def task_actual_fills(task: sqlite3.Row) -> list[dict[str, float | str]]:
    raw = task["actual_execution_json"]
    if not raw:
        return []
    try:
        payload = json.loads(raw)
    except Exception:
        return []
    fills = payload.get("fills")
    return fills if isinstance(fills, list) else []


def task_fill_progress(task: sqlite3.Row) -> tuple[list[dict[str, float | str]], bool]:
    diffs = json.loads(task["diff_json"])
    actual_fills = task_actual_fills(task)
    actual_by_code: dict[str, float] = {}
    for fill in actual_fills:
        ts_code = str(fill.get("ts_code") or "")
        if not ts_code:
            continue
        shares = float(fill.get("shares") or 0.0)
        actual_by_code[ts_code] = actual_by_code.get(ts_code, 0.0) + shares

    progress: list[dict[str, float | str]] = []
    completed = True
    for item in diffs:
        target_shares = float(item.get("reference_shares") or 0.0)
        if abs(target_shares) <= 1e-8:
            continue
        ts_code = str(item["ts_code"])
        actual_signed = actual_by_code.get(ts_code, 0.0)
        remaining = target_shares - actual_signed
        done = abs(remaining) <= 1e-6
        completed = completed and done
        progress.append(
            {
                "ts_code": ts_code,
                "name": str(item["name"]),
                "target_shares": target_shares,
                "actual_shares": actual_signed,
                "remaining_shares": remaining,
                "done": done,
            }
        )
    return progress, completed


def find_open_task(account_id: int, *, task_type: str | None = None, strategy_id: str | None = None) -> sqlite3.Row | None:
    conn = connect_db()
    query = "SELECT * FROM rebalance_tasks WHERE account_id = ? AND status IN ('ready', 'partial')"
    params: list[object] = [account_id]
    if task_type is not None:
        query += " AND task_type = ?"
        params.append(task_type)
    if strategy_id is not None:
        query += " AND strategy_id = ?"
        params.append(strategy_id)
    query += " ORDER BY id DESC LIMIT 1"
    row = conn.execute(query, tuple(params)).fetchone()
    conn.close()
    return row


def account_market_value(holdings: list[sqlite3.Row]) -> float:
    return float(sum(float(row["shares"]) * float(row["last_price"]) for row in holdings))


def current_positions_snapshot(account_id: int) -> dict:
    account = get_account(account_id)
    holdings = get_holdings(account_id)
    positions = []
    market_value = 0.0
    price_sources: set[str] = set()
    for row in holdings:
        latest_price, source = get_latest_price(row["ts_code"])
        last_price = float(latest_price or row["last_price"] or 0.0)
        amount = float(row["shares"]) * last_price
        cost_amount = float(row["shares"]) * float(row["cost_price"])
        unrealized_pnl = amount - cost_amount
        unrealized_pnl_pct = unrealized_pnl / cost_amount if cost_amount > 0 else 0.0
        market_value += amount
        price_sources.add(source)
        positions.append(
            {
                "ts_code": row["ts_code"],
                "name": row["name"],
                "shares": float(row["shares"]),
                "cost_price": float(row["cost_price"]),
                "last_price": last_price,
                "market_value": amount,
                "cost_amount": cost_amount,
                "unrealized_pnl": unrealized_pnl,
                "unrealized_pnl_pct": unrealized_pnl_pct,
            }
        )
    total_assets = float(account["cash"]) + market_value
    for item in positions:
        item["weight"] = item["market_value"] / total_assets if total_assets > 0 else 0.0
    return {
        "account_id": account_id,
        "cash": float(account["cash"]),
        "market_value": market_value,
        "total_assets": total_assets,
        "positions": positions,
        "price_source": ", ".join(sorted(price_sources)) if price_sources else "unknown",
        "price_source_label": "；".join(describe_price_source(source) for source in sorted(price_sources)) if price_sources else describe_price_source("unknown"),
    }


def estimate_task(account_id: int, strategy_id: str, task_type: str) -> dict:
    account = get_account(account_id)
    snapshot = load_strategy_snapshot(strategy_id)
    current = current_positions_snapshot(account_id)
    total_assets = float(current["total_assets"])
    target_exposure = float(snapshot.get("target_total_exposure") or 1.0)
    target_equity = total_assets * target_exposure

    current_map = {item["ts_code"]: item for item in current["positions"]}
    diffs = []
    buy_amount = 0.0
    sell_amount = 0.0
    seen_codes: set[str] = set()

    for item in snapshot.get("latest_weights", []):
        ts_code = str(item["ts_code"])
        seen_codes.add(ts_code)
        current_item = current_map.get(ts_code)
        current_amount = float(current_item["market_value"]) if current_item else 0.0
        current_weight = float(current_item["weight"]) if current_item else 0.0
        target_weight = float(item["weight"])
        target_amount = target_equity * target_weight
        diff_amount = target_amount - current_amount
        last_price = item.get("latest_price") or (current_item["last_price"] if current_item else None)
        ref_shares = diff_amount / last_price if last_price else None
        if diff_amount > 0:
            buy_amount += diff_amount
        else:
            sell_amount += -diff_amount
        diffs.append(
            {
                "ts_code": ts_code,
                "name": str(item["name"]),
                "current_weight": current_weight,
                "target_weight": target_weight,
                "current_amount": current_amount,
                "target_amount": target_amount,
                "diff_amount": diff_amount,
                "last_price": last_price,
                "reference_shares": ref_shares,
                "action": "买入" if diff_amount > 1e-8 else ("卖出" if diff_amount < -1e-8 else "不动"),
            }
        )

    for ts_code, current_item in current_map.items():
        if ts_code in seen_codes:
            continue
        diff_amount = -float(current_item["market_value"])
        sell_amount += -diff_amount
        diffs.append(
            {
                "ts_code": ts_code,
                "name": str(current_item["name"]),
                "current_weight": float(current_item["weight"]),
                "target_weight": 0.0,
                "current_amount": float(current_item["market_value"]),
                "target_amount": 0.0,
                "diff_amount": diff_amount,
                "last_price": float(current_item["last_price"]),
                "reference_shares": -float(current_item["shares"]),
                "action": "卖出",
            }
        )

    estimated_cost = buy_amount * BUY_COMMISSION + sell_amount * (SELL_COMMISSION + SELL_STAMP_DUTY)
    return {
        "account_name": account["name"],
        "strategy_id": strategy_id,
        "strategy_display_name": snapshot["display_name"],
        "task_type": task_type,
        "target_exposure": target_exposure,
        "risk_state": snapshot["risk_state"],
        "current_snapshot": current,
        "target_snapshot": snapshot,
        "diffs": sorted(diffs, key=lambda x: abs(float(x["diff_amount"])), reverse=True),
        "estimated_buy_amount": buy_amount,
        "estimated_sell_amount": sell_amount,
        "estimated_cost": estimated_cost,
    }


def create_task(account_id: int, strategy_id: str, task_type: str) -> int:
    existing = find_open_task(account_id, task_type=task_type, strategy_id=strategy_id)
    if existing is not None:
        return int(existing["id"])
    payload = estimate_task(account_id, strategy_id, task_type)
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO rebalance_tasks
        (account_id, strategy_id, task_type, status, target_snapshot_json, current_snapshot_json, diff_json,
         estimated_buy_amount, estimated_sell_amount, estimated_cost, note, created_at)
        VALUES (?, ?, ?, 'ready', ?, ?, ?, ?, ?, ?, '', ?)
        """,
        (
            account_id,
            strategy_id,
            task_type,
            json.dumps(payload["target_snapshot"], ensure_ascii=False),
            json.dumps(payload["current_snapshot"], ensure_ascii=False),
            json.dumps(payload["diffs"], ensure_ascii=False),
            payload["estimated_buy_amount"],
            payload["estimated_sell_amount"],
            payload["estimated_cost"],
            now_str(),
        ),
    )
    task_id = int(cur.lastrowid)
    conn.commit()
    conn.close()
    return task_id


def _record_account_trade(
    *,
    account_id: int,
    task_id: int | None,
    ts_code: str,
    name: str,
    side: str,
    shares: float,
    price: float,
    gross_amount: float,
    fee: float,
    net_cash_change: float,
    realized_pnl: float | None,
    note: str,
) -> None:
    conn = connect_db()
    conn.execute(
        """
        INSERT INTO account_trades
        (account_id, task_id, ts_code, name, side, shares, price, gross_amount, fee, net_cash_change, realized_pnl, note, executed_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            account_id,
            task_id,
            ts_code,
            name,
            side,
            shares,
            price,
            gross_amount,
            fee,
            net_cash_change,
            realized_pnl,
            note,
            now_str(),
        ),
    )
    conn.commit()
    conn.close()


def _apply_signed_trade_to_account(
    *,
    account_id: int,
    ts_code: str,
    name: str,
    signed_shares: float,
    price: float,
) -> dict[str, float | str | None]:
    if abs(signed_shares) <= 1e-8:
        raise ValueError("成交数量不能为 0")
    if price <= 0:
        raise ValueError("成交价格必须大于 0")

    account = get_account(account_id)
    if account is None:
        raise ValueError("账户不存在")
    current_rows = get_holdings(account_id)
    holdings_map: dict[str, dict[str, float | str]] = {
        str(row["ts_code"]): {
            "ts_code": str(row["ts_code"]),
            "name": str(row["name"]),
            "shares": float(row["shares"]),
            "cost_price": float(row["cost_price"]),
        }
        for row in current_rows
    }
    cash = float(account["cash"])
    gross_amount = abs(signed_shares) * price

    if signed_shares > 0:
        fee = gross_amount * BUY_COMMISSION
        position = holdings_map.get(
            ts_code,
            {"ts_code": ts_code, "name": name, "shares": 0.0, "cost_price": 0.0},
        )
        old_shares = float(position["shares"])
        old_cost_price = float(position["cost_price"])
        new_shares = old_shares + signed_shares
        new_cost_price = (
            ((old_shares * old_cost_price) + (signed_shares * price)) / new_shares if new_shares > 0 else price
        )
        position["shares"] = new_shares
        position["cost_price"] = new_cost_price
        position["name"] = name or str(position["name"])
        holdings_map[ts_code] = position
        cash -= gross_amount + fee
        realized_pnl = None
        side = "buy"
        net_cash_change = -(gross_amount + fee)
    else:
        sell_shares = abs(signed_shares)
        position = holdings_map.get(ts_code)
        if position is None or float(position["shares"]) + 1e-8 < sell_shares:
            raise ValueError(f"{ts_code} 可卖数量不足，无法录入该笔卖出")
        old_shares = float(position["shares"])
        old_cost_price = float(position["cost_price"])
        remaining = old_shares - sell_shares
        fee = gross_amount * (SELL_COMMISSION + SELL_STAMP_DUTY)
        cash += gross_amount - fee
        realized_pnl = sell_shares * (price - old_cost_price) - fee
        if remaining <= 1e-8:
            holdings_map.pop(ts_code, None)
        else:
            position["shares"] = remaining
            holdings_map[ts_code] = position
        side = "sell"
        net_cash_change = gross_amount - fee

    save_account_snapshot(account_id, cash=max(cash, 0.0), holdings=list(holdings_map.values()))
    return {
        "side": side,
        "shares": abs(signed_shares),
        "price": price,
        "gross_amount": gross_amount,
        "fee": fee,
        "net_cash_change": net_cash_change,
        "realized_pnl": realized_pnl,
    }


def _infer_cost_from_sell_trade(trade: sqlite3.Row) -> float:
    shares = float(trade["shares"] or 0.0)
    price = float(trade["price"] or 0.0)
    fee = float(trade["fee"] or 0.0)
    realized = float(trade["realized_pnl"] or 0.0)
    if shares <= 0:
        return price
    return price - ((realized + fee) / shares)


def create_manual_trade_entry(
    *,
    account_id: int,
    side: str,
    ts_code: str,
    name: str,
    shares: float,
    price: float,
    note: str = "",
) -> int:
    signed_shares = shares if side == "buy" else -shares
    result = _apply_signed_trade_to_account(
        account_id=account_id,
        ts_code=ts_code,
        name=name or infer_name(ts_code),
        signed_shares=signed_shares,
        price=price,
    )
    conn = connect_db()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO account_trades
        (account_id, task_id, ts_code, name, side, shares, price, gross_amount, fee, net_cash_change, realized_pnl, note, executed_at)
        VALUES (?, NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            account_id,
            ts_code,
            name or infer_name(ts_code),
            side,
            float(result["shares"]),
            float(result["price"]),
            float(result["gross_amount"]),
            float(result["fee"]),
            float(result["net_cash_change"]),
            float(result["realized_pnl"]) if result["realized_pnl"] is not None else None,
            note or "manual_entry",
            now_str(),
        ),
    )
    trade_id = int(cur.lastrowid)
    conn.commit()
    conn.close()
    return trade_id


def update_manual_trade_entry(
    *,
    trade_id: int,
    side: str,
    ts_code: str,
    name: str,
    shares: float,
    price: float,
    note: str = "",
) -> None:
    trade = get_trade(trade_id)
    if trade is None:
        raise ValueError("交易记录不存在")
    if trade["task_id"] is not None:
        raise ValueError("任务生成的交易记录暂不支持直接编辑")
    old_side = str(trade["side"])
    if old_side != side:
        raise ValueError("当前版本暂不支持直接修改买卖方向，请新建一笔修正交易")

    account_id = int(trade["account_id"])
    account = get_account(account_id)
    if account is None:
        raise ValueError("账户不存在")
    current_rows = get_holdings(account_id)
    holdings_map: dict[str, dict[str, float | str]] = {
        str(row["ts_code"]): {
            "ts_code": str(row["ts_code"]),
            "name": str(row["name"]),
            "shares": float(row["shares"]),
            "cost_price": float(row["cost_price"]),
        }
        for row in current_rows
    }
    cash = float(account["cash"])

    old_qty = float(trade["shares"] or 0.0)
    old_price = float(trade["price"] or 0.0)
    old_fee = float(trade["fee"] or 0.0)
    old_gross = float(trade["gross_amount"] or 0.0)
    old_realized = float(trade["realized_pnl"] or 0.0) if trade["realized_pnl"] is not None else None

    if side == "buy":
        position = holdings_map.get(ts_code, {"ts_code": ts_code, "name": name or infer_name(ts_code), "shares": 0.0, "cost_price": 0.0})
        current_shares = float(position["shares"])
        current_cost_price = float(position["cost_price"])
        delta_qty = shares - old_qty
        new_hold_shares = current_shares + delta_qty
        if new_hold_shares < -1e-8:
            raise ValueError("该买入交易已经被后续卖出消化，当前版本暂不支持回溯修改，请新增修正交易")
        old_net = -(old_gross + old_fee)
        new_gross = shares * price
        new_fee = new_gross * BUY_COMMISSION
        new_net = -(new_gross + new_fee)
        cash += new_net - old_net
        if new_hold_shares <= 1e-8:
            holdings_map.pop(ts_code, None)
        else:
            current_total_cost = current_shares * current_cost_price
            new_total_cost = current_total_cost + (new_gross - old_gross)
            position["shares"] = new_hold_shares
            position["cost_price"] = new_total_cost / new_hold_shares if new_hold_shares > 0 else price
            position["name"] = name or str(position["name"])
            holdings_map[ts_code] = position
        new_realized = None
        net_cash_change = new_net
        gross_amount = new_gross
        fee = new_fee
    else:
        position = holdings_map.get(ts_code)
        current_shares = float(position["shares"]) if position else 0.0
        delta_position = old_qty - shares
        new_hold_shares = current_shares + delta_position
        if new_hold_shares < -1e-8:
            raise ValueError("该卖出交易已经被后续持仓变化覆盖，当前版本暂不支持回溯修改，请新增修正交易")
        old_net = old_gross - old_fee
        new_gross = shares * price
        new_fee = new_gross * (SELL_COMMISSION + SELL_STAMP_DUTY)
        new_net = new_gross - new_fee
        cash += new_net - old_net
        if position is None and new_hold_shares > 1e-8:
            inferred_cost = _infer_cost_from_sell_trade(trade)
            holdings_map[ts_code] = {
                "ts_code": ts_code,
                "name": name or infer_name(ts_code),
                "shares": new_hold_shares,
                "cost_price": inferred_cost,
            }
        elif position is not None:
            if new_hold_shares <= 1e-8:
                holdings_map.pop(ts_code, None)
            else:
                position["shares"] = new_hold_shares
                position["name"] = name or str(position["name"])
                holdings_map[ts_code] = position
        basis = float(position["cost_price"]) if position else _infer_cost_from_sell_trade(trade)
        new_realized = shares * (price - basis) - new_fee
        net_cash_change = new_net
        gross_amount = new_gross
        fee = new_fee

    save_account_snapshot(account_id, cash=max(cash, 0.0), holdings=list(holdings_map.values()))
    conn = connect_db()
    conn.execute(
        """
        UPDATE account_trades
        SET ts_code = ?, name = ?, side = ?, shares = ?, price = ?, gross_amount = ?, fee = ?, net_cash_change = ?, realized_pnl = ?, note = ?
        WHERE id = ?
        """,
        (
            ts_code,
            name or infer_name(ts_code),
            side,
            shares,
            price,
            gross_amount,
            fee,
            net_cash_change,
            new_realized,
            note or "manual_entry",
            trade_id,
        ),
    )
    conn.commit()
    conn.close()


def mark_task_executed(task_id: int) -> None:
    task = get_task(task_id)
    if task is None:
        return
    target_snapshot = json.loads(task["target_snapshot_json"])
    current_snapshot = json.loads(task["current_snapshot_json"])
    total_assets = float(current_snapshot.get("total_assets", 0.0))
    target_exposure = float(target_snapshot.get("target_total_exposure") or 1.0)
    target_equity = total_assets * target_exposure
    current_positions = {
        str(item["ts_code"]): item for item in current_snapshot.get("positions", [])
    }
    diffs = json.loads(task["diff_json"])
    holdings: list[dict[str, float | str]] = []
    for item in target_snapshot.get("latest_weights", []):
        last_price = float(item.get("latest_price") or 0.0)
        if last_price <= 0:
            fetched_price, _ = get_latest_price(str(item["ts_code"]))
            last_price = float(fetched_price or 0.0)
        if last_price <= 0:
            continue
        target_amount = target_equity * float(item["weight"])
        shares = target_amount / last_price if last_price > 0 else 0.0
        prev = current_positions.get(str(item["ts_code"]))
        holdings.append(
            {
                "ts_code": str(item["ts_code"]),
                "name": str(item["name"]),
                "shares": shares,
                # MVP: preserve old cost if position existed, otherwise use current execution reference price.
                "cost_price": float(prev.get("cost_price", last_price)) if prev else last_price,
            }
        )
    remaining_cash = max(total_assets - target_equity - float(task["estimated_cost"]), 0.0)
    save_account_snapshot(int(task["account_id"]), cash=remaining_cash, holdings=holdings)
    for item in diffs:
        diff_amount = float(item["diff_amount"])
        last_price = float(item.get("last_price") or 0.0)
        ref_shares = float(item.get("reference_shares") or 0.0)
        if abs(diff_amount) <= 1e-8 or last_price <= 0 or abs(ref_shares) <= 1e-8:
            continue
        if diff_amount > 0:
            fee = abs(diff_amount) * BUY_COMMISSION
            _record_account_trade(
                account_id=int(task["account_id"]),
                task_id=task_id,
                ts_code=str(item["ts_code"]),
                name=str(item["name"]),
                side="buy",
                shares=abs(ref_shares),
                price=last_price,
                gross_amount=abs(diff_amount),
                fee=fee,
                net_cash_change=-(abs(diff_amount) + fee),
                realized_pnl=None,
                note="estimated_execution",
            )
        else:
            prev = current_positions.get(str(item["ts_code"]))
            prev_cost = float(prev.get("cost_price", last_price)) if prev else last_price
            gross_amount = abs(diff_amount)
            fee = gross_amount * (SELL_COMMISSION + SELL_STAMP_DUTY)
            realized_pnl = abs(ref_shares) * (last_price - prev_cost) - fee
            _record_account_trade(
                account_id=int(task["account_id"]),
                task_id=task_id,
                ts_code=str(item["ts_code"]),
                name=str(item["name"]),
                side="sell",
                shares=abs(ref_shares),
                price=last_price,
                gross_amount=gross_amount,
                fee=fee,
                net_cash_change=gross_amount - fee,
                realized_pnl=realized_pnl,
                note="estimated_execution",
            )
    conn = connect_db()
    conn.execute("UPDATE rebalance_tasks SET status = 'executed', executed_at = ? WHERE id = ?", (now_str(), task_id))
    conn.commit()
    conn.close()


def parse_execution_fills(text: str) -> list[dict[str, float | str]]:
    fills: list[dict[str, float | str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = [part.strip() for part in line.split(",")]
        if len(parts) not in (3, 4):
            raise ValueError(f"成交输入格式错误：{line}，应为 代码,成交数量,成交价格 或 代码,名称,成交数量,成交价格")
        if len(parts) == 3:
            ts_code, shares_text, price_text = parts
            name = infer_name(ts_code)
        else:
            ts_code, name, shares_text, price_text = parts
            name = name or infer_name(ts_code)
        shares = float(shares_text)
        price = float(price_text)
        if shares == 0:
            continue
        fills.append({"ts_code": ts_code, "name": name, "shares": shares, "price": price})
    return fills


def apply_actual_execution(task_id: int, fills: list[dict[str, float | str]], note: str = "") -> None:
    task = get_task(task_id)
    if task is None:
        return
    account_id = int(task["account_id"])
    account = get_account(account_id)
    if account is None:
        return
    current_rows = get_holdings(account_id)
    holdings_map: dict[str, dict[str, float | str]] = {
        str(row["ts_code"]): {
            "ts_code": str(row["ts_code"]),
            "name": str(row["name"]),
            "shares": float(row["shares"]),
            "cost_price": float(row["cost_price"]),
        }
        for row in current_rows
    }
    cash = float(account["cash"])
    actual_buy_amount = 0.0
    actual_sell_amount = 0.0
    actual_cost = 0.0

    for fill in fills:
        ts_code = str(fill["ts_code"])
        name = str(fill["name"])
        shares = float(fill["shares"])
        price = float(fill["price"])
        gross_amount = abs(shares) * price
        position = holdings_map.get(
            ts_code,
            {"ts_code": ts_code, "name": name, "shares": 0.0, "cost_price": 0.0},
        )
        if shares > 0:
            fee = gross_amount * BUY_COMMISSION
            old_shares = float(position["shares"])
            old_cost_price = float(position["cost_price"])
            new_shares = old_shares + shares
            new_cost_price = (
                ((old_shares * old_cost_price) + (shares * price)) / new_shares if new_shares > 0 else price
            )
            position["shares"] = new_shares
            position["cost_price"] = new_cost_price
            position["name"] = name or str(position["name"])
            holdings_map[ts_code] = position
            cash -= gross_amount + fee
            actual_buy_amount += gross_amount
            actual_cost += fee
            _record_account_trade(
                account_id=account_id,
                task_id=task_id,
                ts_code=ts_code,
                name=name,
                side="buy",
                shares=shares,
                price=price,
                gross_amount=gross_amount,
                fee=fee,
                net_cash_change=-(gross_amount + fee),
                realized_pnl=None,
                note=note or "actual_execution",
            )
        else:
            sell_shares = abs(shares)
            old_shares = float(position["shares"])
            old_cost_price = float(position["cost_price"])
            remaining = max(old_shares - sell_shares, 0.0)
            fee = gross_amount * (SELL_COMMISSION + SELL_STAMP_DUTY)
            cash += gross_amount - fee
            actual_sell_amount += gross_amount
            actual_cost += fee
            realized_pnl = sell_shares * (price - old_cost_price) - fee
            _record_account_trade(
                account_id=account_id,
                task_id=task_id,
                ts_code=ts_code,
                name=name,
                side="sell",
                shares=sell_shares,
                price=price,
                gross_amount=gross_amount,
                fee=fee,
                net_cash_change=gross_amount - fee,
                realized_pnl=realized_pnl,
                note=note or "actual_execution",
            )
            if remaining <= 1e-8:
                holdings_map.pop(ts_code, None)
            else:
                position["shares"] = remaining
                holdings_map[ts_code] = position

    normalized_holdings = list(holdings_map.values())
    save_account_snapshot(account_id, cash=max(cash, 0.0), holdings=normalized_holdings)

    existing_fills = task_actual_fills(task)
    merged_fills = existing_fills + fills
    task_payload = dict(task)
    task_payload["actual_execution_json"] = json.dumps({"fills": merged_fills}, ensure_ascii=False)
    progress, completed = task_fill_progress(task_payload)  # type: ignore[arg-type]
    status = "executed" if completed else "partial"

    conn = connect_db()
    conn.execute(
        """
        UPDATE rebalance_tasks
        SET status = ?,
            executed_at = ?,
            note = ?,
            estimated_buy_amount = estimated_buy_amount + ?,
            estimated_sell_amount = estimated_sell_amount + ?,
            estimated_cost = estimated_cost + ?,
            actual_execution_json = ?
        WHERE id = ?
        """,
        (
            status,
            now_str() if completed else None,
            note,
            actual_buy_amount,
            actual_sell_amount,
            actual_cost,
            json.dumps({"fills": merged_fills}, ensure_ascii=False),
            task_id,
        ),
    )
    conn.commit()
    conn.close()


def cancel_task(task_id: int) -> None:
    conn = connect_db()
    conn.execute("UPDATE rebalance_tasks SET status = 'cancelled' WHERE id = ? AND status IN ('ready', 'partial')", (task_id,))
    conn.commit()
    conn.close()


def delete_task(task_id: int) -> None:
    conn = connect_db()
    conn.execute("DELETE FROM rebalance_tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


def delete_account(account_id: int) -> None:
    conn = connect_db()
    conn.execute("DELETE FROM account_holdings WHERE account_id = ?", (account_id,))
    conn.execute("DELETE FROM account_strategy_bindings WHERE account_id = ?", (account_id,))
    conn.execute("DELETE FROM rebalance_tasks WHERE account_id = ?", (account_id,))
    conn.execute("DELETE FROM accounts WHERE id = ?", (account_id,))
    conn.commit()
    conn.close()


def parse_holdings_text(text: str) -> list[dict[str, float | str]]:
    holdings: list[dict[str, float | str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        parts = [part.strip() for part in line.split(",")]
        if len(parts) == 3:
            ts_code, shares_text, cost_price_text = parts
            name = infer_name(ts_code)
        elif len(parts) == 4:
            ts_code, name, shares_text, cost_price_text = parts
            name = name or infer_name(ts_code)
        else:
            raise ValueError(f"持仓输入格式错误：{line}，应为 代码,数量,成本价 或 代码,名称,数量,成本价")
        shares = float(shares_text)
        cost_price = float(cost_price_text)
        holdings.append(
            {
                "ts_code": ts_code,
                "name": name,
                "shares": shares,
                "cost_price": cost_price,
            }
        )
    return holdings


def parse_holdings_form(form: dict[str, list[str]]) -> list[dict[str, float | str]]:
    ts_codes = form.get("ts_code") or []
    names = form.get("holding_name") or []
    shares_list = form.get("holding_shares") or []
    cost_prices = form.get("holding_cost_price") or []
    holdings: list[dict[str, float | str]] = []
    row_count = max(len(ts_codes), len(names), len(shares_list), len(cost_prices))
    for idx in range(row_count):
        ts_code = (ts_codes[idx] if idx < len(ts_codes) else "").strip()
        name = (names[idx] if idx < len(names) else "").strip()
        shares_text = (shares_list[idx] if idx < len(shares_list) else "").strip()
        cost_price_text = (cost_prices[idx] if idx < len(cost_prices) else "").strip()
        if not ts_code:
            continue
        if not shares_text or not cost_price_text:
            raise ValueError(f"持仓输入不完整：{ts_code} 需要同时填写数量和成本价")
        holdings.append(
            {
                "ts_code": ts_code,
                "name": name or infer_name(ts_code),
                "shares": float(shares_text),
                "cost_price": float(cost_price_text),
            }
        )
    return holdings


def strategy_switch_suggestion(account_id: int) -> dict | None:
    binding = get_binding(account_id)
    if binding is None or not int(binding["enable_switch_suggestion"]):
        return None
    current_strategy = load_strategy_snapshot(binding["strategy_id"])
    registry = load_registry()["strategies"]
    current_path = current_strategy["path"]
    if current_strategy["winner_type"] == "robust candidate":
        return None
    same_path = [item for item in registry if item["path"] == current_path and item["winner_type"] == "robust candidate"]
    if not same_path:
        return None
    suggested = same_path[0]
    if suggested["strategy_id"] == binding["strategy_id"]:
        return None
    return {
        "current_strategy_id": binding["strategy_id"],
        "suggested_strategy_id": suggested["strategy_id"],
        "reason": f"当前账户使用 {current_strategy['winner_type']}，同路径鲁棒候选可作为更稳健备选。",
        "suggested_display_name": suggested["display_name"],
    }


def today_advice(account_id: int) -> dict:
    binding = get_binding(account_id)
    tasks = get_tasks(account_id)
    open_task = next((task for task in tasks if task["status"] in ("ready", "partial")), None)
    if open_task is not None:
        return {
            "type": "正式调仓" if open_task["task_type"] == "rebalance" else "偏离修正",
            "reason": "已有待执行任务",
            "task_id": int(open_task["id"]),
        }
    executed_rebalance = next(
        (
            task
            for task in tasks
            if task["status"] == "executed"
            and task["task_type"] == "rebalance"
            and task["strategy_id"] == binding["strategy_id"]
        ),
        None,
    )
    if executed_rebalance is None:
        return {
            "type": "正式调仓",
            "reason": "账户尚未执行过首次正式建仓/调仓",
            "task_id": None,
        }
    switch = strategy_switch_suggestion(account_id)
    if switch:
        return {"type": "策略切换建议", "reason": switch["reason"], "task_id": None}

    binding = get_binding(account_id)
    payload = estimate_task(account_id, binding["strategy_id"], "drift_fix")
    total_assets = payload["current_snapshot"]["total_assets"]
    max_single_drift = max(
        [abs(float(item["target_weight"]) - float(item["current_weight"])) for item in payload["diffs"]] or [0.0]
    )
    total_drift = sum(abs(float(item["diff_amount"])) for item in payload["diffs"]) / total_assets if total_assets > 0 else 0.0
    if max_single_drift > 0.02 or total_drift > 0.05:
        return {
            "type": "偏离修正",
            "reason": f"单票偏离 {max_single_drift:.2%} / 组合总偏离 {total_drift:.2%} 超阈值",
            "task_id": None,
        }
    return {"type": "无需操作", "reason": "当前账户与目标组合偏离较小", "task_id": None}


def render_page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --bg: #f9f6f1; --ink: #0f0f0f; --muted: #6b6b6b; --rule: #0f0f0f;
      --accent: #c8392b; --green: #1a7a4a; --amber: #b06000;
      --card-bg: #f2ede5;
      --serif: 'DM Serif Display', Georgia, serif;
      --sans: 'Inter', system-ui, sans-serif;
    }}
    body {{ font-family: var(--sans); background: var(--bg); color: var(--ink); font-size: 14px; line-height: 1.6; }}
    /* ── Header / Nav ── */
    header {{ border-bottom: 1.5px solid var(--rule); padding: 0; }}
    header nav {{ max-width: 1280px; margin: 0 auto; padding: 14px 32px; display: flex; align-items: center; gap: 24px; }}
    nav a {{ color: var(--ink); text-decoration: none; font-size: 12px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; opacity: .45; transition: opacity .15s; }}
    nav a:hover {{ opacity: 1; }}
    nav a:first-child {{ font-family: var(--serif); font-size: 16px; letter-spacing: -.01em; text-transform: none; font-weight: 400; opacity: 1; }}
    nav a.active {{ opacity: 1; border-bottom: 2px solid var(--ink); padding-bottom: 2px; }}
    /* ── Main ── */
    main {{ max-width: 1280px; margin: 0 auto; padding: 32px 32px 64px; }}
    /* ── Typography ── */
    h1 {{ font-family: var(--serif); font-size: clamp(28px,4vw,44px); letter-spacing: -.02em; line-height: 1.1; margin-bottom: 16px; }}
    h2 {{ font-family: var(--serif); font-size: clamp(18px,2.5vw,26px); letter-spacing: -.01em; margin-bottom: 12px; }}
    h3 {{ font-size: 13px; font-weight: 700; letter-spacing: .06em; margin-bottom: 8px; }}
    p {{ margin-bottom: 8px; }}
    a {{ color: var(--ink); }}
    code {{ font-size: 12px; background: #ede8df; padding: 2px 6px; letter-spacing: .02em; }}
    label {{ font-size: 12px; font-weight: 600; letter-spacing: .06em; color: var(--muted); display: block; margin-bottom: 4px; }}
    /* ── Grid ── */
    .grid {{ display: grid; gap: 16px; }}
    .grid-4 {{ grid-template-columns: repeat(4, minmax(0, 1fr)); }}
    .grid-2 {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    .strategy-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 0;
      border-top: 1.5px solid var(--ink);
      border-left: 1.5px solid var(--ink);
      margin-bottom: 8px;
    }}
    /* ── Card ── */
    .card {{ background: var(--card-bg); padding: 20px; border-top: 2px solid var(--ink); margin-bottom: 16px; }}
    a.strategy-card {{
      display: block;
      min-height: 100%;
      background: var(--bg);
      color: var(--ink);
      text-decoration: none;
      padding: 18px;
      border-right: 1.5px solid var(--ink);
      border-bottom: 1.5px solid var(--ink);
      transition: background .15s, transform .15s;
    }}
    a.strategy-card:hover {{ background: var(--card-bg); transform: translateY(-1px); }}
    a.strategy-card h3 {{ color: var(--ink); margin-bottom: 8px; }}
    a.strategy-card .muted {{ color: var(--muted); }}
    /* ── Tables ── */
    table {{ width: 100%; border-collapse: collapse; }}
    th {{ font-size: 11px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); padding: 8px 12px; text-align: left; border-bottom: 1.5px solid var(--rule); background: transparent; }}
    td {{ padding: 9px 12px; border-bottom: 1px solid #e0d8cc; font-size: 13px; }}
    tr:hover td {{ background: #ede8df; }}
    /* ── Badges / pills ── */
    .muted {{ color: var(--muted); }}
    .pill {{ display: inline-block; padding: 2px 8px; font-size: 11px; font-weight: 700; letter-spacing: .06em; }}
    .danger {{ background: #f8d7da; color: #721c24; }}
    .warn   {{ background: #fff3cd; color: #856404; }}
    .ok     {{ background: #d4edda; color: #155724; }}
    /* ── Forms ── */
    select, input[type=text], input[type=number] {{
      font-family: var(--sans); font-size: 13px; padding: 8px 10px;
      border: 1.5px solid var(--ink); background: var(--bg); color: var(--ink);
      border-radius: 0; outline: none; width: 100%;
    }}
    select {{ cursor: pointer; }}
    .actions form {{ display: inline-block; margin-right: 8px; }}
    /* ── Buttons ── */
    button {{
      font-family: var(--sans); font-size: 12px; font-weight: 600; letter-spacing: .08em;
      text-transform: uppercase; background: var(--ink); color: var(--bg);
      border: 1.5px solid var(--ink); padding: 8px 16px; cursor: pointer;
      border-radius: 0; transition: background .15s, color .15s;
    }}
    button:hover {{ background: #2a2a2a; }}
    button.secondary {{ background: transparent; color: var(--ink); }}
    button.secondary:hover {{ background: var(--ink); color: var(--bg); }}
    a.button {{
      display: inline-block; font-size: 12px; font-weight: 600; letter-spacing: .08em;
      text-transform: uppercase; background: var(--ink); color: var(--bg);
      border: 1.5px solid var(--ink); padding: 8px 16px; text-decoration: none;
      transition: background .15s;
    }}
    a.button:hover {{ background: #2a2a2a; }}
    /* ── Details / summary ── */
    details summary {{ cursor: pointer; padding: 10px 0; font-weight: 600; }}
    /* ── Stat cards ── */
    .stat-label {{ font-size: 11px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); margin-bottom: 10px; }}
    .stat-num {{ font-family: var(--serif); font-size: clamp(32px,4vw,48px); line-height: 1; letter-spacing: -.02em; }}
    .stat-num.alert {{ color: var(--accent); }}
    /* ── Colored values ── */
    .pos {{ color: var(--green); font-weight: 600; }}
    .neg {{ color: var(--accent); font-weight: 600; }}
    /* ── Badges ── */
    .badge {{ display: inline-block; padding: 2px 8px; font-size: 11px; font-weight: 700; letter-spacing: .05em; }}
    .badge-red    {{ background: #f8d7da; color: #721c24; }}
    .badge-amber  {{ background: #fff3cd; color: #856404; }}
    .badge-green  {{ background: #d4edda; color: #155724; }}
    .badge-blue   {{ background: #dbeafe; color: #1e40af; }}
    .badge-muted  {{ background: #e2e3e5; color: #383d41; }}
    /* ── Metric grid ── */
    .metrics-row {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(90px,1fr)); gap: 14px; margin: 14px 0; padding: 14px 0; border-top: 1px solid #e0d8cc; border-bottom: 1px solid #e0d8cc; }}
    .m-label {{ font-size: 10px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); margin-bottom: 3px; }}
    .m-val {{ font-size: 17px; font-weight: 600; letter-spacing: -.01em; }}
    /* ── Page section ── */
    .page-section {{ margin-bottom: 36px; }}
    .section-heading {{ font-family: var(--serif); font-size: clamp(18px,2.5vw,26px); letter-spacing: -.01em; margin-bottom: 16px; padding-bottom: 10px; border-bottom: 1.5px solid var(--rule); }}
    @media (max-width: 720px) {{ .strategy-grid {{ grid-template-columns: 1fr; }} }}
    /* ── Misc ── */
    hr {{ border: none; border-top: 1px solid #e0d8cc; margin: 20px 0; }}
    ul, ol {{ padding-left: 20px; }}
    li {{ margin-bottom: 4px; font-size: 13px; }}
  </style>
</head>
<body>
  <header>
    <nav>
      <a href="/">Dashboard</a>
      <a href="/strategies"{"class='active'" if "策略" in title else ""}>策略中心</a>
      <a href="/accounts"{"class='active'" if "账户" in title else ""}>账户中心</a>
    </nav>
  </header>
  <main>{body}</main>
</body>
</html>"""


def fmt_pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def fmt_amt(value: float) -> str:
    return f"{value:,.2f}"


def render_overlay_trade_details(event: dict) -> str:
    details = event.get("trade_details") or []
    if not details:
        return "<p class='muted'>暂无逐票交易明细。</p>"
    rows = []
    for detail in details:
        side = str(detail.get("side") or "")
        side_label = {"buy": "买入", "sell": "卖出"}.get(side, side or "n/a")
        side_style = " style='color:#166534;font-weight:700'" if side == "buy" else " style='color:#b45309;font-weight:700'"
        rows.append(
            f"<tr><td>{html.escape(str(detail.get('ts_code') or ''))}</td>"
            f"<td>{html.escape(str(detail.get('name') or ''))}</td>"
            f"<td{side_style}>{html.escape(side_label)}</td>"
            f"<td>{fmt_pct(float(detail.get('current_weight') or 0.0))}</td>"
            f"<td>{fmt_pct(float(detail.get('post_trade_weight') or 0.0))}</td>"
            f"<td>{fmt_pct(float(detail.get('diff_weight') or 0.0))}</td>"
            f"<td>{fmt_pct(float(detail.get('gross_amount_pct_nav') or 0.0))}</td>"
            f"<td>{fmt_pct(float(detail.get('fee_pct_nav') or 0.0))}</td></tr>"
        )
    return (
        "<h4>逐票交易明细</h4>"
        "<table><thead><tr><th>代码</th><th>名称</th><th>方向</th><th>调仓前权重</th><th>调仓后权重</th><th>权重变化</th><th>成交额/NAV</th><th>费用/NAV</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table>"
    )


def advice_badge(advice_type: str) -> str:
    cls = {"正式调仓": "badge-red", "偏离修正": "badge-amber", "策略切换建议": "badge-blue"}.get(advice_type, "badge-muted")
    return f"<span class='badge {cls}'>{html.escape(advice_type)}</span>"


def risk_badge(risk_state: str) -> str:
    label = {"risk_on": "满仓", "caution": "减仓", "risk_off": "空仓"}.get(risk_state, risk_state)
    cls = {"risk_on": "badge-green", "caution": "badge-amber", "risk_off": "badge-red"}.get(risk_state, "badge-muted")
    return f"<span class='badge {cls}'>{html.escape(label)}</span>"


def signed_pct_html(value: float) -> str:
    cls = "pos" if value > 0.0005 else ("neg" if value < -0.0005 else "")
    sign = "+" if value > 0.0005 else ""
    return f"<span class='{cls}'>{sign}{fmt_pct(value)}</span>" if cls else fmt_pct(value)


def safe_float(value: object, default: float = 0.0) -> float:
    try:
        return float(value or default)
    except Exception:
        return default


def short_date(value: object) -> str:
    text = str(value or "").strip()
    return text[:10] if len(text) >= 10 else ""


def result_path_for(strategy_id: str, sample_tag: str, market_scope: str, filename: str) -> Path:
    base_dir = HK_RESULTS_DIR if market_scope == "hkconnect" else RESULTS_DIR
    return base_dir / f"{strategy_id}__{sample_tag}" / filename


@lru_cache(maxsize=256)
def load_strategy_trade_events(strategy_id: str, sample_tag: str, market_scope: str) -> tuple[dict, ...]:
    path = result_path_for(strategy_id, sample_tag, market_scope, "turnover.csv")
    if not path.exists():
        return tuple()
    events: list[dict] = []
    try:
        with path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                details: list[dict] = []
                raw_details = str(row.get("trade_details_json") or "").strip()
                if raw_details:
                    try:
                        parsed = json.loads(raw_details)
                    except Exception:
                        parsed = []
                    if isinstance(parsed, list):
                        details = [item for item in parsed if isinstance(item, dict)]
                buy_amount = safe_float(row.get("buy_amount"))
                sell_amount = safe_float(row.get("sell_amount"))
                has_trade = bool(details) or buy_amount > 1e-12 or sell_amount > 1e-12
                if not has_trade:
                    continue
                events.append(
                    {
                        "date": short_date(row.get("date")),
                        "signal_date": short_date(row.get("signal_date")),
                        "trade_date": short_date(row.get("trade_date")),
                        "event_type": str(row.get("event_type") or ""),
                        "buy_amount": buy_amount,
                        "sell_amount": sell_amount,
                        "has_trade_details": bool(details),
                        "trade_details": details,
                    }
                )
    except Exception:
        return tuple()
    return tuple(events)


def trade_event_in_range(event: dict, previous_date: str, current_date: str) -> bool:
    dates = [short_date(event.get(key)) for key in ("trade_date", "date", "signal_date")]
    return any(previous_date < date <= current_date for date in dates if date)


def collect_trade_attribution(trade_events: list[dict], previous_date: str, current_date: str) -> tuple[dict[str, dict], bool]:
    trade_map: dict[str, dict] = {}
    missing_trade_details = False
    for event in trade_events:
        if not trade_event_in_range(event, previous_date, current_date):
            continue
        details = event.get("trade_details") or []
        has_aggregate_trade = safe_float(event.get("buy_amount")) > 1e-12 or safe_float(event.get("sell_amount")) > 1e-12
        if has_aggregate_trade and not details:
            missing_trade_details = True
            continue
        for detail in details:
            code = str(detail.get("ts_code") or "")
            if not code:
                continue
            side = str(detail.get("side") or "")
            delta = safe_float(detail.get("diff_weight"))
            if abs(delta) <= 1e-12:
                gross_weight = safe_float(detail.get("gross_amount_pct_nav"))
                delta = gross_weight if side == "buy" else (-gross_weight if side == "sell" else 0.0)
            entry = trade_map.setdefault(
                code,
                {
                    "trade_weight": 0.0,
                    "trade_abs_weight": 0.0,
                    "buy_weight": 0.0,
                    "sell_weight": 0.0,
                    "event_count": 0,
                },
            )
            entry["trade_weight"] += delta
            entry["trade_abs_weight"] += abs(delta)
            entry["buy_weight"] += max(0.0, delta)
            entry["sell_weight"] += max(0.0, -delta)
            entry["event_count"] += 1
    return trade_map, missing_trade_details


def flatten_history_snapshots(history_windows: list[dict]) -> list[dict]:
    snapshots: list[dict] = []
    seen_dates: set[str] = set()
    for window in history_windows:
        for snapshot in window.get("snapshots", []):
            date = str(snapshot.get("date", ""))
            event_type = str(snapshot.get("event_type") or "holding_snapshot")
            history_key = f"{date}:{event_type}"
            if not date or history_key in seen_dates:
                continue
            seen_dates.add(history_key)
            snapshots.append(snapshot)
    snapshots.sort(key=lambda item: str(item.get("date", "")), reverse=True)
    return snapshots


def build_history_selection(history_windows: list[dict], history_window_key: str) -> tuple[str, dict | None]:
    if not history_windows:
        return "0", None
    all_snapshots = flatten_history_snapshots(history_windows)
    if history_window_key == "all":
        return "all", {
            "window_index": "all",
            "label": "全部历史",
            "start_date": all_snapshots[-1]["date"] if all_snapshots else "",
            "end_date": all_snapshots[0]["date"] if all_snapshots else "",
            "snapshot_count": len(all_snapshots),
            "snapshots": all_snapshots,
        }
    try:
        history_window_index = int(history_window_key)
    except Exception:
        history_window_index = 0
    history_window_index = max(0, min(history_window_index, len(history_windows) - 1))
    return str(history_window_index), history_windows[history_window_index]


def build_rebalance_change_rows(latest_weights: list[dict], history_windows: list[dict], trade_events: list[dict] | None = None) -> dict | None:
    snapshots = [snapshot for snapshot in flatten_history_snapshots(history_windows) if snapshot.get("holdings")]
    if len(snapshots) < 2:
        return None
    current_snapshot = snapshots[0]
    previous_snapshot = snapshots[1]
    current_date = str(current_snapshot.get("date", ""))
    previous_date = str(previous_snapshot.get("date", ""))
    trade_map, missing_trade_details = collect_trade_attribution(trade_events or [], previous_date, current_date)
    latest_price_map = {
        str(row.get("ts_code")): row.get("latest_price")
        for row in latest_weights or []
        if row.get("ts_code")
    }
    current_map = {
        str(row.get("ts_code")): {
            "ts_code": str(row.get("ts_code")),
            "name": str(row.get("name", "")),
            "weight": float(row.get("weight", 0.0)),
            "latest_price": latest_price_map.get(str(row.get("ts_code"))),
        }
        for row in current_snapshot.get("holdings", [])
        if row.get("ts_code")
    }
    previous_map = {
        str(row.get("ts_code")): {
            "ts_code": str(row.get("ts_code")),
            "name": str(row.get("name", "")),
            "weight": float(row.get("weight", 0.0)),
        }
        for row in previous_snapshot.get("holdings", [])
        if row.get("ts_code")
    }
    all_codes = sorted(set(current_map.keys()) | set(previous_map.keys()))
    rows: list[dict] = []
    summary = {"新增": 0, "加仓": 0, "减仓": 0, "清仓": 0}
    source_summary = {"真实交易": 0, "交易+漂移": 0, "市值漂移": 0, "明细不全": 0, "现金余额": 0}
    for code in all_codes:
        current = current_map.get(code, {"ts_code": code, "name": "", "weight": 0.0, "latest_price": None})
        previous = previous_map.get(code, {"ts_code": code, "name": "", "weight": 0.0})
        current_weight = float(current.get("weight", 0.0))
        previous_weight = float(previous.get("weight", 0.0))
        diff = current_weight - previous_weight
        if abs(diff) < 1e-9:
            continue
        if previous_weight <= 1e-9 and current_weight > 1e-9:
            action = "新增"
        elif current_weight <= 1e-9 and previous_weight > 1e-9:
            action = "清仓"
        elif diff > 0:
            action = "加仓"
        else:
            action = "减仓"
        summary[action] += 1
        if code == "CASH":
            trade_weight = None
            drift_weight = None
            source_type = "cash"
            source_label = "现金余额"
            source_summary["现金余额"] += 1
        else:
            trade_info = trade_map.get(code, {})
            trade_abs_weight = float(trade_info.get("trade_abs_weight", 0.0))
            has_trade_detail = trade_abs_weight > 5e-4
            if has_trade_detail:
                trade_weight = float(trade_info.get("trade_weight", 0.0))
                drift_weight = diff - trade_weight
            elif missing_trade_details:
                trade_weight = None
                drift_weight = None
            else:
                trade_weight = 0.0
                drift_weight = diff
            if has_trade_detail:
                if drift_weight is not None and abs(drift_weight) > max(0.002, trade_abs_weight * 0.25):
                    source_type = "mixed"
                    source_label = "交易+漂移"
                    source_summary["交易+漂移"] += 1
                else:
                    source_type = "trade"
                    source_label = "真实交易"
                    source_summary["真实交易"] += 1
            elif missing_trade_details and action not in {"新增", "清仓"}:
                source_type = "missing"
                source_label = "明细不全"
                source_summary["明细不全"] += 1
            elif missing_trade_details:
                source_type = "trade"
                source_label = "真实交易"
                source_summary["真实交易"] += 1
            else:
                source_type = "drift"
                source_label = "市值漂移"
                source_summary["市值漂移"] += 1
        rows.append(
            {
                "ts_code": code,
                "name": str(current.get("name") or previous.get("name") or ""),
                "current_weight": current_weight,
                "previous_weight": previous_weight,
                "diff_weight": diff,
                "trade_weight": trade_weight,
                "drift_weight": drift_weight,
                "source_type": source_type,
                "source_label": source_label,
                "action": action,
                "latest_price": current.get("latest_price"),
            }
        )
    action_order = {"新增": 0, "加仓": 1, "减仓": 2, "清仓": 3}
    rows.sort(key=lambda item: (action_order.get(str(item["action"]), 9), -abs(float(item["diff_weight"])), str(item["ts_code"])))
    return {
        "current_date": current_date,
        "previous_date": previous_date,
        "rows": rows,
        "summary": summary,
        "source_summary": source_summary,
        "trade_detail_complete": not missing_trade_details,
    }


def render_exposure_return_curve(snapshots: list[dict], equity_curve_points: list[dict], start_date: str = "", end_date: str = "") -> str:
    snapshots = [snapshot for snapshot in snapshots if snapshot.get("holdings")]
    if not snapshots:
        return "<div class='muted'>暂无仓位与收益率曲线。</div>"
    ordered = sorted(snapshots, key=lambda item: str(item.get("date", "")))
    dates: list[str] = []
    exposures: list[float] = []
    for snapshot in ordered:
        cash_weight = 0.0
        for row in snapshot.get("holdings", []):
            if str(row.get("ts_code")) == "CASH":
                cash_weight = float(row.get("weight", 0.0))
                break
        dates.append(str(snapshot.get("date", "")))
        exposures.append(max(0.0, min(1.0, 1.0 - cash_weight)))
    curve_points = equity_curve_points or []
    if start_date and end_date:
        curve_points = [point for point in curve_points if start_date <= str(point.get("date", "")) <= end_date]
    curve_map = {str(point.get("date", "")): float(point.get("nav", 1.0)) - 1.0 for point in curve_points}
    returns = [curve_map.get(date, 0.0) for date in dates]
    width = 980
    height = 260
    pad_left = 48
    pad_right = 48
    pad_top = 20
    pad_bottom = 32
    plot_width = width - pad_left - pad_right
    plot_height = height - pad_top - pad_bottom
    if len(exposures) == 1:
        x_positions = [pad_left + plot_width / 2]
    else:
        x_positions = [pad_left + plot_width * i / (len(exposures) - 1) for i in range(len(exposures))]
    exposure_points = []
    for x, exposure in zip(x_positions, exposures):
        y = pad_top + (1.0 - exposure) * plot_height
        exposure_points.append(f"{x:.1f},{y:.1f}")
    min_return = min(returns) if returns else 0.0
    max_return = max(returns) if returns else 0.0
    if abs(max_return - min_return) < 1e-9:
        min_return = min(min_return, 0.0)
        max_return = max(max_return, 0.01)
    return_points = []
    for x, ret in zip(x_positions, returns):
        normalized = (ret - min_return) / (max_return - min_return)
        y = pad_top + (1.0 - normalized) * plot_height
        return_points.append(f"{x:.1f},{y:.1f}")
    grid_lines = []
    left_labels = []
    for pct in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = pad_top + (1.0 - pct) * plot_height
        grid_lines.append(
            f"<line x1='{pad_left}' y1='{y:.1f}' x2='{width - pad_right}' y2='{y:.1f}' stroke='#e5e7eb' stroke-width='1' />"
        )
        left_labels.append(f"<text x='8' y='{y + 4:.1f}' fill='#64748b' font-size='12'>{pct * 100:.0f}%</text>")
    right_labels = []
    for pct in (0.0, 0.25, 0.5, 0.75, 1.0):
        y = pad_top + (1.0 - pct) * plot_height
        value = min_return + (max_return - min_return) * pct
        right_labels.append(
            f"<text x='{width - pad_right + 6}' y='{y + 4:.1f}' fill='#64748b' font-size='12'>{value * 100:.1f}%</text>"
        )
    tick_labels = []
    for idx in sorted({0, len(dates) // 2, len(dates) - 1}):
        x = x_positions[idx]
        tick_labels.append(
            f"<text x='{x:.1f}' y='{height - 8}' text-anchor='middle' fill='#64748b' font-size='12'>{html.escape(dates[idx])}</text>"
        )
    latest_exposure = exposures[-1]
    latest_return = returns[-1] if returns else 0.0
    summary = f"最新总仓位 {fmt_pct(latest_exposure)}，区间收益率 {fmt_pct(latest_return)}，共 {len(exposures)} 个调仓快照。"
    return (
        "<div class='card' style='margin-top:16px'>"
        "<h2>总仓位 + 收益率曲线</h2>"
        f"<p class='muted'>{summary}</p>"
        "<p class='muted'>蓝线为总仓位，绿线为累计收益率（相对样本起点）。</p>"
        f"<svg viewBox='0 0 {width} {height}' width='100%' height='{height}' role='img' aria-label='总仓位与收益率曲线'>"
        + "".join(grid_lines)
        + "".join(left_labels)
        + "".join(right_labels)
        + f"<polyline fill='none' stroke='#2563eb' stroke-width='3' points='{' '.join(exposure_points)}' />"
        + f"<polyline fill='none' stroke='#16a34a' stroke-width='3' points='{' '.join(return_points)}' />"
        + "".join(
            f"<circle cx='{x:.1f}' cy='{pad_top + (1.0 - exposure) * plot_height:.1f}' r='3.5' fill='#1d4ed8' />"
            for x, exposure in zip(x_positions, exposures)
        )
        + "".join(
            f"<circle cx='{x:.1f}' cy='{pad_top + (1.0 - ((ret - min_return) / (max_return - min_return))) * plot_height:.1f}' r='3.5' fill='#15803d' />"
            for x, ret in zip(x_positions, returns)
        )
        + "".join(tick_labels)
        + "</svg></div>"
    )


def task_type_label(task_type: str) -> str:
    return {
        "rebalance": "正式调仓",
        "drift_fix": "偏离修正",
    }.get(task_type, task_type)


def task_status_label(status: str) -> str:
    return {
        "ready": "待执行",
        "partial": "部分成交",
        "executed": "已执行",
        "cancelled": "已忽略",
    }.get(status, status)


def trade_note_label(note: str) -> str:
    normalized = (note or "").strip()
    return {
        "manual_snapshot_sync": "手工持仓同步",
        "manual_entry": "手工新增交易",
        "manual_entry_edit": "手工编辑交易",
        "actual_execution": "实际成交",
        "estimated_execution": "估算执行",
    }.get(normalized, normalized or "-")


def dashboard_html() -> str:
    accounts = get_accounts()
    advice_items = []
    for account in accounts:
        advice = today_advice(int(account["id"]))
        advice_items.append((account, advice))
    open_rebalances = sum(1 for _, advice in advice_items if advice["type"] == "正式调仓")
    open_drift = sum(1 for _, advice in advice_items if advice["type"] == "偏离修正")
    switch_count = sum(1 for _, advice in advice_items if advice["type"] == "策略切换建议")
    updated_at = load_registry()["as_of"]

    alert_cls = lambda n: " alert" if n > 0 else ""
    cards = f"""
    <div class="grid grid-4" style="margin-bottom:32px">
      <div class="card">
        <div class="stat-label">今日正式调仓</div>
        <div class="stat-num{alert_cls(open_rebalances)}">{open_rebalances}</div>
      </div>
      <div class="card">
        <div class="stat-label">今日偏离修正</div>
        <div class="stat-num{alert_cls(open_drift)}">{open_drift}</div>
      </div>
      <div class="card">
        <div class="stat-label">策略切换建议</div>
        <div class="stat-num{alert_cls(switch_count)}">{switch_count}</div>
      </div>
      <div class="card">
        <div class="stat-label">研究数据截止</div>
        <div class="stat-num" style="font-size:clamp(20px,2.5vw,28px)">{html.escape(updated_at)}</div>
      </div>
    </div>
    """

    rows = []
    for account, advice in advice_items:
        binding = get_binding(int(account["id"]))
        strategy = load_strategy_snapshot(binding["strategy_id"])
        current = current_positions_snapshot(int(account["id"]))
        target_exposure = float(strategy["target_total_exposure"])
        current_exposure = (current["market_value"] / current["total_assets"]) if current["total_assets"] > 0 else 0.0
        drift = abs(current_exposure - target_exposure)
        initial_capital = float(account["initial_capital"] or 0.0)
        total_pnl = float(current["total_assets"]) - initial_capital
        total_pnl_pct = (total_pnl / initial_capital) if initial_capital > 0 else 0.0
        rows.append(
            f"<tr>"
            f"<td><a href='/accounts/{account['id']}'>{html.escape(account['name'])}</a></td>"
            f"<td class='muted' style='font-size:12px'>{html.escape(strategy['display_name'][:40])}{'…' if len(strategy['display_name'])>40 else ''}</td>"
            f"<td>{advice_badge(advice['type'])}</td>"
            f"<td>{risk_badge(strategy['risk_state'])}</td>"
            f"<td>{fmt_pct(drift)}</td>"
            f"<td style='font-weight:600'>{fmt_amt(float(current['total_assets']))}</td>"
            f"<td>{signed_pct_html(total_pnl_pct)}</td>"
            f"</tr>"
        )
    accounts_table = (
        "<div class='page-section'>"
        "<div class='section-heading'>账户概览</div>"
        "<table><thead><tr><th>账户</th><th>当前策略</th><th>今日建议</th><th>风险状态</th><th>偏离度</th><th>总资产</th><th>总盈亏率</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>"
    )

    per_account_task_cards = []
    for account in accounts:
        task_rows = []
        for task in get_tasks(int(account["id"]))[:5]:
            status_cls = {"已执行": "badge-green", "待执行": "badge-amber", "部分成交": "badge-blue", "已忽略": "badge-muted"}.get(task_status_label(str(task["status"])), "badge-muted")
            task_rows.append(
                f"<tr>"
                f"<td><a href='/tasks/{task['id']}'>#{task['id']}</a></td>"
                f"<td>{html.escape(task_type_label(str(task['task_type'])))}</td>"
                f"<td><span class='badge {status_cls}'>{html.escape(task_status_label(str(task['status'])))}</span></td>"
                f"<td class='muted'>{html.escape(task['created_at'])}</td>"
                f"</tr>"
            )
        if not task_rows:
            task_rows.append("<tr><td colspan='4' class='muted'>暂无任务</td></tr>")
        per_account_task_cards.append(
            "<div class='card'>"
            f"<h2 style='margin-bottom:12px'>{html.escape(account['name'])}</h2>"
            "<table><thead><tr><th>任务</th><th>类型</th><th>状态</th><th>创建时间</th></tr></thead><tbody>"
            + "".join(task_rows)
            + "</tbody></table></div>"
        )
    tasks_section = (
        "<div class='page-section'>"
        "<div class='section-heading'>近期任务</div>"
        "<div class='grid grid-2'>" + "".join(per_account_task_cards) + "</div>"
        "</div>"
    )

    return render_page("Dashboard", f"<h1>实盘平台</h1>{cards}{accounts_table}{tasks_section}")


def strategies_html() -> str:
    payload = load_registry()
    registry = payload["strategies"]
    core_active_registry = payload.get("core_active_strategies", [])
    groups = {"a_share": [], "hkconnect": []}
    for item in registry:
        groups.setdefault(str(item.get("market_scope", "a_share")), []).append(item)

    def strategy_card(item: dict, extra_note: str = "") -> str:
        metrics = item["summary_metrics"]
        winner_tags = item.get("winner_tags") or []
        is_robust = any(str(t).split(":")[-1] == "robust candidate" for t in winner_tags)
        windows_text = winner_windows_label(winner_tags)
        data_as_of = str(item.get("data_as_of") or item.get("updated_at") or "")
        signal_effective_date = str(item.get("signal_effective_date") or item.get("updated_at") or "")
        href = f"/strategies/{quote(str(item['strategy_id']))}"
        tags_html = ""
        if windows_text:
            robust_suffix = " / 鲁棒" if is_robust else ""
            tags_html += f"<span class='badge badge-blue' style='margin-right:4px'>窗口 {html.escape(windows_text)}{robust_suffix}</span>"
        elif is_robust:
            tags_html += "<span class='badge badge-blue' style='margin-right:4px'>鲁棒</span>"
        tags_html += risk_badge(item["risk_state"])
        return (
            f"<a class='strategy-card' href='{html.escape(href)}' aria-label='查看策略 {html.escape(item['display_name'])}'>"
            f"<div style='margin-bottom:8px'>{tags_html}</div>"
            f"<h3>{html.escape(item['display_name'])}</h3>"
            + (f"<p class='muted' style='font-size:12px;margin:4px 0 0'>{html.escape(extra_note)}</p>" if extra_note else "")
            + f"<div class='metrics-row'>"
            f"<div><div class='m-label'>CAGR</div><div class='m-val pos'>{fmt_pct(float(metrics.get('cagr',0)))}</div></div>"
            f"<div><div class='m-label'>Sharpe</div><div class='m-val'>{float(metrics.get('sharpe_ratio',0)):.2f}</div></div>"
            f"<div><div class='m-label'>Max DD</div><div class='m-val neg'>{fmt_pct(float(metrics.get('max_drawdown',0)))}</div></div>"
            f"<div><div class='m-label'>总收益</div><div class='m-val'>{fmt_pct(float(metrics.get('total_return',0)))}</div></div>"
            f"<div><div class='m-label'>换手率</div><div class='m-val'>{float(metrics.get('average_annual_turnover',0)):.2f}</div></div>"
            f"<div><div class='m-label'>仓位</div><div class='m-val'>{fmt_pct(float(item['target_total_exposure']))}</div></div>"
            f"</div>"
            f"<div class='muted' style='font-size:11px'>{html.escape(adjustment_style_label(item))} · 数据截止 {html.escape(data_as_of)} · 换股/信号 {html.escape(signal_effective_date)}</div>"
            "</a>"
        )

    sections = []
    for scope in ("a_share", "hkconnect"):
        items = groups.get(scope, [])
        if not items:
            continue
        # A股: split by path
        if scope == "a_share":
            path_groups: dict[str, list] = {}
            for item in items:
                path_groups.setdefault(item["path"], []).append(item)
            path_html = ""
            path_labels = {
                "path1": "Path 1 · 稳健路线",
                "path2": "Path 2 · 高收益探索",
                "path3": "Path 3 · 周度高频",
            }
            for path_key in ("path1", "path2", "path3"):
                path_items = path_groups.get(path_key, [])
                if not path_items:
                    continue
                path_label = path_labels[path_key]
                path_html += (
                    f"<div style='font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:20px 0 10px'>{html.escape(path_label)}</div>"
                    f"<div class='strategy-grid'>{''.join(strategy_card(it) for it in path_items)}</div>"
                )
            section_html = (
                "<div class='page-section'>"
                "<div class='section-heading'>A 股策略</div>"
                + path_html + "</div>"
            )
        else:
            section_html = (
                "<div class='page-section'>"
                "<div class='section-heading'>沪港通策略</div>"
                f"<div class='strategy-grid'>{''.join(strategy_card(it) for it in items)}</div>"
                "</div>"
            )
        sections.append(section_html)

    if core_active_registry:
        core_html = "".join(strategy_card(it, extra_note="观察区：当前不在 tracked winners 白名单内") for it in core_active_registry)
        sections.append(
            "<div class='page-section'>"
            "<div class='section-heading'>A股 Core Active 观察区</div>"
            "<p class='muted' style='margin-bottom:16px;font-size:13px'>winner 之外最值得持续观察的核心活跃候选，仅供比较查看，不进入账户绑定白名单。</p>"
            f"<div class='strategy-grid'>{core_html}</div></div>"
        )

    chart_specs = [
        ("2017窗口", "/docs/strategy_family_since_2017_01.png"),
        ("2020窗口", "/docs/strategy_family_since_2020_01.png"),
        ("2023窗口", "/docs/strategy_family_since_2023_01.png"),
        ("2025窗口", "/docs/strategy_family_since_2025_01.png"),
    ]
    chart_cards = "".join(
        f"<div class='card'><h3 style='margin-bottom:8px'>{html.escape(lbl)}</h3>"
        f"<img src='{html.escape(url)}' alt='{html.escape(lbl)}' style='width:100%;border:1px solid #e0d8cc' /></div>"
        for lbl, url in chart_specs
    )
    sections.append(
        "<div class='page-section'>"
        "<div class='section-heading'>Core Family 对比图</div>"
        f"<div class='grid grid-2'>{chart_cards}</div></div>"
    )

    return render_page("策略中心", "<h1>策略中心</h1>" + "".join(sections))


def strategy_detail_html(strategy_id: str, history_window_key: str = "all", sample_view_tag: str = "") -> str:
    item = load_strategy_snapshot(strategy_id)
    windows = item["windows"]
    sample_views = item.get("sample_views") or {}
    selected_sample_tag = sample_view_tag or str(item.get("sample_tag") or "since_2020_01")
    if selected_sample_tag not in sample_views and sample_views:
        selected_sample_tag = str(item.get("sample_tag") or next(iter(sample_views.keys())))
    active_view = sample_views.get(selected_sample_tag) or {
        "updated_at": item.get("updated_at"),
        "rebalance_frequency": item.get("rebalance_frequency"),
        "summary_metrics": item.get("summary_metrics"),
        "target_total_exposure": item.get("target_total_exposure"),
        "risk_state": item.get("risk_state"),
        "latest_weights": item.get("latest_weights"),
        "history_windows": item.get("history_windows"),
        "trade_events": item.get("trade_events"),
        "equity_curve_points": item.get("equity_curve_points"),
        "summary_meta": item.get("summary_meta"),
        "sample_tag": selected_sample_tag,
        "sample_tag_label": selected_sample_tag,
    }
    rebalance_frequency = rebalance_frequency_label(str(active_view.get("rebalance_frequency", item.get("rebalance_frequency", "monthly"))))
    adjustment_style = adjustment_style_label(item)
    active_meta = active_view.get("summary_meta") or {}
    active_sample_label = str(active_meta.get("sample_label") or active_view.get("sample_tag_label") or selected_sample_tag)
    active_sample_start = str(active_meta.get("sample_start") or "")
    active_sample_end = str(active_meta.get("sample_end") or active_view.get("updated_at") or "")
    formal_schedule = active_view.get("formal_schedule") or item.get("formal_schedule") or {}
    data_as_of = str(formal_schedule.get("data_as_of") or active_sample_end or "")
    suggestion_effective_date = str(formal_schedule.get("suggestion_effective_date") or "")
    basket_effective_date = str(formal_schedule.get("basket_effective_date") or "")
    exposure_effective_date = str(formal_schedule.get("exposure_effective_date") or "")
    schedule_kind = str(formal_schedule.get("schedule_kind") or "")
    split_view = active_view.get("split_view") or {}

    sample_options = []
    for key in ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"):
        view = sample_views.get(key)
        if not view:
            continue
        selected = " selected" if key == selected_sample_tag else ""
        label = html.escape(str(view.get("sample_tag_label") or key))
        meta = view.get("summary_meta") or {}
        range_text = f"{meta.get('sample_start', '')} → {meta.get('sample_end', '')}"
        sample_options.append(f"<option value='{html.escape(key)}'{selected}>{label}（{html.escape(range_text)}）</option>")
    sample_selector = ""
    if sample_options:
        sample_selector = (
            f"<form method='get' action='/strategies/{quote(strategy_id)}' style='margin:12px 0 16px 0'>"
            "<label>实际回测窗口</label>"
            f"<select name='sample_view' style='display:block;margin-top:8px;padding:8px 10px;min-width:320px'>{''.join(sample_options)}</select>"
            f"<input type='hidden' name='history_window' value='{html.escape(history_window_key or 'all')}' />"
            "<div style='margin-top:10px'><button>切换窗口</button></div>"
            "</form>"
        )
    rows = []
    for key in ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"):
        if key not in windows:
            continue
        w = windows[key]
        row_style = " style='background:#eff6ff;font-weight:600'" if key == selected_sample_tag else ""
        rows.append(
            f"<tr{row_style}><td>{html.escape(key)}</td><td>{fmt_pct(float(w['total_return']))}</td><td>{fmt_pct(float(w['cagr']))}</td><td>{fmt_pct(float(w['max_drawdown']))}</td><td>{float(w['sharpe']):.4f}</td><td>{float(w['turnover']):.2f}</td></tr>"
        )
    history_windows = active_view.get("history_windows") or []
    trade_events = active_view.get("trade_events") or list(
        load_strategy_trade_events(strategy_id, selected_sample_tag, str(item.get("market_scope") or "a_share"))
    )
    rebalance_change = build_rebalance_change_rows(active_view.get("latest_weights") or [], history_windows, trade_events)
    change_summary_html = ""
    change_rows_html = ""
    if rebalance_change:
        summary = rebalance_change["summary"]
        source_summary = rebalance_change.get("source_summary") or {}
        summary_parts = []
        for key in ("新增", "加仓", "减仓", "清仓"):
            count = int(summary.get(key, 0))
            if count:
                summary_parts.append(f"{key} {count} 只")
        summary_text = " | ".join(summary_parts) if summary_parts else "本次相对上次调仓没有权重变化。"
        source_parts = []
        for key in ("真实交易", "交易+漂移", "市值漂移", "现金余额", "明细不全"):
            count = int(source_summary.get(key, 0))
            if count:
                source_parts.append(f"{key} {count} 只")
        source_text = " | ".join(source_parts)
        detail_note = (
            "逐票交易明细完整，已拆分真实交易与市值漂移。"
            if rebalance_change.get("trade_detail_complete")
            else "这段历史存在缺少逐票交易明细的调仓记录；新增/清仓可确认是真实换入/换出，其余加减仓暂不能拆分。"
        )
        change_summary_html = (
            "<div class='card' style='margin-top:16px'><h2>相对上次调仓的变化</h2>"
            f"<p class='muted'>当前调仓日：{html.escape(rebalance_change['current_date'])} | 上次调仓日：{html.escape(rebalance_change['previous_date'])}</p>"
            f"<p>{summary_text}</p>"
            f"<p class='muted'>{html.escape(source_text + '。' if source_text else '')}{html.escape(detail_note)}</p>"
            "</div>"
        )
        change_rows = []
        for row in rebalance_change["rows"]:
            diff_weight = float(row["diff_weight"])
            abs_diff = abs(diff_weight)
            row_style = ""
            if abs_diff >= 0.10:
                row_style = " style='background:#dbeafe;font-weight:700'"
            elif abs_diff >= 0.05:
                row_style = " style='background:#eff6ff;font-weight:600'"
            elif row["action"] in {"新增", "清仓"}:
                row_style = " style='background:#f8fafc'"
            action_style = ""
            if row["action"] in {"新增", "加仓"}:
                action_style = " style='color:#166534;font-weight:700'"
            elif row["action"] in {"减仓", "清仓"}:
                action_style = " style='color:#b45309;font-weight:700'"
            source_cls = {
                "trade": "badge-green",
                "mixed": "badge-blue",
                "drift": "badge-muted",
                "missing": "badge-amber",
                "cash": "badge-muted",
            }.get(str(row.get("source_type") or ""), "badge-muted")
            source_html = f"<span class='badge {source_cls}'>{html.escape(str(row.get('source_label') or 'n/a'))}</span>"
            trade_weight = row.get("trade_weight")
            drift_weight = row.get("drift_weight")
            trade_text = signed_pct_html(float(trade_weight)) if trade_weight is not None else "<span class='muted'>n/a</span>"
            drift_text = signed_pct_html(float(drift_weight)) if drift_weight is not None else "<span class='muted'>n/a</span>"
            change_rows.append(
                f"<tr{row_style}><td>{html.escape(row['ts_code'])}</td><td>{html.escape(row['name'])}</td><td{action_style}>{html.escape(row['action'])}</td><td>{source_html}</td><td>{fmt_pct(float(row['previous_weight']))}</td><td>{fmt_pct(float(row['current_weight']))}</td><td>{signed_pct_html(diff_weight)}</td><td>{trade_text}</td><td>{drift_text}</td><td>{fmt_amt(float(row['latest_price'] or 0.0)) if row['latest_price'] is not None else 'n/a'}</td></tr>"
            )
        change_rows_html = (
            "<div class='card' style='margin-top:16px'><h2>最新调仓建议变化明细</h2>"
            "<p class='muted'>总变化来自最近两次权重快照；真实交易来自逐票交易明细；市值漂移=总变化-真实交易。变化≥10% 的行会重点高亮，变化≥5% 的行会浅色高亮。</p>"
            "<table><thead><tr><th>代码</th><th>名称</th><th>动作</th><th>归因</th><th>上次权重</th><th>当前权重</th><th>总变化</th><th>真实交易</th><th>市值漂移</th><th>最新价格</th></tr></thead><tbody>"
            + "".join(change_rows)
            + "</tbody></table></div>"
        )
    split_latest_html = ""
    if str(split_view.get("mode") or "") == "satellite_weekly_overlay":
        basket_rows = []
        for row in split_view.get("basket_weights") or []:
            basket_rows.append(
                f"<tr><td>{html.escape(row['ts_code'])}</td><td>{html.escape(row['name'])}</td><td>{fmt_pct(float(row['weight']))}</td><td>{fmt_amt(float(row['latest_price'] or 0.0)) if row['latest_price'] is not None else 'n/a'}</td></tr>"
            )
        overlay_summary = split_view.get("overlay_summary") or {}
        market_momentum = overlay_summary.get("market_12_1_momentum")
        overlay_history_rows = []
        for row in split_view.get("overlay_history") or []:
            is_trade = bool(row.get("is_trade"))
            trade_label = "实际调仓" if is_trade else "仅评估"
            trade_style = " style='color:#166534;font-weight:700'" if is_trade else " class='muted'"
            signal_date = str(row.get("signal_date") or row.get("date") or "")
            trade_date = str(row.get("trade_date") or row.get("date") or "")
            overlay_history_rows.append(
                f"<tr><td>{html.escape(signal_date)}</td>"
                f"<td>{html.escape(trade_date)}</td>"
                f"<td>{html.escape(str(row.get('risk_stage') or 'n/a'))}</td>"
                f"<td>{html.escape(str(row.get('raw_risk_stage') or 'n/a'))}</td>"
                f"<td{trade_style}>{trade_label}</td>"
                f"<td>{fmt_pct(float(row.get('one_way_turnover') or 0.0))}</td>"
                f"<td>{fmt_pct(float(row.get('two_way_turnover') or 0.0))}</td>"
                f"<td>{fmt_pct(float(row.get('buy_amount_pct_nav') or 0.0))}</td>"
                f"<td>{fmt_pct(float(row.get('sell_amount_pct_nav') or 0.0))}</td>"
                f"<td>{fmt_pct(float(row.get('trading_cost_pct_nav') or 0.0))}</td></tr>"
            )
        overlay_history_html = ""
        if overlay_history_rows:
            overlay_history_html = (
                "<div class='card' style='margin-top:16px'><h2>周度卫星仓位调仓/评估历史</h2>"
                "<p class='muted'>这里来自回测 turnover 的 weekly_satellite_overlay 事件；评估日为收盘后信号日，实际交易日为下一可交易日。</p>"
                "<table><thead><tr><th>评估日</th><th>实际交易日</th><th>确认状态</th><th>原始状态</th><th>动作</th><th>单边换手</th><th>双边换手</th><th>买入/NAV</th><th>卖出/NAV</th><th>费用/NAV</th></tr></thead><tbody>"
                + "".join(overlay_history_rows)
                + "</tbody></table></div>"
            )
        split_latest_html = (
            "<div class='card' style='margin-top:16px'><h2>当前建议内容（正式拆分）</h2>"
            "<p class='muted'>这类策略拆成两层：月末股票池生效日对应真实月末确定的股票池/目标权重；周度卫星仓位状态生效日对应周频风控后当前实际卫星仓暴露。月中若只发生风控/仓位切换，不会误显示成重新换股。</p>"
            "</div>"
            + f"<div class='card' style='margin-top:16px'><h2>月末股票池</h2><p>月末股票池生效日：{html.escape(basket_effective_date or 'n/a')}</p><table><thead><tr><th>代码</th><th>名称</th><th>月末目标权重</th><th>最新价格</th></tr></thead><tbody>"
            + "".join(basket_rows)
            + "</tbody></table></div>"
            + "<div class='card' style='margin-top:16px'><h2>周度卫星仓位状态</h2>"
            + f"<p>周度卫星仓位状态评估日：{html.escape(exposure_effective_date or 'n/a')}</p>"
            + f"<p>最近一次卫星仓实际交易日：{html.escape(str(overlay_summary.get('latest_overlay_trade_date') or 'n/a'))}</p>"
            + f"<p>总仓位目标：{fmt_pct(float(overlay_summary.get('target_total_exposure') or 0.0))}</p>"
            + f"<p>核心仓位目标：{fmt_pct(float(overlay_summary.get('core_exposure_target') or 0.0))}</p>"
            + f"<p>卫星仓位目标：{fmt_pct(float(overlay_summary.get('satellite_exposure_target') or 0.0))}</p>"
            + f"<p>风险状态：{html.escape(str(overlay_summary.get('risk_state') or 'n/a'))}</p>"
            + (
                f"<p>市场12-1动量：{fmt_pct(float(market_momentum))}</p>"
                if market_momentum is not None
                else ""
            )
            + f"<p>本期周度 overlay 交易次数：{int(overlay_summary.get('weekly_overlay_trade_count') or 0)}</p>"
            + "</div>"
            + overlay_history_html
        )

    selected_key, selected_history = build_history_selection(history_windows, history_window_key)
    history_selector = ""
    history_html = "<div class='muted'>暂无历史持仓快照。</div>"
    exposure_html = "<div class='muted'>暂无仓位与收益率曲线。</div>"
    if history_windows:
        options = []
        all_selected = " selected" if selected_key == "all" else ""
        all_snapshots = flatten_history_snapshots(history_windows)
        options.append(f"<option value='all'{all_selected}>全部历史（{len(all_snapshots)} 条记录）</option>")
        for hist in history_windows:
            selected = " selected" if str(hist["window_index"]) == selected_key else ""
            options.append(
                f"<option value='{int(hist['window_index'])}'{selected}>{html.escape(str(hist['label']))}（{int(hist['snapshot_count'])} 条记录）</option>"
            )
        history_selector = (
            f"<form method='get' action='/strategies/{quote(strategy_id)}' style='margin:12px 0 16px 0'>"
            f"<label>历史调仓建议窗口（按实际调仓日展示，当前频率：{html.escape(rebalance_frequency)}；每组最近12次调仓）</label>"
            f"<select name='history_window' style='display:block;margin-top:8px;padding:8px 10px;min-width:320px'>{''.join(options)}</select>"
            f"<input type='hidden' name='sample_view' value='{html.escape(selected_sample_tag)}' />"
            "<div style='margin-top:10px'><button>切换窗口</button></div>"
            "</form>"
        )
        exposure_html = render_exposure_return_curve(
            selected_history["snapshots"],
            active_view.get("equity_curve_points") or [],
            start_date=str(selected_history.get("start_date", "")),
            end_date=str(selected_history.get("end_date", "")),
        )
        snapshot_blocks = []
        for snapshot in selected_history["snapshots"]:
            if str(snapshot.get("event_type") or "") == "weekly_satellite_overlay":
                event = snapshot.get("overlay_event") or {}
                signal_date = str(event.get("signal_date") or snapshot["date"])
                trade_date = str(event.get("trade_date") or snapshot["date"])
                snapshot_blocks.append(
                    "<div class='card' style='margin-top:12px'>"
                    f"<h3>信号日：{html.escape(signal_date)}（周度卫星仓实际调仓）</h3>"
                    f"<p class='muted'>实际交易日：{html.escape(trade_date)}</p>"
                    "<table><thead><tr><th>确认状态</th><th>原始状态</th><th>单边换手</th><th>双边换手</th><th>买入/NAV</th><th>卖出/NAV</th><th>费用/NAV</th></tr></thead><tbody>"
                    f"<tr><td>{html.escape(str(event.get('risk_stage') or 'n/a'))}</td>"
                    f"<td>{html.escape(str(event.get('raw_risk_stage') or 'n/a'))}</td>"
                    f"<td>{fmt_pct(float(event.get('one_way_turnover') or 0.0))}</td>"
                    f"<td>{fmt_pct(float(event.get('two_way_turnover') or 0.0))}</td>"
                    f"<td>{fmt_pct(float(event.get('buy_amount_pct_nav') or 0.0))}</td>"
                    f"<td>{fmt_pct(float(event.get('sell_amount_pct_nav') or 0.0))}</td>"
                    f"<td>{fmt_pct(float(event.get('trading_cost_pct_nav') or 0.0))}</td></tr>"
                    "</tbody></table>"
                    + render_overlay_trade_details(event)
                    + "</div>"
                )
                continue
            rows_html = "".join(
                f"<tr><td>{html.escape(row['ts_code'])}</td><td>{html.escape(row['name'])}</td><td>{fmt_pct(float(row['weight']))}</td></tr>"
                for row in snapshot["holdings"]
            )
            snapshot_blocks.append(
                "<div class='card' style='margin-top:12px'>"
                f"<h3>调仓日：{html.escape(snapshot['date'])}</h3>"
                "<table><thead><tr><th>代码</th><th>名称</th><th>权重</th></tr></thead><tbody>"
                + rows_html
                + "</tbody></table></div>"
            )
        history_html = (
            f"<p class='muted'>当前展示窗口：{html.escape(selected_history['label'])}。持仓快照展示目标持仓；周度卫星仓实际调仓展示换手摘要。</p>"
            + "".join(snapshot_blocks)
        )
    body = (
        f"<h1>{html.escape(item['display_name'])}</h1>"
        f"<p><code>{html.escape(strategy_id)}</code></p>"
        f"<p>市场: {html.escape(market_scope_label(str(item.get('market_scope', 'a_share'))))} | 路径: {html.escape(item['path'])} | 类型: {html.escape(item['winner_type'])} | 调仓频率: {html.escape(rebalance_frequency)} | 实际调整频率类型: {html.escape(adjustment_style)} | 当前建议仓位: {fmt_pct(float(active_view['target_total_exposure']))} | 风险状态: {html.escape(active_view['risk_state'])}</p>"
        + sample_selector
        + f"<div class='card'><h2>当前查看窗口</h2><p>{html.escape(active_sample_label)}：{html.escape(active_sample_start)} → {html.escape(active_sample_end)}</p></div>"
        + strategy_detail_explanation_html(item, active_view, schedule_kind, active_sample_label)
        + (
            "<div class='card' style='margin-top:16px'><h2>当前建议时点</h2>"
            f"<p>数据截止日：{html.escape(data_as_of or 'n/a')}</p>"
            + (
                f"<p>月末股票池生效日：{html.escape(basket_effective_date or 'n/a')}</p>"
                f"<p>周度卫星仓位状态评估日：{html.escape(exposure_effective_date or 'n/a')}</p>"
                if schedule_kind == 'satellite_weekly_overlay'
                else f"<p>当前建议生效日：{html.escape(suggestion_effective_date or 'n/a')}</p>"
            )
            + (
                f"<p>股票池生效日：{html.escape(basket_effective_date or 'n/a')}</p>"
                f"<p>仓位状态生效日：{html.escape(exposure_effective_date or 'n/a')}</p>"
                if schedule_kind == 'portfolio_weekly_overlay'
                else ""
            )
            + f"<p class='muted'>判定口径：{html.escape(schedule_kind_label(schedule_kind))}。月度策略按真实月末，周度/双周策略按实际评估点更新“当前建议”；数据截止日可继续前进，但建议日期不一定每天变化。</p>"
            "</div>"
        )
        + "<div class='card'><h2>窗口表现</h2><table><thead><tr><th>窗口</th><th>Total Return</th><th>CAGR</th><th>MaxDD</th><th>Sharpe</th><th>Turnover</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>"
        + split_latest_html
        + change_summary_html
        + change_rows_html
        + exposure_html
        + "<div class='card' style='margin-top:16px'><h2>历史调仓建议</h2>"
        + history_selector
        + history_html
        + "</div>"
    )
    return render_page("策略详情", body)


def accounts_html() -> str:
    rows = []
    registry = load_registry()["strategies"]
    for account in get_accounts():
        binding = get_binding(int(account["id"]))
        strategy = load_strategy_snapshot(binding["strategy_id"])
        advice = today_advice(int(account["id"]))
        current = current_positions_snapshot(int(account["id"]))
        drift = abs((current["market_value"] / current["total_assets"] if current["total_assets"] > 0 else 0.0) - float(strategy["target_total_exposure"]))
        rows.append(
            f"<tr><td><a href='/accounts/{account['id']}'>{html.escape(account['name'])}</a></td><td>{html.escape(account['broker'])}</td><td>{html.escape(strategy['display_name'])}</td><td>{html.escape(advice['type'])}</td><td>{fmt_pct(drift)}</td><td>{fmt_amt(float(current['total_assets']))}</td></tr>"
        )
    options = []
    for item in registry:
        options.append(
            f"<option value='{html.escape(item['strategy_id'])}'>{html.escape(market_scope_label(str(item.get('market_scope', 'a_share'))))} / {html.escape(item['path'])} / {html.escape(item['winner_type'])} / {html.escape(item['display_name'])}</option>"
        )
    return render_page(
        "账户中心",
        "<h1>账户中心</h1>"
        + "<div class='page-section'>"
        + "<div class='section-heading'>账户列表</div>"
        + "<table><thead><tr><th>账户</th><th>券商</th><th>当前策略</th><th>今日建议</th><th>偏离度</th><th>总资产</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>"
        + "<div class='page-section'>"
        + "<div class='section-heading'>新增账户</div>"
        + "<div class='card'><form method='post' action='/accounts/create'>"
        + "<div class='grid grid-2' style='gap:16px'>"
        + "<div><label>账户名称</label><input name='name'></div>"
        + "<div><label>券商</label><input name='broker' value='手工测试'></div>"
        + "<div><label>初始现金</label><input name='initial_cash' value='1000000'></div>"
        + "<div><label>策略</label><select name='strategy_id'>" + "".join(options) + "</select></div>"
        + "</div>"
        + "<div style='margin-top:12px'><label>备注</label><input name='note'></div>"
        + "<div style='margin-top:16px'><button>创建账户</button></div>"
        + "</form></div></div>",
    )


def account_detail_html(account_id: int, *, show_editor: bool = False) -> str:
    account = get_account(account_id)
    binding = get_binding(account_id)
    strategy = load_strategy_snapshot(binding["strategy_id"])
    current = current_positions_snapshot(account_id)
    advice = today_advice(account_id)
    suggestion = strategy_switch_suggestion(account_id)
    current_task = get_tasks(account_id)
    registry = load_registry()["strategies"]
    initial_capital = float(account["initial_capital"] or 0.0)
    total_pnl = float(current["total_assets"]) - initial_capital
    total_pnl_pct = (total_pnl / initial_capital) if initial_capital > 0 else 0.0
    notice = ""
    if suggestion:
        pass

    rows = []
    current_map = {row["ts_code"]: row for row in current["positions"]}
    for target in strategy["latest_weights"]:
        cur = current_map.get(target["ts_code"])
        current_weight = float(cur["weight"]) if cur else 0.0
        diff = float(target["weight"]) - current_weight
        action_label = "买入" if diff > 0.001 else ("卖出" if diff < -0.001 else "持有")
        action_cls = "pos" if action_label == "买入" else ("neg" if action_label == "卖出" else "muted")
        rows.append(
            f"<tr>"
            f"<td style='font-family:monospace;font-size:12px;color:var(--muted)'>{html.escape(target['ts_code'])}</td>"
            f"<td>{html.escape(target['name'])}</td>"
            f"<td>{fmt_pct(current_weight)}</td>"
            f"<td style='font-weight:600'>{fmt_pct(float(target['weight']))}</td>"
            f"<td>{signed_pct_html(diff)}</td>"
            f"<td><span class='{action_cls}'>{action_label}</span></td>"
            f"</tr>"
        )
    tasks_rows = []
    for task in get_tasks(account_id)[:10]:
        status_label = task_status_label(str(task["status"]))
        status_cls = {"已执行": "badge-green", "待执行": "badge-amber", "部分成交": "badge-blue", "已忽略": "badge-muted"}.get(status_label, "badge-muted")
        tasks_rows.append(
            f"<tr>"
            f"<td><a href='/tasks/{task['id']}'>#{task['id']}</a></td>"
            f"<td>{html.escape(task_type_label(str(task['task_type'])))}</td>"
            f"<td><span class='badge {status_cls}'>{html.escape(status_label)}</span></td>"
            f"<td class='muted'>{html.escape(task['created_at'])}</td>"
            f"</tr>"
        )
    if not tasks_rows:
        tasks_rows.append("<tr><td colspan='4' class='muted'>暂无任务</td></tr>")
    existing_holdings = get_holdings(account_id)
    pnl_rows = []
    for row in current["positions"]:
        pnl_cls = "pos" if float(row["unrealized_pnl"]) > 0 else ("neg" if float(row["unrealized_pnl"]) < 0 else "")
        pnl_rows.append(
            f"<tr>"
            f"<td style='font-family:monospace;font-size:12px;color:var(--muted)'>{html.escape(row['ts_code'])}</td>"
            f"<td>{html.escape(row['name'])}</td>"
            f"<td>{row['shares']:.0f}</td>"
            f"<td>{fmt_amt(row['cost_price'])}</td>"
            f"<td>{fmt_amt(row['last_price'])}</td>"
            f"<td style='font-weight:600'>{fmt_amt(row['market_value'])}</td>"
            f"<td class='{pnl_cls}'>{fmt_amt(row['unrealized_pnl'])}</td>"
            f"<td class='{pnl_cls}'>{fmt_pct(row['unrealized_pnl_pct'])}</td>"
            f"</tr>"
        )
    trade_rows = []
    for trade in get_account_trades(account_id, limit=20):
        realized_text = fmt_amt(float(trade["realized_pnl"])) if trade["realized_pnl"] is not None else "—"
        side_label = "买入" if trade["side"] == "buy" else "卖出"
        side_cls = "pos" if trade["side"] == "buy" else "neg"
        action_html = (
            f"<a class='button' style='padding:4px 8px;font-size:11px' href='/trades/{int(trade['id'])}/edit'>编辑</a>"
            if trade["task_id"] is None
            else "<span class='muted' style='font-size:11px'>任务生成</span>"
        )
        trade_rows.append(
            f"<tr>"
            f"<td class='muted'>{html.escape(trade['executed_at'])}</td>"
            f"<td style='font-family:monospace;font-size:12px'>{html.escape(trade['ts_code'])}</td>"
            f"<td>{html.escape(trade['name'])}</td>"
            f"<td><span class='{side_cls}'>{side_label}</span></td>"
            f"<td>{float(trade['shares']):.0f}</td>"
            f"<td>{fmt_amt(float(trade['price']))}</td>"
            f"<td>{fmt_amt(float(trade['gross_amount']))}</td>"
            f"<td class='muted'>{fmt_amt(float(trade['fee']))}</td>"
            f"<td>{fmt_amt(float(trade['net_cash_change']))}</td>"
            f"<td>{realized_text}</td>"
            f"<td class='muted'>{html.escape(trade_note_label(str(trade['note'] or '')))}</td>"
            f"<td>{action_html}</td>"
            f"</tr>"
        )
    if not trade_rows:
        trade_rows.append("<tr><td colspan='12' class='muted'>暂无交易流水</td></tr>")
    strategy_options = []
    for item in registry:
        selected = " selected" if item["strategy_id"] == binding["strategy_id"] else ""
        strategy_options.append(
            f"<option value='{html.escape(item['strategy_id'])}'{selected}>{html.escape(market_scope_label(str(item.get('market_scope', 'a_share'))))} / {html.escape(item['path'])} / {html.escape(item['winner_type'])} / {html.escape(item['display_name'])}</option>"
        )
    holding_editor_rows = "".join(
        f"<tr>"
        f"<td><input name='ts_code' value='{html.escape(str(row['ts_code']))}' style='width:100%;padding:6px 8px'></td>"
        f"<td><input name='holding_name' value='{html.escape(str(row['name']))}' style='width:100%;padding:6px 8px'></td>"
        f"<td><input name='holding_shares' value='{float(row['shares']):.4f}' style='width:100%;padding:6px 8px'></td>"
        f"<td><input name='holding_cost_price' value='{float(row['cost_price']):.4f}' style='width:100%;padding:6px 8px'></td>"
        f"<td><button type='button' class='secondary' onclick='removeHoldingRow(this)'>删除</button></td>"
        f"</tr>"
        for row in existing_holdings
    )
    if not holding_editor_rows:
        holding_editor_rows = (
            "<tr>"
            "<td><input name='ts_code' style='width:100%;padding:6px 8px'></td>"
            "<td><input name='holding_name' style='width:100%;padding:6px 8px'></td>"
            "<td><input name='holding_shares' style='width:100%;padding:6px 8px'></td>"
            "<td><input name='holding_cost_price' style='width:100%;padding:6px 8px'></td>"
            "<td><button type='button' class='secondary' onclick='removeHoldingRow(this)'>删除</button></td>"
            "</tr>"
        )
    holding_editor = (
        "<div style='margin-top:16px;border-top:1px solid #e5e7eb;padding-top:16px'>"
        + "<h3>手工输入 / 编辑当前持仓</h3>"
        + "<p class='muted'>逐行维护当前持仓。名称可留空，平台会按代码自动补全；当前价格由平台自动拉取。</p>"
        + f"<form method='post' action='/accounts/{account_id}/holdings/save'>"
        + f"<p>现金：<input name='cash' value='{html.escape(str(float(account['cash'])))}' style='width:160px;padding:6px 8px;'></p>"
        + "<table><thead><tr><th>股票代码</th><th>股票名称</th><th>持股数量</th><th>成本价</th><th>操作</th></tr></thead>"
        + f"<tbody id='holding-editor-body'>{holding_editor_rows}</tbody></table>"
        + "<div style='margin-top:12px'>"
        + "<button type='button' class='secondary' onclick='addHoldingRow()'>新增一行</button> "
        + "<button>保存持仓快照</button> "
        + f"<a class='button' style='background:#64748b' href='/accounts/{account_id}'>取消编辑</a></div>"
        + """
        <script>
        function addHoldingRow() {
          const body = document.getElementById('holding-editor-body');
          const row = document.createElement('tr');
          row.innerHTML = `
            <td><input name="ts_code" style="width:100%;padding:6px 8px"></td>
            <td><input name="holding_name" style="width:100%;padding:6px 8px"></td>
            <td><input name="holding_shares" style="width:100%;padding:6px 8px"></td>
            <td><input name="holding_cost_price" style="width:100%;padding:6px 8px"></td>
            <td><button type="button" class="secondary" onclick="removeHoldingRow(this)">删除</button></td>
          `;
          body.appendChild(row);
        }
        function removeHoldingRow(button) {
          const body = document.getElementById('holding-editor-body');
          if (body.children.length <= 1) {
            button.closest('tr').querySelectorAll('input').forEach(input => input.value = '');
            return;
          }
          button.closest('tr').remove();
        }
        </script>
        """
        + "</form></div>"
    ) if show_editor else (
        "<div style='margin-top:16px;border-top:1px solid #e5e7eb;padding-top:16px'>"
        + f"<a class='button' href='/accounts/{account_id}?edit=1'>手工输入 / 编辑当前持仓</a>"
        + "</div>"
    )
    pnl_cls = "pos" if total_pnl > 0 else ("neg" if total_pnl < 0 else "")
    body = (
        # ── Header ──
        "<div class='page-section' style='display:flex;justify-content:space-between;align-items:flex-start;gap:16px;flex-wrap:wrap'>"
        + "<div>"
        + f"<h1 style='margin:0 0 4px'>{html.escape(account['name'])}</h1>"
        + f"<p class='muted' style='margin:0'>{html.escape(account['broker'])} · 价格来源：{html.escape(current['price_source_label'])}</p>"
        + "</div>"
        + "<div style='display:flex;gap:8px;flex-wrap:wrap'>"
        + f"<a class='button' href='/accounts/{account_id}/switch-strategy'>切换策略</a>"
        + f"<a class='button' style='background:#b91c1c' href='/accounts/{account_id}/delete-confirm'>删除账户</a>"
        + "</div></div>"
        # ── Key metrics ──
        + "<div class='page-section'>"
        + "<div class='metrics-row'>"
        + f"<div><span class='m-label'>总资产</span><span class='m-val'>{fmt_amt(float(current['total_assets']))}</span></div>"
        + f"<div><span class='m-label'>初始本金</span><span class='m-val'>{fmt_amt(initial_capital)}</span></div>"
        + f"<div><span class='m-label'>总盈亏</span><span class='m-val {pnl_cls}'>{fmt_amt(total_pnl)}</span></div>"
        + f"<div><span class='m-label'>总盈亏率</span><span class='m-val {pnl_cls}'>{fmt_pct(total_pnl_pct)}</span></div>"
        + f"<div><span class='m-label'>现金</span><span class='m-val'>{fmt_amt(float(account['cash']))}</span></div>"
        + f"<div><span class='m-label'>股票市值</span><span class='m-val'>{fmt_amt(current['market_value'])}</span></div>"
        + "</div></div>"
        # ── Strategy binding ──
        + "<div class='page-section'>"
        + f"<p class='muted' style='margin:0 0 6px'>当前策略：<a href='/strategies/{quote(str(strategy['strategy_id']))}'>{html.escape(strategy['display_name'])}</a></p>"
        + f"<p style='margin:0'>建议仓位 <strong>{fmt_pct(float(strategy['target_total_exposure']))}</strong> &nbsp;·&nbsp; 风险状态 {risk_badge(str(strategy['risk_state']))}</p>"
        + "</div>"
        # ── Today advice ──
        + "<div class='page-section'>"
        + "<h2 class='section-heading'>今日建议</h2>"
        + "<div class='card'>"
        + f"<p style='margin:0 0 10px'>{advice_badge(str(advice['type']))} <span style='margin-left:8px'>{html.escape(advice['reason'])}</span></p>"
        + "<div class='actions'>"
        + f"<form method='post' action='/accounts/{account_id}/tasks/rebalance'><button>生成正式调仓单</button></form>"
        + f"<form method='post' action='/accounts/{account_id}/tasks/drift-fix'><button class='secondary'>生成偏离修正单</button></form>"
        + "</div></div></div>"
        # ── Strategy switch suggestion (conditional) ──
        + (
            "<div class='page-section'>"
            + "<h2 class='section-heading'>策略切换建议</h2>"
            + "<div class='card'>"
            + f"<p style='margin:0 0 6px'>建议策略：<a href='/strategies/{quote(str(suggestion['suggested_strategy_id']))}'>{html.escape(suggestion.get('suggested_display_name', suggestion['suggested_strategy_id']))}</a></p>"
            + f"<p class='muted' style='margin:0'>{html.escape(suggestion['reason'])}</p>"
            + "</div></div>"
            if suggestion else ""
        )
        # ── Holdings PnL ──
        + "<div class='page-section'>"
        + "<h2 class='section-heading'>当前持仓盈亏</h2>"
        + "<div class='card'>"
        + "<table><thead><tr><th>代码</th><th>名称</th><th>数量</th><th>成本价</th><th>当前价</th><th>当前市值</th><th>浮盈亏</th><th>收益率</th></tr></thead><tbody>"
        + "".join(pnl_rows)
        + "</tbody></table>"
        + holding_editor
        + "</div></div>"
        # ── Holdings diff ──
        + "<div class='page-section'>"
        + "<h2 class='section-heading'>当前持仓 vs 目标持仓</h2>"
        + "<div class='card'>"
        + "<table><thead><tr><th>代码</th><th>名称</th><th>当前权重</th><th>目标权重</th><th>偏离</th><th>建议动作</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div></div>"
        # ── Recent tasks ──
        + "<div class='page-section'>"
        + "<h2 class='section-heading'>最近任务</h2>"
        + "<div class='card'>"
        + "<table><thead><tr><th>任务</th><th>类型</th><th>状态</th><th>创建时间</th></tr></thead><tbody>"
        + "".join(tasks_rows)
        + "</tbody></table></div></div>"
        # ── Trade history ──
        + "<div class='page-section'>"
        + "<h2 class='section-heading'>交易流水</h2>"
        + "<div class='card'>"
        + "<table><thead><tr><th>时间</th><th>代码</th><th>名称</th><th>方向</th><th>数量</th><th>价格</th><th>成交额</th><th>费用</th><th>现金变化</th><th>已实现盈亏</th><th>备注</th><th>操作</th></tr></thead><tbody>"
        + "".join(trade_rows)
        + "</tbody></table>"
        + f"<div style='margin-top:12px'><a class='button' href='/accounts/{account_id}/trades/new'>新增手工交易</a></div>"
        + "</div></div>"
    )
    return render_page("账户详情", body)


def account_delete_confirm_html(account_id: int) -> str:
    account = get_account(account_id)
    if account is None:
        return render_page("账户不存在", "<h1>账户不存在</h1>")
    tasks = get_tasks(account_id)
    holdings = get_holdings(account_id)
    body = (
        f"<h1>删除账户确认 - {html.escape(account['name'])}</h1>"
        + "<div class='card'>"
        + "<p class='danger' style='padding:12px;border-radius:10px'>这是危险操作。删除后会一并移除该账户的当前持仓、策略绑定和全部任务记录。</p>"
        + f"<p>账户名称：<strong>{html.escape(account['name'])}</strong></p>"
        + f"<p>券商：{html.escape(account['broker'])}</p>"
        + f"<p>当前持仓条目：{len(holdings)} 条</p>"
        + f"<p>关联任务：{len(tasks)} 条</p>"
        + f"<form method='post' action='/accounts/{account_id}/delete-confirm'>"
        + "<button style='background:#b91c1c'>确认删除账户</button> "
        + f"<a class='button' style='background:#64748b' href='/accounts/{account_id}'>取消</a>"
        + "</form></div>"
    )
    return render_page("删除账户确认", body)


def account_switch_strategy_html(account_id: int, *, success: bool = False) -> str:
    account = get_account(account_id)
    if account is None:
        return render_page("账户不存在", "<h1>账户不存在</h1>")
    binding = get_binding(account_id)
    registry = load_registry()["strategies"]
    strategy_options = []
    for item in registry:
        selected = " selected" if item["strategy_id"] == binding["strategy_id"] else ""
        strategy_options.append(
            f"<option value='{html.escape(item['strategy_id'])}'{selected}>{html.escape(market_scope_label(str(item.get('market_scope', 'a_share'))))} / {html.escape(item['path'])} / {html.escape(item['winner_type'])} / {html.escape(item['display_name'])}</option>"
        )
    body = (
        f"<h1>切换策略 - {html.escape(account['name'])}</h1>"
        + (f"<div class='card ok' style='margin-bottom:16px'><strong>切换成功：</strong>账户已绑定到新策略。</div>" if success else "")
        + "<div class='card'>"
        + "<p class='muted'>这里不会自动交易，只会更新账户绑定策略。切换后账户页会进入“建议正式调仓”状态。</p>"
        + f"<form method='post' action='/accounts/{account_id}/bind-strategy'>"
        + f"<select name='strategy_id' style='width:100%;padding:8px 10px;margin-bottom:12px'>{''.join(strategy_options)}</select>"
        + "<button>确认切换策略</button> "
        + f"<a class='button' style='background:#64748b' href='/accounts/{account_id}'>返回账户详情</a>"
        + "</form></div>"
    )
    return render_page("切换策略", body)


def manual_trade_form_html(account_id: int, *, trade_id: int | None = None, error: str = "", success: bool = False) -> str:
    account = get_account(account_id)
    if account is None:
        return render_page("账户不存在", "<h1>账户不存在</h1>")
    trade = get_trade(trade_id) if trade_id is not None else None
    if trade_id is not None and trade is None:
        return render_page("交易不存在", "<h1>交易不存在</h1>")
    if trade is not None and int(trade["account_id"]) != account_id:
        return render_page("错误", "<h1>交易不属于该账户</h1>")

    side = str(trade["side"]) if trade is not None else "buy"
    ts_code = str(trade["ts_code"]) if trade is not None else ""
    name = str(trade["name"]) if trade is not None else ""
    shares = float(trade["shares"]) if trade is not None else 0.0
    price = float(trade["price"]) if trade is not None else 0.0
    note = str(trade["note"] or "") if trade is not None else ""
    title = "编辑手工交易" if trade is not None else "新增手工交易"
    action = f"/trades/{trade_id}/edit" if trade is not None else f"/accounts/{account_id}/trades/create"
    body = (
        f"<h1>{title} - {html.escape(account['name'])}</h1>"
        + (f"<div class='card ok' style='margin-bottom:16px'><strong>保存成功：</strong>交易记录已更新。</div>" if success else "")
        + (f"<div class='card danger' style='margin-bottom:16px'><strong>无法保存：</strong>{html.escape(error)}</div>" if error else "")
        + "<div class='card'>"
        + "<p class='muted'>手工交易会同步更新账户当前持仓、现金和成本价。编辑已有手工交易时，会按差额修正账户。</p>"
        + f"<form method='post' action='{action}'>"
        + "<p>方向</p>"
        + f"<select name='side' style='width:240px;padding:8px 10px;margin-bottom:12px' {'disabled' if trade is not None else ''}>"
        + f"<option value='buy' {'selected' if side == 'buy' else ''}>买入</option>"
        + f"<option value='sell' {'selected' if side == 'sell' else ''}>卖出</option>"
        + "</select>"
        + ("<p class='muted'>当前版本编辑已有交易时不支持直接改买卖方向，如需反向修正，请新增一笔修正交易。</p>" if trade is not None else "")
        + (f"<input type='hidden' name='side' value='{html.escape(side)}'>" if trade is not None else "")
        + "<p>股票代码</p>"
        + f"<input name='ts_code' value='{html.escape(ts_code)}' style='width:100%;padding:8px 10px;margin-bottom:12px'>"
        + "<p>股票名称（可留空）</p>"
        + f"<input name='name' value='{html.escape(name)}' style='width:100%;padding:8px 10px;margin-bottom:12px'>"
        + "<p>成交数量（正数）</p>"
        + f"<input name='shares' value='{shares if shares else ''}' style='width:240px;padding:8px 10px;margin-bottom:12px'>"
        + "<p>成交价格</p>"
        + f"<input name='price' value='{price if price else ''}' style='width:240px;padding:8px 10px;margin-bottom:12px'>"
        + "<p>备注</p>"
        + f"<input name='note' value='{html.escape(note)}' style='width:100%;padding:8px 10px;margin-bottom:12px'>"
        + "<div><button>保存交易记录</button> "
        + f"<a class='button' style='background:#64748b' href='/accounts/{account_id}'>返回账户详情</a></div>"
        + "</form></div>"
    )
    return render_page(title, body)


def task_detail_html(task_id: int) -> str:
    task = get_task(task_id)
    if task is None:
        return render_page("任务不存在", "<h1>任务不存在</h1>")
    diffs = json.loads(task["diff_json"])
    actual_fills = task_actual_fills(task)
    progress_rows, completed = task_fill_progress(task)
    rows = []
    for item in diffs:
        ref_shares = item["reference_shares"]
        ref_text = f"{ref_shares:.2f}" if ref_shares is not None else "n/a"
        rows.append(
            f"<tr><td>{html.escape(item['ts_code'])}</td><td>{html.escape(item['name'])}</td><td>{fmt_pct(float(item['current_weight']))}</td><td>{fmt_pct(float(item['target_weight']))}</td><td>{fmt_amt(float(item['current_amount']))}</td><td>{fmt_amt(float(item['target_amount']))}</td><td>{fmt_amt(float(item['diff_amount']))}</td><td>{ref_text}</td><td>{html.escape(item['action'])}</td></tr>"
        )
    progress_html_rows = []
    for row in progress_rows:
        progress_html_rows.append(
            f"<tr><td>{html.escape(str(row['ts_code']))}</td><td>{html.escape(str(row['name']))}</td><td>{float(row['target_shares']):.2f}</td><td>{float(row['actual_shares']):.2f}</td><td>{float(row['remaining_shares']):.2f}</td><td>{'完成' if row['done'] else '进行中'}</td></tr>"
        )
    if not progress_html_rows:
        progress_html_rows.append("<tr><td colspan='6' class='muted'>暂无成交进度</td></tr>")
    actual_fill_rows = []
    for fill in actual_fills:
        actual_fill_rows.append(
            f"<tr><td>{html.escape(str(fill.get('ts_code') or ''))}</td><td>{html.escape(str(fill.get('name') or ''))}</td><td>{float(fill.get('shares') or 0.0):.2f}</td><td>{fmt_amt(float(fill.get('price') or 0.0))}</td></tr>"
        )
    if not actual_fill_rows:
        actual_fill_rows.append("<tr><td colspan='4' class='muted'>尚未录入实际成交</td></tr>")
    summary_html = (
        f"<h1>调仓任务 #{task['id']}</h1>"
        f"<p>类型: {html.escape(task_type_label(str(task['task_type'])))} | 状态: {html.escape(task_status_label(str(task['status'])))} | 创建时间: {html.escape(task['created_at'])}</p>"
        "<p class='muted'>正式调仓：研究端目标已更新或首次建仓；偏离修正：研究目标不变，只是把账户拉回目标权重。</p>"
        f"<p>预计买入: {fmt_amt(float(task['estimated_buy_amount']))} | 预计卖出: {fmt_amt(float(task['estimated_sell_amount']))} | 预计费用: {fmt_amt(float(task['estimated_cost']))}</p>"
        + "<div class='actions'>"
        + (f"<form method='post' action='/tasks/{task_id}/execute'><button>标记已执行</button></form>" if task['status'] in ('ready', 'partial') else "")
        + (f"<form method='post' action='/tasks/{task_id}/cancel'><button class='secondary'>忽略任务</button></form>" if task['status'] in ('ready', 'partial') else "")
        + f"<form method='post' action='/tasks/{task_id}/delete'><button class='secondary'>删除任务</button></form>"
        + "</div>"
    )
    if task["status"] in ("ready", "partial"):
        execution_html = (
            "<div class='card' style='margin-top:16px'><h2>录入实际成交</h2>"
            + "<p class='muted'>如果实际成交价格和建议单不同，请按成交结果录入。每行格式：<code>股票代码,成交数量,成交价格</code>；买入数量填正数，卖出填负数。也兼容 <code>股票代码,股票名称,成交数量,成交价格</code>。当累计成交与建议股数一致时，任务会自动标记为已执行。</p>"
            + "<p class='muted'>你可以边交易边逐笔录入，不需要最后再额外点击“标记已执行”。</p>"
            + f"<form method='post' action='/tasks/{task_id}/execute-actual'>"
            + "<textarea name='fills_text' rows='8' style='width:100%;font-family:monospace;padding:10px;'></textarea>"
            + "<p>执行备注</p>"
            + "<input name='execution_note' style='width:100%;padding:8px 10px'>"
            + "<div style='margin-top:12px'><button>按实际成交回写账户</button></div>"
            + "</form></div>"
        )
    else:
        execution_html = f"<div class='card' style='margin-top:16px'><h2>执行信息</h2><p>备注：{html.escape(task['note'] or '无')}</p></div>"
    body = (
        summary_html
        + execution_html
        + "<div class='card' style='margin-top:16px'><h2>成交进度</h2>"
        + f"<p class='muted'>当前进度：{'已完成' if completed else '未完成'}</p>"
        + "<table><thead><tr><th>代码</th><th>名称</th><th>目标股数</th><th>已录入股数</th><th>剩余股数</th><th>状态</th></tr></thead><tbody>"
        + "".join(progress_html_rows)
        + "</tbody></table></div>"
        + "<div class='card' style='margin-top:16px'><h2>已录入成交</h2><table><thead><tr><th>代码</th><th>名称</th><th>成交股数</th><th>成交价格</th></tr></thead><tbody>"
        + "".join(actual_fill_rows)
        + "</tbody></table></div>"
        + "<div class='card' style='margin-top:16px'><table><thead><tr><th>代码</th><th>名称</th><th>当前权重</th><th>目标权重</th><th>当前金额</th><th>目标金额</th><th>差额</th><th>参考股数</th><th>动作</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>"
    )
    return render_page("调仓任务", body)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"
        try:
            if path.startswith("/docs/"):
                target = (ROOT / path.lstrip("/")).resolve()
                docs_root = (ROOT / "docs").resolve()
                if not str(target).startswith(str(docs_root)) or not target.exists() or not target.is_file():
                    self.send_error(HTTPStatus.NOT_FOUND)
                    return
                self._send_file(target)
                return
            if path == "/":
                self._html(dashboard_html())
                return
            if path == "/strategies":
                self._html(strategies_html())
                return
            if path.startswith("/strategies/"):
                strategy_id = path.split("/strategies/", 1)[1]
                query = parse_qs(parsed.query)
                history_window_key = (query.get("history_window") or ["all"])[0]
                sample_view_tag = (query.get("sample_view") or [""])[0]
                self._html(strategy_detail_html(strategy_id, history_window_key=history_window_key, sample_view_tag=sample_view_tag))
                return
            if path == "/accounts":
                self._html(accounts_html())
                return
            if path.startswith("/accounts/"):
                account_tail = path.split("/accounts/", 1)[1]
                if account_tail.endswith("/delete-confirm"):
                    account_id = int(account_tail.split("/", 1)[0])
                    self._html(account_delete_confirm_html(account_id))
                    return
                if account_tail.endswith("/trades/new"):
                    account_id = int(account_tail.split("/", 1)[0])
                    query = parse_qs(parsed.query)
                    self._html(
                        manual_trade_form_html(
                            account_id,
                            error=(query.get("error") or [""])[0],
                            success=(query.get("success") == ["1"]),
                        )
                    )
                    return
                if account_tail.endswith("/switch-strategy"):
                    account_id = int(account_tail.split("/", 1)[0])
                    query = parse_qs(parsed.query)
                    self._html(account_switch_strategy_html(account_id, success=(query.get("success") == ["1"])))
                    return
                account_id = int(account_tail)
                query = parse_qs(parsed.query)
                self._html(account_detail_html(account_id, show_editor=(query.get("edit") == ["1"])))
                return
            if path.startswith("/trades/") and path.endswith("/edit"):
                trade_id = int(path.split("/")[2])
                trade = get_trade(trade_id)
                if trade is None:
                    self._html(render_page("交易不存在", "<h1>交易不存在</h1>"), status=404)
                    return
                query = parse_qs(parsed.query)
                self._html(
                    manual_trade_form_html(
                        int(trade["account_id"]),
                        trade_id=trade_id,
                        error=(query.get("error") or [""])[0],
                        success=(query.get("success") == ["1"]),
                    )
                )
                return
            if path.startswith("/tasks/"):
                task_id = int(path.split("/tasks/", 1)[1])
                self._html(task_detail_html(task_id))
                return
            self.send_error(HTTPStatus.NOT_FOUND)
        except Exception as exc:
            self._html(render_page("错误", f"<h1>发生错误</h1><pre>{html.escape(str(exc))}</pre>"), status=500)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        try:
            length = int(self.headers.get("Content-Length", "0") or "0")
            raw_body = self.rfile.read(length).decode("utf-8") if length > 0 else ""
            form = parse_qs(raw_body)
            if path.endswith("/tasks/rebalance") and path.startswith("/accounts/"):
                account_id = int(path.split("/")[2])
                binding = get_binding(account_id)
                task_id = create_task(account_id, binding["strategy_id"], "rebalance")
                self._redirect(f"/tasks/{task_id}")
                return
            if path == "/accounts/create":
                name = (form.get("name") or [""])[0].strip() or f"账户{now_str()}"
                broker = (form.get("broker") or ["手工测试"])[0].strip() or "手工测试"
                note = (form.get("note") or [""])[0].strip()
                initial_cash = float((form.get("initial_cash") or ["1000000"])[0])
                strategy_id = (form.get("strategy_id") or [""])[0]
                if not strategy_id:
                    strategy_id = load_default_strategy_id()
                account_id = create_account(
                    name=name,
                    broker=broker,
                    note=note,
                    initial_cash=initial_cash,
                    strategy_id=strategy_id,
                )
                self._redirect(f"/accounts/{account_id}")
                return
            if path.endswith("/delete-confirm") and path.startswith("/accounts/"):
                account_id = int(path.split("/")[2])
                delete_account(account_id)
                self._redirect("/accounts")
                return
            if path.endswith("/tasks/drift-fix") and path.startswith("/accounts/"):
                account_id = int(path.split("/")[2])
                binding = get_binding(account_id)
                task_id = create_task(account_id, binding["strategy_id"], "drift_fix")
                self._redirect(f"/tasks/{task_id}")
                return
            if path.endswith("/holdings/save") and path.startswith("/accounts/"):
                account_id = int(path.split("/")[2])
                cash_text = (form.get("cash") or ["0"])[0]
                cash = float(cash_text)
                previous_rows = get_holdings(account_id)
                holdings = parse_holdings_form(form)
                save_account_snapshot(account_id, cash=cash, holdings=holdings)
                reconcile_manual_snapshot_trades(
                    account_id,
                    previous_rows,
                    holdings,
                    note="manual_snapshot_sync",
                )
                self._redirect(f"/accounts/{account_id}")
                return
            if path.endswith("/trades/create") and path.startswith("/accounts/"):
                account_id = int(path.split("/")[2])
                side = (form.get("side") or ["buy"])[0].strip() or "buy"
                ts_code = (form.get("ts_code") or [""])[0].strip()
                name = (form.get("name") or [""])[0].strip()
                shares = float((form.get("shares") or ["0"])[0])
                price = float((form.get("price") or ["0"])[0])
                note = (form.get("note") or [""])[0].strip()
                try:
                    create_manual_trade_entry(
                        account_id=account_id,
                        side=side,
                        ts_code=ts_code,
                        name=name,
                        shares=shares,
                        price=price,
                        note=note,
                    )
                except Exception as exc:
                    self._redirect(f"/accounts/{account_id}/trades/new?error={quote(str(exc))}")
                    return
                self._redirect(f"/accounts/{account_id}/trades/new?success=1")
                return
            if path.endswith("/bind-strategy") and path.startswith("/accounts/"):
                account_id = int(path.split("/")[2])
                strategy_id = (form.get("strategy_id") or [""])[0]
                if strategy_id:
                    update_binding_strategy(account_id, strategy_id)
                self._redirect(f"/accounts/{account_id}/switch-strategy?success=1")
                return
            if path.startswith("/trades/") and path.endswith("/edit"):
                trade_id = int(path.split("/")[2])
                trade = get_trade(trade_id)
                if trade is None:
                    self._redirect("/accounts")
                    return
                side = (form.get("side") or ["buy"])[0].strip() or "buy"
                ts_code = (form.get("ts_code") or [""])[0].strip()
                name = (form.get("name") or [""])[0].strip()
                shares = float((form.get("shares") or ["0"])[0])
                price = float((form.get("price") or ["0"])[0])
                note = (form.get("note") or [""])[0].strip()
                try:
                    update_manual_trade_entry(
                        trade_id=trade_id,
                        side=side,
                        ts_code=ts_code,
                        name=name,
                        shares=shares,
                        price=price,
                        note=note,
                    )
                except Exception as exc:
                    self._redirect(f"/trades/{trade_id}/edit?error={quote(str(exc))}")
                    return
                self._redirect(f"/trades/{trade_id}/edit?success=1")
                return
            if path.endswith("/execute") and path.startswith("/tasks/"):
                task_id = int(path.split("/")[2])
                mark_task_executed(task_id)
                self._redirect(f"/tasks/{task_id}")
                return
            if path.endswith("/execute-actual") and path.startswith("/tasks/"):
                task_id = int(path.split("/")[2])
                fills_text = (form.get("fills_text") or [""])[0]
                execution_note = (form.get("execution_note") or [""])[0]
                fills = parse_execution_fills(fills_text)
                apply_actual_execution(task_id, fills, execution_note)
                self._redirect(f"/tasks/{task_id}")
                return
            if path.endswith("/cancel") and path.startswith("/tasks/"):
                task_id = int(path.split("/")[2])
                cancel_task(task_id)
                self._redirect(f"/tasks/{task_id}")
                return
            if path.endswith("/delete") and path.startswith("/tasks/"):
                task_id = int(path.split("/")[2])
                delete_task(task_id)
                self._redirect("/accounts")
                return
            self.send_error(HTTPStatus.NOT_FOUND)
        except Exception as exc:
            self._html(render_page("错误", f"<h1>发生错误</h1><pre>{html.escape(str(exc))}</pre>"), status=500)

    def log_message(self, fmt: str, *args) -> None:
        return

    def _html(self, content: str, status: int = 200) -> None:
        data = content.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _redirect(self, location: str) -> None:
        self.send_response(303)
        self.send_header("Location", location)
        self.end_headers()

    def _send_file(self, path: Path) -> None:
        data = path.read_bytes()
        content_type, _ = mimetypes.guess_type(str(path))
        self.send_response(200)
        self.send_header("Content-Type", content_type or "application/octet-stream")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def main() -> None:
    from scripts.export_live_platform_data import export_live_data

    export_live_data()
    seed_demo_data()
    host = "127.0.0.1"
    port = 8787
    print(f"[OK] live trading platform running at http://{host}:{port}")
    ThreadingHTTPServer((host, port), Handler).serve_forever()


if __name__ == "__main__":
    main()
