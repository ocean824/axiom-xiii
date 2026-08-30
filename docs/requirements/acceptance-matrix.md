# AXIOM-XIII Build-Complete V1 Acceptance Matrix

**Authority:** Derived from sections 76–77 of the [master specification](../source/AXIOM-XIII-V1-Master-Specification.md) and expanded by the [V1 build-complete owner directive](../source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md).

## Acceptance model

Acceptance is tracked separately for **implementation**, **assurance**, and **activation**. A capability can be implementation-complete while remaining disabled in a region or production environment. Conversely, documentation or an interface-only placeholder does not satisfy implementation acceptance.

| State | Required meaning |
|---|---|
| Implemented | Executable code, schemas, APIs, events, migrations, operational controls, and user/operator paths exist |
| Integrated | Upstream/downstream domains work together using versioned contracts and representative failure cases |
| Verified | Reproducible tests and Gauntlet evidence prove the stated criteria |
| Audited | Independent review appropriate to the risk has completed and material findings are resolved |
| Production-Qualified | Security, reliability, operations, support, policy, recovery, and performance criteria for the activation profile pass |
| Disabled-by-Policy | The completed capability is not exposed in the affected operator/jurisdiction/environment; this is not a deferral state |

## Product, project, and AI development

| Domain | V1 acceptance criteria | Required evidence | Build status | Activation status |
|---|---|---|---|---|
| Shell | Seven-tab navigation is exact; controller-only and keyboard/mouse operation pass; identity, privacy, updates, repair, rollback, offline/degraded behavior, and accessibility are integrated | Navigation E2E, device/input matrix, accessibility report, update/repair/recovery capture | Not started | Pending qualification |
| Native project | `.axiom` create/open/save/migrate works; stable IDs survive edits; graph rebuilds from source; cache corruption cannot destroy canonical data; packages lock reproducibly | Round-trip/property/migration tests, corrupted-cache recovery, clean-build hashes | Not started | Developer environments |
| Simple/Advanced | Both modes mutate the same project; switching works mid-task; generated code/graphs are inspectable; manual edits remain understood; history and rollback preserve identity | Cross-mode E2E, semantic diff, rollback, branch/history evidence | Not started | Developer environments |
| AXIOM AI | Ask/Plan/Build boundaries hold; providers can be swapped; local/private modes work; agents are isolated; capability and budget limits are enforced; untrusted-content tests pass; every build emits evidence | Permission-negative tests, prompt-injection suite, model-swap tests, Gauntlet bundle, audit trace | Not started | Policy-controlled |

## Engine, high fidelity, migration, and networking

| Domain | V1 acceptance criteria | Required evidence | Build status | Activation status |
|---|---|---|---|---|
| Engine core | Complete small native game builds for Windows/Linux clients and Linux server; ECS, FABRIC, memory, reflection, serialization, Flow/AXIR, packages, patching, crash recovery, and tools meet contracts | Clean-clone builds, gameplay E2E, ABI/FFI tests, save/migration tests, crash/repair report | Not started | Production profiles |
| Rendering | NEXUS, PHOTON, WORLDSTREAM, OPTICS, materials, atmosphere/weather, water, vegetation, characters, animation integration, and VFX operate under defined profiles | Reference scenes, visual regression, frame-time/memory/loading distributions, GPU capability matrix | Not started | Hardware-profile controlled |
| Simulation/audio/UI | Physics, collision, destruction, motion/facial systems, ORPHEUS, UI, input/haptics, runtime AI, navigation, and simulation LOD integrate with save/network/replay | Determinism tests, stress scenes, audio sync, input latency, accessibility, replay comparison | Not started | Production profiles |
| Networking | Authoritative, rollback, lockstep/strategy, async, local/offline, and large-shard cell profiles are implemented and selected explicitly; replay/spectating/evidence remain consistent under faults | Profile conformance, latency/loss/partition tests, deterministic replay, large-shard simulations, failover | Not started | Per-game and scale-gated |
| Unreal Bridge | Reference corpus is inventoried and translated; legal portability and license/provenance are checked; unsupported items are visible; no silent deletion; rollback and category denominators are exact | Corpus report, migration branches, round-trip samples, unsupported-item UX, license evidence | Not started | Developer production |

## Platform, Store, Media, Social, and creator economics

| Domain | V1 acceptance criteria | Required evidence | Build status | Activation status |
|---|---|---|---|---|
| Identity/Social/Profile | Identity graph, privacy, blocks, messaging, presence, creator profile, achievements, competitive record, and wallet references work without exposing private compliance/custody data | Authorization suite, privacy/export/delete tests, abuse cases, audit logs | Not started | Region/age policy |
| Media | Capture, replay, edit, export, broadcast/livestream integration, ORPHEUS workflows, safe ingestion, provenance, and content policy are implemented | Media corpus, fuzz/scan results, transcode/playback tests, rights metadata, load/cost evidence | Not started | Provider/capacity controlled |
| Store/publishing | Submit, certify, catalog, price, purchase, entitlement, install, launch, update, repair, refund, and enforcement operate across approved rails | Publisher and buyer E2E, offline entitlement, refund/reversal, certification evidence | Not started | Rail/operator policy |
| Rights/provenance | Creator ownership, AXIOM ownership, licenses, collaborators/splits, input sources, generated content, training permissions, and Originality Firewall are enforceable | License-graph tests, blocked-publish cases, provenance export, dispute/appeal record | Not started | Production |
| Creator payables | Sales, fees, royalties, reserves, splits, refunds, chargebacks, tax status, payout eligibility, and payout history reconcile exactly | Ledger/property tests, statement examples, payout and chargeback scenarios, reconciliation | Not started | Approved provider/region |

## Chain, Wallet, tokens/credits, and marketplace settlement

| Domain | V1 acceptance criteria | Required evidence | Build status | Activation status |
|---|---|---|---|---|
| Chain node/network | Nodes start, discover peers, sync verified state, recover from backup, handle partitions/faults, upgrade/migrate, and expose telemetry | Deterministic simulation, node interoperability, partition/fault matrix, restore and upgrade drills | Not started | Testnet → pilot → production |
| Consensus/governance | Selected consensus satisfies safety/liveness assumptions; validator admission/removal, governance, upgrade, pause, and incident authority are explicit and audited | ADR, formal/invariant tests, fault simulation, key/authority review, runbooks | Not started | Audit-controlled |
| State/execution/AXVM | Transactions are deterministic, replay-protected, metered, versioned, bounded, and migratable; native modules and general contracts cannot violate invariants | Differential/property/fuzz tests, migration and invalid-transition corpus, resource exhaustion tests | Not started | Native modules; contracts policy-gated |
| Wallet/custody | Managed, self-custodial, and organization paths support trusted signing, purpose-separated keys, recovery, activity, restrictions, compromise response, and policy denial | Signing usability/security review, recovery drills, device/key matrix, authorization negatives | Not started | Custody/operator policy |
| Digital objects/licenses | Mint, transfer, burn/freeze where authorized, metadata, content references, provenance, license, creator split, royalty, and dispute status work end to end | Object lifecycle E2E, license invariants, privacy check, explorer history | Not started | Policy-controlled production |
| Marketplace settlement | Listing, offer, purchase, fee, royalty, refund, dispute, entitlement, and reconciliation align across Chain and off-chain ledgers | Concurrent purchase tests, settlement/reversal cases, indexer reconciliation, statements | Not started | Approved operator/rail |
| Token/credits | Issuance, supply, treasury, balance, hold, transferability policy, conversion, fee, burn, emergency control, and audit export are explicit | Supply invariants, journal proof, policy matrix, admin dual-control, reconciliation | Not started | Operator/jurisdiction/value limits |
| Cash-equivalent rails | Deposit, withdrawal, payout, refund, chargeback, reserve, sanctions/KYC/KYB result intake, tax record, and provider reconciliation use replaceable adapters | Mock and sandbox provider E2E, signed-webhook replay defense, outage/retry, variance resolution | Not started | Approved providers/regions |

## Arena, prizes, wagering-compatible contests, and integrity

| Domain | V1 acceptance criteria | Required evidence | Build status | Activation status |
|---|---|---|---|---|
| Competitive core | Rating pools, matchmaking, ladders, seasons, brackets, teams/rosters, match authority, spectating, replay, and record updates work deterministically | Match/tournament E2E, rating properties, bracket invariants, replay evidence | Not started | Production |
| Sponsored prize profile | Sponsor funding, rules, participant eligibility, escrow, event, result, dispute, settlement, tax/reporting, and refund/void paths work | Sponsored tournament complete, disputed and cancelled variants, reconciliation | Not started | Approved sponsor/operator/region |
| Player-funded pools | Participant entry commitments and mixed pools reserve before play, cannot double release, and settle only after final attested result | Concurrency/property tests, full event E2E, disconnect/cancel/dispute/void matrix | Not started | Approved jurisdictions/operators |
| One-to-one wagering-compatible contest | Matched terms, symmetric commitments, rule/build lock, eligibility, evidence, finality, payout, appeal, and audit are complete | Matched contest E2E, policy denials, collusion/fraud cases, settlement and reconciliation | Not started | Approved jurisdictions/operators |
| Eligibility/responsible participation | Operator, location, jurisdiction, age, identity, sanctions/risk, limits, exclusions, account state, contest class, and policy version are evaluated server-side | Decision-table coverage, geolocation/provider failure, exclusion/limit tests, immutable policy trace | Not started | Policy-controlled |
| Anti-cheat/fraud/trust | Client/server integrity, telemetry, replay, anomaly, collusion, account/device risk, evidence retention, case review, and appeal are implemented without treating AI signals as proof | Red-team scenarios, false-positive review, chain of custody, moderator/operator audit | Not started | Production profiles |

## PYRAMID, proprietary replacements, and hardware

| Domain | V1 acceptance criteria | Required evidence | Build status | Activation status |
|---|---|---|---|---|
| Virtual Target | CPU/GPU feature class, memory/storage, input/display/audio, network, security, thermal/power, package/update, and certification constraints are parameterized and enforced | Quality/Performance/Competitive reports, limit tests, reference project results | Not started | Developer production |
| PYRAMID OS | Hardened immutable Linux image boots; signed chain, read-only base, A/B update, rollback, recovery, sandboxing, controller Shell, wallet service, diagnostics, and modes work | Image provenance, boot/update/recovery drill, sandbox escape tests, mode isolation | Not started | P0/P1 production candidate |
| PLAY/DEV/NODE | Authenticated mode transitions preserve isolation; NODE is explicit opt-in with resource/power/thermal/compensation policy; secrets remain separated | Transition matrix, negative access tests, consent/limit controls, accounting and pause | Not started | Operator/user policy |
| PYRAMID Kernel | Kernel boots in selected virtual/physical target; memory, interrupts/timers, scheduler, IPC, capability model, initrd/FS, diagnostics, user process, networking/input milestones, and tests exist | Boot logs, fuzzing, unsafe-code audit, scheduler/memory tests, conformance comparison | Not started | Experimental/pilot until replacement-qualified |
| AXIOM GPU/driver | Command/memory model, shader/backend experiments, display/presentation, scheduler design, fixed-hardware prototype, conformance, capture, and telemetry integrate with RENDER | Shader correctness, crash/soak, conformance, frame comparison, thermal/power evidence | Not started | Component replacement gate |
| Transport/Crypto/Media/FS | Executable proprietary paths meet standards/API, safety, fuzz, side-channel, codec, storage, update, snapshot, repair, and provenance requirements | Conformance/differential tests, external review, recovery/soak, malformed-input corpus | Not started | Component replacement gate |
| P0/P1 hardware | Functional enclosure, cooling, acoustics, safety, serviceability, controller/accessories, secure storage, predictable profiles, repair and update work | CAD/BOM, thermal/acoustic/safety tests, manufacturing record, acceptance run | Not started | Prototype/pilot/production |
| P2/P3 program | Custom-board and custom-silicon architecture, economics, toolchain, firmware, security, I/O, power/thermal, manufacturing, certification, and prototype milestones exist | Feasibility packages, simulations, prototype/tape-out decision evidence, capital authorization | Not started | Capital-gated fabrication |

## Cross-domain security and operations

| Domain | V1 acceptance criteria | Required evidence | Build status | Activation status |
|---|---|---|---|---|
| Security | Current threat models, least privilege, secrets/signing isolation, supply-chain controls, security tests, independent reviews, disclosure, and remediation process exist | Threat register, scans, SBOM, audits, pen tests, key review, incident exercise | Not started | Required for production |
| Privacy/safety | Data inventory, purpose/retention, consent, export/delete, legal hold, child protections, moderation, abuse controls, and privileged-access audit work | Data map, privacy tests, moderation scenarios, access review, policy evidence | Not started | Region/age policy |
| Reliability/operations | SLOs, dashboards, alerts, support, moderation, economic reconciliation, backups, restore, rollback, failover, incident response, and disaster recovery are staffed and tested | Load/soak, fault injection, restore/failover, incident and reconciliation drills | Not started | Required for production |
| Accessibility/localization | Controller, keyboard, screen reader, focus, captions, reduced motion, scalable text, locale/time/currency, and plain-language economic consent meet targets | Accessibility audit, assistive-tech matrix, localization/pseudolocale tests | Not started | Production |

## Launch and activation gates

| Gate | Condition | Effect of failure |
|---|---|---|
| Architecture | Every critical domain has an owner, interface, versioning/migration, threats, tests, failure modes, and recovery | Blocks integration/qualification; does not remove build scope |
| Product/developer | New users can play and build; external developers can create, package, publish, update, and support games | Blocks public product activation |
| Security | No unresolved critical findings; key, wallet, Chain, Store, Arena, agent, OS, update, kernel/driver replacement boundaries reviewed | Blocks affected production authority/value |
| Economic | Funds, credits/tokens, assets, fees, royalties, refunds, reserves, prizes, wagers, and payouts reconcile under failure/dispute | Blocks affected real-value activation |
| Policy/legal | Operator, region, age, identity, contest class, token/value disclosure, terms, rights, privacy, and tax duties approved | Sets affected capabilities to Disabled-by-Policy |
| Operations | Monitoring, on-call, support, moderation, reconciliation, incident, backup/restore, and rollback staffed and exercised | Blocks production activation |
| Performance | Engine, networking, Chain, services, OS, and hardware budgets pass named workloads | Blocks affected profile promotion |
| Hardware/capital | Manufacturing, certification, supply, board, silicon, and expenditure decisions approved | Blocks physical fabrication or shipment; not architecture/prototype work |

## Evidence policy

A criterion is complete only when evidence is reproducible, versioned, attributable to a commit/build and requirement, and approved by the named owner. Evidence must state the environment, activation state, assurance state, workload, inputs, expected result, actual result, unresolved findings, and rollback/recovery path. Narrative claims, unversioned demos, passing averages without distributions, and unlabeled mocks do not satisfy acceptance.
