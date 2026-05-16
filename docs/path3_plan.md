# Path 3 研究计划

本文档用于约束和记录 `Path 3`（周度高频调仓路径）。
Path 3 只跟踪纯周度换股候选，候选 `strategy_base_id` 必须以 `_weekly` 结尾；月度选股叠加周度仓位 overlay（例如 `__port_weekly_exposure`、`__sat_weekly_risk`、`__sat_three_stage`）不纳入本路径。

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
