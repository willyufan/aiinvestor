# 沪港通 Path 1 研究计划

## 本轮执行计划（2026-05-28 22:19 CST）

- 开局 guard 为 `pass`；上一轮 plan 要求回到 monthly-weekly overlay 邻域，本轮新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34`，作为无低波但保留成本守门的 `exit34` 对照，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34,hkconnect_path2_inverse_elastic_monthly_cost_guard_v8,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit40`。
- `soft_cost_guard_exit34` 五窗口 CAGR 为 `24.31% / 29.83% / 32.59% / 42.95% / -9.45%`，最大回撤为 `-22.67% / -13.36% / -13.36% / -13.36% / -10.91%`，换手为 `3.52x / 3.55x / 3.26x / 3.45x / 3.67x`。它恢复了长窗收益，但 2026 重新转负，不替换 HK Path 1 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `160/160 complete`，下一轮 focus 为 `biweekly_buffer`。第一条命令建议回到双周低波/成本缓冲，用更低出场阈值检查是否能保留 2026 正收益并少损长窗，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-28 16:18 CST）

- 开局 guard 为 `pass`；上一轮 plan 要求回到双周低波/成本缓冲，本轮新增 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34`，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v7,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover8_exit38`。
- `biweekly_equal_buffered_lowvol_soft_cost_guard_exit34` 五窗口 CAGR 为 `15.56% / 16.56% / 25.85% / 35.85% / 1.70%`，最大回撤为 `-21.08% / -19.22% / -11.21% / -6.94% / -4.49%`，换手为 `5.77x / 5.59x / 5.24x / 6.69x / 7.96x`。它保留浅回撤和 2026 正收益，但长窗收益明显低于 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `157/157 complete`，下一轮 focus 为 `monthly_weekly_overlay`。第一条命令建议回到 monthly-weekly overlay 邻域，测试无低波但保留成本守门的 `exit34` 对照，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `lowvol_soft_cost_guard_exit28` 保持 2026 正收益但长窗收益折损，本轮按 `monthly_weekly_overlay` 去掉 lowvol，保留成本守门并收紧到 `exit30`，验证无低波版本是否能找回长窗收益。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit30_risk25,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit40`。
- `soft_cost_guard_exit30` 五窗口 CAGR 为 `23.99% / 29.46% / 32.25% / 42.95% / -9.45%`，最大回撤为 `-23.29% / -13.36% / -13.36% / -13.36% / -10.91%`，换手为 `3.57x / 3.55x / 3.27x / 3.45x / 3.67x`。去掉 lowvol 找回部分长窗收益，但 2026 重新转负，不替换 HK Path 1 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `154/154 complete`，下一轮 focus 转为 `biweekly_buffer`。第一条命令建议回到双周低波/成本缓冲，测试是否能少损长窗并保持 2026 正收益，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；上一轮双周低波轻成本版收益折损，本轮按 `risk_overlay_cost` 回到 monthly-weekly overlay 低波成本线，确认更低 `exit28` 是否能保留 2026 正收益与浅回撤。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit28`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit28,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit32_risk30,hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit68`。
- `lowvol_soft_cost_guard_exit28` 五窗口 CAGR 为 `19.64% / 25.01% / 29.92% / 34.65% / 6.49%`，最大回撤为 `-21.76% / -7.14% / -6.85% / -6.85% / -6.73%`，换手为 `3.76x / 3.69x / 3.40x / 3.85x / 4.90x`。它保持浅回撤和 2026 正收益，但收益继续低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `151/151 complete`，下一轮 focus 转为 `monthly_weekly_overlay`。第一条命令建议去掉低波收益折损、保留成本守门并收紧出场，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`；上一轮 `monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30` 保持 2026 正收益和浅回撤但长窗收益折损，本轮按 `biweekly_buffer` 测试双周低波轻成本版本，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36,hkconnect_path2_inverse_elastic_monthly_cost_guard_v7,hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit66`。
- `biweekly_equal_buffered_lowvol_soft_cost_guard_exit36` 五窗口 CAGR 为 `15.56% / 16.56% / 25.85% / 35.85% / 1.70%`，最大回撤为 `-21.08% / -19.22% / -11.21% / -6.94% / -4.49%`，换手为 `5.77x / 5.59x / 5.24x / 6.69x / 7.96x`。它保留浅回撤与 2026 正收益，但 2017/2020/2023 收益明显低于 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，下一轮 focus 为 `risk_overlay_cost`。第一条命令建议回到 monthly-weekly overlay 低波成本线，测试更低出场阈值能否保留浅回撤且少损长窗收益，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit28`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮建议沿 `risk_overlay_cost` 测 `lowvol_soft_cost_guard_exit30`，本轮已新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30`，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v6,hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit64`。
- `lowvol_soft_cost_guard_exit30` 五窗口 CAGR 为 `19.77% / 25.18% / 30.07% / 34.65% / 6.49%`，最大回撤 `-21.63% / -7.17% / -6.85% / -6.85% / -6.73%`，换手 `3.73x / 3.68x / 3.39x / 3.85x / 4.90x`。它保持 2026 正收益和浅回撤，但 2017/2020/2023 收益仍低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，四窗口 meanCAGR `33.87%`、minCAGR `26.10%`、worstMaxDD `-21.06%`、meanTurn `3.33x`；三张 HK 图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `145/145 complete`，下一轮 focus 转为 `biweekly_buffer`。第一条命令建议回到双周缓冲线，测试是否能以更低换手保留本轮低波浅回撤，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮低波 + 成本守门 `exit32` 保持 2026 为正但收益折损，本轮按 `monthly_weekly_overlay` 去掉低波、保留成本守门与 `exit32`，新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32`。HK 合并回测命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32,hkconnect_path2_inverse_elastic_monthly_cost_guard_v6,hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit62`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32`。五窗口 CAGR 为 `24.15% / 29.72% / 32.53% / 42.95% / -9.45%`，最大回撤 `-23.19% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.55x / 3.55x / 3.26x / 3.45x / 3.67x`。去低波提高了长窗收益，但 2026 重新转负，不能替换当前 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，四窗口 meanCAGR `33.87%`、minCAGR `26.10%`、worstMaxDD `-21.06%`、meanTurn `3.33x`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议不要只去低波，改在 `exit30/32` 上组合低波与成本守门，先测 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；上一轮要求沿 `risk_overlay_cost` 测试低波 + 成本守门的 monthly-weekly overlay，本轮新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32`。HK 合并回测命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v5,hkconnect_path3_theme_fast_weekly_defensive_turnover3_exit60`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32`。五窗口 CAGR 为 `19.98% / 25.44% / 30.26% / 34.65% / 6.49%`，最大回撤 `-21.30% / -7.16% / -6.85% / -6.85% / -6.73%`，换手 `3.72x / 3.68x / 3.39x / 3.85x / 4.90x`。它把 2026 保持为正且回撤浅，但收益继续低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `monthly_weekly_overlay`。下一轮第一条命令建议去掉低波收益折损、保留成本守门与 `exit32`，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮 `biweekly_equal_buffered_lowvol_soft_exit38` 修复 2026 但收益折损，本轮按 `monthly_weekly_overlay` 回到 monthly-weekly overlay robust 邻域，新增低波 + 轻现金 + `exit32` 组合。HK 合并回测命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit32,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit34_risk35,hkconnect_path3_theme_fast_weekly_cost_guard_turnover3_exit60`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit32`。五窗口 CAGR 为 `19.32% / 24.43% / 29.27% / 34.65% / 6.49%`，最大回撤 `-23.40% / -9.26% / -6.85% / -6.85% / -6.73%`，换手 `3.94x / 4.04x / 3.70x / 3.85x / 4.90x`。它保持 2026 正收益和浅回撤，但 2017/2020/2023 收益继续低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议在本轮 `lowvol_soft_cashguard_exit32` 基础上把现金防守改成更直接的周度 overlay 成本约束，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮 `monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32` 继续保持 2026 为正但收益折损，本轮按 `biweekly_buffer` 新增 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38,hkconnect_path2_theme_monthly_high_return_cost_control_v4,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover10_exit36`。
- `biweekly_equal_buffered_lowvol_soft_exit38` 五窗口 CAGR 为 `16.28% / 17.49% / 27.12% / 35.85% / 1.70%`，最大回撤 `-20.46% / -19.07% / -11.15% / -6.94% / -4.49%`，换手 `5.77x / 5.57x / 5.23x / 6.69x / 7.96x`。它能修复 2026 为小幅正收益并压回撤，但 2017/2020 收益仍显著低于 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `monthly_weekly_overlay`。下一轮第一条命令建议回到 monthly-weekly overlay robust 邻域，把低波浅回撤与现金成本防守合并测试，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮 `biweekly_equal_buffered_lowvol_soft_exit40` 修复 2026 但长窗收益折损，本轮按 `risk_overlay_cost` 回到 monthly-weekly overlay 的低波轻风控线，新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit36_risk35,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38`。
- `lowvol_soft_exit32` 五窗口 CAGR 为 `21.35% / 27.11% / 32.25% / 34.65% / 6.49%`，最大回撤 `-20.31% / -8.41% / -6.85% / -6.85% / -6.73%`，换手 `3.50x / 3.53x / 3.27x / 3.85x / 4.90x`。它继续保持 2026 为正和浅回撤，但相对无低波 `soft_exit34` robust 仍有收益折损。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `biweekly_buffer`。下一轮第一条命令建议从双周缓冲低波线继续找收益折损更小的 2026 修复，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `lowvol_soft_exit34` 修复 2026 但收益折损；本轮按 `biweekly_buffer` 新增 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40,hkconnect_path2_inverse_elastic_monthly_cost_guard_v5,hkconnect_path3_theme_fast_weekly_cost_guard_turnover4_exit58`。
- `biweekly_equal_buffered_lowvol_soft_exit40` 五窗口 CAGR 为 `16.28% / 17.48% / 27.12% / 35.85% / 1.70%`，最大回撤 `-20.46% / -19.06% / -11.15% / -6.94% / -4.49%`，换手 `5.77x / 5.57x / 5.23x / 6.69x / 7.96x`。结果与 `exit42` 基本同形，能保持 2026 正收益和浅回撤，但 2017/2020 长窗收益低于现有 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议回到 monthly-weekly overlay robust 邻域修复 2026 与成本，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `monthly_weekly_overlay`；本轮按计划新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit38_risk40,hkconnect_path3_theme_fast_weekly_cost_guard_turnover5_exit56`。
- `lowvol_soft_exit34` 五窗口 CAGR 为 `21.27% / 27.07% / 32.26% / 34.65% / 6.49%`，最大回撤 `-20.35% / -8.58% / -6.85% / -6.85% / -6.73%`，换手 `3.47x / 3.50x / 3.26x / 3.85x / 4.90x`。它修复 2026 为正并显著压回撤，但 2017/2020/2025 收益仍低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `biweekly_buffer`。下一轮第一条命令建议用双周缓冲低波线修复 2026，同时控制收益折损，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `biweekly_buffer`；本轮按计划新增双周缓冲无低波版本 `hkconnect_path1_biweekly_equal_buffered_soft_exit40`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_soft_exit40`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_exit40,hkconnect_path2_theme_monthly_high_return_cost_control_v3,hkconnect_path3_theme_fast_weekly_defensive_turnover6_exit54`。
- `biweekly_equal_buffered_soft_exit40` 五窗口 CAGR 为 `21.79% / 22.47% / 21.27% / 24.18% / -15.62%`，最大回撤 `-21.03% / -21.03% / -16.20% / -16.20% / -8.76%`，换手 `5.77x / 5.57x / 5.42x / 7.10x / 6.51x`。它比低波双周线保留了更多长窗收益，但 2026 仍明显为负，未能替换当前 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `monthly_weekly_overlay`。下一轮第一条命令建议回到 robust 邻域做月频+周度 overlay 修复，而不是继续双周收益折损线，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass`，上一轮要求沿 `monthly_weekly_overlay` 修复 `soft_exit34` 的 2026 负收益；本轮新增 `soft_exit32`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32,hkconnect_path2_inverse_elastic_monthly_cost_guard_v4,hkconnect_path3_theme_fast_weekly_cost_guard_turnover6_exit54`。
- `soft_exit32` 五窗口 CAGR 为 `26.06% / 32.10% / 34.28% / 42.95% / -9.45%`，最大回撤 `-21.34% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.36x / 3.43x / 3.16x / 3.45x / 3.67x`。它没有修复 2026，且 robust 略低于现有 `soft_exit34`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `biweekly_buffer`。下一轮第一条命令建议回到双周缓冲但去掉过强低波收益折损，例如 `hkconnect_path1_biweekly_equal_buffered_soft_exit40` 或同等更高收益双周缓冲版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass`，上一轮 `biweekly_equal_buffered_lowvol_soft_exit42` 修复 2026 但收益折损较大；本轮按 `risk_overlay_cost`/`monthly_weekly_overlay` 回到 `soft_exit34` robust 邻域，新增浅现金防守版本，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light,hkconnect_path2_theme_monthly_high_return_cost_control_v2,hkconnect_path3_theme_fast_weekly_defensive_turnover8_exit52`。
- `soft_exit34_cashguard_light` 五窗口 CAGR 为 `23.25% / 28.47% / 31.01% / 42.95% / -9.45%`，最大回撤 `-23.78% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.82x / 3.99x / 3.56x / 3.45x / 3.67x`。浅现金没有修复 2026，且 2017/2020/2023 弱于当前 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 为 `monthly_weekly_overlay`。下一轮第一条命令建议不要继续加现金防守，改测更直接的退出阈值修复，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32` 或同等无低波月频周度 overlay 版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass`，上一轮 `soft_exit34` 把 HK Path 1 2017 winner 与 robust 推到无低波 monthly-weekly overlay，但 2026 仍为负；本轮按 `biweekly_buffer` 回到双周缓冲低波版本 `exit42`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit42`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit42,hkconnect_path2_equal_elastic_monthly_cost_guard_v4,hkconnect_path3_theme_fast_weekly_cost_guard_turnover8_exit52`。
- `biweekly_equal_buffered_lowvol_soft_exit42` 五窗口 CAGR 为 `16.28% / 17.48% / 27.12% / 35.85% / 1.70%`，最大回撤 `-20.46% / -19.06% / -11.15% / -6.94% / -4.49%`，换手 `5.77x / 5.57x / 5.23x / 6.69x / 7.96x`。它修复 2026 为小幅正收益且回撤浅，但 2017/2020 收益显著低于 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先。候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议回到当前 `soft_exit34` robust 邻域做浅现金/低波成本对照，而不是继续双周收益折损线，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass`，上一轮低波 `soft_exit36` 保持 2026 正收益但长窗收益低于无低波 soft 线；本轮按 `monthly_weekly_overlay` 回到无低波 `soft_exit34`，继续只作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path2_theme_monthly_high_return_lowturn_reconfirm,hkconnect_path3_theme_fast_weekly_defensive_turnover10_exit50`。
- `soft_exit34` 五窗口 CAGR 为 `26.10% / 32.08% / 34.34% / 42.95% / -9.45%`，最大回撤 `-21.06% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.33x / 3.39x / 3.13x / 3.45x / 3.67x`。它没有修复 2026 负收益，但四窗口 robust 较上一轮 `soft_exit36` 继续小幅提升。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 发生实质变化：2017 window winner 与 robust candidate 切到 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，robust 约为 `meanCAGR=33.87% / minCAGR=26.10% / worstMaxDD=-21.06% / meanTurn=3.33x`；2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先。
- 候选池未触发 HK explore cap evict。最终 guard 对 HK Path 1 为 `stagnation_runs=2 / focus=monthly_weekly_overlay`，因为本轮新 robust 签名已经写入 state；下一轮第一条命令建议围绕新 robust 做 2026 修复对照，例如实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light` 或 `soft_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass`，上一轮 `lowvol_soft_exit38` 修复 2026 但收益低于 HK Path 1 robust；本轮按 `risk_overlay_cost`/下一步对照，把低波轻风控退出阈值降到 `exit36`，继续只作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit40_risk45,hkconnect_path3_theme_fast_weekly_cost_guard_turnover10_exit50`。
- `lowvol_soft_exit36` 五窗口 CAGR 为 `21.10% / 26.75% / 31.96% / 34.73% / 6.49%`，最大回撤 `-20.05% / -8.77% / -6.80% / -6.80% / -6.73%`，换手 `3.44x / 3.46x / 3.24x / 3.86x / 4.90x`。它保持 2026 正收益和浅回撤，略高于上一轮低波 exit38 的长窗收益，但仍低于当前无低波 soft 线 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 新增该候选记录，但 winner/robust 未被替换：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`。候选池未触发 HK explore cap evict。
- 收尾 guard 下一轮 focus 为 `monthly_weekly_overlay`。下一轮第一条命令建议回到无低波 soft robust 邻域修复 2026，而不是继续低波收益折损，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34` 或 `soft_exit36_cashguard_light`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `soft_exit36` 已把 HK Path 1 robust 留在无低波的 soft 线；本轮按计划测试低波轻风控 `exit38`，继续只作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover9_exit42`。
- `lowvol_soft_exit38` 五窗口 CAGR 为 `21.03% / 26.62% / 31.95% / 34.73% / 6.49%`，最大回撤 `-19.68% / -8.96% / -6.80% / -6.80% / -6.73%`，换手 `3.43x / 3.43x / 3.22x / 3.86x / 4.90x`。它修复 2026 为正且回撤很浅，但 2017/2020/2023/2025 收益低于现有 soft/soft_exit36 robust/winner 组合。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 未被本轮低波候选替换：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`。候选池未触发 HK explore cap evict。
- 收尾 focus 转向 `biweekly_buffer`。下一轮第一条命令建议回到双周缓冲，但带上本轮低波浅回撤信息，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit42` 或同等低波双周版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass`，上一轮 `soft_exit38` 已把 2017 winner 与 robust 推到更低退出阈值；本轮按 `monthly_weekly_overlay` 继续测试 `soft_exit36`，目标是只看 2026 观察窗是否修复且不损伤 robust。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36,hkconnect_path2_breakout_cost_guard_biweekly_cashguard_exit35_risk50,hkconnect_path3_theme_fast_weekly_defensive_turnover12_exit48`。
- `soft_exit36` 五窗口 CAGR 为 `25.96% / 31.81% / 34.53% / 42.95% / -9.45%`，最大回撤 `-20.92% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.30x / 3.34x / 3.11x / 3.45x / 3.67x`。它没有修复 2026，但四窗口 robust 小幅高于 `soft_exit38`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 再次变化：2017 window winner 与 robust candidate 切到 `soft_exit36`，robust `meanCAGR=33.81% / minCAGR=25.96% / worstMaxDD=-20.92% / meanTurn=3.30x`；2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先。
- 候选池未触发 HK explore cap evict。收尾 guard 对 HK Path 1 为 `changed=true / stagnation_runs=0 / focus=monthly_weekly_overlay`；下一轮第一条命令建议不要再机械下调 exit，先比较 `soft_exit36` 与低波/现金防守组合，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass`，上一轮 `soft_exit40` 已把 2017 winner 与 robust 切到周度 overlay soft 线，但 2026 仍为负；本轮按 `monthly_weekly_overlay` 再把退出阈值降到 `38`，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit38`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit38,hkconnect_path2_theme_monthly_reconfirm_cost_control,hkconnect_path3_theme_fast_weekly_cost_guard_turnover12_exit48`。
- `soft_exit38` 五窗口 CAGR 为 `25.95% / 31.79% / 34.40% / 42.95% / -9.45%`，最大回撤 `-20.94% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.27x / 3.31x / 3.08x / 3.45x / 3.67x`；robust4 为 `meanCAGR=33.77% / minCAGR=25.95% / worstMaxDD=-20.94% / meanTurn=3.28x`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 再次变化：2017 window winner 与 robust candidate 切到 `soft_exit38`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先。新版本较 `soft_exit40` 稍抬 robust，但仍未修复 2026 负收益。
- 候选池未触发 HK explore cap evict。收尾 guard 对 HK Path 1 为 `changed=true / stagnation_runs=0 / focus=monthly_weekly_overlay`；下一轮第一条命令建议测试 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36` 或同等更低退出阈值版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_soft_exit36_id>`，重点只看能否改善 2026 且不损伤 robust。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass`，上一轮建议从 `monthly_weekly_overlay` 去掉低波并放宽退出；本轮新增 `soft_exit40`，继续只作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40,hkconnect_path2_theme_monthly_cost_control_lowturn,hkconnect_path3_theme_fast_weekly_cost_guard_turnover16_exit45`。
- `soft_exit40` 五窗口 CAGR 为 `25.76% / 31.66% / 34.38% / 42.95% / -9.45%`，最大回撤 `-20.90% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.26x / 3.28x / 3.06x / 3.45x / 3.67x`；它没有修复 2026，但长窗收益/回撤组合优于旧 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 发生实质变化：2017 window winner 切到 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40`，robust candidate 也切到该 ID，robust `meanCAGR=33.69% / minCAGR=25.76% / worstMaxDD=-20.90% / meanTurn=3.26x`。2020/2023 winner 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`。
- 候选池未触发 HK explore cap evict。收尾 guard 的下一轮 focus 为 `monthly_weekly_overlay`；第一条命令建议沿新 robust 做 2026 修复对照，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit38` 或同等更低退出阈值版本，用五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_id>` 判断能否保留 robust 且改善 2026。

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass`，上一轮 `biweekly_equal_buffered_lowvol_soft_cashguard_exit45` 浅回撤但收益折损过大；本轮按 `risk_overlay_cost`/低波轻风控回到月频等权缓冲 + 周度 overlay，去掉 cashguard 并把退出阈值调到 `exit42`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42`。实际 HK 合并命令：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path2_inverse_elastic_monthly_cost_guard_v3,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover9_exit40`。
- `lowvol_soft_exit42` 五窗口 CAGR 为 `21.00% / 26.50% / 31.90% / 34.70% / 6.50%`，最大回撤 `-19.70% / -9.50% / -6.80% / -6.80% / -6.70%`，换手 `3.41x / 3.38x / 3.17x / 3.86x / 4.90x`；2026 保持正收益且回撤浅，但 2017/2020/2023 收益仍低于 `weekly_overlay_soft` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；候选池未触发 HK explore cap evict。
- 下一轮 focus -> candidates 池切到 `monthly_weekly_overlay`，第一条命令建议去掉低波或进一步放宽退出，测试 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_id>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass`，上一轮 `monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45` 2026 转正但长窗收益不足；本轮按 `biweekly_buffer` 回到双周等权缓冲，叠加低波、轻现金防守与 `exit45`，继续只作为 HK 独立研究线。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cashguard_exit45`。实际 HK 合并命令：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cashguard_exit45,hkconnect_path2_equal_elastic_monthly_cost_guard_v3,hkconnect_path3_theme_fast_weekly_cost_guard_turnover14_exit45`。
- `biweekly_lowvol_soft_cashguard_exit45` 五窗口 CAGR 为 `15.43% / 16.36% / 24.12% / 35.85% / 1.70%`，最大回撤 `-21.74% / -19.07% / -11.17% / -6.94% / -4.49%`，换手 `5.88x / 5.77x / 5.34x / 6.69x / 7.96x`；2026 小幅转正且回撤浅，但 2017/2020 收益明显低于月频 weekly-overlay soft robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化；候选池未触发 HK explore cap evict。
- 下一轮 focus -> candidates 池：双周低波现金线收益折损过大，第一条命令建议回到 `monthly_weekly_overlay` 的低波轻风控但放宽现金防守，测试 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42`，五窗口 `--only-strategy-ids <hk_path1_lowvol_soft_exit42_id>`。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 指向 `monthly_weekly_overlay`；上一轮 `lowvol_cashguard_exit45` 长窗收益不足，本轮补 `lowvol + soft + cashguard + exit45`，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45,hkconnect_path2_breakout_cost_guard_biweekly_risk50,hkconnect_path3_theme_fast_weekly_cost_guard_turnover18_exit42`。
- `lowvol_soft_cashguard_exit45` 五窗口 CAGR 为 `18.94% / 24.07% / 28.96% / 34.73% / 6.49%`，最大回撤 `-24.07% / -9.02% / -6.80% / -6.80% / -6.73%`，换手 `4.02x / 4.07x / 3.70x / 3.86x / 4.90x`；2026 为正且回撤浅，但 2017/2020/2023 收益仍低于 `weekly_overlay_soft` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；未触发 HK explore cap evict。
- 收尾 guard 后 HK Path 1 rotation 切到 `biweekly_buffer`。下一轮第一条命令建议实现 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cashguard_exit45`，检查双周缓冲能否保留低波现金防守的浅回撤而减少月频 overlay 的长窗收益折损；五窗口 `--only-strategy-ids <hk_path1_biweekly_lowvol_soft_id>`。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮双周 `soft_cashguard_exit45` 收益不足且 2026 仍负，本轮按 `risk_overlay_cost` 回到月频等权缓冲 + 周度 overlay 的低波现金防守。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45`。
- 该候选五窗口 CAGR 为 `18.36% / 23.40% / 28.45% / 34.73% / 6.49%`，最大回撤 `-24.99% / -8.94% / -6.80% / -6.80% / -6.73%`，换手 `4.08x / 4.07x / 3.70x / 3.86x / 4.90x`；2026 转正且回撤浅，但 2017/2020/2023 收益低于 `weekly_overlay_soft` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；HK 线继续独立，不并入 A 股 winner。
- 下一轮 focus -> candidates 池：继续比较 2026 正收益与长窗收益折损，第一条命令建议实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45`，用五窗口 `--only-strategy-ids <hk_path1_next_risk_overlay_id>` 增量确认。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `soft_cashguard_exit45` 仍未修复 2026，本轮按 `biweekly_buffer` 回到双周等权缓冲，补一个 `soft_cashguard_exit45` 版本，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45,hkconnect_path2_equal_elastic_monthly_cashguard_v3,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover7_exit45`。
- `soft_cashguard_exit45` 五窗口 CAGR 为 `20.31% / 20.32% / 18.33% / 24.18% / -15.62%`，最大回撤 `-21.15% / -21.15% / -16.20% / -16.20% / -8.76%`，换手 `5.84x / 5.71x / 5.55x / 7.10x / 6.51x`；回撤接近双周成本守门，但收益和 2026 仍弱，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；robust 仍为 `weekly_overlay_soft`。收尾 guard 为 `pass`，HK all candidates `79/79 complete`。
- 最终 rotation 为 `stagnation_runs=7 / risk_overlay_cost / rotate`。下一轮 focus -> candidates 池从双周回到月频/周度 overlay 风控成本，第一条命令建议实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45`，五窗口 `--only-strategy-ids <hk_path1_risk_overlay_id>` 增量确认。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `weekly_overlay_cashguard` 把 2025 winner 切过去但 2026 仍负，本轮按 `monthly_weekly_overlay` 补 `soft + cashguard + exit45`，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit45`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit45,hkconnect_path2_inverse_elastic_monthly_cost_guard_v2,hkconnect_path3_theme_fast_weekly_cashguard_turnover20`。
- `soft_cashguard_exit45` 五窗口 CAGR 为 `22.30% / 27.12% / 30.06% / 42.95% / -9.45%`，最大回撤 `-25.23% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.98x / 4.02x / 3.57x / 3.45x / 3.67x`；2025 持平 cashguard，但 2017/2020/2023 弱于 `weekly_overlay_soft` 且 2026 未修复。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；robust 仍为 `weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- 收尾 guard 为 `pass`，HK all candidates `76/76 complete`；最终 rotation 为 `stagnation_runs=4 / biweekly_buffer / rotate`。下一轮 focus -> candidates 池回到双周缓冲，第一条命令建议实现 `hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45`，五窗口 `--only-strategy-ids <hk_path1_biweekly_id>` 增量确认。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `lowvol_cost_guard` 改善 2026 但牺牲长窗，最终 focus 继续 `monthly_weekly_overlay`。本轮补 `cashguard`，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard,hkconnect_path2_theme_monthly_cost_control_v2,hkconnect_path3_stable_weekly_equal_buffered_cashguard_turnover9`。
- `cashguard` 五窗口 CAGR 为 `21.63% / 26.19% / 29.44% / 42.95% / -9.45%`，最大回撤 `-25.94% / -13.51% / -13.36% / -13.36% / -10.91%`，换手 `4.02x / 4.00x / 3.56x / 3.45x / 3.67x`；2025 窗口强于旧月频锚点，但 2017/2020/2023 和 2026 不如 `weekly_overlay_soft`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 的 `since_2025_01` winner 切到 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard`；2017/2020/2023 与 robust 仍为 `monthly_equal_buffered_weekly_overlay_soft`，robust `meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- Guard 显示 HK all candidates `73/73 complete`，本轮未触发 evict；最终 rotation 为 `stagnation_runs=1 / monthly_weekly_overlay / continue`。下一轮 focus -> candidates 池比较 `cashguard` 的 2025 提升是否可保留且修复 2026，第一条命令建议实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit45` 并五窗口增量确认。

## 本轮执行计划（2026-05-20 13:58 CST）

- 上一轮 focus 已从双周现金防守转回 `monthly_weekly_overlay`；本轮新增低波周度 overlay 成本守门版本，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard,hkconnect_path2_equal_elastic_monthly_cost_guard_v2,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8`。
- `lowvol_cost_guard` 五窗口 CAGR 为 `20.46% / 25.98% / 31.24% / 34.73% / 6.49%`，最大回撤 `-20.45% / -8.47% / -6.80% / -6.80% / -6.73%`，换手 `3.55x / 3.48x / 3.23x / 3.86x / 4.90x`；2026 转正且回撤更浅，但 2017/2020/2023 收益低于 `weekly_overlay_soft`，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `hkconnect_path1_monthly_equal_buffered`；robust 仍为 `monthly_equal_buffered_weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- Guard 显示 HK all candidates `70/70 complete`，本轮未触发 evict；最终 rotation 为 `stagnation_runs=11 / monthly_weekly_overlay / rotate`。下一轮 focus -> candidates 池继续比较收益折损和 2026 防守，第一条命令建议实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard`，再用五窗口 `--only-strategy-ids <hk_path1_overlay_id>` 增量确认。

## 本轮执行计划（2026-05-20 05:20 CST）

- 上一轮提示为双周线的 2026 防守修复；本轮新增一个更强现金防守的双周等权缓冲候选，继续只作为 HK Path 1 观察，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_cashguard`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_cashguard,hkconnect_path2_breakout_cost_guard_biweekly_exit35,hkconnect_path3_theme_fast_weekly_defensive_turnover18`。
- `cashguard` 五窗口 CAGR 为 `19.82% / 19.75% / 17.76% / 24.18% / -15.62%`，最大回撤 `-21.23% / -21.23% / -16.20% / -16.20% / -8.76%`，换手 `5.50x-7.10x`；比上一轮 `cost_guard` 收益更低，2026 仍为负，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `hkconnect_path1_monthly_equal_buffered`；robust 仍为 `monthly_equal_buffered_weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- HK candidate_count 为 `67`，未触发 evict；收尾 guard 的 HK Path 1 rotation 为 `stagnation_runs=8 / risk_overlay_cost / rotate`。下一轮 focus -> candidates 池从双周回到月频/周度 overlay 成本，先测低波或更低风险暴露，不再继续加双周现金防守。
- 下一轮第一条命令建议先实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard` 与 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard` 后，用 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_ids>` 补跑。

## 本轮执行计划（2026-05-19 23:14 CST）

- 上一轮 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft` 成为 2017/2020/2023 winner 与 robust；本轮按最终 rotation 的 `biweekly_buffer` 补一个双周成本防守对照，继续不并入 A 股结论。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_cost_guard`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_cost_guard,hkconnect_path2_breakout_cost_guard_biweekly,hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。
- 新双周成本防守五窗口 CAGR 为 `21.45% / 21.96% / 20.68% / 24.18% / -15.62%`，最大回撤 `-21.03% / -21.03% / -16.20% / -16.20% / -8.76%`；比旧双周线更稳一点，但收益与 2026 观察窗仍不如月频 soft robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered`；robust 为 `monthly_equal_buffered_weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- HK candidate_count 为 `64/64 complete`，本轮未触发 evict；下一轮 focus -> candidates 池仍按 `biweekly_buffer`，优先测试双周线的 2026 防守修复而不是再扩月频 overlay。建议先实现 `hkconnect_path1_biweekly_equal_buffered_cashguard` 与 `hkconnect_path1_biweekly_equal_buffered_lowvol_cost_guard`，第一条命令继续用五窗口 `--only-strategy-ids`。

## 本轮执行计划（2026-05-19 17:26 CST）

- 本轮新增并用 `--only-strategy-ids` 五窗口补跑 3 个月频周度 overlay 变体：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_defensive`、`hkconnect_path1_monthly_lowvol_weekly_overlay_soft`；没有裸跑全量 HK。
- `soft` 版成为 2017/2020/2023 window winner 与 robust：2017 `24.96% CAGR / -24.94% MaxDD / 1.30 Sharpe / 3.40 Turn`，2020 `32.33% / -14.83% / 1.55 / 3.40`，2023 `34.60% / -14.83% / 1.73 / 3.13`；2025 仍由 `hkconnect_path1_monthly_equal_buffered` 保持 `40.41% CAGR`。
- `defensive` 版收益略低但接近，`lowvol_weekly_overlay_soft` 的 2026 短窗为正（`5.16% CAGR`）且回撤最浅，但 2017/2020/2023 收益弱于 `soft`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 robust candidate 切换为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=1 / monthly_weekly_overlay / continue`；下一轮优先比较 `soft` overlay 的 2026 防守缺口与 lowvol 版本的收益折损。

## 本轮执行计划（2026-05-19 11:12 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与三张 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 当前窗口指标为：2017 `24.03% CAGR / -23.59% MaxDD / 1.29 Sharpe / 3.09 Turn`，2020 `31.21% / -14.83% / 1.52 / 3.52`，2023 `33.85% / -14.79% / 1.69 / 2.87`，2025 `40.41% / -14.79% / 1.53 / 3.46`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=34 / risk_overlay_cost / rotate`；下一轮优先比较月频稳健线上的风险 overlay 成本和双周缓冲的 2026 短窗失效。

## 本轮执行计划（2026-05-19 05:29 CST）

- 本轮按 `biweekly_buffer` 轮换方向新增并增量补跑 `hkconnect_path1_biweekly_equal_buffered_wide_exit` 与 `hkconnect_path1_biweekly_equal_buffered_defensive`，命令使用 `--only-strategy-ids`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- 新 `wide_exit` 五窗口为：2017 `21.33% CAGR / -22.59% MaxDD / 1.03 Sharpe / 6.09 Turn`，2020 `24.54% / -21.18% / 1.08 / 5.91`，2023 `25.25% / -16.25% / 1.31 / 5.72`，2025 `25.74% / -16.25% / 1.15 / 7.64`，2026 `-15.06%`。
- 新 `defensive` 与 `wide_exit` 接近但略低，2017/2020/2023 CAGR 分别为 `20.83% / 23.79% / 24.38%`；两者均未替换月频稳健锚点。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 三张对比图；HK Path 1 tracked winners 未变：2017/2023/2025 `hkconnect_path1_monthly_equal_buffered`，2020 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 仍为 `stagnation_runs=32 / recommended_focus=biweekly_buffer / rotate`；下一轮继续比较双周缓冲的成本与 2026 年短窗失效。

## 本轮执行计划（2026-05-18 23:13 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 三张对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 当前窗口指标为：2017 `24.03% CAGR / -23.59% MaxDD / 1.29 Sharpe / 3.09 Turn`，2020 `31.21% / -14.83% / 1.52 / 3.52`，2023 `33.85% / -14.79% / 1.69 / 2.87`，2025 `40.41% / -14.79% / 1.53 / 3.46`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=30 / recommended_focus=biweekly_buffer / rotate`；下一轮优先比较双周缓冲与月频稳健线的交易成本和信号生效日。

## 本轮执行计划（2026-05-18 20:34 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 与部分 `hk_daily_adj` 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 三张对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=28 / recommended_focus=monthly_weekly_overlay / rotate`；下一轮优先比较月频稳健线上的周度 overlay 成本与信号生效日。

## 本轮执行计划（2026-05-18 11:11 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=23 / recommended_focus=biweekly_buffer / rotate`；下一轮优先比较双周缓冲与月频稳健线的交易成本。

## 本轮执行计划（2026-05-18 05:53 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=20 / recommended_focus=monthly_weekly_overlay / rotate`；下一轮继续比较月频稳健线上的周度 overlay 成本。

## 本轮执行计划（2026-05-17 23:12 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=18 / recommended_focus=monthly_weekly_overlay / rotate`；下一轮继续比较月频稳健线上的周度 overlay 成本。

## 本轮执行计划（2026-05-17 17:25 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=15 / recommended_focus=risk_overlay_cost / rotate`；下一轮优先比较月频稳健线上的风险 overlay 成本。

## 本轮执行计划（2026-05-17 11:15 CST）

- 本轮完整运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`；trade calendar 在线更新失败后回退本地缓存，HK coverage 收尾仍为 `44/44 complete / pass`。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与三张 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=12 / recommended_focus=biweekly_buffer / rotate`；下一轮优先比较双周缓冲与月频稳健线的真实交易成本和信号生效日。

## 本轮执行计划（2026-05-17 05:15 CST）

- 本轮完整运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`；trade calendar 在线更新失败后回退本地缓存，HK coverage 收尾仍为 `44/44 complete / pass`。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与三张 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=10 / recommended_focus=monthly_weekly_overlay / rotate`；下一轮继续比较月频稳健线上的周度 overlay 真实成本与信号生效日，不把纯周度换股并回 Path 1。

## 本轮执行计划（2026-05-16 23:12 CST）

- 本轮完整运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`；trade calendar 在线更新失败后回退本地缓存，HK coverage 收尾仍为 `44/44 complete / pass`。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与三张 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=8 / recommended_focus=risk_overlay_cost / rotate`；下一轮继续比较月频稳健线上的周度风险 overlay 成本与信号生效日。

## 本轮执行计划（2026-05-16 17:14 CST）

- 本轮完整运行 `.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，并用 `update_hkconnect_artifacts.py` 同步 tracked payload 与三张 HK 对比图。
- HK Path 1 tracked winners 未变：2017 `hkconnect_path1_monthly_equal_buffered`（`24.03% CAGR / -23.59% MaxDD / 1.29 Sharpe / 3.09 Turn`），2020 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% / -14.83% / 1.52 / 3.52`）。
- 2023 与 2025 winner 仍为 `hkconnect_path1_monthly_equal_buffered`，分别为 `33.85% / -14.79% / 1.69 / 2.87` 与 `40.41% / -14.79% / 1.53 / 3.46`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=6 / recommended_focus=risk_overlay_cost / rotate`；下一轮继续比较风险 overlay 成本，但 monthly equal buffered 仍是当前稳健锚点。

## 本轮执行计划（2026-05-16 11:20 CST）

- 本轮独立运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，trade calendar 在线更新失败后按计划回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- HK coverage 仍为 `44/44 complete / pass`，港股结论不并入 A 股 winner；月频数据截止日为 `2026-04-30`，周频观察线数据截止日为 `2026-05-15`。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=2 / recommended_focus=monthly_weekly_overlay / continue`；下一轮继续比较月频稳健线与周度 overlay 的真实成本，不把纯周度换股并回 Path 1。

## 本轮执行计划（2026-05-16 06:56 CST）

- 本轮独立运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `scripts/update_hkconnect_artifacts.py`；HK coverage 仍为 `44/44 complete / pass`，港股结论不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月频数据截止日为 `2026-04-30`，周频观察线数据截止日为 `2026-05-15`；本轮继续保留月频、双周与周度观察，但纯周度换股仍交给 HK Path 3。
- 收尾 rotation 为 `stagnation_runs=32 / recommended_focus=biweekly_buffer / rotate`；下一轮优先复核双周缓冲与月频稳健线的交易成本，而不是只扩月频邻域。

## 本轮执行计划（2026-05-15 15:16 CST）

- 本轮独立运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- HK coverage 收尾仍为 `pass / blocking=0 / warning=0`，港股结论继续不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 最终 rotation 为 `stagnation_runs=24 / recommended_focus=risk_overlay_cost / rotate`；下一轮优先评估月频稳健线上的周度风险 overlay 成本，而不是只扩双周缓冲。

## 本轮执行计划（2026-05-15 10:14 CST）

- 本轮独立运行港股五窗口回测，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`，HK coverage 最终仍为 `pass`，港股结论继续不并入 A 股。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`；最终 rotation 为 `stagnation_runs=22 / biweekly_buffer`。

## 本轮执行计划（2026-05-14 22:55 CST）

- 本轮已完整运行 `backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 并同步 `update_hkconnect_artifacts.py`，HK coverage 收尾仍为 `pass`，港股结论继续独立于 A 股。
- HK Path 1 tracked winners 当前为：2017 `hkconnect_path1_monthly_equal_buffered`（`24.03% CAGR / -23.59% MaxDD / 1.2852 Sharpe / 3.09 Turn`），2020 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% / -14.83% / 1.5210 / 3.52`），2023/2025 仍为 `monthly_equal_buffered`（`33.85% / 40.41% CAGR`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`；最终 guard 为 `stagnation_runs=18 / monthly_weekly_overlay`，下一轮继续比较月频稳健线与周度 overlay 的交易成本。

## 本轮执行计划（2026-05-14 15:10 CST）

- 本轮按独立港股线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后同步 `scripts/update_hkconnect_artifacts.py`。
- 收尾 guard 对 HK coverage 为 `pass`，港股候选 `44` 个五窗口完整；HK Path 1 rotation 为 `stagnation_runs=13 / recommended_focus=biweekly_buffer`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 下一轮按 `biweekly_buffer` 比较双周缓冲在真实信号生效日与交易成本下的稳定性；继续保留月频、双周与周度观察，但不把纯周度换股候选并回 Path 1。

## 本轮执行计划（2026-05-14 09:13 CST）

- 本轮按独立港股线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后同步 `scripts/update_hkconnect_artifacts.py`。
- 收尾 guard 对 HK coverage 为 `pass`，港股候选 `44` 个五窗口完整；HK Path 1 rotation 为 `stagnation_runs=11 / recommended_focus=monthly_weekly_overlay`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 下一轮继续在月频稳健线上比较周度 overlay 的真实成本与信号生效日，不把纯周度换股候选并回 Path 1。

## 本轮执行计划（2026-05-14 03:17 CST）

- 本轮继续离线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后同步 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03%`。
- 收盘 guard 将 HK Path 1 rotation 推进到 `stagnation_runs=9 / recommended_focus=monthly_weekly_overlay`；下一步继续比较月频稳健线上的周度 overlay 成本，不把纯周度换股候选并回 Path 1。

## 本轮执行计划（2026-05-13 21:21 CST）

- 本轮继续离线运行 HK 五窗口回测并同步 `scripts/update_hkconnect_artifacts.py`；`trade_calendar` 在线更新失败后使用本地缓存，港股 tracked payload 仍为 `as_of=2026-05-08`。
- 港股 Path 1 winner 身份未漂移：`since_2017_01 / since_2023_01 / since_2025_01` 仍为 `hkconnect_path1_monthly_equal_buffered`，`since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 最新指标为：2017 `24.03% CAGR / -23.59% MaxDD / 1.2852 Sharpe / 3.09 Turnover`；2020 `31.21% / -14.83% / 1.5210 / 3.52`；2023 `33.85% / -14.79% / 1.6907 / 2.87`；2025 `40.41% / -14.79% / 1.5271 / 3.46`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- rotation 已提示下一轮港股 Path 1 转向 `risk_overlay_cost`；继续保留月频、双周和周频观察，但不把港股结论并入 A 股 winner。

## 本轮执行计划（2026-05-13 09:13 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后继续回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日仍为 `2026-05-08`；本轮同步了 month-end preview 相关 live/export 产物，但 preview 不进入正式 winner 或 robust candidate 规则。

## 本轮执行计划（2026-05-13 03:32 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后继续回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；双周与周频候选继续保留，当前双周线未改写 tracked Path 1 winner。

## 本轮执行计划（2026-05-12 21:20 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；月度、双周与周度观察候选继续保留。

## 本轮执行计划（2026-05-12 09:12 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；月度、双周与周度观察候选继续保留。

## 本轮执行计划（2026-05-12 03:16 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；月度、双周与周度观察候选继续保留。

## 本轮执行计划（2026-05-11 21:22 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；月度、双周与周度观察候选继续保留，纯周度路线不回并到 Path 1 稳健线。

## 本轮执行计划（2026-05-11 15:15 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度、双周与周度观察候选继续保留；纯周度路线仍交给港股 Path 3，不回并到 Path 1 稳健线。

## 本轮执行计划（2026-05-11 09:19 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`。
- 月度、双周与周度观察候选继续保留；纯周度路线仍交给港股 Path 3，不回并到 Path 1 稳健线。

## 本轮执行计划（2026-05-11 03:13 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，纯周度候选继续交给港股 Path 3，不并入 A 股结论。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`。

## 本轮执行计划（2026-05-10 21:14 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，纯周度候选继续交给港股 Path 3，不并入 A 股结论。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`。

## 本轮执行计划（2026-05-10 15:04 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`，本轮 Path 1 身份未漂移；纯周度候选继续交给港股 Path 3，不并入 A 股结论。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`。

## 本轮执行计划（2026-05-10 09:17 CST）

- 本轮运行 `.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 tracked payload 和三张图表与上轮相比无文件漂移。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 继续只保留实盘稳健线的月度/双周候选，纯周度候选留在独立 Path 3。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`。
- 四窗口 robust candidate 仍是 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`；`since_2026_01` 继续只作为观察窗。

## 本轮执行计划（2026-05-10 03:16 CST）

- 本轮继续以港股三路径拆分口径运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后按计划回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 继续只保留实盘稳健线的月度/双周候选，纯周度候选留在独立 Path 3。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 本轮切到 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`，高于纯月度等权缓冲且仍保持稳健线口径。
- 四窗口 robust candidate 仍是 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`；`since_2026_01` 只观察，当前 Path 1 raw leader 是 `hkconnect_path1_biweekly_lowvol`（`24.45% CAGR / -1.95% MaxDD / 2.6064 Sharpe / 4.87 Turnover`）。

## 本轮执行计划（2026-05-09 21:14 CST）

- 本轮继续以港股三路径拆分口径运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- Path 1 继续只保留实盘稳健线的月度/双周候选；纯周度候选保持迁移到独立 Path 3。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01` 与四窗口 robust candidate 全部统一到 `hkconnect_path1_monthly_equal_buffered`。
- 关键指标：`since_2020_01` 为 `24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，`since_2023_01` 为 `33.85% / -14.79% / 1.6907 / 2.87`，`since_2025_01` 为 `40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2026_01` 只观察，当前 Path 1 raw leader 仍是 `hkconnect_path1_biweekly_lowvol`；本轮 HK Path 3 有新周频 winner，但不并回 Path 1。

## 本轮执行计划（2026-05-09 18:09 CST）

- 本轮继续以港股三路径拆分口径运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- Path 1 继续只保留实盘稳健线的月度/双周候选；原单周换股候选保持迁移到独立 Path 3。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01` 与四窗口 robust candidate 全部统一到 `hkconnect_path1_monthly_equal_buffered`。
- 关键指标：`since_2020_01` 为 `24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，`since_2023_01` 为 `33.85% / -14.79% / 1.6907 / 2.87`，`since_2025_01` 为 `40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2026_01` 只观察，当前 Path 1 raw leader 是 `hkconnect_path1_biweekly_lowvol`；下一轮继续围绕“月度调仓 + 周度风控/卫星”，不把纯周度 winner 并回稳健线。

## 本轮执行计划（2026-05-09 三路径拆分）

- 本轮将港股 Path 1 收窄为实盘稳健线：当前候选保留月度/双周稳健族，单周换股候选已迁移到独立 Path 3。
- 重新运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01` 与四窗口 robust candidate 全部统一到 `hkconnect_path1_monthly_equal_buffered`。
- 关键指标：`since_2020_01` 为 `24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，`since_2023_01` 为 `33.85% / -14.79% / 1.6907 / 2.87`，`since_2025_01` 为 `40.41% / -14.79% / 1.5271 / 3.46`。
- 下一轮 Path 1 的新增方向应围绕“月度调仓 + 周度风控/卫星”，而不是把纯周度 winner 重新并回稳健线。

## 本轮执行计划（2026-05-09 13:04 CST）

- 本轮按港股独立线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 继续为 `as_of=2026-05-08`；港股结论继续不并入 A 股 winner，公开快照继续区分数据截止日与真实信号/换股生效日。
- Path 1 `since_2017_01 / since_2020_01` winner 仍是低换手 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，样本截至 `2026-04-30`。
- `since_2023_01` 仍为 `hkconnect_path1_monthly_equal_buffered`，`33.85% CAGR / -14.79% MaxDD / 1.6907 Sharpe / 2.87 Turnover`；`since_2025_01` 仍为 `hkconnect_path1_weekly_equal_buffered`，`44.50% / -13.39% / 1.5761 / 13.14`。
- 四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=31.13% / minCAGR=23.36%`；月频、双周、周频与低波候选继续全部保留。

## 本轮执行计划（2026-05-09 05:08 CST）

- 本轮按港股独立线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 继续为 `as_of=2026-05-08`；港股结论继续不并入 A 股 winner，公开快照继续区分数据截止日与真实信号/换股生效日。
- Path 1 `since_2017_01 / since_2020_01` winner 仍是低换手 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，样本截至 `2026-04-30`。
- `since_2023_01` 仍为 `hkconnect_path1_monthly_equal_buffered`，`33.85% CAGR / -14.79% MaxDD / 1.6907 Sharpe / 2.87 Turnover`；`since_2025_01` 仍为 `hkconnect_path1_weekly_equal_buffered`，`44.50% / -13.39% / 1.5761 / 13.14`。
- 四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=31.13% / minCAGR=23.36%`；月频、双周、周频与低波候选继续全部保留。

## 本轮执行计划（2026-05-08 23:12 CST）

- 本轮按港股独立线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 同步为 `as_of=2026-05-08`；港股结论继续不并入 A 股 winner，公开快照继续区分数据截止日与真实信号/换股生效日。
- Path 1 `since_2017_01 / since_2020_01` winner 仍是低换手 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，样本仍截至 `2026-04-30`。
- `since_2023_01` 本轮切到 `hkconnect_path1_monthly_equal_buffered`（`33.85% CAGR / -14.79% MaxDD / 1.6907 Sharpe / 2.87 Turnover`），低换手与 Sharpe 优先于周频缓冲的更高换手收益。
- `since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，但更新到 `2026-05-08` 后为 `44.50% CAGR / -13.39% MaxDD / 1.5761 Sharpe / 13.14 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=31.13% / minCAGR=23.36%`。
- 月频、双周、周频与低波候选继续全部保留；本轮不因 2023 窗口月频胜出而停止高频路线观察。

## 本轮执行计划（2026-05-08 17:24 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=33.38% / minCAGR=24.37%`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分数据截止日与真实信号/换股生效日。

## 本轮执行计划（2026-05-08 13:15 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=33.38% / minCAGR=24.37%`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分数据截止日与真实信号/换股生效日。

## 本轮执行计划（2026-05-08 07:28 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=33.38% / minCAGR=24.37%`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分数据截止日与真实信号/换股生效日。

## 本轮执行计划（2026-05-07 23:12 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=33.38% / minCAGR=24.37%`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分数据截止日与真实信号/换股生效日。

## 本轮执行计划（2026-05-07 11:10 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分 `data_as_of=2026-05-06` 与港股真实信号/换股生效日。

## 本轮执行计划（2026-05-07 05:06 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 继续区分港股数据截止日与真实换股/信号生效日；月频、双周、周频与低波候选全部保留，不因长窗月频胜出而停止高频路线观察。

## 本轮执行计划（2026-05-06 23:15 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；港股 tracked payload 仍以 `as_of=2026-04-30` 记录，公开快照的缓存数据截止日与信号生效日分开保留。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，指标为 `24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 月频、双周、周频与低波候选继续保留；本轮不因长窗月频胜出而停止高频路线观察。

## 本轮执行计划（2026-05-06 11:35 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新仍失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录。
- Path 1 tracked winners 未较 06:14 记录漂移：`since_2017_01 / since_2020_01` 仍是低换手 `hkconnect_path1_monthly_equal_buffered`（`24.87% CAGR / -14.78% MaxDD / 1.4421 Sharpe / 2.80 Turnover`）。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`（分别为 `34.80% CAGR` 与 `48.95% CAGR`）；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 周频、双周、月频与低波候选全部保留；本轮是结果同步和 turnover 明细重写，不改变港股 Path 1 路线判断。

## 本轮执行计划（2026-05-06 06:14 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新仍失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录。
- Path 1 tracked winners 未较 00:04 记录漂移：`since_2017_01 / since_2020_01` 仍是低换手 `hkconnect_path1_monthly_equal_buffered`（`24.87% CAGR / -14.78% MaxDD / 1.4421 Sharpe / 2.80 Turnover`）。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`（分别为 `34.80% CAGR` 与 `48.95% CAGR`）；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 周频、双周、月频与低波候选全部保留；本轮只是数值级同步重跑，不改变港股 Path 1 路线判断。

## 本轮执行计划（2026-05-06 00:04 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- Path 1 继续评估月频、双周、周频与低波候选；港股 winner 结论不并入 A 股。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 tracked payload 判断是否只是同步重跑，或出现窗口赢家切换。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 tracked payload 仍为 `as_of=2026-04-30`。
- 本轮 Path 1 `since_2017_01 / since_2020_01` winner 从 `hkconnect_path1_weekly_equal_buffered` 切到低换手 `hkconnect_path1_monthly_equal_buffered`（`24.87% CAGR / -14.78% MaxDD / 1.4421 Sharpe / 2.80 Turnover`）。
- `since_2023_01 / since_2025_01` winner 继续是 `hkconnect_path1_weekly_equal_buffered`（分别为 `34.80% CAGR` 与 `48.95% CAGR`）；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 月频、双周、低波与周频候选继续保留为候选对照，不因为长窗月频切换而停止高频路线观察。

## 本轮补充计划与记录（2026-05-05 18:16 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- 月频、双周、低波候选继续保留为低换手和低回撤对照；港股 Path 1 结论不并入 A 股 winner。

## 本轮补充计划与记录（2026-05-05 12:14 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 继续保留月频、双周、周频与低波对照，不新增候选族，不把港股结论并入 A 股 winner。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。

## 本轮补充计划与记录（2026-05-05 06:14 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- 月频、双周、低波候选继续保留为低换手和低回撤对照；港股 Path 1 结论不并入 A 股 winner。

## 本轮补充计划与记录（2026-05-05 00:03 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 继续评估月频、双周、单周与低波候选；不新增候选族，不把港股结论并入 A 股 winner。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 tracked payload 确认是否只是同步重跑，或出现窗口赢家切换。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。

## 本轮补充计划与记录（2026-05-04 18:07 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 继续评估月频、双周、单周与低波候选；不新增候选族，不把港股结论并入 A 股 winner。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 tracked payload 确认是否只是同步重跑，或出现窗口赢家切换。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。

## 本轮补充计划与记录（2026-05-04 15:25 CST）

- 继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败时回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- 月频、双周、低波候选继续保留为低换手和低回撤对照；港股 Path 1 结论仍不并入 A 股 winner。

## 本轮补充计划（2026-05-04 06:45 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，以本地缓存完成五窗口评估。
- Path 1 仍只评估当前月频、双周、单周与低波对照候选，不新增候选族；港股结论不并入 A 股 winner。
- 跑完后用 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 tracked payload 判断是否只是同步重跑，或出现窗口赢家/robust candidate 切换。

### 本轮补充记录（2026-05-04 09:40 CST）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

## 本轮执行计划（2026-05-04）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-05-04 03:57 CST）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

## 本轮执行计划（2026-05-03）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-05-03 00:16 CST；06:11 CST 复核）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

### 本轮补充（2026-05-03 12:05 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 继续为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 仍全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标未漂移：`since_2017_01 / since_2020_01` 仍为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`；月频、双周、低波候选继续作为低换手和低回撤对照保留。

### 本轮补充（2026-05-03 18:13 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

## 本轮执行计划（2026-05-02）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-05-02）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标未漂移：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- `since_2026_01` 仍只作为观察窗；月频、双周、低波候选继续作为低换手和低回撤对照保留。

### 本轮补充（2026-05-02 06:07 CST）

- 重新运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- `results_hkconnect/tracked_winners_hkconnect.json` 与两张港股对比图重写后无实质 git diff；月频、双周、低波候选继续保留为低换手和低回撤对照。

### 本轮补充（2026-05-02 12:10 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

### 本轮补充（2026-05-02 18:08 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

## 本轮执行计划（2026-05-01）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-05-01）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时已回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，robust candidate 也保持同一策略。
- 关键指标未出现 winner 切换：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- `since_2026_01` 仍只作为观察窗；月频、双周、低波候选继续保留为对照，不因为当前单周等权缓冲胜出而移出。

### 本轮补充（2026-05-01 06:11 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标维持：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- 本轮港股 Path 1 没有窗口赢家切换；月频、双周、低波候选继续保留为换手和回撤对照。

### 本轮补充（2026-05-01 12:11 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标仍维持：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / -13.41% MaxDD / 1.5484 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `48.95% CAGR / -13.41% MaxDD / 1.7009 Sharpe / 12.98 Turnover`。
- `since_2026_01` 仍只作为观察窗，raw leader 继续是 `hkconnect_path1_weekly_lowvol`（`26.25% CAGR / -4.77% MaxDD / 1.6746 Sharpe / 5.25 Turnover`）；本轮不新增港股 Path 1 候选族。

### 本轮补充（2026-05-01 18:14 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标未漂移：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / -13.41% MaxDD / 1.5484 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `48.95% CAGR / -13.41% MaxDD / 1.7009 Sharpe / 12.98 Turnover`。
- `since_2026_01` 仍只作为观察窗；月频、双周、低波候选继续作为低换手和低回撤对照保留。

## 本轮执行计划（2026-04-30）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-04-30）

- 运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 1 四窗口 winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，robust candidate 也保持同一策略。
- 关键指标未出现 winner 切换：`since_2017_01 / since_2020_01` 为 `23.08% CAGR / -13.41% MaxDD / 1.2383 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `35.04% CAGR / -13.41% MaxDD / 1.5530 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `49.82% CAGR / -13.41% MaxDD / 1.7137 Sharpe / 13.03 Turnover`。
- `since_2026_01` 仍只作为观察窗；当前 Path 1 raw leader 是 `hkconnect_path1_weekly_lowvol`（`27.00% CAGR / -4.77% MaxDD / 1.6656 Sharpe / 5.33 Turnover`），不进入 tracked winners。本轮港股 tracked JSON 与港股对比图重写后没有实质 git diff，说明当前港股 Path 1 仍是确认性重跑。

### 本轮补充（2026-04-30 06:35 CST）

- 再次运行港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；`results_hkconnect/tracked_winners_hkconnect.json` 与港股 Path 1 图表重写后仍无实质 git diff。
- Path 1 四窗口 tracked winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，`since_2026_01` 仍只保留为观察窗；本轮没有把月频、双周或低波候选晋升为 tracked winner。
- 港股 Path 1 结论继续独立于 A 股，不并入 `winner_only_pass`；下一轮仍用 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照。

### 本轮补充（2026-04-30 12:12 CST）

- 再次运行港股五窗口回测：`./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- Path 1 四窗口 tracked winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，robust candidate 也保持同一策略；本轮港股 Path 1 没有窗口赢家切换。
- `since_2026_01` 继续只作为观察窗；月频、双周、低波候选继续保留为对照，不因为当前单周等权缓冲胜出而移出。

### 本轮补充（2026-04-30 18:16 CST）

- 再次完成港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；tracked payload 的数据截止日推进到 `as_of=2026-04-30`。
- Path 1 四窗口 tracked winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR`，`since_2025_01` 为 `48.95% CAGR`。
- `since_2026_01` 仍只作为观察窗，raw leader 继续是 `hkconnect_path1_weekly_lowvol`（`26.25% CAGR / -4.77% MaxDD / 1.6746 Sharpe / 5.25 Turnover`）；月频、双周、低波候选继续保留为对照。

## 上轮执行计划（2026-04-29）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 是 `hkconnect_path1_weekly_equal_buffered`，但继续把 `hkconnect_path1_monthly_equal_buffered` 与 `hkconnect_path1_monthly_lowvol` 作为低换手/低回撤对照，不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-04-29 12:09 CST）

- 运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 1 四窗口 winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标维持：`since_2017_01 / since_2020_01` 为 `23.08% CAGR / -13.41% MaxDD / 1.2383 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `35.04% CAGR / -13.41% MaxDD / 1.5530 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `49.82% CAGR / -13.41% MaxDD / 1.7137 Sharpe / 13.03 Turnover`。
- `since_2026_01` 仍只做观察窗；当前 Path 1 raw leader 是 `hkconnect_path1_weekly_lowvol`（`27.00% CAGR / -4.77% MaxDD / 1.6656 Sharpe / 5.33 Turnover`），不进入 tracked winners。

### 本轮快筛记录（2026-04-29 18:50 CST）

- 重新运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 1 四窗口 winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，robust candidate 也保持同一策略。
- 关键指标未出现可解释的 winner 切换：`since_2017_01 / since_2020_01` 仍为 `23.08% CAGR / -13.41% MaxDD / 1.2383 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `35.04% CAGR / -13.41% MaxDD / 1.5530 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `49.82% CAGR / -13.41% MaxDD / 1.7137 Sharpe / 13.03 Turnover`。
- 本轮 `results_hkconnect/**`、tracked JSON、港股对比图及 public/live 导出产生小幅同步 diff，主要来自候选明细指标漂移与公开快照 `data_as_of=2026-04-29` 更新；信号/换股生效日仍按真实周频或月频评估点保留。

## 上轮执行计划（2026-04-28）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 已切到 `hkconnect_path1_weekly_equal_buffered`，但需要继续把 `hkconnect_path1_monthly_equal_buffered` 与 `hkconnect_path1_monthly_lowvol` 作为低换手/低回撤对照，不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-04-28 00:08 CST）

- 运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 在线更新失败，已回退本地缓存。
- 运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 后，港股 Path 1 tracked payload 与图表没有新增 git diff。
- 当前四窗口 winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`；`sample_end` 仍为 `2026-03-31`，`robust_candidate` 仍是同一策略（meanCAGR `27.97% / minCAGR 21.77%`）。

### 本轮快筛记录（2026-04-28 12:04 CST）

- 重新运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 四窗口 winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`，`sample_end` 仍为 `2026-03-31`，`robust_candidate` 仍是同一策略（meanCAGR `27.97% / minCAGR 21.77%`）。
- 本次回测把 `02493.HK 缺少 hk_daily_adj 数据，已跳过。` 写入各港股 summary warning；这属于 `results_hkconnect/**` 研究产物同步，不代表 Path 1 winner 切换。

### 本轮快筛记录（2026-04-28 18:29 CST）

- 重新运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 四窗口 winner 从 `hkconnect_path1_monthly_equal_buffered` 切换为 `hkconnect_path1_weekly_equal_buffered`，robust candidate 同步切换到该策略。
- 新 Path 1 winner 的四窗口口径为：`since_2017_01 / since_2020_01` 均为 `23.08% CAGR / -13.41% MaxDD / 1.2383 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `35.04% CAGR / -13.41% MaxDD / 1.5530 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `49.82% CAGR / -13.41% MaxDD / 1.7137 Sharpe / 13.03 Turnover`。
- 这次改写显著提高 CAGR 并小幅改善回撤，但换手从月频主线的约 `2.9-3.6` 抬到 `9.7-13.0`；下一轮需要继续用 `monthly_equal_buffered / lowvol` 做换手与低回撤对照。

## 定位
- 独立于当前 A 股 Path 1
- 仅限沪港通标的（当前使用 Tushare `stock_hsgt` 最新可得名单作为静态池）
- 目标：先做出可解释、换手相对可控、窗口表现稳定的港股主线策略

## 当前假设
- 港股通标的中，月度动量 + 流动性质量 + 三档风险收缩，能形成相对稳健的收益曲线
- 纯粹把 A 股 winner_core 逻辑搬到港股未必有效，港股更需要：
  - 更重视流动性
  - 更宽的权重上限
  - 更直接的风险收缩

## 当前候选方向
1. 月度 / 双周 / 单周稳健（混合权重）
2. 月度 / 双周 / 单周熊市空仓
3. 月度 / 双周 / 单周等权缓冲
4. 月度 / 双周 / 单周低波偏稳

## 本轮迭代执行规则

- 沪港通 `Path 1` 作为**独立于 A 股**的研究线，每轮迭代都要单独评估，不并入 A 股 `winner_only_pass`。
- 默认回测窗口固定为：
  - `since_2017_01`
  - `since_2020_01`
  - `since_2023_01`
  - `since_2025_01`
  - `since_2026_01`（观察窗）
- 默认比较对象固定为当前 4 条港股 `Path 1` 候选主线，并同时比较月度 / 双周 / 单周调仓版本：
  - `hkconnect_path1_*_hybrid`
  - `hkconnect_path1_*_cashoff`
  - `hkconnect_path1_*_equal_buffered`
  - `hkconnect_path1_*_lowvol`
- 下一轮港股 `Path 1` 的主判定口径：
  - 更看重 `since_2020_01 / since_2023_01`
  - 重点指标：
    - `Total Return`
    - `CAGR`
    - `MaxDD`
    - `Sharpe`
    - `Turnover`
- 若港股 `Path 1` 任一窗口赢家发生变化，需同步更新：
  - `results_hkconnect/strategy_comparison_hkconnect.csv`
  - 实盘平台导出层中的沪港通策略注册表
  - README/HISTORY（若当前轮允许更新）

## 当前默认推进结论

- 当前港股 `Path 1` 默认主攻版本是：
  - `hkconnect_path1_weekly_equal_buffered`
- `monthly_equal_buffered / monthly_lowvol` 保留为低换手与低回撤对照。
- `monthly_cashoff` 保留为更防守的候选。
- `monthly_hybrid / monthly_lowvol` 继续作为对照，不轻易移出，直到多轮窗口表现明显失去竞争力。

## 近期优先看
- 2017 / 2020 / 2023 三个窗口的 CAGR、MaxDD、Sharpe
- 2026 观察窗是否出现过强的终点效应

## 已知限制
- 受 `stock_hsgt` 历史覆盖限制，当前不是严格的历史动态沪港通池，而是“最新可得名单静态池”
- 当前交易成本仍是近似模型，先用于研究排序，不用于精确实盘估值
- 若当前 Tushare key 无 `stock_hsgt` 权限，可手工提供 `data_cache/hkconnect/basic/stock_hsgt_manual.csv` 作为静态池输入

## 本轮快筛记录（2026-04-21 18:24）

- 运行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`
- 指标口径修正：`backtest_hkconnect.py` 现在会把 `sample_start` 对齐到**首个可执行调仓点**（避免“长时间无交易导致 CAGR 被错误年化”的窗口指标偏差）。
- 窗口赢家（按 `CAGR`，来源：`results_hkconnect/strategy_comparison_hkconnect.csv`）：
  - `since_2017_01`：`hkconnect_path1_monthly_equal_buffered`（CAGR `23.33%` / MaxDD `-22.36%` / Sharpe `1.1583`）
  - `since_2020_01`：`hkconnect_path1_monthly_equal_buffered`（CAGR `41.17%` / MaxDD `-19.79%` / Sharpe `1.5351`）
  - `since_2023_01`：`hkconnect_path1_monthly_equal_buffered`（CAGR `54.81%` / MaxDD `-0.07%` / Sharpe `3.5914`；该窗口目前实际可交易起点已后移至 `2025`）
  - `since_2025_01`：`hkconnect_path1_monthly_equal_buffered`（同上；与 `since_2023_01` 当前等价）
  - `since_2026_01`：观察窗调仓点不足，本轮全部跳过

## 本轮补充（2026-04-21 20:18）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论不变；`since_2026_01` 仍因调仓点不足全部跳过。

## 本轮补充（2026-04-21 22:20）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论不变；`since_2026_01` 仍因调仓点不足全部跳过（trade_calendar / hk_daily_adj 更新失败时自动回退本地缓存）。

## 本轮补充（2026-04-22）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论继续不变；`since_2026_01` 仍因调仓点不足全部跳过。
- 当前港股窗口的有效起点已稳定为：
  - `since_2017_01` → `2017-02-01`
  - `since_2020_01` → `2020-02-03`
  - `since_2023_01 / since_2025_01` → `2025-02-03`
- `hkconnect_path1_monthly_equal_buffered` 继续占据四窗口赢家：`2017 23.33% / 2020 41.17% / 2023 54.81% / 2025 54.81% CAGR`。
- `hkconnect_path1_monthly_lowvol` 仍值得保留为防守对照：在 `since_2020_01` 上有 `39.89% CAGR / -5.40% MaxDD / 2.0798 Sharpe`，但仍没有在 `CAGR` 上改写 `monthly_equal_buffered`。
- 下一轮继续把 `monthly_equal_buffered` 作为默认主攻版本，同时把 `monthly_lowvol` 固定为“压回撤 / 对照 Sharpe”的参考线；不新增 Path 1 候选族。
- 本次再次重跑后，`results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 仍完全对齐：四窗口 winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`；因此本轮不刷新 README / HISTORY / 港股对比图。
- `2026-04-22 06:27 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 与个别 `hk_daily_adj` 更新失败时继续自动回退本地缓存，窗口赢家与关键指标未出现漂移。
- 当日后续再次以离线缓存重跑同一命令后，`monthly_equal_buffered` 仍稳定占据 `2017 / 2020 / 2023 / 2025` 四窗口第一；`monthly_lowvol` 继续只作为“低回撤/高 Sharpe 对照线”保留，不晋升为主攻版本。
- 当日后续又完整重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，并执行 `.venv/bin/python scripts/update_hkconnect_artifacts.py` 后，港股 Path 1 的 tracked winner 仍未变化，但长窗口口径已进一步稳定到当前缓存基线：
  - `since_2017_01 / since_2020_01`：`hkconnect_path1_monthly_equal_buffered`，两窗当前都从 `2020-12-01` 起算，指标同为 `23.47% CAGR / -14.78% MaxDD / 1.3697 Sharpe / 2.88 Turnover`
  - `since_2023_01`：`34.37% CAGR / -14.78% MaxDD / 1.7044 Sharpe / 2.89 Turnover`
  - `since_2025_01`：`41.63% CAGR / -14.78% MaxDD / 1.5544 Sharpe / 3.47 Turnover`
- `since_2026_01` 原始比较行已不再缺失，但它仍只作为观察窗：当前 Path 1 raw leader 是 `hkconnect_path1_monthly_lowvol`，仅为 `-2.04% CAGR / -5.52% MaxDD / -0.0509 Sharpe / 3.10 Turnover`，说明港股 Path 1 的今年表现仍偏防守。
- `2026-04-22 14:30 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 与 `02940.HK` 更新失败时继续回退本地缓存，窗口赢家与关键指标未出现任何漂移。
- `results_hkconnect/strategy_comparison_hkconnect.csv` 仍与 `results_hkconnect/tracked_winners_hkconnect.json` 完全一致：`hkconnect_path1_monthly_equal_buffered` 继续占据 `2017 / 2020 / 2023 / 2025` 四窗口第一，`monthly_lowvol` 继续只保留为低回撤对照线。
- Path 1 自身窗口 winner 与关键指标本轮都未变化；后续只因 `Path 2 robust_candidate` 的 artifact 口径修正而同步刷新 README / HISTORY / 港股对比图。`Path 1` 本身继续把 `monthly_equal_buffered` 作为默认主攻版本。

## 本轮补充（2026-04-22 23:27 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 与 `02940.HK` 更新失败时继续回退本地缓存，窗口赢家与关键指标未出现漂移。
- 回测后 `results_hkconnect/strategy_comparison_hkconnect.csv` 的 SHA256 仍为 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f`，`tracked_winners_hkconnect.json` 的 SHA256 仍为 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明本轮没有新的港股 Path 1 artifact 漂移。
- 当前结论继续维持：`hkconnect_path1_monthly_equal_buffered` 仍是四窗口 tracked winner，`hkconnect_path1_monthly_lowvol` 仍只保留为低回撤对照与 `since_2026_01` 观察窗 raw leader。
- 下一轮继续只围绕 `monthly_equal_buffered` 与 `monthly_lowvol` 这条主攻/对照组合观察，不新增港股 Path 1 候选族，也不刷新 README / HISTORY / 图表。

## 本轮补充（2026-04-23 01:32 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `.venv/bin/python scripts/update_hkconnect_artifacts.py`：港股 Path 1 的 tracked winners 与关键指标继续完全不变。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明本轮只是确认性重跑，没有新的港股 Path 1 artifact 漂移。
- 当前四窗口 winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.47% CAGR / -14.78% MaxDD / 1.3697 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.37% CAGR / -14.78% MaxDD / 1.7044 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.63% CAGR / -14.78% MaxDD / 1.5544 Sharpe / 3.47 Turn`
- `since_2026_01` 观察窗 raw leader 继续是 `hkconnect_path1_monthly_lowvol`（`-2.04% CAGR / -5.52% MaxDD / -0.0509 Sharpe / 3.10 Turn`）。下一轮港股 `Path 1` 继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 对照，不新增候选族，也不把本轮重跑解读成新的胜负变化。

## 本轮补充（2026-04-23 03:33 CST）

- 本轮继续运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；`trade_calendar` 与个股 `hk_daily_adj` 仍全部走本地缓存回退路径，但回测完成且窗口赢家未出现漂移。
- 回测后 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明本轮港股 `Path 1` 仍是确认性重跑，而不是新的 winner 改写。
- 结论继续维持：`hkconnect_path1_monthly_equal_buffered` 仍稳住 `2017 / 2020 / 2023 / 2025` 四窗口，`hkconnect_path1_monthly_lowvol` 仍只保留为低回撤对照与 `since_2026_01` 观察窗 raw leader。下一轮不新增 `Path 1` 候选族。

## 本轮补充（2026-04-23 05:29 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 与全部 `hk_daily_adj` 继续因为网络受限而回退本地缓存，但回测完成且 Path 1 窗口赢家未出现任何漂移。
- 回测后再次执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`，`results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明这轮港股 Path 1 仍只是确认性重跑，没有新的 artifact drift。
- 当前结论继续维持：`hkconnect_path1_monthly_equal_buffered` 仍稳住 `2017 / 2020 / 2023 / 2025` 四窗口，`hkconnect_path1_monthly_lowvol` 仍只保留为低回撤对照与 `since_2026_01` 观察窗 raw leader。下一轮继续只保留这条主攻/对照组合，不新增港股 Path 1 候选族。

## 本轮补充（2026-04-23 19:59 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`：`trade_calendar` 与 `02940.HK` 继续走本地缓存回退路径，但港股 Path 1 回测完整完成。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 已更新为 `64b36ccb6a6e8e2f2f6aa58f90d7bcaceddfff1c4252add7e9d5312c84567283` 与 `e6a839d2c4315bbe0691ad4d52ddc697ebeb846652d5bc5c2662212e5b9f27b5`；这次变化来自 `sample_end` 前移到 `2026-04-23`，不是 Path 1 winner 改写。
- 当前四窗口 tracked winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.72% CAGR / -14.78% MaxDD / 1.3757 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.83% CAGR / -14.78% MaxDD / 1.7134 Sharpe / 2.89 Turn`
  - `since_2025_01`：`42.89% CAGR / -14.78% MaxDD / 1.5796 Sharpe / 3.47 Turn`
- `since_2026_01` raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`-3.57% CAGR / -5.52% MaxDD / -0.1460 Sharpe / 3.10 Turn`）。本轮 README / HISTORY / 港股对比图之所以刷新，是为了跟随港股 Path 2 的新 winner 一并同步；Path 1 自身继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 对照，不新增候选族。

## 本轮补充（2026-04-24）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 继续回退本地缓存，但港股 Path 1 的窗口赢家没有任何改写，实盘导出层也已同步到最新 tracked payload。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `a35621c7dfce801291e6c2482ef4a17a6071deeeb30a238adee9a34200bf98af` 与 `cc3c4429de9f026db201be9cee185fd388982488606045d104a1a59ddb938b72`；这轮变化来自重新生成完整 tracked payload 和图表，不是 Path 1 winner 切换。
- 当前四窗口 tracked winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.43% CAGR / -14.78% MaxDD / 1.3685 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.29% CAGR / -14.78% MaxDD / 1.7026 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.42% CAGR / -14.78% MaxDD / 1.5498 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.64% / minCAGR 23.43%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`-1.47% CAGR / -5.52% MaxDD / -0.0174 Sharpe / 3.10 Turn`）。
- 下一轮港股 `Path 1` 继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照，不新增候选族。

## 本轮补充（2026-04-25）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：本地 `trade_calendar` 更新仍失败并自动回退缓存，但这不影响港股 Path 1 的独立评估。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `893542dd28ae208a115a22d48f19bd1448bf2b30606892a825cb955aed7a3575` 与 `422d42394fa8731e51526973081debb58c6b537174485238018de37110589355`；这轮是同一 `sample_end=2026-04-24` 下的 metrics 漂移同步，不是新的 winner 切换。
- 当前四窗口 tracked winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.29% CAGR / -14.78% MaxDD / 1.3613 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.40% CAGR / -14.78% MaxDD / 1.7051 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.72% CAGR / -14.78% MaxDD / 1.5563 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.68% / minCAGR 23.29%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`1.41% CAGR / -5.52% MaxDD / 0.1367 Sharpe / 3.10 Turn`）。
- 本轮需要同步刷新 README / HISTORY 的港股摘要文字，但不新增港股 `Path 1` 候选族；下一轮仍只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照。

## 本轮补充（2026-04-26）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 在线更新继续失败，但离线缓存回退路径正常，港股 `Path 1` 独立评估未受阻。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `54097028c3eaea664cb74a26890358c0ff5934a75943a3b0c591655fc4c9efbc` 与 `6ee86d107dc61a23e9b0ef45b839507a34bca7f9a86139c0ee3cb365d0dfe2e8`；这轮仍是同一 `sample_end=2026-04-24` 下的 metrics 漂移同步，不是新的 `Path 1` winner 切换。
- 当前四窗口 tracked winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.32% CAGR / -14.78% MaxDD / 1.3625 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.40% CAGR / -14.78% MaxDD / 1.7051 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.72% CAGR / -14.78% MaxDD / 1.5563 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.69% / minCAGR 23.32%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`1.41% CAGR / -5.52% MaxDD / 0.1367 Sharpe / 3.10 Turn`）。
- 本轮只把 README 港股摘要、tracked payload 与港股对比图同步到当前数值，不新增港股 `Path 1` 候选族；下一轮继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照。

## 本轮补充（2026-04-27）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 在线更新依旧失败，但离线缓存回退路径继续正常，港股 `Path 1` 独立评估未受阻。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `54097028c3eaea664cb74a26890358c0ff5934a75943a3b0c591655fc4c9efbc` 与 `6ee86d107dc61a23e9b0ef45b839507a34bca7f9a86139c0ee3cb365d0dfe2e8`；这轮确认当前缓存口径的 `sample_end` 仍是 `2026-04-24`，不是新的 `2026-04-30` 样本扩展，也不是新的 `Path 1` winner 切换。
- 当前四窗口 tracked winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.32% CAGR / -14.78% MaxDD / 1.3625 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.40% CAGR / -14.78% MaxDD / 1.7051 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.72% CAGR / -14.78% MaxDD / 1.5563 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.69% / minCAGR 23.32%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`1.41% CAGR / -5.52% MaxDD / 0.1367 Sharpe / 3.10 Turn`）。
- 下一轮港股 `Path 1` 继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照，不新增候选族。

## 本轮补充（2026-04-27 09:08 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 在线更新仍失败，但离线缓存已经把港股 Path 1 payload 真正推进到 `sample_end=2026-04-30`。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 已更新为 `83885b39cb11f568d0ce2772e4cbaa9a0c6c1b62c089127e89eb39bbba12ceed` 与 `d5d3bc0cf9a03aeb713d76efd76d2687be6d0d47f65f784dcd12734bf1062d4f`；这说明上一条“仍停在 2026-04-24” 的判断已经过时。
- Path 1 四窗口 tracked winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`，但长窗口指标已按新的月末口径小幅漂移：
  - `since_2017_01 / since_2020_01`：`23.12% CAGR / -14.78% MaxDD / 1.3571 Sharpe / 2.89 Turn`
  - `since_2023_01`：`34.40% CAGR / -14.78% MaxDD / 1.7051 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.72% CAGR / -14.78% MaxDD / 1.5563 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.59% / minCAGR 23.12%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`1.41% CAGR / -5.52% MaxDD / 0.1367 Sharpe / 3.10 Turn`）。
- 下一轮港股 `Path 1` 继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照，不新增候选族。

## 本轮补充（2026-04-27 18:09 CST）

- 本轮在主工作树直接运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`。回测完整完成，但当前 tracked payload 的真实 `as_of` 仍是 `2026-04-24`，月频样本止于 `2026-03-31`，不是上一条记录里的 `2026-04-30` 口径。
- Path 1 四窗口 tracked winner 没有切换，继续全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`21.77% CAGR / -14.78% MaxDD / 1.2947 Sharpe / 2.91 Turn`
  - `since_2023_01`：`32.23% CAGR / -14.78% MaxDD / 1.6150 Sharpe / 2.93 Turn`
  - `since_2025_01`：`36.11% CAGR / -14.78% MaxDD / 1.3635 Sharpe / 3.60 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 27.97% / minCAGR 21.77%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`-27.91% CAGR / -5.52% MaxDD / -2.2545 Sharpe / 3.74 Turn`）。
- 本轮需要同步 README 与 tracked payload 来纠正港股摘要的 stale `2026-04-30` 数值；下一轮仍只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照，不新增港股 Path 1 候选族。
