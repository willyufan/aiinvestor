# 沪港通 Path 2 研究计划

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass`，上一轮 `equal_elastic_monthly_cost_guard_v3` 短窗强但 2023 与长窗回撤弱；本轮按预算留下的第一候选补 `inverse_elastic_monthly_cost_guard_v3`，继续只作为 HK Path 2 高收益月频观察。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v3`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `inverse_elastic_monthly_cost_guard_v3` 五窗口 CAGR 为 `19.40% / 21.10% / 15.10% / 76.40% / 57.70%`，最大回撤 `-33.90% / -33.90% / -35.60% / -8.20% / -5.40%`，换手 `5.61x / 5.47x / 6.05x / 6.31x / 6.83x`；与等权 v3 几乎同形，2025/2026 强但 2023 和长窗回撤不达 robust 标准。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`。`biweekly_breakout` 因连续 `-50%` 级长窗回撤继续作为暂停/归档观察，不做普通阈值微调。
- 收尾 guard 给出 `biweekly_breakout`，但该 focus 已无法映射到高质量候选；下一轮 focus -> candidates 池先记录暂停双周 breakout，再转向主题月频修复。第一条命令建议测试 `hkconnect_path2_theme_monthly_cost_control_lowturn` 或 `hkconnect_path2_theme_monthly_cost_control_reconfirm`, 五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_theme_monthly_repair_id>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass`，上一轮 `breakout_cost_guard_biweekly_risk50` 继续出现 `-50%` 级长窗回撤；本轮按 `elasticity_cost_control` 回到月频高弹性成本约束。受本轮总实验预算限制，只跑等权 `cost_guard_v3`，把 inverse 版本留作下一轮未跑候选。
- 本轮新增并五窗口确认：`hkconnect_path2_equal_elastic_monthly_cost_guard_v3`。实际命令见 HK Path 1 本轮合并命令。
- `equal_elastic_monthly_cost_guard_v3` 五窗口 CAGR 为 `19.36% / 21.13% / 15.13% / 76.36% / 57.75%`，最大回撤 `-33.94% / -33.94% / -35.61% / -8.21% / -5.41%`，换手 `5.61x / 5.48x / 6.05x / 6.31x / 6.83x`；短窗继续强，但 2023 和长窗回撤不达 robust 标准，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；biweekly breakout 支线继续记为暂停/归档观察，不再做普通阈值微调。
- 下一轮 focus -> candidates 池：第一条命令建议补本轮预算留下的 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v3`，若其 2023 仍弱，则转向 `theme_monthly_cost_control` 的低换手/更高 2023 收益修复，五窗口 `--only-strategy-ids <hk_path2_inverse_cost_v3_id>`。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 指向 `biweekly_breakout`；上一轮计划要求判断双周突破是否应归档，本轮补 `risk50` 成本守门版本。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_risk50`。实际命令见 HK Path 1 本轮合并命令。
- `breakout_cost_guard_biweekly_risk50` 五窗口 CAGR 为 `4.90% / 1.35% / -0.94% / 36.68% / -16.67%`，最大回撤 `-54.92% / -54.92% / -40.48% / -16.72% / -9.39%`，换手 `16.92x / 16.89x / 17.79x / 20.28x / 20.28x`；风险阈值没有修复长窗深回撤和 2026 负收益，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`。
- 候选池未触发 cap evict，但 `biweekly_breakout` 支线已连续出现 `-50%` 级长窗回撤；下一轮若仍要推进，第一步应把该支线标记为暂停/归档，不再继续加普通阈值邻域。
- 收尾 guard 后 HK Path 2 rotation 切到 `elasticity_cost_control`。下一轮第一条命令建议回到月频高弹性成本约束，先实现 `hkconnect_path2_equal_elastic_monthly_cost_guard_v3` 与 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v3`，五窗口 `--only-strategy-ids <hk_path2_elasticity_cost_v3_ids>`；双周 breakout 支线先按本轮失败记录暂停，不继续风险阈值微调。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮等权弹性现金防守 v3 短窗强但 2023/长窗回撤弱，本轮按 `biweekly_breakout`/高收益月频衔接，补跑上一轮预算留下的反向弹性现金防守 v3。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cashguard_v3`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_inverse_elastic_monthly_cashguard_v3`。
- 该候选五窗口 CAGR 为 `16.92% / 18.47% / 13.06% / 76.36% / 57.75%`，最大回撤 `-36.39% / -36.39% / -35.57% / -8.21% / -5.41%`，换手 `5.43x / 5.29x / 5.99x / 6.31x / 6.83x`；与等权 v3 几乎同形，2025/2026 强但 2023 和长窗回撤仍不达 robust 标准。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；未触发 HK explore cap evict。
- 下一轮 focus -> candidates 池：不要继续复制 elastic v3；若 rotation 仍给 `biweekly_breakout`，第一条命令建议实现 `hkconnect_path2_breakout_cost_guard_biweekly_risk50`，用五窗口 `--only-strategy-ids <hk_path2_biweekly_risk_id>` 判断双周突破是否应归档。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `inverse_elastic_monthly_cost_guard_v2` 仍是短窗强、2023/长窗回撤弱，本轮按 `high_return_monthly` 先补等权弹性现金防守 v3，并把反向 v3 留作下一轮预算内第一条命令。
- 本轮新增并五窗口确认：`hkconnect_path2_equal_elastic_monthly_cashguard_v3`。实际命令与 HK Path 1/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45,hkconnect_path2_equal_elastic_monthly_cashguard_v3,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover7_exit45`。
- `equal_elastic_monthly_cashguard_v3` 五窗口 CAGR 为 `16.92% / 18.47% / 13.06% / 76.36% / 57.75%`，最大回撤 `-36.39% / -36.39% / -35.57% / -8.21% / -5.41%`，换手 `5.43x / 5.29x / 5.99x / 6.31x / 6.83x`；2025/2026 弹性仍强，但 2017/2020/2023 收益和回撤均弱于 `theme_monthly_cost_control`，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`。
- 收尾 guard 为 `pass`，HK all candidates `79/79 complete`；本轮未触发 HK explore cap evict。最终 rotation 为 `stagnation_runs=20 / high_return_monthly / rotate`。下一轮第一条命令建议实现并五窗口确认 `hkconnect_path2_inverse_elastic_monthly_cashguard_v3`，继续检查高收益月频在 2023 不塌的现金防守形态。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `theme_monthly_cost_control_v2` 收益低于旧 robust，本轮按 `elasticity_cost_control` 先补 `inverse_elastic_monthly_cost_guard_v2`，不裸跑 HK 全量。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v2`。实际命令见 HK Path 1 本轮合并命令。
- `inverse_elastic_monthly_cost_guard_v2` 五窗口 CAGR 为 `19.95% / 22.22% / 15.40% / 76.32% / 57.75%`，最大回撤 `-34.21% / -34.21% / -36.02% / -8.23% / -5.41%`，换手 `5.71x / 5.57x / 6.10x / 6.31x / 6.83x`；2025/2026 弹性强，但 2023 收益和长窗回撤不达 robust 标准，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86`。
- 收尾 guard 为 `pass`，HK all candidates `76/76 complete`；最终 rotation 为 `stagnation_runs=17 / elasticity_cost_control / rotate`。下一轮 focus -> candidates 池继续高弹性成本约束，但要以 2023 不塌为前提，第一条命令建议实现 `hkconnect_path2_equal_elastic_monthly_cashguard_v3` 与 `hkconnect_path2_inverse_elastic_monthly_cashguard_v3`，五窗口 `--only-strategy-ids <hk_path2_elasticity_ids>` 增量确认。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `equal_elastic_monthly_cost_guard_v2` 未晋级，计划提示转向 `theme_monthly_cost_control_v2`。本轮只补这个主题月频成本控制版本，不裸跑 HK 全量。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_cost_control_v2`。实际命令与 HK Path 1/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard,hkconnect_path2_theme_monthly_cost_control_v2,hkconnect_path3_stable_weekly_equal_buffered_cashguard_turnover9`。
- `theme_monthly_cost_control_v2` 五窗口 CAGR 为 `19.02% / 23.67% / 21.72% / 54.61% / 41.26%`，最大回撤 `-24.12% / -16.98% / -12.58% / -10.72% / -10.78%`，换手 `5.27x / 5.00x / 5.26x / 5.69x / 5.09x`；回撤可控且 2026 为正，但收益低于现有 `theme_monthly_cost_control`，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86`。
- Guard 显示 HK all candidates `73/73 complete`，本轮未触发 evict；最终 rotation 为 `stagnation_runs=14 / biweekly_breakout / rotate`。下一轮 focus -> candidates 池必须重新映射到双周突破的失败修复，第一条命令建议实现 `hkconnect_path2_breakout_cost_guard_biweekly_risk50`，五窗口 `--only-strategy-ids <hk_path2_biweekly_breakout_id>` 增量确认；若仍出现 `-50%` 级回撤，应归档该双周 breakout 支线。

## 本轮执行计划（2026-05-20 13:58 CST）

- 上一轮 focus 指向 `high_return_monthly`，本轮从失败的双周突破回到高弹性月频成本控制，只新增一个等权弹性版本，不裸跑 HK 全量。
- 本轮新增并五窗口确认：`hkconnect_path2_equal_elastic_monthly_cost_guard_v2`。实际命令与 HK Path 1/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard,hkconnect_path2_equal_elastic_monthly_cost_guard_v2,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8`。
- `equal_elastic_monthly_cost_guard_v2` 五窗口 CAGR 为 `20.23% / 22.66% / 15.57% / 76.32% / 57.75%`，最大回撤 `-34.42% / -34.42% / -36.24% / -8.23% / -5.41%`，换手 `5.75x / 5.62x / 6.13x / 6.31x / 6.83x`；2025/2026 弹性仍在，但 2023 收益和长窗回撤都不如 `theme_monthly_cost_control`，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86`。
- Guard 显示 HK all candidates `70/70 complete`，本轮未触发 evict；最终 rotation 为 `stagnation_runs=11 / high_return_monthly / rotate`。下一轮 focus -> candidates 池要把高收益月频和主题成本控制结合，第一条命令建议实现 `hkconnect_path2_theme_monthly_cost_control_v2` 或 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v2` 后用五窗口 `--only-strategy-ids <hk_path2_monthly_id>` 增量确认。

## 本轮执行计划（2026-05-20 05:20 CST）

- 上一轮提示为双周突破先压回撤/换手；本轮把 `hkconnect_path2_breakout_cost_guard_biweekly` 的卖出阈值放宽到 `exit35`，测试能否改善长窗回撤与 2026 负收益，继续不裸跑全量 HK。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_exit35`。实际命令与 HK Path 1/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_cashguard,hkconnect_path2_breakout_cost_guard_biweekly_exit35,hkconnect_path3_theme_fast_weekly_defensive_turnover18`。
- `exit35` 五窗口 CAGR 为 `4.59% / 1.00% / -0.82% / 36.68% / -16.67%`，最大回撤 `-55.11% / -55.11% / -40.48% / -16.72% / -9.39%`，换手 `16.29x-20.28x`；只比上一轮成本防守略微改善，长窗回撤仍不可接受，记为失败对照。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86`。
- HK candidate_count 为 `67`，未触发 evict；收尾 guard 的 HK Path 2 rotation 为 `stagnation_runs=8 / elasticity_cost_control / rotate`。下一轮 focus -> candidates 池从失败的双周突破转向高弹性月频的成本/回撤约束。
- 下一轮第一条命令建议先实现 `hkconnect_path2_equal_elastic_monthly_cost_guard_v2` 与 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v2`，再用 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_ids>` 补跑。

## 本轮执行计划（2026-05-19 23:14 CST）

- 上一轮 `hkconnect_path2_theme_monthly_cost_control` 成为 2017/2020 winner 与 robust；本轮按最终 rotation 的 `biweekly_breakout` 补一个双周突破成本防守对照，不裸跑全量 HK。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly`。实际命令与 HK Path 1/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_cost_guard,hkconnect_path2_breakout_cost_guard_biweekly,hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。
- 新双周突破成本防守五窗口 CAGR 为 `4.10% / 0.38% / -1.05% / 36.56% / -16.67%`，最大回撤仍有 `-55.96% / -55.96% / -40.51% / -16.80% / -9.39%`，换手 `16x-20x`；只保留为失败对照，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 `theme_monthly`，2025 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86`。
- HK candidate_count 为 `64/64 complete`，本轮未触发 evict；下一轮 focus -> candidates 池仍按 `biweekly_breakout`，但必须先压回撤/换手。建议先实现 `hkconnect_path2_breakout_cost_guard_biweekly_exit35` 与 `hkconnect_path2_breakout_cost_guard_biweekly_risk50`，第一条命令继续用五窗口 `--only-strategy-ids`。

## 本轮执行计划（2026-05-19 17:26 CST）

- 本轮新增并用 `--only-strategy-ids` 五窗口补跑 3 个成本/回撤控制候选：`hkconnect_path2_equal_elastic_monthly_defensive`、`hkconnect_path2_inverse_elastic_monthly_defensive`、`hkconnect_path2_theme_monthly_cost_control`；没有裸跑全量 HK。
- `theme_monthly_cost_control` 成为 2017/2020 window winner 与 robust：2017 `22.42% CAGR / -25.34% MaxDD / 1.01 Sharpe / 5.87 Turn`，2020 `29.86% / -19.10% / 1.17 / 5.65`，2023 `28.94% / -14.06% / 1.33 / 5.73`，2025 `68.62% / -8.42% / 2.20 / 6.21`，2026 `67.73% / -8.40% / 1.36 / 5.51`。
- `equal_elastic_monthly_defensive` 与 `inverse_elastic_monthly_defensive` 在 2025/2026 均强（`84.64% / 69.49% CAGR`），但 2017/2020/2023 回撤仍到 `-36%~-38%`，只适合作为高弹性成本控制观察。
- HK Path 2 tracked winners 更新为：2017/2020 `hkconnect_path2_theme_monthly_cost_control`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`；robust 切为 `hkconnect_path2_theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 为 `stagnation_runs=1 / high_return_monthly / continue`；下一轮优先在 `theme_monthly_cost_control` 上做更低换手或 2023 收益修复，而不是继续扩高回撤弹性。

## 本轮执行计划（2026-05-19 11:12 CST）

- 本轮随 `tracked_active` 增量刷新月频、双周、高集中突破、高弹性与主题候选；Path 2 继续不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 当前窗口指标为：2017 `21.84% CAGR / -36.76% MaxDD / 0.95 Sharpe / 6.80 Turn`，2020 `25.82% / -36.76% / 1.01 / 6.64`，2023 `31.22% / -16.07% / 1.41 / 6.02`，2025 `97.73% / -7.23% / 2.35 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 为 `stagnation_runs=34 / elasticity_cost_control / rotate`；下一轮优先控制高弹性路线的回撤、换手和交易成本，不继续只扩双周突破强度。

## 本轮执行计划（2026-05-19 05:29 CST）

- 本轮按 `biweekly_breakout` 轮换方向新增并用 `--only-strategy-ids` 增量补跑 `hkconnect_path2_breakout_buffered_biweekly`、`hkconnect_path2_breakout_defensive_biweekly`、`hkconnect_path2_breakout_balanced_biweekly`，没有裸跑全量 HK。
- 三个新双周突破候选在 2025 窗口仍有 `31.33%~35.76% CAGR`，但 2017/2020/2023 长窗收益很弱且回撤约 `-59%~-61%`，2026 短窗也为负，未达到替换月频锚点的质量。
- 其中 `breakout_buffered_biweekly` 五窗口为：2017 `4.51% CAGR / -59.60% MaxDD / 0.31 Sharpe / 17.88 Turn`，2020 `0.21% / -59.60% / 0.19 / 17.84`，2023 `-1.68% / -42.27% / 0.16 / 18.42`，2025 `35.76% / -18.48% / 1.08 / 20.51`，2026 `-17.40%`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 仍为 `stagnation_runs=32 / recommended_focus=biweekly_breakout / rotate`；下一轮不要继续只扩突破强度，优先做回撤/换手约束或回到高收益月频压测。

## 本轮执行计划（2026-05-18 23:13 CST）

- 本轮随 `tracked_active` 增量回测单独刷新月频、双周、高集中突破、高弹性与主题候选；Path 2 仍不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 当前窗口指标为：2017 `21.84% CAGR / -36.76% MaxDD / 0.95 Sharpe / 6.80 Turn`，2020 `25.82% / -36.76% / 1.01 / 6.64`，2023 `31.22% / -16.07% / 1.41 / 6.02`，2025 `97.73% / -7.23% / 2.35 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 为 `stagnation_runs=30 / recommended_focus=biweekly_breakout / rotate`；下一轮优先复核双周突破候选在回撤、换手和成本约束下是否优于月频锚点。

## 本轮执行计划（2026-05-18 20:34 CST）

- 本轮随 `tracked_active` 增量回测单独刷新月频、双周、高集中突破、高弹性与主题候选；Path 2 仍不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 当前窗口指标为：2017 `21.84% CAGR / -36.76% MaxDD / 0.947 Sharpe`，2020 `25.82% / -36.76% / 1.005`，2023 `31.22% / -16.07% / 1.413`，2025 `97.73% / -7.23% / 2.348`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 为 `stagnation_runs=28 / recommended_focus=high_return_monthly / rotate`；下一轮优先比较高收益月频候选在回撤、换手和成本约束后的存活性。

## 本轮执行计划（2026-05-18 11:11 CST）

- 本轮随 `tracked_active` 增量回测单独刷新月频、双周、高集中突破、高弹性与主题候选；Path 2 仍不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 为 `stagnation_runs=23 / recommended_focus=biweekly_breakout / rotate`；下一轮优先比较双周突破候选的回撤、换手和成本约束。

## 本轮执行计划（2026-05-18 05:53 CST）

- 本轮随 `tracked_active` 增量回测单独刷新月频、双周、高集中突破、高弹性与主题候选；Path 2 不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 为 `stagnation_runs=20 / recommended_focus=high_return_monthly / rotate`；下一轮优先比较高收益月频候选在回撤、换手和成本约束后的存活性。

## 本轮执行计划（2026-05-17 23:12 CST）

- 本轮随 `tracked_active` 增量回测单独刷新月频、双周、高集中突破、高弹性与主题候选；Path 2 不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`（`21.84% CAGR / -36.76% MaxDD / 0.95 Sharpe / 6.80 Turn`），2020 `hkconnect_path2_inverse_elastic_monthly`（`25.82% / -36.76% / 1.01 / 6.64`）。
- 2023 winner 仍为 `hkconnect_path2_theme_monthly`（`31.22% CAGR / -16.07% MaxDD / 1.41 Sharpe / 6.02 Turn`），2025 winner 仍为 `hkconnect_path2_breakout_concentrated_monthly`（`97.73% / -7.23% / 2.35 / 9.05`）。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 为 `stagnation_runs=18 / recommended_focus=high_return_monthly / rotate`；下一轮优先比较高收益月频候选在回撤、换手和成本约束后的存活性。

## 本轮执行计划（2026-05-17 17:25 CST）

- 本轮随 `tracked_active` 增量回测单独刷新月频、双周、高集中突破、高弹性与主题候选；Path 2 不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`（`21.84% CAGR / -36.76% MaxDD / 0.95 Sharpe / 6.80 Turn`），2020 `hkconnect_path2_inverse_elastic_monthly`（`25.82% / -36.76% / 1.01 / 6.64`）。
- 2023 winner 仍为 `hkconnect_path2_theme_monthly`（`31.22% CAGR / -16.07% MaxDD / 1.41 Sharpe / 6.02 Turn`），2025 winner 仍为 `hkconnect_path2_breakout_concentrated_monthly`（`97.73% / -7.23% / 2.35 / 9.05`）。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 2 rotation 为 `stagnation_runs=15 / recommended_focus=elasticity_cost_control / rotate`；下一轮优先控制高弹性路线的回撤、换手和交易成本。

## 本轮执行计划（2026-05-17 11:15 CST）

- 本轮随 HK 五窗口回测单独评估月频、双周、高集中突破、高弹性与主题候选；Path 2 不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`（`21.84% CAGR / -36.76% MaxDD / 0.95 Sharpe / 6.80 Turn`），2020 `hkconnect_path2_inverse_elastic_monthly`（`25.82% / -36.76% / 1.01 / 6.64`）。
- 2023 winner 仍为 `hkconnect_path2_theme_monthly`（`31.22% CAGR / -16.07% MaxDD / 1.41 Sharpe / 6.02 Turn`），2025 winner 仍为 `hkconnect_path2_breakout_concentrated_monthly`（`97.73% / -7.23% / 2.35 / 9.05`）。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 rotation 为 `stagnation_runs=12 / recommended_focus=biweekly_breakout / rotate`；下一轮优先复核双周突破候选在回撤、换手和交易成本约束下是否优于月频锚点。

## 本轮执行计划（2026-05-17 05:15 CST）

- 本轮随 HK 五窗口回测单独评估月频、双周、高集中突破、高弹性与主题候选；Path 2 不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`（`21.84% CAGR / -36.76% MaxDD / 0.95 Sharpe / 6.80 Turn`），2020 `hkconnect_path2_inverse_elastic_monthly`（`25.82% / -36.76% / 1.01 / 6.64`）。
- 2023 winner 仍为 `hkconnect_path2_theme_monthly`（`31.22% CAGR / -16.07% MaxDD / 1.41 Sharpe / 6.02 Turn`），2025 winner 仍为 `hkconnect_path2_breakout_concentrated_monthly`（`97.73% / -7.23% / 2.35 / 9.05`）。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 rotation 为 `stagnation_runs=10 / recommended_focus=high_return_monthly / rotate`；下一轮在高收益月频候选上优先做回撤、换手与交易成本约束，同时保留双周与高频观察。

## 本轮执行计划（2026-05-16 23:12 CST）

- 本轮随 HK 五窗口回测单独评估月频、双周、突破、高集中与高弹性候选；Path 2 不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`（`21.84% CAGR / -36.76% MaxDD / 0.95 Sharpe / 6.80 Turn`），2020 `hkconnect_path2_inverse_elastic_monthly`（`25.82% / -36.76% / 1.01 / 6.64`）。
- 2023 winner 仍为 `hkconnect_path2_theme_monthly`（`31.22% CAGR / -16.07% MaxDD / 1.41 Sharpe / 6.02 Turn`），2025 winner 仍为 `hkconnect_path2_breakout_concentrated_monthly`（`97.73% / -7.23% / 2.35 / 9.05`）。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 rotation 为 `stagnation_runs=8 / recommended_focus=elasticity_cost_control / rotate`；下一轮优先控制高弹性路线的回撤、换手和交易成本，同时保留双周突破观察。

## 本轮执行计划（2026-05-16 17:14 CST）

- 本轮与 HK Path 1/3 同批完成五窗口离线回测，Path 2 单独评估月频、双周、高集中突破、高弹性与主题候选；港股线不并入 A 股 winner 结论。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`（`21.84% CAGR / -36.76% MaxDD / 0.95 Sharpe / 6.80 Turn`），2020 `hkconnect_path2_inverse_elastic_monthly`（`25.82% / -36.76% / 1.01 / 6.64`）。
- 2023 winner 仍为 `hkconnect_path2_theme_monthly`（`31.22% CAGR / -16.07% MaxDD / 1.41 Sharpe / 6.02 Turn`），2025 winner 仍为 `hkconnect_path2_breakout_concentrated_monthly`（`97.73% / -7.23% / 2.35 / 9.05`）。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收尾 rotation 为 `stagnation_runs=6 / recommended_focus=elasticity_cost_control / rotate`；下一轮优先控制高弹性路线的回撤、换手和交易成本，但不因月频当前胜出而停止高频路线观察。

## 本轮执行计划（2026-05-16 11:20 CST）

- 本轮随 HK 五窗口离线回测继续单独评估月频、双周、突破、高集中与高弹性候选；Path 2 不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 2025 `breakout_concentrated_monthly` 继续保持短窗弹性（`97.73% CAGR`），但高弹性路线长窗回撤仍约 `-36.76%`、换手约 `6.6x-6.8x`，成本和回撤压力仍需继续记录。
- 收尾 rotation 为 `stagnation_runs=2 / recommended_focus=high_return_monthly / continue`；下一轮保留双周突破观察，同时优先做高收益月频候选的回撤/换手约束。

## 本轮执行计划（2026-05-16 06:56 CST）

- 本轮随 HK 五窗口回测继续单独评估月频、双周、突破、高集中与高弹性候选；Path 2 不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 2025 窗口 `breakout_concentrated_monthly` 仍有 `97.73% CAGR` 的短窗弹性，但长窗 high-elastic winner 回撤约 `-36.76%`、换手约 `6.6x-6.8x`，仍需成本和回撤压力测试。
- 收尾 rotation 为 `stagnation_runs=32 / recommended_focus=biweekly_breakout / rotate`；下一轮优先保留双周突破路线并压回撤/换手，不因为月频当前胜出而停止高频观察。

## 本轮执行计划（2026-05-15 15:16 CST）

- 本轮与 HK Path 1 同批完成五窗口离线回测，并继续单独评估月频、双周、突破、高集中与高弹性候选；港股 Path 2 继续不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 本轮没有新的 HK Path 2 winner 或 robust candidate 漂移；`since_2026_01` 继续只作为观察窗，不进入四窗口 winner 结论。
- 最终 rotation 为 `stagnation_runs=24 / recommended_focus=elasticity_cost_control / rotate`；下一轮优先压高弹性路线的回撤、换手和交易成本，而不是只追月频短窗收益。

## 本轮执行计划（2026-05-15 10:14 CST）

- 本轮港股 Path 2 随五窗口回测完整巡检月频、双周、突破、高集中与高弹性候选；`update_hkconnect_artifacts.py` 已同步 tracked winners 与对比图，HK coverage 最终为 `pass`。
- HK Path 2 tracked winners 未变：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`；最终 rotation 为 `stagnation_runs=22 / biweekly_breakout`，下一轮继续保留双周突破路线而不是只追月频短窗。

## 本轮执行计划（2026-05-14 22:55 CST）

- 本轮港股五窗口回测与 artifact 同步已完成，Path 2 月频/双周高收益探索线继续单独记录，不并入 A 股或 HK Path 1。
- HK Path 2 tracked winners 当前为：2017 `hkconnect_path2_equal_elastic_monthly`（`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turn`），2020 `hkconnect_path2_inverse_elastic_monthly`（`25.82% / -36.76% / 1.0054 / 6.64`），2023 `hkconnect_path2_theme_monthly`（`31.22% / -16.07% / 1.4133 / 6.02`），2025 `hkconnect_path2_breakout_concentrated_monthly`（`97.73% / -7.23% / 2.3476 / 9.05`）。
- 四窗口 robust candidate 为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`；最终 guard 为 `stagnation_runs=18 / high_return_monthly`，下一轮优先控制弹性线成本和回撤。

## 本轮执行计划（2026-05-14 15:10 CST）

- 本轮与港股 Path 1 同批完成五窗口离线回测，并继续单独评估 Path 2 月度、双周、突破、高集中与高弹性候选；港股线不并入 A 股结论。
- 收尾 guard 对 HK coverage 为 `pass`，HK Path 2 rotation 为 `stagnation_runs=13 / recommended_focus=biweekly_breakout`；下一轮新增配额为 HK Path 2 `3` 个候选。
- Path 2 tracked winners 未漂移：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 最新指标为：2017 `21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；2020 `25.82% / -36.76% / 1.0054 / 6.64`；2023 `31.22% / -16.07% / 1.4133 / 6.02`；2025 `97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 下一轮围绕 `biweekly_breakout` 新增或复跑高集中突破的双周缓冲/降仓候选，同时继续保留高收益月频路线，不因当前月频短窗胜出而停止高频路线观察。

## 本轮执行计划（2026-05-14 09:13 CST）

- 本轮与港股 Path 1 同批完成五窗口离线回测，并继续单独评估 Path 2 月度、双周、突破、高集中与高弹性候选；港股线不并入 A 股结论。
- 收尾 guard 对 HK coverage 为 `pass`，HK Path 2 rotation 为 `stagnation_runs=11 / recommended_focus=high_return_monthly`；下一轮新增配额为 HK Path 2 `3` 个候选。
- Path 2 tracked winners 未漂移：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 最新指标为：2017 `21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；2020 `25.82% / -36.76% / 1.0054 / 6.64`；2023 `31.22% / -16.07% / 1.4133 / 6.02`；2025 `97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 下一轮保留高弹性和双周观察，但优先围绕高收益月频候选做回撤、换手和成本约束后的存活性比较，不因月频短窗胜出而停止高频路线观察。

## 本轮执行计划（2026-05-14 03:17 CST）

- 本轮与港股 Path 1 同批完成五窗口离线回测，并继续单独评估 Path 2 月度、双周、突破、高集中与高弹性候选；港股线不并入 A 股结论。
- Path 2 tracked winners 未漂移：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 最新指标为：2017 `21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；2020 `25.82% / -36.76% / 1.0054 / 6.64`；2023 `31.22% / -16.07% / 1.4133 / 6.02`；2025 `97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 收盘 guard 将 HK Path 2 rotation 推进到 `stagnation_runs=9 / recommended_focus=high_return_monthly`；下一步保留高弹性路线，但优先比较高收益月频候选在回撤、换手和成本约束后的存活性，不因月频短窗胜出而停止高频路线观察。

## 本轮执行计划（2026-05-13 21:21 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并单独评估 Path 2 月度、双周、突破、高集中与高弹性候选；港股线继续不并入 A 股结论。
- Path 2 tracked winners 未漂移：2017 `hkconnect_path2_equal_elastic_monthly`，2020 `hkconnect_path2_inverse_elastic_monthly`，2023 `hkconnect_path2_theme_monthly`，2025 `hkconnect_path2_breakout_concentrated_monthly`。
- 最新指标为：2017 `21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；2020 `25.82% / -36.76% / 1.0054 / 6.64`；2023 `31.22% / -16.07% / 1.4133 / 6.02`；2025 `97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- rotation 已提示下一轮港股 Path 2 转向 `elasticity_cost_control`；高弹性路线仍保留，但重点应控制回撤和换手成本。

## 本轮执行计划（2026-05-13 09:13 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 单独评估 Path 2 月度、双周、突破、高集中、高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 港股 Path 3 周频路线继续单独保留：当前 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；不因为月频当前胜出就停止高频路线观察。

## 本轮执行计划（2026-05-13 03:32 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 单独评估 Path 2 月度、双周、突破、高集中、高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 港股 Path 3 周频路线继续单独保留：当前 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；不因为月频当前胜出就停止高频路线观察。

## 本轮执行计划（2026-05-12 21:20 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 单独评估 Path 2 的月度、双周、突破、高集中与高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 港股 Path 3 周频路线继续单独保留：当前 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；不因为月频当前胜出就停止高频路线观察。

## 本轮执行计划（2026-05-12 09:12 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 单独评估 Path 2 的月度、双周、突破、高集中与高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 港股 Path 3 周频路线继续单独保留：当前 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；不因为月频当前胜出就停止高频路线观察。

## 本轮执行计划（2026-05-12 03:16 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 单独评估 Path 2 的月度、双周、突破、高集中与高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 港股 Path 3 周频路线继续单独保留：当前 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；不因为月频当前胜出就停止高频路线观察。

## 本轮执行计划（2026-05-11 21:22 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 单独评估 Path 2 的月度、双周、突破、高集中与高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 港股 Path 3 周频路线继续单独保留：当前 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；不因为月频当前胜出就停止高频路线观察。

## 本轮执行计划（2026-05-11 15:15 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 单独评估 Path 2 的月度、双周、突破、高集中与高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 港股 Path 3 周频路线继续单独保留，当前 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`，`meanCAGR=31.15% / minCAGR=21.78% / worstMaxDD=-33.66% / meanTurn=11.31`；不因为月频当前胜出就停止高频路线观察。

## 本轮执行计划（2026-05-11 09:19 CST）

- 本轮与港股 Path 1 同批跑五窗口离线回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 单独评估 Path 2 的月度、双周、突破、高集中与高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`。
- 港股 Path 3 周频路线继续单独保留，当前 robust candidate 仍为 `hkconnect_path3_stable_weekly_equal_buffered`；不因为月频当前胜出就停止高频路线观察。

## 本轮执行计划（2026-05-11 03:13 CST）

- 本轮与港股 Path 1 同批跑五窗口回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 分离评估 Path 2 的月度/双周主题、突破、高集中、高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`；港股 Path 3 周频路线继续单独保留，当前 robust candidate 为 `hkconnect_path3_stable_weekly_equal_buffered`。

## 本轮执行计划（2026-05-10 21:14 CST）

- 本轮与港股 Path 1 同批跑五窗口回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 分离评估 Path 2 的月度/双周主题、突破、高集中、高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`；港股 Path 3 周频路线继续单独保留，当前 robust candidate 为 `hkconnect_path3_stable_weekly_equal_buffered`。

## 本轮执行计划（2026-05-10 15:04 CST）

- 本轮与港股 Path 1 同批跑五窗口回测，并用 `results_hkconnect/strategy_comparison_hkconnect.csv` 分离评估 Path 2 的月度/双周主题、突破、高集中、高弹性候选；港股线继续不并入 A 股 winner 结论。
- Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍为 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`；港股 Path 3 周频路线继续单独保留，不回并 Path 2 winner 结论。

## 本轮执行计划（2026-05-10 09:17 CST）

- 本轮与港股 Path 1 同批运行五窗口回测，并用 `scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与三张图表；港股线继续不并入 A 股 winner 结论。
- Path 2 继续只保留收益上限探索线的月度/双周主题、突破、高集中、高弹性候选；纯周度主题强度继续交给 Path 3 独立跟踪。
- 当前 Path 2 tracked winners 未漂移：`since_2017_01` 为 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 为 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`；`since_2026_01` 只观察，当前 raw leader 仍是 `hkconnect_path2_breakout_concentrated_monthly`。
- 港股 Path 3 同步观察未漂移：`since_2017_01` winner 为 `hkconnect_path3_stable_weekly_equal_buffered`，`since_2020_01 / since_2023_01` 为 `hkconnect_path3_theme_fast_weekly_buffered`，`since_2025_01` 为 `hkconnect_path3_theme_fast_weekly_defensive`；周频路线继续单独保留，不回并 Path 2。

## 本轮执行计划（2026-05-10 03:16 CST）

- 本轮继续以港股三路径拆分口径运行五窗口离线回测，并用 `scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与三张图表；港股线不并入 A 股 winner 结论。
- Path 2 继续只保留收益上限探索线的月度/双周主题、突破、高集中、高弹性候选；纯周度主题强度继续交给 Path 3 独立跟踪。
- 当前 Path 2 tracked winners：`since_2017_01` 切到 `hkconnect_path2_equal_elastic_monthly`，`21.84% CAGR / -36.76% MaxDD / 0.9475 Sharpe / 6.80 Turnover`；`since_2020_01` 切到 `hkconnect_path2_inverse_elastic_monthly`，`25.82% / -36.76% / 1.0054 / 6.64`。
- `since_2023_01` 仍为 `hkconnect_path2_theme_monthly`，`31.22% CAGR / -16.07% MaxDD / 1.4133 Sharpe / 6.02 Turnover`；`since_2025_01` 仍为 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% / -7.23% / 2.3476 / 9.05`。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_monthly`，`meanCAGR=36.97% / minCAGR=18.64% / worstMaxDD=-30.99% / meanTurn=6.22`；`since_2026_01` 只观察，当前 raw leader 仍是 `hkconnect_path2_breakout_concentrated_monthly`（`246.87% CAGR / -1.25% MaxDD / 2.3968 Sharpe / 8.00 Turnover`）。
- 港股 Path 3 同步观察：`since_2017_01` winner 为 `hkconnect_path3_stable_weekly_equal_buffered`，`since_2020_01 / since_2023_01` 为 `hkconnect_path3_theme_fast_weekly_buffered`，`since_2025_01` 为 `hkconnect_path3_theme_fast_weekly_defensive`；周频路线继续单独保留，不回并 Path 2。

## 本轮执行计划（2026-05-09 21:14 CST）

- 本轮继续以港股三路径拆分口径运行五窗口离线回测，并用 `scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与三张图表。
- Path 2 继续只保留收益上限探索线的月度/双周主题、突破、高集中、高弹性候选；纯周度主题强度交给 Path 3 独立跟踪。
- 当前 Path 2 tracked winners：`since_2017_01 / since_2020_01 / since_2023_01` 为 `hkconnect_path2_theme_monthly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`，四窗口 robust candidate 为 `hkconnect_path2_theme_monthly`。
- 关键指标：`theme_monthly` 长窗为 `21.57% CAGR / -18.98% MaxDD / 1.1176 Sharpe / 6.62 Turnover`，`since_2023_01` 为 `31.22% / -16.07% / 1.4133 / 6.02`；短窗 `breakout_concentrated_monthly` 为 `97.73% / -7.23% / 2.3476 / 9.05`。
- `since_2026_01` 只观察，当前 Path 2 raw leader 仍是 `hkconnect_path2_breakout_concentrated_monthly`；本轮新增 weekly 降仓/宽出场变体只归入 Path 3。

## 本轮执行计划（2026-05-09 18:09 CST）

- 本轮继续以港股三路径拆分口径运行五窗口离线回测，并用 `scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与三张图表。
- Path 2 继续只保留收益上限探索线的月度/双周主题、突破、高集中、高弹性候选；纯周度主题强度交给 Path 3 独立跟踪。
- 当前 Path 2 tracked winners：`since_2017_01 / since_2020_01 / since_2023_01` 为 `hkconnect_path2_theme_monthly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`，四窗口 robust candidate 为 `hkconnect_path2_theme_monthly`。
- 关键指标：`theme_monthly` 长窗为 `21.57% CAGR / -18.98% MaxDD / 1.1176 Sharpe / 6.62 Turnover`，`since_2023_01` 为 `31.22% / -16.07% / 1.4133 / 6.02`；短窗 `breakout_concentrated_monthly` 为 `97.73% / -7.23% / 2.3476 / 9.05`。
- `since_2026_01` 只观察，当前 Path 2 raw leader 是 `hkconnect_path2_breakout_concentrated_monthly`；下一轮继续扩月度/双周高收益结构，而不是回并 weekly 候选。

## 本轮执行计划（2026-05-09 三路径拆分）

- 本轮将港股 Path 2 收窄为收益上限探索线：保留月度/双周主题、突破、高集中、高弹性候选；单周换股候选已迁移到独立 Path 3。
- 重新运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 当前 Path 2 tracked winners：`since_2017_01 / since_2020_01 / since_2023_01` 为 `hkconnect_path2_theme_monthly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`，四窗口 robust candidate 为 `hkconnect_path2_theme_monthly`。
- 关键指标：`theme_monthly` 长窗为 `21.57% CAGR / -18.98% MaxDD / 1.1176 Sharpe / 6.62 Turnover`，`since_2023_01` 为 `31.22% / -16.07% / 1.4133 / 6.02`；短窗 `breakout_concentrated_monthly` 为 `97.73% / -7.23% / 2.3476 / 9.05`。
- 下一轮 Path 2 继续围绕月度/双周高收益结构扩原型；纯周度主题强度交给 Path 3 独立跟踪。

## 本轮执行计划（2026-05-09 13:04 CST）

- 本轮与港股 Path 1 同批运行五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 身份未漂移：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗为 `23.47% CAGR / -33.61% MaxDD / 0.9339 Sharpe / 30.48 Turnover`，`since_2023_01` 为 `40.80% CAGR / -19.56% MaxDD / 1.3152 Sharpe / 29.62 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`，`meanCAGR=41.45% / minCAGR=23.47% / worstMaxDD=-33.61% / meanTurn=31.32`。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-09 05:08 CST）

- 本轮与港股 Path 1 同批运行五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 身份未漂移：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗为 `23.47% CAGR / -33.61% MaxDD / 0.9339 Sharpe / 30.48 Turnover`，`since_2023_01` 为 `40.80% CAGR / -19.56% MaxDD / 1.3152 Sharpe / 29.62 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`，`meanCAGR=41.45% / minCAGR=23.47% / worstMaxDD=-33.61% / meanTurn=31.32`。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-08 23:12 CST）

- 本轮与港股 Path 1 同批运行五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 身份未发生结构性切换：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- 更新到 `sample_end=2026-05-08` 后，`hkconnect_path2_theme_fast_weekly` 长窗为 `23.47% CAGR / -33.61% MaxDD / 0.9339 Sharpe / 30.48 Turnover`，`since_2023_01` 为 `40.80% CAGR / -19.56% MaxDD / 1.3152 Sharpe / 29.62 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`，`meanCAGR=41.45% / minCAGR=23.47% / worstMaxDD=-33.61% / meanTurn=31.32`。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-08 17:24 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗指标为 `24.99% CAGR / -33.61% MaxDD / 0.9832 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `43.75% CAGR / -19.56% MaxDD / 1.3917 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`，`meanCAGR=45.45% / minCAGR=24.99% / worstMaxDD=-33.61% / meanTurn=31.27`。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-08 13:15 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗指标为 `24.99% CAGR / -33.61% MaxDD / 0.9832 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `43.75% CAGR / -19.56% MaxDD / 1.3917 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`，`meanCAGR=45.45% / minCAGR=24.99% / worstMaxDD=-33.61% / meanTurn=31.27`。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-08 07:28 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗指标为 `24.99% CAGR / -33.61% MaxDD / 0.9832 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `43.75% CAGR / -19.56% MaxDD / 1.3917 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`，`meanCAGR=45.45% / minCAGR=24.99% / worstMaxDD=-33.61% / meanTurn=31.27`。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-07 23:12 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗指标为 `24.99% CAGR / -33.61% MaxDD / 0.9832 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `43.75% CAGR / -19.56% MaxDD / 1.3917 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`，`meanCAGR=45.45% / minCAGR=24.99% / worstMaxDD=-33.61% / meanTurn=31.27`。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-07 11:10 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗指标为 `24.99% CAGR / -33.61% MaxDD / 0.9832 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `43.75% CAGR / -19.56% MaxDD / 1.3917 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（`meanCAGR=45.45% / minCAGR=24.99% / worstMaxDD=-33.61% / meanTurn=31.27`）。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-07 05:06 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗指标为 `24.99% CAGR / -33.61% MaxDD / 0.9832 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `43.75% CAGR / -19.56% MaxDD / 1.3917 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，`97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（`meanCAGR=45.45% / minCAGR=24.99% / worstMaxDD=-33.61% / meanTurn=31.27`）。
- 周频、双周、月频候选继续全部保留，不因月频短窗胜出而停止高频路线探索。

## 本轮执行计划（2026-05-06 23:15 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 长窗指标为 `24.99% CAGR / -33.61% MaxDD / 0.9832 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `43.75% CAGR / -19.56% MaxDD / 1.3917 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`，指标为 `97.73% CAGR / -7.23% MaxDD / 2.3476 Sharpe / 9.05 Turnover`。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（`meanCAGR=45.45% / minCAGR=24.99% / worstMaxDD=-33.61% / meanTurn=31.27`）；周频、双周、月频候选继续全部保留。

## 本轮执行计划（2026-05-06 11:35 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未较 06:14 记录漂移：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 关键指标保持为长窗 `23.94% CAGR / -33.61% MaxDD / 0.9555 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `42.85% / minCAGR 23.94% / worstMaxDD -33.61% / meanTurn 31.27`）；周频、双周、月频候选继续全部保留。

## 本轮执行计划（2026-05-06 06:14 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 tracked winners 未较 00:04 记录漂移：`since_2017_01 / since_2020_01 / since_2023_01` 仍是 `hkconnect_path2_theme_fast_weekly`。
- `hkconnect_path2_theme_fast_weekly` 关键指标保持为长窗 `23.94% CAGR / -33.61% MaxDD / 0.9555 Sharpe / 30.45 Turnover`，`since_2023_01` 为 `41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`。
- `since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `42.85% / minCAGR 23.94% / worstMaxDD -33.61% / meanTurn 31.27`）；周频、双周、月频候选继续全部保留。

## 本轮执行计划（2026-05-06 00:04 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 继续单独评估 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 锚点，不复用 A 股 Path 2 的 `promo_liqmom_top15` 阈值邻域。
- 重点核对 `hkconnect_path2_theme_fast_weekly` 是否继续占据 robust candidate，并确认周频、双周、月频候选全部保留。
- 本轮五窗口离线回测后，tracked payload 仍为 `as_of=2026-04-30`；Path 2 `since_2017_01 / since_2020_01` winner 从 `hkconnect_path2_theme_monthly` 切到 `hkconnect_path2_theme_fast_weekly`（`23.94% CAGR / -33.61% MaxDD / 0.9555 Sharpe / 30.45 Turnover`）。
- `since_2023_01` 继续是 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 继续是 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `42.85% / minCAGR 23.94% / worstMaxDD -33.61% / meanTurn 31.27`）；周频、双周、月频候选继续全部保留。

## 本轮补充计划与记录（2026-05-05 18:16 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 继续单独评估 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 锚点，不复用 A 股 Path 2 的 `promotion_signal_mode` 结论。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因月频短窗候选领先而停止高频路线探索。

## 本轮补充计划与记录（2026-05-05 12:14 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 继续单独评估 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 锚点，不复用 A 股 Path 2 的 `midcycle_momentum` 原型。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留。

## 本轮补充计划与记录（2026-05-05 06:14 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 继续单独评估 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 锚点，不复用 A 股 Path 2 的 confirmation filter 结论。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因短窗月频候选领先而停止高频路线探索。

## 本轮补充计划与记录（2026-05-05 00:03 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 继续单独评估 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 锚点，不复用 A 股 Path 2 的 ramp 微批量结论。
- 重点核对 `hkconnect_path2_theme_fast_weekly` 是否继续占据 robust candidate，以及周频、双周、月频候选是否全部保留在候选集。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留。

## 本轮补充计划与记录（2026-05-04 18:07 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 继续单独评估 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 锚点，不复用 A 股 Path 2 的高频单票结论。
- 重点核对 `hkconnect_path2_theme_fast_weekly` 是否继续占据 robust candidate，以及周频、双周、月频候选是否全部保留在候选集。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留。

## 本轮补充计划与记录（2026-05-04 15:25 CST）

- 继续与港股 Path 1 同批运行五窗口离线回测，并执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）。
- 周频、双周、月频候选继续全部保留，不因短窗月频突破候选领先而停止高频路线探索。

## 本轮补充计划（2026-05-04 06:45 CST）

- 本轮继续与港股 Path 1 同批跑五窗口离线回测，再运行 `scripts/update_hkconnect_artifacts.py` 同步 tracked payload 与图表。
- Path 2 继续单独评估 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 当前锚点，不复用 A 股 Path 2 新增的 `core_theme` 结论。
- 重点核对 `hkconnect_path2_theme_fast_weekly` 是否继续占据 robust candidate，以及短窗月频突破候选是否只保持观察窗领先；周频、双周、月频候选继续全部保留。

### 本轮补充记录（2026-05-04 09:40 CST）

- 重新完成港股五窗口离线回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因短窗月频候选领先而停止高频路线探索。

## 本轮执行计划（2026-05-04）

- 本轮继续单独评估港股 Path 2 的 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 当前锚点结构，不复用 A 股 Path 2 结论。
- 默认比较对象继续包括现有月频、双周与单周港股 Path 2 候选，`since_2026_01` 只作为观察窗。
- 跑完后重点核对 `robust_candidate` 是否仍由 `hkconnect_path2_theme_fast_weekly` 占据，以及 `since_2025_01 / since_2026_01` 是否继续由更高集中月频突破候选领先；不因月频当前胜出而停止高频路线探索。

### 本轮快筛记录（2026-05-04 03:57 CST）

- 重新完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因当前短窗月频突破候选领先而停止高频路线探索。

## 本轮执行计划（2026-05-03）

- 本轮继续单独评估港股 Path 2 的 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 当前锚点结构，不复用 A 股 Path 2 结论。
- 默认比较对象继续包括现有月频、双周与单周港股 Path 2 候选，`since_2026_01` 只作为观察窗。
- 跑完后重点核对 `robust_candidate` 是否仍由 `hkconnect_path2_theme_fast_weekly` 占据，以及 `since_2025_01 / since_2026_01` 是否继续由更高集中月频突破候选领先；不因月频当前胜出而停止高频路线探索。

### 本轮快筛记录（2026-05-03 00:16 CST；06:11 CST 复核）

- 重新完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因短窗月频突破候选领先而停止高频路线探索。

### 本轮补充（2026-05-03 12:05 CST）

- 再次完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`，`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因月频短窗候选领先而停止高频路线探索。

### 本轮补充（2026-05-03 18:13 CST）

- 再次完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因当前短窗月频突破候选领先而停止高频路线探索。

## 本轮执行计划（2026-05-02）

- 本轮继续单独评估港股 Path 2 的 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 当前锚点结构，不复用 A 股 Path 2 结论。
- 默认比较对象继续包括现有月频、双周与单周港股 Path 2 候选，`since_2026_01` 只作为观察窗。
- 跑完后重点核对 `robust_candidate` 是否仍由 `hkconnect_path2_theme_fast_weekly` 占据，以及 `since_2025_01 / since_2026_01` 是否继续由更高集中月频突破候选领先；不因月频当前胜出而停止高频路线探索。

### 本轮快筛记录（2026-05-02）

- 重新完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）。
- `since_2026_01` 继续只作为观察窗；周频、双周、月频候选继续全部保留，本轮不因短窗月频突破候选领先而停止高频路线探索。

### 本轮补充（2026-05-02 06:07 CST）

- 重新完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`，`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留。

### 本轮补充（2026-05-02 12:10 CST）

- 再次完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因当前月频或短窗候选领先而停止高频路线探索。

### 本轮补充（2026-05-02 18:08 CST）

- 再次完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；周频、双周、月频候选继续全部保留，不因当前月频或短窗候选领先而停止高频路线探索。

## 本轮执行计划（2026-05-01）

- 本轮继续单独评估港股 Path 2 的 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 当前锚点结构，不复用 A 股 Path 2 结论。
- 默认比较对象继续包括现有月频、双周与单周港股 Path 2 候选，`since_2026_01` 只作为观察窗。
- 跑完后重点核对 `robust_candidate` 是否仍由 `hkconnect_path2_theme_fast_weekly` 占据，以及 `since_2025_01 / since_2026_01` 是否继续由更高集中月频突破候选领先。

### 本轮快筛记录（2026-05-01）

- 重新完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 继续独立于 A 股 Path 2。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`，`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）。
- `since_2026_01` 继续只作为观察窗；周频、双周、月频候选继续全部保留，本轮不因月频或短窗候选当前领先而停止高频路线探索。

### 本轮补充（2026-05-01 06:11 CST）

- 再次完成港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 结论继续独立于 A 股 Path 2。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）。
- `since_2026_01` 继续只作为观察窗；周频、双周、月频候选继续全部保留，本轮不因短窗月频突破候选领先而停止高频路线探索。

### 本轮补充（2026-05-01 12:11 CST）

- 再次完成港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 结论继续独立于 A 股 Path 2。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）。
- `since_2026_01` 继续只作为观察窗，raw leader 仍是 `hkconnect_path2_breakout_concentrated_monthly`（`243.84% CAGR / -1.31% MaxDD / 2.3917 Sharpe / 8.00 Turnover`）；周频、双周、月频候选继续全部保留。

### 本轮补充（2026-05-01 18:14 CST）

- 再次完成港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 Path 2 结论继续独立于 A 股 Path 2。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）。
- `since_2026_01` 继续只作为观察窗；周频、双周、月频候选继续全部保留，本轮不因月频或短窗候选当前领先而停止高频路线探索。

## 本轮执行计划（2026-04-30）

- 本轮继续单独评估港股 Path 2 的 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 当前锚点结构，不复用 A 股 Path 2 结论。
- 默认比较对象继续包括现有月频、双周与单周港股 Path 2 候选，`since_2026_01` 只作为观察窗。
- 跑完后重点核对 `robust_candidate` 是否仍由 `hkconnect_path2_theme_fast_weekly` 占据，以及 `since_2025_01 / since_2026_01` 是否继续由更高集中月频突破候选领先。

### 本轮快筛记录（2026-04-30）

- 重新完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；随后同步运行 live/public 导出。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`，`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`。
- `robust_candidate` 继续是 `hkconnect_path2_theme_fast_weekly`（`meanCAGR 40.60% / minCAGR 20.48% / worstMaxDD -33.61% / meanTurn 31.53`），保持高换手鲁棒锚点。
- `since_2026_01` 仍只做观察窗；raw leader 继续为 `hkconnect_path2_breakout_concentrated_monthly`（`361.49% CAGR / -1.31% MaxDD / 2.2491 Sharpe / 7.51 Turnover`），不进入 tracked winners。
- 本轮港股 tracked JSON 与港股对比图重写后没有实质 git diff；公开快照的有效同步来自 A 股 `data_as_of=2026-04-30` 更新，港股信号/换股生效日仍由真实周频或月频评估点决定。

### 本轮补充（2026-04-30 06:35 CST）

- 再次完成港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；tracked JSON 与 Path 2 图表重写后仍无实质 git diff。
- Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`，`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`，四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`。
- `since_2026_01` 继续只作为观察窗，raw leader 仍为 `hkconnect_path2_breakout_concentrated_monthly`；本轮不因月频当前胜出而移除双周/单周候选。

### 本轮补充（2026-04-30 12:12 CST）

- 再次完成港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`，港股 Path 2 结论仍独立于 A 股 Path 2。
- Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`，`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`；`since_2026_01` 继续只作为观察窗，当前不因短窗高弹性切换而改写 robust 口径。
- 周频、双周、月频候选继续全部保留；本轮只是确认性重跑，没有因为月频或短窗候选当前领先而停止高频路线探索。

### 本轮补充（2026-04-30 18:16 CST）

- 再次完成港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；tracked payload 的数据截止日推进到 `as_of=2026-04-30`，港股 Path 2 结论仍独立于 A 股 Path 2。
- Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`（`22.32% CAGR / -18.86% MaxDD / 1.1522 Sharpe / 6.62 Turnover`），`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`（`41.78% CAGR / -19.56% MaxDD / 1.3529 Sharpe / 29.55 Turnover`），`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`（`97.56% CAGR / -7.23% MaxDD / 2.3471 Sharpe / 9.05 Turnover`）。
- 四窗口 robust candidate 仍是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `41.33% / minCAGR 20.89% / worstMaxDD -33.61% / meanTurn 31.53`）；`since_2026_01` raw leader 仍是 `hkconnect_path2_breakout_concentrated_monthly`（`243.84% CAGR / -1.31% MaxDD / 2.3917 Sharpe / 8.00 Turnover`）。
- 周频、双周、月频候选继续全部保留；本轮是指标同步与公开/实盘产物刷新，不因月频短窗领先而停止高频路线探索。

## 上轮执行计划（2026-04-29）

- 本轮继续单独评估港股 Path 2 的 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 当前锚点结构，不复用 A 股 Path 2 结论。
- 默认比较对象包括现有月频、双周与单周港股 Path 2 候选，`since_2026_01` 只作为观察窗。
- 跑完后重点核对 `robust_candidate` 是否仍由 `hkconnect_path2_theme_fast_weekly` 占据，以及 `since_2025_01 / since_2026_01` 是否继续由更高集中月频突破候选领先。

### 本轮快筛记录（2026-04-29 12:09 CST）

- 重新完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；tracked JSON 与港股对比图同步到当前缓存口径。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`，`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`。
- `robust_candidate` 继续是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `40.60% / minCAGR 20.48% / worstMaxDD -33.61% / meanTurn 31.53`），保持高换手鲁棒锚点。
- `since_2026_01` 仍只做观察窗；当前 raw leader 为 `hkconnect_path2_breakout_concentrated_monthly`（`361.49% CAGR / -1.31% MaxDD / 2.2491 Sharpe / 7.51 Turnover`），不进入 tracked winners。

### 本轮快筛记录（2026-04-29 18:50 CST）

- 重新完成港股五窗口回测，并运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；随后同步运行 live/public 导出。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01` 为 `hkconnect_path2_theme_monthly`，`since_2023_01` 为 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 为 `hkconnect_path2_breakout_concentrated_monthly`。
- `robust_candidate` 继续是 `hkconnect_path2_theme_fast_weekly`（meanCAGR `40.60% / minCAGR 20.48% / worstMaxDD -33.61% / meanTurn 31.53`），保持高换手鲁棒锚点。
- `since_2026_01` 仍只做观察窗；raw leader 继续为 `hkconnect_path2_breakout_concentrated_monthly`（`361.49% CAGR / -1.31% MaxDD / 2.2491 Sharpe / 7.51 Turnover`），不进入 tracked winners。
- 本轮没有新的窗口赢家，但 `results_hkconnect/**` 与公开快照发生有效同步：公开策略详情的 `data_as_of` 更新到 `2026-04-29`，而周频信号生效日仍保持 `2026-04-24`、月频信号生效日保持 `2026-03-31`。

## 上轮执行计划（2026-04-28）

- 本轮继续单独评估港股 Path 2 的 `theme_monthly / theme_fast_weekly / breakout_concentrated_monthly` 当前锚点结构，不复用 A 股 Path 2 结论。
- 默认比较对象包括现有月频、双周与单周港股 Path 2 候选，`since_2026_01` 只作为观察窗。
- 跑完后重点核对 `robust_candidate` 是否仍由 `hkconnect_path2_theme_fast_weekly` 占据，以及 `since_2025_01 / since_2026_01` 是否继续由更高集中月频突破候选领先。

### 本轮快筛记录（2026-04-28 00:08 CST）

- 港股五窗口回测完成，并已运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；本轮未产生新的港股 tracked JSON 或港股图表 git diff。
- 当前 Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01 / since_2023_01` 为 `hkconnect_path2_theme_monthly`，`since_2025_01` 为 `hkconnect_path2_breakout_monthly`。
- `robust_candidate` 继续是 `hkconnect_path2_equal_elastic_monthly`（meanCAGR `36.01% / minCAGR 17.59% / worstMaxDD -38.60%`）；`since_2026_01` 仍只作为观察窗。

### 本轮快筛记录（2026-04-28 12:04 CST）

- 重新完成港股五窗口回测，并已运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；tracked JSON 与港股图表没有新增 git diff。
- 当前 Path 2 tracked winners 继续维持：`since_2017_01 / since_2020_01 / since_2023_01` 为 `hkconnect_path2_theme_monthly`，`since_2025_01` 为 `hkconnect_path2_breakout_monthly`。
- `robust_candidate` 继续是 `hkconnect_path2_equal_elastic_monthly`（meanCAGR `36.01% / minCAGR 17.59% / worstMaxDD -38.60%`）；`since_2026_01` raw leader 仍只作为观察窗，不进入 tracked winners。

### 本轮快筛记录（2026-04-28 18:29 CST）

- 重新完成港股五窗口回测，并已运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；本轮出现新的 Path 2 tracked winner 与 robust 改写。
- 当前 Path 2 tracked winners 改为：`since_2017_01 / since_2020_01` 仍由 `hkconnect_path2_theme_monthly` 占据，`since_2023_01` 切到 `hkconnect_path2_theme_fast_weekly`，`since_2025_01` 切到 `hkconnect_path2_breakout_concentrated_monthly`。
- `robust_candidate` 从 `hkconnect_path2_equal_elastic_monthly` 切到 `hkconnect_path2_theme_fast_weekly`（meanCAGR `40.60% / minCAGR 20.48% / worstMaxDD -33.61%`），收益鲁棒性改善但平均换手升至 `31.53`。
- `since_2026_01` 仍只作为观察窗；当前 raw leader 为 `hkconnect_path2_breakout_concentrated_monthly`（`361.49% CAGR / -1.31% MaxDD / 2.2491 Sharpe / 7.51 Turnover`）。

## 定位
- 独立于当前 A 股 Path 2
- 仅限沪港通标的（当前使用 Tushare `stock_hsgt` 最新可得名单作为静态池）
- 目标：优先冲收益上限，尤其观察 2020 / 2023 窗口能否出现高弹性赢家

## 当前独立候选族
1. 高集中突破（monthly / biweekly / weekly）
2. 高成长主线（monthly / biweekly）
3. 动量 / 等权高弹性（monthly / weekly）

## 本轮迭代执行规则

- 沪港通 `Path 2` 作为**独立于 A 股**的研究线，每轮迭代都要单独评估，不复用 A 股 `scripts/path2_candidate_pass.py` 的 winner 结论。
- 默认回测窗口固定为：
  - `since_2017_01`
  - `since_2020_01`
  - `since_2023_01`
  - `since_2025_01`
  - `since_2026_01`（观察窗）
- 默认比较对象固定为当前港股 `Path 2` 月频 / 双周 / 单周候选集合：
  - 高集中突破与极集中突破
  - 高成长主线与快速主线
  - 等权 / 逆市值高弹性
  - 熊市空仓与风险收缩 sidecar
- 下一轮港股 `Path 2` 的晋级优先顺序固定为：
  1. `since_2020_01` 是否显著改善
  2. `since_2023_01` 是否维持高收益上限
  3. `MaxDD / Turnover` 是否仍在可接受范围
- 重点输出每个候选族的最优代表，并明确列出：
  - `Total Return`
  - `CAGR`
  - `MaxDD`
  - `Sharpe`
  - `Turnover`
- 若港股 `Path 2` 任一窗口赢家发生变化，需同步更新：
  - `results_hkconnect/strategy_comparison_hkconnect.csv`
  - 实盘平台导出层中的沪港通策略注册表
  - README/HISTORY（若当前轮允许更新）

## 当前默认推进结论

- 港股 `Path 2` 当前默认仍优先看：
  - `2020` 窗口能否继续抬高
  - `2023` 窗口能否维持爆发力
- 当前默认锚点已切换为：
  - `hkconnect_path2_theme_monthly`（`2017 / 2020` 窗口）
  - `hkconnect_path2_theme_fast_weekly`（`2023` 窗口与当前四窗口 robust candidate）
  - `hkconnect_path2_breakout_concentrated_monthly`（`2025` 窗口与 `2026` 观察窗 raw leader）
- 双周 / 单周候选继续保留，但当前只作为 sidecar challenger，不因为更高频而自动获得更高优先级。
- 若某候选只强化 `2025 / 2026` 而不能改善 `2020`，默认不作为下一轮主攻方向。

## 当前假设
- 港股高弹性标的对双周 / 单周调仓频率可能更敏感
- 单纯提高频率未必足够，必须和更高集中、更偏突破的信号结合
- 港股回撤天然更大，因此 Path 2 不先追求低回撤，而先追求收益上限

## 近期优先看
- 2020 / 2023 窗口的 CAGR 抬升
- 周频 / 双周频是否只放大换手，还是能真正提高收益上限
- 2026 观察窗是否出现“周频过拟合”

## 已知限制
- 当前不是严格的历史动态沪港通池，而是“最新可得名单静态池”
- 当前没有接入港股财务质量因子，更多依赖动量、突破、流动性与波动
- 若当前 Tushare key 无 `stock_hsgt` 权限，可手工提供 `data_cache/hkconnect/basic/stock_hsgt_manual.csv` 作为静态池输入

## 本轮快筛记录（2026-04-21 18:24）

- 运行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`
- 窗口赢家（按 `CAGR`，来源：`results_hkconnect/strategy_comparison_hkconnect.csv`）：
  - `since_2017_01`：`hkconnect_path2_equal_elastic_monthly`（CAGR `54.13%` / MaxDD `-17.08%` / Sharpe `1.1458`）
  - `since_2020_01`：`hkconnect_path2_equal_elastic_monthly`（CAGR `143.23%` / MaxDD `-12.04%` / Sharpe `1.6228`）
  - `since_2023_01`：`hkconnect_path2_theme_monthly`（CAGR `79.17%` / MaxDD `-1.68%` / Sharpe `3.7272`；该窗口目前实际可交易起点已后移至 `2025`）
  - `since_2025_01`：`hkconnect_path2_theme_monthly`（同上；与 `since_2023_01` 当前等价）
  - `since_2026_01`：观察窗调仓点不足，本轮全部跳过

## 本轮补充（2026-04-21 20:18）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论不变；`since_2026_01` 仍因调仓点不足全部跳过。

## 本轮补充（2026-04-21 22:20）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论不变；`since_2026_01` 仍因调仓点不足全部跳过（离线模式回退本地缓存）。

## 本轮补充（2026-04-22）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论继续不变；`since_2026_01` 仍因调仓点不足全部跳过。
- `hkconnect_path2_equal_elastic_monthly` 继续是 `since_2017_01 / since_2020_01` 赢家：其中 `since_2020_01` 达到 `143.23% CAGR / -12.04% MaxDD / 1.6228 Sharpe / 6.85 Turnover`，仍远高于其余候选。
- `hkconnect_path2_theme_monthly` 继续是 `since_2023_01 / since_2025_01` 赢家：`79.17% CAGR / -1.68% MaxDD / 3.7272 Sharpe / 7.65 Turnover`。
- 当前最接近但仍未改写赢家的挑战者是：
  - `since_2020_01`：`hkconnect_path2_breakout_biweekly`（`65.05% CAGR`，但明显落后于 `equal_elastic_monthly`，且 `Turnover 17.75` 过高）
  - `since_2023_01`：`hkconnect_path2_breakout_monthly`（`67.15% CAGR / -7.72% MaxDD`，仍低于 `theme_monthly`）
- 结论不变：单纯提高频率仍不足以改写港股 Path 2 的主线。下一轮应继续以 `equal_elastic_monthly / theme_monthly` 为锚点，只把双周/单周版本保留为 sidecar challengers。
- 本次再次重跑后，`results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 继续完全一致：`equal_elastic_monthly` 仍赢 `2017/2020`，`theme_monthly` 仍赢 `2023/2025`；因此本轮不刷新 README / HISTORY / 港股对比图。
- `2026-04-22 06:27 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：缓存回退路径工作正常，`equal_elastic_monthly` 与 `theme_monthly` 仍分别稳住 `2017/2020` 与 `2023/2025` 两组窗口，sidecar challenger 顺位也未变化。
- 当日后续再次重跑后，sidecar challenger 顺位仍未漂移：`since_2020_01` 最接近主线的依旧是 `hkconnect_path2_breakout_biweekly`（但 `65.05% CAGR / 17.75 Turnover` 与主线差距仍过大），`since_2023_01` 则仍是 `hkconnect_path2_breakout_monthly`；因此港股 Path 2 继续不新增候选族。
- 当日后续再次完整重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 并同步 `.venv/bin/python scripts/update_hkconnect_artifacts.py` 后，当前缓存基线把港股 Path 2 的 tracked winners 改写为：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`（两窗当前都从 `2020-12-01` 起算，`23.15% CAGR / -18.86% MaxDD / 1.1825 Sharpe / 6.64 Turnover`）
  - `since_2023_01`：`hkconnect_path2_theme_biweekly`（`49.30% CAGR / -16.47% MaxDD / 1.5442 Sharpe / 14.46 Turnover`）
  - `since_2025_01`：`hkconnect_path2_theme_biweekly`（`137.82% CAGR / -10.15% MaxDD / 2.5598 Sharpe / 15.28 Turnover`）
  - `robust`：`hkconnect_path2_theme_biweekly`（按四窗口口径应为 `meanCAGR 58.05% / minCAGR 22.54%`；此前 `breakout_monthly` 是把 `since_2026_01` 观察窗误算进去后的 artifact）
- 这意味着此前把 `equal_elastic_monthly` 当成 `2017 / 2020` 主锚点的结论已经失效；在当前缓存口径下，它只剩 `17.12% CAGR / -36.76% MaxDD / 0.7822 Sharpe / 6.47 Turnover`，不再具备主线资格。
- `since_2026_01` 仍只作为观察窗，不进入 tracked winners；当前 Path 2 raw leader 是 `hkconnect_path2_breakout_monthly`，达到 `190.38% CAGR / -4.77% MaxDD / 2.2531 Sharpe / 7.47 Turnover`。下一轮港股 Path 2 应围绕 `theme_monthly / theme_biweekly` 两条主线继续扩原型，并把 `breakout_monthly` 保留为观察窗 leader / 月频突破对照，而不是回到 `equal_elastic_monthly` 旧锚点。
- `2026-04-22 14:30 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 后，又执行 `.venv/bin/python scripts/update_hkconnect_artifacts.py`：当前 tracked winners 继续不变，`theme_monthly` 稳住 `2017 / 2020`，`theme_biweekly` 稳住 `2023 / 2025`，而四窗口 `robust_candidate` 被更正为 `theme_biweekly`。
- 这次重跑也再次确认了 sidecar challenger 顺位：`since_2020_01` 最接近主线的是 `hkconnect_path2_theme_biweekly`（`22.54% CAGR / -29.05% MaxDD / 0.9189 Sharpe / 15.03 Turnover`），而 `since_2023_01 / since_2025_01` 最接近主线的是 `hkconnect_path2_breakout_biweekly`（分别为 `43.97% / 137.81% CAGR`），但它们都没有改写当前 tracked winners。
- 因此本轮港股 `Path 2` 需要同步刷新 README / HISTORY / 港股对比图与 tracked winner 数据；下一轮继续围绕 `theme_monthly / theme_biweekly` 两条主线推进，并把 `breakout_monthly` 留作观察窗 leader / 月频突破对照。

## 本轮补充（2026-04-22 23:27 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 后，`results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明本轮没有新的港股 Path 2 artifact 漂移。
- 当前 tracked winners 继续维持：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`
  - `since_2023_01 / since_2025_01`：`hkconnect_path2_theme_biweekly`
  - `robust`：`hkconnect_path2_theme_biweekly`
- 当前 sidecar challenger 顺位也没有变化：`since_2020_01` 最接近主线的仍是 `hkconnect_path2_theme_biweekly`，`since_2023_01 / since_2025_01` 最接近主线的仍是 `hkconnect_path2_breakout_biweekly`，而 `since_2026_01` raw leader 继续是 `hkconnect_path2_breakout_monthly`。
- 下一轮继续围绕 `theme_monthly / theme_biweekly` 两条主线推进，把 `breakout_monthly` 只保留为观察窗 leader / 月频突破对照；在 `since_2020_01` 没有出现实质抬升前，不重新打开 `equal_elastic_monthly` 或新增候选族。

## 本轮补充（2026-04-23 01:32 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `.venv/bin/python scripts/update_hkconnect_artifacts.py`：港股 Path 2 tracked winners 与港股对比图都已按最新 comparison CSV 重写，但赢家本身没有变化。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；因此本轮结论仍是“确认稳定”，不是“出现新 winner”。
- 当前 tracked winners 继续维持：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`（`23.15% CAGR / -18.86% MaxDD / 1.1825 Sharpe / 6.64 Turn`）
  - `since_2023_01`：`hkconnect_path2_theme_biweekly`（`49.30% CAGR / -16.47% MaxDD / 1.5442 Sharpe / 14.46 Turn`）
  - `since_2025_01`：`hkconnect_path2_theme_biweekly`（`137.82% CAGR / -10.15% MaxDD / 2.5598 Sharpe / 15.28 Turn`）
  - `robust`：`hkconnect_path2_theme_biweekly`（`meanCAGR 58.05% / minCAGR 22.54%`）
- sidecar challenger 顺位依旧不变：`since_2020_01` 最接近主线的仍是 `hkconnect_path2_theme_biweekly`，而 `since_2023_01 / since_2025_01` 最接近主线的仍是 `hkconnect_path2_breakout_biweekly`；`since_2026_01` raw leader 继续是 `hkconnect_path2_breakout_monthly`（`190.38% CAGR / -4.77% MaxDD / 2.2531 Sharpe / 7.47 Turn`）。
- 下一轮继续围绕 `theme_monthly / theme_biweekly` 两条主线推进，保持 `breakout_monthly` 作为观察窗 leader / 月频突破对照；在 `since_2020_01` 没有实质抬升之前，不新增港股 Path 2 候选族。

## 本轮补充（2026-04-23 03:33 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 并执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`：缓存回退路径继续正常，港股 `Path 2` tracked winners 与 sidecar challenger 顺位没有任何漂移。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；因此本轮港股 `Path 2` 仍然只是确认性重跑，没有新的 artifact 漂移。
- 结论继续维持：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`
  - `since_2023_01 / since_2025_01`：`hkconnect_path2_theme_biweekly`
  - `robust`：`hkconnect_path2_theme_biweekly`
- `since_2026_01` raw leader 继续是 `hkconnect_path2_breakout_monthly`；下一轮仍以 `theme_monthly / theme_biweekly` 为港股 `Path 2` 主线，把 `breakout_monthly` 只保留为观察窗突破对照，不新增候选族。

## 本轮补充（2026-04-23 05:29 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 并执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`：缓存回退路径继续正常，港股 `Path 2` 的 tracked winners、`robust_candidate` 与 sidecar challenger 顺位继续完全不变。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；因此这轮港股 Path 2 仍只是确认稳定，而不是新的 winner / artifact 改写。
- 结论继续维持：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`
  - `since_2023_01 / since_2025_01`：`hkconnect_path2_theme_biweekly`
  - `robust`：`hkconnect_path2_theme_biweekly`
- `since_2026_01` raw leader 继续是 `hkconnect_path2_breakout_monthly`；下一轮仍以 `theme_monthly / theme_biweekly` 为港股 `Path 2` 主线，把 `breakout_monthly` 只保留为观察窗突破对照，不新增候选族。

## 本轮补充（2026-04-23 19:59 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 并执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`：缓存回退路径继续正常，但这次不再是纯确认重跑。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 已更新为 `64b36ccb6a6e8e2f2f6aa58f90d7bcaceddfff1c4252add7e9d5312c84567283` 与 `e6a839d2c4315bbe0691ad4d52ddc697ebeb846652d5bc5c2662212e5b9f27b5`；当前 tracked winners 改写为：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`（`23.65% CAGR / -18.86% MaxDD / 1.1944 Sharpe / 6.64 Turn`）
  - `since_2023_01`：`hkconnect_path2_theme_biweekly`（`49.09% CAGR / -16.47% MaxDD / 1.5382 Sharpe / 14.46 Turn`）
  - `since_2025_01`：`hkconnect_path2_breakout_biweekly`（`138.42% CAGR / -8.87% MaxDD / 2.1944 Sharpe / 18.58 Turn`）
  - `robust`：`hkconnect_path2_theme_biweekly`（`meanCAGR 57.74% / minCAGR 22.44%`）
- 这意味着 `since_2025_01` 的短窗口 tracked winner 已从 `hkconnect_path2_theme_biweekly` 切换到 `hkconnect_path2_breakout_biweekly`。新 winner 只在短窗口上占优：它同时改善了 `CAGR` 与 `MaxDD`，但 `Sharpe` 仍落后于 `theme_biweekly`，且换手更高，因此本轮只把它晋升为 2025-window tracked winner，不改写四窗口 `robust_candidate`。
- `since_2026_01` raw leader 仍是 `hkconnect_path2_breakout_monthly`，当前来到 `213.86% CAGR / -4.77% MaxDD / 2.4182 Sharpe / 7.47 Turn`。下一轮港股 `Path 2` 继续维持三条线并行：
  - `theme_monthly`：中长窗口锚点（`2017 / 2020`）
  - `theme_biweekly`：中窗口/鲁棒锚点（`2023 / robust`）
  - `breakout_biweekly`：新晋 `2025` 短窗口 winner

## 本轮补充（2026-04-24）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：港股 Path 2 的 tracked winners、`robust_candidate` 与实盘导出层都已同步到最新 payload，但赢家本身没有变化。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `a35621c7dfce801291e6c2482ef4a17a6071deeeb30a238adee9a34200bf98af` 与 `cc3c4429de9f026db201be9cee185fd388982488606045d104a1a59ddb938b72`；这轮变化主要来自完整 payload 重写和小幅指标漂移，不是新的 winner 改写。
- 当前 tracked winners 继续维持：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`（`23.41% CAGR / -18.86% MaxDD / 1.1891 Sharpe / 6.64 Turn`）
  - `since_2023_01`：`hkconnect_path2_theme_biweekly`（`48.66% CAGR / -16.47% MaxDD / 1.5256 Sharpe / 14.46 Turn`）
  - `since_2025_01`：`hkconnect_path2_breakout_biweekly`（`137.32% CAGR / -8.87% MaxDD / 2.1812 Sharpe / 18.58 Turn`）
  - `robust`：`hkconnect_path2_theme_biweekly`（`meanCAGR 57.09% / minCAGR 22.22%`）
- `since_2026_01` raw leader 仍是 `hkconnect_path2_breakout_monthly`，当前为 `197.67% CAGR / -4.77% MaxDD / 2.3069 Sharpe / 7.47 Turn`。下一轮港股 `Path 2` 继续维持 `theme_monthly / theme_biweekly / breakout_biweekly` 三条主线，不新增候选族。

## 本轮补充（2026-04-25）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 继续走本地缓存回退路径，但港股 `Path 2` 的 tracked winners 与 sidecar 顺位都没有变化。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `893542dd28ae208a115a22d48f19bd1448bf2b30606892a825cb955aed7a3575` 与 `422d42394fa8731e51526973081debb58c6b537174485238018de37110589355`；这轮同样是 `sample_end=2026-04-24` 下的小幅指标漂移同步，不是新的 winner 改写。
- 当前 tracked winners 继续维持：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`（`23.33% CAGR / -18.86% MaxDD / 1.1874 Sharpe / 6.64 Turn`）
  - `since_2023_01`：`hkconnect_path2_theme_biweekly`（`48.92% CAGR / -16.47% MaxDD / 1.5334 Sharpe / 14.46 Turn`）
  - `since_2025_01`：`hkconnect_path2_breakout_biweekly`（`136.68% CAGR / -8.87% MaxDD / 2.1734 Sharpe / 18.58 Turn`）
  - `robust`：`hkconnect_path2_theme_biweekly`（`meanCAGR 57.66% / minCAGR 22.70%`）
- `since_2026_01` raw leader 仍是 `hkconnect_path2_breakout_monthly`，当前为 `188.57% CAGR / -4.77% MaxDD / 2.2393 Sharpe / 7.47 Turn`。
- 下一轮港股 `Path 2` 继续维持 `theme_monthly / theme_biweekly / breakout_biweekly` 三条主线，不新增候选族；本轮只把 README / HISTORY 与港股 tracked payload 同步到最新数值。

## 本轮补充（2026-04-26）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：缓存回退路径继续正常，港股 `Path 2` 的 tracked winners、`robust_candidate` 与 sidecar 顺位都没有变化。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `54097028c3eaea664cb74a26890358c0ff5934a75943a3b0c591655fc4c9efbc` 与 `6ee86d107dc61a23e9b0ef45b839507a34bca7f9a86139c0ee3cb365d0dfe2e8`；这轮同样是 `sample_end=2026-04-24` 下的小幅指标漂移同步，不是新的 winner 改写。
- 当前 tracked winners 继续维持：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`（`23.89% CAGR / -18.86% MaxDD / 1.2055 Sharpe / 6.62 Turn`）
  - `since_2023_01`：`hkconnect_path2_theme_biweekly`（`48.92% CAGR / -16.47% MaxDD / 1.5334 Sharpe / 14.46 Turn`）
  - `since_2025_01`：`hkconnect_path2_breakout_biweekly`（`136.68% CAGR / -8.87% MaxDD / 2.1734 Sharpe / 18.58 Turn`）
  - `robust`：`hkconnect_path2_theme_biweekly`（`meanCAGR 57.71% / minCAGR 22.79%`）
- `since_2026_01` raw leader 仍是 `hkconnect_path2_breakout_monthly`，当前为 `188.57% CAGR / -4.77% MaxDD / 2.2393 Sharpe / 7.47 Turn`。下一轮继续维持 `theme_monthly / theme_biweekly / breakout_biweekly` 三条主线，不新增港股候选族；本轮只做 tracked payload、README 港股摘要与港股对比图的 sync-only 刷新。

## 本轮补充（2026-04-27）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：缓存回退路径继续正常，这次同步的重点是把主分支里误写成 `2026-04-30` 月频锚点的 `Path 2` 结论纠回当前真实缓存口径。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `54097028c3eaea664cb74a26890358c0ff5934a75943a3b0c591655fc4c9efbc` 与 `6ee86d107dc61a23e9b0ef45b839507a34bca7f9a86139c0ee3cb365d0dfe2e8`；当前 tracked winners 继续维持：
  - `since_2017_01 / since_2020_01`：`hkconnect_path2_theme_monthly`（`23.89% CAGR / -18.86% MaxDD / 1.2055 Sharpe / 6.62 Turn`）
  - `since_2023_01`：`hkconnect_path2_theme_biweekly`（`48.92% CAGR / -16.47% MaxDD / 1.5334 Sharpe / 14.46 Turn`）
  - `since_2025_01`：`hkconnect_path2_breakout_biweekly`（`136.68% CAGR / -8.87% MaxDD / 2.1734 Sharpe / 18.58 Turn`）
  - `robust`：`hkconnect_path2_theme_biweekly`（`meanCAGR 57.71% / minCAGR 22.79%`）
- 这意味着当前港股 `Path 2` 的默认锚点并没有回到月频全覆盖，而是继续保持 `theme_monthly / theme_biweekly / breakout_biweekly` 的分工结构；`since_2026_01` raw leader 仍是 `hkconnect_path2_breakout_monthly`（`188.57% CAGR / -4.77% MaxDD / 2.2393 Sharpe / 7.47 Turn`）。
- 下一轮港股 `Path 2` 继续维持 `theme_monthly / theme_biweekly / breakout_biweekly` 三条主线，不新增港股候选族，也不把 `biweekly / weekly` 从当前 tracked winner 结构中移除。

## 本轮补充（2026-04-27 09:08 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 在线更新依旧失败，但离线缓存已经把港股 Path 2 payload 真正推进到 `sample_end=2026-04-30`。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 已更新为 `83885b39cb11f568d0ce2772e4cbaa9a0c6c1b62c089127e89eb39bbba12ceed` 与 `d5d3bc0cf9a03aeb713d76efd76d2687be6d0d47f65f784dcd12734bf1062d4f`；这意味着上一条“纠回 2026-04-24 月频锚点”的结论已被新的月末缓存扩展覆盖。
- 当前 tracked winners 已改写为：
  - `since_2017_01 / since_2020_01 / since_2023_01`：`hkconnect_path2_theme_monthly`
  - `since_2025_01`：`hkconnect_path2_breakout_monthly`
  - `robust`：`hkconnect_path2_theme_monthly`
- 关键指标同步为：
  - `since_2020_01`：`22.79% CAGR / -18.86% MaxDD / 1.1654 Sharpe / 6.62 Turn`
  - `since_2023_01`：`32.43% CAGR / -16.07% MaxDD / 1.4541 Sharpe / 6.01 Turn`
  - `since_2025_01`：`99.22% CAGR / -7.72% MaxDD / 2.6848 Sharpe / 8.62 Turn`
  - `robust_candidate`：`hkconnect_path2_theme_monthly`（`meanCAGR 38.73% / minCAGR 22.79%`）
- 这说明在样本真正推进到 `2026-04-30` 后，`theme_biweekly / breakout_biweekly` 的 tracked 结构不再成立；下一轮港股 `Path 2` 继续以 `theme_monthly` 作为中长窗口与鲁棒锚点，把 `breakout_monthly` 保留为 `since_2025_01 / since_2026_01` 的短窗口与观察窗 leader，`biweekly / weekly` 版本降回 challenger，不新增候选族。

## 本轮补充（2026-04-27 18:09 CST）

- 本轮在主工作树直接运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`。这次回测把港股 Path 2 摘要从 stale `2026-04-30` 文案纠回当前真实 tracked payload：`as_of=2026-04-24`，月频样本止于 `2026-03-31`。
- 当前 Path 2 tracked winners 为：
  - `since_2017_01 / since_2020_01 / since_2023_01`：`hkconnect_path2_theme_monthly`
  - `since_2025_01`：`hkconnect_path2_breakout_monthly`
  - `robust`：`hkconnect_path2_equal_elastic_monthly`
- 关键指标同步为：
  - `since_2020_01`：`21.17% CAGR / -18.86% MaxDD / 1.1011 Sharpe / 6.64 Turn`
  - `since_2023_01`：`29.77% CAGR / -16.07% MaxDD / 1.3587 Sharpe / 6.04 Turn`
  - `since_2025_01`：`94.85% CAGR / -7.72% MaxDD / 2.5222 Sharpe / 8.65 Turn`
  - `robust_candidate`：`hkconnect_path2_equal_elastic_monthly`（`meanCAGR 36.01% / minCAGR 17.59% / worstMaxDD -38.60%`）
- `since_2026_01` 仍只做观察窗：当前 raw leader 是 `hkconnect_path2_breakout_monthly`（`197.40% CAGR / -4.77% MaxDD / 1.6881 Sharpe / 7.10 Turn`）。下一轮继续以 `theme_monthly` 作为中长窗口锚点、`breakout_monthly` 作为短窗口/观察窗锚点，`equal_elastic_monthly` 只作为 robust payload 的当前胜出者保留；不新增港股候选族。
