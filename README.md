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
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`17.92%` / `0.7658` / `-39.58%` / `3.11`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`21.57%` / `0.8116` / `-37.13%` / `3.81`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `385.89%`, CAGR `17.92%`, Max DD `-39.58%`, Sharpe `0.7658`, Turnover `3.11`
- `2020-01-01` → `2026-08-04`: Total Return `290.52%`, CAGR `22.96%`, Max DD `-41.94%`, Sharpe `0.8218`, Turnover `3.39`
- `2023-01-01` → `2026-08-04`: Total Return `68.95%`, CAGR `15.73%`, Max DD `-42.76%`, Sharpe `0.5937`, Turnover `3.43`
- `2025-01-01` → `2026-08-04`: Total Return `83.91%`, CAGR `46.77%`, Max DD `-41.57%`, Sharpe `1.0001`, Turnover `4.91`
- `2026-01-01` → `2026-08-04`: Total Return `-5.62%`, CAGR `-9.36%`, Max DD `-43.18%`, Sharpe `0.3561`, Turnover `7.16`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`17.28%` / `0.6636` / `-34.17%` / `3.48`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(多因子质量价值行业成本守门再确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`15.74%` / `0.6528` / `-32.06%` / `3.16`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `108.67%`, CAGR `7.97%`, Max DD `-32.48%`, Sharpe `0.4944`, Turnover `3.19`
- `2020-01-01` → `2026-08-04`: Total Return `-1.06%`, CAGR `-0.16%`, Max DD `-32.56%`, Sharpe `0.0791`, Turnover `2.82`
- `2023-01-01` → `2026-08-04`: Total Return `77.20%`, CAGR `17.28%`, Max DD `-34.17%`, Sharpe `0.6636`, Turnover `3.48`
- `2025-01-01` → `2026-08-04`: Total Return `64.07%`, CAGR `36.59%`, Max DD `-32.77%`, Sharpe `0.9015`, Turnover `5.13`
- `2026-01-01` → `2026-08-04`: Total Return `-11.06%`, CAGR `-18.06%`, Max DD `-33.56%`, Sharpe `-0.0669`, Turnover `6.14`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`22.96%` / `0.8218` / `-41.94%` / `3.39`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `385.89%`, CAGR `17.92%`, Max DD `-39.58%`, Sharpe `0.7658`, Turnover `3.11`
- `2020-01-01` → `2026-08-04`: Total Return `290.52%`, CAGR `22.96%`, Max DD `-41.94%`, Sharpe `0.8218`, Turnover `3.39`
- `2023-01-01` → `2026-08-04`: Total Return `68.95%`, CAGR `15.73%`, Max DD `-42.76%`, Sharpe `0.5937`, Turnover `3.43`
- `2025-01-01` → `2026-08-04`: Total Return `83.91%`, CAGR `46.77%`, Max DD `-41.57%`, Sharpe `1.0001`, Turnover `4.91`
- `2026-01-01` → `2026-08-04`: Total Return `-5.62%`, CAGR `-9.36%`, Max DD `-43.18%`, Sharpe `0.3561`, Turnover `7.16`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`（核心80_探索20_总市值底座_胜出者核心__比例24/76(2+8 分步加仓62成本防守)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`56.28%` / `1.1230` / `-36.23%` / `4.64`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `254.42%`, CAGR `14.11%`, Max DD `-33.90%`, Sharpe `0.6312`, Turnover `2.75`
- `2020-01-01` → `2026-08-04`: Total Return `188.78%`, CAGR `17.46%`, Max DD `-40.31%`, Sharpe `0.6533`, Turnover `3.03`
- `2023-01-01` → `2026-08-04`: Total Return `77.84%`, CAGR `17.40%`, Max DD `-39.23%`, Sharpe `0.6033`, Turnover `3.06`
- `2025-01-01` → `2026-08-04`: Total Return `103.20%`, CAGR `56.28%`, Max DD `-36.23%`, Sharpe `1.1230`, Turnover `4.64`
- `2026-01-01` → `2026-08-04`: Total Return `-0.08%`, CAGR `-0.14%`, Max DD `-38.40%`, Sharpe `0.3630`, Turnover `5.87`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_satellite_cost_guard`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(卫星成本防守)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`25.98%` / `18.20%` / `0.7305` / `-41.83%` / `3.58`

窗口指标：

- `2017-01-01` → `2026-08-04`: Total Return `397.04%`, CAGR `18.20%`, Max DD `-41.26%`, Sharpe `0.7140`, Turnover `3.02`
- `2020-01-01` → `2026-08-04`: Total Return `204.48%`, CAGR `18.41%`, Max DD `-41.53%`, Sharpe `0.6419`, Turnover `3.30`
- `2023-01-01` → `2026-08-04`: Total Return `83.59%`, CAGR `18.44%`, Max DD `-41.83%`, Sharpe `0.5840`, Turnover `3.48`
- `2025-01-01` → `2026-08-04`: Total Return `88.07%`, CAGR `48.85%`, Max DD `-41.07%`, Sharpe `0.9820`, Turnover `4.51`
- `2026-01-01` → `2026-08-04`: Total Return `-3.86%`, CAGR `-6.47%`, Max DD `-44.30%`, Sharpe `0.3296`, Turnover `5.60`

## Path 1：组合方案

- 组合ID：`path1_composite_robust_window_blend_v1`
- 组合逻辑：不再要求单一 winner 覆盖所有行情，按鲁棒候选与窗口赢家合并权重。
- 组合鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`25.18%` / `17.16%` / `0.7686` / `-41.03%` / `3.63`

当前组合成分：

- `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_satellite_cost_guard`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(卫星成本防守)）：`45.0%`；来源：robust-candidate
- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）：`40.0%`；来源：2017-01, 2020-01
- `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）：`10.0%`；来源：2023-01
- `core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`（核心80_探索20_总市值底座_胜出者核心__比例24/76(2+8 分步加仓62成本防守)）：`5.0%`；来源：2025-01

组合窗口指标：

- `2017-01-01` → `2026-08-04`: Total Return `356.61%`, CAGR `17.16%`, Max DD `-38.80%`, Sharpe `0.7370`, Turnover `3.06`
- `2020-01-01` → `2026-08-04`: Total Return `217.56%`, CAGR `19.16%`, Max DD `-40.45%`, Sharpe `0.7129`, Turnover `3.28`
- `2023-01-01` → `2026-08-04`: Total Return `76.81%`, CAGR `17.21%`, Max DD `-41.03%`, Sharpe `0.6146`, Turnover `3.44`
- `2025-01-01` → `2026-08-04`: Total Return `84.76%`, CAGR `47.20%`, Max DD `-39.86%`, Sharpe `1.0099`, Turnover `4.74`
- `2026-01-01` → `2026-08-04`: Total Return `-5.10%`, CAGR `-8.50%`, Max DD `-42.34%`, Sharpe `0.2805`, Turnover `6.29`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`（核心90_探索10_总市值底座_胜出者核心__进攻4/96 晋升4只(量价前12%, 动量三档26%, 出场46%, 恢复96, 谨慎58%, 单票22%, 成本防守v30中周期)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`12.90%` / `0.8160` / `-15.80%` / `4.45`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(多因子质量价值行业成本守门再确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`3.05%` / `0.2630` / `-32.69%` / `3.00`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `220.15%`, CAGR `12.90%`, Max DD `-15.80%`, Sharpe `0.8160`, Turnover `4.45`
- `2020-01-01` → `2026-08-04`: Total Return `112.46%`, CAGR `12.11%`, Max DD `-14.98%`, Sharpe `0.7437`, Turnover `3.88`
- `2023-01-01` → `2026-08-04`: Total Return `-9.62%`, CAGR `-2.78%`, Max DD `-34.85%`, Sharpe `0.0396`, Turnover `3.75`
- `2025-01-01` → `2026-08-04`: Total Return `20.47%`, CAGR `12.45%`, Max DD `-37.50%`, Sharpe `0.5368`, Turnover `10.05`
- `2026-01-01` → `2026-08-04`: Total Return `-24.03%`, CAGR `-37.31%`, Max DD `-37.50%`, Sharpe `-0.4060`, Turnover `10.25`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm80_amt110_cap95`（核心90_探索10_总市值底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升确认80+量能110, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`37.05%` / `0.9405` / `-39.73%` / `1.94`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(多因子质量价值行业成本守门再确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`15.74%` / `0.6528` / `-32.06%` / `3.16`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `35.06%`, CAGR `3.18%`, Max DD `-60.28%`, Sharpe `0.2442`, Turnover `3.10`
- `2020-01-01` → `2026-08-04`: Total Return `-60.13%`, CAGR `-13.02%`, Max DD `-69.67%`, Sharpe `-0.3376`, Turnover `2.99`
- `2023-01-01` → `2026-08-04`: Total Return `209.95%`, CAGR `37.05%`, Max DD `-39.73%`, Sharpe `0.9405`, Turnover `1.94`
- `2025-01-01` → `2026-08-04`: Total Return `119.26%`, CAGR `63.95%`, Max DD `-30.69%`, Sharpe `1.1811`, Turnover `4.84`
- `2026-01-01` → `2026-08-04`: Total Return `-19.81%`, CAGR `-31.27%`, Max DD `-30.51%`, Sharpe `-0.7653`, Turnover `6.52`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`（核心90_探索10_总市值底座_胜出者核心__进攻4/96 晋升4只(量价前12%, 动量三档26%, 出场46%, 恢复96, 谨慎58%, 单票22%, 成本防守v30中周期)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`12.11%` / `0.7437` / `-14.98%` / `3.88`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn`（核心60_探索40_等权底座_胜出者核心__进攻3/97 晋升3只(量价弹性双周, 风险16%, 出场36%, 单票10%, 成本防守v70欠配低换手)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`5.13%` / `0.3298` / `-29.14%` / `7.90`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `220.15%`, CAGR `12.90%`, Max DD `-15.80%`, Sharpe `0.8160`, Turnover `4.45`
- `2020-01-01` → `2026-08-04`: Total Return `112.46%`, CAGR `12.11%`, Max DD `-14.98%`, Sharpe `0.7437`, Turnover `3.88`
- `2023-01-01` → `2026-08-04`: Total Return `-9.62%`, CAGR `-2.78%`, Max DD `-34.85%`, Sharpe `0.0396`, Turnover `3.75`
- `2025-01-01` → `2026-08-04`: Total Return `20.47%`, CAGR `12.45%`, Max DD `-37.50%`, Sharpe `0.5368`, Turnover `10.05`
- `2026-01-01` → `2026-08-04`: Total Return `-24.03%`, CAGR `-37.31%`, Max DD `-37.50%`, Sharpe `-0.4060`, Turnover `10.25`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_confirm80_amt110_cap95`（核心90_探索10_总市值底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留50%, 晋升确认80+量能110, 单票95%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`63.95%` / `1.1811` / `-30.69%` / `4.84`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `35.06%`, CAGR `3.18%`, Max DD `-60.28%`, Sharpe `0.2442`, Turnover `3.10`
- `2020-01-01` → `2026-08-04`: Total Return `-60.13%`, CAGR `-13.02%`, Max DD `-69.67%`, Sharpe `-0.3376`, Turnover `2.99`
- `2023-01-01` → `2026-08-04`: Total Return `209.95%`, CAGR `37.05%`, Max DD `-39.73%`, Sharpe `0.9405`, Turnover `1.94`
- `2025-01-01` → `2026-08-04`: Total Return `119.26%`, CAGR `63.95%`, Max DD `-30.69%`, Sharpe `1.1811`, Turnover `4.84`
- `2026-01-01` → `2026-08-04`: Total Return `-19.81%`, CAGR `-31.27%`, Max DD `-30.51%`, Sharpe `-0.7653`, Turnover `6.52`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(多因子质量价值行业成本守门再确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`8.80%` / `-3.18%` / `0.3921` / `-32.69%` / `3.54`

窗口指标：

- `2017-01-01` → `2026-08-04`: Total Return `33.43%`, CAGR `3.05%`, Max DD `-32.69%`, Sharpe `0.2630`, Turnover `3.00`
- `2020-01-01` → `2026-08-04`: Total Return `-19.21%`, CAGR `-3.18%`, Max DD `-31.28%`, Sharpe `-0.0626`, Turnover `2.63`
- `2023-01-01` → `2026-08-04`: Total Return `68.97%`, CAGR `15.74%`, Max DD `-32.06%`, Sharpe `0.6528`, Turnover `3.16`
- `2025-01-01` → `2026-08-04`: Total Return `32.85%`, CAGR `19.59%`, Max DD `-27.36%`, Sharpe `0.7151`, Turnover `5.37`
- `2026-01-01` → `2026-08-04`: Total Return `-4.75%`, CAGR `-7.93%`, Max DD `-19.51%`, Sharpe `-0.1842`, Turnover `7.07`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市16%, 单票54%, 持有5周, 换手5%, 出场98%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`7.87%` / `0.4663` / `-36.90%` / `2.08`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市6%, 单票30%, 持有11周, 换手2%, 出场98%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`2.26%` / `0.4326` / `-16.17%` / `0.41`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `104.45%`, CAGR `7.87%`, Max DD `-36.90%`, Sharpe `0.4663`, Turnover `2.08`
- `2020-01-01` → `2026-08-04`: Total Return `161.54%`, CAGR `15.94%`, Max DD `-38.21%`, Sharpe `0.7094`, Turnover `1.54`
- `2023-01-01` → `2026-08-04`: Total Return `19.01%`, CAGR `5.04%`, Max DD `-37.90%`, Sharpe `0.3302`, Turnover `1.37`
- `2025-01-01` → `2026-08-04`: Total Return `60.29%`, CAGR `34.39%`, Max DD `-37.83%`, Sharpe `0.9451`, Turnover `2.98`
- `2026-01-01` → `2026-08-04`: Total Return `17.00%`, CAGR `31.28%`, Max DD `-21.48%`, Sharpe `0.9112`, Turnover `1.85`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_weekly`（核心70_探索30_等权底座_胜出者核心__进攻2/98 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`27.21%` / `0.6942` / `-35.99%` / `11.77`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市14%, 单票46%, 持有7周, 换手3%, 出场98%, 单周换手修复)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`8.55%` / `0.7649` / `-14.28%` / `0.47`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `607.56%`, CAGR `23.03%`, Max DD `-49.98%`, Sharpe `0.6837`, Turnover `9.39`
- `2020-01-01` → `2026-08-04`: Total Return `50.88%`, CAGR `6.53%`, Max DD `-53.63%`, Sharpe `0.3512`, Turnover `10.96`
- `2023-01-01` → `2026-08-04`: Total Return `134.31%`, CAGR `27.21%`, Max DD `-35.99%`, Sharpe `0.6942`, Turnover `11.77`
- `2025-01-01` → `2026-08-04`: Total Return `285.52%`, CAGR `132.89%`, Max DD `-35.62%`, Sharpe `1.4618`, Turnover `18.40`
- `2026-01-01` → `2026-08-04`: Total Return `44.88%`, CAGR `90.14%`, Max DD `-46.62%`, Sharpe `1.2322`, Turnover `23.26`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.25%` / `0.6665` / `-27.42%` / `1.87`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市16%, 单票54%, 持有5周, 换手5%, 出场98%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`15.94%` / `0.7094` / `-38.21%` / `1.54`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `132.03%`, CAGR `9.32%`, Max DD `-32.32%`, Sharpe `0.5659`, Turnover `2.20`
- `2020-01-01` → `2026-08-04`: Total Return `124.48%`, CAGR `13.25%`, Max DD `-27.42%`, Sharpe `0.6665`, Turnover `1.87`
- `2023-01-01` → `2026-08-04`: Total Return `54.16%`, CAGR `13.01%`, Max DD `-29.31%`, Sharpe `0.6138`, Turnover `1.83`
- `2025-01-01` → `2026-08-04`: Total Return `62.56%`, CAGR `35.58%`, Max DD `-36.48%`, Sharpe `1.0232`, Turnover `3.67`
- `2026-01-01` → `2026-08-04`: Total Return `-1.83%`, CAGR `-3.15%`, Max DD `-31.33%`, Sharpe `0.1363`, Turnover `4.55`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心70_探索30_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`133.65%` / `1.4625` / `-35.61%` / `18.21`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`225.21%` / `1.8326` / `-41.25%` / `15.31`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `481.78%`, CAGR `20.50%`, Max DD `-50.80%`, Sharpe `0.6322`, Turnover `9.30`
- `2020-01-01` → `2026-08-04`: Total Return `48.91%`, CAGR `6.32%`, Max DD `-54.41%`, Sharpe `0.3473`, Turnover `10.86`
- `2023-01-01` → `2026-08-04`: Total Return `133.55%`, CAGR `27.09%`, Max DD `-36.07%`, Sharpe `0.6911`, Turnover `11.70`
- `2025-01-01` → `2026-08-04`: Total Return `287.50%`, CAGR `133.65%`, Max DD `-35.61%`, Sharpe `1.4625`, Turnover `18.21`
- `2026-01-01` → `2026-08-04`: Total Return `45.86%`, CAGR `92.38%`, Max DD `-46.70%`, Sharpe `1.2469`, Turnover `22.99`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市14%, 单票46%, 持有7周, 换手3%, 出场98%, 单周换手修复)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`12.43%` / `4.03%` / `0.7068` / `-27.82%` / `0.63`

窗口指标：

- `2017-01-01` → `2026-08-04`: Total Return `45.27%`, CAGR `4.03%`, Max DD `-22.92%`, Sharpe `0.4305`, Turnover `0.80`
- `2020-01-01` → `2026-08-04`: Total Return `59.16%`, CAGR `7.41%`, Max DD `-27.82%`, Sharpe `0.5238`, Turnover `0.66`
- `2023-01-01` → `2026-08-04`: Total Return `33.68%`, CAGR `8.55%`, Max DD `-14.28%`, Sharpe `0.7649`, Turnover `0.47`
- `2025-01-01` → `2026-08-04`: Total Return `51.50%`, CAGR `29.73%`, Max DD `-14.74%`, Sharpe `1.1082`, Turnover `0.57`
- `2026-01-01` → `2026-08-04`: Total Return `11.36%`, CAGR `20.49%`, Max DD `-33.64%`, Sharpe `0.6214`, Turnover `2.56`

## Path 4：窗口跟踪赢家（观察）

### 2017 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`（核心90_探索10_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`4.99%` / `0.4968` / `-19.28%` / `2.64`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `59.52%`, CAGR `4.99%`, Max DD `-19.28%`, Sharpe `0.4968`, Turnover `2.64`
- `2020-01-01` → `2026-08-04`: Total Return `32.51%`, CAGR `4.36%`, Max DD `-21.16%`, Sharpe `0.3999`, Turnover `2.62`
- `2023-01-01` → `2026-08-04`: Total Return `-3.17%`, CAGR `-0.89%`, Max DD `-19.52%`, Sharpe `0.0356`, Turnover `1.98`
- `2025-01-01` → `2026-08-04`: Total Return `13.08%`, CAGR `8.05%`, Max DD `-20.14%`, Sharpe `0.5344`, Turnover `4.42`
- `2026-01-01` → `2026-08-04`: Total Return `-2.49%`, CAGR `-4.19%`, Max DD `-18.34%`, Sharpe `0.0859`, Turnover `5.03`

### 2023 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`（核心90_探索10_总市值底座_胜出者核心__进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市6%, 单票5%, 出场68%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`1.43%` / `0.2154` / `-17.49%` / `1.82`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `35.88%`, CAGR `3.25%`, Max DD `-17.32%`, Sharpe `0.3665`, Turnover `2.25`
- `2020-01-01` → `2026-08-04`: Total Return `21.35%`, CAGR `2.98%`, Max DD `-17.32%`, Sharpe `0.3183`, Turnover `2.20`
- `2023-01-01` → `2026-08-04`: Total Return `5.22%`, CAGR `1.43%`, Max DD `-17.49%`, Sharpe `0.2154`, Turnover `1.82`
- `2025-01-01` → `2026-08-04`: Total Return `10.59%`, CAGR `6.54%`, Max DD `-17.05%`, Sharpe `0.4785`, Turnover `3.66`
- `2026-01-01` → `2026-08-04`: Total Return `-1.63%`, CAGR `-2.75%`, Max DD `-15.37%`, Sharpe `0.0492`, Turnover `4.18`

### 2020 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`（核心90_探索10_总市值底座_胜出者核心__进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市6%, 单票5%, 出场68%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`2.98%` / `0.3183` / `-17.32%` / `2.20`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`（核心90_探索10_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市12%, 单票6%, 出场60%, 低换手)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`4.36%` / `0.3999` / `-21.16%` / `2.62`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `35.88%`, CAGR `3.25%`, Max DD `-17.32%`, Sharpe `0.3665`, Turnover `2.25`
- `2020-01-01` → `2026-08-04`: Total Return `21.35%`, CAGR `2.98%`, Max DD `-17.32%`, Sharpe `0.3183`, Turnover `2.20`
- `2023-01-01` → `2026-08-04`: Total Return `5.22%`, CAGR `1.43%`, Max DD `-17.49%`, Sharpe `0.2154`, Turnover `1.82`
- `2025-01-01` → `2026-08-04`: Total Return `10.59%`, CAGR `6.54%`, Max DD `-17.05%`, Sharpe `0.4785`, Turnover `3.66`
- `2026-01-01` → `2026-08-04`: Total Return `-1.63%`, CAGR `-2.75%`, Max DD `-15.37%`, Sharpe `0.0492`, Turnover `4.18`

### 2025 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`（核心90_探索10_总市值底座_胜出者核心__进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市6%, 单票5%, 出场68%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`6.54%` / `0.4785` / `-17.05%` / `3.66`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`（核心90_探索10_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市12%, 单票6%, 出场60%, 低换手)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`8.05%` / `0.5344` / `-20.14%` / `4.42`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-08-04`: Total Return `35.88%`, CAGR `3.25%`, Max DD `-17.32%`, Sharpe `0.3665`, Turnover `2.25`
- `2020-01-01` → `2026-08-04`: Total Return `21.35%`, CAGR `2.98%`, Max DD `-17.32%`, Sharpe `0.3183`, Turnover `2.20`
- `2023-01-01` → `2026-08-04`: Total Return `5.22%`, CAGR `1.43%`, Max DD `-17.49%`, Sharpe `0.2154`, Turnover `1.82`
- `2025-01-01` → `2026-08-04`: Total Return `10.59%`, CAGR `6.54%`, Max DD `-17.05%`, Sharpe `0.4785`, Turnover `3.66`
- `2026-01-01` → `2026-08-04`: Total Return `-1.63%`, CAGR `-2.75%`, Max DD `-15.37%`, Sharpe `0.0492`, Turnover `4.18`

## Path 4：鲁棒候选（观察）

### 四窗口鲁棒候选

- 策略：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`（核心90_探索10_总市值底座_胜出者核心__进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市6%, 单票5%, 出场68%, 低换手)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`3.55%` / `1.43%` / `0.3447` / `-17.49%` / `2.48`

窗口指标：

- `2017-01-01` → `2026-08-04`: Total Return `35.88%`, CAGR `3.25%`, Max DD `-17.32%`, Sharpe `0.3665`, Turnover `2.25`
- `2020-01-01` → `2026-08-04`: Total Return `21.35%`, CAGR `2.98%`, Max DD `-17.32%`, Sharpe `0.3183`, Turnover `2.20`
- `2023-01-01` → `2026-08-04`: Total Return `5.22%`, CAGR `1.43%`, Max DD `-17.49%`, Sharpe `0.2154`, Turnover `1.82`
- `2025-01-01` → `2026-08-04`: Total Return `10.59%`, CAGR `6.54%`, Max DD `-17.05%`, Sharpe `0.4785`, Turnover `3.66`
- `2026-01-01` → `2026-08-04`: Total Return `-1.63%`, CAGR `-2.75%`, Max DD `-15.37%`, Sharpe `0.0492`, Turnover `4.18`

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
