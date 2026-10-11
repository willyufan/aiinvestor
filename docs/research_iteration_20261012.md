# 2026-10-12 十二路径研究：持有保护与固定目标集合配权

## 开轮反思 2026-10-12T01:07:14.161161+08:00

读取10/08、10/09、10/10反思、对应scorecard、账本和九plan。上轮Path2传导审计已闭环，门槛移除与hybrid收益假设均未满足，取消相邻阈值/配权比例搜索。10/10承诺的A3持有保护消融与HK2固定父目标集合runner未执行，原因是明确留待本轮的实现/归因任务；本轮继续。资金错误已修复，不重新把资金问题当信号解释。

初始guard截止10/09，Path2唯一block缺736/828。相比10/10的787/828减少51是期间更新，非本轮贡献。严格执行首20-ID四窗批次；Path2正式身份冻结。交易周末缓存截止仍10/09，本轮冻结该日做机制归因，不把同端点复跑数量当新信息。

A股问题：移除六周最短持有保护的防守收益，来自降低风险敞口还是减少交易成本？只确认已注册hold_protection_ablation与本轮实际robust五窗，并读取gross/net、risk_stage和实际敞口。支持条件：2020/2023净CAGR损失≤3pp，MaxDD改善≥3pp且Sharpe下降≤0.3；近窗仍负则最多keep_watch。若成本不能解释净收益损失，停止hold相邻搜索，转风险阶段贡献。

HK问题：完全base配权中窗收益改善是否由股票集合路径变化造成？实现隔离runner冻结父entry10每个信号日原始目标集合，仅重算集合内base权重，不改变父目标总敞口、PIT/风控/成本。验收同信号日目标cohort完全一致、单票cap、资金与双边费用；实际执行持仓因交易缓冲可能不同，不能宣称实际持仓相同。参照为entry10及本轮正式robust，五窗同10/09。支持2020/2023各增1pp、2026不落后2pp；任一中窗CAGR降3pp/MaxDD恶化5pp/Sharpe降0.3或收益支持失败即停止配权族。

目标预算因coverage降到12–18；先完成两项最高证据承诺，再依据阶段归因决定其它实验，停止规则优先，不凑已否定参数。未达数量须记录真实原因，不能声称coverage耗尽全天。kb-web首次隔离pilot已执行（integration记录）；本轮无外部字段假设，复用快照校验，0新调用，不绕过MCP。

## 十二路径巡检、候选与下一轮命令

## 2026-10-12T01:22:55.151898+08:00 A股 Path1（主线 / core_multifactor）

### 上一轮候选与结果摘要

`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual` reject；`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual` reject。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：主线冻结buffered/buffered_asym13检查风险阶段目标与实投；core_multifactor冻结shape_control/risk_graft检查2020损失来自年度/股票贡献还是形态风控。停止小因子权重扩参。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_quality_tilt --comparison-csv /private/tmp/aiinvestor_next_ashare_path1.csv
```

主线：三个weekly_exposure优先形态仅复核既有记录，asym仍无比较行；不声称同日三形态竞争。core_multifactor：guard64/64仅窗口存在，非全组本轮重算；读取代码实际direction group，维持停止小因子权重扩参。

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

主线冻结buffered/buffered_asym13检查风险阶段目标与实投；core_multifactor冻结shape_control/risk_graft检查2020损失来自年度/股票贡献还是形态风控。停止小因子权重扩参。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907'"'"'); print(pd.read_csv('"'"'results/backtests/a_share/core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907__since_2023_01/annual_returns.csv'"'"').to_string(index=False))'
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `core_multifactor_coverage`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `signal_quality`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `satellite_risk_cost`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `holding_shape`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 A股 Path2

### 上一轮候选与结果摘要

`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009` reject；`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_gate_mom61_off_20261010` reject。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：v63/mom61与gate-off传导已闭环，停止排序、门槛、cap、surge相邻扩参；只补精确缺口并保留underrepresented池。

本轮首20-ID四窗补缺（辅助，不计新策略；固定截止10/09）：

```sh
.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom1_core_6_1_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap16_cost_guard_v62_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk28_exit46_cap24_cost_guard_v28,core_explore_70_30_equal_weight_winner_core__aggr_04_96_prom1_core_6_1_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard0_fast,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard50,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk28_exit48_cap28_cost_guard_v39_capacity_stress,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality,core_explore_70_30_equal_weight_winner_core__aggr_08_92_prom6_core_6_1,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100 --end-date 2026-10-09
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

v63/mom61与gate-off传导已闭环，停止排序、门槛、cap、surge相邻扩参；只补精确缺口并保留underrepresented池。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_biweekly,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm80,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp70,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp85,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_risk50_cap100,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_full_risk_cap100,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_theme_cash_off_and_cap100,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_industry_trend_cash_off_and_cap100,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_cash_off_and_cap90,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_3_1_cash_off_and_cap90,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_3_1_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_3_1_cash_off_and_risk50_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_3_1_full_risk_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap90,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap90_biweekly,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95,core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_biweekly --end-date 2026-10-09
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `medium_cycle_growth`：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`、`core_explore_70_30_equal_weight_winner_core`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_gate_mom61_off_20261010`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `risk_reconfirm_sensitivity`：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`、`core_explore_70_30_equal_weight_winner_core`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_gate_mom61_off_20261010`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `underrepresented_families`：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`、`core_explore_70_30_equal_weight_winner_core`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_gate_mom61_off_20261010`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `capacity_and_cost_stress`：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`、`core_explore_70_30_equal_weight_winner_core`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_gate_mom61_off_20261010`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 A股 Path3

### 上一轮候选与结果摘要

`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly` keep_watch。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly`：hold_protection_parameter_confirmation，五窗同10/09，keep_watch。中窗CAGR损失2.62/2.53pp；2020 MaxDD改善6.22pp、2023恶化4.50pp。虽未触发硬稳定性阈值且2026强，但不支持跨窗防守假设，keep_watch，停止相邻hold搜索。成本节省不足以解释收益差。

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly --comparison-csv /private/tmp/aiinvestor-20261012/ashare_path3.csv
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

冻结hold0/hold6比较共同风险状态gross/net对数贡献和股票实投；停止相邻hold搜索。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python scripts/strategy_phase_attribution.py --backtest-root results/backtests/a_share --candidate-id core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly --reference-id core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --end-date 2026-10-09 --output-json results/research/a_share/research_iteration_ashare_attribution_next.json
```

最高优先实现任务、验收与证伪条件：见本轮scorecard.next_priority及研究报告；先完成逐日实际股票贡献重构，不把不存在的策略ID写成执行命令。

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `turnover_reduction`：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `weekly_exit_buffer`：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `risk_downshift`：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `cost_stress`：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 A股 Path4（emergent theme discovery）

### 上一轮候选与结果摘要

`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual` reject。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：冻结leader_gate_ablation与当前robust，按年度领先股票贡献和单票集中度检查theme_signal_quality；不因低敞口直接放大cap。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiinvestor_next_ashare_path4.csv
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

冻结leader_gate_ablation与当前robust，按年度领先股票贡献和单票集中度检查theme_signal_quality；不因低敞口直接放大cap。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn'"'"'); print(pd.read_csv('"'"'results/backtests/a_share/core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn__since_2023_01/annual_returns.csv'"'"').to_string(index=False))'
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `emergent_theme_coverage`：`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `theme_signal_quality`：`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `theme_risk_control`：`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `theme_capacity_cost`：`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 A股 Path5（event knowledge graph）

### 上一轮候选与结果摘要

`ai_datacenter_power_grid_202607_v0` keep_watch。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：60D仍不足且gross/net与Path4比较未统一，无新来源审计，不新增未经审计篮子。

候选设计：v0冻结来源与成员；v1仅为完成来源、成本统一后的实现任务，未注册不写执行ID。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --basket-id ai_datacenter_power_grid_202607_v0 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --path4-sample-tag since_2026_01 --output-json results/research/a_share/research_iteration_event_20261012.json
```

source_audited冻结六成员篮子：20D+11.70%、40D-0.60%、60D不足；与Path4 overlap/净成本口径不足以晋级，keep_watch。

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

v0冻结来源与成员；v1仅为完成来源、成本统一后的实现任务，未注册不写执行ID。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --basket-id ai_datacenter_power_grid_202607_v0 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --path4-sample-tag since_2026_01 --output-json results/research/a_share/research_iteration_event_20261012.json
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `event_basket_registry`：`ai_datacenter_power_grid_202607_v0`、`ai_datacenter_power_grid_202607_v1`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `frozen_candidate_audit`：`ai_datacenter_power_grid_202607_v0`、`ai_datacenter_power_grid_202607_v1`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `event_backtest_entry`：`ai_datacenter_power_grid_202607_v0`、`ai_datacenter_power_grid_202607_v1`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `path4_comparison`：`ai_datacenter_power_grid_202607_v0`、`ai_datacenter_power_grid_202607_v1`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 沪港通 Path1

### 上一轮候选与结果摘要

`hkconnect_path1_mechanism_20261008_manual` keep_watch。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：冻结biweekly_lowvol与机制消融，先比较2020/2023风险阶段与成本，不扩大entry/hold。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_lowvol
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

冻结biweekly_lowvol与机制消融，先比较2020/2023风险阶段与成本，不扩大entry/hold。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path1_biweekly_lowvol'"'"'); print(pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path1_biweekly_lowvol__since_2023_01/annual_returns.csv'"'"').to_string(index=False))'
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `monthly_weekly_overlay`：`hkconnect_path1_mechanism_20261008_manual`、`hkconnect_path1_biweekly_hybrid`、`hkconnect_path1_biweekly_lowvol`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `biweekly_buffer`：`hkconnect_path1_mechanism_20261008_manual`、`hkconnect_path1_biweekly_hybrid`、`hkconnect_path1_biweekly_lowvol`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `risk_overlay_cost`：`hkconnect_path1_mechanism_20261008_manual`、`hkconnect_path1_biweekly_hybrid`、`hkconnect_path1_biweekly_lowvol`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 沪港通 Path2

### 上一轮候选与结果摘要

`hkconnect_path2_theme_hybrid_control_20261010` reject；`hkconnect_path2_mechanism_20261008_manual` reject。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

`hkconnect_path2_fixed_cohort_base_20261012`：new_fixed_cohort_weight_ablation，五窗同10/09，reject。严格固定父目标集合/目标敞口/截断前排名母体后，相对entry10中窗仅+0.33/+0.11pp，2026低1.49pp；未满足各增1pp。正式entry11中窗低1.72/1.38pp，reject，不做配权比例搜索。

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/audit_hk_fixed_cohort.py --output-dir results/research/hkconnect/experiments/fixed_cohort_20261012 --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --reference-id hkconnect_path2_theme_entry11_20261007 --only-strategy-ids hkconnect_path2_theme_entry10_20261006,hkconnect_path2_fixed_cohort_base_20261012,hkconnect_path2_theme_entry11_20261007
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

固定父目标集合base配权收益条件未满足则停止此配权族；转entry10/entry11的2026股票贡献，不以短窗增益复活权重扫描。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python scripts/strategy_phase_attribution.py --backtest-root results/research/hkconnect/experiments/fixed_cohort_20261012 --candidate-id hkconnect_path2_fixed_cohort_base_20261012 --reference-id hkconnect_path2_theme_entry10_20261006 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --end-date 2026-10-09 --output-json results/research/a_share/research_iteration_hk_attribution_next.json
```

最高优先实现任务、验收与证伪条件：见本轮scorecard.next_priority及研究报告；先完成逐日实际股票贡献重构，不把不存在的策略ID写成执行命令。

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `high_return_monthly`：`hkconnect_path2_theme_entry10_20261006`、`hkconnect_path2_theme_entry11_20261007`、`hkconnect_path2_fixed_cohort_base_20261012`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `biweekly_breakout`：`hkconnect_path2_theme_entry10_20261006`、`hkconnect_path2_theme_entry11_20261007`、`hkconnect_path2_fixed_cohort_base_20261012`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `elasticity_cost_control`：`hkconnect_path2_theme_entry10_20261006`、`hkconnect_path2_theme_entry11_20261007`、`hkconnect_path2_fixed_cohort_base_20261012`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 沪港通 Path3

### 上一轮候选与结果摘要

`hkconnect_path3_mechanism_20261008_manual` reject。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：冻结theme_risk52与机制消融，检查换股事件及gross/net成本贡献；不再相邻hold/cap。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

冻结theme_risk52与机制消融，检查换股事件及gross/net成本贡献；不再相邻hold/cap。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path3_theme_risk52_20261003'"'"'); print(pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path3_theme_risk52_20261003__since_2023_01/annual_returns.csv'"'"').to_string(index=False))'
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `weekly_turnover_reduction`：`hkconnect_path3_mechanism_20261008_manual`、`hkconnect_path3_theme_risk52_20261003`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `weekly_defensive_overlay`：`hkconnect_path3_mechanism_20261008_manual`、`hkconnect_path3_theme_risk52_20261003`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `cost_stress`：`hkconnect_path3_mechanism_20261008_manual`、`hkconnect_path3_theme_risk52_20261003`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 沪港通 Path4（quality / liquidity momentum）

### 上一轮候选与结果摘要

`hkconnect_path4_mechanism_20261008_manual` robust_observation。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：冻结v47与mechanism，检查2026负收益是否集中在risk-on股票；观察位不晋级。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

冻结v47与mechanism，检查2026负收益是否集中在risk-on股票；观察位不晋级。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality'"'"'); print(pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality__since_2023_01/annual_returns.csv'"'"').to_string(index=False))'
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `quality_momentum`：`hkconnect_path4_mechanism_20261008_manual`、`hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `liquidity_momentum`：`hkconnect_path4_mechanism_20261008_manual`、`hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `ytd_guard`：`hkconnect_path4_mechanism_20261008_manual`、`hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 沪港通 Path5（breakout retest / pullback continuation）

### 上一轮候选与结果摘要

`hkconnect_path5_mechanism_20261008_manual` reject。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：冻结frozen_shape与满额mechanism，核对risk-on gross损失/实际股票仓位；维持停止补cap修复假设。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

冻结frozen_shape与满额mechanism，核对risk-on gross损失/实际股票仓位；维持停止补cap修复假设。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907'"'"'); print(pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907__since_2023_01/annual_returns.csv'"'"').to_string(index=False))'
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `pullback_definition`：`hkconnect_path5_mechanism_20261008_manual`、`hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `retest_confirmation`：`hkconnect_path5_mechanism_20261008_manual`、`hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `pause_or_redesign`：`hkconnect_path5_mechanism_20261008_manual`、`hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 沪港通 Path6（large liquid core）

### 上一轮候选与结果摘要

`hkconnect_path6_mechanism_20261008_manual` reject。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：冻结lowvol_hold18与mechanism，监控2017、中窗回撤以及集中度/换手，不相邻hold搜索。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

冻结lowvol_hold18与mechanism，监控2017、中窗回撤以及集中度/换手，不相邻hold搜索。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path6_lowvol_hold18_20261008'"'"'); print(pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path6_lowvol_hold18_20261008__since_2023_01/annual_returns.csv'"'"').to_string(index=False))'
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `large_liquid_core`：`hkconnect_path6_mechanism_20261008_manual`、`hkconnect_path6_lowvol_hold18_20261008`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `lowvol_liquid_core`：`hkconnect_path6_mechanism_20261008_manual`、`hkconnect_path6_lowvol_hold18_20261008`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `capacity_cost`：`hkconnect_path6_mechanism_20261008_manual`、`hkconnect_path6_lowvol_hold18_20261008`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 2026-10-12T01:22:55.151898+08:00 沪港通 Path7（barbell quality growth）

### 上一轮候选与结果摘要

`hkconnect_path7_mechanism_20261008_manual` robust_observation。10/10未实跑的路径仍引用10/09历史证据，不计本轮实验。

### 本轮候选 ID 与命令

未新增/确认回测：同10/09周末端点未增加；既有相邻机制已停止，本轮先完成两项承诺及阶段诊断，尚无通过预登记的新结构理由。不是coverage耗尽全天。

候选设计：冻结cap08与v7，先核对2026正收益来源与风险敞口；不照抄旧v7负收益标签，不相邻cap搜索。

冻结配置条件回放（本轮未执行；Path5为已执行事件成熟度复核）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_defensive_cap08_20261004
```

正式window winner/robust/tracked身份未变；无新active/evict/archive，新HK仅隔离runner进程定义。历史快照保留。

### 下一轮 focus 提示

冻结cap08与v7，先核对2026正收益来源与风险敞口；不照抄旧v7负收益标签，不相邻cap搜索。

下一轮第一条可执行命令（诊断或精确补缺；固定端点无新假设不重复回测）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path7_defensive_cap08_20261004'"'"'); print(pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path7_defensive_cap08_20261004__since_2023_01/annual_returns.csv'"'"').to_string(index=False))'
```

### Focus 候选池

explore保留历史/诊断定义；active/watchlist不增加。已reject配置仅作冻结归因对照，不能因轮换复活。

- `barbell_sleeve_structure`：`hkconnect_path7_mechanism_20261008_manual`、`hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`、`hkconnect_path7_defensive_cap08_20261004`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `biweekly_barbell`：`hkconnect_path7_mechanism_20261008_manual`、`hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`、`hkconnect_path7_defensive_cap08_20261004`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。
- `turnover_control`：`hkconnect_path7_mechanism_20261008_manual`、`hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`、`hkconnect_path7_defensive_cap08_20261004`；先验该focus的信号、目标或成本来源，只有新证据才确认结构变化。

证据：`results/research/a_share/research_iteration_scorecard_20261012.json`；历史阶段诊断单列，不计新回测。

## 反思与下一轮决策 2026-10-12T01:22:55.151898+08:00

1. **上轮决策落实**：10/10承诺A3冻结hold0/hold6五窗确认及阶段归因已执行；HK2固定父目标集合base runner已实现并实跑，273个执行信号及5个预览分开冻结，raw/capped集合与总敞口全同，819次执行资金/费用审计无违规。A1/core与HK5股票贡献尚未实现，继续作为次优先；Path2排序/重复门槛、HK hybrid以及相邻hold/cap探索取消并保持停止。20-ID补缺和Path5成熟度单独记辅助。

2. **本轮认知变化**：A股“移除持有保护跨窗防守改善”不获支持：2020 MaxDD改善6.22pp，2023反而恶化4.50pp；中窗CAGR降2.62/2.53pp，未触发硬阈值但不能晋级，keep_watch。2023 gross缺口约97.26%位于risk-on/caution；2020两组都有损失，不泛化为唯一阶段。成本拖累节省2020约0.00243、2023约0.00040对数收益，远小于gross缺口0.15940/0.08539，否定费用节省足以解释收益差。2026 CAGR20.81%对-2.54%、记录股票实投59.00%对83.87%，只支持近窗防守，不追短窗晋级。HK纯配权：保留父截断前排名母体后中窗相对entry10仅+0.33/+0.11pp，2026低1.49pp；不满足各增1pp，reject。相对正式entry11中窗低1.72/1.38pp，即使回撤改善也未支持收益假设。

3. **失败与自我检查**：coverage是数据齐全性阻断，与策略机制失败分开。A3备选解释为risk-on时移除保护导致过早换股，或不同股票收益/敞口路径；当前条件分组不能因果识别，最小区分是逐日股票贡献+费用重构NAV。HK备选解释是原完全base收益主要来自目标集合改变，或极少数大权重股票驱动；本轮固定集合仅排除了新目标股票选取，实际交易缓冲后持仓仍可不同，不能宣称实际同持仓。下一轮同样用逐日执行贡献区分。runner预览无执行日导致PIT辅助校验报错，修正作用域键并五窗完整重跑；另保留截断前百分位母体，初版试跑数值全部不作最终证据。股票敞口统计发现CASH行，剔除后重算，未把合计100%误当股票满仓。默认10/12数据门禁错误通过固定真实缓存截止10/09重试，不降低门禁。13项定向测试通过。候选对实际robust同窗/同成本，不用弱父或短窗制造晋级，不把phase诊断和补缺计入新增。

4. **停止与改变**：停止HK base/hybrid比例族；A3停止hold相邻值和同端点重复确认，保留keep_watch但下次必须有新股票贡献证据。继续停止A1小因子、Path2排序/门槛/cap/surge、HK3/4/5/7相邻持仓/仓位扫描。本轮实际1新ID+1有效参数确认，低于缩量12–18及常规24–36；因为履行两项可证伪机制承诺、同端点周末及三轮停止规则，未发现允许扩大实验的新结构理由，不声称coverage耗尽全天。其余路径有具体冻结诊断候选和下一条命令，不伪装已实跑。新HK从未进入正式active，reject不需扩大或清退active；无新evict/archive。A股Path1–4/HK4–5若当前robust近窗为负均为观察位，不是强稳定winner。

5. **下一轮决策**：A股最高优先保持A3 hold0/hold6，先实现逐日股票贡献runner，检查2023风险开启期拖累是否来自保护退出后股票；HK最高优先改entry10/entry11的2026入口股票贡献，不继续配权。两者实现验收为无未来信息、实际执行贡献+费用+现金对齐净NAV（逐日累计误差≤1e-6），再输出共同风险组及拖累股票。若A3主要缺口来自risk-off/费用，或HK主要差值来自共有股票权重/费用，否定所选解释；无新结构证据不扩参。尚无新候选ID，实现任务先于策略命令。首条已实现诊断命令见九plan与scorecard.next_priority；Path2仍先按最终guard精确下一批补缺，block下不promote。

五窗卡、完整CAGR/Sharpe/MaxDD/turnover/成本、阶段贡献、执行审计与12路径首命令见 `results/research/a_share/research_iteration_scorecard_20261012.json`。

代码强制相邻验证使用真实同10/09窗口winner锚点：A3候选0/4、HK固定集合候选3/4。两者都无promote资格；A3仅keep_watch，HK因预登记收益支持失败reject，不能用较弱robust参照绕过代码护栏。账本首次幂等检查遇历史记录缺entry_key，已改兼容读取；新增10行经复核保留历史。

HK固定集合原始证据持久化到 `results/research/hkconnect/experiments/fixed_cohort_20261012`（父/候选/正式参照五窗CSV、summary及audit）；目录不属于正式backtests/公开策略扫描，affects_official_winners=false。本轮独立对比图 `docs/strategy_mechanism_comparison_20261012.png` 已目视核对。

Path2 partial candidate-pass 口径限制：其robust `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm` 同时列于实际代码Path1 core_multifactor方向组和Path2 scan变体集合；仍含历史跨池诊断行，只作辅助排查。不得将其meanCAGR当Path2有效改善或晋级，正式Path2继续coverage冻结。本轮不修改用户已有dirty候选池代码。

已再查对应since_2020_01 summary：该partial robust实际alpha_pool_profile/pool_id均为core_explore_seed，确认为跨池历史行；下一轮补缺后优先补candidate-pass输入池过滤验收，不把变体名同时存在两个集合当作正确归属证据。

## 同步与收尾验收

Path2首20-ID四窗80行逐项验收同10/09；缺口736→716/828、完整112。唯一block未清零，影响路径保持冻结、不promote；九plan和报告已改为最终guard新首批命令。补缺耗时约20.2分钟，不计新策略。全部正式身份未变化；weighted/HK artifact和partial Path2诊断已执行。live/public门禁与最终guard结果见scorecard.publication/coverage_after。原始HK逐单turnover明细本地保留，权重/收益/summary/audit及全文件哈希提交。

live导出43条；public导出A股Path1–4各5条+HK35，共55榜项和139详情。新HK隔离候选不在live/public；恢复16历史详情。13项定向测试、真实窗口锚点、两卡五窗有效起止日/同成本、九plan四段与12path、正式身份及用户基线检查通过。最终guard warning_missing=0，唯一Path2缺716/828；表面窗口覆盖不是全组重算证明。
