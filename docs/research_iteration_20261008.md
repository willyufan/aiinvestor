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
