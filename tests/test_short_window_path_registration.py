from __future__ import annotations

import unittest

import pandas as pd

import backtest_hkconnect as hk
import backtest_marketcap_etf as ashare
from scripts.research_iteration_guard import SHORT_WINDOW_RETURN_WINDOWS, _extract_path6_short_window_candidates
from scripts.update_hkconnect_artifacts import _build_payload as _build_hk_payload
from scripts.update_short_window_path_artifacts import _build_scorecard
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
        active_path6_ids = {
            strategy_id
            for strategy_id in ashare.get_active_strategy_base_ids()
            if "__path6_short_window_" in strategy_id
        }
        self.assertEqual(active_path6_ids, set(ashare.PATH6_SHORT_WINDOW_BASE_IDS))
        self.assertEqual(SHORT_WINDOW_RETURN_WINDOWS, ("since_2025_01", "since_2026_01"))

    def test_hk_path8_is_registered_as_an_independent_expansion_path(self) -> None:
        path8_ids = {str(variant["strategy_id"]) for variant in hk.HK_PATH8_VARIANTS}
        expansion_ids = {str(variant["strategy_id"]) for variant in hk.HK_EXPANSION_VARIANTS}
        self.assertEqual(len(path8_ids), 6)
        self.assertLessEqual(path8_ids, expansion_ids)
        self.assertTrue(all(variant["path"] == "path8" for variant in hk.HK_PATH8_VARIANTS))
        self.assertTrue(all(variant["signal_family"] == "path8_short_window_momentum" for variant in hk.HK_PATH8_VARIANTS))
        self.assertTrue(hk.is_hk_variant_sample_supported(hk.HK_PATH8_VARIANTS[0], "since_2025_01"))
        self.assertTrue(hk.is_hk_variant_sample_supported(hk.HK_PATH8_VARIANTS[0], "since_2026_01"))
        self.assertFalse(hk.is_hk_variant_sample_supported(hk.HK_PATH8_VARIANTS[0], "since_2023_01"))

    def test_hk_path8_tracked_artifact_only_contains_short_windows_without_robust(self) -> None:
        rows = []
        for sample_tag in (
            "since_2017_01",
            "since_2020_01",
            "since_2023_01",
            "since_2025_01",
            "since_2026_01",
        ):
            rows.append(
                {
                    "strategy_id": "hkconnect_path8_test",
                    "strategy_name": "Path8 test",
                    "path": "path8",
                    "candidate_family": "short_window_momentum",
                    "rebalance_frequency": "weekly",
                    "sample_tag": sample_tag,
                    "sample_start": "2025-01-01",
                    "sample_end": "2026-08-06",
                    "total_return": 0.10,
                    "cagr": 0.20,
                    "max_drawdown": -0.10,
                    "sharpe_ratio": 1.0,
                    "average_annual_turnover": 2.0,
                }
            )
        frame = pd.DataFrame(rows)

        payload = _build_hk_payload(frame, ranking_latest=frame)

        self.assertEqual(set(payload["tracks"]["path8"]), set(hk.HK_PATH8_SAMPLE_TAGS))
        self.assertNotIn("robust_candidate", payload["tracks"]["path8"])
        self.assertEqual(
            set(payload["strategies"]["hkconnect_path8_test"]["windows"]),
            set(hk.HK_PATH8_SAMPLE_TAGS),
        )

    def test_short_window_scorecard_rejects_mixed_candidate_dates(self) -> None:
        rows = []
        for candidate_id, sample_end in (("candidate_a", "2026-08-05"), ("candidate_b", "2026-08-06")):
            for sample_tag in SHORT_WINDOW_RETURN_WINDOWS:
                rows.append(
                    {
                        "strategy_base_id": candidate_id,
                        "sample_tag": sample_tag,
                        "sample_start": "2025-01-01",
                        "sample_end": sample_end,
                        "cagr": 0.20,
                        "sharpe_ratio": 1.0,
                        "max_drawdown": -0.10,
                        "average_annual_turnover": 2.0,
                        "cumulative_trading_cost": 0.01,
                    }
                )

        with self.assertRaisesRegex(RuntimeError, "mixed sample_end dates"):
            _build_scorecard(
                frame=pd.DataFrame(rows),
                id_column="strategy_base_id",
                candidate_ids=["candidate_a", "candidate_b"],
                archived_ids=set(),
                market="ashare",
                path="path6",
            )


if __name__ == "__main__":
    unittest.main()
