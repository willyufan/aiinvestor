# 沪港通 Path 3 周度高频路径

## 本轮执行计划（2026-05-29 10:22 CST）

- 开局 guard 为 `pass`；上一轮 `defensive_turnover6_exit38` 仍未修复 2026，本轮按 `cost_stress` 在稳定周频低换手线上新增 `turnover5/exit42`，只在 HK 纯周度 Path 3 内比较。HK 缓存到 2026-05-27，`--end-date 2026-05-28` 准备保护失败后改用 `--end-date 2026-05-27`。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover5_exit42`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover5_exit42`。
- `turnover5_exit42` 五窗口 CAGR 为 `19.96% / 21.94% / 22.12% / 37.34% / -2.77%`，最大回撤为 `-29.56% / -19.73% / -11.73% / -11.15% / -9.89%`，换手为 `7.45x / 7.23x / 7.68x / 9.07x / 10.35x`。它较前一版继续降低换手且 2026 亏损收窄，但 2017/2023 不及稳定周频 robust，不能替换 tracked。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化，robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，下一轮 focus 为 `weekly_defensive_overlay`。第一条命令建议在本轮稳定周频低换手线上加防守 overlay，而不是回到高换手弹性线，并把 2026 是否转正作为验收，例如 `hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover5_exit40`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_overlay_next_id>`。

## 本轮执行计划（2026-05-29 04:17 CST）

- 开局 guard 为 `pass`；上一轮稳定周频 `cost_guard_turnover6_exit40` 降换手但 2026 仍负，本轮按 `weekly_defensive_overlay` 在同一稳定低换手线上新增防守版 `turnover6/exit38`，只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover6_exit38`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover6_exit38`。
- `stable_weekly_equal_buffered_defensive_turnover6_exit38` 五窗口 CAGR 为 `19.20% / 20.22% / 25.29% / 35.39% / -8.42%`，最大回撤为 `-27.24% / -23.48% / -11.57% / -11.57% / -10.78%`，换手为 `8.09x / 7.83x / 8.34x / 9.99x / 10.63x`。结果与 `turnover8_exit38` 同形，防守 overlay 仍未修复 2026，且长窗不及稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化，robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `163/163 complete`，下一轮 focus 为 `cost_stress`。第一条命令建议停止只加 defensive overlay，改做稳定周频成本压力/更宽出场对照，例如 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover5_exit42`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_cost_stress_next_id>`。

## 本轮执行计划（2026-05-28 22:19 CST）

- 开局 guard 为 `pass`；上一轮 plan 要求沿 `weekly_turnover_reduction` 继续压稳定周频低换手，本轮新增 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit40`，只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit40`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit40`。
- `stable_weekly_equal_buffered_cost_guard_turnover6_exit40` 五窗口 CAGR 为 `19.92% / 21.21% / 23.73% / 37.02% / -4.13%`，最大回撤为 `-27.46% / -22.55% / -11.70% / -10.84% / -9.69%`，换手为 `7.81x / 7.52x / 8.05x / 9.77x / 10.56x`。该组继续降低稳定周频换手，但 2026 仍为负，且 2023 未超过当前 robust，不替换 HK Path 3 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化，robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `160/160 complete`，下一轮 focus 为 `weekly_defensive_overlay`。第一条命令建议在本轮 turnover6 稳定周频线上加防守 overlay，而不是回到 15x+ 高弹性线，例如 `hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover6_exit38`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_overlay_next_id>`。

## 本轮执行计划（2026-05-28 16:18 CST）

- 开局 guard 为 `pass`；上一轮稳定周频低换手 `cost_guard_turnover8_exit40` 长窗较稳但 2026 仍负，本轮按 `weekly_defensive_overlay` 新增 `hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover8_exit38`，只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover8_exit38`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover8_exit38`。
- `stable_weekly_equal_buffered_defensive_turnover8_exit38` 五窗口 CAGR 为 `19.20% / 20.22% / 25.29% / 35.39% / -8.42%`，最大回撤为 `-27.24% / -23.48% / -11.57% / -11.57% / -10.78%`，换手为 `8.09x / 7.83x / 8.34x / 9.99x / 10.63x`。防守 overlay 仍没修复 2026，且 2017/2020 低于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化，robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `157/157 complete`，下一轮 focus 为 `weekly_turnover_reduction`。第一条命令建议停止在稳定低换手线上只加防守，改测更低 turnover 的稳定周频成本线，例如 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit40`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_turnover_reduction_next_id>`。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `theme_fast_weekly_cost_guard_turnover1_exit68` 降换手但仍弱于 stable robust，本轮按 `weekly_turnover_reduction` 转向稳定周频低换手分支，验证 `turnover8/exit40` 能否修复 2026。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit40`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `stable_weekly_equal_buffered_cost_guard_turnover8_exit40` 五窗口 CAGR 为 `19.90% / 20.90% / 25.47% / 33.94% / -9.52%`，最大回撤为 `-25.48% / -22.71% / -11.70% / -11.70% / -11.16%`，换手为 `8.20x / 7.92x / 8.42x / 10.14x / 10.64x`。该组长窗较稳且换手显著低于高弹性周频，但 2026 仍为负，不替换 HK Path 3 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化，robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，下一轮 focus 为 `weekly_defensive_overlay`。第一条命令建议在稳定低换手分支上加防守 overlay，而不是回到 15x+ 高弹性线，例如 `hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover8_exit38`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_overlay_next_id>`。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；上一轮 `theme_fast_weekly_cost_guard_turnover1_exit66` 降低换手但仍不改善 robust，本轮按 `cost_stress` 在同一低 turnover 高弹性周频线上放宽到 `exit68`。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit68`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover1_exit68` 五窗口 CAGR 为 `15.35% / 16.32% / 15.97% / 50.04% / 22.03%`，最大回撤为 `-35.40% / -26.31% / -24.75% / -14.59% / -8.26%`，换手为 `14.91x / 14.67x / 16.16x / 19.50x / 18.32x`。它较 `exit66` 小幅改善收益与换手，但 2017/2020/2023 收益、回撤和 15x+ 换手仍弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化，robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 转为 `weekly_turnover_reduction`。第一条命令建议不要继续只放宽 exit，转向稳定周频低换手分支修复 2026，例如 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit40`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_turnover_reduction_next_id>`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`；上一轮 `theme_fast_weekly_cost_guard_turnover2_exit64` 继续降低换手但不改善 robust，本轮按 `weekly_turnover_reduction` 进一步压到 `turnover1/exit66`，仍只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit66`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover1_exit66` 五窗口 CAGR 为 `13.55% / 15.92% / 15.80% / 49.93% / 20.85%`，最大回撤为 `-36.16% / -26.94% / -25.11% / -14.63% / -8.44%`，换手为 `15.61x / 15.31x / 16.70x / 20.25x / 18.86x`。它相对 `turnover2_exit64` 同时降低换手并略改善收益，但长窗回撤和 15x+ 换手仍弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化，robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 已轮换为 `cost_stress`。第一条命令建议不要继续只加 defensive overlay，先在本轮低 turnover 高弹性周频上做更宽退出的成本压力对照，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit68`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_cost_stress_next_id>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮建议沿 `cost_stress` 测 `turnover2_exit64`，本轮新增 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit64`，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit64`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v6,hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit64`。
- `theme_fast_weekly_cost_guard_turnover2_exit64` 五窗口 CAGR 为 `13.01% / 15.68% / 13.98% / 45.57% / 18.08%`，最大回撤 `-35.66% / -27.13% / -26.56% / -16.53% / -9.00%`，换手 `16.71x / 16.43x / 17.63x / 21.59x / 20.25x`。它继续降低高弹性周频换手并保持 2026 正收益，但 2017/2020/2023 收益与回撤仍弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，四窗口 meanCAGR `24.18%`、minCAGR `21.88%`、worstMaxDD `-24.83%`、meanTurn `9.58x`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 转为 `weekly_turnover_reduction`。第一条命令建议继续压高弹性周频换手上限并记录收益牺牲，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit66`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_turnover_reduction_next_id>`。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮 `theme_fast_weekly_defensive_turnover3_exit60` 仍有约 `18x-24x` 换手，本轮按 `weekly_turnover_reduction` 新增 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit62`，继续只在 HK 纯周度 Path 3 内比较。实际 HK 合并命令见 HK Path 1 本轮记录。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit62`。五窗口 CAGR 为 `12.57% / 14.87% / 12.22% / 40.68% / 15.70%`，最大回撤 `-35.43% / -27.07% / -25.64% / -15.37% / -8.75%`，换手 `17.63x / 17.31x / 18.48x / 22.72x / 21.66x`。它进一步降低高弹性周频换手并保持 2026 正收益，但 2017/2020/2023 收益和回撤仍弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，四窗口 meanCAGR `24.18%`、minCAGR `21.88%`、worstMaxDD `-24.83%`、meanTurn `9.58x`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `cost_stress`。下一轮第一条命令建议继续在高弹性周频低 turnover 线上做成本压力，而不是再单纯加防守 overlay，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit64`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_cost_stress_next_id>`。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；上一轮建议在低 turnover 高弹性周频上加 defensive overlay，本轮新增 `hkconnect_path3_theme_fast_weekly_defensive_turnover3_exit60`，继续只在 HK 纯周度 Path 3 内比较。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_defensive_turnover3_exit60`。五窗口 CAGR 为 `13.32% / 16.20% / 13.42% / 34.89% / 14.45%`，最大回撤 `-35.56% / -27.72% / -22.98% / -17.28% / -8.64%`，换手 `18.66x / 18.23x / 19.42x / 23.95x / 22.35x`。它保持 2026 正收益，并把高弹性周频换手压到约 `18x-24x`，但长窗收益/回撤仍弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `weekly_turnover_reduction`。下一轮第一条命令建议继续压高弹性周频 turnover，而不是再只加 defensive overlay，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit62`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_turnover_reduction_next_id>`。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮稳定周频防守线仍未修复 2026，本轮按 `cost_stress` 回到高弹性周频成本守门，并把 `turnover` 压到 `3`、退出放宽到 `60`，继续只在 HK 纯周度 Path 3 内比较。命令类型为 HK 五窗口 `--only-strategy-ids` 增量确认，实际合并命令见 HK Path 1 本轮记录。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover3_exit60`。五窗口 CAGR 为 `13.56% / 16.73% / 13.25% / 34.89% / 14.45%`，最大回撤 `-35.88% / -27.72% / -22.98% / -17.28% / -8.64%`，换手 `18.72x / 18.28x / 19.48x / 23.95x / 22.35x`。
- 该候选把 2026 保持为正并把高弹性周频换手压低到约 `18x-24x`，但 2017/2020/2023 收益和回撤仍弱于稳定周频 robust，不能替换 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `weekly_defensive_overlay`。下一轮第一条命令建议在本轮低 turnover 高弹性周频上加防守 overlay，而不是再单纯压 turnover，例如 `hkconnect_path3_theme_fast_weekly_defensive_turnover3_exit60`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_overlay_next_id>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮稳定周频成本线 `cost_guard_turnover10_exit38` 长窗较稳但 2026 仍负，本轮按 `weekly_defensive_overlay` 新增 `hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover10_exit36`，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover10_exit36`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `stable_weekly_equal_buffered_defensive_turnover10_exit36` 五窗口 CAGR 为 `19.17% / 20.23% / 25.29% / 35.39% / -8.42%`，最大回撤 `-27.27% / -23.48% / -11.57% / -11.57% / -10.78%`，换手 `8.10x / 7.85x / 8.34x / 9.99x / 10.63x`。防守 overlay 没能修复 2026，且 2017/2020 稳定性弱于当前 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `cost_stress`。下一轮第一条命令建议停止只在低换手稳定线修 2026，回到高弹性周频的低成本边界，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover3_exit60`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_cost_stress_next_id>`，并重点记录 2026 正收益是否足以抵消高换手与长窗回撤代价。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮高弹性周频 `turnover4 / exit58` 仍有接近 `20x` 的换手且收益弱，本轮按 `cost_stress` 回到稳定周频低换手成本线，新增 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38`。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `stable_weekly_equal_buffered_cost_guard_turnover10_exit38` 五窗口 CAGR 为 `19.71% / 20.79% / 25.73% / 35.39% / -8.42%`，最大回撤 `-26.32% / -23.39% / -11.57% / -11.57% / -10.78%`，换手 `8.06x / 7.83x / 8.34x / 9.99x / 10.63x`。它长窗较稳、换手显著低于高弹性周频，但 2026 仍负，不能替换现有 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `weekly_defensive_overlay`。下一轮第一条命令建议继续围绕稳定周频修复 2026，而不是回到 20x 高换手线，例如 `hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover10_exit36` 或同等低换手防守版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_overlay_next_id>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `turnover5 / exit56` 换手仍在 `20x+` 且收益/回撤弱于稳定周频 robust；本轮按 `weekly_turnover_reduction` 继续压到 `turnover4 / exit58`，只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover4_exit58`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover4_exit58` 五窗口 CAGR 为 `13.91% / 17.05% / 12.49% / 33.69% / 13.50%`，最大回撤 `-36.73% / -26.89% / -23.80% / -16.92% / -9.09%`，换手 `19.84x / 19.44x / 20.61x / 25.18x / 23.78x`。它略降换手但仍接近 `20x`，同时 2023/2025 收益更弱，不改善 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `cost_stress`。下一轮第一条命令建议停止只压 `turnover`，改回稳定周频或加现金防守的成本压力对照，例如 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_cost_stress_next_id>`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `cost_stress`；本轮在高弹性周频成本守门线上继续压到 `turnover5 / exit56`，只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover5_exit56`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover5_exit56` 五窗口 CAGR 为 `13.30% / 16.43% / 14.08% / 38.62% / 17.02%`，最大回撤 `-37.01% / -26.99% / -23.58% / -17.21% / -8.40%`，换手 `20.24x / 19.78x / 20.97x / 25.60x / 24.35x`。换手较旧高弹性线下降但仍在 `20x+`，长窗收益/回撤不如稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 为 `weekly_turnover_reduction`。下一轮第一条命令建议不要继续只放宽 exit，改测更低 turnover 或回到稳定线修复 2026，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover4_exit58`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_turnover_reduction_next_id>`。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `weekly_defensive_overlay`；本轮在 `turnover6/exit54` 低换手高弹性周频上加入 defensive overlay，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_defensive_turnover6_exit54`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_defensive_turnover6_exit54` 五窗口 CAGR 为 `12.79% / 15.96% / 15.07% / 43.43% / 14.81%`，最大回撤 `-37.35% / -26.86% / -24.48% / -17.18% / -9.54%`，换手 `20.88x / 20.37x / 21.37x / 26.22x / 24.99x`。它较早期高弹性周频降了换手，但长窗收益/回撤仍弱于稳定周频 robust，且 20x+ 换手成本压力仍高。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；候选池未触发 HK explore cap evict。
- 下一轮 focus 转为 `cost_stress`。下一轮第一条命令建议继续压高弹性周频的成本边界，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover5_exit56`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_cost_stress_next_id>`。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass`，上一轮要求继续压高弹性周频换手到 `turnover6/exit54`；本轮新增低换手成本守门版本，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover6_exit54`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover6_exit54` 五窗口 CAGR 为 `12.81% / 16.16% / 14.93% / 43.43% / 14.81%`，最大回撤 `-37.79% / -26.86% / -24.48% / -17.18% / -9.54%`，换手 `20.84x / 20.31x / 21.34x / 26.22x / 24.99x`。它把高弹性周频换手继续降到约 `20x-26x`，但收益/回撤更弱，仍不如稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `weekly_defensive_overlay`。下一轮第一条命令建议在本轮 `turnover6/exit54` 上只加 defensive overlay 复核，而不是继续压换手，例如 `hkconnect_path3_theme_fast_weekly_defensive_turnover6_exit54`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_overlay_next_id>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass`，上一轮 `theme_fast_weekly_cost_guard_turnover8_exit52` 仍有 22x-28x 年化换手；本轮按 `weekly_turnover_reduction` 在同一低换手形态上加 defensive overlay，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_defensive_turnover8_exit52`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light,hkconnect_path2_theme_monthly_high_return_cost_control_v2,hkconnect_path3_theme_fast_weekly_defensive_turnover8_exit52`。
- `theme_fast_weekly_defensive_turnover8_exit52` 五窗口 CAGR 为 `14.86% / 19.50% / 20.21% / 45.63% / 14.87%`，最大回撤 `-37.49% / -28.47% / -22.59% / -17.93% / -8.34%`，换手 `22.42x / 21.88x / 22.86x / 28.14x / 26.86x`。它维持 2026 正收益并略低于旧 24x-29x 换手，但收益/回撤仍弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 为 `weekly_turnover_reduction`。下一轮第一条命令建议继续压高弹性周频换手到 `turnover6/exit54` 或回到稳定线的 2026 修复，而不是再只加 defensive overlay，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover6_exit54`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_turnover_reduction_id>`。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass`，上一轮 `theme_fast_weekly_defensive_turnover10_exit50` 仍有约 24x-29x 年化换手；本轮按 `weekly_turnover_reduction` 继续压到 `turnover8 / exit52`，只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover8_exit52`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover8_exit52` 五窗口 CAGR 为 `14.91% / 19.70% / 20.17% / 45.63% / 14.87%`，最大回撤 `-37.76% / -28.47% / -22.59% / -17.93% / -8.34%`，换手 `22.37x / 21.80x / 22.81x / 28.14x / 26.86x`。它相对 turnover10 略降换手且 2026 仍正，但收益/回撤仍弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`。候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `weekly_defensive_overlay`。下一轮第一条命令建议在本轮更低换手形态上加 defensive overlay，而不是继续只压 turnover，例如 `hkconnect_path3_theme_fast_weekly_defensive_turnover8_exit52`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_next_id>`。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass`，上一轮 `theme_fast_weekly_cost_guard_turnover10_exit50` 保持 2026 正收益但 23x+ 换手和长窗回撤仍高；本轮按 `weekly_defensive_overlay` 在同一高弹性周频低换手形态上加入 defensive overlay，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_defensive_turnover10_exit50`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path2_theme_monthly_high_return_lowturn_reconfirm,hkconnect_path3_theme_fast_weekly_defensive_turnover10_exit50`。
- `theme_fast_weekly_defensive_turnover10_exit50` 五窗口 CAGR 为 `15.95% / 21.41% / 22.47% / 51.93% / 13.49%`，最大回撤 `-41.93% / -28.93% / -22.94% / -14.71% / -8.06%`，换手 `23.94x / 23.04x / 23.89x / 28.92x / 27.89x`。它保持 2026 为正，但换手仍约 `24x-29x`，2017/2020 回撤仍明显弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked payload 与图表同步；2017 window winner 与 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`，本轮候选未改变 winner/robust。
- 候选池未触发 HK explore cap evict。最终 guard 下一轮 focus 为 `weekly_turnover_reduction`；下一轮第一条命令建议继续压高弹性周频换手，而不是只加 defensive overlay，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover8_exit52` 或同等更低换手版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_turnover_reduction_id>`。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass`，上一轮低换手稳定线 `defensive_turnover9_exit42` 仍不能修复 2026；本轮按 `cost_stress` 回到高弹性周频，并把成本守门进一步压到 `turnover10 / exit50`，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover10_exit50`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover10_exit50` 五窗口 CAGR 为 `16.03% / 21.61% / 22.30% / 51.93% / 13.49%`，最大回撤 `-41.96% / -28.93% / -22.94% / -14.71% / -8.06%`，换手 `23.87x / 22.94x / 23.85x / 28.92x / 27.89x`。它保持 2026 为正且相对 25x+ 周频略降换手，但 2017/2020 回撤与 23x+ 换手仍弱于稳定周频 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked payload 与图表同步；2017 window winner 与 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`，本轮候选未改变 winner/robust。
- 候选池未触发 HK explore cap evict。收尾 guard 下一轮 focus 为 `weekly_defensive_overlay`；下一轮第一条命令建议在本轮 `turnover10_exit50` 上加防守 overlay 或 cashguard，而不是继续单纯压 turnover，例如 `hkconnect_path3_theme_fast_weekly_defensive_turnover10_exit50`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_next_id>`。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass`，上一轮建议从 25x 高换手周频转向低换手稳定线的 2026 修复；本轮新增防守型低换手稳定周频版本，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover9_exit42`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `stable_weekly_equal_buffered_defensive_turnover9_exit42` 五窗口 CAGR 为 `19.86% / 21.10% / 25.69% / 35.63% / -9.85%`，最大回撤 `-26.24% / -22.76% / -11.41% / -11.41% / -11.25%`，换手 `8.14x / 7.87x / 8.36x / 9.99x / 10.64x`。它保持约 8-10x 换手和浅长窗回撤，但 2026 仍为负，未能修复低换手稳定线短窗失效。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked payload 与图表同步；2017 window winner 与 robust candidate 当前为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`。本轮候选未改变 winner/robust。
- 候选池未触发 HK explore cap evict。收尾 focus 转向 `cost_stress`；下一轮第一条命令建议不要继续只在低换手负 2026 线上加防守，回到高弹性周频做成本压力，例如 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover10_exit50` 或同等更低换手版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_cost_stress_next_id>`。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass`，上一轮 `cost_guard_turnover12_exit48` 仍有 24x+ 年化换手和深长窗回撤；本轮按 `weekly_defensive_overlay` 在同一低换手高弹性形态上加入 defensive overlay，继续只在 HK 纯周度 Path 3 内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_defensive_turnover12_exit48`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_defensive_turnover12_exit48` 五窗口 CAGR 为 `15.51% / 21.71% / 23.93% / 54.69% / 8.29%`，最大回撤 `-41.36% / -34.06% / -22.31% / -15.41% / -9.13%`，换手 `24.95x / 23.86x / 24.55x / 29.85x / 29.19x`。它保持 2026 为正，但长窗回撤和高换手仍明显弱于低换手稳定线。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked payload 与图表同步：2017 window winner 与 robust candidate 当前为 `hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`，robust `meanCAGR=24.18% / minCAGR=21.88% / worstMaxDD=-24.83% / meanTurn=9.58x`；2020/2023 仍为 `theme_fast_weekly_buffered`，2025 仍为 `theme_fast_weekly_turnover_guard`。
- 候选池未触发 HK explore cap evict。收尾 guard 给出下一轮 focus `weekly_defensive_overlay`；下一轮不要继续在 25x 换手附近只加防守，第一条命令建议测试一个低换手稳定线的 2026 修复对照，例如 `hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover9_exit42`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_next_id>`。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass`，上一轮高弹性周频 `turnover16_exit45` 仍在 25x+ 年化换手附近；本轮按 `weekly_turnover_reduction` 把成本守门压到 `turnover12_exit48`，继续只在 HK 纯周度 Path 3 比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover12_exit48`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover12_exit48` 五窗口 CAGR 为 `15.43% / 21.64% / 23.64% / 54.69% / 8.29%`，最大回撤 `-41.48% / -34.06% / -22.31% / -15.41% / -9.13%`，换手 `24.78x / 23.65x / 24.42x / 29.85x / 29.19x`。较高弹性版本略降换手并保持 2026 为正，但长窗回撤和 24x+ 换手仍不达 robust 标准。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 为 `theme_fast_weekly_buffered`，2025 为 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`，`meanCAGR=26.69% / minCAGR=21.96% / worstMaxDD=-26.67% / meanTurn=10.50x`。
- 候选池未触发 HK explore cap evict。收尾 guard 给出下一轮 focus `weekly_defensive_overlay`；第一条命令建议不要继续只压 turnover，而是在本轮低换手高弹性版本上加防守 overlay，测试 `hkconnect_path3_theme_fast_weekly_defensive_turnover12_exit48` 或 cashguard 同型，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_turn12_id>`。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass`，上一轮低换手稳定线仍未修复 2026；本轮按 `cost_stress` 回到高弹性周频，但把成本守门从 `turnover14_exit45` 调到 `turnover16_exit45`，继续只在 HK 纯周度路径内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover16_exit45`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_fast_weekly_cost_guard_turnover16_exit45` 五窗口 CAGR 为 `14.96% / 21.81% / 24.57% / 58.31% / 13.00%`，最大回撤 `-42.53% / -36.29% / -22.10% / -15.01% / -8.39%`，换手 `25.79x / 24.68x / 25.48x / 31.25x / 31.17x`。2026 继续为正且 2025 弹性尚可，但长窗回撤和 25x+ 换手仍不达 robust 标准。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 为 `theme_fast_weekly_buffered`，2025 为 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`，`meanCAGR=26.69% / minCAGR=21.96% / worstMaxDD=-26.67% / meanTurn=10.50x`。
- 候选池未触发 HK explore cap evict。收尾 guard 的下一轮 focus 为 `weekly_turnover_reduction`；第一条命令建议不要继续在 25x 换手附近微调，先测试 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover12_exit48` 或同等更低换手版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_turnover_reduction_id>`。

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass`，上一轮 `theme_fast_weekly_cost_guard_turnover14_exit45` 修复 2026 但换手仍在 `25x-31x`；本轮按下一步回到稳定低换手周频线，测试 `turnover9_exit40` 是否能在约 `10x` 换手下改善 2026。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover9_exit40`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `turnover9_exit40` 五窗口 CAGR 为 `20.30% / 21.60% / 26.20% / 35.60% / -9.80%`，最大回撤 `-25.30% / -22.60% / -11.40% / -11.40% / -11.30%`，换手 `8.12x / 7.86x / 8.36x / 9.99x / 10.64x`；换手达标且长窗回撤可控，但 2026 仍为负，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；候选池未触发 HK explore cap evict。
- 下一轮 focus -> candidates 池切到 `weekly_defensive_overlay`，低换手稳定线连续无法修复 2026。第一条命令建议回到高弹性周频但加防守 overlay，测试 `hkconnect_path3_theme_fast_weekly_defensive_turnover16_exit45` 或 `hkconnect_path3_theme_fast_weekly_cashguard_turnover16_exit45`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_weekly_defensive_id>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass`，上一轮 `theme_fast_weekly_cost_guard_turnover18_exit42` 把 2026 转正但 25x-32x 换手与长窗回撤仍偏高；本轮按 `cost_stress`/低换手检查，把高弹性周频的 cap 和买卖阈值继续放松到 `turnover14_exit45`。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover14_exit45`。实际命令见 HK Path 1 本轮合并命令。
- `theme_fast_weekly_cost_guard_turnover14_exit45` 五窗口 CAGR 为 `15.03% / 21.87% / 24.70% / 57.43% / 13.24%`，最大回撤 `-42.29% / -36.31% / -22.07% / -14.97% / -8.36%`，换手 `25.85x / 24.68x / 25.44x / 31.22x / 31.17x`；相对上一轮 2020/2023/2025 略好，但换手仍未降下来，robust 仍不如稳定周频成本线。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`。候选池未触发 cap evict。
- 下一轮 focus -> candidates 池：高弹性周频已证明能修复 2026 但换手难降，第一条命令建议回到稳定周频线测试 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover9_exit40`，检查更窄退出能否修复 2026，同时保持 `10x` 左右换手；五窗口 `--only-strategy-ids <hk_path3_stable_turnover9_exit40_id>`。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 指向 `weekly_defensive_overlay`；上一轮低换手稳定线继续 2026 负收益，本轮回到高弹性周频并加成本守门，继续只作为 HK 纯周度 Path 3 比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cost_guard_turnover18_exit42`。实际命令见 HK Path 1 本轮合并命令。
- `theme_fast_weekly_cost_guard_turnover18_exit42` 五窗口 CAGR 为 `14.47% / 20.80% / 23.52% / 52.38% / 12.46%`，最大回撤 `-42.74% / -37.41% / -22.07% / -16.24% / -8.36%`，换手 `25.95x / 24.91x / 25.79x / 31.73x / 31.14x`；2026 转正但长窗回撤和 25x-32x 换手仍过高，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`。
- 候选池未触发 cap evict；本轮确认高弹性周频可以修复 2026 方向，但代价仍是长窗回撤和交易成本。
- 收尾 guard 后 HK Path 3 rotation 仍指向 `cost_stress`。下一轮第一条命令建议实现 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover14_exit45`，用更低换手和更宽出场检查是否能保留 2026 正收益，同时降低 2017/2020 回撤；五窗口 `--only-strategy-ids <hk_path3_turnover14_exit45_id>`。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `turnover7_exit45` 降换手但 2026 仍负，本轮继续沿稳定周频成本守门线，测试更窄退出缓冲 `turnover8_exit42`。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit42`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit42`。
- 该候选五窗口 CAGR 为 `19.90% / 20.90% / 25.47% / 33.94% / -9.52%`，最大回撤 `-25.48% / -22.71% / -11.70% / -11.70% / -11.16%`，换手 `8.20x / 7.92x / 8.42x / 10.14x / 10.64x`；比 `turnover7_exit45` 的 2026 略好，但仍为负且收益不够，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；HK Path 3 不并入 Path 1/2 月频结论。
- 下一轮 focus -> candidates 池：低换手稳定线已经连续 2026 负收益，第一条命令建议回到高弹性周频但限制成本，测试 `hkconnect_path3_theme_fast_weekly_cost_guard_turnover18_exit42`，五窗口 `--only-strategy-ids <hk_path3_next_weekly_cost_id>`。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `theme_fast_weekly_cashguard_turnover20` 虽把 2026 转正但长窗回撤和约 25-32x 换手仍高，本轮按 `weekly_turnover_reduction` 回到稳定周频低换手线，补 `turnover7_exit45`。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover7_exit45`。实际命令与 HK Path 1/2 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45,hkconnect_path2_equal_elastic_monthly_cashguard_v3,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover7_exit45`。
- `turnover7_exit45` 五窗口 CAGR 为 `20.16% / 21.81% / 25.44% / 35.48% / -11.60%`，最大回撤 `-25.98% / -22.88% / -11.74% / -11.74% / -11.88%`，换手 `8.30x / 7.99x / 8.46x / 10.05x / 10.67x`；换手低于当前 robust，但 2026 仍为负、长窗收益不足，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`。
- 收尾 guard 为 `pass`，HK all candidates `79/79 complete`；本轮未触发 HK explore cap evict。最终 rotation 为 `stagnation_runs=20 / weekly_turnover_reduction / rotate`。下一轮第一条命令建议实现 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit42`，继续比较更窄退出缓冲能否在低换手下修复 2026 负收益。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮稳定低换手现金防守未晋级，计划提示回到高弹性周频并记录成本代价。本轮补 `theme_fast_weekly_cashguard_turnover20`，继续只作为 HK 纯周度 Path 3 比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_cashguard_turnover20`。实际命令见 HK Path 1 本轮合并命令。
- `theme_fast_weekly_cashguard_turnover20` 五窗口 CAGR 为 `13.99% / 20.00% / 21.95% / 55.64% / 8.97%`，最大回撤 `-42.92% / -36.28% / -21.72% / -15.19% / -9.12%`，换手 `25.19x / 24.01x / 25.36x / 31.88x / 31.08x`；2026 转正但 2017/2020 回撤仍深、换手仍约 24-32x，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`，`meanCAGR=26.69% / minCAGR=21.96% / worstMaxDD=-26.67% / meanTurn=10.50`。
- 收尾 guard 为 `pass`，HK all candidates `76/76 complete`；最终 rotation 为 `stagnation_runs=17 / cost_stress / rotate`。下一轮 focus -> candidates 池不要继续追 30x 弹性，第一条命令建议实现 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover7_exit45`，五窗口 `--only-strategy-ids <hk_path3_cost_stress_id>` 增量确认。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `turnover8` 继续负 2026，最终 focus 仍在 `weekly_defensive_overlay`。本轮补 `cashguard_turnover9`，继续只作为 HK 纯周度 Path 3 比较，不并入 Path 1/2 月频结论。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cashguard_turnover9`。实际命令与 HK Path 1/2 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard,hkconnect_path2_theme_monthly_cost_control_v2,hkconnect_path3_stable_weekly_equal_buffered_cashguard_turnover9`。
- `cashguard_turnover9` 五窗口 CAGR 为 `18.81% / 18.85% / 22.93% / 33.40% / -15.74%`，最大回撤 `-27.79% / -22.13% / -12.27% / -12.27% / -12.21%`，换手 `8.74x / 8.49x / 9.03x / 11.17x / 11.24x`；换手低于高弹性周频，但收益和 2026 防守都不如 robust 所需，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`，`meanCAGR=26.69% / minCAGR=21.96% / worstMaxDD=-26.67% / meanTurn=10.50`。
- Guard 显示 HK all candidates `73/73 complete`，本轮未触发 evict；最终 rotation 为 `stagnation_runs=14 / weekly_defensive_overlay / rotate`。下一轮 focus -> candidates 池不要继续在稳定低换手线上加现金防守，第一条命令建议回到高弹性周频的 `hkconnect_path3_theme_fast_weekly_cashguard_turnover20`，并同时记录 30x 换手和长窗回撤代价。

## 本轮执行计划（2026-05-20 13:58 CST）

- 上一轮 focus 为 `weekly_turnover_reduction`，本轮在 `stable_weekly_equal_buffered_cost_guard` 上继续压换手，仍只作为 HK 纯周度 Path 3 观察，不并入 Path 1/2 月频结论。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8`。实际命令与 HK Path 1/2 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard,hkconnect_path2_equal_elastic_monthly_cost_guard_v2,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8`。
- `turnover8` 五窗口 CAGR 为 `21.17% / 21.92% / 25.99% / 33.40% / -15.74%`，最大回撤 `-25.62% / -22.03% / -12.27% / -12.27% / -12.21%`，换手 `8.57x / 8.28x / 8.88x / 11.17x / 11.24x`；换手较 robust 下降，但 2020/2023 收益与 2026 防守不足，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`，`meanCAGR=26.69% / minCAGR=21.96% / worstMaxDD=-26.67% / meanTurn=10.50`。
- Guard 显示 HK all candidates `70/70 complete`，本轮未触发 evict；最终 rotation 为 `stagnation_runs=11 / weekly_turnover_reduction / rotate`。下一轮 focus -> candidates 池不要继续单纯压到负 2026，第一条命令建议实现 `hkconnect_path3_stable_weekly_equal_buffered_cashguard_turnover9`，用五窗口 `--only-strategy-ids <hk_path3_weekly_id>` 增量确认。

## 本轮执行计划（2026-05-20 05:20 CST）

- 上一轮提示为高弹性周频防守 overlay 与换手约束；本轮新增 `theme_fast_weekly` 的防守降仓 + `turnover18` 版本，继续只在 HK 纯周度路径内比较。
- 本轮新增并五窗口确认：`hkconnect_path3_theme_fast_weekly_defensive_turnover18`。实际命令与 HK Path 1/2 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_cashguard,hkconnect_path2_breakout_cost_guard_biweekly_exit35,hkconnect_path3_theme_fast_weekly_defensive_turnover18`。
- `defensive_turnover18` 五窗口 CAGR 为 `14.72% / 21.25% / 23.94% / 51.80% / 12.46%`，最大回撤 `-42.73% / -37.41% / -22.06% / -16.67% / -8.36%`，换手 `25.45x-31.72x`；2025/2026 有弹性，但 2017/2020 回撤仍太深，收益也低于现有 robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`，`meanCAGR=26.69% / minCAGR=21.96% / worstMaxDD=-26.67% / meanTurn=10.50`。
- HK candidate_count 为 `67`，未触发 evict；收尾 guard 的 HK Path 3 rotation 为 `stagnation_runs=8 / cost_stress / rotate`。下一轮 focus -> candidates 池优先在 `stable_weekly_equal_buffered_cost_guard` 上做更低换手/更低交易成本压力，而不是继续追 30x 周频弹性。
- 下一轮第一条命令建议先实现 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8` 与 `hkconnect_path3_stable_weekly_equal_buffered_cashguard_turnover9`，再用 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path3_cost_stress_ids>` 补跑。

## 本轮执行计划（2026-05-19 23:14 CST）

- 上一轮 `hkconnect_path3_stable_weekly_equal_buffered_cost_guard` 成为 2017 winner 与 robust；本轮按低换手稳定线继续加宽出场成本防守，不并入 HK Path 1/2 月频或双周结论。
- 本轮新增并五窗口确认：`hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。实际命令与 HK Path 1/2 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_cost_guard,hkconnect_path2_breakout_cost_guard_biweekly,hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。
- 新宽出场成本防守五窗口 CAGR 为 `21.94% / 23.56% / 25.46% / 26.64% / -16.07%`，最大回撤 `-24.83% / -21.88% / -13.66% / -13.66% / -12.96%`，换手 `8.60x-11.91x`；回撤改善但收益低于当前 robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked/robust 未变化：2017 仍为 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；robust 仍为 `stable_weekly_equal_buffered_cost_guard`，`meanCAGR=26.69% / minCAGR=21.96% / worstMaxDD=-26.67% / meanTurn=10.50`。
- HK candidate_count 为 `64/64 complete`，本轮未触发 evict；收尾 rotation 为 `stagnation_runs=5 / weekly_defensive_overlay / rotate`。下一轮 focus -> candidates 池优先在高弹性周频上加防守 overlay 和换手约束，建议先实现 `hkconnect_path3_theme_fast_weekly_defensive_turnover18` 与 `hkconnect_path3_theme_fast_weekly_cashguard_turnover20`，第一条命令继续用五窗口 `--only-strategy-ids`。

## 本轮执行计划（2026-05-19 17:26 CST）

- 本轮新增并用 `--only-strategy-ids` 五窗口补跑 3 个周频成本/换手候选：`hkconnect_path3_theme_fast_weekly_turnover20`、`hkconnect_path3_theme_fast_weekly_turnover_guard`、`hkconnect_path3_stable_weekly_equal_buffered_cost_guard`；继续只作为 HK 纯周频路径观察。
- `stable_weekly_equal_buffered_cost_guard` 成为 2017 window winner 与 robust：2017 `21.96% CAGR / -26.67% MaxDD / 1.04 Sharpe / 9.66 Turn`，2020 `24.89% / -21.54% / 1.09 / 9.45`，2023 `28.13% / -14.21% / 1.43 / 10.02`，2025 `31.78% / -14.21% / 1.37 / 12.86`。
- `theme_fast_weekly_turnover_guard` 成为 2025 window winner（`71.19% CAGR / -13.25% MaxDD / 1.88 Sharpe / 31.96 Turn`），且 2023 有 `32.28% CAGR`，但 2017/2020 回撤仍有 `-38.54% / -37.31%`，不适合 robust。
- HK Path 3 tracked winners 更新为：2017 `stable_weekly_equal_buffered_cost_guard`，2020/2023 `theme_fast_weekly_buffered`，2025 `theme_fast_weekly_turnover_guard`；robust 切为 `stable_weekly_equal_buffered_cost_guard`，`meanCAGR=26.69% / minCAGR=21.96% / worstMaxDD=-26.67% / meanTurn=10.50`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 3 rotation 为 `stagnation_runs=1 / weekly_turnover_reduction / continue`；下一轮继续尝试低换手稳定线，避免只追 `30x` 年化换手的短窗弹性。

## 本轮执行计划（2026-05-19 11:12 CST）

- 本轮 `tracked_active` 增量刷新继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 当前窗口指标为：2017 `21.54% CAGR / -33.66% MaxDD / 0.97 Sharpe / 10.84 Turn`，2020 `26.45% / -34.43% / 0.89 / 30.99`，2023 `38.29% / -19.56% / 1.25 / 29.75`，2025 `69.82% / -17.82% / 1.63 / 34.96`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 3 rotation 为 `stagnation_runs=34 / cost_stress / rotate`；下一轮重点压约 `30x` 年化换手和交易成本，不提高周频进攻强度。

## 本轮执行计划（2026-05-19 05:29 CST）

- 本轮按 `weekly_defensive_overlay` 轮换方向新增并用 `--only-strategy-ids` 增量补跑 `hkconnect_path3_theme_fast_weekly_defensive_wide`、`hkconnect_path3_theme_fast_weekly_defensive_cap26`、`hkconnect_path3_theme_fast_weekly_cashguard`，继续只作为 HK 纯周频路径观察。
- `defensive_cap26` 五窗口为：2017 `18.51% CAGR / -40.96% MaxDD / 0.74 Sharpe / 29.57 Turn`，2020 `24.96% / -37.71% / 0.88 / 28.84`，2023 `30.27% / -22.24% / 1.09 / 28.43`，2025 `58.24% / -15.24% / 1.54 / 33.60`，2026 `4.14%`；回撤略收，但收益不如现有 winner。
- `cashguard` 在 2025 几乎复刻现有防守 winner（`69.80% CAGR / -17.81% MaxDD / 1.63 Sharpe / 34.96 Turn`），2023 也有 `36.09% CAGR`，但 2017 长窗回撤扩大到 `-46.10%`，未进入 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 3 rotation 仍为 `stagnation_runs=32 / recommended_focus=weekly_defensive_overlay / rotate`；下一轮重点不是提高周频进攻，而是降低约 `30x` 年换手和长窗回撤。

## 本轮执行计划（2026-05-18 23:13 CST）

- 本轮 `tracked_active` 增量回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 当前窗口指标为：2017 `21.54% CAGR / -33.66% MaxDD / 0.97 Sharpe / 10.84 Turn`，2020 `26.45% / -34.43% / 0.89 / 30.99`，2023 `38.29% / -19.56% / 1.25 / 29.75`，2025 `69.82% / -17.82% / 1.63 / 34.96`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `31x/30x`、2025 防守 winner 换手约 `35x`；收尾 rotation 为 `stagnation_runs=30 / recommended_focus=weekly_defensive_overlay / rotate`，下一轮优先比较周频防守 overlay、换手压降与成本压力。

## 本轮执行计划（2026-05-18 20:34 CST）

- 本轮 `tracked_active` 增量回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 当前窗口指标为：2017 `21.54% CAGR / -33.66% MaxDD / 0.972 Sharpe`，2020 `26.45% / -34.43% / 0.887`，2023 `38.29% / -19.56% / 1.250`，2025 `69.82% / -17.82% / 1.631`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `31x/30x`、2025 防守 winner 换手约 `35x`；收尾 rotation 为 `stagnation_runs=28 / recommended_focus=weekly_turnover_reduction / rotate`，下一轮优先压周频换手和交易成本。

## 本轮执行计划（2026-05-18 11:11 CST）

- 本轮 `tracked_active` 增量回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `31x/30x`、2025 防守 winner 换手约 `35x`；交易成本压力仍是主要风险。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 3 rotation 为 `stagnation_runs=23 / recommended_focus=weekly_defensive_overlay / rotate`；下一轮优先做周频防守 overlay、换手压降与成本压力。

## 本轮执行计划（2026-05-18 05:53 CST）

- 本轮 `tracked_active` 增量回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `30x`、2025 防守 winner 换手约 `35x`；交易成本压力仍是主要风险。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 3 rotation 为 `stagnation_runs=20 / recommended_focus=weekly_turnover_reduction / rotate`；下一轮优先做周频换手压降、成本压力与防守 overlay 敏感性。

## 本轮执行计划（2026-05-17 23:12 CST）

- 本轮 `tracked_active` 增量回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`（`21.54% CAGR / -33.66% MaxDD / 0.97 Sharpe / 10.84 Turn`），2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`（`26.45% / 38.29% CAGR`）。
- 2025 winner 仍为 `hkconnect_path3_theme_fast_weekly_defensive`，`69.82% CAGR / -17.82% MaxDD / 1.63 Sharpe / 34.96 Turn`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `30x`、2025 防守 winner 换手约 `35x`；交易成本压力仍是主要风险。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 3 rotation 为 `stagnation_runs=18 / recommended_focus=weekly_turnover_reduction / rotate`；下一轮优先做周频换手压降、成本压力与防守 overlay 敏感性。

## 本轮执行计划（2026-05-17 17:25 CST）

- 本轮 `tracked_active` 增量回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`（`21.54% CAGR / -33.66% MaxDD / 0.97 Sharpe / 10.84 Turn`），2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`（`26.45% / 38.29% CAGR`）。
- 2025 winner 仍为 `hkconnect_path3_theme_fast_weekly_defensive`，`69.82% CAGR / -17.82% MaxDD / 1.63 Sharpe / 34.96 Turn`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `30x`、2025 防守 winner 换手约 `35x`；交易成本压力仍是主要风险。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 3 rotation 为 `stagnation_runs=15 / recommended_focus=cost_stress / rotate`；下一轮优先做周频成本压力、换手压降与防守 overlay 敏感性。

## 本轮执行计划（2026-05-17 11:15 CST）

- 本轮 HK 五窗口离线回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`（`21.54% CAGR / -33.66% MaxDD / 0.97 Sharpe / 10.84 Turn`），2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`（`26.45% / 38.29% CAGR`）。
- 2025 winner 仍为 `hkconnect_path3_theme_fast_weekly_defensive`，`69.82% CAGR / -17.82% MaxDD / 1.63 Sharpe / 34.96 Turn`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `30x`、2025 防守 winner 换手约 `35x`；交易成本压力仍是当前主要风险。
- 收尾 rotation 为 `stagnation_runs=12 / recommended_focus=weekly_defensive_overlay / rotate`；下一轮优先比较周频防守 overlay、换手压降与成本压力。

## 本轮执行计划（2026-05-17 05:15 CST）

- 本轮 HK 五窗口离线回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`（`21.54% CAGR / -33.66% MaxDD / 0.97 Sharpe / 10.84 Turn`），2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`（`26.45% / 38.29% CAGR`）。
- 2025 winner 仍为 `hkconnect_path3_theme_fast_weekly_defensive`，`69.82% CAGR / -17.82% MaxDD / 1.63 Sharpe / 34.96 Turn`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `30x`、2025 防守 winner 换手约 `35x`；交易成本压力仍是当前主要风险。
- 收尾 rotation 为 `stagnation_runs=10 / recommended_focus=weekly_turnover_reduction / rotate`；下一轮优先压换手和成本压力，再比较防守 overlay。

## 本轮执行计划（2026-05-16 23:12 CST）

- 本轮 HK 五窗口离线回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`（`21.54% CAGR / -33.66% MaxDD / 0.97 Sharpe / 10.84 Turn`），2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`（`26.45% / 38.29% CAGR`）。
- 2025 winner 仍为 `hkconnect_path3_theme_fast_weekly_defensive`，`69.82% CAGR / -17.82% MaxDD / 1.63 Sharpe / 34.96 Turn`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线收益弹性仍在，但 2020/2023 winner 换手约 `30x`、2025 防守 winner 换手约 `35x`；交易成本压力仍是当前主要风险。
- 收尾 rotation 为 `stagnation_runs=8 / recommended_focus=cost_stress / rotate`；下一轮优先做周频成本压力、换手压降与防守 overlay 敏感性。

## 本轮执行计划（2026-05-16 17:14 CST）

- 本轮 HK 五窗口离线回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`（`21.54% CAGR / -33.66% MaxDD / 0.97 Sharpe / 10.84 Turn`），2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`（`26.45% / 38.29% CAGR`）。
- 2025 winner 仍为 `hkconnect_path3_theme_fast_weekly_defensive`，`69.82% CAGR / -17.82% MaxDD / 1.63 Sharpe / 34.96 Turn`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 换手约 `30x`，2025 防守 winner 换手约 `35x`；交易成本压力仍是当前主要风险。
- 收尾 rotation 为 `stagnation_runs=6 / recommended_focus=cost_stress / rotate`；下一轮优先做周频成本压力、换手压降与防守 overlay 敏感性。

## 本轮执行计划（2026-05-16 11:20 CST）

- 本轮 HK 五窗口离线回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 周频路线仍有收益弹性，但 2020/2023 winner 换手约 `30x`，2025 防守 winner 换手约 `35x`；交易成本压力仍是主风险。
- 收尾 rotation 为 `stagnation_runs=2 / recommended_focus=weekly_turnover_reduction / continue`；下一轮优先压换手和成本压力，再比较防守 overlay。

## 本轮执行计划（2026-05-16 06:56 CST）

- 本轮 HK 五窗口离线回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；`update_hkconnect_artifacts.py` 已同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=30.23% / minCAGR=21.54% / worstMaxDD=-33.66% / meanTurn=11.33`。
- 高频路线仍有收益弹性，但 2020/2023 winner 的换手约 `30x`，2025 防守 winner 换手约 `35x`；交易成本压力仍是当前主要风险。
- 收尾 rotation 为 `stagnation_runs=32 / recommended_focus=weekly_defensive_overlay / rotate`；下一轮优先做周频防守 overlay、换手压降与成本压力测试。

## 本轮执行计划（2026-05-15 15:16 CST）

- 本轮 HK 五窗口离线回测继续覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；随后 `update_hkconnect_artifacts.py` 同步 tracked payload 与三张对比图。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`。
- 当前高频路线仍有明显收益弹性，但 2020/2023 winner 的换手约 `30x`，2025 防守 winner 换手约 `34.7x`，交易成本压力仍是主风险。
- 最终 rotation 为 `stagnation_runs=24 / recommended_focus=cost_stress / rotate`；下一轮优先做周频成本压力、换手压降和防守 overlay 敏感性。

## 本轮执行计划（2026-05-15 10:14 CST）

- 本轮港股 Path 3 继续只覆盖纯周度候选，月频与双周结论不并入本路径；五窗口回测与 HK artifact 同步完成后 coverage 为 `pass`。
- HK Path 3 tracked winners 未变：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；最终 rotation 为 `stagnation_runs=22 / weekly_defensive_overlay`，下一轮继续压周频换手与防守成本。

## 本轮执行计划（2026-05-14 22:55 CST）

- 本轮港股五窗口回测覆盖纯周度 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；HK coverage 收尾为 `pass`。
- HK Path 3 tracked winners 当前为：2017 `hkconnect_path3_stable_weekly_equal_buffered`（`21.78% CAGR / -33.66% MaxDD / 0.9800 Sharpe / 10.83 Turn`），2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`（`27.62% / 40.82% CAGR`），2025 `hkconnect_path3_theme_fast_weekly_defensive`（`78.07% / -17.82% / 1.7678 / 34.72`）。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；最终 guard 为 `stagnation_runs=18 / weekly_turnover_reduction`，下一轮继续做周频成本压力与换手压降。

## 本轮执行计划（2026-05-14 15:10 CST）

- 本轮 HK 五窗口回测继续覆盖纯周频 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；收尾 guard 对 HK coverage 为 `pass`。
- HK Path 3 rotation 为 `stagnation_runs=13 / recommended_focus=weekly_defensive_overlay`，下一轮新增配额为 HK Path 3 `3` 个候选。
- Path 3 tracked winners 未换身份：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 最新指标为：2017 `21.78% CAGR / -33.66% MaxDD / 0.9800 Sharpe / 10.83 Turnover`；2020 `27.62% / -34.43% / 0.9164 / 30.93`；2023 `40.82% / -19.56% / 1.3156 / 29.62`；2025 `78.07% / -17.82% / 1.7678 / 34.72`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`。
- 下一轮优先在 `weekly_defensive_overlay` 下压降周频换手和回撤，比较风险降仓、宽出场与持仓数量约束；不继续单纯提高周频进攻强度。

## 本轮执行计划（2026-05-14 09:13 CST）

- 本轮 HK 五窗口回测继续覆盖纯周频 Path 3 候选，Path 1/2 月频与双周结论不并入本路径；收尾 guard 对 HK coverage 为 `pass`。
- HK Path 3 rotation 为 `stagnation_runs=11 / recommended_focus=weekly_turnover_reduction`，下一轮新增配额为 HK Path 3 `3` 个候选。
- Path 3 tracked winners 未换身份：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 最新指标为：2017 `21.78% CAGR / -33.66% MaxDD / 0.9800 Sharpe / 10.83 Turnover`；2020 `27.62% / -34.43% / 0.9164 / 30.93`；2023 `40.82% / -19.56% / 1.3156 / 29.62`；2025 `78.07% / -17.82% / 1.7678 / 34.72`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`。
- 下一轮重点仍是周频换手压降与交易成本压力测试，而不是继续提高周频进攻强度。

## 本轮执行计划（2026-05-14 03:17 CST）

- 本轮 HK 五窗口回测继续覆盖纯周频 Path 3 候选，Path 1/2 月频与双周结论不并入本路径。
- Path 3 tracked winners 未换身份：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 最新指标为：2017 `21.78% CAGR / -33.66% MaxDD / 0.9800 Sharpe / 10.83 Turnover`；2020 `27.62% / -34.43% / 0.9164 / 30.93`；2023 `40.82% / -19.56% / 1.3156 / 29.62`；2025 `78.07% / -17.82% / 1.7678 / 34.72`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`。
- 收盘 guard 将 HK Path 3 rotation 推进到 `stagnation_runs=9 / recommended_focus=weekly_turnover_reduction`；下一步重点是周频候选在交易成本和换手压力下是否仍可交易，而不是继续提高进攻强度。

## 本轮执行计划（2026-05-13 21:21 CST）

- 本轮 HK 五窗口回测继续覆盖纯周频 Path 3 候选，Path 1/2 月频与双周结论不并入本路径。
- Path 3 tracked winners 更新后为：2017 `hkconnect_path3_stable_weekly_equal_buffered`，2020/2023 `hkconnect_path3_theme_fast_weekly_buffered`，2025 `hkconnect_path3_theme_fast_weekly_defensive`。
- 最新指标为：2017 `21.78% CAGR / -33.66% MaxDD / 0.9800 Sharpe / 10.83 Turnover`；2020 `27.62% / -34.43% / 0.9164 / 30.93`；2023 `40.82% / -19.56% / 1.3156 / 29.62`；2025 `78.07% / -17.82% / 1.7678 / 34.72`。
- 四窗口 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`。
- rotation 已提示下一轮港股 Path 3 转向 `cost_stress`；当前重点是交易成本与换手压力测试，而不是继续提高周频进攻强度。

## 2026-05-09 21:14 CST 复核

- 本轮在 `hkconnect_path3_theme_fast_weekly` 基础上新增 3 个纯周度降换手/降回撤变体：`_buffered`（宽出场）、`_defensive`（风险降仓）、`_balanced6`（六持仓/降集中），Path 3 候选数从 `13` 扩到 `16`，全部仍为 `weekly`。
- 新 `hkconnect_path3_theme_fast_weekly_defensive` 改写 `since_2017_01 / since_2020_01 / since_2025_01` 窗口 winner：长窗为 `23.86% CAGR / -28.45% MaxDD / 0.9638 Sharpe / 29.23 Turnover`，相对旧 `theme_fast_weekly` 同时改善 CAGR、回撤、Sharpe 与换手。
- `since_2023_01` 窗口小幅切到 `hkconnect_path3_theme_fast_weekly_buffered`，`40.82% CAGR / -19.56% MaxDD / 1.3156 Sharpe / 29.62 Turnover`；改善幅度很小，主要记录为宽出场对照。
- 四窗口 robust candidate 仍是旧 `hkconnect_path3_theme_fast_weekly`，`meanCAGR=41.45% / minCAGR=23.47% / worstMaxDD=-33.61% / meanTurn=31.32`，说明降仓变体改善窗口 winner 但尚未改写四窗口均值排序。
- `since_2026_01` 只观察，当前 raw leader 仍是 `hkconnect_path3_equal_elastic_weekly`；下一轮优先围绕 `defensive` 继续做风险降仓与交易成本敏感性，而不是扩大周频进攻强度。

## 2026-05-09 18:09 CST 复核

- 本轮继续运行五窗口离线回测，Path 3 候选数保持 `13`，全部为 `weekly`；结果单独写入 `results_hkconnect/tracked_winners_hkconnect.json` 与 `docs/strategy_comparison_hkconnect_path3.png`。
- 当前 Path 3 tracked winners 继续全部由 `hkconnect_path3_theme_fast_weekly` 占据：`since_2020_01` 为 `23.47% CAGR / -33.61% MaxDD / 0.9339 Sharpe / 30.48 Turnover`，`since_2023_01` 为 `40.80% / -19.56% / 1.3152 / 29.62`，`since_2025_01` 为 `78.07% / -17.81% / 1.7677 / 34.71`。
- 四窗口 robust candidate 同为 `hkconnect_path3_theme_fast_weekly`，`meanCAGR=41.45% / minCAGR=23.47% / worstMaxDD=-33.61% / meanTurn=31.32`。
- `since_2026_01` 只观察，当前 raw leader 是 `hkconnect_path3_equal_elastic_weekly`；下一轮优先围绕 `theme_fast_weekly` 做降换手/降回撤变体，而不是继续单纯提高 weekly 进攻强度。

## 2026-05-09 三路径拆分基线

- 本轮将沪港通研究线拆为三条独立路径：Path 1 维护实盘稳健线，Path 2 维护月度/双周高收益探索线，Path 3 只维护纯周度信号、纯周度换股候选。
- 代码侧新增 `HK_PATH3_VARIANTS`，从原有单周候选复制为 `hkconnect_path3_*` 独立 ID；Path 1/Path 2 不再承载单周换股候选。
- 当前 Path 3 候选数为 `13`，全部为 `weekly`；五窗口回测完成后已同步 `results_hkconnect/tracked_winners_hkconnect.json` 与 `docs/strategy_comparison_hkconnect_path3.png`。

当前 Path 3 tracked winners：

- `since_2017_01 / since_2020_01`：`hkconnect_path3_theme_fast_weekly`，`23.47% CAGR / -33.61% MaxDD / 0.9339 Sharpe / 30.48 Turnover`。
- `since_2023_01`：`hkconnect_path3_theme_fast_weekly`，`40.80% CAGR / -19.56% MaxDD / 1.3152 Sharpe / 29.62 Turnover`。
- `since_2025_01`：`hkconnect_path3_theme_fast_weekly`，`78.07% CAGR / -17.81% MaxDD / 1.7677 Sharpe / 34.71 Turnover`。
- 四窗口 robust candidate：`hkconnect_path3_theme_fast_weekly`，`meanCAGR=41.45% / minCAGR=23.47% / worstMaxDD=-33.61% / meanTurn=31.32`。

观察结论：

- 纯周度线的收益弹性明显强于 Path 2 的中长窗口月频锚点，但换手也显著更高。
- 当前 Path 3 的核心问题不是短窗强度，而是 `30x+` 年化换手和 `-33.61%` 最差回撤是否能被实际交易成本、流动性和仓位约束接受。
- 下一轮优先围绕 `theme_fast_weekly` 做降换手/降回撤变体，而不是继续单纯提高周度进攻强度。
