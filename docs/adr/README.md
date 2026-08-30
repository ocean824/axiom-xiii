# Mandatory Architecture Decision Records

The following ADRs are required by section 80 of the [master specification](../source/AXIOM-XIII-V1-Master-Specification.md). Each begins in **Proposed** state. CodeSpring may research and draft alternatives, but a named authorized human must accept a decision.

| ADR | Decision | Status | Blocking domains |
|---:|---|---|---|
| [0001](0001-ip-ownership-and-protocol-entity.md) | Exact ownership/entity structure for AXIOM IP and protocol | Proposed | Licensing, contributions, source access, commercialization |
| [0002](0002-core-language-boundary-and-build-toolchain.md) | Core C++/Rust boundary and build toolchain | Proposed | Engine, services, CI, packaging |
| [0003](0003-axiom-manifest-and-schema-language.md) | `.axiom` manifest and schema language | Proposed | Project format, migrations, tools, Bridge |
| [0004](0004-axir-format-and-execution-backend.md) | AXIR format and execution backend | Proposed | Flow, scripting, runtime, determinism |
| [0005](0005-ui-shell-bootstrap-technology.md) | UI shell bootstrap technology and migration to AXIOM UI | Proposed | Shell, DEV, Store, Wallet |
| [0006](0006-ecs-storage-model.md) | ECS storage model | Proposed | Runtime, serialization, editor, networking |
| [0007](0007-renderer-backend-order-and-shader-toolchain.md) | Renderer backend order and shader toolchain | Proposed | Renderer, build, target profiles |
| [0008](0008-production-physics-dependency.md) | Production physics dependency and replacement interface | Proposed | Physics, gameplay API, migration |
| [0009](0009-production-audio-backend.md) | Production audio backend and plugin-hosting sandbox | Proposed | ORPHEUS, editor, packaging |
| [0010](0010-network-transport-and-server-orchestration.md) | Networking transport and dedicated server orchestration | Proposed | NET, services, Arena, replays |
| [0011](0011-chain-consensus-profile.md) | Chain consensus algorithm/profile | Proposed | Node, operations, validator economics |
| [0012](0012-chain-state-and-contract-runtime.md) | Chain state model and contract/runtime strategy | Proposed | Digital objects, modules, AXVM |
| [0013](0013-native-token-necessity-and-economics.md) | Native token necessity and economics | Proposed | Chain, Wallet, Arena, policy |
| [0014](0014-managed-wallet-custody.md) | Managed wallet custody model | Proposed | Wallet, identity, recovery, compliance |
| [0015](0015-store-payments-and-ledger-boundaries.md) | Store payment providers and ledger boundaries | Proposed | Store, payments, refunds, tax |
| [0016](0016-arena-rating-and-prize-policy.md) | Arena rating and prize policy profiles | Proposed | Matchmaking, tournaments, escrow |
| [0017](0017-production-cloud-storage-database.md) | Production cloud, storage, and database stack | Proposed | Services, data residency, disaster recovery |
| [0018](0018-source-available-license-and-economics.md) | Source-available license structure and economic thresholds | Proposed | Distribution, contributions, creator adoption |
| [0019](0019-pyramid-p1-reference-hardware.md) | PYRAMID P1 reference hardware class | Proposed | Virtual Target, performance, supply chain |
| [0020](0020-pyramid-os-base.md) | PYRAMID OS distribution/base | Proposed | OS image, updates, security |
| [0021](0021-kernel-architecture-and-boot-target.md) | Kernel architecture and boot target | Proposed | Experimental kernel, firmware, drivers |
| [0022](0022-anti-cheat-privilege-level.md) | Anti-cheat privilege level | Proposed | Security, privacy, competitive integrity |
| [0023](0023-privacy-and-telemetry-defaults.md) | Privacy and telemetry defaults | Proposed | AI, services, analytics, compliance |
| [0024](0024-first-reference-game.md) | First AXIOM Original used as the engine reference game | Proposed | Validation matrix, roadmap, content resources |
| [0025](0025-public-names-and-trademark-clearance.md) | Public names/trademark clearance for AXIOM-XIII and PYRAMID | Proposed | Branding, launch, legal |

## Required ADR structure

Each ADR must document the context, decision drivers, considered options, evidence, security and privacy implications, legal and licensing implications, operational and migration consequences, decision, status, approvers, and review date. Rejected options must remain visible so that future teams understand why a choice was made.

An ADR must not be marked Accepted until its named owner and reviewers are recorded. High-risk decisions involving cryptography, custody, token economics, prize systems, privacy, anti-cheat privilege, licensing, or public marks require the relevant specialist review before acceptance.
