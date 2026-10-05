# 2026-10-06 十二路径策略竞争记录

市场端点：A股 2026-09-30；沪港通 2026-10-05。全部策略卡同市场五窗同端点、同指标、含累计成本。2个新参数与18个形态确认分别统计；18个中4个已有近期scorecard，20个coverage补缺与事件复核另计。未达到常规24–36新实验目标，原因是Path2全集blocking补缺以及跨路径确认预算；不得把补缺或历史复核当新增。

{'archive': 2, 'keep_watch': 2, 'promote': 1, 'reject': 15}

## 覆盖与限制

Path2 coverage仍block：622；正式身份冻结。02922.HK旧代码未覆盖目标日，按现有1%容忍规则跳过。kb-web复用9/16快照，哈希与PIT门禁通过；0新增调用/credits，历史信号不足，不能声称overlay收益改善。

## A股 Path1（主线与core_multifactor）

- `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_quality`：parameter_confirmation，`reject`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对正式robust确认aggr_08_92_prom6_core_multifactor_industry_momentum_quality形态；按signal_quality检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_signal_mode": {"candidate": "multi_factor", "reference": null}, "factor_weights": {"candidate": {"growth_acceleration": 0.05, "industry_leader": 0.08, "industry_strength": 0.22, "liquidity_surge": 0.03, "momentum_3_1": 0.1, "momentum_6_1": 0.3, "quality": 0.22}, "reference": null}, "market_risk_off_rule": {"candidate": null, "reference": "and"}, "promoted_core_max_holdings": {"candidate": 6, "reference": 8}, "promoted_core_sell_exit_percentile": {"candidate": null, "reference": 0.52}, "risk_evaluation_frequency": {"candidate": null, "reference": "weekly"}, "risk_overlay_scope": {"candidate": null, "reference": "satellite_only"}, "risk_stage_buffered": {"candidate": null, "reference": true}, "risk_stage_confirm_weeks": {"candidate": null, "reference": 2}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_caution_exposure": {"candidate": null, "reference": 0.44}, "satellite_risk_off_exposure": {"candidate": null, "reference": 0.2}, "stable_core_max_holdings": {"candidate": 2, "reference": 1}, "variant_name": {"candidate": "进攻8/92 晋升6只(多因子行业动量质量)", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}, "winner_core_promoted_share": {"candidate": 0.92, "reference": 0.95}, "winner_core_stable_share": {"candidate": 0.08, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -14.86/-6.86pp，MaxDD差 +6.98/+3.64pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

- `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality`：parameter_confirmation，`reject`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对正式robust确认aggr_08_92_prom6_core_multifactor_industry_quality形态；按signal_quality检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_signal_mode": {"candidate": "multi_factor", "reference": null}, "factor_weights": {"candidate": {"growth_acceleration": 0.1, "industry_leader": 0.1, "industry_strength": 0.2, "liquidity_surge": 0.05, "momentum_3_1": 0.05, "momentum_6_1": 0.25, "quality": 0.25}, "reference": null}, "market_risk_off_rule": {"candidate": null, "reference": "and"}, "promoted_core_max_holdings": {"candidate": 6, "reference": 8}, "promoted_core_sell_exit_percentile": {"candidate": null, "reference": 0.52}, "risk_evaluation_frequency": {"candidate": null, "reference": "weekly"}, "risk_overlay_scope": {"candidate": null, "reference": "satellite_only"}, "risk_stage_buffered": {"candidate": null, "reference": true}, "risk_stage_confirm_weeks": {"candidate": null, "reference": 2}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_caution_exposure": {"candidate": null, "reference": 0.44}, "satellite_risk_off_exposure": {"candidate": null, "reference": 0.2}, "stable_core_max_holdings": {"candidate": 2, "reference": 1}, "variant_name": {"candidate": "进攻8/92 晋升6只(多因子行业+质量)", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}, "winner_core_promoted_share": {"candidate": 0.92, "reference": 0.95}, "winner_core_stable_share": {"candidate": 0.08, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -20.02/-8.78pp，MaxDD差 +9.19/+6.86pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution38_20261005`：parameter_confirmation，`keep_watch`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对正式robust确认aggr_05_95_prom8_satellite_caution38_20261005形态；按signal_quality检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"satellite_caution_exposure": {"candidate": 0.38, "reference": 0.44}, "variant_name": {"candidate": "相对robust只将卫星谨慎仓位44→38%；预期降低中窗MaxDD，核实CAGR代价。", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +0.34/+0.98pp，MaxDD差 +0.19/+0.18pp；稳定性阈值通过，但净改善、成本或近窗仍需确认。

- 实际支持：False；正式身份变化：False；保留观察条件；不扩大A股active池

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution36_20261006`：new_parameter，`promote`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对上轮watch只将卫星谨慎仓位38%降到36%；与正式robust44%相比，预期中窗MaxDD下降且CAGR损失不超过3pp，五窗验证成本和近窗代价。

- 2020/2023 CAGR差 +0.69/+1.06pp，MaxDD差 +0.19/+0.19pp；五窗CAGR/Sharpe一致改善，中窗稳定性通过，换手增量不足1倍且总换手低于15倍；具备相邻验证晋级资格。 现有ADJACENT_VALIDATION_THRESHOLDS逐目标窗口通过；本轮不扩大已超软上限的Path1 active集合，仅取得晋级资格，未替换正式身份。

- 实际支持：True；正式身份变化：False；保留观察条件；不扩大A股active池

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution38_20261005,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn --comparison-csv /private/tmp/aiiter1006/ashare.csv

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution36_20261006,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907 --comparison-csv /private/tmp/aiiter1006/ashare_new.csv

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907

```

## A股 Path2

- `core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100`：parameter_confirmation，`reject`。参照 `core_explore_70_30_equal_weight_winner_core`。

- 假设：相对正式robust确认aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100形态；按underrepresented_families检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": null}, "core_signal_mode": {"candidate": "midcycle_momentum", "reference": null}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.1, "reference": null}, "fast_promotion_percentile": {"candidate": 0.12, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": null}, "promoted_core_max_holdings": {"candidate": 1, "reference": null}, "promoted_core_stage_ramp": {"candidate": {"1": 1.0}, "reference": null}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": null}, "stable_core_max_holdings": {"candidate": 1, "reference": null}, "variant_name": {"candidate": "进攻1/99 晋升1只(中周期量价动量, 熊市空仓 and, 单票100%)", "reference": null}, "weight_cap": {"candidate": 1.0, "reference": null}, "winner_core_promoted_share": {"candidate": 0.99, "reference": null}, "winner_core_stable_share": {"candidate": 0.01, "reference": null}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -20.41/-5.35pp，MaxDD差 -36.63/+7.67pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。 全集coverage仍block，禁止promote。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

- `core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95`：parameter_confirmation，`reject`。参照 `core_explore_70_30_equal_weight_winner_core`。

- 假设：相对正式robust确认aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95形态；按underrepresented_families检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": null}, "core_signal_mode": {"candidate": "midcycle_momentum", "reference": null}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.1, "reference": null}, "fast_promotion_percentile": {"candidate": 0.12, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": null}, "promoted_core_max_holdings": {"candidate": 2, "reference": null}, "promoted_core_stage_ramp": {"candidate": {"1": 1.0}, "reference": null}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": null}, "stable_core_max_holdings": {"candidate": 1, "reference": null}, "variant_name": {"candidate": "进攻1/99 晋升2只(中周期量价动量, 熊市空仓 and, 单票95%)", "reference": null}, "weight_cap": {"candidate": 0.95, "reference": null}, "winner_core_promoted_share": {"candidate": 0.99, "reference": null}, "winner_core_stable_share": {"candidate": 0.01, "reference": null}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -16.44/-8.78pp，MaxDD差 -24.93/+0.18pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。 全集coverage仍block，禁止promote。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution38_20261005,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn --comparison-csv /private/tmp/aiiter1006/ashare.csv

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_70_30_equal_weight_winner_core

```

## A股 Path3

- `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly`：parameter_confirmation，`reject`。参照 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`。

- 假设：相对正式robust确认aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly形态；按turnover_reduction检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "core_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "fast_promotion_percentile": {"candidate": 0.1, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": "negative_mom"}, "promoted_core_max_holdings": {"candidate": 2, "reference": 6}, "promoted_core_sell_exit_percentile": {"candidate": 0.8, "reference": 0.98}, "promotion_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "stable_core_max_holdings": {"candidate": 1, "reference": 2}, "standard_promotion_percentile": {"candidate": 0.15, "reference": null}, "variant_name": {"candidate": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有6周, 换手12%, 单周)", "reference": "进攻8/92 晋升6只(成本压力熊市16%, 单票52%, 持有6周, 换手4%, 出场98%, 单周)"}, "weekly_turnover_cap": {"candidate": 0.12, "reference": 0.04}, "weight_cap": {"candidate": 0.6, "reference": 0.52}, "winner_core_promoted_share": {"candidate": 0.97, "reference": 0.92}, "winner_core_stable_share": {"candidate": 0.03, "reference": 0.08}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -16.20/+0.37pp，MaxDD差 -24.33/-8.14pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

- `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly`：parameter_confirmation，`reject`。参照 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`。

- 假设：相对正式robust确认aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly形态；按turnover_reduction检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "core_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "fast_promotion_percentile": {"candidate": 0.1, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": "negative_mom"}, "promoted_core_max_holdings": {"candidate": 2, "reference": 6}, "promoted_core_sell_exit_percentile": {"candidate": 0.9, "reference": 0.98}, "promotion_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "stable_core_max_holdings": {"candidate": 1, "reference": 2}, "standard_promotion_percentile": {"candidate": 0.15, "reference": null}, "variant_name": {"candidate": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票60%, 持有8周, 换手10%, 宽出场90%, 单周)", "reference": "进攻8/92 晋升6只(成本压力熊市16%, 单票52%, 持有6周, 换手4%, 出场98%, 单周)"}, "weekly_min_hold_periods": {"candidate": 8, "reference": 6}, "weekly_turnover_cap": {"candidate": 0.1, "reference": 0.04}, "weight_cap": {"candidate": 0.6, "reference": 0.52}, "winner_core_promoted_share": {"candidate": 0.97, "reference": 0.92}, "winner_core_stable_share": {"candidate": 0.03, "reference": 0.08}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -16.58/+2.74pp，MaxDD差 -27.50/-7.17pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution38_20261005,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn --comparison-csv /private/tmp/aiiter1006/ashare.csv

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly

```

## A股 Path4（emergent theme discovery）

- `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`：parameter_confirmation，`reject`。参照 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。

- 假设：相对正式robust确认aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn形态；按emergent_theme_coverage检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"base_id": {"candidate": "core_explore_80_20_total_mv_winner_core", "reference": "core_explore_90_10_equal_weight_winner_core"}, "core_risk_off_exposure": {"candidate": 0.12, "reference": 0.08}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.38, "reference": 1.36}, "promoted_core_sell_exit_percentile": {"candidate": 0.6, "reference": 0.66}, "satellite_risk_off_exposure": {"candidate": 0.12, "reference": 0.08}, "standard_promotion_percentile": {"candidate": 0.29, "reference": 0.3}, "variant_name": {"candidate": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市12%, 单票6%, 出场60%, 低换手)", "reference": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号30%, 龙头78%, 熊市8%, 单票5%, 出场66%, 低换手)"}, "weight_cap": {"candidate": 0.06, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +3.05/-5.07pp，MaxDD差 -20.99/-23.68pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

- `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`：parameter_confirmation，`reject`。参照 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。

- 假设：相对正式robust确认aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn形态；按emergent_theme_coverage检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"base_id": {"candidate": "core_explore_80_20_total_mv_winner_core", "reference": "core_explore_90_10_equal_weight_winner_core"}, "core_quality_quantile": {"candidate": 0.74, "reference": 0.72}, "core_risk_off_exposure": {"candidate": 0.1, "reference": 0.08}, "explore_quality_quantile": {"candidate": 0.68, "reference": 0.66}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.4, "reference": 1.36}, "fast_promotion_min_industry_leader": {"candidate": 0.94, "reference": 0.92}, "fast_promotion_min_momentum_3_1_rank": {"candidate": 0.78, "reference": 0.76}, "fast_promotion_percentile": {"candidate": 0.04, "reference": 0.045}, "promoted_core_quality_quantile": {"candidate": 0.58, "reference": 0.56}, "promoted_core_sell_exit_percentile": {"candidate": 0.58, "reference": 0.66}, "satellite_risk_off_exposure": {"candidate": 0.1, "reference": 0.08}, "seed_quality_quantile": {"candidate": 0.52, "reference": 0.5}, "standard_promotion_min_industry_leader": {"candidate": 0.8, "reference": 0.78}, "standard_promotion_min_momentum_3_1_rank": {"candidate": 0.68, "reference": 0.66}, "variant_name": {"candidate": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市10%, 单票6%, 出场58%, 低换手)", "reference": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号30%, 龙头78%, 熊市8%, 单票5%, 出场66%, 低换手)"}, "weight_cap": {"candidate": 0.06, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +3.08/-5.91pp，MaxDD差 -20.41/-23.94pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution38_20261005,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn --comparison-csv /private/tmp/aiiter1006/ashare.csv

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn

```

## A股 Path5（event knowledge graph）

- `ai_datacenter_power_grid_202607_v0`，source_audited，20/40/60D；keep_watch。40D转负，60D样本不足；单事件缺完整CAGR/Sharpe/MaxDD/换手口径，不能晋级。

- 20D +11.70%、40D -0.60%、60D不足；与Path4持仓重合0/6；gross/net成本不齐，不做晋级。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --basket-id ai_datacenter_power_grid_202607_v0 --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --path4-sample-tag since_2026_01 --output-json results/research/a_share/research_iteration_event_next.json

```

## 沪港通 Path1

- `hkconnect_path1_monthly_cashoff_weekly_overlay`：parameter_confirmation，`archive`。参照 `hkconnect_path1_biweekly_hybrid`。

- 假设：相对正式robust确认hkconnect_path1_monthly_cashoff_weekly_overlay形态；按monthly_weekly_overlay检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.18, "reference": 0.16}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.7, "reference": 0.8}, "risk_evaluation_frequency": {"candidate": "weekly", "reference": null}, "risk_off_exposure": {"candidate": 0.0, "reference": 0.5}, "risk_overlay_scope": {"candidate": "portfolio_only", "reference": null}, "sell_exit_percentile": {"candidate": 0.32, "reference": 0.3}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -0.18/-0.44pp，MaxDD差 +6.55/-1.43pp；连续3轮观察无实质改善，停止刷新并保留历史快照。

- 实际支持：True；正式身份变化：False；archive_only；退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_cashoff_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_biweekly,hkconnect_path2_theme_entry09_20261005,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay,hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard,hkconnect_path1_biweekly_hybrid

```

## 沪港通 Path2

- `hkconnect_path2_breakout_cashoff_biweekly`：parameter_confirmation，`reject`。参照 `hkconnect_path2_theme_entry09_20261005`。

- 假设：相对正式robust确认hkconnect_path2_breakout_cashoff_biweekly形态；按high_return_monthly检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.1, "reference": 0.09}, "rebalance_frequency": {"candidate": "biweekly", "reference": "monthly"}, "risk_caution_exposure": {"candidate": 0.7, "reference": 0.9}, "risk_off_exposure": {"candidate": 0.0, "reference": 0.65}, "risk_off_rule": {"candidate": "and", "reference": "or"}, "sell_exit_percentile": {"candidate": 0.22, "reference": 0.18}, "signal_family": {"candidate": "path2_breakout", "reference": "path2_theme"}, "weight_cap": {"candidate": 0.28, "reference": 0.25}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -16.90/-20.57pp，MaxDD差 -36.21/-19.13pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

- `hkconnect_path2_theme_entry10_20261006`：new_parameter，`keep_watch`。参照 `hkconnect_path2_theme_entry09_20261005`。

- 假设：相对正式robust entry09只将买入分位9%扩大至10%；预期提升中窗CAGR，检查回撤、成本、2026和多窗稳定性，任一护栏失守即reject。

- 2020/2023 CAGR差 +0.89/+2.44pp，MaxDD差 +1.07/-0.18pp；稳定性阈值通过，但净改善、成本或近窗仍需确认。

- 实际支持：True；正式身份变化：False；保留观察条件；不扩大A股active池

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_cashoff_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_biweekly,hkconnect_path2_theme_entry09_20261005,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_entry10_20261006,hkconnect_path2_theme_entry09_20261005

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_entry10_20261006,hkconnect_path2_breakout_cashoff_monthly,hkconnect_path2_theme_entry09_20261005

```

## 沪港通 Path3

- `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42`：parameter_confirmation，`reject`。参照 `hkconnect_path3_theme_risk52_20261003`。

- 假设：相对正式robust确认hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42形态；按weekly_turnover_reduction检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"base_weight_mode": {"candidate": "hybrid", "reference": "signal"}, "buy_entry_percentile": {"candidate": 0.18, "reference": 0.07}, "max_holdings": {"candidate": 18, "reference": 5}, "risk_caution_exposure": {"candidate": 0.76, "reference": 0.9}, "risk_off_exposure": {"candidate": 0.45, "reference": 0.52}, "risk_off_rule": {"candidate": "and", "reference": "or"}, "sell_exit_percentile": {"candidate": 0.42, "reference": 0.16}, "signal_family": {"candidate": "path1_moderate", "reference": "path2_theme"}, "weight_cap": {"candidate": 0.09, "reference": 0.32}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -7.66/-13.18pp，MaxDD差 +17.94/-4.34pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_cashoff_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_biweekly,hkconnect_path2_theme_entry09_20261005,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38,hkconnect_path3_theme_risk52_20261003

```

## 沪港通 Path4（quality / liquidity momentum）

- `hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5`：parameter_confirmation，`archive`。参照 `hkconnect_path4_liquidity_momentum_biweekly_smoke`。

- 假设：相对正式robust确认hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5形态；按quality_momentum检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.18, "reference": 0.14}, "max_holdings": {"candidate": 20, "reference": 12}, "risk_caution_exposure": {"candidate": 0.68, "reference": 0.78}, "risk_off_exposure": {"candidate": 0.28, "reference": 0.4}, "sell_exit_percentile": {"candidate": 0.34, "reference": 0.32}, "weight_cap": {"candidate": 0.08, "reference": 0.12}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -1.68/+1.63pp，MaxDD差 +1.25/+4.63pp；连续3轮观察无实质改善，停止刷新并保留历史快照。

- 实际支持：True；正式身份变化：False；archive_only；退出active保留历史定义

- `hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair`：parameter_confirmation，`reject`。参照 `hkconnect_path4_liquidity_momentum_biweekly_smoke`。

- 假设：相对正式robust确认hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair形态；按quality_momentum检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.2, "reference": 0.14}, "max_holdings": {"candidate": 28, "reference": 12}, "risk_caution_exposure": {"candidate": 0.58, "reference": 0.78}, "risk_off_exposure": {"candidate": 0.24, "reference": 0.4}, "sell_exit_percentile": {"candidate": 0.36, "reference": 0.32}, "weight_cap": {"candidate": 0.05, "reference": 0.12}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -2.25/+1.96pp，MaxDD差 -5.41/+1.50pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_cashoff_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_biweekly,hkconnect_path2_theme_entry09_20261005,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v14_ytd_repair,hkconnect_path4_liquidity_momentum_biweekly_smoke

```

## 沪港通 Path5（breakout retest / pullback continuation）

- `hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn`：parameter_confirmation，`reject`。参照 `hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`。

- 假设：相对正式robust确认hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn形态；按pullback_definition检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.4, "reference": 0.6}, "max_holdings": {"candidate": 40, "reference": 32}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.4, "reference": 0.2}, "risk_off_exposure": {"candidate": 0.04, "reference": 0.0}, "sell_exit_percentile": {"candidate": 0.56, "reference": 0.76}, "weight_cap": {"candidate": 0.03, "reference": 0.012}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +3.19/+2.50pp，MaxDD差 -9.10/-8.54pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_cashoff_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_biweekly,hkconnect_path2_theme_entry09_20261005,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v8_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907

```

## 沪港通 Path6（large liquid core）

- `hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair`：parameter_confirmation，`reject`。参照 `hkconnect_path6_lowvol_liquid_biweekly_smoke`。

- 假设：相对正式robust确认hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair形态；按large_liquid_core检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.48, "reference": 0.2}, "max_holdings": {"candidate": 52, "reference": 20}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.3, "reference": 0.82}, "risk_off_exposure": {"candidate": 0.0, "reference": 0.5}, "sell_exit_percentile": {"candidate": 0.66, "reference": 0.4}, "weight_cap": {"candidate": 0.016, "reference": 0.09}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -6.79/-9.47pp，MaxDD差 +4.34/-1.30pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_cashoff_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_biweekly,hkconnect_path2_theme_entry09_20261005,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_large_liquid_core_monthly_lowvol_liquidity_mix_v6,hkconnect_path6_lowvol_liquid_biweekly_smoke

```

## 沪港通 Path7（barbell quality growth）

- `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance`：parameter_confirmation，`reject`。参照 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`。

- 假设：相对正式robust确认hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance形态；按barbell_sleeve_structure检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.25, "reference": 0.18}, "max_holdings": {"candidate": 40, "reference": 28}, "risk_caution_exposure": {"candidate": 0.48, "reference": 0.62}, "risk_off_exposure": {"candidate": 0.1, "reference": 0.24}, "sell_exit_percentile": {"candidate": 0.5, "reference": 0.36}, "weight_cap": {"candidate": 0.03, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -2.69/-3.62pp，MaxDD差 -0.15/-1.45pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

- `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance`：parameter_confirmation，`reject`。参照 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`。

- 假设：相对正式robust确认hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance形态；按barbell_sleeve_structure检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.26, "reference": 0.18}, "max_holdings": {"candidate": 42, "reference": 28}, "risk_caution_exposure": {"candidate": 0.46, "reference": 0.62}, "risk_off_exposure": {"candidate": 0.08, "reference": 0.24}, "sell_exit_percentile": {"candidate": 0.52, "reference": 0.36}, "weight_cap": {"candidate": 0.028, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -2.53/-3.52pp，MaxDD差 +0.25/-1.78pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；新HK reject退出active保留历史定义

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_cashoff_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_biweekly,hkconnect_path2_theme_entry09_20261005,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v27_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

## 正式角色与退出刷新

A4/HK4/HK5存在近窗负收益的robust仅为robust_observation：进入观察位，不是强稳定 winner。机械artifact换位经二次scorecard冻结。

{
  "PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS = [": [
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly"
  ],
  "PATH2_ARCHIVED_STRATEGY_BASE_IDS = [": [
    "core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100",
    "core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95"
  ],
  "HK_ARCHIVED_STRATEGY_IDS = {": [
    "hkconnect_path1_monthly_cashoff_weekly_overlay",
    "hkconnect_path2_breakout_cashoff_biweekly",
    "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42",
    "hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5",
    "hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair",
    "hkconnect_path5_pullback_continuation_monthly_quality_retest_v19_definition_lowturn",
    "hkconnect_path6_large_liquid_core_monthly_capacity_cost_v40_ytd_cashguard_repair",
    "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v14_sleeve_rebalance",
    "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v15_sleeve_rebalance"
  ]
}

所有完整CAGR、Sharpe、MaxDD、年换手、成本、差值和护栏命中见 results/research/a_share/research_iteration_scorecard_20261006.json。
