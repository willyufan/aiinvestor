from __future__ import annotations

import unittest

from scripts.export_live_platform_data import (
    StaleStrategyValuationError,
    _validate_strategy_valuation_freshness,
)


class LiveValuationFreshnessTest(unittest.TestCase):
    def test_accepts_latest_trading_day_valuation(self) -> None:
        _validate_strategy_valuation_freshness(
            base_id="monthly_strategy",
            sample_tag="since_2020_01",
            market_scope="hkconnect",
            market_data_as_of="2026-07-21",
            summary={"sample_end": "2026-07-21"},
        )

    def test_rejects_last_rebalance_date_as_valuation_end(self) -> None:
        with self.assertRaisesRegex(
            StaleStrategyValuationError,
            "valuation_as_of=2026-06-30.*raw data_as_of=2026-07-21",
        ):
            _validate_strategy_valuation_freshness(
                base_id="monthly_strategy",
                sample_tag="since_2020_01",
                market_scope="hkconnect",
                market_data_as_of="2026-07-21",
                summary={"sample_end": "2026-06-30"},
            )

    def test_rejects_metadata_only_latest_valuation_date(self) -> None:
        with self.assertRaises(StaleStrategyValuationError):
            _validate_strategy_valuation_freshness(
                base_id="monthly_strategy",
                sample_tag="since_2020_01",
                market_scope="hkconnect",
                market_data_as_of="2026-07-21",
                summary={
                    "sample_end": "2026-06-30",
                    "latest_valuation_date": "2026-07-21",
                    "latest_formal_signal_date": "2026-06-30",
                },
            )


if __name__ == "__main__":
    unittest.main()
