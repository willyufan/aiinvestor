# Path 5 事件知识图谱研究计划

## 2026-06-07 16:06 CST 状态

最终 guard 为 `pass`，Path5 仍处于事件入口、冻结候选池和来源审计阶段；`candidate_count=6`、`frozen_candidate_count=6`、`pending_audit_count=6`、`backtest_ready_count=0`。本轮读取 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl` 与 `results/research/a_share/event_theme_audit.jsonl`，没有把待审计 seed 当成有效策略结论，也没有注册真实 event backtest entry。

本轮按 `event_basket_registry` 巡检并追加 6 条 `pending_primary_source_review` 审计记录，覆盖 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ`；6 条记录均保持 `frozen=true`、`backtest_ready=false`。由于本轮 Path4 signal28/cap10 仍未替换 robust，Path5 下一次比较对象继续包含 Path4 robust `aggr_08_92_prom6_emergent_theme_risk30_cap50`、2020 winner `signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn` 与本轮 signal28/cap10 失败对照。

下一轮第一条动作仍不是回测：先补主来源审计并逐条更新为 `source_audit_passed` 或 `source_audit_failed`。只有至少 1 个候选通过审计后，才执行预留入口：`.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。若脚本仍不存在，先实现只读取冻结候选池的最小 runner，再与 Path4 robust 和 signal28/cap10 失败对照做 T+20D/T+60D/T+120D 比较。

## 2026-06-07 04:26 CST 状态

最终 guard 为 `pass`，Path5 仍处于事件入口、冻结候选池和来源审计阶段；`candidate_count=6`、`frozen_candidate_count=6`、`pending_audit_count=6`、`backtest_ready_count=0`。本轮读取 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl` 与 `results/research/a_share/event_theme_audit.jsonl`，没有把待审计 seed 当成有效策略结论，也没有注册真实 event backtest entry。

本轮按 `event_backtest_entry` 巡检并追加 6 条 `pending_primary_source_review` 审计记录，覆盖 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ`；6 条记录均保持 `frozen=true`、`backtest_ready=false`。最终 guard focus 轮到 `path4_comparison`，但由于 `backtest_ready_count=0`，Path5 仍不能做收益比较；后续比较对象应包含 Path4 robust `aggr_08_92_prom6_emergent_theme_risk30_cap50` 与本轮 signal30 失败对照。

下一轮第一条动作仍不是回测：先补主来源审计并逐条更新为 `source_audit_passed` 或 `source_audit_failed`。只有至少 1 个候选通过审计后，才执行预留入口：`.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。若脚本仍不存在，先实现只读取冻结候选池的最小 runner，再与 Path4 robust 和 signal30 失败对照做 T+20D/T+60D/T+120D 比较。

## 2026-06-06 16:17 CST 状态

最终 guard 为 `pass`，Path5 仍处于事件入口、冻结候选池和来源审计阶段；`candidate_count=6`、`frozen_candidate_count=6`、`pending_audit_count=6`、`backtest_ready_count=0`。本轮读取 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl` 与 `results/research/a_share/event_theme_audit.jsonl`，没有把待审计 seed 当成有效策略结论，也没有注册真实 event backtest entry。

本轮按最终 focus `frozen_candidate_audit` 追加 6 条 `pending_primary_source_review` 审计记录，覆盖 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ`；6 条记录均保持 `frozen=true`、`backtest_ready=false`。由于本轮 Path4 `risk18/cap14/exit66_lowturn` 没有替换 robust，Path5 下一次比较对象仍应包含 Path4 当前 robust `aggr_08_92_prom6_emergent_theme_risk30_cap50`、上一轮 2020 winner `signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn` 与本轮 `risk18/cap14` 失败对照。

下一轮第一条动作仍不是回测：先补主来源审计并逐条更新为 `source_audit_passed` 或 `source_audit_failed`。只有至少 1 个候选通过审计后，才执行预留入口：`.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。若脚本仍不存在，先实现只读取冻结候选池的最小 runner，再与 Path4 做 T+20D/T+60D/T+120D 比较。

## 2026-06-06 10:28 CST 状态

最终 guard 为 `pass`，Path5 仍处于事件入口、冻结候选池和来源审计阶段；`candidate_count=6`、`frozen_candidate_count=6`、`pending_audit_count=6`、`backtest_ready_count=0`。本轮读取 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl` 与 `results/research/a_share/event_theme_audit.jsonl`，没有把待审计 seed 当成有效策略结论，也没有注册真实 event backtest entry。

本轮按最终 focus `event_basket_registry` 追加 6 条 `pending_primary_source_review` 审计记录，覆盖 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ`；6 条记录均保持 `frozen=true`、`backtest_ready=false`。由于本轮 Path4 出现新的 `since_2020_01` window winner，Path5 下一次比较对象应更新为 Path4 `signal29_leader76_coverage_penalty_risk15_cap12_exit64_lowturn`，但在审计通过前仍不能做收益归因。

下一轮第一条动作仍不是回测：先补主来源审计并逐条更新为 `source_audit_passed` 或 `source_audit_failed`。只有至少 1 个候选通过审计后，才执行预留入口：`.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。若脚本仍不存在，先实现只读取冻结候选池的最小 runner，再与 Path4 当前 `signal29...lowturn` 和 robust `aggr_08_92_prom6_emergent_theme_risk30_cap50` 做 T+20D/T+60D/T+120D 比较。

## 2026-06-06 04:23 CST 状态

最终 guard 为 `pass`，Path5 仍处于事件入口、冻结候选池和来源审计阶段；`candidate_count=6`、`frozen_candidate_count=6`、`pending_audit_count=6`、`backtest_ready_count=0`。本轮读取 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl`、`results/research/a_share/event_theme_audit.jsonl`，没有把待审计 seed 当成有效策略结论，也没有注册真实 event backtest entry。

本轮按 `event_backtest_entry/frozen_candidate_audit` 巡检向 `event_theme_audit.jsonl` 追加 6 条 `pending_primary_source_review` 记录，覆盖 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ`；6 条记录均保持 `frozen=true`、`backtest_ready=false`。最终 rotation focus 显示为 `path4_comparison`，但由于 `backtest_ready_count=0`，仍不能和 Path4 做收益比较。

下一轮第一条动作仍不是回测：先补主来源审计并逐条更新为 `source_audit_passed` 或 `source_audit_failed`。只有至少 1 个候选通过审计后，才执行预留入口：`.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。若脚本仍不存在，先实现只读取冻结候选池的最小 runner，再与 Path4 当前 `coverage_penalty_risk15_cap12_exit66` winner 和本轮 `signal28_leader74_coverage_penalty_risk15_cap12_exit64` 失败对照做 T+20D/T+60D/T+120D 比较。

## 2026-06-05 22:21 CST 状态

最终 guard 为 `pass`，Path5 仍处于事件入口、冻结候选池和来源审计阶段；`candidate_count=6`、`frozen_candidate_count=6`、`pending_audit_count=6`、`backtest_ready_count=0`。本轮读取 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl`、`results/research/a_share/event_theme_audit.jsonl`，没有把待审计 seed 当成有效策略结论，也没有注册真实 event backtest entry。

本轮按最终 rotation focus `frozen_candidate_audit` 向 `event_theme_audit.jsonl` 追加 6 条带时间戳的 `pending_primary_source_review` 复核记录，覆盖 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ`；6 条记录均保持 `frozen=true`、`backtest_ready=false`。这说明冻结篮子 `mrc_uec_ai_network_20260506_v0` 仍缺可追溯主来源链路，不能进入事件篮子收益结论。

下一轮第一条动作仍不是回测：先补来源审计并逐条更新为 `source_audit_passed` 或 `source_audit_failed`。建议先运行 `.venv/bin/python scripts/research_iteration_guard.py` 确认 `pending_audit_count`，然后只在至少 1 个候选通过审计后执行预留入口：`.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。若脚本仍不存在，先实现只读取冻结候选池的最小 runner，再和 Path4 当前强主题 winner `coverage_penalty_risk15_cap12_exit66` 以及本轮 lowturn 失败对照做 T+20D/T+60D/T+120D 比较。

## 2026-06-05 10:22 CST 状态

最终 guard 为 `pass`，Path5 仍处于事件入口、冻结候选池和来源审计阶段；`candidate_count=6`、`frozen_candidate_count=6`、`pending_audit_count=6`、`backtest_ready_count=0`。本轮读取并维护 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl`、`results/research/a_share/event_theme_audit.jsonl`，没有把待审计 seed 当成有效策略结论，也没有注册真实 event backtest entry。

本轮把 registry 的 `updated_at` 更新到 `2026-06-05`，并向 `event_theme_audit.jsonl` 追加 6 条 `pending_primary_source_review` 审计记录，覆盖 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ`；6 条记录均保持 `backtest_ready=false`。这说明冻结篮子 `mrc_uec_ai_network_20260506_v0` 已被本轮显式巡检，但仍缺主来源审计，不能进入收益结论。

最新 rotation focus 为 `path4_comparison`，但由于 `backtest_ready_count=0`，下一轮第一条动作仍必须先补来源审计，而不是直接回测：逐条把 audit 状态更新为 `source_audit_passed` 或 `source_audit_failed`。只有至少 1 个候选通过审计后，才执行预留入口 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`；若脚本仍不存在，先实现只读取冻结候选池的最小 runner，再和 Path4 当前强主题 winner `coverage_penalty_risk15_cap12_exit66` 以及本轮失败对照 `risk12_cap10_exit64` 做 T+20D/T+60D/T+120D 对比。

## 2026-06-05 04:11 CST 状态

最新 guard 为 `pass`，Path5 仍处于事件入口、冻结候选池和来源审计阶段；`candidate_count=6`、`frozen_candidate_count=6`、`pending_audit_count=6`、`backtest_ready_count=0`。本轮只读取并复核 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl`、`results/research/a_share/event_theme_audit.jsonl`，没有把待审计 seed 当成有效策略结论，也没有注册 event backtest entry。

冻结篮子仍为 `mrc_uec_ai_network_20260506_v0`，6 个候选是 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ`。最新 rotation focus 为 `event_backtest_entry`，但由于 `backtest_ready_count=0`，下一轮第一条动作仍必须先补主来源审计，而不是直接回测：逐条把 audit 状态更新为 `source_audit_passed` 或 `source_audit_failed`；只有至少 1 个候选通过审计后，才执行预留入口 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。若脚本仍不存在，先实现只读取冻结候选池的最小 runner，再和 Path4 `coverage_penalty_risk15_cap12_exit66` 做 T+20D/T+60D/T+120D 对比。

## 2026-06-04 16:16 CST 状态

本轮 guard 为 `pass`，Path5 继续处在事件入口、冻结候选池和来源审计阶段；没有进入真实回测，也没有把待审计 seed 当成有效策略结论。

本轮巡检对象仍为 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl` 与 `results/research/a_share/event_theme_audit.jsonl`。冻结篮子 `mrc_uec_ai_network_20260506_v0` 保持 `6` 个候选，`pending_audit_count` 仍大于 0，`backtest_ready_count=0`；因此不注册 event backtest entry。

下一轮第一条动作仍不是回测：先补 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ` 的主来源审计，并把 audit 状态更新为 `source_audit_passed` 或 `source_audit_failed`。只有通过审计的候选数大于 0 后，才执行预留入口：`.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`；若脚本仍不存在，先实现最小 runner，再和 Path4 `signal26/28 leader72 cap12` 做 T+20D/T+60D/T+120D 对比。

## 2026-06-04 10:16 CST 状态

本轮 guard 为 `pass`，Path5 仍处于事件入口与来源审计阶段，没有进入真实回测，也没有把待审计 seed 当作有效策略结论。`results/research/a_share/event_theme_registry.json` 与 `results/research/a_share/event_theme_candidates.jsonl` 继续保留冻结篮子 `mrc_uec_ai_network_20260506_v0`，六个候选仍需主来源审计；`backtest_ready=false` 时不注册 event backtest entry。

本轮巡检结论：

1. 事件候选池未扩容，避免在来源未确认时扩大后视风险。
2. Path4 强主题涌现本轮没有新 winner 变化，因此 Path5 下一步仍应先补“可审计来源 + 冻结篮子”而不是直接和 Path4 做收益比较。
3. 下一轮第一条动作不是回测：先读取 `results/research/a_share/event_theme_audit.jsonl`，为 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ` 逐条补主来源并更新 audit 状态。

下一轮命令提示：`.venv/bin/python scripts/research_iteration_guard.py` 后若 `pending_audit_count > 0`，先补审计 JSONL；只有 `source_audit_passed` 候选数大于 0 后，才注册最小事件篮子回测入口并与 Path4 的 `emergent_theme_discovery` 做 T+20D/T+60D/T+120D 对比。

## 2026-06-03 22:20 CST 状态

这条 A 股路径本轮仍未进入真实回测。当前最小入口已经存在：`results/research/a_share/event_theme_registry.json` 与 `results/research/a_share/event_theme_candidates.jsonl` 记录了首个冻结篮子 `mrc_uec_ai_network_20260506_v0`，候选数 `6`，冻结数 `6`。本轮新增 `results/research/a_share/event_theme_audit.jsonl` 并把 registry 状态改为 `source_audit_started`，但六个候选全部仍是 `pending_primary_source_review`，`backtest_ready=false`。

本轮只维护来源审计状态，不把待审计 seed 当作有效策略结论，也不与 Path 4 强主题结果混写。下一步第一轮应先完成最小可跑版本：

1. 为 `300394.SZ / 688498.SH / 300502.SZ / 300308.SZ / 688195.SH / 300408.SZ` 补公司公告、年报或权威产业来源，逐条把 audit 状态从 `pending_primary_source_review` 改为 `source_audit_passed` 或 `source_audit_failed`。
2. 只有审计通过的候选才能进入事件篮子回测；继续保持冻结候选池，不覆盖原 seed。
3. 增加一个只读取冻结候选池的 A 股事件组合回测入口，先跑等权和流动性约束两个版本。
4. 和 Path 4 的强主题涌现候选对比 T+20D、T+60D、T+120D 以及月度持有表现。

下一轮第一条命令不是回测，而是审计状态补齐：`.venv/bin/python scripts/research_iteration_guard.py` 后优先读取 `results/research/a_share/event_theme_audit.jsonl`，补主来源并只在 `backtest_ready_count > 0` 后再注册 event backtest entry。

## 定位

Path 5 先服务 A 股研究，不直接同步到 H 股。

参考信息平台的价值不在页面形式本身，而在它把一个事件型机会拆成了可审计的研究链条：事件触发、概念定义、产业链拆解、股票映射、催化剂、风险和来源。A 股先验证这条路径是否能产生有效策略，如果有效，再把方法迁移到 H 股或 A+H 映射池。

Path 5 和现有 Path 4 的差异：

- Path 4 更偏价格和主题涌现，用行情行为识别新方向。
- Path 5 从明确事件或产业报告出发，先建立主题篮子，再回测事件后的收益、回撤和持续性。
- Path 5 的核心资产是“可追溯研究报告 + 冻结候选池”，不是单纯的价格信号。

## 参考平台结构

每个事件研究报告都应包含：

1. 触发事件：新闻、产业会议、订单、政策、技术迭代或公司公告。
2. 一句话定义：说明这个主题到底是什么。
3. 核心定位：它属于需求变化、供给变化、技术升级、国产替代还是周期修复。
4. 产业链/BOM：上游、中游、下游、关键零部件和替代关系。
5. 股票映射：标的、角色、暴露度、确定性、流动性、市值约束。
6. 催化剂：未来可能验证或证伪主题的时间点。
7. 风险：技术、订单、估值、政策、竞争格局。
8. 来源和审计清单：方便复盘时判断是否存在事后修正。

## 建议数据产物

后续实现时可以增加以下研究产物：

- `research_notes/a_share/events/<YYYYMMDD>_<slug>.md`：人工或半自动事件研究报告。
- `results/research/a_share/event_theme_registry.json`：主题注册表，记录主题、版本、报告日期和有效期。
- `results/research/a_share/event_theme_candidates.jsonl`：冻结后的股票候选池。
- `results/research/a_share/event_theme_audit.jsonl`：回测、修订和剔除原因审计。

第一阶段可以先不做复杂数据库，只用 Markdown + JSON/JSONL，保持轻量。

## 报告模板

```markdown
# <主题名>_<YYYYMMDD>

## 元数据

- report_date:
- event_time:
- theme_tags:
- source_links:
- affected_industries:

## 一句话定义

## 产业链拆解

| 环节 | 说明 | 关键指标 |
| --- | --- | --- |

## 股票映射

| 代码 | 名称 | 角色 | 暴露度 | 确定性 | 纳入理由 | 风险 |
| --- | --- | --- | ---: | ---: | --- | --- |

## 催化剂

| 时间 | 催化剂 | 验证方式 |
| --- | --- | --- |

## 风险地图

## 审计清单

- 是否记录原始来源：
- 是否冻结候选池：
- 是否避免使用报告日之后的信息：
- 是否记录剔除理由：
```

## 研究流程

1. 创建事件报告，记录来源和报告日期。
2. 从报告中提取股票候选池，统一成 A 股代码。
3. 在报告日期冻结候选池，后续修订必须生成新版本。
4. 回测事件窗口：T+1、5D、20D、60D、120D，以及月度持有版本。
5. 构建组合规则：等权、暴露度权重、流动性约束、龙头-卫星结构。
6. 和 Path 4 主题涌现、Path 1/2 常规策略做横向比较。
7. 保留来源、候选池和回测结果，方便未来判断是否是事后归因。

## 第一批 A 股主题方向

优先选产业链清晰、A 股标的充足、催化剂可验证的方向：

- MRC/UEC/800G-1.6T AI 网络升级。
- AI 光模块、PCB、铜连接。
- 国产半导体设备和材料。
- AI 电力、液冷、数据中心基础设施。
- 机器人和具身智能供应链。

这些主题既能复用参考平台的报告结构，也能和现有 A 股策略结果做对照。

## 策略家族候选

- `event_theme_equal_weight`：冻结候选池后等权持有。
- `event_theme_leader_satellite`：产业链龙头为核心，高暴露度弹性标的为卫星。
- `event_theme_liquidity_capped`：按暴露度排序，但用流动性和单票上限控制交易风险。
- `event_theme_catalyst_decay`：事件后权重随时间衰减，适合短催化主题。
- `event_theme_reconfirm_momentum`：只有候选池内标的出现价格确认时才进入组合。

## 防过拟合约束

1. 原始候选池一旦冻结，不允许直接覆盖。
2. 任何新增或删除标的都必须形成新版本，并记录原因。
3. 先做 tracked-only，不进入正式 winner。
4. 至少积累 20 个事件样本或主题实例后，再判断这条路径是否稳定有效。
5. 不能只看单一热门主题，必须覆盖技术、政策、订单、周期修复等不同事件类型。

## 有效性判断

Path 5 成立需要满足至少一个条件：

- 在事件早期发现能力上优于 Path 4。
- 收益不一定最高，但回撤、换手或持仓解释性更好。
- 能在价格信号出现前提供候选池，并在后续价格确认时提高命中率。
- 和现有策略持仓重合度低，对组合有增量价值。

如果 A 股验证有效，再进入 H 股同步阶段：把主题篮子映射到沪港通、A+H 公司和港股同产业链标的，并重新评估港股流动性和交易约束。

## 本轮执行计划（2026-06-04 04:18 CST）

- 上一轮候选/结果摘要：上一轮已创建最小事件篮子 `mrc_uec_ai_network_20260506_v0`，registry 状态为 `source_audit_started`，6 个冻结候选均为 `pending_source_review`，`include_in_backtest=false`。本轮继续先维护入口和审计状态，不把 Path 4 观察 seed 当成有效策略结论。
- 本轮巡检对象：`results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl`、`results/research/a_share/event_theme_audit.jsonl`。最终 guard 显示 `candidate_count=6 / frozen_candidate_count=6 / pending_audit_count=6 / backtest_ready_count=0`，最小 basket entry 已存在但下一步仍是 `source_audit_then_event_backtest_entry`。
- 本轮候选池：`300394.SZ 天孚通信`、`688498.SH 源杰科技`、`300502.SZ 新易盛`、`300308.SZ 中际旭创`、`688195.SH 腾景科技`、`300408.SZ 三环集团`。本轮仅追加审计记录为 `pending_primary_source_review`，没有把任何候选改为 `backtest_ready=true`。
- 未回测原因：Path 5 还缺公司公告、交易所披露或权威产业来源审计；在来源未通过前，不运行事件篮子回测，也不与 Path 4 强主题涌现做收益比较。当前命令状态为“不执行回测”，而不是缺口补跑。
- 下一轮 focus：最终 guard 给出 `ashare_path5 -> path4_comparison`。下一轮第一步仍不是回测，而是完成来源审计；建议先对 6 个冻结候选逐条补来源链接并更新 audit JSONL。若至少 4 个候选通过审计，首条回测入口命令预留为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`；若脚本仍不存在，则先实现最小 runner，再与 Path 4 `risk15/cap12` 和 coverage_penalty 做横向比较。

## 本轮执行计划（2026-06-08 06:05 CST）

- 上一轮候选/结果摘要：上一轮 Path 5 仍停在最小事件篮子入口阶段，6 个冻结候选均未通过来源审计；本轮继续只维护审计状态，不把 Path 4 强主题观察 seed 当成有效策略结论。
- 本轮候选 ID 与命令：巡检 `results/research/a_share/event_theme_registry.json`、`results/research/a_share/event_theme_candidates.jsonl` 与 `results/research/a_share/event_theme_audit.jsonl`；为 `mrc_uec_ai_network_20260506_v0` 的 6 个候选追加 audit 记录，状态均为 `pending_primary_source_review / frozen=true / backtest_ready=false`。本轮不运行事件篮子回测命令。
- 本轮审计候选：`300394.SZ 天孚通信`、`688498.SH 源杰科技`、`300502.SZ 新易盛`、`300308.SZ 中际旭创`、`688195.SH 腾景科技`、`300408.SZ 三环集团`。最终 guard 显示 `candidate_count=6 / frozen_candidate_count=6 / pending_audit_count=6 / backtest_ready_count=0`。
- 未回测原因：仍缺公司公告、交易所披露或权威产业来源审计；来源未通过前，不做收益比较，不进入 tracked/winner，也不与 Path 4 强主题涌现混同。
- 下一轮 focus：最终 guard 给出 `ashare_path5 -> event_backtest_entry`。下一轮第一步是实现或补齐最小 `scripts/event_theme_backtest_entry.py` runner，同时给 6 个候选补 primary source 链接并把通过者写入 audit JSONL；若至少 4 个通过，首条命令为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。

## 本轮执行计划（2026-06-08 12:13 CST）

- 上一轮候选/结果摘要：上一轮 Path 5 还缺 `event_backtest_entry` runner 与来源审计；本轮完成 6 个冻结候选的主来源补链，registry 状态从 `source_audit_started` 推到 `source_audited / entry_probe_ready`。
- 本轮候选 ID 与来源审计：`mrc_uec_ai_network_20260506_v0`，候选为 `300394.SZ 天孚通信`、`688498.SH 源杰科技`、`300502.SZ 新易盛`、`300308.SZ 中际旭创`、`688195.SH 腾景科技`、`300408.SZ 三环集团`。已在 `event_theme_candidates.jsonl` 标记 `audit_status=source_audited / include_in_backtest=true`，并向 `event_theme_audit.jsonl` 追加 6 条 `backtest_ready=true` 记录。
- 本轮命令：新增最小 runner `scripts/event_theme_backtest_entry.py`，并执行 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01`。
- 入口结果：事件日 `2026-05-06` 后 20 个交易日，等权 basket 收益 `41.75%`，seed 权重收益 `43.85%`；60/120 日因可用交易日不足仍为 `insufficient_data`。这只是 event entry probe，不进入 winner/tracked，不作为有效策略结论。
- Path 4 对比提示：Path 5 的最小篮子更像早期事件解释层；下一轮需把该 20 日结果与 Path 4 同期 `emergent_theme` 持仓重合、是否提前捕捉强龙头、以及来源可审计性做横向比较。
- 下一轮 focus：最终 guard 给出 `ashare_path5 -> event_basket_registry`。首条命令为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`；若脚本接口未支持 `--horizons`，先扩展 runner，再输出 Path 4 同期重合度与第二个事件篮子 registry 草案。

## 本轮执行计划（2026-06-08 17:37 CST）

- 上一轮候选/结果摘要：上一轮 runner 已可输出 20 日 entry probe，但缺 `--horizons` 参数和 Path 4 同期比较；本轮先补接口并重跑同一事件篮子。
- 本轮候选 ID 与命令：`mrc_uec_ai_network_20260506_v0`；命令为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`。
- 入口结果：6 个已审计冻结候选全部 eligible；事件日后 20 个交易日等权收益 `41.75%`、seed 权重收益 `43.85%`；40/60 日仍因事件距当前样本不足而 `insufficient_data`。这仍是 entry probe，不进入 winner/tracked。
- 巡检结论：registry/candidates/audit 入口完整，`pending_audit_count=0`；但尚未形成第二个事件篮子，且 Path 4 同期持仓重合度还需要结构化输出。
- 下一轮 focus：最终 guard 给出 `ashare_path5 -> event_backtest_entry`。下一轮第一步继续扩展 entry runner 输出 Path 4 `signal28/cap08` 同期持仓重合度，并补第二个事件篮子 registry 草案；首条命令为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`，同时新增一个 registry/candidates JSONL 审计任务。

## 本轮执行计划（2026-06-08 23:27 CST）

- 上一轮候选/结果摘要：上一轮 entry runner 已能输出 20 日事件篮子结果，但还需要与 Path 4 强主题涌现做结构化对照；本轮重跑入口结果并把 public/guard 同步到最新状态。
- 本轮候选 ID 与命令：`mrc_uec_ai_network_20260506_v0`；命令为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`。
- 入口结果：6 个冻结候选全部 eligible；事件后 20 个交易日等权收益 `41.75%`、seed 权重收益 `43.85%`；40/60 日仍因可用交易日不足为 `insufficient_data`。这仍是 entry probe，不写入 winner/tracked。
- 巡检结论：registry/candidates/audit 入口完整，`pending_audit_count=0`；本轮没有新增第二事件篮子，原因是 A股 active refresh 耗时显著超预期，新增实验预算已投给 Path1/2/3/4 与 HK Path1/2/5。
- 下一轮 focus：最终 guard 给出 `ashare_path5 -> path4_comparison`。下一轮第一步扩展 `event_theme_backtest_entry.py` 输出与 Path 4 `signal30_leader80` 同期持仓/收益对比；首条命令仍为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`，随后补第二个事件篮子 registry 草案。

## 本轮执行计划（2026-06-09 04:20 CST）

- 上一轮候选/结果摘要：上一轮 entry probe 仍缺 Path 4 结构化比较；本轮在同一已审计冻结篮子上重跑 20/40/60 日入口结果，并保持 entry probe 不进入 winner/tracked。
- 本轮候选 ID 与命令：`mrc_uec_ai_network_20260506_v0`；命令为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`。
- 入口结果：6 个冻结候选全部 eligible；事件后 20 个交易日等权收益 `41.75%`、seed 权重收益 `43.85%`。个股 20 日收益中 `300408.SZ 三环集团` 为 `59.52%`、`300394.SZ 天孚通信` 为 `57.32%`、`300502.SZ 新易盛` 为 `49.72%`、`300308.SZ 中际旭创` 为 `48.95%`，`688195.SH 腾景科技` 仅 `1.98%`；40/60 日仍因可用交易日不足为 `insufficient_data`。
- 巡检结论：registry/candidates/audit 入口完整，`pending_audit_count=0 / backtest_ready_count=6`；本轮没有新增第二事件篮子，原因是新增策略预算已投给 A股 Path2/3/4 与 HK Path1/2/3/4/6/7，且 Path5 当前更需要 Path4 对比输出。
- 下一轮 focus：最终 guard 给出 `ashare_path5 -> event_basket_registry`。下一轮第一步补第二个事件篮子 registry/candidates 草案，同时扩展 `event_theme_backtest_entry.py` 输出与 Path 4 `signal30/leader80` 同期持仓重合度；首条命令仍为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`。

## 本轮执行计划（2026-06-09 20:05 CST）

- 上一轮候选/结果摘要：上一轮 entry probe 已确认 `mrc_uec_ai_network_20260506_v0` 的 20 日事件后收益，但仍缺第二事件篮子和 Path 4 同期持仓重合度；本轮继续只维护入口和可审计候选，不进入 winner/tracked。
- 本轮候选 ID 与命令：`mrc_uec_ai_network_20260506_v0`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`。
- 入口结果：6 个冻结候选全部 eligible；事件后 20 个交易日等权收益 `41.75%`、seed 权重收益 `43.85%`。个股 20 日收益中 `300408.SZ 三环集团` 为 `59.52%`、`300394.SZ 天孚通信` 为 `57.32%`、`300502.SZ 新易盛` 为 `49.72%`、`300308.SZ 中际旭创` 为 `48.95%`、`688498.SH 源杰科技` 为 `33.00%`、`688195.SH 腾景科技` 为 `1.98%`；40/60 日仍因可用交易日不足为 `insufficient_data`。
- 巡检结论：最终 guard 显示 `basket_count=1 / frozen_candidate_count=6 / pending_audit_count=0 / backtest_ready_count=6`。本轮不把 entry probe 当成有效策略结论，也不写入 tracked。
- 下一轮 focus：最终 guard 给出 `ashare_path5 -> frozen_candidate_audit`，但当前 pending audit 为 `0`，因此该 focus 映射为“第二事件篮子审计池”。下一轮第一步新增第二个事件篮子 registry/candidates 草案并同步 audit JSONL；同时扩展 `event_theme_backtest_entry.py` 输出与 Path 4 `signal30/leader80` 同期持仓重合度。首条复核命令仍为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`。

## 本轮执行计划（2026-06-09 22:26 CST）

- 上一轮候选/结果摘要：上一轮 Path 5 仍只有一个已审计冻结篮子，缺第二事件篮子与 Path 4 同期重合度；本轮受 10 个新增/确认 ID 预算约束，继续只做入口复核，不进入 winner/tracked。
- 本轮候选 ID 与命令：`mrc_uec_ai_network_20260506_v0`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`。
- 入口结果：6 个冻结候选全部 eligible；事件后 20 个交易日等权收益 `41.75%`、seed 权重收益 `43.85%`。40/60 日仍因可用交易日不足为 `insufficient_data`，不作为有效策略结论。
- 巡检结论：最终 guard 显示 `basket_count=1 / frozen_candidate_count=6 / pending_audit_count=0 / backtest_ready_count=6`，入口完整但样本数远不足。未新增第二篮子原因：本轮新增策略预算已投给 A股 Path1/2/3/4 与 HK Path1/2/3。
- 下一轮 focus：最终 guard 给出 `ashare_path5 -> event_backtest_entry`。下一轮第一步扩展 runner 输出 Path 4 `signal30/leader80/prom16` 同期持仓重合度，并新增第二事件篮子 registry/candidates 草案；首条复核命令仍为 `.venv/bin/python scripts/event_theme_backtest_entry.py --basket-id mrc_uec_ai_network_20260506_v0 --sample-tags since_2025_01,since_2026_01 --horizons 20,40,60`。
