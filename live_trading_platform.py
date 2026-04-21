from __future__ import annotations

import csv
import html
import json
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
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 0; background: #f5f7fb; color: #1f2937; }}
    header {{ background: #0f172a; color: white; padding: 16px 24px; }}
    nav a {{ color: white; margin-right: 16px; text-decoration: none; font-weight: 600; }}
    main {{ padding: 24px; max-width: 1280px; margin: 0 auto; }}
    .grid {{ display: grid; gap: 16px; }}
    .grid-4 {{ grid-template-columns: repeat(4, minmax(0, 1fr)); }}
    .grid-2 {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    .card {{ background: white; border-radius: 14px; padding: 18px; box-shadow: 0 4px 16px rgba(15,23,42,.08); }}
    h1,h2,h3 {{ margin: 0 0 12px 0; }}
    table {{ width: 100%; border-collapse: collapse; background: white; }}
    th, td {{ padding: 10px 12px; border-bottom: 1px solid #e5e7eb; text-align: left; font-size: 14px; }}
    th {{ background: #eef2ff; }}
    .muted {{ color: #64748b; }}
    .pill {{ display: inline-block; padding: 4px 10px; border-radius: 999px; background: #e0f2fe; color: #075985; font-size: 12px; font-weight: 700; }}
    .danger {{ background: #fee2e2; color: #991b1b; }}
    .warn {{ background: #fef3c7; color: #92400e; }}
    .ok {{ background: #dcfce7; color: #166534; }}
    .actions form {{ display: inline-block; margin-right: 8px; }}
    button {{ background: #2563eb; color: white; border: 0; border-radius: 8px; padding: 8px 12px; cursor: pointer; }}
    button.secondary {{ background: #475569; }}
    a.button {{ display: inline-block; background: #2563eb; color: white; padding: 8px 12px; border-radius: 8px; text-decoration: none; }}
    code {{ background: #f1f5f9; padding: 2px 5px; border-radius: 6px; }}
  </style>
</head>
<body>
  <header>
    <nav>
      <a href="/">Dashboard</a>
      <a href="/strategies">策略中心</a>
      <a href="/accounts">账户中心</a>
    </nav>
  </header>
  <main>{body}</main>
</body>
</html>"""


def fmt_pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def fmt_amt(value: float) -> str:
    return f"{value:,.2f}"


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

    cards = f"""
    <div class="grid grid-4">
      <div class="card"><h3>今日正式调仓</h3><div style="font-size:32px;font-weight:700;">{open_rebalances}</div></div>
      <div class="card"><h3>今日偏离修正</h3><div style="font-size:32px;font-weight:700;">{open_drift}</div></div>
      <div class="card"><h3>切换建议</h3><div style="font-size:32px;font-weight:700;">{switch_count}</div></div>
      <div class="card"><h3>研究数据更新</h3><div style="font-size:24px;font-weight:700;">{html.escape(updated_at)}</div></div>
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
            f"<tr><td><a href='/accounts/{account['id']}'>{html.escape(account['name'])}</a></td>"
            f"<td>{html.escape(strategy['display_name'])}</td>"
            f"<td>{html.escape(advice['type'])}</td>"
            f"<td>{html.escape(strategy['risk_state'])}</td>"
            f"<td>{fmt_pct(drift)}</td>"
            f"<td>{fmt_amt(float(current['total_assets']))}</td>"
            f"<td>{fmt_amt(total_pnl)}</td>"
            f"<td>{fmt_pct(total_pnl_pct)}</td></tr>"
        )
    accounts_table = (
        "<div class='card'><h2>账户概览</h2><table><thead><tr><th>账户</th><th>当前策略</th><th>今日建议</th><th>风险状态</th><th>偏离度</th><th>总资产</th><th>总盈亏</th><th>总盈亏率</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>"
    )

    per_account_task_cards = []
    for account in accounts:
        task_rows = []
        for task in get_tasks(int(account["id"]))[:5]:
            task_rows.append(
                f"<tr><td><a href='/tasks/{task['id']}'>任务 #{task['id']}</a></td><td>{html.escape(task_type_label(str(task['task_type'])))}</td><td>{html.escape(task_status_label(str(task['status'])))}</td><td>{html.escape(task['created_at'])}</td></tr>"
            )
        if not task_rows:
            task_rows.append("<tr><td colspan='4' class='muted'>暂无任务</td></tr>")
        per_account_task_cards.append(
            "<div class='card'>"
            f"<h2>{html.escape(account['name'])} 的任务</h2>"
            "<table><thead><tr><th>任务</th><th>类型</th><th>状态</th><th>创建时间</th></tr></thead><tbody>"
            + "".join(task_rows)
            + "</tbody></table></div>"
        )
    tasks_section = "<div class='grid grid-2' style='margin-top:16px'>" + "".join(per_account_task_cards) + "</div>"

    return render_page("Dashboard", f"<h1>aiinvestor 实盘平台</h1>{cards}<div style='margin-top:16px'>{accounts_table}</div>{tasks_section}")


def strategies_html() -> str:
    registry = load_registry()["strategies"]
    groups = {"a_share": [], "hkconnect": []}
    for item in registry:
        groups.setdefault(str(item.get("market_scope", "a_share")), []).append(item)

    sections = []
    for scope in ("a_share", "hkconnect"):
        items = groups.get(scope, [])
        if not items:
            continue
        cards = []
        for item in items:
            metrics = item["summary_metrics"]
            cards.append(
                "<div class='card'>"
                f"<div class='pill'>{html.escape(market_scope_label(str(item.get('market_scope', 'a_share'))))} / {html.escape(item['path'])} / {html.escape(item['winner_type'])}</div>"
                f"<h3 style='margin-top:12px'><a href='/strategies/{item['strategy_id']}'>{html.escape(item['display_name'])}</a></h3>"
                f"<div class='muted'><code>{html.escape(item['strategy_id'])}</code></div>"
                f"<p>Total Return {fmt_pct(float(metrics.get('total_return', 0.0)))} | CAGR {fmt_pct(float(metrics.get('cagr', 0.0)))} | MaxDD {fmt_pct(float(metrics.get('max_drawdown', 0.0)))} | Sharpe {float(metrics.get('sharpe_ratio', 0.0)):.4f} | Turn {float(metrics.get('average_annual_turnover', 0.0)):.2f}</p>"
                f"<p>当前总仓位建议: {fmt_pct(float(item['target_total_exposure']))} | 风险状态: {html.escape(item['risk_state'])} | 更新: {html.escape(str(item['updated_at']))}</p>"
                "</div>"
            )
        sections.append(f"<h2>{html.escape(market_scope_label(scope))}策略</h2><div class='grid grid-2'>{''.join(cards)}</div>")
    return render_page("策略中心", "<h1>策略中心</h1>" + "".join(sections))


def strategy_detail_html(strategy_id: str, history_window_index: int = 0) -> str:
    item = load_strategy_snapshot(strategy_id)
    windows = item["windows"]
    rows = []
    for key in ("since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"):
        if key not in windows:
            continue
        w = windows[key]
        rows.append(
            f"<tr><td>{html.escape(key)}</td><td>{fmt_pct(float(w['total_return']))}</td><td>{fmt_pct(float(w['cagr']))}</td><td>{fmt_pct(float(w['max_drawdown']))}</td><td>{float(w['sharpe']):.4f}</td><td>{float(w['turnover']):.2f}</td></tr>"
        )
    weight_rows = []
    for row in item["latest_weights"]:
        weight_rows.append(
            f"<tr><td>{html.escape(row['ts_code'])}</td><td>{html.escape(row['name'])}</td><td>{fmt_pct(float(row['weight']))}</td><td>{fmt_amt(float(row['latest_price'] or 0.0)) if row['latest_price'] is not None else 'n/a'}</td></tr>"
        )

    history_windows = item.get("history_windows") or []
    if history_windows:
        history_window_index = max(0, min(history_window_index, len(history_windows) - 1))
    else:
        history_window_index = 0
    selected_history = history_windows[history_window_index] if history_windows else None
    history_selector = ""
    history_html = "<div class='muted'>暂无历史持仓快照。</div>"
    if history_windows:
        options = []
        for hist in history_windows:
            selected = " selected" if int(hist["window_index"]) == history_window_index else ""
            options.append(
                f"<option value='{int(hist['window_index'])}'{selected}>{html.escape(str(hist['label']))}（{int(hist['snapshot_count'])} 次快照）</option>"
            )
        history_selector = (
            f"<form method='get' action='/strategies/{quote(strategy_id)}' style='margin:12px 0 16px 0'>"
            "<label>历史持仓窗口（按调仓日，每12个月分组）</label>"
            f"<select name='history_window' style='display:block;margin-top:8px;padding:8px 10px;min-width:320px'>{''.join(options)}</select>"
            "<div style='margin-top:10px'><button>切换窗口</button></div>"
            "</form>"
        )
        snapshot_blocks = []
        for snapshot in selected_history["snapshots"]:
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
            f"<p class='muted'>当前展示窗口：{html.escape(selected_history['label'])}。每个快照日期均为该次调仓后的目标持仓日期。</p>"
            + "".join(snapshot_blocks)
        )
    body = (
        f"<h1>{html.escape(item['display_name'])}</h1>"
        f"<p><code>{html.escape(strategy_id)}</code></p>"
        f"<p>市场: {html.escape(market_scope_label(str(item.get('market_scope', 'a_share'))))} | 路径: {html.escape(item['path'])} | 类型: {html.escape(item['winner_type'])} | 当前建议仓位: {fmt_pct(float(item['target_total_exposure']))} | 风险状态: {html.escape(item['risk_state'])}</p>"
        "<div class='card'><h2>窗口表现</h2><table><thead><tr><th>窗口</th><th>Total Return</th><th>CAGR</th><th>MaxDD</th><th>Sharpe</th><th>Turnover</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>"
        + "<div class='card' style='margin-top:16px'><h2>最新目标持仓</h2><table><thead><tr><th>代码</th><th>名称</th><th>目标权重</th><th>最新价格</th></tr></thead><tbody>"
        + "".join(weight_rows)
        + "</tbody></table></div>"
        + "<div class='card' style='margin-top:16px'><h2>历史持仓（12个月维度）</h2>"
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
        + "<div class='card' style='margin-bottom:16px'><h2>新增账户</h2>"
        + "<form method='post' action='/accounts/create'>"
        + "<div class='grid grid-2'>"
        + "<div><p>账户名称</p><input name='name' style='width:100%;padding:8px 10px'></div>"
        + "<div><p>券商</p><input name='broker' style='width:100%;padding:8px 10px' value='手工测试'></div>"
        + "<div><p>初始现金</p><input name='initial_cash' style='width:100%;padding:8px 10px' value='1000000'></div>"
        + "<div><p>策略</p><select name='strategy_id' style='width:100%;padding:8px 10px'>" + "".join(options) + "</select></div>"
        + "</div>"
        + "<p>备注</p><input name='note' style='width:100%;padding:8px 10px'>"
        + "<div style='margin-top:12px'><button>创建账户</button></div>"
        + "</form></div>"
        + "<div class='card'><table><thead><tr><th>账户</th><th>券商</th><th>当前策略</th><th>今日建议</th><th>偏离度</th><th>总资产</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>",
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
        rows.append(
            f"<tr><td>{html.escape(target['ts_code'])}</td><td>{html.escape(target['name'])}</td><td>{fmt_pct(current_weight)}</td><td>{fmt_pct(float(target['weight']))}</td><td>{fmt_pct(float(target['weight'])-current_weight)}</td><td>{'买入' if float(target['weight'])>current_weight else '持有/卖出'}</td></tr>"
        )
    tasks_rows = []
    for task in get_tasks(account_id)[:10]:
        tasks_rows.append(
            f"<tr><td><a href='/tasks/{task['id']}'>#{task['id']}</a></td><td>{html.escape(task_type_label(str(task['task_type'])))}</td><td>{html.escape(task_status_label(str(task['status'])))}</td><td>{html.escape(task['created_at'])}</td></tr>"
        )
    if not tasks_rows:
        tasks_rows.append("<tr><td colspan='4' class='muted'>暂无任务</td></tr>")
    existing_holdings = get_holdings(account_id)
    pnl_rows = []
    for row in current["positions"]:
        pnl_rows.append(
            f"<tr><td>{html.escape(row['ts_code'])}</td><td>{html.escape(row['name'])}</td><td>{row['shares']:.2f}</td><td>{fmt_amt(row['cost_price'])}</td><td>{fmt_amt(row['last_price'])}</td><td>{fmt_amt(row['market_value'])}</td><td>{fmt_amt(row['unrealized_pnl'])}</td><td>{fmt_pct(row['unrealized_pnl_pct'])}</td></tr>"
        )
    trade_rows = []
    for trade in get_account_trades(account_id, limit=20):
        realized_text = fmt_amt(float(trade["realized_pnl"])) if trade["realized_pnl"] is not None else "-"
        action_html = (
            f"<a class='button' style='padding:6px 10px;font-size:12px' href='/trades/{int(trade['id'])}/edit'>编辑</a>"
            if trade["task_id"] is None
            else "<span class='muted'>任务生成</span>"
        )
        trade_rows.append(
            f"<tr><td>{html.escape(trade['executed_at'])}</td><td>{html.escape(trade['ts_code'])}</td><td>{html.escape(trade['name'])}</td><td>{html.escape('买入' if trade['side']=='buy' else '卖出')}</td><td>{float(trade['shares']):.2f}</td><td>{fmt_amt(float(trade['price']))}</td><td>{fmt_amt(float(trade['gross_amount']))}</td><td>{fmt_amt(float(trade['fee']))}</td><td>{fmt_amt(float(trade['net_cash_change']))}</td><td>{realized_text}</td><td>{html.escape(trade_note_label(str(trade['note'] or '')))}</td><td>{action_html}</td></tr>"
        )
    if not trade_rows:
        trade_rows.append("<tr><td colspan='11' class='muted'>暂无交易流水</td></tr>")
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
    body = (
        "<div style='display:flex;justify-content:space-between;align-items:flex-start;gap:16px'>"
        + "<div>"
        + f"<h1>账户详情 - {html.escape(account['name'])}</h1>"
        f"<p>券商: {html.escape(account['broker'])} | 初始本金: {fmt_amt(initial_capital)} | 总资产: {fmt_amt(float(current['total_assets']))} | 现金: {fmt_amt(float(account['cash']))} | 股票市值: {fmt_amt(current['market_value'])}</p>"
        f"<p>总盈亏: {fmt_amt(total_pnl)} | 总盈亏率: {fmt_pct(total_pnl_pct)}</p>"
        f"<p>当前策略: {html.escape(strategy['display_name'])} | 当前建议仓位: {fmt_pct(float(strategy['target_total_exposure']))} | 风险状态: {html.escape(strategy['risk_state'])}</p>"
        f"<p class='muted'>当前价格来源：{html.escape(current['price_source_label'])}</p>"
        + "</div>"
        + "<div style='display:flex;gap:8px;flex-wrap:wrap'>"
        + f"<a class='button' href='/accounts/{account_id}/switch-strategy'>切换策略</a>"
        + f"<a class='button' style='background:#b91c1c' href='/accounts/{account_id}/delete-confirm'>删除账户</a>"
        + "</div></div>"
        + "<div class='card'><h2>今日建议</h2>"
        + f"<p><strong>{html.escape(advice['type'])}</strong>：{html.escape(advice['reason'])}</p>"
        + "<div class='actions'>"
        + f"<form method='post' action='/accounts/{account_id}/tasks/rebalance'><button>生成正式调仓单</button></form>"
        + f"<form method='post' action='/accounts/{account_id}/tasks/drift-fix'><button class='secondary'>生成偏离修正单</button></form>"
        + "</div></div>"
        + ("<div class='card' style='margin-top:16px'><h2>策略切换建议</h2>"
           f"<p>建议策略：<code>{html.escape(suggestion['suggested_strategy_id'])}</code></p>"
           f"<p>{html.escape(suggestion['reason'])}</p></div>" if suggestion else "")
        + "<div class='card' style='margin-top:16px'><h2>当前持仓盈亏</h2><table><thead><tr><th>代码</th><th>名称</th><th>数量</th><th>成本价</th><th>当前价</th><th>当前市值</th><th>浮盈亏</th><th>收益率</th></tr></thead><tbody>"
        + "".join(pnl_rows)
        + "</tbody></table>"
        + holding_editor
        + "</div>"
        + "<div class='card' style='margin-top:16px'><h2>当前持仓 vs 目标持仓</h2><table><thead><tr><th>代码</th><th>名称</th><th>当前权重</th><th>目标权重</th><th>偏离</th><th>建议动作</th></tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table></div>"
        + "<div class='card' style='margin-top:16px'><h2>最近任务</h2><table><thead><tr><th>任务</th><th>类型</th><th>状态</th><th>创建时间</th></tr></thead><tbody>"
        + "".join(tasks_rows)
        + "</tbody></table></div>"
        + "<div class='card' style='margin-top:16px'><h2>交易流水</h2><table><thead><tr><th>时间</th><th>代码</th><th>名称</th><th>方向</th><th>数量</th><th>价格</th><th>成交额</th><th>费用</th><th>现金变化</th><th>已实现盈亏</th><th>备注</th><th>操作</th></tr></thead><tbody>"
        + "".join(trade_rows)
        + "</tbody></table>"
        + f"<div style='margin-top:12px'><a class='button' href='/accounts/{account_id}/trades/new'>新增手工交易</a></div>"
        + "</div>"
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
            if path == "/":
                self._html(dashboard_html())
                return
            if path == "/strategies":
                self._html(strategies_html())
                return
            if path.startswith("/strategies/"):
                strategy_id = path.split("/strategies/", 1)[1]
                query = parse_qs(parsed.query)
                history_window = 0
                try:
                    history_window = int((query.get("history_window") or ["0"])[0])
                except Exception:
                    history_window = 0
                self._html(strategy_detail_html(strategy_id, history_window_index=history_window))
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
