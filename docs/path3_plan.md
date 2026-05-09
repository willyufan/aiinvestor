# Path 3 研究计划

本文档用于约束和记录 `Path 3`（周度高频调仓路径）。
Path 3 只跟踪纯周度换股候选，候选 `strategy_base_id` 必须以 `_weekly` 结尾；月度选股叠加周度仓位 overlay（例如 `__port_weekly_exposure`、`__sat_weekly_risk`、`__sat_three_stage`）不纳入本路径。

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
