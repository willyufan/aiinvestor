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
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`27.34%` / `1.0733` / `-28.35%` / `3.60`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`27.31%` / `1.0746` / `-27.79%` / `3.67`

窗口指标（截至 `2026-06-11`，权重：2017-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `893.36%`, CAGR `27.34%`, Max DD `-28.35%`, Sharpe `1.0733`, Turnover `3.60`
- `2020-01-01` → `2026-06-11`: Total Return `263.94%`, CAGR `21.99%`, Max DD `-25.37%`, Sharpe `0.8280`, Turnover `3.61`
- `2023-01-01` → `2026-06-11`: Total Return `102.24%`, CAGR `22.29%`, Max DD `-22.29%`, Sharpe `0.8004`, Turnover `3.93`
- `2025-01-01` → `2026-06-11`: Total Return `181.42%`, CAGR `99.33%`, Max DD `-10.69%`, Sharpe `1.9276`, Turnover `4.76`
- `2026-01-01` → `2026-06-11`: Total Return `39.44%`, CAGR `94.45%`, Max DD `-11.49%`, Sharpe `1.7607`, Turnover `6.35`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`32.76%` / `1.0719` / `-19.01%` / `8.49`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`36.19%` / `1.0059` / `-30.69%` / `4.06`

窗口指标（截至 `2026-06-11`，权重：2023-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `85.52%`, CAGR `6.72%`, Max DD `-44.89%`, Sharpe `0.3982`, Turnover `11.28`
- `2020-01-01` → `2026-06-11`: Total Return `-28.80%`, CAGR `-5.09%`, Max DD `-58.40%`, Sharpe `-0.1481`, Turnover `13.49`
- `2023-01-01` → `2026-06-11`: Total Return `169.58%`, CAGR `32.76%`, Max DD `-19.01%`, Sharpe `1.0719`, Turnover `8.49`
- `2025-01-01` → `2026-06-11`: Total Return `74.30%`, CAGR `44.83%`, Max DD `-10.24%`, Sharpe `1.3418`, Turnover `12.79`
- `2026-01-01` → `2026-06-11`: Total Return `-4.46%`, CAGR `-8.71%`, Max DD `-11.18%`, Sharpe `-0.3937`, Turnover `10.28`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险18成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`29.04%` / `1.0587` / `-12.04%` / `3.36`

窗口指标（截至 `2026-06-11`，权重：2020-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `562.49%`, CAGR `22.02%`, Max DD `-14.22%`, Sharpe `0.9519`, Turnover `2.99`
- `2020-01-01` → `2026-06-11`: Total Return `424.39%`, CAGR `29.04%`, Max DD `-12.04%`, Sharpe `1.0587`, Turnover `3.36`
- `2023-01-01` → `2026-06-11`: Total Return `118.27%`, CAGR `24.98%`, Max DD `-17.92%`, Sharpe `0.8962`, Turnover `3.39`
- `2025-01-01` → `2026-06-11`: Total Return `167.70%`, CAGR `92.80%`, Max DD `-10.91%`, Sharpe `1.8026`, Turnover `4.62`
- `2026-01-01` → `2026-06-11`: Total Return `36.75%`, CAGR `87.01%`, Max DD `-6.61%`, Sharpe `1.9761`, Turnover `7.35`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`96.39%` / `2.0590` / `-10.17%` / `4.37`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_satellite_cost_guard`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(卫星成本防守)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`99.46%` / `1.9539` / `-10.33%` / `4.32`

窗口指标（截至 `2026-06-11`，权重：2025-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `465.69%`, CAGR `20.01%`, Max DD `-25.52%`, Sharpe `0.8642`, Turnover `2.60`
- `2020-01-01` → `2026-06-11`: Total Return `207.03%`, CAGR `18.84%`, Max DD `-27.91%`, Sharpe `0.7342`, Turnover `2.95`
- `2023-01-01` → `2026-06-11`: Total Return `171.94%`, CAGR `33.09%`, Max DD `-29.80%`, Sharpe `0.9886`, Turnover `2.96`
- `2025-01-01` → `2026-06-11`: Total Return `175.23%`, CAGR `96.39%`, Max DD `-10.17%`, Sharpe `2.0590`, Turnover `4.37`
- `2026-01-01` → `2026-06-11`: Total Return `33.27%`, CAGR `77.62%`, Max DD `-11.97%`, Sharpe `1.6071`, Turnover `5.33`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险16成本再确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`42.24%` / `21.99%` / `1.1782` / `-17.45%` / `3.59`

窗口指标：

- `2017-01-01` → `2026-06-11`: Total Return `561.03%`, CAGR `21.99%`, Max DD `-14.31%`, Sharpe `0.9512`, Turnover `2.99`
- `2020-01-01` → `2026-06-11`: Total Return `423.80%`, CAGR `29.02%`, Max DD `-12.04%`, Sharpe `1.0580`, Turnover `3.35`
- `2023-01-01` → `2026-06-11`: Total Return `119.18%`, CAGR `25.13%`, Max DD `-17.45%`, Sharpe `0.9009`, Turnover `3.39`
- `2025-01-01` → `2026-06-11`: Total Return `167.72%`, CAGR `92.80%`, Max DD `-10.91%`, Sharpe `1.8027`, Turnover `4.62`
- `2026-01-01` → `2026-06-11`: Total Return `36.75%`, CAGR `87.02%`, Max DD `-6.61%`, Sharpe `1.9762`, Turnover `7.35`

## Path 1：组合方案

- 组合ID：`path1_composite_robust_window_blend_v1`
- 组合逻辑：不再要求单一 winner 覆盖所有行情，按鲁棒候选与窗口赢家合并权重。
- 组合鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`42.33%` / `22.43%` / `1.2187` / `-16.45%` / `4.44`

当前组合成分：

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险16成本再确认)）：`45.0%`；来源：robust-candidate
- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险18成本再确认)）：`20.0%`；来源：2020-01
- `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整(双周确认)）：`20.0%`；来源：2017-01
- `core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）：`10.0%`；来源：2023-01
- `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）：`5.0%`；来源：2025-01

组合窗口指标：

- `2017-01-01` → `2026-06-11`: Total Return `575.47%`, CAGR `22.43%`, Max DD `-12.00%`, Sharpe `1.0049`, Turnover `3.93`
- `2020-01-01` → `2026-06-11`: Total Return `335.85%`, CAGR `25.67%`, Max DD `-12.64%`, Sharpe `0.9844`, Turnover `4.40`
- `2023-01-01` → `2026-06-11`: Total Return `123.29%`, CAGR `26.29%`, Max DD `-16.45%`, Sharpe `0.9572`, Turnover `3.99`
- `2025-01-01` → `2026-06-11`: Total Return `161.49%`, CAGR `94.93%`, Max DD `-8.45%`, Sharpe `1.9282`, Turnover `5.45`
- `2026-01-01` → `2026-06-11`: Total Return `33.00%`, CAGR `90.96%`, Max DD `-7.03%`, Sharpe `2.0613`, Turnover `7.34`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`21.21%` / `0.8886` / `-25.70%` / `2.51`

窗口指标（截至 `2026-06-11`，权重：2017-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `521.93%`, CAGR `21.21%`, Max DD `-25.70%`, Sharpe `0.8886`, Turnover `2.51`
- `2020-01-01` → `2026-06-11`: Total Return `244.57%`, CAGR `20.96%`, Max DD `-26.64%`, Sharpe `0.8237`, Turnover `2.84`
- `2023-01-01` → `2026-06-11`: Total Return `141.06%`, CAGR `28.58%`, Max DD `-28.78%`, Sharpe `0.9133`, Turnover `2.90`
- `2025-01-01` → `2026-06-11`: Total Return `170.22%`, CAGR `94.01%`, Max DD `-10.93%`, Sharpe `2.0453`, Turnover `4.24`
- `2026-01-01` → `2026-06-11`: Total Return `30.55%`, CAGR `70.42%`, Max DD `-9.32%`, Sharpe `1.6766`, Turnover `5.95`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`33.09%` / `0.9886` / `-29.80%` / `2.96`

窗口指标（截至 `2026-06-11`，权重：2023-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `465.69%`, CAGR `20.01%`, Max DD `-25.52%`, Sharpe `0.8642`, Turnover `2.60`
- `2020-01-01` → `2026-06-11`: Total Return `207.03%`, CAGR `18.84%`, Max DD `-27.91%`, Sharpe `0.7342`, Turnover `2.95`
- `2023-01-01` → `2026-06-11`: Total Return `171.94%`, CAGR `33.09%`, Max DD `-29.80%`, Sharpe `0.9886`, Turnover `2.96`
- `2025-01-01` → `2026-06-11`: Total Return `175.23%`, CAGR `96.39%`, Max DD `-10.17%`, Sharpe `2.0590`, Turnover `4.37`
- `2026-01-01` → `2026-06-11`: Total Return `33.27%`, CAGR `77.62%`, Max DD `-11.97%`, Sharpe `1.6071`, Turnover `5.33`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`20.96%` / `0.8237` / `-26.64%` / `2.84`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`23.09%` / `0.9378` / `-15.30%` / `2.42`

窗口指标（截至 `2026-06-11`，权重：2020-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `521.93%`, CAGR `21.21%`, Max DD `-25.70%`, Sharpe `0.8886`, Turnover `2.51`
- `2020-01-01` → `2026-06-11`: Total Return `244.57%`, CAGR `20.96%`, Max DD `-26.64%`, Sharpe `0.8237`, Turnover `2.84`
- `2023-01-01` → `2026-06-11`: Total Return `141.06%`, CAGR `28.58%`, Max DD `-28.78%`, Sharpe `0.9133`, Turnover `2.90`
- `2025-01-01` → `2026-06-11`: Total Return `170.22%`, CAGR `94.01%`, Max DD `-10.93%`, Sharpe `2.0453`, Turnover `4.24`
- `2026-01-01` → `2026-06-11`: Total Return `30.55%`, CAGR `70.42%`, Max DD `-9.32%`, Sharpe `1.6766`, Turnover `5.95`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心70_探索30_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`182.81%` / `1.7408` / `-34.01%` / `18.15`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`297.98%` / `2.1138` / `-38.85%` / `15.14`

窗口指标（截至 `2026-06-11`，权重：2025-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `382.10%`, CAGR `18.45%`, Max DD `-56.04%`, Sharpe `0.5931`, Turnover `9.15`
- `2020-01-01` → `2026-06-11`: Total Return `109.60%`, CAGR `12.37%`, Max DD `-54.40%`, Sharpe `0.4616`, Turnover `10.67`
- `2023-01-01` → `2026-06-11`: Total Return `169.52%`, CAGR `34.04%`, Max DD `-36.15%`, Sharpe `0.8012`, Turnover `11.36`
- `2025-01-01` → `2026-06-11`: Total Return `347.92%`, CAGR `182.81%`, Max DD `-34.01%`, Sharpe `1.7408`, Turnover `18.15`
- `2026-01-01` → `2026-06-11`: Total Return `103.50%`, CAGR `436.21%`, Max DD `-19.67%`, Sharpe `3.2609`, Turnover `24.46`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`41.19%` / `20.96%` / `1.1678` / `-28.78%` / `3.12`

窗口指标：

- `2017-01-01` → `2026-06-11`: Total Return `521.93%`, CAGR `21.21%`, Max DD `-25.70%`, Sharpe `0.8886`, Turnover `2.51`
- `2020-01-01` → `2026-06-11`: Total Return `244.57%`, CAGR `20.96%`, Max DD `-26.64%`, Sharpe `0.8237`, Turnover `2.84`
- `2023-01-01` → `2026-06-11`: Total Return `141.06%`, CAGR `28.58%`, Max DD `-28.78%`, Sharpe `0.9133`, Turnover `2.90`
- `2025-01-01` → `2026-06-11`: Total Return `170.22%`, CAGR `94.01%`, Max DD `-10.93%`, Sharpe `2.0453`, Turnover `4.24`
- `2026-01-01` → `2026-06-11`: Total Return `30.55%`, CAGR `70.42%`, Max DD `-9.32%`, Sharpe `1.6766`, Turnover `5.95`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.62%` / `0.8133` / `-25.00%` / `2.19`

窗口指标（截至 `2026-06-11`，权重：2017-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `227.33%`, CAGR `13.62%`, Max DD `-25.00%`, Sharpe `0.8133`, Turnover `2.19`
- `2020-01-01` → `2026-06-11`: Total Return `192.02%`, CAGR `18.40%`, Max DD `-26.29%`, Sharpe `0.8904`, Turnover `1.90`
- `2023-01-01` → `2026-06-11`: Total Return `90.82%`, CAGR `21.04%`, Max DD `-23.81%`, Sharpe `0.9456`, Turnover `1.77`
- `2025-01-01` → `2026-06-11`: Total Return `60.58%`, CAGR `38.87%`, Max DD `-13.55%`, Sharpe `1.3982`, Turnover `2.08`
- `2026-01-01` → `2026-06-11`: Total Return `22.44%`, CAGR `61.38%`, Max DD `-11.46%`, Sharpe `1.6306`, Turnover `3.98`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有2周, 换手12%, 出场92%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`19.69%` / `0.8044` / `-23.16%` / `3.40`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`21.04%` / `0.9456` / `-23.81%` / `1.77`

窗口指标（截至 `2026-06-11`，权重：2023-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `215.11%`, CAGR `13.15%`, Max DD `-26.28%`, Sharpe `0.6893`, Turnover `3.89`
- `2020-01-01` → `2026-06-11`: Total Return `189.21%`, CAGR `18.22%`, Max DD `-28.10%`, Sharpe `0.7958`, Turnover `3.52`
- `2023-01-01` → `2026-06-11`: Total Return `83.72%`, CAGR `19.69%`, Max DD `-23.16%`, Sharpe `0.8044`, Turnover `3.40`
- `2025-01-01` → `2026-06-11`: Total Return `111.46%`, CAGR `68.07%`, Max DD `-17.81%`, Sharpe `1.6356`, Turnover `6.31`
- `2026-01-01` → `2026-06-11`: Total Return `20.24%`, CAGR `54.61%`, Max DD `-10.32%`, Sharpe `1.5826`, Turnover `8.24`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市20%, 单票56%, 持有5周, 换手5%, 出场96%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`21.51%` / `0.9503` / `-23.89%` / `1.63`

窗口指标（截至 `2026-06-11`，权重：2020-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `173.25%`, CAGR `11.43%`, Max DD `-28.09%`, Sharpe `0.6541`, Turnover `2.09`
- `2020-01-01` → `2026-06-11`: Total Return `244.29%`, CAGR `21.51%`, Max DD `-23.89%`, Sharpe `0.9503`, Turnover `1.63`
- `2023-01-01` → `2026-06-11`: Total Return `67.19%`, CAGR `16.40%`, Max DD `-14.50%`, Sharpe `0.8860`, Turnover `1.65`
- `2025-01-01` → `2026-06-11`: Total Return `112.62%`, CAGR `68.71%`, Max DD `-14.92%`, Sharpe `1.6656`, Turnover `2.93`
- `2026-01-01` → `2026-06-11`: Total Return `29.73%`, CAGR `85.01%`, Max DD `-12.88%`, Sharpe `1.9168`, Turnover `2.09`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`297.98%` / `2.1138` / `-38.85%` / `15.14`

窗口指标（截至 `2026-06-11`，权重：2025-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `288.94%`, CAGR `15.75%`, Max DD `-63.08%`, Sharpe `0.5241`, Turnover `8.05`
- `2020-01-01` → `2026-06-11`: Total Return `128.05%`, CAGR `13.87%`, Max DD `-51.01%`, Sharpe `0.4826`, Turnover `9.27`
- `2023-01-01` → `2026-06-11`: Total Return `64.00%`, CAGR `15.74%`, Max DD `-52.31%`, Sharpe `0.5079`, Turnover `10.52`
- `2025-01-01` → `2026-06-11`: Total Return `633.13%`, CAGR `297.98%`, Max DD `-38.85%`, Sharpe `2.1138`, Turnover `15.14`
- `2026-01-01` → `2026-06-11`: Total Return `111.06%`, CAGR `484.49%`, Max DD `-20.73%`, Sharpe `3.1309`, Turnover `21.28`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有2周, 换手12%, 出场92%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`29.78%` / `13.15%` / `0.9813` / `-28.10%` / `4.28`

窗口指标：

- `2017-01-01` → `2026-06-11`: Total Return `215.11%`, CAGR `13.15%`, Max DD `-26.28%`, Sharpe `0.6893`, Turnover `3.89`
- `2020-01-01` → `2026-06-11`: Total Return `189.21%`, CAGR `18.22%`, Max DD `-28.10%`, Sharpe `0.7958`, Turnover `3.52`
- `2023-01-01` → `2026-06-11`: Total Return `83.72%`, CAGR `19.69%`, Max DD `-23.16%`, Sharpe `0.8044`, Turnover `3.40`
- `2025-01-01` → `2026-06-11`: Total Return `111.46%`, CAGR `68.07%`, Max DD `-17.81%`, Sharpe `1.6356`, Turnover `6.31`
- `2026-01-01` → `2026-06-11`: Total Return `20.24%`, CAGR `54.61%`, Max DD `-10.32%`, Sharpe `1.5826`, Turnover `8.24`

## Path 4：窗口跟踪赢家（观察）

### 2017 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市12%, 单票8%, 出场58%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.11%` / `0.8213` / `-16.86%` / `3.91`

窗口指标（截至 `2026-06-11`，权重：2017-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `222.23%`, CAGR `13.11%`, Max DD `-16.86%`, Sharpe `0.8213`, Turnover `3.91`
- `2020-01-01` → `2026-06-11`: Total Return `138.55%`, CAGR `14.31%`, Max DD `-15.22%`, Sharpe `0.8140`, Turnover `3.83`
- `2023-01-01` → `2026-06-11`: Total Return `41.44%`, CAGR `10.41%`, Max DD `-6.64%`, Sharpe `1.0379`, Turnover `3.31`
- `2025-01-01` → `2026-06-11`: Total Return `90.70%`, CAGR `53.78%`, Max DD `-6.58%`, Sharpe `1.8130`, Turnover `6.77`
- `2026-01-01` → `2026-06-11`: Total Return `29.09%`, CAGR `66.64%`, Max DD `-10.66%`, Sharpe `1.9115`, Turnover `6.93`

### 2023 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 信号28%, 龙头72%, 熊市15%, 单票12%, 出场64%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.55%` / `1.0499` / `-7.04%` / `3.48`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`34.53%` / `1.1460` / `-12.63%` / `3.13`

窗口指标（截至 `2026-06-11`，权重：2023-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `127.44%`, CAGR `9.03%`, Max DD `-24.22%`, Sharpe `0.6076`, Turnover `3.97`
- `2020-01-01` → `2026-06-11`: Total Return `41.30%`, CAGR `5.46%`, Max DD `-22.17%`, Sharpe `0.3884`, Turnover `4.01`
- `2023-01-01` → `2026-06-11`: Total Return `55.99%`, CAGR `13.55%`, Max DD `-7.04%`, Sharpe `1.0499`, Turnover `3.48`
- `2025-01-01` → `2026-06-11`: Total Return `71.19%`, CAGR `43.11%`, Max DD `-7.11%`, Sharpe `1.5508`, Turnover `6.93`
- `2026-01-01` → `2026-06-11`: Total Return `18.90%`, CAGR `41.37%`, Max DD `-9.35%`, Sharpe `1.4345`, Turnover `6.77`

### 2020 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`-4.22%` / `-0.1423` / `-47.40%` / `3.20`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市12%, 单票8%, 出场58%, 低换手)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`14.31%` / `0.8140` / `-15.22%` / `3.83`

窗口指标（截至 `2026-06-11`，权重：2020-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `110.11%`, CAGR `8.13%`, Max DD `-36.58%`, Sharpe `0.5190`, Turnover `3.36`
- `2020-01-01` → `2026-06-11`: Total Return `-24.42%`, CAGR `-4.22%`, Max DD `-47.40%`, Sharpe `-0.1423`, Turnover `3.20`
- `2023-01-01` → `2026-06-11`: Total Return `182.37%`, CAGR `34.53%`, Max DD `-12.63%`, Sharpe `1.1460`, Turnover `3.13`
- `2025-01-01` → `2026-06-11`: Total Return `47.10%`, CAGR `29.34%`, Max DD `-6.23%`, Sharpe `1.6329`, Turnover `4.89`
- `2026-01-01` → `2026-06-11`: Total Return `16.42%`, CAGR `35.54%`, Max DD `-3.42%`, Sharpe `1.4507`, Turnover `5.03`

### 2025 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`29.34%` / `1.6329` / `-6.23%` / `4.89`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市12%, 单票8%, 出场58%, 低换手)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`53.78%` / `1.8130` / `-6.58%` / `6.77`

窗口指标（截至 `2026-06-11`，权重：2025-01=100%）：

- `2017-01-01` → `2026-06-11`: Total Return `110.11%`, CAGR `8.13%`, Max DD `-36.58%`, Sharpe `0.5190`, Turnover `3.36`
- `2020-01-01` → `2026-06-11`: Total Return `-24.42%`, CAGR `-4.22%`, Max DD `-47.40%`, Sharpe `-0.1423`, Turnover `3.20`
- `2023-01-01` → `2026-06-11`: Total Return `182.37%`, CAGR `34.53%`, Max DD `-12.63%`, Sharpe `1.1460`, Turnover `3.13`
- `2025-01-01` → `2026-06-11`: Total Return `47.10%`, CAGR `29.34%`, Max DD `-6.23%`, Sharpe `1.6329`, Turnover `4.89`
- `2026-01-01` → `2026-06-11`: Total Return `16.42%`, CAGR `35.54%`, Max DD `-3.42%`, Sharpe `1.4507`, Turnover `5.03`

## Path 4：鲁棒候选（观察）

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市14%, 单票8%, 出场62%, 低换手)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`22.11%` / `11.09%` / `1.0978` / `-17.45%` / `4.49`

窗口指标：

- `2017-01-01` → `2026-06-11`: Total Return `184.94%`, CAGR `11.65%`, Max DD `-17.45%`, Sharpe `0.7459`, Turnover `3.95`
- `2020-01-01` → `2026-06-11`: Total Return `107.80%`, CAGR `11.91%`, Max DD `-17.45%`, Sharpe `0.7011`, Turnover `3.90`
- `2023-01-01` → `2026-06-11`: Total Return `44.51%`, CAGR `11.09%`, Max DD `-5.19%`, Sharpe `1.1312`, Turnover `3.36`
- `2025-01-01` → `2026-06-11`: Total Return `90.70%`, CAGR `53.78%`, Max DD `-6.58%`, Sharpe `1.8130`, Turnover `6.77`
- `2026-01-01` → `2026-06-11`: Total Return `29.09%`, CAGR `66.64%`, Max DD `-10.66%`, Sharpe `1.9115`, Turnover `6.93`

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
