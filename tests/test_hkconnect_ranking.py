from __future__ import annotations

import json
import unittest

import numpy as np
import pandas as pd

from backtest_hkconnect import HK_ARCHIVED_STRATEGY_IDS
from scripts.export_live_platform_data import _build_hkconnect_leaderboards
from scripts.hkconnect_ranking import prepare_hk_candidate_frames
from scripts.update_hkconnect_artifacts import _build_payload


def _row(
    strategy_id: str,
    sample_end: str,
    *,
    sample_tag: str = "since_2020_01",
    cagr: float | str = 0.1,
    sharpe_ratio: float = 0.8,
    max_drawdown: float = -0.2,
    turnover: float = 1.5,
    total_return: float = 0.5,
) -> dict[str, object]:
    return {
        "strategy_id": strategy_id,
        "strategy_name": strategy_id,
        "path": "path1",
        "candidate_family": "test",
        "rebalance_frequency": "monthly",
        "sample_tag": sample_tag,
        "sample_start": "2020-01-01",
        "sample_end": sample_end,
        "cagr": cagr,
        "sharpe_ratio": sharpe_ratio,
        "max_drawdown": max_drawdown,
        "average_annual_turnover": turnover,
        "total_return": total_return,
    }


class HkconnectRankingTest(unittest.TestCase):
    def test_prepare_filters_archived_stale_invalid_and_superseded_rows(self) -> None:
        frame = pd.DataFrame(
            [
                _row("active", "2026-07-01", cagr=0.05),
                _row("active", "2026-07-20", cagr=0.20),
                _row("stale", "2026-06-01"),
                _row("archived", "2026-07-20"),
                _row("malformed", "2026-07-20", cagr="not-a-number"),
                _row(
                    "invalid",
                    "2026-07-21",
                    cagr=0.0,
                    sharpe_ratio=np.nan,
                    max_drawdown=0.0,
                    turnover=0.0,
                    total_return=0.0,
                ),
            ]
        )

        catalog, ranking, cutoff, stale_count = prepare_hk_candidate_frames(
            frame,
            archived_strategy_ids={"archived"},
        )

        self.assertEqual(set(catalog["strategy_id"]), {"active", "stale"})
        self.assertEqual(set(ranking["strategy_id"]), {"active"})
        self.assertEqual(float(catalog.loc[catalog["strategy_id"] == "active", "cagr"].iloc[0]), 0.20)
        self.assertEqual(cutoff, pd.Timestamp("2026-06-29"))
        self.assertEqual(stale_count, 1)

    def test_newer_invalid_row_does_not_advance_zero_day_cutoff(self) -> None:
        frame = pd.DataFrame(
            [
                _row("active", "2026-07-20"),
                _row(
                    "invalid",
                    "2026-07-21",
                    cagr=0.0,
                    sharpe_ratio=np.nan,
                    max_drawdown=0.0,
                    turnover=0.0,
                    total_return=0.0,
                ),
            ]
        )

        catalog, ranking, cutoff, stale_count = prepare_hk_candidate_frames(
            frame,
            archived_strategy_ids=set(),
            max_staleness_days=0,
        )

        self.assertEqual(list(catalog["strategy_id"]), ["active"])
        self.assertEqual(list(ranking["strategy_id"]), ["active"])
        self.assertEqual(cutoff, pd.Timestamp("2026-07-20"))
        self.assertEqual(stale_count, 0)

    def test_filtered_payload_is_strict_json(self) -> None:
        frame = pd.DataFrame(
            [
                _row("active", "2026-07-20"),
                _row(
                    "invalid",
                    "2026-07-20",
                    cagr=0.0,
                    sharpe_ratio=np.nan,
                    max_drawdown=0.0,
                    turnover=0.0,
                    total_return=0.0,
                ),
            ]
        )
        catalog, ranking, _cutoff, _stale_count = prepare_hk_candidate_frames(
            frame,
            archived_strategy_ids=set(),
        )

        payload = _build_payload(catalog, ranking_latest=ranking)
        encoded = json.dumps(payload, allow_nan=False)

        self.assertNotIn("invalid", payload["strategies"])
        self.assertNotIn("NaN", encoded)

    def test_live_leaderboard_uses_shared_candidate_filters(self) -> None:
        archived_id = next(iter(HK_ARCHIVED_STRATEGY_IDS))
        frame = pd.DataFrame(
            [
                _row("active", "2026-07-20"),
                _row("stale", "2026-06-01", cagr=0.9),
                _row(archived_id, "2026-07-20", cagr=0.8),
                _row(
                    "invalid",
                    "2026-07-20",
                    cagr=0.0,
                    sharpe_ratio=np.nan,
                    max_drawdown=0.0,
                    turnover=0.0,
                    total_return=0.0,
                ),
            ]
        )

        leaderboards = _build_hkconnect_leaderboards(frame)

        entries = leaderboards["path1"]["since_2020_01"]["entries"]
        self.assertEqual([entry["strategy_base_id"] for entry in entries], ["active"])


if __name__ == "__main__":
    unittest.main()
