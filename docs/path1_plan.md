# Path 1 研究计划

本文档用于约束和记录 `Path 1`（胜出者核心主线）的研究方向。  
目标不是无约束追求收益上限，而是在保持框架可交易、可复用、可解释的前提下，把当前常见的 `20%~26% CAGR` 推向 `25%~30%+ CAGR`。  
当前已把 `Path 1` 的单轮探索预算提升到 **`24-28` 个 base candidates / `5` 个固定方向**，并要求候选按方向分组生成，而不是只做参数邻域微调。

## 本轮执行计划（2026-05-04）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-05-04 03:57 CST）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不补跑确认回测。
- 最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，继续被回撤阈值挡住；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，但 Sharpe 仍低于当前 winner。
- A 股 Path 2 新增的 `prom1 core_3_1 cap100` 微批量不并入 Path 1 fast pass；Path 1 继续保持固定方向与固定快筛预算。

## 本轮执行计划（2026-05-03）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-05-03 00:16 CST；06:11 CST 复核）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不补跑确认回测。
- 最近似候选仍被同一组阈值挡住：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，回撤恶化仍超阈值；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，但 Sharpe 仍低于当前 winner。

### 本轮补充（2026-05-03 12:05 CST）

- 在 A 股 Path 2 新增 `prom1 cap100 risk50/full_risk` 微批量并重建 comparison CSV 到 `2331` 行 / `599` 个 base strategies 后，重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮仍不触发确认回测。
- 最近似候选排序不变：`since_2020_01` 仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD -25.00%` 继续超过替换阈值；`since_2025_01` 仍是 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`，但 Sharpe 低于当前 winner。

### 本轮补充（2026-05-03 18:13 CST）

- 在 A 股 Path 2 新增 `70/30` 与 `60/40` 等权底座的 `prom1 cap100` 微批量并重建 comparison CSV 到 `2363` 行 / `607` 个 base strategies 后，重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不触发确认回测，也不把新增 Path 2 底座结构并入 Path 1 fast pass。
- 最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 继续受 `MaxDD -25.00%` 阻挡；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 仍是高 CAGR 但 Sharpe 不达标。

## 本轮执行计划（2026-05-02）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-05-02）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`run_date=2026-05-02 / data_as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写，因此本轮不补跑确认回测。
- 最近似候选仍被原有阈值挡住：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，收益与 Sharpe 更高但回撤恶化仍超阈值；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，Sharpe 仍低于当前 winner。

### 本轮补充（2026-05-02 06:07 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`，确认 `results/winner_only_pass.json` 的 `as_of` 应按本地市场结果数据截止日记录为 `2026-04-30`，不是自动化运行日。
- 四个 Path 1 tracked winners 仍未改写；本轮不触发确认回测，也不把 A 股 Path 2 新增候选并入 Path 1 fast pass。
- 最近似候选排序保持不变：`since_2020_01` 仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD -25.00%` 继续超过替换阈值；`since_2025_01` 仍是 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`，但 Sharpe 仍低于当前 winner。

### 本轮补充（2026-05-02 12:10 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮仍不补跑确认回测。
- 最近似候选继续受同一组条件阻挡：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 为 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，但 Sharpe 低于当前 winner。

### 本轮补充（2026-05-02 18:08 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；本轮不补跑确认回测。
- 最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 继续受 `MaxDD -25.00%` 阻挡；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 虽有更高 CAGR，但 Sharpe 仍低于当前 winner。

## 本轮执行计划（2026-05-01）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-05-01）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-05-01 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写，因此本轮不补跑确认回测。
- 最近似候选仍被同一组风险约束挡住：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 达到 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，但回撤恶化仍超过替换阈值；`since_2023_01` 的 `aggr_10_90_hold_4_6__port_weekly_exposure` 达到 `30.93% CAGR`，但 Sharpe 与 MaxDD 仍不合格。
- 本轮新增的 A 股 Path 2 高集中原型不并入 Path 1 候选池；Path 1 继续保持固定方向和固定快筛预算。

### 本轮补充（2026-05-01 06:11 CST）

- 在 A 股 Path 2 微批量并重建 comparison CSV 后，重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-05-01 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 仍未改写；`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 `MaxDD -25.00%` 仍超过替换阈值。
- 本轮 Path 1 不触发确认回测；新增的 A 股 Path 2 晋升 3 只高集中原型继续只服务无约束上限探索，不并入 Path 1。

### 本轮补充（2026-05-01 12:11 CST）

- 再次运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-05-01 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 在 A 股 Path 2 新增 `core_3_1` 高集中原型并重建 comparison CSV 到 `2139` 行 / `551` 个 base strategies 后复跑快筛，四个 Path 1 tracked winners 仍未改写。
- 最近似候选仍未过阈值：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 为 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`，回撤恶化仍超过替换条件；本轮不补跑 Path 1 确认回测。

### 本轮补充（2026-05-01 18:14 CST）

- 先发现共享 `results/strategy_comparison_base_method.csv` 只剩 `17` 行，按本地 `summary.json` 缓存重建到 `2139` 行 / `551` 个 base strategies 后运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-05-01 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 初筛一度把 `since_2020_01` 的 `aggr_08_92_prom6__sat_three_stage_buffered` 标为可疑改善；随后补跑当前 tracked winner 与该候选的 `since_2020_01` 确认回测，并再次重建 comparison CSV。
- 同口径复筛后四个 Path 1 tracked winners 未改写：当前 `since_2020_01` winner 同步为 `aggr_10_90_prom6__sat_three_stage_buffered`（`25.99% CAGR / -21.53% MaxDD / 0.9185 Sharpe / 0.66 Turnover`）；`aggr_08_92_prom6__sat_three_stage_buffered` 仅 `26.17% CAGR / -21.78% MaxDD / 0.9205 Sharpe`，Sharpe 改善不足；`aggr_05_95_prom7__sat_three_stage_buffered` 仍受 `-25.00% MaxDD` 阻挡。
- 本轮 Path 1 不新增候选族，也不把 A 股 Path 2 高频原型并入 fast pass。

## 本轮执行计划（2026-04-30）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持 `24` 个 fast-pass base candidates / `168` 个展开候选。
- `weekly_exposure_path` 继续优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-04-30）

- 先发现共享 `results/strategy_comparison_base_method.csv` 被压缩到 `73` 行，随后用本地 `summary.json` 缓存重建到 `1477` 行 / `500` 个 base strategies，再重跑 `.venv/bin/python scripts/winner_only_pass.py`。
- 重跑后输出为：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 继续未改写，因此不补跑确认回测。
- 最近似候选仍不满足替换条件：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 达到 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe / 0.67 Turnover`，收益和 Sharpe 更高但回撤恶化超阈值；`since_2023_01` 的 `aggr_10_90_hold_4_6__port_weekly_exposure` 达到 `30.93% CAGR`，但 Sharpe 降到 `0.8987` 且 MaxDD 扩到 `-31.82%`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 达到 `104.59% CAGR`，但 Sharpe 低于当前 tracked winner。

### 本轮补充（2026-04-30 06:35 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`，并在 Path 2 微批量回测后重建完整 comparison CSV 再复跑一次；输出仍为 `as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 均未改写，最近似候选仍是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 回撤恶化过大，`since_2023_01` 的 `aggr_10_90_hold_4_6__port_weekly_exposure` Sharpe/MaxDD 不合格，`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` Sharpe 低于当前 winner。
- 本轮 Path 1 不触发确认回测；后续仍保留 `weekly_exposure_path` 中 `buffered / asym` 的固定对照顺序。

### 本轮补充（2026-04-30 12:12 CST）

- 再次运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；最近似候选仍被同一组回撤或 Sharpe 条件挡住，因此本轮不补跑确认回测。
- 本轮新增的 A 股 Path 2 微批量只用于无约束上限探索，不并入 Path 1 候选池；Path 1 仍限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个方向内。

### 本轮补充（2026-04-30 18:16 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-30 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 Path 1 tracked winners 继续未改写；`since_2020_01` 最近似候选仍是 `aggr_05_95_prom7__sat_three_stage_buffered`，但 MaxDD 扩到 `-25.00%`，不满足替换阈值。
- 本轮 Path 1 不触发确认回测；新增的 A 股 Path 2 高集中原型仍只服务无约束上限探索。

## 上轮执行计划（2026-04-29）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持约 `24-28` 个 fast-pass base candidates 的预算。
- `weekly_exposure_path` 仍优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`；只有候选明确改写窗口赢家时，才补跑必要确认回测。

### 本轮快筛记录（2026-04-29 12:03 CST）

- 先发现共享 `results/strategy_comparison_base_method.csv` 只剩 `73` 行，随后用缓存 `summary.json` 重建到 `1947` 行 / `503` 个 base strategies，再运行 `.venv/bin/python scripts/winner_only_pass.py`。
- 重跑后输出为：`as_of=2026-04-29 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 继续未改写，因此不补跑确认回测；最接近的 `since_2020_01` challenger 是 `aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`），收益和 Sharpe 更高但回撤恶化超阈值。
- `since_2025_01` 最接近候选仍是 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered`（`104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`），收益更高但 Sharpe 与回撤都不满足替换条件。

### 本轮快筛记录（2026-04-29 18:50 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-29 / base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 仍未改写，因此不补跑确认回测。
- 最近似候选继续是同一组：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 达到 `27.83% CAGR / -25.00% MaxDD / 1.0264 Sharpe`，收益和 Sharpe 更高但回撤恶化超阈值；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 达到 `104.59% CAGR / -11.26% MaxDD / 2.2339 Sharpe`，收益更高但 Sharpe 与回撤不满足替换条件。

## 上轮执行计划（2026-04-28）

- 本轮继续限定在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个固定方向内，不新增 Path 1 候选族。
- 快筛优先运行 `.venv/bin/python scripts/winner_only_pass.py`，维持约 `24-28` 个 fast-pass base candidates 的预算。
- `weekly_exposure_path` 仍优先比较 `__port_weekly_exposure_buffered` 与 `__port_weekly_exposure_asym`，只在候选明确改写窗口赢家时补跑确认回测。

### 本轮快筛记录（2026-04-28 00:05 CST）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`：`base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 未改写；本轮不触发确认回测。
- 最接近但未通过阈值的候选仍集中在 `holding_shape / weekly_exposure_path`：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 把 CAGR 抬到 `27.83%`，但 MaxDD 扩到 `-25.00%`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 把 CAGR 抬到 `104.59%`，但 Sharpe 低于当前 tracked winner。

### 本轮快筛记录（2026-04-28 12:04 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 继续未改写，因此不补跑确认回测。
- 最近似候选仍不是合格晋级：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 提升 CAGR 至 `27.83%`，但 MaxDD 扩到 `-25.00%`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 提升 CAGR 至 `104.59%`，但 Sharpe 降到 `2.2339`，低于当前 tracked winner。

### 本轮快筛记录（2026-04-28 18:29 CST）

- 重新运行 `.venv/bin/python scripts/winner_only_pass.py`：`base_candidates=24 / total_candidates=168 / evaluated=168`。
- 四个 tracked winners 继续未改写，因此不补跑确认回测。
- 最接近但未通过阈值的候选仍集中在 `holding_shape / weekly_exposure_path`：`since_2020_01` 的 `aggr_05_95_prom7__sat_three_stage_buffered` 达到 `27.83% CAGR`，但 MaxDD 扩到 `-25.00%`；`since_2025_01` 的 `aggr_08_92_prom6_core_6_1__port_weekly_exposure_buffered` 达到 `104.59% CAGR`，但 Sharpe `2.2339` 低于当前 tracked winner。

## 1. 当前目标

- 路线：`Path 1` 渐进优化
- 主目标：
  - 把 `2017 / 2020 / 2023 / 2025` 四个窗口里的主力版本继续往上推
  - 优先改进 `2020` 和 `2023` 两个窗口
  - 不明显恶化 `Max DD / Sharpe / Turnover`
- 当前研究原则：
  - 尽量不破坏现有 `winner_core` 主线
  - 优先动系统风险层、晋升节奏、卫星仓行为
  - 每次迭代固定试 `5` 个有明确假设的方向
  - 单轮快筛候选预算控制在 `24-28` 个 base candidates

## 2. 当前主线假设

当前 `Path 1` 的核心假设如下：

1. `winner_core` 主线仍然是有效框架，问题不在于“是否保留 winner_core”，而在于“如何更早、更平滑地把强者放大”。
2. 周频系统风险覆盖层如果直接作用于整个组合，通常会伤害收益；但如果只作用于卫星仓，则更有希望改善收益-回撤比。
3. 卫星仓三档风控（`100 / 60 / 30`）优于简单两档，且在进攻主线上配合更少触发次数会进一步改善结果。
4. `cash_off` 线更偏防守，继续叠加太多额外确认逻辑，边际收益有限；更适合保留为防守候选，而不是主攻优化对象。
5. Path 1 的优化应该优先来自：
   - 卫星仓风控
   - 晋升核心后的加仓节奏
   - 月度选股 + 周度仓位调整
   - 触发机制的节奏控制
   而不是频繁改动股票池或彻底换框架。

## 3. 当前默认候选生成

当前 `Path 1` 快速迭代不是扫全部 `winner_core` 变体，而是从显式候选方向组中生成。  
当前默认是 **`5` 个方向组 / `23` 个 fast-pass 变体（对应 `24` 个 base candidates）**（以 `backtest_marketcap_etf.py` 中 `PATH1_FAST_PASS_DIRECTION_GROUPS / PATH1_FAST_PASS_VARIANT_IDS` 为准）；周频 companion 和月度选股/周度仓位调整 companion 会在此基础上自动展开到更大的快筛集合：

1. `promotion_ramp`
   - `aggr_10_90_fast_ramp`
   - `aggr_10_90_prom5`
   - `aggr_10_90_prom6`
   - `aggr_10_90_prom7`
   - `aggr_10_90_prom7_ramp90`
2. `satellite_defense`
   - `aggr_08_92_prom6_cash_off`
   - `aggr_08_92_prom6_cash_off_and`
   - `aggr_10_90_prom6_cash_off`
   - `aggr_10_90_fast_ramp_cash_off`
   - `aggr_10_90_fast_ramp_cash_off_and`
3. `signal_variants`
   - `aggr_08_92_prom6_core_6_1`
   - `aggr_10_90_prom6_core_6_1`
4. `holding_shape`
   - `share_15_85_hold_4_6`
   - `aggr_10_90_hold_4_6`
   - `share_12_88_hold_4_6`
   - `aggr_09_91_prom7`
   - `aggr_08_92_hold_3_6`
   - `aggr_08_92_hold_3_6_ramp90`
   - `aggr_05_95_prom7`
5. `supporting_variants`
   - `aggr_08_92_prom6`
   - `aggr_08_92_prom6_ramp90`
   - `aggr_08_92_prom7`
   - `aggr_08_92_prom7_ramp90`

说明：

- 这组候选是“Path 1 fast pass”的研究入口，不代表全部可用策略。
- 正式确认回测仍然可以扩展到更宽的 `research active family`。
- 如果某一轮出现更优的 companion 版本（例如卫星风控 companion），可以追加进入 fast pass 候选，但应写明加入原因。
- 每轮不要求全部候选都进入完整确认；fast pass 的职责是先筛出每个方向里最值得晋级的 `1-2` 个。
- `2026-04-24` 起，`fast_ramp_cash_off_and / hold_3_6 / hold_3_6_ramp90 / aggr_05_95_prom7` 已正式纳入 `Path 1 fast pass`，用于把固定方向内的 base budget 提升到 `24`，但仍不把 `signal_variants` 重新拉回主攻列表。
- 对 `weekly_exposure_path`，完整确认只允许以下 3 个版本参与：
  - `__port_weekly_exposure`
  - `__port_weekly_exposure_buffered`
  - `__port_weekly_exposure_asym`

## 4. 下一轮优先尝试的方向（每轮固定 5 个）

## 4.1 本轮（2026-04-21）执行清单（限定 5 个方向）

本轮 `Path 1` 研究严格限定在以下 `5` 个方向内（其余方向不主动展开）：

1. **晋升核心后的分阶段加仓节奏（promotion_ramp）**：继续围绕 `ramp90` 与更快晋升/加仓的组合，优先看 `since_2020_01 / since_2023_01` 是否能抬高 `CAGR` 且不明显恶化 `Max DD / Turnover`。
2. **卫星仓防守（satellite_defense）**：只围绕“卫星仓风控 overlay”相关候选（含 `cash_off(_and)` 线），不扩大到全组合周频 overlay。
3. **持仓形态与晋升容量（holding_shape）**：把 `share / prom` 结构性候选作为独立方向，观察结构变化对 `Sharpe / Turnover` 的影响。
4. **月度选股 + 周度仓位调整（weekly_exposure_path）**：月度篮子固定、周内只调总仓位，优先检验它是否能在不明显伤害 `CAGR` 的前提下改善 `Max DD / Sharpe`，并更贴近真实执行节奏。该方向下只比较 `__port_weekly_exposure / __port_weekly_exposure_buffered / __port_weekly_exposure_asym` 三个 companion。
5. **支持性微调（supporting_variants）**：仅保留 `aggr_08_92_prom6(_ramp90)` 作为“更接近主线”的对照与补位候选，避免新增大范围参数扫。

对应的执行约束（本轮继续沿用）：

- 快筛只跑 `scripts/winner_only_pass.py`，候选只来自 `winner_core` 主线 + 显式 fast-pass 变体（含卫星 overlay 与月度选股/周度仓位调整 companion）。
- 只有当候选**明确改写**某个窗口赢家，且指标满足“不明显恶化回撤/换手”的阈值，才考虑补跑必要确认回测。
- 本轮暂不把 `signal_variants` 作为主攻方向（过去多次出现“CAGR 上升但 Sharpe/回撤/换手显著恶化”的形态）。
- `weekly_exposure_path` 的晋级优先级固定为：
  1. `__port_weekly_exposure_buffered`
  2. `__port_weekly_exposure_asym`
  3. `__port_weekly_exposure`
- `weekly_exposure_path` 的最小判定口径固定为：
  - `since_2020_01`
  - `since_2023_01`
  - `Total Return / CAGR / MaxDD / Sharpe / Turnover`
- 当前默认推进结论：
  - `aggr_10_90_prom6` 主线优先继续压回撤
  - `aggr_08_92_prom6_cash_off` 主线优先继续观察 `buffered`

### 本轮已完成的最小对照（2026-04-21）

#### A. `aggr_10_90_prom6`

- `since_2020_01`
  - 原版：`Total Return 291.43% / CAGR 24.04% / MaxDD -21.61% / Sharpe 0.8899 / Turnover 2.88`
  - `__port_weekly_exposure`：`336.49% / 26.20% / -24.36% / 0.9077 / 0.90`
  - `__port_weekly_exposure_buffered`：`339.65% / 26.34% / -23.59% / 0.9103 / 0.86`
  - `__port_weekly_exposure_asym`：`327.60% / 25.79% / -23.87% / 0.9189 / 0.83`
- `since_2023_01`
  - 原版：`Total Return 110.05% / CAGR 24.94% / MaxDD -28.32% / Sharpe 0.8459 / Turnover 2.96`
  - `__port_weekly_exposure`：`122.75% / 27.16% / -32.14% / 0.8391 / 0.99`
  - `__port_weekly_exposure_buffered`：`123.02% / 27.21% / -31.55% / 0.8415 / 0.95`
  - `__port_weekly_exposure_asym`：`116.16% / 26.02% / -31.22% / 0.8430 / 0.88`

结论：

- `weekly_exposure_path` 在该主线上是有效方向；
- `buffered` 当前是默认主攻版本；
- `asym` 作为“快减慢加”备选保留，但下一轮重点应转向继续压回撤。

#### B. `aggr_08_92_prom6_cash_off`

- `since_2020_01`
  - 原版：`Total Return 256.63% / CAGR 22.23% / MaxDD -15.47% / Sharpe 0.9466 / Turnover 2.23`
  - `__port_weekly_exposure`：`255.40% / 22.17% / -14.31% / 0.9632 / 0.54`
  - `__port_weekly_exposure_buffered`：`258.12% / 22.31% / -15.06% / 0.9622 / 0.53`
  - `__port_weekly_exposure_asym`：`253.89% / 22.09% / -14.31% / 0.9614 / 0.54`
- `since_2023_01`
  - 原版：`Total Return 118.80% / CAGR 26.48% / MaxDD -12.34% / Sharpe 1.0938 / Turnover 2.41`
  - `__port_weekly_exposure`：`120.29% / 26.74% / -12.55% / 1.1176 / 0.58`
  - `__port_weekly_exposure_buffered`：`121.32% / 26.91% / -12.55% / 1.1251 / 0.57`
  - `__port_weekly_exposure_asym`：`120.26% / 26.73% / -12.55% / 1.1175 / 0.58`

结论：

- `weekly_exposure_path` 在该防守主线上也成立；
- `buffered` 当前是更稳健的默认候选；
- 下一轮优先保留 `buffered`，其余两个版本仅作为对照。

## 4.0 上轮（2026-04-19）执行清单（限定 5 个方向）

上轮 `Path 1` 研究严格限定在以下 5 个方向内（其余方向不主动展开）：

1. **卫星仓三档风控的非对称确认**：继续围绕 `__sat_three_stage_risk / __sat_three_stage_buffered` 两条线对比，优先看 `since_2020_01 / since_2023_01` 是否能抬高 `CAGR` 同时不明显恶化 `Max DD / Turnover`。
2. **卫星仓三档风控的更少触发次数**：以 `buffered`（双周确认）为主，观察是否能减少无效来回切换并改善 `Sharpe`。
3. **晋升核心后的分阶段加仓节奏**：优先把“分步加仓”（例如 `ramp90`）纳入 fast-pass 候选，观察 `2020/2023` 的收益弹性与回撤代价。
4. **持仓形态与晋升容量微调**：把 `hold_4_6 / prom7 / 15/85` 这一类结构性候选作为独立方向，不再夹带在其他方向里顺手试。
5. **卫星仓专用周频风控 companion 的家族化管理**：仅维护真正有效的卫星 companion（不再扩大到全组合 overlay）。

对应的执行约束：

- 快速筛选只跑 `scripts/winner_only_pass.py`，并且候选只来自 `winner_core` 主线 + 显式 fast-pass 变体（含卫星 companion）。
- 只有当候选**明确改写**某个窗口赢家，且指标满足“不明显恶化回撤/换手”的阈值，才考虑补跑必要确认回测。

### 上轮快筛记录（2026-04-19）

- `scripts/winner_only_pass.py`（Path 1 fast pass）未发现“清晰改写”窗口赢家的候选。
- 补充（2026-04-19 20:50）：重跑 fast pass，窗口赢家结论不变；最接近改写的仍集中在 `since_2023_01: aggr_10_90_fast_ramp_cash_off`（收益/回撤更好但换手显著更高）。
- 近似候选（但未通过回撤/换手阈值）：
  - `since_2023_01`：`aggr_10_90_fast_ramp_cash_off` 小幅抬高 `CAGR/Sharpe` 且 `Max DD` 更好，但 `Turnover` 增幅过大。
  - `since_2020_01`：`aggr_08_92_prom6_ramp90__sat_three_stage_buffered` 小幅抬高 `CAGR`，但 `Sharpe` 改善不足且 `Max DD` 略差（未满足阈值）。
  - `since_2017_01`：`aggr_08_92_prom6_cash_off_and` 抬高 `CAGR/Sharpe`，但 `Max DD` 明显更差。

### A. 卫星仓三档风控的非对称确认

假设：

- 风险恶化时快减仓
- 风险修复时慢加回

目标：

- 保持 `2020 / 2023` 收益不掉队
- 进一步降低不必要的卫星仓来回切换

预期：

- 更有希望继续提升 `Sharpe`
- 有机会在不牺牲 `CAGR` 的情况下小幅改善 `Max DD`

### B. 卫星仓三档风控的更少触发次数

假设：

- 当前三档已经有效，但仍可能有少量无效来回切换

目标：

- 在 `aggr_10_90_prom6` 主线上继续降低触发次数
- 优先观察 `2023` 窗口是否还能继续抬高

预期：

- 进攻主线受益更明显
- `cash_off` 线可能边际改善有限

### C. 晋升核心后的分阶段加仓节奏

假设：

- 现在的晋升核心有效，但仍可能不够快或不够重

目标：

- 在不改选股框架的前提下，优化胜出者被放大的节奏

预期：

- 主要改善 `2020 / 2023`
- 风险是换手和回撤回升，需要严格约束

### D. 卫星仓专用周频风控 companion 的家族化管理

假设：

- companion 版本已经成为有效增强项

目标：

- 把真正有效的 companion 固定纳入 Path 1 研究候选
- 把无效 companion 移回 archive-like 状态

预期：

- 提升研究效率
- 减少无意义的候选扫描

## 4.1 本轮（2026-04-20）执行清单（限定 5 个方向）

本轮 `Path 1` 研究严格限定在以下 `5` 个方向内（与 fast-pass 方向组一致，不额外扩张）：

1. **晋升核心后的分阶段加仓节奏（promotion_ramp）**：优先观察 `since_2020_01 / since_2023_01` 的收益弹性与回撤代价。
2. **卫星仓防守线（satellite_defense）**：优先看 `cash_off` / `cash_off_and` / `fast_ramp_cash_off` 是否能改善 `2023` 的收益-回撤比并控制换手。
3. **信号变体（signal_variants）**：仅在不明显恶化回撤/换手的前提下，观察 `core_6_1` 在 `2020/2023` 的边际收益。
4. **持仓形态（holding_shape）**：把 `hold_4_6 / prom7` 作为结构性候选独立观察，避免夹带在其他方向里顺手试。
5. **支撑性变体（supporting_variants）**：仅保留 `prom6` 与 `prom6_ramp90` 两个支撑线，用于对照“加仓节奏”是否真的带来持续改进。

对应执行约束（本轮继续沿用）：

- 快速筛选只跑 `scripts/winner_only_pass.py`，候选只来自 `winner_core` 主线 + 显式 fast-pass 变体（含卫星 overlay 后缀）。
- 只有当候选**明确改写**某个窗口赢家，且指标满足“不明显恶化回撤/换手”的阈值，才考虑补跑必要确认回测。

### 本轮快筛记录（2026-04-20）

- `.venv/bin/python scripts/winner_only_pass.py`（`as_of=2026-04-20`）未发现“清晰改写”窗口赢家的候选。
- 补充（2026-04-20 13:21）：重跑 `scripts/winner_only_pass.py`，结论不变（`evaluated=26`）。
- 补充（2026-04-20 18:54）：再次重跑 `scripts/winner_only_pass.py`，结论不变（`base_candidates=13 / total_candidates=52 / evaluated=26`）。
- 补充（2026-04-20 20:23）：运行 `scripts/winner_only_pass.py`，结论不变（`base_candidates=13 / total_candidates=52 / evaluated=26`）。
- 补充（2026-04-21 10:17）：先重建 `strategy_comparison_base_method.csv`（覆盖 `since_2017_01/2020_01/2023_01`）后运行 `scripts/winner_only_pass.py`，`as_of=2026-04-21`；仍未发现“清晰改写”窗口赢家的候选。
- 补充（2026-04-21 12:13）：运行 `scripts/winner_only_pass.py`，结论不变（`base_candidates=13 / total_candidates=52 / evaluated=26`）。
- 补充（2026-04-21 14:18）：运行 `scripts/winner_only_pass.py --scan-prefix core_explore_80_20_total_mv_winner_core`，结论不变（`base_candidates=66 / evaluated=47`）。
- 补充（2026-04-21 16:36）：运行 `scripts/winner_only_pass.py`，结论不变（`base_candidates=13 / total_candidates=91 / evaluated=26`）。
- 补充（2026-04-21 17:57）：运行 `scripts/winner_only_pass.py`，结论不变（`base_candidates=20 / total_candidates=140 / evaluated=34`）。
- 扫描范围（fast pass + 卫星/组合 overlay）：`base_candidates=20 / total_candidates=140 / evaluated=34`。
- 当前阈值（guardrails）：`minCAGR=+0.10%`、`minSharpe=+0.005`、`MaxDD` 允许恶化 `<=0.50%`、`Turnover` 允许上升 `<=+0.15`。
- 近似候选（但未通过回撤/换手/Sharpe 阈值）：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__sat_three_stage_buffered`（ΔCAGR `+0.18%`、ΔSharpe `+0.0031`，Sharpe 改善不足且 MaxDD 略差）。
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1`（CAGR 更高但 Sharpe 更低，且回撤/换手显著恶化）。
  - `since_2017_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off_and`（CAGR/Sharpe 更高但回撤与换手恶化过大）。

## 5. 已淘汰或暂缓的方向

### 5.1 全组合周频 overlay

结论：

- 已验证为明显不优，暂不并入主线。

原因：

- 普遍出现收益下降
- 或回撤恶化
- 或收益与夏普都不占优

当前处理：

- 仅保留代码实验痕迹，默认不进入主线候选

### 5.2 纯核心集中策略（`pure_core_growth`）

结论：

- 已确认不适合作为当前主攻方向。

原因：

- 高集中放大了错误信号
- 在多个窗口里明显跑输主线
- 更像“放大噪音”，不是“更早抓住核心”

当前处理：

- 保留历史结果，不再进入 active family

### 5.3 对 `cash_off` 线继续叠加过多确认机制

结论：

- 暂缓。

原因：

- 边际改进很小
- 更适合作为防守备选，不是主攻收益突破的最优对象

## 6. 本轮执行规范

每次自动/手动 Path 1 迭代，应尽量遵守：

1. 先从 `Path 1 fast pass` 候选开始。
2. 每轮尽量只试 `3-5` 个方向，不做无差别全扫。
3. 单轮快筛候选数控制在 `8-12` 个；完整确认只允许少数晋级候选进入。
4. 每个方向必须能回答：
   - 当前假设是什么？
   - 预期改善哪一项指标？
   - 为什么值得试？
5. 如果某方向连续多轮没有进入任何窗口最优或接近最优，应写入“淘汰/暂缓”。
6. 若出现新的有效 companion 或新主线变体，应补充进本文档。

## 7. 维护说明

本文档用于研究规划，不用于自动写死最新回测数字。  
最新赢家和指标仍以：

- `README.md` 顶部自动区块
- `HISTORY.md`
- `results/weighted_track_winners.json`

为准。

## 8. 本轮补充（2026-04-21 18:24）

- 重跑 `scripts/winner_only_pass.py`（Path 1 fast-pass）：未发现“清晰改写窗口赢家”的候选（主要问题仍集中在 `MaxDD/Turnover` 约束未通过）。

## 9. 本轮补充（2026-04-21 20:18）

- 重跑 `scripts/winner_only_pass.py`（Path 1 fast-pass）：结论不变，未发现满足阈值的 `clear improvement`。

## 10. 本轮补充（2026-04-21 22:20）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`（Path 1 fast-pass）：`as_of=2026-04-21 base=20 total=140 eval=34`；四窗口赢家不变，未出现满足阈值的 `clear improvement`。

## 11. 本轮补充（2026-04-22）

- 运行 `.venv/bin/python scripts/winner_only_pass.py`（Path 1 fast-pass）：`as_of=2026-04-22 base=20 total=140 eval=34`；四窗口赢家继续不变，未出现满足阈值的 `clear improvement`。
- `since_2020_01` 最接近改写的仍是 `aggr_08_92_prom6__sat_three_stage_buffered`：`CAGR 25.33% / Sharpe 0.9238 / MaxDD -21.83% / Turn 0.67`，相对当前 `aggr_10_90_prom6__sat_three_stage_buffered` 只有很小收益优势，但 `MaxDD` 略差，未通过阈值。
- `since_2023_01` 继续最值得保留的近似候选是 `aggr_10_90_fast_ramp_cash_off`：`CAGR 27.06% / Sharpe 1.1488 / MaxDD -9.90%`，但 `Turnover 2.37` 仍明显高于当前赢家 `0.96`，问题仍是换手。
- `since_2017_01` 的 `aggr_08_92_prom6_cash_off_and` 依旧表现为“收益/Sharpe 更高但回撤与换手显著恶化”的形态，因此下一轮不应把 `cash_off_and` 扩成主攻方向。
- 下一轮默认继续只压 `promotion_ramp / satellite_defense / weekly_exposure_path` 三个方向；`signal_variants` 仍只保留观察，不回到主攻列表。
- 本次再次用 `AIINVESTOR_FORCE_OFFLINE=1` 重跑后，`since_2023_01` 的 raw-CAGR 前两名仍是 `aggr_08_92_prom6_core_6_1 / aggr_10_90_prom6_core_6_1`，但两者的 `Sharpe / MaxDD / Turnover` 都明显差于当前赢家；因此真正保留为下一轮 sidecar challenger 的仍应是 `aggr_10_90_fast_ramp_cash_off`，而不是把 `signal_variants` 重新拉回主攻清单。
- `2026-04-22 06:27 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出与上述一致，四窗口仍无 `clear improvement`；因此本轮不补任何 A 股 Path 1 确认回测。
- 在新增 `Path 2` 原型并重建 `results/strategy_comparison_base_method.csv` 后，再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-22 base=20 total=140 eval=34`，说明 `Path 1` 的近似 challenger 顺位没有被旁路线干扰。
- 当前最接近改写 `since_2020_01` 的仍是 `aggr_08_92_prom6__sat_three_stage_buffered`，最值得保留的 `since_2023_01` sidecar challenger 仍是 `aggr_10_90_fast_ramp_cash_off`；因此本轮结束时 `Path 1` 继续只保留快筛记录，不新增确认回测。
- 当日后续先用缓存重建了 `results/strategy_comparison_base_method.csv`（`427` 行 / `154` 个 base strategies），再运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：结论仍不变，说明此前被局部回测覆盖过的 comparison CSV 已恢复到可用基线。
- 以这次重建后的完整 comparison CSV 为准，`since_2020_01` 当前赢家是 `aggr_10_90_prom6__sat_three_stage_buffered`（`25.27% CAGR / 0.9222 Sharpe / -21.59% MaxDD / 0.67 Turn`）；最接近挑战者 `aggr_08_92_prom6__sat_three_stage_buffered` 只做到 `25.46% / 0.9253 / -21.83% / 0.66`，仍因 `Sharpe` 改善不足且 `MaxDD` 略差而未过阈值，所以本轮继续不补确认回测。
- `2026-04-22 14:30 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-22 base=20 total=140 eval=34`，四窗口 tracked winner 继续不变。
- 本次重跑没有改变近似 challenger 的排序判断：`since_2020_01` 仍应只保留 `aggr_08_92_prom6__sat_three_stage_buffered` 作为最接近挑战者；`since_2023_01` 虽然 raw-CAGR 最高仍来自 `core_6_1` 线，但真正值得保留的 sidecar challenger 仍是 `aggr_10_90_fast_ramp_cash_off`，问题继续集中在 `Turnover 2.37` 过高。
- 因此下一轮 `Path 1` 继续严格限定在 `promotion_ramp / satellite_defense / weekly_exposure_path` 三个方向内，不补确认回测，也不把 `signal_variants` 拉回主攻列表。

## 12. 本轮补充（2026-04-22 23:27 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-22 base=20 total=140 eval=34`，四窗口赢家继续不变。
- `since_2020_01` 当前最接近挑战者仍是 `aggr_08_92_prom6__sat_three_stage_buffered`：`25.46% CAGR / 0.9253 Sharpe / -21.83% MaxDD / 0.66 Turn`；相对当前 tracked winner 只有很小收益优势，但 `MaxDD` 略差，仍不补确认回测。
- `since_2023_01` 真正值得保留的 sidecar challenger 仍是 `aggr_10_90_fast_ramp_cash_off`：`27.06% CAGR / 1.1488 Sharpe / -9.90% MaxDD / 2.37 Turn`；`core_6_1` 两条线虽然 raw CAGR 更高，但仍明显恶化 `Sharpe / MaxDD / Turnover`，不回到主攻列表。
- 下一轮继续只在 `promotion_ramp / satellite_defense / weekly_exposure_path` 三个方向内推进；`signal_variants` 继续只保留观察，不追加新 family，也不补 A 股 Path 1 确认回测。

## 13. 本轮补充（2026-04-23 01:32 CST）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：`as_of=2026-04-23 base=20 total=140 eval=140`；本轮首次在 `Path 1 fast-pass family` 内出现 3 个明确改写窗口赢家的候选。
- 当前 Path 1 tracked winners 已同步为：
  - `since_2017_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（`24.50% CAGR / 1.1638 Sharpe / -10.65% MaxDD / 0.62 Turn`）
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6__sat_three_stage_buffered`（`25.78% CAGR / 0.9271 Sharpe / -21.59% MaxDD / 0.67 Turn`，本轮不变）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off__port_weekly_exposure_buffered`（`26.91% CAGR / 1.1251 Sharpe / -12.55% MaxDD / 0.57 Turn`）
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_6_1__port_weekly_exposure_asym`（`103.32% CAGR / 2.3086 Sharpe / -9.54% MaxDD / 1.39 Turn`）
- 本轮同时修正了 `scripts/update_weighted_winners.py` 的 Path 1 口径：`tracked winner` 同步现在会纳入 `weekly_exposure_path` 允许的 `__port_weekly_exposure / __port_weekly_exposure_buffered / __port_weekly_exposure_asym` 三个 companion，但仍只限于 `PATH1_FAST_PASS_VARIANT_IDS`，避免把 Path 2 的高集中原型误并入 Path 1。
- 本轮没有再补额外确认回测：因为上述 3 个晋级候选在当前 `results/strategy_comparison_base_method.csv` 中已经具备完整四窗口结果；需要补的不是回测本身，而是把 README / HISTORY / tracked winner 数据与对比图同步到正确口径。
- 当前四窗口鲁棒候选更新为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（`meanCAGR 47.55% / minCAGR 27.01%`）。下一轮 `Path 1` 继续只围绕两个已证实有效的周度仓位 companion 推进：
  - `aggr_08_92_prom6_cash_off + __port_weekly_exposure_buffered`
  - `aggr_08_92_prom6_core_6_1 + __port_weekly_exposure_asym`
  不重新打开非 fast-pass family。

## 14. 本轮补充（2026-04-23 03:33 CST）

- 本轮先补齐了 `Path 2` 计划里已声明但未实际生成的 4 个候选变体，并用离线缓存补跑后重建了 `results/strategy_comparison_base_method.csv`（`1744` 行 / `466` 个 base strategies）；随后再次运行 `./.venv/bin/python scripts/winner_only_pass.py`，输出仍为 `as_of=2026-04-23 base=20 total=140 eval=140`，四窗口 tracked winners 继续不变。
- `since_2020_01` 当前最接近过线的仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure_buffered`：`27.59% CAGR / 0.9338 Sharpe / -23.01% MaxDD / 0.87 Turn`。它相对当前 winner 确实提高了 `CAGR / Sharpe`，但 `MaxDD` 与 `Turnover` 都明显超出 `clear improvement` 阈值，因此本轮继续不补确认回测。
- `since_2023_01` 最接近挑战者仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`：`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`；问题仍然不是收益不够，而是回撤和风险调整后收益明显差于当前 tracked winner。
- 结论不变：`Path 1` 下一轮继续只保留 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path` 里的快筛观察，不新增确认回测，也不把 `signal_variants` 拉回主攻列表。

## 15. 本轮补充（2026-04-23 05:29 CST）

- 再次运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-23 family=path1_fast_family base_candidates=20 total_candidates=140 evaluated=140`，四窗口 tracked winners 与 `robust_candidate` 继续完全不变。
- `since_2020_01` 当前最接近阈值的仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure_buffered`（`27.59% CAGR / 0.9338 Sharpe / -23.01% MaxDD / 0.87 Turn`）；`since_2023_01` 最接近挑战者仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）。两者都仍卡在 `MaxDD / Turnover` 约束，不补确认回测。
- 本轮随后执行 `./.venv/bin/python scripts/update_weighted_winners.py` 与 `./.venv/bin/python scripts/generate_strategy_comparison_chart.py`：`README / HISTORY / results/weighted_track_winners.json` 没有新增漂移，但 A 股对比图与 tracked-winner 汇总图按当前基线重绘后发生了实际 binary diff，因此本轮允许作为 `sync-only` artifact refresh 提交。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path` 四个既定方向内推进，不新增 fast-pass family，也不重新打开 `signal_variants`。

## 16. 本轮补充（2026-04-23 17:57 CST）

- 再次运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出仍为 `as_of=2026-04-23 family=path1_fast_family base_candidates=20 total_candidates=140 evaluated=140`，四窗口 tracked winners 与 `robust_candidate` 继续完全不变，没有新的 `clear improvement`。
- `since_2020_01` 最接近阈值的仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure_buffered`（`27.59% CAGR / 0.9338 Sharpe / -23.01% MaxDD / 0.87 Turn`）；`since_2023_01` 最接近挑战者仍是 `core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）。两者都仍卡在 `MaxDD / Turnover` 约束，因此本轮继续不补确认回测。
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py` 与 `./.venv/bin/python scripts/generate_strategy_comparison_chart.py`：A 股 tracked winner ID 本身没有变化，但 `README / HISTORY / results/weighted_track_winners.json` 与对比图已按 `2026-04-23` 最新 close 刷新到当前口径，因此本轮继续允许作为 `sync-only` artifact refresh 提交。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path` 四个既定方向内推进，不新增 fast-pass family，也不重新打开 `signal_variants`。

## 17. 本轮补充（2026-04-24）

- 按自动化规则先把独立 worktree 对齐到主工作树 `main`，随后以 continuity 基线重建 `results/weighted_track_winners.json` 并运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-24 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`。
- 本轮 `Path 1 fast pass` 已正式纳入 `aggr_10_90_fast_ramp_cash_off_and`、`aggr_08_92_hold_3_6`、`aggr_08_92_hold_3_6_ramp90`、`aggr_05_95_prom7`，固定五方向的 base budget 提升到 `24`；但在保留既有 tracked-winner continuity 口径后，四窗口 tracked winners 与 `robust_candidate` 继续保持不变。
- 当前最强但未过 `clear improvement` 阈值的挑战者是：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`28.30% CAGR / 1.0296 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` 具备更高 raw CAGR，但分别因为 `Sharpe / MaxDD` 不过线而不晋级。
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py`、`./.venv/bin/python scripts/generate_strategy_comparison_chart.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：`README / HISTORY / results/weighted_track_winners.json / results/live` 已同步到 `2026-04-24` 口径，但结论仍是“扩容后没有新的 clear winner”。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 这五个既定方向内推进；`signal_variants` 仍只保留观察，不补确认回测。

## 18. 本轮补充（2026-04-25）

- 本轮先按自动化规则把独立 worktree 对齐到主工作树 `main`，随后用缓存重建 `results/strategy_comparison_base_method.csv`（`1899` 行 / `491` 个 base strategies）；重建后的 A 股真实 `sample_end` 已恢复到 `2026-04-24`，`README / HISTORY / results/weighted_track_winners.json` 也已同步到同一口径。
- 本轮没有新增 `Path 1` winner，但在尝试扩扫 A 股 active family 时踩出了一个真实的 Path 2 边缘 bug：极端高集中候选在周频 overlay 调仓里会把 `NaN` code 混进持仓序列，进而在 `compute_rebalance_trades()` 的持仓聚合处触发崩溃。当前已在 `backtest_marketcap_etf.py` 中加上“丢弃空索引 + 合并重复 code”的最小修复，后续 `Path 1 / Path 2` 的激进候选都可以继续跑，不会因为脏索引中断。
- 在这份重建后的完整 comparison CSV 上再次运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-24 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`；四窗口 tracked winners 与 `robust_candidate` 继续完全不变，没有新的 `clear improvement`。
- 当前仍最值得观察但未过阈值的挑战者没有变化：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_ramp90__port_weekly_exposure_buffered` 仍具更高 raw CAGR，但继续因为 `Sharpe / MaxDD` 不过线而不晋级。
- 本轮允许作为 `sync-only` 提交的原因，不是出现了新 winner，而是：
  - A 股 comparison CSV 已从旧的局部口径恢复到完整口径；
  - `README / HISTORY / results/weighted_track_winners.json / results/live` 已按真实 `sample_end=2026-04-24` 重新同步；
  - `Path 2` 高集中候选会炸的持仓索引问题已在回测内核修掉。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍固定优先 `buffered > asym > base`，`signal_variants` 不重新打开。

## 19. 本轮补充（2026-04-26）

- 本轮先按自动化规则重新检查基线：`git fetch origin` 因沙箱网络限制失败，而当前 worktree 已知 `origin/main` 不是主工作树 `main` 的后继，因此改为以本地主工作树 `main`（`bb3a7d7`）作为基线，并在独立 worktree 中对齐到该提交。
- 随后运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-26 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`，四窗口 tracked winners 与 `robust_candidate` 继续完全不变，没有新的 `clear improvement`。
- 当前仍最接近阈值、但没有晋级确认回测资格的挑战者是：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` 仍具更高 raw CAGR，但继续因为 `Sharpe / MaxDD` 不过线而不晋级。
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py`、`./.venv/bin/python scripts/generate_strategy_comparison_chart.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：A 股 tracked winners、README 自动区块、对比图和 `results/live` 已同步到当前 `as_of=2026-04-26` 口径，但结论仍是“没有新的 Path 1 winner”。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍固定优先 `buffered > asym > base`，`signal_variants` 继续只保留观察。

## 20. 本轮补充（2026-04-27）

- 本轮按自动化基线规则重新检查后，`git -C /Users/valselee/my-code/aiinvestor fetch origin main` 实际成功；最新 `origin/main` 位于 `fd4b214`，领先于本地主工作树 `main`（`39cf735`），因此本轮直接以该最新远端提交作为 publish baseline，并在独立 worktree 上按该基线重放研究。
- 随后运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-24 family=path1_fast_family base_candidates=24 total_candidates=168`，四窗口 tracked winners 与 `robust_candidate` 继续完全不变，没有新的 `clear improvement`。
- 当前最接近阈值但仍不补确认回测的挑战者是：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` 仍具更高 raw CAGR，但继续因为 `Sharpe / MaxDD` 不过线而不晋级。
- 为了恢复 `results/live` 的依赖，这轮只额外补跑了 tracked winners 与导出所需 sidecar summaries；因为没有任何候选达到 `clear improvement`，所以没有追加新的 `Path 1` 确认回测。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍固定优先 `buffered > asym > base`，并继续优先比较 `buffered` 与 `asym` 两条现役分支。

## 21. 本轮补充（2026-04-27 09:08 CST）

- 本轮按自动化基线规则重新检查后，`git fetch origin` 因沙箱网络限制失败；但当前 worktree 已知 `origin/main`（`5a87b29`）已验证是本地主工作树 `main`（`39cf735`）的后继，因此本轮直接以已知 `origin/main` 作为 publish baseline，并在独立 worktree 中对齐到该提交。
- 随后运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-27 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`，四窗口 tracked winners 继续完全不变，仍未出现满足阈值的 `clear improvement`。
- 当前最接近阈值、但仍不补确认回测的挑战者依旧集中在既定五方向内：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`）
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`）
  - `since_2017_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered` 仍具更高 raw CAGR，但继续因为 `Sharpe / MaxDD` 不过线而不晋级。
- 这轮真正发生漂移的是 tracked payload 而不是 fast pass 胜负：`results/weighted_track_winners.json` 的 `robust_candidate` 现已同步为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6__port_weekly_exposure_buffered`（`meanCAGR 47.28% / minCAGR 25.91%`），替代了此前文档里残留的 `ramp90` 口径；因此本轮属于有效的 `sync-only` 刷新。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍固定优先 `buffered > asym > base`，不重新打开 `signal_variants`。

## 22. 本轮补充（2026-04-27 18:09 CST）

- 本轮在主工作树 `main` 上重新检查基线：工作树起始干净，`git fetch origin` 因 SSH 网络限制失败，因此按自动化规则继续基于本地 `main`（`40d124d`）运行；本轮没有触碰策略代码。
- 运行 `./.venv/bin/python scripts/winner_only_pass.py`：输出为 `as_of=2026-04-27 family=path1_fast_family base_candidates=24 total_candidates=168 evaluated=168`，固定五方向候选预算维持在 `24` 个 base candidates。
- 四窗口 tracked winners 继续没有 clear improvement。当前最接近但未过阈值的候选是：
  - `since_2020_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7__sat_three_stage_buffered`（`27.83% CAGR / 1.0264 Sharpe / -25.00% MaxDD / 0.67 Turn`），收益与 Sharpe 更好，但回撤从当前 winner 的 `-21.59%` 加深到 `-25.00%`，不补确认回测。
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_10_90_hold_4_6__port_weekly_exposure`（`30.93% CAGR / 0.8987 Sharpe / -31.82% MaxDD / 0.98 Turn`），仍是收益更高但回撤/风险调整收益明显不合格。
  - `since_2017_01 / since_2025_01`：`aggr_08_92_prom6_ramp90__port_weekly_exposure_buffered` 系列具备更高 raw CAGR，但继续因为 Sharpe 或 MaxDD 不过线而不晋级。
- 下一轮 `Path 1` 继续只在 `promotion_ramp / satellite_defense / holding_shape / weekly_exposure_path / supporting_variants` 五个既定方向内推进；`weekly_exposure_path` 仍优先比较 `buffered` 与 `asym`，不重新打开额外信号族。
