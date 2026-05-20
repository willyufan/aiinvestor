# 沪港通 Path 3 周度高频路径

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
