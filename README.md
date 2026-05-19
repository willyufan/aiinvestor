# aiinvestor

一个基于 Tushare Pro 的 A 股与沪港通组合回测、策略迭代项目。

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

项目当前维护 **三条研究路线**：

- **Path 1（胜出者核心主线）**：渐进优化路线，目标是在保持当前 winner-core 框架可交易、可控回撤的前提下，把长期 CAGR 持续推向 `25%~30%+`。
- **Path 2（无约束上限探索）**：追求更高收益上限的独立路线，可以脱离当前框架自由试验；近期重点是优先把 `2020` 与 `2023` 两个窗口推向 `40%+ CAGR`。Path 2 会独立记录自己的窗口赢家与鲁棒候选，不需要先超过 Path 1 才更新。
- **Path 3（周度高频调仓）**：专门跟踪纯周度换股候选，和“月度选股 + 周度仓位 overlay”分开评估，用于观察更高交易频率是否能带来可持续优势。

当前验证窗口：

- `since_2017_01`：长窗口
- `since_2020_01`：中窗口
- `since_2023_01`：短窗口
- `since_2025_01`：超短窗口
- `since_2026_01`：今年窗口（只用于展示当前四个窗口赢家今年以来表现，不单独评选 winner）

## Path 1：窗口跟踪赢家

### 2017 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered_asym13`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(快减1慢加3)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`26.83%` / `1.0355` / `-25.68%` / `3.81`

窗口指标（截至 `2026-05-19`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `837.58%`, CAGR `26.83%`, Max DD `-25.68%`, Sharpe `1.0355`, Turnover `3.81`
- `2020-01-01` → `2026-05-19`: Total Return `337.39%`, CAGR `25.86%`, Max DD `-27.44%`, Sharpe `0.8979`, Turnover `3.76`
- `2023-01-01` → `2026-05-19`: Total Return `154.40%`, CAGR `31.43%`, Max DD `-28.72%`, Sharpe `0.9564`, Turnover `4.09`
- `2025-01-01` → `2026-05-19`: Total Return `162.66%`, CAGR `97.72%`, Max DD `-10.72%`, Sharpe `1.9747`, Turnover `4.78`
- `2026-01-01` → `2026-05-19`: Total Return `26.81%`, CAGR `76.83%`, Max DD `-11.85%`, Sharpe `1.7216`, Turnover `7.12`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`27.00%` / `0.9051` / `-27.88%` / `2.98`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_balanced__sat_weekly_risk`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(多因子均衡)__卫星周频两档风控）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`33.80%` / `1.0727` / `-29.84%` / `3.64`

窗口指标（截至 `2026-05-19`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `550.41%`, CAGR `22.00%`, Max DD `-25.40%`, Sharpe `0.9456`, Turnover `2.52`
- `2020-01-01` → `2026-05-19`: Total Return `338.35%`, CAGR `25.90%`, Max DD `-25.19%`, Sharpe `0.9808`, Turnover `2.85`
- `2023-01-01` → `2026-05-19`: Total Return `126.31%`, CAGR `27.00%`, Max DD `-27.88%`, Sharpe `0.9051`, Turnover `2.98`
- `2025-01-01` → `2026-05-19`: Total Return `153.03%`, CAGR `92.57%`, Max DD `-11.78%`, Sharpe `2.0634`, Turnover `4.41`
- `2026-01-01` → `2026-05-19`: Total Return `22.92%`, CAGR `64.10%`, Max DD `-9.85%`, Sharpe `1.7006`, Turnover `6.76`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只__卫星周频三档风控(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`28.92%` / `1.0055` / `-31.00%` / `3.45`

窗口指标（截至 `2026-05-19`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `544.53%`, CAGR `21.88%`, Max DD `-25.68%`, Sharpe `0.9054`, Turnover `2.93`
- `2020-01-01` → `2026-05-19`: Total Return `410.40%`, CAGR `28.92%`, Max DD `-31.00%`, Sharpe `1.0055`, Turnover `3.45`
- `2023-01-01` → `2026-05-19`: Total Return `131.17%`, CAGR `27.80%`, Max DD `-29.28%`, Sharpe `0.8927`, Turnover `3.58`
- `2025-01-01` → `2026-05-19`: Total Return `143.27%`, CAGR `87.30%`, Max DD `-11.78%`, Sharpe `1.8249`, Turnover `4.77`
- `2026-01-01` → `2026-05-19`: Total Return `26.48%`, CAGR `75.72%`, Max DD `-6.83%`, Sharpe `2.1318`, Turnover `8.14`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`98.58%` / `2.1665` / `-10.24%` / `4.34`

窗口指标（截至 `2026-05-19`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `595.65%`, CAGR `22.87%`, Max DD `-24.00%`, Sharpe `0.9627`, Turnover `2.64`
- `2020-01-01` → `2026-05-19`: Total Return `342.69%`, CAGR `26.09%`, Max DD `-21.85%`, Sharpe `0.9418`, Turnover `2.89`
- `2023-01-01` → `2026-05-19`: Total Return `141.03%`, CAGR `29.37%`, Max DD `-28.64%`, Sharpe `0.9490`, Turnover `3.01`
- `2025-01-01` → `2026-05-19`: Total Return `164.29%`, CAGR `98.58%`, Max DD `-10.24%`, Sharpe `2.1665`, Turnover `4.34`
- `2026-01-01` → `2026-05-19`: Total Return `20.59%`, CAGR `56.73%`, Max DD `-12.30%`, Sharpe `1.4542`, Turnover `6.08`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered_asym13`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(快减1慢加3)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`45.46%` / `25.86%` / `1.2162` / `-28.72%` / `4.11`

窗口指标：

- `2017-01-01` → `2026-05-19`: Total Return `837.58%`, CAGR `26.83%`, Max DD `-25.68%`, Sharpe `1.0355`, Turnover `3.81`
- `2020-01-01` → `2026-05-19`: Total Return `337.39%`, CAGR `25.86%`, Max DD `-27.44%`, Sharpe `0.8979`, Turnover `3.76`
- `2023-01-01` → `2026-05-19`: Total Return `154.40%`, CAGR `31.43%`, Max DD `-28.72%`, Sharpe `0.9564`, Turnover `4.09`
- `2025-01-01` → `2026-05-19`: Total Return `162.66%`, CAGR `97.72%`, Max DD `-10.72%`, Sharpe `1.9747`, Turnover `4.78`
- `2026-01-01` → `2026-05-19`: Total Return `26.81%`, CAGR `76.83%`, Max DD `-11.85%`, Sharpe `1.7216`, Turnover `7.12`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`22.00%` / `0.9456` / `-25.40%` / `2.52`

窗口指标（截至 `2026-05-19`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `550.41%`, CAGR `22.00%`, Max DD `-25.40%`, Sharpe `0.9456`, Turnover `2.52`
- `2020-01-01` → `2026-05-19`: Total Return `338.35%`, CAGR `25.90%`, Max DD `-25.19%`, Sharpe `0.9808`, Turnover `2.85`
- `2023-01-01` → `2026-05-19`: Total Return `126.31%`, CAGR `27.00%`, Max DD `-27.88%`, Sharpe `0.9051`, Turnover `2.98`
- `2025-01-01` → `2026-05-19`: Total Return `153.03%`, CAGR `92.57%`, Max DD `-11.78%`, Sharpe `2.0634`, Turnover `4.41`
- `2026-01-01` → `2026-05-19`: Total Return `22.92%`, CAGR `64.10%`, Max DD `-9.85%`, Sharpe `1.7006`, Turnover `6.76`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_10_90_prom6_core_multifactor_balanced`（核心80_探索20_等权底座_胜出者核心__进攻10/90 晋升6只(多因子均衡)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`29.80%` / `1.0120` / `-31.09%` / `3.88`

窗口指标（截至 `2026-05-19`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `248.88%`, CAGR `14.19%`, Max DD `-48.39%`, Sharpe `0.7216`, Turnover `3.25`
- `2020-01-01` → `2026-05-19`: Total Return `191.53%`, CAGR `18.15%`, Max DD `-41.38%`, Sharpe `0.7564`, Turnover `3.59`
- `2023-01-01` → `2026-05-19`: Total Return `143.77%`, CAGR `29.80%`, Max DD `-31.09%`, Sharpe `1.0120`, Turnover `3.88`
- `2025-01-01` → `2026-05-19`: Total Return `136.41%`, CAGR `83.56%`, Max DD `-13.14%`, Sharpe `1.8103`, Turnover `5.69`
- `2026-01-01` → `2026-05-19`: Total Return `25.05%`, CAGR `71.01%`, Max DD `-13.54%`, Sharpe `1.6226`, Turnover `7.15`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`25.90%` / `0.9808` / `-25.19%` / `2.85`

窗口指标（截至 `2026-05-19`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `550.41%`, CAGR `22.00%`, Max DD `-25.40%`, Sharpe `0.9456`, Turnover `2.52`
- `2020-01-01` → `2026-05-19`: Total Return `338.35%`, CAGR `25.90%`, Max DD `-25.19%`, Sharpe `0.9808`, Turnover `2.85`
- `2023-01-01` → `2026-05-19`: Total Return `126.31%`, CAGR `27.00%`, Max DD `-27.88%`, Sharpe `0.9051`, Turnover `2.98`
- `2025-01-01` → `2026-05-19`: Total Return `153.03%`, CAGR `92.57%`, Max DD `-11.78%`, Sharpe `2.0634`, Turnover `4.41`
- `2026-01-01` → `2026-05-19`: Total Return `22.92%`, CAGR `64.10%`, Max DD `-9.85%`, Sharpe `1.7006`, Turnover `6.76`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`92.57%` / `2.0634` / `-11.78%` / `4.41`

窗口指标（截至 `2026-05-19`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `550.41%`, CAGR `22.00%`, Max DD `-25.40%`, Sharpe `0.9456`, Turnover `2.52`
- `2020-01-01` → `2026-05-19`: Total Return `338.35%`, CAGR `25.90%`, Max DD `-25.19%`, Sharpe `0.9808`, Turnover `2.85`
- `2023-01-01` → `2026-05-19`: Total Return `126.31%`, CAGR `27.00%`, Max DD `-27.88%`, Sharpe `0.9051`, Turnover `2.98`
- `2025-01-01` → `2026-05-19`: Total Return `153.03%`, CAGR `92.57%`, Max DD `-11.78%`, Sharpe `2.0634`, Turnover `4.41`
- `2026-01-01` → `2026-05-19`: Total Return `22.92%`, CAGR `64.10%`, Max DD `-9.85%`, Sharpe `1.7006`, Turnover `6.76`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`41.87%` / `22.00%` / `1.2237` / `-27.88%` / `3.19`

窗口指标：

- `2017-01-01` → `2026-05-19`: Total Return `550.41%`, CAGR `22.00%`, Max DD `-25.40%`, Sharpe `0.9456`, Turnover `2.52`
- `2020-01-01` → `2026-05-19`: Total Return `338.35%`, CAGR `25.90%`, Max DD `-25.19%`, Sharpe `0.9808`, Turnover `2.85`
- `2023-01-01` → `2026-05-19`: Total Return `126.31%`, CAGR `27.00%`, Max DD `-27.88%`, Sharpe `0.9051`, Turnover `2.98`
- `2025-01-01` → `2026-05-19`: Total Return `153.03%`, CAGR `92.57%`, Max DD `-11.78%`, Sharpe `2.0634`, Turnover `4.41`
- `2026-01-01` → `2026-05-19`: Total Return `22.92%`, CAGR `64.10%`, Max DD `-9.85%`, Sharpe `1.7006`, Turnover `6.76`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有6周, 换手12%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`11.10%` / `0.5455` / `-35.13%` / `3.26`

窗口指标（截至 `2026-05-19`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `164.15%`, CAGR `11.10%`, Max DD `-35.13%`, Sharpe `0.5455`, Turnover `3.26`
- `2020-01-01` → `2026-05-19`: Total Return `156.33%`, CAGR `16.15%`, Max DD `-27.90%`, Sharpe `0.6308`, Turnover `3.59`
- `2023-01-01` → `2026-05-19`: Total Return `79.91%`, CAGR `19.31%`, Max DD `-30.35%`, Sharpe `0.7172`, Turnover `2.81`
- `2025-01-01` → `2026-05-19`: Total Return `71.86%`, CAGR `47.86%`, Max DD `-24.52%`, Sharpe `1.0451`, Turnover `7.68`
- `2026-01-01` → `2026-05-19`: Total Return `-2.18%`, CAGR `-5.86%`, Max DD `-15.09%`, Sharpe `0.0444`, Turnover `9.80`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有6周, 换手12%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`19.31%` / `0.7172` / `-30.35%` / `2.81`

窗口指标（截至 `2026-05-19`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `164.15%`, CAGR `11.10%`, Max DD `-35.13%`, Sharpe `0.5455`, Turnover `3.26`
- `2020-01-01` → `2026-05-19`: Total Return `156.33%`, CAGR `16.15%`, Max DD `-27.90%`, Sharpe `0.6308`, Turnover `3.59`
- `2023-01-01` → `2026-05-19`: Total Return `79.91%`, CAGR `19.31%`, Max DD `-30.35%`, Sharpe `0.7172`, Turnover `2.81`
- `2025-01-01` → `2026-05-19`: Total Return `71.86%`, CAGR `47.86%`, Max DD `-24.52%`, Sharpe `1.0451`, Turnover `7.68`
- `2026-01-01` → `2026-05-19`: Total Return `-2.18%`, CAGR `-5.86%`, Max DD `-15.09%`, Sharpe `0.0444`, Turnover `9.80`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有6周, 换手12%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`16.15%` / `0.6308` / `-27.90%` / `3.59`

窗口指标（截至 `2026-05-19`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `164.15%`, CAGR `11.10%`, Max DD `-35.13%`, Sharpe `0.5455`, Turnover `3.26`
- `2020-01-01` → `2026-05-19`: Total Return `156.33%`, CAGR `16.15%`, Max DD `-27.90%`, Sharpe `0.6308`, Turnover `3.59`
- `2023-01-01` → `2026-05-19`: Total Return `79.91%`, CAGR `19.31%`, Max DD `-30.35%`, Sharpe `0.7172`, Turnover `2.81`
- `2025-01-01` → `2026-05-19`: Total Return `71.86%`, CAGR `47.86%`, Max DD `-24.52%`, Sharpe `1.0451`, Turnover `7.68`
- `2026-01-01` → `2026-05-19`: Total Return `-2.18%`, CAGR `-5.86%`, Max DD `-15.09%`, Sharpe `0.0444`, Turnover `9.80`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn15_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票65%, 持有5周, 换手15%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`78.31%` / `1.3121` / `-24.26%` / `7.17`

窗口指标（截至 `2026-05-19`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `163.62%`, CAGR `11.07%`, Max DD `-33.12%`, Sharpe `0.5495`, Turnover `3.92`
- `2020-01-01` → `2026-05-19`: Total Return `102.01%`, CAGR `11.83%`, Max DD `-28.96%`, Sharpe `0.5486`, Turnover `3.56`
- `2023-01-01` → `2026-05-19`: Total Return `78.84%`, CAGR `19.09%`, Max DD `-33.30%`, Sharpe `0.6797`, Turnover `3.45`
- `2025-01-01` → `2026-05-19`: Total Return `122.73%`, CAGR `78.31%`, Max DD `-24.26%`, Sharpe `1.3121`, Turnover `7.17`
- `2026-01-01` → `2026-05-19`: Total Return `3.59%`, CAGR `10.13%`, Max DD `-14.76%`, Sharpe `0.4349`, Turnover `10.82`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有6周, 换手12%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`23.60%` / `11.10%` / `0.7346` / `-35.13%` / `4.33`

窗口指标：

- `2017-01-01` → `2026-05-19`: Total Return `164.15%`, CAGR `11.10%`, Max DD `-35.13%`, Sharpe `0.5455`, Turnover `3.26`
- `2020-01-01` → `2026-05-19`: Total Return `156.33%`, CAGR `16.15%`, Max DD `-27.90%`, Sharpe `0.6308`, Turnover `3.59`
- `2023-01-01` → `2026-05-19`: Total Return `79.91%`, CAGR `19.31%`, Max DD `-30.35%`, Sharpe `0.7172`, Turnover `2.81`
- `2025-01-01` → `2026-05-19`: Total Return `71.86%`, CAGR `47.86%`, Max DD `-24.52%`, Sharpe `1.0451`, Turnover `7.68`
- `2026-01-01` → `2026-05-19`: Total Return `-2.18%`, CAGR `-5.86%`, Max DD `-15.09%`, Sharpe `0.0444`, Turnover `9.80`

<!-- AUTO:WEIGHTED-WINNERS:END -->

当不同窗口的赢家不同时，项目会同时保留它们，作为防过拟合的护栏。README 中的 `strategy_comparison_*` 图展示跟踪赢家，`strategy_family_*` 图现在只展示默认参与展示的 **core active family**。更宽的 **research active family** 仍继续参与回测与迭代，用于保留更大的候选范围；历史实验策略会保留在 `results/` 中作为 **archive family** 供追溯，但默认不再进入 README、默认图表和默认比较脚本。

A 股各路径在四个窗口下的赢家变化历史，持续记录在：

- [HISTORY.md](HISTORY.md)
- [docs/path1_plan.md](docs/path1_plan.md)
- [docs/path2_plan.md](docs/path2_plan.md)

## 沪港通独立研究线

沪港通结果独立维护，不并入 A 股 `winner_only` 结论。`2026-04-22` 起，港股窗口的 `sample_start` 统一对齐到**首个可执行调仓点**，因此本节数值应以这次重算后的基线为准。

当前 tracked winners（tracked payload `as_of=2026-05-08`；月频/双周样本多截止 `2026-04-30`，周频样本可到 `2026-05-08`，信号生效日仍按各策略真实评估点生成）：

当前港股 `since_2017_01 / since_2020_01` 两个窗口都从首个可执行调仓点起算，因此这两个窗口的港股指标当前相同；月频 Path 1/2 起点为 `2021-01-04`，周频 Path 3 起点为 `2020-12-14`。

三条研究路径按如下口径维护：

- **Path 1：实盘稳健线**，保留月度/双周稳健候选，后续主攻“月度调仓 + 周度风控/卫星”。
- **Path 2：收益上限探索线**，保留月度/双周高收益候选，继续探索主题、突破、高集中与高弹性结构。
- **Path 3：纯周度调仓线**，只纳入周度信号、周度换股候选，单独评估高频交易价值。

- Path 1：
  - `since_2017_01 / since_2020_01`：`hkconnect_path1_monthly_equal_buffered`
  - `since_2023_01`：`hkconnect_path1_monthly_equal_buffered`
  - `since_2025_01`：`hkconnect_path1_monthly_equal_buffered`
  - robust candidate：`hkconnect_path1_monthly_equal_buffered`
- Path 2：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`
  - `since_2023_01`：`hkconnect_path2_theme_monthly`
  - `since_2025_01`：`hkconnect_path2_breakout_concentrated_monthly`
  - robust candidate：`hkconnect_path2_theme_monthly`
- Path 3：
  - `since_2017_01 / since_2020_01`：`hkconnect_path3_theme_fast_weekly_defensive`
  - `since_2023_01`：`hkconnect_path3_theme_fast_weekly_buffered`
  - `since_2025_01`：`hkconnect_path3_theme_fast_weekly_defensive`
  - robust candidate：`hkconnect_path3_theme_fast_weekly`
- `since_2026_01`：只做观察，不进入 tracked winners；当前 raw leader 分别是 `hkconnect_path1_biweekly_lowvol`（Path 1）、`hkconnect_path2_breakout_concentrated_monthly`（Path 2）与 `hkconnect_path3_equal_elastic_weekly`（Path 3）

关键窗口指标：

- Path 1 `since_2020_01`：`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`（`hkconnect_path1_monthly_equal_buffered`）
- Path 1 `since_2023_01`：`33.85% CAGR / -14.79% MaxDD / 1.6907 Sharpe / 2.87 Turnover`（`hkconnect_path1_monthly_equal_buffered`）
- Path 1 `since_2025_01`：`40.41% CAGR / -14.79% MaxDD / 1.5271 Sharpe / 3.46 Turnover`（`hkconnect_path1_monthly_equal_buffered`）
- Path 2 `since_2020_01`：`21.57% CAGR / -18.98% MaxDD / 1.1176 Sharpe / 6.62 Turnover`（`hkconnect_path2_theme_monthly`）
- Path 2 `since_2023_01`：`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`（`hkconnect_path2_theme_monthly`）
- Path 2 `since_2025_01`：`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`（`hkconnect_path2_breakout_concentrated_monthly`）
- Path 3 `since_2020_01`：`23.86% CAGR / -28.45% MaxDD / 0.9638 Sharpe / 29.23 Turnover`（`hkconnect_path3_theme_fast_weekly_defensive`）
- Path 3 `since_2023_01`：`40.82% CAGR / -19.56% MaxDD / 1.3156 Sharpe / 29.62 Turnover`（`hkconnect_path3_theme_fast_weekly_buffered`）
- Path 3 `since_2025_01`：`78.07% CAGR / -17.82% MaxDD / 1.7678 Sharpe / 34.72 Turnover`（`hkconnect_path3_theme_fast_weekly_defensive`）

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
