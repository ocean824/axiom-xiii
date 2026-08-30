#!/usr/bin/env python3
"""Validate AXIOM-XIII bootstrap repository invariants without external dependencies."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "docs/source/AXIOM-XIII-V1-Master-Specification.md"
EXPECTED_MASTER_SHA256 = "dc7feae7b999e8c4802ef8fb67fa894c68e75e8cf1f601132ccb162f6565909d"
LOCKED_NAVIGATION = "GAMES · MEDIA · SOCIAL · DEV · STORE · PROFILE · WALLET"

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "CODESPRING.md",
    ROOT / "AGENTS.md",
    ROOT / "LICENSE",
    ROOT / "SECURITY.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CODEOWNERS",
    ROOT / "docs/source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md",
    ROOT / "docs/analysis/deep-analysis.md",
    ROOT / "docs/architecture/system-map.md",
    ROOT / "docs/domains/README.md",
    ROOT / "docs/requirements/requirements-register.md",
    ROOT / "docs/roadmap/implementation-roadmap.md",
    ROOT / "docs/roadmap/v1-160-tickets.md",
    ROOT / ".agents/PROJECT_MEMORY.md",
    ROOT / "docs/security/threat-model-v0.md",
    ROOT / "docs/legal/provenance-and-license-policy-v0.md",
    ROOT / "docs/validation/repository-readiness.md",
]

REQUIRED_DIRECTORIES = [
    "apps",
    "engine",
    "ai",
    "connect",
    "bridge",
    "protocol",
    "chain",
    "services",
    "pyramid",
    "sdk",
    "games",
    "tools",
    "tests",
    "infra",
    "third_party",
]

PROHIBITED_SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ghp_[A-Za-z0-9]{30,}"),
    re.compile(r"sk-[A-Za-z0-9]{32,}"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def validate() -> list[str]:
    errors: list[str] = []

    if not MASTER.is_file():
        fail(f"Missing canonical master specification: {MASTER}", errors)
    else:
        actual = sha256(MASTER)
        if actual != EXPECTED_MASTER_SHA256:
            fail(
                "Canonical master specification checksum mismatch: "
                f"expected {EXPECTED_MASTER_SHA256}, found {actual}",
                errors,
            )
        master_text = MASTER.read_text(encoding="utf-8")
        if LOCKED_NAVIGATION not in master_text:
            fail("Locked seven-tab navigation is missing from the master specification", errors)

    for path in REQUIRED_FILES:
        if not path.is_file():
            fail(f"Missing required file: {path.relative_to(ROOT)}", errors)

    for relative in REQUIRED_DIRECTORIES:
        path = ROOT / relative
        if not path.is_dir():
            fail(f"Missing required directory: {relative}/", errors)

    manifest_path = ROOT / "axiom-bootstrap.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(f"Invalid bootstrap manifest: {exc}", errors)
        else:
            manifest_sha = manifest.get("canonical_source", {}).get("sha256")
            if manifest_sha != EXPECTED_MASTER_SHA256:
                fail("Bootstrap manifest contains the wrong canonical source checksum", errors)
            counts = manifest.get("counts", {})
            if counts.get("build_complete_v1_requirements") != 72:
                fail("Bootstrap manifest must declare 72 build-complete V1 requirements", errors)
            if counts.get("v1_implementation_tickets") != 160:
                fail("Bootstrap manifest must declare 160 V1 implementation tickets", errors)

    adr_files = sorted((ROOT / "docs/adr").glob("[0-9][0-9][0-9][0-9]-*.md"))
    decision_adrs = [path for path in adr_files if not path.name.startswith("0000-")]
    if len(decision_adrs) != 25:
        fail(f"Expected 25 mandatory ADR records, found {len(decision_adrs)}", errors)

    requirements = ROOT / "docs/requirements/requirements-register.md"
    if requirements.is_file():
        requirement_text = requirements.read_text(encoding="utf-8")
        ids = set(re.findall(r"\bAX-[A-Z]+-\d{3}\b", requirement_text))
        if len(ids) != 72:
            fail(f"Expected 72 unique build-complete V1 requirement IDs, found {len(ids)}", errors)
        if requirement_text.count("V1-BUILD-REQUIRED") < 72:
            fail("Every AXIOM requirement must be marked V1-BUILD-REQUIRED", errors)

    backlog = ROOT / "docs/roadmap/v1-160-tickets.md"
    if backlog.is_file():
        backlog_text = backlog.read_text(encoding="utf-8")
        ticket_ids = re.findall(r"^\| (AX-\d{3}) ", backlog_text, re.MULTILINE)
        expected_tickets = [f"AX-{number:03d}" for number in range(1, 161)]
        if ticket_ids != expected_tickets:
            fail("Complete backlog must contain AX-001 through AX-160 exactly once and in order", errors)
        referenced_ids = set(re.findall(r"\bAX-[A-Z]+-\d{3}\b", backlog_text))
        unresolved = sorted(referenced_ids.difference(ids if requirements.is_file() else set()))
        if unresolved:
            fail(f"Backlog references unknown requirements: {', '.join(unresolved)}", errors)

    directive = ROOT / "docs/source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md"
    if directive.is_file():
        directive_text = directive.read_text(encoding="utf-8").lower()
        for term in ("blockchain", "wager", "pyramid", "custom silicon", "v1-build-required"):
            if term not in directive_text:
                fail(f"Owner directive is missing mandatory V1 term: {term}", errors)

    markdown_link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for markdown_path in ROOT.rglob("*.md"):
        if markdown_path == MASTER:
            continue
        text = markdown_path.read_text(encoding="utf-8", errors="ignore")
        for raw_target in markdown_link_pattern.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (markdown_path.parent / target_path).resolve()
            if not resolved.exists():
                fail(
                    f"Broken local link in {markdown_path.relative_to(ROOT)}: {target}",
                    errors,
                )

    scan_extensions = {".md", ".txt", ".yml", ".yaml", ".json", ".toml", ".py"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in scan_extensions:
            continue
        if path == MASTER:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            fail(f"Could not scan {path.relative_to(ROOT)}: {exc}", errors)
            continue
        for pattern in PROHIBITED_SECRET_PATTERNS:
            if pattern.search(text):
                fail(f"Potential secret pattern in {path.relative_to(ROOT)}", errors)

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("AXIOM-XIII repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("AXIOM-XIII repository validation passed.")
    print(f"Master specification SHA-256: {EXPECTED_MASTER_SHA256}")
    print("Mandatory ADRs: 25")
    print("Build-complete V1 requirements: 72")
    print("Implementation tickets: 160")
    return 0


if __name__ == "__main__":
    sys.exit(main())
