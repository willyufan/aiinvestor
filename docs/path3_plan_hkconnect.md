# 沪港通 Path 3 周度高频路径

## 2026-05-09 18:09 CST 复核

- 本轮继续运行五窗口离线回测，Path 3 候选数保持 `13`，全部为 `weekly`；结果单独写入 `results_hkconnect/tracked_winners_hkconnect.json` 与 `docs/strategy_comparison_hkconnect_path3.png`。
- 当前 Path 3 tracked winners 继续全部由 `hkconnect_path3_theme_fast_weekly` 占据：`since_2020_01` 为 `23.47% CAGR / -33.61% MaxDD / 0.9339 Sharpe / 30.48 Turnover`，`since_2023_01` 为 `40.80% / -19.56% / 1.3152 / 29.62`，`since_2025_01` 为 `78.07% / -17.81% / 1.7677 / 34.71`。
- 四窗口 robust candidate 同为 `hkconnect_path3_theme_fast_weekly`，`meanCAGR=41.45% / minCAGR=23.47% / worstMaxDD=-33.61% / meanTurn=31.32`。
- `since_2026_01` 只观察，当前 raw leader 是 `hkconnect_path3_equal_elastic_weekly`；下一轮优先围绕 `theme_fast_weekly` 做降换手/降回撤变体，而不是继续单纯提高 weekly 进攻强度。

## 2026-05-09 三路径拆分基线

- 本轮将沪港通研究线拆为三条独立路径：Path 1 维护实盘稳健线，Path 2 维护月度/双周高收益探索线，Path 3 只维护纯周度信号、纯周度换股候选。
- 代码侧新增 `HK_PATH3_VARIANTS`，从原有单周候选复制为 `hkconnect_path3_*` 独立 ID；Path 1/Path 2 不再承载单周换股候选。
- 当前 Path 3 候选数为 `13`，全部为 `weekly`；五窗口回测完成后已同步 `results_hkconnect/tracked_winners_hkconnect.json` 与 `docs/strategy_comparison_hkconnect_path3.png`。

当前 Path 3 tracked winners：

- `since_2017_01 / since_2020_01`：`hkconnect_path3_theme_fast_weekly`，`23.47% CAGR / -33.61% MaxDD / 0.9339 Sharpe / 30.48 Turnover`。
- `since_2023_01`：`hkconnect_path3_theme_fast_weekly`，`40.80% CAGR / -19.56% MaxDD / 1.3152 Sharpe / 29.62 Turnover`。
- `since_2025_01`：`hkconnect_path3_theme_fast_weekly`，`78.07% CAGR / -17.81% MaxDD / 1.7677 Sharpe / 34.71 Turnover`。
- 四窗口 robust candidate：`hkconnect_path3_theme_fast_weekly`，`meanCAGR=41.45% / minCAGR=23.47% / worstMaxDD=-33.61% / meanTurn=31.32`。

观察结论：

- 纯周度线的收益弹性明显强于 Path 2 的中长窗口月频锚点，但换手也显著更高。
- 当前 Path 3 的核心问题不是短窗强度，而是 `30x+` 年化换手和 `-33.61%` 最差回撤是否能被实际交易成本、流动性和仓位约束接受。
- 下一轮优先围绕 `theme_fast_weekly` 做降换手/降回撤变体，而不是继续单纯提高周度进攻强度。
