# aiinvestor

A-share portfolio backtesting project based on Tushare Pro.

## Files

- `backtest_marketcap_etf.py`: main backtest script
- `requirements.txt`: Python dependencies

## Quick Start

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python backtest_marketcap_etf.py
```

## Notes

- Tushare Pro token is configured in the script.
- Local cache is stored under `data_cache/`.
- Backtest outputs are written to `results/`.
