import unittest

import numpy as np
import pandas as pd

from backtest_marketcap_etf import compute_rebalance_trades


class RebalanceCashBudgetTest(unittest.TestCase):
    def trade(self, values, cash, target, tradable, buy=0.0, sell=0.0, stamp=0.0):
        result = compute_rebalance_trades(
            pd.Series(values, dtype=float), cash, pd.Series(target, dtype=float),
            pd.Timestamp("2026-10-08"), tradable,
            buy_commission=buy, sell_commission_rate=sell, stamp_rate_override=stamp,
        )
        positions, remaining, gross, gross_cash, stats = result
        nav = sum(values.values()) + cash
        self.assertGreaterEqual(remaining, -1e-12)
        self.assertGreaterEqual(gross_cash, -1e-12)
        self.assertAlmostEqual(positions.sum() + remaining + stats["trading_cost"], nav)
        self.assertAlmostEqual(gross.sum() + gross_cash, nav)
        self.assertAlmostEqual(remaining, cash + stats["sell_amount"] - stats["buy_amount"] - stats["trading_cost"])
        self.assertLessEqual(positions.sum(), stats["post_trade_nav"] + 1e-12)
        self.assertAlmostEqual(sum(t["fee"] for t in stats["trade_details"]), stats["trading_cost"])
        return result

    def test_frozen_small_sale_does_not_fund_new_position(self):
        positions, cash, _, _, stats = self.trade(
            {"A": .5, "B": .5}, 0, {"A": .495, "B": .48, "C": .025}, ["A", "B", "C"],
        )
        self.assertAlmostEqual(positions["A"], .5)
        self.assertAlmostEqual(positions["C"], .02)
        self.assertAlmostEqual(cash, 0)
        self.assertNotIn("A", [t["ts_code"] for t in stats["trade_details"]])

    def test_purchase_budget_reserves_both_sides_fees(self):
        positions, cash, _, _, stats = self.trade(
            {"A": .5, "B": .5}, 0, {"A": .495, "B": .48, "C": .025},
            ["A", "B", "C"], buy=.003, sell=.002, stamp=.005,
        )
        self.assertAlmostEqual(positions["A"], .5)
        self.assertAlmostEqual(stats["buy_amount"] * 1.003, stats["sell_amount"] * .993)
        self.assertAlmostEqual(cash, 0)

    def test_locked_position_and_forced_exit_keep_funding_identity(self):
        positions, _, _, _, _ = self.trade(
            {"LOCKED": .4, "EXIT": .05, "B": .55}, 0,
            {"B": .6, "C": .4}, ["EXIT", "B", "C"], buy=.003, sell=.002, stamp=.005,
        )
        self.assertAlmostEqual(positions["LOCKED"], .4)
        self.assertNotIn("EXIT", positions.index)

    def test_small_trades_stay_buffered_when_cash_is_sufficient(self):
        positions, cash, _, _, stats = self.trade(
            {"A": .5, "B": .4}, .1, {"A": .495, "B": .4}, ["A", "B"],
        )
        self.assertEqual(stats["buy_amount"] + stats["sell_amount"], 0)
        self.assertAlmostEqual(positions["A"], .5)
        self.assertAlmostEqual(cash, .1)

    def test_random_targets_with_locked_holdings_and_fees(self):
        rng = np.random.default_rng(20261009)
        codes = ["A", "B", "C", "D"]
        for _ in range(100):
            current = rng.dirichlet(np.ones(5))
            target = rng.dirichlet(np.ones(5))[:4]
            with self.subTest(current=current, target=target):
                self.trade(dict(zip(codes, current[:4])), current[4], dict(zip(codes, target)),
                           codes[1:] if rng.random() < .5 else codes,
                           buy=.003, sell=.002, stamp=.005)


if __name__ == "__main__":
    unittest.main()
