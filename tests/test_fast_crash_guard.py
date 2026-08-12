from __future__ import annotations

import pandas as pd
import unittest

import backtest_marketcap_etf as backtest


def _market_inputs() -> tuple[pd.Series, pd.DataFrame]:
    dates = pd.bdate_range("2026-05-04", periods=60)
    market = pd.Series(
        [100.0, 102.0, 103.0, 102.0, 94.0],
        index=[dates[19], dates[29], dates[39], dates[49], dates[59]],
    )
    prices = pd.DataFrame(index=dates, columns=["A", "B", "C", "D"], dtype=float)
    prices["A"] = 100.0
    prices["B"] = 100.0
    prices["C"] = 100.0
    prices["D"] = 100.0
    prices.loc[dates[-20] :, ["A", "B", "C"]] = [
        [100.0 - idx] * 3 for idx in range(20)
    ]
    prices.loc[dates[-20] :, "D"] = [100.0 + idx for idx in range(20)]
    return market, prices


class FastCrashGuardTest(unittest.TestCase):
    def test_drawdown_and_combined_trigger_on_price_damage_and_weak_breadth(self) -> None:
        market, prices = _market_inputs()

        drawdown = backtest.compute_fast_crash_state(market, prices, prices.index[-1], mode="drawdown")
        combined = backtest.compute_fast_crash_state(market, prices, prices.index[-1], mode="combined")

        self.assertIs(drawdown["triggered"], True)
        self.assertIs(combined["triggered"], True)
        self.assertLess(float(combined["market_drawdown"]), -0.06)
        self.assertLess(float(combined["weekly_return"]), -0.04)
        self.assertEqual(float(combined["breadth"]), 0.25)

    def test_combined_requires_weak_breadth_while_drawdown_does_not(self) -> None:
        market, prices = _market_inputs()
        rising_prices = prices.copy()
        for code in rising_prices.columns:
            rising_prices.loc[rising_prices.index[-20] :, code] = [100.0 + idx for idx in range(20)]

        drawdown = backtest.compute_fast_crash_state(market, rising_prices, prices.index[-1], mode="drawdown")
        combined = backtest.compute_fast_crash_state(market, rising_prices, prices.index[-1], mode="combined")

        self.assertIs(drawdown["triggered"], True)
        self.assertIs(combined["triggered"], False)
        self.assertEqual(float(combined["breadth"]), 1.0)

    def test_can_delever_in_one_step_and_recover_slowly(self) -> None:
        state = {"confirmed_stage": "risk_on", "pending_stage": None, "pending_count": 0}

        risk_off, state = backtest.apply_buffered_stage_transition(
            raw_stage="risk_off",
            state=state,
            confirm_weeks=2,
            risk_off_confirm_weeks=1,
            risk_on_confirm_weeks=4,
            stepwise=False,
        )
        first_recovery, state = backtest.apply_buffered_stage_transition(
            raw_stage="risk_on",
            state=state,
            confirm_weeks=2,
            risk_off_confirm_weeks=1,
            risk_on_confirm_weeks=4,
            stepwise=True,
        )

        self.assertEqual(risk_off, "risk_off")
        self.assertEqual(first_recovery, "risk_off")
        self.assertEqual(state["pending_count"], 1)

    def test_candidate_registration_is_path_separated(self) -> None:
        self.assertEqual(len(backtest.PATH1_CRASH_RESILIENCE_BASE_IDS), 4)
        self.assertEqual(len(backtest.PATH2_CRASH_RESILIENCE_BASE_IDS), 3)
        self.assertEqual(len(backtest.PATH7_CRASH_RESILIENCE_BASE_IDS), 3)
        self.assertTrue(all("total_mv" in item for item in backtest.PATH1_CRASH_RESILIENCE_BASE_IDS))
        self.assertTrue(all("60_40_equal_weight" in item for item in backtest.PATH2_CRASH_RESILIENCE_BASE_IDS))
        self.assertTrue(all(item.endswith("defbar") for item in backtest.PATH7_CRASH_RESILIENCE_BASE_IDS))
        self.assertTrue(set(backtest.CRASH_RESILIENCE_ACTIVE_BASE_IDS) <= set(backtest.CRASH_RESILIENCE_BASE_IDS))
        self.assertFalse(set(backtest.CRASH_RESILIENCE_BASE_IDS) & backtest.get_winner_only_base_ids())


if __name__ == "__main__":
    unittest.main()
