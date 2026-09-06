# 2026-09-07 多路径策略研究记录

新参数证券候选14个（A股7 / HK7），事件篮子成熟窗确认1个；判定：{'promote': 3, 'reject': 7, 'keep_watch': 4, 'archive': 1}。13个旧证券候选和1个成熟事件篮子退出active。
市场端点2026-09-04。Path2 coverage 718 → 698/832；该路径延后晋级。其余目标路径均有review、候选设计、实跑与下一轮命令。

完整指标：`results/research/a_share/research_iteration_scorecard_20260907.json`；实际批次：`results/research/a_share/research_iteration_manifest_20260907.json`。

## A股 Path1（主线与 core_multifactor）

### 上一轮候选与结果摘要

- `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr,since_2020_01:sharpe_ratio,since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.1730/0.1222，2023=-0.1189/0.0755，2026 CAGR=-0.0357，不支持晋级。
- `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure_buffered_asym13`：`promote`。未触发中窗护栏；2020 CAGR/Sharpe/MaxDD差分=-0.0117/-0.0273/0.0070，2023=0.0135/0.0172/0.0012，具备晋级资格但须服从artifact相邻验证。

### 本轮候选 ID 与命令

- 主线 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`：`promote`。假设：相对risk20将晋升持仓7只增至8只，检验集中度下降能否改善2023/2026回撤并保住中窗收益。2020 CAGR/MaxDD差分 3.28/-1.56pp，2023差分 3.44/2.19pp；2026 CAGR 23.87%，年均换手 7.04x。未触发中窗护栏；关键风险收益改善且五窗正收益，具备正式相邻验证资格。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：True，tracked身份变化：True。
- core_multifactor 子段 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_quality_rebalance_risk09_v20260907`：`reject`。假设：相对trend-quality risk09把质量权重10个百分点移至六个月动量，检验中窗CAGR恢复且不扩大回撤。2020 CAGR/MaxDD差分 -18.33/7.53pp，2023差分 -7.73/9.47pp；2026 CAGR -9.92%，年均换手 5.96x。命中稳定性护栏：since_2020_01:cagr,since_2020_01:sharpe_ratio,since_2023_01:cagr；假设不支持晋级。收益风险退化或成本上升且年内仍负，停止同形扩参。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_quality_rebalance_risk09_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`core_explore_80_20_total_mv_winner_core__aggr_10_90_fast_ramp_cash_off`。当前端点最差收益为负或近期确认触发中窗护栏，从fast-pass及direction group移出；保留定义与历史快照证据：`{"min_cagr": -0.1690994, "worst_maxdd": -0.36096563, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。
- evict/archive：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk08_reconfirm`。当前端点最差收益为负或近期确认触发中窗护栏，从fast-pass及direction group移出；保留定义与历史快照证据：`{"min_cagr": -0.02976009, "worst_maxdd": -0.34451455, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`core_multifactor_coverage`。下一轮第一条可执行命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `core_multifactor_coverage`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk09_reconfirm`；`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm`。
- `signal_quality`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk09_reconfirm`；`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm`。
- `satellite_risk_cost`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`；`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- `holding_shape`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`；`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- `weekly_exposure_path`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure_buffered_asym13`；`core_explore_80_20_total_mv_winner_core__share_12_88_hold_4_6__port_weekly_exposure_buffered_asym13`。

## A股 Path2（growth_elastic）

### 上一轮候选与结果摘要

- `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr,since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0444/-0.0152，2023=-0.0340/0.0801，2026 CAGR=-0.2028，不支持晋级。
- `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap16_cost_guard_v62_underrepresented_lowturn`：`reject`。2020/2023稳定性护栏命中since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0179/0.0106，2023=-0.0376/0.0097，2026 CAGR=-0.2250，不支持晋级。

### 本轮候选 ID 与命令

- 候选 `core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_monthly_risk20_exit40_cap14_v20260907`：`reject`。假设：相对v63将双周调仓改为月频，检验降换手是否改善2020/2023净收益；coverage未齐只能观察或淘汰。2020 CAGR/MaxDD差分 0.21/-6.10pp，2023差分 -10.62/-0.03pp；2026 CAGR -24.22%，年均换手 7.77x。命中稳定性护栏：since_2020_01:max_drawdown,since_2023_01:cagr,since_2023_01:sharpe_ratio；假设不支持晋级。收益风险退化或成本上升且年内仍负，停止同形扩参。Path2 coverage仍阻塞，本轮禁止promote。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_monthly_risk20_exit40_cap14_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- 本路径没有额外 evict；本轮拒绝候选停止同形扩参，保留历史结果。

### 下一轮 focus 提示

- guard focus：`medium_cycle_growth`。下一轮第一条可执行命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm75_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_reconfirm80_amt110_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_ma_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_mom_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit60_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_exit80_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_theme_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_full_risk_cap90,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_industry_trend_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95 --end-date 2026-09-04`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。
- coverage：718 → 698/832，剩余35个精确批次；本轮已完成首批20个四窗，未全量扫池。缺口影响Path2晋级，本轮全部禁止promote。

### Focus 候选池

- `medium_cycle_growth`：`core_explore_60_40_equal_weight_winner_core`；`core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`。
- `risk_reconfirm_sensitivity`：`core_explore_60_40_equal_weight_winner_core`；`core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`。
- `underrepresented_families`：`core_explore_60_40_equal_weight_winner_core`；`core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`。
- `capacity_and_cost_stress`：`core_explore_60_40_equal_weight_winner_core`；`core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`。

## A股 Path3（纯周频）

### 上一轮候选与结果摘要

- `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr；2020 CAGR/MaxDD差分=-0.0981/0.1081，2023=-0.0004/0.2250，2026 CAGR=0.3572，不支持晋级。
- `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`：`keep_watch`。未触发中窗硬护栏，但跨窗仍有权衡；2020 CAGR/MaxDD差分=-0.0291/0.0908，2023=-0.0077/0.1621，2026 CAGR=0.3613，继续观察。

### 本轮候选 ID 与命令

- 候选 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit94_risk14_v20260907_weekly`：`keep_watch`。假设：相对v7把单票上限46%放至50%、每周换手上限4%放至5%，检验修复2025收益同时保住2020/2023风险优势。2020 CAGR/MaxDD差分 -0.25/0.01pp，2023差分 -0.51/-0.01pp；2026 CAGR 28.63%，年均换手 1.65x。未触发中窗护栏；中窗改善或风险边界可观察，但短窗、绝对收益或成本未同时改善。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit94_risk14_v20260907_weekly`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly`。长期防守形态损失中窗收益，停止重复确认，腾出v8风险收益平衡试验名额；保留历史快照证据：`{"min_cagr": -0.01801208, "worst_maxdd": -0.24411175, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`turnover_reduction`。下一轮第一条可执行命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit94_risk14_v20260907_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `turnover_reduction`：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit94_risk14_v20260907_weekly`；`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- `weekly_exit_buffer`：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit94_risk14_v20260907_weekly`；`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- `risk_downshift`：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit94_risk14_v20260907_weekly`；`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- `cost_stress`：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit94_risk14_v20260907_weekly`；`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

## A股 Path4（emergent theme discovery）

### 上一轮候选与结果摘要

- `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`：`reject`。2020/2023稳定性护栏命中since_2020_01:max_drawdown,since_2023_01:max_drawdown；2020 CAGR/MaxDD差分=0.0211/-0.0814，2023=-0.0001/-0.1058，2026 CAGR=-0.1286，不支持晋级。
- `core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`：`keep_watch`。未触发中窗硬护栏，但跨窗仍有权衡；2020 CAGR/MaxDD差分=0.0000/0.0000，2023=0.0000/0.0000，2026 CAGR=-0.0601，继续观察。

### 本轮候选 ID 与命令

- 候选 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit68_v20260907`：`reject`。假设：相对capacity-v2把出场阈值72%收紧至68%，检验强主题衰减时提前退出能否修复2026损失并保持容量与中窗稳定。2020 CAGR/MaxDD差分 2.08/-12.23pp，2023差分 -0.20/-14.60pp；2026 CAGR -13.42%，年均换手 5.12x。命中稳定性护栏：since_2020_01:max_drawdown,since_2023_01:max_drawdown；假设不支持晋级。收益风险退化或成本上升且年内仍负，停止同形扩参。从主题active列表移除新变体。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 候选 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit68_v20260907`：`reject`。假设：相对capacity-v2把出场阈值72%收紧至68%，检验强主题衰减时提前退出能否修复2026损失并保持容量与中窗稳定。五窗口CAGR均低于capacity-v2 robust，2026为-16.21%、换手各窗更高，假设不支持；从主题active列表移除新变体。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 候选 `core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit68_v20260907`：`reject`。假设：相对capacity-v2把出场阈值72%收紧至68%，检验强主题衰减时提前退出能否修复2026损失并保持容量与中窗稳定。五窗口CAGR/Sharpe/MaxDD/turnover与capacity-v2参考完全相同；出场阈值改动未改变结果且2026仍为-3.79%。无新增竞争优势，拒绝无效重复并从主题active列表移除。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit68_v20260907,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit68_v20260907,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit68_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn`。signal30/leader80形态最差2026收益退化，三底座从主题active集合移出；用exit68容量实验替换证据：`{"min_cagr": -0.26555217, "worst_maxdd": -0.36489352, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。
- evict/archive：`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn`。移出失败signal30/leader80家族：代表底座年内收益-26.56%，本底座当前端点comparison未刷新；保留历史快照，停止同形扩参。证据：`{"min_cagr": null, "worst_maxdd": null, "windows": [], "latest_sample_end": "2026-08-25", "historical_min_cagr": -0.20519732}`。
- evict/archive：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn`。移出失败signal30/leader80家族：代表底座年内收益-26.56%，本底座当前端点comparison未刷新；保留历史快照，停止同形扩参。证据：`{"min_cagr": null, "worst_maxdd": null, "windows": [], "latest_sample_end": "2026-08-07", "historical_min_cagr": -0.16194434}`。
- 路由严格为 emergent_theme，未加入Path2池、未使用人工主题或ETF；第一阶段仍是实验/观察口径。

### 下一轮 focus 提示

- guard focus：`emergent_theme_coverage`。下一轮第一条可执行命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `emergent_theme_coverage`：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`；`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- `theme_signal_quality`：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`；`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- `theme_risk_control`：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`；`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- `theme_capacity_cost`：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`；`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

## A股 Path5（event knowledge graph）

### 上一轮候选与结果摘要

- `ai_datacenter_power_grid_202607_v0`：`keep_watch`。20日收益保持正值，但40/60日仍不足且缺连续风险指标，不能进入Path1-4 winner/robust。

### 本轮候选 ID 与命令

- 候选 `ai_glasses_edge_terminal_20260424_v0`：`archive`。假设：检验AI眼镜冻结篮子的20/40日超额收益能否延续到60日；同时与事件日前冻结Path4持仓做相同窗口/成本比较。。20/40/60D毛收益21.80%/26.82%/0.11%；60D扣交易费后约0%、最大回撤23.54%，40日收益大幅回吐，成熟窗未验证持续性。停止active刷新，保留审计与历史结果。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 实跑事件命令：`.venv/bin/python scripts/event_theme_backtest_entry.py --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --basket-id ai_glasses_edge_terminal_20260424_v0 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2 --path4-sample-tag since_2026_01 --output-json results/research/a_share/event_theme_backtest_entry_ai_glasses_edge_terminal_20260424_v0_path4_capacity_v2_20260907_mature.json`。审计 source_audited、冻结；20/40/60D完整。连续五窗风险指标不适用，另提供同日、同成本的冻结Path4持仓对照；不是动态Path4实盘收益。
- 本路径没有额外 evict；本轮拒绝候选停止同形扩参，保留历史结果。
- AI眼镜篮子以 registry archive_only=True 退出active；power-grid继续保留，40/60D尚待成熟。

### 下一轮 focus 提示

- guard focus：`event_basket_registry`。下一轮第一条可执行命令：`.venv/bin/python scripts/event_theme_backtest_entry.py --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --basket-id ai_datacenter_power_grid_202607_v0 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2 --path4-sample-tag since_2026_01 --output-json results/research/a_share/event_theme_backtest_entry_ai_datacenter_power_grid_202607_v0_path4_capacity_v2_next_mature.json`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。
- 未回测新40/60D power-grid长窗原因：本端点仍只有34个后续交易日；不刷新已归档AI眼镜。继续比较同一事件假设的成熟窗与5/10/20D风险。

### Focus 候选池

- `event_basket_registry`：`ai_datacenter_power_grid_202607_v0 / horizons=20,40,60`；`ai_datacenter_power_grid_202607_v0 / horizons=5,10,20`。
- `frozen_candidate_audit`：`ai_datacenter_power_grid_202607_v0 / horizons=20,40,60`；`ai_datacenter_power_grid_202607_v0 / horizons=5,10,20`。
- `event_backtest_entry`：`ai_datacenter_power_grid_202607_v0 / horizons=20,40,60`；`ai_datacenter_power_grid_202607_v0 / horizons=5,10,20`。
- `path4_comparison`：`ai_datacenter_power_grid_202607_v0 / horizons=20,40,60`；`ai_datacenter_power_grid_202607_v0 / horizons=5,10,20`。

## 沪港通 Path1

### 上一轮候选与结果摘要

- `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`：`reject`。2020/2023稳定性护栏命中since_2023_01:max_drawdown；2020 CAGR/MaxDD差分=0.0814/-0.0414，2023=0.0329/-0.0962，2026 CAGR=-0.1369，不支持晋级。
- `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32`：`reject`。2020/2023稳定性护栏命中since_2023_01:max_drawdown；2020 CAGR/MaxDD差分=0.0817/-0.0413，2023=0.0327/-0.0961，2026 CAGR=-0.1369，不支持晋级。

### 本轮候选 ID 与命令

- 候选 `hkconnect_path1_monthly_lowvol_weekly_overlay_risk35_caution80_v20260907`：`reject`。假设：相对低波soft-exit32降低熊市与谨慎仓位，检验中窗回撤与2026风险修复。2020 CAGR/MaxDD差分 6.15/0.26pp，2023差分 5.86/-5.22pp；2026 CAGR -3.36%，年均换手 4.09x。命中稳定性护栏：since_2023_01:max_drawdown；假设不支持晋级。收益风险退化或成本上升且年内仍负，停止同形扩参。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_lowvol_weekly_overlay_risk35_caution80_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32`。当前端点非winner/robust集合内minCAGR最弱，退出active避免候选池净扩张；保留定义与历史结果证据：`{"min_cagr": -0.13692317, "worst_maxdd": -0.22966077, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`monthly_weekly_overlay`。下一轮第一条可执行命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_lowvol,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `monthly_weekly_overlay`：`hkconnect_path1_biweekly_lowvol`；`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`。
- `biweekly_buffer`：`hkconnect_path1_biweekly_lowvol`；`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`。
- `risk_overlay_cost`：`hkconnect_path1_biweekly_lowvol`；`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`。

## 沪港通 Path2

### 上一轮候选与结果摘要

- `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v44_high_return_monthly`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr,since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0405/-0.0056，2023=-0.0777/-0.0056，2026 CAGR=-0.2011，不支持晋级。
- `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v43_high_return_monthly`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr,since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0371/0.0008，2023=-0.0664/0.0008，2026 CAGR=-0.1916，不支持晋级。

### 本轮候选 ID 与命令

- 候选 `hkconnect_path2_high_return_monthly_quality_breadth18_v20260907`：`keep_watch`。假设：相对v27扩大质量流动性入选与持仓宽度，检验降低单票依赖能否修复2026且保住中窗收益。2020 CAGR/MaxDD差分 5.43/1.99pp，2023差分 6.36/1.99pp；2026 CAGR -10.03%，年均换手 3.83x。未触发中窗护栏；中窗改善或风险边界可观察，但短窗、绝对收益或成本未同时改善。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_high_return_monthly_quality_breadth18_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v44_high_return_monthly`。当前端点非winner/robust集合内minCAGR最弱，退出active避免候选池净扩张；保留定义与历史结果证据：`{"min_cagr": -0.20105818, "worst_maxdd": -0.24799754, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`high_return_monthly`。下一轮第一条可执行命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_high_return_monthly_quality_breadth18_v20260907,hkconnect_path2_theme_fast_monthly`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `high_return_monthly`：`hkconnect_path2_high_return_monthly_quality_breadth18_v20260907`；`hkconnect_path2_theme_fast_monthly`。
- `biweekly_breakout`：`hkconnect_path2_high_return_monthly_quality_breadth18_v20260907`；`hkconnect_path2_theme_fast_monthly`。
- `elasticity_cost_control`：`hkconnect_path2_high_return_monthly_quality_breadth18_v20260907`；`hkconnect_path2_theme_fast_monthly`。

## 沪港通 Path3

### 上一轮候选与结果摘要

- `hkconnect_path3_theme_fast_weekly_defensive_turnover3_exit58_v16_stable_blend`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr,since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0897/0.2530，2023=-0.1296/0.1315，2026 CAGR=-0.0818，不支持晋级。
- `hkconnect_path3_theme_fast_weekly_defensive_turnover4_exit58_v15_stable_blend`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr,since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0742/0.2670，2023=-0.1096/0.1432，2026 CAGR=-0.0625，不支持晋级。

### 本轮候选 ID 与命令

- 候选 `hkconnect_path3_weekly_lowvol_exit46_v20260907`：`keep_watch`。假设：相对v38放宽出场阈值36%至46%，检验减少周频换手后是否保住中窗风险与2026收益。2020 CAGR/MaxDD差分 -1.14/33.00pp，2023差分 4.70/19.76pp；2026 CAGR -2.02%，年均换手 9.31x。未触发中窗护栏；中窗改善或风险边界可观察，但短窗、绝对收益或成本未同时改善。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_weekly_lowvol_exit46_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`hkconnect_path3_breakout_cashoff_weekly`。当前端点非winner/robust集合内minCAGR最弱，退出active避免候选池净扩张；保留定义与历史结果证据：`{"min_cagr": -0.22544473, "worst_maxdd": -0.63462884, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`weekly_turnover_reduction`。下一轮第一条可执行命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_weekly_lowvol_exit46_v20260907,hkconnect_path3_equal_elastic_weekly`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `weekly_turnover_reduction`：`hkconnect_path3_weekly_lowvol_exit46_v20260907`；`hkconnect_path3_equal_elastic_weekly`。
- `weekly_defensive_overlay`：`hkconnect_path3_weekly_lowvol_exit46_v20260907`；`hkconnect_path3_equal_elastic_weekly`。
- `cost_stress`：`hkconnect_path3_weekly_lowvol_exit46_v20260907`；`hkconnect_path3_equal_elastic_weekly`。

## 沪港通 Path4（quality / liquidity momentum）

### 上一轮候选与结果摘要

- `hkconnect_path4_quality_momentum_monthly_v51_quality_balance`：`keep_watch`。未触发中窗硬护栏，但跨窗仍有权衡；2020 CAGR/MaxDD差分=0.0293/0.0571，2023=0.0143/-0.0014，2026 CAGR=-0.0213，继续观察。
- `hkconnect_path4_quality_momentum_monthly_ytd_positive_v46_lowdraw_ytd_guard`：`reject`。2020/2023稳定性护栏命中since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0148/0.0342，2023=-0.0448/0.0032，2026 CAGR=-0.0441，不支持晋级。

### 本轮候选 ID 与命令

- 候选 `hkconnect_path4_quality_momentum_monthly_exit46_v20260907`：`keep_watch`。假设：相对v51把出场52%收紧至46%，检验更早退出能否修复2026负收益而不损害2020/2023。2020 CAGR/MaxDD差分 3.30/5.71pp，2023差分 1.72/0.20pp；2026 CAGR -2.22%，年均换手 2.45x。未触发中窗护栏；中窗改善或风险边界可观察，但短窗、绝对收益或成本未同时改善。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_exit46_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`hkconnect_path4_quality_momentum_monthly_lowvol_drawdown_v4`。当前端点非winner/robust集合内minCAGR最弱，退出active避免候选池净扩张；保留定义与历史结果证据：`{"min_cagr": -0.13080938, "worst_maxdd": -0.2083258, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`quality_momentum`。下一轮第一条可执行命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_exit46_v20260907,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `quality_momentum`：`hkconnect_path4_quality_momentum_monthly_exit46_v20260907`；`hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`。
- `liquidity_momentum`：`hkconnect_path4_quality_momentum_monthly_exit46_v20260907`；`hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`。
- `ytd_guard`：`hkconnect_path4_quality_momentum_monthly_exit46_v20260907`；`hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`。

## 沪港通 Path5（breakout retest / pullback continuation）

### 上一轮候选与结果摘要

- `hkconnect_path5_pullback_continuation_monthly_quality_retest_v36_lowturn_pullback_definition`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr,since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0350/0.0756，2023=-0.0414/0.0756，2026 CAGR=0.0000，不支持晋级。
- `hkconnect_path5_pullback_continuation_biweekly_v40_definition_balance`：`reject`。2020/2023稳定性护栏命中since_2020_01:max_drawdown,since_2023_01:max_drawdown；2020 CAGR/MaxDD差分=0.0956/-0.1387，2023=0.0517/-0.1387，2026 CAGR=-0.2257，不支持晋级。

### 本轮候选 ID 与命令

- 候选 `hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`：`reject`。假设：相对v35保持信号仓位不变改双周执行，检验回踩信号及时性是否改善正收益覆盖且不会造成成本爆表。2020 CAGR/MaxDD差分 0.09/-1.33pp，2023差分 -0.07/-0.03pp；2026 CAGR -6.32%，年均换手 1.87x。未触发中窗护栏；收益风险退化或成本上升且年内仍负，停止同形扩参。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`hkconnect_path5_pullback_continuation_monthly_ytd_repair_v2`。当前端点非winner/robust集合内minCAGR最弱，退出active避免候选池净扩张；保留定义与历史结果证据：`{"min_cagr": -0.28978985, "worst_maxdd": -0.27292596, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`pullback_definition`。下一轮第一条可执行命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_pullback_continuation_monthly_quality_retest_v35_ytd_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v34_pullback_definition_rewrite`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `pullback_definition`：`hkconnect_path5_pullback_continuation_monthly_quality_retest_v35_ytd_repair`；`hkconnect_path5_pullback_continuation_monthly_quality_retest_v34_pullback_definition_rewrite`。
- `retest_confirmation`：`hkconnect_path5_pullback_continuation_monthly_quality_retest_v35_ytd_repair`；`hkconnect_path5_pullback_continuation_monthly_quality_retest_v34_pullback_definition_rewrite`。
- `pause_or_redesign`：`hkconnect_path5_pullback_continuation_monthly_quality_retest_v35_ytd_repair`；`hkconnect_path5_pullback_continuation_monthly_quality_retest_v34_pullback_definition_rewrite`。

## 沪港通 Path6（large liquid core）

### 上一轮候选与结果摘要

- `hkconnect_path6_large_liquid_core_monthly_v46_return_balance`：`promote`。未触发中窗护栏；2020 CAGR/Sharpe/MaxDD差分=-0.0203/0.0659/0.0335，2023=-0.0295/0.0281/0.0017，具备晋级资格但须服从artifact相邻验证。
- `hkconnect_path6_lowvol_liquid_biweekly_v47_return_balance`：`reject`。2020/2023稳定性护栏命中since_2020_01:cagr,since_2023_01:cagr；2020 CAGR/MaxDD差分=-0.0376/0.0061，2023=-0.0490/-0.0179，2026 CAGR=0.0163，不支持晋级。

### 本轮候选 ID 与命令

- 候选 `hkconnect_path6_large_liquid_core_monthly_breadth24_v20260907`：`promote`。假设：相对monthly-smoke把持仓18只扩至24只、单票10%降至7.5%，检验降低集中风险且保住多窗正收益。2020 CAGR/MaxDD差分 1.30/0.87pp，2023差分 0.32/-0.37pp；2026 CAGR 5.66%，年均换手 2.11x。未触发中窗护栏；关键风险收益改善且五窗正收益，具备正式相邻验证资格。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_breadth24_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_lowturn_v11`。当前端点非winner/robust集合内minCAGR最弱，退出active避免候选池净扩张；保留定义与历史结果证据：`{"min_cagr": 0.04709397, "worst_maxdd": -0.23834911, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`large_liquid_core`。下一轮第一条可执行命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_breadth24_v20260907,hkconnect_path6_lowvol_liquid_biweekly_smoke`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `large_liquid_core`：`hkconnect_path6_large_liquid_core_monthly_breadth24_v20260907`；`hkconnect_path6_lowvol_liquid_biweekly_smoke`。
- `lowvol_liquid_core`：`hkconnect_path6_large_liquid_core_monthly_breadth24_v20260907`；`hkconnect_path6_lowvol_liquid_biweekly_smoke`。
- `capacity_cost`：`hkconnect_path6_large_liquid_core_monthly_breadth24_v20260907`；`hkconnect_path6_lowvol_liquid_biweekly_smoke`。

## 沪港通 Path7（barbell quality growth）

### 上一轮候选与结果摘要

- `hkconnect_path7_barbell_quality_growth_biweekly_v44_sleeve_balance`：`keep_watch`。未触发中窗硬护栏，但跨窗仍有权衡；2020 CAGR/MaxDD差分=-0.0016/-0.0042，2023=0.0081/-0.0000，2026 CAGR=0.0085，继续观察。
- `hkconnect_path7_barbell_quality_growth_biweekly_v45_quality_balance`：`reject`。虽未触发中窗硬护栏，但2026 CAGR=-0.0499、换手=10.64，短窗收益或成本不可接受，判定reject。

### 本轮候选 ID 与命令

- 候选 `hkconnect_path7_barbell_biweekly_risk15_caution50_v20260907`：`promote`。假设：相对v9把熊市/谨慎仓位20%/58%降至15%/50%，检验2026收益风险是否改善且不中断双袖中窗收益。2020 CAGR/MaxDD差分 -0.05/-1.12pp，2023差分 0.49/1.09pp；2026 CAGR 8.36%，年均换手 5.86x。未触发中窗护栏；关键风险收益改善且五窗正收益，具备正式相邻验证资格。
  - 五窗口同指标详情：`results/research/a_share/research_iteration_scorecard_20260907.json`；window winner/robust变化：False，tracked身份变化：False。
- 五窗实跑批次保存在 `research_iteration_manifest_20260907.json`；本路径等价增量重现命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_biweekly_risk15_caution50_v20260907`。覆盖 since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01。
- evict/archive：`hkconnect_path7_barbell_quality_growth_biweekly_core_growth_dynamic_v6`。当前端点非winner/robust集合内minCAGR最弱，退出active避免候选池净扩张；保留定义与历史结果证据：`{"min_cagr": -0.0484574, "worst_maxdd": -0.18880598, "windows": ["since_2017_01", "since_2020_01", "since_2023_01", "since_2025_01", "since_2026_01"]}`。

### 下一轮 focus 提示

- guard focus：`barbell_sleeve_structure`。下一轮第一条可执行命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-04 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_biweekly_risk15_caution50_v20260907,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。
- 本轮此路径已经实跑；没有把同步、coverage或candidate-pass算作新增实验。其余候选未跑原因：Path2阻塞场景将证券新参数预算降至14个，优先满足12条path的竞争动作；下一轮端点推进或上述观察条件满足后继续。

### Focus 候选池

- `barbell_sleeve_structure`：`hkconnect_path7_barbell_biweekly_risk15_caution50_v20260907`；`hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。
- `biweekly_barbell`：`hkconnect_path7_barbell_biweekly_risk15_caution50_v20260907`；`hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。
- `turnover_control`：`hkconnect_path7_barbell_biweekly_risk15_caution50_v20260907`；`hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。
