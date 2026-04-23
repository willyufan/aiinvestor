# 沪港通 Path 1 研究计划

## 定位
- 独立于当前 A 股 Path 1
- 仅限沪港通标的（当前使用 Tushare `stock_hsgt` 最新可得名单作为静态池）
- 目标：先做出可解释、换手相对可控、窗口表现稳定的港股主线策略

## 当前假设
- 港股通标的中，月度动量 + 流动性质量 + 三档风险收缩，能形成相对稳健的收益曲线
- 纯粹把 A 股 winner_core 逻辑搬到港股未必有效，港股更需要：
  - 更重视流动性
  - 更宽的权重上限
  - 更直接的风险收缩

## 当前候选方向
1. 月度稳健（混合权重）
2. 月度熊市空仓
3. 月度等权缓冲
4. 月度低波偏稳

## 本轮迭代执行规则

- 沪港通 `Path 1` 作为**独立于 A 股**的研究线，每轮迭代都要单独评估，不并入 A 股 `winner_only_pass`。
- 默认回测窗口固定为：
  - `since_2017_01`
  - `since_2020_01`
  - `since_2023_01`
  - `since_2025_01`
  - `since_2026_01`（观察窗）
- 默认比较对象固定为当前 4 个港股 `Path 1` 候选：
  - `hkconnect_path1_monthly_hybrid`
  - `hkconnect_path1_monthly_cashoff`
  - `hkconnect_path1_monthly_equal_buffered`
  - `hkconnect_path1_monthly_lowvol`
- 下一轮港股 `Path 1` 的主判定口径：
  - 更看重 `since_2020_01 / since_2023_01`
  - 重点指标：
    - `Total Return`
    - `CAGR`
    - `MaxDD`
    - `Sharpe`
    - `Turnover`
- 若港股 `Path 1` 任一窗口赢家发生变化，需同步更新：
  - `results_hkconnect/strategy_comparison_hkconnect.csv`
  - 实盘平台导出层中的沪港通策略注册表
  - README/HISTORY（若当前轮允许更新）

## 当前默认推进结论

- 当前港股 `Path 1` 默认主攻版本是：
  - `hkconnect_path1_monthly_equal_buffered`
- `monthly_cashoff` 保留为更防守的候选。
- `monthly_hybrid / monthly_lowvol` 继续作为对照，不轻易移出，直到多轮窗口表现明显失去竞争力。

## 近期优先看
- 2017 / 2020 / 2023 三个窗口的 CAGR、MaxDD、Sharpe
- 2026 观察窗是否出现过强的终点效应

## 已知限制
- 受 `stock_hsgt` 历史覆盖限制，当前不是严格的历史动态沪港通池，而是“最新可得名单静态池”
- 当前交易成本仍是近似模型，先用于研究排序，不用于精确实盘估值
- 若当前 Tushare key 无 `stock_hsgt` 权限，可手工提供 `data_cache/hkconnect/basic/stock_hsgt_manual.csv` 作为静态池输入

## 本轮快筛记录（2026-04-21 18:24）

- 运行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`
- 指标口径修正：`backtest_hkconnect.py` 现在会把 `sample_start` 对齐到**首个可执行调仓点**（避免“长时间无交易导致 CAGR 被错误年化”的窗口指标偏差）。
- 窗口赢家（按 `CAGR`，来源：`results_hkconnect/strategy_comparison_hkconnect.csv`）：
  - `since_2017_01`：`hkconnect_path1_monthly_equal_buffered`（CAGR `23.33%` / MaxDD `-22.36%` / Sharpe `1.1583`）
  - `since_2020_01`：`hkconnect_path1_monthly_equal_buffered`（CAGR `41.17%` / MaxDD `-19.79%` / Sharpe `1.5351`）
  - `since_2023_01`：`hkconnect_path1_monthly_equal_buffered`（CAGR `54.81%` / MaxDD `-0.07%` / Sharpe `3.5914`；该窗口目前实际可交易起点已后移至 `2025`）
  - `since_2025_01`：`hkconnect_path1_monthly_equal_buffered`（同上；与 `since_2023_01` 当前等价）
  - `since_2026_01`：观察窗调仓点不足，本轮全部跳过

## 本轮补充（2026-04-21 20:18）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论不变；`since_2026_01` 仍因调仓点不足全部跳过。

## 本轮补充（2026-04-21 22:20）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论不变；`since_2026_01` 仍因调仓点不足全部跳过（trade_calendar / hk_daily_adj 更新失败时自动回退本地缓存）。

## 本轮补充（2026-04-22）

- 重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：窗口赢家结论继续不变；`since_2026_01` 仍因调仓点不足全部跳过。
- 当前港股窗口的有效起点已稳定为：
  - `since_2017_01` → `2017-02-01`
  - `since_2020_01` → `2020-02-03`
  - `since_2023_01 / since_2025_01` → `2025-02-03`
- `hkconnect_path1_monthly_equal_buffered` 继续占据四窗口赢家：`2017 23.33% / 2020 41.17% / 2023 54.81% / 2025 54.81% CAGR`。
- `hkconnect_path1_monthly_lowvol` 仍值得保留为防守对照：在 `since_2020_01` 上有 `39.89% CAGR / -5.40% MaxDD / 2.0798 Sharpe`，但仍没有在 `CAGR` 上改写 `monthly_equal_buffered`。
- 下一轮继续把 `monthly_equal_buffered` 作为默认主攻版本，同时把 `monthly_lowvol` 固定为“压回撤 / 对照 Sharpe”的参考线；不新增 Path 1 候选族。
- 本次再次重跑后，`results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 仍完全对齐：四窗口 winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`；因此本轮不刷新 README / HISTORY / 港股对比图。
- `2026-04-22 06:27 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 与个别 `hk_daily_adj` 更新失败时继续自动回退本地缓存，窗口赢家与关键指标未出现漂移。
- 当日后续再次以离线缓存重跑同一命令后，`monthly_equal_buffered` 仍稳定占据 `2017 / 2020 / 2023 / 2025` 四窗口第一；`monthly_lowvol` 继续只作为“低回撤/高 Sharpe 对照线”保留，不晋升为主攻版本。
- 当日后续又完整重跑 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，并执行 `.venv/bin/python scripts/update_hkconnect_artifacts.py` 后，港股 Path 1 的 tracked winner 仍未变化，但长窗口口径已进一步稳定到当前缓存基线：
  - `since_2017_01 / since_2020_01`：`hkconnect_path1_monthly_equal_buffered`，两窗当前都从 `2020-12-01` 起算，指标同为 `23.47% CAGR / -14.78% MaxDD / 1.3697 Sharpe / 2.88 Turnover`
  - `since_2023_01`：`34.37% CAGR / -14.78% MaxDD / 1.7044 Sharpe / 2.89 Turnover`
  - `since_2025_01`：`41.63% CAGR / -14.78% MaxDD / 1.5544 Sharpe / 3.47 Turnover`
- `since_2026_01` 原始比较行已不再缺失，但它仍只作为观察窗：当前 Path 1 raw leader 是 `hkconnect_path1_monthly_lowvol`，仅为 `-2.04% CAGR / -5.52% MaxDD / -0.0509 Sharpe / 3.10 Turnover`，说明港股 Path 1 的今年表现仍偏防守。
- `2026-04-22 14:30 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 与 `02940.HK` 更新失败时继续回退本地缓存，窗口赢家与关键指标未出现任何漂移。
- `results_hkconnect/strategy_comparison_hkconnect.csv` 仍与 `results_hkconnect/tracked_winners_hkconnect.json` 完全一致：`hkconnect_path1_monthly_equal_buffered` 继续占据 `2017 / 2020 / 2023 / 2025` 四窗口第一，`monthly_lowvol` 继续只保留为低回撤对照线。
- Path 1 自身窗口 winner 与关键指标本轮都未变化；后续只因 `Path 2 robust_candidate` 的 artifact 口径修正而同步刷新 README / HISTORY / 港股对比图。`Path 1` 本身继续把 `monthly_equal_buffered` 作为默认主攻版本。

## 本轮补充（2026-04-22 23:27 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 与 `02940.HK` 更新失败时继续回退本地缓存，窗口赢家与关键指标未出现漂移。
- 回测后 `results_hkconnect/strategy_comparison_hkconnect.csv` 的 SHA256 仍为 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f`，`tracked_winners_hkconnect.json` 的 SHA256 仍为 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明本轮没有新的港股 Path 1 artifact 漂移。
- 当前结论继续维持：`hkconnect_path1_monthly_equal_buffered` 仍是四窗口 tracked winner，`hkconnect_path1_monthly_lowvol` 仍只保留为低回撤对照与 `since_2026_01` 观察窗 raw leader。
- 下一轮继续只围绕 `monthly_equal_buffered` 与 `monthly_lowvol` 这条主攻/对照组合观察，不新增港股 Path 1 候选族，也不刷新 README / HISTORY / 图表。

## 本轮补充（2026-04-23 01:32 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `.venv/bin/python scripts/update_hkconnect_artifacts.py`：港股 Path 1 的 tracked winners 与关键指标继续完全不变。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明本轮只是确认性重跑，没有新的港股 Path 1 artifact 漂移。
- 当前四窗口 winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.47% CAGR / -14.78% MaxDD / 1.3697 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.37% CAGR / -14.78% MaxDD / 1.7044 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.63% CAGR / -14.78% MaxDD / 1.5544 Sharpe / 3.47 Turn`
- `since_2026_01` 观察窗 raw leader 继续是 `hkconnect_path1_monthly_lowvol`（`-2.04% CAGR / -5.52% MaxDD / -0.0509 Sharpe / 3.10 Turn`）。下一轮港股 `Path 1` 继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 对照，不新增候选族，也不把本轮重跑解读成新的胜负变化。

## 本轮补充（2026-04-23 03:33 CST）

- 本轮继续运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；`trade_calendar` 与个股 `hk_daily_adj` 仍全部走本地缓存回退路径，但回测完成且窗口赢家未出现漂移。
- 回测后 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明本轮港股 `Path 1` 仍是确认性重跑，而不是新的 winner 改写。
- 结论继续维持：`hkconnect_path1_monthly_equal_buffered` 仍稳住 `2017 / 2020 / 2023 / 2025` 四窗口，`hkconnect_path1_monthly_lowvol` 仍只保留为低回撤对照与 `since_2026_01` 观察窗 raw leader。下一轮不新增 `Path 1` 候选族。

## 本轮补充（2026-04-23 05:29 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 与全部 `hk_daily_adj` 继续因为网络受限而回退本地缓存，但回测完成且 Path 1 窗口赢家未出现任何漂移。
- 回测后再次执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`，`results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 仍分别是 `8052682e474fb53eafb079a49a5bc21033d37d513dcd7705b5eb2538ea28784f` 与 `16f00fb889aafdf838b6793cb8edbb4910e9bc700d8f226f3d764e8e46646eec`；说明这轮港股 Path 1 仍只是确认性重跑，没有新的 artifact drift。
- 当前结论继续维持：`hkconnect_path1_monthly_equal_buffered` 仍稳住 `2017 / 2020 / 2023 / 2025` 四窗口，`hkconnect_path1_monthly_lowvol` 仍只保留为低回撤对照与 `since_2026_01` 观察窗 raw leader。下一轮继续只保留这条主攻/对照组合，不新增港股 Path 1 候选族。

## 本轮补充（2026-04-23 09:30 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`：`trade_calendar` 与 `02940.HK` 仍因网络受限回退到本地缓存，但回测完成且 Path 1 tracked winner 继续完全不变。
- 回测后 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 更新为 `64b36ccb6a6e8e2f2f6aa58f90d7bcaceddfff1c4252add7e9d5312c84567283` 与 `e6a839d2c4315bbe0691ad4d52ddc697ebeb846652d5bc5c2662212e5b9f27b5`；本轮不只是“确认稳定”，而是港股 comparison/track artifacts 随 `2026-04-23` 收盘后同步上修。
- 当前四窗口 winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.72% CAGR / -14.78% MaxDD / 1.3757 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.83% CAGR / -14.78% MaxDD / 1.7134 Sharpe / 2.89 Turn`
  - `since_2025_01`：`42.89% CAGR / -14.78% MaxDD / 1.5796 Sharpe / 3.47 Turn`
- `robust_candidate` 仍是 `hkconnect_path1_monthly_equal_buffered`，但口径同步上修到 `meanCAGR 31.29% / minCAGR 23.72% / meanSharpe 1.5111`。`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`-3.57% CAGR / -5.52% MaxDD / -0.1460 Sharpe / 3.10 Turn`）。
- 下一轮继续只保留 `monthly_equal_buffered` 主攻与 `monthly_lowvol` 对照，不新增 Path 1 候选族；本轮 README / HISTORY / 港股图表的刷新，主要是为了同步这次 `2026-04-23` 指标上修与 Path 2 的新窗口 winner。
