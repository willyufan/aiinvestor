import unittest

import pandas as pd

from scripts.strategy_phase_attribution import compare_periods


class AttributionTest(unittest.TestCase):
    def frame(self):
        return pd.DataFrame({"date": ["2026-01-01", "2026-02-01"],
            "gross_return": [.1, -.05], "net_return": [.09, -.06],
            "trading_cost": [.01, .01], "market_risk_off": [False, True]})

    def test_matches_dates_before_conditional_grouping(self):
        a = self.frame()
        result = compare_periods(a.iloc[::-1], a)
        self.assertEqual(result["matched_periods"], 2)
        for group in result["risk_groups"].values():
            self.assertAlmostEqual(group["delta_gross_log_return"], 0.)
            self.assertAlmostEqual(group["delta_net_log_return"], 0.)
            self.assertGreater(group["candidate_cost_log_drag"], 0.)

    def test_missing_date_and_different_regime_fail_closed(self):
        a = self.frame()
        with self.assertRaises(ValueError):
            compare_periods(a, a.iloc[:1])
        b = a.copy()
        b.loc[0, "market_risk_off"] = True
        with self.assertRaises(ValueError):
            compare_periods(a, b)


if __name__ == "__main__":
    unittest.main()
