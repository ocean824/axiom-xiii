## Requirement and decision links

State the parent requirement IDs, backlog or issue IDs, and ADR/RFC links.

## Intent and scope

Describe the observable outcome, included behavior, and explicit exclusions.

## V1 status dimensions

State the **build status** (Accepted, In Progress, Implemented, or Verified), **assurance state** (Prototype, Integrated, Verified, Audited, or Production-Qualified), **activation state** (Local, Sandbox, Testnet, Pilot, Region-Limited, Production-Enabled, or Disabled-by-Policy), **economic effect** (No Value, Simulated, Test Value, or Real Value), and any **replacement state** for proprietary kernel/driver/crypto/transport/media/filesystem work. No activation or replacement gate may be used to defer mandatory V1 construction.

## Architecture and dependencies

Describe affected domains, API/schema changes, third-party dependencies, and migration implications.

## Security, privacy, and abuse analysis

Identify trust zones, permissions, secrets, sensitive data, attacker opportunities, and mitigations. Explain why repository or project content cannot expand agent authority.

## Provenance and licensing

Record new code, assets, datasets, model outputs, dependencies, licenses, hashes, required notices, and AI-generation disclosure.

## Verification

| Check | Result | Evidence path |
|---|---|---|
| Formatting and linting | Pending | Pending |
| Unit/property tests | Pending | Pending |
| Integration/gameplay/network tests | As applicable | Pending |
| Fuzz/security tests | As applicable | Pending |
| Performance/visual tests | As applicable | Pending |
| Clean build/reproducibility | Pending | Pending |
| SBOM/dependency/license review | Pending | Pending |
| Gauntlet evidence bundle | Pending | Pending |

## Rollback and recovery

Explain how to reverse the change safely, including data or schema migrations and artifact revocation where relevant.

## Uncertainty and known limitations

List failed checks, unsupported cases, assumptions, follow-up work, and decisions requiring human approval.

## Human ownership

- **Code owner:** Unassigned
- **Security reviewer:** As required
- **Legal/licensing reviewer:** As required
- **Final approver:** Unassigned

- [ ] I did not commit secrets or production credentials.
- [ ] I did not bypass or weaken required verification.
- [ ] I did not make an unresolved ADR decision implicitly.
- [ ] I preserved the canonical master specification.
- [ ] I advanced mandatory V1 implementation even where activation or production replacement remains gated.
- [ ] I did not promote an unaudited experimental implementation into a production dependency.
