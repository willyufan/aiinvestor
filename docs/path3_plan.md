# Path 3 研究计划

本文档用于约束和记录 `Path 3`（周度高频调仓路径）。
Path 3 只跟踪纯周度换股候选，候选 `strategy_base_id` 必须以 `_weekly` 结尾；月度选股叠加周度仓位 overlay（例如 `__port_weekly_exposure`、`__sat_weekly_risk`、`__sat_three_stage`）不纳入本路径。

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
