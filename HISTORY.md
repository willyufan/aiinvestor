# 跟踪赢家历史

这个文档记录三条研究路径在四个窗口下的赢家变化历史。
仅当赢家策略或关键指标发生变化时，才会追加新记录。

## Path 1：渐进优化路径

### 2017 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp_cash_off__port_weekly_exposure` | 核心80_探索20_总市值底座_胜出者核心__进攻10/90 快速加仓(熊市空仓)__月度选股_周度仓位调整 | `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered` | 818.35% | 26.55% | -23.65% | 1.1129 | 3.57 |

### 2020 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off` | 核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(熊市空仓) | `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered` | 276.40% | 22.95% | -15.47% | 0.9746 | 2.28 |

### 2023 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_balanced` | 核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升7只(多因子均衡) |  | 170.34% | 33.79% | -30.00% | 1.0731 | 3.59 |

### 2025 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1` | 核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量) | `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered` | 163.15% | 97.98% | -8.73% | 2.3403 | 5.39 |

### 鲁棒候选

| 日期 | 策略ID | 策略名称 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` | 核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只__月度选股_周度仓位调整(双周确认) | 359.97% | 26.85% | -27.46% | 0.9120 | 3.71 |

## Path 2：无约束上限探索

### 2017 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95` | 核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 单票95%) |  | 2071.01% | 38.66% | -32.76% | 1.1345 | 3.79 |

### 2020 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95` | 核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认70, 单票95%) |  | 1838.06% | 58.72% | -28.34% | 1.2451 | 4.49 |

### 2023 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_ma_cap95` | 核心90_探索10_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 量价晋升前15%, 均线三档保留50%, 单票95%) |  | 462.80% | 65.81% | -36.51% | 1.3321 | 4.79 |

### 2025 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60` | 核心80_探索20_总市值底座_胜出者核心__进攻5/95 晋升3只(核心6-1动量, 关闭熊市降仓, 单票60%) | `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` | 253.35% | 143.76% | -17.33% | 2.1172 | 5.94 |

### 鲁棒候选

| 日期 | 策略ID | 策略名称 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95` | 核心90_探索10_等权底座_胜出者核心__进攻2/98 晋升2只(量价晋升前15%, 动量三档保留40%, 晋升保留前60%, 恢复确认75, 单票95%) | 1336.09% | 51.47% | -32.05% | 1.2121 | 4.40 |

## Path 3：周度高频路径

### 2017 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly` | 核心80_探索20_等权底座_胜出者核心__进攻1/99 晋升2只(核心6-1动量, 熊市空仓 and, 单票95%, 单周) |  | 596.07% | 23.45% | -40.04% | 0.8004 | 7.70 |

### 2020 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly` | 核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 单周) | `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly` | 133.64% | 14.49% | -51.71% | 0.5587 | 12.99 |

### 2023 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly` | 核心80_探索20_总市值底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票40%, 单周) |  | 169.06% | 34.88% | -37.14% | 0.9546 | 13.65 |

### 2025 窗口

| 日期 | 策略ID | 策略名称 | Raw过滤 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly` | 核心80_探索20_等权底座_胜出者核心__进攻8/92 晋升6只(核心6-1动量, 满风险, 单票60%, 单周) | `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` | 72.60% | 49.15% | -28.73% | 1.2155 | 14.62 |

### 鲁棒候选

| 日期 | 策略ID | 策略名称 | 整体收益率 | CAGR | MaxDD | Sharpe | Turnover |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15 | `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly` | 核心80_探索20_等权底座_胜出者核心__进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票80%, 持有3周, 换手25%, 单周) | 228.26% | 20.88% | -25.89% | 0.7862 | 4.77 |
