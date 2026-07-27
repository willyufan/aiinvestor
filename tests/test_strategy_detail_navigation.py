from __future__ import annotations

import unittest
from unittest.mock import patch

from live_trading_platform import (
    filter_rebalance_change_rows,
    render_history_snapshot_blocks,
    strategy_detail_html,
)


class StrategyDetailNavigationTest(unittest.TestCase):
    def test_change_filters_cover_attribution_and_actions(self) -> None:
        rows = [
            {"source_type": "trade", "action": "新增"},
            {"source_type": "mixed", "action": "加仓"},
            {"source_type": "drift", "action": "减仓"},
            {"source_type": "trade", "action": "清仓"},
        ]

        self.assertEqual(3, len(filter_rebalance_change_rows(rows, "trade")))
        self.assertEqual(1, len(filter_rebalance_change_rows(rows, "drift")))
        self.assertEqual([rows[0]], filter_rebalance_change_rows(rows, "new"))
        self.assertEqual([rows[3]], filter_rebalance_change_rows(rows, "exit"))
        self.assertEqual(rows, filter_rebalance_change_rows(rows, "unknown"))

    def test_history_snapshots_expand_only_the_latest_record(self) -> None:
        history_html = render_history_snapshot_blocks(
            [
                {
                    "date": "2026-06-30",
                    "holdings": [
                        {"ts_code": "000001.SZ", "name": "测试一", "weight": 0.8},
                        {"ts_code": "CASH", "name": "现金", "weight": 0.2},
                    ],
                },
                {
                    "date": "2026-05-29",
                    "holdings": [
                        {"ts_code": "000002.SZ", "name": "测试二", "weight": 0.6},
                        {"ts_code": "CASH", "name": "现金", "weight": 0.4},
                    ],
                },
            ]
        )

        self.assertEqual(2, history_html.count("<details class='history-snapshot'"))
        self.assertEqual(1, history_html.count("<details class='history-snapshot' open>"))
        self.assertIn("1 只持仓 · 总仓位 80.00%", history_html)

    @patch("live_trading_platform.load_strategy_trade_events", return_value=tuple())
    @patch(
        "live_trading_platform.get_strategy_favorite_state",
        return_value={"is_favorite": False, "is_pinned": False},
    )
    @patch("live_trading_platform.load_strategy_snapshot")
    def test_detail_defaults_to_recent_history_and_renders_decision_summary_and_filters(
        self,
        load_snapshot,
        _favorite_state,
        _trade_events,
    ) -> None:
        first_page = {
            "window_index": 0,
            "label": "2026-05-29 → 2026-06-30",
            "start_date": "2026-05-29",
            "end_date": "2026-06-30",
            "snapshot_count": 2,
            "snapshots": [
                {
                    "date": "2026-06-30",
                    "holdings": [
                        {"ts_code": "000001.SZ", "name": "测试一", "weight": 0.6},
                        {"ts_code": "000003.SZ", "name": "测试三", "weight": 0.4},
                        {"ts_code": "CASH", "name": "现金", "weight": 0.0},
                    ],
                },
                {
                    "date": "2026-05-29",
                    "holdings": [
                        {"ts_code": "000001.SZ", "name": "测试一", "weight": 0.5},
                        {"ts_code": "000002.SZ", "name": "测试二", "weight": 0.5},
                        {"ts_code": "CASH", "name": "现金", "weight": 0.0},
                    ],
                },
            ],
        }
        second_page = {
            "window_index": 1,
            "label": "2026-04-30 → 2026-04-30",
            "start_date": "2026-04-30",
            "end_date": "2026-04-30",
            "snapshot_count": 1,
            "snapshots": [
                {
                    "date": "2026-04-30",
                    "holdings": [
                        {"ts_code": "000002.SZ", "name": "测试二", "weight": 1.0},
                        {"ts_code": "CASH", "name": "现金", "weight": 0.0},
                    ],
                }
            ],
        }
        active_view = {
            "updated_at": "2026-07-24",
            "rebalance_frequency": "monthly",
            "summary_metrics": {
                "total_return": 0.2,
                "cagr": 0.1,
                "max_drawdown": -0.08,
                "sharpe_ratio": 1.2,
                "average_annual_turnover": 1.5,
            },
            "target_total_exposure": 1.0,
            "risk_state": "risk_on",
            "latest_weights": [
                {"ts_code": "000001.SZ", "name": "测试一", "weight": 0.6, "latest_price": 12.0},
                {"ts_code": "000003.SZ", "name": "测试三", "weight": 0.4, "latest_price": 18.0},
                {"ts_code": "CASH", "name": "现金", "weight": 0.0, "latest_price": None},
            ],
            "history_windows": [first_page, second_page],
            "trade_events": [],
            "equity_curve_points": [
                {"date": "2026-04-30", "nav": 1.0},
                {"date": "2026-05-29", "nav": 1.1},
                {"date": "2026-06-30", "nav": 1.15},
                {"date": "2026-07-24", "nav": 1.2},
            ],
            "formal_schedule": {
                "data_as_of": "2026-07-24",
                "schedule_kind": "monthly",
                "suggestion_effective_date": "2026-06-30",
                "basket_effective_date": "2026-06-30",
                "exposure_effective_date": "2026-06-30",
            },
            "summary_meta": {
                "sample_start": "2026-01-01",
                "sample_end": "2026-07-24",
                "latest_valuation_date": "2026-07-24",
                "sample_label": "2026年至今",
            },
            "sample_tag": "since_2026_01",
            "sample_tag_label": "2026年至今",
        }
        load_snapshot.return_value = {
            "strategy_id": "test_monthly",
            "display_name": "测试月频策略",
            "market_scope": "a_share",
            "path": "path1",
            "winner_type": "window winner",
            "adjustment_style": "月度换股",
            "sample_tag": "since_2026_01",
            "windows": {
                "since_2026_01": {
                    "total_return": 0.2,
                    "cagr": 0.4,
                    "max_drawdown": -0.08,
                    "sharpe": 1.2,
                    "turnover": 1.5,
                }
            },
            "sample_views": {"since_2026_01": active_view},
            "winner_tags": [],
        }

        detail_html = strategy_detail_html("test_monthly")

        self.assertIn("当前决策摘要", detail_html)
        self.assertIn("持仓估值截至", detail_html)
        self.assertIn("2026-07-24", detail_html)
        self.assertIn("目标总仓位", detail_html)
        self.assertIn("当前持仓", detail_html)
        self.assertNotIn("当前建议时点", detail_html)
        self.assertIn("每页最多 12 次", detail_html)
        self.assertIn("更早记录 →", detail_html)
        self.assertEqual(2, detail_html.count("<details class='history-snapshot'"))
        self.assertIn("共 3 个调仓快照，另含最新估值点 2026-07-24", detail_html)
        self.assertIn("真实交易 0", detail_html)
        self.assertIn("市值漂移 3", detail_html)
        self.assertIn("change_filter=drift", detail_html)


if __name__ == "__main__":
    unittest.main()
