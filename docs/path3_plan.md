# Path 3 研究计划

## 2026-08-13 迭代：周频换手修复跨端点确认（端点 2026-08-12）

### 上一轮候选与结果摘要

- `cap46/turn03` 相对 cap54 将 2023 CAGR/MaxDD/turnover 改善 `1.28pp/23.62pp/-0.89x`，但 2020 CAGR 下降 `9.43pp`，且 2026 MaxDD 恶化 `12.16pp`，判定 `reject`；低换手不能弥补稳定性破坏。
- cap54 incumbent 的 2020/2023/2026 CAGR 为 `17.71%/8.68%/39.60%`，同窗 `promote`。正式 winner/robust/tracked 未变，无 evict/archive；全部 ID 以 `_weekly` 结尾。scorecard：`results/research/a_share/research_iteration_scorecard_20260813.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### 下一轮 focus 提示

- `turnover_reduction` 停止 cap46/turn03，同方向改查 exit-buffer v3 与 cap54 锚，要求 2020 CAGR 下降不超过 3pp。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：cap46-turn03、cap54；`weekly_exit_buffer`：exit-buffer-v3、cap54；`risk_downshift`：cap42-risk10、cap46-risk12；`cost_stress`：cap42-cost-stress、cap54。

## 2026-08-12 四次迭代：周频收益恢复终端确认（端点 2026-08-11）

### 上一轮候选与结果摘要

- 实跑等权底座 `weekly_return_recovery_v6/v7`。v6 的 2020/2023/2026 CAGR 为 `7.82%/7.87%/35.76%`，v7 为 `14.46%/7.38%/42.07%`；相对 cap54 incumbent 的 `17.33%/7.99%/35.67%`，v6 中窗严重退化，v7 虽改善 2026 但 2025 CAGR 从 `41.40%` 降至 `16.94%`，均 `reject`。
- 周频 incumbent/robust/tracked 不变，无 evict/archive；全部 ID 均以 `_weekly` 结尾。scorecard：`results/research/a_share/research_iteration_scorecard_20260812_iter4.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly`、`...cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --comparison-csv results/research/a_share/crash_resilience_strategy_comparison_iter4_batch2.csv --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`。

### 下一轮 focus 提示

- 停止 return-recovery v6/v7，回查 turnover-repair 中间带。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：cap46-turn03、cap54 incumbent；`weekly_exit_buffer`：cap46-exit97、cap54-exit98；`risk_downshift`：cap44-risk08、cap46-risk12；`cost_stress`：cap46-turn03、cap54 incumbent。

## 2026-08-12 三次迭代：周频换手修复确认（端点 2026-08-11）

### 上一轮候选与结果摘要

- `cap46/turn03` 的 2020/2023/2026 CAGR 为 `8.01%/9.59%/36.17%`，turnover `0.65/0.46/2.44x`；相对 cap54 明显改善 2023 回撤与换手并保留短窗弹性，但 2020 收益不足，判定 `keep_watch`。
- `cap44/turn04-v3` 的 2026 CAGR 仅 `0.29%`、MaxDD `-35.21%`，`reject`；cap54 以 `17.33%/7.99%/35.67%` 同窗确认 `promote` incumbent。未改变正式 ID，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`、`...cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly`、`...cap54_hold5_turn05_exit98_risk16_weekly`；全部以 `_weekly` 结尾。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### 下一轮 focus 提示

- 下一轮围绕 cap46 修复 2020，而不是继续压到 cap44；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：cap46-turn03、return-recovery-v7；`weekly_exit_buffer`：cap46-exit97、v6；`risk_downshift`：cap44-risk08、v6-risk12；`cost_stress`：cap46-turn03、cap54 incumbent。

## 2026-08-12 二次迭代记录（端点 2026-08-11）

### 上一轮候选与结果摘要

- return-recovery v6 的 2020/2023/2026 CAGR 为 `6.31%/7.15%/-5.54%`、平均 turnover `1.06x`；v7 为 `10.59%/7.37%/21.74%`、`0.97x`。两者虽降低换手并改善回撤，但 2020 CAGR 相对 cap54 分别下降 `11.02pp/6.74pp`，均 `reject`。
- cap54 以 `17.33%/7.99%/35.67%`、平均 turnover `1.93x` 同窗确认 `promote` incumbent。正式 winner/robust/tracked 未变，无 evict/archive；scorecard：`results/research/a_share/research_iteration_scorecard_20260812_iter2.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`；均以 `_weekly` 结尾。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### 下一轮 focus 提示

- `turnover_reduction` 停止 v6/v7 return-recovery 同形扩参，回查 turnover-repair 两侧，要求 2020 CAGR 不再下降超过 3pp。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：cap46-turn03-repair、cap44-turn04-v3；`weekly_exit_buffer`：cap46-exit97、cap54 incumbent；`risk_downshift`：cap44-risk08、cap46-risk12；`cost_stress`：cap42-cost-stress、cap54 incumbent。

## 2026-08-12 迭代记录（端点 2026-08-11）

### 上一轮候选与结果摘要

- cap44-exit97 与 cap40-turn02 的 2020 CAGR 为 `3.76%/2.50%`，相对 cap54 的 `17.33%` 均大幅退化；cap40 的 2023 CAGR 还降至 `-0.34%`。两条低换手假设均 `reject`，不能用近乎零交易替代收益稳定性。
- cap54 以 2020/2023/2026 CAGR `17.33%/7.99%/35.67%`、五窗平均 turnover `1.93x` 同窗确认 `promote` incumbent。正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`；均以 `_weekly` 结尾。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### 下一轮 focus 提示

- `turnover_reduction` 停止 cap40/44 的极低交易形态，改查 return-recovery v6/v7 是否能恢复中窗。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：return-recovery-v6、return-recovery-v7；`weekly_exit_buffer`：cap46-exit97、v6；`risk_downshift`：cap44-risk08、v6-risk12；`cost_stress`：cap54 incumbent、v7。

## 2026-08-11 二次迭代记录（约 07:38 CST）

### 上一轮候选与结果摘要

- cap46 exit97 与 turn-repair 的 2020 CAGR 为 `2.71%/8.07%`，相对 cap54 分别下降 `14.83pp/9.47pp`，均触发中窗稳定性护栏并 `reject`；虽然 turn-repair 的五窗平均 turnover 降至 `0.99x`，收益牺牲过大。
- cap54 以 2020/2023/2026 CAGR `17.54%/8.27%/37.66%`、五窗平均 turnover `1.93x` 同窗确认 `promote` incumbent。正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`；均以 `_weekly` 结尾。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### 下一轮 focus 提示

- `turnover_reduction` 停止 cap46 当前两条低收益形态，下一轮测试 cap44/cap40 的更低风险换手线并保留 cap54 锚。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：cap40-turn02-v4、cap44-turn02；`weekly_exit_buffer`：cap44-exit97、cap54 incumbent；`risk_downshift`：cap44-risk08、cap40-risk08；`cost_stress`：cap40-turn02、cap54 incumbent。

## 2026-08-11 迭代记录

### 上一轮候选与结果摘要

- turnover-repair-v3 与 cap42/turn03 的 2020 CAGR 为 `11.52%/7.32%`，相对 cap54 分别下降 `6.01pp/10.22pp`，均 `reject`；低换手假设未获得中窗支持。cap54 以 2020/2023/2026 CAGR `17.54%/8.27%/37.66%`、平均 turnover `1.93x` 确认 `promote` incumbent；正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`；均以 `_weekly` 结尾。

### 下一轮 focus 提示

- `turnover_reduction` 停止 turn03/04 的弱收益形态，回到 cap46 的 exit-buffer/turn03 两侧确认。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：cap46-turn03-exit98、cap46-exit97；`weekly_exit_buffer`：cap46-exit97、cap54 incumbent；`risk_downshift`：cap44-risk08、cap46-risk12；`cost_stress`：cap46-turn03、cap54 incumbent。

## 2026-08-10 二次迭代记录（约 07:27 CST）

### 上一轮候选与结果摘要

- cost-stress / risk-downshift 的 2020/2023/2026 CAGR 为 `3.99%/3.48%/30.81%`、`1.66%/2.28%/31.30%`；平均 turnover 降至 `0.77x/0.76x`，但中窗 CAGR 大幅退化，均 `reject`。
- cap54 incumbent 为 `17.89%/8.39%/41.07%`、平均 turnover `1.96x`，确认 `promote`；winner / robust / tracked ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述3个ID>`；所有 ID 均以 `_weekly` 结尾。

### 下一轮 focus 提示

- `turnover_reduction` 停止 turn02 极低换手形态，回到 turn03/04 中间带；目标是在 `1–3x` turnover 恢复 2020/2023。第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：turnover-repair-v3、cap42-turn03；`weekly_exit_buffer`：exit-buffer-v3、cap46-exit97；`risk_downshift`：cap42-risk06、cap44-risk08；`cost_stress`：cap42-risk10、cap54 incumbent。

## 2026-08-10 迭代记录

### 上一轮候选与结果摘要

- return-recovery v6/v7 的 2020/2023/2026 CAGR 为 `8.03%/8.20%/41.99%`、`14.88%/7.74%/47.95%`；短窗爆发不能抵消中窗退化，均触发稳定性护栏并 `reject`。
- cap54 incumbent 为 `17.89%/8.39%/41.07%`、平均 turnover `1.96x`，确认 `promote`；未改变 window winner / robust / tracked，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述3个ID>`。

### 下一轮 focus 提示

- `turnover_reduction` 继续压低交易强度，但要求 2020/2023 CAGR 不触发 3pp 护栏；第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：`...weekly_cost_stress_weekly`、`...weekly_risk_downshift_weekly`；`risk_cost_stress`：cost-stress、risk-downshift。
- `return_recovery`：`...weekly_return_recovery_v6_weekly`、`...v7_weekly`；`pure_weekly_confirmation`：cap54 incumbent、weekly-cost-stress。

## 2026-08-09 二次迭代记录（约 08:00 CST）

### 上一轮候选与结果摘要

- 纯周频确认 exit-buffer `cap44/risk08`、`cap46/risk12` 与 cap54 incumbent。假设是 exit97 + 低 turn 能降换手并保住中窗；前两者五窗平均 turnover 降至 `0.76x/1.04x`，但 2020/2023 CAGR 仅 `3.84%/3.81%`、`2.76%/0.76%`，均 `reject`。
- cap54 为 `17.89%/8.39%/41.07%`、平均 turnover `1.96x`，确认 `promote` incumbent；winner / robust / tracked ID 未变，无 evict。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述3个ID>`；所有 ID 均以 `_weekly` 结尾。

### 下一轮 focus 提示

- `turnover_reduction` 停止继续压 turn02，改验 return-recovery v6/v7 能否在 `1–3x` 换手带恢复中窗。第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：`...return_recovery_v6_weekly`、`...return_recovery_v7_weekly`；`weekly_exit_buffer`：`...cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`、`...cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`。
- `risk_downshift`：`...cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`、`...cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly`；`cost_stress`：`...cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly`、`...cap54_hold5_turn05_exit98_risk16_weekly`。

## 2026-08-09 迭代记录

### 上一轮候选与结果摘要

- 五窗口确认 weekly-only 的 `cap44...v3`、`cap46...repair`、`cap54...weekly`；其 since_2020_01 / since_2023_01 / since_2026_01 CAGR 为 `11.87%/6.37%/1.08%`、`8.33%/9.88%/42.44%`、`17.89%/8.39%/41.07%`。
- `cap54` 以平均 turnover `1.96x` 保住稳健锚点，判定 `promote`（确认，不改变 winner / robust）；其余触发稳定性退化，`reject`，不继续同形扩参。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述3个ID>`。

### 下一轮 focus 提示

- `turnover_reduction`：保持 `_weekly` 纯周频语义，挑战 exit buffer；第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：`...cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly`、`...cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`。
- `weekly_risk_control`：`...cap54_hold5_turn05_exit98_risk16_weekly`、`...cap50_hold6_turn04_exit96_risk12_weekly`。

## 2026-08-08 二次迭代记录（约 07:30 CST）

### 上一轮候选与结果摘要

- 本轮确认 turnover-repair cap42 与 reduction-v4 cap40。假设是更低持仓上限可压换手且保住中窗；实际 2020/2023/2026 CAGR 为 `5.87%/6.29%/29.35%`、`1.75%/-1.42%/22.44%`，相对 cap54 incumbent 的 `17.89%/8.39%/41.07%` 明显损害 2020，均 `reject`。
- cap54/hold5/risk16 复核 `promote` incumbent；不是新替换，winner/robust/tracked 无变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly
```

### 下一轮 focus 提示

- 最终 guard focus 仍为 `turnover_reduction`；停止继续缩 cap，改验 cap44-v3 与 cap46-repair，比较温和降换手能否保住中窗；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly
```

### Focus 候选池

- `turnover_reduction`：cap44-v3、cap46-repair；`weekly_exit_buffer`：cap44-exit97-risk08、cap46-exit97-risk12；`risk_downshift`：cap38-risk06-v5、hold9-risk06；`cost_stress`：risk10-base、risk12-turn02；`return_recovery`：v6、v7。

## 2026-08-08 迭代记录（约 01:30 CST）

### 上一轮候选与结果摘要

- `turnover_reduction` 确认 total-mv cap44/hold8/risk10 与 return-recovery-v6。假设是将平均 turnover 压至约 `1x` 后仍保住中窗收益；实际虽达到 `1.08x/1.09x`，但 2020/2023/2026 CAGR 仅 `5.86%/6.85%/-4.57%`、`6.53%/7.52%/-4.97%`，稳定性护栏触发，均 `reject`。
- cap54/hold5/risk16 对照五窗全正，2020/2023/2026 CAGR `17.89%/8.39%/41.07%`、平均 turnover `1.96x`，确认 `promote` incumbent；winner/robust/tracked 无变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly
```

### 下一轮 focus 提示

- 继续 `turnover_reduction`，验证 total-mv cap42/cap40 是否能兼顾低换手和 2026 正收益；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly
```

### Focus 候选池

- `turnover_reduction`：cap42-hold8-risk10、cap40-hold9-risk08-v4；`weekly_exit_buffer`：cap44-hold8-risk08、exit97-risk12。
- `risk_downshift`：risk-downshift-v5、hold9-risk06；`cost_stress`：risk10-base、risk12-turn02；`return_recovery`：v6、v7。

## 2026-08-07 二次迭代记录（约 07:24 CST）

### 上一轮候选与结果摘要

- 纯周频 `weekly_exit_buffer` 确认 exit97-risk12、exit-buffer-v3 与 turnover-repair。exit97 的 2020/2023/2026 CAGR 为 `2.65%/0.58%/3.72%`；v3 为 `13.14%/5.38%/-6.69%`，两者均触发 2023 CAGR/风险护栏，判 `reject`。
- turnover-repair 为 `7.96%/9.56%/32.69%`、平均 turnover `1.01x`，仍只作 `robust_observation`，进入观察位，不是强稳定 winner。artifact 将 v3 推为 2017-window 排序位，但相邻验证拒绝，窗口排序不等于 promote；无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### 下一轮 focus 提示

- 最终 guard 仍指向 `weekly_exit_buffer`；下一轮确认尚未实跑的 cap44/hold8/risk08，并用本轮 exit97/risk12 与 turnover-repair 作同窗对照；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `turnover_reduction`：hold8-risk10、return-recovery-v6；`weekly_exit_buffer`：cap44-hold8-risk08、exit97-risk12（后者本轮 reject，仅作对照）。
- `risk_downshift`：risk-downshift-v5、hold9-risk06；`cost_stress`：risk10-base、risk12-turn02；`return_recovery`：v6、v7。

## 2026-08-07 迭代记录

### 上一轮候选与结果摘要

- 纯周频 `turnover_reduction` 确认 v4、return-recovery-v6 与 turnover-repair 基线。v4 的 2020/2023/2026 CAGR 为 `2.46%/-0.46%/27.61%`，虽将五窗平均 turnover 压到约 `0.40x`，但中窗收益/Sharpe护栏触发，判 `reject`。
- v6 为 `7.90%/7.69%/32.27%`，未触发硬护栏且 turnover 约 `0.58x`，但仍未超过 turnover-repair 的 `7.96%/9.56%/32.69%`，判 `keep_watch`；turnover-repair 仍为 `robust_observation`，进入观察位，不是强稳定 winner。无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### 下一轮 focus 提示

- 最终 guard focus 为 `turnover_reduction`；v4 停止，v6 保留一轮观察。下一轮加入 hold8/risk10 turnover-repair，要求 2020/2023 缺口不超过 `3pp`、平均 turnover 不高于 `1.0x`；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `turnover_reduction`：hold8-risk10、return-recovery-v6；`weekly_exit_buffer`：exit97-risk12、exit-buffer-v3。
- `risk_downshift`：risk-downshift-v5、risk06-hold9；`cost_stress`：risk10-base、risk12-turn02；`return_recovery`：v6、v7（v7 停止同形）。

## 2026-08-06 迭代记录

### 上一轮候选与结果摘要

- 纯周频 return-recovery v6/v7 与 turnover-repair 同端点比较。v6 的 2020/2023/2026 CAGR 为 `7.80%/7.35%/26.49%`、五窗平均 turnover `0.98x`，未触发硬护栏但未改善 robust，判 `keep_watch`。
- v7 为 `13.48%/6.70%/46.15%`，短窗更强但 2023 MaxDD/Sharpe 相对 robust 分别恶化 `7.13pp/0.33`，判 `reject`。turnover-repair 为 `7.78%/9.09%/26.90%`、平均 turnover `1.01x`，仍只作 `robust_observation`：进入观察位，不是强稳定 winner。所有 ID 均以 `_weekly` 结尾；无 winner/robust/tracked 替换与 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### 下一轮 focus 提示

- 最终 guard 已轮转到 `weekly_exit_buffer`；v6 保留一次观察，v7 停止同形，下一轮复核 exit97 与 exit-buffer-v3，并保留 turnover-repair robust。要求平均 turnover 不超过 `1.5x` 且 2020/2023 缺口不超过 3pp。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `weekly_exit_buffer`：exit97-risk12、exit-buffer-v3；`turnover_reduction`：v4-lowturn、return-recovery-v6。
- `risk_downshift`：risk-downshift-v5、risk06-hold9；`cost_stress`：risk10-base、risk12-turn02；`return_recovery`：v6、v7（v7 本轮 reject）。

## 2026-08-05 二次迭代记录（约 07:29 CST）

### 上一轮候选与结果摘要

- 按 `turnover_reduction` 确认 cap44/risk08 与 v4，并以 turnover-repair 同窗比较。两条挑战者 2020/2023/2026 CAGR 为 `6.22%/4.51%/20.49%`、`2.22%/-0.73%/19.38%`；分别因 2023 CAGR 下降 `4.04pp`、以及 2020/2023 同时退化而 `reject`。降低 turnover 的假设在风险侧成立，但收益稳定性不成立。
- turnover-repair 为 `7.41%/8.55%/20.49%`、五窗平均 turnover `1.01x`，仍只作 `robust_observation`：进入观察位，不是强稳定 winner。全部 ID 均为纯周频 `_weekly`；正式 winner/robust/tracked ID 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn03_exit99_risk08_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### 下一轮 focus 提示

- 低换手 v4 与 cap44 中间档均未守住中窗；下一轮改验 return-recovery v6/v7，目标是在平均 turnover 不超过 `1.5x` 时把 2020/2023 CAGR 缺口缩到 3pp 内。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `turnover_reduction`：cap44-risk08、v4-lowturn；`weekly_exit_buffer`：exit96-v6、exit94-v7。
- `risk_downshift`：risk06-hold9、risk08-hold9；`cost_stress`：risk10-base、risk12-turn02；`return_recovery`：v6、v7。

## 2026-08-05 迭代记录（约 01:28 CST）

### 上一轮候选与结果摘要

- 按 `cost_stress` 确认 risk10 与新参数 risk12/turn02/exit99，并以 turnover-repair robust 同窗比较。risk10/risk12 的 2020/2023/2026 CAGR 为 `3.59%/2.81%/20.12%`、`3.57%/3.91%/20.12%`；虽然短窗转强、换手低，但两条均破坏 2020/2023 稳定性，判 `reject`。
- turnover-repair 为 `7.41%/8.55%/20.49%`、五窗平均 turnover 约 `0.63x`，维持 `robust_observation`：进入观察位，不是强稳定 winner。新 risk12 参数证明仅放宽 exit 无法修复中窗，假设不成立；全部 ID 均为纯周频 `_weekly`，无 winner/robust/tracked 替换与 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn02_exit99_risk12_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### 下一轮 focus 提示

- 最终 guard 已轮换到 `turnover_reduction / rotate`。停止 risk10/risk12 turn02 同形，改验 cap44/risk08 中间档与低换手 v4，并保留 turnover-repair 对照；要求 2020/2023 不触发护栏且 turnover 不高于 `1x`。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn03_exit99_risk08_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `cost_stress`：risk10-base、return-recovery-v7；`weekly_exit_buffer`：exit96-v6、exit97-risk12。
- `turnover_reduction`：cap44-risk08、turnover-reduction-v4；`risk_downshift`：risk06-hold9、risk08-hold9；`return_recovery`：v6、v7。

## 2026-08-04 二次迭代记录（约 07:29 CST）

### 上一轮候选与结果摘要

- 按 `risk_downshift` 五窗口确认 risk06，并以 turnover-reduction-v4 与 turnover-repair 同窗比较。risk06 的 2020/2023/2026 CAGR 为 `1.04%/1.24%/10.16%`，risk08-v4 为 `1.95%/-0.80%/8.25%`，两者都明显损伤中窗，均 `reject`；低风险档修复短窗的假设未获得跨窗支持。
- turnover-repair 为 `6.79%/7.59%/6.06%`，换手约 `1x`，但绝对收益仍弱，维持 `robust_observation`：进入观察位，不是强稳定 winner。全部 ID 均为纯周频 `_weekly`，robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

五窗口 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260804_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `cost_stress`。risk06/hold9 已证伪，下一轮用 active risk10/cap42 与 risk12/turn02 两个成本/风险档确认“更低换手是否能保住中窗”，并保留 turnover-repair 对照；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn02_exit99_risk12_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `cost_stress`：risk10-cost-guard、risk12-turn02；`risk_downshift`：risk06-cap30-hold11、risk12-cap46-turn02。
- `weekly_exit_buffer`：exit96-v6、exit97-risk12；`turnover_control`：cap44-turn02、turnover-repair。

## 2026-08-04 迭代记录（约 01:30 CST）

### 上一轮候选与结果摘要

- `weekly_exit_buffer` 五窗口确认 exit97-risk08、exit90-risk12 与 turnover-repair。前两者分别因 2020/2023 CAGR 护栏及 2026 `-25.62%` 退化判 `reject`；假设“更早退出能恢复收益而不破坏中窗”未获支持。
- turnover-repair 的 2020/2023/2026 CAGR 为 `6.79%/7.59%/6.06%`，平均 turnover 约 `1.01x`，保住低换手但绝对收益仍弱，判 `robust_observation`；进入观察位，不是强稳定 winner。robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

完整五窗口 scorecard：`results/research/a_share/research_iteration_scorecard_20260804.json`。

### 下一轮 focus 提示

- 保留 `_weekly` 纯周频口径，下一轮验证更温和的 exit96 收益恢复，不再追逐 exit90 同形；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `weekly_exit_buffer`：exit96-v6、exit97-risk12；`turnover_control`：cap44-turn02、turnover-repair。
- `risk_downshift`：risk06、risk08；`weekly_cost_stress`：risk10-cost-guard、v7-return-recovery。

## 2026-08-03 二次迭代记录（07:18 CST）

### 上一轮候选与结果摘要

- `turnover_reduction` 五窗口确认 risk08/hold9/turn02。挑战者五窗平均 turnover 降至约 `0.84x`，但 2020/2023 CAGR 为 `1.93%/-0.74%`，相对 turnover-repair robust 下降 `4.82pp/8.32pp`，判定 `reject`。
- turnover-repair robust 的 2020/2023/2026 CAGR 为 `6.75%/7.59%/8.35%`、平均 turnover 约 `1.03x`；绝对收益仍弱，只作 `robust_observation`：进入观察位，不是强稳定 winner。无 winner/robust/tracked 变化与 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803_iter2.json`。

### 下一轮 focus 提示

- 当前 `turnover_reduction` 已接近过度防守，下一轮改验 cap44/hold7/risk08 的中间档，要求保留低换手同时把中窗缺口压到 3pp 内。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn03_exit99_risk08_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `turnover_reduction`：cap44/hold7/risk08、cap40/hold9/risk08-v4；`weekly_exit_buffer`：exit97/risk08、exit-buffer-v3。
- `risk_downshift`：risk06/hold9、risk08/hold9；`cost_stress`：risk10/turn02、return-recovery-v7。

## 2026-08-03 迭代记录（01:18 CST）

### 上一轮候选与结果摘要

- `cost_stress` 五窗口确认 risk10/turn02，并与 turnover-repair-risk14 robust 比较。挑战者的 2020/2023/2026 CAGR 为 `3.26%/2.00%/9.34%`，虽然五窗平均 turnover 仅 `0.79x`，但 2020/2023 CAGR 分别下降 `3.49pp/5.58pp`，触发护栏并 `reject`。
- turnover-repair robust 为 `6.75%/7.59%/8.35%`、五窗平均 turnover `1.03x`；五窗为正但 minCAGR 仅约 `3.74%`，仍作 `robust_observation`：进入观察位，不是强稳定 winner。所有 ID 以 `_weekly` 结尾，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803.json`。

### 下一轮 focus 提示

- 继续压成本已伤及中窗，下一轮转 `turnover_reduction` 的 risk08/hold9 形态，目标是保留当前低换手同时把 2023 CAGR 缺口压到 3pp 内。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `cost_stress`：risk10-cost-stress、return-recovery-v7；`turnover_reduction`：risk08/hold9-v4、cap44/hold7/risk12。
- `risk_downshift`：risk06/hold9、risk08/hold9；`weekly_exit_buffer`：exit97/risk08、exit-buffer-v3。
- `weekly_return_recovery`：return-recovery-v6、return-recovery-v7。

## 2026-08-02 二次迭代记录（08:42 CST）

### 上一轮候选与结果摘要

- 在 risk06 基础上新增确认 risk08，并与 turnover-repair robust 同窗比较。risk06/risk08 的 2020/2023/2026 CAGR 为 `1.09%/1.34%/9.69%`、`1.93%/-0.71%/9.30%`，均以中窗收益大幅退化换取低换手，`reject`。
- turnover-repair 为 `6.75%/7.59%/8.35%`，只作 `robust_observation`：进入观察位，不是强稳定 winner。风险降档假设未获支持；无 winner/robust/tracked 变化与 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802_iter2.json`。

### 下一轮 focus 提示

- 转 `cost_stress`，验证 risk10-cost-stress 与 return-recovery-v7；要求 2023 CAGR 缺口小于 3pp且 turnover 不反弹。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `cost_stress`：risk10-cost-stress、return-recovery-v7；`risk_downshift`：risk06/hold9、risk08/hold9。
- `turnover_reduction`：cap42/hold8/risk10、cap44/hold7/risk12；`weekly_exit_buffer`：exit97/risk08、exit-buffer-v3；`weekly_return_recovery`：v6、v7。

## 2026-08-02 迭代记录（08:12 CST）

### 上一轮候选与结果摘要

- `risk_downshift` 五窗口确认 cap42/hold9/turn02/exit97/risk06，并与 turnover-repair robust 同窗比较。挑战者 2020/2023/2026 CAGR 为 `1.09%/1.34%/9.69%`，虽五窗平均 turnover 降到 `0.77x`，但 2020/2023 CAGR 分别下降 `5.66pp/6.25pp`，四项护栏命中并 `reject`。
- turnover-repair robust 为 `6.75%/7.59%/8.35%`、五窗平均 turnover `1.03x`，防守有效但绝对收益仍弱，`robust_observation`：进入观察位，不是强稳定 winner。window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802.json`。

### 下一轮 focus 提示

- risk06 过度防守，下一轮转 `cost_stress` 的 cap42/hold7/risk10，与 current robust 比较，要求 2023 CAGR 缺口小于 3pp且 turnover 不反弹。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `risk_downshift`：risk06/hold9、risk08/hold8；`cost_stress`：risk10-cost-stress、return-recovery-v7。
- `turnover_reduction`：cap42/hold8/risk10、cap44/hold7/risk12；`weekly_exit_buffer`：exit97/risk08、exit-buffer-v3。
- `weekly_return_recovery`：return-recovery-v6、return-recovery-v7。

## 2026-08-01 二次迭代记录（07:26 CST）

### 上一轮候选与结果摘要

- `weekly_exit_buffer` 确认 exit97/risk12 与 exit-buffer-v3，并与 current turnover-repair robust 同窗比较。两挑战者 2020/2023/2026 CAGR 为 `2.45%/0.13%/0.24%`、`11.70%/2.83%/-21.67%`；前者破坏 2020/2023，后者破坏 2023 且短窗转负，均 `reject`。
- current robust 的 2020/2023/2026 CAGR 为 `6.75%/7.59%/8.35%`、2023 turnover 约 `0.47x`，成本防守有效但绝对收益仍弱，判定 `robust_observation`：进入观察位，不是强稳定 winner。window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260801_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 focus=`risk_downshift / rotate`：exit97/risk12 与 v3 均证伪，下一轮验证 cap42/hold9/risk06 的浅风险降档，要求 2023 CAGR 缺口小于 3pp 且不以短窗爆发换中窗退化。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `weekly_exit_buffer`：cap44/hold8/exit97/risk08、current turnover-repair。
- `turnover_reduction`：cap42/hold8/risk10、cap44/hold7/risk12-v3。
- `risk_downshift`：risk08-v4、risk10-base；`cost_stress`：risk10-cost-stress、return-recovery-v7。
- `weekly_return_recovery`：return-recovery-v6、return-recovery-v7。

## 2026-08-01 迭代记录（01:20 CST）

### 上一轮候选与结果摘要

- `turnover_reduction` 五窗口确认纯周频 cap44/hold8/risk10 与 current robust turnover-repair-risk14。挑战者 2020/2023/2026 CAGR 为 `6.30%/3.51%/8.48%`，2023 相对 robust 下降 `4.08pp`，触发 CAGR 护栏，`reject`。
- robust 的 2020/2023/2026 CAGR 为 `6.75%/7.59%/8.35%`，平均 turnover 约 `0.63x`，防守和成本较好但绝对收益仍弱，判定 `robust_observation`：进入观察位，不是强稳定 winner。实验假设“再压持仓形态可保住收益”未获支持；window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### 下一轮 focus 提示

- focus=`turnover_reduction / rotate`：改验 cap42/hold8/risk10 与 turnover-repair-v3，目标是在不增加到高频爆表的前提下恢复 2023 CAGR。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `turnover_reduction`：cap42/hold8/risk10、cap44/hold7/risk12-v3。
- `weekly_exit_buffer`：exit97/risk12、exit-buffer-v3；`risk_downshift`：risk08-v4、risk10-base。
- `cost_stress`：risk10-cost-stress、return-recovery-v7。

## 2026-07-31 迭代记录（07:55 CST）

### 上一轮候选与结果摘要

- `cost_stress` 确认 risk10-cost-stress、return-recovery-v7 与 turnover-repair。前两条 2020/2023 CAGR 为 `3.12%/1.66%`、`11.18%/3.29%`，分别触发 CAGR、Sharpe 或 MaxDD 护栏，均 `reject`。
- turnover-repair 的 2020/2023/2026 CAGR 为 `6.24%/6.86%/0.29%`，低换手但绝对收益弱，判定 `robust_observation`：进入观察位，不是强稳定 winner。实验假设“压换手和提高退出阈值能在成本后保住收益”仅支持防守面；window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### 下一轮 focus 提示

- focus=`cost_stress`：用基础 risk10-weekly 对照 turnover-repair，分离“成本压力标签”与真实 holding/exit 贡献。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `cost_stress`：risk10-weekly、turnover-repair-risk14。
- `weekly_turnover_reduction`：turn02/exit98-risk10、turn03/exit98-risk14。
- `weekly_return_recovery`：return-recovery-v7、risk16-weekly。
- `risk_downshift`：risk06-downshift、risk10-weekly。

## 2026-07-30 二次迭代记录（07:24 CST）

### 上一轮候选与结果摘要

- 按 `risk_downshift` 五窗口确认纯周频 risk06-downshift、risk16，并与当前 turnover-repair robust 同窗比较。risk06 的 2020/2023 CAGR 为 `1.14%/1.38%`、Sharpe 为 `0.15/0.32`，同时触发两窗 CAGR/Sharpe 护栏；risk16 的 2020/2023 MaxDD 相对 robust 恶化 `8.34pp/21.91pp`，两条均 `reject`。
- turnover-repair 五窗为正、2023 turnover 仅 `0.47x`，但 2020/2023 CAGR 只有 `6.81%/7.70%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。所有 candidate id 均以 `_weekly` 结尾，winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 仍为 `risk_downshift / rotate`。risk06 过度压缩收益，下一轮只确认 risk08 中间档与 turnover-repair，仍保持纯周频 `_weekly`。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `risk_downshift`：risk08 turnover-reduction-v4、risk10 cost-stress；`turnover_reduction`：cap44/turn03/risk10、current turnover-repair。
- `weekly_exit_buffer`：exit-buffer-v3、exit97/risk12；`cost_stress/return_recovery`：risk10 cost-stress、return-recovery-v7。

## 2026-07-30 迭代记录

### 上一轮候选与结果摘要

- 纯周频 `cap44/hold8/turn02/exit97/risk08_weekly_exit_buffer_weekly` 的 2020/2023 CAGR 为 `3.34%/2.55%`，相对当前 turnover-repair 低 `3.47pp/5.15pp`，虽 2023 turnover 仅 `0.13x`，仍触发稳定性护栏并 `reject`。
- 当前 `...cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly` 五窗为正，但 2020/2023 CAGR 仅 `6.81%/7.70%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。window winner、robust candidate 与 tracked payload 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730.json`。

### 下一轮 focus 提示

- 最终 guard 轮换到 `risk_downshift`。下一轮确认 risk06 downshift 与当前 turnover-repair 的风险收益取舍，仍要求 strategy id 以 `_weekly` 结尾。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `weekly_turnover_reduction`：`...cap44_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`、当前 turnover-repair。
- `weekly_exit_buffer`：`...cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`、当前 turnover-repair。
- `risk_downshift`：`...cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`、当前 turnover-repair。
- `return_recovery` / `cost_stress`：`...weekly_return_recovery_v7_weekly`、`...risk10_weekly_cost_stress_weekly`。

## 2026-07-29 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- `...exit97_risk12_weekly_exit_buffer_weekly` 与 `...weekly_turnover_reduction_v4_weekly` 均破坏 `since_2020_01`/`since_2023_01` 稳定性，判定 `reject`。
- 对照 `...exit98_risk14_turnover_repair_weekly` 完成确认，但绝对收益仍弱，判定 `robust_observation`：进入观察位，不是强稳定 winner。
- window winner、robust candidate 与 tracked payload 未变化；低换手改善不足以抵消收益损失。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### 下一轮 focus 提示

- focus：`weekly_exit_buffer`。尝试 `cap44/hold8/turn02/exit97/risk08` 的中间形态，并继续以 turnover-repair 为对照。
- 第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_v2_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly
```

### Focus 候选池

- `weekly_exit_buffer`：`...cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_v2_weekly`、`...cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`。
- `weekly_turnover_reduction`：`...cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly`、`...cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`。
- `weekly_risk_overlay`：`...risk08_weekly`、`...risk12_weekly`。
- `weekly_capacity_cost`：`...cap40...cost_guard_weekly`、`...cap46...cost_guard_weekly`。

## 2026-07-29 迭代记录

### 上一轮候选与结果摘要

- 五窗口确认纯周频 turnover-repair、exit-buffer-v3 与 risk16。artifact robust `turnover_repair_weekly` 的 2020/2023/2026 CAGR 为 `6.80%/7.65%/20.38%`、2023 turnover `0.47x`，因绝对收益仍弱只标 `robust_observation`，进入观察位，不是强稳定 winner。
- exit-buffer-v3 相对 robust 的 2023 CAGR/MaxDD/Sharpe 分别恶化 `4.94pp/9.26pp/0.453`，2026 `-13.65%`；risk16 虽 2026 `26.45%`，但 2020/2023 MaxDD 分别恶化 `7.82pp/21.32pp`。两条均 `reject`；低换手/高收益不能覆盖风险破坏。所有 strategy id 保持 `_weekly`，robust/tracked 未变化，无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 五窗口增量命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260729.json`。

### 下一轮 focus 提示

- guard focus 为 `turnover_reduction`。下一轮确认 v4 的更低风险/更长持有是否能守住 turnover-repair 的 2023 收益；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`。

### Focus 候选池

- `turnover_reduction`：turnover-reduction-v4、turnover-repair robust；`weekly_exit_buffer`：exit-buffer-v3、exit97/risk12；`risk_downshift`：risk06-downshift、risk08-v4；`cost_stress/return_recovery`：risk10-cost-stress、return-recovery-v7。

## 2026-07-28 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- 按 `weekly_exit_buffer` 五窗口确认纯周频 risk08/exit97，并与 risk16 robust 同窗比较。挑战者 2020/2023 CAGR 为 `3.41%/2.95%`，相对 robust `16.76%/6.32%` 下降约 `13.35pp/3.37pp`；虽 2023 turnover 仅 `0.13x`、2026 CAGR `27.36%`，仍触发中窗稳定性护栏并 `reject`。
- risk16 五窗口确认 `promote`；“极低换手退出缓冲可守住中窗”的假设不成立。所有候选保持 `_weekly` 后缀，window winner/robust/tracked 未变化，无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly`、正式 robust `...cap54_hold5_turn05_exit98_risk16_weekly`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728_iter2.json`。

### 下一轮 focus 提示

- 当前 focus 为 `weekly_exit_buffer`。下一轮确认较高 risk 与 exit90 的 v3，检验收益恢复是否足以覆盖换手；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `weekly_exit_buffer`：exit-buffer-v3、risk16 robust；`turnover_reduction`：cap48/risk14、risk16；`risk_downshift`：risk10、risk12；`cost_stress/return_recovery`：risk14 turnover-repair、return-recovery-v7。

## 2026-07-28 迭代记录

### 上一轮候选与结果摘要

- 按 `turnover_reduction` 五窗口确认纯周频 risk14 turnover-repair，并与 risk16 robust 同窗比较。risk14 的 2023 turnover 从 `1.36x` 降至 `0.47x`、MaxDD 改善约 `20.32pp`，但 2020 CAGR 从 `16.76%` 降至 `7.16%`，触发稳定性护栏并 `reject`；“低换手仍守住中窗收益”的假设不成立。
- risk16 五窗口确认 `promote`；window winner/robust/tracked 未改变，无 evict。所有 Path3 candidate id 继续保持 `_weekly` 后缀。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728.json`。

### 下一轮 focus 提示

- 最终 focus 为 `turnover_reduction`。下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold6_turn03_exit98_risk14_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`，测试稍高 cap/稍短持有的收益折中。

### Focus 候选池

- `turnover_reduction`：cap48/risk14、risk16 robust；`weekly_exit_buffer`：exit-buffer-v3、risk16；`risk_downshift`：risk10、risk12；`cost_stress/return_recovery`：risk14 turnover-repair、return-recovery-v7。

## 2026-07-27 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 按 `cost_stress` 五窗口确认纯周频 risk10，并与正式 robust risk16 同窗比较。risk10 的 2020/2023 turnover 降至 `0.43x/0.11x`，2023 MaxDD 改善至 `-8.48%`，但 2020/2023 CAGR 仅 `3.54%/2.60%`，相对 robust 下降 `13.22pp/3.72pp`，触发稳定性护栏并 `reject`；“大幅压换手仍守住中窗收益”的假设不成立。risk16 五窗口确认 `promote`，winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly`、正式 robust `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727_iter2.json`。

### 下一轮 focus 提示

- 当前 focus 为 `cost_stress`。risk10 压换手过度，下一轮用 risk14 turnover-repair 检查中间折中；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `cost_stress/turnover_reduction`：risk14 turnover-repair、risk16 robust；`weekly_exit_buffer`：exit-buffer-v3、risk16；`risk_downshift`：risk10、risk12；`return_recovery`：return-recovery-v6、risk16。

## 2026-07-27 迭代记录

### 上一轮候选与结果摘要

- 按 `risk_downshift` 五窗口确认纯周频 `...cap30_hold11_turn02_exit98_risk06_weekly`，以正式 robust `...cap54_hold5_turn05_exit98_risk16_weekly` 同窗对照。risk06 的换手降至 2023 `0.10x`、2026 CAGR 冲到 `51.32%`，但 2020/2023 CAGR 仅 `1.21%/1.36%`，相对 robust 下降 `15.55pp/4.96pp`；实验假设“极低风险/换手可保持中窗并提高短窗”不成立，`reject`。risk16 确认 `promote`，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727.json`。

### 下一轮 focus 提示

- 最终 focus 轮换为 `cost_stress`。不再向 risk06 极端低风险同形扩参，下一轮确认已注册 risk10 cost-stress 与正式 robust 的换手/收益折中；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `risk_downshift`：risk12-weekly、risk14-weekly；`turnover_cost`：risk12-weekly、正式 robust risk16-weekly；`weekly_signal_quality`：cap50/risk14、cap54/risk16；`return_recovery`：cap54/risk16、cap60/risk18。

## 2026-07-26 二次迭代记录（07:19 CST）

### 上一轮候选与结果摘要

- 按 `weekly_exit_buffer` 五窗口确认纯周频 return-recovery-v6，并与正式 robust `...cap54_hold5_turn05_exit98_risk16_weekly` 同窗比较。v6 的 2020 CAGR 为 `7.27%`、比 robust 低约 `9.49pp`，虽换手更低且 2026 CAGR `32.82%`，仍触发中窗稳定性护栏，判定 `reject`；robust 五窗口同端点确认 `promote`。实验假设“exit96 修复 v7 中窗”未获支持，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 轮换为 `risk_downshift`。return-recovery-v6/v7 均破坏 2020，停止同形收益恢复；下一轮检查 risk06 的回撤降低能否守住中窗。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `weekly_exit_buffer`：exit-buffer-v3、正式 robust cap54；`turnover_reduction`：turnover-repair、正式 robust；`risk_downshift`：risk06、risk10；`cost_stress`：cost-stress risk10、正式 robust。

## 2026-07-26 迭代记录

### 上一轮候选与结果摘要

- 按 `turnover_reduction` 五窗口确认纯周频 return-recovery v7，并复核正式 robust `...cap54_hold5_turn05_exit98_risk16_weekly`。v7 的 MaxDD 与 turnover 明显改善、2026 CAGR 为 `55.79%`，但 2020 CAGR 比 robust 低 `3.24pp`，命中稳定性护栏，判定 `reject`；robust 五窗全正，确认 `promote`。window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `weekly_exit_buffer`。v7 的收益恢复以 2020 退化为代价，下一轮检查更温和、exit96 的 v6 是否能守住中窗。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`。

### Focus 候选池

- `turnover_reduction`：return-recovery v6、正式 robust cap54；`weekly_exit_buffer`：exit-buffer-v3、return-recovery-v6。
- `risk_downshift`：risk-downshift risk06、正式 robust cap54；`cost_stress`：cost-stress risk10、return-recovery-v6。

## 2026-07-25 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 按 `cost_stress` 五窗口确认 cost-stress、turnover-repair 与 risk-downshift 三条纯周频候选，并在 weighted 同步后改用正式 robust `...cap54_hold5_turn05_exit98_risk16_weekly` 重算 scorecard。三条在 2020 或 2023 的 CAGR 分别至少下降 `3.72pp/9.60pp/5.12pp`，均触发稳定性护栏，全部 `reject`。
- 本轮未把 artifact 的单窗口排序当成晋级；Path3 robust/tracked 未被本轮三条候选替换，无 evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260725_iter2.json`。

### 下一轮 focus 提示

- 停止上述三条同形成本参数，下一轮用正式 robust 与 return-recovery v7 检查收益恢复；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`。

### Focus 候选池

- `cost_stress`：正式 robust `cap54_hold5...risk16_weekly`、return-recovery v7；`weekly_turnover_reduction`：turnover-repair、正式 robust。
- `weekly_exit_buffer`：exit-buffer-v3、return-recovery-v7；`risk_downshift`：risk-downshift、正式 robust。

## 2026-07-25 迭代记录

### 上一轮候选与结果摘要

- 五窗口确认纯周频 `risk_downshift_weekly` 与 `weekly_exit_buffer_v3_weekly`。前者 2020/2023 CAGR 相对 robust 低 `5.88pp/7.11pp`；后者虽被 artifact 推为 `since_2017_01` 窗口赢家，但 2023 CAGR 低 `4.89pp`、2026 CAGR `-5.23%`，命中稳定性护栏。两条均 `reject`；2017 window winner 发生机械更新，但 robust/tracked candidate 仍为 `...turnover_repair_weekly`，不构成强稳定晋级，无 evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`。

- stale 修复：对上述全部候选把同一 `--only-base-ids` 命令的 `--end-date` 改为 `2026-07-24` 后完成五窗增量复跑；最终 scorecard、strategy JSON 与 live valuation 均采用该终点。

### 下一轮 focus 提示

- 最终 guard 为 `cost_stress`：优先确认低换手成本压力线与 incumbent robust，不继续扩展 v3 同形；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`。

### Focus 候选池

- `risk_downshift`：`...turnover_repair_weekly`、`...risk_downshift_weekly`；`exit_buffer`：`...weekly_exit_buffer_v3_weekly`、`...turnover_repair_weekly`。
- `turnover_reduction`：`...cap42_hold9_turn02_exit97_risk06_weekly`、`...cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`；`return_recovery`：`...cash_off_and_cap60_hold3_turn05_exit94_weekly`、`...weekly_exit_buffer_v3_weekly`。

## 2026-07-24 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 上一轮 v3 与 v7 为 `keep_watch`、turnover-repair 为 `robust_observation`；本轮确认两条 `_weekly` 纯周频低风险候选，并与 current robust `...turnover_repair_weekly` 同窗比较。
- `...weekly_risk_downshift_weekly` 与 `...cap30_hold11...risk06_weekly` 的 2026 CAGR 虽为 `33.49%/57.70%`，但 2020/2023 CAGR 仅约 `1.3%/1.5%`，中窗 CAGR 下降 `6.2pp-7.4pp` 且 Sharpe 下降超过护栏；短窗爆发不足以晋级，两条均 `reject`。winner/robust/tracked 未改写，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly`。

### 下一轮 focus 提示

- 最终 guard 轮换到 `risk_downshift`；只保留能同时守住 2020/2023 且 2026 非负的纯周频形态，以下命令用于失败边界与 v3 对照。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`。

### Focus 候选池

- `weekly_exit_buffer`：`...weekly_exit_buffer_v3_weekly`、`...weekly_return_recovery_v7_weekly`。
- `turnover_reduction`：`...turnover_repair_weekly`、`...weekly_return_recovery_v7_weekly`。
- `weekly_risk_downshift`：`...weekly_risk_downshift_weekly`、`...cap30_hold11...risk06_weekly`（失败对照）。
- `risk_downshift`：`...weekly_risk_downshift_weekly`、`...weekly_exit_buffer_v3_weekly`。

## 2026-07-24 收尾记录

### 上一轮候选与结果摘要

- 五窗口确认纯周频 v3、`turnover_repair_weekly` 与 v7。v3 的 2026 CAGR `-2.26%`，判 `keep_watch`；turnover-repair 的 2023/2026 CAGR `8.86%/41.18%`、换手 `0.47x/2.71x`，artifact 保留为 `robust_observation`，进入观察位，不是强稳定 winner。
- v7 五窗口 CAGR 全正，2026 CAGR `61.21%`，但尚未通过正式相邻晋级且不在当前 active 选择位，判 `keep_watch`；没有 window winner/tracked 改写或 active evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`。

### 下一轮 focus 提示

- 最终 focus 为 `weekly_exit_buffer`，只接受保持 2020/2023 稳定且 2026 非负的纯周频候选；首条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`。

### Focus 候选池

- `weekly_exit_buffer`：`...weekly_exit_buffer_v3_weekly`、`...weekly_return_recovery_v7_weekly`。
- `turnover_reduction`：`...turnover_repair_weekly`、`...weekly_return_recovery_v7_weekly`。

## 2026-07-23 收尾记录

### 上一轮候选与结果摘要

- 本轮五窗口确认纯周频 v3、`cost_stress_weekly`、`turnover_repair_weekly`。v3 的 2026 CAGR `-0.45%`，继续 `robust_observation`；进入观察位，不是强稳定 winner。cost-stress 虽把 2026 CAGR 提到 `31.82%`，但 2020/2023 CAGR 仅 `3.71%/3.04%`，判 `reject`。
- turnover-repair 的 2023/2026 CAGR `9.04%/40.91%`、换手仅 `0.47x/2.71x`，但 2020 CAGR 比 v3 低 `5.40pp`；artifact 将其推入 Path3 robust 观察位，判 `robust_observation`，不是强稳定 winner。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`。

### 下一轮 focus 提示

- 下一轮只做 turnover-repair 的 2020 收益恢复，不继续追 2026 爆发；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_turnover_repair_weekly`。

### Focus 候选池

- `turnover_reduction`：turnover-repair、return-recovery-v7；`weekly_exit_buffer`：v3、return-recovery-v7；`risk_downshift`：risk06 downshift、risk08 weekly；`cost_stress`：cost-stress-weekly、v3。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260723.json`。

## 2026-07-22 收尾记录

- 上一轮候选与结果摘要：上一轮 v3 进入弱观察、v4/v5 淘汰；本轮按 `turnover_reduction` 五窗口确认纯周频 v3 与两条已归档低换手形态，全部 strategy id 以 `_weekly` 结尾，未混入 Path1 周控 overlay。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`。
- Scorecard 与判定：v3 的 2020 CAGR 仅低 incumbent `0.19pp`、换手降到约 `0.98x`，但 2023 CAGR 低 `8.13pp`；artifact 将其放入 2017 window winner/robust 观察位，判 `robust_observation`：进入观察位，不是强稳定 winner。另两条中窗 CAGR/Sharpe 破坏明显，继续 `archive`。
- 下一轮 focus 提示：最终 guard 已转为 `weekly_exit_buffer`；只在 v3 邻域做收益修复，不再单向压换手。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`。
- Focus 候选池：`turnover_reduction` -> `weekly_exit_buffer_v3_weekly`、`cap42_hold7_turn02_exit98_risk10_weekly` 历史边界；`weekly_exit_buffer` -> `v3_weekly`、`cap46_hold7_turn03_exit97...weekly` 历史边界；`risk_downshift` -> `cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`、`cap40_hold8_turn02_exit98_risk08_weekly`；`cost_stress` -> `cost_stress_weekly`、v3。完整 scorecard 见 `research_iteration_scorecard_20260722.json`。

## 2026-07-21 收尾记录

- 上一轮候选与结果摘要：上一轮 v6/v7 以中窗退化告终；本轮按 `turnover_reduction` 重新确认纯周频 v3/v4/v5，全部 strategy id 以 `_weekly` 结尾，未使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap38_hold10_turn02_exit97_risk06_weekly_risk_downshift_v5_weekly`。
- Scorecard 与判定：v3 的 2020 CAGR/MaxDD/Sharpe/turnover 为 `12.39%/-27.09%/0.69/0.98x`，但 2023/2026 仅 `4.02%/-9.88%`；artifact 将其推到 2017/robust 观察位，判 `robust_observation`：进入观察位，不是强稳定 winner。v4/v5 虽将 2020 换手压到 `0.40x/0.38x` 且 2026 有爆发，但 2020/2023 CAGR 仅约 `2.22%/-0.79%` 与 `1.74%/-0.08%`，均 `reject`，不能用短窗替代稳定性。
- 下一轮 focus 提示：最终 guard 仍为 `turnover_reduction`；下一轮先确认 v3，要求 2023 CAGR 至少回升 3pp 且 2026 转正。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`。
- Focus 候选池：`turnover_reduction` -> `weekly_exit_buffer_v3_weekly`、`cap42_hold7_turn02_exit98_risk10_weekly`；`weekly_exit_buffer` -> `weekly_exit_buffer_v3_weekly`、`cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`；`risk_downshift` -> `cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`、`cap40_hold8_turn02_exit98_risk08_weekly`；`cost_stress` -> `cap42_hold7_turn02_exit98_risk10_weekly_cost_stress_weekly`、`cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`。
- evict/归档：v4/v5 已在 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，历史结果保留；v3 留观察。完整 scorecard 见 `research_iteration_scorecard_20260721.json`。

## 2026-07-20 收尾记录

- 上一轮候选与结果摘要：上一轮低换手 v3 仅进入观察；本轮仍限定纯 `_weekly`，新增 v6/v7 尝试在 `1.0x-1.5x` 年换手附近恢复收益，没有混入 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit96_risk12_weekly_return_recovery_v6_weekly,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold5_turn04_exit94_risk14_weekly_return_recovery_v7_weekly`。
- Scorecard 与判定：v6 相对 robust 在 2020/2023 CAGR 低 `6.99pp/8.47pp`；v7 的 2020 CAGR 只低 `0.60pp`，但 2023 低 `9.03pp`、Sharpe 低 `0.249`。二者虽把换手压到 `1.03x/1.30x` 且 2026 CAGR 达 `48.41%/56.26%`，仍不能用短窗爆发覆盖中期破坏，均判定 `reject` 并加入 Path3 archive；winner/robust/tracked 不变。
- 下一轮 focus 提示：停止继续单向放宽 cap/持有期，优先在 incumbent 邻域做 exit-buffer 小步确认。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit92_risk12_weekly_return_balance_v8_weekly`；未注册原因：先完成 v6/v7 archive。
- Focus 候选池：`turnover_reduction` -> `...return_balance_v8_weekly`、`...cap44_hold7_turn03_exit94_risk10_v9_weekly`；`weekly_exit_buffer` -> `weekly_exit_buffer_v3_weekly`、`...cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`；`risk_downshift` -> `...cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`、`...cap40_hold8_turn02_exit98_risk08_weekly`。
- evict/归档：v6/v7 已写入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，保留历史结果，不再进入 active 排名。

## 2026-07-19 收尾记录

- 上一轮候选与结果摘要：上一轮只巡检纯 `_weekly`；本轮围绕 `turnover_reduction` 五窗口实跑 `weekly_exit_buffer_v3`、`weekly_turnover_reduction_v4`、`weekly_risk_downshift_v5`，全部保持纯周频，没有使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn04_exit90_risk12_weekly_exit_buffer_v3_weekly`、`...cap40_hold9_turn02_exit96_risk08_weekly_turnover_reduction_v4_weekly`、`...cap38_hold10_turn02_exit97_risk06_weekly_risk_downshift_v5_weekly`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述 3 个完整 IDs>`。
- Scorecard 与判定：v3 在 2020 CAGR/MaxDD/Sharpe/turnover 为 `12.81%/-27.09%/0.712/0.98x`，但 2023 CAGR 仅 `4.63%`、Sharpe 相对 incumbent 低 `0.313`；artifact 将其推入 2017 window/candidate 观察位，判定 `robust_observation`，进入观察位，不是强稳定 winner。v4/v5 虽把换手降到约 `0.87x/0.98x` 且 2026 CAGR 爆发到 `36.90%/48.39%`，但 2020/2023 CAGR 均接近零或为负，判定 `archive`，不以短窗爆发晋级。
- 下一轮 focus 提示：最终 guard 为 `turnover_reduction`。第一条可执行命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly`；目标是在 `1.0-1.5x` 换手附近恢复 2023 CAGR。
- Focus 候选池：`turnover_reduction` -> `...cap42_hold7_turn02_exit98_risk10_weekly`、`...cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly`；`weekly_exit_buffer` -> `weekly_exit_buffer_v3_weekly`、`...cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`；`risk_downshift` -> `...cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`、`...cap40_hold8_turn02_exit98_risk08_weekly`。
- evict/归档：v4/v5 已从 `PATH2_SCAN_VARIANT_IDS` 的 weekly active 段移除并加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`；另归档三条历史最弱纯周频候选，历史 snapshot 保留。

## 2026-07-09 收尾记录

- 上一轮候选与结果摘要：上一轮 Path3 只做巡检；本轮继续按纯 `_weekly` 口径巡检，guard coverage 完整，没有使用 Path1 月选周控 overlay，也没有把 HK weekly 结论并入 A股 Path3。
- 本轮候选 ID 与命令：本轮未实跑 Path3，原因是 A股新增确认预算给 Path2 `v79`、独立 Path4 `prom24/risk04` 和 Path5 event entry；最终 guard 轮换到 `weekly_exit_buffer`，未跑候选下一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_v3_weekly`。
- Scorecard 与判定：本轮无新增 Path3 scorecard；`scripts/update_weighted_winners.py` 后 Path3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`，判定 `keep_watch`。未实跑候选不能用于 promote 或 tracked 改写。
- 下一轮 focus 提示：最终 guard 给 `weekly_exit_buffer`。下一候选目标是在 exit buffer 里恢复 2020/2023 CAGR，同时守住低换手；若 2020 或 2023 CAGR 低 robust 超过 3pp，或 MaxDD 恶化超过 5pp，则直接 `reject`。
- Focus 候选池：`turnover_reduction` -> `...cap44_hold8_turn04_exit96_risk10_weekly_defensive_repair_v5_weekly`、`...cap42_hold8_turn04_exit94_risk12_weekly_lowturn_repair_v4_weekly`；`weekly_exit_buffer` -> `...cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_v3_weekly`、`...cap46_hold6_turn04_exit90_risk14_weekly_exit_buffer_v4_weekly`；`risk_downshift` -> `...cap42_hold9_turn03_exit97_risk08_weekly_defensive_repair_v6_weekly`、`...cap40_hold9_turn03_exit98_risk06_weekly_defensive_repair_v7_weekly`。
- evict/归档：本轮无 Path3 evict；下一轮注册新 `_weekly` 候选前优先归档连续三轮 keep_watch 以下且无改善的低换手旧样本。

## 2026-07-08 收尾记录

- 上一轮候选与结果摘要：上一轮 Path3 低换手收益修复仍弱于 robust；本轮 Path3 只做纯 `_weekly` 巡检、覆盖确认和下一轮候选设计，没有使用 Path1 月选周控 overlay，也没有新增 Path3 回测。
- 本轮候选 ID 与命令：本轮未实跑 Path3，原因是 A股最低实跑预算已分配给 Path1 satellite、Path2 underrepresented 与独立 Path4 强主题，且 stale 修复需要重跑 A股到 2026-07-08；本轮保留下一条确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn04_exit96_risk10_weekly_defensive_repair_v5_weekly`。
- Scorecard 与判定：本轮无新增 Path3 scorecard；当前 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`，Path3 本轮判定 `keep_watch`。未实跑候选不能用于 promote 或 tracked 改写。
- 下一轮 focus 提示：最终 guard 继续 `turnover_reduction`。第一条命令如上，目标是在低换手下恢复 2020/2023 CAGR；若 2020 或 2023 CAGR 低 robust 超过 3pp，或 MaxDD 恶化超过 5pp，则直接 `reject`。
- Focus 候选池：`turnover_reduction` -> `...cap44_hold8_turn04_exit96_risk10_weekly_defensive_repair_v5_weekly`、`...cap42_hold8_turn04_exit94_risk12_weekly_lowturn_repair_v4_weekly`；`weekly_exit_buffer` -> `...cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_v3_weekly`、`...cap46_hold6_turn04_exit90_risk14_weekly_exit_buffer_v4_weekly`；`risk_downshift` -> `...cap42_hold9_turn03_exit97_risk08_weekly_defensive_repair_v6_weekly`、`...cap40_hold9_turn03_exit98_risk06_weekly_defensive_repair_v7_weekly`。
- evict/归档：本轮无 Path3 evict；下一轮注册新 `_weekly` 候选前优先归档连续三轮未改善的低换手旧样本。

## 2026-07-08 迭代状态

- 上一轮候选/结果摘要：上一轮 `cap44/hold7/turn04/exit94/risk12_weekly_yield_repair_v2_weekly` 判定 `keep_watch`，低换手有效但 2020/2023 CAGR 弱于 robust；本轮 Path3 继续按纯 `_weekly` 口径巡检，未使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：本轮未新增 Path3 `--only-base-ids` 回测，原因是 A股实跑预算给 Path4/Path5；下一轮第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_v3_weekly`。
- Scorecard 与判定：本轮 Path3 无新增实跑 scorecard；`scripts/update_weighted_winners.py` 后 Path3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`。判定 `keep_watch`；v3 假设是在 v2 低换手基础上恢复收益，若 2020 MaxDD 继续深于 robust 或 2023 CAGR 仍低超 3pp，则转 `reject`。
- evict/归档：本轮无 Path3 archive；未回测原因是 A股新增确认预算已被 Path4/Path5 使用。
- 下一轮 focus：最终 guard 给 `risk_downshift`。第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn04_exit96_risk10_weekly_defensive_repair_v5_weekly`；若未注册，先加入 Path3 weekly scan，且 ID 必须以 `_weekly` 结尾。
- Focus 候选池：`risk_downshift` -> `...cap44_hold8_turn04_exit96_risk10_weekly_defensive_repair_v5_weekly`、`...cap42_hold9_turn03_exit97_risk08_weekly_defensive_repair_v6_weekly`；`weekly_exit_buffer` -> `...cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_v3_weekly`、`...cap46_hold6_turn04_exit90_risk14_weekly_exit_buffer_v4_weekly`；`turnover_reduction` -> `...cap42_hold8_turn04_exit94_risk12_weekly_lowturn_repair_v4_weekly`、`...cap44_hold7_turn04_exit94_risk12_weekly_yield_repair_v2_weekly`。

## 2026-07-07 迭代状态

- 上一轮候选/结果摘要：上一轮收益修复线仍未改变 Path3 robust；本轮继续纯 `_weekly` 路径，确认 `cap44/hold7/turn04/exit94/risk12` 的 yield repair v2，不使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：新增/确认 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_yield_repair_v2_weekly`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_share24>,<two_path2_v74>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_yield_repair_v2_weekly,<three_path4_prom24_signal30>`。
- Scorecard 与判定：候选五窗口 CAGR `10.43% / 12.91% / 8.79% / 29.20% / 64.96%`，Sharpe `0.715 / 0.731 / 0.641 / 0.949 / 1.446`，MaxDD `-20.92% / -27.73% / -11.76% / -18.20% / -13.22%`，turnover `1.28x / 1.01x / 0.59x / 2.10x / 3.20x`。相对当前 robust `cash_off_and_cap60_hold3_turn05_exit94_weekly`，2020/2023 CAGR 分别低 `4.54pp / 11.26pp`，但换手显著低，判定 `keep_watch`，不替换 winner/robust/tracked。
- evict/归档：本轮未新增 Path3 archive；上一轮已归档的低换手弱线继续作为边界样本。
- 下一轮 focus：第一条命令建议只做一次“提高收益但守住低换手”的 v3：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_v3_weekly`；若未注册，先加入 Path3 weekly scan，且 ID 必须以 `_weekly` 结尾。
- Focus 候选池：`turnover_reduction` -> `...cap44_hold7_turn04_exit94_risk12_weekly_yield_repair_v2_weekly`、`...cap42_hold8_turn04_exit94_risk12_weekly_lowturn_repair_v4_weekly`；`weekly_exit_buffer` -> `...cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_v3_weekly`、`...cap46_hold6_turn04_exit90_risk14_weekly_exit_buffer_v4_weekly`。

## 2026-07-06 迭代状态

- 上一轮候选/结果摘要：上一轮建议测试 `weekly_yield_repair_weekly`，本轮已注册并五窗口确认；继续保持纯 `_weekly` 路径，没有使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_weekly`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path3_weekly_yield>,<path1>,<two_path2>,<three_path4>`。
- 五窗口结果：CAGR `11.33% / 22.24% / 15.65% / 89.64% / 84.20%`，最大回撤 `-28.17% / -25.38% / -15.47% / -14.09% / -13.15%`。结论：短窗和 2020 改善明显，但 2017/2020 回撤仍深，未改变 Path3 window winner、robust candidate 或 tracked payload。
- evict/归档：归档旧 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly` 与 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`；原因是同邻域低换手线 2017/2023 收益不足，且已被本轮收益修复线覆盖。
- 下一轮 focus：若最终 guard 继续给 `turnover_reduction` 或 `weekly_exit_buffer`，下一候选应在本轮收益修复线基础上下调回撤和换手：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_yield_repair_v2_weekly`；若未注册，先加入 Path3 weekly scan，且 ID 必须以 `_weekly` 结尾。

## 2026-07-05 迭代状态

- 上一轮候选/结果摘要：上一轮建议测试 `cap44/hold7/turn04/exit94/risk12` 折中线；本轮已注册并五窗口确认，保持纯 `_weekly` 路径，没有使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path3_v3>,<path1>,<two_path2>,<three_path4>`。
- 五窗口结果：CAGR `10.43% / 12.91% / 8.79% / 29.20% / 64.96%`，最大回撤 `-20.92% / -27.73% / -11.76% / -18.20% / -13.22%`，年均换手 `1.28x / 1.01x / 0.59x / 2.10x / 3.20x`。
- 结论：v3 比极低换手线有更高收益，但 2020 回撤仍深、2023 收益不足，未改变 Path3 window winner、robust candidate 或 tracked payload；当前 robust 仍为 `cash_off_and_cap60_hold3_turn05_exit94_weekly`，`meanCAGR=31.98% / minCAGR=12.93%`。
- evict/归档：本轮无新增 Path3 archive；上一轮已归档的 cap42/cap44 弱线继续作为低换手边界样本。
- 下一轮 focus：若最终 guard 继续给 `turnover_reduction`，下一候选不要继续压到无收益状态，首条命令建议 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_weekly`；若未注册，先加入 Path3 weekly scan，且 ID 必须以 `_weekly` 结尾。

## 2026-07-04 07:03 CST 状态

- 上一轮候选/结果摘要：上一轮 `cap44/hold8/turn03/exit96/risk10` 提供低换手但 2020 回撤深；本轮按 `turnover_reduction` 继续纯 `_weekly` 路径，注册并确认 `cap42/hold8/turn03/exit96/risk10`，没有使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path3_cap42_turnover_repair>,<path1>,<two_path2>,<three_path4>`。
- 五窗口结果：CAGR `4.49% / 8.50% / 6.85% / 36.55% / 124.21%`，最大回撤 `-21.00% / -28.37% / -5.16% / -14.76% / -12.89%`，年均换手 `0.71x / 0.58x / 0.35x / 0.59x / 2.99x`。
- 结论：低换手证据继续有效，2026 弹性强，但 2017/2020/2023 收益不足；weighted 后 Path3 robust 回到 `cash_off_and_cap60_hold3_turn05_exit94_weekly`，`meanCAGR=31.98% / minCAGR=12.93%`，本轮候选未改变 window winner/robust/tracked。
- evict/归档：将旧 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`；evict 原因是同邻域非 winner/robust，且被本轮更低 cap 版本覆盖。
- 下一轮 focus：最终 guard 给出 `turnover_reduction`。下一轮应测试略高收益/低换手折中 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly`，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_turnover_repair_v3_weekly`；若未注册，先加入 Path3 weekly scan，且 ID 必须以 `_weekly` 结尾。

## 2026-07-01 20:58 CST 状态

- 上一轮候选/结果摘要：上一轮 risk06 过度防守；本轮按 `turnover_reduction` 注册并五窗口确认 `turn03/exit96/risk10` 版本，保持纯 `_weekly` 口径，不使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path3_turnover_repair>,<path1>,<two_path2>,<three_path4>`。
- 五窗口结果：CAGR `4.95% / 9.01% / 6.42% / 38.79% / 149.41%`，最大回撤 `-21.00% / -28.50% / -6.87% / -14.76% / -12.89%`，年均换手 `0.73x / 0.58x / 0.35x / 0.59x / 2.99x`。
- 结论：本轮候选成为 Path3 robust candidate，但 official window winner 未变；它提供低换手证据和 2026 弹性，代价是 2020 回撤仍深、2017/2023 绝对收益不够。
- evict/归档：本轮无新增 Path3 archive；上一轮 risk06 仍需作为低风险边界保留观察，但下一轮应优先复核收益侧而不是继续下调 risk。
- 下一轮 focus：若 guard 仍给 `turnover_reduction`，下一候选应测试略高收益/低换手折中 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn04_exit94_risk12_weekly_turnover_repair_v2_weekly`，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn04_exit94_risk12_weekly_turnover_repair_v2_weekly`；若未注册，先加入 Path3 weekly scan，且 ID 必须以 `_weekly` 结尾。

## 2026-07-01 05:26 CST 状态

- 上一轮候选/结果摘要：上一轮 `exit97/risk08` 低换手周频线收益仍弱；本轮按 `risk_downshift` 注册并五窗口确认 `risk06` 版本，保持纯 `_weekly` 口径，不使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v66_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`。
- 五窗口结果：CAGR `2.76% / 1.58% / 0.43% / 36.96% / 118.51%`，最大回撤 `-16.63% / -28.05% / -7.07% / -15.51% / -12.74%`。结论：2026 弹性强，但 2017/2020/2023 过弱，说明该低风险长持有形态过度防守。
- payload 变化：`scripts/update_weighted_winners.py` 后 Path3 robust candidate 与 2017-window tracked payload 暂切到本轮 risk06；同时 validation 明确拒绝其替换 2017/2020/2023 incumbent，后续需用更强收益候选复核该 payload 切换。
- evict/归档：将上一轮弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`；evict 原因是同邻域 2020/2023 收益不足且被本轮更低风险形态覆盖。
- 下一轮 focus：最终 guard 仍为 `turnover_reduction`。下一轮第一候选应回到略高收益/低换手折中，而不是继续下调 risk；首条命令草案为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`；若未注册，先加入 Path3 weekly scan，并保证 ID 以 `_weekly` 结尾。

## 2026-06-30 17:26 CST 状态

- 上一轮候选/结果摘要：上一轮 `cap44_hold8_turn02_exit99_risk08_weekly` 长窗收益弱；本轮按 `weekly_exit_buffer` 注册并五窗口确认同邻域 exit97 版本，仍保持纯 `_weekly` 路径，不使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：新增并运行 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly`；命令并入本轮 A股受限回测 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly,<three_path4_ids>`。
- 五窗口结果：CAGR `3.36% / 4.59% / 4.57% / 35.19% / 108.52%`，最大回撤 `-15.12% / -27.97% / -3.51% / -15.25% / -12.74%`，年均换手 `0.49x / 0.38x / 0.16x / 0.51x / 2.85x`。
- active pool 处理：将 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit99_risk08_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`；evict 原因是同邻域 exit99 线非 winner/robust，且本轮 exit97 已覆盖该低换手形态。
- 结论：新候选降低长窗换手但收益弱，2026 弹性不足以替代既有 robust；Path3 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `risk_downshift`。下一轮第一候选建议注册 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold9_turn02_exit97_risk06_weekly_risk_downshift_weekly`；若未注册，先加入 Path3 weekly scan，并保证 ID 以 `_weekly` 结尾。

## 2026-06-30 06:12 CST 状态

- 上一轮候选/结果摘要：上一轮 `cap46_hold7_turn03_exit99_risk10_weekly` 只给出 2026 弹性；本轮继续纯 `_weekly` 路径，补齐 `cap44_hold8_turn02_exit99_risk08_weekly` 完整配置并实际五窗口确认，没有使用 Path1 月选周控 overlay。
- 本轮候选 ID 与命令：新增并运行 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit99_risk08_weekly`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit99_risk08_weekly`。
- 五窗口结果：CAGR `3.36% / 4.59% / 4.57% / 35.19% / 108.52%`，最大回撤 `-15.12% / -27.97% / -3.51% / -15.25% / -12.74%`，年均换手 `0.49x / 0.38x / 0.16x / 0.51x / 2.85x`。
- active pool 处理：将 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit99_risk10_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`；evict 原因是上轮同邻域 2017/2020/2023 收益不足，且非 winner/robust。
- 结论：新候选降低长窗换手但收益过弱，2026 弹性不能弥补 2020/2023；Path3 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `weekly_exit_buffer`。下一轮第一候选建议在本轮低换手形态上只调整 exit buffer：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly`；首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit97_risk08_weekly_exit_buffer_weekly`；若未注册，先加入 Path3 weekly scan，并保证 ID 以 `_weekly` 结尾。

## 2026-06-29 17:30 CST 状态

- 上一轮候选/结果摘要：上一轮周频 exit-buffer 线未晋级；本轮继续只使用 `_weekly` 结尾的纯周度策略，不把 Path1 的月选周控 overlay 计入 Path3。
- 本轮候选 ID 与命令：新增并运行 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit99_risk10_weekly`；命令同本轮 A股受限回测 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v63_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit99_risk10_weekly,<three_path4_ids>`。
- 五窗口结果：CAGR `5.08% / 7.71% / 11.23% / 38.39% / 169.23%`，最大回撤 `-21.05% / -27.59% / -8.45% / -14.78% / -12.89%`，年均换手 `0.74 / 0.58 / 0.41 / 0.60 / 3.12`。
- active pool 处理：新增前归档上一轮失败的 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`；evict 原因是 2020/2023 收益不足且未改善 robust。
- 结论：新候选 2026 弹性强，但 2017/2020 中长窗不及当前 Path3 robust；window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> cost_stress`。下一轮第一候选建议保留 exit99，但降低单票与风险暴露验证成本压力：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit99_risk08_weekly`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit99_risk08_weekly`。

本文档用于约束和记录 `Path 3`（周度高频调仓路径）。
Path 3 只跟踪纯周度换股候选，候选 `strategy_base_id` 必须以 `_weekly` 结尾；月度选股叠加周度仓位 overlay（例如 `__port_weekly_exposure`、`__sat_weekly_risk`、`__sat_three_stage`）不纳入本路径。

## 本轮执行计划（2026-06-29 05:25 CST）

- 上一轮 `cap46/hold7/turn02/exit99/risk12` 提供低换手信息但收益不足，本轮沿 `weekly_exit_buffer` 注册并确认纯 `_weekly` 候选 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`；没有把 Path1 月度选股 + weekly overlay 纳入 Path3。
- 本轮命令与 Path2 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v62_medium_cycle_growth,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v62_medium_cycle_growth,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`。
- 新候选五窗口 CAGR `3.87% / 4.12% / 4.29% / -1.48% / 19.21%`，最大回撤 `-11.71% / -25.71% / -6.04% / -16.05% / -13.27%`，换手 `0.97x / 0.87x / 0.65x / 0.80x / 2.26x`。结论：换手可控但收益断层，2020 回撤偏深，不能替换 Path3 official window winner 或 robust。
- `scripts/update_weighted_winners.py` 后 Path3 official 仍为 2017 `cash_off_and_cap60_hold3_turn05_exit94_weekly`、2020 `cap56_hold5_turn05_exit96_risk20_weekly`、2023 `cash_off_and_cap50_hold2_turn12_exit90_weekly`、2025/robust `core_6_1_cash_off_and_cap100_weekly`；本轮无新增 evict，最终 coverage `ashare_path3_weekly_universe 64/64`。
- 最终 focus 为 `risk_downshift`。下一轮第一条命令建议回到风险下移但避免再牺牲 2023/2025 收益：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn02_exit98_risk10_weekly_risk_downshift_weekly`；若未注册，先加入 Path3 weekly scan，并保证 ID 以 `_weekly` 结尾。

## 本轮执行计划（2026-06-28 17:40 CST）

- 上一轮 focus 指向 risk/exit 邻域，本轮接续启动前已注册的纯 `_weekly` 候选并完成五窗口结果巡检；没有把 Path1 月度选股 + weekly overlay 纳入 Path3。最终 guard 仍为 `ashare_path3_weekly_universe 63/63`。
- 本轮候选 ID：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn02_exit99_risk12_weekly`。五窗口 CAGR `2.86% / 5.08% / 4.75% / 34.54% / 107.24%`，最大回撤 `-16.75% / -27.53% / -5.02% / -15.11% / -12.74%`，换手 `0.50x / 0.40x / 0.20x / 0.51x / 2.85x`；低换手信息有价值，但长中窗收益不足，不替换 official window winner 或 robust。
- 本轮 active pool 处理：启动前代码已归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold8_turn02_exit98_risk14_weekly`，理由是低换手相邻弱线非 winner/robust，且被本轮 `cap46/hold7/exit99/risk12` 覆盖。本轮未新增其它 evict。
- `scripts/update_weighted_winners.py` 后 Path3 official 仍为 2017 `cash_off_and_cap60_hold3_turn05_exit94_weekly`、2020 `cap56_hold5_turn05_exit96_risk20_weekly`、2023 `cash_off_and_cap50_hold2_turn12_exit90_weekly`、2025/robust `core_6_1_cash_off_and_cap100_weekly`。最终 focus 为 `weekly_exit_buffer`。
- 下一轮第一条命令建议沿 exit buffer 方向测试而不是继续压到极低换手：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`；若未注册，先加入 Path3 weekly scan，并保证 ID 以 `_weekly` 结尾。

## 本轮执行计划（2026-06-27 19:24 CST）

- 上一轮 `cap54/hold5/turn05/exit96/risk16_weekly` 未替换 official，本轮没有新增 Path3 `_weekly` 五窗口确认；保持纯周频口径，只做 `refresh_active`、weighted 同步和下一轮候选设计，没有把 Path1 月度选股 + weekly overlay 纳入 Path3。
- `refresh_active` 重新给出 risk-downshift 低换手边界：`cap56_hold5_turn05_exit96_risk20_weekly` 仍是 2020 official winner；`cap50_hold6_turn04_exit98_risk16_weekly` 在 2023 CAGR `18.86%`、MaxDD `-10.68%`、换手约 `0.71x`，说明低换手风险下移仍有信息量；但 `cap54_hold5_turn05_exit96_risk16_weekly` 和相邻候选没有改善 robust。
- `scripts/update_weighted_winners.py` 后 Path3 official winners 为 2017 `cash_off_and_cap60_hold3_turn05_exit94_weekly`、2020 `cap56_hold5_turn05_exit96_risk20_weekly`、2023 `cash_off_and_cap50_hold2_turn12_exit90_weekly`、2025/robust `core_explore_80_20_total_mv_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`；robust `meanCAGR=108.14%`、`minCAGR=19.15%`，但最差回撤 `-63.08%`、集中度惩罚仍高。本轮无 Path3 evict。
- 最终 guard focus 为 `risk_downshift`。下一轮第一条命令建议只做一个更低风险/更长持有的 `_weekly` 确认，并以 2023 回撤与换手约束为主：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk14_weekly`；若未注册，先加入 Path3 weekly scan，并只归档非 winner/robust 弱线。

## 本轮执行计划（2026-06-25 06:56 CST）

- 上一轮 `cap34/hold8/turn02/exit96/risk08` 证明过度降换手失效，本轮保持纯 `_weekly` 口径，注册并确认 `cap54/hold5/turn05/exit96/risk16`；没有把 Path1 月度选股 + weekly overlay 计入 Path3。
- 本轮 active pool 处理：将上一轮弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold8_turn02_exit96_risk08_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。执行中发现 `cap50_hold5_turn05_exit98_risk16_weekly` 仍是 Path3 2020 window winner，已恢复其 active 资格，避免误归档 winner。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk16_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path2 合并执行。
- 新候选五窗口 CAGR `12.86% / 24.14% / 20.50% / 82.59% / 105.38%`，最大回撤 `-28.03% / -25.33% / -14.52% / -14.92% / -12.88%`，换手 `2.04x / 1.49x / 1.30x / 2.89x / 1.98x`。结论：比极低换手线更有可比信息，但 2017/2020 回撤偏深，且 official 2020 winner 仍是 `cap50_hold5_turn05_exit98_risk16_weekly`；不替换 Path3 robust/tracked。
- `scripts/update_weighted_winners.py` 后 Path3 official winners 为 2017 `cash_off_and_cap60_hold3_turn05_exit94_weekly`、2020 `cap50_hold5_turn05_exit98_risk16_weekly`、2023 `cash_off_and_cap50_hold2_turn12_exit90_weekly`、2025 `core_6_1_cash_off_and_cap100_weekly`；Path3 candidate 仍为 `cash_off_and_cap60_hold2_turn12_exit92_weekly`。最终 focus 为 `weekly_exit_buffer`。
- 下一轮第一条命令建议在本轮 `hold5/turn05` 形态上测试 exit buffer，而不是回到 `hold8/turn02` 极端低换手：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`；若未注册，先加入 Path3 weekly scan，并只归档非 winner/robust 弱线。

## 本轮执行计划（2026-06-24 19:22 CST）

- 上一轮 `cap32/hold8/turn03/exit96/risk06` 证明低换手但收益不足，本轮保持纯 `_weekly` 口径，注册并确认 `cap34/hold8/turn02/exit96/risk08`，仍使用 `core_explore_seed` 池。
- 本轮 active pool 处理：将 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap32_hold8_turn03_exit96_risk06_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，并继续排除出 Path2 pass。evict 理由：同一低换手长持有邻域 2023/2025 连续弱，非 window winner/robust。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold8_turn02_exit96_risk08_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股其它路径合并执行。
- 五窗口 CAGR `3.39% / 3.76% / 1.33% / -2.35% / 70.95%`，最大回撤 `-12.99% / -27.18% / -4.44% / -21.98% / -18.15%`，换手 `0.51x / 0.39x / 0.13x / 1.63x / 4.53x`。结论：进一步压换手后 2017-2025 收益基本失效，2026 单窗弹性不足以晋级。
- `refresh_active` 同步补充了边界信息：过度低换手长持有版本在 2023/2025 容易收益塌缩；`hold5/turn05/exit96`、`hold4/turn06/exit94` 等中等换手线仍比极低换手线更可用。`scripts/update_weighted_winners.py` 后 Path3 window winner、robust candidate、tracked/live/public 未切换。
- 最终 guard 为 `pass`，下一轮 focus 转为 `weekly_exit_buffer`。不要继续压到 `turn02/hold8` 以下；第一条命令建议回到中等换手、成本压力与 exit buffer 的平衡形态：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk16_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条非 winner/robust 弱周频候选。

## 本轮执行计划（2026-06-24 06:57 CST）

- 上一轮 `cap28_hold10_turn04_exit94_risk04_weekly` 2023 仍为负，本轮保持纯 `_weekly` 口径，注册并确认 `cap32/hold8/turn03/exit96/risk06` 低换手收益修复；首次合并回测后已确认并修正 alpha pool，最终使用 `Path1/3 核心-探索-种子共用池 (core_explore_seed)`。
- 本轮 active pool 处理：将 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap28_hold10_turn04_exit94_risk04_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，并同步排除出 Path2 pass。evict 理由：同一低风险长持有邻域连续 2023/2025 失败，且非 winner/robust。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap32_hold8_turn03_exit96_risk06_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，首次与 A股其它路径合并执行，修正池归属后单独重跑同一 ID。
- 修正后五窗口 CAGR `6.14% / 7.80% / 0.64% / -2.91% / 15.86%`，最大回撤 `-13.52% / -26.05% / -9.15% / -20.57% / -15.95%`。结论：2017 回撤较浅但收益不足，2025 为负，不能替换 Path3 window winner、robust candidate 或 tracked/live/public payload。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 62/62 complete`；`update_weighted_winners.py` 后 Path3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`，本轮不因短窗波动晋级。
- 下一轮 focus 仍为 `turnover_reduction`。第一条命令建议在当前 `hold8` 低换手形态上进一步降低交易强度但补风险缓冲：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold8_turn02_exit96_risk08_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条非 winner/robust 弱周频候选。

## 本轮执行计划（2026-06-23 17:21 CST）

- 上一轮 `cap28_hold12_turn03_exit96_risk04_weekly` 证明继续拉长持有会牺牲 2023/2025；本轮保持纯 `_weekly` 口径，回补到 `hold10/turn04/exit94` 做成本压力下的收益修复，仍显式使用 `core_explore_seed` 池。
- 本轮 active pool 处理：将 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap28_hold12_turn03_exit96_risk04_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，并同步排除出 Path2 pass。evict 理由：同一低风险长持有邻域已连续给出 2023/2025 负样本，且不是 winner/robust。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap28_hold10_turn04_exit94_risk04_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股其它路径合并执行。
- 五窗口结果：CAGR `12.33% / 12.29% / -1.14% / 28.68% / 103.11%`，最大回撤 `-24.58% / -21.20% / -19.44% / -19.38% / -13.70%`，Sharpe `0.7780 / 0.7305 / -0.0175 / 0.9564 / 1.8896`，换手 `1.20x / 1.19x / 0.59x / 2.46x / 4.84x`。结论：2026 弹性恢复，但 2023 为负且回撤不浅，不能替换 Path3 window winner、robust candidate 或 tracked/live/public payload。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 62/62 complete`；`scripts/update_weighted_winners.py` validation 继续拒绝该低风险周频支线。
- 最终 focus 转为 `turnover_reduction`。下一轮第一条命令建议暂停 `risk04` 长持有支线，改测更平衡的低换手收益修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap32_hold8_turn03_exit96_risk06_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条非 winner/robust 弱周频候选。

## 本轮执行计划（2026-06-23 05:27 CST）

- 上一轮 `cap30_hold11_turn03_exit96_risk06_weekly` 已确认 2023/2025 失败；本轮按 `risk_downshift` 继续保持纯 `_weekly` 口径，把单票降到 `cap28`、持有拉到 12 周、风险阈值降到 `risk04`，并显式使用 `core_explore_seed` 池。
- 本轮 active pool 处理：将旧弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn03_exit96_risk06_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：同一低换手长持有邻域上一轮已给出负样本，且不是 winner/robust。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap28_hold12_turn03_exit96_risk04_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股其它路径合并执行。
- 五窗口结果：CAGR `11.76% / 5.95% / -0.14% / -7.18% / 24.31%`，最大回撤 `-23.17% / -26.25% / -7.98% / -24.76% / -15.85%`，Sharpe `0.8521 / 0.5050 / -0.0150 / -0.0940 / 0.7404`，换手 `0.99x / 0.48x / 0.10x / 1.75x / 4.23x`。结论：换手低但 2023/2025 收益断层，不能替换 Path3 window winner、robust candidate 或 tracked/live/public payload。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 62/62 complete`。`scripts/update_weighted_winners.py` validation 继续拒绝该低风险长持有支线。
- 最终 focus 转为 `cost_stress`。下一轮第一条命令建议不要继续拉长持有，改做成本压力下的收益修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap28_hold10_turn04_exit94_risk04_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条非 winner/robust 弱周频候选。

## 本轮执行计划（2026-06-22 17:34 CST）

- 上一轮 `cap30_hold11_turn02_exit98_risk06_weekly` 继续压低换手但 2023/2025 不足；本轮保持纯 `_weekly` 口径，按 focus `weekly_exit_buffer` 回补一点出场缓冲与允许换手，并显式指定 `ALPHA_POOL_PROFILE_CORE_EXPLORE_SEED`，避免因策略名前缀误入 Path2 `growth_elastic` 池。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn03_exit96_risk06_weekly`。首次合并回测后发现池归属不对，已修正后单独重跑：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn03_exit96_risk06_weekly`。
- 修正后五窗口 CAGR `6.36% / 8.04% / 0.82% / -7.51% / 14.76%`，最大回撤 `-13.46% / -27.00% / -9.19% / -24.80% / -15.78%`，换手 `0.66x / 0.49x / 0.19x / 1.74x / 4.20x`。结论：退出缓冲没有修复 2023/2025，且 2020 回撤恶化，不替换 Path3 window winner、robust candidate 或 tracked/live/public payload。
- 为维持 Path3 active 池，本轮归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap32_hold10_turn02_exit98_risk06_weekly`；理由是同一 low-turn/exit98/risk06 邻域旧线非 winner/robust，且本轮 turn03/exit96 复核已经给出负样本。`scripts/update_weighted_winners.py` validation 继续拒绝本轮候选。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 62/62 complete`，最终 focus 转为 `risk_downshift`。下一轮第一条命令建议只做一条更低风险周频确认，若 2023/2025 仍弱则暂停该 low-turn 支线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap28_hold12_turn03_exit96_risk04_weekly`；若未注册，先加入 Path3 weekly scan，并同步归档一条非 winner/robust 弱线。

## 本轮执行计划（2026-06-22 05:23 CST）

- 上一轮预留 `cap30_hold11_turn02_exit98_risk06_weekly`，本轮保持纯 `_weekly` 口径，先归档旧弱线再五窗口确认新低单票/长持有候选；所有 A股回测显式锁定 `--end-date 2026-06-18`。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly`。实际命令与 Path1/2 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly,...`。
- 五窗口 CAGR `11.27% / 13.86% / 7.79% / 27.70% / 45.76%`，最大回撤 `-11.67% / -11.28% / -6.87% / -12.52% / -10.33%`，换手 `0.69x / 0.79x / 0.33x / 1.82x / 3.43x`。结论：相对上一轮继续压低换手和回撤，2017/2020 风险收益尚可，但 2023 CAGR 仍只有 `7.79%`，validation 低于 Path3 incumbent 要求，不晋级。
- 为维持 Path3 active 池，本轮在代码中归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold9_turn02_exit98_risk06_weekly`；理由是同一 low-turn/exit98/risk06 邻域旧线不是 winner/robust，且被本轮 `cap30/hold11` 覆盖。`scripts/update_weighted_winners.py` 明确拒绝该候选替换 Path3 `since_2017_01`/`since_2020_01`。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 62/62 complete`，Path3 window winner、robust candidate、tracked/live/public payload 未切换。最终 focus 转为 `weekly_exit_buffer`；下一轮第一条命令建议回补一点退出缓冲和允许换手，若 2023 仍弱则暂停该低 cap/长持有支线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn03_exit96_risk06_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条同形非 winner/robust 弱线。

## 本轮执行计划（2026-06-21 17:29 CST）

- 上一轮 `cap34_hold9_turn02_exit98_risk06_weekly` 恢复收益但 2023 仍弱；本轮继续按 `cost_stress` 做更低单票、更长持有的纯 `_weekly` 变体。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap32_hold10_turn02_exit98_risk06_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股 Path1/2/4 合并执行。
- 新候选五窗口 CAGR `10.79% / 14.93% / 6.81% / 29.78% / 51.87%`，最大回撤 `-24.83% / -12.78% / -7.93% / -12.80% / -10.88%`，换手 `1.38x / 0.82x / 0.42x / 1.89x / 3.47x`。结论：换手与回撤继续下降，但 2023 验证窗 CAGR 只有 `6.81%`，收益不够支撑晋级；最新持仓仍有少数票集中风险。
- 为维持 Path3 active 池，新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold8_turn02_exit99_risk06_weekly`，理由是同一 low-turn/low-risk 邻域旧线不是 winner/robust，且被本轮 `cap32/hold10/turn02/exit98` 覆盖。`scripts/update_weighted_winners.py` validation 拒绝该候选替换 Path3 `since_2020_01`，Path3 window winner、robust candidate、tracked/live/public payload 未切换。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 62/62 complete`，最终 focus 仍为 `cost_stress`。下一轮第一条命令建议只再做一条同形低成本压力测试，若 2023 仍弱则暂停该低 cap/hold10 支线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap30_hold11_turn02_exit98_risk06_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条非 winner/robust 弱线。

## 本轮执行计划（2026-06-21 05:27 CST）

- 上一轮 `cap34_hold9_turn01_exit99_risk06_weekly` 证明过度压换手会牺牲 2017-2025 收益；本轮按最终 focus `cost_stress` 回补一点出场缓冲和允许换手，新增并五窗口确认 1 个纯 `_weekly` base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold9_turn02_exit98_risk06_weekly`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path1/2/4 合并执行，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold9_turn01_exit99_risk06_weekly`，理由是同一低换手邻域旧线已被 `turn02/exit98` 覆盖，且不是 winner/robust。
- `cap34_hold9_turn02_exit98_risk06_weekly` 五窗口 CAGR `11.56% / 16.08% / 7.63% / 34.81% / 58.36%`，最大回撤 `-25.96% / -14.49% / -8.31% / -13.09% / -11.33%`，换手 `1.35x / 0.90x / 0.44x / 1.98x / 3.48x`。结论：相对上一轮 `turn01` 负样本恢复收益，但 2023 CAGR 仍不足，不能替换 Path3 window winner、robust candidate 或 tracked/live/public payload。
- `scripts/update_weighted_winners.py` 后 Path3 tracked 仍未切换；最终 coverage 为 `ashare_path3_weekly_universe 62/62 complete`，最终 focus 仍为 `cost_stress`。下一轮第一条命令建议在当前形态上继续做成本压力和单票容量压缩，而不是回到高换手周频：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap32_hold10_turn02_exit98_risk06_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条同形非 winner/robust 弱线。

## 本轮执行计划（2026-06-20 17:27 CST）

- 上一轮 `cap34_hold8_turn02_exit99_risk06_weekly` 2023 验证不足；本轮保持纯 `_weekly` 口径，新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold9_turn01_exit99_risk06_weekly`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path2 v51 合并执行。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap36_hold8_turn02_exit99_risk08_weekly`，理由是同一 exit99/低风险低换手邻域旧线不是 winner/robust，且本轮 `hold9/turn01/risk06` 覆盖更低换手压力测试。
- `cap34_hold9_turn01_exit99_risk06_weekly` 五窗口 CAGR `0.73% / 3.03% / -0.24% / 1.77% / 54.88%`，最大回撤 `-13.18% / -8.93% / -1.57% / -13.09% / -11.46%`，换手 `0.27x / 0.37x / 0.18x / 0.84x / 3.23x`。结论：换手显著下降，但 2017-2025 收益基本失效，只能作为“过度降换手损害收益”的负样本。
- `scripts/update_weighted_winners.py` validation 明确拒绝该候选替换 Path3 `since_2020_01`，原因是 validation window `since_2023_01` 低于要求；Path3 window winner、robust candidate、tracked/live/public payload 未切换。最终 coverage 为 `ashare_path3_weekly_universe 62/62 complete`。最终 focus 仍为 `weekly_exit_buffer`，下一轮第一条命令建议回补一点出场缓冲和允许换手，而不是继续压到 `turn01`：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold9_turn02_exit98_risk06_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条同形非 winner/robust 弱线。

## 本轮执行计划（2026-06-20 05:28 CST）

- 上一轮 `cap36_hold8_turn02_exit99_risk08_weekly` 继续降换手但 2023 弱；本轮保持纯 `_weekly` 口径，新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold8_turn02_exit99_risk06_weekly`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path2 v50 合并执行。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap38_hold7_turn02_exit99_risk08_weekly`，理由是同一 exit99/risk08 邻域旧线不是 winner/robust，且本轮 cap34/risk06 覆盖更低单票和更低风险方向。
- `cap34_hold8_turn02_exit99_risk06_weekly` 五窗口 CAGR `11.63% / 16.10% / 7.62% / 34.59% / 59.44%`，最大回撤 `-26.05% / -14.49% / -8.31% / -13.09% / -11.33%`，换手 `1.35x / 0.89x / 0.44x / 1.97x / 3.49x`。结论：2020 风险收益尚可，但 2023 验证窗 CAGR 只有 `7.62%`，仍不足以支撑晋级。
- `scripts/update_weighted_winners.py` validation 明确拒绝该候选替换 Path3 `since_2020_01`，原因是 validation window `since_2023_01` 低于要求；Path3 window winner、robust candidate、tracked/live/public payload 未切换。最终 coverage 为 `ashare_path3_weekly_universe 62/62 complete`。最终 focus 为 `turnover_reduction`，下一轮第一条命令建议继续压换手但避免 2023 进一步塌陷：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold9_turn01_exit99_risk06_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条同形非 winner/robust 弱线。

## 本轮执行计划（2026-06-19 17:29 CST）

- 上一轮 `cap38_hold7_turn02_exit99_risk08_weekly` 降低换手但 2023 仍弱；本轮继续保持纯 `_weekly` 口径，新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap36_hold8_turn02_exit99_risk08_weekly`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path1/2/4 合并执行，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold7_turn03_exit99_risk08_weekly`，理由是同一 exit99/risk08 邻域旧线不是 winner/robust，且本轮 cap36/hold8/turn02 覆盖更低单票和更低换手方向。
- `cap36_hold8_turn02_exit99_risk08_weekly` 五窗口 CAGR `12.44% / 16.82% / 5.85% / 36.81% / 64.42%`，最大回撤 `-26.84% / -15.75% / -9.67% / -13.37% / -12.04%`，换手 `1.46x / 1.00x / 0.59x / 2.05x / 3.54x`。结论：换手继续下降，但 2023 CAGR 低于上一轮 cap38，最新持仓仍有 `源杰科技`、`拓荆科技` 等集中风险，不晋级。
- `scripts/update_weighted_winners.py` 后 Path3 window winner、robust candidate、tracked/live/public payload 未切换；最终 coverage 为 `ashare_path3_weekly_universe 62/62 complete`。最终 focus 为 `risk_downshift`，下一轮第一条命令建议继续压风险而不是只降换手：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold8_turn02_exit99_risk06_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条同形非 winner/robust 弱线。

## 本轮执行计划（2026-06-19 05:26 CST）

- 上一轮 `cap40_hold7_turn03_exit99_risk08_weekly` 短窗强但单票集中度仍高；本轮继续保持纯 `_weekly` 口径，新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap38_hold7_turn02_exit99_risk08_weekly`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际命令与 Path2 v48 合并执行，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn03_exit99_risk08_weekly`，理由是同一 exit99/risk08 高集中度弱线已被本轮更低 cap/turnover 形态覆盖，且不是 winner/robust。
- `cap38_hold7_turn02_exit99_risk08_weekly` 五窗口 CAGR `12.90% / 16.80% / 6.60% / 38.73% / 132.63%`，最大回撤 `-26.89% / -16.20% / -10.56% / -13.66% / -15.17%`，换手 `1.47x / 1.03x / 0.61x / 2.10x / 6.58x`。结论：2026 弹性强，但 2023 收益过低，且最新持仓仍出现 `源杰科技`、`新易盛` 等少数票高集中，不适合晋级。
- `scripts/update_weighted_winners.py` 后 Path3 window winner、robust candidate、tracked/live/public payload 未切换；最终 coverage 为 `ashare_path3_weekly_universe 62/62 complete`。最终 focus 为 `weekly_exit_buffer`，下一轮第一条命令建议在低 cap/low-turn 形态上保留 exit buffer，而不是继续单纯压换手：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap36_hold8_turn02_exit99_risk08_weekly`；若未注册，先加入 Path3 weekly scan，并在新增前再归档一条同形非 winner/robust 弱线。

## 本轮执行计划（2026-06-18 17:16 CST）

- 上一轮 Path3 `cap40_hold7_turn03_exit99_risk08_weekly` 短窗强但单票集中度过高；本轮开局 focus 为 `risk_downshift`，但新增实验预算已投给 Path1/2/4 与 HK Path4-7，Path3 只完成巡检、candidate 设计和下一轮命令记录，没有新增 `--only-base-ids` 回测。
- `scripts/update_weighted_winners.py` 后 Path3 window winner、robust candidate、tracked/live/public payload 未切换；`ashare_path3_weekly_universe 62/62 complete`。本轮没有新增 evict；下一次新增前应先归档一条同形高集中度弱线，避免 weekly active 池继续膨胀。
- 最终 focus 为 `cost_stress`。下一轮候选应仍以纯 `_weekly` 结尾，不能使用 Path1 的月度选股 + weekly exposure overlay。第一条命令建议注册并确认成本压力 + 单票压缩：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap38_hold7_turn02_exit99_risk08_weekly`；若未注册，先加入 Path3 weekly scan，并同步归档一条非 winner/robust 的弱周频候选。

## 本轮执行计划（2026-06-18 05:21 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度选股 + weekly exposure overlay 纳入 Path3。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold7_turn03_exit99_risk08_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 该候选五窗口 CAGR `14.79% / 18.79% / 10.80% / 70.41% / 84.77%`，最大回撤 `-31.53% / -19.89% / -9.77% / -13.16% / -13.11%`。相对上一轮 `cap44/hold7/turn03/exit99/risk08`，它降低部分窗口回撤但最新持仓仍出现 `源杰科技` 约 `38%-41%` 单票、历史窗口也有 `拓荆科技` 约 `45%` 单票，集中度风险不适合晋级。
- 本轮无新增 evict，上一轮已归档同形弱线。`scripts/update_weighted_winners.py` 后 Path3 window winner、robust candidate、tracked/live/public payload 未切换。最终 focus 为 `weekly_exit_buffer`，下一轮第一条命令建议继续保留 exit buffer 同时进一步压单票：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap36_hold7_turn03_exit99_risk08_weekly`；若未注册，先加入 Path3 weekly scan，并在新增前归档一条同形集中度弱线。

## 本轮执行计划（2026-06-17 18:02 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度选股 + weekly exposure overlay 纳入 Path3。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn03_exit99_risk08_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 该周频候选五窗口 CAGR `14.99% / 17.92% / 10.29% / 75.38% / 93.08%`，最大回撤 `-28.67% / -20.48% / -10.43% / -13.07% / -13.18%`，换手 `1.91x / 1.36x / 0.86x / 2.50x / 3.70x`。结论：收益显著优于上一轮 `turn01` 负样本，但最新持仓出现 `源杰科技`/`拓荆科技` 40%+ 单票，容量与单票幸运风险太高，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold8_turn01_exit98_risk08_weekly`，理由是上一轮确认其 2017-2025 收益近乎失效，且本轮候选覆盖同一低风险/低换手邻域。本轮最终 focus 为 `turnover_reduction`，下一轮第一条命令建议在保留 `exit99/hold7` 的同时压单票集中：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold7_turn03_exit99_risk08_weekly`；若未注册，先加入 Path3 weekly scan，并再归档一条同形弱线以维持 active cap。

## 本轮执行计划（2026-06-17 05:20 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮 Path3 只做 weighted 同步和纯 `_weekly` 候选巡检，没有新增 Path3 `--only-base-ids` 回测，也没有把 Path1 月度选股 + weekly exposure overlay 计入 Path3。
- `scripts/update_weighted_winners.py` 后 Path3 window winner、robust candidate、tracked/live/public payload 均未切换；本轮无 Path3 evict。上一轮 `turn01/exit98/risk08` 已证明过度降换手会牺牲 2017-2025 收益，本轮不复跑同形。
- 本轮未回测原因：新增策略预算给 A股 Path4 与 HK Path4-7；Path3 完成下一候选设计但不消耗新增实验名额。
- 最终 focus 为 `risk_downshift`。下一轮第一条命令建议在 `cap44/hold7/exit99` 形态上小幅下调风险阈值，而不是继续压换手：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn03_exit99_risk08_weekly`；若未注册，先加入 Path3 weekly scan，并在新增前归档一条同形低换手弱线以维持 active cap。

## 本轮执行计划（2026-06-16 17:36 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；上一轮预留的低换手 `turn01/exit98/risk08` 纯周度候选本轮已注册并五窗口确认。执行前按计划归档旧线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold8_turn02_exit98_risk08_weekly`，理由是同一低换手 exit98/risk08 邻域已由本轮 `turn01` 覆盖。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold8_turn01_exit98_risk08_weekly`。实际命令为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- `turn01` 五窗口 CAGR 为 `-1.25% / -0.09% / -0.16% / 3.16% / 162.52%`，最大回撤 `-13.60% / -8.96% / -1.74% / -13.16% / -12.87%`，换手 `0.23x / 0.28x / 0.09x / 0.77x / 2.44x`。结论：换手极低但 2017-2025 几乎没有收益，只能作为“过度降换手导致失效”的负样本，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 最终 focus 为 `weekly_exit_buffer`，下一轮第一条命令建议回补一点换手与出场缓冲，不继续压到 `turn01`：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-15 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn03_exit99_risk10_weekly`；若未注册，先加入 weekly scan，新增前再归档一条同形弱线。

## 本轮执行计划（2026-06-16 05:17 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮没有新增 Path3 `--only-base-ids` 回测，预算投给 A股 Path2/4、Path5 事件入口和 HK Path4-7。Path3 继续只比较纯 `_weekly` 候选，没有把 Path1 月度 overlay 纳入 Path3。
- 本轮执行的 Path3 动作为巡检与 weighted 同步；`scripts/update_weighted_winners.py` 后 Path3 window winner、robust candidate、tracked/live/public payload 均未切换。本轮没有 Path3 evict。
- 候选设计：最终 focus 转为 `turnover_reduction`，下一轮仍应在 `cap40/hold8/exit98/risk08` 低换手形态上继续压换手，同时避免 2023 进一步塌陷。新增前建议归档一条旧弱线：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold8_turn02_exit98_risk08_weekly`，理由是下一候选覆盖同一 exit98/risk08 邻域。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold8_turn01_exit98_risk08_weekly`；若未注册，先加入 Path3 weekly scan 并同步归档上述旧线。

## 本轮执行计划（2026-06-15 17:18 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度 overlay 纳入 Path3。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly`，理由是本轮 `cap40/hold8/turn02/risk08` 覆盖同一低换手 exit98 邻域且旧线未改善 robust。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold8_turn02_exit98_risk08_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- `cap40_hold8_turn02_exit98_risk08_weekly` 五窗口 CAGR 为 `12.64% / 15.46% / 6.05% / 32.30% / 48.61%`，最大回撤 `-28.02% / -16.65% / -11.08% / -13.16% / -13.23%`，换手 `1.48x / 1.05x / 0.63x / 1.55x / 3.65x`。相对归档的 `cap42_hold7_turn02_exit98_risk10_weekly`，它改善 2017/2020 回撤和换手，但 2023/2026 收益下降，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 最终 focus 为 `cost_stress`。下一轮第一条命令建议继续做低换手成本压力，但不要继续牺牲 2023：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold8_turn01_exit98_risk08_weekly`；若未注册，先加入 Path3 weekly scan，并在新增前继续归档一条 2020/2023 弱线。

## 本轮执行计划（2026-06-15 05:39 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度 overlay 纳入 Path3。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit98_risk10_weekly`，理由是同一 exit98/低换手邻域已被本轮 `cap42/hold7/turn02/risk10` 覆盖，且旧线未改善 robust。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- `cap42_hold7_turn02_exit98_risk10_weekly` 五窗口 CAGR 为 `12.07% / 15.06% / 6.63% / 32.03% / 55.64%`，最大回撤 `-28.17% / -17.22% / -11.36% / -13.07% / -13.27%`。结论：换手和短窗弹性有可比性，但 2023 明显弱，且最新持仓存在单票/少数票集中风险，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 最终 focus 为 `risk_downshift`。下一轮第一条命令建议继续降低风险与集中度，但新增前仍先归档一条 2020/2023 弱线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap40_hold8_turn02_exit98_risk08_weekly`；若未注册，先加入 Path3 weekly scan。

## 本轮执行计划（2026-06-14 17:25 CST）

- 开局 guard 为 `pass`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度 overlay 纳入 Path3。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn03_exit98_risk12_weekly`，理由是同一 exit98/hold6/turn03 邻域被本轮 `cap44/risk10` 覆盖，且 cap46 未改善 robust。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit98_risk10_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，与 Path2 v39 合并执行。
- `cap44_hold6_turn03_exit98_risk10_weekly` 五窗口 CAGR 为 `15.85% / 17.11% / 9.91% / 63.70% / 61.24%`，最大回撤 `-20.73% / -20.54% / -10.32% / -13.07% / -13.18%`，换手 `1.84x / 1.44x / 0.96x / 2.51x / 3.80x`。结论：换手继续下降且短窗弹性保留，但 2023 收益低于 stable weekly robust，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 中段 guard focus 为 `turnover_reduction`。下一轮第一条命令建议继续做低换手形态，但先在 active pool 内归档一条 2020/2023 弱线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly`；若未注册，先加入 Path3 weekly scan。

## 本轮执行计划（2026-06-14 05:29 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度 overlay 纳入 Path3。新增前归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold6_turn03_exit98_risk14_weekly`，理由是同一 exit98/低换手邻域被本轮 `cap46/risk12` 覆盖，且旧线不改善 robust。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn03_exit98_risk12_weekly`。命令与 Path2/Path4 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn03_exit98_risk12_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn`。
- `cap46_hold6_turn03_exit98_risk12_weekly` 五窗口 CAGR 为 `16.32% / 16.78% / 10.44% / 64.14% / 64.97%`，最大回撤为 `-20.96% / -20.96% / -10.66% / -13.07% / -13.18%`，换手为 `1.83x / 1.51x / 1.05x / 2.51x / 3.78x`。结论：比上一轮低换手线更可用，短窗保持弹性且回撤较浅，但 2023 仍低于 stable weekly robust，不替换 Path3 weighted robust 或 tracked payload。
- 最终 focus 为 `cost_stress`。下一轮第一条命令建议继续在该低换手形态上加成本/容量压力，而不是回到高频弹性线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold6_turn03_exit98_risk10_weekly`；若未注册，先加入 Path3 weekly scan，并在新增前继续归档一条 2020/2023 弱线。

## 本轮执行计划（2026-06-13 17:30 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度 overlay 纳入 Path3。新增前已把旧 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly` 归档，理由是同一低换手 exit98 邻域被本轮 `cap48/turn03/risk14` 覆盖且不改善 robust。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold6_turn03_exit98_risk14_weekly`。命令与 Path2 v37 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold6_turn03_exit98_risk14_weekly`。
- `cap48_hold6_turn03_exit98_risk14_weekly` 五窗口 CAGR 为 `15.84% / 16.81% / 10.85% / 64.14% / 64.97%`，最大回撤为 `-21.64% / -21.64% / -10.99% / -13.07% / -13.18%`，换手为 `2.07x / 1.61x / 1.15x / 2.51x / 3.78x`。结论：低换手有效但 2020/2023 仍弱，且最新持仓存在单票/少数票集中风险，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 最终 focus 为 `risk_downshift`。下一轮第一条命令建议在该低换手形态上继续降 risk 并压集中度，而不是回到高频弹性线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn03_exit98_risk12_weekly`；若未注册，先加入 Path3 weekly scan，并在新增前继续归档一条 2020/2023 弱线。

## 本轮执行计划（2026-06-13 05:09 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮保持纯 `_weekly` 口径，没有把 Path1 月度选股 + 周度仓位 overlay 并入 Path3。上一轮预留的 `hold6/turn04/risk16` 已有五窗口结果，本轮只做结果判读和 weighted 同步，没有新增 A股 Path3 回测命令。
- 本轮候选 ID：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly`。五窗口 CAGR 为 `14.70% / 17.57% / 14.08% / 71.47% / 69.77%`，最大回撤为 `-32.75% / -23.82% / -14.62% / -13.07% / -13.00%`，换手为 `2.50x / 1.94x / 1.42x / 3.42x / 3.94x`。
- 结论：该候选相对上一轮继续压换手并保留 2025/2026 弹性，但 2017 回撤过深且 2020/2023 不及当前 stable weekly robust；`update_weighted_winners.py` 后 Path3 weighted robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly`，`meanCAGR=38.25%`、`minCAGR=14.60%`。已有代码归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly`，理由是旧线被 cost_guard/lowturn 邻域覆盖且不改善中窗。
- 本轮命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`。下一轮 focus 仍为 `turnover_reduction`，新增前应先把 active pool 压回 cap；第一条命令建议在本轮低换手形态上再降 risk/cap，而不是回到高换手弹性线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold6_turn03_exit98_risk14_weekly`；若未注册，先加入 Path3 weekly scan 并同步归档一条旧弱线。

## 本轮执行计划（2026-06-12 05:28 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度选股 + 周度仓位 overlay 并入 Path3。上一轮 `cap52_hold5_turn05_exit98_risk18_weekly` 未晋级，本轮按 `risk_downshift` 做 `cap50/risk16` 低风险对照。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit98_risk16_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 该候选五窗口 CAGR 为 `11.38% / 22.13% / 17.00% / 68.67% / 85.01%`，最大回撤为 `-28.03% / -25.33% / -14.58% / -14.92% / -12.88%`，Sharpe 为 `0.66 / 0.98 / 0.95 / 1.67 / 1.92`，换手为 `2.06x / 1.49x / 1.31x / 2.93x / 2.09x`。结论：收益不够成为 robust，但相对上一轮修复 `since_2020_01`，`scripts/update_weighted_winners.py` 后切换为 Path3 `since_2020_01` window winner。
- Path3 robust candidate 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`，`meanCAGR=29.78%`、`minCAGR=13.15%`；tracked composite 只同步 window winner 变化。为维持 active cap，本轮归档旧弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold5_turn05_exit98_risk18_weekly`，原因是新 `cap50/risk16` 已覆盖同一 exit98 成本守门邻域且改善 2020。
- 最终 guard focus 为 `turnover_reduction`。下一轮第一条命令建议只在新 2020 winner 上降换手并保留 2020/2023，不回到高换手弹性线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly`；若未注册，先加入 Path3 weekly scan 后再跑。

## 本轮执行计划（2026-06-07 16:06 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度选股 + 周度仓位 overlay 并入 Path3。上一轮 `cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly` 降回撤但中窗收益不足，本轮按 `cost_stress` 加入成本守门并收紧出场到 `exit92`。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit92_risk25_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖窗口为 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 该候选五窗口 CAGR 为 `15.94% / 15.21% / 12.83% / 35.16% / 158.69%`，最大回撤为 `-18.22% / -22.19% / -15.01% / -12.75% / -6.97%`，Sharpe 为 `0.98 / 0.80 / 0.85 / 1.36 / 3.04`，换手为 `1.51x / 1.27x / 1.16x / 0.68x / 5.96x`。结论：成本守门保持低换手与浅回撤，但 2020/2023 收益仍不够，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 为维持 active cap `60`，本轮归档旧弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly`；原因是新 cost_guard 版本覆盖同一 risk25/turn04 邻域，且旧线 2020/2023 不足。本轮没有其它 Path3 evict。
- 最终 guard 将下一轮 focus 推到 `weekly_exit_buffer`。下一轮第一条命令建议只在当前成本守门低换手形态上放宽退出缓冲：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit94_risk25_weekly`；若未注册，先加入 Path3 weekly scan 后再跑。

## 本轮执行计划（2026-06-07 04:26 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度选股 + 周度仓位 overlay 并入 Path3。上一轮 `cap58_hold4_turn03_exit96_weekly` 低换手但中窗弱，本轮按 `risk_downshift` 做 `turn04/exit94/risk25` 对照。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，实际命令见 Path2 本轮记录。
- 该候选五窗口 CAGR 为 `14.88% / 15.12% / 12.83% / 35.16% / 158.69%`，最大回撤为 `-18.22% / -22.19% / -15.01% / -12.75% / -6.97%`，Sharpe 为 `0.95 / 0.80 / 0.85 / 1.36 / 3.04`，换手为 `1.51x / 1.26x / 1.16x / 0.68x / 5.96x`。结论：回撤与低换手较上一轮改善，但 2020/2023 收益仍低于 Path3 robust，不替换 window winner、robust candidate 或 tracked payload。
- 为维持 active cap `60`，本轮归档旧弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn03_exit96_weekly`；原因是本轮 `risk25/turn04/exit94` 已覆盖同一低换手退出缓冲邻域，且旧线 2020/2023 不足。本轮没有其它 Path3 evict。
- 最终 guard 将下一轮 focus 推到 `cost_stress`。下一轮第一条命令建议在 current risk25 形态上加入成本守门或更低 turnover，不要回到 2026 弹性线：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit92_risk25_weekly`；若未注册，先加入 Path3 weekly scan 后再跑。

## 本轮执行计划（2026-06-06 16:17 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度选股 + 周度仓位 overlay 并入 Path3。上一轮 `cap55_hold3_turn04_exit94_weekly` 降换手但 2020/2023 塌陷，本轮按 `weekly_exit_buffer` 放宽到 `cap58/hold4/turn03/exit96`。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn03_exit96_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，A股实际合并命令见 Path1 本轮记录。
- 该候选五窗口 CAGR 为 `9.51% / 14.28% / 8.73% / 34.94% / 98.13%`，最大回撤为 `-22.88% / -28.10% / -20.55% / -14.82% / -12.55%`，Sharpe 为 `0.59 / 0.70 / 0.55 / 1.22 / 2.03`，换手为 `1.58x / 1.36x / 1.06x / 1.79x / 3.81x`。结论：换手极低且 2026 弹性强，但 2020/2023 收益明显不足，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 本轮为保持 active cap，归档旧弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn04_exit94_weekly`；原因是其 2020/2023 已塌陷，且本轮 `cap58/hold4/turn03/exit96` 已覆盖低换手退出缓冲对照。本轮没有其它 Path3 evict。
- 最终 guard 将下一轮 focus 推到 `risk_downshift`。下一轮第一条命令建议在本轮低换手基础上做浅风险降档，目标是修复 2020/2023 而不是继续追 2026：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly`；若未注册，先加入 Path3 weekly scan 后再跑。

## 本轮执行计划（2026-06-06 10:28 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`；本轮继续只比较纯 `_weekly` 候选，没有把 Path1 月度选股 + 周度仓位 overlay 并入 Path3。上一轮 cap55/hold3/turn06 仍不改善 2023，本轮沿 `turnover_reduction` 把 `turn06` 降到 `turn04` 并收紧 `exit94`。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn04_exit94_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path1 本轮记录。
- 该候选五窗口 CAGR 为 `12.08% / 12.99% / 10.52% / 29.18% / 88.22%`，最大回撤为 `-24.51% / -26.91% / -19.37% / -14.65% / -11.85%`，换手为 `1.93x / 1.57x / 1.11x / 1.88x / 3.94x`。结论：换手明显下降且 2026 弹性恢复，但 2020/2023 收益塌陷，不替换 Path3 window winner、robust candidate 或 tracked payload。
- 本轮为保持 active cap，归档旧弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn06_exit92_weekly`；原因是其 2023 不足且已由 cap55/hold3 邻域的新低换手对照覆盖。本轮没有其它 Path3 evict。
- 最终 guard 将下一轮 focus 轮到 `weekly_exit_buffer`。下一轮第一条命令建议在低换手基础上放宽退出缓冲，要求 2020/2023 不再塌陷：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn03_exit96_weekly`；若未注册，先加入 Path3 weekly scan 后再跑。

## 本轮执行计划（2026-06-06 04:23 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`；本轮继续保持纯 `_weekly` 口径，没有把 Path1 月度选股 + 周度仓位 overlay 计入 Path3。上一轮 `cap60_hold3_turn06_exit92_weekly` 修复 2020 但 2023 不足，本轮按 `risk_downshift/cost_stress` 把单票上限压到 `55%`。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn06_exit92_weekly`。命令为：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn06_exit92_weekly`。
- 该候选五窗口 CAGR 为 `12.03% / 22.68% / 19.66% / 81.69% / 72.20%`，最大回撤为 `-23.84% / -26.51% / -22.50% / -13.65% / -11.45%`，换手为 `2.96x / 2.34x / 2.19x / 3.53x / 5.75x`。结论：2020 与 2026 弹性可用，但 2023 仍低于 stable weekly robust，不替换 Path3 winner/robust/tracked。
- 为把 active pool 压回 cap `60`，本轮归档 3 条旧弱线：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly`；原因是 2020/2023 弱且已被 hold3/turn06/exit92 新线覆盖。
- 最终 rotation focus 为 `cost_stress`。下一轮第一条命令建议在本轮 cap55/hold3/turn06 形态上加成本守门或更紧 exit，而不是回到 pullback 弱线：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap55_hold3_turn06_exit90_weekly`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-05 22:21 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 62/62 complete`；本轮继续保持纯 `_weekly` 口径，没有把 Path1 月度选股 + 周度仓位 overlay 计入 Path3。
- 本轮按上一轮 `weekly_exit_buffer` 提示新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn06_exit92_weekly`。命令为：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn06_exit92_weekly`。
- 该候选五窗口 CAGR 为 `11.42% / 22.68% / 19.66% / 81.69% / 72.20%`，最大回撤 `-23.84% / -26.51% / -22.50% / -13.65% / -11.45%`，换手 `2.94x / 2.34x / 2.19x / 3.53x / 5.75x`。它明显修复 2020，相比上一轮 `turn05_exit94` 也恢复短窗弹性，但 2023 仍低于 stable weekly robust，不替换 Path3 robust/tracked。
- 本轮未新增归档；旧 weak pullback/cashoff 归档继续保留。最终 rotation focus 为 `risk_downshift`，下一轮第一条命令建议在当前 hold3/turn06/exit92 上做浅风险降档或 cap 下调，验收重点是 2020 不回落且 2023 不低于 robust：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn06_exit92_weekly`；若未注册，先加入 Path3 weekly scan 后再跑。

## 本轮执行计划（2026-06-05 10:22 CST）

- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 61/61 complete`；本轮保持纯 `_weekly` 口径，没有把 Path1 月度选股 + 周度 overlay 误并入 Path3。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path1 本轮记录。
- 该候选五窗口 CAGR 为 `17.56% / 19.15% / 11.76% / 37.95% / 81.77%`，最大回撤 `-25.37% / -26.28% / -21.04% / -13.32% / -11.56%`，换手 `2.21x / 1.92x / 1.22x / 2.07x / 4.10x`。它切换为 Path3 `since_2017_01` window winner，但 2023 收益不足，不能替换 2023/2020 winner 或 robust candidate。
- `scripts/update_weighted_winners.py` validation 明确拒绝该候选作为 2020 winner，原因是验证窗口 `since_2023_01` 的 CAGR 低于要求。本轮未新增归档；上一轮已归档的弱 pullback/cashoff 线继续保留归档状态。
- 最新 rotation focus 为 `turnover_reduction`，但本轮说明单纯降换手会牺牲 2023。下一轮第一条命令建议在本轮 winner 上稍放松出场或恢复 2023 暴露：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn06_exit92_weekly`；若未注册，先加入 Path3 weekly scan，验收重点是 `since_2023_01` 不低于当前 robust，同时换手不回到高频过度区间。

## 本轮执行计划（2026-06-05 04:11 CST）

- 最新 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`；本轮保持纯 `_weekly` 口径，没有把 Path1 的月度 overlay 混入 Path3。
- 本轮纳入并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 该候选五窗口 CAGR 为 `16.12% / 17.87% / 8.29% / 68.93% / 115.86%`，最大回撤为 `-27.21% / -26.87% / -27.01% / -17.34% / -6.65%`，换手为 `2.71x / 2.13x / 1.89x / 4.00x / 7.07x`。`scripts/update_weighted_winners.py` 后它切换为 Path3 `since_2017_01` window winner，但 `since_2023_01` 明显塌陷，robust candidate 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`。
- 本轮从 active/scan 归档 3 条旧 pullback/cashoff 弱线：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold4_turn16_exit85_weekly`、`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly`；原因是 2020/2023 弱且已被 cap60/cash_off 邻域覆盖。
- 最新 rotation focus 为 `turnover_reduction`。下一轮第一条命令建议沿本轮 winner 降换手但修复 2023：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-04 16:16 CST）

- 开局 guard 为 `pass`，`ashare_path3_weekly_universe` 为 `61/61 complete`。本轮继续保持纯 `_weekly` 口径，没有把 Path1 的月度选股 + 周度仓位 overlay 混入。
- 本轮新增并五窗口确认 1 个 Path3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly`。该 id 相比上一轮 Path3 robust `cap60_hold2_turn12_exit92_weekly` 延长持仓到 3 周、降低换手阈值到 8%，用于验证降换手是否保住 2020/2023。
- 五窗口 CAGR 为 `12.70% / 16.47% / 13.34% / 77.81% / 23.71%`，最大回撤为 `-25.19% / -29.06% / -25.67% / -16.32% / -11.60%`，换手为 `3.35x / 2.85x / 2.63x / 5.08x / 4.80x`。`scripts/update_weighted_winners.py` validation 显示其 `since_2020_01` 未达晋级要求，不替换 Path3 window winner 或 robust。
- 本轮已归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit90_weekly`，原因是旧 cap50/exit90 线短窗弹性不足且已被 cap60/exit92 邻域覆盖。最终 guard 将下一轮 focus 轮到 `risk_downshift`，第一条命令建议注册并确认低风险/低换手版：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn08_exit92_weekly`。

## 本轮执行计划（2026-06-04 10:16 CST）

- 开局 guard 为 `pass`，`ashare_path3_weekly_universe` 已完整；上一轮计划的 `cash_off_and_cap60_hold2_turn12_exit90_weekly` 本轮按纯 `_weekly` 要求五窗口确认，没有把月度 overlay 误算进 Path3。
- 本轮新增并确认 1 个 Path3 base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly`。实际命令见 Path1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 五窗口 CAGR 为 `13.57% / 11.25% / 13.26% / 76.83% / 99.57%`，最大回撤为 `-26.57% / -28.81% / -26.79% / -16.79% / -9.81%`。它显著强化 2025/2026 短窗，但 2020/2023 仍低于既有 stable weekly robust，且 2026 换手升到约 `9x`，不替换 Path3 window winner 或 robust。
- `scripts/update_weighted_winners.py` 后 Path3 window winner/robust/tracked 未切换；本轮未归档新增候选，先列入下一轮待观察。候选池 active cap 未触发 evict。
- 下一轮 focus 继续 `weekly_exit_buffer`，但不要追更高 2026 弹性。第一条命令建议回到 `cap55/60 + hold2 + turn10/12` 的 2020/2023 修复对照：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold2_turn10_exit90_weekly`；若未注册，先注册后再用 `--only-base-ids`。

## 本轮执行计划（2026-06-03 22:20 CST）

- 开局与最新 guard 的 Path3 coverage 均为 `60/60 complete`；本轮未追加 Path3 回测，预算优先给 Path4 blocking、Path1 warning 与 HK 增量。Path3 已完成巡检：`scripts/update_weighted_winners.py` 后 window winner、robust candidate 和 tracked payload 均未切换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。
- `recommended_focus=cost_stress`，本轮候选设计回到更接近既有 winner 的 `cash_off_and_weekly` 邻域，而不是继续 pullback 低换手链条。已注册但未回测的纯 `_weekly` 候选为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly`，对照已在 CSV 中存在的 `cap50_hold2_turn12_exit90_weekly`（四窗口 CAGR `14.60% / 12.04% / 14.89% / 80.01%`，换手 `3.78x / 3.72x / 3.48x / 6.39x`）。
- 本轮没有新增 Path3 归档；候选池 active cap 未触发 evict。下一轮第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly`。验收重点是 `since_2020_01/since_2023_01` 是否能超过既有 stable weekly，同时换手不能重新回到高频过度区间。

## 本轮执行计划（2026-06-02 16:20 CST）

- 开局 guard 为 `pass`；上一轮 `risk20_cap66_hold7_turn04_exit94_weekly` 只保留 2026 弹性，2020/2023/2025 都失效。本轮新增前将它加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是 `since_2020_01 CAGR=1.75%`、`since_2025_01 CAGR=1.23%` 且不改善 robust；随后按 `turnover_reduction` 注册 `cap68/hold6/turn08/exit90` 成本守门版，测试略放宽换手后能否恢复 2020 暴露。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold6_turn08_exit90_weekly`。增量确认命令见 Path 2 本轮记录，命令类型为五窗口 `--only-base-ids`。
- `cost_guard_cap68_hold6_turn08_exit90_weekly` 五窗口 CAGR 为 `11.05% / 2.45% / 5.26% / 19.88% / 49.83%`，最大回撤为 `-31.22% / -37.94% / -32.59% / -22.67% / -15.19%`，换手为 `3.41x / 3.80x / 3.93x / 4.70x / 7.23x`。它仍未修复 2020/2023，换手回升但收益没有跟上，不替换 Path 3 winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整，`scripts/update_weighted_winners.py` 后 Path 3 tracked/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk20_cap66_hold7_turn04_exit94_weekly`。
- 最新 guard 为 `pass`，下一轮 focus 为 `turnover_reduction`。第一条命令建议不要再沿 pullback 低换手链条微调，改回更接近既有 winner 的 `cash_off_and_weekly` 或 `core_6_1_full_risk_cap60_weekly` 邻域做低换手约束：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_id>`。

## 本轮执行计划（2026-06-02 13:49 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap66_hold7_turn04_exit96_weekly` 与 exit94 近似，仍没修复 2020/2026。本轮新增前将 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit96_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是 `since_2020_01 CAGR=6.77%`、`since_2026_01 CAGR=-14.61%` 且不改善 robust；随后按 `risk_downshift` 测试同一 `cap66/hold7/turn04` 的 `risk20/exit94` 纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk20_cap66_hold7_turn04_exit94_weekly`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `risk20_cap66_hold7_turn04_exit94_weekly` 五窗口 CAGR 为 `9.33% / 1.75% / 3.22% / 1.23% / 40.84%`，最大回撤为 `-29.16% / -41.07% / -23.91% / -26.02% / -15.03%`，换手为 `2.60x / 2.72x / 2.63x / 3.68x / 6.15x`。风险降档只保留 2026 正弹性，2020/2023/2025 都失效，不替换 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；最终 guard 口径 `ashare_path3_weekly_universe 60/60 complete`。`scripts/update_weighted_winners.py` 后 Path 3 tracked/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit96_weekly`。
- 下一轮 focus 为 `cost_stress`。第一条命令建议先把本轮 `risk20...exit94_weekly` 列入待归档观察，再停止继续 risk_downshift；改测成本压力但恢复 2020 暴露质量，例如更接近既有 winner 的 cashoff/cost guard 对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-06-02 04:20 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap66_hold7_turn04_exit94_weekly` 2020 和 2026 失败。本轮新增前将它加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是 `since_2020_01 CAGR=6.77%`、`since_2026_01 CAGR=-14.61%` 且不改善 robust；随后按开局 `weekly_exit_buffer` 在同一 cap/hold/turn 线上把 exit 放宽到 `96`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit96_weekly`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap66_hold7_turn04_exit96_weekly` 五窗口 CAGR 为 `15.08% / 6.77% / 26.47% / 21.50% / -14.61%`，最大回撤为 `-27.04% / -32.14% / -28.18% / -25.95% / -18.56%`，换手为 `2.58x / 2.20x / 2.42x / 5.19x / 8.50x`。它与 exit94 近似，没有修复 2020/2026，只保留 2023 中等弹性，不替换 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；最终 guard 口径 `ashare_path3_weekly_universe 60/60 complete`。`scripts/update_weighted_winners.py` 后 Path 3 tracked/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit94_weekly`。
- 下一轮 focus 为 `risk_downshift`。第一条命令建议不要继续放宽 exit，改测同一低换手形态的浅风险/回撤触发版本，且新增前若 exit96 仍无改善应列入待归档：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-06-01 22:30 CST）

- 开局 guard 为 `pass`；上一轮 `risk25_cap64_hold8_turn03_exit92_weekly` 只保留 2026 弹性、2020/2023 失败。本轮新增前把 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是同一 cap/hold 线的成本守门版 2020 弱且不改善 robust；随后按 `turnover_reduction` 测试 cashoff + `exit94` 的纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit94_weekly`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap66_hold7_turn04_exit94_weekly` 五窗口 CAGR 为 `15.08% / 6.77% / 26.41% / 21.48% / -14.61%`，最大回撤为 `-27.04% / -32.14% / -28.18% / -25.97% / -18.56%`，换手为 `2.58x / 2.20x / 2.42x / 5.19x / 8.50x`。它在 `since_2023_01` 的纯 weekly 子池排名靠前，但 2020 和 2026 失败，不能替换 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；最终 guard 口径 `ashare_path3_weekly_universe 60/60 complete`。`scripts/update_weighted_winners.py` 后 Path 3 window winner/robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly`；本轮新增候选列入下一轮待归档观察。
- 最终 guard 把下一轮 focus 轮换为 `weekly_exit_buffer`。第一条命令建议不要继续单纯降低换手，改在 `cap66/hold7/turn04` 上用退出缓冲修复 2020 和 2026，例如更宽 exit 叠加回撤触发：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_weekly_exit_buffer_id>`。

## 本轮执行计划（2026-06-01 10:27 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap64_hold8_turn03_exit94_weekly` 宽出场只改善 2017/2026，2020/2023 仍弱。本轮新增前已将它加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是 `since_2020_01 CAGR=7.00%`、`since_2023_01 CAGR=17.93%` 且不改善 robust；随后按 `risk_downshift` 测试同一 `cap64/hold8/turn03` 的 `risk25/exit92` 纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly`。
- `risk25_cap64_hold8_turn03_exit92_weekly` 五窗口 CAGR 为 `8.21% / 0.48% / 1.85% / 15.46% / 74.90%`，最大回撤为 `-27.89% / -38.70% / -25.96% / -17.32% / -10.18%`，换手为 `2.45x / 2.72x / 2.60x / 2.87x / 3.68x`。风险降档只保留 2026 弹性，2020/2023 基本失效，不晋级。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；最终 guard 口径 `ashare_path3_weekly_universe 60/60 complete`。`scripts/update_weighted_winners.py` 后 Path 3 window winner/robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap64_hold8_turn03_exit94_weekly`；当前 `risk25...exit92_weekly` 列入下一轮待归档观察。
- 下一轮 focus 为 `cost_stress`。第一条命令建议先归档本轮 `risk25...exit92_weekly`，然后改测成本压力但提高 2020 暴露质量，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-06-01 04:18 CST）

- 开局 guard 为 `pass`；上一轮 `cost_guard_cap64_hold8_turn03_exit90_weekly` 换手低但 2020/2023 收益不足。本轮新增前把它加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是 `since_2020_01 CAGR=0.47%` 且不改善 robust；随后按 `weekly_exit_buffer/turnover_reduction` 改测同一 `cap64/hold8/turn03` 的现金防守宽出场 `exit94`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap64_hold8_turn03_exit94_weekly`。实际 A股增量命令见 Path 2 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap64_hold8_turn03_exit94_weekly` 五窗口 CAGR 为 `15.24% / 7.00% / 17.93% / 30.57% / 24.33%`，最大回撤为 `-23.20% / -23.83% / -30.07% / -23.66% / -13.52%`，换手为 `2.34x / 1.60x / 1.74x / 4.33x / 6.03x`。宽出场与现金防守改善 2017/2026，但 2020/2023 仍明显弱于当前 Path 3 robust，不晋级。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整，guard 口径 `ashare_path3_weekly_universe 59/59 complete`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap64_hold8_turn03_exit90_weekly`。
- 下一轮 focus 为 `risk_downshift`。第一条命令建议不要再只放宽 exit，在同一低换手框架上测试风险降档或回撤触发，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-31 22:26 CST）

- 开局 guard 为 `pass`；上一轮 `risk25_cap62_hold9_turn02_exit94_weekly` 2020/2023 更弱，本轮先把它加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，evict/归档原因是 `since_2020_01 CAGR=-3.89%` 且不改善 robust。随后按 `turnover_reduction/cost_stress` 新增纯 `_weekly` 的 `cost_guard_cap64_hold8_turn03_exit90`，目标是在更低换手下恢复 2020/2023 暴露。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap64_hold8_turn03_exit90_weekly`。可复现实验命令见 Path 2 合并命令，命令类型为五窗口 `--only-base-ids` 增量确认。
- 该候选五窗口 CAGR 为 `6.87% / 0.47% / 13.14% / 17.02% / 78.90%`，最大回撤为 `-35.52% / -35.67% / -21.28% / -19.59% / -10.18%`，换手为 `2.33x / 2.36x / 2.70x / 2.88x / 3.75x`。换手确实低于高频 winner，但 2020/2023 收益仍显著不足，只保留 2026 观察弹性，不晋级。
- `scripts/update_weighted_winners.py` 后 Path 3 window winner/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`；`scripts/path2_candidate_pass.py` 后 weekly family 为 `75`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap62_hold9_turn02_exit94_weekly`。
- 下一轮 focus 继续围绕 `turnover_reduction`，但不要再单纯拉长持有/降换手；第一条命令建议回到更强 2020 暴露的 `cashoff/cost_guard` 形态并做轻成本压力：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_quality_id>`。

## 本轮执行计划（2026-05-31 16:20 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap62_hold9_turn02_exit94_weekly` 只保留 2026 弹性、2020/2023 明显弱。本轮新增前将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是 2020 CAGR 仅 `0.77%` 且不改善 robust；随后按 `risk_downshift` 测试同一低换手形态的 `risk25` 版本。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap62_hold9_turn02_exit94_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap62_hold9_turn02_exit94_weekly`。
- `risk25_cap62_hold9_turn02_exit94_weekly` 五窗口 CAGR 为 `9.12% / -3.89% / 3.56% / 8.16% / 68.77%`，最大回撤为 `-31.18% / -43.24% / -19.85% / -20.77% / -10.43%`，换手为 `1.72x / 2.24x / 1.80x / 1.50x / 3.31x`。风险降档进一步牺牲 2020/2023，仅保留 2026 弹性，不晋级。
- `scripts/path2_candidate_pass.py` 后 weekly family 为 `74`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold9_turn02_exit94_weekly`。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `cost_stress`。下一轮新增前应先把本轮 `risk25_cap62_hold9_turn02_exit94_weekly` 列入待归档观察；第一条命令建议停止继续降风险，改测成本压力但提高 2020 暴露质量：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-31 10:26 CST）

- 开局 guard 为 `pass`；上一轮 focus 为 `weekly_exit_buffer`，本轮先把 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn02_exit92_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是 2020 为负且不改善 robust；随后测试更宽退出的纯 `_weekly` 现金防守版本。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold9_turn02_exit94_weekly`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap62_hold9_turn02_exit94_weekly` 五窗口 CAGR 为 `11.20% / 0.77% / 9.08% / 25.00% / 99.26%`，最大回撤为 `-46.73% / -33.72% / -27.44% / -20.63% / -10.43%`，换手为 `1.73x / 1.54x / 1.35x / 2.57x / 4.21x`。它保留低换手与 2026 弹性，但 2020/2023 仍明显弱，不晋级。
- `scripts/path2_candidate_pass.py` 后 weekly family 为 `73`，`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮新增候选列入下一轮待归档观察。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60` 完整，下一轮 focus 轮换为 `risk_downshift`。第一条命令建议不要继续只放宽 exit，改在低换手现金防守形态上降风险或提高 2020 暴露质量：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-31 04:21 CST）

- 开局 guard 为 `pass`；上一轮要求从 `cost_stress` 改测低换手成本压力。本轮新增前已把 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap58_hold10_turn02_exit94_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是 2020 为负且 2023 仅 `1.04%`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn02_exit92_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn02_exit92_weekly`。
- `cost_guard_cap60_hold9_turn02_exit92_weekly` 五窗口 CAGR 为 `13.09% / -3.03% / 3.61% / 9.20% / 72.09%`，最大回撤为 `-27.90% / -40.26% / -25.43% / -20.79% / -10.35%`，换手为 `1.49x / 1.87x / 1.91x / 1.55x / 3.40x`。它只保留 2026 弹性和低换手，2020/2023 失败，不晋级。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮新增候选列入下一轮待归档观察。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 轮换为 `weekly_exit_buffer`。第一条命令建议在低换手框架上放宽退出而不是继续成本守门，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold9_turn02_exit94_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_weekly_exit_buffer_id>`。

## 本轮执行计划（2026-05-30 22:20 CST）

- 开局 guard 为 `pass`；上一轮低换手 `cashoff_cap58_hold10_turn02_exit94_weekly` 2023 仍弱，本轮新增前将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2023 CAGR 仅 `8.91%` 且不改善 robust。随后按 `risk_downshift` 改测 `risk25/cap58/hold10/turn02/exit94` 纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap58_hold10_turn02_exit94_weekly`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `risk25_cap58_hold10_turn02_exit94_weekly` 五窗口 CAGR 为 `9.43% / -3.41% / 1.04% / 8.05% / 67.64%`，最大回撤为 `-27.20% / -41.58% / -26.17% / -20.94% / -10.34%`，换手为 `1.67x / 2.46x / 1.98x / 1.50x / 3.33x`。风险降档牺牲了 2020/2023，除 2026 外没有可用改善，不晋级。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；`scripts/update_weighted_winners.py` 后 Path 3 window winner/robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold10_turn02_exit94_weekly`。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 轮换为 `cost_stress`。下一轮新增前应把本轮 `risk25_cap58_hold10_turn02_exit94_weekly` 列入待归档观察；第一条命令建议停止继续降风险，改测低换手成本压力但提高中窗暴露，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn02_exit92_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-30 16:22 CST）

- 开局 guard 为 `pass`；上一轮 `cost_guard_cap55_hold10_turn03_exit92_weekly` 2020 转负，本轮新增前已将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2023 不改善 robust 且成本守门只强化 2026。随后按 `turnover_reduction/weekly_exit_buffer` 改测 `cashoff_cap58/hold10/turn02/exit94`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold10_turn02_exit94_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold10_turn02_exit94_weekly`。
- `cashoff_cap58_hold10_turn02_exit94_weekly` 五窗口 CAGR 为 `11.06% / 12.25% / 8.91% / 33.18% / 97.92%`，最大回撤为 `-45.81% / -33.02% / -27.40% / -20.80% / -10.34%`，换手为 `1.68x / 2.51x / 1.35x / 2.57x / 4.23x`。它显著压低 2023 换手并修复 2026 弹性，但 2017/2020 回撤太深、2023 CAGR 低，不替换 Path 3 winner/robust。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；`scripts/update_weighted_winners.py` 后 Path 3 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`，tracked payload 未被本轮候选替换。本轮归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold10_turn03_exit92_weekly`。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 轮换为 `risk_downshift`。下一轮新增前应先把本轮候选列入待归档观察，理由是 2023 CAGR 仅 `8.91%`；第一条命令建议在同一低换手框架下降风险暴露，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap58_hold10_turn02_exit94_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-30 10:17 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap55_hold10_turn03_exit94_weekly` 低换手但 2023 回撤仍深。本轮新增前已将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2023 不改善 robust 且 2026 弹性不足；随后按 `cost_stress` 改测同一 `cap55/hold10/turn03` 形态的成本守门版。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold10_turn03_exit92_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold10_turn03_exit92_weekly`。
- `cost_guard_cap55_hold10_turn03_exit92_weekly` 五窗口 CAGR 为 `8.13% / -0.24% / 12.09% / 22.80% / 75.39%`，最大回撤为 `-35.21% / -36.87% / -23.63% / -19.59% / -10.20%`，换手为 `2.41x / 2.57x / 2.73x / 2.97x / 3.69x`。成本守门只强化 2026，2020 转负且 2023 收益弱，不替换 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold10_turn03_exit94_weekly`。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 轮换为 `turnover_reduction`。下一轮新增前应先归档本轮 `cost_guard_cap55_hold10_turn03_exit92_weekly`，理由是 2020 CAGR 为负；第一条命令建议测试低换手但放松退出的现金防守对照，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold10_turn02_exit94_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_weekly_id>`。

## 本轮执行计划（2026-05-30 04:31 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap60_hold10_turn03_exit92_weekly` 2020/2023 仍弱，本轮新增前将其归档，理由是 2020 CAGR 仅 `7.89%` 且 2026 弹性不足。随后按 `turnover_reduction/weekly_exit_buffer` 把单票 cap 降到 `55`、退出放宽到 `exit94`，继续只在纯 `_weekly` Path 3 内比较。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold10_turn03_exit94_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold10_turn03_exit94_weekly`。
- `cashoff_cap55_hold10_turn03_exit94_weekly` 五窗口 CAGR 为 `14.43% / 15.17% / 15.03% / 58.88% / 21.90%`，最大回撤为 `-31.02% / -24.34% / -32.44% / -13.83% / -13.52%`，换手为 `2.32x / 2.47x / 1.89x / 4.03x / 5.97x`。它保留低换手，但 2023 回撤仍深，2026 弹性也不足以补偿，不替换 Path 3 winner/robust。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；最终 guard `ashare_path3_weekly_universe 60/60 complete`。`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold10_turn03_exit92_weekly`。
- 下一轮 focus 为 `risk_downshift`。下一轮新增前应先把本轮候选列入待归档观察，理由是 2023 MaxDD `-32.44%` 且不改善 robust；第一条命令建议在 `cap55/hold10/turn03/exit94` 上降低风险暴露，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap55_hold10_turn03_exit94_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_weekly_id>`。

## 本轮执行计划（2026-05-29 22:21 CST）

- 开局 guard 为 `pass`；上一轮 `cost_guard_cap60_hold9_turn03_exit90_weekly` 的 2020 CAGR 仅 `2.10%`，本轮新增前将其归档，理由是 2020/2023 均不改善 robust。随后按 `weekly_exit_buffer` 测试更长持有 `hold10`、现金防守与 `exit92` 的纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold10_turn03_exit92_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold10_turn03_exit92_weekly`。
- `cashoff_cap60_hold10_turn03_exit92_weekly` 五窗口 CAGR 为 `14.53% / 7.89% / 15.03% / 58.69% / 22.68%`，最大回撤为 `-31.02% / -23.78% / -32.44% / -14.30% / -13.52%`，换手为 `2.34x / 1.73x / 1.89x / 4.04x / 5.96x`。它把换手压低且改善 2025，但 2020/2023 仍不够，2026 弹性也低于近期候选。
- `scripts/update_weighted_winners.py` 后 Path 3 window winner、robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn03_exit90_weekly`；最终 guard `ashare_path3_weekly_universe 60/60 complete`。
- 下一轮 focus 为 `turnover_reduction`。新增前应先归档本轮 `cashoff_cap60_hold10_turn03_exit92_weekly`，理由是 2020 CAGR 只有 `7.89%` 且 2026 弹性不足；第一条命令建议在低换手框架下改测 `cap55/hold10/turn03/exit94` 或 risk30 对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_weekly_id>`。

## 本轮执行计划（2026-05-29 16:33 CST）

- 开局 guard 完成 Path 4 blocking 后，Path 3 按上一轮 `cost_stress` 只用增量 `--only-base-ids`。上一轮 `risk30_cap60_hold9_turn03_exit92_weekly` 2020/2023 仍弱，本轮新增前将其归档，理由是 2020 CAGR `7.07%`、2023 CAGR `10.97%` 且不改善 robust；active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn03_exit90_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn03_exit90_weekly`。
- `cost_guard_cap60_hold9_turn03_exit90_weekly` 五窗口 CAGR 为 `7.91% / 2.10% / 12.34% / 16.07% / 76.54%`，最大回撤为 `-34.02% / -32.50% / -22.15% / -17.50% / -10.38%`，换手为 `2.33x / 2.48x / 2.70x / 2.89x / 3.69x`。它降低换手并保留 2026 弹性，但 2020/2023 坍塌，不替换 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 weekly family 完整；最终 guard `ashare_path3_weekly_universe 60/60 complete`。`scripts/update_weighted_winners.py` 后 Path 3 tracked/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold9_turn03_exit92_weekly`。
- 下一轮 focus 轮换为 `weekly_exit_buffer`。下一轮新增前应先归档本轮 `cost_guard_cap60_hold9_turn03_exit90_weekly`，理由是 2020 CAGR 仅 `2.10%`；第一条命令建议测试同一低换手框架的更宽退出缓冲或现金防守，而不是继续成本守门，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold10_turn03_exit92_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_weekly_exit_buffer_id>`。

## 本轮执行计划（2026-05-29 10:22 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap60_hold9_turn03_exit94_weekly` 2023 CAGR 仅 `0.58%`，本轮新增前已将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，active weekly universe 维持 cap `60`。随后按 `risk_downshift` 在同一低换手形态上把熊市暴露改为 `30%`、退出收紧到 `exit92`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold9_turn03_exit92_weekly`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold9_turn03_exit92_weekly`。
- `risk30_cap60_hold9_turn03_exit92_weekly` 五窗口 CAGR 为 `12.02% / 7.07% / 10.97% / 16.54% / 91.99%`，最大回撤为 `-26.48% / -29.67% / -25.16% / -19.31% / -10.38%`，换手为 `2.56x / 2.81x / 2.94x / 3.05x / 4.12x`。风险降档修复 2026 弹性，但 2020/2023/2025 仍弱，不替换 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=66`；最终 guard 的 `ashare_path3_weekly_universe` 仍为 `60/60 complete`。本轮 evict/归档：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly`，原因是 2023 近乎失效且不改善 robust。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `cost_stress`。下一轮新增前应先归档本轮 `risk30_cap60_hold9_turn03_exit92_weekly`，理由是 2020 CAGR 只有 `7.07%`、2023 只有 `10.97%`；第一条命令建议测试同一低换手形态的成本守门/更宽退出对照，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold9_turn03_exit90_weekly`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-29 04:17 CST）

- 开局 guard 为 `pass`；上一轮 `cost_guard_cap60_hold8_turn04_exit90_weekly` 继续 2020/2023 坍塌，本轮新增前已将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，active weekly universe 维持 cap `60`。随后按 `weekly_exit_buffer/turnover_reduction` 测试更低换手、更长持有的现金防守纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly`。
- `cashoff_cap60_hold9_turn03_exit94_weekly` 五窗口 CAGR 为 `13.78% / 12.59% / 0.58% / 14.72% / 37.19%`，最大回撤为 `-29.22% / -33.67% / -35.86% / -22.77% / -10.38%`，换手为 `2.33x / 2.02x / 2.15x / 4.46x / 6.28x`。低换手目标达成，但 2023 几乎失效，且 2025 弹性不足，不替换 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=65`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`cost_guard_cap60_hold8_turn04_exit90_weekly`，原因是 2020 CAGR 仅 `2.43%`、2023 仅 `7.41%`。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 轮换为 `risk_downshift`。下一轮新增前应先归档本轮 `cashoff_cap60_hold9_turn03_exit94_weekly`，理由是 2023 CAGR 仅 `0.58%` 且不改善 robust；第一条命令建议在同一低换手框架上降低风险暴露，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold9_turn03_exit92_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-28 22:19 CST）

- 开局 guard 为 `pass`；上一轮 `risk30_cap60_hold8_turn04_exit92_weekly` 强化 2026 但牺牲 2020/2023，本轮新增前已将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，active weekly universe 维持 cap `60`。随后按 `turnover_reduction` 测试同一低换手形态的成本守门、更窄 `exit90` 纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold8_turn04_exit90_weekly`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold8_turn04_exit90_weekly`。
- `cost_guard_cap60_hold8_turn04_exit90_weekly` 五窗口 CAGR 为 `11.11% / 2.43% / 7.41% / 33.18% / 52.95%`，最大回撤为 `-32.72% / -45.62% / -28.62% / -20.00% / -11.42%`，换手为 `3.03x / 3.25x / 3.14x / 3.52x / 5.95x`。成本守门没有修复 2020/2023 塌陷，只保留 2026 弹性，不替换 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=64`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`risk30_cap60_hold8_turn04_exit92_weekly`，原因是 2020 CAGR 仅 `1.00%`、2023 仅 `8.52%`。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 仍为 `turnover_reduction`。下一轮新增前应先归档本轮 `cost_guard_cap60_hold8_turn04_exit90_weekly`，理由是 2020 CAGR 仅 `2.43%`、2023 仅 `7.41%`；第一条命令建议不要继续成本守门，改测更低 turn 与更长持有但保留现金防守的纯周频版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_id>`。

## 本轮执行计划（2026-05-28 16:18 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap60_hold8_turn04_exit94_weekly` 继续 2023 塌陷且 2020 回撤恶化，本轮新增前已将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，active weekly universe 维持 cap `60`。随后按 `risk_downshift` 测试同一低换手框架的 `risk30/cap60/exit92` 纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn04_exit92_weekly`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn04_exit92_weekly`。
- `risk30_cap60_hold8_turn04_exit92_weekly` 五窗口 CAGR 为 `10.89% / 1.00% / 8.52% / 33.18% / 52.95%`，最大回撤为 `-30.30% / -48.13% / -28.15% / -20.00% / -11.42%`，换手为 `3.05x / 3.24x / 3.32x / 3.52x / 5.95x`。风险降档强化 2026，但几乎牺牲 2020/2023，可持续性弱于 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=63`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`cashoff_cap60_hold8_turn04_exit94_weekly`，原因是 2023 CAGR 仅 `4.83%` 且 2020 回撤恶化。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 为 `cost_stress`。下一轮新增前应先归档本轮 `risk30_cap60_hold8_turn04_exit92_weekly`，理由是 2020 CAGR 仅 `1.00%`、2023 只有 `8.52%`；第一条命令建议测试同一形态的成本压力/更窄出场版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold8_turn04_exit90_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap55_hold8_turn04_exit94_weekly` 2023 CAGR 只有 `4.83%`，本轮新增前已将其加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，active weekly universe 维持 `60/60 complete`。随后按 `turnover_reduction/weekly_exit_buffer` 提高 cap 到 `60`，验证低换手形态是否只是被 cap55 压低收益。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn04_exit94_weekly`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap60_hold8_turn04_exit94_weekly` 五窗口 CAGR 为 `14.73% / 15.07% / 4.83% / 20.68% / 37.06%`，最大回撤为 `-26.54% / -40.38% / -29.08% / -26.12% / -10.20%`，换手为 `2.52x / 2.16x / 2.32x / 4.63x / 8.64x`。提高 cap 没有修复 2023 塌陷，反而加深 2020 回撤，不能替换 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=62`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`cashoff_cap55_hold8_turn04_exit94_weekly`，原因是 2023 收益过低且未改善 robust。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 为 `risk_downshift`。下一轮新增前应先归档本轮 `cashoff_cap60_hold8_turn04_exit94_weekly`，理由是 2023 CAGR 只有 `4.83%` 且 2020 回撤恶化；第一条命令建议在同一低换手框架上降低风险暴露并收紧退出，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn04_exit92_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；上一轮 `cost_guard_cap58_hold6_turn04_exit90_weekly` 2020 转负且 2023 仍弱，本轮新增前已加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，active weekly universe 维持 `60/60 complete`。随后按 `turnover_reduction` 测试更低 cap、更长持有、更宽出场的纯 `_weekly` 版本。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn04_exit94_weekly`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap55_hold8_turn04_exit94_weekly` 五窗口 CAGR 为 `14.67% / 15.11% / 4.83% / 20.96% / 36.17%`，最大回撤为 `-26.54% / -27.54% / -29.08% / -26.12% / -10.20%`，换手为 `2.50x / 2.74x / 2.32x / 4.63x / 8.64x`。它保留低换手，但 2023 收益继续坍塌且 2025 弹性不足，不能替换 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=61`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`cost_guard_cap58_hold6_turn04_exit90_weekly`，原因是 2020 负收益与 2023 弱。
- 最终 guard 为 `pass`，下一轮 focus 仍为 `turnover_reduction`。下一轮新增前应先归档本轮 `cashoff_cap55_hold8_turn04_exit94_weekly`，理由是 2023 CAGR 只有 `4.83%` 且不改善 robust；第一条命令建议不要继续拓宽 exit，改测低换手但保留更高 cap 的纯周频对照，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn04_exit94_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_id>`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap58_hold6_turn04_exit92_weekly` 2023 CAGR 只有 `8.07%` 且不改善 robust，本轮新增前已加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，active weekly universe 维持 `60/60 complete`。随后按 `cost_stress` 测试同一低换手框架的成本守门/更窄出场版本。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn04_exit90_weekly`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cost_guard_cap58_hold6_turn04_exit90_weekly` 五窗口 CAGR 为 `10.75% / -0.29% / 8.72% / 27.32% / 109.31%`，最大回撤为 `-31.73% / -50.25% / -25.16% / -22.40% / -7.73%`，换手为 `2.94x / 3.11x / 2.81x / 3.61x / 6.75x`。它只强化 2026，2020 转负且 2023 仍塌陷，不能替换 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=60`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`。本轮 evict/归档：`cashoff_cap58_hold6_turn04_exit92_weekly`，原因是 2023 收益过低且未改善 robust。
- 最终 guard 为 `pass`，下一轮 focus 已轮换为 `turnover_reduction`。下一轮新增前应先归档本轮 `cost_guard_cap58_hold6_turn04_exit90_weekly`，理由是 2020 负收益与 2023 弱；第一条命令建议不继续强成本守门，改测更低换手且退出更宽的纯 `_weekly` 版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn04_exit94_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_id>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮要求新增前先归档 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly`，本轮已加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2023 失败且不改善 robust。随后按 `weekly_exit_buffer` 新增纯 `_weekly` 的 `turn04/exit92` 低换手缓冲版本。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_12_88_hold_3_7_ramp85_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly`。
- `cashoff_cap58_hold6_turn04_exit92_weekly` 五窗口 CAGR 为 `15.58% / 13.90% / 8.07% / 19.24% / 63.61%`，最大回撤 `-27.44% / -27.31% / -29.39% / -23.62% / -10.20%`，换手 `2.48x / 2.52x / 2.33x / 4.73x / 8.74x`。更宽退出缓冲保住 2026 弹性并降低中窗换手，但 2023 收益继续坍塌，不能替换 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=59`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`，四窗口 meanCAGR `30.44%`、minCAGR `12.70%`、worstMaxDD `-28.69%`、meanTurn `8.98x`。
- 最终 guard 为 `pass`，`ashare_path3_weekly_universe 60/60 complete`。下一轮新增前应先归档本轮 `cashoff_cap58_hold6_turn04_exit92_weekly`，理由是 2023 CAGR 只有 `8.07%` 且不改善 robust；下一轮 focus 转为 `risk_downshift`，第一条命令建议测试同一低换手框架的风险降档版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap58_hold6_turn04_exit90_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮要求新增前先归档 `cashoff_cap58_hold6_turn06_exit88_weekly`，本轮已加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2023 CAGR 只有 `11.63%` 且不改善 robust。随后按 `cost_stress` 新增同一形态的纯 `_weekly` 成本守门版。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly`。实际命令见 Path 2 本轮 A股非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cost_guard_cap58_hold6_turn06_exit88_weekly` 五窗口 CAGR 为 `8.70% / -0.27% / 5.89% / 48.99% / 103.97%`，最大回撤 `-37.89% / -51.25% / -35.05% / -24.89% / -7.91%`，换手 `3.50x / 3.90x / 3.93x / 4.95x / 7.05x`。成本守门只强化 2026 短窗，2020/2023 收益和回撤明显坍塌，不适合晋级。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=58`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`，四窗口 meanCAGR `30.44%`、minCAGR `12.70%`、worstMaxDD `-28.69%`、meanTurn `8.98x`。最终 guard 为 `ashare_path3_weekly_universe 60/60 complete`。
- 下一轮新增前应先归档本轮 `cost_guard_cap58_hold6_turn06_exit88_weekly`，理由是 2020/2023 失败且不改善 robust。最终 focus 转为 `weekly_exit_buffer`；第一条命令建议改测不加成本守门、但保留低换手框架的更宽退出缓冲版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_exit_buffer_id>`。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；上一轮要求新增前先归档 `cashoff_cap58_hold7_turn05_exit92_weekly`，本轮已加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2023 CAGR 只有 `11.64%` 且 2026 为负。随后按 `risk_downshift/weekly_exit_buffer` 把持有期缩到 6 周、退出收紧到 `exit88`，仍只在纯 `_weekly` Path 3 内比较。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn06_exit88_weekly`。实际命令见 Path 2 本轮非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap58_hold6_turn06_exit88_weekly` 五窗口 CAGR 为 `15.30% / 13.97% / 11.63% / 57.01% / 58.17%`，最大回撤 `-29.33% / -28.53% / -29.62% / -24.89% / -10.20%`，换手 `2.77x / 2.82x / 2.38x / 5.45x / 8.82x`。它修复了上一版 2026 负收益，但 2020/2023 收益仍明显低于当前 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=57`；`scripts/update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未变化，active weekly universe 仍为 `60/60 complete`。下一轮新增前应先归档本轮候选，理由是 2023 CAGR 只有 `11.63%` 且不改善 robust；最终 focus 转为 `cost_stress`，第一条命令建议测试同一形态的成本守门版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap55_hold8_turn05_exit92_weekly` 2023 仍塌陷，本轮按 `turnover_reduction` 测试稍放宽单票 cap、保持 7 周持有和 `turn05/exit92` 的低换手纯 `_weekly` 对照。命令类型为五窗口 `--only-base-ids` 增量确认，实际 A股合并命令见 Path 1 本轮记录。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold7_turn05_exit92_weekly`。
- `cashoff_cap58_hold7_turn05_exit92_weekly` 五窗口 CAGR 为 `16.93% / 12.41% / 11.64% / 22.16% / -5.76%`，最大回撤 `-28.01% / -28.84% / -28.34% / -26.50% / -15.66%`，换手 `2.69x / 2.71x / 2.27x / 4.52x / 9.03x`。它压低了 2020/2023 换手，但 2025 弹性大幅折损且 2026 转负，不能替换当前 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=56`；`scripts/update_weighted_winners.py` 后 Path 3 official winner 与 robust 未变化，仍由旧 `cashoff_cap80_hold3_turn25_weekly` 与高弹性周频组合主导。
- active weekly universe 仍为 `60/60 complete`。下一轮新增前应先归档本轮 `cashoff_cap58_hold7_turn05_exit92_weekly`，理由是 2023 CAGR 只有 `11.64%` 且 2026 为负；最终 focus 转为 `weekly_exit_buffer`，第一条命令建议只在归档后测试更窄退出缓冲或更短持有的纯周频版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn06_exit88_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_exit_buffer_id>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮 `cost_guard_cap60_hold7_turn06_exit90_weekly` 2020/2023 坍塌，本轮新增前把它加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2023 CAGR 仅 `2.17% / 5.03%` 且未改善 robust，active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn05_exit92_weekly`。实际命令见 Path 2 本轮 A股合并批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap55_hold8_turn05_exit92_weekly` 五窗口 CAGR 为 `14.84% / 14.88% / 7.82% / 67.02% / 35.22%`，最大回撤 `-27.79% / -27.77% / -27.48% / -23.30% / -10.20%`，换手 `2.69x / 2.71x / 2.25x / 4.40x / 8.67x`。该候选把 2026 修到正收益并保持低换手，但 2023 收益仍明显塌陷，不适合替换当前 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=55`；`scripts/update_weighted_winners.py` 后 Path 3 official winner 与 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，未改 tracked payload。最终 guard 为 `ashare_path3_weekly_universe 60/60 complete`。
- 下一轮新增前应先归档本轮 `cashoff_cap55_hold8_turn05_exit92_weekly`，理由是 2023 CAGR 只有 `7.82%`。最终 focus 转为 `risk_downshift`；第一条命令建议测试同一低换手框架的风险降档版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap55_hold8_turn05_exit90_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮 `cashoff_cap60_hold7_turn06_exit90_weekly` 仍然 2023 低收益，本轮新增前把该候选加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是中窗 CAGR 只有 `8.46%` 且未改善 robust，active weekly universe 继续维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold7_turn06_exit90_weekly`。实际命令见 Path 1 本轮 A股非阻塞合并批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cost_guard_cap60_hold7_turn06_exit90_weekly` 五窗口 CAGR 为 `8.18% / 2.17% / 5.03% / 32.02% / 97.49%`，最大回撤 `-30.35% / -37.46% / -30.77% / -25.23% / -7.95%`，换手 `3.22x / 3.52x / 3.39x / 4.68x / 6.51x`。成本守门修复 2026，但 2017/2020/2023 坍塌更明显，确认这条低换手成本线不适合晋级。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=54`；`scripts/update_weighted_winners.py` 后 Path 3 official winner 与 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，未改 tracked payload。最终 guard 为 `ashare_path3_weekly_universe 60/60 complete`。
- 下一轮新增前应先归档本轮 `cost_guard_cap60_hold7_turn06_exit90_weekly`，理由是 2020/2023 失败。最终 focus 转为 `turnover_reduction`；第一条命令建议测试不加成本守门、进一步降换手但给退出更宽缓冲的版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn05_exit92_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_id>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `cashoff_cap60_hold7_turn06_exit94_weekly` 换手降到约 `2.5x` 但 2023 CAGR 只有 `8.45%`；本轮新增前把该候选加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是中窗收益过低、2025 回撤较深且未改善 robust，active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit90_weekly`。实际 A股非阻塞命令见 Path 2 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap60_hold7_turn06_exit90_weekly` 五窗口 CAGR 为 `15.08% / 16.32% / 8.46% / 55.53% / 59.70%`，最大回撤 `-29.02% / -34.06% / -29.83% / -25.23% / -10.20%`，换手 `2.79x / 2.57x / 2.51x / 5.44x / 8.77x`。它相对 `exit94` 略修 2020，但 2023 仍塌陷，不能替换当前 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=52`；`scripts/update_weighted_winners.py` 后 Path 3 official winner 与 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，未改 tracked payload。最终 guard 为 `ashare_path3_weekly_universe 60/60 complete`。
- 最终 guard 后 focus 转为 `cost_stress`。下一轮新增前继续先归档本轮若仍未改善的低换手候选；第一条命令建议测试同一低换手框架的成本守门，而不是再只调 exit，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold7_turn06_exit90_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`，上一轮 `cost_guard_cap65_hold6_turn08_exit90_weekly` 中窗继续坍塌；本轮新增前把该候选加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2023 CAGR 仅 `2.40% / 2.43%` 且不改善 robust，active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit94_weekly`。命令类型为 A股五窗口 `--only-base-ids` 增量确认：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit94_weekly`。
- `cashoff_cap60_hold7_turn06_exit94_weekly` 五窗口 CAGR 为 `15.08% / 15.93% / 8.45% / 55.53% / 59.70%`，最大回撤 `-29.02% / -34.11% / -29.83% / -25.23% / -10.20%`，换手 `2.79x / 2.51x / 2.51x / 5.44x / 8.77x`。它确实把 2020/2023 换手降到约 `2.5x`，但 2023 收益太低、2025 回撤较深，未改善 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=52`；`scripts/update_weighted_winners.py` 后 Path 3 official winner 与 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，未改 tracked payload。最终 guard 为 `ashare_path3_weekly_universe 60/60 complete`。
- 下一轮 focus 为 `weekly_exit_buffer`。下一轮新增前先归档本轮若仍未改善的低换手候选；第一条命令建议收紧退出缓冲而保留低换手框架，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit90_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_exit_buffer_id>`。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass`，上一轮 `risk30_cap65_hold6_turn08_exit90_weekly` 修复 2026 但 2020/2023 CAGR 只有 `2.83% / 2.70%`；本轮新增前把该候选加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是中窗坍塌且未改善 robust，active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap65_hold6_turn08_exit90_weekly`。命令类型为 A股五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path 1 本轮记录。
- `cost_guard_cap65_hold6_turn08_exit90_weekly` 五窗口 CAGR 为 `9.58% / 2.40% / 2.43% / 18.88% / 33.80%`，最大回撤 `-31.22% / -37.81% / -33.07% / -22.72% / -15.05%`，换手 `3.62x / 3.79x / 3.89x / 4.74x / 7.40x`。成本守门保留 2026 正收益，但 2020/2023 比上一轮 risk-downshift 更弱，确认这条低风险/低换手形态不适合晋级。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=51`；`scripts/update_weighted_winners.py` 后 Path 3 official winner 与 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，未改 tracked payload。
- 最终 guard 为 `ashare_path3_weekly_universe 60/60 complete`，下一轮 focus 转为 `turnover_reduction`。下一轮新增前继续先归档本轮中窗塌陷候选；第一条命令建议测试不加成本守门、进一步降低换手但保留更宽退出的版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit94_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_id>`。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass`，上一轮要求先做 `risk_downshift`；新增前把 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是上一轮确认后 2020/2023 CAGR 仅 `9.10% / 13.69%` 且 2026 为 `-8.95%`，未改善 robust，active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap65_hold6_turn08_exit90_weekly`。实际命令见 Path 1 本轮 A股合并批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `risk30_cap65_hold6_turn08_exit90_weekly` 五窗口 CAGR 为 `8.15% / 2.83% / 2.70% / 22.30% / 34.74%`，最大回撤 `-29.90% / -35.32% / -35.77% / -22.72% / -15.05%`，换手 `3.84x / 4.13x / 4.04x / 4.86x / 7.40x`。风险降档修复了 2026 为正，但 2020/2023 进一步塌陷，且收益/回撤均弱于当前 Path 3 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=51`；`scripts/update_weighted_winners.py` 后 Path 3 window winner 与 robust 未变化，robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，最终 guard `ashare_path3_weekly_universe 60/60 complete`。
- 收尾再次运行 guard 后下一轮 focus 转为 `cost_stress`。下一轮新增前继续先归档一个 2020/2023 明显塌陷候选；第一条命令建议不要继续只降低风险仓位，改测带成本守门但不过度牺牲中窗的版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap65_hold6_turn08_exit90_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass`，上一轮 `cost_guard_cap68_hold5_turn10_exit92_weekly` 修复 2026 但 2020/2023 坍塌；本轮按 `turnover_reduction` 新增更低换手、无成本守门的 `cashoff_cap65_hold6_turn08_exit94_weekly`。新增前把 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2023 CAGR 仅 `3.70% / 4.83%` 且未改善 robust，active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly`。实际命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly`。
- `cashoff_cap65_hold6_turn08_exit94_weekly` 五窗口 CAGR 为 `10.16% / 9.10% / 13.69% / 41.54% / -8.95%`，最大回撤 `-32.68% / -29.72% / -29.47% / -24.99% / -16.20%`，换手 `3.28x / 2.50x / 2.58x / 5.38x / 9.43x`。它降低 2020/2023 换手但收益不足，且 2026 转负，未改变 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=50`；`scripts/update_weighted_winners.py` 后 Path 3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，最终 guard `ashare_path3_weekly_universe 60/60 complete`。
- 最终 guard 下一轮 focus 转为 `risk_downshift`。下一轮新增前继续先归档一个 2020/2023 明显塌陷候选；第一条命令建议不要继续放宽到 `exit94`，改测更低风险暴露的纯周频版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap65_hold6_turn08_exit90_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass`，上一轮 `cashoff_cap68_hold5_turn10_exit92_weekly` 的 2020/2023 收益不足且 2026 仍负；本轮按 `cost_stress` 改成成本守门版本。新增前已将 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 `2020/2023 CAGR=9.51%/12.56%` 且未改善 robust，active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly`。实际命令见 Path 2 本轮 A股新增批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cost_guard_cap68_hold5_turn10_exit92_weekly` 五窗口 CAGR 为 `9.65% / 3.70% / 4.83% / 39.64% / 25.25%`，最大回撤 `-33.07% / -33.81% / -37.51% / -22.24% / -17.36%`，换手 `3.92x / 4.05x / 4.27x / 5.40x / 8.00x`。成本守门能让 2026 转正，但 2020/2023 严重坍塌，未改变 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=49`；`scripts/update_weighted_winners.py` 后 Path 3 official winners 与 robust 未变化，robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`。
- 最终 guard 下一轮 focus 为 `turnover_reduction`。下一轮新增前继续先归档一个 2020/2023 明显塌陷候选；第一条命令建议实现更低换手但不过度成本守门的纯周频版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_id>`。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass`，上一轮 `cost_guard_cap55_hold6_turn10_exit88_weekly` 只修复 2026、但 2020/2023 全面弱；本轮按 `weekly_exit_buffer` 新增更温和的 `exit92` 对照。新增前将 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2023 CAGR 只有 `3.42% / 5.60%` 且未改善 robust，active weekly universe 维持 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly`。实际命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly`。
- `cashoff_cap68_hold5_turn10_exit92_weekly` 五窗口 CAGR 为 `16.81% / 9.51% / 12.56% / 68.84% / -1.78%`，最大回撤 `-31.27% / -26.36% / -31.45% / -25.54% / -18.83%`，换手 `3.46x / 2.54x / 2.58x / 6.03x / 10.09x`。退出缓冲能提升 2025，但 2020/2023 收益不足且 2026 仍为负，不改变 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=48`；`scripts/update_weighted_winners.py` 后 Path 3 official winners 与 robust 未变化，robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`。
- 最终 guard 下一轮 focus 轮到 `cost_stress`。下一轮新增前继续先归档一个 2020/2023 明显塌陷候选；第一条命令建议实现并确认更直接的成本压力版本，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly` 或同等低换手成本守门候选，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass`，上一轮 `risk35_cap70_hold5_turn10_exit88_weekly` 2020/2023 坍塌且不改善 robust；本轮按 `cost_stress` 新增前先把 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk35_cap70_hold5_turn10_exit88_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是五窗口中 2020/2023 CAGR 只有 `2.62% / 3.93%`，active weekly universe 继续维持默认 cap `60`。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly`。实际命令见 Path 2 本轮 A股非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cost_guard_cap55_hold6_turn10_exit88_weekly` 五窗口 CAGR 为 `7.86% / 3.42% / 5.60% / 39.73% / 57.29%`，最大回撤 `-31.23% / -32.97% / -33.81% / -19.90% / -9.06%`，换手 `3.65x / 3.68x / 3.74x / 5.49x / 7.77x`。它能把 2026 修到较强正收益，但 2017/2020/2023 全面低于 Path 3 robust，失败原因仍是成本守门/低换手过度牺牲中长窗收益。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=47`；`scripts/update_weighted_winners.py` 后 Path 3 official winners 与 robust 未变化，robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`。
- 收尾 guard 下一轮 focus 为 `weekly_exit_buffer`。下一轮新增前继续先归档一个 2020/2023 明显塌陷候选；第一条命令建议不要继续加强成本守门，改测较温和的退出缓冲，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly` 或同等 `exit92` 版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_exit_buffer_id>`。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `risk_downshift`；本轮新增前先把 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn14_exit90_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2026 弱、未改善 robust，并使 active weekly universe 继续维持在默认 cap `60` 内。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk35_cap70_hold5_turn10_exit88_weekly`。实际命令见 Path 1 本轮 A股非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `risk35_cap70_hold5_turn10_exit88_weekly` 五窗口 CAGR 为 `8.18% / 2.62% / 3.93% / 40.11% / 27.01%`，最大回撤 `-35.08% / -39.54% / -40.22% / -22.24% / -17.36%`，换手 `4.23x / 4.50x / 4.60x / 5.35x / 8.08x`。风险降档没有修复 2020/2023，且 2026 弹性不足以抵消长窗失败，未改变 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=46`；`scripts/update_weighted_winners.py` 后 Path 3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，official window winners 未变化。
- 收尾 focus 转向 `cost_stress`。下一轮新增前继续先归档一个 2020/2023 明显塌陷候选；第一条命令建议测试一个更直接的成本压力对照，如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_cost_stress_id>`。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass`，上一轮 `cost_guard_cap45_hold5_turn12_exit90_weekly` 修复 2026 但 2020/2023 坍塌。本轮按 `turnover_reduction` 新增一个纯 `_weekly` 的 `cashoff_cap75_hold5_turn12_exit88` 版本；新增前把 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap45_hold5_turn12_exit90_weekly` 归档出 active universe，理由是 2020/2023 CAGR 仅 `2.72% / 15.79%`，且未改善 robust。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly`。实际命令见 Path 2 本轮非阻塞 A股批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap75_hold5_turn12_exit88_weekly` 五窗口 CAGR 为 `12.47% / 14.21% / 17.72% / 46.16% / 56.96%`，最大回撤 `-35.40% / -27.80% / -32.22% / -26.06% / -9.92%`，换手 `3.29x / 3.33x / 3.11x / 6.49x / 9.87x`。它把 2026 修到正收益且换手低于高弹性周频，但 2017/2023 收益和回撤不足，未改变 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=45`；`scripts/update_weighted_winners.py` 后 Path 3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=27.45% / minCAGR=19.50%`。
- 收尾 guard 给出下一轮 focus `risk_downshift`，active weekly universe 保持 `60/60 complete`。下一轮新增前继续先归档一个 2020/2023 弱候选；第一条命令建议实现 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk35_cap70_hold5_turn10_exit88_weekly` 或同等风险降档版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_risk_downshift_id>`。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass`，上一轮 `cashoff_cap70_hold4_turn14_exit90_weekly` 修复不了 2020/2026；本轮按 `cost_stress` 新增一个纯 `_weekly` 成本守门版本。新增前把 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap50_hold5_turn14_exit85_weekly` 归档出 active universe，理由是 2020 CAGR 仅 `4.39%`、2023 仅 `16.09%`，且未改善 robust，active weekly cap 维持在 `60`。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap45_hold5_turn12_exit90_weekly`。实际命令见 Path 1 本轮 A股非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cost_guard_cap45_hold5_turn12_exit90_weekly` 五窗口 CAGR 为 `12.33% / 2.72% / 15.79% / 46.81% / 63.41%`，最大回撤 `-38.43% / -41.00% / -30.55% / -18.97% / -13.46%`，换手 `5.18x / 5.59x / 6.05x / 6.51x / 8.26x`。它能把 2026 观察窗转强，但 2020 坍塌且长窗回撤过深，不改变 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=44`，`scripts/update_weighted_winners.py` 后 Path 3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=25.78% / minCAGR=18.95%`。
- 收尾 guard 给出下一轮 focus `turnover_reduction`。下一轮新增前继续先归档一个 2020/2023 明显塌陷候选；第一条命令建议实现 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly` 或同等低换手纯 `_weekly` 版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_turnover_reduction_id>`。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass`，上一轮第一条命令要求先归档另一个 2023/2020 弱候选再测试 exit buffer；本轮把 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap50_hold4_turn18_exit85_weekly` 归档出 active universe，理由是 2020/2023 CAGR 仅 `5.93% / 12.99%` 且未改善 robust。
- 本轮新增并五窗口确认 1 个纯 `_weekly` Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn14_exit90_weekly`。实际命令见 Path 1 本轮 A股合并命令，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap70_hold4_turn14_exit90_weekly` 五窗口 CAGR 为 `15.20% / 9.16% / 18.71% / 62.35% / -21.93%`，最大回撤 `-31.36% / -32.72% / -35.07% / -25.24% / -20.44%`，换手 `4.16x / 3.24x / 3.13x / 7.56x / 10.92x`。较上一轮 cap75 版本提高 2025 弹性，但 2020 收益和 2026 观察窗恶化，未改变 Path 3 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=43`，`update_weighted_winners.py` 后 Path 3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=25.78% / minCAGR=18.95%`；active weekly universe 通过本轮归档保持在 cap 内。
- 收尾 guard 的下一轮 focus 为 `cost_stress`。第一条命令建议不要继续放宽 exit90，而是测试一个更直接的成本折中，如 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap45_hold5_turn12_exit90_weekly`；新增前继续优先归档 2020/2023 低于 10%-13% 且未改善 robust 的旧周频候选。

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass`，上一轮 `cost_guard_cap50_hold5_turn14_exit85_weekly` 2026 转正但 2020/2023 塌陷；本轮按 `turnover_reduction`/中等退出缓冲测试更高 cap 与较短持有的纯 `_weekly` 候选。新增前已把旧 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn08_exit85_weekly` 归档出 active universe，理由是 2023 CAGR 仅 `9.29%` 且未改善 robust。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold4_turn16_exit85_weekly`。实际命令见 Path 1 本轮合并命令，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cashoff_cap75_hold4_turn16_exit85_weekly` 五窗口 CAGR 为 `19.00% / 17.60% / 11.10% / 35.20% / 13.80%`，最大回撤 `-31.40% / -26.90% / -36.00% / -22.10% / -13.80%`，换手 `4.22x / 3.51x / 3.65x / 7.72x / 11.04x`；2026 由负转正且换手低于高弹性周频，但 2023 塌陷、2025 弹性不足，未改变 Path 3 winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=42`，`update_weighted_winners.py` 后 robust 仍为 `cashoff_cap80_hold3_turn25_weekly`；active weekly universe 通过本轮归档继续维持在 cap 内。
- 下一轮 focus -> candidates 池切到 `weekly_exit_buffer`，不要继续只调 cap；第一条命令建议先归档另一个 2023 明显塌陷候选，再测试 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn14_exit90_weekly`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path3_exit_buffer_id>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass`，上一轮 `risk40_cap50_hold4_turn18_exit85_weekly` 2026 爆发但 2020/2023 塌陷；本轮按成本压力方向新增一个纯 `_weekly` 成本守门版，并先把旧 `cashoff_cap55_hold9_turn08_exit90_weekly` 归档出 active universe，理由是 2023 CAGR 仅 `8.29%` 且不改善 robust。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap50_hold5_turn14_exit85_weekly`。实际命令见 Path 1 本轮合并命令。
- `cost_guard_cap50_hold5_turn14_exit85_weekly` 五窗口 CAGR 为 `14.26% / 4.39% / 16.09% / 48.53% / 69.32%`，最大回撤 `-37.31% / -41.05% / -34.12% / -19.28% / -12.79%`，换手 `5.67x / 6.00x / 6.45x / 7.67x / 9.05x`；成本版能让 2026 为正，但 2020 只有 `4.39%` 且回撤更深，未晋级。
- `scripts/path2_candidate_pass.py` 后 `weekly_rebalance_aggressive=41`，`update_weighted_winners.py` 后 Path 3 official winners 与 robust 未变，robust 仍为 `cashoff_cap80_hold3_turn25_weekly`。active weekly cap 通过归档弱项维持，不触发新增冲突。
- 下一轮 focus -> candidates 池：不要继续在 `aggr_05_95_prom3` 上加更强成本防守；第一条命令建议测试 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold4_turn16_exit85_weekly`，用较高 cap 和中等换手检查能否保留 2020/2023，同时把 2026 从负转正；新增前优先再归档一个 2023 明显塌陷候选。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 指向 `risk_downshift`；上一轮低换手 `cap62_hold6_turn10_exit88_weekly` 仍未修复 2026，本轮提高 promotion 到 `aggr_05_95_prom3` 并限制风险/换手。
- 本轮先将 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2023 CAGR 仅 `4.89%` 且未改善 robust；新增并五窗口确认 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap50_hold4_turn18_exit85_weekly`。实际命令见 Path 1 本轮合并命令。
- `risk40_cap50_hold4_turn18_exit85_weekly` 五窗口 CAGR 为 `14.12% / 5.93% / 12.99% / 54.12% / 117.64%`，最大回撤 `-29.97% / -41.01% / -37.56% / -19.09% / -9.94%`，换手 `6.25x / 6.63x / 6.92x / 8.86x / 10.71x`；2026 爆发很强，但 2020/2023 收益与回撤失效，未晋级。
- `update_weighted_winners.py` 后 Path 3 official winners 与 robust 未变，robust 仍为 `cashoff_cap80_hold3_turn25_weekly`；`scripts/path2_candidate_pass.py` 中 `weekly_rebalance_aggressive=40`，active weekly universe 通过归档弱项维持 cap。
- 收尾 guard 后 rotation 切到 `cost_stress`。下一轮第一条命令建议实现成本守门版 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap50_hold5_turn14_exit85_weekly`，用更长持有和更低换手检查 2020/2023 是否恢复；若再新增第二个周频 ID，先归档另一个 2023 明显塌陷候选。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `cap60_hold7_turn08_exit85_weekly` 低换手但 2023 塌陷，本轮按 `risk_downshift`/低换手折中，先归档旧弱候选再新增 1 个纯 `_weekly` 对照。
- 本轮将 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2023 CAGR 仅约 `7.02%` 且对 robust 无改善；新增并五窗口确认 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly`。
- `cap62_hold6_turn10_exit88_weekly` 五窗口 CAGR 为 `14.32% / 15.93% / 14.87% / 73.50% / -9.59%`，最大回撤 `-32.36% / -26.66% / -29.86% / -24.21% / -16.39%`，换手 `3.46x / 3.05x / 2.55x / 5.91x / 9.62x`；换手低于高弹性周频，但 2026 转负且 2023 不足，未晋级。
- `update_weighted_winners.py` 后 Path 3 official winners 与 robust 未变，robust 仍为 `cashoff_cap80_hold3_turn25_weekly`；`scripts/path2_candidate_pass.py` 中 `weekly_rebalance_aggressive=39`，active weekly cap 继续保持 `60/60 complete`。
- 下一轮 focus -> candidates 池：不要继续单纯降低换手；第一条命令建议测试 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap55_hold4_turn18_weekly` 的五窗口确认，观察是否能用更高弹性抵消 2026 失效；若再新增第二个周频 ID，先归档 `cap50_hold10_turn06_weekly`。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；active weekly cap 已满，本轮先按上一轮计划归档失败的 `risk30_cap60_hold8_turn10_exit90_weekly`，再测试低换手但不过度降仓的纯 `_weekly` 变体。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn08_exit85_weekly`。实际回测命令见 Path 1 本轮合并命令。
- `cashoff_cap60_hold7_turn08_exit85_weekly` 五窗口 CAGR 为 `14.49% / 13.84% / 9.29% / 56.56% / 54.76%`，最大回撤 `-30.92% / -29.51% / -31.69% / -24.53% / -10.20%`，换手 `2.98x / 2.89x / 2.65x / 5.45x / 9.13x`；换手压低但 2023 收益继续塌陷，未晋级。
- `update_weighted_winners.py` 后 Path 3 official winners 与 robust 未变化，robust 仍为 `cashoff_cap80_hold3_turn25_weekly`；`scripts/path2_candidate_pass.py` 中 `weekly_rebalance_aggressive=38`。已将 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn10_exit90_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，理由是 2020/2023 CAGR 仅 `2.25% / 6.04%` 且未改善回撤。
- 收尾 guard 为 `pass`，Path 3 active weekly universe 保持 `60/60 complete`，rotation 为 `stagnation_runs=5 / weekly_exit_buffer / rotate`。下一轮 focus -> candidates 池不要继续压到 `turn08+hold7`，第一条命令建议先实现 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold6_turn10_exit88_weekly` 并五窗口 `--only-base-ids <next_path3_exit_buffer_id>` 补跑；若再新增第二个周频 ID，先归档 `cap45_hold9_turn06_weekly`。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `cost_guard_cap60_hold6_turn12_exit85_weekly` 五窗口失败且 active cap 已满，本轮先把该失败对照从 active coverage 归档，再测试低换手但不过度降仓的纯 `_weekly` 变体。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly`。实际回测命令见 Path 1 本轮合并命令。
- `cashoff_cap65_hold5_turn10_exit85_weekly` 五窗口 CAGR 为 `16.57% / 9.87% / 12.55% / 70.10% / -13.25%`，最大回撤 `-31.30% / -26.36% / -31.45% / -25.56% / -17.58%`，换手 `3.46x / 2.64x / 2.58x / 5.73x / 10.00x`；换手较高弹性周频低，但 2020/2023 收益不足且 2026 为负，未晋级。
- `update_weighted_winners.py` 后 Path 3 official winners 未变化：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `cashoff_cap80_hold3_turn25_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `cashoff_cap70_hold4_turn20_weekly`；四窗口 robust 仍为 `cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=26.96% / minCAGR=19.19% / worstMaxDD=-37.59% / meanTurn=6.09`。
- 已将 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold6_turn12_exit85_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，保留历史 CSV 但不再计入 active guard；收尾 guard 为 `pass`，Path 3 active weekly universe 回到 `60/60 complete`。最终 rotation 为 `stagnation_runs=2 / turnover_reduction / continue`；下一轮若新增必须先再归档一个弱候选，优先 evict `risk30_cap60_hold8_turn10_exit90_weekly`，再实现 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn08_exit85_weekly` 并五窗口 `--only-base-ids <next_path3_turnover_id>` 补跑。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `risk30` 降仓候选长窗收益塌陷，最终 focus 指向 `cost_stress`。本轮只新增 1 个纯 `_weekly` 成本守门候选，没有混入 Path 1 的月度选股 + 周度仓位 overlay。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold6_turn12_exit85_weekly`。实际回测命令见 Path 1 本轮合并命令。
- `cost_guard_cap60_hold6_turn12_exit85_weekly` 五窗口 CAGR 为 `5.71% / 1.60% / 7.53% / 41.42% / 38.13%`，最大回撤 `-35.21% / -38.00% / -36.73% / -19.54% / -14.66%`，换手 `4.07x / 4.22x / 4.21x / 7.35x / 8.24x`；成本守门太强，2017/2020/2023 全面低于现有 Path 3 robust，只保留失败对照。
- `update_weighted_winners.py` 后 Path 3 official winners 未变化：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020/2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`；四窗口 robust 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`。
- Guard 显示 weekly universe 为 `60/60 complete`，已到默认 active cap；本轮没有新增前的实质冲突，因此不回删用户/既有结果，但下一轮新增 Path 3 前必须先 evict。优先归档本轮 `cost_guard_cap60_hold6_turn12_exit85_weekly`，理由是 2020 CAGR 仅 `1.60%` 且未改善回撤/换手组合。
- 最终 guard 后 rotation 为 `stagnation_runs=12 / turnover_reduction / rotate`；下一轮第一步不是直接加候选，而是先移出上述失败对照，再测试 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly` 或同等低换手但不过度降仓的纯 `_weekly` 变体。

## 本轮执行计划（2026-05-20 13:58 CST）

- 上一轮提示为 `risk_downshift`，本轮只新增 1 个纯 `_weekly` 降仓候选，没有把 Path 1 的月度选股 + 周度仓位 overlay 混入 Path 3。
- 本轮新增并五窗口确认 1 个 Path 3 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn10_exit90_weekly`。实际回测命令见 Path 1 本轮合并命令。
- `risk30_cap60_hold8_turn10_exit90_weekly` 五窗口 CAGR 为 `6.54% / 2.25% / 6.04% / 39.60% / 52.06%`，最大回撤 `-38.66% / -35.64% / -39.41% / -19.74% / -10.14%`，换手 `4.07x / 4.46x / 4.54x / 5.33x / 7.03x`；降仓过重导致 2020/2023 收益塌陷，只保留为失败对照。
- `update_weighted_winners.py` 后 Path 3 official winners 未变化：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020/2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`；四窗口 robust 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`。
- Guard 显示 weekly universe 为 `59/59 complete`，接近默认 active cap `60`；本轮未触发 evict。下一轮若新增超过 1 个，应优先归档本轮 `risk30_cap60_hold8_turn10_exit90_weekly` 或旧 `cap45_hold9_turn06_weekly` 这类 2023 明显塌陷候选。
- 最终 guard 后 rotation 为 `stagnation_runs=9 / cost_stress / rotate`；下一轮 focus -> candidates 池不要再降到 `risk30`，先做交易成本压力和更稳出场。第一条命令建议先实现 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold6_turn12_exit85_weekly`，再用五窗口 `--only-base-ids <path3_cost_stress_id>` 补跑；如同时加第二个 ID，先执行上述 evict。

## 本轮执行计划（2026-05-20 05:20 CST）

- 上一轮提示为 `cap55/60 + hold8/9 + turn08/10 + wider sell_exit`；本轮继续只做纯 `_weekly` 候选，没有混入 Path 1 的周度仓位 overlay。
- 本轮新增并五窗口确认 2 个 Path 3 base ids：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold9_turn08_exit90_weekly` 与 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly`。实际回测命令见 Path 1 本轮合并命令。
- `cap55_hold9_turn08_exit90_weekly` 五窗口 CAGR 为 `10.29% / 15.67% / 8.29% / 62.56% / 29.76%`，最大回撤 `-32.68% / -24.44% / -28.79% / -26.28% / -10.30%`，换手 `2.66x / 2.94x / 2.55x / 6.02x / 8.86x`；2020 回撤好，但 2023 收益塌陷。
- `cap60_hold8_turn10_exit90_weekly` 五窗口 CAGR 为 `11.16% / 15.40% / 16.14% / 69.15% / 30.37%`，最大回撤 `-30.67% / -28.24% / -27.16% / -27.60% / -10.20%`，换手 `3.19x / 2.97x / 2.59x / 6.14x / 9.09x`；较上一候选更均衡，但仍低于现有 robust 的 2017/2020/2023 稳定性。
- `update_weighted_winners.py` 后 Path 3 official winners 未变化：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`；四窗口 robust 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`，`meanCAGR=29.87% / minCAGR=19.15% / worstMaxDD=-37.68% / meanTurn=5.28`。
- Guard 收尾为 `pass`，weekly universe 为 `58`，接近默认 active cap `60` 但未触发 evict；下一轮若新增超过 60，优先归档 `cap45_hold9_turn06` 与 `cap50_hold10_turn06` 这类 2023 塌陷且未改善 robust 的低换手候选。
- 收尾 rotation 为 `stagnation_runs=6 / risk_downshift / rotate`；下一轮 focus -> candidates 池优先做纯周频降仓，不再只压换手。第一条命令建议先实现 `aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn10_exit90_weekly` 与 `aggr_03_97_prom2_weekly_alpha_pullback_risk40_cap55_hold9_turn08_exit90_weekly` 后五窗口 `--only-base-ids` 补跑。

## 本轮执行计划（2026-05-19 23:14 CST）

- 上一轮新增 `cap50_hold8_turn08_weekly` 成为低换手 robust，下一轮提示为 `cap45/50 + hold9/10 + turn06/08`；本轮只沿纯 `_weekly` 路径推进，没有混入 Path 1 的周度仓位 overlay。
- 本轮新增并五窗口确认 2 个 Path 3 base ids：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly` 与 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly`。实际命令与 Path 1/2 合并执行：
  `.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly`。
- `cap45_hold9_turn06` 五窗口 CAGR 为 `14.54% / 12.54% / 7.02% / 66.16% / 31.20%`，换手 `2.66x-4.58x`（2026 观察窗 `8.76x`）；`cap50_hold10_turn06` 为 `15.92% / 15.47% / 4.89% / 61.20% / 43.63%`，换手更低但 2023 塌陷，二者均未晋级。
- Guard 后 Path 3 weekly universe 为 `56/56 complete`，未触发 evict；本轮验证说明继续压到 `turn06 + hold9/10` 会明显牺牲 2023 可持续性。
- `update_weighted_winners.py` 后 Path 3 official winners 同步为：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`；四窗口 robust 回到 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`，`meanCAGR=29.87% / minCAGR=19.15% / worstMaxDD=-37.68% / meanTurn=5.28`。
- 收尾 rotation 为 `stagnation_runs=3 / weekly_exit_buffer / rotate`；下一轮 focus -> candidates 池优先 `cap55/60 + hold8/9 + turn08/10 + wider sell_exit`，第一条命令建议在实现 `cap55_hold9_turn08_exit90_weekly` 与 `cap60_hold8_turn10_exit90_weekly` 后用五窗口 `--only-base-ids` 补跑。

## 本轮执行计划（2026-05-19 17:26 CST）

- 本轮新增并五窗口 `--only-base-ids` 补跑 3 个纯 `_weekly` 候选：`aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold7_turn10_weekly`、`aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold8_turn08_weekly`、`aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap55_hold4_turn18_weekly`；未混入 Path 1 周度仓位 overlay。
- Guard 后 Path 3 weekly universe 变为 `54` 个候选完整覆盖，收尾 `pass / blocking=0 / warning=0`。
- 新 `cap50_hold8_turn08` 成为 2017 window winner 与四窗口 robust：2017 `14.19% CAGR / -30.27% MaxDD / 0.64 Sharpe / 3.01 Turn`，2020 `14.49% / -25.32% / 0.60 / 3.06`，2023 `12.08% / -28.70% / 0.51 / 2.54`，2025 `63.76% / -25.62% / 1.24 / 6.04`。
- `cap55_hold7_turn10` 没有赢长窗，但 2026 短窗最好（`56.62% CAGR / -8.76% MaxDD / 1.57 Sharpe / 9.30 Turn`）；`risk40_cap55_hold4_turn18` 因 2020 只有 `9.47% CAGR` 被验证门槛拦截，虽有 2026 `113.78% CAGR`，换手已升到 `10.73`。
- `update_weighted_winners.py` 后 Path 3 official winners 为：2017 `cap50_hold8_turn08_weekly`，2020/2023 `cap60_hold6_turn12_weekly`，2025 `cap65_hold5_turn15_weekly`；robust 切为 `cap50_hold8_turn08_weekly`，`meanCAGR=26.13% / minCAGR=12.08% / worstMaxDD=-30.27% / meanTurn=3.66`。
- 收尾 rotation 为 `stagnation_runs=1 / turnover_reduction / continue`；下一轮继续尝试 `cap45/50 + hold9/10 + turn06/08`，以 2020/2023 不塌为前提压换手。

## 本轮执行计划（2026-05-19 11:12 CST）

- 本轮独立复核纯 `_weekly` universe，当前 `51/51` 个四窗口候选完整；未把 Path 1 的月度选股 + 周度仓位 overlay 或 Path 2 月频/双周候选混入本路径。
- `update_weighted_winners.py` 后 Path 3 official winners 保持成本压降结构：2017/2020/2023 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly`，2025 为 `cap65_hold5_turn15_weekly`。
- 当前四窗口指标为：2017 `11.10% CAGR / -35.13% MaxDD / 0.5455 Sharpe / 3.26 Turn`，2020 `16.15% / -27.90% / 0.6308 / 3.59`，2023 `19.31% / -30.35% / 0.7172 / 2.81`，2025 `78.31% / -24.26% / 1.3121 / 7.17`。
- 四窗口 robust candidate 仍为 `cap60_hold6_turn12_weekly`，`meanCAGR=23.60% / minCAGR=11.10% / worstMaxDD=-35.13% / meanTurn=4.33`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 3 rotation 为 `stagnation_runs=2 / turnover_reduction / continue`；下一轮继续比较更低换手、宽出场和风险降仓，短窗 2025 弹性不足以掩盖 2020/2023 的收益短板。

## 本轮执行计划（2026-05-19 05:29 CST）

- 本轮按 `cost_stress` 轮换方向新增并补跑两个纯 `_weekly` 候选：`aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn15_weekly` 与 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold6_turn12_weekly`，未混入 Path 1 周度仓位 overlay。
- Guard 对 Path 3 weekly universe 为 `51/51 complete / pass`；所有新增候选均用 `--only-base-ids` 完成 `since_2017_01/since_2020_01/since_2023_01/since_2025_01/since_2026_01` 增量覆盖。
- 新 `cap60_hold6_turn12` 四窗口表现为：2017 `11.10% CAGR / -35.13% MaxDD / 0.55 Sharpe / 3.26 Turn`，2020 `16.15% / -27.90% / 0.63 / 3.59`，2023 `19.31% / -30.35% / 0.72 / 2.81`，2025 `47.86% / -24.52% / 1.05 / 7.68`。
- `cap65_hold5_turn15` 2025 弹性更高（`78.31% CAGR / -24.26% MaxDD / 1.31 Sharpe / 7.17 Turn`），但 2020 只有 `11.83% CAGR`，未成为四窗口 robust。
- `update_weighted_winners.py` 后 Path 3 window winners 切换为：2017/2020/2023 `cap60_hold6_turn12_weekly`，2025 `cap65_hold5_turn15_weekly`。
- 四窗口 robust candidate 切换为 `cap60_hold6_turn12_weekly`，`meanCAGR=23.60% / minCAGR=11.10% / worstMaxDD=-35.13% / meanTurn=4.33`；收益低于旧高弹性周频，但换手与成本压力明显下降。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 3 rotation 重置为 `stagnation_runs=0 / recommended_focus=turnover_reduction / continue`；下一轮继续沿最短持有期、换手上限和降仓约束压成本。

## 本轮执行计划（2026-05-18 23:13 CST）

- 本轮通过 `update_weighted_winners.py` 独立巡检 Path 3，继续只使用纯 `_weekly` 口径；guard 对 Path 3 weekly universe 为 `49/49 complete / pass`，未把 Path 1 周度仓位 overlay 或 Path 2 月频/双周候选混入本路径。
- Path 3 window tracked winners 未换身份：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`。
- 当前四窗口指标分别为：2017 `23.50% CAGR / -40.04% MaxDD / 0.80 Sharpe / 7.71 Turn`，2020 `14.67% / -51.71% / 0.56 / 12.99`，2023 `35.18% / -37.14% / 0.96 / 13.65`，2025 `49.08% / -28.73% / 1.22 / 14.62`。
- 四窗口 robust candidate 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`，`meanCAGR=29.65% / minCAGR=19.14% / worstMaxDD=-37.68% / meanTurn=5.28`；2020 raw pullback 候选继续因 2023 验证不足被拦截。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 3 rotation 为 `stagnation_runs=10 / recommended_focus=cost_stress / rotate`；下一轮优先做交易成本压力、换手上限和风险降仓约束。

## 本轮执行计划（2026-05-18 20:34 CST）

- 本轮通过 `update_weighted_winners.py` 独立巡检 Path 3，继续只使用纯 `_weekly` 口径；guard 对 Path 3 weekly universe 为 `49/49 complete / pass`，未把 Path 1 周度仓位 overlay 或 Path 2 月频/双周候选混入本路径。
- Path 3 window tracked winners 未换身份：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`。
- 当前四窗口指标分别为：2017 `23.39% CAGR / -40.04% MaxDD / 0.800 Sharpe / 7.69 Turn`，2020 `14.45% / -51.71% / 0.558 / 12.95`，2023 `34.65% / -37.14% / 0.952 / 13.57`，2025 `48.32% / -28.73% / 1.207 / 14.52`。
- 四窗口 robust candidate 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`，`meanCAGR=29.52% / minCAGR=19.09% / worstMaxDD=-37.68% / meanTurn=5.23`；2020 raw pullback 候选继续因 2023 验证不足被拦截。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 3 rotation 为 `stagnation_runs=8 / recommended_focus=risk_downshift / rotate`；下一轮优先比较纯周频降仓、宽确认与换手上限，不提高单周进攻强度。

## 本轮执行计划（2026-05-18 11:11 CST）

- 本轮通过 `update_weighted_winners.py` 独立巡检 Path 3，继续只使用纯 `_weekly` 口径；guard 对 Path 3 weekly universe 为 `49/49 complete / pass`，未把 Path 1 周度仓位 overlay 或 Path 2 月频/双周候选混入本路径。
- Path 3 window tracked winners 未换身份：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`。
- 当前四窗口指标分别为：2017 `23.39% CAGR / -40.04% MaxDD / 0.800 Sharpe / 7.69 Turn`，2020 `14.45% / -51.71% / 0.558 / 12.95`，2023 `34.65% / -37.14% / 0.952 / 13.57`，2025 `48.32% / -28.73% / 1.207 / 14.52`。
- 四窗口 robust candidate 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`，`meanCAGR=29.52% / minCAGR=19.09% / worstMaxDD=-37.68% / meanTurn=5.23`；2020 单窗候选仍被 2023 验证门槛拦下。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 3 rotation 为 `stagnation_runs=3 / recommended_focus=weekly_exit_buffer / rotate`；下一轮优先比较宽出场、最短持有期和换手上限，不提高单周进攻强度。

## 本轮执行计划（2026-05-18 05:53 CST）

- 本轮新增并完整补跑纯周度候选 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`，Path 3 weekly universe 变为 `49/49 complete`；仍只使用 `_weekly` 口径，未把 Path 1 周度仓位 overlay 或 Path 2 月频/双周候选混入本路径。
- 新候选四窗口表现为：2017 `19.09% CAGR / -30.35% MaxDD / 0.763 Sharpe / 4.43 Turn`，2020 `19.85% / -25.77% / 0.747 / 4.03`，2023 `20.82% / -37.68% / 0.707 / 3.87`，2025 `58.32% / -22.35% / 1.188 / 8.57`。
- Path 3 window tracked winners 基本保持原结构：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`。
- 四窗口 robust candidate 切换为新候选 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn20_weekly`，`meanCAGR=29.52% / minCAGR=19.09% / worstMaxDD=-37.68% / meanTurn=5.23`；相比旧 `cap80_hold3_turn25`，换手降低且 min CAGR 略抬升。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 3 rotation 因 robust 变化重置为 `stagnation_runs=0 / recommended_focus=turnover_reduction / continue`；下一轮优先继续沿最短持有期、换手上限和降仓约束压成本。

## 本轮执行计划（2026-05-17 23:12 CST）

- 本轮通过 `update_weighted_winners.py` 独立巡检 Path 3，继续只使用纯 `_weekly` 口径；Path 1 周度仓位 overlay 与 Path 2 月频/双周候选未混入本路径。
- Guard 对 Path 3 weekly universe 仍为 `48/48 complete / pass`，A 股总体 coverage 维持 `pass / blocking=0 / warning=0`。
- Path 3 tracked winners 未变：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`。
- 四窗口 robust candidate 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.51% / minCAGR=18.80% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 2020 与 2025 的 raw weekly 候选继续被验证窗口拦截；主要代价仍是 2023 验证不足、高换手或深回撤，短窗弹性不直接晋升。
- 收尾 rotation 为 `stagnation_runs=18 / recommended_focus=risk_downshift / rotate`；下一轮优先比较纯周频降仓、宽出场和换手上限，而不是提高单周进攻强度。

## 本轮执行计划（2026-05-17 17:25 CST）

- 本轮通过 `update_weighted_winners.py` 独立巡检 Path 3，继续只使用纯 `_weekly` 口径；Path 1 月度选股 + 周度仓位 overlay 与 Path 2 月频/双周候选未混入本路径。
- Guard 对 Path 3 weekly universe 仍为 `48/48 complete / pass`；A 股总体 coverage 已由 13 个 warning 清到 `pass / blocking=0 / warning=0`。
- Path 3 tracked winners 未变：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`。
- 四窗口 robust candidate 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.51% / minCAGR=18.80% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 短窗 weekly raw leader 继续被验证口径拦截；2020 pullback 候选虽有约 `20.88% CAGR`，但 2023 验证窗口 `18.80%` 仍不足以替换，且高换手与深回撤代价未改善。
- 收尾 rotation 为 `stagnation_runs=15 / recommended_focus=weekly_exit_buffer / rotate`；下一轮优先比较宽出场、最短持有期与换手上限，不提高单周进攻强度。

## 本轮执行计划（2026-05-17 11:15 CST）

- 本轮通过 `update_weighted_winners.py` 独立巡检 Path 3，继续只使用纯 `_weekly` 口径；Path 1 月度选股 + 周度仓位 overlay 与 Path 2 月频/双周候选未混入本路径。
- Guard 对 Path 3 weekly universe 为 `48/48 complete / pass`；短窗 weekly raw leader 继续被验证口径拦截，主要问题仍是 2023 验证窗口不足、高回撤或高换手。
- Path 3 tracked winners 未变：2017 `80/20 equal_weight aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（`23.45% CAGR / -40.04% MaxDD / 0.80 Sharpe / 7.70 Turn`），2020 `80/20 total_mv aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`14.49% / -51.71% / 0.56 / 12.99`）。
- 2023 winner 仍为 `80/20 total_mv aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（`34.88% CAGR / -37.14% MaxDD / 0.95 Sharpe / 13.65 Turn`），2025 winner 仍为 `80/20 equal_weight aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`49.15% / -28.73% / 1.22 / 14.62`）。
- 四窗口 robust candidate 仍为 `80/20 equal_weight aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.51% / minCAGR=18.80% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 收尾 rotation 为 `stagnation_runs=12 / recommended_focus=turnover_reduction / rotate`；下一轮优先做纯周频换手压降与交易成本敏感性，不提高单周进攻强度。

## 本轮执行计划（2026-05-17 05:15 CST）

- 本轮通过 `update_weighted_winners.py` 独立巡检 Path 3，继续只使用纯 `_weekly` 口径；Path 1 的月度选股 + 周度仓位 overlay 与 Path 2 月频/双周候选未混入本路径。
- Guard 对 Path 3 weekly universe 为 `48/48 complete / pass`；短窗 weekly raw leader 继续被验证口径拦截，主要原因仍是 2023 验证窗口不足或高回撤、高换手代价过高。
- Path 3 tracked winners 未变：2017 `80/20 equal_weight aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（`23.45% CAGR / -40.04% MaxDD / 0.80 Sharpe / 7.70 Turn`），2020 `80/20 total_mv aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`14.49% / -51.71% / 0.56 / 12.99`）。
- 2023 winner 仍为 `80/20 total_mv aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（`34.88% CAGR / -37.14% MaxDD / 0.95 Sharpe / 13.65 Turn`），2025 winner 仍为 `80/20 equal_weight aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`49.15% / -28.73% / 1.22 / 14.62`）。
- 四窗口 robust candidate 仍为 `80/20 equal_weight aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.51% / minCAGR=18.80% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 收尾 rotation 为 `stagnation_runs=10 / recommended_focus=cost_stress / rotate`；下一轮优先复核纯周频在交易成本、换手上限与降仓约束下的存活性，不提高单周进攻强度。

## 本轮执行计划（2026-05-16 23:12 CST）

- 本轮通过 `update_weighted_winners.py` 独立巡检 Path 3，继续只使用纯 `_weekly` 口径；Path 1 的周度仓位 overlay 与 Path 2 月频/双周候选未混入本路径。
- Guard 对 Path 3 weekly universe 为 `48/48 complete / pass`；短窗 raw weekly 爆发继续被验证口径拦截，原因仍是 2023 验证窗口不足或回撤/换手代价过高。
- Path 3 tracked winners 未变：2017 `80/20 equal_weight aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（`23.45% CAGR / -40.04% MaxDD / 0.80 Sharpe / 7.70 Turn`），2020 `80/20 total_mv aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`14.49% / -51.71% / 0.56 / 12.99`）。
- 2023 winner 仍为 `80/20 total_mv aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（`34.88% CAGR / -37.14% MaxDD / 0.95 Sharpe / 13.65 Turn`），2025 winner 仍为 `80/20 equal_weight aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`49.15% / -28.73% / 1.22 / 14.62`）。
- 四窗口 robust candidate 仍为 `80/20 equal_weight aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.51% / minCAGR=18.80% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 收尾 rotation 为 `stagnation_runs=8 / recommended_focus=risk_downshift / rotate`；下一轮优先做纯周频降仓、宽确认与换手压降，不提高单周进攻强度。

## 本轮执行计划（2026-05-16 17:14 CST）

- 本轮 Path 3 随 A 股 comparison 重建与 `update_weighted_winners.py` 独立巡检完成；纯 `_weekly` 候选继续与 Path 1 的月度选股 + 周度仓位 overlay 分离。
- Path 3 tracked winners 当前为：2017 `80/20 equal_weight aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（`23.45% CAGR / -40.04% MaxDD / 0.80 Sharpe / 7.70 Turn`），2020 `80/20 total_mv aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`14.49% / -51.71% / 0.56 / 12.99`）。
- 2023 winner 为 `80/20 total_mv aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（`34.88% CAGR / -37.14% MaxDD / 0.95 Sharpe / 13.65 Turn`），2025 winner 为 `80/20 equal_weight aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`49.15% / -28.73% / 1.22 / 14.62`）。
- 四窗口 robust candidate 为 `80/20 equal_weight aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.51% / minCAGR=18.80% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 若只看短窗，部分 weekly 候选在 2025 爆发很强，但因 2023 验证窗口 CAGR 接近零或不足被拒；继续记录高换手和深回撤代价，不并入 Path 2/月度逻辑。
- 收尾 rotation 为 `stagnation_runs=6 / recommended_focus=risk_downshift / rotate`；下一轮优先做纯周频降仓、宽确认与换手压降。

## 本轮执行计划（2026-05-16 11:20 CST）

- 本轮继续只使用纯 `_weekly` 口径，Path 1 周度仓位 overlay 与 Path 2 月频高收益候选未混入 Path 3；guard 对 Path 3 weekly universe 为 `48/48 complete / pass`。
- `update_weighted_winners.py` 后 Path 3 tracked winners 未变：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`。
- 四窗口 robust candidate 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.51% / minCAGR=18.80% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 2020 窗口仍是核心短板：当前 winner 仅 `14.49% CAGR`，且 `MaxDD=-51.71% / Turn=12.99`；短窗周频爆发继续因 2023 验证不足被拒绝。
- 收尾 rotation 为 `stagnation_runs=2 / recommended_focus=turnover_reduction / continue`；下一轮优先比较周频换手上限、宽出场与风险降仓，而不是提高单周进攻强度。

## 本轮执行计划（2026-05-16 06:56 CST）

- 本轮继续只使用纯 `_weekly` 口径，Path 1 的周度仓位 overlay 与 Path 2 的月频高收益候选没有混入 Path 3；guard 对 Path 3 pure weekly universe 为 `48/48 complete / pass`。
- `update_weighted_winners.py` 后 Path 3 tracked winners 为：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`。
- 四窗口 robust candidate 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.51% / minCAGR=18.80% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 2020 窗口仍是 Path 3 的核心短板，当前 winner 仅 `14.49% CAGR` 且 `MaxDD=-51.71% / Turn=12.99`；短窗 2025 弹性仍未抵消中长窗口的高换手与深回撤代价。
- 收尾 rotation 为 `stagnation_runs=7 / recommended_focus=risk_downshift / rotate`；下一轮优先比较周频降仓、宽出场和换手上限，不继续单纯提高周频进攻强度。

## 本轮执行计划（2026-05-15 15:16 CST）

- 本轮通过 `scripts/update_weighted_winners.py` 继续只使用纯 `_weekly` 口径；Path 1 的周度仓位 overlay 与 Path 2 的月频候选没有混入 Path 3。
- Path 3 tracked winners 未变，仍由 `weekly_alpha_pullback` 族占据：2017/2020 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，2023 为 `aggr_08_92_prom6_weekly_alpha_pullback_risk50_cap40_hold2_turn40_weekly`，2025 为 `aggr_05_95_prom3_weekly_alpha_pullback_risk50_cap60_hold2_turn30_weekly`。
- 四窗口 robust candidate 仍为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.95% / minCAGR=19.02% / worstMaxDD=-37.64% / meanTurn=6.07`。
- `weekly_alpha_balanced` 的 2025 raw 候选继续被验证口径拒绝：对应 2023 验证窗口低于当前 `pullback` incumbent 的 70% 门槛，说明短窗爆发仍未形成可持续替换。
- 最终 rotation 为 `stagnation_runs=3 / recommended_focus=weekly_exit_buffer / rotate`；下一轮优先比较宽出场、最短持有期与换手上限，不继续单纯提高周频进攻强度。

## 本轮执行计划（2026-05-15 10:14 CST）

- 本轮补跑并完整覆盖 `weekly_alpha_balanced / breakout / pullback` 的等权与总市值底座缺口，五窗口 aggregate 重建后 `weekly_alpha` 行数为 `189`，最终 guard 对 Path 3 pure weekly universe 为 `pass`。
- Path 3 tracked winners 已切到 `weekly_alpha_pullback` 族：2017/2020 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`（`19.02% / 21.13% CAGR`），2023 为 `aggr_08_92_prom6_weekly_alpha_pullback_risk50_cap40_hold2_turn40_weekly`（`22.19% CAGR`），2025 为 `aggr_05_95_prom3_weekly_alpha_pullback_risk50_cap60_hold2_turn30_weekly`（`76.26% CAGR`）。
- 四窗口 robust candidate 同步为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.95% / minCAGR=19.02% / worstMaxDD=-37.64% / meanTurn=6.07`；总市值 `balanced` 的 2025 raw `91.87% CAGR` 因 2023 验证不足被拒绝。
- 最终 rotation 为 `stagnation_runs=1 / turnover_reduction`；下一轮优先沿 `weekly_alpha_pullback` 做宽出场、换手上限与最短持有期敏感性，而不是继续提高单周进攻强度。

## 本轮执行计划（2026-05-14 周频信号修正）

- 新增 `weekly_alpha_balanced / weekly_alpha_breakout / weekly_alpha_pullback` 三类周频专用信号，使用 3-1/6-1 动量、近 1 月强弱、放量、20 日突破、行业强度/龙头度与质量分数，而不是只把月频 6-1 动量改成每周调仓。
- 新增周频执行约束：`weekly_min_hold_periods` 控制最短持有周数，`weekly_turnover_cap` 控制单期目标换手；当目标仓位低于当前仓位时视为风险降仓，约束自动让路。
- 新增 9 个 `_weekly` 变体，覆盖三类周频 alpha × 三种组合形态（8/92 prom6、5/95 prom3、3/97 prom2），继续由 Path 3 的纯 `_weekly` 口径独立跟踪。

## 本轮执行计划（2026-05-14 22:55 CST）

- 本轮 guard blocking coverage 已补齐，Path 3 pure weekly universe 收尾为 `pass`；`update_weighted_winners.py` 继续只使用纯 `_weekly` 口径，月度选股 + 周度仓位 overlay 没有混入本路径。
- Path 3 tracked winners 当前为：2017 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（`23.87% CAGR / -40.04% MaxDD / 0.8106 Sharpe / 7.70 Turn`），2020 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`14.98% / -51.71% / 0.5707 / 12.99`），2023 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`（`35.93% / -37.14% / 0.9743 / 13.65`），2025 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`52.69% / -28.73% / 1.2740 / 14.62`）。
- 四窗口 robust candidate 为 `aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=23.57% / minCAGR=16.05% / worstMaxDD=-46.64% / meanTurn=11.00`；raw 2025 高爆发单周候选继续因 2023 验证窗口失效被拒绝。
- 最终 guard 为 `stagnation_runs=1 / recommended_focus=turnover_reduction`；下一轮优先评估新 `weekly_alpha_*` 变体的宽出场、最短持有和换手上限，而不是提高单周进攻强度。

## 本轮执行计划（2026-05-14 15:10 CST）

- 本轮研究守卫收尾 coverage gate 为 `pass`，Path 3 pure weekly universe 继续为 `30` 个四窗口完整候选；收尾 rotation 为 `stagnation_runs=13 / recommended_focus=turnover_reduction`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，Path 3 继续只使用纯 `_weekly` 口径；Path 1 周度仓位 overlay 与 Path 2 月频候选没有混入本路径。
- Path 3 tracked winners 未换身份：2017 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023/2025 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`。
- 最新指标分别为 `23.85% / 15.42% / 36.91% / 52.85% CAGR`；2020 窗口仍是主要短板，且 raw 2025 的 `aggr_01_99_prom1...cap100_weekly` 继续因 2023 验证窗口失效被拒绝。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=23.88% / minCAGR=16.12% / worstMaxDD=-46.64% / meanTurn=11.00`。
- 下一轮按 turnover_reduction 新增或复跑纯周度降换手候选，优先比较更少持仓切换、宽出场与交易成本压力；短窗爆发型 `_weekly` 继续单独记录，不回并到 Path 2。

## 本轮执行计划（2026-05-14 09:13 CST）

- 本轮研究守卫收尾 coverage gate 为 `pass`，Path 3 pure weekly universe 继续为 `30` 个四窗口完整候选；收尾 rotation 为 `stagnation_runs=11 / recommended_focus=cost_stress`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，Path 3 继续只使用纯 `_weekly` 口径；Path 1 周度仓位 overlay 与 Path 2 月频候选没有混入本路径。
- Path 3 tracked winners 未换身份：2017 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023/2025 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`。
- 最新指标分别为 `23.85% / 15.42% / 36.91% / 52.85% CAGR`；2020 窗口仍是主要短板，且 raw 2025 的 `aggr_01_99_prom1...cap100_weekly` 继续因 2023 验证窗口失效被拒绝。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=23.88% / minCAGR=16.12% / worstMaxDD=-46.64% / meanTurn=11.00`。
- 下一轮只做交易成本压力与换手敏感性验证；短窗爆发型 `_weekly` 候选继续单独记录，不回并到 Path 2。

## 本轮执行计划（2026-05-14 03:17 CST）

- 本轮 guard 覆盖率为 `pass`，Path 3 pure weekly universe 继续为 `30` 个四窗口完整候选；收盘 guard 将 Path 3 rotation 推进到 `stagnation_runs=9 / recommended_focus=cost_stress`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后仍只使用纯 `_weekly` 口径，Path 1 周度仓位 overlay 与 Path 2 月频候选没有混入 Path 3。
- Path 3 tracked winners 未换身份：2017 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023/2025 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`。
- 最新指标分别为 `23.85% / 15.42% / 36.91% / 52.85% CAGR`；2020 窗口仍弱，且 raw 2025 的 `aggr_01_99_prom1...cap100_weekly` 继续因 2023 验证窗口失效被拒绝。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=23.88% / minCAGR=16.12% / worstMaxDD=-46.64% / meanTurn=11.00`。
- 下一步只比较周频降仓、宽出场与交易成本压力下的存活性，不把短窗爆发型 `_weekly` 候选并入 Path 2。

## 本轮执行计划（2026-05-13 21:21 CST）

- 本轮复跑 `scripts/update_weighted_winners.py` 后继续只使用纯 `_weekly` 口径；Path 1 周度仓位 overlay 与 Path 2 月频高收益候选仍未混入 Path 3。
- Path 3 tracked winners 未换身份：2017 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，2020 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，2023/2025 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`。
- 最新指标分别为 `23.85% / 15.42% / 36.91% / 52.85% CAGR`；2020 窗口仍弱，且 2025 raw weekly 爆发候选继续因 2023 验证失败被拒绝。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=23.88% / minCAGR=16.12% / worstMaxDD=-46.64% / meanTurn=11.00`。
- rotation 已提示下一轮 Path 3 转向 `risk_downshift`，重点应比较周频降仓/退出缓冲，而不是继续提高短窗进攻强度。

## 本轮执行计划（2026-05-13 09:13 CST）

- 本轮复跑 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 1 的周度仓位 overlay 与 Path 2 的月频高收益候选均未混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.69% CAGR / -40.04% MaxDD / 0.8063 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`15.11% CAGR / -51.71% MaxDD / 0.5739 Sharpe / 12.99 Turnover`；raw 更高的 `aggr_01_99_prom1...cap100_weekly` 继续因 2023 验证窗口失效被拒绝。
- `since_2023_01` 与 `since_2025_01` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `36.20% / -37.14% / 0.9791 / 13.65` 与 `51.67% / -27.38% / 1.2897 / 13.73`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=23.57% / minCAGR=15.89%`；高换手和深回撤仍是本路径的核心代价，继续独立记录。

## 本轮执行计划（2026-05-13 03:32 CST）

- 本轮复跑 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；月度选股加周度仓位 overlay 未混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.69% CAGR / -40.04% MaxDD / 0.8063 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`15.11% CAGR / -51.71% MaxDD / 0.5739 Sharpe / 12.99 Turnover`；纯周度路线的 2020 窗口仍是主要短板。
- `since_2023_01` 与 `since_2025_01` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `36.20% / -37.14% / 0.9791 / 13.65` 与 `51.67% / -27.38% / 1.2897 / 13.73`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=23.57% / minCAGR=15.89%`；短窗爆发候选继续被验证窗口拒绝，高换手与深回撤代价保留记录。

## 本轮执行计划（2026-05-12 21:20 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 的 `risk40...caution80` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.69% CAGR / -40.04% MaxDD / 0.8063 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`15.11% CAGR / -51.71% MaxDD / 0.5739 Sharpe / 12.99 Turnover`；纯周度路线继续没有形成 2020 可持续优势。
- `since_2023_01` 与 `since_2025_01` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `36.20% / -37.14% / 0.9791 / 13.65` 与 `51.67% / -27.38% / 1.2897 / 13.73`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=23.57% / minCAGR=15.89%`；短窗爆发候选仍被验证窗口拒绝，高换手和深回撤代价继续单独记录。

## 本轮执行计划（2026-05-12 09:12 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 新增的 `risk40_mom_exit60_reconfirm70/reconfirm75` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.30% CAGR / -40.04% MaxDD / 0.7969 Sharpe / 7.69 Turnover`。
- `since_2020_01` winner 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`14.63% CAGR / -51.71% MaxDD / 0.5620 Sharpe / 12.94 Turnover`；纯周度路线继续没有形成 2020 可持续优势。
- `since_2023_01` 与 `since_2025_01` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `34.85% / -37.14% / 0.9540 / 13.57` 与 `46.84% / -27.38% / 1.2063 / 13.45`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.09% / minCAGR=15.54% / worstMaxDD=-46.64% / meanTurn=10.95`；高换手与深回撤代价继续单独记录。

## 本轮执行计划（2026-05-12 03:16 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 新增的 `risk50_mom_exit60_reconfirm70/reconfirm65` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.30% CAGR / -40.04% MaxDD / 0.7969 Sharpe / 7.69 Turnover`。
- `since_2020_01` winner 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`14.63% CAGR / -51.71% MaxDD / 0.5620 Sharpe / 12.94 Turnover`；raw 更高的短窗候选继续因深回撤/验证口径不替换。
- `since_2023_01` 与 `since_2025_01` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `34.85% / -37.14% / 0.9540 / 13.57` 与 `46.84% / -27.38% / 1.2063 / 13.45`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.09% / minCAGR=15.54% / worstMaxDD=-46.64% / meanTurn=10.95`；高换手与深回撤代价继续单独记录。

## 本轮执行计划（2026-05-11 21:22 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 新增的 `risk50_mom_exit60_reconfirm75_caution80/caution75` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.30% CAGR / -40.04% MaxDD / 0.7969 Sharpe / 7.69 Turnover`。
- `since_2020_01` winner 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`14.63% CAGR / -51.71% MaxDD / 0.5620 Sharpe / 12.94 Turnover`；raw 更高的短窗候选仍因深回撤/验证口径不替换。
- `since_2023_01` 与 `since_2025_01` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `34.85% / -37.14% / 0.9540 / 13.57` 与 `46.84% / -27.38% / 1.2063 / 13.45`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.09% / minCAGR=15.54% / worstMaxDD=-46.64% / meanTurn=10.95`；高换手与深回撤代价继续单独记录。

## 本轮执行计划（2026-05-11 15:15 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 新增的 `risk50_mom_exit60_caution80/caution75` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`14.67% CAGR / -51.71% MaxDD / 0.5628 Sharpe / 12.98 Turnover`；纯周度路线继续没有形成 2020 可持续优势。
- `since_2023_01` 与 `since_2025_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `35.09% / -37.14% / 0.9568 / 13.65` 与 `47.65% / -27.38% / 1.2150 / 13.64`。
- 四窗口鲁棒候选仍为 `aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.29% / minCAGR=15.59% / worstMaxDD=-46.64% / meanTurn=11.03`；高换手和深回撤代价继续单独记录。

## 本轮执行计划（2026-05-11 09:19 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 新增的 `risk50_mom_exit60_reconfirm*` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`14.67% CAGR / -51.71% MaxDD / 0.5628 Sharpe / 12.98 Turnover`；raw 单窗口最高的 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 仍因深回撤与短窗化不替换验证 winner。
- `since_2023_01` 与 `since_2025_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `35.09% / -37.14% / 0.9568 / 13.65` 与 `47.65% / -27.38% / 1.2150 / 13.64`。
- 四窗口鲁棒候选仍为 `aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.29% / minCAGR=15.59% / worstMaxDD=-46.64% / meanTurn=11.03`；高换手和高回撤代价继续单独记录。

## 本轮执行计划（2026-05-11 03:13 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 新增的 `risk50_mom_top12/top18` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`14.67% CAGR / -51.71% MaxDD / 0.5628 Sharpe / 12.98 Turnover`，继续未形成可持续优势。
- `since_2023_01` 与 `since_2025_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `35.09% / -37.14% / 0.9568 / 13.65` 与 `47.65% / -27.38% / 1.2150 / 13.64`。
- 四窗口鲁棒候选仍为 `aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.29% / minCAGR=15.59% / worstMaxDD=-46.64% / meanTurn=11.03`；高换手和深回撤代价继续单独记录。

## 本轮执行计划（2026-05-10 21:14 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 新增的 `risk50_mom_caution*` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- 验证口径下，`since_2020_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`14.67% CAGR / -51.71% MaxDD / 0.5628 Sharpe / 12.98 Turnover`，继续未形成可持续优势。
- `since_2023_01` 与 `since_2025_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，分别为 `35.09% / -37.14% / 0.9568 / 13.65` 与 `47.65% / -27.38% / 1.2150 / 13.64`。
- 四窗口鲁棒候选仍为 `aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.29% / minCAGR=15.59% / worstMaxDD=-46.64% / meanTurn=11.03`；高换手和深回撤代价继续单独记录。

## 本轮执行计划（2026-05-10 15:04 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；Path 2 新增的 `risk50_mom_confirm*` 月频候选没有混入 Path 3。
- Path 3 `since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- 验证口径同步后，`since_2020_01` winner 为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`14.67% CAGR / -51.71% MaxDD / 0.5628 Sharpe / 12.98 Turnover`，继续没有形成可持续优势。
- `since_2023_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，`35.09% CAGR / -37.14% MaxDD / 0.9568 Sharpe / 13.65 Turnover`；`since_2025_01` 同步为同一 `cap40_weekly`，`47.65% / -27.38% / 1.2150 / 13.64`。
- 四窗口鲁棒候选仍为 `aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.29% / minCAGR=15.59% / worstMaxDD=-46.64% / meanTurn=11.03`；高换手和深回撤代价继续单独记录。

## 本轮执行计划（2026-05-10 09:17 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；A 股 Path 2 新增的 `risk50_mom_exit80/exit60` 月频候选没有混入 Path 3。
- Path 3 四个窗口 winner 未发生身份漂移：`since_2017_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`19.38% CAGR / -49.93% MaxDD / 0.5755 Sharpe / 8.78 Turnover`，继续没有形成可持续优势。
- `since_2023_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，`35.09% CAGR / -37.14% MaxDD / 0.9568 Sharpe / 13.65 Turnover`；`since_2025_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`181.26% / -40.77% / 1.6970 / 16.50`。
- 四窗口鲁棒候选仍为 `aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.29% / minCAGR=15.59% / worstMaxDD=-46.64% / meanTurn=11.03`；高换手和深回撤代价继续单独记录。

## 本轮执行计划（2026-05-10 03:16 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；月度选股 + 周度仓位 overlay 没有混入 Path 3。
- Path 3 四个窗口 winner 未发生身份漂移：`since_2017_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`19.38% CAGR / -49.93% MaxDD / 0.5755 Sharpe / 8.78 Turnover`，继续没有形成可持续优势。
- `since_2023_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，`35.09% CAGR / -37.14% MaxDD / 0.9568 Sharpe / 13.65 Turnover`；`since_2025_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`181.26% / -40.77% / 1.6970 / 16.50`。
- 本轮有效同步修正是四窗口鲁棒候选切到 `aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80_weekly`，`meanCAGR=22.29% / minCAGR=15.59% / worstMaxDD=-46.64% / meanTurn=11.03`；最低 CAGR 从旧候选的负值区间转正，但高换手与深回撤代价仍需单独跟踪。

## 本轮执行计划（2026-05-09 21:14 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；月度选股 + 周度仓位 overlay 没有混入 Path 3。
- Path 3 tracked winners 未发生身份漂移：`since_2017_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`19.38% CAGR / -49.93% MaxDD / 0.5755 Sharpe / 8.78 Turnover`，继续没有形成可持续优势。
- `since_2023_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，`35.09% CAGR / -37.14% MaxDD / 0.9568 Sharpe / 13.65 Turnover`；`since_2025_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`181.26% / -40.77% / 1.6970 / 16.50`。
- 四窗口鲁棒候选仍是 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`meanCAGR=51.14% / minCAGR=-2.19% / worstMaxDD=-74.57% / meanTurn=11.22`，继续独立记录高换手和深回撤代价。

## 本轮执行计划（2026-05-09 18:09 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；月度选股 + 周度仓位 overlay 没有混入 Path 3。
- Path 3 tracked winners 未发生身份漂移：`since_2017_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`19.38% CAGR / -49.93% MaxDD / 0.5755 Sharpe / 8.78 Turnover`，继续没有形成可持续优势。
- `since_2023_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，`35.09% CAGR / -37.14% MaxDD / 0.9568 Sharpe / 13.65 Turnover`；`since_2025_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`181.26% / -40.77% / 1.6970 / 16.50`。
- 四窗口鲁棒候选仍是 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`meanCAGR=51.14% / minCAGR=-2.19% / worstMaxDD=-74.57% / meanTurn=11.22`，继续独立记录高换手和深回撤代价。

## 本轮执行计划（2026-05-09 13:04 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；月度选股 + 周度仓位 overlay 没有混入 Path 3。
- Path 3 tracked winners 未发生身份漂移：`since_2017_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`19.38% CAGR / -49.93% MaxDD / 0.5755 Sharpe / 8.78 Turnover`，继续没有形成可持续优势。
- `since_2023_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，`35.09% CAGR / -37.14% MaxDD / 0.9568 Sharpe / 13.65 Turnover`；`since_2025_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`181.26% / -40.77% / 1.6970 / 16.50`。
- 四窗口鲁棒候选仍是 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`meanCAGR=51.14% / minCAGR=-2.19% / worstMaxDD=-74.57% / meanTurn=11.22`，继续独立记录高换手和深回撤代价。

## 本轮执行计划（2026-05-09 05:08 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；月度选股 + 周度仓位 overlay 没有混入 Path 3。
- Path 3 tracked winners 未发生身份漂移：`since_2017_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`19.38% CAGR / -49.93% MaxDD / 0.5755 Sharpe / 8.78 Turnover`，继续没有形成可持续优势。
- `since_2023_01` 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，`35.09% CAGR / -37.14% MaxDD / 0.9568 Sharpe / 13.65 Turnover`；`since_2025_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`181.26% / -40.77% / 1.6970 / 16.50`。
- 四窗口鲁棒候选仍是 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`meanCAGR=51.14% / minCAGR=-2.19% / worstMaxDD=-74.57% / meanTurn=11.22`，继续独立记录高换手和深回撤代价。

## 本轮执行计划（2026-05-08 23:12 CST）

- 本轮运行 `.venv/bin/python scripts/update_weighted_winners.py`，继续只使用 `_matches_path3()` 的纯 `_weekly` 口径；月度选股 + 周度仓位 overlay 没有混入 Path 3。
- Path 3 继续独立使用纯 `_weekly` 口径；随 fresh comparison 同步后，`since_2017_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`23.36% CAGR / -40.04% MaxDD / 0.7977 Sharpe / 7.70 Turnover`。
- `since_2020_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`19.38% CAGR / -49.93% MaxDD / 0.5755 Sharpe / 8.78 Turnover`，继续未形成可持续优势。
- `since_2023_01` 从 `cap60_weekly` 切到 `aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`，`35.09% CAGR / -37.14% MaxDD / 0.9568 Sharpe / 13.65 Turnover`。
- `since_2025_01` 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口鲁棒候选同名，`meanCAGR=51.14% / minCAGR=-2.19% / worstMaxDD=-74.57% / meanTurn=11.22`，继续独立记录高换手和深回撤代价。

## 本轮执行计划（2026-05-08 17:24 CST）

- 本轮继续只使用 `scripts/update_weighted_winners.py` 中 `_matches_path3()` 的纯 `_weekly` 口径；没有把月度选股 + 周度 overlay 混入 Path 3。
- 复核后 Path 3 tracked winners 未发生身份漂移：`since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`22.91% CAGR / -40.04% MaxDD / 0.7889 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`18.56% CAGR / -49.93% MaxDD / 0.5621 Sharpe / 8.78 Turnover`，继续未形成可持续优势。
- `since_2023_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`34.31% CAGR / -37.14% MaxDD / 0.9391 Sharpe / 13.59 Turnover`。
- `since_2025_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`172.51% CAGR / -40.77% MaxDD / 1.6610 Sharpe / 16.50 Turnover`；四窗口鲁棒候选同名，`minCAGR=-3.44% / worstMaxDD=-74.57% / meanTurn=11.22`，继续单独记录高换手和深回撤代价。

## 本轮执行计划（2026-05-08 13:15 CST）

- 本轮继续只使用 `scripts/update_weighted_winners.py` 中 `_matches_path3()` 的纯 `_weekly` 口径；没有把月度选股 + 周度 overlay 混入 Path 3。
- 复核后 Path 3 tracked winners 未发生身份漂移：`since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`22.91% CAGR / -40.04% MaxDD / 0.7889 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`18.56% CAGR / -49.93% MaxDD / 0.5621 Sharpe / 8.78 Turnover`，继续未形成可持续优势。
- `since_2023_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`34.31% CAGR / -37.14% MaxDD / 0.9391 Sharpe / 13.59 Turnover`。
- `since_2025_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`172.51% CAGR / -40.77% MaxDD / 1.6610 Sharpe / 16.50 Turnover`；四窗口鲁棒候选同名，`minCAGR=-3.44%`，继续记录高换手和深回撤代价。

## 本轮执行计划（2026-05-08 07:28 CST）

- 本轮继续只使用 `scripts/update_weighted_winners.py` 中 `_matches_path3()` 的纯 `_weekly` 口径；没有把月度选股 + 周度 overlay 混入 Path 3。
- 复核后 Path 3 tracked winners 未发生身份漂移：`since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`22.91% CAGR / -40.04% MaxDD / 0.7889 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`18.56% CAGR / -49.93% MaxDD / 0.5621 Sharpe / 8.78 Turnover`，继续未形成可持续优势。
- `since_2023_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`34.31% CAGR / -37.14% MaxDD / 0.9391 Sharpe / 13.59 Turnover`。
- `since_2025_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`172.51% CAGR / -40.77% MaxDD / 1.6610 Sharpe / 16.50 Turnover`；四窗口鲁棒候选同名，`minCAGR=-3.44%`，继续记录高换手和深回撤代价。

## 本轮执行计划（2026-05-07 23:12 CST）

- 本轮继续只使用 `scripts/update_weighted_winners.py` 中 `_matches_path3()` 的纯 `_weekly` 口径；没有把月度选股 + 周度 overlay 混入 Path 3。
- 复核后 Path 3 tracked winners 未发生身份漂移，但指标随 `as_of=2026-05-07` 同步更新：`since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`22.91% CAGR / -40.04% MaxDD / 0.7889 Sharpe / 7.75 Turnover`。
- `since_2020_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`18.56% CAGR / -49.93% MaxDD / 0.5621 Sharpe / 8.78 Turnover`，继续未形成可持续优势。
- `since_2023_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`34.31% CAGR / -37.14% MaxDD / 0.9391 Sharpe / 13.84 Turnover`。
- `since_2025_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`172.51% CAGR / -40.77% MaxDD / 1.6610 Sharpe / 16.50 Turnover`；四窗口鲁棒候选同名，`minCAGR=-3.44%`，继续记录高换手和深回撤代价。

## 本轮执行计划（2026-05-07 11:10 CST）

- 本轮继续只使用 `scripts/update_weighted_winners.py` 中 `_matches_path3()` 的纯 `_weekly` 口径；没有把月度选股 + 周度 overlay 混入 Path 3。
- 复核后 Path 3 tracked winners 未漂移：`since_2017_01` winner 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`22.25% CAGR / -40.04% MaxDD / 0.7745 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`18.17% CAGR / -49.93% MaxDD / 0.5557 Sharpe / 8.78 Turnover`，继续未形成可持续优势。
- `since_2023_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`33.30% CAGR / -37.14% MaxDD / 0.9212 Sharpe / 13.59 Turnover`。
- `since_2025_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`168.30% CAGR / -40.77% MaxDD / 1.6420 Sharpe / 16.50 Turnover`；四窗口鲁棒候选同名，`minCAGR=-4.05%`，继续记录高换手和深回撤代价。

## 本轮执行计划（2026-05-07 05:06 CST）

- 本轮继续只使用 `scripts/update_weighted_winners.py` 中 `_matches_path3()` 的纯 `_weekly` 口径；不把月度选股 + 周度 overlay 混入 Path 3。
- 复核后 Path 3 tracked winners 未漂移：`since_2017_01` winner 为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，`22.25% CAGR / -40.04% MaxDD / 0.7745 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`18.17% CAGR / -49.93% MaxDD / 0.5557 Sharpe / 8.78 Turnover`；未形成可持续优势。
- `since_2023_01` winner 仍为 `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，`33.30% CAGR / -37.14% MaxDD / 0.9212 Sharpe / 13.59 Turnover`。
- `since_2025_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`168.30% CAGR / -40.77% MaxDD / 1.6420 Sharpe / 16.50 Turnover`；四窗口鲁棒候选同名，但 `minCAGR=-4.05%`，继续独立跟踪高换手和深回撤代价。

## 本轮执行计划（2026-05-06 23:15 CST）

- 本轮继续只使用 `scripts/update_weighted_winners.py` 中 `_matches_path3()` 的纯 `_weekly` 口径，未把月度选股 + 周度 overlay 混入 Path 3。
- 复核后 `since_2017_01` winner 为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`，指标为 `22.25% CAGR / -40.04% MaxDD / 0.7745 Sharpe / 7.70 Turnover`。
- `since_2020_01` winner 为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，指标为 `18.17% CAGR / -49.93% MaxDD / 0.5557 Sharpe / 8.78 Turnover`，仍未形成可持续优势。
- `since_2023_01` winner 为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`，指标为 `33.30% CAGR / -37.14% MaxDD / 0.9212 Sharpe / 13.59 Turnover`。
- `since_2025_01` winner 仍为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`168.30% CAGR / -40.77% MaxDD / 1.6420 Sharpe / 16.50 Turnover`，继续属于短窗爆发型。
- 四窗口鲁棒候选同为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，但 `minCAGR=-4.05% / worstMaxDD=-74.57% / meanTurn=11.22`，高换手和深回撤代价仍需单独记录。

## 本轮执行计划（2026-05-06 11:35 CST）

- 先运行 `.venv/bin/python scripts/update_weighted_winners.py`，使用脚本内 `_matches_path3()` 的 `_weekly` 口径检查四窗口 Path 3 winner 与四窗口鲁棒候选。
- 本轮只在现有纯周度候选上做复核；若缓存和运行时允许，再考虑补跑更有针对性的 `_weekly` variants，但不把月度选股 + 周度 overlay 混入 Path 3。
- 重点记录 `since_2020_01` 与 `since_2023_01` 是否能获得可持续改善，同时如实记录高换手和高回撤代价；短窗爆发、长窗失效或鲁棒候选最低 CAGR 为负都保留跟踪。
- 本轮复核结果：`since_2017_01` winner 为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`（`21.57% CAGR / -40.04% MaxDD / 0.7574 Sharpe / 7.66 Turnover`）。
- `since_2020_01` winner 为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_weekly`（`17.15% CAGR / -28.61% MaxDD / 0.7369 Sharpe / 7.18 Turnover`），未形成相对 Path 1/Path 2 的可持续优势。
- `since_2023_01` winner 为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`（`32.97% CAGR / -37.14% MaxDD / 0.9100 Sharpe / 13.47 Turnover`），收益高于 Path 1 2023 窗口但回撤和换手代价明显更高。
- `since_2025_01` winner 为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`（`156.73% CAGR / -40.77% MaxDD / 1.5775 Sharpe / 16.06 Turnover`），属于短窗爆发型 winner。
- 四窗口鲁棒候选同为 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，但 `minCAGR=-6.32% / worstMaxDD=-74.57% / meanTurn=11.01`，说明纯周度路径仍需独立跟踪，不应并入 Path 2。
## 本轮执行计划（2026-06-01 16:23 CST）

- 上一轮候选/结果摘要：上一轮建议先归档低换手失败线 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly`，再测试 `cost_guard_cap66_hold7_turn04_exit90_weekly`，检查更宽持仓与成本防守是否能保住 2020/2023。
- 本轮已归档：`PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS` 新增 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap64_hold8_turn03_exit92_weekly`，原因是低换手/低风险线连续未改善中窗，继续占用 active pool 会稀释纯周度候选质量。
- 本轮候选 ID：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap66_hold7_turn04_exit90_weekly`。
- 五窗口结果：CAGR 为 `10.48% / 1.28% / -0.74% / 3.16% / 45.18%`，最大回撤为 `-30.33% / -44.03% / -28.56% / -26.10% / -15.03%`，换手为 `2.79x / 2.96x / 2.94x / 3.66x / 6.17x`。除 2026 观察窗外全面弱于现有 Path 3 tracked winners，未改变 window winner 或 robust candidate。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction`，但本轮说明继续降低换手/放宽持仓不能解决 2020/2023。下一轮第一候选建议回到较高质量暴露并只加轻度成本闸门：`aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap52_hold5_turn12_exit88_weekly`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap52_hold5_turn12_exit88_weekly`。

## 本轮执行计划（2026-06-02 22:30 CST）

- 上一轮候选/结果摘要：上一轮 `cost_guard_cap68_hold6_turn08_exit90_weekly` 仍没有修复 2020/2023，本轮先把该低换手失败线归档，再测试纯周度 `cash_off_and_cap50_hold2_turn12_exit90_weekly`，检查更短持仓和较低 cap 是否能改善短窗同时保住中窗。
- 本轮已归档：`PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS` 新增 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold6_turn08_exit90_weekly`。evict 原因：连续低换手 pullback 线在 2020/2023 中窗弱，继续保留会挤占 Path 3 `60` 个 active weekly 候选上限。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit90_weekly`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit90_weekly`。
- 五窗口结果：CAGR 为 `14.60% / 12.04% / 14.89% / 80.01% / 123.25%`，最大回撤为 `-26.57% / -28.81% / -26.79% / -16.79% / -9.81%`，换手为 `3.78x / 3.72x / 3.48x / 6.39x / 9.01x`。2026 观察窗强，但 2020/2023 不接近现有 Path 3 winner，且 2026 换手上升，未改变 window winner 或 robust candidate。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> weekly_exit_buffer`。下一轮第一候选建议在同一纯周度线只测试更宽 exit buffer：`aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit94_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap50_hold2_turn12_exit94_weekly`。

## 本轮执行计划（2026-06-03 12:10 CST）

- 上一轮候选/结果摘要：上一轮 `cash_off_and_cap50_hold2_turn12_exit90_weekly` 2026 强但 2020/2023 不够。本轮按 `weekly_exit_buffer` 把 exit 放宽到 `92`、换手上限降到 `10%`、单票放到 `55%`，只作为纯 `_weekly` Path 3 候选。
- 本轮已归档：`PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS` 新增 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_balanced_risk50_cap60_hold2_turn30_weekly`。evict 原因：四窗口最弱 active 之一，`minCAGR=-4.60% / worstMaxDD=-72.55% / meanTurn=11.82x`，继续占用 Path 3 `60` 个 active weekly 候选上限价值低。
- 本轮候选 ID：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold2_turn10_exit92_weekly`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold2_turn10_exit92_weekly`。
- 五窗口结果：CAGR 为 `13.94% / 20.23% / 20.76% / 69.47% / 71.87%`，最大回撤为 `-26.05% / -26.09% / -26.38% / -18.62% / -10.81%`，换手为 `3.55x / 3.39x / 2.98x / 5.87x / 8.27x`。它改善 2020 相对上一轮，但 2023/2025 仍不接近现有 Path 3 winner，未改变 window winner 或 robust candidate。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> risk_downshift`。下一轮第一候选建议测试更低风险暴露/更低换手的同族变体：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap50_hold3_turn08_exit92_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap50_hold3_turn08_exit92_weekly`。

## 本轮执行计划（2026-06-03 10:35 CST）

- 上一轮候选/结果摘要：上一轮 `cap55/turn10/exit92` 改善 2020 但未晋级。本轮继续纯 `_weekly` 口径，把单票放到 `60%`、换手上限回到 `12%`，检查更高弹性是否能在 2017 长窗通过验证。
- 本轮已归档：`PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS` 新增 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold2_turn10_exit92_weekly`。evict 原因：cap55 线虽改善 2020，但 2023/2025 不接近现有 winner，继续占用 Path 3 `60` 个 active weekly 候选上限价值低。
- 本轮候选 ID：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`。增量命令与 Path 1/2 合并执行：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_14_86_hold_2_8_ramp75_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`。
- 五窗口结果：CAGR 为 `16.28% / 17.55% / 17.60% / 59.09% / 59.40%`，最大回撤为 `-24.55% / -29.10% / -26.74% / -20.97% / -10.52%`，换手为 `3.84x / 3.90x / 3.07x / 6.25x / 8.47x`。`update_weighted_winners.py` 后它改写 Path 3 `since_2017_01` window winner，并成为四窗口 robust candidate；但 2020/2023 仍弱于 Path 2 主线，继续作为纯周频独立观察。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction` 且处于 `continue` 状态。下一轮第一候选建议只做降换手确认：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly`。

## 本轮执行计划（2026-06-04 04:18 CST）

- 上一轮候选/结果摘要：上一轮 `cash_off_and_cap60_hold2_turn12_exit92_weekly` 已改写 Path 3 `since_2017_01` window winner 并成为四窗口 robust candidate，但 2020/2023 仍弱于 Path 2 主线。本轮 guard 继续给出 `turnover_reduction`，Path 3 保持纯 `_weekly` 口径，未把月度选股 + 周度仓位 overlay 混入。
- 巡检结果：最终 guard 显示 `ashare_path3_weekly_universe 60/60 complete`，`update_weighted_winners.py` 后 Path 3 当前 winners 为 2017 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`、2020 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`、2023 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_full_risk_cap40_weekly`、2025 `core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`。
- 本轮候选设计但未回测：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly`，目标是用更长持仓和更低 turnover limit 复核上一轮 winner 是否能降换手。本轮未新增 Path 3 回测，原因是预算优先补齐 Path 1 core、Path 4 强主题与 HK 扩展线；因此也未触发新的 active pool evict。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction`。下一轮首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly`；新增前先按四窗口 robust 排名归档一个低换手失败的旧 pullback weekly 候选，避免 active 池超过 `60`。

## 本轮执行计划（2026-06-08 06:05 CST）

- 上一轮候选/结果摘要：上一轮 Path 3 建议继续降换手，但本轮 A股新增预算已分给 Path 2 与 Path 4；Path 3 保持纯 `_weekly` 口径，只巡检与同步 active 集合，没有把月度选股 + 周度仓位 overlay 混入。
- 本轮候选 ID 与命令：没有新增 Path 3 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --family-scope refresh_active --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 同步现有活跃观察集合。该同步确认 `hold3_turn05_exit94_weekly` 仍偏稳但收益不足，`weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly` 仍有高换手与高回撤代价。
- 结论：`update_weighted_winners.py` 后 Path 3 2017/2020/2023/2025 window winners 与 robust candidate 均未改变；候选池维持 `60/60 complete`，本轮未触发新的 evict。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> risk_downshift`。下一轮第一候选建议注册 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly`；新增前先归档一个低换手 pullback 失败线。

## 本轮执行计划（2026-06-08 12:13 CST）

- 上一轮候选/结果摘要：上一轮建议在纯 `_weekly` 口径测试 `cap58/hold4/turn04/exit94/risk25`；本轮实际注册并确认更低 exit 的 `exit92` 版本，继续不把月度选股 + 周度仓位 overlay 混入 Path 3。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit92_risk25_weekly`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit92_risk25_weekly`。
- 五窗口结果：CAGR `15.94% / 15.21% / 12.83% / 35.16% / 158.69%`，最大回撤 `-18.22% / -22.19% / -15.01% / -12.75% / -6.97%`，换手 `1.51x / 1.27x / 1.16x / 0.68x / 5.96x`。它显著压低长窗换手，但 2020/2023 收益不足，2026 强势带有短窗高换手代价。
- 结论：`update_weighted_winners.py` 后 Path 3 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`；本轮候选未改变 window winner、robust candidate 或 tracked payload，未触发新增 evict。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction`。首条命令确认原计划 `exit94` 对照： `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly`；新增前先归档一个低收益高换手旧 weekly。

## 本轮执行计划（2026-06-08 17:37 CST）

- 上一轮候选/结果摘要：上一轮要求确认 `exit94` 对照，但该 ID 已有五窗口历史覆盖；本轮改为测试更长持有、较低换手的 `hold5/turn03/exit94`，保持纯 `_weekly` 口径。
- 本轮 active pool 处理：将旧弱线 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold4_turn04_exit92_risk25_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`，原因是上一轮长窗收益不足，继续占用 active `60` 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly`。
- 五窗口结果：CAGR `5.19% / 10.55% / 12.68% / 38.16% / 63.02%`，最大回撤 `-23.22% / -26.44% / -13.58% / -14.22% / -12.88%`，换手 `1.03x / 0.91x / 0.71x / 0.61x / 3.36x`。低换手特征成立，但收益远低于 Path 3 winners，未改变 window winner、robust candidate 或 tracked payload。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> risk_downshift`。下一轮第一候选建议在本轮低换手结构上继续降风险阈值：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk20_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk20_weekly`。

## 本轮执行计划（2026-06-08 23:27 CST）

- 上一轮候选/结果摘要：上一轮 `hold5/turn03/exit94` 低换手成立但收益不足；本轮继续走纯 `_weekly` Path 3，将持有期延长到 6 周、换手阈值降到 `turn02`。
- 本轮 active pool 处理：归档旧活跃 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn03_exit94_risk25_weekly`，原因是 2017/2020/2023 收益不足且不能改善 robust。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold6_turn02_exit96_risk25_weekly`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold6_turn02_exit96_risk25_weekly`。
- 五窗口结果：CAGR `6.31% / 1.63% / 15.78% / 29.38% / 75.05%`，最大回撤 `-28.21% / -30.13% / -8.85% / -15.47% / -12.79%`，换手 `0.68x / 0.52x / 0.29x / 0.52x / 3.07x`。
- 结论：换手显著下降，但 2017/2020/2025 太弱，validation 拒绝；Path 3 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> weekly_exit_buffer`。下一轮第一候选建议回到 `hold5`，只微调 exit buffer：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly`。

## 本轮执行计划（2026-06-09 04:20 CST）

- 上一轮候选/结果摘要：上一轮 `hold6/turn02/exit96` 换手极低但收益失败；本轮回到 `hold5`，把 exit buffer 收到 `95`、turnover 放到 `04`，继续保持纯 `_weekly` Path 3 口径。
- 本轮 active pool 处理：将旧活跃 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold6_turn02_exit96_risk25_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：2017/2020/2025 收益不足，validation 拒绝，继续占用 active weekly 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly`；实际命令与 Path 2 合并为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v27_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly`。
- 五窗口结果：CAGR `12.96% / 15.80% / 11.94% / 15.11% / 119.82%`，最大回撤 `-20.32% / -25.75% / -14.69% / -18.03% / -7.08%`，换手 `1.50x / 1.37x / 1.18x / 2.13x / 5.76x`。
- 结论：该线的 2026 弹性强，但 2020/2023 收益不足，`update_weighted_winners.py` validation 拒绝；Path 3 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> risk_downshift`。下一轮第一候选建议在本轮结构上降低风险阈值而非继续拉长持有：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk20_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk20_weekly`；新增前继续按 robust 排名归档一个低收益旧 weekly。

## 本轮执行计划（2026-06-09 20:05 CST）

- 上一轮候选/结果摘要：上一轮 `risk25_weekly` 的 2026 弹性强但 2020/2023 不足，本轮按 `risk_downshift` 把风险阈值降到 `risk20`，继续保持纯 `_weekly` Path 3 口径。
- 本轮 active pool 处理：将旧活跃 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：旧 risk25 线 2020/2023 收益不足且 validation 拒绝，继续占用 active weekly 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk20_weekly`；实际 A股合并命令使用五窗口 `--only-base-ids` 覆盖。
- 五窗口结果：CAGR `15.02% / 18.88% / 12.88% / 15.11% / 119.82%`，最大回撤 `-18.56% / -25.87% / -12.88% / -18.03% / -7.08%`，换手 `1.37x / 1.17x / 0.91x / 2.13x / 5.76x`。
- 结论：risk20 成为 Path 3 `since_2017_01` window winner，tracked payload 随 `update_weighted_winners.py` 更新；但 2020/2023 validation 仍未通过，robust candidate 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction` 且本路径 `changed=true / stagnation_runs=0`。下一轮第一候选建议在 risk20 基础上继续压 2026 换手：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold6_turn03_exit96_risk20_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold6_turn03_exit96_risk20_weekly`；新增前继续按 robust 排名归档一个低收益旧 weekly。

## 本轮执行计划（2026-06-09 22:26 CST）

- 上一轮候选/结果摘要：上一轮 `cap58/hold5/turn04/exit95/risk20` 改写 2017 窗口但 2020/2023 不足；本轮按 `turnover_reduction` 把单票降到 `56%`、持有期延到 6 周、换手阈值降到 `3%`，继续保持纯 `_weekly` 口径。
- 本轮 active pool 处理：将旧活跃 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk20_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：旧线虽然一度改写 2017，但 2020/2023 收益不足且不改善 robust，继续占用 `60` 个 weekly active 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold6_turn03_exit96_risk20_weekly`；实际 A股合并命令使用五窗口 `--only-base-ids` 覆盖。
- 五窗口结果：CAGR `6.98% / 9.33% / 12.99% / 33.96% / 98.31%`，最大回撤 `-18.11% / -27.27% / -9.30% / -14.50% / -12.93%`，换手 `0.97x / 0.71x / 0.69x / 0.61x / 3.36x`。
- 结论：新线换手明显降低但收益不足，`update_weighted_winners.py` validation 拒绝；Path 3 window winner、robust candidate 与 tracked payload 未改变。最终 guard 显示 `ashare_path3_weekly_universe 60/60 complete`。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction`。下一轮不应继续只拉长持有，建议做同一低换手结构的收益修复：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn04_exit94_risk20_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn04_exit94_risk20_weekly`。

## 本轮执行计划（2026-06-10 04:41 CST）

- 上一轮候选/结果摘要：上一轮 `hold6/turn03/exit96` 换手低但收益不足；本轮按收益修复思路回到 `hold5/turn04/exit94`，仍保持纯 `_weekly` 口径，不混入 Path 1 周度仓位 overlay。
- 本轮 active pool 处理：将旧低收益 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold6_turn03_exit96_risk20_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：换手低但五窗口收益不改善 robust，继续占用 `60` 个 weekly active 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn04_exit94_risk20_weekly`；实际 A股合并命令使用五窗口 `--only-base-ids` 覆盖。
- 五窗口结果：CAGR `10.84% / 17.26% / 14.41% / 20.89% / 100.45%`，最大回撤 `-20.55% / -26.20% / -12.44% / -18.30% / -13.00%`，换手 `1.35x / 1.07x / 0.86x / 2.12x / 1.83x`。
- 结论：新线相对上一轮收益修复有效、换手仍低，但 2020 回撤和 2025 收益不足，未改变 Path 3 window winner、robust candidate 或 tracked payload。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> weekly_exit_buffer`。下一轮第一候选建议只放宽出场并观察 2023/2026：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly`；新增前继续归档一个低收益旧 weekly。

## 本轮执行计划（2026-06-10 10:40 CST）

- 上一轮候选/结果摘要：上一轮 `cap56/hold5/turn04/exit94/risk20_weekly` 收益修复但未晋级；本轮按 weekly exit buffer 放宽到 `turn05/exit96`，仍保持纯 `_weekly` 口径，不混入 Path 1 周度仓位 overlay。
- 本轮 active pool 处理：将旧低收益 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn04_exit94_risk20_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：2020/2023 与 robust 仍不足，继续占用 `60` 个 weekly active 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly`；实际命令与 Path 1/2 合并五窗口执行。
- 五窗口结果：CAGR `11.95% / 22.13% / 17.61% / 71.29% / 96.63%`，最大回撤 `-28.09% / -23.89% / -14.50% / -14.92% / -12.88%`，换手 `2.09x / 1.63x / 1.65x / 2.93x / 2.09x`。收益比上一轮修复明显，但 `update_weighted_winners.py` validation 仍拒绝；Path 3 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> cost_stress`。下一轮第一候选建议在当前收益修复结构上继续降 cap/risk：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk18_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk18_weekly`；新增前继续按 robust 排名归档一个低收益旧 weekly。

## 本轮执行计划（2026-06-10 16:31 CST）

- 上一轮候选/结果摘要：上一轮 `cap56/hold5/turn05/exit96/risk20_weekly` 收益修复但未晋级；本轮按 `cost_stress` 继续降 cap/risk 到 `cap54/risk18`，保持纯 `_weekly` Path 3 口径。
- 本轮 active pool 处理：将旧活跃 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap56_hold5_turn05_exit96_risk20_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：上一轮收益修复但未改善 robust，继续占用 `60` 个 weekly active 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk18_weekly`；路径首命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk18_weekly`。
- 五窗口结果：CAGR `12.11% / 22.12% / 18.77% / 71.29% / 96.63%`，最大回撤 `-28.24% / -24.44% / -14.54% / -14.92% / -12.88%`，换手 `2.08x / 1.55x / 1.40x / 2.93x / 2.09x`。
- 结论：`update_weighted_winners.py` 后该候选成为 Path 3 `since_2020_01` 与 `since_2023_01` window winner；但 validation 仍提示它对 2020 track 的交叉验证不足，robust candidate 未切换。最终 guard 显示 `ashare_path3 changed=true / stagnation_runs=0`。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction`。下一轮第一候选建议在本轮 winner 基础上拉长持有并继续压换手：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit96_risk18_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit96_risk18_weekly`；新增前继续归档一个低收益旧 weekly。

## 本轮执行计划（2026-06-11 05:45 CST）

- 上一轮候选/结果摘要：上一轮 `cap54/hold5/turn05/exit96/risk18_weekly` 一度改善 Path 3 的 2020/2023 window，但 robust 未切换；本轮按 `turnover_reduction` 拉长持有到 6 周、把 cap 压到 `52%`，继续保持纯 `_weekly` 口径。
- 本轮 active pool 处理：将旧活跃 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk18_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：旧线已完成收益修复验证但未改善 robust，继续占用 `60` 个 weekly active 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit96_risk18_weekly`；实际命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v33_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit96_risk18_weekly`。
- 五窗口结果：CAGR `14.29% / 18.05% / 13.47% / 24.22% / 55.83%`，最大回撤 `-20.91% / -26.53% / -12.22% / -18.39% / -13.22%`，换手 `1.35x / 1.09x / 0.82x / 2.12x / 3.48x`。
- 结论：该线确实降换手，但 2020 回撤与 2023 收益不够，未改变 Path 3 window winner、robust candidate 或 tracked payload。最终 guard 显示 Path 3 覆盖 `60/60 complete`，但因未继续切换 winner，rotation 进入 `weekly_exit_buffer / rotate`。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> weekly_exit_buffer`。下一轮第一候选建议在本轮低换手结构上只放宽出场缓冲：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold5_turn05_exit98_risk18_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold5_turn05_exit98_risk18_weekly`；新增前继续归档一个低收益旧 weekly。

## 本轮执行计划（2026-06-11 16:10 CST）

- 上一轮候选/结果摘要：上一轮留下 `cap52/hold5/turn05/exit98/risk18_weekly`，目标是在低换手结构上放宽 exit buffer；本轮继续保持纯 `_weekly` 口径，没有把 Path 1 月度选股 + 周度仓位 overlay 混入 Path 3。
- 本轮 active pool 处理：将旧活跃 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit96_risk18_weekly` 加入 `PATH3_ARCHIVED_WEEKLY_STRATEGY_IDS`。evict 原因：上一轮低换手结构收益不足且未改善 robust，继续占用 `60` 个 weekly active 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold5_turn05_exit98_risk18_weekly`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v34_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold5_turn05_exit98_risk18_weekly`。
- 五窗口结果：CAGR `11.35% / 21.14% / 17.22% / 67.23% / 89.07%`，最大回撤 `-28.24% / -24.60% / -14.52% / -14.92% / -12.88%`，换手 `2.08x / 1.56x / 1.41x / 2.93x / 2.09x`。
- 结论：新线修复 2020/2025/2026 收益，但 2017 回撤与 2023 持续性仍不足；`update_weighted_winners.py` validation 拒绝，Path 3 window winner、robust candidate 与 tracked payload 未改变。最终 guard 显示 `ashare_path3_weekly_universe 60/60 complete`，rotation 转为 `risk_downshift / rotate`。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> risk_downshift`。下一轮第一候选建议在本轮收益修复结构上降低风险阈值和单票上限：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit98_risk16_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit98_risk16_weekly`；新增前继续归档一个低收益旧 weekly。

## 本轮执行计划（2026-06-25 21:16 CST）

- 上一轮候选/结果摘要：本轮继续保持 Path 3 纯 `_weekly` 口径，新增一条 `cap54/hold5/turn05/exit98/risk16_weekly`，不把 Path 1 月频选股 + weekly exposure overlay 混作 Path 3。
- 本轮 active pool 处理：归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit96_risk16_weekly`。evict 原因：旧 `exit96/risk16` 未改善 robust，占用 60 条 weekly active 池；新线只调整 exit buffer，便于直接比较。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v46_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap54_hold5_turn05_exit98_risk16_weekly,<three_path4_prom22_ids>`。
- 五窗口结果：CAGR `12.86% / 24.69% / 21.69% / 85.57% / 117.55%`，最大回撤 `-28.03% / -25.33% / -14.52% / -14.92% / -12.88%`，换手 `2.04x / 1.49x / 1.30x / 2.89x / 1.98x`。
- 结论：新 weekly 线明显改善 2020/2025/2026，但 2017/2020 回撤仍大，`update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未改变。最终 guard 显示 Path 3 `continue / turnover_reduction`。
- 下一轮 focus：下一轮第一候选应在本线基础上继续降换手和单票上限，而不是追短窗 CAGR：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`，新增前继续归档一条弱 weekly。

## 本轮执行计划（2026-06-26 09:46 CST）

- 上一轮候选/结果摘要：上一轮要求在 `cap54/hold5/turn05/exit98/risk16_weekly` 基础上继续降换手和单票上限；本轮新增纯 `_weekly` 的 `cap52/hold6/turn04/exit98/risk16`，没有把 Path 1 月频选股 + 周度仓位 overlay 混入 Path 3。
- 本轮 active pool 处理：归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold5_turn05_exit98_risk16_weekly`。evict 原因：旧线未改善 robust，继续占用 Path 3 active weekly 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v59_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap52_hold6_turn04_exit98_risk16_weekly`。
- 五窗口结果：CAGR `11.40% / 16.02% / 19.71% / 33.91% / 82.29%`，最大回撤 `-20.22% / -26.51% / -10.68% / -18.39% / -13.22%`，换手 `1.29x / 1.06x / 0.71x / 2.08x / 3.26x`。
- 结论：新线改善 2023 结构且换手相对温和，但 2020/2025 回撤仍不够，`update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> weekly_exit_buffer`。下一轮第一候选建议继续压单票并拉长持有，同时观察 exit buffer：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold7_turn03_exit98_risk14_weekly`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold7_turn03_exit98_risk14_weekly`。

## 本轮执行计划（2026-06-26 20:46 CST）

- 上一轮候选/结果摘要：上一轮留下 `cap50/hold7/turn03/exit98/risk14_weekly`，本轮保持 Path 3 纯 `_weekly` 口径执行，不把 Path 1 月频选股 + 周度仓位 overlay 混入 Path 3。
- 本轮 active pool 处理：本轮未新增归档；当前 weekly active count 已高于默认 cap，下一轮新增前应按 robust 排名归档一条低收益旧 weekly。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold7_turn03_exit98_risk14_weekly`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v60_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold7_turn03_exit98_risk14_weekly`。
- 五窗口结果：CAGR `5.41% / 10.04% / 10.08% / 41.30% / 173.21%`，最大回撤 `-22.69% / -27.54% / -7.39% / -14.78% / -12.89%`，换手 `0.84x / 0.66x / 0.48x / 0.60x / 3.12x`。
- 结论：新线 2026 弹性极强且长窗换手低，但 2017/2020 收益和回撤不足，未改变 Path 3 window winner、robust candidate 或 tracked payload。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction`。下一轮第一候选建议在本线基础上继续压换手和单票上限：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold8_turn02_exit98_risk14_weekly`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold8_turn02_exit98_risk14_weekly`，新增前先归档一条弱 weekly。

## 本轮执行计划（2026-06-27 07:44 CST）

- 上一轮候选/结果摘要：上一轮留下 `cap48/hold8/turn02/exit98/risk14_weekly`，本轮保持 Path 3 纯 `_weekly` 口径执行，不把月频选股 + 周度仓位 overlay 混作 Path 3。
- 本轮 active pool 处理：归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold7_turn03_exit98_risk14_weekly`。evict 原因：上一轮长中窗收益不足且未改善 robust，继续占用 weekly active 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold8_turn02_exit98_risk14_weekly`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v61_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold8_turn02_exit98_risk14_weekly`。
- 五窗口结果：CAGR `3.52% / 5.81% / 0.40% / 35.19% / 108.52%`，最大回撤 `-15.53% / -28.01% / -5.02% / -15.25% / -12.74%`，Sharpe `0.5439 / 0.4948 / 0.1271 / 1.2100 / 2.1406`。
- 结论：新线压换手后长中窗收益明显塌陷，只有 2026 弹性保留；`update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> risk_downshift`。下一轮第一候选建议不要继续单纯压换手，先下调风险阈值并保持 exit98 对照：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold7_turn03_exit98_risk12_weekly`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold7_turn03_exit98_risk12_weekly`，新增前继续归档一条弱 weekly。

## 本轮执行计划（2026-07-02 07:00 CST）

- 上一轮候选/结果摘要：上一轮要求在新增前归档弱 weekly；本轮没有注册新 Path 3 `_weekly` id，原因是最终 guard 显示 weekly universe 已为 `65/65 pass`，高于默认 active cap `60`，新增前必须先做池压缩。
- 本轮候选 ID 与命令：本轮无新增 Path 3 回测；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-01 --family-scope refresh_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 同步当前活跃观察集合，并通过 `scripts/update_weighted_winners.py` 复核 official/tracked。
- 巡检结果：低换手 raw leader `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap50_hold6_turn04_exit98_risk16_weekly` 五窗口 CAGR `14.20% / 15.34% / 18.10% / 33.88% / 78.95%`，最大回撤 `-21.11% / -27.11% / -10.65% / -18.37% / -13.22%`，换手 `1.48x / 1.07x / 0.71x / 2.07x / 3.16x`；但 validation 对 `since_2017_01` 仍未通过，因为 `since_2020_01` 低于现有 2020 winner 要求。
- 结论：`update_weighted_winners.py` 后 Path 3 official candidate 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`，mean CAGR `35.59%`、min CAGR `13.94%`；window winners 未由本轮新增改变。Path 3 无新增 evict，但已明确下一轮必须先归档 5 条长窗弱或高换手旧 weekly。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> turnover_reduction`。下一轮第一步不是直接新增，而是先按 robust 排名归档 5 条旧 weekly，把 active count 压回 `60`；随后注册低换手收益修复候选 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_weekly_turnover_repair`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit98_risk14_weekly_turnover_repair`。

## 本轮执行计划（2026-07-03 07:23 CST）

- 上一轮候选/结果摘要：上一轮要求先归档 5 条弱 weekly 再新增；本轮没有改代码归档池，但确认了一个已注册、纯 `_weekly` 低换手收益修复候选，仍不把 Path 1 的月频选股 + weekly exposure overlay 混入 Path 3。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <six_ashare_ids>`。
- 五窗口结果：CAGR `4.57% / 8.44% / 5.75% / 35.55% / 120.90%`，最大回撤 `-21.00% / -28.50% / -6.87% / -14.76% / -12.89%`，Sharpe `0.5018 / 0.6178 / 0.6914 / 1.2621 / 2.0197`，换手 `0.73x / 0.58x / 0.35x / 0.59x / 2.99x`。低换手成立，但 2017/2020/2023 收益不足，2026 弹性带有短窗性质。
- 结论：`update_weighted_winners.py` validation 仍拒绝它对 2017/2020/2023 的稳健性；Path 3 official/robust 没有干净晋级，tracked payload 只是同步重写。本轮没有完成旧 weekly evict，这是下一轮新增前的硬前置。
- 下一轮 focus：第一步先按 robust/窗口覆盖归档 5 条长窗弱或高换手旧 weekly，把 active count 压回默认 `60`；随后再确认 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold8_turn03_exit96_risk10_weekly_turnover_repair_weekly`。

## 本轮执行计划（2026-07-07 05:01 CST）

- 上一轮候选/结果摘要：上一轮要求先压缩 weekly 池；本轮归档一条旧 `weekly_yield_repair`，新增纯 `_weekly` 的 v2，继续不把 Path 1 月频选股 + weekly exposure overlay 混入 Path 3。
- 本轮 active pool 处理：归档 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold6_turn05_exit92_risk14_weekly_yield_repair_weekly`。evict 原因：旧收益修复线回撤高且未改善 robust，继续占用 60 条 weekly active 池价值低。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap44_hold7_turn04_exit94_risk12_weekly_yield_repair_v2_weekly`；成功命令与 Path2 v73 合并为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v73_ids>,<one_path3_v2_id>`。
- 五窗口结果：CAGR `10.43% / 12.91% / 8.79% / 29.20% / 64.96%`，最大回撤 `-20.92% / -27.73% / -11.76% / -18.20% / -13.22%`，Sharpe `0.7151 / 0.7310 / 0.6407 / 0.9493 / 1.4455`，换手 `1.28x / 1.01x / 0.59x / 2.10x / 3.20x`。低换手成立，但 2020 回撤太深，2023 收益不足。
- 结论：`update_weighted_winners.py` 后 Path 3 window winner、robust candidate 与 tracked payload 未改变；v2 是风险下移样本，不是晋级候选。
- 下一轮 focus：最终 guard 给出 `ashare_path3 -> risk_downshift`。下一轮新增前继续归档一条长窗弱 weekly，并注册/确认 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn03_exit96_risk10_weekly_yield_repair_v3_weekly`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn03_exit96_risk10_weekly_yield_repair_v3_weekly`。
- Final guard 修正：最终 guard 轮换为 `ashare_path3 -> cost_stress / rotate / stagnation_runs=9`。下一轮首条命令改为已注册成本压力线 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap42_hold7_turn02_exit98_risk10_weekly`；新增前仍先归档一条长窗弱 weekly。
