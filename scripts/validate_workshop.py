# SPDX-License-Identifier: MIT
"""Validate the portable Personal AI Workshop repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "WORKSHOP.md",
    "LICENSING.md",
    "LICENSE-CODE",
    "LICENSE-CONTENT",
    "adviser/ADVISER.md",
    "adviser/PACKAGE_CATALOG.json",
    "package-core/PACKAGE_CORE.md",
    "package-core/package-manifest.schema.json",
    "post-box/post-box.schema.json",
    "experience/experience.schema.json",
)
PACKAGE_REQUIRED = {
    "schema_version",
    "id",
    "name",
    "version",
    "purpose",
    "entry_role",
    "risk_level",
    "validators",
    "human_gates",
    "entrypoint",
}
RISK_LEVELS = {"low", "medium", "high"}
LOCAL_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|mailto:|#)([^)]+)\)")
SECRET_PATTERNS = {
    "OpenAI key": re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
PRIVATE_MARKERS = (
    "FIELD_NOTES_DRAFT",
    "C:\\Users\\",
    "/Users/",
    "0_MISSION_CONTROL/",
)


def json_file(path: Path, errors: list[str]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
        return None


def validate(root: Path = ROOT) -> list[str]:
    global ROOT
    previous_root = ROOT
    ROOT = root.resolve()
    errors: list[str] = []
    try:
        for relative in REQUIRED:
            if not (ROOT / relative).is_file():
                errors.append(f"missing required file: {relative}")

        for path in ROOT.rglob("*.json"):
            json_file(path, errors)

        catalog_path = ROOT / "adviser/PACKAGE_CATALOG.json"
        catalog = json_file(catalog_path, errors) if catalog_path.is_file() else None
        if isinstance(catalog, dict):
            packages = catalog.get("packages")
            if not isinstance(packages, list):
                errors.append("catalog field 'packages' must be a list")
            else:
                for entry in packages:
                    if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
                        errors.append("every catalog entry needs a string path")
                        continue
                    target = (ROOT / entry["path"]).resolve()
                    if not target.is_dir():
                        errors.append(f"catalog path does not exist: {entry['path']}")

        manifests = list((ROOT / "examples").glob("*/package.json"))
        if not manifests:
            errors.append("no example package manifests found")
        for path in manifests:
            data = json_file(path, errors)
            if not isinstance(data, dict):
                continue
            missing = sorted(PACKAGE_REQUIRED - data.keys())
            if missing:
                errors.append(f"{path.relative_to(ROOT)} missing: {', '.join(missing)}")
            if data.get("schema_version") != "workshop.package.v1":
                errors.append(f"{path.relative_to(ROOT)} has unsupported schema_version")
            if data.get("risk_level") not in RISK_LEVELS:
                errors.append(f"{path.relative_to(ROOT)} has invalid risk_level")
            entrypoint = data.get("entrypoint")
            if isinstance(entrypoint, str) and not (path.parent / entrypoint).is_file():
                errors.append(f"{path.relative_to(ROOT)} entrypoint does not exist")

        for path in ROOT.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for raw_target in LOCAL_LINK.findall(text):
                target = raw_target.split("#", 1)[0].replace("%20", " ")
                if target and not (path.parent / target).resolve().exists():
                    errors.append(f"broken link in {path.relative_to(ROOT)}: {raw_target}")

        text_extensions = {".md", ".json", ".py", ".txt", ""}
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in text_extensions:
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(text):
                    errors.append(f"possible {label} in {path.relative_to(ROOT)}")
            if path.name != "validate_workshop.py":
                for marker in PRIVATE_MARKERS:
                    if marker in text:
                        errors.append(f"private workspace marker in {path.relative_to(ROOT)}: {marker}")
    finally:
        ROOT = previous_root
    return sorted(set(errors))


def main() -> int:
    errors = validate()
    if errors:
        print(f"WORKSHOP VALIDATION: FAIL ({len(errors)} issue(s))")
        for error in errors:
            print(f"- {error}")
        return 1
    print("WORKSHOP VALIDATION: PASS")
    print("required files, JSON, catalog routes, manifests, links, and disclosure scan: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
