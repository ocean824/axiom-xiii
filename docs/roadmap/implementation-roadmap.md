# AXIOM-XIII Build-Complete V1 Implementation Roadmap

**Authority:** This roadmap derives from the [verbatim master specification](../source/AXIOM-XIII-V1-Master-Specification.md) and is governed by the [V1 build-complete owner directive](../source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md).

## Roadmap doctrine

AXIOM-XIII V1 is one dependency-ordered program whose destination includes every system described in the source. Sequencing controls **when work integrates**, not whether it belongs to V1. Blockchain, Wallet, player-funded prize and wager flows, cash-equivalent adapters, large-shard networking, native streaming/media paths, PYRAMID OS and hardware, proprietary kernel/GPU/transport/crypto/media/filesystem replacements, and P2/P3 hardware programs remain inside the V1 program.

| Rule | Enforcement |
|---|---|
| No hidden deferral | Every described capability has a V1 requirement, owner role, repository path, work package, tests, and evidence target |
| No all-at-once merge | Work is split into dependency-valid trains and bounded pull requests |
| No gate-as-excuse | Legal, security, provider, audit, performance, hardware, and capital gates control activation or replacement, not construction |
| No maturity fiction | Build, assurance, and activation status are reported independently |
| No experimental promotion by assertion | Proprietary replacements require conformance, security, compatibility, performance, update, and recovery evidence before production substitution |
| No agent-only authority | Critical economic, consensus, signing, kernel, driver, crypto, production-policy, and release decisions require named human owners |
| No fabricated completion | Documentation, interfaces, placeholders, and passing happy-path demos do not equal implemented or verified capability |

## Integrated V1 trains

### Train 0 — Governance, repository, and reproducible foundation

Train 0 establishes the control plane for the entire program. It preserves source integrity; assigns ownership; defines the ADR/RFC, requirement, risk, issue, and evidence schemas; configures the monorepo and toolchain; creates the stable ID/versioning policy; establishes threat zones; provides a deterministic local build; and activates CI, provenance, dependency, license, secret, and artifact checks.

| Deliverable | Exit evidence |
|---|---|
| Source and owner-directive validation | Canonical checksum and authority-order test |
| Toolchain and repository baseline | Clean checkout configures, builds, tests, and produces identical documented artifacts on supported environments |
| Requirements and decision control | Seventy-two V1 requirements, ADR/RFC templates, risk register, owners, and traceability checks |
| Security/provenance baseline | Threat model, trust zones, secret policy, SBOM, dependency/license scan, signed development artifact path |
| Domain ownership map | Every app, engine, AI, protocol, service, Chain, Arena, and PYRAMID path points to a domain spec and owner role |

### Train 1 — Semantic project, Shell, native runtime, and small-game path

Train 1 builds the smallest coherent native product. A `.axiom` project contains stable semantic IDs, source, assets, packages, tests, settings, and build metadata. The controller-first Shell exposes the seven locked tabs. DEV Simple and Advanced open the same project. The engine skeleton provides platform, memory, ECS/object, FABRIC jobs, reflection, serialization, Flow/AXIR, package/build, input, UI, renderer, audio, physics, and runtime hooks sufficient for a small native title.

The exit scenario creates a project, edits the same entity through Simple and Advanced, builds a signed development package, installs it into GAMES, launches it, saves state, records telemetry, and reproduces the result from a clean checkout.

### Train 2 — Native AI development loop and Gauntlet

Train 2 implements PRIME, Intent Compiler, requirement-first planning, context assembly, model routing, capability broker, isolated agents, consequence tiers, memory, provenance, history, rollback, and Gauntlet evidence. No external orchestration product becomes a shipping dependency.

The exit scenario begins with a natural-language mechanic request, normalizes requirements, presents a plan and impact, performs bounded branch-scoped changes, runs deterministic verification, displays evidence, allows Advanced inspection/editing, and returns to Simple without conversion or lost history.

### Train 3 — Complete engine, rendering, simulation, audio, and networking profiles

Train 3 completes the native engine path: NEXUS, PHOTON, WORLDSTREAM, OPTICS, materials/shaders, atmosphere/weather, water, vegetation, character rendering, VFX, physics/destruction, animation/facial systems, ORPHEUS, UI/input/haptics, runtime AI/navigation, simulation LOD, persistence, replays, spectating, and all named network profiles.

Large-shard cells are implemented and exercised through deterministic V1 simulations; their production activation remains bounded by measured scale and operating cost. Exit evidence includes small-game and high-fidelity reference projects, frame-time and memory distributions, loading/streaming tests, network fault tests, replay determinism, dedicated server operation, and cross-platform build evidence.

### Train 4 — Connect, Unreal Bridge, Store, Media, Social, Profile, and cloud services

Train 4 exposes stable AXIOM Connect capabilities and typed SDKs, then builds Unreal inventory/import/translation with category-specific compatibility and license reports. It implements identity, profiles, social graph, messaging, media capture/edit/export/broadcast, cloud project/build storage, Store catalog, certification, entitlements, installation, updates, refunds, moderation, support, policy, telemetry, and developer publishing.

The exit scenario analyzes an Unreal reference project without hiding unsupported content; separately, an external developer creates, submits, certifies, publishes, purchases, installs, launches, updates, refunds, and supports a native title using sandbox or approved rails with complete audit evidence.

### Train 5 — AXIOM Chain, Wallet, digital objects, marketplace, and value rails

Train 5 implements the sovereign chain and complete economic foundation. It includes node networking and state sync, selected consensus, deterministic execution, native modules, AXVM contract path, migrations, validator/governance operations, testnet, production-candidate network, indexer, explorer, managed/self-custodial/organization wallet paths, trusted signing, recovery, digital objects, licenses, provenance, royalties, marketplace settlement, token/credits, fiat/payment adapters, reserves, payouts, chargebacks, tax records, and reconciliation.

| Economic proof | Required outcome |
|---|---|
| Object lifecycle | Mint, license, list, purchase, transfer, burn/freeze where policy allows, dispute, and provenance history |
| Creator economics | Split calculation, fee disclosure, royalty posting, reserve, payable, payout, refund, chargeback, and reconciliation |
| Wallet | Managed and self-custodial creation, trusted signing, policy denial, activity, recovery, compromised-key response |
| Chain resilience | Node restore, partition/fault simulation, invalid transition rejection, upgrade/migration, emergency module pause, explorer/indexer consistency |
| Ledger integrity | Debits equal credits, no duplicate mutation, concurrent settlement safety, reversal by compensating entry, projected balance equals journals |

Independent review is required before high-value activation, but implementation and testnet integration remain mandatory.

### Train 6 — Arena, prizes, player-funded contests, and wagering-compatible competition

Train 6 implements skill ratings, matchmaking, ladders, seasons, brackets, teams/rosters, authoritative match services, integrity profiles, anti-cheat, replay/evidence capture, sponsored pools, participant-funded pools, mixed pools, entry fees, one-to-one stake commitments, escrow, result attestation, disputes, appeals, settlement, limits, exclusions, fraud review, and operator/jurisdiction policy.

The exit program executes free, sponsored, player-funded, and one-to-one contest scenarios. Each locks its rules and build, evaluates identity/age/location/limits, reserves funds before play, captures evidence, creates a provisional and final result, handles cancellation/disconnect/cheat/dispute alternatives, settles exactly once, updates ratings appropriately, and reconciles Chain and off-chain ledgers. Real-value activation occurs only under the selected operator and approved policy profile; no implementation is moved to a later version.

### Train 7 — PYRAMID Virtual Target, OS, proprietary systems, and hardware

Train 7 implements the Virtual Target profiles and simulator, hardened immutable Linux-based OS, PLAY/DEV/NODE isolation, signed boot, A/B update, recovery, controller-first Shell, secure wallet service, diagnostics, firmware/controller interfaces, and P0/P1 physical prototypes.

The same V1 train owns executable PYRAMID Kernel, AXIOM GPU/driver, Secure Transport, Crypto API, Image/Media, AXIOM FS, and distributed-node workstreams. Each retains a mature production adapter until conformance gates pass. P2 custom-board and P3 custom-silicon programs receive architecture, feasibility, toolchain, firmware, security, thermal/power, economic, manufacturing, certification, and prototype milestones. Capital-intensive fabrication requires explicit approval, but the workstream is not removed from V1.

Exit evidence includes Virtual Target reports, OS boot and recovery, mode isolation, wallet/validator secret separation, NODE consent and resource limits, controller operation, P0/P1 thermal/acoustic/safety tests, proprietary implementation benchmarks, and P2/P3 decision packages.

### Train 8 — Cross-domain hardening and controlled production activation

Train 8 does not add missing product scope; it proves that the completed V1 system can operate. It covers performance/load/soak, external audits, red-team exercises, incident response, disaster recovery, backups/restores, support and moderation staffing, catalog and developer operations, economic reconciliation, regional/operator profiles, accessibility, localization, privacy requests, legal documents, and launch evidence.

A feature may remain `DISABLED_BY_POLICY` in a region or environment after V1 construction is complete. Its implementation, tests, evidence, and ownership remain part of V1.

## Cross-train dependency graph

```text
Train 0 Governance and Contracts
  ├─→ Train 1 Project/Shell/Runtime
  │     ├─→ Train 2 AI/Gauntlet
  │     ├─→ Train 3 Engine/Render/Simulation/Net
  │     └─→ Train 4 Connect/Bridge/Platform
  ├─→ Train 5 Chain/Wallet/Economy
  │     └─→ Train 6 Arena/Prizes/Wagers
  └─→ Train 7 PYRAMID/Proprietary/Hardware

Trains 1–7 ─→ Train 8 Cross-Domain Qualification and Activation
```

Train 5 can begin consensus, state, ledger, wallet, and policy simulations while Train 3 stabilizes. Train 7 can begin Virtual Target, OS, kernel, and hardware work while engine profiles evolve. Parallelism is allowed only where owned contracts and fixtures prevent incompatible forks.

## Immediate CodeSpring package

The first CodeSpring engagement establishes the executable foundation and the contract surface for every V1 domain. It is bounded in code volume, not in long-term scope.

| Order | Work item | Completion evidence |
|---:|---|---|
| 1 | Validate source, directive, repository, and seventy-two requirement records | Integrity validator and traceability report |
| 2 | Finalize work-package, ADR/RFC, risk, threat, event, schema, and evidence formats | Schema tests and example artifacts |
| 3 | Draft blocking ADRs for toolchain, `.axiom`, IDs, C++/Rust, ECS, renderer, physics, audio, networking, consensus, wallet custody, economic ledgers, policy, PYRAMID, and licensing | Compared options, consequences, owner, status |
| 4 | Implement `.axiom` v0, stable IDs, migrations, sample project, and round-trip validation | Parser/serializer/property tests |
| 5 | Implement AXIOM Connect v0 capability and permission schema | Generated types and positive/negative conformance tests |
| 6 | Create compilable interfaces for every domain, including Chain, Wallet, Arena value, and PYRAMID replacement/hardware workstreams | Dependency-graph and build evidence; no unlabeled empty paths |
| 7 | Implement deterministic hello-world native runtime and package/install/launch path | Clean environment reproduces result |
| 8 | Implement ledger amount/journal/escrow and chain state-transition simulation skeletons | Property tests, fault cases, mock provider, deterministic replay |
| 9 | Implement Virtual Target profile/report skeleton | Enforced fixture budgets and deterministic report |
| 10 | Configure CI/Gauntlet evidence | Format, compile, tests, compatibility, secret/dependency/license scans, SBOM, evidence manifest |

After this package, CodeSpring continues directly into the next dependency-valid train through reviewed pull requests; approval is not a pretext to move V1 systems into V2.

## Evidence standard

| Category | Minimum evidence |
|---|---|
| Traceability | Requirement, owner, ADR/RFC, work package, commits, builds, and test identifiers |
| Reproducibility | Clean setup, exact commands, locks, environment, deterministic fixtures, and artifact hashes |
| Correctness | Unit, property, integration, migration, gameplay, network, chain, ledger, and state-invariant results |
| Security | Threat delta, static/dynamic checks, fuzzing, permission negatives, secret scan, SBOM, independent findings |
| Economic | Journal samples, balance proof, holds/releases, concurrency/idempotency, refunds/chargebacks, reconciliation |
| Performance | Reference workload/hardware, distributions, budgets, regressions, resource and cost observations |
| Provenance | Dependencies, licenses, assets, models, generated output, modifications, and signed build metadata |
| Operations | Deployment/run procedure, metrics, alerts, degraded behavior, rollback, backup/restore, incident implications |
| Human authority | Named owners/reviewers, activation approvals, residual risk, temporary waivers, and expiry |

## Production activation gates

Activation gates remain strict precisely because construction is complete.

| Gate | Required proof before the affected production exposure |
|---|---|
| Architecture | Owned interfaces, migrations, compatibility, tests, failure modes, and recovery |
| Product/developer | New users can play/build and external developers can package, publish, update, and support titles |
| Security | No unresolved critical findings; keys, signing, agents, Chain, Wallet, Store, Arena, OS, and updates reviewed |
| Economic | Funds, credits/tokens, assets, royalties, refunds, reserves, prizes, wagers, and payouts reconcile under failure/dispute |
| Policy/legal | Operator, regions, eligibility, age, contest class, terms, rights, privacy, token/value disclosures, and tax responsibilities approved |
| Operations | Monitoring, on-call, support, moderation, reconciliation, incident response, backup/restore, and rollback staffed and tested |
| Performance | Engine, network, chain, services, OS, and hardware targets measured on named workloads |
| Hardware/capital | Manufacturing, certification, component, supply, custom-board, and custom-silicon decisions explicitly authorized |

Failure of an activation gate sets the capability to a restricted activation state. It does not change `V1-BUILD-REQUIRED`.

## Schedule policy

Dates are added only after owners, principal ADRs, baseline prototypes, staffing, provider dependencies, and capital assumptions are known. Until then, the honest planning unit is a dependency-ordered work package with measurable exit evidence. Schedule uncertainty never erases the complete V1 destination.
