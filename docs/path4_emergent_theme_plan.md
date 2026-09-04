# Path 4 强主题涌现路径

## 2026-09-05 迭代：capacity-v2 降回撤换手，但年内仍负（端点 2026-09-04）

### 上一轮候选与结果摘要

- 上轮 risk08 成为 2017 window winner但仍为 `keep_watch`；risk06 因2026负收益仅 `robust_observation`，本轮加入 capacity-v2 检验容量与风险前沿。

### 本轮候选 ID 与命令

- 五窗实跑 risk08、risk06、capacity-v2；命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- risk08 相对 risk06 的 2017 CAGR/Sharpe提高 `1.75pp/0.180`，但2026 CAGR `-6.23%`，维持 `keep_watch`；risk06 2026 CAGR `-6.01%`，维持 `robust_observation`。
- capacity-v2 的2020/2023 MaxDD改善约 `3.91/3.80pp`、换手降低约 `0.48/0.44x`且CAGR基本持平，继续占据2020 window winner与路径 robust 观察位；但2026 CAGR仍为 `-3.79%`，判 `robust_observation`：进入观察位，不是强稳定 winner。official ID未变，无人工主题/ETF、无 evict/archive。

### 下一轮 focus 提示

- `emergent_theme_coverage` 转验 risk-control-v5 与 signal30 是否能保持中窗并修复2026。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：risk-control-v5、signal30-risk06；`theme_signal_quality`：signal30-risk06、signal28-risk08；`theme_risk_control`：risk-control-v5、capacity-v2；`theme_capacity_cost`：capacity-v2、risk08-lowturn。

## 2026-09-04 迭代：risk08 赢长窗但未修复年内负收益（端点 2026-09-03）

### 上一轮候选与结果摘要

- 上轮 signal28-risk08 长窗略优但 2026 为负，只 `keep_watch`；signal29-risk06 仍为弱路径 `robust_observation`。

### 本轮候选 ID 与命令

- 五窗再跑 risk08/risk06；命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- risk08 相对 risk06 的 2017 CAGR高 `1.74pp`、MaxDD改善 `2.45pp`，成为 2017 window winner，但 2023 CAGR低 `0.54pp`且 2026仍为 `-6.03%`，仅 `keep_watch`。risk06 的 2026 CAGR `-5.81%`，维持 `robust_observation`：进入观察位，不是强稳定 winner。无人工主题/ETF/单票幸运，无 evict/archive。

### 下一轮 focus 提示

- 最终 guard focus 转向 `emergent_theme_coverage`，先复核 risk08/risk06 与新 artifact 观察位 capacity-v2 的五窗完整性，再比较更小单票上限的 risk-control-v5；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`。

### Focus 候选池

- `theme_risk_control`：risk-control-v5、signal28-risk08；`theme_signal_quality`：signal-quality-v3、signal-quality-v4；`theme_capacity_cost`：capacity-v2、cap06-lowturn；`emergent_theme_coverage`：signal28-risk08、signal29-risk06。

## 2026-09-03 迭代：risk08 改善长窗但年内仍为负（端点 2026-09-02）

### 上一轮候选与结果摘要

- 上轮 capacity-v2/cap06 均未修复中窗或年内收益而 `reject`；signal29-risk06 保持弱观察位。

### 本轮候选 ID 与命令

- 五窗实跑 `...signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn` 与 `...signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`；命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- signal28 相对 signal29 的 2017 CAGR 高 `1.74pp`、2020高 `0.19pp`，但 2023 低 `0.54pp`、2026仍为 `-5.79%`，判 `keep_watch`；signal29 的2026 CAGR `-5.57%`，仅 `robust_observation`：进入观察位，不是强稳定 winner。候选无人工主题/ETF，当前持仓分散且非单票幸运；正式 winner/robust/tracked 未变，无 evict/archive。

### 下一轮 focus 提示

- `theme_signal_quality` 转验 signal-quality-v3/v4；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_risk_control`：signal28-risk08、signal29-risk06；`theme_signal_quality`：signal-quality-v3、signal-quality-v4；`theme_capacity_cost`：capacity-v2、cap06-lowturn；`emergent_theme_coverage`：signal28-risk08、signal29-risk06。


## 2026-09-02 迭代：容量与 cap06 形态仍未修复中窗回撤/负收益（端点 2026-09-01）

### 上一轮候选与结果摘要

- 上轮 90/10 signal30/risk04 微调与参考近乎无差异且 2026 为负，均 `reject`；signal29-risk06 保持弱观察位。

### 本轮候选 ID 与命令

- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- capacity-v2 的2020/2023 MaxDD恶化 `8.26/10.81pp`且2026 CAGR `-13.14%`，`reject`；cap06 在2023/2026 CAGR为 `-0.65/-7.30%`且换手更高，`reject`。signal29-risk06 仍为 `robust_observation`：进入观察位，不是强稳定 winner。无人工主题/ETF/单票幸运、无 evict/archive，正式 winner/robust/tracked 未变。

### 下一轮 focus 提示

- `theme_risk_control` 转验已注册的 signal28-risk08 与 signal29-risk06 正交边界；第一条可执行命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-09-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_risk_control`：signal28-risk08、signal29-risk06；`theme_signal_quality`：signal28-v3、signal29-reference；`theme_capacity_cost`：capacity-v2、cap06-lowturn；`emergent_theme_coverage`：signal28-risk08、signal29-risk06。

## 2026-09-01 迭代：90/10 信号与风险微调未形成差异（端点 2026-08-31）

### 上一轮候选与结果摘要

- `signal30-risk06` 与 signal29-risk06 五窗指标完全相同；`signal29-risk04` 的2020/2023 CAGR只低 `0.005/0.003pp`，其余近乎相同。两条均未改善绝对弱收益，2026 CAGR仍 `-5.84%`，按无有效差异 `reject`；参考继续 `robust_observation`，进入观察位，不是强稳定 winner。无人工主题、ETF、单票幸运及 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality` 转向容量/信号正交形态；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_signal_quality`：capacity-v2、signal29-cap06；`theme_risk_control`：risk04-capacity、risk06-reference；`theme_capacity_cost`：capacity-v2、cap06-lowturn；`emergent_theme_coverage`：signal28-risk08、signal29-risk06。

## 2026-08-31 迭代：80/20 中窗收益改善仍以回撤与负短窗为代价（端点 2026-08-28）

### 上一轮候选与结果摘要

- `risk_control_v5` 与 `signal_quality_v4` 相对90/10 signal29-risk06 的 2020 CAGR分别提高 `2.18/2.56pp`，但 2020 MaxDD恶化 `7.89/7.46pp`、2023均恶化 `10.53pp`，且2026 CAGR均为 `-12.65%`，触发回撤护栏并 `reject`。
- artifact 将 `risk_control_v5` 推为 2023/2025 window winner，但 scorecard 明确否定正式晋级；signal29-risk06 仍因 2026 CAGR `-6.05%`、绝对收益弱判 `robust_observation`，进入观察位，不是强稳定 winner。假设“80/20可同时改善中窗收益、回撤与年内收益”不获支持；无人工主题、ETF、单票幸运或 evict/archive。

### 本轮候选 ID 与命令

- 实跑 IDs：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality`：停止 80/20 同形，转回90/10信号与风险正交边界，要求2026先转正且中窗不弱于 robust。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_signal_quality`：signal30-risk06、signal29-risk04；`theme_risk_control`：risk04-exit70、risk06-exit68；`theme_capacity_cost`：capacity-v2、cap06-lowturn；`emergent_theme_coverage`：signal28-risk08、signal29-risk06。

## 2026-08-30 迭代：90/10 signal-quality 邻域保持负短窗（端点 2026-08-28）

### 上一轮候选与结果摘要

- `signal30-leader78-risk08-exit66` 相对 signal29-risk06 的 2020 CAGR `+0.36pp`、2023 `-1.66pp`，但 2026 CAGR仍为 `-6.05%`；`signal28-leader76-risk08-exit68` 的 2020/2023差分 `+0.19/-0.54pp`，2026为 `-6.28%`。两条未触发中窗硬护栏，但绝对短窗仍负，均 `keep_watch`。
- signal29-risk06 仍为 Path4 robust 观察位，2020/2023 CAGR仅 `2.43%/1.25%`、2026 `-6.05%`，判 `robust_observation`：进入观察位，不是强稳定 winner。artifact 的 2017 window winner 切到 signal28-risk08，未改 official tracked；假设“risk08 信号微调可修复年内收益”不获支持，无人工主题、ETF 或单票幸运晋级，无 evict/archive。

### 本轮候选 ID 与命令

- 实跑 ID：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality`：停止 90/10 signal28-30 局部微调，回到 80/20 `risk_control_v5` / `signal_quality_v4` 与 90/10 robust 做五窗竞争，重点验证中窗回撤与 2026 负收益能否同时修复。第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_signal_quality`：`...emergent_theme_signal_quality_v4`、`...signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。
- `theme_risk_control`：`...emergent_theme_risk_control_v5`、`...signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- `theme_capacity_cost`：`...emergent_theme_capacity_v2`、`...signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`。

## 2026-08-29 迭代：signal-quality/capacity 的收益回撤冲突（端点 2026-08-28）

### 上一轮候选与结果摘要

- `signal_quality_v4` 相对90/10 robust 的2020 CAGR提高 `2.56pp`，但2020/2023 MaxDD恶化 `7.46/10.53pp`、2026 CAGR `-12.65%`；`capacity_v2` 的2020 CAGR提高 `2.14pp`，但2020/2023 MaxDD恶化 `8.12/10.75pp`、2026 `-13.56%`。两条均命中回撤护栏并 `reject`。
- weighted active top5 将 `signal_quality_v4` 纳入观察排序，但正式 window winner/robust 未变；90/10 `signal29-risk06` 的2026 CAGR仍为 `-6.05%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。假设“80/20 signal/capacity 可在中窗增益下守住回撤并修复年内收益”不获支持；无人工主题、无ETF、无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality` 停止80/20同形，回到90/10 signal28/30 边界，要求2026转正且中窗收益不低于 robust；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal28-risk08、signal29-risk06；`theme_signal_quality`：signal30-risk08、signal28-risk08；`theme_risk_control`：risk04-lowturn、risk06-cap04；`theme_capacity_cost`：capacity-v2、cap06-lowturn。

## 2026-08-28 迭代：80/20 signal-quality 与 risk-control 回撤否定（端点 2026-08-27）

### 上一轮候选与结果摘要

- `signal_quality_v3` 相对90/10 robust 的2020/2023 MaxDD恶化 `8.06/11.28pp`，2026 CAGR `-20.18%`；`risk_control_v5` 的2020/2023 MaxDD恶化 `7.50/10.44pp`，2026 CAGR `-12.13%`。两条均触发回撤护栏并 `reject`。
- 90/10 `signal29-risk06` 仍为 `robust_observation`，2026 CAGR `-6.20%`：进入观察位，不是强稳定 winner。假设“80/20可在改善中窗收益时守住回撤并修复年内收益”不获支持；正式 winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality` 停止 v3/v5 同形，转验 signal-quality-v4 与 capacity-v2，要求2020/2023 MaxDD不再恶化5pp且2026先转正；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal-quality-v4、capacity-v2；`theme_signal_quality`：signal-quality-v4、signal30-risk08；`theme_risk_control`：risk04-lowturn、risk06-cap04；`theme_capacity_cost`：capacity-v2、cap06-lowturn。

## 2026-08-27 迭代：signal/risk 正交边界未修复年内收益（端点 2026-08-26）

### 上一轮候选与结果摘要

- `signal30-risk06` 与 robust `signal29-risk06` 五窗口指标实质相同；`signal29-risk04` 也只产生近零差分。两条候选均未触发中窗护栏，但 2026 CAGR仍为 `-6.38%`，均 `keep_watch`，不具备晋级条件。
- artifact robust `signal29-risk06` 仍为 `robust_observation`：minCAGR/2026 为负，进入观察位，不是强稳定 winner。假设“提高信号或下调风险能让2026转正”不获支持；正式 window winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 停止90/10近等价同形，改验80/20的 signal-quality/risk-control 正交形态，要求先让2026转正且中窗MaxDD不恶化5pp；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal-quality-v3、risk-control-v5；`theme_signal_quality`：signal-quality-v3、signal-quality-v4；`theme_risk_control`：risk-control-v5、risk04-lowturn；`theme_capacity_cost`：capacity-v2、cap06-lowturn。

## 2026-08-26 迭代：90/10 信号覆盖边界与年内失效确认（端点 2026-08-25）

### 上一轮候选与结果摘要

- `signal30-risk08` 相对 `signal29-risk06` 的 2020 CAGR提高 `0.36pp`，2023下降 `1.67pp`，回撤与换手近似，但 2026 CAGR仍为 `-6.40%`；`signal28-risk08` 的2020 CAGR提高 `0.19pp`、2023下降 `0.54pp`、2025提高 `0.27pp`，2026仍为 `-6.63%`。两者未触发中窗硬护栏，但都未实现年内转正，判 `keep_watch`。
- artifact 保持 `signal28-risk08` 为 since_2017_01 window winner，本轮未发生 winner/robust/tracked ID 变化；该窗口排序不改变 scorecard 的 `keep_watch`。`signal29-risk06` 因 2026 负收益继续 `robust_observation`：进入观察位，不是强稳定 winner。假设“90/10 信号覆盖边界可修复年内收益”不获支持；无人工主题标签、无 ETF、无 evict/archive。完整卡见 `results/research/a_share/research_iteration_scorecard_20260826.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 停止继续提高 risk08，转验 signal30-risk06 与 signal29-risk04 的信号/风险正交边界，要求2026转正且2020/2023 MaxDD不恶化5pp；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal30-risk06、signal29-risk04；`theme_signal_quality`：signal30-risk06、signal28-risk08；`theme_risk_control`：risk04-exit70、risk06-cap05；`theme_capacity_cost`：capacity-v2、risk06-cap06。

## 2026-08-25 迭代：signal-quality/risk-control 的回撤护栏否定（端点 2026-08-24）

### 上一轮候选与结果摘要

- `signal_quality_v3` 相对 `signal29-risk06-cap05` 的2020/2023 MaxDD恶化 `8.64/11.52pp`，2026 CAGR为 `-22.04%`；`risk_control_v5` 的2020/2023 MaxDD恶化 `8.33/10.68pp`，2026 CAGR为 `-14.14%`，均触发护栏并 `reject`。假设“80/20 signal/risk 正交形态可改善短窗且不扩大中窗回撤”不获支持。
- artifact 仍将 `risk_control_v5` 推为2023/2025 window winner，但二次 scorecard 明确否决晋级；`signal29-risk06-cap05` 因2026负收益维持 `robust_observation`，进入观察位，不是强稳定 winner。正式 robust 未变，无人工主题标签、无 ETF、无 evict/archive；完整卡见 `results/research/a_share/research_iteration_scorecard_20260825.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 回到90/10风险/信号边界，要求2026先转正且2020/2023 MaxDD不恶化5pp；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal30-risk08、signal28-risk08；`theme_signal_quality`：signal30-risk08、signal29-risk06；`theme_risk_control`：risk04-exit70、risk06-cap05；`theme_capacity_cost`：capacity-v2、risk06-cap06。

## 2026-08-24 迭代：risk04 与 capacity 风险收益边界复核（端点 2026-08-21）

### 上一轮候选与结果摘要

- `signal29-risk04-cap05` 与 robust `risk06-cap05` 五窗几乎等价，2026 CAGR仍为 `-5.42%`，判 `keep_watch`；假设“risk04 可令短窗转正”不获支持。
- `capacity_v2` 的 2020 CAGR提高 `2.18pp`、2025提高 `8.34pp`，但 2020/2023 MaxDD分别恶化 `8.02/10.71pp`，2026 CAGR `-12.66%`，仅 `robust_observation`；`risk06-cap05` 同样因 2026负收益继续 `robust_observation`。两者均为进入观察位，不是强稳定 winner；正式 window winner/robust/tracked 主体未变，无人工主题标签、无 ETF、无 evict/archive。完整卡见 `results/research/a_share/research_iteration_scorecard_20260824.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 转向 signal-quality/risk-control 正交变体，要求先改善2026且不扩大中窗回撤；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal-quality-v3、risk-control-v5；`theme_signal_quality`：signal-quality-v3、signal30-risk06；`theme_risk_control`：risk-control-v5、risk04-exit70；`theme_capacity_cost`：capacity-v2、risk06-cap06。

## 2026-08-23 迭代：signal29/30 容量边界确认（端点 2026-08-21）

### 上一轮候选与结果摘要

- `signal29-risk06-cap06` 相对 robust `signal29-risk06-cap05` 的 2020 CAGR提高 `0.81pp`，但 2023下降 `1.91pp`、2026仍为负，判 `keep_watch`；`signal30-risk06-cap05` 指标与锚近乎等价且 2026仍负，也为 `keep_watch`。
- `signal29-risk06-cap05` 继续 `robust_observation`：进入观察位，不是强稳定 winner；正式 2017/2020/2023/2025 window winner 与 tracked 未改变。无人工主题标签、无 ETF、无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 继续要求 2026 转正，下一轮比较 risk04/capacity-v2 与 risk06 锚，不再扩 signal29/30 同形；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal29-risk06、signal28-risk08；`theme_signal_quality`：signal30-risk06、signal29-risk06；`theme_risk_control`：risk04-exit70、risk06-exit68；`theme_capacity_cost`：risk06-cap06、capacity-v2。

## 2026-08-22 迭代：risk04 覆盖边界与弱观察位复核（端点 2026-08-21）

### 上一轮候选与结果摘要

- `signal29/risk04` 相对同步后的 robust `signal29/risk06` 指标近乎等价，2026 CAGR仍为 `-5.42%`，没有形成新前沿，判 `keep_watch`。`prom20/signal28/risk12` 的 2023 CAGR为 `-1.12%`、2026为 `-7.41%`；`signal28/risk08` 的 2026为 `-5.65%`，两者均只作 `robust_observation`：进入观察位，不是强稳定 winner。
- artifact 同步后 2017 window winner 保持 `signal28/risk08`，2020 window winner 与 tracked-only robust 更新为 `signal29/risk06`；这是既有候选端点刷新，不是本轮挑战者 promote。无人工主题标签、无 ETF、无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 的 risk04 未修复负短窗；下一轮转 `theme_signal_quality / theme_capacity_cost` 的 risk06 容量边界，硬条件仍是 2026 转正且 2020/2023 不触发护栏。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal29-risk06、signal28-risk08；`theme_signal_quality`：signal30-risk06、signal29-risk06；`theme_risk_control`：risk04-exit70、risk06-exit68；`theme_capacity_cost`：risk06-cap06、capacity-v2。

## 2026-08-21 迭代：signal28/30 主题质量确认（端点 2026-08-20）

### 上一轮候选与结果摘要

- 当前 artifact robust `signal28/risk08` 的 2020/2023 CAGR为 `2.85/0.89%`，但 2026 CAGR为 `-4.54%`，只能 `robust_observation`：进入观察位，不是强稳定 winner。`signal30/risk08` 相对它的 2020 CAGR仅改善 `0.13pp`、2023下降 `1.19pp`，2026仍为 `-4.76%`，`keep_watch`；旧 signal29/risk06 的 2023 CAGR高 `0.49pp`但短窗同样为负，`keep_watch`。
- 假设“提高信号门槛可修复弱路径短窗且不伤中窗”不获支持；artifact 与运行前 `HEAD` 一致，无人工主题标签、无 ETF、无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 转向 risk04 与较宽覆盖的正交边界，硬条件仍是 2026 转正且中窗 MaxDD不恶化超过 `5pp`；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：risk04-exit70、prom20-risk12；`theme_signal_quality`：signal28-risk08、signal30-risk08；`theme_risk_control`：risk04-exit70、risk08；`theme_capacity_cost`：capacity-v2、risk06-cap06（仅历史边界）。

## 2026-08-20 迭代：覆盖 winner 与容量边界确认（端点 2026-08-19）

### 上一轮候选与结果摘要

- `prom20/signal28/risk12` 相对 signal29 robust 未触发 2020/2023硬护栏，并改善 2017/2020 CAGR `1.70/1.30pp`，但 2023 CAGR为 `-0.92%`、2026为 `-7.12%`，仅 `robust_observation`：进入观察位，不是强稳定 winner。`capacity_v2` 虽改善 2020/2025 CAGR，却令 2020/2023 MaxDD恶化 `8.20/10.84pp`、2026 CAGR为 `-12.14%`，`reject`。signal29 robust 的 2026 CAGR仍为 `-5.33%`，继续 `robust_observation`。
- artifact 同步后正式 ID 与运行前一致；无人工主题标签、无 ETF、无 evict/archive。假设“扩大覆盖/容量能改善收益且守住风险”不获支持。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 停止 capacity-v2 同形扩参，转向 signal28/30 的风险质量确认，硬条件仍是 2026 转正；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal28-risk08、prom20-risk12；`theme_signal_quality`：signal28-risk08、signal30-risk08；`theme_risk_control`：risk04-exit70、risk08；`theme_capacity_cost`：capacity-v2、risk06-cap06（仅历史边界）。

## 2026-08-19 迭代：风险控制与覆盖排序复核（端点 2026-08-18）

### 上一轮候选与结果摘要

- `signal28/risk08` 相对 signal29/risk06 的 2020/2023 CAGR仅变化 `+0.18/-0.49pp`，但 2026 CAGR仍为 `-4.56%`，判 `keep_watch`；`signal29/risk04` 与参考几乎等价且未改善负短窗，判 `reject`。signal29/risk06 仍是 `robust_observation`，进入观察位，不是强稳定 winner。A股 artifact 同端点同步后 Path4 2017 window winner由 capacity-v2 更新为 prom20/signal28/risk12，robust 仍为 signal29/risk06；这是旧候选刷新变化，不是本轮候选晋级。无人工主题标签、无 ETF、无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 以新 2017 winner 和 capacity-v2 做覆盖/风险对照，仍要求 2026 转正且不破坏 2020/2023 MaxDD；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：prom20-signal28-risk12、capacity-v2；`theme_signal_quality`：signal28-risk08、signal29-risk06；`theme_risk_control`：risk04-exit70、risk08；`theme_capacity_cost`：capacity-v2、risk06-cap06。

## 2026-08-18 迭代：容量/成本边界确认（端点 2026-08-18）

### 上一轮候选与结果摘要

- `risk06_cap06` 相对 robust `signal29/risk06/cap05` 的 2020 CAGR改善 `0.87pp`，但 2023 CAGR转负、2026 CAGR降至 `-5.71%`，且短窗 turnover 增加 `0.80x`，判定 `reject`。`capacity_v2` 改善 2020/2025 CAGR，却在 2020/2023 MaxDD分别恶化 `7.75/10.48pp`，2026 CAGR `-8.37%`；artifact 内部排序将其推到 window 观察位，判定 `robust_observation`：进入观察位，不是强稳定 winner。`signal29` 同窗仍为弱路径 `robust_observation`。假设“放宽容量可以改善收益且不破坏稳定性”不成立；无人工主题标签、无 ETF、无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_risk_control` 优先验证 risk08 与 signal28 锚，要求 2026 不再为负且 2020/2023 MaxDD不恶化超过 `5pp`；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：risk06-cap06、capacity-v2；`theme_signal_quality`：signal28-risk08、signal29-risk06；`theme_risk_control`：risk04-exit70、signal28-risk08；`theme_capacity_cost`：capacity-v2、risk06-cap06。

## 2026-08-16 迭代：signal30 与 risk04 覆盖边界确认（端点 2026-08-14）

### 上一轮候选与结果摘要

- `signal30/risk06` 与 robust `signal29/risk06` 五窗 CAGR、Sharpe、MaxDD、turnover 完全等价；`signal29/risk04/exit70` 也仅有万分位差异，均未形成新前沿且 2026 CAGR仍为 `-4.83%`，判定 `reject` 并停止同形阈值扩参。`signal29/risk06` 仍是弱路径内 `robust_observation`：进入观察位，不是强稳定 winner。未使用人工主题标签或 ETF；正式 window winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-14 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 转向容量/成本差异，而非 signal29/30 阈值；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：risk06-cap06、capacity-v2；`theme_signal_quality`：signal28-risk08、signal29-risk06；`theme_risk_control`：risk04-exit70、risk06-exit68；`theme_capacity_cost`：capacity-v2、risk06-cap06。

## 2026-08-15 迭代：signal28/29 覆盖与 capacity 锚确认（端点 2026-08-14）

### 上一轮候选与结果摘要

- `signal28-leader76` 相对 robust `signal29-risk06` 的 2020 CAGR/Sharpe改善 `0.20pp/0.029`、2023 CAGR下降 `0.49pp`，同步后刷新 Path4 `since_2017_01` 与 `since_2020_01` window winner；但 2026 CAGR `-5.03%`，仅 `keep_watch`，不是强稳定 winner。
- `capacity_v2` 刷新 `since_2023_01` / `since_2025_01` window winner，但 2020/2023 MaxDD相对 robust 恶化 `7.60/10.59pp`、2026 CAGR `-9.91%`，仅 `robust_observation`；`signal29-risk06` 的 2026 CAGR `-4.83%`，仍为 `robust_observation`，进入观察位，不是强稳定 winner。假设“覆盖与容量能同时改善稳定性”不成立；robust/tracked 不变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-14 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 停止 signal28/29 同形微调，改验 signal30 与低风险覆盖能否避免 2026 负收益；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal30-leader78、signal29-risk04；`theme_signal_quality`：signal30-risk06、signal28-risk08；`theme_risk_control`：risk04-exit70、risk06-exit68；`theme_capacity_cost`：capacity-v2、risk06-cap05。

## 2026-08-14 迭代：signal28 与容量边界确认（端点 2026-08-13）

### 上一轮候选与结果摘要

- `signal28/leader76/risk08` 相对 signal29/risk06 在 2017/2020 CAGR 改善 `1.56/0.20pp`，回撤近似，未触发中窗护栏；但 2026 CAGR 仍为 `-4.77%`，判定 `keep_watch`，不是强稳定 winner。假设“轻量 signal28 改善主题信号质量”获有限支持。
- `capacity_v2` 在 2025 CAGR 改善 `8.35pp`，但 2020/2023 MaxDD 恶化 `7.92/10.60pp` 且 2026 CAGR `-10.24%`，仅 `robust_observation`：进入观察位，不是强稳定 winner。signal29/risk06 同样只作弱 `robust_observation`；未使用人工主题标签或 ETF，无 evict/archive。scorecard：`results/research/a_share/research_iteration_scorecard_20260814.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-13 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- 最终 guard 转向 `emergent_theme_coverage`；下一轮先确认 signal28/29 覆盖差异与 capacity 锚，不继续同形信号阈值微调。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `theme_signal_quality`：signal30-risk06、signal28-risk08；`emergent_theme_coverage`：signal28-leader76、signal29-leader78；`theme_risk_control`：risk04-exit70、risk06-exit68；`theme_capacity_cost`：capacity-v2、risk06-cap05。

## 2026-08-13 二次迭代：signal28/29 信号边界确认（端点 2026-08-12）

### 上一轮候选与结果摘要

- `signal28/leader76` 相对 signal29/risk06 在 2020/2025 CAGR 改善 `1.32pp/1.47pp`，但 2023/2026 CAGR 为 `-0.92%/-6.39%`、turnover 增加 `0.16x/0.82x`，判定 `keep_watch`。`signal29/leader78/risk12` 同样在 2023/2026 为负，判定 `keep_watch`；两条均未形成 robust 前沿。
- artifact 确认 `signal28/leader76` 为 Path4 2017-window winner，但相邻 2023 验证失败，不能写成强稳定 winner；signal29/risk06 仍为 `robust_observation`，进入观察位，不是强稳定 winner。未使用人工主题标签或 ETF，正式 robust/tracked 未改变，无 evict/archive。scorecard：`results/research/a_share/research_iteration_scorecard_20260813_iter2.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality` 停止 signal28/29-risk12 同形线，转查较轻 risk08 与 capacity-v2 的收益/容量取舍；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_signal_quality`：signal28-risk08、signal29-risk06；`emergent_theme_coverage`：signal28-leader76、signal29-leader78；`theme_risk_control`：risk08-exit68、risk06-exit68；`theme_capacity_cost`：capacity-v2、risk06-cap05。

## 2026-08-13 迭代：信号质量与容量确认（端点 2026-08-12）

### 上一轮候选与结果摘要

- `signal30/risk08` 相对 signal29/risk06 在 2020 CAGR/Sharpe 小幅改善 `0.37pp/0.032`，但 2023 CAGR 转负至 `-0.29%`，2026 CAGR 仍 `-4.46%`；判定 `keep_watch`。假设“信号30与风险8能修复中短窗”只在 2020 获弱支持。
- `capacity_v2` 的 2020 CAGR提高 `2.33pp`，但 2020/2023 MaxDD 分别恶化 `8.00pp/10.60pp`，2026 CAGR `-9.82%`；artifact 保留观察位置，判定 `robust_observation`，进入观察位，不是强稳定 winner。signal29/risk06 同样仅为弱 `robust_observation`；未使用人工主题标签或 ETF，正式 tracked 未变，无 evict/archive。scorecard：`results/research/a_share/research_iteration_scorecard_20260813.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality` 停止 signal30/risk08 同形扩参，下一轮回查 signal28/29 的 leader76/78 差异。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_signal_quality`：signal28-leader76、signal29-leader78；`emergent_theme_coverage`：prom20-signal28、prom22-signal29；`theme_risk_control`：risk06-exit68、risk08-exit66；`theme_capacity_cost`：capacity-v2、risk06-cap05。

## 2026-08-12 四次迭代：风险与容量终端确认（端点 2026-08-11）

### 上一轮候选与结果摘要

- 独立 Path4 实跑 `risk_control_v5` 与 `capacity_v2`。前者 2020/2023/2026 CAGR 为 `4.24%/-0.07%/-18.51%`，`reject`；后者为 `5.03%/1.22%/-10.98%`，被 artifact 保留为 2023/2025 窗口位置，但 2026 仍负，判定 `robust_observation`：进入观察位，不是强稳定 winner。
- 假设“leader78 下风险/容量微调能修复短窗”不成立；未使用人工主题标签，未纳入 ETF。正式 tracked 未改变，无新增 evict/archive；scorecard：`results/research/a_share/research_iteration_scorecard_20260812_iter4.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、`...signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --comparison-csv results/research/a_share/crash_resilience_strategy_comparison_iter4_batch2.csv --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### 下一轮 focus 提示

- `theme_signal_quality` 停止本组同形扩参，下一轮先确认弱锚与 capacity-v2，再决定是否改信号定义。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_signal_quality`：capacity-v2、signal29-risk06；`emergent_theme_coverage`：signal28-leader78、signal29-leader78；`theme_risk_control`：risk-control-v5、risk06-exit68；`theme_capacity_cost`：capacity-v2、risk06-cap05。

## 2026-08-12 三次迭代：信号质量确认（端点 2026-08-11）

### 上一轮候选与结果摘要

- 独立 Path4 五窗口实跑 signal-quality v3/v4 与 signal29/risk06 弱锚，不使用人工主题标签、不纳入 ETF。v3 的 2020/2023/2026 CAGR 为 `3.83%/-1.71%/-20.60%`，`reject`；v4 为 `5.31%/-0.07%/-18.51%`，只在 2020 小幅改善，`keep_watch`。
- signal29/risk06 为 `2.78%/1.39%/-4.86%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。official winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3`、`...signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- 停止 leader80 同形扩参，回到 leader78 并比较 risk-control-v5 与 capacity-v2；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_signal_quality`：signal-quality-v4、risk-control-v5；`emergent_theme_coverage`：signal28-leader78、signal29-leader78；`theme_risk_control`：risk-control-v5、risk06-exit68；`theme_capacity_cost`：capacity-v2、risk06-cap05。

## 2026-08-12 二次迭代记录（端点 2026-08-11）

### 上一轮候选与结果摘要

- prom24/signal30 的 2020/2023/2026 CAGR 为 `2.19%/-0.86%/-14.69%`；signal30/risk06 为 `2.78%/1.39%/-4.86%`，与 signal29/risk06 指标完全相同。两者均未触发中窗护栏，但未实现“2023/2026 同时转正”，判定 `keep_watch`。
- signal29/risk06 继续是弱 `robust_observation`：进入观察位，不是强稳定 winner。未做人工后视主题归类；正式 winner/robust/tracked 未变，无 evict/archive；scorecard：`results/research/a_share/research_iteration_scorecard_20260812_iter2.json`。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality` 停止 prom24/signal30 同形扩参，转查 signal-quality v3/v4 的龙头门槛与低风险组合。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `theme_signal_quality` / `emergent_theme_coverage`：signal-quality-v3、signal-quality-v4；`theme_risk_control`：risk04-exit72、risk06-exit74；`theme_capacity_cost`：capacity-v2、signal29-risk06。

## 2026-08-12 迭代记录（端点 2026-08-11）

### 上一轮候选与结果摘要

- capacity-v2 的 2020 CAGR 提高到 `5.03%`，但 2020/2023 MaxDD 相对 signal29/risk06 恶化约 `7.9pp/10.7pp`，且 2026 CAGR `-10.98%`，`reject`；signal30/risk08 的 2020/2023/2026 CAGR `3.15%/-0.30%/-4.86%`，回撤改善但中短窗未修复，`keep_watch`。
- signal29/risk06 为 `2.78%/1.39%/-4.86%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。未做人工后视主题归类；正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `theme_signal_quality` 停止 capacity-v2 同形扩参，比较 signal30 的 prom24/低风险相邻形态并保留 signal29 弱锚；要求 2023、2026 同时转正。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal28/leader76、signal30/prom24；`theme_signal_quality`：signal30/prom24、signal30/risk06；`theme_risk_control`：risk06/exit68、risk08/exit64；`theme_capacity_cost`：capacity-v2、equal-weight-cap04。

## 2026-08-11 二次迭代记录（约 07:38 CST）

### 上一轮候选与结果摘要

- signal31/leader80 的 2020/2023/2026 CAGR 为 `1.79%/-1.76%/-19.74%`，2023 CAGR/Sharpe 相对 signal29/risk06 分别下降 `3.14pp/0.304`，`reject`；signal29/risk04 与 risk06 的中窗指标近乎相同，2026 仍为 `-4.39%`，仅 `keep_watch`，降低 risk 档的修复假设未获支持。
- signal29/risk06 为 `2.85%/1.38%/-4.39%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。未做人工后视主题归类；正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 停止 signal31 与单纯 risk04 同形扩参，下一轮回到 capacity-v2 与 signal30/risk08 比较，要求 2023 非负且 2026 修复。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：capacity-v2、signal30/risk08；`theme_signal_quality`：signal30/leader78、signal29/capacity-v2；`theme_risk_control`：risk08/exit66、risk06/exit68；`theme_capacity_cost`：capacity-v2、equal-weight-cap04。

## 2026-08-11 迭代记录

### 上一轮候选与结果摘要

- equal-weight signal30/leader80 的 2023 Sharpe 下降 `0.301`，判定 `reject`；total-mv signal30/risk08 的 2020/2023/2026 CAGR 为 `3.22%/-0.31%/-4.39%`，仅 `keep_watch`。signal29/risk06 为 `2.85%/1.38%/-4.39%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。未人工后视归类主题，正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 继续以 signal29/risk06 为弱锚，尝试更高 signal quality 与更低 risk 档，要求 2023 非负且 2026 明显修复。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：signal31/leader80、signal29/risk04；`theme_signal_quality`：signal31/leader80、signal30/leader78；`theme_risk_control`：risk04/exit70、risk08/exit66；`theme_capacity_cost`：equal-weight-cap04、capacity-v2。

## 2026-08-10 二次迭代记录（约 07:27 CST）

### 上一轮候选与结果摘要

- leader80 signal31/risk10 与 signal30/risk06 的 2020/2023/2026 CAGR 为 `1.83%/-1.75%/-19.69%`、`2.19%/-1.80%/-16.19%`，均触发 2023 稳定性护栏并 `reject`；提高门槛未改善主题覆盖质量。
- signal29/risk06 为 `2.89%/1.40%/-4.13%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。未人工归类主题；正式 winner / robust / tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述3个ID>`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 停止 leader80 高门槛同形扩参，转向 equal-weight coverage 与 risk08/exit66；目标是修复 2023/2026，同时检查容量与单票集中。第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：equal-weight signal30/leader80、total-mv signal30/risk08；`theme_signal_quality`：signal32/leader82、signal31/leader80；`theme_risk_control`：risk08/exit66、risk04/exit70；`theme_capacity_cost`：cap04 equal-weight、capacity-v2。

## 2026-08-10 迭代记录

### 上一轮候选与结果摘要

- signal30-risk06 与现有 signal29-risk06 的 2020/2023/2026 CAGR 同为 `2.89%/1.40%/-4.13%`，未形成增量，前者 `keep_watch`、后者 `robust_observation`。
- capacity-v2 为 `5.24%/1.28%/-9.51%`，虽被 artifact 推到部分窗口观察位，但中窗 MaxDD 恶化 `8.37pp/10.58pp`，仅 `robust_observation`：进入观察位，不是强稳定 winner。未人工归类主题、未因短窗晋级；正式 winner / robust / tracked ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述3个ID>`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 转向 leader80 的 signal31/30，目标是提高主题信号质量并限制 2020/2023 MaxDD；第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage` / `theme_signal_quality`：`...signal31_leader80...risk10_cap05_exit58`、`...signal30_leader80...risk06_cap05_exit68`。
- `theme_risk_control`：`...signal29...risk04_cap05_exit70`、`...signal29...risk06_cap05_exit68`；`theme_capacity_cost`：capacity-v2、`...risk12_cap06_exit60`。

## 2026-08-09 二次迭代记录（约 08:00 CST）

### 上一轮候选与结果摘要

- 五窗口确认 `signal29/risk04/exit70`、`signal28/risk-control-v5` 与 `signal29/risk06`。假设是降低 risk 或提高 exit 缓冲能改善回撤；前两者 2020/2023/2026 CAGR 为 `2.89%/1.40%/-4.13%`、`2.00%/-0.98%/-10.46%`，未形成跨窗改善，均 `keep_watch`。
- risk06 观察位同样为 `2.89%/1.40%/-4.13%`，判定 `robust_observation`：进入观察位，不是强稳定 winner。未用人工主题解释持仓；window winner / robust / tracked ID 未变，无 evict。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述3个ID>`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 停止 risk04/risk06 同值扩参，改验 signal30 与 capacity-v2，重点检查 2026 负收益、top1 集中度和 2020/2023 MaxDD。第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：`...signal30_leader78...risk06_cap05_exit68`、`...capacity_v2`；`theme_signal_quality`：`...signal31_leader80...risk10_cap05_exit58`、`...signal30_leader80...risk10_cap06_exit58`。
- `theme_risk_control`：`...risk04_cap05_exit70_lowturn`、`...risk_control_v5`；`theme_capacity_cost`：`...capacity_v2`、`...risk12_cap06_exit60_lowturn`。

## 2026-08-09 迭代记录

### 上一轮候选与结果摘要

- 五窗口确认 equal-weight `signal31`、total-mv `signal30`、total-mv `signal29/risk06`；CAGR（2020/2023/2026）为 `0.36%/-0.61%/-23.92%`、`2.15%/-2.64%/-19.63%`、`2.89%/1.40%/-4.13%`。
- 前两者分别 `keep_watch` / `reject`；`signal29/risk06` 仅为弱路径内相对防守改善，判定 `robust_observation`：进入观察位，不是强稳定 winner。无 winner / robust / tracked 变化。

### 本轮候选 ID 与命令

- IDs：`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述3个ID>`。

### 下一轮 focus 提示

- `emergent_theme_coverage` 转向 drawdown/exit 细调，避免继续追逐短窗；第一条命令：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。

### Focus 候选池

- `emergent_theme_coverage`：`...signal29_leader78...risk04_cap05_exit70_lowturn`、`...signal28_leader78...risk06_cap04_exit72_risk_control_v5`。
- `theme_signal_quality`：`...signal31_leader80...risk10_cap05_exit58_lowturn`、`...signal30_leader80...risk10_cap06_exit58_lowturn`。
- `theme_risk_control`：`...risk04_cap05_exit70_lowturn`、`...risk06_cap04_exit72_risk_control_v5`。
- `theme_capacity_cost`：`...cap05_exit68_lowturn`、`...cap06_exit58_lowturn`。

## 2026-08-08 二次迭代记录（约 07:30 CST）

### 上一轮候选与结果摘要

- 本轮以 80/20-total 确认 signal30-risk08 与 signal28-risk12。假设是底座切换能缓解 2026 负收益并保持主题覆盖；实际 2020/2023/2026 CAGR 为 `7.12%/-1.34%/-14.39%`、`5.97%/-1.63%/-20.17%`，MaxDD 相对 signal29 robust 恶化约 15-19 个百分点，均 `reject`。
- signal29-risk06 为 `2.89%/1.40%/-4.13%`，仍是 `robust_observation`：进入观察位，不是强稳定 winner。未以人工/后视主题解释结果；winner/robust/tracked 无变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### 下一轮 focus 提示

- 最终 guard focus 仍为 `emergent_theme_coverage`；停止 80/20 同形扩参，改验 90/10 prom24 中间覆盖带，比较 signal30/31 门槛；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `emergent_theme_coverage`：prom24-signal31-90/10-equal、prom24-signal30-90/10-total；`theme_signal_quality`：signal31-90/10-equal、prom24-signal30-90/10-total；`theme_risk_control`：signal29-risk04、risk-control-v5；`theme_capacity_cost`：capacity-v2、signal30-cap04。

## 2026-08-08 迭代记录（约 01:30 CST）

### 上一轮候选与结果摘要

- `emergent_theme_coverage` 确认 90/10-total signal30-risk08 与 signal28-risk12。假设是 coverage penalty 与不同风险带能改善 2023/2026；实际 CAGR 为 `3.26%/-0.30%/-4.13%`、`4.24%/-0.92%/-5.98%`，只保留 `keep_watch`。
- signal29-risk06 对照为 `2.89%/1.40%/-4.13%`、平均 turnover `2.81x`，维持 `robust_observation`：进入观察位，不是强稳定 winner。未人工归类主题、无单票幸运晋级，winner/robust/tracked 无变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### 下一轮 focus 提示

- 继续 `emergent_theme_coverage`，用 80/20-total 复核同参数能否缓解 2026 负收益，同时继续检查持仓集中度、成本与单票贡献。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `emergent_theme_coverage`：signal30-risk08-80/20-total、signal28-risk12-80/20-total；`theme_signal_quality`：signal31-90/10-equal、signal30-90/10-total。
- `theme_risk_control`：risk-control-v5、signal29-risk04；`theme_capacity_cost`：capacity-v2、signal30-cap04。

## 2026-08-07 二次迭代记录（约 07:24 CST）

### 上一轮候选与结果摘要

- `emergent_theme_coverage` 确认 signal30-risk08、signal28-risk12 与 signal29-risk06 robust。两条挑战者 2020/2023/2026 CAGR 为 `3.27%/-0.29%/-3.84%`、`4.25%/-0.91%/-5.59%`，未触发二次硬护栏但 2023/2026 为负，只能 `keep_watch`，不能因 2017 或短窗局部排序晋级。
- signal29-risk06 为 `2.90%/1.41%/-3.84%`，绝对收益弱且 2026 为负，维持 `robust_observation`：进入观察位，不是强稳定 winner。未做人工主题归类；持仓、换手、成本均进入 scorecard，无单票幸运晋级、无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### 下一轮 focus 提示

- 按轮换顺序转 `theme_signal_quality`；优先确认 signal31 的 90/10 equal 与 signal30 的 90/10 total，要求 2023/2026 转正、MaxDD 不恶化且 latest top1 不构成单票幸运；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `emergent_theme_coverage`：signal30-risk08、signal28-risk12；`theme_signal_quality`：signal31-90/10-equal、signal30-90/10-total。
- `theme_risk_control`：risk-control-v5、signal29-risk04；`theme_capacity_cost`：capacity-v2、signal30-cap04。

## 2026-08-07 迭代记录

### 上一轮候选与结果摘要

- 按 `theme_risk_control` 确认 risk-control-v5、历史 capacity-v2、signal29-risk04 与 signal29-risk06 robust。v5 为 `4.36%/-0.05%/-17.97%`，中窗护栏触发，判 `reject`；capacity-v2 为 `5.16%/1.25%/-10.12%`，2020/2023 MaxDD 分别恶化约 `8.38/10.69pp`，但 artifact 将其推入 2023/2025 window 位，因此判 `robust_observation`：进入观察位，不是强稳定 winner，更不是 `promote`。
- signal29-risk04 为 `2.89%/1.41%/-3.84%`，与 risk06 基本同形且短窗仍负，只 `keep_watch`；risk06 artifact robust 同样为 `robust_observation`。window payload 已改变但 robust ID 未变；未做人工主题归类，持仓/换手已纳入卡片，无单票幸运晋级、无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### 下一轮 focus 提示

- 最终 guard 已轮转为 `emergent_theme_coverage`；risk-control-v5 停止同形，capacity-v2 仅保留 artifact 观察位。下一轮改验 signal30-risk08 与 signal28-risk12，并保留 risk06 robust；目标是 2023/2026 转正且 MaxDD 不恶化。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `theme_risk_control`：signal30-risk08、signal29-risk04；`theme_capacity_cost`：signal29-cap05、signal29-cap06。
- `emergent_theme_coverage`：signal30-risk08、signal28-risk12；`theme_signal_quality`：signal31-90/10-equal、signal30-90/10-total。

## 2026-08-06 迭代记录

### 上一轮候选与结果摘要

- 按 `theme_signal_quality` 确认 signal31/leader80 的 80/20-total、90/10-equal、90/10-total 三种底座，并与 signal29-risk06 robust 同窗比较。80/20-total 的 2023 CAGR/MaxDD 相对 robust 恶化 `5.08pp/16.24pp`，90/10-total 的 2023 CAGR/Sharpe 恶化 `3.48pp/0.33`，均 `reject`。
- 90/10-equal 的 2020/2023/2026 CAGR 为 `0.80%/-0.95%/-22.70%`，未触发硬护栏但短窗与绝对收益弱，只 `keep_watch`。signal29-risk06 为 `2.94%/1.41%/-3.55%`，artifact 仍推为 robust，但绝对收益弱且 2026 为负，判 `robust_observation`：进入观察位，不是强稳定 winner。正式 window winner/robust/tracked ID 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### 下一轮 focus 提示

- 最终 guard 已轮转到 `theme_risk_control`；signal31-total 两种底座停止同形扩参，下一轮确认 risk-control-v5 与 signal29-risk04，并保留 signal29-risk06 robust。要求 2023/2026 转正、MaxDD 不恶化且非单票幸运；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `theme_risk_control`：risk-control-v5、signal29-risk04；`theme_capacity_cost`：capacity-v2、signal30-cap04。
- `emergent_theme_coverage`：signal30-risk08、signal28-risk12；`theme_signal_quality`：signal31-90/10-equal、signal30-90/10-total。

## 2026-08-05 二次迭代记录（约 07:29 CST）

### 上一轮候选与结果摘要

- 按 `emergent_theme_coverage` 确认 signal30/risk08 与 signal28/risk12，并以 signal29/risk06 robust 同窗比较。两条挑战者 2020/2023/2026 CAGR 为 `3.35%/-0.27%/-2.75%`、`4.36%/-0.89%/-4.19%`；中窗未触发二次护栏但 2023/2026 为负，只判 `keep_watch`。
- signal29/risk06 为 `2.98%/1.43%/-2.75%`，绝对收益弱且 2026 为负、最新 top1 集中度仍高，维持 `robust_observation`：进入观察位，不是强稳定 winner。signal28/risk12 继续占既有 2017-window 位，但本轮 artifact ID 无变化；窗口排序不等于 promote。无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### 下一轮 focus 提示

- 最终 guard 预计跨入 `theme_signal_quality`；下一轮确认 active signal31/leader80 的 80/20、90/10 两种底座形态，并保留 signal29 robust。要求 2023/2026 转正、MaxDD 不恶化且 top1 集中度下降。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `emergent_theme_coverage`：signal30-risk08、signal28-risk12；`theme_signal_quality`：signal31-80/20-total、signal31-90/10-total。
- `theme_risk_control`：risk-control-v5、signal29-risk04；`theme_capacity_cost`：capacity-v2、signal30-cap04。

## 2026-08-05 迭代记录（约 01:28 CST）

### 上一轮候选与结果摘要

- 按 `theme_risk_control` 确认 80/20 risk-control-v5 与 90/10 signal29-risk04，并以 signal29-risk06 robust 同窗比较。risk-control-v5 的 2020/2023/2026 CAGR 为 `4.27%/-0.11%/-18.70%`，破坏 2023 且短窗明显为负，判 `reject`。
- signal29-risk04 为 `2.98%/1.42%/-2.75%`，与 robust 几乎等效，仅 `keep_watch`；同步后它刷新为 since_2025_01 window winner，但窗口排序不等于 `promote`。signal29-risk06 为 `2.98%/1.43%/-2.75%`，artifact 仍推为 robust，但绝对收益弱且最新 top1 集中度高，仅 `robust_observation`：进入观察位，不是强稳定 winner。robust/tracked 未替换，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### 下一轮 focus 提示

- 最终 guard 转为 `emergent_theme_coverage`。risk-control-v5 停止同形，下一轮比较 signal30/risk08 与 signal28/risk12 两个 coverage 边界，并保留当前 robust；要求 2023/2026 回撤改善且持仓不再由 top1 主导。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `theme_risk_control`：risk-control-v5、signal29-risk04；`theme_capacity_cost`：capacity-v2、signal30-cap04。
- `theme_signal_quality`：signal31-80/20、signal31-90/10；`emergent_theme_coverage`：signal30-risk08、signal28-risk12。

## 2026-08-04 二次迭代记录（约 07:29 CST）

### 上一轮候选与结果摘要

- 按 `theme_signal_quality` 五窗口确认 signal30 的 80/20 与 90/10 形态，并以 signal29 robust 同窗对照。80/20 signal30 的 2020/2023/2026 CAGR 为 `4.52%/-4.76%/-34.95%`，触发中窗 CAGR/MaxDD 护栏，判 `reject`。
- 90/10 signal30 为 `2.86%/1.40%/-3.67%`，与 signal29 指标完全相同，说明本次 signal 阈值没有产生有效差异，仅 `keep_watch`；signal29 因绝对收益弱且 2026 为负维持 `robust_observation`，进入观察位，不是强稳定 winner。未发现单票幸运式改善，window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

五窗口 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260804_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `theme_risk_control`。停止等效的 signal30/leader78 形态，下一轮改验 active risk-control-v5 与 signal29/risk04，目标是在真正改变持仓的同时改善 2023/2026 MaxDD；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `theme_risk_control`：signal28-risk-control-v5、signal29-risk04；`theme_signal_quality`：signal31-leader80-80/20、signal31-leader80-90/10。
- `emergent_theme_coverage`：signal28-coverage、signal29-coverage；`theme_capacity_cost`：signal29-capacity-v2、signal30-cap04。

## 2026-08-04 迭代记录（约 01:30 CST）

### 上一轮候选与结果摘要

- `emergent_theme_coverage` 五窗口确认 signal28-80/20、signal29-90/10 与 signal29 robust。signal28-80/20 的 2020/2023/2026 CAGR 为 `5.37%/-1.91%/-24.08%`，`reject`；signal29-90/10 为 `3.92%/-0.50%/-5.11%`，风险改善但收益仍弱，`keep_watch`。
- signal29 robust 的 2020/2023/2026 CAGR 为 `2.86%/1.40%/-3.67%`、平均 turnover `2.83x`，判 `robust_observation`；进入观察位，不是强稳定 winner。假设“coverage penalty 可改善回撤并保持收益”仅获风险侧部分支持。2017 window 排序由既有 signal28-90/10 占位，不代表本轮候选 `promote`；tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

完整五窗口 scorecard：`results/research/a_share/research_iteration_scorecard_20260804.json`。

### 下一轮 focus 提示

- coverage 缺口已为零；最终 guard 继续 `emergent_theme_coverage`，下一轮用 signal30 做 coverage 边界确认，要求同时改善 2023 与 2026，第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `emergent_theme_coverage`：signal28-coverage、signal29-coverage；`theme_signal_quality`：signal30-prom20、signal30-prom22。
- `theme_risk_control`：risk06-exit68、risk08-exit66；`theme_capacity_cost`：cap05-lowturn、cap06-lowturn。

## 2026-08-03 二次迭代记录（07:18 CST）

### 上一轮候选与结果摘要

- `emergent_theme_coverage` 确认 signal-quality-v4 与 capacity-v2，并与 signal29-lowturn robust 同窗比较。signal-quality-v4 的 2020/2023/2026 CAGR 为 `5.37%/0.34%/-18.23%`，capacity-v2 为 `5.07%/1.64%/-10.30%`；两条中窗 MaxDD 均相对 robust 恶化超过 5pp，判定 `reject`。
- signal29-lowturn 为 `3.07%/1.82%/-1.80%`，绝对收益弱且短窗为负，只作 `robust_observation`：进入观察位，不是强稳定 winner。无人工主题标签、无单票短窗晋级，winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803_iter2.json`。

### 下一轮 focus 提示

- 下一轮继续 `emergent_theme_coverage`，改验 prom20/risk12/cap06 的 80/20 与 90/10 边界；仅接受中窗 MaxDD 不再恶化且 2026 收敛的结果。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `emergent_theme_coverage`：prom20/signal28/risk12/cap06-80/20、prom20/signal29/risk12/cap06-90/10；`theme_signal_quality`：signal28/leader80-v4、signal30/leader78。
- `theme_risk_control`：risk-control-v5-80/20、risk-control-v5-90/10；`theme_capacity_cost`：capacity-v2、signal29-lowturn。

## 2026-08-03 迭代记录（01:18 CST）

### 上一轮候选与结果摘要

- `theme_capacity_cost` 五窗口确认 80/20 capacity-v2，并与 90/10 signal29-lowturn robust 同窗比较。capacity-v2 的 2020/2023/2026 CAGR 为 `5.07%/1.64%/-10.30%`，中窗 MaxDD 相对 robust 恶化超过 `10pp`，触发护栏并 `reject`。
- signal29-lowturn robust 为 `3.07%/1.82%/-1.80%`、五窗平均 turnover `2.69x`；绝对收益弱且 2026 为负，继续 `robust_observation`：进入观察位，不是强稳定 winner。无人工主题标签、无单票短窗晋级，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803.json`。

### 下一轮 focus 提示

- 最终 guard 轮换为 `emergent_theme_coverage`。下一轮以 80/20 signal-quality-v4 和 90/10 signal29-lowturn 检查覆盖扩展边界，并继续以 capacity-v2 为对照；仅接受中窗不触发护栏、2026 收敛且持仓不是单票幸运的结果。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

### Focus 候选池

- `theme_capacity_cost`：capacity-v2、signal29-lowturn；`theme_signal_quality`：signal28/leader80-v4、signal30/leader78。
- `theme_risk_control`：risk-control-v5-80/20、risk-control-v5-90/10；`emergent_theme_coverage`：p20/risk12/cap06、p22/risk06/cap05。
- `leader_quality`：signal29/leader80、signal30/leader78。

## 2026-08-02 二次迭代记录（08:42 CST）

### 上一轮候选与结果摘要

- 二次确认 risk-control-v5 的 80/20、90/10 与 signal29 robust。80/20 的 2020/2023/2026 CAGR `4.29%/0.34%/-18.23%` 且 MaxDD 恶化，`reject`；90/10 为 `2.13%/-0.69%/-8.59%`，只 `keep_watch`。
- signal29 为 `3.07%/1.82%/-1.80%`，仍是 `robust_observation`：进入观察位，不是强稳定 winner。无人工主题标签，风险控制假设未获支持；无 winner/robust/tracked 变化与 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802_iter2.json`。

### 下一轮 focus 提示

- 转 `theme_capacity_cost`，比较 capacity-v2 与 signal29，只接受集中度/回撤改善且 2020/2023 不退化。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `theme_capacity_cost`：capacity-v2、signal29-lowturn；`theme_risk_control`：risk-control-v5-80/20、risk-control-v5-90/10。
- `theme_signal_quality`：signal28/leader80、signal30/leader78；`emergent_theme_coverage`：p20/risk12/cap06、p22/risk06/cap05；`leader_quality`：signal29/leader80、signal30/leader78。

## 2026-08-02 迭代记录（08:12 CST）

### 上一轮候选与结果摘要

- `theme_risk_control` 确认 risk-control-v5 的 80/20 与 90/10 total-mv，并与 signal29 current robust 同窗比较。80/20 的 2020/2023/2026 CAGR 为 `4.29%/0.34%/-18.23%`，中窗 MaxDD/Sharpe 两项护栏命中，`reject`；90/10 为 `2.13%/-0.69%/-8.59%`，未触发硬阈值但绝对收益弱，只 `keep_watch`。
- current robust 为 `3.07%/1.82%/-1.80%`、五窗平均 turnover `2.69x`，仍为 `robust_observation`：进入观察位，不是强稳定 winner。无人工主题标签，window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802.json`。

### 下一轮 focus 提示

- risk-control-v5 未修复负窗，下一轮转 `theme_capacity_cost`，比较 capacity-v2 与 current robust；只接受集中度/回撤改善且 2020/2023 不退化。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `theme_risk_control`：risk-control-v5-80/20、risk-control-v5-90/10；`theme_capacity_cost`：capacity-v2、signal29-lowturn。
- `theme_signal_quality`：signal28/leader80、signal30/leader78；`emergent_theme_coverage`：p20/risk12/cap06、p22/risk06/cap05。
- `leader_quality`：signal29/leader80、signal30/leader78。

## 2026-08-01 二次迭代记录（07:26 CST）

### 上一轮候选与结果摘要

- `theme_signal_quality` 确认 signal30 的 80/20 与 90/10 total-mv，并与 signal29 current robust 同窗比较。80/20 的 2020/2023/2026 CAGR 为 `5.98%/1.85%/-14.64%`，中窗 MaxDD 相对 robust 恶化超过 5pp，`reject`；90/10 为 `3.07%/1.82%/-1.80%`，与 signal29 指标完全等效，只 `keep_watch`，参数提升未产生有效信号差异。
- current robust minCAGR 为 `-1.80%`、平均收益仍弱，继续判定 `robust_observation`：进入观察位，不是强稳定 winner。实验假设“仅提高 signal 门槛可改善主题质量”未获支持；window winner/robust/tracked 未改变，无人工主题标签、无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260801_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 focus=`theme_risk_control / rotate`：signal30 在同一主体上无有效差异，转向 risk-control-v5 的 80/20 与 90/10 风险边界，并继续检查 80/20 是否造成回撤放大。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `theme_signal_quality`：signal28/leader80-80/20、signal28/leader80-90/10。
- `emergent_theme_coverage`：p20/risk12/cap06、p22/risk06/cap05。
- `theme_risk_control`：risk-control-v5、current robust；`theme_capacity_cost`：cap04-capacity-v2、cap05-current-robust。
- `leader_quality`：signal29/leader80、signal30/leader78。

## 2026-08-01 迭代记录（01:20 CST）

### 上一轮候选与结果摘要

- `emergent_theme_coverage` 确认 90/10 cap06、80/20 signal-quality-v4 与 capacity-v2。三者 2020/2023/2026 CAGR 分别为 `4.02%/-0.02%/-2.82%`、`5.37%/0.34%/-18.23%`、`5.07%/1.64%/-10.30%`；前者有两个负窗，后两者相对 current robust 的中窗 MaxDD 恶化超过 5pp，全部 `reject`。
- weighted 同步后 current robust 切到 `90/10 prom22 signal29 leader78 risk06 cap05 exit68 lowturn`，minCAGR `1.82%`，但最新 top1 权重约 `69.81%`、平均 top1 约 `60.97%`，只作 `robust_observation`：进入观察位，不是强稳定 winner。该变化来自最新端点 artifact 排序，不是弱候选 promote；没有人工主题标签，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

### 下一轮 focus 提示

- focus=`emergent_theme_coverage`：转向 2017-window p20/risk12/cap06 与 current robust 的覆盖边界确认；只接受降低单票集中且不破坏 2020/2023。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn
```

### Focus 候选池

- `emergent_theme_coverage`：p20/risk12/cap06、p22/risk06/cap05 current robust。
- `theme_signal_quality`：signal30/leader78、signal28/leader80；`theme_risk_control`：risk-control-v5、current robust。
- `theme_capacity_cost`：cap04-capacity-v2、cap05-current-robust。

## 2026-07-31 迭代记录（07:55 CST）

### 上一轮候选与结果摘要

- `emergent_theme_coverage` 确认 lowturn-cap06、signal-quality-v4、capacity-v2。lowturn-cap06 的 2020/2023/2026 CAGR 为 `6.72%/-2.23%/-24.82%`，触发多项护栏，`reject`；signal-quality-v4 为 `4.82%/-0.56%/-23.20%`，未触发中窗硬阈值但短窗为负，`keep_watch`。
- capacity-v2 为 `4.59%/0.78%/-15.35%`，仍在 2023/2025 排名与 robust 观察位，但判定 `robust_observation`：进入观察位，不是强稳定 winner。实验假设“覆盖惩罚与容量约束能降低单票依赖并保住收益”仅部分支持；无人工主题归类、无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

### 下一轮 focus 提示

- focus=`emergent_theme_coverage`：用 90/10 total-mv 的 cap06 coverage 形态对照 capacity-v2，确认 base allocation 是否是本轮失败主因。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

### Focus 候选池

- `emergent_theme_coverage`：90/10-cap06-lowturn、80/20-capacity-v2。
- `theme_signal_quality`：signal-quality-v4、signal29/leader78-capacity-v2。
- `theme_risk_control`：risk-control-v5、capacity-v2。
- `theme_capacity_cost`：cap04-capacity-v2、cap06-lowturn。

## 2026-07-30 二次迭代记录（07:24 CST）

### 上一轮候选与结果摘要

- 按 `theme_signal_quality` 五窗口确认 80/20 total-mv signal-quality-v4，并与 capacity-v2 同窗比较。候选 2020 CAGR 略高 `0.30pp`、2023 低 `1.45pp`，未触发中窗硬护栏，但 2026 CAGR 从 capacity-v2 的 `-6.24%` 恶化到 `-15.37%`，只 `keep_watch`。
- capacity-v2 继续保持 Path4 window winner/robust，但 2026 为负，判定 `robust_observation`：进入观察位，不是强稳定 winner。没有人工主题分类、没有以单票幸运晋级，winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 轮换到 `theme_risk_control / rotate`。下一轮比较 80/20 total-mv risk-control-v5 与 capacity-v2，只接受中窗不触发护栏且 2026 明显收敛。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

### Focus 候选池

- `theme_risk_control`：80/20 total-mv risk-control-v5、capacity-v2；`theme_signal_quality`：signal-quality-v4、risk-control-v5。
- `theme_capacity_cost`：capacity-v2、cap05/exit70-lowturn；`emergent_theme_coverage`：signal-quality-v4、capacity-v2。

## 2026-07-30 迭代记录

### 上一轮候选与结果摘要

- 三个 Path4 底座确认 `signal_quality_v4`。80/20 total-mv 的 2020/2023/2026 CAGR 为 `5.67%/0.94%/-15.37%`，中窗未触发硬护栏但短窗转弱，判定 `keep_watch`；90/10 equal-weight 触发 2020/2023 CAGR 与 2023 Sharpe 护栏，`reject`；90/10 total-mv 中窗未触发硬护栏但 2023/2026 为负，`keep_watch`。
- 当前 `capacity_v2` 的 2026 CAGR `-6.24%`，仍只是 `robust_observation`：进入观察位，不是强稳定 winner。本轮没有人工主题归类、没有单票幸运晋级，window winner、robust candidate 与 tracked payload 未因参数竞争改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730.json`。

### 下一轮 focus 提示

- 最终 guard 仍给出 `theme_signal_quality / rotate`。下一轮只在 80/20 total-mv 上确认 signal-quality-v4 与 capacity-v2 的终点变化；若 2026 继续为负，不扩弱 90/10 底座。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

### Focus 候选池

- `theme_signal_quality`：80/20 total-mv `signal_quality_v4`、`risk_control_v5`。
- `theme_risk_control`：80/20 total-mv `risk_control_v5`、`capacity_v2`。
- `theme_capacity_cost`：`capacity_v2`、`...signal29_leader78_risk04_cap05_exit70_lowturn`。
- `emergent_theme_coverage`：80/20 total-mv `signal_quality_v4`、`capacity_v2`。

## 2026-07-29 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- `80_20_total_mv` signal30 与 `90_10_equal_weight` signal30 分别因中窗 MaxDD 恶化超过 5 个百分点、收益失速而 `reject`。
- `90_10_total_mv` signal30 在 `since_2020_01`/`since_2023_01` CAGR 仅下降约 2.16/0.39 个百分点，同时 MaxDD 改善约 8.65/9.53 个百分点，判定 `promote` 资格；artifact 仍保留 capacity-v2，未改 official winner。
- capacity-v2 对照因 `since_2026_01` 仍为负，判定 `robust_observation`：进入观察位，不是强稳定 winner。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

### 下一轮 focus 提示

- focus：`emergent_theme_coverage`。以 coverage/capacity 折中变体挑战 capacity-v2，重点复核中窗 MaxDD 与单票集中度。
- 第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2
```

### Focus 候选池

- `emergent_theme_coverage`：`...signal29...risk06_cap06_exit66_lowturn`、`...signal30...risk06_cap05_exit68_lowturn`。
- `theme_signal_quality`：`...signal30_leader78...`、`...signal29_leader78...`。
- `theme_risk_control`：`...risk04_cap04_exit72_capacity_v2`、`...risk06_cap05_exit68_lowturn`。
- `theme_capacity_cost`：`...capacity_v2`、`...cap06_exit66_lowturn`。

## 2026-07-29 迭代记录

### 上一轮候选与结果摘要

- 按 `theme_capacity_cost` 五窗口确认 cap05/exit70、prom22 cap06/exit66 与 capacity-v2。cap05 的 2020/2023 MaxDD 相对 capacity-v2 恶化 `5.87pp/5.52pp`，cap06 恶化 `9.54pp/7.15pp`，2026 CAGR 分别为 `-8.19%/-10.22%`，两条均 `reject`；容量放宽未带来可接受风险收益。
- capacity-v2 仍是 artifact window winner/robust，但 2026 CAGR `-5.32%`，故判定 `robust_observation`，进入观察位，不是强稳定 winner。独立 Path4 仍只使用 emergent-theme 自动发现池，不含人工主题标签；无新增注册、无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn`。
- 五窗口增量命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260729.json`。

### 下一轮 focus 提示

- 最终 guard focus 已轮换为 `emergent_theme_coverage`。cap05/cap06 已证伪，下一轮回到 signal30/cap05 的覆盖边界，并与 capacity-v2 同窗检查 2026 是否转正；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `theme_capacity_cost`：signal30/risk06/cap05/exit68、capacity-v2；`theme_signal_quality`：signal-quality-v4、signal30/cap05；`theme_risk_control`：risk-control-v5、capacity-v2；`emergent_theme_coverage`：signal29/cap06、signal30/cap05。

## 2026-07-28 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- 按 `theme_risk_control` 五窗口确认 90/10 与 80/20 risk-control-v5，并与正式 robust capacity-v2 同窗比较。90/10 的 2020/2023/2026 CAGR 为 `2.56%/0.08%/-4.39%`，中窗显著退化，判定 `reject`；80/20 为 `5.35%/2.43%/-6.94%`，未触发硬护栏但短窗为负，判定 `keep_watch`。
- capacity-v2 五窗口确认 `promote`，2020/2023/2026 CAGR 为 `6.12%/3.78%/1.97%`。未使用人工主题标签，无单票幸运晋级；window winner/robust/tracked 未变化，无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、对应 80/20 total-mv、正式 robust `...signal29_leader78...risk04_cap04_exit72_capacity_v2`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728_iter2.json`。

### 下一轮 focus 提示

- 最终 guard focus 为 `theme_capacity_cost`。90/10 底座已证伪，下一轮只在 80/20 上测试已注册 cap05/exit70 的容量风险折中；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `theme_risk_control`：80/20 risk-control-v5、capacity-v2；`theme_signal_quality`：signal-quality-v4、capacity-v2；`theme_capacity_cost`：cap05/exit70、capacity-v2；`emergent_theme_coverage`：signal29/cap06、capacity-v2。

## 2026-07-28 迭代记录

### 上一轮候选与结果摘要

- 按 `theme_signal_quality` 五窗口确认 signal-quality-v4、risk-control-v5，并与正式 robust `capacity_v2` 比较。v4 的 2020 CAGR 高 `0.23pp`、2023 CAGR低 `1.36pp`，v5 的 2020/2023 CAGR低 `0.77pp/1.36pp`；两条均未触发中窗硬护栏，但 2026 CAGR同为 `-6.94%`，只能 `keep_watch`，不能凭长窗小幅改善晋级。
- capacity-v2 五窗口 CAGR `6.51%/6.12%/3.78%/21.78%/1.97%`，确认 `promote`；未做人工主题归类，无单票幸运晋级，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`、`...signal28_leader78...risk_control_v5`、正式 robust `...signal29_leader78...capacity_v2`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728.json`。

### 下一轮 focus 提示

- 最终 focus 转为 `theme_risk_control`。下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`，检验底座容量变化而不放宽单票 cap。

### Focus 候选池

- `theme_risk_control`：90/10 risk-control-v5、capacity-v2；`theme_signal_quality`：90/10 signal-quality-v4、capacity-v2；`theme_capacity_cost`：cap05/exit70、capacity-v2；`emergent_theme_coverage`：signal29/cap06、capacity-v2。

## 2026-07-27 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 按 `emergent_theme_coverage` 五窗口确认 signal-quality-v4、risk-control-v5，并与正式 robust `capacity_v2` 同窗比较。v4 的 2020 CAGR 比 robust 高 `0.23pp`、2017 CAGR 高 `0.39pp`，v5 的中窗亦未触发硬护栏；但两条 2026 CAGR 均为 `-6.94%`，因此均 `keep_watch`，不能凭长窗小幅改善晋级。capacity-v2 五窗口确认 `promote`；未做人工主题归类、无单票幸运晋级，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、正式 robust `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727_iter2.json`。

### 下一轮 focus 提示

- 最终 guard focus 为 `theme_signal_quality`。v4/v5 需先修复 2026，下一轮继续以 signal-quality-v4 与 capacity-v2 做同窗边界确认，注册新变体时不得放宽 cap05；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `emergent_theme_coverage`：signal29/cap06、capacity-v2；`theme_signal_quality`：signal-quality-v4、capacity-v2；`theme_risk_control`：risk-control-v5、capacity-v2；`theme_capacity_cost`：cap05/exit70、capacity-v2。

## 2026-07-27 迭代记录

### 上一轮候选与结果摘要

- 五窗口确认 cap05/exit70、signal-quality-v4、risk-control-v5，并与正式 Path4 robust `...capacity_v2` 同窗比较。cap05 的 2020/2023 CAGR 比 robust 高 `1.29pp/0.92pp`，但 2020 MaxDD 恶化 `5.05pp`，触发护栏并 `reject`；v4/v5 未触发中窗硬护栏，但 2026 CAGR 均为 `-6.94%`，分别 `keep_watch`。实验假设“扩容量或提高 signal/leader 阈值能在不破坏风险下提高收益”仅获部分支持。capacity-v2 确认 `promote`，window winner/robust/tracked 未改变，且未做人工主题归类、无单票幸运晋级、无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`...signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`、`...signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、`...signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727.json`。

### 下一轮 focus 提示

- 最终 focus 轮换为 `emergent_theme_coverage`。下一轮优先比较 coverage-penalty 邻域，不再放宽 cap05；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `emergent_theme_coverage`：signal-quality-v4、risk-control-v5；`theme_signal_quality`：signal-quality-v4、capacity-v2；`theme_risk_control`：risk-control-v5、capacity-v2；`theme_capacity_cost`：cap05/exit70（失败边界）、capacity-v2。

## 2026-07-26 二次迭代记录（07:19 CST）

### 上一轮候选与结果摘要

- 按 `theme_capacity_cost` 五窗口确认 80/20 total-mv 的 `signal30/leader80/risk06/cap05/exit68-lowturn`，并与正式 robust `capacity_v2` 比较。挑战者 2020/2023 MaxDD 分别恶化约 `6.31pp/5.02pp`，2026 CAGR `-12.10%`，触发回撤护栏并判定 `reject`；capacity-v2 五窗口同端点确认 `promote`。实验假设“更高信号/龙头权重兼顾容量”未获支持；无人工主题标签、无单票幸运晋级、window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726_iter2.json`。

### 下一轮 focus 提示

- 停止 signal30/leader80 同形扩参；下一轮只检查 signal29/cap05/exit70 的更温和容量边界。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `theme_capacity_cost`：cap05-exit70-lowturn、capacity-v2；`theme_signal_quality`：signal-quality-v4、capacity-v2；`theme_risk_control`：risk-control-v5、capacity-v2；`emergent_theme_coverage`：signal28、capacity-v2。

## 2026-07-26 迭代记录

### 上一轮候选与结果摘要

- 按 `theme_risk_control` 五窗口确认 risk-control-v5 的三个底座，并与 80/20 total-mv `capacity_v2` 同窗比较。80/20 total-mv risk-control-v5 未触发中窗硬护栏，但 2026 CAGR `-6.94%`，判定 `keep_watch`；90/10 equal/total-mv 的 2020 或 2023 CAGR 下降超过 `3pp`，且 2026 为负，均 `reject`；capacity-v2 五窗全正，确认 `promote`。独立 Path4 robust/window winner/tracked 未改变，无人工主题标签、无单票幸运晋级、无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、相同 variant 的 `core_explore_90_10_equal_weight_winner_core` 与 `core_explore_90_10_total_mv_winner_core` 两个底座，以及 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726.json`。

### 下一轮 focus 提示

- 停止 90/10 risk-control-v5 同形扩参；下一轮仅在 80/20 total-mv 上测试 signal30 低换手风险控制，并继续与 capacity-v2 比较。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `emergent_theme_coverage`：signal-quality-v4、capacity-v2；`theme_signal_quality`：signal30/leader80/risk06 lowturn、capacity-v2。
- `theme_risk_control`：80/20 risk-control-v5、signal30/leader80/risk06 lowturn；`theme_capacity_cost`：capacity-v2、cap05-exit70-lowturn。

## 2026-07-25 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 按 `theme_signal_quality` 五窗口确认 80/20 total-mv 的 signal-quality-v4、risk-control-v5 与 capacity-v2。前两条未触发 2020/2023 硬护栏，但 2026 CAGR 均为 `-6.94%`，只判 `keep_watch`；capacity-v2 五窗全正，继续 `promote` 为 incumbent robust/window winner。
- 本轮没有人工主题标签、没有单票幸运晋级；weighted 同步未改写 Path4 robust/tracked，无 evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260725_iter2.json`。

### 下一轮 focus 提示

- 继续 signal-quality，但停止 signal28 同形；下一轮用已注册 signal30 低换手线挑战 capacity-v2。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `theme_signal_quality`：signal30 lowturn、capacity-v2；`theme_risk_control`：risk-control-v5、capacity-v2。
- `theme_capacity_cost`：capacity-v2、cap05-exit70-lowturn；`emergent_theme_coverage`：signal-quality-v4、capacity-v2。

## 2026-07-25 迭代记录

### 上一轮候选与结果摘要

- 以三个底座分别确认 `signal_quality_v4` 与 `risk_control_v5`，共 6 个 base ids。80/20 total-mv 两条的 2020/2023 CAGR 为 `6.35%/2.43%` 与 `5.35%/2.43%`，未破坏中窗但 2026 均为 `-6.94%`，判 `keep_watch`；四条 90/10 候选中窗 CAGR 弱、2026 为 `-14.66%` 或 `-4.39%`，全部 `reject`。
- 强主题信号质量/风险控制假设只获局部支持；current robust/window winner 仍为 `...capacity_v2`，tracked 未改写，无单票幸运晋级、无 evict。

### 本轮候选 ID 与命令

- 候选为 `core_explore_{80_20_total_mv,90_10_equal_weight,90_10_total_mv}_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_{signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5}`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`；四条 90/10 候选另补齐到 `2026-07-24`。

- stale 修复：对上述全部候选把同一 `--only-base-ids` 命令的 `--end-date` 改为 `2026-07-24` 后完成五窗增量复跑；最终 scorecard、strategy JSON 与 live valuation 均采用该终点。

### 下一轮 focus 提示

- `emergent_theme_coverage`：只保留 80/20 total-mv 两条观察线，与 capacity incumbent 做终点复核；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `emergent_theme_coverage`：80/20 total-mv `signal_quality_v4`、`capacity_v2`；`theme_signal_quality`：80/20 total-mv `signal_quality_v4`、`risk_control_v5`。
- `theme_risk_control`：80/20 total-mv `risk_control_v5`、`capacity_v2`；`theme_capacity_cost`：`capacity_v2`、`...cap05_exit70_lowturn`。

## 2026-07-24 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 上一轮 `capacity_v2` 继续作为 incumbent robust；本轮围绕 `theme_signal_quality/theme_risk_control` 五窗口确认四条 80/20 total_mv 候选，并与 `capacity_v2` 同窗、同指标比较。
- `risk_control_v5` 与 `signal_quality_v4` 未命中 2020/2023 硬护栏，但 2023 CAGR 仅 `2.77%`、2026 CAGR `-5.27%`，均 `keep_watch`；两条 `signal29/leader78/risk06|08/cap06` 虽 2026 CAGR 转为 `4.16%`，但 2020/2023 MaxDD 分别恶化约 `8.0pp/5.5pp`，均 `reject`。未发现单票幸运晋级，winner/robust/tracked 未改写，无 evict。

### 本轮候选 ID 与命令

- 候选：`...risk_control_v5`、`...signal_quality_v4`、`...risk06_cap06_exit66_lowturn`、`...risk08_cap06_exit64_lowturn`（完整 ID 见命令）。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap06_exit64_lowturn`。

### 下一轮 focus 提示

- 下一轮先确认两条低回撤观察线是否能修复 2026，再考虑扩大容量；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`。

### Focus 候选池

- `theme_signal_quality`：`...signal_quality_v4`、`...risk_control_v5`。
- `theme_risk_control`：`...risk_control_v5`、`...capacity_v2`。
- `theme_capacity_cost`：`...capacity_v2`、`...risk06_cap06_exit66_lowturn`。
- `emergent_theme_coverage`：`...signal_quality_v4`、`...capacity_v2`。

## 2026-07-24 收尾记录

### 上一轮候选与结果摘要

- `emergent_theme_coverage` 五窗口确认两组 variant × 三底座。80/20 `signal28/leader76/risk08/cap05/exit68` 成为 artifact 的 2017-window winner，但相对 robust `capacity_v2` 的 2023 MaxDD 恶化约 `5.10pp` 且 2026 CAGR `-0.06%`，二次判定仅 `keep_watch`。
- 80/20 `capacity_v2` 五窗口确认并继续 `promote` 为 incumbent robust；90/10 total_mv 两条防守变体 `keep_watch`，90/10 equal 两条 `reject`。无人工主题标签、无单票幸运晋级、无 active evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### 下一轮 focus 提示

- 最终 focus 为 `theme_signal_quality`；在 coverage 完整前提下降低 signal28 回撤并维持 capacity_v2 中窗收益。首条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`。

### Focus 候选池

- `emergent_theme_coverage`：`...signal28_leader76...exit68_lowturn`、`...signal29_leader78...capacity_v2`。
- `theme_signal_quality`：`...risk_control_v5`、`...signal_quality_v4`。

## 2026-07-23 收尾记录

### 上一轮候选与结果摘要

- 本轮围绕 `emergent_theme_coverage` 五窗口确认两组 variant × 三底座。`signal28/leader76/risk08/cap05/exit68` 的 80/20 total_mv 在 2017/2023 CAGR 达 `10.06%/5.64%`，2020 CAGR 仅低 current robust `0.19pp`，中窗未触发护栏；已 `promote` 为 Path4 2017-window winner，robust 仍为 `capacity_v2`。
- 同组 90/10 total_mv 用更浅回撤换取较低收益，判 `keep_watch`；90/10 equal `reject`。`signal30/leader80/risk06/cap04/exit70` 的 80/20 与 90/10 equal 被 current robust 支配，`reject`；90/10 total_mv 仅作防守 `keep_watch`。无人工主题标签、无单票幸运晋级。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`。

### 下一轮 focus 提示

- 下一轮确认新 2017 winner 的容量/成本边界，并要求 2026 至少不低于 current robust；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。

### Focus 候选池

- `emergent_theme_coverage`：signal28/leader76/risk08、capacity_v2；`theme_signal_quality`：signal-quality-v4、signal30/leader80；`theme_risk_control`：risk-control-v5、signal28/risk08；`theme_capacity_cost`：capacity_v2、signal28/cap05。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260723.json`。

## 2026-07-22 收尾记录

- 上一轮候选与结果摘要：上一轮 `risk_control_v5` 只到 raw robust 观察；本轮按 `emergent_theme_coverage` 对 `signal_quality_v4` 与 `risk_control_v5` 各三底座做五窗口确认，继续使用自动涌现主题，不做人工行业归类。
- 本轮候选 ID 与命令：六个 base ids 为三个 `PATH4_THEME_DISCOVERY_BASE_IDS` 分别拼接 `aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4` 与 `aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`；完整命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`。
- Scorecard 与判定：`signal_quality_v4` 80/20 在 2017/2020 CAGR 小幅优于 `capacity_v2`，2023 仅低约 `1.54pp` 且未触发护栏，已 `promote` 为 Path4 2017-window winner；robust 仍是 `capacity_v2`。其 90/10 total 因明显浅回撤留 `keep_watch`，90/10 equal `reject`。`risk_control_v5` 80/20 未破坏中窗但被同组支配，`keep_watch`；两个 90/10 `reject`。
- 下一轮 focus 提示：先验证新 2017 winner 与 robust 的持仓/容量差异，再扩 theme signal。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- Focus 候选池：`emergent_theme_coverage` -> `signal_quality_v4` 80/20、`capacity_v2` 80/20；`theme_signal_quality` -> `signal_quality_v4`、`prom22_signal30`；`theme_risk_control` -> `risk_control_v5`、`capacity_v2`；`theme_capacity_cost` -> `capacity_v2`、`prom22...cap05_exit70`。无单票幸运晋级，下一轮继续检查持仓集中度与交易成本。

## 2026-07-21 收尾记录

- 上一轮候选与结果摘要：上一轮 signal-quality v4 仅留观察；本轮按 `theme_risk_control` 新增 `risk_control_v5`，仍由三个 `PATH4_THEME_DISCOVERY_BASE_IDS` 自动拼接，不做人工主题归类，共 3 个 base ids、五窗口同端点实跑。
- 本轮候选 ID 与命令：新增三个完整 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`。
- Scorecard 与判定：80/20 total_mv 的 2020/2023 CAGR 为 `5.03%/1.93%`、MaxDD `-23.48%/-23.64%`、turnover `2.62x/2.42x`，raw artifact 排序进入 robust，但 `update_weighted_winners.py` 相邻验证拒绝且 2026 CAGR `-10.69%`，判 `robust_observation`：进入观察位，不是强稳定 winner。两个 90/10 底座的 2020/2023 CAGR 仅 `2.45%/-0.09%` 与 `1.13%/-0.73%`，均 `reject`。未改写 A股 official live winner。
- 下一轮 focus 提示：最终 guard 回到 `emergent_theme_coverage`；先确认 incumbent `capacity_v2`，若 risk_control_v5 的 2023 与 2026 不能转强则移除整个 variant。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- Focus 候选池：`emergent_theme_coverage` -> `capacity_v2` 80/20、`risk_control_v5` 80/20；`theme_signal_quality` -> `signal_quality_v4`、`signal_capacity_v5`；`theme_risk_control` -> `risk_control_v5`、`risk04/cap05/exit74_v6`；`theme_capacity_cost` -> `cap035/exit72_v5`、`cap04/exit74/cost_guard_v6`。
- evict/归档：两个 90/10 base_id 判 reject，但 variant 为与 80/20 共享的生成单元，暂不删除定义；只保留 80/20 active/watch，停止 90/10 同形扩参。完整 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260721.json`。

## 2026-07-20 收尾记录

- 上一轮候选与结果摘要：上一轮 `capacity_v2` 成为独立 Path4 tracked-only robust；本轮按 `theme_signal_quality` 新增 signal-quality v3/v4，仍由三个 `PATH4_THEME_DISCOVERY_BASE_IDS` 自动拼接，共六个 base ids，不做人工主题归类。
- 本轮候选 ID 与命令：执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader80_coverage_penalty_risk04_cap04_exit72_signal_quality_v3,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader80_coverage_penalty_risk06_cap04_exit74_signal_quality_v4`。
- Scorecard 与判定：80/20 总市值 v4 相对 `capacity_v2` 的 2020 CAGR/Sharpe 改善 `0.38pp/0.025`，2023 CAGR 仅低 `1.32pp`，未触发护栏，但 2026 CAGR `-5.92%`，判定 `keep_watch`；v4 两个 90/10 底座回撤显著更浅但中期收益/2026 仍弱，也只 `keep_watch`。v3 三底座综合更弱，判定 `reject` 并从 active variant 移除。没有 official winner 改写，Path4 robust/tracked 预期仍为 `capacity_v2`。
- 下一轮 focus 提示：最终 guard 已轮换到 `theme_risk_control`；不复跑 v3，改测风险暴露与容量交叉。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk06_cap04_exit72_risk_control_v5`；未注册原因：本轮先观察 v4 的 2026 负收益。
- Focus 候选池：`emergent_theme_coverage` -> `capacity_v2` 80/20、`capacity_v2` 90/10；`theme_signal_quality` -> `signal_quality_v4`、`signal_capacity_v5`；`theme_risk_control` -> `risk06/cap04/exit72_v5`、`risk04/cap05/exit74_v5`；`theme_capacity_cost` -> `cap035/exit72_v5`、`cap04/exit74/cost_guard_v6`。
- evict/归档：v3 variant 已移出 active，v4 三底座保留 watch；历史 snapshot 不删除。

## 2026-07-19 收尾记录

- 上一轮候选与结果摘要：上一轮 `prom24/risk04` 仍弱于 `prom23/signal29/risk04`；本轮按独立 `emergent_theme` 池新增 `signal30/leader80` 信号质量 v2 与 `cap04/exit72` 容量 v2，分别覆盖 80/20 总市值、90/10 总市值、90/10 等权，共 6 个 base ids，并完成五窗口比较。
- 本轮候选 ID 与命令：三个 `PATH4_THEME_DISCOVERY_BASE_IDS` 分别拼接 `aggr_13_87_prom23_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk04_cap05_exit70_lowturn_v2`、`aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述 6 个完整 IDs>`。
- Scorecard 与判定：80/20 总市值 `capacity_v2` 在 2020/2023 CAGR 为 `6.25%/4.00%`，相对旧参考仅低 `1.33pp/0.97pp`，MaxDD 改善 `4.93pp/4.74pp`、turnover 降至 `2.61x/2.43x`，2026 CAGR `2.75%`；代码相邻验证通过并成为 tracked-only 四个长窗 winner/robust，判定 `promote`。90/10 总市值容量版回撤显著更低但 2020 CAGR 低 `4.12pp`，判定 `keep_watch`；90/10 等权容量版及三条 signal-quality v2 因中长窗/2026 退化判定 `reject`。Path4 仍不直接改写 A股 official live allocation。
- 下一轮 focus 提示：最终 guard 为 `emergent_theme_coverage`。第一条可执行命令继续确认晋级组：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap04_exit72_capacity_v2`。
- Focus 候选池：`emergent_theme_coverage` -> `capacity_v2` 80/20 总市值、`capacity_v2` 90/10 总市值；`theme_signal_quality` -> `signal29/leader80/cap04_v3`、`signal28/leader78/cap04_v3`；`theme_risk_control` -> `risk06/cap04/exit72_v3`、`risk04/cap05/exit74_v3`；`theme_capacity_cost` -> `cap035/max_holdings32_v3`、`cap04/exit74/cost_guard_v3`。
- evict/归档：为两条新方向腾出槽位，旧 `prom24/signal29/risk10` 与 `prom24/signal30/risk08` 从 active 移除；新 signal-quality v2 失败后也移出 active。最终 active 为 20 个 variants，未删除历史结果。

## 2026-07-09 收尾记录

- 上一轮候选与结果摘要：上一轮 `prom23/signal29/risk04/cap05/exit70` 成为 Path4 tracked-only robust 主体；本轮按独立 `PATH4_THEME_DISCOVERY_*` 新增并确认 `prom24/signal29/risk04/cap05/exit70` 三底座，不并入 Path2，也不做半导体/AI/PCB 等人工后视主题分类。
- 本轮候选 ID 与命令：实跑 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path2_v79_two_ids>,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`。
- Scorecard 与判定：80/20 total_mv 五窗口 CAGR `9.78% / 9.98% / 9.48% / 39.78% / 32.96%`、MaxDD 最差 `-13.77%`、turnover 最高 `5.66x`，与 prom23 robust 五窗口完全持平，判定 `keep_watch`，确认扩持仓没有退化但没有增益；90/10 total_mv 在 2020/2023 CAGR `4.95% / 5.14%`、MaxDD `-6.54% / -6.13%`、turnover `2.16x / 1.78x`，判定 `keep_watch` 作为防守观察；90/10 equal_weight `since_2026_01` CAGR `-4.49%`，判定 `reject`。
- 下一轮 focus 提示：下一轮从覆盖数量转向信号质量或风险/容量交叉，第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。
- Focus 候选池：`emergent_theme_coverage` -> `prom24/signal29/risk04/cap05/exit70` 三底座、`prom21/signal29/risk04/cap05/exit70` 三底座；`theme_signal_quality` -> `prom23/signal30/risk04/cap05/exit70` 三底座、`prom22/signal30/risk06/cap05/exit68` 三底座；`theme_risk_control` -> `prom20/signal29/risk08/cap06/exit62` 三底座、`prom22/signal29/risk04/cap05/exit70` 三底座；`theme_capacity_cost` -> `prom22/signal29/risk06/cap04/exit68` 三底座、`prom20/signal28/risk08/cap04/exit68` 三底座。
- evict/归档：本轮无 Path4 evict；prom24 只保留观察，不替换 prom23 tracked-only robust。

## 2026-07-08 收尾记录

- 上一轮候选与结果摘要：上一轮留下 `prom23/signal29/risk04/cap05/exit70` 覆盖确认；本轮按独立 `PATH4_THEME_DISCOVERY_*` 实跑三底座，不并入 Path2，也不做半导体/AI/PCB 等人工后视主题分类。
- 本轮候选 ID 与命令：实跑 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_risk18>,<path1_risk16>,<path2_v78_two_ids>,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`。
- Scorecard 与判定：80/20 total_mv 在 2020/2023 CAGR `9.98% / 9.48%`、Sharpe `0.599 / 0.620`、MaxDD `-13.77% / -13.65%`、turnover `3.27x / 3.03x`，进入 Path4 tracked-only observation，判定 `robust_observation`，进入观察位，不是强稳定 winner；90/10 total_mv 在 2020/2023 CAGR `4.95% / 5.14%` 且回撤低，判定 `keep_watch`；90/10 equal_weight 在 2020/2023 CAGR `2.56% / 3.63%`，判定 `reject`。
- 下一轮 focus 提示：最终 guard 仍给 `emergent_theme_coverage`。第一条命令建议测试 `prom24/signal29/risk04` 是否能提升覆盖而不破坏 2020/2023：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`。
- Focus 候选池：`emergent_theme_coverage` -> `prom24/signal29/risk04/cap05/exit70` 三底座、`prom21/signal29/risk04/cap05/exit70` 三底座；`theme_signal_quality` -> `prom23/signal30/risk04/cap05/exit70` 三底座、`prom22/signal30/risk06/cap05/exit68` 三底座；`theme_risk_control` -> `prom20/signal29/risk08/cap06/exit62` 三底座、`prom22/signal29/risk04/cap05/exit70` 三底座；`theme_capacity_cost` -> `prom22/signal29/risk06/cap04/exit68` 三底座、`prom20/signal28/risk08/cap04/exit68` 三底座。
- evict/归档：从 active variant 移出旧 `aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit66_lowturn`；原因是同槽位非 winner/robust 且被 `prom23/signal29/risk04` 覆盖。

## 2026-07-08 迭代状态

- 上一轮候选/结果摘要：上一轮 `prom24/signal30/risk08/cap05/exit64` 判定 `keep_watch`；本轮按独立 `emergent_theme` 池和 guard `theme_risk_control` 注册并确认 `prom22/signal29/leader78/risk04/cap05/exit70` 三底座，不并入 Path2，也不做人工主题归类。
- 本轮候选 ID 与命令：新增/确认三底座 `aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`；首次不带 `--end-date` 因本地 A股缓存只到 `2026-07-07`、默认目标日 `2026-07-08` 被拒绝，随后补固定 end-date 成功。
- Scorecard 与判定：80/20 total_mv 五窗口 CAGR `9.91% / 10.18% / 9.82% / 40.95% / 35.16%`，Sharpe `0.657 / 0.611 / 0.645 / 1.316 / 0.953`，MaxDD 最差 `-13.58%`，turnover 最高 `5.66x`；相对上一 robust `risk06/exit68`，2020/2023 CAGR 几乎持平、2017 低 `0.39pp`，未触发稳定性破坏阈值。90/10 total_mv 五窗口 CAGR `4.61% / 4.96% / 5.13% / 15.16% / 16.92%`，90/10 equal_weight 为 `1.87% / 2.80% / 4.02% / 13.69% / -2.01%`，均明显弱于 80/20。判定：80/20 `promote` 到 Path4 tracked-only robust 观察位；两个 90/10 底座 `reject`。
- 强主题捕捉检查：80/20 近端仍覆盖海光信息、寒武纪、生益科技、源杰科技、新易盛、深南电路、中际旭创等电子/AI/PCB/光通信强势簇，不是单票幸运；但 2025/2026 仍不及短窗 `prom20/risk12/exit60`，第一阶段仍只 tracked-only。
- evict/归档：从 Path4 active variant 移出旧 `aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk10_cap05_exit64_lowturn`；原因是旧线非 current winner/robust，且本轮 risk-control 对照覆盖同槽位。
- 下一轮 focus：最终 guard 给 `emergent_theme_coverage`。第一条命令建议做覆盖面确认而不是继续降 risk：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom23_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk04_cap05_exit70_lowturn`。
- Focus 候选池：`emergent_theme_coverage` -> `prom23/signal29/risk04/cap05/exit70` 三底座、`prom21/signal29/risk04/cap05/exit70` 三底座；`theme_risk_control` -> `prom22/signal29/risk04/cap05/exit70` 三底座、`prom20/signal29/risk08/cap06/exit62` 三底座；`theme_signal_quality` -> `prom22/signal30/risk04/cap05/exit70` 三底座、`prom22/signal30/risk06/cap05/exit68` 三底座；`theme_capacity_cost` -> `prom22/signal29/risk06/cap04/exit68` 三底座、`prom20/signal28/risk08/cap04/exit68` 三底座。

## 2026-07-07 迭代状态

- 上一轮候选/结果摘要：上一轮 `prom22/signal30/risk08/exit66` 未替换 robust；本轮继续独立 `emergent_theme` 池，确认 `prom24/signal30/leader78/risk08/cap05/exit64` 三底座，不并入 Path2，也不做人工主题归类。
- 本轮候选 ID 与命令：新增/确认三底座 `aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_share24>,<two_path2_v74>,<one_path3_yield_v2>,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn`。
- Scorecard 与判定：80/20 total_mv 五窗口 CAGR `10.11% / 10.16% / 6.45% / 35.78% / 23.39%`，MaxDD 最差 `-14.83%`，turnover 最高 `5.82x`；90/10 total_mv CAGR `4.16% / 4.51% / 2.90% / 11.46% / 6.02%`；90/10 equal_weight CAGR `1.40% / 2.40% / 3.65% / 8.32% / -4.44%`。相对 robust `prom22/signal29/risk06/exit68`，80/20 在 2023 CAGR 低 `3.38pp` 且 2025/2026 弹性下降，判定 `keep_watch`，不替换 tracked-only robust。
- 强主题捕捉检查：80/20 近端仍能捕捉生益科技、深南电路、中际旭创、寒武纪、新易盛等电子/AI/PCB/光通信强势簇，不是单票幸运；但跨底座收益与 2023 稳定性不支持晋级。
- evict/归档：本轮未新增 Path4 evict；开局 dirty code 中的 active 变化保留，不在本轮扩大。
- 下一轮 focus：第一条命令建议回到 robust 风险结构、只提高 signal：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。
- Focus 候选池：`theme_signal_quality` -> `prom22/signal30/risk06/cap05/exit68` 三底座、`prom20/signal30/risk10/cap06/exit60` 三底座；`theme_risk_control` -> `prom22/signal29/risk04/cap05/exit70` 三底座、`prom20/signal29/risk08/cap06/exit62` 三底座；`theme_capacity_cost` -> `prom22/signal29/risk06/cap04/exit68` 三底座、`prom20/signal28/risk08/cap04/exit68` 三底座。

## 2026-07-06 迭代状态

- 上一轮候选/结果摘要：上一轮建议在 robust 主体附近测试更高 signal 与中等风险；本轮按独立 `emergent_theme` 池确认 `prom22/signal30/leader78/risk08/cap05/exit66` 三底座，不并入 Path2，也不做人工主题归类。
- 本轮候选 ID 与命令：新增三底座 `aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `10.99% / 11.76% / 7.66% / 42.85% / 41.03%`，最大回撤最差 `-13.56%`；`90/10 total_mv` CAGR `5.07% / 5.64% / 3.72% / 16.28% / 20.42%`；`90/10 equal_weight` CAGR `2.15% / 3.20% / 5.12% / 14.05% / -0.82%`。
- 强主题捕捉检查：80/20 近端仍覆盖多只电子/AI/PCB/光通信强势簇，不是单票幸运；但 2020/2023 稳定性、90/10 跨底座收益和换手代价仍弱于现有 Path4 robust 主体。
- payload 变化：`scripts/update_weighted_winners.py` 后 Path4 tracked-only robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`；第一阶段仍不并入 A股 Path1/2/3 official winner。
- evict/归档：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧 `aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；evict 原因是旧 signal29/risk08 同槽位非 winner/robust，且本轮 signal30 对照已覆盖。
- 下一轮 focus：若最终 guard 继续给 `emergent_theme_coverage` 或 `theme_signal_quality`，下一候选应回到 robust 风险结构并只提高 signal：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 2026-07-05 迭代状态

- 上一轮候选/结果摘要：上一轮留下 `prom21/signal29/leader78/risk08/cap05/exit66` 三底座；本轮已按独立 `emergent_theme` 池确认，不并入 Path2，也不做人工主题归类。
- 本轮候选 ID 与命令：新增三底座 `aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `10.99% / 11.76% / 7.66% / 42.85% / 41.03%`，最大回撤最差 `-13.56%`，换手最高 `5.66x`；`90/10 total_mv` CAGR `5.07% / 5.64% / 3.72% / 16.28% / 20.42%`；`90/10 equal_weight` CAGR `2.15% / 3.20% / 5.12% / 14.05% / -0.82%`。
- 强主题捕捉检查：80/20 近端覆盖生益科技、深南电路、寒武纪、新易盛、中际旭创、海光信息等多票强势簇，不是单票幸运；但 2020/2023 稳定性和跨底座收益仍弱于现有 Path4 robust 主体。
- payload 变化：`scripts/update_weighted_winners.py` 后 Path4 tracked-only robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`，`meanCAGR=18.60% / minCAGR=10.30%`；第一阶段仍不并入 A股 Path1/2/3 official winner。
- evict/归档：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧 `aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn`；evict 原因是旧线非 winner/robust，且本轮 `prom21/signal29/risk08/cap05/exit66` 已覆盖同一信号质量/风险控制槽位。
- 下一轮 focus：若最终 guard 继续给 `emergent_theme_coverage`，下一候选应在 robust 主体附近测试更高 signal 与中等风险，而不是继续只扩 prom；首条命令建议 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 2026-07-04 07:03 CST 状态

- 上一轮候选/结果摘要：上一轮 `prom22/signal28/risk08/cap05/exit68` 给出 robust 线索但 2020/2023 仍弱；本轮按 `emergent_theme_coverage` 测试 `prom24/signal29/leader78/risk10/cap05/exit60` 三底座，继续保持独立 `emergent_theme` 池，不并入 Path2。
- 本轮候选 ID 与命令：新增三底座 `aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit60_lowturn`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit60_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `10.30% / 10.42% / 7.01% / 37.30% / 27.80%`，最大回撤最差 `-14.83%`，换手最高 `5.82x`；`90/10 total_mv` CAGR `4.37% / 4.81% / 3.14% / 12.12% / 8.21%`；`90/10 equal_weight` CAGR `1.61% / 2.72% / 3.94% / 8.94% / -2.47%`。
- 强主题捕捉检查：80/20 近端能覆盖生益科技、深南电路、寒武纪、新易盛、中际旭创等电子/AI/PCB 强势簇，不是单票幸运；但 2020/2023 稳定性和跨底座收益弱于现有主体。
- payload 变化：本轮新增 `prom24/signal29` 未晋级；weighted 同步后 Path4 tracked-only robust 为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`，`meanCAGR=18.60% / minCAGR=10.30% / worstDD=-13.57%`。第一阶段仍不并入 A股 Path1/2/3 official winner。
- evict/归档：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧 `aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`；evict 原因是旧高信号低 cap 线非 winner/robust，且本轮 `prom24/signal29` 已覆盖同一高门槛槽位。
- 下一轮 focus：最终 guard 给出 `emergent_theme_coverage`。下一候选应测试 `prom21/signal29/leader78/risk08/cap05/exit66` 是否比本轮 prom24 更稳，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 2026-07-01 20:58 CST 状态

- 上一轮候选/结果摘要：上一轮 `prom20/signal28/risk08/cap04/exit68` 降 cap 后跨底座仍弱；本轮按 `emergent_theme_coverage` 测试覆盖面恢复到 `prom22/cap05`，仍保持独立 `emergent_theme` 池，不并入 Path2 或 Path1-lite。
- 本轮候选 ID 与命令：新增三底座 `aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `13.85% / 10.26% / 13.09% / 48.41% / 57.31%`，最大回撤最差 `-14.89%`，换手最高 `5.70x`；`90/10 total_mv` CAGR `6.76% / 6.03% / 6.08% / 19.24% / 27.21%`；`90/10 equal_weight` CAGR `3.25% / 3.28% / 5.83% / 12.01% / 6.99%`。
- 强主题捕捉检查：`80/20 total_mv` 成为 Path4 robust candidate 与 2017-window winner，但 2020/2023 仍弱于既有 `prom20/signal29/risk12/cap06/exit60`，2025 仍弱于既有 `prom20/signal29/risk10/cap06/exit62`；持仓集中度 `avg_top1 15.2% / avg_top3 28.7% / max_top1 41.6% / max_top3 52.7%`，不是纯单票幸运，但仍需压缩极端 top1 风险。
- evict/归档：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧 `aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap08_exit62_lowturn`；evict 原因是旧高 prom、高 cap 线非当前 winner/robust，且被本轮更低 cap、较宽覆盖的 prom22/cap05 对照覆盖。
- 下一轮 focus：若 guard 继续指 `emergent_theme_coverage`，下一候选池应测试 signal29/leader78 与本轮低风险 cap05 的交叉，而不是继续扩 cap；候选 `aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom21_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit66_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 2026-07-01 05:26 CST 状态

- 上一轮候选/结果摘要：上一轮 `prom20/signal28/risk08/cap05/exit66` 能捕捉 80/20 强势簇但跨底座弱；本轮按 `theme_capacity_cost` 进一步压单票到 `cap04`、放宽 exit 到 `68`，仍保持独立 `emergent_theme` 池，不并入 Path2。
- 本轮候选 ID 与命令：新增三底座 `aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap04_exit68_lowturn`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap04_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap04_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap04_exit68_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `11.07% / 8.95% / 12.13% / 42.99% / 60.47%`，最大回撤最差 `-12.42%`；`90/10 total_mv` CAGR `5.42% / 5.18% / 5.65% / 14.97% / 28.29%`；`90/10 equal_weight` CAGR `2.88% / 3.43% / 3.99% / 9.70% / 6.53%`。
- 强主题捕捉检查：80/20 近端持仓覆盖中船特气、芯碁微装、联瑞新材、中际旭创、源杰科技、宏和科技、生益科技、长飞光纤、寒武纪、新易盛、中国卫通、中国海油等多票强势簇，不是单票幸运；但 90/10 跨底座稳定性仍弱。
- payload 变化：`scripts/update_weighted_winners.py` 后 Path4 tracked-only robust candidate 与 2017/2020/2023 window payload 切到本轮 cap04；但 validation 已提示弱于既有 `signal29/risk12/cap06/exit60` 主体，第一阶段仍只作为 tracked-only 观察，不并入 A股 Path1/2/3 official。
- evict/归档：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`；evict 原因是旧高信号低 cap 线非 winner/robust，且收益弱于本轮更贴近 robust 主体的 `prom20/signal28/risk08/cap04/exit68`。
- 下一轮 focus：最终 guard 仍为 `emergent_theme_coverage`。下一轮第一候选应测试覆盖面恢复而不是继续压 cap，命令草案为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit68_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 2026-06-30 17:26 CST 状态

- 上一轮候选/结果摘要：上一轮 `prom20/signal28/risk10/cap05/exit64` 在 80/20 总市值底座可用但未改 robust；本轮按 `theme_risk_control` 降到 `risk08` 并放宽 exit 到 `66`，仍保持独立 `emergent_theme` 池，不并入 Path2。
- 本轮候选 ID 与命令：新增三底座 `aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit66_lowturn`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit66_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `13.07% / 11.75% / 11.41% / 56.04% / 83.26%`，最大回撤最差 `-14.89%`，换手最高 `5.60x`；`90/10 total_mv` CAGR `6.74% / 7.01% / 4.58% / 21.84% / 38.48%`；`90/10 equal_weight` CAGR `3.62% / 3.82% / 6.49% / 12.09% / 9.19%`。
- active pool 处理：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap06_exit56_lowturn`；evict 原因是旧高信号线非 winner/robust，且被本轮更贴近 robust 主体的 `signal28/risk08/cap05/exit66` 覆盖。
- 强主题捕捉检查：80/20 总市值近端持仓覆盖中船特气、源杰科技、宏和科技、芯碁微装、联瑞新材、生益科技、长飞光纤、寒武纪、新易盛、中际旭创等多票强势簇，不是单票幸运；但跨底座 90/10 稳定性仍弱。
- 结论与下一轮：Path4 window winner、robust candidate 与 tracked payload 未改变。最终 focus 为 `theme_capacity_cost`；下一轮第一候选建议在本轮基础上测容量成本边界 `aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap04_exit68_lowturn` 三底座，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom20_signal28_risk08_cap04_exit68_ids>`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 2026-06-30 06:12 CST 状态

- 上一轮候选/结果摘要：上一轮 prom24/signal30 低风险低 cap 线弱于既有 robust；本轮按 `theme_signal_quality/theme_risk_control` 交界，把 active 组替换为 `prom20/signal28/leader76/risk10/cap05/exit64`，仍保持独立 `emergent_theme` 池，不并入 Path2。
- 本轮候选 ID 与命令：新增三底座 `aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk10_cap05_exit64_lowturn`；最终成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk10_cap05_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk10_cap05_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk10_cap05_exit64_lowturn`。
- 执行修正：开局 guard 报 `ashare_path4_emergent_theme` 缺 `3/60`；首次按 rerun 不带 `--end-date` 因本地行情缓存未覆盖 `2026-06-30` 被拒绝，随后补 `--end-date 2026-06-26`；还补齐该 variant 的完整配置块后复跑成功，最终 guard `pass`。
- 五窗口结果：`80/20 total_mv` CAGR `13.07% / 11.75% / 11.42% / 56.04% / 83.26%`，最大回撤最差 `-14.90%`，换手最高 `5.60x`；`90/10 total_mv` CAGR `6.74% / 7.02% / 4.58% / 21.84% / 38.48%`；`90/10 equal_weight` CAGR `3.62% / 3.82% / 6.49% / 12.09% / 9.19%`。
- active pool 处理：移出 `aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`；evict 原因是旧高信号/低 cap 线非 winner/robust，且已被本轮更贴近 robust 主体的 `signal28/risk10/cap05/exit64` 覆盖。
- 强主题捕捉检查：80/20 total_mv 近端持仓覆盖中船特气、源杰科技、宏和科技、芯碁微装、联瑞新材、生益科技、长飞光纤、寒武纪、新易盛、中际旭创等多票强势簇，不是单票幸运；但 90/10 跨底座收益仍弱。
- 结论与下一轮：Path4 window winner、robust candidate 与 tracked payload 未改变。最终 focus 为 `theme_risk_control`；下一轮第一候选建议测更低 risk/更宽 exit 的三底座 `aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk08_cap05_exit66_lowturn`，命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom20_signal28_risk08_cap05_exit66_ids>`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 2026-06-29 17:30 CST 状态

- 上一轮候选/结果摘要：上一轮 prom22/signal30/cap04 作为容量成本候选已覆盖；本轮在独立 `emergent_theme` 池新增 prom24/signal30/leader80/risk06/cap04/exit70，继续不并入 Path2。
- 本轮候选 ID 与命令：新增三底座 `aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn`；命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `9.00% / 9.77% / 8.31% / 35.67% / 48.25%`，最大回撤最差 `-12.86%`；`90/10 total_mv` CAGR `4.00% / 4.79% / 2.22% / 11.26% / 13.69%`；`90/10 equal_weight` CAGR `2.19% / 4.13% / 3.31% / 11.51% / 9.44%`。
- active pool 处理：为维持 Path4 active variants cap，移出旧 `aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk12_cap08_exit60_lowturn`；evict 原因是旧高信号/高 cap 原型在稳健性与容量成本方向上弱于现有 prom20/prom22 线。
- 强主题捕捉检查：`80/20 total_mv` 近端持仓仍覆盖源杰科技、宏和科技、芯碁微装、联瑞新材、寒武纪、新易盛、中际旭创等多票强势簇，不是单票幸运；但两个 90/10 底座和 2020/2023 稳定性不足。
- 结论：Path4 window winner、robust candidate 与 tracked payload 未改变；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> emergent_theme_coverage`。下一轮第一候选建议回到覆盖面而不是继续提高 prom 数：`aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk10_cap05_exit64_lowturn` 三底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom20_signal28_risk10_cap05_exit64_ids>`。

## 本轮执行计划（2026-06-29 05:25 CST）

- 开局 guard 曾因新 Path4 变体缺三底座五窗口覆盖而 block，本轮按 `ashare_path4_emergent_theme` rerun command 优先补齐，没有改成 A股全量。首次不带 `--end-date` 因本地 A股原始行情缓存未覆盖 `2026-06-29` 失败；随后显式 `--end-date 2026-06-26` 成功。
- 本轮 active pool 处理：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`，加入 `aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn`。evict 理由：旧 prom12/signal30/risk14/cap08 高风险高 cap 线非 winner/robust，且被本轮更贴近 robust 主体的低风险/窄退出测试覆盖。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn`。成功命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn`。
- 80/20 总市值版五窗口 CAGR `11.95% / 12.82% / 9.25% / 51.32% / 69.99%`，最大回撤 `-17.68% / -17.68% / -8.48% / -10.41% / -9.73%`，换手 `3.58x / 3.65x / 3.18x / 6.29x / 6.53x`；90/10 总市值版 CAGR `5.07% / 5.79% / 4.26% / 18.40% / 20.97%`；90/10 等权版 CAGR `2.45% / 5.03% / 6.34% / 17.28% / 14.09%`。
- 结论：80/20 仍能捕捉芯碁微装、联瑞新材、宏和科技、海光信息、寒武纪、新易盛、生益科技、中际旭创等多票强势簇，不是单票幸运；但 2017/2020/2023 与 90/10 跨底座稳定性弱于现有 `prom20/signal29/risk12/cap06/exit60` robust。`scripts/update_weighted_winners.py` 后 Path4 window winner/robust/tracked-only 未切换，public/live 只同步 detail。
- 最终 focus 为 `theme_capacity_cost`。下一轮第一条命令建议不要继续只降 risk，而是测试更低 cap 与容量成本边界，同时若 active 仍满先 evict 非 winner/robust 弱项：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap05_exit60_lowturn`。

## 本轮执行计划（2026-06-28 17:40 CST）

- 上一轮 low-cap 容量成本线较弱，本轮接续启动前已注册的 `prom24/signal29/leader78/risk12/cap08/exit62` 主题风险控制候选，继续保持独立 Path4 强主题涌现路径：不做人工/后视主题归类、不纳入 ETF、不并入 Path2 扫描池。最终 guard 为 `ashare_path4_emergent_theme 60/60`。
- 本轮新增/复核三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap08_exit62_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap08_exit62_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap08_exit62_lowturn`。80/20 总市值五窗口 CAGR `13.17% / 14.41% / 11.17% / 63.73% / 103.56%`，最大回撤 `-16.86% / -15.22% / -6.64% / -6.58% / -10.66%`；90/10 总市值 2020/2026 为 `10.80% / 67.23%`，等权 2020/2026 为 `7.15% / 12.29%`。
- 结论：80/20 能继续捕捉强行业/强龙头，但跨底座稳定性弱于现有 `prom20/signal29/risk12/cap06/exit60` robust；不改变 Path4 window winner、robust candidate、tracked-only 或 public/live 展示逻辑。
- 本轮 active pool 处理：启动前已从 Path4 active 组移出两条旧 `prom16`/中间信号弱线，保留 active cap `60`；本轮无新增 evict。`generate_public_snapshot.py` 同步了 Path4 detail，并清理旧 public detail 文件。
- 最终 focus 为 `theme_risk_control`。下一轮第一条命令建议不要继续加宽 `prom24`，而是在现有 robust 主体上测试更低风险/更窄退出：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit58_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 本轮执行计划（2026-06-27 19:24 CST）

- 上一轮 `prom22/signal29/risk10/cap06/exit62` 只能在 80/20 总市值底座延续强势，本轮按最终 focus `theme_capacity_cost` 做更低单票 cap 与更宽出场的容量成本实验；仍严格保持独立 Path4 强主题涌现路径，不做人工主题归类、不纳入 ETF、不并入 Path2。
- 本轮 active pool 处理：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom14_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`，加入 `aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn`。evict 理由：旧 prom14/risk14/cap08 高风险高 cap 线非 winner/robust，且被本轮低风险低 cap 容量成本实验覆盖。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn`。命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_cap04_exit70_ids>`。
- 80/20 总市值版五窗口 CAGR `9.00% / 9.77% / 8.31% / 35.67% / 48.25%`，最大回撤 `-12.86% / -12.86% / -7.30% / -7.33% / -7.40%`；90/10 总市值版 CAGR `4.00% / 4.79% / 2.22% / 11.26% / 13.69%`；90/10 等权版 CAGR `2.19% / 4.13% / 3.31% / 11.51% / 9.44%`。结论：能捕捉 PCB/服务器/光模块/AI 芯片强势簇，但长窗与跨底座收益明显弱于既有 `prom20/signal29/risk12/cap06` 主体，不改变 Path4 window winner、robust candidate 或 tracked-only 状态。
- 最终 guard focus 仍为 `theme_capacity_cost`。下一轮第一条命令建议在本轮 low-cap 负样本基础上只做一次 `cap03/exit72` 压力测试，若 2020/2023 继续弱则回到 `cap06` 主体：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap03_exit72_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap03_exit72_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap03_exit72_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 本轮执行计划（2026-06-25 06:56 CST）

- 上一轮建议扩 `prom22` 覆盖宽度，本轮严格保持独立 Path4 强主题涌现路径，不做人工主题归类、不纳入 ETF、不并入 Path2 扫描池。
- 本轮 active pool 处理：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`，加入 `aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`，保持 Path4 active cap。evict 理由：旧 signal30/risk12 中间信号质量线非 winner/robust，且被本轮 prom22/risk10 覆盖。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`。成功命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_prom22_risk10_ids>`。
- 80/20 总市值版五窗口 CAGR `13.74% / 15.66% / 12.59% / 68.03% / 103.46%`，最大回撤 `-14.97% / -14.74% / -5.74% / -7.24% / -10.82%`，换手 `3.54x / 3.59x / 3.16x / 6.15x / 6.21x`；90/10 总市值版 CAGR `6.64% / 8.27% / 6.34% / 28.40% / 48.64%`；90/10 等权版 CAGR `3.35% / 5.57% / 7.83% / 21.44% / 9.98%`。
- 结论：80/20 底座继续能捕捉中际旭创、新易盛、生益科技、联瑞新材、海光信息等强势簇，不是单票幸运；但跨底座仍弱，official Path4 2025 winner 仍由 `prom20/signal29/risk10/cap06/exit62` 维持，robust/tracked 仍为 `prom20/signal29/risk12/cap06/exit60`。本轮不并入 A股 Path1/2/3 official winner。
- 最终 focus 为 `theme_risk_control`。下一轮第一条命令建议在 prom22/signal29 主体上做更低风险/更宽退出对照，观察能否保留 2025/2026 同时改善 2020/2023 稳定性：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap06_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap06_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap06_exit64_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入。

## 本轮执行计划（2026-06-24 19:22 CST）

- 上一轮建议在 `signal29/risk12/cap06` 主体上做风险控制，本轮严格保持独立 Path4 强主题涌现路径，不使用人工主题归类、不纳入 ETF、不并入 Path2 扫描池。
- 本轮 active pool 处理：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`，加入 `aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`，保持 Path4 active cap `60`。evict 理由：signal31/risk10/cap05 折中信号质量线连续弱于 `signal29/risk12/cap06` 主体，非 winner/robust。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 80/20 总市值版五窗口 CAGR `13.46% / 15.24% / 12.36% / 65.89% / 95.30%`，最大回撤 `-14.97% / -14.74% / -5.74% / -7.24% / -10.82%`，换手 `3.54x / 3.59x / 3.16x / 6.15x / 6.21x`；90/10 总市值版 CAGR `6.50% / 8.05% / 6.27% / 27.72% / 45.95%`；90/10 等权版 CAGR `3.28% / 5.48% / 7.82% / 21.43% / 9.66%`。
- `scripts/update_weighted_winners.py` 后 Path4 `since_2025_01` window winner 切到本轮 80/20 `risk10/cap06/exit62`，但 2017/2020/2023 winners 与 robust candidate 仍由旧 `signal29/risk12/cap06` 和 `prom18/signal28` 维持。本轮不并入 A股 Path1/2/3 official winner；强主题仍要同时看 2020/2023 稳定性、回撤、换手与是否多票捕捉。
- 最终 guard 为 `pass`，Path4 rotation 重置为 `continue`，下一轮 focus 转为 `emergent_theme_coverage`。第一条命令建议测试同主体的晋升覆盖宽度，观察是否保留 2025 winner 同时改善 2020/2023 稳定性与 90/10 跨底座表现：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入 `PATH4_THEME_DISCOVERY_VARIANT_IDS`。

## 本轮执行计划（2026-06-24 06:57 CST）

- 上一轮建议回到 `risk12/cap06` 主体做 `signal30/leader78` 中间信号质量修复；本轮严格保持独立 Path4 强主题涌现路径，不使用人工主题归类、不纳入 ETF、不并入 Path2 扫描池。
- 本轮 active pool 处理：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn`，加入 `aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`，保持 Path4 active cap `60`。evict 理由：signal29/risk10/cap05 低容量折中线已连续弱于 `risk12/cap06` 主体，非 winner/robust。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 80/20 总市值版五窗口 CAGR `11.58% / 12.27% / 8.85% / 48.68% / 57.54%`，最大回撤 `-17.69% / -17.69% / -8.48% / -10.41% / -9.73%`；90/10 总市值版 CAGR `4.96% / 5.64% / 4.24% / 18.25% / 19.81%`；90/10 等权版 CAGR `2.43% / 5.00% / 6.37% / 17.87% / 15.15%`。结论：80/20 能继续捕捉多票强势簇，但 2017/2020/2023 稳定性仍弱于现有 `signal29/risk12/cap06` 与 2023 的 `prom18/signal28`，不改 Path4 winner/robust/tracked。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；`scripts/update_weighted_winners.py` 后 Path4 2017/2020/2025 winner 与 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`，2023 winner 仍为 `prom18/signal28`。本轮不并入 A股 Path1/2/3 official winner。
- 下一轮 focus 轮到 `theme_risk_control`。第一条命令建议在 `signal29/risk12/cap06` 主体上只做风险控制，不继续提高 signal 门槛：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`；若未注册，先 evict 一条非 winner/robust 弱项后加入 `PATH4_THEME_DISCOVERY_VARIANT_IDS`。

## 本轮执行计划（2026-06-23 17:21 CST）

- 上一轮 `prom20/signal29/leader78/risk10/cap05` 证明 cap05 折中容量仍弱于 `risk12/cap06` 主体；本轮按 `theme_signal_quality` 提高信号质量到 `signal31/leader80`，同时保留 `risk10/cap05/exit58` 的低换手形态，仍不使用人工主题归类、不纳入 ETF，也不并入 Path2 扫描池。
- 本轮 active pool 处理：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn`，加入 `aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`，保持 Path4 active cap `60`。evict 理由：signal34/leader84 高门槛线收益被压低，非 winner/robust，已被本轮 signal31/leader80 折中信号质量测试覆盖。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 80/20 总市值版五窗口 CAGR `11.01% / 11.82% / 8.09% / 44.55% / 58.03%`，最大回撤 `-16.19% / -16.19% / -7.58% / -9.04% / -9.27%`，换手 `3.13x / 3.21x / 2.84x / 5.56x / 5.79x`；90/10 总市值版 CAGR `4.62% / 5.45% / 3.62% / 16.08% / 18.91%`；90/10 等权版 CAGR `2.22% / 4.43% / 5.33% / 15.37% / 14.14%`。结论：能捕捉生益科技、联瑞新材、芯朋微、川投能源、宝新能源、新集能源等多票强势簇，不是单票幸运，但收益和 2023 稳定性仍弱于 `signal29/risk12/cap06` 主体。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；`scripts/update_weighted_winners.py` 后 Path4 window winner 仍为 `prom20/signal29/risk12/cap06` 与 2023 的 `prom18/signal28`。本轮不并入 A股 Path1/2/3 official winner。
- 最终 focus 仍为 `theme_signal_quality`。下一轮第一条命令建议不要继续提高到 signal34，而是回到 `risk12/cap06` 主体做中间信号质量修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-23 05:27 CST）

- 上一轮 `prom20/signal29/leader78/risk10/cap04` 降回撤但收益偏弱；本轮按 `theme_capacity_cost` 的下一步测试 `cap05` 折中容量，仍不使用人工主题归类、不纳入 ETF，也不并入 Path2 扫描池。
- 本轮 active pool 处理：从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap04_exit58_lowturn`，加入 `aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn`，保持 Path4 active cap `60`。evict 理由：cap04 是上一轮容量成本负样本，80/20 总市值版收益不足以继续占用 active 池；public strategy detail 同步删除对应 cap04 文件。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 80/20 总市值版五窗口 CAGR `11.89% / 13.25% / 10.70% / 55.30% / 79.44%`，最大回撤 `-13.55% / -13.55% / -5.22% / -6.30% / -10.14%`，换手 `3.12x / 3.18x / 2.83x / 5.50x / 5.51x`；90/10 总市值版 CAGR `5.39% / 6.64% / 5.20% / 22.46% / 35.93%`；90/10 等权版 CAGR `2.79% / 4.61% / 6.51% / 17.96% / 8.80%`。结论：80/20 底座能捕捉中船特气、芯碁微装、中际旭创、生益科技、联瑞新材等多票强势簇，不是单票幸运，但 2017/2020/2023 仍弱于 `risk12/cap06` 主体，不改 Path4 winner/robust/tracked-only。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；`scripts/update_weighted_winners.py` 后 Path4 window winner 仍为 `prom20/signal29/risk12/cap06` 与 2023 的 `prom18/signal28`。
- 最终 focus 为 `emergent_theme_coverage`。下一轮第一条命令建议在 cap05 上扩一次晋升覆盖，验证能否修复 2023：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-22 17:34 CST）

- 上一轮 `prom26/signal34/leader84/risk08/cap04` 压回撤但收益被明显压低；本轮按 `theme_capacity_cost` 回到当前 tracked-only 主体附近，测试 `prom20/signal29/leader78` 的更低风险与更低 cap 版本，仍不做人工主题归类，也不纳入 ETF。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap04_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap04_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap04_exit58_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股其它路径合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap04_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap04_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap04_exit58_lowturn,...`。
- 80/20 总市值版五窗口 CAGR `9.53% / 10.73% / 8.52% / 43.13% / 60.25%`，最大回撤 `-10.68% / -10.68% / -4.18% / -5.15% / -8.09%`，换手 `2.49x / 2.54x / 2.26x / 4.41x / 4.38x`；90/10 总市值版 CAGR `4.66% / 5.81% / 3.70% / 15.94% / 29.19%`；90/10 等权版 CAGR `2.78% / 4.47% / 4.49% / 14.33% / 7.07%`。结论：80/20 底座的回撤/换手明显更稳，但 2017/2020/2023 收益仍弱于现有 `risk12/cap06` 主体，不改 Path4 winner/robust/tracked-only。
- 为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`；理由是该旧高风险/高 cap 线非 winner/robust，且被本轮 signal29/risk10/cap04 容量成本实验覆盖。`scripts/update_weighted_winners.py` 后 Path4 window winner 仍为 `prom20/signal29/risk12/cap06` 与 2023 的 `prom18/signal28`。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，最终 focus 仍为 `theme_capacity_cost`。下一轮第一条命令建议测试 cap05 的折中容量，而不是继续压到 cap04：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-22 05:23 CST）

- 开局 guard 报 `ashare_path4_emergent_theme` block，缺本轮新 `signal34/leader84/risk08/cap04` 三底座五窗口覆盖；已按 guard rerun command 优先补齐，没有替换为 A股全量。首次未锁 end date 时因本地 A股原始行情缓存未覆盖 `2026-06-22` 失败，随后显式 `--end-date 2026-06-18` 成功。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn`。成功命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn`。
- 80/20 总市值版五窗口 CAGR `8.47% / 9.29% / 7.76% / 36.88% / 44.08%`，最大回撤 `-10.18% / -9.92% / -7.04% / -8.02% / -7.21%`，换手 `2.43x / 2.44x / 2.25x / 4.32x / 4.62x`；90/10 等权版 CAGR `3.31% / 4.90% / 2.83% / 11.93% / 14.26%`；90/10 总市值版 CAGR `3.70% / 4.03% / 0.77% / 8.04% / 13.19%`。结论：signal34/leader84 进一步压回撤，但收益被明显压低；最新持仓能捕捉光模块、半导体、电子材料和电力能源等强势簇，但不是跨底座稳定 improvement，也不改 Path4 winner/robust/tracked-only。
- 为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`；理由是旧 prom20/signal30/risk12/cap06 线非 winner/robust，且被新一组 signal quality/risk control 变体覆盖。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`。
- `scripts/update_weighted_winners.py` 后 Path4 window winner 仍为 `prom20/signal29` 与 2023 的 `prom18/signal28`，Path4 candidate 仍为 `prom20/signal29`，本轮不并入 A股 Path1/2/3 official winner。最终 focus 转为 `theme_risk_control`；下一轮第一条命令建议回到 `prom20/signal29` 主体做风险控制，而不是继续提高 signal/leader 门槛：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit58_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-21 17:29 CST）

- 上一轮 `prom24/signal32/leader82/risk08/cap04` 只在 80/20 总市值底座保留低回撤短窗弹性，未改写 Path4 tracked-only 主体；本轮沿 `emergent_theme_coverage` 扩晋升覆盖到 `prom26`，仍不做人工主题归类，也不纳入 ETF。
- 本轮新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 80/20 总市值版五窗口 CAGR `7.14% / 7.58% / 6.49% / 38.55% / 40.90%`，最大回撤 `-14.41% / -14.41% / -6.39% / -7.53% / -7.40%`，换手 `2.41x / 2.43x / 2.25x / 4.29x / 4.62x`；90/10 等权版 CAGR `2.21% / 4.01% / 3.55% / 11.81% / 10.00%`；90/10 总市值版 CAGR `3.33% / 3.93% / 1.40% / 11.01% / 9.21%`。结论：扩覆盖后仍主要是低波动防守型主题捕捉，收益不及现有 `prom20/signal29`，不改变 Path4 winner/robust/tracked。
- 为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn`；理由是旧 prom12/signal28/risk14/cap10 线非 winner/robust，且被本轮更高信号质量和覆盖扩展形态覆盖。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`。
- 最终 focus 转为 `theme_signal_quality`。下一轮第一条命令建议提高信号质量和 leader 门槛，而不是继续单纯扩 prom：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk08_cap04_exit56_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-21 05:27 CST）

- 上一轮 focus 指向 `theme_capacity_cost`，本轮按预留命令新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`。命令严格使用五窗口 `--only-base-ids`，没有跑 A 股全量。
- 80/20 总市值版五窗口 CAGR `7.14% / 7.58% / 6.49% / 38.55% / 40.90%`，最大回撤 `-14.41% / -14.41% / -6.39% / -7.53% / -7.40%`，换手 `2.41x / 2.43x / 2.25x / 4.29x / 4.62x`；90/10 等权版 CAGR `2.21% / 4.01% / 3.55% / 11.81% / 10.00%`；90/10 总市值版 CAGR `3.33% / 3.93% / 1.40% / 11.01% / 9.21%`。结论：`cap04` 明显降低回撤和换手，但收益弱于现有 `prom20/signal29` tracked-only 主体，不改变 Path4 winner/robust/tracked。
- 为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn`；理由是同一 cap04 容量成本旧线非 winner/robust，且被本轮 `prom24/signal32/leader82/risk08/cap04` 覆盖。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`。
- 最终 focus 转为 `emergent_theme_coverage`。下一轮第一条命令建议在保持 `signal32/leader82/risk08/cap04` 的前提下扩大 coverage，而不是继续单纯压 cap：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-20 17:27 CST）

- 上一轮 `prom24/signal30/leader80/risk10/cap06/exit58` 只在 80/20 总市值保留短窗弹性；本轮按 guard blocking scope 先补齐新风险控制候选，没有替换为全量回测。新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap06_exit56_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap06_exit56_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap06_exit56_lowturn`。
- 本轮核心命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap06_exit56_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap06_exit56_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap06_exit56_lowturn`。
- 80/20 总市值版五窗口 CAGR `9.67% / 9.90% / 8.91% / 55.20% / 58.13%`，最大回撤 `-19.89% / -19.89% / -8.73% / -10.60% / -9.71%`，换手 `3.45x / 3.45x / 3.16x / 6.12x / 6.52x`；90/10 等权版 CAGR `3.02% / 5.68% / 6.22% / 17.37% / 15.02%`；90/10 总市值版 CAGR `4.87% / 5.80% / 3.58% / 17.44% / 13.84%`。结论：signal32/leader82/risk08 在 80/20 短窗仍有弹性，但 2017/2020/2023 不优于既有 `prom20/signal29`，不替换 Path4 winner/robust/tracked-only。
- 为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn`；理由是旧 prom12/signal28/risk16 高风险邻域非 winner/robust，且被本轮信号质量+风险控制实验覆盖。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`。最终 focus 转为 `theme_capacity_cost`，下一轮第一条命令建议在本轮 80/20 可比形态上压单票容量：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-20 05:28 CST）

- 上一轮把 focus 指向 `emergent_theme_coverage` 并预留 `prom24/signal30/leader80/risk10/cap06/exit58`；本轮按 guard blocking scope 先补齐三底座，新增并五窗口确认：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，先按 guard block 补 Path4 三底座，没有替换为全量回测。核心命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`。
- 80/20 总市值版五窗口 CAGR `12.18% / 13.16% / 9.03% / 50.64% / 65.12%`，最大回撤 `-17.69% / -17.69% / -8.48% / -10.41% / -9.73%`，换手 `3.57x / 3.63x / 3.18x / 6.29x / 6.53x`；90/10 等权版 CAGR `2.62% / 5.29% / 6.43% / 18.59% / 17.06%`；90/10 总市值版 CAGR `5.58% / 6.54% / 4.32% / 19.37% / 22.98%`。结论：只在 80/20 总市值底座保留短窗弹性，2017/2020/2023 不优于 `prom20/signal29` tracked-only 主体，不替换 Path4 winner/robust/tracked-only。
- 为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn`；理由是旧高风险/高 cap 邻域非 winner/robust，且被本轮 signal30/risk10/cap06 低换手实验覆盖。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`。最终 focus 为 `theme_signal_quality`，下一轮第一条命令建议在 prom24 基础上提高信号质量和 leader 要求，而不是继续扩大 prom：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk10_cap06_exit58_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-19 17:29 CST）

- 上一轮 `prom22/signal29` 不优于 Path4 tracked-only `prom20/signal29`；本轮按 guard blocking scope 优先补齐新风险控制候选，新增并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，先按 guard block 补 Path4 三底座，再与 A股其它路径合并复跑同一目标；没有跑 A股全量。核心命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`。
- 80/20 总市值版五窗口 CAGR `12.18% / 13.16% / 9.03% / 50.64% / 65.12%`，最大回撤 `-17.69% / -17.69% / -8.48% / -10.41% / -9.73%`；90/10 等权版 CAGR `2.62% / 5.29% / 6.43% / 18.59% / 17.06%`；90/10 总市值版 CAGR `5.58% / 6.54% / 4.32% / 19.37% / 22.98%`。结论：风险下移降低短窗回撤，但 2017/2020/2023 收益明显弱于 `prom20/signal29`，不替换 Path4 winner/robust/tracked-only。
- 为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`；理由是旧 prom24/signal28 线非 winner/robust，且被 prom22/signal30/risk10 的风险控制实验覆盖。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`。最终 focus 为 `emergent_theme_coverage`，第一条命令建议在保持 signal30/risk10/cap06 的前提下扩覆盖，而不是继续单纯降风险：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`；若未注册，先新增 variant 并再 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-19 05:26 CST）

- 上一轮 `prom20/signal29/leader78/risk12/cap06` 成为 Path4 tracked-only 主体；本轮按 coverage 扩展注册 `aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`，并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__...prom22...`、`core_explore_90_10_equal_weight_winner_core__...prom22...`、`core_explore_90_10_total_mv_winner_core__...prom22...`。命令类型为五窗口 `--only-base-ids` 增量确认，严格按 guard blocking scope 补齐，没有跑 A股全量。
- 80/20 总市值版五窗口 CAGR `13.32% / 15.03% / 12.28% / 64.43% / 91.37%`，最大回撤 `-14.99% / -14.74% / -5.73% / -7.24% / -10.82%`；90/10 等权版 CAGR `3.35% / 5.57% / 7.84% / 21.78% / 10.41%`；90/10 总市值版 CAGR `6.46% / 7.99% / 6.23% / 27.26% / 44.15%`。结论：prom22 只在 80/20 总市值底座有可比性，跨底座不稳，且不优于既有 `prom20/signal29` robust。
- 新增后 Path4 active 池一度到 `63`；本轮已归档 `aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn`，理由是该旧 cap04 线 15 条结果均值 CAGR 约 `11.17%`、最低 `1.63%`，不是 winner/robust，且被 cap06 与本轮 prom22/signal29 覆盖。最终 guard 恢复 `ashare_path4_emergent_theme 60/60 complete`。
- `scripts/update_weighted_winners.py` 后 Path4 2017/2020/2025 window winner 与 robust/tracked-only candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`，2023 window winner 仍为 `prom18/signal28`；本轮不并入 A股 Path1/2/3 official winner。最终 focus 为 `theme_risk_control`，下一轮第一条命令建议在 prom22 形态上做风险控制而不是继续扩大 prom：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk10_cap06_exit58_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-18 17:16 CST）

- 上一轮 `prom20/signal28/leader76/risk12/cap06` 提升短窗但 2023 稳定性不足；本轮按 focus `theme_risk_control`/下一步质量信号修复，新增 `aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`，并五窗口确认三底座：`core_explore_80_20_total_mv_winner_core__...signal29_leader78...`、`core_explore_90_10_equal_weight_winner_core__...signal29_leader78...`、`core_explore_90_10_total_mv_winner_core__...signal29_leader78...`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 80/20 总市值版五窗口 CAGR `13.17% / 14.81% / 12.17% / 63.45% / 87.72%`，最大回撤 `-14.99% / -14.74% / -5.73% / -7.24% / -10.83%`；90/10 总市值版 CAGR `6.36% / 7.84% / 6.20% / 26.83% / 42.69%`；90/10 等权版 CAGR `3.40% / 5.65% / 7.90% / 22.57% / 12.56%`。结论：强主题信号质量提升主要只在 80/20 总市值底座有效，且仍不是跨底座普适改善。
- `scripts/update_weighted_winners.py` 后 Path4 2017/2020/2025 window winner 与 Path4 candidate 切到 80/20 总市值 `signal29/leader78`，但仍标记为 Path4 tracked-only/experimental，不并入 A股 Path1/2/3 official winner。为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧弱项 `aggr_08_92_prom6_emergent_theme_risk30_cap50`；evict 理由是旧粗风险基线五窗口最差 CAGR `-33.29%`、最差回撤约 `-65.82%`，且不是 winner/robust。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，rotation 重置为 `continue`，下一轮 focus 为 `emergent_theme_coverage`。下一轮第一条命令建议做覆盖广度验证，而不是继续只提高信号阈值：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`；若未注册，先新增 variant 并再 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-18 05:21 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；开局新增 `prom20/signal28/leader76/risk12/cap06/exit60` 后 guard 报 3 个阻塞缺口，已按 rerun command 只用 `--only-base-ids` 补齐三底座五窗口。首次未锁 `--end-date` 时因 A股原始行情缓存未覆盖 `2026-06-18` 失败，随后显式 `--end-date 2026-06-17` 成功。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`。命令覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 80/20 总市值版五窗口 CAGR `13.61% / 12.45% / 12.49% / 61.32% / 83.19%`，最大回撤 `-17.80% / -14.88% / -5.32% / -7.61% / -11.05%`；90/10 总市值版 CAGR `7.31% / 8.23% / 5.37% / 25.29% / 42.14%`；90/10 等权版 CAGR `4.02% / 4.91% / 7.93% / 16.11% / 14.58%`。结论：宽晋升提升短窗，但 2023 稳定性仍不足。
- `scripts/update_weighted_winners.py` validation 拒绝本轮 80/20 总市值版替换 2020/2025，原因是 `since_2023_01` 校验 CAGR `12.49%` 低于 incumbent 要求；因此本轮不改 Path4 robust/tracked，也未替换 2017 window winner。为维持 active cap，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧弱项 `aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn`，evict 理由是旧 signal29/高 cap 邻域不属于 winner/robust 且被本轮 signal28/cap06 覆盖。
- 最终 focus 为 `theme_signal_quality`。下一轮第一条命令建议在本轮短窗强形态上提高一点信号质量和 leader 要求，观察 2023 是否改善：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-17 18:02 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；开局新增 `signal28/leader76/prom18/cap06` 变体后 guard 报 3 个阻塞缺口，已按 rerun command 只用 `--only-base-ids` 补齐三底座五窗口，没有替换成全量回测。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`。命令覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 80/20 总市值版五窗口 CAGR `13.46% / 12.16% / 12.31% / 59.54% / 77.38%`，最大回撤 `-17.80% / -14.88% / -5.32% / -7.61% / -11.05%`，换手 `3.58x / 3.59x / 3.19x / 6.23x / 6.30x`；它成为 Path4 `since_2017_01` window winner，并使 Path4 rotation 重置为 `continue`。90/10 总市值版更稳但收益低，五窗口 CAGR `7.18% / 7.96% / 5.28% / 23.98% / 38.42%`；90/10 等权版长窗仅 `4.04% / 4.86%`。
- `scripts/update_weighted_winners.py` 的验证层仍拒绝把新 80/20 变体作为 2020/2025 替代，原因是 `since_2023_01` 校验 CAGR `12.31%` 低于 incumbent 要求；因此它只改 Path4 2017 window winner，不改 robust/tracked。为维持 active cap，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧弱项 `aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn`，evict 理由是旧高风险/高 cap 邻域且不属于 winner/robust。
- 最终 focus 为 `emergent_theme_coverage`。下一轮第一条命令建议沿本轮胜出的 coverage 放宽方向提高晋升宽度，同时观察是否改善 2023 稳定性：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-17 05:20 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；开局注册 `aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn` 后 guard 先报 3 个缺口，按 rerun command 用 `--only-base-ids` 补齐三底座五窗口。首次未锁 `--end-date` 时因本地 A股缓存未覆盖 `2026-06-17` 失败，随后显式 `--end-date 2026-06-16` 成功。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn`。实际成功命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn`。
- 80/20 总市值版五窗口 CAGR `8.67% / 9.28% / 6.17% / 33.37% / 39.31%`，最差回撤 `-12.85%`，平均换手约 `3.28x`；90/10 等权版 CAGR `2.27% / 4.25% / 3.74% / 12.80% / 13.13%`；90/10 总市值版 CAGR `3.87% / 4.61% / 1.63% / 11.20% / 13.23%`。结论：cap04 明显压单票容量但收益不如 cap06，短窗可正、长窗不足，不替换 Path4 window winner、robust candidate 或 tracked payload。
- 为维持 active cap，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧弱项 `aggr_13_87_prom18_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn`，evict 理由是 15 行覆盖均值 CAGR 约 `13.62%`、最差回撤约 `-25.96%`，不属于 winner/robust。最终 focus 转为 `emergent_theme_coverage`，下一轮第一条命令建议不要继续单票 cap 下压，改测覆盖宽度修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap06_exit60_lowturn`；若未注册，先新增 variant 并同步 evict 一条非 winner/robust 弱项。

## 本轮执行计划（2026-06-16 17:36 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；上一轮预留的 `theme_risk_control` 新 variant 已在 3 个 Path4 base ids 上五窗口确认。为保持 active 池 cap，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出旧弱项 `aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn`，evict 理由是 active 内均值最低（约 `12.15%`）且最差回撤约 `-25.71%`，不属于 winner/robust。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap06_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap06_exit58_lowturn`。实际命令为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 80/20 总市值版 CAGR `11.60% / 12.31% / 8.46% / 45.87% / 49.89%`，最大回撤 `-17.69% / -17.69% / -8.48% / -10.41% / -9.73%`；90/10 等权版 CAGR `2.64% / 5.31% / 6.41% / 18.11% / 16.45%`；90/10 总市值版 CAGR `5.39% / 6.27% / 4.18% / 17.44% / 17.95%`。结论：新 variant 相比旧 robust 更偏短窗风险控制，但 2023 稳定性不足，不替换 Path4 window winner 或 tracked-only robust。
- `scripts/update_weighted_winners.py` 后 Path4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`。最终 focus 为 `theme_capacity_cost`，下一轮第一条命令建议在本轮胜出的 80/20 形态上继续压单票容量和换手成本：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-15 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader82_coverage_penalty_risk10_cap04_exit58_lowturn`；若未注册，先新增 variant 并同步 evict 一条旧弱项。

## 定位

Path 4 用来捕捉从市场结构中自动涌现的强主题，不使用人工主题名单，也不把“半导体、存储”等事后标签写进策略。ETF 先不纳入，本阶段只在现有 A 股股票动态池内探索。

## 信号原则

- 主题只能从已有截面数据中自然产生：行业相对强度、行业内龙头强度、3-1 动量、近 1 月收益、成交额放量、20 日突破。
- 不做显性主题归类，避免后视镜。
- 财务质量仍保留为底线，但强主题路径会降低质量分位门槛，避免强趋势早期被传统质量筛选过早拦下。
- 回测执行规则不变：信号来自收盘数据，收益从下一个交易日调仓后开始计算。

## 第一批候选

本轮新增 `core_signal_mode = emergent_theme` 与 `promotion_signal_mode = emergent_theme`，并先观察 3 个底座乘 4 个变体：

- `core_explore_80_20_total_mv_winner_core`
- `core_explore_90_10_equal_weight_winner_core`
- `core_explore_90_10_total_mv_winner_core`

变体：

- `aggr_02_98_prom2_emergent_theme_cash_off_and_cap95`
- `aggr_02_98_prom2_emergent_theme_risk40_cap90`
- `aggr_05_95_prom3_emergent_theme_risk40_cap70`
- `aggr_08_92_prom6_emergent_theme_risk50_cap50`

## 迭代规则

- `research_iteration_guard.py` 会按代码中的 `PATH4_THEME_DISCOVERY_BASE_IDS` 与 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 实际集合做独立 coverage scope 检查，要求覆盖 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`。
- Path 4 不通过 `path2_candidate_pass.py` 的扫描族评价，也不把 emergent_theme 变体并入 Path 2；横向比较只读取独立 Path4 结果、weighted robust payload 与持仓明细。
- 第一阶段不直接改写 official winner；等五窗口完整后，再决定是否独立展示为 Path 4 winner 或并入现有 winner 体系。

## 本轮执行计划（2026-06-16 05:17 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮仍只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF，也没有把 emergent_theme 结果并入 Path2。
- 本轮为维持 active cap `60`，从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` evict 旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap10_exit60_lowturn`；原因是该 signal28/leader76/cap10 形态已被 signal30-32、leader80-82 与 cap08 低换手系列覆盖，近期不改善 2020/2023 或 robust。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `8.68% / 8.76% / 6.85% / 44.53% / 23.75%`，最大回撤 `-21.13% / -21.13% / -8.67% / -10.53% / -10.52%`；`90/10 equal_weight` 为 `3.40% / 6.77% / 8.00% / 20.71% / 13.45%`；`90/10 total_mv` 为 `5.41% / 6.20% / 4.27% / 17.78% / 3.65%`。结论：高信号质量仍能捕捉强龙头组合，但中长窗收益不足，不能只凭 2025/2026 短窗晋级，不替换 Path4 window winner、robust candidate 或 tracked payload。
- 最终 guard 将 focus 推到 `theme_risk_control`。下一轮第一条命令建议降低一点信号质量、提高 leader 要求，并把 risk trigger 收到 `risk10`，测试 `signal32/leader84/risk10` 是否比 signal34 更稳：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal32_leader84_coverage_penalty_risk10_cap08_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal32_leader84_coverage_penalty_risk10_cap08_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal32_leader84_coverage_penalty_risk10_cap08_exit60_lowturn`；若未注册，先 evict 一条旧弱线后加入 `PATH4_THEME_DISCOVERY_VARIANT_IDS`。

## 本轮执行计划（2026-06-15 17:18 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮 Path4 只完成独立池巡检、weighted robust 判读和下一轮候选设计，没有新增 Path4 `--only-base-ids` 回测，也没有把 emergent_theme 结果并入 Path2。
- 上一轮候选 `prom20/signal30/leader80/risk12/cap06/exit60_lowturn` 已被 validation 拒绝；当前 Path4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`，robust 指标约 `meanCAGR=21.54%`、`minCAGR=10.87%`、最差回撤 `-17.45%`、平均换手 `4.49x`。
- 本轮未触发 Path4 evict；原因是新增实验预算优先给 Path1 risk10、Path2 v41、Path3 cap40、Path5 事件篮子和 HK Path1/2/3，且 Path4 coverage 没有 blocking 缺口。候选池仍处于 cap `60`，下一轮新增前必须先淘汰一条旧弱线。
- 最终 focus 为 `theme_signal_quality`。下一轮第一条命令沿上一轮未跑的更高信号质量三底座推进：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn`；若未注册，先 evict 旧弱线后加入 `PATH4_THEME_DISCOVERY_VARIANT_IDS`。

## 本轮执行计划（2026-06-15 05:39 CST）

- 开局 guard 在注册本轮新变体后报告 `ashare_path4_emergent_theme 3/60 missing`；已按 blocking scope 的 `--only-base-ids` 命令补齐三底座五窗口，最终 guard 恢复 `pass`、`ashare_path4_emergent_theme 60/60 complete`。有效补缺口命令使用 `AIINVESTOR_FORCE_OFFLINE=1` 与 `--end-date 2026-06-12`，没有替换成全量回测。
- 本轮为维持 active cap `60`，从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` evict 旧弱线 `aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`；原因是它已被 signal30/leader80/prom20/cap06 线覆盖，且不改善 2020/2023 或 robust。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `10.90% / 11.28% / 7.86% / 40.25% / 31.80%`，最大回撤 `-17.69% / -17.69% / -8.48% / -10.41% / -9.73%`；`90/10 equal_weight` 为 `2.46% / 5.05% / 6.28% / 16.71% / 12.16%`；`90/10 total_mv` 为 `5.09% / 5.83% / 4.00% / 15.21% / 11.16%`。结论：能捕捉强行业/强龙头，但 2020/2023 稳定性仍弱，`scripts/update_weighted_winners.py` validation 拒绝，不替换 Path4 winner、robust 或 tracked payload。
- 最终 focus 为 `theme_signal_quality`。下一轮第一条命令建议先 evict 一条旧弱线，再测试更高信号质量而不是继续降 cap：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal34_leader84_coverage_penalty_risk12_cap08_exit60_lowturn`；若未注册，先加入 `PATH4_THEME_DISCOVERY_VARIANT_IDS`。

## 本轮执行计划（2026-06-14 17:25 CST）

- 开局 guard 为 `pass`；注册本轮 `cap06/exit60` 后 guard 立即报告 `ashare_path4_emergent_theme 3/60 missing`，已严格按 `report.blocking_scopes.rerun_commands` 用 `--only-base-ids` 补齐三底座五窗口，最终恢复 coverage complete。本轮仍只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。
- 本轮为维持 active cap `60`，从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` evict 旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn`；原因是同一 signal30/leader80/risk12 形态已被 cap08/exit60 与本轮 cap06/exit60 覆盖，且不改善 2020/2023 或 robust。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`。补缺口命令覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有替换成全量回测。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `10.90% / 11.28% / 7.86% / 40.25% / 31.80%`，最大回撤 `-17.69% / -17.69% / -8.48% / -10.41% / -9.73%`，换手 `3.57x / 3.63x / 3.18x / 6.29x / 6.53x`；`90/10 equal_weight` 为 `2.46% / 5.05% / 6.28% / 16.71% / 12.16%`；`90/10 total_mv` 为 `5.09% / 5.83% / 4.00% / 15.21% / 11.16%`。结论：cap06 降容量后没有改善 2020/2023 稳定性，`scripts/update_weighted_winners.py` validation 继续拒绝，不替换 Path4 window winner、robust candidate 或 tracked payload。
- 中段 guard focus 为 `emergent_theme_coverage`。下一轮第一条命令建议先 evict 一条旧弱线，再测试更宽 promotion 但保留 signal30/leader80：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`；若未注册，先加入 `PATH4_THEME_DISCOVERY_VARIANT_IDS`。

## 本轮执行计划（2026-06-14 05:29 CST）

- 开局 guard 为 `pass`；注册本轮 prom18/risk12/cap08 变体后按 `--only-base-ids` 五窗口补齐，最终 guard 为 `pass`、`ashare_path4_emergent_theme 60/60 complete`。本轮仍只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。
- 本轮为维持 active cap `60`，从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` evict 旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64`；原因是 signal28/leader74/cap12 旧形态已被 leader78-80、coverage_penalty、lowturn 与 cap08 系列覆盖，近期不改善 2020/2023 或 robust。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn`。补齐命令与 Path2/3 合并执行，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `10.67% / 10.72% / 6.82% / 43.16% / 31.21%`，最大回撤 `-17.58% / -17.58% / -8.42% / -10.44% / -10.55%`；`90/10 equal_weight` 为 `3.08% / 6.54% / 8.25% / 22.38% / 16.09%`；`90/10 total_mv` 为 `6.52% / 7.53% / 5.29% / 20.31% / 14.48%`。结论：`80/20 total_mv` 能捕捉中国卫通、中际旭创、新易盛、寒武纪、生益科技等强龙头，但 2020/2023 稳定性和 robust 指标仍低于当前 `prom12/signal30/leader80/risk14/cap08` robust，不替换 official winner/robust/tracked。
- `scripts/update_weighted_winners.py` 后 Path4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`，robust 指标仍约 `meanCAGR=21.54%`、`minCAGR=10.87%`。最终 focus 为 `theme_capacity_cost`；下一轮第一条命令建议继续从 cap08 降到 cap06 做容量成本压力，而不是提高 promotion：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap06_exit60_lowturn`；若未注册，先 evict 一条旧弱线后注册。

## 本轮执行计划（2026-06-13 17:30 CST）

- 开局 guard 为 `pass`；注册本轮 prom24 变体后 guard 一度提示 `ashare_path4_emergent_theme 3/60 missing`，已严格按 rerun command 用 `--only-base-ids` 补齐五窗口，最终 guard 恢复 `pass`、`ashare_path4_emergent_theme 60/60 complete`。本轮仍只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。
- 本轮为维持 active cap `60`，从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` evict 旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64`；原因是 leader72/signal28/cap12 旧形态已被 leader76-80、coverage_penalty、lowturn 与本轮 prom24 宽覆盖形态覆盖，近期不改善 2020/2023 或 robust。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`。补齐命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `9.62% / 8.94% / 10.87% / 52.20% / 59.11%`，最大回撤 `-20.91% / -20.91% / -5.19% / -6.58% / -10.66%`；`90/10 total_mv` 为 `5.95% / 6.76% / 8.02% / 30.38% / 39.60%`；`90/10 equal_weight` 为 `2.25% / 4.24% / 9.10% / 27.66% / 9.75%`。结论：80/20 total_mv 能捕捉光模块、半导体设备、能源质量龙头等强结构，且不是单票幸运，但 2020/2023 收益弱于当前 Path4 robust，不替换 official winner/robust/tracked。
- `scripts/update_weighted_winners.py` 后 Path4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`，robust 指标 `meanCAGR=21.54%`、`minCAGR=10.87%`、最差回撤 `-17.45%`。最终 focus 为 `theme_risk_control`；下一轮第一条命令建议不要继续单纯放宽 promotion，改测更低风险触发并保留 cap08：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn`；若未注册，先 evict 一条旧弱线后注册。

## 本轮执行计划（2026-06-13 05:09 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。上一轮 prom20/signal28 未改善 robust；本轮未新增 Path4 回测，预算投给 HK 与 Path5 事件篮子，但重新同步 weighted winners 后 Path4 robust/tracked 口径发生有效变化。
- 本轮候选/结果摘要：`scripts/update_weighted_winners.py` 将 Path4 robust candidate 切到 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`，四窗口 robust 指标为 `meanCAGR=21.54%`、`minCAGR=10.87%`、最差回撤 `-17.45%`、平均换手 `4.49x`；它不是短窗单票幸运，`since_2026_01` 最新 top3 权重约 `28.47%`，但 2020/2023 稳定性仍弱于完全晋级要求。
- 本轮命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`；没有新增 Path4 `--only-base-ids`，也没有新增 evict。Path5 新事件篮子复核与该 Path4 参考持仓在事件日前快照 `2026-04-30` 仅重合 `1/6`，说明 Path5 能提供独立候选层。
- 下一轮 focus 继续为 `emergent_theme_coverage`。新增前先 evict 一条旧弱线，然后注册更宽 promotion 但不继续降低 signal 质量的对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`；若未注册，先加入 `PATH4_THEME_DISCOVERY_VARIANT_IDS`。

## 本轮执行计划（2026-06-12 05:28 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。上一轮 prom20/signal30/leader80 未改 robust，本轮按 `emergent_theme_coverage` 降到 `signal28/leader78`，保持 `prom20/risk14/cap08/exit62/lowturn`，检查更宽覆盖是否改善中窗。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `9.89% / 9.34% / 11.09% / 53.78% / 66.64%`，最大回撤 `-20.91% / -20.91% / -5.19% / -6.58% / -10.66%`，换手 `4.02x / 4.00x / 3.36x / 6.77x / 6.93x`；`90/10 equal_weight` 为 `2.19% / 4.16% / 9.04% / 26.39% / 8.02%`；`90/10 total_mv` 为 `6.19% / 7.10% / 8.15% / 31.47% / 44.82%`。结论：`80/20 total_mv` 的回撤浅，但 2020/2023 收益明显不足；不能只凭 2025/2026 短窗晋级。
- `scripts/update_weighted_winners.py` 后 Path4 window winners 与 robust 未被本轮 prom20/signal28 替换；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`。为维持 active cap，本轮 evict 代码实际弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn`；原因是 signal27/leader72 已被 signal28-30、leader78-80 与 prom18-20 系列覆盖，且不改善 2020/2023 或 robust。
- 最终 guard focus 继续为 `emergent_theme_coverage`。下一轮第一条命令建议在新增前先 evict 一条旧弱线，然后注册更宽 promotion 但不再降低 signal 质量的对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn`；若未注册，先加入 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 后再跑。

## 本轮执行计划（2026-06-07 16:06 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。上一轮 signal30 失败后，按 `theme_capacity_cost` 回到 signal28/leader76，并把 cap 降到 `10%`、risk 放在 `16%`。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `11.45% / 18.08% / 25.27% / 86.89% / 70.86%`，最大回撤 `-24.30% / -17.71% / -10.64% / -11.23% / -9.53%`；`90/10 equal_weight` 为 `13.00% / 17.34% / 24.88% / 88.19% / 66.91%`；`90/10 total_mv` 为 `12.91% / 16.97% / 24.25% / 87.00% / 63.29%`。结论：2020/2023 回撤质量改善，但 2017 和 2023 CAGR 仍弱于 Path4 robust/当前 window winner，不替换 robust 或 tracked。
- `scripts/update_weighted_winners.py` 后 Path4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`；`since_2020_01` winner 仍为前序 `signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn`。持仓贡献继续按强行业/强龙头结构观察，不做半导体、AI 等人工主题归因。
- 为维持 active cap `60`，本轮 evict `aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70`；原因是旧 signal24/cap18 线已被 signal26-30、leader 与 coverage_penalty/lowturn 系列覆盖，且近期不改善 2020/2023 或 robust。
- 最终 rotation focus 为 `emergent_theme_coverage`。下一轮第一条命令建议在本轮 signal28/cap10 基础上继续拉宽覆盖而不是再降 cap：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn`；新增前继续先 evict 一条旧弱线。

## 本轮执行计划（2026-06-07 04:26 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。上一轮 `signal29/leader76/coverage_penalty/risk18/cap14/exit66_lowturn` 未改 robust，本轮按 `theme_signal_quality` 抬到 `signal30/leader78`，检查更高信号门槛是否牺牲中长窗。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认，实际补覆盖命令见 Path1 本轮记录。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `12.07% / 19.52% / 17.21% / 70.81% / 79.72%`，最大回撤 `-29.12% / -26.16% / -9.74% / -8.85% / -8.40%`；`90/10 equal_weight` 为 `10.52% / 18.87% / 19.92% / 75.71% / 79.04%`；`90/10 total_mv` 为 `10.80% / 17.46% / 17.83% / 75.82% / 77.63%`。结论：2020 有一定修复但 2017/2023 明显弱于既有 coverage/robust，且短窗换手最高到 `8.45x`，不能只凭 2025/2026 高 CAGR 晋级。
- `scripts/update_weighted_winners.py` 后 Path4 window winner 与 robust 未被本轮 signal30 替换；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。持仓仍来自多只强行业/强龙头，不做半导体、AI 等人工主题归因。
- 为维持 active cap `60`，本轮 evict `aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72`；原因是旧 signal24/risk30/cap18 已被 signal26-30、leader、coverage_penalty/lowturn 系列覆盖，且近期不改善 2020/2023 或 robust。
- 最终 rotation focus 为 `theme_capacity_cost`。下一轮第一条命令建议在 signal30 失败后降低门槛并直接测试容量/成本控制：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk16_cap10_exit64_lowturn`；新增前继续先 evict 一条旧弱线。

## 本轮执行计划（2026-06-06 16:17 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。上一轮 `signal29/leader76/coverage_penalty/risk15/cap12/exit64_lowturn` 切换 2020 window winner 但未改 robust，本轮按 `theme_signal_quality` 提高风险与容量阈值到 `risk18/cap14/exit66_lowturn`，观察更稳风险控制是否保持中窗。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认，A股实际合并命令见 Path1 本轮记录。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `12.47% / 16.73% / 24.20% / 87.70% / 64.42%`，最大回撤 `-26.63% / -24.53% / -10.42% / -11.26% / -8.40%`，换手 `2.83x / 3.39x / 3.46x / 5.92x / 6.44x`；`90/10 equal_weight` 为 `11.74% / 14.19% / 23.08% / 100.29% / 64.79%`；`90/10 total_mv` 为 `12.05% / 13.81% / 21.50% / 99.82% / 62.91%`。
- 结论：`80/20 total_mv` 的 2020 可比性尚可，但 2023 弱于既有 coverage_penalty winner，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`；不改 official robust/tracked。持仓贡献仍来自多只强行业/强龙头，不按半导体、AI 等人工主题归因，也不能只看单一短窗 CAGR 晋级。
- 为维持 active cap `60`，本轮 evict `aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72`；原因是旧 signal22/risk30/cap18 线已被 signal26-29、leader、coverage_penalty/lowturn 系列覆盖，且近期不改善 2020/2023 或 robust。
- 最终 rotation focus 为 `theme_signal_quality`。下一轮第一条命令建议继续检验信号质量但加更明确的 leader/coverage 修复，新增前先 evict 一条旧弱线：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-06 10:28 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。上一轮 signal28/leader74 没有改善 2020/2023，本轮按 `emergent_theme_coverage` 把 `signal29 + leader76 + coverage_penalty` 与 `lowturn` 合并，目标是观察更强信号是否能同时维持中窗和降低换手。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path1 本轮记录。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `11.98% / 16.76% / 24.18% / 84.31% / 60.19%`，最大回撤 `-22.89% / -19.85% / -10.14% / -11.26% / -8.93%`，换手 `2.81x / 3.42x / 3.39x / 5.90x / 6.49x`；`90/10 equal_weight` 为 `12.02% / 15.16% / 24.14% / 93.64% / 60.76%`；`90/10 total_mv` 为 `11.99% / 14.00% / 22.81% / 92.38% / 57.86%`。结论：`80/20 total_mv` 切换为 Path4 `since_2020_01` window winner，但 2023 弱于既有 coverage_penalty winner，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 持仓贡献仍来自多只强行业/强龙头，不按半导体、AI 等人工主题打标签；但 `signal29/leader76` 的 2023 退化说明不能只抬信号门槛。为维持 active cap `60`，本轮 evict `aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk30_cap20_exit72`，原因是旧 signal22/risk30/cap20 线已被 signal26-29、leader 与 coverage_penalty/lowturn 线覆盖，且近期不改善 2020/2023 或 robust。
- 最终 rotation focus 为 `emergent_theme_coverage`。下一轮第一条命令建议在本轮 winner 上做覆盖广度和风险阈值修复，新增前继续先 evict 一条旧弱线：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-06 04:23 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。上一轮 lowturn 线短窗可用但未改善 2020/2023，本轮回到 `theme_signal_quality`，测试 `signal28 + leader74 + coverage_penalty`。
- 本轮新增并五窗口确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64`。命令为：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader74_coverage_penalty_risk15_cap12_exit64`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `11.37% / 14.41% / 26.66% / 85.82% / 80.36%`，`90/10 equal_weight` 为 `10.96% / 13.77% / 25.28% / 91.29% / 84.61%`，`90/10 total_mv` 为 `11.25% / 13.91% / 24.28% / 93.79% / 78.59%`。最近持仓仍由源杰科技、鼎龙股份、华峰测控、天孚通信、中际旭创等多票贡献，不是单票幸运；但 2020/2023 弱于既有 `coverage_penalty_risk15_cap12_exit66`，不替换 Path4 winner/robust。
- 为维持 active cap `60`，本轮从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 Path2 scan evict `aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74`；原因是旧 signal22/risk35/cap20 线已被 signal26/28、leader72/74、coverage_penalty 与 lowturn 线覆盖，近期不改善 2020/2023 或 robust。
- 最终 rotation focus 为 `theme_signal_quality`。下一轮第一条命令建议继续做信号质量但加入低换手约束，而不是继续单纯抬 leader：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn`；新增前继续先 evict 一条旧弱线。

## 本轮执行计划（2026-06-05 22:21 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。`scripts/path2_candidate_pass.py` 中 `emergent_theme_discovery` family 维持 60 个可比候选。
- 本轮为维持 active cap `60`，从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 Path2 scan 中 evict `aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74`；原因是旧 signal20/risk35/cap20 线已被 signal26/27、leader72、coverage_penalty 与低 cap/lowturn 线覆盖，近期不改善 2020/2023 或 robust。
- 本轮新增并五窗口确认 3 个 Path4 lowturn 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn`。命令为：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `11.18% / 15.02% / 29.19% / 84.48% / 94.04%`，`90/10 equal_weight` 为 `11.24% / 12.85% / 28.47% / 89.31% / 83.48%`，`90/10 total_mv` 为 `11.44% / 13.15% / 27.23% / 91.45% / 78.59%`。换手最高仍到 `8.48x`，2020/2023 不如 `coverage_penalty_risk15_cap12_exit66`，不替换 Path4 window winner 或 robust candidate。
- 最终 rotation focus 为 `theme_capacity_cost`。下一轮第一条命令建议在 lowturn 基础上做容量成本约束，而不是继续只抬 signal 门槛；新增前仍需先 evict 一条旧弱线：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap10_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap10_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap10_exit64_lowturn`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-05 10:22 CST）

- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。`scripts/path2_candidate_pass.py` 中 `emergent_theme_discovery` family 维持 60 个可比候选。
- 本轮新增并五窗口确认 3 个 Path4 `coverage_penalty/risk12/cap10/exit64` 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64`。命令类型为五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path1 本轮记录。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `11.11% / 15.79% / 30.09% / 84.03% / 93.22%`，`90/10 equal_weight` 为 `12.00% / 14.75% / 28.96% / 85.67% / 80.77%`，`90/10 total_mv` 为 `12.28% / 14.91% / 28.34% / 88.02% / 75.28%`。2023/2025/2026 仍能捕捉源杰科技、鼎龙股份、华峰测控、杰瑞股份、中际旭创等多票强结构，不是单票幸运；但 2017/2020 收益低于 `risk15/cap12` 与早期 robust，且短窗换手最高到 `7.44x`。
- `scripts/update_weighted_winners.py` 后 Path4 window winner 与 robust 未被本轮 risk12/cap10 替换：2020 winner 仍是 `90/10 equal_weight coverage_penalty_risk15_cap12_exit66`，2023 winner 仍是 `80/20 total_mv coverage_penalty_risk15_cap12_exit66`，robust candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。结论：继续压 risk/cap 会牺牲长中窗，不应只凭短窗高 CAGR 晋级。
- 为维持 active cap `60`，本轮从 active/scan evict `aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76`；原因是旧 signal20/risk35/cap25 线已被 signal26/leader72/coverage_penalty 覆盖，且近期未改善 2020/2023 或 robust。最新 rotation focus 为 `theme_signal_quality`；下一轮第一条命令建议停止继续降 cap，改测信号质量和低换手的折中：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal27_leader72_coverage_penalty_risk15_cap12_exit64_lowturn`；新增前继续先 evict 一条同形旧弱线。

## 本轮执行计划（2026-06-05 04:11 CST）

- 最新 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；本轮继续只使用市场结构涌现信号，不使用人工主题标签、不纳入 ETF。`scripts/path2_candidate_pass.py` 中 `emergent_theme_discovery` family 已同步到 60 个可比候选。
- 本轮纳入并五窗口确认 3 个 Path4 coverage/capacity 候选：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap12_exit66`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap12_exit66`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap12_exit66`。命令类型为五窗口 `--only-base-ids` 增量确认。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `12.01% / 16.21% / 33.60% / 82.84% / 92.56%`，`90/10 equal_weight` 为 `11.53% / 16.46% / 32.82% / 87.14% / 79.50%`，`90/10 total_mv` 为 `12.07% / 15.63% / 31.67% / 86.39% / 73.82%`。最大回撤在 2017/2020 仍约 `-18.92%~-25.75%`，短窗换手最高约 `6.57x`。
- `scripts/update_weighted_winners.py` 后 Path4 `since_2020_01` winner 切到 `90/10 equal_weight coverage_penalty_risk15_cap12_exit66`，`since_2023_01` winner 切到 `80/20 total_mv coverage_penalty_risk15_cap12_exit66`；robust candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。结论是 coverage_penalty 能改善 2020/2023 局部排序，但还不能只凭短窗替换 robust。
- 本轮为维持 active cap，从 active/scan 归档 `aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78` 与 `aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`，原因是旧 signal20/risk40 线已被 signal26/leader72/coverage_penalty 覆盖且不改善 robust。
- 最新 rotation focus 为 `emergent_theme_coverage`。下一轮第一条命令建议继续测试覆盖广度与容量约束的组合，而不是继续单独提高 signal 门槛：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64`；新增前继续 evict 一条同形旧弱线。

## 本轮执行计划（2026-06-04 16:16 CST）

- 开局 guard 为 `pass`，`ashare_path4_emergent_theme` 为 `60/60 complete`，没有 blocking rerun command。本轮按 `theme_signal_quality` 新增并确认 signal28/leader72/risk15/cap12/exit64 三底座，不使用人工主题标签、不纳入 ETF。
- 本轮新增 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64`。实际命令见 Path1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `11.70% / 16.08% / 31.64% / 82.90% / 87.54%`，`90/10 equal_weight` 为 `12.13% / 15.91% / 31.17% / 94.79% / 76.10%`，`90/10 total_mv` 为 `12.71% / 15.26% / 29.95% / 93.05% / 73.49%`。最大回撤在 2020 窗口仍达 `-24.52% / -24.87% / -30.97%`，短窗换手最高到 `8.51x`；结论是 signal28 提高信号门槛后没有改善 2020 稳定性，不能只凭 2025/2026 晋级。
- `scripts/update_weighted_winners.py` 后 Path4 window winners 与 robust 未切换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。本轮新增前已从 active/scan 归档 `aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78` 的旧弱线，原因是 signal18/risk40 已被 signal26/28 与 leader/cap12 线覆盖且不改善 robust。
- 下一轮 focus 继续 `theme_signal_quality`，但不再单纯抬 signal 门槛。第一条命令建议改测“信号质量 + 低拥挤/低换手”组合：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap10_exit64,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap10_exit64,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap10_exit64`；新增前继续先 evict 一条同形旧弱线。

## 本轮执行计划（2026-06-04 10:16 CST）

- 开局 guard 为 `pass`，`ashare_path4_emergent_theme` 已 `60/60 complete`，本轮没有 blocking rerun command；预算优先给 A股 Path2/3 与 HK 四个新增候选。Path4 完成巡检：`scripts/path2_candidate_pass.py` 中 `emergent_theme_discovery` family 仍完整，`scripts/update_weighted_winners.py` 后 Path4 window winner/robust candidate 未被本轮同步改变。
- 已有 `coverage_penalty_risk20_cap12_exit68` 三底座结果显示覆盖惩罚能压部分回撤，但 2017/2020 仍不够；当前 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，不能只凭 2025/2026 短窗晋级。
- 本轮候选设计不使用人工主题标签：下一组应从 `signal26 + leader72 + coverage_penalty` 继续加容量/换手约束，而不是再降 risk 单参数。候选 id 设计为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap10_exit66`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap10_exit66`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap10_exit66`。
- 当前 active cap 为 `60`，下一轮新增前需先 evict 一条旧弱线，建议优先归档已被 signal26/leader/coverage 覆盖且不改善 robust 的旧 `signal20/risk40` 或 `risk35/cap25` 线，并在本文件记录原因。第一条命令为注册后增量确认：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap10_exit66,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap10_exit66,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap10_exit66`。

## 本轮执行计划（2026-06-03 22:20 CST）

- 开局 guard 报 `ashare_path4_emergent_theme` blocking，第一优先级按 rerun command 补齐三底座五窗口，没有改跑全量。新增并确认 3 个 Path4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66`。补缺口命令为：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `12.34% / 16.67% / 30.55% / 85.98% / 87.57%`，`90/10 equal_weight` 为 `13.46% / 15.56% / 31.99% / 101.10% / 82.47%`，`90/10 total_mv` 为 `14.03% / 14.68% / 29.08% / 97.79% / 73.37%`。最大回撤分别在 2020 窗口达到 `-23.94% / -25.17% / -29.36%`，短窗换手最高到 `8.49x`，不能只凭 2025/2026 晋级。
- 持仓抽样由源杰科技、鼎龙股份、天孚通信、华峰测控、杰瑞股份、中际旭创等多票贡献，不是单票幸运；但容量成本和 2020 稳定性仍是约束。`scripts/update_weighted_winners.py` 后 Path4 window winner 发生变化：2020 winner 切到 `80/20 total_mv risk15/cap12/exit66`，2025 winner 切到 `90/10 equal_weight risk15/cap12/exit66`；robust candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 候选池 active cap 维持 `60`：本轮从 active 与 scan 移出 `aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`，原因是旧 signal18/risk40/cap30 线已被 signal24/26、leader 与低 cap 线覆盖且不改善 robust。最终 guard 为 `pass`，Path4 因窗口 winner 变化重置为 `continue / emergent_theme_coverage`；第一条命令建议不要继续只降 risk，改做覆盖广度与拥挤惩罚的组合，例如注册下一组更分散的 signal26/leader 变体：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-06-02 16:20 CST）

- 开局 guard 为 `pass`；注册本轮 active 后 `ashare_path4_emergent_theme` 按预期变为 `3/60 missing`，已作为 blocking scope 第一优先级按 rerun command 补齐五窗口。上一轮 `leader68/risk20/cap16/exit68` 短窗强但 2020 弱，本轮按 `emergent_theme_coverage/theme_capacity_cost` 继续压单票 cap 到 `12`，不使用人工主题标签、不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68`。blocking 补齐命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `11.97% / 16.01% / 28.52% / 88.95% / 88.11%`，`90/10 equal_weight` 为 `12.06% / 15.99% / 29.75% / 104.90% / 88.29%`，`90/10 total_mv` 为 `12.34% / 14.13% / 26.66% / 100.31% / 61.70%`。cap12 降低了部分短窗单票风险，但 2017/2020 仍明显低于 Path 4 robust，且 2026 换手最高到 `9.42x`，不能只凭 2025/2026 晋级。
- 最近持仓由宏和科技、天孚通信、源杰科技、华峰测控、华海清科、杰瑞股份、中国海油、长飞光纤、赤峰黄金等多票贡献，不是单票幸运；主要问题仍是强行业拥挤、容量成本和 2020 稳定性。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 候选池 active cap 维持 `60`：本轮从 active `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与全局 scan 移出 `aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76`，原因是旧 prom8/cap30 风险线已被 signal24、leader68 与低 cap 线覆盖且不改善 robust；新增 `aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68`。最新 guard 为 `pass`，下一轮 focus 为 `emergent_theme_coverage`；第一条命令建议不要继续只压 cap，改做主题覆盖/拥挤惩罚双目标：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-06-02 13:49 CST）

- 开局 guard 为 `pass`；注册本轮 active 后 `ashare_path4_emergent_theme` 按预期变为 `3/60 missing`，已作为 blocking scope 第一优先级按 rerun command 补齐五窗口，没有改跑全量。上一轮 `leader68/risk25/cap16/exit70` 仍是短窗强、2020 弱；本轮按 `theme_risk_control` 把熊市保留降到 `risk20`、出场收紧到 `exit68`，继续不使用人工主题标签、不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `13.17% / 15.20% / 28.35% / 86.99% / 93.73%`，`90/10 equal_weight` 为 `12.39% / 15.82% / 28.82% / 105.53% / 88.03%`，`90/10 total_mv` 为 `12.78% / 13.93% / 26.84% / 101.88% / 61.56%`。最大回撤在 2017/2020 仍约 `-32%~-39%`，2020 稳定性低于 Path 4 robust；短窗换手最高到 `9.53x`，不能凭 2025/2026 晋级。
- 最近持仓抽样由源杰科技、天孚通信、国瓷材料、华峰测控、杰瑞股份、中国海油、融捷股份、赤峰黄金等多票贡献，不是单票幸运；但强行业拥挤、容量成本和 2020 回撤没有被 `risk20/exit68` 根治。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 候选池 active cap 维持 `60`：本轮从 active `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与全局 scan 移出 `aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76`，原因是旧 prom8/cap35 风险线已被 signal24、leader68 和低 cap 线覆盖且不改善 robust；新增 `aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68`。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；下一轮 focus 为 `theme_capacity_cost`，第一条命令建议不要继续降 risk，改加容量/拥挤惩罚或更低换手门槛：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`。

## 本轮执行计划（2026-06-02 04:20 CST）

- 开局 guard 为 `pass`；注册本轮 active 后 `ashare_path4_emergent_theme` 按预期变为 `3/60 missing`，已按 rerun command 第一优先级补齐五窗口，没有改跑全量。上一轮 `signal24/risk25/cap16/exit70` 仍是短窗强、2020 弱；本轮按开局 `theme_signal_quality` 增加 `leader68` 分散/龙头质量约束，最终 guard 下一轮 focus 轮换为 `theme_risk_control`。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70`。补齐命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `11.95% / 14.33% / 28.16% / 86.85% / 93.73%`，`90/10 equal_weight` 为 `11.55% / 14.09% / 28.33% / 106.90% / 88.03%`，`90/10 total_mv` 为 `11.96% / 11.78% / 26.46% / 102.56% / 61.56%`。leader68 稍压部分短窗回撤，但 2017/2020/2023 收益明显低于现有 Path 4 robust，不能只凭 2025/2026 晋级。
- 最近持仓由源杰科技、宏和科技、国瓷材料、杰瑞股份、长飞光纤等多票贡献，不是单票幸运；主要问题仍是强行业拥挤、2020 稳定性与短窗换手。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 候选池 active cap 维持 `60`：本轮从 active `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与全局 scan 移出 `aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78`，原因是旧高风险 prom8/cap35 已被 signal24/cap16 与 leader guard 线覆盖且不改善 robust；新增 `aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70`。下一轮第一条命令建议沿 `theme_risk_control` 做回撤/拥挤惩罚，而不是继续加 promotion 或 leader 门槛：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`。

## 本轮执行计划（2026-06-01 22:30 CST）

- 开局 guard 为 `pass`；注册本轮 active 后 `ashare_path4_emergent_theme` 按预期变为 `3/60 missing`，已作为 blocking scope 第一优先级按 rerun command 补齐五窗口。上一轮 `signal24/risk25/cap18/exit70` 仍是 2023/短窗强、2020 弱；本轮按 `emergent_theme_coverage` 把 promotion 提到 `13/87 prom12`，并把单票 cap 压到 `16`，继续不使用人工主题标签、不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `13.14% / 14.14% / 34.99% / 108.44% / 118.22%`，`90/10 equal_weight` 为 `12.53% / 15.65% / 36.02% / 128.96% / 112.62%`，`90/10 total_mv` 为 `13.09% / 13.99% / 33.40% / 126.12% / 82.84%`。2023 与 2025 仍有强主题弹性，但 2017/2020 明显低于当前 Path 4 robust，2026 换手最高到 `9.34x`，不能凭短窗晋级。
- 最近持仓由杰普特、宏和科技、鼎龙股份、国瓷材料、源杰科技、天孚通信、华峰测控、广钢气体、杰瑞股份、中国海油等多票贡献，不像单票幸运；主要问题仍是强行业拥挤、容量与短窗换手。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 候选池 active cap 维持 `60`：本轮从 active `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与全局 scan 移出 `aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50`，原因是旧 quality-gate 中段形态已被 signal24/risk25/cap16 线覆盖且不改善 robust；新增 `aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`。
- 最终 guard 把下一轮 focus 轮换为 `theme_signal_quality`。第一条命令建议不要继续只提高 promotion 或压 cap，改加信号质量、leader 分散或容量拥挤惩罚：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_signal_quality_crowding_ids>`。

## 本轮执行计划（2026-06-01 10:27 CST）

- 开局与收尾 guard 均为 `pass`，`ashare_path4_emergent_theme 60/60 complete`；上一轮 `signal24/risk30/cap18/exit72` 仍是短窗强、2020 弱。本轮按 `theme_capacity_cost/theme_risk_control` 在 signal24 线上进一步降熊市保留到 `risk25`，出场收紧到 `exit70`，继续不使用人工主题标签、不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70`、`core_explore_90_10_equal_weight_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70`、`core_explore_90_10_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70,core_explore_90_10_equal_weight_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70,core_explore_90_10_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `14.60% / 13.07% / 35.78% / 96.45% / 128.98%`，`90/10 equal_weight` 为 `14.14% / 13.66% / 37.54% / 117.22% / 115.95%`，`90/10 total_mv` 为 `14.29% / 11.18% / 35.09% / 113.67% / 89.34%`。2023 与短窗继续强，但 2020 仍低于当前 Path 4 robust；2026 换手最高到 `9.24x`，容量成本仍是主要约束。
- 最近持仓由杰普特、天孚通信、鼎龙股份、源杰科技、华峰测控、广钢气体、盛科通信-U、中国海油、藏格矿业等多票贡献，不像单票幸运；但强行业拥挤和换手成本没有被 `risk25/exit70` 根治。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 候选池 active cap 维持 `60`：本轮从 active `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与全局 scan 移出 `aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80`，原因是旧 `prom7/risk45/cap35` 高风险线已被 signal22/24 与低 cap 线覆盖且不改善 robust；新增 `aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap18_exit70`。下一轮 focus 仍为 `theme_capacity_cost`，第一条命令建议不要继续只降 risk，改加容量/拥挤惩罚或进一步压单票上限，例如三底座 `aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`。

## 本轮执行计划（2026-06-01 04:18 CST）

- 开局 guard 为 `pass`；注册本轮 active 后 `ashare_path4_emergent_theme` 按预期变为 `3/60 missing`，已作为第一优先级按 rerun command 补齐五窗口。上一轮 `signal22/risk30/cap18/exit72` 仍是短窗强、2020 弱；本轮按 `theme_signal_quality` 把信号门槛提高到 `signal24`，不使用人工主题标签、不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72`、`core_explore_90_10_equal_weight_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72`、`core_explore_90_10_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72`。实际补齐命令见 Path 1 本轮 blocking 批次。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `14.39% / 12.79% / 34.14% / 97.03% / 128.98%`，`90/10 equal_weight` 为 `14.24% / 13.57% / 36.17% / 117.66% / 115.95%`，`90/10 total_mv` 为 `14.45% / 11.18% / 33.35% / 114.10% / 89.34%`。最大回撤分别约为 `-24.42%~-27.67%`、`-28.26%~-28.02%`、`-27.28%~-27.95%` 的长中窗区间；2023/短窗仍强，但 2020 稳定性低于当前 Path 4 robust。
- 持仓抽样由宏和科技、杰普特、鼎龙股份、国瓷材料、杰瑞股份、大族数控、三环集团、睿创微纳、沃尔德、长飞光纤、广钢气体等多票贡献，不像单票幸运；主要风险仍是强行业拥挤、容量和 2026 `7.17x-9.24x` 换手。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 候选池 active cap 维持 `60`：本轮从 active `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与全局 scan 移出 `aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80`，原因是旧 prom6/cap35 风险线已被 signal22/24 与低 cap 线覆盖且不改善 robust；新增 `aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72`。下一轮 focus 为 `theme_risk_control`，第一条命令建议在 signal24 线上降风险或加拥挤/回撤惩罚，而不是继续提高信号阈值：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`。

## 本轮执行计划（2026-05-31 22:26 CST）

- 开局 guard 为 `pass`；注册本轮强主题 active 变体后，guard 按预期报 `ashare_path4_emergent_theme 3/60 missing`，本轮第一优先级按 rerun command 五窗口补齐，没有改跑全量。上一轮 `signal22/risk30/cap20/exit72` 仍是短窗强、2020 弱，本轮按 `emergent_theme_coverage/theme_capacity_cost` 把 promotion 提到 `12/88 prom11` 且 cap 继续压到 `18`，观察更宽覆盖能否保留短窗同时改善稳定性。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72`、`core_explore_90_10_equal_weight_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72`、`core_explore_90_10_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72`。补齐命令见 Path 1 本轮 blocking 批次。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `14.46% / 15.66% / 32.60% / 104.96% / 133.64%`，`90/10 equal_weight` 为 `14.20% / 16.81% / 33.72% / 119.18% / 102.87%`，`90/10 total_mv` 为 `14.08% / 14.69% / 32.14% / 122.03% / 96.08%`。2023/短窗仍强，且 80/20 total 的 2020 回撤收窄到 `-24.38%`，但 2017/2020 CAGR 明显低于当前 Path 4 robust。
- 持仓抽样继续由杰普特、天孚通信、鼎龙股份、源杰科技、中国海油、广钢气体、盛科通信等多票贡献，不像单票幸运；主要风险仍是强行业拥挤与短窗换手。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 候选池 active cap 保持 `60`：本轮从 active `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移出 `aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80`，原因是旧 prom6/cap40 已被 signal20/22 与更低 cap 线覆盖且不改善 robust；新增 `aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72`。下一轮 focus 已转到 `theme_signal_quality`；第一条命令建议不要继续只降 cap，改做信号质量或拥挤/换手惩罚：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_signal_quality_or_crowding_ids>`。

## 本轮执行计划（2026-05-31 16:20 CST）

- 开局 guard 为 `pass`，但注册本轮新变体后 `ashare_path4_emergent_theme` 变为 blocking；本轮按 rerun command 第一优先级补齐五窗口，没有改跑全量。上一轮 `signal22/risk35/cap20/exit74` 仍未改善 2020 稳定性，本轮按 `theme_risk_control` 把风险保留降到 `risk30`、exit 降到 `72`，并从 active discovery universe 与全局 Path2 scan 中移出 `aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82`，原因是旧 prom6/cap45 已被 signal22/cap20 线覆盖且不改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk30_cap20_exit72`、`core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk30_cap20_exit72`、`core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk30_cap20_exit72`。实际补齐命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk30_cap20_exit72,core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk30_cap20_exit72,core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk30_cap20_exit72`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `14.51% / 18.27% / 32.14% / 101.62% / 126.88%`，`90/10 equal_weight` 为 `14.75% / 18.07% / 33.31% / 117.80% / 96.36%`，`90/10 total_mv` 为 `14.41% / 15.43% / 31.77% / 118.03% / 89.00%`。2023 和短窗仍强，但 2017/2020 未超过现有 Path 4 robust，短窗换手最高仍到 `9.08x`，不能只凭短窗晋级。
- 最近持仓由杰普特、宏和科技、鼎龙股份/源杰科技、国瓷材料、杰瑞股份、睿创微纳、广钢气体、中国海油等多票贡献，不是单票幸运；主要风险仍是强行业拥挤、容量和换手成本。`scripts/path2_candidate_pass.py` 后 emergent theme family 保持完整，`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 最终 guard 为 `pass`，最后一次收尾 guard 将下一轮 focus 轮换为 `emergent_theme_coverage`。第一条命令建议不要继续单纯降 risk，改测覆盖边界与容量约束的折中，例如在 `signal22/risk30` 线上调整 `prom/cap` 或加入换手/拥挤惩罚：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-05-31 10:26 CST）

- 开局 guard 为 `pass`；上一轮 focus 为 `theme_signal_quality`，本轮在 `prom10/cap20/exit74` 上把强主题信号阈值提高到 `signal22`。新增前从 active discovery universe 与全局 Path2 scan 中移出 `aggr_07_93_prom6_emergent_theme_quality_gate_risk35_cap45_exit82`，原因是旧 prom6/cap45 已被 signal20/signal22 高门槛线覆盖且不改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74`、`core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74`、`core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `14.08% / 18.16% / 32.86% / 100.38% / 126.88%`，`90/10 equal_weight` 为 `14.37% / 17.79% / 34.03% / 117.04% / 96.36%`，`90/10 total_mv` 为 `13.99% / 15.11% / 32.24% / 116.47% / 89.00%`。2023 和短窗仍强，但 2017/2020 没有超过当前 Path 4 robust，2026 换手升到 `7.15x-9.08x`，不能只凭短窗晋级。
- 最近持仓由杰普特、宏和科技、天孚通信、国瓷材料/鼎龙股份、源杰科技、杰瑞股份、睿创微纳、广钢气体等多票贡献，并非单票幸运；但强行业/强龙头拥挤和容量成本仍是主风险。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60` 完整，下一轮 focus 轮换为 `theme_risk_control`。第一条命令建议在 signal22 线下降风险或增加回撤触发，而不是继续提高信号阈值：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`。

## 本轮执行计划（2026-05-31 04:21 CST）

- 开局 guard 为 `pass`；上一轮建议继续在 `signal20/prom10` 线上压容量和换手。本轮先按 guard 阻塞优先级补齐 Path 4 强主题涌现新增三底座，然后将 `aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82` 从 active discovery universe 和全局 Path2 scan 中移出，原因是旧 prom5/cap45 已被 signal18/signal20/prom10 线覆盖且未改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74`、`core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74`、`core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74,core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74,core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `15.46% / 14.87% / 34.60% / 91.21% / 128.04%`，`90/10 equal_weight` 为 `15.76% / 15.48% / 34.70% / 107.89% / 110.76%`，`90/10 total_mv` 为 `15.10% / 13.10% / 34.80% / 108.38% / 97.87%`。2023/短窗仍强，但 2020 CAGR 仅 `13.10%-15.48%` 且 2020 MaxDD 约 `-30.78%~-31.24%`，不能只凭短窗晋级。
- 最近持仓由宏和科技、鼎龙股份、源杰科技、天孚通信、国瓷材料、杰瑞股份、睿创微纳、广钢气体、沃尔德、长飞光纤、中国海油等多票贡献，不是单票幸运；但短窗换手升至 `7.68x-9.07x`，容量成本仍是主要风险。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 轮换为 `theme_signal_quality`。第一条命令建议在 cap20 上提高信号质量或 leader 过滤，而不是再单纯压 cap，例如三底座 `aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_signal_quality_ids>`。

## 本轮执行计划（2026-05-30 22:20 CST）

- 开局 guard 为 `pass`；上一轮建议在 `prom10/signal20` 上降风险和降退出。本轮按 `theme_risk_control` 新增 `risk35/cap25/exit76` 三底座，同时因 active cap 维持 `60`，从 active discovery universe 移出 `aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82`，原因是旧 prom4/cap45 已被 signal20/prom10 线覆盖且不改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76`、`core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76`、`core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `16.61% / 15.22% / 34.14% / 86.96% / 131.14%`，`90/10 equal_weight` 为 `17.60% / 15.95% / 34.65% / 100.92% / 118.82%`，`90/10 total_mv` 为 `16.82% / 13.62% / 34.64% / 100.94% / 99.16%`。2023/短窗仍强，但 2020 CAGR 只有 `13.62%-15.95%` 且 MaxDD 约 `-31%`，不满足稳定性要求。
- 最近持仓由宏和科技、鼎龙股份、源杰科技、天孚通信、国瓷材料、杰瑞股份、睿创微纳、华峰测控等多票贡献，不是单票幸运；但短窗换手升至 `7.74x-9.02x`，容量成本仍是主要风险。`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 轮换为 `theme_capacity_cost`。第一条命令建议继续在 signal20/prom10 线上压容量和换手，例如三底座 `aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap20_exit74`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`。

## 本轮执行计划（2026-05-30 16:22 CST）

- 开局 guard 为 `pass`；上一轮 `prom9/signal20/cap25` 仍未修复 2020 稳定性。本轮按 `emergent_theme_coverage/theme_signal_quality` 把覆盖提高到 `prom10`，保持 `signal20/risk40/cap25/exit78`，继续不使用人工主题标签、不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`、`core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`、`core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78,core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78,core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `16.57% / 15.43% / 35.97% / 86.08% / 131.14%`，`90/10 equal_weight` 为 `17.22% / 15.77% / 36.67% / 100.37% / 118.82%`，`90/10 total_mv` 为 `16.70% / 13.58% / 36.78% / 100.54% / 99.16%`。2023/短窗强，但 2020 回撤仍约 `-33.70%~-34.18%`，短窗换手最高到 `9.02x`，不晋级。
- 最近持仓复查显示 `90/10 total_mv` 并非单票幸运，前排由宏和科技、鼎龙股份、国瓷材料、大族数控、杰瑞股份、睿创微纳、沃尔德、长飞光纤、广钢气体等多票贡献，但前 3 权重约 `31.88%`，仍需关注主题拥挤和容量成本。新增前从 active discovery universe 移出 `aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82`，原因是旧 quality-gate 中段形态被 signal20/prom10 线覆盖且不改善 robust。
- `scripts/path2_candidate_pass.py` 与 `scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`；本阶段不改 official 展示。最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 轮换为 `theme_risk_control`。第一条命令建议在 prom10/signal20 上降风险或降退出，例如三底座 `aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`。

## 本轮执行计划（2026-05-30 10:17 CST）

- 开局 guard 为 `pass`；上一轮 `signal20/risk40/cap28` 改善 2023/短窗但 2020 回撤仍深。本轮按 `theme_capacity_cost` 继续把单票上限从 `cap28` 压到 `cap25`，保持 `prom9/signal20/risk40/exit78`，仍不使用人工主题标签、不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`、`core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`、`core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78,core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78,core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `17.44% / 17.34% / 37.12% / 95.38% / 117.84%`，`90/10 equal_weight` 为 `19.96% / 16.67% / 36.89% / 111.39% / 104.43%`，`90/10 total_mv` 为 `19.20% / 14.80% / 37.47% / 110.48% / 87.18%`。最大回撤在 2020 仍约 `-35.86%~-36.50%`，短窗换手升到 `7.68x~8.99x`；cap25 没有改善 2020 稳定性，不晋级。
- 新增前从 active discovery universe 移出 `aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65`，原因是旧 prom3/cap65 已被 signal18/signal20 质量门槛线覆盖，且不改善 robust。`scripts/path2_candidate_pass.py` 后 emergent theme family 完整，`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`；本阶段不改 official 展示。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 轮换为 `emergent_theme_coverage`。第一条命令建议不要再单纯压 cap，改测 `prom10/signal20/cap25` 覆盖边界并继续 evict 一个弱旧 quality-gate active，例如三底座 `aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-05-30 04:31 CST）

- 开局 guard 为 `pass`；上一轮 `prom10/signal18/cap30` 没有改善 robust，本轮按 `theme_signal_quality` 回到 `prom9`，把信号阈值提高到 `signal20`、单票上限压到 `cap28`。新增前从 active discovery universe 移出 `aggr_08_92_prom6_emergent_theme_risk50_cap50`，原因是旧高风险 first-batch 形态已被后续 quality-gate/signal 线覆盖，且不改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78`、`core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78`、`core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78,core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78,core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `17.81% / 17.42% / 36.73% / 93.42% / 119.25%`，`90/10 equal_weight` 为 `20.62% / 16.64% / 36.28% / 107.58% / 109.02%`，`90/10 total_mv` 为 `19.71% / 14.86% / 37.11% / 106.61% / 88.53%`。最大回撤在 2020 仍约 `-35.86%~-36.50%`，换手在短窗升到 `7.71x~8.96x`；该组改善 2023/短窗强度，但 2020 稳定性低于 `signal18` winner，不晋级。
- `scripts/path2_candidate_pass.py` 后 emergent theme family 完整，`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`；不改 official winner。最终 guard `ashare_path4_emergent_theme 60/60 complete`，本轮 evict/归档：`aggr_08_92_prom6_emergent_theme_risk50_cap50`。
- 下一轮 focus 为 `theme_capacity_cost`。第一条命令建议保留 `signal18/signal20` 质量门槛但继续压单票容量上限，例如注册三底座 `aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`。

## 本轮执行计划（2026-05-29 22:21 CST）

- 开局 guard 为 `pass`；上一轮 `aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78` 把 2020 等权提升到 `19.83%`，但尚未形成 robust 替换。本轮按 `emergent_theme_coverage/theme_signal_quality` 继续提高 prom 到 10，并把旧 `aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap45` 从 active Path 4 池移出，原因是相对新 signal18/cap30 线收益与风险均弱，避免候选池只增不减。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`、`core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`、`core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78,core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78,core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `18.55% / 18.47% / 30.36% / 86.34% / 112.83%`，`90/10 equal_weight` 为 `19.01% / 19.69% / 33.36% / 101.71% / 112.35%`，`90/10 total_mv` 为 `18.35% / 17.56% / 30.73% / 97.96% / 84.28%`。最大回撤长中窗约 `-24%~-30%`，换手约 `3.0x~9.0x`；等权版短窗较强，但 2020 仍低于上一轮 signal18 prom9 等权 winner。
- `scripts/path2_candidate_pass.py` 后 emergent theme family 完整，`scripts/update_weighted_winners.py` 后 Path 4 window winner/robust 未变，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`；不改 official winner。最终 guard `ashare_path4_emergent_theme 60/60 complete`，本轮 evict/归档：`aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap45`。
- 下一轮 focus 为 `theme_signal_quality`。第一条命令建议从 `prom9/signal18` 而不是 prom10 继续，测试更严格质量/行业 leader 约束或更低 cap，例如注册三底座 `aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap28_exit78`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_signal_quality_ids>`。

## 本轮执行计划（2026-05-29 16:33 CST）

- 开局 guard 对 `ashare_path4_emergent_theme` 报 blocking 缺口；先按 blocking scope 补齐，但原始命令默认目标日 `2026-05-29` 命中本地 A股缓存未覆盖，改用 `AIINVESTOR_FORCE_OFFLINE=1 --end-date 2026-05-28` 完成五窗口补齐。上一轮 `risk40_cap30_exit78` 已把 2023 winner 推到 prom9/cap30 线，本轮按 `theme_signal_quality` 在同一 prom9 框架上提高信号质量阈值到 `signal18`。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`、`core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`、`core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78,core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78,core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`。
- 三底座五窗口 CAGR：`80/20 total_mv` 为 `18.56% / 15.84% / 32.98% / 86.66% / 120.44%`，`90/10 equal_weight` 为 `19.53% / 19.83% / 33.46% / 103.73% / 117.58%`，`90/10 total_mv` 为 `19.17% / 17.47% / 31.28% / 100.87% / 90.55%`。最大回撤在 2020 仍约 `-32.91%~-36.30%`，但等权版把 `since_2020_01` Path 4 window winner 推到 `19.83% CAGR`，短窗继续强。
- 持仓由宏和科技、鼎龙股份、国瓷材料、杰瑞股份、睿创微纳、沃尔德、长飞光纤、广钢气体、三环集团、亚钾国际、德业股份等多票贡献，不是单票幸运；但 robust 仍由旧 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50` 保持。`scripts/update_weighted_winners.py` 后 Path 4 的 `since_2020_01` window winner 变为 `core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`，新增 public strategy detail，暂不改写独立 official 展示口径。
- 本轮 evict/归档：`aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45`，原因是旧 prom6 quality-gate 已被 prom9/cap30/signal18 线覆盖且不改善 robust。最终 guard `ashare_path4_emergent_theme 60/60 complete`，因 `since_2020_01` window winner 改善，下一轮 focus 重置为 `emergent_theme_coverage`；第一条命令建议继续验证 signal18 的覆盖边界，例如三底座 `aggr_11_89_prom10_emergent_theme_quality_gate_signal18_risk40_cap30_exit78` 或 `aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap25_exit78`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-05-29 10:22 CST）

- 开局 guard 为 `pass`；上一轮 prom9/risk35/cap30/exit76 继续短窗强但 2020 回撤深，本轮按 `theme_signal_quality` 提高熊市保留到 `risk40`、退出放宽到 `exit78`，继续不使用人工主题标签、不纳入 ETF。新增前从 active discovery universe 移出 `aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50`，原因是旧 prom6 quality-gate 已被后续 prom8-prom9/cap30 线覆盖，且未改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78`、`core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78`、`core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78,core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78,core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78`。
- 新组三底座五窗口 CAGR：`80/20 total_mv` 为 `18.72% / 14.88% / 35.58% / 81.86% / 115.40%`，`90/10 equal_weight` 为 `20.16% / 14.42% / 35.48% / 89.20% / 117.95%`，`90/10 total_mv` 为 `19.94% / 13.09% / 34.15% / 92.87% / 92.82%`。2023/2025/2026 明显强，但 2020 CAGR 仅 `13%-15%` 且最大回撤仍约 `-34%~-36%`，不能只凭短窗晋级。
- 持仓由宏和科技、鼎龙股份、天孚通信、源杰科技、国瓷材料、杰瑞股份、睿创微纳、广钢气体、盛科通信-U、天赐材料等多票贡献，不是单票幸运。`scripts/update_weighted_winners.py` 后 Path 4 的 `since_2023_01` window winner 改为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78`；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，暂不改写独立 official 展示口径。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=60`。下一轮 focus 为 `emergent_theme_coverage`；第一条命令建议新增前继续 evict 弱旧 quality-gate active，并测试 prom10 或 cap25 的覆盖/容量对照，例如三底座 `aggr_11_89_prom10_emergent_theme_quality_gate_risk40_cap30_exit78` 或 `aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap25_exit78`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-05-29 04:17 CST）

- 开局 guard 为 `pass`；上一轮 `prom8/risk35/cap30/exit76` 组短窗继续强但 2020 回撤仍深，本轮按 `emergent_theme_coverage` 扩到 `prom9`，继续不使用人工主题标签、不纳入 ETF。新增前从 active discovery universe 移出 `aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40`，原因是旧 prom6/cap40 已被后续 prom8-prom9/cap30 线覆盖，且不改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76`、`core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76`、`core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76,core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76,core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76`。
- 新 prom9/cap30 组三底座五窗口 CAGR：`80/20 total_mv` 为 `17.83% / 15.56% / 29.01% / 73.19% / 96.35%`，`90/10 equal_weight` 为 `20.84% / 16.10% / 30.35% / 81.78% / 90.30%`，`90/10 total_mv` 为 `20.10% / 13.80% / 28.77% / 82.70% / 77.57%`。2025/2026 仍强，2020 最大回撤仍约 `-32%`，长窗稳定性低于现有 Path 4 robust。
- 持仓由鼎龙股份、杰普特、华峰测控、源杰科技、宏和科技、广钢气体、睿创微纳、盛科通信-U、天赐材料等多票贡献，不是单票幸运；但不能只凭短窗 CAGR 晋级。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=59`，`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 为 `theme_signal_quality`。第一条命令建议新增前继续 evict 一个弱旧 quality-gate active，并在 prom9/cap30 上提高信号质量或更严风险过滤，例如三底座 `aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_signal_quality_ids>`。

## 本轮执行计划（2026-05-28 22:19 CST）

- 开局 guard 为 `pass`；上一轮 `risk35/cap35/exit76` 短窗强但 2020 回撤仍深，本轮按 `theme_capacity_cost` 把单票上限继续收紧到 `cap30`，仍不使用人工主题标签、不纳入 ETF。新增前从 active discovery universe 移出 `aggr_05_95_prom3_emergent_theme_risk40_cap70`，原因是第一批旧 cap70 已被后续 quality-gate/prom7-prom8 线覆盖，且不改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76`、`core_explore_90_10_equal_weight_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76`、`core_explore_90_10_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76,core_explore_90_10_equal_weight_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76,core_explore_90_10_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76`。
- 新 cap30 组三底座五窗口 CAGR：`80/20 total_mv` 为 `18.32% / 18.68% / 29.69% / 73.12% / 95.66%`，`90/10 equal_weight` 为 `19.95% / 18.18% / 30.75% / 82.14% / 86.04%`，`90/10 total_mv` 为 `19.26% / 16.32% / 29.72% / 84.08% / 73.99%`。最大回撤在 2020 窗口仍约 `-33%`，换手在 2026 窗口升到 `7.77x / 8.96x / 8.78x`，长窗稳定性仍低于现有 Path 4 robust。
- 持仓由鼎龙股份、国瓷材料、杰瑞股份、宏和科技、广钢气体、长飞光纤、睿创微纳等多票贡献，不是单票幸运；但不能只凭 2025/2026 强短窗晋级。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=59`，`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 为 `emergent_theme_coverage`。第一条命令建议新增前继续 evict 一个弱旧 quality-gate active，并测试更高覆盖但保留 cap30 的 prom9 对照，例如三底座 `aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-05-28 16:18 CST）

- 开局 guard 为 `pass`；上一轮 prom8 `risk40/cap35/exit78` 短窗强但 2020 回撤仍深，本轮按 `theme_risk_control` 继续收紧到 `risk35/cap35/exit76`，仍不使用人工主题标签、不纳入 ETF。新增前从 active discovery universe 移出 `aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70`，原因是旧 prom3/cap70 已被后续 prom4-prom8 quality-gate 线覆盖，且不改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76`、`core_explore_90_10_equal_weight_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76`、`core_explore_90_10_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76,core_explore_90_10_equal_weight_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76,core_explore_90_10_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76`。
- 新 prom8 风险收紧组三底座五窗口 CAGR：`80/20 total_mv` 为 `18.89% / 18.60% / 29.53% / 69.95% / 96.42%`，`90/10 equal_weight` 为 `20.66% / 18.06% / 30.42% / 76.72% / 91.71%`，`90/10 total_mv` 为 `19.98% / 16.27% / 29.41% / 78.91% / 76.18%`。最大回撤大致仍在 2020 窗口 `-33%` 左右，长窗稳定性低于现有 Path 4 robust。
- 持仓由鼎龙股份、国瓷材料、杰瑞股份、宏和科技、广钢气体、长飞光纤、睿创微纳等多票贡献，不是单票幸运；但不能只凭 2025/2026 短窗强势晋级。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=59`，`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 为 `theme_capacity_cost`。第一条命令建议新增前继续 evict 一个弱旧 quality-gate active，并测试更低单票上限/容量成本版本，例如三底座 `aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78` 2025/2026 强但 2020 回撤仍深，本轮按 `emergent_theme_coverage/theme_signal_quality` 扩到 `prom8`，继续不使用人工主题标签、不纳入 ETF。新增前从 active discovery universe 移出 `aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65`，原因是旧 prom3/cap65 组已被后续 prom4-prom8 quality-gate 线覆盖，且未改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78`、`core_explore_90_10_equal_weight_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78`、`core_explore_90_10_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 新 prom8 组五窗口表现：`80/20 total_mv` CAGR `18.59% / 17.06% / 29.84% / 69.91% / 96.42%`，最大回撤 `-30.05% / -35.72% / -24.90% / -14.68% / -7.33%`，换手 `3.25x / 3.93x / 3.79x / 6.10x / 7.82x`；`90/10 equal_weight` CAGR `20.08% / 16.74% / 29.33% / 76.68% / 91.71%`；`90/10 total_mv` CAGR `19.36% / 14.88% / 28.49% / 79.38% / 76.18%`。
- 持仓由鼎龙股份、国瓷材料、杰瑞股份、宏和科技、广钢气体、长飞光纤、睿创微纳等多票贡献，不是单票幸运；但 `since_2020_01` 回撤仍约 `-35%`，2017/2020 稳定性低于现有 Path 4 robust，不能只凭短窗强势晋级。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=60`，`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 为 `theme_risk_control`。第一条命令建议新增前继续 evict 一个弱旧 quality-gate active，并测试更严格风险控制/更低退出阈值的 prom8 对照，例如三底座 `aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；上一轮 `aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80` 仍有较深 2020 回撤，本轮按 `theme_risk_control` 收紧到 `risk40/exit78`。新增前从 active discovery universe 移出 `aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60`，原因是旧 prom3/cap60 组已被后续 prom4-prom7 quality-gate 线覆盖，且未改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78`、`core_explore_90_10_total_mv_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78`。实际 A股合并命令见 Path 1 本轮记录。
- 新组五窗口表现：`80/20 total_mv` CAGR `18.73% / 15.74% / 33.02% / 82.60% / 103.01%`，最大回撤 `-29.87% / -37.14% / -25.10% / -14.27% / -7.33%`；`90/10 equal_weight` CAGR `19.69% / 19.23% / 32.53% / 89.43% / 97.88%`；`90/10 total_mv` CAGR `19.14% / 18.28% / 31.35% / 90.84% / 82.29%`。
- 持仓由鼎龙股份、国瓷材料、杰瑞股份、宏和科技、广钢气体、睿创微纳等多票贡献，不是单票幸运；但 2020 回撤仍在 `-35.24%` 到 `-37.14%`，且 2017/2020 收益低于现有 Path 4 robust，不能只凭 2025/2026 短窗晋级。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=60`，`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 为 `emergent_theme_coverage`。第一条命令建议新增前继续 evict 一个弱旧 quality-gate active，并测试更高覆盖的 prom8 版本，例如三底座 `aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`；上一轮 `aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80` 能捕捉多票强主题但 2020 回撤仍深，本轮新增前从 active discovery universe 移出 `aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45`，原因是旧 prom2/cap45 组 2020 稳定性弱且未改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80`、`core_explore_90_10_total_mv_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80`。实际 blocking 补齐命令见 Path 1 本轮合并命令。
- 新 prom7 组五窗口表现：`80/20 total_mv` CAGR `18.52% / 15.22% / 34.30% / 82.60% / 103.01%`，最大回撤 `-30.87% / -39.65% / -26.65% / -14.27% / -7.33%`；`90/10 equal_weight` CAGR `19.23% / 18.86% / 32.84% / 89.41% / 97.88%`；`90/10 total_mv` CAGR `18.72% / 17.91% / 32.22% / 90.82% / 82.29%`。
- 持仓仍由鼎龙股份、国瓷材料、杰瑞股份、宏和科技、长飞光纤、睿创微纳等多票贡献，不是单票幸运；但 2020 回撤在 `-37.80%` 到 `-39.65%`，2020 稳定性仍弱于现有 robust，不能只凭 2025/2026 短窗晋级。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=60`，`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 已轮换为 `theme_risk_control`。第一条命令建议新增前继续 evict 一个弱 prom2 active，并在本轮 prom7 强主题框架上收紧风险/退出，例如三底座 `aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮要求优先执行三底座 `aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80`，本轮已注册并按 guard blocking `--only-base-ids` 五窗口补齐，继续不使用人工主题标签、不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80`、`core_explore_90_10_equal_weight_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80`、`core_explore_90_10_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80`。实际 blocking 命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80,core_explore_90_10_equal_weight_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80,core_explore_90_10_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80`。
- `80/20 total_mv` 五窗口 CAGR 为 `19.47% / 14.73% / 34.87% / 93.12% / 101.00%`，最大回撤 `-34.06% / -40.43% / -26.31% / -16.70% / -5.70%`，换手 `3.50x / 4.02x / 3.67x / 6.00x / 7.26x`；`90/10 equal_weight` 为 `20.66% / 16.52% / 34.20% / 123.63% / 101.99%`；`90/10 total_mv` 为 `20.14% / 16.19% / 31.95% / 117.92% / 87.62%`。新组能捕捉鼎龙股份、国瓷材料、杰瑞股份、宏和科技、长飞光纤、睿创微纳等多票强主题，不是单票幸运；但 2020 回撤仍深，不能只按 2025/2026 短窗晋级。
- 因 Path 4 active cap 维持 `60`，本轮从 active discovery universe 移出 `aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50`，原因是旧 prom2/cap50 组 2020 稳定性弱且未改善 robust。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=58`；`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- 最终 guard 为 `pass`，`ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 转为 `emergent_theme_coverage`。第一条命令建议新增前继续 evict 一个弱 prom2 active，并测试更高覆盖但仍压 cap 的三底座版本，例如 `aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮要求优先执行三底座 `aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80`，本轮已注册并按 guard blocking `--only-base-ids` 五窗口补齐，继续不使用人工主题标签、不纳入 ETF。实际补缺口命令见 Path 1 本轮 blocking 批次。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80`、`core_explore_90_10_equal_weight_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80`、`core_explore_90_10_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80`。
- `80/20 total_mv` 五窗口 CAGR 为 `19.76% / 14.78% / 34.66% / 92.14% / 102.80%`，最大回撤 `-34.06% / -40.43% / -26.47% / -16.70% / -4.46%`，换手 `3.52x / 4.03x / 3.66x / 6.00x / 7.22x`；`90/10 equal_weight` 为 `21.12% / 16.31% / 33.93% / 120.64% / 109.83%`；`90/10 total_mv` 为 `20.61% / 16.24% / 31.80% / 115.42% / 90.99%`。新组能捕捉鼎龙股份、源杰科技、国瓷材料、杰瑞股份、宏和科技、长飞光纤、睿创微纳等多票强主题，不是单票幸运；但 2020 回撤仍深，不能只按 2025/2026 短窗晋级。
- 因 Path 4 active cap 维持 `60`，本轮从 active discovery universe 移出 `aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60`，原因是旧 prom2/cap60 组长窗与 2020 稳定性弱于后续 prom4-prom7 quality-gate 线，且未改善 robust。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=58`；`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，四窗口 meanCAGR `44.46%`、minCAGR `21.78%`、worstMaxDD `-33.79%`、meanTurn `4.24x`，official/tracked 未改。
- 最终 guard 为 `ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 转为 `theme_capacity_cost`。第一条命令建议继续压单票/容量上限，并在新增前再 evict 一个弱 prom2 active，例如三底座 `aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap35_exit80`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；上一轮要求优先执行 `theme_signal_quality` 的 `risk40/cap45/exit82`，本轮在三底座注册 `aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82`。注册后 guard 如预期出现 Path 4 blocking 缺口，已按 `--only-base-ids` 五窗口增量补齐，命令见 Path 1 blocking 批次。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82`、`core_explore_90_10_equal_weight_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82`、`core_explore_90_10_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82`。
- `80/20 total_mv` 五窗口 CAGR 为 `20.22% / 15.08% / 34.11% / 91.27% / 104.61%`，最大回撤 `-33.06% / -39.08% / -24.92% / -16.70% / -3.21%`，换手 `3.47x / 3.96x / 3.57x / 6.00x / 7.18x`；`90/10 equal_weight` 为 `21.94% / 16.78% / 34.25% / 117.66% / 117.55%`；`90/10 total_mv` 为 `21.19% / 16.92% / 31.90% / 112.91% / 93.85%`。该组仍能捕捉鼎龙股份、源杰科技、国瓷材料、杰瑞股份、长飞光纤、睿创微纳等多票强主题，不是单票幸运；但 2020 回撤加深，不能只按 2025/2026 短窗晋级。
- 因 Path 4 active cap 维持 `60`，本轮从 active discovery universe 移出 `aggr_02_98_prom2_emergent_theme_risk40_cap90`，原因是旧第一批 cap90 形态集中度/稳定性弱于新的 quality-gate 线且未改善 robust。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=59`，`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。最终 guard 为 `ashare_path4_emergent_theme 60/60 complete`，下一轮 focus 仍为 `theme_signal_quality`；第一条命令建议继续提高信号质量但压集中度，例如三底座 `aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_signal_quality_ids>`。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮 `prom5 + risk35 + cap45 + exit82` 短窗强但 2020/2023 稳定性不足，本轮按 `emergent_theme_coverage` 扩到 `prom6` 覆盖形态，仍不引入人工主题标签或 ETF。命令类型为五窗口 `--only-base-ids` 增量确认，实际 A股合并命令见 Path 1 本轮记录。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk35_cap45_exit82`、`core_explore_90_10_equal_weight_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk35_cap45_exit82`、`core_explore_90_10_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk35_cap45_exit82`。
- `80/20 total_mv` 五窗口 CAGR 为 `20.78% / 15.97% / 32.57% / 91.27% / 104.61%`，最大回撤 `-30.60% / -35.87% / -23.14% / -16.70% / -3.21%`，换手 `3.41x / 3.89x / 3.47x / 6.00x / 7.18x`；`90/10 equal_weight` 为 `22.41% / 17.38% / 34.86% / 117.66% / 117.55%`；`90/10 total_mv` 为 `21.69% / 17.52% / 32.43% / 112.91% / 93.85%`。该组继续捕捉鼎龙股份、国瓷材料、杰瑞股份、宏和科技、长飞光纤、睿创微纳等多票强主题，但 2020 回撤和 2025/2026 换手仍偏高。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=59`，family 前列仍由 `aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82` 等旧 prom4 质量门槛形态占优；`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，本轮不改 official/tracked。
- 因 active cap 维持 `60`，本轮从 active discovery universe 移出 `aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45`，原因是旧 prom2/cap45 组未改善 robust 且 2020 稳定性不足。最终 focus 转为 `theme_signal_quality`；下一轮第一条命令建议在 prom6 覆盖形态上提高风险/信号质量要求，例如三底座 `aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_signal_quality_ids>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮 `prom4 + cap40 + exit82` 短窗很强但 2020/2023 稳定性仍不足，本轮按 `emergent_theme_coverage` 扩到 `prom5` 覆盖形态。新增前因 active cap 已到 `60`，从 active discovery universe 移出 `aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55`，原因是旧 prom2/cap55 组未改善 robust、2020 稳定性不足，且会挤压新的 prom5 覆盖实验。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82`、`core_explore_90_10_equal_weight_winner_core__aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82`、`core_explore_90_10_total_mv_winner_core__aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82`。实际 blocking 补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82,core_explore_90_10_equal_weight_winner_core__aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82,core_explore_90_10_total_mv_winner_core__aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82`。
- `80/20 total_mv` 五窗口 CAGR 为 `22.13% / 20.55% / 29.78% / 93.49% / 97.88%`，最大回撤 `-32.74% / -36.02% / -25.31% / -16.61% / -3.21%`，换手 `3.49x / 3.92x / 3.72x / 6.18x / 7.32x`；`90/10 equal_weight` 为 `22.35% / 17.00% / 32.18% / 123.21% / 69.69%`；`90/10 total_mv` 为 `22.00% / 18.33% / 29.35% / 118.38% / 48.80%`。
- 新组继续捕捉源杰科技、腾景科技、鼎龙股份、杰瑞股份、睿创微纳等多票强主题，非单票幸运；但 2020/2023 回撤仍深，不能只按 2025/2026 短窗 CAGR 晋级。`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=59`，最终 guard 为 `ashare_path4_emergent_theme 60/60 complete`。下一轮 focus 转为 `theme_risk_control`；新增前需继续 evict 一个弱 active，第一条命令建议在 `prom5` 覆盖形态上做更严格风险控制，例如三底座 `aggr_06_94_prom5_emergent_theme_quality_gate_risk40_cap45_exit82`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮 `prom4 + cap45 + exit82` 保留短窗弹性但 2020/2023 回撤仍深，本轮按 `theme_capacity_cost` 把同一 `prom4` 覆盖形态 cap 继续压到 `40`。新增前因 active cap 已到 `60`，从 active discovery universe 移出 `aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45`，原因是旧 prom2/cap45 组未改善 robust、2020 稳定性不足，且会挤压新的 prom4 容量实验。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82`、`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82`、`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82`。实际 blocking 补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82`。
- `80/20 total_mv` 五窗口 CAGR 为 `22.10% / 28.99% / 29.89% / 111.45% / 99.97%`，最大回撤 `-29.52% / -35.40% / -28.57% / -15.42% / -4.46%`，换手 `3.65x / 3.80x / 3.91x / 6.50x / 7.62x`；`90/10 equal_weight` 为 `24.72% / 25.23% / 31.88% / 138.53% / 59.42%`；`90/10 total_mv` 为 `23.97% / 25.85% / 29.48% / 135.67% / 43.12%`。
- 新组继续捕捉鼎龙股份、源杰科技、杰瑞股份、睿创微纳等强势票，2025/2026 仍强，但 2020/2023 稳定性和少票集中风险没有根本解决；不能只按短窗 CAGR 晋级。`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，official/tracked 未改。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=59`，最终 guard 为 `ashare_path4_emergent_theme 60/60 complete`。下一轮 focus 转为 `emergent_theme_coverage`；新增前需继续 evict 一个弱 active，第一条命令建议测试新的覆盖形态而不是继续只压 cap，例如三底座 `aggr_06_94_prom5_emergent_theme_quality_gate_risk35_cap45_exit82`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_emergent_theme_coverage_ids>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `prom4 + risk35 + cap50` 改善 2020 稳定性但 2020/2023 回撤仍深；本轮按 `theme_signal_quality` 在同一 `prom4` 覆盖形态上加入 `cap45 + exit82`。新增前因 active cap 已到 `60`，从 active discovery universe 移出 `aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40`，原因是旧 cap40 组未改善 robust 且 2020 稳定性不足。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82`、`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82`、`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82`。实际补缺口命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `80/20 total_mv` 五窗口 CAGR 为 `22.26% / 28.97% / 30.05% / 110.49% / 101.75%`，最大回撤 `-29.52% / -35.17% / -28.43% / -15.42% / -3.21%`，换手 `3.67x / 3.81x / 3.91x / 6.50x / 7.58x`；`90/10 equal_weight` 为 `25.10% / 25.08% / 31.96% / 135.32% / 61.13%`；`90/10 total_mv` 为 `24.19% / 25.98% / 29.57% / 132.95% / 41.53%`。
- 新组保持 2025 强弹性，但 2020/2023 回撤和少数强票集中风险仍未解决；不能只因短窗 CAGR 晋级。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=58`，`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 最终 guard 为 `ashare_path4_emergent_theme 60/60 complete`，focus 转为 `theme_capacity_cost`。下一轮新增前需继续 evict 一个弱 active；第一条命令建议在本组上先压容量/成本边界，例如三底座 `aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap40_exit82`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`，上一轮建议扩 `prom4` 覆盖形态；本轮新增前因 active cap 已到 `60`，从 active discovery universe 移出 `aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40`，原因是上一轮三底座 2020 稳定性不足、未改善 robust，且继续占用 cap 会挤压新 `prom4` 覆盖实验。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50`、`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50`、`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50`。覆盖命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50`。
- `80/20 total_mv` 五窗口 CAGR 为 `22.42% / 28.94% / 29.97% / 109.30% / 104.58%`，最大回撤 `-29.52% / -34.94% / -28.73% / -15.42% / -1.95%`，换手 `3.69x / 3.82x / 3.89x / 6.51x / 7.54x`；`90/10 equal_weight` 为 `25.36% / 25.05% / 31.97% / 132.11% / 62.73%`；`90/10 total_mv` 为 `24.51% / 26.07% / 29.65% / 130.22% / 39.95%`。
- 新组比上一轮 `cap40` 明显改善 2020 稳定性，并继续捕捉鼎龙股份、源杰科技、杰瑞股份、睿创微纳等强势票，但 2020/2023 回撤仍深、2025/2026 换手偏高，不能只按短窗 CAGR 晋级。`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，未改 official/tracked。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=58`，最终 guard 为 `ashare_path4_emergent_theme 60/60 complete`。下一轮 focus 为 `theme_signal_quality`；第一条命令建议在 `prom4` 覆盖形态上改信号质量和退出，而不是继续只调 cap，例如三底座 `aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_signal_quality_ids>`。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass`，上一轮 `aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45` 短窗很强但 2020 稳定性不足；本轮按 `theme_capacity_cost` 把同一三底座 cap 继续压到 `40`，仍不引入人工主题标签或 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40`。命令类型为 A股五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path 1 本轮记录。
- `80/20 total_mv` 五窗口 CAGR 为 `20.99% / 18.75% / 27.16% / 106.31% / 141.43%`，最大回撤 `-30.55% / -35.66% / -22.57% / -16.89% / -4.46%`，换手 `4.43x / 4.55x / 4.29x / 7.51x / 7.35x`；`90/10 equal_weight` 为 `22.67% / 16.92% / 23.71% / 146.19% / 74.19%`；`90/10 total_mv` 为 `20.66% / 17.99% / 21.56% / 141.60% / 56.87%`。
- 新组继续证明 cap40 能保留 2025/2026 极强弹性，但 2020 CAGR 与回撤仍弱；近期持仓仍集中在鼎龙股份、杰瑞股份、中国海油、源杰科技等强势票，属于多票强主题贡献但少票集中风险没有消除。`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 因本轮新增后三底座 active 会把 `ashare_path4_emergent_theme` 推到 63 个，收尾从 active discovery universe 移出 `aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35`，原因是该组 2020 CAGR 仅约 `17%-19%`、长窗回撤仍深，且未改善 robust；保留历史结果但不再占用 active cap。收口后 `scripts/path2_candidate_pass.py` 为 `emergent_theme_discovery=58`，最终 guard 为 `ashare_path4_emergent_theme 60/60 complete`。最终 focus 转为 `emergent_theme_coverage`；下一轮第一条命令建议换 promotion/覆盖形态而不是继续只降 cap，例如三底座 `aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap50`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_coverage_ids>`。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass`，上一轮要求按 `theme_risk_control` 测三底座 `aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45`；新增前因 Path 4 active cap 已到 `60`，先把最弱变体 `aggr_02_98_prom2_emergent_theme_cash_off_and_cap95` 从 active discovery universe 移出，原因是三底座四窗口最小 CAGR 仅约 `5.11% / 8.39% / 9.06%`，平均 min CAGR 低且未改善 robust。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45`。实际命令见 Path 1 本轮 A股合并批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `80/20 total_mv` 五窗口 CAGR 为 `21.51% / 19.11% / 28.38% / 109.72% / 154.33%`，最大回撤 `-31.98% / -37.65% / -23.44% / -16.89% / -3.21%`，换手 `4.47x / 4.48x / 4.26x / 7.43x / 7.29x`；`90/10 equal_weight` 为 `23.42% / 16.07% / 23.22% / 148.00% / 75.33%`；`90/10 total_mv` 为 `21.69% / 17.36% / 22.15% / 146.59% / 54.32%`。
- 本轮新组仍是短窗极强、2020 稳定性不足的形态，且最近持仓继续集中在鼎龙股份、杰瑞股份、中国海油、源杰科技等强势票；按 Path 4 晋级规则不因 2025/2026 单窗 CAGR 改写 official。`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=58`，最终 guard `ashare_path4_emergent_theme 60/60 complete`；收尾再次运行 guard 后下一轮 focus 转为 `theme_capacity_cost`。第一条命令建议在不引入人工主题/ETF 的前提下继续压单票/容量上限，例如三底座 `aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40` 或同等 cap40 成本版，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass`，上一轮建议扩 `aggr_04_96_prom2` 覆盖形态；本轮注册三底座 `aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50` 后，guard 如预期报 `ashare_path4_emergent_theme 3/60 missing`，已作为 blocking 第一优先级按原始 `--only-base-ids` 补齐。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance,core_explore_80_20_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50`。
- `80/20 total_mv` 五窗口 CAGR 为 `21.82% / 19.43% / 28.43% / 109.64% / 157.81%`，最大回撤 `-30.55% / -36.76% / -22.78% / -16.89% / -1.95%`，换手 `4.41x / 4.42x / 4.16x / 7.41x / 7.23x`；`90/10 equal_weight` 为 `23.59% / 16.24% / 23.98% / 147.74% / 77.05%`；`90/10 total_mv` 为 `22.03% / 17.78% / 23.10% / 146.90% / 52.54%`。
- 本轮 `04/96 risk30 cap50` 仍显示极强 2025/2026，但 2020 稳定性和最差回撤不足，近期持仓仍集中在鼎龙股份、杰瑞股份、源杰科技、中国海油等强势票；按 Path 4 晋级规则不因单一短窗 CAGR 改写 official。`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=58`，最终 guard 为 `ashare_path4_emergent_theme 60/60 complete`，候选池未触发 evict。下一轮 focus 为 `theme_risk_control`；第一条命令建议测试三底座 `aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45` 或同等更严格风险控制/容量组合，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`，继续记录集中度、最差回撤与是否只是少票幸运。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass`，上一轮 `risk30_cap45` 短窗强但 2020 稳定性和少票集中风险仍不足；本轮按 `theme_capacity_cost` 把三底座 cap 进一步压到 `40`，继续只用无人工主题标签的强主题涌现信号。新增注册后 guard 如预期报 `ashare_path4_emergent_theme 3/57 missing`，已作为第一优先级按原始 `--only-base-ids` 补齐。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40`、`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40`。实际补缺口命令见 Path 1 本轮 coverage 批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `80/20 total_mv` 五窗口 CAGR 为 `21.36% / 18.42% / 27.54% / 105.69% / 141.78%`，最大回撤 `-28.54% / -35.42% / -20.91% / -17.14% / -4.46%`，换手 `4.45x / 4.60x / 4.33x / 7.51x / 7.36x`；`90/10 equal_weight` 为 `22.53% / 16.69% / 22.74% / 144.17% / 75.24%`，最大回撤 `-26.99% / -38.10% / -25.07% / -18.82% / -13.03%`；`90/10 total_mv` 为 `20.96% / 17.73% / 21.38% / 140.55% / 58.23%`，最大回撤 `-30.52% / -35.81% / -22.07% / -17.00% / -3.41%`。
- 本轮 `cap40` 仍有极强 2025/2026，但 2020 弱、换手高，且持仓继续集中在鼎龙股份、杰瑞股份、中国海油等少数强势票；按 Path 4 晋级规则不因单一短窗 CAGR 改写 official。`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=55`，最终 guard 为 `57/57 complete`，候选池未触发 evict。下一轮 focus 转为 `emergent_theme_coverage`；第一条命令建议扩一个不同 promotion/覆盖形态而不是继续只压 cap，例如三底座 `aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_coverage_ids>`，继续记录集中度、最差回撤与是否只是少票幸运。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass`，上一轮 `risk35_cap45` 把 2025/2026 短窗推高但 2020 仍弱；本轮按 `theme_signal_quality` 把三底座风险阈值压到 `risk30` 并保持 `cap45`，继续只用无人工主题标签的强主题涌现信号。新增注册后 guard 如预期报 `ashare_path4_emergent_theme 3/54 missing`，已作为第一优先级按原始 `--only-base-ids` 补齐。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45`、`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_quality_rebalance,core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45`。
- `80/20 total_mv` 五窗口 CAGR 为 `21.90% / 19.28% / 27.98% / 109.71% / 155.79%`，最大回撤 `-30.94% / -36.55% / -22.43% / -17.13% / -3.21%`，换手 `4.38x / 4.40x / 4.15x / 7.43x / 7.29x`；`90/10 equal_weight` 为 `23.86% / 16.19% / 22.65% / 146.55% / 75.96%`，最大回撤 `-28.49% / -40.79% / -27.78% / -19.47% / -13.51%`；`90/10 total_mv` 为 `22.22% / 17.61% / 21.81% / 146.81% / 55.26%`，最大回撤 `-32.61% / -39.11% / -25.87% / -18.31% / -3.39%`。
- 本轮 `risk30_cap45` 继续显示 2025/2026 极强，但 2020 稳定性和最差回撤仍弱于当前 Path 4 robust，且近期持仓仍集中在鼎龙股份、杰瑞股份、中国海油等少数强势票，不能只按短窗 CAGR 晋级。`scripts/update_weighted_winners.py` 后 Path 4 official/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=52`，最终 guard 为 `54/54 complete`，候选池未触发 evict。下一轮 focus 轮到 `theme_capacity_cost`；第一条命令建议在不引入人工主题/ETF 的前提下继续压单票/容量上限，例如三底座 `aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_capacity_cost_ids>`，并继续记录持仓集中度、最差回撤与是否只是单票幸运。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass`，上一轮 `risk35_cap55` 仍是短窗强、2020/回撤弱；本轮按 `theme_capacity_cost` 把三底座单票/容量上限继续压到 `cap45`。新增注册后 guard 如预期报 `ashare_path4_emergent_theme 3/51 missing`，已作为第一优先级按原始 `--only-base-ids` 补齐，没有替换成全量回测。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45`、`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45`。实际补缺口命令见 Path 1 本轮 coverage block 批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `80/20 total_mv` 五窗口 CAGR 为 `21.48% / 19.01% / 28.20% / 109.71% / 155.79%`，最大回撤 `-32.50% / -38.14% / -23.83% / -17.13% / -3.21%`，换手 `4.45x / 4.47x / 4.24x / 7.43x / 7.29x`；`90/10 equal_weight` 为 `23.56% / 16.10% / 23.32% / 146.55% / 75.96%`；`90/10 total_mv` 为 `21.77% / 17.29% / 22.02% / 146.81% / 55.26%`。
- 本轮 `cap45` 把 2025/2026 短窗推得更高，且 `80/20 total_mv` 的 2026 回撤控制较好；但 2020 稳定性仍低于当前 Path 4 robust，`90/10` 两个底座还暴露更深的 2020 回撤。近期持仓仍集中在鼎龙股份、杰瑞股份、中国海油等少数强势票，虽不是单票幸运，但少票集中风险未消除，第一阶段继续不改写 official winner。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=49`，2025 family top list 已出现本轮 `cap45` 候选；`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。收尾 guard 为 `ashare_path4_emergent_theme 51/51 complete`，下一轮 focus 为 `theme_signal_quality`；第一条命令建议不要继续只压 cap，改测信号质量/风险阈值交互，例如三底座 `aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45` 或同等更严格质量门槛版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_signal_quality_ids>`，并继续记录持仓集中度与最差回撤。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass`；按上一轮第一条命令新增三底座 `aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55` 后，guard 如预期报 `ashare_path4_emergent_theme 3/48 missing`。本轮第一优先级已按 report 原始 `--only-base-ids` 增量补齐，没有替换成全量回测。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55`、`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55`。
- `80/20 total_mv` 五窗口 CAGR 为 `21.41% / 18.78% / 28.61% / 108.76% / 161.60%`，最大回撤 `-32.89% / -38.43% / -23.90% / -17.13% / -0.68%`，换手 `4.48x / 4.48x / 4.25x / 7.41x / 7.18x`；`90/10 equal_weight` 为 `23.66% / 16.21% / 23.64% / 143.45% / 79.23%`，`90/10 total_mv` 为 `21.53% / 17.30% / 23.24% / 144.37% / 51.56%`。
- 本轮 risk35/cap55 组短窗仍强，尤其 `80/20 total_mv` 的 2026 CAGR `161.60%` 且回撤极浅；但 2020 稳定性和最差回撤仍弱于当前 Path 4 robust。近期持仓抽样显示 `80/20 total_mv` 仍集中在鼎龙股份、杰瑞股份等少数强势票，但不是单票一票驱动；第一阶段继续不改写 official winner。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=47`；`scripts/update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。候选池未触发 evict。收尾 focus 转向 `theme_capacity_cost`；下一轮第一条命令建议在本轮强短窗基础上做容量/单票压力而不是继续放大短窗，例如三底座 `aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_capacity_cost_ids>`。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass`；按上一轮第一条命令新增三底座 `aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60` 后，guard 如预期报 `ashare_path4_emergent_theme 3/45 missing`，已优先按 report 原始 `--only-base-ids` 增量补齐，没有替换成全量回测。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60`、`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60`。实际补缺口命令见 Path 1 本轮 coverage block 批次。
- `80/20 total_mv` 五窗口 CAGR 为 `21.94% / 18.88% / 28.80% / 107.21% / 163.61%`，最大回撤 `-31.17% / -37.64% / -22.55% / -17.13% / 0.00%`，换手 `4.41x / 4.42x / 4.14x / 7.41x / 7.13x`；`90/10 equal_weight` 为 `23.95% / 15.94% / 23.69% / 140.10% / 80.68%`，`90/10 total_mv` 为 `21.94% / 17.42% / 23.33% / 141.49% / 49.72%`。
- 本轮 `aggr_03_97_prom2` 组短窗很强，尤其 `80/20 total_mv` 的 2026 回撤为 `0.00%`，但 2020 稳定性弱于当前 robust；近期持仓仍集中在少数强势票上，需要继续把单票/少票贡献当作风险项记录。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=44`，`update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 收尾 guard 为 `ashare_path4_emergent_theme 45/45 complete`，下一轮 focus `theme_risk_control`。第一条命令建议不要继续只追短窗 cap，先实现三底座 `aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap55` 或同等风险控制版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_theme_risk_control_ids>`，并继续检查是否由多票强势贡献而非单票幸运。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass`；按上一轮 `theme_capacity_cost` 第一条命令新增三底座 `aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60` 后，guard 如预期报 `ashare_path4_emergent_theme 3/42 missing`。已优先按 report 原始 `--only-base-ids` 增量补齐，没有替换成全量回测。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60`、`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60`、`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60`。
- `80/20 total_mv` 五窗口 CAGR 为 `18.77% / 28.16% / 36.15% / 117.77% / 116.41%`，最大回撤 `-29.03% / -31.32% / -23.57% / -15.22% / 0.00%`，换手 `3.96x / 4.06x / 3.78x / 6.41x / 7.35x`；`90/10 equal_weight` 为 `21.82% / 22.34% / 28.29% / 138.05% / 62.73%`，`90/10 total_mv` 为 `21.51% / 24.60% / 34.70% / 136.63% / 34.44%`。
- cap60 仍以 `80/20 total_mv` 最均衡，短窗强且 2026 回撤为 `0.00%`，但 2017/2020 仍不足以替换当前 Path 4 robust。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=41`，family 前列仍偏向上一轮 `risk30_cap65` 与旧 `risk40_cap70`；`update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，第一阶段不改写 official winner。
- 收尾 guard 为 `ashare_path4_emergent_theme 42/42 complete`，下一轮 focus 为 `emergent_theme_coverage`。第一条命令建议扩一个不同 promotion/持有形态的覆盖组，而不是继续只降 cap：实现三底座 `aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_coverage_ids>`，并继续记录持仓是否由多票强势贡献而非单票幸运。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass`；按上一轮下一步新增 `aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65` 后，guard 如预期报 `ashare_path4_emergent_theme 3/39 missing`。第一次按 guard 命令执行时未指定 `--end-date`，本地离线缓存拒绝使用 2026-05-22 stale prepared cache；随后按同一 `--only-base-ids` 范围加 `--end-date 2026-05-19` 补齐，没有跑全量。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65`、`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65`、`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65`。
- `80/20 total_mv` 五窗口 CAGR 为 `18.85% / 28.11% / 36.41% / 116.07% / 118.06%`，最大回撤 `-29.03% / -31.32% / -23.54% / -15.22% / 0.00%`，换手 `3.96x / 4.07x / 3.78x / 6.41x / 7.30x`；`90/10 equal_weight` 为 `21.92% / 22.11% / 28.56% / 134.75% / 64.00%`，`90/10 total_mv` 为 `21.61% / 24.63% / 34.96% / 133.83% / 32.92%`。
- 本轮仍以 `80/20 total_mv` 最均衡：2020/2023 稳定性强且 2026 最大回撤为 `0.00%`，但 2017 与 2020 仍不足以替换当前 Path 4 robust。`update_weighted_winners.py` 后 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，第一阶段不改写 official winner。
- 收尾 guard 为 `ashare_path4_emergent_theme 39/39 complete`，下一轮 focus 为 `theme_capacity_cost`。第一条命令建议在本轮最均衡形态上降低单票/容量压力，测试三底座 `aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap60`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_capacity_cost_ids>`。

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass`，新增注册后按 guard 原始 block 命令补齐 `ashare_path4_emergent_theme 3/36 missing`；上一轮 `quality_gate_risk35_cap35` 证明继续压单票上限不能修复 2020，本轮回到 `aggr_05_95_prom3` 并把 cap 放宽到 `65`，检查质量门槛 + 中等容量是否改善稳定性。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65`、`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65`、`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65`。实际命令见 Path 1 本轮合并命令，命令类型为五窗口 `--only-base-ids` 增量确认。
- `80/20 total_mv` 五窗口 CAGR 为 `18.50% / 28.20% / 36.60% / 116.10% / 118.10%`，最大回撤 `-30.20% / -32.20% / -25.00% / -15.20% / 0.00%`，换手 `4.02x / 4.13x / 3.88x / 6.41x / 7.30x`；`90/10 equal_weight` 为 `21.70% / 22.10% / 29.40% / 134.70% / 64.00%`，`90/10 total_mv` 为 `21.40% / 24.80% / 35.90% / 133.80% / 32.90%`。
- 本轮最均衡的是 `80/20 total_mv`：2020/2023 稳定性和 2026 弹性都较强，且 2026 最大回撤为 `0.00%`；但 2020 仍没有稳定打穿既有 Path 4 robust，第一阶段不改写 official winner。`update_weighted_winners.py` 后 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=35`，最终 guard 为 `36/36 complete`。下一轮 focus -> candidates 池切到 `theme_signal_quality`：第一条命令建议测试三底座 `aggr_05_95_prom3_emergent_theme_quality_gate_risk30_cap65` 或 `risk35_cap60`，用更严格风险阈值/略低 cap 判断本轮 2026 弹性是否能保留且不靠单票幸运；五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_signal_quality_ids>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass`，新增注册后按 guard 原始 block 命令补齐 `ashare_path4_emergent_theme 3/33 missing`；上一轮 `risk35_cap40` 仍有短窗强度但长窗弱，本轮按 `theme_capacity_cost` 把单票上限继续压到 `35%`，检查是否仍不是单票幸运。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35`、`core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35`。实际命令见 Path 1 本轮合并命令。
- `80/20 total_mv` 五窗口 CAGR 为 `17.11% / 19.06% / 33.02% / 97.37% / 96.59%`，最大回撤 `-30.61% / -36.96% / -22.72% / -16.73% / -7.46%`，换手 `3.47x / 3.93x / 3.62x / 6.28x / 7.86x`；`90/10 equal_weight` 为 `16.98% / 19.36% / 33.54% / 100.88% / 93.21%`；`90/10 total_mv` 为 `17.08% / 18.38% / 32.53% / 109.59% / 74.75%`。
- 持仓抽样仍是多票分散：鼎龙股份、国瓷材料、杰瑞股份、宏和科技、长飞光纤、睿创微纳等共同贡献，单票没有接近 cap；但 2017/2020 收益仍弱于旧 `risk30_cap50` robust，2020 回撤没有改善，未改变 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=33`，family 前列仍由 `aggr_05_95_prom3_emergent_theme_risk40_cap70` 与 `quality_gate_risk40_cap70` 占据；`update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。候选池未触发 evict。
- 下一轮 focus -> candidates 池：最终 guard 给出 `emergent_theme_coverage`，但 cap35 证明继续压 cap 不能修复 2020；第一条命令建议用覆盖扩展方式回到更均衡 promotion，测试三底座 `aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65`，用中等 cap 检查 2020/2023 稳定性；五窗口 `--only-base-ids <next_path4_coverage_ids>`。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 指向 `theme_risk_control`；上一轮 `risk35_cap45` 2026 强但 2020 回撤偏宽，本轮把单票/容量 cap 进一步压到 `40`，继续不使用人工主题标签，也不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40`、`core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40`。实际命令见 Path 1 本轮合并命令。
- `80/20 total_mv` 五窗口 CAGR 为 `17.42% / 18.56% / 33.03% / 98.21% / 92.46%`，最大回撤 `-30.61% / -36.96% / -22.88% / -16.73% / -6.80%`，换手 `3.49x / 3.94x / 3.60x / 6.25x / 7.69x`；`90/10 equal_weight` 为 `17.59% / 19.17% / 33.31% / 94.94% / 98.98%`；`90/10 total_mv` 为 `17.54% / 18.33% / 32.47% / 104.83% / 77.17%`。
- 持仓抽样仍呈多只强票分散贡献，不像单票幸运；但 2017/2020 CAGR 和 2020 回撤弱于现有 Path 4 robust，未改变 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=30`，`update_weighted_winners.py` 后 Path 4 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`；候选池未触发 evict。
- 收尾 guard 后 rotation 切到 `theme_capacity_cost`。下一轮第一条命令建议测试三底座 `aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35`，用更低单票上限做容量压力检查，并在 plan 中同步持仓集中度/换手；五窗口命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path4_capacity_cost_ids>`。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `quality_gate_risk30_cap45` 确认 cap45 能压单票集中但长窗仍弱，本轮按 rotation 的 `theme_risk_control` 把风险阈值从 `30` 放宽到 `35`，继续不使用人工主题标签，也不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap45`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap45`、`core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap45`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_quality_gate_risk35_cap45_ids>`。
- `80/20 total_mv` 五窗口 CAGR 为 `17.59% / 18.40% / 33.12% / 98.63% / 96.07%`，最大回撤 `-30.61% / -36.96% / -22.79% / -16.73% / -5.24%`，换手 `3.51x / 3.95x / 3.55x / 6.15x / 7.82x`；`90/10 equal_weight` 为 `17.71% / 19.01% / 33.13% / 89.33% / 105.26%`；`90/10 total_mv` 为 `17.76% / 18.28% / 32.53% / 102.90% / 80.57%`。
- 持仓抽样仍是多只强票分散贡献，近期前列包括鼎龙股份、国瓷材料、杰瑞股份、宏和科技、长飞光纤、睿创微纳等，不像单票幸运；但 2020 回撤扩大、2017/2020 CAGR 低于现有 Path 4 robust，未改变 window winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=27`，`update_weighted_winners.py` 后 Path 4 official winners 与 robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`；候选池未触发 evict。
- 下一轮 focus -> candidates 池：`theme_risk_control` 不能只放宽风险阈值，第一条命令建议测试三底座 `aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40`，用更低 cap 检查 2026 强势是否仍非单票驱动，五窗口 `--only-base-ids <next_path4_risk_control_ids>`。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `quality_gate_risk30_cap50` 2026 强但需检查容量与单票依赖，本轮按 `theme_signal_quality` 把单票上限从 `50%` 压到 `45%`，继续不使用人工主题标签，也不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45`、`core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45`。实际回测命令见 Path 1 本轮合并命令。
- `80/20 total_mv` 五窗口 CAGR 为 `17.93% / 18.85% / 32.93% / 98.63% / 96.07%`，最大回撤 `-29.10% / -35.01% / -21.73% / -16.73% / -5.24%`，换手 `3.46x / 3.89x / 3.48x / 6.15x / 7.82x`；`90/10 equal_weight` 为 `17.97% / 19.36% / 32.89% / 89.33% / 105.26%`，`90/10 total_mv` 为 `18.06% / 18.52% / 32.30% / 102.90% / 80.57%`。
- 持仓抽样看，cap45 降低了单票集中，2026 观察窗前列为鼎龙股份、国瓷材料、杰瑞股份、宏和科技、长飞光纤、睿创微纳等，单票未超过约 `18%`，不像单票幸运；但 2017/2020 长窗仍弱于现有 Path 4 robust，未晋级。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=24`，`update_weighted_winners.py` 后 Path 4 2017 window winner 为旧 `quality_gate_risk40_cap70` 等权候选，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。收尾 guard 为 `pass`，Path 4 `24/24 complete`，rotation 为 `stagnation_runs=5 / theme_signal_quality / rotate`。
- 下一轮 focus -> candidates 池继续信号质量，但不要只压单票上限；第一条命令建议实现三底座 `aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap45`，五窗口 `--only-base-ids <next_path4_signal_quality_ids>` 增量确认。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `risk30_cap50` 抬高短窗但仍需验证质量门槛与容量，本轮按 `emergent_theme_coverage` 补三底座 `quality_gate_risk30_cap50`，继续不使用人工主题标签，也不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50`、`core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50`。实际回测命令见 Path 1 本轮合并命令。
- `80/20 total_mv` 五窗口 CAGR 为 `17.98% / 18.81% / 32.94% / 98.69% / 99.46%`，最大回撤 `-29.10% / -35.01% / -22.10% / -16.73% / -5.24%`，换手 `3.48x / 3.89x / 3.47x / 6.12x / 7.81x`；`90/10 equal_weight` 为 `18.28% / 19.20% / 32.73% / 89.15% / 109.31%`，`90/10 total_mv` 为 `18.13% / 18.47% / 32.34% / 103.47% / 85.40%`。质量门槛改善 2026 观察，但 2017/2020 长窗低于现有 `risk30_cap50` robust，未晋级。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=21`，`update_weighted_winners.py` 后 Path 4 window winners 与 robust 未变化；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，`meanCAGR=42.88% / minCAGR=21.82% / worstMaxDD=-33.79% / meanTurn=4.24`。
- 收尾 guard 为 `pass`，Path 4 `21/21 complete`，rotation 为 `stagnation_runs=2 / emergent_theme_coverage / continue`；候选池未触发 evict。下一轮 focus -> candidates 池继续覆盖强主题涌现，但必须抽样检查持仓是否由少数单票贡献，第一条命令建议先实现三底座 `aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45`，五窗口 `--only-base-ids <next_path4_coverage_ids>` 增量确认。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 quality gate 说明 80/20 总市值更均衡，下一步指向容量/风险控制。本轮新增三底座 `risk30_cap50`，继续不使用人工主题标签，也不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`、`core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。实际回测命令见 Path 1 本轮合并命令。
- `80/20 total_mv` 五窗口 CAGR 为 `22.88% / 22.41% / 31.07% / 93.62% / 136.50%`，最大回撤 `-30.11% / -32.16% / -21.49% / -16.86% / 0.00%`，换手 `3.46x / 4.13x / 3.44x / 6.16x / 6.01x`；相比 `risk50_cap50` 明显收窄 2020/2023 回撤，并保持短窗强弹性。
- `90/10 equal_weight` 五窗口 CAGR 为 `24.93% / 20.59% / 33.10% / 88.76% / 109.69%`，`90/10 total_mv` 为 `23.89% / 18.96% / 32.34% / 101.10% / 126.99%`；两者 raw 2017 更高，但 2020 验证不足，`update_weighted_winners.py` 未采纳为 official。
- `update_weighted_winners.py` 后 Path 4 发生实质变化：2017 window winner 与四窗口 robust 切到 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`，robust 为 `meanCAGR=42.50% / minCAGR=22.41% / worstMaxDD=-32.16% / meanTurn=4.30`；2020 仍为 `risk40_cap70`，2023 为 `quality_gate_risk40_cap70`，2025 为 `90/10 total_mv risk40_cap70`。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=18`，最终 guard 显示 Path 4 `18/18 complete` 且 rotation 为 `stagnation_runs=1 / emergent_theme_coverage / continue`；候选池未触发 evict。下一轮 focus -> candidates 池继续 `emergent_theme_coverage`，但必须检查持仓明细是否由少数单票贡献。第一条命令建议先实现 `aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50` 或 `risk30_cap45` 三底座，并用五窗口 `--only-base-ids <next_path4_ids>` 增量确认。

## 本轮执行计划（2026-05-20 13:58 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，上一轮 12 个强主题候选已补齐；本轮按 `theme_signal_quality / theme_risk_control` 新增 quality gate 变体，继续不使用人工主题标签，也不纳入 ETF。
- 本轮新增并五窗口确认 3 个 Path 4 base ids：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70`、`core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70`、`core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70`。实际回测命令见 Path 1 本轮合并命令。
- 三个 quality gate 版本中，`80/20 total_mv` 最均衡：五窗口 CAGR `17.85% / 27.49% / 37.88% / 114.97% / 119.72%`，最大回撤 `-33.05% / -34.80% / -26.93% / -15.22% / 0.00%`，换手 `4.10x / 4.23x / 4.00x / 6.40x / 7.26x`；相比第一批强主题候选，2020/2023 稳定性更好，但仍需检查持仓是否由单票幸运贡献。
- `90/10 equal_weight` 五窗口 CAGR 为 `21.22% / 21.52% / 29.07% / 131.46% / 65.15%`，2023 回撤 `-38.40%` 偏深；`90/10 total_mv` 为 `20.74% / 24.58% / 35.69% / 131.04% / 31.40%`，2026 弹性不足且换手最高到 `8.46x`。
- `scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=15`，guard 显示 Path 4 `15/15 complete`；第一阶段仍不改 official winner/tracked/top5。候选池未触发 evict。
- 收尾 rotation 未给独立 Path 4 stagnation，但 quotas 给出 `theme_signal_quality=3 / theme_risk_control=3 / theme_capacity_cost=2`；下一轮 focus -> candidates 池先做质量门槛后的容量/集中度压力。第一条命令建议先实现三底座 `aggr_08_92_prom6_emergent_theme_risk30_cap50`，再用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_risk_control_ids>` 增量确认。

## 本轮执行计划（2026-05-20 05:20 CST）

- 开局 guard 为 `block / blocking=12 / scope=ashare_path4_emergent_theme`；按 report 原始 rerun command 优先补齐 12 个强主题候选的五窗口覆盖，没有替换成全量回测。首次未锁 `--end-date` 触发本地 A 股缓存只到 `2026-05-19` 的 stale guard；随后使用离线缓存并显式锁定 `--end-date 2026-05-19` 完成补跑。
- 覆盖补跑命令：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_emergent_theme_cash_off_and_cap95,core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_emergent_theme_risk40_cap90,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk50_cap50,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_emergent_theme_cash_off_and_cap95,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_emergent_theme_risk40_cap90,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_risk50_cap50,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_emergent_theme_cash_off_and_cap95,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_emergent_theme_risk40_cap90,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk50_cap50`。
- `scripts/path2_candidate_pass.py` 已把 `emergent_theme_discovery` 识别为独立 family，`12/12` candidates complete。按 2017/2020/2023 最低 CAGR 看，较稳的候选是 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk50_cap50`，五窗口 CAGR `21.26% / 20.61% / 30.79% / 93.62% / 136.50%`，最差回撤 `-39.74%`，换手 `3.72x-6.16x`；短窗很强，但回撤仍深且 2026 观察窗可能受单票/少数强票影响。
- 另一个较稳候选 `core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70` 五窗口 CAGR 为 `19.43% / 21.99% / 35.66% / 140.82% / 35.50%`，最差回撤 `-39.50%`，换手最高到 `8.51x`；上限高但容量与成本压力更重。
- 本阶段未改写 official winner/tracked/top5，只作为 Path 4 独立观察；guard 收尾为 `pass / blocking=0 / warning=0`。Path 4 候选池为 `12`，未触发 evict。
- 下一轮 focus -> candidates 池按 report quota 先走 `theme_signal_quality` 与 `theme_risk_control`：建议实现 `aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70` 与 `aggr_08_92_prom6_emergent_theme_risk30_cap50`，第一条命令用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <new_path4_theme_ids>`。
## 本轮执行计划（2026-06-01 16:23 CST）

- 上一轮候选/结果摘要：上一轮三底座 `signal24_risk25_cap16_exit70` 计划用于继续检查强主题涌现的容量与单票依赖，且要求达到候选池 cap 后先淘汰弱线。
- 本轮 active pool cap 处理：Path 4 active 候选池维持 `60` 个；新增前从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除旧弱线 `aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78`。evict 原因：旧 prom7/risk40/cap35 在此前 2020/2023 稳定性和 robust 排序均弱，继续压低 cap 未修复长窗。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`、`core_explore_90_10_equal_weight_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`、`core_explore_90_10_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_cap16_ids>`。
- `80/20 total_mv` 五窗口 CAGR 为 `14.19% / 13.11% / 35.90% / 97.80% / 124.74%`，最大回撤为 `-23.40% / -26.35% / -16.25% / -10.78% / -8.73%`，换手为 `2.95x / 3.28x / 3.40x / 5.78x / 7.20x`；`90/10 equal_weight` 为 `13.16% / 13.44% / 37.67% / 118.10% / 113.46%`，`90/10 total_mv` 为 `13.52% / 11.24% / 35.22% / 114.59% / 88.12%`。
- 持仓抽样仍是多票强势结构，近期包括杰普特、宏和科技、鼎龙股份、天孚通信、源杰科技、杰瑞股份、华峰测控等，并非单票幸运；但 2017/2020 CAGR 明显低于现有 Path 4 robust，未改变 window winner、robust candidate 或 tracked payload。`scripts/path2_candidate_pass.py` 后 Path 4 coverage 达到 `60/60 complete`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> emergent_theme_coverage`。下一轮不要继续只降 cap，第一候选建议实现 `aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap16_exit70_coverage_penalty`，增加主题覆盖/拥挤惩罚，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_coverage_penalty_ids>`。

## 本轮执行计划（2026-06-02 22:30 CST）

- 上一轮候选/结果摘要：上一轮 `signal24_leader68_risk20_cap12_exit68` 继续显示短窗强但 2017/2020 弱。本轮按 guard blocking scope 优先补齐 Path 4 新强主题涌现候选，继续不使用人工主题标签、不纳入 ETF。
- 本轮 active pool cap 处理：Path 4 active 候选池维持 `60` 个；新增前从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除旧弱线 `aggr_10_90_prom9_emergent_theme_quality_gate_signal18_risk40_cap30_exit78`。evict 原因：signal18/risk40/cap30 在长窗与 robust 排序持续落后，且继续占用强主题涌现 cap。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk25_cap16_exit70`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk25_cap16_exit70`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk25_cap16_exit70`。补缺口命令与 Path 1 core_multifactor 合并执行，使用 `--only-base-ids <three_path4_signal26_ids>` 覆盖五窗口。
- `80/20 total_mv` 五窗口 CAGR 为 `14.47% / 16.97% / 31.77% / 89.85% / 118.70%`，最大回撤为 `-25.52% / -29.94% / -15.17% / -10.20% / -8.78%`，换手为 `2.85x / 3.22x / 3.22x / 5.69x / 7.11x`；`90/10 equal_weight` CAGR 为 `12.49% / 15.28% / 32.60% / 108.94% / 114.40%`；`90/10 total_mv` 为 `13.44% / 14.50% / 30.22% / 104.72% / 93.50%`。
- 持仓抽样仍是多票强势结构，近期包括宏和科技、国瓷材料、大族数控、杰瑞股份、中国海油、沃尔德、长飞光纤、精智达等，不像单票幸运；但 2017/2020 低于旧 `risk30_cap50` robust，未改变 Path 4 window winner、robust candidate 或 tracked payload。`scripts/path2_candidate_pass.py` 后 `emergent_theme_discovery=60` 且最终 guard 为 `60/60 complete`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_risk_control`。下一轮第一候选建议 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap16_exit68`，用更低 risk/exit 检查 2020 回撤是否能改善；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_risk20_signal26_ids>`。

## 本轮执行计划（2026-06-03 12:10 CST）

- 上一轮候选/结果摘要：上一轮 `signal26_leader72_risk25_cap16_exit70` 显示短窗强但 2020/2023 不足。本轮按 `theme_risk_control` 将 risk 从 `25` 降到 `20`、exit 从 `70` 收到 `68`，继续不使用人工主题标签、不纳入 ETF。
- 本轮 active pool cap 处理：Path 4 active 候选池维持 `60` 个；新增前从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除旧弱线 `aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76`。evict 原因：旧 prom9/risk35/cap30 线已被 signal24/26 与 leader 线覆盖，robust 排序长期不进入前列。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap16_exit68`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap16_exit68`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap16_exit68`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal26_risk20_ids>`。
- `80/20 total_mv` 五窗口 CAGR 为 `13.55% / 17.34% / 30.38% / 89.46% / 118.70%`，最大回撤为 `-25.50% / -26.79% / -18.44% / -10.53% / -8.78%`，换手为 `2.81x / 3.18x / 3.14x / 5.75x / 7.11x`；`90/10 equal_weight` CAGR 为 `13.11% / 15.62% / 31.95% / 108.37% / 114.40%`；`90/10 total_mv` 为 `13.88% / 14.83% / 29.27% / 104.33% / 93.50%`。
- 结论：risk20 确实收窄部分回撤并保留 2026 强势，但 2017/2020 仍低于旧 `risk30_cap50` robust；持仓仍是多票强势结构，不像单票幸运。`path2_candidate_pass.py` 后 `emergent_theme_discovery=60`，Path 4 window winner、robust candidate、tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_capacity_cost`。下一轮第一候选建议 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal26_cap12_ids>`，重点检查降 cap 后 2025/2026 是否仍非单票驱动。

## 本轮执行计划（2026-06-03 10:35 CST）

- 上一轮候选/结果摘要：上一轮 `signal26_leader72_risk20_cap16_exit68` 保留 2026 强势但 2017/2020 仍弱。本轮按 `theme_capacity_cost` 把单票上限从 `16%` 降到 `12%`，检查容量压力下短窗强势是否仍来自多票涌现结构。
- 本轮 active pool cap 处理：Path 4 active 候选池维持 `60` 个；新增前从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除旧弱线 `aggr_10_90_prom9_emergent_theme_quality_gate_signal20_risk40_cap25_exit78`。evict 原因：旧 signal20/risk40/cap25 长窗和 robust 排序持续弱于 signal24/26 leader 线，继续占用强主题涌现 cap。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68`。先按 guard 原始 rerun command 补缺口但未锁 `--end-date`，因 A股缓存只到 `2026-06-02` 触发 stale guard；随后成功命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68`。
- `80/20 total_mv` 五窗口 CAGR 为 `12.09% / 15.34% / 29.03% / 82.66% / 82.03%`，最大回撤为 `-22.42% / -27.19% / -14.86% / -10.73% / -9.73%`；`90/10 equal_weight` CAGR 为 `12.13% / 14.11% / 30.63% / 96.71% / 79.32%`；`90/10 total_mv` 为 `12.86% / 13.37% / 27.61% / 93.18% / 68.17%`。
- 结论：cap12 牺牲 2017/2020，但把 2025 window winner 切到 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68`，回撤较旧短窗 winner 更窄；robust candidate 仍是旧 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。持仓抽样仍呈自动涌现的光通信、半导体设备/材料、能源/油运等强结构，不使用人工主题标签，也未纳入 ETF。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> emergent_theme_coverage` 且处于 `continue` 状态。下一轮第一候选建议在 cap12 上加入覆盖/拥挤惩罚：`aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_coverage_penalty_ids>`。

## 本轮执行计划（2026-06-04 04:18 CST）

- 上一轮候选/结果摘要：上一轮 `signal26_leader72_risk20_cap12_exit68` 把 2025 window winner 切到 90/10 equal_weight，但 2017/2020 偏弱。本轮按 `emergent_theme_coverage` 在 cap12 上增加覆盖/拥挤惩罚近似：提高晋升持仓数到 `14`、单票 cap 降到 `10%`、质量门槛略提高，继续不使用人工主题标签、不纳入 ETF。
- 本轮 active pool cap 处理：Path 4 active 候选池维持 `60` 个；新增前从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除旧弱线 `aggr_10_90_prom9_emergent_theme_quality_gate_risk40_cap30_exit78`。evict 原因：旧 risk40/cap30 长窗与 robust 排名持续弱于 signal24/26 leader 线，继续占用强主题涌现 cap。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68`。实际命令见 Path 1 本轮合并增量命令，使用 `--only-base-ids` 覆盖五窗口。
- `80/20 total_mv` 五窗口 CAGR 为 `10.74% / 14.63% / 30.76% / 77.53% / 77.63%`，最大回撤为 `-28.94% / -24.01% / -13.49% / -10.85% / -10.30%`，换手为 `2.79x / 3.24x / 2.99x / 5.78x / 6.57x`；`90/10 equal_weight` CAGR 为 `11.01% / 15.20% / 30.71% / 82.36% / 66.48%`；`90/10 total_mv` 为 `11.67% / 14.34% / 29.38% / 80.43% / 60.19%`。
- 结论：coverage_penalty 改善了 2020/2023 回撤形态，但牺牲 2017 与短窗收益，未直接改写本轮 Path 4 robust。`update_weighted_winners.py` 同步后 Path 4 `since_2023_01` window winner 从旧 `risk40_cap30_exit78` 切到上一轮 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66`，这是 tracked 口径修正，不是本轮 coverage_penalty 晋级；robust candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> emergent_theme_coverage` 且本路径因 tracked 同步 `changed=true / stagnation_runs=0`。下一轮第一候选建议只做覆盖惩罚的风险阈值对照：`aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap12_exit66` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_coverage_penalty_risk15_ids>`。

## 本轮执行计划（2026-06-08 06:05 CST）

- 上一轮候选/结果摘要：上一轮 coverage penalty 已改善部分 2020/2023 回撤，但 2017 与短窗收益被压低；本轮按 `theme_signal_quality` 测试更低 `risk14/cap10/exit62`，继续不使用人工主题标签、不纳入 ETF。
- 本轮 active pool cap 处理：Path 4 active 候选池维持 `60` 个；新增前从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除 `aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`。evict 原因：该 signal24/risk25/cap16 线 2017/2020 长窗偏弱，已被 signal26/28 leader 覆盖，继续占用 cap 价值低。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk14_cap10_exit62_lowturn`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_risk14_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `11.55% / 19.26% / 26.49% / 85.94% / 70.86%`，最大回撤 `-24.41% / -16.65% / -10.51% / -11.06% / -9.53%`；`90/10 equal_weight` CAGR `12.94% / 18.52% / 24.37% / 88.19% / 66.91%`；`90/10 total_mv` CAGR `12.83% / 18.05% / 24.00% / 87.00% / 63.29%`。
- 结论：risk14/cap10 明显压低回撤，并在 `path2_candidate_pass.py` 的 `emergent_theme_discovery` family score 中让 80/20 total_mv 排到第 1，但仍未改写独立 Path 4 window winner 或 robust candidate；持仓仍是多票强势结构，不是单票幸运。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_risk_control`。下一轮第一候选建议在本轮 `risk14/cap10` 基础上继续压风险阈值：`aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap10_exit60_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_risk12_ids>`。

## 本轮执行计划（2026-06-08 12:13 CST）

- 上一轮候选/结果摘要：上一轮 `risk14/cap10` 降低回撤并在 family score 中靠前，但未改写独立 Path 4 robust。本轮按 `theme_risk_control` 继续压到 `risk12/cap10/exit60`，仍不使用人工主题标签、不纳入 ETF。
- 本轮 active pool cap 处理：Path 4 active 候选池维持 `60` 个；新增前从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移除 `aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`。evict 原因：旧 signal24/risk25/cap16 长窗弱于 signal26/28 leader 线，继续占用 cap 价值低。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap10_exit60_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap10_exit60_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap10_exit60_lowturn`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_risk12_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `11.61% / 20.57% / 26.61% / 85.94% / 70.86%`，最大回撤 `-24.43% / -15.81% / -10.51% / -11.06% / -9.53%`；`90/10 equal_weight` CAGR `12.78% / 19.70% / 24.41% / 86.80% / 66.91%`；`90/10 total_mv` CAGR `13.05% / 19.48% / 24.12% / 86.58% / 63.29%`。
- 结论：risk12 继续改善 2020/2023 回撤，但 2017/robust 分数仍未超过旧 `aggr_08_92_prom6_emergent_theme_risk30_cap50`；`update_weighted_winners.py` 后独立 Path 4 window winner、robust candidate 与 tracked payload 均未改变。持仓仍是多票强势结构，不像单票幸运。
- 下一轮 focus：`theme_capacity_cost / theme_signal_quality`，首条命令建议对同一 signal28 线做 `risk12_cap08_exit60` 容量压力测试： `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal28_risk12_cap08_ids>`。

## 本轮执行计划（2026-06-08 17:37 CST）

- 上一轮候选/结果摘要：上一轮 `risk12/cap10/exit60` 改善 2020/2023 回撤但未改写 robust；本轮按 capacity/cost 压力测试把单票上限降到 `8%`。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 和 `PATH2_SCAN_VARIANT_IDS` 移除旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk25_cap16_exit70`。evict 原因：长窗和 robust 排名持续弱于 signal26/28 leader 线。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap08_exit60_lowturn`。blocking 补跑命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_cap08_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `13.05% / 23.72% / 25.66% / 85.92% / 66.11%`，最差回撤 `-23.23%`；`90/10 equal_weight` CAGR `13.97% / 22.32% / 24.19% / 78.63% / 54.72%`；`90/10 total_mv` CAGR `14.18% / 22.68% / 25.03% / 79.08% / 49.57%`。
- 结论：cap08 保留多票强势结构并进一步控制短窗回撤，但 2017/robust 仍弱于旧 `aggr_08_92_prom6_emergent_theme_risk30_cap50`；Path 4 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_signal_quality`。下一轮第一候选建议不要继续只降 cap，改在同一 cap08 线上提高信号/leader 门槛：`aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk12_cap08_exit60_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal30_cap08_ids>`。

## 本轮执行计划（2026-06-08 23:27 CST）

- 上一轮候选/结果摘要：上一轮 cap08 降低集中度但 2017/robust 不足；本轮按 `theme_signal_quality` 提高到 `signal30/leader80`，并继续保持无人工主题标签、ETF 不纳入。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 active lists 移除 `aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68`，原因是老 signal24/leader68 线在窗口覆盖和 robust 排名上持续弱于新 coverage_penalty 线。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit58_lowturn`；coverage 补齐命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal30_leader80_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `11.60% / 20.23% / 17.60% / 60.10% / 51.40%`，最差回撤 `-19.05%`；`90/10 equal_weight` CAGR `12.91% / 18.22% / 16.69% / 36.65% / 27.46%`，最差回撤 `-13.78%`；`90/10 total_mv` CAGR `12.53% / 16.89% / 16.07% / 38.22% / 32.33%`，最差回撤 `-12.67%`。
- 结论：新线显著压低回撤，但 2023/2025 收益不够，`update_weighted_winners.py` validation 拒绝；Path 4 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_risk_control`。下一轮第一候选建议在 signal30/leader80 保持不变时只放宽 `exit58 -> exit62` 与 `risk12 -> risk14`，三底座首命令为 `.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal30_leader80_risk14_exit62_ids>`。

## 本轮执行计划（2026-06-09 04:20 CST）

- 上一轮候选/结果摘要：上一轮 `signal30/leader80/risk12/cap08/exit58` 回撤很低但 2023/2025 收益不足；本轮按计划放宽到 `risk14/exit62`，继续不使用人工主题标签、不纳入 ETF。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除 `aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68`。evict 原因：老 signal24/leader68/cap12 线长窗和 robust 排名持续弱于新 coverage_penalty 线。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`。首次未锁 `--end-date` 的补缺口命令触发本地 A股缓存 stale guard；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `10.54% / 18.56% / 18.02% / 60.92% / 51.40%`，最大回撤 `-22.46% / -12.70% / -11.46% / -9.39% / -10.26%`；`90/10 equal_weight` CAGR `12.32% / 15.09% / 17.87% / 37.59% / 27.46%`；`90/10 total_mv` CAGR `11.90% / 14.87% / 16.86% / 39.21% / 32.33%`。
- 结论：risk14/exit62 保留较低回撤，但 2023/2025 收益仍不足，`update_weighted_winners.py` validation 拒绝；Path 4 window winner、robust candidate 与 tracked payload 未改变。该线不是单票幸运，但目前更像低回撤参照。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> emergent_theme_coverage`。下一轮第一候选建议继续沿 signal30/leader80 增加覆盖宽度，而不是再单纯放宽风险：`aggr_13_87_prom14_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal30_prom14_coverage_ids>`。

## 本轮执行计划（2026-06-09 20:05 CST）

- 上一轮候选/结果摘要：上一轮 `signal30/leader80/risk14/cap08/exit62` 回撤低但 2023/2025 收益不足；本轮按 `emergent_theme_coverage` 把晋升数从 `prom12` 扩到 `prom14`，继续不使用人工主题标签、不纳入 ETF。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk25_cap16_exit70`。evict 原因：旧 signal26/risk25/cap16 长窗和 robust 排名持续弱于 coverage_penalty 线。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom14_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`；实际 A股合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom14_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `10.54% / 18.56% / 18.02% / 60.92% / 51.40%`，最大回撤 `-22.46% / -12.70% / -11.46% / -9.39% / -10.26%`；`90/10 equal_weight` CAGR `12.32% / 15.09% / 17.87% / 37.59% / 27.46%`，最大回撤最差 `-14.96%`；`90/10 total_mv` CAGR `11.90% / 14.87% / 16.86% / 39.21% / 32.33%`。
- 结论：prom14 扩覆盖后仍保持低回撤多票强势结构，但 2023/2025 收益不足，`update_weighted_winners.py` validation 拒绝；Path 4 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 仍给出 `ashare_path4 -> emergent_theme_coverage`。下一轮第一候选建议只再扩一次覆盖宽度并要求 2023 不低于 prom14：`aggr_13_87_prom16_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal30_prom16_coverage_ids>`。

## 本轮执行计划（2026-06-09 22:26 CST）

- 上一轮候选/结果摘要：上一轮 prom14 低回撤但 2023/2025 收益不足；本轮按 `emergent_theme_coverage` 再扩到 `prom16`，检查更宽晋升池是否能改善 2023 稳定性，同时继续不使用人工主题标签、不纳入 ETF。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 与 `PATH2_SCAN_VARIANT_IDS` 移除旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap16_exit68`。evict 原因：老 signal26/risk20/cap16 长窗和 robust 排名持续弱于 coverage_penalty 线，继续占用强主题涌现 cap 价值低。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom16_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`；实际 A股合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom16_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `10.54% / 18.56% / 18.02% / 60.92% / 51.40%`，最大回撤 `-22.46% / -12.70% / -11.46% / -9.39% / -10.26%`；`90/10 equal_weight` CAGR `12.32% / 15.09% / 17.87% / 37.59% / 27.46%`；`90/10 total_mv` CAGR `11.90% / 14.87% / 16.86% / 39.21% / 32.33%`。
- 结论：prom16 与 prom14 指标基本持平，低回撤、多票强势结构成立，但 2023/2025 收益仍不足，`update_weighted_winners.py` validation 拒绝；Path 4 window winner、robust candidate 与 tracked payload 未改变。最终 guard 显示 `ashare_path4_emergent_theme 60/60 complete`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_signal_quality`。下一轮不要再单纯扩晋升数，建议提高质量/信号确认并保持 cap08：`aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal32_prom16_ids>`。

## 本轮执行计划（2026-06-10 04:41 CST）

- 上一轮候选/结果摘要：上一轮 `signal30/prom16` 低回撤但收益不足；本轮按 `theme_signal_quality` 提高 signal/leader 门槛到 `32/82`，继续保持自动强主题涌现路径，不引入人工主题标签或 ETF。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 归档旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk20_cap12_exit68`。evict 原因：风险阈值高、信号质量低，长期弱于 coverage_penalty/lowturn 线；公开快照同步删除对应三个旧 strategy detail。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk12_cap08_exit60_lowturn`；实际 A股合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal32_prom16_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `10.57% / 10.58% / 6.82% / 42.56% / 30.69%`，最大回撤 `-17.58% / -17.58% / -8.42% / -10.44% / -10.55%`，换手 `3.93x / 3.86x / 3.32x / 6.86x / 7.02x`；`90/10 equal_weight` CAGR `2.72% / 5.99% / 8.07% / 19.57% / 9.45%`；`90/10 total_mv` CAGR `6.38% / 7.33% / 5.24% / 19.25% / 12.65%`。
- 结论：更硬 signal/risk12 降回撤但显著压低 2020/2023 收益，未改变 Path 4 window winner、robust candidate 或 tracked payload。该结果说明下一轮不应继续单纯加严信号。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_risk_control`。下一轮第一候选建议在同一 signal32 上放回 `risk14/exit62` 做收益恢复：`aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal32_risk14_ids>`。

## 本轮执行计划（2026-06-10 10:40 CST）

- 上一轮候选/结果摘要：上一轮 `signal32/risk12/exit60` 回撤低但收益被压低；本轮按 `theme_risk_control` 放回 `risk14/exit62`，继续保持独立 Path 4 强主题涌现口径，不使用人工主题标签、不纳入 ETF，也不并入 Path 2 扫描池。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移除旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68`。evict 原因：低 signal/高 risk 线长期弱于 coverage_penalty/lowturn 线，继续占用强主题 cap 价值低。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom16_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn`；guard 注册后先报 `ashare_path4_emergent_theme 3/60 missing`，成功补齐命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal32_risk14_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `10.43% / 10.08% / 7.48% / 45.60% / 39.88%`，最大回撤 `-19.19% / -19.19% / -8.42% / -10.44% / -10.55%`，换手 `3.98x / 3.93x / 3.37x / 6.86x / 7.02x`；`90/10 equal_weight` CAGR `2.47% / 5.65% / 8.17% / 21.64% / 14.82%`；`90/10 total_mv` CAGR `5.91% / 6.60% / 5.66% / 21.01% / 17.32%`。
- 结论：risk14 恢复了短窗收益，但 2020/2023 稳定性仍弱于当前 Path 4 robust；持仓仍呈多票强势结构而非单票幸运。`update_weighted_winners.py` validation 拒绝，Path 4 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> emergent_theme_coverage`。下一轮第一候选建议只扩一次覆盖宽度并要求 2023 不继续失真：`aggr_13_87_prom18_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal32_prom18_ids>`；新增前按 robust 排名再淘汰一条弱 signal26 旧线。

## 本轮执行计划（2026-06-10 16:31 CST）

- 上一轮候选/结果摘要：上一轮 `signal32/risk14` 恢复短窗但 2020/2023 仍弱；本轮按 `emergent_theme_coverage` 扩到 `prom18`，继续保持独立 Path 4 强主题涌现口径，不使用人工主题标签、不纳入 ETF。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移除实际仍在 active 的旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap12_exit66`。evict 原因：旧 signal26/risk15 线长期弱于 coverage_penalty/lowturn 新线，且上一轮文档建议的 `signal26...risk20...` 已不在 active。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom18_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk14_cap08_exit62_lowturn`；guard 注册后报 `ashare_path4_emergent_theme 3/60 missing`，成功补齐命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal32_prom18_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `10.43% / 10.08% / 7.48% / 45.60% / 39.88%`，最大回撤最差 `-19.19%`，换手最高 `7.02x`；`90/10 equal_weight` CAGR `2.47% / 5.65% / 8.17% / 21.64% / 14.82%`；`90/10 total_mv` CAGR `5.91% / 6.60% / 5.66% / 21.01% / 17.32%`。
- 结论：prom18 没有改善 2020/2023 稳定性，且 90/10 equal_weight 长窗明显失真；持仓仍是多票强势结构（光模块、半导体、电力/能源等簇），不是单票幸运，但 `update_weighted_winners.py` validation 拒绝，Path 4 window winner、robust candidate 与 tracked payload 未改变。最终 guard 显示 Path4 signature changed，是 active/coverage 状态变化，不是 official robust 晋级。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> emergent_theme_coverage`。下一轮不要继续提高 signal32 覆盖，建议用更低 signal 门槛对照收益恢复：`aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal30_prom18_ids>`；新增前再淘汰 `signal26_leader72_coverage_penalty_risk12_cap10_exit64` 这条旧弱线。

## 本轮执行计划（2026-06-11 05:45 CST）

- 上一轮候选/结果摘要：上一轮 `signal32/prom18` 没有改善 2020/2023 稳定性；本轮按计划降低信号门槛到 `signal30/leader80`，继续保持独立 Path 4 强主题涌现口径，不使用人工主题标签、不纳入 ETF，也不并入 Path 2 扫描池。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移除旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64`。evict 原因：旧 signal26/leader72/cap10 线长期弱于 coverage_penalty/lowturn 新线，且不改善 robust。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`；成功补齐命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `10.43% / 10.08% / 7.48% / 45.60% / 39.88%`，最大回撤 `-19.19% / -19.19% / -8.42% / -10.44% / -10.55%`；`90/10 equal_weight` CAGR `2.47% / 5.65% / 8.17% / 21.64% / 14.82%`；`90/10 total_mv` CAGR `5.91% / 6.60% / 5.66% / 21.01% / 17.32%`。
- 结论：signal30/prom18 保持多票强势结构，但 2020/2023 收益仍弱，不是 official robust 晋级；`update_weighted_winners.py` 后 Path 4 window winner、robust candidate 与 tracked payload 未被本轮候选改写。最终 guard 显示 `ashare_path4_emergent_theme 60/60 complete`，rotation 为 `emergent_theme_coverage / continue`。
- 下一轮 focus：最终 guard 继续给出 `ashare_path4 -> emergent_theme_coverage`。下一轮不要再只重复 prom18，建议测试更宽晋升池是否能修复 2023：`aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal30_prom20_ids>`；新增前再按 robust 排名淘汰一条旧弱 signal26 线。

## 本轮执行计划（2026-06-11 16:10 CST）

- 上一轮候选/结果摘要：上一轮留下 `signal30/leader80/prom20/risk14/cap08/exit62`，本轮优先补齐该 Path 4 强主题涌现候选三底座五窗口覆盖；全程不使用人工主题标签、不纳入 ETF，也不并入 Path 2 扫描池。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移除旧弱线 `aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_risk15_cap12_exit66`。evict 原因：旧 signal26/leader72/cap12 线长期弱于 coverage_penalty/lowturn 新线，且不改善 robust。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`；成功补齐命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `10.14% / 9.65% / 7.28% / 43.07% / 32.95%`，最大回撤 `-19.19% / -19.19% / -8.42% / -10.44% / -10.55%`；`90/10 total_mv` CAGR `5.76% / 6.38% / 5.59% / 19.94% / 14.97%`；`90/10 equal_weight` CAGR `2.37% / 5.50% / 8.13% / 20.89% / 13.41%`。
- 结论：prom20 保持多票强势结构，近端持仓覆盖光模块、半导体、电力/能源等簇，不是单票幸运；但 2020/2023 稳定性明显不足，`update_weighted_winners.py` 后 Path 4 window winner、robust candidate 与 tracked payload 未改变。最终 guard 显示 `ashare_path4_emergent_theme 60/60 complete`。
- 下一轮 focus：最终 guard 仍给出 `ashare_path4 -> emergent_theme_coverage` 且状态为 `continue`。下一轮不要继续单纯提高 prom，建议用更宽覆盖但稍低信号门槛修复 2023：`aggr_13_87_prom20_emergent_theme_quality_gate_signal28_leader78_coverage_penalty_risk14_cap08_exit62_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal28_prom20_ids>`；新增前继续按 robust 排名淘汰一条旧弱 signal26 线。

## 本轮执行计划（2026-06-25 21:16 CST）

- 上一轮候选/结果摘要：本轮独立 Path 4 使用 `PATH4_THEME_DISCOVERY_BASE_IDS` × `PATH4_THEME_DISCOVERY_VARIANT_IDS` 的真实代码集合，新增 `prom22/signal29/leader78/risk08/cap06/exit64` 强主题涌现变体，不使用人工主题标签、不纳入 ETF、不经由 `path2_candidate_pass.py` 评价。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；移除 `aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk14_cap08_exit62_lowturn`。evict 原因：旧 prom18/signal30 线在稳健排名与近端弹性上均弱于 prom20/22 覆盖惩罚线。
- 本轮候选 ID 与命令：三底座 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap06_exit64_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap06_exit64_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk08_cap06_exit64_lowturn`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v46_ids>,<one_path3_id>,<three_path4_prom22_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `13.67% / 16.09% / 12.94% / 71.18% / 116.76%`，最大回撤 `-14.95% / -14.75% / -5.76% / -7.24% / -10.82%`，换手 `3.54x / 3.58x / 3.16x / 6.15x / 6.21x`；`90/10 total_mv` CAGR `6.54% / 8.11% / 6.34% / 28.40% / 48.64%`；`90/10 equal_weight` CAGR `3.24% / 5.42% / 7.83% / 21.44% / 9.98%`。
- 结论：80/20 total_mv 能捕捉强行业/强龙头短窗弹性，且不是单票幸运；但 2020/2023 稳定性仍不够，90/10 两个底座不足。`update_weighted_winners.py` 后 Path 4 2025 window winner 仍为 `...prom20...risk10_cap06_exit62_lowturn`，robust candidate 仍为 `...prom20...risk12_cap06_exit60_lowturn`，tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_risk_control`。下一轮第一候选建议只在 80/20 total_mv 与两个 90/10 对照上测试更低风险/更长 exit 的风险控制线：`aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom22_risk06_ids>`，新增前继续按 robust/窗口覆盖淘汰一条弱旧线。

## 本轮执行计划（2026-06-26 09:46 CST）

- 上一轮候选/结果摘要：上一轮 `prom22/signal29/leader78/risk08/cap06/exit64` 短窗弹性强但 2020/2023 稳定性不足；本轮按 `theme_risk_control` 继续降低风险阈值到 `risk06` 并放宽 exit 到 `66`，仍只使用 `PATH4_THEME_DISCOVERY_BASE_IDS × PATH4_THEME_DISCOVERY_VARIANT_IDS`，不使用人工主题标签、不纳入 ETF、不经由 Path 2 candidate pass。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；移除 `aggr_13_87_prom18_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk12_cap08_exit60_lowturn`。evict 原因：旧 prom18/signal30/cap08 线在 robust 排名、近端弹性和容量成本上均弱于 prom20/22 cap06 线。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap06_exit66_lowturn`；成功补齐命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom22_risk06_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `13.67% / 15.55% / 12.57% / 68.03% / 103.46%`，最大回撤 `-14.93% / -14.75% / -5.77% / -7.24% / -10.82%`，换手 `3.54x / 3.58x / 3.16x / 6.15x / 6.21x`；`90/10 total_mv` CAGR `6.54% / 8.10% / 6.33% / 28.40% / 48.64%`；`90/10 equal_weight` CAGR `3.24% / 5.42% / 7.84% / 21.44% / 9.98%`。
- 强主题捕捉检查：`80/20 total_mv` 近端持仓覆盖中船特气、芯碁微装、联瑞新材、长飞光纤、海光信息、源杰科技、寒武纪、中际旭创、新易盛、生益科技等，呈半导体/光模块/PCB/电力强势簇，不是单票幸运；但 90/10 两个底座仍弱，不能只按 2026 CAGR 晋级。
- 结论：`update_weighted_winners.py` 后 Path 4 window winner、robust candidate 与 tracked payload 未改变；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_capacity_cost`。下一轮第一候选建议在 risk06 上继续压容量并延后 exit：`aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn` 三底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom22_risk06_cap05_exit68_ids>`。

## 本轮执行计划（2026-06-26 20:46 CST）

- 上一轮候选/结果摘要：上一轮 `prom22/signal29/leader78/risk06/cap06/exit66` 的 80/20 total_mv 短窗弹性强但 90/10 两底座弱；本轮按 `theme_capacity_cost` 降 cap 到 `5%` 并延后 exit 到 `68`，继续保持独立 Path 4 强主题涌现口径，不使用人工主题标签、不纳入 ETF、不经由 Path 2 candidate pass。
- 本轮 active pool 处理：注册新 cap05 变体后 guard 报 `ashare_path4_emergent_theme 3/63 missing`，本轮按 `rerun_commands` 等价的三底座 `--only-base-ids` 补齐；未额外 evict，下一轮若继续扩变体需按 robust/窗口覆盖归档一条旧弱线。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 五窗口结果：`80/20 total_mv` 刷新到 `2026-06-26` 后 CAGR `11.83% / 13.16% / 14.89% / 58.11% / 90.39%`，最大回撤 `-13.57% / -13.57% / -10.66% / -6.30% / -10.14%`，换手 `3.15x / 3.22x / 2.95x / 5.50x / 5.51x`；`90/10 total_mv` CAGR `5.31% / 6.52% / 8.21% / 24.54% / 43.11%`；`90/10 equal_weight` CAGR `2.58% / 4.30% / 5.99% / 18.55% / 10.45%`。
- 强主题捕捉检查：80/20 total_mv 近端持仓继续集中在半导体、光模块、PCB、电力等市场自动涌现强势簇，含中船特气、芯碁微装、联瑞新材、长飞光纤、中际旭创、寒武纪等多票，不是单票幸运；但 90/10 两底座和 2020/2023 稳定性仍不足，不能只按短窗 CAGR 晋级。
- 结论：`update_weighted_winners.py` 后 Path 4 window winner、robust candidate 与 tracked payload 未改变；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_signal_quality`。下一轮第一候选建议在 cap05 线上提高信号质量而不继续单纯压 cap：`aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn` 三底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom22_signal30_cap05_ids>`。

## 本轮执行计划（2026-06-27 07:44 CST）

- 上一轮候选/结果摘要：上一轮 `prom22/signal29/leader78/risk06/cap05/exit68` 的 80/20 total_mv 仍有短窗弹性但 90/10 两底座弱；本轮按 `theme_signal_quality` 提高信号与龙头门槛，继续保持独立 Path 4 强主题涌现口径，不使用人工主题标签、不纳入 ETF、不经由 Path 2 candidate pass。
- 本轮 active pool 处理：移除 `aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap08_exit60_lowturn`。evict 原因：旧 prom12/cap08 线在 robust 排名、近端弹性和容量成本上均弱于 prom20/22 cap05/cap06 线。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `11.11% / 11.96% / 10.51% / 45.35% / 63.01%`，最大回撤 `-16.19% / -16.19% / -9.17% / -9.04% / -9.27%`；`90/10 total_mv` CAGR `4.76% / 5.64% / 4.28% / 15.26% / 17.28%`；`90/10 equal_weight` CAGR `2.28% / 4.52% / 5.02% / 14.31% / 11.73%`。
- 强主题捕捉检查：80/20 total_mv 近端持仓覆盖源杰科技、宏和科技、芯碁微装、联瑞新材、寒武纪、新易盛、中际旭创等多票强势簇，不是单票幸运；但 2020/2023 稳定性与两个 90/10 底座仍不足，不能按单一短窗 CAGR 晋级。
- 结论：`update_weighted_winners.py` 后 Path 4 window winner、robust candidate 与 tracked payload 均未改变；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_capacity_cost`。下一轮第一候选建议在 signal30/leader80 上继续压容量并延后 exit，而不继续提高信号门槛：`aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader80_coverage_penalty_risk06_cap04_exit70_lowturn` 三底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom22_signal30_cap04_exit70_ids>`。

## 本轮执行计划（2026-07-02 07:00 CST）

- 上一轮候选/结果摘要：上一轮建议 `signal30/cap04/exit70`，但本轮最终 focus 为 `emergent_theme_coverage`；因此改为 `prom26/signal32/leader82/risk08/cap04/exit56` 的强主题覆盖/容量组合，继续保持独立 Path 4，不使用人工主题标签、不纳入 ETF、不经由 Path 2 candidate pass。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；从 `PATH4_THEME_DISCOVERY_VARIANT_IDS` 移除 `aggr_13_87_prom18_emergent_theme_quality_gate_signal28_leader76_coverage_penalty_risk12_cap08_exit60_lowturn`。evict 原因：旧 prom18/signal28 线在 robust 排名与近端容量控制上弱于 prom20/prom22 线，继续占用强主题 active cap 价值低。
- 本轮候选 ID 与命令：三底座 `aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom26_emergent_theme_quality_gate_signal32_leader82_coverage_penalty_risk08_cap04_exit56_lowturn`。
- 五窗口结果：`80/20 total_mv` CAGR `6.80% / 6.72% / 6.59% / 36.72% / 34.33%`，最大回撤 `-14.58% / -14.58% / -6.39% / -7.52% / -7.40%`，换手 `2.43x / 2.45x / 2.28x / 4.26x / 4.55x`；`90/10 equal_weight` CAGR `2.47% / 4.03% / 3.72% / 10.44% / 5.49%`；`90/10 total_mv` CAGR `2.93% / 3.03% / 1.07% / 8.72% / 4.33%`。
- 强主题捕捉检查：`80/20 total_mv` 近端持仓覆盖源杰科技、蓝特光学、杰普特、宏和科技、腾景科技、联瑞新材、中际旭创、新易盛等多票自动涌现强势簇，偏光模块/半导体/PCB/通信链条，不是单票幸运；但 2020/2023 收益明显弱于 `prom20/signal29/risk12` robust。
- 结论：最终 guard 显示 `ashare_path4_emergent_theme 60/60 pass`。`update_weighted_winners.py` 后 Path 4 official candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`，mean CAGR `24.38%`、min CAGR `11.61%`；本轮 prom26 不改变 window winner、robust candidate 或 tracked payload。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> emergent_theme_coverage`。下一轮第一候选建议做 `prom24` 中间覆盖，而不是继续扩到更宽：`aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn` 三底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom24_signal31_cap05_ids>`；新增前继续按 robust/窗口覆盖淘汰一条旧弱 prom18 或 signal28 线。

## 本轮执行计划（2026-07-03 07:23 CST）

- 上一轮候选/结果摘要：上一轮留下 `prom24/signal31/leader80/risk10/cap05/exit58` 三底座中间覆盖；本轮按独立 Path 4 强主题涌现集合执行，不使用人工主题标签、不纳入 ETF、不经由 Path 2 candidate pass。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal31_leader80_coverage_penalty_risk10_cap05_exit58_lowturn`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <six_ashare_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `9.12% / 9.15% / 5.46% / 36.36% / 26.15%`，最大回撤 `-18.03% / -18.03% / -8.60% / -10.11% / -10.54%`，换手 `3.17x / 3.25x / 2.89x / 5.45x / 5.74x`；`90/10 equal_weight` CAGR `1.69% / 3.02% / 4.18% / 10.72% / 1.69%`；`90/10 total_mv` CAGR `3.94% / 4.20% / 2.43% / 11.83% / 2.09%`。
- 强主题捕捉检查：80/20 total_mv 近端仍能抓到多票自动涌现强势簇，偏光模块、半导体、PCB/通信链条，不是单票幸运；但两个 90/10 底座收益不足，且 2020/2023 稳定性仍弱于 `prom20/signal29/risk12` robust。
- 结论：`update_weighted_winners.py` 后 Path 4 tracked payload 有同步重写，80/20 total_mv prom24 可作为 target-viable fallback，但未形成干净 robust 晋级；本轮没有 Path 4 evict/归档。
- 下一轮 focus：如果继续 `emergent_theme_coverage`，不要再单纯扩 prom；第一候选改为 `theme_signal_quality` 回看 `prom20` robust 与 `prom24` 的差异，注册 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit60_lowturn`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_13_87_prom24_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap05_exit60_lowturn`；新增前仍需按 robust/窗口覆盖淘汰一条旧弱 prom18 或 signal28 线。

## 本轮执行计划（2026-07-07 05:01 CST）

- 上一轮候选/结果摘要：上一轮 prom24 中间覆盖未形成 robust 晋级；本轮按强主题 `theme_signal_quality`/开局候选执行 `prom22/signal30/leader78/risk06/cap05/exit68` 三底座，继续保持独立 Path 4，不使用人工主题标签、不纳入 ETF、不经由 Path2 candidate pass。
- 本轮 active pool 处理：Path 4 active 池维持 `60`；移除 `aggr_13_87_prom20_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk10_cap06_exit62_lowturn`。evict 原因：该旧线在 robust/窗口覆盖上弱于现役 `prom20/signal29/risk12` 与 `prom22/signal29/risk06`，且本轮需要为 signal30/risk06 让出三底座覆盖。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`、`core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`；补缺口命令同 Path1 合并为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <one_path1_id>,<three_path4_signal30_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `10.30% / 10.75% / 10.49% / 42.85% / 41.03%`，最大回撤 `-13.57% / -13.57% / -10.76% / -10.71% / -10.56%`，换手最高 `5.66x`；`90/10 total_mv` CAGR `4.81% / 5.25% / 5.55% / 16.28% / 20.42%`，回撤最低但收益弱；`90/10 equal_weight` CAGR `1.95% / 2.91% / 4.13% / 14.05% / -0.82%`，2026 转负。
- 强主题捕捉检查：80/20 total_mv 近端持仓覆盖生益科技、深南电路、圣邦股份、寒武纪、海光信息、新易盛、源杰科技、联芸科技等多票强势簇，能捕捉半导体/PCB/光模块链条，但不是单票幸运；由于 90/10 两底座弱且 2020/2023 仍低于 robust，不晋级。
- 结论：`update_weighted_winners.py` 后 Path 4 window winner、robust candidate 与 tracked payload 未改变，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk06_cap05_exit68_lowturn`。
- 下一轮 focus：最终 guard 给出 `ashare_path4 -> theme_risk_control`。下一轮不要继续提高 signal，建议注册/确认 `aggr_13_87_prom22_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk04_cap05_exit70_lowturn` 三底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_signal30_risk04_ids>`。
- Final guard 修正：最终 guard 显示 `ashare_path4 changed=true / continue / emergent_theme_coverage`，这是本轮 active/coverage 签名变化，不代表 official robust 晋级。下一轮不要直接改 official winner；首条命令改为注册一个覆盖中间线 `aggr_13_87_prom24_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk08_cap05_exit64_lowturn` 三底座并执行 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <three_path4_prom24_signal30_coverage_ids>`；新增前继续按 robust/窗口覆盖淘汰一条旧弱 prom18/signal28 线。
