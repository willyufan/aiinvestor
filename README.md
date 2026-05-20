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

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`27.50%` / `1.0486` / `-26.16%` / `3.78`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`28.12%` / `1.1367` / `-29.73%` / `3.60`

窗口指标（截至 `2026-05-20`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `885.51%`, CAGR `27.50%`, Max DD `-26.16%`, Sharpe `1.0486`, Turnover `3.78`
- `2020-01-01` → `2026-05-20`: Total Return `363.08%`, CAGR `26.98%`, Max DD `-27.61%`, Sharpe `0.9114`, Turnover `3.72`
- `2023-01-01` → `2026-05-20`: Total Return `158.25%`, CAGR `32.01%`, Max DD `-29.57%`, Sharpe `0.9528`, Turnover `4.08`
- `2025-01-01` → `2026-05-20`: Total Return `172.11%`, CAGR `102.71%`, Max DD `-10.73%`, Sharpe `1.9878`, Turnover `4.73`
- `2026-01-01` → `2026-05-20`: Total Return `30.38%`, CAGR `89.03%`, Max DD `-11.84%`, Sharpe `1.8275`, Turnover `7.15`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`45.67%` / `1.2608` / `-34.22%` / `10.37`

窗口指标（截至 `2026-05-20`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `602.26%`, CAGR `23.00%`, Max DD `-46.61%`, Sharpe `0.7395`, Turnover `11.23`
- `2020-01-01` → `2026-05-20`: Total Return `536.16%`, CAGR `33.42%`, Max DD `-55.00%`, Sharpe `0.9052`, Turnover `12.50`
- `2023-01-01` → `2026-05-20`: Total Return `261.59%`, CAGR `45.67%`, Max DD `-34.22%`, Sharpe `1.2608`, Turnover `10.37`
- `2025-01-01` → `2026-05-20`: Total Return `147.53%`, CAGR `89.61%`, Max DD `-14.31%`, Sharpe `1.7795`, Turnover `10.36`
- `2026-01-01` → `2026-05-20`: Total Return `22.59%`, CAGR `63.05%`, Max DD `-14.57%`, Sharpe `1.4035`, Turnover `7.69`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`33.42%` / `0.9052` / `-55.00%` / `12.50`

窗口指标（截至 `2026-05-20`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `602.26%`, CAGR `23.00%`, Max DD `-46.61%`, Sharpe `0.7395`, Turnover `11.23`
- `2020-01-01` → `2026-05-20`: Total Return `536.16%`, CAGR `33.42%`, Max DD `-55.00%`, Sharpe `0.9052`, Turnover `12.50`
- `2023-01-01` → `2026-05-20`: Total Return `261.59%`, CAGR `45.67%`, Max DD `-34.22%`, Sharpe `1.2608`, Turnover `10.37`
- `2025-01-01` → `2026-05-20`: Total Return `147.53%`, CAGR `89.61%`, Max DD `-14.31%`, Sharpe `1.7795`, Turnover `10.36`
- `2026-01-01` → `2026-05-20`: Total Return `22.59%`, CAGR `63.05%`, Max DD `-14.57%`, Sharpe `1.4035`, Turnover `7.69`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只__月度选股_周度仓位调整(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`102.78%` / `1.9792` / `-10.81%` / `4.72`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_satellite_cost_guard`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(卫星成本防守)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`104.66%` / `2.0239` / `-10.27%` / `4.27`

窗口指标（截至 `2026-05-20`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `871.17%`, CAGR `27.31%`, Max DD `-25.98%`, Sharpe `1.0442`, Turnover `3.76`
- `2020-01-01` → `2026-05-20`: Total Return `362.62%`, CAGR `26.96%`, Max DD `-27.28%`, Sharpe `0.9143`, Turnover `3.73`
- `2023-01-01` → `2026-05-20`: Total Return `160.41%`, CAGR `32.33%`, Max DD `-29.18%`, Sharpe `0.9582`, Turnover `4.07`
- `2025-01-01` → `2026-05-20`: Total Return `172.23%`, CAGR `102.78%`, Max DD `-10.81%`, Sharpe `1.9792`, Turnover `4.72`
- `2026-01-01` → `2026-05-20`: Total Return `30.74%`, CAGR `90.26%`, Max DD `-11.84%`, Sharpe `1.8370`, Turnover `7.09`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`47.30%` / `26.98%` / `1.2252` / `-29.57%` / `4.08`

窗口指标：

- `2017-01-01` → `2026-05-20`: Total Return `885.51%`, CAGR `27.50%`, Max DD `-26.16%`, Sharpe `1.0486`, Turnover `3.78`
- `2020-01-01` → `2026-05-20`: Total Return `363.08%`, CAGR `26.98%`, Max DD `-27.61%`, Sharpe `0.9114`, Turnover `3.72`
- `2023-01-01` → `2026-05-20`: Total Return `158.25%`, CAGR `32.01%`, Max DD `-29.57%`, Sharpe `0.9528`, Turnover `4.08`
- `2025-01-01` → `2026-05-20`: Total Return `172.11%`, CAGR `102.71%`, Max DD `-10.73%`, Sharpe `1.9878`, Turnover `4.73`
- `2026-01-01` → `2026-05-20`: Total Return `30.38%`, CAGR `89.03%`, Max DD `-11.84%`, Sharpe `1.8275`, Turnover `7.15`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认65, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`37.34%` / `0.9921` / `-40.07%` / `4.09`

窗口指标（截至 `2026-05-20`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `1883.81%`, CAGR `37.34%`, Max DD `-40.07%`, Sharpe `0.9921`, Turnover `4.09`
- `2020-01-01` → `2026-05-20`: Total Return `1809.67%`, CAGR `58.35%`, Max DD `-40.74%`, Sharpe `1.2155`, Turnover `4.85`
- `2023-01-01` → `2026-05-20`: Total Return `404.19%`, CAGR `60.56%`, Max DD `-33.28%`, Sharpe `1.3214`, Turnover `4.45`
- `2025-01-01` → `2026-05-20`: Total Return `170.67%`, CAGR `101.95%`, Max DD `-14.23%`, Sharpe `1.8497`, Turnover `7.39`
- `2026-01-01` → `2026-05-20`: Total Return `-7.47%`, CAGR `-17.00%`, Max DD `-15.74%`, Sharpe `-0.4542`, Turnover `6.00`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 均线三档保留50%, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`67.11%` / `1.3503` / `-36.51%` / `4.80`

窗口指标（截至 `2026-05-20`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `1005.03%`, CAGR `29.06%`, Max DD `-42.42%`, Sharpe `0.9012`, Turnover `3.82`
- `2020-01-01` → `2026-05-20`: Total Return `1205.25%`, CAGR `49.24%`, Max DD `-48.68%`, Sharpe `1.1727`, Turnover `4.87`
- `2023-01-01` → `2026-05-20`: Total Return `477.99%`, CAGR `67.11%`, Max DD `-36.51%`, Sharpe `1.3503`, Turnover `4.80`
- `2025-01-01` → `2026-05-20`: Total Return `155.28%`, CAGR `93.78%`, Max DD `-14.30%`, Sharpe `2.0037`, Turnover `7.33`
- `2026-01-01` → `2026-05-20`: Total Return `-4.61%`, CAGR `-10.71%`, Max DD `-15.74%`, Sharpe `-0.2428`, Turnover `5.18`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`59.92%` / `1.2486` / `-34.58%` / `4.61`

窗口指标（截至 `2026-05-20`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `1551.80%`, CAGR `34.69%`, Max DD `-32.71%`, Sharpe `0.9486`, Turnover `4.14`
- `2020-01-01` → `2026-05-20`: Total Return `1934.38%`, CAGR `59.92%`, Max DD `-34.58%`, Sharpe `1.2486`, Turnover `4.61`
- `2023-01-01` → `2026-05-20`: Total Return `369.94%`, CAGR `57.29%`, Max DD `-29.20%`, Sharpe `1.3059`, Turnover `4.19`
- `2025-01-01` → `2026-05-20`: Total Return `171.15%`, CAGR `102.21%`, Max DD `-14.30%`, Sharpe `1.8400`, Turnover `7.38`
- `2026-01-01` → `2026-05-20`: Total Return `-7.82%`, CAGR `-17.75%`, Max DD `-15.74%`, Sharpe `-0.4862`, Turnover `5.97`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70`（核心90_探索10_总市值底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`150.68%` / `2.1552` / `-16.00%` / `6.64`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`217.60%` / `1.8676` / `-40.99%` / `16.78`

窗口指标（截至 `2026-05-20`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `436.80%`, CAGR `19.54%`, Max DD `-35.42%`, Sharpe `0.7677`, Turnover `4.33`
- `2020-01-01` → `2026-05-20`: Total Return `259.68%`, CAGR `22.08%`, Max DD `-40.47%`, Sharpe `0.6838`, Turnover `4.68`
- `2023-01-01` → `2026-05-20`: Total Return `186.97%`, CAGR `36.14%`, Max DD `-27.86%`, Sharpe `0.9431`, Turnover `4.29`
- `2025-01-01` → `2026-05-20`: Total Return `267.63%`, CAGR `150.68%`, Max DD `-16.00%`, Sharpe `2.1552`, Turnover `6.64`
- `2026-01-01` → `2026-05-20`: Total Return `19.33%`, CAGR `52.82%`, Max DD `-7.80%`, Sharpe `1.6904`, Turnover `8.51`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认65, 单票95%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`64.55%` / `37.34%` / `1.3447` / `-40.74%` / `5.20`

窗口指标：

- `2017-01-01` → `2026-05-20`: Total Return `1883.81%`, CAGR `37.34%`, Max DD `-40.07%`, Sharpe `0.9921`, Turnover `4.09`
- `2020-01-01` → `2026-05-20`: Total Return `1809.67%`, CAGR `58.35%`, Max DD `-40.74%`, Sharpe `1.2155`, Turnover `4.85`
- `2023-01-01` → `2026-05-20`: Total Return `404.19%`, CAGR `60.56%`, Max DD `-33.28%`, Sharpe `1.3214`, Turnover `4.45`
- `2025-01-01` → `2026-05-20`: Total Return `170.67%`, CAGR `101.95%`, Max DD `-14.23%`, Sharpe `1.8497`, Turnover `7.39`
- `2026-01-01` → `2026-05-20`: Total Return `-7.47%`, CAGR `-17.00%`, Max DD `-15.74%`, Sharpe `-0.4542`, Turnover `6.00`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`24.14%` / `0.8179` / `-40.18%` / `7.70`

窗口指标（截至 `2026-05-20`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `636.07%`, CAGR `24.14%`, Max DD `-40.18%`, Sharpe `0.8179`, Turnover `7.70`
- `2020-01-01` → `2026-05-20`: Total Return `210.50%`, CAGR `19.74%`, Max DD `-35.89%`, Sharpe `0.6619`, Turnover `8.20`
- `2023-01-01` → `2026-05-20`: Total Return `9.09%`, CAGR `2.65%`, Max DD `-38.83%`, Sharpe `0.2481`, Turnover `8.05`
- `2025-01-01` → `2026-05-20`: Total Return `60.56%`, CAGR `40.77%`, Max DD `-33.36%`, Sharpe `0.9268`, Turnover `16.89`
- `2026-01-01` → `2026-05-20`: Total Return `51.58%`, CAGR `212.18%`, Max DD `-14.43%`, Sharpe `2.6087`, Turnover `24.11`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票40%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`36.83%` / `0.9895` / `-37.13%` / `13.75`

窗口指标（截至 `2026-05-20`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `239.46%`, CAGR `14.16%`, Max DD `-50.02%`, Sharpe `0.5934`, Turnover `12.13`
- `2020-01-01` → `2026-05-20`: Total Return `111.64%`, CAGR `12.66%`, Max DD `-56.68%`, Sharpe `0.5122`, Turnover `12.95`
- `2023-01-01` → `2026-05-20`: Total Return `183.85%`, CAGR `36.83%`, Max DD `-37.13%`, Sharpe `0.9895`, Turnover `13.75`
- `2025-01-01` → `2026-05-20`: Total Return `78.68%`, CAGR `52.08%`, Max DD `-26.74%`, Sharpe `1.3009`, Turnover `13.71`
- `2026-01-01` → `2026-05-20`: Total Return `30.51%`, CAGR `107.27%`, Max DD `-12.12%`, Sharpe `2.4966`, Turnover `18.80`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`20.85%` / `0.7901` / `-25.90%` / `4.85`

窗口指标（截至 `2026-05-20`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `405.70%`, CAGR `19.19%`, Max DD `-30.32%`, Sharpe `0.8048`, Turnover `4.88`
- `2020-01-01` → `2026-05-20`: Total Return `228.95%`, CAGR `20.85%`, Max DD `-25.90%`, Sharpe `0.7901`, Turnover `4.85`
- `2023-01-01` → `2026-05-20`: Total Return `159.71%`, CAGR `33.23%`, Max DD `-37.59%`, Sharpe `0.9066`, Turnover `4.58`
- `2025-01-01` → `2026-05-20`: Total Return `50.87%`, CAGR `34.58%`, Max DD `-23.10%`, Sharpe `0.8907`, Turnover `10.05`
- `2026-01-01` → `2026-05-20`: Total Return `10.34%`, CAGR `30.90%`, Max DD `-12.70%`, Sharpe `0.9365`, Turnover `11.82`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票70%, 持有4周, 换手20%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`58.16%` / `1.1021` / `-25.69%` / `8.78`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`217.60%` / `1.8676` / `-40.99%` / `16.78`

窗口指标（截至 `2026-05-20`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `407.16%`, CAGR `19.23%`, Max DD `-30.35%`, Sharpe `0.7686`, Turnover `4.40`
- `2020-01-01` → `2026-05-20`: Total Return `195.58%`, CAGR `18.81%`, Max DD `-25.77%`, Sharpe `0.7347`, Turnover `4.25`
- `2023-01-01` → `2026-05-20`: Total Return `149.41%`, CAGR `31.62%`, Max DD `-37.62%`, Sharpe `0.8725`, Turnover `4.04`
- `2025-01-01` → `2026-05-20`: Total Return `88.66%`, CAGR `58.16%`, Max DD `-25.69%`, Sharpe `1.1021`, Turnover `8.78`
- `2026-01-01` → `2026-05-20`: Total Return `-7.36%`, CAGR `-18.88%`, Max DD `-20.44%`, Sharpe `-0.3133`, Turnover `11.65`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`26.96%` / `19.19%` / `0.8481` / `-37.59%` / `6.09`

窗口指标：

- `2017-01-01` → `2026-05-20`: Total Return `405.70%`, CAGR `19.19%`, Max DD `-30.32%`, Sharpe `0.8048`, Turnover `4.88`
- `2020-01-01` → `2026-05-20`: Total Return `228.95%`, CAGR `20.85%`, Max DD `-25.90%`, Sharpe `0.7901`, Turnover `4.85`
- `2023-01-01` → `2026-05-20`: Total Return `159.71%`, CAGR `33.23%`, Max DD `-37.59%`, Sharpe `0.9066`, Turnover `4.58`
- `2025-01-01` → `2026-05-20`: Total Return `50.87%`, CAGR `34.58%`, Max DD `-23.10%`, Sharpe `0.8907`, Turnover `10.05`
- `2026-01-01` → `2026-05-20`: Total Return `10.34%`, CAGR `30.90%`, Max DD `-12.70%`, Sharpe `0.9365`, Turnover `11.82`

## Path 4：窗口跟踪赢家（观察）

### 2017 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70`（核心90_探索10_等权底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 质量门槛, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`20.57%` / `0.8013` / `-35.67%` / `4.26`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心90_探索10_等权底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`25.82%` / `1.0259` / `-31.40%` / `3.66`

窗口指标（截至 `2026-05-20`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `482.21%`, CAGR `20.57%`, Max DD `-35.67%`, Sharpe `0.8013`, Turnover `4.26`
- `2020-01-01` → `2026-05-20`: Total Return `349.33%`, CAGR `26.39%`, Max DD `-36.18%`, Sharpe `0.7670`, Turnover `4.37`
- `2023-01-01` → `2026-05-20`: Total Return `154.16%`, CAGR `31.39%`, Max DD `-38.48%`, Sharpe `0.8056`, Turnover `4.64`
- `2025-01-01` → `2026-05-20`: Total Return `245.81%`, CAGR `140.08%`, Max DD `-17.55%`, Sharpe `1.9889`, Turnover `6.92`
- `2026-01-01` → `2026-05-20`: Total Return `29.86%`, CAGR `87.22%`, Max DD `-15.74%`, Sharpe `1.2542`, Turnover `8.69`

### 2023 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 质量门槛, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`36.86%` / `0.9994` / `-26.93%` / `3.99`

窗口指标（截至 `2026-05-20`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `369.80%`, CAGR `17.86%`, Max DD `-36.98%`, Sharpe `0.7316`, Turnover `4.06`
- `2020-01-01` → `2026-05-20`: Total Return `375.14%`, CAGR `27.49%`, Max DD `-34.39%`, Sharpe `0.8389`, Turnover `4.21`
- `2023-01-01` → `2026-05-20`: Total Return `192.13%`, CAGR `36.86%`, Max DD `-26.93%`, Sharpe `0.9994`, Turnover `3.99`
- `2025-01-01` → `2026-05-20`: Total Return `202.08%`, CAGR `118.23%`, Max DD `-15.22%`, Sharpe `1.9022`, Turnover `6.24`
- `2026-01-01` → `2026-05-20`: Total Return `45.28%`, CAGR `145.09%`, Max DD `0.00%`, Sharpe `5.0027`, Turnover `7.25`

### 2020 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`29.53%` / `0.8761` / `-35.62%` / `4.36`

窗口指标（截至 `2026-05-20`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `356.87%`, CAGR `17.51%`, Max DD `-34.66%`, Sharpe `0.7484`, Turnover `4.22`
- `2020-01-01` → `2026-05-20`: Total Return `425.99%`, CAGR `29.53%`, Max DD `-35.62%`, Sharpe `0.8761`, Turnover `4.36`
- `2023-01-01` → `2026-05-20`: Total Return `176.68%`, CAGR `34.70%`, Max DD `-26.85%`, Sharpe `0.9750`, Turnover `4.09`
- `2025-01-01` → `2026-05-20`: Total Return `220.53%`, CAGR `127.55%`, Max DD `-15.60%`, Sharpe `2.0446`, Turnover `6.27`
- `2026-01-01` → `2026-05-20`: Total Return `46.48%`, CAGR `149.94%`, Max DD `0.00%`, Sharpe `4.7296`, Turnover `7.33`

### 2025 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70`（核心90_探索10_总市值底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`150.68%` / `2.1552` / `-16.00%` / `6.64`

窗口指标（截至 `2026-05-20`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-20`: Total Return `436.80%`, CAGR `19.54%`, Max DD `-35.42%`, Sharpe `0.7677`, Turnover `4.33`
- `2020-01-01` → `2026-05-20`: Total Return `259.68%`, CAGR `22.08%`, Max DD `-40.47%`, Sharpe `0.6838`, Turnover `4.68`
- `2023-01-01` → `2026-05-20`: Total Return `186.97%`, CAGR `36.14%`, Max DD `-27.86%`, Sharpe `0.9431`, Turnover `4.29`
- `2025-01-01` → `2026-05-20`: Total Return `267.63%`, CAGR `150.68%`, Max DD `-16.00%`, Sharpe `2.1552`, Turnover `6.64`
- `2026-01-01` → `2026-05-20`: Total Return `19.33%`, CAGR `52.82%`, Max DD `-7.80%`, Sharpe `1.6904`, Turnover `8.51`

## Path 4：鲁棒候选（观察）

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`42.88%` / `21.82%` / `1.1328` / `-33.79%` / `4.24`

窗口指标：

- `2017-01-01` → `2026-05-20`: Total Return `694.50%`, CAGR `24.62%`, Max DD `-30.37%`, Sharpe `1.0032`, Turnover `3.41`
- `2020-01-01` → `2026-05-20`: Total Return `254.90%`, CAGR `21.82%`, Max DD `-33.79%`, Sharpe `0.7898`, Turnover `4.00`
- `2023-01-01` → `2026-05-20`: Total Return `156.40%`, CAGR `31.73%`, Max DD `-21.49%`, Sharpe `0.9435`, Turnover `3.41`
- `2025-01-01` → `2026-05-20`: Total Return `154.48%`, CAGR `93.35%`, Max DD `-18.05%`, Sharpe `1.7947`, Turnover `6.13`
- `2026-01-01` → `2026-05-20`: Total Return `45.00%`, CAGR `143.93%`, Max DD `0.00%`, Sharpe `4.4569`, Turnover `5.98`

<!-- AUTO:WEIGHTED-WINNERS:END -->

当不同窗口的赢家不同时，项目会同时保留它们，作为防过拟合的护栏。README 中的 `strategy_comparison_*` 图展示跟踪赢家，`strategy_family_*` 图现在只展示默认参与展示的 **core active family**。更宽的 **research active family** 仍继续参与回测与迭代，用于保留更大的候选范围；历史实验策略会保留在 `results/` 中作为 **archive family** 供追溯，但默认不再进入 README、默认图表和默认比较脚本。

A 股各路径在四个窗口下的赢家变化历史，持续记录在：

- [HISTORY.md](HISTORY.md)
- [docs/path1_plan.md](docs/path1_plan.md)
- [docs/path2_plan.md](docs/path2_plan.md)

## 沪港通独立研究线

沪港通结果独立维护，不并入 A 股 `winner_only` 结论。`2026-04-22` 起，港股窗口的 `sample_start` 统一对齐到**首个可执行调仓点**，因此本节数值应以这次重算后的基线为准。

当前 tracked winners（市场数据截止 `2026-05-19`；tracked payload `as_of=2026-05-15`；月频/双周信号生效日多为 `2026-04-30`，周频信号生效日可到 `2026-05-15`，信号生效日仍按各策略真实评估点生成）：

当前港股各窗口都从各自首个可执行调仓点起算；月频/双周 Path 1/2 当前信号样本多截止 `2026-04-30`，周频 Path 3 当前信号样本可到 `2026-05-15`。

三条研究路径按如下口径维护：

- **Path 1：实盘稳健线**，保留月度/双周稳健候选，后续主攻“月度调仓 + 周度风控/卫星”。
- **Path 2：收益上限探索线**，保留月度/双周高收益候选，继续探索主题、突破、高集中与高弹性结构。
- **Path 3：纯周度调仓线**，只纳入周度信号、周度换股候选，单独评估高频交易价值。

- Path 1：
  - `since_2017_01 / since_2020_01`：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`
  - `since_2023_01`：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`
  - `since_2025_01`：`hkconnect_path1_monthly_equal_buffered`
  - robust candidate：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`
- Path 2：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly_cost_control`
  - `since_2023_01`：`hkconnect_path2_theme_monthly`
  - `since_2025_01`：`hkconnect_path2_breakout_concentrated_monthly`
  - robust candidate：`hkconnect_path2_theme_monthly_cost_control`
- Path 3：
  - `since_2017_01`：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard`
  - `since_2020_01`：`hkconnect_path3_theme_fast_weekly_buffered`
  - `since_2023_01`：`hkconnect_path3_theme_fast_weekly_buffered`
  - `since_2025_01`：`hkconnect_path3_theme_fast_weekly_turnover_guard`
  - robust candidate：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard`
- `since_2026_01`：只做观察，不进入 tracked winners；当前 raw leader 分别是 `hkconnect_path1_biweekly_cashoff`（Path 1）、`hkconnect_path2_breakout_concentrated_monthly`（Path 2）与 `hkconnect_path3_equal_elastic_cashoff_weekly`（Path 3）

关键窗口指标：

- Path 1 `since_2020_01`：`32.33% CAGR / -14.83% MaxDD / 1.5504 Sharpe / 3.40 Turnover`（`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`）
- Path 1 `since_2023_01`：`34.60% CAGR / -14.83% MaxDD / 1.7299 Sharpe / 3.13 Turnover`（`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`）
- Path 1 `since_2025_01`：`40.41% CAGR / -14.79% MaxDD / 1.5271 Sharpe / 3.46 Turnover`（`hkconnect_path1_monthly_equal_buffered`）
- Path 2 `since_2020_01`：`29.86% CAGR / -19.10% MaxDD / 1.1680 Sharpe / 5.65 Turnover`（`hkconnect_path2_theme_monthly_cost_control`）
- Path 2 `since_2023_01`：`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`（`hkconnect_path2_theme_monthly`）
- Path 2 `since_2025_01`：`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`（`hkconnect_path2_breakout_concentrated_monthly`）
- Path 3 `since_2020_01`：`26.45% CAGR / -34.43% MaxDD / 0.8873 Sharpe / 30.99 Turnover`（`hkconnect_path3_theme_fast_weekly_buffered`）
- Path 3 `since_2023_01`：`38.29% CAGR / -19.56% MaxDD / 1.2502 Sharpe / 29.75 Turnover`（`hkconnect_path3_theme_fast_weekly_buffered`）
- Path 3 `since_2025_01`：`71.19% CAGR / -13.25% MaxDD / 1.8813 Sharpe / 31.96 Turnover`（`hkconnect_path3_theme_fast_weekly_turnover_guard`）

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
