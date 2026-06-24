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

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险10成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`25.04%` / `1.0516` / `-12.13%` / `2.96`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险25成本再确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`26.01%` / `1.0815` / `-12.67%` / `3.02`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `735.37%`, CAGR `25.04%`, Max DD `-12.13%`, Sharpe `1.0516`, Turnover `2.96`
- `2020-01-01` → `2026-06-23`: Total Return `431.52%`, CAGR `29.31%`, Max DD `-13.26%`, Sharpe `1.0656`, Turnover `3.32`
- `2023-01-01` → `2026-06-23`: Total Return `154.16%`, CAGR `30.54%`, Max DD `-18.26%`, Sharpe `1.0255`, Turnover `3.49`
- `2025-01-01` → `2026-06-23`: Total Return `209.21%`, CAGR `112.24%`, Max DD `-10.91%`, Sharpe `2.0202`, Turnover `4.63`
- `2026-01-01` → `2026-06-23`: Total Return `60.17%`, CAGR `156.54%`, Max DD `-6.61%`, Sharpe `2.9441`, Turnover `7.35`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`34.19%` / `1.1097` / `-17.94%` / `3.39`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`39.74%` / `1.0816` / `-31.03%` / `4.08`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `738.28%`, CAGR `25.08%`, Max DD `-14.02%`, Sharpe `1.0538`, Turnover `3.01`
- `2020-01-01` → `2026-06-23`: Total Return `533.78%`, CAGR `32.85%`, Max DD `-12.03%`, Sharpe `1.1652`, Turnover `3.36`
- `2023-01-01` → `2026-06-23`: Total Return `179.94%`, CAGR `34.19%`, Max DD `-17.94%`, Sharpe `1.1097`, Turnover `3.39`
- `2025-01-01` → `2026-06-23`: Total Return `200.33%`, CAGR `108.16%`, Max DD `-10.91%`, Sharpe `1.9869`, Turnover `4.75`
- `2026-01-01` → `2026-06-23`: Total Return `60.15%`, CAGR `156.48%`, Max DD `-6.61%`, Sharpe `2.9434`, Turnover `7.35`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`32.85%` / `1.1652` / `-12.03%` / `3.36`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `738.28%`, CAGR `25.08%`, Max DD `-14.02%`, Sharpe `1.0538`, Turnover `3.01`
- `2020-01-01` → `2026-06-23`: Total Return `533.78%`, CAGR `32.85%`, Max DD `-12.03%`, Sharpe `1.1652`, Turnover `3.36`
- `2023-01-01` → `2026-06-23`: Total Return `179.94%`, CAGR `34.19%`, Max DD `-17.94%`, Sharpe `1.1097`, Turnover `3.39`
- `2025-01-01` → `2026-06-23`: Total Return `200.33%`, CAGR `108.16%`, Max DD `-10.91%`, Sharpe `1.9869`, Turnover `4.75`
- `2026-01-01` → `2026-06-23`: Total Return `60.15%`, CAGR `156.48%`, Max DD `-6.61%`, Sharpe `2.9434`, Turnover `7.35`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`76.33%` / `1.8159` / `-6.66%` / `4.82`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_satellite_cost_guard`（核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(卫星成本防守)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`116.91%` / `2.1728` / `-10.33%` / `4.32`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `141.11%`, CAGR `9.71%`, Max DD `-32.12%`, Sharpe `0.5991`, Turnover `3.18`
- `2020-01-01` → `2026-06-23`: Total Return `16.64%`, CAGR `2.40%`, Max DD `-33.05%`, Sharpe `0.2194`, Turnover `2.78`
- `2023-01-01` → `2026-06-23`: Total Return `134.78%`, CAGR `27.61%`, Max DD `-13.22%`, Sharpe `1.0622`, Turnover `3.45`
- `2025-01-01` → `2026-06-23`: Total Return `134.14%`, CAGR `76.33%`, Max DD `-6.66%`, Sharpe `1.8159`, Turnover `4.82`
- `2026-01-01` → `2026-06-23`: Total Return `29.73%`, CAGR `68.31%`, Max DD `-11.33%`, Sharpe `1.9441`, Turnover `5.30`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险25成本再确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`49.89%` / `26.01%` / `1.3231` / `-20.12%` / `3.65`

窗口指标：

- `2017-01-01` → `2026-06-23`: Total Return `799.05%`, CAGR `26.01%`, Max DD `-12.67%`, Sharpe `1.0815`, Turnover `3.02`
- `2020-01-01` → `2026-06-23`: Total Return `506.10%`, CAGR `31.94%`, Max DD `-13.04%`, Sharpe `1.1363`, Turnover `3.37`
- `2023-01-01` → `2026-06-23`: Total Return `174.66%`, CAGR `33.47%`, Max DD `-20.12%`, Sharpe `1.0879`, Turnover `3.46`
- `2025-01-01` → `2026-06-23`: Total Return `200.30%`, CAGR `108.15%`, Max DD `-10.91%`, Sharpe `1.9865`, Turnover `4.75`
- `2026-01-01` → `2026-06-23`: Total Return `60.14%`, CAGR `156.46%`, Max DD `-6.61%`, Sharpe `2.9432`, Turnover `7.36`

## Path 1：组合方案

- 组合ID：`path1_composite_robust_window_blend_v1`
- 组合逻辑：不再要求单一 winner 覆盖所有行情，按鲁棒候选与窗口赢家合并权重。
- 组合鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`49.87%` / `25.11%` / `1.3362` / `-18.09%` / `3.63`

当前组合成分：

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险25成本再确认)）：`45.0%`；来源：robust-candidate
- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）：`30.0%`；来源：2020-01, 2023-01
- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险10成本再确认)）：`20.0%`；来源：2017-01
- `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）：`5.0%`；来源：2025-01

组合窗口指标：

- `2017-01-01` → `2026-06-23`: Total Return `735.19%`, CAGR `25.11%`, Max DD `-12.02%`, Sharpe `1.0767`, Turnover `3.01`
- `2020-01-01` → `2026-06-23`: Total Return `475.02%`, CAGR `31.02%`, Max DD `-12.27%`, Sharpe `1.1265`, Turnover `3.33`
- `2023-01-01` → `2026-06-23`: Total Return `170.15%`, CAGR `33.11%`, Max DD `-18.09%`, Sharpe `1.1057`, Turnover `3.44`
- `2025-01-01` → `2026-06-23`: Total Return `198.78%`, CAGR `110.24%`, Max DD `-10.24%`, Sharpe `2.0357`, Turnover `4.73`
- `2026-01-01` → `2026-06-23`: Total Return `58.63%`, CAGR `164.89%`, Max DD `-6.85%`, Sharpe `2.9967`, Turnover `7.25`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`（核心90_探索10_总市值底座_胜出者核心__进攻4/96 晋升4只(量价前12%, 动量三档26%, 出场46%, 恢复96, 谨慎58%, 单票22%, 成本防守v30中周期)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.27%` / `0.8411` / `-15.80%` / `4.44`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `226.56%`, CAGR `13.27%`, Max DD `-15.80%`, Sharpe `0.8411`, Turnover `4.44`
- `2020-01-01` → `2026-06-23`: Total Return `124.44%`, CAGR `13.24%`, Max DD `-14.98%`, Sharpe `0.8040`, Turnover `3.86`
- `2023-01-01` → `2026-06-23`: Total Return `34.33%`, CAGR `8.80%`, Max DD `-13.35%`, Sharpe `0.6616`, Turnover `3.55`
- `2025-01-01` → `2026-06-23`: Total Return `89.73%`, CAGR `53.26%`, Max DD `-15.03%`, Sharpe `1.4965`, Turnover `9.68`
- `2026-01-01` → `2026-06-23`: Total Return `19.64%`, CAGR `43.13%`, Max DD `-13.10%`, Sharpe `1.3036`, Turnover `9.19`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70`（核心90_探索10_总市值底座_胜出者核心__进攻5/95 晋升3只(强主题涌现, 熊市40%, 单票70%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`45.06%` / `1.2058` / `-13.92%` / `3.40`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `167.01%`, CAGR `10.89%`, Max DD `-41.89%`, Sharpe `0.5950`, Turnover `3.61`
- `2020-01-01` → `2026-06-23`: Total Return `-30.89%`, CAGR `-5.53%`, Max DD `-57.63%`, Sharpe `-0.1382`, Turnover `3.48`
- `2023-01-01` → `2026-06-23`: Total Return `267.65%`, CAGR `45.06%`, Max DD `-13.92%`, Sharpe `1.2058`, Turnover `3.40`
- `2025-01-01` → `2026-06-23`: Total Return `72.90%`, CAGR `44.05%`, Max DD `-8.24%`, Sharpe `1.9221`, Turnover `4.92`
- `2026-01-01` → `2026-06-23`: Total Return `20.68%`, CAGR `45.64%`, Max DD `-8.56%`, Sharpe `1.4916`, Turnover `7.68`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`（核心90_探索10_总市值底座_胜出者核心__进攻4/96 晋升4只(量价前12%, 动量三档26%, 出场46%, 恢复96, 谨慎58%, 单票22%, 成本防守v30中周期)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.24%` / `0.8040` / `-14.98%` / `3.86`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `226.56%`, CAGR `13.27%`, Max DD `-15.80%`, Sharpe `0.8411`, Turnover `4.44`
- `2020-01-01` → `2026-06-23`: Total Return `124.44%`, CAGR `13.24%`, Max DD `-14.98%`, Sharpe `0.8040`, Turnover `3.86`
- `2023-01-01` → `2026-06-23`: Total Return `34.33%`, CAGR `8.80%`, Max DD `-13.35%`, Sharpe `0.6616`, Turnover `3.55`
- `2025-01-01` → `2026-06-23`: Total Return `89.73%`, CAGR `53.26%`, Max DD `-15.03%`, Sharpe `1.4965`, Turnover `9.68`
- `2026-01-01` → `2026-06-23`: Total Return `19.64%`, CAGR `43.13%`, Max DD `-13.10%`, Sharpe `1.3036`, Turnover `9.19`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升3只(核心6-1动量, 关闭熊市降仓, 单票60%)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`74.71%` / `1.9696` / `-8.16%` / `4.19`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`76.33%` / `1.8159` / `-6.66%` / `4.82`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `66.19%`, CAGR `5.49%`, Max DD `-56.49%`, Sharpe `0.3306`, Turnover `4.21`
- `2020-01-01` → `2026-06-23`: Total Return `-33.50%`, CAGR `-6.08%`, Max DD `-60.80%`, Sharpe `-0.0648`, Turnover `4.09`
- `2023-01-01` → `2026-06-23`: Total Return `216.50%`, CAGR `38.98%`, Max DD `-22.29%`, Sharpe `1.1432`, Turnover `3.32`
- `2025-01-01` → `2026-06-23`: Total Return `130.92%`, CAGR `74.71%`, Max DD `-8.16%`, Sharpe `1.9696`, Turnover `4.19`
- `2026-01-01` → `2026-06-23`: Total Return `3.06%`, CAGR `6.21%`, Max DD `-6.60%`, Sharpe `0.4587`, Turnover `7.07`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66`（核心90_探索10_总市值底座_胜出者核心__进攻13/87 晋升12只(强主题涌现, 信号26%, 龙头72%, 熊市15%, 单票12%, 出场66%)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`23.26%` / `11.91%` / `1.0544` / `-27.73%` / `5.39`

窗口指标：

- `2017-01-01` → `2026-06-23`: Total Return `191.26%`, CAGR `11.91%`, Max DD `-27.73%`, Sharpe `0.7202`, Turnover `4.75`
- `2020-01-01` → `2026-06-23`: Total Return `114.60%`, CAGR `12.47%`, Max DD `-13.26%`, Sharpe `0.7050`, Turnover `4.53`
- `2023-01-01` → `2026-06-23`: Total Return `80.89%`, CAGR `18.45%`, Max DD `-7.70%`, Sharpe `1.1115`, Turnover `3.98`
- `2025-01-01` → `2026-06-23`: Total Return `84.07%`, CAGR `50.20%`, Max DD `-12.78%`, Sharpe `1.6807`, Turnover `8.30`
- `2026-01-01` → `2026-06-23`: Total Return `46.96%`, CAGR `115.97%`, Max DD `-8.78%`, Sharpe `2.4921`, Turnover `8.48`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`14.56%` / `0.8469` / `-25.00%` / `2.18`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `255.17%`, CAGR `14.56%`, Max DD `-25.00%`, Sharpe `0.8469`, Turnover `2.18`
- `2020-01-01` → `2026-06-23`: Total Return `210.57%`, CAGR `19.42%`, Max DD `-26.29%`, Sharpe `0.9245`, Turnover `1.89`
- `2023-01-01` → `2026-06-23`: Total Return `106.03%`, CAGR `23.51%`, Max DD `-23.81%`, Sharpe `1.0191`, Turnover `1.75`
- `2025-01-01` → `2026-06-23`: Total Return `77.14%`, CAGR `47.13%`, Max DD `-13.55%`, Sharpe `1.5815`, Turnover `2.05`
- `2026-01-01` → `2026-06-23`: Total Return `37.03%`, CAGR `97.88%`, Max DD `-11.46%`, Sharpe `2.0188`, Turnover `4.42`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`23.51%` / `1.0191` / `-23.81%` / `1.75`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市16%, 单票50%, 持有6周, 换手4%, 出场98%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`19.15%` / `1.1597` / `-10.68%` / `0.71`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `255.17%`, CAGR `14.56%`, Max DD `-25.00%`, Sharpe `0.8469`, Turnover `2.18`
- `2020-01-01` → `2026-06-23`: Total Return `210.57%`, CAGR `19.42%`, Max DD `-26.29%`, Sharpe `0.9245`, Turnover `1.89`
- `2023-01-01` → `2026-06-23`: Total Return `106.03%`, CAGR `23.51%`, Max DD `-23.81%`, Sharpe `1.0191`, Turnover `1.75`
- `2025-01-01` → `2026-06-23`: Total Return `77.14%`, CAGR `47.13%`, Max DD `-13.55%`, Sharpe `1.5815`, Turnover `2.05`
- `2026-01-01` → `2026-06-23`: Total Return `37.03%`, CAGR `97.88%`, Max DD `-11.46%`, Sharpe `2.0188`, Turnover `4.42`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit98_risk16_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市16%, 单票50%, 持有5周, 换手5%, 出场98%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`23.52%` / `1.0076` / `-25.33%` / `1.49`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `194.22%`, CAGR `12.27%`, Max DD `-28.03%`, Sharpe `0.6893`, Turnover `2.06`
- `2020-01-01` → `2026-06-23`: Total Return `285.26%`, CAGR `23.52%`, Max DD `-25.33%`, Sharpe `1.0076`, Turnover `1.49`
- `2023-01-01` → `2026-06-23`: Total Return `83.26%`, CAGR `19.36%`, Max DD `-14.58%`, Sharpe `0.9926`, Turnover `1.31`
- `2025-01-01` → `2026-06-23`: Total Return `137.17%`, CAGR `79.18%`, Max DD `-14.92%`, Sharpe `1.7973`, Turnover `2.89`
- `2026-01-01` → `2026-06-23`: Total Return `38.49%`, CAGR `102.48%`, Max DD `-12.88%`, Sharpe `2.1210`, Turnover `1.98`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`322.95%` / `2.1844` / `-38.85%` / `14.88`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `349.84%`, CAGR `17.49%`, Max DD `-63.08%`, Sharpe `0.5558`, Turnover `8.04`
- `2020-01-01` → `2026-06-23`: Total Return `163.76%`, CAGR `16.40%`, Max DD `-51.01%`, Sharpe `0.5264`, Turnover `9.24`
- `2023-01-01` → `2026-06-23`: Total Return `89.51%`, CAGR `20.53%`, Max DD `-52.31%`, Sharpe `0.5810`, Turnover `10.46`
- `2025-01-01` → `2026-06-23`: Total Return `746.04%`, CAGR `322.95%`, Max DD `-38.85%`, Sharpe `2.1844`, Turnover `14.88`
- `2026-01-01` → `2026-06-23`: Total Return `143.42%`, CAGR `587.26%`, Max DD `-20.73%`, Sharpe `3.2703`, Turnover `19.97`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有2周, 换手12%, 出场92%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`34.52%` / `14.38%` / `1.0524` / `-28.10%` / `4.26`

窗口指标：

- `2017-01-01` → `2026-06-23`: Total Return `250.11%`, CAGR `14.38%`, Max DD `-26.28%`, Sharpe `0.7281`, Turnover `3.91`
- `2020-01-01` → `2026-06-23`: Total Return `217.81%`, CAGR `19.85%`, Max DD `-28.10%`, Sharpe `0.8386`, Turnover `3.52`
- `2023-01-01` → `2026-06-23`: Total Return `101.63%`, CAGR `22.74%`, Max DD `-23.16%`, Sharpe `0.8823`, Turnover `3.40`
- `2025-01-01` → `2026-06-23`: Total Return `140.96%`, CAGR `81.11%`, Max DD `-17.81%`, Sharpe `1.7606`, Turnover `6.23`
- `2026-01-01` → `2026-06-23`: Total Return `34.33%`, CAGR `89.56%`, Max DD `-10.32%`, Sharpe `1.9586`, Turnover `8.17`

## Path 4：窗口跟踪赢家（观察）

### 2017 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.46%` / `0.8189` / `-14.99%` / `3.54`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `231.93%`, CAGR `13.46%`, Max DD `-14.99%`, Sharpe `0.8189`, Turnover `3.54`
- `2020-01-01` → `2026-06-23`: Total Return `151.50%`, CAGR `15.24%`, Max DD `-14.74%`, Sharpe `0.8274`, Turnover `3.59`
- `2023-01-01` → `2026-06-23`: Total Return `50.42%`, CAGR `12.37%`, Max DD `-5.73%`, Sharpe `1.1941`, Turnover `3.16`
- `2025-01-01` → `2026-06-23`: Total Return `113.67%`, CAGR `65.89%`, Max DD `-7.24%`, Sharpe `1.8695`, Turnover `6.15`
- `2026-01-01` → `2026-06-23`: Total Return `39.75%`, CAGR `95.30%`, Max DD `-10.82%`, Sharpe `2.1468`, Turnover `6.21`

### 2023 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升18只(强主题涌现, 覆盖惩罚, 信号28%, 龙头76%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`12.69%` / `1.2052` / `-5.32%` / `3.19`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `242.58%`, CAGR `13.84%`, Max DD `-17.80%`, Sharpe `0.8790`, Turnover `3.58`
- `2020-01-01` → `2026-06-23`: Total Return `119.74%`, CAGR `12.88%`, Max DD `-14.88%`, Sharpe `0.7164`, Turnover `3.59`
- `2023-01-01` → `2026-06-23`: Total Return `51.90%`, CAGR `12.69%`, Max DD `-5.32%`, Sharpe `1.2052`, Turnover `3.19`
- `2025-01-01` → `2026-06-23`: Total Return `109.51%`, CAGR `63.73%`, Max DD `-7.61%`, Sharpe `1.8512`, Turnover `6.23`
- `2026-01-01` → `2026-06-23`: Total Return `38.04%`, CAGR `90.56%`, Max DD `-11.05%`, Sharpe `2.1005`, Turnover `6.30`

### 2020 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`15.24%` / `0.8274` / `-14.74%` / `3.59`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `231.93%`, CAGR `13.46%`, Max DD `-14.99%`, Sharpe `0.8189`, Turnover `3.54`
- `2020-01-01` → `2026-06-23`: Total Return `151.50%`, CAGR `15.24%`, Max DD `-14.74%`, Sharpe `0.8274`, Turnover `3.59`
- `2023-01-01` → `2026-06-23`: Total Return `50.42%`, CAGR `12.37%`, Max DD `-5.73%`, Sharpe `1.1941`, Turnover `3.16`
- `2025-01-01` → `2026-06-23`: Total Return `113.67%`, CAGR `65.89%`, Max DD `-7.24%`, Sharpe `1.8695`, Turnover `6.15`
- `2026-01-01` → `2026-06-23`: Total Return `39.75%`, CAGR `95.30%`, Max DD `-10.82%`, Sharpe `2.1468`, Turnover `6.21`

### 2025 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市10%, 单票6%, 出场62%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`65.89%` / `1.8695` / `-7.24%` / `6.15`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-06-23`: Total Return `231.83%`, CAGR `13.46%`, Max DD `-14.97%`, Sharpe `0.8187`, Turnover `3.54`
- `2020-01-01` → `2026-06-23`: Total Return `151.40%`, CAGR `15.24%`, Max DD `-14.74%`, Sharpe `0.8270`, Turnover `3.59`
- `2023-01-01` → `2026-06-23`: Total Return `50.38%`, CAGR `12.36%`, Max DD `-5.74%`, Sharpe `1.1932`, Turnover `3.16`
- `2025-01-01` → `2026-06-23`: Total Return `113.67%`, CAGR `65.89%`, Max DD `-7.24%`, Sharpe `1.8695`, Turnover `6.15`
- `2026-01-01` → `2026-06-23`: Total Return `39.75%`, CAGR `95.30%`, Max DD `-10.82%`, Sharpe `2.1468`, Turnover `6.21`

## Path 4：鲁棒候选（观察）

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`26.74%` / `12.37%` / `1.1774` / `-14.99%` / `4.11`

窗口指标：

- `2017-01-01` → `2026-06-23`: Total Return `231.93%`, CAGR `13.46%`, Max DD `-14.99%`, Sharpe `0.8189`, Turnover `3.54`
- `2020-01-01` → `2026-06-23`: Total Return `151.50%`, CAGR `15.24%`, Max DD `-14.74%`, Sharpe `0.8274`, Turnover `3.59`
- `2023-01-01` → `2026-06-23`: Total Return `50.42%`, CAGR `12.37%`, Max DD `-5.73%`, Sharpe `1.1941`, Turnover `3.16`
- `2025-01-01` → `2026-06-23`: Total Return `113.67%`, CAGR `65.89%`, Max DD `-7.24%`, Sharpe `1.8695`, Turnover `6.15`
- `2026-01-01` → `2026-06-23`: Total Return `39.75%`, CAGR `95.30%`, Max DD `-10.82%`, Sharpe `2.1468`, Turnover `6.21`

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
