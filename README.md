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

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`27.24%` / `1.0410` / `-25.54%` / `3.78`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`27.90%` / `1.1385` / `-28.16%` / `3.62`

窗口指标（截至 `2026-05-19`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `866.55%`, CAGR `27.24%`, Max DD `-25.54%`, Sharpe `1.0410`, Turnover `3.78`
- `2020-01-01` → `2026-05-19`: Total Return `353.40%`, CAGR `26.56%`, Max DD `-27.46%`, Sharpe `0.9060`, Turnover `3.72`
- `2023-01-01` → `2026-05-19`: Total Return `154.67%`, CAGR `31.47%`, Max DD `-29.23%`, Sharpe `0.9443`, Turnover `4.08`
- `2025-01-01` → `2026-05-19`: Total Return `168.72%`, CAGR `100.93%`, Max DD `-10.72%`, Sharpe `1.9677`, Turnover `4.73`
- `2026-01-01` → `2026-05-19`: Total Return `28.34%`, CAGR `82.00%`, Max DD `-11.85%`, Sharpe `1.7690`, Turnover `7.15`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`43.66%` / `1.2176` / `-34.22%` / `10.35`

窗口指标（截至 `2026-05-19`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `627.22%`, CAGR `23.45%`, Max DD `-46.29%`, Sharpe `0.7491`, Turnover `11.20`
- `2020-01-01` → `2026-05-19`: Total Return `707.20%`, CAGR `38.47%`, Max DD `-46.00%`, Sharpe `1.0191`, Turnover `11.97`
- `2023-01-01` → `2026-05-19`: Total Return `244.80%`, CAGR `43.66%`, Max DD `-34.22%`, Sharpe `1.2176`, Turnover `10.35`
- `2025-01-01` → `2026-05-19`: Total Return `136.37%`, CAGR `83.53%`, Max DD `-13.73%`, Sharpe `1.7155`, Turnover `10.37`
- `2026-01-01` → `2026-05-19`: Total Return `21.99%`, CAGR `61.15%`, Max DD `-14.58%`, Sharpe `1.3884`, Turnover `7.69`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`38.47%` / `1.0191` / `-46.00%` / `11.97`

窗口指标（截至 `2026-05-19`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `627.22%`, CAGR `23.45%`, Max DD `-46.29%`, Sharpe `0.7491`, Turnover `11.20`
- `2020-01-01` → `2026-05-19`: Total Return `707.20%`, CAGR `38.47%`, Max DD `-46.00%`, Sharpe `1.0191`, Turnover `11.97`
- `2023-01-01` → `2026-05-19`: Total Return `244.80%`, CAGR `43.66%`, Max DD `-34.22%`, Sharpe `1.2176`, Turnover `10.35`
- `2025-01-01` → `2026-05-19`: Total Return `136.37%`, CAGR `83.53%`, Max DD `-13.73%`, Sharpe `1.7155`, Turnover `10.37`
- `2026-01-01` → `2026-05-19`: Total Return `21.99%`, CAGR `61.15%`, Max DD `-14.58%`, Sharpe `1.3884`, Turnover `7.69`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只__月度选股_周度仓位调整(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`100.94%` / `1.9577` / `-10.80%` / `4.74`

窗口指标（截至 `2026-05-19`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `853.68%`, CAGR `27.06%`, Max DD `-25.42%`, Sharpe `1.0369`, Turnover `3.76`
- `2020-01-01` → `2026-05-19`: Total Return `353.33%`, CAGR `26.56%`, Max DD `-27.00%`, Sharpe `0.9090`, Turnover `3.72`
- `2023-01-01` → `2026-05-19`: Total Return `155.43%`, CAGR `31.58%`, Max DD `-28.91%`, Sharpe `0.9463`, Turnover `4.06`
- `2025-01-01` → `2026-05-19`: Total Return `168.75%`, CAGR `100.94%`, Max DD `-10.80%`, Sharpe `1.9577`, Turnover `4.74`
- `2026-01-01` → `2026-05-19`: Total Return `28.68%`, CAGR `83.16%`, Max DD `-11.85%`, Sharpe `1.7784`, Turnover `7.09`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`46.55%` / `26.56%` / `1.2147` / `-29.23%` / `4.08`

窗口指标：

- `2017-01-01` → `2026-05-19`: Total Return `866.55%`, CAGR `27.24%`, Max DD `-25.54%`, Sharpe `1.0410`, Turnover `3.78`
- `2020-01-01` → `2026-05-19`: Total Return `353.40%`, CAGR `26.56%`, Max DD `-27.46%`, Sharpe `0.9060`, Turnover `3.72`
- `2023-01-01` → `2026-05-19`: Total Return `154.67%`, CAGR `31.47%`, Max DD `-29.23%`, Sharpe `0.9443`, Turnover `4.08`
- `2025-01-01` → `2026-05-19`: Total Return `168.72%`, CAGR `100.93%`, Max DD `-10.72%`, Sharpe `1.9677`, Turnover `4.73`
- `2026-01-01` → `2026-05-19`: Total Return `28.34%`, CAGR `82.00%`, Max DD `-11.85%`, Sharpe `1.7690`, Turnover `7.15`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`38.32%` / `1.1270` / `-32.76%` / `3.79`

窗口指标（截至 `2026-05-19`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `2021.48%`, CAGR `38.32%`, Max DD `-32.76%`, Sharpe `1.1270`, Turnover `3.79`
- `2020-01-01` → `2026-05-19`: Total Return `1303.39%`, CAGR `50.93%`, Max DD `-32.05%`, Sharpe `1.2029`, Turnover `4.40`
- `2023-01-01` → `2026-05-19`: Total Return `313.98%`, CAGR `51.56%`, Max DD `-29.13%`, Sharpe `1.2218`, Turnover `4.33`
- `2025-01-01` → `2026-05-19`: Total Return `175.15%`, CAGR `104.31%`, Max DD `-13.92%`, Sharpe `1.8721`, Turnover `7.38`
- `2026-01-01` → `2026-05-19`: Total Return `-7.22%`, CAGR `-16.46%`, Max DD `-15.74%`, Sharpe `-0.4301`, Turnover `6.00`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 均线三档保留50%, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`64.74%` / `1.3162` / `-36.51%` / `4.79`

窗口指标（截至 `2026-05-19`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `1229.68%`, CAGR `31.62%`, Max DD `-41.54%`, Sharpe `0.9604`, Turnover `3.89`
- `2020-01-01` → `2026-05-19`: Total Return `1174.35%`, CAGR `48.68%`, Max DD `-39.65%`, Sharpe `1.1840`, Turnover `4.70`
- `2023-01-01` → `2026-05-19`: Total Return `450.44%`, CAGR `64.74%`, Max DD `-36.51%`, Sharpe `1.3162`, Turnover `4.79`
- `2025-01-01` → `2026-05-19`: Total Return `143.08%`, CAGR `87.20%`, Max DD `-14.29%`, Sharpe `1.8943`, Turnover `7.34`
- `2026-01-01` → `2026-05-19`: Total Return `-4.37%`, CAGR `-10.18%`, Max DD `-15.74%`, Sharpe `-0.2213`, Turnover `5.19`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`58.19%` / `1.2371` / `-28.34%` / `4.49`

窗口指标（截至 `2026-05-19`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `1535.07%`, CAGR `34.55%`, Max DD `-31.89%`, Sharpe `0.9470`, Turnover `4.16`
- `2020-01-01` → `2026-05-19`: Total Return `1797.20%`, CAGR `58.19%`, Max DD `-28.34%`, Sharpe `1.2371`, Turnover `4.49`
- `2023-01-01` → `2026-05-19`: Total Return `347.68%`, CAGR `55.07%`, Max DD `-29.20%`, Sharpe `1.2694`, Turnover `4.19`
- `2025-01-01` → `2026-05-19`: Total Return `158.22%`, CAGR `95.35%`, Max DD `-14.29%`, Sharpe `1.7490`, Turnover `7.39`
- `2026-01-01` → `2026-05-19`: Total Return `-7.59%`, CAGR `-17.25%`, Max DD `-15.74%`, Sharpe `-0.4639`, Turnover `5.97`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升3只(核心6-1动量, 关闭熊市降仓, 单票60%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`142.81%` / `2.1070` / `-17.33%` / `5.94`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`207.27%` / `1.8271` / `-40.77%` / `16.79`

窗口指标（截至 `2026-05-19`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `381.35%`, CAGR `18.16%`, Max DD `-65.24%`, Sharpe `0.6524`, Turnover `5.18`
- `2020-01-01` → `2026-05-19`: Total Return `252.09%`, CAGR `21.67%`, Max DD `-66.07%`, Sharpe `0.6293`, Turnover `5.65`
- `2023-01-01` → `2026-05-19`: Total Return `350.30%`, CAGR `55.34%`, Max DD `-49.35%`, Sharpe `1.2339`, Turnover `5.42`
- `2025-01-01` → `2026-05-19`: Total Return `251.39%`, CAGR `142.81%`, Max DD `-17.33%`, Sharpe `2.1070`, Turnover `5.94`
- `2026-01-01` → `2026-05-19`: Total Return `32.51%`, CAGR `96.50%`, Max DD `-10.91%`, Sharpe `1.8002`, Turnover `6.34`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 单票95%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`61.28%` / `38.32%` / `1.3560` / `-32.76%` / `4.98`

窗口指标：

- `2017-01-01` → `2026-05-19`: Total Return `2021.48%`, CAGR `38.32%`, Max DD `-32.76%`, Sharpe `1.1270`, Turnover `3.79`
- `2020-01-01` → `2026-05-19`: Total Return `1303.39%`, CAGR `50.93%`, Max DD `-32.05%`, Sharpe `1.2029`, Turnover `4.40`
- `2023-01-01` → `2026-05-19`: Total Return `313.98%`, CAGR `51.56%`, Max DD `-29.13%`, Sharpe `1.2218`, Turnover `4.33`
- `2025-01-01` → `2026-05-19`: Total Return `175.15%`, CAGR `104.31%`, Max DD `-13.92%`, Sharpe `1.8721`, Turnover `7.38`
- `2026-01-01` → `2026-05-19`: Total Return `-7.22%`, CAGR `-16.46%`, Max DD `-15.74%`, Sharpe `-0.4301`, Turnover `6.00`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`23.83%` / `0.8103` / `-40.04%` / `7.71`

窗口指标（截至 `2026-05-19`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `619.22%`, CAGR `23.83%`, Max DD `-40.04%`, Sharpe `0.8103`, Turnover `7.71`
- `2020-01-01` → `2026-05-19`: Total Return `203.64%`, CAGR `19.32%`, Max DD `-35.74%`, Sharpe `0.6518`, Turnover `8.21`
- `2023-01-01` → `2026-05-19`: Total Return `5.19%`, CAGR `1.53%`, Max DD `-38.94%`, Sharpe `0.2186`, Turnover `8.03`
- `2025-01-01` → `2026-05-19`: Total Return `53.88%`, CAGR `36.52%`, Max DD `-33.32%`, Sharpe `0.8657`, Turnover `16.91`
- `2026-01-01` → `2026-05-19`: Total Return `45.79%`, CAGR `180.60%`, Max DD `-14.43%`, Sharpe `2.3921`, Turnover `24.11`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票40%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`35.28%` / `0.9638` / `-37.14%` / `13.65`

窗口指标（截至 `2026-05-19`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `209.54%`, CAGR `13.02%`, Max DD `-50.28%`, Sharpe `0.5632`, Turnover `12.18`
- `2020-01-01` → `2026-05-19`: Total Return `136.97%`, CAGR `14.71%`, Max DD `-51.71%`, Sharpe `0.5643`, Turnover `12.98`
- `2023-01-01` → `2026-05-19`: Total Return `173.28%`, CAGR `35.28%`, Max DD `-37.14%`, Sharpe `0.9638`, Turnover `13.65`
- `2025-01-01` → `2026-05-19`: Total Return `71.84%`, CAGR `47.85%`, Max DD `-27.38%`, Sharpe `1.2307`, Turnover `13.71`
- `2026-01-01` → `2026-05-19`: Total Return `33.66%`, CAGR `121.22%`, Max DD `-12.06%`, Sharpe `2.6427`, Turnover `18.39`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`14.72%` / `0.5646` / `-51.71%` / `12.99`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`21.04%` / `0.7916` / `-25.89%` / `4.78`

窗口指标（截至 `2026-05-19`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `265.56%`, CAGR `15.08%`, Max DD `-50.28%`, Sharpe `0.6207`, Turnover `12.06`
- `2020-01-01` → `2026-05-19`: Total Return `137.16%`, CAGR `14.72%`, Max DD `-51.71%`, Sharpe `0.5646`, Turnover `12.99`
- `2023-01-01` → `2026-05-19`: Total Return `169.79%`, CAGR `34.76%`, Max DD `-37.14%`, Sharpe `0.9503`, Turnover `13.59`
- `2025-01-01` → `2026-05-19`: Total Return `70.79%`, CAGR `47.19%`, Max DD `-27.38%`, Sharpe `1.2184`, Turnover `13.75`
- `2026-01-01` → `2026-05-19`: Total Return `32.98%`, CAGR `118.16%`, Max DD `-12.06%`, Sharpe `2.5951`, Turnover `18.28`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`49.44%` / `1.2264` / `-28.73%` / `14.62`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`207.27%` / `1.8271` / `-40.77%` / `16.79`

窗口指标（截至 `2026-05-19`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-19`: Total Return `268.13%`, CAGR `15.16%`, Max DD `-51.47%`, Sharpe `0.6198`, Turnover `12.51`
- `2020-01-01` → `2026-05-19`: Total Return `51.05%`, CAGR `6.78%`, Max DD `-60.66%`, Sharpe `0.3606`, Turnover `13.63`
- `2023-01-01` → `2026-05-19`: Total Return `145.61%`, CAGR `31.01%`, Max DD `-38.90%`, Sharpe `0.8695`, Turnover `14.02`
- `2025-01-01` → `2026-05-19`: Total Return `74.41%`, CAGR `49.44%`, Max DD `-28.73%`, Sharpe `1.2264`, Turnover `14.62`
- `2026-01-01` → `2026-05-19`: Total Return `30.46%`, CAGR `107.05%`, Max DD `-12.32%`, Sharpe `2.2158`, Turnover `18.94`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票70%, 持有4周, 换手20%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`29.87%` / `19.15%` / `0.8570` / `-37.68%` / `5.28`

窗口指标：

- `2017-01-01` → `2026-05-19`: Total Return `404.14%`, CAGR `19.15%`, Max DD `-30.35%`, Sharpe `0.7651`, Turnover `4.45`
- `2020-01-01` → `2026-05-19`: Total Return `213.83%`, CAGR `19.95%`, Max DD `-25.77%`, Sharpe `0.7494`, Turnover `4.06`
- `2023-01-01` → `2026-05-19`: Total Return `88.55%`, CAGR `21.00%`, Max DD `-37.68%`, Sharpe `0.7115`, Turnover `3.91`
- `2025-01-01` → `2026-05-19`: Total Return `90.64%`, CAGR `59.36%`, Max DD `-22.35%`, Sharpe `1.2018`, Turnover `8.69`
- `2026-01-01` → `2026-05-19`: Total Return `-10.93%`, CAGR `-27.15%`, Max DD `-22.48%`, Sharpe `-0.5657`, Turnover `11.66`

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
