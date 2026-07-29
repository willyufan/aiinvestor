# A股 Path6：2025/2026 短窗收益竞争路径

Path6 与 Path1-5 独立，alpha pool 为 `short_window_return_max`。目标顺序是 `since_2025_01` / `since_2026_01` CAGR，其次才是 MaxDD、Sharpe、turnover 和成本。路径内短窗领先不等于跨窗口 robust winner；未完成 2017/2020/2023 确认前不进入 A股正式 winner payload。

## 上一轮候选与结果摘要（2026-07-22）

- 本轮为 Path6 首轮，无上一轮历史候选。已实跑 6 个 base id 的 `since_2025_01` / `since_2026_01`，估值截止日均为 `2026-07-21`。
- 路径内 2025 winner 为 `core_explore_80_20_equal_weight_winner_core__path6_short_window_weekly_pullback_top3_cashoff_v4_weekly`：CAGR `44.63%`、Sharpe `1.0514`、MaxDD `-28.69%`、年换手 `1770.47%`；但 2026 CAGR `-24.21%`，判定 `reject`。
- 路径内 2026 winner 为 `core_explore_80_20_total_mv_winner_core__path6_short_window_weekly_balanced_top4_risk15_v3_weekly`：CAGR `6.94%`、Sharpe `0.3646`、MaxDD `-21.03%`、年换手 `1806.72%`；2025 CAGR `-1.84%`，判定 `reject`。
- 唯一保留观察为 `core_explore_80_20_total_mv_winner_core__path6_short_window_monthly_3_1_top2_risk15_v5`：2025/2026 CAGR `42.99% / -12.99%`、Sharpe `0.9305 / -0.1518`、MaxDD `-30.78% / -19.54%`、年换手 `665.83% / 600.64%`，判定 `keep_watch`。它显著落后同截止日现有短窗冠军（2025/2026 CAGR `234.38% / 125.46%`），不是 promote。
- `v1/v2/v3/v4/v6` 均为 `reject`；原因是两个目标窗口无法同时维持正收益，且周频形态年换手达 `1597%-2491%`。无 evict 历史快照；这 5 个 ID 不进入 active/watchlist。
- 完整对比见 `results/research/a_share/path6_short_window_scorecard.json`。

## 本轮候选 ID 与命令

- 实验假设：独立短窗 alpha pool、周频快速跟踪和月频集中动量能在不依赖 Path5 事件审计的情况下，同时抬升 2025/2026 CAGR。实际只有月频 `v5` 在 2025 显示弹性，周频高换手假设不成立。
- 实际命令：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_equal_weight_winner_core__path6_short_window_monthly_midcycle_top3_risk20_v6,core_explore_80_20_equal_weight_winner_core__path6_short_window_weekly_breakout_top3_risk10_v2_weekly,core_explore_80_20_equal_weight_winner_core__path6_short_window_weekly_pullback_top3_cashoff_v4_weekly,core_explore_80_20_total_mv_winner_core__path6_short_window_monthly_3_1_top2_risk15_v5,core_explore_80_20_total_mv_winner_core__path6_short_window_weekly_balanced_top4_risk15_v3_weekly,core_explore_80_20_total_mv_winner_core__path6_short_window_weekly_breakout_top6_risk25_v1_weekly`。
- 该命令前一次未带 `--end-date` 的尝试被 stale-cache 护栏拒绝：缓存只到 `2026-07-21`，不会把失败尝试计为实验。

## 下一轮 focus 提示

- 主 focus：以月频 `v5` 为唯一 active/watch 种子，先修复 2026 负收益，观察条件是 2026 CAGR 转正、MaxDD 不差于 `-20%`、年换手不高于 `700%`。
- 下轮第一条可执行确认命令：`.venv/bin/python backtest_marketcap_etf.py --end-date 2026-07-21 --sample-tags since_2025_01,since_2026_01 --only-base-ids core_explore_80_20_total_mv_winner_core__path6_short_window_monthly_3_1_top2_risk15_v5`。
- 待探索候选：`path6_short_window_monthly_3_1_top4_risk25_v7`、`path6_short_window_monthly_3_1_top6_risk30_v8`、`path6_short_window_monthly_3_1_liquidity_guard_v9`、`path6_short_window_monthly_3_1_cost_guard_v10`。先注册再执行，不再扩展已 reject 的周频突破同形参数。

## Focus 候选池

- `short_window_breakout`：`path6_short_window_monthly_breakout_top4_risk20_v11`、`path6_short_window_monthly_breakout_top6_risk25_v12`。
- `short_window_momentum`：`path6_short_window_monthly_3_1_top4_risk25_v7`、`path6_short_window_monthly_3_1_top6_risk30_v8`。
- `concentration_risk`：`path6_short_window_monthly_3_1_cap25_v13`、`path6_short_window_monthly_3_1_cap35_v14`。
- `turnover_cost`：`path6_short_window_monthly_3_1_liquidity_guard_v9`、`path6_short_window_monthly_3_1_cost_guard_v10`。
