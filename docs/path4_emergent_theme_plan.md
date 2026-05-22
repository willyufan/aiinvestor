# Path 4 强主题涌现路径

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

- `research_iteration_guard.py` 会把 12 个强主题候选作为独立 coverage scope 检查，要求覆盖 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`。
- `path2_candidate_pass.py` 会把这些候选归入独立 family `emergent_theme_discovery`，用于和 Path 2 其他探索族横向比较。
- 第一阶段不直接改写 official winner；等五窗口完整后，再决定是否独立展示为 Path 4 winner 或并入现有 winner 体系。

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
