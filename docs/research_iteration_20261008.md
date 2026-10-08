# 2026-10-08 十二路径策略竞争记录

市场端点：A股2026-09-30，HK2026-10-07；候选与正式robust同市场五窗口同端点。12个真实新参数（A股5/HK7）、20-ID覆盖补缺和既有Path5事件复核分别统计。判定：{'keep_watch': 2, 'reject': 9, 'promote': 1}。

Path2覆盖592→572/832，正式身份冻结；因覆盖阻断预算回落至12，未达常规24–36。其余目标scope通过。

kb-web：既有9/16盈利修订快照哈希/PIT验证通过；0新MCP/0新credits，无新可证伪数据假设。HK旧代码02922.HK按1/665、1%容忍跳过。

五窗口：since_2017_01、since_2020_01、since_2023_01、since_2025_01、since_2026_01；所有卡包含CAGR、Sharpe、MaxDD、年换手、累计成本、参照值及delta。

本轮A股完整增量实跑命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_confirm3_20261008,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_growth25_20261008,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_cap12_20261008,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_hold5_20261008_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_mom70_20261008,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiiter1008/ashare_new.csv

```

本轮HK完整增量实跑命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_hybrid_hold16_20261008,hkconnect_path1_biweekly_hybrid,hkconnect_path2_theme_hold7_20261008,hkconnect_path2_theme_entry11_20261007,hkconnect_path3_theme_hold6_20261008,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_liquidity_hold14_20261008,hkconnect_path4_liquidity_momentum_biweekly_smoke,hkconnect_path5_pullback_hold28_20261008,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_lowvol_hold18_20261008,hkconnect_path6_lowvol_liquid_biweekly_smoke,hkconnect_path7_barbell_hold30_20261008,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

## A股 Path1（主线与core_multifactor）

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_satellite_confirm3_20261008`：new_parameter，`keep_watch`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：主线只把风险状态确认2周延至3周；减少卫星仓位噪声切换，预期降换手而不损伤2020/2023收益或2026防守。

- 实际参数差异：`{"risk_stage_confirm_weeks": {"candidate": 3, "reference": 2}}`。

- 2020/2023 CAGR差 +0.04/+0.18pp，MaxDD差 +0.00/+0.00pp；2026 CAGR +0.66%，最大年换手 6.54x。稳定性阈值通过，但净改善、成本或近窗仍需确认。

- 假设验证支持：False；正式身份变化：False；保留active/watch，最多3轮观察成本与稳定性。

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_growth25_20261008`：new_parameter，`reject`。参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。

- 假设：core_multifactor从quality_tilt动量6-1转移10pp到成长加速；检验新增长质量协同能否缩小与正式robust的中窗差距，避免继续行业权重失败形态。

- 实际参数差异：`{"core_signal_mode": {"candidate": "multi_factor", "reference": null}, "factor_weights": {"candidate": {"growth_acceleration": 0.25, "industry_leader": 0.1, "industry_strength": 0.1, "liquidity_surge": 0.05, "momentum_3_1": 0.1, "momentum_6_1": 0.1, "quality": 0.3}, "reference": null}, "market_risk_off_rule": {"candidate": null, "reference": "and"}, "promoted_core_max_holdings": {"candidate": 7, "reference": 8}, "promoted_core_sell_exit_percentile": {"candidate": null, "reference": 0.52}, "risk_evaluation_frequency": {"candidate": null, "reference": "weekly"}, "risk_overlay_scope": {"candidate": null, "reference": "satellite_only"}, "risk_stage_buffered": {"candidate": null, "reference": true}, "risk_stage_confirm_weeks": {"candidate": null, "reference": 2}, "risk_staging_mode": {"candidate": null, "reference": "three_stage"}, "satellite_caution_exposure": {"candidate": null, "reference": 0.44}, "satellite_risk_off_exposure": {"candidate": null, "reference": 0.2}}`。

- 2020/2023 CAGR差 -21.47/-5.29pp，MaxDD差 +7.82/+10.80pp；2026 CAGR +4.23%，最大年换手 5.78x。2020/2023触发稳定性阈值，停止同形扩参。

- 假设验证支持：False；正式身份变化：False；停止同形扩参，隔离定义与历史保留。

- 主线confirm3与core_multifactor growth25分别实跑；core_multifactor实际原有64/64覆盖pass，新组合单独计入预算，active未扩张。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_balanced,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_balanced,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907

```

## A股 Path2

- `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_cap12_20261008`：new_parameter，`reject`。参照 `core_explore_70_30_equal_weight_winner_core`。

- 假设：欠配双周流动动量族仅将单票上限14→12%；检验容量与分散度能否修复中窗回撤，同时记录仓位不足和收益代价；block下禁止晋级。

- 实际参数差异：`{"core_caution_exposure": {"candidate": 0.58, "reference": null}, "core_risk_off_exposure": {"candidate": 0.2, "reference": null}, "core_signal_mode": {"candidate": "6_1", "reference": null}, "fast_promotion_min_amount_surge_ratio": {"candidate": 1.26, "reference": null}, "fast_promotion_min_momentum_3_1_rank": {"candidate": 0.78, "reference": null}, "fast_promotion_min_momentum_6_1_rank": {"candidate": 0.985, "reference": null}, "fast_promotion_min_recent_1m_return": {"candidate": 0.01, "reference": null}, "fast_promotion_percentile": {"candidate": 0.09, "reference": null}, "market_risk_off_rule": {"candidate": "negative_mom", "reference": null}, "promoted_core_max_holdings": {"candidate": 3, "reference": null}, "promoted_core_sell_exit_percentile": {"candidate": 0.4, "reference": null}, "promoted_core_stage_ramp": {"candidate": {"1": 1.0}, "reference": null}, "promotion_signal_mode": {"candidate": "liquidity_momentum", "reference": null}, "rebalance_frequency": {"candidate": "biweekly", "reference": null}, "risk_staging_mode": {"candidate": "three_stage", "reference": null}, "satellite_caution_exposure": {"candidate": 0.4, "reference": null}, "satellite_risk_off_exposure": {"candidate": 0.2, "reference": null}, "stable_core_max_holdings": {"candidate": 1, "reference": null}, "standard_promotion_min_momentum_3_1_rank": {"candidate": 0.74, "reference": null}, "standard_promotion_min_momentum_6_1_rank": {"candidate": 0.96, "reference": null}, "standard_promotion_percentile": {"candidate": 0.14, "reference": null}, "weight_cap": {"candidate": 0.12, "reference": null}, "winner_core_promoted_share": {"candidate": 0.97, "reference": null}, "winner_core_stable_share": {"candidate": 0.03, "reference": null}}`。

- 2020/2023 CAGR差 -2.48/-9.91pp，MaxDD差 -6.04/+9.61pp；2026 CAGR -23.16%，最大年换手 18.13x。2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。 全集coverage仍block，禁止promote。

- 假设验证支持：False；正式身份变化：False；退出刷新，保留历史定义与快照。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_3_1_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_3_1_full_risk_cap100,core_explore_70_30_equal_weight_winner_core

```

## A股 Path3

- `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_hold5_20261008_weekly`：new_parameter，`reject`。参照 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`。

- 假设：纯周频把最短持有6周降至5周；检验稍快释放弱仓是否改善中窗回撤，记录换手和成本增加。

- 实际参数差异：`{"weekly_min_hold_periods": {"candidate": 5, "reference": 6}}`。

- 2020/2023 CAGR差 +0.10/-4.09pp，MaxDD差 -1.10/+6.28pp；2026 CAGR +30.22%，最大年换手 2.51x。2020/2023触发稳定性阈值，停止同形扩参。

- 假设验证支持：False；正式身份变化：False；退出刷新，保留历史定义与快照。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn15_weekly,core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_breakout_risk50_cap60_hold2_turn30_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly

```

## A股 Path4（emergent theme discovery）

- `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_mom70_20261008`：new_parameter，`keep_watch`。参照 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。

- 假设：独立强主题将3-1动量门槛66→70%，用市场结构筛选而非人工主题；预期降低弱主题和2026亏损，检验中窗及容量代价。

- 实际参数差异：`{"standard_promotion_min_momentum_3_1_rank": {"candidate": 0.7, "reference": 0.66}}`。

- 2020/2023 CAGR差 +1.04/+0.00pp，MaxDD差 +1.07/+0.00pp；2026 CAGR -7.92%，最大年换手 4.09x。稳定性阈值通过，但净改善、成本或近窗仍需确认。 存在负CAGR窗口，不能视为强稳定winner。

- 假设验证支持：True；正式身份变化：False；保留active/watch，最多3轮观察成本与稳定性。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn

```

## A股 Path5（event knowledge graph）

- `ai_datacenter_power_grid_202607_v0` source_audited冻结篮子，horizon20/40/60，keep_watch；20D +11.70%、40D -0.60%、60D不足；Path4 overlap 0/6。没有新增已审计事件，v1仅设计不实跑；gross事件篮子与net Path4成本口径不同，不据此晋级。

- 40D转负，60D样本不足；单事件缺完整CAGR/Sharpe/MaxDD/换手口径，不能晋级。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --basket-id ai_datacenter_power_grid_202607_v0 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --path4-sample-tag since_2026_01 --output-json results/research/a_share/research_iteration_event_next.json

```

## 沪港通 Path1

- `hkconnect_path1_hybrid_hold16_20261008`：new_parameter，`reject`。参照 `hkconnect_path1_biweekly_hybrid`。

- 假设：相对当前robust只改持仓14→16只，检验分散度对中窗回撤、换手及容量的影响。

- 实际参数差异：`{"max_holdings": {"candidate": 16, "reference": 14}}`。

- 2020/2023 CAGR差 -0.16/-0.18pp，MaxDD差 +1.17/-0.08pp；2026 CAGR -0.48%，最大年换手 3.51x。收益未形成可验证净改善且出现负CAGR，停止此形态扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 假设验证支持：False；正式身份变化：False；退出刷新，保留历史定义与快照。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45,hkconnect_path1_biweekly_hybrid

```

## 沪港通 Path2

- `hkconnect_path2_theme_hold7_20261008`：new_parameter，`reject`。参照 `hkconnect_path2_theme_entry11_20261007`。

- 假设：相对当前robust只改月频主题持仓6→7只，检验中窗稳健性与2026弹性；停止只改买入分位。

- 实际参数差异：`{"max_holdings": {"candidate": 7, "reference": 6}}`。

- 2020/2023 CAGR差 -1.17/-4.73pp，MaxDD差 +2.47/+2.47pp；2026 CAGR +5.41%，最大年换手 8.22x。2020/2023触发稳定性阈值，停止同形扩参。

- 假设验证支持：False；正式身份变化：False；退出刷新，保留历史定义与快照。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_breakout_concentrated_monthly,hkconnect_path2_breakout_monthly,hkconnect_path2_theme_entry11_20261007

```

## 沪港通 Path3

- `hkconnect_path3_theme_hold6_20261008`：new_parameter，`reject`。参照 `hkconnect_path3_theme_risk52_20261003`。

- 假设：相对当前robust只改周频主题持仓5→6只，检验集中风险下降及高换手成本。

- 实际参数差异：`{"max_holdings": {"candidate": 6, "reference": 5}}`。

- 2020/2023 CAGR差 -5.61/-12.55pp，MaxDD差 -0.35/-4.88pp；2026 CAGR -4.40%，最大年换手 36.30x。2020/2023触发稳定性阈值，停止同形扩参。 存在负CAGR窗口，不能视为强稳定winner。 年均换手超过30倍，成本压力未解决。

- 假设验证支持：False；正式身份变化：False；退出刷新，保留历史定义与快照。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover1_exit42_v10_ytd_repair,hkconnect_path3_theme_risk52_20261003

```

## 沪港通 Path4（quality / liquidity momentum）

- `hkconnect_path4_liquidity_hold14_20261008`：new_parameter，`reject`。参照 `hkconnect_path4_liquidity_momentum_biweekly_smoke`。

- 假设：相对当前robust只改流动动量持仓12→14只，检验弱路径分散化能否修复近窗。

- 实际参数差异：`{"max_holdings": {"candidate": 14, "reference": 12}}`。

- 2020/2023 CAGR差 -1.63/-1.10pp，MaxDD差 -0.24/-0.02pp；2026 CAGR -7.89%，最大年换手 11.24x。收益未形成可验证净改善且出现负CAGR，停止此形态扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 假设验证支持：False；正式身份变化：False；退出刷新，保留历史定义与快照。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v14_ytd_repair,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v18_liquidity_repair,hkconnect_path4_liquidity_momentum_biweekly_smoke

```

## 沪港通 Path5（breakout retest / pullback continuation）

- `hkconnect_path5_pullback_hold28_20261008`：new_parameter，`reject`。参照 `hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`。

- 假设：相对当前robust只改回踩持仓32→28只，检验低权重下仓位减少是否导致容量/收益不足。

- 实际参数差异：`{"max_holdings": {"candidate": 28, "reference": 32}}`。

- 2020/2023 CAGR差 -0.28/-0.79pp，MaxDD差 +1.71/-0.58pp；2026 CAGR -6.23%，最大年换手 1.85x。收益未形成可验证净改善且出现负CAGR，停止此形态扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 假设验证支持：False；正式身份变化：False；退出刷新，保留历史定义与快照。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_pullback_continuation_monthly_quality_retest_v8_definition_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v9_definition_repair,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907

```

## 沪港通 Path6（large liquid core）

- `hkconnect_path6_lowvol_hold18_20261008`：new_parameter，`promote`。参照 `hkconnect_path6_lowvol_liquid_biweekly_smoke`。

- 假设：相对当前robust只改低波核心持仓20→18只，检验核心集中带来的中窗收益与回撤代价。

- 实际参数差异：`{"max_holdings": {"candidate": 18, "reference": 20}}`。

- 2020/2023 CAGR差 +0.79/+1.72pp，MaxDD差 -0.08/-0.23pp；2026 CAGR +4.57%，最大年换手 3.01x。五窗净CAGR/Sharpe均增、换手与成本均降，五窗收益正，中窗稳定性通过；2017 MaxDD恶化0.98pp、2020/2023恶化0.08/0.23pp，风险代价小于1pp但需保留监测。真实窗口winner锚点四项ADJACENT_VALIDATION_THRESHOLDS通过，可进入正式robust晋级。

- 假设验证支持：True；正式身份变化：True；完成相邻验证，进入正式晋级流程。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_lowvol_liquidity_mix_v6,hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v10,hkconnect_path6_lowvol_hold18_20261008

```

## 沪港通 Path7（barbell quality growth）

- `hkconnect_path7_barbell_hold30_20261008`：new_parameter，`reject`。参照 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`。

- 假设：相对当前robust只改杠铃持仓28→30只，检验分散化保住中窗收益与近窗防守。

- 实际参数差异：`{"max_holdings": {"candidate": 30, "reference": 28}}`。

- 2020/2023 CAGR差 -0.54/-0.71pp，MaxDD差 -0.45/-0.30pp；2026 CAGR -1.53%，最大年换手 5.77x。收益未形成可验证净改善且出现负CAGR，停止此形态扩参。 存在负CAGR窗口，不能视为强稳定winner。

- 假设验证支持：False；正式身份变化：False；退出刷新，保留历史定义与快照。

下一轮第一条命令：

```sh

AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_quality_v27_structure_repair,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_turnover_control_v25_ytd_guard,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7

```

## 正式身份、观察与退出刷新

[
  {
    "path": "path6",
    "slot": "robust_candidate",
    "old_id": "hkconnect_path6_lowvol_liquid_biweekly_smoke",
    "new_id": "hkconnect_path6_lowvol_hold18_20261008",
    "adjacent_validation": [
      {
        "passed": true,
        "candidate_id": "hkconnect_path6_lowvol_hold18_20261008",
        "target_window": "since_2017_01",
        "validation_window": "since_2020_01",
        "threshold": 0.75,
        "absolute_floor": 0.0,
        "incumbent_id": "hkconnect_path6_large_liquid_core_monthly_smoke",
        "candidate_cagr": 0.13551071,
        "incumbent_cagr": 0.16610237,
        "required_cagr": 0.1245767775,
        "reason": "threshold_check"
      },
      {
        "passed": true,
        "candidate_id": "hkconnect_path6_lowvol_hold18_20261008",
        "target_window": "since_2020_01",
        "validation_window": "since_2023_01",
        "threshold": 0.7,
        "absolute_floor": 0.0,
        "incumbent_id": "hkconnect_path6_large_liquid_core_monthly_smoke",
        "candidate_cagr": 0.20801225,
        "incumbent_cagr": 0.22609555,
        "required_cagr": 0.158266885,
        "reason": "threshold_check"
      },
      {
        "passed": true,
        "candidate_id": "hkconnect_path6_lowvol_hold18_20261008",
        "target_window": "since_2023_01",
        "validation_window": "since_2025_01",
        "threshold": 0.6,
        "absolute_floor": 0.0,
        "incumbent_id": "hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v10",
        "candidate_cagr": 0.20840381,
        "incumbent_cagr": 0.22317153,
        "required_cagr": 0.133902918,
        "reason": "threshold_check"
      },
      {
        "passed": true,
        "candidate_id": "hkconnect_path6_lowvol_hold18_20261008",
        "target_window": "since_2025_01",
        "validation_window": "since_2023_01",
        "threshold": 0.7,
        "absolute_floor": 0.0,
        "incumbent_id": "hkconnect_path6_large_liquid_core_monthly_smoke",
        "candidate_cagr": 0.20801225,
        "incumbent_cagr": 0.22609555,
        "required_cagr": 0.158266885,
        "reason": "threshold_check"
      }
    ]
  },
  {
    "path": "path6",
    "slot": "since_2026_01",
    "old_id": "hkconnect_path6_lowvol_liquid_biweekly_smoke",
    "new_id": "hkconnect_path6_lowvol_hold18_20261008",
    "adjacent_validation": [
      {
        "passed": true,
        "candidate_id": "hkconnect_path6_lowvol_hold18_20261008",
        "target_window": "since_2026_01",
        "validation_window": null,
        "reason": "no_adjacent_window"
      }
    ]
  }
]

其它window winner/robust身份未变；tracked payload仅同端点指标/观察同步。负minCAGR或2026亏损的A4/HK4/HK5 robust为robust_observation：进入观察位，不是强稳定 winner。

新增前弱候选淘汰：`[{"path": "hkconnect_path1", "candidate_id": "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit28_v15_2026_repair", "decision": "reject", "reason": "active已超软上限；新增前淘汰五窗最差minCAGR候选，保留历史与定义", "min_cagr": -0.33730612, "worst_maxdd": -0.29292214}, {"path": "hkconnect_path2", "candidate_id": "hkconnect_path2_inverse_elastic_monthly_cost_guard_v4", "decision": "reject", "reason": "active已超软上限；新增前淘汰五窗最差minCAGR候选，保留历史与定义", "min_cagr": -0.43751, "worst_maxdd": -0.37016576}, {"path": "hkconnect_path3", "candidate_id": "hkconnect_path3_breakout_risk50_weekly", "decision": "reject", "reason": "active已超软上限；新增前淘汰五窗最差minCAGR候选，保留历史与定义", "min_cagr": -0.37166525, "worst_maxdd": -0.61753716}, {"path": "hkconnect_path4", "candidate_id": "hkconnect_path4_quality_liquidity_momentum_monthly_v9", "decision": "reject", "reason": "active已超软上限；新增前淘汰五窗最差minCAGR候选，保留历史与定义", "min_cagr": -0.2144415, "worst_maxdd": -0.22852664}, {"path": "hkconnect_path5", "candidate_id": "hkconnect_path5_breakout_retest_biweekly_quality_confirm_v15_retest_confirmation", "decision": "reject", "reason": "active已超软上限；新增前淘汰五窗最差minCAGR候选，保留历史与定义", "min_cagr": -0.24511661, "worst_maxdd": -0.27284626}, {"path": "hkconnect_path6", "candidate_id": "hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v16_core_reconfirm", "decision": "reject", "reason": "active已超软上限；新增前淘汰五窗最差minCAGR候选，保留历史与定义", "min_cagr": -0.24756274, "worst_maxdd": -0.22790678}, {"path": "hkconnect_path7", "candidate_id": "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_turnover_control_v20_ytd_guard", "decision": "reject", "reason": "active已超软上限；新增前淘汰五窗最差minCAGR候选，保留历史与定义", "min_cagr": -0.13858982, "worst_maxdd": -0.19378971}]`。

本轮退出刷新ID：`{"PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS = [": ["core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_hold5_20261008_weekly"], "PATH2_ARCHIVED_STRATEGY_BASE_IDS = [": ["core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn_cap12_20261008"], "HK_ARCHIVED_STRATEGY_IDS = {": ["hkconnect_path1_hybrid_hold16_20261008", "hkconnect_path2_theme_hold7_20261008", "hkconnect_path3_theme_hold6_20261008", "hkconnect_path4_liquidity_hold14_20261008", "hkconnect_path5_pullback_hold28_20261008", "hkconnect_path7_barbell_hold30_20261008", "hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit28_v15_2026_repair", "hkconnect_path2_inverse_elastic_monthly_cost_guard_v4", "hkconnect_path3_breakout_risk50_weekly", "hkconnect_path4_quality_liquidity_momentum_monthly_v9", "hkconnect_path5_breakout_retest_biweekly_quality_confirm_v15_retest_confirmation", "hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v16_core_reconfirm", "hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_turnover_control_v20_ytd_guard"]}`。历史定义与快照保留，无物理删除。

完整指标、delta、假设、护栏、十二路径下一轮命令和最终guard见 research_iteration_scorecard_20261008.json。


## 手动反思轮 2026-10-08T18:48:57+08:00：开轮决策（回测前预登记）

首次反思记录缺失，因此以10/06、10/07、10/08自动轮报告及scorecard作为基线。本轮不把候选数量当作进步；预登记完整设计、父配置、支持/证伪条件保存在本轮独立scorecard，保留上午报告。

上轮动作核对：12个上午新参数已实跑，9 reject/2 keep_watch/1 promote；HK6 hold18已进入当前正式robust。本轮继续落实Path2精确20-ID补缺。原下一轮多因子balanced复跑、HK持仓/分位邻近扩参取消，改为冻结父形态的信号/风控/权重消融；已有Path5单事件20/40D反复复核取消，改为检查60D成熟度和gross/net口径。其余旧首命令保留为备选，不默认照抄。

A股问题：过去多因子候选同时改变信号、持仓、风险执行，其劣势不能单独归因于因子。以正式robust形态替换冻结多因子信号，并把robust风控移植到原quality_tilt，分别检验信号与风险执行；不继续成长/行业权重小幅搜索。HK问题：反复调持仓或谨慎仓位多数失败，且Path5 max_holdings32×cap1.2%=38.4%隐含容量上限。冻结信号/风险，分别检验权重映射和容量上限机制。两个研究问题均需同父策略和当前正式robust分别比较，避免弱参照制造晋级。

预算：Path2仍block572/832，按任务阻断规则回落至12个新机制实验（A股5/HK7），coverage20-ID与参照不计新增。A股截止日依guard为2026-09-30；HK本地prepare_progress到2026-10-08、665/666缓存覆盖，旧02922.HK为容忍缺口；不补raw cache。HK诊断ID归档且只用explicit IDs执行，不扩大已有超cap的自动active池。

- ashare_path1 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual`：保留正式robust持仓与周频卫星风控，仅替换为冻结quality_tilt核心信号；区分多因子选股效应与既往持仓/风控混杂。 支持条件：父策略2020/2023 CAGR均不降且至少一窗提高1pp；五窗无稳定性破坏，成本和2026风险不恶化。
- ashare_path1 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual`：冻结quality_tilt因子和持仓，仅移植正式robust的周频卫星风控；检验旧多因子落后是否主要来自执行风控差异。 支持条件：相对冻结父策略2020/2023 CAGR均改善至少1pp，且MaxDD均改善至少2pp；再独立比较正式robust，不能以弱父策略晋级。
- ashare_path2 `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_ablation_20261008_manual`：欠配v63保持持仓、风险、换手、晋升门槛，移除流动动量晋升排序改用6-1；定位信号机制而非继续调cap/surge。 支持条件：父策略2020/2023 CAGR均改善至少1pp且MaxDD不恶化；coverage block期间只诊断，禁止promote。
- ashare_path3 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly`：保持纯周频和4%周换手上限，完全移除最短持有保护；验证此前5/6周小调失败是否说明保护机制必要。 支持条件：父策略2020/2023 CAGR均不降、任一窗MaxDD改善至少2pp，且年换手不增加超过1倍。
- ashare_path4 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual`：保持自动强主题信号，移除常规与快速晋升的行业龙头硬门槛；检验门槛是否造成2026选股不足，停止相邻门槛微调。 支持条件：父策略2026 CAGR提高至少3pp，2020/2023不触发护栏；若仍负收益仅观察，不称稳定winner。
- hkconnect_path1 `hkconnect_path1_mechanism_20261008_manual`：冻结path1_moderate排序、持仓与风控，仅改变权重映射hybrid→base；验证信号强度配权/市值混合的收益与换手贡献。 支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- hkconnect_path2 `hkconnect_path2_mechanism_20261008_manual`：冻结path2_theme排序、持仓与风控，仅改变权重映射signal→base；验证信号强度配权/市值混合的收益与换手贡献。 支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- hkconnect_path3 `hkconnect_path3_mechanism_20261008_manual`：冻结path2_theme排序、持仓与风控，仅改变权重映射signal→base；验证信号强度配权/市值混合的收益与换手贡献。 支持条件：父策略2020/2023净CAGR均不降，年換手五窗平均下降至少20%，2026为正；周频保持不变。
- hkconnect_path4 `hkconnect_path4_mechanism_20261008_manual`：冻结path4_quality_momentum排序、持仓与风控，仅改变权重映射hybrid→signal；验证信号强度配权/市值混合的收益与换手贡献。 支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- hkconnect_path5 `hkconnect_path5_mechanism_20261008_manual`：冻结回踩信号、32持仓和风险，仅将单票容量上限设为1/32；原32×1.2%=38.4%最高投入，验证低仓位是否掩盖信号而非继续调持仓。 支持条件：先核实实际平均投入提高至少10pp；父策略2020/2023净CAGR均增至少1pp且2026转正才支持收益机制，护栏仍必须通过。
- hkconnect_path6 `hkconnect_path6_mechanism_20261008_manual`：冻结path6_large_liquid_core排序、持仓与风控，仅改变权重映射hybrid→base；验证信号强度配权/市值混合的收益与换手贡献。 支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- hkconnect_path7 `hkconnect_path7_mechanism_20261008_manual`：冻结path7_barbell_quality_growth排序、持仓与风控，仅改变权重映射hybrid→signal；验证信号强度配权/市值混合的收益与换手贡献。 支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。


## 手动反思轮 2026-10-08T19:19:01+08:00：完成记录

实际完成12个机制消融（A股5/HK7）五窗口同市场同截止日回测，判定 {'reject': 11, 'robust_observation': 1}。Path2精确20-ID四窗补缺 572→552/832，仍block，正式身份冻结。新增、coverage与Path5历史复核分开统计；因阻断按任务规则回落12，未达24–36常规目标。

完整逐窗CAGR/Sharpe/MaxDD/年换手/累计成本、正式参照delta、父策略delta、回测前假设和判定均见 `results/research/a_share/research_iteration_scorecard_20261008_manual.json`。当前工作树源码哈希已记录；回测使用已有用户改动，提交只包含本轮片段，不宣称原有未提交源码已经发布。

### A股 Path1（主线固定，core_multifactor控制变量）

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual`：`reject`；父策略 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`；正式参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。
- 假设：保留正式robust持仓与周频卫星风控，仅替换为冻结quality_tilt核心信号；区分多因子选股效应与既往持仓/风控混杂。
- 预登记支持条件：父策略2020/2023 CAGR均不降且至少一窗提高1pp；五窗无稳定性破坏，成本和2026风险不恶化。
- 2020/2023正式参照CAGR差 -12.71pp/+4.59pp；2026 CAGR +16.20%；机制支持=False。中窗正式参照护栏失守。 当前引擎数值未达到预登记统计条件。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

- `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual`：`reject`；父策略 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_quality_tilt`；正式参照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`。
- 假设：冻结quality_tilt因子和持仓，仅移植正式robust的周频卫星风控；检验旧多因子落后是否主要来自执行风控差异。
- 预登记支持条件：相对冻结父策略2020/2023 CAGR均改善至少1pp，且MaxDD均改善至少2pp；再独立比较正式robust，不能以弱父策略晋级。
- 2020/2023正式参照CAGR差 -15.15pp/-0.50pp；2026 CAGR +8.75%；机制支持=False。中窗正式参照护栏失守。 当前引擎数值未达到预登记统计条件。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_quality_tilt,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_ablation_20261008_manual,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiinvestor_manual_20261008_reflection/ashare.csv
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/a_share/core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### A股 Path2

- `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_ablation_20261008_manual`：`reject`；父策略 `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`；正式参照 `core_explore_70_30_equal_weight_winner_core`。
- 假设：欠配v63保持持仓、风险、换手、晋升门槛，移除流动动量晋升排序改用6-1；定位信号机制而非继续调cap/surge。
- 预登记支持条件：父策略2020/2023 CAGR均改善至少1pp且MaxDD不恶化；coverage block期间只诊断，禁止promote。
- 2020/2023正式参照CAGR差 -2.30pp/-9.33pp；2026 CAGR -24.36%；机制支持=False。消融后五窗关键指标完全不变，未验证该机制有贡献；需检查约束饱和/配置是否生效。 当前引擎数值未达到预登记统计条件。 Path2全集coverage未补齐，禁止promote。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_quality_tilt,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_ablation_20261008_manual,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiinvestor_manual_20261008_reflection/ashare.csv
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_biweekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_3_1_full_risk_cap40,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_6_1,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_6_1_full_risk,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_biweekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_biweekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_balanced,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm --end-date 2026-09-30
```

### A股 Path3

- `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly`：`reject`；父策略 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`；正式参照 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`。
- 假设：保持纯周频和4%周换手上限，完全移除最短持有保护；验证此前5/6周小调失败是否说明保护机制必要。
- 预登记支持条件：父策略2020/2023 CAGR均不降、任一窗MaxDD改善至少2pp，且年换手不增加超过1倍。
- 2020/2023正式参照CAGR差 -2.65pp/-2.55pp；2026 CAGR +26.85%；机制支持=False。相对正式参照有部分收益/防守增量，尚未确认全部预登记条件。 当前引擎数值未达到预登记统计条件。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_quality_tilt,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_ablation_20261008_manual,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiinvestor_manual_20261008_reflection/ashare.csv
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/a_share/core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### A股 Path4

- `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual`：`robust_observation`；父策略 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；正式参照 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。
- 假设：保持自动强主题信号，移除常规与快速晋升的行业龙头硬门槛；检验门槛是否造成2026选股不足，停止相邻门槛微调。
- 预登记支持条件：父策略2026 CAGR提高至少3pp，2020/2023不触发护栏；若仍负收益仅观察，不称稳定winner。
- 2020/2023正式参照CAGR差 +3.44pp/+0.92pp；2026 CAGR -7.92%；机制支持=False。相对正式参照有部分收益/防守增量，尚未确认全部预登记条件。 当前引擎数值未达到预登记统计条件。 进入观察位，不是强稳定 winner。
- 正式window winner/robust/tracked均未改变；隔离诊断；不加入自动active；保留定义、结果和明确后续验证。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_quality_tilt,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_ablation_20261008_manual,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiinvestor_manual_20261008_reflection/ashare.csv
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/a_share/core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### A股 Path5

已复核source_audited冻结篮子 `ai_datacenter_power_grid_202607_v0`；20D +11.70%、40D -0.60%、60D不足。keep_watch；gross事件篮子与net Path4口径不同，不混算winner。没有新增已审计事件，v1未冻结，故只做成熟度复核，不冒充新实验。

实际命令：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --basket-id ai_datacenter_power_grid_202607_v0 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --path4-sample-tag since_2026_01 --output-json results/research/a_share/research_iteration_event_20261008_manual.json
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c "import json; d=json.load(open('results/research/a_share/research_iteration_event_20261008_manual.json')); print(d['portfolio_returns']['60']); print(d['notes'])"
```

### 沪港通 Path1

- `hkconnect_path1_mechanism_20261008_manual`：`reject`；父策略 `hkconnect_path1_biweekly_hybrid`；正式参照 `hkconnect_path1_biweekly_hybrid`。
- 假设：冻结path1_moderate排序、持仓与风控，仅改变权重映射hybrid→base；验证信号强度配权/市值混合的收益与换手贡献。
- 预登记支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- 2020/2023正式参照CAGR差 -0.59pp/+0.24pp；2026 CAGR +0.98%；机制支持=False。相对正式参照有部分收益/防守增量，尚未确认全部预登记条件。 当前引擎数值未达到预登记统计条件。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path2_mechanism_20261008_manual,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality,hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008,hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path1_mechanism_20261008_manual__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### 沪港通 Path2

- `hkconnect_path2_mechanism_20261008_manual`：`reject`；父策略 `hkconnect_path2_theme_entry10_20261006`；正式参照 `hkconnect_path2_theme_entry10_20261006`。
- 假设：冻结path2_theme排序、持仓与风控，仅改变权重映射signal→base；验证信号强度配权/市值混合的收益与换手贡献。
- 预登记支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- 2020/2023正式参照CAGR差 +5.07pp/+3.73pp；2026 CAGR +0.74%；机制支持=False。中窗正式参照护栏失守。 当前引擎数值未达到预登记统计条件。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path2_mechanism_20261008_manual,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality,hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008,hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path2_mechanism_20261008_manual__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### 沪港通 Path3

- `hkconnect_path3_mechanism_20261008_manual`：`reject`；父策略 `hkconnect_path3_theme_risk52_20261003`；正式参照 `hkconnect_path3_theme_risk52_20261003`。
- 假设：冻结path2_theme排序、持仓与风控，仅改变权重映射signal→base；验证信号强度配权/市值混合的收益与换手贡献。
- 预登记支持条件：父策略2020/2023净CAGR均不降，年換手五窗平均下降至少20%，2026为正；周频保持不变。
- 2020/2023正式参照CAGR差 -9.51pp/-8.01pp；2026 CAGR -15.00%；机制支持=False。中窗正式参照护栏失守。 当前引擎数值未达到预登记统计条件。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path2_mechanism_20261008_manual,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality,hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008,hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path3_mechanism_20261008_manual__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### 沪港通 Path4

- `hkconnect_path4_mechanism_20261008_manual`：`reject`；父策略 `hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`；正式参照 `hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`。
- 假设：冻结path4_quality_momentum排序、持仓与风控，仅改变权重映射hybrid→signal；验证信号强度配权/市值混合的收益与换手贡献。
- 预登记支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- 2020/2023正式参照CAGR差 -0.01pp/-2.45pp；2026 CAGR -12.82%；机制支持=False。相对正式参照有部分收益/防守增量，尚未确认全部预登记条件。 当前引擎数值未达到预登记统计条件。 统计条件原可进入观察位，但资金验收未通过，不保留观察资格。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path2_mechanism_20261008_manual,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality,hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008,hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path4_mechanism_20261008_manual__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### 沪港通 Path5

- `hkconnect_path5_mechanism_20261008_manual`：`reject`；父策略 `hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`；正式参照 `hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`。
- 假设：冻结回踩信号、32持仓和风险，仅将单票容量上限设为1/32；原32×1.2%=38.4%最高投入，验证低仓位是否掩盖信号而非继续调持仓。
- 预登记支持条件：先核实实际平均投入提高至少10pp；父策略2020/2023净CAGR均增至少1pp且2026转正才支持收益机制，护栏仍必须通过。
- 2020/2023正式参照CAGR差 +4.27pp/+4.54pp；2026 CAGR -17.93%；机制支持=False。中窗正式参照护栏失守。 当前引擎数值未达到预登记统计条件。 放宽cap后部分持仓记录合计超过100%，资金约束/记录口径待审计，结果仅作诊断，禁止晋级。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path2_mechanism_20261008_manual,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality,hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008,hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path5_mechanism_20261008_manual__since_2023_01/weights_history.csv'"'"'); print(d.groupby('"'"'date'"'"').weight.sum().describe()); print(d.groupby('"'"'date'"'"').target_total_exposure.first().describe())'
```

### 沪港通 Path6

- `hkconnect_path6_mechanism_20261008_manual`：`reject`；父策略 `hkconnect_path6_lowvol_hold18_20261008`；正式参照 `hkconnect_path6_lowvol_hold18_20261008`。
- 假设：冻结path6_large_liquid_core排序、持仓与风控，仅改变权重映射hybrid→base；验证信号强度配权/市值混合的收益与换手贡献。
- 预登记支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- 2020/2023正式参照CAGR差 -0.56pp/-1.02pp；2026 CAGR +2.37%；机制支持=False。未形成可验证的关键指标增量。 当前引擎数值未达到预登记统计条件。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path2_mechanism_20261008_manual,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality,hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008,hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path6_mechanism_20261008_manual__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### 沪港通 Path7

- `hkconnect_path7_mechanism_20261008_manual`：`reject`；父策略 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`；正式参照 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`。
- 假设：冻结path7_barbell_quality_growth排序、持仓与风控，仅改变权重映射hybrid→signal；验证信号强度配权/市值混合的收益与换手贡献。
- 预登记支持条件：父策略2020/2023净CAGR均不降，至少一窗提高1pp或回撤改善2pp；成本不升，2026为正；否则仅诊断/拒绝。
- 2020/2023正式参照CAGR差 +0.31pp/-0.59pp；2026 CAGR -7.40%；机制支持=False。相对正式参照有部分收益/防守增量，尚未确认全部预登记条件。 当前引擎数值未达到预登记统计条件。 统计条件原可进入观察位，但资金验收未通过，不保留观察资格。 候选或参照有超过100%的持仓记录；已局部复现调仓缓冲造成负现金，机制结论未验证，收益差仅诊断，停止晋级与扩参，先修复/审计资金约束。
- 正式window winner/robust/tracked均未改变；停止该消融方向扩参；保留历史；不加入自动active。

实跑命令（含该市场所有候选、父策略和正式参照；五窗）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path2_mechanism_20261008_manual,hkconnect_path2_theme_entry10_20261006,hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003,hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality,hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907,hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008,hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7
```

下一轮第一条命令（诊断/补缺，不冒充新增回测）：

```sh
.venv/bin/python -c 'import pandas as pd; d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path7_mechanism_20261008_manual__since_2023_01/turnover.csv'"'"'); print(d.groupby(d.get('"'"'event_type'"'"',pd.Series('"'"'rebalance'"'"',index=d.index))).two_way_turnover.agg(['"'"'count'"'"','"'"'sum'"'"','"'"'mean'"'"']))'
```

### 反思与下一轮决策

**资金约束验收阻断**：11/12个实验的候选或参照出现股票持仓合计超过100%。最小复现：原A/B各50%，目标A49.5%/B48%/C2.5%，目标合计100%；A的小卖单被冻结、B卖单与C买单执行后，现金=-0.5%、股票敞口100.5%。锁定不可交易持仓的另一组最小用例没有出现负现金，因此不能把原因一概归到停牌。共享 `compute_rebalance_trades` 的调仓缓冲/买入预算边界已有确定性复现，历史各次发生原因仍需回放；受影响的收益差只是当前引擎输出，机制判断无法确认，不作晋级。根因修复未在本轮完成，下一轮优先级提升为资金约束修复与同配置复跑。

1. **上轮决策落实**：继续完成guard指定20-ID补缺；当前正式HK6 hold18身份保留。旧balanced复跑、买入分位/持仓相邻扩参取消，A股5/HK7转为机制消融；12条path均有审查、候选或事件复核、诊断首命令。A6/HK8为已存在扩展线，本轮未扩大它们的实验范围。Path5只复核60D成熟度，未冻结新篮子。

2. **本轮认知变化**：A股多因子此前与正式robust同时改变了信号、持仓和风控，跨形态失败不能单独归因于多因子。本轮分别保留正式形态换信号、保留旧quality_tilt换风控；父策略机制支持与正式参照晋级分开判断，详见两张A1卡。当前引擎模拟中，HK Path5提高上限使目标配置显著增加，2020/2023 CAGR改善约4.27/4.54pp，但2026下降10.57pp且仍为负；该数值不支持“补足仓位即可修复策略”，且资金阻断使机制结论仍无法确认。HK Path3改权重只降低约4%换手，2020/2023 CAGR却下降9.51/8.01pp；这是换股来源诊断线索，受影响结果仍需修复后确认。

3. **失败与自我检查**：HK5的替代解释是增加风险敞口放大了原信号的阶段性亏损；另一个解释是不可交易持仓/费用预算/负现金或权重记录问题。部分满额实验持仓合计超过100%，因此只作诊断并禁止晋级；调仓缓冲造成负现金已通过最小用例复现，历史各次超额持仓的具体原因仍需用恒等式与不可卖持仓回放区分。HK3两形态在since_2023_01的196个调仓事件中均有194次实际交易，改权重未减少交易事件；支持继续做换股来源归因，而不是断言信号整体无效。HK窗口“存在覆盖”不能等同于同截止日覆盖：本地HK共有101个策略具备10/08同端点五窗，本轮14个候选/参照均按同端点严格核对，不从全集pass推出全集最新。

4. **停止与改变**：停止A1成长/行业因子小权重搜索，以及HK3/4/5/7的相邻持仓、谨慎仓位扩参。保留基于证据的单项机制消融；不因弱参照改善或少数短窗强收益晋级。12个诊断ID保留可重放定义和历史；7个HK ID明确归档，不扩大已超cap的自动active池。已有A4/HK4/HK5弱robust仍为观察位，不是强稳定winner。外部kb-web首次接入pilot已做过，本轮无新外部数据假设，复用哈希/PIT已验证的9/16快照，0新增调用/credits。

5. **下一轮具体决策**：A股与HK首先修复/审计共享调仓缓冲造成的负现金边界，现金>=0、股票敞口<=100%、资金恒等式与费用预算的回归验收通过后，以本轮冻结配置、同截止日重跑受影响候选。之后A股再用两张core_multifactor卡做股票/风险阶段收益归因，HK重点复核Path5满额容量机制。修复前停止放宽cap、因子小调和晋级；不改信号来掩盖引擎错误。需要实现的修复明确作为下一轮任务，不把尚未修复的引擎写成可执行新策略ID。支持条件、停止规则、现有ID及可执行诊断命令在本轮scorecard.next_priority中；下一轮必须报告执行/取消原因，不能重新照抄旧扩参命令。

**日期选择与发布反思**：本轮依guard.as_of选择A股9/30作为冻结历史实验端点，但原始缓存已到10/08；两者用途不同。不能把9/30同日对照完成误写成最新估值刷新完成。下轮开始须分别解析研究冻结端点与正式发布所需raw cache截止日；资金修复通过后，使用显式受影响/发布ID增量补到10/08，再重试导出，不为过门禁降低freshness规则。

同步：weighted/HK artifacts已执行；live和public均实际尝试但被StaleStrategyValuationError阻断（A股正式估值9/30落后raw cache10/08），本轮没有完成正式发布更新，未绕过门禁。正式角色与既有受保护dirty文件已保留，6份较新父策略回测目录已恢复，防止9/30诊断覆盖10/08正式产物。日志在本轮执行目录，错误概要已持久化到scorecard.publication。
