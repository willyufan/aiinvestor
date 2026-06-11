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

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`27.23%` / `1.0690` / `-28.35%` / `3.60`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`27.20%` / `1.0704` / `-27.79%` / `3.67`

窗口指标（截至 `2026-06-10`，权重：2017-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `885.42%`, CAGR `27.23%`, Max DD `-28.35%`, Sharpe `1.0690`, Turnover `3.60`
- `2020-01-01` → `2026-06-10`: Total Return `261.41%`, CAGR `21.86%`, Max DD `-25.37%`, Sharpe `0.8237`, Turnover `3.61`
- `2023-01-01` → `2026-06-10`: Total Return `100.47%`, CAGR `21.98%`, Max DD `-22.29%`, Sharpe `0.7912`, Turnover `3.93`
- `2025-01-01` → `2026-06-10`: Total Return `178.93%`, CAGR `98.15%`, Max DD `-10.69%`, Sharpe `1.9077`, Turnover `4.76`
- `2026-01-01` → `2026-06-10`: Total Return `38.95%`, CAGR `93.06%`, Max DD `-11.49%`, Sharpe `1.7386`, Turnover `6.35`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`32.33%` / `1.0598` / `-19.01%` / `8.49`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`36.09%` / `1.0037` / `-30.69%` / `4.06`

窗口指标（截至 `2026-06-10`，权重：2023-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `79.18%`, CAGR `6.33%`, Max DD `-44.89%`, Sharpe `0.3817`, Turnover `11.26`
- `2020-01-01` → `2026-06-10`: Total Return `-31.24%`, CAGR `-5.60%`, Max DD `-58.40%`, Sharpe `-0.1740`, Turnover `13.45`
- `2023-01-01` → `2026-06-10`: Total Return `166.54%`, CAGR `32.33%`, Max DD `-19.01%`, Sharpe `1.0598`, Turnover `8.49`
- `2025-01-01` → `2026-06-10`: Total Return `73.44%`, CAGR `44.36%`, Max DD `-10.24%`, Sharpe `1.3286`, Turnover `12.79`
- `2026-01-01` → `2026-06-10`: Total Return `-4.42%`, CAGR `-8.64%`, Max DD `-11.15%`, Sharpe `-0.3894`, Turnover `9.85`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险18成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`28.82%` / `1.0509` / `-12.04%` / `3.36`

窗口指标（截至 `2026-06-10`，权重：2020-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `553.52%`, CAGR `21.85%`, Max DD `-14.22%`, Sharpe `0.9446`, Turnover `2.99`
- `2020-01-01` → `2026-06-10`: Total Return `418.56%`, CAGR `28.82%`, Max DD `-12.04%`, Sharpe `1.0509`, Turnover `3.36`
- `2023-01-01` → `2026-06-10`: Total Return `117.42%`, CAGR `24.84%`, Max DD `-17.92%`, Sharpe `0.8918`, Turnover `3.39`
- `2025-01-01` → `2026-06-10`: Total Return `163.20%`, CAGR `90.63%`, Max DD `-10.91%`, Sharpe `1.7667`, Turnover `4.62`
- `2026-01-01` → `2026-06-10`: Total Return `35.85%`, CAGR `84.55%`, Max DD `-6.61%`, Sharpe `1.9209`, Turnover `7.35`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`95.30%` / `2.0371` / `-10.17%` / `4.37`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`98.31%` / `1.9044` / `-10.73%` / `4.75`

窗口指标（截至 `2026-06-10`，权重：2025-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `459.66%`, CAGR `19.88%`, Max DD `-25.52%`, Sharpe `0.8587`, Turnover `2.60`
- `2020-01-01` → `2026-06-10`: Total Return `203.04%`, CAGR `18.60%`, Max DD `-27.91%`, Sharpe `0.7265`, Turnover `2.95`
- `2023-01-01` → `2026-06-10`: Total Return `171.19%`, CAGR `32.98%`, Max DD `-29.80%`, Sharpe `0.9860`, Turnover `2.96`
- `2025-01-01` → `2026-06-10`: Total Return `172.93%`, CAGR `95.30%`, Max DD `-10.17%`, Sharpe `2.0371`, Turnover `4.37`
- `2026-01-01` → `2026-06-10`: Total Return `32.81%`, CAGR `76.37%`, Max DD `-11.97%`, Sharpe `1.5854`, Turnover `5.33`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险16成本再确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`41.56%` / `21.82%` / `1.1644` / `-17.45%` / `3.59`

窗口指标：

- `2017-01-01` → `2026-06-10`: Total Return `552.09%`, CAGR `21.82%`, Max DD `-14.31%`, Sharpe `0.9439`, Turnover `2.99`
- `2020-01-01` → `2026-06-10`: Total Return `417.97%`, CAGR `28.79%`, Max DD `-12.04%`, Sharpe `1.0503`, Turnover `3.35`
- `2023-01-01` → `2026-06-10`: Total Return `118.32%`, CAGR `24.99%`, Max DD `-17.45%`, Sharpe `0.8966`, Turnover `3.39`
- `2025-01-01` → `2026-06-10`: Total Return `163.21%`, CAGR `90.63%`, Max DD `-10.91%`, Sharpe `1.7668`, Turnover `4.62`
- `2026-01-01` → `2026-06-10`: Total Return `35.85%`, CAGR `84.55%`, Max DD `-6.61%`, Sharpe `1.9209`, Turnover `7.35`

## Path 1：组合方案

- 组合ID：`path1_composite_robust_window_blend_v1`
- 组合逻辑：不再要求单一 winner 覆盖所有行情，按鲁棒候选与窗口赢家合并权重。
- 组合鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`41.79%` / `22.27%` / `1.2054` / `-16.45%` / `4.44`

当前组合成分：

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险16成本再确认)）：`45.0%`；来源：robust-candidate
- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险18成本再确认)）：`20.0%`；来源：2020-01
- `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整(双周确认)）：`20.0%`；来源：2017-01
- `core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）：`10.0%`；来源：2023-01
- `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）：`5.0%`；来源：2025-01

组合窗口指标：

- `2017-01-01` → `2026-06-10`: Total Return `567.13%`, CAGR `22.27%`, Max DD `-12.00%`, Sharpe `0.9978`, Turnover `3.92`
- `2020-01-01` → `2026-06-10`: Total Return `331.11%`, CAGR `25.47%`, Max DD `-12.64%`, Sharpe `0.9769`, Turnover `4.40`
- `2023-01-01` → `2026-06-10`: Total Return `122.03%`, CAGR `26.11%`, Max DD `-16.45%`, Sharpe `0.9508`, Turnover `3.99`
- `2025-01-01` → `2026-06-10`: Total Return `157.86%`, CAGR `93.29%`, Max DD `-8.45%`, Sharpe `1.8962`, Turnover `5.45`
- `2026-01-01` → `2026-06-10`: Total Return `32.29%`, CAGR `89.42%`, Max DD `-7.03%`, Sharpe `2.0174`, Turnover `7.30`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`21.07%` / `0.8831` / `-25.70%` / `2.51`

窗口指标（截至 `2026-06-10`，权重：2017-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `515.12%`, CAGR `21.07%`, Max DD `-25.70%`, Sharpe `0.8831`, Turnover `2.51`
- `2020-01-01` → `2026-06-10`: Total Return `243.51%`, CAGR `20.91%`, Max DD `-26.64%`, Sharpe `0.8217`, Turnover `2.84`
- `2023-01-01` → `2026-06-10`: Total Return `140.26%`, CAGR `28.46%`, Max DD `-28.78%`, Sharpe `0.9101`, Turnover `2.90`
- `2025-01-01` → `2026-06-10`: Total Return `167.38%`, CAGR `92.64%`, Max DD `-10.93%`, Sharpe `2.0174`, Turnover `4.24`
- `2026-01-01` → `2026-06-10`: Total Return `29.69%`, CAGR `68.20%`, Max DD `-9.32%`, Sharpe `1.6273`, Turnover `5.95`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`32.98%` / `0.9860` / `-29.80%` / `2.96`

窗口指标（截至 `2026-06-10`，权重：2023-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `459.66%`, CAGR `19.88%`, Max DD `-25.52%`, Sharpe `0.8587`, Turnover `2.60`
- `2020-01-01` → `2026-06-10`: Total Return `203.04%`, CAGR `18.60%`, Max DD `-27.91%`, Sharpe `0.7265`, Turnover `2.95`
- `2023-01-01` → `2026-06-10`: Total Return `171.19%`, CAGR `32.98%`, Max DD `-29.80%`, Sharpe `0.9860`, Turnover `2.96`
- `2025-01-01` → `2026-06-10`: Total Return `172.93%`, CAGR `95.30%`, Max DD `-10.17%`, Sharpe `2.0371`, Turnover `4.37`
- `2026-01-01` → `2026-06-10`: Total Return `32.81%`, CAGR `76.37%`, Max DD `-11.97%`, Sharpe `1.5854`, Turnover `5.33`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`20.91%` / `0.8217` / `-26.64%` / `2.84`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`22.91%` / `0.9306` / `-15.30%` / `2.42`

窗口指标（截至 `2026-06-10`，权重：2020-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `515.12%`, CAGR `21.07%`, Max DD `-25.70%`, Sharpe `0.8831`, Turnover `2.51`
- `2020-01-01` → `2026-06-10`: Total Return `243.51%`, CAGR `20.91%`, Max DD `-26.64%`, Sharpe `0.8217`, Turnover `2.84`
- `2023-01-01` → `2026-06-10`: Total Return `140.26%`, CAGR `28.46%`, Max DD `-28.78%`, Sharpe `0.9101`, Turnover `2.90`
- `2025-01-01` → `2026-06-10`: Total Return `167.38%`, CAGR `92.64%`, Max DD `-10.93%`, Sharpe `2.0174`, Turnover `4.24`
- `2026-01-01` → `2026-06-10`: Total Return `29.69%`, CAGR `68.20%`, Max DD `-9.32%`, Sharpe `1.6273`, Turnover `5.95`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升3只(核心6-1动量, 关闭熊市降仓, 单票60%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`146.28%` / `2.1719` / `-17.39%` / `5.89`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`283.48%` / `2.0658` / `-38.85%` / `15.14`

窗口指标（截至 `2026-06-10`，权重：2025-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `234.99%`, CAGR `13.57%`, Max DD `-63.06%`, Sharpe `0.5396`, Turnover `5.27`
- `2020-01-01` → `2026-06-10`: Total Return `230.36%`, CAGR `20.18%`, Max DD `-59.70%`, Sharpe `0.6401`, Turnover `5.64`
- `2023-01-01` → `2026-06-10`: Total Return `230.91%`, CAGR `40.76%`, Max DD `-48.65%`, Sharpe `0.9989`, Turnover `5.28`
- `2025-01-01` → `2026-06-10`: Total Return `286.51%`, CAGR `146.28%`, Max DD `-17.39%`, Sharpe `2.1719`, Turnover `5.89`
- `2026-01-01` → `2026-06-10`: Total Return `48.31%`, CAGR `119.97%`, Max DD `-10.64%`, Sharpe `2.0772`, Turnover `6.55`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`40.77%` / `20.91%` / `1.1581` / `-28.78%` / `3.12`

窗口指标：

- `2017-01-01` → `2026-06-10`: Total Return `515.12%`, CAGR `21.07%`, Max DD `-25.70%`, Sharpe `0.8831`, Turnover `2.51`
- `2020-01-01` → `2026-06-10`: Total Return `243.51%`, CAGR `20.91%`, Max DD `-26.64%`, Sharpe `0.8217`, Turnover `2.84`
- `2023-01-01` → `2026-06-10`: Total Return `140.26%`, CAGR `28.46%`, Max DD `-28.78%`, Sharpe `0.9101`, Turnover `2.90`
- `2025-01-01` → `2026-06-10`: Total Return `167.38%`, CAGR `92.64%`, Max DD `-10.93%`, Sharpe `2.0174`, Turnover `4.24`
- `2026-01-01` → `2026-06-10`: Total Return `29.69%`, CAGR `68.20%`, Max DD `-9.32%`, Sharpe `1.6273`, Turnover `5.95`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.22%` / `0.7915` / `-25.00%` / `2.19`

窗口指标（截至 `2026-06-10`，权重：2017-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `216.80%`, CAGR `13.22%`, Max DD `-25.00%`, Sharpe `0.7915`, Turnover `2.19`
- `2020-01-01` → `2026-06-10`: Total Return `179.41%`, CAGR `17.58%`, Max DD `-26.29%`, Sharpe `0.8557`, Turnover `1.90`
- `2023-01-01` → `2026-06-10`: Total Return `82.38%`, CAGR `19.43%`, Max DD `-23.81%`, Sharpe `0.8857`, Turnover `1.77`
- `2025-01-01` → `2026-06-10`: Total Return `55.46%`, CAGR `35.79%`, Max DD `-13.55%`, Sharpe `1.3139`, Turnover `2.08`
- `2026-01-01` → `2026-06-10`: Total Return `20.98%`, CAGR `56.85%`, Max DD `-11.46%`, Sharpe `1.5333`, Turnover `3.98`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有2周, 换手12%, 出场92%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`18.72%` / `0.7724` / `-23.16%` / `3.40`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`19.43%` / `0.8857` / `-23.81%` / `1.77`

窗口指标（截至 `2026-06-10`，权重：2023-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `209.53%`, CAGR `12.94%`, Max DD `-26.28%`, Sharpe `0.6796`, Turnover `3.89`
- `2020-01-01` → `2026-06-10`: Total Return `186.84%`, CAGR `18.06%`, Max DD `-28.10%`, Sharpe `0.7900`, Turnover `3.52`
- `2023-01-01` → `2026-06-10`: Total Return `78.74%`, CAGR `18.72%`, Max DD `-23.16%`, Sharpe `0.7724`, Turnover `3.40`
- `2025-01-01` → `2026-06-10`: Total Return `109.54%`, CAGR `67.01%`, Max DD `-17.81%`, Sharpe `1.6157`, Turnover `6.31`
- `2026-01-01` → `2026-06-10`: Total Return `19.83%`, CAGR `53.37%`, Max DD `-10.32%`, Sharpe `1.5526`, Turnover `8.24`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市20%, 单票56%, 持有5周, 换手5%, 出场96%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`21.29%` / `0.9414` / `-23.89%` / `1.63`

窗口指标（截至 `2026-06-10`，权重：2020-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `171.73%`, CAGR `11.36%`, Max DD `-28.09%`, Sharpe `0.6506`, Turnover `2.09`
- `2020-01-01` → `2026-06-10`: Total Return `240.41%`, CAGR `21.29%`, Max DD `-23.89%`, Sharpe `0.9414`, Turnover `1.63`
- `2023-01-01` → `2026-06-10`: Total Return `65.29%`, CAGR `16.01%`, Max DD `-14.50%`, Sharpe `0.8649`, Turnover `1.65`
- `2025-01-01` → `2026-06-10`: Total Return `110.01%`, CAGR `67.27%`, Max DD `-14.92%`, Sharpe `1.6386`, Turnover `2.93`
- `2026-01-01` → `2026-06-10`: Total Return `30.93%`, CAGR `89.07%`, Max DD `-12.88%`, Sharpe `1.9854`, Turnover `2.09`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`283.48%` / `2.0658` / `-38.85%` / `15.14`

窗口指标（截至 `2026-06-10`，权重：2025-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `268.67%`, CAGR `15.08%`, Max DD `-63.08%`, Sharpe `0.5115`, Turnover `8.05`
- `2020-01-01` → `2026-06-10`: Total Return `116.16%`, CAGR `12.92%`, Max DD `-51.01%`, Sharpe `0.4655`, Turnover `9.27`
- `2023-01-01` → `2026-06-10`: Total Return `55.46%`, CAGR `13.92%`, Max DD `-52.31%`, Sharpe `0.4788`, Turnover `10.52`
- `2025-01-01` → `2026-06-10`: Total Return `594.93%`, CAGR `283.48%`, Max DD `-38.85%`, Sharpe `2.0658`, Turnover `15.14`
- `2026-01-01` → `2026-06-10`: Total Return `99.93%`, CAGR `414.27%`, Max DD `-20.73%`, Sharpe `2.9209`, Turnover `21.28`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有2周, 换手12%, 出场92%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`29.18%` / `12.94%` / `0.9644` / `-28.10%` / `4.28`

窗口指标：

- `2017-01-01` → `2026-06-10`: Total Return `209.53%`, CAGR `12.94%`, Max DD `-26.28%`, Sharpe `0.6796`, Turnover `3.89`
- `2020-01-01` → `2026-06-10`: Total Return `186.84%`, CAGR `18.06%`, Max DD `-28.10%`, Sharpe `0.7900`, Turnover `3.52`
- `2023-01-01` → `2026-06-10`: Total Return `78.74%`, CAGR `18.72%`, Max DD `-23.16%`, Sharpe `0.7724`, Turnover `3.40`
- `2025-01-01` → `2026-06-10`: Total Return `109.54%`, CAGR `67.01%`, Max DD `-17.81%`, Sharpe `1.6157`, Turnover `6.31`
- `2026-01-01` → `2026-06-10`: Total Return `19.83%`, CAGR `53.37%`, Max DD `-10.32%`, Sharpe `1.5526`, Turnover `8.24`

## Path 4：窗口跟踪赢家（观察）

### 2017 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市12%, 单票8%, 出场58%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`12.85%` / `0.8100` / `-16.86%` / `3.91`

窗口指标（截至 `2026-06-10`，权重：2017-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `215.23%`, CAGR `12.85%`, Max DD `-16.86%`, Sharpe `0.8100`, Turnover `3.91`
- `2020-01-01` → `2026-06-10`: Total Return `133.36%`, CAGR `13.93%`, Max DD `-15.22%`, Sharpe `0.7986`, Turnover `3.83`
- `2023-01-01` → `2026-06-10`: Total Return `40.63%`, CAGR `10.23%`, Max DD `-6.64%`, Sharpe `1.0206`, Turnover `3.31`
- `2025-01-01` → `2026-06-10`: Total Return `87.15%`, CAGR `51.86%`, Max DD `-6.58%`, Sharpe `1.7658`, Turnover `6.77`
- `2026-01-01` → `2026-06-10`: Total Return `26.46%`, CAGR `59.93%`, Max DD `-10.66%`, Sharpe `1.7790`, Turnover `6.93`

### 2023 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`33.95%` / `1.1293` / `-12.63%` / `3.13`

窗口指标（截至 `2026-06-10`，权重：2023-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `107.29%`, CAGR `7.97%`, Max DD `-36.58%`, Sharpe `0.5112`, Turnover `3.36`
- `2020-01-01` → `2026-06-10`: Total Return `-25.95%`, CAGR `-4.52%`, Max DD `-47.40%`, Sharpe `-0.1601`, Turnover `3.20`
- `2023-01-01` → `2026-06-10`: Total Return `178.15%`, CAGR `33.95%`, Max DD `-12.63%`, Sharpe `1.1293`, Turnover `3.13`
- `2025-01-01` → `2026-06-10`: Total Return `45.60%`, CAGR `28.46%`, Max DD `-6.23%`, Sharpe `1.5719`, Turnover `4.89`
- `2026-01-01` → `2026-06-10`: Total Return `14.84%`, CAGR `31.88%`, Max DD `-3.42%`, Sharpe `1.3228`, Turnover `5.03`

### 2020 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市12%, 单票8%, 出场58%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.93%` / `0.7986` / `-15.22%` / `3.83`

窗口指标（截至 `2026-06-10`，权重：2020-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `215.23%`, CAGR `12.85%`, Max DD `-16.86%`, Sharpe `0.8100`, Turnover `3.91`
- `2020-01-01` → `2026-06-10`: Total Return `133.36%`, CAGR `13.93%`, Max DD `-15.22%`, Sharpe `0.7986`, Turnover `3.83`
- `2023-01-01` → `2026-06-10`: Total Return `40.63%`, CAGR `10.23%`, Max DD `-6.64%`, Sharpe `1.0206`, Turnover `3.31`
- `2025-01-01` → `2026-06-10`: Total Return `87.15%`, CAGR `51.86%`, Max DD `-6.58%`, Sharpe `1.7658`, Turnover `6.77`
- `2026-01-01` → `2026-06-10`: Total Return `26.46%`, CAGR `59.93%`, Max DD `-10.66%`, Sharpe `1.7790`, Turnover `6.93`

### 2025 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市12%, 单票8%, 出场58%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`51.86%` / `1.7658` / `-6.58%` / `6.77`

窗口指标（截至 `2026-06-10`，权重：2025-01=100%）：

- `2017-01-01` → `2026-06-10`: Total Return `215.23%`, CAGR `12.85%`, Max DD `-16.86%`, Sharpe `0.8100`, Turnover `3.91`
- `2020-01-01` → `2026-06-10`: Total Return `133.36%`, CAGR `13.93%`, Max DD `-15.22%`, Sharpe `0.7986`, Turnover `3.83`
- `2023-01-01` → `2026-06-10`: Total Return `40.63%`, CAGR `10.23%`, Max DD `-6.64%`, Sharpe `1.0206`, Turnover `3.31`
- `2025-01-01` → `2026-06-10`: Total Return `87.15%`, CAGR `51.86%`, Max DD `-6.58%`, Sharpe `1.7658`, Turnover `6.77`
- `2026-01-01` → `2026-06-10`: Total Return `26.46%`, CAGR `59.93%`, Max DD `-10.66%`, Sharpe `1.7790`, Turnover `6.93`

## Path 4：鲁棒候选（观察）

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市14%, 单票8%, 出场62%, 低换手)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`21.43%` / `10.91%` / `1.0746` / `-17.45%` / `4.49`

窗口指标：

- `2017-01-01` → `2026-06-10`: Total Return `178.75%`, CAGR `11.39%`, Max DD `-17.45%`, Sharpe `0.7344`, Turnover `3.95`
- `2020-01-01` → `2026-06-10`: Total Return `103.28%`, CAGR `11.53%`, Max DD `-17.45%`, Sharpe `0.6852`, Turnover `3.90`
- `2023-01-01` → `2026-06-10`: Total Return `43.68%`, CAGR `10.91%`, Max DD `-5.19%`, Sharpe `1.1131`, Turnover `3.36`
- `2025-01-01` → `2026-06-10`: Total Return `87.15%`, CAGR `51.86%`, Max DD `-6.58%`, Sharpe `1.7658`, Turnover `6.77`
- `2026-01-01` → `2026-06-10`: Total Return `26.46%`, CAGR `59.93%`, Max DD `-10.66%`, Sharpe `1.7790`, Turnover `6.93`

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
