# SPDX-License-Identifier: MIT
"""Tests for the repository validator."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_workshop import validate  # noqa: E402


class WorkshopValidatorTests(unittest.TestCase):
    def test_repository_is_valid(self) -> None:
        self.assertEqual(validate(ROOT), [])

    def test_missing_manifest_field_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / "repo"
            shutil.copytree(ROOT, copy)
            manifest = copy / "examples/observer-package/package.json"
            data = json.loads(manifest.read_text(encoding="utf-8"))
            del data["purpose"]
            manifest.write_text(json.dumps(data), encoding="utf-8")
            errors = validate(copy)
            self.assertTrue(any("missing: purpose" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()

