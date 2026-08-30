# AXIOM-XIII V1 Product and Shell UX Domain Specification

## 1. Executive Summary and Purpose

The **Product and Shell UX** domain represents the primary interactive layer of the AXIOM-XIII platform. AXIOM-XIII is not merely an engine, but a fully integrated environment where users can play, build, publish, own, compete, and eventually run dedicated PYRAMID hardware.

The purpose of this domain is to provide a unified, controller-first desktop console experience. It enforces the strict continuity between gaming, creation, commerce, and ownership without requiring users to switch contexts, restart applications, or understand blockchain terminology for ordinary use. The Shell is the central hub that connects the AXIOM Engine, AI, Connect, Services, Protocol, Arena, Chain, and future PYRAMID hardware.

### 1.1 Non-Negotiable Doctrine

The V1 scope is build-complete, meaning every capability described in the canonical specification is a mandatory V1 implementation requirement (`V1-BUILD-REQUIRED`). This includes the full Shell, locked seven-tab navigation, identity surfaces, DEV Simple/Advanced continuity, and controller-first UX.

The Shell must provide controller-first continuity, being entirely navigable by controller and supporting instant transition between play, social, store, wallet, and development.

A core principle is "One Project, Two Interfaces". DEV Simple (AI chat-first) and DEV Advanced (professional direct-edit) must operate on the exact same project graph, source tree, and assets. Switching between them must preserve state without any export or conversion step.

There must be clear value separation. Public player identity must be separated from private financial and verification data. Irreversible chain operations and real-value transfers must be clearly distinguished from reversible store actions.

Finally, the platform follows a protocol-first, hardware-later approach. The desktop shell must provide the complete ecosystem experience before the physical PYRAMID console is manufactured, acting as the exact software stack that PYRAMID will eventually run.

## 2. Personas and Actors

The Shell must accommodate multiple user types within the same application.

The **Player** uses GAMES, MEDIA, SOCIAL, STORE, PROFILE, and WALLET, focusing on discovery, play, and progression.

The **Chat-First Creator** uses DEV Simple, relying on AXIOM AI (Ask, Plan, Build) to construct games through natural language and media references.

The **Technical Game Developer** uses DEV Advanced, requiring direct access to the engine, code, graphs, profilers, and source control.

The **Studio Team** requires permission models, shared workspaces, audit history, branch management, and budget controls.

The **Asset/Plugin Creator** builds signed `.axpkg` packages, manages licenses, and tracks royalties through STORE and WALLET.

The **Competitive Player/Team** uses Arena ladders, tournament rosters, and prize settlement interfaces.

## 3. Domain Boundaries and Named Components

The Product and Shell UX domain interfaces with the AXIOM Engine, Services, Protocol, and Chain, but maintains strict separation of concerns.

### 3.1 Top-Level Navigation

The Shell enforces a locked, seven-tab primary navigation structure.

| Tab | Functionality |
| :--- | :--- |
| **GAMES** | Library, installation, AXIOM Originals, updates, and launch options. |
| **MEDIA** | Capture, replays, streaming, game music (ORPHEUS), and rights-checked publishing. |
| **SOCIAL** | Friends, parties, guilds, messaging, and cross-game identity. |
| **DEV** | The unified creation environment (Simple and Advanced modes). |
| **STORE** | Discovery, purchases, entitlements, asset packs, and developer publishing. |
| **PROFILE** | Public identity, achievements, competitive history, and reputation. |
| **WALLET** | Fiat, token, and asset balances, transaction history, and secure signing UI. |

A **Home** dashboard acts as the default landing state but is not a distinct tab. It aggregates active games, downloads, social presence, DEV project status, and critical alerts.

### 3.2 Named Components

The **Shell Router** manages navigation state, deep linking, and transitions between the seven tabs.

The **DEV Mode Switcher** handles the seamless transition between Simple and Advanced DEV interfaces.

The **AXIOM AI Chat Viewport (Simple Mode)** is the primary interface for chat-first creators, displaying conversation, plans, changes, and live game preview.

The **Professional Workspace (Advanced Mode)** is the modular windowing system exposing code, AXIOM Flow, materials, profilers, and Gauntlet controls.

The **Secure Signing Overlay** is a trusted UI component invoked by the WALLET or Chain domains for irreversible transactions and capability approvals.

The **Media Studio** provides integrated tools for trimming, captioning, and publishing captured clips and replays.

## 4. Canonical Entities and Stable IDs

The Shell interacts with Protocol objects using stable AXIOM identifiers, ensuring continuity across file moves and renames.

| Category | Entities |
| :--- | :--- |
| Identity | `UserIdentity`, `PublicProfile` |
| Product | `Game`, `Build`, `Package` |
| Asset | `Asset`, `DigitalObject`, `License` |
| Commerce | `Entitlement`, `Purchase` |
| Finance | `Wallet`, `Transaction` |
| Development | `Project`, `Requirement`, `Decision` |

## 5. State Machines and Transitions

### 5.1 DEV Mode Continuity

The DEV environment allows seamless transitions between Simple and Advanced modes. A user starts in DEV Simple, requests a feature, and AXIOM AI creates a plan. Upon approval, AXIOM AI builds the feature, which is then reflected in both DEV Simple and DEV Advanced. The user can toggle between the two modes at any time to inspect or modify the changes.

### 5.2 Play-to-Develop Transition

A user can seamlessly transition from playing a game to developing it. From the GAMES Library, a user launches a development build. While playing, they can invoke DEV context by selecting an entity or error. This creates a patch branch where they can make changes and run tests via Gauntlet. Once satisfied, they can return to play.

## 6. API and Capability Contracts

The Shell communicates with underlying domains via **AXIOM Connect**. Every capability call requires a typed payload including caller identity, project identity, capability scope, and consequence tier.

### 6.1 Required Connect Capabilities (Shell Context)

The Shell context utilizes specific capabilities such as `project.open`, `project.build`, and `project.test` for project management. It invokes `wallet.sign_request` to trigger the Secure Signing Overlay. For publishing, it uses `release.submit` to transition a project to the STORE sandbox. It also uses `playtest.start` and `playtest.observe` for testing.

### 6.2 Consequence Tiers and Approvals

Every AXIOM AI operation is classified into consequence tiers.

| Tier | Description | Default Behavior |
| :--- | :--- | :--- |
| **T0** | Read only (e.g., inspect scene). | Executes immediately. |
| **T1** | Reversible local edit (e.g., move object). | Executes with undo and change log. |
| **T2** | Multi-system project edit. | Plan summary plus approval or configured auto-approval. |
| **T3** | Destructive or costly. | Explicit approval and checkpoint required. |
| **T4** | External or irreversible (e.g., publish, sign chain transaction). | Strong authentication, detailed review, explicit signing. |

## 7. Data Ownership and Storage

Canonical project data is stored in Git-friendly files such as manifests, `DECISIONS.md`, `REQUIREMENTS`, and `LICENSES`. The Semantic Project Graph is a rebuildable index, not a proprietary database.

Identity and entitlements are managed by AXIOM Services. The Shell caches state but relies on Services for authority.

Wallet keys in managed mode are secured by AXIOM. Self-custodial keys are stored securely on the user's device or hardware wallet and never exposed to untrusted game UI.

## 8. Failure and Degraded Modes

The architecture ensures control plane isolation. A failure in the Social or Media services must not crash a running game or corrupt a DEV project.

In the event of a chain outage, games that do not require online ownership checks must remain playable offline. The WALLET must gracefully indicate sync delays without blocking Shell navigation.

If the primary AI provider fails, AXIOM AI must support model routing. It must fallback to an approved alternative or local model, ensuring DEV Simple remains functional.

## 9. Security, Privacy, and Legal Considerations

Secure signing is paramount. Untrusted game UI cannot obscure or replace the secure wallet confirmation overlay.

Identity separation is strictly enforced. PROFILE displays public reputation, while WALLET and Services handle KYC and legal verification.

Rights provenance is automatically checked when publishing through MEDIA or STORE, verifying game capture permissions, music rights, and imported asset licenses.

Jurisdiction awareness is built into the Shell. It respects the modular policy engine, hiding or disabling real-value features like Arena prize pools and chain operations based on regional legal configurations.

## 10. Observability and Performance

User actions in the Shell, such as a purchase, a DEV build, or a crash, are tracked across domains using correlation IDs, with sensitive data redacted.

DEV Simple interactions log task IDs, compute cost, change sets, and user approvals to manage budgets and audit AXIOM AI behavior.

The Shell must maintain 60 FPS responsiveness on reference hardware, ensuring seamless transitions between tabs even while a game is suspended in the background.

## 11. Accessibility

The Shell and DEV environments must support remappable controls for both keyboard and controller. They must provide scalable text and UI contrast controls, along with screen reader semantics. Clear focus states and error messaging are required. Speech-to-text and text-to-speech must be supported where available, which is critical for DEV Simple.

## 12. Test Pyramid and Acceptance Tests

Unit and integration tests validate Shell Router state transitions and AXIOM Connect capability payloads.

End-to-end tests verify the controller-only navigation across all seven tabs. They also verify that a user can request a feature in DEV Simple, approve the plan, switch to DEV Advanced, see the generated code, make a manual edit, and switch back to Simple without data loss. Furthermore, they verify that the Secure Signing Overlay cannot be bypassed by simulated game input.

Visual regression tests ensure UI consistency across desktop and PYRAMID Virtual Target resolutions.

## 13. V1 Definition of Done (DoD)

The Product and Shell UX domain is considered build-complete for V1 when the seven-tab navigation is implemented exactly as specified. Controller-only end-to-end navigation must pass all tests. Account switching and privacy separation between PROFILE and WALLET must pass audit. DEV Simple and Advanced must operate on the exact same project data, allowing mid-task switching with full direct-edit fidelity. AXIOM AI Ask, Plan, and Build states must enforce consequence tiers and require strong approval for publish and value actions. The Secure Signing UI must correctly intercept and display all T4 irreversible actions.

## 14. Work Packages (Dependency Order)

The implementation of the Product and Shell UX domain is broken down into sequential work packages.

| Package | Description |
| :--- | :--- |
| **WP-SHL-01** | Implement core Shell Router and locked seven-tab layout. |
| **WP-SHL-02** | Implement controller input abstraction and focus management. |
| **WP-SHL-03** | Build Home dashboard and notification aggregation. |
| **WP-SHL-04** | Implement DEV Mode Switcher and shared project state context. |
| **WP-SHL-05** | Build DEV Simple chat viewport and AXIOM Connect integration. |
| **WP-SHL-06** | Build DEV Advanced workspace windowing and direct-edit views. |
| **WP-SHL-07** | Implement Secure Signing Overlay and Wallet integration. |
| **WP-SHL-08** | Build Media Studio capture and publishing workflows. |

## 15. Open ADRs

Several architectural decision records remain open and must be resolved before major implementation.

| ADR | Description |
| :--- | :--- |
| **ADR-SHL-01** | UI shell bootstrap technology and migration path to native AXIOM UI. |
| **ADR-SHL-02** | Privacy and telemetry defaults for Shell interactions. |
| **ADR-SHL-03** | Managed wallet custody model and integration with the Secure Signing UI. |

## 16. Interfaces with Other Domains

The Shell invokes `project.build` and `playtest.start` via Connect to interface with the Engine.

DEV Simple sends user intents to the PRIME Orchestrator and receives Plans and Change Sets to interface with AI.

The Shell queries `UserIdentity` and `Entitlement` schemas to populate PROFILE and GAMES, interfacing with Protocol and Services.

The WALLET tab interfaces with the Chain domain for balances and invokes the signing overlay for transactions.

The GAMES and PROFILE tabs query Arena for matchmaking status and competitive history.

## 17. Detailed Component Specifications

### 17.1 DEV Simple Mode (Chat-First Interface)

The DEV Simple mode is designed for creators who prefer to build through natural language and media references. It is not a reduced version of the engine; rather, it is the full engine operated primarily through AXIOM AI.

The primary interaction area is the Conversation View, where the user communicates with AXIOM AI. It must support text, images, video, audio, and file uploads. A Live Game/Editor Viewport provides a real-time rendering of the game world or specific scene being edited. A Project Context Strip displays the current active project, branch, and overall status. A dedicated panel shows proposed changes from the Plan state and applied changes from the Build state. Real-time indicators display ongoing builds, Gauntlet test results, and deployment status. A visual repository holds imported assets, concept art, and reference materials. A visual timeline of all changes allows the user to easily revert to a previous state.

For every meaningful action, DEV Simple must be able to explain what changed and why, which requirements were satisfied, and the affected files, assets, and systems. It must also explain test outcomes, uncertainties or failed verifications, how to undo or manually modify the change, applicable licenses and provenance, compute or external service costs, and the impact on performance budgets.

### 17.2 DEV Advanced Mode (Professional Interface)

DEV Advanced mode is the complete, professional AXIOM environment. It exposes direct control over all engine systems while maintaining the context of AI assistance.

Advanced mode must provide dedicated workspaces for Project Management, World and Scene Editing, Entity and Component Configuration, Code Editing, AXIOM Flow (Visual Logic), Materials and Shaders, Animation and Rigging, Physics and Destruction, VFX and Audio (ORPHEUS), UI Design, Narrative and Data Management, AI Behavior Configuration, Network and Chain Integration, Database and Persistence, Profiling and Memory Analysis, Renderer and Network Debugging, Replay Analysis, Test and Gauntlet Execution, Build, Deploy, and Source Control, Package Management, and Project Policy, Provenance, and Security.

Every AI-generated system must expose its source representation in Advanced mode. Users must never be forced to regenerate a system merely to change one parameter. This includes code, AXIOM Flow graphs, AXIR, entity and component data, material graphs, shader source, animation state graphs, behavior graphs, test definitions, data schemas, and build metadata.

### 17.3 Media Studio and Publishing

The MEDIA tab provides integrated tools for capturing, editing, and publishing content.

Native capture capabilities include screenshot and video capture, replay bookmarks, and last-N-minutes capture. It provides microphone and party audio policy controls, HDR-aware capture, and performance-aware encoding. Privacy indicators and rights metadata embedding are also included.

Editing features include trimming, combining, and cropping or aspect ratio adjustments. It supports captions and overlays, replay camera selection (changing angles where deterministic replay data exists), and soundtrack selection from owned or authorized media. It also provides export and publish workflows.

Before publishing, the system must verify game capture permissions, music rights and voice or likeness consent, imported asset licenses, disclosure requirements, and region restrictions.

### 17.4 Social and Profile Systems

The SOCIAL and PROFILE tabs manage user identity, relationships, and reputation.

AXIOM distinguishes between several identity layers to protect privacy and manage permissions. These include private account identity (internal), public profile identity (chosen by the user), legal or KYC reference (for real-value operations), wallet addresses, developer or studio identity, competitive team identity, and pseudonymous identities (where permitted by policy).

The social graph supports mutual friends, follows, blocks, groups, parties, guilds or clans, developer teams, tournament rosters, project collaboration, and reputation claims. Messaging requires direct and group text, party voice, project comments, moderation and reporting tools, spam and rate limits, parental controls, encryption in transit, retention and legal policy enforcement, and safe-link and file scanning.

Reputation models may include completed transactions, creator credits, tournament conduct, moderation history, project collaboration, verified skills, and community endorsements. These models must avoid exposing sensitive personal data or functioning as opaque social-credit systems.

## 18. Semantic Project Graph Details

The Semantic Project Graph is a core architectural concept that allows AXIOM-XIII to understand a game as a system of meaningful relationships rather than a directory of unrelated files.

The graph is versioned and schema-validated. It is queryable, diffable, branch-aware, and partially loadable. It remains stable across DEV Simple and Advanced modes and is accessible through AXIOM Connect. It is capable of representing external assets and unresolved references, is protected by permissions, and is recoverable from source files and manifests.

Every project must include specific ledgers to track decisions and canon. These include `DECISIONS.md` or structured ADRs, a `CANON_LEDGER` (where narrative canon applies), a `REQUIREMENTS` register, a `MECHANICS_REGISTRY`, a `LICENSES` and provenance index, a `RISK_REGISTER`, a `CHANGELOG`, and `MIGRATIONS`. AXIOM AI-generated ideas default to a "PROPOSED" status until an authorized user explicitly changes their status.

## 19. AXIOM Connect and Capability Model

AXIOM Connect is the typed interface through which AXIOM AI, internal tools, external agents, CI systems, plugins, and services interact with the platform.

Supported interfaces include a native in-process SDK, a command-line interface (CLI), local IPC, gRPC (or equivalent typed high-performance RPC), REST (for broadly compatible service operations), WebSocket and event streams (for realtime state), MCP-compatible tool exposure (for authorized AI clients), plugin capability manifests, event subscriptions, and authenticated service-to-service APIs.

Every capability call via AXIOM Connect must include a detailed payload for permission and audit purposes. This payload includes caller identity, project identity, capability scope, requested operation, consequence tier, authorization result, input and output hashes (where practical), duration and resource use, resulting change set or transaction ID, and an audit event record. This ensures that all actions, especially those initiated by AI agents, are fully traceable and accountable.
