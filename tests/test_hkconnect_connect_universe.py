import unittest

import pandas as pd

from backtest_hkconnect import filter_replaced_hk_connect_codes


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
