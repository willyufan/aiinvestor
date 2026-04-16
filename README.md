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

## 中文策略说明

当前项目里最值得继续迭代的版本，不是纯核心集中策略，而是：

- `核心80_探索20_总市值底座_胜出者核心`

这套框架的核心思想是：

- 核心池提供相对稳定的底座，来源于 `沪深300 + 科创50`
- 探索池和种子池负责更早发现潜在强者，来源于 `中证500 + 科创100 + 科创200`
- 强势个股不是一直留在卫星仓，而是可以逐步晋升到 `winner_core`
- 核心仓内部继续拆成“稳定核心”和“晋升核心”，前者更稳，后者更偏进攻

这次重点优化的 4 个方向如下：

1. 行业强度信号接入探索 / 种子层  
   探索和种子层不再只看个股涨幅，而是同时看行业强度、行业内龙头强度、动量和突破信号，尽量做到“先选对赛道，再选赛道里的强股”。

2. 双轨晋升到 `winner_core`  
   既保留普通晋升路径，也保留快速晋升路径。普通晋升要求更连续，快速晋升要求更强的行业强度、放量和突破确认。

3. 晋升核心分阶段加仓  
   新晋升的核心股不是一步到位给满，而是按阶段逐步放大权重，减少误判时的大回撤。

4. 核心内部拆成“稳定核心 + 晋升核心”  
   稳定核心更偏成熟龙头，晋升核心更偏正在走强的新胜出者，组合层面兼顾稳定性和超额收益。

### 这轮优化回测情况

以 `核心80_探索20_总市值底座_指数核心` 作为优化前基线，对比优化后的 `核心80_探索20_总市值底座_胜出者核心`：

- 累计收益从 `96.46%` 提升到 `113.33%`
- CAGR 从 `11.25%` 提升到 `12.71%`
- 最大回撤从 `-34.49%` 改善到 `-28.43%`
- 夏普从 `0.5158` 提升到 `0.5684`
- 年均换手从 `2.42` 降到 `2.25`

这说明这 4 项优化在当前动态发现框架里是有效的，既提升了收益，也改善了回撤和效率。

但也要明确一点：

- 这套“市场发现”策略目前仍然明显落后于你最初给定的静态冠军池
- `大市值池`：累计收益 `390.94%`，CAGR `28.56%`，最大回撤 `-19.03%`
- `科创选股`：累计收益 `200.11%`，CAGR `18.95%`，最大回撤 `-24.00%`

所以现在更准确的结论是：

- 这轮优化已经把动态发现框架从“能跑”推到“有明显改进”
- 但它还没有做到“比后视镜精选冠军池更早、更重地抓住真正的大牛股”
- 下一步最有价值的方向，仍然是继续加强探索 / 种子层的早期发现能力，而不是把仓位继续往纯核心集中上推

### 结果对比图

下图对比了几个最关键版本：

- `Large Cap Static`：你最早给定的大市值池
- `Kechuang Static`：你最早给定的科创选股池
- `80/20 Index Core`：优化前的动态基线
- `80/20 Winner Core`：当前优化后的最佳动态版本
- `Pure Core 6`：纯核心集中实验版

![Strategy Comparison](docs/strategy_comparison.png)
