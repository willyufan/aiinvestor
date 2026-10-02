import unittest
from unittest.mock import patch

import pandas as pd

from scripts.export_live_platform_data import _build_ashare_2026_leaderboards


class ArchivedWeeklyLeaderboardTests(unittest.TestCase):
    def test_archived_weekly_candidate_cannot_enter_display_ranking(self):
        archived = "core_explore_80_20_equal_weight_winner_core__archived_weekly"
        active = "core_explore_80_20_equal_weight_winner_core__active_weekly"
        frame = pd.DataFrame({"strategy_base_id": [archived, active]})
        seen = []

        def rank(frame, tag, *, allowed_base_ids):
            seen.append(allowed_base_ids)
            return []

        module = "scripts.update_weighted_winners."
        with (
            patch("scripts.export_live_platform_data.pd.read_csv", return_value=frame),
            patch(module + "_latest_per_strategy_window", side_effect=lambda df: df),
            patch(module + "_augment_with_synthetic_windows", side_effect=lambda df: df),
            patch(module + "load_archived_path_ids", return_value=(set(), {archived})),
            patch(module + "load_path1_family_ids", return_value=set()),
            patch(module + "load_path4_theme_ids", return_value=set()),
            patch(module + "_matches_path2", return_value=False),
            patch(module + "_build_strategy_map", return_value={}),
            patch(module + "_filter_ids_to_current_as_of", side_effect=lambda df, ids: df),
            patch(module + "_rank_single_window_candidates", side_effect=rank),
        ):
            _build_ashare_2026_leaderboards()
        self.assertEqual(seen, [{active}])


if __name__ == "__main__":
    unittest.main()
