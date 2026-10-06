# 2026-10-07 十二路径策略竞争记录

市场端点：A股2026-09-30；沪港通2026-10-06。所有策略卡五窗同市场同端点，含CAGR、Sharpe、MaxDD、换手与成本。12个真实新增参数、15个首次形态确认、1个历史复核分别计数；20个覆盖补缺及事件篮子复核另计。覆盖阻断下新增预算回落至12个。

{'reject': 24, 'promote': 1, 'keep_watch': 3}

## 覆盖与限制

Path2仍block，缺598；正式身份冻结。kb-web复用既有快照、0新调用/credits；无新可证伪数据假设，不能倒填历史。

## A股 Path1（主线与core_multifactor）

- `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality`：parameter_confirmation，`reject`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对正式robust确认aggr_08_92_prom6_core_multifactor_momentum_quality形态；按signal_quality检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_signal_mode": {"candidate": "multi_factor", "reference": null}, "factor_weights": {"candidate": {"growth_acceleration": 0.1, "industry_leader": 0.1, "industry_strength": 0.1, "liquidity_surge": 0.0, "momentum_3_1": 0.1, "momentum_6_1": 0.4, "quality": 0.2}, "reference": null}, "market_risk_off_rule": {"candidate": null, "reference": "and"}, "promoted_core_max_holdings": {"candidate": 6, "reference": 8}, "promoted_core_sell_exit_percentile": {"candidate": null, "reference": 0.52}, "risk_evaluation_frequency": {"candidate": null, "reference": "weekly"}, "risk_overlay_scope": {"candidate": null, "reference": "satellite_only"}, "risk_stage_buffered": {"candidate": null, "reference": true}, "risk_stage_confirm_weeks": {"candidate": null, "reference": 2}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_caution_exposure": {"candidate": null, "reference": 0.44}, "satellite_risk_off_exposure": {"candidate": null, "reference": 0.2}, "stable_core_max_holdings": {"candidate": 2, "reference": 1}, "variant_name": {"candidate": "进攻8/92 晋升6只(多因子动量+质量)", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}, "winner_core_promoted_share": {"candidate": 0.92, "reference": 0.95}, "winner_core_stable_share": {"candidate": 0.08, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"core_signal_mode": {"candidate": "multi_factor", "reference": null}, "factor_weights": {"candidate": {"growth_acceleration": 0.1, "industry_leader": 0.1, "industry_strength": 0.1, "liquidity_surge": 0.0, "momentum_3_1": 0.1, "momentum_6_1": 0.4, "quality": 0.2}, "reference": null}, "market_risk_off_rule": {"candidate": null, "reference": "and"}, "promoted_core_max_holdings": {"candidate": 6, "reference": 8}, "promoted_core_sell_exit_percentile": {"candidate": null, "reference": 0.52}, "risk_evaluation_frequency": {"candidate": null, "reference": "weekly"}, "risk_overlay_scope": {"candidate": null, "reference": "satellite_only"}, "risk_stage_buffered": {"candidate": null, "reference": true}, "risk_stage_confirm_weeks": {"candidate": null, "reference": 2}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_caution_exposure": {"candidate": null, "reference": 0.44}, "satellite_risk_off_exposure": {"candidate": null, "reference": 0.2}, "stable_core_max_holdings": {"candidate": 2, "reference": 1}, "variant_name": {"candidate": "进攻8/92 晋升6只(多因子动量+质量)", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}, "winner_core_promoted_share": {"candidate": 0.92, "reference": 0.95}, "winner_core_stable_share": {"candidate": 0.08, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -15.19/-5.73pp，MaxDD差 +7.01/+9.04pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；隔离定义与历史保留

- `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense`：parameter_confirmation，`reject`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对正式robust确认aggr_08_92_prom6_core_multifactor_quality_defense形态；按signal_quality检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_signal_mode": {"candidate": "multi_factor", "reference": null}, "factor_weights": {"candidate": {"growth_acceleration": 0.05, "industry_leader": 0.1, "industry_strength": 0.2, "liquidity_surge": 0.05, "momentum_3_1": 0.05, "momentum_6_1": 0.2, "quality": 0.35}, "reference": null}, "market_risk_off_rule": {"candidate": null, "reference": "and"}, "promoted_core_max_holdings": {"candidate": 6, "reference": 8}, "promoted_core_sell_exit_percentile": {"candidate": null, "reference": 0.52}, "risk_evaluation_frequency": {"candidate": null, "reference": "weekly"}, "risk_overlay_scope": {"candidate": null, "reference": "satellite_only"}, "risk_stage_buffered": {"candidate": null, "reference": true}, "risk_stage_confirm_weeks": {"candidate": null, "reference": 2}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_caution_exposure": {"candidate": null, "reference": 0.44}, "satellite_risk_off_exposure": {"candidate": null, "reference": 0.2}, "stable_core_max_holdings": {"candidate": 2, "reference": 1}, "variant_name": {"candidate": "进攻8/92 晋升6只(多因子质量防守)", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}, "winner_core_promoted_share": {"candidate": 0.92, "reference": 0.95}, "winner_core_stable_share": {"candidate": 0.08, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"core_signal_mode": {"candidate": "multi_factor", "reference": null}, "factor_weights": {"candidate": {"growth_acceleration": 0.05, "industry_leader": 0.1, "industry_strength": 0.2, "liquidity_surge": 0.05, "momentum_3_1": 0.05, "momentum_6_1": 0.2, "quality": 0.35}, "reference": null}, "market_risk_off_rule": {"candidate": null, "reference": "and"}, "promoted_core_max_holdings": {"candidate": 6, "reference": 8}, "promoted_core_sell_exit_percentile": {"candidate": null, "reference": 0.52}, "risk_evaluation_frequency": {"candidate": null, "reference": "weekly"}, "risk_overlay_scope": {"candidate": null, "reference": "satellite_only"}, "risk_stage_buffered": {"candidate": null, "reference": true}, "risk_stage_confirm_weeks": {"candidate": null, "reference": 2}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_caution_exposure": {"candidate": null, "reference": 0.44}, "satellite_risk_off_exposure": {"candidate": null, "reference": 0.2}, "stable_core_max_holdings": {"candidate": 2, "reference": 1}, "variant_name": {"candidate": "进攻8/92 晋升6只(多因子质量防守)", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}, "winner_core_promoted_share": {"candidate": 0.92, "reference": 0.95}, "winner_core_stable_share": {"candidate": 0.08, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -20.34/-6.61pp，MaxDD差 +10.31/+7.16pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；隔离定义与历史保留

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution36_20261006`：historical_recheck，`promote`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对正式robust确认aggr_05_95_prom8_satellite_caution36_20261006形态；按signal_quality检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"satellite_caution_exposure": {"candidate": 0.36, "reference": 0.44}, "variant_name": {"candidate": "相对上轮watch只将卫星谨慎仓位38%降到36%；与正式robust44%相比，预期中窗MaxDD下降且CAGR损失不超过3pp，五窗验证成本和近窗代价。", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"satellite_caution_exposure": {"candidate": 0.36, "reference": 0.44}, "variant_name": {"candidate": "相对上轮watch只将卫星谨慎仓位38%降到36%；与正式robust44%相比，预期中窗MaxDD下降且CAGR损失不超过3pp，五窗验证成本和近窗代价。", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +0.69/+1.06pp，MaxDD差 +0.19/+0.19pp；五窗CAGR/Sharpe一致改善，中窗稳定性通过，换手增量不足1倍且总换手低于15倍；具备相邻验证晋级资格。 现有ADJACENT_VALIDATION_THRESHOLDS逐目标窗口通过；本轮不扩大已超软上限的Path1 active集合，仅取得晋级资格，未替换正式身份。

- 实际支持：True；正式身份变化：False；保留晋级资格；未扩大active集合

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution34_20261007`：new_parameter，`keep_watch`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对robust只将卫星谨慎仓位44→34%；预期降低中窗MaxDD，核实CAGR代价。 明确参数差异：{"satellite_caution_exposure": {"candidate": 0.34, "reference": 0.44}, "variant_name": {"candidate": "相对robust只将卫星谨慎仓位44→34%；预期降低中窗MaxDD，核实CAGR代价。", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -1.01/+0.96pp，MaxDD差 -0.23/+0.19pp；稳定性阈值通过，但净改善、成本或近窗仍需确认。

- 实际支持：False；正式身份变化：False；保留观察并要求中窗稳定性、近窗与净成本再验证

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_industry27_20261007`：new_parameter，`reject`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：相对quality_tilt将6-1动量20→13%、行业强度10→17%；检验行业质量协同对中窗风险收益影响，与正式robust竞争。 明确参数差异：{"core_signal_mode": {"candidate": "multi_factor", "reference": null}, "factor_weights": {"candidate": {"growth_acceleration": 0.15, "industry_leader": 0.1, "industry_strength": 0.17, "liquidity_surge": 0.05, "momentum_3_1": 0.1, "momentum_6_1": 0.13, "quality": 0.3}, "reference": null}, "market_risk_off_rule": {"candidate": null, "reference": "and"}, "promoted_core_max_holdings": {"candidate": 7, "reference": 8}, "promoted_core_sell_exit_percentile": {"candidate": null, "reference": 0.52}, "risk_evaluation_frequency": {"candidate": null, "reference": "weekly"}, "risk_overlay_scope": {"candidate": null, "reference": "satellite_only"}, "risk_stage_buffered": {"candidate": null, "reference": true}, "risk_stage_confirm_weeks": {"candidate": null, "reference": 2}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_caution_exposure": {"candidate": null, "reference": 0.44}, "satellite_risk_off_exposure": {"candidate": null, "reference": 0.2}, "variant_name": {"candidate": "相对quality_tilt将6-1动量20→13%、行业强度10→17%；检验行业质量协同对中窗风险收益影响，与正式robust竞争。", "reference": "20260907 相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益"}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -22.24/-8.43pp，MaxDD差 +8.02/+6.36pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；隔离定义与历史保留

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution36_20261006,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn --comparison-csv /private/tmp/aiiter1007/ashare.csv

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution34_20261007,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_industry27_20261007,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_surge134_20261007,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn032_exit98_risk16_20261007_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_leader82_risk08_cap05_exit66_20261007,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiiter1007/ashare_new.csv

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_industry_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907

```

## A股 Path2

- `core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100`：parameter_confirmation，`reject`。参照 `core_explore_70_30_equal_weight_winner_core`。

- 假设：相对正式robust确认aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100形态；按underrepresented_families检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": null}, "core_signal_mode": {"candidate": "midcycle_momentum", "reference": null}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.1, "reference": null}, "fast_promotion_percentile": {"candidate": 0.12, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": null}, "promoted_core_max_holdings": {"candidate": 1, "reference": null}, "promoted_core_stage_ramp": {"candidate": {"1": 1.0}, "reference": null}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": null}, "stable_core_max_holdings": {"candidate": 1, "reference": null}, "variant_name": {"candidate": "进攻2/98 晋升1只(中周期量价动量, 熊市空仓 and, 单票100%)", "reference": null}, "weight_cap": {"candidate": 1.0, "reference": null}, "winner_core_promoted_share": {"candidate": 0.98, "reference": null}, "winner_core_stable_share": {"candidate": 0.02, "reference": null}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": null}, "core_signal_mode": {"candidate": "midcycle_momentum", "reference": null}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.1, "reference": null}, "fast_promotion_percentile": {"candidate": 0.12, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": null}, "promoted_core_max_holdings": {"candidate": 1, "reference": null}, "promoted_core_stage_ramp": {"candidate": {"1": 1.0}, "reference": null}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": null}, "stable_core_max_holdings": {"candidate": 1, "reference": null}, "variant_name": {"candidate": "进攻2/98 晋升1只(中周期量价动量, 熊市空仓 and, 单票100%)", "reference": null}, "weight_cap": {"candidate": 1.0, "reference": null}, "winner_core_promoted_share": {"candidate": 0.98, "reference": null}, "winner_core_stable_share": {"candidate": 0.02, "reference": null}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -20.61/-5.97pp，MaxDD差 -37.16/+7.43pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。 全集coverage仍block，禁止promote。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95`：parameter_confirmation，`reject`。参照 `core_explore_70_30_equal_weight_winner_core`。

- 假设：相对正式robust确认aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95形态；按underrepresented_families检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": null}, "core_signal_mode": {"candidate": "midcycle_momentum", "reference": null}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.1, "reference": null}, "fast_promotion_percentile": {"candidate": 0.12, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": null}, "promoted_core_max_holdings": {"candidate": 2, "reference": null}, "promoted_core_stage_ramp": {"candidate": {"1": 1.0}, "reference": null}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": null}, "stable_core_max_holdings": {"candidate": 1, "reference": null}, "variant_name": {"candidate": "进攻2/98 晋升2只(中周期量价动量, 熊市空仓 and, 单票95%)", "reference": null}, "weight_cap": {"candidate": 0.95, "reference": null}, "winner_core_promoted_share": {"candidate": 0.98, "reference": null}, "winner_core_stable_share": {"candidate": 0.02, "reference": null}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": null}, "core_signal_mode": {"candidate": "midcycle_momentum", "reference": null}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.1, "reference": null}, "fast_promotion_percentile": {"candidate": 0.12, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": null}, "promoted_core_max_holdings": {"candidate": 2, "reference": null}, "promoted_core_stage_ramp": {"candidate": {"1": 1.0}, "reference": null}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": null}, "stable_core_max_holdings": {"candidate": 1, "reference": null}, "variant_name": {"candidate": "进攻2/98 晋升2只(中周期量价动量, 熊市空仓 and, 单票95%)", "reference": null}, "weight_cap": {"candidate": 0.95, "reference": null}, "winner_core_promoted_share": {"candidate": 0.98, "reference": null}, "winner_core_stable_share": {"candidate": 0.02, "reference": null}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -16.75/-9.45pp，MaxDD差 -25.93/+0.21pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。 全集coverage仍block，禁止promote。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_surge134_20261007`：new_parameter，`reject`。参照 `core_explore_70_30_equal_weight_winner_core`。

- 假设：相对欠配族v63仅提高快晋升放量要求1.26→1.34；检验减少噪声交易能否改善2020/2023与成本；block下禁止promote。 明确参数差异：{"core_caution_exposure": {"candidate": 0.58, "reference": null}, "core_risk_off_exposure": {"candidate": 0.2, "reference": null}, "core_signal_mode": {"candidate": "6_1", "reference": null}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.34, "reference": null}, "fast_promotion_min_momentum_3_1_rank": {"candidate": 0.78, "reference": null}, "fast_promotion_min_momentum_6_1_rank": {"candidate": 0.985, "reference": null}, "fast_promotion_min_recent_1m_return": {"candidate": 0.01, "reference": null}, "fast_promotion_percentile": {"candidate": 0.09, "reference": null}, "market_risk_off_rule": {"candidate": "negative_mom", "reference": null}, "promoted_core_max_holdings": {"candidate": 3, "reference": null}, "promoted_core_sell_exit_percentile": {"candidate": 0.4, "reference": null}, "promoted_core_stage_ramp": {"candidate": {"1": 1.0}, "reference": null}, "promotion_signal_mode": {"candidate": "liquidity_momentum", "reference": null}, "rebalance_frequency": {"candidate": "biweekly", "reference": null}, "risk_staging_mode": {"candidate": "three_stage", "reference": null}, "satellite_caution_exposure": {"candidate": 0.4, "reference": null}, "satellite_risk_off_exposure": {"candidate": 0.2, "reference": null}, "stable_core_max_holdings": {"candidate": 1, "reference": null}, "standard_promotion_min_momentum_3_1_rank": {"candidate": 0.74, "reference": null}, "standard_promotion_min_momentum_6_1_rank": {"candidate": 0.96, "reference": null}, "standard_promotion_percentile": {"candidate": 0.14, "reference": null}, "variant_name": {"candidate": "相对欠配族v63仅提高快晋升放量要求1.26→1.34；检验减少噪声交易能否改善2020/2023与成本；block下禁止promote。", "reference": null}, "weight_cap": {"candidate": 0.14, "reference": null}, "winner_core_promoted_share": {"candidate": 0.97, "reference": null}, "winner_core_stable_share": {"candidate": 0.03, "reference": null}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -2.30/-9.33pp，MaxDD差 -5.26/+10.26pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。 全集coverage仍block，禁止promote。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution36_20261006,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn --comparison-csv /private/tmp/aiiter1007/ashare.csv

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution34_20261007,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_industry27_20261007,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_surge134_20261007,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn032_exit98_risk16_20261007_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_leader82_risk08_cap05_exit66_20261007,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiiter1007/ashare_new.csv

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_3_1_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_3_1_full_risk_cap100,core_explore_70_30_equal_weight_winner_core

```

## A股 Path3

- `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly`：parameter_confirmation，`reject`。参照 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`。

- 假设：相对正式robust确认aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly形态；按turnover_reduction检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "core_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "fast_promotion_percentile": {"candidate": 0.1, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": "negative_mom"}, "promoted_core_max_holdings": {"candidate": 2, "reference": 6}, "promoted_core_sell_exit_percentile": {"candidate": 0.88, "reference": 0.98}, "promotion_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "stable_core_max_holdings": {"candidate": 1, "reference": 2}, "standard_promotion_percentile": {"candidate": 0.15, "reference": null}, "variant_name": {"candidate": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票62%, 持有6周, 换手10%, 出场88%, 单周)", "reference": "进攻8/92 晋升6只(成本压力熊市16%, 单票52%, 持有6周, 换手4%, 出场98%, 单周)"}, "weekly_turnover_cap": {"candidate": 0.1, "reference": 0.04}, "weight_cap": {"candidate": 0.62, "reference": 0.52}, "winner_core_promoted_share": {"candidate": 0.97, "reference": 0.92}, "winner_core_stable_share": {"candidate": 0.03, "reference": 0.08}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "core_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "fast_promotion_percentile": {"candidate": 0.1, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": "negative_mom"}, "promoted_core_max_holdings": {"candidate": 2, "reference": 6}, "promoted_core_sell_exit_percentile": {"candidate": 0.88, "reference": 0.98}, "promotion_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "stable_core_max_holdings": {"candidate": 1, "reference": 2}, "standard_promotion_percentile": {"candidate": 0.15, "reference": null}, "variant_name": {"candidate": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票62%, 持有6周, 换手10%, 出场88%, 单周)", "reference": "进攻8/92 晋升6只(成本压力熊市16%, 单票52%, 持有6周, 换手4%, 出场98%, 单周)"}, "weekly_turnover_cap": {"candidate": 0.1, "reference": 0.04}, "weight_cap": {"candidate": 0.62, "reference": 0.52}, "winner_core_promoted_share": {"candidate": 0.97, "reference": 0.92}, "winner_core_stable_share": {"candidate": 0.03, "reference": 0.08}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -15.03/-8.90pp，MaxDD差 -25.19/-11.37pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly`：parameter_confirmation，`reject`。参照 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`。

- 假设：相对正式robust确认aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly形态；按turnover_reduction检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "core_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "fast_promotion_percentile": {"candidate": 0.1, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": "negative_mom"}, "promoted_core_max_holdings": {"candidate": 2, "reference": 6}, "promoted_core_sell_exit_percentile": {"candidate": 0.85, "reference": 0.98}, "promotion_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "stable_core_max_holdings": {"candidate": 1, "reference": 2}, "standard_promotion_percentile": {"candidate": 0.15, "reference": null}, "variant_name": {"candidate": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票65%, 持有5周, 换手10%, 出场85%, 单周)", "reference": "进攻8/92 晋升6只(成本压力熊市16%, 单票52%, 持有6周, 换手4%, 出场98%, 单周)"}, "weekly_min_hold_periods": {"candidate": 5, "reference": 6}, "weekly_turnover_cap": {"candidate": 0.1, "reference": 0.04}, "weight_cap": {"candidate": 0.65, "reference": 0.52}, "winner_core_promoted_share": {"candidate": 0.97, "reference": 0.92}, "winner_core_stable_share": {"candidate": 0.03, "reference": 0.08}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"core_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "core_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "fast_promotion_percentile": {"candidate": 0.1, "reference": null}, "market_risk_off_rule": {"candidate": "and", "reference": "negative_mom"}, "promoted_core_max_holdings": {"candidate": 2, "reference": 6}, "promoted_core_sell_exit_percentile": {"candidate": 0.85, "reference": 0.98}, "promotion_signal_mode": {"candidate": "weekly_alpha_pullback", "reference": null}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_risk_off_exposure": {"candidate": 0.0, "reference": 0.16}, "stable_core_max_holdings": {"candidate": 1, "reference": 2}, "standard_promotion_percentile": {"candidate": 0.15, "reference": null}, "variant_name": {"candidate": "进攻3/97 晋升2只(周频Alpha回踩, 熊市空仓, 单票65%, 持有5周, 换手10%, 出场85%, 单周)", "reference": "进攻8/92 晋升6只(成本压力熊市16%, 单票52%, 持有6周, 换手4%, 出场98%, 单周)"}, "weekly_min_hold_periods": {"candidate": 5, "reference": 6}, "weekly_turnover_cap": {"candidate": 0.1, "reference": 0.04}, "weight_cap": {"candidate": 0.65, "reference": 0.52}, "winner_core_promoted_share": {"candidate": 0.97, "reference": 0.92}, "winner_core_stable_share": {"candidate": 0.03, "reference": 0.08}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -13.84/-4.39pp，MaxDD差 -8.74/-7.76pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn032_exit98_risk16_20261007_weekly`：new_parameter，`reject`。参照 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`。

- 假设：相对robust只把单周换手上限4→3.2%；预期降成本同时保持中窗稳定性。 明确参数差异：{"variant_name": {"candidate": "相对robust只把单周换手上限4→3.2%；预期降成本同时保持中窗稳定性。", "reference": "进攻8/92 晋升6只(成本压力熊市16%, 单票52%, 持有6周, 换手4%, 出场98%, 单周)"}, "weekly_turnover_cap": {"candidate": 0.032, "reference": 0.04}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -4.20/-1.38pp，MaxDD差 +0.00/+7.10pp；2020/2023触发稳定性阈值，停止同形扩参。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution36_20261006,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn --comparison-csv /private/tmp/aiiter1007/ashare.csv

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution34_20261007,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_industry27_20261007,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_surge134_20261007,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn032_exit98_risk16_20261007_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_leader82_risk08_cap05_exit66_20261007,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiiter1007/ashare_new.csv

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn15_weekly,core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_breakout_risk50_cap60_hold2_turn30_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly

```

## A股 Path4（emergent theme discovery）

- `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`：parameter_confirmation，`reject`。参照 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。

- 假设：相对正式robust确认aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn形态；按emergent_theme_coverage检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"base_id": {"candidate": "core_explore_80_20_total_mv_winner_core", "reference": "core_explore_90_10_equal_weight_winner_core"}, "core_risk_off_exposure": {"candidate": 0.04, "reference": 0.08}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.38, "reference": 1.36}, "promoted_core_max_holdings": {"candidate": 24, "reference": 28}, "promoted_core_sell_exit_percentile": {"candidate": 0.7, "reference": 0.66}, "satellite_risk_off_exposure": {"candidate": 0.04, "reference": 0.08}, "standard_promotion_percentile": {"candidate": 0.29, "reference": 0.3}, "variant_name": {"candidate": "进攻13/87 晋升24只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市4%, 单票5%, 出场70%, 低换手)", "reference": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号30%, 龙头78%, 熊市8%, 单票5%, 出场66%, 低换手)"}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"base_id": {"candidate": "core_explore_80_20_total_mv_winner_core", "reference": "core_explore_90_10_equal_weight_winner_core"}, "core_risk_off_exposure": {"candidate": 0.04, "reference": 0.08}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.38, "reference": 1.36}, "promoted_core_max_holdings": {"candidate": 24, "reference": 28}, "promoted_core_sell_exit_percentile": {"candidate": 0.7, "reference": 0.66}, "satellite_risk_off_exposure": {"candidate": 0.04, "reference": 0.08}, "standard_promotion_percentile": {"candidate": 0.29, "reference": 0.3}, "variant_name": {"candidate": "进攻13/87 晋升24只(强主题涌现, 覆盖惩罚, 信号29%, 龙头78%, 熊市4%, 单票5%, 出场70%, 低换手)", "reference": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号30%, 龙头78%, 熊市8%, 单票5%, 出场66%, 低换手)"}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +1.77/-2.40pp，MaxDD差 -17.23/-20.72pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；隔离定义与历史保留

- `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn`：parameter_confirmation，`reject`。参照 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。

- 假设：相对正式robust确认aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn形态；按emergent_theme_coverage检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"base_id": {"candidate": "core_explore_80_20_total_mv_winner_core", "reference": "core_explore_90_10_equal_weight_winner_core"}, "core_quality_quantile": {"candidate": 0.74, "reference": 0.72}, "core_risk_off_exposure": {"candidate": 0.06, "reference": 0.08}, "explore_quality_quantile": {"candidate": 0.68, "reference": 0.66}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.4, "reference": 1.36}, "fast_promotion_min_industry_leader": {"candidate": 0.94, "reference": 0.92}, "fast_promotion_min_momentum_3_1_rank": {"candidate": 0.78, "reference": 0.76}, "fast_promotion_percentile": {"candidate": 0.04, "reference": 0.045}, "promoted_core_max_holdings": {"candidate": 30, "reference": 28}, "promoted_core_quality_quantile": {"candidate": 0.58, "reference": 0.56}, "promoted_core_sell_exit_percentile": {"candidate": 0.7, "reference": 0.66}, "satellite_risk_off_exposure": {"candidate": 0.06, "reference": 0.08}, "seed_quality_quantile": {"candidate": 0.52, "reference": 0.5}, "standard_promotion_min_industry_leader": {"candidate": 0.8, "reference": 0.78}, "standard_promotion_min_momentum_3_1_rank": {"candidate": 0.68, "reference": 0.66}, "variant_name": {"candidate": "进攻13/87 晋升24只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市6%, 单票4%, 出场70%, 低换手)", "reference": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号30%, 龙头78%, 熊市8%, 单票5%, 出场66%, 低换手)"}, "weight_cap": {"candidate": 0.04, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"base_id": {"candidate": "core_explore_80_20_total_mv_winner_core", "reference": "core_explore_90_10_equal_weight_winner_core"}, "core_quality_quantile": {"candidate": 0.74, "reference": 0.72}, "core_risk_off_exposure": {"candidate": 0.06, "reference": 0.08}, "explore_quality_quantile": {"candidate": 0.68, "reference": 0.66}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.4, "reference": 1.36}, "fast_promotion_min_industry_leader": {"candidate": 0.94, "reference": 0.92}, "fast_promotion_min_momentum_3_1_rank": {"candidate": 0.78, "reference": 0.76}, "fast_promotion_percentile": {"candidate": 0.04, "reference": 0.045}, "promoted_core_max_holdings": {"candidate": 30, "reference": 28}, "promoted_core_quality_quantile": {"candidate": 0.58, "reference": 0.56}, "promoted_core_sell_exit_percentile": {"candidate": 0.7, "reference": 0.66}, "satellite_risk_off_exposure": {"candidate": 0.06, "reference": 0.08}, "seed_quality_quantile": {"candidate": 0.52, "reference": 0.5}, "standard_promotion_min_industry_leader": {"candidate": 0.8, "reference": 0.78}, "standard_promotion_min_momentum_3_1_rank": {"candidate": 0.68, "reference": 0.66}, "variant_name": {"candidate": "进攻13/87 晋升24只(强主题涌现, 覆盖惩罚, 信号30%, 龙头80%, 熊市6%, 单票4%, 出场70%, 低换手)", "reference": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号30%, 龙头78%, 熊市8%, 单票5%, 出场66%, 低换手)"}, "weight_cap": {"candidate": 0.04, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +2.27/-2.17pp，MaxDD差 -9.50/-13.81pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；隔离定义与历史保留

- `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_leader82_risk08_cap05_exit66_20261007`：new_parameter，`reject`。参照 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。

- 假设：相对robust仅把行业龙头下限78→82%；检验质量筛选是否修复2026负收益并保持中窗稳定性。 明确参数差异：{"standard_promotion_min_industry_leader": {"candidate": 0.82, "reference": 0.78}, "variant_name": {"candidate": "相对robust仅把行业龙头下限78→82%；检验质量筛选是否修复2026负收益并保持中窗稳定性。", "reference": "进攻13/87 晋升22只(强主题涌现, 覆盖惩罚, 信号30%, 龙头78%, 熊市8%, 单票5%, 出场66%, 低换手)"}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +0.36/+0.00pp，MaxDD差 +0.40/+0.00pp；收益未形成可验证净改善且出现负CAGR，停止此形态扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；停止同形扩参；隔离定义与历史保留

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution36_20261006,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core,core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn --comparison-csv /private/tmp/aiiter1007/ashare.csv

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_caution34_20261007,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_industry27_20261007,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_surge134_20261007,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn032_exit98_risk16_20261007_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_leader82_risk08_cap05_exit66_20261007,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiiter1007/ashare_new.csv

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn

```

## A股 Path5（event knowledge graph）

- `ai_datacenter_power_grid_202607_v0`，source_audited，20/40/60D；keep_watch。40D转负，60D样本不足；单事件缺完整CAGR/Sharpe/MaxDD/换手口径，不能晋级。

- 20D +11.70%、40D -0.60%、60D不足；与Path4持仓重合0/6；gross/net成本不齐，不做晋级。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --basket-id ai_datacenter_power_grid_202607_v0 --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --path4-sample-tag since_2026_01 --output-json results/research/a_share/research_iteration_event_next.json

```

## 沪港通 Path1

- `hkconnect_path1_monthly_equal_buffered_weekly_overlay`：parameter_confirmation，`reject`。参照 `hkconnect_path1_biweekly_hybrid`。

- 假设：相对正式robust确认hkconnect_path1_monthly_equal_buffered_weekly_overlay形态；按monthly_weekly_overlay检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"base_weight_method": {"candidate": "equal_weight", "reference": "total_mv"}, "buy_entry_percentile": {"candidate": 0.2, "reference": 0.16}, "max_holdings": {"candidate": 12, "reference": 14}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.85, "reference": 0.8}, "risk_evaluation_frequency": {"candidate": "weekly", "reference": null}, "risk_off_exposure": {"candidate": 0.6, "reference": 0.5}, "risk_off_rule": {"candidate": "and", "reference": "or"}, "risk_overlay_scope": {"candidate": "portfolio_only", "reference": null}, "sell_exit_percentile": {"candidate": 0.35, "reference": 0.3}, "weight_cap": {"candidate": 0.16, "reference": 0.18}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"base_weight_method": {"candidate": "equal_weight", "reference": "total_mv"}, "buy_entry_percentile": {"candidate": 0.2, "reference": 0.16}, "max_holdings": {"candidate": 12, "reference": 14}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.85, "reference": 0.8}, "risk_evaluation_frequency": {"candidate": "weekly", "reference": null}, "risk_off_exposure": {"candidate": 0.6, "reference": 0.5}, "risk_off_rule": {"candidate": "and", "reference": "or"}, "risk_overlay_scope": {"candidate": "portfolio_only", "reference": null}, "sell_exit_percentile": {"candidate": 0.35, "reference": 0.3}, "weight_cap": {"candidate": 0.16, "reference": 0.18}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +6.21/+4.50pp，MaxDD差 -3.89/-11.87pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `hkconnect_path1_hybrid_caution74_20261007`：new_parameter，`reject`。参照 `hkconnect_path1_biweekly_hybrid`。

- 假设：相对当前robust只改谨慎仓位80→74%，检验中窗回撤改善与收益代价。 明确参数差异：{"risk_caution_exposure": {"candidate": 0.74, "reference": 0.8}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -0.42/-0.34pp，MaxDD差 -0.00/+0.00pp；同窗收益/回撤无实质增量，停止此形态扩参。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_monthly,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_hybrid_caution74_20261007,hkconnect_path1_biweekly_hybrid,hkconnect_path2_theme_entry11_20261007,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_theme_caution88_20261007,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_entry13_20261007,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_frozen_caution12_20261007,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_lowvol_caution78_20261007,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_defensive_caution58_20261007,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45,hkconnect_path1_biweekly_hybrid

```

## 沪港通 Path2

- `hkconnect_path2_breakout_cashoff_monthly`：parameter_confirmation，`reject`。参照 `hkconnect_path2_theme_entry10_20261006`。

- 假设：相对正式robust确认hkconnect_path2_breakout_cashoff_monthly形态；按high_return_monthly检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"risk_caution_exposure": {"candidate": 0.7, "reference": 0.9}, "risk_off_exposure": {"candidate": 0.0, "reference": 0.65}, "risk_off_rule": {"candidate": "and", "reference": "or"}, "sell_exit_percentile": {"candidate": 0.22, "reference": 0.18}, "signal_family": {"candidate": "path2_breakout", "reference": "path2_theme"}, "weight_cap": {"candidate": 0.28, "reference": 0.25}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"risk_caution_exposure": {"candidate": 0.7, "reference": 0.9}, "risk_off_exposure": {"candidate": 0.0, "reference": 0.65}, "risk_off_rule": {"candidate": "and", "reference": "or"}, "sell_exit_percentile": {"candidate": 0.22, "reference": 0.18}, "signal_family": {"candidate": "path2_breakout", "reference": "path2_theme"}, "weight_cap": {"candidate": 0.28, "reference": 0.25}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -4.26/-6.22pp，MaxDD差 -23.86/-8.68pp；2020/2023触发稳定性阈值，停止同形扩参。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `hkconnect_path2_theme_entry11_20261007`：new_parameter，`keep_watch`。参照 `hkconnect_path2_theme_entry10_20261006`。

- 假设：相对当前robust只改买入分位10→11%，检验入口广度而非继续cap扩参。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.11, "reference": 0.1}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +2.00/+1.40pp，MaxDD差 +0.17/-1.29pp；稳定性阈值通过，但净改善、成本或近窗仍需确认。

- 实际支持：True；正式身份变化：False；保留观察并要求中窗稳定性、近窗与净成本再验证

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_monthly,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_hybrid_caution74_20261007,hkconnect_path1_biweekly_hybrid,hkconnect_path2_theme_entry11_20261007,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_theme_caution88_20261007,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_entry13_20261007,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_frozen_caution12_20261007,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_lowvol_caution78_20261007,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_defensive_caution58_20261007,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_entry11_20261007,hkconnect_path2_breakout_concentrated_biweekly,hkconnect_path2_theme_entry10_20261006

```

## 沪港通 Path3

- `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard`：parameter_confirmation，`reject`。参照 `hkconnect_path3_theme_risk52_20261003`。

- 假设：相对正式robust确认hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard形态；按weekly_turnover_reduction检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"base_weight_mode": {"candidate": "hybrid", "reference": "signal"}, "buy_entry_percentile": {"candidate": 0.18, "reference": 0.07}, "max_holdings": {"candidate": 18, "reference": 5}, "risk_caution_exposure": {"candidate": 0.8, "reference": 0.9}, "risk_off_exposure": {"candidate": 0.55, "reference": 0.52}, "risk_off_rule": {"candidate": "and", "reference": "or"}, "sell_exit_percentile": {"candidate": 0.44, "reference": 0.16}, "signal_family": {"candidate": "path1_moderate", "reference": "path2_theme"}, "weight_cap": {"candidate": 0.09, "reference": 0.32}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"base_weight_mode": {"candidate": "hybrid", "reference": "signal"}, "buy_entry_percentile": {"candidate": 0.18, "reference": 0.07}, "max_holdings": {"candidate": 18, "reference": 5}, "risk_caution_exposure": {"candidate": 0.8, "reference": 0.9}, "risk_off_exposure": {"candidate": 0.55, "reference": 0.52}, "risk_off_rule": {"candidate": "and", "reference": "or"}, "sell_exit_percentile": {"candidate": 0.44, "reference": 0.16}, "signal_family": {"candidate": "path1_moderate", "reference": "path2_theme"}, "weight_cap": {"candidate": 0.09, "reference": 0.32}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -6.74/-11.83pp，MaxDD差 +18.13/-4.34pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `hkconnect_path3_theme_caution88_20261007`：new_parameter，`reject`。参照 `hkconnect_path3_theme_risk52_20261003`。

- 假设：相对当前robust只改谨慎仓位90→88%，检验高换手周频的风险成本权衡。 明确参数差异：{"risk_caution_exposure": {"candidate": 0.88, "reference": 0.9}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -0.20/-0.05pp，MaxDD差 +0.00/+0.00pp；同窗收益/回撤无实质增量，停止此形态扩参。 年均换手超过30倍，成本压力未解决。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_monthly,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_hybrid_caution74_20261007,hkconnect_path1_biweekly_hybrid,hkconnect_path2_theme_entry11_20261007,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_theme_caution88_20261007,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_entry13_20261007,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_frozen_caution12_20261007,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_lowvol_caution78_20261007,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_defensive_caution58_20261007,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover1_exit42_v10_ytd_repair,hkconnect_path3_theme_risk52_20261003

```

## 沪港通 Path4（quality / liquidity momentum）

- `hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter`：parameter_confirmation，`reject`。参照 `hkconnect_path4_liquidity_momentum_biweekly_smoke`。

- 假设：相对正式robust确认hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter形态；按quality_momentum检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.22, "reference": 0.14}, "max_holdings": {"candidate": 30, "reference": 12}, "risk_caution_exposure": {"candidate": 0.56, "reference": 0.78}, "risk_off_exposure": {"candidate": 0.26, "reference": 0.4}, "sell_exit_percentile": {"candidate": 0.38, "reference": 0.32}, "weight_cap": {"candidate": 0.045, "reference": 0.12}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.22, "reference": 0.14}, "max_holdings": {"candidate": 30, "reference": 12}, "risk_caution_exposure": {"candidate": 0.56, "reference": 0.78}, "risk_off_exposure": {"candidate": 0.26, "reference": 0.4}, "sell_exit_percentile": {"candidate": 0.38, "reference": 0.32}, "weight_cap": {"candidate": 0.045, "reference": 0.12}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -3.41/+0.37pp，MaxDD差 -5.27/+1.51pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `hkconnect_path4_liquidity_entry13_20261007`：new_parameter，`reject`。参照 `hkconnect_path4_liquidity_momentum_biweekly_smoke`。

- 假设：相对当前robust只改买入分位14→13%，检验更严格流动性动量选择。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.13, "reference": 0.14}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -0.77/+0.58pp，MaxDD差 -3.95/-0.89pp；收益未形成可验证净改善且出现负CAGR，停止此形态扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_monthly,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_hybrid_caution74_20261007,hkconnect_path1_biweekly_hybrid,hkconnect_path2_theme_entry11_20261007,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_theme_caution88_20261007,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_entry13_20261007,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_frozen_caution12_20261007,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_lowvol_caution78_20261007,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_defensive_caution58_20261007,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v14_ytd_repair,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v18_liquidity_repair,hkconnect_path4_liquidity_momentum_biweekly_smoke

```

## 沪港通 Path5（breakout retest / pullback continuation）

- `hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair`：parameter_confirmation，`reject`。参照 `hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`。

- 假设：相对正式robust确认hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair形态；按pullback_definition检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.42, "reference": 0.6}, "max_holdings": {"candidate": 42, "reference": 32}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.38, "reference": 0.2}, "risk_off_exposure": {"candidate": 0.02, "reference": 0.0}, "sell_exit_percentile": {"candidate": 0.58, "reference": 0.76}, "weight_cap": {"candidate": 0.028, "reference": 0.012}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.42, "reference": 0.6}, "max_holdings": {"candidate": 42, "reference": 32}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.38, "reference": 0.2}, "risk_off_exposure": {"candidate": 0.02, "reference": 0.0}, "sell_exit_percentile": {"candidate": 0.58, "reference": 0.76}, "weight_cap": {"candidate": 0.028, "reference": 0.012}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +2.18/+1.82pp，MaxDD差 -10.79/-8.94pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `hkconnect_path5_frozen_caution12_20261007`：new_parameter，`reject`。参照 `hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`。

- 假设：相对当前robust只改谨慎仓位20→12%，检验回踩信号近窗防守，不继续退出分位扩参。 明确参数差异：{"risk_caution_exposure": {"candidate": 0.12, "reference": 0.2}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 +0.05/-0.07pp，MaxDD差 -1.31/+0.00pp；收益未形成可验证净改善且出现负CAGR，停止此形态扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_monthly,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_hybrid_caution74_20261007,hkconnect_path1_biweekly_hybrid,hkconnect_path2_theme_entry11_20261007,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_theme_caution88_20261007,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_entry13_20261007,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_frozen_caution12_20261007,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_lowvol_caution78_20261007,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_defensive_caution58_20261007,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_pullback_continuation_monthly_quality_retest_v8_definition_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v9_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907

```

## 沪港通 Path6（large liquid core）

- `hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2`：parameter_confirmation，`keep_watch`。参照 `hkconnect_path6_lowvol_liquid_biweekly_smoke`。

- 假设：相对正式robust确认hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2形态；按large_liquid_core检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.22, "reference": 0.2}, "max_holdings": {"candidate": 24, "reference": 20}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.75, "reference": 0.82}, "risk_off_exposure": {"candidate": 0.4, "reference": 0.5}, "sell_exit_percentile": {"candidate": 0.42, "reference": 0.4}, "weight_cap": {"candidate": 0.07, "reference": 0.09}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.22, "reference": 0.2}, "max_holdings": {"candidate": 24, "reference": 20}, "rebalance_frequency": {"candidate": "monthly", "reference": "biweekly"}, "risk_caution_exposure": {"candidate": 0.75, "reference": 0.82}, "risk_off_exposure": {"candidate": 0.4, "reference": 0.5}, "sell_exit_percentile": {"candidate": 0.42, "reference": 0.4}, "weight_cap": {"candidate": 0.07, "reference": 0.09}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -0.01/-1.18pp，MaxDD差 +2.30/-0.90pp；稳定性阈值通过，但净改善、成本或近窗仍需确认。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：True；正式身份变化：False；保留观察并要求中窗稳定性、近窗与净成本再验证

- `hkconnect_path6_lowvol_caution78_20261007`：new_parameter，`reject`。参照 `hkconnect_path6_lowvol_liquid_biweekly_smoke`。

- 假设：相对当前robust只改谨慎仓位82→78%，检验低波核心风险控制。 明确参数差异：{"risk_caution_exposure": {"candidate": 0.78, "reference": 0.82}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -0.23/-0.06pp，MaxDD差 -0.02/-0.20pp；同窗收益/回撤无实质增量，停止此形态扩参。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_monthly,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_hybrid_caution74_20261007,hkconnect_path1_biweekly_hybrid,hkconnect_path2_theme_entry11_20261007,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_theme_caution88_20261007,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_entry13_20261007,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_frozen_caution12_20261007,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_lowvol_caution78_20261007,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_defensive_caution58_20261007,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_large_liquid_core_monthly_lowvol_liquidity_mix_v6,hkconnect_path6_lowvol_liquid_biweekly_smoke

```

## 沪港通 Path7（barbell quality growth）

- `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair`：parameter_confirmation，`reject`。参照 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`。

- 假设：相对正式robust确认hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair形态；按barbell_sleeve_structure检验2020/2023收益、回撤和换手，五窗排除近窗代价。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.38, "reference": 0.18}, "max_holdings": {"candidate": 56, "reference": 28}, "risk_caution_exposure": {"candidate": 0.32, "reference": 0.62}, "risk_off_exposure": {"candidate": 0.0, "reference": 0.24}, "sell_exit_percentile": {"candidate": 0.66, "reference": 0.36}, "weight_cap": {"candidate": 0.014, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。 明确参数差异：{"buy_entry_percentile": {"candidate": 0.38, "reference": 0.18}, "max_holdings": {"candidate": 56, "reference": 28}, "risk_caution_exposure": {"candidate": 0.32, "reference": 0.62}, "risk_off_exposure": {"candidate": 0.0, "reference": 0.24}, "sell_exit_percentile": {"candidate": 0.66, "reference": 0.36}, "weight_cap": {"candidate": 0.014, "reference": 0.05}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -6.54/-8.87pp，MaxDD差 +2.22/-0.66pp；2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

- `hkconnect_path7_defensive_caution58_20261007`：new_parameter，`reject`。参照 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`。

- 假设：相对当前robust只改谨慎仓位62→58%，检验杠铃近窗防守及中窗稳定性。 明确参数差异：{"risk_caution_exposure": {"candidate": 0.58, "reference": 0.62}}；预期降低风险或换手且不损伤中窗CAGR，实际支持情况由scorecard判定。

- 2020/2023 CAGR差 -0.16/-0.26pp，MaxDD差 +0.25/+0.00pp；同窗收益/回撤无实质增量，停止此形态扩参。

- 实际支持：False；正式身份变化：False；退出刷新，保留定义与历史快照

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay,hkconnect_path1_biweekly_hybrid,hkconnect_path2_breakout_cashoff_monthly,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_hybrid_caution74_20261007,hkconnect_path1_biweekly_hybrid,hkconnect_path2_theme_entry11_20261007,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_theme_caution88_20261007,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_entry13_20261007,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_frozen_caution12_20261007,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_lowvol_caution78_20261007,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_defensive_caution58_20261007,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v27_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_turnover_control_v20_ytd_guard,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

## 正式角色与退出刷新

A4/HK4/HK5存在近窗负收益的robust仅为robust_observation：进入观察位，不是强稳定 winner。机械artifact换位经二次scorecard冻结。

{
  "PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS = [": [
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly",
    "core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn032_exit98_risk16_20261007_weekly"
  ],
  "PATH2_ARCHIVED_STRATEGY_BASE_IDS = [": [
    "core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100",
    "core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95",
    "core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_surge134_20261007"
  ],
  "HK_ARCHIVED_STRATEGY_IDS = {": [
    "hkconnect_path1_monthly_equal_buffered_weekly_overlay",
    "hkconnect_path2_breakout_cashoff_monthly",
    "hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff55_turnover8_exit44_ytd_guard",
    "hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter",
    "hkconnect_path5_pullback_continuation_monthly_quality_retest_v20_definition_repair",
    "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v26_structure_repair",
    "hkconnect_path1_hybrid_caution74_20261007",
    "hkconnect_path3_theme_caution88_20261007",
    "hkconnect_path4_liquidity_entry13_20261007",
    "hkconnect_path5_frozen_caution12_20261007",
    "hkconnect_path6_lowvol_caution78_20261007",
    "hkconnect_path7_defensive_caution58_20261007",
    "hkconnect_path1_monthly_equal_buffered_weekly_overlay_defensive",
    "hkconnect_path2_inverse_elastic_monthly_cost_guard_v7",
    "hkconnect_path3_breakout_weekly",
    "hkconnect_path4_quality_momentum_monthly_cashguard_drawdown_v7",
    "hkconnect_path5_breakout_retest_biweekly_quality_confirm_v16_lowturn_retest",
    "hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v18_ytd_repair",
    "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_ytd_guard_v19"
  ]
}

所有完整CAGR、Sharpe、MaxDD、年换手、成本、差值和护栏命中见 results/research/a_share/research_iteration_scorecard_20261007.json。
