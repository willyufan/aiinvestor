# Path 2 研究计划

本文档用于约束和记录 `Path 2`（无约束上限探索）的研究方向。  
`Path 2` 的目标不是延续 `Path 1` 的稳健改良逻辑，而是作为**独立路线**去追求更高收益上限，优先冲击：

- `since_2020_01` 窗口 `40%+ CAGR`
- `since_2023_01` 窗口 `40%+ CAGR`

在这个阶段，`Path 2` 不要求先打赢 `Path 1` 才记录，也不要求先把回撤压到与 `Path 1` 同级；它的优先级是：

1. 先做出显著更高的收益上限
2. 再讨论如何把极端回撤收回来

当前已把 `Path 2` 的单轮探索预算提升到 **`24-36` 个显式原型 / `5` 条独立候选族**，并把 family-ranked 候选宇宙扩到 **`100+`** 规模；每条候选族固定保留 `4-6` 个代表候选。

## 本轮执行计划（2026-04-28）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点仍是维持 `100+` family-ranked universe，并优先观察是否出现更适配 `since_2020_01` 的中周期高收益原型；若无 winner 改写，只同步记录扫描结果。

### 本轮快筛记录（2026-04-28 00:06 CST）

- 运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数 `103`，五个 family 规模继续为 `43 / 23 / 16 / 4 / 4`。
- 四窗口 tracked winner 与 robust candidate 的身份未改写，只出现缓存指标小幅漂移：`since_2020_01` winner 仍是 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（CAGR `32.07%`），`robust` 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 当前 `since_2020_01` 仍未冲到 `40%+ CAGR`，下一轮继续优先寻找更适配 2020 的中周期高收益原型，而不是扩大高频候选权重。

## 1. 当前目标

- 路线：`Path 2` 无约束上限探索
- 主目标：
  - 优先提升 `2020 / 2023` 两个窗口的 CAGR
  - 保持 `2025` 超短窗口仍然具备爆发力
  - 允许比 `Path 1` 更高的集中度、更激进的持仓与风控
- 现实检查（基于当前缓存结果）：截至 `2026-04-21`，`since_2020_01` 窗口在现有策略家族里的上限约 `~35.85% CAGR`，要冲击 `40%+` 仍需要新增更激进且更独立的候选族（或更激进的信号/约束组合），并针对 `since_2020_01` 补跑小批量回测。
- 当前研究原则：
  - 不受 `winner_core` 主线约束
- 每次迭代固定覆盖 `5` 条独立候选族
  - 每条候选族内部保留 `4-6` 个有代表性的候选
  - 单轮显式原型预算控制在 `24-36` 个，family-ranked universe 目标保持在 `100+`

## 2. 当前主线假设

当前 `Path 2` 的核心假设如下：

1. 想把 `2020 / 2023` 推到 `40%+ CAGR`，不能只在 `Path 1` 的约束框架里微调，必须允许更高集中和更激进的候选。
2. 真正高收益候选，往往会在：
   - 等权或弱底座结构
   - 更短周期趋势/突破信号
   - 更强行业主线
   - 更高单票上限
   这些方向里出现。
3. `Path 2` 的候选生成应以“独立候选族”为单位推进，而不是从 `Path 1` 结果里被动捡赢家。
4. 在当前阶段，`Path 2` 的最大问题不是收益不够激进，而是：
   - 候选族还不够真正独立
   - 高收益版本的回撤往往过深
   - 还没有形成一套“高收益但可持续迭代”的研究体系
5. 单纯把月度调仓提升到双周/单周，并不足以自动改善 `since_2020_01`；下一轮新增探索强度应优先投向更适配 `2020` 的中周期高收益原型，而不是继续平均强化 `2023 / 2025`。
6. 候选族归类必须使用更严格的“显式 variant + 窄 prefix”规则，避免宽前缀匹配把不同家族压到一起，削弱代表候选的独立性。

## 3. 当前独立候选族

目前 `Path 2` 已经开始用独立候选扫描逻辑，当前重点拆成五类候选族：

### A. 高集中突破

特点：

- 更少持仓
- 更高单票上限
- 更强调突破、加速、趋势延续
- 更适合牛市或强主线阶段

当前代表方向（目标 `4-6` 个）：

- `aggr_05_95_prom3_core_6_1_full_risk`
- `aggr_05_95_prom3_core_6_1_full_risk_cap60`
- `aggr_05_95_prom3_core_6_1_cap60`
- `aggr_05_95_prom3_core_6_1_cash_off_and_cap60`

近期新增的 bridging 原型（用于验证“更高集中 + 明确 risk-off”是否能改善 `since_2020_01`）：

- `aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
- `aggr_03_97_prom2_core_6_1_cash_off_and_risk30_cap80`
- `aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`

### B. 高成长主线

特点：

- 更强调行业主线、成长加速、龙头放大
- 倾向于更早切入高成长方向
- 容忍更高波动

当前代表方向（目标 `4-6` 个）：

- `aggr_08_92_prom6_full_risk`
- `aggr_08_92_prom6_core_6_1_full_risk`
- `aggr_08_92_prom6_core_6_1_full_risk_cap40`
- `aggr_08_92_prom6_core_6_1_full_risk_cap60`
- `aggr_10_90_fast_ramp_cash_off_and`

### C. 动量 / 等权高弹性

特点：

- 不再限定为单一底座（等权 / `total_mv` 均可）
- 更强调动量、等权、高弹性
- 更容易在短中窗口做出很高收益

当前代表方向（目标 `4-6` 个）：

- `core_explore_80_20_equal_weight_winner_core...`
- `momentum_top_...`
- `aggr_08_92_prom6_cash_off_and`
- `aggr_05_95_prom3_core_6_1_cash_off_and_cap60`

### D. 双周调仓高收益族

特点：

- 以双周调仓代替月度调仓
- 比月度更快响应，但不至于像单周那样过于高噪音
- 优先观察 `since_2020_01 / since_2023_01`

当前代表方向（目标 `4-6` 个）：

- `aggr_08_92_prom6_core_6_1_full_risk_cap60_biweekly`
- `aggr_05_95_prom3_core_6_1_full_risk_cap60_biweekly`
- `aggr_08_92_prom6_cash_off_and_biweekly`

### E. 单周调仓高收益族

特点：

- 以单周调仓追求更高收益上限
- 更适合高集中突破 / 高弹性动量候选
- 更容易带来更高换手和更深波动

当前代表方向（目标 `4-6` 个）：

- `aggr_08_92_prom6_core_6_1_full_risk_cap60_weekly`
- `aggr_05_95_prom3_core_6_1_full_risk_cap60_weekly`
- `aggr_08_92_prom6_cash_off_and_weekly`

## 4. 当前默认候选生成

当前 `Path 2` 使用独立扫描脚本：

- [scripts/path2_candidate_pass.py](/Users/valselee/my-code/aiinvestor/scripts/path2_candidate_pass.py)

当前候选来源已经从“统一候选池”升级成**显式多候选族生成**：

1. `high_concentration_breakout`
   - 更高集中
   - 更少持仓
   - 更看突破与趋势延续
2. `high_growth_theme`
   - 更看成长主线
   - 更看行业主线与业绩加速
3. `momentum_equal_weight_elastic`
   - 更弱底座
   - 更高弹性
   - 更适合从 `2023 / 2025` 里挖上限

脚本现在会按候选族输出：
- 候选族规模
- 每族目标预算
- 每族排序后的代表候选

当前默认扫描宇宙（`2026-04-24`）已提升到 `103` 个 candidates；五个 family 的当前规模分别为 `43 / 23 / 16 / 4 / 4`。其中 `high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic` 三条长周期 family 已显式纳入 `core_explore_80_20_total_mv_winner_core` 这一窄 prefix，避免当前 `since_2025 / robust` 的 `total_mv` tracked winners 脱离 family ranking。

说明：

- 这些候选的目的不是“稳”，而是尽快拉高收益上限。
- 其中一部分候选的回撤会明显深于 `Path 1`，这是当前阶段允许的。
- 下一轮晋级逻辑对 `since_2020_01` 加权更高；若某候选只明显强化 `since_2023_01 / since_2025_01` 而不能改善 `since_2020_01`，默认不作为主攻方向。
- 当前 family ranking 已从“宽 prefix 匹配”改成“显式 variant + 少数 prefix-only 家族”：
  - 大多数候选族必须命中明确的 `variant_id`
  - 只有 `momentum_top_*` / `satellite_mom_*` 这类天然独立的前缀族允许 prefix-only 归类
  - 这样五条候选族的代表性会更清晰，不再被同一个大前缀重复稀释

## 5. 下一轮优先尝试的方向

## 5.1 本轮（2026-04-21）执行清单（覆盖 5 条独立候选族）

本轮 `Path 2` 固定覆盖以下 `5` 条候选族，不再减少到 `3` 条：

1. **高集中突破族**：继续围绕 `aggr_05_95_prom3_core_6_1_*`，观察高集中高弹性版本在 `since_2020_01 / since_2023_01` 的上限弹性。
2. **高成长主线族**：继续围绕 `aggr_08_92_prom6*_full_risk*`，重点观察是否能真正把 `since_2020_01` 往 `40%+ CAGR` 推。
3. **动量 / 等权高弹性族**：继续围绕 `equal_weight_winner_core*` 与 `momentum_top_*`，但若仅强化 `since_2023_01 / since_2025_01`，默认不作为主攻方向。
4. **双周调仓高收益族**：保留在扫描宇宙里，继续作为“更高频但不过度高噪音”的中间态候选。
5. **单周调仓高收益族**：保留在扫描宇宙里，继续作为最高弹性的激进候选族。

对应执行约束（本轮固定）：

- 必须先独立运行 `scripts/path2_candidate_pass.py`，并以 `PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 定义的候选宇宙为准。
- 每条候选族最多只允许前 `1-2` 个代表候选晋级完整确认。
- 晋级优先顺序固定为：
  1. `since_2020_01` 有显著改善
  2. `since_2023_01` 不明显退化
  3. 回撤和换手仍在可接受范围内
- 双周 / 单周候选族继续保留，但不因为“更高频”而自动获得更高优先级。

### 本轮方向性结论（2026-04-21）

- 双周 / 单周两条新族已经正式接入 `Path 2` 扫描宇宙。
- 第一轮结果表明：单纯提频并没有改写当前 `Path 2` 的窗口赢家。
- 因此下一轮默认策略是：
  - 保留双周 / 单周候选族
  - 但新增探索强度优先投向更适配 `since_2020_01` 的中周期高收益原型
  - 不再平均强化 `since_2023_01 / since_2025_01`

### 本轮快筛记录（2026-04-21 17:57）

- 运行 `scripts/path2_candidate_pass.py`：候选数 `49`，四窗口赢家与四窗口鲁棒候选均未改写。
- 当前（缓存结果）仍然显示：
  - `since_2017_01 / since_2020_01 / since_2025_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（`since_2020_01` 仍约 `35.85% CAGR`）。
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（上限高但回撤深）。
  - `robust`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80`（`meanCAGR~57.11% / minCAGR~26.93%`）。
- 补充（2026-04-21 18:02）：
  - 新增两条候选：`aggr_05_95_prom3_core_6_1_cash_off_and_cap80`、`aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80`，并各自跑了 `since_2017_01/2020_01/2023_01` 离线微回测（复用缓存）后重建对比 CSV。
  - 重跑 `scripts/path2_candidate_pass.py`：候选数增至 `51`，四窗口赢家与鲁棒候选仍未改写；新变体在 `since_2020_01` 上限仅约 `26% CAGR`，明显不具竞争力。

## 5.0 上轮（2026-04-19）执行清单（覆盖 3 条独立候选族）

上轮 `Path 2` 严格按“独立候选族”推进，优先覆盖 3 条候选族（每条内部只观察 3-5 个代表候选，不做无差别全扫）：

1. **高集中突破族**：围绕 `aggr_05_95_prom3_core_6_1_full_risk(_cap60)` 这一支，重点看 `since_2023_01 / since_2025_01` 是否继续维持 `40%+` 的上限弹性。
2. **高成长主线族**：围绕 `aggr_08_92_prom6_core_6_1_full_risk_(cap40/cap60)`，优先把 `since_2020_01 / since_2023_01` 往 `40%+` 推。
3. **动量 / 等权高弹性族**：继续扩展 `core_explore_80_20_equal_weight_winner_core*` 与 `momentum_top_*` 两条前缀族的代表候选，用于寻找更“轻底座”的爆发版本。

对应的预算约束：

- 每轮至少覆盖 `3` 条独立候选族
- 每条候选族至少保留 `4-6` 个代表候选
- 单轮快筛总预算目标 `24-36` 个
- 脚本侧每族目标预算默认按 `target_candidates=6` 执行（3 族合计 `<=18`），避免无意义扩大代表候选数

对应的执行约束：

- 必须先独立运行 `scripts/path2_candidate_pass.py`，并以其扫描规则（`PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS`）作为 Path 2 的候选宇宙。
- Path 2 的窗口赢家与鲁棒候选允许跑输 Path 1（不要求先打赢再记录），但必须**持续**单独维护四窗口赢家 + 四窗口鲁棒候选。
- 若本轮没有出现新的窗口赢家或鲁棒候选改写，则只更新本文档的研究记录，不额外补跑确认回测。

### 本轮快筛记录（2026-04-19）

- `scripts/path2_candidate_pass.py`（独立候选扫描）未改写当前已记录的四窗口赢家与四窗口鲁棒候选。
- 补充（2026-04-19 20:50）：重跑扫描，四窗口赢家与四窗口鲁棒候选结论不变；当时 `since_2020_01` 上限仍约 `~25% CAGR`（后续已提升到 `35.85%`，但仍未到 `40%+`）。
- 当前（缓存结果）仍然显示：
  - `since_2023_01` 上限主要来自 `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（收益上限高，但回撤深）。
  - `since_2020_01` 在现有候选宇宙内仍停留在 `~35.85% CAGR` 附近，需要更独立、更激进（且针对 2020 的）新候选族才有机会冲击 `40%+`。

## 5.1 本轮（2026-04-20）执行清单（覆盖 5 条独立候选族）

本轮 `Path 2` 继续严格按“独立候选族”推进，覆盖以下 5 条候选族（不要求先打赢 Path 1 才记录）：

1. **高集中突破族**：继续围绕 `aggr_05_95_prom3_core_6_1_*`，重点看 `since_2023_01 / since_2025_01` 的上限弹性是否可持续。
2. **高成长主线族**：继续围绕 `aggr_08_92_prom6*_full_risk*` 与 `aggr_10_90_fast_ramp_cash_off_and`，优先把 `since_2020_01` 往 `40%+ CAGR` 推。
3. **动量 / 等权高弹性族**：继续把 `momentum_top_*` 与 `cash_off_and` 线作为“弱底座 + 高弹性”的候选来源，观察是否能在 `2020/2023/2025` 形成更一致的强势版本。
4. **双周调仓高收益族**：新增 `*_biweekly` 变体，验证“更快调仓但不至于像单周一样高噪音”的中间解是否能抬高 `2020/2023`。
5. **单周调仓高收益族**：新增 `*_weekly` 变体，验证更高频调仓是否能给高集中突破和高弹性候选带来更高上限。

对应执行约束（本轮继续沿用）：

- 必须先独立运行 `scripts/path2_candidate_pass.py`，并以 `backtest_marketcap_etf.py` 中 `PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 定义的候选宇宙为准。
- Path 2 必须持续单独维护四窗口赢家 + 四窗口鲁棒候选。
- 若本轮没有出现新的窗口赢家或鲁棒候选改写，则只更新本文档的研究记录，不额外补跑确认回测。

### 本轮快筛记录（2026-04-20）

- 先后运行 `.venv/bin/python scripts/path2_candidate_pass.py`（基于缓存对比 CSV）：
  - 扩展 `PATH2_SCAN_BASE_PREFIXES / PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 后，`path2 candidates=43`；四窗口赢家与四窗口鲁棒候选均未改写。
- 补充（2026-04-20 13:21）：重跑 `scripts/path2_candidate_pass.py`，四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-20 18:54）：再次重跑 `scripts/path2_candidate_pass.py`，`candidates=43`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-20 20:23）：运行 `scripts/path2_candidate_pass.py`，`candidates=43`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-21 10:17）：先重建 `strategy_comparison_base_method.csv`（覆盖 `since_2017_01/2020_01/2023_01`）后运行 `scripts/path2_candidate_pass.py`，`candidates=46`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-21 12:13）：运行 `scripts/path2_candidate_pass.py`，`candidates=46`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-21 14:18）：运行 `scripts/path2_candidate_pass.py`，`candidates=46`；四窗口赢家与四窗口鲁棒候选结论不变。
- 补充（2026-04-21 16:36）：新增/恢复高集中候选变体（含 `prom2_cap80`）并离线补跑小批量回测（`since_2017_01/2020_01/2023_01`），随后重建对比 CSV 并复扫 `scripts/path2_candidate_pass.py`：`candidates=49`；四窗口赢家与鲁棒候选均未改写。
- 当前（缓存结果）四窗口赢家与鲁棒候选：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（CAGR `31.53%`）
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（CAGR `35.85%`，仍未到 `40%+`）
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（CAGR `56.01%`）
  - `since_2025_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（CAGR `124.08%`）
  - `robust`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80`（meanCAGR `57.11%` / minCAGR `26.93%`）

## 5.2 本轮（2026-04-21）执行清单（覆盖 3 条独立候选族）

本轮 `Path 2` 继续按“独立候选族”推进，研究重点限定在以下 `3` 条候选族：

1. **高集中突破族**：继续围绕 `aggr_05_95_prom3_core_6_1_*`，重点观察 `since_2023_01 / since_2025_01` 的上限弹性是否稳定。
2. **高成长主线族**：继续围绕 `aggr_08_92_prom6*_full_risk*`，重点把 `since_2020_01 / since_2023_01` 往 `40%+ CAGR` 推。
3. **动量 / 等权高弹性族**：继续围绕 `equal_weight_winner_core*` 与 `momentum_top_*` 的代表候选，寻找“弱底座 + 高弹性”的更一致版本。

对应执行约束（本轮继续沿用）：

- 必须先独立运行 `scripts/path2_candidate_pass.py`（基于缓存对比 CSV），并以 `backtest_marketcap_etf.py` 中的扫描规则作为候选宇宙。
- Path 2 必须持续单独维护四窗口赢家 + 四窗口鲁棒候选；不要求先打赢 Path 1 才记录。
- 若本轮没有出现新的窗口赢家或鲁棒候选改写，则只更新本文档的研究记录，不额外补跑确认回测。

### A. 更高集中度的突破线

假设：

- 当前高收益候选已经说明更高集中度有效，但还不够纯粹

目标：

- 进一步压缩持仓数
- 强化前 1-2 名权重
- 重点观察 `2020 / 2023` 是否继续上行

预期：

- CAGR 继续提升
- 回撤可能恶化，需要后续第二阶段处理

### B. 行业主线 + 成长加速的更强版本

假设：

- 单纯高动量不够，需要更强的行业主线约束

目标：

- 提升“高成长主线”候选族的纯度
- 减少弱行业里的短期强股

预期：

- 有望提高中窗口质量
- 但实现复杂度更高

### C. 等权 / 高弹性体系的更极端版本

假设：

- 当前 `equal_weight_winner_core` 已经说明“弱底座”有更高爆发力

目标：

- 进一步削弱市值/稳定性约束
- 放大真正强势票的收益贡献

预期：

- 对 `2023 / 2025` 更有利
- `2017` 可能仍然承受很大回撤

## 6. 已淘汰或暂缓的方向

### 6.1 把 Path 2 当成“Path 1 的激进变体集合”

结论：

- 已淘汰。

原因：

- 会导致 `Path 2` 的 winner 仍然大量来自 `Path 1`
- 路径虽然名义独立，但本质没有独立研究价值

当前处理：

- `Path 2` 已经开始使用独立 candidate pass
- 后续应继续扩大独立候选族，而不是继续依赖 `Path 1`

### 6.2 过早把回撤控制作为第一优先级

结论：

- 暂缓。

原因：

- 会直接压掉 `Path 2` 最重要的收益上限探索能力

当前处理：

- 第一阶段先接受更深回撤
- 等形成稳定高收益候选后，再单独研究回撤收敛方案

## 7. 本轮执行规范

每次自动/手动 `Path 2` 迭代，应尽量遵守：

1. 先跑独立 candidate pass，而不是复用 Path 1 fast pass。
2. 每轮固定覆盖 `3` 条独立候选族。
3. 每条候选族内部保留 `4-6` 个代表候选，单轮总预算目标 `24-36` 个。
4. 若某方向虽然收益高，但连续多轮只在一个窗口短暂领先、且回撤极端失控，应写入“暂缓/观察”。
5. 若某候选在 `2020 / 2023 / 2025` 都显著强，应优先进入 `Path 2 robust candidate` 比较。

## 8. 当前观察重点

当前最值得持续观察的是这类候选：

- `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`

原因：

- 在 `2023 / 2025` 窗口已经表现出明显更高的收益弹性
- 说明 `Path 2` 的独立方向正在形成

但它当前的问题也非常明确：

- `2017 / 2020` 的回撤过深
- 还不能直接作为“生产候选”

所以当前更合理的定位是：

- 它是 `Path 2` 的收益上限样本
- 不是当前最终版本

## 9. 维护说明

本文档用于记录 `Path 2` 的研究规划与候选族结构，不用于写死最新数值。  
最新赢家和指标仍以：

- `README.md` 顶部自动区块
- `HISTORY.md`
- `results/weighted_track_winners.json`
- `results/path2_candidate_pass.json`

为准。

## 10. 本轮补充（2026-04-21 18:24）

- 重跑 `scripts/path2_candidate_pass.py`：候选数仍为 `51`，四窗口赢家与 `robust` 候选均未改写。

## 11. 本轮补充（2026-04-21 20:18）

- 重跑 `scripts/path2_candidate_pass.py`：候选数 `51`，四窗口赢家与 `robust` 候选结论不变。

## 12. 本轮补充（2026-04-21 22:20）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数 `51`；四窗口赢家与 `robust` 候选均未改写（近期目标 `since_2020_01 40%+ CAGR` 仍需新增更独立、更激进的候选族）。

## 13. 本轮补充（2026-04-22）

- 运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数仍为 `51`；四窗口赢家与 `robust` 候选继续不变。
- 当前五个候选族的前排仍被同一批高集中等权变体占住，说明“新增周频/双周频族”目前主要是在扩扫描宇宙，还没有形成真正独立的 `since_2020_01` 赢家族。
- `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk30_cap80` 仍是几乎所有候选族里的最高 promotion-score 候选：`since_2020_01 CAGR 35.76% / since_2023_01 CAGR 50.65% / worst MaxDD -38.62%`；它强化了 `2023`，但仍没有把 `2020` 推到 `40%+`。
- `core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60` 继续是 `since_2020_01` 窗口赢家（`35.85% CAGR`），`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80` 继续是 `since_2023_01` 窗口赢家（`56.01% CAGR`）。
- 下一轮新增探索预算不应继续平均投向提频变体；更合理的方向是新增真正面向 `2020` 的中周期高收益原型，而不是再复制一轮 `monthly -> biweekly -> weekly` 频率克隆。
- 本次再次用 `AIINVESTOR_FORCE_OFFLINE=1` 重跑后，五个候选族的前二仍被同一组 `aggr_05_95_prom3_core_6_1_*` 高集中等权变体占据；`risk30_cap80` 的 promotion score 仍约 `0.5033`，而 `cap60` 仍是 `since_2020_01` 的最高窗口赢家（`35.85% CAGR`），说明现有扫描宇宙新增部分还没有产出新的独立 family leader。
- `2026-04-22 06:27 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数仍为 `51`，窗口赢家与 `robust` 候选继续不变。
- 追加了一个只看 `since_2020_01 / since_2023_01` 的 sidecar 微回测：把 `aggr_05_95_prom3_core_6_1_cash_off_and_cap60 / risk30_cap80 / risk50_cap80` 从 `80/20` 扩到 `70/30`、`60/40` 等权底座后，全部都弱于当前 `80/20` 主线。
- 其中新组里表现最好的也只有：
  - `since_2020_01`：`core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_cap60`，`CAGR 26.86% / MaxDD -22.83% / Sharpe 1.0641 / Turnover 3.11`
  - `since_2023_01`：`core_explore_70_30_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_cash_off_and_risk50_cap80`，`CAGR 37.72% / MaxDD -28.76% / Sharpe 1.2732 / Turnover 3.98`
- 结论：当前瓶颈不在 `core/explore` 比例本身，而在候选原型没有真正把 `since_2020_01` 推过 `40%+`；下一轮不应继续把新增预算投到 `80/20 -> 70/30/60/40` 的比例克隆上。
- 本轮继续新增了 `prom2 + cash_off_and + cap80` 三个原型，并离线补跑 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01` 后重建对比 CSV，再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数从 `51` 增至 `63`。
- 新组里表现最好的 `since_2020_01` 候选是 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`，仅到 `32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe / 2.95 Turnover`；仍明显弱于当前 `since_2020_01` winner `aggr_05_95_prom3_core_6_1_cash_off_and_cap60` 的 `35.85% CAGR`。
- 但 `since_2025_01` 窗口赢家被这条新原型改写：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80` 以 `128.06% CAGR / -12.42% MaxDD / 2.1335 Sharpe / 5.80 Turnover` 超过原先的 `aggr_05_95_prom3_core_6_1_cash_off_and_cap60`（`124.08% CAGR / -13.73% MaxDD / 2.1116 Sharpe / 6.18 Turnover`）。
- 结论更新：`prom2 + cash_off_and + cap80` 已经成为新的超短窗口赢家，但它仍不是把 `since_2020_01` 推到 `40%+` 的解。下一轮新增预算应继续面向“中周期高收益原型”，而不是继续复制 `prom2` 的频率或比例分支。
- 当日后续先用缓存重建了 `results/strategy_comparison_base_method.csv`（`427` 行 / `154` 个 base strategies），再运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数维持 `63`，但也暴露出此前 `weighted_track_winners.json` 相对当前 `summary.json` 已经滞后。
- 按这次重建后的完整 comparison CSV 重新同步后，当前真实 tracked winners 改写为：
  - `since_2017_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`（`28.08% CAGR / -46.94% MaxDD / 1.0061 Sharpe / 3.89 Turnover`）
  - `since_2020_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe / 2.95 Turnover`）
  - `since_2023_01`：`aggr_05_95_prom3_core_6_1_full_risk_cap80`（`56.40% CAGR / -50.82% MaxDD / 1.1727 Sharpe / 5.32 Turnover`）
  - `since_2025_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`128.06% CAGR / -12.42% MaxDD / 2.1335 Sharpe / 5.80 Turnover`）
  - `robust`：`aggr_05_95_prom3_core_6_1_full_risk_cap60`（`meanCAGR 54.57% / minCAGR 17.70%`）
- 这次同步后的关键信号是：当前“真实 `since_2020_01` 窗口赢家”已经降到 `32.07% CAGR`，距离 `40%+` 目标比旧快照显示的更远；因此下一轮新增探索预算必须继续投向新的中周期原型，而不是再把 `cap60 / risk30 / equal_elastic` 一类旧锚点当成已验证高水位。
- `2026-04-22 14:30 CST` 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数维持 `63`，四窗口 winner 与 `robust` 候选继续完全不变。
- 当前五个候选族的规模与前排顺位也没有漂移：`43 / 43 / 44 / 41 / 41` 的 family counts 继续稳定，而 `since_2020_01` 仍由 `aggr_03_97_prom2_core_6_1_cash_off_and_cap80` 领跑在 `32.07% CAGR`，离 `40%+` 目标仍有明显距离。
- 本轮再次确认：新增预算不该再投向频率克隆或 family 内参数平移；下一轮 `Path 2` 应继续优先寻找新的中周期高收益原型，同时把现有 `prom2_cap80` 与 `full_risk_cap80/cap60` 只保留为锚点和对照。

## 14. 本轮补充（2026-04-22 23:27 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：候选数维持 `63`，四窗口 winner 与 `robust` 候选继续完全不变。
- 当前 tracked winners 仍是：
  - `since_2017_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01 / since_2025_01`：`aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `robust`：`aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 五个候选族的规模与前排顺位继续稳定在 `43 / 43 / 44 / 41 / 41`；新增双周/单周族与 `prom2_cap80` 原型已经进入扫描宇宙，但还没有形成新的独立 family leader。
- 当前 `since_2020_01` 仍只到 `32.07% CAGR`，距离 `40%+` 目标还有明显缺口；下一轮新增预算仍应优先投向新的中周期高收益原型，而不是继续复制 `monthly -> biweekly -> weekly` 频率克隆。
- `3_1` 短周期变体继续只保留在扫描宇宙里做观察；在它们没有明确打赢当前 `6_1` 主锚点之前，不升级成新的主攻候选族。

## 15. 本轮补充（2026-04-23 01:32 CST）

- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：当前独立候选宇宙为 `32` 个候选，五个候选族规模为 `14 / 7 / 8 / 6 / 6`；最近几轮文档里引用的 `63` 候选快照已经不是当前 comparison CSV 的真实状态。
- 按本轮 `path2_candidate_pass.json` 与 `weighted_track_winners.json` 重新同步后，当前 Path 2 tracked winners 为：
  - `since_2017_01 / since_2020_01 / since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 当前关键指标是：
  - `since_2020_01` winner 只到 `26.20% CAGR / 1.0012 Sharpe / -28.09% MaxDD / 2.84 Turn`
  - `since_2023_01` winner 为 `52.24% CAGR / 1.1933 Sharpe / -49.35% MaxDD / 5.43 Turn`
  - `robust` 候选为 `meanCAGR 58.88% / minCAGR 17.57%`
  这说明当前瓶颈比前一版文档记录的 `32%+` 还更低，`since_2020_01 40%+ CAGR` 目标仍有明显距离。
- 本轮 family leader 也给出更清晰的取舍：
  - `high_concentration_breakout` 仍由 `aggr_05_95_prom3_core_6_1_full_risk(_cap80)` 系列主导
  - `momentum_equal_weight_elastic` 当前真正的窗口赢家已切到 `aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `biweekly / weekly_rebalance_aggressive` 的前排仍只是底座级别基线，没有出现能改写四窗口 winner 的高频 leader
- 因此下一轮 `Path 2` 继续把新增预算优先投向新的中周期高收益原型，不再给 `biweekly / weekly` 的频率克隆额外预算；它们继续只保留为对照，不升级成新的主攻族。

## 16. 本轮补充（2026-04-23 03:33 CST）

- 本轮修正了一个真实缺口：`PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 已经声明了 `aggr_08_92_prom6_core_3_1_full_risk_cap40`、`aggr_05_95_prom7_core_6_1_full_risk`、`aggr_05_95_prom7_core_6_1_full_risk_cap40`、`aggr_05_95_prom7_core_3_1_full_risk_cap40`，但 `WINNER_CORE_VARIANTS` 里此前没有这些定义，导致 candidate pass 实际跑不到它们。本轮已补齐这 4 个变体，并离线补跑 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`。
- 新补变体里最有价值的观察是：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom7_core_3_1_full_risk_cap40` 在 `since_2023_01` 做到了 `40.40% CAGR / 1.0147 Sharpe / -45.82% MaxDD / 507.33% Turnover`，说明 `prom7 + 3_1` 确实具备独立的高弹性；但它仍明显落后于当前 `since_2023_01` winner `aggr_05_95_prom3_core_6_1_full_risk_cap80` 的 `56.40% CAGR`，因此只保留为 sidecar prototype，不晋升为新主线。
- 在把新增变体结果并回全量 `summary.json` 后，重建出的 `results/strategy_comparison_base_method.csv` 已恢复到完整口径（`1744` 行 / `466` 个 base strategies）。基于这份完整 CSV，再次运行 `./.venv/bin/python scripts/path2_candidate_pass.py` 后，当前独立候选宇宙恢复为 `87` 个候选，而不是上一版局部 CSV 下看到的 `32` 个。
- 以这次完整重建后的口径为准，当前 Path 2 tracked winners 已同步为：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 关键约束没有变：即使在完整口径下，`since_2020_01` 当前 tracked winner 也只到 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`，距离 `40%+ CAGR` 目标仍有明显缺口。所以下一轮新增预算依然应该优先投向新的中周期高收益原型，而不是继续复制 `biweekly / weekly` 频率克隆。

## 17. 本轮补充（2026-04-23 05:29 CST）

- 再次运行 `./.venv/bin/python scripts/path2_candidate_pass.py`：当前独立候选宇宙仍为 `87` 个候选；四窗口 tracked winners 与 `robust_candidate` 均未改写，`since_2020_01` 仍由 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80` 领跑，但也只做到 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`。
- 本轮新增的研究发现不是 winner 改写，而是 `family_ranked_candidates` 口径仍存在串线：由于 `PATH2_SCAN_FAMILY_RULES` 里的宽前缀（尤其是 `core_explore_80_20_equal_weight_winner_core` 一类）会把同一批 `80/20` 高集中候选同时并入多个 family，当前五个 family leaderboard 仍被几乎相同的候选占满，不能真实反映“独立候选族”的前排顺位。
- 这意味着下一轮 `Path 2` 的第一优先级不该是继续追加 `biweekly / weekly` 克隆，而是先收紧 family membership 口径，再把新增预算投向真正面向 `since_2020_01` 的中周期高收益原型；否则 family 级排序会持续高估同一批 `80/20` 高集中等权版本。
- 本轮随后执行 `./.venv/bin/python scripts/update_weighted_winners.py` 与 `./.venv/bin/python scripts/generate_strategy_comparison_chart.py`：Path 2 的 tracked winners / robust candidate 文本口径没有继续漂移，但 A 股对比图按当前 tracked 基线重绘后发生了实际 binary diff，因此本轮保留 `sync-only` 提交即可，不额外补跑确认回测。

## 18. 本轮补充（2026-04-23 17:57 CST）

- 再次运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：本轮 `path2_candidate_pass.json` 的真实口径是 `candidate_count=86`，五个候选族规模分别为 `21 / 8 / 9 / 4 / 4`；四窗口 tracked winners 与 `robust_candidate` 均未改写。
- 当前 tracked winners 继续维持：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 关键约束没有变化：`since_2020_01` 当前 winner 仍只做到 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`，离 `40%+ CAGR` 目标仍有明显缺口；`biweekly / weekly` 两个高频族当前都只剩 `4` 个候选，继续没有改写主线的证据。
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py` 与 `./.venv/bin/python scripts/generate_strategy_comparison_chart.py`：Path 2 的 winner/robust 文本口径仍未改写，但 README/HISTORY 与 A 股对比图已经同步到最新 `as_of=2026-04-23` 指标，因此本轮继续保留 `sync-only` 提交即可，不额外补跑确认回测。
- 下一轮 `Path 2` 继续把新增预算优先投向新的中周期高收益原型，并优先收紧 family membership 口径；不继续给 `biweekly / weekly` 频率克隆追加预算。

## 19. 本轮补充（2026-04-24）

- 本轮先把 `PATH2_SCAN_VARIANT_IDS / PATH2_SCAN_FAMILY_RULES` 扩到当前缓存里已经存在的一批中周期 `total_mv` 原型，并补上 `core_explore_80_20_total_mv_winner_core` 在三条长周期 family 里的窄 prefix 归类。随后运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`：当前独立候选宇宙已提升到 `103` 个 candidates，五个 family 规模分别为 `43 / 23 / 16 / 4 / 4`。
- 这次扩容的目的不是立刻改写 winner，而是解决两个结构性缺口：
  - 当前 `since_2025_01` winner 与 `robust_candidate` 都落在 `total_mv` 原型上，但旧的 family rules 不能把它们纳入 family ranking。
  - `since_2020_01` 仍只有 `32.07% CAGR`，因此需要把 `aggr_05_95_prom7 / aggr_07_93_prom6 / aggr_07_93_prom8(_ramp85) / risk_on / conc35 / balance_* / mid_15_85_prom7 / share_12_88_hold_3_7` 这一批中周期原型正式纳入扫描宇宙，而不是继续只扩高频克隆。
- 扩容后四窗口 tracked winners 与 `robust_candidate` 继续不变：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 本轮随后再次执行 `./.venv/bin/python scripts/update_weighted_winners.py`、`./.venv/bin/python scripts/generate_strategy_comparison_chart.py` 与 `./.venv/bin/python scripts/export_live_platform_data.py`：README / HISTORY / `results/weighted_track_winners.json` / `results/live` 已同步到 `as_of=2026-04-24`，但 Path 2 仍属于 `sync-only` 指标更新，没有新的窗口 winner 改写。
- 下一轮继续优先新增更适配 `since_2020_01` 的中周期高收益原型，不给 `biweekly / weekly` 两个高频族额外预算。

## 20. 本轮补充（2026-04-25）

- 本轮先按自动化规则把独立 worktree 对齐到主工作树 `main`，随后用缓存重建了 `results/strategy_comparison_base_method.csv`（`1899` 行 / `491` 个 base strategies）；这次重建把此前未并入 comparison CSV 的 cached summaries 补回到了 `Path 2` 扫描宇宙里，并把整条 A 股 artifact 链重新同步到 `sample_end=2026-04-24`。
- 本轮同时修掉了一个真实的 `Path 2` 执行层问题：极端高集中候选在周频 overlay 调仓里会把 `NaN` code 混进持仓序列，导致 `compute_rebalance_trades()` 在持仓聚合时崩溃。当前已在 `backtest_marketcap_etf.py` 中加上“丢弃空索引 + 合并重复 code”的最小修复；用 `core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80__sat_three_stage_buffered` 做窄复现后，回测已能完整跑通。
- 在这份重建后的完整 comparison CSV 上再次运行 `./.venv/bin/python scripts/path2_candidate_pass.py`：
  - `candidate_count=104`
  - family 规模为 `43 / 23 / 16 / 4 / 4`
  - 四窗口 tracked winners 与 `robust_candidate` 继续完全不变。
- 当前 Path 2 tracked winners 仍维持：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 这轮最有价值的新信息不是 winner 改写，而是“口径补齐后结论仍不变”：
  - `since_2020_01` 上限仍只到 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`
  - `robust_candidate` 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`（`meanCAGR 58.51% / minCAGR 17.57%`）
  - `biweekly / weekly` 两个高频族依旧只有 `4 / 4` 个候选，继续没有改写主线的证据
  - 新补回 CSV 的候选只把扫描宇宙从 `103` 推到 `104`，没有改变五族的主次关系。
- 因此本轮继续作为 `sync-only` 提交：同步了完整 comparison CSV、刷新了 `Path 2` tracked artifact，并把高集中候选的回测崩溃点修掉；下一轮仍优先把新增预算投向更适配 `since_2020_01` 的中周期高收益原型，而不是继续扩高频克隆。

## 21. 本轮补充（2026-04-26）

- 本轮同样先重查基线：`git fetch origin` 失败后，因当前 worktree 已知 `origin/main` 不是主工作树 `main` 的后继，本轮回退到本地主工作树 `main`（`bb3a7d7`）作为 publish baseline，再在该基线上重跑独立扫描。
- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py` 后，当前 `Path 2` 独立候选宇宙为 `117` 个 candidates；五条 family 的规模分别为 `49 / 23 / 16 / 4 / 4`。新增体量主要重新落在 `high_concentration_breakout`，说明这轮更多是在完整缓存口径下把高集中家族成员补齐，而不是出现新的高频主线。
- 四窗口 tracked winners 与 `robust_candidate` 继续不变：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`
- 这轮最关键的约束没有变化：`since_2020_01` 上限依旧停在 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`，而 `biweekly / weekly` 两条高频族依旧只有 `4 / 4` 个候选，且没有任何一条能接近改写主线。因此本轮只把 `results/path2_candidate_pass.json`、README 自动区块与 A 股对比图同步到当前口径，不额外补跑确认回测。
- 下一轮继续把新增预算优先投向更适配 `since_2020_01` 的中周期高收益原型，并继续压紧 family membership 口径；不继续给 `biweekly / weekly` 高频克隆追加预算。

## 22. 本轮补充（2026-04-27）

- 本轮同样先按自动化基线规则重查 publish baseline：`git -C /Users/valselee/my-code/aiinvestor fetch origin main` 成功后，确认最新 `origin/main` 位于 `fd4b214`，领先于本地主工作树 `main`（`39cf735`），因此独立扫描直接基于该远端基线重放。
- 运行 `./.venv/bin/python scripts/path2_candidate_pass.py` 后，当前 `Path 2` 独立候选宇宙收敛到 `104` 个 candidates；五条 family 的规模分别是 `43 / 23 / 16 / 4 / 4`，说明这轮主要是继续压紧 `high_concentration_breakout` 的 family membership 口径，而不是扩新的高频分支。
- 四窗口 tracked winners 继续完全不变，`robust_candidate` 同步落在更稳的 `cap80` 版本：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`
- 这轮新增的信息主要是“收紧 membership 后结论仍不变”：当前 `since_2020_01` ceiling 仍停在 `32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`，而 `robust_candidate` 的四窗汇总同步为 `meanCAGR 58.06% / minCAGR 18.04%`；`biweekly / weekly` 两条高频族依旧只有 `4 / 4` 个候选，继续没有改写主线的证据。
- 除了导出 `results/live` 依赖所需的 summary replay 之外，这轮没有再补新的 `Path 2` 确认回测；本轮价值主要是把 `results/path2_candidate_pass.json` 从旧的 `117` 候选、过宽 family membership 与 `cap60` robust 口径，同步回当前 `104` 候选、压紧 membership、`cap80` robust 的真实状态。
- 下一轮继续把新增预算优先投向更适配 `since_2020_01` 的中周期高收益原型，不给 `biweekly / weekly` 高频克隆追加预算；若要扩新族，优先考虑月频或中周期原型，而不是继续放大家族内的高频副本。

## 23. 本轮补充（2026-04-27 09:08 CST）

- 本轮同样先按自动化基线规则重查 publish baseline：`git fetch origin` 失败后，确认当前 worktree 已知 `origin/main`（`5a87b29`）仍是本地主工作树 `main`（`39cf735`）的后继，因此独立扫描直接基于该已知远端基线重放。
- 运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py` 后，当前 `Path 2` 独立候选宇宙恢复到 `117` 个 candidates；五条 family 的规模分别为 `49 / 23 / 16 / 4 / 4`。新增体量再次主要落在 `high_concentration_breakout`，说明当前 shared comparison CSV 的真实状态比上一版 `104` 候选更宽，而不是新的高频 family 扩张。
- 四窗口 tracked winners 继续保持不变，但关键指标已经同步抬升到当前 `as_of=2026-04-27` 口径：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`（`28.48% CAGR / 1.0116 Sharpe / -46.94% MaxDD / 3.89 Turn`）
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`）
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（`58.03% CAGR / 1.1874 Sharpe / -50.82% MaxDD / 5.32 Turn`）
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`145.68% CAGR / 2.1978 Sharpe / -12.20% MaxDD / 5.29 Turn`）
- 当前 tracked `robust_candidate` 也回到了更稳的 `cap60` 版本：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap60`（`meanCAGR 58.51% / minCAGR 17.57% / meanSharpe 1.1406 / worstMaxDD -66.07%`）。这说明最新 shared payload 的真实状态不是上一条记录里的 `cap80 robust`。
- 下一轮继续把新增预算优先投向更适配 `since_2020_01` 的中周期高收益原型，不给 `biweekly / weekly` 高频克隆追加预算；若要扩新族，优先考虑月频或中周期原型，而不是继续放大家族内的高频副本。

## 24. 本轮补充（2026-04-27 18:09 CST）

- 本轮在主工作树 `main` 上运行 `./.venv/bin/python scripts/path2_candidate_pass.py`，当前 `Path 2` 独立候选宇宙为 `103` 个 candidates；五条 family 规模继续是 `43 / 23 / 16 / 4 / 4`，满足 `100+` family-ranked universe 的最低要求。
- 四窗口 tracked winners 与本轮扫描输出保持为：
  - `since_2017_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap80`（`27.95% CAGR / 1.0039 Sharpe / -46.94% MaxDD / 3.89 Turn`）
  - `since_2020_01`：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / 1.1480 Sharpe / -23.02% MaxDD / 2.95 Turn`）
  - `since_2023_01`：`core_explore_80_20_equal_weight_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（`55.29% CAGR / 1.1612 Sharpe / -50.82% MaxDD / 5.32 Turn`）
  - `since_2025_01`：`core_explore_80_20_total_mv_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`145.68% CAGR / 2.1978 Sharpe / -12.20% MaxDD / 5.29 Turn`）
  - `robust`：`core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（`meanCAGR 58.06% / minCAGR 18.04%`）
- 关键约束继续不变：`since_2020_01` 上限仍停在 `32.07% CAGR`，距离 `40%+` 目标仍有明显缺口；`biweekly / weekly` 两个高频族各只有 `4` 个候选，且仍没有改写主线。
- 下一轮继续优先新增更适配 `since_2020_01` 的中周期/月频高收益原型，并继续压紧 family membership 口径；不把预算继续投向高频克隆扩张。
