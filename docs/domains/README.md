# AXIOM-XIII V1 Domain Implementation Corpus

This directory turns the preserved master specification into fully written implementation documents. Each document is derived from the canonical source and interpreted through the build-complete V1 owner directive. The corpus is not a substitute for source code or evidence; it is the engineering contract that prevents empty directories, disconnected components, and silent deferral.

## Reading rule

Read [`../source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md`](../source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md) first. Every described capability is a V1 build obligation. A maturity or policy gate may constrain production activation, but it cannot remove the architecture, code, simulation, tests, integration, operations, or ownership required in V1.

## Domain documents

| Domain specification | Primary implementation paths | V1 outcome |
|---|---|---|
| [`axiom-xiii-product-shell-ux.md`](axiom-xiii-product-shell-ux.md) | `apps/desktop-shell`, `apps/dev-simple`, `apps/dev-advanced`, consumer platform apps | Locked Shell navigation, coherent identity, controller-first operation, accessible workflows, and one-project Simple/Advanced continuity |
| [`axiom-ai-domain-specification.md`](axiom-ai-domain-specification.md) | `ai/prime`, `ai/intent-compiler`, `ai/planner`, `ai/model-router`, `ai/capability-broker`, `ai/agents`, `ai/gauntlet` | Requirement-first planning, bounded agents, model abstraction, permissioned mutations, memory, verification, and evidence |
| [`semantic-project-graph.md`](semantic-project-graph.md) | `engine/axir`, `engine/packages`, `connect`, `bridge`, project services | Stable semantic graph, `.axiom`/`.ax*` formats, source control, semantic diffs, Connect capabilities, and Unreal migration |
| [`engine-core-specification.md`](engine-core-specification.md) | `engine/core`, `ecs`, `fabric`, `memory`, `reflection`, `serialization`, `flow`, `platform`, `packages`, `devtools` | Native runtime foundation, C++/Rust boundary, jobs, data model, scripting, packaging, build, patch, and tools |
| [`axiom-render-specification.md`](axiom-render-specification.md) | `engine/render/*` | NEXUS, PHOTON, WORLDSTREAM, OPTICS, materials, atmosphere, weather, water, vegetation, characters, and VFX |
| [`physics-ui-audio-ai-domain-spec.md`](physics-ui-audio-ai-domain-spec.md) | `engine/physics`, `animation`, `audio-orpheus`, `ui`, `input`, `navigation`, `ai-runtime` | Physics/destruction, motion/facial systems, ORPHEUS, UI/input/haptics, navigation, runtime AI, and simulation LOD |
| [`axiom-net-domain-specification.md`](axiom-net-domain-specification.md) | `engine/networking`, `engine/replay`, `protocol`, multiplayer/persistence services | Authoritative, rollback, lockstep, asynchronous, local, and large-shard networking plus replay, spectating, and evidence |
| [`axiom-chain-domain.md`](axiom-chain-domain.md) | `chain`, `protocol/wallet`, `services/ledger`, `services/payments` | Sovereign chain, consensus, execution, wallet, tokens/credits, objects, licenses, royalties, marketplace, escrow, cash rails, and audits |
| [`axiom-xiii-arena.md`](axiom-xiii-arena.md) | `apps/arena`, `protocol/arena`, Arena/matchmaking/moderation services | Ratings, matchmaking, ladders, tournaments, teams, sponsored/player-funded pools, wagers, attestations, anti-cheat, disputes, and settlement |
| [`axiom-store-domain.md`](axiom-store-domain.md) | Store/Media/Social/Profile apps and services, protocol assets/licenses/provenance | Publishing, certification, entitlements, creator economics, media, identity graph, rights, provenance, and Originality Firewall |
| [`axiom-xiii-policy-operations-spec.md`](axiom-xiii-policy-operations-spec.md) | Policy, telemetry, infra, CI/CD, tests, incident and recovery paths | Trust zones, security, privacy, moderation, observability, Gauntlet, accessibility, live operations, incidents, and release evidence |
| [`pyramid-virtual-target-spec.md`](pyramid-virtual-target-spec.md) | `pyramid/*` | Virtual Target, Linux production OS, PLAY/DEV/NODE, kernel/GPU/transport/crypto/media/FS, firmware/controller, P0–P3, manufacturing, and certification |

## Cross-domain build order

The documents must not be implemented as isolated product silos. Their primary dependency sequence is:

```text
Governance and semantic IDs
→ project formats and Connect contracts
→ engine/platform foundations
→ product Shell and DEV continuity
→ AI planning and Gauntlet
→ rendering/simulation/audio/networking
→ identity, Store, Media, Social, Profile, and cloud services
→ Chain, Wallet, digital objects, ledger, and marketplace settlement
→ Arena competition, evidence, prizes, wagers, and settlement
→ PYRAMID Virtual Target, OS, proprietary replacements, and physical program
→ cross-domain hardening, audits, recovery, and controlled production activation
```

Work may overlap when contracts are stable, but a downstream team cannot bypass its upstream source of truth. Arena does not maintain a second balance. Store does not invent a second license model. Games do not implement a private signing UI. Agents do not create untracked project mutations. PYRAMID does not expose wallet or validator secrets to packages.

## Completion model

Each domain uses three independent states:

| State | Meaning |
|---|---|
| **Build status** | Whether the architecture, implementation, tests, documentation, and ownership exist |
| **Assurance status** | Whether the capability is Prototype, Integrated, Verified, Audited, or Production-Qualified |
| **Activation status** | Whether it is enabled in Local, Sandbox, Testnet, Pilot, Region-Limited, or Production environments |

No document may mark a capability “done” because it is described. No team may mark it “out of V1” because production activation is restricted. The repository must always say what exists, what has evidence, what remains unverified, and where the capability is permitted to run.

## Maintaining this corpus

When a change affects a stable format, public API, protocol object, chain state, economic rule, wallet behavior, competition rule, security boundary, or hardware profile, update the relevant domain document in the same pull request. Link the requirement, ADR/RFC, migration, tests, evidence, and rollback. If a founder directive changes scope, preserve the prior source, add the new directive, and update all derived artifacts consistently.
