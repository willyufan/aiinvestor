# A股 Path 7 暴跌适应与防守杠铃研究计划

## 2026-08-12 首轮（端点 2026-08-11）

### 上一轮候选与结果摘要

- 新建独立 Path 7，先验证现金 + Path 3 周频进攻 sleeve。`cash70_weekly30_v1` 五窗口 MaxDD 为 `-9.75%/-8.68%/-8.37%/-7.41%/-7.40%`，但 2020 CAGR 仅 `0.98%`、2026 CAGR `-4.67%`，`reject`；`cash50_weekly50_v2` 回撤放大且 2026 CAGR `-6.92%`，`reject`。假设“长期高现金本身可成为可投资防守路径”不成立。
- `cash50_static_fast_pulse_v3` 将慢趋势压仓移除，常态50%进攻、快跌时15%；五窗口 MaxDD 约 `-11.35%/-10.94%/-10.19%/-7.91%/-7.90%`，但 2020 CAGR仅 `2.50%`、2026 `-1.40%`。判定 `keep_watch`：进入 active 观察位，不是强稳定 winner；其价值是证明动态脉冲优于长期低仓，但现金并非足够好的防守资产。v1/v2 从 active 移除并保留历史快照；Path 7 未进入 A股 Path1-4 winner / robust / tracked 体系。

### 本轮候选 ID 与命令

- IDs：`core_explore_80_20_equal_weight_winner_core__path7_crash_resilience_cash70_weekly30_fast_combined_v1_defbar`、`...cash50_weekly50_fast_combined_v2_defbar`、`...cash50_static_fast_pulse_v3_defbar`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__path7_crash_resilience_cash70_weekly30_fast_combined_v1_defbar,core_explore_80_20_equal_weight_winner_core__path7_crash_resilience_cash50_weekly50_fast_combined_v2_defbar,core_explore_80_20_equal_weight_winner_core__path7_crash_resilience_cash50_static_fast_pulse_v3_defbar`；scorecard：`results/research/a_share/crash_resilience_scorecard_20260812.json`。

### 下一轮 focus 提示

- 下一轮把现金防守腿替换为可交易的质量/低波防守篮子，再与 20%-30% Path 3 周频进攻 sleeve 组合；先确保防守腿自身 since_2020 / since_2023 CAGR 为正，再验证 2026 7月 MaxDD。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__path7_quality_lowvol70_weekly30_fast_pulse_v4_defbar,core_explore_80_20_equal_weight_winner_core__path7_quality_lowvol60_weekly40_fast_pulse_v5_defbar`（需先实现双 sleeve 权重合成）。

### Focus 候选池

- `defensive_sleeve`：`quality_lowvol70_weekly30_v4`、`quality_lowvol60_weekly40_v5`；`crash_pulse`：`pulse15_1w_v4`、`pulse25_1w_v5`。
- `recovery_control`：`immediate_recovery_v4`、`two_week_recovery_v5`；`capacity_cost`：`quality_top20_equal_v4`、`quality_top30_capped_v5`。
