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
