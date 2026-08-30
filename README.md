# AXIOM-XIII V1

> **Private implementation repository for an AI-native game engine, creation environment, gaming protocol, desktop console, platform network, native blockchain, competitive economy, and PYRAMID hardware/software stack.**

**Status:** Governing specification, architecture, and implementation-control repository. The repository preserves the complete founder specification verbatim, converts it into domain-level engineering plans, and establishes a build-complete V1 program. It does not falsely claim that the engine, chain, operating system, services, or hardware have already been implemented.

## What AXIOM-XIII is

AXIOM-XIII is one integrated creation and gaming platform. It combines a native engine, an AI-first development environment, a controller-first consumer shell, a protocol shared by games and services, a publishing and commerce platform, competitive infrastructure, a sovereign game-native blockchain, and a PYRAMID computer-console program.

The locked product shell is **GAMES · MEDIA · SOCIAL · DEV · STORE · PROFILE · WALLET**. These surfaces are not independent applications assembled around a launcher. They are views over a common identity, entitlement, project, content, economic, and policy system.

The engine and platform are organized around five non-negotiable ideas. First, **DEV Simple and DEV Advanced manipulate the same semantic project**; changing interfaces never converts or forks the user’s work. Second, **AXIOM AI plans against explicit requirements and produces inspectable evidence** rather than hiding unbounded changes behind chat. Third, **the native engine and platform own their interfaces**, even when production initially uses mature third-party implementations behind those interfaces. Fourth, **Unreal is a migration and translation bridge**, not the runtime foundation. Fifth, **creators retain ownership of their original games and content while AXIOM retains ownership of its engine, platform, services, formats, and proprietary technology**.

## Governing authority and source preservation

The authoritative source is [`docs/source/AXIOM-XIII-V1-Master-Specification.md`](docs/source/AXIOM-XIII-V1-Master-Specification.md). It is a byte-for-byte copy of the supplied source and has SHA-256 digest:

```text
dc7feae7b999e8c4802ef8fb67fa894c68e75e8cf1f601132ccb162f6565909d
```

The source remains immutable for provenance. The founder’s later clarification is recorded in [`docs/source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md`](docs/source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md). That directive controls current scope wherever the preserved source describes a capability as future, later, Preview, Experimental, Architected, deferred, non-blocking, or outside V1.

| Priority | Authority | Repository effect |
|---:|---|---|
| 1 | Founder owner directives | Control current product intent and may override historical scope or timing language |
| 2 | Verbatim master specification | Governs product canon and all details not superseded by a later directive |
| 3 | Approved ADRs and RFCs | Resolve architecture and implementation choices without weakening founder requirements |
| 4 | Requirements, acceptance, risk, and domain specifications | Translate canon into traceable engineering obligations |
| 5 | Backlogs, code, tests, releases, and evidence | Implement and prove the approved system |

No derived document may silently erase a founder decision. If two artifacts conflict, the conflict must be recorded, the higher authority must be followed, and the lower artifact must be corrected through review.

## Build-complete V1 doctrine

**Every capability described as part of the intended AXIOM-XIII or PYRAMID destination is mandatory V1 build scope.** This includes the native blockchain, wallet, tokens and credits, marketplace, creator royalties, paid entry, player-funded prize pools, wagering-compatible skill contests, escrow, settlement, cash-equivalent rails, all networking profiles, high-fidelity rendering, large-world streaming, platform services, Unreal migration, PYRAMID OS, PYRAMID Kernel, GPU/driver work, secure transport, cryptography APIs, media codecs, filesystem work, physical reference hardware, and the custom board/silicon program.

The program distinguishes three independent questions:

| Dimension | Governing question | Example states |
|---|---|---|
| **Build obligation** | Must the capability be constructed during V1? | All described capabilities are `V1-BUILD-REQUIRED` |
| **Assurance** | How much evidence supports the implementation? | Prototype, Integrated, Verified, Audited, Production-Qualified |
| **Activation** | Where and for whom may it operate? | Local, Sandbox, Testnet, Pilot, Region-Limited, Production-Enabled, Disabled-by-Policy |

A security, legal, provider, capital, performance, or hardware gate can prevent unsafe public exposure. It **cannot** remove architecture, interfaces, implementation, local execution, simulation, testnet operation, adversarial testing, or end-to-end integration from V1. “Blocked for activation” is not “deferred from construction.”

This doctrine allows the repository to remain honest. A proprietary kernel can be mandatory V1 construction while the shipping OS continues to use a hardened Linux foundation until the kernel passes replacement gates. A player-funded contest can be fully implemented and tested while production policy disables it in an unapproved jurisdiction. A chain module can run on testnet while independent audits remain open. The system is built now; exposure follows evidence.

## Integrated system architecture

AXIOM-XIII is divided into stable domains with typed boundaries. The boundaries protect the program from becoming one inseparable codebase while preserving a coherent product.

| Domain | Primary repository paths | Responsibility |
|---|---|---|
| **Product and Shell** | `apps/desktop-shell`, `apps/dev-simple`, `apps/dev-advanced`, `apps/store`, `apps/wallet`, `apps/arena` | Seven-tab consumer shell, creation UX, accessibility, identity surfaces, and controller-first operation |
| **AXIOM AI** | `ai/prime`, `ai/intent-compiler`, `ai/planner`, `ai/model-router`, `ai/capability-broker`, `ai/agents`, `ai/gauntlet` | Requirement normalization, planning, permissions, model routing, isolated agents, memory, verification, and evidence |
| **Semantic project system** | `engine/axir`, `engine/packages`, `connect/schemas`, `bridge/unreal` | Stable IDs, project graph, `.axiom` and `.ax*` formats, semantic diffs, source control, Connect contracts, and migration |
| **Engine core** | `engine/core`, `engine/ecs`, `engine/fabric`, `engine/memory`, `engine/reflection`, `engine/serialization`, `engine/flow`, `engine/platform` | Runtime, object model, jobs, memory, reflection, persistence, scripting, ABI/FFI, packages, builds, and tools |
| **Rendering** | `engine/render/*` | AXIOM RENDER, NEXUS geometry, PHOTON lighting, WORLDSTREAM, OPTICS, materials, atmosphere, water, vegetation, characters, and VFX |
| **Simulation and presentation** | `engine/physics`, `engine/animation`, `engine/audio-orpheus`, `engine/ui`, `engine/input`, `engine/navigation`, `engine/ai-runtime` | Physics, destruction, motion, facial systems, audio/music, UI, input/haptics, runtime AI, navigation, and simulation LOD |
| **Networking and protocol** | `engine/networking`, `engine/replay`, `protocol/*`, `services/gameservers`, `services/matchmaking` | Authority, replication, rollback, lockstep, large shards, replays, spectating, canonical objects/events, and persistence |
| **Chain and Wallet** | `chain/*`, `protocol/wallet`, `services/ledger`, `services/payments` | Sovereign blockchain, consensus, state, execution, validators, wallet custody, digital objects, token/credits, royalties, and cash-equivalent adapters |
| **Arena and trust** | `apps/arena`, `protocol/arena`, `services/arena`, `services/moderation`, `tests/security` | Ratings, matchmaking, ladders, tournaments, team competition, pools, wagers, evidence, anti-cheat, fraud, disputes, and appeals |
| **Store, Media, Social, and Profile** | `apps/store`, `apps/media`, `apps/social`, `apps/profile`, `services/store`, `services/media`, `services/social` | Publishing, certification, catalog, entitlements, commerce, capture/edit/broadcast, identity graph, messaging, IP, licenses, and provenance |
| **Policy and operations** | `services/policy`, `services/telemetry`, `infra`, `tests`, `.github` | Operator/jurisdiction policy, privacy, safety, observability, CI/CD, incidents, recovery, accessibility, and launch evidence |
| **PYRAMID** | `pyramid/*` | Virtual Target, production OS, kernel, drivers, secure system programs, controller/firmware, physical hardware, enclosure, manufacturing, and certification |

The complete dependency view is maintained in [`docs/architecture/system-map.md`](docs/architecture/system-map.md). The expanded implementation specifications are indexed under [`docs/domains/`](docs/domains/).

## Product and creation experience

A user should be able to enter DEV with an idea, normalize that idea into requirements, inspect a plan, authorize bounded work, see changes appear in the project, test the result, review evidence, and continue in either Simple or Advanced mode without conversion. Simple mode presents intent, guided controls, safe defaults, previews, and outcomes. Advanced mode exposes the same project through graphs, source, assets, packages, profiling, networking, rendering, and build controls.

AXIOM AI uses a consequence model. Read-only analysis and reversible drafts can proceed with low friction. Project mutations require an explicit plan, claimed scope, and rollback path. Publishing, signing, wallet activity, economic changes, security policy, deployment, and destructive operations require progressively stronger authorization and evidence. Agents work in isolated branches or worktrees, cannot treat repository content as trusted instructions, and cannot bypass the capability broker.

The Gauntlet is the acceptance system. It combines deterministic tests, build validation, scenario tests, visual evidence, performance measurements, security checks, provenance, change summaries, and rollback evidence. “The agent says it works” is never acceptance.

## Engine and high-fidelity path

The native engine is a modular C++/Rust system with explicit ABI/FFI boundaries, platform abstraction, semantic types, owned formats, and reproducible builds. The object model, job system, allocator strategy, serialization, reflection, scripting, package manager, build graph, and tooling are foundational; higher-level systems cannot bypass them through untracked custom data.

AXIOM RENDER includes the complete intended V1 path: NEXUS virtualized geometry, PHOTON lighting/reflections/path tracing, WORLDSTREAM world and asset streaming, OPTICS camera, programmable materials and shaders, atmosphere and weather, water, vegetation, character rendering, animation integration, and VFX. The implementation must operate through capability detection and quality profiles rather than assuming one GPU. Performance budgets are measured by reference scenes and PYRAMID profiles, not promotional labels.

Physics, destruction, animation, facial motion, ORPHEUS audio/music, UI, input, haptics, navigation, runtime AI, and causal simulation share the same deterministic evidence and profiling framework. Networking must support authoritative replication, rollback, lockstep, asynchronous play, local play, and the large-shard program behind explicit profiles. These are all V1 construction obligations, even when a game activates only one profile.

## Native blockchain, wallet, and digital economy

AXIOM Chain is a sovereign, game-native blockchain rather than a generic chain renamed for gaming. V1 must include runnable node software, a selected consensus profile, deterministic state execution, versioned migrations, native protocol modules, validators and governance, indexer, explorer, wallet core, recovery, telemetry, testnet, and a production-candidate network.

The chain records compact canonical evidence: ownership, license and provenance references, digital objects, creator splits, tournament commitments, result attestations, escrow state, settlements, and governance. Large media, private gameplay, identity documents, and unnecessary personal data remain off-chain. Content hashes and signed references connect the two worlds.

Wallet supports managed, self-custodial, and organization/treasury paths. Signing occurs in a trusted surface that displays the human-readable consequence, asset, value, fee, permissions, counterparty, and policy result. Games and marketplace content cannot imitate or replace that surface. Keys are separated by purpose and assurance; production treasury and platform signing use isolated infrastructure and dual control.

The economic architecture separates:

| Economic boundary | Purpose |
|---|---|
| **Fiat/payment ledger** | External deposits, withdrawals, refunds, chargebacks, processor settlement, reserves, and reconciliation |
| **Internal credit/token ledger** | Platform-denominated balances, holds, fees, liabilities, issuance, supply controls, and conversions |
| **On-chain state** | Wallet ownership, digital objects, escrow/settlement records, creator splits, and verifiable protocol events |
| **Entitlement system** | Rights to install, access, participate, consume, or use a product independent of the payment rail |
| **Creator payable ledger** | Earned revenue, royalties, reserves, adjustments, tax status, payout eligibility, and payout history |

The system implements mint, transfer, burn, license, listing, offer, purchase, fee, royalty, refund, dispute, escrow, release, and recovery flows with idempotency and audit evidence. A token does not silently grant intellectual-property rights. Rights are defined by explicit, versioned licenses.

## Arena, prizes, and wagering-compatible skill competition

Arena provides rating pools, skill-based matchmaking, ladders, seasons, brackets, team rosters, tournament administration, spectator/replay evidence, and verifiable results. It supports sponsored, platform-funded, and player-funded prize structures plus one-to-one or tournament stake commitments where the operator and jurisdiction permit them.

A paid competition follows an auditable lifecycle: rule version and build are locked; participant identity, age, location, exclusions, limits, and eligibility are evaluated; funds are reserved before play; an authoritative match service and integrity profile are assigned; deterministic evidence and replays are retained; the result is attested; a dispute window opens; and settlement occurs only after finality. Cancellation, disconnect, cheating suspicion, void results, refunds, chargebacks, appeals, and operator intervention are first-class states rather than manual exceptions.

The platform does not conceal legal uncertainty in code. Operator profiles and jurisdiction policy determine which contest forms, funding sources, values, currencies, age thresholds, verification levels, and cash-out paths are active. These controls restrict exposure but do not excuse incomplete implementation.

## Store, creator economy, Media, Social, and Profile

Store owns catalog, publishing intake, certification, prices, purchases, entitlements, installation, updates, refunds, creator revenue shares, and marketplace discovery. It integrates standard commerce, chain settlement, credits/tokens, and payable ledgers without merging their accounting boundaries.

Creators can define license terms, commercial rights, collaborators, split recipients, royalties, provenance, training permissions, and distribution policies. The Originality Firewall records sources and rights evidence, detects missing or contradictory grants, and can block publishing pending review. It does not pretend automated similarity analysis is legal proof.

Media provides capture, replay, editing, export, livestream/broadcast integration, and ORPHEUS music workflows. Social and Profile provide the identity graph, privacy controls, messaging, blocks, moderation, game presence, creator pages, competitive records, achievements, and wallet-linked public identity without exposing sensitive custody or compliance records.

## PYRAMID software and hardware program

The PYRAMID Virtual Target exists before final hardware. It defines CPU/GPU feature class, memory, storage, display/frame profiles, input/controller, audio, network, secure storage, operating APIs, thermal/power envelope, package format, update behavior, and certification tests. Developers can build against **Quality**, **Performance**, and **Competitive** profiles and receive measured compatibility reports.

The production software path begins with a hardened, immutable Linux-based PYRAMID OS using verified boot where supported, read-only system images, atomic A/B updates, sandboxed applications, controller-first Shell, secure wallet service, recovery, diagnostics, and explicit PLAY/DEV/NODE separation.

In parallel, V1 constructs the PYRAMID Kernel, AXIOM GPU/driver path, Secure Transport, Crypto APIs, Image/Media path, AXIOM FS, firmware, controller, and hardware programs. The production system may continue using reviewed dependencies until each proprietary replacement passes correctness, compatibility, security, performance, update, and recovery gates. Replacement gates control substitution, not construction.

The physical sequence covers P0 industrial/design prototype, P1 controlled reference computer, P2 custom board/platform, and P3 custom-silicon program. The V1 repository must contain requirements, interfaces, simulations, benchmarks, prototype plans, manufacturing and certification evidence models, and owned workstreams for all four generations. Capital-intensive fabrication is governed by explicit founder and financing decisions, but it is not erased from V1 architecture.

## Security, privacy, provenance, and operational doctrine

The trust model separates public clients, authenticated clients, projects, game runtimes, agents, build workers, cloud services, Chain nodes, wallet/signing systems, payment providers, operator/admin systems, and PYRAMID secure services. Cross-zone operations use typed authenticated interfaces and least privilege.

The security baseline includes threat models, capability-based agent permissions, sandboxing, secret isolation, signed and reproducible artifacts, SBOMs, dependency and license controls, provenance, branch protection, code review, static/dynamic analysis, fuzzing, adversarial simulations, rate limits, abuse controls, immutable economic records, dual control, incident response, and disaster recovery. No production keys or user secrets belong in source, prompts, screenshots, logs, or ordinary CI.

Privacy and safety are product features. The platform minimizes sensitive data, classifies purpose and retention, separates compliance identity from public identity, supports export and deletion where legally possible, preserves legal holds, protects minors, controls messaging and discovery, records administrative access, and avoids putting sensitive personal information on immutable ledgers.

## How the V1 program is sequenced

Build-complete does not mean “build everything in one pull request.” Work proceeds through dependency-ordered trains that remain inside the same V1 program.

| Train | Required integrated outcome |
|---:|---|
| 0 | Governance, source integrity, standards, ownership, threat model, ADR/RFC process, requirements traceability, CI, test harness, and reproducible bootstrap |
| 1 | `.axiom` semantic project, Shell, DEV continuity, engine/core skeleton, package/build/install path, and small native game |
| 2 | PRIME/Intent Compiler/planner/capability broker, isolated agents, Gauntlet, evidence, rollback, and model-provider abstraction |
| 3 | Renderer, physics, animation, audio, UI/input, runtime AI, networking profiles, persistence, replay, and high-fidelity reference scenes |
| 4 | Identity, Social/Profile, Media, Store, publishing, certification, entitlements, game servers, moderation, telemetry, and first-party validation games |
| 5 | AXIOM Chain, Wallet, digital objects, licenses, marketplace settlement, creator royalties, testnet, explorer, and recovery |
| 6 | Arena ratings, matchmaking, ladders, tournaments, teams, anti-cheat, sponsored/player-funded pools, wagers, escrow, result attestation, disputes, and settlement |
| 7 | PYRAMID Virtual Target, OS image, modes, firmware/controller, P0/P1 prototypes, kernel/GPU/transport/crypto/media/FS programs, and P2/P3 workstreams |
| 8 | Cross-domain hardening, audits, performance/scale, regional/operator activation profiles, disaster-recovery drills, release evidence, and selective production enablement |

A train may begin preparatory work before the previous train is fully promoted, but stable contracts and safety-critical dependencies must be respected. Every formerly deferred feature receives an owner, package path, acceptance criteria, tests, and a completion status.

## CodeSpring execution contract

CodeSpring starts with [`CODESPRING.md`](CODESPRING.md), then reads the owner directive, master specification, architecture map, domain index, requirements register, acceptance matrix, risk register, roadmap, ADR index, threat model, and provenance policy.

Every implementation package must state the requirement IDs, objective, user or operator outcome, affected modules, dependencies, schema/API/event changes, security and privacy impact, economic impact, failure modes, observability, acceptance criteria, test commands, evidence, migration, and rollback. Shared contracts change only through coordinated ADR/RFC work. Critical financial, consensus, signing, kernel, driver, crypto, anti-cheat, and production-policy changes require named human ownership and independent review.

Agents must never use “gated,” “experimental,” “future,” or “later” as a reason to skip implementation. They must write the production boundary and complete the local/sandbox/testnet implementation while the activation gate remains visible.

## Repository map and written implementation corpus

| Document | Purpose |
|---|---|
| [`docs/source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md`](docs/source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md) | Governing clarification that all described capabilities are mandatory V1 construction |
| [`docs/source/AXIOM-XIII-V1-Master-Specification.md`](docs/source/AXIOM-XIII-V1-Master-Specification.md) | Verbatim founder specification |
| [`docs/domains/`](docs/domains/) | Fully written product, engine, AI, chain, economy, Arena, platform, operations, and PYRAMID implementation specifications |
| [`docs/analysis/deep-analysis.md`](docs/analysis/deep-analysis.md) | Feasibility, architecture, dependency, risk, and contradiction analysis |
| [`docs/architecture/system-map.md`](docs/architecture/system-map.md) | System boundaries, dependencies, and trust relationships |
| [`docs/requirements/requirements-register.md`](docs/requirements/requirements-register.md) | Traceable requirements and ownership controls |
| [`docs/requirements/acceptance-matrix.md`](docs/requirements/acceptance-matrix.md) | Production acceptance and evidence gates |
| [`docs/requirements/risk-register.md`](docs/requirements/risk-register.md) | Program risks, triggers, mitigations, and contingencies |
| [`docs/roadmap/implementation-roadmap.md`](docs/roadmap/implementation-roadmap.md) | Dependency-ordered V1 implementation program |
| [`docs/roadmap/v1-160-tickets.md`](docs/roadmap/v1-160-tickets.md) | Complete 160-ticket build-complete V1 backlog |
| [`docs/adr/README.md`](docs/adr/README.md) | Open architecture decisions |
| [`docs/security/threat-model-v0.md`](docs/security/threat-model-v0.md) | Initial threats, trust zones, and controls |
| [`docs/legal/provenance-and-license-policy-v0.md`](docs/legal/provenance-and-license-policy-v0.md) | Ownership, licensing, provenance, and clean-room controls |

## Current truth

This repository is comprehensive planning and implementation control, not a fabricated completion claim. The source is preserved, the V1 scope is explicit, the monorepo paths exist, and the domain specifications define what must be built. Most runtime directories remain implementation targets rather than finished production systems. Open ADRs, named owner assignments, provider selection, legal operator decisions, hardware profiles, and evidence thresholds still require resolution.

That distinction is intentional: **nothing described is removed from V1, and nothing unimplemented is mislabeled as complete**.

## Confidentiality and licensing

This repository is private and proprietary. No public license is granted. See [`LICENSE`](LICENSE), [`LICENSES/PROPRIETARY.md`](LICENSES/PROPRIETARY.md), [`SECURITY.md`](SECURITY.md), and [`CONTRIBUTING.md`](CONTRIBUTING.md). Do not publish, mirror, redistribute, sublicense, or train external models on its contents without written authorization from the owner.

## TL;DR: CodeSpring launch sequence

1. Clone the private repository and create a short-lived branch from `develop`.
2. Read [`docs/source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md`](docs/source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md) before interpreting any historical maturity label.
3. Read [`CODESPRING.md`](CODESPRING.md), the verbatim master specification, and the relevant document under [`docs/domains/`](docs/domains/).
4. Confirm the ticket has requirement IDs, dependencies, owned files, acceptance criteria, tests, evidence, and rollback.
5. Build the smallest dependency-valid vertical slice without deleting or deferring later V1 obligations.
6. For blockchain, wallet, prize, wager, payment, kernel, driver, crypto, signing, or production-policy work, keep construction moving in local/sandbox/testnet while activation controls remain explicit.
7. Run repository validation, compilation, tests, Gauntlet checks, security scans, and documentation checks before opening a pull request.
8. Attach evidence and update project memory, requirements, risks, ADRs, APIs, schemas, events, and runbooks affected by the change.
9. Merge through `develop` → `staging` → `main`; never force-push shared branches or bypass named human review.
10. Declare a capability complete only when its implementation and evidence satisfy the domain Definition of Done—never because a placeholder directory or document exists.
