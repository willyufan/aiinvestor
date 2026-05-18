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

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`20.83%` / `1.0819` / `-11.08%` / `2.23`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`27.89%` / `1.1382` / `-28.16%` / `3.62`

窗口指标（截至 `2026-05-18`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `494.07%`, CAGR `20.83%`, Max DD `-11.08%`, Sharpe `1.0819`, Turnover `2.23`
- `2020-01-01` → `2026-05-18`: Total Return `276.50%`, CAGR `22.95%`, Max DD `-15.47%`, Sharpe `0.9748`, Turnover `2.28`
- `2023-01-01` → `2026-05-18`: Total Return `130.22%`, CAGR `27.64%`, Max DD `-12.34%`, Sharpe `1.1425`, Turnover `2.49`
- `2025-01-01` → `2026-05-18`: Total Return `165.51%`, CAGR `99.23%`, Max DD `-9.60%`, Sharpe `2.0976`, Turnover `5.04`
- `2026-01-01` → `2026-05-18`: Total Return `9.88%`, CAGR `25.38%`, Max DD `-12.30%`, Sharpe `0.8750`, Turnover `5.45`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_balanced`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(多因子均衡)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`33.56%` / `1.0680` / `-30.00%` / `3.59`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`44.23%` / `1.2293` / `-34.22%` / `10.35`

窗口指标（截至 `2026-05-18`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `272.48%`, CAGR `14.99%`, Max DD `-33.99%`, Sharpe `0.7944`, Turnover `2.88`
- `2020-01-01` → `2026-05-18`: Total Return `136.69%`, CAGR `14.37%`, Max DD `-38.12%`, Sharpe `0.6724`, Turnover `3.35`
- `2023-01-01` → `2026-05-18`: Total Return `168.76%`, CAGR `33.56%`, Max DD `-30.00%`, Sharpe `1.0680`, Turnover `3.59`
- `2025-01-01` → `2026-05-18`: Total Return `139.56%`, CAGR `85.28%`, Max DD `-13.04%`, Sharpe `1.9834`, Turnover `5.59`
- `2026-01-01` → `2026-05-18`: Total Return `16.07%`, CAGR `43.00%`, Max DD `-9.47%`, Sharpe `1.3762`, Turnover `6.94`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只__卫星周频三档风控(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`28.92%` / `1.0055` / `-31.00%` / `3.45`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`38.76%` / `1.0246` / `-46.00%` / `11.97`

窗口指标（截至 `2026-05-18`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `544.53%`, CAGR `21.88%`, Max DD `-25.68%`, Sharpe `0.9054`, Turnover `2.93`
- `2020-01-01` → `2026-05-18`: Total Return `410.40%`, CAGR `28.92%`, Max DD `-31.00%`, Sharpe `1.0055`, Turnover `3.45`
- `2023-01-01` → `2026-05-18`: Total Return `131.17%`, CAGR `27.80%`, Max DD `-29.28%`, Sharpe `0.8927`, Turnover `3.58`
- `2025-01-01` → `2026-05-18`: Total Return `143.27%`, CAGR `87.30%`, Max DD `-11.78%`, Sharpe `1.8249`, Turnover `4.77`
- `2026-01-01` → `2026-05-18`: Total Return `26.48%`, CAGR `75.72%`, Max DD `-6.83%`, Sharpe `2.1318`, Turnover `8.14`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`97.94%` / `2.3396` / `-8.73%` / `5.39`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`100.94%` / `1.9577` / `-10.80%` / `4.74`

窗口指标（截至 `2026-05-18`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `292.32%`, CAGR `15.62%`, Max DD `-39.49%`, Sharpe `0.7300`, Turnover `3.21`
- `2020-01-01` → `2026-05-18`: Total Return `217.75%`, CAGR `19.74%`, Max DD `-37.85%`, Sharpe `0.7716`, Turnover `3.71`
- `2023-01-01` → `2026-05-18`: Total Return `135.30%`, CAGR `28.46%`, Max DD `-33.11%`, Sharpe `0.9954`, Turnover `3.82`
- `2025-01-01` → `2026-05-18`: Total Return `163.09%`, CAGR `97.94%`, Max DD `-8.73%`, Sharpe `2.3396`, Turnover `5.39`
- `2026-01-01` → `2026-05-18`: Total Return `14.94%`, CAGR `39.69%`, Max DD `-10.75%`, Sharpe `1.2364`, Turnover `6.59`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`46.74%` / `26.68%` / `1.2184` / `-29.23%` / `4.08`

窗口指标：

- `2017-01-01` → `2026-05-18`: Total Return `871.32%`, CAGR `27.31%`, Max DD `-25.54%`, Sharpe `1.0427`, Turnover `3.78`
- `2020-01-01` → `2026-05-18`: Total Return `355.99%`, CAGR `26.68%`, Max DD `-27.46%`, Sharpe `0.9084`, Turnover `3.72`
- `2023-01-01` → `2026-05-18`: Total Return `159.04%`, CAGR `32.13%`, Max DD `-29.23%`, Sharpe `0.9557`, Turnover `4.08`
- `2025-01-01` → `2026-05-18`: Total Return `168.61%`, CAGR `100.87%`, Max DD `-10.72%`, Sharpe `1.9669`, Turnover `4.73`
- `2026-01-01` → `2026-05-18`: Total Return `27.30%`, CAGR `78.48%`, Max DD `-11.85%`, Sharpe `1.7350`, Turnover `7.15`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`38.58%` / `1.1328` / `-32.76%` / `3.79`

窗口指标（截至 `2026-05-18`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `2059.45%`, CAGR `38.58%`, Max DD `-32.76%`, Sharpe `1.1328`, Turnover `3.79`
- `2020-01-01` → `2026-05-18`: Total Return `1328.42%`, CAGR `51.35%`, Max DD `-32.05%`, Sharpe `1.2100`, Turnover `4.40`
- `2023-01-01` → `2026-05-18`: Total Return `321.80%`, CAGR `52.39%`, Max DD `-29.13%`, Sharpe `1.2365`, Turnover `4.33`
- `2025-01-01` → `2026-05-18`: Total Return `180.65%`, CAGR `107.18%`, Max DD `-13.92%`, Sharpe `1.9100`, Turnover `7.38`
- `2026-01-01` → `2026-05-18`: Total Return `-6.89%`, CAGR `-15.74%`, Max DD `-15.74%`, Sharpe `-0.3989`, Turnover `6.00`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 均线三档保留50%, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`65.59%` / `1.3289` / `-36.51%` / `4.79`

窗口指标（截至 `2026-05-18`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `1252.13%`, CAGR `31.86%`, Max DD `-41.54%`, Sharpe `0.9658`, Turnover `3.89`
- `2020-01-01` → `2026-05-18`: Total Return `1195.79%`, CAGR `49.07%`, Max DD `-39.65%`, Sharpe `1.1909`, Turnover `4.70`
- `2023-01-01` → `2026-05-18`: Total Return `460.24%`, CAGR `65.59%`, Max DD `-36.51%`, Sharpe `1.3289`, Turnover `4.79`
- `2025-01-01` → `2026-05-18`: Total Return `147.68%`, CAGR `89.69%`, Max DD `-14.29%`, Sharpe `1.9364`, Turnover `7.34`
- `2026-01-01` → `2026-05-18`: Total Return `-4.14%`, CAGR `-9.66%`, Max DD `-15.74%`, Sharpe `-0.2010`, Turnover `5.19`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`58.60%` / `1.2434` / `-28.34%` / `4.49`

窗口指标（截至 `2026-05-18`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `1486.35%`, CAGR `34.11%`, Max DD `-31.89%`, Sharpe `0.9391`, Turnover `4.16`
- `2020-01-01` → `2026-05-18`: Total Return `1829.11%`, CAGR `58.60%`, Max DD `-28.34%`, Sharpe `1.2434`, Turnover `4.49`
- `2023-01-01` → `2026-05-18`: Total Return `355.65%`, CAGR `55.87%`, Max DD `-29.20%`, Sharpe `1.2832`, Turnover `4.19`
- `2025-01-01` → `2026-05-18`: Total Return `163.12%`, CAGR `97.96%`, Max DD `-14.29%`, Sharpe `1.7842`, Turnover `7.39`
- `2026-01-01` → `2026-05-18`: Total Return `-7.37%`, CAGR `-16.78%`, Max DD `-15.74%`, Sharpe `-0.4429`, Turnover `5.97`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升3只(核心6-1动量, 关闭熊市降仓, 单票60%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`144.19%` / `2.1217` / `-17.33%` / `5.94`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`198.70%` / `1.7899` / `-40.77%` / `16.79`

窗口指标（截至 `2026-05-18`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `377.56%`, CAGR `18.06%`, Max DD `-65.24%`, Sharpe `0.6500`, Turnover `5.18`
- `2020-01-01` → `2026-05-18`: Total Return `253.49%`, CAGR `21.75%`, Max DD `-66.07%`, Sharpe `0.6307`, Turnover `5.65`
- `2023-01-01` → `2026-05-18`: Total Return `346.11%`, CAGR `54.91%`, Max DD `-49.35%`, Sharpe `1.2276`, Turnover `5.42`
- `2025-01-01` → `2026-05-18`: Total Return `254.23%`, CAGR `144.19%`, Max DD `-17.33%`, Sharpe `2.1217`, Turnover `5.94`
- `2026-01-01` → `2026-05-18`: Total Return `28.78%`, CAGR `83.49%`, Max DD `-10.91%`, Sharpe `1.6599`, Turnover `6.34`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 单票95%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`62.37%` / `38.58%` / `1.3723` / `-32.76%` / `4.98`

窗口指标：

- `2017-01-01` → `2026-05-18`: Total Return `2059.45%`, CAGR `38.58%`, Max DD `-32.76%`, Sharpe `1.1328`, Turnover `3.79`
- `2020-01-01` → `2026-05-18`: Total Return `1328.42%`, CAGR `51.35%`, Max DD `-32.05%`, Sharpe `1.2100`, Turnover `4.40`
- `2023-01-01` → `2026-05-18`: Total Return `321.80%`, CAGR `52.39%`, Max DD `-29.13%`, Sharpe `1.2365`, Turnover `4.33`
- `2025-01-01` → `2026-05-18`: Total Return `180.65%`, CAGR `107.18%`, Max DD `-13.92%`, Sharpe `1.9100`, Turnover `7.38`
- `2026-01-01` → `2026-05-18`: Total Return `-6.89%`, CAGR `-15.74%`, Max DD `-15.74%`, Sharpe `-0.3989`, Turnover `6.00`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`23.50%` / `0.8024` / `-40.04%` / `7.71`

窗口指标（截至 `2026-05-18`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `601.97%`, CAGR `23.50%`, Max DD `-40.04%`, Sharpe `0.8024`, Turnover `7.71`
- `2020-01-01` → `2026-05-18`: Total Return `196.40%`, CAGR `18.86%`, Max DD `-35.74%`, Sharpe `0.6416`, Turnover `8.21`
- `2023-01-01` → `2026-05-18`: Total Return `2.80%`, CAGR `0.83%`, Max DD `-38.94%`, Sharpe `0.1999`, Turnover `8.03`
- `2025-01-01` → `2026-05-18`: Total Return `49.81%`, CAGR `33.90%`, Max DD `-33.32%`, Sharpe `0.8265`, Turnover `16.91`
- `2026-01-01` → `2026-05-18`: Total Return `45.54%`, CAGR `179.29%`, Max DD `-14.43%`, Sharpe `2.3816`, Turnover `24.11`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票40%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`35.18%` / `0.9619` / `-37.14%` / `13.65`

窗口指标（截至 `2026-05-18`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `208.24%`, CAGR `12.97%`, Max DD `-50.28%`, Sharpe `0.5616`, Turnover `12.18`
- `2020-01-01` → `2026-05-18`: Total Return `136.37%`, CAGR `14.66%`, Max DD `-51.71%`, Sharpe `0.5631`, Turnover `12.98`
- `2023-01-01` → `2026-05-18`: Total Return `172.59%`, CAGR `35.18%`, Max DD `-37.14%`, Sharpe `0.9619`, Turnover `13.65`
- `2025-01-01` → `2026-05-18`: Total Return `71.15%`, CAGR `47.42%`, Max DD `-27.38%`, Sharpe `1.2230`, Turnover `13.71`
- `2026-01-01` → `2026-05-18`: Total Return `33.01%`, CAGR `118.30%`, Max DD `-12.06%`, Sharpe `2.5996`, Turnover `18.39`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`14.67%` / `0.5634` / `-51.71%` / `12.99`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`20.95%` / `0.7890` / `-25.89%` / `4.78`

窗口指标（截至 `2026-05-18`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `264.02%`, CAGR `15.02%`, Max DD `-50.28%`, Sharpe `0.6192`, Turnover `12.06`
- `2020-01-01` → `2026-05-18`: Total Return `136.55%`, CAGR `14.67%`, Max DD `-51.71%`, Sharpe `0.5634`, Turnover `12.99`
- `2023-01-01` → `2026-05-18`: Total Return `169.11%`, CAGR `34.66%`, Max DD `-37.14%`, Sharpe `0.9484`, Turnover `13.59`
- `2025-01-01` → `2026-05-18`: Total Return `70.10%`, CAGR `46.76%`, Max DD `-27.38%`, Sharpe `1.2107`, Turnover `13.75`
- `2026-01-01` → `2026-05-18`: Total Return `32.33%`, CAGR `115.27%`, Max DD `-12.06%`, Sharpe `2.5521`, Turnover `18.28`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`49.08%` / `1.2203` / `-28.73%` / `14.62`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`198.70%` / `1.7899` / `-40.77%` / `16.79`

窗口指标（截至 `2026-05-18`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-18`: Total Return `267.21%`, CAGR `15.13%`, Max DD `-51.47%`, Sharpe `0.6189`, Turnover `12.51`
- `2020-01-01` → `2026-05-18`: Total Return `50.84%`, CAGR `6.75%`, Max DD `-60.66%`, Sharpe `0.3600`, Turnover `13.63`
- `2023-01-01` → `2026-05-18`: Total Return `144.95%`, CAGR `30.90%`, Max DD `-38.90%`, Sharpe `0.8675`, Turnover `14.02`
- `2025-01-01` → `2026-05-18`: Total Return `73.84%`, CAGR `49.08%`, Max DD `-28.73%`, Sharpe `1.2203`, Turnover `14.62`
- `2026-01-01` → `2026-05-18`: Total Return `29.66%`, CAGR `103.57%`, Max DD `-12.32%`, Sharpe `2.1669`, Turnover `18.94`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票70%, 持有4周, 换手20%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`29.65%` / `19.14%` / `0.8525` / `-37.68%` / `5.28`

窗口指标：

- `2017-01-01` → `2026-05-18`: Total Return `403.49%`, CAGR `19.14%`, Max DD `-30.35%`, Sharpe `0.7646`, Turnover `4.45`
- `2020-01-01` → `2026-05-18`: Total Return `213.45%`, CAGR `19.92%`, Max DD `-25.77%`, Sharpe `0.7487`, Turnover `4.06`
- `2023-01-01` → `2026-05-18`: Total Return `85.62%`, CAGR `20.43%`, Max DD `-37.68%`, Sharpe `0.6979`, Turnover `3.91`
- `2025-01-01` → `2026-05-18`: Total Return `90.25%`, CAGR `59.13%`, Max DD `-22.35%`, Sharpe `1.1987`, Turnover `8.69`
- `2026-01-01` → `2026-05-18`: Total Return `-10.34%`, CAGR `-25.82%`, Max DD `-21.97%`, Sharpe `-0.5227`, Turnover `11.66`

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
