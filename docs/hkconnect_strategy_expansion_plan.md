# 沪港通策略空间扩展计划

## 2026-06-07 16:06 CST 扩展复核结果

本轮扩展线五窗口确认 HK Path4 `hkconnect_path4_quality_liquidity_momentum_monthly_v9`、HK Path6 `hkconnect_path6_large_liquid_core_biweekly_capacity_cost_v9`、HK Path7 `hkconnect_path7_barbell_quality_growth_biweekly_lowturn_dual_sleeve_v9`，HK Path5 只做定义巡检和下一轮候选设计。实际 HK 命令为：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover4_exit40_v4,hkconnect_path4_quality_liquidity_momentum_monthly_v9,hkconnect_path6_large_liquid_core_biweekly_capacity_cost_v9,hkconnect_path7_barbell_quality_growth_biweekly_lowturn_dual_sleeve_v9`。最终 guard 为 `pass`，HK 总候选 `278/278 complete`，Path4/5/6/7 扩展分别为 `12/12`、`4/4`、`11/11`、`10/10` complete。

- Path4 多因子质量/流动性动量：`hkconnect_path4_quality_liquidity_momentum_monthly_v9` 五窗口 CAGR `16.68% / 19.78% / 23.58% / 29.24% / -7.71%`，最大回撤 `-23.19% / -10.74% / -10.74% / -11.43% / -10.34%`，Sharpe `1.07 / 1.18 / 1.34 / 1.36 / -0.17`，换手 `2.74x / 2.56x / 2.61x / 3.31x / 4.11x`。它仍未修复 2026，长中窗弱于 `quality_momentum_monthly_ytd_guard`，不替换 Path4 robust；robust 仍为 `hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5`。下一轮 focus 为 `quality_momentum`，第一条命令建议转回双周流动性动量的质量过滤/低回撤确认：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v10`；若未注册，先注册。
- Path5 回踩续涨：本轮未新增回测；`pullback_continuation` 与 `breakout_retest` 仍存在 2026/2023 或高换手断层。最终 focus 为 `retest_confirmation`，下一轮第一动作仍是重写回踩/突破回踩定义，候选草案保留 `hkconnect_path5_retest_breakout_monthly_trend_reconfirm_v4`，通过定义复核后再跑五窗口。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_biweekly_capacity_cost_v9` 五窗口 CAGR `13.48% / 13.00% / 19.57% / 33.85% / 8.09%`，最大回撤 `-22.68% / -16.06% / -12.06% / -8.22% / -2.53%`，Sharpe `0.89 / 0.84 / 1.13 / 2.06 / 1.01`，换手 `2.14x / 2.08x / 1.88x / 2.09x / 3.80x`。它保留低回撤和正 2026，但长中窗弱于 `large_liquid_core_monthly_smoke`，不替换 robust。下一轮 focus 为 `large_liquid_core`，命令建议：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v10`；若未注册，先注册。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_lowturn_dual_sleeve_v9` 五窗口 CAGR `15.16% / 14.25% / 22.10% / 31.45% / 11.68%`，最大回撤 `-21.35% / -15.41% / -10.85% / -7.15% / -2.39%`，Sharpe `0.95 / 0.89 / 1.23 / 1.88 / 1.37`，换手 `5.18x / 5.01x / 4.86x / 6.08x / 6.77x`。它改善 2026 与低换手，但 2017/2020/2023 仍低于既有 barbell smoke，不替换 robust；tracked robust 仍为 `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。下一轮 focus 为 `barbell_sleeve_structure`，命令建议：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_defensive_lowturn_v10`；若未注册，先注册。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；扩展线未触发 evict。本轮 HK Path4/6/7 rotation 因新增可比候选重置为 `changed/continue`，但 tracked robust 未切换。

## 2026-06-07 04:26 CST 扩展复核结果

本轮扩展线五窗口确认 HK Path4 `hkconnect_path4_quality_momentum_monthly_2026_repair_v8`；HK Path5/6/7 只做定义巡检和下一轮候选设计。实际 HK 命令与 Path1/2 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v23_2023_restore,hkconnect_path4_quality_momentum_monthly_2026_repair_v8`。最终 guard 为 `pass`，HK 总候选 `274/274 complete`，Path4/5/6/7 扩展分别为 `11/11`、`4/4`、`10/10`、`9/9` complete。

- Path4 多因子质量/流动性动量：`hkconnect_path4_quality_momentum_monthly_2026_repair_v8` 五窗口 CAGR `17.65% / 20.29% / 23.54% / 28.54% / -8.96%`，最大回撤 `-21.73% / -10.86% / -10.86% / -11.59% / -10.25%`，Sharpe `1.12 / 1.20 / 1.34 / 1.33 / -0.22`，换手 `2.74x / 2.58x / 2.60x / 3.28x / 3.95x`。它仍未修复 2026，长中窗弱于 `quality_momentum_monthly_ytd_guard`，不替换 Path4 window winner 或 robust；robust 仍为 `hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5`。下一轮 focus 为 `quality_momentum`，第一条命令建议不要继续月频 2026 修复同形，转向质量动量 + 流动性确认：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_liquidity_momentum_monthly_v9`；若未注册，先注册。
- Path5 回踩续涨：本轮未新增回测；`pullback_continuation` 与 `breakout_retest` 仍存在 2026/2023 或高换手断层。最终 focus 为 `pullback_definition`，下一轮第一动作仍是重写回踩/突破回踩定义，候选草案保留 `hkconnect_path5_retest_breakout_monthly_trend_reconfirm_v4`，通过定义复核后再跑五窗口。
- Path6 大市值高流动核心：本轮未新增回测，tracked 仍为 2017/2020/2023 `large_liquid_core_monthly_smoke`、短窗和 robust 由低波/流动性双周线支撑。最终 focus 为 `capacity_cost`，下一轮第一条命令建议确认低容量/低成本的大市值流动核心：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_biweekly_capacity_cost_v9`；若未注册，先注册。
- Path7 杠铃组合：本轮未新增回测，tracked 仍由 biweekly/monthly smoke 与 `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3` 占据。最终 focus 为 `turnover_control`，下一轮第一条命令建议回到低换手双袖结构：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_lowturn_dual_sleeve_v9`；若未注册，先注册。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；`scripts/export_live_platform_data.py` 与 `scripts/generate_public_snapshot.py` 已同步 live/public。扩展线未触发 evict；本轮 HK Path4 rotation 因新增可比候选重置为 changed/continue，但 tracked robust 未切换。

## 2026-06-06 16:17 CST 扩展复核结果

本轮扩展线五窗口确认 HK Path4 `hkconnect_path4_quality_momentum_monthly_cashguard_drawdown_v7`、HK Path6 `hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_mix_v8`、HK Path7 `hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v8`，HK Path5 只做定义巡检和下一轮候选设计。实际命令与 HK Path2/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_equal_elastic_monthly_cost_guard_v18_terminal,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff36_turnover4_exit40_v3,hkconnect_path4_quality_momentum_monthly_cashguard_drawdown_v7,hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_mix_v8,hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v8`。最终 guard 为 `pass`，HK 总候选 `271/271 complete`，Path4/5/6/7 扩展分别为 `10/10`、`4/4`、`10/10`、`9/9` complete。

- Path4 多因子质量/流动性动量：`hkconnect_path4_quality_momentum_monthly_cashguard_drawdown_v7` 五窗口 CAGR `16.47% / 19.26% / 21.70% / 26.84% / -14.35%`，最大回撤 `-22.71% / -11.06% / -11.06% / -10.71% / -10.17%`，Sharpe `1.06 / 1.15 / 1.27 / 1.30 / -0.48`，换手 `2.82x / 2.70x / 2.65x / 3.30x / 3.95x`。它没有修复 2026，且长中窗弱于旧质量动量；最终 guard 标记 Path4 changed/continue，但 tracked robust 仍应保留前序流动性/质量线。下一轮 focus 为 `quality_momentum`，第一条命令建议做月频质量动量的 2026 修复而不是继续现金守门：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_2026_repair_v8`；若未注册，先注册。
- Path5 回踩续涨：本轮未新增回测；`pullback_continuation` 与 `breakout_retest` 仍存在 2026/2023 或高换手断层。最终 focus 为 `retest_confirmation`，下一轮第一动作仍是重写回踩/突破回踩定义；候选草案保留 `hkconnect_path5_retest_breakout_monthly_trend_reconfirm_v4`，通过定义复核后再跑五窗口。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_mix_v8` 五窗口 CAGR `12.95% / 12.13% / 19.99% / 31.90% / 11.57%`，最大回撤 `-22.55% / -16.00% / -12.02% / -8.19% / -2.00%`，Sharpe `0.85 / 0.79 / 1.15 / 1.97 / 1.45`，换手 `2.18x / 2.13x / 1.88x / 2.15x / 3.96x`。它保留低回撤和 2026 正收益，但长中窗仍弱于 `large_liquid_core_monthly_smoke`，不替换 robust。下一轮 focus 为 `large_liquid_core`，命令建议：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_lowturn_v9`；若未注册，先注册。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v8` 五窗口 CAGR `16.11% / 15.01% / 20.11% / 26.60% / 0.22%`，最大回撤 `-18.30% / -14.78% / -11.19% / -9.96% / -5.32%`，Sharpe `0.97 / 0.90 / 1.13 / 1.40 / 0.07`，换手 `8.48x / 8.26x / 8.54x / 11.60x / 10.27x`。它没有替换既有 barbell smoke 或 robust，且 2026 仅小幅正；下一轮 focus 为 `barbell_sleeve_structure`，命令建议改成更低换手的防守双袖：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_defensive_dual_sleeve_v9`；若未注册，先注册。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；扩展线没有 evict。本轮 HK Path4/6/7 因新增比较重置为 `continue`，但未形成需要改写 README/HISTORY 的新 robust 结论。

## 2026-06-06 10:28 CST 扩展复核结果

本轮扩展线五窗口确认 HK Path4 `hkconnect_path4_quality_momentum_monthly_quality_lowturn_v6`、HK Path6 `hkconnect_path6_large_liquid_core_biweekly_lowvol_liquidity_mix_v7`、HK Path7 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`，Path5 只巡检和定义重写设计。实际命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_quality_lowturn_v6,hkconnect_path6_large_liquid_core_biweekly_lowvol_liquidity_mix_v7,hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7`。最终 guard 为 `pass`，HK 总候选 `266/266 complete`，Path4/5/6/7 扩展分别为 `9/9`、`4/4`、`9/9`、`8/8` complete。

- Path4 多因子质量/流动性动量：`hkconnect_path4_quality_momentum_monthly_quality_lowturn_v6` 五窗口 CAGR `18.11% / 21.78% / 26.21% / 31.55% / -9.77%`，最大回撤 `-21.16% / -9.28% / -8.97% / -9.66% / -9.25%`，换手 `2.81x / 2.63x / 2.61x / 3.27x / 4.17x`。它没有修复 2026，也未替换 Path4 window winner 或 robust；tracked robust 仍为 `hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5`。最终 focus 为 `quality_momentum`，下一轮第一条命令建议做月频质量动量的现金/回撤修复，而不是继续 lowturn：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_cashguard_drawdown_v7`；若未注册，先注册。
- Path5 回踩续涨：本轮未新增回测；`pullback_continuation` 与 `breakout_retest` 仍存在 2026/2023 或高换手断层。最终 focus 为 `pullback_definition`，下一轮第一动作仍是重写回踩/突破回踩定义；候选草案保留 `hkconnect_path5_retest_breakout_monthly_trend_reconfirm_v4`，通过定义复核后再跑五窗口。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_biweekly_lowvol_liquidity_mix_v7` 五窗口 CAGR `13.82% / 13.26% / 19.99% / 33.48% / 9.80%`，最大回撤 `-22.29% / -16.72% / -12.14% / -8.11% / -2.19%`，换手 `2.07x / 2.03x / 1.83x / 2.06x / 3.80x`。它切换 HK Path6 `since_2025_01` window winner，但长中窗仍弱于 `large_liquid_core_monthly_smoke`，robust 仍为 `hkconnect_path6_lowvol_liquid_biweekly_smoke`。下一轮 focus 为 `large_liquid_core`，命令建议：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_mix_v8`；若未注册，先注册。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_defensive_core_sleeve_v7` 五窗口 CAGR `15.93% / 15.01% / 23.38% / 33.94% / 11.79%`，最大回撤 `-19.65% / -14.95% / -10.76% / -6.69% / -2.49%`，换手 `5.22x / 5.02x / 4.70x / 5.80x / 7.09x`。它保留低换手和 2026 正收益，但 2017/2020/2023 仍低于既有 barbell smoke，不替换 window winner 或 robust；tracked robust 仍为 `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。下一轮 focus 为 `barbell_sleeve_structure`，命令建议：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v8`；若未注册，先注册。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；扩展线未触发 evict。本轮有 tracked payload 变化的是 HK Path6 `since_2025_01` window winner，HK Path4/7 只新增可比候选不替换 robust。

## 2026-06-06 04:23 CST 扩展复核结果

本轮扩展线五窗口确认 HK Path4 `hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5`、HK Path6 `hkconnect_path6_large_liquid_core_monthly_lowvol_liquidity_mix_v6`、HK Path7 `hkconnect_path7_barbell_quality_growth_biweekly_core_growth_dynamic_v6`，Path5 只巡检和暂停/重写设计。实际命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5,hkconnect_path6_large_liquid_core_monthly_lowvol_liquidity_mix_v6,hkconnect_path7_barbell_quality_growth_biweekly_core_growth_dynamic_v6`。最终 guard 为 `pass`，HK 总候选 `263/263 complete`，Path4/5/6/7 扩展分别为 `8/8`、`4/4`、`8/8`、`7/7` complete。

- Path4 多因子质量/流动性动量：`hkconnect_path4_liquidity_momentum_biweekly_quality_filter_v5` 五窗口 CAGR `14.23% / 12.96% / 8.45% / 48.94% / 18.86%`，最大回撤 `-34.86% / -34.86% / -27.19% / -14.35% / -6.46%`，换手 `7.96x / 7.76x / 8.03x / 9.27x / 8.32x`。它修复 2026 为正且以更好的最差 CAGR 切换为 HK Path4 robust candidate；各窗口 winner 仍由 `quality_momentum_monthly_ytd_guard` 与 `liquidity_momentum_biweekly_ytd_guard_v2` 占据。最终 focus 为 `quality_momentum`，下一轮第一条命令建议回到月频质量动量而不是继续流动性双周：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_cashguard_drawdown_v6`；若未注册，先注册。
- Path5 回踩续涨：本轮未新增回测；`pullback_continuation` 与 `breakout_retest` 仍显示 2026/2023 或高换手断层。最终 focus 为 `pause_or_redesign`，下一轮第一动作不是同形 v4，而是重写回踩/突破回踩定义；候选池仅保留设计草案 `hkconnect_path5_retest_breakout_monthly_trend_reconfirm_v4`，通过定义复核后再跑五窗口。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_monthly_lowvol_liquidity_mix_v6` 五窗口 CAGR `12.46% / 14.18% / 20.36% / 30.03% / 1.70%`，最大回撤 `-18.89% / -15.28% / -6.92% / -3.52% / -4.33%`，换手 `1.20x / 1.25x / 1.12x / 1.63x / 2.61x`。它继续证明低回撤低换手价值，但收益弱于 large-liquid smoke，不替换 winner/robust；下一轮 focus 为 `large_liquid_core`，命令建议：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_quality_liquidity_mix_v7`；若未注册，先注册。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_core_growth_dynamic_v6` 五窗口 CAGR `16.12% / 14.85% / 20.73% / 26.40% / 1.52%`，最大回撤 `-18.42% / -15.11% / -11.13% / -10.25% / -4.85%`，换手 `8.87x / 8.66x / 8.92x / 11.99x / 10.87x`。它让 2026 转正但长中窗仍低于既有 barbell smoke，不替换 robust；下一轮 focus 为 `barbell_sleeve_structure`，命令建议：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v7`；若未注册，先注册。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；`scripts/export_live_platform_data.py` 与 `scripts/generate_public_snapshot.py` 已同步 live/public。扩展线未触发 evict；本轮 HK Path4 robust candidate 切到 v5，HK Path6/7 未切换 winner/robust，Path4/6/7 因新增比较重置为 `continue`。

## 2026-06-05 22:21 CST 扩展复核结果

本轮扩展线五窗口确认 HK Path4 `hkconnect_path4_quality_momentum_monthly_lowvol_drawdown_v4`、HK Path5 `hkconnect_path5_breakout_retest_biweekly_volume_confirm_v3`、HK Path6 `hkconnect_path6_lowvol_liquid_monthly_lowturn_v5`，Path7 只巡检和下一轮设计。实际命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_lowvol_drawdown_v4,hkconnect_path5_breakout_retest_biweekly_volume_confirm_v3,hkconnect_path6_lowvol_liquid_monthly_lowturn_v5`。最终 guard 为 `pass`，HK 总候选 `260/260 complete`，Path4/5/6/7 扩展分别为 `7/7`、`4/4`、`7/7`、`6/6` complete。

- Path4 多因子质量/流动性动量：`hkconnect_path4_quality_momentum_monthly_lowvol_drawdown_v4` 五窗口 CAGR `18.86% / 22.79% / 27.50% / 31.28% / -12.06%`，最大回撤 `-19.46% / -10.66% / -10.66% / -11.40% / -10.95%`，换手 `2.89x / 2.75x / 2.69x / 3.39x / 4.21x`。低波 drawdown 版没有修复 2026，长中窗也低于 `quality_momentum_monthly_ytd_guard`；tracked robust 仍为 `hkconnect_path4_liquidity_momentum_biweekly_ytd_guard_v2`。下一轮 focus 仍是 `quality_momentum`，第一条命令建议转向更直接的 2026 drawdown 修复而不是再降低波：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_cashguard_drawdown_v5`；若未注册，先注册。
- Path5 回踩续涨：`hkconnect_path5_breakout_retest_biweekly_volume_confirm_v3` 五窗口 CAGR `14.27% / 10.44% / 12.66% / 30.25% / -3.36%`，最大回撤 `-25.52% / -25.52% / -18.14% / -14.34% / -6.59%`，换手 `14.64x / 14.30x / 14.94x / 18.19x / 16.42x`。它没有修复 2023 和高换手，但相对旧 retest smoke 把 2026 亏损收窄；`tracked_winners_hkconnect.json` 已把 Path5 `since_2026_01` window winner 与 robust candidate 切到本轮 v3。下一轮 focus 为 `pullback_definition`，第一条动作不是继续同形 v4，而是重写买入定义；若仍要复核，候选应先加入趋势再确认或降低换手。
- Path6 大市值高流动核心：`hkconnect_path6_lowvol_liquid_monthly_lowturn_v5` 五窗口 CAGR `12.10% / 13.89% / 19.48% / 30.60% / 0.02%`，最大回撤 `-20.57% / -14.14% / -7.01% / -3.95% / -4.73%`，换手 `1.20x / 1.26x / 1.13x / 1.65x / 2.54x`。低换手和回撤有效，但收益弱于 `large_liquid_core_monthly_smoke` 与 `lowvol_liquid_biweekly_smoke`，不替换 Path6 winner 或 robust。下一轮 focus 为 `large_liquid_core`，第一条命令建议做大市值核心 + 低波流动性混合权重，而不是继续单纯降换手：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_lowvol_liquidity_mix_v6`；若未注册，先注册。
- Path7 杠铃组合：本轮未新增回测，原因是 10 个 strategy/base id 预算已用于 A股 7 个与 HK Path4/5/6 三个候选。tracked 仍由 biweekly/monthly smoke 与 `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3` 占据，最终 rotation focus 为 `turnover_control`。下一轮第一条命令建议先确认低换手双袖结构：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_growth_dynamic_v6`；若未注册，先注册。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；`scripts/export_live_platform_data.py` 与 `scripts/generate_public_snapshot.py` 已同步 live/public。扩展线未触发 evict；本轮有 tracked payload 变化的是 HK Path5 v3。

## 2026-06-05 10:22 CST 扩展复核结果

本轮扩展线五窗口确认 HK Path4 `hkconnect_path4_quality_momentum_monthly_ytd_guard_v3` 与 HK Path7 `hkconnect_path7_barbell_quality_growth_biweekly_defensive_sleeve_v5`，Path5/6 只注册/设计下一轮候选。实际命令与 HK Path3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_theme_fast_weekly_defensive_exit60_turnover2_cost_guard_v2,hkconnect_path4_quality_momentum_monthly_ytd_guard_v3,hkconnect_path7_barbell_quality_growth_biweekly_defensive_sleeve_v5`。

- Path4 多因子质量/流动性动量：`hkconnect_path4_quality_momentum_monthly_ytd_guard_v3` 五窗口 CAGR `20.24% / 24.58% / 29.41% / 33.25% / -6.11%`，最大回撤 `-18.16% / -10.33% / -10.33% / -10.89% / -10.11%`，换手 `2.96x / 2.84x / 2.78x / 3.49x / 3.99x`。它接近旧 `quality_momentum_monthly_ytd_guard` 的长中窗质量，但 2026 仍为负，没有替换 window winner 或 robust；robust 仍为 `hkconnect_path4_liquidity_momentum_biweekly_ytd_guard_v2`。最新 focus 为 `quality_momentum`，下一轮第一条命令建议不要继续同形 ytd guard，改测质量动量 + 轻低波/2026 drawdown repair：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_lowvol_drawdown_v4`。
- Path5 回踩续涨：本轮未新增回测，只注册/设计 `hkconnect_path5_breakout_retest_biweekly_volume_confirm_v3` 作为下一轮候选。原因是既有 pullback/retest 支线仍存在 2026 或 2023 断层，本轮预算优先给 Path4/7；最终 guard focus 为 `pullback_definition`，下一轮应先确认成交量再确认是否真能修复回踩定义，第一条命令为：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_breakout_retest_biweekly_volume_confirm_v3`。若仍无法修复 2026，应暂停同形回踩线并重写买入定义。
- Path6 大市值高流动核心：本轮未新增回测，只注册/设计 `hkconnect_path6_lowvol_liquid_monthly_lowturn_v5`。当前 tracked 仍由 old smoke 与 `lowvol_liquid_biweekly_smoke` 承担，Path6 下一轮 focus 为 `lowvol_liquid_core`；第一条命令为：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_lowvol_liquid_monthly_lowturn_v5`，验收重点是保留低回撤低换手，同时不能继续牺牲 2017/2020 收益。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_defensive_sleeve_v5` 五窗口 CAGR `15.86% / 14.76% / 20.82% / 25.73% / 3.82%`，最大回撤 `-20.52% / -14.70% / -10.96% / -10.78% / -4.88%`，换手 `9.10x / 8.84x / 9.00x / 12.26x / 11.17x`。它改善防守袖形态但收益低于既有 biweekly smoke 与 `core_sleeve_v3`，不替换 window winner 或 robust。最新 focus 为 `barbell_sleeve_structure`；下一轮第一条命令建议做更明确的核心袖/成长袖动态权重，而不是继续降防守：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_growth_dynamic_v6`。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；本轮 HK Path4/7 rotation 因新增比较重置，但 tracked payload 未切换到新 v3/v5。扩展线未触发 evict。

## 2026-06-05 04:11 CST 扩展复核结果

本轮扩展线新增并五窗口确认 HK Path4 `hkconnect_path4_liquidity_momentum_biweekly_ytd_guard_v2` 与 HK Path6 `hkconnect_path6_large_liquid_core_monthly_lowturn_v4`，Path5/7 仅巡检和下一轮设计。实际命令与 HK Path3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff38_turnover4_exit42_v2,hkconnect_path4_liquidity_momentum_biweekly_ytd_guard_v2,hkconnect_path6_large_liquid_core_monthly_lowturn_v4`。

- Path4 多因子质量/流动性动量：`hkconnect_path4_liquidity_momentum_biweekly_ytd_guard_v2` 五窗口 CAGR `15.26% / 14.07% / 6.76% / 54.89% / 26.77%`，最大回撤 `-34.49% / -34.49% / -32.74% / -15.97% / -6.64%`，换手 `8.75x / 8.62x / 9.10x / 10.68x / 9.98x`。它切换 Path4 `since_2025_01`、`since_2026_01` window winner，并成为 Path4 robust candidate，但 2020/2023 断层和长窗回撤仍深。最新 focus 为 `quality_momentum`；下一轮第一条命令应回到质量动量月频修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_ytd_guard_v3`。
- Path5 回踩续涨：本轮未新增回测；`pullback_continuation` 与 `breakout_retest` 仍显示 2026/2023 断层。最新 focus 为 `retest_confirmation`，下一轮只能先改回踩/突破回踩定义，候选建议 `hkconnect_path5_breakout_retest_biweekly_volume_confirm_v3`，若未注册先注册后再五窗口确认；若仍无法修复 2026，则暂停同形回踩线。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_monthly_lowturn_v4` 五窗口 CAGR `12.52% / 14.35% / 20.48% / 30.03% / 1.69%`，最大回撤 `-18.73% / -15.35% / -6.92% / -3.52% / -4.33%`，换手 `1.19x / 1.24x / 1.12x / 1.63x / 2.61x`。它保留低回撤低换手，但收益弱于现有 large-liquid smoke，不替换 winner 或 robust。最新 focus 为 `large_liquid_core`；下一轮第一条命令建议测试低波+流动性权重而不是继续单纯降换手：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_lowvol_liquid_monthly_lowturn_v5`。
- Path7 杠铃组合：本轮未新增回测；tracked 仍由 biweekly/monthly smoke 与 `core_sleeve_v3` 占据。最新 focus 为 `biweekly_barbell`，下一轮第一条命令建议做更清晰的双袖结构：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_defensive_sleeve_v5`。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；Path4 因 v2 切换 robust/tracked payload，是本轮 HK 扩展线主要增量。本轮扩展线未触发 evict。

## 2026-06-04 16:16 CST 扩展复核结果

本轮扩展线新增并五窗口确认 HK Path5 `hkconnect_path5_pullback_continuation_monthly_ytd_repair_v2`，Path4/6/7 仅巡检和下一轮设计。实际回测命令与 HK Path1/2/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair,hkconnect_path2_equal_elastic_monthly_cost_guard_v17_repair,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit42_coststress_2026_repair,hkconnect_path5_pullback_continuation_monthly_ytd_repair_v2`。

- Path4 多因子质量动量：本轮未新增回测；`quality_momentum_monthly_ytd_guard` 仍占 2017/2020/2023，`liquidity_momentum_biweekly_smoke` 仍占 2025/2026 与 robust。最终 guard 将下一轮 focus 轮到 `liquidity_momentum`；第一条命令改为确认 `hkconnect_path4_liquidity_momentum_biweekly_ytd_guard_v2`，目标是在保留 2025/2026 的同时提升 2020/2023。
- Path5 回踩续涨：`hkconnect_path5_pullback_continuation_monthly_ytd_repair_v2` 五窗口 CAGR `20.35% / 22.03% / 17.38% / 28.01% / -16.61%`，最大回撤 `-22.57% / -12.38% / -12.38% / -12.32% / -12.46%`，换手 `4.08x / 3.97x / 4.20x / 5.28x / 5.12x`。它切换 HK Path5 的 2017/2020 window winner，但 2026 仍深负，robust 仍为 `hkconnect_path5_breakout_retest_biweekly_smoke`。
- Path6 大市值高流动核心：本轮未新增回测；tracked 仍为 2017/2020/2023 `large_liquid_core_monthly_smoke`、2025 `large_liquid_core_biweekly_liquidity_mix_v3`、2026/robust `lowvol_liquid_biweekly_smoke`。下一轮可做低换手 monthly liquidity mix，而不是继续提高短窗弹性。
- Path7 杠铃组合：本轮未新增回测；tracked 仍由首批 biweekly/monthly smoke 与 v3 2026 sleeve 共同占据。下一轮 focus 为 `barbell_sleeve_structure`，优先做更清晰的防守袖/成长袖权重拆分，而不是继续单一 hybrid 权重。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；Path4-7 仍缺独立图表。本轮扩展线未触发 evict。下一轮扩展第一优先级是 Path4 `liquidity_momentum_biweekly_ytd_guard_v2`，第二优先级是 Path5 回踩定义重写后的成交质量确认；若 Path5 仍无法修复 2026，则暂停同形回踩线。

## 2026-06-04 10:16 CST 扩展复核结果

本轮按 HK 扩展线新增 Path6 与 Path7 各 1 个候选，Path4/Path5 仅做巡检和下一轮设计。实际回测命令与 HK Path1/2 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair,hkconnect_path2_equal_elastic_monthly_cost_guard_v17_repair,hkconnect_path6_large_liquid_core_biweekly_liquidity_mix_v3,hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v4`。

- Path4 多因子质量动量：本轮未新增回测；上一轮 v2 仍未修复 2026，下一轮候选设计为 `hkconnect_path4_quality_momentum_monthly_ytd_guard_v3`，目标是保留 `quality_momentum_monthly_ytd_guard` 的 2020/2023 稳定性并降低 2026 负收益。第一条命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_ytd_guard_v3`。
- Path5 回踩续涨：本轮仍不跑同形回踩线。原因是 smoke 的 `pullback_continuation` 与 `breakout_retest` 已显示 2026/2023 断层；下一步必须先改 `pullback_definition`，加入成交质量或趋势再确认，不能直接注册第三个同形 id。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_biweekly_liquidity_mix_v3` 五窗口 CAGR `12.86% / 13.23% / 22.05% / 32.33% / 12.78%`，最大回撤 `-21.65% / -16.03% / -10.96% / -7.77% / -2.55%`。它把 2026 转正并被 `tracked_winners_hkconnect.json` 记录为 HK Path6 的窗口 winner，但长窗收益弱于首批 monthly smoke，robust 未切换。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v4` 五窗口 CAGR `16.12% / 14.56% / 22.77% / 28.66% / 8.73%`，最大回撤 `-19.20% / -14.96% / -10.75% / -10.57% / -5.01%`。它比 v3 更接近“双袖”结构且 2026 为正，但 2017/2020/2023 弱于 Path7 既有 biweekly smoke，不替换 robust。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；Path4-7 仍缺独立图表。本轮扩展线未触发 evict。下一轮第一优先级：先跑 Path4 `ytd_guard_v3`，第二优先级继续 Path6 防守核心的低换手版本；Path5 只做定义重写，不回测。

## 2026-06-04 04:18 CST 扩展复核结果

本轮按 HK Path4/6/7 扩展 focus 各新增 1 个候选，Path5 继续暂停同形回踩线。实际回测命令与 HK Path1 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff28_exit36_v22_drawdown_repair,hkconnect_path4_quality_momentum_monthly_2026_repair_v2,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。

- Path4 多因子质量动量：`hkconnect_path4_quality_momentum_monthly_2026_repair_v2` 五窗口 CAGR `20.34% / 24.14% / 28.80% / 31.84% / -9.40%`，最大回撤 `-16.05% / -10.79% / -10.79% / -11.64% / -10.59%`，换手 `2.98x / 2.85x / 2.76x / 3.47x / 4.20x`。它弱于现有 `quality_momentum_monthly_ytd_guard`，没有替换 Path4 robust。
- Path5 回踩续涨：本轮未跑新增 id。原因是当前 `pullback_continuation` 和 `breakout_retest` 两个 smoke 已显示 2026/2023 断层，最终 guard focus 为 `pullback_definition`；下一轮必须先重写回踩定义或加入成交/趋势再确认，不能继续注册同形 smoke。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2` 五窗口 CAGR `12.90% / 14.60% / 22.41% / 30.79% / 1.82%`，最大回撤 `-17.85% / -14.82% / -6.18% / -2.73% / -3.83%`，换手 `1.23x / 1.26x / 1.11x / 1.70x / 2.67x`。本轮有效变化是 HK Path6 `since_2025_01` winner 切到该 v2；robust 仍是首批 `large_liquid_core_monthly_smoke`。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3` 五窗口 CAGR `14.81% / 13.68% / 21.25% / 30.08% / 21.16%`，最大回撤 `-22.53% / -14.44% / -11.03% / -6.69% / -3.00%`，换手 `5.20x / 4.99x / 4.55x / 5.28x / 6.44x`。它显著改善 2026 与换手，但中长窗弱于现有 barbell smoke，未替换 robust；说明“核心袖”需要更明确的双 sleeve，而不是只靠 hybrid 权重。

最终 guard 为 `pass`，HK Path4 `4/4`、Path5 `2/2`、Path6 `4/4`、Path7 `4/4` complete；Path4/6/7 因新增 tracked 信号均为 `changed=true` 后下一次 guard 记录为 `stagnation_runs=1`。下一轮第一条扩展命令建议优先 Path7 真双 sleeve 结构：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v4`；Path4 下一候选为 `quality_momentum_monthly_ytd_guard_v3`，Path6 下一候选为 `large_liquid_core_biweekly_liquidity_mix_v3`，Path5 只做 pullback definition redesign 记录。

## 2026-06-03 22:20 CST 扩展复核结果

本轮在 Path4-7 扩展线只新增/确认 3 个 smoke 后续候选，Path5 暂停同形回踩线，避免继续复跑弱定义：

- Path4 多因子质量动量：`hkconnect_path4_quality_momentum_monthly_ytd_guard` 五窗口 CAGR `20.87% / 25.92% / 30.81% / 33.19% / -6.68%`，最大回撤 `-15.16% / -11.46% / -9.80% / -10.16% / -9.16%`，换手 `3.03x / 2.92x / 2.81x / 3.65x / 4.14x`。相对首批 monthly smoke，长中窗和 2026 均有改善，是本轮扩展线最有增量的候选；但 2026 仍负，不能直接切 robust。
- Path5 回踩续涨：本轮未跑新增 id。原因是首批 pullback/retest 两个 smoke 都显示 2026 或 2023 断层，继续同形只会扩充弱候选池；下一轮必须先修改回踩定义或加入再确认条件，再注册新 id。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_monthly_ytd_guard` 五窗口 CAGR `14.17% / 16.15% / 25.33% / 29.20% / 9.28%`，最大回撤 `-17.17% / -14.33% / -5.35% / -2.68% / -2.64%`，换手 `1.24x / 1.25x / 1.15x / 1.50x / 2.60x`。它保留低回撤和正 2026，但长窗收益弱于首批 large-liquid smoke，适合作防守基线而不是收益 winner。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_defensive_v2` 五窗口 CAGR `18.39% / 17.54% / 26.42% / 33.29% / 7.11%`，最大回撤 `-20.17% / -13.70% / -10.81% / -11.15% / -5.66%`，换手 `10.40x / 10.10x / 9.97x / 13.00x / 11.63x`。相对首批 biweekly smoke 收益略弱但 2026 正，说明当前单信号近似还不够，需要真正双 sleeve。

`scripts/update_hkconnect_artifacts.py` 已刷新 Path1-3 tracked 与图表；Path4-7 仍只进入 tracked/public/live payload，尚无独立图表。最终 guard 为 `pass`，HK Path4-7 各 `2/2 complete`。下一轮第一条扩展命令建议优先 Path4 ytd guard 的 2026 转正修复，其次 Path6 市值/流动性混合权重；Path5 必须先重定义，不直接新增同形回踩。

## 2026-06-03 smoke 结果

本轮已把扩展计划中的 Path 4-7 先落成 8 个可跑 smoke 候选，并完成五窗口回测：

- Path 4 多因子质量动量：
  - `hkconnect_path4_quality_momentum_monthly_smoke`：CAGR `19.77% / 23.65% / 29.36% / 30.85% / -7.49%`，最大回撤 `-12.26% / -12.26% / -12.26% / -12.26% / -10.22%`，换手 `3.16x / 3.10x / 3.02x / 3.91x / 4.08x`。结论：长中窗稳、回撤浅，2026 观察窗转负，需要做年内保护。
  - `hkconnect_path4_liquidity_momentum_biweekly_smoke`：CAGR `16.83% / 16.03% / 6.40% / 54.48% / 20.13%`，最大回撤 `-33.29% / -33.29% / -33.07% / -15.47% / -7.09%`，换手约 `10x-12x`。结论：短窗强但 2023 断层和回撤过深，不宜作为下一批主线。
- Path 5 回踩续涨：
  - `hkconnect_path5_pullback_continuation_monthly_smoke`：CAGR `20.01% / 20.14% / 19.15% / 23.80% / -17.27%`，最大回撤 `-21.90% / -14.54% / -14.54% / -14.43% / -14.52%`。
  - `hkconnect_path5_breakout_retest_biweekly_smoke`：CAGR `14.23% / 10.67% / 11.01% / 33.82% / -3.74%`，换手约 `16x-19x`。
  - 结论：回踩线首批没有显示增量优势，下一批不继续简单回踩/突破回踩，除非先改掉买入端必须 `recent_1m > 0` 的约束或增加更明确的再确认条件。
- Path 6 大市值高流动性稳健线：
  - `hkconnect_path6_large_liquid_core_monthly_smoke`：CAGR `15.15% / 17.90% / 25.99% / 30.50% / 8.21%`，最大回撤 `-16.62% / -13.54% / -5.32% / -2.97% / -2.49%`，换手 `1.16x / 1.23x / 1.07x / 1.45x / 2.53x`。
  - `hkconnect_path6_lowvol_liquid_biweekly_smoke`：CAGR `14.58% / 14.99% / 23.53% / 29.77% / 20.89%`，最大回撤 `-19.99% / -15.91% / -10.54% / -8.16% / -2.39%`，换手 `2.09x / 2.03x / 1.78x / 2.06x / 4.07x`。
  - 结论：收益不是最强，但回撤、换手、2026 观察窗都明显有防守价值，是下一批最值得扩的方向。
- Path 7 杠铃组合线：
  - `hkconnect_path7_barbell_quality_growth_monthly_smoke`：CAGR `16.68% / 21.15% / 26.07% / 18.11% / -11.76%`，最大回撤 `-18.55% / -15.34% / -10.37% / -10.36% / -10.41%`。
  - `hkconnect_path7_barbell_quality_growth_biweekly_smoke`：CAGR `19.36% / 18.17% / 28.71% / 34.24% / 8.30%`，最大回撤 `-17.64% / -13.24% / -10.79% / -11.16% / -6.08%`，换手约 `11x-14x`。
  - 结论：双周杠铃比月度更有观察价值，但当前实现只是单组合信号近似，还不是严格核心/卫星双 sleeve。

本轮同步后，HK coverage 从 `229/229` 更新为 `237/237`，最终 guard 为 `pass / blocking_missing=0 / warning_missing=0`。`tracked_winners_hkconnect.json` 已包含 Path 4-7 的 strategies payload；现有 `update_hkconnect_artifacts.py` 图表仍只画 Path 1-3，下一步如果扩展线继续推进，需要补 Path 4-7 的独立图表与 track 摘要。

下一批建议：

1. 优先扩 Path 6：`large_liquid_core` 增加 signal weight、市值/流动性混合权重、月度/双周各 2-3 个。
2. 次优扩 Path 4：保留 `quality_momentum_monthly`，做 2026 guard 和轻微容量约束。
3. Path 7 只扩双周版本，并尽快实现真正的核心/卫星双 sleeve；当前单信号近似只能当 smoke。
4. Path 5 暂停同形回踩线，先调整回踩定义或新增再确认规则。
5. Path 8 仍是第二阶段，等南向/AH/股息/估值数据合同确定后再跑。

## 背景

当前沪港通策略探索明显少于 A 股：

- 沪港通对比表约 226 个 `strategy_id`，A 股对比表约 2563 个基础策略。
- 沪港通现有路径分布相对均衡但偏少：Path 1 约 72 个、Path 2 约 77 个、Path 3 约 77 个。
- 现有沪港通信号家族主要集中在 `path1_moderate`、`path1_lowvol`、`path2_breakout`、`path2_theme`、`path2_elastic`。
- 权重方法高度集中在 `equal_weight`，市值、低波、流动性、信号强度类权重还没有形成足够宽的对照组。

这份计划的目标不是继续微调少数参数，而是先扩大沪港通的正交探索空间，让策略候选数、信号家族和权重结构接近 A 股研究平台的广度。

## 原则

1. 第一阶段只用现有沪港通数据字段，不引入新的外部数据依赖。
2. 新路径先作为 tracked-only 实验，不直接进入正式 winner。
3. 每个候选都在 `since_2017_01`、`since_2020_01`、`since_2023_01`、`since_2025_01`、`since_2026_01` 五个窗口观察。
4. 新路径要和现有 Path 1/2/3 保持职责分离，避免只是换名字的参数组合。
5. 每批新增先做小规模 smoke 组，确认结果分布后再批量扩容。

## 现有可复用因子

第一阶段可以优先复用这些已在沪港通回测中可得的字段和衍生分数：

- 趋势：`momentum_12_1`、`momentum_6_1`、`momentum_3_1`、`recent_1m_return`。
- 放量与突破：`amount_surge_ratio`、`breakout_signal`。
- 质量与交易可行性：`liquidity_quality_scores`、成交额、停牌/缺失过滤。
- 防守：`low_vol_scores`、回撤控制、risk-off overlay。
- 规模：`total_mv`、`small_cap_scores`。

这些字段足够先形成 4 到 5 条新的沪港通研究线，不需要等待新增数据源。

## 新路径候选

### Path 4：多因子质量动量线

目标：把“趋势强”从单一动量扩展为趋势、流动性、低波、规模的组合评分。

候选信号家族：

- `hk_quality_momentum`：中期动量 + 流动性质量 + 低波过滤。
- `hk_liquidity_momentum`：动量强度 + 成交活跃度，偏向可交易的大中盘。
- `hk_defensive_momentum`：动量不弱 + 低波 + 风险控制，服务回撤更小的组合。
- `hk_signal_blend`：对 12-1、6-1、3-1 动量和突破做 rank blend。

第一批规模：40 到 60 个候选。

### Path 5：回踩续涨线

目标：寻找中期趋势仍在、短期回踩后有继续上涨可能的港股标的，补足现有突破策略对“回踩买点”的覆盖。

候选信号家族：

- `hk_pullback_continuation`：6-1 或 12-1 动量较强，但 1 个月收益回落。
- `hk_retest_breakout`：前期突破后短期未破坏趋势。
- `hk_volume_confirmed_pullback`：回踩过程中成交质量不恶化。

第一批规模：30 到 45 个候选。

### Path 6：大市值高流动性稳健线

目标：修正现有沪港通组合中过度依赖等权的结构，专门建立大市值、强流动性、低波动的基线。

候选权重和信号：

- `hk_large_liquid_core`：市值和成交额双过滤。
- `hk_lowvol_liquid_core`：低波 + 流动性。
- `hk_hybrid_mv_signal`：市值权重和信号强度权重混合。
- `hk_liquidity_weight`：按流动性质量分配权重，设置单票上限。

第一批规模：30 到 45 个候选。

### Path 7：杠铃组合线

目标：把防守核心和弹性卫星放在同一个组合结构里评估，而不是只比较单一信号。

组合结构：

- 核心仓：低波、高流动性、大市值标的。
- 卫星仓：突破、主题或高成长动量标的。
- 配比组：`70/30`、`60/40`、`50/50`。
- 再平衡：月度为主，双周作为对照。

第一批规模：20 到 30 个候选。

### Path 8：港股专属数据线（第二阶段）

目标：引入真正能体现港股差异的数据，但放在第二阶段，避免第一轮探索被数据接入拖慢。

潜在数据：

- 南向资金持股或成交变化。
- AH 溢价、A+H 映射关系。
- 股息率、估值、盈利修正。
- 行业龙头与港股稀缺资产标签。

进入条件：先定义稳定的数据合同和缺失处理规则，再纳入回测。

## 第一阶段候选预算

建议先新增 120 到 180 个候选，而不是一次性扩到 500 个以上。

| 新路径 | 初始候选数 | 主要作用 |
| --- | ---: | --- |
| Path 4 多因子质量动量 | 40-60 | 扩展信号组合空间 |
| Path 5 回踩续涨 | 30-45 | 补足非突破买点 |
| Path 6 大市值高流动性 | 30-45 | 建立稳健权重基线 |
| Path 7 杠铃组合 | 20-30 | 评估组合结构 |

第一批可以先注册 20 到 30 个 smoke 候选，跑完五个窗口后再继续扩容。

## 代码接入建议

后续如果开始实现，建议按这个顺序推进：

1. 在 `build_hk_signal_scores` 中增加新信号家族，先复用现有字段。
2. 在 `build_hk_base_weights` 中增加 `liquidity_weight`、`low_vol_inverse`、`signal_score_weight`、`hybrid_mv_signal` 等权重方法。
3. 增加 `HK_PATH4_VARIANTS`、`HK_PATH5_VARIANTS`、`HK_PATH6_VARIANTS`、`HK_PATH7_VARIANTS`，或抽一个简单 helper 生成候选。
4. 新路径稳定后再同步更新 `scripts/update_hkconnect_artifacts.py`、`scripts/export_live_platform_data.py`、`scripts/generate_public_snapshot.py`。
5. 在研究 guard 中增加每条新路径的候选上限，避免单一路径快速膨胀。

## 判断标准

保留一条新路径需要满足至少一个条件：

- 在某个关键窗口明显优于现有沪港通 winner。
- 虽然收益不是最强，但回撤、换手、稳定性明显更好。
- 与现有 Path 1/2/3 的持仓重合度低，提供新的组合角色。

如果连续三批候选都没有改善，也没有独特组合价值，就归档该路径，避免长期占用迭代预算。

## 本轮执行计划（2026-06-08 06:05 CST）

- 上一轮候选/结果摘要：上一轮 HK Path4/6/7 扩展线仍有同步空间，Path5 继续处于暂停/重设计；本轮按配额新增或确认 Path4、Path6、Path7 各 1 个候选，Path5 只巡检不追加参数。
- HK Path4 本轮候选：`hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v10`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v10`。五窗口 CAGR `12.56% / 11.92% / 8.49% / 51.63% / 12.75%`，最大回撤最差 `-38.05%`；最终 guard 标记 `hkconnect_path4 changed=true`，robust candidate 切到该 v10，但它仍是高回撤/中等收益的 tracked-only 扩展线。
- HK Path5 本轮候选：无新增；`hkconnect_path5_breakout_retest_biweekly_volume_confirm_v3` 仍为 robust 观察，`since_2026_01` 为负。未回测原因：guard focus 为 `pause_or_redesign`，Path5 需要重设回踩/突破确认结构，不继续堆参数。下一轮先设计 `hkconnect_path5_pullback_continuation_monthly_quality_retest_v4`，再决定是否执行。
- HK Path6 本轮候选：`hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v10`。五窗口 CAGR `11.41% / 13.06% / 18.43% / 32.09% / 0.98%`，最大回撤 `-21.65% / -12.60% / -6.43% / -4.18% / -4.75%`，换手 `1.28x-2.52x`；最终 guard 标记 `hkconnect_path6 changed=true`，但 robust candidate 仍由低波/流动性双周 smoke 线占据，v10 作为低换手月频对照保留。
- HK Path7 本轮候选：`hkconnect_path7_barbell_quality_growth_biweekly_core_defensive_lowturn_v10`。五窗口 CAGR `14.18% / 13.02% / 19.99% / 30.80% / 9.57%`，最差回撤 `-21.53%`，换手 `4.78x-6.53x`；最终 guard 标记 `hkconnect_path7 changed=true`，但 robust candidate 仍为 `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`，v10 只作为低换手防守杠铃对照。
- HK 扩展线收尾：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 已同步 285 个 HK candidates，最终 guard 为 `pass`，Path4/5/6/7 coverage 分别为 `13/13`、`4/4`、`12/12`、`11/11`。
- 下一轮 focus：Path4 `quality_momentum` 第一命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_lowvol_drawdown_v11`；Path5 最终 guard 已转为 `pullback_definition`，先重设计 `hkconnect_path5_pullback_continuation_monthly_quality_retest_v4`；Path6 第一命令为 `--only-strategy-ids hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_lowturn_v11`；Path7 第一命令为 `--only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_defensive_dynamic_v11`。

## 本轮执行计划（2026-06-08 12:13 CST）

- 上一轮候选/结果摘要：上一轮 HK Path4/6/7 留下 v11 首命令，Path5 留下 `pullback_continuation_monthly_quality_retest_v4` 重设计；本轮按扩展线配额确认 Path5/6/7，Path4 只巡检并保留下一轮候选。
- HK Path4 本轮：未新增回测。最终 guard 给出 `hkconnect_path4 -> liquidity_momentum`，当前 robust 仍为 `hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v10`；未回测原因是本轮 HK 预算优先给 Path1/2/3/5/6/7 六个新增策略。下一轮首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair`。
- HK Path5 本轮候选：`hkconnect_path5_pullback_continuation_monthly_quality_retest_v4`，五窗口 CAGR `17.80% / 19.27% / 16.65% / 28.65% / -10.51%`，最大回撤 `-22.80% / -11.80% / -11.80% / -12.08% / -12.10%`，换手 `3.83x / 3.71x / 3.87x / 4.89x / 4.81x`。未改写 robust，下一轮继续重设回踩定义。
- HK Path6 本轮候选：`hkconnect_path6_large_liquid_core_biweekly_quality_liquidity_lowturn_v11`，五窗口 CAGR `13.50% / 12.99% / 19.51% / 32.55% / 8.03%`，最大回撤 `-22.52% / -15.90% / -12.38% / -8.01% / -2.60%`，换手 `2.14x / 2.08x / 1.85x / 2.07x / 3.66x`。它改善短窗和低换手属性，但 robust 仍为旧 lowvol/liquid smoke 线。
- HK Path7 本轮候选：`hkconnect_path7_barbell_quality_growth_biweekly_core_defensive_dynamic_v11`，五窗口 CAGR `13.58% / 12.37% / 18.90% / 29.59% / 6.35%`，最大回撤 `-21.92% / -15.94% / -11.24% / -7.41% / -3.38%`，换手 `4.99x / 4.82x / 4.63x / 6.00x / 6.63x`。未改写 robust，但作为防守杠铃对照保留。
- HK 扩展线收尾：本轮未跑 HK `tracked_active`，因为 A股 `refresh_active` 同步耗时显著超预期；已运行 `scripts/update_hkconnect_artifacts.py` 同步 comparison 和图表。下一轮第一条同步命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。

## 本轮执行计划（2026-06-08 17:37 CST）

- 上一轮候选/结果摘要：上一轮 HK Path4 留下 `liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair`，Path5/6/7 继续要求重设回踩、低波流动核心和双周杠铃结构。
- HK Path4 本轮候选：`hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair`。五窗口 CAGR `13.15% / 12.81% / 10.19% / 47.28% / 10.64%`，最差回撤 `-37.63%`，换手 `6.44x-8.28x`；未优于 v10 robust。
- HK Path5 本轮：无新增回测；最终 focus 为 `pause_or_redesign`。下一步先暂停 `pullback_continuation` 小参数堆叠，改设计 `hkconnect_path5_breakout_retest_biweekly_quality_confirm_v5`，要求先重定义突破后回踩确认再回测。
- HK Path6 本轮：无新增回测；最终 focus 为 `capacity_cost`。下一候选设计 `hkconnect_path6_lowvol_liquid_core_monthly_quality_lowturn_v12_cost_cap`，用于检查低波流动核心在容量/成本约束下是否仍能改善 2026。
- HK Path7 本轮：无新增回测；最终 focus 为 `turnover_control`。下一候选设计 `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v12`，目标是压低 v11 防守杠铃换手。
- HK Path4 下一轮 focus：最终 guard 给出 `quality_momentum` 且状态为 `continue`。下一候选建议 `hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter`，用于检查 v11 的低回撤修复是否能转为 robust 改善。
- HK 扩展线收尾：已运行 `scripts/update_hkconnect_artifacts.py`；HK `tracked_active` 五窗口同步虽耗时较长但最终完成，覆盖当前活跃 HK 观察集合。下一轮优先按最终 guard focus 推进 Path4/5/6/7 新候选，若 comparison 再漂移再补 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。

## 本轮执行计划（2026-06-08 23:27 CST）

- 上一轮候选/结果摘要：上一轮 Path4 v11 未优于 v10，Path5/6/7 留下重设候选；本轮执行 Path5 v5，Path4/6/7 做巡检和下一轮设计。
- HK Path4 本轮：未新增回测。最终 guard 给出 `hkconnect_path4 -> liquidity_momentum`，当前 robust 仍为旧 liquidity/quality lowdraw 线；下一候选设计 `hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter`，首条命令为 `.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter`。
- HK Path5 本轮候选：`hkconnect_path5_breakout_retest_biweekly_quality_confirm_v5`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path5_breakout_retest_biweekly_quality_confirm_v5`。五窗口 CAGR `14.64% / 11.57% / 14.41% / 33.22% / -7.26%`，最差回撤 `-23.30%`，换手 `13.47x-17.88x`；未改写 robust。
- HK Path6 本轮：未新增回测。最终 guard 给出 `hkconnect_path6 -> lowvol_liquid_core`，下一候选设计 `hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v12_cost_cap`，首条命令为 `.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v12_cost_cap`。
- HK Path7 本轮：未新增回测。最终 guard 给出 `hkconnect_path7 -> biweekly_barbell`，下一候选设计 `hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v12`，首条命令为 `.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v12`。
- HK 扩展线收尾：已运行 `scripts/update_hkconnect_artifacts.py`，但本轮没有额外跑 HK `tracked_active`，原因是 A股 `refresh_active` 全五窗口同步耗时显著超预期；下一轮若 comparison 漂移，先补 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。

## 本轮执行计划（2026-06-09 04:20 CST）

- 上一轮候选/结果摘要：上一轮 Path4/6/7 留下 v12 设计，Path5 v5 未改写 robust；本轮执行 Path4、Path6、Path7 各 1 个候选，Path5 做巡检和下一轮设计。HK 新增命令与 Path1/2/3 合并为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <six_hk_new_ids>`。
- HK Path4 本轮候选：`hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter`。五窗口 CAGR `12.95% / 12.80% / 9.35% / 44.84% / 11.65%`，最大回撤最差 `-36.26%`，换手 `6.37x-8.25x`；未优于当前 Path4 robust `hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v11_turnover_repair`，最终 guard 状态因 HK 扩展签名同步转为 `changed=true / continue`，下一轮 focus 为 `quality_momentum`。
- HK Path5 本轮：无新增回测；上一轮 `hkconnect_path5_breakout_retest_biweekly_quality_confirm_v5` 仍未改写 robust，最终 focus 为 `retest_confirmation`。下一候选设计 `hkconnect_path5_breakout_retest_biweekly_quality_confirm_v6_retest_width`，先调整回踩宽度和确认周期，不继续无约束提高突破强度。
- HK Path6 本轮候选：`hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v12_cost_cap`。五窗口 CAGR `11.05% / 12.78% / 17.88% / 31.53% / 0.63%`，最大回撤 `-22.25% / -11.39% / -6.81% / -4.65% / -5.32%`，换手 `1.29x-2.45x`；低换手核心属性成立，但未改写 robust。最终 guard 状态为 `changed=true / continue`，下一轮 focus 为 `large_liquid_core`。
- HK Path7 本轮候选：`hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v12`。五窗口 CAGR `13.42% / 12.15% / 18.84% / 30.15% / 2.46%`，最大回撤 `-21.07% / -15.99% / -11.26% / -7.61% / -4.30%`，换手 `4.62x-6.59x`；未改写 robust，但继续作为低换手杠铃对照。最终 guard 状态为 `changed=true / continue`，下一轮 focus 为 `barbell_sleeve_structure`。
- HK 扩展线收尾：本轮补跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `scripts/update_hkconnect_artifacts.py`。最终 guard 显示 HK 全候选 `297/297 complete`，Path4/5/6/7 coverage 分别为 `14/14`、`6/6`、`13/13`、`12/12`。
- 下一轮 focus：Path4 `quality_momentum` 第一命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_lowdraw_v13_reconfirm`；Path5 `retest_confirmation` 首命令为 `--only-strategy-ids hkconnect_path5_breakout_retest_biweekly_quality_confirm_v6_retest_width`；Path6 `large_liquid_core` 首命令为 `--only-strategy-ids hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v13_core_reconfirm`；Path7 `barbell_sleeve_structure` 首命令为 `--only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v13_sleeve_rebalance`。
