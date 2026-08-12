from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCORECARD_DIR = ROOT / "results" / "research" / "a_share"


def _reject_nonstandard_constant(value: str) -> None:
    raise ValueError(f"non-standard JSON constant: {value}")


class ResearchScorecardJsonTest(unittest.TestCase):
    def test_all_scorecards_are_strict_json(self) -> None:
        scorecards = sorted(SCORECARD_DIR.glob("research_iteration_scorecard_*.json"))
        self.assertTrue(scorecards, "expected at least one research iteration scorecard")

        for path in scorecards:
            with self.subTest(path=path.name):
                json.loads(
                    path.read_text(encoding="utf-8"),
                    parse_constant=_reject_nonstandard_constant,
                )


if __name__ == "__main__":
    unittest.main()
