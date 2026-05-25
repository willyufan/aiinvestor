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
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`28.09%` / `1.0607` / `-26.16%` / `3.78`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓)__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`28.83%` / `1.1502` / `-29.73%` / `3.61`

窗口指标（截至 `2026-05-25`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `929.29%`, CAGR `28.09%`, Max DD `-26.16%`, Sharpe `1.0607`, Turnover `3.78`
- `2020-01-01` → `2026-05-25`: Total Return `389.33%`, CAGR `28.08%`, Max DD `-27.61%`, Sharpe `0.9308`, Turnover `3.73`
- `2023-01-01` → `2026-05-25`: Total Return `168.09%`, CAGR `33.46%`, Max DD `-29.57%`, Sharpe `0.9748`, Turnover `4.09`
- `2025-01-01` → `2026-05-25`: Total Return `188.32%`, CAGR `111.16%`, Max DD `-10.73%`, Sharpe `2.0636`, Turnover `4.75`
- `2026-01-01` → `2026-05-25`: Total Return `42.08%`, CAGR `132.31%`, Max DD `-11.84%`, Sharpe `1.9893`, Turnover `7.23`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`44.06%` / `1.2292` / `-34.22%` / `10.44`

窗口指标（截至 `2026-05-25`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `575.81%`, CAGR `22.50%`, Max DD `-46.61%`, Sharpe `0.7280`, Turnover `11.25`
- `2020-01-01` → `2026-05-25`: Total Return `512.21%`, CAGR `32.63%`, Max DD `-55.00%`, Sharpe `0.8903`, Turnover `12.54`
- `2023-01-01` → `2026-05-25`: Total Return `248.12%`, CAGR `44.06%`, Max DD `-34.22%`, Sharpe `1.2292`, Turnover `10.44`
- `2025-01-01` → `2026-05-25`: Total Return `138.36%`, CAGR `84.62%`, Max DD `-14.31%`, Sharpe `1.7099`, Turnover `10.51`
- `2026-01-01` → `2026-05-25`: Total Return `20.97%`, CAGR `57.92%`, Max DD `-14.57%`, Sharpe `1.3326`, Turnover `7.69`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(量价前15%, 动量三档40%, 恢复70, 日级回撤防守50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`32.63%` / `0.8903` / `-55.00%` / `12.54`

窗口指标（截至 `2026-05-25`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `575.81%`, CAGR `22.50%`, Max DD `-46.61%`, Sharpe `0.7280`, Turnover `11.25`
- `2020-01-01` → `2026-05-25`: Total Return `512.21%`, CAGR `32.63%`, Max DD `-55.00%`, Sharpe `0.8903`, Turnover `12.54`
- `2023-01-01` → `2026-05-25`: Total Return `248.12%`, CAGR `44.06%`, Max DD `-34.22%`, Sharpe `1.2292`, Turnover `10.44`
- `2025-01-01` → `2026-05-25`: Total Return `138.36%`, CAGR `84.62%`, Max DD `-14.31%`, Sharpe `1.7099`, Turnover `10.51`
- `2026-01-01` → `2026-05-25`: Total Return `20.97%`, CAGR `57.92%`, Max DD `-14.57%`, Sharpe `1.3326`, Turnover `7.69`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只__月度选股_周度仓位调整(双周确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`111.23%` / `2.0543` / `-10.81%` / `4.74`

窗口指标（截至 `2026-05-25`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `914.72%`, CAGR `27.90%`, Max DD `-25.98%`, Sharpe `1.0564`, Turnover `3.76`
- `2020-01-01` → `2026-05-25`: Total Return `388.96%`, CAGR `28.06%`, Max DD `-27.28%`, Sharpe `0.9337`, Turnover `3.73`
- `2023-01-01` → `2026-05-25`: Total Return `170.49%`, CAGR `33.81%`, Max DD `-29.18%`, Sharpe `0.9804`, Turnover `4.08`
- `2025-01-01` → `2026-05-25`: Total Return `188.45%`, CAGR `111.23%`, Max DD `-10.81%`, Sharpe `2.0543`, Turnover `4.74`
- `2026-01-01` → `2026-05-25`: Total Return `42.38%`, CAGR `133.51%`, Max DD `-11.84%`, Sharpe `1.9980`, Turnover `7.18`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`50.20%` / `28.08%` / `1.2575` / `-29.57%` / `4.09`

窗口指标：

- `2017-01-01` → `2026-05-25`: Total Return `929.29%`, CAGR `28.09%`, Max DD `-26.16%`, Sharpe `1.0607`, Turnover `3.78`
- `2020-01-01` → `2026-05-25`: Total Return `389.33%`, CAGR `28.08%`, Max DD `-27.61%`, Sharpe `0.9308`, Turnover `3.73`
- `2023-01-01` → `2026-05-25`: Total Return `168.09%`, CAGR `33.46%`, Max DD `-29.57%`, Sharpe `0.9748`, Turnover `4.09`
- `2025-01-01` → `2026-05-25`: Total Return `188.32%`, CAGR `111.16%`, Max DD `-10.73%`, Sharpe `2.0636`, Turnover `4.75`
- `2026-01-01` → `2026-05-25`: Total Return `42.08%`, CAGR `132.31%`, Max DD `-11.84%`, Sharpe `1.9893`, Turnover `7.23`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认65, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`36.86%` / `0.9830` / `-40.07%` / `4.09`

窗口指标（截至 `2026-05-25`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `1819.23%`, CAGR `36.86%`, Max DD `-40.07%`, Sharpe `0.9830`, Turnover `4.09`
- `2020-01-01` → `2026-05-25`: Total Return `1747.55%`, CAGR `57.54%`, Max DD `-40.74%`, Sharpe `1.2039`, Turnover `4.85`
- `2023-01-01` → `2026-05-25`: Total Return `387.17%`, CAGR `58.95%`, Max DD `-33.28%`, Sharpe `1.2966`, Turnover `4.45`
- `2025-01-01` → `2026-05-25`: Total Return `161.53%`, CAGR `97.12%`, Max DD `-14.23%`, Sharpe `1.7893`, Turnover `7.39`
- `2026-01-01` → `2026-05-25`: Total Return `-8.42%`, CAGR `-19.02%`, Max DD `-15.74%`, Sharpe `-0.5455`, Turnover `6.00`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 均线三档保留50%, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`65.32%` / `1.3246` / `-36.51%` / `4.80`

窗口指标（截至 `2026-05-25`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `966.38%`, CAGR `28.58%`, Max DD `-42.42%`, Sharpe `0.8904`, Turnover `3.82`
- `2020-01-01` → `2026-05-25`: Total Return `1159.63%`, CAGR `48.41%`, Max DD `-48.68%`, Sharpe `1.1589`, Turnover `4.87`
- `2023-01-01` → `2026-05-25`: Total Return `457.08%`, CAGR `65.32%`, Max DD `-36.51%`, Sharpe `1.3246`, Turnover `4.80`
- `2025-01-01` → `2026-05-25`: Total Return `146.05%`, CAGR `88.81%`, Max DD `-14.30%`, Sharpe `1.9269`, Turnover `7.33`
- `2026-01-01` → `2026-05-25`: Total Return `-5.80%`, CAGR `-13.35%`, Max DD `-15.74%`, Sharpe `-0.3500`, Turnover `5.18`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95`（核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`59.04%` / `1.2359` / `-34.58%` / `4.61`

窗口指标（截至 `2026-05-25`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `1529.35%`, CAGR `34.50%`, Max DD `-32.71%`, Sharpe `0.9453`, Turnover `4.14`
- `2020-01-01` → `2026-05-25`: Total Return `1863.28%`, CAGR `59.04%`, Max DD `-34.58%`, Sharpe `1.2359`, Turnover `4.61`
- `2023-01-01` → `2026-05-25`: Total Return `352.93%`, CAGR `55.60%`, Max DD `-29.20%`, Sharpe `1.2782`, Turnover `4.19`
- `2025-01-01` → `2026-05-25`: Total Return `161.34%`, CAGR `97.02%`, Max DD `-14.30%`, Sharpe `1.7749`, Turnover `7.38`
- `2026-01-01` → `2026-05-25`: Total Return `-8.96%`, CAGR `-20.18%`, Max DD `-15.74%`, Sharpe `-0.5980`, Turnover `5.97`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70`（核心90_探索10_总市值底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`160.93%` / `2.2185` / `-16.00%` / `6.64`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`250.37%` / `1.9876` / `-40.99%` / `16.61`

窗口指标（截至 `2026-05-25`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `421.00%`, CAGR `19.16%`, Max DD `-35.42%`, Sharpe `0.7568`, Turnover `4.33`
- `2020-01-01` → `2026-05-25`: Total Return `249.32%`, CAGR `21.52%`, Max DD `-40.47%`, Sharpe `0.6722`, Turnover `4.68`
- `2023-01-01` → `2026-05-25`: Total Return `181.16%`, CAGR `35.33%`, Max DD `-27.86%`, Sharpe `0.9282`, Turnover `4.29`
- `2025-01-01` → `2026-05-25`: Total Return `289.10%`, CAGR `160.93%`, Max DD `-16.00%`, Sharpe `2.2185`, Turnover `6.64`
- `2026-01-01` → `2026-05-25`: Total Return `26.11%`, CAGR `74.51%`, Max DD `-7.80%`, Sharpe `1.9357`, Turnover `8.51`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`（核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升保留前60%, 恢复确认65, 单票95%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`62.62%` / `36.86%` / `1.3182` / `-40.74%` / `5.20`

窗口指标：

- `2017-01-01` → `2026-05-25`: Total Return `1819.23%`, CAGR `36.86%`, Max DD `-40.07%`, Sharpe `0.9830`, Turnover `4.09`
- `2020-01-01` → `2026-05-25`: Total Return `1747.55%`, CAGR `57.54%`, Max DD `-40.74%`, Sharpe `1.2039`, Turnover `4.85`
- `2023-01-01` → `2026-05-25`: Total Return `387.17%`, CAGR `58.95%`, Max DD `-33.28%`, Sharpe `1.2966`, Turnover `4.45`
- `2025-01-01` → `2026-05-25`: Total Return `161.53%`, CAGR `97.12%`, Max DD `-14.23%`, Sharpe `1.7893`, Turnover `7.39`
- `2026-01-01` → `2026-05-25`: Total Return `-8.42%`, CAGR `-19.02%`, Max DD `-15.74%`, Sharpe `-0.5455`, Turnover `6.00`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`25.11%` / `0.8391` / `-40.18%` / `7.70`

窗口指标（截至 `2026-05-25`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `694.29%`, CAGR `25.11%`, Max DD `-40.18%`, Sharpe `0.8391`, Turnover `7.70`
- `2020-01-01` → `2026-05-25`: Total Return `234.71%`, CAGR `21.11%`, Max DD `-35.89%`, Sharpe `0.6910`, Turnover `8.20`
- `2023-01-01` → `2026-05-25`: Total Return `17.83%`, CAGR `5.03%`, Max DD `-38.83%`, Sharpe `0.3100`, Turnover `8.03`
- `2025-01-01` → `2026-05-25`: Total Return `73.87%`, CAGR `48.29%`, Max DD `-33.36%`, Sharpe `1.0315`, Turnover `17.01`
- `2026-01-01` → `2026-05-25`: Total Return `63.44%`, CAGR `258.71%`, Max DD `-14.43%`, Sharpe `2.9255`, Turnover `24.21`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票40%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`37.26%` / `0.9991` / `-37.13%` / `13.73`

窗口指标（截至 `2026-05-25`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `249.99%`, CAGR `14.50%`, Max DD `-50.02%`, Sharpe `0.6035`, Turnover `12.14`
- `2020-01-01` → `2026-05-25`: Total Return `116.02%`, CAGR `12.99%`, Max DD `-56.68%`, Sharpe `0.5205`, Turnover `12.95`
- `2023-01-01` → `2026-05-25`: Total Return `188.56%`, CAGR `37.26%`, Max DD `-37.13%`, Sharpe `0.9991`, Turnover `13.73`
- `2025-01-01` → `2026-05-25`: Total Return `80.80%`, CAGR `52.48%`, Max DD `-26.74%`, Sharpe `1.3148`, Turnover `13.68`
- `2026-01-01` → `2026-05-25`: Total Return `34.01%`, CAGR `114.09%`, Max DD `-12.12%`, Sharpe `2.6487`, Turnover `18.84`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`21.04%` / `0.7956` / `-25.90%` / `4.87`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap90_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票90%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`21.62%` / `0.7006` / `-34.47%` / `7.99`

窗口指标（截至 `2026-05-25`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `412.71%`, CAGR `19.33%`, Max DD `-30.32%`, Sharpe `0.8089`, Turnover `4.89`
- `2020-01-01` → `2026-05-25`: Total Return `233.50%`, CAGR `21.04%`, Max DD `-25.90%`, Sharpe `0.7956`, Turnover `4.87`
- `2023-01-01` → `2026-05-25`: Total Return `157.17%`, CAGR `32.62%`, Max DD `-37.59%`, Sharpe `0.8964`, Turnover `4.61`
- `2025-01-01` → `2026-05-25`: Total Return `51.59%`, CAGR `34.50%`, Max DD `-23.10%`, Sharpe `0.8920`, Turnover `10.06`
- `2026-01-01` → `2026-05-25`: Total Return `9.32%`, CAGR `26.07%`, Max DD `-12.70%`, Sharpe `0.8413`, Turnover `11.75`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心70_探索30_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`150.15%` / `1.6042` / `-34.16%` / `19.42`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`250.37%` / `1.9876` / `-40.99%` / `16.61`

窗口指标（截至 `2026-05-25`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `106.07%`, CAGR `8.13%`, Max DD `-71.83%`, Sharpe `0.3774`, Turnover `10.06`
- `2020-01-01` → `2026-05-25`: Total Return `160.15%`, CAGR `16.37%`, Max DD `-54.16%`, Sharpe `0.5343`, Turnover `10.55`
- `2023-01-01` → `2026-05-25`: Total Return `132.15%`, CAGR `28.62%`, Max DD `-35.91%`, Sharpe `0.7241`, Turnover `11.41`
- `2025-01-01` → `2026-05-25`: Total Return `262.25%`, CAGR `150.15%`, Max DD `-34.16%`, Sharpe `1.6042`, Turnover `19.42`
- `2026-01-01` → `2026-05-25`: Total Return `78.39%`, CAGR `350.38%`, Max DD `-19.67%`, Sharpe `3.1106`, Turnover `25.93`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`（核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`26.87%` / `19.33%` / `0.8482` / `-37.59%` / `6.11`

窗口指标：

- `2017-01-01` → `2026-05-25`: Total Return `412.71%`, CAGR `19.33%`, Max DD `-30.32%`, Sharpe `0.8089`, Turnover `4.89`
- `2020-01-01` → `2026-05-25`: Total Return `233.50%`, CAGR `21.04%`, Max DD `-25.90%`, Sharpe `0.7956`, Turnover `4.87`
- `2023-01-01` → `2026-05-25`: Total Return `157.17%`, CAGR `32.62%`, Max DD `-37.59%`, Sharpe `0.8964`, Turnover `4.61`
- `2025-01-01` → `2026-05-25`: Total Return `51.59%`, CAGR `34.50%`, Max DD `-23.10%`, Sharpe `0.8920`, Turnover `10.06`
- `2026-01-01` → `2026-05-25`: Total Return `9.32%`, CAGR `26.07%`, Max DD `-12.70%`, Sharpe `0.8413`, Turnover `11.75`

## Path 4：窗口跟踪赢家（观察）

### 2017 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`24.73%` / `1.0060` / `-30.37%` / `3.41`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心90_探索10_等权底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`25.93%` / `1.0289` / `-31.40%` / `3.66`

窗口指标（截至 `2026-05-25`，权重：2017-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `700.93%`, CAGR `24.73%`, Max DD `-30.37%`, Sharpe `1.0060`, Turnover `3.41`
- `2020-01-01` → `2026-05-25`: Total Return `253.72%`, CAGR `21.76%`, Max DD `-33.79%`, Sharpe `0.7882`, Turnover `4.00`
- `2023-01-01` → `2026-05-25`: Total Return `164.55%`, CAGR `32.94%`, Max DD `-21.49%`, Sharpe `0.9666`, Turnover `3.41`
- `2025-01-01` → `2026-05-25`: Total Return `165.63%`, CAGR `99.29%`, Max DD `-18.05%`, Sharpe `1.8566`, Turnover `6.13`
- `2026-01-01` → `2026-05-25`: Total Return `51.99%`, CAGR `173.12%`, Max DD `0.00%`, Sharpe `4.2702`, Turnover `5.98`

### 2023 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70`（核心90_探索10_等权底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`36.13%` / `0.9315` / `-33.62%` / `4.51`

窗口指标（截至 `2026-05-25`，权重：2023-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `473.35%`, CAGR `20.38%`, Max DD `-35.36%`, Sharpe `0.7922`, Turnover `4.36`
- `2020-01-01` → `2026-05-25`: Total Return `203.31%`, CAGR `18.88%`, Max DD `-40.67%`, Sharpe `0.6168`, Turnover `4.64`
- `2023-01-01` → `2026-05-25`: Total Return `186.89%`, CAGR `36.13%`, Max DD `-33.62%`, Sharpe `0.9315`, Turnover `4.51`
- `2025-01-01` → `2026-05-25`: Total Return `251.01%`, CAGR `142.62%`, Max DD `-17.17%`, Sharpe `1.9896`, Turnover `7.18`
- `2026-01-01` → `2026-05-25`: Total Return `39.50%`, CAGR `122.32%`, Max DD `-15.31%`, Sharpe `1.5389`, Turnover `8.69`

### 2020 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`28.94%` / `0.8636` / `-35.62%` / `4.36`

窗口指标（截至 `2026-05-25`，权重：2020-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `343.76%`, CAGR `17.14%`, Max DD `-34.66%`, Sharpe `0.7370`, Turnover `4.22`
- `2020-01-01` → `2026-05-25`: Total Return `410.94%`, CAGR `28.94%`, Max DD `-35.62%`, Sharpe `0.8636`, Turnover `4.36`
- `2023-01-01` → `2026-05-25`: Total Return `171.04%`, CAGR `33.89%`, Max DD `-26.85%`, Sharpe `0.9587`, Turnover `4.09`
- `2025-01-01` → `2026-05-25`: Total Return `237.13%`, CAGR `135.81%`, Max DD `-15.60%`, Sharpe `2.1002`, Turnover `6.27`
- `2026-01-01` → `2026-05-25`: Total Return `53.73%`, CAGR `180.68%`, Max DD `0.00%`, Sharpe `4.3547`, Turnover `7.33`

### 2025 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70`（核心90_探索10_总市值底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`160.93%` / `2.2185` / `-16.00%` / `6.64`

窗口指标（截至 `2026-05-25`，权重：2025-01=100%）：

- `2017-01-01` → `2026-05-25`: Total Return `421.00%`, CAGR `19.16%`, Max DD `-35.42%`, Sharpe `0.7568`, Turnover `4.33`
- `2020-01-01` → `2026-05-25`: Total Return `249.32%`, CAGR `21.52%`, Max DD `-40.47%`, Sharpe `0.6722`, Turnover `4.68`
- `2023-01-01` → `2026-05-25`: Total Return `181.16%`, CAGR `35.33%`, Max DD `-27.86%`, Sharpe `0.9282`, Turnover `4.29`
- `2025-01-01` → `2026-05-25`: Total Return `289.10%`, CAGR `160.93%`, Max DD `-16.00%`, Sharpe `2.2185`, Turnover `6.64`
- `2026-01-01` → `2026-05-25`: Total Return `26.11%`, CAGR `74.51%`, Max DD `-7.80%`, Sharpe `1.9357`, Turnover `8.51`

## Path 4：鲁棒候选（观察）

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(强主题涌现, 熊市30%, 单票50%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`44.68%` / `21.76%` / `1.1543` / `-33.79%` / `4.24`

窗口指标：

- `2017-01-01` → `2026-05-25`: Total Return `700.93%`, CAGR `24.73%`, Max DD `-30.37%`, Sharpe `1.0060`, Turnover `3.41`
- `2020-01-01` → `2026-05-25`: Total Return `253.72%`, CAGR `21.76%`, Max DD `-33.79%`, Sharpe `0.7882`, Turnover `4.00`
- `2023-01-01` → `2026-05-25`: Total Return `164.55%`, CAGR `32.94%`, Max DD `-21.49%`, Sharpe `0.9666`, Turnover `3.41`
- `2025-01-01` → `2026-05-25`: Total Return `165.63%`, CAGR `99.29%`, Max DD `-18.05%`, Sharpe `1.8566`, Turnover `6.13`
- `2026-01-01` → `2026-05-25`: Total Return `51.99%`, CAGR `173.12%`, Max DD `0.00%`, Sharpe `4.2702`, Turnover `5.98`

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
