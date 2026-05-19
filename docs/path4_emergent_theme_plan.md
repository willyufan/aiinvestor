# Path 4 强主题涌现路径

## 定位

Path 4 用来捕捉从市场结构中自动涌现的强主题，不使用人工主题名单，也不把“半导体、存储”等事后标签写进策略。ETF 先不纳入，本阶段只在现有 A 股股票动态池内探索。

## 信号原则

- 主题只能从已有截面数据中自然产生：行业相对强度、行业内龙头强度、3-1 动量、近 1 月收益、成交额放量、20 日突破。
- 不做显性主题归类，避免后视镜。
- 财务质量仍保留为底线，但强主题路径会降低质量分位门槛，避免强趋势早期被传统质量筛选过早拦下。
- 回测执行规则不变：信号来自收盘数据，收益从下一个交易日调仓后开始计算。

## 第一批候选

本轮新增 `core_signal_mode = emergent_theme` 与 `promotion_signal_mode = emergent_theme`，并先观察 3 个底座乘 4 个变体：

- `core_explore_80_20_total_mv_winner_core`
- `core_explore_90_10_equal_weight_winner_core`
- `core_explore_90_10_total_mv_winner_core`

变体：

- `aggr_02_98_prom2_emergent_theme_cash_off_and_cap95`
- `aggr_02_98_prom2_emergent_theme_risk40_cap90`
- `aggr_05_95_prom3_emergent_theme_risk40_cap70`
- `aggr_08_92_prom6_emergent_theme_risk50_cap50`

## 迭代规则

- `research_iteration_guard.py` 会把 12 个强主题候选作为独立 coverage scope 检查，要求覆盖 `since_2017_01 / since_2020_01 / since_2023_01 / since_2025_01 / since_2026_01`。
- `path2_candidate_pass.py` 会把这些候选归入独立 family `emergent_theme_discovery`，用于和 Path 2 其他探索族横向比较。
- 第一阶段不直接改写 official winner；等五窗口完整后，再决定是否独立展示为 Path 4 winner 或并入现有 winner 体系。

## 本轮执行计划（2026-05-20 05:20 CST）

- 开局 guard 为 `block / blocking=12 / scope=ashare_path4_emergent_theme`；按 report 原始 rerun command 优先补齐 12 个强主题候选的五窗口覆盖，没有替换成全量回测。首次未锁 `--end-date` 触发本地 A 股缓存只到 `2026-05-19` 的 stale guard；随后使用离线缓存并显式锁定 `--end-date 2026-05-19` 完成补跑。
- 覆盖补跑命令：
  `AIINVESTOR_FORCE_OFFLINE=1 .venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_emergent_theme_cash_off_and_cap95,core_explore_80_20_total_mv_winner_core__aggr_02_98_prom2_emergent_theme_risk40_cap90,core_explore_80_20_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70,core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk50_cap50,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_emergent_theme_cash_off_and_cap95,core_explore_90_10_equal_weight_winner_core__aggr_02_98_prom2_emergent_theme_risk40_cap90,core_explore_90_10_equal_weight_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70,core_explore_90_10_equal_weight_winner_core__aggr_08_92_prom6_emergent_theme_risk50_cap50,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_emergent_theme_cash_off_and_cap95,core_explore_90_10_total_mv_winner_core__aggr_02_98_prom2_emergent_theme_risk40_cap90,core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70,core_explore_90_10_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk50_cap50`。
- `scripts/path2_candidate_pass.py` 已把 `emergent_theme_discovery` 识别为独立 family，`12/12` candidates complete。按 2017/2020/2023 最低 CAGR 看，较稳的候选是 `core_explore_80_20_total_mv_winner_core__aggr_08_92_prom6_emergent_theme_risk50_cap50`，五窗口 CAGR `21.26% / 20.61% / 30.79% / 93.62% / 136.50%`，最差回撤 `-39.74%`，换手 `3.72x-6.16x`；短窗很强，但回撤仍深且 2026 观察窗可能受单票/少数强票影响。
- 另一个较稳候选 `core_explore_90_10_total_mv_winner_core__aggr_05_95_prom3_emergent_theme_risk40_cap70` 五窗口 CAGR 为 `19.43% / 21.99% / 35.66% / 140.82% / 35.50%`，最差回撤 `-39.50%`，换手最高到 `8.51x`；上限高但容量与成本压力更重。
- 本阶段未改写 official winner/tracked/top5，只作为 Path 4 独立观察；guard 收尾为 `pass / blocking=0 / warning=0`。Path 4 候选池为 `12`，未触发 evict。
- 下一轮 focus -> candidates 池按 report quota 先走 `theme_signal_quality` 与 `theme_risk_control`：建议实现 `aggr_05_95_prom3_emergent_theme_quality_gate_risk40_cap70` 与 `aggr_08_92_prom6_emergent_theme_risk30_cap50`，第一条命令用 `.venv/bin/python backtest_marketcap_etf.py --end-date 2026-05-19 --sample-tags since_2017_01,since_2020_01,since_2023_01,since_2025_01,since_2026_01 --only-base-ids <new_path4_theme_ids>`。
