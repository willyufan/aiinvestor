# Path 1 研究计划

本文档用于约束和记录 `Path 1`（胜出者核心主线）的研究方向。  
目标不是无约束追求收益上限，而是在保持框架可交易、可复用、可解释的前提下，把当前常见的 `20%~26% CAGR` 推向 `25%~30%+ CAGR`。  
当前已把 `Path 1` 的单轮探索预算提升到 **`8-12` 个候选 / `3-5` 个方向**，并要求候选按方向分组生成，而不是只做参数邻域微调。

## 1. 当前目标

- 路线：`Path 1` 渐进优化
- 主目标：
  - 把 `2017 / 2020 / 2023 / 2025` 四个窗口里的主力版本继续往上推
  - 优先改进 `2020` 和 `2023` 两个窗口
  - 不明显恶化 `Max DD / Sharpe / Turnover`
- 当前研究原则：
  - 尽量不破坏现有 `winner_core` 主线
  - 优先动系统风险层、晋升节奏、卫星仓行为
  - 每次迭代固定试 `3-5` 个有明确假设的方向
  - 单轮快筛候选预算控制在 `8-12` 个

## 2. 当前主线假设

当前 `Path 1` 的核心假设如下：

1. `winner_core` 主线仍然是有效框架，问题不在于“是否保留 winner_core”，而在于“如何更早、更平滑地把强者放大”。
2. 周频系统风险覆盖层如果直接作用于整个组合，通常会伤害收益；但如果只作用于卫星仓，则更有希望改善收益-回撤比。
3. 卫星仓三档风控（`100 / 60 / 30`）优于简单两档，且在进攻主线上配合更少触发次数会进一步改善结果。
4. `cash_off` 线更偏防守，继续叠加太多额外确认逻辑，边际收益有限；更适合保留为防守候选，而不是主攻优化对象。
5. Path 1 的优化应该优先来自：
   - 卫星仓风控
   - 晋升核心后的加仓节奏
   - 触发机制的节奏控制
   而不是频繁改动股票池或彻底换框架。

## 3. 当前默认候选生成

当前 `Path 1` 快速迭代不是扫全部 `winner_core` 变体，而是从显式候选方向组中生成。  
当前默认是 **`5` 个方向组 / `12` 个 fast-pass 候选**（以 `backtest_marketcap_etf.py` 中 `PATH1_FAST_PASS_DIRECTION_GROUPS / PATH1_FAST_PASS_VARIANT_IDS` 为准）：

1. `promotion_ramp`
   - `aggr_10_90_fast_ramp`
   - `aggr_10_90_prom6`
   - `aggr_10_90_prom7_ramp90`
2. `satellite_defense`
   - `aggr_08_92_prom6_cash_off`
   - `aggr_08_92_prom6_cash_off_and`
   - `aggr_10_90_fast_ramp_cash_off`
3. `signal_variants`
   - `aggr_08_92_prom6_core_6_1`
   - `aggr_10_90_prom6_core_6_1`
4. `holding_shape`
   - `share_15_85_hold_4_6`
   - `aggr_09_91_prom7`
5. `supporting_variants`
   - `aggr_08_92_prom6`
   - `aggr_08_92_prom6_ramp90`

说明：

- 这组候选是“Path 1 fast pass”的研究入口，不代表全部可用策略。
- 正式确认回测仍然可以扩展到更宽的 `research active family`。
- 如果某一轮出现更优的 companion 版本（例如卫星风控 companion），可以追加进入 fast pass 候选，但应写明加入原因。
- 每轮不要求 12 个候选都进入完整确认；fast pass 的职责是先筛出每个方向里最值得晋级的 `1-2` 个。

## 4. 下一轮优先尝试的方向（每轮 3-5 个）

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
- 扫描范围（fast pass + 卫星 overlay）：`base_candidates=13 / total_candidates=52 / evaluated=26`。
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
