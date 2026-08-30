# Owner Directive: AXIOM-XIII V1 Is Build-Complete

- **Directive authority:** Founder/Product Owner Ø
- **Effective date:** 2026-08-30
- **Status:** Governing clarification and scope override
- **Applies to:** AXIOM-XIII V1 repository, requirements, architecture, backlogs, roadmaps, milestones, implementation agents, testing, and release planning
- **Preservation rule:** The original master specification remains preserved verbatim for provenance. Where that source classifies a described capability as future, Preview, Experimental, Architected, later, deferred, optional, non-blocking, or outside V1, this directive governs the implementation scope.

## Executive directive

AXIOM-XIII V1 is a **build-complete platform release program**. Every capability described as part of the intended AXIOM-XIII or PYRAMID product—including native blockchain functionality, wallets, tokens and digital objects, real-value competition, paid entry, player-funded prize pools, wagering-compatible contest infrastructure, escrow, settlement, cash-equivalent value flows, marketplaces, creator royalties, the full engine and renderer path, Unreal migration, platform services, PYRAMID software, and proprietary replacement programs—must be represented as mandatory V1 implementation scope.

No roadmap gate, maturity label, compliance dependency, security review, jurisdiction rule, provider dependency, capital constraint, or unresolved ADR may be interpreted as permission to remove, indefinitely defer, omit, or replace these capabilities with documentation-only placeholders. The organization must build the code, schemas, interfaces, service boundaries, simulations, sandbox flows, operational controls, test suites, and end-to-end integration required for the full V1 destination.

## Build gates versus activation gates

The program distinguishes **construction** from **activation**.

| Gate type | May control | Must not control |
|---|---|---|
| Build sequencing | Dependency order, staffing order, merge order, test order, and integration order | Whether an in-scope capability is eventually built in V1 |
| Security gate | Production keys, value limits, public accessibility, signing authority, and release eligibility | Development of the system, local execution, simulation, sandbox integration, or adversarial testing |
| Legal/compliance gate | Jurisdictional exposure, operator eligibility, user eligibility, product wording, provider selection, and launch configuration | Core implementation, policy-engine construction, ledger construction, contest/wagering flows in sandbox, or end-to-end testability |
| Economic gate | Mainnet value limits, custody activation, cash-in/cash-out, player-funded pools, and irreversible settlement | Testnet, deterministic simulations, mock-provider flows, reconciliation, escrow state machines, or production-grade interfaces |
| Hardware gate | Manufacturing, retail distribution, certification, and field activation | Virtual Target, OS image, firmware interfaces, kernel/GPU/transport/FS implementation, conformance testing, or reference-hardware prototypes |
| Performance gate | Promotion to a public profile or production backend | Construction, benchmarking, profiling, fallback implementation, or optimization work |

A gate can cause a feature to ship **disabled by policy in a specific jurisdiction or environment**. It cannot cause the capability to disappear from V1 engineering scope.

## Mandatory V1 blockchain and economic scope

AXIOM Chain is not a future appendix. V1 must include an operational sovereign game-native blockchain implementation, testnet and production-candidate network, wallet core, managed and self-custodial paths, digital objects, licenses, provenance, royalty distribution, marketplace settlement, prize escrow, result attestation, validator operations, indexer, explorer, recovery, incident controls, and integration with Store and Arena.

| Capability | Required V1 implementation outcome |
|---|---|
| Chain node | Runnable node software with documented state synchronization, networking, storage, telemetry, upgrade, backup, and recovery |
| Consensus | Selected and implemented consensus profile with deterministic simulation, fault testing, validator operations, and governance controls |
| State and execution | Versioned state model, transaction validation, native modules, deterministic execution boundary, migrations, and invariants |
| Wallet | Managed and self-custodial wallet flows, purpose-separated keys, trusted signing UI, recovery, transaction history, limits, and policy evaluation |
| Digital objects | Mint, transfer, burn, freeze where legally/policy permitted, rights metadata, provenance, licensing, and content-address links |
| Marketplace | Listing, offer, purchase, fee, royalty, refund, dispute, reversal where supported, and reconciliation workflows |
| Arena value | Entry funding, participant commitments, sponsor and player-funded pools, escrow, cancellation, result attestation, settlement, disputes, and audit |
| Wagering-compatible infrastructure | One-to-one and tournament stake commitments, odds-free skill-contest state, jurisdiction policy, age/identity controls, limits, exclusion, fraud detection, and complete ledger evidence |
| Token and credits | Native token and/or credit abstractions, issuance policy, balances, holds, conversions where authorized, fees, liabilities, accounting boundaries, and supply controls |
| Cash-equivalent flows | Provider adapters for deposits, withdrawals, refunds, chargebacks, holds, reserve management, sanctions/KYC/KYB checks, tax records, and reconciliation |

The legal characterization of a specific contest or value flow may vary by jurisdiction. That uncertainty must be encoded into the policy engine and operator deployment profile, not used to avoid implementing the platform capability.

## Mandatory V1 platform and game scope

The full desktop console environment, native engine, Simple/Advanced DEV continuity, AI planning and Gauntlet system, semantic project graph, native formats, Connect, Unreal Bridge, advanced renderer, audio, networking profiles, replays, social, media, Store, Profile, Wallet, Arena, cloud services, moderation, telemetry, and developer publishing flow remain V1 implementation obligations.

The requirement to prove a small-game path first remains a sequencing rule. It does not reduce the V1 destination. High-fidelity rendering, large streamed worlds, rollback and strategy networking, large-shard architecture, production services, economic systems, and first-party validation must all have coded, integrated V1 outcomes.

## Mandatory V1 PYRAMID and proprietary replacement scope

The Virtual Target, Linux-based production OS path, PLAY/DEV/NODE modes, update and recovery system, controller-first operation, secure boot architecture, firmware interfaces, physical P0/P1 reference prototypes, the P2 custom-board program, the P3 custom silicon program, kernel, GPU stack, secure transport, cryptography implementation, image/media codecs, filesystem, AXVM, distributed compute, and hardware/firmware programs are all V1 build scope.

Maturity labels may still describe **release confidence**. They no longer describe whether the team builds the capability. Experimental systems must be coded, booted or executed, tested, benchmarked, documented, and integrated behind replacement interfaces. Production may continue using a mature dependency until the AXIOM implementation passes its replacement gate, but the proprietary implementation cannot remain a paper-only future workstream.

## Requirement-class override

The repository must adopt two independent axes instead of using one maturity class to control both engineering and exposure.

| Axis | Values | Meaning |
|---|---|---|
| Build obligation | `V1-BUILD-REQUIRED` | The capability must be implemented, integrated, tested, and owned during the V1 program |
| Activation state | `LOCAL`, `TEST`, `SANDBOX`, `TESTNET`, `PILOT`, `REGION-LIMITED`, `PRODUCTION-ENABLED`, `DISABLED-BY-POLICY` | Where and for whom the completed capability may operate |
| Assurance state | `PROTOTYPE`, `INTEGRATED`, `VERIFIED`, `AUDITED`, `PRODUCTION-QUALIFIED` | The confidence and evidence achieved by the implementation |

All capabilities in the master specification are now `V1-BUILD-REQUIRED` unless Ø explicitly removes them in a later signed owner directive. Existing labels such as V1-PREVIEW, V1-EXPERIMENTAL, and V1-ARCHITECTED remain useful only as initial assurance targets and risk disclosures; they no longer authorize deferral beyond the V1 build program.

## Backlog and milestone implications

Every formerly deferred capability must have an owning workstream, architecture document, requirements, API/schema contracts, implementation epics, dependency graph, tests, threat model, operational plan, and Definition of Done. A milestone may be blocked from public launch, but its engineering tasks remain active and dependency-ordered.

The backlog must distinguish:

| Status | Interpretation |
|---|---|
| Blocked for design | An ADR or interface decision is required; research, prototypes, and tests continue |
| Blocked for activation | Implementation is complete enough for sandbox/test, but public or real-value exposure awaits an external gate |
| Blocked for production qualification | Reliability, security, performance, or operational evidence is insufficient; implementation and verification continue |
| Deferred | Permitted only by a later explicit owner directive that identifies the removed V1 obligation |

## Definition of V1 completion

V1 cannot be declared build-complete merely because the desktop shell or small-game path works. It requires executable implementations and integrated test evidence for every major domain named in the master specification, including the chain, wallet, Store, Arena, player-funded and sponsored value flows, marketplace, platform services, high-fidelity engine path, Unreal Bridge, PYRAMID software/hardware path, and proprietary replacement workstreams.

Public activation may remain selective by jurisdiction, operator, assurance level, hardware readiness, or value limit. The codebase and system design, however, must support the complete destination without requiring a later architectural restart.

## Agent instruction

CodeSpring, Traycer, Manus, Codex, Claude, and every other implementation worker must interpret phrases such as “future,” “later,” “Preview,” “Experimental,” “Architected,” “deferred,” “not a V1 requirement,” or “non-blocking” as follows:

> Preserve the risk label and activation restriction, but move the capability into mandatory V1 construction, integration, and test scope. Do not omit it, reduce it to a placeholder, or postpone its architecture and implementation to a later product version.

When the source and this directive conflict, report the conflict and follow this directive for repository planning and implementation.
