# 沪港通策略空间扩展计划

## 2026-06-04 10:16 CST 扩展复核结果

本轮按 HK 扩展线新增 Path6 与 Path7 各 1 个候选，Path4/Path5 仅做巡检和下一轮设计。实际回测命令与 HK Path1/2 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff26_exit38_v23_cost_repair,hkconnect_path2_equal_elastic_monthly_cost_guard_v17_repair,hkconnect_path6_large_liquid_core_biweekly_liquidity_mix_v3,hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v4`。

- Path4 多因子质量动量：本轮未新增回测；上一轮 v2 仍未修复 2026，下一轮候选设计为 `hkconnect_path4_quality_momentum_monthly_ytd_guard_v3`，目标是保留 `quality_momentum_monthly_ytd_guard` 的 2020/2023 稳定性并降低 2026 负收益。第一条命令：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path4_quality_momentum_monthly_ytd_guard_v3`。
- Path5 回踩续涨：本轮仍不跑同形回踩线。原因是 smoke 的 `pullback_continuation` 与 `breakout_retest` 已显示 2026/2023 断层；下一步必须先改 `pullback_definition`，加入成交质量或趋势再确认，不能直接注册第三个同形 id。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_biweekly_liquidity_mix_v3` 五窗口 CAGR `12.86% / 13.23% / 22.05% / 32.33% / 12.78%`，最大回撤 `-21.65% / -16.03% / -10.96% / -7.77% / -2.55%`。它把 2026 转正并被 `tracked_winners_hkconnect.json` 记录为 HK Path6 的窗口 winner，但长窗收益弱于首批 monthly smoke，robust 未切换。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v4` 五窗口 CAGR `16.12% / 14.56% / 22.77% / 28.66% / 8.73%`，最大回撤 `-19.20% / -14.96% / -10.75% / -10.57% / -5.01%`。它比 v3 更接近“双袖”结构且 2026 为正，但 2017/2020/2023 弱于 Path7 既有 biweekly smoke，不替换 robust。

`scripts/update_hkconnect_artifacts.py` 已刷新 HK tracked 与 Path1-3 图表；Path4-7 仍缺独立图表。本轮扩展线未触发 evict。下一轮第一优先级：先跑 Path4 `ytd_guard_v3`，第二优先级继续 Path6 防守核心的低换手版本；Path5 只做定义重写，不回测。

## 2026-06-04 04:18 CST 扩展复核结果

本轮按 HK Path4/6/7 扩展 focus 各新增 1 个候选，Path5 继续暂停同形回踩线。实际回测命令与 HK Path1 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path1_monthly_equal_buffered_weekly_overlay_soft_riskoff28_exit36_v22_drawdown_repair,hkconnect_path4_quality_momentum_monthly_2026_repair_v2,hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2,hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3`。

- Path4 多因子质量动量：`hkconnect_path4_quality_momentum_monthly_2026_repair_v2` 五窗口 CAGR `20.34% / 24.14% / 28.80% / 31.84% / -9.40%`，最大回撤 `-16.05% / -10.79% / -10.79% / -11.64% / -10.59%`，换手 `2.98x / 2.85x / 2.76x / 3.47x / 4.20x`。它弱于现有 `quality_momentum_monthly_ytd_guard`，没有替换 Path4 robust。
- Path5 回踩续涨：本轮未跑新增 id。原因是当前 `pullback_continuation` 和 `breakout_retest` 两个 smoke 已显示 2026/2023 断层，最终 guard focus 为 `pullback_definition`；下一轮必须先重写回踩定义或加入成交/趋势再确认，不能继续注册同形 smoke。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_monthly_liquidity_mix_v2` 五窗口 CAGR `12.90% / 14.60% / 22.41% / 30.79% / 1.82%`，最大回撤 `-17.85% / -14.82% / -6.18% / -2.73% / -3.83%`，换手 `1.23x / 1.26x / 1.11x / 1.70x / 2.67x`。本轮有效变化是 HK Path6 `since_2025_01` winner 切到该 v2；robust 仍是首批 `large_liquid_core_monthly_smoke`。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_core_sleeve_v3` 五窗口 CAGR `14.81% / 13.68% / 21.25% / 30.08% / 21.16%`，最大回撤 `-22.53% / -14.44% / -11.03% / -6.69% / -3.00%`，换手 `5.20x / 4.99x / 4.55x / 5.28x / 6.44x`。它显著改善 2026 与换手，但中长窗弱于现有 barbell smoke，未替换 robust；说明“核心袖”需要更明确的双 sleeve，而不是只靠 hybrid 权重。

最终 guard 为 `pass`，HK Path4 `4/4`、Path5 `2/2`、Path6 `4/4`、Path7 `4/4` complete；Path4/6/7 因新增 tracked 信号均为 `changed=true` 后下一次 guard 记录为 `stagnation_runs=1`。下一轮第一条扩展命令建议优先 Path7 真双 sleeve 结构：`.venv/bin/python backtest_hkconnect.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-strategy-ids hkconnect_path7_barbell_quality_growth_biweekly_dual_sleeve_v4`；Path4 下一候选为 `quality_momentum_monthly_ytd_guard_v3`，Path6 下一候选为 `large_liquid_core_biweekly_liquidity_mix_v3`，Path5 只做 pullback definition redesign 记录。

## 2026-06-03 22:20 CST 扩展复核结果

本轮在 Path4-7 扩展线只新增/确认 3 个 smoke 后续候选，Path5 暂停同形回踩线，避免继续复跑弱定义：

- Path4 多因子质量动量：`hkconnect_path4_quality_momentum_monthly_ytd_guard` 五窗口 CAGR `20.87% / 25.92% / 30.81% / 33.19% / -6.68%`，最大回撤 `-15.16% / -11.46% / -9.80% / -10.16% / -9.16%`，换手 `3.03x / 2.92x / 2.81x / 3.65x / 4.14x`。相对首批 monthly smoke，长中窗和 2026 均有改善，是本轮扩展线最有增量的候选；但 2026 仍负，不能直接切 robust。
- Path5 回踩续涨：本轮未跑新增 id。原因是首批 pullback/retest 两个 smoke 都显示 2026 或 2023 断层，继续同形只会扩充弱候选池；下一轮必须先修改回踩定义或加入再确认条件，再注册新 id。
- Path6 大市值高流动核心：`hkconnect_path6_large_liquid_core_monthly_ytd_guard` 五窗口 CAGR `14.17% / 16.15% / 25.33% / 29.20% / 9.28%`，最大回撤 `-17.17% / -14.33% / -5.35% / -2.68% / -2.64%`，换手 `1.24x / 1.25x / 1.15x / 1.50x / 2.60x`。它保留低回撤和正 2026，但长窗收益弱于首批 large-liquid smoke，适合作防守基线而不是收益 winner。
- Path7 杠铃组合：`hkconnect_path7_barbell_quality_growth_biweekly_defensive_v2` 五窗口 CAGR `18.39% / 17.54% / 26.42% / 33.29% / 7.11%`，最大回撤 `-20.17% / -13.70% / -10.81% / -11.15% / -5.66%`，换手 `10.40x / 10.10x / 9.97x / 13.00x / 11.63x`。相对首批 biweekly smoke 收益略弱但 2026 正，说明当前单信号近似还不够，需要真正双 sleeve。

`scripts/update_hkconnect_artifacts.py` 已刷新 Path1-3 tracked 与图表；Path4-7 仍只进入 tracked/public/live payload，尚无独立图表。最终 guard 为 `pass`，HK Path4-7 各 `2/2 complete`。下一轮第一条扩展命令建议优先 Path4 ytd guard 的 2026 转正修复，其次 Path6 市值/流动性混合权重；Path5 必须先重定义，不直接新增同形回踩。

## 2026-06-03 smoke 结果

本轮已把扩展计划中的 Path 4-7 先落成 8 个可跑 smoke 候选，并完成五窗口回测：

- Path 4 多因子质量动量：
  - `hkconnect_path4_quality_momentum_monthly_smoke`：CAGR `19.77% / 23.65% / 29.36% / 30.85% / -7.49%`，最大回撤 `-12.26% / -12.26% / -12.26% / -12.26% / -10.22%`，换手 `3.16x / 3.10x / 3.02x / 3.91x / 4.08x`。结论：长中窗稳、回撤浅，2026 观察窗转负，需要做年内保护。
  - `hkconnect_path4_liquidity_momentum_biweekly_smoke`：CAGR `16.83% / 16.03% / 6.40% / 54.48% / 20.13%`，最大回撤 `-33.29% / -33.29% / -33.07% / -15.47% / -7.09%`，换手约 `10x-12x`。结论：短窗强但 2023 断层和回撤过深，不宜作为下一批主线。
- Path 5 回踩续涨：
  - `hkconnect_path5_pullback_continuation_monthly_smoke`：CAGR `20.01% / 20.14% / 19.15% / 23.80% / -17.27%`，最大回撤 `-21.90% / -14.54% / -14.54% / -14.43% / -14.52%`。
  - `hkconnect_path5_breakout_retest_biweekly_smoke`：CAGR `14.23% / 10.67% / 11.01% / 33.82% / -3.74%`，换手约 `16x-19x`。
  - 结论：回踩线首批没有显示增量优势，下一批不继续简单回踩/突破回踩，除非先改掉买入端必须 `recent_1m > 0` 的约束或增加更明确的再确认条件。
- Path 6 大市值高流动性稳健线：
  - `hkconnect_path6_large_liquid_core_monthly_smoke`：CAGR `15.15% / 17.90% / 25.99% / 30.50% / 8.21%`，最大回撤 `-16.62% / -13.54% / -5.32% / -2.97% / -2.49%`，换手 `1.16x / 1.23x / 1.07x / 1.45x / 2.53x`。
  - `hkconnect_path6_lowvol_liquid_biweekly_smoke`：CAGR `14.58% / 14.99% / 23.53% / 29.77% / 20.89%`，最大回撤 `-19.99% / -15.91% / -10.54% / -8.16% / -2.39%`，换手 `2.09x / 2.03x / 1.78x / 2.06x / 4.07x`。
  - 结论：收益不是最强，但回撤、换手、2026 观察窗都明显有防守价值，是下一批最值得扩的方向。
- Path 7 杠铃组合线：
  - `hkconnect_path7_barbell_quality_growth_monthly_smoke`：CAGR `16.68% / 21.15% / 26.07% / 18.11% / -11.76%`，最大回撤 `-18.55% / -15.34% / -10.37% / -10.36% / -10.41%`。
  - `hkconnect_path7_barbell_quality_growth_biweekly_smoke`：CAGR `19.36% / 18.17% / 28.71% / 34.24% / 8.30%`，最大回撤 `-17.64% / -13.24% / -10.79% / -11.16% / -6.08%`，换手约 `11x-14x`。
  - 结论：双周杠铃比月度更有观察价值，但当前实现只是单组合信号近似，还不是严格核心/卫星双 sleeve。

本轮同步后，HK coverage 从 `229/229` 更新为 `237/237`，最终 guard 为 `pass / blocking_missing=0 / warning_missing=0`。`tracked_winners_hkconnect.json` 已包含 Path 4-7 的 strategies payload；现有 `update_hkconnect_artifacts.py` 图表仍只画 Path 1-3，下一步如果扩展线继续推进，需要补 Path 4-7 的独立图表与 track 摘要。

下一批建议：

1. 优先扩 Path 6：`large_liquid_core` 增加 signal weight、市值/流动性混合权重、月度/双周各 2-3 个。
2. 次优扩 Path 4：保留 `quality_momentum_monthly`，做 2026 guard 和轻微容量约束。
3. Path 7 只扩双周版本，并尽快实现真正的核心/卫星双 sleeve；当前单信号近似只能当 smoke。
4. Path 5 暂停同形回踩线，先调整回踩定义或新增再确认规则。
5. Path 8 仍是第二阶段，等南向/AH/股息/估值数据合同确定后再跑。

## 背景

当前沪港通策略探索明显少于 A 股：

- 沪港通对比表约 226 个 `strategy_id`，A 股对比表约 2563 个基础策略。
- 沪港通现有路径分布相对均衡但偏少：Path 1 约 72 个、Path 2 约 77 个、Path 3 约 77 个。
- 现有沪港通信号家族主要集中在 `path1_moderate`、`path1_lowvol`、`path2_breakout`、`path2_theme`、`path2_elastic`。
- 权重方法高度集中在 `equal_weight`，市值、低波、流动性、信号强度类权重还没有形成足够宽的对照组。

这份计划的目标不是继续微调少数参数，而是先扩大沪港通的正交探索空间，让策略候选数、信号家族和权重结构接近 A 股研究平台的广度。

## 原则

1. 第一阶段只用现有沪港通数据字段，不引入新的外部数据依赖。
2. 新路径先作为 tracked-only 实验，不直接进入正式 winner。
3. 每个候选都在 `since_2017_01`、`since_2020_01`、`since_2023_01`、`since_2025_01`、`since_2026_01` 五个窗口观察。
4. 新路径要和现有 Path 1/2/3 保持职责分离，避免只是换名字的参数组合。
5. 每批新增先做小规模 smoke 组，确认结果分布后再批量扩容。

## 现有可复用因子

第一阶段可以优先复用这些已在沪港通回测中可得的字段和衍生分数：

- 趋势：`momentum_12_1`、`momentum_6_1`、`momentum_3_1`、`recent_1m_return`。
- 放量与突破：`amount_surge_ratio`、`breakout_signal`。
- 质量与交易可行性：`liquidity_quality_scores`、成交额、停牌/缺失过滤。
- 防守：`low_vol_scores`、回撤控制、risk-off overlay。
- 规模：`total_mv`、`small_cap_scores`。

这些字段足够先形成 4 到 5 条新的沪港通研究线，不需要等待新增数据源。

## 新路径候选

### Path 4：多因子质量动量线

目标：把“趋势强”从单一动量扩展为趋势、流动性、低波、规模的组合评分。

候选信号家族：

- `hk_quality_momentum`：中期动量 + 流动性质量 + 低波过滤。
- `hk_liquidity_momentum`：动量强度 + 成交活跃度，偏向可交易的大中盘。
- `hk_defensive_momentum`：动量不弱 + 低波 + 风险控制，服务回撤更小的组合。
- `hk_signal_blend`：对 12-1、6-1、3-1 动量和突破做 rank blend。

第一批规模：40 到 60 个候选。

### Path 5：回踩续涨线

目标：寻找中期趋势仍在、短期回踩后有继续上涨可能的港股标的，补足现有突破策略对“回踩买点”的覆盖。

候选信号家族：

- `hk_pullback_continuation`：6-1 或 12-1 动量较强，但 1 个月收益回落。
- `hk_retest_breakout`：前期突破后短期未破坏趋势。
- `hk_volume_confirmed_pullback`：回踩过程中成交质量不恶化。

第一批规模：30 到 45 个候选。

### Path 6：大市值高流动性稳健线

目标：修正现有沪港通组合中过度依赖等权的结构，专门建立大市值、强流动性、低波动的基线。

候选权重和信号：

- `hk_large_liquid_core`：市值和成交额双过滤。
- `hk_lowvol_liquid_core`：低波 + 流动性。
- `hk_hybrid_mv_signal`：市值权重和信号强度权重混合。
- `hk_liquidity_weight`：按流动性质量分配权重，设置单票上限。

第一批规模：30 到 45 个候选。

### Path 7：杠铃组合线

目标：把防守核心和弹性卫星放在同一个组合结构里评估，而不是只比较单一信号。

组合结构：

- 核心仓：低波、高流动性、大市值标的。
- 卫星仓：突破、主题或高成长动量标的。
- 配比组：`70/30`、`60/40`、`50/50`。
- 再平衡：月度为主，双周作为对照。

第一批规模：20 到 30 个候选。

### Path 8：港股专属数据线（第二阶段）

目标：引入真正能体现港股差异的数据，但放在第二阶段，避免第一轮探索被数据接入拖慢。

潜在数据：

- 南向资金持股或成交变化。
- AH 溢价、A+H 映射关系。
- 股息率、估值、盈利修正。
- 行业龙头与港股稀缺资产标签。

进入条件：先定义稳定的数据合同和缺失处理规则，再纳入回测。

## 第一阶段候选预算

建议先新增 120 到 180 个候选，而不是一次性扩到 500 个以上。

| 新路径 | 初始候选数 | 主要作用 |
| --- | ---: | --- |
| Path 4 多因子质量动量 | 40-60 | 扩展信号组合空间 |
| Path 5 回踩续涨 | 30-45 | 补足非突破买点 |
| Path 6 大市值高流动性 | 30-45 | 建立稳健权重基线 |
| Path 7 杠铃组合 | 20-30 | 评估组合结构 |

第一批可以先注册 20 到 30 个 smoke 候选，跑完五个窗口后再继续扩容。

## 代码接入建议

后续如果开始实现，建议按这个顺序推进：

1. 在 `build_hk_signal_scores` 中增加新信号家族，先复用现有字段。
2. 在 `build_hk_base_weights` 中增加 `liquidity_weight`、`low_vol_inverse`、`signal_score_weight`、`hybrid_mv_signal` 等权重方法。
3. 增加 `HK_PATH4_VARIANTS`、`HK_PATH5_VARIANTS`、`HK_PATH6_VARIANTS`、`HK_PATH7_VARIANTS`，或抽一个简单 helper 生成候选。
4. 新路径稳定后再同步更新 `scripts/update_hkconnect_artifacts.py`、`scripts/export_live_platform_data.py`、`scripts/generate_public_snapshot.py`。
5. 在研究 guard 中增加每条新路径的候选上限，避免单一路径快速膨胀。

## 判断标准

保留一条新路径需要满足至少一个条件：

- 在某个关键窗口明显优于现有沪港通 winner。
- 虽然收益不是最强，但回撤、换手、稳定性明显更好。
- 与现有 Path 1/2/3 的持仓重合度低，提供新的组合角色。

如果连续三批候选都没有改善，也没有独特组合价值，就归档该路径，避免长期占用迭代预算。
