from __future__ import annotations

import unittest
from unittest.mock import patch

from scripts.export_live_platform_data import build_snapshot_from_live_spec
from scripts.generate_public_snapshot import _resolve_frequency
from scripts.update_weighted_winners import TrackMetrics, _retain_official_in_leaderboard


class LiveExportMetadataTest(unittest.TestCase):
    @patch("scripts.export_live_platform_data.load_strategy_snapshot")
    def test_frequency_defaults_to_snapshot_rebalance_frequency(self, load_snapshot) -> None:
        load_snapshot.return_value = {"rebalance_frequency": "weekly"}
        spec = {
            "market_scope": "a_share",
            "path": "path1",
            "winner_type": "window winner",
            "strategy_id": "test_strategy",
            "sample_tag": "since_2020_01",
            "winner_tags": [],
        }

        snapshot = build_snapshot_from_live_spec(spec)

        self.assertEqual(snapshot["frequency"], "weekly")

    def test_official_incumbent_is_retained_beyond_top_five(self) -> None:
        metrics = TrackMetrics(cagr=0.1, sharpe=1.0, max_drawdown=-0.1, turnover=1.0)
        ranked = [(f"candidate_{index}", metrics) for index in range(1, 8)]

        selected = _retain_official_in_leaderboard(ranked, "candidate_7", 5)

        self.assertEqual([rank for rank, _ in selected], [1, 2, 3, 4, 5, 7])
        self.assertEqual(selected[-1][1][0], "candidate_7")

    def test_public_frequency_falls_back_to_rebalance_frequency(self) -> None:
        self.assertEqual(_resolve_frequency("", {"rebalance_frequency": "biweekly"}), "biweekly")
        self.assertEqual(
            _resolve_frequency("monthly", {"rebalance_frequency": "biweekly"}),
            "monthly",
        )


if __name__ == "__main__":
    unittest.main()
