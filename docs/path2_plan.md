# Path 2 研究计划

本文档用于约束和记录 `Path 2`（无约束上限探索）的研究方向。  
`Path 2` 的目标不是延续 `Path 1` 的稳健改良逻辑，而是作为**独立路线**去追求更高收益上限，优先冲击：

- `since_2020_01` 窗口 `40%+ CAGR`
- `since_2023_01` 窗口 `40%+ CAGR`

在这个阶段，`Path 2` 不要求先打赢 `Path 1` 才记录，也不要求先把回撤压到与 `Path 1` 同级；它的优先级是：

1. 先做出显著更高的收益上限
2. 再讨论如何把极端回撤收回来

当前已把 `Path 2` 的单轮探索预算提升到 **`24-36` 个显式原型 / `5` 条独立候选族**，并把 family-ranked 候选宇宙扩到 **`100+`** 规模；每条候选族固定保留 `4-6` 个代表候选。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `reconfirm75/caution85/cap75` 保留 2020/2025 弹性但 2026 转负，本轮按 `medium_cycle_growth/risk_reconfirm_sensitivity` 继续同一中周期高收益族，把单票 cap 降到 `65`，观察能否修复 2026 与集中风险。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `25.34% / 39.69% / 38.86% / 130.50% / -12.60%`，最大回撤为 `-52.66% / -36.35% / -33.69% / -11.51% / -13.03%`，换手为 `3.77x / 4.65x / 4.44x / 7.30x / 7.25x`；总市值版为 `24.84% / 35.04% / 31.15% / 142.71% / -6.29%`，最大回撤为 `-52.50% / -35.26% / -33.51% / -13.29% / -10.19%`。降低 cap 没有修复 2017 深回撤与 2026 负收益，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `733`，`high_growth_theme=323`、`weekly_rebalance_aggressive=62`、`emergent_theme_discovery=60`；`scripts/update_weighted_winners.py` 后 Path 2 tracked/window winner 有同步校验但本轮候选未替换 official/robust，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 733/733 complete`，下一轮 focus 为 `underrepresented_families`。第一条命令建议暂停 high-growth cap/risk 邻域，补一个低相关双周或防守多因子代表，例如 `core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_ids>`。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；上一轮等权多因子 companion 只提供低相关失败对照，本轮按 `medium_cycle_growth` 回到高收益中周期族。上一轮建议的 `risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard` 已有完整结果，因此本轮新增更严恢复确认、更高谨慎仓、更低 cap 的 `reconfirm75/caution85/cap75` 版本。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `25.58% / 40.34% / 39.97% / 123.65% / -16.32%`，最大回撤 `-52.66% / -37.14% / -34.65% / -12.63% / -14.07%`，换手 `3.78x / 4.67x / 4.44x / 7.31x / 6.78x`；总市值版为 `24.93% / 34.91% / 31.45% / 137.04% / -12.00%`，最大回撤 `-52.50% / -36.38% / -33.89% / -14.69% / -12.05%`。该组验证更严恢复确认仍保留 2020/2025 弹性，但 2017 深回撤和 2026 负收益仍未修复，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `727`，`high_growth_theme=321`；`scripts/update_weighted_winners.py` 后 Path 2 tracked/window winner 有同步校验但本轮候选未替换 official/robust，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 仍为 `medium_cycle_growth`。第一条命令建议不要继续只升恢复确认，改测 `risk45/exit55` 下的 2026 修复约束，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`；上一轮 high-growth `risk35/exit55/reconfirm80/caution80/cap80_cost_guard` 仍保留 2023/2025 弹性但 2026 转负，本轮按计划补一个非 high-growth/低相关等权多因子代表，避免 Path 2 继续被 high_growth family 压扁。
- 本轮新增并五窗口确认 1 个 Path 2/decorrelated defensive mix base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版 `quality_lowvol_trend_reconfirm` 五窗口 CAGR 为 `11.43% / 13.24% / 28.21% / 62.24% / 70.34%`，最大回撤为 `-48.92% / -37.49% / -31.57% / -14.92% / -13.55%`，换手为 `3.23x / 3.59x / 3.99x / 5.96x / 6.62x`。它能给 2026 正收益对照，但 2017/2020 收益与回撤远弱于 Path 2 robust，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `722`，`decorrelated_defensive_mix=21`、`high_growth_theme=319`、`weekly_rebalance_aggressive=60`；`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 已轮换为 `medium_cycle_growth`。第一条命令建议回到中周期高收益原型，但显式带 2026 防守约束，测试等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard` 或同等恢复阈值/风险阈值折中，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮 focus 指向 `risk_reconfirm_sensitivity`，本轮按计划用等权/总市值双底座确认更低风险阈值 `risk35`、更严恢复确认 `reconfirm80`、更低 `exit55` 与 `caution80/cap80` 的 high-growth 变体。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_12_88_hold_3_7_ramp85_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly`。
- 等权版五窗口 CAGR 为 `32.74% / 32.30% / 47.32% / 89.91% / -12.81%`，最大回撤 `-29.20% / -30.50% / -33.63% / -24.52% / -14.09%`，换手 `3.65x / 4.20x / 4.23x / 7.55x / 6.44x`；总市值版为 `29.84% / 27.35% / 41.13% / 104.93% / -8.68%`，最大回撤 `-30.06% / -30.43% / -33.69% / -26.80% / -12.54%`。该组仍保留 2023/2025 弹性，但 2026 转负且最近持仓高度集中在源杰科技/腾景科技，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `716`，`high_growth_theme=319`，raw robust 仍由旧 high-growth 组合领先；`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`，四窗口 meanCAGR `46.97%`、minCAGR `21.83%`、worstMaxDD `-15.47%`、meanTurn `3.00x`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 716/716 complete`，下一轮 focus 转为 `underrepresented_families`。第一条命令建议暂停继续堆 high-growth 参数，补一个非 high-growth/低相关代表，例如等权多因子或双周低回撤族 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm` 或同等 underrepresented family，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_ids>`。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮双周 underrepresented family 与等权多因子 companion 都没有改善 robust，本轮按 `capacity_and_cost_stress` 回到 high-growth robust 邻域。上一轮文档建议的 `aggr_02_98...reconfirm75_cap80_cost_guard` 已有结果，因此本轮改为未尝试的 `aggr_02_98...reconfirm75_caution80_cap80_cost_guard`，用等权/总市值双底座五窗口确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard`。实际 A股非阻塞命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly`。
- 等权版五窗口 CAGR 为 `37.17% / 50.02% / 49.92% / 109.40% / -11.67%`，最大回撤 `-32.86% / -32.31% / -29.14% / -12.09% / -14.09%`，换手 `3.70x / 4.33x / 4.36x / 7.32x / 6.44x`；总市值版为 `34.81% / 43.44% / 43.02% / 123.49% / -7.48%`，最大回撤 `-33.12% / -32.53% / -30.81% / -14.73% / -12.54%`。该组保留 2020/2023 高收益，但 2026 仍负，且最近持仓高度集中在源杰科技/腾景科技，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `710`，`high_growth_theme=317`；`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`，四窗口 meanCAGR `46.97%`、minCAGR `21.83%`、worstMaxDD `-15.47%`、meanTurn `3.00x`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 转为 `risk_reconfirm_sensitivity`。第一条命令建议不要继续只压 cap，改测更强风险阈值与恢复确认组合，例如等权/总市值 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；上一轮要求从 `underrepresented_families` 补非 high-growth 代表，本轮用双周 rebalance + 成本守门做压力测试，并把等权多因子 companion 纳入 Path 2 横向比较。A股非阻塞命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn06_exit88_weekly`。
- 本轮新增并五窗口确认 1 个 Path 2 underrepresented/biweekly base id：`core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard`。五窗口 CAGR 为 `7.80% / 12.91% / 21.82% / 66.66% / 36.64%`，最大回撤 `-43.17% / -34.99% / -27.49% / -20.18% / -11.61%`，换手 `4.99x / 5.47x / 6.03x / 12.00x / 12.54x`。双周成本守门没有改善 2020/2023，上限也低于 high-growth robust。
- 等权多因子 companion `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm` 的五窗口 CAGR 为 `12.76% / 15.65% / 30.93% / 55.06% / 69.85%`，2026 较强但 2017/2020/2023 回撤过深，只保留为 decorrelated defensive mix 失败对照。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `705`，raw robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`；`scripts/update_weighted_winners.py` 后 Path 2 official winner/robust/tracked payload 未变化。候选池未触发 Path 2 evict。最终 focus 转为 `capacity_and_cost_stress`；下一轮第一条命令建议回到 high-growth robust 邻域压 cap 与成本，而不是继续扩弱双周，例如等权/总市值 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮 `exit55/reconfirm75/caution80/cap75` 仍无法修复 2026 负收益，本轮沿 `medium_cycle_growth` 把退出阈值进一步收紧到 `exit50`，继续只用等权/总市值双底座确认。命令类型为五窗口 `--only-base-ids` 增量确认，实际 A股合并命令见 Path 1 本轮记录。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard`。
- 等权版五窗口 CAGR 为 `27.37% / 41.10% / 37.42% / 112.60% / -10.52%`，最大回撤 `-29.02% / -35.78% / -27.60% / -11.78% / -13.61%`，换手 `3.81x / 4.47x / 4.61x / 7.30x / 6.66x`；总市值版为 `26.55% / 35.36% / 27.84% / 123.31% / -6.02%`，最大回撤 `-28.98% / -35.55% / -29.95% / -13.87% / -11.64%`。该组证明单纯收紧 exit 不能修复 2026，且近期贡献仍高度集中在少数高弹性票。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `699`，`high_growth_theme=315`，raw robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`；`scripts/update_weighted_winners.py` 后 official robust/tracked payload 未变化。
- 候选池未触发 Path 2 evict。最终 focus 转为 `risk_reconfirm_sensitivity`；下一轮第一条命令建议不要继续只压 exit，改测更强风险阈值与恢复确认组合，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit50_reconfirm80_caution80_cap70_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮 `risk35 + exit55 + reconfirm75 + caution80 + cap70` 仍无法修复 2026 负收益，本轮按 `risk_reconfirm_sensitivity` 把风险阈值调回 `risk40`、保留 `exit55/reconfirm75/caution80/cap75/cashguard`，继续只用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard`。实际命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn05_exit92_weekly`。
- 等权版五窗口 CAGR 为 `26.50% / 41.09% / 37.42% / 112.60% / -10.52%`，最大回撤 `-33.44% / -35.78% / -27.60% / -11.78% / -13.61%`，换手 `3.78x / 4.47x / 4.61x / 7.30x / 6.66x`；总市值版为 `25.68% / 35.35% / 27.84% / 123.31% / -6.02%`，最大回撤 `-33.40% / -35.55% / -29.95% / -13.87% / -11.64%`。该组保留 2020/2025 弹性，但 2026 仍负，且近期贡献继续集中在少数高弹性票。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `686`，raw robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95`；`scripts/update_weighted_winners.py` 后 official robust 仍偏向既有 high-growth 组合，本轮未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 focus 转为 `underrepresented_families`；下一轮第一条命令不要继续只压 high-growth 参数，建议补一个双周/非 high-growth 代表，例如 `core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮 `risk35 + reconfirm75 + caution75 + cap80` 保留 2020 中周期强收益但 2026 仍负，本轮按 `capacity_and_cost_stress` 把谨慎仓提高到 `80/55`、单票 cap 降到 `70`，继续只用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard`。实际命令见 Path 1 本轮 A股非阻塞合并批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `26.38% / 40.94% / 36.43% / 115.84% / -8.58%`，最大回撤 `-33.44% / -35.78% / -27.96% / -11.51% / -13.10%`，换手 `3.77x / 4.46x / 4.61x / 7.29x / 6.90x`；总市值版为 `25.64% / 35.49% / 27.47% / 125.98% / -3.08%`，最大回撤 `-33.40% / -35.55% / -30.20% / -13.16% / -10.74%`。
- 该组比上一轮更强容量约束后仍不能修复 2026，且近期收益仍高度集中在源杰科技、腾景科技等少数票；`scripts/path2_candidate_pass.py` 后 universe 为 `681`，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95`，未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 guard 为 `ashare_path2_candidate_universe 681/681 complete`，下一轮 focus 转为 `risk_reconfirm_sensitivity`；第一条命令建议停止继续单纯压 cap，改测风险阈值与恢复确认折中，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `risk45 + exit55 + reconfirm70 + caution80 + cap80 + cashguard` 保留 2017/2020 高收益但 2026 仍负；本轮按 `risk_reconfirm_sensitivity` 继续把风险阈值降到 `risk35`、恢复确认升到 `reconfirm75`，用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard`。实际 A股非阻塞命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit90_weekly`。
- 等权版五窗口 CAGR 为 `26.40% / 41.14% / 37.59% / 108.60% / -11.46%`，最大回撤 `-31.78% / -34.45% / -26.60% / -11.78% / -13.93%`，换手 `3.71x / 4.38x / 4.53x / 7.30x / 6.30x`；总市值版为 `25.49% / 35.12% / 27.80% / 119.76% / -7.95%`，最大回撤 `-31.88% / -34.32% / -28.97% / -13.96% / -12.54%`。
- 该组相对近期 cap/caution 失败组改善部分中窗平衡，但 2026 仍为负，且近期贡献仍集中在源杰科技、腾景科技等少数高弹性票；`scripts/path2_candidate_pass.py` 后 universe 为 `675`，`scripts/update_weighted_winners.py` 后 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 focus 转为 `capacity_and_cost_stress`；下一轮第一条命令建议在本组基础上先测更强容量/谨慎仓约束，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`，上一轮建议测试中周期恢复阈值与 2026 防守折中；本轮在 high-growth robust 邻域新增 `risk45 + exit55 + reconfirm70 + caution80 + cap80 + cashguard`，用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard`。命令类型为 A股五窗口 `--only-base-ids` 增量确认：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard`。
- 等权版五窗口 CAGR 为 `30.73% / 48.46% / 38.45% / 100.65% / -12.45%`，最大回撤 `-23.86% / -27.67% / -27.19% / -14.29% / -14.12%`，换手 `4.15x / 4.57x / 4.61x / 7.33x / 6.42x`；总市值版为 `30.32% / 42.17% / 28.26% / 110.68% / -8.93%`，最大回撤 `-23.81% / -28.98% / -29.65% / -14.58% / -12.55%`。该组合保留 2017/2020 中周期高收益，但 2023 走弱且 2026 仍为负，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `670`，family 规模为 `emergent_theme_discovery=58 / high_growth_theme=307 / momentum_equal_weight_elastic=30 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=52`；`scripts/update_weighted_winners.py` 后 Path 2 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 focus 为 `risk_reconfirm_sensitivity`；下一轮第一条命令建议更直接降低风险门槛并提高恢复确认，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass`，上一轮等权 `profitability_lowvol_rebalance` 只保留 2025/2026 弹性、长窗回撤过深；本轮按 `capacity_and_cost_stress` 回到 high-growth robust 邻域，在 `cap70 + cashguard` 上把谨慎仓提高到 `80/55`，用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard`。命令类型为 A股五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path 1 本轮记录。
- 等权版五窗口 CAGR 为 `29.75% / 49.36% / 42.26% / 106.66% / -8.60%`，最大回撤 `-30.50% / -23.78% / -27.89% / -14.29% / -13.10%`，换手 `3.94x / 4.41x / 4.76x / 7.32x / 6.90x`；总市值版为 `29.03% / 43.61% / 32.92% / 115.68% / -3.10%`，最大回撤 `-30.46% / -27.21% / -30.13% / -13.93% / -10.74%`。提高 caution 后仍无法修复 2026 负收益，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `666`，family 规模为 `emergent_theme_discovery=61 / high_growth_theme=305 / momentum_equal_weight_elastic=30 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=51`；`scripts/update_weighted_winners.py` 后 Path 2 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 focus 转为 `medium_cycle_growth`；下一轮第一条命令建议停止继续只降 cap，改测中周期恢复阈值与 2026 防守的折中，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `underrepresented_families`，要求不要继续只压 high-growth cap；本轮补等权多因子弹性代表 `profitability_lowvol_rebalance`，作为非 high-growth family 压力测试。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance`。实际命令见 Path 1 本轮 A股合并批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `equal_weight profitability_lowvol_rebalance` 五窗口 CAGR 为 `11.92% / 15.23% / 29.17% / 67.76% / 70.34%`，最大回撤 `-49.67% / -32.91% / -31.55% / -15.06% / -13.55%`，换手 `3.23x / 3.59x / 3.88x / 5.93x / 6.62x`。它保留 2025/2026 弹性，但 2017/2020 回撤太深，不改善 Path 2 robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `660`，family 规模为 `emergent_theme_discovery=58 / high_growth_theme=303 / momentum_equal_weight_elastic=30 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=51`；`scripts/update_weighted_winners.py` 后 Path 2 official winners 与 robust 未变化，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 Path 2 evict。最终 guard 下一轮 focus 转为 `capacity_and_cost_stress`；第一条命令建议回到当前 high-growth robust 邻域做更强容量/成本约束，而不是继续扩弱多因子，例如注册等权/总市值 `risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard` 或同等 cap/caution 成本版，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass`，上一轮 `risk50/reconfirm65/cap75/cashguard` 仍无法修复 2026 负收益；本轮按上一轮 `medium_cycle_growth`/本轮开局 `risk_reconfirm_sensitivity` 把 high-growth robust 邻域改成 `risk45 + reconfirm70 + cap75 + cashguard`，继续只跑等权/总市值双底座。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard`。实际命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly`。
- 等权版五窗口 CAGR 为 `29.52% / 48.00% / 35.59% / 101.37% / -8.75%`，最大回撤 `-20.44% / -23.39% / -26.33% / -14.29% / -12.98%`，换手 `3.96x / 4.25x / 4.47x / 7.32x / 6.44x`；总市值版为 `29.05% / 41.94% / 27.06% / 110.89% / -4.47%`，最大回撤 `-20.57% / -28.09% / -28.47% / -13.93% / -11.24%`。两者保留 2020 中周期收益，但 2023 回落且 2026 仍为负，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `656`，family 规模为 `emergent_theme_discovery=58 / high_growth_theme=303 / momentum_equal_weight_elastic=29 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=50`；`scripts/update_weighted_winners.py` 后 Path 2 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。候选池未触发 Path 2 evict。
- 最终 guard 下一轮 focus 转为 `underrepresented_families`。下一轮第一条命令不要继续只压 high-growth cap，建议补一个等权多因子弹性代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance` 或同等非 high-growth family，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass`，上一轮 `reconfirm70_cap85_cashguard` 仍未修复 2026 负收益；本轮按 `capacity_and_cost_stress` 把相同 high-growth robust 邻域进一步降到 `cap75`，继续只用等权/总市值双底座做五窗口确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard`。实际命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly`。
- 等权版五窗口 CAGR 为 `29.39% / 48.56% / 42.17% / 102.15% / -9.52%`，最大回撤 `-28.74% / -23.39% / -26.80% / -14.29% / -13.08%`，换手 `3.86x / 4.32x / 4.67x / 7.32x / 6.53x`；总市值版为 `28.56% / 42.48% / 32.81% / 111.67% / -5.21%`，最大回撤 `-28.87% / -28.09% / -29.07% / -13.93% / -11.24%`。cap75/cashguard 保留 2020/2023 中周期收益，但仍不能把 2026 转正，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `649`，family 规模为 `emergent_theme_discovery=55 / high_growth_theme=301 / momentum_equal_weight_elastic=28 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=49`；`scripts/update_weighted_winners.py` 后 Path 2 official winners/robust 未变化，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 Path 2 evict。最终 guard 下一轮 focus 为 `medium_cycle_growth`；下一轮第一条命令建议不要继续机械降 cap，改测恢复阈值/风险阈值折中，例如等权/总市值 `risk45_mom_exit60_reconfirm70_cap75_cashguard`，注册后五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass`，上一轮 `cap85_cashguard` 仍保留 2020/2023 中周期收益但 2026 为负；本轮按 `risk_reconfirm_sensitivity` 把恢复确认阈值提高到 `reconfirm70`，继续用等权/总市值双底座确认是否能修复 2026，而不是扩全量 high-growth 邻域。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard`。实际非阻塞 A股批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly`。
- 等权版五窗口 CAGR 为 `30.46% / 48.44% / 38.38% / 96.12% / -13.27%`，最大回撤 `-21.20% / -25.61% / -26.09% / -14.29% / -14.88%`，换手 `4.04x / 4.34x / 4.53x / 7.33x / 6.04x`；总市值版为 `30.05% / 41.81% / 28.08% / 106.76% / -10.78%`，最大回撤 `-21.36% / -30.06% / -28.60% / -14.61% / -13.84%`。两者仍未把 2026 转正，因此不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `643`，family 规模为 `emergent_theme_discovery=52 / high_concentration_breakout=154 / high_growth_theme=299 / momentum_equal_weight_elastic=28 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=48`。`scripts/update_weighted_winners.py` 后 official Path 2 winners/robust 切回验证更稳的 high-growth 组合：2017 robust 为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，2020/2023 分别仍由 `risk40...reconfirm70_cap95` 与 `risk50_ma_cap95` 领先；本轮 `reconfirm70_cap85_cashguard` 未替换 official。
- 候选池未触发 Path 2 evict。最终 guard 下一轮 focus 为 `capacity_and_cost_stress`；下一轮第一条命令建议回到 official robust 邻域做更直接容量/成本压力，而不是继续只调 reconfirm，例如实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap75_cashguard` 或同等更低 cap/cost 版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass`，上一轮 `cap75_biweekly_cost_guard` 确认双周 underrepresented family 长窗回撤过深；本轮按 rotation 的 `medium_cycle_growth` 回到 Path 2 high-growth robust 邻域，新增 `risk50 + reconfirm65 + cap85 + cashguard`，用等权/总市值双底座检查能否在保留 2020/2023 中周期收益的同时修复 2026。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard`。实际非阻塞 A股批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly`。
- 等权版五窗口 CAGR 为 `29.54% / 48.43% / 44.27% / 95.95% / -13.27%`，最大回撤 `-28.74% / -25.61% / -26.09% / -14.29% / -14.88%`，换手 `3.86x / 4.34x / 4.67x / 7.33x / 6.04x`；总市值版为 `28.59% / 41.79% / 33.53% / 106.58% / -10.78%`，最大回撤 `-28.87% / -30.06% / -28.60% / -14.61% / -13.84%`。cap85/cashguard 保留了 2020/2023 中周期收益，但 2026 仍为负，不替换 official winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `636`，family 规模为 `emergent_theme_discovery=49 / high_concentration_breakout=154 / high_growth_theme=297 / momentum_equal_weight_elastic=27 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=47`；raw robust 仍偏向 `risk40_mom_exit60_reconfirm75_caution80_cap95`，`scripts/update_weighted_winners.py` 后 official robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 Path 2 evict。收尾 guard 下一轮 focus 为 `risk_reconfirm_sensitivity`；下一轮第一条命令建议不要继续只调 cap，改测恢复确认阈值/谨慎仓组合对 2026 的影响，例如等权/总市值 `risk50_mom_exit60_reconfirm70_cap85_cashguard` 或 `risk45_mom_exit60_reconfirm65_caution75_cap85_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_reconfirm_sensitivity_ids>`。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `underrepresented_families`；本轮按计划新增一个双周成本守门代表，而不是继续扩大 high_growth family。Path 4 新注册先触发 blocking coverage，本轮已先按 guard 原始 Path 4 `--only-base-ids` 补齐后再执行 Path 2 非阻塞批次。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard`。实际命令见 Path 1 本轮 A股非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cap75_biweekly_cost_guard` 五窗口 CAGR 为 `3.08% / 10.20% / 26.95% / 65.20% / 34.60%`，最大回撤 `-64.94% / -57.72% / -30.61% / -26.92% / -14.68%`，换手 `4.50x / 4.69x / 4.96x / 9.28x / 11.23x`。它保留 2025/2026 弹性，但 2017/2020 深回撤确认双周 underrepresented family 仍不是可晋级中周期高收益原型。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `631`，family 规模为 `emergent_theme_discovery=47 / high_concentration_breakout=154 / high_growth_theme=295 / momentum_equal_weight_elastic=27 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=46`。raw robust 临时偏向 `risk40_mom_exit60_reconfirm75_caution80_cap95`，但 `scripts/update_weighted_winners.py` 后 official Path 2 winners 与 robust 仍未变化，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 Path 2 evict。收尾 focus 转向 `capacity_and_cost_stress`；下一轮第一条命令建议回到 official robust 邻域做容量/成本压力，而不是继续普通双周扩展，例如实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap85_cashguard` 或同等 cap85/cost 对照，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass`，上一轮 `cap70 cashguard` 仍未把 2026 转正；本轮按 `risk_reconfirm_sensitivity` 继续在 high_growth robust 邻域上增加谨慎仓阈值，用等权/总市值双底座确认 `caution75 + cap70 + cashguard` 是否能保留 2020/2023 中周期收益。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard`。实际非阻塞 A股批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly`。
- 等权版五窗口 CAGR 为 `29.37% / 48.74% / 41.44% / 105.48% / -7.67%`，最大回撤 `-29.05% / -22.88% / -27.27% / -14.29% / -12.64%`，换手 `3.86x / 4.32x / 4.68x / 7.31x / 6.78x`；总市值版为 `28.63% / 42.98% / 32.63% / 114.49% / -2.20%`，最大回撤 `-29.15% / -27.21% / -29.38% / -13.93% / -10.30%`。相对 cap70 旧版，2026 亏损缩窄但仍为负，未改变 official winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `626`，family 规模为 `emergent_theme_discovery=44 / high_concentration_breakout=154 / high_growth_theme=295 / momentum_equal_weight_elastic=27 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=45`。raw robust 仍偏向 `risk40_mom_exit60_reconfirm75_caution80_cap95`，但 `update_weighted_winners.py` official robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`，说明验证窗仍不接受本轮更强现金防守。
- 候选池未触发 cap evict。收尾 guard 给出下一轮 focus `underrepresented_families`；下一轮不要继续只压 high_growth cap，第一条命令建议实现一个双周或等权弹性代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_id>`。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass`，上一轮 `trend_industry_momentum` 等权弹性代表长窗回撤过深，本轮按 `capacity_and_cost_stress` 回到当前 high_growth robust 邻域，把上一轮 `cap80 cashguard` 继续压到 `cap70`，用等权/总市值双底座确认容量约束是否能修复 2026。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard`。实际命令见 Path 1 本轮 A股非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `29.29% / 48.57% / 41.20% / 105.24% / -7.62%`，最大回撤 `-28.74% / -22.88% / -27.15% / -14.29% / -12.60%`，换手 `3.85x / 4.31x / 4.67x / 7.31x / 6.77x`；总市值版为 `28.55% / 42.81% / 32.44% / 114.20% / -2.34%`，最大回撤 `-28.87% / -27.21% / -29.30% / -13.93% / -10.35%`。cap70 降低部分长窗回撤，但 2026 仍为负，未晋级 official。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `618`，family 规模为 `emergent_theme_discovery=41 / high_concentration_breakout=154 / high_growth_theme=293 / momentum_equal_weight_elastic=25 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=44`。raw robust 仍偏向 `risk50_mom_exit60_reconfirm75_caution75_cap95`，`update_weighted_winners.py` official robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 cap evict。收尾 guard 给出下一轮 focus `medium_cycle_growth`；下一轮不要继续只压 cap，第一条命令建议实现等权/总市值 `risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard`，检查谨慎仓阈值能否让 2026 转正且保留 2020/2023 中周期收益，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass`，上一轮建议把 focus 从 high_growth/cap80 邻域转向 `underrepresented_families`；本轮补 1 个 `momentum_equal_weight_elastic` 代表，使用等权底座的 `trend_industry_momentum` 多因子压力测试，而不是继续扩单一 high_growth family。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_trend_industry_momentum`。实际命令见 Path 1 本轮 A股合并命令，命令类型为五窗口 `--only-base-ids` 增量确认。
- `equal_weight trend_industry_momentum` 五窗口 CAGR 为 `15.32% / 18.36% / 30.98% / 91.55% / 79.34%`，最大回撤 `-37.83% / -39.59% / -31.78% / -11.52% / -10.89%`，换手 `3.28x / 3.70x / 3.99x / 5.51x / 7.75x`；2025/2026 弹性尚可，但 2017/2020 回撤和收益均弱于 Path 2 robust，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `612`，`momentum_equal_weight_elastic=25`、`weekly_rebalance_aggressive=43`；raw robust 仍偏向 `risk50_mom_exit60_reconfirm75_caution75_cap95`，`update_weighted_winners.py` official robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，`meanCAGR=60.27% / minCAGR=36.23%`。
- 候选池未触发 cap evict。收尾 guard 的下一轮 focus 为 `capacity_and_cost_stress`，第一条命令建议不要复制本轮弱多因子，而是回到当前 robust 邻域做更严格容量/成本确认：实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap70_cashguard` 或同等 cap70 成本守门候选，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass`，上一轮 `risk50_mom_exit60_reconfirm65_cap80_cost_guard` 保留中周期收益但 2026 仍负；本轮按 `risk_reconfirm_sensitivity`/2026 防守缺口，在相同 cap80 邻域切到 `cashguard`，继续只用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard`。实际命令见 Path 1 本轮合并命令，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `29.50% / 48.50% / 43.30% / 99.10% / -11.40%`，最大回撤 `-28.70% / -24.50% / -26.40% / -14.30% / -13.90%`，换手 `3.86x / 4.33x / 4.67x / 7.33x / 6.29x`；总市值版为 `28.60% / 42.20% / 33.20% / 109.00% / -8.00%`，最大回撤 `-28.90% / -29.00% / -28.80% / -13.90% / -12.50%`。cashguard 降低了长窗回撤，但仍不能把 2026 转正，未晋级 official。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `607`，family 规模为 `emergent_theme_discovery=35 / high_concentration_breakout=154 / high_growth_theme=291 / momentum_equal_weight_elastic=24 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=42`；raw robust 临时偏向 `risk50_mom_exit60_reconfirm75_caution75_cap95`，但 `update_weighted_winners.py` official robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 cap evict。收尾 guard 将下一轮 focus 转到 `underrepresented_families`，因此不要继续只扩 high_growth/cap80 邻域；第一条命令建议补一个 `momentum_equal_weight_elastic` 或双周代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_trend_industry_momentum` 或一个低回撤双周成本候选，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_id>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass`，上一轮 `cap70_biweekly` 确认双周 underrepresented family 的 2017/2020 回撤不可接受；本轮按上一轮下一步和 candidate-pass raw robust 线，转向当前高收益 robust 邻域的容量/成本压力，不继续扩大双周失败支线。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard`。实际命令见 Path 1 本轮合并命令。
- 等权版五窗口 CAGR 为 `34.10% / 56.20% / 56.46% / 99.55% / -12.18%`，最大回撤 `-39.23% / -33.08% / -33.27% / -14.29% / -13.97%`，换手 `4.12x / 4.65x / 4.49x / 7.34x / 6.38x`；总市值版为 `33.32% / 49.16% / 47.72% / 109.53% / -8.78%`，最大回撤 `-39.58% / -33.47% / -35.16% / -14.51% / -12.54%`。cap80 保留 2020/2023 高收益，但 2026 仍为负，未晋级 official。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `602`，family 规模为 `emergent_theme_discovery=33 / high_concentration_breakout=154 / high_growth_theme=289 / momentum_equal_weight_elastic=24 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=41`。raw robust 临时切到 `risk50_mom_exit60_reconfirm75_caution75_cap95`，但 `update_weighted_winners.py` official robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`，说明 validation 仍偏好旧恢复确认形态。
- 候选池未触发 cap evict；本轮结论是容量 cap80 不是解决 2026 负收益的充分条件。下一轮 focus -> candidates 池优先做 `2026 defense without killing 2020/2023`：第一条命令建议实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap80_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path2_cap80_cashguard_ids>`；若继续成本线，先记录本轮 `cap80_cost_guard` 为 2026 失败对照。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 继续指向 `underrepresented_families`；上一轮 80/20 等权双周 cap60 深回撤，本轮不再扩 high_growth 邻域，改测 70/30 等权双周 cap70。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly`。实际命令见 Path 1 本轮合并命令。
- `cap70_biweekly` 五窗口 CAGR 为 `3.98% / 10.04% / 24.39% / 71.47% / 40.86%`，最大回撤 `-56.21% / -53.86% / -28.69% / -21.50% / -13.12%`，换手 `4.81x / 5.25x / 6.01x / 11.72x / 12.33x`；70/30 提高短窗弹性但 2017/2020 回撤仍不可接受，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `595`，family 规模为 `emergent_theme_discovery=30 / high_concentration_breakout=154 / high_growth_theme=287 / momentum_equal_weight_elastic=23 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=40`；`update_weighted_winners.py` 后 Path 2 official winners 与 robust 未变，robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 cap evict；本轮确认说明双周 underrepresented family 的主要问题仍是长窗回撤和 2020 收益不足，而不是单纯 cap 太低。
- 收尾 guard 后 rotation 切到 `capacity_and_cost_stress`。下一轮第一条命令建议围绕当前 robust 直接做容量/成本压力：实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap80_cost_guard` 双底座，用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path2_capacity_cost_ids>` 增量确认；若仍要继续双周 underrepresented family，先把 `cap70_biweekly` 作为失败对照，不再扩大高回撤邻域。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `reconfirm70 cap80 cashguard` 没能修复 2026，本轮按当前 rotation 的 `underrepresented_families` 不再加 high_growth 邻域，转向双周代表候选。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly`。
- 该双周 cap60 五窗口 CAGR 为 `3.74% / 10.33% / 26.59% / 67.99% / 48.67%`，最大回撤 `-62.70% / -56.35% / -30.61% / -26.92% / -14.21%`，换手 `4.31x / 4.65x / 4.97x / 9.41x / 11.68x`；2025/2026 弹性不够抵消 2017/2020 深回撤，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `590/590 complete`，`biweekly_rebalance_aggressive=19`、`weekly_rebalance_aggressive=39`、`emergent_theme_discovery=27`；`update_weighted_winners.py` 后 Path 2 official winners 与 robust 未变，robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 cap evict；本轮新增确认说明普通 80/20 等权双周 cap60 不能作为中周期高收益原型，只保留为 underrepresented family 失败对照。
- 下一轮 focus -> candidates 池：如果仍是 `underrepresented_families`，第一条命令建议测试更高弹性的 `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly`；若 rotation 回到风险确认线，再执行上一轮未跑的 `risk40_mom_exit60_reconfirm70_cap75_cashguard` 等权/总市值双底座，均用五窗口 `--only-base-ids`。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `reconfirm75 cap80 cashguard` 保留 2020/2023 高收益但 2026 仍负，本轮按 `risk_reconfirm_sensitivity` 把恢复确认放宽到 `70`，继续只测等权/总市值双底座。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard`。实际回测命令见 Path 1 本轮合并命令。
- 等权版五窗口 CAGR 为 `29.99% / 48.24% / 37.08% / 98.80% / -11.01%`，最大回撤 `-20.84% / -24.48% / -26.19% / -14.29% / -13.93%`，换手 `4.00x / 4.29x / 4.50x / 7.33x / 6.24x`；总市值版为 `29.55% / 41.91% / 27.59% / 108.77% / -7.64%`，最大回撤 `-20.92% / -28.98% / -28.47% / -13.93% / -12.54%`。放宽确认改善 2020 与 2017 回撤，但 2023/2026 不足，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `585/585 complete`，family 规模为 `high_concentration_breakout=154 / high_growth_theme=287 / momentum_equal_weight_elastic=23 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=38 / emergent_theme_discovery=24`。`update_weighted_winners.py` 后 Path 2 official winners 与 robust 未变化，robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 收尾 guard 为 `pass`，Path 2 rotation 为 `stagnation_runs=5 / risk_reconfirm_sensitivity / rotate`；候选池未触发 evict。下一轮 focus -> candidates 池继续恢复确认/风控敏感性，但要解决 2026 负收益，第一条命令建议实现 `risk40_mom_exit60_reconfirm70_cap75_cashguard` 的等权/总市值双底座，并用五窗口 `--only-base-ids <next_reconfirm_sensitivity_ids>` 增量确认。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `cap80 + cost_guard` 保留了 2020/2023 高收益但 2026 仍为负，本轮按 `medium_cycle_growth` 的防守修复补 `cap80 + cashguard` 等权/总市值双底座。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard`。实际回测命令见 Path 1 本轮合并命令。
- 等权版五窗口 CAGR 为 `29.48% / 41.80% / 37.02% / 107.86% / -10.99%`，最大回撤 `-30.99% / -31.34% / -26.24% / -11.51% / -13.93%`，换手 `3.67x / 4.20x / 4.50x / 7.30x / 6.24x`；总市值版为 `28.55% / 35.75% / 27.54% / 118.98% / -7.62%`，最大回撤 `-31.04% / -31.20% / -28.52% / -13.62% / -12.54%`。现金防守降低长窗收益且 2026 仍未转正，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `578/578 complete`；family 规模为 `high_concentration_breakout=154 / high_growth_theme=285 / momentum_equal_weight_elastic=22 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=37 / emergent_theme_discovery=21`。`update_weighted_winners.py` 后 Path 2 official winners 未变化，robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`，`meanCAGR=64.55% / minCAGR=37.34% / worstMaxDD=-40.74% / meanTurn=5.20`。
- 收尾 guard 为 `pass`，Path 2 rotation 为 `stagnation_runs=2 / medium_cycle_growth / continue`；候选池未触发 evict。下一轮 focus -> candidates 池继续中周期高收益，但要优先修复 2026 防守，第一条命令建议实现 `risk40_mom_exit60_reconfirm70_cap80_cashguard` 的等权/总市值双底座，并用五窗口 `--only-base-ids <next_medium_cycle_growth_ids>` 增量确认。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮等权弹性/多因子代表未晋级，最终 focus 指向 `capacity_and_cost_stress`。本轮按当前 high-growth robust 的容量压力测试，只补 `cap80 + cost_guard` 等权/总市值双底座。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard`。实际回测命令见 Path 1 本轮合并命令。
- 等权版五窗口 CAGR 为 `36.69% / 49.57% / 49.54% / 108.61% / -10.84%`，最大回撤 `-32.93% / -32.18% / -29.14% / -11.53% / -13.93%`，换手 `3.67x / 4.30x / 4.35x / 7.32x / 6.33x`；总市值版为 `34.36% / 43.02% / 42.68% / 122.70% / -6.91%`，最大回撤 `-33.20% / -32.40% / -30.81% / -14.15% / -12.54%`。容量约束保留了 2020/2023 高收益，但 2026 仍为负，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `571/571 complete`；family 规模为 `high_concentration_breakout=154 / high_growth_theme=283 / momentum_equal_weight_elastic=21 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=37 / emergent_theme_discovery=18`。raw robust 仍为 `risk40_mom_exit60_reconfirm75_caution80`，official robust 仍为 `risk40_mom_exit60_reconfirm75_cap95`。
- `update_weighted_winners.py` 后 Path 2 official winners 未变化：2017 `risk40_mom_exit60_reconfirm75_cap95`，2020 `risk40_mom_exit60_reconfirm70_cap95`，2023 `risk50_ma_cap95`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；候选池未触发 evict。
- 最终 guard 后 rotation 为 `stagnation_runs=12 / medium_cycle_growth / rotate`；下一轮 focus -> candidates 池回到中周期高收益原型，但必须带 2026 防守约束。第一条候选命令建议实现 `risk40_mom_exit60_reconfirm75_cap80_cashguard` 的等权/总市值双底座，并用五窗口 `--only-base-ids <next_medium_cycle_growth_ids>` 增量确认。

## 本轮执行计划（2026-05-20 13:58 CST）

- 上一轮 Path 2 rotation 指向 `underrepresented_families`，且 high_growth 已扩到 `281`；本轮只补 1 个等权弹性/多因子代表，不继续加 high_growth 邻域。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense`。实际回测命令见 Path 1 本轮合并命令。
- `core_multifactor_quality_defense` 五窗口 CAGR 为 `9.71% / 13.45% / 26.85% / 50.12% / 69.97%`，最大回撤 `-51.64% / -41.68% / -30.97% / -15.53% / -13.55%`，换手 `3.21x / 3.54x / 3.95x / 5.45x / 6.62x`；短窗尚可，但 2017/2020 收益和回撤明显弱于 Path 2 robust，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `565/565 complete`；family 规模为 `high_concentration_breakout=154 / high_growth_theme=281 / momentum_equal_weight_elastic=21 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=36 / emergent_theme_discovery=15`。raw robust 仍为 `risk40_mom_exit60_reconfirm75_caution80`，official robust 仍为 `risk40_mom_exit60_reconfirm75_cap95`。
- `update_weighted_winners.py` 后 Path 2 official winners 未变化：2017 `risk40_mom_exit60_reconfirm75_cap95`，2020 `risk40_mom_exit60_reconfirm70_cap95`，2023 `risk50_ma_cap95`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；候选池未触发 evict。
- 最终 guard 后 rotation 为 `stagnation_runs=9 / capacity_and_cost_stress / rotate`；下一轮 focus -> candidates 池先对当前 high-growth robust 做容量/换手压力，而不是继续扩大弱等权弹性。第一条命令建议先实现 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard` 与对应总市值版本，再用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <capacity_cost_ids>` 补跑。

## 本轮执行计划（2026-05-20 05:20 CST）

- 上一轮提示为 `risk35/40`、`reconfirm75/80` 与 `caution65/70` 的交互；本轮在完成 Path 4 coverage block 后，沿 `risk_reconfirm_sensitivity` 新增 `risk35/reconfirm75/caution70` 与 `risk40/reconfirm80/caution70` 两个变体，并同时测试等权/总市值双底座。
- 本轮新增并五窗口确认 4 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95`、`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95`。实际回测命令见 Path 1 本轮合并命令。
- `risk35/reconfirm75/caution70` 等权版五窗口 CAGR 为 `35.44% / 50.05% / 49.04% / 100.99% / -14.08%`，总市值版为 `34.43% / 42.78% / 41.80% / 113.32% / -12.70%`；长窗仍强，但 2026 防守失败，且不如当前 official robust 的 2017/2020 平衡。
- `risk40/reconfirm80/caution70` 等权版五窗口 CAGR 为 `30.99% / 29.95% / 47.87% / 81.84% / -15.20%`，总市值版为 `29.19% / 24.09% / 39.48% / 94.63% / -13.84%`；恢复确认过严明显牺牲 2020/2017，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `560`，新增独立 `emergent_theme_discovery=12`；family 规模为 `high_concentration_breakout=154 / high_growth_theme=281 / momentum_equal_weight_elastic=19 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=35`。raw robust 仍为 `risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`。
- `update_weighted_winners.py` 后 Path 2 official winners 未变化：2017 `risk40_mom_exit60_reconfirm75_cap95`，2020 `risk40_mom_exit60_reconfirm70_cap95`，2023 `risk50_ma_cap95`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust 仍为 `risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=61.28% / minCAGR=38.32% / worstMaxDD=-32.76% / meanTurn=4.98`。
- Guard 收尾为 `pass`，Path 2 rotation 为 `stagnation_runs=6 / underrepresented_families / rotate`；未触发 evict，但 high_growth 已扩到 `281`，下一轮新增前优先补 `momentum_equal_weight_elastic` 或双周/周频代表，不再继续只加 high_growth。
- 下一轮第一条候选命令建议先实现 `aggr_08_92_prom6_core_multifactor_quality_defense` 在 `core_explore_80_20_equal_weight_winner_core` 与 `core_explore_90_10_equal_weight_winner_core` 的等权弹性版本，或一个双周成本候选，然后用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <underrepresented_family_ids>` 补跑。

## 本轮执行计划（2026-05-19 23:14 CST）

- 上一轮 `risk40_mom_exit60_reconfirm65` 等权版成为 official 2017/2020 winner 与 robust，但 `since_2026_01` 仍为负；本轮按 `medium_cycle_growth` 的 2026 防守缺口，增加谨慎仓约束而不扩全量。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95` 与 `core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95`。实际命令与 Path 1/3 合并执行：
  `.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly`。
- 新 `caution70` 等权版五窗口 CAGR 为 `33.78% / 55.33% / 53.79% / 92.06% / -14.10%`，总市值版为 `32.83% / 47.78% / 45.75% / 103.20% / -12.72%`；相对上一轮 `reconfirm65` 的 2026 负收益有所收窄，但牺牲 2017/2020/2023 与 2025 弹性，未替换 official robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `541/541 complete`，五族规模为 `high_concentration_breakout=154 / high_growth_theme=277 / momentum_equal_weight_elastic=19 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=33`；未触发 evict。
- family-ranked raw robust 仍偏向 `risk40_mom_exit60_reconfirm75_caution80`，但 `update_weighted_winners.py` official 口径同步为：2017 `risk40_mom_exit60_reconfirm75_cap95`，2020 `risk40_mom_exit60_reconfirm70_cap95`，2023 `risk50_ma_cap95`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust 为 `risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=61.28% / minCAGR=38.32% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 rotation 为 `stagnation_runs=3 / risk_reconfirm_sensitivity / rotate`；下一轮 focus -> candidates 池优先比较 `risk35/40`、`reconfirm75/80` 与 `caution65/70` 的交互，不继续只加高收益族。建议先实现 `risk35_mom_exit60_reconfirm75_caution70_cap95` 和 `risk40_mom_exit60_reconfirm80_caution70_cap95` 的等权/总市值双底座，并用五窗口 `--only-base-ids` 增量补跑。

## 本轮执行计划（2026-05-19 17:26 CST）

- 本轮沿 `medium_cycle_growth` 新增 3 个高收益参数变体，并对等权/总市值两套底座共 `6` 个 base id 做五窗口 `--only-base-ids` 增量确认：`risk45_mom_exit60_reconfirm70`、`risk40_mom_exit55_reconfirm70`、`risk40_mom_exit60_reconfirm65`。
- `scripts/path2_candidate_pass.py` 后 candidate universe 变为 `536`，五族规模为 `high_concentration_breakout=154 / high_growth_theme=275 / momentum_equal_weight_elastic=19 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=31`。
- 新 `risk40_mom_exit60_reconfirm65` 等权版成为 2017/2020 official winner 与四窗口 robust：2017 `35.89% CAGR / -33.25% MaxDD / 0.97 Sharpe / 3.98 Turn`，2020 `58.60% / -28.34% / 1.24 / 4.49`，2023 `55.88% / -29.20% / 1.28 / 4.19`，2025 `97.78% / -14.29% / 1.78 / 7.39`。
- 其他新变体也有效抬高上限：`risk45_mom_exit60_reconfirm70` 等权版成为 2023 official winner（`57.56% CAGR / -31.31% MaxDD / 1.29 Sharpe / 4.32 Turn`），`risk40_mom_exit55_reconfirm70` 总市值版成为 2025 official winner（`108.88% CAGR / -16.71% MaxDD / 1.83 Sharpe / 6.77 Turn`）。
- 四窗口 official robust candidate 切换为等权 `risk40_mom_exit60_reconfirm65`，`meanCAGR=62.04% / minCAGR=35.89% / worstMaxDD=-33.25% / meanTurn=5.01`；但新高收益族在 `since_2026_01` 均为负（等权约 `-16.78%`、总市值约 `-15.07%`），下一轮要加 2026 风控/确认约束。
- 收尾 rotation 为 `stagnation_runs=1 / medium_cycle_growth / continue`；下一轮第一优先命令应围绕当前 robust 做 `caution/现金防守/恢复确认` 变体的 `--only-base-ids` 增量补跑。

## 本轮执行计划（2026-05-19 11:12 CST）

- 本轮按 `medium_cycle_growth` 轮换方向先做既有候选巡检；`scripts/path2_candidate_pass.py` 继续保持 `524` 个 candidate，五族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=16 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=28`。
- family-ranked raw winners 仍集中在旧中周期高收益原型：2017 `risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `risk40_mom_exit60_reconfirm70`（`58.60%`），2023 `risk50_ma`（`65.59%`），2025 高换手 weekly `cap100_weekly`（`198.70% / 16.79 Turn`）。
- `update_weighted_winners.py` 的 official 口径切回更稳的 Path 1 邻近候选：2017/2020/2025 为 `aggr_05_95_prom7`，2023 为等权 `aggr_10_90_prom6_core_multifactor_balanced`。
- 四窗口 official robust candidate 切换为 `aggr_05_95_prom7`，`meanCAGR=41.87% / minCAGR=22.00% / worstMaxDD=-27.88% / meanTurn=3.19`；raw high-growth 上限继续只作为观察，不直接晋升。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 重置为 `stagnation_runs=0 / medium_cycle_growth / continue`；本轮没有继续扩大 `high_growth_theme` 数量，下一轮按 report quota 优先用中周期高收益原型做风险确认、成本和回撤压测，同时保持五个 family 的代表性。

## 本轮执行计划（2026-05-19 05:29 CST）

- 本轮按 `underrepresented_families` 轮换方向扩展候选池：等权/总市值多因子弹性加入 `aggr_08_92_prom6_core_multifactor_balanced` 与 `aggr_10_90_prom6_core_multifactor_balanced`，双周加入 `cap70/cap50` 两个代表，周频成本压力加入 `cap65_hold5_turn15` 与 `cap60_hold6_turn12`。
- 独立复跑 `scripts/path2_candidate_pass.py` 后，candidate universe 为 `524/524 complete`；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=16 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=28`。
- family-ranked raw winners 仍集中在旧中周期高收益原型：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.60%`），2023 `1/99 risk50_ma`（`65.59%`），2025 高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`198.70% / 16.79 Turn`）。
- 新双周 `cap70/cap50` 在 2020 窗口约 `10.16%/10.13% CAGR` 且回撤偏深；新增多因子弹性在 official weighted 口径更稳，推动 Path 2 official tracked/robust 同步到 `aggr_10_90_prom6_core_multifactor_balanced`。
- `update_weighted_winners.py` 后 Path 2 official window winners 为：2017 `aggr_10_90_prom6_core_multifactor_balanced`，2020 `aggr_08_92_prom6_core_multifactor_balanced`，2023 `aggr_10_90_prom6_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_multifactor_balanced`。
- 四窗口 official robust candidate 为 `aggr_10_90_prom6_core_multifactor_balanced`，`meanCAGR=35.95% / minCAGR=14.72% / worstMaxDD=-41.55% / meanTurn=4.03`；raw high-growth 上限继续作为观察，不直接晋升。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 重置为 `stagnation_runs=0 / recommended_focus=medium_cycle_growth / continue`；下一轮继续用中周期高收益原型做确认，而不是再单纯扩大 high_growth 数量。

## 本轮执行计划（2026-05-18 23:13 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，candidate universe 继续为 `516/516 complete`；五个候选族规模保持 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=12 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.60%`），2023 `1/99 risk50_ma`（`65.59%`），2025 高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`198.70% / 16.79 Turn`）。
- candidate-pass raw robust 仍为 `2/98 risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`，继续作为观察，不直接晋升 official。
- `update_weighted_winners.py` 验证后，Path 2 official tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.37% / minCAGR=38.58% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=30 / recommended_focus=underrepresented_families / rotate`；下一轮优先按配额补等权动量、双周与周频代表性，不继续让 high_growth family 单独扩张。

## 本轮执行计划（2026-05-18 20:34 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，candidate universe 继续为 `516/516 complete`；五个候选族规模保持 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=12 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.72%`），2023 `1/99 risk50_ma`（`65.81%`），2025 高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% / 16.33 Turn`）。
- candidate-pass raw robust 仍为 `2/98 risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`，继续作为观察，不直接晋升 official。
- `update_weighted_winners.py` 验证后，Path 2 official tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=28 / recommended_focus=risk_reconfirm_sensitivity / rotate`；下一轮优先比较 `risk40/risk50` 与恢复确认阈值敏感性，同时保持五个 family 不被 high_growth 压扁。

## 本轮执行计划（2026-05-18 11:11 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，candidate universe 继续为 `516/516 complete`；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=12 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.72%`），2023 `1/99 risk50_ma`（`65.81%`），2025 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% / 16.33 Turn`）。
- candidate-pass raw robust 仍为 `2/98 risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`，继续只作为观察，不晋升 official。
- `update_weighted_winners.py` 验证后，Path 2 official tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=23 / recommended_focus=capacity_and_cost_stress / rotate`；下一轮优先做容量、回撤、换手与交易成本压力，不继续只扩 high_growth family。

## 本轮执行计划（2026-05-18 05:53 CST）

- 本轮按 `underrepresented_families` 方向微扩候选池，将 `aggr_08_92_prom6_core_6_1` 与 `aggr_10_90_prom6_core_6_1` 纳入 `momentum_equal_weight_elastic`；独立复跑 `scripts/path2_candidate_pass.py` 后候选宇宙为 `516/516 complete`。
- 五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=12 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`，未继续由单一 high_growth family 压扁。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.72%`），2023 `1/99 risk50_ma`（`65.81%`），2025 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% / 16.33 Turn`）。
- `update_weighted_winners.py` 验证后，Path 2 official tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=20 / recommended_focus=underrepresented_families / rotate`；下一轮继续按配额补等权动量、双周和周频代表性。

## 本轮执行计划（2026-05-17 23:12 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70_caution80`（`58.78%`），2023 `1/99 risk50_ma`（`65.81%`）。
- 2025 raw leader 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% CAGR / -39.39% MaxDD / 16.33 Turn`），但 `update_weighted_winners.py` 继续因 2023 验证窗口不足拒绝其进入 official winner。
- Path 2 official tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 official robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`；candidate-pass raw robust 切到 `2/98 risk40_mom_exit60_reconfirm75_caution80`，作为观察不晋升。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=18 / recommended_focus=underrepresented_families / rotate`；下一轮按配额优先补等权动量、双周与周频代表性，不让 high_growth family 继续压扁候选池。

## 本轮执行计划（2026-05-17 17:25 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 仍为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`）。
- 2025 raw leader 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% CAGR / 16.33 Turn`），但 `update_weighted_winners.py` 继续因验证窗口不足拒绝其进入 official winner。
- Path 2 official tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=15 / recommended_focus=risk_reconfirm_sensitivity / rotate`；下一轮优先做 `risk40/risk50` 再确认阈值敏感性。

## 本轮执行计划（2026-05-17 11:15 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 仍集中在中周期高收益原型：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`），2025 raw leader 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% / Turn=16.33`）。
- `update_weighted_winners.py` 验证后，2025 weekly raw leader 继续因 2023 验证窗口不足被拒；Path 2 tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- Guard 对 Path 2 candidate universe 为 `513/513 complete / pass`，收尾 rotation 为 `stagnation_runs=12 / recommended_focus=medium_cycle_growth / rotate`。
- 下一轮按 medium-cycle growth 继续扩展和压测中周期高收益原型，同时保持五个 family 的代表性，避免 high_growth family 单独压扁候选池。

## 本轮执行计划（2026-05-17 05:15 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates，五个候选族规模仍为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`），2025 仍为高换手纯周频 `aggr_01_99_prom1...cap100_weekly`（`197.61% / Turn=16.33`）。
- `update_weighted_winners.py` 验证后，2025 weekly raw leader 继续因 2023 验证窗口不足被拒；Path 2 tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 对 Path 2 candidate universe 为 `513/513 complete / pass`，rotation 为 `stagnation_runs=10 / recommended_focus=capacity_and_cost_stress / rotate`。
- 下一轮优先做容量、回撤、换手与交易成本压力测试，并按配额继续保留 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive` 的代表性，不让 high_growth family 继续压扁候选池。

## 本轮执行计划（2026-05-16 23:12 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates，五个候选族继续为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`），2025 raw leader 仍为高换手纯周频 `aggr_01_99_prom1...cap100_weekly`（`197.61% / Turn=16.33`）。
- `update_weighted_winners.py` 验证后，2025 weekly raw leader 因 2023 验证窗口不足被拒；Path 2 tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 对 Path 2 candidate universe 为 `513/513 complete / pass`，rotation 为 `stagnation_runs=8 / recommended_focus=underrepresented_families / rotate`。
- 下一轮按配额优先补 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive` 的低代表性族，并继续压紧 family membership 口径。

## 本轮执行计划（2026-05-16 17:14 CST）

- 本轮先用本地 `summary.json` 重建 A 股 comparison 到 `8693` 行，解除 Path 2 coverage `block`；`scripts/path2_candidate_pass.py` 复跑后候选宇宙保持 `513` 个 base candidates。
- 五个候选族继续独立保留：`high_concentration_breakout=154`、`high_growth_theme=269`、`momentum_equal_weight_elastic=9`、`biweekly_rebalance_aggressive=16`、`weekly_rebalance_aggressive=25`；family membership 没有被单一高集中族压扁。
- Path 2 tracked winners 当前为：2017 `90/10 equal_weight risk40_mom_exit60_reconfirm75_cap95`（`38.66% CAGR / -32.76% MaxDD / 1.13 Sharpe / 3.79 Turn`），2020 `90/10 equal_weight risk40_mom_exit60_reconfirm70_cap95`（`58.72% / -28.34% / 1.25 / 4.49`）。
- 2023 winner 为 `90/10 equal_weight risk50_ma_cap95`（`65.81% CAGR / -36.51% MaxDD / 1.33 Sharpe / 4.79 Turn`）；2025 raw weekly 高弹性候选因 2023 验证不足被拒，official winner 仍为 `80/20 total_mv aggr_05_95_prom3_core_6_1_full_risk_cap60`（`143.76% / -17.33% / 2.12 / 5.94`）。
- 四窗口 robust candidate 仍为 `90/10 equal_weight risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 rotation 为 `stagnation_runs=6 / recommended_focus=underrepresented_families / rotate`；下一轮优先补 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive` 等低代表性族，而不是扩大短窗 weekly 爆发族。

## 本轮执行计划（2026-05-16 11:20 CST）

- 本轮先通过缓存重建解除 Path 2 aggregate coverage 的假性 blocking 缺口；最终 guard 对 Path 2 candidate universe 为 `513/513 complete / pass`。
- 独立复跑 `scripts/path2_candidate_pass.py` 后，candidate universe 为 `raw=513 / complete=513 / incomplete=0`，五族规模为 `154 / 269 / 9 / 16 / 25`，继续保持 `100+` 且未被单一 family 压扁。
- family-ranked winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`），2025 仍为高换手纯周频 `aggr_01_99_prom1...cap100_weekly`（`197.61% / Turn=16.33`）。
- family-ranked robust 为 `2/98 risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`。
- `update_weighted_winners.py` 验证后 Path 2 tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66%`。
- 收尾 rotation 为 `stagnation_runs=2 / recommended_focus=medium_cycle_growth / continue`；下一轮继续优先中周期高收益原型，并保留双周/周频 family 配额。

## 本轮执行计划（2026-05-16 06:56 CST）

- 本轮 guard 开局显示 Path 2 blocking coverage 缺口为 `284` 个，按 rerun commands 离线补跑后降到 `3` 个；已在 `WINNER_CORE_VARIANTS` 中补齐 `aggr_07_93_prom8 / aggr_07_93_prom8_ramp85 / share_12_88_hold_3_7` 三个被候选池引用但不可生成的变体，并复跑确认到 `blocking=0`。
- 重建后的 comparison universe 为 `8613` 行 / `2137` 个 base strategies；Path 2 active universe 为 `raw=513 / complete=513 / incomplete=0`，五族规模为 `154 / 269 / 9 / 16 / 25`，继续保持 `100+` 候选且未被单一 family 完全压扁。
- `path2_candidate_pass.py` 的 family-ranked winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`，2020 `2/98 risk40_mom_exit60_reconfirm70`，2023 `2/98 risk50_ma`，2025 短窗 raw leader 仍为高换手纯周频 `aggr_01_99_prom1...cap100_weekly`。
- family-ranked robust 为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap95`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`。
- `update_weighted_winners.py` 验证后 Path 2 tracked winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust 为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 rotation 为 `stagnation_runs=7 / recommended_focus=underrepresented_families / rotate`；下一轮按每族 `2` 个新增配额优先补 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`，不要继续只扩 high_growth_theme。

## 本轮执行计划（2026-05-15 15:16 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，family-ranked universe 仍为 `raw=536 / complete=473 / incomplete=63`；五族规模保持 `154 / 229 / 9 / 16 / 25`，候选宇宙继续满足 `100+` 规模且未被单一 high_growth family 压扁。
- `path2_candidate_pass.json` 同步修正了部分历史候选的可用窗口：若干 incomplete 候选已具备 `since_2025_01` 记录，当前主要缺口集中在 `since_2023_01`，不影响 active complete universe。
- family-ranked robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=65.09% / minCAGR=39.27% / worstMaxDD=-32.76% / meanTurn=4.98`。
- `update_weighted_winners.py` 后 tracked Path 2 仍由 `weekly_alpha_pullback` 纯周频族占据；四窗口 robust 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.95% / minCAGR=19.02% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 最终 rotation 为 `stagnation_runs=3 / recommended_focus=risk_reconfirm_sensitivity / rotate`；下一轮应优先围绕 `risk40/risk50` 的再确认阈值与风险降仓敏感性做中周期验证，同时继续复核 Path 2 是否应允许纯周频族主导 tracked 口径。

## 本轮执行计划（2026-05-15 10:14 CST）

- 本轮在修复 aggregate 覆盖后复跑 `scripts/path2_candidate_pass.py`，family-ranked universe 恢复为 `raw=536 / complete=473 / incomplete=63`；五族规模为 `154 / 229 / 9 / 16 / 25`，新增 `weekly_alpha_*` 只扩充单周调仓族，没有压扁高集中、高成长、动量或双周 family。
- family-ranked Path 2 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=65.09% / minCAGR=39.27% / worstMaxDD=-32.76% / meanTurn=4.98`。
- `update_weighted_winners.py` 的 tracked Path 2 本轮切到纯周频 `weekly_alpha_pullback` 族：2017/2020 robust leg 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，2023 为 `aggr_08_92_prom6_weekly_alpha_pullback_risk50_cap40_hold2_turn40_weekly`，2025 为 `aggr_05_95_prom3_weekly_alpha_pullback_risk50_cap60_hold2_turn30_weekly`。
- weighted Path 2 robust 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.95% / minCAGR=19.02% / worstMaxDD=-37.64% / meanTurn=6.07`；最终 rotation 为 `stagnation_runs=1 / medium_cycle_growth`，下一轮应确认 Path 2 tracked 口径是否继续允许纯周频族主导。

## 本轮执行计划（2026-05-14 22:55 CST）

- 本轮优先修复 guard blocking coverage：Path 2 active universe 的 `since_2025_01` aggregate 缺口已通过阻塞 rerun 与五窗口 `strategy_comparison.csv` 重建补齐，收尾 guard 为 `pass`。
- `path2_candidate_pass.py` 在当前脚本口径下只输出 `candidate_count=1` 的严格候选 shortlist，robust 为 `aggr_10_90_fast_ramp_cash_off`；但 `update_weighted_winners.py` 仍基于完整 comparison universe 更新 Path 2 tracked winners。
- Path 2 tracked winners 已同步为：2017 `2/98 risk40_mom_exit60_reconfirm75`（`39.27% CAGR / -32.76% MaxDD / 1.1468 Sharpe / 3.79 Turn`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`59.78% / -28.34% / 1.2602 / 4.49`），2023 `1/99 risk50_ma`（`67.87% / -36.51% / 1.3606 / 4.79`），2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`（`148.68% / -17.33% / 2.1665 / 5.94`）。
- 四窗口 robust candidate 为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=65.09% / minCAGR=39.27% / worstMaxDD=-32.76% / meanTurn=4.98`；最终 guard 为 `stagnation_runs=1 / recommended_focus=medium_cycle_growth`，下一轮优先处理 candidate-pass family shortlist 过窄的问题，再继续中周期扩展。

## 本轮执行计划（2026-05-14 15:10 CST）

- 本轮起止两次运行研究守卫，收尾 coverage gate 为 `pass`，Path 2 active universe 继续为 `455` 个四窗口完整候选，另有不完整历史候选仅保留追溯；收尾 rotation 为 `stagnation_runs=13 / recommended_focus=medium_cycle_growth`。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，五个 family 规模仍为 `154 / 229 / 9 / 16 / 16`，分别对应高集中突破、高成长主线、动量/等权高弹性、双周调仓高收益、单周调仓高收益；本轮先完成巡检和同步，未新增代码候选。
- raw `since_2025_01` leader 仍是纯周度 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`195.54% CAGR / -40.77% MaxDD / 1.7685 Sharpe / 16.36 Turnover`；验证口径继续因 2023 窗口失效拒绝其进入 Path 2 tracked winner。
- 验证后 Path 2 tracked winners 未换身份：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 最新指标分别为 `39.66% / 60.45% / 69.21% / 154.34% CAGR`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=66.44% / minCAGR=39.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 下一轮按 report quota 每族 `2` 个新增配额推进，优先 `medium_cycle_growth`：在中周期高收益原型上比较更宽退出、低成本确认与不同底座，而不是继续让 high_growth_theme 单独扩张。

## 本轮执行计划（2026-05-14 09:13 CST）

- 本轮起止两次运行研究守卫，收尾 coverage gate 为 `pass`，Path 2 active universe 继续为 `455` 个四窗口完整候选，另有 `23` 个不完整历史候选仅保留追溯；收尾 rotation 为 `stagnation_runs=11 / recommended_focus=capacity_and_cost_stress`。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，五个 family 规模仍为 `154 / 229 / 9 / 16 / 16`，分别对应高集中突破、高成长主线、动量/等权高弹性、双周调仓高收益、单周调仓高收益；本轮没有继续扩大 `high_growth_theme` 邻域。
- raw `since_2025_01` leader 仍是纯周度 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`195.54% CAGR / -40.77% MaxDD / 1.7685 Sharpe / 16.36 Turnover`；验证口径继续因 2023 窗口失效拒绝其进入 Path 2 tracked winner。
- 验证后 Path 2 tracked winners 未换身份：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 最新指标分别为 `39.66% / 60.45% / 69.21% / 154.34% CAGR`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=66.44% / minCAGR=39.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 下一轮按 report quota 每族 `2` 个新增配额，但应先做 `capacity_and_cost_stress`：优先对现有中周期强点做容量、回撤、换手成本压力，而不是继续让高成长主线压扁 family membership。

## 本轮执行计划（2026-05-14 03:17 CST）

- 本轮 guard 覆盖率为 `pass`，Path 2 active universe 继续为 `455` 个四窗口完整候选，另有 `23` 个不完整历史候选仅保留追溯；收盘 guard 将 Path 2 rotation 推进到 `stagnation_runs=9 / recommended_focus=capacity_and_cost_stress`。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，五个 family 规模为 `154 / 229 / 9 / 16 / 16`，分别对应高集中突破、高成长主线、动量/等权高弹性、双周调仓高收益、单周调仓高收益；本轮不继续扩 `high_growth_theme` 邻域。
- raw `since_2025_01` leader 仍是纯周度 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`195.54% CAGR / -40.77% MaxDD / 1.7685 Sharpe / 16.36 Turnover`；验证口径继续因 2023 窗口失效拒绝。
- 验证后 Path 2 tracked winners 未换身份：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 最新指标分别为 `39.66% / 60.45% / 69.21% / 154.34% CAGR`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=66.44% / minCAGR=39.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 下一轮新增候选按 report quota 每族 `2` 个优先补 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`，并在 `capacity_and_cost_stress` 下约束容量、回撤与换手，避免让高成长主线继续压扁 family membership。

## 本轮执行计划（2026-05-13 21:21 CST）

- 本轮先按 guard 补跑 Path 2 blocking rerun commands；其中 23 个历史候选已不再由当前回测生成器实际产出，因此同步修正 `scripts/path2_candidate_pass.py`：active universe 只纳入四窗口完整候选，并把不完整历史候选写入 `incomplete_candidates` 供追溯。
- 修正后 Path 2 active universe 为 `455`，raw universe 为 `478`，incomplete historical candidates 为 `23`；五个 family 规模为 `154 / 229 / 9 / 16 / 16`，仍保持 `100+` 候选和五族独立观察，未被单一高集中 family 压扁。
- Path 2 raw `since_2025_01` leader 仍是纯周度 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`195.54% CAGR / -40.77% MaxDD / 1.7685 Sharpe / 16.36 Turnover`；验证口径继续因 2023 失效拒绝其进入 Path 2 winner。
- 验证后 Path 2 tracked winners 未换身份：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 最新指标分别为 `39.66% / 60.45% / 69.21% / 154.34% CAGR`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=66.44% / minCAGR=39.66% / worstMaxDD=-32.76% / meanTurn=4.98`。rotation 已提示下一轮转向 `underrepresented_families`，优先补强等权动量/双周/周频代表而非继续只扩 high_growth_theme。

## 本轮执行计划（2026-05-13 09:13 CST）

- 本轮复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，候选宇宙继续维持 `478`，五个 family 规模仍为 `159 / 237 / 16 / 16 / 16`；`risk40_mom_exit60_reconfirm*_caution80` 仍只扩充 `high_growth_theme`，没有压扁其他 family。
- raw 扫描的 `since_2025_01` 单窗口 leader 仍是纯周度 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`188.62% CAGR / -40.77% MaxDD / 1.7388 Sharpe / 16.36 Turnover`，但验证口径继续因 2023 窗口失效拒绝进入 Path 2 winner。
- 验证后 Path 2 winner 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，`39.51% CAGR / -32.76% MaxDD / 1.1512 Sharpe / 3.79 Turnover`；2020 `1/99 risk40_mom_exit60_reconfirm70`，`60.26% / -28.34% / 1.2665 / 4.49`。
- 2023 仍为 `1/99 risk50_ma`，`69.00% CAGR / -36.51% MaxDD / 1.3748 Sharpe / 4.79 Turnover`；2025 验证 winner 仍为 `aggr_05_95_prom3_core_6_1_full_risk_cap60`，`151.34% / -17.33% / 2.1910 / 5.94`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=65.89% / minCAGR=39.51% / worstMaxDD=-32.76% / meanTurn=4.98`；下一轮仍优先寻找更适配 2020 的中周期高收益原型，而不是继续追逐短窗周频爆发。

## 本轮执行计划（2026-05-13 03:32 CST）

- 本轮复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，候选宇宙维持 `478`，五个 family 规模仍为 `159 / 237 / 16 / 16 / 16`；`results/strategy_comparison_base_method.csv` 仍保持约 `3407` 条数据行，未再被压缩。
- Path 2 raw 扫描的 `since_2025_01` 单窗口 leader 仍是纯周度 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`188.62% CAGR / -40.77% MaxDD / 1.7388 Sharpe / 16.36 Turnover`，但验证口径继续拒绝它进入 Path 2 winner。
- 验证后 Path 2 winner 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，`39.51% CAGR / -32.76% MaxDD / 1.1512 Sharpe / 3.79 Turnover`；2020 `1/99 risk40_mom_exit60_reconfirm70`，`60.26% / -28.34% / 1.2665 / 4.49`。
- 2023 仍为 `1/99 risk50_ma`，`69.00% CAGR / -36.51% MaxDD / 1.3748 Sharpe / 4.79 Turnover`；2025 验证 winner 仍为 `aggr_05_95_prom3_core_6_1_full_risk_cap60`，`151.34% / -17.33% / 2.1910 / 5.94`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=65.89% / minCAGR=39.51% / worstMaxDD=-32.76% / meanTurn=4.98`；下一步仍应优先寻找更适配 2020 的中周期高收益原型，而非继续提高短窗爆发。

## 本轮执行计划（2026-05-12 21:20 CST）

- 本轮先发现当前 `results/strategy_comparison_base_method.csv` 被缩成 `256` 行，会把 Path 2 候选宇宙压到 `30` 个且双周 family 为 `0`；已用本地 `summary.json` 运行 `.venv/bin/python scripts/rebuild_strategy_comparison_csv.py --windows since_2017_01 since_2020_01 since_2023_01 since_2025_01`，恢复到 `3407` 行 / `871` 个 base strategies。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `478`，五个 family 规模为 `159 / 237 / 16 / 16 / 16`；新增或同步的 `risk40_mom_exit60_reconfirm*_caution80` 只扩充 `high_growth_theme`，没有压扁高集中、等权动量、双周或周频 family membership。
- `risk40_mom_exit60_reconfirm75_caution80` 与 `risk40_mom_exit60_reconfirm70_caution80` 没有改写 Path 2 winner：最好 2020 为 `90/10` 等权 `1/99 reconfirm70_caution80`，`58.79% CAGR / -28.34% MaxDD / 1.2651 Sharpe / 4.43 Turnover`，低于当前 `risk40 reconfirm70` 的 `60.26% CAGR`。
- caution80 最好长窗为 `90/10` 等权 `2/98 reconfirm75_caution80`，`38.66% CAGR / -32.85% MaxDD / 1.1502 Sharpe / 3.74 Turnover`，低于当前 `2/98 risk40 reconfirm75` 的 `39.51% / -32.76% / 1.1512 / 3.79`。
- Path 2 验证 winner 仍为：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 验证后 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=65.89% / minCAGR=39.51%`。

## 本轮执行计划（2026-05-12 09:12 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线为 `462` candidates；随后新增 4 个介于旧 `risk30` 与强势 `risk50` 之间的高成长主线原型：`risk40_mom_exit60_reconfirm75` 与 `risk40_mom_exit60_reconfirm70`，覆盖 `1/99`、`2/98`，继续只扩充 `high_growth_theme` family。
- 微批量只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-11`；随后重建 comparison 到 `3375` 行 / `863` 个 base strategies。
- 复跑 Path 2 后候选宇宙增至 `470`，五个 family 规模为 `159 / 229 / 16 / 16 / 16`；新增候选没有压扁高集中、等权动量、双周或周频 family membership。
- 新 `risk40_mom_exit60_reconfirm70` 改写 Path 2 `since_2020_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95` 达到 `59.29% CAGR / -28.34% MaxDD / 1.2534 Sharpe / 4.49 Turnover`，相对旧 `risk50 reconfirm70` 同时改善收益、回撤、Sharpe 与换手。
- 新 `risk40_mom_exit60_reconfirm75` 改写 Path 2 `since_2017_01` winner 与四窗口 robust candidate：`2/98` 等权版本为 `38.93% CAGR / -32.76% MaxDD / 1.1402 Sharpe / 3.79 Turnover`；robust 为 `meanCAGR=63.44% / minCAGR=38.93% / worstMaxDD=-32.76% / meanTurn=4.98`。
- `since_2023_01 / since_2025_01` 验证后 winner 不变：2023 仍为 `risk50_ma`，2025 仍为验证后的 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；下一轮优先围绕 `risk40` 的退出阈值或谨慎仓，而不是继续单纯放宽恢复确认。

## 本轮执行计划（2026-05-12 03:16 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线为 `454` candidates，随后新增 4 个更适配 `since_2020_01` 的恢复确认放松原型：`risk50_mom_exit60_reconfirm70` 与 `risk50_mom_exit60_reconfirm65`，覆盖 `1/99`、`2/98`，继续只扩充 `high_growth_theme` family。
- 微批量只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-11`；随后重建 comparison 到 `3343` 行 / `855` 个 base strategies。
- 复跑 Path 2 后候选宇宙增至 `462`，五个 family 规模为 `159 / 221 / 16 / 16 / 16`；新增候选只扩充 `high_growth_theme`，没有压扁高集中、等权动量、双周或周频 family membership。
- 新 `reconfirm70` 改写 Path 2 `since_2020_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap95` 达到 `58.76% CAGR / -33.08% MaxDD / 1.2319 Sharpe / 4.71 Turnover`，相对旧 `risk50_mom` 同时改善收益、回撤与 Sharpe，换手小幅升高。
- 新 `reconfirm65` 更偏长窗，但未改写长窗 winner：最好长窗为 `90/10` 等权 `2/98 reconfirm65`，`37.51% CAGR / -39.15% MaxDD / 0.9958 Sharpe / 4.12 Turnover`，仍低于当前 `2/98 reconfirm75` 的 `38.67% / -38.80% / 1.1164 / 3.96`。
- `since_2017_01 / since_2023_01 / since_2025_01` 验证后 winner 不变；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60_reconfirm75`，`meanCAGR=63.93% / minCAGR=38.67% / worstMaxDD=-38.80% / meanTurn=5.13`。

## 本轮执行计划（2026-05-11 21:22 CST）

- 本轮复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，并新增 4 个独立高成长主线原型：`risk50_mom_exit60_reconfirm75_caution80` 与 `risk50_mom_exit60_reconfirm75_caution75`，覆盖 `1/99`、`2/98`，继续只扩充 `high_growth_theme` family。
- 微批量只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-11`；随后重建 comparison 到 `3311` 行 / `847` 个 base strategies。
- 复跑 Path 2 后候选宇宙增至 `454`，五个 family 规模为 `159 / 213 / 16 / 16 / 16`；family membership 未被新高集中候选压扁。
- 新 `reconfirm75_caution` 组合没有改写 Path 2 winner：最好 2020 候选为 `90/10` 等权 `1/99 caution80`，`51.03% CAGR / -36.89% MaxDD / 1.1948 Sharpe / 4.55 Turnover`，低于当前 `risk50_mom` 的 `55.60% / -36.55% / 1.2050 / 4.65`。
- 长窗最好为 `90/10` 等权 `2/98 caution80`，`38.11% CAGR / -38.88% MaxDD / 1.1194 Sharpe / 3.91 Turnover`，接近但仍低于当前 `reconfirm75` 长窗 winner 的 `38.67% / -38.80% / 1.1164 / 3.96`。
- 短窗 side observation：总市值 `2/98 caution80` 在 `since_2025_01` 达到约 `124.95% / -16.13% / 2.0428 / 6.73`，但低于验证后的 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60_reconfirm75`，`meanCAGR=63.93% / minCAGR=38.67% / worstMaxDD=-38.80% / meanTurn=5.13`。

## 本轮执行计划（2026-05-11 15:15 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线为 `438` candidates，随后新增 4 个独立风险时点原型：`risk50_mom_exit60_caution80` 与 `risk50_mom_exit60_caution75`，覆盖 `1/99`、`2/98`。
- 微批量只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`；随后用本地 summary 缓存重建 comparison 到 `3267` 行 / `833` 个 base strategies。
- 复跑 Path 2 后候选宇宙增至 `446`，五个 family 规模为 `159 / 205 / 16 / 16 / 16`；新增候选只扩充 `high_growth_theme`，没有压扁其他 family membership。
- 新 `exit60_caution` 组合没有改写 Path 2 winner：最好 2020 候选为 `90/10` 等权 `1/99 risk50_mom_exit60_caution80`，`54.03% CAGR / -36.43% MaxDD / 1.1991 Sharpe / 4.69 Turnover`，低于当前 `risk50_mom` 的 `55.60% / -36.55% / 1.2050 / 4.65`。
- 长窗最好为 `90/10` 等权 `2/98 risk50_mom_exit60_caution80`，`36.52% CAGR / -40.22% MaxDD / 0.9945 Sharpe / 4.02 Turnover`，低于当前 `reconfirm75` 长窗 winner 的 `38.67% / -38.80% / 1.1164 / 3.96`。
- 短窗 side observation：总市值 `2/98 caution80` 在 `since_2025_01` 达到 `114.94% / -16.13% / 1.9286 / 6.75`，但低于验证后的 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60_reconfirm75`，`meanCAGR=63.93% / minCAGR=38.67% / worstMaxDD=-38.80% / meanTurn=5.13`。

## 本轮执行计划（2026-05-11 09:19 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线为 `430` candidates，五个 family 规模为 `159 / 189 / 16 / 16 / 16`，窗口强点仍集中在 `risk50_mom_exit60 / risk50_mom / risk50_ma`。
- 新增 4 个独立恢复确认原型：`risk50_mom_exit60_reconfirm75_cap95` 与 `risk50_mom_exit60_reconfirm80_amt110_cap95`，覆盖 `1/99`、`2/98`；只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3235` 行 / `825` 个 base strategies；复跑 Path 2 后候选宇宙增至 `438`，五个 family 规模为 `159 / 197 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新 `reconfirm75` 改写 Path 2 `since_2017_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_cap95` 达到 `38.67% CAGR / -38.80% MaxDD / 1.1164 Sharpe / 3.96 Turnover`。
- 四窗口 robust candidate 同步切到同一 `2/98 reconfirm75`，`meanCAGR=63.93% / minCAGR=38.67% / worstMaxDD=-38.80% / meanTurn=5.13`；相对旧 `exit60`，长窗收益、Sharpe、回撤与换手均小幅改善。
- `since_2020_01 / since_2023_01 / since_2025_01` 验证后 winner 不变：新候选最佳 2020 为 `1/99 reconfirm75` 的 `51.59% / -36.99% / 1.1971 / 4.61`，低于当前 `risk50_mom` 的 `55.60%`；`reconfirm80_amt110` 过严，最好 2020 等权仅约 `31.30% CAGR`，下一轮不应继续单纯加严确认阈值。

## 本轮执行计划（2026-05-11 03:13 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍为 `422` candidates，五个 family 规模为 `159 / 181 / 16 / 16 / 16`，窗口 winner 继续由 `risk50_mom_exit60 / risk50_mom / risk50_ma` 占据。
- 新增 4 个独立量价晋升阈值原型：`risk50_mom_top12` 与 `risk50_mom_top18`，覆盖 `1/99`、`2/98`；只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3203` 行 / `817` 个 base strategies；复跑 Path 2 后候选宇宙增至 `430`，五个 family 规模为 `159 / 189 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新阈值没有改写 Path 2 winner：最好 2020 候选为 `90/10` 等权 `1/99 risk50_mom_top12`，`46.19% CAGR / -36.26% MaxDD / 0.9698 Sharpe / 4.88 Turnover`，收益与 Sharpe 均低于当前 `risk50_mom`。
- 主要 side observation 是 `top18` 偏向短窗：`90/10` 等权 `1/99 risk50_mom_top18` 在 `since_2023_01` 为 `63.08% CAGR / -33.34% MaxDD / 1.3521 Sharpe / 4.41 Turnover`，`since_2025_01` 为 `100.23% / -14.30% / 1.8119 / 7.39`，但 2020 窗口降到 `37.47% CAGR`，不足以替换。
- Path 2 tracked winners 仍为：`since_2017_01` 的 `90/10` 等权 `2/98 risk50_mom_exit60`、`since_2020_01` 的 `90/10` 等权 `1/99 risk50_mom`、`since_2023_01` 的 `90/10` 等权 `1/99 risk50_ma`、验证后的 `since_2025_01` `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60`，`meanCAGR=63.07% / minCAGR=37.18% / worstMaxDD=-40.14% / meanTurn=5.17`。

## 本轮执行计划（2026-05-10 21:14 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍为 `414` candidates，五个 family 规模为 `159 / 173 / 16 / 16 / 16`，窗口 winner 继续由 `risk50_mom_exit60 / risk50_mom / risk50_ma` 占据。
- 新增 4 个独立风险节奏原型：`risk50_mom_caution70` 与 `risk50_mom_caution60`，覆盖 `1/99`、`2/98`；只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3171` 行 / `809` 个 base strategies；复跑 Path 2 后候选宇宙增至 `422`，五个 family 规模为 `159 / 181 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新谨慎仓没有改写 Path 2 winner：最好 2020 候选为 `90/10` 等权 `1/99 risk50_mom_caution70`，`52.79% CAGR / -36.76% MaxDD / 1.2114 Sharpe / 4.53 Turnover`，Sharpe 略好但收益低于当前 `risk50_mom` 且回撤略差。
- 主要 side observation 是 2023 窗口：`90/10` 等权 `1/99 risk50_mom_caution70` 为 `61.64% CAGR / -33.36% MaxDD / 1.3678 Sharpe / 4.36 Turnover`，比当前 `risk50_ma` 更稳但收益不足以替换；`caution60` 进一步降收益，只改善局部 Sharpe。
- Path 2 tracked winners 仍为：`since_2017_01` 的 `90/10` 等权 `2/98 risk50_mom_exit60`、`since_2020_01` 的 `90/10` 等权 `1/99 risk50_mom`、`since_2023_01` 的 `90/10` 等权 `1/99 risk50_ma`、验证后的 `since_2025_01` `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60`，`meanCAGR=63.07% / minCAGR=37.18% / worstMaxDD=-40.14% / meanTurn=5.17`。

## 本轮执行计划（2026-05-10 15:04 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍由 `risk50_mom_exit60 / risk50_mom / risk50_ma` 占据；随后新增 4 个独立过滤原型，而不是继续单纯收紧晋升保留 exit 阈值。
- 新增原型为 `risk50_mom_confirm75` 与 `risk50_mom_confirm80_amt110`，覆盖 `1/99`、`2/98`，只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3139` 行 / `801` 个 base strategies；复跑 Path 2 后候选宇宙增至 `414`，五个 family 规模为 `159 / 173 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新过滤没有改写 Path 2 winner：`confirm75` 最好的 2020 候选为 `90/10` 等权 `1/99`，`52.16% CAGR / -37.21% MaxDD / 1.2070 Sharpe / 4.52 Turnover`，收益低于现 `risk50_mom` 且回撤略差。
- `confirm80_amt110` 能把长窗回撤压到约 `-35.60%`，最好的长窗候选为 `90/10` 等权 `2/98`，`33.73% CAGR / -35.60% MaxDD / 1.0221 Sharpe / 3.76 Turnover`，但 2020 窗口降到约 `39.18% CAGR`，不足以替换。
- Path 2 tracked winners 仍为：`since_2017_01` 的 `90/10` 等权 `2/98 risk50_mom_exit60`、`since_2020_01` 的 `90/10` 等权 `1/99 risk50_mom`、`since_2023_01` 的 `90/10` 等权 `1/99 risk50_ma`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60`，`meanCAGR=63.07% / minCAGR=37.18% / worstMaxDD=-40.14% / meanTurn=5.17`。
- `update_weighted_winners.py` 的验证口径同步修正 Path 2 `since_2025_01` tracked winner 为 `aggr_05_95_prom3_core_6_1_full_risk_cap60`，`147.28% CAGR / -17.33% MaxDD / 2.1530 Sharpe / 5.94 Turnover`；短窗纯周度爆发候选仍保留在候选宇宙，但不再作为验证后的 Path 2 窗口 winner。

## 本轮执行计划（2026-05-10 09:17 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍为 `398` candidates，五个 family 规模为 `159 / 157 / 16 / 16 / 16`；随后围绕当前强点 `90/10 risk50_mom` 增加 `exit80 / exit60` 晋升保留阈值微批量。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95`；只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3107` 行 / `793` 个 base strategies；复跑 Path 2 后候选宇宙扩为 `406`，五个 family 规模为 `159 / 165 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新 `exit60` 改写 Path 2 `since_2017_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95` 达到 `37.18% CAGR / -40.14% MaxDD / 0.9855 Sharpe / 4.06 Turnover`；相对旧 `risk50_mom` 长窗提高收益与 Sharpe，但回撤和换手略变差。
- `since_2020_01` winner 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；新增 `exit60` 在 2020 窗口约 `54.99% CAGR / -36.33% MaxDD / 1.1953 Sharpe / 4.74 Turnover`，回撤小幅改善但收益和 Sharpe 不足以替换。
- `since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`；`since_2025_01` 仍为纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`。
- 四窗口 robust candidate 切到 `90/10` 等权 `2/98 risk50_mom_exit60`，`meanCAGR=63.07% / minCAGR=37.18% / worstMaxDD=-40.14% / meanTurn=5.17`；下一轮不要只继续收紧晋升保留阈值，应优先寻找能保住 2020 收益同时降低长窗回撤的独立过滤或风险时点。

## 本轮执行计划（2026-05-10 03:16 CST）

- 本轮先独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，发现全局 `sample_end=2026-05-08` 过滤会把真实双周信号点仍在 `2026-04-30` 的候选误删；已修正 `scripts/path2_candidate_pass.py`，改为保留每个策略/窗口自身最新记录，避免混淆数据截止日与调仓/信号生效日。
- 针对高频 family 额外补跑 6 个双周与 4 个周频代表候选，并用 `.venv/bin/python scripts/rebuild_strategy_comparison_csv.py --windows since_2017_01 since_2020_01 since_2023_01 since_2025_01` 重建 comparison；复跑 Path 2 后候选宇宙恢复为 `398`。
- 五个 family 规模恢复为 `159 / 157 / 16 / 16 / 16`，`biweekly_rebalance_aggressive` 与 `weekly_rebalance_aggressive` 不再被当前最新周频 `sample_end` 压扁。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `2/98 risk50_mom`，`meanCAGR=63.47% / minCAGR=35.88% / worstMaxDD=-39.17% / meanTurn=5.09`。

## 本轮执行计划（2026-05-09 21:14 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙保持 `398`，五个 family 规模继续为 `159 / 157 / 16 / 16 / 16`，family membership 未被高集中候选压扁。
- 本轮不继续简单抬高风险保留仓位，也不继续 `risk50_or` 的 cap/ramp/exit 邻域；当前研究基线仍聚焦 `90/10` 等权 `risk50_mom / risk50_ma` 三档择时线的回撤压缩。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-09 18:09 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙保持 `398`，五个 family 规模继续为 `159 / 157 / 16 / 16 / 16`，family membership 未被高集中候选压扁。
- 本轮不继续简单抬高风险保留仓位，也不继续 `risk50_or` 的 cap/ramp 邻域；当前研究基线仍聚焦 `90/10` 等权 `risk50_mom / risk50_ma` 三档择时线的回撤压缩。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-09 13:04 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙保持 `398`，五个 family 规模为 `159 / 157 / 16 / 16 / 16`，family membership 仍未被高集中候选压扁。
- 本轮不继续简单抬高风险保留仓位，也不继续 `risk50_or` 的 cap/ramp 邻域；当前研究基线继续聚焦 `90/10` 等权 `risk50_mom / risk50_ma` 三档择时线的回撤压缩。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-09 05:08 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙从上轮记录的 `374` 同步为 `398`，五个 family 规模为 `159 / 157 / 16 / 16 / 16`，新增可识别候选主要扩充 `high_growth_theme`，family membership 仍未被高集中候选压扁。
- 本轮不继续简单抬高风险保留仓位，也不继续 `risk50_or` 的 cap/ramp 邻域；当前研究基线继续聚焦 `90/10` 等权 `risk50_mom / risk50_ma` 三档择时线的回撤压缩。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-08 23:12 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙保持 `374`，五个 family 规模为 `159 / 149 / 16 / 16 / 16`，family membership 未被高集中候选压扁。
- 本轮不继续简单抬高三档风险保留仓位，也不新增 `risk50_or` 的 cap/ramp 邻域；先把 17:24 已修正的 `risk50_mom / risk50_ma` 三档择时口径作为当前基线复核。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`（`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`）。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`（`55.60% / -36.55% / 1.2050 / 4.65`），`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`（`67.06% / -36.51% / 1.3498 / 4.79`）。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出（`181.26% / -40.77% / 1.6970 / 16.50`）；四窗口 robust candidate 仍是 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-08 17:24 CST）

- 基线复跑后发现 `negative_mom / below_ma` 风控别名与月频 `risk_staging_mode` 未真正进入 `compute_market_exposure()`；本轮修正别名映射，并把月频回测接入三档风险暴露参数，避免 `risk50_mom / risk50_ma` 与旧两档口径混同。
- 本轮先跑 24-base timing batch，再在修正后公平复跑 12-base `risk50_or / risk50_mom / risk50_ma` 对照，覆盖 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座、四个跟踪窗口，并固定 `--end-date 2026-05-07`。
- 重建 comparison 后为 `2979` 行 / `761` 个 base strategies；复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后候选宇宙升至 `374`，五个 family 规模为 `159 / 149 / 16 / 16 / 16`，新增三档择时候选归入 `high_growth_theme`。
- 新三档动量候选改写 `since_2017_01` 与 `since_2020_01` winner：`90/10` 等权 `2/98 risk50_mom` 长窗达到 `35.95% CAGR / -39.17% MaxDD / 0.9471 Sharpe / 3.87 Turnover`；`1/99 risk50_mom` 在 2020 窗口达到 `55.72% CAGR / -36.55% MaxDD / 1.2068 Sharpe / 4.65 Turnover`。
- `since_2023_01` 改写为 `90/10` 等权 `1/99 risk50_ma`，`67.32% CAGR / -36.51% MaxDD / 1.3533 Sharpe / 4.79 Turnover`；`since_2025_01` 仍由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`172.51% CAGR / -40.77% MaxDD / 1.6610 Sharpe / 16.50 Turnover`。
- 四窗口 robust candidate 切到 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.95% / minCAGR=35.90% / worstMaxDD=-39.14% / meanTurn=5.08`；下一轮优先研究这条三档动量线的回撤压缩，而不是继续简单提高风险保留仓位。

## 本轮执行计划（2026-05-08 13:15 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `348`；本轮不继续提高核心占比，也不继续拆 `risk30/risk50` 触发器，而是在当前 `90/10` 等权 `risk50_or` 2020 winner 上测试独立 drawdown-control 分支。
- 新增 4 个显式原型：`risk50_or_cap80`、`risk50_or_cap70`、`risk50_or_ramp85_cap95`、`risk50_or_ramp70_cap95`；只跑 `core_explore_90_10_equal_weight_winner_core` 与 `core_explore_90_10_total_mv_winner_core` 两个底座四窗口，并固定 `--end-date 2026-04-30`。
- 微批量后用本地 summary 缓存重建 comparison 到 `2907` 行 / `743` 个 base strategies；复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后候选宇宙升至 `356`，五个 family 规模为 `159 / 131 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`。
- 新候选没有改写 Path 2 tracked winners 或四窗口 robust candidate。当前 `since_2020_01` winner 仍是 `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95`，`48.41% CAGR / -37.10% MaxDD / 1.1875 Sharpe / 4.38 Turnover`。
- 最好的新 2020 候选是等权 `risk50_or_cap80`：`48.12% CAGR / -37.10% MaxDD / 1.1917 Sharpe / 4.37 Turnover`；等权 `cap70` 为 `47.78% CAGR / -37.10% MaxDD / 1.1955 Sharpe / 4.35 Turnover`，Sharpe 略好但没有降低回撤且收益低于 winner。
- 首月 ramp 控制在当前缓存下与原 `cap95` 结果基本重合，未提供独立降回撤效果；下一轮不要继续在 `risk50_or` 上做简单 cap/ramp 微调，应转向真正不同的风险时点或候选来源过滤。

## 本轮执行计划（2026-05-08 07:28 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `340`；本轮不继续拆 `risk30/risk50` 触发器，新增 `core_explore_90_10` 与 `core_explore_95_05` 两个核心/探索组合底座，围绕当前强点 `promo_liqmom_top15` 跑 `risk50_or` 与 `risk30_or` 的等权/总市值对照。
- 微批量覆盖 8 个 base candidates、四个跟踪窗口，并固定 `--end-date 2026-04-30`；随后用本地 summary 缓存按四窗口重建 comparison 到 `2875` 行 / `735` 个 base strategies。
- 重建后复跑 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `348`，五个 family 规模为 `159 / 123 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`，family membership 未被高集中候选压扁。
- 新 `90/10` 等权 `risk50_or` 改写 Path 2 `since_2020_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95` 达到 `48.41% CAGR / -37.10% MaxDD / 1.1875 Sharpe / 4.38 Turnover`，高于旧 `80/20` 等权 `risk50_or` 的 `47.48% CAGR`，但回撤与换手仍偏高。
- 结构对照里最均衡的新候选是 `90/10` 等权 `risk30_or`：`46.11% CAGR / -26.63% MaxDD / 1.2174 Sharpe / 3.86 Turnover`，未改写 winner 但继续证明降仓 30% 分支更稳。
- `since_2017_01 / since_2023_01 / since_2025_01` winners 与四窗口 robust candidate 未改写；下一轮不要继续单纯提高核心占比，可考虑在 `90/10 risk50_or` 上找降低回撤的独立约束。

## 本轮执行计划（2026-05-07 23:12 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `332`；本轮不继续 `risk50_or` 退出阈值微调，新增 4 个 `promo_liqmom_top15 risk30` 风控触发拆分原型：`risk30_mom` 与 `risk30_ma`，覆盖 `1/99` 与 `2/98`。
- 微批量只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口，并固定 `--end-date 2026-04-30`；随后用本地 summary 缓存重建 comparison 到 `2843` 行 / `727` 个 base strategies。
- 重建后复跑 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `340`，五个 family 规模为 `159 / 115 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`，family membership 未压扁。
- 新触发拆分没有改写 Path 2 tracked winner 或四窗口 robust candidate。`since_2020_01` winner 仍是等权 `risk50_or 1/99`，`47.48% CAGR / -36.36% MaxDD / 1.2388 Sharpe / 4.29 Turnover`。
- 新候选中最好的是等权 `1/99 risk30_mom/risk30_ma`，`since_2020_01` 为 `44.82% CAGR / -26.53% MaxDD / 1.2612 Sharpe / 3.78 Turnover`，与旧 `risk30_or` 结果完全重合；当前本地缓存下动量负值与跌破均线触发没有提供新的择时差异。
- `since_2023_01` 新候选最高为 `47.10% CAGR / -24.59% MaxDD / 1.3340 Sharpe`，仍低于当前 2023 winner；下一轮不要继续拆分同一 `risk30` 风控触发，应回到独立的 2020 中周期信号或组合结构。

## 本轮执行计划（2026-05-07 11:10 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `324`；本轮新增 4 个当前 `risk50_or` 强点的退出阈值原型：`risk50_or_exit80` 与 `risk50_or_exit60`，覆盖 `1/99` 与 `2/98`。
- 微批量只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口，并固定 `--end-date 2026-04-30`；随后用本地 summary 缓存重建 comparison 到 `2811` 行 / `719` 个 base strategies。
- 重建后复跑 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `332`，五个 family 规模为 `159 / 107 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`，family membership 未压扁。
- 新退出阈值没有改写 Path 2 tracked winner 或四窗口 robust candidate。`since_2020_01` winner 仍是等权 `risk50_or 1/99`，`46.78% CAGR / -36.36% MaxDD / 1.2198 Sharpe / 4.27 Turnover`。
- 最好的新候选是等权 `1/99 risk50_or_exit60`：`since_2020_01` 为 `46.25% CAGR / -36.16% MaxDD / 1.2095 Sharpe / 4.35 Turnover`，只小幅改善回撤但收益、Sharpe、换手均弱于现 winner。
- 新候选的 `since_2023_01` 最好为 `52.99% CAGR / -31.82% MaxDD / 1.3261 Sharpe`，仍低于当前 2023 winner `57.19% CAGR`；`since_2017_01` 最好为 `30.35% CAGR`，未超过当前长窗 winner。
- 下一轮不要继续单纯收紧 `risk50_or` 的退出阈值；应回到独立的 2020 中周期信号或更明确的风险时点，而不是继续在同一风险/退出参数邻域内微调。

## 本轮执行计划（2026-05-07 05:06 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `316`；本轮新增 4 个 `risk30_exit60` 恢复/再晋升确认原型，跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口，并固定 `--end-date 2026-04-30`。
- 重建 comparison 后为 `2779` 行 / `711` 个 base strategies；复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后候选宇宙升至 `324`，五个 family 规模为 `159 / 99 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`，family membership 未压扁。
- 新恢复确认原型没有改写 Path 2 tracked winner 或 robust candidate。`since_2020_01` winner 仍是等权 `risk50_or 1/99`，`46.78% CAGR / -36.36% MaxDD / 1.2198 Sharpe / 4.27 Turnover`。
- 最好的新 `reconfirm75` 等权候选在 `since_2020_01` 只有 `36.79% CAGR / -31.51% MaxDD / 1.0632 Sharpe / 3.66 Turnover`，明显低于旧 `risk30_exit60` 的 `44.30% CAGR`。
- 更严格的 `reconfirm80_amt110` 能把等权 `since_2023_01` 回撤压到约 `-21.22%~-21.37%`，但 `since_2020_01` 只剩约 `29.82%~29.85% CAGR`，不适合作为 2020 主攻线；下一轮不要继续加严同类再晋升确认。

## 本轮执行计划（2026-05-06 23:15 CST）

- 基线复跑前先用缓存 summary 重建 comparison，避免压缩 CSV 导致 Path 2 只识别少量候选；重建后基线为 `308` candidates，五个 family 规模为 `159 / 83 / 16 / 16 / 16`。
- 本轮围绕上轮的 `risk30` 更均衡 side observation 增加晋升核心退出阈值 hook：`promoted_core_sell_exit_percentile`，默认值仍为 `1.0`，旧策略行为不变。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口，并固定 `--end-date 2026-04-30`；随后重建 comparison 到 `2747` 行 / `703` 个 base strategies。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后候选宇宙升至 `316`，五个 family 规模为 `159 / 91 / 16 / 16 / 16`；新增候选全部归入 `high_growth_theme`，family membership 未压扁。
- 新退出阈值没有改写 Path 2 tracked winner 或 robust candidate。最佳新候选为等权 `1/99 risk30_exit60`：`since_2020_01` 为 `44.30% CAGR / -26.37% MaxDD / 1.2498 Sharpe / 3.85 Turnover`，收益低于现有 `risk50_or` winner 的 `46.78%`，但回撤和 Sharpe 更均衡。
- `since_2023_01` 上新候选最高约 `45.81% CAGR / -24.59% MaxDD / 1.3075 Sharpe`，仍低于当前 2023 winner 的 `57.19% CAGR`；下一轮优先比较 `risk30_exit60` 的恢复确认/再晋升条件，而不是继续收紧同一个退出阈值。

## 本轮执行计划（2026-05-06 11:35 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，旧口径为 `299` candidates，五个 family 规模为 `159 / 75 / 16 / 16 / 16`，四窗口 tracked winners 与 robust candidate 未漂移。
- 本轮不继续扩 `top10/top20` 或单纯提高风险保留仓位；围绕当前 `since_2020_01` winner 的 `promo_liqmom_top15` 测试更早触发的 `or` 风险规则，新增 `risk30_or` 与 `risk50_or` 两档，覆盖 `1/99` 与 `2/98` 两个进攻配比。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量，并固定 `--end-date 2026-04-30`；随后用缓存 summary 重建 comparison 到 `2715` 行 / `695` 个 base strategies。
- 重建后复跑 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `308`，五个 family 规模为 `159 / 83 / 16 / 16 / 16`，新增候选归入 `high_growth_theme`，family membership 未压扁。
- 新 `or` 风险触发没有改写 Path 2 tracked winner 或四窗口 robust candidate；`since_2020_01` winner 仍是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95`（`46.78% CAGR / -36.36% MaxDD / 1.2198 Sharpe / 4.27 Turnover`）。
- 新候选的有效 side observation：等权 `risk50_or 1/99` 在 `since_2023_01` 达到 `54.98% CAGR / -31.82% MaxDD / 1.3582 Sharpe / 4.09 Turnover`，但仍低于当前 2023 winner `58.20% CAGR`；等权 `risk30_or 1/99` 在 2020 为 `44.82% CAGR / -26.53% MaxDD / 1.2612 Sharpe / 3.78 Turnover`，继续是更均衡的下一轮风险节奏对照。
- `since_2017_01`、`since_2023_01`、`since_2025_01` 与四窗口 robust candidate 均未改写；下一轮应比较 `risk30` 的退出/恢复确认，而不是继续增加 `risk50` 同义规则。

## 本轮执行计划（2026-05-06 06:14 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，旧口径为 `292` candidates，五个 family 规模为 `159 / 67 / 16 / 16 / 16`，旧 tracked winners 与 robust candidate 未漂移。
- 本轮不继续 `top10/top20` 阈值宽窄邻域，改为围绕当前 `since_2020_01` winner 的 `promo_liqmom_top15` 做风险节奏微批量：新增 `risk30` 与 `risk50` 两档熊市保留仓位，覆盖 `1/99` 与 `2/98` 两个进攻配比。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量，并固定 `--end-date 2026-04-30`；随后用缓存 summary 重建 comparison 到 `2029` 行 / `684` 个 base strategies。
- 重建后运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `299`，五个 family 规模为 `159 / 75 / 16 / 16 / 16`，新增候选仍归入 `high_growth_theme`。
- 新 `risk50` 等权 `1/99` 改写 `since_2020_01` Path 2 winner：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95` 达到 `46.78% CAGR / -36.36% MaxDD / 1.2198 Sharpe / 4.27 Turnover`，相对旧 top15 winner 的 `37.38% / -22.51% / 1.2283 / 3.22` 明显提高收益但显著放大回撤与换手。
- `risk30` 等权 `1/99` 作为更保守 side observation：`44.82% CAGR / -26.53% MaxDD / 1.2612 Sharpe / 3.78 Turnover`，收益低于 `risk50` winner，但回撤和 Sharpe 更平衡，值得下一轮围绕退出/降仓节奏继续比较。
- `since_2017_01`、`since_2023_01`、`since_2025_01` 与四窗口 robust candidate 未改写；robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`。

## 本轮执行计划（2026-05-06 00:04 CST）

- 基线先独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，确认五个 family 的 membership 与旧 tracked winners 是否漂移。
- 本轮优先围绕上轮新改写 `since_2020_01` winner 的 `promo_liqmom_top15` 做窄阈值邻域，不回到 `midcycle_momentum / industry_trend / core_theme` 等已验证偏弱路线。
- 候选继续归入 `high_growth_theme` family，用来测试晋升来源阈值是否能进一步改善 2020，同时避免高集中 family 被同一批候选压扁。
- 若新增候选未明确改写 Path 2 四窗口 winner 或四窗口 robust candidate，只记录扫描结果，不强行同步为 winner。
- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `284`，五个 family 规模为 `159 / 59 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 未漂移。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；首次默认跑到本地当前日后，立即用 `--end-date 2026-04-30` 覆盖同一批结果，保持与现有 comparison 口径一致。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2651` 行 / `679` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `292`，五个 family 规模为 `159 / 67 / 16 / 16 / 16`。
- 新 top10/top20 邻域没有改写 Path 2 tracked winner 或 robust candidate；`since_2020_01` winner 仍是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95`（`37.38% CAGR / -22.51% MaxDD / 1.2283 Sharpe / 3.22 Turnover`）。
- 新邻域中 `top20` 在 `since_2025_01` 有较强 side observation（总市值 `2/98` 为 `149.97% CAGR / -12.37% MaxDD / 2.2204 Sharpe`），但仍低于当前 `confirm80` 短窗 winner；下一轮不要继续只做 topN 宽窄阈值，应转向组合持有/退出或风险节奏。

## 本轮补充计划与记录（2026-05-05 18:16 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `276`，五个 family 规模为 `159 / 51 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不继续 `confirm / ramp / cadence / core_theme / industry_trend / midcycle_momentum` 简单邻域，新增 `promotion_signal_mode` hook：默认逻辑保持不变，仅新候选可把晋升排序切到 `momentum_6_1` 或 `liquidity_momentum`，并用 `standard_promotion_percentile` 限制标准晋升池。
- 新增 4 个显式原型：`aggr_01_99_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100`、`aggr_02_98_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；新候选归入 `high_growth_theme` family，用来测试晋升来源是否能改善 2020，而不压扁高集中 family 口径。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2619` 行 / `671` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `284`，五个 family 规模为 `159 / 59 / 16 / 16 / 16`。
- 新 `liquidity_momentum` 晋升池改写 `since_2020_01` Path 2 tracked winner：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95` 达到 `37.38% CAGR / -22.51% MaxDD / 1.2283 Sharpe / 3.22 Turnover`，相对旧 `34.12% / -22.77% / 1.0402 / 3.43` 同时改善收益、回撤、Sharpe 与换手。
- `since_2023_01`、`since_2025_01` 与四窗口 robust candidate 未改写；robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`。下一轮优先围绕 `promo_liqmom_top15` 做 2020 稳健化/阈值邻域，而不是回到已失效的主题或纯 cadence 线。

## 本轮补充计划与记录（2026-05-05 12:14 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙仍为 `268`，五个 family 规模为 `159 / 43 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不继续 `confirm / ramp / cadence / core_theme / industry_trend / core_3_1` 的简单邻域，新增一个独立中周期量价排序口径 `midcycle_momentum`：以 `6-1` 动量为主，叠加量能放大、近月收益、行业领涨和突破。
- 新增 4 个显式原型：`aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100`、`aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100`、`aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95`、`aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；新候选归入 `high_growth_theme` family，避免继续把高集中 family 口径压扁。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2587` 行 / `663` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `276`，五个 family 规模为 `159 / 51 / 16 / 16 / 16`。
- 新 `midcycle_momentum` 没有改写任何 Path 2 tracked winner 或 robust candidate。新增候选里 `since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95`，仅 `11.77% CAGR / -22.15% MaxDD / 0.5693 Sharpe / 3.53 Turnover`，明显低于当前 `34.12%` winner。
- 新候选的 `since_2023_01` 最好为等权 `2/98 prom1` 的 `27.92% CAGR`，`since_2025_01` 最好为等权 `2/98 prom2` 的 `78.20% CAGR`，均低于当前对应窗口 winners；下一轮不要继续沿 `midcycle_momentum` 加码。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`。

## 本轮补充计划与记录（2026-05-05 06:14 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `260`，五个 family 规模为 `151 / 43 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不继续首月 ramp、简单 cadence、`core_theme / industry_trend` 或 `core_3_1` 邻域，新增一个真实的 2020 promotion 确认过滤 hook：在晋升候选中可配置 `6-1` 动量分位、`3-1` 动量分位与量能放大阈值，默认值保持旧行为不变。
- 新增 4 个显式原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm80`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80`、`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；新候选仍归入 `high_concentration_breakout`，不并入主题或高频 family。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2555` 行 / `655` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `268`，五个 family 规模为 `159 / 43 / 16 / 16 / 16`。
- 新确认过滤没有改善 `since_2020_01`：新增等权候选最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80`，为 `31.36% CAGR / -26.21% MaxDD / 0.9493 Sharpe / 3.43 Turnover`，低于当前 `34.12%` winner。
- 新确认过滤改写了 `since_2025_01` Path 2 tracked winner：`core_explore_80_20_total_mv_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80` 达到 `157.73% CAGR / -26.81% MaxDD / 1.7514 Sharpe / 6.63 Turnover`，相对旧 weekly winner 的 `156.73% CAGR / -40.77% MaxDD / 1.5775 Sharpe / 16.06 Turnover` 同时改善收益、回撤、Sharpe 与换手。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`。下一轮不要继续把确认过滤当作 2020 主攻线，应另找独立的中周期信号；`confirm80` 可作为 2025 风险效率 sidecar 保留。

## 本轮补充计划与记录（2026-05-05 00:03 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `252`，五个 family 规模为 `143 / 43 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不再继续扩 `core_theme / industry_trend / core_3_1 / 高频 cadence` 的简单邻域，改测 `prom1 core_6_1 cap100` 的晋升首月 ramp，验证是否能减少 2020 中周期错误重仓和换手伤害。
- 新增 4 个显式原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp70`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70`、`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp85`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp85`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；新候选仍归入 `high_concentration_breakout`，不并入 `high_growth_theme` 或高频 family。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2523` 行 / `647` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `260`，五个 family 规模为 `151 / 43 / 16 / 16 / 16`。
- 新 ramp 原型没有改写任何 Path 2 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70/ramp85`，为 `34.12% CAGR / -22.77% MaxDD / 1.0402 Sharpe / 3.43 Turnover`，与当前 winner 基本等价而非突破。
- `since_2025_01` 新原型最好的是总市值底座 `aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70/ramp85`，仅 `112.20% CAGR / -22.88% MaxDD / 1.4665 Sharpe / 5.47 Turnover`，低于当前 weekly 短窗 winner 的 `156.73% CAGR`。下一轮不应继续只改首月 ramp，应改成真实的 2020 过滤/确认逻辑或寻找独立信号。

## 本轮补充计划与记录（2026-05-04 18:07 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `244`，五个 family 规模为 `143 / 43 / 16 / 12 / 12`，旧 tracked winners 与 robust candidate 均未漂移。
- 本轮停止继续扩 `core_theme / industry_trend` 排序口径，回到当前 `since_2020_01` 强点 `prom1 core_6_1 cap100`，只验证 cadence 是否能改善中周期收益或风险。
- 新增 4 个显式原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_biweekly`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_biweekly`、`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_weekly`。
- 只跑 `80/20 equal_weight` 与 `70/30 equal_weight` 两个底座的四窗口微批量；新增候选归入 `biweekly_rebalance_aggressive / weekly_rebalance_aggressive`，不并入 `high_growth_theme`。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2491` 行 / `639` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `252`，五个 family 规模为 `143 / 43 / 16 / 16 / 16`。
- 新高频 cadence 没有改善 `since_2020_01`：新增候选最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_weekly`，仅 `16.88% CAGR / -48.98% MaxDD / 0.5343 Sharpe / 8.77 Turnover`，明显低于当前 `34.12%` winner。
- `since_2025_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`：`156.73% CAGR / -40.77% MaxDD / 1.5775 Sharpe / 16.06 Turnover`，收益上限高于旧 `147.54%` winner，但回撤和换手显著恶化，只作为短窗高风险窗口赢家记录。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`；下一轮不应继续简单提高 `prom1 cap100` cadence，应转向 2020 专属过滤或降低错误换手的确认逻辑。

## 本轮补充计划与记录（2026-05-04 15:25 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `236`，五个 family 规模为 `143 / 35 / 16 / 12 / 12`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不继续加码上一轮偏弱的 `core_theme` 财务主题口径，改测更偏 2020 中周期趋势的 `industry_trend` 核心信号：行业强度、行业内领涨、`6-1 / 3-1` 动量和突破宽度组合，不再把财务增长作为主权重。
- 新增 4 个显式原型：`aggr_01_99_prom1_industry_trend_cash_off_and_cap100`、`aggr_02_98_prom1_industry_trend_cash_off_and_cap100`、`aggr_01_99_prom2_industry_trend_cash_off_and_cap95`、`aggr_02_98_prom2_industry_trend_cash_off_and_cap95`；只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2459` 行 / `631` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `244`，五个 family 规模为 `143 / 43 / 16 / 12 / 12`，新增候选只扩充 `high_growth_theme`。
- `industry_trend` 没有改写任何 Path 2 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_industry_trend_cash_off_and_cap100`，仅 `14.60% CAGR / -25.49% MaxDD / 0.6491 Sharpe / 3.45 Turnover`，明显低于当前 `34.12%` winner。
- 主要 side observation 是 `since_2025_01` 的 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom1_industry_trend_cash_off_and_cap100` 达到 `116.82% CAGR`，但仍低于当前短窗 winner 的 `147.54% CAGR`。下一轮不应继续单独加码行业趋势/主题排序，应回到当前 `core_6_1 prom1 cap100` 强点附近寻找更有针对性的 2020 过滤或节奏控制。

## 本轮补充计划（2026-05-04 06:45 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，当前候选宇宙仍为 `228`，五个 family 规模为 `143 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均未漂移。
- 本轮不继续沿上一轮偏弱的 `prom1 core_3_1` 加码，改测一个更独立的 2020 中周期排序口径：新增 `core_theme` promoted-core 信号，把增长加速、行业强度、行业龙头与 `6-1 / 3-1` 动量合成为核心排序。
- 显式原型只补 4 个：`aggr_01_99_prom1_core_theme_cash_off_and_cap100`、`aggr_02_98_prom1_core_theme_cash_off_and_cap100`、`aggr_01_99_prom2_core_theme_cash_off_and_cap95`、`aggr_02_98_prom2_core_theme_cash_off_and_cap95`；只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 新候选归入 `high_growth_theme` family，不并入 `high_concentration_breakout`，用来压紧 family membership 口径并避免高集中候选继续挤压其他 family。

### 本轮补充记录（2026-05-04 09:40 CST）

- 完成 8 个 `core_theme` base candidates 的四窗口微批量后，用缓存 summary 重建 comparison CSV 到 `2427` 行 / `623` 个 base strategies。
- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `236`，五个 family 规模为 `143 / 35 / 16 / 12 / 12`，新增候选只扩充 `high_growth_theme`。
- `core_theme` 没有改写任何 Path 2 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_theme_cash_off_and_cap95`，为 `22.98% CAGR / -22.33% MaxDD / 0.9094 Sharpe / 2.58 Turnover`，明显低于当前 `34.12%` winner。
- 新候选的主要 side observation 是 `since_2025_01` 的 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom1_core_theme_cash_off_and_cap100` 达到 `101.89% CAGR`，但仍低于当前短窗 winner 的 `147.54% CAGR`；下一轮不应继续单纯加码 `core_theme`，除非引入更强的 2020 专属过滤或风险节奏。

## 本轮执行计划（2026-05-04）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 避开上一轮已经验证偏弱的 `prom1 cap100` 底座迁移，本轮只测试更独立的 2020 中周期信号：把 `prom1 cap100` 的 promoted-core 信号从 `core_6_1` 改成 `core_3_1`，并只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。

### 本轮快筛记录（2026-05-04 03:57 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `220`，五个 family 规模为 `135 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均保持不变。
- 新增 4 个 `prom1 core_3_1 cap100` 原型：`aggr_01_99_prom1_core_3_1_cash_off_and_cap100`、`aggr_02_98_prom1_core_3_1_cash_off_and_cap100`、`aggr_01_99_prom1_core_3_1_full_risk_cap100`、`aggr_02_98_prom1_core_3_1_full_risk_cap100`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2395` 行 / `615` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `228`，五个 family 规模为 `143 / 27 / 16 / 12 / 12`。
- 新 `core_3_1` 原型未改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_3_1_cash_off_and_cap100`，仅 `11.90% CAGR / -29.60% MaxDD / 0.5153 Sharpe / 3.30 Turnover`，明显弱于当前 `34.12%` winner。
- `core_3_1 full_risk cap100` 在 `since_2025_01` 可做到约 `114.14% CAGR`，但仍低于当前短窗 winner 的 `147.54% CAGR`，且长窗回撤接近 `-72%~-74%`；下一轮不应继续沿 `prom1 core_3_1` 加码，应转向更独立的高成长/行业主线或重新寻找 2020 专属排序口径。

## 本轮执行计划（2026-05-03）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 避开上一轮效果较弱的 `core_3_1 full_risk` 与简单风险暴露放松，本轮只补 4 个更窄的单票高集中中周期原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100`、`aggr_03_97_prom1_core_6_1_cash_off_and_cap100`、`aggr_04_96_prom1_core_6_1_cash_off_and_cap100`；仍只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。

### 本轮快筛记录（2026-05-03 00:16 CST；06:11 CST 复核）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `196`，五个 family 规模为 `111 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均保持不变。
- 新增 4 个单票高集中中周期原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100`、`aggr_03_97_prom1_core_6_1_cash_off_and_cap100`、`aggr_04_96_prom1_core_6_1_cash_off_and_cap100`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2299` 行 / `591` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `204`，五个 family 规模为 `119 / 27 / 16 / 12 / 12`。
- `since_2020_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100`：`34.12% CAGR / -22.77% MaxDD / 1.0402 Sharpe / 3.43 Turnover`，相对旧 `prom2 cash_off_and cap90` 的 `32.25% CAGR` 明确抬升收益上限，但 Sharpe 降低且换手增加。
- 新单票原型未改写 `since_2017_01`、`since_2023_01`、`since_2025_01` 或四窗口 robust candidate；`since_2023_01` 最好仅约 `7.98% CAGR`，说明它是明确的 2020 中周期收益原型，不适合作为 2023 主攻线。

### 本轮补充（2026-05-03 12:05 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙保持 `204`，五个 family 规模为 `119 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均保持不变。
- 沿刚改写 `since_2020_01` 的 `prom1 cap100` 强点补 4 个风险暴露对照：`aggr_01_99_prom1_core_6_1_cash_off_and_risk50_cap100`、`aggr_02_98_prom1_core_6_1_cash_off_and_risk50_cap100`、`aggr_01_99_prom1_core_6_1_full_risk_cap100`、`aggr_02_98_prom1_core_6_1_full_risk_cap100`；仍只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2331` 行 / `599` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `212`，五个 family 规模为 `127 / 27 / 16 / 12 / 12`。
- 新风险暴露原型未改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_risk50_cap100`，仅 `31.43% CAGR / -44.54% MaxDD / 0.8470 Sharpe / 5.57 Turnover`，低于当前 `34.12%` winner 且回撤明显恶化。
- `full_risk cap100` 在 `since_2023_01` 可做到约 `43.33% CAGR`，但仍低于当前 `58.20%` winner，且 `MaxDD` 接近 `-45%`；下一轮不应继续单纯放松 `prom1 cap100` 风险暴露，应转向更独立的 2020 信号或底座结构。

### 本轮补充（2026-05-03 18:07 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙仍为 `212`，五个 family 规模为 `127 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均保持不变。
- 本轮不继续沿 `prom1 cap100` 单纯放松风险暴露，改为验证更独立的底座结构：把当前 `80/20 equal_weight` 上最强的 `prom1 cap100` 原型迁移到 `70/30 equal_weight` 与 `60/40 equal_weight` 两个底座。
- 计划只补跑 8 个四窗口 base candidates：`core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100`、`core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom1_core_6_1_cash_off_and_cap100`、`core_explore_70_30_equal_weight_winner_core__aggr_04_96_prom1_core_6_1_cash_off_and_cap100`，以及对应的 `60/40 equal_weight` 四个同名变体；这些候选仍归入现有 `high_concentration_breakout` family，不新增 family 规则。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2363` 行 / `607` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `220`，五个 family 规模为 `135 / 27 / 16 / 12 / 12`。
- 新底座结构没有改写任何 tracked winner 或 robust candidate。`70/30 equal_weight` 最好的是 `core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100`，`since_2020_01` 为 `31.58% CAGR / -23.68% MaxDD / 1.0231 Sharpe / 3.46 Turnover`；`60/40 equal_weight` 最好约 `27.89% CAGR / -21.61% MaxDD / 0.9952 Sharpe`，都低于当前 `80/20 equal_weight` 的 `34.12%` winner。
- 这次结果说明 `prom1 cap100` 强点对 `80/20 equal_weight` 底座较敏感，单纯降低核心占比会同步压低 `since_2020_01` 收益；下一轮应继续找更独立的 2020 信号或排序口径，而不是继续横向迁移同一底座结构。

## 本轮执行计划（2026-05-02）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 避开上一轮失效的“当前 `1/99 prom2` 月频强点直接改周频/双周频”路线，本轮只补 4 个更窄的中周期风险暴露原型：围绕 `2/98`、`3/97`、`4/96` 的 `risk50 / full_risk` 暴露与 `cap80/90` 约束，继续只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。

### 本轮快筛记录（2026-05-02）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `172`，五个 family 规模为 `87 / 27 / 16 / 12 / 12`，旧 winners 与 robust candidate 均保持不变。
- 新增 4 个中周期风险暴露原型：`aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90`、`aggr_02_98_prom2_core_6_1_full_risk_cap90`、`aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap90`、`aggr_04_96_prom2_core_6_1_cash_off_and_risk50_cap80`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2203` 行 / `567` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `180`，五个 family 规模为 `95 / 27 / 16 / 12 / 12`。
- `since_2017_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90`：`28.93% CAGR / -47.20% MaxDD / 1.0173 Sharpe / 3.89 Turnover`，相对旧 `1/99 risk50 cap95` 小幅抬升 CAGR 与 Sharpe，并略微改善回撤。
- 新原型未改写 `since_2020_01`、`since_2023_01`、`since_2025_01` 或四窗口 robust candidate；新增 2017 winner 的 `since_2020_01` 只有 `26.04% CAGR / -54.33% MaxDD / 0.8418 Sharpe`，因此下一轮不应把 `risk50 cap90` 作为 2020 主攻线。

### 本轮补充（2026-05-02 06:07 CST）

- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙仍为 `180`，五个 family 规模为 `95 / 27 / 16 / 12 / 12`，说明 family membership 口径保持稳定。
- 四窗口 tracked winner 身份未变化：`since_2017_01` 仍为 `aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90`，`since_2020_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap90`，`since_2023_01 / since_2025_01` 仍由 `aggr_05_95_prom3_core_6_1_full_risk_cap80` 系列占据。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`，指标随当前 comparison CSV 漂移到 `meanCAGR 59.93% / minCAGR 18.16% / worstMaxDD -67.50% / meanTurn 5.53`；这属于同步修正，不是新候选突破。
- 本轮仍没有把 `since_2020_01` 推向 `40%+ CAGR`；下一轮优先寻找更独立的 2020 中周期信号或底座组合，而不是继续沿 `risk50_cap90` 放松风险暴露。

### 本轮补充（2026-05-02 12:10 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙仍为 `180`，五个 family 规模为 `95 / 27 / 16 / 12 / 12`。
- 新增 4 个默认长周期动量口径的中周期原型：`aggr_01_99_prom2_cash_off_and_cap90`、`aggr_01_99_prom2_full_risk_cap90`、`aggr_02_98_prom2_cash_off_and_cap90`、`aggr_02_98_prom2_full_risk_cap90`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2235` 行 / `575` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `188`，五个 family 规模为 `103 / 27 / 16 / 12 / 12`。
- 新默认动量原型没有改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_full_risk_cap90`，仅 `14.31% CAGR / -56.03% MaxDD / 0.5113 Sharpe / 4.31 Turnover`，明显弱于当前 `32.25%` winner；`cash_off_and` 版本只有约 `10.75% CAGR`。
- 新原型在 `since_2025_01` 可做出 `110.29% CAGR`（`aggr_02_98_prom2_cash_off_and_cap90`），但仍低于当前短窗 winner 的 `147.54% CAGR`。下一轮不要继续把默认长周期动量作为 2020 主攻方向，应转向更独立的信号或底座组合。

### 本轮补充（2026-05-02 18:08 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `188`，五个 family 规模为 `103 / 27 / 16 / 12 / 12`。
- 新增 4 个 `core_3_1` 中周期高集中原型：`aggr_01_99_prom2_core_3_1_cash_off_and_risk50_cap95`、`aggr_01_99_prom2_core_3_1_full_risk_cap95`、`aggr_02_98_prom2_core_3_1_cash_off_and_risk50_cap95`、`aggr_02_98_prom2_core_3_1_full_risk_cap95`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `1717` 行 / `580` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `195`，五个 family 规模为 `111 / 27 / 16 / 12 / 12`。
- 新原型改写 `since_2017_01` Path 2 tracked winner 为 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom2_core_3_1_full_risk_cap95`：`33.40% CAGR / -47.23% MaxDD / 0.8712 Sharpe / 5.79 Turnover`，属于收益上限提升但 Sharpe 与换手明显承压的高风险长窗 winner。
- `since_2020_01`、`since_2023_01`、`since_2025_01` 与四窗口 robust candidate 均未改写；新增候选在 `since_2020_01` 最好仅 `24.37% CAGR`（总市值底座 `1/99 risk50 cap95`），明显弱于当前 `32.25%` winner。下一轮不应把 `core_3_1 full_risk` 作为 2020 主攻线，应继续寻找更独立的 2020 信号或底座组合。

## 本轮执行计划（2026-05-01）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点沿 `since_2020_01` 当前强点附近继续扩展中周期高集中 prom2 原型；本轮只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。

### 本轮快筛记录（2026-05-01）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `140`，五个 family 规模为 `63 / 27 / 16 / 10 / 10`；旧 `since_2020_01` winner 仍是 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95`。
- 新增 4 个围绕当前强点的高集中 prom2 原型：`aggr_01_99_prom2_core_6_1_cash_off_and_risk30_cap95`、`aggr_01_99_prom2_core_6_1_cash_off_and_risk50_cap95`、`aggr_01_99_prom2_core_6_1_full_risk_cap95`、`aggr_01_99_prom2_core_6_1_cash_off_and_cap90`。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2075` 行 / `535` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `148`，五个 family 规模为 `71 / 27 / 16 / 10 / 10`。
- `since_2017_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_risk50_cap95`：`28.89% CAGR / -47.26% MaxDD / 1.0140 Sharpe / 3.89 Turnover`，相对旧 `risk50_cap80` 小幅抬升 CAGR 与 Sharpe，但回撤略深。
- `since_2020_01` Path 2 winner 身份从 `cap95` 漂移到 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap90`，关键指标持平为 `32.25% CAGR / -22.51% MaxDD / 1.1511 Sharpe / 2.94 Turnover`；这属于 cap 约束未触发下的弱等价切换，不代表收益上限突破。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.98% / minCAGR 18.01%`）。新增 `risk30/risk50/full_risk` 版本没有改善 `since_2020_01`，后续应避免继续单纯放松风险暴露。

### 本轮补充（2026-05-01 06:11 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `148`，五个 family 规模为 `71 / 27 / 16 / 10 / 10`，旧 winners 与 robust candidate 均保持不变。
- 新增 4 个围绕当前 `1/99`、`2/98` 强点的晋升 3 只高集中原型：`aggr_01_99_prom3_core_6_1_cash_off_and_cap90`、`aggr_01_99_prom3_core_6_1_cash_off_and_cap95`、`aggr_02_98_prom3_core_6_1_cash_off_and_cap90`、`aggr_02_98_prom3_core_6_1_cash_off_and_cap95`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2107` 行 / `543` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `156`，五个 family 规模为 `79 / 27 / 16 / 10 / 10`。
- 新晋升 3 只原型未改写任何 tracked winner 或 robust candidate；其中 `since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom3_core_6_1_cash_off_and_cap90` / `cap95`，仅 `26.41% CAGR / -22.77% MaxDD / 1.0351 Sharpe / 2.82 Turnover`，明显低于当前 `since_2020_01` winner 的 `32.25% CAGR`。
- `since_2025_01` 新原型最好的是 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom3_core_6_1_cash_off_and_cap90` / `cap95`（`124.67% CAGR / -12.08% MaxDD / 2.2307 Sharpe`），仍低于当前短窗 winner 的 `145.68% CAGR`。下一轮不应继续单纯把 `prom2` 放宽到 `prom3`，而应寻找更独立的 2020 中周期信号或底座组合。

### 本轮补充（2026-05-01 12:11 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `156`，五个 family 规模为 `79 / 27 / 16 / 10 / 10`，旧 winners 与 robust candidate 均保持不变。
- 新增 4 个更独立的 `core_3_1` 高集中 prom2 原型：`aggr_01_99_prom2_core_3_1_cash_off_and_cap90`、`aggr_01_99_prom2_core_3_1_cash_off_and_cap95`、`aggr_02_98_prom2_core_3_1_cash_off_and_cap90`、`aggr_02_98_prom2_core_3_1_cash_off_and_cap95`；仍只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2139` 行 / `551` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `164`，五个 family 规模为 `87 / 27 / 16 / 10 / 10`。
- 新 `core_3_1` 原型没有改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_3_1_cash_off_and_cap90` / `cap95`，仅 `17.82% CAGR / -22.47% MaxDD / 0.7887 Sharpe / 2.76 Turnover`，明显低于当前 `32.25%` winner。
- `since_2025_01` 新原型最好的是 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_core_3_1_cash_off_and_cap90` / `cap95`（`94.82% CAGR / -12.85% MaxDD / 1.6521 Sharpe`），同样低于当前短窗 winner 的 `145.68% CAGR`。下一轮不应继续沿 `3_1 + cash_off_and` 高集中线加码。

### 本轮补充（2026-05-01 18:14 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `164`，五个 family 规模为 `87 / 27 / 16 / 10 / 10`，旧 winners 与 robust candidate 均保持不变。
- 避开前几轮失效的 `prom3` 与 `core_3_1 + cash_off_and` 高集中线，本轮新增 4 个当前 `since_2020_01` 月频强点的高频执行原型：`aggr_01_99_prom2_core_6_1_cash_off_and_cap90_biweekly`、`aggr_01_99_prom2_core_6_1_cash_off_and_cap90_weekly`、`aggr_01_99_prom2_core_6_1_cash_off_and_cap95_biweekly`、`aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2171` 行 / `559` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `172`，五个 family 规模为 `87 / 27 / 16 / 12 / 12`。
- 新高频原型没有改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是等权单周版本（`16.09% CAGR / -35.74% MaxDD / 0.5795 Sharpe / 8.16 Turnover`），双周版本只有约 `9.12% CAGR` 且回撤超过 `-60%`，明显低于当前月频 winner 的 `32.25% CAGR / -22.51% MaxDD / 1.1511 Sharpe`。
- `since_2023_01` 新原型只有双周版本保留正收益（总市值底座约 `26.68% CAGR / -31.43% MaxDD / 1.0267 Sharpe`），单周版本转负；`since_2025_01` 最好也仅约 `60.73% CAGR`，远低于当前短窗 winner 的 `145.68% CAGR`。下一轮不应继续把当前 `1/99 prom2` 月频强点简单改成周频/双周频。

## 本轮执行计划（2026-04-30）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点仍是保持 `100+` family-ranked universe，并优先观察是否出现更适配 `since_2020_01` 的中周期高收益原型；若无 winner 改写，只同步记录扫描结果。

### 本轮快筛记录（2026-04-30）

- 在发现 A 股 comparison CSV 只剩 `73` 行后，先用缓存 summary 重建为 `1477` 行 / `500` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`。
- 本轮候选宇宙为 `115`，五个 family 规模为 `43 / 23 / 16 / 10 / 10`，仍满足 `100+` family-ranked universe 要求；减少的 `1` 个候选来自缓存中不再可匹配的空 membership 行，不影响五族结构。
- 四窗口 tracked winner 身份继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe`）。
- 四窗口 robust candidate 身份继续是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`，指标随 `as_of=2026-04-30` 同步到 `meanCAGR 57.98% / minCAGR 18.01% / worstMaxDD -67.50%`。
- 本轮仍没有找到能把 `since_2020_01` 推向 `40%+ CAGR` 的中周期高收益原型；价值主要是恢复完整候选扫描口径并同步 `2026-04-30` 指标漂移。

### 本轮补充（2026-04-30 06:35 CST）

- 新增 4 个中周期 Path 2 原型并只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量：`aggr_04_96_prom3_core_6_1_cash_off_and_cap70`、`aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70`、`aggr_06_94_prom4_core_6_1_full_risk_cap70`、`aggr_06_94_prom4_core_6_1_cash_off_and_cap70`。
- 微批量回测后用缓存 summary 重建 comparison CSV 到 `1979` 行 / `511` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `124`，五个 family 规模为 `47 / 27 / 16 / 10 / 10`。
- 新原型没有改写 tracked winners 或 robust candidate。新增候选里 `since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_04_96_prom3_core_6_1_cash_off_and_cap70`，仅 `25.37% CAGR / -24.64% MaxDD / 1.0102 Sharpe / 2.83 Turnover`，明显低于当前 Path 2 2020 winner 的 `32.07% CAGR`。
- 新原型的有效观察主要在 `since_2023_01` sidecar：`aggr_06_94_prom4_core_6_1_full_risk_cap70` 达到 `46.12% CAGR` 但 MaxDD 深至 `-47.32%`；`aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70` 达到 `42.86% CAGR / 1.3744 Sharpe / -32.63% MaxDD`，仍低于当前 2023 winner 的 `57.48% CAGR`。
- `since_2025_01` 新原型最好的是 `core_explore_80_20_total_mv_winner_core__aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70`（`135.01% CAGR / -11.56% MaxDD / 2.3268 Sharpe`），仍低于当前短窗 winner `aggr_03_97_prom2_core_6_1_cash_off_and_cap80` 的 `145.68% CAGR`。

### 本轮补充（2026-04-30 12:12 CST）

- 先重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍为 `124` 个候选，五个 family 规模为 `47 / 27 / 16 / 10 / 10`，旧 `since_2020_01` winner 仍是 `aggr_03_97_prom2_core_6_1_cash_off_and_cap80`。
- 新增 4 个围绕 `since_2020_01` 当前强点的中周期高集中原型，并只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量：`aggr_02_98_prom2_core_6_1_cash_off_and_cap90`、`aggr_02_98_prom2_core_6_1_cash_off_and_risk30_cap90`、`aggr_04_96_prom2_core_6_1_cash_off_and_cap80`、`aggr_04_96_prom2_core_6_1_cash_off_and_risk30_cap80`。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2011` 行 / `519` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `132`，五个 family 规模为 `55 / 27 / 16 / 10 / 10`。
- `since_2020_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_cash_off_and_cap90`：`32.19% CAGR / -22.77% MaxDD / 1.1480 Sharpe / 2.95 Turnover`，相对旧 winner `32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe / 2.95 Turnover` 小幅抬升收益并改善回撤。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.98% / minCAGR 18.01%`）；新原型的 `risk30` 版本在 2017 长窗进入前列，但 2020 回撤过深，不作为主 winner。

### 本轮补充（2026-04-30 18:16 CST）

- 在 `since_2020_01` 强点附近继续新增 4 个高集中 prom2 原型，并只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口微批量：`aggr_01_99_prom2_core_6_1_cash_off_and_cap95`、`aggr_02_98_prom2_core_6_1_cash_off_and_cap95`、`aggr_03_97_prom2_core_6_1_cash_off_and_cap90`、`aggr_04_96_prom2_core_6_1_cash_off_and_cap90`。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2043` 行 / `527` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `140`，五个 family 规模为 `63 / 27 / 16 / 10 / 10`。
- `since_2020_01` Path 2 tracked winner 再次改写为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95`：`32.25% CAGR / -22.51% MaxDD / 1.1511 Sharpe / 2.94 Turnover`，相对 12:12 winner 小幅抬升收益、Sharpe，并改善回撤与换手。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.98% / minCAGR 18.01%`）；新增 `cap95/cap90` 原型有效改善 2020 窗口，但还没有把 `since_2020_01` 推向 `40%+ CAGR`。

## 上轮执行计划（2026-04-29）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点仍是维持 `100+` family-ranked universe，并优先观察是否出现更适配 `since_2020_01` 的中周期高收益原型；若无 winner 改写，只同步记录扫描结果。

### 本轮快筛记录（2026-04-29 12:04 CST）

- 在重建后的完整 comparison CSV 上重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`，候选宇宙恢复为 `116`，五个 family 规模为 `43 / 23 / 16 / 10 / 10`。
- 四窗口 tracked winner 与 robust candidate 继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe`），`robust` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 本轮没有找到能把 `since_2020_01` 推向 `40%+ CAGR` 的中周期高收益原型；当前价值主要是恢复被局部 CSV 压缩掉的 `100+` 候选扫描口径。

### 本轮快筛记录（2026-04-29 18:50 CST）

- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙仍为 `116`，五个 family 规模继续为 `43 / 23 / 16 / 10 / 10`。
- 四窗口 tracked winner 与 robust candidate 身份继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe`），`robust` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 本轮新增价值仍是确认 `100+` family-ranked universe 的五族口径稳定；没有出现能把 `since_2020_01` 推向 `40%+ CAGR` 的中周期高收益原型。

## 上轮执行计划（2026-04-28）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点仍是维持 `100+` family-ranked universe，并优先观察是否出现更适配 `since_2020_01` 的中周期高收益原型；若无 winner 改写，只同步记录扫描结果。

### 本轮快筛记录（2026-04-28 00:06 CST）

- 运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数 `103`，五个 family 规模继续为 `43 / 23 / 16 / 4 / 4`。
- 四窗口 tracked winner 与 robust candidate 的身份未改写，只出现缓存指标小幅漂移：`since_2020_01` winner 仍是 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（CAGR `32.07%`），`robust` 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 当前 `since_2020_01` 仍未冲到 `40%+ CAGR`，下一轮继续优先寻找更适配 2020 的中周期高收益原型，而不是扩大高频候选权重。

### 本轮快筛记录（2026-04-28 12:04 CST）

- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数仍为 `103`，五个 family 规模仍为 `43 / 23 / 16 / 4 / 4`。
- 四窗口 tracked winner 与 robust candidate 身份继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（CAGR `32.07%`），`robust` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 本轮没有找到能把 `since_2020_01` 推向 `40%+ CAGR` 的中周期高收益原型；下一轮继续优先扩大真正适配 2020 的独立原型，而不是简单增加周频/双周频权重。

### 本轮快筛记录（2026-04-28 18:29 CST）

- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数扩到 `116`，五个 family 规模为 `43 / 23 / 16 / 10 / 10`。
- 四窗口 tracked winner 与 robust candidate 身份继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（CAGR `32.07%`），`robust` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 本轮新增的周频/双周频候选规模提升了 family-ranked universe，但仍没有把 `since_2020_01` 推向 `40%+ CAGR`；下一轮继续优先寻找更适配 2020 的中周期高收益原型。

## 1. 当前目标

- 路线：`Path 2` 无约束上限探索
- 主目标：
  - 优先提升 `2020 / 2023` 两个窗口的 CAGR
  - 保持 `2025` 超短窗口仍然具备爆发力
  - 允许比 `Path 1` 更高的集中度、更激进的持仓与风控
- 现实检查（基于当前缓存结果）：截至 `2026-04-21`，`since_2020_01` 窗口在现有策略家族里的上限约 `~35.85% CAGR`，要冲击 `40%+` 仍需要新增更激进且更独立的候选族（或更激进的信号/约束组合），并针对 `since_2020_01` 补跑小批量回测。
- 当前研究原则：
  - 不受 `winner_core` 主线约束
- 每次迭代固定覆盖 `5` 条独立候选族
  - 每条候选族内部保留 `4-6` 个有代表性的候选
  - 单轮显式原型预算控制在 `24-36` 个，family-ranked universe 目标保持在 `100+`

## 2. 当前主线假设

当前 `Path 2` 的核心假设如下：

1. 想把 `2020 / 2023` 推到 `40%+ CAGR`，不能只在 `Path 1` 的约束框架里微调，必须允许更高集中和更激进的候选。
2. 真正高收益候选，往往会在：
   - 等权或弱底座结构
   - 更短周期趋势/突破信号
   - 更强行业主线
   - 更高单票上限
   这些方向里出现。
3. `Path 2` 的候选生成应以“独立候选族”为单位推进，而不是从 `Path 1` 结果里被动捡赢家。
4. 在当前阶段，`Path 2` 的最大问题不是收益不够激进，而是：
   - 候选族还不够真正独立
   - 高收益版本的回撤往往过深
   - 还没有形成一套“高收益但可持续迭代”的研究体系
5. 单纯把月度调仓提升到双周/单周，并不足以自动改善 `since_2020_01`；下一轮新增探索强度应优先投向更适配 `2020` 的中周期高收益原型，而不是继续平均强化 `2023 / 2025`。
6. 候选族归类必须使用更严格的“显式 variant + 窄 prefix”规则，避免宽前缀匹配把不同家族压到一起，削弱代表候选的独立性。

## 3. 当前独立候选族

目前 `Path 2` 已经开始用独立候选扫描逻辑，当前重点拆成五类候选族：

### A. 高集中突破

特点：

- 更少持仓
- 更高单票上限
- 更强调突破、加速、趋势延续
- 更适合牛市或强主线阶段

当前代表方向（目标 `4-6` 个）：

- `aggr_05_95_prom3_core_6_1_full_risk`
- `aggr_05_95_prom3_core_6_1_full_risk_cap60`
- `aggr_05_95_prom3_core_6_1_cap60`
- `aggr_05_95_prom3_core_6_1_cash_off_and_cap60`

近期新增的 bridging 原型（用于验证“更高集中 + 明确 risk-off”是否能改善 `since_2020_01`）：

- `aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
- `aggr_03_97_prom2_core_6_1_cash_off_and_risk30_cap80`
- `aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`

### B. 高成长主线

特点：

- 更强调行业主线、成长加速、龙头放大
- 倾向于更早切入高成长方向
- 容忍更高波动

当前代表方向（目标 `4-6` 个）：

- `aggr_08_92_prom6_full_risk`
- `aggr_08_92_prom6_core_6_1_full_risk`
- `aggr_08_92_prom6_core_6_1_full_risk_cap40`
- `aggr_08_92_prom6_core_6_1_full_risk_cap60`
- `aggr_10_90_fast_ramp_cash_off_and`

### C. 动量 / 等权高弹性

特点：

- 不再限定为单一底座（等权 / `total_mv` 均可）
- 更强调动量、等权、高弹性
- 更容易在短中窗口做出很高收益

当前代表方向（目标 `4-6` 个）：

- `core_explore_80_20_equal_weight_winner_core...`
- `momentum_top_...`
- `aggr_08_92_prom6_cash_off_and`
- `aggr_05_95_prom3_core_6_1_cash_off_and_cap60`

### D. 双周调仓高收益族

特点：

- 以双周调仓代替月度调仓
- 比月度更快响应，但不至于像单周那样过于高噪音
- 优先观察 `since_2020_01 / since_2023_01`

当前代表方向（目标 `4-6` 个）：

- `aggr_08_92_prom6_core_6_1_full_risk_cap60_biweekly`
- `aggr_05_95_prom3_core_6_1_full_risk_cap60_biweekly`
- `aggr_08_92_prom6_cash_off_and_biweekly`

### E. 单周调仓高收益族

特点：

- 以单周调仓追求更高收益上限
- 更适合高集中突破 / 高弹性动量候选
- 更容易带来更高换手和更深波动

当前代表方向（目标 `4-6` 个）：

- `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`
- `aggr_05_95_prom3_core_6_1_full_risk_cap60_weekly`
- `aggr_08_92_prom6_cash_off_and_weekly`

## 4. 当前默认候选生成

当前 `Path 2` 使用独立扫描脚本：

- [scripts/path2_candidate_pass.py](/Users/valselee/my-code/aiinvestor/scripts/path2_candidate_pass.py)

当前候选来源已经从“统一候选池”升级成**显式多候选族生成**：

1. `high_concentration_breakout`
   - 更高集中
   - 更少持仓
   - 更看突破与趋势延续
2. `high_growth_theme`
   - 更看成长主线
   - 更看行业主线与业绩加速
3. `momentum_equal_weight_elastic`
   - 更弱底座
   - 更高弹性
   - 更适合从 `2023 / 2025` 里挖上限

脚本现在会按候选族输出：
- 候选族规模
- 每族目标预算
- 每族排序后的代表候选

当前默认扫描宇宙（`2026-04-28`）已提升到 `116` 个 candidates；五个 family 的当前规模分别为 `43 / 23 / 16 / 10 / 10`。其中 `high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic` 三条长周期 family 已显式纳入 `core_explore_80_20_total_mv_winner_core` 这一窄 prefix，避免当前 `since_2025 / robust` 的 `total_mv` tracked winners 脱离 family ranking。

说明：

- 这些候选的目的不是“稳”，而是尽快拉高收益上限。
- 其中一部分候选的回撤会明显深于 `Path 1`，这是当前阶段允许的。
- 下一轮晋级逻辑对 `since_2020_01` 加权更高；若某候选只明显强化 `since_2023_01 / since_2025_01` 而不能改善 `since_2020_01`，默认不作为主攻方向。
- 当前 family ranking 已从“宽 prefix 匹配”改成“显式 variant + 少数 prefix-only 家族”：
  - 大多数候选族必须命中明确的 `variant_id`
  - 只有 `momentum_top_*` / `satellite_mom_*` 这类天然独立的前缀族允许 prefix-only 归类
  - 这样五条候选族的代表性会更清晰，不再被同一个大前缀重复稀释

## 5. 下一轮优先尝试的方向

## 5.1 本轮（2026-04-21）执行清单（覆盖 5 条独立候选族）

本轮 `Path 2` 固定覆盖以下 `5` 条候选族，不再减少到 `3` 条：

1. **高集中突破族**：继续围绕 `aggr_05_95_prom3_core_6_1_*`，观察高集中高弹性版本在 `since_2020_01 / since_2023_01` 的上限弹性。
2. **高成长主线族**：继续围绕 `aggr_08_92_prom6*_full_risk*`，重点观察是否能真正把 `since_2020_01` 往 `40%+ CAGR` 推。
3. **动量 / 等权高弹性族**：继续围绕 `equal_weight_winner_core*` 与 `momentum_top_*`，但若仅强化 `since_2023_01 / since_2025_01`，默认不作为主攻方向。
4. **双周调仓高收益族**：保留在扫描宇宙里，继续作为“更高频但不过度高噪音”的中间态候选。
5. **单周调仓高收益族**：保留在扫描宇宙里，继续作为最高弹性的激进候选族。

对应执行约束（本轮固定）：

- 必须先独立运行 `scripts/path2_candidate_pass.py`，并以 `PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 定义的候选宇宙为准。
- 每条候选族最多只允许前 `1-2` 个代表候选晋级完整确认。
- 晋级优先顺序固定为：
  1. `since_2020_01` 有显著改善
  2. `since_2023_01` 不明显退化
  3. 回撤和换手仍在可接受范围内
- 双周 / 单周候选族继续保留，但不因为“更高频”而自动获得更高优先级。

### 本轮方向性结论（2026-04-21）

- 双周 / 单周两条新族已经正式接入 `Path 2` 扫描宇宙。
- 第一轮结果表明：单纯提频并没有改写当前 `Path 2` 的窗口赢家。
- 因此下一轮默认策略是：
  - 保留双周 / 单周候选族
  - 但新增探索强度优先投向更适配 `since_2020_01` 的中周期高收益原型
  - 不再平均强化 `since_2023_01 / since_2025_01`

### 本轮快筛记录（2026-04-21 17:57）

- 运行 `scripts/path2_candidate_pass.py`：候选数 `49`，四窗口赢家与四窗口鲁棒候选均未改写。
- 当前（缓存结果）仍然显示：
  - `since_2017_01 / since_2020_01 / since_2025_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（`since_2020_01` 仍约 `35.85% CAGR`）。
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（上限高但回撤深）。
  - `robust`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80`（`meanCAGR~57.11% / minCAGR~26.93%`）。
- 补充（2026-04-21 18:02）：
  - 新增两条候选：`aggr_05_95_prom3_core_6_1_cash_off_and_cap80`、`aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80`，并各自跑了 `since_2017_01/2020_01/2023_01` 离线微回测（复用缓存）后重建对比 CSV。
  - 重跑 `scripts/path2_candidate_pass.py`：候选数增至 `51`，四窗口赢家与鲁棒候选仍未改写；新变体在 `since_2020_01` 上限仅约 `26% CAGR`，明显不具竞争力。

## 5.0 上轮（2026-04-19）执行清单（覆盖 3 条独立候选族）

上轮 `Path 2` 严格按“独立候选族”推进，优先覆盖 3 条候选族（每条内部只观察 3-5 个代表候选，不做无差别全扫）：

1. **高集中突破族**：围绕 `aggr_05_95_prom3_core_6_1_full_risk(_cap60)` 这一支，重点看 `since_2023_01 / since_2025_01` 是否继续维持 `40%+` 的上限弹性。
2. **高成长主线族**：围绕 `aggr_08_92_prom6_core_6_1_full_risk_(cap40/cap60)`，优先把 `since_2020_01 / since_2023_01` 往 `40%+` 推。
3. **动量 / 等权高弹性族**：继续扩展 `core_explore_80_20_equal_weight_winner_core*` 与 `momentum_top_*` 两条前缀族的代表候选，用于寻找更“轻底座”的爆发版本。

对应的预算约束：

- 每轮至少覆盖 `3` 条独立候选族
- 每条候选族至少保留 `4-6` 个代表候选
- 单轮快筛总预算目标 `24-36` 个
- 脚本侧每族目标预算默认按 `target_candidates=6` 执行（3 族合计 `<=18`），避免无意义扩大代表候选数

对应的执行约束：

- 必须先独立运行 `scripts/path2_candidate_pass.py`，并以其扫描规则（`PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS`）作为 Path 2 的候选宇宙。
- Path 2 的窗口赢家与鲁棒候选允许跑输 Path 1（不要求先打赢再记录），但必须**持续**单独维护四窗口赢家 + 四窗口鲁棒候选。
- 若本轮没有出现新的窗口赢家或鲁棒候选改写，则只更新本文档的研究记录，不额外补跑确认回测。

### 本轮快筛记录（2026-04-19）

- `scripts/path2_candidate_pass.py`（独立候选扫描）未改写当前已记录的四窗口赢家与四窗口鲁棒候选。
- 补充（2026-04-19 20:50）：重跑扫描，四窗口赢家与四窗口鲁棒候选结论不变；当时 `since_2020_01` 上限仍约 `~25% CAGR`（后续已提升到 `35.85%`，但仍未到 `40%+`）。
- 当前（缓存结果）仍然显示：
  - `since_2023_01` 上限主要来自 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（收益上限高，但回撤深）。
  - `since_2020_01` 在现有候选宇宙内仍停留在 `~35.85% CAGR` 附近，需要更独立、更激进（且针对 2020 的）新候选族才有机会冲击 `40%+`。

## 5.1 本轮（2026-04-20）执行清单（覆盖 5 条独立候选族）

本轮 `Path 2` 继续严格按“独立候选族”推进，覆盖以下 5 条候选族（不要求先打赢 Path 1 才记录）：

1. **高集中突破族**：继续围绕 `aggr_05_95_prom3_core_6_1_*`，重点看 `since_2023_01 / since_2025_01` 的上限弹性是否可持续。
2. **高成长主线族**：继续围绕 `aggr_08_92_prom6*_full_risk*` 与 `aggr_10_90_fast_ramp_cash_off_and`，优先把 `since_2020_01` 往 `40%+ CAGR` 推。
3. **动量 / 等权高弹性族**：继续把 `momentum_top_*` 与 `cash_off_and` 线作为“弱底座 + 高弹性”的候选来源，观察是否能在 `2020/2023/2025` 形成更一致的强势版本。
4. **双周调仓高收益族**：新增 `*_biweekly` 变体，验证“更快调仓但不至于像单周一样高噪音”的中间解是否能抬高 `2020/2023`。
5. **单周调仓高收益族**：新增 `*_weekly` 变体，验证更高频调仓是否能给高集中突破和高弹性候选带来更高上限。

对应执行约束（本轮继续沿用）：

- 必须先独立运行 `scripts/path2_candidate_pass.py`，并以 `backtest_marketcap_etf.py` 中 `PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 定义的候选宇宙为准。
- Path 2 必须持续单独维护四窗口赢家 + 四窗口鲁棒候选。
- 若本轮没有出现新的窗口赢家或鲁棒候选改写，则只更新本文档的研究记录，不额外补跑确认回测。

### 本轮快筛记录（2026-04-20）

- 先后运行 `.venv/bin/python scripts/path2_candidate_pass.py`（基于缓存对比 CSV）：
  - 扩展 `PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 后，`path2 candidates=43`；四窗口赢家与四窗口鲁棒候选均未改写。
- 补充（2026-04-20 13:21）：重跑 `scripts/path2_candidate_pass.py`，四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-20 18:54）：再次重跑 `scripts/path2_candidate_pass.py`，`candidates=43`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-20 20:23）：运行 `scripts/path2_candidate_pass.py`，`candidates=43`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-21 10:17）：先重建 `strategy_comparison_base_method.csv`（覆盖 `since_2017_01/2020_01/2023_01`）后运行 `scripts/path2_candidate_pass.py`，`candidates=46`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-21 12:13）：运行 `scripts/path2_candidate_pass.py`，`candidates=46`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-21 14:18）：运行 `scripts/path2_candidate_pass.py`，`candidates=46`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-21 16:36）：新增/恢复高集中候选变体（含 `prom2_cap80`）并离线补跑小批量回测（`since_2017_01/2020_01/2023_01`），随后重建对比 CSV 并复扫 `scripts/path2_candidate_pass.py`：`candidates=49`；四窗口赢家与鲁棒候选均未改写。
- 当前（缓存结果）四窗口赢家与鲁棒候选：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（CAGR `31.53%`）
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（CAGR `35.85%`，仍未到 `40%+`）
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（CAGR `56.01%`）
  - `since_2025_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（CAGR `124.08%`）
  - `robust`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80`（meanCAGR `57.11%` / minCAGR `26.93%`）

## 5.2 本轮（2026-04-21）执行清单（覆盖 3 条独立候选族）

本轮 `Path 2` 继续按“独立候选族”推进，研究重点限定在以下 `3` 条候选族：

1. **高集中突破族**：继续围绕 `aggr_05_95_prom3_core_6_1_*`，重点观察 `since_2023_01 / since_2025_01` 的上限弹性是否稳定。
2. **高成长主线族**：继续围绕 `aggr_08_92_prom6*_full_risk*`，重点把 `since_2020_01 / since_2023_01` 往 `40%+ CAGR` 推。
3. **动量 / 等权高弹性族**：继续围绕 `equal_weight_winner_core*` 与 `momentum_top_*` 的代表候选，寻找“弱底座 + 高弹性”的更一致版本。

对应执行约束（本轮继续沿用）：

- 必须先独立运行 `scripts/path2_candidate_pass.py`（基于缓存对比 CSV），并以 `backtest_marketcap_etf.py` 中的扫描规则作为候选宇宙。
- Path 2 必须持续单独维护四窗口赢家 + 四窗口鲁棒候选；不要求先打赢 Path 1 才记录。
- 若本轮没有出现新的窗口赢家或鲁棒候选改写，则只更新本文档的研究记录，不额外补跑确认回测。

### A. 更高集中度的突破线

假设：

- 当前高收益候选已经说明更高集中度有效，但还不够纯粹

目标：

- 进一步压缩持仓数
- 强化前 1-2 名权重
- 重点观察 `2020 / 2023` 是否继续上行

预期：

- CAGR 继续提升
- 回撤可能恶化，需要后续第二阶段处理

### B. 行业主线 + 成长加速的更强版本

假设：

- 单纯高动量不够，需要更强的行业主线约束

目标：

- 提升“高成长主线”候选族的纯度
- 减少弱行业里的短期强股

预期：

- 有望提高中窗口质量
- 但实现复杂度更高

### C. 等权 / 高弹性体系的更极端版本

假设：

- 当前 `equal_weight_winner_core` 已经说明“弱底座”有更高爆发力

目标：

- 进一步削弱市值/稳定性约束
- 放大真正强势票的收益贡献

预期：

- 对 `2023 / 2025` 更有利
- `2017` 可能仍然承受很大回撤

## 6. 已淘汰或暂缓的方向

### 6.1 把 Path 2 当成“Path 1 的激进变体集合”

结论：

- 已淘汰。

原因：

- 会导致 `Path 2` 的 winner 仍然大量来自 `Path 1`
- 路径虽然名义独立，但本质没有独立研究价值

当前处理：

- `Path 2` 已经开始使用独立 candidate pass
- 后续应继续扩大独立候选族，而不是继续依赖 `Path 1`

### 6.2 过早把回撤控制作为第一优先级

结论：

- 暂缓。

原因：

- 会直接压掉 `Path 2` 最重要的收益上限探索能力

当前处理：

- 第一阶段先接受更深回撤
- 等形成稳定高收益候选后，再单独研究回撤收敛方案

## 7. 本轮执行规范

每次自动/手动 `Path 2` 迭代，应尽量遵守：

1. 先跑独立 candidate pass，而不是复用 Path 1 fast pass。
2. 每轮固定覆盖 `3` 条独立候选族。
3. 每条候选族内部保留 `4-6` 个代表候选，单轮总预算目标 `24-36` 个。
4. 若某方向虽然收益高，但连续多轮只在一个窗口短暂领先、且回撤极端失控，应写入“暂缓/观察”。
5. 若某候选在 `2020 / 2023 / 2025` 都显著强，应优先进入 `Path 2 robust candidate` 比较。

## 8. 当前观察重点

当前最值得持续观察的是这类候选：

- `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`

原因：

- 在 `2023 / 2025` 窗口已经表现出明显更高的收益弹性
- 说明 `Path 2` 的独立方向正在形成

但它当前的问题也非常明确：

- `2017 / 2020` 的回撤过深
- 还不能直接作为“生产候选”

所以当前更合理的定位是：

- 它是 `Path 2` 的收益上限样本
- 不是当前最终版本

## 9. 维护说明

本文档用于记录 `Path 2` 的研究规划与候选族结构，不用于写死最新数值。  
最新赢家和指标仍以：

- `README.md` 顶部自动区块
- `HISTORY.md`
- `results/weighted_track_winners.json`
- `results/path2_candidate_pass.json`

为准。

## 10. 本轮补充（2026-04-21 18:24）

- 重跑 `scripts/path2_candidate_pass.py`：候选数仍为 `51`，四窗口赢家与 `robust` 候选均未改写。

## 11. 本轮补充（2026-04-21 20:18）

- 重跑 `scripts/path2_candidate_pass.py`：候选数 `51`，四窗口赢家与 `robust` 候选结论不变。

## 12. 本轮补充（2026-04-21 22:20）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数 `51`；四窗口赢家与 `robust` 候选均未改写（近期目标 `since_2020_01 40%+ CAGR` 仍需新增更独立、更激进的候选族）。

## 13. 本轮补充（2026-04-22）

- 运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数仍为 `51`；四窗口赢家与 `robust` 候选继续不变。
- 当前五个候选族的前排仍被同一批高集中等权变体占住，说明“新增周频/双周频族”目前主要是在扩扫描宇宙，还没有形成真正独立的 `since_2020_01` 赢家族。
- `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80` 仍是几乎所有候选族里的最高 promotion-score 候选：`since_2020_01 CAGR 35.76% / since_2023_01 CAGR 50.65% / worst MaxDD -38.62%`；它强化了 `2023`，但仍没有把 `2020` 推到 `40%+`。
- `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60` 继续是 `since_2020_01` 窗口赢家（`35.85% CAGR`），`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80` 继续是 `since_2023_01` 窗口赢家（`56.01% CAGR`）。
- 下一轮新增探索预算不应继续平均投向提频变体；更合理的方向是新增真正面向 `2020` 的中周期高收益原型，而不是再复制一轮 `monthly -> biweekly -> weekly` 频率克隆。
- 本次再次用 `AIINVESTOR_FORCE_OFFLINE=1` 重跑后，五个候选族的前二仍被同一组 `aggr_05_95_prom3_core_6_1_*` 高集中等权变体占据；`risk30_cap80` 的 promotion score 仍约 `0.5033`，而 `cap60` 仍是 `since_2020_01` 的最高窗口赢家（`35.85% CAGR`），说明现有扫描宇宙新增部分还没有产出新的独立 family leader。
- `2026-04-22 06:27 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数仍为 `51`，窗口赢家与 `robust` 候选继续不变。
- 追加了一个只看 `since_2020_01 / since_2023_01` 的 sidecar 微回测：把 `aggr_05_95_prom3_core_6_1_cash_off_and_cap60 / risk30_cap80 / risk50_cap80` 从 `80/20` 扩到 `70/30`、`60/40` 等权底座后，全部都弱于当前 `80/20` 主线。
- 其中新组里表现最好的也只有：
  - `since_2020_01`：`core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`，`CAGR 26.86% / MaxDD -22.83% / Sharpe 1.0641 / Turnover 3.11`
  - `since_2023_01`：`core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80`，`CAGR 37.72% / MaxDD -28.76% / Sharpe 1.2732 / Turnover 3.98`
- 结论：当前瓶颈不在 `core/explore` 比例本身，而在候选原型没有真正把 `since_2020_01` 推过 `40%+`；下一轮不应继续把新增预算投到 `80/20 -> 70/30/60/40` 的比例克隆上。
- 本轮继续新增了 `prom2 + cash_off_and + cap80` 三个原型，并离线补跑 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01` 后重建对比 CSV，再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数从 `51` 增至 `63`。
- 新组里表现最好的 `since_2020_01` 候选是 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`，仅到 `32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe / 2.95 Turnover`；仍明显弱于当前 `since_2020_01` winner `aggr_05_95_prom3_core_6_1_cash_off_and_cap60` 的 `35.85% CAGR`。
- 但 `since_2025_01` 窗口赢家被这条新原型改写：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80` 以 `128.06% CAGR / -12.42% MaxDD / 2.1335 Sharpe / 5.80 Turnover` 超过原先的 `aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（`124.08% CAGR / -13.73% MaxDD / 2.1116 Sharpe / 6.18 Turnover`）。
- 结论更新：`prom2 + cash_off_and + cap80` 已经成为新的超短窗口赢家，但它仍不是把 `since_2020_01` 推到 `40%+` 的解。下一轮新增预算应继续面向“中周期高收益原型”，而不是继续复制 `prom2` 的频率或比例分支。
- 当日后续先用缓存重建了 `results/strategy_comparison_base_method.csv`（`427` 行 / `154` 个 base strategies），再运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数维持 `63`，但也暴露出此前 `weighted_track_winners.json` 相对当前 `summary.json` 已经滞后。
- 按这次重建后的完整 comparison CSV 重新同步后，当前真实 tracked winners 改写为：
  - `since_2017_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`（`28.08% CAGR / -46.94% MaxDD / 1.0061 Sharpe / 3.89 Turnover`）
  - `since_2020_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe / 2.95 Turnover`）
  - `since_2023_01`：`aggr_05_95_prom3_core_6_1_full_risk_cap80`（`56.40% CAGR / -50.82% MaxDD / 1.1727 Sharpe / 5.32 Turnover`）
  - `since_2025_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`128.06% CAGR / -12.42% MaxDD / 2.1335 Sharpe / 5.80 Turnover`）
  - `robust`：`aggr_05_95_prom3_core_6_1_full_risk_cap60`（`meanCAGR 54.57% / minCAGR 17.70%`）
- 这次同步后的关键信号是：当前“真实 `since_2020_01` 窗口赢家”已经降到 `32.07% CAGR`，距离 `40%+` 目标比旧快照显示的更远；因此下一轮新增探索预算必须继续投向新的中周期原型，而不是再把 `cap60 / risk30 / equal_elastic` 一类旧锚点当成已验证高水位。
- `2026-04-22 14:30 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数维持 `63`，四窗口 winner 与 `robust` 候选继续完全不变。
- 当前五个候选族的规模与前排顺位也没有漂移：`43 / 43 / 44 / 41 / 41` 的 family counts 继续稳定，而 `since_2020_01` 仍由 `aggr_03_97_prom2_core_6_1_cash_off_and_cap80` 领跑在 `32.07% CAGR`，离 `40%+` 目标仍有明显距离。
- 本轮再次确认：新增预算不该再投向频率克隆或 family 内参数平移；下一轮 `Path 2` 应继续优先寻找新的中周期高收益原型，同时把现有 `prom2_cap80` 与 `full_risk_cap80/cap60` 只保留为锚点和对照。

## 14. 本轮补充（2026-04-22 23:27 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数维持 `63`，四窗口 winner 与 `robust` 候选继续完全不变。
- 当前 tracked winners 仍是：
  - `since_2017_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01 / since_2025_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `robust`：`aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 五个候选族的规模与前排顺位继续稳定在 `43 / 43 / 44 / 41 / 41`；新增双周/单周族与 `prom2_cap80` 原型已经进入扫描宇宙，但还没有形成新的独立 family leader。
- 当前 `since_2020_01` 仍只到 `32.07% CAGR`，距离 `40%+` 目标还有明显缺口；下一轮新增预算仍应优先投向新的中周期高收益原型，而不是继续复制 `monthly -> biweekly -> weekly` 频率克隆。
- `3_1` 短周期变体继续只保留在扫描宇宙里做观察；在它们没有明确打赢当前 `6_1` 主锚点之前，不升级成新的主攻候选族。

## 15. 本轮补充（2026-04-23 01:32 CST）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：当前独立候选宇宙为 `32` 个候选，五个候选族规模为 `14 / 7 / 8 / 6 / 6`；最近几轮文档里引用的 `63` 候选快照已经不是当前 comparison CSV 的真实状态。
- 按本轮 `path2_candidate_pass.json` 与 `weighted_track_winners.json` 重新同步后，当前 Path 2 tracked winners 为：
  - `since_2017_01 / since_2020_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 当前关键指标是：
  - `since_2020_01` winner 只到 `26.20% CAGR / 1.0012 Sharpe / -28.09% MaxDD / 2.84 Turn`
  - `since_2023_01` winner 为 `52.24% CAGR / 1.1933 Sharpe / -49.35% MaxDD / 5.43 Turn`
  - `robust` 候选为 `meanCAGR 58.88% / minCAGR 17.57%`
  这说明当前瓶颈比前一版文档记录的 `32%+` 还更低，`since_2020_01 40%+ CAGR` 目标仍有明显距离。
- 本轮 family leader 也给出更清晰的取舍：
  - `high_concentration_breakout` 仍由 `aggr_05_95_prom3_core_6_1_full_risk(_cap80)` 系列主导
  - `momentum_equal_weight_elastic` 当前真正的窗口赢家已切到 `aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `biweekly / weekly_rebalance_aggressive` 的前排仍只是底座级别基线，没有出现能改写四窗口 winner 的高频 leader
- 因此下一轮 `Path 2` 继续把新增预算优先投向新的中周期高收益原型，不再给 `biweekly / weekly` 的频率克隆额外预算；它们继续只保留为对照，不升级成新的主攻族。

## 16. 本轮补充（2026-04-23 03:33 CST）

- 本轮修正了一个真实缺口：`PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 已经声明了 `aggr_08_92_prom6_core_3_1_full_risk_cap40`、`aggr_05_95_prom7_core_6_1_full_risk`、`aggr_05_95_prom7_core_6_1_full_risk_cap40`、`aggr_05_95_prom7_core_3_1_full_risk_cap40`，但 `WINNER_CORE_VARIANTS` 里此前没有这些定义，导致 candidate pass 实际跑不到它们。本轮已补齐这 4 个变体，并离线补跑 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`。
- 新补变体里最有价值的观察是：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_3_1_full_risk_cap40` 在 `since_2023_01` 做到了 `40.40% CAGR / 1.0147 Sharpe / -45.82% MaxDD / 507.33% Turnover`，说明 `prom7 + 3_1` 确实具备独立的高弹性；但它仍明显落后于当前 `since_2023_01` winner `aggr_05_95_prom3_core_6_1_full_risk_cap80` 的 `56.40% CAGR`，因此只保留为 sidecar prototype，不晋升为新主线。
- 在把新增变体结果并回全量 `summary.json` 后，重建出的 `results/strategy_comparison_base_method.csv` 已恢复到完整口径（`1744` 行 / `466` 个 base strategies）。基于这份完整 CSV，再次运行 `./.venv/bin/python scripts/path2_candidate_pass.py` 后，当前独立候选宇宙恢复为 `87` 个候选，而不是上一版局部 CSV 下看到的 `32` 个。
- 以这次完整重建后的口径为准，当前 Path 2 tracked winners 已同步为：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 关键约束没有变：即使在完整口径下，`since_2020_01` 当前 tracked winner 也只到 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`，距离 `40%+ CAGR` 目标仍有明显缺口。所以下一轮新增预算依然应该优先投向新的中周期高收益原型，而不是继续复制 `biweekly / weekly` 频率克隆。

## 17. 本轮补充（2026-04-23 05:29 CST）

- 再次运行 `./.venv/bin/python scripts/path2_candidate_pass.py`：当前独立候选宇宙仍为 `87` 个候选；四窗口 tracked winners 与 `robust_candidate` 均未改写，`since_2020_01` 仍由 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80` 领跑，但也只做到 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`。
- 本轮新增的研究发现不是 winner 改写，而是 `family_ranked_candidates` 口径仍存在串线：由于 `PATH2_SCAN_FAMILY_RULES` 里的宽前缀（尤其是 `core_explore_80_20_equal_weight_winner_core` 一类）会把同一批 `80/20` 高集中候选同时并入多个 family，当前五个 family leaderboard 仍被几乎相同的候选占满，不能真实反映“独立候选族”的前排顺位。
- 这意味着下一轮 `Path 2` 的第一优先级不该是继续追加 `biweekly / weekly` 克隆，而是先收紧 family membership 口径，再把新增预算投向真正面向 `since_2020_01` 的中周期高收益原型；否则 family 级排序会持续高估同一批 `80/20` 高集中等权版本。
- 本轮随后执行 `./.venv/bin/python scripts/update_weighted_winners.py` 与 `./.venv/bin/python scripts/generate_strategy_comparison_chart.py`：Path 2 的 tracked winners / robust candidate 文本口径没有继续漂移，但 A 股对比图按当前 tracked 基线重绘后发生了实际 binary diff，因此本轮保留 `sync-only` 提交即可，不额外补跑确认回测。

## 18. 本轮补充（2026-04-23 17:57 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：本轮 `path2_candidate_pass.json` 的真实口径是 `candidate_count=86`，五个候选族规模分别为 `21 / 8 / 9 / 4 / 4`；四窗口 tracked winners 与 `robust_candidate` 均未改写。
- 当前 tracked winners 继续维持：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 关键约束没有变化：`since_2020_01` 当前 winner 仍只做到 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`，离 `40%+ CAGR` 目标仍有明显缺口；`biweekly / weekly` 两个高频族当前都只剩 `4` 个候选，继续没有改写主线的证据。
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py` 与 `./.venv/bin/python scripts/generate_strategy_comparison_chart.py`：Path 2 的 winner/robust 文本口径仍未改写，但 README/HISTORY 与 A 股对比图已经同步到最新 `as_of=2026-04-23` 指标，因此本轮继续保留 `sync-only` 提交即可，不额外补跑确认回测。
- 下一轮 `Path 2` 继续把新增预算优先投向新的中周期高收益原型，并优先收紧 family membership 口径；不继续给 `biweekly / weekly` 频率克隆追加预算。

## 19. 本轮补充（2026-04-24）

- 本轮先把 `PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 扩到当前缓存里已经存在的一批中周期 `total_mv` 原型，并补上 `core_explore_80_20_total_mv_winner_core` 在三条长周期 family 里的窄 prefix 归类。随后运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：当前独立候选宇宙已提升到 `103` 个 candidates，五个 family 规模分别为 `43 / 23 / 16 / 4 / 4`。
- 这次扩容的目的不是立刻改写 winner，而是解决两个结构性缺口：
  - 当前 `since_2025_01` winner 与 `robust_candidate` 都落在 `total_mv` 原型上，但旧的 family rules 不能把它们纳入 family ranking。
  - `since_2020_01` 仍只有 `32.07% CAGR`，因此需要把 `aggr_05_95_prom7 / aggr_07_93_prom6 / aggr_07_93_prom8(_ramp85) / risk_on / conc35 / balance_* / mid_15_85_prom7 / share_12_88_hold_3_7` 这一批中周期原型正式纳入扫描宇宙，而不是继续只扩高频克隆。
- 扩容后四窗口 tracked winners 与 `robust_candidate` 继续不变：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py`、`./.venv/bin/python scripts/generate_strategy_comparison_chart.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：README / HISTORY / `results/weighted_track_winners.json` / `results/live` 已同步到 `as_of=2026-04-24`，但 Path 2 仍属于 `sync-only` 指标更新，没有新的窗口 winner 改写。
- 下一轮继续优先新增更适配 `since_2020_01` 的中周期高收益原型，不给 `biweekly / weekly` 两个高频族额外预算。

## 20. 本轮补充（2026-04-25）

- 本轮先按自动化规则把独立 worktree 对齐到主工作树 `main`，随后用缓存重建了 `results/strategy_comparison_base_method.csv`（`1899` 行 / `491` 个 base strategies）；这次重建把此前未并入 comparison CSV 的 cached summaries 补回到了 `Path 2` 扫描宇宙里，并把整条 A 股 artifact 链重新同步到 `sample_end=2026-04-24`。
- 本轮同时修掉了一个真实的 `Path 2` 执行层问题：极端高集中候选在周频 overlay 调仓里会把 `NaN` code 混进持仓序列，导致 `compute_rebalance_trades()` 在持仓聚合时崩溃。当前已在 `backtest_marketcap_etf.py` 中加上“丢弃空索引 + 合并重复 code”的最小修复；用 `core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80__sat_three_stage_buffered` 做窄复现后，回测已能完整跑通。
- 在这份重建后的完整 comparison CSV 上再次运行 `./.venv/bin/python scripts/path2_candidate_pass.py`：
  - `candidate_count=104`
  - family 规模为 `43 / 23 / 16 / 4 / 4`
  - 四窗口 tracked winners 与 `robust_candidate` 继续完全不变。
- 当前 Path 2 tracked winners 仍维持：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 这轮最有价值的新信息不是 winner 改写，而是“口径补齐后结论仍不变”：
  - `since_2020_01` 上限仍只到 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`
  - `robust_candidate` 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`（`meanCAGR 58.51% / minCAGR 17.57%`）
  - `biweekly / weekly` 两个高频族依旧只有 `4 / 4` 个候选，继续没有改写主线的证据
  - 新补回 CSV 的候选只把扫描宇宙从 `103` 推到 `104`，没有改变五族的主次关系。
- 因此本轮继续作为 `sync-only` 提交：同步了完整 comparison CSV、刷新了 `Path 2` tracked artifact，并把高集中候选的回测崩溃点修掉；下一轮仍优先把新增预算投向更适配 `since_2020_01` 的中周期高收益原型，而不是继续扩高频克隆。

## 21. 本轮补充（2026-04-26）

- 本轮同样先重查基线：`git fetch origin` 失败后，因当前 worktree 已知 `origin/main` 不是主工作树 `main` 的后继，本轮回退到本地主工作树 `main`（`bb3a7d7`）作为 publish baseline，再在该基线上重跑独立扫描。
- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py` 后，当前 `Path 2` 独立候选宇宙为 `117` 个 candidates；五条 family 的规模分别为 `49 / 23 / 16 / 4 / 4`。新增体量主要重新落在 `high_concentration_breakout`，说明这轮更多是在完整缓存口径下把高集中家族成员补齐，而不是出现新的高频主线。
- 四窗口 tracked winners 与 `robust_candidate` 继续不变：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 这轮最关键的约束没有变化：`since_2020_01` 上限依旧停在 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`，而 `biweekly / weekly` 两条高频族依旧只有 `4 / 4` 个候选，且没有任何一条能接近改写主线。因此本轮只把 `results/path2_candidate_pass.json`、README 自动区块与 A 股对比图同步到当前口径，不额外补跑确认回测。
- 下一轮继续把新增预算优先投向更适配 `since_2020_01` 的中周期高收益原型，并继续压紧 family membership 口径；不继续给 `biweekly / weekly` 高频克隆追加预算。

## 22. 本轮补充（2026-04-27）

- 本轮同样先按自动化基线规则重查 publish baseline：`git -C /Users/valselee/my-code/aiinvestor fetch origin main` 成功后，确认最新 `origin/main` 位于 `fd4b214`，领先于本地主工作树 `main`（`39cf735`），因此独立扫描直接基于该远端基线重放。
- 运行 `./.venv/bin/python scripts/path2_candidate_pass.py` 后，当前 `Path 2` 独立候选宇宙收敛到 `104` 个 candidates；五条 family 的规模分别是 `43 / 23 / 16 / 4 / 4`，说明这轮主要是继续压紧 `high_concentration_breakout` 的 family membership 口径，而不是扩新的高频分支。
- 四窗口 tracked winners 继续完全不变，`robust_candidate` 同步落在更稳的 `cap80` 版本：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
- 这轮新增的信息主要是“收紧 membership 后结论仍不变”：当前 `since_2020_01` ceiling 仍停在 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`，而 `robust_candidate` 的四窗汇总同步为 `meanCAGR 58.06% / minCAGR 18.04%`；`biweekly / weekly` 两条高频族依旧只有 `4 / 4` 个候选，继续没有改写主线的证据。
- 除了导出 `results/live` 依赖所需的 summary replay 之外，这轮没有再补新的 `Path 2` 确认回测；本轮价值主要是把 `results/path2_candidate_pass.json` 从旧的 `117` 候选、过宽 family membership 与 `cap60` robust 口径，同步回当前 `104` 候选、压紧 membership、`cap80` robust 的真实状态。
- 下一轮继续把新增预算优先投向更适配 `since_2020_01` 的中周期高收益原型，不给 `biweekly / weekly` 高频克隆追加预算；若要扩新族，优先考虑月频或中周期原型，而不是继续放大家族内的高频副本。

## 23. 本轮补充（2026-04-27 09:08 CST）

- 本轮同样先按自动化基线规则重查 publish baseline：`git fetch origin` 失败后，确认当前 worktree 已知 `origin/main`（`5a87b29`）仍是本地主工作树 `main`（`39cf735`）的后继，因此独立扫描直接基于该已知远端基线重放。
- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py` 后，当前 `Path 2` 独立候选宇宙恢复到 `117` 个 candidates；五条 family 的规模分别为 `49 / 23 / 16 / 4 / 4`。新增体量再次主要落在 `high_concentration_breakout`，说明当前 shared comparison CSV 的真实状态比上一版 `104` 候选更宽，而不是新的高频 family 扩张。
- 四窗口 tracked winners 继续保持不变，但关键指标已经同步抬升到当前 `as_of=2026-04-27` 口径：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`（`28.48% CAGR / 1.0116 Sharpe / -46.94% MaxDD / 3.89 Turn`）
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`）
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（`58.03% CAGR / 1.1874 Sharpe / -50.82% MaxDD / 5.32 Turn`）
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`145.68% CAGR / 2.1978 Sharpe / -12.20% MaxDD / 5.29 Turn`）
- 当前 tracked `robust_candidate` 也回到了更稳的 `cap60` 版本：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`（`meanCAGR 58.51% / minCAGR 17.57% / meanSharpe 1.1406 / worstMaxDD -66.07%`）。这说明最新 shared payload 的真实状态不是上一条记录里的 `cap80 robust`。
- 下一轮继续把新增预算优先投向更适配 `since_2020_01` 的中周期高收益原型，不给 `biweekly / weekly` 高频克隆追加预算；若要扩新族，优先考虑月频或中周期原型，而不是继续放大家族内的高频副本。

## 24. 本轮补充（2026-04-27 18:09 CST）

- 本轮在主工作树 `main` 上运行 `./.venv/bin/python scripts/path2_candidate_pass.py`，当前 `Path 2` 独立候选宇宙为 `103` 个 candidates；五条 family 规模继续是 `43 / 23 / 16 / 4 / 4`，满足 `100+` family-ranked universe 的最低要求。
- 四窗口 tracked winners 与本轮扫描输出保持为：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`（`27.95% CAGR / 1.0039 Sharpe / -46.94% MaxDD / 3.89 Turn`）
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`）
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（`55.29% CAGR / 1.1612 Sharpe / -50.82% MaxDD / 5.32 Turn`）
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`145.68% CAGR / 2.1978 Sharpe / -12.20% MaxDD / 5.29 Turn`）
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（`meanCAGR 58.06% / minCAGR 18.04%`）
- 关键约束继续不变：`since_2020_01` 上限仍停在 `32.07% CAGR`，距离 `40%+` 目标仍有明显缺口；`biweekly / weekly` 两个高频族各只有 `4` 个候选，且仍没有改写主线。
- 下一轮继续优先新增更适配 `since_2020_01` 的中周期/月频高收益原型，并继续压紧 family membership 口径；不把预算继续投向高频克隆扩张。
