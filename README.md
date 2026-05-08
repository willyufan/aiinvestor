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

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`24.15%` / `1.1599` / `-10.54%` / `0.63`

窗口指标（截至 `2026-05-07`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `666.86%`, CAGR `24.15%`, Max DD `-10.54%`, Sharpe `1.1599`, Turnover `0.63`
- `2020-01-01` → `2026-05-07`: Total Return `256.62%`, CAGR `21.92%`, Max DD `-15.81%`, Sharpe `0.9542`, Turnover `0.55`
- `2023-01-01` → `2026-05-07`: Total Return `121.84%`, CAGR `26.26%`, Max DD `-12.47%`, Sharpe `1.1103`, Turnover `0.60`
- `2025-01-01` → `2026-05-07`: Total Return `148.26%`, CAGR `90.00%`, Max DD `-9.50%`, Sharpe `1.9886`, Turnover `1.24`
- `2026-01-01` → `2026-05-07`: Total Return `-0.47%`, CAGR `-1.12%`, Max DD `-8.57%`, Sharpe `1.2714`, Turnover `1.33`

### 2023 窗口赢家

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`26.74%` / `1.1176` / `-12.55%` / `0.58`

窗口指标（截至 `2026-05-07`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `667.53%`, CAGR `24.40%`, Max DD `-10.65%`, Sharpe `1.1632`, Turnover `0.62`
- `2020-01-01` → `2026-05-07`: Total Return `255.40%`, CAGR `22.17%`, Max DD `-14.31%`, Sharpe `0.9632`, Turnover `0.54`
- `2023-01-01` → `2026-05-07`: Total Return `120.29%`, CAGR `26.74%`, Max DD `-12.55%`, Sharpe `1.1176`, Turnover `0.58`
- `2025-01-01` → `2026-05-07`: Total Return `154.31%`, CAGR `101.38%`, Max DD `-9.79%`, Sharpe `2.1042`, Turnover `1.21`
- `2026-01-01` → `2026-05-07`: Total Return `-0.43%`, CAGR `-1.30%`, Max DD `-8.35%`, Sharpe `1.4090`, Turnover `1.11`

### 2020 窗口赢家

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只__卫星周频三档风控(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`26.25%` / `0.9298` / `-21.53%` / `0.68`

窗口指标（截至 `2026-05-07`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `537.63%`, CAGR `21.74%`, Max DD `-23.43%`, Sharpe `0.9119`, Turnover `0.67`
- `2020-01-01` → `2026-05-07`: Total Return `346.22%`, CAGR `26.25%`, Max DD `-21.53%`, Sharpe `0.9298`, Turnover `0.68`
- `2023-01-01` → `2026-05-07`: Total Return `119.01%`, CAGR `25.79%`, Max DD `-27.82%`, Sharpe `0.8664`, Turnover `0.72`
- `2025-01-01` → `2026-05-07`: Total Return `143.58%`, CAGR `87.47%`, Max DD `-10.10%`, Sharpe `1.9270`, Turnover `1.08`
- `2026-01-01` → `2026-05-07`: Total Return `31.51%`, CAGR `92.97%`, Max DD `-3.61%`, Sharpe `2.8903`, Turnover `0.98`

### 2025 窗口赢家

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6_core_6_1__port_weekly_exposure_asym`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只(核心6-1动量)__月度选股_周度仓位调整(快减慢加)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`97.24%` / `2.2473` / `-9.43%` / `1.41`

窗口指标（截至 `2026-05-07`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `322.42%`, CAGR `16.53%`, Max DD `-43.53%`, Sharpe `0.7405`, Turnover `0.98`
- `2020-01-01` → `2026-05-07`: Total Return `198.68%`, CAGR `18.59%`, Max DD `-41.34%`, Sharpe `0.7232`, Turnover `1.02`
- `2023-01-01` → `2026-05-07`: Total Return `139.96%`, CAGR `29.20%`, Max DD `-36.34%`, Sharpe `0.9778`, Turnover `1.09`
- `2025-01-01` → `2026-05-07`: Total Return `161.76%`, CAGR `97.24%`, Max DD `-9.43%`, Sharpe `2.2473`, Turnover `1.41`
- `2026-01-01` → `2026-05-07`: Total Return `30.82%`, CAGR `90.55%`, Max DD `0.00%`, Sharpe `3.1217`, Turnover `1.48`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__port_weekly_exposure`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只__月度选股_周度仓位调整）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`44.09%` / `25.51%` / `1.1612` / `-30.84%` / `0.99`

窗口指标：

- `2017-01-01` → `2026-05-07`: Total Return `820.74%`, CAGR `26.85%`, Max DD `-27.72%`, Sharpe `1.0101`, Turnover `0.88`
- `2020-01-01` → `2026-05-07`: Total Return `321.66%`, CAGR `25.51%`, Max DD `-28.68%`, Sharpe `0.9408`, Turnover `0.89`
- `2023-01-01` → `2026-05-07`: Total Return `123.51%`, CAGR `27.29%`, Max DD `-30.84%`, Sharpe `0.8283`, Turnover `1.00`
- `2025-01-01` → `2026-05-07`: Total Return `146.48%`, CAGR `96.72%`, Max DD `-12.01%`, Sharpe `1.8657`, Turnover `1.18`
- `2026-01-01` → `2026-05-07`: Total Return `33.66%`, CAGR `138.79%`, Max DD `-5.77%`, Sharpe `2.6573`, Turnover `1.11`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 策略：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`35.95%` / `0.9471` / `-39.17%` / `3.87`

窗口指标（截至 `2026-05-07`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `1702.64%`, CAGR `35.95%`, Max DD `-39.17%`, Sharpe `0.9471`, Turnover `3.87`
- `2020-01-01` → `2026-05-07`: Total Return `1591.41%`, CAGR `55.39%`, Max DD `-36.62%`, Sharpe `1.2046`, Turnover `4.67`
- `2023-01-01` → `2026-05-07`: Total Return `430.18%`, CAGR `62.94%`, Max DD `-33.28%`, Sharpe `1.3555`, Turnover `4.40`
- `2025-01-01` → `2026-05-07`: Total Return `168.27%`, CAGR `100.69%`, Max DD `-14.22%`, Sharpe `1.8310`, Turnover `7.41`
- `2026-01-01` → `2026-05-07`: Total Return `53.13%`, CAGR `178.05%`, Max DD `0.00%`, Sharpe `3.2634`, Turnover `7.54`

### 2023 窗口赢家（Path 2）

- 策略：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 均线三档保留50%, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`67.32%` / `1.3533` / `-36.51%` / `4.79`

窗口指标（截至 `2026-05-07`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `1296.89%`, CAGR `32.32%`, Max DD `-41.54%`, Sharpe `0.9757`, Turnover `3.89`
- `2020-01-01` → `2026-05-07`: Total Return `1238.72%`, CAGR `49.83%`, Max DD `-39.65%`, Sharpe `1.2038`, Turnover `4.70`
- `2023-01-01` → `2026-05-07`: Total Return `480.52%`, CAGR `67.32%`, Max DD `-36.51%`, Sharpe `1.3533`, Turnover `4.79`
- `2025-01-01` → `2026-05-07`: Total Return `153.33%`, CAGR `92.73%`, Max DD `-14.29%`, Sharpe `1.9834`, Turnover `7.34`
- `2026-01-01` → `2026-05-07`: Total Return `38.71%`, CAGR `119.29%`, Max DD `0.00%`, Sharpe `3.7384`, Turnover `7.43`

### 2020 窗口赢家（Path 2）

- 策略：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`55.72%` / `1.2068` / `-36.55%` / `4.65`

窗口指标（截至 `2026-05-07`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `1696.46%`, CAGR `35.90%`, Max DD `-39.14%`, Sharpe `0.9426`, Turnover `3.86`
- `2020-01-01` → `2026-05-07`: Total Return `1614.78%`, CAGR `55.72%`, Max DD `-36.55%`, Sharpe `1.2068`, Turnover `4.65`
- `2023-01-01` → `2026-05-07`: Total Return `433.47%`, CAGR `63.23%`, Max DD `-33.36%`, Sharpe `1.3548`, Turnover `4.40`
- `2025-01-01` → `2026-05-07`: Total Return `168.73%`, CAGR `100.93%`, Max DD `-14.29%`, Sharpe `1.8214`, Turnover `7.39`
- `2026-01-01` → `2026-05-07`: Total Return `53.77%`, CAGR `180.85%`, Max DD `0.00%`, Sharpe `3.2688`, Turnover `7.53`

### 2025 窗口赢家（Path 2）

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`172.51%` / `1.6610` / `-40.77%` / `16.50`

窗口指标（截至 `2026-05-07`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `65.12%`, CAGR `5.61%`, Max DD `-74.57%`, Sharpe `0.3227`, Turnover `9.20`
- `2020-01-01` → `2026-05-07`: Total Return `189.76%`, CAGR `18.56%`, Max DD `-49.93%`, Sharpe `0.5621`, Turnover `8.78`
- `2023-01-01` → `2026-05-07`: Total Return `-10.87%`, CAGR `-3.44%`, Max DD `-54.14%`, Sharpe `0.1605`, Turnover `10.42`
- `2025-01-01` → `2026-05-07`: Total Return `285.55%`, CAGR `172.51%`, Max DD `-40.77%`, Sharpe `1.6610`, Turnover `16.50`
- `2026-01-01` → `2026-05-07`: Total Return `0.48%`, CAGR `0.34%`, Max DD `-22.34%`, Sharpe `0.4460`, Turnover `4.48`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 动量三档保留50%, 单票95%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`63.95%` / `35.90%` / `1.3314` / `-39.14%` / `5.08`

窗口指标：

- `2017-01-01` → `2026-05-07`: Total Return `1696.46%`, CAGR `35.90%`, Max DD `-39.14%`, Sharpe `0.9426`, Turnover `3.86`
- `2020-01-01` → `2026-05-07`: Total Return `1614.78%`, CAGR `55.72%`, Max DD `-36.55%`, Sharpe `1.2068`, Turnover `4.65`
- `2023-01-01` → `2026-05-07`: Total Return `433.47%`, CAGR `63.23%`, Max DD `-33.36%`, Sharpe `1.3548`, Turnover `4.40`
- `2025-01-01` → `2026-05-07`: Total Return `168.73%`, CAGR `100.93%`, Max DD `-14.29%`, Sharpe `1.8214`, Turnover `7.39`
- `2026-01-01` → `2026-05-07`: Total Return `53.77%`, CAGR `180.85%`, Max DD `0.00%`, Sharpe `3.2688`, Turnover `7.53`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`22.91%` / `0.7889` / `-40.04%` / `7.70`

窗口指标（截至 `2026-05-07`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `565.91%`, CAGR `22.91%`, Max DD `-40.04%`, Sharpe `0.7889`, Turnover `7.70`
- `2020-01-01` → `2026-05-07`: Total Return `181.18%`, CAGR `17.99%`, Max DD `-35.74%`, Sharpe `0.6223`, Turnover `8.22`
- `2023-01-01` → `2026-05-07`: Total Return `-2.35%`, CAGR `-0.72%`, Max DD `-38.94%`, Sharpe `0.1574`, Turnover `8.04`
- `2025-01-01` → `2026-05-07`: Total Return `45.15%`, CAGR `31.89%`, Max DD `-33.32%`, Sharpe `0.7911`, Turnover `16.59`
- `2026-01-01` → `2026-05-07`: Total Return `16.39%`, CAGR `11.31%`, Max DD `-20.34%`, Sharpe `0.8629`, Turnover `4.18`

### 2023 窗口赢家（Path 3）

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`34.31%` / `0.9391` / `-37.14%` / `13.59`

窗口指标（截至 `2026-05-07`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `251.48%`, CAGR `14.65%`, Max DD `-50.28%`, Sharpe `0.6078`, Turnover `12.03`
- `2020-01-01` → `2026-05-07`: Total Return `133.19%`, CAGR `14.51%`, Max DD `-51.71%`, Sharpe `0.5589`, Turnover `12.98`
- `2023-01-01` → `2026-05-07`: Total Return `163.83%`, CAGR `34.31%`, Max DD `-37.14%`, Sharpe `0.9391`, Turnover `13.59`
- `2025-01-01` → `2026-05-07`: Total Return `68.10%`, CAGR `47.09%`, Max DD `-27.38%`, Sharpe `1.2044`, Turnover `13.67`
- `2026-01-01` → `2026-05-07`: Total Return `52.94%`, CAGR `34.97%`, Max DD `-5.84%`, Sharpe `2.4353`, Turnover `3.11`

### 2020 窗口赢家（Path 3）

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`18.56%` / `0.5621` / `-49.93%` / `8.78`

窗口指标（截至 `2026-05-07`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `65.12%`, CAGR `5.61%`, Max DD `-74.57%`, Sharpe `0.3227`, Turnover `9.20`
- `2020-01-01` → `2026-05-07`: Total Return `189.76%`, CAGR `18.56%`, Max DD `-49.93%`, Sharpe `0.5621`, Turnover `8.78`
- `2023-01-01` → `2026-05-07`: Total Return `-10.87%`, CAGR `-3.44%`, Max DD `-54.14%`, Sharpe `0.1605`, Turnover `10.42`
- `2025-01-01` → `2026-05-07`: Total Return `285.55%`, CAGR `172.51%`, Max DD `-40.77%`, Sharpe `1.6610`, Turnover `16.50`
- `2026-01-01` → `2026-05-07`: Total Return `0.48%`, CAGR `0.34%`, Max DD `-22.34%`, Sharpe `0.4460`, Turnover `4.48`

### 2025 窗口赢家（Path 3）

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`172.51%` / `1.6610` / `-40.77%` / `16.50`

窗口指标（截至 `2026-05-07`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-07`: Total Return `65.12%`, CAGR `5.61%`, Max DD `-74.57%`, Sharpe `0.3227`, Turnover `9.20`
- `2020-01-01` → `2026-05-07`: Total Return `189.76%`, CAGR `18.56%`, Max DD `-49.93%`, Sharpe `0.5621`, Turnover `8.78`
- `2023-01-01` → `2026-05-07`: Total Return `-10.87%`, CAGR `-3.44%`, Max DD `-54.14%`, Sharpe `0.1605`, Turnover `10.42`
- `2025-01-01` → `2026-05-07`: Total Return `285.55%`, CAGR `172.51%`, Max DD `-40.77%`, Sharpe `1.6610`, Turnover `16.50`
- `2026-01-01` → `2026-05-07`: Total Return `0.48%`, CAGR `0.34%`, Max DD `-22.34%`, Sharpe `0.4460`, Turnover `4.48`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`48.31%` / `-3.44%` / `0.6766` / `-74.57%` / `11.22`

窗口指标：

- `2017-01-01` → `2026-05-07`: Total Return `65.12%`, CAGR `5.61%`, Max DD `-74.57%`, Sharpe `0.3227`, Turnover `9.20`
- `2020-01-01` → `2026-05-07`: Total Return `189.76%`, CAGR `18.56%`, Max DD `-49.93%`, Sharpe `0.5621`, Turnover `8.78`
- `2023-01-01` → `2026-05-07`: Total Return `-10.87%`, CAGR `-3.44%`, Max DD `-54.14%`, Sharpe `0.1605`, Turnover `10.42`
- `2025-01-01` → `2026-05-07`: Total Return `285.55%`, CAGR `172.51%`, Max DD `-40.77%`, Sharpe `1.6610`, Turnover `16.50`
- `2026-01-01` → `2026-05-07`: Total Return `0.48%`, CAGR `0.34%`, Max DD `-22.34%`, Sharpe `0.4460`, Turnover `4.48`

<!-- AUTO:WEIGHTED-WINNERS:END -->

当不同窗口的赢家不同时，项目会同时保留它们，作为防过拟合的护栏。README 中的 `strategy_comparison_*` 图展示跟踪赢家，`strategy_family_*` 图现在只展示默认参与展示的 **core active family**。更宽的 **research active family** 仍继续参与回测与迭代，用于保留更大的候选范围；历史实验策略会保留在 `results/` 中作为 **archive family** 供追溯，但默认不再进入 README、默认图表和默认比较脚本。

A 股各路径在四个窗口下的赢家变化历史，持续记录在：

- [HISTORY.md](HISTORY.md)
- [docs/path1_plan.md](docs/path1_plan.md)
- [docs/path2_plan.md](docs/path2_plan.md)

## 沪港通独立研究线

沪港通结果独立维护，不并入 A 股 `winner_only` 结论。`2026-04-22` 起，港股窗口的 `sample_start` 统一对齐到**首个可执行调仓点**，因此本节数值应以这次重算后的基线为准。

当前 tracked winners（数据截止 `2026-04-30`；月频、双周、周频信号生效日仍按各策略真实评估点生成）：

当前港股 `since_2017_01 / since_2020_01` 两个窗口都从首个可执行调仓点起算，因此这两个窗口的港股指标当前相同；月频 Path 1 起点为 `2021-01-04`，周频 Path 2 起点为 `2020-12-14`。

- Path 1：
  - `since_2017_01 / since_2020_01`：`hkconnect_path1_monthly_equal_buffered`
  - `since_2023_01 / since_2025_01`：`hkconnect_path1_weekly_equal_buffered`
  - robust candidate：`hkconnect_path1_weekly_equal_buffered`
- Path 2：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_fast_weekly`
  - `since_2023_01`：`hkconnect_path2_theme_fast_weekly`
  - `since_2025_01`：`hkconnect_path2_breakout_concentrated_monthly`
  - robust candidate：`hkconnect_path2_theme_fast_weekly`
- `since_2026_01`：只做观察，不进入 tracked winners；当前 raw leader 分别是 `hkconnect_path1_weekly_lowvol`（Path 1）与 `hkconnect_path2_breakout_concentrated_monthly`（Path 2）

关键窗口指标：

- Path 1 `since_2020_01`：`24.87% CAGR / -14.78% MaxDD / 1.4421 Sharpe / 2.80 Turnover`（`hkconnect_path1_monthly_equal_buffered`）
- Path 1 `since_2023_01`：`34.80% CAGR / -13.41% MaxDD / 1.5484 Sharpe / 10.62 Turnover`
- Path 1 `since_2025_01`：`48.95% CAGR / -13.41% MaxDD / 1.7009 Sharpe / 12.98 Turnover`
- Path 2 `since_2020_01`：`23.94% CAGR / -33.61% MaxDD / 0.9555 Sharpe / 30.45 Turnover`（`hkconnect_path2_theme_fast_weekly`）
- Path 2 `since_2023_01`：`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`（`hkconnect_path2_theme_fast_weekly`）
- Path 2 `since_2025_01`：`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`（`hkconnect_path2_breakout_concentrated_monthly`）

相关产物：

- [docs/path1_plan_hkconnect.md](docs/path1_plan_hkconnect.md)
- [docs/path2_plan_hkconnect.md](docs/path2_plan_hkconnect.md)
- [results_hkconnect/tracked_winners_hkconnect.json](results_hkconnect/tracked_winners_hkconnect.json)

![HK Connect Path1 Comparison](docs/strategy_comparison_hkconnect_path1.png)

![HK Connect Path2 Comparison](docs/strategy_comparison_hkconnect_path2.png)

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
