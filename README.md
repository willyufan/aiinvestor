# aiinvestor

一个基于 Tushare Pro 的 A 股与沪港通组合回测、策略迭代项目。

> 2026-07-24 研究校准：A股 `share24` 仅成为 2025-window artifact winner；因 2020 CAGR 相对 Path1 robust 下降超过 6pp，判定仍为 `keep_watch`，不是正式 promote。HK Path4 v47 与 Path5 v35 为 `robust_observation`，进入观察位，不是强稳定 winner。

项目当前重点是构建并持续迭代一个月度调仓的 A 股选股框架，核心关注点包括：

- 使用动态股票池，而不是纯后视镜的静态冠军池
- 使用带真实交易费用的市值加权组合构建
- 使用 `core / explore / seed` 三层结构去发现和放大新强者
- 独立维护 A 股研究线与沪港通研究线，港股结论不并入 A 股 winner
- 使用本地缓存与可复现输出支持持续回测迭代

## 当前最佳策略

当前项目不再只用单一时间窗挑一个“唯一最佳策略”，而是并行维护 **4 条跟踪赢家线**：

- `since_2017_01`：长窗口
- `since_2020_01`：中窗口
- `since_2023_01`：短窗口
- `since_2025_01`：超短窗口

另外还增加了一个 **`since_2026_01` 今年窗口**，但它只用于展示当前 4 个窗口赢家在今年以来的表现：

- 不单独评选新的 `2026-window winner`
- 不加入 tracked winners 保存逻辑
- 不加入 core active family 默认比较
- 只出现在 tracked-winners 对比图里，作为今年以来的附加观察窗

自动任务会把最新赢家和指标更新到下面这个区块：

<!-- AUTO:WEIGHTED-WINNERS:START -->

项目当前维护 **四条研究路线**：

- **Path 1（胜出者核心主线）**：渐进优化路线，目标是在保持当前 winner-core 框架可交易、可控回撤的前提下，把长期 CAGR 持续推向 `25%~30%+`。
- **Path 2（无约束上限探索）**：追求更高收益上限的独立路线，可以脱离当前框架自由试验；近期重点是优先把 `2020` 与 `2023` 两个窗口推向 `40%+ CAGR`。Path 2 会独立记录自己的窗口赢家与鲁棒候选，不需要先超过 Path 1 才更新。
- **Path 3（周度高频调仓）**：专门跟踪纯周度换股候选，和“月度选股 + 周度仓位 overlay”分开评估，用于观察更高交易频率是否能带来可持续优势。
- **Path 4（月频强主题涌现）**：观察型 tracked-only 路线，目标是在不显性贴行业标签的前提下捕捉强主题扩散；暂不直接进入正式实盘分配。

当前验证窗口：

- `since_2017_01`：长窗口
- `since_2020_01`：中窗口
- `since_2023_01`：短窗口
- `since_2025_01`：超短窗口
- `since_2026_01`：今年窗口（只用于展示当前四个窗口赢家今年以来表现，不单独评选 winner）

## Path 1：窗口跟踪赢家

### 2017 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`20.67%` / `0.8779` / `-24.73%` / `3.09`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `505.31%`, CAGR `20.67%`, Max DD `-24.73%`, Sharpe `0.8779`, Turnover `3.09`
- `2020-01-01` → `2026-07-21`: Total Return `390.98%`, CAGR `27.34%`, Max DD `-27.01%`, Sharpe `0.9567`, Turnover `3.36`
- `2023-01-01` → `2026-07-21`: Total Return `116.41%`, CAGR `24.04%`, Max DD `-26.68%`, Sharpe `0.7946`, Turnover `3.37`
- `2025-01-01` → `2026-07-21`: Total Return `126.40%`, CAGR `67.55%`, Max DD `-28.06%`, Sharpe `1.2692`, Turnover `4.78`
- `2026-01-01` → `2026-07-21`: Total Return `17.86%`, CAGR `32.53%`, Max DD `-29.04%`, Sharpe `0.7521`, Turnover `6.73`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`23.67%` / `0.8646` / `-20.45%` / `3.42`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `123.99%`, CAGR `8.78%`, Max DD `-32.48%`, Sharpe `0.5462`, Turnover `3.17`
- `2020-01-01` → `2026-07-21`: Total Return `7.34%`, CAGR `1.08%`, Max DD `-32.56%`, Sharpe `0.1479`, Turnover `2.79`
- `2023-01-01` → `2026-07-21`: Total Return `114.11%`, CAGR `23.67%`, Max DD `-20.45%`, Sharpe `0.8646`, Turnover `3.42`
- `2025-01-01` → `2026-07-21`: Total Return `85.31%`, CAGR `47.64%`, Max DD `-23.61%`, Sharpe `1.1526`, Turnover `4.87`
- `2026-01-01` → `2026-07-21`: Total Return `10.98%`, CAGR `19.55%`, Max DD `-16.72%`, Sharpe `0.6269`, Turnover `5.34`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`27.34%` / `0.9567` / `-27.01%` / `3.36`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `505.31%`, CAGR `20.67%`, Max DD `-24.73%`, Sharpe `0.8779`, Turnover `3.09`
- `2020-01-01` → `2026-07-21`: Total Return `390.98%`, CAGR `27.34%`, Max DD `-27.01%`, Sharpe `0.9567`, Turnover `3.36`
- `2023-01-01` → `2026-07-21`: Total Return `116.41%`, CAGR `24.04%`, Max DD `-26.68%`, Sharpe `0.7946`, Turnover `3.37`
- `2025-01-01` → `2026-07-21`: Total Return `126.40%`, CAGR `67.55%`, Max DD `-28.06%`, Sharpe `1.2692`, Turnover `4.78`
- `2026-01-01` → `2026-07-21`: Total Return `17.86%`, CAGR `32.53%`, Max DD `-29.04%`, Sharpe `0.7521`, Turnover `6.73`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`（核心80_探索20_总市值底座_胜出者核心__比例20/80(2+8 分步加仓62成本防守再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`73.25%` / `1.5113` / `-22.06%` / `4.43`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-07-17`: Total Return `304.43%`, CAGR `15.70%`, Max DD `-27.59%`, Sharpe `0.7083`, Turnover `2.71`
- `2020-01-01` → `2026-07-21`: Total Return `257.60%`, CAGR `21.36%`, Max DD `-24.96%`, Sharpe `0.7901`, Turnover `2.97`
- `2023-01-01` → `2026-07-21`: Total Return `114.48%`, CAGR `23.73%`, Max DD `-23.30%`, Sharpe `0.8034`, Turnover `2.93`
- `2025-01-01` → `2026-07-21`: Total Return `138.73%`, CAGR `73.25%`, Max DD `-22.06%`, Sharpe `1.5113`, Turnover `4.43`
- `2026-01-01` → `2026-07-21`: Total Return `20.31%`, CAGR `37.30%`, Max DD `-24.92%`, Sharpe `0.8092`, Turnover `5.32`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`34.90%` / `20.67%` / `0.9746` / `-28.06%` / `3.65`

窗口指标：

- `2017-01-01` → `2026-07-21`: Total Return `505.31%`, CAGR `20.67%`, Max DD `-24.73%`, Sharpe `0.8779`, Turnover `3.09`
- `2020-01-01` → `2026-07-21`: Total Return `390.98%`, CAGR `27.34%`, Max DD `-27.01%`, Sharpe `0.9567`, Turnover `3.36`
- `2023-01-01` → `2026-07-21`: Total Return `116.41%`, CAGR `24.04%`, Max DD `-26.68%`, Sharpe `0.7946`, Turnover `3.37`
- `2025-01-01` → `2026-07-21`: Total Return `126.40%`, CAGR `67.55%`, Max DD `-28.06%`, Sharpe `1.2692`, Turnover `4.78`
- `2026-01-01` → `2026-07-21`: Total Return `17.86%`, CAGR `32.53%`, Max DD `-29.04%`, Sharpe `0.7521`, Turnover `6.73`

## Path 1：组合方案

- 组合ID：`path1_composite_robust_window_blend_v1`
- 组合逻辑：不再要求单一 winner 覆盖所有行情，按鲁棒候选与窗口赢家合并权重。
- 组合鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`34.33%` / `19.71%` / `0.9827` / `-27.41%` / `3.62`

当前组合成分：

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）：`85.0%`；来源：robust-candidate, 2017-01, 2020-01
- `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）：`10.0%`；来源：2023-01
- `core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`（核心80_探索20_总市值底座_胜出者核心__比例20/80(2+8 分步加仓62成本防守再确认)）：`5.0%`；来源：2025-01

组合窗口指标：

- `2017-01-01` → `2026-07-21`: Total Return `457.13%`, CAGR `19.71%`, Max DD `-24.31%`, Sharpe `0.8783`, Turnover `3.08`
- `2020-01-01` → `2026-07-21`: Total Return `345.94%`, CAGR `25.63%`, Max DD `-26.61%`, Sharpe `0.9287`, Turnover `3.28`
- `2023-01-01` → `2026-07-21`: Total Return `116.08%`, CAGR `24.23%`, Max DD `-25.92%`, Sharpe `0.8176`, Turnover `3.35`
- `2025-01-01` → `2026-07-21`: Total Return `122.91%`, CAGR `67.75%`, Max DD `-27.41%`, Sharpe `1.3061`, Turnover `4.77`
- `2026-01-01` → `2026-07-21`: Total Return `17.29%`, CAGR `33.62%`, Max DD `-27.83%`, Sharpe `0.7652`, Turnover `6.52`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`8.78%` / `0.5462` / `-32.48%` / `3.17`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `123.99%`, CAGR `8.78%`, Max DD `-32.48%`, Sharpe `0.5462`, Turnover `3.17`
- `2020-01-01` → `2026-07-21`: Total Return `7.34%`, CAGR `1.08%`, Max DD `-32.56%`, Sharpe `0.1479`, Turnover `2.79`
- `2023-01-01` → `2026-07-21`: Total Return `114.11%`, CAGR `23.67%`, Max DD `-20.45%`, Sharpe `0.8646`, Turnover `3.42`
- `2025-01-01` → `2026-07-21`: Total Return `85.31%`, CAGR `47.64%`, Max DD `-23.61%`, Sharpe `1.1526`, Turnover `4.87`
- `2026-01-01` → `2026-07-21`: Total Return `10.98%`, CAGR `19.55%`, Max DD `-16.72%`, Sharpe `0.6269`, Turnover `5.34`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`23.67%` / `0.8646` / `-20.45%` / `3.42`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `123.99%`, CAGR `8.78%`, Max DD `-32.48%`, Sharpe `0.5462`, Turnover `3.17`
- `2020-01-01` → `2026-07-21`: Total Return `7.34%`, CAGR `1.08%`, Max DD `-32.56%`, Sharpe `0.1479`, Turnover `2.79`
- `2023-01-01` → `2026-07-21`: Total Return `114.11%`, CAGR `23.67%`, Max DD `-20.45%`, Sharpe `0.8646`, Turnover `3.42`
- `2025-01-01` → `2026-07-21`: Total Return `85.31%`, CAGR `47.64%`, Max DD `-23.61%`, Sharpe `1.1526`, Turnover `4.87`
- `2026-01-01` → `2026-07-21`: Total Return `10.98%`, CAGR `19.55%`, Max DD `-16.72%`, Sharpe `0.6269`, Turnover `5.34`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`1.08%` / `0.1479` / `-32.56%` / `2.79`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `123.99%`, CAGR `8.78%`, Max DD `-32.48%`, Sharpe `0.5462`, Turnover `3.17`
- `2020-01-01` → `2026-07-21`: Total Return `7.34%`, CAGR `1.08%`, Max DD `-32.56%`, Sharpe `0.1479`, Turnover `2.79`
- `2023-01-01` → `2026-07-21`: Total Return `114.11%`, CAGR `23.67%`, Max DD `-20.45%`, Sharpe `0.8646`, Turnover `3.42`
- `2025-01-01` → `2026-07-21`: Total Return `85.31%`, CAGR `47.64%`, Max DD `-23.61%`, Sharpe `1.1526`, Turnover `4.87`
- `2026-01-01` → `2026-07-21`: Total Return `10.98%`, CAGR `19.55%`, Max DD `-16.72%`, Sharpe `0.6269`, Turnover `5.34`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`47.64%` / `1.1526` / `-23.61%` / `4.87`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `123.99%`, CAGR `8.78%`, Max DD `-32.48%`, Sharpe `0.5462`, Turnover `3.17`
- `2020-01-01` → `2026-07-21`: Total Return `7.34%`, CAGR `1.08%`, Max DD `-32.56%`, Sharpe `0.1479`, Turnover `2.79`
- `2023-01-01` → `2026-07-21`: Total Return `114.11%`, CAGR `23.67%`, Max DD `-20.45%`, Sharpe `0.8646`, Turnover `3.42`
- `2025-01-01` → `2026-07-21`: Total Return `85.31%`, CAGR `47.64%`, Max DD `-23.61%`, Sharpe `1.1526`, Turnover `4.87`
- `2026-01-01` → `2026-07-21`: Total Return `10.98%`, CAGR `19.55%`, Max DD `-16.72%`, Sharpe `0.6269`, Turnover `5.34`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`20.29%` / `1.08%` / `0.6778` / `-32.56%` / `3.56`

窗口指标：

- `2017-01-01` → `2026-07-21`: Total Return `123.99%`, CAGR `8.78%`, Max DD `-32.48%`, Sharpe `0.5462`, Turnover `3.17`
- `2020-01-01` → `2026-07-21`: Total Return `7.34%`, CAGR `1.08%`, Max DD `-32.56%`, Sharpe `0.1479`, Turnover `2.79`
- `2023-01-01` → `2026-07-21`: Total Return `114.11%`, CAGR `23.67%`, Max DD `-20.45%`, Sharpe `0.8646`, Turnover `3.42`
- `2025-01-01` → `2026-07-21`: Total Return `85.31%`, CAGR `47.64%`, Max DD `-23.61%`, Sharpe `1.1526`, Turnover `4.87`
- `2026-01-01` → `2026-07-21`: Total Return `10.98%`, CAGR `19.55%`, Max DD `-16.72%`, Sharpe `0.6269`, Turnover `5.34`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(周频出场缓冲v3, 熊市12%, 单票46%, 持有6周, 换手4%, 出场90%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`10.43%` / `0.7146` / `-20.43%` / `1.17`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `154.15%`, CAGR `10.43%`, Max DD `-20.43%`, Sharpe `0.7146`, Turnover `1.17`
- `2020-01-01` → `2026-07-21`: Total Return `121.97%`, CAGR `13.13%`, Max DD `-27.09%`, Sharpe `0.7242`, Turnover `0.98`
- `2023-01-01` → `2026-07-21`: Total Return `18.68%`, CAGR `5.02%`, Max DD `-19.12%`, Sharpe `0.3827`, Turnover `0.59`
- `2025-01-01` → `2026-07-21`: Total Return `29.81%`, CAGR `18.23%`, Max DD `-19.22%`, Sharpe `0.6720`, Turnover `2.25`
- `2026-01-01` → `2026-07-21`: Total Return `2.97%`, CAGR `5.59%`, Max DD `-23.24%`, Sharpe `0.3394`, Turnover `3.46`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心70_探索30_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`27.12%` / `0.6907` / `-36.07%` / `11.84`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(周频出场缓冲v3, 熊市12%, 单票46%, 持有6周, 换手4%, 出场90%)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`5.02%` / `0.3827` / `-19.12%` / `0.59`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-07-17`: Total Return `530.72%`, CAGR `21.68%`, Max DD `-50.80%`, Sharpe `0.6549`, Turnover `9.31`
- `2020-01-01` → `2026-07-21`: Total Return `48.05%`, CAGR `6.26%`, Max DD `-54.41%`, Sharpe `0.3465`, Turnover `10.93`
- `2023-01-01` → `2026-07-21`: Total Return `131.62%`, CAGR `27.12%`, Max DD `-36.07%`, Sharpe `0.6907`, Turnover `11.84`
- `2025-01-01` → `2026-07-21`: Total Return `284.28%`, CAGR `137.32%`, Max DD `-35.90%`, Sharpe `1.4742`, Turnover `18.68`
- `2026-01-01` → `2026-07-21`: Total Return `44.92%`, CAGR `99.18%`, Max DD `-46.76%`, Sharpe `1.2761`, Turnover `24.69`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.33%` / `0.6684` / `-27.46%` / `1.89`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(周频出场缓冲v3, 熊市12%, 单票46%, 持有6周, 换手4%, 出场90%)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`13.13%` / `0.7242` / `-27.09%` / `0.98`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-07-21`: Total Return `131.33%`, CAGR `9.33%`, Max DD `-32.55%`, Sharpe `0.5650`, Turnover `2.21`
- `2020-01-01` → `2026-07-21`: Total Return `124.44%`, CAGR `13.33%`, Max DD `-27.46%`, Sharpe `0.6684`, Turnover `1.89`
- `2023-01-01` → `2026-07-21`: Total Return `54.10%`, CAGR `13.15%`, Max DD `-29.36%`, Sharpe `0.6165`, Turnover `1.85`
- `2025-01-01` → `2026-07-21`: Total Return `60.30%`, CAGR `35.38%`, Max DD `-37.36%`, Sharpe `1.0065`, Turnover `3.76`
- `2026-01-01` → `2026-07-21`: Total Return `-1.83%`, CAGR `-3.37%`, Max DD `-31.33%`, Sharpe `0.1409`, Turnover `4.87`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心70_探索30_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`137.32%` / `1.4742` / `-35.90%` / `18.68`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`234.38%` / `1.8551` / `-41.25%` / `15.68`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-07-22`: Total Return `478.41%`, CAGR `20.52%`, Max DD `-50.80%`, Sharpe `0.6321`, Turnover `9.34`
- `2020-01-01` → `2026-07-22`: Total Return `48.05%`, CAGR `6.26%`, Max DD `-54.41%`, Sharpe `0.3465`, Turnover `10.93`
- `2023-01-01` → `2026-07-22`: Total Return `131.62%`, CAGR `27.12%`, Max DD `-36.07%`, Sharpe `0.6907`, Turnover `11.84`
- `2025-01-01` → `2026-07-22`: Total Return `284.28%`, CAGR `137.32%`, Max DD `-35.90%`, Sharpe `1.4742`, Turnover `18.68`
- `2026-01-01` → `2026-07-22`: Total Return `44.92%`, CAGR `99.18%`, Max DD `-46.76%`, Sharpe `1.2761`, Turnover `24.69`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市14%, 单票46%, 持有7周, 换手3%, 出场98%, 单周换手修复)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`13.51%` / `4.18%` / `0.7491` / `-27.82%` / `0.63`

窗口指标：

- `2017-01-01` → `2026-07-22`: Total Return `47.03%`, CAGR `4.18%`, Max DD `-22.92%`, Sharpe `0.4458`, Turnover `0.80`
- `2020-01-01` → `2026-07-22`: Total Return `61.24%`, CAGR `7.67%`, Max DD `-27.82%`, Sharpe `0.5411`, Turnover `0.66`
- `2023-01-01` → `2026-07-22`: Total Return `35.36%`, CAGR `9.04%`, Max DD `-11.72%`, Sharpe `0.8103`, Turnover `0.47`
- `2025-01-01` → `2026-07-22`: Total Return `56.23%`, CAGR `33.16%`, Max DD `-14.74%`, Sharpe `1.1993`, Turnover `0.58`
- `2026-01-01` → `2026-07-22`: Total Return `20.28%`, CAGR `40.91%`, Max DD `-23.67%`, Sharpe `0.9655`, Turnover `2.71`

## Path 4：窗口跟踪赢家（观察）

### 2017 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市8%, 单票5%, 出场68%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`10.06%` / `0.6399` / `-22.98%` / `3.21`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-07-22`: Total Return `150.58%`, CAGR `10.06%`, Max DD `-22.98%`, Sharpe `0.6399`, Turnover `3.21`
- `2020-01-01` → `2026-07-22`: Total Return `49.01%`, CAGR `6.25%`, Max DD `-23.82%`, Sharpe `0.4045`, Turnover `3.28`
- `2023-01-01` → `2026-07-22`: Total Return `21.72%`, CAGR `5.64%`, Max DD `-24.23%`, Sharpe `0.3776`, Turnover `3.04`
- `2025-01-01` → `2026-07-22`: Total Return `45.29%`, CAGR `26.61%`, Max DD `-24.87%`, Sharpe `0.8585`, Turnover `5.68`
- `2026-01-01` → `2026-07-22`: Total Return `1.50%`, CAGR `2.59%`, Max DD `-24.28%`, Sharpe `0.2777`, Turnover `5.74`

### 2023 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升23只(强主题涌现容量v2, 信号29%, 龙头78%, 熊市4%, 单票4%, 出场72%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`4.60%` / `0.3633` / `-19.35%` / `2.43`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-07-22`: Total Return `86.63%`, CAGR `6.73%`, Max DD `-19.54%`, Sharpe `0.5272`, Turnover `2.55`
- `2020-01-01` → `2026-07-22`: Total Return `50.85%`, CAGR `6.44%`, Max DD `-19.54%`, Sharpe `0.4627`, Turnover `2.61`
- `2023-01-01` → `2026-07-22`: Total Return `17.48%`, CAGR `4.60%`, Max DD `-19.35%`, Sharpe `0.3633`, Turnover `2.43`
- `2025-01-01` → `2026-07-22`: Total Return `39.92%`, CAGR `23.63%`, Max DD `-19.45%`, Sharpe `0.9038`, Turnover `4.48`
- `2026-01-01` → `2026-07-22`: Total Return `3.84%`, CAGR `6.68%`, Max DD `-19.28%`, Sharpe `0.3423`, Turnover `4.52`

### 2020 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升23只(强主题涌现容量v2, 信号29%, 龙头78%, 熊市4%, 单票4%, 出场72%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`6.44%` / `0.4627` / `-19.54%` / `2.61`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-07-22`: Total Return `86.63%`, CAGR `6.73%`, Max DD `-19.54%`, Sharpe `0.5272`, Turnover `2.55`
- `2020-01-01` → `2026-07-22`: Total Return `50.85%`, CAGR `6.44%`, Max DD `-19.54%`, Sharpe `0.4627`, Turnover `2.61`
- `2023-01-01` → `2026-07-22`: Total Return `17.48%`, CAGR `4.60%`, Max DD `-19.35%`, Sharpe `0.3633`, Turnover `2.43`
- `2025-01-01` → `2026-07-22`: Total Return `39.92%`, CAGR `23.63%`, Max DD `-19.45%`, Sharpe `0.9038`, Turnover `4.48`
- `2026-01-01` → `2026-07-22`: Total Return `3.84%`, CAGR `6.68%`, Max DD `-19.28%`, Sharpe `0.3423`, Turnover `4.52`

### 2025 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`32.58%` / `0.9259` / `-27.15%` / `6.23`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-07-22`: Total Return `146.15%`, CAGR `9.86%`, Max DD `-27.12%`, Sharpe `0.5719`, Turnover `3.60`
- `2020-01-01` → `2026-07-22`: Total Return `85.05%`, CAGR `9.80%`, Max DD `-27.12%`, Sharpe `0.5236`, Turnover `3.65`
- `2023-01-01` → `2026-07-22`: Total Return `13.36%`, CAGR `3.56%`, Max DD `-24.34%`, Sharpe `0.2997`, Turnover `3.24`
- `2025-01-01` → `2026-07-22`: Total Return `56.28%`, CAGR `32.58%`, Max DD `-27.15%`, Sharpe `0.9259`, Turnover `6.23`
- `2026-01-01` → `2026-07-22`: Total Return `4.31%`, CAGR `7.50%`, Max DD `-26.13%`, Sharpe `0.3832`, Turnover `6.40`

## Path 4：鲁棒候选（观察）

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升23只(强主题涌现容量v2, 信号29%, 龙头78%, 熊市4%, 单票4%, 出场72%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`10.35%` / `4.60%` / `0.5643` / `-19.54%` / `3.02`

窗口指标：

- `2017-01-01` → `2026-07-22`: Total Return `86.63%`, CAGR `6.73%`, Max DD `-19.54%`, Sharpe `0.5272`, Turnover `2.55`
- `2020-01-01` → `2026-07-22`: Total Return `50.85%`, CAGR `6.44%`, Max DD `-19.54%`, Sharpe `0.4627`, Turnover `2.61`
- `2023-01-01` → `2026-07-22`: Total Return `17.48%`, CAGR `4.60%`, Max DD `-19.35%`, Sharpe `0.3633`, Turnover `2.43`
- `2025-01-01` → `2026-07-22`: Total Return `39.92%`, CAGR `23.63%`, Max DD `-19.45%`, Sharpe `0.9038`, Turnover `4.48`
- `2026-01-01` → `2026-07-22`: Total Return `3.84%`, CAGR `6.68%`, Max DD `-19.28%`, Sharpe `0.3423`, Turnover `4.52`

<!-- AUTO:WEIGHTED-WINNERS:END -->

当不同窗口的赢家不同时，项目会同时保留它们，作为防过拟合的护栏。README 中的 `strategy_comparison_*` 图展示跟踪赢家，`strategy_family_*` 图现在只展示默认参与展示的 **core active family**。更宽的 **research active family** 仍继续参与回测与迭代，用于保留更大的候选范围；历史实验策略会保留在 `results/` 中作为 **archive family** 供追溯，但默认不再进入 README、默认图表和默认比较脚本。

A 股各路径在四个窗口下的赢家变化历史，持续记录在：

- [HISTORY.md](HISTORY.md)
- [docs/path1_plan.md](docs/path1_plan.md)
- [docs/path2_plan.md](docs/path2_plan.md)

## 沪港通独立研究线

沪港通结果独立维护，不并入 A 股 `winner_only` 结论。`2026-04-22` 起，港股窗口的 `sample_start` 统一对齐到**首个可执行调仓点**，因此本节数值应以这次重算后的基线为准。

当前 tracked winners（市场数据截止 `2026-05-22`；tracked payload `as_of=2026-05-22`；月频/双周信号生效日多为 `2026-04-30`，周频信号生效日可到 `2026-05-22`，信号生效日仍按各策略真实评估点生成）：

当前港股各窗口都从各自首个可执行调仓点起算；月频/双周 Path 1/2 当前信号样本多截止 `2026-04-30`，周频 Path 3 当前信号样本可到 `2026-05-15`。

三条研究路径按如下口径维护：

- **Path 1：实盘稳健线**，保留月度/双周稳健候选，后续主攻“月度调仓 + 周度风控/卫星”。
- **Path 2：收益上限探索线**，保留月度/双周高收益候选，继续探索主题、突破、高集中与高弹性结构。
- **Path 3：纯周度调仓线**，只纳入周度信号、周度换股候选，单独评估高频交易价值。

- Path 1：
  - `since_2017_01`：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36`
  - `since_2020_01`：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`
  - `since_2023_01`：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`
  - `since_2025_01`：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard`
  - robust candidate：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36`
- Path 2：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly_cost_control`
  - `since_2023_01`：`hkconnect_path2_theme_monthly`
  - `since_2025_01`：`hkconnect_path2_breakout_concentrated_monthly`
  - robust candidate：`hkconnect_path2_theme_monthly_cost_control`
- Path 3：
  - `since_2017_01`：`hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`
  - `since_2020_01`：`hkconnect_path3_theme_fast_weekly_buffered`
  - `since_2023_01`：`hkconnect_path3_theme_fast_weekly_buffered`
  - `since_2025_01`：`hkconnect_path3_theme_fast_weekly_turnover_guard`
  - robust candidate：`hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`
- `since_2026_01`：只做观察，不进入 tracked winners；当前 raw leader 分别是 `hkconnect_path1_biweekly_cashoff`（Path 1）、`hkconnect_path2_breakout_concentrated_monthly`（Path 2）与 `hkconnect_path3_equal_elastic_cashoff_weekly`（Path 3）

关键窗口指标：

- Path 1 `since_2020_01`：`32.33% CAGR / -14.83% MaxDD / 1.5504 Sharpe / 3.40 Turnover`（`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`）
- Path 1 `since_2023_01`：`34.60% CAGR / -14.83% MaxDD / 1.7299 Sharpe / 3.13 Turnover`（`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`）
- Path 1 `since_2025_01`：`42.95% CAGR / -13.36% MaxDD / 1.6581 Sharpe / 3.45 Turnover`（`hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard`）
- Path 2 `since_2020_01`：`29.86% CAGR / -19.10% MaxDD / 1.1680 Sharpe / 5.65 Turnover`（`hkconnect_path2_theme_monthly_cost_control`）
- Path 2 `since_2023_01`：`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`（`hkconnect_path2_theme_monthly`）
- Path 2 `since_2025_01`：`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`（`hkconnect_path2_breakout_concentrated_monthly`）
- Path 3 `since_2020_01`：`26.55% CAGR / -34.43% MaxDD / 0.8906 Sharpe / 30.99 Turnover`（`hkconnect_path3_theme_fast_weekly_buffered`）
- Path 3 `since_2023_01`：`38.42% CAGR / -19.56% MaxDD / 1.2564 Sharpe / 29.76 Turnover`（`hkconnect_path3_theme_fast_weekly_buffered`）
- Path 3 `since_2025_01`：`70.38% CAGR / -13.25% MaxDD / 1.8766 Sharpe / 32.03 Turnover`（`hkconnect_path3_theme_fast_weekly_turnover_guard`）

相关产物：

- [docs/path1_plan_hkconnect.md](docs/path1_plan_hkconnect.md)
- [docs/path2_plan_hkconnect.md](docs/path2_plan_hkconnect.md)
- [docs/path3_plan_hkconnect.md](docs/path3_plan_hkconnect.md)
- [results/research/hkconnect/tracked_winners_hkconnect.json](results/research/hkconnect/tracked_winners_hkconnect.json)

![HK Connect Path1 Comparison](docs/strategy_comparison_hkconnect_path1.png)

![HK Connect Path2 Comparison](docs/strategy_comparison_hkconnect_path2.png)

![HK Connect Path3 Comparison](docs/strategy_comparison_hkconnect_path3.png)

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

README 中间这部分只解释当前研究框架，不重复写死顶部自动区块里的最新数值。

当前项目已经从“只追一个总冠军策略”，演进成 **三条研究路径 + 四个验证窗口**：

- **Path 1：渐进优化路径**
  - 仍然基于 `winner_core` 主线持续优化
  - 目标是在可交易、可控回撤的前提下，把现阶段常见的 `20%~26% CAGR` 推向 `25%~30%+`
  - 重点关注：晋升机制、核心/卫星结构、仓位节奏、系统风控
  - 当前已经增加了显式研究计划文件：[docs/path1_plan.md](docs/path1_plan.md)
  - 后续迭代应优先围绕计划文件中定义的 `3-5` 个方向推进，而不是无差别扫全部历史变体

- **Path 2：无约束上限探索**
  - 不受当前框架限制，可以尝试更激进或完全不同的方案
  - 目标优先冲收益上限，近期重点是先把 `2020` 和 `2023` 两个窗口推向 `40%+ CAGR`
  - 这条路径会独立记录自己的窗口赢家与鲁棒候选，不需要先打赢 Path 1 才保留
  - 当前也已经增加显式研究计划文件：[docs/path2_plan.md](docs/path2_plan.md)
  - 当前已开始独立候选生成，重点拆成三类方向：
    - 高集中突破
    - 高成长主线
    - 动量 / 等权高弹性

- **Path 3：周度高频调仓**
  - 专门跟踪纯周度换股候选，不和“月度选股 + 周度仓位 overlay”混在同一条线里
  - 目标是评估更高交易频率是否能形成可持续优势，同时单独观察换手和回撤代价
  - 当前会独立记录四窗口赢家与四窗口鲁棒候选

四个验证窗口分别是：

- `2017-01 起`：长窗口，检验跨牛熊长期稳定性
- `2020-01 起`：中窗口，当前最重要的主比较窗口
- `2023-01 起`：短窗口，检验近年行情适应性
- `2025-01 起`：超短窗口，检验最新市场环境下的爆发力

### 当前主框架

目前项目的主框架仍然是：

- 动态股票池，而不是固定后视镜冠军池
- `核心 / 探索 / 种子` 三层结构，负责“发现 -> 验证 -> 放大”
- `winner_core` 负责把探索层跑出来的强者逐步提升为核心重仓
- 真实计入佣金、印花税和调仓成本

核心资产的发现逻辑，当前更强调：

- 中期动量与短期回避
- 行业强度与行业内龙头强度
- 业绩加速与质量过滤
- 晋升核心后的分阶段加仓

### Active Family 与 Archive Family

当前项目不再把“历史上试过的所有策略”都混在默认比较里，而是分成两层：

- **active family**
  - 当前仍在持续研究、会进入 README 默认展示和默认图表的策略集合
  - 目前主要集中在 `核心80_探索20` 的 `index_core / winner_core` 主线，以及其现役卫星风控变体

- **archive family**
  - 历史上做过、但当前不再作为默认比较对象的旧策略
  - 结果仍保留在 `results/` 中方便追溯
  - 默认不会再进入 README 顶部摘要、默认图表和默认比较脚本

这样做的目的，是把当前真正还在竞争的策略与历史试验策略隔离开，避免 README 和图表被旧版本噪音干扰。

### 结果对比图

下面四张图分别展示：

- `2017-01 起` 长样本
- `2020-01 起` 中样本
- `2023-01 起` 短样本
- `2025-01 起` 超短样本
- `2026-01 起` 今年窗口（只展示当前四个窗口赢家、基准和静态参考的今年表现）

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

#### 2026-01 起（今年窗口，仅 tracked winners）

![Strategy Comparison Since 2026-01](docs/strategy_comparison_since_2026_01.png)

### Core Active Family 对比图

下面四张图只展示当前默认参与展示的 **core active family**。  
更宽的 **research active family** 仍然继续跑，用于给自动迭代提供更大的候选空间；已经淘汰的旧策略则保留在 `results/` 中作为 archive family，默认不再出现在这里。

#### 2017-01 起（core active family）

![Strategy Family Since 2017-01](docs/strategy_family_since_2017_01.png)

#### 2020-01 起（core active family）

![Strategy Family Since 2020-01](docs/strategy_family_since_2020_01.png)

#### 2023-01 起（core active family）

![Strategy Family Since 2023-01](docs/strategy_family_since_2023_01.png)

#### 2025-01 起（core active family）

![Strategy Family Since 2025-01](docs/strategy_family_since_2025_01.png)

## 实盘交易平台（MVP）

项目当前已经同步搭建了一个可用于日常实盘操作的网页平台，定位是：

- 单用户
- 多账户
- 策略白名单只来自 tracked winners
- 人工执行调仓，不直接对接券商交易接口
- 研究端低频更新，实盘端日频查看与执行

当前实盘平台主程序：

- [live_trading_platform.py](live_trading_platform.py)
- [scripts/export_live_platform_data.py](scripts/export_live_platform_data.py)

### 当前已支持的能力

- 展示 tracked winners 白名单策略
- 单用户、多账户管理
- 账户绑定策略
- 手工输入 / 编辑当前持仓
- 自动拉取当前价格
  - 交易时间优先分钟线实时价
  - 非交易时间显示上一交易日收盘价
- 展示当前持仓盈亏、账户总盈亏、账户总盈亏率
- 生成正式调仓单与偏离修正单
- 任务页逐笔录入实际成交
- 当累计成交与建议股数一致时自动标记任务为已执行
- 交易流水记录
  - 实际成交
  - 估算执行
  - 手工持仓同步
  - 手工新增 / 编辑交易

### 当前实盘平台的使用方式

1. 研究端先导出可实盘策略快照
2. 在实盘平台中创建账户并绑定某个 tracked winner 策略
3. 手工录入当前账户持仓
4. 每天查看今日建议
   - 正式调仓
   - 偏离修正
   - 策略切换建议
   - 无需操作
5. 生成任务单并人工去券商执行
6. 在任务页逐笔录入实际成交，平台自动回写账户

### 启动方式

```bash
cd /Users/valselee/my-code/aiinvestor
.venv/bin/python scripts/export_live_platform_data.py
.venv/bin/python live_trading_platform.py
```

浏览器打开：

- [http://127.0.0.1:8787](http://127.0.0.1:8787)

### 当前定位

这套平台当前仍然是 **Stage 1：研究结果到人工执行之间的操作平台**。

也就是说：

- 平台负责生成建议与任务
- 你负责实际下单
- 平台负责回写与留痕

后续如果需要，再继续往 CSV 导入、券商接口对接、自动执行等方向扩展。
