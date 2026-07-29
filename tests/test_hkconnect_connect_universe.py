import unittest

import pandas as pd

from backtest_hkconnect import filter_replaced_hk_connect_codes, repair_hk_forward_adj_close_continuity


class HkconnectConnectUniverseTest(unittest.TestCase):
    def test_filter_replaced_hk_connect_codes_prefers_new_code(self) -> None:
        latest = pd.DataFrame(
            [
                {"ts_code": "02525.HK", "name": "禾赛-W(新)"},
                {"ts_code": "02983.HK", "name": "禾赛-W(旧)"},
                {"ts_code": "09999.HK", "name": "普通标的"},
            ]
        )

        filtered = filter_replaced_hk_connect_codes(latest)

        self.assertEqual(filtered["ts_code"].tolist(), ["02525.HK", "09999.HK"])

    def test_filter_replaced_hk_connect_codes_keeps_unmatched_old_code(self) -> None:
        latest = pd.DataFrame([{"ts_code": "02983.HK", "name": "禾赛-W(旧)"}])

        filtered = filter_replaced_hk_connect_codes(latest)

        self.assertEqual(filtered["ts_code"].tolist(), ["02983.HK"])

    def test_repair_forward_adjusted_price_across_delayed_split_factor(self) -> None:
        daily = pd.DataFrame(
            [
                {
                    "trade_date": "2026-07-09",
                    "close": 128.80,
                    "pre_close": 131.50,
                    "forward_adj_close": 128.80,
                },
                {
                    "trade_date": "2026-07-10",
                    "close": 16.57,
                    "pre_close": 16.10,
                    "forward_adj_close": 16.57,
                },
                {
                    "trade_date": "2026-07-28",
                    "close": 15.52,
                    "pre_close": 14.96,
                    "forward_adj_close": 15.52,
                },
                {
                    "trade_date": "2026-07-29",
                    "close": 16.49,
                    "pre_close": 15.52,
                    "forward_adj_close": 131.92,
                },
            ]
        )

        repaired = repair_hk_forward_adj_close_continuity(daily)

        self.assertAlmostEqual(repaired.iloc[0]["forward_adj_close"], 128.80)
        self.assertAlmostEqual(repaired.iloc[1]["forward_adj_close"], 132.56)
        self.assertAlmostEqual(repaired.iloc[2]["forward_adj_close"], 124.16)
        self.assertAlmostEqual(repaired.iloc[3]["forward_adj_close"], 131.92)
