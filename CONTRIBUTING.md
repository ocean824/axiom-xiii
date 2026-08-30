# Contributing to AXIOM-XIII

AXIOM-XIII is a private proprietary project. Contributions are accepted only from authorized collaborators operating under applicable confidentiality, intellectual-property, and access agreements.

## Before starting work

Read [`CODESPRING.md`](CODESPRING.md), the [master specification](docs/source/AXIOM-XIII-V1-Master-Specification.md), the relevant requirements, open ADRs, threat models, and domain documentation. Confirm that the task has a named human owner and does not depend on an unresolved ADR.

| Required field | Description |
|---|---|
| Requirement ID | Parent and child requirements implemented or affected |
| Backlog or issue ID | Approved unit of work |
| Owner | Human accountable for the domain |
| Maturity class | Production, Preview, Experimental, or Architected |
| Scope | Explicit included and excluded behavior |
| Dependencies | Upstream decisions, schemas, packages, services, and data |
| Acceptance criteria | Observable pass/fail conditions |
| Threat impact | Trust zones, permissions, secrets, abuse cases, and mitigations |
| Provenance impact | Source, licenses, generated content, assets, and SBOM changes |
| Evidence plan | Tests, benchmarks, scans, captures, and reproducibility |
| Rollback | Reversal and migration procedure |

## Branching

Use short-lived branches created from the appropriate protected integration branch. The intended long-lived branches are `main`, `staging`, and `develop`. Do not push directly to protected branches. AI-generated changes must remain isolated until reviewed and verified.

## Pull requests

A pull request must be narrowly scoped, readable, tested, documented, and assigned to a human owner. It must link requirements and decisions, identify risks and unknowns, and include or point to a Gauntlet evidence package. Do not hide failed checks or reduce policy to make a change pass.

| Change | Additional requirement |
|---|---|
| Public API, schema, format, or storage change | Approved ADR/RFC and migration guidance |
| Dependency change | Security, license, API, performance, and rollback analysis |
| Native or unsafe code | Boundary review, focused tests, sanitizers or equivalent evidence |
| Parser or decoder | Bounds checks and fuzzing plan |
| Wallet, Chain, Store, Arena, payments, or custody | Restricted review and staged-value controls |
| Signing, firmware, secure boot, anti-cheat, or production infrastructure | Security owner approval and isolated access |
| AI-generated code or content | Generation disclosure, source review, provenance, and human ownership |

## Coding principles

Code must use explicit ownership and lifetime, bounded resource consumption, handled errors, deterministic tests, documented public APIs, reviewed unsafe boundaries, justified dependencies, owned and expiring feature flags, explicit migrations, classified telemetry, accessibility consideration, and recorded license/provenance.

Services communicate through APIs or events. Shared database tables must not become invisible cross-domain coupling. Replaceable third-party implementation types must not become permanent public AXIOM APIs.

## Definition of accepted work

Work is accepted only when the required tests and scans pass, documentation and provenance are current, rollback is understood, unresolved risks are visible, and the named human owner approves the evidence. Compilation alone is not acceptance.
