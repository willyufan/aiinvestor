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

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险18成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`21.27%` / `0.9326` / `-13.51%` / `3.08`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-07-08`: Total Return `534.86%`, CAGR `21.27%`, Max DD `-13.51%`, Sharpe `0.9326`, Turnover `3.08`
- `2020-01-01` → `2026-07-09`: Total Return `456.02%`, CAGR `29.77%`, Max DD `-12.04%`, Sharpe `1.0746`, Turnover `3.36`
- `2023-01-01` → `2026-07-09`: Total Return `129.62%`, CAGR `26.11%`, Max DD `-17.92%`, Sharpe `0.9119`, Turnover `3.36`
- `2025-01-01` → `2026-07-09`: Total Return `187.74%`, CAGR `94.94%`, Max DD `-10.91%`, Sharpe `1.7361`, Turnover `4.78`
- `2026-01-01` → `2026-07-09`: Total Return `48.83%`, CAGR `97.72%`, Max DD `-10.40%`, Sharpe `1.8139`, Turnover `6.73`

### 2023 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`31.21%` / `1.0157` / `-17.93%` / `3.37`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`31.30%` / `1.1200` / `-15.10%` / `3.60`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `677.17%`, CAGR `23.86%`, Max DD `-12.25%`, Sharpe `1.0291`, Turnover `3.09`
- `2020-01-01` → `2026-07-09`: Total Return `512.01%`, CAGR `31.68%`, Max DD `-12.03%`, Sharpe `1.1216`, Turnover `3.36`
- `2023-01-01` → `2026-07-09`: Total Return `164.68%`, CAGR `31.21%`, Max DD `-17.93%`, Sharpe `1.0157`, Turnover `3.37`
- `2025-01-01` → `2026-07-09`: Total Return `187.70%`, CAGR `94.92%`, Max DD `-10.91%`, Sharpe `1.7358`, Turnover `4.78`
- `2026-01-01` → `2026-07-09`: Total Return `48.83%`, CAGR `97.72%`, Max DD `-10.40%`, Sharpe `1.8139`, Turnover `6.73`

### 2020 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`31.68%` / `1.1216` / `-12.03%` / `3.36`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `677.17%`, CAGR `23.86%`, Max DD `-12.25%`, Sharpe `1.0291`, Turnover `3.09`
- `2020-01-01` → `2026-07-09`: Total Return `512.01%`, CAGR `31.68%`, Max DD `-12.03%`, Sharpe `1.1216`, Turnover `3.36`
- `2023-01-01` → `2026-07-09`: Total Return `164.68%`, CAGR `31.21%`, Max DD `-17.93%`, Sharpe `1.0157`, Turnover `3.37`
- `2025-01-01` → `2026-07-09`: Total Return `187.70%`, CAGR `94.92%`, Max DD `-10.91%`, Sharpe `1.7358`, Turnover `4.78`
- `2026-01-01` → `2026-07-09`: Total Return `48.83%`, CAGR `97.72%`, Max DD `-10.40%`, Sharpe `1.8139`, Turnover `6.73`

### 2025 窗口赢家

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险10成本再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`97.96%` / `1.7693` / `-10.91%` / `4.68`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `686.11%`, CAGR `24.01%`, Max DD `-13.49%`, Sharpe `0.9990`, Turnover `3.09`
- `2020-01-01` → `2026-07-09`: Total Return `378.16%`, CAGR `26.83%`, Max DD `-13.26%`, Sharpe `0.9874`, Turnover `3.26`
- `2023-01-01` → `2026-07-09`: Total Return `144.39%`, CAGR `28.32%`, Max DD `-19.30%`, Sharpe `0.9497`, Turnover `3.48`
- `2025-01-01` → `2026-07-09`: Total Return `194.85%`, CAGR `97.96%`, Max DD `-10.91%`, Sharpe `1.7693`, Turnover `4.68`
- `2026-01-01` → `2026-07-09`: Total Return `48.85%`, CAGR `97.76%`, Max DD `-10.40%`, Sharpe `1.8143`, Turnover `6.72`

## Path 1：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险16成本再确认)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`40.81%` / `21.26%` / `1.1109` / `-17.45%` / `3.64`

窗口指标：

- `2017-01-01` → `2026-07-08`: Total Return `534.44%`, CAGR `21.26%`, Max DD `-13.51%`, Sharpe `0.9324`, Turnover `3.07`
- `2020-01-01` → `2026-07-09`: Total Return `455.20%`, CAGR `29.74%`, Max DD `-12.04%`, Sharpe `1.0739`, Turnover `3.35`
- `2023-01-01` → `2026-07-09`: Total Return `130.69%`, CAGR `26.27%`, Max DD `-17.45%`, Sharpe `0.9170`, Turnover `3.37`
- `2025-01-01` → `2026-07-09`: Total Return `187.76%`, CAGR `94.95%`, Max DD `-10.91%`, Sharpe `1.7362`, Turnover `4.78`
- `2026-01-01` → `2026-07-09`: Total Return `48.83%`, CAGR `97.72%`, Max DD `-10.40%`, Sharpe `1.8140`, Turnover `6.73`

## Path 1：组合方案

- 组合ID：`path1_composite_robust_window_blend_v1`
- 组合逻辑：不再要求单一 winner 覆盖所有行情，按鲁棒候选与窗口赢家合并权重。
- 组合鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`45.78%` / `23.23%` / `1.2105` / `-17.68%` / `3.65`

当前组合成分：

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险16成本再确认)）：`45.0%`；来源：robust-candidate
- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险20成本再确认)）：`30.0%`；来源：2020-01, 2023-01
- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险18成本再确认)）：`20.0%`；来源：2017-01
- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm`（核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(卫星三档风险10成本再确认)）：`5.0%`；来源：2025-01

组合窗口指标：

- `2017-01-01` → `2026-07-09`: Total Return `627.63%`, CAGR `23.23%`, Max DD `-12.78%`, Sharpe `1.0094`, Turnover `3.08`
- `2020-01-01` → `2026-07-09`: Total Return `468.55%`, CAGR `30.55%`, Max DD `-12.03%`, Sharpe `1.0926`, Turnover `3.35`
- `2023-01-01` → `2026-07-09`: Total Return `141.36%`, CAGR `28.46%`, Max DD `-17.68%`, Sharpe `0.9643`, Turnover `3.37`
- `2025-01-01` → `2026-07-09`: Total Return `188.09%`, CAGR `100.89%`, Max DD `-10.91%`, Sharpe `1.7755`, Turnover `4.78`
- `2026-01-01` → `2026-07-09`: Total Return `48.83%`, CAGR `115.65%`, Max DD `-10.40%`, Sharpe `1.9260`, Turnover `6.73`

## Path 2：窗口跟踪赢家

### 2017 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair`（核心90_探索10_总市值底座_胜出者核心__进攻4/96 晋升4只(中周期成长核心, 量价前12%, 动量三档24%, 出场46%, 恢复98, 谨慎56%, 单票18%, 成本防守v79中周期修复)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`7.00%` / `0.5050` / `-21.18%` / `4.45`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-07-08`: Total Return `91.32%`, CAGR `7.00%`, Max DD `-21.18%`, Sharpe `0.5050`, Turnover `4.45`
- `2020-01-01` → `2026-07-09`: Total Return `47.60%`, CAGR `6.09%`, Max DD `-20.54%`, Sharpe `0.4524`, Turnover `3.75`
- `2023-01-01` → `2026-07-09`: Total Return `62.51%`, CAGR `14.51%`, Max DD `-14.73%`, Sharpe `0.6949`, Turnover `5.62`
- `2025-01-01` → `2026-07-09`: Total Return `79.84%`, CAGR `44.87%`, Max DD `-15.41%`, Sharpe `1.2625`, Turnover `10.21`
- `2026-01-01` → `2026-07-09`: Total Return `13.44%`, CAGR `24.13%`, Max DD `-10.86%`, Sharpe `0.8413`, Turnover `9.52`

### 2023 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(多因子质量成长信号再确认)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`31.42%` / `1.1930` / `-12.45%` / `3.67`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45`（核心90_探索10_总市值底座_胜出者核心__进攻3/97 晋升2只(强主题涌现, 质量门槛, 熊市30%, 单票45%)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`49.73%` / `1.3091` / `-14.24%` / `3.73`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `49.58%`, CAGR `4.29%`, Max DD `-33.73%`, Sharpe `0.3225`, Turnover `3.38`
- `2020-01-01` → `2026-07-09`: Total Return `-5.62%`, CAGR `-0.88%`, Max DD `-34.45%`, Sharpe `0.0564`, Turnover `2.97`
- `2023-01-01` → `2026-07-09`: Total Return `166.20%`, CAGR `31.42%`, Max DD `-12.45%`, Sharpe `1.1930`, Turnover `3.67`
- `2025-01-01` → `2026-07-09`: Total Return `85.52%`, CAGR `47.74%`, Max DD `-9.12%`, Sharpe `1.7024`, Turnover `6.02`
- `2026-01-01` → `2026-07-09`: Total Return `25.76%`, CAGR `48.13%`, Max DD `-12.64%`, Sharpe `1.3049`, Turnover `8.81`

### 2020 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`2.52%` / `0.2259` / `-32.56%` / `2.79`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`（核心90_探索10_总市值底座_胜出者核心__进攻4/96 晋升4只(量价前12%, 动量三档26%, 出场46%, 恢复96, 谨慎58%, 单票22%, 成本防守v30中周期)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`12.67%` / `0.7852` / `-14.98%` / `3.84`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `129.86%`, CAGR `9.07%`, Max DD `-32.48%`, Sharpe `0.5632`, Turnover `3.17`
- `2020-01-01` → `2026-07-09`: Total Return `17.77%`, CAGR `2.52%`, Max DD `-32.56%`, Sharpe `0.2259`, Turnover `2.79`
- `2023-01-01` → `2026-07-09`: Total Return `156.08%`, CAGR `30.01%`, Max DD `-13.22%`, Sharpe `1.1005`, Turnover `3.42`
- `2025-01-01` → `2026-07-09`: Total Return `120.44%`, CAGR `64.75%`, Max DD `-9.13%`, Sharpe `1.5786`, Turnover `4.87`
- `2026-01-01` → `2026-07-09`: Total Return `23.05%`, CAGR `42.70%`, Max DD `-11.34%`, Sharpe `1.2503`, Turnover `5.34`

### 2025 窗口赢家（Path 2）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`（核心80_探索20_总市值底座_胜出者核心__进攻10/90 晋升6只）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`64.75%` / `1.5786` / `-9.13%` / `4.87`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `129.86%`, CAGR `9.07%`, Max DD `-32.48%`, Sharpe `0.5632`, Turnover `3.17`
- `2020-01-01` → `2026-07-09`: Total Return `17.77%`, CAGR `2.52%`, Max DD `-32.56%`, Sharpe `0.2259`, Turnover `2.79`
- `2023-01-01` → `2026-07-09`: Total Return `156.08%`, CAGR `30.01%`, Max DD `-13.22%`, Sharpe `1.1005`, Turnover `3.42`
- `2025-01-01` → `2026-07-09`: Total Return `120.44%`, CAGR `64.75%`, Max DD `-9.13%`, Sharpe `1.5786`, Turnover `4.87`
- `2026-01-01` → `2026-07-09`: Total Return `23.05%`, CAGR `42.70%`, Max DD `-11.34%`, Sharpe `1.2503`, Turnover `5.34`

## Path 2：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair`（核心90_探索10_总市值底座_胜出者核心__进攻4/96 晋升4只(中周期成长核心, 量价前12%, 动量三档24%, 出场46%, 恢复98, 谨慎56%, 单票18%, 成本防守v79中周期修复)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`15.99%` / `5.95%` / `0.6601` / `-21.18%` / `6.00`

窗口指标：

- `2017-01-01` → `2026-07-08`: Total Return `91.32%`, CAGR `7.00%`, Max DD `-21.18%`, Sharpe `0.5050`, Turnover `4.45`
- `2020-01-01` → `2026-07-09`: Total Return `47.60%`, CAGR `6.09%`, Max DD `-20.54%`, Sharpe `0.4524`, Turnover `3.75`
- `2023-01-01` → `2026-07-09`: Total Return `62.51%`, CAGR `14.51%`, Max DD `-14.73%`, Sharpe `0.6949`, Turnover `5.62`
- `2025-01-01` → `2026-07-09`: Total Return `79.84%`, CAGR `44.87%`, Max DD `-15.41%`, Sharpe `1.2625`, Turnover `10.21`
- `2026-01-01` → `2026-07-09`: Total Return `13.44%`, CAGR `24.13%`, Max DD `-10.86%`, Sharpe `0.8413`, Turnover `9.52`

## Path 3：窗口跟踪赢家

### 2017 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`12.93%` / `0.7625` / `-25.00%` / `2.16`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市16%, 单票50%, 持有6周, 换手4%, 出场98%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`13.41%` / `0.8327` / `-21.11%` / `1.48`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `211.46%`, CAGR `12.93%`, Max DD `-25.00%`, Sharpe `0.7625`, Turnover `2.16`
- `2020-01-01` → `2026-07-09`: Total Return `187.51%`, CAGR `17.87%`, Max DD `-26.27%`, Sharpe `0.8654`, Turnover `1.83`
- `2023-01-01` → `2026-07-09`: Total Return `90.79%`, CAGR `20.52%`, Max DD `-22.97%`, Sharpe `0.8968`, Turnover `1.74`
- `2025-01-01` → `2026-07-09`: Total Return `127.01%`, CAGR `71.54%`, Max DD `-18.12%`, Sharpe `1.8143`, Turnover `3.19`
- `2026-01-01` → `2026-07-09`: Total Return `30.74%`, CAGR `70.93%`, Max DD `-11.46%`, Sharpe `1.5830`, Turnover `4.23`

### 2023 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`20.52%` / `0.8968` / `-22.97%` / `1.74`
- 单窗口最高收益（被鲁棒检验过滤）：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(成本压力熊市16%, 单票50%, 持有6周, 换手4%, 出场98%, 单周)）
  - 该窗口指标（CAGR / Sharpe / Max DD / Turnover）：`16.83%` / `1.0166` / `-10.65%` / `0.70`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `211.46%`, CAGR `12.93%`, Max DD `-25.00%`, Sharpe `0.7625`, Turnover `2.16`
- `2020-01-01` → `2026-07-09`: Total Return `187.51%`, CAGR `17.87%`, Max DD `-26.27%`, Sharpe `0.8654`, Turnover `1.83`
- `2023-01-01` → `2026-07-09`: Total Return `90.79%`, CAGR `20.52%`, Max DD `-22.97%`, Sharpe `0.8968`, Turnover `1.74`
- `2025-01-01` → `2026-07-09`: Total Return `127.01%`, CAGR `71.54%`, Max DD `-18.12%`, Sharpe `1.8143`, Turnover `3.19`
- `2026-01-01` → `2026-07-09`: Total Return `30.74%`, CAGR `70.93%`, Max DD `-11.46%`, Sharpe `1.5830`, Turnover `4.23`

### 2020 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有2周, 换手12%, 出场92%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`19.84%` / `0.8403` / `-24.94%` / `3.67`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `236.89%`, CAGR `13.88%`, Max DD `-26.17%`, Sharpe `0.7103`, Turnover `3.94`
- `2020-01-01` → `2026-07-09`: Total Return `219.72%`, CAGR `19.84%`, Max DD `-24.94%`, Sharpe `0.8403`, Turnover `3.67`
- `2023-01-01` → `2026-07-09`: Total Return `87.68%`, CAGR `19.95%`, Max DD `-22.33%`, Sharpe `0.7817`, Turnover `3.46`
- `2025-01-01` → `2026-07-09`: Total Return `129.47%`, CAGR `72.76%`, Max DD `-17.13%`, Sharpe `1.6156`, Turnover `6.46`
- `2026-01-01` → `2026-07-09`: Total Return `27.67%`, CAGR `62.99%`, Max DD `-10.32%`, Sharpe `1.4841`, Turnover `7.87`

### 2025 窗口赢家（Path 3）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（核心80_探索20_总市值底座_胜出者核心__进攻1/99 晋升1只(核心6-1动量, 熊市空仓 and, 单票100%, 单周)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`320.96%` / `2.1549` / `-39.09%` / `15.25`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `658.10%`, CAGR `24.20%`, Max DD `-55.97%`, Sharpe `0.6782`, Turnover `8.62`
- `2020-01-01` → `2026-07-09`: Total Return `126.69%`, CAGR `13.59%`, Max DD `-51.34%`, Sharpe `0.4791`, Turnover `9.34`
- `2023-01-01` → `2026-07-09`: Total Return `99.50%`, CAGR `22.08%`, Max DD `-52.35%`, Sharpe `0.6043`, Turnover `10.64`
- `2025-01-01` → `2026-07-09`: Total Return `787.91%`, CAGR `320.96%`, Max DD `-39.09%`, Sharpe `2.1549`, Turnover `15.25`
- `2026-01-01` → `2026-07-09`: Total Return `118.97%`, CAGR `379.47%`, Max DD `-22.13%`, Sharpe `2.5461`, Turnover `20.48`

## Path 3：鲁棒候选

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`（核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(熊市空仓and, 单票60%, 持有3周, 换手5%, 出场94%, 单周)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`31.98%` / `12.93%` / `1.1131` / `-26.27%` / `2.24`

窗口指标：

- `2017-01-01` → `2026-07-03`: Total Return `211.46%`, CAGR `12.93%`, Max DD `-25.00%`, Sharpe `0.7625`, Turnover `2.16`
- `2020-01-01` → `2026-07-09`: Total Return `187.51%`, CAGR `17.87%`, Max DD `-26.27%`, Sharpe `0.8654`, Turnover `1.83`
- `2023-01-01` → `2026-07-09`: Total Return `90.79%`, CAGR `20.52%`, Max DD `-22.97%`, Sharpe `0.8968`, Turnover `1.74`
- `2025-01-01` → `2026-07-09`: Total Return `127.01%`, CAGR `71.54%`, Max DD `-18.12%`, Sharpe `1.8143`, Turnover `3.19`
- `2026-01-01` → `2026-07-09`: Total Return `30.74%`, CAGR `70.93%`, Max DD `-11.46%`, Sharpe `1.5830`, Turnover `4.23`

## Path 4：窗口跟踪赢家（观察）

### 2017 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升23只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市4%, 单票5%, 出场70%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`9.78%` / `0.6463` / `-13.77%` / `3.19`

窗口指标（权重：2017-01=100%）：

- `2017-01-01` → `2026-07-08`: Total Return `144.47%`, CAGR `9.78%`, Max DD `-13.77%`, Sharpe `0.6463`, Turnover `3.19`
- `2020-01-01` → `2026-07-09`: Total Return `99.73%`, CAGR `11.08%`, Max DD `-13.58%`, Sharpe `0.6665`, Turnover `3.27`
- `2023-01-01` → `2026-07-09`: Total Return `49.24%`, CAGR `11.82%`, Max DD `-10.66%`, Sharpe `0.7965`, Turnover `3.03`
- `2025-01-01` → `2026-07-09`: Total Return `83.87%`, CAGR `46.91%`, Max DD `-6.65%`, Sharpe `1.5383`, Turnover `5.58`
- `2026-01-01` → `2026-07-09`: Total Return `28.14%`, CAGR `52.96%`, Max DD `-10.14%`, Sharpe `1.4138`, Turnover `5.66`

### 2023 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`10.31%` / `0.9788` / `-5.73%` / `3.24`

窗口指标（权重：2023-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `199.78%`, CAGR `12.14%`, Max DD `-14.74%`, Sharpe `0.7190`, Turnover `3.60`
- `2020-01-01` → `2026-07-09`: Total Return `130.50%`, CAGR `13.52%`, Max DD `-14.74%`, Sharpe `0.7203`, Turnover `3.65`
- `2023-01-01` → `2026-07-09`: Total Return `42.12%`, CAGR `10.31%`, Max DD `-5.73%`, Sharpe `0.9788`, Turnover `3.24`
- `2025-01-01` → `2026-07-09`: Total Return `98.47%`, CAGR `54.18%`, Max DD `-7.49%`, Sharpe `1.5702`, Turnover `6.23`
- `2026-01-01` → `2026-07-09`: Total Return `31.62%`, CAGR `60.16%`, Max DD `-10.82%`, Sharpe `1.4651`, Turnover `6.40`

### 2020 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`13.52%` / `0.7203` / `-14.74%` / `3.65`

窗口指标（权重：2020-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `199.78%`, CAGR `12.14%`, Max DD `-14.74%`, Sharpe `0.7190`, Turnover `3.60`
- `2020-01-01` → `2026-07-09`: Total Return `130.50%`, CAGR `13.52%`, Max DD `-14.74%`, Sharpe `0.7203`, Turnover `3.65`
- `2023-01-01` → `2026-07-09`: Total Return `42.12%`, CAGR `10.31%`, Max DD `-5.73%`, Sharpe `0.9788`, Turnover `3.24`
- `2025-01-01` → `2026-07-09`: Total Return `98.47%`, CAGR `54.18%`, Max DD `-7.49%`, Sharpe `1.5702`, Turnover `6.23`
- `2026-01-01` → `2026-07-09`: Total Return `31.62%`, CAGR `60.16%`, Max DD `-10.82%`, Sharpe `1.4651`, Turnover `6.40`

### 2025 窗口赢家（Path 4）

- 鲁棒赢家：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升20只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市12%, 单票6%, 出场60%, 低换手)）
- 加权指标（CAGR / Sharpe / Max DD / Turnover）：`54.18%` / `1.5702` / `-7.49%` / `6.23`

窗口指标（权重：2025-01=100%）：

- `2017-01-01` → `2026-07-03`: Total Return `199.78%`, CAGR `12.14%`, Max DD `-14.74%`, Sharpe `0.7190`, Turnover `3.60`
- `2020-01-01` → `2026-07-09`: Total Return `130.50%`, CAGR `13.52%`, Max DD `-14.74%`, Sharpe `0.7203`, Turnover `3.65`
- `2023-01-01` → `2026-07-09`: Total Return `42.12%`, CAGR `10.31%`, Max DD `-5.73%`, Sharpe `0.9788`, Turnover `3.24`
- `2025-01-01` → `2026-07-09`: Total Return `98.47%`, CAGR `54.18%`, Max DD `-7.49%`, Sharpe `1.5702`, Turnover `6.23`
- `2026-01-01` → `2026-07-09`: Total Return `31.62%`, CAGR `60.16%`, Max DD `-10.82%`, Sharpe `1.4651`, Turnover `6.40`

## Path 4：鲁棒候选（观察）

### 四窗口鲁棒候选

- 策略：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`（核心80_探索20_总市值底座_胜出者核心__进攻13/87 晋升23只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市4%, 单票5%, 出场70%, 低换手)）
- 鲁棒指标（平均 CAGR / 最低 CAGR / 平均 Sharpe / 最差 Max DD / 平均 Turnover）：`17.25%` / `9.48%` / `0.7846` / `-13.77%` / `3.77`

窗口指标：

- `2017-01-01` → `2026-07-08`: Total Return `144.47%`, CAGR `9.78%`, Max DD `-13.77%`, Sharpe `0.6463`, Turnover `3.19`
- `2020-01-01` → `2026-07-09`: Total Return `99.73%`, CAGR `11.08%`, Max DD `-13.58%`, Sharpe `0.6665`, Turnover `3.27`
- `2023-01-01` → `2026-07-09`: Total Return `49.24%`, CAGR `11.82%`, Max DD `-10.66%`, Sharpe `0.7965`, Turnover `3.03`
- `2025-01-01` → `2026-07-09`: Total Return `83.87%`, CAGR `46.91%`, Max DD `-6.65%`, Sharpe `1.5383`, Turnover `5.58`
- `2026-01-01` → `2026-07-09`: Total Return `28.14%`, CAGR `52.96%`, Max DD `-10.14%`, Sharpe `1.4138`, Turnover `5.66`

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
