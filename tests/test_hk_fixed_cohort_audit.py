import unittest

import pandas as pd

from scripts.audit_hk_fixed_cohort import reweight_cohort
from backtest_marketcap_etf import apply_weight_cap_with_redistribution, compute_rebalance_trades


class FixedCohortTest(unittest.TestCase):
    def test_freezes_final_cohort_and_exposure_when_outside_stock_ranks_first(self):
        parent = pd.Series({"A": .4, "B": .2})
        base = pd.Series({"A": 1., "B": 3., "C": 100.})
        signal = pd.Series({"A": .2, "B": .8, "C": 1.})
        quality = pd.Series({"A": .5, "B": .6, "C": 1.})
        weights = reweight_cohort(parent, base, signal, quality, pd.Series(False, index=base.index))
        self.assertEqual(set(weights.index), {"A", "B"})
        self.assertAlmostEqual(weights.sum(), .6)
        self.assertGreater(weights["B"], weights["A"])
        capped, cash = apply_weight_cap_with_redistribution(weights, cap=.25)
        self.assertEqual(set(capped.index), {"A", "B"})
        self.assertLessEqual(capped.max(), .25 + 1e-12)
        self.assertAlmostEqual(capped.sum() + cash, 1.)
        positions, cash_value, _, _, stats = compute_rebalance_trades(
            current_values=pd.Series({"A": .5, "B": .4}), current_cash=.1,
            target_weights=capped, rebalance_date=pd.Timestamp("2026-10-09"),
            tradable_codes=["A", "B"], buy_commission=.001, sell_commission_rate=.002,
            stamp_rate_override=0.)
        self.assertGreaterEqual(cash_value, 0.)
        self.assertAlmostEqual(positions.sum() + cash_value + stats["trading_cost"], 1.)
        self.assertGreater(stats["sell_commission"], 0.)

    def test_missing_input_fails_closed(self):
        parent = pd.Series({"A": .5, "B": .5})
        with self.assertRaises(RuntimeError):
            reweight_cohort(parent, pd.Series({"A": 1.}), parent, parent, parent > 0)

    def test_retains_pre_truncation_ranking_population(self):
        parent = pd.Series({"A": .4, "B": .2})
        base = pd.Series({"A": 1., "B": 1., "C": 1.})
        signal = pd.Series({"A": .2, "B": .8, "C": .5})
        quality = pd.Series({"A": .6, "B": .6, "C": .9})
        breakout = pd.Series(False, index=base.index)
        final_only = reweight_cohort(parent, base, signal, quality, breakout)
        frozen_population = reweight_cohort(parent, base, signal, quality, breakout, set(base.index))
        self.assertEqual(set(frozen_population.index), set(parent.index))
        self.assertAlmostEqual(frozen_population.sum(), parent.sum())
        self.assertNotAlmostEqual(final_only["A"], frozen_population["A"])

    def test_empty_parent_does_not_create_exposure(self):
        self.assertTrue(reweight_cohort(pd.Series(dtype=float), pd.Series({"A": 1.}),
                        pd.Series({"A": 1.}), pd.Series({"A": 1.}), pd.Series({"A": True})).empty)


if __name__ == "__main__":
    unittest.main()
