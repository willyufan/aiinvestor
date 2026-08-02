# Path 1 研究计划

## 2026-08-03 二次迭代记录（07:18 CST）

### 上一轮候选与结果摘要

- `core_multifactor_coverage` 五窗口确认 profitability-signal risk18/risk14，并与主线 risk20 同窗比较。两条挑战者的 2020/2023/2026 CAGR 分别为 `9.65%/11.33%/-6.04%`、`9.44%/11.20%/-6.46%`，相对 risk20 的中窗降幅均超过 3pp，判定 `reject`。
- 主线 risk20 为 `23.44%/16.15%/-1.75%`，短窗仍负，只作 `robust_observation`：进入观察位，不是强稳定 winner。主线与 core_multifactor 均无 window winner/robust/tracked 变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803_iter2.json`。

### 下一轮 focus 提示

- guard 继续指向 `core_multifactor_coverage`。risk14/risk18 同形已证伪，下一轮改验 risk16 与 growth-trend-signal risk12，目标是把 2020/2023 CAGR 缺口压到 3pp 内；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### Focus 候选池

- `core_multifactor_coverage`：profitability-signal-risk16、growth-trend-signal-risk12；`signal_quality`：growth-signal-risk16、growth-trend-quality-gate-risk10。
- `holding_shape`：share20、share22；`satellite_risk_cost`：risk18、risk16；`weekly_exposure_path`：buffered、buffered-asym13。

## 2026-08-03 迭代记录（01:18 CST）

### 上一轮候选与结果摘要

- `holding_shape` 五窗口确认 share20/ramp66、share22/ramp64，并与 risk20 同端点比较。两条挑战者的 2020/2023/2026 CAGR 分别为 `17.09%/15.76%/-2.37%`、`17.02%/16.57%/-1.04%`；2020 CAGR 相对 risk20 均下降约 `6.4pp`，全部 `reject`。
- risk20 的 2020/2023/2026 CAGR 为 `23.44%/16.15%/-1.75%`，仍为 Path1 robust，但短窗为负，只作 `robust_observation`：进入观察位，不是强稳定 winner。window winner/robust/tracked 未改变，无 evict。
- `core_multifactor` 子段：代码方向组与 guard 覆盖仍为 `64/64`；winner-only 完成 132 个 fast-family 的同端点巡检。本轮作为 Path2 对照实跑的 quality-value-industry 五窗仍含负窗口，未形成 Path1 core_multifactor 晋级，下一轮改测更轻 signal-quality 组合。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard,core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803.json`。

### 下一轮 focus 提示

- 最终 guard 轮换为 `core_multifactor_coverage`。下一轮确认 profitability-signal 的 risk18/risk14 两档，并与 Path1 risk20 robust 同窗比较；只有 2020/2023 不触发护栏且 2026 明显收敛才保留。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### Focus 候选池

- `holding_shape`：share20/ramp66、share22/ramp64；`satellite_risk_cost`：risk16、risk20。
- `core_multifactor_coverage`：profitability-signal-risk18、profitability-signal-risk14；`signal_quality`：growth-trend-quality-gate-risk12、risk10。
- `weekly_exposure_path`：buffered、buffered-asym13。

## 2026-08-02 二次迭代记录（08:42 CST）

### 上一轮候选与结果摘要

- 在 08:12 首轮基础上二次确认 risk18、risk20 与 `holding_shape` share20/ramp66。三者 2020/2023/2026 CAGR 分别为 `21.65%/11.64%/-1.73%`、`23.44%/16.15%/-1.75%`、`17.12%/15.76%/-2.40%`；risk18 与 share20 破坏中窗或短窗仍负，均 `reject`，risk20 仍是 `robust_observation`：进入观察位，不是强稳定 winner。
- `core_multifactor` 子段复核首轮 risk16 结论与代码覆盖 `64/64`，本次没有追加同形扩参；risk16 仍 `reject`。window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802_iter2.json`。

### 下一轮 focus 提示

- 转 `holding_shape`，用 share22/ramp64 挑战 risk20；要求 2026 转正且 2020/2023 CAGR 缺口不超过 3pp。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard,core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### Focus 候选池

- `holding_shape`：share20/ramp66、share22/ramp64；`satellite_risk_cost`：risk16、risk20。
- `core_multifactor_coverage`：profitability-signal-risk18、profitability-signal-risk14；`signal_quality`：growth-trend-quality-gate-risk12、risk10。
- `weekly_exposure_path`：buffered、buffered-asym13。

## 2026-08-02 迭代记录（08:12 CST）

### 上一轮候选与结果摘要

- 主线按 `satellite_risk_cost` 五窗口确认 risk18 与 risk20。risk18 的 2020/2023/2026 CAGR 为 `21.65%/11.64%/-1.73%`，2023 相对 risk20 下降 `4.51pp`，触发稳定性护栏并 `reject`；risk20 为 `23.44%/16.15%/-1.75%`，仍因 2026 为负只判 `robust_observation`：进入观察位，不是强稳定 winner。
- `core_multifactor` 子段确认 quality-profitability-signal-risk16，2020/2023/2026 CAGR 为 `9.30%/11.37%/-6.25%`，中窗 CAGR/Sharpe 三项护栏命中，`reject`。假设“移除 growth 倾斜能缩小中窗缺口”未获支持；window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802.json`。

### 下一轮 focus 提示

- `satellite_risk_cost` 已再次证伪 risk18；下一轮优先轮到 `holding_shape`，比较 share20/ramp66、share22/ramp64 与 risk20，要求 2026 转正且 2020/2023 缺口均不超过 3pp。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard,core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### Focus 候选池

- `satellite_risk_cost`：risk16、risk20；`holding_shape`：share20/ramp66、share22/ramp64。
- `core_multifactor_coverage`：profitability-signal-risk18、profitability-signal-risk14；`signal_quality`：growth-trend-quality-gate-risk12、risk10。
- `weekly_exposure_path`：buffered、buffered-asym13。

## 2026-08-01 二次迭代记录（07:26 CST）

### 上一轮候选与结果摘要

- 主线同端点确认 `risk20`：2020/2023/2026 CAGR 为 `23.44%/16.15%/-1.75%`，短窗仍负，判定 `robust_observation`：进入观察位，不是强稳定 winner；window winner/robust/tracked 未改变。
- `core_multifactor` 子段确认 growth-signal risk16/risk14。两者 2020/2023/2026 CAGR 为 `9.67%/12.39%/-6.06%`、`9.54%/12.46%/-6.28%`，相对 risk20 的 2020 CAGR 下降约 `13.77pp/13.90pp`，均触发稳定性护栏并 `reject`。假设“简化到 growth-signal 可缩小中窗缺口”未获支持；无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk16_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk14_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260801_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 focus=`satellite_risk_cost / rotate`：停止 growth-signal risk16/risk14，回到 risk18 对 risk20 的卫星风险成本边界，要求 2026 转正且 2020/2023 缺口均不超过 3pp。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### Focus 候选池

- `signal_quality`：growth-trend-signal-gate-risk12、growth-trend-signal-gate-risk10。
- `core_multifactor_coverage`：profitability-signal-risk16、profitability-signal-risk14。
- `satellite_risk_cost`：risk18、risk20；`holding_shape`：share20/ramp66、share22/ramp64。
- `weekly_exposure_path`：buffered、buffered-asym13。

## 2026-08-01 迭代记录（01:20 CST）

### 上一轮候选与结果摘要

- 主线确认 risk20 与周度仓位 `buffered_asym13`。risk20 的 2020/2023/2026 CAGR 为 `23.44%/16.15%/-1.75%`，仍是 Path1 robust 组成，但短窗为负，判定 `robust_observation`：进入观察位，不是强稳定 winner；asym13 为 `15.12%/11.35%/0.61%`，相对 risk20 的 2020/2023 CAGR 下降 `8.32pp/4.80pp`，触发护栏，`reject`。
- `core_multifactor` 子段确认 growth-trend-risk08 与 value-lowvol-trend-risk20。两者 2020/2023/2026 CAGR 分别为 `6.54%/12.66%/-9.26%`、`-3.60%/13.07%/-10.79%`，均明显破坏中窗稳定性，`reject`。假设“降低风险档或加入价值低波可改善回撤而保住收益”未获支持；window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6_cash_off__port_weekly_exposure_buffered_asym13
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260801.json`。

### 下一轮 focus 提示

- focus=`core_multifactor_coverage`：停止本轮两条弱组合，转向较简洁的 profitability-signal risk16/risk14，目标是缩小 2020/2023 收益缺口而不重新放大回撤。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### Focus 候选池

- `core_multifactor_coverage`：profitability-signal-risk16、profitability-signal-risk14。
- `signal_quality`：growth-signal-risk16、growth-signal-risk14。
- `satellite_risk_cost`：risk18、risk20；`holding_shape`：share20/ramp66、share22/ramp64。
- `weekly_exposure_path`：buffered、buffered-asym13。

## 2026-07-31 迭代记录（07:55 CST）

### 上一轮候选与结果摘要

- 主线确认正式 risk20：2020/2023/2026 CAGR 为 `22.15%/14.32%/-9.74%`，判定 `robust_observation`，进入观察位，不是强稳定 winner；window winner、robust 与 tracked 未改变。
- `core_multifactor` 子段确认 quality-profitability-growth-lowvol-risk08 与 quality-profitability-growth-trend-risk10。相对 risk20，前者 2020/2023 CAGR 下降 `13.96pp/6.96pp`，后者下降 `16.99pp/1.90pp` 且 Sharpe 触发护栏，均 `reject`。实验假设“低波或趋势质量门改善中窗回撤”未获支持；无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk08_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk10_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### 下一轮 focus 提示

- focus=`core_multifactor_coverage`：改用 growth-trend risk08 与 value-lowvol-trend risk20，验证更低风险档能否修复 2020 CAGR 且不牺牲 2023。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm
```

### Focus 候选池

- `core_multifactor_coverage`：growth-trend-risk08、value-lowvol-trend-risk20。
- `signal_quality`：growth-lowvol-risk08、growth-trend-risk08。
- `satellite_risk_cost`：sat-three-stage-risk20、sat-three-stage-risk18。
- `holding_shape`：share20/ramp66、share22/ramp64。
- `weekly_exposure_path`：buffered、buffered-asym13。

## 2026-07-30 二次迭代记录（07:24 CST）

### 上一轮候选与结果摘要

- 主线按 `holding_shape` 五窗口确认 share22/ramp64、share24/ramp62，并与正式 robust risk20 同端点比较。两条 holding-shape 的 2020 CAGR 为 `18.01%/18.15%`，相对 risk20 的 `24.44%` 下降 `6.43pp/6.29pp`，触发稳定性护栏；但 2023 CAGR 均约 `18.5%`、2026 为 `7.34%/8.03%`，故只 `keep_watch`。risk20 五窗确认 `promote`；window winner、robust candidate 与 tracked payload 未改变，无 evict/archive。
- `core_multifactor` 子段：最终 guard 的代码实际覆盖为 `64/64`。本轮 27 个证券策略预算优先投向最终 focus 的 holding-shape 与其余路径最低实跑，没有把已有同步当成新增多因子实验；下一轮若 focus 转回 signal/core，再执行下方五窗口确认。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard,core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 仍为 `holding_shape / rotate`。share22/share24 的 2020 缺口已再次确认，下一轮只验证中间 share20/ramp66 与 risk20，不继续向更高 share 同形扩参。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

- `core_multifactor` 未实跑原因为本轮 focus 与预算分配；若 rotation 转回 signal/core，第一条确认命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk08_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。

### Focus 候选池

- `holding_shape`：share20/ramp66、share22/ramp64；`satellite_risk_cost`：risk16、risk20。
- `signal_quality/core_multifactor_coverage`：growth-lowvol-quality-gate-risk08、growth-trend-quality-gate-risk10；`weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`。

## 2026-07-30 迭代记录

### 上一轮候选与结果摘要

- 主线按 `satellite_risk_cost` 五窗口确认 `risk18_reconfirm` 与正式对照 `risk20_reconfirm`。risk18 的 2023 CAGR 为 `13.53%`，相对 risk20 的 `18.13%` 下降 `4.61pp`，触发稳定性护栏并 `reject`；risk20 五窗确认 `promote`。window winner、robust candidate 与 tracked payload 未因参数竞争改变，无 evict/archive。
- `core_multifactor` 子段：开局 guard 的代码实际覆盖仍为 `64/64`；本轮预算优先用于 satellite risk 边界，没有把既有多因子同步当成新增实验。上一轮 signal-quality 两条均已 `reject`，下一轮仅在 rotation 再指向时用完整五窗口确认。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730.json`。

### 下一轮 focus 提示

- 最终 guard 仍给出 `satellite_risk_cost / rotate`。risk18 已证实破坏 2023，下一轮回到较温和的 risk16 与 risk20 做终点确认；若 risk16 再触发 2023 护栏，则该邻域停止扩参。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### Focus 候选池

- `holding_shape`：`...share_22_78_hold_2_8_ramp64_cost_guard`、`...share_24_76_hold_2_8_ramp62_cost_guard`。
- `satellite_risk_cost`：`...risk16_reconfirm`、`...risk20_reconfirm`。
- `signal_quality` / `core_multifactor`：`...quality_profitability_growth_lowvol...risk08_reconfirm`、`...quality_profitability_growth_trend...risk10_reconfirm`。
- `weekly_exposure_path`：`...__port_weekly_exposure_buffered_asym13`、`...__port_weekly_exposure_buffered`。

## 2026-07-29 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- 五窗口确认 `...quality_profitability_growth_lowvol...risk08_reconfirm` 与 `...quality_profitability_growth_trend...risk10_reconfirm`：两者在 `since_2020_01`/`since_2023_01` 相对当前 `risk20_reconfirm` 分别明显失速，且 `since_2026_01` 为负，均判定 `reject`。
- 当前对照 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 完成确认，判定 `promote`；window winner、robust candidate 与 tracked payload 未变化。
- `core_multifactor` 子组覆盖保持 `64/64`；本轮两个 signal-quality 多因子变体均未通过稳定性护栏。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk08_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk10_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260729_iter2.json`。

### 下一轮 focus 提示

- focus：`satellite_risk_cost`。优先确认 `risk18_reconfirm` 对 `risk20_reconfirm` 的回撤/收益取舍。
- 第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm
```

### Focus 候选池

- `signal_quality` / `core_multifactor`：`...quality_profitability_growth_lowvol...risk08_reconfirm`、`...quality_profitability_growth_trend...risk10_reconfirm`。
- `satellite_risk_cost`：`...sat_three_stage_buffered_cost_guard_risk18_reconfirm`、`...sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- `holding_shape`：`...holding_shape_share22_reconfirm`、`...holding_shape_share24_reconfirm`。
- `weekly_exposure_path`：`...__port_weekly_exposure_buffered`、`...__port_weekly_exposure_buffered_asym13`。

## 2026-07-29 迭代记录

### 上一轮候选与结果摘要

- 主线五窗口确认 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6_cash_off__port_weekly_exposure_buffered_asym13` 与正式 robust risk20。周度仓位 asym13 的 2020/2023 CAGR 相对 robust 下降 `8.70pp/4.95pp`，虽 2026 CAGR `11.20%`、winner-only 在 2017/2025 raw 排名领先，仍判定 `keep_watch`；相邻验证未通过，official window winner/robust/tracked 不变。risk20 2026 CAGR `9.27%`，五窗确认 `promote`。
- core_multifactor 子段：代码实际覆盖 `64/64`。新确认 `quality_profitability_growth_trend_signal_quality_gate_cashguard_risk12_reconfirm`，2020 CAGR/Sharpe 相对 risk20 分别下降 `18.03pp/0.475`，2026 CAGR `-4.23%`，判定 `reject`；实验假设“质量门槛可修复中窗且控制风险”不成立。无新增注册、无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk12_reconfirm`、`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6_cash_off__port_weekly_exposure_buffered_asym13`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- 五窗口增量命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk12_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6_cash_off__port_weekly_exposure_buffered_asym13,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260729.json`。

### 下一轮 focus 提示

- guard focus 为 `signal_quality`。risk12 quality-gate 已证伪，下一轮先确认较低风险的 growth/lowvol quality-gate 是否能缩小 2020 缺口；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk08_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。只有 2020/2023 均不触发护栏才继续；asym13 保留观察，不按 raw 单窗排名晋级。

### Focus 候选池

- `signal_quality/core_multifactor_coverage`：growth-lowvol-quality-gate-risk08、growth-trend-quality-gate-risk10；`holding_shape`：share22/ramp64、share24/ramp62；`satellite_risk_cost`：risk18、risk20；`weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`。

## 2026-07-28 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- 主线按 `holding_shape` 五窗口确认 share20/ramp66、share24/ramp62，并与正式 robust risk20 同窗比较。share20/share24 的 2020 CAGR 为 `19.71%/19.79%`，相对 robust `26.00%` 下降约 `6.29pp/6.21pp`；但 2023 CAGR 为 `20.75%/21.45%`，2026 为 `20.62%/23.80%`，且 share24 继续保留 2025-window artifact winner。两条均判定 `keep_watch`，不因单一 2025 窗口晋级；risk20 五窗口确认 `promote`。
- core_multifactor 子段：代码实际覆盖 `64/64`。确认 `quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`，其 2020 CAGR `-3.49%`、相对 risk20 下降约 `29.49pp`，判定 `reject`；多因子叠加未修复中窗。window winner/robust/tracked 未变化，无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard`、`...share_24_76_hold_2_8_ramp62_cost_guard`、risk20 robust，以及 core_multifactor `...quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard,core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728_iter2.json`。

### 下一轮 focus 提示

- 最终 guard focus 为 `core_multifactor_coverage`。本轮 risk20 多因子同形已证伪，下一轮转 growth/trend quality-gate risk12 与正式 robust 比较；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk12_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。

### Focus 候选池

- `holding_shape`：share18/ramp68、share22/ramp64；`satellite_risk_cost`：risk18、risk20；`signal_quality/core_multifactor_coverage`：quality-profitability-growth-quality-gate-risk12、quality-growth-signal；`weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`。

## 2026-07-28 迭代记录

### 上一轮候选与结果摘要

- 主线五窗口确认 `risk25/risk20/risk16_reconfirm`。risk25 的 2020/2023 CAGR 为 `25.14%/20.37%`，相对正式 robust risk20 低 `0.85pp/0.64pp`，风险上沿没有换来更好收益，判定 `keep_watch`；risk16 的 2023 CAGR 低 `4.55pp`，判定 `keep_watch`。risk20 五窗口确认 `promote`，window winner/robust/tracked 未变化，无 evict。
- core_multifactor 子段：代码实际覆盖仍为 `64/64`，本轮预算优先投向 rotation 的 `satellite_risk_cost`，没有新增多因子实跑；上一轮两条纯质量多因子已 `reject`。下一轮先转 `holding_shape`，避免继续同形 risk 参数。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`、`...risk20_reconfirm`、`...risk16_reconfirm`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728.json`。

### 下一轮 focus 提示

- 最终 focus 为 `holding_shape`。下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard,core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`，验证较平滑持仓是否能保住 2020/2023 并降低回撤。

### Focus 候选池

- `holding_shape`：share20/ramp66、share24/ramp62；`satellite_risk_cost`：risk25、risk20；`signal_quality/core_multifactor_coverage`：quality-profitability-signal、quality-growth-signal；`weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`。

## 2026-07-27 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 主线：正式 robust `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 五窗口同端点确认，2017/2020/2023/2026 CAGR 为 `20.03%/26.00%/21.00%/19.02%`，判定 `promote`；window winner/robust/tracked 未变化，无 evict。
- core_multifactor 子段：`quality_profitability_signal_cost_guard_reconfirm` 的 2020/2023 CAGR 为 `-3.47%/17.69%`，相对正式 robust 下降 `29.47pp/3.31pp`；equal-weight `quality_growth_signal_reconfirm` 的 2020 CAGR `-2.47%`、2026 CAGR `-6.44%`。两条均触发稳定性护栏并 `reject`；“纯质量信号修复中窗且降成本”的假设不成立。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm`、正式 robust `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727_iter2.json`。

### 下一轮 focus 提示

- 当前 rotation focus 为 `satellite_risk_cost`。纯质量多因子两条已证伪，下一轮先确认 risk25 风险上沿能否在不扩大回撤/换手的前提下改善 2023；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。

### Focus 候选池

- `satellite_risk_cost`：risk25、risk20；`signal_quality/core_multifactor_coverage`：quality-profitability-signal、quality-growth-signal；`holding_shape`：share18、share20；`weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`。

## 2026-07-27 迭代记录

### 上一轮候选与结果摘要

- 主线确认 `core_explore_80_20_total_mv_winner_core__share_18_82_hold_2_8_ramp68_cost_guard`：假设是降低核心仓位并延长持有可改善 2023/短窗；实际 2020/2023/2026 CAGR 为 `19.50%/20.59%/18.58%`，相对正式 robust 的 2020 CAGR 低 `6.49pp`，触发稳定性护栏，仅 `keep_watch`。正式 robust `...sat_three_stage_buffered_cost_guard_risk20_reconfirm` 同端点确认 `promote`，window winner/robust/tracked 未改变。
- core_multifactor 子段确认 `...quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`：假设是 value/lowvol/trend 与 cashguard 能修复此前质量组合的中窗；实际 2020 CAGR `-3.49%`、2023 CAGR `15.61%`，相对 robust 分别低 `29.49pp/5.39pp`，假设不成立，`reject`。本轮无新增注册、无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`、`core_explore_80_20_total_mv_winner_core__share_18_82_hold_2_8_ramp68_cost_guard`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__share_18_82_hold_2_8_ramp68_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727.json`。

### 下一轮 focus 提示

- 最终 focus 为 `signal_quality`。停止 value/lowvol/trend 同形扩参，下一轮重新比较两个已注册的纯质量信号边界与正式 robust；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。

### Focus 候选池

- `signal_quality/core_multifactor_coverage`：`...quality_profitability_signal_cost_guard_reconfirm`、`...quality_growth_signal_reconfirm`；`holding_shape`：share18、share20；`satellite_risk_cost`：risk20、risk25；`weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`。

## 2026-07-26 二次迭代记录（07:19 CST）

### 上一轮候选与结果摘要

- 主线本轮未新增实跑：预算优先补上轮明确欠缺的 `core_multifactor_coverage`；正式 robust 仍为 `...risk20_reconfirm`，window winner/robust/tracked 未改变。core_multifactor 子段五窗口确认 `quality_profitability_signal_cost_guard_reconfirm` 与 `growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`，两者相对 risk20 的 2020 CAGR 分别下降约 `29.5pp/17.9pp`，且均触发中窗护栏，判定 `reject`。实验假设“质量/趋势门槛改善多窗口稳定性”未获支持，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 仍为 `core_multifactor_coverage`。本轮两条质量信号边界均失败，下一轮改用 value/lowvol/trend/cashguard 风险20组合挑战正式 robust；主线 share18 放入随后确认队列。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。

### Focus 候选池

- `core_multifactor_coverage/signal_quality`：`quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`、正式 robust `risk20_reconfirm`；`holding_shape`：share18、share20；`satellite_risk_cost`：risk25、risk20。

## 2026-07-26 迭代记录

### 上一轮候选与结果摘要

- 主线按 `holding_shape` 五窗口确认 `share24/share22`，并以正式 robust `...risk20_reconfirm` 同端点比较。`share24` 的 2025/2026 CAGR 为 `68.87%/23.80%`、2020 CAGR 比 robust 低 `6.21pp`，判定 `keep_watch`；`share22` 的 2020 CAGR 低 `6.36pp` 且短窗不优于 share24，判定 `reject`；`risk20` 五窗全正，确认 `promote`。2025 window winner 仍为 share24，robust/tracked 未改变，无 evict。
- core_multifactor 子段本轮没有新增回测：首轮 guard 确认代码实际集合 `64/64` 五窗口覆盖完整，新增预算用于本轮 rotation 指向的 holding-shape、Path2/3/4/5 与 HK Path1-7；不得以主线同步替代 core_multifactor 实验结论。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`、`core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard,core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `core_multifactor_coverage`。第一条确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`；本轮未跑原因是 29 个证券策略预算已按 rotation 分配，且 core coverage 无 blocking。
- `holding_shape` 不再向 share22/share24 同形扩参；后续用 share18 与 risk20 检查 fast-pass 给出的 2023 优势能否通过 2020 稳定性护栏。

### Focus 候选池

- `core_multifactor_coverage`：`quality_profitability_signal_cost_guard_reconfirm`、`growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`；`signal_quality`：同两条质量信号边界候选。
- `satellite_risk_cost`：`risk25_reconfirm`、`risk20_reconfirm`；`holding_shape`：`share_18_82_hold_2_8_ramp68_cost_guard`、`share_20_80_hold_2_8_ramp66_cost_guard`。

## 2026-07-25 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 主线按 `satellite_risk_cost` 五窗口确认 `risk25/risk20/risk16`。`risk20` 继续以 2017/2020/2023 CAGR `20.03%/26.00%/21.00%` 确认 incumbent，判定 `promote`；`risk25` 未触发硬护栏，但 2020/2023 CAGR 分别低 `0.85pp/0.64pp` 且换手略高，判定 `keep_watch`；`risk16` 的 2023 CAGR 低 `4.55pp`，判定 `reject`。window winner/robust/tracked 未改变，无 evict。
- core_multifactor 子段本轮没有新增回测：初始 guard 已确认代码实际集合 `64/64` 五窗口覆盖完整，本轮 rotation 明确指向 `satellite_risk_cost`，预算用于主线风险边界与其余 11 条任务路径；不得用主线结果替代 core_multifactor 结论。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`、`...risk20_reconfirm`、`...risk16_reconfirm`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260725_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `holding_shape`；主线停止向更低风险同形扩参，下一轮用 share24/share22 与 incumbent 检查 2020 稳定性修复。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard,core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- core_multifactor 下一条确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`。

### Focus 候选池

- `satellite_risk_cost`：`risk30_reconfirm`、`risk20_reconfirm`；`signal_quality/core_multifactor_coverage`：`quality_profitability_signal_cost_guard_reconfirm`、`growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`。
- `holding_shape`：`share_24_76_hold_2_8_ramp62_cost_guard`、`share_22_78_hold_2_8_ramp64_cost_guard`；`weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`。

## 2026-07-25 迭代记录

### 上一轮候选与结果摘要

- 主线：本轮没有新增主线参数，按统一 scorecard 继续以 `...sat_three_stage_buffered_cost_guard_risk20_reconfirm` 为 current robust；主线 window winner、robust 与 tracked 均未改变，无 evict。
- core_multifactor：五窗口确认 `...quality_growth_signal_reconfirm` 与 `...quality_profitability_signal_cost_guard_reconfirm`。两者 2020 CAGR 为 `-2.47%/-3.47%`，相对 robust 下降 `28.47pp/29.47pp`；第一条 2026 CAGR `-6.44%`，第二条虽为 `2.03%`，仍破坏 2020/2023 稳定性。实验假设不成立，均 `reject`。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`。
- 主确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`；为统一 `2026-07-24` 终点，对第二条执行了同参数增量补齐。

- stale 修复：对上述全部候选把同一 `--only-base-ids` 命令的 `--end-date` 改为 `2026-07-24` 后完成五窗增量复跑；最终 scorecard、strategy JSON 与 live valuation 均采用该终点。

### 下一轮 focus 提示

- 最终 guard 为 `satellite_risk_cost`：用风险上沿与 incumbent 做边界复核；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。

### Focus 候选池

- `signal_quality`：`...core_multifactor_quality_profitability_signal_cost_guard_reconfirm`、`...core_multifactor_quality_growth_signal_reconfirm`；`core_multifactor_coverage`：同两条作为失败边界。
- `satellite_risk_cost`：`...sat_three_stage_buffered_cost_guard_risk20_reconfirm`、`...risk25_reconfirm`；`holding_shape`：`...share_24_76_hold_2_8_ramp62_cost_guard`、`...share_22_78_hold_2_8_ramp64_cost_guard`。
- `weekly_exposure_path`：`...__port_weekly_exposure_buffered`、`...__port_weekly_exposure_buffered_asym13`。

## 2026-07-24 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 上一轮 holding-shape 的 `share20/share22` 为 `reject`，`share24` 仅 `keep_watch`；本轮按 `core_multifactor_coverage` 五窗口确认两条等权多因子候选，并继续与主线 robust `...sat_three_stage_buffered_cost_guard_risk20_reconfirm` 同窗比较。
- `...core_multifactor_quality_growth_signal_reconfirm` 与 `...quality_profitability_value_lowvol_trend_cost_guard_reconfirm` 的 2020 CAGR 分别为 `-2.22%/-2.69%`，相对 robust 下降约 `28.78pp/29.24pp`，且 2026 CAGR 为 `-4.22%/-12.48%`；假设未获支持，两条均 `reject`。Path1 主线、core_multifactor robust、window winner 与 tracked 均未改写，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm`、`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`。

### 下一轮 focus 提示

- 最终 guard 轮换到 `signal_quality`；停止继续扩展同形等权低波组合，下一轮先对质量成长与盈利质量信号做边界确认。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`。

### Focus 候选池

- `core_multifactor_coverage`：`...core_multifactor_quality_growth_signal_reconfirm`、`...core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`（只作失败对照，不再同形扩参）。
- `signal_quality`：`...core_multifactor_quality_growth_signal_reconfirm`、`...core_multifactor_quality_profitability_signal_cost_guard_reconfirm`。
- `holding_shape`：`...share_24_76_hold_2_8_ramp62_cost_guard`、`...share_22_78_hold_2_8_ramp64_cost_guard`。
- `satellite_risk_cost`：`...sat_three_stage_buffered_cost_guard_risk25_reconfirm`、`...sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- `weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`。

## 2026-07-24 收尾记录

### 上一轮候选与结果摘要

- 主线围绕 `holding_shape` 五窗口确认 `share20/share22/share24`。相对 robust `...risk20_reconfirm`，三者都把 2020 CAGR 降低超过 `6pp`，触发稳定性护栏；`share20/share22` 判 `reject`，`share24` 虽成为 2025-window winner（CAGR `71.66%`、MaxDD `-24.17%`），仍只判 `keep_watch`，不进入正式 promote。
- core_multifactor 子段本轮仅复核上一轮结果，没有用同步替代实验；日更实跑预算优先给 holding shape、Path2/3/4/5 与 HK。下一轮先确认 `quality_growth_signal_reconfirm`，当前 Path1 robust/tracked 仍为 `...risk20_reconfirm`。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`、`core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard`、`core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp62_cost_guard_reconfirm,core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard,core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`。

### 下一轮 focus 提示

- 最终 focus 为 `core_multifactor_coverage`；首条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`。
- holding-shape 暂停新增；`share24` 只有修复 2020 CAGR 缺口后才可重新申请晋级。

### Focus 候选池

- `holding_shape`：`...share_24_76_hold_2_8_ramp62_cost_guard`、`...share_22_78_hold_2_8_ramp64_cost_guard`。
- `core_multifactor_coverage`：`...core_multifactor_quality_growth_signal_reconfirm`、`...core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`。

## 2026-07-23 收尾记录

### 上一轮候选与结果摘要

- 上一轮两个 lowvol core_multifactor 已归档；本轮转向 guard 的 `satellite_risk_cost`，五窗口确认 `risk20/risk18`，并用 growth-trend `risk08` 检查 core_multifactor 中窗修复。`risk20` 继续作为 Path1 incumbent，2020/2023 CAGR `27.06%/22.60%`，判定 `promote`（确认 incumbent）；`risk18` 的 2023 CAGR 低 `4.77pp`，判定 `reject`。
- core_multifactor 子段：`growth_trend...risk08` 的 2020 CAGR 仅 `8.85%`，比 `risk20` 低 `18.21pp`；MaxDD 虽较浅，但 CAGR/Sharpe 触发护栏，判定 `reject`。Path1 main/core_multifactor 均未产生新的 robust 替换。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`、`...risk18_reconfirm`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`。

### 下一轮 focus 提示

- `satellite_risk_cost` 不再继续向低 risk 扩参，第一条命令改为确认风险上沿能否提升 2023 且不扩大回撤：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。

### Focus 候选池

- `satellite_risk_cost`：`risk25_reconfirm`、`risk20_reconfirm`；`core_multifactor_coverage`：`growth_trend...risk10_reconfirm`、`growth_lowvol...risk08_reconfirm`；`weekly_exposure_path`：`__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`；`holding_shape`：`share_22_78_hold_2_8_ramp64_cost_guard`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260723.json`。

## 2026-07-22 收尾记录

- 上一轮候选与结果摘要：上一轮 `risk18/risk16` 只留观察、多因子 `risk09_v5` 淘汰；本轮按 `core_multifactor_coverage` 五窗口确认 `risk07_v4/risk06_v2`。两条相对主线 robust `risk20_reconfirm` 的 2020 CAGR 分别低约 `16.19pp/16.42pp`，2023 低约 `7.64pp/9.35pp`，虽 MaxDD 改善约 `7.5pp-8.5pp`，仍触发 CAGR/Sharpe 护栏，均判 `archive`。Path1 主线 winner/robust 未变。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk07_reconfirm_v4`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm_v2`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk07_reconfirm_v4,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm_v2`。
- core_multifactor 子段：两条弱 lowvol 变体已从 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 移除，定义和历史结果保留；代码实际 coverage 由 `66` 降为 `64`，仍高于 direction 最低要求。`winner_only_pass.py` 的 clear 信号已交由 weighted 相邻验证，official Path1 winner/robust 未改写。
- 下一轮 focus 提示：停止继续下调同形 risk 暴露，改查质量成长/趋势组合。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`。
- Focus 候选池：`core_multifactor_coverage` -> `growth_trend...risk08_reconfirm`、`growth_lowvol...risk08_reconfirm`；`signal_quality` -> `quality_profitability_growth_trend...risk08`、`quality_profitability_signal...risk14`；`satellite_risk_cost` -> `risk20_reconfirm`、`risk18_reconfirm`；`weekly_exposure_path` -> `__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`；`holding_shape` -> `share_22_78_hold_2_8_ramp64_cost_guard`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`。完整 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260722.json`。

## 2026-07-21 收尾记录

- 上一轮候选与结果摘要：上一轮 core_multifactor 新候选均 `reject`；本轮按 `core_multifactor_coverage` 同窗确认卫星风险 `risk18/risk16` 与多因子 `risk09_v5`，全部覆盖 `since_2017_01/since_2020_01/since_2023_01/since_2025_01/since_2026_01`。主线与 core_multifactor 仍属于同一 Path1，未混入独立 Path4。
- 本轮候选 ID 与命令：实跑 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`。
- Scorecard 与判定：`risk18/risk16` 的 2020 CAGR 约 `23.49%/23.46%`，但 2023 相对 `risk20` 低 `4.69pp/4.54pp`；`risk18` 虽进入 2017 窗口排序首位，仍只 `keep_watch`，`risk16` 被 artifact 推到 robust 后判定 `robust_observation`：进入观察位，不是强稳定 winner。core_multifactor `risk09_v5` 的 2020/2023 CAGR 仅 `7.52%/13.25%`、2026 `-8.48%`，判定 `reject` 并从 fast-pass direction/active 移除。实验假设均未获跨窗支持。
- core_multifactor 子段：代码实际 coverage 继续由 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 返回集合决定；本轮只淘汰 `risk09_v5`，下一轮不扩展同形 lowvol 组合。
- 下一轮 focus 提示：最终 guard 为 `core_multifactor_coverage`；先确认保留的 `risk07_v4/risk06_v2`，观察条件是 2020/2023 CAGR 不得再低于 `risk20` 超过 3pp。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk07_reconfirm_v4,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm_v2`。
- Focus 候选池：`core_multifactor_coverage` -> `risk07_reconfirm_v4`、`risk06_reconfirm_v2`；`signal_quality` -> `growth_trend...risk08_reconfirm`、`growth_lowvol...risk07_reconfirm_v4`；`satellite_risk_cost` -> `risk18_reconfirm`、`risk16_reconfirm`；`weekly_exposure_path` -> `__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`；`holding_shape` -> `share_22_78_hold_2_8_ramp64_cost_guard_reconfirm`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`。
- evict/归档：core_multifactor `risk09_v5` 从 active 移除但保留定义与历史结果；`risk18/risk16` 留 watch。完整 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260721.json`。

## 2026-07-20 收尾记录

- 上一轮候选与结果摘要：上一轮多因子低波质量线未挑战 `risk20_reconfirm`；本轮先把 incumbent 刷新到同一 `2026-07-17` 端点，再按 `signal_quality` 新增两条动量/质量多因子候选。Path1 主线未新增变体，core_multifactor 仍只是 Path1 direction group。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality_growth_signal_gate_cashguard_risk14_v7`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality_industry_signal_gate_cashguard_risk18_v8`；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality_growth_signal_gate_cashguard_risk14_v7,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_momentum_quality_industry_signal_gate_cashguard_risk18_v8`。
- Scorecard 与判定：相对 `risk20_reconfirm`，v7 的 2020/2023 CAGR 低 `16.66pp/5.98pp`、2020 Sharpe 低 `0.422`；v8 分别低 `17.14pp/5.91pp`、2020 Sharpe 低 `0.438`，且 2026 CAGR `-3.65%`。两者假设均未获支持，判定 `reject`，已从 fast-pass active 恢复为原 risk07/risk06 两条覆盖项；winner/robust/tracked 不应改变。
- core_multifactor 子段：代码覆盖仍以 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 为准；新定义保留供历史复算，但不再参与 active 排名。主线 incumbent 同端点复跑只作 comparator，不算新增实验。
- 下一轮 focus 提示：最终 guard 已轮换到 `satellite_risk_cost`；先复核卫星风险成本邻域，不再扩大单纯 momentum 权重。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`。
- Focus 候选池：`signal_quality` -> `...risk09_reconfirm_v5`、`...quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；`core_multifactor_coverage` -> `...risk07_reconfirm_v4`、`...risk06_reconfirm_v2`；`satellite_risk_cost` -> `risk18_reconfirm`、`risk16_reconfirm`；`weekly_exposure_path` -> `__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`；`holding_shape` -> `share_22_78_hold_2_8_ramp64_cost_guard_reconfirm`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`。
- evict/归档：v7/v8 从 active 移除，定义与五窗口结果保留；完整 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260720.json`。

## 2026-07-19 收尾记录

- 上一轮候选与结果摘要：上一轮只保留 core_multifactor 信号质量候选设计；本轮五窗口实跑 `quality46...risk08_v6`，并额外确认正式 incumbent `risk20_reconfirm` 与恢复 active 的 `quality_profitability...risk06_reconfirm_v2`。`risk20_reconfirm` 在 2020/2023 CAGR 为 `26.35%/21.87%`，确认继续作为 Path1 winner；主线没有被独立 Path4 或月选周控混入。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality46_growth_lowvol_signal_quality_gate_cashguard_risk08_v6`，确认 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`、`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm_v2`；均使用 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述具体 IDs>` 增量回测。
- Scorecard 与判定：`quality46...risk08_v6` 相对 `risk20_reconfirm` 的 2020/2023 CAGR 分别低 `18.39pp/8.20pp`，2020 Sharpe 低 `0.485`，判定 `reject` 并移出 fast-pass active；恢复对照 `risk06_reconfirm_v2` 2020 CAGR 仅 `9.02%`，判定 `reject`。`risk20_reconfirm` 确认结果判定 `promote`（保留 incumbent，不是新增换位）。artifact 曾因无 current incumbent 行误写新多因子为 2017 winner，补跑后已纠正；最终 Path1 winner/robust 回到 `risk20_reconfirm`。
- core_multifactor 子段：本轮覆盖由代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 决定；新增 v6 未通过稳定性护栏，旧 `risk06_reconfirm_v2` 恢复 active 仅用于保持方向覆盖，不等同独立 Path4。
- 下一轮 focus 提示：最终 guard 为 `core_multifactor_coverage`。第一条可执行命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`；目标是确认中等风险是否能缩小 2020/2023 CAGR 差距。
- Focus 候选池：`core_multifactor_coverage` -> `...risk09_reconfirm_v5`、`...risk07_reconfirm_v4`；`satellite_risk_cost` -> `risk18_reconfirm`、`risk16_reconfirm`；`weekly_exposure_path` -> `__port_weekly_exposure_buffered`、`__port_weekly_exposure_buffered_asym13`；`holding_shape` -> `share_22_78_hold_2_8_ramp64_cost_guard_reconfirm`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`。
- evict/归档：新 v6 从 Path1 active 移除但保留历史结果；没有物理删除 snapshot。scorecard 见 `results/research/a_share/research_iteration_20260719_scorecards.json`。

## 2026-07-09 收尾记录

- 上一轮候选与结果摘要：上一轮 Path1 `risk16/risk18` 已完成 satellite defense 晋级复核；本轮开局 guard 显示 Path1 fast family `136/136`、core_multifactor `67/67` 完整。Path1 主线与 core_multifactor 本轮只做巡检、winner/tracked 同步和下一轮候选设计，没有新增 `--only-base-ids` 实跑，也没有把独立 Path4 `emergent_theme` 或月选周控 overlay 写成 core_multifactor。
- 本轮候选 ID 与命令：本轮未实跑 Path1，原因是 A股新增确认预算优先给 Path2 `v79_medium_cycle_repair`、独立 Path4 `prom24/risk04` 三底座和 Path5 event entry；本轮实际 A股命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path2_v79_two_ids>,<path4_prom24_three_ids>`。Path1 下一条确认命令保留为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`。
- Scorecard 与判定：本轮 Path1 无新增 scorecard；`scripts/update_weighted_winners.py` 后 Path1 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`，Path1 主线判定 `keep_watch`，core_multifactor 子段判定 `keep_watch`。未实跑候选不能用于 promote 或 winner 改写。
- 下一轮 focus 提示：最终 guard 轮换到 `signal_quality`。下一轮第一条命令仍用 core_multifactor 的 signal-quality gate 低波质量门槛中风险恢复来测试 2020/2023 稳定性；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`，并归档一条非 winner/robust 旧低波线。
- Focus 候选池：`core_multifactor_coverage` -> `aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`、`aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；`satellite_risk_cost` -> `risk14_reconfirm`、`risk12_reconfirm`；`weekly_exposure_path` -> `__port_weekly_exposure_buffered_asym13`、`__port_weekly_exposure_buffered`；`holding_shape` -> `share_22_78_hold_2_8_ramp64_cost_guard_reconfirm`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`。
- evict/归档：本轮 Path1 无 evict；scorecard 总表见 `results/research/a_share/research_iteration_20260709_scorecards.json`。

## 2026-07-08 收尾记录

- 上一轮候选与结果摘要：上一轮 Path1 只有候选设计；本轮按 `satellite_risk_cost` 实跑 `risk18_reconfirm` 与 `risk16_reconfirm`，core_multifactor 只做覆盖巡检（guard 口径完整），没有把独立 Path4 `emergent_theme` 或 Path1 月选周控 overlay 误并入 core_multifactor。
- 本轮候选 ID 与命令：实跑 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm,<path2_v78_two_ids>,<path4_prom23_three_ids>`。
- Scorecard 与判定：相对 `risk20_reconfirm`，`risk16_reconfirm` 在 2020/2023 CAGR `28.51% / 24.02%`、MaxDD `-14.54% / -17.45%`、turnover `3.35x / 3.37x`，稳定性未破坏并成为 Path1 robust candidate，判定 `promote`；`risk18_reconfirm` 在 2020/2023 CAGR `28.54% / 23.86%`、MaxDD `-14.54% / -17.92%`，成为 2017 window winner，判定 `promote` 但不是 robust candidate。core_multifactor 本轮没有新增确认回测，判定 `keep_watch`。
- 下一轮 focus 提示：最终 guard 给 `core_multifactor_coverage`，下一轮第一条命令转回多因子低波质量线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 并归档一条非 winner/robust 旧低波线。
- Focus 候选池：`core_multifactor_coverage` -> `aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`、`aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；`satellite_risk_cost` -> `risk14_reconfirm`、`risk12_reconfirm`；`weekly_exposure_path` -> `__port_weekly_exposure_buffered_asym13`、`__port_weekly_exposure_buffered`；`holding_shape` -> `share_22_78_hold_2_8_ramp64_cost_guard_reconfirm`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`。
- evict/归档：本轮 Path1 无 evict；Path1 official/robust/tracked payload 已由 `scripts/update_weighted_winners.py` 同步，scorecard 详见 `results/research/a_share/research_iteration_20260708_scorecards.json`。

## 2026-07-08 迭代状态

- 上一轮候选/结果摘要：上一轮 `share_24_76_hold_2_8_ramp62_cost_guard` 判定 `reject`，core_multifactor clear candidate 仍只保留 `keep_watch`；本轮开局 guard 显示 Path1 fast/core_multifactor coverage 完整，主线和 core_multifactor 仅做巡检与候选设计，没有把独立 Path4 `emergent_theme` 并入 Path1。
- 本轮候选 ID 与命令：本轮未新增 Path1 `--only-base-ids` 回测，原因是 A股实跑预算优先给 guard focus `theme_risk_control` 的独立 Path4，并补 Path5 event entry；本轮 Path1 下一条确认命令保留为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`。
- Scorecard 与判定：本轮 Path1 无新增实跑 scorecard；`scripts/update_weighted_winners.py` 后 Path1 official/window winner、robust candidate 与 tracked payload 未改变。判定：Path1 主线 `keep_watch`，core_multifactor 子段 `keep_watch`，不能用本轮同步产物替代策略实验结论。
- core_multifactor 子段同步：代码实际 core_multifactor 覆盖仍由 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 决定；本轮没有新增 overlay，也没有把 Path4-lite/core_multifactor 误写为独立 Path4。
- evict/归档：本轮无 Path1 evict/归档；未回测原因是 A股新增确认预算投给 Path4/Path5，且 Path1 当前 coverage 无 blocking。
- 下一轮 focus：最终 guard 给 `satellite_risk_cost`。第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`；若未注册，先加入 Path1 fast-pass satellite direction，并 evict 一条非 winner/robust 旧卫星线。
- Focus 候选池：`satellite_risk_cost` -> `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`、`aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`；`signal_quality` -> `aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`、`aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；`core_multifactor_coverage` -> `...risk09_reconfirm_v5`、`...quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；`holding_shape` -> `share_22_78_hold_2_8_ramp64_cost_guard_reconfirm`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`；`weekly_exposure_path` -> `__port_weekly_exposure_buffered_asym13`、`__port_weekly_exposure_buffered`。

## 2026-07-07 迭代状态

- 上一轮候选/结果摘要：上一轮留下 `lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`；本轮先执行 fast-pass 巡检，再用 A股五窗口增量命令确认 holding-shape 新候选 `core_explore_80_20_equal_weight_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`，并保持 core_multifactor 只作为 Path1 direction group，不并入独立 Path4。
- 本轮候选 ID 与命令：本轮 A股增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__share_24_76_hold_2_8_ramp62_cost_guard,<two_path2_v74>,<one_path3_yield_v2>,<three_path4_prom24_signal30>`；`scripts/winner_only_pass.py` 另发现既有 fast-pass clear candidates：2017 `share_08_92_hold_2_8_ramp75_cost_guard`、2023 core_multifactor `quality_profitability_value_lowvol_trend_cost_guard_reconfirm`、2025 `sat_three_stage_buffered_cost_guard_risk06_reconfirm`。
- Scorecard 与判定：`share_24_76_hold_2_8_ramp62_cost_guard` 五窗口 CAGR `12.08% / 5.64% / 19.39% / 40.67% / 57.63%`，MaxDD `-43.50% / -41.36% / -24.59% / -12.63% / -12.38%`，turnover 最高 `7.57x`；相对当前 Path1 robust `risk20_reconfirm` 在 2020 CAGR 低 `24.92pp`、MaxDD 恶化 `27.37pp`，判定 `reject`。core_multifactor clear candidate 五窗口 CAGR `14.34% / 14.59% / 30.90% / 58.08% / 63.18%`，2023 Sharpe 改善但 2017/2020 仍弱，判定 `keep_watch`，`update_weighted_winners.py` 后 official winner/robust/tracked payload 未改变。
- core_multifactor 子段同步：coverage 仍按代码实际 `67/67` 完整；本轮没有新增 overlay，也没有把独立 `emergent_theme` 变体加入 Path1。下一轮若继续 focus `core_multifactor_coverage`，优先补低波质量中风险恢复确认，而不是继续扩大 holding-shape。
- evict/归档：本轮未新增 Path1 evict；开局已有 dirty code 中的 active/archive 变更保持原样，未在本轮回滚或扩大。
- 下一轮 focus：第一条确认命令建议 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`；若 guard 转到 holding-shape，则先测 `core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard_reconfirm`。
- Focus 候选池：`signal_quality` -> `aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`、`aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；`core_multifactor_coverage` -> `...risk09_reconfirm_v5`、`...quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；`holding_shape` -> `share_22_78_hold_2_8_ramp64_cost_guard_reconfirm`、`share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`；`weekly_exposure_path` -> `__port_weekly_exposure_buffered_asym13`、`__port_weekly_exposure_buffered`。

## 2026-07-06 迭代状态

- 上一轮候选/结果摘要：上一轮把下一步指向 `lowvol_signal_quality_gate_cashguard_risk07_reconfirm_v4`；本轮已注册并五窗口确认，仍只作为 Path1/core_multifactor fast-pass，不与独立 Path4 强主题涌现混用。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk07_reconfirm_v4`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_risk07>,<two_path2_v72>,<one_path3_weekly_yield>,<three_path4_signal30>`。
- 五窗口结果：CAGR `12.29% / 12.79% / 19.02% / 52.38% / 56.20%`，最大回撤 `-15.47% / -16.29% / -13.92% / -15.42% / -11.16%`。结论：2020/2023 仍弱于当前 Path1 robust 主体，`scripts/update_weighted_winners.py` validation 拒绝替换，window winner、robust candidate 与 tracked payload 未改变。
- core_multifactor 子段同步：代码实际 core_multifactor 覆盖仍按 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 返回集合为准；本轮没有把独立 Path4 `emergent_theme` 变体并入 Path1。
- evict/归档：从 active core_multifactor 组移出旧 `aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk04_reconfirm`；evict 原因是旧 risk04 非当前 winner/robust，且本轮 risk07 已覆盖同一低波质量信号槽位。
- 下一轮 focus：若最终 guard 继续指向 `signal_quality` 或 `core_multifactor_coverage`，下一候选不要复跑 risk07，改测低波质量线的中等风险恢复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`；若未注册，先加入 core_multifactor group/list 并再淘汰一条非 winner/robust 旧低波线。

## 2026-07-05 迭代状态

- 上一轮候选/结果摘要：上一轮把下一步指向 `trend_signal_quality_gate_cashguard_risk09_reconfirm`；本轮已注册并五窗口确认，继续只作为 Path1/core_multifactor fast-pass，不与独立 Path4 强主题涌现混用。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk09_reconfirm`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_risk09>,<two_path2_v71>,<one_path3_v3>,<three_path4_prom21>`。
- 五窗口结果：CAGR `9.71% / 10.58% / 20.78% / 57.33% / 52.74%`，最大回撤 `-20.38% / -21.14% / -13.19% / -15.23% / -11.03%`，换手最高 `5.35x`。结论：2017/2020 弱于当前 Path1 主体，未替换 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段同步：代码实际 core_multifactor 覆盖扩到 `67` 条；`scripts/winner_only_pass.py` 仍只发现既有 fast-pass 方向的 clear improvement，`scripts/update_weighted_winners.py` 后 2017 仍由 `trend_signal_quality_gate_cashguard_risk10_reconfirm` 承担，2020/2023 robust 仍由 `sat_three_stage_buffered_cost_guard_risk20_reconfirm` 承担。
- evict/归档：本轮无 Path1 evict；`risk09` 作为 risk10/risk06 之间的趋势信号质量插值负样本保留。
- 下一轮 focus：若最终 guard 继续给 `core_multifactor_coverage`，不要继续单纯插值 trend risk；下一候选池转回低波质量信号线，首条命令建议 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk07_reconfirm_v4`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 2026-07-04 07:03 CST 状态

- 上一轮候选/结果摘要：上一轮把 focus 留给 core_multifactor/signal-quality；本轮按代码实际集合新增并确认 `trend_signal_quality_gate_cashguard_risk06_reconfirm`，仍只作为 Path1/core_multifactor fast-pass，不与独立 Path4 强主题涌现混用。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk06_reconfirm`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_trend_risk06>,<two_path2_v70>,<one_path3_turnover>,<three_path4_prom24_signal29>`。
- 五窗口结果：CAGR `11.32% / 12.89% / 19.05% / 56.60% / 52.66%`，最大回撤 `-15.08% / -20.00% / -12.38% / -15.23% / -11.03%`，年均换手最高 `5.36x`。结论：长中窗弱于 satellite robust，未替换 Path1 official/robust。
- core_multifactor 子段同步：`scripts/winner_only_pass.py` 退出码 `2` 表示 fast-pass 出现 clear improvement，但 weighted validation 拒绝本轮 risk06 替换 2017 official；`scripts/update_weighted_winners.py` 后 Path1 composite 由 `risk20_reconfirm` 承担 robust/2020/2023，`trend_signal_quality_gate_cashguard_risk10_reconfirm` 承担 2017，`risk10_reconfirm` 卫星承担 2025，composite `meanCAGR=46.39% / minCAGR=22.19% / worstDD=-17.08%`。
- evict/归档：本轮无 Path1 evict；只是把 core_multifactor 覆盖扩到 guard 口径 `66/66`，不因 risk06 短窗弱而跳过其它窗口。
- 下一轮 focus：最终 guard 给出 `core_multifactor_coverage`。下一轮第一候选建议在当前 2017 组件 `trend risk10` 与本轮弱 `trend risk06` 中间测试 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk09_reconfirm`；首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk09_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 2026-07-01 20:58 CST 状态

- 上一轮候选/结果摘要：上一轮把下一步指向 `core_multifactor risk06_reconfirm_v2`；本轮已注册并五窗口确认，继续只作为 Path1/core_multifactor fast-pass 候选，不与独立 Path4 强主题涌现混用。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm_v2`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_risk06_v2>,<two_path2_v67>,<one_path3_turnover>,<three_path4_prom22_signal28>`。
- 五窗口结果：CAGR `16.20% / 13.99% / 20.66% / 61.31% / 80.26%`，最大回撤 `-16.36% / -16.21% / -13.92% / -15.42% / -4.26%`，年均换手最高 `5.29x`。结论：未替换 Path1 official/robust；当前 robust 与 2017-window 仍为 risk04，2020/2023 仍为 risk20，2025 仍为 `aggr_10_90_prom6`。
- core_multifactor 子段同步：`scripts/winner_only_pass.py` 退出码 `2` 仅代表发现 fast-pass clear improvement，信号集中在 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6_cash_off` 的 2017-only 快筛，不足以直接改 official winner；`scripts/update_weighted_winners.py`、`refresh_active`、live/public 已同步。
- evict/归档：从 core_multifactor active 组移出旧 `aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`；evict 原因是旧 trend risk08 非 winner/robust，且本轮 risk06_v2 覆盖同一风险恢复对照槽位。
- 下一轮 focus：最终 guard 给出 `signal_quality`；下一轮不要复跑 risk06_v2，先把 `signal_quality` 映射到 core_multifactor 低波质量门槛的中间风险对照。候选池占位 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk05_reconfirm_v3`，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk05_reconfirm_v3`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 2026-07-01 05:26 CST 状态

- 上一轮候选/结果摘要：上一轮只记录 `core_multifactor risk04` 候选；本轮已注册并五窗口确认，保持 Path1/core_multifactor 属于 Path1 fast-pass，不把独立 Path4 强主题涌现并入 Path1。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk04_reconfirm`；命令并入本轮 A股增量回测 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_risk04>,<three_path4_cap04_ids>`。
- 五窗口结果：CAGR `16.23% / 16.51% / 22.06% / 78.20% / 111.77%`，最大回撤 `-18.16% / -18.41% / -12.87% / -15.71% / -4.25%`；短窗和 2026 回撤较好，但 2017/2020 不及既有 satellite robust。
- core_multifactor 子段同步：`scripts/winner_only_pass.py` 覆盖 `base_candidates=130 / total_candidates=1430 / evaluated=273`，无 clear improvement；`scripts/update_weighted_winners.py` 后 Path1 robust candidate 与 2017-window tracked payload 暂切到本轮 risk04，README/HISTORY/live/public 已同步。
- evict/归档：从 active core_multifactor 组移出旧 `aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk10_reconfirm`；evict 原因是旧 risk10 非当前 robust/tracked 主体，且本轮 risk04 已覆盖更低风险信号质量形态。
- 下一轮 focus：最终 guard 给出 `core_multifactor_coverage`。下一轮第一候选建议不要复跑 risk04，改做同一 lowvol/quality/profitability/growth 线的中等风险恢复对照；首条命令草案为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm_v2`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`，并同步 evict 一条非 winner/robust 旧多因子线。

## 2026-06-30 17:26 CST 状态

- 上一轮候选/结果摘要：上一轮 Path1 仅做 fast-pass 巡检，本轮继续按代码实际集合巡检 Path1 与 core_multifactor；最终 guard 显示 `ashare_path1_core_multifactor 63/63`、`ashare_path1_fast_family 131/131`，coverage 仍完整。
- 本轮候选 ID 与命令：本轮没有新增 Path1 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`，结果 `base_candidates=130 / total_candidates=1430 / evaluated=273`，无 clear improvement。
- core_multifactor 子段巡检：没有新增 overlay 或确认形态；未把独立 Path4 `emergent_theme` 变体并入 Path1。`scripts/update_weighted_winners.py` 后 Path1 window winner、robust candidate、tracked/live/public payload 未改变。
- evict/归档：本轮无 Path1 evict/归档。
- 下一轮 focus：最终 guard 为 `signal_quality`。下一轮第一候选建议注册/确认 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk04_reconfirm`；首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk04_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`，并在 plan 中继续映射 signal-quality 到 core_multifactor 质量门槛候选池。

## 2026-06-30 06:12 CST 状态

- 上一轮候选/结果摘要：上一轮 Path1 只做 fast-pass 巡检并把下一轮 focus 指向 `satellite_risk_cost`；本轮开局/收尾 guard 均显示 Path1 coverage 完整，最终 focus 转为 `holding_shape`。
- 本轮候选 ID 与命令：本轮没有新增 Path1 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`，`base_candidates=130 / total_candidates=1430 / evaluated=273`，无 clear improvement。同步命令包括 `.venv/bin/python scripts/update_weighted_winners.py`、`.venv/bin/python scripts/export_live_platform_data.py`、`.venv/bin/python scripts/generate_public_snapshot.py`。
- core_multifactor 子段巡检：最终 guard 显示 `ashare_path1_core_multifactor 63/63`、`ashare_path1_fast_family 131/131`；本轮没有新增 core_multifactor overlay，也没有把独立 Path4 `emergent_theme` 变体并入 Path1。
- 结论：Path1 window winner、robust candidate、tracked/live/public payload 未改变；本轮无 Path1 evict/归档。
- 下一轮 focus：按最终 guard 的 `holding_shape`，下一轮第一候选建议注册/确认 `core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp62_cost_guard_reconfirm`，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp62_cost_guard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["holding_shape"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 2026-06-29 17:30 CST 状态

- 上一轮候选/结果摘要：上一轮留下 Path1 fast-pass 与 core_multifactor 信号质量候选；本轮执行 `scripts/winner_only_pass.py` 巡检，`base_candidates=130 / total_candidates=1430 / evaluated=273`，未发现可同时改善 CAGR、Sharpe 与回撤的 clear improvement。
- 本轮候选 ID 与命令：本轮没有新增 Path1 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`，并在收尾通过 `.venv/bin/python scripts/update_weighted_winners.py`、`.venv/bin/python scripts/export_live_platform_data.py`、`.venv/bin/python scripts/generate_public_snapshot.py` 同步 tracked/live/public。
- core_multifactor 子段巡检：最终 guard 显示 `ashare_path1_core_multifactor` 为 `63/63` 完整覆盖；本轮没有新增 overlay，也没有把独立 Path4 emergent_theme 计入 Path1。
- 结论：Path1 window winner、robust candidate 与 tracked payload 未被本轮改写；本轮没有 Path1 evict/归档。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> satellite_risk_cost`。下一轮第一候选建议只注册一条更低风险卫星成本线 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk04_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk04_reconfirm`。

本文档用于约束和记录 `Path 1`（胜出者核心主线）的研究方向。  
目标不是无约束追求收益上限，而是在保持框架可交易、可复用、可解释的前提下，把当前常见的 `20%~26% CAGR` 推向 `25%~30%+ CAGR`。  
当前已把 `Path 1` 的单轮探索预算提升到 **`24-28` 个 base candidates / `5` 个固定方向**，并要求候选按方向分组生成，而不是只做参数邻域微调。

## 本轮执行计划（2026-06-29 05:25 CST）

- 上一轮 `core_multifactor risk06_reconfirm` 未改变 Path1 official/robust，本轮保持 Path1 fast-pass 口径，只执行巡检与同步：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py` 覆盖 `130` 个 base candidates / `1430` 条组合，实际评估 `273` 条，没有 clear improvement；没有把独立 Path4 强主题变体并入 Path1，也没有新增 Path1 `--only-base-ids` 回测。
- `scripts/update_weighted_winners.py` 后 Path1 official 仍为 2017 `risk10_reconfirm`、2020/2023 `risk20_reconfirm`、2025 `aggr_10_90_prom6`，robust 仍为 `risk25_reconfirm`。最终 guard 为 `pass`，`ashare_path1_core_multifactor 63/63`、`ashare_path1_fast_family 131/131`；本轮无 Path1 evict，tracked/live/public 只有同步刷新。
- core_multifactor 子段本轮只按代码实际集合巡检，没有新增 overlay 或确认形态；最终 focus 转为 `signal_quality`。下一轮第一条命令建议从多因子信号质量池新增一个更低风险/更窄确认的对照，而不是复跑本轮巡检：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk04_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-28 17:40 CST）

- 上一轮建议确认 core_multifactor `risk06_reconfirm`；本轮接续启动前已注册的候选并完成巡检，保持 Path1/core_multifactor 属于 Path1 fast-pass，不把独立 Path4 强主题涌现并入 Path1。最终 guard 仍为 `pass`，`ashare_path1_core_multifactor 63/63`、`ashare_path1_fast_family 131/131`。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm`。五窗口 CAGR `15.68% / 13.94% / 21.07% / 76.14% / 113.46%`，最大回撤 `-16.28% / -16.01% / -13.83% / -15.71% / -4.25%`，换手 `2.47x / 2.69x / 2.82x / 5.04x / 5.33x`；短窗强但 2017/2020 不足，未改变 Path1 window winner、robust candidate 或 tracked payload。
- 本轮命令类型：`scripts/winner_only_pass.py`、`scripts/update_weighted_winners.py`、`scripts/export_live_platform_data.py`、`scripts/generate_public_snapshot.py` 与最终 guard。尝试执行 `backtest_marketcap_etf.py --family-scope refresh_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，但实际集合为 `99` 个 base ids，约 `495` 次回测，运行约 25 分钟后按预算中断；不把这次中断视为完整 active refresh。
- `scripts/update_weighted_winners.py` 后 Path1 official 仍为 2017 `risk10_reconfirm`、2020/2023 `risk20_reconfirm`、2025 `aggr_10_90_prom6`，robust 仍为 `risk25_reconfirm`。本轮无 Path1 evict；public/live 只做同步导出。
- 最终 focus 为 `holding_shape`。下一轮第一条命令建议回到持仓形态修复，而不是继续堆 core_multifactor：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp62_cost_guard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["holding_shape"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-27 19:24 CST）

- 上一轮 Path1 没有新增且下一步仍需回到 signal/core_multifactor 质量线；本轮实际只做 Path1 巡检、`winner_only_pass.py`、`refresh_active` 与 weighted/live/public 同步，没有新增 Path1/base id，也没有把独立 Path4 强主题涌现并入 Path1。
- 本轮命令类型：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --family-scope refresh_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`。`winner_only_pass.py` 覆盖 `129` 个 fast-pass base candidates / `1419` 条组合，core_multifactor 代码实际覆盖为 `62/62`，没有 clear improvement。
- `scripts/update_weighted_winners.py` 后 Path1 composite 组件维持为 robust `risk25_reconfirm`、2020/2023 `risk20_reconfirm`、2017 `risk10_reconfirm`、2025 `aggr_10_90_prom6`；composite 五窗口 CAGR 为 `26.17% / 32.29% / 35.23% / 115.76% / 187.66%`，robust metrics `meanCAGR=52.36%`、`minCAGR=26.17%`、最差回撤 `-18.09%`。本轮无 Path1 evict，tracked/live/public 只有同步刷新。
- 最终 guard focus 为 `signal_quality`。下一轮第一条命令建议只注册并确认一个更偏信号质量/低风险的 core_multifactor 对照，不复跑本轮巡检：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk06_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-25 06:56 CST）

- 上一轮 core_multifactor risk10 未改变 official，本轮开局 guard 为 `satellite_risk_cost`，实际只做 Path1 巡检、`winner_only_pass.py`、`refresh_active` 与 weighted/live/public 同步，没有新增 Path1/base id；独立 Path4 强主题仍未并入 Path1。
- `scripts/winner_only_pass.py` 提示既有 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk08_reconfirm` 在 `since_2017_only` 有 clear improvement，但 `scripts/update_weighted_winners.py` 后 official 2017/2020/2023/2025 winners 仍为 `risk10/risk20/risk20/aggr_10_90_prom6`，Path1 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`，`meanCAGR=51.16%`、`minCAGR=26.42%`。
- 本轮同步命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --family-scope refresh_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`。本轮无 Path1 evict。
- core_multifactor 子段只巡检代码实际集合，没有新增 overlay 或确认回测；最终 guard 仍为 coverage pass，focus 转为 `holding_shape`。下一轮第一条命令建议注册并确认持仓形态修复，而不是复跑本轮 clear 但未官方晋级的 risk08：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp62_cost_guard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["holding_shape"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-24 19:22 CST）

- 上一轮候选池把下一步明确指向 `core_multifactor_coverage`，本轮按代码实际集合注册并确认低波质量成长信号组合，不把独立 Path4 强主题变体并入 Path1。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk10_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股 Path2/3/4 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk10_reconfirm,<two_path2_v58_ids>,<one_path3_weekly_id>,<three_path4_risk10_cap06_exit62_ids>`。
- 新 core_multifactor 五窗口 CAGR `15.33% / 12.63% / 25.28% / 75.09% / 99.77%`，最大回撤 `-21.93% / -21.26% / -13.35% / -15.71% / -4.25%`，换手 `2.53x / 2.73x / 2.89x / 5.02x / 5.35x`。结论：2023 和短窗可比，但 2017/2020 仍弱于当前 satellite robust，不替换 Path1 window winner、robust candidate 或 tracked/live/public payload。
- `scripts/winner_only_pass.py` 给出 raw clear candidate `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk08_reconfirm`，但 `scripts/update_weighted_winners.py` 后官方 Path1 2017/2020/2023/2025 window winners 与 robust 仍分别维持 `risk10/risk20/risk20/prom6` 与 `risk25_reconfirm`。本轮 core_multifactor 覆盖从 `61/61` 扩到待 guard 确认的 `62/62`，无 Path1 evict。
- 最终 guard 为 `pass`，下一轮 focus 转为 `signal_quality`。不要复跑本轮 core_multifactor risk10；第一条命令建议回到 signal-quality 修复池，先注册并确认更强调信号质量/低波过滤的对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk08_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-24 06:57 CST）

- 上一轮 `risk06_reconfirm` 仍是短窗强、中长窗弱，本轮按预留命令实际注册并五窗口确认 `exit50` 对照；最终 guard 转为 `core_multifactor_coverage`，所以下一轮 focus 不再继续复跑 risk06 支线。
- 本轮新增并确认 base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk06_exit50_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股 Path2/3/4 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk06_exit50_reconfirm,<two_path2_v57_ids>,<one_path3_weekly_id>,<three_path4_signal30_ids>`。
- `exit50` 五窗口 CAGR `23.61% / 29.75% / 29.54% / 110.86% / 158.13%`，最大回撤 `-12.10% / -13.22% / -16.97% / -10.91% / -6.61%`。结论：短窗比上一轮更强，但 2017/2020/2023 仍未超过当前 Path1 official window winners；`scripts/update_weighted_winners.py` 后 Path1 robust candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`，`meanCAGR=49.89%`、`minCAGR=26.01%`。
- core_multifactor 子段本轮完成巡检和 `refresh_active` 同步，代码实际覆盖 `61/61`；fast family 覆盖 `129/129`。`scripts/winner_only_pass.py` 无 clear improvement，本轮没有 Path1 evict，也没有改变 tracked/live/public official payload。
- 下一轮第一条命令应映射最终 focus `core_multifactor_coverage`，先注册一个未在当前 61 个池内的低波质量成长信号组合，再补五窗口：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk10_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-23 17:21 CST）

- 上一轮 core_multifactor `risk08_reconfirm` 仍未改善 2017/2020；本轮按最终 rotation `satellite_risk_cost` 回到 satellite defense 风险/成本邻域，只新增 1 个 Path1 fast-pass base candidate，不把独立 Path4 emergent_theme 结果并入 Path1。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk06_reconfirm`。实际 A股合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk06_reconfirm,<two_path2_ids>,<one_path3_id>,<three_path4_ids>`。
- `risk06_reconfirm` 五窗口 CAGR `24.64% / 30.12% / 28.92% / 113.02% / 125.41%`，最大回撤 `-12.13% / -13.77% / -23.12% / -11.13% / -6.61%`，Sharpe `1.0595 / 1.0736 / 0.9583 / 2.0514 / 2.7855`，换手 `2.93x / 3.32x / 3.49x / 4.65x / 7.39x`。结论：短窗仍强，但 2017/2020 弱于 `risk25/risk20` 主体，2023 回撤偏深，不替换 Path1 window winner、robust candidate 或 tracked/live/public payload。
- `scripts/winner_only_pass.py` 退出码 `0`，无 clear improvement；`scripts/update_weighted_winners.py` 后 Path1 candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`。core_multifactor 子段本轮只巡检，代码实际覆盖 `61/61`；fast family 覆盖 `128/128`。本轮无 Path1 evict。
- 最终 focus 为 `satellite_risk_cost`。下一轮第一条命令建议不要复跑 risk06，而是先注册一个 `risk06` 出场/确认修复对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk06_exit50_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-23 05:27 CST）

- 上一轮 `core_multifactor` 的 `risk10_reconfirm` 仍未改善 2017/2020；本轮按最终 focus 继续做 `signal_quality`，只新增 1 个 core_multifactor 风险下探确认，不把独立 Path4 emergent_theme 结果并入 Path1。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`。实际 A股合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <one_path1_id>,<two_path2_ids>,<one_path3_id>,<three_path4_ids>`。
- 五窗口结果：CAGR `14.67% / 12.59% / 23.69% / 78.61% / 97.44%`，最大回撤 `-18.62% / -20.00% / -12.80% / -15.21% / -4.25%`，Sharpe `0.8190 / 0.6628 / 0.9367 / 1.6900 / 2.9294`，换手 `2.51x / 2.68x / 2.98x / 5.21x / 5.35x`。结论：短窗和 2023 回撤可比，但 2017/2020 CAGR 仍弱于 Path1 satellite robust，未改变 window winner、robust candidate、tracked/live/public payload。
- core_multifactor 子段按代码实际集合扩到 `61` 个 base candidates；最终 guard 为 `pass`，`ashare_path1_core_multifactor 61/61 complete`、`ashare_path1_fast_family 127/127 complete`。本轮无 Path1 evict。
- 最终 focus 仍为 `signal_quality`。下一轮第一条命令建议不要复跑 risk08，而是注册一个更偏低波/质量的 signal-quality 对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk08_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-22 17:34 CST）

- 上一轮 `satellite_defense` 的 `risk08_reconfirm` 只增强 2025/2026，2017/2020 和 2023 回撤仍不足以替换 Path1 robust；本轮按 guard rotation 回到 `core_multifactor_coverage`，只新增 1 个 core_multifactor 确认，不把 Path4 emergent_theme 并入 Path1。
- 本轮新增并五窗口确认 base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk10_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股 Path2/3/4 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk10_reconfirm,...`。
- 新 core_multifactor 五窗口 CAGR `14.11% / 12.10% / 25.41% / 78.93% / 98.11%`，最大回撤 `-22.52% / -20.88% / -13.74% / -15.21% / -4.25%`，换手 `2.54x / 2.69x / 2.96x / 5.21x / 5.36x`。结论：相对上一轮 risk12 降低了 2023/长窗回撤，但 2017/2020 CAGR 仍弱于既有 satellite robust，不替换 Path1 window winner、robust candidate 或 tracked/live/public payload。
- `scripts/update_weighted_winners.py` 后 Path1 winner/robust 未切换；最终 guard 为 `pass`，`ashare_path1_core_multifactor 60/60 complete`、`ashare_path1_fast_family 126/126 complete`。本轮无 Path1 evict。
- 最终 focus 仍为 `core_multifactor_coverage`。下一轮第一条命令建议继续在同一多因子组里做更低风险确认，而不是复跑 risk10：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-22 05:23 CST）

- 上一轮预留 `satellite_risk_cost` 的风险 8% 再确认，本轮先按 guard 补齐 Path4 block，再与 Path2/3 合并五窗口确认 Path1 fast-family 候选；因本地 A股原始行情缓存只到 `2026-06-18`，所有 A股回测均显式使用 `--end-date 2026-06-18`。
- 本轮 Path1 新增 base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk08_reconfirm`。实际命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk08_reconfirm,...`。
- 五窗口 CAGR `25.70% / 29.78% / 28.87% / 113.06% / 153.23%`，最大回撤 `-12.13% / -13.29% / -23.27% / -11.13% / -6.61%`，换手 `2.97x / 3.32x / 3.49x / 4.65x / 7.35x`。结论：risk08 明显增强 2025/2026 暴露，但 2017/2020 仍弱于现有 Path1 robust，2023 回撤也偏深，不替换 window winner 或 tracked。
- `scripts/winner_only_pass.py` 退出码 `0`，未发现相对 tracked winners 的 clear improvement；`scripts/update_weighted_winners.py` 后 Path1 window winner 仍为 `risk25_reconfirm`/`risk20_reconfirm`/`aggr_10_90_prom6` 组合，Path1 candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`。core_multifactor 子段本轮只巡检，代码实际覆盖 `59/59`，没有新增 overlay。
- 最终 guard 为 `pass`，`ashare_path1_fast_family 125/125 complete`，本轮无 Path1 evict。最终 focus 转为 `holding_shape`；下一轮第一条命令建议先注册并确认更温和持仓形态，而不是继续下调卫星风险暴露：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp62_cost_guard_reconfirm`；若未注册，先加入 `WINNER_CORE_VARIANTS`、`PATH1_FAST_PASS_DIRECTION_GROUPS["holding_shape"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-21 17:29 CST）

- 上一轮 `core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm` 只增强短窗，2017/2020 仍弱于 Path1 satellite robust，未改变 window winner/robust/tracked；本轮按最终 focus `signal_quality` 注册更偏质量门槛的 core_multifactor 变体。
- 本轮新增并五窗口确认 1 个 Path1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk12_reconfirm`。命令与其它 A股新增候选合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk12_reconfirm,...`。
- 五窗口 CAGR `14.11% / 12.20% / 25.70% / 79.37% / 98.84%`，最大回撤 `-23.50% / -21.75% / -14.45% / -15.21% / -4.25%`，换手 `2.56x / 2.73x / 2.99x / 5.20x / 5.37x`。结论：2023/短窗仍有弹性，但 2017/2020 和回撤均不足以替换 Path1 satellite robust。
- `scripts/update_weighted_winners.py` 后 Path1 window winner、robust candidate、tracked/live/public payload 未切换；最终 guard 为 `pass`，`ashare_path1_core_multifactor 59/59 complete`、`ashare_path1_fast_family 124/124 complete`。本轮无 Path1 evict。
- 最终 focus 转为 `satellite_risk_cost`。下一轮第一条命令建议回到卫星防守风险/成本邻域，而不是继续堆多因子信号：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk08_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-21 05:23 CST）

- 上一轮预留 `core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm`；本轮先注册到 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`，再与其它 A股目标合并做五窗口 `--only-base-ids` 增量确认。
- 本轮 Path1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm`。五窗口 CAGR `16.42% / 14.71% / 30.56% / 83.42% / 109.11%`，最大回撤 `-23.43% / -21.36% / -15.30% / -15.10% / -4.25%`，换手 `2.52x / 2.81x / 3.03x / 5.03x / 5.40x`。
- 结论：risk12 延续短窗弹性，但 2017/2020 仍明显弱于 Path1 satellite robust；`scripts/update_weighted_winners.py` 后 Path1 window winner、robust candidate、tracked/live/public payload 未切换。本轮无 Path1 evict，最终 guard `ashare_path1_core_multifactor 58/58 complete`、`ashare_path1_fast_family 123/123 complete`。
- 最终 focus 为 `signal_quality`。下一轮第一条命令建议先注册更偏信号质量门槛的多因子变体，而不是继续单纯下调风险：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk12_reconfirm`；若未注册，先加入 core_multifactor group/list。

## 本轮执行计划（2026-06-20 17:27 CST）

- 上一轮 core_multifactor `quality_profitability_growth_trend_signal_cashguard_risk14_reconfirm` 改善 2023/短窗但 2017/2020 仍弱，开局 focus 为 `holding_shape`；本轮预算优先投给 A股 Path2/3/4 与 HK Path4/5，Path1 只完成 coverage/weighted/live/public 巡检，没有新增 Path1 `--only-base-ids` 回测。
- 巡检结果：最终 guard 为 `pass`，`ashare_path1_core_multifactor 57/57 complete`、`ashare_path1_fast_family 122/122 complete`；`scripts/update_weighted_winners.py` 后 Path1 window winner、robust candidate、tracked/live/public payload 均未被本轮同步改变。本轮无 Path1 evict。
- core_multifactor 子段仍以 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 代码实际集合为准；本轮没有新增 overlay，也没有把 Path4 emergent_theme 结果并入 Path1。
- 最终 focus 转为 `core_multifactor_coverage`。下一轮第一条命令建议注册并确认更低风险的质量/盈利/成长/趋势多因子，而不是复跑本轮未改善的 risk14：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-20 05:28 CST）

- 上一轮把 focus 指向 `signal_quality`，本轮按代码实际集合注册并确认 1 个 Path1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk14_reconfirm`。命令与 Path4 blocking 覆盖合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk14_reconfirm,...`。
- 新 core_multifactor 五窗口 CAGR 为 `16.41% / 14.86% / 30.64% / 83.60% / 110.16%`，最大回撤为 `-24.32% / -22.15% / -16.12% / -15.10% / -4.25%`，换手为 `2.55x / 2.84x / 3.07x / 5.02x / 5.44x`。结论：2023 与短窗弹性好，但 2017/2020 仍弱于 Path1 satellite robust，且长窗回撤偏深，不替换 Path1 window winner、robust candidate 或 tracked/live/public payload。
- `scripts/update_weighted_winners.py` 后 Path1 candidate 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`；最终 coverage 为 `ashare_path1_core_multifactor 57/57 complete`、`ashare_path1_fast_family 122/122 complete`。本轮无 Path1 evict。
- 最终 guard focus 为 `satellite_risk_cost`。下一轮第一条命令建议回到卫星防守风险/成本邻域，而不是继续堆多因子信号：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk08_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-19 17:29 CST）

- 上一轮 core_multifactor 新线只改善短窗，最终 focus 转为 `holding_shape`；本轮按候选池注册并五窗口确认 `core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`，命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`。
- `share_20_80_hold_2_8_ramp62_cost_guard_reconfirm` 五窗口 CAGR `20.24% / 27.47% / 33.82% / 106.59% / 131.84%`，最大回撤 `-20.66% / -17.93% / -23.14% / -10.74% / -11.72%`，换手 `2.65x / 2.97x / 2.94x / 4.44x / 5.60x`。结论：短窗很强，但 2017/2020 仍低于 Path1 robust，2023 回撤也偏深，不替换 Path1 window winner、robust candidate 或 tracked/live/public payload。
- core_multifactor 子段本轮只巡检，不新增；最终覆盖 `ashare_path1_core_multifactor 56/56 complete`，fast family `121/121 complete`。`scripts/update_weighted_winners.py` 后 Path1 candidate 仍为 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`，无 Path1 evict。
- 最终 guard focus 为 `signal_quality`。下一轮第一条命令建议补质量/盈利/成长/趋势信号质量修复，而不是复跑 holding_shape：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk14_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-19 05:26 CST）

- 上一轮 core_multifactor `quality_profitability_signal_cashguard_risk14_reconfirm` 改善短窗但没有改写 Path1 winner/robust；本轮按上一轮候选池注册并确认 `aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk14_reconfirm`，只新增 1 个 Path1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk14_reconfirm`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path4 blocking 补覆盖合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk14_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom22_emergent_theme_quality_gate_signal29_leader78_coverage_penalty_risk12_cap06_exit60_lowturn`。
- 新 core_multifactor 五窗口 CAGR 为 `16.14% / 15.92% / 26.76% / 85.95% / 110.19%`，最大回撤为 `-21.07% / -20.47% / -15.08% / -13.91% / -4.25%`，换手为 `2.60x / 2.86x / 3.08x / 5.44x / 5.45x`。结论：短窗弹性好于上一轮 signal-only 版本，但 2017/2020 仍弱于 Path1 satellite robust，不替换 window winner、robust candidate 或 tracked payload。
- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 56/56 complete`、`ashare_path1_fast_family 120/120 complete`；本轮无 Path1 evict。最终 focus 转为 `holding_shape`，下一轮第一条命令建议回到持仓形态修复，而不是继续追加多因子：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp62_cost_guard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["holding_shape"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-18 17:16 CST）

- 上一轮候选池给出的下一步是 core_multifactor 风险下移确认；本轮按代码实际集合新增 `aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm`，并只确认 1 个 Path1 base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm`。命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm`。
- 五窗口 CAGR 为 `16.16% / 15.82% / 25.36% / 76.40% / 106.76%`，最大回撤为 `-24.41% / -21.71% / -16.04% / -14.14% / -4.25%`。相对既有 Path1 winner，risk14 改善短窗但长中窗 CAGR 和回撤不够，`scripts/winner_only_pass.py` 仍显示 no clear improvement。
- `scripts/update_weighted_winners.py` 后 Path1 window winner、composite candidate、tracked/live/public payload 未切换；core_multifactor 覆盖从 `54/54` 增为 `55/55`，无 Path1 evict。
- 最终 guard 为 `pass`，Path1 rotation 仍为 `rotate`，下一轮 focus 转为 `signal_quality`。下一轮第一条命令建议注册并确认质量盈利信号的质量门槛修复，而不是继续单纯降风险：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk14_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-18 05:21 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 54/54 complete`、`ashare_path1_fast_family 118/118 complete`；本轮 Path1 只做 `scripts/winner_only_pass.py` 巡检与 weighted/live/public 同步，没有新增 Path1 `--only-base-ids` 回测，也没有新增 core_multifactor overlay。
- `winner_only_pass.py` 本轮没有 clear improvement；`scripts/update_weighted_winners.py` 后 Path1 window winner、composite candidate、tracked/live/public payload 未切换。core_multifactor 子段仍以代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 为准，覆盖为 `54` 个变体。
- 本轮新增预算投给 A股 Path2/3/4、Path5 事件入口与 HK Path4-7；Path1 无 evict。最终 rotation focus 为 `core_multifactor_coverage`，下一轮候选池映射回多因子覆盖，但仍必须按代码实际返回的 core_multifactor 集合补，不假设固定 overlay 数。
- 下一轮第一条命令建议先注册并确认更窄质量/盈利多因子候选：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-17 18:02 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 54/54 complete`、`ashare_path1_fast_family 118/118 complete`；本轮 Path1 只做 `scripts/winner_only_pass.py` 巡检与 weighted/live/public 同步，没有新增 Path1 `--only-base-ids` 回测，也没有新增 core_multifactor overlay。
- `winner_only_pass.py` 本轮没有 clear improvement；`scripts/update_weighted_winners.py` 后 Path1 window winner、composite component、tracked/live/public payload 未切换。本轮新增策略预算用于 A股 Path2/3/4 与 HK Path1/2/3，Path1 无 evict。
- core_multifactor 子段仍以代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` / `PATH1_FAST_PASS_VARIANT_IDS` 为准；本轮只确认覆盖完整，不把 Path4 emergent_theme 结果并入 Path1 core_multifactor。
- 最终 focus 为 `satellite_risk_cost`。下一轮第一条命令建议回到 satellite defense 风险/成本邻域，而不是复跑本轮未改写的多因子旧候选：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk08_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-17 05:20 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 54/54 complete`、`ashare_path1_fast_family 118/118 complete`；本轮 Path1 只做 `scripts/winner_only_pass.py` 巡检与 weighted 同步，新增预算投给 A股 Path4 与 HK Path4-7，没有新增 Path1 `--only-base-ids` 回测。
- `winner_only_pass.py` 退出码为 `0`，没有发现相对 tracked winners 的 clear improvement。core_multifactor 子段继续按代码实际池 `54` 个 fast-pass 变体巡检，没有新增 overlay，也没有 Path1 evict。
- `scripts/update_weighted_winners.py` 后 Path1 window winner、robust candidate、tracked/live/public payload 均未被本轮同步改变；本轮命令类型为巡检/同步：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/export_live_platform_data.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/generate_public_snapshot.py`。
- 最终 focus 继续为 `core_multifactor_coverage`。下一轮第一条命令建议注册并确认更窄的质量/盈利信号，而不是继续堆叠 value/lowvol/trend：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-16 17:36 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 54/54 complete`、`ashare_path1_fast_family 118/118 complete`；上一轮预留的 core_multifactor `quality_profitability_value_lowvol_trend_signal_cashguard_risk18_reconfirm` 本轮已注册并五窗口确认，同时继续用 `scripts/winner_only_pass.py` 巡检旧 fast-pass clear-improvement。
- 本轮新增并五窗口确认 1 个 Path1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk18_reconfirm`。实际命令与 A股 Path2/3/4 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-15 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk18_reconfirm,...`。
- 该候选五窗口 CAGR 为 `4.83% / -2.38% / 20.03% / 40.60% / 27.54%`，最大回撤 `-31.18% / -30.01% / -12.19% / -8.65% / -2.55%`，换手 `2.76x / 2.45x / 2.62x / 4.88x / 5.67x`。结论：短窗风险可控但 2017/2020 失效，不替换 Path1 window winner、composite robust、tracked/live/public payload；本轮无 Path1 evict。
- `scripts/winner_only_pass.py` 仍提示旧 `risk25_reconfirm` 与 `share_22_78_hold_2_8_ramp64_cost_guard` 有分窗 clear-improvement；这些不是本轮新增实验。最终 focus 为 `signal_quality`，下一轮第一条命令建议改测更窄的质量/盈利信号而非继续堆叠 value/lowvol/trend：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-15 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk14_reconfirm`；若未注册，先加入 `WINNER_CORE_VARIANTS`、`PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-16 05:17 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 53/53 complete`、`ashare_path1_fast_family 117/117 complete`；本轮 Path1 只做 `scripts/winner_only_pass.py` 巡检和 weighted 同步，没有新增 Path1 `--only-base-ids` 回测，也没有 core_multifactor overlay 或 evict。
- `winner_only_pass.py` 仍提示旧候选存在 clear-improvement：`risk25_reconfirm` 指向 `since_2017_only`，`share_22_78_hold_2_8_ramp64_cost_guard` 指向 `since_2023_only`；这些是既有 fast-pass 信号，本轮不把它们记为新增策略实验。
- `scripts/update_weighted_winners.py` 后 Path1 window winner、robust candidate、tracked/live/public payload 均未被本轮其它路径同步改变；Path1 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm`，本轮无 Path1 evict。
- 最终 rotation focus 转为 `core_multifactor_coverage`。下一轮第一条命令建议注册并确认一个更强调质量/盈利/价值/低波/趋势信号的多因子风险确认：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk18_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-15 17:18 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 53/53 complete`、`ashare_path1_fast_family 117/117 complete`。上一轮预留的 satellite defense `risk10_reconfirm` 本轮已注册并五窗口确认；core_multifactor 子段只按代码实际池巡检，没有新增 overlay，也没有 evict。
- 本轮新增并五窗口确认 1 个 Path1 fast-pass base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm`。实际命令与 A股 Path2/3 合并执行，命令类型为 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- `risk10_reconfirm` 五窗口 CAGR 为 `23.21% / 27.32% / 25.99% / 94.42% / 87.30%`，最大回撤为 `-12.13% / -13.26% / -18.26% / -10.91% / -6.61%`，Sharpe 为 `0.99 / 1.00 / 0.91 / 1.80 / 1.98`，换手为 `2.96x / 3.32x / 3.49x / 4.63x / 7.35x`。结论：它进入 Path1 robust leaderboard 第 2，但 promotion score 仍略低于 `risk14_reconfirm`；不替换 window winner、robust candidate 或 tracked/live/public payload。
- 最终 rotation focus 为 `holding_shape`。下一轮第一条命令建议回到持仓形态修复，而不是继续 satellite risk 邻域：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard`；若下一轮 rotation 转回 `core_multifactor`，再注册新的多因子 overlay 并单独计入 Path1 预算。

## 本轮执行计划（2026-06-15 05:39 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 53/53 complete`、`ashare_path1_fast_family 116/116 complete`；本轮没有新增 Path1 `--only-base-ids` 回测，预算投给 A股 Path2/3/4、Path5 事件入口与 HK Path4-7。core_multifactor 子段按代码实际池巡检为 `53` 个，没有新增 overlay，也没有 Path1 evict。
- 本轮 Path1 命令类型为 fast-pass 巡检：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`。脚本退出码 `2` 表示仍存在旧候选 clear-improvement：`risk25_reconfirm` 指向 `since_2017_only`，`share_22_78_hold_2_8_ramp64_cost_guard` 指向 `since_2023_only`；这些不是本轮新增实验。
- `scripts/update_weighted_winners.py` 后 Path1 composite/robust 未切换：robust component 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm`；window winner、robust candidate、tracked/live/public payload 均未改变。
- 最终 rotation focus 为 `satellite_risk_cost`。下一轮第一条命令应回到 satellite defense 风险/成本压缩，而不是继续复跑旧 clear-improvement：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-14 17:25 CST）

- 开局 guard 为 `pass`，`ashare_path1_core_multifactor 53/53 complete`、`ashare_path1_fast_family 116/116 complete`；本轮没有新增 Path1 `--only-base-ids`，预算投给 A股 Path2/3/4、Path5 事件入口与 HK Path1/2/3。core_multifactor 子段按代码实际池巡检，没有新增 overlay，也没有 Path1 evict。
- `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py` 完成 fast-pass 巡检，退出码 `2` 仅表示旧候选存在 clear-improvement 提示：`risk25_reconfirm` 指向 `since_2017_only`，`share_22_78_hold_2_8_ramp64_cost_guard` 指向 `since_2023_only`；这两条都不是本轮新增实验。
- `scripts/update_weighted_winners.py` 后 Path1 composite 未切换：robust component 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm`，composite 指标维持 `meanCAGR=41.56%`、`minCAGR=21.71%`、最差回撤 `-16.18%`、平均换手 `4.39x`；window winner、robust candidate、tracked/live/public payload 均未改变。
- 中段 guard 将 rotation focus 推到 `core_multifactor_coverage`。下一轮第一条动作应先注册并确认一个多因子覆盖对照，而不是复跑旧 satellite：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk18_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-14 05:29 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 53/53 complete`、`ashare_path1_fast_family 116/116 complete`；本轮没有新增 Path1 `--only-base-ids` 回测，预算投给 A股 Path2/3/4、Path5 事件篮子与 HK Path1/5/6/7。Path1 完成 `winner_only_pass.py` 巡检，仍只给旧 clear-improvement 提示：`risk25_reconfirm` 在 `since_2017_only`、`share_22_78_hold_2_8_ramp64_cost_guard` 在 `since_2023_only`，不计作新增策略实验。
- `scripts/update_weighted_winners.py` 后 Path1 composite 未切换：robust component 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm`；window winner、robust candidate、tracked/live/public payload 均未改变。core_multifactor 子段本轮只按代码实际池巡检，没有新增 overlay，也没有 Path1 evict。
- 本轮命令类型为巡检和同步：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/export_live_platform_data.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/generate_public_snapshot.py`。
- 最终 rotation focus 为 `holding_shape`。下一轮第一条命令应优先把旧 clear-improvement 的持仓形态做五窗口确认，而不是复跑 satellite id：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard`；若下一轮 rotation 转回 core_multifactor，再设计新的多因子 overlay 并单独计入 Path1 预算。

## 本轮执行计划（2026-06-13 17:30 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 53/53 complete`、`ashare_path1_fast_family 116/116 complete`；本轮没有新增 Path1 `--only-base-ids` 回测，预算投给 A股 Path2/3/4、Path5 事件篮子与 HK Path1-4。`scripts/winner_only_pass.py` 仍只给旧候选 clear-improvement 提示：`risk25_reconfirm` 在 `since_2017_only`、`share_22_78_hold_2_8_ramp64_cost_guard` 在 `since_2023_only`，不计为新增实验。
- `scripts/update_weighted_winners.py` 后 Path1 composite 未切换：robust component 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm`，composite 指标为 `meanCAGR=41.56%`、`minCAGR=21.71%`、最差回撤 `-16.18%`、平均换手 `4.39x`；window winner、robust candidate、tracked/live/public payload 均未改变。
- 本轮命令类型为巡检和同步：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`。core_multifactor 子段本轮只读取代码实际池并保持 `53` 个覆盖，没有新增 overlay，也没有 Path1 evict。
- 最终 rotation focus 为 `satellite_risk_cost`。下一轮第一条命令建议回到 satellite defense，把 `risk14_reconfirm` 的浅回撤继续向下压而不复跑旧 id：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-13 05:09 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 53/53 complete`、`ashare_path1_fast_family 116/116 complete`；本轮没有新增 Path1 `--only-base-ids` 回测，预算投给 HK 五窗口确认与 Path5 事件篮子。`scripts/winner_only_pass.py` 巡检 `115` 个 fast-pass base candidates / `1265` 条组合，core_multifactor 仍按代码实际池 `53` 个覆盖。
- 上一轮 candidate `risk14_reconfirm` 仍是 Path1 composite 组件；本轮 `scripts/update_weighted_winners.py` 后 Path1 composite 维持 `meanCAGR=41.56%`、`minCAGR=21.71%`、最差回撤 `-16.18%`、平均换手 `4.39x`，没有新的 Path1 window winner 或 tracked payload 切换。
- 本轮候选 ID 与命令：巡检命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`；同步命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`。`winner_only_pass.py` 仍提示旧 `risk25_reconfirm` 在 `since_2017_only`、旧 `share_22_78_hold_2_8_ramp64_cost_guard` 在 `since_2023_only` 有 clear improvement，但这是旧候选复核信号，不计为本轮新增策略实验。
- core_multifactor 子段本轮只巡检，没有新增 overlay，也没有 Path1 evict。下一轮 focus 继续映射到 `core_multifactor_coverage`，第一条命令仍应注册并确认一个更强调质量/盈利/价值/低波/趋势信号的多因子防守对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk18_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS`。

## 本轮执行计划（2026-06-12 05:28 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 53/53 complete`、`ashare_path1_fast_family 116/116 complete`。上一轮 Path1 core `quality_profitability_growth_trend_signal_cashguard_risk16_reconfirm` 未改 winner/robust；本轮 rotation 指向 `satellite_risk_cost`，因此只注册并确认 1 个 satellite defense 风险下调候选，同时继续按代码实际池巡检 core_multifactor。
- 本轮新增并五窗口确认 1 个 Path1 fast-pass base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，合并命令覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，并显式锁定 `--end-date 2026-06-11`。
- `risk14_reconfirm` 五窗口 CAGR 为 `23.50% / 28.87% / 24.51% / 94.09% / 87.03%`，最大回撤为 `-12.84% / -12.02% / -18.28% / -10.91% / -6.61%`，Sharpe 为 `1.00 / 1.05 / 0.88 / 1.80 / 1.98`，换手为 `2.99x / 3.33x / 3.47x / 4.62x / 7.35x`。结论：回撤质量优于上一轮 risk16/risk20 邻域，`scripts/update_weighted_winners.py` 将 Path1 composite robust component 切到本轮 `risk14_reconfirm`，target weight `45%`；但 Path1 window winners 未切换。
- core_multifactor 子段本轮只巡检，按代码实际池为 `53` 个，没有新增 overlay；`scripts/winner_only_pass.py` 仍以 exit `2` 提示旧候选在部分窗口有 clear improvement，本轮不把旧提示记作新实验。本轮没有 Path1 evict。
- 最终 guard 将下一轮 focus 推到 `core_multifactor_coverage`。下一轮第一条命令建议注册并确认一个更强调质量/盈利/价值/低波/趋势信号的多因子防守对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk18_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 后再跑。

## 本轮执行计划（2026-06-07 16:06 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 46/46 complete`、`ashare_path1_fast_family 107/107 complete`。上一轮已把下一候选指向 satellite risk/cost，本轮按该方向注册并五窗口确认 `risk12_reconfirm`，同时继续巡检 core_multifactor 实际池。
- 本轮新增并五窗口确认 1 个 Path1 fast-pass base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk12_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖窗口为 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- `risk12_reconfirm` 五窗口 CAGR 为 `22.53% / 28.17% / 29.70% / 88.55% / 70.92%`，最大回撤为 `-12.74% / -14.73% / -20.68% / -11.07% / -6.83%`，Sharpe 为 `0.99 / 1.04 / 0.96 / 1.69 / 1.65`，换手为 `2.98x / 3.41x / 3.55x / 4.81x / 7.34x`。结论：回撤显著浅，但收益低于旧 `risk20_reconfirm` 和 official Path1 winner，不替换 window winner、robust candidate 或 tracked/live/public payload。
- `scripts/winner_only_pass.py` 仍提示旧 `risk20_reconfirm` 在 `since_2020_only` 有 fast-pass clear improvement；`scripts/update_weighted_winners.py` 后 official Path1 仍未采纳该 fast-pass，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。本轮没有 Path1 evict。
- 最终 guard 将下一轮 focus 推到 `core_multifactor_coverage`。下一轮第一条命令建议注册一个不同于现有 signal/cashguard 的多因子趋势防守对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cashguard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 后再跑。

## 本轮执行计划（2026-06-07 04:26 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 46/46 complete`、`ashare_path1_fast_family 106/106 complete`。上一轮按 `core_multifactor_coverage` 记录 `quality_profitability_value_lowvol_industry_cost_guard_reconfirm`，本轮按 rotation focus `satellite_risk_cost` 与上一轮 next command 补齐新 core_multifactor signal/cashguard 对照，同时巡检 fast-pass。
- 本轮新增并五窗口确认 1 个 Path1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，实际补覆盖命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal30_leader78_coverage_penalty_risk18_cap14_exit66_lowturn`。
- 新 core_multifactor 五窗口 CAGR 为 `15.01% / 14.86% / 29.84% / 60.45% / 62.63%`，最大回撤为 `-28.50% / -26.64% / -15.98% / -15.24% / -4.62%`，Sharpe 为 `0.82 / 0.74 / 1.13 / 1.42 / 2.27`，换手为 `2.70x / 2.95x / 3.04x / 5.04x / 5.46x`。结论：2023 与短窗尚可，但 2017/2020 不足，不替换 Path1 window winner、robust candidate、tracked/live/public payload。
- `scripts/winner_only_pass.py` 仍以 exit `2` 提示旧 satellite defense 候选在 `since_2020_only` 有 clear improvement；`scripts/update_weighted_winners.py` 后 official winner 仍未切换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。本轮没有 Path1 evict。
- 最终 guard 将下一轮 focus 继续推到 `satellite_risk_cost`。下一轮第一条命令建议不再扩弱多因子同形，回到卫星风险/成本线的更浅回撤确认：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk12_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 后再跑。

## 本轮执行计划（2026-06-06 16:17 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 45/45 complete`、`ashare_path1_fast_family 105/105 complete`。上一轮 Path1 按 `holding_shape` 确认 `share_20_80_hold_2_8_ramp66_cost_guard`，短窗强但未改 official winner/robust；本轮按 rotation/recommended focus `core_multifactor_coverage` 新增 1 个 core_multifactor 确认候选。
- 本轮新增并五窗口确认：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_cost_guard_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，实际合并命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_cost_guard_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn03_exit96_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk18_cap14_exit66_lowturn`。
- 新 core_multifactor 五窗口 CAGR 为 `14.88% / 13.22% / 30.42% / 59.55% / 63.47%`，最大回撤为 `-29.94% / -30.94% / -16.85% / -15.24% / -4.62%`，Sharpe 为 `0.81 / 0.67 / 1.14 / 1.41 / 2.29`，换手为 `2.74x / 2.99x / 3.06x / 4.99x / 5.48x`。结论：2023 和短窗可比较，但 2017/2020 仍低于 Path1 robust，不替换 window winner、robust candidate、tracked/live/public payload。
- `scripts/winner_only_pass.py` 仍以 exit `2` 提示旧 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 在 `since_2020_only` 有 clear improvement；本轮不把该旧信号当成新增结论。本轮没有触发 Path1 evict。
- 最终 guard 将下一轮 focus 推到 `signal_quality`。下一轮第一条命令建议注册并确认“质量+盈利+价值+低波+行业 + signal/cashguard”的 2017/2020 修复对照，而不是复跑本轮 id：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 后再跑。

## 本轮执行计划（2026-06-06 10:28 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 44/44 complete`、`ashare_path1_fast_family 104/104 complete`。上一轮 Path1 只做巡检且未新增回测；本轮按最终 focus `holding_shape` 五窗口确认 1 个 fast-pass 候选，core_multifactor 子段按代码实际池巡检为 `44` 个，没有新增 overlay。
- 本轮新增并确认：`core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard`。命令类型为五窗口 `--only-base-ids` 增量确认，合并命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_20_80_hold_2_8_ramp66_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution52_cap22_cost_guard_v21,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution52_cap22_cost_guard_v21,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap55_hold3_turn04_exit94_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn`。
- `share_20_80_hold_2_8_ramp66_cost_guard` 五窗口 CAGR 为 `19.69% / 23.26% / 35.64% / 97.25% / 102.72%`，最大回撤为 `-20.92% / -17.10% / -20.25% / -10.33% / -11.99%`，换手为 `2.65x / 2.98x / 2.97x / 4.45x / 5.59x`。相对近几轮 holding_shape 提升 2023 与短窗，但 2017/2020 仍不足以替换 Path1 official window winner、robust candidate 或 tracked/live/public payload。
- `scripts/winner_only_pass.py` 仍以 exit `2` 提示旧 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 在 `since_2020_only` 有 clear improvement；本轮不把该旧信号当作新结论。本轮未触发 Path1 evict。
- 最终 guard 将下一轮 focus 轮到 `core_multifactor_coverage`。下一轮第一条命令建议回到能修复 2017/2020 的多因子覆盖，而不是继续扩 holding_shape：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_cost_guard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 后再跑。

## 本轮执行计划（2026-06-06 04:23 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 44/44 complete`、`ashare_path1_fast_family 103/103 complete`。上一轮 `share_18_82_hold_2_8_ramp68_cost_guard` 改善短窗但未替换 Path1 winner/robust；本轮 Path1 只完成巡检，没有新增 Path1 回测 id，预算投给 A股 Path2/3/4 与 HK Path4/6/7。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 在 `since_2020_only` 有 clear improvement；`scripts/update_weighted_winners.py` 后 official Path1 window winner、robust candidate、tracked/live/public payload 均未切换。
- core_multifactor 子段按代码实际池仍为 `44` 个，本轮没有新增 overlay，也没有 Path1 evict。最终 rotation focus 为 `satellite_risk_cost`，下一轮第一条候选命令建议回到卫星防守成本/风险邻域，而不是继续扩弱多因子：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk12_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 后再跑增量。

## 本轮执行计划（2026-06-05 22:21 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 44/44 complete`、`ashare_path1_fast_family 103/103 complete`；本轮 `winner_only_pass.py` 仍以 exit 2 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 在 `since_2020_only` clear improvement，但 `scripts/update_weighted_winners.py` 后 official Path1 tracked 仍未切换。
- 本轮按上一轮 holding_shape 提示新增并五窗口确认 1 个 Path1 fast-pass 候选：`core_explore_80_20_total_mv_winner_core__share_18_82_hold_2_8_ramp68_cost_guard`。可复现命令为：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_18_82_hold_2_8_ramp68_cost_guard`。
- `share_18_82_hold_2_8_ramp68_cost_guard` 五窗口 CAGR 为 `20.14% / 22.78% / 34.85% / 95.78% / 98.88%`，最大回撤为 `-19.84% / -17.54% / -21.46% / -10.49% / -11.67%`，换手为 `2.65x / 2.97x / 2.94x / 4.43x / 5.50x`。相对上一轮 `share_16_84` 改善 2020/2023/短窗，但 2017 与 robust 质量仍不足，不替换 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段本轮只巡检，没有新增 overlay；代码实际池仍为 `44` 个。本轮未触发 Path1 evict。最终 rotation focus 为 `signal_quality`，下一轮第一条命令建议回到能修复 2017/2020 的多因子质量信号，而不是继续扩 holding_shape：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_industry_signal_cost_guard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 后再跑增量。

## 本轮执行计划（2026-06-05 10:22 CST）

- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 44/44 complete`、`ashare_path1_fast_family 102/102 complete`。`winner_only_pass.py` 仍以 exit 2 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 在 `since_2020_only` clear improvement，本轮 `update_weighted_winners.py` 仍未把它改写为 official winner。
- 本轮按上一轮计划新增并五窗口确认 1 个 Path1/core_multifactor 候选：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm`。实际合并增量命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk12_cap10_exit64,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn05_exit94_weekly`。
- 新多因子候选五窗口 CAGR 为 `14.77% / 14.62% / 30.31% / 60.22% / 63.61%`，最大回撤为 `-32.04% / -28.56% / -17.49% / -15.24% / -4.62%`，换手为 `2.76x / 3.00x / 3.11x / 5.05x / 5.48x`。结论：2023 与短窗尚可，但 2017/2020 仍弱于 Path1 robust，不替换 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段按代码实际池扩到 `44` 个，新增 overlay 只计入本轮 Path1 预算；本轮未触发 Path1 evict。最终 guard 将下一轮 focus 推到 `holding_shape`，第一条命令建议不再扩同形弱多因子，改测低 ramp/稳仓形态能否修复 2017/2020：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_18_82_hold_2_8_ramp68_cost_guard`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["holding_shape"]` 后再跑增量。

## 本轮执行计划（2026-06-05 04:11 CST）

- 最新 guard 为 `pass`，`ashare_path1_core_multifactor 43/43 complete`、`ashare_path1_fast_family 101/101 complete`。`winner_only_pass.py` 仍只提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 在 `since_2020_only` clear improvement，本轮没有把它改写为 official winner。
- 本轮纳入并五窗口确认 1 个 Path1/core_multifactor 候选：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`。可复现增量命令为：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`。
- 该候选五窗口 CAGR 为 `15.16% / 13.37% / 27.58% / 59.17% / 64.53%`，最大回撤为 `-32.53% / -30.50% / -20.25% / -14.09% / -4.62%`，换手为 `2.77x / 3.19x / 3.44x / 5.16x / 5.49x`。结论：短窗弹性可用，但 2017/2020 收益和回撤仍弱于 Path1 robust，不替换 window winner、robust candidate 或 tracked payload。
- 本轮未触发 Path1 evict。最新 rotation focus 为 `signal_quality`；下一轮第一条命令建议改测“质量+盈利+低波/行业信号”的长窗修复，而不是继续追 2026 弹性：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_signal_cost_guard_reconfirm`；若未注册，先加入 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 后再跑增量。

## 本轮执行计划（2026-06-04 16:16 CST）

- 开局 guard 为 `pass`，`PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 按代码实际返回为 `42` 个，fast-family 为 `99/99 complete`。`winner_only_pass.py` 仍只提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 在 `since_2020_only` clear improvement，本轮不把它当新结论。
- 本轮按 `holding_shape` 新增并五窗口确认 1 个 Path1 fast-pass 候选：`core_explore_80_20_total_mv_winner_core__share_16_84_hold_2_8_ramp70_cost_guard`。合并增量命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_16_84_hold_2_8_ramp70_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold3_turn08_exit92_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal28_leader72_risk15_cap12_exit64`。
- `share_16_84_hold_2_8_ramp70_cost_guard` 五窗口 CAGR 为 `20.67% / 22.73% / 33.59% / 93.39% / 90.12%`，最大回撤为 `-18.72% / -17.84% / -22.60% / -10.65% / -11.71%`，换手为 `2.65x / 2.96x / 2.96x / 4.41x / 5.44x`。它改善短窗弹性，但未超过 Path1 composite 的 2017/2020/2023 质量，也未替换 window winner、robust candidate 或 tracked payload。
- 本轮未新增 core_multifactor overlay，未触发 Path1 active evict。下一轮 focus 继续映射到 `holding_shape` 与 `satellite_risk_cost`：第一条命令建议只确认一个更接近既有 robust 的持仓形态，而不是继续扩弱多因子：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_18_82_hold_2_8_ramp70_cost_guard`；若未注册，先加入 Path1 `holding_shape` 后再跑增量。

## 本轮执行计划（2026-06-04 10:16 CST）

- 开局 guard 为 `pass`，无 blocking/warning coverage；`PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 按代码实际池巡检为 `42` 个变体，`winner_only_pass.py` 评估 `path1_fast_family base_candidates=98`、`evaluated=241`，仍只在 `since_2020_only` 给出旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` clear improvement。`scripts/update_weighted_winners.py` 后 Path1 window winner、robust candidate 与 tracked payload 未切换。
- 本轮没有新增 Path1 official fast-pass base；预算用于把最新 core_multifactor 低相关形态纳入 Path2 universe 后做交叉验证。复核的两个多因子底座为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm`，与 Path3 周频候选合并命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit90_weekly`。
- `80/20 equal_weight` 五窗口 CAGR 为 `15.27% / 14.85% / 28.12% / 53.58% / 58.78%`，最大回撤 `-31.22% / -28.31% / -17.93% / -15.53% / -13.55%`；`90/10 equal_weight` 为 `15.01% / 14.70% / 25.98% / 63.12% / 48.89%`，最大回撤 `-32.72% / -30.67% / -18.70% / -16.50% / -11.37%`。结论：短窗弹性尚可，但 2017/2020 不足，不能替换 Path1 robust，也不触发 evict。
- 下一轮 focus 继续优先 `satellite_risk_cost` 与 `core_multifactor_coverage` 的交叉点，不再单纯扩弱多因子。第一条命令建议确认一个能把 `risk20_reconfirm` 的浅回撤和多因子质量结合的总市值底座：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_quality_profitability_reconfirm`；若尚未注册，先在 `PATH1_FAST_PASS_DIRECTION_GROUPS["satellite_defense"]` 中注册后再跑增量。

## 本轮执行计划（2026-06-03 22:20 CST）

- 开局 guard 先因 Path4 blocking 与 Path1 fast-family warning 报 `block`；按 rerun command 只补缺口，没有改跑全量。Path1 本轮补齐 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm` 四窗口，命令为：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`。
- `risk18_reconfirm` 四窗口 CAGR 为 `21.99% / 29.70% / 29.13% / 84.60%`，最大回撤为 `-14.22% / -14.73% / -21.31% / -11.70%`，换手为 `3.00x / 3.40x / 3.51x / 4.91x`。它比旧 `risk20_reconfirm` 的 2020 CAGR 弱，收益质量不足以替换 Path1 winner 或 robust。
- core_multifactor 子段按代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 巡检为 `41/41 complete`；本轮没有新增多因子 overlay。`scripts/update_weighted_winners.py` 后 Path1 window winner、robust candidate 与 tracked payload 未被 `risk18` 替换，候选池未触发 evict。
- 最新 guard 为 `pass`，`ashare_path1_fast_family 98/98 complete`，下一轮 focus 仍是 `core_multifactor_coverage`。第一条命令建议不要继续下调 satellite risk，改回能修复 2017/2020 的多因子低波/盈利/行业防守组合：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_coverage_id>`。

## 本轮执行计划（2026-06-02 16:20 CST）

- 开局 guard 为 `pass`，上一轮 `share_12_88_hold_2_8_ramp75_cost_guard` 只保留短窗弹性，不能替换 Path 1 robust。本轮按 rotation 的 `core_multifactor_coverage/signal_quality` 回到代码实际 `core_multifactor` 池，新增质量+价值+行业强度成本守门再确认；注册后 guard 给出 `ashare_path1_core_multifactor 1/39 missing` 与 Path4 blocking，已按 `--only-base-ids` 增量补齐，没有改跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm`。blocking 补齐命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap12_exit68`。
- `quality_value_industry_cost_guard_reconfirm` 五窗口 CAGR 为 `14.58% / 15.59% / 29.18% / 65.87% / 99.32%`，最大回撤为 `-31.90% / -29.95% / -19.82% / -14.10% / -4.62%`，换手为 `2.80x / 3.21x / 3.45x / 5.24x / 5.92x`。它比上一轮多因子短窗更稳，但 2017/2020 仍明显低于 Path 1 robust，不晋级。
- `scripts/winner_only_pass.py` 以退出码 `2` 提示既有 satellite_defense 候选在 `since_2020_only` 与 `since_2025_only` 有 clear improvement；`scripts/update_weighted_winners.py` 后 official Path 1 window winner、robust/tracked payload 未被本轮多因子候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。本路径未触发 evict。
- 最新 guard 为 `pass`，`ashare_path1_core_multifactor 39/39 complete`，下一轮 focus 为 `signal_quality`。第一条命令建议不要继续增加价值/行业同形组合，改测能修复 2017/2020 的质量+低波/盈利+行业防守信号：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_signal_quality_core_multifactor_id>`。

## 本轮执行计划（2026-06-02 13:49 CST）

- 开局 guard 为 `pass`；上一轮 `risk15_reconfirm` 证明 satellite_defense 降风险不能替换 `risk20` 或 official robust。本轮按 rotation 的 `holding_shape`，新增 `12/88 + 2/8 hold + ramp75 + cost_guard` 稳仓形态，目标是检验低 ramp/高 promoted 持有是否能把短窗弹性转化为更稳定的 Path 1 robust。注册后 guard 一度给 `ashare_path1_fast_family 1/93 missing`，已按增量 `--only-base-ids` 补齐，没有改跑全量。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__share_12_88_hold_2_8_ramp75_cost_guard`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_12_88_hold_2_8_ramp75_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap65_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap65_biweekly_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk20_cap66_hold7_turn04_exit94_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_leader68_risk20_cap16_exit68`。
- `share_12_88_hold_2_8_ramp75_cost_guard` 五窗口 CAGR 为 `21.21% / 22.41% / 33.15% / 100.15% / 112.22%`，最大回撤为 `-18.48% / -18.23% / -23.67% / -10.99% / -11.94%`，换手为 `2.68x / 2.98x / 3.00x / 4.52x / 5.95x`。结论是短窗弹性还在，但 2017/2020/2023 明显低于现有 Path 1 robust，不晋级。
- core_multifactor 子段按代码实际池巡检为 `38/38 complete`，本轮没有新增 core_multifactor overlay。`scripts/winner_only_pass.py` 仍以退出码 `2` 提示既有 satellite_defense 候选在 `since_2020_only` 与 `since_2025_only` 有 clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust/tracked payload 未被本轮 holding_shape 候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。本路径未触发 evict。
- 最终 guard 为 `pass`：`ashare_path1_core_multifactor 38/38 complete`、`ashare_path1_fast_family 93/93 complete`。下一轮 focus 为 `core_multifactor_coverage`；第一条命令建议回到代码实际多因子池，新增一个能修复 2017/2020 的低回撤质量/盈利/行业组合，而不是继续扩 2+8 稳仓线：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-06-02 04:20 CST）

- 开局 guard 为 `pass`；上一轮 `quality_growth_industry_cost_guard_reconfirm` 只改善短窗弹性，不替换 Path 1 winner/robust。本轮按开局 rotation 的 `satellite_risk_cost` 继续压 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard` 的熊市保留，从 `risk20` 降到 `risk15`；最终 guard 为 `pass`，下一轮 focus 轮换到 `holding_shape`。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk15_reconfirm`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk15_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm88_caution62_cap50_cost_guard_v13,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm88_caution62_cap50_cost_guard_v13,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit96_weekly`。
- `risk15_reconfirm` 五窗口 CAGR 为 `23.21% / 31.49% / 32.89% / 106.24% / 129.43%`，最大回撤为 `-14.25% / -14.73% / -21.34% / -11.70% / -6.83%`，换手为 `3.01x / 3.42x / 3.55x / 4.89x / 8.42x`。它继续证明卫星三段式能给浅回撤和 2026 弹性，但 2020 CAGR 低于 `risk20_reconfirm` 的 `34.38%`，不替换 official Path 1 window winner 或 robust。
- core_multifactor 子段按代码实际池巡检为 `38/38 complete`，本轮没有新增 core_multifactor overlay；`scripts/winner_only_pass.py` 以退出码 `2` 提示 `risk20_reconfirm` 仍是 `since_2020_only` clear improvement，`risk15` 只在 `since_2025_only` 名义靠前。`scripts/update_weighted_winners.py` 后 Path 1 tracked/robust 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`；本路径未触发 evict。
- 下一轮 focus 为 `holding_shape`。第一条命令建议停止继续降低 satellite risk，回到低 ramp/稳仓形态检验能否把 `risk20` 的收益质量转化为更稳 robust：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-06-01 22:30 CST）

- 开局 guard 为 `pass`；注册本轮 Path 1/core_multifactor 与 Path 4 active 后，guard 按预期变为 `block`：`ashare_path1_core_multifactor 1/38 missing`、`ashare_path4_emergent_theme 3/60 missing`。已按 rerun command 只补 `--only-base-ids`，没有改跑全量。上一轮 `risk20_reconfirm` 是旧 satellite 风险线的 clear-improvement 候选，但 `update_weighted_winners.py` 仍未切换 official robust；本轮按 rotation 的 `signal_quality` 回到代码实际 core_multifactor 池。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_industry_cost_guard_reconfirm`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_industry_cost_guard_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk34_mom_exit52_reconfirm86_caution64_cap48_cost_guard_v12,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk34_mom_exit52_reconfirm86_caution64_cap48_cost_guard_v12,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap66_hold7_turn04_exit94_weekly,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal24_risk25_cap16_exit70`。
- `quality_growth_industry_cost_guard_reconfirm` 五窗口 CAGR 为 `13.44% / 14.80% / 29.90% / 69.60% / 100.39%`，最大回撤为 `-34.39% / -29.29% / -19.78% / -13.85% / -4.62%`，换手为 `2.85x / 3.10x / 3.42x / 5.26x / 5.93x`。它在 `since_2026_01` core_multifactor 子池排名靠前，但 2017/2020 太弱，不替换 Path 1 window winner 或 robust。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 fast-pass 候选在 `since_2020_only` 和 `since_2025_only` 有 clear improvement；`scripts/update_weighted_winners.py` 后 official Path 1 window winner、robust/tracked payload 未被本轮多因子候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。最终 guard 为 `pass`，`ashare_path1_core_multifactor 38/38 complete`、`ashare_path1_fast_family 91/91 complete`；本路径未触发 evict。
- 下一轮 focus 仍为 `signal_quality`。第一条命令建议不要继续只追 2026 弹性，改测一个带低波/防守约束的质量+行业信号组合，目标先修复 2017/2020：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_signal_quality_core_multifactor_id>`。

## 本轮执行计划（2026-06-01 10:27 CST）

- 开局与收尾 guard 均为 `pass`，无 blocking coverage；上一轮 `quality_industry_signal_cashguard_reconfirm` 只强化 2026 弹性。本轮按上一轮 `satellite_risk_cost` 提示回到 `aggr_05_95_prom7` 卫星三档成本守门邻域，把熊市保留进一步降到 `risk20`，测试是否能在不牺牲 2020 的前提下压回撤。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。
- `risk20_reconfirm` 五窗口 CAGR 为 `24.44% / 34.38% / 38.44% / 104.65% / 129.41%`，最大回撤为 `-14.02% / -14.73% / -21.55% / -11.70% / -6.83%`，换手为 `3.03x / 3.38x / 3.56x / 5.03x / 8.42x`。它相对 `risk25_reconfirm` 进一步改善 2020 CAGR，并被 `scripts/winner_only_pass.py` 标记为 `since_2020_only` clear improvement：相对当前 tracked 2020 winner CAGR +`1.78%`、Sharpe +`0.3097`、MaxDD 从 `-55.00%` 降到 `-14.73%`。
- `scripts/update_weighted_winners.py` 重跑后 official Path 1 window winner、robust candidate 与 weighted tracked payload 仍未切换；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。core_multifactor 子段按代码实际池巡检为 `37/37 complete`，本轮没有新增 Path 1/core_multifactor overlay；`quality_value_trend_cost_guard_reconfirm` 作为 Path 2 低相关候选单独记录。候选池未触发 Path 1 evict。
- 下一轮 focus 为 `holding_shape`。第一条命令建议不要继续压卫星风险，改测 2+8 低 ramp 稳仓形态以判断 `risk20` 的收益是否能转化为更稳定 robust，例如先注册 `core_explore_80_20_total_mv_winner_core__share_06_94_hold_2_8_ramp75_cost_guard`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_06_94_hold_2_8_ramp75_cost_guard`。

## 本轮执行计划（2026-06-01 04:18 CST）

- 开局 guard 为 `pass`；注册本轮 Path 1 core 与 Path 4 强主题新 active 后，guard 变为 `block`：`ashare_path1_core_multifactor 1/37 missing`、`ashare_path4_emergent_theme 3/60 missing`。已按 rerun command 只补 `--only-base-ids`，没有改跑全量。上一轮 `profitability_growth_signal_reconfirm` 只强化 2026 弹性，不改善 2017/2020；本轮继续在代码实际 core_multifactor 池做质量+行业+信号+现金守门再确认。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_industry_signal_cashguard_reconfirm`。与 Path 4 blocking 合并补齐命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_industry_signal_cashguard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72,core_explore_90_10_equal_weight_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72,core_explore_90_10_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal24_risk30_cap18_exit72`。
- `quality_industry_signal_cashguard_reconfirm` 五窗口 CAGR 为 `14.75% / 12.81% / 15.31% / 65.63% / 99.25%`，最大回撤为 `-30.49% / -25.07% / -13.36% / -14.56% / -4.62%`，换手为 `2.77x / 3.32x / 3.59x / 5.16x / 5.92x`。现金守门继续给 2026 弹性和较浅短窗回撤，但 2017/2020/2023 收益太弱，不替换 Path 1 window winner/robust。
- `scripts/update_weighted_winners.py` 后 Path 1 official winner、robust candidate 与 tracked payload 未被本轮候选替换；robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。当前 guard scope：`ashare_path1_core_multifactor 37/37 complete`、`ashare_path1_fast_family 88/88 complete`；本路径未触发 evict。
- 下一轮 focus 为 `satellite_risk_cost`。第一条命令建议不要继续叠多因子现金守门，回到旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` clear-improvement 邻域，注册一个更低风险/更低成本的卫星再确认，例如 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-31 22:26 CST）

- 开局 guard 为 `pass`，但注册本轮 Path 1 core 与 Path 4 新 active 后，guard 变为 `block`：`ashare_path1_core_multifactor 1/36 missing`、`ashare_path4_emergent_theme 3/60 missing`。上一轮 `risk25_reconfirm` 保留 2020 强度但未替换 winner/robust；本轮按 rotation 的 `core_multifactor_coverage` 回到代码实际 core_multifactor 池，新增盈利+成长+行业信号再确认组合。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_growth_signal_reconfirm`。与 Path 4 blocking 一起的补齐命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_growth_signal_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72,core_explore_90_10_equal_weight_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72,core_explore_90_10_total_mv_winner_core__aggr_12_88_prom11_emergent_theme_quality_gate_signal22_risk30_cap18_exit72`。
- `profitability_growth_signal_reconfirm` 五窗口 CAGR 为 `13.67% / 14.77% / 30.71% / 72.83% / 100.39%`，最大回撤为 `-32.71% / -29.48% / -19.79% / -14.31% / -4.62%`，换手为 `2.86x / 3.19x / 3.37x / 5.47x / 5.93x`。它改善 2026 弹性且 2023 风险调整尚可，但 2017/2020 太弱，不替换 Path 1 window winner/robust。
- `winner_only_pass.py` 仍以 code `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 在 `since_2020_only` 有 clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 official winners/robust 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。core_multifactor 池按代码实际返回为 `36/36 complete`，候选池未触发 evict。
- 最终 guard 后下一轮 focus 仍会在 `core_multifactor_coverage` 与停滞 rotation 中轮换；第一条命令建议不要继续只加盈利成长信号，改测一个低回撤 core overlay 或回到 `holding_shape` 低 ramp 稳仓，命令模板：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_or_holding_shape_id>`。

## 本轮执行计划（2026-05-31 16:20 CST）

- 开局 guard 为 `pass`；上一轮 `profitability_industry_signal_reconfirm` 只改善 2026 弹性，不改善 Path 1 robust。本轮先按 guard 提示补齐 Path 4 blocking，再回到 `satellite_risk_cost` 的 `aggr_05_95_prom7` 卫星三档邻域，新增 `risk25_reconfirm`，目标是相对旧 clear-improvement 候选继续压回撤与换手。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk25_reconfirm`。
- `risk25_reconfirm` 五窗口 CAGR 为 `25.43% / 33.37% / 39.59% / 102.81% / 129.40%`，最大回撤为 `-12.83% / -14.73% / -19.62% / -11.66% / -6.83%`，换手为 `3.04x / 3.39x / 3.60x / 5.02x / 8.42x`。它保留了 2020 强度并显著浅于 `dd_guard50` 回撤，但 2020 CAGR 仍低于旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `34.00%`，不替换 official window winner。
- core_multifactor 子段按代码实际池巡检为 `35/35 complete`，本轮未新增 core_multifactor overlay；`scripts/winner_only_pass.py` 仍只提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 在 `since_2020_only` 有 clear improvement。`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust/tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `holding_shape`。第一条命令建议暂停继续压卫星风险，回到低 ramp 持仓形态，注册一个不同于近期 2+8/3+7 失败组的稳仓对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-31 10:26 CST）

- 开局 guard 为 `pass`；上一轮 focus 指向 `signal_quality`，本轮回到代码实际 `core_multifactor` 池，新增盈利质量+行业强度+信号再确认组合 `aggr_08_92_prom6_core_multifactor_profitability_industry_signal_reconfirm`。注册后 guard 一度提示 Path 1 core 与 Path 4 新增候选缺口，本轮按 `--only-base-ids` 增量补齐，没有改跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_signal_reconfirm`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_signal_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk32_mom_exit52_reconfirm88_caution60_cap55_cost_guard_v8,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk32_mom_exit52_reconfirm88_caution60_cap55_cost_guard_v8,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap62_hold9_turn02_exit94_weekly,core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74,core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74,core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal22_risk35_cap20_exit74`。
- `profitability_industry_signal_reconfirm` 五窗口 CAGR 为 `14.22% / 13.72% / 29.44% / 69.71% / 100.16%`，最大回撤为 `-32.69% / -29.64% / -19.97% / -13.77% / -4.62%`，换手为 `2.85x / 3.05x / 3.39x / 5.32x / 5.94x`。它改善 2026 弹性但 2017/2020 收益太弱，不能替换 Path 1 robust。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 在 `since_2020_only` 有 clear improvement；`scripts/update_weighted_winners.py` 同步后 Path 1 的 `since_2020` window winner 为 `core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`，Path 1 composite/robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`core_multifactor=35`、Path 1 fast-family 完整，下一轮 focus 轮换为 `satellite_risk_cost`。第一条命令建议回到 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` clear-improvement 邻域，测试是否能降低 `dd_guard50` 的 2020 回撤/换手代价：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-31 04:21 CST）

- 开局 guard 为 `pass`；上一轮 focus 要求回到 `holding_shape`，本轮沿 2+8 低 ramp 持仓形态新增 `share_04_96_hold_2_8_ramp75_cost_guard`。代码实际 `core_multifactor` 池同步巡检为 `34/34 complete`，本轮没有新增 core_multifactor overlay。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__share_04_96_hold_2_8_ramp75_cost_guard`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_04_96_hold_2_8_ramp75_cost_guard`。
- `share_04_96_hold_2_8_ramp75_cost_guard` 五窗口 CAGR 为 `20.47% / 22.41% / 33.89% / 102.39% / 108.69%`，最大回撤为 `-20.71% / -19.95% / -22.87% / -11.63% / -11.99%`，换手为 `2.74x / 2.97x / 3.10x / 4.55x / 6.42x`。它继续证明低 ramp 持仓线可压回撤并保留短窗弹性，但 2017/2020/2023 仍低于现有 Path 1 robust，不晋级。
- `scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_fast_family 84/84 complete`、`ashare_path1_core_multifactor 34/34 complete`，下一轮 focus 轮换为 `signal_quality`。第一条命令建议回到代码实际多因子/信号质量池，注册区别于近期 lowvol/value 失败组的质量+盈利+行业强度再确认候选：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_signal_quality_or_core_multifactor_id>`。

## 本轮执行计划（2026-05-30 22:20 CST）

- 开局 guard 为 `pass`；上一轮建议回到 `satellite_risk_cost` 的 `aggr_05_95_prom7` 卫星三段式再确认。本轮按该方向新增 `risk30_reconfirm`，同时巡检代码实际 `core_multifactor` 池，最终仍为 `34/34 complete`，本轮没有把 Path 2 的等权质量成长多因子计入 Path 1 core_multifactor。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk30_reconfirm`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk30_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk25_cap58_hold10_turn02_exit94_weekly,core_explore_80_20_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76,core_explore_90_10_equal_weight_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76,core_explore_90_10_total_mv_winner_core__aggr_11_89_prom10_emergent_theme_quality_gate_signal20_risk35_cap25_exit76`。
- `risk30_reconfirm` 五窗口 CAGR 为 `21.98% / 32.32% / 34.99% / 102.83% / 129.39%`，最大回撤为 `-25.64% / -26.84% / -29.59% / -11.66% / -6.83%`，换手为 `3.13x / 3.36x / 3.66x / 5.01x / 8.42x`。它保留 2020 强度和 2026 弹性，但回撤明显劣于旧 `sat_three_stage_buffered_cost_guard`，不替换 Path 1 window winner/robust。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 robust/tracked payload 未被本轮候选替换，robust 为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_fast_family 83/83 complete`、`ashare_path1_core_multifactor 34/34 complete`，下一轮 focus 轮换为 `holding_shape`。第一条命令建议不要继续压卫星 risk，回到低 ramp 持仓形态，如 `core_explore_80_20_total_mv_winner_core__share_04_96_hold_2_8_ramp75_cost_guard` 或同等 2+8 更低进攻仓版本：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-30 16:22 CST）

- 开局 guard 为 `pass`；上一轮建议回到代码实际 `core_multifactor` 池，本轮按 `core_multifactor_coverage/signal_quality` 注册盈利+估值+现金守门组合，不凭文字假定 overlay 数量。注册后按 blocking scope 只补新 base 的五窗口覆盖。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_value_cashguard_reconfirm`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_value_cashguard_reconfirm`。
- `profitability_value_cashguard_reconfirm` 五窗口 CAGR 为 `16.40% / 14.43% / 16.58% / 67.10% / 99.10%`，最大回撤为 `-24.73% / -28.29% / -13.26% / -15.26% / -4.62%`，换手为 `2.79x / 3.32x / 3.63x / 5.13x / 5.92x`。它改善 2026 弹性和短窗回撤，但 2017/2020/2023 收益仍弱于 Path 1 robust，不晋级。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 composite/tracked payload 已同步，robust 组件为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`，window winner 未被本轮多因子候选替换。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 34/34 complete`、`ashare_path1_fast_family 82/82 complete`，下一轮 focus 轮换为 `satellite_risk_cost`。第一条命令建议回到旧 `aggr_05_95_prom7` 卫星三段式 clear-improvement 邻域，注册更低风险阈值/成本守门再确认，例如 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk30_reconfirm`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-30 10:17 CST）

- 开局 guard 为 `pass`，上一轮 `quality_lowvol_value_reconfirm` 只提供 2026 弹性，未改善 Path 1 robust。本轮按 final rotation 的 `holding_shape`，新增 `2+8 / ramp80 / cost_guard` 的更进攻持仓形态；core_multifactor 子段按代码实际池完成巡检，仍为 `33/33 complete`，本轮没有新增多因子 overlay。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__share_06_94_hold_2_8_ramp80_cost_guard`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_06_94_hold_2_8_ramp80_cost_guard`。
- `share_06_94_hold_2_8_ramp80_cost_guard` 五窗口 CAGR 为 `21.03% / 22.36% / 33.32% / 100.90% / 109.61%`，最大回撤为 `-19.23% / -19.42% / -23.21% / -11.47% / -11.67%`，换手为 `2.71x / 2.98x / 3.06x / 4.53x / 6.29x`。它延续了低 ramp 持仓线的短窗弹性，但 2017/2020/2023 仍低于当前 Path 1 robust，不晋级。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_fast_family 81/81 complete`、`ashare_path1_core_multifactor 33/33 complete`，下一轮 focus 轮换为 `core_multifactor_coverage`。第一条命令建议回到代码实际多因子池，注册区别于近期 quality/lowvol/value 失败组的盈利+估值+现金守门组合，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_value_cashguard_reconfirm`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-30 04:31 CST）

- 开局 guard 为 `pass`，coverage 已完整；上一轮 `quality_value_trend_cost_guard_reconfirm` 只改善 2026 弹性，未替换 Path 1 robust。本轮按上一轮提示回到代码实际 `core_multifactor` 池，新增质量+低波+估值再确认组合，仍只用五窗口 `--only-base-ids` 增量确认。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_value_reconfirm`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_value_reconfirm`。
- `quality_lowvol_value_reconfirm` 五窗口 CAGR 为 `11.84% / 12.24% / 25.77% / 66.63% / 95.03%`，最大回撤为 `-46.20% / -41.96% / -29.14% / -15.41% / -4.62%`，换手为 `2.97x / 3.46x / 3.86x / 5.18x / 5.81x`。它继续给出 2026 弹性，但 2017/2020 回撤和 2023 收益弱于现有 Path 1 robust，不晋级。
- core_multifactor 子段按代码实际池提升为 `33/33 complete`，fast family 为 `80/80 complete`；`scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement。`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `satellite_risk_cost`。第一条命令建议回到旧 `aggr_05_95_prom7` 卫星三段式 clear-improvement 邻域，注册并确认风险阈值更低的再确认形态，例如 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk30_reconfirm`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-29 22:21 CST）

- 开局 guard 为 `pass`；上一轮 `share_08_92_hold_2_8_ramp75_cost_guard` 只改善防守形态，未替换 Path 1 robust。本轮按 rotation 的 `core_multifactor_coverage` 回到代码实际 `core_multifactor` 池，新增质量+估值+趋势+成本守门再确认组合，仍只用五窗口 `--only-base-ids` 增量确认。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm`。
- `quality_value_trend_cost_guard_reconfirm` 五窗口 CAGR 为 `14.51% / 14.85% / 29.32% / 66.56% / 100.39%`，最大回撤为 `-32.68% / -32.21% / -21.67% / -13.89% / -4.62%`，换手为 `2.84x / 3.17x / 3.52x / 5.21x / 5.93x`。该组合修复了 2026 弹性，但 2017/2020 明显弱于现有 Path 1 robust，不晋级。
- core_multifactor 子段按代码实际池提升为 `32/32 complete`，fast family 为 `79/79 complete`；`scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement。`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，下一轮 focus 继续 `core_multifactor_coverage`。第一条命令建议不要继续叠 cost_guard，改测质量+低波+估值或盈利低相关组合，例如注册并五窗口确认 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_value_reconfirm`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-29 16:33 CST）

- 开局 guard 先给出 Path 4 blocking 和 Path 1 fast-family warning；Path 4 按 blocking scope 补齐后，Path 1 只用 `--only-base-ids` 增量确认本轮候选。上一轮 `sat_three_stage_buffered_cost_guard_cashguard_light` 只改善防守形态，未替换 Path 1 robust；本轮按上一轮 focus 回到 `holding_shape`，测试更低 ramp 的 `2+8` 持仓形态。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp75_cost_guard`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp75_cost_guard`。
- `share_08_92_hold_2_8_ramp75_cost_guard` 五窗口 CAGR 为 `21.28% / 22.51% / 33.28% / 100.33% / 106.96%`，最大回撤为 `-18.81% / -18.28% / -23.44% / -11.31% / -11.71%`，换手为 `2.70x / 2.98x / 3.03x / 4.52x / 6.13x`。它继续证明低 ramp 持仓形态能改善短窗弹性和回撤，但长窗和 2023 不及现有 Path 1 robust。
- core_multifactor 子段本轮巡检代码实际池为 `31/31 complete`，未新增多因子 base id；`scripts/winner_only_pass.py` 仍只提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement。`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_fast_family 78/78 complete`、`ashare_path1_core_multifactor 31/31 complete`，下一轮 focus 轮换为 `signal_quality`。第一条命令建议回到代码实际 `core_multifactor` 池，补一个区别于近期现金防守失败组的质量+估值/趋势低相关组合，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_signal_quality_id>`。

## 本轮执行计划（2026-05-29 10:22 CST）

- 开局 guard 为 `pass`；上一轮 `quality_profitability_cashguard_reconfirm` 继续只改善防守形态、不改善 Path 1 robust。本轮按 rotation 的 `satellite_risk_cost` 新增 `aggr_05_95_prom7` 卫星三档轻现金成本防守，对照旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` clear improvement 是否能以浅现金版保留收益。
- 本轮新增并五窗口确认 1 个 Path 1 fast-family base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_cashguard_light`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_cashguard_light`。
- 该候选五窗口 CAGR 为 `22.98% / 29.30% / 32.13% / 103.21% / 129.13%`，最大回撤为 `-16.13% / -17.44% / -19.03% / -11.66% / -6.83%`，换手为 `3.04x / 3.31x / 3.57x / 4.88x / 8.43x`。它显著优于近期多因子防守组，但仍低于旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 2020 clear improvement；不替换 Path 1 window winner 或 robust。
- core_multifactor 子段本轮完成巡检，代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 仍为 `31/31 complete`，未新增 Path 1 core_multifactor；`quality_defense_cashguard_reconfirm` 只作为 Path 2 低相关候选进入 `PATH2_SCAN_VARIANT_IDS`。`scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 tracked/robust 未改，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_fast_family 77/77 complete`、`ashare_path1_core_multifactor 31/31 complete`，下一轮 focus 轮换为 `holding_shape`。第一条命令建议回到持仓形态线，不继续叠卫星现金守门，例如注册并五窗口确认 `core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp75_cost_guard` 或同等更低 ramp 的 2+8/3+7 形态：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-29 04:17 CST）

- 开局 guard 为 `pass`；上一轮 `quality_industry_cashguard_reconfirm` 只改善回撤与 2026 弹性，未改善 Path 1 robust。本轮按 rotation 的 `signal_quality` 继续补代码实际 `core_multifactor` 池，新增 `quality_profitability_cashguard_reconfirm`，用质量+盈利+现金防守测试是否比行业强度更稳。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_cashguard_reconfirm`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_cashguard_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold9_turn03_exit94_weekly,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76,core_explore_90_10_equal_weight_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76,core_explore_90_10_total_mv_winner_core__aggr_10_90_prom9_emergent_theme_quality_gate_risk35_cap30_exit76`。
- `quality_profitability_cashguard_reconfirm` 五窗口 CAGR 为 `16.48% / 11.97% / 13.92% / 61.21% / 76.13%`，最大回撤为 `-25.94% / -28.92% / -15.57% / -15.36% / -4.63%`，换手为 `2.83x / 3.38x / 3.68x / 5.14x / 5.94x`。它延续现金防守的浅回撤与 2026 弹性，但 2020/2023 收益低于现有 Path 1 robust，不替换 window winner 或 robust candidate。
- core_multifactor 子段按代码实际池提升为 `31/31 complete`，fast family 为 `76/76 complete`；`scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement。`scripts/update_weighted_winners.py` 后 Path 1 tracked/robust 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `satellite_risk_cost`。第一条命令建议暂停继续叠多因子，回到旧 `sat_three_stage_buffered_cost_guard` clear improvement 的低风险确认线，例如 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard_cashguard_light`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-28 22:19 CST）

- 开局 guard 为 `pass`；上一轮 `quality_industry_reconfirm` 没有改善 robust，本轮按最终 rotation 的 `core_multifactor_coverage` 继续补代码实际 `core_multifactor` 池，新增 `quality_industry_cashguard_reconfirm`，用现金防守约束测试质量+行业强度再确认是否能修复长窗回撤。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_industry_cashguard_reconfirm`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_industry_cashguard_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold8_turn04_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76,core_explore_90_10_equal_weight_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76,core_explore_90_10_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap30_exit76`。
- `quality_industry_cashguard_reconfirm` 五窗口 CAGR 为 `16.83% / 11.81% / 17.77% / 56.29% / 77.83%`，最大回撤为 `-25.90% / -28.93% / -11.62% / -13.08% / -4.63%`，换手为 `2.88x / 3.36x / 3.59x / 5.41x / 5.93x`。现金防守改善回撤形态和 2026 弹性，但 2020/2023 收益明显弱于现有 Path 1 robust，不替换 window winner 或 robust candidate。
- core_multifactor 子段按代码实际池提升为 `30/30 complete`，fast family 为 `75/75 complete`；`scripts/winner_only_pass.py` 仍只提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement。`scripts/update_weighted_winners.py` 后 Path 1 tracked/robust 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，下一轮 focus 继续为 `core_multifactor_coverage`。第一条命令建议不要继续只叠行业强度，改测质量+估值/盈利现金守门的低相关组合，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_cashguard_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-28 16:18 CST）

- 开局 guard 为 `pass`；上一轮 `share_10_90_hold_3_7_ramp80_cost_guard` 继续证明持仓形态能压回撤但不改善 Path 1 robust。本轮 rotation 回到 `signal_quality/core_multifactor`，按代码实际 `core_multifactor` 池新增 `quality_industry_reconfirm`，把质量和行业强度再确认作为低相关信号测试。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_industry_reconfirm`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_industry_reconfirm,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn04_exit92_weekly,core_explore_80_20_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76,core_explore_90_10_equal_weight_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76,core_explore_90_10_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk35_cap35_exit76`。
- `quality_industry_reconfirm` 五窗口 CAGR 为 `11.99% / 13.75% / 27.16% / 56.41% / 59.87%`，最大回撤为 `-44.87% / -31.73% / -28.70% / -12.78% / -5.49%`，换手为 `3.09x / 3.35x / 3.79x / 5.58x / 6.39x`。它保留 2025/2026 弹性，但 2017/2020 长窗收益和回撤明显弱于当前 Path 1 robust，不替换 window winner 或 robust candidate。
- core_multifactor 子段按代码实际池提升为 `29/29 complete`；`scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement，但 `scripts/update_weighted_winners.py` 后 Path 1 official/tracked/robust 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 29/29 complete`、`ashare_path1_fast_family 74/74 complete`，下一轮 focus 为 `satellite_risk_cost`。第一条命令建议不要继续加重行业暴露，回到旧 `sat_three_stage_buffered_cost_guard` clear improvement 的低风险确认线，例如 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard_cashguard_light`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `sat_three_stage_buffered_cost_guard_cashguard` 继续只压回撤、不改善 Path 1 robust，本轮按 `holding_shape` 补一个 `10/90 + 3+7 + ramp80` 成本防守持仓形态，对照近期 `2+8` 与 `12/88` 稳仓线。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__share_10_90_hold_3_7_ramp80_cost_guard`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_10_90_hold_3_7_ramp80_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn04_exit94_weekly,core_explore_80_20_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78,core_explore_90_10_equal_weight_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78,core_explore_90_10_total_mv_winner_core__aggr_09_91_prom8_emergent_theme_quality_gate_risk40_cap35_exit78`。
- `share_10_90_hold_3_7_ramp80_cost_guard` 五窗口 CAGR 为 `19.64% / 23.95% / 25.74% / 75.55% / 57.65%`，最大回撤为 `-23.09% / -23.76% / -25.55% / -11.13% / -7.91%`，换手为 `2.74x / 3.01x / 3.08x / 4.52x / 5.31x`。它继续说明 3+7 稳仓能压短窗回撤，但 2017/2020/2023 CAGR 低于当前 Path 1 robust，不替换 window winner 或 robust candidate。
- core_multifactor 子段本轮只巡检，代码实际池仍为 `28/28 complete`，未新增 overlay；`scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement。`scripts/update_weighted_winners.py` 后 Path 1 tracked/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 28/28 complete`、`ashare_path1_fast_family 73/73 complete`，下一轮 focus 转为 `core_multifactor_coverage`。第一条命令建议回到代码实际多因子池，新增区别于近期 quality/lowvol/trend 失败组的质量+估值/盈利再确认候选，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_lowvol_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；上一轮 `quality_lowvol_trend_reconfirm` 没有改善 Path 1 robust，本轮按 `satellite_risk_cost` 回到卫星三段式成本线，补齐尚未确认的 `aggr_08_92_prom6` 现金成本防守 overlay。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__sat_three_stage_buffered_cost_guard_cashguard`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__sat_three_stage_buffered_cost_guard_cashguard,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn04_exit94_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk40_cap35_exit78`。
- `aggr_08_92_prom6__sat_three_stage_buffered_cost_guard_cashguard` 五窗口 CAGR 为 `21.77% / 28.25% / 25.04% / 96.13% / 73.29%`，最大回撤为 `-13.71% / -13.56% / -18.52% / -10.23% / -10.31%`，换手为 `3.08x / 3.32x / 3.53x / 4.52x / 7.36x`。它显著压低 2017/2020 回撤，但 2017/2023 CAGR 仍低于当前 Path 1 robust，不替换 window winner 或 robust。
- core_multifactor 子段本轮只巡检，代码实际池仍为 `28/28 complete`，未新增多因子变体；`scripts/winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement，`scripts/update_weighted_winners.py` 后 Path 1 tracked/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 28/28 complete`、`ashare_path1_fast_family 72/72 complete`，下一轮 focus 转为 `holding_shape`。第一条命令建议回到 3+7/2+8 持仓形态线，测试更低 ramp 的成本防守版本，例如 `core_explore_80_20_total_mv_winner_core__share_10_90_hold_3_7_ramp80_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`，后续注册新多因子后按 guard 原始 blocking scope 补齐 `ashare_path1_core_multifactor 1/28 missing`；上一轮 `share_12_88_hold_3_7_ramp85_cost_guard` 继续证明持仓形态能压短窗回撤但不能改善 robust，本轮转回 `signal_quality/core_multifactor`。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn04_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom7_emergent_theme_quality_gate_risk45_cap35_exit80`。
- `quality_lowvol_trend_reconfirm` 五窗口 CAGR 为 `12.16% / 10.93% / 26.07% / 68.43% / 60.31%`，最大回撤为 `-46.55% / -35.56% / -28.22% / -13.63% / -5.49%`，换手为 `3.09x / 3.46x / 3.79x / 5.36x / 6.39x`。它没有修复 2017/2020 长窗弱势，不能替换 Path 1 window winner 或 robust candidate。
- core_multifactor 子段本轮按代码实际池提升为 `28/28 complete`；`scripts/winner_only_pass.py` 仍只报告旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement，`scripts/update_weighted_winners.py` 后 Path 1 tracked/robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，下一轮 focus 已轮换为 `satellite_risk_cost`。第一条命令建议回到卫星三段式成本线，比较旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 raw improvement 与浅现金/低风险版本，例如 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard_cashguard_light`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮 focus 指向 `holding_shape`，本轮按计划注册并确认 `core_explore_80_20_total_mv_winner_core__share_12_88_hold_3_7_ramp85_cost_guard`。注册后 guard 只对该 fast-family 候选给出 warning，另有 Path 4 新变体 blocking，均已用 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮 Path 1 新增并五窗口确认 1 个 base id：`core_explore_80_20_total_mv_winner_core__share_12_88_hold_3_7_ramp85_cost_guard`。实际 A股非阻塞合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_12_88_hold_3_7_ramp85_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly`。
- `share_12_88_hold_3_7_ramp85_cost_guard` 五窗口 CAGR 为 `19.53% / 23.61% / 25.38% / 73.22% / 57.06%`，最大回撤为 `-23.46% / -23.66% / -26.17% / -10.94% / -7.82%`，换手为 `2.74x / 3.00x / 3.04x / 4.49x / 5.08x`。它继续验证 3+7 稳仓形态能压短窗回撤，但 2017/2020/2023 收益仍低于当前 Path 1 robust，不能替换 window winner 或 robust candidate。
- core_multifactor 子段本轮只巡检，代码实际池仍为 `27/27 complete`，未新增多因子变体；`scripts/winner_only_pass.py` 仍以退出码 `2` 报告旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement，但 `scripts/update_weighted_winners.py` 后 Path 1 tracked/robust 未改，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 27/27 complete`、`ashare_path1_fast_family 70/70 complete`，下一轮 focus 转为 `core_multifactor_coverage`。第一条命令建议回到代码实际多因子池，注册区别于近期 quality/trend cashguard 的低回撤确认组合，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮 `profitability_industry_reconfirm` 仍无法修复长窗回撤，本轮按 `signal_quality` 注册并优先补齐代码实际 `core_multifactor` 新变体 `aggr_08_92_prom6_core_multifactor_quality_trend_cashguard_reconfirm`。注册后 guard 如预期给出 Path 1 core_multifactor 与 Path 4 新变体缺口，已用五窗口 `--only-base-ids` 增量补齐，没有跑全量。blocking 命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_trend_cashguard_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80,core_explore_90_10_equal_weight_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80,core_explore_90_10_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk45_cap40_exit80`。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_trend_cashguard_reconfirm`。五窗口 CAGR 为 `17.22% / 13.49% / 19.22% / 72.87% / 66.29%`，最大回撤为 `-25.91% / -24.30% / -11.95% / -13.78% / -5.49%`，换手为 `2.85x / 3.40x / 3.67x / 5.41x / 6.50x`。趋势质量现金守门改善回撤形态，但 2020/2023 收益仍低于当前 Path 1 robust，不能替换 window winner 或 robust candidate。
- core_multifactor 子段按代码实际池完成 `27/27` 覆盖；`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`，四窗口 meanCAGR `50.20%`、minCAGR `28.01%`、worstMaxDD `-29.18%`、meanTurn `4.08x`。候选池未触发 Path 1 evict。
- 最终 guard 为 `pass`，`ashare_path1_core_multifactor 27/27 complete`、`ashare_path1_fast_family 69/69 complete`，下一轮 focus 转为 `holding_shape`。第一条命令建议回到持仓形态线，补一个区别于近期 2+8/ramp80 的 3+7 成本防守形态，例如 `core_explore_80_20_total_mv_winner_core__share_12_88_hold_3_7_ramp85_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；按上一轮 `core_multifactor_coverage` 注册 `profitability_industry_reconfirm`，注册后 guard 如预期给出 `ashare_path1_core_multifactor` 与 Path 4 新变体缺口，已用 `--only-base-ids` 增量补齐，没有跑全量。blocking 覆盖命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82,core_explore_90_10_equal_weight_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82,core_explore_90_10_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk40_cap45_exit82`。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor 代码口径 base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm`。五窗口 CAGR 为 `12.26% / 13.44% / 27.77% / 55.65% / 43.79%`，最大回撤为 `-43.78% / -31.12% / -28.70% / -12.87% / -10.35%`，换手为 `3.05x / 3.37x / 3.78x / 5.59x / 6.89x`。盈利/行业再确认没有修复 2017/2020 长窗回撤，不能替换 Path 1 robust。
- 非阻塞确认中另跑等权 companion `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm`，作为 Path 2 underrepresented family 对照；五窗口 CAGR 为 `12.76% / 15.65% / 30.93% / 55.06% / 69.85%`，但回撤 `-45.11% / -37.22% / -31.55% / -15.15% / -13.55%` 仍过深。本轮 `scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 未变化。
- 候选池未触发 Path 1 evict。最终 guard 为 `pass`，`ashare_path1_core_multifactor 26/26 complete`、`ashare_path1_fast_family 68/68 complete`，下一轮 focus 转为 `signal_quality`；第一条命令建议注册区别于本轮盈利/行业失败组的趋势质量现金守门组合，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_trend_cashguard_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_signal_quality_id>`。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮 `quality_lowvol_cashguard_reconfirm` 没有改善 Path 1 robust，本轮按 rotation 的 `holding_shape` 增量确认一个更高稳定仓比例的 12/88 持仓形态成本防守对照。A股合并回测命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_12_88_hold_2_8_ramp80_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold7_turn05_exit92_weekly,core_explore_80_20_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk35_cap45_exit82,core_explore_90_10_equal_weight_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk35_cap45_exit82,core_explore_90_10_total_mv_winner_core__aggr_07_93_prom6_emergent_theme_quality_gate_risk35_cap45_exit82`。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__share_12_88_hold_2_8_ramp80_cost_guard`。五窗口 CAGR 为 `20.06% / 22.04% / 26.71% / 80.91% / 61.58%`，最大回撤为 `-17.70% / -16.59% / -23.86% / -11.97% / -12.18%`，换手为 `2.72x / 2.95x / 3.05x / 4.61x / 5.84x`。该组继续证明 2+8 稳仓形态能压回撤，但 2017/2020/2023 收益不足，不能替换 Path 1 robust。
- core_multifactor 子段本轮只巡检，代码实际 `core_multifactor` 为 `25/25 complete`，没有新增多因子变体。`scripts/winner_only_pass.py` 仍以退出码 `2` 只报告旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 official winner、robust candidate 与 tracked payload 未被本轮候选替换。
- 候选池未触发 Path 1 evict。最终 guard 为 `pass`，`ashare_path1_fast_family 67/67 complete`，下一轮 focus 转为 `core_multifactor_coverage`；第一条命令建议回到代码实际多因子池，注册区别于近期低波质量失败组的盈利/行业动量再确认形态，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮 `share_08_92_hold_2_8_ramp80_cost_guard` 继续证明 holding_shape 可压回撤但不改善 robust，本轮按 `signal_quality` 回到代码实际 `core_multifactor` 池，注册 `quality_lowvol_cashguard_reconfirm`。注册后 guard 如预期出现 `ashare_path1_core_multifactor 1/25 missing` 与 Path 4 三底座缺口，已按原始 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm`。
- `quality_lowvol_cashguard_reconfirm` 五窗口 CAGR 为 `15.86% / 11.71% / 15.36% / 58.06% / 76.40%`，最大回撤 `-23.90% / -27.84% / -12.32% / -14.24% / -4.63%`，换手 `2.86x / 3.41x / 3.62x / 5.15x / 5.93x`。现金防守改善 2026 回撤，但 2017/2020/2023 收益不足，不能替换 Path 1 robust。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 只报告旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 official winner、robust candidate 与 tracked payload 未被本轮候选替换。最终 guard 为 `ashare_path1_core_multifactor 25/25 complete`、`ashare_path1_fast_family 66/66 complete`。
- 候选池未触发 Path 1 evict。最终 focus 转为 `satellite_risk_cost`；下一轮第一条命令建议回到卫星三段式成本线，补一个尚未确认的现金成本对照，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__sat_three_stage_buffered_cost_guard_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮 `quality_trend_reconfirm` 仍只保留 2025/2026 弹性、长窗回撤弱，本轮按上一轮 focus `holding_shape` 注册 `share_08_92_hold_2_8_ramp80_cost_guard`。注册后 guard 出现预期 `ashare_path1_fast_family 1/65 missing` warning；先补 Path 4 blocking，再用五窗口 `--only-base-ids` 增量补齐本候选。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp80_cost_guard`。实际 A股非阻塞合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp80_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold7_turn06_exit90_weekly`。
- `share_08_92_hold_2_8_ramp80_cost_guard` 五窗口 CAGR 为 `19.86% / 22.20% / 27.23% / 82.30% / 61.86%`，最大回撤 `-18.32% / -17.01% / -23.23% / -12.30% / -11.72%`，换手 `2.72x / 2.95x / 3.09x / 4.63x / 6.13x`。它和上一轮 `10/90 ramp80` 同形，继续证明降 ramp 能压回撤但不能改善 Path 1 robust。
- core_multifactor 子段本轮只做巡检，代码实际 `core_multifactor` 仍为 `24/24 complete`，未新增多因子变体。`scripts/winner_only_pass.py` 仍以退出码 `2` 报告旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 official winner、robust candidate 与 tracked payload 未被本轮候选替换。
- 候选池未触发 Path 1 evict。最终 guard 为 `pass`，`ashare_path1_fast_family 65/65 complete`，下一轮 focus 转为 `signal_quality`；第一条命令建议注册一个区别于近期 quality/trend 失败组的防守信号质量组合，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_cashguard_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_signal_quality_id>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`；上一轮 `quality_lowvol_reconfirm` 只保留短窗弹性、长窗回撤弱，本轮按 `signal_quality` 在代码实际 `core_multifactor` 池新增 `quality_trend_reconfirm`。注册后 guard 如预期出现 `ashare_path1_core_multifactor 1/24 missing` 与 Path 4 三底座缺口，已按原始 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_trend_reconfirm`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_trend_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom4_emergent_theme_quality_gate_risk35_cap45_exit82`。
- `quality_trend_reconfirm` 五窗口 CAGR 为 `12.25% / 13.65% / 29.37% / 72.66% / 60.29%`，最大回撤 `-46.98% / -33.98% / -28.70% / -12.91% / -5.49%`，换手 `3.05x / 3.41x / 3.74x / 5.54x / 6.39x`。它保留 2025/2026 弹性，但 2017/2020 收益和长窗回撤仍弱于当前 Path 1 robust。
- `scripts/winner_only_pass.py` 以退出码 `2` 继续只报告旧 `sat_three_stage_buffered_cost_guard` 的 `since_2020_only` clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 official winner、robust candidate 与 tracked payload 未被本轮候选替换。最终 guard 为 `ashare_path1_core_multifactor 24/24 complete`、`ashare_path1_fast_family 64/64 complete`。
- 候选池未触发 Path 1 evict。最终 focus 转为 `holding_shape`；下一轮第一条命令建议从持仓形态而非继续堆多因子开始，例如注册 `core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp80_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`；上一轮要求优先补 `core_multifactor_quality_lowvol_reconfirm`。注册后 guard 如预期出现 `ashare_path1_core_multifactor 1/23 missing` 与 Path 4 三底座缺口；首次未加 `--end-date` 的补缺口尝试失败在 `2026-05-25` stale cache 校验，没有写入策略结果，随后用固定 `--end-date 2026-05-19` 增量补齐。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_reconfirm`。覆盖命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_reconfirm`。
- `quality_lowvol_reconfirm` 五窗口 CAGR 为 `10.16% / 10.83% / 24.23% / 59.70% / 60.18%`，最大回撤 `-49.37% / -38.03% / -28.21% / -13.77% / -5.49%`，换手 `3.08x / 3.38x / 3.83x / 5.22x / 6.40x`。它改善不了 2017/2020 长窗，也弱于当前 Path 1 robust；只提供质量低波再确认的负面对照。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 只提示旧 `sat_three_stage_buffered_cost_guard` 的 `since_2020_only` raw clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 official winners 与 robust 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`。最终 guard 为 `ashare_path1_core_multifactor 23/23 complete`、`ashare_path1_fast_family 63/63 complete`。
- 候选池未触发 Path 1 evict。最终 focus 转为 `signal_quality`；下一轮第一条命令建议不要继续只堆低波质量，改注册一个信号质量/趋势确认组合，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_trend_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_signal_quality_id>`。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，上一轮 `sat_three_stage_buffered_cost_guard_cashguard` 只形成 `since_2020_only` clear improvement，未改 official winner/robust；本轮按最终 focus `holding_shape` 注册并确认更低首段 ramp 的持仓形态对照。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__share_10_90_hold_2_8_ramp80_cost_guard`。A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_10_90_hold_2_8_ramp80_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap65_hold6_turn08_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap40`。
- `share_10_90_hold_2_8_ramp80_cost_guard` 五窗口 CAGR 为 `19.97% / 22.14% / 27.06% / 81.55% / 62.88%`，最大回撤 `-17.78% / -16.87% / -23.52% / -12.14% / -11.95%`，换手 `2.72x / 2.95x / 3.07x / 4.62x / 5.98x`。结果与上一条 `ramp85` 近似同形，说明继续压首段 ramp 没有新增收益信息；`winner_only_pass.py` 仍只在旧 `sat_three_stage_buffered_cost_guard` 上报 `since_2020_only` clear improvement。
- core_multifactor 子段本轮没有新增代码口径候选，最终 guard 为 `ashare_path1_core_multifactor 22/22 complete`、`ashare_path1_fast_family 62/62 complete`。`scripts/update_weighted_winners.py` 后 Path 1 official winner 与 robust 仍为旧组合，未触发 tracked payload 替换。
- 最终 focus 转为 `core_multifactor_coverage`。下一轮第一条命令建议回到代码实际 `core_multifactor` 池，注册一个区别于 `profitability_lowvol_rebalance` 的低回撤再平衡组合，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，上一轮要求优先确认 `satellite_risk_cost` 的 `sat_three_stage_buffered_cost_guard_cashguard`；本轮按增量范围执行，未跑 `research_active/all`。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard_cashguard`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap65_hold6_turn08_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk35_cap45`。
- `sat_three_stage_buffered_cost_guard_cashguard` 五窗口 CAGR 为 `21.34% / 29.32% / 26.37% / 88.74% / 73.97%`，最大回撤 `-13.63% / -14.21% / -20.85% / -11.76% / -6.83%`，换手 `3.00x / 3.39x / 3.53x / 4.75x / 8.43x`。它继续证明三段式卫星防守能显著压 2020 回撤，`winner_only_pass.py` 以退出码 `2` 记录 `since_2020_only` clear improvement，但 `update_weighted_winners.py` 后 official window winner 与 robust candidate 未替换。
- core_multifactor 子段本轮没有新增 Path 1 代码口径候选；上一轮 `profitability_lowvol_rebalance` 已补齐后，最终 guard 仍为 `ashare_path1_core_multifactor 22/22 complete`、`ashare_path1_fast_family 61/61 complete`。本轮另有等权 `profitability_lowvol_rebalance` 作为 Path 2 underrepresented family 压力测试，不计入 Path 1 core_multifactor 新增。
- 候选池未触发 Path 1 evict。最终 guard 下一轮 focus 转为 `holding_shape`；第一条命令建议注册一个低 ramp/更稳仓位的持仓形态对照，例如 `core_explore_80_20_total_mv_winner_core__share_10_90_hold_2_8_ramp80_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，上一轮要求优先补 `profitability_lowvol_rebalance` 多因子；本轮注册后 guard 如预期变成 `ashare_path1_core_multifactor 1/22 missing` 与 Path 4 三底座缺口，已按原始 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance`。覆盖命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance,core_explore_80_20_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50`。
- `profitability_lowvol_rebalance` 五窗口 CAGR 为 `11.79% / 13.06% / 30.86% / 68.36% / 71.72%`，最大回撤 `-47.79% / -32.46% / -28.70% / -12.94% / -4.63%`，换手 `3.05x / 3.42x / 3.71x / 5.69x / 5.81x`。它只保留 2023+ 弹性，2017/2020 收益和长窗回撤明显弱于当前 Path 1 robust，未改变 official window winner、robust candidate 或 tracked payload。
- `scripts/update_weighted_winners.py` 后 Path 1 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，core_multifactor 覆盖提升为 `22/22 complete`，fast-family 为 `61/61 complete`；候选池未触发 evict。
- 最终 guard 下一轮 focus 转为 `satellite_risk_cost`。下一轮第一条命令建议从旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 raw improvement 出发，注册并确认一个浅现金/低风险的卫星成本候选，例如 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，上一轮 `trend_quality_rebalance` 多因子保留短窗弹性但未改善 Path 1 robust；本轮按上一轮 `holding_shape` 提示新增更高稳定仓比例 `share_10_90_hold_2_8_ramp85_cost_guard`。注册后 guard 如预期报 Path 1 fast-family 1 个缺口与 Path 4 三底座缺口，已按原始 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__share_10_90_hold_2_8_ramp85_cost_guard`。覆盖命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_10_90_hold_2_8_ramp85_cost_guard,core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap40`。
- `share_10_90_hold_2_8_ramp85_cost_guard` 五窗口 CAGR 为 `19.97% / 22.14% / 27.06% / 81.55% / 62.88%`，最大回撤 `-17.78% / -16.87% / -23.52% / -12.14% / -11.95%`，换手 `2.72x / 2.95x / 3.07x / 4.62x / 5.98x`。它继续证明高稳定仓比例能压回撤，但 2017/2020 收益仍低于 `aggr_08_92_prom6__port_weekly_exposure_buffered` robust，未改变 official window winner、robust candidate 或 tracked payload。
- core_multifactor 按代码实际返回口径仍为 `21/21 complete`，fast-family 提升到 `60/60 complete`；本轮没有新增 core_multifactor 变体。`scripts/update_weighted_winners.py` 后 Path 1 official winners 与 robust 未变化，候选池未触发 evict。
- 最终 guard 下一轮 focus 转为 `core_multifactor_coverage`。下一轮第一条命令应先补一个代码实际注册的多因子组合，而不是继续 holding_shape；候选池建议 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance` 或同等 `profitability + lowvol + trend rebalance` 版本，注册后五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `industry_momentum_quality` 只保留 2023/2025 短窗弹性，未改 Path 1 winner。本轮按上一轮下一步新增 `trend_quality_rebalance` 多因子预设。注册后 guard 出现预期 coverage block：`ashare_path1_core_multifactor` 1 个缺口与 Path 4 三底座缺口，已按 guard 原始 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_quality_rebalance`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_quality_rebalance,core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45`。
- `trend_quality_rebalance` 五窗口 CAGR 为 `12.39% / 14.87% / 29.76% / 69.90% / 62.06%`，最大回撤 `-44.00% / -32.46% / -28.70% / -12.84% / -5.49%`，换手 `3.10x / 3.43x / 3.81x / 5.69x / 6.34x`。它保留 2025/2026 弹性，但 2017/2020 收益和 2017 回撤明显弱于当前 robust，未改变 official window winner、robust candidate 或 tracked payload。
- `scripts/winner_only_pass.py` 以退出码 `2` 报告旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` raw clear improvement；`scripts/update_weighted_winners.py` 后 Path 1 official winners 仍为 2017 `aggr_08_92_prom6__port_weekly_exposure_buffered`、2020/2023 `risk40_mom_exit60_reconfirm70_cap95_dd_guard50`、2025 `aggr_10_90_prom6__port_weekly_exposure_buffered`，robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`。
- core_multifactor 按代码实际口径提升到 `21/21 complete`，fast-family 为 `59/59 complete`，候选池未触发 Path 1 evict。最终 guard 下一轮 focus 轮到 `holding_shape`；下一轮第一条命令建议不要继续只加多因子，先实现并确认一个更高稳定仓比例的持仓形态对照，例如 `core_explore_80_20_total_mv_winner_core__share_10_90_hold_2_8_ramp85_cost_guard` 或同等 `holding_shape` 版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，上一轮 `sat_three_stage_buffered_cost_guard_cashguard` 只压回撤、未改 Path 1 winner；本轮按 guard rotation 的 `core_multifactor_coverage` 新增一个行业动量 + 质量的多因子预设。新增注册后出现预期 coverage block：`ashare_path1_core_multifactor 1/20 missing` 与 Path 4 三底座缺口，已按 guard 原始 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_quality`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_quality,core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk35_cap45`。
- `industry_momentum_quality` 五窗口 CAGR 为 `12.04% / 18.56% / 31.13% / 73.25% / 45.47%`，最大回撤 `-39.30% / -34.66% / -28.69% / -11.73% / -10.35%`，换手 `3.16x / 3.47x / 3.83x / 5.52x / 6.84x`。它只保留 2023/2025 短窗弹性，2017/2020 收益和回撤仍弱于 Path 1 robust，未改变 official window winner、robust candidate 或 tracked payload。
- `scripts/winner_only_pass.py` 仍以退出码 `2` 报告旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` raw improvement；`scripts/update_weighted_winners.py` 后 Path 1 official winners 仍为 2017 `aggr_08_92_prom6__port_weekly_exposure_buffered`、2020/2023 `risk40_mom_exit60_reconfirm70_cap95_dd_guard50`、2025 `aggr_10_90_prom6__port_weekly_exposure_buffered`，robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`。
- core_multifactor 按代码实际口径提升到 `20/20 complete`，fast-family 为 `58/58 complete`，候选池未触发 Path 1 evict。收尾 guard 下一轮 focus 为 `signal_quality`；下一轮第一条命令建议不要继续只堆行业动量，先实现一个质量/趋势再平衡的信号质量候选，例如 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_quality_rebalance` 或同等 `quality + trend + lower drawdown` 版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_signal_quality_id>`。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，Path 1 fast-family 与 core_multifactor 覆盖完整；上一轮建议的 `satellite_risk_cost` 已落实为三段式卫星风控的 cashguard 版本。代码口径 core_multifactor 仍为 `19/19 complete`，本轮没有新增 core_multifactor 候选，但同步修复了 `scripts/winner_only_pass.py` 与 `scripts/update_weighted_winners.py` 对三段式成本守门 suffix 的识别，避免 fast-pass 漏看旧/新卫星 overlay。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered_cost_guard_cashguard`。实际非阻塞 A股批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered_cost_guard_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk35_cap70_hold5_turn10_exit88_weekly`。
- 新 cashguard 五窗口 CAGR 为 `21.64% / 28.29% / 25.20% / 96.07% / 74.30%`，最大回撤 `-13.51% / -13.69% / -18.33% / -10.10% / -10.31%`，换手 `3.07x / 3.32x / 3.52x / 4.54x / 7.31x`。它进一步压低 2017/2020/2023 回撤，但 2017/2023/2025 收益仍低于当前 Path 1 robust/winners，未改变 official window winner、robust candidate 或 tracked payload。
- `scripts/winner_only_pass.py` 以退出码 `2` 报告 clear improvement，这是预期的“发现 raw improvement”状态而非执行失败；clear improvement 集中在旧 `aggr_05_95_prom7__sat_three_stage_buffered_cost_guard` 的 `since_2020_only` 对照，`scripts/update_weighted_winners.py` 后 Path 1 official winners 仍为 2017 `aggr_08_92_prom6__port_weekly_exposure_buffered`、2020/2023 `risk40_mom_exit60_reconfirm70_cap95_dd_guard50`、2025 `aggr_10_90_prom6__port_weekly_exposure_buffered`，robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`。
- 候选池未触发 Path 1 evict。收尾 focus 转向 `holding_shape`；下一轮第一条命令建议不要继续只加卫星防守，先实现并确认一个更高稳定仓比例的持仓形态对照，例如 `core_explore_80_20_total_mv_winner_core__share_10_90_hold_2_8_ramp85_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `share_08_92_hold_2_8_ramp85_cost_guard` 继续证明持仓形态能压回撤但不能补 2017/2020 收益。本轮按上一轮第一条命令和 Path 1/core_multifactor 覆盖要求，新增一个行业动量 + 低波过滤的多因子预设；注册后出现预期 coverage block：`ashare_path1_core_multifactor 1/19 missing` 与 Path 4 三底座缺口，已按 guard 原始 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol`。实际补缺口命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol,core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap60`。
- `industry_momentum_lowvol` 五窗口 CAGR 为 `14.29% / 19.40% / 29.60% / 76.25% / 60.36%`，最大回撤 `-36.71% / -32.86% / -28.88% / -11.84% / -7.63%`，换手 `3.19x / 3.61x / 3.95x / 5.47x / 6.59x`。它保留 2025/2026 短窗弹性，但 2017/2020 仍低于 Path 1 robust，且长窗回撤没有改善，未晋级。
- `scripts/winner_only_pass.py` 为 `base_candidates=57 / total_candidates=513 / evaluated=194`，core_multifactor 按代码实际口径为 `19` 个候选，fast-family 为 `57/57 complete`；clear improvement 仍只来自旧周度仓位 overlay 的 raw 对照，`scripts/update_weighted_winners.py` 后 Path 1 window winner 与 robust 未变化。
- 候选池未触发 Path 1 evict。收尾 guard 给出下一轮 focus `satellite_risk_cost`；下一轮第一条命令建议回到卫星周度风控成本线，先实现并确认一个只改风险/退出成本的 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered_cost_guard_cashguard` 或同等候选，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，上一轮 `aggr_10_90_prom6__sat_three_stage_buffered_cost_guard` 只压低回撤、未改变 robust；本轮按上一轮 focus `holding_shape` 实现并确认更高稳定仓比例的 `2+8` 持仓形态。注册后 Path 4 先触发 blocking 缺口，已优先按 guard 原始 `--only-base-ids` 补齐；Path 1 只留下 `ashare_path1_fast_family 1/56 missing` warning，随后用增量批次补齐，没有跑 `research_active/all`。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp85_cost_guard`。实际 A股非阻塞批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp85_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap45_hold5_turn12_exit90_weekly`。
- `share_08_92_hold_2_8_ramp85_cost_guard` 五窗口 CAGR 为 `19.86% / 22.20% / 27.23% / 82.30% / 61.86%`，最大回撤 `-18.32% / -17.01% / -23.23% / -12.30% / -11.72%`，换手 `2.72x / 2.95x / 3.09x / 4.63x / 6.13x`。它是低回撤持仓形态对照，robust4 为 `meanCAGR=37.90% / minCAGR=19.86% / worstMaxDD=-23.23% / meanTurn=3.35x`，但 2017/2020 收益仍低于现有 Path 1 robust。
- `scripts/winner_only_pass.py` 为 `base_candidates=56 / total_candidates=504 / evaluated=193`，clear improvement 仍集中在旧 `__port_weekly_exposure_buffered_asym13` 相关候选；`scripts/update_weighted_winners.py` 后 Path 1 window winner 与 robust 未变化。core_multifactor 按代码实际口径仍为 `18/18 complete`，fast-family 为 `56/56 complete`。
- 候选池未触发 Path 1 evict。收尾 guard 给出下一轮 focus `core_multifactor_coverage`，下一轮第一条命令建议实现并确认 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_momentum_lowvol`，用行业/放量动量加低波过滤检查能否改善 2017/2020，而不是继续只加 holding_shape；五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_core_multifactor_id>`。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `trend_industry_momentum` 多因子只保留短窗弹性，最终 focus 转到 `satellite_risk_cost`。本轮先按上一轮第一条命令补 `aggr_10_90_prom6__sat_three_stage_buffered_cost_guard`，同时巡检 core_multifactor：代码口径仍为 `18/18 complete`，本轮没有新增 Path 1 core_multifactor，另把等权 `trend_industry_momentum` 作为 Path 2 underrepresented family 压力测试。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered_cost_guard`。实际 A股新增批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_trend_industry_momentum,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap70_hold4_turn14_exit90_weekly`。
- `aggr_10_90_prom6__sat_three_stage_buffered_cost_guard` 五窗口 CAGR 为 `25.05% / 28.36% / 32.09% / 96.12% / 82.21%`，最大回撤 `-13.73% / -13.67% / -16.02% / -10.10% / -10.31%`，换手 `3.18x / 3.53x / 3.68x / 4.54x / 7.12x`。它比普通 `aggr_10_90_prom6` 显著压低 2017/2020/2023 回撤，但 `update_weighted_winners.py` 仍保留旧 Path 1 window winners 与 robust，原因是 robust 最小 CAGR 仍低于 `aggr_08_92_prom6__port_weekly_exposure_buffered`。
- `scripts/winner_only_pass.py` 为 `base_candidates=55 / total_candidates=495 / evaluated=192`，clear improvement 仍只来自旧 `__port_weekly_exposure_buffered_asym13` / `cash_off__port_weekly_exposure_buffered_asym13`，`update_weighted_winners.py` 继续用验证窗拦截。core_multifactor 子段继续按代码实际返回口径计数，不按文字扩成全 overlay 乘积。
- 候选池未触发 Path 1 evict。收尾 guard 的下一轮 focus 为 `holding_shape`，第一条命令建议从上一轮未跑的更高稳定仓比例形态开始：实现并确认 `core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp85_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_holding_shape_id>`。

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `trend_momentum_quality` 只改善 2023/2026 短窗，2017/2020 仍弱。本轮按 rotation 的 `signal_quality` 新增更偏行业动量/放量强度的 core_multifactor 预设，注册后触发预期 coverage block：`ashare_path1_core_multifactor 1/18 missing` 与 Path 4 三底座缺口，已按 guard 原始 `--only-base-ids` 增量补齐，没有跑全量。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_industry_momentum`。实际命令与 Path 2/3/4 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_industry_momentum,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold4_turn16_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk35_cap65`。
- `trend_industry_momentum` 五窗口 CAGR 为 `14.90% / 18.60% / 31.10% / 90.20% / 37.90%`，最大回撤 `-36.30% / -34.90% / -30.20% / -9.60% / -11.90%`，换手 `3.18x / 3.55x / 3.83x / 5.52x / 6.30x`；相对上一轮多因子增强了 2025 弹性，但 2017/2020 与 2026 不足，未改变 Path 1 window winner 或 robust。
- `scripts/winner_only_pass.py` 为 `base_candidates=55 / total_candidates=495 / evaluated=192`，clear improvement 仍只来自旧 `__port_weekly_exposure_buffered_asym13` / `cash_off__port_weekly_exposure_buffered_asym13`，`update_weighted_winners.py` 继续拒绝晋级。core_multifactor 按代码口径为 `18/18 complete`，fast-family 为 `55/55 complete`。
- 候选池未触发 Path 1 evict。收尾 guard 将下一轮 focus 转到 `satellite_risk_cost`，且 `winner_only_pass.py` 的 clear improvement 仍集中在旧周度仓位卫星 overlay；第一条命令建议只补一个 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered_cost_guard` 或同等高稳定仓比例的卫星成本守门候选，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path1_satellite_risk_cost_id>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass` 后，新增注册触发预期 block：`ashare_path1_core_multifactor 1/17 missing` 与 Path 4 三底座缺口；本轮按 guard 原始 `--only-base-ids` 增量补齐，没有替换成全量回测。上一轮 holding_shape 的 `share_06_94_hold_2_8_ramp85_cost_guard` 低回撤但 2020/2023 收益不足，本轮按 rotation 的 `core_multifactor_coverage` 新增一个更偏动量/行业强度的多因子预设。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_momentum_quality`。实际命令与 Path 2/3/4 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_momentum_quality,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_cost_guard_cap50_hold5_turn14_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap35`。
- `trend_momentum_quality` 五窗口 CAGR 为 `13.94% / 18.60% / 31.85% / 70.42% / 56.30%`，最大回撤 `-35.47% / -35.07% / -28.70% / -12.25% / -6.91%`，换手 `3.17x / 3.58x / 3.80x / 5.78x / 6.33x`；2023/2026 改善了近期弹性，但 2017/2020 仍明显弱于 Path 1 robust，未晋级。
- `scripts/winner_only_pass.py` 为 `base_candidates=54 / total_candidates=486 / evaluated=191`，仍只在旧 `__port_weekly_exposure_buffered_asym13` / `cash_off__port_weekly_exposure_buffered_asym13` 上发现 2017/2025 clear improvement；`update_weighted_winners.py` 因验证窗继续拒绝，Path 1 official winners 与 robust 未变。core_multifactor 按代码实际口径提升到 `17` 个候选。
- 候选池未触发 Path 1 evict。下一轮 focus -> candidates 池：如果 rotation 仍指向 `core_multifactor_coverage`，不要再单纯加质量防守，第一条命令建议测试 `aggr_08_92_prom6_core_multifactor_trend_industry_momentum`，提高 `industry_strength/liquidity_surge` 并降低质量权重；若 rotation 转回 holding_shape，再执行上一轮未跑的 `share_08_92_hold_2_8_ramp85_cost_guard` 五窗口确认。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 指向 `holding_shape`；上一轮三段式成本守门候选只压回撤、未改善 winner，本轮改测更分散的 `2+8` 持仓形态成本防守。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__share_06_94_hold_2_8_ramp85_cost_guard`。实际命令与 Path 2/3/4 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_06_94_hold_2_8_ramp85_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly,core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_weekly_alpha_pullback_risk40_cap50_hold4_turn18_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk35_cap40`。
- `share_06_94_hold_2_8_ramp85_cost_guard` 五窗口 CAGR 为 `19.57% / 22.34% / 27.26% / 82.94% / 63.30%`，最大回撤 `-19.21% / -17.57% / -23.06% / -12.48% / -11.67%`，换手 `2.73x / 2.95x / 3.13x / 4.63x / 6.29x`；回撤和换手可控，但 2020/2023 收益低于现有 Path 1 robust，未晋级。
- `scripts/winner_only_pass.py` 为 `base_candidates=53 / total_candidates=477 / evaluated=190`，clear improvement 仍只来自旧 `satellite_cost_guard` 的 2025 raw；`update_weighted_winners.py` 因 2023 验证不足继续拒绝。Path 1 official winners 与 robust 未变。
- core_multifactor 子段按代码口径仍为 `16/16 complete`；本轮没有新增多因子 overlay，只把 holding_shape 计数提升到 `12`，未触发 Path 1 evict。
- 下一轮 focus -> candidates 池：若 rotation 继续 `holding_shape`，不要继续只加防守，先实现 `core_explore_80_20_total_mv_winner_core__share_08_92_hold_2_8_ramp85_cost_guard`，用更高稳定仓比例检查能否保留本轮低回撤并补回 2020/2023 CAGR；仍用五窗口 `--only-base-ids <next_holding_shape_id>`。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `trend_lowvol_quality` 长窗弱，rotation 转到 `satellite_risk_cost`，因此本轮回到卫星周频风控成本，不再扩普通多因子。
- 本轮新增并五窗口确认 2 个 Path 1 base ids：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__sat_three_stage_buffered_cost_guard`、`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_sat_three_stage_buffered_cost_guard_ids>`。
- `aggr_08_92_prom6` 版本五窗口 CAGR 为 `25.27% / 28.28% / 32.08% / 96.17% / 78.40%`，最大回撤 `-14.18% / -13.53% / -16.25% / -10.23% / -10.31%`，换手 `3.21x / 3.53x / 3.70x / 4.52x / 7.17x`；`aggr_05_95_prom7` 版本为 `24.90% / 34.00% / 33.96% / 88.78% / 79.58%`，最大回撤 `-13.83% / -14.16% / -17.77% / -11.76% / -6.83%`，换手 `3.12x / 3.53x / 3.71x / 4.76x / 8.20x`。
- 两个成本守门版本均明显压低 2017/2020/2023 回撤，但 2025 弹性不如当前 winner；`winner_only_pass.py` 仍只把旧 `satellite_cost_guard` 标记为 2025 raw clear improvement，`update_weighted_winners.py` 因 2023 验证不足拒绝，Path 1 official winners 与 robust 未变。
- core_multifactor 子段按代码口径巡检为 `16/16 complete`；本轮只把 `__sat_three_stage_buffered_cost_guard` 作为 `aggr_08_92_prom6` 与 `aggr_05_95_prom7` 的定向 overlay，不扩成全量 overlay 乘积，未触发 Path 1 evict。
- 下一轮 focus -> candidates 池：若 rotation 仍指向 `satellite_risk_cost`，先比较 `__sat_three_stage_buffered_cost_guard` 与旧 `satellite_cost_guard` 的验证窗差异；第一条命令建议只补一个更低 2025 损失的 `aggr_10_90_prom6__sat_three_stage_buffered_cost_guard`，仍用五窗口 `--only-base-ids <next_satellite_risk_cost_id>` 增量确认。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `trend_quality_defense` 2025/2026 尚可但长窗弱，本轮按 rotation 的 `signal_quality` 只补 1 个多因子信号质量候选，继续按代码实际 `core_multifactor` 返回口径计数。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_lowvol_quality`。实际命令与 Path 2/3/4 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_lowvol_quality,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn08_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap45`。
- `trend_lowvol_quality` 五窗口 CAGR 为 `12.40% / 12.08% / 29.68% / 62.49% / 60.29%`，最大回撤 `-47.13% / -34.13% / -28.70% / -13.08% / -5.49%`，换手 `3.08x / 3.43x / 3.74x / 5.55x / 6.39x`；短窗防守好但 2017/2020 收益与 2017 回撤明显弱，不替换 Path 1 winner 或 robust。
- `winner_only_pass.py` 为 `base_candidates=52 / total_candidates=468 / evaluated=189`，clear improvement 仍只来自旧 `satellite_cost_guard` 的 2025 fast-pass；`update_weighted_winners.py` 因 2023 验证不足继续拒绝。Path 1 robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`core_multifactor=16/16 complete`、fast-family `52/52 complete`，未触发 Path 1 evict。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，rotation 为 `stagnation_runs=18 / satellite_risk_cost / rotate`。下一轮 focus -> candidates 池回到卫星周频风控成本，第一条命令建议先实现 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__sat_three_stage_buffered_cost_guard` 与 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard`，五窗口 `--only-base-ids <next_satellite_risk_cost_ids>` 增量确认。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，上一轮持仓形态候选 `share_08_92_hold_3_7_ramp90_cost_guard` 未晋级；本轮按当时 rotation 的 `core_multifactor_coverage` 补一个 `trend_quality_defense` 多因子预设，继续按代码实际 core_multifactor 返回口径计数。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_quality_defense`。实际命令与 Path 2/3/4 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_quality_defense,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold5_turn10_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_quality_gate_risk30_cap50`。
- `trend_quality_defense` 五窗口 CAGR 为 `14.40% / 13.00% / 26.95% / 61.43% / 45.74%`，最大回撤 `-36.22% / -35.76% / -28.21% / -13.32% / -10.35%`，换手 `3.13x / 3.52x / 3.74x / 5.32x / 6.84x`；2025/2026 尚可，但 2017/2020 长窗弱，未替换现有 Path 1 winner 或 robust。
- `winner_only_pass.py` 为 `base_candidates=51 / total_candidates=459 / evaluated=188`，clear improvement 仍只在旧 `satellite_cost_guard` 的 2025 raw；`update_weighted_winners.py` 后 Path 1 official winner 未变，四窗口 robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=47.30% / minCAGR=26.98% / worstMaxDD=-29.57% / meanTurn=4.08`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，`core_multifactor=15/15 complete`、Path 1 fast-family `51/51 complete`；本轮未触发 Path 1 evict。最终 rotation 为 `stagnation_runs=15 / signal_quality / rotate`。下一轮 focus -> candidates 池切到信号质量而不是继续加普通多因子，第一条命令建议先实现 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_trend_lowvol_quality` 并五窗口 `--only-base-ids <next_signal_quality_id>` 增量确认。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `satellite_cost_guard` 只形成 2025 near-miss，最终 focus 转到 `holding_shape`。本轮按提示先补 1 个持仓形态成本守门候选，暂未扩大普通多因子。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__share_08_92_hold_3_7_ramp90_cost_guard`。实际命令与 Path 2/3/4 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_08_92_hold_3_7_ramp90_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap60_hold6_turn12_exit85_weekly,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk30_cap50`。
- `share_08_92_hold_3_7_ramp90_cost_guard` 五窗口 CAGR 为 `19.78% / 24.11% / 25.45% / 75.55% / 56.13%`，最大回撤 `-23.48% / -24.04% / -25.71% / -11.33% / -7.91%`，换手 `2.76x / 3.02x / 3.12x / 4.52x / 5.32x`；2025/2026 防守尚可，但 2017/2020/2023 不足以替换现有 Path 1 winner。
- `winner_only_pass.py` 本轮为 `base_candidates=50 / total_candidates=450 / evaluated=187`，clear improvement 仍只出现在旧 `satellite_cost_guard` 的 `since_2025_only`；`update_weighted_winners.py` 后 Path 1 official winners 与 robust 未变化，robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`。core_multifactor 按代码口径为 `14/14 complete`，fast-family 为 `50/50 complete`，未触发 evict。
- 最终 guard 后 rotation 为 `stagnation_runs=12 / core_multifactor_coverage / rotate`；下一轮 focus -> candidates 池切回代码实际 `core_multifactor` 覆盖口径，不按文字假定 9×overlay。第一条命令建议实现一个新多因子预设 `aggr_08_92_prom6_core_multifactor_trend_quality_defense`，权重在 `momentum_quality` 与 `quality_defense` 之间折中，并用五窗口 `--only-base-ids <next_core_multifactor_id>` 增量确认。

## 本轮执行计划（2026-05-20 13:58 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，Path 1 rotation 继续指向 `satellite_risk_cost`；上一轮 `quality_defense` 未晋级后，本轮不再扩大普通质量多因子，而是按卫星周频风控成本补一个低卖出阈值的三段式对照。
- 本轮新增并五窗口确认 1 个 Path 1 base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_satellite_cost_guard`。实际命令与 Path 2/3/4 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_satellite_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_risk30_cap60_hold8_turn10_exit90_weekly,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70`。
- `satellite_cost_guard` 五窗口 CAGR 为 `22.70% / 27.01% / 28.82% / 101.77% / 72.95%`，最大回撤 `-24.11% / -23.10% / -27.02% / -10.23% / -12.30%`，换手 `3.00x / 3.16x / 3.39x / 4.22x / 6.39x`；`winner_only_pass.py` 报告它在 `since_2025_only` 有 clear improvement，但 `update_weighted_winners.py` 因 2023 验证 CAGR `28.82% < 30.56%` 拦截，未替换 2025 official winner。
- core_multifactor 子段按代码实际返回的覆盖口径巡检为 `14/14 complete`；本轮另有等权弹性 `core_multifactor_quality_defense` 在 Path 2 候选池中确认，五窗口 `9.71% / 13.45% / 26.85% / 50.12% / 69.97%`，长窗收益与回撤不足，不作为 Path 1 多因子晋级线索。
- `update_weighted_winners.py` 后 Path 1 official winners 未变化：2017 `aggr_08_92_prom6__port_weekly_exposure_buffered`，2020/2023 `risk40_mom_exit60_reconfirm70_cap95_dd_guard50`，2025 `aggr_10_90_prom6__port_weekly_exposure_buffered`；四窗口 robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`。fast-family 为 `49/49 complete`，其中 `satellite_defense=6`、`core_multifactor=14`，未触发 evict。
- 最终 guard 后 rotation 为 `stagnation_runs=9 / holding_shape / rotate`；下一轮 focus -> candidates 池先回到持仓形态，同时保留本轮 `satellite_cost_guard` 的 2025 near-miss 观察。下一轮第一条命令建议先实现 `core_explore_80_20_total_mv_winner_core__share_08_92_hold_3_7_ramp90_cost_guard` 与 `core_explore_80_20_total_mv_winner_core__share_10_90_hold_2_8_ramp85_cost_guard`，再用五窗口 `--only-base-ids <two_holding_shape_ids>` 增量确认。

## 本轮执行计划（2026-05-20 05:20 CST）

- 上一轮 Path 1/core_multifactor 的 `industry_quality` 没有晋级，robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`；本轮开局 guard 因独立 Path 4 缺口为 `block / blocking=12`，已先按 report 原始 Path 4 `--only-base-ids` 命令补齐覆盖，再推进本路径候选。
- 本轮新增并五窗口确认 1 个 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense`。实际命令与 Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold9_turn08_exit90_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold8_turn10_exit90_weekly`。
- `quality_defense` 五窗口 CAGR 为 `11.08% / 11.92% / 24.68% / 64.23% / 59.92%`，最大回撤 `-44.53% / -40.39% / -28.08% / -10.95% / -5.49%`；短窗防守改善不能弥补 2017/2020 长窗收益与回撤弱点，未晋级。
- `update_weighted_winners.py` 后 Path 1 official winners 未变化：2017 `aggr_08_92_prom6__port_weekly_exposure_buffered`，2020/2023 `risk40_mom_exit60_reconfirm70_cap95_dd_guard50`，2025 `aggr_10_90_prom6__port_weekly_exposure_buffered`；四窗口 robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.55% / minCAGR=26.56% / worstMaxDD=-29.23% / meanTurn=4.08`。
- Guard 收尾为 `pass / blocking=0 / warning=0`，`core_multifactor=13/13 complete`，Path 1 fast-family `47/47 complete`；候选池未触发 evict。收尾 rotation 为 `stagnation_runs=6 / satellite_risk_cost / rotate`；下一轮 focus -> candidates 池应回到卫星周频风控成本，先比较 `__sat_three_stage_buffered` 的低换手/低频确认变体，不继续扩大质量多因子。
- 下一轮第一条候选命令建议先实现并补跑 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__sat_three_stage_buffered_cost_guard` 与 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered_cost_guard`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_satellite_risk_cost_ids>`。

## 本轮执行计划（2026-05-19 23:14 CST）

- 开局 guard 为 `block / blocking=10 / warning=5`；已按 report 原始 `--only-base-ids` 命令补齐 Path 1/core_multifactor 与 Path 2 coverage，随后补跑 `core_explore_80_20_total_mv_winner_core__share_10_90_hold_3_7` 的 warning 缺口，收尾 guard 为 `pass / blocking=0 / warning=0`。
- 上一轮 Path 1 新增 `growth_quality` 多因子与 3 个 holding-shape 候选均未晋级，robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered_asym13`；本轮按 rotation 继续处理 `core_multifactor_coverage` 后，新增 `industry_quality` 多因子预设。
- 本轮新增并五窗口确认的 Path 1/core_multifactor base id：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality`。实际命令与 Path 2/3 合并执行：
  `.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly`。
- `industry_quality` 五窗口 CAGR 为 `10.87% / 11.36% / 27.21% / 78.03% / 43.79%`，2017/2020 长窗与 `-42.85% / -36.44%` 回撤明显弱于现有 Path 1 锚点，未晋级；`core_multifactor=13/13 complete`，fast-family 为 `47/47 complete`，未触发 evict。
- `scripts/winner_only_pass.py` 本轮为 `base_candidates=47 / total_candidates=423 / evaluated=184`；clear improvement 只出现在旧 `since_2025_only` 候选 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered_asym13`，不是本轮新增候选。
- `update_weighted_winners.py` 后 Path 1 official winners 同步为：2017 `aggr_08_92_prom6__port_weekly_exposure_buffered`，2020/2023 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`，2025 `aggr_10_90_prom6__port_weekly_exposure_buffered`；四窗口 robust 切为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.55% / minCAGR=26.56% / worstMaxDD=-29.23% / meanTurn=4.08`。
- 收尾 rotation 为 `stagnation_runs=3 / signal_quality / rotate`；下一轮 focus -> candidates 池先落在质量/低波/行业强度信号，而不是继续扩 growth tilt。建议先实现并补跑 `aggr_08_92_prom6_core_multifactor_quality_lowvol` 与 `aggr_05_95_prom7_core_multifactor_quality_lowvol`，第一条命令仍用五窗口 `--only-base-ids`，不跑 `research_active/all`。

## 本轮执行计划（2026-05-19 17:26 CST）

- 开局与收尾 guard 均为 `pass / blocking=0 / warning=0`，首轮同步追加 `18` 条实验记录；本轮没有运行 `research_active/all`，A 股新增候选均用 `--only-base-ids` 五窗口增量确认。
- Path 1 / Path 4-lite 新增 `growth_quality` 多因子预设，并把 `aggr_08_92_prom6_core_multifactor_growth_quality`、`aggr_10_90_prom6_core_multifactor_growth_quality`、`aggr_05_95_prom7_core_multifactor_growth_quality` 加入 `core_multifactor` 方向；随后补做非多因子 `holding_shape` 三候选 `aggr_07_93_hold_3_7_ramp90`、`share_10_90_hold_3_7`、`share_06_94_hold_2_8_ramp85`。最终 fast-pass 为 `base_candidates=46 / total_candidates=414 / evaluated=183`，`core_multifactor=12 / holding_shape=10`。
- 新多因子候选没有晋级：`08/92 growth_quality` 五窗口 CAGR 为 `12.26% / 13.15% / 26.25% / 77.27% / 66.91%`，`10/90 growth_quality` 为 `12.30% / 12.96% / 25.87% / 77.80% / 65.67%`，`05/95 growth_quality` 为 `11.39% / 10.64% / 30.77% / 76.61% / 77.22%`；2017/2020 长窗收益和 `-42%~-44%` 回撤明显弱于现有 Path 1/core_multifactor 锚点。
- 新 holding-shape 候选也未晋级：`share_06_94_hold_2_8_ramp85` 在 2020/2025 为 `25.28% / 80.20% CAGR` 且 2026 为 `57.67%`，但 2017 `20.64%`、2023 `26.74%` 不足以替换当前 Path 1 winner；另外两个 `3+7` 形态 2020 约 `24.4% CAGR`、2025 约 `73%~74%`。
- `scripts/winner_only_pass.py` 仍只在旧候选上给出 2017/2023 clear improvement 观察，`update_weighted_winners.py` 后 Path 1 official winners 未变：2017 `aggr_08_92_prom6__port_weekly_exposure_buffered_asym13`，2020 `aggr_05_95_prom7__sat_three_stage_buffered`，2023 `aggr_05_95_prom7`，2025 `aggr_08_92_prom6`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered_asym13`，`meanCAGR=45.46% / minCAGR=25.86% / worstMaxDD=-28.72% / meanTurn=4.11`。
- 收尾 rotation 为 `stagnation_runs=3 / signal_quality / rotate`；下一轮先做信号质量或低波风控，不再扩大纯 growth tilt 或普通持仓形态邻域。

## 本轮执行计划（2026-05-19 11:12 CST）

- 开局与收尾 guard 均为 `pass / blocking=0 / warning=0`，收尾追加 `10` 条实验记录；Path 4-lite/core_multifactor 仍为 `9/9 complete`，9 个 base candidate 均在 `PATH1_FAST_PASS_VARIANT_IDS` 中。
- `scripts/winner_only_pass.py` 本轮为 `base_candidates=40 / total_candidates=360 / evaluated=177`；方向继续覆盖 `promotion_ramp / satellite_defense / signal_variants / core_multifactor / holding_shape / supporting_variants / drawdown_guard`。
- fast-pass raw clear 出现在 2017、2020、2025：2017 `aggr_08_92_prom6`，2020 `aggr_05_95_prom7__sat_three_stage_buffered`，2025 `aggr_08_92_prom6__port_weekly_exposure_buffered_asym13`；已用 `--only-base-ids` 五窗口增量确认，没有运行 `research_active/all`。
- `update_weighted_winners.py` 后 Path 1 official winners 切换为：2017 `aggr_08_92_prom6__port_weekly_exposure_buffered_asym13`，2020 `aggr_05_95_prom7__sat_three_stage_buffered`，2023 `aggr_05_95_prom7`，2025 `aggr_08_92_prom6`。
- 四窗口 robust candidate 切换为 `aggr_08_92_prom6__port_weekly_exposure_buffered_asym13`，`meanCAGR=45.46% / minCAGR=25.86% / worstMaxDD=-28.72% / meanTurn=4.11`。
- raw 2023 仍由 `aggr_05_95_prom7_core_multifactor_balanced__sat_weekly_risk` 领先，但 official 口径没有晋升；收尾 rotation 为 `stagnation_runs=0 / core_multifactor_coverage / continue`，下一轮继续复核 core_multifactor 的短窗优势和周度仓位 overlay 的换手代价。

## 本轮执行计划（2026-05-19 05:29 CST）

- 开局与收尾均运行 `.venv/bin/python scripts/research_iteration_guard.py`；收尾 guard 为 `pass / blocking=0 / warning=0`，并追加 `78` 条实验记录。
- 已复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 仍全部在 `PATH1_FAST_PASS_VARIANT_IDS` 中；Path 4-lite/core_multifactor 五窗口覆盖继续为 `9/9 complete`。
- Path 1 fast-pass 复跑为 `base_candidates=40 / total_candidates=360 / evaluated=177`；raw clear improvement 出现在 `since_2023_only` 的 `aggr_05_95_prom7_core_multifactor_balanced__sat_weekly_risk`，但 weighted 同步后 official 2023 winner 仍保留原 `aggr_05_95_prom7_core_multifactor_balanced`。
- 本轮用 `--only-base-ids` 增量确认多因子与新增候选；由于命令未锁 `--end-date`，数据准备触发到 `2026-05-19` 缓存并遇到 Tushare 限频，随后继续使用本地缓存完成，未运行 `research_active/all`。
- `update_weighted_winners.py` 验证后，Path 1 tracked winners 同步为：2017/2023/2025 `aggr_05_95_prom7_core_multifactor_balanced`，2020 `aggr_08_92_prom6_core_multifactor_balanced`。
- 四窗口 robust candidate 切换为 `aggr_10_90_prom6_core_multifactor_balanced`，`meanCAGR=35.95% / minCAGR=14.72% / worstMaxDD=-41.55% / meanTurn=4.03`。
- 收尾 rotation 为 `stagnation_runs=0 / recommended_focus=core_multifactor_coverage / continue`；下一轮继续复核多因子胜出是否只是短期缓存日差异，并观察 `sat_weekly_risk` 的回撤改善能否通过 official 口径。

## 本轮执行计划（2026-05-18 23:13 CST）

- 开局与收尾均运行 `.venv/bin/python scripts/research_iteration_guard.py`；收尾 guard 为 `pass / blocking=0 / warning=0`，并追加 `7` 条实验记录。
- 已复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 仍全部在 `PATH1_FAST_PASS_VARIANT_IDS` 中；Path 4-lite/core_multifactor 覆盖无缺口。
- Path 1 fast-pass 复跑为 `base_candidates=40 / total_candidates=360 / evaluated=177`；方向规模为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4 / drawdown_guard=7`。
- fast-pass 只在 `since_2025_01` 找到 clear candidate：`aggr_10_90_prom6_cash_off__port_weekly_exposure_buffered_asym13`，`101.52% CAGR / -10.80% MaxDD / 2.01 Sharpe / 4.78 Turn`；已用 `--only-base-ids` 对该 base id 做五窗口增量确认。
- `update_weighted_winners.py` 验证后，Path 1 official tracked winners 同步为：2017 `aggr_08_92_prom6_cash_off`，2020 `aggr_05_95_prom7__sat_three_stage_buffered`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.74% / minCAGR=26.68% / worstMaxDD=-29.23% / meanTurn=4.08`。
- 收尾 rotation 为 `stagnation_runs=0 / recommended_focus=core_multifactor_coverage / continue`；下一轮继续复核多因子覆盖与 2025 raw clear 的验证口径差异。

## 本轮执行计划（2026-05-18 20:34 CST）

- 开局 guard 为 `warn / blocking=0 / warning=7`，缺口集中在 `ashare_path1_fast_family`；已按 report 给出的 `--only-base-ids` 增量 rerun command 用离线缓存补齐，收尾 guard 升为 `pass / blocking=0 / warning=0`。
- 本轮修正 `read_cached_csv()` 对空缓存文件的容错，避免 warning 补跑遇到空 CSV 时中断；这只影响缓存读取健壮性，不改变策略逻辑。
- 已复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 继续全部在 `PATH1_FAST_PASS_VARIANT_IDS` 中；Path 4-lite/core_multifactor 五窗口覆盖完整。
- Path 1 fast-pass 复跑为 `base_candidates=40 / total_candidates=360 / evaluated=177`；新增 `drawdown_guard=7` 方向后，方向规模为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4 / drawdown_guard=7`。
- `update_weighted_winners.py` 验证后，Path 1 2020/2023 window winner 切换为 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`，对应 `38.76% / 44.23% CAGR`；2017 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，2025 仍为 `aggr_10_90_prom6__port_weekly_exposure_buffered`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=1 / recommended_focus=core_multifactor_coverage / continue`；下一轮在新 winner 生效后，继续检查 core_multifactor 覆盖与 drawdown_guard 的回撤/换手代价，不回到旧失败邻域盲调。

## 本轮执行计划（2026-05-18 11:11 CST）

- 开局与收尾均运行 `.venv/bin/python scripts/research_iteration_guard.py`；收尾 guard 为 `pass / blocking=0 / warning=0`，A 股 Path 1 fast-family 与 Path 4-lite/core_multifactor 均无覆盖缺口。
- 已复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 全部在 `PATH1_FAST_PASS_VARIANT_IDS` 中；五窗口覆盖继续完整。
- Path 1 fast-pass 复跑为 `base_candidates=33 / total_candidates=297 / evaluated=170`；方向规模仍为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4`。
- 本轮没有 clear improvement：2017/2020 raw best 仍以更深回撤换收益，2023/2025 raw best 的 Sharpe 或回撤不足以替换 incumbent。
- Path 1 tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=23 / recommended_focus=holding_shape / rotate`；下一轮优先回到持仓形态与低成本确认，不在旧 weekly exposure 邻域继续微调。

## 本轮执行计划（2026-05-18 05:53 CST）

- 开局与收尾均运行 `.venv/bin/python scripts/research_iteration_guard.py`；收尾 guard 为 `pass / blocking=0 / warning=0`，A 股 Path 1 fast-family 与 Path 4-lite/core_multifactor 覆盖均无缺口。
- 已复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 全部在 `PATH1_FAST_PASS_VARIANT_IDS` 中；五窗口覆盖继续完整。
- Path 1 fast-pass 复跑为 `base_candidates=33 / total_candidates=297 / evaluated=170`；方向规模仍为 `5 / 5 / 2 / 9 / 7 / 4`。
- 本轮没有 clear improvement：2017/2020 raw best 仍以更深回撤换收益，2023/2025 raw best 的 Sharpe 或回撤不足以替换 incumbent。
- Path 1 tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=20 / recommended_focus=satellite_risk_cost / rotate`；下一轮继续优先卫星风险成本和低成本确认，不在旧 weekly exposure 邻域继续微调。

## 本轮执行计划（2026-05-17 23:12 CST）

- 开局与收尾均运行 `.venv/bin/python scripts/research_iteration_guard.py`；收尾 guard 继续为 `pass / blocking=0 / warning=0`，A 股 Path 1 fast-family 与 Path 4-lite/core_multifactor 覆盖均无缺口。
- 已再次复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 全部在 `PATH1_FAST_PASS_VARIANT_IDS` 中，且 guard 对五窗口覆盖保持完整。
- Path 1 fast-pass 复跑为 `base_candidates=33 / total_candidates=297 / evaluated=170`；方向规模为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4`。
- 本轮没有 clear improvement：2017 raw best `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered` 收益更高但 `MaxDD=-28.16%` 劣于当前 winner；2020 raw best `aggr_05_95_prom7__sat_three_stage_buffered_asym13` 回撤加深到 `-30.57%`。
- 2023 raw best `aggr_10_90_hold_4_6__port_weekly_exposure_buffered_asym13` 的 Sharpe 低于 incumbent；2025 raw best `aggr_10_90_prom6__port_weekly_exposure_buffered_asym13` 的 Sharpe 与回撤不足以替换。
- Path 1 tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=18 / recommended_focus=satellite_risk_cost / rotate`；下一轮继续优先卫星风险成本与低成本确认，不在旧 weekly exposure 邻域继续微调。

## 本轮执行计划（2026-05-17 17:25 CST）

- 开局 guard 为 `warn / blocking=0 / warning=13`，已按 `ashare_path1_fast_family` 增量 rerun command 用 `--only-base-ids` 补齐 13 个 fast-family 非阻塞缺口；收尾 guard 升为 `pass / blocking=0 / warning=0`。
- 已再次复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 全部在 `PATH1_FAST_PASS_VARIANT_IDS` 中，且五窗口覆盖完整；Path 4-lite/core_multifactor 本轮无缺口。
- Path 1 fast-pass 复跑为 `base_candidates=33 / total_candidates=297 / evaluated=170`；方向规模为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4`。
- 本轮没有 clear improvement：2017 raw best `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered` 收益更高但 `MaxDD=-28.16%` 劣于当前 winner；2020 raw best `aggr_05_95_prom7__sat_three_stage_buffered_asym13` 回撤加深到 `-30.57%`。
- 2023 raw best 的 Sharpe 不足，2025 raw best 虽有 `101.52% CAGR` 但 Sharpe 与回撤均劣于现有口径；Path 1 tracked winners 与 robust candidate 未变。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=15 / recommended_focus=signal_quality / rotate`；下一轮在 coverage 已清零后优先转向信号质量，不继续旧 weekly exposure 邻域微调。

## 本轮执行计划（2026-05-17 11:15 CST）

- 开局与收尾均运行 `.venv/bin/python scripts/research_iteration_guard.py`；收尾 coverage gate 仍为 `warn / blocking=0 / warning=13`，Path 4-lite/core_multifactor 固定项继续 `9/9 complete`，13 个 warning 仍是旧 fast-family ID 的非阻塞缺口。
- 已再次复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 均在 `PATH1_FAST_PASS_VARIANT_IDS` 中，且 guard 确认五窗口覆盖完整。
- Path 1 fast-pass 复跑为 `base_candidates=33 / total_candidates=297 / evaluated=157`；方向规模保持 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4`。
- 本轮没有 clear improvement：2017 raw best `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered` 收益更高但回撤劣化；2020 raw best `aggr_05_95_prom7__sat_three_stage_buffered_asym13` 仍以明显更深回撤换收益。
- Path 1 tracked winners 未变：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，2020 `aggr_08_92_prom6_cash_off`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=12 / recommended_focus=core_multifactor_coverage / rotate`；下一轮优先处理 core_multifactor 覆盖观察与 13 个 fast-family warning 的可生成性，不继续旧周度 overlay 邻域微调。

## 本轮执行计划（2026-05-17 05:15 CST）

- 开局与收尾均运行 `.venv/bin/python scripts/research_iteration_guard.py`；收尾 coverage gate 为 `warn / blocking=0 / warning=13`，Path 4-lite/core_multifactor 固定项继续 `9/9 complete`，13 个 warning 仍是旧 fast-family ID 的非阻塞缺口。
- 已复核 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 均在 `PATH1_FAST_PASS_VARIANT_IDS` 中，且完整 base id 在 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01` 五窗口均有结果。
- Path 1 fast-pass 复跑为 `base_candidates=33 / total_candidates=297 / evaluated=157`；六个方向规模仍为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4`。
- 本轮没有 clear improvement：2017 raw best 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（`27.89% CAGR / -28.16% MaxDD / 1.14 Sharpe / 3.62 Turn`），但回撤劣化；2020 raw best `aggr_05_95_prom7__sat_three_stage_buffered_asym13` 收益更高但回撤显著加深。
- Path 1 tracked winners 未变：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，2020 `aggr_08_92_prom6_cash_off`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=10 / recommended_focus=holding_shape / rotate`；下一轮优先处理 holding shape 与 13 个 fast-family warning 的可生成性，不继续在旧周度仓位 overlay 邻域微调。

## 本轮执行计划（2026-05-16 23:12 CST）

- 开局与收尾均运行 `.venv/bin/python scripts/research_iteration_guard.py`；coverage gate 保持 `warn / blocking=0 / warning=13`，Path 4-lite/core_multifactor 固定项为 `9/9 complete`，非阻塞缺口仍集中在 13 个旧 fast-family ID。
- Path 1 fast-pass 复跑为 `base_candidates=33 / total_candidates=297 / evaluated=157`；六个方向规模为 `5 / 5 / 2 / 9 / 7 / 4`，`core_multifactor` 9 个 base candidate 全部仍在候选池中。
- 本轮没有 clear improvement：2017 raw best 为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（`27.89% CAGR / -28.16% MaxDD / 1.14 Sharpe / 3.62 Turn`），但回撤劣化未改写 tracked winner；2020 raw best 为 `aggr_05_95_prom7__sat_three_stage_buffered_asym13`，收益更高但回撤明显加深。
- Path 1 tracked winners 未变：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，2020 `aggr_08_92_prom6_cash_off`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=8 / recommended_focus=satellite_risk_cost / rotate`；下一轮优先处理卫星风险成本与 13 个 fast-family warning 的可生成性，不继续旧 weekly exposure 邻域微调。

## 本轮执行计划（2026-05-16 17:14 CST）

- 开局 guard 因新旧结果布局聚合只剩 `80` 条 A 股 comparison 行而显示 `block / blocking=502`；已先用本地 `summary.json` 缓存重建 `results/research/a_share/strategy_comparison*.csv` 到 `8693` 行 / `2137` 个 base strategies，随后 guard 降为 `warn / blocking=0 / warning=13`。
- Path 4-lite/core_multifactor 固定项继续完整覆盖：`core_multifactor` 9 个 base candidate 全部在 `winner_only_pass.py` 的方向池中，且五窗口覆盖不再阻塞。
- Path 1 快筛复跑为 `base_candidates=33 / total_candidates=297 / evaluated=157`；`promotion_ramp / satellite_defense / signal_variants / core_multifactor / holding_shape / supporting_variants` 均被巡检，本轮仍没有 clear improvement。
- Path 1 tracked winners 未变：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，2020 `aggr_08_92_prom6_cash_off`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 guard 为 `warn / blocking=0 / warning=13`，rotation 为 `stagnation_runs=6 / recommended_focus=satellite_risk_cost / rotate`；下一轮优先处理卫星风险成本与 13 个 fast-family warning 的可生成性，不继续旧周度 overlay 邻域微调。

## 本轮执行计划（2026-05-16 11:20 CST）

- 开局 guard 因 comparison 迁移后的聚合缺口显示 `block / blocking=502`；已先用本地 `summary.json` 缓存重建 `results/research/a_share/strategy_comparison*.csv` 到 `8613` 行 / `2137` 个 base strategies，随后 guard 降为 `warn / blocking=0 / warning=13`。
- Path 4-lite/core_multifactor 固定项已确认：`PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 的 9 个 base candidate 全部在 fast-pass 池中，并完整覆盖 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`。
- 复跑 `scripts/winner_only_pass.py` 后，Path 1 快筛为 `base_candidates=33 / total_candidates=297 / evaluated=157`，方向规模仍为 `5 / 5 / 2 / 9 / 7 / 4`；本轮没有 clear improvement。
- Path 1 tracked winners 未变：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，2020 `aggr_08_92_prom6_cash_off`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 guard 为 `warn / blocking=0 / warning=13`，rotation 为 `stagnation_runs=2 / recommended_focus=core_multifactor_coverage / continue`；下一轮优先处理 13 个 fast-family warning 的可生成性，而不是继续扩旧周度 overlay 邻域。

## 本轮执行计划（2026-05-16 06:56 CST）

- 本轮开局 guard 为 `block`，优先补齐 Path 4-lite/core_multifactor 与 Path 2 blocking coverage；补齐后 Path 4-lite/core_multifactor 9 个 base candidate 已完整覆盖五个要求窗口，收尾 guard 暂为 `warn / blocking=0 / warning=13`。
- `ashare_path1_fast_family` 的 13 个 warning 缺口仍为非阻塞项，集中在尚未由当前回测生成器产出的旧 fast-family ID；本轮不把它们作为 Path 1 winner 判断前置条件。
- 复跑 `scripts/winner_only_pass.py` 后，快筛口径为 `base_candidates=33 / total_candidates=297 / evaluated=157`；方向规模仍为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4`，本轮没有 clear improvement。
- Path 1 tracked winners 未变：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，2020 `aggr_08_92_prom6_cash_off`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.94% / minCAGR=26.85% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 收尾 rotation 为 `stagnation_runs=15 / recommended_focus=signal_quality / rotate`；下一轮先处理 fast-family 可生成性与信号质量口径，再比较 holding_shape 的低成本确认。

## 本轮执行计划（2026-05-15 15:16 CST）

- 本轮起止两次运行 `.venv/bin/python scripts/research_iteration_guard.py`，coverage gate 保持 `pass / blocking=0 / warning=0`；Path 4-lite/core_multifactor 9 个 base candidate 已确认全部在 `PATH1_FAST_PASS_VARIANT_IDS` 中，并完整覆盖五个要求窗口。
- 复跑 `scripts/winner_only_pass.py` 后，Path 1 快筛仍为 `base_candidates=33 / total_candidates=297 / evaluated=179`；六个方向规模为 `5 / 5 / 2 / 9 / 7 / 4`，本轮没有 clear improvement。
- Path 1 四窗口 tracked winners 未变：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，2020 `aggr_08_92_prom6_cash_off`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=48.03% / minCAGR=27.14% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 最终 rotation 为 `stagnation_runs=7 / recommended_focus=satellite_risk_cost / rotate`；下一轮不要继续旧周度仓位邻域微调，优先比较卫星风险成本与信号质量约束。

## 本轮执行计划（2026-05-15 10:14 CST）

- 本轮起始 guard 为 `pass`，收尾前曾因新增 `weekly_alpha_*` 纯周频族的 `total_mv` 覆盖缺口进入 block；已按 guard rerun commands 补齐后重建五窗口 `strategy_comparison.csv` 到 `6807` 行，最终 guard 为 `pass / blocking=0 / warning=0`。
- `winner_only_pass.py` 仍为 `base_candidates=33 / total_candidates=297 / evaluated=179`，Path 4-lite/core_multifactor 9 个 base candidate 继续完整覆盖五窗口；本轮没有新的 Path 1 clear improvement。
- Path 1 四窗口 tracked winners 未变：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，2020 `aggr_08_92_prom6_cash_off`，2023 `aggr_05_95_prom7_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_6_1`。
- 四窗口 robust candidate 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=48.03% / minCAGR=27.14% / worstMaxDD=-29.23% / meanTurn=4.07`；最终 rotation 为 `stagnation_runs=5 / signal_quality`，下一轮不继续在旧周度 overlay 邻域微调。

## 本轮执行计划（2026-05-14 22:55 CST）

- 本轮开局 guard 因 aggregate CSV 未覆盖 `since_2025_01 / since_2026_01` 显示 block；已按 blocking rerun commands 补齐 Path 4-lite/core_multifactor 与 Path 2/3 缺口，并用显式五窗口重建 `strategy_comparison.csv`，收尾 guard 为 `pass / blocking=0 / warning=0`。
- `winner_only_pass.py` 本轮仍为 `base_candidates=33 / total_candidates=297 / evaluated=179`，raw clear 出现在 2017 与 2025；已对 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure` 与 `aggr_08_92_prom6_core_6_1__sat_three_stage_buffered` 补跑五窗口确认。
- `update_weighted_winners.py` 后 Path 1 tracked winners 已同步为：2017 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`（`26.83% CAGR / -23.65% MaxDD / 1.1204 Sharpe / 3.57 Turn`），2020 `aggr_08_92_prom6_cash_off`（`23.37% / -15.47% / 0.9869 / 2.28`），2023 `aggr_05_95_prom7_core_multifactor_balanced`（`33.79% / -30.00% / 1.0731 / 3.59`），2025 `aggr_08_92_prom6_core_6_1`（`99.96% / -8.73% / 2.3793 / 5.39`）。
- Path 1 四窗口候选仍以 `aggr_08_92_prom6__port_weekly_exposure_buffered` 为主；最终 guard 为 `stagnation_runs=1 / recommended_focus=core_multifactor_coverage`，下一轮优先看多因子覆盖、信号质量与低成本确认。

## 本轮执行计划（2026-05-14 15:10 CST）

- 本轮起止两次运行 `.venv/bin/python scripts/research_iteration_guard.py`，收尾 coverage gate 为 `pass`，blocking/warning 均为 `0`；Path 4-lite/core_multifactor 9 个 base candidate 继续完整覆盖 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`。
- 收尾 rotation 为 `stagnation_runs=13 / recommended_focus=core_multifactor_coverage / rotation_status=rotate`；本轮不继续扩旧周度 overlay 邻域，只固定记录 core_multifactor best/top5 与验证口径差异。
- 复跑 `.venv/bin/python scripts/winner_only_pass.py` 后，快筛口径仍为 `as_of=2026-05-13 / base_candidates=33 / total_candidates=297 / evaluated=179`；方向数为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4`。
- raw clear 仍只出现在 `since_2017_01` 与 `since_2025_01`：2017 clear 为 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，`26.03% CAGR / -23.65% MaxDD / 1.0963 Sharpe / 0.79 Turnover`；2025 clear 为 `aggr_08_92_prom6_core_6_1__sat_three_stage_buffered`，`96.47% / -8.73% / 2.2272 / 1.29`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，验证口径未改写 Path 1 四窗口 winner：2017 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，2020/2023/2025 仍为 `core_explore_80_20_total_mv_winner_core`，指标为 `23.30% / 25.67% / 31.71% / 87.17% CAGR`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=49.23% / minCAGR=27.41% / worstMaxDD=-29.23% / meanTurn=4.07`；下一轮仍先围绕 core_multifactor 覆盖观察和低成本持仓形态做对照，不把 raw fast-pass 命中直接晋升。

## 本轮执行计划（2026-05-14 09:13 CST）

- 本轮起止两次运行 `.venv/bin/python scripts/research_iteration_guard.py`，收尾 coverage gate 为 `pass`，blocking/warning 均为 `0`；Path 4-lite/core_multifactor 9 个 base candidate 已完整覆盖 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`。
- 收尾 rotation 继续为 `stagnation_runs=11 / recommended_focus=holding_shape / rotation_status=rotate`，因此本轮不继续扩大旧 `weekly_exposure` 邻域，只记录持仓形态与多因子固定观察项的验证结果。
- 复跑 `.venv/bin/python scripts/winner_only_pass.py` 后，快筛口径仍为 `as_of=2026-05-13 / base_candidates=33 / total_candidates=297 / evaluated=179`；方向数为 `promotion_ramp=5 / satellite_defense=5 / signal_variants=2 / core_multifactor=9 / holding_shape=7 / supporting_variants=4`。
- raw clear 仍只出现在 `since_2017_01` 与 `since_2025_01`：2017 clear 为 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，`26.03% CAGR / -23.65% MaxDD / 1.0963 Sharpe / 0.79 Turnover`；2025 clear 为 `aggr_08_92_prom6_core_6_1__sat_three_stage_buffered`，`96.47% / -8.73% / 2.2272 / 1.29`。
- 验证口径未改写 Path 1 四窗口 winner：2017 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，2020/2023/2025 仍为 `core_explore_80_20_total_mv_winner_core`，指标为 `23.30% / 25.67% / 31.71% / 87.17% CAGR`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=49.23% / minCAGR=27.41% / worstMaxDD=-29.23% / meanTurn=4.07`。
- core_multifactor 继续只作为 Path 1 固定验证项：当前 raw best 为 `aggr_05_95_prom7_core_multifactor_balanced` 的 2023 窗口 `34.35% CAGR`，但回撤/换手与验证规则不足以改写 tracked winner；下一轮仍按 `holding_shape` 优先比较持仓形态和低成本周度防守。

## 本轮执行计划（2026-05-14 03:17 CST）

- 本轮 guard 覆盖率为 `pass`，Path 4-lite/core_multifactor 9 个 base candidate 已完整覆盖 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`；收盘 guard 将 Path 1 rotation 推进到 `stagnation_runs=9 / recommended_focus=holding_shape`。
- 复跑 `.venv/bin/python scripts/winner_only_pass.py` 后，快筛口径仍为 `as_of=2026-05-13 / base_candidates=33 / total_candidates=297 / evaluated=179`，并保留 `promotion_ramp / satellite_defense / signal_variants / core_multifactor / holding_shape / supporting_variants` 六个方向。
- raw clear 仍只出现在 `since_2017_01` 与 `since_2025_01`：2017 clear 为 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，`26.03% CAGR / -23.65% MaxDD / 1.0963 Sharpe / 0.79 Turnover`；2025 clear 为 `aggr_08_92_prom6_core_6_1__sat_three_stage_buffered`，`96.47% / -8.73% / 2.2272 / 1.29`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，验证口径未改写 Path 1 四窗口 winner：2017 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，2020/2023/2025 仍为 `core_explore_80_20_total_mv_winner_core`。
- 最新 tracked 指标为 `23.30% / 25.67% / 31.71% / 87.17% CAGR`；四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=49.23% / minCAGR=27.41%`。
- core_multifactor best 仍偏窗口化：2017 最好为 `aggr_05_95_prom7_core_multifactor_balanced`（`15.38% CAGR`），2020 最好为 `aggr_08_92_prom6_core_multifactor_balanced`（`17.54%`），2023/2025 最好为 `aggr_05_95_prom7_core_multifactor_balanced`（`34.35% / 89.24%`），但没有改写 Path 1 winner；下一步按 `holding_shape` 比较持仓形态与低成本周度风控/仓位 overlay。

## 本轮执行计划（2026-05-13 21:21 CST）

- 本轮先按 `research_iteration_guard.py` 补齐 Path 4-lite/core_multifactor 五窗口覆盖，随后将 comparison CSV 从本地 `summary.json` 重建到 `3500` 行 / `877` 个 base strategies；最终 coverage gate 为 `pass`，blocking/warning 均为 `0`。
- Path 1 fast-pass 口径为 `as_of=2026-05-13 / base_candidates=33 / total_candidates=297 / evaluated=179`；`core_multifactor` 9 个 base candidate 已在五窗口覆盖，但仍只作为 Path 1 固定方向内的观察项。
- raw clear 仍出现在 `since_2017_01` 与 `since_2025_01`：2017 raw best 是 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，2025 raw best 是 `aggr_08_92_prom6__port_weekly_exposure_buffered`；验证后均未改写 tracked winner。
- Path 1 tracked winners 仍为：2017 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，2020/2023/2025 `core_explore_80_20_total_mv_winner_core`；对应指标为 `23.30% / 25.67% / 31.71% / 87.17% CAGR`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=49.23% / minCAGR=27.41% / worstMaxDD=-29.23% / meanTurn=4.07`；rotation 已提示下一轮 Path 1 应转向 `satellite_risk_cost`，避免继续在同一失败邻域微调。

## 本轮执行计划（2026-05-13 09:13 CST）

- 本轮在既有 dirty 工作树上复跑 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径仍为 `as_of=2026-05-12 / base_candidates=33 / total_candidates=297 / evaluated=170`；方向继续限定在 `promotion_ramp / satellite_defense / signal_variants / core_multifactor / holding_shape / supporting_variants`。
- raw 快筛继续给出 `since_2017_01` 与 `since_2025_01` clear candidates：2017 最近似仍为 `aggr_10_90_fast_ramp_cash_off__port_weekly_exposure`，`26.03% CAGR / -23.65% MaxDD / 1.0963 Sharpe / 0.79 Turnover`；2025 最近似为 `aggr_08_92_prom6_core_6_1__sat_three_stage_buffered`，`96.47% / -8.73% / 2.2272 / 1.29`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，验证口径未改写 Path 1 四窗口 winner：2017 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，2020/2023/2025 仍为 `core_explore_80_20_total_mv_winner_core`。
- 最新验证指标为：2017 `22.95% CAGR / -24.00% MaxDD / 0.9649 Sharpe / 2.64 Turnover`，2020 `25.03% / -20.97% / 0.9371 / 2.91`，2023 `30.41% / -27.24% / 0.9831 / 2.91`，2025 `84.06% / -9.38% / 1.9322 / 4.35`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=48.03% / minCAGR=26.91% / worstMaxDD=-29.23% / meanTurn=4.07`；本轮只做结果、图表、live/public 快照同步，不引入新的 Path 1 变体。

## 本轮执行计划（2026-05-13 03:32 CST）

- 本轮在既有 dirty 工作树上复跑 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径为 `as_of=2026-05-12 / base_candidates=33 / total_candidates=297 / overlay_candidates=264`；方向仍限定在 `promotion_ramp / satellite_defense / signal_variants / core_multifactor / holding_shape / supporting_variants`。
- raw 快筛继续给出 `since_2017_01` 与 `since_2025_01` clear candidates：2017 best 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`28.43% CAGR / -28.16% MaxDD / 1.1512 Sharpe / 3.62 Turnover`；2025 best 仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`106.28% / -10.72% / 2.0289 / 4.73`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，验证口径仍未改写 Path 1 四窗口 winner：2017 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，2020/2023/2025 仍为 `core_explore_80_20_total_mv_winner_core`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=48.03% / minCAGR=26.91% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 本轮没有引入新的 Path 1 变体；A 股 Path 2 的月频高收益候选与纯 `_weekly` 候选继续分别留在 Path 2 / Path 3。

## 本轮执行计划（2026-05-12 21:20 CST）

- 本轮在已有 dirty 工作树上先运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径为 `as_of=2026-05-12 / base_candidates=33 / total_candidates=297 / evaluated=25`；`core_multifactor` 仍使 base 数高于原 `24-28`，但仍限定在 Path 1 固定方向内。
- raw 快筛继续只给出近似改善而非 clear replacement：2017 raw best 为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`28.43% CAGR / -28.16% MaxDD / 1.1512 Sharpe / 3.62 Turnover`；2020 raw best 为 `aggr_05_95_prom7__sat_three_stage_buffered`，`29.27% / -31.00% / 1.0131 / 3.45`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，验证口径未改写 Path 1 四窗口 winner：2017 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，2020/2023/2025 仍为 `core_explore_80_20_total_mv_winner_core`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，更新后为 `meanCAGR=48.03% / minCAGR=26.91% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 本轮 A 股 Path 2 的 `risk40_mom_exit60_reconfirm*_caution80` 候选只作为 Path 2 独立上限观察；纯 `_weekly` 候选继续只交给 Path 3。

## 本轮执行计划（2026-05-12 09:12 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径仍为 `as_of=2026-05-11 / base_candidates=33 / total_candidates=297 / evaluated=170`；`core_multifactor` 继续使 base 数高于原 `24-28` 目标，但仍只作为 Path 1 固定方向内扩展。
- raw 快筛继续在 `since_2017_01 / since_2020_01 / since_2025_01` 给出 clear candidates，其中 2020 最近似仍为 `share_15_85_hold_4_6`，`25.16% CAGR / -21.37% MaxDD / 0.9362 Sharpe / 2.93 Turnover`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，验证口径未改写 Path 1 四窗口 winner：2017 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，2020/2023/2025 仍为 `core_explore_80_20_total_mv_winner_core`。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.47% / minCAGR=26.40% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 本轮 A 股 Path 2 新增并胜出的 `risk40_mom_exit60_reconfirm70/reconfirm75` 高成长主线候选不并入 Path 1；纯 `_weekly` 候选继续只交给 Path 3。

## 本轮执行计划（2026-05-12 03:16 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径为 `as_of=2026-05-11 / base_candidates=33 / total_candidates=297 / evaluated=170`；`core_multifactor` 仍使 base 数高于原 `24-28` 目标，但继续只作为 Path 1 固定方向内的候选扩展。
- raw 快筛仍在 `since_2017_01 / since_2020_01 / since_2025_01` 找到 clear candidates，其中 2020 最近似为 `share_15_85_hold_4_6`，`25.16% CAGR / -21.37% MaxDD / 0.9362 Sharpe / 2.93 Turnover`。
- 复跑 `.venv/bin/python scripts/update_weighted_winners.py` 后，验证口径未改写 Path 1 四窗口 winner：四个窗口继续为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`（2017）与 `core_explore_80_20_total_mv_winner_core`（2020/2023/2025）。
- 四窗口鲁棒候选仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.47% / minCAGR=26.40% / worstMaxDD=-29.23% / meanTurn=4.07`。
- 本轮 A 股 Path 2 新增的 `risk50_mom_exit60_reconfirm70/reconfirm65` 高成长主线候选不并入 Path 1；纯 `_weekly` 候选继续只交给 Path 3。

## 本轮执行计划（2026-05-11 21:22 CST）

- 本轮先修复 `scripts/winner_only_pass.py`、`scripts/update_weighted_winners.py` 与 `scripts/path2_candidate_pass.py` 的 Python 常量解析器，使其能解析 `MULTI_FACTOR_PRESETS[...]` 这类引用式常量；这是为了让已有 `core_multifactor` 方向进入快筛，不改变策略打分规则。
- 复跑 `.venv/bin/python scripts/winner_only_pass.py` 后，快筛口径为 `as_of=2026-05-11 / base_candidates=33 / total_candidates=297 / evaluated=170`；base 数高于原 `24-28` 是因为当前代码库已有 `core_multifactor` 方向，最终仍以 `update_weighted_winners.py` 的验证/active 口径为准。
- Path 1 `since_2017_01` 验证 winner 同步为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6`，`22.59% CAGR / -24.00% MaxDD / 0.9544 Sharpe / 2.64 Turnover`；raw 更高的 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered` 因验证口径被替换。
- `since_2020_01 / since_2023_01 / since_2025_01` 验证 winner 仍为 `core_explore_80_20_total_mv_winner_core`，分别为 `24.43% / -20.97% / 0.9228 / 2.91`、`28.24% / -27.24% / 0.9385 / 2.91`、`80.27% / -9.38% / 1.8839 / 4.35`。
- 四窗口鲁棒候选同步为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=46.47% / minCAGR=26.40% / worstMaxDD=-29.23% / meanTurn=4.07`；A 股 Path 2 新增月频候选与纯 `_weekly` 候选仍不并入 Path 1。

## 本轮执行计划（2026-05-11 15:15 CST）

- 本轮运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径仍为 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`；五个方向继续限定在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants`。
- Path 1 四窗口 winner 未被改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% / -31.00% / 0.9776 / 0.76`；`since_2023_01` 仍由 `aggr_08_92_prom6_cash_off__sat_weekly_risk` 占优，`25.37% / -12.34% / 1.0722 / 1.02`。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% / -11.64% / 2.1472 / 1.37`；四窗口鲁棒候选仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=43.26% / minCAGR=25.26% / worstMaxDD=-29.23% / meanTurn=0.92`。
- 本轮新增的 A 股 Path 2 `risk50_mom_exit60_caution80/caution75` 月频候选不并入 Path 1；纯 `_weekly` 候选继续只交给 Path 3。

## 本轮执行计划（2026-05-11 09:19 CST）

- 本轮运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径为 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`；五个方向仍限定在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants`。
- 快筛没有清晰改写 Path 1 窗口 winner：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% / -31.00% / 0.9776 / 0.76`；`since_2023_01` 与 `since_2025_01` 继续分别由周频防守 overlay 与 buffered weekly exposure 占优。
- 四窗口鲁棒候选仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=43.26% / minCAGR=25.26% / worstMaxDD=-29.23% / meanTurn=0.92`。
- 本轮新增的 A 股 Path 2 `risk50_mom_exit60_reconfirm75/reconfirm80_amt110` 独立上限候选不并入 Path 1；纯 `_weekly` 候选继续只交给 Path 3。

## 本轮执行计划（2026-05-11 03:13 CST）

- 本轮运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径仍为 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`，五个方向继续限定为 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants`。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% / -31.00% / 0.9776 / 0.76`；`since_2023_01` 的高 CAGR 候选继续因 Sharpe 与回撤不足不替换。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% / -11.64% / 2.1472 / 1.37`；四窗口鲁棒候选仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=43.26% / minCAGR=25.26% / worstMaxDD=-29.23% / meanTurn=0.92`。
- 本轮新增的 A 股 Path 2 `risk50_mom top12/top18` 量价晋升阈值候选不并入 Path 1；纯 `_weekly` 候选继续留在 Path 3。

## 本轮执行计划（2026-05-10 21:14 CST）

- 本轮运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径继续为 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`；方向仍限定在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants`。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% / -31.00% / 0.9776 / 0.76`；`since_2023_01` 的更高 CAGR 候选仍因 Sharpe 与回撤不足不替换。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% / -11.64% / 2.1472 / 1.37`；四窗口鲁棒候选仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=43.26% / minCAGR=25.26% / worstMaxDD=-29.23% / meanTurn=0.92`。
- 本轮 A 股 Path 2 新增的 `risk50_mom_caution*` 风险节奏候选不并入 Path 1；纯 `_weekly` 候选继续留在 Path 3。

## 本轮执行计划（2026-05-10 15:04 CST）

- 本轮运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径保持 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`；仍限定在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% / -31.00% / 0.9776 / 0.76`；`since_2023_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 虽有更高 CAGR，但 Sharpe 与回撤仍不足以替换。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% / -11.64% / 2.1472 / 1.37`；四窗口鲁棒候选仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=43.26% / minCAGR=25.26% / worstMaxDD=-29.23% / meanTurn=0.92`。
- A 股 Path 2 本轮新增的 `risk50_mom + 晋升确认过滤` 不并入 Path 1；纯 `_weekly` 仍留在 Path 3。

## 本轮执行计划（2026-05-10 09:17 CST）

- 本轮继续运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径保持 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 仍严格限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向；本轮新增的 A 股 Path 2 `risk50_mom_exit80/exit60` 候选不并入 Path 1，纯 `_weekly` 候选也继续留在 Path 3。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% CAGR / -31.00% MaxDD / 0.9776 Sharpe / 0.76 Turnover`；`since_2023_01` 的高 CAGR `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 仍因 Sharpe 与回撤不足不替换。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% CAGR / -11.64% MaxDD / 2.1472 Sharpe / 1.37 Turnover`；四窗口鲁棒候选仍为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=43.26% / minCAGR=25.26% / worstMaxDD=-29.23% / meanTurn=0.92`。

## 本轮执行计划（2026-05-10 03:16 CST）

- 本轮继续运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径保持 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 仍限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向；本轮不吸收 A 股 Path 2 的三档择时线，也不把纯 `_weekly` 候选混入 Path 1。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% CAGR / -31.00% MaxDD / 0.9776 Sharpe / 0.76 Turnover`；`since_2023_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 仍因 Sharpe 与回撤不足不替换。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% CAGR / -11.64% MaxDD / 2.1472 Sharpe / 1.37 Turnover`；四窗口鲁棒候选同步为 `aggr_08_92_prom6__port_weekly_exposure_buffered`，`meanCAGR=43.26% / minCAGR=25.26% / worstMaxDD=-29.23% / meanTurn=0.92`。

## 本轮执行计划（2026-05-09 21:14 CST）

- 本轮继续运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径保持 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 仍限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向；本轮不吸收 A 股 Path 2 的 `90/10 risk50_mom / risk50_ma` 三档择时线。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% CAGR / -31.00% MaxDD / 0.9776 Sharpe / 0.76 Turnover`；`since_2023_01` 的高 CAGR `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 继续因 Sharpe 与回撤不足而不替换。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% CAGR / -11.64% MaxDD / 2.1472 Sharpe / 1.37 Turnover`；四窗口鲁棒候选仍是 `aggr_08_92_prom6`，`meanCAGR=43.81% / minCAGR=22.59% / worstMaxDD=-28.64% / meanTurn=3.22`。

## 本轮执行计划（2026-05-09 18:09 CST）

- 本轮继续运行 `.venv/bin/python scripts/winner_only_pass.py`，快筛口径保持 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 仍限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向；不吸收 A 股 Path 2 的 `90/10 risk50_mom / risk50_ma` 三档择时强点。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% CAGR / -31.00% MaxDD / 0.9776 Sharpe / 0.76 Turnover`；`since_2023_01` 的高 CAGR `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 继续因 Sharpe 与回撤不足而不替换。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% CAGR / -11.64% MaxDD / 2.1472 Sharpe / 1.37 Turnover`；四窗口鲁棒候选仍是 `aggr_08_92_prom6`，`meanCAGR=43.81% / minCAGR=22.59% / worstMaxDD=-28.64% / meanTurn=3.22`。

## 本轮执行计划（2026-05-09 13:04 CST）

- 本轮复跑 `.venv/bin/python scripts/winner_only_pass.py`，固定快筛口径保持 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内；本轮不吸收 A 股 Path 2 的 `90/10 risk50_mom / risk50_ma` 三档择时强点。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% CAGR / -31.00% MaxDD / 0.9776 Sharpe / 0.76 Turnover`；`since_2023_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 虽有 `31.44% CAGR`，但 Sharpe 与回撤不足以替换当前 winner。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% CAGR / -11.64% MaxDD / 2.1472 Sharpe / 1.37 Turnover`；更高 CAGR 的 `aggr_08_92_prom6_cash_off` 换手升至 `5.04` 且 Sharpe 略低，不改写 winner。
- 四窗口鲁棒候选仍是 `aggr_08_92_prom6`，`meanCAGR=43.81% / minCAGR=22.59% / worstMaxDD=-28.64% / meanTurn=3.22`。

## 本轮执行计划（2026-05-09 05:08 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py`，固定快筛口径为 `as_of=2026-05-08 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内；本轮不吸收 A 股 Path 2 的 `90/10 risk50_mom / risk50_ma` 三档择时强点，也不新增候选族。
- 快筛没有清晰窗口 winner 改写：`since_2017_01` 仍为 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`，`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`。
- `since_2020_01` 仍为 `aggr_05_95_prom7__sat_three_stage_buffered`，`27.80% CAGR / -31.00% MaxDD / 0.9776 Sharpe / 0.76 Turnover`；`since_2023_01` 的高 CAGR 候选仍因 Sharpe/回撤不满足替换条件而不改写 winner。
- `since_2025_01` 仍为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`，`97.91% CAGR / -11.64% MaxDD / 2.1472 Sharpe / 1.37 Turnover`；四窗口鲁棒候选仍是 `aggr_08_92_prom6`，`meanCAGR=43.81% / minCAGR=22.59% / worstMaxDD=-28.64% / meanTurn=3.22`。

## 本轮执行计划（2026-05-08 23:27 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py`，随后重跑 winner-only 确认并把 `720` 条 fresh rows 合并回 comparison CSV，再复跑 `.venv/bin/python scripts/update_weighted_winners.py` 与快筛；最终固定 `path1_fast_family` 口径下无剩余 clear improvement。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内；本轮不吸收 A 股 Path 2 的 `risk50_mom / risk50_ma` 三档择时家族，也不新增候选族。
- 窗口 winner 同步后为：`since_2017_01` 仍是 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（`27.25% CAGR / -28.16% MaxDD / 1.1183 Sharpe / 0.80 Turnover`），`since_2020_01` 切到 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.80% / -31.00% / 0.9776 / 0.76`）。
- `since_2023_01` 同步切到 `aggr_08_92_prom6_cash_off__sat_weekly_risk`（`25.37% CAGR / -12.34% MaxDD / 1.0722 Sharpe / 1.02 Turnover`）；`since_2025_01` 同步为 `aggr_10_90_prom6_core_6_1__port_weekly_exposure_buffered`（`97.91% / -11.64% / 2.1472 / 1.37`）。
- 四窗口鲁棒候选同步为 `aggr_08_92_prom6`，`meanCAGR=43.81% / minCAGR=22.59% / worstMaxDD=-28.64% / meanTurn=3.22`；`weekly_exposure_path` 继续保留 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym` 的固定比较顺序。

## 本轮执行计划（2026-05-08 17:24 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py` 做固定快筛，口径仍为 `as_of=2026-05-07 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内；本轮 A 股 Path 2 的 `risk50_mom / risk50_ma` 月频三档择时修正不并入 Path 1。
- 快筛没有清晰窗口 winner 改写：`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD=-25.00%` 继续阻挡替换；`since_2025_01` 最近似候选仍是更高 CAGR 但 Sharpe 略低。
- 复跑 `scripts/update_weighted_winners.py` 后，四窗口 tracked winners 与四窗口鲁棒候选未发生身份漂移；本轮不触发 Path 1 确认回测。
- `weekly_exposure_path` 继续保留 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym` 的固定比较顺序。

## 本轮执行计划（2026-05-08 13:15 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py` 做固定快筛，口径为 `as_of=2026-05-07 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内；本轮 A 股 Path 2 新增的 `90/10 risk50_or` 降单票上限与首月 ramp 控制不并入 Path 1。
- 快筛没有清晰窗口 winner 改写：`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD=-25.00%` 继续阻挡替换；`since_2025_01` 最近似候选仍是更高 CAGR 但 Sharpe 略低。
- 复跑 `scripts/update_weighted_winners.py` 后，四窗口 tracked winners 与四窗口鲁棒候选未发生身份漂移；本轮不触发 Path 1 确认回测。
- `weekly_exposure_path` 继续保留 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym` 的固定比较顺序。

## 本轮执行计划（2026-05-08 07:28 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py` 做固定快筛，口径为 `as_of=2026-05-07 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内；本轮 A 股 Path 2 新增的 `90/10` 与 `95/05` 组合结构候选不并入 Path 1。
- 快筛没有清晰窗口 winner 改写：`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD=-25.00%` 继续阻挡替换；`since_2025_01` 最近似候选仍是更高 CAGR 但 Sharpe 略低。
- 复跑 `scripts/update_weighted_winners.py` 后，四窗口 tracked winners 未发生身份漂移；本轮不触发 Path 1 确认回测。
- `weekly_exposure_path` 继续保留 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym` 的固定比较顺序。

## 本轮执行计划（2026-05-07 23:12 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py` 做固定快筛，口径为 `as_of=2026-05-07 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内；本轮 A 股 Path 2 新增的 `risk30_mom / risk30_ma` 风控触发拆分不并入 Path 1。
- 快筛没有清晰窗口 winner 改写：`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD=-25.00%` 继续阻挡替换；`since_2025_01` 最近似候选仍是高 CAGR 但 Sharpe 略低于当前 winner。
- 复跑 `scripts/update_weighted_winners.py` 后，四窗口 tracked winners 未发生身份漂移；本轮不触发 Path 1 确认回测。
- `weekly_exposure_path` 继续保留 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym` 的固定比较顺序。

## 本轮执行计划（2026-05-07 11:10 CST）

- 本轮先运行 `.venv/bin/python scripts/winner_only_pass.py` 做固定快筛，口径仍为 `as_of=2026-05-06 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内；本轮 A 股 Path 2 新增的 `risk50_or_exit80/exit60` 微批量不并入 Path 1。
- 快筛结果没有清晰窗口 winner 改写：`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD=-25.00%` 继续阻挡替换；`since_2025_01` 最近似候选仍是高 CAGR 但 Sharpe 不足。
- 复跑 `scripts/update_weighted_winners.py` 后，四窗口 tracked winners 未漂移；四窗口鲁棒候选仍为 `aggr_10_90_prom6__port_weekly_exposure_buffered`，`meanCAGR=44.22% / minCAGR=26.01%`。
- 本轮不触发 Path 1 确认回测；继续保持 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym` 的固定比较顺序。

## 本轮执行计划（2026-05-07 05:06 CST）

- 本轮已先运行 `.venv/bin/python scripts/winner_only_pass.py` 做固定快筛，口径仍为 `as_of=2026-05-06 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- Path 1 继续限制在 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants` 五个固定方向内，不吸收本轮 Path 2 的 `promo_liqmom_top15 risk30_exit60` 恢复确认微批量。
- 快筛结果暂无清晰窗口 winner 改写：`since_2020_01` 最近似候选仍受 `MaxDD -25.00%` 阻挡，`since_2025_01` 最近似候选收益更高但 Sharpe 低于当前 winner。
- 复跑 `scripts/update_weighted_winners.py` 后，四窗口 tracked winners 继续保持不变；四窗口鲁棒候选为 `aggr_10_90_prom6__port_weekly_exposure_buffered`，`meanCAGR=44.22% / minCAGR=26.01%`。
- 本轮不触发 Path 1 确认回测；继续保留 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym` 的固定比较顺序。

## 本轮执行计划（2026-05-06 23:15 CST）

- 本轮先发现 comparison CSV 当前只保留少量候选，已用本地 `summary.json` 缓存重建完整 comparison 到 `2747` 行 / `703` 个 base strategies，再运行 `.venv/bin/python scripts/winner_only_pass.py`。
- Path 1 快筛口径恢复为 `base_candidates=24 / total_candidates=168 / evaluated=168`；方向仍限于 `promotion_ramp / satellite_defense / signal_variants / holding_shape / supporting_variants`，不吸收 Path 2 的 `promo_liqmom_top15 risk30_exit*` 候选。
- `since_2023_01` 出现清晰同步改写：winner 从 `aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered` 切到 `aggr_08_92_prom6_cash_off_and__port_weekly_exposure_buffered`，指标为 `26.91% CAGR / -12.55% MaxDD / 1.1251 Sharpe / 0.57 Turnover`。
- `since_2017_01 / since_2020_01 / since_2025_01` winners 未改写；`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD -25.00%` 继续阻挡替换。
- 四窗口鲁棒候选同步为 `aggr_10_90_prom6__port_weekly_exposure_buffered`，`meanCAGR=44.22% / minCAGR=26.01% / worstMaxDD=-31.55% / meanTurn=0.95`。
- 已运行 `scripts/update_weighted_winners.py`、图表、live export 与 public snapshot；公开快照中 A 股数据截止日为 `2026-05-06`，信号/换股生效日继续来自真实月末、周末或双周评估点。

## 本轮执行计划（2026-05-06 11:35 CST）

- 本轮 Path 1 继续严格限制在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不吸收 Path 2 新增的 `promo_liqmom_top15 risk*_or` 风险触发候选。
- 运行 `.venv/bin/python scripts/winner_only_pass.py`，口径仍为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 未改写；`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`），继续受回撤阈值阻挡。
- `since_2025_01` 最近似候选仍是 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe / 1.40 Turnover`），Sharpe 仍低于当前 winner。
- 本轮不触发 Path 1 确认回测；下一轮继续在固定方向内优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`。

## 本轮执行计划（2026-05-06 06:14 CST）

- 本轮 Path 1 仍严格限制在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向，不吸收 Path 2 的 `promo_liqmom_top15 risk30/risk50` 风险节奏微批量。
- 先后运行 `.venv/bin/python scripts/winner_only_pass.py`；重建 comparison 后口径仍为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 未改写；`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`），但不满足回撤约束。
- `since_2025_01` 最近似候选仍是 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe / 1.40 Turnover`），Sharpe 仍略低于当前 winner。
- 本轮不触发 Path 1 确认回测；下一轮继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym` 的稳定性。

## 本轮执行计划（2026-05-06 00:04 CST）

- 本轮 Path 1 继续限制在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不吸收 A 股 Path 2 的 `promo_liqmom_top15` 阈值邻域。
- 先运行 `.venv/bin/python scripts/winner_only_pass.py` 作为固定快筛，保持约 `24-28` 个 base candidates 与完整展开候选预算。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写 Path 1 四窗口 winner 才补确认回测。
- 本轮先后在 Path 2 微批量前后运行 `.venv/bin/python scripts/winner_only_pass.py`；重建 comparison CSV 后复跑输出仍为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 未改写；最近似候选仍是 `since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`）与 `since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`）。
- 本轮不触发 Path 1 确认回测；`weekly_exposure_path` 的 buffered/asym 对照顺序保持不变。

## 本轮补充计划与记录（2026-05-05 18:16 CST）

- 本轮 Path 1 继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不吸收 A 股 Path 2 新增的 `promotion_signal_mode` 微批量。
- 先后运行 `.venv/bin/python scripts/winner_only_pass.py` 两次；重建 comparison CSV 后复跑输出仍为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；最近似候选仍是 `since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`）与 `since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`）。
- `weekly_exposure_path` 继续按固定顺序比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；本轮不触发 Path 1 确认回测。

## 本轮补充计划与记录（2026-05-05 12:14 CST）

- 本轮 Path 1 继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不吸收 A 股 Path 2 新增的 `midcycle_momentum` 微批量。
- 先运行 `.venv/bin/python scripts/winner_only_pass.py`，并在 Path 2 微批量、comparison CSV 重建后复跑；两次输出均为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；最近似候选仍是 `since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`）与 `since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`）。
- `weekly_exposure_path` 继续按固定顺序比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；本轮不触发确认回测。

## 本轮补充计划与记录（2026-05-05 06:14 CST）

- 本轮 Path 1 继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不吸收 A 股 Path 2 新增的高集中确认过滤微批量。
- 先运行 `.venv/bin/python scripts/winner_only_pass.py`，并在 Path 2 微批量、comparison CSV 重建后复跑；两次输出均为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- `weekly_exposure_path` 继续按固定顺序比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；本轮没有 Path 1 四窗口 tracked winner 改写，因此不补确认回测。
- 最近似候选仍是 `since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`）与 `since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`），继续分别受回撤或 Sharpe 条件阻挡。

## 本轮补充计划与记录（2026-05-05 00:03 CST）

- 本轮 Path 1 继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不吸收 A 股 Path 2 的高集中 ramp 微批量。
- 先运行 `.venv/bin/python scripts/winner_only_pass.py` 固定快筛，继续保持 `24` 个 base / `168` 个展开候选；只有四窗口 tracked winner 被明确改写才补确认回测。
- `weekly_exposure_path` 仍优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；若只是同步重跑，不更新 Path 1 winner 结论。
- 运行 `.venv/bin/python scripts/winner_only_pass.py` 并在 Path 2 微批量后复跑，输出仍为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；最近似候选仍是 `since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`）与 `since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`），本轮不触发确认回测。

## 本轮补充计划与记录（2026-05-04 18:07 CST）

- 本轮 Path 1 继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不吸收 A 股 Path 2 的高频单票候选。
- 先运行 `.venv/bin/python scripts/winner_only_pass.py` 固定快筛，继续保持 `24` 个 base / `168` 个展开候选；只有四窗口 tracked winner 被明确改写才补确认回测。
- A 股 Path 2 本轮只测试 `prom1 core_6_1 cap100` 的周频/双周 cadence 对照，结论只服务无约束上限探索。
- 运行 `.venv/bin/python scripts/winner_only_pass.py` 并在 Path 2 微批量后复跑，输出仍为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；最近似候选仍是 `since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`）与 `since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`），本轮不触发确认回测。

## 本轮补充计划与记录（2026-05-04 15:25 CST）

- 本轮 Path 1 继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内；A 股 Path 2 新增的 `industry_trend` 排序候选不并入 Path 1 fast pass。
- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不触发确认回测。
- 最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，继续被回撤阈值挡住；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，但 Sharpe 仍低于当前 winner。

## 本轮补充计划（2026-05-04 06:45 CST）

- 本轮 Path 1 继续限定在既有 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个方向，不新增候选族。
- 先运行 `.venv/bin/python scripts/winner_only_pass.py` 作为固定快筛；若四窗口 tracked winners 未被清晰改写，不补跑确认回测。
- A 股 Path 2 新增的 `core_theme` 排序候选只服务无约束上限探索，不并入 Path 1 fast pass。

### 本轮补充记录（2026-05-04 09:40 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；最近似候选仍是 `since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`）与 `since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`），仍分别受回撤或 Sharpe 条件阻挡。
- A 股 Path 2 新增的 `core_theme` 候选不并入 Path 1，Path 1 本轮不补跑确认回测。

## 本轮执行计划（2026-05-04）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-05-04 03:57 CST）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不补跑确认回测。
- 最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，继续被回撤阈值挡住；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，但 Sharpe 仍低于当前 winner。
- A 股 Path 2 新增的 `prom1 core_3_1 cap100` 微批量不并入 Path 1 fast pass；Path 1 继续保持固定方向与固定快筛预算。

## 本轮执行计划（2026-05-03）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-05-03 00:16 CST；06:11 CST 复核）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不补跑确认回测。
- 最近似候选仍被同一组阈值挡住：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，回撤恶化仍超阈值；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，但 Sharpe 仍低于当前 winner。

### 本轮补充（2026-05-03 12:05 CST）

- 在 A 股 Path 2 新增 `prom1 cap100 risk50/full_risk` 微批量并重建 comparison CSV 到 `2331` 行 / `599` 个 base strategies 后，重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮仍不触发确认回测。
- 最近似候选排序不变：`since_2020_01` 仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD -25.00%` 继续超过替换阈值；`since_2025_01` 仍是 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`，但 Sharpe 低于当前 winner。

### 本轮补充（2026-05-03 18:13 CST）

- 在 A 股 Path 2 新增 `70/30` 与 `60/40` 等权底座的 `prom1 cap100` 微批量并重建 comparison CSV 到 `2363` 行 / `607` 个 base strategies 后，重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不触发确认回测，也不把新增 Path 2 底座结构并入 Path 1 fast pass。
- 最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 继续受 `MaxDD -25.00%` 阻挡；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 仍是高 CAGR 但 Sharpe 不达标。

## 本轮执行计划（2026-05-02）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-05-02）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`run_date=2026-05-02 / data_as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写，因此本轮不补跑确认回测。
- 最近似候选仍被原有阈值挡住：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，收益与 Sharpe 更高但回撤恶化仍超阈值；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，Sharpe 仍低于当前 winner。

### 本轮补充（2026-05-02 06:07 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`，确认 `results/winner_only_pass.json` 的 `as_of` 应按本地市场结果数据截止日记录为 `2026-04-30`，不是自动化运行日。
- 四个 Path 1 tracked winners 仍未改写；本轮不触发确认回测，也不把 A 股 Path 2 新增候选并入 Path 1 fast pass。
- 最近似候选排序保持不变：`since_2020_01` 仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD -25.00%` 继续超过替换阈值；`since_2025_01` 仍是 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`，但 Sharpe 仍低于当前 winner。

### 本轮补充（2026-05-02 12:10 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮仍不补跑确认回测。
- 最近似候选继续受同一组条件阻挡：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，但 Sharpe 低于当前 winner。

### 本轮补充（2026-05-02 18:08 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不补跑确认回测。
- 最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 继续受 `MaxDD -25.00%` 阻挡；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 虽有更高 CAGR，但 Sharpe 仍低于当前 winner。

## 本轮执行计划（2026-05-01）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-05-01）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-05-01 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写，因此本轮不补跑确认回测。
- 最近似候选仍被同一组风险约束挡住：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 达到 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，但回撤恶化仍超过替换阈值；`since_2023_01` 的 `aggr_10_90_hold_4_6__port_weekly_exposure` 达到 `30.93% CAGR`，但 Sharpe 与 MaxDD 仍不合格。
- 本轮新增的 A 股 Path 2 高集中原型不并入 Path 1 候选池；Path 1 继续保持固定方向和固定快筛预算。

### 本轮补充（2026-05-01 06:11 CST）

- 在 A 股 Path 2 微批量并重建 comparison CSV 后，重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-05-01 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 仍未改写；`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD -25.00%` 仍超过替换阈值。
- 本轮 Path 1 不触发确认回测；新增的 A 股 Path 2 晋升 3 只高集中原型继续只服务无约束上限探索，不并入 Path 1。

### 本轮补充（2026-05-01 12:11 CST）

- 再次运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-05-01 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 在 A 股 Path 2 新增 `core_3_1` 高集中原型并重建 comparison CSV 到 `2139` 行 / `551` 个 base strategies 后复跑快筛，四个 Path 1 tracked winners 仍未改写。
- 最近似候选仍未过阈值：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`，回撤恶化仍超过替换条件；本轮不补跑 Path 1 确认回测。

### 本轮补充（2026-05-01 18:14 CST）

- 先发现共享 `results/strategy_comparison_base_method.csv` 只剩 `17` 行，按本地 `summary.json` 缓存重建到 `2139` 行 / `551` 个 base strategies 后运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-05-01 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 初筛一度把 `since_2020_01` 的 `aggr_08_92_prom6__sat_three_stage_buffered` 标为可疑改善；随后补跑当前 tracked winner 与该候选的 `since_2020_01` 确认回测，并再次重建 comparison CSV。
- 同口径复筛后四个 Path 1 tracked winners 未改写：当前 `since_2020_01` winner 同步为 `aggr_10_90_prom6__sat_three_stage_buffered`（`25.99% CAGR / -21.53% MaxDD / 0.9185 Sharpe / 0.66 Turnover`）；`aggr_08_92_prom6__sat_three_stage_buffered` 仅 `26.17% CAGR / -21.78% MaxDD / 0.9205 Sharpe`，Sharpe 改善不足；`aggr_05_95_prom7__sat_three_stage_buffered` 仍受 `-25.00% MaxDD` 阻挡。
- 本轮 Path 1 不新增候选族，也不把 A 股 Path 2 高频原型并入 fast pass。

## 本轮执行计划（2026-04-30）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-04-30）

- 先发现共享 `results/strategy_comparison_base_method.csv` 被压缩到 `73` 行，随后用本地 `summary.json` 缓存重建到 `1477` 行 / `500` 个 base strategies，再重跑 `.venv/bin/python scripts/winner_only_pass.py`。
- 重跑后输出为：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 继续未改写，因此不补跑确认回测。
- 最近似候选仍不满足替换条件：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 达到 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，收益和 Sharpe 更高但回撤恶化超阈值；`since_2023_01` 的 `aggr_10_90_hold_4_6__port_weekly_exposure` 达到 `30.93% CAGR`，但 Sharpe 降到 `0.8987` 且 MaxDD 扩到 `-31.82%`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 达到 `104.59% CAGR`，但 Sharpe 低于当前 tracked winner。

### 本轮补充（2026-04-30 06:35 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`，并在 Path 2 微批量回测后重建完整 comparison CSV 再复跑一次；输出仍为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 均未改写，最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 回撤恶化过大，`since_2023_01` 的 `aggr_10_90_hold_4_6__port_weekly_exposure` Sharpe/MaxDD 不合格，`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` Sharpe 低于当前 winner。
- 本轮 Path 1 不触发确认回测；后续仍保留 `weekly_exposure_path` 中 `buffered / asym` 的固定对照顺序。

### 本轮补充（2026-04-30 12:12 CST）

- 再次运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；最近似候选仍被同一组回撤或 Sharpe 条件挡住，因此本轮不补跑确认回测。
- 本轮新增的 A 股 Path 2 微批量只用于无约束上限探索，不并入 Path 1 候选池；Path 1 仍限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个方向内。

### 本轮补充（2026-04-30 18:16 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 MaxDD 扩到 `-25.00%`，不满足替换阈值。
- 本轮 Path 1 不触发确认回测；新增的 A 股 Path 2 高集中原型仍只服务无约束上限探索。

## 上轮执行计划（2026-04-29）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持约 `24-28` 个 fast-pass base candidates 的预算。
- `weekly_exposure_path` 仍优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-04-29 12:03 CST）

- 先发现共享 `results/strategy_comparison_base_method.csv` 只剩 `73` 行，随后用缓存 `summary.json` 重建到 `1947` 行 / `503` 个 base strategies，再运行 `.venv/bin/python scripts/winner_only_pass.py`。
- 重跑后输出为：`as_of=2026-04-29 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 继续未改写，因此不补跑确认回测；最接近的 `since_2020_01` challenger 是 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`），收益和 Sharpe 更高但回撤恶化超阈值。
- `since_2025_01` 最接近候选仍是 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`），收益更高但 Sharpe 与回撤都不满足替换条件。

### 本轮快筛记录（2026-04-29 18:50 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-29 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 仍未改写，因此不补跑确认回测。
- 最近似候选继续是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 达到 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`，收益和 Sharpe 更高但回撤恶化超阈值；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 达到 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，收益更高但 Sharpe 与回撤不满足替换条件。

## 上轮执行计划（2026-04-28）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持约 `24-28` 个 fast-pass base candidates 的预算。
- `weekly_exposure_path` 仍优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`，只在候选明确改写窗口赢家时补跑确认回测。

### 本轮快筛记录（2026-04-28 00:05 CST）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 未改写；本轮不触发确认回测。
- 最接近但未通过阈值的候选仍集中在 `holding_shape / weekly_exposure_path`：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 把 CAGR 抬到 `27.83%`，但 MaxDD 扩到 `-25.00%`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 把 CAGR 抬到 `104.59%`，但 Sharpe 低于当前 tracked winner。

### 本轮快筛记录（2026-04-28 12:04 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 继续未改写，因此不补跑确认回测。
- 最近似候选仍不是合格晋级：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 提升 CAGR 至 `27.83%`，但 MaxDD 扩到 `-25.00%`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 提升 CAGR 至 `104.59%`，但 Sharpe 降到 `2.2339`，低于当前 tracked winner。

### 本轮快筛记录（2026-04-28 18:29 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 继续未改写，因此不补跑确认回测。
- 最接近但未通过阈值的候选仍集中在 `holding_shape / weekly_exposure_path`：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 达到 `27.83% CAGR`，但 MaxDD 扩到 `-25.00%`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 达到 `104.59% CAGR`，但 Sharpe `2.2339` 低于当前 tracked winner。

## 1. 当前目标

- 路线：`Path 1` 渐进优化
- 主目标：
  - 把 `2017 / 2020 / 2023 / 2025` 四个窗口里的主力版本继续往上推
  - 优先改进 `2020` 和 `2023` 两个窗口
  - 不明显恶化 `Max DD / Sharpe / Turnover`
- 当前研究原则：
  - 尽量不破坏现有 `winner_core` 主线
  - 优先动系统风险层、晋升节奏、卫星仓行为
  - 每次迭代固定试 `5` 个有明确假设的方向
  - 单轮快筛候选预算控制在 `24-28` 个 base candidates

## 2. 当前主线假设

当前 `Path 1` 的核心假设如下：

1. `winner_core` 主线仍然是有效框架，问题不在于“是否保留 winner_core”，而在于“如何更早、更平滑地把强者放大”。
2. 周频系统风险覆盖层如果直接作用于整个组合，通常会伤害收益；但如果只作用于卫星仓，则更有希望改善收益-回撤比。
3. 卫星仓三档风控（`100 / 60 / 30`）优于简单两档，且在进攻主线上配合更少触发次数会进一步改善结果。
4. `cash_off` 线更偏防守，继续叠加太多额外确认逻辑，边际收益有限；更适合保留为防守候选，而不是主攻优化对象。
5. Path 1 的优化应该优先来自：
   - 卫星仓风控
   - 晋升核心后的加仓节奏
   - 月度选股 + 周度仓位调整
   - 触发机制的节奏控制
   而不是频繁改动股票池或彻底换框架。

## 3. 当前默认候选生成

当前 `Path 1` 快速迭代不是扫全部 `winner_core` 变体，而是从显式候选方向组中生成。  
当前默认是 **`5` 个方向组 / `23` 个 fast-pass 变体（对应 `24` 个 base candidates）**（以 `backtest_marketcap_etf.py` 中 `PATH1_FAST_PASS_DIRECTION_GROUPS / PATH1_FAST_PASS_VARIANT_IDS` 为准）；周频 companion 和月度选股/周度仓位调整 companion 会在此基础上自动展开到更大的快筛集合：

1. `promotion_ramp`
   - `aggr_10_90_fast_ramp`
   - `aggr_10_90_prom5`
   - `aggr_10_90_prom6`
   - `aggr_10_90_prom7`
   - `aggr_10_90_prom7_ramp90`
2. `satellite_defense`
   - `aggr_08_92_prom6_cash_off`
   - `aggr_08_92_prom6_cash_off_and`
   - `aggr_10_90_prom6_cash_off`
   - `aggr_10_90_fast_ramp_cash_off`
   - `aggr_10_90_fast_ramp_cash_off_and`
3. `signal_variants`
   - `aggr_08_92_prom6_core_6_1`
   - `aggr_10_90_prom6_core_6_1`
4. `holding_shape`
   - `share_15_85_hold_4_6`
   - `aggr_10_90_hold_4_6`
   - `share_12_88_hold_4_6`
   - `aggr_09_91_prom7`
   - `aggr_08_92_hold_3_6`
   - `aggr_08_92_hold_3_6_ramp90`
   - `aggr_05_95_prom7`
5. `supporting_variants`
   - `aggr_08_92_prom6`
   - `aggr_08_92_prom6_ramp90`
   - `aggr_08_92_prom7`
   - `aggr_08_92_prom7_ramp90`

说明：

- 这组候选是“Path 1 fast pass”的研究入口，不代表全部可用策略。
- 正式确认回测仍然可以扩展到更宽的 `research active family`。
- 如果某一轮出现更优的 companion 版本（例如卫星风控 companion），可以追加进入 fast pass 候选，但应写明加入原因。
- 每轮不要求全部候选都进入完整确认；fast pass 的职责是先筛出每个方向里最值得晋级的 `1-2` 个。
- `2026-04-24` 起，`fast_ramp_cash_off_and / hold_3_6 / hold_3_6_ramp90 / aggr_05_95_prom7` 已正式纳入 `Path 1 fast pass`，用于把固定方向内的 base budget 提升到 `24`，但仍不把 `signal_variants` 重新拉回主攻列表。
- 对 `weekly_exposure_path`，完整确认只允许以下 3 个版本参与：
  - `__port_weekly_exposure`
  - `__port_weekly_exposure_buffered`
  - `__port_weekly_exposure_asym`

## 4. 下一轮优先尝试的方向（每轮固定 5 个）

## 4.1 本轮（2026-04-21）执行清单（限定 5 个方向）

本轮 `Path 1` 研究严格限定在以下 `5` 个方向内（其余方向不主动展开）：

1. **晋升核心后的分阶段加仓节奏（promotion_ramp）**：继续围绕 `ramp90` 与更快晋升/加仓的组合，优先看 `since_2020_01 / since_2023_01` 是否能抬高 `CAGR` 且不明显恶化 `Max DD / Turnover`。
2. **卫星仓防守（satellite_defense）**：只围绕“卫星仓风控 overlay”相关候选（含 `cash_off(_and)` 线），不扩大到全组合周频 overlay。
3. **持仓形态与晋升容量（holding_shape）**：把 `share / prom` 结构性候选作为独立方向，观察结构变化对 `Sharpe / Turnover` 的影响。
4. **月度选股 + 周度仓位调整（weekly_exposure_path）**：月度篮子固定、周内只调总仓位，优先检验它是否能在不明显伤害 `CAGR` 的前提下改善 `Max DD / Sharpe`，并更贴近真实执行节奏。该方向下只比较 `__port_weekly_exposure / __port_weekly_exposure_buffered / __port_weekly_exposure_asym` 三个 companion。
5. **支持性微调（supporting_variants）**：仅保留 `aggr_08_92_prom6(_ramp90)` 作为“更接近主线”的对照与补位候选，避免新增大范围参数扫。

对应的执行约束（本轮继续沿用）：

- 快筛只跑 `scripts/winner_only_pass.py`，候选只来自 `winner_core` 主线 + 显式 fast-pass 变体（含卫星 overlay 与月度选股/周度仓位调整 companion）。
- 只有当候选**明确改写**某个窗口赢家，且指标满足“不明显恶化回撤/换手”的阈值，才考虑补跑必要确认回测。
- 本轮暂不把 `signal_variants` 作为主攻方向（过去多次出现“CAGR 上升但 Sharpe/回撤/换手显著恶化”的形态）。
- `weekly_exposure_path` 的晋级优先级固定为：
  1. `__port_weekly_exposure_buffered`
  2. `__port_weekly_exposure_asym`
  3. `__port_weekly_exposure`
- `weekly_exposure_path` 的最小判定口径固定为：
  - `since_2020_01`
  - `since_2023_01`
  - `Total Return / CAGR / MaxDD / Sharpe / Turnover`
- 当前默认推进结论：
  - `aggr_10_90_prom6` 主线优先继续压回撤
  - `aggr_08_92_prom6_cash_off` 主线优先继续观察 `buffered`

### 本轮已完成的最小对照（2026-04-21）

#### A. `aggr_10_90_prom6`

- `since_2020_01`
  - 原版：`Total Return 291.43% / CAGR 24.04% / MaxDD -21.61% / Sharpe 0.8899 / Turnover 2.88`
  - `__port_weekly_exposure`：`336.49% / 26.20% / -24.36% / 0.9077 / 0.90`
  - `__port_weekly_exposure_buffered`：`339.65% / 26.34% / -23.59% / 0.9103 / 0.86`
  - `__port_weekly_exposure_asym`：`327.60% / 25.79% / -23.87% / 0.9189 / 0.83`
- `since_2023_01`
  - 原版：`Total Return 110.05% / CAGR 24.94% / MaxDD -28.32% / Sharpe 0.8459 / Turnover 2.96`
  - `__port_weekly_exposure`：`122.75% / 27.16% / -32.14% / 0.8391 / 0.99`
  - `__port_weekly_exposure_buffered`：`123.02% / 27.21% / -31.55% / 0.8415 / 0.95`
  - `__port_weekly_exposure_asym`：`116.16% / 26.02% / -31.22% / 0.8430 / 0.88`

结论：

- `weekly_exposure_path` 在该主线上是有效方向；
- `buffered` 当前是默认主攻版本；
- `asym` 作为“快减慢加”备选保留，但下一轮重点应转向继续压回撤。

#### B. `aggr_08_92_prom6_cash_off`

- `since_2020_01`
  - 原版：`Total Return 256.63% / CAGR 22.23% / MaxDD -15.47% / Sharpe 0.9466 / Turnover 2.23`
  - `__port_weekly_exposure`：`255.40% / 22.17% / -14.31% / 0.9632 / 0.54`
  - `__port_weekly_exposure_buffered`：`258.12% / 22.31% / -15.06% / 0.9622 / 0.53`
  - `__port_weekly_exposure_asym`：`253.89% / 22.09% / -14.31% / 0.9614 / 0.54`
- `since_2023_01`
  - 原版：`Total Return 118.80% / CAGR 26.48% / MaxDD -12.34% / Sharpe 1.0938 / Turnover 2.41`
  - `__port_weekly_exposure`：`120.29% / 26.74% / -12.55% / 1.1176 / 0.58`
  - `__port_weekly_exposure_buffered`：`121.32% / 26.91% / -12.55% / 1.1251 / 0.57`
  - `__port_weekly_exposure_asym`：`120.26% / 26.73% / -12.55% / 1.1175 / 0.58`

结论：

- `weekly_exposure_path` 在该防守主线上也成立；
- `buffered` 当前是更稳健的默认候选；
- 下一轮优先保留 `buffered`，其余两个版本仅作为对照。

## 4.0 上轮（2026-04-19）执行清单（限定 5 个方向）

上轮 `Path 1` 研究严格限定在以下 5 个方向内（其余方向不主动展开）：

1. **卫星仓三档风控的非对称确认**：继续围绕 `__sat_three_stage_risk / __sat_three_stage_buffered` 两条线对比，优先看 `since_2020_01 / since_2023_01` 是否能抬高 `CAGR` 同时不明显恶化 `Max DD / Turnover`。
2. **卫星仓三档风控的更少触发次数**：以 `buffered`（双周确认）为主，观察是否能减少无效来回切换并改善 `Sharpe`。
3. **晋升核心后的分阶段加仓节奏**：优先把“分步加仓”（例如 `ramp90`）纳入 fast-pass 候选，观察 `2020/2023` 的收益弹性与回撤代价。
4. **持仓形态与晋升容量微调**：把 `hold_4_6 / prom7 / 15/85` 这一类结构性候选作为独立方向，不再夹带在其他方向里顺手试。
5. **卫星仓专用周频风控 companion 的家族化管理**：仅维护真正有效的卫星 companion（不再扩大到全组合 overlay）。

对应的执行约束：

- 快速筛选只跑 `scripts/winner_only_pass.py`，并且候选只来自 `winner_core` 主线 + 显式 fast-pass 变体（含卫星 companion）。
- 只有当候选**明确改写**某个窗口赢家，且指标满足“不明显恶化回撤/换手”的阈值，才考虑补跑必要确认回测。

### 上轮快筛记录（2026-04-19）

- `scripts/winner_only_pass.py`（Path 1 fast pass）未发现“清晰改写”窗口赢家的候选。
- 补充（2026-04-19 20:50）：重跑 fast pass，窗口赢家结论不变；最接近改写的仍集中在 `since_2023_01: aggr_10_90_fast_ramp_cash_off`（收益/回撤更好但换手显著更高）。
- 近似候选（但未通过回撤/换手阈值）：
  - `since_2023_01`：`aggr_10_90_fast_ramp_cash_off` 小幅抬高 `CAGR/Sharpe` 且 `Max DD` 更好，但 `Turnover` 增幅过大。
  - `since_2020_01`：`aggr_08_92_prom6_ramp90__sat_three_stage_buffered` 小幅抬高 `CAGR`，但 `Sharpe` 改善不足且 `Max DD` 略差（未满足阈值）。
  - `since_2017_01`：`aggr_08_92_prom6_cash_off_and` 抬高 `CAGR/Sharpe`，但 `Max DD` 明显更差。

### A. 卫星仓三档风控的非对称确认

假设：

- 风险恶化时快减仓
- 风险修复时慢加回

目标：

- 保持 `2020 / 2023` 收益不掉队
- 进一步降低不必要的卫星仓来回切换

预期：

- 更有希望继续提升 `Sharpe`
- 有机会在不牺牲 `CAGR` 的情况下小幅改善 `Max DD`

### B. 卫星仓三档风控的更少触发次数

假设：

- 当前三档已经有效，但仍可能有少量无效来回切换

目标：

- 在 `aggr_10_90_prom6` 主线上继续降低触发次数
- 优先观察 `2023` 窗口是否还能继续抬高

预期：

- 进攻主线受益更明显
- `cash_off` 线可能边际改善有限

### C. 晋升核心后的分阶段加仓节奏

假设：

- 现在的晋升核心有效，但仍可能不够快或不够重

目标：

- 在不改选股框架的前提下，优化胜出者被放大的节奏

预期：

- 主要改善 `2020 / 2023`
- 风险是换手和回撤回升，需要严格约束

### D. 卫星仓专用周频风控 companion 的家族化管理

假设：

- companion 版本已经成为有效增强项

目标：

- 把真正有效的 companion 固定纳入 Path 1 研究候选
- 把无效 companion 移回 archive-like 状态

预期：

- 提升研究效率
- 减少无意义的候选扫描

## 4.1 本轮（2026-04-20）执行清单（限定 5 个方向）

本轮 `Path 1` 研究严格限定在以下 `5` 个方向内（与 fast-pass 方向组一致，不额外扩张）：

1. **晋升核心后的分阶段加仓节奏（promotion_ramp）**：优先观察 `since_2020_01 / since_2023_01` 的收益弹性与回撤代价。
2. **卫星仓防守线（satellite_defense）**：优先看 `cash_off` / `cash_off_and` / `fast_ramp_cash_off` 是否能改善 `2023` 的收益-回撤比并控制换手。
3. **信号变体（signal_variants）**：仅在不明显恶化回撤/换手的前提下，观察 `core_6_1` 在 `2020/2023` 的边际收益。
4. **持仓形态（holding_shape）**：把 `hold_4_6 / prom7` 作为结构性候选独立观察，避免夹带在其他方向里顺手试。
5. **支撑性变体（supporting_variants）**：仅保留 `prom6` 与 `prom6_ramp90` 两个支撑线，用于对照“加仓节奏”是否真的带来持续改进。

对应执行约束（本轮继续沿用）：

- 快速筛选只跑 `scripts/winner_only_pass.py`，候选只来自 `winner_core` 主线 + 显式 fast-pass 变体（含卫星 overlay 后缀）。
- 只有当候选**明确改写**某个窗口赢家，且指标满足“不明显恶化回撤/换手”的阈值，才考虑补跑必要确认回测。

### 本轮快筛记录（2026-04-20）

- `.venv/bin/python scripts/winner_only_pass.py`（`as_of=2026-04-20`）未发现“清晰改写”窗口赢家的候选。
- 补充（2026-04-20 13:21）：重跑 `scripts/winner_only_pass.py`，结论不变（`evaluated=26`）。
- 补充（2026-04-20 18:54）：再次重跑 `scripts/winner_only_pass.py`，结论不变（`base_candidates=13 / total_candidates=52 / evaluated=26`）。
- 补充（2026-04-20 20:23）：运行 `scripts/winner_only_pass.py`，结论不变（`base_candidates=13 / total_candidates=52 / evaluated=26`）。
- 补充（2026-04-21 10:17）：先重建 `strategy_comparison_base_method.csv`（覆盖 `since_2017_01/2020_01/2023_01`）后运行 `scripts/winner_only_pass.py`，`as_of=2026-04-21`；仍未发现“清晰改写”窗口赢家的候选。
- 补充（2026-04-21 12:13）：运行 `scripts/winner_only_pass.py`，结论不变（`base_candidates=13 / total_candidates=52 / evaluated=26`）。
- 补充（2026-04-21 14:18）：运行 `scripts/winner_only_pass.py --scan-prefix core_explore_80_20_total_mv_winner_core`，结论不变（`base_candidates=66 / evaluated=47`）。
- 补充（2026-04-21 16:36）：运行 `scripts/winner_only_pass.py`，结论不变（`base_candidates=13 / total_candidates=91 / evaluated=26`）。
- 补充（2026-04-21 17:57）：运行 `scripts/winner_only_pass.py`，结论不变（`base_candidates=20 / total_candidates=140 / evaluated=34`）。
- 扫描范围（fast pass + 卫星/组合 overlay）：`base_candidates=20 / total_candidates=140 / evaluated=34`。
- 当前阈值（guardrails）：`minCAGR=+0.10%`、`minSharpe=+0.005`、`MaxDD` 允许恶化 `<=0.50%`、`Turnover` 允许上升 `<=+0.15`。
- 近似候选（但未通过回撤/换手/Sharpe 阈值）：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__sat_three_stage_buffered`（ΔCAGR `+0.18%`、ΔSharpe `+0.0031`，Sharpe 改善不足且 MaxDD 略差）。
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1`（CAGR 更高但 Sharpe 更低，且回撤/换手显著恶化）。
  - `since_2017_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and`（CAGR/Sharpe 更高但回撤与换手恶化过大）。

## 5. 已淘汰或暂缓的方向

### 5.1 全组合周频 overlay

结论：

- 已验证为明显不优，暂不并入主线。

原因：

- 普遍出现收益下降
- 或回撤恶化
- 或收益与夏普都不占优

当前处理：

- 仅保留代码实验痕迹，默认不进入主线候选

### 5.2 纯核心集中策略（`pure_core_growth`）

结论：

- 已确认不适合作为当前主攻方向。

原因：

- 高集中放大了错误信号
- 在多个窗口里明显跑输主线
- 更像“放大噪音”，不是“更早抓住核心”

当前处理：

- 保留历史结果，不再进入 active family

### 5.3 对 `cash_off` 线继续叠加过多确认机制

结论：

- 暂缓。

原因：

- 边际改进很小
- 更适合作为防守备选，不是主攻收益突破的最优对象

## 6. 本轮执行规范

每次自动/手动 Path 1 迭代，应尽量遵守：

1. 先从 `Path 1 fast pass` 候选开始。
2. 每轮尽量只试 `3-5` 个方向，不做无差别全扫。
3. 单轮快筛候选数控制在 `8-12` 个；完整确认只允许少数晋级候选进入。
4. 每个方向必须能回答：
   - 当前假设是什么？
   - 预期改善哪一项指标？
   - 为什么值得试？
5. 如果某方向连续多轮没有进入任何窗口最优或接近最优，应写入“淘汰/暂缓”。
6. 若出现新的有效 companion 或新主线变体，应补充进本文档。

## 7. 维护说明

本文档用于研究规划，不用于自动写死最新回测数字。  
最新赢家和指标仍以：

- `README.md` 顶部自动区块
- `HISTORY.md`
- `results/weighted_track_winners.json`

为准。

## 8. 本轮补充（2026-04-21 18:24）

- 重跑 `scripts/winner_only_pass.py`（Path 1 fast-pass）：未发现“清晰改写窗口赢家”的候选（主要问题仍集中在 `MaxDD/Turnover` 约束未通过）。

## 9. 本轮补充（2026-04-21 20:18）

- 重跑 `scripts/winner_only_pass.py`（Path 1 fast-pass）：结论不变，未发现满足阈值的 `clear improvement`。

## 10. 本轮补充（2026-04-21 22:20）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`（Path 1 fast-pass）：`as_of=2026-04-21 base=20 total=140 eval=34`；四窗口赢家不变，未出现满足阈值的 `clear improvement`。

## 11. 本轮补充（2026-04-22）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`（Path 1 fast-pass）：`as_of=2026-04-22 base=20 total=140 eval=34`；四窗口赢家继续不变，未出现满足阈值的 `clear improvement`。
- `since_2020_01` 最接近改写的仍是 `aggr_08_92_prom6__sat_three_stage_buffered`：`CAGR 25.33% / Sharpe 0.9238 / MaxDD -21.83% / Turn 0.67`，相对当前 `aggr_10_90_prom6__sat_three_stage_buffered` 只有很小收益优势，但 `MaxDD` 略差，未通过阈值。
- `since_2023_01` 继续最值得保留的近似候选是 `aggr_10_90_fast_ramp_cash_off`：`CAGR 27.06% / Sharpe 1.1488 / MaxDD -9.90%`，但 `Turnover 2.37` 仍明显高于当前赢家 `0.96`，问题仍是换手。
- `since_2017_01` 的 `aggr_08_92_prom6_cash_off_and` 依旧表现为“收益/Sharpe 更高但回撤与换手显著恶化”的形态，因此下一轮不应把 `cash_off_and` 扩成主攻方向。
- 下一轮默认继续只压 `promotion_ramp / satellite_defense / weekly_exposure_path` 三个方向；`signal_variants` 仍只保留观察，不回到主攻列表。
- 本次再次用 `AIINVESTOR_FORCE_OFFLINE=1` 重跑后，`since_2023_01` 的 raw-CAGR 前两名仍是 `aggr_08_92_prom6_core_6_1 / aggr_10_90_prom6_core_6_1`，但两者的 `Sharpe / MaxDD / Turnover` 都明显差于当前赢家；因此真正保留为下一轮 sidecar challenger 的仍应是 `aggr_10_90_fast_ramp_cash_off`，而不是把 `signal_variants` 重新拉回主攻清单。
- `2026-04-22 06:27 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出与上述一致，四窗口仍无 `clear improvement`；因此本轮不补任何 A 股 Path 1 确认回测。
- 在新增 `Path 2` 原型并重建 `results/strategy_comparison_base_method.csv` 后，再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-22 base=20 total=140 eval=34`，说明 `Path 1` 的近似 challenger 顺位没有被旁路线干扰。
- 当前最接近改写 `since_2020_01` 的仍是 `aggr_08_92_prom6__sat_three_stage_buffered`，最值得保留的 `since_2023_01` sidecar challenger 仍是 `aggr_10_90_fast_ramp_cash_off`；因此本轮结束时 `Path 1` 继续只保留快筛记录，不新增确认回测。
- 当日后续先用缓存重建了 `results/strategy_comparison_base_method.csv`（`427` 行 / `154` 个 base strategies），再运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：结论仍不变，说明此前被局部回测覆盖过的 comparison CSV 已恢复到可用基线。
- 以这次重建后的完整 comparison CSV 为准，`since_2020_01` 当前赢家是 `aggr_10_90_prom6__sat_three_stage_buffered`（`25.27% CAGR / 0.9222 Sharpe / -21.59% MaxDD / 0.67 Turn`）；最接近挑战者 `aggr_08_92_prom6__sat_three_stage_buffered` 只做到 `25.46% / 0.9253 / -21.83% / 0.66`，仍因 `Sharpe` 改善不足且 `MaxDD` 略差而未过阈值，所以本轮继续不补确认回测。
- `2026-04-22 14:30 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-22 base=20 total=140 eval=34`，四窗口 tracked winner 继续不变。
- 本次重跑没有改变近似 challenger 的排序判断：`since_2020_01` 仍应只保留 `aggr_08_92_prom6__sat_three_stage_buffered` 作为最接近挑战者；`since_2023_01` 虽然 raw-CAGR 最高仍来自 `core_6_1` 线，但真正值得保留的 sidecar challenger 仍是 `aggr_10_90_fast_ramp_cash_off`，问题继续集中在 `Turnover 2.37` 过高。
- 因此下一轮 `Path 1` 继续严格限定在 `promotion_ramp / satellite_defense / weekly_exposure_path` 三个方向内，不补确认回测，也不把 `signal_variants` 拉回主攻列表。

## 12. 本轮补充（2026-04-22 23:27 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-22 base=20 total=140 eval=34`，四窗口赢家继续不变。
- `since_2020_01` 当前最接近挑战者仍是 `aggr_08_92_prom6__sat_three_stage_buffered`：`25.46% CAGR / 0.9253 Sharpe / -21.83% MaxDD / 0.66 Turn`；相对当前 tracked winner 只有很小收益优势，但 `MaxDD` 略差，仍不补确认回测。
- `since_2023_01` 真正值得保留的 sidecar challenger 仍是 `aggr_10_90_fast_ramp_cash_off`：`27.06% CAGR / 1.1488 Sharpe / -9.90% MaxDD / 2.37 Turn`；`core_6_1` 两条线虽然 raw CAGR 更高，但仍明显恶化 `Sharpe / MaxDD / Turnover`，不回到主攻列表。
- 下一轮继续只在 `promotion_ramp / satellite_defense / weekly_exposure_path` 三个方向内推进；`signal_variants` 继续只保留观察，不追加新 family，也不补 A 股 Path 1 确认回测。

## 13. 本轮补充（2026-04-23 01:32 CST）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-23 base=20 total=140 eval=140`；本轮首次在 `Path 1 fast-pass family` 内出现 3 个明确改写窗口赢家的候选。
- 当前 Path 1 tracked winners 已同步为：
  - `since_2017_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（`24.50% CAGR / 1.1638 Sharpe / -10.65% MaxDD / 0.62 Turn`）
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered`（`25.78% CAGR / 0.9271 Sharpe / -21.59% MaxDD / 0.67 Turn`，本轮不变）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（`26.91% CAGR / 1.1251 Sharpe / -12.55% MaxDD / 0.57 Turn`）
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1__port_weekly_exposure_asym`（`103.32% CAGR / 2.3086 Sharpe / -9.54% MaxDD / 1.39 Turn`）
- 本轮同时修正了 `scripts/update_weighted_winners.py` 的 Path 1 口径：`tracked winner` 同步现在会纳入 `weekly_exposure_path` 允许的 `__port_weekly_exposure / __port_weekly_exposure_buffered / __port_weekly_exposure_asym` 三个 companion，但仍只限于 `PATH1_FAST_PASS_VARIANT_IDS`，避免把 Path 2 的高集中原型误并入 Path 1。
- 本轮没有再补额外确认回测：因为上述 3 个晋级候选在当前 `results/strategy_comparison_base_method.csv` 中已经具备完整四窗口结果；需要补的不是回测本身，而是把 README / HISTORY / tracked winner 数据与对比图同步到正确口径。
- 当前四窗口鲁棒候选更新为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（`meanCAGR 47.55% / minCAGR 27.01%`）。下一轮 `Path 1` 继续只围绕两个已证实有效的周度仓位 companion 推进：
  - `aggr_08_92_prom6_cash_off + __port_weekly_exposure_buffered`
  - `aggr_08_92_prom6_core_6_1 + __port_weekly_exposure_asym`
  不重新打开非 fast-pass family。

## 14. 本轮补充（2026-04-23 03:33 CST）

- 本轮先补齐了 `Path 2` 计划里已声明但未实际生成的 4 个候选变体，并用离线缓存补跑后重建了 `results/strategy_comparison_base_method.csv`（`1744` 行 / `466` 个 base strategies）；随后再次运行 `./.venv/bin/python scripts/winner_only_pass.py`，输出仍为 `as_of=2026-04-23 base=20 total=140 eval=140`，四窗口 tracked winners 继续不变。
- `since_2020_01` 当前最接近过线的仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure_buffered`：`27.59% CAGR / 0.9338 Sharpe / -23.01% MaxDD / 0.87 Turn`。它相对当前 winner 确实提高了 `CAGR / Sharpe`，但 `MaxDD` 与 `Turnover` 都明显超出 `clear improvement` 阈值，因此本轮继续不补确认回测。
- `since_2023_01` 最接近挑战者仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`：`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`；问题仍然不是收益不够，而是回撤和风险调整后收益明显差于当前 tracked winner。
- 结论不变：`Path 1` 下一轮继续只保留 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path` 里的快筛观察，不新增确认回测，也不把 `signal_variants` 拉回主攻列表。

## 15. 本轮补充（2026-04-23 05:29 CST）

- 再次运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-23 family=path1_fast_family base_candidates=20 total_candidates=140 evaluated=140`，四窗口 tracked winners 与 `robust_candidate` 继续完全不变。
- `since_2020_01` 当前最接近阈值的仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure_buffered`（`27.59% CAGR / 0.9338 Sharpe / -23.01% MaxDD / 0.87 Turn`）；`since_2023_01` 最接近挑战者仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）。两者都仍卡在 `MaxDD / Turnover` 约束，不补确认回测。
- 本轮随后执行 `./.venv/bin/python scripts/update_weighted_winners.py` 与 `./.venv/bin/python scripts/generate_strategy_comparison_chart.py`：`README / HISTORY / results/weighted_track_winners.json` 没有新增漂移，但 A 股对比图与 tracked-winner 汇总图按当前基线重绘后发生了实际 binary diff，因此本轮允许作为 `sync-only` artifact refresh 提交。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path` 四个既定方向内推进，不新增 fast-pass family，也不重新打开 `signal_variants`。

## 16. 本轮补充（2026-04-23 17:57 CST）

- 再次运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-23 family=path1_fast_family base_candidates=20 total_candidates=140 evaluated=140`，四窗口 tracked winners 与 `robust_candidate` 继续完全不变，没有新的 `clear improvement`。
- `since_2020_01` 最接近阈值的仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure_buffered`（`27.59% CAGR / 0.9338 Sharpe / -23.01% MaxDD / 0.87 Turn`）；`since_2023_01` 最接近挑战者仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）。两者都仍卡在 `MaxDD / Turnover` 约束，因此本轮继续不补确认回测。
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py` 与 `./.venv/bin/python scripts/generate_strategy_comparison_chart.py`：A 股 tracked winner ID 本身没有变化，但 `README / HISTORY / results/weighted_track_winners.json` 与对比图已按 `2026-04-23` 最新 close 刷新到当前口径，因此本轮继续允许作为 `sync-only` artifact refresh 提交。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path` 四个既定方向内推进，不新增 fast-pass family，也不重新打开 `signal_variants`。

## 17. 本轮补充（2026-04-24）

- 按自动化规则先把独立 worktree 对齐到主工作树 `main`，随后以 continuity 基线重建 `results/weighted_track_winners.json` 并运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-24 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`。
- 本轮 `Path 1 fast pass` 已正式纳入 `aggr_10_90_fast_ramp_cash_off_and`、`aggr_08_92_hold_3_6`、`aggr_08_92_hold_3_6_ramp90`、`aggr_05_95_prom7`，固定五方向的 base budget 提升到 `24`；但在保留既有 tracked-winner continuity 口径后，四窗口 tracked winners 与 `robust_candidate` 继续保持不变。
- 当前最强但未过 `clear improvement` 阈值的挑战者是：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`28.30% CAGR / 1.0296 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` 具备更高 raw CAGR，但分别因为 `Sharpe / MaxDD` 不过线而不晋级。
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py`、`./.venv/bin/python scripts/generate_strategy_comparison_chart.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`README / HISTORY / results/weighted_track_winners.json / results/live` 已同步到 `2026-04-24` 口径，但结论仍是“扩容后没有新的 clear winner”。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 这五个既定方向内推进；`signal_variants` 仍只保留观察，不补确认回测。

## 18. 本轮补充（2026-04-25）

- 本轮先按自动化规则把独立 worktree 对齐到主工作树 `main`，随后用缓存重建 `results/strategy_comparison_base_method.csv`（`1899` 行 / `491` 个 base strategies）；重建后的 A 股真实 `sample_end` 已恢复到 `2026-04-24`，`README / HISTORY / results/weighted_track_winners.json` 也已同步到同一口径。
- 本轮没有新增 `Path 1` winner，但在尝试扩扫 A 股 active family 时踩出了一个真实的 Path 2 边缘 bug：极端高集中候选在周频 overlay 调仓里会把 `NaN` code 混进持仓序列，进而在 `compute_rebalance_trades()` 的持仓聚合处触发崩溃。当前已在 `backtest_marketcap_etf.py` 中加上“丢弃空索引 + 合并重复 code”的最小修复，后续 `Path 1 / Path 2` 的激进候选都可以继续跑，不会因为脏索引中断。
- 在这份重建后的完整 comparison CSV 上再次运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-24 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`；四窗口 tracked winners 与 `robust_candidate` 继续完全不变，没有新的 `clear improvement`。
- 当前仍最值得观察但未过阈值的挑战者没有变化：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_ramp90__port_weekly_exposure_buffered` 仍具更高 raw CAGR，但继续因为 `Sharpe / MaxDD` 不过线而不晋级。
- 本轮允许作为 `sync-only` 提交的原因，不是出现了新 winner，而是：
  - A 股 comparison CSV 已从旧的局部口径恢复到完整口径；
  - `README / HISTORY / results/weighted_track_winners.json / results/live` 已按真实 `sample_end=2026-04-24` 重新同步；
  - `Path 2` 高集中候选会炸的持仓索引问题已在回测内核修掉。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍固定优先 `buffered > asym > base`，`signal_variants` 不重新打开。

## 19. 本轮补充（2026-04-26）

- 本轮先按自动化规则重新检查基线：`git fetch origin` 因沙箱网络限制失败，而当前 worktree 已知 `origin/main` 不是主工作树 `main` 的后继，因此改为以本地主工作树 `main`（`bb3a7d7`）作为基线，并在独立 worktree 中对齐到该提交。
- 随后运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-26 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`，四窗口 tracked winners 与 `robust_candidate` 继续完全不变，没有新的 `clear improvement`。
- 当前仍最接近阈值、但没有晋级确认回测资格的挑战者是：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` 仍具更高 raw CAGR，但继续因为 `Sharpe / MaxDD` 不过线而不晋级。
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py`、`./.venv/bin/python scripts/generate_strategy_comparison_chart.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：A 股 tracked winners、README 自动区块、对比图和 `results/live` 已同步到当前 `as_of=2026-04-26` 口径，但结论仍是“没有新的 Path 1 winner”。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍固定优先 `buffered > asym > base`，`signal_variants` 继续只保留观察。

## 20. 本轮补充（2026-04-27）

- 本轮按自动化基线规则重新检查后，`git -C /Users/valselee/my-code/aiinvestor fetch origin main` 实际成功；最新 `origin/main` 位于 `fd4b214`，领先于本地主工作树 `main`（`39cf735`），因此本轮直接以该最新远端提交作为 publish baseline，并在独立 worktree 上按该基线重放研究。
- 随后运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-24 family=path1_fast_family base_candidates=24 total_candidates=168`，四窗口 tracked winners 与 `robust_candidate` 继续完全不变，没有新的 `clear improvement`。
- 当前最接近阈值但仍不补确认回测的挑战者是：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` 仍具更高 raw CAGR，但继续因为 `Sharpe / MaxDD` 不过线而不晋级。
- 为了恢复 `results/live` 的依赖，这轮只额外补跑了 tracked winners 与导出所需 sidecar summaries；因为没有任何候选达到 `clear improvement`，所以没有追加新的 `Path 1` 确认回测。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍固定优先 `buffered > asym > base`，并继续优先比较 `buffered` 与 `asym` 两条现役分支。

## 21. 本轮补充（2026-04-27 09:08 CST）

- 本轮按自动化基线规则重新检查后，`git fetch origin` 因沙箱网络限制失败；但当前 worktree 已知 `origin/main`（`5a87b29`）已验证是本地主工作树 `main`（`39cf735`）的后继，因此本轮直接以已知 `origin/main` 作为 publish baseline，并在独立 worktree 中对齐到该提交。
- 随后运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-27 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`，四窗口 tracked winners 继续完全不变，仍未出现满足阈值的 `clear improvement`。
- 当前最接近阈值、但仍不补确认回测的挑战者依旧集中在既定五方向内：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` 仍具更高 raw CAGR，但继续因为 `Sharpe / MaxDD` 不过线而不晋级。
- 这轮真正发生漂移的是 tracked payload 而不是 fast pass 胜负：`results/weighted_track_winners.json` 的 `robust_candidate` 现已同步为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（`meanCAGR 47.28% / minCAGR 25.91%`），替代了此前文档里残留的 `ramp90` 口径；因此本轮属于有效的 `sync-only` 刷新。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍固定优先 `buffered > asym > base`，不重新打开 `signal_variants`。

## 22. 本轮补充（2026-04-27 18:09 CST）

- 本轮在主工作树 `main` 上重新检查基线：工作树起始干净，`git fetch origin` 因 SSH 网络限制失败，因此按自动化规则继续基于本地 `main`（`40d124d`）运行；本轮没有触碰策略代码。
- 运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-27 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`，固定五方向候选预算维持在 `24` 个 base candidates。
- 四窗口 tracked winners 继续没有 clear improvement。当前最接近但未过阈值的候选是：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`），收益与 Sharpe 更好，但回撤从当前 winner 的 `-21.59%` 加深到 `-25.00%`，不补确认回测。
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`），仍是收益更高但回撤/风险调整收益明显不合格。
  - `since_2017_01 / since_2025_01`：`aggr_08_92_prom6_ramp90__port_weekly_exposure_buffered` 系列具备更高 raw CAGR，但继续因为 Sharpe 或 MaxDD 不过线而不晋级。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍优先比较 `buffered` 与 `asym`，不重新打开额外信号族。
## 本轮执行计划（2026-06-01 16:23 CST）

- 上一轮候选/结果摘要：上一轮留下的 `holding_shape` 候选为 `share_06_94_hold_2_8_ramp75_cost_guard`，目标是继续压低 `share_06_94_hold_2_8` 的回撤与加仓节奏；本轮开局 guard 为 `pass`，随后新增注册后补齐该候选五窗口覆盖。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__share_06_94_hold_2_8_ramp75_cost_guard`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_06_94_hold_2_8_ramp75_cost_guard`。
- 五窗口结果：CAGR 为 `21.03% / 22.36% / 33.32% / 100.90% / 109.61%`，最大回撤为 `-19.23% / -19.42% / -23.21% / -11.47% / -11.67%`，换手为 `2.71x / 2.98x / 3.06x / 4.53x / 6.29x`。它改善了 holding-shape 的短窗弹性，但没有改写 Path 1 window winner 或 robust candidate。
- `winner_only_pass.py` 本轮提示 `since_2020_only` 存在 fast-pass clear improvement：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 为当前 fast-pass 最优，但 `update_weighted_winners.py` 后官方 `since_2020_01` 仍保持 `core_explore_80_20_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95_dd_guard50`，需要下一轮继续核对 fast-pass 与正式 promotion score 的差异。
- core_multifactor 子段巡检：本轮读取代码后实际覆盖为 `37` 个 core_multifactor variants，最终 guard 没有 core_multifactor 缺口；本轮没有新增多因子实验，因为预算优先用于 guard 补齐、holding_shape、Path 2/3/4 与 HK 三路候选。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> core_multifactor_coverage`。下一轮第一候选建议实现 `aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`，用五窗口 `--only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm` 先补 80/20 total_mv；若 fast-pass 仍提示 `sat_three_stage_buffered_cost_guard_risk20_reconfirm`，同步复核它与官方 promotion score 的排序差异。

## 本轮执行计划（2026-06-02 22:30 CST）

- 上一轮候选/结果摘要：上一轮要求补 `core_multifactor_coverage`，本轮开局 guard 曾提示 `ashare_path1_core_multifactor` 缺 `quality_defense_cashguard_reconfirm` 的 80/20 total_mv 窗口覆盖；按 blocking rerun command 优先补齐，没有替换成全量回测。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm`。
- 五窗口结果：CAGR 为 `17.00% / 12.04% / 15.93% / 68.08% / 99.12%`，最大回撤为 `-25.62% / -29.05% / -16.91% / -15.38% / -4.62%`，换手为 `2.86x / 3.38x / 3.71x / 5.14x / 5.92x`。它修复了 core_multifactor 覆盖缺口，但 2020/2023 明显弱于 Path 1 现有 winner 与 robust，没有改变 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段巡检：本轮读取代码后实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 为 `40` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 40/40 complete`，`ashare_path1_fast_family 95/95 complete`。`winner_only_pass.py` 仍以退出码 `2` 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 对 `since_2020_only` 有 fast-pass clear improvement；`update_weighted_winners.py` 后官方 Path 1 winner/robust 未采纳该 fast-pass。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> signal_quality`。下一轮第一候选建议在既有 `signal_variants` 内实现 `aggr_08_92_prom6_core_6_1_signal_quality_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1_signal_quality_reconfirm`；若下一轮 guard 再次指向 core_multifactor，先以代码实际 direction group 为准补缺口。

## 本轮执行计划（2026-06-03 12:10 CST）

- 上一轮候选/结果摘要：上一轮 core `quality_defense_cashguard_reconfirm` 只补齐多因子覆盖，2020/2023 明显弱。本轮按开局 `signal_quality` 与 core_multifactor 覆盖要求新增 `quality_lowvol_industry_cost_guard_reconfirm`，检查质量低波+行业强度能否比纯现金防守更稳。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm`。
- 五窗口结果：CAGR 为 `15.38% / 17.27% / 28.43% / 64.07% / 98.06%`，最大回撤为 `-25.53% / -22.66% / -17.98% / -14.09% / -4.62%`，换手为 `2.79x / 3.16x / 3.21x / 5.26x / 5.91x`。它比上一轮 core 的 2020/2023 更好，但仍未改写 Path 1 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 已扩为 `41` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 41/41 complete`、`ashare_path1_fast_family 96/96 complete`。`winner_only_pass.py` 仍提示旧 `risk20_reconfirm` 是 `since_2020_only` fast-pass clear improvement，`update_weighted_winners.py` 后官方 Path 1 未采纳。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> satellite_risk_cost`。下一轮第一候选建议回到 satellite defense 成本/风险线：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`。

## 本轮执行计划（2026-06-03 10:35 CST）

- 上一轮候选/结果摘要：上一轮建议回到 satellite risk/cost，但本轮开局 guard 实际把 Path 1 rotation 指到 `holding_shape`；因此先在 `share_12/14` 一带测试更温和的 `2+8` 分步加仓，同时继续巡检 core_multifactor。首次未锁 `--end-date` 的 Path 4 补跑触发本地 A股缓存只到 `2026-06-02` 的 stale guard，随后所有 A股增量命令显式使用 `--end-date 2026-06-02`。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__share_14_86_hold_2_8_ramp75_cost_guard`。实际合并增量命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_14_86_hold_2_8_ramp75_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`。
- 五窗口结果：CAGR 为 `20.50% / 21.69% / 31.58% / 87.76% / 78.24%`，最大回撤为 `-18.29% / -18.18% / -23.54% / -10.83% / -11.94%`，换手为 `2.67x / 2.96x / 2.96x / 4.38x / 5.37x`。它改善 holding-shape 的回撤稳定性，但收益不足以改写 Path 1 window winner 或 robust candidate。
- core_multifactor 子段巡检：本轮读取代码后实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 为 `41` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 41/41 complete`、`ashare_path1_fast_family 97/97 complete`。本轮没有新增 core_multifactor 实验；`winner_only_pass.py` 仍以 exit `2` 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 是 `since_2020_only` fast-pass clear improvement，但 `update_weighted_winners.py` 后官方 Path 1 winner/robust 未采纳。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> core_multifactor_coverage`。下一轮第一候选建议新增 `aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`，先跑 80/20 total_mv 五窗口；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm`。

## 本轮执行计划（2026-06-04 04:18 CST）

- 上一轮候选/结果摘要：上一轮要求补 core multifactor 覆盖；本轮实际新增 `quality_profitability_industry_defense_reconfirm`，把质量/盈利权重提高，同时保留行业强度和三阶段防守，目标是检查 `signal_quality` 下的多因子防守能否改善 2020/2023。
- 本轮候选 ID：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm`。实际 A股合并增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68,core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68,core_explore_90_10_total_mv_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk20_cap12_exit68`。
- 五窗口结果：CAGR 为 `15.19% / 14.10% / 28.78% / 57.21% / 57.21%`，最大回撤为 `-28.73% / -30.34% / -16.78% / -15.39% / -4.62%`，换手为 `2.72x / 3.02x / 3.14x / 5.04x / 5.48x`。2023 与 2026 风险调整收益可用，但 2017/2020 收益不足，未改变 Path 1 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 已扩为 `42` 个 variants；最终 guard 显示 `ashare_path1_core_multifactor 42/42 complete`、`ashare_path1_fast_family 99/99 complete`。`winner_only_pass.py` 仍以 exit `2` 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 是 `since_2020_only` fast-pass clear improvement，但 `update_weighted_winners.py` 后官方 Path 1 未采纳。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> satellite_risk_cost`。下一轮不要继续只做质量盈利防守，第一候选建议回到 satellite defense 成本/风险线：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk12_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk12_reconfirm`。

## 本轮执行计划（2026-06-08 06:05 CST）

- 上一轮候选/结果摘要：上一轮 Path 1 core multifactor `quality_profitability_industry_defense_reconfirm` 只改善局部 2023/2026，未改写 winner；本轮开局 guard 已显示 `ashare_path1_core_multifactor 46/46 complete`，因此不再补覆盖缺口。
- 本轮候选 ID 与命令：本轮 Path 1 没有新增 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py` 做 fast-pass 巡检。该命令提示 `since_2020_only` clear improvement 为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`，但 `./.venv/bin/python scripts/update_weighted_winners.py` 后正式 Path 1 window winner、robust candidate 与 tracked payload 均未改变。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 覆盖仍为 `46` 个 strategy/base candidates，最终 guard 继续显示 `46/46 complete`；本轮预算优先给 Path 2、Path 4、Path 5 audit 与 HK 扩展线，因此 core_multifactor 只做设计记录。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> signal_quality`。下一轮第一候选建议注册并确认 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`。

## 本轮执行计划（2026-06-08 12:13 CST）

- 上一轮候选/结果摘要：上一轮要求确认 core multifactor 的 `quality_profitability_value_lowvol_trend_cost_guard_reconfirm`；本轮开局 guard pass，但注册该新 base 后出现 `ashare_path1_core_multifactor 1/47 missing`，按增量缺口命令补齐五窗口，没有改跑全量。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`。首个未锁日期命令触发 A股缓存 stale guard，成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_cost_guard_reconfirm`。
- 五窗口结果：CAGR `14.34% / 14.59% / 30.90% / 58.08% / 63.18%`，最大回撤 `-28.99% / -29.84% / -16.78% / -14.07% / -4.62%`，换手 `2.72x / 3.01x / 3.21x / 5.13x / 5.47x`。2023/2026 可用，但 2017/2020 明显弱于当前 Path 1 robust。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 扩到 `47` 个 variants，最终补齐后 guard 覆盖 complete；`winner_only_pass.py` 仍提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 是 `since_2020_only` fast-pass clear improvement。`update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> holding_shape`。第一条命令建议确认 `core_explore_80_20_total_mv_winner_core__share_16_84_hold_2_8_ramp70_cost_guard_reconfirm`，命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_16_84_hold_2_8_ramp70_cost_guard_reconfirm`；若未注册，先按现有 holding_shape helper 增加该单一变体。

## 本轮执行计划（2026-06-08 17:37 CST）

- 上一轮候选/结果摘要：上一轮留下 `share_16_84_hold_2_8_ramp70_cost_guard_reconfirm`，但代码中 `share_16_84_hold_2_8_ramp70_cost_guard` 已是现役完整候选；本轮按 guard 的 `holding_shape` focus 继续向更高核心占比推进。
- 本轮 active pool 处理：从 Path 1 fast-pass lists 移除旧弱线 `share_04_96_hold_2_8_ramp75_cost_guard`，新增 `share_22_78_hold_2_8_ramp64_cost_guard`，保持 holding_shape 约 `28` 个 active candidates。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_22_78_hold_2_8_ramp64_cost_guard`。
- 四窗口结果：CAGR `18.99% / 23.07% / 36.21% / 99.04%`，最大回撤 `-22.42% / -17.69% / -19.24% / -10.06%`，换手 `2.65x / 2.98x / 3.01x / 4.47x`。它短窗强，但长窗回撤和 Sharpe 不足，未改变 Path 1 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 为 `47` 个 variants，guard 最终为 `47/47 complete`。`winner_only_pass.py` 仍提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 对 `since_2020_only` 有 fast-pass clear improvement，但 `update_weighted_winners.py` 后正式 Path 1 winner/robust 未采纳。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> signal_quality`。现有 core_multifactor coverage 已完整，下一轮先把 focus 映射到 satellite_defense 的信号质量线，注册/确认 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_sat_three_stage_buffered_cost_guard_risk18_quality_gate_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_sat_three_stage_buffered_cost_guard_risk18_quality_gate_reconfirm`。

## 本轮执行计划（2026-06-08 23:27 CST）

- 上一轮候选/结果摘要：上一轮 `share_22_78_hold_2_8_ramp64_cost_guard` 短窗强但长窗回撤不足；本轮开局 guard pass，随后注册 core multifactor 的 `signal_cashguard` 再确认候选并按 coverage 缺口补齐。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm`；覆盖命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_reconfirm`。
- 五窗口结果：CAGR `14.90% / 14.39% / 29.55% / 50.84% / 40.21%`，最大回撤 `-26.01% / -27.31% / -16.32% / -14.40% / -5.61%`，换手 `2.64x / 2.97x / 3.19x / 5.19x / 5.47x`。2023 可用但 2017/2020 不足，未改变 Path 1 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段巡检：代码实际 core_multifactor coverage 扩为 `48` 个 variants，最终 guard 为 complete。`winner_only_pass.py` 仍提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 是 `since_2020_only` fast-pass clear improvement，但 `update_weighted_winners.py` 未采纳。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> satellite_risk_cost`。下一轮第一条命令建议直接确认 fast-pass 提示线并与当前 2020 winner 比较： `.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`。

## 本轮执行计划（2026-06-09 04:20 CST）

- 上一轮候选/结果摘要：上一轮 core multifactor `signal_cashguard` 只改善局部 2023，未被正式 winner/robust 采纳。本轮开局 guard pass，Path 1 coverage 完整，预算优先用于 A股 Path2/3/4 新参数、Path5 入口复核和 HK 六个策略，因此 Path 1 做 fast-pass 巡检和下一轮候选设计。
- 本轮候选 ID 与命令：本轮没有新增 Path 1 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`。该命令仍提示 `since_2020_only` clear improvement 为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`，但 `./.venv/bin/python scripts/update_weighted_winners.py` 后正式 Path 1 window winner、robust candidate 与 tracked payload 均未改变。
- core_multifactor 子段巡检：本轮读取代码后实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 为 `48` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 48/48 complete`、`ashare_path1_fast_family 109/109 complete`。本轮没有新增 overlay 变体，也没有把 Path 4 emergent theme 当作 Path 1 core_multifactor。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> holding_shape`。下一轮第一候选建议注册并确认 `core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`；若 fast-pass 继续提示旧 `risk20_reconfirm`，同步复核它与正式 promotion score 的排序差异。

## 本轮执行计划（2026-06-09 20:05 CST）

- 上一轮候选/结果摘要：上一轮建议继续 holding_shape 的 `share_24_76_hold_2_8_ramp62_cost_guard`，但本轮开局与最终 guard 均把 Path 1 轮换回 `core_multifactor_coverage`，且代码实际 `core_multifactor=48/48 complete`，因此本轮不新增 Path 1 base id，避免在 focus 已变化时继续扩 holding_shape。
- 本轮候选 ID 与命令：本轮 Path 1 仅执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py` 做 fast-pass 巡检。该命令仍提示 `since_2020_only` clear improvement 为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm`；随后 `.venv/bin/python scripts/update_weighted_winners.py` 未把它提升为官方 Path 1 window winner 或 robust candidate。
- core_multifactor 子段巡检：本轮读取代码后实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 为 `48` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 48/48 complete`、`ashare_path1_fast_family 109/109 complete`。本轮没有新增 overlay，也没有把独立 Path 4 emergent theme 计入 Path 1。
- 结论：Path 1 本轮没有 window winner、robust candidate 或 tracked payload 变化；`winner_only_pass.py` 与正式 promotion score 的差异仍需单独复核。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> core_multifactor_coverage`。下一轮第一候选建议注册一个单一多因子风险/信号复核：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`；若未注册，先按现有 core_multifactor helper 只增加该一个 variant。

## 本轮执行计划（2026-06-09 22:26 CST）

- 上一轮候选/结果摘要：上一轮留下的 core_multifactor `risk20_reconfirm` 已按本轮开局 guard 注册后补齐；初始 guard 为 pass，注册后出现 `ashare_path1_core_multifactor` 与 fast-family 缺口，本轮按增量 `--only-base-ids` 补齐，没有改跑全量。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_trend_signal_cashguard_risk20_reconfirm`；实际合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <seven_ashare_incremental_ids>`。
- 五窗口结果：CAGR `14.64% / 14.18% / 29.15% / 50.72% / 39.84%`，最大回撤 `-27.16% / -28.90% / -17.83% / -14.40% / -5.61%`，换手 `2.66x / 2.99x / 3.23x / 5.20x / 5.46x`。它没有改善 2017/2020，未改变 Path 1 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段巡检：代码实际 core_multifactor 扩到 `49` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 49/49 complete`、`ashare_path1_fast_family 110/110 complete`。`winner_only_pass.py` 仍以 exit `2` 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 是 `since_2020_only` fast-pass clear improvement，但 `update_weighted_winners.py` 后官方 Path 1 未采纳。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> signal_quality`。下一轮不要再只补覆盖，第一候选建议注册 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk18_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk18_reconfirm`；若未注册，先只增加这一条 signal_quality 变体。

## 本轮执行计划（2026-06-10 04:41 CST）

- 上一轮候选/结果摘要：上一轮留下 `signal_quality` 多因子复核，本轮注册并五窗口确认 `risk18_reconfirm`，目标是用质量/盈利/信号现金守门降低长窗回撤，而不是补覆盖。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk18_reconfirm`；实际 A股合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <seven_ashare_incremental_ids>`。
- 五窗口结果：CAGR `14.55% / 12.91% / 21.09% / 61.27% / 38.12%`，最大回撤 `-23.56% / -22.03% / -17.70% / -14.14% / -5.60%`，换手 `2.69x / 3.02x / 3.09x / 5.19x / 5.46x`。它未改善 Path 1 现有 official winner 或 robust。
- core_multifactor 子段巡检：代码实际 core_multifactor 扩到 `50` 个 variants，`winner_only_pass.py` 仍 exit `2` 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 为 `since_2020_only` fast-pass clear improvement；`update_weighted_winners.py` 后官方 Path 1 仍保持 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__port_weekly_exposure_buffered`。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> satellite_risk_cost`。下一轮第一候选建议回到 fast-pass 提示的 satellite 三段线，测试更低风险/成本约束：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk18_reconfirm`；若未注册，先只增加这一条，core_multifactor 暂不继续加宽。

## 本轮执行计划（2026-06-10 10:40 CST）

- 上一轮候选/结果摘要：上一轮 `risk18_reconfirm` 已确认但未改写 official winner；本轮开局 guard pass，最终按 satellite risk/cost 与 fast-pass 提示线之间的空档注册更低风险暴露的 `risk16_reconfirm`，不是继续扩 core_multifactor 覆盖。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk16_reconfirm`；实际 A股合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <one_path1_id>,<two_path2_ids>,<one_path3_id>`。
- 五窗口结果：CAGR `22.40% / 29.69% / 26.39% / 94.62% / 98.46%`，最大回撤 `-14.31% / -12.04% / -17.45% / -10.91% / -6.61%`，换手 `2.99x / 3.35x / 3.39x / 4.62x / 7.35x`。它短窗和回撤形态可用，但未超过官方 Path 1 window winner 或 robust candidate。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 仍为 `50` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 50/50 complete`、`ashare_path1_fast_family 112/112 complete`。本轮没有新增 core_multifactor overlay；`winner_only_pass.py` 仍以 exit `2` 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 是 `since_2020_only` fast-pass clear improvement，但 `update_weighted_winners.py` 后 official winner/robust 未采纳。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> core_multifactor_coverage`。下一轮第一候选建议只注册一个多因子风险下探对照：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm`；若未注册，先只增加这一条。

## 本轮执行计划（2026-06-10 16:31 CST）

- 上一轮候选/结果摘要：上一轮留下 core_multifactor 的 `quality_profitability_signal_cashguard_risk16_reconfirm`；本轮注册后 guard 报 `ashare_path1_core_multifactor 1/51 missing`，按增量 `--only-base-ids` 补齐五窗口，没有改跑全量。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm`；路径首命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cashguard_risk16_reconfirm`。
- 五窗口结果：CAGR `14.62% / 13.24% / 22.45% / 64.65% / 50.33%`，最大回撤 `-25.51% / -22.98% / -16.86% / -14.14% / -4.25%`，换手 `2.66x / 2.99x / 3.07x / 5.20x / 5.45x`。它没有改写 Path 1 window winner、robust candidate 或 tracked payload。
- core_multifactor 子段巡检：代码实际 core_multifactor 扩到 `51` 个 variants，最终 guard 显示 `51/51 complete`、fast family `113/113 complete`。`winner_only_pass.py` 仍以 exit `2` 提示旧 `aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk20_reconfirm` 是 `since_2020_only` fast-pass clear improvement；`update_weighted_winners.py` 后 official Path 1 未采纳。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> signal_quality`。下一轮不要继续单纯下探 risk，建议注册一个 signal/growth 交叉验证：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk16_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk16_reconfirm`；若未注册，先只增加这一条。

## 本轮执行计划（2026-06-11 05:45 CST）

- 上一轮候选/结果摘要：上一轮留下 core_multifactor 的 `quality_profitability_growth_signal_cashguard_risk16_reconfirm`；本轮注册后初次 guard 出现 `ashare_path1_core_multifactor 1/52 missing`，曾有一次未锁 `--end-date` 的增量补跑触发 A股缓存目标日 `2026-06-11` stale guard，随后用 `--end-date 2026-06-09` 按 `--only-base-ids` 补齐，没有改跑全量。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk16_reconfirm`；成功命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_signal_cashguard_risk16_reconfirm`。
- 五窗口结果：CAGR `14.81% / 13.58% / 22.76% / 72.39% / 50.67%`，最大回撤 `-21.22% / -20.75% / -15.98% / -13.91% / -4.25%`，换手 `2.63x / 2.89x / 3.11x / 5.43x / 5.46x`。该线短窗和 2023 可用，但 2017/2020 仍弱于当前 Path 1 official winner/robust。
- core_multifactor 子段巡检：代码实际 core_multifactor 扩到 `52` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 52/52 complete`、fast family `114/114 complete`。`winner_only_pass.py` 仍以 exit `2` 提示旧 fast-pass 线有 clear improvement；`update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> signal_quality` 且状态为 `rotate`。下一轮第一候选建议只注册一个 signal/growth/trend 交叉验证：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk16_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk16_reconfirm`；若未注册，先只增加这一条，避免继续无边界扩 core_multifactor。

## 本轮执行计划（2026-06-11 16:10 CST）

- 上一轮候选/结果摘要：上一轮留下 core_multifactor 的 `quality_profitability_growth_trend_signal_cashguard_risk16_reconfirm`；本轮注册后 guard 报 `ashare_path1_core_multifactor 1/53 missing`，与 Path 4 prom20 缺口一起按 `--only-base-ids` 补齐五窗口，未改跑全量。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk16_reconfirm`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <one_path1_id>,<three_path4_prom20_ids>`。
- 五窗口结果：CAGR `14.85% / 12.29% / 24.91% / 68.85% / 47.93%`，最大回撤 `-24.54% / -22.79% / -17.17% / -15.10% / -4.25%`，换手 `2.58x / 2.88x / 3.10x / 5.02x / 5.45x`。2025/2026 有弹性，但 2017/2020 仍弱于 Path 1 official winner/robust。
- core_multifactor 子段巡检：代码实际 core_multifactor 扩到 `53` 个 variants，最终 guard 显示 `ashare_path1_core_multifactor 53/53 complete`、fast family `115/115 complete`。`update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> satellite_risk_cost`。下一轮不要继续扩 core_multifactor，第一候选建议在已覆盖的 satellite 三段线之间补一个成本/风险插值：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk14_reconfirm`；若未注册，先只增加这一条。

## 本轮执行计划（2026-06-25 21:16 CST）

- 上一轮候选/结果摘要：本轮 Path 1 没有新增 base id，按 guard 要求巡检 fast-pass 与 core_multifactor 真实代码集合；`scripts/winner_only_pass.py` 显示 fast family `base_candidates=129`、`evaluated=272`、core_multifactor 实际 `62` 条，未发现可替换 official winner 的 fast-pass。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 与 `PATH1_FAST_PASS_VARIANT_IDS` 覆盖完成，最终 guard 显示 `ashare_path1 -> rotate / core_multifactor_coverage`，direction counts 中 core_multifactor 为 `62`。本轮没有把 Path 4-lite/core_multifactor 当作独立 Path 4。
- 本轮命令：`.venv/bin/python scripts/winner_only_pass.py`、`.venv/bin/python scripts/update_weighted_winners.py`，以及 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --family-scope refresh_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 结论：Path 1 window winner、robust candidate、tracked payload 均未改变；本轮新增预算让给 Path 2/3/4 与 Path 5 入口。A股 tracked/live/public 已通过后续 export 与 snapshot 同步。
- 下一轮 focus：最终 guard 仍指向 `core_multifactor_coverage`。下一轮第一候选建议只注册一条多因子确认线，检查 `quality/profitability/growth/trend` 加更硬 cash/risk guard 后是否改善 2020/2023：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk14_reconfirm`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk14_reconfirm`。

## 本轮执行计划（2026-06-26 09:46 CST）

- 上一轮候选/结果摘要：上一轮 Path 1 没有新增 base id，本轮继续按要求巡检 fast-pass 与 core_multifactor 真实代码集合；`scripts/winner_only_pass.py` 显示 fast family `base_candidates=129`、`evaluated=272`、core_multifactor 实际 `62` 条，未发现足以替换 official winner 的 fast-pass。
- 本轮候选 ID 与命令：本轮没有新增 Path 1 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-25 --family-scope refresh_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- core_multifactor 子段巡检：最终 guard 显示 `ashare_path1_core_multifactor 62/62 complete`、`ashare_path1_fast_family 130/130 complete`。本轮没有新增 overlay，也没有把独立 Path 4 emergent_theme 计入 Path 1。
- 结论：`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 均未改变；live/public 已在 A股刷新到 2026-06-25 后重新导出。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> signal_quality`。下一轮第一候选建议只注册一条多因子信号质量对照：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm`。

## 本轮执行计划（2026-06-26 20:46 CST）

- 上一轮候选/结果摘要：上一轮计划的 Path 1 信号质量候选本轮未注册，原因是开局 guard pass 后预算优先投给 Path2/3/4、Path5 入口和 HK Path1/2/3；Path 1 本轮完成 fast-pass 与 core_multifactor 真实代码池巡检。
- 本轮候选 ID 与命令：本轮没有新增 Path 1 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`，并在收尾执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --family-scope refresh_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 同步活跃观察集合。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 仍为 `62` 个 variants，最终 guard 通过且 Path 1 direction counts 中 `core_multifactor=62`；本轮没有新增 overlay，也没有把独立 Path 4 emergent theme 计入 Path 1。
- 结论：`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 均未改变；`export_live_platform_data.py` 输出 `44` 个 live strategies，`generate_public_snapshot.py` 已重新通过。Path 1 本轮没有 evict/归档。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> satellite_risk_cost`。下一轮第一候选建议只注册一条 satellite 风险/成本微调线：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm_exit64`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk10_reconfirm_exit64`。若未注册，先只加入该一个 satellite variant。

## 本轮执行计划（2026-06-27 07:44 CST）

- 上一轮候选/结果摘要：上一轮留下 satellite 风险/成本微调，但本轮开局 guard pass 且新增预算优先给 Path2/3/4 与 HK 扩展确认；Path 1 完成 fast-pass 与 core_multifactor 真实代码池巡检。
- 本轮候选 ID 与命令：本轮没有新增 Path 1 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`，并在收尾执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --family-scope refresh_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 同步活跃观察集合。
- core_multifactor 子段巡检：代码实际 `PATH1_FAST_PASS_DIRECTION_GROUPS["core_multifactor"]` 仍为 `62` 个 variants，最终 guard 通过且 Path 1 direction counts 中 `core_multifactor=62`；本轮没有新增 overlay，也没有把独立 Path 4 emergent theme 计入 Path 1。
- 结论：`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 均未改变；`export_live_platform_data.py` 输出 `44` 个 live strategies，`generate_public_snapshot.py` 重新通过。Path 1 本轮没有 evict/归档。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> core_multifactor_coverage`。下一轮第一候选建议回到多因子覆盖，注册一条更硬 cash/risk guard 的信号质量确认线：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_cashguard_risk12_reconfirm`。若未注册，先只加入该一个 core_multifactor variant。

## 本轮执行计划（2026-07-02 07:00 CST）

- 上一轮候选/结果摘要：上一轮建议继续 core_multifactor 的 signal/cash/risk guard；本轮按最终 focus `core_multifactor_coverage` 注册并确认一条更低风险暴露的趋势信号线，目标是验证 `quality/profitability/growth/trend` 在 2017/2020 长窗是否能压回撤。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk08_reconfirm,<two_path2_v68_ids>,<three_path4_prom26_ids>`。曾有一次未锁 `--end-date` 的 A股增量命令因本地缓存未覆盖 `2026-07-02` 失败，随后用 `--end-date 2026-07-01` 增量补齐。
- 五窗口结果：CAGR `11.20% / 12.26% / 22.24% / 65.04% / 76.13%`，最大回撤 `-16.19% / -20.00% / -12.85% / -15.23% / -4.26%`，Sharpe `0.6804 / 0.6432 / 0.8913 / 1.4750 / 2.1943`，换手 `2.54x / 2.72x / 3.04x / 5.36x / 5.33x`。该线防守性优于前几条高风险多因子，但 2017/2020 收益仍低于现有 Path 1 official winner/robust。
- core_multifactor 子段巡检：最终 guard 显示 `ashare_path1_core_multifactor 64/64 pass`、`ashare_path1_fast_family 132/132 pass`。`update_weighted_winners.py` 后 Path 1 composite 仍由 `risk20_reconfirm`、`aggr_10_90_prom6_cash_off`、`aggr_10_90_prom6` 组成，composite mean CAGR `48.78%`、min CAGR `22.67%`，本轮 `risk08` 未进入 tracked。
- 结论与归档：本轮没有 Path 1 evict/归档；新增多因子只完成确认，不改变 window winner、robust candidate 或 tracked payload。
- 下一轮 focus：最终 guard 给出 `ashare_path1 -> core_multifactor_coverage`。下一轮第一候选建议不要继续只降 risk，而是比较 `risk08` 与旧 `risk12/risk16` 的信号门槛差异后注册一条 `risk10` 中间确认线：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk10_reconfirm`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk10_reconfirm`。

## 本轮执行计划（2026-07-03 07:23 CST）

- 上一轮候选/结果摘要：上一轮留下 `risk10` 中间确认线；本轮开局 guard 为 `pass`，`ashare_path1_core_multifactor 65/65 complete`、fast family `133/133 complete`，无 blocking coverage。曾先用未锁日期运行 A股 `refresh_active`，因本地缓存只到 `2026-07-02` 而失败，随后全部成功命令均锁定 `--end-date 2026-07-02`。
- 本轮候选 ID 与命令：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk10_reconfirm`；实际合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <one_path1_id>,<one_path2_id>,<one_path3_id>,<three_path4_ids>`，随后执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`、`.venv/bin/python scripts/update_weighted_winners.py` 与 `refresh_active`。
- 五窗口结果：CAGR `10.22% / 10.80% / 21.58% / 58.70% / 58.54%`，最大回撤 `-20.04% / -21.89% / -13.75% / -15.23% / -9.19%`，Sharpe `0.6229 / 0.5761 / 0.8591 / 1.3400 / 1.5940`，换手 `2.58x / 2.73x / 3.01x / 5.34x / 5.34x`。它比 `risk08` 提高部分收益，但 2017/2020 仍低于 Path 1 official robust。
- core_multifactor 子段巡检：代码实际 core_multifactor 覆盖为 `65` 个 variants，guard 无缺口；本轮没有新增 overlay，也没有把独立 Path 4 emergent theme 计入 Path 1。`winner_only_pass.py` 以 exit `2` 给出 fast-pass clear improvement 信号：`risk06_reconfirm` 在 `since_2025_only` 优于当前 `risk10`，但该 fast-pass 只作为下一轮候选，不直接改 official。
- 结论：`update_weighted_winners.py` 后 Path 1 tracked payload 有同步重写，但 `risk10` 属于 target-viable/validation-risk fallback，没有形成干净 robust 晋级；本轮无 Path 1 evict/归档。
- 下一轮 focus：若最终 guard 仍指向 `core_multifactor_coverage` 或 `signal_quality`，第一候选先确认 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk06_reconfirm`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_trend_signal_quality_gate_cashguard_risk06_reconfirm`。

## 本轮执行计划（2026-07-07 05:01 CST）

- 上一轮候选/结果摘要：上一轮 `risk10` 中间确认线没有成为干净 robust，本轮按开局 plan 先补 core_multifactor 的 `risk09_v5`，最终 guard 轮换到 `satellite_risk_cost`。本轮没有把独立 Path 4 强主题涌现并入 Path 1。
- 本轮候选 ID 与命令：新增/确认 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_growth_lowvol_signal_quality_gate_cashguard_risk09_reconfirm_v5`；成功补缺口命令与 Path4 三底座合并为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <one_path1_core_multifactor_id>,<three_path4_signal30_ids>`。
- 五窗口结果：CAGR `11.83% / 11.28% / 19.39% / 52.76% / 56.16%`，最大回撤 `-20.19% / -21.11% / -13.07% / -15.42% / -11.16%`，Sharpe `0.6784 / 0.5916 / 0.7877 / 1.2370 / 1.4369`，换手 `2.54x / 2.75x / 2.87x / 5.12x / 5.29x`。长窗收益仍低于现有 official robust，不能晋级。
- core_multifactor 子段巡检：代码实际 core_multifactor 为 `67` 个 variants，最终 guard 显示覆盖完整；`scripts/winner_only_pass.py` exit `2`，提示 fast-pass clear improvement 主要来自既有 `share_08_92_hold_2_8_ramp75_cost_guard`、`quality_profitability_value_lowvol_trend_cost_guard_reconfirm` 与 satellite `risk06_reconfirm`，不是本轮 `risk09_v5` 直接改写 official。
- 结论与归档：`scripts/update_weighted_winners.py` 后 Path 1 window winner、robust candidate 与 tracked payload 未改变；本轮没有 Path 1 evict。下一轮 focus 为 `satellite_risk_cost`，不要继续只扩 core_multifactor。
- 下一轮 focus：第一候选建议确认 satellite 成本/风险线 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk06_exit50_reconfirm`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_sat_three_stage_buffered_cost_guard_risk06_exit50_reconfirm`。
- Final guard 修正：最终 guard 轮换为 `ashare_path1 -> holding_shape / rotate / stagnation_runs=9`。下一轮先映射到 holding_shape 池，注册/确认 `core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`；首条命令改为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_24_76_hold_2_8_ramp62_cost_guard`。若该 id 未注册，先按 existing holding_shape helper 只增加这一条。
