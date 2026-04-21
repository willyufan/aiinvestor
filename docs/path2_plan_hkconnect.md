# 沪港通 Path 2 研究计划

## 定位
- 独立于当前 A 股 Path 2
- 仅限沪港通标的（当前使用 Tushare `stock_hsgt` 最新可得名单作为静态池）
- 目标：优先冲收益上限，尤其观察 2020 / 2023 窗口能否出现高弹性赢家

## 当前独立候选族
1. 高集中突破（monthly / biweekly / weekly）
2. 高成长主线（monthly / biweekly）
3. 动量 / 等权高弹性（monthly / weekly）

## 本轮迭代执行规则

- 沪港通 `Path 2` 作为**独立于 A 股**的研究线，每轮迭代都要单独评估，不复用 A 股 `scripts/path2_candidate_pass.py` 的 winner 结论。
- 默认回测窗口固定为：
  - `since_2017_01`
  - `since_2020_01`
  - `since_2023_01`
  - `since_2025_01`
  - `since_2026_01`（观察窗）
- 默认比较对象固定为当前 7 个港股 `Path 2` 候选：
  - `hkconnect_path2_breakout_monthly`
  - `hkconnect_path2_breakout_biweekly`
  - `hkconnect_path2_breakout_weekly`
  - `hkconnect_path2_theme_monthly`
  - `hkconnect_path2_theme_biweekly`
  - `hkconnect_path2_equal_elastic_monthly`
  - `hkconnect_path2_equal_elastic_weekly`
- 下一轮港股 `Path 2` 的晋级优先顺序固定为：
  1. `since_2020_01` 是否显著改善
  2. `since_2023_01` 是否维持高收益上限
  3. `MaxDD / Turnover` 是否仍在可接受范围
- 重点输出每个候选族的最优代表，并明确列出：
  - `Total Return`
  - `CAGR`
  - `MaxDD`
  - `Sharpe`
  - `Turnover`
- 若港股 `Path 2` 任一窗口赢家发生变化，需同步更新：
  - `results_hkconnect/strategy_comparison_hkconnect.csv`
  - 实盘平台导出层中的沪港通策略注册表
  - README/HISTORY（若当前轮允许更新）

## 当前默认推进结论

- 港股 `Path 2` 当前默认仍优先看：
  - `2020` 窗口能否继续抬高
  - `2023` 窗口能否维持爆发力
- 双周 / 单周候选继续保留，但不因为更高频而自动获得更高优先级。
- 若某候选只强化 `2025 / 2026` 而不能改善 `2020`，默认不作为下一轮主攻方向。

## 当前假设
- 港股高弹性标的对双周 / 单周调仓频率可能更敏感
- 单纯提高频率未必足够，必须和更高集中、更偏突破的信号结合
- 港股回撤天然更大，因此 Path 2 不先追求低回撤，而先追求收益上限

## 近期优先看
- 2020 / 2023 窗口的 CAGR 抬升
- 周频 / 双周频是否只放大换手，还是能真正提高收益上限
- 2026 观察窗是否出现“周频过拟合”

## 已知限制
- 当前不是严格的历史动态沪港通池，而是“最新可得名单静态池”
- 当前没有接入港股财务质量因子，更多依赖动量、突破、流动性与波动
- 若当前 Tushare key 无 `stock_hsgt` 权限，可手工提供 `data_cache/hkconnect/basic/stock_hsgt_manual.csv` 作为静态池输入
