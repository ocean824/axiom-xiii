# Canonical Source Preservation

[`AXIOM-XIII-V1-Master-Specification.md`](AXIOM-XIII-V1-Master-Specification.md) is a byte-for-byte copy of the supplied `Pasted_content.txt`. It is retained as the primary source of truth so that no generated summary, repository scaffold, or implementation plan can erase wording, requirements, maturity classifications, or unresolved decisions.

| File | Purpose |
|---|---|
| `AXIOM-XIII-V1-Master-Specification.md` | Verbatim canonical source |
| `SHA256SUMS` | Current repository copy digest |
| `ORIGINAL-SOURCE-CHECKSUM.txt` | Original uploaded filename and digest |

The expected SHA-256 digest is:

```text
dc7feae7b999e8c4802ef8fb67fa894c68e75e8cf1f601132ccb162f6565909d
```

Do not edit the canonical file in place. A proposed source change should first be recorded through an ADR or RFC, reviewed by the appropriate owners, and applied as a deliberate new source version with an updated checksum and changelog. Derived documents must identify themselves as derived and must not silently contradict this file.

Repository validation runs the following local command:

```bash
python3 tools/validate_repository.py
```

A checksum failure is a blocking error because it indicates that the preserved source no longer matches the supplied document.
