# aiinvestor

An A-share portfolio backtesting project based on Tushare Pro.

The project focuses on building and iterating a monthly-rebalanced stock selection framework for the China A-share market, with emphasis on:

- dynamic stock pools instead of hindsight-picked static lists
- market-cap weighted portfolio construction with realistic trading costs
- core / explore / seed style discovery logic for finding emerging leaders
- reproducible outputs with local caching

## Current Best Strategy

The current best-performing dynamic-market-discovery version in this project is:

- `核心80_探索20_总市值底座_胜出者核心`
- sample period: `2020-01-01` to `2026-04-16`
- total return: `113.33%`
- CAGR: `12.71%`
- max drawdown: `-28.43%`
- annual volatility: `26.76%`
- Sharpe ratio: `0.5684`

This strategy uses:

- core pool: `沪深300 + 科创50`
- explore pool: `中证500 + 科创100 + 科创200`
- monthly rebalance
- forward-adjusted prices
- market-cap base weights
- winner promotion from explore/seed into core
- realistic buy/sell commissions and stamp duty

## Strategy Structure

The project currently contains several strategy branches for comparison:

- `index_core`: the core sleeve stays anchored to index constituents
- `winner_core`: strong names discovered in explore/seed can be promoted into the core sleeve
- `pure_core_growth`: an experimental concentrated growth-only version without market risk control

The main production-style framework is `core_explore`, which combines:

- a core sleeve for relatively stable leaders
- an explore sleeve for faster iteration
- a seed sleeve for earlier-stage discovery
- staged promotion and slower demotion for promoted core names

## Data And Rules

- data source: `Tushare Pro`
- prices: forward-adjusted close built from `daily.close` and `adj_factor`
- market cap: `daily_basic.total_mv`
- rebalance timing:
  - use the last trading day of each month to compute target weights
  - trade on the first trading day of the next month
- costs:
  - buy commission: `0.03%`
  - sell commission: `0.03%`
  - stamp duty:
    - `0.10%` before `2023-08-28`
    - `0.05%` on and after `2023-08-28`

## Repository Files

- `backtest_marketcap_etf.py`: main backtest program
- `requirements.txt`: Python dependencies
- `README.md`: project overview

The following directories are intentionally kept out of git:

- `data_cache/`: local Tushare cache
- `results/`: backtest output files
- `.venv/`: local Python environment

## Quick Start

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python backtest_marketcap_etf.py
```

## Output Files

Each strategy run writes results under `results/`, including:

- `equity_curve.csv`
- `monthly_returns.csv`
- `annual_returns.csv`
- `latest_weights.csv`
- `turnover.csv`
- `summary.json`
- `equity_curve.png`

There is also a strategy comparison table:

- `results/strategy_comparison_base_method.csv`

## Notes

- The current implementation includes a Tushare token directly in the script for local research use.
- Local cache is used to reduce repeated API requests.
- Some historical index constituents may be unavailable in `stock_basic`; these are logged and excluded explicitly instead of being silently skipped.

## Status

The project has already been initialized as a git repository and synced to GitHub:

- repository: `willyufan/aiinvestor`
- URL: `https://github.com/willyufan/aiinvestor`
