from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.update_weighted_winners import coverage_scope_is_blocked


class CoverageScopeGateTests(unittest.TestCase):
    def test_blocks_only_matching_explicit_blocking_scope(self) -> None:
        payload = {
            "coverage_gate": {
                "status": "block",
                "scopes": [
                    {
                        "scope_id": "ashare_path2_candidate_universe",
                        "blocking": True,
                        "status": "block",
                    },
                    {
                        "scope_id": "ashare_path1_fast_family",
                        "blocking": False,
                        "status": "warn",
                    },
                ],
            }
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            self.assertTrue(coverage_scope_is_blocked("ashare_path2_candidate_universe", path))
            self.assertFalse(coverage_scope_is_blocked("ashare_path1_fast_family", path))

    def test_missing_or_invalid_report_fails_open(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.json"
            invalid = Path(directory) / "invalid.json"
            invalid.write_text("not-json", encoding="utf-8")
            self.assertFalse(coverage_scope_is_blocked("ashare_path2_candidate_universe", missing))
            self.assertFalse(coverage_scope_is_blocked("ashare_path2_candidate_universe", invalid))


if __name__ == "__main__":
    unittest.main()
