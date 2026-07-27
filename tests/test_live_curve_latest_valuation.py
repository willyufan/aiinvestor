from __future__ import annotations

import unittest

from live_trading_platform import render_exposure_return_curve


class LiveCurveLatestValuationTest(unittest.TestCase):
    def test_monthly_curve_appends_latest_valuation_without_fake_rebalance(self) -> None:
        html = render_exposure_return_curve(
            snapshots=[
                {
                    "date": "2026-05-29",
                    "holdings": [
                        {"ts_code": "TEST", "weight": 0.8},
                        {"ts_code": "CASH", "weight": 0.2},
                    ],
                },
                {
                    "date": "2026-06-30",
                    "holdings": [
                        {"ts_code": "TEST", "weight": 1.0},
                        {"ts_code": "CASH", "weight": 0.0},
                    ],
                },
            ],
            equity_curve_points=[
                {"date": "2026-05-29", "nav": 2.10},
                {"date": "2026-06-30", "nav": 2.20},
                {"date": "2026-07-21", "nav": 2.4258},
            ],
            start_date="2026-05-29",
            end_date="2026-07-21",
            latest_valuation_date="2026-07-21",
            latest_holdings=[
                {"ts_code": "TEST", "weight": 1.0},
                {"ts_code": "CASH", "weight": 0.0},
            ],
        )

        self.assertIn("2026-07-21", html)
        self.assertIn("区间收益率 142.58%", html)
        self.assertIn("共 2 个调仓快照，另含最新估值点 2026-07-21", html)

    def test_weekly_or_biweekly_curve_does_not_duplicate_existing_endpoint(self) -> None:
        html = render_exposure_return_curve(
            snapshots=[
                {
                    "date": "2026-07-17",
                    "holdings": [
                        {"ts_code": "TEST", "weight": 0.7},
                        {"ts_code": "CASH", "weight": 0.3},
                    ],
                },
                {
                    "date": "2026-07-21",
                    "holdings": [
                        {"ts_code": "TEST", "weight": 0.9},
                        {"ts_code": "CASH", "weight": 0.1},
                    ],
                },
            ],
            equity_curve_points=[
                {"date": "2026-07-17", "nav": 1.10},
                {"date": "2026-07-21", "nav": 1.12},
            ],
            start_date="2026-07-17",
            end_date="2026-07-21",
            latest_valuation_date="2026-07-21",
        )

        self.assertIn("区间收益率 12.00%", html)
        self.assertIn("共 2 个调仓快照。", html)
        self.assertNotIn("另含最新估值点", html)


if __name__ == "__main__":
    unittest.main()
