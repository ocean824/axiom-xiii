# AXIOM-XIII V1 Risk Register

**Status:** Derived from section 75 of the [master specification](../source/AXIOM-XIII-V1-Master-Specification.md). Probability and impact are initial qualitative assessments for planning and require owner review.

| ID | Risk | Probability | Impact | Primary mitigation | Trigger | Contingency | Owner |
|---|---|---:|---:|---|---|---|---|
| R-001 | Scope collapse across engine, AI, services, Chain, Arena, OS, hardware, and games | High | Critical | Enforce maturity classes, phase gates, one complete sample game, and non-blocking research | Multiple phases begin without prior exit evidence; critical-path ownership falls below plan | Freeze expansion, stop low-priority streams, restore one vertical-slice milestone | Unassigned |
| R-002 | AI-generated technical debt and inconsistent architecture | High | High | Requirement-first tasks, typed APIs, isolated branches, human code owners, complexity budgets, Gauntlet | Duplicate abstractions, rising defect/revert rate, unreadable changes, bypassed tests | Pause autonomous implementation; architecture refactor and stricter capability limits | Unassigned |
| R-003 | AAA renderer ambition consumes the program before the engine ships | High | High | Complete small-game path first; measured renderer increments; reference scenes and budgets | Renderer headcount or schedule dominates while end-to-end game path remains incomplete | Cap research, ship scalable baseline, defer advanced paths to Preview/Experimental | Unassigned |
| R-004 | Blockchain exploit, key compromise, consensus failure, or fraud causes irreversible loss | Medium | Critical | Narrow modules, curated validator launch, value limits, audits, HSM/multisig, bug bounty, no bridge dependency | Critical invariant failure, key anomaly, unresolved high-severity audit finding | Halt value movement, activate emergency controls, rotate/recover keys, reconcile from evidence | Unassigned |
| R-005 | Prize systems create legal, regulatory, or fraud exposure | High | Critical | Policy/operator layer, sponsor-funded first profile, geolocation/identity where required, evidence, disputes, counsel | Unsupported region, manipulation, inconsistent classification, unreconciled prize | Disable affected profile/region, preserve evidence, refund or hold under approved process | Unassigned |
| R-006 | Proprietary source leaks or enables unauthorized engine cloning | Medium | Critical | Private access, segmentation, source-available terms, contractor isolation, provenance, watermarking where appropriate | Unauthorized clone, unusual access, leaked archive, agent context crossover | Revoke access, rotate secrets, preserve logs, legal/security response, segment further | Unassigned |
| R-007 | Creators reject the platform due to lock-in, opaque fees, rights grabs, or wallet confusion | Medium | High | Creator ownership promise, exportable projects, ordinary non-chain path, transparent agreements and economics | Negative external validation, project export failure, agreement objections, support volume | Simplify terms, improve portability, decouple optional economics, revise policy before launch | Unassigned |
| R-008 | Unreal migration expectations exceed achievable compatibility | High | High | Category-specific reports, license scan, explicit unsupported items, isolated branches, measured corpus | Users interpret one score as complete compatibility; silent loss or severe regressions | Restrict supported versions/categories, increase manual workflow, publish limitations | Unassigned |
| R-009 | Kernel, GPU, filesystem, crypto, or transport research diverts critical-path resources | High | High | Resource caps, independent owners, reference implementations, conformance and pause gates | Experimental staffing grows while production milestones slip; no benchmark improvement | Pause or archive stream, retain interfaces, continue with proven dependency path | Unassigned |
| R-010 | Social, media, packages, assets, and marketplace produce abuse, malware, fraud, or stolen content | High | High | Sandboxing, provenance, reporting, seller verification, moderation, malware scanning, appeals | Malware detection, rights complaints, coordinated abuse, moderation backlog | Disable distribution/accounts under policy, quarantine content, notify affected users, review controls | Unassigned |
| R-011 | Hardware capital, manufacturing, certification, warranty, or supply-chain failure | Medium | Critical | Software/protocol first, commodity P0/P1, controlled pilots, modular sourcing, demand evidence | Component shortage, thermal failure, certification delay, inventory exposure | Delay physical launch, continue desktop/Virtual Target path, redesign around alternates | Unassigned |
| R-012 | External model, cloud, payment, or platform provider captures a critical dependency | High | High | Model router, multi-cloud interfaces, self-host options, payment abstraction, portable data, contracts | Price/term change, outage, access loss, unsupported geography, degraded quality | Switch provider, invoke local/offline path, reduce dependent feature, migrate data |

## Additional cross-cutting risks

The deep analysis identified risks that cut across the twelve source risks and should be tracked as child risks rather than replacing the canonical list.

| ID | Cross-cutting risk | Relationship | Required control |
|---|---|---|---|
| R-X01 | Prompt injection in project files, assets, packages, web content, or issue text | Amplifies R-002, R-004, R-006, R-010 | Treat content as data; capability broker; denied-action tests; no instruction inheritance |
| R-X02 | Cross-domain cascading failure | Amplifies platform and economic risk | API/event boundaries, offline policy, circuit breakers, chaos and recovery tests |
| R-X03 | Sensitive data enters immutable or broadly replicated systems | Amplifies legal/privacy risk | Data minimization, classification, off-chain storage, explicit schema review |
| R-X04 | Production signing compromise | Amplifies every distribution and device risk | Isolated signing, dual control, key rotation/revocation, no ordinary CI access |
| R-X05 | Unmeasured performance claims damage credibility | Amplifies renderer, networking, Chain, and hardware risk | Defined workload, reference hardware, reproducible benchmark methods, distributions not averages |
| R-X06 | Feature flags become permanent undocumented forks | Amplifies operations and support risk | Owner, expiry, review date, test coverage, removal plan |

## Review cadence

The risk register should be reviewed at each phase gate, after any major incident, before enabling real value, before expanding a public beta, and whenever an accepted ADR materially changes system boundaries. A risk cannot be closed merely because implementation started; closure requires evidence that probability or impact is acceptably reduced and that residual risk is owned.
