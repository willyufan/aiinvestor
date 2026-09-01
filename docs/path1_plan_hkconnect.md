# 沪港通 Path 1 研究计划

## 2026-09-02 迭代：cost-exit36 中窗改善被换手与年内转负抵消（端点 2026-09-01）

### 上一轮候选与结果摘要

- 上轮 soft-exit38 因 turnover 增约3.5x且2026转负而 `reject`；正式 winner/robust/tracked 未变。

### 本轮候选 ID 与命令

- 命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-01 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36`。
- 相对 biweekly-lowvol，2020/2023 CAGR提高 `0.19/4.83pp`，但 turnover 增 `3.52/3.45x`，2026 CAGR从 `11.52%` 降至 `-2.37%`，二次成本/绝对收益判断为 `reject`；无 winner/robust/tracked 变化及 evict/archive。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 soft-exit 同形，回到 hybrid/cashoff 的低换手边界；第一条命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-09-01 --allow-hk-akshare-fallback --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：hybrid、cashoff；`biweekly_buffer`：hybrid、lowvol；`risk_overlay_cost`：cashoff、lowvol；`drawdown_repair`：lowvol、hybrid。

## 2026-09-01 迭代：soft-exit38 的中窗弹性被成本与年内失效抵消（端点 2026-08-31）

### 上一轮候选与结果摘要

- `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38` 相对 lowvol 的2020/2023 CAGR提高 `1.29/6.67pp`，但 turnover增加 `3.53/3.47x`、2026 CAGR从 `10.91%`降至 `-1.28%`，判 `reject`。假设“soft-exit38可改善中窗且维持成本/年内收益”不获支持；正式 winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 转验 cost-guard-exit36 与 lowvol；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：soft-cost-exit36、biweekly-lowvol；`biweekly_buffer`：hybrid、cashoff；`risk_overlay_cost`：soft-cost-exit36、cashoff；`drawdown_repair`：lowvol、hybrid。

## 2026-08-31 迭代：hybrid 保持五窗正收益但未优于 lowvol（端点 2026-08-28）

### 上一轮候选与结果摘要

- `hkconnect_path1_biweekly_hybrid` 五窗口保持正收益；相对 lowvol 的2020/2023 CAGR仅低 `0.05/1.29pp`且回撤接近，但 turnover 高约 `0.99/1.10x`，判 `keep_watch`。假设“hybrid 可在低波锚附近改善风险成本前沿”只获稳定性支持，未形成关键指标优势；正式 winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- 确认 ID：`hkconnect_path1_biweekly_hybrid`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid`。

### 下一轮 focus 提示

- `biweekly_buffer`：用 cashoff 与 hybrid/lowvol 同窗比较是否能进一步降 turnover 且守住中窗；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `biweekly_buffer`：hybrid、cashoff；`monthly_weekly_overlay`：lowvol-soft-exit36、lowvol-soft-exit38；`risk_overlay_cost`：hybrid、cashoff；`drawdown_repair`：lowvol、hybrid。

## 2026-08-30 迭代：双周 hybrid 的正收益与成本权衡（端点 2026-08-28）

### 上一轮候选与结果摘要

- `hkconnect_path1_biweekly_hybrid` 相对 `hkconnect_path1_biweekly_lowvol` 的 2020 CAGR `-0.05pp`、MaxDD 恶化 `2.90pp`、turnover 增加约 `0.99x`；五窗口均为正，2026 CAGR `9.75%`，判 `keep_watch`。
- 假设“hybrid 可在保持双周正收益时提升弹性且不显著增加成本”仅获收益稳定性支持，成本/回撤不支持；正式 window winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- 确认 ID：`hkconnect_path1_biweekly_hybrid`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid`。

### 下一轮 focus 提示

- `biweekly_buffer`：用 cashoff 与 lowvol 夹住 hybrid，要求 2020/2023 不低于 lowvol 3pp 且 turnover 不高于 hybrid。第一条命令：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `biweekly_buffer`：`hkconnect_path1_biweekly_hybrid`、`hkconnect_path1_biweekly_cashoff`。
- `monthly_weekly_risk`：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`、`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36`。
- `drawdown_repair`：`hkconnect_path1_biweekly_lowvol`、`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36`。

## 2026-08-29 迭代：月频周风控 soft-exit 的回撤护栏再否定（端点 2026-08-28）

### 上一轮候选与结果摘要

- `soft_exit36/38` 相对 lowvol 的2020 CAGR均提高约 `8.0pp`、2023提高约 `7.95pp`，但2023 MaxDD恶化 `5.22pp`且2026 CAGR均为 `-5.85%`，命中护栏并 `reject`。lowvol 五窗确认 `promote` incumbent，2026 CAGR `9.77%`。
- 假设“soft-exit 可用中窗收益改善换取可控回撤且保持年内正收益”不获支持；正式 winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `biweekly_buffer` 停止 soft-exit 同形，回到 hybrid/cashoff 与 lowvol 的成本边界；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `biweekly_buffer`：hybrid、cashoff；`monthly_weekly_overlay`：lowvol-soft-exit36、lowvol-soft-exit38；`risk_overlay_cost`：hybrid、cashoff；`ytd_guard`：v26-positive-guard、v49-ytd-repair。

## 2026-08-28 迭代：hybrid/cashoff 与 lowvol 成本边界（端点 2026-08-27）

### 上一轮候选与结果摘要

- `biweekly_hybrid` 五窗均为正且未触发护栏，但中窗与 lowvol 略弱，`keep_watch`；`biweekly_cashoff` 的2023 CAGR下降 `4.74pp`，触发护栏并 `reject`。lowvol同窗确认 `promote` incumbent，2026 CAGR `9.29%`。
- 假设“hybrid/cashoff 可在低波锚附近改善成本”仅获 hybrid 的局部支持；正式 winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_hybrid`、`hkconnect_path1_biweekly_cashoff`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `biweekly_buffer` 已确认 hybrid 更接近前沿，下一轮转验月频选股+周风控 lowvol soft-exit；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `biweekly_buffer`：hybrid、lowvol；`monthly_weekly_overlay`：lowvol-soft-exit36、lowvol-soft-exit38；`risk_overlay_cost`：hybrid、cashoff；`ytd_guard`：v26-positive-guard、v49-ytd-repair。

## 2026-08-27 迭代：双周 buffer 年内守门失败（端点 2026-08-26）

### 上一轮候选与结果摘要

- `v43_buffer_repair` 与 `v49_ytd_repair` 的 2026 CAGR虽为 `2.06%/0.07%`，但相对 lowvol 的 2023 CAGR分别下降 `6.25/6.89pp`、Sharpe下降 `0.304/0.319`，均触发护栏并 `reject`。
- lowvol 五窗口确认 `promote` incumbent，2026 CAGR `10.07%`；假设“双周 buffer 能降低换手并守住年内正收益”不获支持。正式 winner/robust/tracked 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `biweekly_buffer` 停止 v43/v49 同形，回到 hybrid/cashoff 与 lowvol 的成本边界；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `biweekly_buffer`：hybrid、cashoff；`monthly_weekly_overlay`：lowvol-soft-exit36、lowvol-soft-exit38；`risk_overlay_cost`：cashoff、hybrid；`ytd_guard`：v26-positive-guard、v49-ytd-repair。

## 2026-08-26 迭代：双周 hybrid/cashoff 与 lowvol 锚竞争（端点 2026-08-25）

### 上一轮候选与结果摘要

- `biweekly_hybrid` 相对 `biweekly_lowvol` 的2020/2023 CAGR仅下降 `0.06/1.32pp`，回撤近似且2026 CAGR `9.98%`，但换手提高约 `0.99/1.11x`，判 `keep_watch`。`biweekly_cashoff` 的2023 CAGR下降 `4.73pp`并触发护栏，判 `reject`。
- `biweekly_lowvol` 五窗确认 `promote` incumbent，2020/2023/2026 CAGR为 `17.73/23.11/10.13%`。假设“hybrid/cashoff 可在不破坏中窗下改善年内防守”仅对 hybrid 部分成立；正式 robust/tracked 未变，无 evict/archive。完整卡见 `results/research/a_share/research_iteration_scorecard_20260826.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_hybrid`、`hkconnect_path1_biweekly_cashoff`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 保留 hybrid 观察结论，转验 v43/v49 的双周缓冲能否降低换手并守住2026正收益；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：v43-buffer、v49-ytd；`biweekly_buffer`：v43、v49；`risk_overlay_cost`：hybrid、cashoff；`ytd_guard`：v26、v49。

## 2026-08-25 迭代：月频周风控 cost/cash guard 再否定（端点 2026-08-24）

### 上一轮候选与结果摘要

- `lowvol-soft-cost-exit32` 虽令2020/2023 CAGR提高 `6.51/6.32pp`，但2023 MaxDD恶化 `5.22pp`且2026 CAGR `-4.85%`；`soft-cashguard-exit34-v2` 的2023 MaxDD恶化 `9.62pp`且2026 CAGR `-14.85%`，两者均触发护栏并 `reject`。假设“cost/cash guard可修复年内收益且不损伤中窗回撤”不获支持。
- `biweekly_lowvol` 五窗确认 `promote` incumbent，2020/2023/2026 CAGR为 `17.73/23.11/10.07%`；正式 winner/robust/tracked 未变，无 evict/archive。完整卡见 `results/research/a_share/research_iteration_scorecard_20260825.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v2`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v2,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 soft-exit 同形，回到双周 hybrid/cashoff 与 lowvol 锚比较；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：biweekly-hybrid、biweekly-cashoff；`biweekly_buffer`：v43、biweekly-lowvol；`risk_overlay_cost`：hybrid、cashoff；`ytd_guard`：v26、v49。

## 2026-08-24 迭代：月频周风控 soft-exit 收益回撤冲突确认（端点 2026-08-21）

### 上一轮候选与结果摘要

- `lowvol-soft42` 与 `soft34` 相对 robust `biweekly_lowvol` 的 2020/2023 CAGR均改善，但 2023 MaxDD分别恶化 `5.22/9.62pp`，且 2026 CAGR为 `-3.11/-13.70%`，均 `reject`。假设“放宽soft-exit可恢复中窗收益且守住年内风险”不获支持。
- `biweekly_lowvol` 五窗确认 `promote` incumbent；正式 window winner/robust/tracked 未改变，无 evict/archive。完整卡见 `results/research/a_share/research_iteration_scorecard_20260824.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止裸 soft-exit，转向 cost/cash guard；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v2,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-cost-exit32、cashguard-exit34-v2；`biweekly_buffer`：v43、biweekly-lowvol；`risk_overlay_cost`：hybrid、cashoff；`ytd_guard`：v26、v49。

## 2026-08-23 迭代：双周 buffer 修复确认（端点 2026-08-21）

### 上一轮候选与结果摘要

- `v43/v49` 相对 robust `biweekly_lowvol` 的 2023 CAGR分别下降 `6.00/6.64pp`、Sharpe下降 `0.304/0.319`，均触发稳定性护栏并 `reject`；`biweekly_lowvol` 五窗确认 `promote` incumbent。
- 正式 window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 v43/v49 同形，回到 soft42/soft34 与 lowvol 锚；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft42、soft34；`biweekly_buffer`：v43、lowvol；`risk_overlay_cost`：hybrid、cashoff；`ytd_guard`：v26、v49。

## 2026-08-22 迭代：lowvol soft-exit 短窗失效确认（端点 2026-08-21）

### 上一轮候选与结果摘要

- `lowvol_soft_exit36/38` 相对当前 robust `biweekly_lowvol` 将 2020/2023 CAGR提高约 `8.3/8.4pp`，但 2023 MaxDD恶化约 `5.22pp`，触发稳定性护栏，且 2026 CAGR均为 `-3.11%`，判 `reject`。
- `biweekly_hybrid` 的 2020/2023 CAGR为 `17.78/22.05%`、2026为 `11.73%`，但换手高于 lowvol、未形成新前沿，判 `keep_watch`。artifact robust 为 `biweekly_lowvol`，window winner/tracked 未因本轮候选切换，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`、`hkconnect_path1_biweekly_hybrid`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_hybrid`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 lowvol soft36/38 同形扩参，回到双周 buffer 与年内守门；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft42、soft34；`biweekly_buffer`：v43、lowvol；`risk_overlay_cost`：hybrid、cashoff；`ytd_guard`：v26、v49。

## 2026-08-21 迭代：双周 risk-overlay 结构确认（端点 2026-08-20）

### 上一轮候选与结果摘要

- 当前 robust `biweekly_hybrid` 五窗同窗确认 `promote`，2020/2023/2026 CAGR为 `17.66/21.78/9.68%`。`biweekly_cashoff` 的 2023 CAGR下降 `3.42pp`，触发稳定性护栏并 `reject`；`biweekly_lowvol` 中窗略强、2026 CAGR `9.50%` 且 turnover更低，但未形成相对 hybrid 的清晰新前沿，`keep_watch`。
- 假设“cashoff/lowvol 可在保持中窗下改善短窗风险”仅获 lowvol 部分支持；artifact 与运行前 `HEAD` 一致，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_cashoff`、`hkconnect_path1_biweekly_hybrid`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 回到低波 soft-exit 边界，并以 hybrid 为同窗锚；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_hybrid`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft36、lowvol-soft38；`biweekly_buffer`：hybrid、lowvol；`risk_overlay_cost`：cashoff、hybrid；`ytd_guard`：v26、v49。

## 2026-08-20 迭代：低波周风控与年内守门确认（端点 2026-08-19）

### 上一轮候选与结果摘要

- `lowvol_soft_exit42` 的 2023 MaxDD 触发护栏且 2026 CAGR 为 `-6.88%`，判 `reject`；`v26_ytd_positive_guard` 在 2020/2023/2025 收益改善但 2026 CAGR 仍为 `-3.12%`、turnover 增加约 `2.79x`，判 `keep_watch`。`biweekly_lowvol` 五窗确认 `promote` incumbent，2026 CAGR `8.33%`。实验假设“lowvol overlay / ytd guard 可在不损伤中窗下修复年内收益”仅获 v26 的中窗支持。正式 window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- 转向 `risk_overlay_cost`，要求风险覆盖至少保持 2026 正收益且 turnover 不高于低波锚；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft42、v26-ytd；`biweekly_buffer`：hybrid、lowvol；`risk_overlay_cost`：cashoff、lowvol；`ytd_guard`：v26、v49。

## 2026-08-19 迭代：月频周风控短窗淘汰（端点 2026-08-18）

### 上一轮候选与结果摘要

- `soft_exit32/34` 相对 `biweekly_lowvol` 虽令 2020/2023 CAGR提高约 `8.45/3.80pp`，但 2023 MaxDD恶化约 `9.61pp`，2026 CAGR均为 `-17.05%`，判 `reject`；早退出没有修复短窗。`biweekly_lowvol` 五窗确认 `promote` incumbent，2026 CAGR `7.74%`、MaxDD `-11.28%`、turnover `3.18x`。正式 window winner/robust/tracked 与 `HEAD` 相同，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止非低波 soft-exit 同形扩参，转查 lowvol overlay 与 v26 ytd guard；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft42、v26-ytd；`biweekly_buffer`：hybrid、lowvol；`risk_overlay_cost`：cashoff、lowvol；`ytd_guard`：v26、v49。

## 2026-08-18 迭代：月频周风控队列保留（端点 2026-08-18）

### 上一轮候选与结果摘要

- 上一轮 `lowvol_soft_exit32/34` 因 2023 MaxDD恶化 `5.22pp` 且 2026 为负而 `reject`，`biweekly_lowvol` 维持五窗 `promote` incumbent。本轮因 23:07 启动、需先完成 Path2/4/5 的新增竞争及全 tracked 同端点同步，Path1 未实跑新增 ID；非 coverage blocking。全 tracked 刷新后 `since_2025_01` window winner 由 `v43_biweekly_buffer_repair` 更新为 `v26_ytd_positive_guard`，robust 仍为 `biweekly_lowvol`；这是端点同步变化，不是新增候选晋级。无 evict/archive。

### 本轮候选 ID 与命令

- 本轮未实跑新增 ID；下一批保留非低波 `soft_exit32/34` 与 `biweekly_lowvol` 锚。未跑原因是日更窗口压缩。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 要求早退出变体先让 2026 转正，再评估其中窗收益；若仍为负，停止该 overlay 同形扩参。

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit32、soft-exit34；`biweekly_buffer`：hybrid、lowvol；`risk_overlay_cost`：cashoff、lowvol；`ytd_guard`：v49、lowvol。

## 2026-08-16 迭代：月频周风控早退出确认（端点 2026-08-14）

### 上一轮候选与结果摘要

- `lowvol_soft_exit32/34` 相对 robust `biweekly_lowvol` 将 2020/2023 CAGR改善约 `8.5/8.4pp`，但 2023 MaxDD恶化 `5.22pp`、2026 CAGR均为 `-8.78%`，触发稳定性护栏，均 `reject`。`biweekly_lowvol` 五窗全正且同窗 `promote` incumbent；正式 window winner/robust/tracked 均未改变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-14 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 的低波 exit32-38 已收敛，下一轮改验非低波早退出能否守住 2026；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit32、soft-exit34；`biweekly_buffer`：hybrid、lowvol；`risk_overlay_cost`：cashoff、lowvol；`ytd_guard`：v49、lowvol。

## 2026-08-15 迭代：月频周风控低波边界确认（端点 2026-08-14）

### 上一轮候选与结果摘要

- `lowvol_soft_exit36` / `exit38` 相对 robust `biweekly_lowvol` 的 2020/2023 CAGR 改善约 `8.3/8.6pp`、Sharpe 同步改善，但 2023 MaxDD均恶化 `5.22pp` 且 2026 CAGR均为 `-8.78%`，触发稳定性护栏，均 `reject`。假设“月频周风控可在低波锚上同时改善中窗与短窗”不成立。
- `biweekly_lowvol` 以 2020/2023/2026 CAGR `17.25%/22.24%/4.94%` 同窗确认 `promote` incumbent；正式 window winner/robust/tracked 均未改变，无 evict/archive。scorecard：`results/research/a_share/research_iteration_scorecard_20260815.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-14 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 exit36/38 同形扩参，回查较早退出是否能保住 2026 正收益；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit32、exit34；`biweekly_buffer`：hybrid、lowvol；`risk_overlay_cost`：cashoff、lowvol；`ytd_guard`：v49、lowvol。

## 2026-08-14 迭代：双周低波权重边界确认（端点 2026-08-13）

### 上一轮候选与结果摘要

- hybrid 相对 lowvol 在 2020/2023 CAGR 下降 `0.13/1.40pp`，2026 仅下降 `0.62pp`，未触发中窗硬护栏，判定 `keep_watch`；cashoff 的 2023 CAGR 下降 `4.84pp`，`reject`。低波 incumbent 五窗为正、turnover 最低，同窗 `promote`。
- 假设“混合权重可接近低波同时保留弹性”只获弱支持；正式 winner/robust/tracked 未改变，无 evict/archive。scorecard：`results/research/a_share/research_iteration_scorecard_20260814.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_cashoff`、`hkconnect_path1_biweekly_hybrid`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-13 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 转回低波月频周风控与低波锚。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit36、exit38；`biweekly_buffer`：hybrid、lowvol；`risk_overlay_cost`：cashoff、lowvol；`ytd_guard`：v49、lowvol。

## 2026-08-13 二次迭代：双周缓冲与低波确认（端点 2026-08-12）

### 上一轮候选与结果摘要

- v49 在 2025 CAGR 提高 `5.72pp`，但 2023 CAGR 下降 `6.57pp`、2026 转为 `-3.26%`，`reject`；v34 的 2023 CAGR/MaxDD 下降 `4.27pp/3.78pp` 且 2026 为 `-12.27%`，`reject`。假设“质量动量缓冲可替换低波锚”不成立。
- `hkconnect_path1_biweekly_lowvol` 以 2020/2023/2026 CAGR `17.31%/22.35%/5.39%` 同窗确认 `promote` incumbent。正式 winner/robust/tracked 未改变，无 evict/archive；scorecard：`results/research/a_share/research_iteration_scorecard_20260813_iter2.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v34_lowvol_ytd_repair`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v34_lowvol_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 v34/v49，下一轮只确认 cashoff 与低波锚的成本边界；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_cashoff,hkconnect_path1_biweekly_hybrid,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：biweekly-hybrid、biweekly-lowvol；`biweekly_buffer`：biweekly-cashoff、biweekly-lowvol；`risk_overlay_cost`：v46、biweekly-lowvol；`cashoff_confirmation`：biweekly-cashoff、biweekly-lowvol。

## 2026-08-13 迭代：月频周风控与双周缓冲确认（端点 2026-08-12）

### 上一轮候选与结果摘要

- v49 的 2020/2023 CAGR 相对双周低波下降 `2.59pp/6.57pp`，2026 CAGR `-3.26%`，且 turnover 增加约 `1.7–2.2x`，`reject`。lowvol-soft-exit36 虽提高 2020/2023 CAGR `8.32pp/8.48pp`，但 2023 MaxDD 恶化 `5.22pp`、2026 CAGR `-9.04%`，`reject`。
- `hkconnect_path1_biweekly_lowvol` 以 2020/2023/2026 CAGR `17.31%/22.35%/5.39%` 同窗确认 `promote` incumbent。正式 winner/robust/tracked 未变，无 evict/archive；scorecard：`results/research/a_share/research_iteration_scorecard_20260813.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 lowvol-soft-exit 梯度，回到 soft-exit36 与非 lowvol soft-exit36 的结构差异确认。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit36、lowvol-soft-exit36；`biweekly_buffer`：v49、biweekly-lowvol；`risk_overlay_cost`：v46、biweekly-lowvol；`cashoff_confirmation`：biweekly-cashoff、biweekly-lowvol。

## 2026-08-12 四次迭代：双周缓冲与月频周风控终端确认（端点 2026-08-11）

### 上一轮候选与结果摘要

- 五窗口实跑 v49、lowvol-soft-exit36 与双周低波锚。v49 的 2020/2023/2025/2026 CAGR 为 `14.81%/15.96%/30.95%/-2.39%`，回撤较浅且 2025 较强，但相邻 2023 低于双周低波 `6.67pp`、2026 转负，`keep_watch`。soft-exit36 为 `25.77%/31.12%/22.44%/-7.86%`，未修复短窗，`keep_watch`。
- `hkconnect_path1_biweekly_lowvol` 以 `17.45%/22.63%/25.39%/6.78%` 同窗确认 `promote` incumbent；winner/robust/tracked 未变，无 evict/archive。scorecard：`results/research/a_share/research_iteration_scorecard_20260812_iter4.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- 本组未显著挑战双周低波，停止同形 soft-exit；下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v34_lowvol_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit36、biweekly-buffer-v49；`biweekly_buffer`：v49、biweekly-lowvol；`risk_overlay_cost`：v34、biweekly-lowvol；`cashoff_confirmation`：biweekly-cashoff、biweekly-lowvol。

## 2026-08-12 三次迭代：月频周风控中间带（端点 2026-08-11）

### 上一轮候选与结果摘要

- 本轮五窗确认 lowvol soft-exit34/38。两者 2020/2023 CAGR 分别为 `25.91%/30.99%`、`25.73%/31.10%`，但 2026 CAGR 均为 `-7.86%`，且 turnover 约 `3.2–3.9x`；相邻短窗没有超过双周低波锚，均 `keep_watch`，而不是因较远窗口直接 `reject`。
- `hkconnect_path1_biweekly_lowvol` 的 2020/2023/2026 CAGR 为 `17.45%/22.63%/6.78%`，MaxDD 为 `-16.78%/-11.30%/-11.28%`，同窗确认 `promote` incumbent。winner/robust/tracked 未变，无 evict/archive；scorecard：`results/research/a_share/research_iteration_scorecard_20260812_iter3.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 不再继续同一 soft-exit 梯度，改比较双周 buffer 与月频低波的触发速度；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit36、biweekly-buffer-v49；`biweekly_buffer`：v49、biweekly-lowvol；`risk_overlay_cost`：v46、biweekly-lowvol；`cashoff_confirmation`：biweekly-cashoff、biweekly-lowvol。

## 2026-08-12 二次迭代记录（端点 2026-08-11）

### 上一轮候选与结果摘要

- lowvol soft-exit32/42 的 2020/2023/2026 CAGR 分别为 `25.93%/30.96%/-7.86%`、`25.78%/31.32%/-7.86%`；虽显著提高中窗收益，但 2023 MaxDD 相对双周低波锚恶化 `5.22pp` 且 2026 转负，均 `reject`。
- `hkconnect_path1_biweekly_lowvol` 以 `17.45%/22.63%/6.78%` 同窗确认 `promote` incumbent。正式 winner/robust/tracked 未变，无 evict/archive；scorecard：`results/research/a_share/research_iteration_scorecard_20260812_iter2.json`。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42`、`hkconnect_path1_biweekly_lowvol`。原 plan 的 lowvol-soft-exit40 未由 active variant set 生成，以同族 soft-exit42 替代且只计实际完成 ID。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 soft-exit32/42 两端，回查 34/38 中间带，要求 2023 MaxDD 恶化小于 5pp 且 2026 转正。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay` / `biweekly_buffer`：lowvol-soft-exit34、lowvol-soft-exit38；`risk_overlay_cost`：biweekly-lowvol、soft-exit34；`cashoff_confirmation`：biweekly-cashoff、biweekly-lowvol。

## 2026-08-12 迭代记录（端点 2026-08-11）

### 上一轮候选与结果摘要

- lowvol-soft-exit36/38 的 2020/2023 CAGR 提高到约 `25.7%/31.1%`，但 2023 MaxDD 相对双周低波锚恶化超过 5pp，且 2026 CAGR 均为 `-7.86%`，两者均 `reject`；高收益未通过回撤和短窗稳定性验证。
- `hkconnect_path1_biweekly_lowvol` 以 2020/2023/2026 CAGR `17.45%/22.63%/6.78%`、五窗平均 turnover `2.17x` 同窗确认 `promote` incumbent。正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 soft-exit36/38 同形扩参，回查 soft-exit32/40 两侧并保留低波锚；要求 2026 转正且 MaxDD 不再破坏阈值。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit40,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit32、lowvol-soft-exit40；`biweekly_buffer`：v43-buffer、biweekly-lowvol；`risk_overlay_cost`：v37、v46；`low_turnover_defense`：biweekly-lowvol、soft-exit32。

## 2026-08-11 二次迭代记录（约 07:38 CST）

### 上一轮候选与结果摘要

- v43 buffer-repair 的 2023 CAGR 相对 lowvol 下降 `5.99pp`，`reject`；lowvol-soft-exit34 的 2020/2023 CAGR 提高到 `26.03%/31.23%`，但 2023 MaxDD 恶化约 `5.20pp` 且 2026 CAGR `-6.90%`，按稳定性与短窗风险 `reject`。
- `hkconnect_path1_biweekly_lowvol` 以 2020/2023/2026 CAGR `17.57%/22.87%/8.06%`、五窗平均 turnover `2.17x` 同窗确认 `promote` incumbent；正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 soft-exit34 的短窗负收益形态，转向 soft-exit36/38 相邻参数并保留低波锚。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit36、lowvol-soft-exit38；`biweekly_buffer`：v43-buffer、biweekly-lowvol；`risk_overlay_cost`：v37、v46；`low_turnover_defense`：biweekly-lowvol、lowvol-soft-exit36。

## 2026-08-11 迭代记录

### 上一轮候选与结果摘要

- risk-overlay v37 的 2026 CAGR 为 `-12.03%`，且 2023 CAGR/MaxDD 触发护栏；v46 的 2023 CAGR/Sharpe 分别下降 `5.86pp/0.302`，两者均 `reject`。`hkconnect_path1_biweekly_lowvol` 以 2020/2023/2026 CAGR `17.57%/22.87%/8.06%`、平均 turnover `2.17x` 确认 `promote` incumbent；正式 ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_risk_overlay_cost_v37_2026_repair`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_risk_overlay_cost_v37_2026_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 v37/v46 同形扩参，回到双周 buffer 修复并保留低波锚。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：v43-buffer、soft-exit34；`biweekly_buffer`：v43-buffer、biweekly-lowvol；`risk_overlay_cost`：v37、v46；`low_turnover_defense`：biweekly-lowvol、soft-exit34。

## 2026-08-10 二次迭代记录（约 07:27 CST）

### 上一轮候选与结果摘要

- lowvol soft-exit36/34 的 2020/2023/2026 CAGR 为 `25.93%/31.43%/-8.60%`、`26.12%/31.41%/-8.60%`；两者均使 2023 MaxDD 恶化约 `5.22pp`，判定 `reject`。
- `hkconnect_path1_biweekly_lowvol` 为 `17.02%/21.88%/6.63%`、平均 turnover `2.08x`，确认 `promote` incumbent；winner / robust / tracked ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <上述3个ID>`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 soft-exit 同形扩参，转向 risk-overlay cost guard，要求 2026 转正且 2023 MaxDD 不再恶化。第一条命令：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_risk_overlay_cost_v37_2026_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：v37-overlay-cost、v45-monthly-weekly；`biweekly_buffer`：v43-buffer、v49-ytd；`risk_overlay_cost`：v37、v46；`low_turnover_defense`：biweekly-lowvol、v37-overlay。

## 2026-08-10 迭代记录

### 上一轮候选与结果摘要

- lowvol soft-exit38/soft-exit40 的 2020/2023/2026 CAGR 为 `25.90%/31.43%/-8.60%`、`25.65%/26.60%/-18.19%`；分别触发 2023 MaxDD `5.22pp/9.62pp` 恶化，均 `reject`，overlay 放宽退出的假设未成立。
- `hkconnect_path1_biweekly_lowvol` 为 `17.02%/21.88%/6.63%`、平均 turnover `2.08x`，确认 `promote` incumbent；winner / robust / tracked ID 未变，无 evict/archive。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <上述3个ID>`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 回到更早 soft-exit34/36，验证是否存在收益与回撤的可接受折中；第一条命令：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit34、soft-exit36；`biweekly_buffer`：v33-risk-overlay、v43-buffer-repair。
- `risk_overlay_cost`：soft-exit34-cashguard-light、v46-risk-overlay；`low_turnover_defense`：biweekly-lowvol、soft-exit36。

## 2026-08-09 二次迭代记录（约 08:00 CST）

### 上一轮候选与结果摘要

- 五窗口确认 monthly-weekly-overlay v31、biweekly buffered v33 与 lowvol incumbent。假设是 overlay/成本守门能修复 2026；v31/v33 的 2020/2023/2026 CAGR 为 `19.05%/19.95%/-18.62%`、`17.75%/18.65%/-8.62%`，触发中窗或风险护栏，均 `reject`。
- lowvol 为 `17.02%/21.88%/6.63%`、平均 turnover `2.08x`，确认 `promote` incumbent；winner / robust / tracked ID 未变，无 evict。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v31_ytd_repair`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v33_risk_overlay_cost_guard`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <上述3个ID>`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 停止 v31/v33 同形扩参，改验 lowvol-overlay 的 exit38/40，并继续以 lowvol 锚定。第一条命令：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：`...weekly_overlay_lowvol_soft_exit38`、`...weekly_overlay_soft_exit40`；`biweekly_buffer`：`...equal_buffered_v33_risk_overlay_cost_guard`、`...equal_buffered_v43_biweekly_buffer_repair`。
- `risk_overlay_cost`：`...v46_risk_overlay_cost_guard`、`...v33_risk_overlay_cost_guard`；`low_turnover_defense`：`hkconnect_path1_biweekly_lowvol`、`...weekly_overlay_lowvol_soft_exit38`。

## 2026-08-09 迭代记录

### 上一轮候选与结果摘要

- 五窗口确认 `...exit42`、`...cashguard_exit45`、`hkconnect_path1_lowvol_monthly_biweekly_smoke`；CAGR（2020/2023/2026）为 `25.87%/31.52%/-8.60%`、`21.93%/27.39%/-8.60%`、`17.02%/21.88%/6.63%`。
- 前两者因 2026 负收益及稳定性退化 `reject`；lowvol 候选以平均 turnover `2.08x` 通过确认，`promote`（确认资格，不改变 window winner / robust / tracked）。

### 本轮候选 ID 与命令

- IDs：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45`、`hkconnect_path1_biweekly_lowvol`。
- 命令：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <上述3个ID>`。

### 下一轮 focus 提示

- `monthly_weekly_overlay`：用更缓和的 buffered/cost guard 修复 2026；第一条命令：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v31_ytd_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v33_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：`hkconnect_path1_stable_monthly_totalmv_buffered_v31_ytd_repair`、`hkconnect_path1_stable_monthly_totalmv_buffered_v33_risk_overlay_cost_guard`。
- `low_turnover_defense`：`hkconnect_path1_lowvol_monthly_biweekly_smoke`、`hkconnect_path1_stable_monthly_totalmv_cashguard_exit45_reconfirm`。

## 2026-08-08 二次迭代记录（约 07:30 CST）

### 上一轮候选与结果摘要

- 本轮确认 monthly-weekly-overlay soft-exit36/38。假设是放宽退出能修复 2026 且保持中窗；实际 2020/2023 CAGR 约 `25.9%/31.4%`，但 2023 MaxDD 恶化 `5.22pp`、2026 均为 `-8.60%`，两条均 `reject`。
- biweekly-lowvol 为 `17.02%/21.88%/6.63%`，确认 `promote` incumbent；winner/robust/tracked 无变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol
```

### 下一轮 focus 提示

- 停止 soft36/38 同形扩参，下一轮验证 soft-exit42 与 cashguard-exit45，要求 2026 转正且不再触发中窗 MaxDD 护栏；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit42、soft-cashguard-exit45；`biweekly_buffer`：v31、v33；`risk_overlay_cost`：v40、v44；`turnover_control`：v51、v52。

## 2026-08-08 迭代记录（约 01:30 CST）

### 上一轮候选与结果摘要

- `monthly_weekly_overlay` 确认 lowvol-soft-exit32/34。假设是月频选股叠加周度退出能提高中窗收益而保持风险；实际 2020/2023 CAGR 达 `26.14%/31.38%`、`26.12%/31.41%`，但 2023 MaxDD 护栏触发且 2026 均为 `-8.60%`，判 `reject`。
- biweekly-lowvol 对照 2020/2023/2026 CAGR `17.02%/21.88%/6.63%`、平均 turnover `2.08x`，确认 `promote` incumbent；winner/robust/tracked 无变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol
```

### 下一轮 focus 提示

- 继续 `monthly_weekly_overlay`，改验 soft-exit36/38；目标是修复 2026，并避免 MaxDD 护栏。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit36、lowvol-soft-exit38；`biweekly_buffer`：v31、v33。
- `risk_overlay_cost`：v40、v44；`turnover_control`：v51、v52。

## 2026-08-07 二次迭代记录（约 07:24 CST）

### 上一轮候选与结果摘要

- `biweekly_buffer` 确认 v41/v42，并与 lowvol robust 同端点比较。两条挑战者 2020/2023/2026 CAGR 为 `15.03%/15.57%/-9.11%`、`14.95%/15.37%/-5.38%`，均触发 2023 CAGR/Sharpe 护栏，判 `reject`。
- `hkconnect_path1_biweekly_lowvol` 为 `17.05%/21.86%/7.27%`、五窗平均 turnover `2.10x`，确认 `promote` incumbent，不是挑战者替换；正式 winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

### 下一轮 focus 提示

- 最终 guard 仍指向 `biweekly_buffer`；v41/v42 同形停止，下一轮改验 active v31 buffer-repair 与 v33 cost-guard，并保留 lowvol robust；要求 2020/2023 缺口不超过 `3pp`、2026 非负且回撤不恶化。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v31_buffer_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v33_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit32、lowvol-soft-exit34；`biweekly_buffer`：v31、v33（v41/v42 本轮 reject）。
- `risk_overlay_cost`：v40、v44；`turnover_control`：v51、v52。

## 2026-08-07 迭代记录

### 上一轮候选与结果摘要

- 按 `monthly_weekly_overlay` 确认 lowvol-soft-exit36/38，并与 biweekly-lowvol robust 同窗比较。两条月选周控的 2020/2023 CAGR 均约 `25.9%/31.5%`，但 MaxDD 护栏触发且 2026 CAGR 均为 `-8.69%`，判 `reject`。
- `hkconnect_path1_biweekly_lowvol` 为 `17.05%/21.86%/7.27%`，五窗均正，确认 `promote` incumbent，不是挑战者替换；正式 robust/tracked 暂未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol
```

### 下一轮 focus 提示

- soft-exit36/38 同形停止；最终 guard 仍为 `monthly_weekly_overlay`，下一轮改验 lowvol-soft-exit32/34 并保留 lowvol robust。目标是 2026 转正且中窗 MaxDD 不恶化；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit32、lowvol-soft-exit34；`biweekly_buffer`：v41、v42。
- `risk_overlay_cost`：v40、v44；`turnover_control`：v51、v52。

## 2026-08-06 迭代记录

### 上一轮候选与结果摘要

- 按 `biweekly_buffer` 确认 v43/v49，并与 lowvol robust 同窗比较。v43/v49 的 2020/2023/2026 CAGR 为 `15.29%/16.14%/-0.48%`、`14.73%/15.81%/-2.26%`；两者 2023 CAGR/Sharpe 均触发稳定性护栏，判 `reject`。
- `hkconnect_path1_biweekly_lowvol` 为 `17.15%/22.06%/8.33%`，五窗均正、平均 turnover `2.10x`，确认 `promote`（incumbent 确认，不是挑战者替换）。v49 仅确认既有 since_2025 window winner；正式 robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol
```

### 下一轮 focus 提示

- 最终 guard 已轮转到 `biweekly_buffer`；v43/v49 同形停止，下一轮改验 v41/v42 两个较宽缓冲档，并保留 lowvol robust。目标是在不破坏 2020/2023 的前提下降低回撤并保持 2026 非负。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `biweekly_buffer`：v41、v42；`monthly_weekly_overlay`：lowvol-soft-exit36、lowvol-soft-exit38。
- `risk_overlay_cost`：v40、v44；`turnover_control`：v51、v52。

## 2026-08-05 二次迭代记录（约 07:29 CST）

### 上一轮候选与结果摘要

- 按 `monthly_weekly_overlay` 确认 soft-exit32/34，并与 `hkconnect_path1_biweekly_lowvol` 同窗比较。两条挑战者 2020/2023 CAGR 提升约 `9pp`，但 2026 均为 `-7.67%`，且 MaxDD/Sharpe 护栏或短窗稳定性不合格，均 `reject`。
- lowvol 为 `17.28%/22.32%/9.77%`，五窗均正，确认 `promote` 资格并维持 incumbent robust；这是 incumbent 确认，不是挑战者替换。正式 window winner/robust/tracked ID 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol
```

### 下一轮 focus 提示

- soft-exit32/34 同形停止；最终 guard 将转到 `biweekly_buffer`，下一轮验证 active v43/v49 能否守住 lowvol 的 2020/2023 并让 2026 非负。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit32、soft-exit34；`biweekly_buffer`：v43、v49。
- `risk_overlay_cost`：v40、v44；`turnover_control`：v51、v52。

## 2026-08-05 迭代记录（约 01:28 CST）

### 上一轮候选与结果摘要

- 按 `risk_overlay_cost` 确认 v40/v44，并与 `hkconnect_path1_biweekly_lowvol` 同窗比较。v40/v44 的 2020/2023/2026 CAGR 为 `15.57%/16.50%/-7.29%`、`15.16%/15.76%/-3.67%`，均破坏 2023 稳定性且短窗为负，判 `reject`。
- lowvol 为 `17.28%/22.32%/9.77%`，五窗均正，确认 `promote` 资格并维持 incumbent robust；不是挑战者替换。winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v40_risk_overlay_cost,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol
```

### 下一轮 focus 提示

- 最终 guard 转为 `monthly_weekly_overlay / rotate`。停止 v40/v44 同形，改验 active lowvol soft-exit32/34，要求 2023 缺口小于 3pp、MaxDD 不恶化 5pp且 2026 非负；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `risk_overlay_cost`：v40、v44；`biweekly_buffer`：v43、v49。
- `monthly_weekly_overlay`：lowvol-soft-exit32、lowvol-soft-exit34；`turnover_control`：v51、v53。

## 2026-08-04 二次迭代记录（约 07:29 CST）

### 上一轮候选与结果摘要

- 按 `biweekly_buffer` 五窗口确认 v41/v42，并与正式 robust `hkconnect_path1_biweekly_lowvol` 同窗比较。v41/v42 的 2020/2023/2026 CAGR 分别为 `15.29%/16.05%/-7.04%`、`15.23%/15.89%/-3.12%`，2023 相对 lowvol 均下降超过 7pp，判 `reject`。
- lowvol 为 `17.62%/22.98%/13.54%`，五窗均正，确认 `promote` 资格并维持 incumbent robust；本轮不是 challenger 替换。window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

五窗口 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260804_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已从 `biweekly_buffer` 前进到 `risk_overlay_cost`。停止 v41/v42 同形，改验未归档 active v40 与 v44 两个风险/成本档，目标是守住 lowvol 的 2023 稳定性、降低换手并让 2026 为正；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v40_risk_overlay_cost,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `risk_overlay_cost`：v40-risk-overlay、v44-cost-guard；`biweekly_buffer`：v43-buffer-repair、v49-ytd-repair。
- `monthly_weekly_overlay`：soft-exit36、soft-exit38；`turnover_control`：v51-ytd-repair、v52-cashguard-repair。

## 2026-08-04 迭代记录（约 01:30 CST）

### 上一轮候选与结果摘要

- `monthly_weekly_overlay` 确认 soft-exit36、soft-exit38，并与 `hkconnect_path1_biweekly_lowvol` 同窗比较。两条 soft-exit 的 2020/2023/2026 CAGR 均约 `26.4%/32.3%/-5.73%`，但 2023 MaxDD 相对 lowvol 恶化超过 5pp且短窗为负，均 `reject`；假设“软退出保收益同时控制回撤”未获支持。
- lowvol 的 2020/2023/2026 CAGR 为 `17.62%/22.98%/13.54%`，五窗为正，确认 `promote` 并维持 robust。无 robust/tracked 改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-08-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol
```

完整五窗口 scorecard：`results/research/a_share/research_iteration_scorecard_20260804.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `biweekly_buffer`；停止 soft-exit36/38 同形扩参，改验 v41/v42 的双周缓冲并保留 lowvol 对照；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit34、soft-exit36；`biweekly_buffer`：v41、v42；`risk_overlay_cost`：cost-guard-v30、cost-guard-v33；`turnover_control`：buffer-v51、buffer-v53。

## 2026-08-03 二次迭代记录（07:18 CST）

### 上一轮候选与结果摘要

- `risk_overlay_cost` 五窗口确认 v44/v46。两条 2020/2023/2026 CAGR 为 `15.33%/16.08%/-2.36%`、`15.51%/16.59%/0.74%`；2023 CAGR/Sharpe 相对 lowvol 均越过护栏，判定 `reject`。
- lowvol 五窗口均正，2020/2023/2026 CAGR 为 `17.75%/23.24%/14.94%`，确认 `promote` 资格并维持 robust；这是 incumbent 确认，不是挑战者替换。无 winner/robust/tracked 变化与 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `monthly_weekly_overlay`；v44/v46 同形停止，下一轮改验 soft-exit36/38，要求 2023 缺口不超过 3pp、MaxDD 不恶化 5pp 且 2026 为正。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit36、soft-exit38；`risk_overlay_cost`：v30-cost-guard、v33-cost-guard。
- `biweekly_buffer`：v41-buffer、v42-buffer；`turnover_control`：v51-ytd-repair、v53-ytd-repair。

## 2026-08-03 迭代记录（01:18 CST）

### 上一轮候选与结果摘要

- 五窗口确认 biweekly-buffer v41/v42 与正式 robust lowvol。v41/v42 的 2020/2023/2026 CAGR 为 `15.39%/16.24%/-6.34%`、`15.33%/16.08%/-2.36%`，2023 相对 lowvol 均下降约 `7pp`，触发护栏并 `reject`。
- lowvol 的 2020/2023/2026 CAGR 为 `17.75%/23.24%/14.94%`，五窗均正且平均 turnover `2.13x`，确认 `promote` 资格并维持 robust；window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803.json`。

### 下一轮 focus 提示

- 最终候选设计对齐 guard 的 `risk_overlay_cost`：停止 v41/v42 同形，改验 v44/v46 对 lowvol，要求 2023 缺口不超过 3pp 且 2026 为正。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `risk_overlay_cost`：v44-risk-overlay、v46-cost-guard；`biweekly_buffer`：v41-buffer、v42-buffer。
- `monthly_weekly_overlay`：soft-exit36、soft-exit38；`lowvol_defense`：biweekly-lowvol、monthly-lowvol。
- `turnover_control`：v51-ytd-repair、v53-ytd-repair。

## 2026-08-02 二次迭代记录（08:42 CST）

### 上一轮候选与结果摘要

- 二次确认 soft-exit36/38 与 biweekly-lowvol。两挑战者 2020/2023/2026 CAGR 均约 `26.4%/32.5%/-4.80%`，中窗 MaxDD 相对 robust 恶化超过 5pp，均 `reject`。
- biweekly-lowvol 为 `17.75%/23.24%/14.94%`，确认 `promote` 资格并维持 robust；这是 incumbent 确认，不是替换。无 winner/robust/tracked 变化与 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802_iter2.json`。

### 下一轮 focus 提示

- 转 `biweekly_buffer`，比较 v41/v42 与 biweekly-lowvol；要求 2026 为正且中窗回撤不恶化 5pp。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `biweekly_buffer`：v41-buffer、v42-buffer；`monthly_weekly_overlay`：soft-exit36、soft-exit38。
- `risk_overlay_cost`：v44-risk-overlay、v46-cost-guard；`lowvol_defense`：biweekly-lowvol、monthly-lowvol；`turnover_control`：v51-ytd-repair、v53-ytd-repair。

## 2026-08-02 迭代记录（08:12 CST）

### 上一轮候选与结果摘要

- `monthly_weekly_overlay` 确认 soft-exit36/38 与 current biweekly-lowvol robust。两条挑战者 2020/2023/2026 CAGR 均约 `26.4%/32.5%/-4.80%`，虽中窗收益更高，但 MaxDD 相对 robust 恶化超过 5pp，均 `reject`。
- biweekly-lowvol 五窗均正，2020/2023/2026 CAGR 为 `17.75%/23.24%/14.94%`，确认 `promote` 资格并维持 robust；这是 incumbent 确认，不是挑战者替换。window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802.json`。

### 下一轮 focus 提示

- 月频周度 overlay 再次因回撤失败；最终 guard 已轮换到 `biweekly_buffer`，下一轮比较 v41/v42 与 biweekly-lowvol，要求 2026 保持正收益且中窗回撤不恶化 5pp。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit36、soft-exit38；`risk_overlay_cost`：v44-risk-overlay、v46-cost-guard。
- `biweekly_buffer`：v41-buffer、v42-buffer；`lowvol_defense`：biweekly-lowvol、monthly-lowvol。
- `turnover_control`：v51-ytd-repair、v53-ytd-repair。

## 2026-08-01 二次迭代记录（07:26 CST）

### 上一轮候选与结果摘要

- `biweekly_buffer` 确认 v41 与 current biweekly-lowvol robust。v41 的 2020/2023/2026 CAGR 为 `15.39%/16.24%/-6.34%`，2023 CAGR/Sharpe 相对 robust 触发护栏，判定 `reject`。
- biweekly-lowvol 五窗均为正，2020/2023/2026 CAGR `17.75%/23.24%/14.94%`，确认 `promote` 资格并维持 robust。实验假设“v41 缓冲边界可降低回撤且保持短窗正收益”未获支持；window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260801_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已转为 focus=`monthly_weekly_overlay / continue`：停止 v41/v42 缓冲同形，转向月频选股 + 周度 soft-exit36/38，要求 2026 转正且 2023 不触发回撤护栏。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit36、soft-exit38。
- `risk_overlay_cost`：v44-cost-guard、v46-cost-guard；`biweekly_buffer`：v41-buffer、v42-buffer。
- `lowvol_defense`：biweekly-lowvol、monthly-lowvol；`turnover_control`：v51-ytd-repair、v53-ytd-repair。

## 2026-08-01 迭代记录（01:20 CST）

### 上一轮候选与结果摘要

- `monthly_weekly_overlay` 确认 lowvol-soft-exit36 与 current robust biweekly-lowvol。soft-exit36 的 2020/2023/2026 CAGR 为 `26.46%/32.54%/-4.80%`，但中窗 MaxDD 相对 robust 恶化超过 5pp，判定 `reject`。
- biweekly-lowvol 五窗均为正，2020/2023/2026 CAGR `17.75%/23.24%/14.94%`，确认 `promote` 资格并维持 robust；实验假设“月频选股加周度退出可兼顾收益与回撤”未获支持。window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_biweekly_lowvol
```

### 下一轮 focus 提示

- focus=`biweekly_buffer / rotate`：转向 v41/v42 缓冲边界，要求 2026 保持正收益且中窗不触发回撤护栏。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `biweekly_buffer`：v41-buffer、v42-buffer。
- `monthly_weekly_overlay`：soft-exit36、soft-exit38；`lowvol_defense`：biweekly-lowvol、monthly-lowvol。
- `risk_overlay_cost`：v44-cost-guard、v46-cost-guard；`turnover_control`：v51-ytd-repair、v53-ytd-repair。

## 2026-07-31 迭代记录（07:55 CST）

### 上一轮候选与结果摘要

- `monthly_weekly_overlay` 确认 soft-exit38 与 v26-ytd-positive-guard。soft-exit38 的 2020/2023 CAGR 为 `26.55%/32.73%`，但 2026 为 `-4.45%` 且回撤护栏命中，`reject`；v26 为 `20.34%/26.05%/-2.21%`，中窗较 current robust 改善且未触发硬阈值，但短窗为负，`keep_watch`。
- tracked-active 同步后的 current robust 为 `hkconnect_path1_biweekly_lowvol`，minCAGR `17.05%`；两条确认候选未替换 window winner/robust/tracked。实验假设“月频选股叠加周度退出能降低回撤”仅部分支持；无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard
```

### 下一轮 focus 提示

- focus=`monthly_weekly_overlay`：确认 soft-exit36，并继续以 biweekly-lowvol 为同窗基准，要求修复 2026 且不恶化中窗回撤。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_biweekly_lowvol
```

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit36、soft-exit38。
- `ytd_repair`：v26-ytd-positive-guard、v27-risk-overlay。
- `lowvol_defense`：biweekly-lowvol、monthly-lowvol。
- `turnover_control`：biweekly-buffered、monthly-equal-buffered。

## 2026-07-30 二次迭代记录（07:24 CST）

### 上一轮候选与结果摘要

- 在修复后的 current robust `v26_ytd_positive_guard` 基线上确认 monthly-weekly-overlay soft-exit40 与 v27 risk-overlay。两条的 2020/2023 CAGR 分别为 `25.83%/26.87%` 与 `20.36%/25.82%`，相对 robust 下降 `26.90pp/61.03pp` 与 `32.37pp/62.08pp`；2026 为 `-18.43%/-3.99%`，全部 `reject`。
- 正式 window winner、robust candidate 与 tracked payload 未改变，无 evict/archive；本轮结果是参数竞争，不把上轮数据纠偏当作晋级。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v27_risk_overlay
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 为 `monthly_weekly_overlay / continue`。soft-exit40 未修复 YTD，下一轮只确认 lowvol soft-exit38 与 current robust。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard
```

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit38、soft-exit40；`biweekly_equal_buffered`：biweekly-lowvol、v26 positive-guard。
- `lowvol_risk_overlay`：biweekly-lowvol、v27 risk-overlay；`capacity_cost`：soft-exit38、soft-exit40。

## 2026-07-30 迭代记录

### 上一轮候选与结果摘要

- `monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42` 的 2020/2023 CAGR 为 `26.36%/32.52%`、2026 为 `-6.15%`；`biweekly_lowvol` 为 `17.66%/23.08%/13.95%`。两者相对修复后的 current robust `biweekly_quality_momentum_equal_buffered_v27_risk_overlay` 都触发中窗 CAGR 护栏，均 `reject`。
- 本轮发现 `02525.HK` 换码后复权因子导致 8 倍不连续，修复后用 `tracked_active` 五窗口重建比较基线；artifact robust 与部分 window winner 因数据纠偏更新，不是新候选的参数晋级。无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path1_biweekly_lowvol
```

修复后另执行 `--family-scope tracked_active` 五窗口刷新；Scorecard：`results/research/a_share/research_iteration_scorecard_20260730.json`。

### 下一轮 focus 提示

- `monthly_weekly_overlay` 的 soft-exit42 未修复 YTD；下一轮回测较温和的 soft-exit40，并继续以 v27 robust 为同窗对照。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v27_risk_overlay
```

### Focus 候选池

- `monthly_weekly_overlay`：`...weekly_overlay_soft_exit40`、`...weekly_overlay_lowvol_soft_exit38`。
- `biweekly_equal_buffered`：`...biweekly_equal_buffered_lowvol_soft_exit40`、`...biweekly_quality_momentum_equal_buffered_v27_risk_overlay`。
- `lowvol_risk_overlay`：`...biweekly_lowvol`、`...v27_risk_overlay`。
- `capacity_cost`：`...soft_exit40`、`...lowvol_soft_exit38`。

## 2026-07-29 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair` 在 `since_2023_01` 明显弱于对照且 `since_2026_01` 为负，判定 `reject`。
- `hkconnect_path1_biweekly_lowvol` 五窗口确认通过本轮二次判断，判定 `promote`；artifact 同步后 window winner、robust candidate 与 tracked payload 未变化。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_biweekly_lowvol
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260729_iter2.json`。

### 下一轮 focus 提示

- focus：`biweekly_buffer`。v43 已失败，下一轮先用当前可生成的 lowvol 与 buffered incumbent 做再确认，不扩未注册同形参数。
- 第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_lowvol,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair
```

### Focus 候选池

- `biweekly_buffer`：`hkconnect_path1_biweekly_lowvol`、`...v43_biweekly_buffer_repair`。
- `quality_momentum`：`hkconnect_path1_biweekly_quality_momentum_equal_buffered`、`hkconnect_path1_biweekly_lowvol`。
- `lowvol_defense`：`hkconnect_path1_biweekly_lowvol`、`hkconnect_path1_monthly_lowvol`。
- `cost_capacity`：buffered equal-weight、biweekly lowvol。

## 2026-07-29 迭代记录

### 上一轮候选与结果摘要

- 按 `monthly_weekly_overlay` 五窗口确认 lowvol soft-exit36/38，并与正式 robust `hkconnect_path1_biweekly_lowvol` 同窗比较。两条 overlay 的 2020/2023 CAGR 仍优于 robust，但 2026 CAGR 均为 `-3.92%`，实验假设“继续放宽退出可修复 YTD”未获支持，均 `keep_watch`。
- biweekly-lowvol 的 2026 CAGR 为 `9.55%`，五窗口确认 `promote`；window winner、robust candidate 与 tracked payload 均未改变，无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`、正式 robust `hkconnect_path1_biweekly_lowvol`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260729.json`。

### 下一轮 focus 提示

- 当前 focus 为 `monthly_weekly_overlay`。soft-exit36/38 已同形失败，下一轮以已注册 soft-exit42 验证“更宽退出能否让 2026 转正且守住中窗”；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit42、biweekly-lowvol；`risk_overlay_cost`：v27 risk-overlay、biweekly-lowvol；`biweekly_buffer`：v43 buffer-repair、biweekly-lowvol；`return_recovery`：lowvol-soft-exit42、biweekly-lowvol。

## 2026-07-28 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- 按 `monthly_weekly_overlay` 五窗口确认 lowvol soft-exit32/34，并与正式 robust `hkconnect_path1_biweekly_lowvol` 同窗比较。两条 overlay 的 2020/2023 CAGR 为 `26.70%/33.77%` 与 `26.58%/33.74%`，明显高于 robust `18.52%/23.31%`；但 2026 均为 `-4.44%`、2023 turnover 约 `3.16x/3.14x`，因此只 `keep_watch`。
- biweekly-lowvol 五窗口确认 `promote`，2026 CAGR `8.17%`；window winner/robust/tracked 未变化，无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`、`...soft_exit34`、正式 robust `hkconnect_path1_biweekly_lowvol`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728_iter2.json`。

### 下一轮 focus 提示

- 当前 focus 为 `monthly_weekly_overlay`。soft-exit32/34 的负 2026 已确认，下一轮检查 soft-exit36 是否形成收益/退出折中；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol-soft-exit36、lowvol-soft-exit38；`risk_overlay_cost`：v27 risk-overlay、biweekly-lowvol；`biweekly_buffer`：v43 buffer-repair、biweekly-lowvol；`return_recovery`：soft-exit36、biweekly-lowvol。

## 2026-07-28 迭代记录

### 上一轮候选与结果摘要

- 按 `risk_overlay_cost` 五窗口确认 v44/v46，并与正式 robust `hkconnect_path1_biweekly_lowvol` 比较。v44/v46 的 2023 CAGR 为 `16.11%/16.20%`，相对 robust 下降 `7.21pp/7.11pp`，2026 CAGR 为 `-7.70%/-5.27%`，均触发中窗稳定性护栏并 `reject`；风险覆盖成本守门未修复短窗。
- biweekly-lowvol 五窗口确认 `promote`，window winner/robust/tracked 未变化，无 evict。

### 本轮候选 ID 与命令

- 候选：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard`、`...v46_risk_overlay_cost_guard`、`hkconnect_path1_biweekly_lowvol`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728.json`。

### 下一轮 focus 提示

- 最终 focus 仍为 `risk_overlay_cost`。下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v27_risk_overlay,hkconnect_path1_biweekly_lowvol`，用较轻 risk overlay 检查 v44/v46 是否过度防守。

### Focus 候选池

- `risk_overlay_cost`：v27 risk-overlay、biweekly-lowvol；`biweekly_buffer`：v43 buffer-repair、biweekly-lowvol；`monthly_weekly_overlay`：soft-exit32、soft-exit34；`return_recovery`：v45 monthly-weekly-repair、biweekly-lowvol。

## 2026-07-27 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 按 `biweekly_buffer` 五窗口确认 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`，并与正式 robust `hkconnect_path1_biweekly_lowvol` 同窗比较。挑战者 2023 CAGR 提高 `6.03pp`，但 2026 CAGR `-7.56%`、2023 turnover `5.10x`，显著高于 robust 的 `1.58x`，仅 `keep_watch`；正式 robust 五窗口确认 `promote`。window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`、`hkconnect_path1_biweekly_lowvol`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727_iter2.json`。

### 下一轮 focus 提示

- 当前 focus 为 `biweekly_buffer`。soft-exit38 的 2026 与换手不合格，下一轮改回 v43 buffer-repair 与 incumbent；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `biweekly_buffer`：v43 buffer-repair、biweekly-lowvol；`monthly_weekly_overlay`：soft-exit32、soft-exit34；`risk_overlay_cost`：v46、biweekly-lowvol；`return_recovery`：v45 monthly-weekly-repair、biweekly-lowvol。

## 2026-07-27 迭代记录

### 上一轮候选与结果摘要

- 按 `monthly_weekly_overlay` 五窗口确认 lowvol soft-exit32/34，并与正式 robust `hkconnect_path1_biweekly_lowvol` 同窗比较。两条 overlay 的 2020/2023 CAGR 为 `26.70%/33.77%` 与 `26.58%/33.74%`，显著高于 robust，但 2026 CAGR 均为 `-4.44%`，实验假设“软退出可兼顾长中窗与 YTD”只在长中窗获支持，均 `keep_watch`；biweekly-lowvol 五窗确认 `promote`。window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`、`hkconnect_path1_biweekly_lowvol`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727.json`。

### 下一轮 focus 提示

- 最终 focus 轮换为 `biweekly_buffer`。soft-exit32/34 的 YTD 同形失败，下一轮改确认双周 equal-buffered 低波形态；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：v45 monthly-weekly-repair、soft-exit34；`risk_overlay_cost`：soft-exit32、biweekly-lowvol；`biweekly_buffer`：biweekly-lowvol、biweekly-equal-buffered-lowvol-soft-exit38；`return_recovery`：v45、biweekly-lowvol。

## 2026-07-26 二次迭代记录（07:19 CST）

### 上一轮候选与结果摘要

- 按 `risk_overlay_cost` 五窗口确认 v46 与正式 robust `hkconnect_path1_biweekly_lowvol`。v46 的 2023 CAGR/Sharpe 分别下降约 `7.12pp/0.36`，2026 CAGR `-5.27%`，触发稳定性护栏并判定 `reject`；lowvol 五窗口全正，同端点确认 `promote`。实验假设“风险覆盖降低成本且守住中窗”未获支持，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726_iter2.json`。

### 下一轮 focus 提示

- v46 同形停止；下一轮回到 `monthly_weekly_overlay`，比较 lowvol soft-exit32/34。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `risk_overlay_cost`：v46、biweekly-lowvol；`monthly_weekly_overlay`：lowvol soft-exit32、soft-exit34；`biweekly_buffer`：v43、v49。

## 2026-07-26 迭代记录

### 上一轮候选与结果摘要

- 按 `biweekly_buffer` 五窗口确认 v49 YTD-repair 与正式 robust `hkconnect_path1_biweekly_lowvol`。v49 的 2025 CAGR 高 `4.44pp`、回撤较浅，但 2023 CAGR 低 `7.12pp`、turnover 超过两倍且 2026 CAGR `-4.91%`，判定 `reject`；lowvol 五窗全正，确认 `promote`。window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `risk_overlay_cost`。v49 未修复 2026 且换手过高，下一轮改查 v46 risk-overlay-cost-guard 与 lowvol 的成本风险边界。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：lowvol soft-exit32、soft-exit34；`biweekly_buffer`：v43 buffer-repair、v49 YTD-repair。
- `risk_overlay_cost`：biweekly-lowvol、v46 risk-overlay-cost-guard。

## 2026-07-25 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 按 `monthly_weekly_overlay` 五窗口确认 lowvol soft-exit34/36 与 current robust `biweekly_lowvol`。两条 overlay 的 2020/2023 CAGR 比 robust 高约 `7.9pp-10.4pp`，回撤也更浅，但 2026 CAGR 均为 `-4.44%`，只能 `keep_watch`；lowvol 五窗全正，确认 `promote`。
- Path1 多个中长窗口机械 winner 可变化，但 robust/tracked 未被负 2026 候选替换，无 evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path1_biweekly_lowvol`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260725_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `biweekly_buffer`；下一轮用 v49 与 incumbent lowvol 检查缓冲修复，不继续扩展负 2026 的月选周控同形。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `monthly_weekly_overlay`：soft-exit32、soft-exit34；`risk_overlay_cost`：biweekly-lowvol、v46 risk-overlay-cost-guard。
- `biweekly_buffer`：v49 YTD-repair、biweekly-lowvol；`return_recovery`：v43 buffer-repair、biweekly-lowvol。

## 2026-07-25 迭代记录

### 上一轮候选与结果摘要

- 五窗口确认 `v49_biweekly_buffer_ytd_repair` 与 incumbent `biweekly_lowvol`。v49 的 2023 CAGR 比 incumbent 低 `7.12pp`、2026 CAGR `-4.91%`，判 `reject`；lowvol 五窗稳定，2020/2023/2026 CAGR `18.52%/23.31%/8.17%`，判 `promote`（确认 incumbent）。
- window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。

- stale 修复：对上述全部候选把同一 `--only-strategy-ids` 命令的 `--end-date` 改为 `2026-07-24` 后完成五窗增量复跑；最终 scorecard 与 strategy JSON 均采用该终点。

### 下一轮 focus 提示

- 最终 guard 为 `monthly_weekly_overlay`：用 lowvol soft-exit 34/36 检查月选周控形态；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`。

### Focus 候选池

- `risk_overlay_cost`：v46 risk-overlay-cost-guard、biweekly-lowvol；`biweekly_buffer`：v49 YTD-repair、v43 buffer-repair。
- `monthly_weekly_overlay`：lowvol-soft-exit34、lowvol-soft-exit36。
- `return_recovery`：v43 buffer-repair、biweekly-lowvol；`ytd_positive_guard`：v26 YTD-guard、v49 YTD-repair。

## 2026-07-24 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 上一轮 v49 为 `keep_watch`、`biweekly_lowvol` 确认 incumbent robust；本轮按 `biweekly_buffer` 五窗口确认 v46/v43，并继续与 `hkconnect_path1_biweekly_lowvol` 同窗比较。
- v46/v43 的 2023 CAGR 为 `16.51%/16.37%`，相对 robust 下降约 `6.8pp/7.0pp`，Sharpe 下降约 `0.34/0.35`，2026 CAGR 均为 `-4.03%`；两条均 `reject`。window winner/robust/tracked 未改写，无 evict。

### 本轮候选 ID 与命令

- 候选：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair`。

### 下一轮 focus 提示

- 最终 guard 轮换到 `risk_overlay_cost`；停止 v43/v46 同形扩参，回到 v49 与 lowvol 做风险/成本相邻确认；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `biweekly_buffer`：v49 YTD-repair、`biweekly_lowvol`。
- `risk_overlay_cost`：v49 YTD-repair、`biweekly_lowvol`。
- `risk_overlay`：v46 risk-overlay、v49 YTD-repair。
- `turnover_cost`：`biweekly_lowvol`、v43 buffer-repair。

## 2026-07-24 收尾记录

### 上一轮候选与结果摘要

- 五窗口确认 v49 与 `biweekly_lowvol`。v49 的 2020/2023 CAGR `16.80%/16.46%`，但 2026 CAGR `-3.26%`，判 `keep_watch`；lowvol 五窗 CAGR 全正、2020/2023 为 `18.53%/23.34%`、2026 为 `8.26%`，判 `promote`（确认 incumbent robust）。
- 低波 robust 保持不变，没有 tracked/window winner 改写或 active evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_lowvol`。

### 下一轮 focus 提示

- `biweekly_buffer` 只保留能让 2026 转正且不损失中窗超过 3pp 的变体；首条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path1_biweekly_lowvol`。

### Focus 候选池

- `biweekly_buffer`：v46 risk-overlay cost-guard、v49 YTD-repair。
- `lowvol_defense`：`biweekly_lowvol`、`monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`。

## 2026-07-23 收尾记录

### 上一轮候选与结果摘要

- 五窗口确认 v45 月选周控与 v49 双周 buffer。两条 2020/2023 尚可，但 2026 CAGR 分别 `-10.88%/-5.95%`，均判 `keep_watch`；当前 robust `hkconnect_path1_biweekly_lowvol` 的 2026 CAGR 为 `5.11%`，winner/robust/tracked 未变。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v45_monthly_weekly_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`。

### 下一轮 focus 提示

- 下一轮优先做 2026 防守修复；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_lowvol,hkconnect_path1_monthly_quality_momentum_weekly_overlay_v46_ytd_guard`。

### Focus 候选池

- `monthly_weekly_overlay`：v45、v46；`biweekly_buffer`：v49、biweekly-lowvol；`risk_overlay_repair`：v45、v49；`risk_overlay_cost`：biweekly-lowvol、v45。scorecard：`results/research/a_share/research_iteration_scorecard_20260723.json`。

## 2026-07-22 收尾记录

- 上一轮候选与结果摘要：上一轮 v49 留短窗观察、v53 淘汰；本轮按 `monthly_weekly_overlay` 五窗口确认 v45/v48，并与 `hkconnect_path1_biweekly_lowvol` 同端点比较。
- 本轮候选 ID 与命令：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v45_monthly_weekly_repair`、`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v45_monthly_weekly_repair,hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay`。
- Scorecard 与判定：v45 的 2020/2023 CAGR 为 `21.39%/20.69%`，未触发中窗护栏，但 2026 CAGR `-19.56%`，判 `keep_watch`；v48 的 2023 CAGR 相对 robust 低约 `4.79pp` 且 2026 `-19.76%`，判 `archive` 并加入 `HK_ARCHIVED_STRATEGY_IDS`。window winner/robust/tracked 未变。
- 下一轮 focus 提示：v45 只有在 2026 转正且 2023 不退化时才继续保留。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v45_monthly_weekly_repair`。
- Focus 候选池：`monthly_weekly_overlay` -> v45、`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v46_ytd_guard`；`biweekly_buffer` -> v49、`hkconnect_path1_biweekly_lowvol`；`risk_overlay_repair` -> v45、v49；`risk_overlay_cost` -> `hkconnect_path1_biweekly_lowvol`、v45。完整 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260722.json`。

## 2026-07-21 收尾记录

- 上一轮候选与结果摘要：上一轮月频周控 v56/v57 淘汰；本轮按双周 buffer 与 `risk_overlay_cost` 确认 v49/v53，两条均覆盖五窗口并与 `hkconnect_path1_biweekly_lowvol` 同窗比较。
- 本轮候选 ID 与命令：执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair`。
- Scorecard 与判定：v49 的 2020/2023 CAGR `16.10%/15.15%`、2025 `28.85%`，进入 2025 窗口 winner，但 2023 相对 robust 触发护栏且 2026 `-12.01%`，判 `keep_watch`；v53 的 2020/2023 `14.15%/13.23%`、2026 `-15.29%`，被 v49 支配，判 `reject`。robust/tracked 主体不变。
- 下一轮 focus 提示：最终 guard 为 `risk_overlay_cost`；先复核 v49，要求 2026 转正且 2023 不再触发 3pp 护栏。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`。
- Focus 候选池：`monthly_weekly_overlay` -> `v54_signal_buffer`、`v55_drawdown_buffer`；`biweekly_buffer` -> `v49_biweekly_buffer_ytd_repair`、`hkconnect_path1_biweekly_lowvol`；`risk_overlay_repair` -> `v49_biweekly_buffer_ytd_repair`、`v53_biweekly_buffer_ytd_repair`；`risk_overlay_cost` -> `v49_biweekly_buffer_ytd_repair`、`hkconnect_path1_biweekly_lowvol`。
- evict/归档：v53 加入 `HK_ARCHIVED_STRATEGY_IDS`；v49 留 watch。完整 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260721.json`。

## 2026-07-20 收尾记录

- 上一轮候选与结果摘要：上一轮月频周控 v54/v55 均失败；本轮继续 `monthly_weekly_overlay`，新增低波 v56 与质量动量 v57，并把 robust `hkconnect_path1_biweekly_lowvol` 刷新到同端点。
- 本轮候选 ID 与命令：执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_lowvol_weekly_overlay_v56_ytd_repair,hkconnect_path1_monthly_quality_momentum_weekly_overlay_v57_return_repair`。
- Scorecard 与判定：v56/v57 相对 robust 的 2023 CAGR 低 `7.79pp/8.24pp`、Sharpe 低 `0.304/0.341`，2026 CAGR `-22.54%/-14.06%`；假设未获支持，均 `reject` 并移出 active。window winner/robust/tracked 不改变。
- 下一轮 focus 提示：停止月频周控同形扩参，转回双周 buffer 与风险成本。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_lowvol_quality_equal_buffered_v58_return_risk_balance`；未注册原因：本轮先归档 v56/v57。
- Focus 候选池：`monthly_weekly_overlay` -> `v58_overlay_return_balance`、`v59_overlay_risk_guard`；`biweekly_buffer` -> `v58_return_risk_balance`、`v59_biweekly_cost_guard`；`risk_overlay_repair` -> `v58_soft_exit_risk_guard`、`v59_lowvol_cost_guard`。
- evict/归档：v56/v57 写入 `HK_ARCHIVED_STRATEGY_IDS`，定义与 CSV 历史保留。

## 2026-07-19 收尾记录

- 上一轮候选与结果摘要：上一轮双周 v53 仍未替换 robust；本轮按 `monthly_weekly_overlay` 五窗口实跑月度质量动量周控 `v54_signal_buffer`、`v55_drawdown_buffer`，继续与 HK Path1 robust `hkconnect_path1_biweekly_lowvol` 同窗比较。
- 本轮候选 ID 与命令：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v54_signal_buffer`、`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v55_drawdown_buffer`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <上述 2 个 IDs>`。
- Scorecard 与判定：v54/v55 的 2020 CAGR 为 `17.66%/16.67%`，但 2023 仅 `15.26%/14.37%`，相对 robust 低 `6.21pp/7.09pp`，2026 CAGR 为 `-20.20%/-18.63%`；均命中稳定性破坏，判定 `reject`，从 active variants 移除。window winner、robust candidate、tracked payload 均未改变。
- 下一轮 focus 提示：最终 guard 为 `monthly_weekly_overlay`。第一条可执行命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair`；下一变体必须优先修复 2026，不再继续同形月频降 cap。
- Focus 候选池：`monthly_weekly_overlay` -> `v53_biweekly_buffer_ytd_repair`、`v56_monthly_weekly_overlay_ytd_guard`；`biweekly_buffer` -> `v49_biweekly_buffer_ytd_repair`、`v57_biweekly_drawdown_repair`；`risk_overlay_repair` -> `v58_soft_exit_risk_guard`、`v59_lowvol_cost_guard`。
- evict/归档：v54/v55 已从 HK Path1 active 列表移除，CSV 五窗口历史保留。

## 2026-07-09 收尾记录

- 上一轮候选与结果摘要：上一轮 v53 仍未确认能修复 2026；本轮继续按 `biweekly_buffer` 实跑 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair`，保持 HK Path1 独立于 A股与 HK Path2/3/扩展线。
- 本轮候选 ID 与命令：实跑 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair,hkconnect_path2_theme_biweekly_quality_liquidity_breakout_v53_drawdown_guard,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff42_turnover0_exit58_v32_turnover_reduction_retest,hkconnect_path4_quality_momentum_monthly_ytd_positive_v46_lowdraw_ytd_guard,hkconnect_path5_pullback_continuation_monthly_quality_retest_v36_lowturn_pullback_definition,hkconnect_path6_lowvol_liquid_biweekly_quality_ytd_guard_v42_lowvol_liquid_core_repair,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_turnover_control_v41_core_sleeve_turnover_control`。
- Scorecard 与判定：v53 五窗口 CAGR `15.28% / 14.34% / 13.69% / 27.48% / -16.01%`、MaxDD 最差 `-19.23%`、turnover 最高 `4.99x`；相对 robust `hkconnect_path1_biweekly_lowvol`，2026 防守明显更差，判定 `reject`。window winner、robust candidate、tracked payload 未改变。
- 下一轮 focus 提示：最终 guard 轮换到 `risk_overlay_cost`，下一轮从质量动量回到低波/风险覆盖成本线。第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_lowvol_equal_buffered_v53_risk_overlay_cost`；若未注册，先加入 HK Path1 variants。
- Focus 候选池：`biweekly_buffer` -> `hkconnect_path1_biweekly_lowvol_quality_equal_buffered_v54_cashguard_repair`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v55_biweekly_buffer_ytd_repair`；`monthly_weekly_overlay` -> `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v53_ytd_drawdown_repair`、`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v54_lowvol_weekly_overlay_repair`；`risk_overlay_cost` -> `hkconnect_path1_biweekly_quality_lowvol_equal_buffered_v53_risk_overlay_cost`、`hkconnect_path1_biweekly_lowvol_quality_equal_buffered_v54_cashguard_repair`。
- evict/归档：本轮无 HK Path1 evict；v53 标记 `reject`，下一轮不继续同形质量动量 buffer 小修。

## 2026-07-08 收尾记录

- 上一轮候选与结果摘要：上一轮 Path1 低波现金保护失败；本轮按 `biweekly_buffer` 实跑 v53，仍保持 HK Path1 独立于 A股与 HK Path2/3/扩展线。
- 本轮候选 ID 与命令：实跑 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair,<hk_path2_v46>,<hk_path3_v32>,<hk_path4_v46>,<hk_path5_v36>,<hk_path6_v42>,<hk_path7_v41>`。
- Scorecard 与判定：v53 在 2020/2023 CAGR `14.34% / 13.69%`、Sharpe `0.828 / 0.801`、MaxDD `-15.94% / -11.49%`、turnover `3.41x / 3.58x`，仍未超过 robust `hkconnect_path1_biweekly_lowvol`，判定 `keep_watch`；window winner、robust candidate、tracked payload 未改变。
- 下一轮 focus 提示：最终 guard 仍为 `biweekly_buffer`。第一条命令改测低波质量缓冲：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_lowvol_quality_equal_buffered_v54_cashguard_repair`；若未注册，先加入 HK Path1 variants。
- Focus 候选池：`biweekly_buffer` -> `hkconnect_path1_biweekly_lowvol_quality_equal_buffered_v54_cashguard_repair`、`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v55_biweekly_buffer_ytd_repair`；`monthly_weekly_overlay` -> `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v53_ytd_drawdown_repair`、`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v54_lowvol_weekly_overlay_repair`；`risk_overlay_cost` -> `hkconnect_path1_biweekly_quality_lowvol_equal_buffered_v53_risk_overlay_cost`、`hkconnect_path1_biweekly_lowvol_quality_equal_buffered_v54_cashguard_repair`。
- evict/归档：本轮无 HK Path1 evict；v53 若连续三轮无法修复 2026 或超过 robust，应归档为双周 buffer 负样本。

## 2026-07-08 迭代状态

- 上一轮候选/结果摘要：上一轮 v52 低波/现金保护线判定 `reject`，未修复 2026；本轮 HK Path1 coverage 完整，只做巡检、tracked/live/public 同步和下一轮候选设计，仍独立于 A股 winner 与 HK Path2/3/扩展线。
- 本轮候选 ID 与命令：本轮没有新增 HK Path1 `--only-strategy-ids`；未跑原因是 HK 新增确认预算优先给 Path2 high-return monthly 和 HK Path4-7 扩展线。下一轮第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v53_ytd_drawdown_repair`。
- Scorecard 与判定：本轮 Path1 无新增实跑 scorecard；`scripts/update_hkconnect_artifacts.py` 后 robust 仍为 `hkconnect_path1_biweekly_lowvol`，判定 `keep_watch`。v53 假设是用月频质量动量 + 周度 overlay 修复 2026 负收益，同时不放大 2017/2020 回撤。
- evict/归档：本轮无 HK Path1 evict；v52 继续作为低波现金保护失败样本保留。
- 下一轮 focus：若 guard 继续 `monthly_weekly_overlay`，执行 v53；若转到 `biweekly_buffer`，第一条命令改为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair`。
- Focus 候选池：`monthly_weekly_overlay` -> `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v53_ytd_drawdown_repair`、`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v54_lowvol_weekly_overlay_repair`；`biweekly_buffer` -> `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair`、`hkconnect_path1_biweekly_lowvol_quality_equal_buffered_v54_cashguard_repair`；`risk_overlay_cost` -> `hkconnect_path1_biweekly_quality_lowvol_equal_buffered_v53_risk_overlay_cost`、`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v53_ytd_drawdown_repair`。

## 2026-07-07 迭代状态

- 上一轮候选/结果摘要：上一轮 HK Path1 v51 未修复 2026 负收益；本轮注册并五窗口确认 v52 低波/现金保护线，保持 HK Path1 独立于 A股 winner 与 HK Path2/3/扩展线。
- 本轮候选 ID 与命令：新增 `hkconnect_path1_biweekly_quality_lowvol_equal_buffered_v52_ytd_cashguard_repair`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_lowvol_equal_buffered_v52_ytd_cashguard_repair,<hk_path2_v53>,<hk_path3_v31>,<hk_path4_v44>,<hk_path5_v34>,<hk_path6_v40>,<hk_path7_v39>`；首次带 `--end-date 2026-07-03` 的结果因 public freshness 护栏要求，又按最新 raw cache 无 `--end-date` 复跑。
- Scorecard 与判定：v52 五窗口 CAGR `11.32% / 10.31% / 13.62% / 23.64% / -19.88%`，Sharpe `0.745 / 0.662 / 0.785 / 1.424 / -1.501`，MaxDD 最差 `-24.60%`，turnover `1.33x / 1.33x / 1.01x / 0.95x / 2.37x`。相对当前 Path1 robust `hkconnect_path1_biweekly_lowvol`，2020/2023 CAGR 分别低 `7.08pp / 7.55pp`，2026 更差，判定 `reject`；window winner、robust candidate、tracked payload 未改变。
- evict/归档：本轮无 HK Path1 evict；v52 作为低波现金保护的 2026 失败样本保留。
- 下一轮 focus：第一条命令建议切回月频质量动量周控的 drawdown 修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v53_ytd_drawdown_repair`；若未注册，先在 HK Path1 variants 中注册。
- Focus 候选池：`risk_overlay_cost` -> `hkconnect_path1_biweekly_quality_lowvol_equal_buffered_v53_risk_overlay_cost`、`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v53_ytd_drawdown_repair`；`biweekly_buffer` -> `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v53_biweekly_buffer_ytd_repair`、`hkconnect_path1_biweekly_lowvol_quality_equal_buffered_v54_cashguard_repair`；`monthly_weekly_overlay` -> `v53_ytd_drawdown_repair`、`v54_lowvol_weekly_overlay_repair`。

## 2026-07-06 迭代状态

- 上一轮候选/结果摘要：上一轮把下一步指向 `biweekly_buffer` v51；本轮已注册并五窗口确认，保持 HK Path1 独立于 A股 winner 与 HK Path2/3/扩展线。
- 本轮候选 ID 与命令：新增 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v51_biweekly_buffer_ytd_repair`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_v51>,<hk_path2_v44>,<hk_path3_v30>,<hk_path4_v43>,<hk_path5_v33>,<hk_path6_v39>,<hk_path7_v38>`。
- 五窗口结果：CAGR `15.88% / 14.99% / 14.21% / 27.74% / -16.62%`，最大回撤最差 `-19.03%`。结论：v51 没有修复 2026 负收益，未替换 HK Path1 window winner、robust candidate 或 tracked payload。
- evict/归档：本轮无 HK Path1 evict；v51 作为双周质量动量缓冲的 2026 失败样本保留。
- 下一轮 focus：若最终 guard 仍给 `biweekly_buffer`，不要复跑 v51，转向低波/现金保护的 2026 修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_lowvol_equal_buffered_v52_ytd_cashguard_repair`；若未注册，先在 HK Path1 variants 中注册。

## 2026-07-05 迭代状态

- 上一轮候选/结果摘要：上一轮 HK Path1 继续留下 v50 月频质量动量周控候选；本轮新增 HK 回测预算投给 Path2/6/7，Path1 完成 guard 巡检、`tracked_active` 同步、artifact/live/public 同步和下一轮候选设计，仍独立于 A股 winner。
- 本轮候选 ID 与命令：本轮没有新增 HK Path1 `--only-strategy-ids`；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `scripts/update_hkconnect_artifacts.py`、`scripts/export_live_platform_data.py`、`scripts/generate_public_snapshot.py`。
- 结论：HK Path1 window winner/robust 未由本轮新实验改变；tracked/robust 仍沿用既有低波与双周缓冲主体。本轮只产生同步信息，不并入 A股 winner。
- evict/归档：本轮无 HK Path1 evict；未回测原因是本轮 HK 新增预算优先给 Path2 的高收益月频修复与 Path6/7 扩展零交易修复。
- 下一轮 focus：最终 guard 已轮换到 `biweekly_buffer`；第一候选改为 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v51_biweekly_buffer_ytd_repair`，命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v51_biweekly_buffer_ytd_repair`；若未注册，先在 HK Path1 variants 中注册。

## 2026-07-04 07:03 CST 状态

- 上一轮候选/结果摘要：上一轮留下 HK Path1 v50 月频质量动量周控候选；本轮新增 HK 回测预算投给 Path2/3/4/5，Path1 完成 guard 巡检、`tracked_active`、artifact/live/public 同步和下一轮候选设计，仍独立于 A股 winner。
- 本轮候选 ID 与命令：本轮没有新增 HK Path1 `--only-strategy-ids`；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 以及 `scripts/update_hkconnect_artifacts.py`、`scripts/export_live_platform_data.py`、`scripts/generate_public_snapshot.py`。
- 结论：HK Path1 window winner/robust 未由本轮新实验改变；tracked 当前为 2017/2020 `monthly_equal_buffered_weekly_overlay_soft_exit32`，2023 `monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`，2025 `v49_biweekly_buffer_ytd_repair`，2026 `hkconnect_path1_biweekly_lowvol`，robust 仍为 `hkconnect_path1_biweekly_lowvol`。
- evict/归档：本轮无 HK Path1 evict；未回测原因是本轮 HK 新增预算优先给 rotate 更久的 Path2 与扩展线，同时 Path1 coverage 已完整。
- 下一轮 focus：最终 guard 给出 `monthly_weekly_overlay`。下一轮第一候选仍是 `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v50_ytd_drawdown_repair`，命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v50_ytd_drawdown_repair`；若未注册，先在 HK Path1 variants 中注册。

## 2026-07-01 20:58 CST 状态

- 上一轮候选/结果摘要：上一轮只设计 HK Path1 v49；本轮已注册并五窗口确认，保持 HK Path1 独立于 A股 winner 与 HK Path2/3/扩展线。
- 本轮候选 ID 与命令：新增 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair,<hk_path2_v50>,<hk_path3_v26>`。
- 五窗口结果：CAGR `16.85% / 16.05% / 15.13% / 29.34% / -14.57%`，最大回撤 `-19.06% / -16.38% / -12.67% / -9.18% / -8.94%`，年均换手最高 `5.01x`。
- 结论：v49 没有修复 2026 负收益，未替换 HK Path1 window winner、robust candidate 或 tracked payload；当前 robust 仍为 `hkconnect_path1_biweekly_lowvol`。
- evict/归档：本轮无 HK Path1 evict；但 v49 后续若继续 2026 为负，应从双周质量动量缓冲槽回到低波/现金保护线。
- 下一轮 focus：最终 guard 给出 `monthly_weekly_overlay`；下一候选回到月频质量动量+周控，并优先修复 2026 负收益：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v50_ytd_drawdown_repair`，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v50_ytd_drawdown_repair`；若未注册，先在 HK Path1 variants 中注册。

## 2026-07-01 05:26 CST 状态

- 上一轮候选/结果摘要：上一轮 HK Path1 v48 未修复 2026 负收益；本轮 HK 新增预算投给 Path5/6/7 扩展线，Path1 完成 guard 巡检、artifact/live/public 同步与下一轮候选设计，保持 HK 研究线独立于 A股 winner。
- 本轮候选 ID 与命令：本轮没有新增 HK Path1 `--only-strategy-ids`；执行 `.venv/bin/python scripts/update_hkconnect_artifacts.py`、`.venv/bin/python scripts/export_live_platform_data.py`、`.venv/bin/python scripts/generate_public_snapshot.py` 同步 HK tracked/live/public。
- 结论：HK Path1 window winner、robust candidate、tracked payload 未改变；本轮没有 HK Path1 evict。最终 guard coverage 为 HK 全候选 complete，Path1 focus 为 `biweekly_buffer`。
- 下一轮 focus：候选 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`；若未注册，先在 HK Path1 variants 中注册。

## 2026-06-30 17:26 CST 状态

- 上一轮候选/结果摘要：上一轮 HK Path1 只做同步并把下一步指向月频质量动量周控；本轮实际注册并五窗口确认 v48，保持 HK 研究线独立于 A股 winner。
- 本轮候选 ID 与命令：新增并运行 `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay`；命令并入 HK 受限回测 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay,<hk_path2_v48>,<hk_path3_v25>,<hk_path4_v38>`。
- 五窗口结果：CAGR `16.12% / 19.88% / 19.01% / 30.32% / -10.38%`，最大回撤最差 `-26.95%`，Sharpe `1.0357 / 1.1680 / 1.1029 / 1.4183 / -0.2830`。
- 结论：v48 仍未修复 2026 负收益，且 2017 回撤偏深；HK Path1 window winner、robust candidate、tracked payload 未改变。本轮无 HK Path1 evict。
- 下一轮 focus：最终 guard 给出 `biweekly_buffer`。下一轮第一候选建议回到双周质量动量缓冲 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`，命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v49_biweekly_buffer_ytd_repair`；若未注册，先在 HK Path1 variants 中注册。

## 2026-06-30 06:12 CST 状态

- 上一轮候选/结果摘要：上一轮 HK Path1 v46 风险覆盖线 2026 仍为负；本轮新增 HK 回测预算投给 HK Path2 与 HK Path5/6/7 扩展线，Path1 完成 guard 巡检、artifact/public/live 同步与下一轮候选设计。
- 本轮候选 ID 与命令：本轮没有新增 HK Path1 `--only-strategy-ids`；执行 `.venv/bin/python scripts/update_hkconnect_artifacts.py`、`.venv/bin/python scripts/export_live_platform_data.py`、`.venv/bin/python scripts/generate_public_snapshot.py` 同步 HK tracked/live/public。
- 结论：HK Path1 window winner、robust candidate、tracked payload 未改变；本轮没有 HK Path1 evict。最终 guard coverage 为 HK 全候选 complete，Path1 focus 为 `monthly_weekly_overlay`。
- 下一轮 focus：优先修复 2026 负收益的月频质量动量 + 周度 overlay，候选 `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay`；首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay`；若未注册，先在 HK Path1 variants 中注册。

## 2026-06-29 17:30 CST 状态

- 上一轮候选/结果摘要：上一轮留下双周质量动量风险覆盖 v46；本轮注册并五窗口确认，不并入 A股 winner 结论。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard`；命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard,hkconnect_path2_theme_biweekly_quality_liquidity_breakout_v47_lowturn_confirmation,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff38_turnover0_exit52_v24_cost_stress,hkconnect_path4_quality_momentum_monthly_lowdraw_v37_quality_momentum_ytd_guard`。
- 五窗口结果：CAGR `16.99% / 16.67% / 15.79% / 28.40% / -13.75%`，最大回撤最差 `-18.85%`，2026 观察窗为负。
- 结论：HK Path1 window winner、robust candidate 与 tracked payload 未改变；本轮没有 HK Path1 evict。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> biweekly_buffer`。下一轮第一候选建议补一条更低 2026 drawdown 的双周缓冲修复：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v47_biweekly_buffer_ytd_repair`；首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v47_biweekly_buffer_ytd_repair`。

## 本轮执行计划（2026-06-29 05:25 CST）

- 上一轮 HK Path1 的 `v46_ytd_guard` 已确认但 2026 仍为负；本轮新增 HK 预算投给 Path4-7 扩展线，HK Path1 完成 guard 巡检、`scripts/update_hkconnect_artifacts.py` 与 public/live 同步，没有新增 Path1 `--only-strategy-ids` 回测，也没有把 HK 扩展线并入 Path1 结论。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 未切换；本轮无 HK Path1 evict。最终 guard coverage 为 HK 全候选 `452/452`，Path1 候选数 `105`。
- 最终 focus 为 `monthly_weekly_overlay`。下一轮第一条命令建议从双周/普通风险成本线转回月频选股 + 周度 overlay，优先修复 2026 负收益并控制 2017 回撤：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-28 17:40 CST）

- 上一轮 HK Path1 下一步指向 `risk_overlay_cost`；本轮接续检查已注册/已落盘的五窗口候选 `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v46_ytd_guard`，并执行 `scripts/update_hkconnect_artifacts.py`、live/public 导出同步。没有额外裸跑 HK 全量或 `research_active`。
- v46 五窗口 CAGR `17.09% / 21.62% / 22.07% / 34.37% / -5.99%`，最大回撤 `-27.38% / -11.60% / -10.06% / -10.22% / -8.96%`，换手 `3.27x / 3.17x / 3.12x / 3.31x / 3.88x`。结论：2020-2025 可比，但 2017 回撤偏深、2026 仍为负，不替换 HK Path1 window winner、robust candidate、tracked/live/public payload。
- 本轮无 HK Path1 evict。HK 主线 `tracked_active` 未单独执行，原因是 A股 `refresh_active` 展开为 99 个 base ids 后已占用本轮长时预算并被中断；后续只做 HK artifact/public 同步，保证研究线不与 A股 winner 结论混用。
- 最终 guard focus 为 `risk_overlay_cost`。下一轮第一条命令建议继续在月频质量动量 + 周度 overlay 上加风险成本守门：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v47_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-27 19:24 CST）

- 上一轮 HK Path1 只做同步并把候选指向 `risk_overlay_cost`；本轮 HK 新增确认预算投给 Path4/5/6 扩展线，HK Path1 完成巡检、`tracked_active` 同步到 `2026-06-26`、artifact/public 同步和下一轮候选设计，没有新增 Path1 `--only-strategy-ids` 回测。
- 本轮同步命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_hkconnect_artifacts.py`。该同步修复了 public snapshot 对 HK preview as-of 过旧的拦截。
- HK Path1 window winner 维持：2017/2020 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32`，2023 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`，2025 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v9_repair`，2026 `hkconnect_path1_monthly_lowvol_weekly_overlay`；robust 仍为 `hkconnect_path1_monthly_lowvol_weekly_overlay_soft`。本轮无 HK Path1 evict，tracked/live/public 只有日期和 artifact 同步刷新。
- 最终 guard focus 为 `risk_overlay_cost`。下一轮第一条命令建议继续注册/确认双周质量动量风险成本修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-25 06:56 CST）

- 上一轮 Path1 只做同步并把候选指向 monthly-weekly overlay，本轮 HK 新增确认预算投给 Path4/5/6 扩展线；HK Path1 完成巡检、`tracked_active` 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- 本轮同步命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_hkconnect_artifacts.py`。执行时仍有离线缓存/交易日历回退警告，但退出码为 `0`。
- HK Path1 window winner、robust candidate、tracked/live/public payload 未切换，本轮无 HK Path1 evict。未回测原因：本轮 HK 新增实验预算优先给扩展线产生 Path4/5/6 新比较信息。
- 最终 guard focus 转为 `risk_overlay_cost`。下一轮第一条命令建议在双周质量/动量缓冲上叠加风险 overlay 与成本守门，修复 2026 负收益同时不放大 2017 回撤：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-24 19:22 CST）

- 上一轮 v43 双周缓冲只把 2026 修到接近持平，开局 focus 为 `risk_overlay_cost`。本轮 HK 新增确认预算投给 Path4/6/7 扩展线，HK Path1 只完成巡检、`tracked_active` 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- 本轮同步命令覆盖 HK tracked/top5/live active：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`；执行时仍有离线缓存/交易日历回退警告，但退出码为 `0`。`scripts/update_hkconnect_artifacts.py` 已刷新 tracked 与 Path1-3 图表。
- 同步后 HK Path1 window winner、robust candidate、tracked/live/public payload 未切换；本轮无 HK Path1 evict。未回测原因：本轮 HK 新增实验预算优先给扩展线的 Path4 流动性动量、Path6 低波高流动、Path7 杠铃组合三条可比较候选。
- 最终 guard 为 `pass`，下一轮 focus 转为 `monthly_weekly_overlay`。第一条命令应从双周缓冲转回月频选股 + 周度风险 overlay，重点修复 2026 负收益并控制 2017 回撤：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_v44_monthly_weekly_overlay`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-24 06:57 CST）

- 上一轮只设计 `v43_biweekly_buffer_repair`，本轮按 HK Path1 focus 实际五窗口确认该双周质量/动量缓冲候选，保持 HK 研究线独立于 A股 winner 结论。
- 本轮新增 strategy id：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair`。命令与 HK Path2/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v42_high_return_monthly,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff40_turnover0_exit56_v20_turnover_reduction`；执行时仍有离线缓存警告，但退出码为 `0`。
- v43 五窗口 CAGR `17.84% / 17.95% / 18.22% / 35.77% / -0.12%`，最大回撤 `-18.74% / -16.85% / -12.16% / -9.49% / -5.29%`。结论：2026 由上一轮负收益修到接近持平，但中长窗仍低于当前 Path1 robust，不替换 HK Path1 window winner、robust candidate、tracked/live/public payload。
- `scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；最终 guard 为 `pass`，HK 总候选 `425/425 complete`，Path1 无 evict。
- 最终 guard 将下一轮 focus 转到 `risk_overlay_cost`。第一条命令建议在双周缓冲基础上加入风险 overlay 与成本守门，而不是复跑普通 biweekly：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-23 17:21 CST）

- 上一轮 HK Path1 未新增回测，候选设计指向 monthly-weekly overlay；本轮 HK 新增预算投给 Path6/7 扩展线，HK Path1 完成巡检、artifact 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- `scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；最终 guard 为 `pass`，HK 总候选 `422/422 complete`，Path1 候选数 `101`，HK Path1 window winner、robust candidate、tracked/live/public payload 均未切换，本轮无 evict。
- 本轮候选设计映射最终 focus `biweekly_buffer`：下一轮应回到双周质量/动量缓冲，重点修复 2026 负收益，同时不放大 2017/2020 回撤。候选 ID：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair`。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_biweekly_buffer_repair`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-23 05:27 CST）

- 上一轮 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer` 五窗口确认后仍未修复 2026 负收益，本轮 HK 新增预算转投 Path4/5 扩展线；HK Path1 完成巡检、artifact 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- `scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；最终 guard 为 `pass`，HK 总候选 `420/420 complete`，Path1 window winner、robust candidate、tracked/live/public payload 均未切换，本轮无 evict。
- 本轮候选设计映射最终 focus `monthly_weekly_overlay`：下一轮应从双周缓冲转回月频选股 + 周度 overlay，并优先检查 2026 负收益与长窗回撤是否能同时改善。候选 ID：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_v43_monthly_weekly_overlay`。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_v43_monthly_weekly_overlay`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-22 17:34 CST）

- 上一轮只记录 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer`；本轮按 HK Path1 rotation 实际五窗口确认该双周质量/动量缓冲候选，保持 HK 研究线独立于 A股 winner 结论。
- 本轮新增 strategy id：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer`。命令与 HK Path2/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v41_high_return_monthly,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff38_turnover0_exit54_v19_turnover_reduction`；执行时港股 trade calendar 更新失败并回退本地缓存，退出码为 `0`。
- v42 五窗口 CAGR `16.70% / 18.24% / 18.42% / 35.01% / -1.65%`，最大回撤 `-19.66% / -17.66% / -11.67% / -9.65% / -4.40%`，换手 `3.95x / 3.85x / 4.02x / 4.75x / 4.92x`。结论：2017/2020/2023 风险收益可比，但 2026 仍为负，不替换 HK Path1 window winner、robust candidate 或 tracked/live/public payload。
- `scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；最终 guard 为 `pass`，HK 总候选 `415/415 complete`，Path1 候选数 `101`，本轮无 evict。
- 最终 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议继续双周质量/动量，但加风险成本修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v43_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-22 05:23 CST）

- 上一轮预留 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_risk_overlay_cost`；本轮 HK 新增预算投给 Path4-7 扩展四条，HK Path1 完成巡检、artifact 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 未切换；最终 guard 为 `pass`，HK 总候选 `411/411 complete`，Path1 候选数 `100`，本轮无 evict。
- 本轮候选设计映射最终 focus `biweekly_buffer`：下一轮应回到双周质量/动量缓冲，优先修复 2026 负收益，同时控制 2017 回撤，不把 HK Path4-7 的扩展候选并入 Path1 结论。候选 ID：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer`。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-21 17:29 CST）

- 上一轮预留 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_risk_overlay_cost`；本轮 HK 新增预算投给 Path4/5 扩展线，HK Path1 完成巡检、artifact 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 未切换；最终 guard 为 `pass`，HK 总候选 `411/411 complete`，Path1 候选数 `100`，本轮无 evict。
- 本轮候选设计继续映射最终 focus `risk_overlay_cost`：下一轮仍应回到双周质量/动量缓冲的风险和成本修复，目标是修复 2026 负收益，同时不牺牲 2020-2025 的月周 overlay 优势。候选 ID：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_risk_overlay_cost`。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-21 05:27 CST）

- 上一轮预留 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_v35_ytd_repair`，但本轮新增 HK 预算投给 Path6/7 扩展线；HK Path1 完成巡检、artifact 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 未切换；最终 guard 为 `pass`，HK 总候选 `409/409 complete`，Path1 候选数 `100`，本轮无 evict。
- 本轮候选设计映射最终 focus `risk_overlay_cost`：下一轮应回到双周质量/动量缓冲的风险和成本修复，目标是修复 2026 负收益，同时不牺牲 2020-2025 的月周 overlay 优势。候选 ID：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_risk_overlay_cost`。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-20 17:27 CST）

- 上一轮 v34 月周 overlay 仍未修复 2026 负收益；本轮 HK 新增预算优先投给 Path4/5 扩展线，HK Path1 完成巡检、artifact 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 未切换；最终 guard 为 `pass`，HK 总候选 `407/407 complete`，Path1 候选数 `100`，本轮无 evict。
- 本轮候选设计映射最终 focus `monthly_weekly_overlay`：下一轮建议回到月频选股 + 周度风险 overlay，但要修复 2017 深回撤和 2026 负收益。候选 ID：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_v35_ytd_repair`。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_v35_ytd_repair`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-20 05:28 CST）

- 上一轮候选设计为 `monthly_weekly_overlay` 成本守门；本轮新增并五窗口确认 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_v34_overlay_cost_guard`，保持 HK Path1 独立于 A股结论。
- 本轮命令类型为五窗口 `--only-strategy-ids` 增量确认，实际与 HK Path2/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_v34_overlay_cost_guard,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v40_elasticity_cost_control,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff36_turnover0_exit52_v18_turnover_reduction`。执行时港股 trade calendar 更新失败并回退本地缓存，退出码为 `0`。
- v34 五窗口 CAGR `18.54% / 22.87% / 23.77% / 34.80% / -10.08%`，最大回撤 `-29.15% / -11.70% / -10.57% / -10.86% / -10.77%`，换手 `3.40x / 3.30x / 3.20x / 3.40x / 3.99x`。结论：2020-2025 可比但 2017 回撤偏深、2026 仍为负，不替换 HK Path1 window winner、robust candidate 或 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；最终 guard 为 `pass`，HK 总候选 `405/405 complete`，无 evict。最终 focus 为 `risk_overlay_cost`，下一轮第一条命令建议回到双周质量动量的风险/成本修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-19 17:29 CST）

- 上一轮 HK Path1 v33 月周 overlay 成本修复仍未解决 2026 负收益；本轮新增预算投给 HK Path4-7 扩展线，HK Path1 完成巡检、artifact 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 未切换；最终 guard 为 `pass`，HK 总候选 `402/402 complete`，Path1 候选数 `99`，无 evict。
- 本轮候选设计回到 `monthly_weekly_overlay`：下一轮候选 ID 建议 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_v34_overlay_cost_guard`，改动点是保留 v33 月频选股 + 周度风险 overlay，但提高风险确认并控制换手，验收看 2026 是否转正且 2017 MaxDD 不劣于 v33。
- 下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_v34_overlay_cost_guard`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-19 05:26 CST）

- 上一轮 HK Path1 只做巡检并把下一步指向 monthly-weekly overlay 成本复核；本轮新增并五窗口确认 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_v33_cost_repair`，保持 HK Path1 独立于 A股结论。
- 本轮命令类型为五窗口 `--only-strategy-ids` 增量确认，实际与 HK Path2/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_v33_cost_repair,hkconnect_path2_theme_biweekly_breakout_cost_guard_v39_biweekly_repair,hkconnect_path3_stable_weekly_equal_buffered_cost_stress_v17_cost_guard`。执行时港股 trade calendar 更新失败并回退本地缓存，退出码为 `0`。
- v33 五窗口 CAGR `18.84% / 23.55% / 24.31% / 34.70% / -10.08%`，最大回撤 `-29.26% / -11.49% / -10.47% / -10.94% / -10.77%`，换手 `3.31x / 3.26x / 3.20x / 3.40x / 3.99x`。结论：2020-2025 可比但 2017 回撤偏深、2026 仍为负，不替换 HK Path1 window winner、robust candidate 或 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；最终 guard 为 `pass`，HK Path1 候选数 `99`，无 evict。最终 focus 为 `risk_overlay_cost`，下一轮第一条命令建议回到双周质量动量的风险/成本修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-18 17:16 CST）

- 上一轮 HK Path1 未新增，下一步候选为双周质量动量缓冲；本轮 HK 新增预算优先投给 Path4-7 扩展线，Path1 只完成巡检、artifact 同步和候选设计，没有新增 `--only-strategy-ids` 回测。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 未切换；HK 总 coverage 为 `395/395 complete`，Path1 仍为 `98` 个候选，本轮无 evict。
- 最终 focus 为 `monthly_weekly_overlay`。下一轮第一条命令建议回到月频选股 + 周度风险 overlay 的成本复核：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_v33_cost_repair`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-18 05:21 CST）

- 最终 guard 为 `pass`，HK 总候选 `391/391 complete`；本轮 HK Path1 完成巡检、tracked/artifact 同步和下一轮候选设计，没有新增 Path1 `--only-strategy-ids` 回测，继续独立于 A股 winner 结论。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 均未切换；robust 仍由既有双周低波/质量动量线维持。本轮无 HK Path1 evict。
- 本轮未回测原因：HK 新增预算优先投给 Path4-7 扩展四条 v23/v17；Path1 只记录 focus 映射和下一轮命令。
- 最终 focus 为 `biweekly_buffer`。下一轮第一条命令建议回到双周质量/动量缓冲，而不是继续 monthly-weekly overlay 同形：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v42_biweekly_buffer`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-17 18:02 CST）

- 最终 guard 为 `pass`，HK 总候选 `387/387 complete`；本轮新增并五窗口确认 HK Path1 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer`，保持沪港通研究线独立，不并入 A股 winner 结论。
- 本轮命令类型为五窗口 `--only-strategy-ids` 增量确认，实际与 HK Path2/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v37_high_return_monthly,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff30_turnover0_exit50_v15_turnover_reduction`。
- v41 五窗口 CAGR `17.14% / 18.66% / 18.49% / 31.34% / -6.41%`，最大回撤 `-20.26% / -18.57% / -11.67% / -9.65% / -5.47%`，换手 `4.08x / 3.99x / 4.11x / 4.94x / 5.04x`。结论：双周缓冲没有修复 2026 负收益，也弱于既有 Path1 robust，不替换 window winner、robust candidate 或 tracked payload。本轮无 HK Path1 evict。
- 最终 focus 为 `monthly_weekly_overlay`。下一轮第一条命令建议转回月周 overlay 的质量/低波组合：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_lowvol_v42_overlay_repair`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-17 05:20 CST）

- 最终 guard 为 `pass`，HK 总候选 `384/384 complete`；本轮 HK Path1 完成巡检、tracked 同步和下一轮候选设计，没有新增 Path1 `--only-strategy-ids` 回测，继续独立于 A股 winner 结论。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate、tracked/live/public payload 均未切换；robust 仍为 `hkconnect_path1_biweekly_lowvol`。本轮无 HK Path1 evict。
- 本轮未回测原因：HK 新增预算优先投给 Path4-7 扩展四条 v22；Path1 仅记录下一轮 focus 映射和第一条命令。
- 最终 focus 为 `biweekly_buffer`。下一轮第一条命令建议回到双周质量/动量缓冲，避免继续 monthly overlay 同形：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v41_biweekly_buffer`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-16 17:36 CST）

- 最终 guard 为 `pass`，HK 总候选 `380/380 complete`；上一轮预留的 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v40_risk_overlay_cost` 本轮已注册并五窗口确认，HK Path1 继续独立于 A股 winner 结论。
- 本轮命令类型为五窗口 `--only-strategy-ids` 增量确认，实际与 HK Path2/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-15 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v40_risk_overlay_cost,hkconnect_path2_theme_biweekly_quality_liquidity_breakout_v36_terminal_check,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff30_turnover0_exit48_v14_turnover_reduction`。执行时港股 trade calendar 更新失败并回退本地缓存，退出码为 `0`。
- v40 五窗口 CAGR 为 `17.12% / 18.59% / 18.44% / 31.68% / -6.35%`，最大回撤 `-19.64% / -18.78% / -12.13% / -9.95% / -6.08%`，换手 `4.21x / 4.14x / 4.25x / 5.07x / 5.28x`。结论：风险覆盖成本线没有修复 2026 负收益，也弱于既有 monthly/weekly overlay winner；不替换 HK Path1 window winner、robust candidate 或 tracked payload。本轮无 HK Path1 evict。
- 最终 focus 为 `monthly_weekly_overlay`。下一轮第一条命令建议转回月周 overlay 的质量/低波组合，而不是继续双周同形：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-15 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_lowvol_v41_overlay_repair`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-16 05:21 CST）

- 最终 guard 为 `pass`，HK 总候选 `377/377 complete`；本轮 HK 新增预算投给 Path4-7 扩展确认，HK Path1 完成巡检、tracked 同步和下一轮候选设计，没有新增 `--only-strategy-ids` 回测，继续独立于 A股 winner 结论。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 robust 仍为 `hkconnect_path1_biweekly_lowvol`，window winner、robust candidate、tracked/live/public payload 均未切换。本轮无 HK Path1 evict。
- 最终 focus 为 `risk_overlay_cost`。下一轮第一条命令建议回到双周质量/动量缓冲的风险成本修复，而不是继续 monthly overlay 同形：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v40_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-15 17:18 CST）

- 最终 guard 为 `pass`，HK 总候选 `373/373 complete`；本轮新增并五窗口确认 HK Path1 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_lowvol_mix_v39_ytd_risk_repair`，保持 HK Path1 独立研究线，不并入 A股 winner 结论。
- 本轮命令类型为五窗口 `--only-strategy-ids` 增量确认，实际与 HK Path2/3 合并执行。v39 五窗口 CAGR 为 `17.71% / 22.70% / 23.05% / 35.51% / -10.52%`，最大回撤 `-29.11% / -11.42% / -10.53% / -10.46% / -10.02%`，换手 `3.42x / 3.30x / 3.15x / 3.25x / 3.99x`。
- 结论：v39 的 2020-2025 仍可比，但 2026 更弱为负且 2017 回撤偏深，不替换 Path1 window winner、robust candidate 或 tracked payload；`scripts/update_hkconnect_artifacts.py` 后 robust 仍为 `hkconnect_path1_biweekly_lowvol`。本轮无 HK Path1 evict。
- 最终 focus 为 `biweekly_buffer`。下一轮第一条命令建议转回双周质量/动量缓冲，而不是继续 monthly overlay 同形：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v40_biweekly_buffer`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-15 05:39 CST）

- 最终 guard 为 `pass`，HK 总候选 `370/370 complete`；本轮没有新增 HK Path1 `--only-strategy-ids` 回测，预算投给 HK Path4-7 扩展确认。HK Path1 保持独立研究线，不并入 A股 winner 结论。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 robust 仍为 `hkconnect_path1_biweekly_lowvol`，window winner、robust candidate、tracked/live/public payload 均未切换。本轮无 HK Path1 evict。
- 本轮候选池巡检显示上一轮 v38 monthly overlay 仍未修复 2026，最终 focus 回到 `monthly_weekly_overlay`。下一轮第一条命令建议注册一个更明确的质量/低波月周 overlay 2026 修复，而不是复跑 v38：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_lowvol_mix_v39_ytd_risk_repair`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-14 17:25 CST）

- 开局 guard 为 `pass`，HK Path1 coverage 完整；本轮注册并五窗口确认 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_lowvol_mix_v38_monthly_overlay`，保持 HK Path1 独立研究线，不并入 A股 winner 结论。
- 本轮命令类型为五窗口 `--only-strategy-ids` 增量确认，实际与 HK Path2/3 合并执行。v38 五窗口 CAGR 为 `17.98% / 23.29% / 24.22% / 33.16% / -8.02%`，最大回撤 `-29.05% / -10.96% / -10.91% / -10.65% / -10.15%`，换手 `3.48x / 3.37x / 3.22x / 3.39x / 4.06x`。
- 结论：v38 的 2020-2025 有可比性，但 2017 回撤偏深且 2026 仍为负，不替换 Path1 window winner、robust candidate 或 tracked payload；`scripts/update_hkconnect_artifacts.py` 后 robust 仍为 `hkconnect_path1_biweekly_lowvol`。本轮无 HK Path1 evict。
- 中段 guard focus 为 `biweekly_buffer`。下一轮第一条命令建议转回双周质量动量缓冲，而不是继续 monthly overlay 同形：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v39_biweekly_buffer`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-14 05:29 CST）

- 最终 guard 为 `pass`，HK 总候选 `363/363 complete`；本轮按上一轮计划注册并确认 lowvol + risk overlay 的 monthly-weekly 2026 修复候选，保持 HK Path1 独立研究线，不并入 A股 winner 结论。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_risk_overlay_cost_v37_2026_repair`。命令类型为五窗口 `--only-strategy-ids` 增量确认，实际命令与 HK Path5/6/7 合并：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_risk_overlay_cost_v37_2026_repair,hkconnect_path5_breakout_retest_biweekly_quality_confirm_v13_ytd_guard,hkconnect_path6_lowvol_liquid_biweekly_quality_ytd_guard_v19,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_ytd_guard_v19`。
- `v37_2026_repair` 五窗口 CAGR 为 `18.18% / 21.35% / 23.91% / 31.09% / -9.94%`，最大回撤为 `-19.47% / -10.94% / -9.89% / -9.69% / -7.94%`，换手为 `3.39x / 3.31x / 3.07x / 3.32x / 4.05x`。结论：2020-2025 有可比性且回撤浅于部分旧 monthly-weekly 线，但 2026 更弱为负，不替换 Path1 window winner、robust candidate 或 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 robust 仍为 `hkconnect_path1_biweekly_lowvol`，本轮无 HK Path1 evict。最终 focus 为 `monthly_weekly_overlay`，下一轮第一条命令建议停止继续单纯 lowvol/risk overlay，转向质量 + 低波混合月周 overlay：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_lowvol_mix_v38_monthly_overlay`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-13 17:30 CST）

- 最终 guard 为 `pass`，HK 总候选 `359/359 complete`；本轮按上一轮计划注册并确认 monthly-weekly overlay 的 2026 修复候选，保持 HK Path1 独立研究线，不并入 A股 winner 结论。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_cost_guard_exit32_v36_2026_repair`。命令类型为五窗口 `--only-strategy-ids` 增量确认，实际命令与 HK Path2/3/4 合并：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_cost_guard_exit32_v36_2026_repair,hkconnect_path2_equal_elastic_monthly_cost_guard_v33_elasticity_cost_repair,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff34_turnover1_exit44_v11_defensive_repair,hkconnect_path4_quality_momentum_monthly_lowdraw_v19_signal_quality_repair`。
- `v36_2026_repair` 五窗口 CAGR 为 `18.52% / 23.93% / 26.19% / 36.79% / -8.94%`，最大回撤为 `-27.61% / -10.82% / -8.86% / -8.97% / -9.04%`，换手为 `3.55x / 3.45x / 3.27x / 3.42x / 4.29x`。结论：2023/2025 仍可比，但 2026 继续为负，2017 回撤偏深，不替换 Path1 window winner、robust candidate 或 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 robust 仍为 `hkconnect_path1_biweekly_lowvol`，本轮无 HK Path1 evict。最终 focus 为 `risk_overlay_cost`，下一轮第一条命令建议注册 lowvol + risk overlay 的 monthly-weekly 成本修复，而不是继续普通 exit32 同形：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_risk_overlay_cost_v37_2026_repair`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-13 05:09 CST）

- 最终 guard 开局为 `pass`，HK 总候选可比；本轮按上一轮 `risk_overlay_cost` 预留 ID 执行五窗口增量确认，保持 HK Path1 独立研究线，不并入 A股 winner 结论。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v35_risk_overlay_cost`。命令类型为 `--only-strategy-ids` 增量确认，实际命令与 HK Path2/3/5/6/7 合并：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v35_risk_overlay_cost,hkconnect_path2_theme_biweekly_cost_guard_v32_breakout_repair,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover1_exit42_v10_ytd_repair,hkconnect_path5_pullback_continuation_monthly_quality_retest_v12_definition_guard,hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v18_ytd_repair,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v18_sleeve_balance`。
- `v35_risk_overlay_cost` 五窗口 CAGR 为 `16.71% / 18.30% / 18.65% / 29.78% / -6.24%`，最大回撤为 `-19.89% / -18.98% / -11.15% / -10.12% / -5.57%`，换手为 `4.33x / 4.25x / 4.32x / 5.13x / 5.31x`。结论：回撤仍浅但 2026 负收益未修复，中长窗低于 Path1 robust，不替换 window winner、robust candidate 或 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 robust 仍为 `hkconnect_path1_biweekly_lowvol`，本轮无 HK Path1 evict。最终 focus 仍在 rotate，下一轮第一条命令建议回到 `monthly_weekly_overlay` 的 2026 修复，而不是继续普通 biweekly：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_cost_guard_exit32_v36_2026_repair`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-12 05:28 CST）

- 最终 guard 为 `pass`，HK 总候选 `349/349 complete`；HK Path1 保持独立研究线，不并入 A股 winner 结论。上一轮 v33 risk overlay cost guard 未修复 2026，本轮按 `risk_overlay_cost` 注册并确认低波/ytd 修复版 `v34`。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v34_lowvol_ytd_repair`。命令类型为五窗口 `--only-strategy-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- `v34_lowvol_ytd_repair` 五窗口 CAGR 为 `17.49% / 19.43% / 21.47% / 27.01% / -7.02%`，最大回撤为 `-19.83% / -14.85% / -8.83% / -7.14% / -4.99%`，Sharpe 为 `1.04 / 1.07 / 1.22 / 1.50 / -0.63`，换手为 `4.39x / 4.31x / 4.38x / 5.16x / 5.11x`。结论：回撤较浅但 2026 仍为负，且中长窗低于 robust，不替换 Path1 window winner、robust candidate 或 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 robust 仍为 `hkconnect_path1_biweekly_lowvol`；本轮无 HK Path1 evict。最终 guard focus 继续为 `risk_overlay_cost`。
- 下一轮第一条命令建议不要继续普通 lowvol 小步微调，注册更明确的风险 overlay/cost 对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v35_risk_overlay_cost`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-07 23:50 CST）

- 针对“为什么没有不断迭代”做修正：上一轮 HK Path1 只做巡检而未新增回测，原因是当轮预算被 HK Path3/4/6/7 与 A股 Path1/3/4 占用，不是 Path1 停止研究。本轮把上一轮预留 ID 注册并实际五窗口确认。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v26_2026_balance`。命令类型为五窗口 `--only-strategy-ids` 增量确认，命令为：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v26_2026_balance,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v24_2023_2026_balance`。
- `v26_2026_balance` 五窗口 CAGR 为 `18.35% / 23.21% / 21.57% / 34.64% / -6.82%`，最大回撤为 `-28.85% / -12.37% / -12.37% / -12.37% / -9.06%`，Sharpe 为 `1.07 / 1.22 / 1.20 / 1.41 / -0.17`，换手为 `3.39x / 3.40x / 3.39x / 3.59x / 4.29x`。结论：仍未修复 2026，且 2017 回撤偏深，不替换 Path1 window winner、robust candidate 或 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 robust 仍为 `hkconnect_path1_biweekly_lowvol`，window winners 与 tracked payload 不变；本轮无 HK Path1 evict。
- 下一轮 focus：停止继续 `exit32/exit34` 同形 monthly-weekly 微调，优先执行已注册的质量/动量双周缓冲对照：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`。

## 本轮执行计划（2026-06-07 16:06 CST）

- 最终 guard 为 `pass`，HK 总候选 `278/278 complete`，HK Path1 当前 `77` 个候选完整。本轮没有执行 HK Path1 回测，预算投给 HK Path3/4/6/7 与 A股 Path1/3/4；HK Path1 保持独立研究线，不并入 A股 winner 结论。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 window winner、robust candidate 和 tracked payload 未切换；robust 仍为 `hkconnect_path1_biweekly_lowvol`，window winners 仍由旧 monthly-weekly overlay 与 biweekly lowvol 分担。本轮没有 HK Path1 evict。
- 本轮候选池设计：最终 guard focus 为 `monthly_weekly_overlay`，上一轮 `v25_2026_repair` 仍未修复 2026，因此下一条只允许一次 monthly-weekly overlay 的不同风险暴露对照，候选 id 预留 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v26_2026_balance`。
- 下一轮第一条命令：`.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v26_2026_balance`；若未注册，先在 HK Path1 variants 中注册。`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24` 保留为 backup。

## 本轮执行计划（2026-06-07 04:26 CST）

- 最终 guard 为 `pass`，HK 总候选 `274/274 complete`，HK Path1 当前 `77` 个候选完整。上一轮未跑的 monthly-weekly overlay 修复线本轮已执行，保持 HK 独立研究线，不并入 A股 winner 结论。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair`。命令类型为五窗口 `--only-strategy-ids` 增量确认，实际 HK 命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v23_2023_restore,hkconnect_path4_quality_momentum_monthly_2026_repair_v8`。
- `v25_2026_repair` 五窗口 CAGR 为 `18.39% / 23.18% / 21.65% / 34.75% / -6.82%`，最大回撤为 `-28.62% / -12.28% / -12.28% / -12.28% / -9.06%`，Sharpe 为 `1.07 / 1.22 / 1.20 / 1.41 / -0.17`，换手为 `3.38x / 3.37x / 3.34x / 3.60x / 4.29x`。结论：仍未修复 2026 负收益，2017 回撤偏深，不替换 Path1 window winner、robust candidate 或 tracked payload。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 tracked 仍为 `hkconnect_path1_biweekly_lowvol` robust；本轮没有 HK Path1 evict。最终 guard 将下一轮 focus 推到 `biweekly_buffer`。
- 下一轮第一条命令建议回到普通双周质量/动量缓冲，而不是继续 monthly-weekly 同形修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`；若未注册，先在 HK Path1 variants 中注册。

## 本轮执行计划（2026-06-06 16:17 CST）

- 最终 guard 为 `pass`，HK Path1 当前 `76` 个候选完整；本轮没有执行 HK Path1 回测，预算投给 HK Path2/3/4/6/7 与 A股 Path1-4。上一轮未跑的 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24` 继续保留为普通 biweekly backup，但最终 focus 已切到 `risk_overlay_cost`。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 window winner、robust candidate 和 tracked payload 未切换；robust 仍为 `hkconnect_path1_biweekly_lowvol`，window winners 仍由旧 monthly-weekly overlay 与 biweekly lowvol 分担。本轮没有 HK Path1 evict，也没有 public/live 的 Path1 winner 变化。
- 下一轮第一条命令应优先确认 monthly-weekly overlay 的风险/成本修复，而不是本轮未跑的普通 biweekly：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair`；若未注册，先在 HK Path1 variants 中注册。`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24` 保留为 backup。

## 本轮执行计划（2026-06-06 10:28 CST）

- 最终 guard 为 `pass`，HK Path1 当前 `76` 个候选完整；本轮没有执行 HK Path1 回测，预算投给 HK Path4/6/7 与 A股 Path1-4。上一轮未跑的 monthly-weekly overlay 修复线继续保留为第一待确认候选。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 window winner、robust candidate 和 tracked payload 未切换；robust 仍为 `hkconnect_path1_biweekly_lowvol`，window winners 仍由旧 monthly-weekly overlay 与 biweekly lowvol 分担。本轮没有 HK Path1 evict，也没有 public/live 的 Path1 winner 变化。
- 最终 rotation focus 为 `biweekly_buffer`。下一轮第一条命令改回普通双周质量/动量缓冲，而不是继续 monthly-weekly 同形修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`；若未注册，先在 HK Path1 variants 中注册。`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair` 保留为 backup。

## 本轮执行计划（2026-06-06 04:23 CST）

- 最终 guard 为 `pass`，HK 总 coverage 为 `263/263 complete`，HK Path1 当前 `76` 个候选完整。本轮没有执行 HK Path1 回测；预算投给 HK Path4/6/7 与 A股 Path2/3/4。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 window winner、robust candidate 和 tracked payload 未切换；robust 仍为 `hkconnect_path1_biweekly_lowvol`，monthly-weekly overlay 修复线继续作为主对照池。上一轮未跑的 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair` 仍是当前 focus 的第一候选。
- 最终 rotation focus 为 `monthly_weekly_overlay`。下一轮第一条命令为：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair`；若未注册，先在 HK Path1 variants 中注册。`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24` 保留为 biweekly backup，不作为下一轮第一优先级。

## 本轮执行计划（2026-06-05 22:21 CST）

- 最终 guard 为 `pass`，HK 总 coverage 为 `260/260 complete`，HK Path1 当前 `76` 个候选完整。本轮没有执行 HK Path1 回测；预算投给 HK Path4/5/6 与 A股 Path1-4。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 window winner、robust candidate 和 tracked payload 未切换；robust 仍为 `hkconnect_path1_biweekly_lowvol`，普通 biweekly buffer 与 monthly-weekly overlay 修复线继续作为对照池。
- 本轮候选设计保留上一轮未跑的 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`，但最终 guard 后 rotation focus 推进到 `risk_overlay_cost`。下一轮第一条命令应先确认 monthly-weekly overlay 的风险/成本修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair`；若未注册，先在 Path1 variants 中注册。`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24` 保留为 biweekly backup，不作为下一轮第一优先级。
- 本轮未触发 HK Path1 evict；没有 public/live 的 Path1 winner 变化。

## 本轮执行计划（2026-06-05 10:22 CST）

- 最终 guard 为 `pass`，HK 总 coverage 为 `257/257 complete`，HK Path1 当前 `76` 个候选完整。本轮只注册/设计 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`，没有执行 HK Path1 回测；预算优先投给 HK Path3/4/7 与 A股 Path1-4。
- `scripts/update_hkconnect_artifacts.py` 后 Path1 window winner、robust candidate 和 tracked payload 未切换；robust 仍为 `hkconnect_path1_biweekly_lowvol`，window winners 仍由 monthly-weekly overlay 与旧 biweekly lowvol 分担。
- 巡检结论：普通 biweekly buffer 连续弱，上一轮计划的 v24 仍适合作为“质量/动量双周缓冲”单点确认，但本轮未跑，不能写入策略结论或 public/live 变更。
- 最终 guard 将下一轮 focus 推到 `monthly_weekly_overlay`。下一轮第一条命令应先回到 monthly-weekly overlay 的 2026 修复，而不是继续普通 biweekly：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v25_2026_repair`；若未注册，先在 Path1 variants 中注册，已注册的 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24` 保留为后续 biweekly 对照，不改跑 HK 全量。

## 本轮执行计划（2026-06-05 04:11 CST）

- 最新 guard 为 `pass`，HK coverage 为 `254/254 complete`，HK Path1 当前 `76` 个候选完整。本轮没有新增 HK Path1 回测，预算优先投给 HK Path3/4/6 与 A股 Path3/4；`scripts/update_hkconnect_artifacts.py` 后 Path1 window winner、robust candidate 和 tracked payload 未切换。
- 巡检结论：上一轮 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair` 仍未修复 2026，Path1 robust 继续由 monthly-weekly overlay 旧线占据；普通 biweekly buffer 连续弱，不能只靠 exit/risk-off 微调。
- 最新 rotation focus 为 `biweekly_buffer`。下一轮第一条命令建议用质量/动量双周缓冲修复 2026，而不是继续同形 monthly-weekly：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`；若未注册，先在 Path1 variants 中注册。

## 本轮执行计划（2026-06-04 16:16 CST）

- 开局 guard 为 `pass`，HK coverage 无 blocking。当前轮复跑确认 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair`，与 HK Path2/3/5 合并执行五窗口 `--only-strategy-ids`，没有新增 Path1 id。
- 复跑后 `v23_cost_repair` 五窗口 CAGR 为 `18.70% / 23.68% / 21.84% / 34.75% / -7.11%`，最大回撤为 `-28.41% / -12.28% / -12.28% / -12.28% / -9.10%`，换手为 `3.39x / 3.34x / 3.33x / 3.60x / 4.30x`。2026 仍为负，2017 回撤偏深，不替换 HK Path1 window winner 或 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path1 tracked payload 未切换。最终 guard 将下一轮 focus 轮到 `biweekly_buffer`；第一条命令建议从低波/质量双周缓冲修复 2026，而不是继续 monthly-weekly risk-off 单参数：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`；若未注册，先在 Path1 variants 中注册。

## 本轮执行计划（2026-06-04 10:16 CST）

- 开局 guard 为 `pass`，HK blocking 为 0；上一轮 Path1 的 v22 仍没有修复 2026，本轮按 `monthly_weekly_overlay` 继续做浅 risk-off + exit38 的成本修复，而不是回到普通双周缓冲线。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair`。实际 HK 合并命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair,hkconnect_path2_equal_elastic_monthly_cost_guard_v17_repair,hkconnect_path6_large_liquid_core_biweekly_liquidity_mix_v3,hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v4`。
- `v23_cost_repair` 五窗口 CAGR 为 `18.70% / 23.68% / 21.84% / 34.75% / -7.11%`，最大回撤为 `-28.41% / -12.28% / -12.28% / -12.28% / -9.10%`。它没有修复 2026，且 2023/2025 弱于现有 monthly-weekly robust；`scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate 和 tracked payload 未切换。
- 下一轮 focus 仍是 `monthly_weekly_overlay`，但不要继续只降低 risk-off。第一条命令建议转向低波/质量过滤的 2026 drawdown repair：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_riskoff24_exit38_v24_2026_repair`；若未注册，先在 Path1 variants 中注册。

## 本轮执行计划（2026-06-03 22:20 CST）

- 开局 guard 为 `pass`，HK coverage 在本轮代码注册后通过五窗口增量回测补到 `237/237 complete`。Path1 本轮新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit34_v21_ytd_guard`，目标是在 monthly-weekly overlay 上加入低波与 ytd 防守，修复 2026 观察窗。
- 本轮 HK 合并增量命令为：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit34_v21_ytd_guard,hkconnect_path2_inverse_elastic_monthly_cost_guard_v16_terminal,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover5_exit42_coststress_ytd_guard,hkconnect_path4_quality_momentum_monthly_ytd_guard,hkconnect_path6_large_liquid_core_monthly_ytd_guard,hkconnect_path7_barbell_quality_growth_biweekly_defensive_v2`。
- `v21_ytd_guard` 五窗口 CAGR 为 `17.81% / 21.92% / 28.50% / 28.87% / -4.83%`，最大回撤为 `-21.66% / -10.09% / -9.08% / -8.80% / -7.56%`，换手为 `3.53x / 3.40x / 3.18x / 3.56x / 4.33x`。
- 结论：低波 ytd guard 压住了中短窗回撤，但 2017/2020/2025 收益弱于 monthly-weekly robust，2026 仍为负；`scripts/update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate 和 tracked payload 未切换。下一轮 focus 为 `monthly_weekly_overlay`，第一条命令建议停止继续低波同形修复，改测浅 risk-off 或 2026 drawdown repair：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_drawdown_next_id>`。

## 本轮执行计划（2026-06-03 14:34 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，HK coverage 为 `226/226 complete`；本轮按 `biweekly_buffer` 新增 `hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit34_v20_buffer`，用于检验普通双周缓冲线在更宽持仓和较低单票上限下，是否能修复 2026 且保住长窗。
- 本轮 HK 合并增量命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit34_v20_buffer,hkconnect_path2_theme_biweekly_cost_guard_v21_breakout_repair,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit42_coststress_2026_repair`。
- `v20_buffer` 五窗口 CAGR 为 `21.02% / 20.83% / 19.35% / 27.31% / -16.14%`，最大回撤为 `-21.12% / -21.12% / -14.50% / -14.50% / -8.23%`，换手为 `5.51x / 5.36x / 5.53x / 7.14x / 6.47x`。
- 结论：该双周缓冲候选没有修复 2026，且 2023/2025 明显弱于 monthly-weekly overlay robust；`scripts/update_hkconnect_artifacts.py` 后 HK Path 1 window winner、robust candidate 和 tracked payload 均未切换。候选池从 `226` 扩到 `229`，最终 guard 仍为 `pass`。
- 下一轮 focus 仍显示 `hkconnect_path1 -> biweekly_buffer`，但普通双周等权缓冲连续弱，下一轮不要继续同形 `exit/risk_off` 微调；第一候选建议转成双周多因子质量动量线，例如 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v21`，先复用动量、低波、流动性字段做新信号家族，而不是只调整出场阈值。

## 本轮执行计划（2026-06-02 16:20 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `v16_ytd_balance` 仍未修复 2026，最终 rotation 转向 `risk_overlay_cost`。本轮按该 focus 回到真正双周缓冲线，新增低波+浅 risk-off 的 `exit28_v17_repair`，目标是在不继续扩 monthly-weekly overlay 同形参数的前提下观察 2026 修复和长窗回撤。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit28_v17_repair`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit28_v17_repair,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v19_2023_restore,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_riskoff45_turnover8_exit42`。
- `v17_repair` 五窗口 CAGR 为 `17.15% / 18.51% / 31.06% / 36.91% / -0.52%`，最大回撤为 `-20.65% / -18.95% / -10.19% / -6.91% / -4.44%`，换手为 `5.75x / 5.47x / 5.07x / 6.65x / 7.04x`。它改善 2026 亏损幅度和 2025 回撤，但长窗收益明显低于 monthly-weekly robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracks 未切换，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；`tracked_winners_hkconnect.json` 的 strategies payload 纳入本轮 v17，三张 HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最新 guard 为 `pass`，下一轮 focus 为 `risk_overlay_cost`。第一条命令建议不要继续普通双周低波线，回到 robust 的 monthly-weekly overlay 做浅 risk-off 或 2026 drawdown repair：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-06-02 13:49 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `v15_2026_repair` 仍没修复 2026 负收益，最终 rotation 转向 `biweekly_buffer`。本轮没有回到普通双周低收益线，而是在 monthly-weekly overlay 上把 `exit32` 与轻成本守门组合做 `v16_ytd_balance`，目标是观察能否保留 2025 winner 水平并减少 2026 年内亏损。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v16_ytd_balance`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v16_ytd_balance,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v18_2020_guard,hkconnect_path3_theme_fast_weekly_defensive_exit62_turnover2_cost_guard`。
- `v16_ytd_balance` 五窗口 CAGR 为 `20.13% / 26.02% / 27.03% / 46.50% / -8.06%`，最大回撤为 `-28.39% / -12.96% / -11.82% / -11.82% / -10.70%`，换手为 `3.65x / 3.61x / 3.46x / 3.57x / 4.10x`。它与 v15 的 2025/2026 结果同形，2017/2020/2023 仍低于 robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracks 未切换，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；但 `tracked_winners_hkconnect.json` 的 strategies payload 纳入了本轮 v16，三张 HK comparison 图和 public/live snapshot 已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 中 HK Path 1 focus 为 `biweekly_buffer`。第一条命令建议做一次真正的双周缓冲对照，但不要扩成大量同形参数；优先测试低波/浅 risk-off 的双周修复能否改善 2026，同时保留 2017 回撤优势：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-06-02 04:20 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `exit28_v14_2026_repair` 切成 HK Path 1 `since_2025_01` winner，但 2026 仍为负。本轮按 `monthly_weekly_overlay` 在同一 `exit28` 上加轻现金守门，测试是否能保住 2025 winner 并修复 2026。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit28_v15_2026_repair`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit28_v15_2026_repair,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v17_2023_break30,hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit68_hardcap`。
- `v15_2026_repair` 五窗口 CAGR 为 `19.03% / 24.46% / 26.19% / 46.50% / -8.06%`，最大回撤为 `-29.53% / -13.25% / -11.82% / -11.82% / -10.70%`，换手为 `3.84x / 3.82x / 3.60x / 3.57x / 4.10x`。它没有修复 2026，且 2017/2020/2023 不及 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 发生变化：`since_2025_01` winner 切换为本轮 `v15_2026_repair`；robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。HK comparison 图、live/public snapshot 已刷新；候选池未触发 HK explore cap evict。
- 最终 guard 中 HK Path 1 为 `continue / monthly_weekly_overlay`。第一条命令建议不要继续同形 cashguard，改测低波或浅 risk-off 对 `exit28/30` 的 2026 修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-06-01 22:30 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `biweekly_equal_buffered_soft_cost_guard_exit30_v12_repair` 说明普通双周修复长窗收益不足且 2026 仍负。本轮按 `monthly_weekly_overlay` 回到 monthly + weekly overlay，在 `exit28` 上加 soft cost guard，目标是修复 2025 winner，同时观察 2026 是否能转正。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit28_v14_2026_repair`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit28_v14_2026_repair,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v16_2023_lift,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover1_exit44_hardcap`。
- `exit28_v14_2026_repair` 五窗口 CAGR 为 `20.06% / 25.94% / 27.04% / 46.50% / -8.06%`，最大回撤为 `-28.58% / -13.04% / -11.82% / -11.82% / -10.70%`，换手为 `3.64x / 3.59x / 3.44x / 3.57x / 4.10x`。它成为 HK Path 1 `since_2025_01` window winner，但 2017/2020/2023 不及 robust，且 2026 仍为负。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 发生变化：`since_2025_01` winner 切换为本轮 `exit28_v14_2026_repair`；robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。HK comparison 图、live/public snapshot 已刷新；候选池未触发 HK explore cap evict。
- 下一轮 focus 仍为 `monthly_weekly_overlay`。第一条命令建议继续修 2026，但不能只收 exit；优先测试轻现金/浅 risk-off 对 v14 的 2026 修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_v15_2026_repair_id>`。

## 本轮执行计划（2026-06-01 10:27 CST）

- 开局与收尾 guard 均为 `pass` 且 HK coverage complete；上一轮 `exit30_v11_repair` 低波 monthly overlay 压回撤但仍未修复 2026。本轮按 `biweekly_buffer` 回到双周等权缓冲线，新增轻成本 `exit30_v12_repair`，目标是验证不加低波过滤时是否能恢复长窗并观察 2026 修复。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit30_v12_repair`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit30_v12_repair`。
- `v12_repair` 五窗口 CAGR 为 `21.13% / 21.66% / 20.45% / 27.51% / -13.62%`，最大回撤为 `-21.68% / -21.68% / -16.91% / -16.91% / -7.24%`，换手为 `5.69x / 5.63x / 5.59x / 7.44x / 6.92x`。它略接近双周成本线长窗，但 2023/2025 明显弱于 monthly-weekly overlay robust，且 2026 仍为负，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 window winner/robust/tracked 未被本轮候选替换，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；HK comparison 图刷新。候选池未触发 HK explore cap evict。
- 下一轮 focus 为 `risk_overlay_cost`。第一条命令建议停止普通双周 `exit30` 修复，回到 monthly-weekly overlay 做成本/风险叠加的 2026 修复，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30_v13_risk_overlay`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-06-01 04:18 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `exit32_v10_repair` 仍未修复 2026 负收益。本轮按 `biweekly_buffer/monthly_weekly_overlay` 的交叉验证思路，新增低波 weekly overlay + 轻成本 `exit30_v11_repair`，目标是用低波过滤修复 2026，同时保留 2023 收益。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30_v11_repair`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30_v11_repair,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v14_signal_guard,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover2_exit44`。
- `exit30_v11_repair` 五窗口 CAGR 为 `18.36% / 23.68% / 31.29% / 30.34% / -1.15%`，最大回撤为 `-22.22% / -11.47% / -10.34% / -9.91% / -9.18%`，换手为 `3.59x / 3.51x / 3.24x / 3.74x / 4.51x`。低波版本压住回撤但牺牲长窗和 2025，仍未修复 2026，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 robust/tracked winner 未被本轮候选替换，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；HK comparison 图刷新。候选池未触发 HK explore cap evict。
- 下一轮 focus 为 `biweekly_buffer`。第一条命令建议停止同形 monthly-lowvol 修复，回到双周缓冲但保留 2026 修复约束，例如 `hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit30_v12_repair`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-31 22:26 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `v9_repair` 仍没修复 2026 负收益，只把 2025 winner 推到同形高位。本轮按 `monthly_weekly_overlay` 继续修 2026，改用 `exit32_v10_repair`，仍作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v10_repair`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v10_repair,hkconnect_path2_inverse_elastic_monthly_cost_guard_v13_terminal,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover1_exit46`。
- `exit32_v10_repair` 五窗口 CAGR 为 `21.98% / 29.35% / 32.39% / 52.56% / -0.50%`，最大回撤为 `-26.71% / -12.85% / -10.86% / -10.86% / -9.29%`，换手为 `3.63x / 3.59x / 3.38x / 3.61x / 4.19x`。它继续维持 2025 强度但仍未修复 2026，且 2017 回撤深于 robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 robust/tracked payload 无实质改写，HK comparison 图刷新；候选池未触发 HK explore cap evict。
- 下一轮 focus 若继续停在 `monthly_weekly_overlay`，第一条命令建议停止同形 exit32/34 微调，改测更浅 risk-off 或低波 overlay 对 2026 的修复：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_overlay_2026_repair_next_id>`。

## 本轮执行计划（2026-05-31 16:20 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `soft_cost_guard_exit34_v8_drawdown_guard` 把 `since_2025` winner 推高但 2026 转负。本轮继续沿 `monthly_weekly_overlay` 修复 2026，新增轻现金守门 `v9_repair`，仍作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v9_repair`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v9_repair`。
- `v9_repair` 五窗口 CAGR 为 `20.72% / 27.79% / 31.22% / 52.56% / -0.50%`，最大回撤为 `-28.99% / -12.84% / -10.87% / -10.87% / -9.29%`，换手为 `3.93x / 3.96x / 3.62x / 3.61x / 4.19x`。它没有修复 2026 负收益，且 2017 回撤比 robust 更深，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 有同步变化：`since_2025_01` winner 从上一轮 v8/drawdown guard 切到本轮 `v9_repair`，但两者同形且 2026 仍为 `-0.50%`，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。HK comparison 图已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK Path 1 rotation 因上一轮 winner 变化仍为 `continue / monthly_weekly_overlay`。第一条命令建议继续修 2026，但下一次不要再用同形 cashguard，改为更浅 drawdown guard 或 exit32/34 组合：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-31 10:26 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 focus 为 `risk_overlay_cost`，本轮回到 monthly-weekly overlay，在 `soft_exit34` 邻域增加 cost guard 与 drawdown guard，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v8_drawdown_guard`。实际 HK 增量命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v8_drawdown_guard,hkconnect_path2_inverse_elastic_monthly_cost_guard_v12_terminal,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover1_exit44`。
- `soft_cost_guard_exit34_v8_drawdown_guard` 五窗口 CAGR 为 `22.02% / 29.48% / 32.40% / 52.56% / -0.50%`，最大回撤为 `-26.82% / -12.81% / -10.87% / -10.87% / -9.29%`，换手为 `3.62x / 3.59x / 3.39x / 3.61x / 4.19x`。它把 HK Path 1 的 `since_2025` window winner 推到 `52.56%`，但 2017 回撤变深且 2026 转负，不替换 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 发生变化：`since_2025_01` winner 为本轮 v8 drawdown guard；robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。HK comparison 图已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `190` 完整，HK Path 1 rotation 因 winner 变化重置为 `continue / monthly_weekly_overlay`。第一条命令建议继续围绕 monthly-weekly overlay 修复 2026 负收益，优先用轻现金或更浅 drawdown guard 而不是回到双周低收益线：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-31 04:21 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮建议回到双周缓冲线，本轮新增 `hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit34_v7`，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit34_v7`。实际 HK 增量命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit34_v7`。
- `biweekly_equal_buffered_soft_cost_guard_exit34_v7` 五窗口 CAGR 为 `21.14% / 21.71% / 20.21% / 25.98% / -13.96%`，最大回撤为 `-21.23% / -21.23% / -17.14% / -17.14% / -7.24%`，换手为 `5.78x / 5.73x / 5.67x / 7.52x / 6.93x`。它略好于 v5，但 2026 仍为负且长窗收益不及 monthly-weekly overlay robust，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `187/187 complete`，下一轮 focus 轮换为 `risk_overlay_cost`。第一条命令建议回到 monthly-weekly overlay 并加 drawdown/cost guard，而不是继续双周线，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v8_drawdown_guard`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-30 22:20 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮建议回到 monthly-weekly overlay 的轻成本 `exit34`，本轮新增 `soft_cost_guard_exit34_v6`，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v6`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v6,hkconnect_path2_inverse_elastic_monthly_cost_guard_v11_terminal,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover2_exit44`。
- `soft_cost_guard_exit34_v6` 五窗口 CAGR 为 `23.78% / 31.06% / 32.20% / 42.91% / 2.13%`，最大回撤为 `-24.56% / -12.19% / -11.58% / -11.58% / -8.44%`，换手为 `3.70x / 3.72x / 3.39x / 3.59x / 4.23x`。它保持 2026 小幅正收益，但 2017 回撤和长窗收益仍不及 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `184/184 complete`，下一轮 focus 轮换为 `biweekly_buffer`。第一条命令建议回到双周缓冲线，测试是否能少损长窗并保留 2026 正收益，例如 `hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit34_v7`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-30 16:22 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `soft_cost_guard_exit32_v4` 长窗仍低于 monthly-weekly overlay robust。本轮按 `biweekly_buffer/risk_overlay_cost` 回到双周等权缓冲，新增无低波的轻成本 `exit32_v5`，验证双周线能否少损长窗并改善 2026。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit32_v5`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit32_v5,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v11,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover3_exit42`。
- `biweekly_equal_buffered_soft_cost_guard_exit32_v5` 五窗口 CAGR 为 `20.93% / 21.51% / 20.00% / 25.98% / -13.96%`，最大回撤为 `-21.36% / -21.36% / -17.14% / -17.14% / -7.24%`，换手为 `5.77x / 5.72x / 5.65x / 7.52x / 6.93x`。双周线长窗稳定但收益明显低于 Path 1 robust，且 2026 转负，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `181/181 complete`，下一轮 focus 轮换为 `monthly_weekly_overlay`。第一条命令建议回到 monthly-weekly overlay，并在 soft exit 上做成本/现金守门折中，而不是继续双周低收益线，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v6`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-30 10:17 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `soft_cashguard_exit32_v3` 让 2026 转正但长窗仍低于 robust。本轮按 `monthly_weekly_overlay` 与 `risk_overlay_cost`，新增无低波的 `soft_cost_guard_exit32_v4`，验证成本守门是否能比 cashguard 少损长窗。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v4`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v4,hkconnect_path2_inverse_elastic_monthly_cost_guard_v10,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover3_exit44`。
- `soft_cost_guard_exit32_v4` 五窗口 CAGR 为 `23.76% / 30.95% / 32.20% / 42.91% / 2.13%`，最大回撤为 `-24.36% / -12.37% / -11.57% / -11.57% / -8.44%`，换手为 `3.72x / 3.70x / 3.39x / 3.59x / 4.23x`。它好于 v3 的长窗收益和换手，但仍未超过 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `178/178 complete`，下一轮 focus 轮换为 `biweekly_buffer`。第一条命令建议回到双周缓冲线，测试是否能保留 v4 的 2026 正收益并降低 2017 回撤，例如 `hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit32_v5`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-30 04:31 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `soft_cashguard_exit34_v2` 修复 2026 为小幅正收益但不改善 robust。本轮按 `monthly_weekly_overlay/biweekly_buffer` 提示，把 exit 从 `34` 收到 `32`，新增 `soft_cashguard_exit32_v3`，继续作为 HK 独立研究线。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit32_v3`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit32_v3`。
- `soft_cashguard_exit32_v3` 五窗口 CAGR 为 `22.55% / 29.09% / 30.15% / 42.91% / 2.13%`，最大回撤为 `-25.28% / -12.37% / -11.57% / -11.57% / -8.44%`，换手为 `4.02x / 4.10x / 3.68x / 3.59x / 4.23x`。它与 v2 同形，2026 为正但 2017/2020/2023 仍低于 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `175/175 complete`，下一轮 focus 为 `risk_overlay_cost`。第一条命令建议不要继续只压 exit，改在 monthly-weekly overlay 上加成本/风险 overlay 对照，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32_v4`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-29 22:21 CST）

- 开局 guard 为 `pass` 且 HK coverage complete；上一轮 `biweekly_equal_buffered_lowvol_soft_cost_guard_exit30` 保持浅回撤但长窗收益不足。本轮按 `monthly_weekly_overlay` 回到 monthly + weekly overlay，并在 `soft_exit34` 上增加轻现金守门 v2，目标是修复 2026 负收益。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v2`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v2`。
- `soft_cashguard_exit34_v2` 五窗口 CAGR 为 `22.67% / 29.30% / 30.35% / 42.91% / 2.13%`，最大回撤为 `-25.17% / -12.19% / -11.58% / -11.58% / -8.44%`，换手为 `3.99x / 4.10x / 3.67x / 3.59x / 4.23x`。v2 修复 2026 转正，且 2025 接近旧 `soft_exit34_cashguard_light`，但 2017/2020/2023 仍低于 Path 1 tracked winners。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `169/169 complete`，下一轮 focus 继续 `monthly_weekly_overlay`。第一条命令建议在 v2 基础上只微调现金阈值/exit，避免退回长窗弱的低波双周线，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit32_v3`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-29 16:33 CST）

- 开局 HK coverage 为 complete；上一轮 `monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit26` 保持浅回撤但长窗收益低于 robust。本轮按 `monthly_weekly_overlay/biweekly_buffer` 回到双周低波成本缓冲，并把退出放宽到 `exit30`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit30`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit30`。
- `biweekly_equal_buffered_lowvol_soft_cost_guard_exit30` 五窗口 CAGR 为 `17.39% / 18.96% / 31.90% / 37.89% / 2.91%`，最大回撤为 `-21.19% / -18.99% / -10.28% / -6.90% / -4.47%`，换手为 `5.74x / 5.47x / 5.09x / 6.65x / 6.98x`。它保持 2026 为正且回撤浅，但长窗收益仍低于 `weekly_overlay_soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`；三张 HK comparison 图已刷新。候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `166/166 complete`，下一轮 focus 为 `monthly_weekly_overlay`。第一条命令建议回到 monthly-weekly overlay，并用现金/成本守门修复 2026 负收益，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v2`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-29 10:22 CST）

- 开局 guard 为 `pass`；上一轮 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit32` 保持浅回撤但长窗收益弱，本轮按 `monthly_weekly_overlay/risk_overlay_cost` 回到月频+周度低波成本守门，测试更低 `exit26` 是否保持 2026 正收益并少损长窗。HK 缓存到 2026-05-27，`--end-date 2026-05-28` 准备保护失败后改用 `--end-date 2026-05-27` 完成增量回测。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit26`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit26`。
- `lowvol_soft_cost_guard_exit26` 五窗口 CAGR 为 `19.40% / 24.77% / 29.76% / 34.66% / 6.49%`，最大回撤为 `-22.22% / -7.16% / -6.85% / -6.85% / -6.73%`，换手为 `3.78x / 3.69x / 3.39x / 3.85x / 4.90x`。它继续保持 2026 正收益与浅回撤，但长窗收益仍低于 `weekly_overlay_soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `166/166 complete`，下一轮 focus 仍为 `monthly_weekly_overlay`。第一条命令建议停止继续压低 lowvol exit，回到无低波 monthly-weekly overlay 并补一个 2026 修复约束，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit34_v2`：`.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-29 04:17 CST）

- 开局 guard 为 `pass`；上一轮 monthly-weekly overlay 成本版恢复长窗收益但 2026 转负，本轮按 `biweekly_buffer/risk_overlay_cost` 回到双周低波成本缓冲，测试更低 `exit32` 是否能保持 2026 正收益并少损长窗。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit32`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit32,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v8,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover6_exit38`。
- `biweekly_equal_buffered_lowvol_soft_cost_guard_exit32` 五窗口 CAGR 为 `15.56% / 16.56% / 25.85% / 35.85% / 1.70%`，最大回撤为 `-21.07% / -19.22% / -11.21% / -6.94% / -4.49%`，换手为 `5.77x / 5.59x / 5.24x / 6.69x / 7.96x`。结果与 `exit34/36` 几乎同形，能保持 2026 正收益和浅回撤，但长窗收益显著低于 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `163/163 complete`，下一轮 focus 为 `risk_overlay_cost`。第一条命令建议回到 monthly-weekly overlay 的低波+成本守门，测试更低出场是否能保留 2026 正收益同时提高长窗，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit26`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-28 22:19 CST）

- 开局 guard 为 `pass`；上一轮 plan 要求回到 monthly-weekly overlay 邻域，本轮新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34`，作为无低波但保留成本守门的 `exit34` 对照，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34,hkconnect_path2_inverse_elastic_monthly_cost_guard_v8,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover6_exit40`。
- `soft_cost_guard_exit34` 五窗口 CAGR 为 `24.31% / 29.83% / 32.59% / 42.95% / -9.45%`，最大回撤为 `-22.67% / -13.36% / -13.36% / -13.36% / -10.91%`，换手为 `3.52x / 3.55x / 3.26x / 3.45x / 3.67x`。它恢复了长窗收益，但 2026 重新转负，不替换 HK Path 1 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `160/160 complete`，下一轮 focus 为 `biweekly_buffer`。第一条命令建议回到双周低波/成本缓冲，用更低出场阈值检查是否能保留 2026 正收益并少损长窗，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-28 16:18 CST）

- 开局 guard 为 `pass`；上一轮 plan 要求回到双周低波/成本缓冲，本轮新增 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34`，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v7,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover8_exit38`。
- `biweekly_equal_buffered_lowvol_soft_cost_guard_exit34` 五窗口 CAGR 为 `15.56% / 16.56% / 25.85% / 35.85% / 1.70%`，最大回撤为 `-21.08% / -19.22% / -11.21% / -6.94% / -4.49%`，换手为 `5.77x / 5.59x / 5.24x / 6.69x / 7.96x`。它保留浅回撤和 2026 正收益，但长窗收益明显低于 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `157/157 complete`，下一轮 focus 为 `monthly_weekly_overlay`。第一条命令建议回到 monthly-weekly overlay 邻域，测试无低波但保留成本守门的 `exit34` 对照，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `lowvol_soft_cost_guard_exit28` 保持 2026 正收益但长窗收益折损，本轮按 `monthly_weekly_overlay` 去掉 lowvol，保留成本守门并收紧到 `exit30`，验证无低波版本是否能找回长窗收益。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit30_risk25,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8_exit40`。
- `soft_cost_guard_exit30` 五窗口 CAGR 为 `23.99% / 29.46% / 32.25% / 42.95% / -9.45%`，最大回撤为 `-23.29% / -13.36% / -13.36% / -13.36% / -10.91%`，换手为 `3.57x / 3.55x / 3.27x / 3.45x / 3.67x`。去掉 lowvol 找回部分长窗收益，但 2026 重新转负，不替换 HK Path 1 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `154/154 complete`，下一轮 focus 转为 `biweekly_buffer`。第一条命令建议回到双周低波/成本缓冲，测试是否能少损长窗并保持 2026 正收益，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit34`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；上一轮双周低波轻成本版收益折损，本轮按 `risk_overlay_cost` 回到 monthly-weekly overlay 低波成本线，确认更低 `exit28` 是否能保留 2026 正收益与浅回撤。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit28`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit28,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit32_risk30,hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit68`。
- `lowvol_soft_cost_guard_exit28` 五窗口 CAGR 为 `19.64% / 25.01% / 29.92% / 34.65% / 6.49%`，最大回撤为 `-21.76% / -7.14% / -6.85% / -6.85% / -6.73%`，换手为 `3.76x / 3.69x / 3.40x / 3.85x / 4.90x`。它保持浅回撤和 2026 正收益，但收益继续低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，HK candidates `151/151 complete`，下一轮 focus 转为 `monthly_weekly_overlay`。第一条命令建议去掉低波收益折损、保留成本守门并收紧出场，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`；上一轮 `monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30` 保持 2026 正收益和浅回撤但长窗收益折损，本轮按 `biweekly_buffer` 测试双周低波轻成本版本，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36,hkconnect_path2_inverse_elastic_monthly_cost_guard_v7,hkconnect_path3_theme_fast_weekly_cost_guard_turnover1_exit66`。
- `biweekly_equal_buffered_lowvol_soft_cost_guard_exit36` 五窗口 CAGR 为 `15.56% / 16.56% / 25.85% / 35.85% / 1.70%`，最大回撤为 `-21.08% / -19.22% / -11.21% / -6.94% / -4.49%`，换手为 `5.77x / 5.59x / 5.24x / 6.69x / 7.96x`。它保留浅回撤与 2026 正收益，但 2017/2020/2023 收益明显低于 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。候选池未触发 HK explore cap evict，三张 HK 图表已刷新。
- 最终 guard 为 `pass`，下一轮 focus 为 `risk_overlay_cost`。第一条命令建议回到 monthly-weekly overlay 低波成本线，测试更低出场阈值能否保留浅回撤且少损长窗收益，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit28`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮建议沿 `risk_overlay_cost` 测 `lowvol_soft_cost_guard_exit30`，本轮已新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30`，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v6,hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit64`。
- `lowvol_soft_cost_guard_exit30` 五窗口 CAGR 为 `19.77% / 25.18% / 30.07% / 34.65% / 6.49%`，最大回撤 `-21.63% / -7.17% / -6.85% / -6.85% / -6.73%`，换手 `3.73x / 3.68x / 3.39x / 3.85x / 4.90x`。它保持 2026 正收益和浅回撤，但 2017/2020/2023 收益仍低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，四窗口 meanCAGR `33.87%`、minCAGR `26.10%`、worstMaxDD `-21.06%`、meanTurn `3.33x`；三张 HK 图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 为 `pass`，HK candidates `145/145 complete`，下一轮 focus 转为 `biweekly_buffer`。第一条命令建议回到双周缓冲线，测试是否能以更低换手保留本轮低波浅回撤，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cost_guard_exit36`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮低波 + 成本守门 `exit32` 保持 2026 为正但收益折损，本轮按 `monthly_weekly_overlay` 去掉低波、保留成本守门与 `exit32`，新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32`。HK 合并回测命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32,hkconnect_path2_inverse_elastic_monthly_cost_guard_v6,hkconnect_path3_theme_fast_weekly_cost_guard_turnover2_exit62`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32`。五窗口 CAGR 为 `24.15% / 29.72% / 32.53% / 42.95% / -9.45%`，最大回撤 `-23.19% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.55x / 3.55x / 3.26x / 3.45x / 3.67x`。去低波提高了长窗收益，但 2026 重新转负，不能替换当前 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，四窗口 meanCAGR `33.87%`、minCAGR `26.10%`、worstMaxDD `-21.06%`、meanTurn `3.33x`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议不要只去低波，改在 `exit30/32` 上组合低波与成本守门，先测 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；上一轮要求沿 `risk_overlay_cost` 测试低波 + 成本守门的 monthly-weekly overlay，本轮新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32`。HK 合并回测命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control_v5,hkconnect_path3_theme_fast_weekly_defensive_turnover3_exit60`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32`。五窗口 CAGR 为 `19.98% / 25.44% / 30.26% / 34.65% / 6.49%`，最大回撤 `-21.30% / -7.16% / -6.85% / -6.85% / -6.73%`，换手 `3.72x / 3.68x / 3.39x / 3.85x / 4.90x`。它把 2026 保持为正且回撤浅，但收益继续低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `monthly_weekly_overlay`。下一轮第一条命令建议去掉低波收益折损、保留成本守门与 `exit32`，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮 `biweekly_equal_buffered_lowvol_soft_exit38` 修复 2026 但收益折损，本轮按 `monthly_weekly_overlay` 回到 monthly-weekly overlay robust 邻域，新增低波 + 轻现金 + `exit32` 组合。HK 合并回测命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit32,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit34_risk35,hkconnect_path3_theme_fast_weekly_cost_guard_turnover3_exit60`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit32`。五窗口 CAGR 为 `19.32% / 24.43% / 29.27% / 34.65% / 6.49%`，最大回撤 `-23.40% / -9.26% / -6.85% / -6.85% / -6.73%`，换手 `3.94x / 4.04x / 3.70x / 3.85x / 4.90x`。它保持 2026 正收益和浅回撤，但 2017/2020/2023 收益继续低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议在本轮 `lowvol_soft_cashguard_exit32` 基础上把现金防守改成更直接的周度 overlay 成本约束，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮 `monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32` 继续保持 2026 为正但收益折损，本轮按 `biweekly_buffer` 新增 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38,hkconnect_path2_theme_monthly_high_return_cost_control_v4,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover10_exit36`。
- `biweekly_equal_buffered_lowvol_soft_exit38` 五窗口 CAGR 为 `16.28% / 17.49% / 27.12% / 35.85% / 1.70%`，最大回撤 `-20.46% / -19.07% / -11.15% / -6.94% / -4.49%`，换手 `5.77x / 5.57x / 5.23x / 6.69x / 7.96x`。它能修复 2026 为小幅正收益并压回撤，但 2017/2020 收益仍显著低于 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `monthly_weekly_overlay`。下一轮第一条命令建议回到 monthly-weekly overlay robust 邻域，把低波浅回撤与现金成本防守合并测试，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮 `biweekly_equal_buffered_lowvol_soft_exit40` 修复 2026 但长窗收益折损，本轮按 `risk_overlay_cost` 回到 monthly-weekly overlay 的低波轻风控线，新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit36_risk35,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover10_exit38`。
- `lowvol_soft_exit32` 五窗口 CAGR 为 `21.35% / 27.11% / 32.25% / 34.65% / 6.49%`，最大回撤 `-20.31% / -8.41% / -6.85% / -6.85% / -6.73%`，换手 `3.50x / 3.53x / 3.27x / 3.85x / 4.90x`。它继续保持 2026 为正和浅回撤，但相对无低波 `soft_exit34` robust 仍有收益折损。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；图表已刷新，候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `biweekly_buffer`。下一轮第一条命令建议从双周缓冲低波线继续找收益折损更小的 2026 修复，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit38`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `lowvol_soft_exit34` 修复 2026 但收益折损；本轮按 `biweekly_buffer` 新增 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40,hkconnect_path2_inverse_elastic_monthly_cost_guard_v5,hkconnect_path3_theme_fast_weekly_cost_guard_turnover4_exit58`。
- `biweekly_equal_buffered_lowvol_soft_exit40` 五窗口 CAGR 为 `16.28% / 17.48% / 27.12% / 35.85% / 1.70%`，最大回撤 `-20.46% / -19.06% / -11.15% / -6.94% / -4.49%`，换手 `5.77x / 5.57x / 5.23x / 6.69x / 7.96x`。结果与 `exit42` 基本同形，能保持 2026 正收益和浅回撤，但 2017/2020 长窗收益低于现有 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议回到 monthly-weekly overlay robust 邻域修复 2026 与成本，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `monthly_weekly_overlay`；本轮按计划新增 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit38_risk40,hkconnect_path3_theme_fast_weekly_cost_guard_turnover5_exit56`。
- `lowvol_soft_exit34` 五窗口 CAGR 为 `21.27% / 27.07% / 32.26% / 34.65% / 6.49%`，最大回撤 `-20.35% / -8.58% / -6.85% / -6.85% / -6.73%`，换手 `3.47x / 3.50x / 3.26x / 3.85x / 4.90x`。它修复 2026 为正并显著压回撤，但 2017/2020/2025 收益仍低于无低波 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `biweekly_buffer`。下一轮第一条命令建议用双周缓冲低波线修复 2026，同时控制收益折损，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit40`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `biweekly_buffer`；本轮按计划新增双周缓冲无低波版本 `hkconnect_path1_biweekly_equal_buffered_soft_exit40`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_soft_exit40`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_exit40,hkconnect_path2_theme_monthly_high_return_cost_control_v3,hkconnect_path3_theme_fast_weekly_defensive_turnover6_exit54`。
- `biweekly_equal_buffered_soft_exit40` 五窗口 CAGR 为 `21.79% / 22.47% / 21.27% / 24.18% / -15.62%`，最大回撤 `-21.03% / -21.03% / -16.20% / -16.20% / -8.76%`，换手 `5.77x / 5.57x / 5.42x / 7.10x / 6.51x`。它比低波双周线保留了更多长窗收益，但 2026 仍明显为负，未能替换当前 monthly-weekly overlay robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `monthly_weekly_overlay`。下一轮第一条命令建议回到 robust 邻域做月频+周度 overlay 修复，而不是继续双周收益折损线，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass`，上一轮要求沿 `monthly_weekly_overlay` 修复 `soft_exit34` 的 2026 负收益；本轮新增 `soft_exit32`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32,hkconnect_path2_inverse_elastic_monthly_cost_guard_v4,hkconnect_path3_theme_fast_weekly_cost_guard_turnover6_exit54`。
- `soft_exit32` 五窗口 CAGR 为 `26.06% / 32.10% / 34.28% / 42.95% / -9.45%`，最大回撤 `-21.34% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.36x / 3.43x / 3.16x / 3.45x / 3.67x`。它没有修复 2026，且 robust 略低于现有 `soft_exit34`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `biweekly_buffer`。下一轮第一条命令建议回到双周缓冲但去掉过强低波收益折损，例如 `hkconnect_path1_biweekly_equal_buffered_soft_exit40` 或同等更高收益双周缓冲版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass`，上一轮 `biweekly_equal_buffered_lowvol_soft_exit42` 修复 2026 但收益折损较大；本轮按 `risk_overlay_cost`/`monthly_weekly_overlay` 回到 `soft_exit34` robust 邻域，新增浅现金防守版本，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light,hkconnect_path2_theme_monthly_high_return_cost_control_v2,hkconnect_path3_theme_fast_weekly_defensive_turnover8_exit52`。
- `soft_exit34_cashguard_light` 五窗口 CAGR 为 `23.25% / 28.47% / 31.01% / 42.95% / -9.45%`，最大回撤 `-23.78% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.82x / 3.99x / 3.56x / 3.45x / 3.67x`。浅现金没有修复 2026，且 2017/2020/2023 弱于当前 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先；候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 为 `monthly_weekly_overlay`。下一轮第一条命令建议不要继续加现金防守，改测更直接的退出阈值修复，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32` 或同等无低波月频周度 overlay 版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass`，上一轮 `soft_exit34` 把 HK Path 1 2017 winner 与 robust 推到无低波 monthly-weekly overlay，但 2026 仍为负；本轮按 `biweekly_buffer` 回到双周缓冲低波版本 `exit42`，继续作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit42`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit42,hkconnect_path2_equal_elastic_monthly_cost_guard_v4,hkconnect_path3_theme_fast_weekly_cost_guard_turnover8_exit52`。
- `biweekly_equal_buffered_lowvol_soft_exit42` 五窗口 CAGR 为 `16.28% / 17.48% / 27.12% / 35.85% / 1.70%`，最大回撤 `-20.46% / -19.06% / -11.15% / -6.94% / -4.49%`，换手 `5.77x / 5.57x / 5.23x / 6.69x / 7.96x`。它修复 2026 为小幅正收益且回撤浅，但 2017/2020 收益显著低于 `soft_exit34` robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先。候选池未触发 HK explore cap evict。
- 最终 guard 下一轮 focus 转为 `risk_overlay_cost`。下一轮第一条命令建议回到当前 `soft_exit34` robust 邻域做浅现金/低波成本对照，而不是继续双周收益折损线，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_next_id>`。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass`，上一轮低波 `soft_exit36` 保持 2026 正收益但长窗收益低于无低波 soft 线；本轮按 `monthly_weekly_overlay` 回到无低波 `soft_exit34`，继续只作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34,hkconnect_path2_theme_monthly_high_return_lowturn_reconfirm,hkconnect_path3_theme_fast_weekly_defensive_turnover10_exit50`。
- `soft_exit34` 五窗口 CAGR 为 `26.10% / 32.08% / 34.34% / 42.95% / -9.45%`，最大回撤 `-21.06% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.33x / 3.39x / 3.13x / 3.45x / 3.67x`。它没有修复 2026 负收益，但四窗口 robust 较上一轮 `soft_exit36` 继续小幅提升。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 发生实质变化：2017 window winner 与 robust candidate 切到 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，robust 约为 `meanCAGR=33.87% / minCAGR=26.10% / worstMaxDD=-21.06% / meanTurn=3.33x`；2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先。
- 候选池未触发 HK explore cap evict。最终 guard 对 HK Path 1 为 `stagnation_runs=2 / focus=monthly_weekly_overlay`，因为本轮新 robust 签名已经写入 state；下一轮第一条命令建议围绕新 robust 做 2026 修复对照，例如实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34_cashguard_light` 或 `soft_exit32`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass`，上一轮 `lowvol_soft_exit38` 修复 2026 但收益低于 HK Path 1 robust；本轮按 `risk_overlay_cost`/下一步对照，把低波轻风控退出阈值降到 `exit36`，继续只作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit36,hkconnect_path2_breakout_cost_guard_biweekly_defensive_cashguard_exit40_risk45,hkconnect_path3_theme_fast_weekly_cost_guard_turnover10_exit50`。
- `lowvol_soft_exit36` 五窗口 CAGR 为 `21.10% / 26.75% / 31.96% / 34.73% / 6.49%`，最大回撤 `-20.05% / -8.77% / -6.80% / -6.80% / -6.73%`，换手 `3.44x / 3.46x / 3.24x / 3.86x / 4.90x`。它保持 2026 正收益和浅回撤，略高于上一轮低波 exit38 的长窗收益，但仍低于当前无低波 soft 线 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 新增该候选记录，但 winner/robust 未被替换：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`。候选池未触发 HK explore cap evict。
- 收尾 guard 下一轮 focus 为 `monthly_weekly_overlay`。下一轮第一条命令建议回到无低波 soft robust 邻域修复 2026，而不是继续低波收益折损，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34` 或 `soft_exit36_cashguard_light`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `soft_exit36` 已把 HK Path 1 robust 留在无低波的 soft 线；本轮按计划测试低波轻风控 `exit38`，继续只作为沪港通独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38,hkconnect_path2_theme_monthly_reconfirm_high_return_cost_control,hkconnect_path3_stable_weekly_equal_buffered_defensive_turnover9_exit42`。
- `lowvol_soft_exit38` 五窗口 CAGR 为 `21.03% / 26.62% / 31.95% / 34.73% / 6.49%`，最大回撤 `-19.68% / -8.96% / -6.80% / -6.80% / -6.73%`，换手 `3.43x / 3.43x / 3.22x / 3.86x / 4.90x`。它修复 2026 为正且回撤很浅，但 2017/2020/2023/2025 收益低于现有 soft/soft_exit36 robust/winner 组合。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 未被本轮低波候选替换：2017 与 robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36`，2020/2023 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`。候选池未触发 HK explore cap evict。
- 收尾 focus 转向 `biweekly_buffer`。下一轮第一条命令建议回到双周缓冲，但带上本轮低波浅回撤信息，例如 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_exit42` 或同等低波双周版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_biweekly_buffer_next_id>`。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass`，上一轮 `soft_exit38` 已把 2017 winner 与 robust 推到更低退出阈值；本轮按 `monthly_weekly_overlay` 继续测试 `soft_exit36`，目标是只看 2026 观察窗是否修复且不损伤 robust。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36,hkconnect_path2_breakout_cost_guard_biweekly_cashguard_exit35_risk50,hkconnect_path3_theme_fast_weekly_defensive_turnover12_exit48`。
- `soft_exit36` 五窗口 CAGR 为 `25.96% / 31.81% / 34.53% / 42.95% / -9.45%`，最大回撤 `-20.92% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.30x / 3.34x / 3.11x / 3.45x / 3.67x`。它没有修复 2026，但四窗口 robust 小幅高于 `soft_exit38`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 再次变化：2017 window winner 与 robust candidate 切到 `soft_exit36`，robust `meanCAGR=33.81% / minCAGR=25.96% / worstMaxDD=-20.92% / meanTurn=3.30x`；2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先。
- 候选池未触发 HK explore cap evict。收尾 guard 对 HK Path 1 为 `changed=true / stagnation_runs=0 / focus=monthly_weekly_overlay`；下一轮第一条命令建议不要再机械下调 exit，先比较 `soft_exit36` 与低波/现金防守组合，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit38`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_next_id>`。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass`，上一轮 `soft_exit40` 已把 2017 winner 与 robust 切到周度 overlay soft 线，但 2026 仍为负；本轮按 `monthly_weekly_overlay` 再把退出阈值降到 `38`，继续作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit38`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit38,hkconnect_path2_theme_monthly_reconfirm_cost_control,hkconnect_path3_theme_fast_weekly_cost_guard_turnover12_exit48`。
- `soft_exit38` 五窗口 CAGR 为 `25.95% / 31.79% / 34.40% / 42.95% / -9.45%`，最大回撤 `-20.94% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.27x / 3.31x / 3.08x / 3.45x / 3.67x`；robust4 为 `meanCAGR=33.77% / minCAGR=25.95% / worstMaxDD=-20.94% / meanTurn=3.28x`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 再次变化：2017 window winner 与 robust candidate 切到 `soft_exit38`，2020/2023 仍由 `weekly_overlay_soft` 领先，2025 仍由 `weekly_overlay_cashguard` 领先。新版本较 `soft_exit40` 稍抬 robust，但仍未修复 2026 负收益。
- 候选池未触发 HK explore cap evict。收尾 guard 对 HK Path 1 为 `changed=true / stagnation_runs=0 / focus=monthly_weekly_overlay`；下一轮第一条命令建议测试 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit36` 或同等更低退出阈值版本，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_soft_exit36_id>`，重点只看能否改善 2026 且不损伤 robust。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass`，上一轮建议从 `monthly_weekly_overlay` 去掉低波并放宽退出；本轮新增 `soft_exit40`，继续只作为 HK 独立研究线，不并入 A股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40`。实际 HK 合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40,hkconnect_path2_theme_monthly_cost_control_lowturn,hkconnect_path3_theme_fast_weekly_cost_guard_turnover16_exit45`。
- `soft_exit40` 五窗口 CAGR 为 `25.76% / 31.66% / 34.38% / 42.95% / -9.45%`，最大回撤 `-20.90% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.26x / 3.28x / 3.06x / 3.45x / 3.67x`；它没有修复 2026，但长窗收益/回撤组合优于旧 robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 发生实质变化：2017 window winner 切到 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40`，robust candidate 也切到该 ID，robust `meanCAGR=33.69% / minCAGR=25.76% / worstMaxDD=-20.90% / meanTurn=3.26x`。2020/2023 winner 仍为 `weekly_overlay_soft`，2025 仍为 `weekly_overlay_cashguard`。
- 候选池未触发 HK explore cap evict。收尾 guard 的下一轮 focus 为 `monthly_weekly_overlay`；第一条命令建议沿新 robust 做 2026 修复对照，例如 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit38` 或同等更低退出阈值版本，用五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_id>` 判断能否保留 robust 且改善 2026。

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass`，上一轮 `biweekly_equal_buffered_lowvol_soft_cashguard_exit45` 浅回撤但收益折损过大；本轮按 `risk_overlay_cost`/低波轻风控回到月频等权缓冲 + 周度 overlay，去掉 cashguard 并把退出阈值调到 `exit42`。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42`。实际 HK 合并命令：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42,hkconnect_path2_inverse_elastic_monthly_cost_guard_v3,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover9_exit40`。
- `lowvol_soft_exit42` 五窗口 CAGR 为 `21.00% / 26.50% / 31.90% / 34.70% / 6.50%`，最大回撤 `-19.70% / -9.50% / -6.80% / -6.80% / -6.70%`，换手 `3.41x / 3.38x / 3.17x / 3.86x / 4.90x`；2026 保持正收益且回撤浅，但 2017/2020/2023 收益仍低于 `weekly_overlay_soft` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；候选池未触发 HK explore cap evict。
- 下一轮 focus -> candidates 池切到 `monthly_weekly_overlay`，第一条命令建议去掉低波或进一步放宽退出，测试 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit40`，五窗口 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_monthly_weekly_overlay_id>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass`，上一轮 `monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45` 2026 转正但长窗收益不足；本轮按 `biweekly_buffer` 回到双周等权缓冲，叠加低波、轻现金防守与 `exit45`，继续只作为 HK 独立研究线。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cashguard_exit45`。实际 HK 合并命令：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cashguard_exit45,hkconnect_path2_equal_elastic_monthly_cost_guard_v3,hkconnect_path3_theme_fast_weekly_cost_guard_turnover14_exit45`。
- `biweekly_lowvol_soft_cashguard_exit45` 五窗口 CAGR 为 `15.43% / 16.36% / 24.12% / 35.85% / 1.70%`，最大回撤 `-21.74% / -19.07% / -11.17% / -6.94% / -4.49%`，换手 `5.88x / 5.77x / 5.34x / 6.69x / 7.96x`；2026 小幅转正且回撤浅，但 2017/2020 收益明显低于月频 weekly-overlay soft robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化；候选池未触发 HK explore cap evict。
- 下一轮 focus -> candidates 池：双周低波现金线收益折损过大，第一条命令建议回到 `monthly_weekly_overlay` 的低波轻风控但放宽现金防守，测试 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit42`，五窗口 `--only-strategy-ids <hk_path1_lowvol_soft_exit42_id>`。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 指向 `monthly_weekly_overlay`；上一轮 `lowvol_cashguard_exit45` 长窗收益不足，本轮补 `lowvol + soft + cashguard + exit45`，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45,hkconnect_path2_breakout_cost_guard_biweekly_risk50,hkconnect_path3_theme_fast_weekly_cost_guard_turnover18_exit42`。
- `lowvol_soft_cashguard_exit45` 五窗口 CAGR 为 `18.94% / 24.07% / 28.96% / 34.73% / 6.49%`，最大回撤 `-24.07% / -9.02% / -6.80% / -6.80% / -6.73%`，换手 `4.02x / 4.07x / 3.70x / 3.86x / 4.90x`；2026 为正且回撤浅，但 2017/2020/2023 收益仍低于 `weekly_overlay_soft` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；未触发 HK explore cap evict。
- 收尾 guard 后 HK Path 1 rotation 切到 `biweekly_buffer`。下一轮第一条命令建议实现 `hkconnect_path1_biweekly_equal_buffered_lowvol_soft_cashguard_exit45`，检查双周缓冲能否保留低波现金防守的浅回撤而减少月频 overlay 的长窗收益折损；五窗口 `--only-strategy-ids <hk_path1_biweekly_lowvol_soft_id>`。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮双周 `soft_cashguard_exit45` 收益不足且 2026 仍负，本轮按 `risk_overlay_cost` 回到月频等权缓冲 + 周度 overlay 的低波现金防守。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45`。
- 该候选五窗口 CAGR 为 `18.36% / 23.40% / 28.45% / 34.73% / 6.49%`，最大回撤 `-24.99% / -8.94% / -6.80% / -6.80% / -6.73%`，换手 `4.08x / 4.07x / 3.70x / 3.86x / 4.90x`；2026 转正且回撤浅，但 2017/2020/2023 收益低于 `weekly_overlay_soft` robust，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；HK 线继续独立，不并入 A 股 winner。
- 下一轮 focus -> candidates 池：继续比较 2026 正收益与长窗收益折损，第一条命令建议实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cashguard_exit45`，用五窗口 `--only-strategy-ids <hk_path1_next_risk_overlay_id>` 增量确认。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `soft_cashguard_exit45` 仍未修复 2026，本轮按 `biweekly_buffer` 回到双周等权缓冲，补一个 `soft_cashguard_exit45` 版本，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45,hkconnect_path2_equal_elastic_monthly_cashguard_v3,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover7_exit45`。
- `soft_cashguard_exit45` 五窗口 CAGR 为 `20.31% / 20.32% / 18.33% / 24.18% / -15.62%`，最大回撤 `-21.15% / -21.15% / -16.20% / -16.20% / -8.76%`，换手 `5.84x / 5.71x / 5.55x / 7.10x / 6.51x`；回撤接近双周成本守门，但收益和 2026 仍弱，不晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；robust 仍为 `weekly_overlay_soft`。收尾 guard 为 `pass`，HK all candidates `79/79 complete`。
- 最终 rotation 为 `stagnation_runs=7 / risk_overlay_cost / rotate`。下一轮 focus -> candidates 池从双周回到月频/周度 overlay 风控成本，第一条命令建议实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cashguard_exit45`，五窗口 `--only-strategy-ids <hk_path1_risk_overlay_id>` 增量确认。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `weekly_overlay_cashguard` 把 2025 winner 切过去但 2026 仍负，本轮按 `monthly_weekly_overlay` 补 `soft + cashguard + exit45`，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit45`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit45,hkconnect_path2_inverse_elastic_monthly_cost_guard_v2,hkconnect_path3_theme_fast_weekly_cashguard_turnover20`。
- `soft_cashguard_exit45` 五窗口 CAGR 为 `22.30% / 27.12% / 30.06% / 42.95% / -9.45%`，最大回撤 `-25.23% / -13.36% / -13.36% / -13.36% / -10.91%`，换手 `3.98x / 4.02x / 3.57x / 3.45x / 3.67x`；2025 持平 cashguard，但 2017/2020/2023 弱于 `weekly_overlay_soft` 且 2026 未修复。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered_weekly_overlay_cashguard`；robust 仍为 `weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- 收尾 guard 为 `pass`，HK all candidates `76/76 complete`；最终 rotation 为 `stagnation_runs=4 / biweekly_buffer / rotate`。下一轮 focus -> candidates 池回到双周缓冲，第一条命令建议实现 `hkconnect_path1_biweekly_equal_buffered_soft_cashguard_exit45`，五窗口 `--only-strategy-ids <hk_path1_biweekly_id>` 增量确认。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `lowvol_cost_guard` 改善 2026 但牺牲长窗，最终 focus 继续 `monthly_weekly_overlay`。本轮补 `cashguard`，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard,hkconnect_path2_theme_monthly_cost_control_v2,hkconnect_path3_stable_weekly_equal_buffered_cashguard_turnover9`。
- `cashguard` 五窗口 CAGR 为 `21.63% / 26.19% / 29.44% / 42.95% / -9.45%`，最大回撤 `-25.94% / -13.51% / -13.36% / -13.36% / -10.91%`，换手 `4.02x / 4.00x / 3.56x / 3.45x / 3.67x`；2025 窗口强于旧月频锚点，但 2017/2020/2023 和 2026 不如 `weekly_overlay_soft`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 的 `since_2025_01` winner 切到 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard`；2017/2020/2023 与 robust 仍为 `monthly_equal_buffered_weekly_overlay_soft`，robust `meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- Guard 显示 HK all candidates `73/73 complete`，本轮未触发 evict；最终 rotation 为 `stagnation_runs=1 / monthly_weekly_overlay / continue`。下一轮 focus -> candidates 池比较 `cashguard` 的 2025 提升是否可保留且修复 2026，第一条命令建议实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cashguard_exit45` 并五窗口增量确认。

## 本轮执行计划（2026-05-20 13:58 CST）

- 上一轮 focus 已从双周现金防守转回 `monthly_weekly_overlay`；本轮新增低波周度 overlay 成本守门版本，继续作为 HK 独立研究线，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard,hkconnect_path2_equal_elastic_monthly_cost_guard_v2,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover8`。
- `lowvol_cost_guard` 五窗口 CAGR 为 `20.46% / 25.98% / 31.24% / 34.73% / 6.49%`，最大回撤 `-20.45% / -8.47% / -6.80% / -6.80% / -6.73%`，换手 `3.55x / 3.48x / 3.23x / 3.86x / 4.90x`；2026 转正且回撤更浅，但 2017/2020/2023 收益低于 `weekly_overlay_soft`，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `hkconnect_path1_monthly_equal_buffered`；robust 仍为 `monthly_equal_buffered_weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- Guard 显示 HK all candidates `70/70 complete`，本轮未触发 evict；最终 rotation 为 `stagnation_runs=11 / monthly_weekly_overlay / rotate`。下一轮 focus -> candidates 池继续比较收益折损和 2026 防守，第一条命令建议实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard`，再用五窗口 `--only-strategy-ids <hk_path1_overlay_id>` 增量确认。

## 本轮执行计划（2026-05-20 05:20 CST）

- 上一轮提示为双周线的 2026 防守修复；本轮新增一个更强现金防守的双周等权缓冲候选，继续只作为 HK Path 1 观察，不并入 A 股 winner。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_cashguard`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_cashguard,hkconnect_path2_breakout_cost_guard_biweekly_exit35,hkconnect_path3_theme_fast_weekly_defensive_turnover18`。
- `cashguard` 五窗口 CAGR 为 `19.82% / 19.75% / 17.76% / 24.18% / -15.62%`，最大回撤 `-21.23% / -21.23% / -16.20% / -16.20% / -8.76%`，换手 `5.50x-7.10x`；比上一轮 `cost_guard` 收益更低，2026 仍为负，未晋级。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `hkconnect_path1_monthly_equal_buffered`；robust 仍为 `monthly_equal_buffered_weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- HK candidate_count 为 `67`，未触发 evict；收尾 guard 的 HK Path 1 rotation 为 `stagnation_runs=8 / risk_overlay_cost / rotate`。下一轮 focus -> candidates 池从双周回到月频/周度 overlay 成本，先测低波或更低风险暴露，不再继续加双周现金防守。
- 下一轮第一条命令建议先实现 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_cost_guard` 与 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_cashguard` 后，用 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <hk_path1_risk_overlay_cost_ids>` 补跑。

## 本轮执行计划（2026-05-19 23:14 CST）

- 上一轮 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft` 成为 2017/2020/2023 winner 与 robust；本轮按最终 rotation 的 `biweekly_buffer` 补一个双周成本防守对照，继续不并入 A 股结论。
- 本轮新增并五窗口确认：`hkconnect_path1_biweekly_equal_buffered_cost_guard`。实际命令与 HK Path 2/3 合并执行：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_cost_guard,hkconnect_path2_breakout_cost_guard_biweekly,hkconnect_path3_stable_weekly_equal_buffered_wide_cost_guard`。
- 新双周成本防守五窗口 CAGR 为 `21.45% / 21.96% / 20.68% / 24.18% / -15.62%`，最大回撤 `-21.03% / -21.03% / -16.20% / -16.20% / -8.76%`；比旧双周线更稳一点，但收益与 2026 观察窗仍不如月频 soft robust。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 tracked/robust 未变化：2017/2020/2023 仍为 `monthly_equal_buffered_weekly_overlay_soft`，2025 仍为 `monthly_equal_buffered`；robust 为 `monthly_equal_buffered_weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- HK candidate_count 为 `64/64 complete`，本轮未触发 evict；下一轮 focus -> candidates 池仍按 `biweekly_buffer`，优先测试双周线的 2026 防守修复而不是再扩月频 overlay。建议先实现 `hkconnect_path1_biweekly_equal_buffered_cashguard` 与 `hkconnect_path1_biweekly_equal_buffered_lowvol_cost_guard`，第一条命令继续用五窗口 `--only-strategy-ids`。

## 本轮执行计划（2026-05-19 17:26 CST）

- 本轮新增并用 `--only-strategy-ids` 五窗口补跑 3 个月频周度 overlay 变体：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_defensive`、`hkconnect_path1_monthly_lowvol_weekly_overlay_soft`；没有裸跑全量 HK。
- `soft` 版成为 2017/2020/2023 window winner 与 robust：2017 `24.96% CAGR / -24.94% MaxDD / 1.30 Sharpe / 3.40 Turn`，2020 `32.33% / -14.83% / 1.55 / 3.40`，2023 `34.60% / -14.83% / 1.73 / 3.13`；2025 仍由 `hkconnect_path1_monthly_equal_buffered` 保持 `40.41% CAGR`。
- `defensive` 版收益略低但接近，`lowvol_weekly_overlay_soft` 的 2026 短窗为正（`5.16% CAGR`）且回撤最浅，但 2017/2020/2023 收益弱于 `soft`。
- `scripts/update_hkconnect_artifacts.py` 后 HK Path 1 robust candidate 切换为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft`，`meanCAGR=32.95% / minCAGR=24.96% / worstMaxDD=-24.94% / meanTurn=3.37`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=1 / monthly_weekly_overlay / continue`；下一轮优先比较 `soft` overlay 的 2026 防守缺口与 lowvol 版本的收益折损。

## 本轮执行计划（2026-05-19 11:12 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与三张 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 当前窗口指标为：2017 `24.03% CAGR / -23.59% MaxDD / 1.29 Sharpe / 3.09 Turn`，2020 `31.21% / -14.83% / 1.52 / 3.52`，2023 `33.85% / -14.79% / 1.69 / 2.87`，2025 `40.41% / -14.79% / 1.53 / 3.46`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=34 / risk_overlay_cost / rotate`；下一轮优先比较月频稳健线上的风险 overlay 成本和双周缓冲的 2026 短窗失效。

## 本轮执行计划（2026-05-19 05:29 CST）

- 本轮按 `biweekly_buffer` 轮换方向新增并增量补跑 `hkconnect_path1_biweekly_equal_buffered_wide_exit` 与 `hkconnect_path1_biweekly_equal_buffered_defensive`，命令使用 `--only-strategy-ids`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- 新 `wide_exit` 五窗口为：2017 `21.33% CAGR / -22.59% MaxDD / 1.03 Sharpe / 6.09 Turn`，2020 `24.54% / -21.18% / 1.08 / 5.91`，2023 `25.25% / -16.25% / 1.31 / 5.72`，2025 `25.74% / -16.25% / 1.15 / 7.64`，2026 `-15.06%`。
- 新 `defensive` 与 `wide_exit` 接近但略低，2017/2020/2023 CAGR 分别为 `20.83% / 23.79% / 24.38%`；两者均未替换月频稳健锚点。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 三张对比图；HK Path 1 tracked winners 未变：2017/2023/2025 `hkconnect_path1_monthly_equal_buffered`，2020 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 仍为 `stagnation_runs=32 / recommended_focus=biweekly_buffer / rotate`；下一轮继续比较双周缓冲的成本与 2026 年短窗失效。

## 本轮执行计划（2026-05-18 23:13 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 三张对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 当前窗口指标为：2017 `24.03% CAGR / -23.59% MaxDD / 1.29 Sharpe / 3.09 Turn`，2020 `31.21% / -14.83% / 1.52 / 3.52`，2023 `33.85% / -14.79% / 1.69 / 2.87`，2025 `40.41% / -14.79% / 1.53 / 3.46`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=30 / recommended_focus=biweekly_buffer / rotate`；下一轮优先比较双周缓冲与月频稳健线的交易成本和信号生效日。

## 本轮执行计划（2026-05-18 20:34 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 与部分 `hk_daily_adj` 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 三张对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=28 / recommended_focus=monthly_weekly_overlay / rotate`；下一轮优先比较月频稳健线上的周度 overlay 成本与信号生效日。

## 本轮执行计划（2026-05-18 11:11 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=23 / recommended_focus=biweekly_buffer / rotate`；下一轮优先比较双周缓冲与月频稳健线的交易成本。

## 本轮执行计划（2026-05-18 05:53 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=20 / recommended_focus=monthly_weekly_overlay / rotate`；下一轮继续比较月频稳健线上的周度 overlay 成本。

## 本轮执行计划（2026-05-17 23:12 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=18 / recommended_focus=monthly_weekly_overlay / rotate`；下一轮继续比较月频稳健线上的周度 overlay 成本。

## 本轮执行计划（2026-05-17 17:25 CST）

- 本轮按增量要求运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，没有裸跑全量 HK；trade calendar 在线更新失败后回退本地缓存。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，HK Path 1 rotation 为 `stagnation_runs=15 / recommended_focus=risk_overlay_cost / rotate`；下一轮优先比较月频稳健线上的风险 overlay 成本。

## 本轮执行计划（2026-05-17 11:15 CST）

- 本轮完整运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`；trade calendar 在线更新失败后回退本地缓存，HK coverage 收尾仍为 `44/44 complete / pass`。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与三张 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=12 / recommended_focus=biweekly_buffer / rotate`；下一轮优先比较双周缓冲与月频稳健线的真实交易成本和信号生效日。

## 本轮执行计划（2026-05-17 05:15 CST）

- 本轮完整运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`；trade calendar 在线更新失败后回退本地缓存，HK coverage 收尾仍为 `44/44 complete / pass`。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与三张 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=10 / recommended_focus=monthly_weekly_overlay / rotate`；下一轮继续比较月频稳健线上的周度 overlay 真实成本与信号生效日，不把纯周度换股并回 Path 1。

## 本轮执行计划（2026-05-16 23:12 CST）

- 本轮完整运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`；trade calendar 在线更新失败后回退本地缓存，HK coverage 收尾仍为 `44/44 complete / pass`。
- `scripts/update_hkconnect_artifacts.py` 已同步 tracked payload 与三张 HK 对比图；港股线继续独立，不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，指标分别为 `24.03% / 33.85% / 40.41% CAGR`；2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% CAGR / -14.83% MaxDD / 1.52 Sharpe / 3.52 Turn`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=8 / recommended_focus=risk_overlay_cost / rotate`；下一轮继续比较月频稳健线上的周度风险 overlay 成本与信号生效日。

## 本轮执行计划（2026-05-16 17:14 CST）

- 本轮完整运行 `.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，并用 `update_hkconnect_artifacts.py` 同步 tracked payload 与三张 HK 对比图。
- HK Path 1 tracked winners 未变：2017 `hkconnect_path1_monthly_equal_buffered`（`24.03% CAGR / -23.59% MaxDD / 1.29 Sharpe / 3.09 Turn`），2020 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% / -14.83% / 1.52 / 3.52`）。
- 2023 与 2025 winner 仍为 `hkconnect_path1_monthly_equal_buffered`，分别为 `33.85% / -14.79% / 1.69 / 2.87` 与 `40.41% / -14.79% / 1.53 / 3.46`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=6 / recommended_focus=risk_overlay_cost / rotate`；下一轮继续比较风险 overlay 成本，但 monthly equal buffered 仍是当前稳健锚点。

## 本轮执行计划（2026-05-16 11:20 CST）

- 本轮独立运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，trade calendar 在线更新失败后按计划回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- HK coverage 仍为 `44/44 complete / pass`，港股结论不并入 A 股 winner；月频数据截止日为 `2026-04-30`，周频观察线数据截止日为 `2026-05-15`。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 收尾 rotation 为 `stagnation_runs=2 / recommended_focus=monthly_weekly_overlay / continue`；下一轮继续比较月频稳健线与周度 overlay 的真实成本，不把纯周度换股并回 Path 1。

## 本轮执行计划（2026-05-16 06:56 CST）

- 本轮独立运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `scripts/update_hkconnect_artifacts.py`；HK coverage 仍为 `44/44 complete / pass`，港股结论不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月频数据截止日为 `2026-04-30`，周频观察线数据截止日为 `2026-05-15`；本轮继续保留月频、双周与周度观察，但纯周度换股仍交给 HK Path 3。
- 收尾 rotation 为 `stagnation_runs=32 / recommended_focus=biweekly_buffer / rotate`；下一轮优先复核双周缓冲与月频稳健线的交易成本，而不是只扩月频邻域。

## 本轮执行计划（2026-05-15 15:16 CST）

- 本轮独立运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- HK coverage 收尾仍为 `pass / blocking=0 / warning=0`，港股结论继续不并入 A 股 winner。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 最终 rotation 为 `stagnation_runs=24 / recommended_focus=risk_overlay_cost / rotate`；下一轮优先评估月频稳健线上的周度风险 overlay 成本，而不是只扩双周缓冲。

## 本轮执行计划（2026-05-15 10:14 CST）

- 本轮独立运行港股五窗口回测，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`，HK coverage 最终仍为 `pass`，港股结论继续不并入 A 股。
- HK Path 1 tracked winners 未变：2017/2023/2025 为 `hkconnect_path1_monthly_equal_buffered`，2020 为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`；最终 rotation 为 `stagnation_runs=22 / biweekly_buffer`。

## 本轮执行计划（2026-05-14 22:55 CST）

- 本轮已完整运行 `backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 并同步 `update_hkconnect_artifacts.py`，HK coverage 收尾仍为 `pass`，港股结论继续独立于 A 股。
- HK Path 1 tracked winners 当前为：2017 `hkconnect_path1_monthly_equal_buffered`（`24.03% CAGR / -23.59% MaxDD / 1.2852 Sharpe / 3.09 Turn`），2020 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`（`31.21% / -14.83% / 1.5210 / 3.52`），2023/2025 仍为 `monthly_equal_buffered`（`33.85% / 40.41% CAGR`）。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`；最终 guard 为 `stagnation_runs=18 / monthly_weekly_overlay`，下一轮继续比较月频稳健线与周度 overlay 的交易成本。

## 本轮执行计划（2026-05-14 15:10 CST）

- 本轮按独立港股线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后同步 `scripts/update_hkconnect_artifacts.py`。
- 收尾 guard 对 HK coverage 为 `pass`，港股候选 `44` 个五窗口完整；HK Path 1 rotation 为 `stagnation_runs=13 / recommended_focus=biweekly_buffer`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 下一轮按 `biweekly_buffer` 比较双周缓冲在真实信号生效日与交易成本下的稳定性；继续保留月频、双周与周度观察，但不把纯周度换股候选并回 Path 1。

## 本轮执行计划（2026-05-14 09:13 CST）

- 本轮按独立港股线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后同步 `scripts/update_hkconnect_artifacts.py`。
- 收尾 guard 对 HK coverage 为 `pass`，港股候选 `44` 个五窗口完整；HK Path 1 rotation 为 `stagnation_runs=11 / recommended_focus=monthly_weekly_overlay`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 下一轮继续在月频稳健线上比较周度 overlay 的真实成本与信号生效日，不把纯周度换股候选并回 Path 1。

## 本轮执行计划（2026-05-14 03:17 CST）

- 本轮继续离线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后同步 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03%`。
- 收盘 guard 将 HK Path 1 rotation 推进到 `stagnation_runs=9 / recommended_focus=monthly_weekly_overlay`；下一步继续比较月频稳健线上的周度 overlay 成本，不把纯周度换股候选并回 Path 1。

## 本轮执行计划（2026-05-13 21:21 CST）

- 本轮继续离线运行 HK 五窗口回测并同步 `scripts/update_hkconnect_artifacts.py`；`trade_calendar` 在线更新失败后使用本地缓存，港股 tracked payload 仍为 `as_of=2026-05-08`。
- 港股 Path 1 winner 身份未漂移：`since_2017_01 / since_2023_01 / since_2025_01` 仍为 `hkconnect_path1_monthly_equal_buffered`，`since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`。
- 最新指标为：2017 `24.03% CAGR / -23.59% MaxDD / 1.2852 Sharpe / 3.09 Turnover`；2020 `31.21% / -14.83% / 1.5210 / 3.52`；2023 `33.85% / -14.79% / 1.6907 / 2.87`；2025 `40.41% / -14.79% / 1.5271 / 3.46`。
- 四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- rotation 已提示下一轮港股 Path 1 转向 `risk_overlay_cost`；继续保留月频、双周和周频观察，但不把港股结论并入 A 股 winner。

## 本轮执行计划（2026-05-13 09:13 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后继续回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日仍为 `2026-05-08`；本轮同步了 month-end preview 相关 live/export 产物，但 preview 不进入正式 winner 或 robust candidate 规则。

## 本轮执行计划（2026-05-13 03:32 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后继续回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 winner 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；双周与周频候选继续保留，当前双周线未改写 tracked Path 1 winner。

## 本轮执行计划（2026-05-12 21:20 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；月度、双周与周度观察候选继续保留。

## 本轮执行计划（2026-05-12 09:12 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；月度、双周与周度观察候选继续保留。

## 本轮执行计划（2026-05-12 03:16 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；月度、双周与周度观察候选继续保留。

## 本轮执行计划（2026-05-11 21:22 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度数据截止日仍为 `2026-04-30`，周频观察线数据截止日为 `2026-05-08`；月度、双周与周度观察候选继续保留，纯周度路线不回并到 Path 1 稳健线。

## 本轮执行计划（2026-05-11 15:15 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`。
- 月度、双周与周度观察候选继续保留；纯周度路线仍交给港股 Path 3，不回并到 Path 1 稳健线。

## 本轮执行计划（2026-05-11 09:19 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，港股结论继续不并入 A 股 winner。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`。
- 月度、双周与周度观察候选继续保留；纯周度路线仍交给港股 Path 3，不回并到 Path 1 稳健线。

## 本轮执行计划（2026-05-11 03:13 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，纯周度候选继续交给港股 Path 3，不并入 A 股结论。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`。

## 本轮执行计划（2026-05-10 21:14 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`；Path 1 身份未漂移，纯周度候选继续交给港股 Path 3，不并入 A 股结论。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`。

## 本轮执行计划（2026-05-10 15:04 CST）

- 本轮运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `scripts/update_hkconnect_artifacts.py`。
- 港股 tracked payload 仍为 `as_of=2026-05-08`，本轮 Path 1 身份未漂移；纯周度候选继续交给港股 Path 3，不并入 A 股结论。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`；四窗口 robust candidate 仍为 `hkconnect_path1_monthly_equal_buffered`。

## 本轮执行计划（2026-05-10 09:17 CST）

- 本轮运行 `.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`；港股 tracked payload 和三张图表与上轮相比无文件漂移。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 继续只保留实盘稳健线的月度/双周候选，纯周度候选留在独立 Path 3。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`。
- 四窗口 robust candidate 仍是 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`；`since_2026_01` 继续只作为观察窗。

## 本轮执行计划（2026-05-10 03:16 CST）

- 本轮继续以港股三路径拆分口径运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后按计划回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 继续只保留实盘稳健线的月度/双周候选，纯周度候选留在独立 Path 3。
- `since_2017_01 / since_2023_01 / since_2025_01` winner 仍为 `hkconnect_path1_monthly_equal_buffered`，关键指标分别为 `24.03% / -23.59% / 1.2852 / 3.09`、`33.85% / -14.79% / 1.6907 / 2.87`、`40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2020_01` 本轮切到 `hkconnect_path1_monthly_equal_buffered_weekly_overlay`，`31.21% CAGR / -14.83% MaxDD / 1.5210 Sharpe / 3.52 Turnover`，高于纯月度等权缓冲且仍保持稳健线口径。
- 四窗口 robust candidate 仍是 `hkconnect_path1_monthly_equal_buffered`，`meanCAGR=32.07% / minCAGR=24.03% / worstMaxDD=-23.59% / meanTurn=3.11`；`since_2026_01` 只观察，当前 Path 1 raw leader 是 `hkconnect_path1_biweekly_lowvol`（`24.45% CAGR / -1.95% MaxDD / 2.6064 Sharpe / 4.87 Turnover`）。

## 本轮执行计划（2026-05-09 21:14 CST）

- 本轮继续以港股三路径拆分口径运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- Path 1 继续只保留实盘稳健线的月度/双周候选；纯周度候选保持迁移到独立 Path 3。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01` 与四窗口 robust candidate 全部统一到 `hkconnect_path1_monthly_equal_buffered`。
- 关键指标：`since_2020_01` 为 `24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，`since_2023_01` 为 `33.85% / -14.79% / 1.6907 / 2.87`，`since_2025_01` 为 `40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2026_01` 只观察，当前 Path 1 raw leader 仍是 `hkconnect_path1_biweekly_lowvol`；本轮 HK Path 3 有新周频 winner，但不并回 Path 1。

## 本轮执行计划（2026-05-09 18:09 CST）

- 本轮继续以港股三路径拆分口径运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- Path 1 继续只保留实盘稳健线的月度/双周候选；原单周换股候选保持迁移到独立 Path 3。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01` 与四窗口 robust candidate 全部统一到 `hkconnect_path1_monthly_equal_buffered`。
- 关键指标：`since_2020_01` 为 `24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，`since_2023_01` 为 `33.85% / -14.79% / 1.6907 / 2.87`，`since_2025_01` 为 `40.41% / -14.79% / 1.5271 / 3.46`。
- `since_2026_01` 只观察，当前 Path 1 raw leader 是 `hkconnect_path1_biweekly_lowvol`；下一轮继续围绕“月度调仓 + 周度风控/卫星”，不把纯周度 winner 并回稳健线。

## 本轮执行计划（2026-05-09 三路径拆分）

- 本轮将港股 Path 1 收窄为实盘稳健线：当前候选保留月度/双周稳健族，单周换股候选已迁移到独立 Path 3。
- 重新运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 仍为 `as_of=2026-05-08`；Path 1 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01` 与四窗口 robust candidate 全部统一到 `hkconnect_path1_monthly_equal_buffered`。
- 关键指标：`since_2020_01` 为 `24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，`since_2023_01` 为 `33.85% / -14.79% / 1.6907 / 2.87`，`since_2025_01` 为 `40.41% / -14.79% / 1.5271 / 3.46`。
- 下一轮 Path 1 的新增方向应围绕“月度调仓 + 周度风控/卫星”，而不是把纯周度 winner 重新并回稳健线。

## 本轮执行计划（2026-05-09 13:04 CST）

- 本轮按港股独立线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 继续为 `as_of=2026-05-08`；港股结论继续不并入 A 股 winner，公开快照继续区分数据截止日与真实信号/换股生效日。
- Path 1 `since_2017_01 / since_2020_01` winner 仍是低换手 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，样本截至 `2026-04-30`。
- `since_2023_01` 仍为 `hkconnect_path1_monthly_equal_buffered`，`33.85% CAGR / -14.79% MaxDD / 1.6907 Sharpe / 2.87 Turnover`；`since_2025_01` 仍为 `hkconnect_path1_weekly_equal_buffered`，`44.50% / -13.39% / 1.5761 / 13.14`。
- 四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=31.13% / minCAGR=23.36%`；月频、双周、周频与低波候选继续全部保留。

## 本轮执行计划（2026-05-09 05:08 CST）

- 本轮按港股独立线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 继续为 `as_of=2026-05-08`；港股结论继续不并入 A 股 winner，公开快照继续区分数据截止日与真实信号/换股生效日。
- Path 1 `since_2017_01 / since_2020_01` winner 仍是低换手 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，样本截至 `2026-04-30`。
- `since_2023_01` 仍为 `hkconnect_path1_monthly_equal_buffered`，`33.85% CAGR / -14.79% MaxDD / 1.6907 Sharpe / 2.87 Turnover`；`since_2025_01` 仍为 `hkconnect_path1_weekly_equal_buffered`，`44.50% / -13.39% / 1.5761 / 13.14`。
- 四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=31.13% / minCAGR=23.36%`；月频、双周、周频与低波候选继续全部保留。

## 本轮执行计划（2026-05-08 23:12 CST）

- 本轮按港股独立线运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，`trade_calendar` 在线更新失败后回退本地缓存；随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- tracked payload 同步为 `as_of=2026-05-08`；港股结论继续不并入 A 股 winner，公开快照继续区分数据截止日与真实信号/换股生效日。
- Path 1 `since_2017_01 / since_2020_01` winner 仍是低换手 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`，样本仍截至 `2026-04-30`。
- `since_2023_01` 本轮切到 `hkconnect_path1_monthly_equal_buffered`（`33.85% CAGR / -14.79% MaxDD / 1.6907 Sharpe / 2.87 Turnover`），低换手与 Sharpe 优先于周频缓冲的更高换手收益。
- `since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，但更新到 `2026-05-08` 后为 `44.50% CAGR / -13.39% MaxDD / 1.5761 Sharpe / 13.14 Turnover`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=31.13% / minCAGR=23.36%`。
- 月频、双周、周频与低波候选继续全部保留；本轮不因 2023 窗口月频胜出而停止高频路线观察。

## 本轮执行计划（2026-05-08 17:24 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=33.38% / minCAGR=24.37%`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分数据截止日与真实信号/换股生效日。

## 本轮执行计划（2026-05-08 13:15 CST）

- 本轮继续单独运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，随后运行 `./.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- `trade_calendar` 在线更新失败，已按计划回退本地缓存；tracked payload 继续以 `as_of=2026-04-30` 记录，港股结论不并入 A 股 winner。
- Path 1 tracked winners 未发生结构性切换：`since_2017_01 / since_2020_01` 仍是 `hkconnect_path1_monthly_equal_buffered`，`24.84% CAGR / -14.79% MaxDD / 1.4406 Sharpe / 2.79 Turnover`。
- `since_2023_01 / since_2025_01` 继续是 `hkconnect_path1_weekly_equal_buffered`，分别为 `35.12% CAGR` 与 `49.66% CAGR`；四窗口 robust candidate 仍是 `hkconnect_path1_weekly_equal_buffered`，`meanCAGR=33.38% / minCAGR=24.37%`。
- 月频、双周、周频与低波候选继续全部保留；公开快照继续区分数据截止日与真实信号/换股生效日。

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
## 本轮执行计划（2026-06-01 16:23 CST）

- 上一轮候选/结果摘要：上一轮建议测试 `monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30_v13_risk_overlay`，用于检查 Path 1 月频主线叠加周度仓位与更软风险降仓后，是否能改善 `since_2025_01` 同时不过度损伤长窗。
- 本轮候选 ID：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30_v13_risk_overlay`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30_v13_risk_overlay`。
- 五窗口结果：CAGR 为 `21.64% / 28.64% / 32.03% / 52.56% / -0.50%`，最大回撤为 `-27.03% / -13.04% / -10.86% / -10.86% / -9.29%`，换手为 `3.70x / 3.62x / 3.41x / 3.61x / 4.19x`。
- 结论：`update_hkconnect_artifacts.py` 后 `hkconnect_path1` 发生有效 tracked payload 变化，`since_2025_01` window winner 切到本轮 v13；robust candidate 仍是 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit34`，长窗 winner 没有切换。2026 观察窗转负，说明 v13 不宜直接作为全窗口主线。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay` 且 rotation 为 `continue`。下一轮第一候选建议 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30_v14_ytd_repair`，略放宽风险降仓或恢复确认以修复 2026；首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit30_v14_ytd_repair`。

## 本轮执行计划（2026-06-02 22:30 CST）

- 上一轮候选/结果摘要：上一轮 v17/v13 一类周度 overlay 修复了 `since_2025_01`，但 2026 观察窗转负。本轮继续在 `monthly_weekly_overlay` 下测试 `exit34_v18_drawdown_repair`，目标是保留短窗弹性并控制回撤。
- 本轮候选 ID：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v18_drawdown_repair`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v18_drawdown_repair`。
- 五窗口结果：CAGR 为 `20.31% / 26.41% / 27.13% / 46.51% / -8.02%`，最大回撤为 `-28.68% / -11.82% / -11.82% / -11.82% / -10.70%`，换手为 `3.57x / 3.53x / 3.49x / 3.57x / 4.10x`。
- 结论：`update_hkconnect_artifacts.py` 后 HK Path 1 tracked payload 发生有效变化，`since_2025_01` window winner 切到本轮 v18；但 2017/2020/2023 与 robust candidate 仍分别由旧 `soft_exit32`、`lowvol_cost_guard` 与 `soft_exit32` 占据，v18 的 2026 观察窗仍为负，不宜直接升为全窗口主线。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay` 且 rotation 为 `continue`。下一轮第一候选建议 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v19_ytd_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_cost_guard_exit34_v19_ytd_repair`。

## 本轮执行计划（2026-06-03 12:10 CST）

- 上一轮候选/结果摘要：上一轮 v18 改写了 `since_2025_01`，但 2026 仍为负。本轮在 `monthly_weekly_overlay` 上提高 risk-off exposure 到 `42%`，检查是否能修复 2026 且不丢短窗。
- 本轮候选 ID：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff42_exit34_v19_2026_guard`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff42_exit34_v19_2026_guard`。
- 五窗口结果：CAGR 为 `22.23% / 28.86% / 29.12% / 46.51% / -8.02%`，最大回撤为 `-25.61% / -11.82% / -11.82% / -11.82% / -10.70%`，换手为 `3.21x / 3.22x / 3.24x / 3.57x / 4.10x`。
- 结论：v19 长窗好于 v18，但 2026 仍未修复；`update_hkconnect_artifacts.py` 后 HK Path 1 window winner 与 robust candidate 未改变，`since_2025_01` 仍由 v18 占据，robust 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32`。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> biweekly_buffer`。下一轮第一候选建议转回双周缓冲线而非继续月周小修：`hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit34_v20_buffer`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-05-27 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_equal_buffered_soft_cost_guard_exit34_v20_buffer`。

## 本轮执行计划（2026-06-03 10:35 CST）

- 上一轮候选/结果摘要：上一轮 v19 提高 risk-off exposure 后 2026 仍为负。本轮 guard focus 回到 `monthly_weekly_overlay`，所以测试更低 risk-off exposure `34%` 与 `exit34`，确认月频主线叠加周度仓位能否保住 2025 且减少长窗拖累。
- 本轮候选 ID：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff34_exit34_v20_2026_repair`。增量命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff34_exit34_v20_2026_repair`。
- 五窗口结果：CAGR 为 `20.63% / 26.55% / 26.09% / 39.32% / -15.62%`，最大回撤为 `-27.10% / -11.82% / -11.82% / -11.82% / -10.70%`，换手为 `3.37x / 3.31x / 3.34x / 3.65x / 4.29x`。
- 结论：v20 比 v19 更弱，2026 仍未修复，且未替换 `soft_exit32`、`lowvol_cost_guard` 或 v18 短窗 winner；`update_hkconnect_artifacts.py` 后 HK Path 1 window winner、robust candidate 与 tracked payload 均未改变。HK explore cap 未触发 evict。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay`。下一轮第一候选建议测试更宽恢复/出场而不是继续压 risk-off：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff30_exit36_v21_2026_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff30_exit36_v21_2026_repair`。

## 本轮执行计划（2026-06-04 04:18 CST）

- 上一轮候选/结果摘要：上一轮 v20 降 risk-off 后 2026 更弱。本轮按 `monthly_weekly_overlay` 测试更宽 `exit36` 与更浅 `riskoff28`，目标是修复 2026 但不牺牲 2025 短窗。
- 本轮候选 ID：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff28_exit36_v22_drawdown_repair`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff28_exit36_v22_drawdown_repair,hkconnect_path4_quality_momentum_monthly_2026_repair_v2,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。
- 五窗口结果：CAGR 为 `18.92% / 23.98% / 22.09% / 34.75% / -7.11%`，最大回撤为 `-27.96% / -12.28% / -12.28% / -12.28% / -9.10%`，换手为 `3.33x / 3.30x / 3.31x / 3.60x / 4.30x`。
- 结论：v22 比 v20 的 2026 损失收窄，但长中短窗均弱于现有 `soft_exit32`、`lowvol_cost_guard` 和旧短窗 winner；`update_hkconnect_artifacts.py` 后 HK Path 1 window winner 与 robust candidate 未改变，tracked payload 仅随 HK 图表/策略列表同步。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> risk_overlay_cost`。下一轮不要继续月周 overlay 小修，第一候选建议做风险 overlay 成本修复：`hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair`。

## 本轮执行计划（2026-06-08 06:05 CST）

- 上一轮候选/结果摘要：上一轮月周 overlay 小修未修复 2026，本轮按 `biweekly_buffer` 确认双周质量动量等权缓冲线，而不是继续在月频 risk-off 上微调。
- 本轮候选 ID：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v24`；随后 `tracked_active` 又用同五窗口同步 HK active 集合。
- 五窗口结果：CAGR 为 `21.90% / 24.63% / 29.40% / 34.63% / -2.03%`，最大回撤为 `-21.30% / -21.30% / -9.70% / -8.31% / -5.78%`，换手为 `5.39x / 5.13x / 5.06x / 6.30x / 5.97x`。
- 结论：v24 是 2017 窗口表头观察，但 2026 转负且最终 guard 对 `hkconnect_path1` signature 未标记 changed；`update_hkconnect_artifacts.py` 后 Path 1 robust candidate/tracked payload 未发生本轮新切换。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> biweekly_buffer`。下一轮第一候选建议 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v25_ytd_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v25_ytd_repair`。

## 本轮执行计划（2026-06-08 12:13 CST）

- 上一轮候选/结果摘要：上一轮 v24 双周缓冲线长窗靠前但 2026 转负；本轮继续按 `biweekly_buffer` 做 YTD repair，保持 HK Path 1 不并入 A股结论。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v25_ytd_repair`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v25_ytd_repair`。
- 五窗口结果：CAGR `22.61% / 25.63% / 29.11% / 35.42% / -3.64%`，最大回撤 `-21.05% / -21.05% / -10.13% / -8.30% / -5.77%`，换手 `5.42x / 5.17x / 5.11x / 6.35x / 5.97x`。
- 结论：v25 改善长窗并成为 `since_2017_01` 表头观察，但 2026 仍负；`update_hkconnect_artifacts.py` 后 HK Path 1 robust candidate 未改写，tracked payload 仅随候选列表和图表同步。
- 下一轮 focus：继续 `biweekly_buffer / risk_overlay_cost`，第一候选建议 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard`。

## 本轮执行计划（2026-06-08 17:37 CST）

- 上一轮候选/结果摘要：上一轮 v25 长窗靠前但 2026 仍负；本轮按 `biweekly_buffer` 做 v26 年内正收益守门，保持 HK Path 1 独立于 A股。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v26_ytd_positive_guard`。
- 五窗口结果：CAGR `22.14% / 24.20% / 28.21% / 36.85% / -6.53%`，最大回撤 `-21.34% / -21.34% / -10.72% / -6.88% / -5.77%`，换手 `5.30x / 5.10x / 5.05x / 6.00x / 6.21x`。
- 结论：v26 没有修复 2026，且低于 v25 长窗；`update_hkconnect_artifacts.py` 后 HK Path 1 winner/robust/tracked payload 未改写。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> biweekly_buffer`。下一轮建议停止单纯提高防守暴露，改测 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v27_recovery_guard`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v27_recovery_guard`。

## 本轮执行计划（2026-06-08 23:27 CST）

- 上一轮候选/结果摘要：上一轮 v26 没有修复 2026；本轮改用 `risk_overlay` 降低风险段暴露，测试是否能保住长窗同时修复年内负收益。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v27_risk_overlay`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v27_risk_overlay`。
- 五窗口结果：CAGR `22.48% / 24.76% / 27.75% / 34.34% / -6.60%`，最大回撤 `-21.44% / -21.44% / -10.71% / -7.61% / -5.78%`，换手 `5.32x / 5.14x / 5.08x / 5.98x / 6.22x`。
- 结论：v27 长窗接近 v25/v26，但 2026 仍负，HK Path 1 winner/robust/tracked payload 未改变；`update_hkconnect_artifacts.py` 已同步 comparison 与图表。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay`。下一轮第一候选建议从双周切到月选周控：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v28_cost_guard`，首条命令为 `.venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v28_cost_guard`。

## 本轮执行计划（2026-06-09 04:20 CST）

- 上一轮候选/结果摘要：上一轮双周 v27 仍未修复 2026；本轮按计划切到月选周控的质量/动量 overlay，保持 HK Path 1 独立于 A股结论。
- 本轮候选 ID 与命令：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v28_cost_guard`。实际 HK 合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v28_cost_guard,hkconnect_path2_high_return_monthly_quality_liquidity_v27_cost_guard,hkconnect_path3_theme_fast_weekly_defensive_turnover5_exit56_v12_cost_guard,hkconnect_path4_liquidity_momentum_biweekly_quality_lowdraw_v12_quality_filter,hkconnect_path6_large_liquid_core_monthly_quality_liquidity_lowturn_v12_cost_cap,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_lowturn_v12`。
- 五窗口结果：CAGR `19.95% / 26.19% / 28.82% / 37.93% / -10.64%`，最大回撤 `-25.22% / -10.76% / -10.76% / -11.07% / -10.75%`，换手 `3.60x / 3.48x / 3.32x / 3.51x / 4.42x`。
- 结论：v28 风险调整可用，但 2026 仍负且长窗不优于现有 HK Path 1 robust；`update_hkconnect_artifacts.py` 与 `tracked_active` 同步后，Path 1 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> biweekly_buffer`。下一轮第一候选建议回到双周缓冲但加入恢复确认：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v29_recovery_guard`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v29_recovery_guard`。

## 本轮执行计划（2026-06-09 20:05 CST）

- 上一轮候选/结果摘要：上一轮月选周控 v28 仍未修复 2026；本轮按 `biweekly_buffer` 回到双周质量动量等权缓冲，并加入恢复确认。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v29_recovery_guard`；实际 HK 合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <five_hk_new_ids>`。
- 五窗口结果：CAGR `20.29% / 22.02% / 23.96% / 30.33% / -10.96%`，最大回撤 `-21.16% / -19.98% / -11.58% / -7.95% / -6.53%`，换手 `5.22x / 5.07x / 5.10x / 6.19x / 6.42x`。
- 结论：v29 长中窗不优于现有 `monthly_equal_buffered_weekly_overlay_soft_exit32` 与 `biweekly_lowvol` robust，2026 仍为负；`update_hkconnect_artifacts.py` 后 HK Path 1 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> risk_overlay_cost`。下一轮第一候选建议在双周质量动量线上直接做风险 overlay 成本修复：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v30_risk_overlay_cost_guard`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v30_risk_overlay_cost_guard`。

## 本轮执行计划（2026-06-09 22:26 CST）

- 上一轮候选/结果摘要：上一轮 v29 双周质量动量仍未修复 2026；本轮按 `risk_overlay_cost` 加入更低 risk-off exposure、caution exposure 和单票上限，检查能否降低回撤和成本压力。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v30_risk_overlay_cost_guard`；实际 HK 合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <three_hk_new_ids>`。
- 五窗口结果：CAGR `20.23% / 22.01% / 23.84% / 30.33% / -10.96%`，最大回撤 `-20.85% / -19.98% / -11.58% / -7.95% / -6.53%`，换手 `5.22x / 5.06x / 5.09x / 6.19x / 6.42x`。
- 结论：v30 回撤略低但收益低于现有月周 overlay winner 与 `biweekly_lowvol` robust，2026 仍为负；`update_hkconnect_artifacts.py` 后 HK Path 1 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay`。下一轮停止双周质量动量小修，回到月选周控：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v31_ytd_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v31_ytd_repair`。

## 本轮执行计划（2026-06-10 04:41 CST）

- 上一轮候选/结果摘要：上一轮 v30 双周质量动量仍未修复 2026；本轮按 `monthly_weekly_overlay` 回到月选周控，并加入 YTD 修复约束。
- 本轮候选 ID 与命令：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v31_ytd_repair`；实际 HK 合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <seven_hk_incremental_ids>`。
- 五窗口结果：CAGR `18.45% / 23.88% / 26.19% / 36.79% / -8.94%`，最大回撤 `-27.80% / -10.82% / -8.86% / -8.97% / -9.04%`，换手 `3.56x / 3.45x / 3.27x / 3.42x / 4.29x`。
- 结论：v31 中长窗仍有竞争力，但 2026 仍为负且不优于当前 HK Path 1 winner/robust；`update_hkconnect_artifacts.py` 后 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> biweekly_buffer`。下一轮第一候选建议回到双周 buffer，测试低波/缓冲是否比 v31 月周 overlay 更能修复 2026：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v31_buffer_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v31_buffer_repair`。

## 本轮执行计划（2026-06-10 10:40 CST）

- 上一轮候选/结果摘要：上一轮 v31 月周 overlay 未修复 2026；本轮按 `biweekly_buffer` 回到双周质量动量等权缓冲，测试低波/缓冲结构能否改善 2026。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v31_buffer_repair`；实际 HK 合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <seven_hk_incremental_ids>`。
- 五窗口结果：CAGR `20.00% / 22.29% / 24.07% / 35.53% / -11.28%`，最大回撤 `-21.43% / -19.59% / -11.98% / -6.68% / -6.45%`，换手 `4.97x / 4.81x / 4.81x / 5.72x / 6.27x`。
- 结论：v31 buffer 长中窗可用，但 2026 仍显著为负；`update_hkconnect_artifacts.py` 后 HK Path 1 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay`。下一轮第一候选建议回到月选周控而不是继续双周小修：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v32_ytd_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v32_ytd_repair`。

## 本轮执行计划（2026-06-10 16:31 CST）

- 上一轮候选/结果摘要：上一轮 v31 月周 overlay 未修复 2026；本轮执行 v32，把 `risk_off=0.16 / caution=0.68 / exit38 / max_holdings24 / cap7%` 作为 YTD 修复对照。
- 本轮候选 ID 与命令：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v32_ytd_repair`；路径首命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v32_ytd_repair`。
- 五窗口结果：CAGR `18.13% / 23.25% / 24.19% / 33.25% / -7.55%`，最大回撤 `-28.16% / -10.94% / -10.94% / -10.67% / -10.14%`，换手 `3.45x / 3.36x / 3.23x / 3.39x / 4.19x`。
- 结论：v32 仍未修复 2026，且长中窗低于现有 Path1 winner/robust；`update_hkconnect_artifacts.py` 后 HK Path1 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> biweekly_buffer`。下一轮第一候选建议回到双周质量动量缓冲，并只做一次 YTD repair：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v32_ytd_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v32_ytd_repair`。

## 本轮执行计划（2026-06-11 05:45 CST）

- 上一轮候选/结果摘要：上一轮 v32 月周 overlay 仍未修复 2026；本轮回到双周质量动量等权缓冲，并只做一次 YTD repair，保持 HK Path 1 独立于 A股结论。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v32_ytd_repair`；实际 HK 合并命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids <seven_hk_incremental_ids>`。
- 五窗口结果：CAGR `19.22% / 21.03% / 21.77% / 32.48% / -11.95%`，最大回撤 `-21.24% / -19.43% / -11.56% / -8.50% / -6.37%`，换手 `4.70x / 4.57x / 4.60x / 5.36x / 5.73x`。
- 结论：v32 双周线长中窗低于现有 HK Path1 winner/robust，且 2026 更弱；`update_hkconnect_artifacts.py` 后 window winner、robust candidate 与 tracked payload 未改变。最终 guard 显示 `hkconnect_path1 -> risk_overlay_cost / rotate`，停滞计数仍高。
- 下一轮 focus：下一轮第一候选建议在双周质量动量线上只做一次风险 overlay 成本修复：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v33_risk_overlay_cost_guard`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v33_risk_overlay_cost_guard`；若 2026 仍显著为负，回到低波 robust 而不是继续质量动量小修。

## 本轮执行计划（2026-06-11 16:10 CST）

- 上一轮候选/结果摘要：上一轮留下双周质量动量 `v33_risk_overlay_cost_guard`；本轮按 HK Path 1 独立口径执行五窗口增量，不并入 A股 winner 结论。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v33_risk_overlay_cost_guard`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v33_risk_overlay_cost_guard,hkconnect_path2_theme_biweekly_cost_guard_v31_breakout_lowturn_repair,hkconnect_path3_stable_weekly_equal_buffered_cost_guard_turnover2_exit40_v8_lowturn_repair`。
- 五窗口结果：CAGR `18.22% / 20.40% / 20.43% / 31.30% / -12.70%`，最大回撤 `-22.63% / -19.88% / -11.42% / -9.19% / -6.70%`，换手 `4.60x / 4.43x / 4.52x / 5.32x / 5.72x`。
- 结论：v33 长中窗继续低于现有 HK Path 1 winner/robust，2026 仍明显为负；`scripts/update_hkconnect_artifacts.py` 后 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> biweekly_buffer`。下一轮第一候选建议回到双周缓冲但加入低波/YTD 修复：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v34_lowvol_ytd_repair`，首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v34_lowvol_ytd_repair`；若未注册，先只增加这一条。

## 本轮执行计划（2026-06-25 21:16 CST）

- 上一轮候选/结果摘要：本轮 HK Path 1 没有新增 strategy id，按沪港通独立研究线完成 tracked_active 刷新与 artifact 同步，不并入 A股 winner 结论。
- 本轮命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 与 `.venv/bin/python scripts/update_hkconnect_artifacts.py`。增量 budget 让给 HK Path 2 与 Path 7。
- 结论：HK Path 1 window winner、robust candidate、tracked payload 未改变；最终 guard 给出 `hkconnect_path1 -> rotate / risk_overlay_cost`，长期停滞仍需风险/成本 overlay 方向，而不是扩月频旧线。
- 下一轮 focus：第一候选建议从上一轮 v34 低波修复改成更直接的 risk overlay/cost guard：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v34_risk_overlay_cost_guard`；首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v34_risk_overlay_cost_guard`。

## 本轮执行计划（2026-06-26 09:46 CST）

- 上一轮候选/结果摘要：上一轮 HK Path 1 留下 `v34_risk_overlay_cost_guard`；本轮实际新增 `hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard`，并在 public stale preview 后把 HK `tracked_active` 刷新到 2026-06-25。
- 本轮候选 ID 与命令：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard`；增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v44_risk_overlay_cost_guard,<hk_path2_v44>,<hk_path3_v21>`，随后执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-25 --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 五窗口结果：CAGR `16.70% / 18.24% / 18.42% / 35.01% / -1.65%`，最大回撤 `-19.66% / -17.66% / -11.67% / -9.65% / -4.40%`，换手 `3.95x / 3.85x / 4.02x / 4.75x / 4.92x`。
- 结论：v44 回撤可控但 2026 仍为负，且长中窗低于现有 HK Path1 robust `hkconnect_path1_biweekly_lowvol`；`update_hkconnect_artifacts.py` 后 window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay`。下一轮第一候选建议回到月选周控修复，而不是继续双周质量动量小修：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v45_monthly_weekly_repair`；首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v45_monthly_weekly_repair`。

## 本轮执行计划（2026-06-26 20:46 CST）

- 上一轮候选/结果摘要：上一轮留下月选周控 v45，本轮按 HK Path 1 独立研究线执行，不并入 A股 winner 结论；HK `tracked_active` 已刷新并同步 artifact。
- 本轮候选 ID 与命令：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v45_monthly_weekly_repair`；增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v45_monthly_weekly_repair,hkconnect_path2_equal_elastic_monthly_cost_guard_v45_elasticity_cost_control,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff40_turnover0_exit56_v22_cost_stress`，随后执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-25 --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- 五窗口结果：CAGR `17.82% / 22.65% / 23.15% / 33.73% / -10.71%`，最大回撤 `-27.57% / -11.35% / -10.44% / -10.34% / -10.08%`，换手 `3.34x / 3.26x / 3.16x / 3.29x / 3.99x`。
- 结论：v45 长中窗仍可用，但 2026 显著为负，未改变 HK Path 1 window winner、robust candidate 或 tracked payload；robust 仍为 `hkconnect_path1_biweekly_lowvol`。本轮没有 HK Path1 evict。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay`。下一轮第一候选建议继续月选周控但加入更硬 YTD guard：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v46_ytd_guard`；首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v46_ytd_guard`。

## 本轮执行计划（2026-06-27 07:44 CST）

- 上一轮候选/结果摘要：上一轮留下月选周控 v46，但本轮新增预算投给 HK Path2 与 Path4/6/7；HK Path 1 完成 tracked_active 与 public stale preview 修复，不并入 A股 winner 结论。
- 本轮候选 ID 与命令：本轮没有新增 HK Path 1 strategy id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，并为 public snapshot 补刷 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_cost_guard_exit30_v11_repair` 五窗口。
- v11 同步结果：CAGR `17.72% / 22.55% / 29.26% / 25.40% / -12.44%`，最大回撤 `-22.37% / -11.42% / -10.67% / -10.09% / -9.22%`。这是 stale preview 修复，不计作新增策略实验。
- 结论：`scripts/update_hkconnect_artifacts.py` 后 HK Path 1 window winner、robust candidate 与 tracked payload 未改变；本轮没有 HK Path1 evict。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> risk_overlay_cost`。下一轮第一候选建议回到双周缓冲并加入更硬 risk overlay/cost guard：`hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard`；首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_biweekly_quality_momentum_equal_buffered_v46_risk_overlay_cost_guard`。若未注册，先只加入该一个 HK Path1 variant。

## 本轮执行计划（2026-07-02 07:00 CST）

- 上一轮候选/结果摘要：上一轮留下 `v46_risk_overlay_cost_guard`，但本轮 HK 新增预算投给 Path2/3；HK Path1 完成 tracked_active、artifact、public/live 同步，不并入 A股 winner 结论。
- 本轮候选 ID 与命令：本轮没有新增 HK Path1 strategy id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path2_theme_biweekly_quality_liquidity_breakout_v51_elasticity_cost_control,hkconnect_path3_stable_weekly_equal_buffered_soft_riskoff36_turnover0_exit50_v27_cost_stress`、`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 与 `.venv/bin/python scripts/update_hkconnect_artifacts.py`。
- 巡检结果：最终 tracked winners 中 Path1 仍为 `hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_exit32`（2017/2020）、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_lowvol_soft_exit34`（2023）、`hkconnect_path1_monthly_equal_buffered_weekly_overlay_quality_lowvol_mix_v39_ytd_risk_repair`（2025）、`hkconnect_path1_biweekly_lowvol`（2026 与 robust）。robust mean CAGR `14.85%`、min CAGR `-3.28%`。
- 结论：HK Path1 window winner、robust candidate 与 tracked payload 未改变；本轮没有 HK Path1 evict。同步产生的 comparison/public detail 更新属于 refresh，不计作新增策略实验。
- 下一轮 focus：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay`。下一轮第一候选建议回到月选周控并加入 YTD/低波过滤，而不是继续双周质量动量小修：`hkconnect_path1_monthly_quality_momentum_weekly_overlay_v52_monthly_weekly_ytd_guard`；首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-06-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v52_monthly_weekly_ytd_guard`。

## 本轮执行计划（2026-07-03 07:23 CST）

- 上一轮候选/结果摘要：上一轮留下 `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v52_monthly_weekly_ytd_guard`；本轮开局 guard pass，新增 HK 预算优先给 Path3 与 Path4/6/7，Path1 完成巡检、tracked_active、artifact、live/public 同步，不并入 A股 winner 结论。
- 本轮候选 ID 与命令：本轮未跑新增 HK Path1 strategy id，原因是 `v52_monthly_weekly_ytd_guard` 当前未在可执行候选集合中注册；执行了 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-07-02 --family-scope tracked_active --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`、`.venv/bin/python scripts/update_hkconnect_artifacts.py`、`.venv/bin/python scripts/export_live_platform_data.py` 与 `.venv/bin/python scripts/generate_public_snapshot.py`。
- 巡检结论：HK Path1 window winner、robust candidate 与 tracked payload 未因本轮新增实验改变；comparison/public/live 的更新属于同步，不计作新增策略实验。本轮没有 HK Path1 evict。
- 下一轮 focus：先注册 `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v52_monthly_weekly_ytd_guard`，再执行首条命令 `.venv/bin/python backtest_hkconnect.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v52_monthly_weekly_ytd_guard`；若注册成本高，则改确认一个已注册的月周 overlay YTD/低波相邻候选。

## 本轮执行计划（2026-07-07 05:01 CST）

- 上一轮候选/结果摘要：上一轮留下 `v52_monthly_weekly_ytd_guard` 但未注册。本轮开局 guard pass，新增/确认预算优先投给 A股 Path1/2/3/4 与 Path5 入口；HK Path1 完成巡检和下一轮候选设计，不并入 A股 winner 结论。
- 本轮候选 ID 与命令：本轮未跑新增 HK Path1 strategy id；未跑原因是本轮已执行 7 个 A股 strategy/base ids 与 1 个 Path5 event entry，且 HK 无 blocking coverage。HK tracked/live/public 同步将在收尾由 artifact/export/snapshot 统一处理。
- 巡检结论：最终 guard 给出 `hkconnect_path1 -> monthly_weekly_overlay / rotate / stagnation_runs=9`。HK Path1 window winner、robust candidate 与 tracked payload 未因本轮新增实验改变；本轮没有 HK Path1 evict。
- 下一轮 focus：若 `v52` 仍未注册，先跑已注册的月周 overlay 相邻候选 `hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay`；首条命令为 `.venv/bin/python backtest_hkconnect.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_quality_momentum_weekly_overlay_v48_monthly_weekly_overlay`。若下一轮能注册 v52，则用 v52 替换该命令。
