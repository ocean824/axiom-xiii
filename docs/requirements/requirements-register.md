# AXIOM-XIII Build-Complete V1 Requirements Register

**Status:** Governing derived register. The first forty-eight requirements originate in section 78 of the preserved [master specification](../source/AXIOM-XIII-V1-Master-Specification.md). Requirements 49–72 operationalize the later [Owner Directive: V1 Is Build-Complete](../source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md). All seventy-two requirements are accepted V1 construction obligations; assignment and evidence remain pending until implementation begins.

## Requirement-state model

A single maturity label cannot represent both implementation and exposure. This register preserves the historical source class while adding independent build, assurance, and activation fields.

| Field | Meaning |
|---|---|
| **Source class** | Historical class copied from the master specification or `DIRECTIVE-ADDED` for a requirement made explicit by the owner directive |
| **Build obligation** | Always `V1-BUILD-REQUIRED` unless a later owner directive explicitly removes the requirement |
| **Assurance target** | Minimum evidence state expected during V1: Integrated, Verified, Audited, or Production-Qualified |
| **Activation** | Broadest activation that may be pursued after gates pass; this never changes the build obligation |
| **Delivery status** | Accepted, In Progress, Implemented, Verified, Superseded, or Removed-by-Owner-Directive |

“Deferred” is intentionally absent. A requirement can be blocked for a decision, provider, audit, manufacturing, capital, or production activation while implementation and safe verification continue.

## A. Product, development, AI, formats, engine, and rendering

| # | ID | Requirement | Source class | Build obligation | Assurance target | Activation | Status |
|---:|---|---|---|---|---|---|---|
| 1 | AX-PROD-001 | AXIOM shall ship as a controller-first desktop console environment. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 2 | AX-PROD-002 | Top navigation shall be GAMES, MEDIA, SOCIAL, DEV, STORE, PROFILE, WALLET. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 3 | AX-PROD-003 | There shall be no separate CREATE tab in V1. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 4 | AX-DEV-001 | DEV shall provide Simple and Advanced modes over one semantic project. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 5 | AX-DEV-002 | Users shall switch modes mid-project without conversion, duplication, or loss. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 6 | AX-AI-001 | Simple mode shall be chat-first with AXIOM AI while preserving inspectable project state. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 7 | AX-AI-002 | AXIOM AI shall expose Ask, Plan, and Build states with explicit consequence boundaries. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 8 | AX-AI-003 | AXIOM AI shall use requirement-first planning, isolated parallel agents, and Gauntlet loops. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 9 | AX-AI-004 | External agents may bootstrap implementation but shall not become shipping runtime dependencies. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 10 | AX-AI-005 | Models and providers shall be replaceable through owned interfaces. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 11 | AX-AI-006 | Agent actions shall be permissioned, audited, reversible where possible, and branch-scoped. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 12 | AX-FMT-001 | AXIOM shall create and save native `.axiom` projects. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 13 | AX-FMT-002 | Canonical project data shall be inspectable, versioned, migratable, and Git-friendly. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 14 | AX-FMT-003 | AXIOM shall maintain a semantic project graph rebuildable from source. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 15 | AX-BRG-001 | AXIOM shall analyze and import legally portable Unreal projects, code, and assets. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 16 | AX-BRG-002 | Unreal conversion shall produce category-specific compatibility, fidelity, provenance, and license reports. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 17 | AX-ENG-001 | AXIOM shall run native 3D and 2D/2.5D projects. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 18 | AX-ENG-002 | AXIOM shall support Windows and Linux client builds and Linux dedicated servers. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 19 | AX-ENG-003 | Engine APIs shall not permanently expose replaceable third-party implementation types. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 20 | AX-REN-001 | Renderer architecture shall target contemporary AAA world scale and visual fidelity. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production profiles | Accepted |
| 21 | AX-REN-002 | NEXUS clustered virtual geometry shall ship as a V1 engine capability. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production profiles | Accepted |
| 22 | AX-REN-003 | PHOTON dynamic lighting, reflection, and path-tracing profiles shall ship. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Capability-gated production | Accepted |
| 23 | AX-REN-004 | WORLDSTREAM shall support large hierarchical streamed worlds. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production profiles | Accepted |
| 24 | AX-REN-005 | OPTICS shall provide physical and stylized camera controls. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 25 | AX-AUD-001 | ORPHEUS shall provide spatial, adaptive audio and music graphs. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |

## B. Networking, Chain, Wallet, Arena, Store, licensing, security, PYRAMID, provenance, and quality

| # | ID | Requirement | Source class | Build obligation | Assurance target | Activation | Status |
|---:|---|---|---|---|---|---|---|
| 26 | AX-NET-001 | AXIOM shall implement authoritative, rollback, strategy/lockstep, asynchronous, offline/local, and profile-selection networking. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Per-game production profile | Accepted |
| 27 | AX-NET-002 | AXIOM shall implement and integrate the large-shard cell architecture for 10,000-plus logical-participant scenarios, with measured V1 simulations and bounded production profiles. | V1-ARCHITECTED | V1-BUILD-REQUIRED | Verified | Pilot/region-limited until scale gates pass | Accepted |
| 28 | AX-CHN-001 | AXIOM shall implement its own game-native blockchain node and state model. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Testnet then production | Accepted |
| 29 | AX-CHN-002 | AXIOM Chain shall support digital objects/NFTs, licenses, provenance, royalties, marketplace settlement, and prize escrow. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Policy-controlled production | Accepted |
| 30 | AX-CHN-003 | General AXVM contracts shall be implemented and integrated in V1; unrestricted production deployment remains assurance- and policy-gated until audited. | V1-PREVIEW | V1-BUILD-REQUIRED | Audited | Restricted then production | Accepted |
| 31 | AX-WAL-001 | Wallet shall support managed, self-custodial, and organization-controlled paths with trusted signing. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Policy-controlled production | Accepted |
| 32 | AX-ARN-001 | Arena shall support skill matchmaking, ranked play, tournaments, replays, evidence, and prize pools. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 33 | AX-ARN-002 | Sponsored prize pools shall be a fully implemented V1 real-value competition profile. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Approved jurisdictions/operators | Accepted |
| 34 | AX-ARN-003 | Player-funded and token/credit competition, including one-to-one and tournament stake commitments, shall be fully implemented in V1; activation is jurisdiction-, identity-, age-, limit-, and policy-controlled. | V1-PREVIEW | V1-BUILD-REQUIRED | Audited | Approved jurisdictions/operators | Accepted |
| 35 | AX-STO-001 | AXIOM shall control official Store policy, certification, payments, discovery, entitlements, installation, updates, refunds, and enforcement. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 36 | AX-LIC-001 | Creators shall own original game IP while AXIOM retains AXIOM technology ownership. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 37 | AX-LIC-002 | Core engine shall use a proprietary/source-available licensing strategy, not permissive open source by default. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 38 | AX-SEC-001 | Secrets shall never be exposed to unscoped agents, projects, prompts, logs, or ordinary CI. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 39 | AX-SEC-002 | Production packages, builds, updates, chain modules, and privileged policy artifacts shall be signed and provenance-verifiable. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 40 | AX-PYR-001 | V1 shall include an executable PYRAMID Virtual Target and compatibility-reporting simulator. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Developer production | Accepted |
| 41 | AX-PYR-002 | Production PYRAMID OS shall implement a hardened immutable Linux-based path with signed boot, A/B update, recovery, sandboxing, and secure services. | V1-ARCHITECTED | V1-BUILD-REQUIRED | Audited | Reference hardware production | Accepted |
| 42 | AX-PYR-003 | PYRAMID Kernel shall be implemented, booted, integrated behind a conformance boundary, and tested during V1; production replacement requires independent evidence. | V1-EXPERIMENTAL | V1-BUILD-REQUIRED | Verified | Experimental/pilot until audited | Accepted |
| 43 | AX-PYR-004 | AXIOM GPU, Secure Transport, Crypto API, Image/Media, codecs, and AXIOM FS replacement programs shall produce executable V1 implementations and conformance evidence. | V1-EXPERIMENTAL | V1-BUILD-REQUIRED | Verified | Component-specific gated replacement | Accepted |
| 44 | AX-PYR-005 | Physical PYRAMID shall implement PLAY, DEV, and opt-in NODE modes with secure isolation and resource policy. | V1-ARCHITECTED | V1-BUILD-REQUIRED | Audited | Hardware profile production | Accepted |
| 45 | AX-IP-001 | Every asset, package, model output, and imported source shall retain provenance and license metadata. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 46 | AX-IP-002 | Mechanics Registry and Originality Firewall shall be required for first-party games and official publishing review. | V1-PRODUCTION | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 47 | AX-QA-001 | Every accepted Build shall produce a machine- and human-readable Gauntlet evidence package. | V1-PRODUCTION | V1-BUILD-REQUIRED | Production-Qualified | Production | Accepted |
| 48 | AX-QA-002 | Critical platform systems shall undergo independent security review before real value, privileged identity, or irreversible authority is exposed. | V1-PRODUCTION | V1-BUILD-REQUIRED | Audited | Production activation gate | Accepted |

## C. Owner-directive requirements added to make the full V1 destination explicit

| # | ID | Requirement | Source class | Build obligation | Assurance target | Activation | Status |
|---:|---|---|---|---|---|---|---|
| 49 | AX-NET-003 | Network profile selection, versioning, compatibility, fallback, and migration shall be explicit in project/build metadata. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 50 | AX-CHN-004 | V1 shall include a production-candidate network, testnet, deterministic consensus simulator, validator operations, upgrade, backup, and disaster recovery. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Testnet/pilot/production | Accepted |
| 51 | AX-CHN-005 | Chain state and execution shall be deterministic, versioned, resource-metered, replay-protected, migratable, and protected by explicit invariants. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 52 | AX-CHN-006 | Native modules shall implement identity references, objects, mint/burn/transfer, licenses, splits, marketplace settlement, escrow, result attestations, and governance. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Policy-controlled production | Accepted |
| 53 | AX-CHN-007 | Indexer and explorer shall expose privacy-aware transaction, object, license, provenance, escrow, settlement, validator, and governance history. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Verified | Production | Accepted |
| 54 | AX-CHN-008 | Chain and wallet recovery shall include node restore, state verification, key recovery boundaries, incident pause, upgrade rollback, and operator drills. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 55 | AX-CHN-009 | Sensitive identity, KYC, private gameplay, and large media shall remain off-chain; only minimized hashes, commitments, and policy-safe references may be immutable. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 56 | AX-WAL-002 | Wallet keys shall be purpose-separated, hardware-backed where appropriate, recoverable according to custody mode, and unavailable to untrusted game UI. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 57 | AX-WAL-003 | Trusted signing UI shall display the human-readable action, value, fee, permissions, counterparty, policy result, and irreversible consequence before authorization. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 58 | AX-WAL-004 | Wallet history shall reconcile on-chain state, internal ledgers, provider events, holds, pending operations, failures, reversals, and support cases. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 59 | AX-ECO-001 | Fiat/payment, internal credit/token, on-chain asset, entitlement, and creator-payable ledgers shall remain technically and accounting-separated. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 60 | AX-ECO-002 | Economic journals shall be immutable, balanced, idempotent, concurrency-safe, minor/atomic-unit precise, and fully reversible only through compensating entries. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 61 | AX-ECO-003 | V1 shall implement provider-neutral deposit, withdrawal, conversion, refund, chargeback, payout, reserve, tax-record, and reconciliation adapters, including deterministic mocks. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Approved provider/region | Accepted |
| 62 | AX-ECO-004 | Prize and wager funds shall be reserved before play, bounded by policy, protected from double release, and settled only against final attested results. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Approved provider/region | Accepted |
| 63 | AX-ECO-005 | Fees, royalties, processor costs, network costs, taxes, reserves, and participant winnings shall be separate, versioned, disclosed ledger concepts. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 64 | AX-ECO-006 | Economic operations shall support holds, limits, exclusions, fraud review, disputes, reversals, negative-balance/reserve policy, and exact reconciliation. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 65 | AX-ECO-007 | Token/credit issuance, supply, conversion, transferability, burn, treasury, and emergency controls shall be policy-driven, attributable, and audit-exportable. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Policy-controlled production | Accepted |
| 66 | AX-ARN-004 | Paid and player-funded contest eligibility shall evaluate operator, jurisdiction, location, age, identity, sanctions/risk, limits, exclusions, contest class, and policy version. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Approved jurisdictions/operators | Accepted |
| 67 | AX-ARN-005 | Arena shall retain immutable ruleset/build references, authoritative match evidence, replay hashes, anti-cheat results, result attestations, dispute records, and settlement linkage. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Production | Accepted |
| 68 | AX-ARN-006 | One-to-one stakes, tournament entries, sponsored pools, participant-funded pools, mixed pools, cancellations, voids, refunds, disputes, and appeals shall pass end-to-end V1 tests. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Approved jurisdictions/operators | Accepted |
| 69 | AX-PYR-006 | V1 shall deliver P0 and P1 physical reference prototypes plus requirements, interfaces, simulation, manufacturing, and certification evidence for P2 and P3. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Verified | Prototype/pilot | Accepted |
| 70 | AX-PYR-007 | P2 custom-board and P3 custom-silicon programs shall have owned V1 architecture, feasibility, toolchain, firmware, security, thermal/power, cost, and prototype milestones. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Integrated | Capital-gated fabrication | Accepted |
| 71 | AX-PYR-008 | NODE mode shall implement explicit opt-in, isolation, verifiable work, compensation accounting, limits, anti-fraud, power/thermal policy, pause, and user-visible earnings/costs. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Audited | Policy-controlled pilot/production | Accepted |
| 72 | AX-OPS-001 | Every capability shall publish independent build, assurance, and activation status; no gate may silently convert an accepted V1 requirement into deferred work. | DIRECTIVE-ADDED | V1-BUILD-REQUIRED | Verified | All environments | Accepted |

## Traceability and non-regression rules

Every epic, issue, pull request, migration, API or format change, test plan, release artifact, and Gauntlet package must reference at least one requirement ID. Child requirements may add specificity but may not weaken a parent without a later owner directive or an approved change that has equivalent authority.

A production activation may be denied even after implementation is complete. The denial must identify the affected environment, operator, jurisdiction, user class, value limit, assurance finding, or missing approval. It must not delete implementation status, tests, ownership, or backlog work.

For every requirement, evidence must ultimately include the relevant source/decision links, implementation commit, test results, security and provenance results, operational signals, migration/rollback instructions, and named review.
