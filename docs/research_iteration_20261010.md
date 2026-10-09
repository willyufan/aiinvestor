# 2026-10-10 十二路径研究：信号传导与配权机制

## 开轮反思 2026-10-10T01:01:48.922863+08:00

读取10/07、10/08（含手动轮）、10/09报告及scorecard、实验账本和九plan。10/07旧相邻参数承诺已执行或在手动轮取消；10/08资金修复承诺10/09落实，资金回归通过。本轮落实10/09的Path2传导runner和HK2单项hybrid实现，不重复相邻signal/cap/hold搜索。其它路径先复核已登记机制与归因，不能把同步算实验。

A股最高问题：v63与正确momentum_6_1排名不同、权重相同的首个断点在哪里？先实现隔离runner记录排序、晋升掩码、状态及目标；两组无约束/饱和合成例必须区分传导接线与约束压扁。证伪条件：排序差异被合法门槛/状态消除，则否定接线错误；无约束仍不消费排序则先修实现，不推断机制收益。完成后按同截止五窗确认并与正式robust比较，Path2 block禁止promote。

HK最高问题：完全base中窗增益是否可用既有hybrid保留，同时修复2020回撤及2026收益损失？先验公式，再只改entry10的base_weight_mode，隔离不加入active。支持条件：2020/2023净CAGR各增至少1pp，MaxDD恶化≤5pp、Sharpe下降≤0.3、2026净CAGR落后≤2pp；不支持则停止配权比例扩张，转持仓收益归因。

初始guard as_of10/09，Path2缺807/828，较前轮770/832增大源于截止日推进/active口径变化，需进一步核对。先执行guard首20-ID四窗增量批次，保留两市场最低竞争预算。新实验目标因持续coverage阻断降到12–18，但不为凑数制造无信息量参数；机制审计不算新增回测，实际不足必须逐项说明。正式身份先冻结，发布脚本需用各自raw缓存最新端点。kb-web首次pilot既有记录已执行；本轮无新外部字段假设，先验证缓存，不新增调用。

预登记下一轮承诺来源：results/research/a_share/research_iteration_scorecard_20261009.json 的 next_priority。

### 传导证据后的单项消融预登记 2026-10-10T01:10:29.457035+08:00

2020窗口初步174日排名变化、131日standard候选集变化、2日晋升状态变化，但raw/capped目标0变化，core分数0变化。移除重复6-1硬门槛会在174/174日扩大标准候选，合计13254个候选日；这是门槛机制试验理由，不是收益证据。新增隔离aggr_03_97_prom3_liqmom_gate_mom61_off_20261010，仅将standard/fast momentum_6_1阈值设为0，显式growth_elastic池；其余v63配置冻结。候选只由audit runner --gate-ablation在独立进程中注册，不加入任何正式active/scan集合。支持：候选差异传入目标，父策略2020/2023净CAGR各增1pp，MaxDD恶化≤5pp、Sharpe下降≤0.3、2026不恶化2pp；正式robust另做五窗护栏。否定：仍无目标差异或不满足支持条件即停止门槛移除方向，转核心排序/质量选择诊断，不继续cap/surge扫描。端点推进至双方最新10/09，同组显式同日，不将跨日差值当机制收益。

## 十二路径巡检、候选与下轮命令

### A股 Path1（主线 / core_multifactor）

上一轮结果：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual` reject；`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual` reject。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907`，五窗同10/09；2026 CAGR -1.76%。进入观察位，不是强稳定 winner。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。
主线已巡检三个weekly_exposure形态的已有数据，未重新快筛/确认；core_multifactor覆盖64/64只是窗口存在，不等于全组本轮重算。停止旧成长/行业小权重扩参，下一步冻结形态做年度收益与风险阶段归因。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907'"'"'); d=pd.read_csv('"'"'results/backtests/a_share/core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_core_multifactor_shape_control_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom8_sat_three_stage_buffered_cost_guard_risk20_breadth_v20260907,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_risk_graft_20261008_manual,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_multifactor_quality_tilt --comparison-csv /private/tmp/aiinvestor_next_ashare_path1.csv
```

### A股 Path2

上一轮结果：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_ablation_20261008_manual` reject；`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009` reject。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `core_explore_70_30_equal_weight_winner_core`，五窗同10/09；2026 CAGR -14.34%。进入观察位，不是强稳定 winner。

- `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009`：mechanism_parameter_confirmation，五窗口，`reject`。正式参照 `core_explore_70_30_equal_weight_winner_core`；2020/2023净CAGR差 -2.42/-9.39pp、MaxDD差 -7.50/+9.09pp。父配置差 +0.00/+0.00pp。五窗目标和交易仍相同；不是信号未接入，候选/状态差异被后续持仓选择消除。无收益增量且落后正式robust，停止此排序变体。
- `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_gate_mom61_off_20261010`：new_mechanism_ablation，五窗口，`reject`。正式参照 `core_explore_70_30_equal_weight_winner_core`；2020/2023净CAGR差 -2.48/-13.31pp、MaxDD差 -4.76/+9.09pp。父配置差 -0.06/-3.92pp。传导得到支持但收益假设否定：相对v63 2023 CAGR下降3.92pp、2017 MaxDD恶化10.41pp；2026仍-27.04%。停止门槛移除，不扫描邻近阈值。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python scripts/audit_path2_signal_transmission.py --summarize results/research/a_share/research_iteration_state_inspection_20261010.jsonl.gz --candidate-id core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009 --parent-id core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn --summary-json results/research/a_share/research_iteration_state_summary_20261010.json
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_liqmom_signal_mom61_20261009,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core --comparison-csv /private/tmp/aiinvestor_next_ashare_path2.csv
```

### A股 Path3

上一轮结果：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly` keep_watch。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`，五窗同10/09；2026 CAGR -2.54%。进入观察位，不是强稳定 winner。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly'"'"'); d=pd.read_csv('"'"'results/backtests/a_share/core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly --comparison-csv /private/tmp/aiinvestor_next_ashare_path3.csv
```

### A股 Path4（emergent theme discovery）

上一轮结果：`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual` reject。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`，五窗同10/09；2026 CAGR -8.59%。进入观察位，不是强稳定 winner。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn'"'"'); d=pd.read_csv('"'"'results/backtests/a_share/core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_theme_leader_gate_ablation_20261008_manual,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --comparison-csv /private/tmp/aiinvestor_next_ashare_path4.csv
```

### A股 Path5（event knowledge graph）

上一轮结果：`ai_datacenter_power_grid_202607_v0` keep_watch。历史证据截止10/08，不能冒充10/09新实跑。

本轮未新增/确认回测：没有新审计来源；60D仍不足，gross事件收益与Path4 net年化评价未统一，不新增未经审计篮子。
已审计v0成熟度复核：20D +11.70%、40D -0.60%、60D不足；keep_watch。单事件没有五窗CAGR/Sharpe/MaxDD/年换手的可比口径，窗口标签只是元数据，gross与Path4 net未齐，不晋级。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --basket-id ai_datacenter_power_grid_202607_v0 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --path4-sample-tag since_2026_01 --output-json results/research/a_share/research_iteration_event_next.json
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --registry-json results/research/a_share/event_theme_registry.json --candidates-jsonl results/research/a_share/event_theme_candidates.jsonl --basket-id ai_datacenter_power_grid_202607_v0 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --horizons 20,40,60 --path4-reference-strategy-id core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn --path4-sample-tag since_2026_01 --output-json results/research/a_share/research_iteration_event_next.json
```

### 沪港通 Path1

上一轮结果：`hkconnect_path1_mechanism_20261008_manual` keep_watch。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `hkconnect_path1_biweekly_lowvol`，五窗同10/09；2026 CAGR 3.61%。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path1_biweekly_lowvol'"'"'); d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path1_biweekly_lowvol__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_mechanism_20261008_manual,hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_lowvol
```

### 沪港通 Path2

上一轮结果：`hkconnect_path2_mechanism_20261008_manual` reject。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `hkconnect_path2_theme_entry11_20261007`，五窗同10/09；2026 CAGR 13.10%。

- `hkconnect_path2_theme_hybrid_control_20261010`：new_mechanism_ablation，五窗口，`reject`。正式参照 `hkconnect_path2_theme_entry11_20261007`；2020/2023净CAGR差 -1.88/-1.60pp、MaxDD差 +0.76/+0.76pp。父配置差 +0.17/-0.11pp。相对entry10中窗仅+0.17/-0.11pp，换手与成本略升；不满足预登记，不把相对较弱父策略小幅改善当晋级。停止混合比例探索。
- `hkconnect_path2_mechanism_20261008_manual`：mechanism_parameter_confirmation，五窗口，`reject`。正式参照 `hkconnect_path2_theme_entry11_20261007`；2020/2023净CAGR差 +3.04/+2.33pp、MaxDD差 -5.03/+4.26pp。父配置差 +5.09/+3.82pp。相对当前entry11 2020 MaxDD恶化5.03pp、2026净CAGR低10.55pp；保持reject，不继续此配权族。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import json; s=json.load(open('"'"'results/research/a_share/research_iteration_scorecard_20261010.json'"'"')); print(json.dumps(s['"'"'hk_model_set_diagnostic'"'"'],ensure_ascii=False,indent=2))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_mechanism_20261008_manual,hkconnect_path2_theme_entry10_20261006,hkconnect_path2_theme_entry11_20261007
```

### 沪港通 Path3

上一轮结果：`hkconnect_path3_mechanism_20261008_manual` reject。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `hkconnect_path3_theme_risk52_20261003`，五窗同10/09；2026 CAGR 14.05%。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path3_theme_risk52_20261003'"'"'); d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path3_theme_risk52_20261003__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_mechanism_20261008_manual,hkconnect_path3_theme_risk52_20261003
```

### 沪港通 Path4（quality / liquidity momentum）

上一轮结果：`hkconnect_path4_mechanism_20261008_manual` robust_observation。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality`，五窗同10/09；2026 CAGR -3.32%。进入观察位，不是强稳定 winner。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality'"'"'); d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_mechanism_20261008_manual,hkconnect_path4_quality_momentum_monthly_v47_totalmv_quality
```

### 沪港通 Path5（breakout retest / pullback continuation）

上一轮结果：`hkconnect_path5_mechanism_20261008_manual` reject。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907`，五窗同10/09；2026 CAGR -6.98%。进入观察位，不是强稳定 winner。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907'"'"'); d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_mechanism_20261008_manual,hkconnect_path5_pullback_continuation_biweekly_frozen_shape_v20260907
```

### 沪港通 Path6（large liquid core）

上一轮结果：`hkconnect_path6_mechanism_20261008_manual` reject。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `hkconnect_path6_lowvol_hold18_20261008`，五窗同10/09；2026 CAGR 6.24%。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path6_lowvol_hold18_20261008'"'"'); d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path6_lowvol_hold18_20261008__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_mechanism_20261008_manual,hkconnect_path6_lowvol_hold18_20261008
```

### 沪港通 Path7（barbell quality growth）

上一轮结果：`hkconnect_path7_mechanism_20261008_manual` robust_observation。历史证据截止10/08，不能冒充10/09新实跑。

本轮实际robust `hkconnect_path7_defensive_cap08_20261004`，五窗同10/09；2026 CAGR 0.29%。

本轮未新增/确认回测：按连续三轮停止规则暂停旧相邻扩参；本轮优先落实Path2传导/配权机制诊断，未发现有依据的新结构，不为配额复跑已否定形态。coverage仍block但没有声称耗尽整日日更窗口。

正式window winner/robust/tracked身份本轮保持；无新active、无evict/新archive判定，历史定义与快照保留。

下一轮第一条命令（先诊断，重放须满足新数据/新假设停止条件）：

```sh
.venv/bin/python -c 'import pandas as pd; print('"'"'hkconnect_path7_defensive_cap08_20261004'"'"'); d=pd.read_csv('"'"'results/backtests/hkconnect/hkconnect_path7_defensive_cap08_20261004__since_2023_01/annual_returns.csv'"'"'); print(d.to_string(index=False))'
```

五窗确认重放（不是无条件下一轮再跑）：

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_mechanism_20261008_manual,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7,hkconnect_path7_defensive_cap08_20261004
```

## 反思与下一轮决策 2026-10-10T01:27:35.051661+08:00

1. **上轮决策落实**：10/07旧参数在10/08自动轮执行；手动轮发现资金缺陷后取消相邻搜索。10/08资金修复及同配置确认已由10/09完成。本轮落实10/09最高承诺：Path2隔离runner、无约束/饱和合成例、五窗口逐门槛/状态/目标审计；HK2冻结entry10单项hybrid对照实现并实跑。A1阶段归因本轮未执行，继续作为次优先；HK5满额容量方向取消后保持停止。依据为本轮scorecard、transmission_summary、gate_summary、state_inspection；补缺与事件成熟度不冒充新增。

2. **本轮认知变化**：A股原“信号未被消费”被否定：排名五窗全变，2020/2023 standard候选集131/71日改变，但目标0变；2017/2020各2日状态不同。300850.SZ两个状态差异日近月收益-23.40%/-7.50%，新买入要求>0，且实际buy/keep集合无它；这是足够阻断条件，不宣称唯一原因。移除6-1硬门槛后2020目标141/174日改变，证明门槛到持仓可传导；但2023 CAGR相对v63下降3.92pp、2017 MaxDD恶化10.41pp，reject。HK hybrid相对entry10中窗仅+0.17/-0.11pp，未满足各增1pp；正式robust实际为entry11，另列同10/09五窗差值。完全base相对实际robust2020 MaxDD恶化5.03pp、2026 CAGR低10.55pp，reject。

3. **失败与自我检查**：coverage（807→787/828）是资料齐全性阻断；A股本轮失败是门槛机制的收益/风险代价，不是排名字符串接线错误；HK失败是hybrid增益不足且换手/成本略增，不笼统说策略无效。HK配置只改配权，但实际model股票集合极少数日也不同（2017 2日、其它窗口各1日），故不能视为严格“同持仓”配权因果试验；备选解释为交易缓冲/权重路径改变后续保留集合或同分排序，下一轮固定父目标集合区分。A股阻断还可能受质量/保留排名门槛共同影响；本轮只证明负近月收益足以阻断。候选均与当前正式robust比较，4张五窗卡全部reject；没有用短窗爆发或弱父参照晋级。真实ADJACENT验证：两个A股卡0/4、HK hybrid3/4、base4/4；base仍被二次MaxDD护栏拒绝，代码相邻CAGR护栏不能替代风险判断。预检曾误用系统Python，改.venv后通过；下一轮命令初稿误用旧strategies路径，已按results_layout改为backtests并实执行诊断验收。

4. **停止与改变**：停止Path2 mom61排序、重复6-1硬门槛移除、HK hybrid比例探索，保持停止A1小因子权重及HK3/4/5/7相邻hold/cap。新增仅两项有证据机制消融；另2项真实机制确认，4卡reject。未达到coverage缩量目标12–18，更未达常规24–36；原因是三轮停止规则和兑现传导机制闭环，不制造无信息量变体，不声称coverage耗尽整日运行预算。新A股候选只在显式runner进程注册；HK新ID为archive_only隔离研究配置、结论reject；正式active不增，无evict或新增archive判定，历史保留。A股Path1–4及HK4/5当前robust近窗为负，进入观察位，不是强稳定winner；HK7当前实际robust已是cap08，2026 +0.29%，不能照抄上轮v7负收益标签。

5. **下一轮最高决策**：A股转Path3 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly` 对 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`，承接旧卡净CAGR代价约2.5pp而回撤改善的keep_watch证据；先一次五窗同10/09确认，再用已实现gross/net、风险状态与实际敞口字段归因，停止相邻hold扩参。第一条命令如下。HK转固定父策略目标股票集合的base配权机制对照；尚未实现，先实现隔离runner并验收逐信号日cohort一致、PIT、资金与双边费用；保留entry10父/entry11正式参照。支持2020/2023各增1pp、2026不降2pp；任一CAGR降3pp/MaxDD恶化5pp/Sharpe降0.3或收益支持失败即停止该配权族。未实现计划ID不写可执行回测命令，先运行scorecard的model集合诊断。九plan均已落实；十二路径有review/候选设计/首命令。

```sh
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-10-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_hold_protection_ablation_20261008_manual_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly --comparison-csv /private/tmp/aiinvestor_next_ashare_path3.csv
```

Path2下一轮必须先按最终guard精确批次补缺（本轮未补齐，不晋级）：

```sh
.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom1_core_6_1_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap65_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap16_cost_guard_v62_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk28_exit46_cap24_cost_guard_v28,core_explore_70_30_equal_weight_winner_core__aggr_04_96_prom1_core_6_1_cash_off_and_cap100,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard0_fast,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60_dd_guard50,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80,core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk28_exit48_cap28_cost_guard_v39_capacity_stress,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk26_exit46_cap24_cost_guard_v41_underrep_quality,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality
```

完整五窗CAGR/Sharpe/MaxDD/turnover/成本、父与正式参照差值、code相邻验证、十二路径首命令：`results/research/a_share/research_iteration_scorecard_20261010.json`。原始压缩审计保留本地，不上传大文件；可审计摘要、哈希与例证随提交。

Path1主线巡检限制：三个优先weekly_exposure形态中只找到buffered与buffered_asym13共10条既有记录，截止日分别10/09与10/08；asym无比较行。不能宣称三形态同窗同日竞争完成；保持下一轮确认预算记录。

## 同步与验收

weighted/HK artifacts、Path2 partial候选诊断、live/public已执行；正式身份保持。live43/public55榜项与136详情，freshness门禁通过；历史详情删除已逐项恢复（17份）。10项定向测试、4卡五窗同10/09、代码真实相邻锚点、九plan四段和12路径/全focus池验收通过；11条首诊断命令已实执行，Path5事件命令独立执行。原始压缩审计约154MB保留本地，不入Git；摘要含哈希和例证。
