# 沪港通 Path 2 研究计划

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
- 默认比较对象固定为当前 7 个港股 `Path 2` 候选：
  - `hkconnect_path2_breakout_monthly`
  - `hkconnect_path2_breakout_biweekly`
  - `hkconnect_path2_breakout_weekly`
  - `hkconnect_path2_theme_monthly`
  - `hkconnect_path2_theme_biweekly`
  - `hkconnect_path2_equal_elastic_monthly`
  - `hkconnect_path2_equal_elastic_weekly`
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
  - `hkconnect_path2_theme_monthly`（`2017 / 2020 / 2023` 窗口）
  - `hkconnect_path2_breakout_monthly`（`2025` 窗口）
  - `hkconnect_path2_theme_monthly`（当前四窗口 robust candidate）
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

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：缓存回退路径继续正常，这次同步把当前主分支基线里缺失的港股 `Path 2` 月频 winner 结构重新写回 tracked payload。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `83885b39cb11f568d0ce2772e4cbaa9a0c6c1b62c089127e89eb39bbba12ceed` 与 `d5d3bc0cf9a03aeb713d76efd76d2687be6d0d47f65f784dcd12734bf1062d4f`；当前 tracked winners 已同步为：
  - `since_2017_01 / since_2020_01 / since_2023_01`：`hkconnect_path2_theme_monthly`（对应 `22.79% CAGR / -18.86% MaxDD / 1.1654 Sharpe / 6.62 Turn` 与 `32.43% CAGR / -16.07% MaxDD / 1.4541 Sharpe / 6.01 Turn`）
  - `since_2025_01`：`hkconnect_path2_breakout_monthly`（`99.22% CAGR / -7.72% MaxDD / 2.6848 Sharpe / 8.62 Turn`）
  - `robust`：`hkconnect_path2_theme_monthly`（`meanCAGR 38.73% / minCAGR 22.79%`）
- 这意味着当前港股 `Path 2` 的默认锚点已经从 `theme_biweekly / breakout_biweekly` 重新回到月频主线：`theme_monthly` 同时占住 `2017 / 2020 / 2023 / robust`，而 `breakout_monthly` 接管 `2025` 短窗口 winner。`since_2026_01` raw leader 仍是 `hkconnect_path2_breakout_monthly`（`188.57% CAGR / -4.77% MaxDD / 2.2393 Sharpe / 7.47 Turn`）。
- 当前 sidecar challenger 顺位也随之收窄到月频族优先：
  - `since_2020_01`：`hkconnect_path2_equal_elastic_monthly` 仍是最接近主线的 challenger（`18.33% CAGR / -36.76% MaxDD / 0.8263 Sharpe / 6.58 Turn`）
  - `since_2023_01`：`hkconnect_path2_breakout_monthly` 是当前最接近 `theme_monthly` 的 challenger（`23.31% CAGR / -30.38% MaxDD / 0.9455 Sharpe / 8.61 Turn`）
  - `since_2025_01`：`hkconnect_path2_equal_elastic_monthly` 仍是最接近 `breakout_monthly` 的 challenger（`90.24% CAGR / -8.40% MaxDD / 2.6254 Sharpe / 6.64 Turn`）
- 下一轮港股 `Path 2` 继续优先围绕 `theme_monthly / breakout_monthly / equal_elastic_monthly` 这三条月频主线推进，不新增港股高频候选族，也不把 `biweekly / weekly` 重新拉回默认锚点。
