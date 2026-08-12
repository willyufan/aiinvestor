from __future__ import annotations

import unittest

from scripts.research_iteration_guard import _update_state


class ResearchIterationGuardTest(unittest.TestCase):
    def test_same_as_of_and_signature_does_not_increment_stagnation(self) -> None:
        previous_state = {
            "as_of": "2026-08-06",
            "paths": {
                "ashare_path1": {
                    "signature": "same",
                    "stagnation_runs": 2,
                    "last_changed_at": "2026-08-06T08:00:00+08:00",
                }
            },
        }

        state = _update_state(
            previous_state=previous_state,
            signatures={"ashare_path1": "same"},
            quotas={},
            as_of="2026-08-06",
            stagnation_threshold=3,
        )

        self.assertEqual(state["paths"]["ashare_path1"]["stagnation_runs"], 2)
        self.assertEqual(state["paths"]["ashare_path1"]["rotation_status"], "continue")

    def test_new_as_of_with_same_signature_increments_once(self) -> None:
        previous_state = {
            "as_of": "2026-08-05",
            "paths": {
                "ashare_path1": {
                    "signature": "same",
                    "stagnation_runs": 2,
                    "last_changed_at": "2026-08-05T08:00:00+08:00",
                }
            },
        }

        state = _update_state(
            previous_state=previous_state,
            signatures={"ashare_path1": "same"},
            quotas={},
            as_of="2026-08-06",
            stagnation_threshold=3,
        )

        self.assertEqual(state["paths"]["ashare_path1"]["stagnation_runs"], 3)
        self.assertEqual(state["paths"]["ashare_path1"]["rotation_status"], "rotate")


if __name__ == "__main__":
    unittest.main()
