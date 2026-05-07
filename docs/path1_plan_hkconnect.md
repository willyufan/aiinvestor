# 沪港通 Path 1 研究计划

## 本轮执行计划（2026-05-08 07:28 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=33.38% / minCAGR=24.37%`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分数据截止日与真实信号/换股生效日。

## 本轮执行计划（2026-05-07 23:12 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=33.38% / minCAGR=24.37%`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分数据截止日与真实信号/换股生效日。

## 本轮执行计划（2026-05-07 11:10 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分 `data_as_of=2026-05-06` 与港股真实信号/换股生效日。

## 本轮执行计划（2026-05-07 05:06 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 继续区分港股数据截止日与真实换股/信号生效日；月频、双周、周频与低波候选全部保留，不因长窗月频胜出而停止高频路线观察。

## 本轮执行计划（2026-05-06 23:15 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；港股 tracked payload 仍以 `as_of=2026-04-30` 记录，公开快照的缓存数据截止日与信号生效日分开保留。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，指标为 `24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 月频、双周、周频与低波候选继续保留；本轮不因长窗月频胜出而停止高频路线观察。

## 本轮执行计划（2026-05-06 11:35 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新仍失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录。
- Path 1 tracked winners 未较 06:14 记录漂移：`since_2017_01 / since_2020_01` 仍是低换手 `hkconnect_path1_monthly_equal_buffered`（`24.87% CAGR / -14.78% MaxDD / 1.4421 Sharpe / 2.80 Turnover`）。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`（分别为 `34.80% CAGR` 与 `48.95% CAGR`）；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 周频、双周、月频与低波候选全部保留；本轮是结果同步和 turnover 明细重写，不改变港股 Path 1 路线判断。

## 本轮执行计划（2026-05-06 06:14 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新仍失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录。
- Path 1 tracked winners 未较 00:04 记录漂移：`since_2017_01 / since_2020_01` 仍是低换手 `hkconnect_path1_monthly_equal_buffered`（`24.87% CAGR / -14.78% MaxDD / 1.4421 Sharpe / 2.80 Turnover`）。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`（分别为 `34.80% CAGR` 与 `48.95% CAGR`）；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 周频、双周、月频与低波候选全部保留；本轮只是数值级同步重跑，不改变港股 Path 1 路线判断。

## 本轮执行计划（2026-05-06 00:04 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- Path 1 继续评估月频、双周、周频与低波候选；港股 winner 结论不并入 A 股。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 tracked payload 判断是否只是同步重跑，或出现窗口赢家切换。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 tracked payload 仍为 `as_of=2026-04-30`。
- 本轮 Path 1 `since_2017_01 / since_2020_01` winner 从 `hkconnect_path1_weekly_equal_buffered` 切到低换手 `hkconnect_path1_monthly_equal_buffered`（`24.87% CAGR / -14.78% MaxDD / 1.4421 Sharpe / 2.80 Turnover`）。
- `since_2023_01 / since_2025_01` winner 继续是 `hkconnect_path1_weekly_equal_buffered`（分别为 `34.80% CAGR` 与 `48.95% CAGR`）；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`。
- 月频、双周、低波与周频候选继续保留为候选对照，不因为长窗月频切换而停止高频路线观察。

## 本轮补充计划与记录（2026-05-05 18:16 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- 月频、双周、低波候选继续保留为低换手和低回撤对照；港股 Path 1 结论不并入 A 股 winner。

## 本轮补充计划与记录（2026-05-05 12:14 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 继续保留月频、双周、周频与低波对照，不新增候选族，不把港股结论并入 A 股 winner。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。

## 本轮补充计划与记录（2026-05-05 06:14 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- 月频、双周、低波候选继续保留为低换手和低回撤对照；港股 Path 1 结论不并入 A 股 winner。

## 本轮补充计划与记录（2026-05-05 00:03 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 继续评估月频、双周、单周与低波候选；不新增候选族，不把港股结论并入 A 股 winner。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 tracked payload 确认是否只是同步重跑，或出现窗口赢家切换。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。

## 本轮补充计划与记录（2026-05-04 18:07 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，再运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 继续评估月频、双周、单周与低波候选；不新增候选族，不把港股结论并入 A 股 winner。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 tracked payload 确认是否只是同步重跑，或出现窗口赢家切换。
- `trade_calendar` 在线更新失败时继续回退本地缓存；港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`。
- 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。

## 本轮补充计划与记录（2026-05-04 15:25 CST）

- 继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败时回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- 月频、双周、低波候选继续保留为低换手和低回撤对照；港股 Path 1 结论仍不并入 A 股 winner。

## 本轮补充计划（2026-05-04 06:45 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，以本地缓存完成五窗口评估。
- Path 1 仍只评估当前月频、双周、单周与低波对照候选，不新增候选族；港股结论不并入 A 股 winner。
- 跑完后用 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 tracked payload 判断是否只是同步重跑，或出现窗口赢家/robust candidate 切换。

### 本轮补充记录（2026-05-04 09:40 CST）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

## 本轮执行计划（2026-05-04）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-05-04 03:57 CST）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

## 本轮执行计划（2026-05-03）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-05-03 00:16 CST；06:11 CST 复核）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

### 本轮补充（2026-05-03 12:05 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 继续为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 仍全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标未漂移：`since_2017_01 / since_2020_01` 仍为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`；月频、双周、低波候选继续作为低换手和低回撤对照保留。

### 本轮补充（2026-05-03 18:13 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

## 本轮执行计划（2026-05-02）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-05-02）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标未漂移：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- `since_2026_01` 仍只作为观察窗；月频、双周、低波候选继续作为低换手和低回撤对照保留。

### 本轮补充（2026-05-02 06:07 CST）

- 重新运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- `results_hkconnect/tracked_winners_hkconnect.json` 与两张港股对比图重写后无实质 git diff；月频、双周、低波候选继续保留为低换手和低回撤对照。

### 本轮补充（2026-05-02 12:10 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

### 本轮补充（2026-05-02 18:08 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 tracked payload 仍为 `as_of=2026-04-30`；四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标保持不变：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`；月频、双周、低波候选继续保留为对照。

## 本轮执行计划（2026-05-01）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-05-01）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时已回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，robust candidate 也保持同一策略。
- 关键指标未出现 winner 切换：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- `since_2026_01` 仍只作为观察窗；月频、双周、低波候选继续保留为对照，不因为当前单周等权缓冲胜出而移出。

### 本轮补充（2026-05-01 06:11 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标维持：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / 1.5484 Sharpe`，`since_2025_01` 为 `48.95% CAGR / 1.7009 Sharpe`。
- 本轮港股 Path 1 没有窗口赢家切换；月频、双周、低波候选继续保留为换手和回撤对照。

### 本轮补充（2026-05-01 12:11 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标仍维持：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / -13.41% MaxDD / 1.5484 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `48.95% CAGR / -13.41% MaxDD / 1.7009 Sharpe / 12.98 Turnover`。
- `since_2026_01` 仍只作为观察窗，raw leader 继续是 `hkconnect_path1_weekly_lowvol`（`26.25% CAGR / -4.77% MaxDD / 1.6746 Sharpe / 5.25 Turnover`）；本轮不新增港股 Path 1 候选族。

### 本轮补充（2026-05-01 18:14 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 更新失败时继续回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 的数据截止日仍为 `as_of=2026-04-30`；Path 1 四窗口 winner 与 robust candidate 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标未漂移：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR / -13.41% MaxDD / 1.5484 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `48.95% CAGR / -13.41% MaxDD / 1.7009 Sharpe / 12.98 Turnover`。
- `since_2026_01` 仍只作为观察窗；月频、双周、低波候选继续作为低换手和低回撤对照保留。

## 本轮执行计划（2026-04-30）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 继续观察 `hkconnect_path1_weekly_equal_buffered`，并保留 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照；不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-04-30）

- 运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 1 四窗口 winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，robust candidate 也保持同一策略。
- 关键指标未出现 winner 切换：`since_2017_01 / since_2020_01` 为 `23.08% CAGR / -13.41% MaxDD / 1.2383 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `35.04% CAGR / -13.41% MaxDD / 1.5530 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `49.82% CAGR / -13.41% MaxDD / 1.7137 Sharpe / 13.03 Turnover`。
- `since_2026_01` 仍只作为观察窗；当前 Path 1 raw leader 是 `hkconnect_path1_weekly_lowvol`（`27.00% CAGR / -4.77% MaxDD / 1.6656 Sharpe / 5.33 Turnover`），不进入 tracked winners。本轮港股 tracked JSON 与港股对比图重写后没有实质 git diff，说明当前港股 Path 1 仍是确认性重跑。

### 本轮补充（2026-04-30 06:35 CST）

- 再次运行港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；`results_hkconnect/tracked_winners_hkconnect.json` 与港股 Path 1 图表重写后仍无实质 git diff。
- Path 1 四窗口 tracked winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，`since_2026_01` 仍只保留为观察窗；本轮没有把月频、双周或低波候选晋升为 tracked winner。
- 港股 Path 1 结论继续独立于 A 股，不并入 `winner_only_pass`；下一轮仍用 `monthly_equal_buffered / monthly_lowvol` 作为低换手、低回撤对照。

### 本轮补充（2026-04-30 12:12 CST）

- 再次运行港股五窗口回测：`./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- Path 1 四窗口 tracked winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，robust candidate 也保持同一策略；本轮港股 Path 1 没有窗口赢家切换。
- `since_2026_01` 继续只作为观察窗；月频、双周、低波候选继续保留为对照，不因为当前单周等权缓冲胜出而移出。

### 本轮补充（2026-04-30 18:16 CST）

- 再次完成港股五窗口回测与 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；tracked payload 的数据截止日推进到 `as_of=2026-04-30`。
- Path 1 四窗口 tracked winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`：`since_2017_01 / since_2020_01` 为 `23.00% CAGR / -13.41% MaxDD / 1.2361 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `34.80% CAGR`，`since_2025_01` 为 `48.95% CAGR`。
- `since_2026_01` 仍只作为观察窗，raw leader 继续是 `hkconnect_path1_weekly_lowvol`（`26.25% CAGR / -4.77% MaxDD / 1.6746 Sharpe / 5.25 Turnover`）；月频、双周、低波候选继续保留为对照。

## 上轮执行计划（2026-04-29）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 是 `hkconnect_path1_weekly_equal_buffered`，但继续把 `hkconnect_path1_monthly_equal_buffered` 与 `hkconnect_path1_monthly_lowvol` 作为低换手/低回撤对照，不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-04-29 12:09 CST）

- 运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 1 四窗口 winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`。
- 关键指标维持：`since_2017_01 / since_2020_01` 为 `23.08% CAGR / -13.41% MaxDD / 1.2383 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `35.04% CAGR / -13.41% MaxDD / 1.5530 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `49.82% CAGR / -13.41% MaxDD / 1.7137 Sharpe / 13.03 Turnover`。
- `since_2026_01` 仍只做观察窗；当前 Path 1 raw leader 是 `hkconnect_path1_weekly_lowvol`（`27.00% CAGR / -4.77% MaxDD / 1.6656 Sharpe / 5.33 Turnover`），不进入 tracked winners。

### 本轮快筛记录（2026-04-29 18:50 CST）

- 重新运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 当前 tracked payload 的数据截止日仍为 `as_of=2026-04-24`；Path 1 四窗口 winner 继续全部是 `hkconnect_path1_weekly_equal_buffered`，robust candidate 也保持同一策略。
- 关键指标未出现可解释的 winner 切换：`since_2017_01 / since_2020_01` 仍为 `23.08% CAGR / -13.41% MaxDD / 1.2383 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `35.04% CAGR / -13.41% MaxDD / 1.5530 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `49.82% CAGR / -13.41% MaxDD / 1.7137 Sharpe / 13.03 Turnover`。
- 本轮 `results_hkconnect/**`、tracked JSON、港股对比图及 public/live 导出产生小幅同步 diff，主要来自候选明细指标漂移与公开快照 `data_as_of=2026-04-29` 更新；信号/换股生效日仍按真实周频或月频评估点保留。

## 上轮执行计划（2026-04-28）

- 本轮继续单独运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，港股 Path 1 结论不并入 A 股 winner。
- Path 1 当前 tracked winner 已切到 `hkconnect_path1_weekly_equal_buffered`，但需要继续把 `hkconnect_path1_monthly_equal_buffered` 与 `hkconnect_path1_monthly_lowvol` 作为低换手/低回撤对照，不新增候选族。
- 跑完后以 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `results_hkconnect/tracked_winners_hkconnect.json` 为准，确认是否只是 sample/metrics 同步还是出现窗口赢家切换。

### 本轮快筛记录（2026-04-28 00:08 CST）

- 运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`：`trade_calendar` 在线更新失败，已回退本地缓存。
- 运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 后，港股 Path 1 tracked payload 与图表没有新增 git diff。
- 当前四窗口 winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`；`sample_end` 仍为 `2026-03-31`，`robust_candidate` 仍是同一策略（meanCAGR `27.97% / minCAGR 21.77%`）。

### 本轮快筛记录（2026-04-28 12:04 CST）

- 重新运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 四窗口 winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`，`sample_end` 仍为 `2026-03-31`，`robust_candidate` 仍是同一策略（meanCAGR `27.97% / minCAGR 21.77%`）。
- 本次回测把 `02493.HK 缺少 hk_daily_adj 数据，已跳过。` 写入各港股 summary warning；这属于 `results_hkconnect/**` 研究产物同步，不代表 Path 1 winner 切换。

### 本轮快筛记录（2026-04-28 18:29 CST）

- 重新运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 港股 Path 1 四窗口 winner 从 `hkconnect_path1_monthly_equal_buffered` 切换为 `hkconnect_path1_weekly_equal_buffered`，robust candidate 同步切换到该策略。
- 新 Path 1 winner 的四窗口口径为：`since_2017_01 / since_2020_01` 均为 `23.08% CAGR / -13.41% MaxDD / 1.2383 Sharpe / 9.72 Turnover`，`since_2023_01` 为 `35.04% CAGR / -13.41% MaxDD / 1.5530 Sharpe / 10.62 Turnover`，`since_2025_01` 为 `49.82% CAGR / -13.41% MaxDD / 1.7137 Sharpe / 13.03 Turnover`。
- 这次改写显著提高 CAGR 并小幅改善回撤，但换手从月频主线的约 `2.9-3.6` 抬到 `9.7-13.0`；下一轮需要继续用 `monthly_equal_buffered / lowvol` 做换手与低回撤对照。

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
1. 月度 / 双周 / 单周稳健（混合权重）
2. 月度 / 双周 / 单周熊市空仓
3. 月度 / 双周 / 单周等权缓冲
4. 月度 / 双周 / 单周低波偏稳

## 本轮迭代执行规则

- 沪港通 `Path 1` 作为**独立于 A 股**的研究线，每轮迭代都要单独评估，不并入 A 股 `winner_only_pass`。
- 默认回测窗口固定为：
  - `since_2017_01`
  - `since_2020_01`
  - `since_2023_01`
  - `since_2025_01`
  - `since_2026_01`（观察窗）
- 默认比较对象固定为当前 4 条港股 `Path 1` 候选主线，并同时比较月度 / 双周 / 单周调仓版本：
  - `hkconnect_path1_*_hybrid`
  - `hkconnect_path1_*_cashoff`
  - `hkconnect_path1_*_equal_buffered`
  - `hkconnect_path1_*_lowvol`
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
  - `hkconnect_path1_weekly_equal_buffered`
- `monthly_equal_buffered / monthly_lowvol` 保留为低换手与低回撤对照。
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

## 本轮补充（2026-04-23 19:59 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`：`trade_calendar` 与 `02940.HK` 继续走本地缓存回退路径，但港股 Path 1 回测完整完成。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 已更新为 `64b36ccb6a6e8e2f2f6aa58f90d7bcaceddfff1c4252add7e9d5312c84567283` 与 `e6a839d2c4315bbe0691ad4d52ddc697ebeb846652d5bc5c2662212e5b9f27b5`；这次变化来自 `sample_end` 前移到 `2026-04-23`，不是 Path 1 winner 改写。
- 当前四窗口 tracked winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.72% CAGR / -14.78% MaxDD / 1.3757 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.83% CAGR / -14.78% MaxDD / 1.7134 Sharpe / 2.89 Turn`
  - `since_2025_01`：`42.89% CAGR / -14.78% MaxDD / 1.5796 Sharpe / 3.47 Turn`
- `since_2026_01` raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`-3.57% CAGR / -5.52% MaxDD / -0.1460 Sharpe / 3.10 Turn`）。本轮 README / HISTORY / 港股对比图之所以刷新，是为了跟随港股 Path 2 的新 winner 一并同步；Path 1 自身继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 对照，不新增候选族。

## 本轮补充（2026-04-24）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 继续回退本地缓存，但港股 Path 1 的窗口赢家没有任何改写，实盘导出层也已同步到最新 tracked payload。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `a35621c7dfce801291e6c2482ef4a17a6071deeeb30a238adee9a34200bf98af` 与 `cc3c4429de9f026db201be9cee185fd388982488606045d104a1a59ddb938b72`；这轮变化来自重新生成完整 tracked payload 和图表，不是 Path 1 winner 切换。
- 当前四窗口 tracked winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.43% CAGR / -14.78% MaxDD / 1.3685 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.29% CAGR / -14.78% MaxDD / 1.7026 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.42% CAGR / -14.78% MaxDD / 1.5498 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.64% / minCAGR 23.43%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`-1.47% CAGR / -5.52% MaxDD / -0.0174 Sharpe / 3.10 Turn`）。
- 下一轮港股 `Path 1` 继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照，不新增候选族。

## 本轮补充（2026-04-25）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：本地 `trade_calendar` 更新仍失败并自动回退缓存，但这不影响港股 Path 1 的独立评估。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `893542dd28ae208a115a22d48f19bd1448bf2b30606892a825cb955aed7a3575` 与 `422d42394fa8731e51526973081debb58c6b537174485238018de37110589355`；这轮是同一 `sample_end=2026-04-24` 下的 metrics 漂移同步，不是新的 winner 切换。
- 当前四窗口 tracked winner 仍全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.29% CAGR / -14.78% MaxDD / 1.3613 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.40% CAGR / -14.78% MaxDD / 1.7051 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.72% CAGR / -14.78% MaxDD / 1.5563 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.68% / minCAGR 23.29%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`1.41% CAGR / -5.52% MaxDD / 0.1367 Sharpe / 3.10 Turn`）。
- 本轮需要同步刷新 README / HISTORY 的港股摘要文字，但不新增港股 `Path 1` 候选族；下一轮仍只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照。

## 本轮补充（2026-04-26）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 在线更新继续失败，但离线缓存回退路径正常，港股 `Path 1` 独立评估未受阻。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `54097028c3eaea664cb74a26890358c0ff5934a75943a3b0c591655fc4c9efbc` 与 `6ee86d107dc61a23e9b0ef45b839507a34bca7f9a86139c0ee3cb365d0dfe2e8`；这轮仍是同一 `sample_end=2026-04-24` 下的 metrics 漂移同步，不是新的 `Path 1` winner 切换。
- 当前四窗口 tracked winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.32% CAGR / -14.78% MaxDD / 1.3625 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.40% CAGR / -14.78% MaxDD / 1.7051 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.72% CAGR / -14.78% MaxDD / 1.5563 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.69% / minCAGR 23.32%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`1.41% CAGR / -5.52% MaxDD / 0.1367 Sharpe / 3.10 Turn`）。
- 本轮只把 README 港股摘要、tracked payload 与港股对比图同步到当前数值，不新增港股 `Path 1` 候选族；下一轮继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照。

## 本轮补充（2026-04-27）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 在线更新依旧失败，但离线缓存回退路径继续正常，港股 `Path 1` 独立评估未受阻。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 分别是 `54097028c3eaea664cb74a26890358c0ff5934a75943a3b0c591655fc4c9efbc` 与 `6ee86d107dc61a23e9b0ef45b839507a34bca7f9a86139c0ee3cb365d0dfe2e8`；这轮确认当前缓存口径的 `sample_end` 仍是 `2026-04-24`，不是新的 `2026-04-30` 样本扩展，也不是新的 `Path 1` winner 切换。
- 当前四窗口 tracked winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`23.32% CAGR / -14.78% MaxDD / 1.3625 Sharpe / 2.88 Turn`
  - `since_2023_01`：`34.40% CAGR / -14.78% MaxDD / 1.7051 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.72% CAGR / -14.78% MaxDD / 1.5563 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.69% / minCAGR 23.32%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`1.41% CAGR / -5.52% MaxDD / 0.1367 Sharpe / 3.10 Turn`）。
- 下一轮港股 `Path 1` 继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照，不新增候选族。

## 本轮补充（2026-04-27 09:08 CST）

- 本轮再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`trade_calendar` 在线更新仍失败，但离线缓存已经把港股 Path 1 payload 真正推进到 `sample_end=2026-04-30`。
- 当前 `results_hkconnect/strategy_comparison_hkconnect.csv` 与 `tracked_winners_hkconnect.json` 的 SHA256 已更新为 `83885b39cb11f568d0ce2772e4cbaa9a0c6c1b62c089127e89eb39bbba12ceed` 与 `d5d3bc0cf9a03aeb713d76efd76d2687be6d0d47f65f784dcd12734bf1062d4f`；这说明上一条“仍停在 2026-04-24” 的判断已经过时。
- Path 1 四窗口 tracked winner 继续全部是 `hkconnect_path1_monthly_equal_buffered`，但长窗口指标已按新的月末口径小幅漂移：
  - `since_2017_01 / since_2020_01`：`23.12% CAGR / -14.78% MaxDD / 1.3571 Sharpe / 2.89 Turn`
  - `since_2023_01`：`34.40% CAGR / -14.78% MaxDD / 1.7051 Sharpe / 2.89 Turn`
  - `since_2025_01`：`41.72% CAGR / -14.78% MaxDD / 1.5563 Sharpe / 3.47 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 30.59% / minCAGR 23.12%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`1.41% CAGR / -5.52% MaxDD / 0.1367 Sharpe / 3.10 Turn`）。
- 下一轮港股 `Path 1` 继续只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照，不新增候选族。

## 本轮补充（2026-04-27 18:09 CST）

- 本轮在主工作树直接运行 `./.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后执行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`。回测完整完成，但当前 tracked payload 的真实 `as_of` 仍是 `2026-04-24`，月频样本止于 `2026-03-31`，不是上一条记录里的 `2026-04-30` 口径。
- Path 1 四窗口 tracked winner 没有切换，继续全部是 `hkconnect_path1_monthly_equal_buffered`：
  - `since_2017_01 / since_2020_01`：`21.77% CAGR / -14.78% MaxDD / 1.2947 Sharpe / 2.91 Turn`
  - `since_2023_01`：`32.23% CAGR / -14.78% MaxDD / 1.6150 Sharpe / 2.93 Turn`
  - `since_2025_01`：`36.11% CAGR / -14.78% MaxDD / 1.3635 Sharpe / 3.60 Turn`
- `robust_candidate` 继续是 `hkconnect_path1_monthly_equal_buffered`（`meanCAGR 27.97% / minCAGR 21.77%`）；`since_2026_01` 观察窗 raw leader 仍是 `hkconnect_path1_monthly_lowvol`（`-27.91% CAGR / -5.52% MaxDD / -2.2545 Sharpe / 3.74 Turn`）。
- 本轮需要同步 README 与 tracked payload 来纠正港股摘要的 stale `2026-04-30` 数值；下一轮仍只保留 `monthly_equal_buffered` 主攻和 `monthly_lowvol` 低回撤对照，不新增港股 Path 1 候选族。
