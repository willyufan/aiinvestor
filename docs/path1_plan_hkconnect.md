# 沪港通 Path 1 研究计划

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
1. 月度稳健（混合权重）
2. 月度熊市空仓
3. 月度等权缓冲
4. 月度低波偏稳

## 本轮迭代执行规则

- 沪港通 `Path 1` 作为**独立于 A 股**的研究线，每轮迭代都要单独评估，不并入 A 股 `winner_only_pass`。
- 默认回测窗口固定为：
  - `since_2017_01`
  - `since_2020_01`
  - `since_2023_01`
  - `since_2025_01`
  - `since_2026_01`（观察窗）
- 默认比较对象固定为当前 4 个港股 `Path 1` 候选：
  - `hkconnect_path1_monthly_hybrid`
  - `hkconnect_path1_monthly_cashoff`
  - `hkconnect_path1_monthly_equal_buffered`
  - `hkconnect_path1_monthly_lowvol`
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
  - `hkconnect_path1_monthly_equal_buffered`
- `monthly_cashoff` 保留为更防守的候选。
- `monthly_hybrid / monthly_lowvol` 继续作为对照，不轻易移出，直到多轮窗口表现明显失去竞争力。

## 近期优先看
- 2017 / 2020 / 2023 三个窗口的 CAGR、MaxDD、Sharpe
- 2026 观察窗是否出现过强的终点效应

## 已知限制
- 受 `stock_hsgt` 历史覆盖限制，当前不是严格的历史动态沪港通池，而是“最新可得名单静态池”
- 当前交易成本仍是近似模型，先用于研究排序，不用于精确实盘估值
- 若当前 Tushare key 无 `stock_hsgt` 权限，可手工提供 `data_cache/hkconnect/basic/stock_hsgt_manual.csv` 作为静态池输入
