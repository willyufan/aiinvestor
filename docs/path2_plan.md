# Path 2 研究计划

## 2026-08-08 二次迭代记录（约 07:30 CST）

### 上一轮候选与结果摘要

- 本轮确认 `medium_cycle_growth` v68/v71。假设是中周期风险/退出折中能修复 2023/2026；实际 2020/2023/2026 CAGR 为 `2.32%/-5.69%/-39.64%`、`1.91%/-5.83%/-40.53%`，CAGR 与 MaxDD 均破坏稳定性，均 `reject`。
- v70 对照为 `5.98%/2.20%/17.04%`，但平均 turnover 约 `11.60x` 且绝对收益弱，维持 `robust_observation`：进入观察位，不是强稳定 winner。winner/robust/tracked ID 无变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm94_caution58_cap16_cost_guard_v68_medium_cycle_growth_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk26_mom_exit46_reconfirm96_caution56_cap18_cost_guard_v71_medium_cycle_growth_repair,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### 下一轮 focus 提示

- 最终 guard focus 仍为 `medium_cycle_growth`；停止 v68/v71 同形扩参，改验 v72/v79，目标是在不触发 2020/2023 护栏下恢复中窗收益；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top16_risk28_mom_exit48_reconfirm94_caution58_cap20_cost_guard_v72_medium_cycle_growth_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### Focus 候选池

- `medium_cycle_growth`：v72、v79；`risk_reconfirm_sensitivity`：v42、v34；`underrepresented_families`：v62、v63；`capacity_and_cost_stress`：v74-equal、v74-total；`biweekly_rebalance_aggressive`：v70、v78。

## 2026-08-08 迭代记录（约 01:30 CST）

### 上一轮候选与结果摘要

- `medium_cycle_growth` 确认 v67 equal/total 与 v69 total。假设是中周期参数可提升 2020 收益并压低换手；实际 2020/2023/2026 CAGR 分别为 `-3.70%/-4.57%/-42.46%`、`1.89%/-5.85%/-40.53%`、`2.38%/-5.82%/-40.36%`，均破坏跨窗稳定性，判 `reject`。
- v70 对照为 `5.98%/2.20%/17.04%`、平均 turnover `11.60x`，维持 `robust_observation`：进入观察位，不是强稳定 winner。winner/robust/tracked 无变化，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v67_medium_cycle_growth_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v67_medium_cycle_growth_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top11_risk28_mom_exit48_reconfirm94_caution60_cap18_cost_guard_v69_medium_cycle_growth_repair,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### 下一轮 focus 提示

- 继续 `medium_cycle_growth`，停止 v67/v69 同形扩参，改验 v68/v71；目标是修复 2023/2026 负收益，同时使平均 turnover 低于 v70。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm94_caution58_cap16_cost_guard_v68_medium_cycle_growth_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk26_mom_exit46_reconfirm96_caution56_cap18_cost_guard_v71_medium_cycle_growth_repair,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### Focus 候选池

- `medium_cycle_growth`：v68、v71；`risk_reconfirm_sensitivity`：v42、v34；`underrepresented_families`：v62、v63。
- `capacity_and_cost_stress`：v74-equal、v74-total；`biweekly_rebalance_aggressive`：v70、v78；`weekly_rebalance_aggressive`：weekly-growth-v1、weekly-growth-v2（注册后启用）。

## 2026-08-07 二次迭代记录（约 07:24 CST）

### 上一轮候选与结果摘要

- `underrepresented_families` 确认 v64/v78，并与 v70 robust observation 同端点比较。v64/v78 的 2020/2023/2026 CAGR 为 `7.44%/-0.40%/13.42%`、`5.87%/1.96%/14.52%`；相对弱 robust 未触发二次硬护栏，但五窗平均 turnover 仍为 `11.61x/11.58x`，均 `keep_watch`，不能据此挑战正式窗口 winner。
- v70 为 `5.78%/2.09%/14.65%`、平均 turnover `11.60x`，维持 `robust_observation`：进入观察位，不是强稳定 winner。相邻验证拒绝 v64/v78/v70 对正式窗口 winner 的晋级，winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### 下一轮 focus 提示

- 最终 guard 仍指向 `underrepresented_families`；v64/v78 已确认但换手偏高，下一轮改验同族尚未确认的 v62/v63，并保留 v70。目标是平均 turnover 显著低于 `10x` 且 2020/2023 不触发护栏；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap16_cost_guard_v62_underrepresented_lowturn,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### Focus 候选池

- `medium_cycle_growth`：v67、v69；`risk_reconfirm_sensitivity`：v42、v34；`underrepresented_families`：v62、v63（v64/v78 已确认）。
- `capacity_and_cost_stress`：v74 双底座、v85（待注册）；`biweekly_rebalance_aggressive`：v70、v78；`weekly_rebalance_aggressive`：注册有效生成器后再入池。

## 2026-08-07 迭代记录

### 上一轮候选与结果摘要

- 按 `risk_reconfirm_sensitivity` 确认 v56/v66，并与 v70 artifact robust 同窗比较。v56 的 2020/2023/2026 CAGR 为 `2.60%/-5.87%/-41.90%`，多项护栏触发；v66 为 `5.74%/1.44%/-37.50%`，仍触发中窗风险护栏，均 `reject`。
- v70 为 `5.78%/2.09%/14.65%`，五窗平均 turnover 约 `10.02x`，仍是绝对收益偏弱且容量/成本受限的 `robust_observation`：进入观察位，不是强稳定 winner。无 evict/archive，正式 tracked 暂未改变。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-06 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk30_mom_exit48_reconfirm92_caution60_cap22_cost_guard_v56_risk_reconfirm_sensitivity,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### 下一轮 focus 提示

- v56/v66 同形停止；最终 guard 已轮转到 `underrepresented_families`，下一轮重新确认不同风险/退出档的 v64/v78，并保留 v70。观察条件是 2020/2023 同时改善、2026 非负且平均 turnover 显著低于 `10x`；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### Focus 候选池

- `risk_reconfirm_sensitivity`：v42、v34；`medium_cycle_growth`：v67、v69；`underrepresented_families`：v64、v78。
- `capacity_and_cost_stress`：v74、v85；`biweekly_rebalance_aggressive`：v70、v78；`weekly_rebalance_aggressive`：先注册有效生成器后再入池。

## 2026-08-06 迭代记录

### 上一轮候选与结果摘要

- 按 underrepresented 双周线确认 v64/v78，并在 weighted 更新后补跑最终 robust `v70_underrepresented_lowturn` 到同一端点。v64/v78/v70 的 2020/2023/2026 CAGR 分别为 `7.18%/-0.55%/10.25%`、`5.63%/1.82%/11.60%`、`5.53%/1.93%/11.59%`；v64/v78 未触发中窗硬护栏但五窗平均 turnover 约 `11.6x`，均 `keep_watch`。
- `quality_value_industry` 在 2020 CAGR `-3.09%`，相对 v70 下降 `8.62pp` 且 2023 MaxDD 恶化超过 `5pp`，判 `reject`。v70 被 artifact 推为 Path2 robust，但绝对收益弱、换手高，只判 `robust_observation`：进入观察位，不是强稳定 winner。candidate-pass 巡检 `816` 条；正式 window winner/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-05 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### 下一轮 focus 提示

- 最终 guard 已轮转到 `risk_reconfirm_sensitivity`；v64/v78 仅留下高换手观察，下一轮以新 artifact robust v70 为对照复核 v56/v66 的风险敏感性，要求 2020/2023 同时改善且平均 turnover 明显低于 `11.6x`。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk30_mom_exit48_reconfirm92_caution60_cap22_cost_guard_v56_risk_reconfirm_sensitivity,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### Focus 候选池

- `risk_reconfirm_sensitivity`：v56、v66；`medium_cycle_growth`：v54、v55；`underrepresented_families`：v64、v78。
- `capacity_and_cost_stress`：v74、v85；`biweekly_rebalance_aggressive`：v70、v78；`weekly_rebalance_aggressive`：先注册有效生成器后再入池。

## 2026-08-05 二次迭代记录（约 07:29 CST）

### 上一轮候选与结果摘要

- 按 `risk_reconfirm_sensitivity` 确认 v56/v66，并与 artifact robust observation `quality_value_industry` 同窗比较。v56/v66 的 2020/2023/2026 CAGR 为 `2.63%/-5.88%/-41.23%`、`5.74%/1.70%/-36.77%`；两者相对对照的 2023 CAGR 下降 `21.62/14.03pp`，均 `reject`，风险再确认不能修复跨窗稳定性。
- `quality_value_industry` 本身为 `-3.18%/15.74%/-7.93%`、minCAGR 为负，只维持 `robust_observation`：进入观察位，不是强稳定 winner。candidate-pass 巡检 `814` 条；正式 window winner/robust/tracked ID 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk30_mom_exit48_reconfirm92_caution60_cap22_cost_guard_v56_risk_reconfirm_sensitivity,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### 下一轮 focus 提示

- v56/v66 同形已证伪，`risk_reconfirm_sensitivity` 当前 active 边界耗尽；下一轮先切到未归档的 underrepresented v64/v78，验证不同风险/退出档能否同时修复 2020/2023，并继续与当前 artifact robust observation 比较。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### Focus 候选池

- `medium_cycle_growth`：v54、v55；`risk_reconfirm_sensitivity`：v56、v66（本轮 reject，停止同形扩参）。
- `underrepresented_families`：v64、v78；`capacity_and_cost_stress`：v74、v85；`biweekly_rebalance_aggressive`：v70、v78。

## 2026-08-05 迭代记录（约 01:28 CST）

### 上一轮候选与结果摘要

- 按 `medium_cycle_growth` 确认 v79/v81，并复核 v70；三者 2020/2023/2026 CAGR 分别为 `5.33%/1.64%/-40.04%`、`10.15%/1.59%/-39.34%`、`5.13%/1.68%/7.36%`。相对当前 robust observation `quality_value_industry`，三条都破坏 2023 稳定性，全部 `reject`。
- 假设“更低换手的中周期形态能同时修复 2020/2023”未获支持；v81 只改善 2020，短窗与 2023 仍失败。candidate-pass 巡检 `814` 条；weighted 后 robust 刷新为 `quality_value_industry`，但 minCAGR 仍为负，进入观察位，不是强稳定 winner。window winners 未替换，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### 下一轮 focus 提示

- 最终 guard 仍为 `medium_cycle_growth`。停止 v79/v81 同形，改验较早但未归档的 v54/v55 中周期风险/质量边界，要求 2023 CAGR 缺口小于 3pp、2026 非负且 turnover 不高于当前 robust；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v54_medium_cycle_rebound,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit46_reconfirm94_caution58_cap20_cost_guard_v55_medium_cycle_quality,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### Focus 候选池

- `medium_cycle_growth`：v54、v55；`underrepresented_families`：v64、v78。
- `risk_reconfirm_sensitivity`：v56、v66；`capacity_and_cost_stress`：v74、v85；`biweekly_rebalance_aggressive`：v70、v78。

## 2026-08-04 二次迭代记录（约 07:29 CST）

### 上一轮候选与结果摘要

- 按 `risk_reconfirm_sensitivity` 五窗口确认 v42 total-mv/equal-weight，并以 active robust v70 同窗对照。两条 v42 的 2020/2023/2026 CAGR 分别为 `12.08%/-3.10%/-38.81%`、`10.39%/-5.50%/-51.69%`，中窗与短窗严重退化，均 `reject`；风险再确认无法修复跨窗稳定性。
- v70 为 `4.93%/1.54%/5.01%`，五窗为正但绝对收益弱，且五窗 turnover 约 `6.81x-17.94x`，仅 `robust_observation`：进入观察位，不是强稳定 winner。candidate-pass 已巡检 814 个候选；winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

五窗口 scorecard 见 `results/research/a_share/research_iteration_scorecard_20260804_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `underrepresented_families`。v42 同形停止，下一轮改验未归档 active v64/v78，以不同风险/退出档挑战 v70，只有 2020/2023 不触发护栏且 turnover 可接受才保留；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### Focus 候选池

- `underrepresented_families`：v64-underrepresented-lowturn、v78-underrepresented-repair；`risk_reconfirm_sensitivity`：v56、v66。
- `medium_cycle_growth`：v30-medium-cycle、v37-medium-cycle-repair；`capacity_cost_stress`：v74-capacity-cost、v85-cap14-cost-guard-retest。

## 2026-08-04 迭代记录（约 01:30 CST）

### 上一轮候选与结果摘要

- `medium_cycle_growth` 五窗口确认 v30、v37 与旧 quality/value 对照。v30/v37 的 2020 CAGR 约 `11.91%`，但 2023 CAGR 分别为 `-2.83%/-2.86%`、2026 均为 `-38.75%`，对当前 robust v70 命中 2023 CAGR/MaxDD 护栏，均 `reject`；quality/value 也因 2020 与短窗退化 `reject`。短周期收益修复假设未获跨窗口支持。
- artifact 同步将当前 robust 观察位更新为 v70：2020/2023/2026 CAGR `4.93%/1.54%/5.01%`，五窗均值 `7.74%`、最小值 `1.54%`，仅判 `robust_observation`；进入观察位，不是强稳定 winner。v30 的局部 window 排名不等于 `promote`。无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-08-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

完整五窗口 scorecard：`results/research/a_share/research_iteration_scorecard_20260804.json`。

### 下一轮 focus 提示

- 最终 guard 继续 `medium_cycle_growth`；停止 v30/v37 同形扩参，改验 v79/v81 的低换手中周期形态是否能保住 2023 稳定性；第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn
```

### Focus 候选池

- `medium_cycle_growth`：v79-medium-cycle-repair、v81-midcycle-lowturn；`risk_reconfirm_sensitivity`：v42-risk-reconfirm、v79-medium-cycle-repair。
- `underrepresented_families`：v70-underrepresented-lowturn、v78-underrepresented-repair；`capacity_cost_stress`：v74-capacity-cost-stress、v85-cap14-cost-guard-retest。

## 2026-08-03 二次迭代记录（07:18 CST）

### 上一轮候选与结果摘要

- `medium_cycle_growth` 五窗口确认 v45/v48。两条挑战者的 2020/2023/2026 CAGR 为 `6.97%/3.40%/-34.41%`、`8.32%/3.37%/-33.06%`；虽改善弱 robust 的 2020 窗口，但 2023 CAGR/Sharpe 明显破坏稳定性，均 `reject`。
- quality-value robust 的 2020/2023/2026 CAGR 为 `-3.09%/16.04%/-10.39%`，minCAGR 为负，只作 `robust_observation`：进入观察位，不是强稳定 winner。window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v45_medium_cycle_growth,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803_iter2.json`。

### 下一轮 focus 提示

- v45/v48 证明“只修 2020”不可接受；下一轮 `medium_cycle_growth` 回到 v30/v37 的较宽容量形态，必须同时守住 2023 并修复 2026。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### Focus 候选池

- `medium_cycle_growth`：v30-medium-cycle、v37-medium-cycle-repair；`risk_reconfirm_sensitivity`：v42-risk-reconfirm、v79-medium-cycle-repair。
- `capacity_and_cost_stress`：v44-underrep-repair、v46-capacity-cost；`underrepresented_families`：v70-lowturn、v78-repair。

## 2026-08-03 迭代记录（01:18 CST）

### 上一轮候选与结果摘要

- 按 `capacity_and_cost_stress` 五窗口确认 v45 total-mv/equal-weight。两条挑战者的 2020/2023/2026 CAGR 为 `4.39%/3.47%/-37.39%`、`8.27%/6.13%/-35.35%`，2023 相对 current robust 分别下降 `12.57pp/9.91pp`，均触发稳定性护栏并 `reject`。
- current robust quality-value-industry 的 2020/2023/2026 CAGR 为 `-3.09%/16.04%/-10.39%`，minCAGR 为负，只作 `robust_observation`：进入观察位，不是强稳定 winner。Path2 candidate-pass 已完成 814 个候选巡检；正式 winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260803.json`。

### 下一轮 focus 提示

- capacity-stress 未守住 2023，下一轮转 `medium_cycle_growth` 的 v45/v48，要求 2023 CAGR 不下降超过 3pp，且 2026 不再出现超过 30% 的负收益。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v45_medium_cycle_growth,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### Focus 候选池

- `capacity_and_cost_stress`：v44-underrep-repair、v45-capacity-stress；`medium_cycle_growth`：v45-top10-cap20、v48-top10-cap16。
- `underrepresented_families`：60/40-v70、70/30-v70；`risk_reconfirm_sensitivity`：v42-total、v42-equal。
- `drawdown_repair`：v37、v52。

## 2026-08-02 二次迭代记录（08:42 CST）

### 上一轮候选与结果摘要

- 二次确认 60/40-v70、70/30-v70 与 current robust。两条挑战者 2020/2023/2026 CAGR 为 `5.27%/1.72%/8.90%`、`2.29%/2.24%/-5.89%`，2023 均落后 robust 约 14pp，`reject`。
- current robust 为 `-3.09%/16.04%/-10.39%`，只作 `robust_observation`：进入观察位，不是强稳定 winner。假设“欠代表双周族能守住中窗并降成本”再次未获支持；无 winner/robust/tracked 变化与 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802_iter2.json`。

### 下一轮 focus 提示

- 转 `capacity_and_cost_stress`，比较 v45 total/equal 与 robust，要求换手下降且 2020/2023 不触发护栏。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### Focus 候选池

- `capacity_and_cost_stress`：v44-underrep-repair、v45-capacity-stress；`underrepresented_families`：60/40-v70、70/30-v70。
- `medium_cycle_growth`：v45-top10-cap20、v48-top10-cap16；`risk_reconfirm_sensitivity`：v42-total、v42-equal；`drawdown_repair`：v37、v52。

## 2026-08-02 迭代记录（08:12 CST）

### 上一轮候选与结果摘要

- 按 `underrepresented_families` 五窗口确认 v70 的 60/40 与 70/30 等权双周线，并与 current robust quality-value-industry 同窗比较。60/40 的 2020/2023/2026 CAGR 为 `5.27%/1.72%/8.90%`，70/30 为 `2.29%/2.24%/-5.89%`；两条 2023 CAGR 相对 robust 均下降约 `14pp`，且换手均值 `11.63x/12.13x`，全部 `reject`。
- current robust 为 `-3.09%/16.04%/-10.39%`，minCAGR 为负，只判 `robust_observation`：进入观察位，不是强稳定 winner。实验假设“欠配双周族能降低单一家族偏置并守住中窗”未获支持；正式 window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260802.json`。

### 下一轮 focus 提示

- v70 双周线已证伪，下一轮转 `capacity_and_cost_stress` 的 v45 total/equal 形态，目标是把换手压回 current robust 附近且守住 2020/2023。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### Focus 候选池

- `underrepresented_families`：60/40-v70、70/30-v70；`capacity_and_cost_stress`：v44-underrep-repair、v45-capacity-stress。
- `medium_cycle_growth`：v45-top10-cap20、v48-top10-cap16；`risk_reconfirm_sensitivity`：v42-total、v42-equal。
- `drawdown_repair`：v37、v52。

## 2026-08-01 二次迭代记录（07:26 CST）

### 上一轮候选与结果摘要

- `risk_reconfirm_sensitivity` 五窗口确认 v42 total-mv/equal-weight，并与 current robust `quality_value_industry_cost_guard_reconfirm` 同窗比较。v42 两底座的 2020 CAGR 为 `12.14%/10.45%`，但 2023 CAGR 降至 `-1.98%/-4.43%`、2026 为 `-35.07%/-48.89%`，均触发中窗护栏并 `reject`。
- current robust 的 2020/2023/2026 CAGR 为 `-3.09%/16.04%/-10.39%`，minCAGR 仍负，只判 `robust_observation`：进入观察位，不是强稳定 winner。实验假设“v42 风险再确认能修复负窗同时守住 2023”未获支持；window winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260801_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 focus=`underrepresented_families / rotate`：v42 已证伪，转向 60/40 与 70/30 的 v70 双周低换手线，检查能否降低单一家族偏置并守住 2020/2023。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### Focus 候选池

- `risk_reconfirm_sensitivity`：v56-total-mv、v56-equal-weight。
- `medium_cycle_growth`：v45-top10-cap20、v48-top10-cap16。
- `underrepresented_families`：40/60-v70、60/40-v78；`capacity_and_cost_stress`：v44-underrep-repair、v45-capacity-stress。
- `drawdown_repair`：v37、v52。

## 2026-08-01 迭代记录（01:20 CST）

### 上一轮候选与结果摘要

- `medium_cycle_growth` 确认 v79 total-mv/equal-weight 与 2023/2025 window incumbent `aggr_10_90_prom6`。三者 2020/2023/2026 CAGR 分别为 `5.43%/3.39%/-33.72%`、`2.23%/-6.49%/-37.48%`、`-0.32%/17.66%/-18.86%`；v79 两底座触发中窗护栏，aggr 则有两个负收益窗口，全部 `reject`。
- 当前 artifact robust 为 `...quality_value_industry_cost_guard_reconfirm`，minCAGR `-3.09%`，只能 `robust_observation`：进入观察位，不是强稳定 winner。实验假设“v79 的更低 risk/cap 可修复中周期收益与容量”未获支持；window winner/robust/tracked 未因本轮候选改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6
```

### 下一轮 focus 提示

- focus=`medium_cycle_growth`：v79 已证伪，下一轮转 v45/v48 的不同 top-N 与 risk/cap 组合，并继续与 current robust 同窗比较。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-31 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v45_medium_cycle_growth,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_industry_cost_guard_reconfirm
```

### Focus 候选池

- `medium_cycle_growth`：v45-top10-cap20、v48-top10-cap16。
- `underrepresented_families`：40/60-v70、60/40-v78；`drawdown_repair`：v37、v52。
- `capacity_and_cost_stress`：v44-underrep-repair、v45-capacity-stress；`risk_reconfirm_sensitivity`：v42-total-mv、v42-equal-weight。

## 2026-07-31 迭代记录（07:55 CST）

### 上一轮候选与结果摘要

- `medium_cycle_growth` 确认 v30 与 v37。二者 2020 CAGR 都为 `11.89%`，但 2023 约 `-3.1%`、2026 `-42.18%`；相对运行前 robust `aggr_10_90_prom6` 的 2023 CAGR 下降约 `20pp`，均 `reject`。v30 虽被 artifact 推为 2017/2020 window winner，但只是路径内排序变化，不构成 promote。
- `aggr_10_90_prom6` 的 2020/2023/2026 CAGR 为 `-0.55%/16.92%/-26.27%`，继续 `robust_observation`：进入观察位，不是强稳定 winner。实验假设“中周期风险/退出微调可保住 2020 弹性并修复回撤”未获支持；不再扩同形参数，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6
```

### 下一轮 focus 提示

- focus=`medium_cycle_growth`：停止 v30/v37 邻近扩参，改验更低 risk/cap 的 v79 total-mv 与 equal-weight 形态。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-30 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair
```

### Focus 候选池

- `medium_cycle_growth`：v79-total-mv、v79-equal-weight。
- `underrepresented_families`：60/40-biweekly-v70、70/30-biweekly-v70。
- `drawdown_repair`：v37-medium-cycle-repair、v79-medium-cycle-repair。
- `capacity_cost`：cap18-v79、cap22-v30。

## 2026-07-30 二次迭代记录（07:24 CST）

### 上一轮候选与结果摘要

- 按 `underrepresented_families` 五窗口确认 v70 的 60/40、70/30 等权双周形态，并与正式 robust `aggr_10_90_prom6` 同窗比较。两条候选 2023 CAGR 仅 `1.88%/1.96%`，相对 robust `18.19%` 下降约 `16.31pp/16.23pp`，Sharpe 也下降约 `0.99`；70/30 的 2026 CAGR 为 `-4.25%`，全部 `reject`。
- `aggr_10_90_prom6` 的 2020/2026 CAGR 为 `-0.09%/-12.78%`，虽仍被 artifact 保留为 Path2 robust，但只判 `robust_observation`：进入观察位，不是强稳定 winner。Path4 未混入 Path2，winner/robust/tracked 未改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 仍为 `underrepresented_families / rotate`。60/40 与 70/30 已证伪，下一轮只用 40/60 做最后一次比例边界确认；若 2023 再触发护栏，则停止 v70 同形扩参。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_40_60_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6
```

### Focus 候选池

- `underrepresented_families`：40/60-v70、60/40-v78；`medium_cycle_growth`：v30 medium-cycle、v37 medium-cycle-repair。
- `risk_reconfirm_sensitivity`：v42 risk-reconfirm、正式 robust；`capacity_and_cost_stress`：v44 underrep-repair、v45 capacity-stress。

## 2026-07-30 迭代记录

### 上一轮候选与结果摘要

- 等权 `v42_risk_reconfirm` 的 2023 CAGR 为 `-3.35%`，相对当前观察位 `aggr_10_90_prom6` 的 `18.19%` 下降 `21.54pp`，Sharpe 下降 `0.52`，且 2026 CAGR `-44.99%`，判定 `reject`。
- `aggr_10_90_prom6` 的 2020/2026 CAGR 仍为 `-0.09%/-12.79%`，只能标记 `robust_observation`：进入观察位，不是强稳定 winner。window winner、robust candidate 与 tracked payload 未因新候选改变，无 evict/archive。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-29 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6
```

Scorecard：`results/research/a_share/research_iteration_scorecard_20260730.json`。

### 下一轮 focus 提示

- 最终 guard 轮换到 `underrepresented_families`。下一轮用 60/40 等权双周 v70 与弱 robust 同窗确认不同 core/explore 配比；该族若继续出现长窗回撤或 2023 断裂，不再做同形微调。第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6
```

### Focus 候选池

- `medium_cycle_growth`：`...v37_medium_cycle_repair`、`...v30_medium_cycle`。
- `risk_reconfirm_sensitivity`：total-mv `...v42_risk_reconfirm`、正式观察位 `...aggr_10_90_prom6`。
- `cost_capacity`：`...cap22_cost_guard_v37`、`...cap24_cost_guard_v42`。
- `short_window_elasticity`：`...aggr_10_90_prom6`、`...theme_fast_growth_elastic`。

## 2026-07-29 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- `...v42_risk_reconfirm` 与 `...v37_medium_cycle_repair` 在 `since_2023_01` 近零、`since_2026_01` 约 `-32%`，均判定 `reject`。
- 对照 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 在部分窗口仍居前，但 `since_2026_01` 为负，判定 `robust_observation`：进入观察位，不是强稳定 winner。
- window winner、robust candidate 与 tracked payload 未变化。

### 本轮候选 ID 与命令

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6
```

### 下一轮 focus 提示

- focus：`risk_reconfirm_sensitivity`。下一轮比较 equal-weight 风险复核变体与当前观察位。
- 第一条命令：

```bash
AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6
```

### Focus 候选池

- `risk_reconfirm_sensitivity`：`...v42_risk_reconfirm`、`...v37_medium_cycle_repair`。
- `medium_cycle_growth`：`...v37_medium_cycle_repair`、`...v38_medium_cycle_balance`。
- `cost_capacity`：`...cap22_cost_guard_v37`、`...cap24_cost_guard_v42`。
- `short_window_elasticity`：`...aggr_10_90_prom6`、`...theme_fast_growth_elastic`。

## 2026-07-29 迭代记录

### 上一轮候选与结果摘要

- 按 `medium_cycle_growth`/温和欠配修复五窗口确认 v30、v44，并与正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 同窗比较。v30/v44 的 2023 CAGR 相对 robust 分别下降 `19.16pp/20.28pp`，Sharpe 下降 `0.610/0.651`，2026 CAGR 为 `-31.78%/-32.92%`，均 `reject`；实验假设“中周期或温和等权能修复 2023”不成立。
- robust 本身 2020/2026 CAGR 已为 `-0.11%/-14.73%`，虽仍是 artifact robust，但只能标记 `robust_observation`，进入观察位，不是强稳定 winner。v30 的窗口排序未改变 robust/tracked；Path4 未混入 Path2，无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`、`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair`、`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。
- 五窗口增量命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260729.json`。

### 下一轮 focus 提示

- guard focus 为 `medium_cycle_growth`。v30 已因 2023 断裂被拒绝，下一轮只确认注册的 v37 修复边界；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`；若仍破坏 2023，停止 v30/v37 同形扩参并转 risk-reconfirm。

### Focus 候选池

- `medium_cycle_growth`：v37 medium-cycle-repair、v30 失败边界；`risk_reconfirm_sensitivity`：v42 risk-reconfirm、正式 robust；`underrepresented_families`：60/40-v70、70/30-v70；`capacity_and_cost_stress`：v44 underrep-repair、v45 capacity-stress。

## 2026-07-28 二次迭代记录（07:23 CST）

### 上一轮候选与结果摘要

- 按 `capacity_and_cost_stress` 五窗口确认 equal-weight v45/v46，并与正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 同窗比较。v45/v46 的 2020 CAGR 为 `8.41%/8.44%`，但 2023 仅 `8.53%/9.17%`、相对 robust `20.48%` 下降约 `11.95pp/11.31pp`，2026 为 `-25.82%/-22.64%`，且 2023 turnover 约 `4.76x/4.74x`；两条均 `reject`。
- robust 五窗口确认 `promote`；实验假设“压集中度和成本可守住 2023 并修复短窗”不成立。Path4 未混入 Path2，window winner/robust/tracked 未变化，无 evict/archive。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress`、`...top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`、正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728_iter2.json`。

### 下一轮 focus 提示

- 当前 focus 为 `capacity_and_cost_stress`。v45/v46 同形已证伪，下一轮回到较温和 v44；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。

### Focus 候选池

- `capacity_and_cost_stress`：v44 underrep-repair、v45 capacity-stress；`underrepresented_families`：60/40-v70、70/30-v70；`medium_cycle_growth`：v30、v37；`risk_reconfirm_sensitivity`：v42、正式 robust。

## 2026-07-28 迭代记录

### 上一轮候选与结果摘要

- 按 `underrepresented_families` 五窗口确认 v70 的 70/30、80/20 等权底座及 v78 的 70/30 等权底座，并与正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 同窗比较。三条双周候选的 2023 CAGR 仅 `1.83%/-0.30%/1.78%`，相对 robust 下降约 `18.64pp/20.77pp/18.69pp`，2026 CAGR 为 `-6.83%/-20.18%/-6.97%`，且 2023 turnover 约 `6.17x-6.69x`，全部 `reject`；欠配双周族修复中窗的假设不成立。
- 正式 robust 五窗口确认 `promote`；Path4 未混入 Path2，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn`、`core_explore_80_20_equal_weight_winner_core__...v70_underrepresented_lowturn`、`core_explore_70_30_equal_weight_winner_core__...v78_underrepresented_repair`、正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260728.json`。

### 下一轮 focus 提示

- 最终 focus 仍为 `underrepresented_families`，但 v70/v78 同形已证伪。下一轮第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`，只验证不同 core/explore 配比，不再下调 risk/exit。

### Focus 候选池

- `underrepresented_families`：60/40-v70、70/30-v70；`medium_cycle_growth`：v30、v37；`risk_reconfirm_sensitivity`：v42、正式 robust；`capacity_and_cost_stress`：v45、v46。

## 2026-07-27 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 按 `risk_reconfirm_sensitivity` 五窗口确认 v73 双底座，并与正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 同窗比较。total-mv v73 的 2020 CAGR 提高 `5.31pp`，但 2023 CAGR 仅 `5.92%`、相对 robust 下降 `14.55pp`，2026 CAGR `-23.09%`；equal-weight v73 的 2023/2026 CAGR 为 `-4.39%/-28.35%`。两条均触发中窗护栏并 `reject`；正式 robust 同端点确认 `promote`。Path4 未混入 Path2，winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity`、正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727_iter2.json`。

### 下一轮 focus 提示

- 当前 focus 为 `risk_reconfirm_sensitivity`，v73 双底座已证伪，下一轮回到已注册 v42 风险边界，要求 2023 不再破坏稳定性；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。

### Focus 候选池

- `risk_reconfirm_sensitivity`：v42、正式 robust；`medium_cycle_growth`：v30、v37；`underrepresented_families`：双周 v70、v78；`capacity_and_cost_stress`：v45、v46。

## 2026-07-27 迭代记录

### 上一轮候选与结果摘要

- 按 `medium_cycle_growth` 五窗口确认 v30/v37，并与正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 同窗比较。两条候选的 2020 CAGR 均约 `12.15%`，但 2023 CAGR 仅 `1.29%/1.26%`，相对 robust 下降 `19.18pp/19.21pp`，2026 CAGR 均为 `-22.60%`，假设“中周期 liqmom 可修复 2020 且守住 2023”不成立，均 `reject`；incumbent 确认 `promote`。Path4 未混入 Path2，winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair`、`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。
- 五窗口确认命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260727.json`。

### 下一轮 focus 提示

- 最终 focus 轮换为 `risk_reconfirm_sensitivity`。v30/v37 已连续证伪，下一轮改测已注册 v73 双底座的风险/再确认边界；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。

### Focus 候选池

- `medium_cycle_growth`：双周 v70 lowturn、双周 v78 repair；`underrepresented_families`：v70、v78；`capacity_and_cost_stress`：v45、v46；`risk_reconfirm_sensitivity`：v74、正式 robust `aggr_10_90_prom6`。

## 2026-07-26 二次迭代记录（07:19 CST）

### 上一轮候选与结果摘要

- 按 `capacity_and_cost_stress` 五窗口确认 equal-weight v45/v46，并与正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 同窗比较。v45/v46 的 2020 CAGR 提高约 `8.2pp`，但 2023 CAGR 下降约 `11.9pp/11.3pp`、2026 CAGR 为 `-25.82%/-22.64%`，触发 CAGR/MaxDD/Sharpe 护栏，均 `reject`；robust 同端点确认 `promote`。实验假设“容量成本改善且守住中窗”未获支持，Path4 未混入 Path2，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress`、`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`、`core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 轮换为 `medium_cycle_growth`。v45/v46 容量同形停止，下一轮转 v30/v37 中周期增长修复，并继续与正式 robust 比较。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。

### Focus 候选池

- `capacity_and_cost_stress`：v45、v46（本轮已 reject，停止同形）；`underrepresented_families`：双周 v70、v78；`medium_cycle_growth`：v30、v37；`risk_reconfirm_sensitivity`：v74、正式 robust。

## 2026-07-26 迭代记录

### 上一轮候选与结果摘要

- 按 `underrepresented_families` 五窗口确认 equal-weight v43/v44，并与正式 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 同窗比较。v43/v44 的 2023 CAGR 为 `-1.09%/-0.76%`、2026 CAGR 为 `-37.65%/-29.02%`，中窗 CAGR/Sharpe 明显破坏稳定性，均判定 `reject`。Path4 候选未混入 Path2，window winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 候选：`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality`、`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260726.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `capacity_and_cost_stress`。v43/v44 同形已失败，下一轮改测 equal-weight v45/v46 的容量成本边界，并以正式 robust 为同窗对照。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。

### Focus 候选池

- `medium_cycle_growth`：v30 medium-cycle、v37 growth-repair；`risk_reconfirm_sensitivity`：v74 capacity-cost、正式 robust `aggr_10_90_prom6`。
- `underrepresented_families`：双周 v70 lowturn、双周 v78 repair；`capacity_and_cost_stress`：equal-weight v45、v46 capacity-cost。

## 2026-07-25 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 按 `risk_reconfirm_sensitivity` 五窗口确认 v66、v69 与 current robust `aggr_10_90_prom6`。v66/v69 的 2023 CAGR 相对 robust 下降 `14.68pp/22.24pp`，Sharpe 下降 `0.41/0.74`，且 2026 CAGR 为 `-19.76%/-22.70%`，均 `reject`；incumbent 五窗确认 `promote`。Path4 候选未混入本路径，winner/robust/tracked 未改变，无 evict。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top11_risk28_mom_exit48_reconfirm94_caution60_cap18_cost_guard_v69_medium_cycle_growth_repair,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。完整 scorecard：`results/research/a_share/research_iteration_scorecard_20260725_iter2.json`。

### 下一轮 focus 提示

- 最终 guard 已轮换到 `underrepresented_families`；v66-v69 同形连续失败后停止扩参，下一轮回到等权弹性质量/容量修复线。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair`。

### Focus 候选池

- `risk_reconfirm_sensitivity`：v74 capacity-cost、current `aggr_10_90_prom6`；`medium_cycle_growth`：v30、v37（仅作失败边界）。
- `capacity_and_cost_stress`：v74 total-mv、v74 equal-weight；`underrepresented_families`：v43 underrep-quality、v44 underrep-repair。

## 2026-07-25 迭代记录

### 上一轮候选与结果摘要

- 五窗口确认 v66/v67/v68/v69 四条中周期 growth-elastic 参数。v66 的 2023 CAGR 比 robust 低 `14.68pp`，v67-v69 低约 `22.17pp-22.28pp`；四条 2026 CAGR 均为 `-19.76%` 至 `-23.09%`，换手最高约 `9.62x`。中周期收益修复假设未成立，四条均 `reject`；Path2 window winner/robust/tracked 未改变，未混入 Path4，无 evict。

### 本轮候选 ID 与命令

- 候选：`...v66_risk_reconfirm_sensitivity`、`...v67_medium_cycle_growth_repair`、`...v68_medium_cycle_growth_repair`、`...v69_medium_cycle_growth_repair`。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v67_medium_cycle_growth_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm94_caution58_cap16_cost_guard_v68_medium_cycle_growth_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top11_risk28_mom_exit48_reconfirm94_caution60_cap18_cost_guard_v69_medium_cycle_growth_repair`；v68 另补齐到 `2026-07-24`。

- stale 修复：对上述全部候选把同一 `--only-base-ids` 命令的 `--end-date` 改为 `2026-07-24` 后完成五窗增量复跑；最终 scorecard、strategy JSON 与 live valuation 均采用该终点。

### 下一轮 focus 提示

- 最终 guard 为 `risk_reconfirm_sensitivity`：停止 v66-v69 同形扩参，用 v66 与 incumbent 做风险边界复核；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity,core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`。

### Focus 候选池

- `medium_cycle_growth`：v67、v68（失败边界）；`risk_reconfirm_sensitivity`：v66、v69。
- `capacity_and_cost_stress`：v74 total-mv、v74 equal-weight；`underrepresented_families`：v43 underrep-quality、v44 underrep-repair。

## 2026-07-24 二次迭代记录（07:25 CST）

### 上一轮候选与结果摘要

- 上一轮 v43/v44/v46 容量成本压力线全部 `reject`；本轮确认 90/10 中周期 v30/v37/v42，并与 Path2 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 同窗比较，未混入 Path4。
- v30/v37/v42 的 2023 CAGR 仅 `1.70%/1.67%/1.43%`，相对 robust 下降约 `19.1pp-19.4pp`，Sharpe 下降约 `0.58-0.59`，2026 CAGR 均约 `-19.7%`；三条均 `reject`，实验假设不成立。window winner/robust/tracked 未改写，无 evict。

### 本轮候选 ID 与命令

- 候选：`...v30_medium_cycle`、`...v37_medium_cycle_repair`、`...v42_risk_reconfirm`（完整 ID 见下列命令与 scorecard）。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm`。

### 下一轮 focus 提示

- 最终 guard 轮换到 `medium_cycle_growth`；停止继续增加 v30/v37/v42 同形参数，下一轮先以 v30/v37 作失败边界复核，再从注册池设计不同底座的中周期原型。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair`。

### Focus 候选池

- `capacity_and_cost_stress`：v74 total_mv、v74 equal_weight。
- `medium_cycle_growth`：v30 medium-cycle、v37 medium-cycle-repair（失败边界对照；新原型必须更换底座或信号形态）。
- `risk_reconfirm_sensitivity`：v42 risk-reconfirm、v74 capacity-cost。
- `underrepresented_families`：v43 underrep-quality、v44 underrep-repair。

## 2026-07-24 收尾记录

### 上一轮候选与结果摘要

- `capacity_and_cost_stress` 五窗口确认 v43/v44/v46。三者 2023 CAGR 分别 `-0.62%/-0.22%/9.94%`，2026 CAGR `-34.66%/-25.79%/-19.24%`，且换手约 `8.4x-8.9x`；相对 robust `...aggr_10_90_prom6` 明显破坏 2023/2026 稳定性，全部 `reject`。
- Path2 winner/robust/tracked 未变，Path4 emergent-theme 未混入本路径，也未产生 active evict。

### 本轮候选 ID 与命令

- 候选：`...v43_underrep_quality`、`...v44_underrep_repair`、`...v46_capacity_cost`（完整 ID 见 scorecard）。
- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`。

### 下一轮 focus 提示

- 停止 v43/v44/v46 同形扩参，回到已注册的 `capacity_and_cost_stress` 对照，先确认是否仍应归档；首条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit44_reconfirm99_caution54_cap16_cost_guard_v74_capacity_cost_stress,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit44_reconfirm99_caution54_cap16_cost_guard_v74_capacity_cost_stress`。

### Focus 候选池

- `capacity_and_cost_stress`：v74 total_mv、v74 equal_weight 两个已注册对照；若仍弱则归档，不继续同形扩参。
- `underrepresented_families`：`...v43_underrep_quality`、`...v44_underrep_repair`（仅作历史对照，不再同形扩参）。

## 2026-07-23 收尾记录

### 上一轮候选与结果摘要

- 上一轮 90/10 中周期同形线全部归档；本轮按 `underrepresented_families` 确认 v70/v78 双周 70/30 与 v38/v41 等权弹性，共 4 个 base ids。v70/v78 的 2023 CAGR 仅约 `2.1%`、换手 `6.7x-19.3x`；v38/v41 的 2026 CAGR `-45.15%/-29.69%`，四条均 `reject`。
- 当前 Path2 winner/robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6`，本轮没有 window winner、robust 或 tracked 改写，也没有把 Path4 emergent-theme 混入 Path2。

### 本轮候选 ID 与命令

- 实跑命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk26_exit46_cap24_cost_guard_v41_underrep_quality`。

### 下一轮 focus 提示

- 欠配族需要停止高换手 70/30 小修，转向 v43/v44 的质量/容量约束；第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-22 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair`。

### Focus 候选池

- `underrepresented_families`：v43、v44；`medium_cycle_growth`：v30 历史强线、v41 underrep-quality；`risk_reconfirm_sensitivity`：v69、v77；`capacity_and_cost_stress`：v44、v46。`scripts/path2_candidate_pass.py` 已完成，scorecard 见 `results/research/a_share/research_iteration_scorecard_20260723.json`。

## 2026-07-22 收尾记录

- 上一轮候选与结果摘要：上一轮 v78/v81 只留弱观察；本轮按 `medium_cycle_growth` 同端点确认 v79 双底座、v81 total_mv 与 v74 total_mv，共 4 个 base ids。四条均在 2023 CAGR/Sharpe 上显著落后 robust，且 2026 CAGR 约 `-12.5%` 至 `-14.9%`。
- 本轮候选 ID 与命令：`core_explore_90_10_{total_mv,equal_weight}_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit44_reconfirm99_caution54_cap16_cost_guard_v74_capacity_cost_stress`；完整命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit44_reconfirm99_caution54_cap16_cost_guard_v74_capacity_cost_stress`。
- Scorecard 与判定：v79 total/equal、v81 total、v74 total 的 2023 CAGR 相对 robust 低约 `15.63pp-25.35pp`，Sharpe 低 `0.44-0.79`；四条均判 `archive` 并加入 `PATH2_ARCHIVED_STRATEGY_BASE_IDS`。Path2 window winner/robust/tracked 未变。
- 下一轮 focus 提示：不再围绕 90/10 中周期同形扩参，转向 underrepresented 双周 70/30 低换手确认。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn`。
- Focus 候选池：`medium_cycle_growth` -> `v79_medium_cycle_repair` 历史对照、`v70_underrepresented_lowturn`；`underrepresented_families` -> `v70` 70/30、`v78` 70/30；`risk_reconfirm_sensitivity` -> `v77_reconfirm100_caution52`、`v69_risk_reconfirm`；`capacity_cost_stress` -> `v73_capacity_cost`、`v70_underrepresented_lowturn`。归档项只保留历史 snapshot，不再进入 active。

## 2026-07-21 收尾记录

- 上一轮候选与结果摘要：上一轮 v82/v83 全部淘汰；本轮按 `underrepresented_families` 与 `medium_cycle_growth` 确认 v78 双周流动性动量两底座、v81 中周期低换手两底座，共 4 个 base ids，继续保持 `growth_elastic` 独立池。
- 本轮候选 ID 与命令：执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm`，随后运行 `scripts/path2_candidate_pass.py` 与 `scripts/update_weighted_winners.py`。
- Scorecard 与判定：v78 70/30 的 2020/2023 CAGR 仅 `1.86%/1.57%`、换手约 `8.07x/6.68x`，虽进入弱路径 robust，仍判定 `robust_observation`：进入观察位，不是强稳定 winner；v78 80/20 因 2023/2026 为负判 `reject`。v81 total_mv 的 2017/2020 CAGR `10.19%/10.42%` 并进入 2017 窗口排序，但 2023/2026 仅 `4.34%/-28.88%`，判 `keep_watch`；equal_weight 判 `reject`。无正式 promote。
- 下一轮 focus 提示：最终 guard 为 `medium_cycle_growth`；先复核 v81 total_mv，只有 2023 至少恢复 3pp 且 2026 转正才保留。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-20 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm`。
- Focus 候选池：`medium_cycle_growth` -> `v81_midcycle_lowturn_confirm` total_mv、`v79_medium_cycle_repair` total_mv；`underrepresented_families` -> `v78_underrepresented_repair` 70/30、`v70_underrepresented_lowturn` 70/30；`risk_reconfirm_sensitivity` -> `v77_reconfirm100_caution52`、`v84_risk18_exit46_reconfirm99`；`capacity_cost_stress` -> `v74_capacity_cost_stress`、`v85_cap14_cost_guard_retest`。
- evict/归档：v78 80/20 equal_weight 与 v81 90/10 equal_weight 加入 `PATH2_ARCHIVED_STRATEGY_BASE_IDS`；v78 70/30 与 v81 total_mv 留 watch。完整 scorecard 见 `research_iteration_scorecard_20260721.json`。

## 2026-07-20 收尾记录

- 上一轮候选与结果摘要：上一轮 `v81_midcycle_lowturn_confirm` 仅为弱观察；本轮继续独立 `growth_elastic` 池，新增 v82/v83 在 90/10 总市值与等权两个底座上的四个 base ids，专门挑战 2023 中周期稳定性。
- 本轮候选 ID 与命令：执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit48_reconfirm98_caution56_cap18_cost_guard_v82_2023_quality_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit48_reconfirm98_caution56_cap18_cost_guard_v82_2023_quality_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk28_mom_exit46_reconfirm96_caution60_cap20_cost_guard_v83_midcycle_breadth_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk28_mom_exit46_reconfirm96_caution60_cap20_cost_guard_v83_midcycle_breadth_repair`，随后运行 `scripts/path2_candidate_pass.py`。
- Scorecard 与判定：四条候选相对当前 robust `core_explore_80_20_total_mv_winner_core__aggr_10_90_prom6` 的 2023 CAGR 下降 `15.68pp-24.87pp`，Sharpe 下降 `0.441-0.788`；2026 CAGR 均约 `-25%`，部分换手达到 `6.5x-7.1x`。实验假设未获支持，四条全部 `reject` 并加入 `PATH2_ARCHIVED_STRATEGY_BASE_IDS`；无 window winner/robust/tracked 变化。
- 下一轮 focus 提示：最终 guard 为 `risk_reconfirm_sensitivity`；停止 v82/v83 同形扩参，转向更窄风险暴露的 2023 修复。第一条命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit46_reconfirm99_caution54_cap14_cost_guard_v84_2023_risk_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit46_reconfirm99_caution54_cap14_cost_guard_v84_2023_risk_repair`；未注册原因：本轮需先归档失败项并完成 artifact 同步。
- Focus 候选池：`medium_cycle_growth` -> `v84_2023_risk_repair` 双底座、`v85_midcycle_quality_lowturn` 双底座；`underrepresented_families` -> `v78_underrepresented_repair` 70/30、`v83_underrepresented_quality_lowturn` 80/20；`risk_reconfirm_sensitivity` -> `v77_reconfirm100_caution52`、`v84_risk18_exit46_reconfirm99`；`capacity_cost_stress` -> `v74_capacity_cost_stress`、`v85_cap14_cost_guard_retest`。
- evict/归档：v82/v83 四个 base ids 均从 active 竞争口径移除，历史 CSV/策略定义保留；完整 scorecard 见 `research_iteration_scorecard_20260720.json`。

## 2026-07-19 收尾记录

- 上一轮候选与结果摘要：上一轮 `v79_medium_cycle_repair` 只进入弱观察；本轮沿 `medium_cycle_growth` 五窗口实跑 `v80_2023_repair`、`v81_midcycle_lowturn_confirm` 的 90/10 总市值与等权双底座，共 4 个 base ids，继续保持 `growth_elastic` 独立池。
- 本轮候选 ID 与命令：`core_explore_90_10_{total_mv,equal_weight}_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk26_mom_exit48_reconfirm96_caution58_cap20_cost_guard_v80_2023_repair` 与 `core_explore_90_10_{total_mv,equal_weight}_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <上述 4 个完整 IDs>`，随后运行 `scripts/path2_candidate_pass.py` 与 `scripts/update_weighted_winners.py`。
- Scorecard 与判定：v80 总市值在 2023 CAGR 为 `-2.40%`、等权在 2020/2023 为 `-2.45%/-1.67%`，两者均 `archive`；v81 等权在 2023 CAGR `-2.88%` 且 MaxDD `-38.37%`，判定 `reject`。v81 总市值在 2020 CAGR/MaxDD/Sharpe 为 `10.48%/-16.00%/0.628`，相对 v79 有改善且未命中二次硬阈值，但 2026 CAGR `-24.24%`，artifact 将其推到观察位，判定 `robust_observation`：进入观察位，不是强稳定 winner；正式 2020/2023 winner 未改变。
- 下一轮 focus 提示：最终 guard 继续 `medium_cycle_growth`。第一条可执行命令：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit50_reconfirm97_caution54_cap16_cost_guard_v81_midcycle_lowturn_confirm`；观察条件是 2026 转正且 2023 不低于当前 robust 超过 3pp。
- Focus 候选池：`medium_cycle_growth` -> `v81_midcycle_lowturn_confirm` 总市值、`v82_2023_quality_repair` 总市值；`underrepresented_families` -> `v78_underrepresented_repair` 70/30、`v83_underrepresented_quality_lowturn` 80/20；`risk_reconfirm_sensitivity` -> `v77_reconfirm100_caution52`、`v84_risk18_exit46_reconfirm99`；`capacity_cost_stress` -> `v74_capacity_cost_stress`、`v85_cap14_cost_guard_retest`。
- evict/归档：v80 两个 base ids 已加入 `PATH2_ARCHIVED_STRATEGY_BASE_IDS`；`update_weighted_winners.py` 同步应用 archive，并显式排除 `emergent_theme` 泄漏，不再把独立 Path4 历史结果算入 Path2。

## 2026-07-09 收尾记录

- 上一轮候选与结果摘要：上一轮 v78 underrepresented 修复只进入弱观察；本轮按 `medium_cycle_growth` 新增并五窗口确认 `v79_medium_cycle_repair` 双底座，仍保持独立 `growth_elastic` 池，未引入 Path4 `emergent_theme`，也未把 Path3 `_weekly` 结论并入 Path2。
- 本轮候选 ID 与命令：实跑 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,<path4_prom24_three_ids>`。
- Scorecard 与判定：v79 total_mv 五窗口 CAGR `7.00% / 5.95% / 12.32% / 38.68% / 10.26%`、MaxDD 最差 `-21.18%`、turnover 最高 `10.21x`；`update_weighted_winners.py` 将其推到 Path2 artifact 观察位，但相对历史 scan robust `caution75_cap95` 的 2020/2023 CAGR 大幅降低，判定 `robust_observation`，进入观察位，不是强稳定 winner。v79 equal_weight 五窗口 CAGR `4.03% / 2.76% / 2.94% / 14.56% / 12.78%`、MaxDD 最差 `-26.42%`、turnover 最高 `10.85x`，判定 `reject`。
- 下一轮 focus 提示：下一轮继续 `medium_cycle_growth`，但不复跑 v79 等权。第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk26_mom_exit48_reconfirm96_caution58_cap20_cost_guard_v80_2023_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk26_mom_exit48_reconfirm96_caution58_cap20_cost_guard_v80_2023_repair`；若未注册，先加入 Path2 scan family/list，并归档一条连续失败的旧 medium-cycle 或 underrepresented 负样本。
- Focus 候选池：`medium_cycle_growth` -> `v80_2023_repair` 双底座、`v81_midcycle_lowturn_confirm` 双底座；`underrepresented_families` -> `v81_underrepresented_lowturn_confirm` 双底座、`v78_underrepresented_repair` 负样本；`risk_reconfirm_sensitivity` -> `v77_reconfirm100_caution52` 双底座、`v82_risk18_exit38_reconfirm` 双底座；`capacity_cost_stress` -> `v83_cap18_cost_guard_retest` 双底座、`v74_capacity_cost_stress` 负样本。
- evict/归档：本轮无代码 archive；v79 equal_weight 标记 `reject`，v79 total_mv 仅保留 artifact 观察，不写成 promote。

## 2026-07-08 收尾记录

- 上一轮候选与结果摘要：上一轮 Path2 只留下 `underrepresented_families` 双周量价弹性修复；本轮保持独立 `growth_elastic` 池，未引入 Path4 `emergent_theme`，也未把 Path3 `_weekly` 候选并入 Path2。
- 本轮候选 ID 与命令：实跑 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair` 与 `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_risk18>,<path1_risk16>,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,<path4_prom23_three_ids>`。
- Scorecard 与判定：相对 `v46_capacity_cost`，70/30 v78 的 2020/2023 CAGR `6.82% / 4.16%`、Sharpe `0.425 / 0.329`、MaxDD `-24.32% / -18.43%`、turnover `8.04x / 6.69x`，2020/2023 收益显著退化且换手过高；artifact 把它写入 Path2 observation，但本质判定 `robust_observation`，进入观察位，不是强稳定 winner。80/20 v78 的 2020/2023 CAGR `5.04% / 0.46%`、MaxDD `-24.94% / -20.14%`、turnover `8.06x / 6.19x`，判定 `reject`，停止同形继续压 risk/exit/cap。
- 下一轮 focus 提示：最终 guard 给 `medium_cycle_growth`。第一条命令回到中周期修复而不是继续 v78 同形：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v79_medium_cycle_repair`；若未注册，先加入 Path2 scan family/list，并归档一条连续失败的 underrepresented 旧样本。
- Focus 候选池：`medium_cycle_growth` -> `v79_medium_cycle_repair` 双底座、`v80_2023_repair` 双底座；`underrepresented_families` -> `v78_underrepresented_repair` 负样本、`v81_underrepresented_lowturn_confirm` 双底座；`risk_reconfirm_sensitivity` -> `v77_reconfirm100_caution52` 双底座、`v82_risk18_exit38_reconfirm` 双底座；`capacity_cost_stress` -> `v74_capacity_cost_stress` 负样本、`v83_cap18_cost_guard_retest` 双底座。
- evict/归档：本轮无代码 archive，但 v78 80/20 标记 `reject`，70/30 只保留 artifact 观察；`scripts/path2_candidate_pass.py` 与 `scripts/update_weighted_winners.py` 已同步，不能把该 observation 写成 promote。

## 2026-07-08 迭代状态

- 上一轮候选/结果摘要：上一轮 v74 capacity-cost stress 双底座均因 2020/2023 收益不足和短窗换手高判定 `reject`；本轮 Path2 独立 `growth_elastic` 池完成 guard 巡检，未引入 Path4 `emergent_theme`，也未把 Path3 `_weekly` 结论并入 Path2。
- 本轮候选 ID 与命令：本轮未新增 Path2 `--only-base-ids` 回测，原因是 A股新增确认预算优先给 Path4 `theme_risk_control` 与 Path5 event entry；下一轮第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v75_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v75_medium_cycle_repair`。
- Scorecard 与判定：本轮 Path2 无新增实跑 scorecard；`scripts/update_weighted_winners.py` 后 Path2 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`，判定 `keep_watch`。v75 假设是比 v74 回升 risk/exit/reconfirm，优先修复 2020/2023 CAGR，若 2023 仍低于 robust 超过 3pp 则直接 `reject`。
- evict/归档：本轮无 Path2 evict；v74 作为 capacity-cost stress 负样本保留，下一轮不继续同形降 risk/cap。
- 下一轮 focus：最终 guard 给 `underrepresented_families`。第一条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-07 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v78_underrepresented_repair`；若未注册，先加入 Path2 scan family/list 并归档一条旧 underrepresented 负样本。
- Focus 候选池：`underrepresented_families` -> `v78_underrepresented_repair` 双底座、`v79_underrepresented_lowturn_confirm` 双底座；`medium_cycle_growth` -> `v75_medium_cycle_repair` 双底座、`v76_2023_repair` 双底座；`risk_reconfirm_sensitivity` -> `v77_reconfirm100_caution52` 双底座、`v73_risk_reconfirm_sensitivity` 双底座；`capacity_cost_stress` -> v74 负样本、`v80_cap18_cost_guard_retest` 双底座；`momentum_equal_weight_elastic` -> `v46_capacity_cost` 周边、`v81_lowturn_confirm` 双底座。

## 2026-07-07 迭代状态

- 上一轮候选/结果摘要：上一轮 v72 中周期修复失败后，开局 dirty code 中已注册 v74 capacity-cost stress 双底座；本轮按独立 `growth_elastic` 池五窗口确认，不引入 Path4 `emergent_theme`，也不把 Path3 `_weekly` 当作 Path2。
- 本轮候选 ID 与命令：新增/确认 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit44_reconfirm99_caution54_cap16_cost_guard_v74_capacity_cost_stress`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit44_reconfirm99_caution54_cap16_cost_guard_v74_capacity_cost_stress`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path1_share24>,<two_path2_v74>,<one_path3_yield_v2>,<three_path4_prom24_signal30>`。
- Scorecard 与判定：v74 total_mv CAGR `7.35% / 6.32% / 12.23% / 38.48% / 10.95%`、MaxDD 最差 `-20.31%`、turnover 最高 `10.26x`；v74 equal_weight CAGR `4.63% / 3.25% / 4.35% / 17.73% / 19.36%`、MaxDD 最差 `-24.18%`、turnover 最高 `10.82x`。相对当前 Path2 robust `v46_capacity_cost`，total_mv 在 2020/2023 CAGR 分别低 `2.78pp / 4.97pp`，equal_weight 更弱；短窗换手过高，判定两条均 `reject`。`path2_candidate_pass.py` 后候选宇宙 `809`，weighted robust 仍为 `v46_capacity_cost`。
- evict/归档：本轮未新增 Path2 evict；v74 作为 capacity-cost stress 负样本保留，下一轮不继续同形降 risk/cap。
- 下一轮 focus：第一条命令建议转回中周期收益修复而非继续 capacity stress：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v75_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v75_medium_cycle_repair`；若未注册，先加入 Path2 scan family/list 并优先归档旧 underrepresented 负样本。
- Focus 候选池：`medium_cycle_growth` -> `v75_medium_cycle_repair` 双底座、`v76_2023_repair` 双底座；`risk_reconfirm_sensitivity` -> `v73_risk_reconfirm_sensitivity` 双底座、`v77_reconfirm100_caution52` 双底座；`capacity_cost_stress` -> 仅保留 v74 负样本，不再优先新增。

## 2026-07-06 迭代状态

- 上一轮候选/结果摘要：上一轮留下 v72 中周期增长修复双底座；本轮在独立 `growth_elastic` 池确认 v72，没有引入 Path4 `emergent_theme`，也没有把 Path3 `_weekly` 当作 Path2 结论。
- 本轮候选 ID 与命令：新增 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top16_risk28_mom_exit48_reconfirm94_caution58_cap20_cost_guard_v72_medium_cycle_growth_repair`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top16_risk28_mom_exit48_reconfirm94_caution58_cap20_cost_guard_v72_medium_cycle_growth_repair`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v72>,<path1>,<path3>,<three_path4>`。
- 五窗口结果：`90/10 total_mv` CAGR `8.10% / 7.46% / 2.78% / 38.79% / 9.26%`，最大回撤最差 `-21.07%`；`90/10 equal_weight` CAGR `3.34% / 1.75% / 5.42% / 18.03% / 24.18%`，最大回撤最差 `-26.66%`。
- 结论：v72 扩大 top16/risk28 后仍未修复 `since_2020_01`/`since_2023_01` 中周期收益，短窗也不及既有 robust；`scripts/path2_candidate_pass.py` 后候选宇宙维持 `808`，weighted robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`。
- evict/归档：归档旧 `v64_underrepresented_lowturn` 双底座：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn` 与 `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn`；原因是 2020/2023 弱、换手高，且被后续 v70-v72 medium-cycle 复核覆盖。
- 下一轮 focus：最终 guard 给 `risk_reconfirm_sensitivity`，下一候选应停止 v72 同形中周期扩张，改测更低风险/更高再确认的敏感性对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity`；若未注册，先加入 Path2 scan family/list 并继续控制 active cap。

## 2026-07-05 迭代状态

- 上一轮候选/结果摘要：上一轮留下 v71 中周期增长修复候选；本轮在独立 `growth_elastic` 池确认 v71 双底座，没有把 Path4 `emergent_theme` 或 Path3 `_weekly` 结论并入 Path2。
- 本轮候选 ID 与命令：新增 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk26_mom_exit46_reconfirm96_caution56_cap18_cost_guard_v71_medium_cycle_growth_repair`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk26_mom_exit46_reconfirm96_caution56_cap18_cost_guard_v71_medium_cycle_growth_repair`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v71>,<path1>,<path3>,<three_path4>`。
- 五窗口结果：`90/10 total_mv` CAGR `7.80% / 7.07% / 3.07% / 38.85% / 10.62%`，最大回撤最差 `-21.06%`，换手最高 `10.21x`；`90/10 equal_weight` CAGR `3.34% / 1.77% / 6.35% / 19.40% / 26.19%`，最大回撤最差 `-26.41%`。
- 结论：v71 仍不能修复 `since_2020_01`/`since_2023_01` 中周期收益，且短窗弹性不及既有 robust；`scripts/path2_candidate_pass.py` 后候选宇宙 `808`，weighted robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`，`meanCAGR=20.70% / minCAGR=9.16%`。
- evict/归档：本轮无 Path2 evict；v71 作为 medium-cycle 扩 risk/top14 的负样本，后续若 cap 紧张优先淘汰更早的 v63/v64 低换手短窗负样本。
- 下一轮 focus：若最终 guard 继续给 `medium_cycle_growth`，下一候选应减少短窗换手并提高 2020/2023 稳定性，首条命令建议 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top16_risk28_mom_exit48_reconfirm94_caution58_cap20_cost_guard_v72_medium_cycle_growth_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top16_risk28_mom_exit48_reconfirm94_caution58_cap20_cost_guard_v72_medium_cycle_growth_repair`；若未注册，先加入 Path2 scan family/list。

## 2026-07-04 07:03 CST 状态

- 上一轮候选/结果摘要：上一轮 v67 只改善 Path2 2017 口径，2020/2023 仍弱；本轮在独立 `growth_elastic` 池新增 v70 underrepresented 低换手双周线，没有引入 Path4 `emergent_theme`，也没有把 Path3 `_weekly` 当作 Path2 结论。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk16_exit36_cap10_cost_guard_v70_underrepresented_lowturn`；命令并入 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v70>,<path1>,<path3>,<three_path4>`。
- 五窗口结果：`80/20 equal_weight` CAGR `6.49% / 6.07% / 0.98% / 46.24% / 57.33%`，最大回撤最差 `-28.14%`，换手最高 `20.03x`；`70/30 equal_weight` CAGR `7.81% / 7.88% / 5.34% / 56.90% / 102.27%`，最大回撤最差 `-27.75%`，换手最高 `19.26x`。
- 结论：v70 仍是短窗弹性样本，不能修复 `since_2020_01`/`since_2023_01` 中周期收益；`scripts/path2_candidate_pass.py` universe 更新到 `806`，weighted robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`，`meanCAGR=20.70% / minCAGR=9.16%`。
- evict/归档：本轮无 Path2 evict；v70 只是补 underrepresented 低换手族代表，后续若 cap 紧张，优先淘汰更早的 v63/v64 低换手负样本。
- 下一轮 focus：最终 guard 仍给 `medium_cycle_growth`。下一轮第一候选应回到中周期增长修复，而不是继续压 cap；候选 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk26_mom_exit46_reconfirm96_caution56_cap18_cost_guard_v71_medium_cycle_growth_repair` 与 equal_weight 对照，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v71_medium_cycle_growth_repair_ids>`；若未注册，先加入 Path2 scan family/list。

## 2026-07-01 20:58 CST 状态

- 上一轮候选/结果摘要：上一轮 v66 仍未真正修复 2020/2023 中周期收益；本轮按 `medium_cycle_growth` 在独立 `growth_elastic` 池确认 v67 双底座，没有引入 Path4 `emergent_theme`，也没有把 Path3 `_weekly` 结论并入 Path2。
- 本轮候选 ID 与命令：新增并五窗口确认 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v67_medium_cycle_growth_repair`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v67_medium_cycle_growth_repair`；命令并入本轮 A股受限回测 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v67>,<path1>,<path3>,<three_path4>`。
- 五窗口结果：`90/10 total_mv` CAGR `8.82% / 8.57% / 5.76% / 47.72% / 30.88%`，最大回撤最差 `-21.20%`，换手最高 `10.16x`；`90/10 equal_weight` CAGR `4.42% / 3.93% / 9.79% / 28.28% / 53.32%`，最大回撤最差 `-26.86%`。
- 结论：v67 总市值版切成 Path2 2017-window winner 与 robust candidate，但仍未修复 2020/2023，equal_weight 只在 2026 弹性较强；`scripts/path2_candidate_pass.py` universe 为 `801`，Path2 2020/2023/2025 window winner 仍由既有候选保持。
- evict/归档：本轮未新增 Path2 archive；v67 只是接替 v66 的 active 研究槽，后续若 2020/2023 继续弱，应淘汰 v66 或更早 v65/v64 的非 winner 线。
- 下一轮 focus：继续映射 `medium_cycle_growth` 到中周期收益修复，而不是只降风险；下一候选 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution54_cap16_cost_guard_v68_medium_cycle_2023_repair` 与 equal_weight 对照，首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v68_medium_cycle_2023_repair_ids>`；若未注册，先加入 Path2 scan family/list 并按 cap 归档一条旧弱线。

## 2026-07-01 05:26 CST 状态

- 上一轮候选/结果摘要：上一轮 v65 中周期增长修复仍只保留短窗弹性；本轮按 `risk_reconfirm_sensitivity` 在独立 `growth_elastic` 池确认 v66 双底座，没有引入 Path4 `emergent_theme`，也没有把 Path3 `_weekly` 当作 Path2 结论。
- 本轮候选 ID 与命令：新增并五窗口确认 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v66_ids>,<one_path3_id>`。
- 五窗口结果：`90/10 total_mv` CAGR `6.73% / 6.05% / 16.39% / 51.63% / 57.21%`，最大回撤最差 `-22.11%`；`90/10 equal_weight` CAGR `4.61% / 3.87% / 9.12% / 30.76% / 70.67%`，最大回撤最差 `-23.85%`。
- 结论：v66 总市值版因 candidate universe 口径成为 Path2 2017/2020/2023 window winner 与 robust payload，但绝对 2020/2023 收益仍低、2025/2026 换手压力高，不能视为高弹性目标达成。`scripts/path2_candidate_pass.py` universe 为 `799`，raw 四窗口赢家与 robust 仍由既有高弹性族主导。
- evict/归档：将 v65 双底座加入 `PATH2_ARCHIVED_STRATEGY_BASE_IDS`；evict 原因是 v65 2020/2023 不达标且被本轮更低风险/更高再确认 v66 覆盖。
- 下一轮 focus：最终 guard 给出 `medium_cycle_growth`。下一轮第一候选应回到中周期收益修复，而不是继续单纯降风险；首条命令草案为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v67_medium_cycle_growth_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v67_medium_cycle_growth_repair`；若未注册，先加入 Path2 scan family/list。

## 2026-06-30 17:26 CST 状态

- 上一轮候选/结果摘要：上一轮 v64 underrepresented 双周低换手仍只保留短窗弹性；本轮按 `medium_cycle_growth` 在独立 `growth_elastic` 池确认 v65 双底座，没有引入 Path4 `emergent_theme` 或 Path3 `_weekly` 结论。
- 本轮候选 ID 与命令：新增并五窗口确认 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm98_caution56_cap16_cost_guard_v65_medium_cycle_growth_repair`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm98_caution56_cap16_cost_guard_v65_medium_cycle_growth_repair`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v65_ids>,<one_path3_id>,<three_path4_ids>`。
- 五窗口结果：`90/10 total_mv` CAGR `6.71% / 6.10% / 16.63% / 52.97% / 52.50%`，最大回撤最差 `-22.70%`，年均换手最高 `10.19x`；`90/10 equal_weight` CAGR `4.21% / 3.52% / 9.64% / 32.98% / 81.25%`，最大回撤最差 `-25.65%`，年均换手最高 `10.78x`。
- 结论：v65 仅在 2025/2026 保留弹性，2020/2023 不达 Path2 目标线且短窗换手高；`scripts/path2_candidate_pass.py` universe 为 `799`，`scripts/update_weighted_winners.py` 后 Path2 window winner、robust candidate、tracked payload 未改变。本轮无 Path2 evict。
- 下一轮 focus：最终 guard 给出 `risk_reconfirm_sensitivity`。下一轮第一候选建议注册/确认更低风险、更高再确认的 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity` 与 `core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm99_caution54_cap14_cost_guard_v66_risk_reconfirm_sensitivity`；首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v66_ids>`；若未注册，先加入 Path2 scan family/list。

## 2026-06-30 06:12 CST 状态

- 上一轮候选/结果摘要：上一轮 v63 underrepresented 双周低换手只保留短窗弹性；本轮继续在独立 `growth_elastic` 池压风险、出场和单票 cap，没有引入 Path4 `emergent_theme`，也没有把 Path3 `_weekly` 当作 Path2 结论。
- 本轮候选 ID 与命令：新增并五窗口确认 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v64_ids>,<one_path3_id>,<three_path4_ids>`。
- 五窗口结果：`80/20 equal_weight` CAGR `5.49% / 6.52% / -4.96% / 49.04% / 61.15%`，最大回撤最差 `-31.90%`，年均换手最高 `20.15x`；`70/30 equal_weight` CAGR `7.37% / 8.87% / 0.62% / 56.35% / 99.45%`，最大回撤最差 `-26.27%`，年均换手最高 `19.44x`。
- 结论：v64 仍只提供 2025/2026 短窗弹性，2020/2023 不达 Path2 验收线且换手过高；`scripts/path2_candidate_pass.py` universe 更新为 `797`，`scripts/update_weighted_winners.py` 后 Path2 window winner、robust candidate 与 tracked payload 未改变。本轮无 Path2 evict。
- 下一轮 focus：最终 guard 给出 `medium_cycle_growth`。下一轮第一候选建议回到中周期增长修复双底座：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm98_caution56_cap16_cost_guard_v65_medium_cycle_growth_repair`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm98_caution56_cap16_cost_guard_v65_medium_cycle_growth_repair`；首条命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v65_medium_cycle_ids>`；若未注册，先加入 Path2 scan family/list。

## 2026-06-29 17:30 CST 状态

- 上一轮候选/结果摘要：上一轮留下 underrepresented 双周低换手 v62，本轮在独立 `growth_elastic` 池继续压风险、出场与单票 cap，未引入 Path4 emergent_theme。
- 本轮候选 ID 与命令：新增并运行 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn` 与 `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`；命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v63_ids>,<one_path3_id>,<three_path4_ids>`。
- 五窗口结果：`80/20 equal_weight` CAGR `4.74% / 6.78% / 4.57% / 25.62% / 62.16%`，最大回撤最差 `-33.72%`，年均换手最高 `20.38`；`70/30 equal_weight` CAGR `6.88% / 9.26% / 9.75% / 37.42% / 101.62%`，最大回撤最差 `-29.01%`，年均换手最高 `19.51`。
- 结论：v63 只保留短窗弹性，2017/2020/2023 中长窗弱且换手仍高；`update_weighted_winners.py` 后 Path2 window winner、robust candidate 与 tracked payload 未改变。本轮没有 Path2 evict。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> underrepresented_families`。下一轮第一候选建议不要继续单纯降 cap，改做低换手双周的确认/恢复门槛：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk18_exit38_cap12_cost_guard_v64_underrepresented_lowturn`；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v64_underrepresented_ids>`。

本文档用于约束和记录 `Path 2`（无约束上限探索）的研究方向。  
`Path 2` 的目标不是延续 `Path 1` 的稳健改良逻辑，而是作为**独立路线**去追求更高收益上限，优先冲击：

- `since_2020_01` 窗口 `40%+ CAGR`
- `since_2023_01` 窗口 `40%+ CAGR`

在这个阶段，`Path 2` 不要求先打赢 `Path 1` 才记录，也不要求先把回撤压到与 `Path 1` 同级；它的优先级是：

1. 先做出显著更高的收益上限
2. 再讨论如何把极端回撤收回来

当前已把 `Path 2` 的单轮探索预算提升到 **`24-36` 个显式原型 / `5` 条独立候选族**，并把 family-ranked 候选宇宙扩到 **`100+`** 规模；每条候选族固定保留 `4-6` 个代表候选。

## 本轮执行计划（2026-06-29 05:25 CST）

- 上一轮 v60 medium-cycle 只保留 2026 弹性，本轮按 `medium_cycle_growth` 注册并确认 v62 双底座，继续保持 Path2 `growth_elastic` 独立池，不把 Path4 emergent_theme 或 Path3 `_weekly` 变体当作 Path2 结论。实际命令与 Path3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v62_medium_cycle_growth,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v62_medium_cycle_growth,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap46_hold7_turn03_exit97_risk12_weekly_exit_buffer_weekly`。
- v62 total_mv 五窗口 CAGR `8.38% / 8.54% / 16.57% / 52.72% / 49.77%`，最大回撤 `-21.25% / -16.19% / -16.22% / -16.90% / -10.86%`，换手 `4.52x / 3.81x / 5.50x / 10.13x / 9.13x`；equal_weight 版 CAGR `5.81% / 6.12% / 8.88% / 31.36% / 78.17%`，最大回撤 `-27.25% / -17.67% / -21.10% / -21.10% / -10.28%`，换手 `4.87x / 4.00x / 5.83x / 10.81x / 9.85x`。结论：2025/2026 仍有弹性，但 2020/2023 没修到 Path2 验收线，且短窗换手偏高，不晋级。
- `scripts/path2_candidate_pass.py` 重跑后 universe 为 `793`，raw leaders/robust 未实质切换；`scripts/update_weighted_winners.py` 后 official Path2 robust 仍为 `...v34_reconfirm_balance`，`meanCAGR=23.50% / minCAGR=12.60%`。本轮没有 Path2 evict；代码中预留的 `v62_underrepresented_lowturn` 属于设计-only，未做五窗口确认，不计新增回测实验。
- 最终 focus 为 `risk_reconfirm_sensitivity`。下一轮第一条命令建议停止 v62 同形中周期修复，注册并确认更低风险/更高再确认的敏感性对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm98_caution56_cap16_cost_guard_v63_risk_reconfirm_sensitivity,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm98_caution56_cap16_cost_guard_v63_risk_reconfirm_sensitivity`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-28 17:40 CST）

- 上一轮预留 v60 medium-cycle 双底座，本轮接续启动前已注册候选，保持 Path2 独立 `growth_elastic` 池，不把独立 Path4 的 `PATH4_THEME_DISCOVERY_*` 变体加入 Path2 扫描池。`scripts/path2_candidate_pass.py` 重跑后 universe 为 `791`，raw robust 转向 `core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution80_cap95`，但 official robust 仍以后续 weighted 校验为准。
- 本轮候选 ID：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top8_risk34_mom_exit54_reconfirm88_caution66_cap20_cost_guard_v60_medium_cycle_repair` 与 `core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top8_risk34_mom_exit54_reconfirm88_caution66_cap20_cost_guard_v60_medium_cycle_repair`。总市值五窗口 CAGR `6.03% / 4.88% / 13.72% / 41.48% / 48.64%`，等权五窗口 CAGR `0.23% / -1.67% / 0.08% / 12.28% / 74.90%`；2026 有弹性但 2017/2020/2023 不足，未晋级。
- `scripts/update_weighted_winners.py` 后 Path2 official 2017 winner 为 `...v30_medium_cycle`，2025 winner 为 `...mom_confirm80_amt110_cap95`，robust candidate 为 `...v34_reconfirm_balance`，`meanCAGR=23.50% / minCAGR=12.60%`；Path2 rotation 因 signature 变化重置为 `continue`，最终 focus 为 `medium_cycle_growth`。本轮无 Path2 evict。
- `refresh_active` 曾按 `collect_ashare_refresh_active_ids()` 展开到 `99` 个 base ids，运行过久后中断；该中断只影响完整 active refresh，不影响 guard 覆盖，最终 coverage 仍 `ashare_path2_candidate_universe 791/791`。
- 下一轮第一条命令建议围绕 medium-cycle growth 只确认一个更温和的中周期增长修复双底座：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v62_medium_cycle_growth,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v62_medium_cycle_growth`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-27 19:24 CST）

- 上一轮 v45 capacity stress 未修复 2020/2023，本轮没有新增 Path2 `--only-base-ids`；实际工作是重跑 `scripts/path2_candidate_pass.py`、修正 Path2 pass 口径、执行 `refresh_active` 与 weighted 同步。继续保持 Path2 `growth_elastic` 独立池，没有把独立 Path4 的 `emergent_theme_quality_gate_signal*` 变体并入 Path2 扫描池。
- 本轮代码修正：`scripts/path2_candidate_pass.py` 额外排除 variant id 中包含 `emergent_theme_quality_gate_signal` 的强主题候选；重跑后 comparable universe 为 `789`。候选 pass raw leaders 为 2020 `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_ma_cap95`、2023 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom2_emergent_theme_quality_gate_risk30_cap50`、2025 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_core_6_1_full_risk_cap90`，raw robust 为 `core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_caution80_cap95`。
- `scripts/update_weighted_winners.py` 后 official Path2 robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v34_reconfirm_balance`，`meanCAGR=23.50%`、`minCAGR=12.60%`、最差回撤 `-16.87%`。weighted 2023 winner 同步为 `core_explore_90_10_total_mv_winner_core__aggr_03_97_prom2_emergent_theme_quality_gate_risk30_cap45`，但这是 Path2 历史粗主题风险线，不作为独立 Path4 结论。本轮无 Path2 evict。
- 最终 guard focus 为 `medium_cycle_growth`。下一轮第一条命令建议注册并确认中周期修复双底座，验收仍看 2020/2023 而不是单看 2026：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top8_risk34_mom_exit54_reconfirm88_caution66_cap20_cost_guard_v60_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top8_risk34_mom_exit54_reconfirm88_caution66_cap20_cost_guard_v60_medium_cycle_repair`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-25 06:56 CST）

- 上一轮 v58 未修复 2020/2023，本轮按最终 `underrepresented_families`/本轮 `capacity_and_cost_stress` 交集，在 Path2 `growth_elastic` 独立池注册 `momentum_equal_weight_elastic` v45 双底座；没有把 Path4 emergent_theme 或 Path3 `_weekly` 变体并入 Path2。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress`、`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path3/Path4 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v45_ids>,<one_path3_weekly_id>`。
- v45 total_mv 五窗口 CAGR `8.50% / 5.98% / 19.52% / 68.57% / 60.55%`，最大回撤 `-15.35% / -15.07% / -9.39% / -8.40% / -7.97%`；equal_weight 版 CAGR `10.38% / 9.50% / 22.17% / 57.89% / 62.02%`，最大回撤 `-17.53% / -15.69% / -15.29% / -15.29% / -15.43%`。结论：容量下降后回撤可控，但 2020/2023 远低于 Path2 目标线，不晋级。
- `scripts/path2_candidate_pass.py` 已重跑，候选池 `875`，其中 `momentum_equal_weight_elastic=45`、`biweekly_rebalance_aggressive=33`、`weekly_rebalance_aggressive=0`。`scripts/update_weighted_winners.py` validation 明确拒绝 v45 equal_weight 替换 `since_2020_01`，原因是 2023 校验 `22.17%` 低于 required `32.52%`；Path2 window winner、robust、tracked/live/public 未切换。本轮无 Path2 evict。
- 最终 focus 为 `capacity_and_cost_stress`。下一轮第一条命令应继续沿 v45 压容量/交易强度，但不能牺牲 2020/2023 到个位数：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-24 19:22 CST）

- 上一轮 v57 未修复 2020/2023，本轮按 `medium_cycle_growth` 在 Path2 `growth_elastic` 独立池注册 v58 双底座；未把 Path4 强主题涌现变体或 Path3 `_weekly` 候选并入 Path2 扫描池。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk34_mom_exit52_reconfirm88_caution64_cap22_cost_guard_v58_medium_cycle_restore`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk34_mom_exit52_reconfirm88_caution64_cap22_cost_guard_v58_medium_cycle_restore`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股其它路径合并执行。
- v58 total_mv 五窗口 CAGR `5.29% / 3.65% / 17.73% / 42.13% / 42.52%`，最大回撤 `-34.77% / -34.77% / -24.85% / -17.34% / -10.61%`，换手 `5.49x / 4.93x / 4.30x / 8.23x / 9.03x`；equal_weight 版 CAGR `0.27% / -1.53% / 9.22% / 13.17% / 75.86%`，最大回撤 `-38.48% / -37.09% / -26.62% / -21.70% / -11.15%`。结论：单一 2026 弹性不足以弥补 2020/2023 与长窗回撤，不晋级。
- `scripts/path2_candidate_pass.py` 候选数更新为 `871`；`scripts/update_weighted_winners.py` validation 继续拒绝近期 v57/v58 邻域，官方 Path2 window winner/robust/tracked/live/public 未因 v58 切换。本轮无 Path2 evict。
- 最终 guard 为 `pass`，下一轮 focus 转为 `risk_reconfirm_sensitivity`。第一条命令应停止 v58 同形中周期恢复，转向风险/再确认敏感性修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top8_risk32_mom_exit50_reconfirm92_caution62_cap20_cost_guard_v59_risk_reconfirm_sensitivity,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top8_risk32_mom_exit50_reconfirm92_caution62_cap20_cost_guard_v59_risk_reconfirm_sensitivity`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-24 06:57 CST）

- 上一轮 v56 仍未修复 2020/2023，本轮按预留 `risk_reconfirm_sensitivity` 注册并确认 v57 双底座；执行中同步修复 Path2 pass/weighted 过滤，明确排除 Path3 `_weekly` 和 `PATH4_THEME_DISCOVERY_VARIANT_IDS`，避免 Path2/3/4 口径污染。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk32_mom_exit50_reconfirm90_caution62_cap24_cost_guard_v57_risk_reconfirm_sensitivity`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk32_mom_exit50_reconfirm90_caution62_cap24_cost_guard_v57_risk_reconfirm_sensitivity`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股其它路径合并执行。
- v57 total_mv 五窗口 CAGR `7.70% / 6.99% / 12.49% / 42.87% / 39.90%`，最大回撤 `-30.25% / -30.25% / -15.73% / -17.27% / -10.49%`；equal_weight 版 CAGR `1.39% / -0.28% / 9.90% / 12.66% / 73.97%`，最大回撤 `-38.64% / -37.18% / -20.98% / -22.01% / -11.58%`。结论：单一 2026 弹性不足以抵消 2020/2023 弱势，`update_weighted_winners.py` validation 明确拒绝 v57。
- `scripts/path2_candidate_pass.py` 后 comparable candidate_count 从污染状态收敛为 `867`，`weekly_rebalance_aggressive=0`；窗口 winner 仍为旧高弹性族，robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，`meanCAGR=64.13%`、`minCAGR=35.34%`。本轮没有 Path2 evict，tracked/live/public 未切换。
- 下一轮 focus 为 `medium_cycle_growth`。第一条命令建议停止 v57 同形确认，注册一个更明确的中周期恢复/低拥挤对照：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-23 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk34_mom_exit52_reconfirm88_caution64_cap22_cost_guard_v58_medium_cycle_restore,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk34_mom_exit52_reconfirm88_caution64_cap22_cost_guard_v58_medium_cycle_restore`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-23 17:21 CST）

- 上一轮 v55 只保留短窗弹性，2020/2023 仍远低于 Path2 目标线；本轮按最终 focus `risk_reconfirm_sensitivity` 在 Path2 `growth_elastic` 独立池注册 v56 双底座，没有把 Path4 emergent_theme 或 Path3 weekly 结论混入 Path2。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk30_mom_exit48_reconfirm92_caution60_cap22_cost_guard_v56_risk_reconfirm_sensitivity`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk30_mom_exit48_reconfirm92_caution60_cap22_cost_guard_v56_risk_reconfirm_sensitivity`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股其它路径合并执行。
- total_mv 版五窗口 CAGR `8.80% / 9.77% / 6.50% / 54.13% / 49.27%`，最大回撤 `-24.70% / -17.51% / -15.75% / -17.10% / -10.61%`，换手 `5.16x / 4.55x / 4.20x / 9.99x / 8.97x`；equal_weight 版 CAGR `4.45% / 4.88% / 6.77% / 30.53% / 80.54%`。结论：短窗仍可动，但 2020/2023 太弱且 2025/2026 换手接近或超过 `9x`，不晋级。
- `scripts/path2_candidate_pass.py` 后候选池为 `1052`，最终 guard 为 `ashare_path2_candidate_universe 1052/1052 complete`；`scripts/update_weighted_winners.py` 后 Path2 window winner、robust candidate、tracked/live/public payload 未切换。本轮只把上一轮 Path3 低换手弱周频线同步归档出 active/scan 池，避免 Path2/Path3 口径污染；无 Path2 growth_elastic evict。
- 最终 focus 仍为 `risk_reconfirm_sensitivity`。下一轮第一条命令建议测试更宽确认/更高恢复阈值能否修复 2020/2023，而不是复跑 v56：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk32_mom_exit50_reconfirm90_caution62_cap24_cost_guard_v57_risk_reconfirm_sensitivity,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk32_mom_exit50_reconfirm90_caution62_cap24_cost_guard_v57_risk_reconfirm_sensitivity`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-23 05:27 CST）

- 上一轮 v54 2020/2023 仍偏弱；本轮按 `medium_cycle_growth` 在 Path2 `growth_elastic` 独立池中注册 v55 双底座，没有把 Path4 强主题涌现或 Path3 weekly 结论混入 Path2。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit46_reconfirm94_caution58_cap20_cost_guard_v55_medium_cycle_quality`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit46_reconfirm94_caution58_cap20_cost_guard_v55_medium_cycle_quality`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股其它路径合并执行。
- total_mv 版五窗口 CAGR `8.70% / 8.90% / 6.84% / 54.03% / 51.06%`，最大回撤 `-21.13% / -14.38% / -13.18% / -16.94% / -10.73%`，换手 `4.82x / 4.18x / 3.72x / 10.05x / 9.04x`；equal_weight 版 CAGR `4.13% / 3.55% / 8.12% / 31.82% / 82.81%`。结论：2025/2026 有弹性但 2020/2023 远低于 Path2 目标线，且短窗换手偏高，不晋级。
- `scripts/path2_candidate_pass.py` 后候选池为 `1048`，最终 guard 为 `ashare_path2_candidate_universe 1048/1048 complete`；`scripts/update_weighted_winners.py` 后 Path2 window winner、robust candidate、tracked/live/public payload 未切换。本轮无 Path2 evict。
- 最终 focus 仍为 `medium_cycle_growth`。下一轮第一条命令建议停止 v55 同形微调，改测更高确认/更低 cap 的中周期质量修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk30_mom_exit48_reconfirm92_caution60_cap22_cost_guard_v56_medium_cycle_quality_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk30_mom_exit48_reconfirm92_caution60_cap22_cost_guard_v56_medium_cycle_quality_repair`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-22 17:34 CST）

- 上一轮 `momentum_equal_weight_elastic` v44 的 2020/2023 仍远低于 Path2 目标线；本轮按 rotation 的 `medium_cycle_growth` 回到 `growth_elastic` 独立池，没有把 Path4 emergent_theme 或 Path3 weekly 变体纳入 Path2 扫描结论。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v54_medium_cycle_rebound`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v54_medium_cycle_rebound`。实际命令与 A股其它路径合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v54_medium_cycle_rebound,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit44_reconfirm96_caution56_cap18_cost_guard_v54_medium_cycle_rebound,...`。
- total_mv 版五窗口 CAGR `8.39% / 8.50% / 16.93% / 53.89% / 52.84%`，最大回撤 `-21.08% / -16.14% / -16.11% / -16.78% / -10.86%`，换手 `4.50x / 3.80x / 5.48x / 10.11x / 9.11x`；equal_weight 版 CAGR `5.82% / 6.04% / 9.42% / 33.10% / 85.05%`。结论：2025/2026 弹性仍在，但 2020/2023 低于 Path2 中周期目标线，且短窗换手偏高，不晋级。
- 为保持候选池可读性，本轮把 v50/v51 capacity/risk_reconfirm 四个旧 base ids 加入 `PATH2_ARCHIVED_STRATEGY_BASE_IDS`，并在 `scripts/path2_candidate_pass.py` 中排除 archived ids；同时把本轮 Path3 纯周频 base id 排除出 Path2 pass，避免跨路径污染。最终 `path2_candidate_pass` 候选数回到 `1043`，robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，Path2 window winner/robust/tracked 未切换。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 1043/1043 complete`，最终 focus 仍为 `medium_cycle_growth`。下一轮第一条命令建议在 v54 基础上增加质量确认但降低短窗交易强度：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit46_reconfirm94_caution58_cap20_cost_guard_v55_medium_cycle_quality,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit46_reconfirm94_caution58_cap20_cost_guard_v55_medium_cycle_quality`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-22 05:23 CST）

- 上一轮预留 `underrepresented_families` 的 `momentum_equal_weight_elastic` v44；本轮仍使用 Path2 `growth_elastic` 独立池，没有把 Path4 emergent_theme 结果并入 Path2。因本地 A股缓存最新日为 `2026-06-18`，实际回测命令显式锁定 `--end-date 2026-06-18`。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair`、`core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair`。实际命令与 Path1/3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair,core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair,...`。
- equal_weight 版五窗口 CAGR `10.49% / 9.84% / 8.97% / 54.07% / 52.14%`，最大回撤 `-17.79% / -16.76% / -11.75% / -15.59% / -15.73%`，换手 `4.08x / 3.78x / 3.47x / 8.82x / 8.14x`；total_mv 版 CAGR `10.26% / 8.44% / 8.57% / 66.22% / 51.26%`，最大回撤 `-14.91% / -15.08% / -10.00% / -8.45% / -7.65%`，换手 `3.77x / 3.50x / 3.38x / 7.79x / 6.91x`。结论：total_mv 版更稳且短窗更强，但 2020/2023 远低于 Path2 目标线，短窗换手仍过高，不晋级。
- `scripts/path2_candidate_pass.py` 后候选池输出 `1043`；`scripts/update_weighted_winners.py` validation 未接受本轮候选，Path2 window winner、robust candidate、tracked/live/public payload 未切换。本轮无 Path2 evict。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 1038/1038 complete`，最终 focus 转为 `capacity_and_cost_stress`。下一轮第一条命令建议在 v44 的 total_mv 短窗优势上继续压单票和交易强度：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress,core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk24_exit44_cap18_cost_guard_v45_capacity_stress`；若未注册，先加入 Path2 scan family/list。

## 本轮执行计划（2026-06-21 17:29 CST）

- 上一轮 v52 中周期修复仍未改善 2020/2023，且没有改写 Path2 window winner/robust；本轮沿 `risk_reconfirm_sensitivity` 注册并确认两个 v53 风险敏感候选，仍使用 `growth_elastic` 独立池，没有把 Path4 emergent_theme 结果并入 Path2。
- 本轮 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v53_risk_sensitivity`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v53_risk_sensitivity`。命令类型为五窗口 `--only-base-ids` 增量确认，实际与 A股 Path1/3/4 合并执行。
- total_mv 版五窗口 CAGR `6.86% / 5.98% / 16.53% / 52.14% / 58.40%`，最大回撤 `-22.18% / -22.18% / -15.88% / -16.37% / -10.79%`，换手 `4.34x / 3.70x / 5.35x / 10.01x / 9.03x`；equal_weight 版 CAGR `4.82% / 3.83% / 10.35% / 34.44% / 85.26%`。结论：短窗有弹性但 2020/2023 远低于 Path2 目标线，且换手偏高，不晋级。
- `scripts/path2_candidate_pass.py` 后候选池为 `1038`；`scripts/update_weighted_winners.py` 后 Path2 window winner、robust candidate、tracked/live/public payload 未切换。本轮无 Path2 evict。
- 最终 focus 转为 `underrepresented_families`；映射到下一轮候选池为 `momentum_equal_weight_elastic` 与 `biweekly_rebalance_aggressive` 的欠代表形态。下一轮第一条命令建议先注册并确认一条 underrep 质量/成本修复线：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair,core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk24_exit44_cap20_cost_guard_v44_underrep_repair`；若未注册，先加入 Path2 scan family。

## 本轮执行计划（2026-06-21 05:23 CST）

- 上一轮预留 `v52_medium_cycle_repair`；本轮注册并五窗口确认两个 Path2 growth_elastic base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v52_medium_cycle_repair`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v52_medium_cycle_repair`。
- 命令类型为五窗口 `--only-base-ids` 增量确认。total_mv 版 CAGR `8.97% / 9.32% / 16.91% / 53.93% / 54.98%`，最大回撤 `-20.58% / -16.05% / -16.04% / -16.60% / -10.98%`，换手 `4.48x / 3.80x / 5.47x / 10.16x / 9.17x`；equal_weight 版 CAGR `6.39% / 6.58% / 10.11% / 34.53% / 87.38%`，回撤 `-25.13% / -17.77% / -20.79% / -20.79% / -9.84%`。
- `scripts/path2_candidate_pass.py` 后候选池为 `1033`；`scripts/update_weighted_winners.py` 的验证层拒绝本轮相关候选，Path2 window winner、robust candidate、tracked/live/public payload 未切换。本轮无 Path2 evict。
- 最终 focus 为 `risk_reconfirm_sensitivity`。下一轮第一条命令建议在 v52 的 2025/2026 弹性基础上降低风险确认敏感度与换手：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v53_risk_sensitivity,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v53_risk_sensitivity`；若未注册，先加入 Path2 scan 规则。

## 本轮执行计划（2026-06-20 17:27 CST）

- 上一轮 v50 capacity stress 没有修复 2020/2023；本轮继续使用 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入 Path2 scan。新增并五窗口确认 2 个 v51 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit39_reconfirm99_caution51_cap12_cost_guard_v51_risk_reconfirm`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit39_reconfirm99_caution51_cap12_cost_guard_v51_risk_reconfirm`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit39_reconfirm99_caution51_cap12_cost_guard_v51_risk_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit39_reconfirm99_caution51_cap12_cost_guard_v51_risk_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold9_turn01_exit99_risk06_weekly`。
- v51 总市值版五窗口 CAGR `6.43% / 5.83% / 14.29% / 44.14% / 48.77%`，最大回撤 `-19.68% / -19.68% / -13.64% / -14.09% / -9.20%`，换手 `3.87x / 3.35x / 4.58x / 8.59x / 7.74x`；等权版 CAGR `4.59% / 3.84% / 9.15% / 29.48% / 70.89%`，最大回撤 `-18.98% / -18.98% / -17.48% / -17.48% / -8.07%`。结论：2026 弹性保留，但 2020/2023 仍远低于 Path2 目标线，且短窗换手偏高，不晋级。
- `scripts/path2_candidate_pass.py` 后候选池为 `1028/1028 complete`，四窗口 winner 与 robust 仍由既有高弹性/周频组合占优；`scripts/update_weighted_winners.py` 后 Path2 tracked/live/public 未切换。本轮无 evict。最终 focus 重置为 `medium_cycle_growth`，下一轮第一条命令建议停止 v51 同形风险再确认，回到中周期成长质量修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v52_medium_cycle_repair,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v52_medium_cycle_repair`；若未注册，先加入 Path2 `high_growth_theme` 候选池。

## 本轮执行计划（2026-06-20 05:28 CST）

- 上一轮 v49 风险再确认继续牺牲 2020/2023；本轮仍使用 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入 Path2 scan。新增并五窗口确认 2 个 v50 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit38_reconfirm99_caution50_cap12_cost_guard_v50_capacity_stress`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit38_reconfirm99_caution50_cap12_cost_guard_v50_capacity_stress`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit38_reconfirm99_caution50_cap12_cost_guard_v50_capacity_stress,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit38_reconfirm99_caution50_cap12_cost_guard_v50_capacity_stress,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap34_hold8_turn02_exit99_risk06_weekly`。
- v50 总市值版五窗口 CAGR `6.49% / 5.80% / 14.23% / 44.12% / 48.55%`，最大回撤 `-19.66% / -19.66% / -13.60% / -14.04% / -9.20%`，换手 `3.85x / 3.34x / 4.56x / 8.58x / 7.73x`；等权版 CAGR `4.64% / 3.85% / 9.21% / 29.50% / 70.91%`，最大回撤 `-18.65% / -18.65% / -17.48% / -17.48% / -8.07%`。结论：容量/成本压力没有修复 2020/2023，中周期收益远低于 Path2 目标线，不晋级。
- `scripts/path2_candidate_pass.py` 后四窗口 winner 与 robust 仍为旧高弹性/周频组合；`scripts/update_weighted_winners.py` 后 Path2 tracked/live/public 未切换。最终 coverage 为 `ashare_path2_candidate_universe 1023/1023 complete`，无 evict。最终 focus 为 `risk_reconfirm_sensitivity`，下一轮第一条命令建议在 v50 失败后做风险/再确认敏感性，而不是复跑 v50：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v51_risk_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v51_risk_reconfirm`；若未注册，先加入 Path2 `high_growth_theme` 候选池。

## 本轮执行计划（2026-06-19 17:29 CST）

- 上一轮 v48 短窗有弹性但 2020/2023 不达标；本轮继续使用 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入 Path2 scan。新增并五窗口确认 2 个 Path2 v49 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v49_risk_reconfirm`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v49_risk_reconfirm`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path1/3/4 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v49_risk_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v49_risk_reconfirm`。
- v49 总市值版五窗口 CAGR `6.91% / 6.01% / 16.42% / 52.14% / 58.40%`，最大回撤 `-22.05% / -22.05% / -15.88% / -16.37% / -10.79%`；等权版 CAGR `4.97% / 3.98% / 10.54% / 34.44% / 85.26%`，最大回撤 `-21.81% / -21.40% / -20.20% / -20.20% / -9.41%`。结论：风险再确认继续牺牲 2020/2023，不晋级。
- `scripts/path2_candidate_pass.py` 后四窗口 winner 与 robust 仍为旧高弹性/周频组合；`scripts/update_weighted_winners.py` 后 Path2 tracked/live/public 未切换。最终 coverage 为 `ashare_path2_candidate_universe 1018/1018 complete`，无 evict。最终 focus 为 `capacity_and_cost_stress`，下一轮第一条命令建议在 v49 上进一步压容量/成本而不是回到 v48：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit38_reconfirm99_caution50_cap12_cost_guard_v50_capacity_stress,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit38_reconfirm99_caution50_cap12_cost_guard_v50_capacity_stress`；若未注册，先加入 Path2 `high_growth_theme` 候选池。

## 本轮执行计划（2026-06-19 05:26 CST）

- 上一轮 v47 capacity/cost 下移未修复 2020/2023；本轮继续使用 Path2 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入 Path2 scan，新增并五窗口确认 2 个 Path2 v48 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth`。
- 本轮命令类型为五窗口 `--only-base-ids` 增量确认，实际与 Path3 合并执行：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap38_hold7_turn02_exit99_risk08_weekly`。
- v48 总市值版五窗口 CAGR `8.98% / 9.29% / 16.85% / 53.93% / 54.98%`，最大回撤 `-20.37% / -16.05% / -16.04% / -16.60% / -10.98%`；等权版 CAGR `6.43% / 6.58% / 10.21% / 34.53% / 87.38%`，最大回撤 `-24.87% / -17.77% / -20.79% / -20.79% / -9.84%`。结论：短窗仍有弹性，但 2020/2023 远低于 Path2 目标线，且 2025/2026 换手约 `9x-10x`，不晋级。
- `scripts/path2_candidate_pass.py` 后四窗口 winner 与 robust 仍为旧高弹性/周频组合；`scripts/update_weighted_winners.py` 后 Path2 tracked/live/public 未切换。最终 coverage 为 `ashare_path2_candidate_universe 1013/1013 complete`，无 evict。最终 focus 为 `risk_reconfirm_sensitivity`，下一轮第一条命令建议在 v48 上继续做风险/再确认敏感性而不是复跑 v48：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-18 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v49_risk_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk18_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v49_risk_reconfirm`；若未注册，先加入 Path2 `high_growth_theme` 候选池。

## 本轮执行计划（2026-06-18 17:16 CST）

- 上一轮 v46 风险确认只保留短窗弹性，2020/2023 不达标；本轮继续沿 `growth_elastic` 独立池做容量/成本压力下移，新增并五窗口确认 2 个 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v47_capacity_cost`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v47_capacity_cost`。命令类型为五窗口 `--only-base-ids` 增量确认，未把 Path4 emergent_theme 并入 Path2。
- v47 总市值版五窗口 CAGR `6.86% / 5.96% / 16.43% / 52.00% / 57.98%`，最大回撤 `-22.11% / -22.11% / -15.88% / -16.37% / -10.79%`；等权版 CAGR `4.94% / 3.95% / 11.16% / 36.49% / 93.86%`，最大回撤 `-21.96% / -21.80% / -20.20% / -20.20% / -9.41%`。结论：容量下移没有修复 2020/2023，中周期收益仍远弱于 Path2 winner，不晋级。
- `scripts/path2_candidate_pass.py` 后四窗口 winner 与 robust 仍为旧候选，`scripts/update_weighted_winners.py` 后 Path2 tracked/live/public payload 未切换；Path2 candidate universe 变为 `1008/1008 complete`，无 evict。
- 最终 focus 为 `medium_cycle_growth`。下一轮第一条命令建议回到中周期成长而非继续压 cap：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm97_caution54_cap16_cost_guard_v48_medium_cycle_growth`；若未注册，先加入 Path2 `high_growth_theme` 候选池。

## 本轮执行计划（2026-06-18 05:21 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 1004/1004 complete`；本轮继续使用 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入 Path2 scan。`scripts/path2_candidate_pass.py` 后四窗口 winner 与 robust 仍由旧高弹性/周频组合占优，本轮 v46 未改变 winner/robust/tracked。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v46_risk_reconfirm_growth`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v46_risk_reconfirm_growth`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- v46 总市值版五窗口 CAGR `6.47% / 5.63% / 16.75% / 53.85% / 52.29%`，最大回撤 `-22.98% / -22.98% / -15.99% / -16.67% / -10.86%`；等权版 CAGR `3.88% / 3.09% / 10.30% / 35.16% / 93.46%`，最大回撤 `-26.25% / -24.11% / -21.10% / -21.10% / -10.28%`。结论：短窗弹性保留但 2020/2023 远低于 Path2 目标线，不晋级。
- 本轮无 Path2 evict。最终 focus 为 `capacity_and_cost_stress`，下一轮第一条命令建议从 high-growth 同形转为容量/成本压力复核：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-17 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v47_capacity_cost,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk20_mom_exit40_reconfirm98_caution52_cap14_cost_guard_v47_capacity_cost`；若未注册，先加入 Path2 `high_growth_theme`/medium-cycle 候选池。

## 本轮执行计划（2026-06-17 18:02 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 999/999 complete`；本轮 Path2 仍使用 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入 Path2 scan。`scripts/path2_candidate_pass.py` 后四窗口 winner 与 robust 仍为旧高弹性组合，本轮 v45 未改变 winner/robust/tracked。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v45_medium_cycle_growth`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v45_medium_cycle_growth`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- v45 总市值版五窗口 CAGR `8.00% / 7.87% / 16.54% / 53.07% / 47.82%`，最大回撤 `-21.15% / -16.30% / -16.07% / -16.82% / -10.73%`，换手 `4.46x / 3.75x / 5.46x / 10.03x / 9.01x`；等权版 CAGR `5.31% / 5.39% / 9.63% / 33.79% / 90.81%`，最大回撤 `-27.87% / -17.46% / -21.40% / -21.40% / -10.72%`。结论：中周期成长核心能给短窗弹性，但 2020/2023 远低于 Path2 目标线且 2025/2026 换手过高，不晋级。
- 本轮无 Path2 evict。最终 focus 为 `risk_reconfirm_sensitivity`。下一轮第一条命令建议在 v45 的中周期成长核心上压风险/单票/再确认，而不是复跑 v45：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v46_risk_reconfirm_growth,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v46_risk_reconfirm_growth`；若未注册，先加入 Path2 `high_growth_theme`/medium-cycle 候选池。

## 本轮执行计划（2026-06-17 05:20 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 994/994 complete`；本轮 Path2 只运行 `scripts/path2_candidate_pass.py` 巡检与 weighted 同步，没有新增 Path2 `--only-base-ids` 回测，继续保持 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入 Path2 scan。
- `scripts/path2_candidate_pass.py` 后四窗口 winner 仍由既有高弹性家族占优，robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95`；`scripts/update_weighted_winners.py` 的 official Path2 candidate 仍为旧低换手周频形态，window winner、robust candidate、tracked/live/public payload 未因本轮改变。本轮无 Path2 evict。
- 本轮未回测原因：新增策略预算优先给 `ashare_path4_emergent_theme` 的 capacity/cost 三底座和 HK Path4-7 四条扩展候选；Path2 完成候选设计但不消耗新增实验名额。
- 最终 focus 为 `medium_cycle_growth`。下一轮第一条命令建议把上一轮 v43 低相关弹性失败后转回中周期增长修复：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-16 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v45_medium_cycle_growth,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v45_medium_cycle_growth`；若未注册，先注册到 Path2 `high_growth_theme`/medium-cycle 候选池。

## 本轮执行计划（2026-06-16 17:36 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 986/986 complete`；上一轮预留的 underrepresented `momentum_equal_weight_elastic` v43 本轮已注册并五窗口确认，Path2 仍使用 `growth_elastic` 独立池，没有吸收 Path4 emergent_theme 结果。
- 本轮新增并五窗口确认 2 个 Path2 base ids：`core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality`、`core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality`。实际命令为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- v43 总市值版 CAGR 为 `8.26% / 5.39% / 7.49% / 63.25% / 37.86%`，最大回撤 `-15.00% / -15.85% / -10.37% / -9.10% / -6.71%`；等权 70/30 版 CAGR 为 `8.34% / 6.07% / 9.86% / 41.00% / 26.73%`，最大回撤 `-28.10% / -28.10% / -16.55% / -17.67% / -17.77%`。结论：两条都没有修复 2020/2023 收益断层，不替换 Path2 window winner、robust candidate 或 tracked payload；本轮无 Path2 evict。
- `scripts/path2_candidate_pass.py` 巡检后 Path2 robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly`。最终 focus 为 `capacity_and_cost_stress`，下一轮第一条命令建议把 `v43` 的短窗弹性转为更低 cap/成本压力复核：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-15 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk26_exit46_cap22_cost_guard_v44_capacity_cost,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk26_exit46_cap22_cost_guard_v44_capacity_cost`；若未注册，先加入 `momentum_equal_weight_elastic` family。

## 本轮执行计划（2026-06-16 05:17 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 986/986 complete`；`scripts/path2_candidate_pass.py` 后 comparable universe 刷到 `986`。Path2 继续保持 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入扫描池或结论。
- 本轮新增并五窗口确认 2 个 Path2 v42 风险确认候选：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- v42 总市值版五窗口 CAGR 为 `12.88% / 13.15% / 7.96% / 44.15% / 15.54%`，最大回撤 `-18.69% / -15.14% / -13.36% / -15.12% / -13.20%`；等权版 CAGR 为 `9.51% / 11.19% / 7.63% / 26.66% / 33.56%`，最大回撤 `-23.09% / -14.92% / -15.32% / -11.16% / -11.15%`。结论：短窗有一定弹性但 2020/2023 远低于 Path2 目标线，不替换 window winner、robust candidate 或 tracked payload。
- 本轮没有 Path2 evict。最终 guard 将 focus 推到 `underrepresented_families`，v42 risk-reconfirm 同形确认失败后，下一轮第一条命令应暂停 high-growth/liqmom 风险确认，转向低相关 `momentum_equal_weight_elastic` 代表：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top14_risk28_exit48_cap26_cost_guard_v43_underrep_quality`；若未注册，先注册到 Path2 scan 池。

## 本轮执行计划（2026-06-15 17:18 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 982/982 complete`；`scripts/path2_candidate_pass.py` 后 comparable universe 刷到 `982`，其中 `momentum_equal_weight_elastic` 扩到 `39`。Path2 继续保持 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入扫描池或结论。
- 本轮新增并五窗口确认 2 个 Path2 v41 underrepresented quality 候选：`core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk26_exit46_cap24_cost_guard_v41_underrep_quality`、`core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk26_exit46_cap24_cost_guard_v41_underrep_quality`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- v41 `80/20 total_mv` 五窗口 CAGR 为 `9.05% / 6.55% / 7.58% / 60.12% / 30.87%`，最大回撤 `-14.55% / -15.64% / -10.21% / -8.63% / -7.02%`；`70/30 equal` CAGR 为 `9.13% / 8.09% / 9.87% / 36.98% / 15.14%`，最大回撤 `-21.72% / -21.72% / -13.34% / -17.40% / -17.51%`。结论：短窗尚有弹性但 2020/2023 远低于 Path2 目标线，不替换 window winner、robust candidate 或 tracked payload。
- 本轮没有 Path2 evict。最终 focus 为 `risk_reconfirm_sensitivity`。下一轮第一条命令建议停止 underrepresented v41 同形，回到 high-growth/liqmom 的风险确认敏感性双底座：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution60_cap24_cost_guard_v42_risk_reconfirm`；若未注册，先注册到 Path2 scan 池。

## 本轮执行计划（2026-06-15 05:39 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 979/979 complete`；本轮执行 `scripts/path2_candidate_pass.py` 后 comparable universe 刷到 `979`。Path2 继续保持 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入扫描池或结论。
- 本轮新增并五窗口确认 2 个 Path2 v40 中周期质量修复候选：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v40_medium_cycle_quality`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v40_medium_cycle_quality`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，并与 Path3 新周频候选合并执行。
- v40 总市值版五窗口 CAGR 为 `11.17% / 10.42% / 13.37% / 41.93% / 17.23%`，最大回撤 `-16.05% / -15.49% / -14.94% / -14.94% / -12.99%`；等权版为 `9.08% / 10.08% / 10.24% / 28.45% / 40.53%`，最大回撤 `-20.26% / -12.98% / -15.18% / -10.34% / -10.34%`。结论：短窗有弹性但 2020/2023 远低于 Path2 目标线，不替换 window winner、robust candidate 或 tracked payload。
- 本轮没有 Path2 evict。最终 focus 为 `underrepresented_families`，下一轮第一条命令应暂停 high-growth 同形扩参，转向低相关 `momentum_equal_weight_elastic` 代表：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk26_exit46_cap24_cost_guard_v41_underrep_quality,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top12_risk26_exit46_cap24_cost_guard_v41_underrep_quality`；若未注册，先注册到 Path2 scan 池。

## 本轮执行计划（2026-06-14 17:25 CST）

- 开局 guard 为 `pass`，本轮注册并五窗口确认 3 个 Path2 v39 capacity stress 候选；`scripts/path2_candidate_pass.py` 后 comparable universe 刷到 `974`，`momentum_equal_weight_elastic` 扩到 `37` 个候选。Path2 仍保持 `growth_elastic` 独立池，没有把 Path4 emergent_theme 变体并入扫描池或结论。
- 本轮新增 ID：`core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk28_exit48_cap28_cost_guard_v39_capacity_stress`、`core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk28_exit48_cap28_cost_guard_v39_capacity_stress`、`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk28_exit48_cap28_cost_guard_v39_capacity_stress`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- v39 `80/20 total_mv` 五窗口 CAGR 为 `6.08% / 2.12% / 17.16% / 60.31% / 28.37%`，最大回撤 `-21.30% / -21.30% / -10.63% / -9.15% / -6.39%`，换手 `3.81x / 3.45x / 4.33x / 7.74x / 6.96x`；`70/30 equal` 为 `6.68% / 3.91% / 14.99% / 32.85% / 7.08%`；`80/20 equal` 为 `5.76% / 4.33% / 17.43% / 36.94% / 11.45%`。结论：短窗弹性尚可，但 2020/2023 远低于 Path2 目标线，不替换 window winner、robust candidate 或 tracked payload。
- 本轮没有 Path2 evict。中段 guard focus 转向 `medium_cycle_growth`，下一轮第一条命令建议停止 v39 容量压缩，注册并确认中周期质量修复双底座：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v40_medium_cycle_quality,core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v40_medium_cycle_quality`；若未注册，先注册到 Path2 scan 池。

## 本轮执行计划（2026-06-14 05:29 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 967/967 complete`；本轮执行 `scripts/path2_candidate_pass.py` 后 comparable universe 刷到 `967`，`momentum_equal_weight_elastic` 扩到 `33` 个候选，继续保持 Path2 `growth_elastic` 独立池，不把 Path4 emergent_theme 结果并入 Path2 结论。
- 本轮新增并五窗口确认 3 个 Path2 v38 underrepresented/capacity 对照：`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep`、`core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep`、`core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep`。合并增量命令覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`，命令类型为 `--only-base-ids`，没有改跑全量。
- v38 `80/20 equal` 五窗口 CAGR 为 `3.25% / 1.13% / 15.04% / 29.41% / -2.65%`，`70/30 equal` 为 `5.29% / 2.96% / 13.56% / 25.89% / -5.82%`，`80/20 total_mv` 为 `4.12% / -0.54% / 21.49% / 60.74% / 23.87%`。结论：总市值版短窗较强，但 2020 转负且长窗弱，两个等权版也低于 Path2 目标线；不替换 Path2 window winner、robust candidate 或 tracked payload。
- `path2_candidate_pass.py` 后 family robust 仍为旧 high-growth/liquidity momentum 族，`scripts/update_weighted_winners.py` 未采纳 v38。本轮没有 Path2 evict。最终 focus 为 `capacity_and_cost_stress`，下一轮第一条命令建议在 v38 的 `80/20 total_mv` 上继续压 cap/成本并观察 2020 能否转正：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk28_exit48_cap28_cost_guard_v39_capacity_stress,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk28_exit48_cap28_cost_guard_v39_capacity_stress`；若未注册，先注册到 Path2 scan 池，且不要引入 Path4 emergent_theme 变体。

## 本轮执行计划（2026-06-13 17:30 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 962/962 complete`；本轮执行 `scripts/path2_candidate_pass.py` 后 comparable universe 刷到 `962`，继续保持 Path2 `growth_elastic` 独立池，不把 Path4 emergent_theme 结果并入 Path2 结论。
- 本轮新增并五窗口确认 2 个 Path2 v37 中周期修复候选：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair`。命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk27_mom_exit47_reconfirm95_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap48_hold6_turn03_exit98_risk14_weekly`。
- v37 总市值版五窗口 CAGR 为 `13.11% / 12.99% / 8.32% / 43.04% / 16.38%`，最大回撤为 `-16.35% / -14.98% / -13.35% / -15.03% / -13.10%`，短窗换手升至 `9.68x / 9.19x`；等权版 CAGR 为 `9.88% / 11.16% / 7.94% / 27.55% / 36.97%`，最大回撤为 `-20.06% / -13.94% / -14.96% / -10.75% / -10.74%`。结论：v37 接近 2017 raw 排名前列，但 2020/2023 离 Path2 目标线太远，且短窗换手偏高，不替换 Path2 window winner、robust candidate 或 tracked payload。
- `path2_candidate_pass.py` 后 family robust 仍由旧高增长 liqmom 族占据，`update_weighted_winners.py` 后官方 tracked 也未切换。本轮没有 Path2 evict。最终 focus 为 `underrepresented_families`，下一轮第一条命令建议暂停 high-growth v 系列，补一个低相关高弹性代表：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep,core_explore_70_30_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top10_risk30_exit50_cap35_cost_guard_v38_underrep`；若未注册，先注册到 Path2 scan 池，且不要引入 Path4 emergent_theme 变体。

## 本轮执行计划（2026-06-13 05:09 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 954/954 complete`；本轮执行 `scripts/path2_candidate_pass.py` 后 comparable universe 刷到 `957`。上一轮预留的 v36 风险确认双底座已在 comparison 中具备五窗口结果，本轮只做 universe 刷新和结果判读，没有重跑 A股 Path2 `--only-base-ids`。
- 本轮候选 ID 与结果摘要：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm98_caution54_cap24_cost_guard_v36_risk_reconfirm` 五窗口 CAGR 为 `6.73% / 6.46% / 9.38% / 25.17% / 28.18%`，最大回撤 `-27.51% / -27.51% / -15.79% / -11.16% / -11.15%`；`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm98_caution54_cap24_cost_guard_v36_risk_reconfirm` 为 `8.81% / 6.54% / 14.19% / 44.57% / 15.46%`，最大回撤 `-26.52% / -26.52% / -14.72% / -14.72% / -13.20%`。
- 结论：v36 总市值版改善短窗回撤但 2020/2023 仍显著低于 Path2 目标线，等权版也没有恢复中窗；`update_weighted_winners.py` 后 Path2 robust 仍不是 v36，当前 weighted robust 为 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold4_turn06_exit94_weekly`，`meanCAGR=38.25%`、`minCAGR=14.60%`。本轮没有 Path2 evict。
- 本轮命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py` 与 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/update_weighted_winners.py`。下一轮 focus 为 `medium_cycle_growth`，第一条命令建议暂停 v36 同形风险确认，转回中周期收益修复双底座：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-12 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v37_medium_cycle_repair,core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v37_medium_cycle_repair`；若未注册，先注册到 Path2 scan 池。

## 本轮执行计划（2026-06-12 05:28 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 954/954 complete`；`scripts/path2_candidate_pass.py` 重建 comparable universe 到 `954`。上一轮 v34 双底座未改 winner/robust，本轮按 `medium_cycle_growth` 增加双周弹性低换手 v35 对照，仍保持 Path2 独立于 Path4 emergent_theme。
- 本轮新增并五窗口确认 2 个 Path2 `biweekly_rebalance_aggressive` 候选：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn`。命令类型为五窗口 `--only-base-ids` 增量确认，覆盖 `since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01`。
- v35 `80/20 equal` 五窗口 CAGR 为 `-0.59% / 4.07% / -0.45% / 12.89% / 14.90%`，最大回撤为 `-56.05% / -29.05% / -23.17% / -17.64% / -17.82%`，2026 换手 `20.59x`；`70/30 equal` 为 `1.47% / 5.78% / 3.26% / 20.16% / 31.81%`，最大回撤 `-50.41% / -26.40% / -23.27% / -16.91% / -17.45%`，2026 换手 `19.68x`。结论：低 cap 没有修复 2017/2020/2023，短窗也被高换手侵蚀，不替换 Path2 window winner、robust candidate 或 tracked payload。
- `path2_candidate_pass.py` 后 robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=64.36%`、`minCAGR=36.67%`。本轮没有 Path2 evict；v35 只保留为“低 cap 双周弹性失败对照”。
- 最终 guard focus 轮到 `risk_reconfirm_sensitivity`。下一轮第一条命令建议停止继续压 cap，回到 liqmom/promo 的风险确认邻域做双底座复核：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-11 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm98_caution54_cap24_cost_guard_v36_risk_reconfirm,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm98_caution54_cap24_cost_guard_v36_risk_reconfirm`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-07 16:06 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 915/915 complete`；`scripts/path2_candidate_pass.py` 重建 comparable universe 到 `915`。上一轮 high-growth v23 仍未达 2023 验收线，本轮预算投给 Path1/3/4 与 HK Path3/4/6/7，Path2 不新增回测，只做 universe 巡检和下一轮候选设计。
- 本轮命令类型为 `scripts/path2_candidate_pass.py` 候选宇宙刷新；没有新增 `--only-base-ids` Path2 回测。刷新后 Path2 window winners 与 robust candidate 未切换，robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=64.36%`、`minCAGR=36.67%`。
- 候选池结构仍偏重 `high_growth_theme=363` 与 `high_concentration_breakout=154`，但新增 Path1 core 多因子已进入低相关扫描面；本轮不把该 universe refresh 伪装成新策略实验。没有 Path2 evict。
- 最终 guard 将下一轮 focus 推到 `medium_cycle_growth`。下一轮第一条命令建议暂停高增长小步降 cap，改测中周期恢复确认与较低集中度双底座：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm92_caution60_cap32_cost_guard_v24_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm92_caution60_cap32_cost_guard_v24_medium_cycle`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-07 04:26 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 909/909 complete`；`scripts/path2_candidate_pass.py` 重建 comparable universe 到 `909`。上一轮 v22 修复 2023 但 2020/长窗不足，本轮按 `risk_reconfirm_sensitivity` 确认 v23 双底座，并保留非 high-growth 族下一轮设计以避免候选池继续被 `high_growth_theme` 压重。
- 本轮新增并五窗口确认 2 个 Path2 `high_growth_theme` 候选：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm`。命令类型为五窗口 `--only-base-ids` 增量确认，实际命令为：`AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap58_hold4_turn04_exit94_risk25_weekly`。
- v23 等权版五窗口 CAGR 为 `12.84% / 25.32% / 29.67% / 82.77% / 16.22%`，最大回撤为 `-37.07% / -17.33% / -22.35% / -20.61% / -10.20%`；总市值版为 `12.16% / 22.31% / 29.02% / 85.42% / 23.93%`，最大回撤为 `-36.38% / -22.44% / -20.02% / -20.00% / -8.15%`。结论：2020 有恢复但 2023 未达 `40%`，2017 回撤偏深，不能替换 Path2 window winner 或 robust。
- `path2_candidate_pass.py` 后 Path2 window winners 与 robust 未切换；robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=64.36%`、`minCAGR=36.67%`。本轮未触发 Path2 evict。
- 最终 guard 将下一轮 focus 推到 `underrepresented_families`。下一轮第一条命令应暂停 high-growth v 系列，转向低相关代表：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm,core_explore_70_30_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_value_lowvol_industry_signal_cashguard_reconfirm`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-06 16:17 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 904/904 complete`；`scripts/path2_candidate_pass.py` 重建 comparable universe 到 `904`。上一轮 v21 继续牺牲 2020/2023，本轮按 `medium_cycle_growth` 将 high-growth v 系列恢复到 `risk26/mom_exit46/reconfirm96/caution56/cap28`，用等权与总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path2 `high_growth_theme` 候选：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore`。命令类型为五窗口 `--only-base-ids` 增量确认，A股实际合并命令见 Path1 本轮记录。
- v22 等权版五窗口 CAGR 为 `14.41% / 21.58% / 44.12% / 88.47% / 24.50%`，最大回撤为 `-28.16% / -20.65% / -23.18% / -15.71% / -8.62%`，Sharpe 为 `0.69 / 0.89 / 1.19 / 1.56 / 1.24`，换手为 `3.69x / 3.89x / 4.09x / 6.56x / 6.86x`；总市值版 CAGR 为 `12.61% / 16.08% / 43.64% / 90.20% / 33.47%`，最大回撤为 `-30.37% / -28.70% / -24.52% / -15.73% / -5.85%`。
- 结论：2023 重新超过 `40%`，但 2020 与长窗仍低于现有 winner/robust，Path2 robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，不改 tracked/live/public。候选池未触发 Path2 evict，`high_growth_theme` 仍显著压重。
- 最终 guard 将下一轮 focus 推到 `risk_reconfirm_sensitivity`。下一轮第一条命令建议继续在 v22 邻域测试恢复确认和风险阈值敏感性，但不要只扩 high-growth 单一族：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap30_cost_guard_v23_risk_reconfirm`；若未注册，先注册，并同步保留一个非 high-growth 低相关候选作为备选。

## 本轮执行计划（2026-06-06 10:28 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 898/898 complete`；`scripts/path2_candidate_pass.py` 刷新 comparable universe 到 `898`，robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=64.36%`、`minCAGR=36.67%`。上一轮 v20 继续牺牲 2020/2023；本轮按 `capacity_and_cost_stress` 确认更强恢复确认、更低 cap 的 v21 双底座。
- 本轮新增并五窗口确认 2 个 Path2 `high_growth_theme` 候选：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution52_cap22_cost_guard_v21`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution52_cap22_cost_guard_v21`。命令类型为五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path1 本轮记录。
- v21 等权版五窗口 CAGR 为 `16.86% / 14.95% / 22.69% / 65.76% / 23.31%`，最大回撤为 `-23.06% / -17.57% / -11.24% / -9.86% / -8.36%`，换手为 `3.51x / 3.66x / 3.51x / 7.66x / 7.34x`；总市值版为 `12.71% / 15.48% / 29.16% / 86.45% / 25.82%`，最大回撤为 `-25.53% / -21.54% / -9.77% / -6.96% / -6.76%`，换手为 `3.46x / 3.60x / 3.58x / 7.52x / 7.67x`。结论：短窗回撤改善但 2020/2023 收益仍低于当前 winner 和目标线，不替换 winner/robust。
- 本轮未触发 Path2 evict；`high_growth_theme=359`，候选池继续被该族压重。最终 guard 将下一轮 focus 轮到 `medium_cycle_growth`，下一轮第一条命令建议从 v21 退回中周期收益修复，而不是继续单纯降 risk/cap：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v22_growth_restore`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-06 04:23 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 893/893 complete`；`scripts/path2_candidate_pass.py` 已刷新 comparable universe 到 `893`。上一轮双周 `cap60` 对照仍无法修复 2017/2020，本轮按 `risk_reconfirm_sensitivity` 的后续设计确认 high-growth v20，但 Path2 window winner 与 robust candidate 均未切换。
- 本轮新增并五窗口确认 2 个 Path2 `high_growth_theme` v20 候选：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution54_cap24_cost_guard_v20`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution54_cap24_cost_guard_v20`。命令类型为五窗口 `--only-base-ids` 增量确认，等效命令为：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution54_cap24_cost_guard_v20,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution54_cap24_cost_guard_v20`。
- v20 等权版五窗口 CAGR 为 `11.06% / 13.74% / 20.88% / 69.72% / 1.56%`，最大回撤为 `-27.46% / -19.62% / -15.76% / -16.03% / -10.20%`；总市值版为 `7.35% / 8.76% / 18.86% / 72.03% / 7.40%`，最大回撤为 `-27.61% / -30.93% / -13.25% / -14.36% / -9.40%`。结论：继续降低 `risk/cap/exit` 已明显牺牲 2020/2023，不替换 winner/robust。
- 本轮未触发 Path2 evict。最终 rotation focus 为 `underrepresented_families`，下一轮第一条命令建议暂停 high-growth v 系列，先注册并确认低相关多因子/防守混合候选：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_industry_cost_guard_reconfirm,core_explore_70_30_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_lowvol_industry_cost_guard_reconfirm`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-05 22:21 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 888/888 complete`；`scripts/path2_candidate_pass.py` 已刷新 comparable universe 到 `888`。本轮 Path2 window winner 与 robust candidate 未被双周成本守门候选替换，robust 仍为既有 liqmom/high-growth 族。
- 本轮按上一轮 `underrepresented/capacity` 提示五窗口确认 2 个 Path2 `biweekly_rebalance_aggressive` 候选：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`。命令为：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`。
- 80/20 等权版五窗口 CAGR 为 `2.80% / 9.78% / 25.61% / 65.13% / 52.98%`，最大回撤 `-65.30% / -57.27% / -31.01% / -26.92% / -14.00%`，换手 `4.46x / 4.69x / 4.93x / 9.25x / 11.63x`；70/30 等权版为 `3.46% / 10.09% / 22.05% / 64.01% / 53.57%`，最大回撤 `-57.58% / -52.09% / -28.90% / -21.56% / -12.75%`，换手 `4.92x / 5.30x / 6.08x / 11.63x / 12.67x`。结论：该低相关双周线继续不能修复 2017/2020，短窗换手也偏高，只作为失败对照。
- 本轮未触发 Path2 evict。最终 rotation focus 为 `risk_reconfirm_sensitivity`，下一轮第一条命令建议回到 high-growth v 系列做恢复确认/风险阈值敏感性，而不是继续扩双周弱线：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit50_reconfirm94_caution58_cap32_cost_guard_v20,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit50_reconfirm94_caution58_cap32_cost_guard_v20`；若未注册，先注册后再跑。

## 本轮执行计划（2026-06-05 10:22 CST）

- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 883/883 complete`；`scripts/path2_candidate_pass.py` 更新 comparable universe 到 `883`。本轮 Path2 window winner 与 robust candidate 未被 v19 替换，robust 仍为既有 liqmom/high-growth 族。
- 本轮新增并五窗口确认 2 个 Path2 `high_growth_theme` v19 候选：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19`。命令类型为五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path1 本轮记录。
- v19 等权版五窗口 CAGR 为 `14.41% / 21.58% / 44.12% / 88.47% / 24.50%`，最大回撤 `-28.16% / -20.65% / -23.18% / -15.71% / -8.62%`；总市值版为 `12.61% / 16.08% / 43.64% / 90.20% / 33.47%`，最大回撤 `-30.37% / -28.70% / -24.52% / -15.73% / -5.85%`。结论：2023 已超过 `40%`，但 2020 仍低于 Path2 目标和当前 winner，且长窗不强，不晋级。
- `path2_candidate_pass.py` 当前窗口 winners：2017 `...risk35_mom_exit55_reconfirm82_caution70_cap70_cost_guard_v5`、2020 `...risk40_mom_exit60_reconfirm70_cap95`、2023 `...risk50_or_cap95`、2025 `...cash_off_and_cap100_weekly`；robust 仍为 `...risk40_mom_exit60_reconfirm75_cap95`。本轮未触发 Path2 evict；若继续扩池，优先归档最近多轮未改善 2020/2023 的同形 low-return 多因子和 v18/v19 短窗弹性失败线。
- 最新 rotation focus 为 `underrepresented_families`。下一轮第一条命令建议先补非 high-growth 代表，而不是继续 v20：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`；若预算只能跑 1 组，优先 80/20 等权底座。

## 本轮执行计划（2026-06-05 04:11 CST）

- 最新 guard 为 `pass`，`ashare_path2_candidate_universe 877/877 complete`；`scripts/path2_candidate_pass.py` 已重建 comparable universe。Path2 window winner 与 robust candidate 未被本轮 v18 替换，robust 仍为既有 liqmom/high-growth 族。
- 本轮纳入并确认 2 个 Path2 `high_growth_theme` v18 候选：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap32_cost_guard_v18`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap32_cost_guard_v18`。命令类型为五窗口 `--only-base-ids` 增量确认。
- v18 等权版五窗口 CAGR 为 `13.17% / 25.41% / 30.18% / 81.16% / 16.15%`，总市值版为 `12.13% / 22.43% / 29.20% / 83.51% / 23.67%`；两者 2020/2023 都低于当前 Path2 winner，且长窗回撤仍偏深，不晋级。
- 本轮 `emergent_theme_discovery` family 的 family-ranked 第一名变为 `core_explore_90_10_equal_weight_winner_core__aggr_13_87_prom12_emergent_theme_quality_gate_signal26_leader72_coverage_penalty_risk15_cap12_exit66`，但这属于 Path4 横向观察，不改写 Path2 official winner。最新 rotation focus 为 `risk_reconfirm_sensitivity`；下一轮第一条命令建议在 v18 邻域提高恢复确认并继续降单票幸运：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution56_cap28_cost_guard_v19`；若未注册，先注册后再跑。
- 本轮未触发 Path2 active cap evict；若下一轮新增前池继续膨胀，优先归档最近三轮未改善 2020/2023 的同形 low-return multifactor 对照。

## 本轮执行计划（2026-06-04 16:16 CST）

- 开局 guard 为 `pass`，本轮 Path2 没有新增独立回测 id；预算优先给 Path1 holding shape、Path3 纯周度降换手、Path4 强主题信号质量和 HK Path5。`scripts/path2_candidate_pass.py` 已重新巡检，comparable universe 更新到 `872`，其中新增比较信息主要来自 Path4 `emergent_theme_discovery` family。
- 本轮复核结论：Path2 window winners 与 robust candidate 均未切换；robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。本轮不把 Path1 `share_16_84` 或 Path3 `_weekly` 结果并入 Path2 结论。
- 下一轮 focus 由 guard 给出 `capacity_and_cost_stress`，且当前 family 仍被 high-growth/liqmom 压得较重。下一轮第一条命令继续补前序未跑的双周 capacity/cost 对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`。
- 本轮未触发 Path2 active cap evict。若下一轮新增前 candidate pool 继续膨胀，先归档最近三轮未改善 2020/2023 且同形的 low-return multifactor 对照，再注册新的 `capacity_and_cost_stress` id。

## 本轮执行计划（2026-06-04 10:16 CST）

- 开局 guard 为 `pass`，上一轮未跑的 underrepresented/capacity 对照仍需要推进。本轮先把 `aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm` 加入 `PATH2_SCAN_VARIANT_IDS`，随后用 80/20 与 90/10 等权底座五窗口确认，避免 Path2 universe 继续只被 high-growth/liqmom 族压扁。
- 本轮新增并确认 2 个 Path2 低相关多因子候选：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm`、`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm`。实际命令见 Path1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 两个候选的五窗口 CAGR 分别为 `15.27% / 14.85% / 28.12% / 53.58% / 58.78%` 与 `15.01% / 14.70% / 25.98% / 63.12% / 48.89%`；回撤相对 high-growth 族更温和，但 2020/2023 收益明显低于 Path2 winner，作为低相关失败对照记录，不晋级。
- `scripts/path2_candidate_pass.py` 后 comparable universe 更新为 `868`，robust 仍为既有 liqmom/high-growth 确认族；`scripts/update_weighted_winners.py` 后 Path2 window winner、robust candidate 和 tracked payload 未切换，本轮未触发 evict。
- 下一轮 focus 仍是 `underrepresented_families`，但不要继续扩低收益多因子。第一条命令建议补回上一轮未跑的双周 capacity/cost 对照：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`。

## 本轮执行计划（2026-06-03 22:20 CST）

- 开局 guard 的 Path2 coverage 为 `860/860 complete`；本轮没有追加 Path2 回测预算，原因是 coverage 补缺口已经占用 Path4 三底座五窗口与 Path1 fast-family，HK 还需完成六个增量 id。`scripts/path2_candidate_pass.py` 已巡检并更新 family ranking，当前 comparable universe 为 `862`，robust 仍集中在既有 liqmom 高收益族。
- 本轮候选设计分两层：`recommended_focus=medium_cycle_growth` 映射到下一批 high-growth 修复池，目标是提高 promoted count 并降低单票幸运；同时保留已注册但未回测的 `biweekly_rebalance_aggressive` 成本容量候选 `aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`，用于补足非 high-growth 族代表。
- 未回测候选 id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`。下一轮若先补 underrepresented/capacity 对照，第一条命令为：`.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly_cost_guard`。
- `scripts/update_weighted_winners.py` 后 Path2 window winner、robust candidate 与 tracked payload 未被本轮同步改变；最新 robust candidate 仍为既有 high-growth/liqmom 族，Path2 未触发 evict。下一轮若严格响应 `medium_cycle_growth`，应先注册一个分散化 v18 双底座，而不是继续降低 cap 牺牲 2020 收益。

## 本轮执行计划（2026-06-02 16:20 CST）

- 开局 guard 为 `pass`；上一轮双周 `cap65 + cost_guard` 代表没有修复 2017/2020，最终 rotation 回到 `medium_cycle_growth`。本轮重启 high-growth 中周期族，但把 v13 的 `risk32/exit52/reconfirm88/caution62/cap50` 改为更强确认和更低集中度的 `top12/risk30/exit50/reconfirm90/caution60/cap45` v14，用等权与总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm90_caution60_cap45_cost_guard_v14`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm90_caution60_cap45_cost_guard_v14`。增量确认命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm90_caution60_cap45_cost_guard_v14,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm90_caution60_cap45_cost_guard_v14,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold6_turn08_exit90_weekly`。
- v14 等权版五窗口 CAGR 为 `26.77% / 36.22% / 40.03% / 131.34% / 13.20%`，最大回撤为 `-37.00% / -21.23% / -19.25% / -20.88% / -9.38%`，换手为 `3.35x / 4.12x / 4.61x / 7.91x / 6.41x`；总市值版为 `24.61% / 30.89% / 35.92% / 139.93% / 20.62%`，最大回撤为 `-37.97% / -24.32% / -19.12% / -21.08% / -6.43%`。等权版把 2023 重新推过 `40%`，但 2020 仍未达 `40%`，且最新持仓高度集中于源杰科技/腾景科技，存在单票幸运与容量风险，不晋级。
- `scripts/path2_candidate_pass.py` 后 Path 2 comparable universe 为 `843`，`high_growth_theme=343`、`weekly_rebalance_aggressive=82`、`emergent_theme_discovery=60`。`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked 未被 v14 替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict。
- 最新 guard 为 `pass`，下一轮 focus 为 `medium_cycle_growth`。第一条命令建议继续在 v14 邻域做“降单票幸运”的中周期修复，例如提高 promoted count 或加入行业/流动性分散，而不是继续降低 cap 到牺牲 2020：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_growth_ids>`。

## 本轮执行计划（2026-06-02 13:49 CST）

- 开局 guard 为 `pass`；上一轮 v13 high-growth 没把 2020 拉到 `40%`，且最终 focus 指向 `underrepresented_families`。本轮暂停 high-growth v 系列，新增 `biweekly_rebalance_aggressive` 的 `cap65 + cost_guard` 代表，用 80/20 与 70/30 等权双底座确认，避免 Path 2 候选池继续被单一 high-growth family 压扁。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap65_biweekly_cost_guard`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap65_biweekly_cost_guard`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 80/20 等权版五窗口 CAGR 为 `3.09% / 10.27% / 26.73% / 67.41% / 61.98%`，最大回撤为 `-65.45% / -57.61% / -31.01% / -26.92% / -14.18%`，换手为 `4.46x / 4.69x / 4.93x / 9.23x / 11.51x`；70/30 等权版为 `3.78% / 10.72% / 23.53% / 67.59% / 64.20%`，最大回撤为 `-57.93% / -52.58% / -28.90% / -21.38% / -12.95%`，换手为 `4.92x / 5.30x / 6.08x / 11.61x / 12.56x`。双周低相关线没有修复 2017/2020，短窗换手也偏高，不晋级。
- `scripts/path2_candidate_pass.py` 后 Path 2 comparable universe 为 `837/837 complete`，其中 `biweekly_rebalance_aggressive=25`、`decorrelated_defensive_mix=27`、`high_growth_theme=343`。`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict。
- 最终 guard 下一轮 focus 为 `capacity_and_cost_stress`。第一条命令建议不要继续扩双周弱线，回到 high-growth robust 邻域做容量/成本压力，优先用更低 cap 或更严恢复确认测试 2017/2020 回撤：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-06-02 04:20 CST）

- 开局 guard 为 `pass`；上一轮 high-growth v12 修复短窗但 2020 未达 `40%`。本轮按开局 `risk_reconfirm_sensitivity` 继续在中周期 high-growth 族做 v13，把 v12 的 `risk34/exit52/reconfirm86/caution64/cap48` 调成 `risk32/exit52/reconfirm88/caution62/cap50`，用等权与总市值双底座确认；最终 guard 下一轮 focus 轮换为 `underrepresented_families`。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm88_caution62_cap50_cost_guard_v13`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm88_caution62_cap50_cost_guard_v13`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- v13 等权版五窗口 CAGR 为 `28.34% / 33.15% / 39.27% / 124.30% / 11.78%`，最大回撤为 `-40.30% / -29.39% / -26.99% / -21.30% / -9.62%`，换手为 `3.52x / 4.31x / 4.53x / 7.83x / 6.18x`；总市值版为 `26.19% / 28.70% / 34.91% / 132.96% / 18.32%`，最大回撤为 `-40.03% / -30.17% / -26.71% / -21.76% / -6.93%`。v13 没有把 2020 拉到 `40%`，且 2017 回撤仍深，不晋级。
- `scripts/path2_candidate_pass.py` 后 Path 2 comparable universe 为 `831/831 complete`，high-growth family 已到 `343`；`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked 未被 v13 替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict。
- 下一轮 focus 为 `underrepresented_families`。第一条命令建议暂停 high-growth v 系列，补一个低相关/非单一 high-growth 的代表，例如 momentum equal-weight elastic、decorrelated defensive mix 或 biweekly 对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-06-01 22:30 CST）

- 开局 guard 为 `pass`；上一轮低相关多因子对照只提供 2026 弹性，不能替换 high-growth winner。本轮按 `medium_cycle_growth` 回到中周期高收益族，把 v11 的 `top12/risk36/exit54/reconfirm84/caution66/cap50` 改成更浅风险和更低 cap 的 `risk34/exit52/reconfirm86/caution64/cap48` v12，用等权与总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk34_mom_exit52_reconfirm86_caution64_cap48_cost_guard_v12`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk34_mom_exit52_reconfirm86_caution64_cap48_cost_guard_v12`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `21.14% / 38.78% / 41.59% / 138.87% / 8.06%`，最大回撤为 `-42.86% / -23.33% / -28.39% / -16.24% / -9.53%`，换手为 `3.65x / 4.29x / 4.79x / 7.92x / 7.61x`；总市值版为 `18.61% / 33.92% / 37.34% / 148.69% / 19.58%`，最大回撤为 `-48.93% / -24.24% / -28.12% / -15.92% / -6.73%`。v12 修复了 2025/2026 弹性，但 2017 过弱且 2020 未达 `40%`，不晋级。
- `scripts/path2_candidate_pass.py` 后 Path 2 comparable universe 为 `826/826 complete`，high-growth family 为 `341`；`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked 未被 v12 替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict。
- 最终 guard 把下一轮 focus 轮换为 `risk_reconfirm_sensitivity`。v12 说明单纯压 cap 会牺牲长窗，第一条命令建议在 v12 邻域改测更强 2020 恢复确认或更浅 risk-off，而不是继续下调单票上限：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-06-01 10:27 CST）

- 开局 guard 为 `pass`；上一轮 high-growth v10 保住 2023 高收益但 2020/2026 弱、回撤深。本轮按 `underrepresented_families` 暂停 high-growth v 系列，使用已有多因子质量+估值+趋势+成本守门变体放到 `80/20 equal_weight` 底座，作为低相关防守/多因子对照。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_trend_cost_guard_reconfirm`。
- 该候选五窗口 CAGR 为 `14.11% / 15.77% / 32.95% / 63.17% / 103.03%`，最大回撤为 `-35.11% / -30.15% / -21.63% / -15.34% / -13.55%`，换手为 `2.99x / 3.31x / 3.61x / 5.75x / 6.73x`。它验证了低相关多因子可以给 2026 正弹性，但 2020/2023 仍明显低于 high-growth winner，不晋级。
- `scripts/path2_candidate_pass.py` 后 Path 2 comparable universe 为 `815`，`decorrelated_defensive_mix=26`、`weekly_rebalance_aggressive=77`、`emergent_theme_discovery=60`；`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict。
- 下一轮 focus 为 `capacity_and_cost_stress`。第一条命令建议回到 high-growth robust 邻域做容量/成本压力，而不是继续扩弱多因子；候选池可先补 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk36_mom_exit54_reconfirm84_caution66_cap50_cost_guard_v11` 与总市值对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-06-01 04:18 CST）

- 开局 guard 为 `pass`；上一轮 high-growth v9 把 2023 拉回 `40%+` 但 2020 和 2026 仍弱。本轮按 `risk_reconfirm_sensitivity` 继续在中周期高收益族做 v10，扩大到 `risk36/exit54/reconfirm84/caution64/cap55`，用等权与总市值双底座确认是否能保留 2023 强度并修复 2026。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk36_mom_exit54_reconfirm84_caution64_cap55_cost_guard_v10`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk36_mom_exit54_reconfirm84_caution64_cap55_cost_guard_v10`。与 Path 3 合并增量命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk36_mom_exit54_reconfirm84_caution64_cap55_cost_guard_v10,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk36_mom_exit54_reconfirm84_caution64_cap55_cost_guard_v10,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap64_hold8_turn03_exit94_weekly`。
- 等权版五窗口 CAGR 为 `27.34% / 26.71% / 46.71% / 60.59% / 5.33%`，最大回撤为 `-38.71% / -43.29% / -26.91% / -19.78% / -9.86%`，换手为 `3.69x / 4.42x / 4.62x / 8.36x / 7.29x`；总市值版为 `24.94% / 22.31% / 42.01% / 68.45% / 13.68%`，最大回撤为 `-39.25% / -43.14% / -28.32% / -19.87% / -7.44%`。v10 保住 2023 高收益，但 2020 未达 `40%`、回撤过深且 2026 偏弱，不晋级。
- `scripts/path2_candidate_pass.py` 后 comparable universe 完整，guard 口径 `ashare_path2_candidate_universe 806/806 complete`；`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked 未被 v10 替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict。
- 下一轮 focus 为 `underrepresented_families`。第一条命令建议暂停 high-growth v 系列，补一个低相关防守/双周或多因子代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_signal_reconfirm` 或低换手 biweekly 对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-31 22:26 CST）

- 开局 guard 为 `pass`；上一轮 `90/10 quality-defense cashguard` 在 2020/2023 明显弱，本轮按 `medium_cycle_growth` 回到 high-growth 中周期高收益族，新增 `top10/risk34/exit54/reconfirm86/caution62/cap58` v9 双底座，目标是恢复 v7 的 2023 强度并观察 2026 是否可接受。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk34_mom_exit54_reconfirm86_caution62_cap58_cost_guard_v9`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk34_mom_exit54_reconfirm86_caution62_cap58_cost_guard_v9`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk34_mom_exit54_reconfirm86_caution62_cap58_cost_guard_v9,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk34_mom_exit54_reconfirm86_caution62_cap58_cost_guard_v9,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap64_hold8_turn03_exit90_weekly`。
- 等权版五窗口 CAGR 为 `24.52% / 30.66% / 42.79% / 68.41% / 2.94%`，最大回撤为 `-39.80% / -42.96% / -27.88% / -15.11% / -10.01%`，换手为 `3.65x / 4.44x / 4.36x / 8.36x / 7.10x`；总市值版为 `21.99% / 25.77% / 38.06% / 75.69% / 11.38%`，最大回撤为 `-41.66% / -43.15% / -30.62% / -17.16% / -7.74%`。v9 等权把 2023 拉回 `40%+`，但 2020 未到 `40%` 且长窗回撤仍过深，2026 太弱，不晋级。
- `scripts/path2_candidate_pass.py` 后 Path 2 universe 为 `806`；`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust 未变化，official robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict，但 v9 说明 high-growth 族仍有 2023 弹性、风险控制仍未解决。
- 下一轮 focus 建议转向 `capacity_and_cost_stress` 或 `risk_reconfirm_sensitivity`，第一条命令不要扩大 top10 高集中度，而是测试更低单票/更浅 risk-off 或 cashguard 组合：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_or_risk_id>`。

## 本轮执行计划（2026-05-31 16:20 CST）

- 开局 guard 为 `pass`；上一轮 high-growth v8 修复 2026 但牺牲 2023，上轮建议转向 `underrepresented_families`。本轮新增低相关多因子/防守代表，把既有 `quality_defense_cashguard_reconfirm` 放到 `90/10 equal_weight` 底座上，验证是否能比 80/20 等权版改善中窗。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm`。
- 该候选五窗口 CAGR 为 `17.91% / 11.35% / 16.08% / 73.82% / 85.54%`，最大回撤为 `-24.71% / -27.56% / -20.95% / -16.20% / -11.37%`，换手为 `2.93x / 3.36x / 3.90x / 5.76x / 7.21x`。它相对 80/20 等权版改善 2017，但 2020/2023 仍远低于 high-growth winner，不晋级。
- `scripts/path2_candidate_pass.py` 后 comparable universe 为 `799`；`scripts/update_weighted_winners.py` 后 Path 2 window winner 和 robust/tracked 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict，但结果确认低相关质量防守线只能作为失败对照，不能继续扩大量。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `capacity_and_cost_stress`。第一条命令建议回到现有 high-growth robust 邻域做容量/成本压力，而不是继续增加弱多因子：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-31 10:26 CST）

- 开局 guard 为 `pass`；上一轮 focus 为 `risk_reconfirm_sensitivity`，本轮在 high-growth 中周期高收益族做更低 `risk32/exit52/reconfirm88/caution60/cap55` 的 v8 双底座复核，目标是修复 2026 并观察 2023 是否还能留在高收益区间。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk32_mom_exit52_reconfirm88_caution60_cap55_cost_guard_v8`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk32_mom_exit52_reconfirm88_caution60_cap55_cost_guard_v8`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `18.89% / 30.62% / 20.85% / 64.91% / 10.64%`，最大回撤为 `-43.24% / -33.68% / -27.84% / -14.86% / -9.86%`，换手为 `3.68x / 4.37x / 4.39x / 8.62x / 5.94x`；总市值版为 `16.54% / 26.38% / 19.03% / 71.93% / 16.38%`，最大回撤为 `-45.01% / -33.22% / -26.12% / -16.49% / -7.44%`。v8 修复了 2026 正收益，但 2023 从 v7 的 `44%+ / 49%+` 降到约 `19%-21%`，不晋级。
- 新增后将 v7 从 active high-growth 扫描池移出，理由是 v8 覆盖了更严 `top10/reconfirm88/cap55` 复核且 v7 未改善 robust；历史结果保留。`scripts/path2_candidate_pass.py` 后 Path 2 comparable universe 为 `795`，high-growth family 为 `333`，window winner 与 official robust 未被 v8 替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `underrepresented_families`。第一条命令建议暂停继续压 high-growth cap，补一个低相关防守/多因子或双周代表，目标先把 2020/2023 稳定性拉回而不是追逐 2026：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-31 04:21 CST）

- 开局 guard 为 `pass`；上一轮 focus 指向 `capacity_and_cost_stress`，本轮继续在 high-growth 中周期高收益族压集中度，把 `top12/reconfirm85/caution65/cap60` 作为 v7，并用等权与总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution65_cap60_cost_guard_v7`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution65_cap60_cost_guard_v7`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution65_cap60_cost_guard_v7,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution65_cap60_cost_guard_v7`。
- 等权版五窗口 CAGR 为 `20.02% / 35.37% / 49.79% / 134.76% / 1.46%`，最大回撤为 `-43.39% / -32.84% / -25.85% / -16.42% / -10.11%`，换手为 `3.61x / 4.28x / 4.29x / 7.75x / 7.07x`；总市值版为 `18.87% / 30.24% / 44.13% / 145.06% / 9.59%`，最大回撤为 `-48.19% / -34.75% / -25.78% / -17.17% / -7.95%`，换手为 `3.63x / 4.20x / 4.20x / 7.34x / 7.06x`。v7 修复总市值 2026，但 2017/2020 回撤仍过深，未替换 Path 2 winner/robust。
- 新增后将 `aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution70_cap65_cost_guard_v6` 从 active high-growth 扫描池移出，原因是 v6 已被 v7 的更低 `caution65/cap60` 约束覆盖且未改善 robust。`scripts/path2_candidate_pass.py` 后 Path 2 comparable universe 为 `790/790 complete`，high-growth family 为 `333`，robust/tracked 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `risk_reconfirm_sensitivity`。第一条命令建议不要继续单纯降 cap，改测更低 risk/更严恢复确认对 2026 与 2023 的折中，例如双底座 `aggr_02_98_prom2_core_6_1_promo_liqmom_top10_risk32_mom_exit52_reconfirm88_caution60_cap55_cost_guard_v8`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-30 22:20 CST）

- 开局 guard 为 `pass`；上一轮要求从 `underrepresented_families` 补低相关/多因子代表。本轮新增等权 `quality_growth_signal_reconfirm`，用质量、成长加速度、行业强度与流动性放量组合做非 high-growth 对照。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- `quality_growth_signal_reconfirm` 五窗口 CAGR 为 `14.01% / 16.84% / 33.70% / 72.00% / 107.53%`，最大回撤为 `-35.93% / -28.30% / -21.77% / -14.65% / -13.55%`，换手为 `3.01x / 3.27x / 3.55x / 5.87x / 6.71x`。它能给 2023+ 弹性，但 2017/2020 收益和回撤均低于当前 Path 2 robust，不晋级。
- `scripts/path2_candidate_pass.py` 后 Path 2 candidate universe 为 `786/786 complete`；四窗口 winner 仍为既有 high-growth/liqmom 族，robust/tracked 未被本轮候选替换，`scripts/update_weighted_winners.py` 口径 Path 2 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。本轮未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `capacity_and_cost_stress`。第一条命令建议回到当前 high-growth robust 邻域做容量/成本压力，而不是继续补弱多因子，例如双底座 `aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution65_cap60_cost_guard_v7`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-30 16:22 CST）

- 开局 guard 为 `pass`；上一轮 v5 证明 `caution70/cap70` 仍不能修复 2026 等权负收益。本轮按 `medium_cycle_growth/risk_reconfirm_sensitivity` 把 high-growth 族改为 `top12/reconfirm85/cap65`，继续用等权和总市值双底座五窗口确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution70_cap65_cost_guard_v6`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution70_cap65_cost_guard_v6`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution70_cap65_cost_guard_v6,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution70_cap65_cost_guard_v6`。
- 等权版五窗口 CAGR 为 `20.56% / 35.61% / 51.02% / 132.43% / -1.65%`，最大回撤为 `-44.23% / -33.98% / -26.56% / -16.57% / -11.06%`，换手为 `3.63x / 4.32x / 4.28x / 7.77x / 6.94x`；总市值版为 `19.37% / 30.37% / 44.76% / 143.34% / 5.36%`，最大回撤 `-48.73% / -35.63% / -26.51% / -18.57% / -8.62%`。v6 保留 2023/2025 上限并让总市值 2026 转正，但 2017/2020 回撤过深，未替换 Path 2 winner/robust。
- 新增后把上一轮 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution70_cap70_cost_guard_v5` 从 active scan 池移出，原因是 v5 的 2026 等权仍为负且已被 v6 的更低 `top12/cap65` 覆盖；历史结果保留为失败对照。`scripts/path2_candidate_pass.py` 后 Path 2 robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`，window winners 未被 v6 替换。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 782/782 complete`，下一轮 focus 轮换为 `underrepresented_families`。第一条命令建议暂停 high-growth 邻域，补一个低相关防守/多因子代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_growth_signal_reconfirm` 或双周低回撤对照：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-30 10:17 CST）

- 开局 guard 为 `pass`；上一轮 high-growth v4 修复 2017/2023 但 2026 仍为负。本轮按 `capacity_and_cost_stress` 继续在同一中周期高收益族做容量/成本压力，把谨慎仓从 `75%` 降到 `70%`、单票上限从 `75%` 降到 `70%`，使用等权与总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution70_cap70_cost_guard_v5`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution70_cap70_cost_guard_v5`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution70_cap70_cost_guard_v5,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution70_cap70_cost_guard_v5`。
- 等权版五窗口 CAGR 为 `37.53% / 30.73% / 46.50% / 139.34% / -3.45%`，最大回撤为 `-24.58% / -35.29% / -32.32% / -22.19% / -12.02%`，换手为 `3.82x / 4.18x / 4.25x / 7.68x / 6.70x`；总市值版为 `34.28% / 25.90% / 40.88% / 153.79% / 1.20%`，最大回撤为 `-25.90% / -34.76% / -32.28% / -24.18% / -9.93%`，换手为 `3.87x / 4.08x / 4.18x / 7.21x / 6.69x`。v5 保留 2017/2023/2025 上限，但等权 2026 仍为负、2020 弱于现有 high-growth winner，不晋级。
- 新增前将上一轮 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution75_cap75_cost_guard_v4` 从 active high-growth scan 池移出，原因是 v4 的 2026 两底座均为负且已被 v5 的更低容量约束覆盖；历史结果保留为失败对照。`scripts/path2_candidate_pass.py` 后 comparable universe 为 `776/776 complete`，`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust/tracked 未变，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `medium_cycle_growth`。第一条命令建议停止只压 cap，转测更低集中度且保留 2026 正收益的中周期高收益对照，例如 `aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk35_mom_exit55_reconfirm85_caution70_cap65_cost_guard_v6` 双底座：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-30 04:31 CST）

- 开局 guard 为 `pass`；上一轮 `risk35/exit58/reconfirm80/cap80_cost_guard_v3` 保留 2023 上限但 2026 转负。本轮按上一轮 focus 的中周期高收益修复线，把退出收紧到 `exit55`、恢复确认升到 `reconfirm82`，加入 `caution75/cap75`，继续用等权与总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution75_cap75_cost_guard_v4`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution75_cap75_cost_guard_v4`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution75_cap75_cost_guard_v4,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution75_cap75_cost_guard_v4`。
- 等权版五窗口 CAGR 为 `38.42% / 31.57% / 47.63% / 136.88% / -6.75%`，最大回撤为 `-25.11% / -35.36% / -33.03% / -23.36% / -12.97%`，换手为 `3.84x / 4.21x / 4.25x / 7.71x / 6.57x`；总市值版为 `35.03% / 26.40% / 41.55% / 151.93% / -3.17%`，最大回撤为 `-26.45% / -34.90% / -33.01% / -25.48% / -11.24%`。v4 修复了 2017/2023 上限，但 2026 仍为负，不替换 robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `770`，`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust/tracked 未变，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 为 `underrepresented_families`。第一条命令建议暂停 high-growth 邻域，注册一个低相关防守/多因子代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_value_defense_reconfirm`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-29 22:21 CST）

- 开局 guard 为 `pass`；上一轮 `risk40/reconfirm75/cap80_cost_guard_v2` 修复了 2026，但 2020/2023 仍低于 high-growth winner。本轮按 `risk_reconfirm_sensitivity` 把风险阈值降到 `risk35`、出场调到 `exit58`、恢复调到 `reconfirm80`，继续用等权与总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit58_reconfirm80_cap80_cost_guard_v3`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit58_reconfirm80_cap80_cost_guard_v3`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit58_reconfirm80_cap80_cost_guard_v3,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit58_reconfirm80_cap80_cost_guard_v3`。
- 等权版五窗口 CAGR 为 `33.87% / 33.13% / 48.43% / 94.53% / -8.82%`，最大回撤为 `-31.11% / -31.29% / -32.24% / -23.19% / -13.92%`，换手为 `3.62x / 4.16x / 4.22x / 7.52x / 6.22x`；总市值版为 `30.48% / 27.16% / 41.92% / 108.41% / -4.81%`，最大回撤为 `-30.94% / -32.57% / -32.21% / -25.42% / -12.54%`。v3 保留 2017/2023 上限，但 2026 转负且持仓仍高度集中，不替换 winner/robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `765`，`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust/tracked 未变，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 继续 `medium_cycle_growth`。第一条命令建议不要继续只降 risk，改做中周期高收益的 2026 修复：注册 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm82_caution75_cap75_cost_guard_v4` 的等权/总市值双底座，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-29 16:33 CST）

- 开局 guard 为 Path 4 blocking、Path 1 warning；补齐后按上一轮 `capacity_and_cost_stress` 继续只用增量 `--only-base-ids`。上一轮 `quality_defense_cashguard_reconfirm` 证明防守多因子能给 2026 弹性但 2020/2023 太弱；本轮回到 high-growth robust 邻域，把 `cap95` 降到 `cap80` 并加成本守门 v2，分别用等权和总市值底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard_v2`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard_v2`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard_v2,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard_v2`。
- 等权版五窗口 CAGR 为 `32.71% / 39.98% / 48.67% / 77.78% / 45.26%`，最大回撤为 `-33.32% / -29.20% / -32.23% / -23.19% / -13.92%`，换手为 `3.64x / 4.08x / 4.17x / 7.24x / 6.22x`；总市值版为 `30.00% / 33.89% / 40.71% / 91.37% / 49.77%`，最大回撤为 `-33.16% / -29.99% / -32.27% / -25.42% / -12.54%`。v2 明显修复 2026，但 2020/2023 与现有 high-growth winner/robust 仍有差距。
- `scripts/path2_candidate_pass.py` 后 candidate universe 完整，最终 guard 口径 `ashare_path2_candidate_universe 753/753 complete`；raw robust 表仍偏向 high-growth `cap95`，`scripts/update_weighted_winners.py` 的 official Path 2 robust/tracked 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 下一轮 focus 轮换为 `risk_reconfirm_sensitivity`。第一条命令建议不要继续只压 cap，改测试 `reconfirm80/risk35` 或更强恢复过滤对 2026 与 2023 的折中，例如等权/总市值 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit58_reconfirm80_cap80_cost_guard_v3`：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-29 10:22 CST）

- 开局 guard 为 `pass`；上一轮 top12/caution85/cap70 仍未修复 high-growth 的 2026 负收益，本轮按 `underrepresented_families` 暂停 high-growth 邻域，新增等权底座的多因子质量防守现金再确认，作为低相关防守/非 high-growth 对照。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm`。可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense_cashguard_reconfirm`。
- `quality_defense_cashguard_reconfirm` 五窗口 CAGR 为 `15.22% / 11.71% / 18.21% / 62.70% / 100.74%`，最大回撤为 `-26.98% / -25.31% / -16.65% / -15.38% / -13.55%`，换手为 `2.92x / 3.45x / 3.86x / 5.47x / 6.71x`。它给出 2026 正弹性和较浅回撤，但 2020/2023 收益远低于 Path 2 high-growth winner，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `753`，`decorrelated_defensive_mix` 与多因子族增加 1 个可比样本；`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `capacity_and_cost_stress`。第一条命令建议回到 robust 邻域做容量/成本压力，而不是继续新增弱多因子，例如等权/总市值 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard_v2` 或同等降低集中度版本：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-29 04:17 CST）

- 开局 guard 为 `pass`；上一轮 top15/cap60 仍未修复 2026 负收益与深回撤，本轮按 `risk_reconfirm_sensitivity` 不再单纯压 cap，改用 `top12 + reconfirm80 + caution85/cap70 + cashguard` 的中周期高收益对照，继续用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard`。
- 等权版五窗口 CAGR 为 `24.59% / 21.78% / 30.90% / 43.40% / -10.64%`，最大回撤为 `-50.67% / -40.79% / -32.04% / -24.73% / -13.55%`，换手为 `3.72x / 4.32x / 4.63x / 8.02x / 7.01x`；总市值版为 `24.02% / 17.57% / 22.03% / 51.92% / -5.11%`，最大回撤为 `-50.59% / -40.18% / -34.04% / -26.28% / -11.12%`。缩到 top12 后 2020/2023 大幅低于现有 high-growth winner，且 2026 仍为负，不晋级。
- `scripts/path2_candidate_pass.py` 输出 candidate universe 为 `748`；最终 guard 的 comparable coverage scope 为 `748/748 complete`。`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 轮换为 `underrepresented_families`。第一条命令建议暂停 high-growth 邻域，补一个低相关防守/双周代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_value_lowvol_cashguard_reconfirm` 或同等非 high-growth family，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-28 22:19 CST）

- 开局 guard 为 `pass`；上一轮 underrepresented 双周成本线收益/回撤都弱，本轮按 `medium_cycle_growth` 回到 high-growth 中周期族，把 `risk45/exit55/reconfirm75/caution85` 线的单票 cap 继续压到 `60`，检验是否能修复 2026 负收益和集中风险。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard`。
- 等权版五窗口 CAGR 为 `25.15% / 39.37% / 38.26% / 133.96% / -10.71%`，最大回撤为 `-52.66% / -35.96% / -33.25% / -11.51% / -12.51%`，换手为 `3.77x / 4.64x / 4.44x / 7.29x / 7.48x`；总市值版为 `24.74% / 35.09% / 31.02% / 145.57% / -3.36%`，最大回撤为 `-52.50% / -34.70% / -33.28% / -12.58% / -9.26%`，换手为 `3.78x / 4.57x / 4.43x / 6.90x / 7.53x`。降 cap 仍没有修复 2017 深回撤和 2026 负收益，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `743`，其中 `high_growth_theme=325`、`weekly_rebalance_aggressive=64`、`emergent_theme_discovery=59`；`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked payload 未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 743/743 complete`，下一轮 focus 仍为 `medium_cycle_growth`。第一条命令建议停止单纯压 cap，改在中周期高收益族上降低候选数或加入更强恢复过滤，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top12_risk45_mom_exit55_reconfirm80_caution85_cap70_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-28 16:18 CST）

- 开局 guard 为 `pass`；上一轮 high-growth `cap65` 仍未修复 2017 深回撤与 2026 负收益，本轮按 `underrepresented_families` 暂停 high-growth 邻域，补一个双周 rebalance + 成本守门的低相关代表。
- 本轮新增并五窗口确认 1 个 Path 2/biweekly base id：`core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly_cost_guard`。本路径可复现实验命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly_cost_guard`。
- `cap70_biweekly_cost_guard` 五窗口 CAGR 为 `7.80% / 12.90% / 21.82% / 66.66% / 36.64%`，最大回撤为 `-43.06% / -34.99% / -27.49% / -20.18% / -11.61%`，换手为 `4.98x / 5.47x / 6.03x / 12.00x / 12.54x`。结果确认这条双周成本线的长窗收益和回撤都弱，短窗换手也偏高，只保留为 underrepresented 失败对照。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `738`，`biweekly_rebalance_aggressive=23`、`weekly_rebalance_aggressive=63`、`high_growth_theme=323`；`scripts/update_weighted_winners.py` 后 Path 2 window winner/robust/tracked payload 重新同步但未被本轮候选替换，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 738/738 complete`，下一轮 focus 为 `capacity_and_cost_stress`。第一条命令建议回到 high-growth robust 邻域做容量/成本压力，而不是继续扩弱双周线，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap60_cashguard_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-28 10:34 CST）

- 开局 guard 为 `pass`；上一轮 `reconfirm75/caution85/cap75` 保留 2020/2025 弹性但 2026 转负，本轮按 `medium_cycle_growth/risk_reconfirm_sensitivity` 继续同一中周期高收益族，把单票 cap 降到 `65`，观察能否修复 2026 与集中风险。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `25.34% / 39.69% / 38.86% / 130.50% / -12.60%`，最大回撤为 `-52.66% / -36.35% / -33.69% / -11.51% / -13.03%`，换手为 `3.77x / 4.65x / 4.44x / 7.30x / 7.25x`；总市值版为 `24.84% / 35.04% / 31.15% / 142.71% / -6.29%`，最大回撤为 `-52.50% / -35.26% / -33.51% / -13.29% / -10.19%`。降低 cap 没有修复 2017 深回撤与 2026 负收益，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `733`，`high_growth_theme=323`、`weekly_rebalance_aggressive=62`、`emergent_theme_discovery=60`；`scripts/update_weighted_winners.py` 后 Path 2 tracked/window winner 有同步校验但本轮候选未替换 official/robust，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 733/733 complete`，下一轮 focus 为 `underrepresented_families`。第一条命令建议暂停 high-growth cap/risk 邻域，补一个低相关双周或防守多因子代表，例如 `core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_ids>`。

## 本轮执行计划（2026-05-28 04:19 CST）

- 开局 guard 为 `pass`；上一轮等权多因子 companion 只提供低相关失败对照，本轮按 `medium_cycle_growth` 回到高收益中周期族。上一轮建议的 `risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard` 已有完整结果，因此本轮新增更严恢复确认、更高谨慎仓、更低 cap 的 `reconfirm75/caution85/cap75` 版本。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap75_cashguard`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `25.58% / 40.34% / 39.97% / 123.65% / -16.32%`，最大回撤 `-52.66% / -37.14% / -34.65% / -12.63% / -14.07%`，换手 `3.78x / 4.67x / 4.44x / 7.31x / 6.78x`；总市值版为 `24.93% / 34.91% / 31.45% / 137.04% / -12.00%`，最大回撤 `-52.50% / -36.38% / -33.89% / -14.69% / -12.05%`。该组验证更严恢复确认仍保留 2020/2025 弹性，但 2017 深回撤和 2026 负收益仍未修复，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `727`，`high_growth_theme=321`；`scripts/update_weighted_winners.py` 后 Path 2 tracked/window winner 有同步校验但本轮候选未替换 official/robust，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 仍为 `medium_cycle_growth`。第一条命令建议不要继续只升恢复确认，改测 `risk45/exit55` 下的 2026 修复约束，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm75_caution85_cap65_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-27 17:17 CST）

- 开局 guard 为 `pass`；上一轮 high-growth `risk35/exit55/reconfirm80/caution80/cap80_cost_guard` 仍保留 2023/2025 弹性但 2026 转负，本轮按计划补一个非 high-growth/低相关等权多因子代表，避免 Path 2 继续被 high_growth family 压扁。
- 本轮新增并五窗口确认 1 个 Path 2/decorrelated defensive mix base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm`。实际 A股合并命令见 Path 1 本轮记录，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版 `quality_lowvol_trend_reconfirm` 五窗口 CAGR 为 `11.43% / 13.24% / 28.21% / 62.24% / 70.34%`，最大回撤为 `-48.92% / -37.49% / -31.57% / -14.92% / -13.55%`，换手为 `3.23x / 3.59x / 3.99x / 5.96x / 6.62x`。它能给 2026 正收益对照，但 2017/2020 收益与回撤远弱于 Path 2 robust，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `722`，`decorrelated_defensive_mix=21`、`high_growth_theme=319`、`weekly_rebalance_aggressive=60`；`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 已轮换为 `medium_cycle_growth`。第一条命令建议回到中周期高收益原型，但显式带 2026 防守约束，测试等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard` 或同等恢复阈值/风险阈值折中，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-27 11:22 CST）

- 开局 guard 为 `pass`；上一轮 focus 指向 `risk_reconfirm_sensitivity`，本轮按计划用等权/总市值双底座确认更低风险阈值 `risk35`、更严恢复确认 `reconfirm80`、更低 `exit55` 与 `caution80/cap80` 的 high-growth 变体。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard`。实际 A股合并命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_12_88_hold_3_7_ramp85_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn04_exit92_weekly`。
- 等权版五窗口 CAGR 为 `32.74% / 32.30% / 47.32% / 89.91% / -12.81%`，最大回撤 `-29.20% / -30.50% / -33.63% / -24.52% / -14.09%`，换手 `3.65x / 4.20x / 4.23x / 7.55x / 6.44x`；总市值版为 `29.84% / 27.35% / 41.13% / 104.93% / -8.68%`，最大回撤 `-30.06% / -30.43% / -33.69% / -26.80% / -12.54%`。该组仍保留 2023/2025 弹性，但 2026 转负且最近持仓高度集中在源杰科技/腾景科技，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `716`，`high_growth_theme=319`，raw robust 仍由旧 high-growth 组合领先；`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`，四窗口 meanCAGR `46.97%`、minCAGR `21.83%`、worstMaxDD `-15.47%`、meanTurn `3.00x`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，`ashare_path2_candidate_universe 716/716 complete`，下一轮 focus 转为 `underrepresented_families`。第一条命令建议暂停继续堆 high-growth 参数，补一个非 high-growth/低相关代表，例如等权多因子或双周低回撤族 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_trend_reconfirm` 或同等 underrepresented family，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_ids>`。

## 本轮执行计划（2026-05-27 05:20 CST）

- 开局 guard 为 `pass`；上一轮双周 underrepresented family 与等权多因子 companion 都没有改善 robust，本轮按 `capacity_and_cost_stress` 回到 high-growth robust 邻域。上一轮文档建议的 `aggr_02_98...reconfirm75_cap80_cost_guard` 已有结果，因此本轮改为未尝试的 `aggr_02_98...reconfirm75_caution80_cap80_cost_guard`，用等权/总市值双底座五窗口确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard`。实际 A股非阻塞命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap80_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap58_hold6_turn06_exit88_weekly`。
- 等权版五窗口 CAGR 为 `37.17% / 50.02% / 49.92% / 109.40% / -11.67%`，最大回撤 `-32.86% / -32.31% / -29.14% / -12.09% / -14.09%`，换手 `3.70x / 4.33x / 4.36x / 7.32x / 6.44x`；总市值版为 `34.81% / 43.44% / 43.02% / 123.49% / -7.48%`，最大回撤 `-33.12% / -32.53% / -30.81% / -14.73% / -12.54%`。该组保留 2020/2023 高收益，但 2026 仍负，且最近持仓高度集中在源杰科技/腾景科技，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `710`，`high_growth_theme=317`；`scripts/update_weighted_winners.py` 后 Path 2 official winner、robust candidate 与 tracked payload 未变化，robust 仍为 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_cash_off`，四窗口 meanCAGR `46.97%`、minCAGR `21.83%`、worstMaxDD `-15.47%`、meanTurn `3.00x`。候选池未触发 Path 2 evict。
- 最终 guard 为 `pass`，下一轮 focus 转为 `risk_reconfirm_sensitivity`。第一条命令建议不要继续只压 cap，改测更强风险阈值与恢复确认组合，例如等权/总市值 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm80_caution80_cap80_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-26 23:15 CST）

- 开局 guard 为 `pass`；上一轮要求从 `underrepresented_families` 补非 high-growth 代表，本轮用双周 rebalance + 成本守门做压力测试，并把等权多因子 companion 纳入 Path 2 横向比较。A股非阻塞命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm,core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap58_hold6_turn06_exit88_weekly`。
- 本轮新增并五窗口确认 1 个 Path 2 underrepresented/biweekly base id：`core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard`。五窗口 CAGR 为 `7.80% / 12.91% / 21.82% / 66.66% / 36.64%`，最大回撤 `-43.17% / -34.99% / -27.49% / -20.18% / -11.61%`，换手 `4.99x / 5.47x / 6.03x / 12.00x / 12.54x`。双周成本守门没有改善 2020/2023，上限也低于 high-growth robust。
- 等权多因子 companion `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_industry_reconfirm` 的五窗口 CAGR 为 `12.76% / 15.65% / 30.93% / 55.06% / 69.85%`，2026 较强但 2017/2020/2023 回撤过深，只保留为 decorrelated defensive mix 失败对照。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `705`，raw robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`；`scripts/update_weighted_winners.py` 后 Path 2 official winner/robust/tracked payload 未变化。候选池未触发 Path 2 evict。最终 focus 转为 `capacity_and_cost_stress`；下一轮第一条命令建议回到 high-growth robust 邻域压 cap 与成本，而不是继续扩弱双周，例如等权/总市值 `aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-26 05:09 CST）

- 开局 guard 为 `pass`；上一轮 `exit55/reconfirm75/caution80/cap75` 仍无法修复 2026 负收益，本轮沿 `medium_cycle_growth` 把退出阈值进一步收紧到 `exit50`，继续只用等权/总市值双底座确认。命令类型为五窗口 `--only-base-ids` 增量确认，实际 A股合并命令见 Path 1 本轮记录。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit50_reconfirm75_caution80_cap75_cashguard`。
- 等权版五窗口 CAGR 为 `27.37% / 41.10% / 37.42% / 112.60% / -10.52%`，最大回撤 `-29.02% / -35.78% / -27.60% / -11.78% / -13.61%`，换手 `3.81x / 4.47x / 4.61x / 7.30x / 6.66x`；总市值版为 `26.55% / 35.36% / 27.84% / 123.31% / -6.02%`，最大回撤 `-28.98% / -35.55% / -29.95% / -13.87% / -11.64%`。该组证明单纯收紧 exit 不能修复 2026，且近期贡献仍高度集中在少数高弹性票。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `699`，`high_growth_theme=315`，raw robust 仍为 `core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`；`scripts/update_weighted_winners.py` 后 official robust/tracked payload 未变化。
- 候选池未触发 Path 2 evict。最终 focus 转为 `risk_reconfirm_sensitivity`；下一轮第一条命令建议不要继续只压 exit，改测更强风险阈值与恢复确认组合，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit50_reconfirm80_caution80_cap70_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-25 17:20 CST）

- 开局 guard 为 `pass`；上一轮 `risk35 + exit55 + reconfirm75 + caution80 + cap70` 仍无法修复 2026 负收益，本轮按 `risk_reconfirm_sensitivity` 把风险阈值调回 `risk40`、保留 `exit55/reconfirm75/caution80/cap75/cashguard`，继续只用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard`。实际命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap55_hold8_turn05_exit92_weekly`。
- 等权版五窗口 CAGR 为 `26.50% / 41.09% / 37.42% / 112.60% / -10.52%`，最大回撤 `-33.44% / -35.78% / -27.60% / -11.78% / -13.61%`，换手 `3.78x / 4.47x / 4.61x / 7.30x / 6.66x`；总市值版为 `25.68% / 35.35% / 27.84% / 123.31% / -6.02%`，最大回撤 `-33.40% / -35.55% / -29.95% / -13.87% / -11.64%`。该组保留 2020/2025 弹性，但 2026 仍负，且近期贡献继续集中在少数高弹性票。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `686`，raw robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95`；`scripts/update_weighted_winners.py` 后 official robust 仍偏向既有 high-growth 组合，本轮未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 focus 转为 `underrepresented_families`；下一轮第一条命令不要继续只压 high-growth 参数，建议补一个双周/非 high-growth 代表，例如 `core_explore_60_40_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-25 11:21 CST）

- 开局 guard 为 `pass`；上一轮 `risk35 + reconfirm75 + caution75 + cap80` 保留 2020 中周期强收益但 2026 仍负，本轮按 `capacity_and_cost_stress` 把谨慎仓提高到 `80/55`、单票 cap 降到 `70`，继续只用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard`。实际命令见 Path 1 本轮 A股非阻塞合并批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `26.38% / 40.94% / 36.43% / 115.84% / -8.58%`，最大回撤 `-33.44% / -35.78% / -27.96% / -11.51% / -13.10%`，换手 `3.77x / 4.46x / 4.61x / 7.29x / 6.90x`；总市值版为 `25.64% / 35.49% / 27.47% / 125.98% / -3.08%`，最大回撤 `-33.40% / -35.55% / -30.20% / -13.16% / -10.74%`。
- 该组比上一轮更强容量约束后仍不能修复 2026，且近期收益仍高度集中在源杰科技、腾景科技等少数票；`scripts/path2_candidate_pass.py` 后 universe 为 `681`，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_caution80_cap95`，未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 guard 为 `ashare_path2_candidate_universe 681/681 complete`，下一轮 focus 转为 `risk_reconfirm_sensitivity`；第一条命令建议停止继续单纯压 cap，改测风险阈值与恢复确认折中，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit55_reconfirm75_caution80_cap75_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-25 05:15 CST）

- 开局 guard 为 `pass`，上一轮 `risk45 + exit55 + reconfirm70 + caution80 + cap80 + cashguard` 保留 2017/2020 高收益但 2026 仍负；本轮按 `risk_reconfirm_sensitivity` 继续把风险阈值降到 `risk35`、恢复确认升到 `reconfirm75`，用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard`。实际 A股非阻塞命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap60_hold7_turn06_exit90_weekly`。
- 等权版五窗口 CAGR 为 `26.40% / 41.14% / 37.59% / 108.60% / -11.46%`，最大回撤 `-31.78% / -34.45% / -26.60% / -11.78% / -13.93%`，换手 `3.71x / 4.38x / 4.53x / 7.30x / 6.30x`；总市值版为 `25.49% / 35.12% / 27.80% / 119.76% / -7.95%`，最大回撤 `-31.88% / -34.32% / -28.97% / -13.96% / -12.54%`。
- 该组相对近期 cap/caution 失败组改善部分中窗平衡，但 2026 仍为负，且近期贡献仍集中在源杰科技、腾景科技等少数高弹性票；`scripts/path2_candidate_pass.py` 后 universe 为 `675`，`scripts/update_weighted_winners.py` 后 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 focus 转为 `capacity_and_cost_stress`；下一轮第一条命令建议在本组基础上先测更强容量/谨慎仓约束，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution80_cap70_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-25 00:29 CST）

- 开局 guard 为 `pass`，上一轮建议测试中周期恢复阈值与 2026 防守折中；本轮在 high-growth robust 邻域新增 `risk45 + exit55 + reconfirm70 + caution80 + cap80 + cashguard`，用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard`。命令类型为 A股五窗口 `--only-base-ids` 增量确认：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard`。
- 等权版五窗口 CAGR 为 `30.73% / 48.46% / 38.45% / 100.65% / -12.45%`，最大回撤 `-23.86% / -27.67% / -27.19% / -14.29% / -14.12%`，换手 `4.15x / 4.57x / 4.61x / 7.33x / 6.42x`；总市值版为 `30.32% / 42.17% / 28.26% / 110.68% / -8.93%`，最大回撤 `-23.81% / -28.98% / -29.65% / -14.58% / -12.55%`。该组合保留 2017/2020 中周期高收益，但 2023 走弱且 2026 仍为负，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `670`，family 规模为 `emergent_theme_discovery=58 / high_growth_theme=307 / momentum_equal_weight_elastic=30 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=52`；`scripts/update_weighted_winners.py` 后 Path 2 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 focus 为 `risk_reconfirm_sensitivity`；下一轮第一条命令建议更直接降低风险门槛并提高恢复确认，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit55_reconfirm75_caution75_cap80_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_risk_reconfirm_ids>`。

## 本轮执行计划（2026-05-24 17:14 CST）

- 开局 guard 为 `pass`，上一轮等权 `profitability_lowvol_rebalance` 只保留 2025/2026 弹性、长窗回撤过深；本轮按 `capacity_and_cost_stress` 回到 high-growth robust 邻域，在 `cap70 + cashguard` 上把谨慎仓提高到 `80/55`，用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard`。命令类型为 A股五窗口 `--only-base-ids` 增量确认，实际合并命令见 Path 1 本轮记录。
- 等权版五窗口 CAGR 为 `29.75% / 49.36% / 42.26% / 106.66% / -8.60%`，最大回撤 `-30.50% / -23.78% / -27.89% / -14.29% / -13.10%`，换手 `3.94x / 4.41x / 4.76x / 7.32x / 6.90x`；总市值版为 `29.03% / 43.61% / 32.92% / 115.68% / -3.10%`，最大回撤 `-30.46% / -27.21% / -30.13% / -13.93% / -10.74%`。提高 caution 后仍无法修复 2026 负收益，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `666`，family 规模为 `emergent_theme_discovery=61 / high_growth_theme=305 / momentum_equal_weight_elastic=30 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=51`；`scripts/update_weighted_winners.py` 后 Path 2 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，未触发 tracked payload 替换。
- 候选池未触发 Path 2 evict。最终 focus 转为 `medium_cycle_growth`；下一轮第一条命令建议停止继续只降 cap，改测中周期恢复阈值与 2026 防守的折中，例如等权/总市值 `aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit55_reconfirm70_caution80_cap80_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-24 11:14 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `underrepresented_families`，要求不要继续只压 high-growth cap；本轮补等权多因子弹性代表 `profitability_lowvol_rebalance`，作为非 high-growth family 压力测试。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance`。实际命令见 Path 1 本轮 A股合并批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `equal_weight profitability_lowvol_rebalance` 五窗口 CAGR 为 `11.92% / 15.23% / 29.17% / 67.76% / 70.34%`，最大回撤 `-49.67% / -32.91% / -31.55% / -15.06% / -13.55%`，换手 `3.23x / 3.59x / 3.88x / 5.93x / 6.62x`。它保留 2025/2026 弹性，但 2017/2020 回撤太深，不改善 Path 2 robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `660`，family 规模为 `emergent_theme_discovery=58 / high_growth_theme=303 / momentum_equal_weight_elastic=30 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=51`；`scripts/update_weighted_winners.py` 后 Path 2 official winners 与 robust 未变化，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 Path 2 evict。最终 guard 下一轮 focus 转为 `capacity_and_cost_stress`；第一条命令建议回到当前 high-growth robust 邻域做更强容量/成本约束，而不是继续扩弱多因子，例如注册等权/总市值 `risk50_mom_exit60_reconfirm65_caution80_cap70_cashguard` 或同等 cap/caution 成本版，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-24 05:13 CST）

- 开局 guard 为 `pass`，上一轮 `risk50/reconfirm65/cap75/cashguard` 仍无法修复 2026 负收益；本轮按上一轮 `medium_cycle_growth`/本轮开局 `risk_reconfirm_sensitivity` 把 high-growth robust 邻域改成 `risk45 + reconfirm70 + cap75 + cashguard`，继续只跑等权/总市值双底座。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard`。实际命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk45_mom_exit60_reconfirm70_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap65_hold6_turn08_exit94_weekly`。
- 等权版五窗口 CAGR 为 `29.52% / 48.00% / 35.59% / 101.37% / -8.75%`，最大回撤 `-20.44% / -23.39% / -26.33% / -14.29% / -12.98%`，换手 `3.96x / 4.25x / 4.47x / 7.32x / 6.44x`；总市值版为 `29.05% / 41.94% / 27.06% / 110.89% / -4.47%`，最大回撤 `-20.57% / -28.09% / -28.47% / -13.93% / -11.24%`。两者保留 2020 中周期收益，但 2023 回落且 2026 仍为负，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `656`，family 规模为 `emergent_theme_discovery=58 / high_growth_theme=303 / momentum_equal_weight_elastic=29 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=50`；`scripts/update_weighted_winners.py` 后 Path 2 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。候选池未触发 Path 2 evict。
- 最终 guard 下一轮 focus 转为 `underrepresented_families`。下一轮第一条命令不要继续只压 high-growth cap，建议补一个等权多因子弹性代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_profitability_lowvol_rebalance` 或同等非 high-growth family，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_ids>`。

## 本轮执行计划（2026-05-23 23:19 CST）

- 开局 guard 为 `pass`，上一轮 `reconfirm70_cap85_cashguard` 仍未修复 2026 负收益；本轮按 `capacity_and_cost_stress` 把相同 high-growth robust 邻域进一步降到 `cap75`，继续只用等权/总市值双底座做五窗口确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard`。实际命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap75_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap68_hold5_turn10_exit92_weekly`。
- 等权版五窗口 CAGR 为 `29.39% / 48.56% / 42.17% / 102.15% / -9.52%`，最大回撤 `-28.74% / -23.39% / -26.80% / -14.29% / -13.08%`，换手 `3.86x / 4.32x / 4.67x / 7.32x / 6.53x`；总市值版为 `28.56% / 42.48% / 32.81% / 111.67% / -5.21%`，最大回撤 `-28.87% / -28.09% / -29.07% / -13.93% / -11.24%`。cap75/cashguard 保留 2020/2023 中周期收益，但仍不能把 2026 转正，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `649`，family 规模为 `emergent_theme_discovery=55 / high_growth_theme=301 / momentum_equal_weight_elastic=28 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=49`；`scripts/update_weighted_winners.py` 后 Path 2 official winners/robust 未变化，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 Path 2 evict。最终 guard 下一轮 focus 为 `medium_cycle_growth`；下一轮第一条命令建议不要继续机械降 cap，改测恢复阈值/风险阈值折中，例如等权/总市值 `risk45_mom_exit60_reconfirm70_cap75_cashguard`，注册后五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-23 17:14 CST）

- 开局 guard 为 `pass`，上一轮 `cap85_cashguard` 仍保留 2020/2023 中周期收益但 2026 为负；本轮按 `risk_reconfirm_sensitivity` 把恢复确认阈值提高到 `reconfirm70`，继续用等权/总市值双底座确认是否能修复 2026，而不是扩全量 high-growth 邻域。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard`。实际非阻塞 A股批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap85_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap68_hold5_turn10_exit92_weekly`。
- 等权版五窗口 CAGR 为 `30.46% / 48.44% / 38.38% / 96.12% / -13.27%`，最大回撤 `-21.20% / -25.61% / -26.09% / -14.29% / -14.88%`，换手 `4.04x / 4.34x / 4.53x / 7.33x / 6.04x`；总市值版为 `30.05% / 41.81% / 28.08% / 106.76% / -10.78%`，最大回撤 `-21.36% / -30.06% / -28.60% / -14.61% / -13.84%`。两者仍未把 2026 转正，因此不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `643`，family 规模为 `emergent_theme_discovery=52 / high_concentration_breakout=154 / high_growth_theme=299 / momentum_equal_weight_elastic=28 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=48`。`scripts/update_weighted_winners.py` 后 official Path 2 winners/robust 切回验证更稳的 high-growth 组合：2017 robust 为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，2020/2023 分别仍由 `risk40...reconfirm70_cap95` 与 `risk50_ma_cap95` 领先；本轮 `reconfirm70_cap85_cashguard` 未替换 official。
- 候选池未触发 Path 2 evict。最终 guard 下一轮 focus 为 `capacity_and_cost_stress`；下一轮第一条命令建议回到 official robust 邻域做更直接容量/成本压力，而不是继续只调 reconfirm，例如实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap75_cashguard` 或同等更低 cap/cost 版本，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-23 11:18 CST）

- 开局 guard 为 `pass`，上一轮 `cap75_biweekly_cost_guard` 确认双周 underrepresented family 长窗回撤过深；本轮按 rotation 的 `medium_cycle_growth` 回到 Path 2 high-growth robust 邻域，新增 `risk50 + reconfirm65 + cap85 + cashguard`，用等权/总市值双底座检查能否在保留 2020/2023 中周期收益的同时修复 2026。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard`。实际非阻塞 A股批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap85_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cost_guard_cap55_hold6_turn10_exit88_weekly`。
- 等权版五窗口 CAGR 为 `29.54% / 48.43% / 44.27% / 95.95% / -13.27%`，最大回撤 `-28.74% / -25.61% / -26.09% / -14.29% / -14.88%`，换手 `3.86x / 4.34x / 4.67x / 7.33x / 6.04x`；总市值版为 `28.59% / 41.79% / 33.53% / 106.58% / -10.78%`，最大回撤 `-28.87% / -30.06% / -28.60% / -14.61% / -13.84%`。cap85/cashguard 保留了 2020/2023 中周期收益，但 2026 仍为负，不替换 official winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `636`，family 规模为 `emergent_theme_discovery=49 / high_concentration_breakout=154 / high_growth_theme=297 / momentum_equal_weight_elastic=27 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=47`；raw robust 仍偏向 `risk40_mom_exit60_reconfirm75_caution80_cap95`，`scripts/update_weighted_winners.py` 后 official robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 Path 2 evict。收尾 guard 下一轮 focus 为 `risk_reconfirm_sensitivity`；下一轮第一条命令建议不要继续只调 cap，改测恢复确认阈值/谨慎仓组合对 2026 的影响，例如等权/总市值 `risk50_mom_exit60_reconfirm70_cap85_cashguard` 或 `risk45_mom_exit60_reconfirm65_caution75_cap85_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_reconfirm_sensitivity_ids>`。

## 本轮执行计划（2026-05-23 05:15 CST）

- 开局 guard 为 `pass`，上一轮 focus 为 `underrepresented_families`；本轮按计划新增一个双周成本守门代表，而不是继续扩大 high_growth family。Path 4 新注册先触发 blocking coverage，本轮已先按 guard 原始 Path 4 `--only-base-ids` 补齐后再执行 Path 2 非阻塞批次。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard`。实际命令见 Path 1 本轮 A股非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- `cap75_biweekly_cost_guard` 五窗口 CAGR 为 `3.08% / 10.20% / 26.95% / 65.20% / 34.60%`，最大回撤 `-64.94% / -57.72% / -30.61% / -26.92% / -14.68%`，换手 `4.50x / 4.69x / 4.96x / 9.28x / 11.23x`。它保留 2025/2026 弹性，但 2017/2020 深回撤确认双周 underrepresented family 仍不是可晋级中周期高收益原型。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `631`，family 规模为 `emergent_theme_discovery=47 / high_concentration_breakout=154 / high_growth_theme=295 / momentum_equal_weight_elastic=27 / biweekly_rebalance_aggressive=21 / weekly_rebalance_aggressive=46`。raw robust 临时偏向 `risk40_mom_exit60_reconfirm75_caution80_cap95`，但 `scripts/update_weighted_winners.py` 后 official Path 2 winners 与 robust 仍未变化，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 Path 2 evict。收尾 focus 转向 `capacity_and_cost_stress`；下一轮第一条命令建议回到 official robust 邻域做容量/成本压力，而不是继续普通双周扩展，例如实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap85_cashguard` 或同等 cap85/cost 对照，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-22 23:15 CST）

- 开局 guard 为 `pass`，上一轮 `cap70 cashguard` 仍未把 2026 转正；本轮按 `risk_reconfirm_sensitivity` 继续在 high_growth robust 邻域上增加谨慎仓阈值，用等权/总市值双底座确认 `caution75 + cap70 + cashguard` 是否能保留 2020/2023 中周期收益。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard`。实际非阻塞 A股批次命令为：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap75_hold5_turn12_exit88_weekly`。
- 等权版五窗口 CAGR 为 `29.37% / 48.74% / 41.44% / 105.48% / -7.67%`，最大回撤 `-29.05% / -22.88% / -27.27% / -14.29% / -12.64%`，换手 `3.86x / 4.32x / 4.68x / 7.31x / 6.78x`；总市值版为 `28.63% / 42.98% / 32.63% / 114.49% / -2.20%`，最大回撤 `-29.15% / -27.21% / -29.38% / -13.93% / -10.30%`。相对 cap70 旧版，2026 亏损缩窄但仍为负，未改变 official winner 或 robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `626`，family 规模为 `emergent_theme_discovery=44 / high_concentration_breakout=154 / high_growth_theme=295 / momentum_equal_weight_elastic=27 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=45`。raw robust 仍偏向 `risk40_mom_exit60_reconfirm75_caution80_cap95`，但 `update_weighted_winners.py` official robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`，说明验证窗仍不接受本轮更强现金防守。
- 候选池未触发 cap evict。收尾 guard 给出下一轮 focus `underrepresented_families`；下一轮不要继续只压 high_growth cap，第一条命令建议实现一个双周或等权弹性代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap75_biweekly_cost_guard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_id>`。

## 本轮执行计划（2026-05-22 18:19 CST）

- 开局 guard 为 `pass`，上一轮 `trend_industry_momentum` 等权弹性代表长窗回撤过深，本轮按 `capacity_and_cost_stress` 回到当前 high_growth robust 邻域，把上一轮 `cap80 cashguard` 继续压到 `cap70`，用等权/总市值双底座确认容量约束是否能修复 2026。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap70_cashguard`。实际命令见 Path 1 本轮 A股非阻塞批次，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `29.29% / 48.57% / 41.20% / 105.24% / -7.62%`，最大回撤 `-28.74% / -22.88% / -27.15% / -14.29% / -12.60%`，换手 `3.85x / 4.31x / 4.67x / 7.31x / 6.77x`；总市值版为 `28.55% / 42.81% / 32.44% / 114.20% / -2.34%`，最大回撤 `-28.87% / -27.21% / -29.30% / -13.93% / -10.35%`。cap70 降低部分长窗回撤，但 2026 仍为负，未晋级 official。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `618`，family 规模为 `emergent_theme_discovery=41 / high_concentration_breakout=154 / high_growth_theme=293 / momentum_equal_weight_elastic=25 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=44`。raw robust 仍偏向 `risk50_mom_exit60_reconfirm75_caution75_cap95`，`update_weighted_winners.py` official robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 cap evict。收尾 guard 给出下一轮 focus `medium_cycle_growth`；下一轮不要继续只压 cap，第一条命令建议实现等权/总市值 `risk50_mom_exit60_reconfirm65_caution75_cap70_cashguard`，检查谨慎仓阈值能否让 2026 转正且保留 2020/2023 中周期收益，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_medium_cycle_ids>`。

## 本轮执行计划（2026-05-22 11:17 CST）

- 开局 guard 为 `pass`，上一轮建议把 focus 从 high_growth/cap80 邻域转向 `underrepresented_families`；本轮补 1 个 `momentum_equal_weight_elastic` 代表，使用等权底座的 `trend_industry_momentum` 多因子压力测试，而不是继续扩单一 high_growth family。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_trend_industry_momentum`。实际命令见 Path 1 本轮 A股合并命令，命令类型为五窗口 `--only-base-ids` 增量确认。
- `equal_weight trend_industry_momentum` 五窗口 CAGR 为 `15.32% / 18.36% / 30.98% / 91.55% / 79.34%`，最大回撤 `-37.83% / -39.59% / -31.78% / -11.52% / -10.89%`，换手 `3.28x / 3.70x / 3.99x / 5.51x / 7.75x`；2025/2026 弹性尚可，但 2017/2020 回撤和收益均弱于 Path 2 robust，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `612`，`momentum_equal_weight_elastic=25`、`weekly_rebalance_aggressive=43`；raw robust 仍偏向 `risk50_mom_exit60_reconfirm75_caution75_cap95`，`update_weighted_winners.py` official robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`，`meanCAGR=60.27% / minCAGR=36.23%`。
- 候选池未触发 cap evict。收尾 guard 的下一轮 focus 为 `capacity_and_cost_stress`，第一条命令建议不要复制本轮弱多因子，而是回到当前 robust 邻域做更严格容量/成本确认：实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap70_cashguard` 或同等 cap70 成本守门候选，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_capacity_cost_ids>`。

## 本轮执行计划（2026-05-22 05:14 CST）

- 开局 guard 为 `pass`，上一轮 `risk50_mom_exit60_reconfirm65_cap80_cost_guard` 保留中周期收益但 2026 仍负；本轮按 `risk_reconfirm_sensitivity`/2026 防守缺口，在相同 cap80 邻域切到 `cashguard`，继续只用等权/总市值双底座确认。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cashguard`。实际命令见 Path 1 本轮合并命令，命令类型为五窗口 `--only-base-ids` 增量确认。
- 等权版五窗口 CAGR 为 `29.50% / 48.50% / 43.30% / 99.10% / -11.40%`，最大回撤 `-28.70% / -24.50% / -26.40% / -14.30% / -13.90%`，换手 `3.86x / 4.33x / 4.67x / 7.33x / 6.29x`；总市值版为 `28.60% / 42.20% / 33.20% / 109.00% / -8.00%`，最大回撤 `-28.90% / -29.00% / -28.80% / -13.90% / -12.50%`。cashguard 降低了长窗回撤，但仍不能把 2026 转正，未晋级 official。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `607`，family 规模为 `emergent_theme_discovery=35 / high_concentration_breakout=154 / high_growth_theme=291 / momentum_equal_weight_elastic=24 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=42`；raw robust 临时偏向 `risk50_mom_exit60_reconfirm75_caution75_cap95`，但 `update_weighted_winners.py` official robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 cap evict。收尾 guard 将下一轮 focus 转到 `underrepresented_families`，因此不要继续只扩 high_growth/cap80 邻域；第一条命令建议补一个 `momentum_equal_weight_elastic` 或双周代表，例如 `core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_trend_industry_momentum` 或一个低回撤双周成本候选，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <next_path2_underrepresented_family_id>`。

## 本轮执行计划（2026-05-21 23:16 CST）

- 开局 guard 为 `pass`，上一轮 `cap70_biweekly` 确认双周 underrepresented family 的 2017/2020 回撤不可接受；本轮按上一轮下一步和 candidate-pass raw robust 线，转向当前高收益 robust 邻域的容量/成本压力，不继续扩大双周失败支线。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap80_cost_guard`。实际命令见 Path 1 本轮合并命令。
- 等权版五窗口 CAGR 为 `34.10% / 56.20% / 56.46% / 99.55% / -12.18%`，最大回撤 `-39.23% / -33.08% / -33.27% / -14.29% / -13.97%`，换手 `4.12x / 4.65x / 4.49x / 7.34x / 6.38x`；总市值版为 `33.32% / 49.16% / 47.72% / 109.53% / -8.78%`，最大回撤 `-39.58% / -33.47% / -35.16% / -14.51% / -12.54%`。cap80 保留 2020/2023 高收益，但 2026 仍为负，未晋级 official。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `602`，family 规模为 `emergent_theme_discovery=33 / high_concentration_breakout=154 / high_growth_theme=289 / momentum_equal_weight_elastic=24 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=41`。raw robust 临时切到 `risk50_mom_exit60_reconfirm75_caution75_cap95`，但 `update_weighted_winners.py` official robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`，说明 validation 仍偏好旧恢复确认形态。
- 候选池未触发 cap evict；本轮结论是容量 cap80 不是解决 2026 负收益的充分条件。下一轮 focus -> candidates 池优先做 `2026 defense without killing 2020/2023`：第一条命令建议实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap80_cashguard`，五窗口 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path2_cap80_cashguard_ids>`；若继续成本线，先记录本轮 `cap80_cost_guard` 为 2026 失败对照。

## 本轮执行计划（2026-05-21 18:23 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`，rotation 继续指向 `underrepresented_families`；上一轮 80/20 等权双周 cap60 深回撤，本轮不再扩 high_growth 邻域，改测 70/30 等权双周 cap70。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly`。实际命令见 Path 1 本轮合并命令。
- `cap70_biweekly` 五窗口 CAGR 为 `3.98% / 10.04% / 24.39% / 71.47% / 40.86%`，最大回撤 `-56.21% / -53.86% / -28.69% / -21.50% / -13.12%`，换手 `4.81x / 5.25x / 6.01x / 11.72x / 12.33x`；70/30 提高短窗弹性但 2017/2020 回撤仍不可接受，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `595`，family 规模为 `emergent_theme_discovery=30 / high_concentration_breakout=154 / high_growth_theme=287 / momentum_equal_weight_elastic=23 / biweekly_rebalance_aggressive=20 / weekly_rebalance_aggressive=40`；`update_weighted_winners.py` 后 Path 2 official winners 与 robust 未变，robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 cap evict；本轮确认说明双周 underrepresented family 的主要问题仍是长窗回撤和 2020 收益不足，而不是单纯 cap 太低。
- 收尾 guard 后 rotation 切到 `capacity_and_cost_stress`。下一轮第一条命令建议围绕当前 robust 直接做容量/成本压力：实现等权/总市值 `risk50_mom_exit60_reconfirm65_cap80_cost_guard` 双底座，用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <path2_capacity_cost_ids>` 增量确认；若仍要继续双周 underrepresented family，先把 `cap70_biweekly` 作为失败对照，不再扩大高回撤邻域。

## 本轮执行计划（2026-05-21 11:17 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `reconfirm70 cap80 cashguard` 没能修复 2026，本轮按当前 rotation 的 `underrepresented_families` 不再加 high_growth 邻域，转向双周代表候选。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap60_biweekly`。
- 该双周 cap60 五窗口 CAGR 为 `3.74% / 10.33% / 26.59% / 67.99% / 48.67%`，最大回撤 `-62.70% / -56.35% / -30.61% / -26.92% / -14.21%`，换手 `4.31x / 4.65x / 4.97x / 9.41x / 11.68x`；2025/2026 弹性不够抵消 2017/2020 深回撤，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `590/590 complete`，`biweekly_rebalance_aggressive=19`、`weekly_rebalance_aggressive=39`、`emergent_theme_discovery=27`；`update_weighted_winners.py` 后 Path 2 official winners 与 robust 未变，robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 候选池未触发 cap evict；本轮新增确认说明普通 80/20 等权双周 cap60 不能作为中周期高收益原型，只保留为 underrepresented family 失败对照。
- 下一轮 focus -> candidates 池：如果仍是 `underrepresented_families`，第一条命令建议测试更高弹性的 `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap70_biweekly`；若 rotation 回到风险确认线，再执行上一轮未跑的 `risk40_mom_exit60_reconfirm70_cap75_cashguard` 等权/总市值双底座，均用五窗口 `--only-base-ids`。

## 本轮执行计划（2026-05-21 05:14 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `reconfirm75 cap80 cashguard` 保留 2020/2023 高收益但 2026 仍负，本轮按 `risk_reconfirm_sensitivity` 把恢复确认放宽到 `70`，继续只测等权/总市值双底座。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap80_cashguard`。实际回测命令见 Path 1 本轮合并命令。
- 等权版五窗口 CAGR 为 `29.99% / 48.24% / 37.08% / 98.80% / -11.01%`，最大回撤 `-20.84% / -24.48% / -26.19% / -14.29% / -13.93%`，换手 `4.00x / 4.29x / 4.50x / 7.33x / 6.24x`；总市值版为 `29.55% / 41.91% / 27.59% / 108.77% / -7.64%`，最大回撤 `-20.92% / -28.98% / -28.47% / -13.93% / -12.54%`。放宽确认改善 2020 与 2017 回撤，但 2023/2026 不足，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `585/585 complete`，family 规模为 `high_concentration_breakout=154 / high_growth_theme=287 / momentum_equal_weight_elastic=23 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=38 / emergent_theme_discovery=24`。`update_weighted_winners.py` 后 Path 2 official winners 与 robust 未变化，robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`。
- 收尾 guard 为 `pass`，Path 2 rotation 为 `stagnation_runs=5 / risk_reconfirm_sensitivity / rotate`；候选池未触发 evict。下一轮 focus -> candidates 池继续恢复确认/风控敏感性，但要解决 2026 负收益，第一条命令建议实现 `risk40_mom_exit60_reconfirm70_cap75_cashguard` 的等权/总市值双底座，并用五窗口 `--only-base-ids <next_reconfirm_sensitivity_ids>` 增量确认。

## 本轮执行计划（2026-05-20 23:27 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮 `cap80 + cost_guard` 保留了 2020/2023 高收益但 2026 仍为负，本轮按 `medium_cycle_growth` 的防守修复补 `cap80 + cashguard` 等权/总市值双底座。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cashguard`。实际回测命令见 Path 1 本轮合并命令。
- 等权版五窗口 CAGR 为 `29.48% / 41.80% / 37.02% / 107.86% / -10.99%`，最大回撤 `-30.99% / -31.34% / -26.24% / -11.51% / -13.93%`，换手 `3.67x / 4.20x / 4.50x / 7.30x / 6.24x`；总市值版为 `28.55% / 35.75% / 27.54% / 118.98% / -7.62%`，最大回撤 `-31.04% / -31.20% / -28.52% / -13.62% / -12.54%`。现金防守降低长窗收益且 2026 仍未转正，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `578/578 complete`；family 规模为 `high_concentration_breakout=154 / high_growth_theme=285 / momentum_equal_weight_elastic=22 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=37 / emergent_theme_discovery=21`。`update_weighted_winners.py` 后 Path 2 official winners 未变化，robust 仍为 `risk50_mom_exit60_reconfirm65_cap95`，`meanCAGR=64.55% / minCAGR=37.34% / worstMaxDD=-40.74% / meanTurn=5.20`。
- 收尾 guard 为 `pass`，Path 2 rotation 为 `stagnation_runs=2 / medium_cycle_growth / continue`；候选池未触发 evict。下一轮 focus -> candidates 池继续中周期高收益，但要优先修复 2026 防守，第一条命令建议实现 `risk40_mom_exit60_reconfirm70_cap80_cashguard` 的等权/总市值双底座，并用五窗口 `--only-base-ids <next_medium_cycle_growth_ids>` 增量确认。

## 本轮执行计划（2026-05-20 18:06 CST）

- 开局 guard 为 `pass / blocking=0 / warning=0`；上一轮等权弹性/多因子代表未晋级，最终 focus 指向 `capacity_and_cost_stress`。本轮按当前 high-growth robust 的容量压力测试，只补 `cap80 + cost_guard` 等权/总市值双底座。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard`。实际回测命令见 Path 1 本轮合并命令。
- 等权版五窗口 CAGR 为 `36.69% / 49.57% / 49.54% / 108.61% / -10.84%`，最大回撤 `-32.93% / -32.18% / -29.14% / -11.53% / -13.93%`，换手 `3.67x / 4.30x / 4.35x / 7.32x / 6.33x`；总市值版为 `34.36% / 43.02% / 42.68% / 122.70% / -6.91%`，最大回撤 `-33.20% / -32.40% / -30.81% / -14.15% / -12.54%`。容量约束保留了 2020/2023 高收益，但 2026 仍为负，未晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `571/571 complete`；family 规模为 `high_concentration_breakout=154 / high_growth_theme=283 / momentum_equal_weight_elastic=21 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=37 / emergent_theme_discovery=18`。raw robust 仍为 `risk40_mom_exit60_reconfirm75_caution80`，official robust 仍为 `risk40_mom_exit60_reconfirm75_cap95`。
- `update_weighted_winners.py` 后 Path 2 official winners 未变化：2017 `risk40_mom_exit60_reconfirm75_cap95`，2020 `risk40_mom_exit60_reconfirm70_cap95`，2023 `risk50_ma_cap95`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；候选池未触发 evict。
- 最终 guard 后 rotation 为 `stagnation_runs=12 / medium_cycle_growth / rotate`；下一轮 focus -> candidates 池回到中周期高收益原型，但必须带 2026 防守约束。第一条候选命令建议实现 `risk40_mom_exit60_reconfirm75_cap80_cashguard` 的等权/总市值双底座，并用五窗口 `--only-base-ids <next_medium_cycle_growth_ids>` 增量确认。

## 本轮执行计划（2026-05-20 13:58 CST）

- 上一轮 Path 2 rotation 指向 `underrepresented_families`，且 high_growth 已扩到 `281`；本轮只补 1 个等权弹性/多因子代表，不继续加 high_growth 邻域。
- 本轮新增并五窗口确认 1 个 Path 2 base id：`core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_defense`。实际回测命令见 Path 1 本轮合并命令。
- `core_multifactor_quality_defense` 五窗口 CAGR 为 `9.71% / 13.45% / 26.85% / 50.12% / 69.97%`，最大回撤 `-51.64% / -41.68% / -30.97% / -15.53% / -13.55%`，换手 `3.21x / 3.54x / 3.95x / 5.45x / 6.62x`；短窗尚可，但 2017/2020 收益和回撤明显弱于 Path 2 robust，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `565/565 complete`；family 规模为 `high_concentration_breakout=154 / high_growth_theme=281 / momentum_equal_weight_elastic=21 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=36 / emergent_theme_discovery=15`。raw robust 仍为 `risk40_mom_exit60_reconfirm75_caution80`，official robust 仍为 `risk40_mom_exit60_reconfirm75_cap95`。
- `update_weighted_winners.py` 后 Path 2 official winners 未变化：2017 `risk40_mom_exit60_reconfirm75_cap95`，2020 `risk40_mom_exit60_reconfirm70_cap95`，2023 `risk50_ma_cap95`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；候选池未触发 evict。
- 最终 guard 后 rotation 为 `stagnation_runs=9 / capacity_and_cost_stress / rotate`；下一轮 focus -> candidates 池先对当前 high-growth robust 做容量/换手压力，而不是继续扩大弱等权弹性。第一条命令建议先实现 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap80_cost_guard` 与对应总市值版本，再用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <capacity_cost_ids>` 补跑。

## 本轮执行计划（2026-05-20 05:20 CST）

- 上一轮提示为 `risk35/40`、`reconfirm75/80` 与 `caution65/70` 的交互；本轮在完成 Path 4 coverage block 后，沿 `risk_reconfirm_sensitivity` 新增 `risk35/reconfirm75/caution70` 与 `risk40/reconfirm80/caution70` 两个变体，并同时测试等权/总市值双底座。
- 本轮新增并五窗口确认 4 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk35_mom_exit60_reconfirm75_caution70_cap95`、`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95`、`core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm80_caution70_cap95`。实际回测命令见 Path 1 本轮合并命令。
- `risk35/reconfirm75/caution70` 等权版五窗口 CAGR 为 `35.44% / 50.05% / 49.04% / 100.99% / -14.08%`，总市值版为 `34.43% / 42.78% / 41.80% / 113.32% / -12.70%`；长窗仍强，但 2026 防守失败，且不如当前 official robust 的 2017/2020 平衡。
- `risk40/reconfirm80/caution70` 等权版五窗口 CAGR 为 `30.99% / 29.95% / 47.87% / 81.84% / -15.20%`，总市值版为 `29.19% / 24.09% / 39.48% / 94.63% / -13.84%`；恢复确认过严明显牺牲 2020/2017，不晋级。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `560`，新增独立 `emergent_theme_discovery=12`；family 规模为 `high_concentration_breakout=154 / high_growth_theme=281 / momentum_equal_weight_elastic=19 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=35`。raw robust 仍为 `risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`。
- `update_weighted_winners.py` 后 Path 2 official winners 未变化：2017 `risk40_mom_exit60_reconfirm75_cap95`，2020 `risk40_mom_exit60_reconfirm70_cap95`，2023 `risk50_ma_cap95`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust 仍为 `risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=61.28% / minCAGR=38.32% / worstMaxDD=-32.76% / meanTurn=4.98`。
- Guard 收尾为 `pass`，Path 2 rotation 为 `stagnation_runs=6 / underrepresented_families / rotate`；未触发 evict，但 high_growth 已扩到 `281`，下一轮新增前优先补 `momentum_equal_weight_elastic` 或双周/周频代表，不再继续只加 high_growth。
- 下一轮第一条候选命令建议先实现 `aggr_08_92_prom6_core_multifactor_quality_defense` 在 `core_explore_80_20_equal_weight_winner_core` 与 `core_explore_90_10_equal_weight_winner_core` 的等权弹性版本，或一个双周成本候选，然后用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <underrepresented_family_ids>` 补跑。

## 本轮执行计划（2026-05-19 23:14 CST）

- 上一轮 `risk40_mom_exit60_reconfirm65` 等权版成为 official 2017/2020 winner 与 robust，但 `since_2026_01` 仍为负；本轮按 `medium_cycle_growth` 的 2026 防守缺口，增加谨慎仓约束而不扩全量。
- 本轮新增并五窗口确认 2 个 Path 2 base ids：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95` 与 `core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95`。实际命令与 Path 1/3 合并执行：
  `.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_core_multifactor_industry_quality,core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95,core_explore_90_10_total_mv_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm65_caution70_cap95,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap45_hold9_turn06_weekly,core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap50_hold10_turn06_weekly`。
- 新 `caution70` 等权版五窗口 CAGR 为 `33.78% / 55.33% / 53.79% / 92.06% / -14.10%`，总市值版为 `32.83% / 47.78% / 45.75% / 103.20% / -12.72%`；相对上一轮 `reconfirm65` 的 2026 负收益有所收窄，但牺牲 2017/2020/2023 与 2025 弹性，未替换 official robust。
- `scripts/path2_candidate_pass.py` 后 candidate universe 为 `541/541 complete`，五族规模为 `high_concentration_breakout=154 / high_growth_theme=277 / momentum_equal_weight_elastic=19 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=33`；未触发 evict。
- family-ranked raw robust 仍偏向 `risk40_mom_exit60_reconfirm75_caution80`，但 `update_weighted_winners.py` official 口径同步为：2017 `risk40_mom_exit60_reconfirm75_cap95`，2020 `risk40_mom_exit60_reconfirm70_cap95`，2023 `risk50_ma_cap95`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust 为 `risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=61.28% / minCAGR=38.32% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 rotation 为 `stagnation_runs=3 / risk_reconfirm_sensitivity / rotate`；下一轮 focus -> candidates 池优先比较 `risk35/40`、`reconfirm75/80` 与 `caution65/70` 的交互，不继续只加高收益族。建议先实现 `risk35_mom_exit60_reconfirm75_caution70_cap95` 和 `risk40_mom_exit60_reconfirm80_caution70_cap95` 的等权/总市值双底座，并用五窗口 `--only-base-ids` 增量补跑。

## 本轮执行计划（2026-05-19 17:26 CST）

- 本轮沿 `medium_cycle_growth` 新增 3 个高收益参数变体，并对等权/总市值两套底座共 `6` 个 base id 做五窗口 `--only-base-ids` 增量确认：`risk45_mom_exit60_reconfirm70`、`risk40_mom_exit55_reconfirm70`、`risk40_mom_exit60_reconfirm65`。
- `scripts/path2_candidate_pass.py` 后 candidate universe 变为 `536`，五族规模为 `high_concentration_breakout=154 / high_growth_theme=275 / momentum_equal_weight_elastic=19 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=31`。
- 新 `risk40_mom_exit60_reconfirm65` 等权版成为 2017/2020 official winner 与四窗口 robust：2017 `35.89% CAGR / -33.25% MaxDD / 0.97 Sharpe / 3.98 Turn`，2020 `58.60% / -28.34% / 1.24 / 4.49`，2023 `55.88% / -29.20% / 1.28 / 4.19`，2025 `97.78% / -14.29% / 1.78 / 7.39`。
- 其他新变体也有效抬高上限：`risk45_mom_exit60_reconfirm70` 等权版成为 2023 official winner（`57.56% CAGR / -31.31% MaxDD / 1.29 Sharpe / 4.32 Turn`），`risk40_mom_exit55_reconfirm70` 总市值版成为 2025 official winner（`108.88% CAGR / -16.71% MaxDD / 1.83 Sharpe / 6.77 Turn`）。
- 四窗口 official robust candidate 切换为等权 `risk40_mom_exit60_reconfirm65`，`meanCAGR=62.04% / minCAGR=35.89% / worstMaxDD=-33.25% / meanTurn=5.01`；但新高收益族在 `since_2026_01` 均为负（等权约 `-16.78%`、总市值约 `-15.07%`），下一轮要加 2026 风控/确认约束。
- 收尾 rotation 为 `stagnation_runs=1 / medium_cycle_growth / continue`；下一轮第一优先命令应围绕当前 robust 做 `caution/现金防守/恢复确认` 变体的 `--only-base-ids` 增量补跑。

## 本轮执行计划（2026-05-19 11:12 CST）

- 本轮按 `medium_cycle_growth` 轮换方向先做既有候选巡检；`scripts/path2_candidate_pass.py` 继续保持 `524` 个 candidate，五族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=16 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=28`。
- family-ranked raw winners 仍集中在旧中周期高收益原型：2017 `risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `risk40_mom_exit60_reconfirm70`（`58.60%`），2023 `risk50_ma`（`65.59%`），2025 高换手 weekly `cap100_weekly`（`198.70% / 16.79 Turn`）。
- `update_weighted_winners.py` 的 official 口径切回更稳的 Path 1 邻近候选：2017/2020/2025 为 `aggr_05_95_prom7`，2023 为等权 `aggr_10_90_prom6_core_multifactor_balanced`。
- 四窗口 official robust candidate 切换为 `aggr_05_95_prom7`，`meanCAGR=41.87% / minCAGR=22.00% / worstMaxDD=-27.88% / meanTurn=3.19`；raw high-growth 上限继续只作为观察，不直接晋升。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 重置为 `stagnation_runs=0 / medium_cycle_growth / continue`；本轮没有继续扩大 `high_growth_theme` 数量，下一轮按 report quota 优先用中周期高收益原型做风险确认、成本和回撤压测，同时保持五个 family 的代表性。

## 本轮执行计划（2026-05-19 05:29 CST）

- 本轮按 `underrepresented_families` 轮换方向扩展候选池：等权/总市值多因子弹性加入 `aggr_08_92_prom6_core_multifactor_balanced` 与 `aggr_10_90_prom6_core_multifactor_balanced`，双周加入 `cap70/cap50` 两个代表，周频成本压力加入 `cap65_hold5_turn15` 与 `cap60_hold6_turn12`。
- 独立复跑 `scripts/path2_candidate_pass.py` 后，candidate universe 为 `524/524 complete`；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=16 / biweekly_rebalance_aggressive=18 / weekly_rebalance_aggressive=28`。
- family-ranked raw winners 仍集中在旧中周期高收益原型：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.60%`），2023 `1/99 risk50_ma`（`65.59%`），2025 高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`198.70% / 16.79 Turn`）。
- 新双周 `cap70/cap50` 在 2020 窗口约 `10.16%/10.13% CAGR` 且回撤偏深；新增多因子弹性在 official weighted 口径更稳，推动 Path 2 official tracked/robust 同步到 `aggr_10_90_prom6_core_multifactor_balanced`。
- `update_weighted_winners.py` 后 Path 2 official window winners 为：2017 `aggr_10_90_prom6_core_multifactor_balanced`，2020 `aggr_08_92_prom6_core_multifactor_balanced`，2023 `aggr_10_90_prom6_core_multifactor_balanced`，2025 `aggr_08_92_prom6_core_multifactor_balanced`。
- 四窗口 official robust candidate 为 `aggr_10_90_prom6_core_multifactor_balanced`，`meanCAGR=35.95% / minCAGR=14.72% / worstMaxDD=-41.55% / meanTurn=4.03`；raw high-growth 上限继续作为观察，不直接晋升。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 重置为 `stagnation_runs=0 / recommended_focus=medium_cycle_growth / continue`；下一轮继续用中周期高收益原型做确认，而不是再单纯扩大 high_growth 数量。

## 本轮执行计划（2026-05-18 23:13 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，candidate universe 继续为 `516/516 complete`；五个候选族规模保持 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=12 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.60%`），2023 `1/99 risk50_ma`（`65.59%`），2025 高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`198.70% / 16.79 Turn`）。
- candidate-pass raw robust 仍为 `2/98 risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`，继续作为观察，不直接晋升 official。
- `update_weighted_winners.py` 验证后，Path 2 official tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.37% / minCAGR=38.58% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=30 / recommended_focus=underrepresented_families / rotate`；下一轮优先按配额补等权动量、双周与周频代表性，不继续让 high_growth family 单独扩张。

## 本轮执行计划（2026-05-18 20:34 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，candidate universe 继续为 `516/516 complete`；五个候选族规模保持 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=12 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.72%`），2023 `1/99 risk50_ma`（`65.81%`），2025 高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% / 16.33 Turn`）。
- candidate-pass raw robust 仍为 `2/98 risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`，继续作为观察，不直接晋升 official。
- `update_weighted_winners.py` 验证后，Path 2 official tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=28 / recommended_focus=risk_reconfirm_sensitivity / rotate`；下一轮优先比较 `risk40/risk50` 与恢复确认阈值敏感性，同时保持五个 family 不被 high_growth 压扁。

## 本轮执行计划（2026-05-18 11:11 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，candidate universe 继续为 `516/516 complete`；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=12 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.72%`），2023 `1/99 risk50_ma`（`65.81%`），2025 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% / 16.33 Turn`）。
- candidate-pass raw robust 仍为 `2/98 risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`，继续只作为观察，不晋升 official。
- `update_weighted_winners.py` 验证后，Path 2 official tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=23 / recommended_focus=capacity_and_cost_stress / rotate`；下一轮优先做容量、回撤、换手与交易成本压力，不继续只扩 high_growth family。

## 本轮执行计划（2026-05-18 05:53 CST）

- 本轮按 `underrepresented_families` 方向微扩候选池，将 `aggr_08_92_prom6_core_6_1` 与 `aggr_10_90_prom6_core_6_1` 纳入 `momentum_equal_weight_elastic`；独立复跑 `scripts/path2_candidate_pass.py` 后候选宇宙为 `516/516 complete`。
- 五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=12 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`，未继续由单一 high_growth family 压扁。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`58.72%`），2023 `1/99 risk50_ma`（`65.81%`），2025 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% / 16.33 Turn`）。
- `update_weighted_winners.py` 验证后，Path 2 official tracked winners 与 robust candidate 未变；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=20 / recommended_focus=underrepresented_families / rotate`；下一轮继续按配额补等权动量、双周和周频代表性。

## 本轮执行计划（2026-05-17 23:12 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `1/99 risk40_mom_exit60_reconfirm70_caution80`（`58.78%`），2023 `1/99 risk50_ma`（`65.81%`）。
- 2025 raw leader 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% CAGR / -39.39% MaxDD / 16.33 Turn`），但 `update_weighted_winners.py` 继续因 2023 验证窗口不足拒绝其进入 official winner。
- Path 2 official tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 official robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`；candidate-pass raw robust 切到 `2/98 risk40_mom_exit60_reconfirm75_caution80`，作为观察不晋升。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=18 / recommended_focus=underrepresented_families / rotate`；下一轮按配额优先补等权动量、双周与周频代表性，不让 high_growth family 继续压扁候选池。

## 本轮执行计划（2026-05-17 17:25 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 仍为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`）。
- 2025 raw leader 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% CAGR / 16.33 Turn`），但 `update_weighted_winners.py` 继续因验证窗口不足拒绝其进入 official winner。
- Path 2 official tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 为 `pass / blocking=0 / warning=0`，Path 2 rotation 为 `stagnation_runs=15 / recommended_focus=risk_reconfirm_sensitivity / rotate`；下一轮优先做 `risk40/risk50` 再确认阈值敏感性。

## 本轮执行计划（2026-05-17 11:15 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates；五个候选族规模为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 仍集中在中周期高收益原型：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`），2025 raw leader 仍为高换手 weekly `aggr_01_99_prom1...cap100_weekly`（`197.61% / Turn=16.33`）。
- `update_weighted_winners.py` 验证后，2025 weekly raw leader 继续因 2023 验证窗口不足被拒；Path 2 tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- Guard 对 Path 2 candidate universe 为 `513/513 complete / pass`，收尾 rotation 为 `stagnation_runs=12 / recommended_focus=medium_cycle_growth / rotate`。
- 下一轮按 medium-cycle growth 继续扩展和压测中周期高收益原型，同时保持五个 family 的代表性，避免 high_growth family 单独压扁候选池。

## 本轮执行计划（2026-05-17 05:15 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates，五个候选族规模仍为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked raw winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`），2025 仍为高换手纯周频 `aggr_01_99_prom1...cap100_weekly`（`197.61% / Turn=16.33`）。
- `update_weighted_winners.py` 验证后，2025 weekly raw leader 继续因 2023 验证窗口不足被拒；Path 2 tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 对 Path 2 candidate universe 为 `513/513 complete / pass`，rotation 为 `stagnation_runs=10 / recommended_focus=capacity_and_cost_stress / rotate`。
- 下一轮优先做容量、回撤、换手与交易成本压力测试，并按配额继续保留 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive` 的代表性，不让 high_growth family 继续压扁候选池。

## 本轮执行计划（2026-05-16 23:12 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，候选宇宙保持 `513` 个 base candidates，五个候选族继续为 `high_concentration_breakout=154 / high_growth_theme=269 / momentum_equal_weight_elastic=9 / biweekly_rebalance_aggressive=16 / weekly_rebalance_aggressive=25`。
- family-ranked winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`），2025 raw leader 仍为高换手纯周频 `aggr_01_99_prom1...cap100_weekly`（`197.61% / Turn=16.33`）。
- `update_weighted_winners.py` 验证后，2025 weekly raw leader 因 2023 验证窗口不足被拒；Path 2 tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 guard 对 Path 2 candidate universe 为 `513/513 complete / pass`，rotation 为 `stagnation_runs=8 / recommended_focus=underrepresented_families / rotate`。
- 下一轮按配额优先补 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive` 的低代表性族，并继续压紧 family membership 口径。

## 本轮执行计划（2026-05-16 17:14 CST）

- 本轮先用本地 `summary.json` 重建 A 股 comparison 到 `8693` 行，解除 Path 2 coverage `block`；`scripts/path2_candidate_pass.py` 复跑后候选宇宙保持 `513` 个 base candidates。
- 五个候选族继续独立保留：`high_concentration_breakout=154`、`high_growth_theme=269`、`momentum_equal_weight_elastic=9`、`biweekly_rebalance_aggressive=16`、`weekly_rebalance_aggressive=25`；family membership 没有被单一高集中族压扁。
- Path 2 tracked winners 当前为：2017 `90/10 equal_weight risk40_mom_exit60_reconfirm75_cap95`（`38.66% CAGR / -32.76% MaxDD / 1.13 Sharpe / 3.79 Turn`），2020 `90/10 equal_weight risk40_mom_exit60_reconfirm70_cap95`（`58.72% / -28.34% / 1.25 / 4.49`）。
- 2023 winner 为 `90/10 equal_weight risk50_ma_cap95`（`65.81% CAGR / -36.51% MaxDD / 1.33 Sharpe / 4.79 Turn`）；2025 raw weekly 高弹性候选因 2023 验证不足被拒，official winner 仍为 `80/20 total_mv aggr_05_95_prom3_core_6_1_full_risk_cap60`（`143.76% / -17.33% / 2.12 / 5.94`）。
- 四窗口 robust candidate 仍为 `90/10 equal_weight risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 rotation 为 `stagnation_runs=6 / recommended_focus=underrepresented_families / rotate`；下一轮优先补 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive` 等低代表性族，而不是扩大短窗 weekly 爆发族。

## 本轮执行计划（2026-05-16 11:20 CST）

- 本轮先通过缓存重建解除 Path 2 aggregate coverage 的假性 blocking 缺口；最终 guard 对 Path 2 candidate universe 为 `513/513 complete / pass`。
- 独立复跑 `scripts/path2_candidate_pass.py` 后，candidate universe 为 `raw=513 / complete=513 / incomplete=0`，五族规模为 `154 / 269 / 9 / 16 / 25`，继续保持 `100+` 且未被单一 family 压扁。
- family-ranked winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`（`38.70% CAGR`），2020 `2/98 risk40_mom_exit60_reconfirm70`（`59.52%`），2023 `2/98 risk50_ma`（`67.42%`），2025 仍为高换手纯周频 `aggr_01_99_prom1...cap100_weekly`（`197.61% / Turn=16.33`）。
- family-ranked robust 为 `2/98 risk40_mom_exit60_reconfirm75_caution80`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`。
- `update_weighted_winners.py` 验证后 Path 2 tracked winners 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66%`。
- 收尾 rotation 为 `stagnation_runs=2 / recommended_focus=medium_cycle_growth / continue`；下一轮继续优先中周期高收益原型，并保留双周/周频 family 配额。

## 本轮执行计划（2026-05-16 06:56 CST）

- 本轮 guard 开局显示 Path 2 blocking coverage 缺口为 `284` 个，按 rerun commands 离线补跑后降到 `3` 个；已在 `WINNER_CORE_VARIANTS` 中补齐 `aggr_07_93_prom8 / aggr_07_93_prom8_ramp85 / share_12_88_hold_3_7` 三个被候选池引用但不可生成的变体，并复跑确认到 `blocking=0`。
- 重建后的 comparison universe 为 `8613` 行 / `2137` 个 base strategies；Path 2 active universe 为 `raw=513 / complete=513 / incomplete=0`，五族规模为 `154 / 269 / 9 / 16 / 25`，继续保持 `100+` 候选且未被单一 family 完全压扁。
- `path2_candidate_pass.py` 的 family-ranked winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75_caution80`，2020 `2/98 risk40_mom_exit60_reconfirm70`，2023 `2/98 risk50_ma`，2025 短窗 raw leader 仍为高换手纯周频 `aggr_01_99_prom1...cap100_weekly`。
- family-ranked robust 为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_caution80_cap95`，`meanCAGR=64.35% / minCAGR=38.70% / worstMaxDD=-32.85% / meanTurn=4.93`。
- `update_weighted_winners.py` 验证后 Path 2 tracked winners 为：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust 为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=62.76% / minCAGR=38.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 收尾 rotation 为 `stagnation_runs=7 / recommended_focus=underrepresented_families / rotate`；下一轮按每族 `2` 个新增配额优先补 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`，不要继续只扩 high_growth_theme。

## 本轮执行计划（2026-05-15 15:16 CST）

- 本轮独立复跑 `scripts/path2_candidate_pass.py`，family-ranked universe 仍为 `raw=536 / complete=473 / incomplete=63`；五族规模保持 `154 / 229 / 9 / 16 / 25`，候选宇宙继续满足 `100+` 规模且未被单一 high_growth family 压扁。
- `path2_candidate_pass.json` 同步修正了部分历史候选的可用窗口：若干 incomplete 候选已具备 `since_2025_01` 记录，当前主要缺口集中在 `since_2023_01`，不影响 active complete universe。
- family-ranked robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=65.09% / minCAGR=39.27% / worstMaxDD=-32.76% / meanTurn=4.98`。
- `update_weighted_winners.py` 后 tracked Path 2 仍由 `weekly_alpha_pullback` 纯周频族占据；四窗口 robust 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.95% / minCAGR=19.02% / worstMaxDD=-37.64% / meanTurn=6.07`。
- 最终 rotation 为 `stagnation_runs=3 / recommended_focus=risk_reconfirm_sensitivity / rotate`；下一轮应优先围绕 `risk40/risk50` 的再确认阈值与风险降仓敏感性做中周期验证，同时继续复核 Path 2 是否应允许纯周频族主导 tracked 口径。

## 本轮执行计划（2026-05-15 10:14 CST）

- 本轮在修复 aggregate 覆盖后复跑 `scripts/path2_candidate_pass.py`，family-ranked universe 恢复为 `raw=536 / complete=473 / incomplete=63`；五族规模为 `154 / 229 / 9 / 16 / 25`，新增 `weekly_alpha_*` 只扩充单周调仓族，没有压扁高集中、高成长、动量或双周 family。
- family-ranked Path 2 robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm75_cap95`，`meanCAGR=65.09% / minCAGR=39.27% / worstMaxDD=-32.76% / meanTurn=4.98`。
- `update_weighted_winners.py` 的 tracked Path 2 本轮切到纯周频 `weekly_alpha_pullback` 族：2017/2020 robust leg 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，2023 为 `aggr_08_92_prom6_weekly_alpha_pullback_risk50_cap40_hold2_turn40_weekly`，2025 为 `aggr_05_95_prom3_weekly_alpha_pullback_risk50_cap60_hold2_turn30_weekly`。
- weighted Path 2 robust 为 `aggr_03_97_prom2_weekly_alpha_pullback_cashoff_cap80_hold3_turn25_weekly`，`meanCAGR=24.95% / minCAGR=19.02% / worstMaxDD=-37.64% / meanTurn=6.07`；最终 rotation 为 `stagnation_runs=1 / medium_cycle_growth`，下一轮应确认 Path 2 tracked 口径是否继续允许纯周频族主导。

## 本轮执行计划（2026-05-14 22:55 CST）

- 本轮优先修复 guard blocking coverage：Path 2 active universe 的 `since_2025_01` aggregate 缺口已通过阻塞 rerun 与五窗口 `strategy_comparison.csv` 重建补齐，收尾 guard 为 `pass`。
- `path2_candidate_pass.py` 在当前脚本口径下只输出 `candidate_count=1` 的严格候选 shortlist，robust 为 `aggr_10_90_fast_ramp_cash_off`；但 `update_weighted_winners.py` 仍基于完整 comparison universe 更新 Path 2 tracked winners。
- Path 2 tracked winners 已同步为：2017 `2/98 risk40_mom_exit60_reconfirm75`（`39.27% CAGR / -32.76% MaxDD / 1.1468 Sharpe / 3.79 Turn`），2020 `1/99 risk40_mom_exit60_reconfirm70`（`59.78% / -28.34% / 1.2602 / 4.49`），2023 `1/99 risk50_ma`（`67.87% / -36.51% / 1.3606 / 4.79`），2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`（`148.68% / -17.33% / 2.1665 / 5.94`）。
- 四窗口 robust candidate 为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=65.09% / minCAGR=39.27% / worstMaxDD=-32.76% / meanTurn=4.98`；最终 guard 为 `stagnation_runs=1 / recommended_focus=medium_cycle_growth`，下一轮优先处理 candidate-pass family shortlist 过窄的问题，再继续中周期扩展。

## 本轮执行计划（2026-05-14 15:10 CST）

- 本轮起止两次运行研究守卫，收尾 coverage gate 为 `pass`，Path 2 active universe 继续为 `455` 个四窗口完整候选，另有不完整历史候选仅保留追溯；收尾 rotation 为 `stagnation_runs=13 / recommended_focus=medium_cycle_growth`。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，五个 family 规模仍为 `154 / 229 / 9 / 16 / 16`，分别对应高集中突破、高成长主线、动量/等权高弹性、双周调仓高收益、单周调仓高收益；本轮先完成巡检和同步，未新增代码候选。
- raw `since_2025_01` leader 仍是纯周度 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`195.54% CAGR / -40.77% MaxDD / 1.7685 Sharpe / 16.36 Turnover`；验证口径继续因 2023 窗口失效拒绝其进入 Path 2 tracked winner。
- 验证后 Path 2 tracked winners 未换身份：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 最新指标分别为 `39.66% / 60.45% / 69.21% / 154.34% CAGR`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=66.44% / minCAGR=39.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 下一轮按 report quota 每族 `2` 个新增配额推进，优先 `medium_cycle_growth`：在中周期高收益原型上比较更宽退出、低成本确认与不同底座，而不是继续让 high_growth_theme 单独扩张。

## 本轮执行计划（2026-05-14 09:13 CST）

- 本轮起止两次运行研究守卫，收尾 coverage gate 为 `pass`，Path 2 active universe 继续为 `455` 个四窗口完整候选，另有 `23` 个不完整历史候选仅保留追溯；收尾 rotation 为 `stagnation_runs=11 / recommended_focus=capacity_and_cost_stress`。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，五个 family 规模仍为 `154 / 229 / 9 / 16 / 16`，分别对应高集中突破、高成长主线、动量/等权高弹性、双周调仓高收益、单周调仓高收益；本轮没有继续扩大 `high_growth_theme` 邻域。
- raw `since_2025_01` leader 仍是纯周度 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`195.54% CAGR / -40.77% MaxDD / 1.7685 Sharpe / 16.36 Turnover`；验证口径继续因 2023 窗口失效拒绝其进入 Path 2 tracked winner。
- 验证后 Path 2 tracked winners 未换身份：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 最新指标分别为 `39.66% / 60.45% / 69.21% / 154.34% CAGR`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=66.44% / minCAGR=39.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 下一轮按 report quota 每族 `2` 个新增配额，但应先做 `capacity_and_cost_stress`：优先对现有中周期强点做容量、回撤、换手成本压力，而不是继续让高成长主线压扁 family membership。

## 本轮执行计划（2026-05-14 03:17 CST）

- 本轮 guard 覆盖率为 `pass`，Path 2 active universe 继续为 `455` 个四窗口完整候选，另有 `23` 个不完整历史候选仅保留追溯；收盘 guard 将 Path 2 rotation 推进到 `stagnation_runs=9 / recommended_focus=capacity_and_cost_stress`。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，五个 family 规模为 `154 / 229 / 9 / 16 / 16`，分别对应高集中突破、高成长主线、动量/等权高弹性、双周调仓高收益、单周调仓高收益；本轮不继续扩 `high_growth_theme` 邻域。
- raw `since_2025_01` leader 仍是纯周度 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`195.54% CAGR / -40.77% MaxDD / 1.7685 Sharpe / 16.36 Turnover`；验证口径继续因 2023 窗口失效拒绝。
- 验证后 Path 2 tracked winners 未换身份：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 最新指标分别为 `39.66% / 60.45% / 69.21% / 154.34% CAGR`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=66.44% / minCAGR=39.66% / worstMaxDD=-32.76% / meanTurn=4.98`。
- 下一轮新增候选按 report quota 每族 `2` 个优先补 `momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`，并在 `capacity_and_cost_stress` 下约束容量、回撤与换手，避免让高成长主线继续压扁 family membership。

## 本轮执行计划（2026-05-13 21:21 CST）

- 本轮先按 guard 补跑 Path 2 blocking rerun commands；其中 23 个历史候选已不再由当前回测生成器实际产出，因此同步修正 `scripts/path2_candidate_pass.py`：active universe 只纳入四窗口完整候选，并把不完整历史候选写入 `incomplete_candidates` 供追溯。
- 修正后 Path 2 active universe 为 `455`，raw universe 为 `478`，incomplete historical candidates 为 `23`；五个 family 规模为 `154 / 229 / 9 / 16 / 16`，仍保持 `100+` 候选和五族独立观察，未被单一高集中 family 压扁。
- Path 2 raw `since_2025_01` leader 仍是纯周度 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`195.54% CAGR / -40.77% MaxDD / 1.7685 Sharpe / 16.36 Turnover`；验证口径继续因 2023 失效拒绝其进入 Path 2 winner。
- 验证后 Path 2 tracked winners 未换身份：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 `aggr_05_95_prom3_core_6_1_full_risk_cap60`。
- 最新指标分别为 `39.66% / 60.45% / 69.21% / 154.34% CAGR`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=66.44% / minCAGR=39.66% / worstMaxDD=-32.76% / meanTurn=4.98`。rotation 已提示下一轮转向 `underrepresented_families`，优先补强等权动量/双周/周频代表而非继续只扩 high_growth_theme。

## 本轮执行计划（2026-05-13 09:13 CST）

- 本轮复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，候选宇宙继续维持 `478`，五个 family 规模仍为 `159 / 237 / 16 / 16 / 16`；`risk40_mom_exit60_reconfirm*_caution80` 仍只扩充 `high_growth_theme`，没有压扁其他 family。
- raw 扫描的 `since_2025_01` 单窗口 leader 仍是纯周度 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`188.62% CAGR / -40.77% MaxDD / 1.7388 Sharpe / 16.36 Turnover`，但验证口径继续因 2023 窗口失效拒绝进入 Path 2 winner。
- 验证后 Path 2 winner 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，`39.51% CAGR / -32.76% MaxDD / 1.1512 Sharpe / 3.79 Turnover`；2020 `1/99 risk40_mom_exit60_reconfirm70`，`60.26% / -28.34% / 1.2665 / 4.49`。
- 2023 仍为 `1/99 risk50_ma`，`69.00% CAGR / -36.51% MaxDD / 1.3748 Sharpe / 4.79 Turnover`；2025 验证 winner 仍为 `aggr_05_95_prom3_core_6_1_full_risk_cap60`，`151.34% / -17.33% / 2.1910 / 5.94`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=65.89% / minCAGR=39.51% / worstMaxDD=-32.76% / meanTurn=4.98`；下一轮仍优先寻找更适配 2020 的中周期高收益原型，而不是继续追逐短窗周频爆发。

## 本轮执行计划（2026-05-13 03:32 CST）

- 本轮复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，候选宇宙维持 `478`，五个 family 规模仍为 `159 / 237 / 16 / 16 / 16`；`results/strategy_comparison_base_method.csv` 仍保持约 `3407` 条数据行，未再被压缩。
- Path 2 raw 扫描的 `since_2025_01` 单窗口 leader 仍是纯周度 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`，`188.62% CAGR / -40.77% MaxDD / 1.7388 Sharpe / 16.36 Turnover`，但验证口径继续拒绝它进入 Path 2 winner。
- 验证后 Path 2 winner 未变：2017 `2/98 risk40_mom_exit60_reconfirm75`，`39.51% CAGR / -32.76% MaxDD / 1.1512 Sharpe / 3.79 Turnover`；2020 `1/99 risk40_mom_exit60_reconfirm70`，`60.26% / -28.34% / 1.2665 / 4.49`。
- 2023 仍为 `1/99 risk50_ma`，`69.00% CAGR / -36.51% MaxDD / 1.3748 Sharpe / 4.79 Turnover`；2025 验证 winner 仍为 `aggr_05_95_prom3_core_6_1_full_risk_cap60`，`151.34% / -17.33% / 2.1910 / 5.94`。
- 四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=65.89% / minCAGR=39.51% / worstMaxDD=-32.76% / meanTurn=4.98`；下一步仍应优先寻找更适配 2020 的中周期高收益原型，而非继续提高短窗爆发。

## 本轮执行计划（2026-05-12 21:20 CST）

- 本轮先发现当前 `results/strategy_comparison_base_method.csv` 被缩成 `256` 行，会把 Path 2 候选宇宙压到 `30` 个且双周 family 为 `0`；已用本地 `summary.json` 运行 `.venv/bin/python scripts/rebuild_strategy_comparison_csv.py --windows since_2017_01 since_2020_01 since_2023_01 since_2025_01`，恢复到 `3407` 行 / `871` 个 base strategies。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `478`，五个 family 规模为 `159 / 237 / 16 / 16 / 16`；新增或同步的 `risk40_mom_exit60_reconfirm*_caution80` 只扩充 `high_growth_theme`，没有压扁高集中、等权动量、双周或周频 family membership。
- `risk40_mom_exit60_reconfirm75_caution80` 与 `risk40_mom_exit60_reconfirm70_caution80` 没有改写 Path 2 winner：最好 2020 为 `90/10` 等权 `1/99 reconfirm70_caution80`，`58.79% CAGR / -28.34% MaxDD / 1.2651 Sharpe / 4.43 Turnover`，低于当前 `risk40 reconfirm70` 的 `60.26% CAGR`。
- caution80 最好长窗为 `90/10` 等权 `2/98 reconfirm75_caution80`，`38.66% CAGR / -32.85% MaxDD / 1.1502 Sharpe / 3.74 Turnover`，低于当前 `2/98 risk40 reconfirm75` 的 `39.51% / -32.76% / 1.1512 / 3.79`。
- Path 2 验证 winner 仍为：2017 `2/98 risk40_mom_exit60_reconfirm75`，2020 `1/99 risk40_mom_exit60_reconfirm70`，2023 `1/99 risk50_ma`，2025 验证后 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk40_mom_exit60_reconfirm75`，`meanCAGR=65.89% / minCAGR=39.51%`。

## 本轮执行计划（2026-05-12 09:12 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线为 `462` candidates；随后新增 4 个介于旧 `risk30` 与强势 `risk50` 之间的高成长主线原型：`risk40_mom_exit60_reconfirm75` 与 `risk40_mom_exit60_reconfirm70`，覆盖 `1/99`、`2/98`，继续只扩充 `high_growth_theme` family。
- 微批量只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-11`；随后重建 comparison 到 `3375` 行 / `863` 个 base strategies。
- 复跑 Path 2 后候选宇宙增至 `470`，五个 family 规模为 `159 / 229 / 16 / 16 / 16`；新增候选没有压扁高集中、等权动量、双周或周频 family membership。
- 新 `risk40_mom_exit60_reconfirm70` 改写 Path 2 `since_2020_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk40_mom_exit60_reconfirm70_cap95` 达到 `59.29% CAGR / -28.34% MaxDD / 1.2534 Sharpe / 4.49 Turnover`，相对旧 `risk50 reconfirm70` 同时改善收益、回撤、Sharpe 与换手。
- 新 `risk40_mom_exit60_reconfirm75` 改写 Path 2 `since_2017_01` winner 与四窗口 robust candidate：`2/98` 等权版本为 `38.93% CAGR / -32.76% MaxDD / 1.1402 Sharpe / 3.79 Turnover`；robust 为 `meanCAGR=63.44% / minCAGR=38.93% / worstMaxDD=-32.76% / meanTurn=4.98`。
- `since_2023_01 / since_2025_01` 验证后 winner 不变：2023 仍为 `risk50_ma`，2025 仍为验证后的 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；下一轮优先围绕 `risk40` 的退出阈值或谨慎仓，而不是继续单纯放宽恢复确认。

## 本轮执行计划（2026-05-12 03:16 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线为 `454` candidates，随后新增 4 个更适配 `since_2020_01` 的恢复确认放松原型：`risk50_mom_exit60_reconfirm70` 与 `risk50_mom_exit60_reconfirm65`，覆盖 `1/99`、`2/98`，继续只扩充 `high_growth_theme` family。
- 微批量只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-11`；随后重建 comparison 到 `3343` 行 / `855` 个 base strategies。
- 复跑 Path 2 后候选宇宙增至 `462`，五个 family 规模为 `159 / 221 / 16 / 16 / 16`；新增候选只扩充 `high_growth_theme`，没有压扁高集中、等权动量、双周或周频 family membership。
- 新 `reconfirm70` 改写 Path 2 `since_2020_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm70_cap95` 达到 `58.76% CAGR / -33.08% MaxDD / 1.2319 Sharpe / 4.71 Turnover`，相对旧 `risk50_mom` 同时改善收益、回撤与 Sharpe，换手小幅升高。
- 新 `reconfirm65` 更偏长窗，但未改写长窗 winner：最好长窗为 `90/10` 等权 `2/98 reconfirm65`，`37.51% CAGR / -39.15% MaxDD / 0.9958 Sharpe / 4.12 Turnover`，仍低于当前 `2/98 reconfirm75` 的 `38.67% / -38.80% / 1.1164 / 3.96`。
- `since_2017_01 / since_2023_01 / since_2025_01` 验证后 winner 不变；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60_reconfirm75`，`meanCAGR=63.93% / minCAGR=38.67% / worstMaxDD=-38.80% / meanTurn=5.13`。

## 本轮执行计划（2026-05-11 21:22 CST）

- 本轮复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，并新增 4 个独立高成长主线原型：`risk50_mom_exit60_reconfirm75_caution80` 与 `risk50_mom_exit60_reconfirm75_caution75`，覆盖 `1/99`、`2/98`，继续只扩充 `high_growth_theme` family。
- 微批量只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-11`；随后重建 comparison 到 `3311` 行 / `847` 个 base strategies。
- 复跑 Path 2 后候选宇宙增至 `454`，五个 family 规模为 `159 / 213 / 16 / 16 / 16`；family membership 未被新高集中候选压扁。
- 新 `reconfirm75_caution` 组合没有改写 Path 2 winner：最好 2020 候选为 `90/10` 等权 `1/99 caution80`，`51.03% CAGR / -36.89% MaxDD / 1.1948 Sharpe / 4.55 Turnover`，低于当前 `risk50_mom` 的 `55.60% / -36.55% / 1.2050 / 4.65`。
- 长窗最好为 `90/10` 等权 `2/98 caution80`，`38.11% CAGR / -38.88% MaxDD / 1.1194 Sharpe / 3.91 Turnover`，接近但仍低于当前 `reconfirm75` 长窗 winner 的 `38.67% / -38.80% / 1.1164 / 3.96`。
- 短窗 side observation：总市值 `2/98 caution80` 在 `since_2025_01` 达到约 `124.95% / -16.13% / 2.0428 / 6.73`，但低于验证后的 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60_reconfirm75`，`meanCAGR=63.93% / minCAGR=38.67% / worstMaxDD=-38.80% / meanTurn=5.13`。

## 本轮执行计划（2026-05-11 15:15 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线为 `438` candidates，随后新增 4 个独立风险时点原型：`risk50_mom_exit60_caution80` 与 `risk50_mom_exit60_caution75`，覆盖 `1/99`、`2/98`。
- 微批量只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`；随后用本地 summary 缓存重建 comparison 到 `3267` 行 / `833` 个 base strategies。
- 复跑 Path 2 后候选宇宙增至 `446`，五个 family 规模为 `159 / 205 / 16 / 16 / 16`；新增候选只扩充 `high_growth_theme`，没有压扁其他 family membership。
- 新 `exit60_caution` 组合没有改写 Path 2 winner：最好 2020 候选为 `90/10` 等权 `1/99 risk50_mom_exit60_caution80`，`54.03% CAGR / -36.43% MaxDD / 1.1991 Sharpe / 4.69 Turnover`，低于当前 `risk50_mom` 的 `55.60% / -36.55% / 1.2050 / 4.65`。
- 长窗最好为 `90/10` 等权 `2/98 risk50_mom_exit60_caution80`，`36.52% CAGR / -40.22% MaxDD / 0.9945 Sharpe / 4.02 Turnover`，低于当前 `reconfirm75` 长窗 winner 的 `38.67% / -38.80% / 1.1164 / 3.96`。
- 短窗 side observation：总市值 `2/98 caution80` 在 `since_2025_01` 达到 `114.94% / -16.13% / 1.9286 / 6.75`，但低于验证后的 `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60_reconfirm75`，`meanCAGR=63.93% / minCAGR=38.67% / worstMaxDD=-38.80% / meanTurn=5.13`。

## 本轮执行计划（2026-05-11 09:19 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线为 `430` candidates，五个 family 规模为 `159 / 189 / 16 / 16 / 16`，窗口强点仍集中在 `risk50_mom_exit60 / risk50_mom / risk50_ma`。
- 新增 4 个独立恢复确认原型：`risk50_mom_exit60_reconfirm75_cap95` 与 `risk50_mom_exit60_reconfirm80_amt110_cap95`，覆盖 `1/99`、`2/98`；只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3235` 行 / `825` 个 base strategies；复跑 Path 2 后候选宇宙增至 `438`，五个 family 规模为 `159 / 197 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新 `reconfirm75` 改写 Path 2 `since_2017_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm75_cap95` 达到 `38.67% CAGR / -38.80% MaxDD / 1.1164 Sharpe / 3.96 Turnover`。
- 四窗口 robust candidate 同步切到同一 `2/98 reconfirm75`，`meanCAGR=63.93% / minCAGR=38.67% / worstMaxDD=-38.80% / meanTurn=5.13`；相对旧 `exit60`，长窗收益、Sharpe、回撤与换手均小幅改善。
- `since_2020_01 / since_2023_01 / since_2025_01` 验证后 winner 不变：新候选最佳 2020 为 `1/99 reconfirm75` 的 `51.59% / -36.99% / 1.1971 / 4.61`，低于当前 `risk50_mom` 的 `55.60%`；`reconfirm80_amt110` 过严，最好 2020 等权仅约 `31.30% CAGR`，下一轮不应继续单纯加严确认阈值。

## 本轮执行计划（2026-05-11 03:13 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍为 `422` candidates，五个 family 规模为 `159 / 181 / 16 / 16 / 16`，窗口 winner 继续由 `risk50_mom_exit60 / risk50_mom / risk50_ma` 占据。
- 新增 4 个独立量价晋升阈值原型：`risk50_mom_top12` 与 `risk50_mom_top18`，覆盖 `1/99`、`2/98`；只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3203` 行 / `817` 个 base strategies；复跑 Path 2 后候选宇宙增至 `430`，五个 family 规模为 `159 / 189 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新阈值没有改写 Path 2 winner：最好 2020 候选为 `90/10` 等权 `1/99 risk50_mom_top12`，`46.19% CAGR / -36.26% MaxDD / 0.9698 Sharpe / 4.88 Turnover`，收益与 Sharpe 均低于当前 `risk50_mom`。
- 主要 side observation 是 `top18` 偏向短窗：`90/10` 等权 `1/99 risk50_mom_top18` 在 `since_2023_01` 为 `63.08% CAGR / -33.34% MaxDD / 1.3521 Sharpe / 4.41 Turnover`，`since_2025_01` 为 `100.23% / -14.30% / 1.8119 / 7.39`，但 2020 窗口降到 `37.47% CAGR`，不足以替换。
- Path 2 tracked winners 仍为：`since_2017_01` 的 `90/10` 等权 `2/98 risk50_mom_exit60`、`since_2020_01` 的 `90/10` 等权 `1/99 risk50_mom`、`since_2023_01` 的 `90/10` 等权 `1/99 risk50_ma`、验证后的 `since_2025_01` `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60`，`meanCAGR=63.07% / minCAGR=37.18% / worstMaxDD=-40.14% / meanTurn=5.17`。

## 本轮执行计划（2026-05-10 21:14 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍为 `414` candidates，五个 family 规模为 `159 / 173 / 16 / 16 / 16`，窗口 winner 继续由 `risk50_mom_exit60 / risk50_mom / risk50_ma` 占据。
- 新增 4 个独立风险节奏原型：`risk50_mom_caution70` 与 `risk50_mom_caution60`，覆盖 `1/99`、`2/98`；只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3171` 行 / `809` 个 base strategies；复跑 Path 2 后候选宇宙增至 `422`，五个 family 规模为 `159 / 181 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新谨慎仓没有改写 Path 2 winner：最好 2020 候选为 `90/10` 等权 `1/99 risk50_mom_caution70`，`52.79% CAGR / -36.76% MaxDD / 1.2114 Sharpe / 4.53 Turnover`，Sharpe 略好但收益低于当前 `risk50_mom` 且回撤略差。
- 主要 side observation 是 2023 窗口：`90/10` 等权 `1/99 risk50_mom_caution70` 为 `61.64% CAGR / -33.36% MaxDD / 1.3678 Sharpe / 4.36 Turnover`，比当前 `risk50_ma` 更稳但收益不足以替换；`caution60` 进一步降收益，只改善局部 Sharpe。
- Path 2 tracked winners 仍为：`since_2017_01` 的 `90/10` 等权 `2/98 risk50_mom_exit60`、`since_2020_01` 的 `90/10` 等权 `1/99 risk50_mom`、`since_2023_01` 的 `90/10` 等权 `1/99 risk50_ma`、验证后的 `since_2025_01` `aggr_05_95_prom3_core_6_1_full_risk_cap60`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60`，`meanCAGR=63.07% / minCAGR=37.18% / worstMaxDD=-40.14% / meanTurn=5.17`。

## 本轮执行计划（2026-05-10 15:04 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍由 `risk50_mom_exit60 / risk50_mom / risk50_ma` 占据；随后新增 4 个独立过滤原型，而不是继续单纯收紧晋升保留 exit 阈值。
- 新增原型为 `risk50_mom_confirm75` 与 `risk50_mom_confirm80_amt110`，覆盖 `1/99`、`2/98`，只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3139` 行 / `801` 个 base strategies；复跑 Path 2 后候选宇宙增至 `414`，五个 family 规模为 `159 / 173 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新过滤没有改写 Path 2 winner：`confirm75` 最好的 2020 候选为 `90/10` 等权 `1/99`，`52.16% CAGR / -37.21% MaxDD / 1.2070 Sharpe / 4.52 Turnover`，收益低于现 `risk50_mom` 且回撤略差。
- `confirm80_amt110` 能把长窗回撤压到约 `-35.60%`，最好的长窗候选为 `90/10` 等权 `2/98`，`33.73% CAGR / -35.60% MaxDD / 1.0221 Sharpe / 3.76 Turnover`，但 2020 窗口降到约 `39.18% CAGR`，不足以替换。
- Path 2 tracked winners 仍为：`since_2017_01` 的 `90/10` 等权 `2/98 risk50_mom_exit60`、`since_2020_01` 的 `90/10` 等权 `1/99 risk50_mom`、`since_2023_01` 的 `90/10` 等权 `1/99 risk50_ma`；四窗口 robust candidate 仍为 `2/98 risk50_mom_exit60`，`meanCAGR=63.07% / minCAGR=37.18% / worstMaxDD=-40.14% / meanTurn=5.17`。
- `update_weighted_winners.py` 的验证口径同步修正 Path 2 `since_2025_01` tracked winner 为 `aggr_05_95_prom3_core_6_1_full_risk_cap60`，`147.28% CAGR / -17.33% MaxDD / 2.1530 Sharpe / 5.94 Turnover`；短窗纯周度爆发候选仍保留在候选宇宙，但不再作为验证后的 Path 2 窗口 winner。

## 本轮执行计划（2026-05-10 09:17 CST）

- 本轮先复跑 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍为 `398` candidates，五个 family 规模为 `159 / 157 / 16 / 16 / 16`；随后围绕当前强点 `90/10 risk50_mom` 增加 `exit80 / exit60` 晋升保留阈值微批量。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit80_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95`；只跑 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座四窗口，并固定 `--end-date 2026-05-08`。
- 微批量后用本地 summary 缓存重建 comparison 到 `3107` 行 / `793` 个 base strategies；复跑 Path 2 后候选宇宙扩为 `406`，五个 family 规模为 `159 / 165 / 16 / 16 / 16`，新增候选只扩充 `high_growth_theme`。
- 新 `exit60` 改写 Path 2 `since_2017_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_cap95` 达到 `37.18% CAGR / -40.14% MaxDD / 0.9855 Sharpe / 4.06 Turnover`；相对旧 `risk50_mom` 长窗提高收益与 Sharpe，但回撤和换手略变差。
- `since_2020_01` winner 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；新增 `exit60` 在 2020 窗口约 `54.99% CAGR / -36.33% MaxDD / 1.1953 Sharpe / 4.74 Turnover`，回撤小幅改善但收益和 Sharpe 不足以替换。
- `since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`；`since_2025_01` 仍为纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`。
- 四窗口 robust candidate 切到 `90/10` 等权 `2/98 risk50_mom_exit60`，`meanCAGR=63.07% / minCAGR=37.18% / worstMaxDD=-40.14% / meanTurn=5.17`；下一轮不要只继续收紧晋升保留阈值，应优先寻找能保住 2020 收益同时降低长窗回撤的独立过滤或风险时点。

## 本轮执行计划（2026-05-10 03:16 CST）

- 本轮先独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，发现全局 `sample_end=2026-05-08` 过滤会把真实双周信号点仍在 `2026-04-30` 的候选误删；已修正 `scripts/path2_candidate_pass.py`，改为保留每个策略/窗口自身最新记录，避免混淆数据截止日与调仓/信号生效日。
- 针对高频 family 额外补跑 6 个双周与 4 个周频代表候选，并用 `.venv/bin/python scripts/rebuild_strategy_comparison_csv.py --windows since_2017_01 since_2020_01 since_2023_01 since_2025_01` 重建 comparison；复跑 Path 2 后候选宇宙恢复为 `398`。
- 五个 family 规模恢复为 `159 / 157 / 16 / 16 / 16`，`biweekly_rebalance_aggressive` 与 `weekly_rebalance_aggressive` 不再被当前最新周频 `sample_end` 压扁。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `2/98 risk50_mom`，`meanCAGR=63.47% / minCAGR=35.88% / worstMaxDD=-39.17% / meanTurn=5.09`。

## 本轮执行计划（2026-05-09 21:14 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙保持 `398`，五个 family 规模继续为 `159 / 157 / 16 / 16 / 16`，family membership 未被高集中候选压扁。
- 本轮不继续简单抬高风险保留仓位，也不继续 `risk50_or` 的 cap/ramp/exit 邻域；当前研究基线仍聚焦 `90/10` 等权 `risk50_mom / risk50_ma` 三档择时线的回撤压缩。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-09 18:09 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙保持 `398`，五个 family 规模继续为 `159 / 157 / 16 / 16 / 16`，family membership 未被高集中候选压扁。
- 本轮不继续简单抬高风险保留仓位，也不继续 `risk50_or` 的 cap/ramp 邻域；当前研究基线仍聚焦 `90/10` 等权 `risk50_mom / risk50_ma` 三档择时线的回撤压缩。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-09 13:04 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙保持 `398`，五个 family 规模为 `159 / 157 / 16 / 16 / 16`，family membership 仍未被高集中候选压扁。
- 本轮不继续简单抬高风险保留仓位，也不继续 `risk50_or` 的 cap/ramp 邻域；当前研究基线继续聚焦 `90/10` 等权 `risk50_mom / risk50_ma` 三档择时线的回撤压缩。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-09 05:08 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙从上轮记录的 `374` 同步为 `398`，五个 family 规模为 `159 / 157 / 16 / 16 / 16`，新增可识别候选主要扩充 `high_growth_theme`，family membership 仍未被高集中候选压扁。
- 本轮不继续简单抬高风险保留仓位，也不继续 `risk50_or` 的 cap/ramp 邻域；当前研究基线继续聚焦 `90/10` 等权 `risk50_mom / risk50_ma` 三档择时线的回撤压缩。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`，`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`，`55.60% CAGR / -36.55% MaxDD / 1.2050 Sharpe / 4.65 Turnover`；`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`，`67.06% / -36.51% / 1.3498 / 4.79`。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`181.26% CAGR / -40.77% MaxDD / 1.6970 Sharpe / 16.50 Turnover`；四窗口 robust candidate 仍为 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-08 23:12 CST）

- 本轮独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙保持 `374`，五个 family 规模为 `159 / 149 / 16 / 16 / 16`，family membership 未被高集中候选压扁。
- 本轮不继续简单抬高三档风险保留仓位，也不新增 `risk50_or` 的 cap/ramp 邻域；先把 17:24 已修正的 `risk50_mom / risk50_ma` 三档择时口径作为当前基线复核。
- Path 2 四窗口 winner 身份未漂移：`since_2017_01` 仍为 `90/10` 等权 `2/98 risk50_mom`（`35.88% CAGR / -39.17% MaxDD / 0.9458 Sharpe / 3.87 Turnover`）。
- `since_2020_01` 仍为 `90/10` 等权 `1/99 risk50_mom`（`55.60% / -36.55% / 1.2050 / 4.65`），`since_2023_01` 仍为 `90/10` 等权 `1/99 risk50_ma`（`67.06% / -36.51% / 1.3498 / 4.79`）。
- `since_2025_01` 继续由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出（`181.26% / -40.77% / 1.6970 / 16.50`）；四窗口 robust candidate 仍是 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.68% / minCAGR=35.83% / worstMaxDD=-39.14% / meanTurn=5.08`。

## 本轮执行计划（2026-05-08 17:24 CST）

- 基线复跑后发现 `negative_mom / below_ma` 风控别名与月频 `risk_staging_mode` 未真正进入 `compute_market_exposure()`；本轮修正别名映射，并把月频回测接入三档风险暴露参数，避免 `risk50_mom / risk50_ma` 与旧两档口径混同。
- 本轮先跑 24-base timing batch，再在修正后公平复跑 12-base `risk50_or / risk50_mom / risk50_ma` 对照，覆盖 `90/10 equal_weight` 与 `90/10 total_mv` 两个底座、四个跟踪窗口，并固定 `--end-date 2026-05-07`。
- 重建 comparison 后为 `2979` 行 / `761` 个 base strategies；复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后候选宇宙升至 `374`，五个 family 规模为 `159 / 149 / 16 / 16 / 16`，新增三档择时候选归入 `high_growth_theme`。
- 新三档动量候选改写 `since_2017_01` 与 `since_2020_01` winner：`90/10` 等权 `2/98 risk50_mom` 长窗达到 `35.95% CAGR / -39.17% MaxDD / 0.9471 Sharpe / 3.87 Turnover`；`1/99 risk50_mom` 在 2020 窗口达到 `55.72% CAGR / -36.55% MaxDD / 1.2068 Sharpe / 4.65 Turnover`。
- `since_2023_01` 改写为 `90/10` 等权 `1/99 risk50_ma`，`67.32% CAGR / -36.51% MaxDD / 1.3533 Sharpe / 4.79 Turnover`；`since_2025_01` 仍由纯周度短窗候选 `aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly` 胜出，`172.51% CAGR / -40.77% MaxDD / 1.6610 Sharpe / 16.50 Turnover`。
- 四窗口 robust candidate 切到 `90/10` 等权 `1/99 risk50_mom`，`meanCAGR=63.95% / minCAGR=35.90% / worstMaxDD=-39.14% / meanTurn=5.08`；下一轮优先研究这条三档动量线的回撤压缩，而不是继续简单提高风险保留仓位。

## 本轮执行计划（2026-05-08 13:15 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `348`；本轮不继续提高核心占比，也不继续拆 `risk30/risk50` 触发器，而是在当前 `90/10` 等权 `risk50_or` 2020 winner 上测试独立 drawdown-control 分支。
- 新增 4 个显式原型：`risk50_or_cap80`、`risk50_or_cap70`、`risk50_or_ramp85_cap95`、`risk50_or_ramp70_cap95`；只跑 `core_explore_90_10_equal_weight_winner_core` 与 `core_explore_90_10_total_mv_winner_core` 两个底座四窗口，并固定 `--end-date 2026-04-30`。
- 微批量后用本地 summary 缓存重建 comparison 到 `2907` 行 / `743` 个 base strategies；复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后候选宇宙升至 `356`，五个 family 规模为 `159 / 131 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`。
- 新候选没有改写 Path 2 tracked winners 或四窗口 robust candidate。当前 `since_2020_01` winner 仍是 `core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95`，`48.41% CAGR / -37.10% MaxDD / 1.1875 Sharpe / 4.38 Turnover`。
- 最好的新 2020 候选是等权 `risk50_or_cap80`：`48.12% CAGR / -37.10% MaxDD / 1.1917 Sharpe / 4.37 Turnover`；等权 `cap70` 为 `47.78% CAGR / -37.10% MaxDD / 1.1955 Sharpe / 4.35 Turnover`，Sharpe 略好但没有降低回撤且收益低于 winner。
- 首月 ramp 控制在当前缓存下与原 `cap95` 结果基本重合，未提供独立降回撤效果；下一轮不要继续在 `risk50_or` 上做简单 cap/ramp 微调，应转向真正不同的风险时点或候选来源过滤。

## 本轮执行计划（2026-05-08 07:28 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `340`；本轮不继续拆 `risk30/risk50` 触发器，新增 `core_explore_90_10` 与 `core_explore_95_05` 两个核心/探索组合底座，围绕当前强点 `promo_liqmom_top15` 跑 `risk50_or` 与 `risk30_or` 的等权/总市值对照。
- 微批量覆盖 8 个 base candidates、四个跟踪窗口，并固定 `--end-date 2026-04-30`；随后用本地 summary 缓存按四窗口重建 comparison 到 `2875` 行 / `735` 个 base strategies。
- 重建后复跑 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `348`，五个 family 规模为 `159 / 123 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`，family membership 未被高集中候选压扁。
- 新 `90/10` 等权 `risk50_or` 改写 Path 2 `since_2020_01` winner：`core_explore_90_10_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95` 达到 `48.41% CAGR / -37.10% MaxDD / 1.1875 Sharpe / 4.38 Turnover`，高于旧 `80/20` 等权 `risk50_or` 的 `47.48% CAGR`，但回撤与换手仍偏高。
- 结构对照里最均衡的新候选是 `90/10` 等权 `risk30_or`：`46.11% CAGR / -26.63% MaxDD / 1.2174 Sharpe / 3.86 Turnover`，未改写 winner 但继续证明降仓 30% 分支更稳。
- `since_2017_01 / since_2023_01 / since_2025_01` winners 与四窗口 robust candidate 未改写；下一轮不要继续单纯提高核心占比，可考虑在 `90/10 risk50_or` 上找降低回撤的独立约束。

## 本轮执行计划（2026-05-07 23:12 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `332`；本轮不继续 `risk50_or` 退出阈值微调，新增 4 个 `promo_liqmom_top15 risk30` 风控触发拆分原型：`risk30_mom` 与 `risk30_ma`，覆盖 `1/99` 与 `2/98`。
- 微批量只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口，并固定 `--end-date 2026-04-30`；随后用本地 summary 缓存重建 comparison 到 `2843` 行 / `727` 个 base strategies。
- 重建后复跑 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `340`，五个 family 规模为 `159 / 115 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`，family membership 未压扁。
- 新触发拆分没有改写 Path 2 tracked winner 或四窗口 robust candidate。`since_2020_01` winner 仍是等权 `risk50_or 1/99`，`47.48% CAGR / -36.36% MaxDD / 1.2388 Sharpe / 4.29 Turnover`。
- 新候选中最好的是等权 `1/99 risk30_mom/risk30_ma`，`since_2020_01` 为 `44.82% CAGR / -26.53% MaxDD / 1.2612 Sharpe / 3.78 Turnover`，与旧 `risk30_or` 结果完全重合；当前本地缓存下动量负值与跌破均线触发没有提供新的择时差异。
- `since_2023_01` 新候选最高为 `47.10% CAGR / -24.59% MaxDD / 1.3340 Sharpe`，仍低于当前 2023 winner；下一轮不要继续拆分同一 `risk30` 风控触发，应回到独立的 2020 中周期信号或组合结构。

## 本轮执行计划（2026-05-07 11:10 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `324`；本轮新增 4 个当前 `risk50_or` 强点的退出阈值原型：`risk50_or_exit80` 与 `risk50_or_exit60`，覆盖 `1/99` 与 `2/98`。
- 微批量只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口，并固定 `--end-date 2026-04-30`；随后用本地 summary 缓存重建 comparison 到 `2811` 行 / `719` 个 base strategies。
- 重建后复跑 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `332`，五个 family 规模为 `159 / 107 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`，family membership 未压扁。
- 新退出阈值没有改写 Path 2 tracked winner 或四窗口 robust candidate。`since_2020_01` winner 仍是等权 `risk50_or 1/99`，`46.78% CAGR / -36.36% MaxDD / 1.2198 Sharpe / 4.27 Turnover`。
- 最好的新候选是等权 `1/99 risk50_or_exit60`：`since_2020_01` 为 `46.25% CAGR / -36.16% MaxDD / 1.2095 Sharpe / 4.35 Turnover`，只小幅改善回撤但收益、Sharpe、换手均弱于现 winner。
- 新候选的 `since_2023_01` 最好为 `52.99% CAGR / -31.82% MaxDD / 1.3261 Sharpe`，仍低于当前 2023 winner `57.19% CAGR`；`since_2017_01` 最好为 `30.35% CAGR`，未超过当前长窗 winner。
- 下一轮不要继续单纯收紧 `risk50_or` 的退出阈值；应回到独立的 2020 中周期信号或更明确的风险时点，而不是继续在同一风险/退出参数邻域内微调。

## 本轮执行计划（2026-05-07 05:06 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `316`；本轮新增 4 个 `risk30_exit60` 恢复/再晋升确认原型，跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口，并固定 `--end-date 2026-04-30`。
- 重建 comparison 后为 `2779` 行 / `711` 个 base strategies；复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后候选宇宙升至 `324`，五个 family 规模为 `159 / 99 / 16 / 16 / 16`，新增候选全部归入 `high_growth_theme`，family membership 未压扁。
- 新恢复确认原型没有改写 Path 2 tracked winner 或 robust candidate。`since_2020_01` winner 仍是等权 `risk50_or 1/99`，`46.78% CAGR / -36.36% MaxDD / 1.2198 Sharpe / 4.27 Turnover`。
- 最好的新 `reconfirm75` 等权候选在 `since_2020_01` 只有 `36.79% CAGR / -31.51% MaxDD / 1.0632 Sharpe / 3.66 Turnover`，明显低于旧 `risk30_exit60` 的 `44.30% CAGR`。
- 更严格的 `reconfirm80_amt110` 能把等权 `since_2023_01` 回撤压到约 `-21.22%~-21.37%`，但 `since_2020_01` 只剩约 `29.82%~29.85% CAGR`，不适合作为 2020 主攻线；下一轮不要继续加严同类再晋升确认。

## 本轮执行计划（2026-05-06 23:15 CST）

- 基线复跑前先用缓存 summary 重建 comparison，避免压缩 CSV 导致 Path 2 只识别少量候选；重建后基线为 `308` candidates，五个 family 规模为 `159 / 83 / 16 / 16 / 16`。
- 本轮围绕上轮的 `risk30` 更均衡 side observation 增加晋升核心退出阈值 hook：`promoted_core_sell_exit_percentile`，默认值仍为 `1.0`，旧策略行为不变。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit80_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_exit60_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口，并固定 `--end-date 2026-04-30`；随后重建 comparison 到 `2747` 行 / `703` 个 base strategies。
- 复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后候选宇宙升至 `316`，五个 family 规模为 `159 / 91 / 16 / 16 / 16`；新增候选全部归入 `high_growth_theme`，family membership 未压扁。
- 新退出阈值没有改写 Path 2 tracked winner 或 robust candidate。最佳新候选为等权 `1/99 risk30_exit60`：`since_2020_01` 为 `44.30% CAGR / -26.37% MaxDD / 1.2498 Sharpe / 3.85 Turnover`，收益低于现有 `risk50_or` winner 的 `46.78%`，但回撤和 Sharpe 更均衡。
- `since_2023_01` 上新候选最高约 `45.81% CAGR / -24.59% MaxDD / 1.3075 Sharpe`，仍低于当前 2023 winner 的 `57.19% CAGR`；下一轮优先比较 `risk30_exit60` 的恢复确认/再晋升条件，而不是继续收紧同一个退出阈值。

## 本轮执行计划（2026-05-06 11:35 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，旧口径为 `299` candidates，五个 family 规模为 `159 / 75 / 16 / 16 / 16`，四窗口 tracked winners 与 robust candidate 未漂移。
- 本轮不继续扩 `top10/top20` 或单纯提高风险保留仓位；围绕当前 `since_2020_01` winner 的 `promo_liqmom_top15` 测试更早触发的 `or` 风险规则，新增 `risk30_or` 与 `risk50_or` 两档，覆盖 `1/99` 与 `2/98` 两个进攻配比。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk30_or_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_or_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量，并固定 `--end-date 2026-04-30`；随后用缓存 summary 重建 comparison 到 `2715` 行 / `695` 个 base strategies。
- 重建后复跑 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `308`，五个 family 规模为 `159 / 83 / 16 / 16 / 16`，新增候选归入 `high_growth_theme`，family membership 未压扁。
- 新 `or` 风险触发没有改写 Path 2 tracked winner 或四窗口 robust candidate；`since_2020_01` winner 仍是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95`（`46.78% CAGR / -36.36% MaxDD / 1.2198 Sharpe / 4.27 Turnover`）。
- 新候选的有效 side observation：等权 `risk50_or 1/99` 在 `since_2023_01` 达到 `54.98% CAGR / -31.82% MaxDD / 1.3582 Sharpe / 4.09 Turnover`，但仍低于当前 2023 winner `58.20% CAGR`；等权 `risk30_or 1/99` 在 2020 为 `44.82% CAGR / -26.53% MaxDD / 1.2612 Sharpe / 3.78 Turnover`，继续是更均衡的下一轮风险节奏对照。
- `since_2017_01`、`since_2023_01`、`since_2025_01` 与四窗口 robust candidate 均未改写；下一轮应比较 `risk30` 的退出/恢复确认，而不是继续增加 `risk50` 同义规则。

## 本轮执行计划（2026-05-06 06:14 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，旧口径为 `292` candidates，五个 family 规模为 `159 / 67 / 16 / 16 / 16`，旧 tracked winners 与 robust candidate 未漂移。
- 本轮不继续 `top10/top20` 阈值宽窄邻域，改为围绕当前 `since_2020_01` winner 的 `promo_liqmom_top15` 做风险节奏微批量：新增 `risk30` 与 `risk50` 两档熊市保留仓位，覆盖 `1/99` 与 `2/98` 两个进攻配比。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk30_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量，并固定 `--end-date 2026-04-30`；随后用缓存 summary 重建 comparison 到 `2029` 行 / `684` 个 base strategies。
- 重建后运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `299`，五个 family 规模为 `159 / 75 / 16 / 16 / 16`，新增候选仍归入 `high_growth_theme`。
- 新 `risk50` 等权 `1/99` 改写 `since_2020_01` Path 2 winner：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_risk50_cap95` 达到 `46.78% CAGR / -36.36% MaxDD / 1.2198 Sharpe / 4.27 Turnover`，相对旧 top15 winner 的 `37.38% / -22.51% / 1.2283 / 3.22` 明显提高收益但显著放大回撤与换手。
- `risk30` 等权 `1/99` 作为更保守 side observation：`44.82% CAGR / -26.53% MaxDD / 1.2612 Sharpe / 3.78 Turnover`，收益低于 `risk50` winner，但回撤和 Sharpe 更平衡，值得下一轮围绕退出/降仓节奏继续比较。
- `since_2017_01`、`since_2023_01`、`since_2025_01` 与四窗口 robust candidate 未改写；robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`。

## 本轮执行计划（2026-05-06 00:04 CST）

- 基线先独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，确认五个 family 的 membership 与旧 tracked winners 是否漂移。
- 本轮优先围绕上轮新改写 `since_2020_01` winner 的 `promo_liqmom_top15` 做窄阈值邻域，不回到 `midcycle_momentum / industry_trend / core_theme` 等已验证偏弱路线。
- 候选继续归入 `high_growth_theme` family，用来测试晋升来源阈值是否能进一步改善 2020，同时避免高集中 family 被同一批候选压扁。
- 若新增候选未明确改写 Path 2 四窗口 winner 或四窗口 robust candidate，只记录扫描结果，不强行同步为 winner。
- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `284`，五个 family 规模为 `159 / 59 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 未漂移。
- 新增 4 个显式原型：`aggr_01_99_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top10_cash_off_and_cap95`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top20_cash_off_and_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；首次默认跑到本地当前日后，立即用 `--end-date 2026-04-30` 覆盖同一批结果，保持与现有 comparison 口径一致。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2651` 行 / `679` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `292`，五个 family 规模为 `159 / 67 / 16 / 16 / 16`。
- 新 top10/top20 邻域没有改写 Path 2 tracked winner 或 robust candidate；`since_2020_01` winner 仍是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95`（`37.38% CAGR / -22.51% MaxDD / 1.2283 Sharpe / 3.22 Turnover`）。
- 新邻域中 `top20` 在 `since_2025_01` 有较强 side observation（总市值 `2/98` 为 `149.97% CAGR / -12.37% MaxDD / 2.2204 Sharpe`），但仍低于当前 `confirm80` 短窗 winner；下一轮不要继续只做 topN 宽窄阈值，应转向组合持有/退出或风险节奏。

## 本轮补充计划与记录（2026-05-05 18:16 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `276`，五个 family 规模为 `159 / 51 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不继续 `confirm / ramp / cadence / core_theme / industry_trend / midcycle_momentum` 简单邻域，新增 `promotion_signal_mode` hook：默认逻辑保持不变，仅新候选可把晋升排序切到 `momentum_6_1` 或 `liquidity_momentum`，并用 `standard_promotion_percentile` 限制标准晋升池。
- 新增 4 个显式原型：`aggr_01_99_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100`、`aggr_02_98_prom1_core_6_1_promo_6_1_top15_cash_off_and_cap100`、`aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95`、`aggr_02_98_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；新候选归入 `high_growth_theme` family，用来测试晋升来源是否能改善 2020，而不压扁高集中 family 口径。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2619` 行 / `671` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `284`，五个 family 规模为 `159 / 59 / 16 / 16 / 16`。
- 新 `liquidity_momentum` 晋升池改写 `since_2020_01` Path 2 tracked winner：`core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_promo_liqmom_top15_cash_off_and_cap95` 达到 `37.38% CAGR / -22.51% MaxDD / 1.2283 Sharpe / 3.22 Turnover`，相对旧 `34.12% / -22.77% / 1.0402 / 3.43` 同时改善收益、回撤、Sharpe 与换手。
- `since_2023_01`、`since_2025_01` 与四窗口 robust candidate 未改写；robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`。下一轮优先围绕 `promo_liqmom_top15` 做 2020 稳健化/阈值邻域，而不是回到已失效的主题或纯 cadence 线。

## 本轮补充计划与记录（2026-05-05 12:14 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙仍为 `268`，五个 family 规模为 `159 / 43 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不继续 `confirm / ramp / cadence / core_theme / industry_trend / core_3_1` 的简单邻域，新增一个独立中周期量价排序口径 `midcycle_momentum`：以 `6-1` 动量为主，叠加量能放大、近月收益、行业领涨和突破。
- 新增 4 个显式原型：`aggr_01_99_prom1_midcycle_momentum_cash_off_and_cap100`、`aggr_02_98_prom1_midcycle_momentum_cash_off_and_cap100`、`aggr_01_99_prom2_midcycle_momentum_cash_off_and_cap95`、`aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；新候选归入 `high_growth_theme` family，避免继续把高集中 family 口径压扁。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2587` 行 / `663` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `276`，五个 family 规模为 `159 / 51 / 16 / 16 / 16`。
- 新 `midcycle_momentum` 没有改写任何 Path 2 tracked winner 或 robust candidate。新增候选里 `since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom2_midcycle_momentum_cash_off_and_cap95`，仅 `11.77% CAGR / -22.15% MaxDD / 0.5693 Sharpe / 3.53 Turnover`，明显低于当前 `34.12%` winner。
- 新候选的 `since_2023_01` 最好为等权 `2/98 prom1` 的 `27.92% CAGR`，`since_2025_01` 最好为等权 `2/98 prom2` 的 `78.20% CAGR`，均低于当前对应窗口 winners；下一轮不要继续沿 `midcycle_momentum` 加码。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`。

## 本轮补充计划与记录（2026-05-05 06:14 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `260`，五个 family 规模为 `151 / 43 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不继续首月 ramp、简单 cadence、`core_theme / industry_trend` 或 `core_3_1` 邻域，新增一个真实的 2020 promotion 确认过滤 hook：在晋升候选中可配置 `6-1` 动量分位、`3-1` 动量分位与量能放大阈值，默认值保持旧行为不变。
- 新增 4 个显式原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm80`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80`、`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm85_amt130`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；新候选仍归入 `high_concentration_breakout`，不并入主题或高频 family。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2555` 行 / `655` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `268`，五个 family 规模为 `159 / 43 / 16 / 16 / 16`。
- 新确认过滤没有改善 `since_2020_01`：新增等权候选最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80`，为 `31.36% CAGR / -26.21% MaxDD / 0.9493 Sharpe / 3.43 Turnover`，低于当前 `34.12%` winner。
- 新确认过滤改写了 `since_2025_01` Path 2 tracked winner：`core_explore_80_20_total_mv_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_confirm80` 达到 `157.73% CAGR / -26.81% MaxDD / 1.7514 Sharpe / 6.63 Turnover`，相对旧 weekly winner 的 `156.73% CAGR / -40.77% MaxDD / 1.5775 Sharpe / 16.06 Turnover` 同时改善收益、回撤、Sharpe 与换手。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`。下一轮不要继续把确认过滤当作 2020 主攻线，应另找独立的中周期信号；`confirm80` 可作为 2025 风险效率 sidecar 保留。

## 本轮补充计划与记录（2026-05-05 00:03 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `252`，五个 family 规模为 `143 / 43 / 16 / 16 / 16`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不再继续扩 `core_theme / industry_trend / core_3_1 / 高频 cadence` 的简单邻域，改测 `prom1 core_6_1 cap100` 的晋升首月 ramp，验证是否能减少 2020 中周期错误重仓和换手伤害。
- 新增 4 个显式原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp70`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70`、`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_ramp85`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp85`。
- 只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量；新候选仍归入 `high_concentration_breakout`，不并入 `high_growth_theme` 或高频 family。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2523` 行 / `647` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `260`，五个 family 规模为 `151 / 43 / 16 / 16 / 16`。
- 新 ramp 原型没有改写任何 Path 2 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70/ramp85`，为 `34.12% CAGR / -22.77% MaxDD / 1.0402 Sharpe / 3.43 Turnover`，与当前 winner 基本等价而非突破。
- `since_2025_01` 新原型最好的是总市值底座 `aggr_02_98_prom1_core_6_1_cash_off_and_cap100_ramp70/ramp85`，仅 `112.20% CAGR / -22.88% MaxDD / 1.4665 Sharpe / 5.47 Turnover`，低于当前 weekly 短窗 winner 的 `156.73% CAGR`。下一轮不应继续只改首月 ramp，应改成真实的 2020 过滤/确认逻辑或寻找独立信号。

## 本轮补充计划与记录（2026-05-04 18:07 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `244`，五个 family 规模为 `143 / 43 / 16 / 12 / 12`，旧 tracked winners 与 robust candidate 均未漂移。
- 本轮停止继续扩 `core_theme / industry_trend` 排序口径，回到当前 `since_2020_01` 强点 `prom1 core_6_1 cap100`，只验证 cadence 是否能改善中周期收益或风险。
- 新增 4 个显式原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_biweekly`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_biweekly`、`aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100_weekly`。
- 只跑 `80/20 equal_weight` 与 `70/30 equal_weight` 两个底座的四窗口微批量；新增候选归入 `biweekly_rebalance_aggressive / weekly_rebalance_aggressive`，不并入 `high_growth_theme`。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2491` 行 / `639` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `252`，五个 family 规模为 `143 / 43 / 16 / 16 / 16`。
- 新高频 cadence 没有改善 `since_2020_01`：新增候选最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100_weekly`，仅 `16.88% CAGR / -48.98% MaxDD / 0.5343 Sharpe / 8.77 Turnover`，明显低于当前 `34.12%` winner。
- `since_2025_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100_weekly`：`156.73% CAGR / -40.77% MaxDD / 1.5775 Sharpe / 16.06 Turnover`，收益上限高于旧 `147.54%` winner，但回撤和换手显著恶化，只作为短窗高风险窗口赢家记录。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`；下一轮不应继续简单提高 `prom1 cap100` cadence，应转向 2020 专属过滤或降低错误换手的确认逻辑。

## 本轮补充计划与记录（2026-05-04 15:25 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `236`，五个 family 规模为 `143 / 35 / 16 / 12 / 12`；旧 tracked winners 与 robust candidate 均未漂移。
- 本轮不继续加码上一轮偏弱的 `core_theme` 财务主题口径，改测更偏 2020 中周期趋势的 `industry_trend` 核心信号：行业强度、行业内领涨、`6-1 / 3-1` 动量和突破宽度组合，不再把财务增长作为主权重。
- 新增 4 个显式原型：`aggr_01_99_prom1_industry_trend_cash_off_and_cap100`、`aggr_02_98_prom1_industry_trend_cash_off_and_cap100`、`aggr_01_99_prom2_industry_trend_cash_off_and_cap95`、`aggr_02_98_prom2_industry_trend_cash_off_and_cap95`；只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2459` 行 / `631` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `244`，五个 family 规模为 `143 / 43 / 16 / 12 / 12`，新增候选只扩充 `high_growth_theme`。
- `industry_trend` 没有改写任何 Path 2 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_industry_trend_cash_off_and_cap100`，仅 `14.60% CAGR / -25.49% MaxDD / 0.6491 Sharpe / 3.45 Turnover`，明显低于当前 `34.12%` winner。
- 主要 side observation 是 `since_2025_01` 的 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom1_industry_trend_cash_off_and_cap100` 达到 `116.82% CAGR`，但仍低于当前短窗 winner 的 `147.54% CAGR`。下一轮不应继续单独加码行业趋势/主题排序，应回到当前 `core_6_1 prom1 cap100` 强点附近寻找更有针对性的 2020 过滤或节奏控制。

## 本轮补充计划（2026-05-04 06:45 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，当前候选宇宙仍为 `228`，五个 family 规模为 `143 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均未漂移。
- 本轮不继续沿上一轮偏弱的 `prom1 core_3_1` 加码，改测一个更独立的 2020 中周期排序口径：新增 `core_theme` promoted-core 信号，把增长加速、行业强度、行业龙头与 `6-1 / 3-1` 动量合成为核心排序。
- 显式原型只补 4 个：`aggr_01_99_prom1_core_theme_cash_off_and_cap100`、`aggr_02_98_prom1_core_theme_cash_off_and_cap100`、`aggr_01_99_prom2_core_theme_cash_off_and_cap95`、`aggr_02_98_prom2_core_theme_cash_off_and_cap95`；只跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 新候选归入 `high_growth_theme` family，不并入 `high_concentration_breakout`，用来压紧 family membership 口径并避免高集中候选继续挤压其他 family。

### 本轮补充记录（2026-05-04 09:40 CST）

- 完成 8 个 `core_theme` base candidates 的四窗口微批量后，用缓存 summary 重建 comparison CSV 到 `2427` 行 / `623` 个 base strategies。
- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙升至 `236`，五个 family 规模为 `143 / 35 / 16 / 12 / 12`，新增候选只扩充 `high_growth_theme`。
- `core_theme` 没有改写任何 Path 2 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_theme_cash_off_and_cap95`，为 `22.98% CAGR / -22.33% MaxDD / 0.9094 Sharpe / 2.58 Turnover`，明显低于当前 `34.12%` winner。
- 新候选的主要 side observation 是 `since_2025_01` 的 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom1_core_theme_cash_off_and_cap100` 达到 `101.89% CAGR`，但仍低于当前短窗 winner 的 `147.54% CAGR`；下一轮不应继续单纯加码 `core_theme`，除非引入更强的 2020 专属过滤或风险节奏。

## 本轮执行计划（2026-05-04）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 避开上一轮已经验证偏弱的 `prom1 cap100` 底座迁移，本轮只测试更独立的 2020 中周期信号：把 `prom1 cap100` 的 promoted-core 信号从 `core_6_1` 改成 `core_3_1`，并只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。

### 本轮快筛记录（2026-05-04 03:57 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `220`，五个 family 规模为 `135 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均保持不变。
- 新增 4 个 `prom1 core_3_1 cap100` 原型：`aggr_01_99_prom1_core_3_1_cash_off_and_cap100`、`aggr_02_98_prom1_core_3_1_cash_off_and_cap100`、`aggr_01_99_prom1_core_3_1_full_risk_cap100`、`aggr_02_98_prom1_core_3_1_full_risk_cap100`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2395` 行 / `615` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `228`，五个 family 规模为 `143 / 27 / 16 / 12 / 12`。
- 新 `core_3_1` 原型未改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom1_core_3_1_cash_off_and_cap100`，仅 `11.90% CAGR / -29.60% MaxDD / 0.5153 Sharpe / 3.30 Turnover`，明显弱于当前 `34.12%` winner。
- `core_3_1 full_risk cap100` 在 `since_2025_01` 可做到约 `114.14% CAGR`，但仍低于当前短窗 winner 的 `147.54% CAGR`，且长窗回撤接近 `-72%~-74%`；下一轮不应继续沿 `prom1 core_3_1` 加码，应转向更独立的高成长/行业主线或重新寻找 2020 专属排序口径。

## 本轮执行计划（2026-05-03）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 避开上一轮效果较弱的 `core_3_1 full_risk` 与简单风险暴露放松，本轮只补 4 个更窄的单票高集中中周期原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100`、`aggr_03_97_prom1_core_6_1_cash_off_and_cap100`、`aggr_04_96_prom1_core_6_1_cash_off_and_cap100`；仍只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。

### 本轮快筛记录（2026-05-03 00:16 CST；06:11 CST 复核）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `196`，五个 family 规模为 `111 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均保持不变。
- 新增 4 个单票高集中中周期原型：`aggr_01_99_prom1_core_6_1_cash_off_and_cap100`、`aggr_02_98_prom1_core_6_1_cash_off_and_cap100`、`aggr_03_97_prom1_core_6_1_cash_off_and_cap100`、`aggr_04_96_prom1_core_6_1_cash_off_and_cap100`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2299` 行 / `591` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `204`，五个 family 规模为 `119 / 27 / 16 / 12 / 12`。
- `since_2020_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100`：`34.12% CAGR / -22.77% MaxDD / 1.0402 Sharpe / 3.43 Turnover`，相对旧 `prom2 cash_off_and cap90` 的 `32.25% CAGR` 明确抬升收益上限，但 Sharpe 降低且换手增加。
- 新单票原型未改写 `since_2017_01`、`since_2023_01`、`since_2025_01` 或四窗口 robust candidate；`since_2023_01` 最好仅约 `7.98% CAGR`，说明它是明确的 2020 中周期收益原型，不适合作为 2023 主攻线。

### 本轮补充（2026-05-03 12:05 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙保持 `204`，五个 family 规模为 `119 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均保持不变。
- 沿刚改写 `since_2020_01` 的 `prom1 cap100` 强点补 4 个风险暴露对照：`aggr_01_99_prom1_core_6_1_cash_off_and_risk50_cap100`、`aggr_02_98_prom1_core_6_1_cash_off_and_risk50_cap100`、`aggr_01_99_prom1_core_6_1_full_risk_cap100`、`aggr_02_98_prom1_core_6_1_full_risk_cap100`；仍只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2331` 行 / `599` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `212`，五个 family 规模为 `127 / 27 / 16 / 12 / 12`。
- 新风险暴露原型未改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_risk50_cap100`，仅 `31.43% CAGR / -44.54% MaxDD / 0.8470 Sharpe / 5.57 Turnover`，低于当前 `34.12%` winner 且回撤明显恶化。
- `full_risk cap100` 在 `since_2023_01` 可做到约 `43.33% CAGR`，但仍低于当前 `58.20%` winner，且 `MaxDD` 接近 `-45%`；下一轮不应继续单纯放松 `prom1 cap100` 风险暴露，应转向更独立的 2020 信号或底座结构。

### 本轮补充（2026-05-03 18:07 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙仍为 `212`，五个 family 规模为 `127 / 27 / 16 / 12 / 12`；旧 winners 与 robust candidate 均保持不变。
- 本轮不继续沿 `prom1 cap100` 单纯放松风险暴露，改为验证更独立的底座结构：把当前 `80/20 equal_weight` 上最强的 `prom1 cap100` 原型迁移到 `70/30 equal_weight` 与 `60/40 equal_weight` 两个底座。
- 计划只补跑 8 个四窗口 base candidates：`core_explore_70_30_equal_weight_winner_core__aggr_01_99_prom1_core_6_1_cash_off_and_cap100`、`core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom1_core_6_1_cash_off_and_cap100`、`core_explore_70_30_equal_weight_winner_core__aggr_04_96_prom1_core_6_1_cash_off_and_cap100`，以及对应的 `60/40 equal_weight` 四个同名变体；这些候选仍归入现有 `high_concentration_breakout` family，不新增 family 规则。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2363` 行 / `607` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `220`，五个 family 规模为 `135 / 27 / 16 / 12 / 12`。
- 新底座结构没有改写任何 tracked winner 或 robust candidate。`70/30 equal_weight` 最好的是 `core_explore_70_30_equal_weight_winner_core__aggr_02_98_prom1_core_6_1_cash_off_and_cap100`，`since_2020_01` 为 `31.58% CAGR / -23.68% MaxDD / 1.0231 Sharpe / 3.46 Turnover`；`60/40 equal_weight` 最好约 `27.89% CAGR / -21.61% MaxDD / 0.9952 Sharpe`，都低于当前 `80/20 equal_weight` 的 `34.12%` winner。
- 这次结果说明 `prom1 cap100` 强点对 `80/20 equal_weight` 底座较敏感，单纯降低核心占比会同步压低 `since_2020_01` 收益；下一轮应继续找更独立的 2020 信号或排序口径，而不是继续横向迁移同一底座结构。

## 本轮执行计划（2026-05-02）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 避开上一轮失效的“当前 `1/99 prom2` 月频强点直接改周频/双周频”路线，本轮只补 4 个更窄的中周期风险暴露原型：围绕 `2/98`、`3/97`、`4/96` 的 `risk50 / full_risk` 暴露与 `cap80/90` 约束，继续只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。

### 本轮快筛记录（2026-05-02）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `172`，五个 family 规模为 `87 / 27 / 16 / 12 / 12`，旧 winners 与 robust candidate 均保持不变。
- 新增 4 个中周期风险暴露原型：`aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90`、`aggr_02_98_prom2_core_6_1_full_risk_cap90`、`aggr_03_97_prom2_core_6_1_cash_off_and_risk50_cap90`、`aggr_04_96_prom2_core_6_1_cash_off_and_risk50_cap80`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2203` 行 / `567` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `180`，五个 family 规模为 `95 / 27 / 16 / 12 / 12`。
- `since_2017_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90`：`28.93% CAGR / -47.20% MaxDD / 1.0173 Sharpe / 3.89 Turnover`，相对旧 `1/99 risk50 cap95` 小幅抬升 CAGR 与 Sharpe，并略微改善回撤。
- 新原型未改写 `since_2020_01`、`since_2023_01`、`since_2025_01` 或四窗口 robust candidate；新增 2017 winner 的 `since_2020_01` 只有 `26.04% CAGR / -54.33% MaxDD / 0.8418 Sharpe`，因此下一轮不应把 `risk50 cap90` 作为 2020 主攻线。

### 本轮补充（2026-05-02 06:07 CST）

- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙仍为 `180`，五个 family 规模为 `95 / 27 / 16 / 12 / 12`，说明 family membership 口径保持稳定。
- 四窗口 tracked winner 身份未变化：`since_2017_01` 仍为 `aggr_02_98_prom2_core_6_1_cash_off_and_risk50_cap90`，`since_2020_01` 仍为 `aggr_01_99_prom2_core_6_1_cash_off_and_cap90`，`since_2023_01 / since_2025_01` 仍由 `aggr_05_95_prom3_core_6_1_full_risk_cap80` 系列占据。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`，指标随当前 comparison CSV 漂移到 `meanCAGR 59.93% / minCAGR 18.16% / worstMaxDD -67.50% / meanTurn 5.53`；这属于同步修正，不是新候选突破。
- 本轮仍没有把 `since_2020_01` 推向 `40%+ CAGR`；下一轮优先寻找更独立的 2020 中周期信号或底座组合，而不是继续沿 `risk50_cap90` 放松风险暴露。

### 本轮补充（2026-05-02 12:10 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙仍为 `180`，五个 family 规模为 `95 / 27 / 16 / 12 / 12`。
- 新增 4 个默认长周期动量口径的中周期原型：`aggr_01_99_prom2_cash_off_and_cap90`、`aggr_01_99_prom2_full_risk_cap90`、`aggr_02_98_prom2_cash_off_and_cap90`、`aggr_02_98_prom2_full_risk_cap90`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2235` 行 / `575` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `188`，五个 family 规模为 `103 / 27 / 16 / 12 / 12`。
- 新默认动量原型没有改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_full_risk_cap90`，仅 `14.31% CAGR / -56.03% MaxDD / 0.5113 Sharpe / 4.31 Turnover`，明显弱于当前 `32.25%` winner；`cash_off_and` 版本只有约 `10.75% CAGR`。
- 新原型在 `since_2025_01` 可做出 `110.29% CAGR`（`aggr_02_98_prom2_cash_off_and_cap90`），但仍低于当前短窗 winner 的 `147.54% CAGR`。下一轮不要继续把默认长周期动量作为 2020 主攻方向，应转向更独立的信号或底座组合。

### 本轮补充（2026-05-02 18:08 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `188`，五个 family 规模为 `103 / 27 / 16 / 12 / 12`。
- 新增 4 个 `core_3_1` 中周期高集中原型：`aggr_01_99_prom2_core_3_1_cash_off_and_risk50_cap95`、`aggr_01_99_prom2_core_3_1_full_risk_cap95`、`aggr_02_98_prom2_core_3_1_cash_off_and_risk50_cap95`、`aggr_02_98_prom2_core_3_1_full_risk_cap95`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `1717` 行 / `580` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `195`，五个 family 规模为 `111 / 27 / 16 / 12 / 12`。
- 新原型改写 `since_2017_01` Path 2 tracked winner 为 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom2_core_3_1_full_risk_cap95`：`33.40% CAGR / -47.23% MaxDD / 0.8712 Sharpe / 5.79 Turnover`，属于收益上限提升但 Sharpe 与换手明显承压的高风险长窗 winner。
- `since_2020_01`、`since_2023_01`、`since_2025_01` 与四窗口 robust candidate 均未改写；新增候选在 `since_2020_01` 最好仅 `24.37% CAGR`（总市值底座 `1/99 risk50 cap95`），明显弱于当前 `32.25%` winner。下一轮不应把 `core_3_1 full_risk` 作为 2020 主攻线，应继续寻找更独立的 2020 信号或底座组合。

## 本轮执行计划（2026-05-01）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点沿 `since_2020_01` 当前强点附近继续扩展中周期高集中 prom2 原型；本轮只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。

### 本轮快筛记录（2026-05-01）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `140`，五个 family 规模为 `63 / 27 / 16 / 10 / 10`；旧 `since_2020_01` winner 仍是 `aggr_01_99_prom2_core_6_1_cash_off_and_cap95`。
- 新增 4 个围绕当前强点的高集中 prom2 原型：`aggr_01_99_prom2_core_6_1_cash_off_and_risk30_cap95`、`aggr_01_99_prom2_core_6_1_cash_off_and_risk50_cap95`、`aggr_01_99_prom2_core_6_1_full_risk_cap95`、`aggr_01_99_prom2_core_6_1_cash_off_and_cap90`。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2075` 行 / `535` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `148`，五个 family 规模为 `71 / 27 / 16 / 10 / 10`。
- `since_2017_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_risk50_cap95`：`28.89% CAGR / -47.26% MaxDD / 1.0140 Sharpe / 3.89 Turnover`，相对旧 `risk50_cap80` 小幅抬升 CAGR 与 Sharpe，但回撤略深。
- `since_2020_01` Path 2 winner 身份从 `cap95` 漂移到 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap90`，关键指标持平为 `32.25% CAGR / -22.51% MaxDD / 1.1511 Sharpe / 2.94 Turnover`；这属于 cap 约束未触发下的弱等价切换，不代表收益上限突破。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.98% / minCAGR 18.01%`）。新增 `risk30/risk50/full_risk` 版本没有改善 `since_2020_01`，后续应避免继续单纯放松风险暴露。

### 本轮补充（2026-05-01 06:11 CST）

- 基线复跑 `.venv/bin/python scripts/path2_candidate_pass.py` 后，候选宇宙为 `148`，五个 family 规模为 `71 / 27 / 16 / 10 / 10`，旧 winners 与 robust candidate 均保持不变。
- 新增 4 个围绕当前 `1/99`、`2/98` 强点的晋升 3 只高集中原型：`aggr_01_99_prom3_core_6_1_cash_off_and_cap90`、`aggr_01_99_prom3_core_6_1_cash_off_and_cap95`、`aggr_02_98_prom3_core_6_1_cash_off_and_cap90`、`aggr_02_98_prom3_core_6_1_cash_off_and_cap95`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2107` 行 / `543` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `156`，五个 family 规模为 `79 / 27 / 16 / 10 / 10`。
- 新晋升 3 只原型未改写任何 tracked winner 或 robust candidate；其中 `since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom3_core_6_1_cash_off_and_cap90` / `cap95`，仅 `26.41% CAGR / -22.77% MaxDD / 1.0351 Sharpe / 2.82 Turnover`，明显低于当前 `since_2020_01` winner 的 `32.25% CAGR`。
- `since_2025_01` 新原型最好的是 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom3_core_6_1_cash_off_and_cap90` / `cap95`（`124.67% CAGR / -12.08% MaxDD / 2.2307 Sharpe`），仍低于当前短窗 winner 的 `145.68% CAGR`。下一轮不应继续单纯把 `prom2` 放宽到 `prom3`，而应寻找更独立的 2020 中周期信号或底座组合。

### 本轮补充（2026-05-01 12:11 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `156`，五个 family 规模为 `79 / 27 / 16 / 10 / 10`，旧 winners 与 robust candidate 均保持不变。
- 新增 4 个更独立的 `core_3_1` 高集中 prom2 原型：`aggr_01_99_prom2_core_3_1_cash_off_and_cap90`、`aggr_01_99_prom2_core_3_1_cash_off_and_cap95`、`aggr_02_98_prom2_core_3_1_cash_off_and_cap90`、`aggr_02_98_prom2_core_3_1_cash_off_and_cap95`；仍只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2139` 行 / `551` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `164`，五个 family 规模为 `87 / 27 / 16 / 10 / 10`。
- 新 `core_3_1` 原型没有改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_3_1_cash_off_and_cap90` / `cap95`，仅 `17.82% CAGR / -22.47% MaxDD / 0.7887 Sharpe / 2.76 Turnover`，明显低于当前 `32.25%` winner。
- `since_2025_01` 新原型最好的是 `core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_core_3_1_cash_off_and_cap90` / `cap95`（`94.82% CAGR / -12.85% MaxDD / 1.6521 Sharpe`），同样低于当前短窗 winner 的 `145.68% CAGR`。下一轮不应继续沿 `3_1 + cash_off_and` 高集中线加码。

### 本轮补充（2026-05-01 18:14 CST）

- 基线运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙为 `164`，五个 family 规模为 `87 / 27 / 16 / 10 / 10`，旧 winners 与 robust candidate 均保持不变。
- 避开前几轮失效的 `prom3` 与 `core_3_1 + cash_off_and` 高集中线，本轮新增 4 个当前 `since_2020_01` 月频强点的高频执行原型：`aggr_01_99_prom2_core_6_1_cash_off_and_cap90_biweekly`、`aggr_01_99_prom2_core_6_1_cash_off_and_cap90_weekly`、`aggr_01_99_prom2_core_6_1_cash_off_and_cap95_biweekly`、`aggr_01_99_prom2_core_6_1_cash_off_and_cap95_weekly`；只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2171` 行 / `559` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `172`，五个 family 规模为 `87 / 27 / 16 / 12 / 12`。
- 新高频原型没有改写任何 tracked winner 或 robust candidate。`since_2020_01` 最好的是等权单周版本（`16.09% CAGR / -35.74% MaxDD / 0.5795 Sharpe / 8.16 Turnover`），双周版本只有约 `9.12% CAGR` 且回撤超过 `-60%`，明显低于当前月频 winner 的 `32.25% CAGR / -22.51% MaxDD / 1.1511 Sharpe`。
- `since_2023_01` 新原型只有双周版本保留正收益（总市值底座约 `26.68% CAGR / -31.43% MaxDD / 1.0267 Sharpe`），单周版本转负；`since_2025_01` 最好也仅约 `60.73% CAGR`，远低于当前短窗 winner 的 `145.68% CAGR`。下一轮不应继续把当前 `1/99 prom2` 月频强点简单改成周频/双周频。

## 本轮执行计划（2026-04-30）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙继续维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点仍是保持 `100+` family-ranked universe，并优先观察是否出现更适配 `since_2020_01` 的中周期高收益原型；若无 winner 改写，只同步记录扫描结果。

### 本轮快筛记录（2026-04-30）

- 在发现 A 股 comparison CSV 只剩 `73` 行后，先用缓存 summary 重建为 `1477` 行 / `500` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`。
- 本轮候选宇宙为 `115`，五个 family 规模为 `43 / 23 / 16 / 10 / 10`，仍满足 `100+` family-ranked universe 要求；减少的 `1` 个候选来自缓存中不再可匹配的空 membership 行，不影响五族结构。
- 四窗口 tracked winner 身份继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe`）。
- 四窗口 robust candidate 身份继续是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`，指标随 `as_of=2026-04-30` 同步到 `meanCAGR 57.98% / minCAGR 18.01% / worstMaxDD -67.50%`。
- 本轮仍没有找到能把 `since_2020_01` 推向 `40%+ CAGR` 的中周期高收益原型；价值主要是恢复完整候选扫描口径并同步 `2026-04-30` 指标漂移。

### 本轮补充（2026-04-30 06:35 CST）

- 新增 4 个中周期 Path 2 原型并只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量：`aggr_04_96_prom3_core_6_1_cash_off_and_cap70`、`aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70`、`aggr_06_94_prom4_core_6_1_full_risk_cap70`、`aggr_06_94_prom4_core_6_1_cash_off_and_cap70`。
- 微批量回测后用缓存 summary 重建 comparison CSV 到 `1979` 行 / `511` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `124`，五个 family 规模为 `47 / 27 / 16 / 10 / 10`。
- 新原型没有改写 tracked winners 或 robust candidate。新增候选里 `since_2020_01` 最好的是 `core_explore_80_20_equal_weight_winner_core__aggr_04_96_prom3_core_6_1_cash_off_and_cap70`，仅 `25.37% CAGR / -24.64% MaxDD / 1.0102 Sharpe / 2.83 Turnover`，明显低于当前 Path 2 2020 winner 的 `32.07% CAGR`。
- 新原型的有效观察主要在 `since_2023_01` sidecar：`aggr_06_94_prom4_core_6_1_full_risk_cap70` 达到 `46.12% CAGR` 但 MaxDD 深至 `-47.32%`；`aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70` 达到 `42.86% CAGR / 1.3744 Sharpe / -32.63% MaxDD`，仍低于当前 2023 winner 的 `57.48% CAGR`。
- `since_2025_01` 新原型最好的是 `core_explore_80_20_total_mv_winner_core__aggr_04_96_prom3_core_6_1_cash_off_and_risk50_cap70`（`135.01% CAGR / -11.56% MaxDD / 2.3268 Sharpe`），仍低于当前短窗 winner `aggr_03_97_prom2_core_6_1_cash_off_and_cap80` 的 `145.68% CAGR`。

### 本轮补充（2026-04-30 12:12 CST）

- 先重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`，基线仍为 `124` 个候选，五个 family 规模为 `47 / 27 / 16 / 10 / 10`，旧 `since_2020_01` winner 仍是 `aggr_03_97_prom2_core_6_1_cash_off_and_cap80`。
- 新增 4 个围绕 `since_2020_01` 当前强点的中周期高集中原型，并只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座的四窗口微批量：`aggr_02_98_prom2_core_6_1_cash_off_and_cap90`、`aggr_02_98_prom2_core_6_1_cash_off_and_risk30_cap90`、`aggr_04_96_prom2_core_6_1_cash_off_and_cap80`、`aggr_04_96_prom2_core_6_1_cash_off_and_risk30_cap80`。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2011` 行 / `519` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `132`，五个 family 规模为 `55 / 27 / 16 / 10 / 10`。
- `since_2020_01` Path 2 tracked winner 改写为 `core_explore_80_20_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_cash_off_and_cap90`：`32.19% CAGR / -22.77% MaxDD / 1.1480 Sharpe / 2.95 Turnover`，相对旧 winner `32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe / 2.95 Turnover` 小幅抬升收益并改善回撤。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.98% / minCAGR 18.01%`）；新原型的 `risk30` 版本在 2017 长窗进入前列，但 2020 回撤过深，不作为主 winner。

### 本轮补充（2026-04-30 18:16 CST）

- 在 `since_2020_01` 强点附近继续新增 4 个高集中 prom2 原型，并只补跑 `80/20 equal_weight` 与 `80/20 total_mv` 两个底座四窗口微批量：`aggr_01_99_prom2_core_6_1_cash_off_and_cap95`、`aggr_02_98_prom2_core_6_1_cash_off_and_cap95`、`aggr_03_97_prom2_core_6_1_cash_off_and_cap90`、`aggr_04_96_prom2_core_6_1_cash_off_and_cap90`。
- 微批量后用缓存 summary 重建 comparison CSV 到 `2043` 行 / `527` 个 base strategies，再运行 `.venv/bin/python scripts/path2_candidate_pass.py`；候选宇宙升至 `140`，五个 family 规模为 `63 / 27 / 16 / 10 / 10`。
- `since_2020_01` Path 2 tracked winner 再次改写为 `core_explore_80_20_equal_weight_winner_core__aggr_01_99_prom2_core_6_1_cash_off_and_cap95`：`32.25% CAGR / -22.51% MaxDD / 1.1511 Sharpe / 2.94 Turnover`，相对 12:12 winner 小幅抬升收益、Sharpe，并改善回撤与换手。
- 四窗口 robust candidate 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.98% / minCAGR 18.01%`）；新增 `cap95/cap90` 原型有效改善 2020 窗口，但还没有把 `since_2020_01` 推向 `40%+ CAGR`。

## 上轮执行计划（2026-04-29）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点仍是维持 `100+` family-ranked universe，并优先观察是否出现更适配 `since_2020_01` 的中周期高收益原型；若无 winner 改写，只同步记录扫描结果。

### 本轮快筛记录（2026-04-29 12:04 CST）

- 在重建后的完整 comparison CSV 上重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`，候选宇宙恢复为 `116`，五个 family 规模为 `43 / 23 / 16 / 10 / 10`。
- 四窗口 tracked winner 与 robust candidate 继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe`），`robust` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 本轮没有找到能把 `since_2020_01` 推向 `40%+ CAGR` 的中周期高收益原型；当前价值主要是恢复被局部 CSV 压缩掉的 `100+` 候选扫描口径。

### 本轮快筛记录（2026-04-29 18:50 CST）

- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选宇宙仍为 `116`，五个 family 规模继续为 `43 / 23 / 16 / 10 / 10`。
- 四窗口 tracked winner 与 robust candidate 身份继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（`32.07% CAGR / -23.02% MaxDD / 1.1480 Sharpe`），`robust` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 本轮新增价值仍是确认 `100+` family-ranked universe 的五族口径稳定；没有出现能把 `since_2020_01` 推向 `40%+ CAGR` 的中周期高收益原型。

## 上轮执行计划（2026-04-28）

- 本轮继续独立运行 `.venv/bin/python scripts/path2_candidate_pass.py`，不要求先打赢 Path 1 才记录结果。
- 候选宇宙维持五个 family：`high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic / biweekly_rebalance_aggressive / weekly_rebalance_aggressive`。
- 重点仍是维持 `100+` family-ranked universe，并优先观察是否出现更适配 `since_2020_01` 的中周期高收益原型；若无 winner 改写，只同步记录扫描结果。

### 本轮快筛记录（2026-04-28 00:06 CST）

- 运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数 `103`，五个 family 规模继续为 `43 / 23 / 16 / 4 / 4`。
- 四窗口 tracked winner 与 robust candidate 的身份未改写，只出现缓存指标小幅漂移：`since_2020_01` winner 仍是 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（CAGR `32.07%`），`robust` 仍是 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 当前 `since_2020_01` 仍未冲到 `40%+ CAGR`，下一轮继续优先寻找更适配 2020 的中周期高收益原型，而不是扩大高频候选权重。

### 本轮快筛记录（2026-04-28 12:04 CST）

- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数仍为 `103`，五个 family 规模仍为 `43 / 23 / 16 / 4 / 4`。
- 四窗口 tracked winner 与 robust candidate 身份继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（CAGR `32.07%`），`robust` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 本轮没有找到能把 `since_2020_01` 推向 `40%+ CAGR` 的中周期高收益原型；下一轮继续优先扩大真正适配 2020 的独立原型，而不是简单增加周频/双周频权重。

### 本轮快筛记录（2026-04-28 18:29 CST）

- 重新运行 `.venv/bin/python scripts/path2_candidate_pass.py`：候选数扩到 `116`，五个 family 规模为 `43 / 23 / 16 / 10 / 10`。
- 四窗口 tracked winner 与 robust candidate 身份继续不变：`since_2020_01` 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom2_core_6_1_cash_off_and_cap80`（CAGR `32.07%`），`robust` 仍为 `core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_core_6_1_full_risk_cap80`（meanCAGR `57.28% / minCAGR 17.78%`）。
- 本轮新增的周频/双周频候选规模提升了 family-ranked universe，但仍没有把 `since_2020_01` 推向 `40%+ CAGR`；下一轮继续优先寻找更适配 2020 的中周期高收益原型。

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

当前默认扫描宇宙（`2026-04-28`）已提升到 `116` 个 candidates；五个 family 的当前规模分别为 `43 / 23 / 16 / 10 / 10`。其中 `high_concentration_breakout / high_growth_theme / momentum_equal_weight_elastic` 三条长周期 family 已显式纳入 `core_explore_80_20_total_mv_winner_core` 这一窄 prefix，避免当前 `since_2025 / robust` 的 `total_mv` tracked winners 脱离 family ranking。

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
## 本轮执行计划（2026-06-01 16:23 CST）

- 上一轮候选/结果摘要：上一轮建议继续推进 high-growth 容量/成本线 `top12_risk36_exit54_reconfirm84_caution66_cap50_cost_guard_v11`，用于检查 `since_2020_01` 中周期高收益是否能在更低单票上限和更严格恢复确认下保留。
- 本轮候选 ID：`core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk36_mom_exit54_reconfirm84_caution66_cap50_cost_guard_v11`、`core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk36_mom_exit54_reconfirm84_caution66_cap50_cost_guard_v11`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v11_ids>`。
- `90/10 equal_weight` 五窗口 CAGR 为 `22.12% / 33.68% / 48.52% / 140.31% / 7.96%`，最大回撤为 `-43.66% / -32.75% / -26.05% / -16.39% / -9.62%`，换手为 `3.60x / 4.25x / 4.35x / 7.73x / 7.56x`；`90/10 total_mv` 为 `19.90% / 29.00% / 44.07% / 151.62% / 18.00%`，最大回撤 `-49.38% / -35.08% / -25.98% / -15.93% / -6.93%`。
- 结论：v11 的 `since_2023_01` 和 `since_2025_01` 弹性可比，但 2017/2020 回撤仍深，2026 观察窗明显不稳；`path2_candidate_pass.py` 后 universe 为 `820`，`update_weighted_winners.py` 后 Path 2 window winner 与 robust candidate 未被 v11 改写。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> medium_cycle_growth`。下一轮不要继续单纯压 cap，第一候选建议做 `aggr_02_98_prom2_core_6_1_promo_liqmom_top12_risk34_mom_exit52_reconfirm86_caution62_cap45_cost_guard_v12`，目标是修复 2020 回撤和 2026 弱观测；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v12_ids>`。

## 本轮执行计划（2026-06-02 22:30 CST）

- 上一轮候选/结果摘要：上一轮 high-growth v14 修复部分 2026 观察但仍被单一 high-growth family 压扁；本轮在 `medium_cycle_growth` 邻域改为 `prom3/top14/risk32/exit52/reconfirm88/caution62/cap40`，检查增加晋升数和扩大候选池能否降低集中度。
- 本轮候选 ID：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk32_mom_exit52_reconfirm88_caution62_cap40_cost_guard_v15`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk32_mom_exit52_reconfirm88_caution62_cap40_cost_guard_v15`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v15_ids>`。
- `90/10 equal_weight` 五窗口 CAGR 为 `23.30% / 23.18% / 34.50% / 139.23% / 23.01%`，最大回撤为 `-35.58% / -26.32% / -20.54% / -13.51% / -9.15%`，换手为 `3.32x / 3.92x / 4.28x / 6.79x / 6.67x`；`90/10 total_mv` CAGR 为 `21.51% / 19.45% / 32.37% / 147.35% / 31.27%`。
- 结论：v15 的 2025 弹性仍强，但 2020/2023 显著弱于当前 Path 2 window winners，持仓抽样仍集中在少数强票，未解决 high-growth family 的集中度约束。`path2_candidate_pass.py` 后 universe 为 `849`，`update_weighted_winners.py` 后 Path 2 window winner 与 robust candidate 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> risk_reconfirm_sensitivity`。下一轮不要继续只扩 topN，第一候选建议 `aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v16`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v16_ids>`。

## 本轮执行计划（2026-06-03 12:10 CST）

- 上一轮候选/结果摘要：上一轮 v15 扩到 `prom3/top14` 后 2025 很强，但 2020/2023 仍弱。本轮按 `risk_reconfirm_sensitivity` 不再只压 cap，而是放宽 risk/exit/reconfirm 到 `risk34/exit54/reconfirm86/caution64/cap42`，确认是否能换回中窗收益。
- 本轮候选 ID：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk34_mom_exit54_reconfirm86_caution64_cap42_cost_guard_v16`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk34_mom_exit54_reconfirm86_caution64_cap42_cost_guard_v16`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v16_ids>`。
- `90/10 equal_weight` 五窗口 CAGR 为 `27.87% / 32.28% / 55.17% / 173.70% / 19.27%`，最大回撤为 `-29.08% / -32.67% / -18.72% / -11.22% / -9.25%`，换手为 `3.22x / 3.69x / 4.04x / 6.44x / 7.90x`；`90/10 total_mv` CAGR 为 `26.40% / 27.96% / 46.41% / 183.80% / 35.73%`。
- 结论：v16 的 2023/2025 明显优于 v15，但 2020 仍低于 Path 2 现有 winner/robust，且 2026 不稳。`path2_candidate_pass.py` 后 universe 为 `855`，high_growth 为 `349`，Path 2 window winner 与 robust candidate 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> underrepresented_families`。下一轮第一候选建议把本轮 Path 1 core 多因子放到低相关 family 做双底座确认：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-28 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_lowvol_industry_cost_guard_reconfirm`，避免继续把预算压到单一 high_growth family。

## 本轮执行计划（2026-06-03 10:35 CST）

- 上一轮候选/结果摘要：上一轮 v16 把 `prom3/top14` 放宽后 2023/2025 弹性强但 2020 不够。本轮继续沿 `medium_cycle_growth` 做反向验证，把 risk/exit/reconfirm 收紧到 `risk30/exit50/reconfirm92/caution60/cap40`，检查更严格恢复确认能否改善 2020 和回撤。
- 本轮候选 ID：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17`。增量命令与 Path 1/3 合并执行：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__share_14_86_hold_2_8_ramp75_cost_guard,core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm92_caution60_cap40_cost_guard_v17,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cash_off_and_cap60_hold2_turn12_exit92_weekly`。
- `90/10 equal_weight` 五窗口 CAGR 为 `25.51% / 24.66% / 42.35% / 117.00% / 15.15%`，最大回撤为 `-32.47% / -27.89% / -19.47% / -20.76% / -9.15%`，换手为 `3.20x / 3.90x / 3.98x / 6.85x / 5.80x`；`90/10 total_mv` CAGR 为 `24.03% / 20.63% / 40.08% / 126.03% / 21.00%`，最大回撤为 `-33.91% / -26.50% / -17.70% / -20.52% / -5.93%`。
- 结论：v17 比 v16 更保守，2025 仍强，但 2020/2023 低于现有 Path 2 winner/robust；终端持仓仍容易集中在少数光通信/半导体强票，不能仅凭 2025 短窗晋级。`path2_candidate_pass.py` 后 universe 为 `860`，Path 2 window winner 与 robust candidate 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> medium_cycle_growth`。下一轮不要继续只在 high_growth 线小幅调参，第一候选建议加入更低集中度约束的 `aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap32_cost_guard_v18`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v18_ids>`。

## 本轮执行计划（2026-06-04 04:18 CST）

- 上一轮候选/结果摘要：上一轮 v17 证明 `prom3/top14/risk30/exit50/reconfirm92` 比 v16 更保守，但 2020/2023 仍低于现有 Path 2 winner/robust。本轮开局与最终 guard 均提示 `risk_reconfirm_sensitivity`，但新增预算优先用于 Path 1 core、Path 4 coverage_penalty 与 HK 扩展线，Path 2 本轮只做巡检和下一轮候选设计。
- 巡检结果：`scripts/path2_candidate_pass.py` 后 Path 2 universe 为 `864` 个 candidates，四窗口 coverage 为 `864/864 complete`。当前 Path 2 winners 仍为旧高收益/高集中家族：2017 `...cost_guard_v5`、2020 `...reconfirm70_cap95`、2023 `...risk50_ma_cap95`、2025 `...emergent_theme_risk40_cap70`；robust candidate 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 本轮候选设计但未回测：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap32_cost_guard_v18`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk28_mom_exit48_reconfirm94_caution58_cap32_cost_guard_v18`。未回测原因：本轮新增/确认 A股 base ids 已用 4 个，且 HK 扩展线新增 4 个 strategy ids；在 10 个以内预算约束下，Path 2 只记录下一轮第一条命令。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> underrepresented_families`。下一轮首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_core_multifactor_quality_profitability_industry_defense_reconfirm`；若该低相关多因子双底座仍弱，再回到 `risk_reconfirm_sensitivity` 的 v18 高收益线。

## 本轮执行计划（2026-06-08 06:05 CST）

- 上一轮候选/结果摘要：上一轮 Path 2 只记录 `risk_reconfirm_sensitivity` 下一候选，本轮按该 focus 实现 `v24_medium_cycle`，目标是在 `prom3/top12/risk30/exit50/reconfirm92/caution60/cap32` 下压低集中度并检查 2020/2023 稳定性。
- 本轮候选 ID：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm92_caution60_cap32_cost_guard_v24_medium_cycle`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk30_mom_exit50_reconfirm92_caution60_cap32_cost_guard_v24_medium_cycle`。增量命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v24_ids>`。
- 五窗口结果：`90/10 equal_weight` CAGR 为 `22.08% / 26.28% / 45.81% / 146.30% / 35.22%`，最大回撤为 `-38.36% / -29.89% / -17.85% / -19.44% / -8.79%`；`90/10 total_mv` CAGR 为 `20.55% / 22.25% / 45.05% / 157.65% / 44.44%`，最大回撤为 `-39.34% / -32.15% / -13.35% / -18.93% / -5.23%`。
- 结论：v24 改善短窗和 2023，但 2017/2020 仍低于现有 Path 2 winner/robust，且换手仍在 `3.2x-7.0x`；`scripts/path2_candidate_pass.py` 后 universe 为 `919`，Path 2 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> risk_reconfirm_sensitivity`。下一轮第一候选建议 `aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v25_ids>`。

## 本轮执行计划（2026-06-08 12:13 CST）

- 上一轮候选/结果摘要：上一轮 Path 2 `v24_medium_cycle` 2023/短窗强但 2017/2020 仍弱。本轮 `scripts/path2_candidate_pass.py` 继续巡检，候选池增至 `921`，当前 winners 仍为旧高收益线，robust 仍为 `core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_core_6_1_promo_liqmom_top15_risk50_mom_exit60_reconfirm65_cap95`。
- 本轮候选 ID 与命令：本轮未新增 Path 2 base id；执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py` 与 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --family-scope refresh_active --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01` 完成 active 同步。
- 结论：Path 2 本轮没有 window winner、robust candidate 或 tracked payload 变化；高收益 family 仍压倒中周期修复候选，新增预算优先投给 Path 1 core、Path 3、Path 4、Path 5 与 HK 六个策略。
- 候选设计但未回测：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle`。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> capacity_and_cost_stress`。首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle,core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle`；重点看 cap28 是否能降低 2026 集中度惩罚。

## 本轮执行计划（2026-06-08 17:37 CST）

- 上一轮候选/结果摘要：上一轮留下 v25 `cap28` 中周期候选，目标是进一步降低单票集中度并验证 2020/2023 的可持续性。
- 本轮候选 ID 与命令：`core_explore_90_10_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle`、`core_explore_90_10_total_mv_winner_core__aggr_03_97_prom3_core_6_1_promo_liqmom_top12_risk32_mom_exit52_reconfirm90_caution62_cap28_cost_guard_v25_medium_cycle`。命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v25_ids>`。
- `90/10 equal_weight` 五窗口 CAGR `19.37% / 27.88% / 42.87% / 146.82% / 47.23%`，最大回撤 `-40.37% / -26.12% / -16.14% / -11.96% / -8.62%`，换手最高 `6.87x`；`90/10 total_mv` CAGR `17.14% / 23.20% / 41.63% / 153.00% / 57.23%`，最大回撤最差 `-42.48%`。
- 结论：v25 短窗强，但长窗回撤和集中度仍不合格，`path2_candidate_pass.py` 后 universe 为 `926`，robust 仍是旧 `...risk50_mom_exit60_reconfirm65_cap95`，window winner/tracked payload 未变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> risk_reconfirm_sensitivity`。下一轮不要继续只压 cap，建议注册 `aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm95_caution62_cap28_cost_guard_v26_medium_cycle` 双底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-04 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v26_risk_reconfirm_ids>`。

## 本轮执行计划（2026-06-08 23:27 CST）

- 上一轮候选/结果摘要：上一轮 v25 短窗强但长窗回撤和集中度不合格；本轮按计划注册 v26，把 `prom4/top14/risk30/exit50/reconfirm95/caution62/cap28` 作为中周期修复验证。
- 本轮候选 ID 与命令：`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm95_caution62_cap28_cost_guard_v26_medium_cycle`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top14_risk30_mom_exit50_reconfirm95_caution62_cap28_cost_guard_v26_medium_cycle`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v26_ids>`。
- 五窗口结果：`90/10 equal_weight` CAGR `21.32% / 25.43% / 36.56% / 95.54% / 20.45%`，最大回撤 `-30.37% / -21.69% / -20.40% / -16.57% / -8.62%`；`90/10 total_mv` CAGR `19.34% / 20.64% / 36.13% / 102.99% / 29.02%`，最大回撤 `-30.98% / -28.05% / -19.56% / -16.13% / -5.85%`。
- 结论：v26 降低部分 2020 回撤但中长窗收益仍低于现有 Path 2 winner/robust；`path2_candidate_pass.py` 后 candidates 为 `932`，window winner、robust candidate 与 tracked payload 未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> risk_reconfirm_sensitivity`。下一轮第一候选建议在 v26 基础上降低换手和短窗集中度：`aggr_04_96_prom4_core_6_1_promo_liqmom_top13_risk28_mom_exit48_reconfirm96_caution64_cap24_cost_guard_v27_medium_cycle` 双底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v27_ids>`。

## 本轮执行计划（2026-06-09 04:20 CST）

- 上一轮候选/结果摘要：上一轮 v26 降低部分 2020 回撤但收益不足；本轮按计划注册 v27，把 `top13/risk28/exit48/reconfirm96/caution64/cap24` 作为更低集中度的中周期修复验证。
- 本轮候选 ID 与命令：`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top13_risk28_mom_exit48_reconfirm96_caution64_cap24_cost_guard_v27_medium_cycle`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top13_risk28_mom_exit48_reconfirm96_caution64_cap24_cost_guard_v27_medium_cycle`。实际合并命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v27_ids>,core_explore_80_20_equal_weight_winner_core__aggr_08_92_prom6_cost_guard_cap58_hold5_turn04_exit95_risk25_weekly`。
- 五窗口结果：`90/10 equal_weight` CAGR `18.99% / 28.88% / 32.91% / 84.34% / -6.84%`，最大回撤 `-20.20% / -19.86% / -18.78% / -17.37% / -12.13%`，换手 `3.28x / 3.92x / 4.20x / 6.65x / 7.06x`；`90/10 total_mv` CAGR `16.03% / 25.25% / 32.56% / 87.22% / -0.56%`。
- 结论：v27 比 v26 回撤更稳，但 2017/2020/2023 收益仍低于当前 Path 2 winner/robust，2026 观察窗也不足。`path2_candidate_pass.py` 后 universe 为 `937`，`update_weighted_winners.py` 后 Path 2 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> underrepresented_families`。下一轮不要继续只沿 high_growth 小步调参，第一候选建议注册低相关双周/弹性线 `aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk28_exit46_cap24_cost_guard_v28` 双底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v28_underrepresented_ids>`。

## 本轮执行计划（2026-06-09 20:05 CST）

- 上一轮候选/结果摘要：上一轮 high-growth v27 回撤更稳但收益不足，本轮按 `underrepresented_families` 注册低相关双周/弹性线 `v28`，目标是补 `biweekly_rebalance_aggressive` 的中周期原型，而不是继续沿 high_growth 小步调参。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk28_exit46_cap24_cost_guard_v28`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk28_exit46_cap24_cost_guard_v28`。实际 A股合并命令使用五窗口 `--only-base-ids` 覆盖。
- 五窗口结果：`80/20 equal_weight` CAGR `3.25% / 9.11% / 13.36% / 46.36% / 255.12%`，最大回撤 `-57.80% / -47.46% / -31.22% / -26.89% / -8.99%`，换手 `7.02x / 8.18x / 7.43x / 11.25x / 14.90x`；`70/30 equal_weight` CAGR `4.35% / 10.10% / 14.91% / 43.78% / 252.51%`，最大回撤 `-53.80% / -44.65% / -29.22% / -26.37% / -8.99%`。
- 结论：v28 只在 2025/2026 观察窗有弹性，2017/2020 回撤太深；`scripts/path2_candidate_pass.py` 后候选池为 `942`，`biweekly_rebalance_aggressive=29`，`update_weighted_winners.py` 后 Path 2 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> capacity_and_cost_stress`。下一轮第一候选建议在 v28 上继续压 cap/risk/exit：`aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29,core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29`。

## 本轮执行计划（2026-06-09 22:26 CST）

- 上一轮候选/结果摘要：上一轮 v28 只在短窗有弹性且长窗回撤过深；本轮按 `capacity_and_cost_stress` 把风险阈值、出场和单票上限继续收紧到 v29，测试双周弹性线能否降低 2017/2020 损伤。
- 本轮候选 ID 与命令：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk24_exit44_cap20_cost_guard_v29`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v29_ids>`。
- 五窗口结果：`80/20 equal_weight` CAGR `4.87% / 11.83% / 16.12% / 64.17% / 272.19%`，最大回撤 `-38.62% / -43.71% / -23.85% / -21.04% / -7.90%`，换手 `6.89x / 8.02x / 7.32x / 14.09x / 14.37x`；`70/30 equal_weight` CAGR `5.14% / 11.73% / 15.28% / 58.18% / 289.85%`，最大回撤最差 `-46.32%`。
- 结论：v29 相比 v28 略改善部分短窗，但 2017/2020 回撤仍太深且换手极高；`scripts/path2_candidate_pass.py` 后候选池为 `948`，`biweekly_rebalance_aggressive=31`，Path 2 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> medium_cycle_growth`。下一轮不要继续只压双周 cap，建议回到中周期低集中度月频线：`aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle` 双底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v30_medium_cycle_ids>`。

## 本轮执行计划（2026-06-10 04:41 CST）

- 上一轮候选/结果摘要：上一轮 v29 双周弹性线长窗回撤和换手仍高；本轮按 `medium_cycle_growth` 回到月频中周期、低集中度 `liqmom_top12`，确认是否能降低 2017/2020 损伤。
- 本轮候选 ID 与命令：`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm96_caution58_cap22_cost_guard_v30_medium_cycle`；实际 A股合并命令使用五窗口 `--only-base-ids` 覆盖。
- 五窗口结果：`90/10 equal_weight` CAGR `9.77% / 11.04% / 7.92% / 24.68% / 27.93%`，最大回撤 `-20.25% / -13.94% / -14.76% / -10.75% / -10.74%`，换手 `4.75x / 4.06x / 3.65x / 10.33x / 9.24x`；`90/10 total_mv` CAGR `13.06% / 12.95% / 8.27% / 40.99% / 11.43%`，最大回撤 `-15.80% / -14.98% / -13.35% / -15.03% / -13.10%`。
- 结论：v30 相比双周线显著降回撤和换手，但 2020/2023 收益不足，未改变 Path 2 window winner、robust candidate 或 tracked payload；`scripts/path2_candidate_pass.py` 后候选池为 `929`，说明移除 Path 4 emergent theme 后 Path 2 池已重新分离。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> risk_reconfirm_sensitivity`。下一轮第一候选建议只微调确认强度和 cap：`aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v31_medium_cycle` 双底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-08 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v31_medium_cycle_ids>`。

## 本轮执行计划（2026-06-10 10:40 CST）

- 上一轮候选/结果摘要：上一轮 v30 降低回撤但 2020/2023 收益不足；本轮按计划微调到 v31，把 `risk24/exit44/reconfirm97/caution56/cap20` 作为中周期低集中度确认。
- 本轮候选 ID 与命令：`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v31_medium_cycle`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit44_reconfirm97_caution56_cap20_cost_guard_v31_medium_cycle`；实际命令与 Path 1/3 合并五窗口执行。
- 五窗口结果：`90/10 equal_weight` CAGR `8.94% / 9.87% / 10.07% / 27.99% / 39.02%`，最大回撤 `-20.26% / -12.98% / -15.18% / -10.34% / -10.34%`，换手 `4.62x / 3.90x / 5.42x / 10.35x / 9.26x`；`90/10 total_mv` CAGR `11.06% / 10.27% / 13.95% / 43.64% / 21.53%`，最大回撤 `-16.05% / -15.49% / -14.94% / -14.94% / -12.99%`。
- 结论：v31 相比高换手双周线更稳，但 2020/2023 仍低于现有 Path 2 winner/robust；`scripts/path2_candidate_pass.py` 后候选池为 `934`，Path 2 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> capacity_and_cost_stress`。下一轮第一候选建议继续压容量/成本而不是回到高集中突破：`aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v32_capacity_stress` 双底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v32_capacity_ids>`；若 v32 仍弱，再停止该月频小修。

## 本轮执行计划（2026-06-10 16:31 CST）

- 上一轮候选/结果摘要：上一轮 v31 中周期低集中度仍弱；本轮按 `capacity_and_cost_stress` 注册 v32，把 `risk22/exit42/reconfirm98/caution54/cap18` 作为更硬容量/成本压力测试。
- 本轮候选 ID 与命令：`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v32_capacity_stress`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit42_reconfirm98_caution54_cap18_cost_guard_v32_capacity_stress`；路径首命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v32_capacity_ids>`。
- 五窗口结果：`90/10 equal_weight` CAGR `7.06% / 7.15% / 10.25% / 28.64% / 41.90%`，最大回撤最差 `-25.61%`，换手最高 `10.37x`；`90/10 total_mv` CAGR `8.82% / 7.21% / 13.53% / 42.47% / 22.35%`，最大回撤最差 `-25.35%`，换手最高 `9.85x`。
- 结论：v32 进一步降低部分风险参数后中长窗收益反而不足，短窗仍高换手；`scripts/path2_candidate_pass.py` 后候选池为 `939`，Path 2 window winner、robust candidate 与 tracked payload 均未改变。该月频小修应暂停。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> medium_cycle_growth`。下一轮第一候选建议回到收益修复而不是继续压 cap：`aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap18_cost_guard_v33_medium_cycle_repair` 双底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v33_medium_cycle_ids>`；若 v33 仍弱，停止 `prom4/top12` 月频小修。

## 本轮执行计划（2026-06-11 05:45 CST）

- 上一轮候选/结果摘要：上一轮 v32 容量压力测试确认月频小修过弱；本轮按 `medium_cycle_growth` 回到 `prom4/top10/risk24/exit44/reconfirm97/caution56/cap18` 的收益修复版本，继续保持 Path 2 的 `growth_elastic` 独立候选池，不引入 Path 4 emergent theme 变体。
- 本轮候选 ID 与命令：`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap18_cost_guard_v33_medium_cycle_repair`、`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap18_cost_guard_v33_medium_cycle_repair`；实际命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v33_ids>,<one_path3_id>`。
- 五窗口结果：`90/10 equal_weight` CAGR `9.02% / 10.11% / 10.30% / 28.71% / 42.31%`，最大回撤 `-20.46% / -12.95% / -14.78% / -10.57% / -9.93%`；`90/10 total_mv` CAGR `11.29% / 10.87% / 13.53% / 42.35% / 22.38%`，最大回撤 `-16.63% / -15.33% / -14.99% / -14.99% / -12.88%`。
- 结论：v33 相比 v32 稍修复 2023/2025，但仍远低于当前 Path 2 official winner/robust，且换手仍偏高；`scripts/path2_candidate_pass.py` 后候选池为 `944`，Path 2 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> risk_reconfirm_sensitivity` 且状态为 `rotate`。下一轮第一候选建议只做一次确认强度/风险弹性对照：`aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v34_reconfirm_balance` 双底座，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-09 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v34_reconfirm_ids>`；若仍弱，暂停 `prom4/top10` 月频修复。

## 本轮执行计划（2026-06-11 16:10 CST）

- 上一轮候选/结果摘要：上一轮留下 `prom4/top10/risk26/exit46/reconfirm96/caution58/cap18` 的 v34 确认强度/风险弹性对照；本轮按 Path 2 独立 `growth_elastic` 池执行双底座，没有把 Path 4 emergent theme 变体并入 Path 2 扫描池。
- 本轮候选 ID 与命令：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v34_reconfirm_balance`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v34_reconfirm_balance`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v34_ids>,<one_path3_id>`。
- 五窗口结果：`90/10 total_mv` CAGR `11.56% / 11.30% / 13.01% / 40.69% / 18.47%`，最大回撤 `-16.87% / -14.62% / -15.10% / -15.10% / -12.88%`，换手 `4.34x / 3.69x / 5.27x / 9.89x / 9.30x`；`90/10 equal_weight` CAGR `7.13% / 7.35% / 9.88% / 27.70% / 39.19%`，最大回撤 `-20.55% / -13.42% / -15.08% / -10.57% / -9.93%`。
- 结论：v34 没有修复 2020/2023 收益，短窗仍带高换手；`scripts/path2_candidate_pass.py` 后候选池为 `949`，Path 2 window winner、robust candidate 与 tracked payload 均未改变。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> underrepresented_families`。下一轮暂停 `prom4/top10` 月频小修，第一候选建议切回低相关双周/弹性族并进一步压风险和 cap：`core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn`、`core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap18_cost_guard_v35_lowturn`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-10 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v35_underrepresented_ids>`；若未注册，先只增加这两个 base ids。

## 本轮执行计划（2026-06-25 21:16 CST）

- 上一轮候选/结果摘要：本轮按 Path 2 独立 `growth_elastic` 池推进 `momentum_equal_weight_elastic` 的 capacity/cost 变体，没有把 Path 4 emergent_theme 结果并入 Path 2。`scripts/path2_candidate_pass.py` 显示候选池 `879`，`momentum_equal_weight_elastic` 族为 `47` 条。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_total_mv_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`、`core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`；实际命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v46_ids>,<one_path3_id>,<three_path4_prom22_ids>`。
- 五窗口结果：`80/20 total_mv` CAGR `8.54% / 6.30% / 20.21% / 70.87% / 72.57%`，最大回撤 `-15.61% / -14.86% / -9.14% / -8.24% / -8.28%`，换手 `3.57x / 3.21x / 4.14x / 7.81x / 6.91x`；`80/20 equal_weight` CAGR `10.44% / 9.35% / 23.80% / 63.87% / 78.98%`，最大回撤 `-16.67% / -15.74% / -14.99% / -14.99% / -15.13%`。
- 结论：v46 未改变四个 window winner，但 `update_weighted_winners.py` 将 Path 2 robust candidate 切到 `core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`，mean CAGR `25.76%`、min CAGR `9.28%`。这是本轮 A股最明确的可推进信息。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> medium_cycle_growth`。下一轮第一候选建议不要继续只压 cap，而是补一个中周期收益修复确认：`core_explore_80_20_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk24_mom_exit44_reconfirm97_caution56_cap16_cost_guard_v47_medium_cycle_repair` 与 total_mv 对照；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v47_medium_cycle_ids>`。

## 本轮执行计划（2026-06-26 09:46 CST）

- 上一轮候选/结果摘要：上一轮 v46 把 Path 2 robust 切到 `momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`；本轮按 `medium_cycle_growth` 设计中周期收益/确认平衡 v59，保持 Path 2 独立 `growth_elastic` 池，不引入 Path 4 emergent theme。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk30_mom_exit48_reconfirm92_caution60_cap20_cost_guard_v59_medium_cycle_balance` 与 `core_explore_80_20_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk30_mom_exit48_reconfirm92_caution60_cap20_cost_guard_v59_medium_cycle_balance`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-24 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v59_ids>,<one_path3_id>`，随后执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`。
- 五窗口结果：`80/20 total_mv` CAGR `6.17% / 4.44% / 22.30% / 69.58% / 49.73%`，最大回撤 `-20.56% / -20.52% / -14.05% / -12.68% / -12.85%`，换手 `4.24x / 3.88x / 5.24x / 7.82x / 7.13x`；`80/20 equal_weight` CAGR `4.68% / 3.36% / 18.74% / 53.57% / 93.83%`，最大回撤最差 `-26.60%`。
- 结论：v59 有短窗弹性，但 2017/2020 收益太弱且换手偏高；`path2_candidate_pass.py` 后候选池为 `883`，`update_weighted_winners.py` 后 Path 2 window winner、robust candidate 与 tracked payload 均未改变，robust 仍为 v46。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> risk_reconfirm_sensitivity`。下一轮第一候选建议在 v59 上降低风险阈值和确认强度：`aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk28_mom_exit46_reconfirm94_caution58_cap18_cost_guard_v60_reconfirm_balance` 双底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v60_ids>`。

## 本轮执行计划（2026-06-26 20:46 CST）

- 上一轮候选/结果摘要：上一轮留下 v60 风险/确认平衡线，本轮按 Path 2 独立 `growth_elastic` 池执行，不引入 Path 4 emergent theme，也不经由 Path 4 结论评价。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk28_mom_exit46_reconfirm94_caution58_cap18_cost_guard_v60_reconfirm_balance` 与 `core_explore_80_20_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk28_mom_exit46_reconfirm94_caution58_cap18_cost_guard_v60_reconfirm_balance`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-25 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v60_ids>,<one_path3_id>`，随后执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`。
- 五窗口结果：`80/20 total_mv` 刷新到 `2026-06-26` 后 CAGR `7.91% / 6.26% / 20.38% / 69.72% / 52.23%`，最大回撤 `-17.10% / -13.30% / -12.41% / -12.41% / -12.59%`，换手 `3.89x / 3.49x / 4.46x / 7.84x / 7.18x`；`80/20 equal_weight` CAGR `7.72% / 6.80% / 19.92% / 56.02% / 97.84%`，最大回撤最差 `-22.18%`。
- 结论：v60 较 v59 降低了部分回撤，但 2017/2020 收益仍弱，未改变 Path 2 window winner 或 robust candidate；robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`。本轮没有 Path 2 evict。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> medium_cycle_growth`。下一轮第一候选建议停止 v59/v60 的确认小修，回到中周期收益修复：`aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk30_mom_exit48_reconfirm92_caution60_cap16_cost_guard_v61_medium_cycle_repair` 双底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v61_medium_cycle_ids>`。

## 本轮执行计划（2026-06-27 07:44 CST）

- 上一轮候选/结果摘要：上一轮留下 v61 中周期收益修复，本轮按 Path 2 独立 `growth_elastic` 池执行双底座；未引入 Path 4 emergent theme，也未用 Path 4 结果充当 Path 2 结论。
- 本轮候选 ID 与命令：新增 `core_explore_80_20_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk30_mom_exit48_reconfirm92_caution60_cap16_cost_guard_v61_medium_cycle_repair` 与 `core_explore_80_20_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk30_mom_exit48_reconfirm92_caution60_cap16_cost_guard_v61_medium_cycle_repair`；命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v61_ids>,<one_path3_id>`，随后执行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`。
- 五窗口结果：`80/20 total_mv` CAGR `7.13% / 5.74% / 21.89% / 70.31% / 56.96%`，最大回撤 `-20.78% / -17.41% / -12.96% / -12.14% / -12.33%`；`80/20 equal_weight` CAGR `6.84% / 5.85% / 20.83% / 58.71% / 104.05%`，最大回撤最差 `-24.97%`。
- 结论：v61 短窗弹性仍在，但 2017/2020 不足且回撤高于 robust 线；`path2_candidate_pass.py` 与 `update_weighted_winners.py` 后 Path 2 window winner、robust candidate 与 tracked payload 均未改变，robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`。本轮没有 Path 2 evict。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> underrepresented_families`。下一轮暂停 v59-v61 的 `prom4/top10` 小修，第一候选建议切回低相关双周/弹性族并压风险与 cap：`aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap16_cost_guard_v62_underrepresented_lowturn` 双底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-06-26 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v62_underrepresented_ids>`。

## 本轮执行计划（2026-07-02 07:00 CST）

- 上一轮候选/结果摘要：上一轮建议转向低相关 underrepresented，但最终 guard 本轮给出 `medium_cycle_growth`；因此本轮不继续扩双周弹性族，改注册 `prom4/top12` 的 medium-cycle 修复版 v68，保持 Path 2 独立 `growth_elastic` 池，未引入 Path 4 emergent theme。
- 本轮候选 ID 与命令：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm94_caution58_cap16_cost_guard_v68_medium_cycle_growth_repair` 与 `core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk26_mom_exit46_reconfirm94_caution58_cap16_cost_guard_v68_medium_cycle_growth_repair`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <one_path1_id>,<two_path2_v68_ids>,<three_path4_prom26_ids>`，随后运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`。
- 五窗口结果：`90/10 total_mv` CAGR `9.20% / 9.15% / 6.11% / 48.00% / 33.49%`，最大回撤 `-20.98% / -14.38% / -11.92% / -15.41% / -10.98%`，换手 `4.77x / 4.21x / 3.73x / 10.26x / 9.50x`；`90/10 equal_weight` CAGR `5.75% / 5.11% / 10.49% / 29.65% / 55.43%`，最大回撤 `-25.34% / -15.64% / -15.92% / -18.87% / -9.84%`。
- 结论：v68 没有超过现有 medium-cycle official winner；`path2_candidate_pass.py` 后 candidates 为 `803`，最终 guard 显示 `ashare_path2_candidate_universe 803/803 pass`。`update_weighted_winners.py` 后 Path 2 candidate 仍为 `core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top10_risk26_mom_exit46_reconfirm96_caution58_cap18_cost_guard_v34_reconfirm_balance`，mean CAGR `20.91%`、min CAGR `11.85%`；window winners 仍由 v30 与 `top15_risk50_confirm80` 承担。
- 候选池控制：本轮没有 Path 2 evict。candidate universe 已达 `803`，但 Path 2 的 active/candidate 管理仍应优先清理 2017/2020 长窗弱、短窗单票集中过高的旧 high-growth 线，而不是继续堆叠 `prom4/top10/top12` 小修。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> medium_cycle_growth`。下一轮第一候选建议在 v68 的 `cap16/reconfirm94` 基础上只做一次 total_mv 收益修复：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top11_risk28_mom_exit48_reconfirm94_caution60_cap18_cost_guard_v69_medium_cycle_growth_repair`，首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-01 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top11_risk28_mom_exit48_reconfirm94_caution60_cap18_cost_guard_v69_medium_cycle_growth_repair`；若仍弱，暂停 `prom4/top12` 月频小修并回到 underrepresented 族。

## 本轮执行计划（2026-07-03 07:23 CST）

- 上一轮候选/结果摘要：上一轮留下 v69 total_mv 收益修复；本轮按 `growth_elastic` 独立池执行，没有引入 Path 4 emergent theme 结果，也没有通过 Path 4 评价 Path 2。
- 本轮候选 ID 与命令：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top11_risk28_mom_exit48_reconfirm94_caution60_cap18_cost_guard_v69_medium_cycle_growth_repair`；成功命令与 A股其它路径合并为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <six_ashare_ids>`，随后运行 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python scripts/path2_candidate_pass.py`。
- 五窗口结果：CAGR `8.32% / 8.02% / 3.89% / 42.20% / 18.58%`，最大回撤 `-21.95% / -15.87% / -12.03% / -15.64% / -10.86%`，Sharpe `0.5366 / 0.5076 / 0.3170 / 1.1885 / 0.6658`，换手 `4.84x / 4.23x / 3.80x / 10.24x / 9.57x`。v69 没有修复 2020/2023 收益，短窗也不如已有高弹 winners。
- 巡检结果：`path2_candidate_pass.py` 显示 candidates `804`；窗口 winners 仍主要由旧 high-growth / medium-cycle 高收益线承担，robust 仍偏向旧 `risk50_mom_exit60` 线。`update_weighted_winners.py` 后 Path 2 tracked payload 有同步重写，但 v69 是 target-viable fallback，不是干净晋级。
- 候选池控制：本轮没有 Path 2 evict。candidate universe 仍很大，下一轮新增前应清理 2017/2020 长窗弱且短窗高换手的 `prom4/top10/top12` 小修线，避免继续扩同质月频参数。
- 下一轮 focus：若最终 guard 仍为 `medium_cycle_growth`，不要继续只在 v68/v69 上微调；第一候选切回 underrepresented 族的低相关双周/弹性修复，或先淘汰弱 v59-v69 旧线。若必须给首条回测命令，建议注册 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap16_cost_guard_v70_underrepresented_lowturn` 并执行 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-02 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk22_exit42_cap16_cost_guard_v70_underrepresented_lowturn`。

## 本轮执行计划（2026-07-07 05:01 CST）

- 上一轮候选/结果摘要：上一轮 v69 没有修复 2020/2023，本轮按开局 `risk_reconfirm_sensitivity` 执行 v73 双底座；全程保持 Path 2 独立 `growth_elastic` 池，没有把 Path 4 emergent_theme 变体并入扫描池。
- 本轮候选 ID 与命令：`core_explore_90_10_total_mv_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity`、`core_explore_90_10_equal_weight_winner_core__aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk24_mom_exit46_reconfirm98_caution56_cap18_cost_guard_v73_risk_reconfirm_sensitivity`；成功命令为 `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v73_ids>,<one_path3_v2_id>`。
- 五窗口结果：`90/10 total_mv` CAGR `7.01% / 5.95% / 12.38% / 38.85% / 10.62%`，最大回撤 `-21.18% / -20.54% / -14.73% / -15.41% / -13.31%`，换手最高 `10.21x`；`90/10 equal_weight` CAGR `4.12% / 2.89% / 4.84% / 19.40% / 26.19%`，最大回撤最差 `-26.42%`，换手最高 `10.85x`。
- 巡检结论：`scripts/path2_candidate_pass.py` 显示 candidates `808`，window winners 仍为旧 high-growth / medium-cycle 线，robust 仍为 `core_explore_80_20_equal_weight_winner_core__aggr_06_94_prom4_momentum_equal_weight_elastic_top8_risk22_exit42_cap16_cost_guard_v46_capacity_cost`。v73 长窗弱且换手高，不进入 winner/robust/tracked。
- 候选池控制：本轮为控制同质候选，归档 `core_explore_80_20_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn` 与 `core_explore_70_30_equal_weight_winner_core__aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk20_exit40_cap14_cost_guard_v63_underrepresented_lowturn`；evict 原因为 v63 underrepresented 低换手线长窗和 robust 排名弱于 v46/v70。
- 下一轮 focus：最终 guard 给出 `ashare_path2 -> underrepresented_families`。下一轮先停止 v68-v73 月频小修，注册一条更低相关双周弹性候选 `aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_risk14_exit34_cap10_cost_guard_v74_underrepresented_lowturn` 双底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v74_underrepresented_ids>`。
- Final guard 修正：最终 guard 轮换为 `ashare_path2 -> capacity_and_cost_stress / rotate / stagnation_runs=9`。下一轮不要继续扩 v73 的高换手小修，先注册/确认容量成本压力线 `aggr_04_96_prom4_core_6_1_promo_liqmom_top12_risk22_mom_exit44_reconfirm99_caution54_cap16_cost_guard_v74_capacity_cost_stress` 双底座；首条命令为 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-03 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <two_path2_v74_capacity_cost_ids>`。新增前优先归档一组 2017/2020 长窗弱且短窗高换手的旧 prom4/top12 线。
