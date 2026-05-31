# 沪港通 Path 2 研究计划

## 本轮执行计划（2026-06-01 04:18 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `v13_terminal` 确认 inverse elastic 支线终止复核失败。本轮虽然 rotation 仍给 `biweekly_breakout`，plan 已把该 focus 映射为失败支线终止/不重启普通 breakout，因此新增预算转回主题月频高收益修复池，注册 `v14_signal_guard`，目标是维持 2017 MaxDD 小于 `25%` 并把 2023 推近 `30%`。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v14_signal_guard`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `v14_signal_guard` 五窗口 CAGR 为 `20.75% / 25.57% / 27.62% / 61.73% / 65.66%`，最大回撤为 `-23.20% / -17.07% / -13.37% / -10.22% / -9.49%`，换手为 `5.53x / 5.28x / 5.43x / 6.08x / 5.55x`。它继续满足 2017 回撤门槛并保持 2025/2026，但 2023 仍低于 `30%`，不替换 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 window winner/robust/tracked 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`；HK comparison 图刷新。候选池未触发 HK explore cap evict。
- 下一轮 focus 仍可能报 `biweekly_breakout`；本 plan 继续将其映射为失败支线，不重启普通 breakout。第一条命令若必须响应该 focus，只做一个更严格 terminal check；若跳过失败支线，则直接回到主题月频 `v15` 的 2023 收益修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_terminal_or_theme_v15_id>`。

## 本轮执行计划（2026-05-31 22:26 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `v13_return_guard` 回到主题月频修复池但 2023 仍未达 `30%`。本轮因 rotation 指向 `elasticity_cost_control`，只做一次更严格 inverse elastic 终止复核 `v13_terminal`，验收仍是 `since_2023_01 >= 15%` 且长窗 MaxDD 低于 `30%`。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v13_terminal`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `v13_terminal` 五窗口 CAGR 为 `10.72% / 10.08% / 9.36% / 49.86% / 15.12%`，最大回撤为 `-37.42% / -37.42% / -31.62% / -11.82% / -11.82%`，换手为 `4.59x / 4.44x / 5.10x / 5.94x / 6.66x`。它低于 `v12_terminal` 的 2023，且长窗回撤继续穿 `30%`，inverse elastic 支线终止复核失败。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 window winner/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`；候选池未触发 HK explore cap evict。结论：`elasticity_cost_control` 不再追加普通参数，后续只保留历史对照。
- 下一轮第一条命令应转回主题月频高收益修复池，目标 `since_2023_01 >= 30%` 且 2017 MaxDD 不劣于 `-25%`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_theme_monthly_v14_repair_id>`。

## 本轮执行计划（2026-05-31 16:20 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `inverse_elastic_monthly_cost_guard_v12_terminal` 终止复核失败，本轮按 `high_return_monthly` 回到主题月频高收益修复池，新增 `v13_return_guard`，目标是保持 2017 MaxDD 小于 `25%` 并把 2023 向 `30%` 验收线拉近。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v13_return_guard`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v13_return_guard`。
- `v13_return_guard` 五窗口 CAGR 为 `20.61% / 25.48% / 27.60% / 61.74% / 65.55%`，最大回撤为 `-23.36% / -16.93% / -13.22% / -10.22% / -9.49%`，换手为 `5.52x / 5.27x / 5.42x / 6.08x / 5.57x`。它相对 v12 明显修复 2026 并保持 2017 回撤门槛，但 2023 仍低于 `30%`，不替换 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 window winner、robust/tracked 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `biweekly_breakout`。本 plan 继续把该 focus 映射为失败支线终止复核，不重启普通 breakout；第一条命令只允许更严格终止检查，若仍失败则预算回到 `v13` 的 2023 收益修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_terminal_or_v14_id>`。

## 本轮执行计划（2026-05-31 10:26 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 plan 说明 inverse elastic 只允许一次终止复核。本轮按 `elasticity_cost_control` 新增 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v12_terminal`，验收线仍是 `since_2023_01 >= 15%` 且长窗 MaxDD 低于 `30%`。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v12_terminal`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `inverse_elastic_monthly_cost_guard_v12_terminal` 五窗口 CAGR 为 `11.28% / 11.17% / 9.60% / 50.72% / 21.87%`，最大回撤为 `-36.27% / -36.27% / -32.35% / -11.41% / -10.28%`，换手为 `4.76x / 4.62x / 5.25x / 6.16x / 6.72x`。它低于 v11 的 2023 收益且长窗回撤仍穿 `30%`，inverse elastic 支线终止复核失败，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 window winner、robust/tracked 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `high_return_monthly`。第一条命令应把新增预算转回主题月频高收益修复池，目标 `since_2023_01 >= 30%` 且 2017 MaxDD 不劣于 `-25%`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`。

## 本轮执行计划（2026-05-31 04:21 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮建议把新增预算转回主题月频高收益修复池。本轮新增 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v12_drawdown_guard`，目标是保持 2025/2026 正收益并把 2017 MaxDD 控在 `-25%` 内。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v12_drawdown_guard`。实际 HK 增量命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v12_drawdown_guard`。
- `theme_monthly_reconfirm_high_return_cost_control_v12_drawdown_guard` 五窗口 CAGR 为 `21.05% / 26.52% / 26.26% / 61.05% / 54.36%`，最大回撤为 `-23.91% / -15.30% / -13.01% / -10.86% / -10.43%`，换手为 `5.33x / 5.04x / 5.28x / 5.98x / 5.40x`。v12 修复 2017 回撤门槛并保留短窗正收益，但 2023 仍未达到 `30%`，不替换 HK Path 2 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `elasticity_cost_control`。由于 inverse elastic 多轮终止复核失败，下一轮若必须响应 focus，只测一次更严格 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v12_terminal`；若 2023 仍低于 `15%` 或长窗 MaxDD 超过 `30%`，预算转回 `v12` 的 2023 收益修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_terminal_or_v13_id>`。

## 本轮执行计划（2026-05-30 22:20 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮要求对 `elasticity_cost_control` 做最后终止复核。本轮新增 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v11_terminal`，要求 `since_2023_01 >= 15%` 且长窗 MaxDD 低于 `30%`。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v11_terminal`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `inverse_elastic_monthly_cost_guard_v11_terminal` 五窗口 CAGR 为 `13.14% / 13.04% / 11.23% / 56.71% / 26.61%`，最大回撤为 `-35.97% / -35.97% / -32.91% / -10.62% / -8.91%`，换手为 `4.94x / 4.80x / 5.39x / 6.14x / 6.77x`。它未达到 2023 和长窗回撤验收线，inverse elastic 支线继续不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `high_return_monthly`。第一条命令建议把新增预算转回主题月频高收益修复池，目标 `since_2023_01 >= 30%` 且 2017 MaxDD 不劣于 `-25%`，例如 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v12_drawdown_guard`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`。

## 本轮执行计划（2026-05-30 16:22 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 inverse elastic v10 终止复核失败。本轮按 `high_return_monthly` 回到主题月频高收益修复池，新增 v11，目标是让 `since_2023_01` 稳定到 `27%+` 且 worst MaxDD 不劣于 `-25%`。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v11`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit32_v5,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v11,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover3_exit42`。
- `theme_monthly_reconfirm_high_return_cost_control_v11` 五窗口 CAGR 为 `20.84% / 26.53% / 28.84% / 63.79% / 62.21%`，最大回撤为 `-25.10% / -18.04% / -12.26% / -10.07% / -9.94%`，换手为 `5.60x / 5.33x / 5.44x / 6.05x / 5.52x`。v11 达到 2023 验收线并保持 2025/2026 正收益，但 2017 MaxDD 略穿 `-25%` 且 2017/2020 仍低于 `theme_monthly_cost_control` robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `elasticity_cost_control`。由于 inverse elastic v10 已失败，第一条命令只建议做一次更严格的终止复核，例如 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v11_terminal`，要求 `since_2023_01 >= 15%` 且 long-window MaxDD 低于 `30%`；若仍失败，新增预算转回 v11 的回撤修复版：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_terminal_or_drawdown_guard_id>`。

## 本轮执行计划（2026-05-30 10:17 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 plan 已提示 inverse elastic v9 终止复核失败，但 final rotation 仍给出 `elasticity_cost_control`。本轮只做一次更低集中度的 inverse elastic v10 复核，不扩普通 breakout。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v10`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v4,hkconnect_path2_inverse_elastic_monthly_cost_guard_v10,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover3_exit44`。
- `inverse_elastic_monthly_cost_guard_v10` 五窗口 CAGR 为 `13.92% / 13.00% / 10.23% / 53.90% / 31.53%`，最大回撤为 `-37.62% / -37.62% / -33.92% / -10.53% / -8.20%`，换手为 `5.12x / 4.99x / 5.55x / 6.18x / 6.44x`。v10 保留短窗正收益，但 2023 与长窗回撤继续低于验收线，elasticity_cost_control 支线不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict；HK comparison 图已刷新。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `high_return_monthly`。inverse elastic v10 终止复核失败后，第一条命令建议注册并确认 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v11`，目标是 `since_2023_01 >= 27%` 且 worst MaxDD 不劣于 `-25%`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_theme_monthly_v11_id>`。

## 本轮执行计划（2026-05-30 04:31 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `inverse_elastic_monthly_cost_guard_v9` 终止复核失败，本轮按 plan 转回主题月频修复池，新增 `theme_monthly_reconfirm_high_return_cost_control_v10`，目标是继续抬高 `since_2023_01` 且保留 2025/2026 正收益。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v10`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v10`。
- `theme_monthly_reconfirm_high_return_cost_control_v10` 五窗口 CAGR 为 `21.17% / 26.28% / 26.69% / 64.35% / 51.76%`，最大回撤为 `-22.37% / -16.68% / -13.95% / -10.87% / -10.83%`，换手为 `5.42x / 5.16x / 5.32x / 6.03x / 5.34x`。v10 相对 v9 略改善 2017/2020/2023，但仍低于 `theme_monthly_cost_control` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict；HK comparison 图已刷新。
- 最终 guard 为 `pass`，下一轮 focus 为 `biweekly_breakout`。本 plan 继续把该 focus 映射为“失败支线只允许终止复核，不重启普通 breakout”；若必须响应 focus，第一条命令只测 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit26_risk15`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_terminal_check_id>`；若仍失败，预算转回 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v11`。

## 本轮执行计划（2026-05-29 22:21 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 plan 要求对 `elasticity_cost_control` 做终止复核。本轮新增 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v9`，要求至少把 `since_2023_01` 拉回 `15%` 附近且长窗回撤低于 `30%`。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v9`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_inverse_elastic_monthly_cost_guard_v9`。
- `inverse_elastic_monthly_cost_guard_v9` 五窗口 CAGR 为 `15.62% / 15.50% / 13.06% / 61.92% / 28.32%`，最大回撤为 `-36.24% / -36.24% / -36.30% / -9.74% / -7.33%`，换手为 `5.34x / 5.13x / 5.69x / 6.40x / 6.76x`。v9 保留 2025/2026 正弹性，但 2023 未达标且长窗回撤仍超过 `30%`，弹性成本线继续不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict；HK comparison 图已刷新。
- 最终 guard 为 `pass`，下一轮 focus 仍为 `elasticity_cost_control`。由于 v9 终止复核失败，第一条命令建议转回主题月频修复池，而不是继续 inverse elastic：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v10`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_theme_monthly_v10_id>`。

## 本轮执行计划（2026-05-29 16:33 CST）

- 开局 HK coverage 为 complete；上一轮 `breakout_cost_guard_biweekly_defensive_cashguard_exit28_risk20` 继续确认双周 breakout 失败支线应终止。本轮按 plan 把预算转回 `high_return_monthly`，新增主题月频高收益修复 v9，目标是让 `since_2023_01` 回到 `25%+`，同时保留 2025/2026 正收益。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v9`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v9`。
- `theme_monthly_reconfirm_high_return_cost_control_v9` 五窗口 CAGR 为 `21.04% / 26.07% / 26.55% / 64.35% / 51.76%`，最大回撤为 `-22.50% / -16.17% / -13.97% / -10.87% / -10.83%`，换手为 `5.39x / 5.12x / 5.29x / 6.03x / 5.34x`。v9 相对 v8 把 2023 提到 `25%+`，但 2017/2020 仍低于 `theme_monthly_cost_control` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict；HK comparison 图已刷新。
- 最终 guard 为 `pass`，下一轮 focus 为 `biweekly_breakout`。本 plan 继续把该 focus 映射为“普通 breakout 不再扩展，只允许终止复核或跳过”；若必须响应，第一条命令只测 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit26_risk15`，否则优先把预算用于 `theme_monthly_reconfirm_high_return_cost_control_v10`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_terminal_or_theme_v10_id>`。

## 本轮执行计划（2026-05-29 10:22 CST）

- 开局 guard 为 `pass`；上一轮 `theme_monthly_reconfirm_high_return_cost_control_v8` 仍低于 2023 验收线，本轮按 `biweekly_breakout` 的失败支线终止复核，只测更低 `exit28/risk20` 的强防守双周 breakout，不重启普通 breakout 邻域。HK 缓存到 2026-05-27，`--end-date 2026-05-28` 准备保护失败后改用 `--end-date 2026-05-27`。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit28_risk20`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit28_risk20`。
- `exit28_risk20` 五窗口 CAGR 为 `0.34% / -3.51% / -1.35% / 30.40% / -23.16%`，最大回撤为 `-60.30% / -60.30% / -37.07% / -15.20% / -10.21%`，换手为 `13.35x / 13.17x / 15.11x / 20.11x / 19.81x`。结果确认双周 breakout 支线即使强现金防守仍无法修复长窗深回撤和 2026 负收益，应终止该支线扩展。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `elasticity_cost_control`。第一条命令建议回到月频弹性成本线，只测一个更严格的终止复核，例如 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v9`，要求 `since_2023_01 >= 15%` 且 long-window MaxDD 低于 `30%`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_next_id>`；若仍失败，预算转回主题月频修复池。

## 本轮执行计划（2026-05-29 04:17 CST）

- 开局 guard 为 `pass`；上一轮 `inverse_elastic_monthly_cost_guard_v8` 2023 与长窗回撤继续失败，本轮按 `high_return_monthly` 回到主题月频高收益修复池，新增 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v8`，目标是保留 2025/2026 强收益同时让 2023 接近验收线。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v8`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v8`。
- `theme_monthly_reconfirm_high_return_cost_control_v8` 五窗口 CAGR 为 `18.95% / 23.32% / 21.97% / 56.67% / 49.38%`，最大回撤为 `-25.12% / -16.72% / -13.23% / -10.91% / -10.66%`，换手为 `5.29x / 5.06x / 5.29x / 5.67x / 5.08x`。v8 保持 2025/2026 正收益和可控回撤，但 2023 仍低于 `25%` 验收线，2017/2020 也不及 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `163/163 complete`，下一轮 focus 轮换为 `biweekly_breakout`。该 focus 继续映射为“失败支线只允许终止复核”，不重启普通 breakout；若必须响应，第一条命令只测更低风险/更低退出的 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit28_risk20`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_terminal_check_id>`；若继续失败，新增预算转回主题月频修复池 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v9`。

## 本轮执行计划（2026-05-28 22:19 CST）

- 开局 guard 为 `pass`；上一轮 `theme_monthly_reconfirm_high_return_cost_control_v7` 保持短窗强但 2023 未达验收线，本轮按 `elasticity_cost_control` 注册 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v8`，继续设置 2023 稳定性和长窗回撤为主要验收。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v8`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_inverse_elastic_monthly_cost_guard_v8`。
- `inverse_elastic_monthly_cost_guard_v8` 五窗口 CAGR 为 `13.32% / 13.69% / 8.61% / 63.09% / 35.60%`，最大回撤为 `-35.86% / -35.86% / -32.24% / -11.15% / -7.67%`，换手为 `5.10x / 5.00x / 5.60x / 6.08x / 6.64x`。v8 保留 2025/2026 正弹性，但 2023 更弱且长窗回撤超过 `30%`，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `160/160 complete`，下一轮 focus 仍为 `elasticity_cost_control`。第一条命令建议只做一个更严格的弹性成本终止复核，例如 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v9`，要求 `since_2023_01` 至少回到 `15%` 且 long-window MaxDD 低于 `30%`；五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_next_id>`。若仍失败，后续新增预算转回主题月频修复池。

## 本轮执行计划（2026-05-28 16:18 CST）

- 开局 guard 为 `pass`；上一轮强约束双周 breakout 最后复核失败，本轮按 `high_return_monthly` 回到主题月频高收益修复池，新增 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v7`。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v7`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v7`。
- `theme_monthly_reconfirm_high_return_cost_control_v7` 五窗口 CAGR 为 `19.28% / 24.90% / 23.93% / 65.61% / 58.64%`，最大回撤为 `-26.73% / -17.49% / -12.75% / -10.05% / -9.91%`，换手为 `5.57x / 5.34x / 5.51x / 5.87x / 5.25x`。v7 保持 2025/2026 强正收益和可控回撤，但 2023 仍低于 `25%` 验收线，且 2017/2020 不及 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `157/157 complete`，下一轮 focus 仍为 `biweekly_breakout`。该 focus 继续映射为“失败支线只允许终止复核”，不重启普通 breakout；若必须响应，第一条命令只测更低风险/出场的 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit28_risk20`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_terminal_check_id>`；若继续失败，新增预算转回主题月频修复池。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `exit32/risk30` 的强约束双周 breakout 仍失败，本轮按 plan 中“最后复核池”完成更低 `exit30/risk25`，不重启普通双周 breakout 邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit30_risk25`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `breakout_cost_guard_biweekly_defensive_cashguard_exit30_risk25` 五窗口 CAGR 为 `0.70% / -3.26% / -1.34% / 30.39% / -23.16%`，最大回撤为 `-59.85% / -59.85% / -37.36% / -15.20% / -10.21%`，换手为 `13.53x / 13.37x / 15.29x / 20.11x / 19.81x`。结果确认双周 breakout 即使强防守也无法修复长窗深回撤和 2026 负收益，本支线仅保留为失败对照。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 为 `high_return_monthly`。第一条命令建议停止扩普通 breakout，回到主题月频高收益修复池，并设置 `2023>=25% / worstDD>-25%` 验收线，例如 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v7`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`；若 2023 仍低于门槛，再回到 elastic 月频成本线而不是双周 breakout。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；当前 guard focus 为 `biweekly_breakout`，本轮按 plan 中“失败支线强约束最后复核池”继续确认更低 `exit32/risk30`，不重启普通双周 breakout 参数邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit32_risk30`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `breakout_cost_guard_biweekly_defensive_cashguard_exit32_risk30` 五窗口 CAGR 为 `1.03% / -2.85% / -1.38% / 31.02% / -23.16%`，最大回撤为 `-59.07% / -59.07% / -37.83% / -14.71% / -10.21%`，换手为 `13.71x / 13.55x / 15.41x / 20.02x / 19.81x`。结果确认更强防守仍无法修复长窗深回撤和 2026 负收益，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 仍给 `biweekly_breakout` focus；本 plan 将该 focus 映射为“只允许强约束失败复核，不做普通 breakout 扩展”。下一轮第一条命令若必须响应 focus，仅测最后一个更低谨慎仓对照 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit30_risk25`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_last_check_id>`；若仍失败，应把后续新增预算转回 `high_return_monthly`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`；上一轮 `theme_monthly_reconfirm_high_return_cost_control_v6` 保持 2025/2026 强正收益但未改善 robust，本轮按 `elasticity_cost_control` 测试 inverse elastic 月频成本 v7，并设置 2023 不低于 `25%` 的验收线。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v7`。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `inverse_elastic_monthly_cost_guard_v7` 五窗口 CAGR 为 `16.89% / 18.24% / 11.05% / 71.73% / 45.36%`，最大回撤为 `-35.21% / -35.21% / -34.90% / -9.95% / -6.43%`，换手为 `5.25x / 5.17x / 5.70x / 6.05x / 6.73x`。v7 继续保留短窗弹性，但 2023 收益显著低于验收线且长窗回撤超过 `30%`，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化，robust 仍为 `hkconnect_path2_theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 转为 `high_return_monthly`。第一条命令建议回到主题月频高收益修复池，而不是继续扩 elastic，测试 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v7` 或同等 `2023>=25% / worstDD>-25%` 版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮 `inverse_elastic_monthly_cost_guard_v6` 保留短窗弹性但 2023 和长窗回撤弱，本轮按 `high_return_monthly` 回到主题月频修复池，新增 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v6`，不并入 A股 winner 结论。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v6`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v6,hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit64`。
- `theme_monthly_reconfirm_high_return_cost_control_v6` 五窗口 CAGR 为 `19.63% / 25.60% / 24.23% / 62.17% / 68.70%`，最大回撤 `-25.59% / -16.44% / -13.77% / -8.70% / -8.32%`，换手 `5.69x / 5.43x / 5.57x / 6.00x / 5.53x`。v6 保持 2025/2026 强正收益和浅回撤，但 2017/2020/2023 仍低于 `theme_monthly_cost_control` robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：robust 仍为 `hkconnect_path2_theme_monthly_cost_control`，四窗口 meanCAGR `37.46%`、minCAGR `22.42%`、worstMaxDD `-25.34%`、meanTurn `5.86x`；候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，下一轮 focus 转为 `elasticity_cost_control`。第一条命令建议只测一个带 2023 验收线的弹性成本版，例如 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v7`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_next_id>`；若 2023 仍低于 `25%` 或长窗回撤超过 `30%`，继续回到主题月频修复池。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮 `theme_monthly_reconfirm_high_return_cost_control_v5` 强化 2025/2026 但未改善 robust，本轮按 `elasticity_cost_control` 新增 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v6`，继续作为 HK 独立研究线，不并入 A股 winner 结论。实际 HK 合并命令见 HK Path 1 本轮记录。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v6`。五窗口 CAGR 为 `17.23% / 18.42% / 13.56% / 74.66% / 49.79%`，最大回撤 `-34.06% / -34.06% / -35.09% / -7.96% / -5.35%`，换手 `5.86x / 5.71x / 6.30x / 6.43x / 7.12x`。v6 保留 2025/2026 弹性，但 2023 收益和长窗回撤仍明显弱于 `theme_monthly_cost_control` robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：robust 仍为 `hkconnect_path2_theme_monthly_cost_control`，四窗口 meanCAGR `37.46%`、minCAGR `22.42%`、worstMaxDD `-25.34%`、meanTurn `5.86x`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `high_return_monthly`。下一轮第一条命令建议回到主题月频高收益修复池，并设置 2023 不塌的验收线，例如 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v6`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`；若 2023 仍低于 `25%`，继续回到 robust 邻域而不是扩双周 breakout。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；上一轮要求回到 `high_return_monthly` 修复池，本轮新增 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v5`，不并入 A股 winner 结论。实际 HK 合并命令见 HK Path 1 本轮记录，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v5`。五窗口 CAGR 为 `19.90% / 26.34% / 26.30% / 66.54% / 78.22%`，最大回撤 `-26.68% / -18.77% / -13.60% / -10.01% / -7.35%`，换手 `5.90x / 5.68x / 5.69x / 6.13x / 5.82x`。v5 相对 v4 继续强化 2026 与 2025，但 2017/2020 仍低于 `theme_monthly_cost_control` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `elasticity_cost_control`。下一轮第一条命令建议从月频弹性成本线验证能否保留 v5 的 2026 强度但提高 2023 稳定性，例如 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v6`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_next_id>`；若 2023 仍低于 `25%` 或长窗回撤超过 `30%`，继续回到主题月频高收益修复池。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮 plan 将 `biweekly_breakout` 限定为失败支线的强约束最后复核，本轮只测更低退出和更强谨慎仓的 `exit34/risk35`，不重启普通双周 breakout 阈值邻域。命令类型为 HK 五窗口 `--only-strategy-ids` 增量确认，实际合并命令见 HK Path 1 本轮记录。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit34_risk35`。五窗口 CAGR 为 `1.28% / -2.60% / -1.38% / 31.02% / -23.16%`，最大回撤 `-58.39% / -58.39% / -37.85% / -14.71% / -10.21%`，换手 `13.90x / 13.75x / 15.57x / 20.02x / 19.81x`。
- 该结果确认双周 breakout 即使强现金/防守约束仍无法修复长窗深回撤和 2026 负收益；只保留为失败对照，不再扩普通 breakout 邻域。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `high_return_monthly`。下一轮第一条命令建议回到主题月频高收益修复池，并设置 2023 不塌的验收线，例如 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v5` 或同等低回撤版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮强约束双周 breakout 继续失败，本轮没有重启普通 breakout 阈值邻域，而是按 `high_return_monthly` 回到主题月频修复池，新增 `hkconnect_path2_theme_monthly_high_return_cost_control_v4`。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_high_return_cost_control_v4`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_monthly_high_return_cost_control_v4` 五窗口 CAGR 为 `19.45% / 25.33% / 24.13% / 62.17% / 68.70%`，最大回撤 `-25.64% / -16.21% / -13.77% / -8.70% / -8.32%`，换手 `5.68x / 5.42x / 5.57x / 6.00x / 5.53x`。它较 v3 改善 2020/2025/2026，且 2026 转为强正收益，但 2017/2020/2023 仍低于 `theme_monthly_cost_control` robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `biweekly_breakout`。该 focus 继续映射为失败支线的强约束最后复核池，不做普通阈值邻域；第一条命令若必须响应 focus，建议只测 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit34_risk35`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_last_check_id>`；若仍失败，继续回到主题月频高收益修复池。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮 plan 已把 `biweekly_breakout` 限定为失败支线最后复核，本轮只新增更强防守/更低谨慎仓的 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit36_risk35`，不重启普通 breakout 阈值邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit36_risk35`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `breakout_cost_guard_biweekly_defensive_cashguard_exit36_risk35` 五窗口 CAGR 为 `0.98% / -2.88% / -1.47% / 31.00% / -23.16%`，最大回撤 `-58.50% / -58.50% / -38.04% / -14.71% / -10.21%`，换手 `13.87x / 13.70x / 15.52x / 20.02x / 19.81x`。更强防守仍不能修复长窗深回撤和 2026 负收益，双周 breakout 支线继续暂停普通探索。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `elasticity_cost_control`。下一轮第一条命令建议回到月频弹性成本控制，但设置 2023 收益门槛，例如 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v6` 或回到 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v4`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_next_id>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`，上一轮强约束双周 breakout 继续失败；本轮按 `elasticity_cost_control` 回到月频弹性成本控制，新增 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v5`，不重启普通双周 breakout 邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v5`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `inverse_elastic_monthly_cost_guard_v5` 五窗口 CAGR 为 `18.75% / 21.36% / 17.38% / 84.64% / 69.49%`，最大回撤 `-34.66% / -34.66% / -36.33% / -8.47% / -5.57%`，换手 `6.24x / 6.05x / 6.55x / 6.69x / 7.32x`。它保留 2025/2026 高弹性，但 2023 CAGR 与长窗回撤仍明显弱于 `theme_monthly_cost_control` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `biweekly_breakout`。该 focus 已映射为失败支线的强约束复核池，不做普通阈值邻域；下一轮第一条命令若必须响应 focus，只测一个更强防守/更低换手的最后复核，例如 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit36_risk35`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_last_check_id>`；若仍失败，继续回到主题月频高收益修复池 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v4`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `biweekly_breakout` 且 plan 已限制为强约束最后复核；本轮只补一条更低退出、更低谨慎仓的双周 breakout 复核，不重启普通阈值邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit38_risk40`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `breakout_cost_guard_biweekly_defensive_cashguard_exit38_risk40` 五窗口 CAGR 为 `1.09% / -2.79% / -1.75% / 31.00% / -23.16%`，最大回撤 `-58.23% / -58.23% / -38.62% / -14.71% / -10.21%`，换手 `14.06x / 13.90x / 15.68x / 20.02x / 19.81x`。更强防守仍无法修复长窗深回撤和 2026 负收益，双周 breakout 支线继续暂停普通探索。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 为 `elasticity_cost_control`。下一轮第一条命令建议回到月频弹性成本控制并设置 2023 不低于 `25%` 的验收线，例如 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v5`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_next_id>`；若仍低于门槛，继续回到主题月频修复池。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `high_return_monthly`；本轮按计划新增 `hkconnect_path2_theme_monthly_high_return_cost_control_v3`，继续在主题月频高收益修复池内确认，不重启普通双周 breakout 邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_high_return_cost_control_v3`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_monthly_high_return_cost_control_v3` 五窗口 CAGR 为 `18.60% / 23.19% / 21.67% / 54.29% / 41.19%`，最大回撤 `-25.18% / -16.03% / -12.78% / -11.00% / -10.96%`，换手 `5.29x / 5.05x / 5.28x / 5.70x / 5.06x`。它保持 2025/2026 正弹性和较浅回撤，但 2017/2020/2023 收益仍低于 `theme_monthly_cost_control` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 下一轮 focus 转为 `biweekly_breakout`，但该支线近期多次暴露长窗深回撤，仍只允许强约束最后复核。下一轮第一条命令若必须响应 focus，建议只测 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit38_risk40` 或同等更强防守版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_last_check_id>`；若仍失败，继续回到主题月频修复池。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `elasticity_cost_control`；本轮按计划补 `inverse_elastic_monthly_cost_guard_v4`，不重启普通双周 breakout 阈值邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_inverse_elastic_monthly_cost_guard_v4`。实际命令见 HK Path 1 本轮合并批次，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `inverse_elastic_monthly_cost_guard_v4` 五窗口 CAGR 为 `16.71% / 17.65% / 10.70% / 71.97% / 45.30%`，最大回撤 `-36.33% / -36.33% / -34.18% / -9.95% / -6.44%`，换手 `5.10x / 5.01x / 5.58x / 6.04x / 6.74x`。它与上一轮等权 v4 同形，保留 2025/2026 弹性，但 2023 和长窗回撤不达 robust 标准。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 收尾再次运行 guard 后下一轮 focus 转为 `high_return_monthly`。下一轮第一条命令不要再复制 elastic v4，同一支线转回主题月频高收益修复池，例如 `hkconnect_path2_theme_monthly_high_return_cost_control_v3` 或同等 `2023>=25% / worstDD>-25%` 目标版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass`，上一轮 `equal_elastic_monthly_cost_guard_v4` 仍是 2025/2026 强、2023 和长窗回撤弱；本轮按上一轮 `high_return_monthly` 新增 `theme_monthly_high_return_cost_control_v2`，不重启普通双周 breakout 阈值邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_high_return_cost_control_v2`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light,hkconnect_path2_theme_monthly_high_return_cost_control_v2,hkconnect_path3_theme_fast_weekly_defensive_turnover8_exit52`。
- `theme_monthly_high_return_cost_control_v2` 五窗口 CAGR 为 `18.56% / 23.52% / 22.49% / 59.92% / 57.95%`，最大回撤 `-27.59% / -16.42% / -13.08% / -10.12% / -9.96%`，换手 `5.48x / 5.25x / 5.43x / 5.97x / 5.23x`。它保持 2025/2026 正弹性，但 2017/2020/2023 仍低于 `theme_monthly_cost_control` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `elasticity_cost_control`。双周 breakout 继续作为失败/暂停对照，不做普通邻域；下一轮第一条命令建议只补一个弹性月频成本版的低回撤复核，例如 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v4` 或同等 `2023>=25%` 目标版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_next_id>`；若 2023 仍低于 25% 或长窗回撤超过 30%，继续回到主题月频修复池。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass`，上一轮 `theme_monthly_high_return_lowturn_reconfirm` 保持 2026 正收益但 2017/2020/2023 不足；本轮按 `elasticity_cost_control` 补等权弹性月频成本版 v4，观察能否改善 v3 的 2023 弱和长窗回撤。
- 本轮新增并五窗口确认：`hkconnect_path2_equal_elastic_monthly_cost_guard_v4`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `equal_elastic_monthly_cost_guard_v4` 五窗口 CAGR 为 `16.71% / 17.65% / 10.70% / 71.97% / 45.30%`，最大回撤 `-36.33% / -36.33% / -34.18% / -9.95% / -6.44%`，换手 `5.10x / 5.01x / 5.58x / 6.04x / 6.74x`。v4 保留 2025/2026 弹性，但 2023 和长窗回撤更弱，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `hkconnect_path2_theme_monthly_cost_control`，2023 为 `hkconnect_path2_theme_monthly`，2025 为 `hkconnect_path2_breakout_concentrated_monthly`，robust 仍为 `theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `high_return_monthly`。下一轮第一条命令建议回到主题月频高收益修复池，而不是继续 elastic v4 邻域，例如 `hkconnect_path2_theme_monthly_high_return_cost_control_v2` 或同等 `2023>=25%` 的成本版，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass`，上一轮强约束双周 breakout 最后复核仍失败；本轮按 `high_return_monthly` 回到主题月频高收益修复池，新增 `high_return_lowturn_reconfirm`，重点看 2026 正收益能否不牺牲 2017/2020/2023 太多。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_high_return_lowturn_reconfirm`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path2_theme_monthly_high_return_lowturn_reconfirm,hkconnect_path3_theme_fast_weekly_defensive_turnover10_exit50`。
- `theme_monthly_high_return_lowturn_reconfirm` 五窗口 CAGR 为 `18.75% / 23.47% / 21.80% / 54.29% / 41.19%`，最大回撤 `-25.03% / -16.46% / -12.78% / -11.00% / -10.96%`，换手 `5.30x / 5.06x / 5.29x / 5.70x / 5.06x`。它保持 2026 正收益和可控回撤，但 2017/2020/2023 仍低于 `theme_monthly_cost_control` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 为 `theme_monthly`，2025 为 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`。候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 轮到 `elasticity_cost_control`；双周 breakout 仍保留为失败/暂停对照，不做普通阈值邻域。下一轮第一条命令建议只测一个低回撤弹性月频成本版，例如 `hkconnect_path2_equal_elastic_monthly_cost_guard_v4` 或 `hkconnect_path2_inverse_elastic_monthly_cost_guard_v4`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_elasticity_cost_control_next_id>`；若 2023 仍低于 25% 或长窗回撤超过 30%，继续回到主题月频修复池。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass`，上一轮 plan 已把 `biweekly_breakout` 映射为“只允许强约束复核”的失败支线；本轮按该约束只补一条更强防守/低卖出阈值的双周 breakout 复核，不重启普通阈值邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit40_risk45`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `breakout_cost_guard_biweekly_defensive_cashguard_exit40_risk45` 五窗口 CAGR 为 `1.28% / -2.65% / -1.94% / 31.21% / -23.16%`，最大回撤 `-57.79% / -57.79% / -38.95% / -14.62% / -10.21%`，换手 `14.26x / 14.11x / 15.87x / 20.07x / 19.81x`。更强防守仍无法修复长窗深回撤和 2026 负收益，双周 breakout 支线继续作为失败/暂停对照。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 为 `theme_monthly`，2025 为 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，候选池未触发 HK explore cap evict。
- 收尾 guard 下一轮 focus 为 `high_return_monthly`。下一轮第一条命令建议不要再补普通双周 breakout，回到主题/月频高收益但以 2023 不塌为前提，例如 `hkconnect_path2_theme_monthly_high_return_lowturn_reconfirm` 或 `hkconnect_path2_theme_monthly_high_return_cost_control_v2`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass`，上一轮 focus 已回到 `high_return_monthly`；本轮按计划测试主题月频的高收益再确认成本约束，不再继续普通双周 breakout 阈值邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_monthly_reconfirm_high_return_cost_control` 五窗口 CAGR 为 `19.46% / 24.96% / 24.32% / 62.44% / 68.14%`，最大回撤 `-26.34% / -17.71% / -13.58% / -9.86% / -8.35%`，换手 `5.68x / 5.40x / 5.56x / 6.13x / 5.52x`。它保持 2025/2026 高弹性且回撤可控，但 2017/2020/2023 收益仍低于 `theme_monthly_cost_control` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 为 `theme_monthly`，2025 为 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86x`。
- 候选池未触发 HK explore cap evict。最终 guard 又给出 `biweekly_breakout`，但该 focus 已连续出现 `-50%` 级长窗回撤，因此本轮在 plan 中把它映射为“只允许强约束复核”的候选池，而不是普通阈值邻域。下一轮第一条命令若必须响应该 focus，建议只测一个更强防守/低换手的最后复核，如 `hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit40_risk45`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_breakout_last_check_id>`；若仍深回撤，则继续回到 `theme_monthly_cost_control` 修复池。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass`，上一轮计划把连续深回撤的 `biweekly_breakout` 映射为“最后一次强约束复核池”；本轮只执行 `cashguard_exit35_risk50` 单条复核，不重启普通双周阈值邻域。
- 本轮新增并五窗口确认：`hkconnect_path2_breakout_cost_guard_biweekly_cashguard_exit35_risk50`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `breakout_cost_guard_biweekly_cashguard_exit35_risk50` 五窗口 CAGR 为 `3.23% / -0.61% / -0.43% / 36.68% / -16.67%`，最大回撤 `-56.75% / -56.75% / -40.48% / -16.72% / -9.39%`，换手 `14.80x / 14.59x / 16.25x / 20.28x / 20.28x`。现金防守没有修复长窗深回撤，也没有修复 2026 负收益，双周 breakout 支线继续作为失败/暂停对照。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 为 `theme_monthly`，2025 为 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86x`。
- 候选池未触发 HK explore cap evict。收尾 guard 给出下一轮 focus `high_return_monthly`；下一轮第一条命令建议回到主题/月频高收益修复池，例如 `hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control` 或等权/反向弹性低回撤版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_high_return_monthly_next_id>`。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass`，上一轮 `theme_monthly_cost_control_lowturn` 回撤浅但收益低于旧 robust；本轮按计划补更保守的高收益主题月频修复对照 `reconfirm_cost_control`，不重启普通双周 breakout 阈值微调。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_reconfirm_cost_control`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_monthly_reconfirm_cost_control` 五窗口 CAGR 为 `18.91% / 23.68% / 22.97% / 57.61% / 56.68%`，最大回撤 `-24.67% / -15.98% / -12.76% / -9.44% / -9.40%`，换手 `5.22x / 4.94x / 5.20x / 5.70x / 5.27x`。它能保持 2026 为正并控制回撤，但 2017/2020/2023 收益仍低于 `theme_monthly_cost_control` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 为 `theme_monthly`，2025 为 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86x`。
- 收尾 guard 给出下一轮 focus `biweekly_breakout`。该 focus 已连续产出 `-50%` 级长窗回撤，本轮将它映射为“暂停后的单次强约束复核池”，不再做普通阈值邻域；第一条命令若必须响应 focus，建议只实现 `hkconnect_path2_breakout_cost_guard_biweekly_cashguard_exit35_risk50` 这一条，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path2_biweekly_last_check_id>`。若仍出现长窗深回撤，则继续回到主题月频修复池。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass`，上一轮已记录 `biweekly_breakout` 连续 `-50%` 级长窗回撤，应暂停普通阈值微调；本轮按 focus -> candidates 池转向主题月频修复，新增低换手成本控制版本。
- 本轮新增并五窗口确认：`hkconnect_path2_theme_monthly_cost_control_lowturn`。实际命令见 HK Path 1 本轮合并命令，命令类型为五窗口 `--only-strategy-ids` 增量确认。
- `theme_monthly_cost_control_lowturn` 五窗口 CAGR 为 `21.29% / 26.06% / 22.34% / 54.03% / 37.50%`，最大回撤 `-16.76% / -12.14% / -11.49% / -11.49% / -11.48%`，换手 `5.02x / 4.85x / 5.15x / 5.56x / 4.91x`。它明显降低回撤并让 2026 为正，但收益仍低于既有 `theme_monthly_cost_control` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 2 tracked/robust 未变化：2017/2020 仍为 `theme_monthly_cost_control`，2023 为 `theme_monthly`，2025 为 `breakout_concentrated_monthly`；robust 仍为 `theme_monthly_cost_control`，`meanCAGR=37.46% / minCAGR=22.42% / worstMaxDD=-25.34% / meanTurn=5.86x`。
- 候选池未触发 HK explore cap evict。收尾 guard 的下一轮 focus 为 `high_return_monthly`，但 elastic v3 已反复证明 2023/长窗弱；第一条命令建议只做一个更保守的高收益月频修复对照 `hkconnect_path2_theme_monthly_reconfirm_cost_control`，若仍 2023 低于 25% 或回撤超过 25%，继续把 `lowturn` 作为浅回撤观察而非重启双周 breakout。

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
