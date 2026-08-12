from __future__ import annotations

from types import SimpleNamespace
import unittest

import pandas as pd

from backtest_hkconnect import (
    get_formal_rebalance_signal_dates,
    get_rebalance_signal_dates,
)
from backtest_marketcap_etf import (
    build_month_boundaries,
    compute_metrics,
    formal_calendar_required_end_date,
    get_formal_rebalance_signal_dates as get_a_share_formal_rebalance_signal_dates,
    get_rebalance_signal_dates as get_a_share_rebalance_signal_dates,
)


def _prepared(latest_date: str) -> SimpleNamespace:
    index = pd.DatetimeIndex(pd.to_datetime(["2026-06-30", "2026-07-21"] if latest_date == "2026-07-21" else [latest_date]))
    return SimpleNamespace(
        month_end_dates=[pd.Timestamp("2026-05-29"), pd.Timestamp("2026-06-30")],
        monthly_period_end_dates=[pd.Timestamp("2026-05-29"), pd.Timestamp("2026-06-30")],
        week_end_dates=[
            pd.Timestamp("2026-06-26"),
            pd.Timestamp("2026-07-03"),
            pd.Timestamp("2026-07-10"),
            pd.Timestamp("2026-07-17"),
        ],
        price_ffill=pd.DataFrame({"TEST.HK": [1.0] * len(index)}, index=index),
    )


class HkconnectValuationScheduleTest(unittest.TestCase):
    def test_formal_calendar_fetch_extends_through_cross_month_week_end(self) -> None:
        self.assertEqual(
            formal_calendar_required_end_date(pd.Timestamp("2026-08-31")),
            pd.Timestamp("2026-09-04"),
        )

    def test_month_end_does_not_complete_a_cross_month_week(self) -> None:
        formal_calendar = pd.DataFrame(
            {
                "cal_date": pd.date_range("2026-08-24", "2026-08-31", freq="D"),
            }
        )
        formal_calendar["is_open"] = (formal_calendar["cal_date"].dt.weekday < 5).astype(int)

        _, _, week_end_dates, _, _ = build_month_boundaries(
            formal_calendar,
            formal_calendar=formal_calendar,
        )

        self.assertEqual(week_end_dates, [pd.Timestamp("2026-08-28")])

    def test_incomplete_week_is_not_a_formal_week_end(self) -> None:
        formal_calendar = pd.DataFrame(
            {
                "cal_date": pd.date_range("2026-07-27", "2026-08-07", freq="D"),
            }
        )
        formal_calendar["is_open"] = (formal_calendar["cal_date"].dt.weekday < 5).astype(int)
        usable_calendar = formal_calendar.loc[
            formal_calendar["cal_date"] <= pd.Timestamp("2026-08-06")
        ].copy()

        _, _, week_end_dates, _, _ = build_month_boundaries(
            usable_calendar,
            formal_calendar=formal_calendar,
        )

        self.assertEqual(week_end_dates, [pd.Timestamp("2026-07-31")])

    def test_closed_friday_keeps_thursday_as_formal_week_end(self) -> None:
        formal_calendar = pd.DataFrame(
            {
                "cal_date": pd.date_range("2026-08-03", "2026-08-07", freq="D"),
                "is_open": [1, 1, 1, 1, 0],
            }
        )
        usable_calendar = formal_calendar.loc[
            formal_calendar["cal_date"] <= pd.Timestamp("2026-08-06")
        ].copy()

        _, _, week_end_dates, _, _ = build_month_boundaries(
            usable_calendar,
            formal_calendar=formal_calendar,
        )

        self.assertEqual(week_end_dates, [pd.Timestamp("2026-08-06")])

    def test_monthly_appends_latest_day_without_extra_rebalance(self) -> None:
        schedule = get_rebalance_signal_dates(_prepared("2026-07-21"), "monthly")
        self.assertEqual(schedule[-2:], [pd.Timestamp("2026-06-30"), pd.Timestamp("2026-07-21")])

    def test_biweekly_preserves_parity_and_appends_latest_day(self) -> None:
        schedule = get_rebalance_signal_dates(_prepared("2026-07-21"), "biweekly")
        self.assertEqual(
            schedule,
            [pd.Timestamp("2026-07-03"), pd.Timestamp("2026-07-17"), pd.Timestamp("2026-07-21")],
        )

    def test_weekly_does_not_duplicate_completed_week_end(self) -> None:
        schedule = get_rebalance_signal_dates(_prepared("2026-07-17"), "weekly")
        self.assertEqual(schedule[-1], pd.Timestamp("2026-07-17"))
        self.assertEqual(schedule.count(pd.Timestamp("2026-07-17")), 1)

    def test_a_share_biweekly_also_appends_latest_valuation_day(self) -> None:
        schedule = get_a_share_rebalance_signal_dates(_prepared("2026-07-21"), "biweekly")
        self.assertEqual(
            schedule,
            [pd.Timestamp("2026-07-03"), pd.Timestamp("2026-07-17"), pd.Timestamp("2026-07-21")],
        )

    def test_latest_valuation_day_is_not_a_formal_period_end(self) -> None:
        prepared = _prepared("2026-07-21")

        self.assertNotIn(
            pd.Timestamp("2026-07-21"),
            get_formal_rebalance_signal_dates(prepared, "biweekly"),
        )
        self.assertNotIn(
            pd.Timestamp("2026-07-21"),
            get_a_share_formal_rebalance_signal_dates(prepared, "biweekly"),
        )

    def test_partial_period_is_excluded_from_fixed_frequency_metrics(self) -> None:
        equity_curve = pd.DataFrame(
            {
                "date": pd.to_datetime(["2026-01-01", "2026-01-31", "2026-02-28", "2026-03-10"]),
                "nav": [1.0, 1.1, 1.045, 1.254],
                "drawdown": [0.0, 0.0, -0.05, 0.0],
            }
        )
        period_returns = pd.DataFrame(
            {
                "date": pd.to_datetime(["2026-01-31", "2026-02-28", "2026-03-10"]),
                "net_return": [0.10, -0.05, 0.20],
                "is_partial_period": [False, False, True],
            }
        )
        turnover = pd.DataFrame(
            {
                "one_way_turnover": [0.20, 0.20, 0.20],
                "trading_cost": [0.001, 0.001, 0.001],
            }
        )

        metrics = compute_metrics(equity_curve, period_returns, turnover)

        complete_returns = period_returns.loc[~period_returns["is_partial_period"], "net_return"]
        complete_std = complete_returns.std(ddof=1)
        elapsed_years = 68 / 365.25
        self.assertAlmostEqual(metrics["monthly_win_rate"], 0.5)
        self.assertAlmostEqual(metrics["annual_volatility"], complete_std * (12.0 ** 0.5))
        self.assertAlmostEqual(
            metrics["sharpe_ratio"],
            complete_returns.mean() / complete_std * (12.0 ** 0.5),
        )
        self.assertAlmostEqual(metrics["cagr"], 1.254 ** (1 / elapsed_years) - 1)
        self.assertAlmostEqual(metrics["average_annual_turnover"], 0.60 / elapsed_years)


if __name__ == "__main__":
    unittest.main()
