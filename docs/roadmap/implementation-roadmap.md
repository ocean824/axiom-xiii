# AXIOM-XIII V1 Implementation Roadmap

**Status:** Derived execution plan. The [master specification](../source/AXIOM-XIII-V1-Master-Specification.md) remains authoritative.

## Roadmap policy

This roadmap is milestone-driven rather than date-driven. A phase starts only when its blocking decisions, owners, dependencies, budgets, and threat controls are in place. A phase completes only when its exit gate is reproducibly demonstrated and the evidence is committed.

| Rule | Enforcement |
|---|---|
| No phase-by-calendar fiction | Report achieved gates, not optimistic completion percentages |
| No hidden scope transfer | Deferred work retains a requirement, owner, rationale, and re-entry condition |
| No all-at-once execution | The critical path takes priority over breadth |
| No experimental promotion by assertion | Conformance, security, compatibility, operational, and performance gates are mandatory |
| No agent-only ownership | Critical systems require named human code owners and approvers |
| No irreversible action without authorization | Production deployment, custody, token issuance, prize activation, and public release require explicit approval |

## Phase sequence

| Phase | Outcome | Principal deliverables | Exit gate |
|---:|---|---|---|
| 0 | Canonical foundation | Ownership, repository, standards, ADR/RFC process, requirements/risk registers, CI, Connect schemas, `.axiom` v0, threat model, budget controls, reference hardware | Clean repository; reproducible hello-world; signed development artifacts; baseline tests; no unresolved ownership of foundational code |
| 1 | Shell and native runtime skeleton | Controller-first Shell, seven tabs, local identity sandbox, `.axiom` create/open/save, project graph, native window/input/UI, ECS/Core/FABRIC skeleton, basic renderer, asset import, build/package/launch | Sample project can be created, edited, built, installed in GAMES, and launched |
| 2 | AI development loop | Ask/Plan/Build, Intent Compiler, project context graph, planner DAG, model router, capability broker, isolated agents, Gauntlet v0, history/rollback, Simple/Advanced continuity, provenance | Nontechnical tester can request and approve a mechanic, build it, inspect/edit it in Advanced, and return to Simple without conversion |
| 3 | Complete small-game path | Scene/entity authoring, Flow/AXIR, physics, animation, ORPHEUS, UI/input, saves, networking, packages, profiler, Windows/Linux, server, 2D/2.5D, sample game | External developers can complete and ship a small commercial-quality game through the documented path |
| 4 | High-fidelity world path | NEXUS, WORLDSTREAM, PHOTON, OPTICS, materials, environment, characters, motion foundation, profilers, reference scenes, visual tests | Representative high-fidelity scene meets frame, memory, loading, and quality targets on reference hardware |
| 5 | Unreal Bridge | Project inventory, license scan, asset/material/world conversion, C++ analysis, Blueprint subset, plugin report, migration Gauntlet, intervention UX | Reference projects convert with measured category-specific compatibility and no silent data loss |
| 6 | Platform services | Identity, social, media, cloud projects, Store sandbox, entitlements, payment sandbox, telemetry, moderation, support, developer portal | Developer can submit, certify, purchase, install, launch, update, and refund with sandbox funds |
| 7 | Chain and Wallet | Node, consensus testnet, wallet core, digital objects, provenance/licenses, marketplace, splits, explorer/indexer, custody modes, audits | Mint, license, purchase, transfer, royalty, and recovery scenarios pass audit gates on a candidate network |
| 8 | Arena and prizes | Matchmaking, ratings, tournaments, attestation, replay evidence, anti-cheat, policy, sponsored escrow, teams, disputes, UI integration | Sponsored tournament can be created, played, verified, disputed, settled, and audited |
| 9 | PYRAMID prototype | Virtual Target, controller certification, Linux image, A/B recovery, DEV mode, enclosure, thermal/acoustic tests, experimental kernel/GPU/transport/FS milestones | Reference hardware boots into AXIOM, plays native titles, builds a sample, and passes update/recovery and thermal tests |
| 10 | Public beta and V1 production | Security audits, external cohort, catalog operations, support, moderation, controlled economics, Arena events, incident response, legal profiles | All applicable V1-PRODUCTION requirements and launch gates pass |

## Immediate CodeSpring work package

CodeSpring should begin with a bounded Phase 0 package. The implementation sequence below is designed to surface decisions before they become expensive code dependencies.

| Order | Work item | Dependencies | Completion evidence |
|---:|---|---|---|
| 1 | Validate repository integrity and canonical-source handling | None | Source checksum passes; no mutation of master file |
| 2 | Create issue, requirement, ADR, RFC, threat, and evidence schemas | Repository conventions | Schema validation in CI |
| 3 | Draft blocking ADRs for ownership, toolchain, `.axiom`, UI, ECS, renderer, physics, networking, cloud, and license | Options research and named reviewers | ADRs in Proposed state with alternatives and consequences |
| 4 | Define stable AXIOM ID and schema version conventions | ADR proposals | Fixtures and compatibility tests |
| 5 | Draft `.axiom` manifest v0 and minimal sample project | ID/schema conventions | Round-trip parser test and human-readable fixture |
| 6 | Draft AXIOM Connect capability schema v0 | Threat model and trust zones | Positive and negative permission fixtures |
| 7 | Select or isolate a provisional build bootstrap behind an ADR | Toolchain ADR | Clean configure/build/test commands |
| 8 | Implement minimal native hello-world runtime | Build bootstrap and project schema | Clean build launches deterministic sample |
| 9 | Add CI validation and development artifact signing | Build and repository policy | Reproducible CI run, SBOM, secret scan, attestations |
| 10 | Produce first Gauntlet evidence bundle | Tests and evidence schema | Human-readable report plus machine-readable metadata |

The first engagement should stop after this package and obtain approval before expanding into Phase 1 product implementation.

## Initial backlog map

The eighty source backlog items are preserved by workstream below. Item numbers match section 79 of the master specification.

| Workstream | Items | Near-term priority | Dependency posture |
|---|---:|---|---|
| Foundation | 1–8 | Immediate | Blocks all implementation |
| Shell | 9–17 | Next | Depends on UI bootstrap, identity sandbox, project/install manifests |
| Engine | 18–29 | Next | Depends on language/toolchain, ECS, schema, platform abstractions |
| DEV and AI | 30–43 | After typed engine operations exist | Depends on project graph, Connect, source control, tests |
| Unreal Bridge | 44–49 | After `.axiom` and engine import contracts stabilize | Must not become runtime dependency |
| Platform | 50–57 | Sandbox after local vertical slice | Requires service boundaries, policy, privacy, observability |
| Chain and Arena | 58–67 | Simulation and sandbox only until audits | Requires protocol, identity, evidence, legal/security gates |
| Renderer/AAA | 68–73 | Prototype after complete small-game path | Must be budgeted and measured |
| PYRAMID | 74–80 | Virtual Target first; experimental work capped | Must not block desktop V1 |

## Parallel non-blocking workstreams

Experimental programs may begin early to reduce long-term uncertainty, but each requires an owner, threat/performance model, reference implementation, conformance tests, benchmark baseline, replacement gate, and pause criterion.

| Workstream | Permitted early outcome | Prohibited early assumption |
|---|---|---|
| PYRAMID Kernel | Boot, memory, scheduler, IPC experiments | Production OS dependency |
| AXIOM GPU | Conformance and performance research harness | Replacing vendor drivers without compatibility evidence |
| Secure Transport | Standards-conformance prototype | Custom unreviewed transport securing value |
| AXIOM Crypto | API wrappers and test vectors around established primitives | New cryptographic primitive for branding |
| Image/Media | Fuzzed parsers, compression and streaming experiments | Unbounded parsing of untrusted media |
| AXIOM FS | Content-addressing, snapshots, integrity experiments | Replacing host filesystem before recovery/soak tests |
| AXVM | Deterministic sandbox research | Unrestricted production smart contracts |
| Large-shard research | Cell simulation and measured workloads | Public concurrency claims without reproducible benchmarks |
| Distributed PYRAMID compute | Opt-in, resource-capped experiments | Background work harming gameplay or hiding economics |
| Internal model training | Evaluation and provenance pipeline | Training on unlicensed or undisclosed content |

## Exit evidence standard

Every exit gate should have a versioned evidence directory. Evidence is a product artifact, not an ephemeral CI log.

| Evidence category | Minimum content |
|---|---|
| Traceability | Requirements, ADRs, owners, commits, builds, and test-plan identifiers |
| Reproducibility | Clean-environment setup, exact commands, toolchain and dependency locks |
| Correctness | Unit, property, integration, migration, gameplay, network, and state-invariant results as applicable |
| Security | Threat-model delta, static/security scans, permission negatives, fuzzing, secret scan |
| Performance | Reference hardware/workload, frame-time distributions, memory, loading, network or chain measures |
| Provenance | SBOM, dependency licenses, asset/model origins, hashes, generated-content disclosure |
| Operations | Deployment or local-run procedure, monitoring, rollback, recovery, incident implications |
| Human approval | Named owner and reviewer decisions with unresolved risks stated explicitly |

## Launch gates

| Gate | Required proof |
|---|---|
| Architecture | Every critical domain has an owner, interface, threat model, tests, and migration policy |
| Product | New users can play and build without core-team intervention |
| Developer | External developers can complete, package, publish, update, and support a game |
| Security | No unresolved critical findings; key, wallet, chain, Store, and agent boundaries reviewed |
| Economic | Funds, assets, royalties, refunds, prize settlements, and records reconcile under failure and dispute |
| Operations | Monitoring, support, moderation, incident response, backups, and rollback are staffed and tested |
| Legal/Policy | Terms, licenses, Store and Arena rules, token disclosures, privacy, and operator policies are approved |
| Performance | Reference projects meet frame, memory, loading, network, chain, service, and editor targets |
| Hardware readiness | Required only for a physical PYRAMID launch, not the desktop V1 release |

## Scheduling principle

Dates should be added only after Phase 0 resolves the principal ADRs and baseline prototypes provide throughput and complexity evidence. Until then, the correct planning unit is a dependency-ordered milestone with an exit gate, not a calendar promise.
