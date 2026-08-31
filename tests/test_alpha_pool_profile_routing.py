from __future__ import annotations

import unittest

import backtest_marketcap_etf as ashare


class AlphaPoolProfileRoutingTest(unittest.TestCase):
    def test_path1_core_multifactor_precedes_generic_path2_prefix(self) -> None:
        strategy_base_id = (
            "core_explore_80_20_total_mv_winner_core__"
            "aggr_08_92_prom6_core_multifactor_quality_profitability_signal_cost_guard_reconfirm"
        )

        self.assertEqual(
            ashare.get_strategy_alpha_pool_profile({"strategy_base_id": strategy_base_id}),
            ashare.ALPHA_POOL_PROFILE_CORE_EXPLORE_SEED,
        )

    def test_path2_liquidity_momentum_stays_in_growth_pool(self) -> None:
        strategy_base_id = (
            "core_explore_60_40_equal_weight_winner_core__"
            "aggr_03_97_prom3_core_6_1_liqmom_elastic_biweekly_"
            "risk22_exit42_cap18_cost_guard_v35_lowturn"
        )

        self.assertEqual(
            ashare.get_strategy_alpha_pool_profile({"strategy_base_id": strategy_base_id}),
            ashare.ALPHA_POOL_PROFILE_GROWTH_ELASTIC,
        )


if __name__ == "__main__":
    unittest.main()
