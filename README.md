# aiinvestor

一个基于 Tushare Pro 的 A 股组合回测与策略迭代项目。

项目当前重点是构建并持续迭代一个月度调仓的 A 股选股框架，核心关注点包括：

- 使用动态股票池，而不是纯后视镜的静态冠军池
- 使用带真实交易费用的市值加权组合构建
- 使用 `core / explore / seed` 三层结构去发现和放大新强者
- 使用本地缓存与可复现输出支持持续回测迭代

## 当前最佳策略

当前项目不再只用单一时间窗挑一个“唯一最佳策略”，而是并行维护 **4 条跟踪赢家线**：

- `since_2017_01`：长窗口
- `since_2020_01`：中窗口
- `since_2023_01`：短窗口
- `since_2025_01`：超短窗口

自动任务会把最新赢家和指标更新到下面这个区块：

<!-- AUTO:WEIGHTED-WINNERS:START -->

This repo tracks **two research paths**:

- **Path 1 (winner-core family constrained):** 4 tracked winners across multi-window + checkpoint scoring.
- **Path 2 (unconstrained max-return):** a separate best candidate ranked by robust return across all 4 windows.

Validation windows:

- `since_2017_01` (long window)
- `since_2020_01` (mid window)
- `since_2023_01` (short window)
- `since_2025_01` (very short window)

## Path 1 — Winner-Core Tracked Winners

### Short-cycle Winner (30/30/40)

- Strategy: `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6` (核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只)
- Weighted (CAGR / Sharpe / Max DD / Turnover): `24.69%` / `0.9124` / `-22.75%` / `2.85`

Window metrics (as of `2026-04-18`, weights: 2017-01=30%, 2020-01=30%, 2023-01=40%):

- `2017-01-01` → `2026-04-18`: CAGR `22.33%`, Max DD `-22.02%`, Sharpe `0.9442`
- `2020-01-01` → `2026-04-18`: CAGR `24.26%`, Max DD `-20.95%`, Sharpe `0.8945`
- `2023-01-01` → `2026-04-18`: CAGR `26.78%`, Max DD `-24.63%`, Sharpe `0.9020`
- `2025-01-01` → `2026-04-18`: CAGR `62.45%`, Max DD `-13.40%`, Sharpe `1.5153`

### Mid-cycle Winner (30/40/30)

- Strategy: `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6` (核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只)
- Weighted (CAGR / Sharpe / Max DD / Turnover): `24.44%` / `0.9117` / `-22.38%` / `2.85`

Window metrics (as of `2026-04-18`, weights: 2017-01=30%, 2020-01=40%, 2023-01=30%):

- `2017-01-01` → `2026-04-18`: CAGR `22.33%`, Max DD `-22.02%`, Sharpe `0.9442`
- `2020-01-01` → `2026-04-18`: CAGR `24.26%`, Max DD `-20.95%`, Sharpe `0.8945`
- `2023-01-01` → `2026-04-18`: CAGR `26.78%`, Max DD `-24.63%`, Sharpe `0.9020`
- `2025-01-01` → `2026-04-18`: CAGR `62.45%`, Max DD `-13.40%`, Sharpe `1.5153`

### 2020-Window Winner (2020-only checkpoint)

- Strategy: `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` (核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只)
- Weighted (CAGR / Sharpe / Max DD / Turnover): `25.58%` / `0.9122` / `-21.84%` / `2.86`

Window metrics (as of `2026-04-18`, weights: 2020-01=100%):

- `2017-01-01` → `2026-04-18`: CAGR `19.74%`, Max DD `-22.50%`, Sharpe `0.8480`
- `2020-01-01` → `2026-04-18`: CAGR `25.58%`, Max DD `-21.84%`, Sharpe `0.9122`
- `2023-01-01` → `2026-04-18`: CAGR `25.36%`, Max DD `-24.37%`, Sharpe `0.8533`
- `2025-01-01` → `2026-04-18`: CAGR `58.22%`, Max DD `-12.34%`, Sharpe `1.3951`

### 2025-Window Winner (2025-only checkpoint)

- Strategy: `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7` (核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只)
- Weighted (CAGR / Sharpe / Max DD / Turnover): `93.14%` / `2.0609` / `-9.93%` / `3.81`

Window metrics (as of `2026-04-18`, weights: 2025-01=100%):

- `2017-01-01` → `2026-04-18`: CAGR `19.28%`, Max DD `-25.33%`, Sharpe `0.8492`
- `2020-01-01` → `2026-04-18`: CAGR `24.53%`, Max DD `-22.49%`, Sharpe `0.9170`
- `2023-01-01` window: n/a
- `2025-01-01` → `2026-04-18`: CAGR `93.14%`, Max DD `-9.93%`, Sharpe `2.0609`

## Path 2 — Max-Return Candidate

### Best Robust Candidate (4-window)

- Strategy: `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom7` (核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升7只)
- Robust (mean CAGR / min CAGR / mean Sharpe / worst Max DD / mean Turnover): `34.95%` / `19.83%` / `1.0372` / `-23.76%` / `3.18`

Window metrics:

- `2017-01-01` → `2026-04-18`: CAGR `19.83%`, Max DD `-22.50%`, Sharpe `0.8652`
- `2020-01-01` → `2026-04-18`: CAGR `24.19%`, Max DD `-22.28%`, Sharpe `0.9086`
- `2023-01-01` → `2026-04-18`: CAGR `26.68%`, Max DD `-23.76%`, Sharpe `0.8791`
- `2025-01-01` → `2026-04-18`: CAGR `69.09%`, Max DD `-9.40%`, Sharpe `1.4960`

<!-- AUTO:WEIGHTED-WINNERS:END -->

当不同窗口的赢家不同时，项目会同时保留它们，作为防过拟合的护栏。README 中的 `strategy_comparison_*` 图展示跟踪赢家，`strategy_family_*` 图展示完整策略家族，而且完整家族图只使用已有结果文件，不额外触发回测。

当前主策略框架使用：

- 核心池：`沪深300 + 科创50`
- 探索池：`中证500 + 科创100 + 科创200`
- 月度调仓
- 前复权价格
- 总市值底座
- 从 explore/seed 晋升到 `winner_core`
- 按不同跟踪线调整 `winner_core` 的稳定核心 / 晋升核心分配
- 真实买卖佣金与印花税

## 中文详细说明

下面是当前的中文详细说明与图表区。

## 英文说明

An A-share portfolio backtesting and strategy-iteration project based on Tushare Pro.

The project focuses on building and iterating a monthly-rebalanced stock-selection framework for the China A-share market, with emphasis on:

- dynamic stock pools instead of hindsight-picked static lists
- market-cap weighted portfolio construction with realistic trading costs
- core / explore / seed style discovery logic for finding emerging leaders
- reproducible outputs with local caching

## English Strategy Structure

The project currently contains several strategy branches for comparison:

- `index_core`: the core sleeve stays anchored to index constituents
- `winner_core`: strong names discovered in explore/seed can be promoted into the core sleeve
- `pure_core_growth`: an experimental concentrated growth-only version without market risk control

The main production-style framework is `core_explore`, which combines:

- a core sleeve for relatively stable leaders
- an explore sleeve for faster iteration
- a seed sleeve for earlier-stage discovery
- staged promotion and slower demotion for promoted core names

## English Data And Rules

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

## English Repository Files

- `backtest_marketcap_etf.py`: main backtest program
- `requirements.txt`: Python dependencies
- `README.md`: project overview

The following directories are intentionally kept out of git:

- `data_cache/`: local Tushare cache
- `results/`: backtest output files
- `.venv/`: local Python environment

## English Quick Start

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python backtest_marketcap_etf.py
```

## English Output Files

Each strategy run writes results under `results/`, including:

- `equity_curve.csv`
- `monthly_returns.csv`
- `annual_returns.csv`
- `latest_weights.csv`
- `weights_history.csv` (每月末持仓权重快照，含 `CASH` 现金行)
- `turnover.csv`
- `summary.json`
- `equity_curve.png`

There is also a strategy comparison table:

- `results/strategy_comparison_base_method.csv`

## English Notes

- The current implementation includes a Tushare token directly in the script for local research use.
- Local cache is used to reduce repeated API requests.
- Some historical index constituents may be unavailable in `stock_basic`; these are logged and excluded explicitly instead of being silently skipped.

## English Status

The project has already been initialized as a git repository and synced to GitHub:

- repository: `willyufan/aiinvestor`
- URL: `https://github.com/willyufan/aiinvestor`

当前项目里最值得继续迭代的版本，不是纯核心集中策略，而是：

- `核心80_探索20_总市值底座_胜出者核心 (进攻10/90 快速加仓)`

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

### 三窗口验证结果

为了减少过拟合风险，当前每个重要策略都会同时跑三档样本：

- `2017-01 起`：长样本，约 9 年
- `2020-01 起`：中样本，约 6 年
- `2023-01 起`：短样本，约 3 年

当前“生产候选版本”仍然是：

- `核心80_探索20_总市值底座_胜出者核心 (进攻10/90 快速加仓)`

它在三档样本里的表现分别是：

- `2017-01 起`：累计收益 `472.27%`，CAGR `20.55%`，最大回撤 `-22.50%`，夏普 `0.8980`
- `2020-01 起`：累计收益 `282.72%`，CAGR `23.60%`，最大回撤 `-24.66%`，夏普 `0.8845`
- `2023-01 起`：累计收益 `92.11%`，CAGR `21.64%`，最大回撤 `-23.75%`，夏普 `0.8062`

以 `核心80_探索20_总市值底座_指数核心` 作为优化前基线，对比优化后的 `核心80_探索20_总市值底座_胜出者核心 (进攻10/90 快速加仓)`：

- `2020-01` 主样本里，累计收益从 `83.19%` 提升到 `282.72%`
- `2020-01` 主样本里，CAGR 从 `10.03%` 提升到 `23.60%`
- `2017-01` 长样本里，累计收益从 `105.60%` 提升到 `472.27%`
- `2017-01` 长样本里，CAGR 从 `8.03%` 提升到 `20.55%`
- 最新组合持仓仍然明显集中在少数胜出者核心上

这一轮新增的关键动作是：

- 修正 `winner_core` 的降级方向，让晋升核心真正按“连续掉队”而不是“连续保留”来退出
- 把风险状态下的卫星仓暴露进一步收缩到 `0.30`，让探索 / 种子层在逆风期更主动减仓
- 把核心内部权重进一步调整为 `稳定核心 10% + 晋升核心 90%`，并把新晋升核心的加仓节奏提前，让真正跑出来的胜出者更早拿到更高权重

这说明当前动态发现框架已经不只是“能跑通”，而是在长中短三档窗口里都具备了比较稳定的超额收益能力。

但也要明确一点：

- 这套“市场发现”策略目前仍然明显落后于你最初给定的静态冠军池
- `大市值池`：累计收益 `390.94%`，CAGR `28.56%`，最大回撤 `-19.03%`
- `科创选股`：累计收益 `200.11%`，CAGR `18.95%`，最大回撤 `-24.00%`

所以现在更准确的结论是：

- 这轮优化已经把动态发现框架从“能跑”推到“有明显改进”
- 但它还没有做到“比后视镜精选冠军池更早、更重地抓住真正的大牛股”
- 下一步最有价值的方向，仍然是继续加强探索 / 种子层的早期发现能力，而不是把仓位继续往纯核心集中上推

另外，短窗口也给了一个重要提示：

- `2023-01` 这档短样本里，最好的并不是“进攻10/90 快速加仓”，而是标准版 `核心80_探索20_总市值底座_胜出者核心`
- 这说明策略越激进，越容易在短窗口里出现表现顺序切换
- 也正因为如此，README 和图表现在都会同时展示 `2017 / 2020 / 2023` 三档结果，而不再只看单一窗口

### 结果对比图

下面四张图分别展示：

- `2017-01 起` 长样本
- `2020-01 起` 中样本
- `2023-01 起` 短样本
- `2025-01 起` 超短样本

每张图都包含：

- 净值曲线
- 风险收益散点
- 指标表

图中最关键的策略包括：

- `SSE Composite`：上证指数基准，用于看策略相对大盘的超额表现
- `Large Cap Static`：你最早给定的大市值池，当前放在 `2020-01`、`2023-01` 与 `2025-01` 三个窗口里作为静态参考
- `Kechuang Static`：你最早给定的科创池，因科创板发布时间较晚，当前放在 `2020-01`、`2023-01` 与 `2025-01` 三个窗口
- `80/20 Index Core`：优化前的动态基线
- `80/20 Winner Core`：标准版胜出者核心
- `80/20 Winner Core (Aggressive)`：当前长中样本的最佳动态版本

#### 2017-01 起

![Strategy Comparison Since 2017-01](docs/strategy_comparison_since_2017_01.png)

#### 2020-01 起

![Strategy Comparison Since 2020-01](docs/strategy_comparison_since_2020_01.png)

#### 2023-01 起

![Strategy Comparison Since 2023-01](docs/strategy_comparison_since_2023_01.png)

#### 2025-01 起

![Strategy Comparison Since 2025-01](docs/strategy_comparison_since_2025_01.png)

### 完整策略家族对比图

下面四张图使用同一批已有回测结果，展示更完整的策略家族，不需要额外重跑回测：

#### 2017-01 起（完整家族）

![Strategy Family Since 2017-01](docs/strategy_family_since_2017_01.png)

#### 2020-01 起（完整家族）

![Strategy Family Since 2020-01](docs/strategy_family_since_2020_01.png)

#### 2023-01 起（完整家族）

![Strategy Family Since 2023-01](docs/strategy_family_since_2023_01.png)

#### 2025-01 起（完整家族）

![Strategy Family Since 2025-01](docs/strategy_family_since_2025_01.png)
