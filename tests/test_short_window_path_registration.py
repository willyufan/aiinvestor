from __future__ import annotations

import unittest

import backtest_hkconnect as hk
import backtest_marketcap_etf as ashare
from scripts.research_iteration_guard import SHORT_WINDOW_RETURN_WINDOWS, _extract_path6_short_window_candidates
from scripts.update_weighted_winners import load_path6_short_window_ids


class ShortWindowPathRegistrationTest(unittest.TestCase):
    def test_ashare_path6_is_registered_and_isolated_from_path2_and_path3(self) -> None:
        self.assertEqual(len(ashare.PATH6_SHORT_WINDOW_VARIANT_IDS), 6)
        self.assertEqual(len(ashare.PATH6_SHORT_WINDOW_BASE_IDS), 6)
        self.assertTrue(all("__path6_short_window_" in candidate_id for candidate_id in ashare.PATH6_SHORT_WINDOW_BASE_IDS))
        self.assertTrue(
            all(not ashare.is_path2_scan_strategy_base_id(candidate_id) for candidate_id in ashare.PATH6_SHORT_WINDOW_BASE_IDS)
        )
        self.assertEqual(set(load_path6_short_window_ids()), set(ashare.PATH6_SHORT_WINDOW_BASE_IDS))
        self.assertEqual(
            set(_extract_path6_short_window_candidates({"PATH6_SHORT_WINDOW_BASE_IDS": ashare.PATH6_SHORT_WINDOW_BASE_IDS})),
            set(ashare.PATH6_SHORT_WINDOW_BASE_IDS),
        )
        self.assertEqual(SHORT_WINDOW_RETURN_WINDOWS, ("since_2025_01", "since_2026_01"))

    def test_hk_path8_is_registered_as_an_independent_expansion_path(self) -> None:
        path8_ids = {str(variant["strategy_id"]) for variant in hk.HK_PATH8_VARIANTS}
        expansion_ids = {str(variant["strategy_id"]) for variant in hk.HK_EXPANSION_VARIANTS}
        self.assertEqual(len(path8_ids), 6)
        self.assertLessEqual(path8_ids, expansion_ids)
        self.assertTrue(all(variant["path"] == "path8" for variant in hk.HK_PATH8_VARIANTS))
        self.assertTrue(all(variant["signal_family"] == "path8_short_window_momentum" for variant in hk.HK_PATH8_VARIANTS))


if __name__ == "__main__":
    unittest.main()
