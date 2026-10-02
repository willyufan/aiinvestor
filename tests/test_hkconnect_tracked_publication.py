import unittest
from unittest.mock import patch

import pandas as pd

from scripts.export_live_platform_data import _build_hkconnect_leaderboards, load_hkconnect_registry


class TrackedPublicationTests(unittest.TestCase):
    def test_higher_raw_rank_does_not_override_tracked_roles(self):
        approved = "hkconnect_path2_approved"
        watch = "hkconnect_path2_watch"
        frame = pd.DataFrame([
            dict(strategy_id=sid, strategy_name=sid, path="path2", sample_tag="since_2026_01",
                 sample_end="2026-10-02", cagr=cagr, max_drawdown=-0.2, sharpe_ratio=1.0,
                 average_annual_turnover=2.0, total_return=cagr, rebalance_frequency="monthly")
            for sid, cagr in [(approved, 0.2), (watch, 0.3)]
        ])
        tracked = {"tracks": {"path2": {
            "since_2026_01": {"winner": approved},
            "robust_candidate": {"strategy_id": approved},
        }}}
        module = "scripts.export_live_platform_data."
        with (
            patch(module + "pd.read_csv", return_value=frame),
            patch(module + "prepare_hk_candidate_frames", return_value=(frame, frame, pd.Timestamp("2026-10-02"), 0)),
            patch(module + "load_json", return_value=tracked),
            patch(module + "_pick_hk_robust_candidate", return_value=None),
        ):
            registry = load_hkconnect_registry()
            leaderboard = _build_hkconnect_leaderboards(frame)["path2"]["since_2026_01"]["entries"]
        self.assertEqual([row["strategy_id"] for row in registry], [approved])
        self.assertIn("hkconnect:path2:robust candidate", registry[0]["winner_tags"])
        self.assertEqual(leaderboard[0]["strategy_base_id"], watch)
        self.assertFalse(leaderboard[0]["is_official_winner"])
        self.assertTrue(leaderboard[1]["is_official_winner"])


if __name__ == "__main__":
    unittest.main()
