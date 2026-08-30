AXIOM-XIII V1

Master Production Specification for the AI-Native Game Engine, Gaming Protocol, Desktop Console Environment, Economic Network, and PYRAMID Hardware Path

Document status: Production source of truth — V1.0 Draft for implementation
Owner: Ø / AXIOM-XIII
Primary audience: AXIOM core engineering, engine, AI, blockchain, networking, security, product, design, legal, operations, and first-party game teams
Supersedes: The prior Unreal-first AXIOM-XIII meta-engine specification
Primary implementation objective: Build an independent AI-native game-development and gaming platform that can begin as a desktop console application, import Unreal projects, create and run native .axiom projects, support skill-based competition and a native blockchain economy, and later become the native software environment of PYRAMID hardware.
Confidentiality: Proprietary planning document. Distribution should be limited to authorized personnel, contractors, investors under appropriate confidentiality terms, and implementation agents operating under scoped access.

────────

Normative language

The terms MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are used as implementation requirements.

Every requirement is assigned one of four V1 maturity classes:

|Class              |Meaning                                                                                                                                                        |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**V1-PRODUCTION**  |Required to ship the first public commercial AXIOM-XIII release. It must pass security, performance, reliability, usability, and operational gates.            |
|**V1-PREVIEW**     |Included in the first public release behind an explicit preview label. It must be usable and recoverable but may have documented limits.                       |
|**V1-EXPERIMENTAL**|Included in the V1 source tree and development program, with a bootable or testable reference implementation, but it is not trusted as a production dependency.|
|**V1-ARCHITECTED** |Interfaces, data models, tests, and replacement boundaries must exist in V1 even when the complete implementation is scheduled after V1.                       |

This distinction allows AXIOM-XIII V1 to be designed around the final proprietary destination without falsely presenting immature kernel, driver, cryptography, or distributed systems work as production-secure.

────────

1. Executive Directive

AXIOM-XIII is not merely a game engine, launcher, blockchain, marketplace, social network, AI coding assistant, or console operating system. It is an integrated interactive-computing platform built around one central premise:

> **A person should be able to play, build, publish, own, compete in, earn from, and help evolve digital worlds through one AI-native environment.**

The first public form of AXIOM-XIII will be a controller-first desktop application that feels like loading a new console on a PC. Its locked primary navigation is:

GAMES · MEDIA · SOCIAL · DEV · STORE · PROFILE · WALLET

The first version must already contain the essential layers of the future protocol and console ecosystem:

• a native game runtime and engine;
• an AI-first development environment;
• a complete advanced development interface;
• a semantic project format owned by AXIOM-XIII;
• Unreal project, code, and asset migration tooling;
• identity, social, media, store, wallet, and entitlement systems;
• skill-based matchmaking, competition, tournaments, and prize-pool infrastructure;
• a custom game-native blockchain;
• first-class tokenized assets, NFTs, provenance, licensing, and creator splits;
• a model-agnostic native agent with CodeSpring-like planning, parallel workers, and Traycer-style Gauntlet loops;
• a virtual PYRAMID hardware target;
• production abstractions and experimental implementations for the future PYRAMID kernel, GPU stack, secure transport, cryptography layer, codecs, filesystem, and other proprietary replacements;
• renderer, world, animation, audio, simulation, and networking architecture capable of pursuing contemporary AAA scale and visual quality rather than being limited to lightweight indie games.

AXIOM-XIII will be accessible to creators while remaining commercially and legally controlled by its owner. The system must make it possible for creators to own the games and original content they create while AXIOM-XIII retains ownership and licensing control over the engine, runtime, platform, services, protocols, store, AI, infrastructure, brand, and proprietary technology.

The first software release precedes custom hardware. PYRAMID is the eventual purpose-built physical endpoint for an ecosystem that must already have games, developers, identities, assets, tournaments, economic activity, and network value before a proprietary console is manufactured at scale.

────────

2. Locked Product Definition

2.1 What AXIOM-XIII is

AXIOM-XIII is a combined:

1. Game engine and runtime capable of native .axiom projects.
2. AI development operating environment with chat-first and direct professional workflows.
3. Gaming shell providing a console-like user experience on desktop systems.
4. Development platform covering world building, code, logic, animation, materials, audio, physics, networking, profiling, testing, packaging, publishing, and live operations.
5. Protocol layer for identity, assets, provenance, reputation, game and creator relationships, competition, and settlement.
6. Native blockchain network designed around games, creators, licenses, prize pools, tournaments, and digital objects.
7. Distribution platform and store under AXIOM policy control.
8. Social and media network built around games, creators, teams, clips, replays, streams, soundtracks, and events.
9. Competitive platform supporting skill-based matchmaking, ranked ladders, tournaments, prize pools, spectating, replays, and anti-cheat.
10. Future console software stack for PYRAMID hardware, including operating environment, virtual hardware target, custom kernel program, and proprietary driver replacement path.

2.2 What AXIOM-XIII is not

AXIOM-XIII V1 is not:

• an Unreal plugin suite masquerading as an independent engine;
• a thin launcher around third-party games;
• a chatbot attached to an editor;
• an NFT marketplace with a game engine added later;
• a generalized gambling product;
• an opaque no-code toy that traps projects in a simplified mode;
• a permissively open-sourced engine that can be cloned, rebranded, and commercialized without AXIOM licensing obligations;
• a requirement to replace every mature dependency before the product can ship;
• a promise that the experimental PYRAMID kernel, GPU driver, TLS stack, or cryptographic implementation is production-secure in V1;
• a public modding or Forge ecosystem in V1;
• a requirement to build all first-party games simultaneously;
• a copy of Unreal, PlayStation, Xbox, Steam, Epic Games Store, Roblox, or an existing blockchain.

2.3 The core product statement

> **AXIOM-XIII is an AI-native digital-world platform where the same environment is used to play games, create commercial games, publish them, compete for value, manage programmable ownership, and eventually power a dedicated PYRAMID computer-console.**

────────

3. Non-Negotiable Principles

3.1 One project, two development interfaces

DEV Simple and DEV Advanced MUST operate on the same project graph, source tree, assets, history, tests, build system, and .axiom project. There is no export step between them.

Simple mode is not a reduced engine. It is the full engine operated primarily through AXIOM AI.

Advanced mode is not an AI-off mode. It exposes direct professional control while AXIOM AI remains context-aware.

A user MUST be able to switch between Simple and Advanced at any time without losing functionality, fidelity, history, or editability.

3.2 AI-native, not AI-uncontrolled

AI may plan, implement, generate, refactor, import, test, profile, document, and publish only through typed permissions, auditable change sets, project branches, resource budgets, and acceptance gates.

AXIOM AI MUST NOT:

• silently change project canon;
• commit secrets;
• bypass licensing restrictions;
• publish without authorized approval;
• merge unverified code;
• spend outside configured budgets;
• weaken security checks to make a test pass;
• conceal uncertainty or failed verification;
• expose AXIOM internal proprietary source to unauthorized creator contexts.

3.3 Protocol-first, hardware-later

The AXIOM account, identity, store, wallet, chain, Arena, developer environment, and runtime must provide value on ordinary computers before PYRAMID hardware exists.

PYRAMID must eventually become the best native endpoint for AXIOM, not the prerequisite for AXIOM’s existence.

3.4 Creators own their original games; AXIOM owns AXIOM

AXIOM-XIII’s licensing system MUST clearly separate:

• creator-owned original content and game-specific code;
• AXIOM-owned engine, runtime, APIs, tools, AI systems, services, protocols, store, network, and proprietary source;
• third-party content with separate licenses;
• community or collaborative assets with explicit provenance and split terms.

3.5 Accessible does not mean uncontrollable

AXIOM may provide broad access, source visibility, free tiers, public SDKs, documentation, and creator-friendly economics while retaining:

• ownership of the technology;
• license enforcement rights;
• store and publishing policies;
• service and protocol terms;
• trademark control;
• commercial royalty or subscription rights;
• the right to protect proprietary internal systems;
• control of official builds, signing, discovery, tournaments, and first-party services.

3.6 Proprietary destination, staged replacement

Every major external dependency that AXIOM may eventually replace MUST sit behind an AXIOM-owned abstraction from V1.

Where strategic value justifies replacement, V1 MUST include an experimental AXIOM implementation or an explicit research program with tests and conformance targets.

Production reliability takes priority over performing ownership theatrically. Replacing a mature dependency is considered complete only when the AXIOM alternative demonstrably meets security, correctness, compatibility, and performance requirements.

3.7 AAA-scale destination

The renderer, world system, animation stack, asset pipeline, networking, editor, and runtime must be architected for:

• large authored fantasy worlds;
• long sight lines and dense geometry;
• photorealistic environments and camera behavior;
• cinematic characters;
• modern dynamic lighting;
• large creatures and destruction;
• high-fidelity materials and VFX;
• 30/60/120 frame-per-second performance profiles;
• desktop and future fixed-console optimization;
• scalable quality levels for less powerful hardware.

The implementation may mature incrementally, but no foundational decision may permanently cap AXIOM at mobile, browser, low-poly, or small-scene use cases.

3.8 Game mechanics remain original to each game

AXIOM provides systems and primitives. Each first-party game must define its own signature mechanics, terminology, audiovisual identity, progression, interaction patterns, and expression.

AXIOM’s Mechanics Registry and Originality Firewall must document inspirations, extracted design goals, original implementation, terminology, differentiators, patent-review triggers, and prohibited imitation.

3.9 Security and verifiability are architecture

Wallets, prize pools, digital ownership, remote code generation, plugins, marketplaces, player economies, and custom engine code create a large attack surface. Security cannot be added after the platform becomes economically valuable.

All production systems require:

• least privilege;
• signed artifacts;
• reproducible builds where practical;
• provenance and SBOMs;
• secrets isolation;
• sandboxing;
• server authority or cryptographic attestation where appropriate;
• audit logs;
• abuse and fraud controls;
• independent security review before high-value operation.

3.10 Global architecture, jurisdiction-aware exposure

AXIOM-XIII should not be architecturally reduced to the rules of one country. It must support multiple operators, legal entities, payment rails, deployment regions, and policy configurations.

However, Internet distribution or incorporation in a permissive jurisdiction does not automatically eliminate obligations in user, operator, marketing, server, or payment locations. Features must be controlled by a modular policy engine so the protocol can remain broad while particular frontends expose appropriate functionality.

────────

4. V1 Product Maturity Model

The phrase AXIOM-XIII V1 describes one coordinated release family, not one single binary becoming perfect at once.

4.1 V1 release stages

|Stage                   |Purpose                                                                                                                            |Exit condition                                                                                              |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
|**V1 Foundation**       |Establish repository, architecture, project schemas, shell, runtime skeleton, AI planning, and automated build/test infrastructure.|A native `.axiom` project can be created, built, run, versioned, and inspected.                             |
|**V1 Developer Preview**|Allow invited creators to build small complete games through Simple and Advanced mode.                                             |External developers can complete documented sample projects without core-team intervention.                 |
|**V1 Network Alpha**    |Add identity, social, store sandbox, wallet sandbox, Arena sandbox, and AXIOM Chain test network.                                  |End-to-end test purchases, ownership, tournament settlement, and multiplayer work with fake or capped value.|
|**V1 Public Beta**      |Open the desktop console environment, store submissions, and economic systems under controlled limits.                             |Security, anti-cheat, support, recovery, moderation, and operations pass beta gates.                        |
|**V1 Production**       |Commercial release of the software ecosystem.                                                                                      |All V1-PRODUCTION acceptance criteria in this document pass.                                                |

4.2 V1 scope classification

V1-PRODUCTION

• desktop AXIOM shell;
• locked seven-tab navigation;
• GAMES library and installation;
• MEDIA capture, replay, and basic publishing;
• SOCIAL friends, parties, groups, presence, messaging, and invitations;
• DEV Simple and Advanced;
• AXIOM AI Ask, Plan, and Build modes;
• native .axiom projects;
• project graph, history, branching, undo, change sets, tests, and packaging;
• native runtime for at least Windows and Linux;
• renderer capable of high-fidelity real-time 3D and scalable 2D/2.5D;
• world, entity, component, logic, input, UI, animation, physics, audio, networking, save, and package foundations;
• Unreal project analyzer and partial converter with explicit compatibility reporting;
• STORE submission, purchase, entitlement, update, refund workflow, and developer payout ledger;
• PROFILE identity and reputation foundations;
• WALLET managed-custody mode, self-custody export path, balances, transaction history, creator revenue, and prize history;
• AXIOM Chain production network with a narrow audited native module set;
• AXIOM Arena matchmaking, ranking, tournaments, replays, anti-cheat, and sponsor-funded prize pools;
• NFT/digital-object minting, licensing, creator splits, marketplace listing, transfer, and provenance;
• security, moderation, support, observability, backup, disaster recovery, and incident response;
• PYRAMID Virtual Target and controller-first console UX profile.

V1-PREVIEW

• general third-party smart contracts;
• player-funded entry-fee tournaments;
• high-value non-custodial settlement;
• distributed build compute from user devices;
• large-scale persistent worlds above the validated V1 concurrency envelope;
• one-click conversion of complex Unreal Blueprints and plugins;
• AI-generated cinematic-quality character, animation, and voice pipelines without human correction;
• public creator asset marketplace beyond curated categories;
• cross-chain asset bridges;
• advanced cloud streaming.

V1-EXPERIMENTAL

• PYRAMID Kernel;
• AXIOM GPU kernel/user-mode driver stack;
• AXIOM Secure Transport implementation;
• AXIOM cryptographic implementation library;
• AXIOM Image/codecs;
• AXIOM filesystem;
• AXIOM hypervisor/secure sandbox runtime;
• AXIOM custom shader compiler backend;
• custom deterministic physics core replacing the production reference implementation;
• AXVM as a fully independent bytecode/runtime backend if the production runtime initially uses native or WebAssembly execution.

V1-ARCHITECTED

• physical PYRAMID hardware manufacturing;
• PYRAMID secure boot and device attestation;
• custom motherboard or silicon;
• console certification program;
• 10,000-plus-player shard deployment;
• global decentralized validator expansion;
• public Forge/modding ecosystem;
• full replacement of all operating-system and graphics dependencies;
• first-party game exclusivity and external-store strategy.

────────

5. User Types

AXIOM-XIII must serve different users without forcing them into separate products.

5.1 Player

Uses GAMES, MEDIA, SOCIAL, STORE, PROFILE, and WALLET. May never open DEV.

5.2 Chat-first creator

Uses DEV Simple, provides text/images/audio/video/documents/repositories, approves plans, tests generated builds, and publishes without manually editing engine internals.

5.3 Technical game developer

Uses DEV Advanced, source control, code, graphs, assets, profilers, debuggers, network tools, chain tools, build targets, and AXIOM AI.

5.4 Studio team

Uses permissions, branches, reviews, shared workspaces, roles, audit history, budgets, build farms, private packages, project policy, and live operations.

5.5 Asset or plugin creator

Builds signed .axpkg packages, receives license and provenance metadata, publishes through STORE, and may receive programmatic royalties.

5.6 Competitive player or team

Uses Arena ladders, tournaments, match history, replays, anti-cheat, team management, eligibility, and prize settlement.

5.7 Validator, node, or infrastructure operator

Runs authorized AXIOM services, chain validators, storage, relays, build capacity, or future PYRAMID node functions under a specific node license and policy profile.

5.8 AXIOM internal engineer

Receives access to restricted engine, AI, anti-cheat, security, chain, store, ranking, kernel, and hardware repositories according to least privilege.

────────

6. Top-Level Product Shell

6.1 Locked navigation

The top-level navigation MUST be exactly:

GAMES · MEDIA · SOCIAL · DEV · STORE · PROFILE · WALLET

There is no separate CREATE tab in V1. All game creation belongs under DEV.

A Home dashboard may exist as the default landing state, but it is not an eighth functional tab. The logo or system button returns to Home.

6.2 Console-first behavior

The shell MUST:

• be completely navigable by controller;
• support keyboard and mouse without switching applications;
• support high-DPI televisions and monitors;
• allow instant transition from play to social, media, store, wallet, or DEV;
• support suspend/resume of compatible games;
• preserve downloads and updates in the background;
• separate public player identity from private financial and verification data;
• provide clear indicators when real value, blockchain signing, publishing, or irreversible operations are involved;
• use the same design language on desktop and future PYRAMID hardware.

6.3 Home dashboard

Home SHOULD surface:

• continue playing;
• installed and recently played games;
• active downloads and updates;
• friends and parties;
• Arena events;
• creator project status;
• build/Gauntlet status;
• media drafts;
• store discovery;
• wallet alerts that require action;
• system health and security notices.

Home MUST NOT expose private wallet balances or legal identity by default on a shared screen.

6.4 GAMES

GAMES provides:

• owned and installed games;
• AXIOM Originals;
• local, cloud, and future PYRAMID-compatible builds;
• updates, DLC, and content packs;
• achievements and progression;
• Arena eligibility and events;
• multiplayer invitations;
• game-specific media and communities;
• version channels where the developer permits them;
• compatibility, performance, accessibility, controller, and policy information;
• launch options for standard, benchmark, safe, offline, developer, or tournament modes where authorized.

6.5 MEDIA

MEDIA provides:

• screenshots;
• clips;
• replays;
• live streams;
• tournament broadcasts;
• machinima and in-engine cinematics;
• soundtracks and music releases;
• creator channels;
• editing, trimming, captions, metadata, rights, and publishing;
• game-aware replay playback that can change camera angles where deterministic replay data exists;
• content provenance and rights status.

V1 does not need to become a complete general-purpose video platform, but capture, replay, game music, sharing, and broadcast must be native rather than outsourced afterthoughts.

6.6 SOCIAL

SOCIAL provides:

• friends and follows;
• parties and voice/text chat;
• guilds, clans, development teams, and creator groups;
• presence and activity;
• invitations to games, projects, tests, tournaments, or collaborative sessions;
• moderation, blocking, reporting, parental controls, and privacy;
• reputation and trust indicators that do not reveal protected personal data;
• cross-game identity under user control.

6.7 DEV

DEV contains all creation and professional development functions. It has two primary modes:

• SIMPLE — chat-first AXIOM AI interface;
• ADVANCED — direct professional engine and platform interface.

Both operate on the same .axiom project and semantic project graph.

6.8 STORE

STORE provides:

• games;
• DLC;
• subscriptions;
• asset packs;
• plugins;
• templates;
• developer tools;
• sound, music, models, animation, code, logic, materials, and other licensed resources;
• tokenized and non-tokenized items;
• creator content categories approved for V1;
• discovery, curation, search, reviews, refunds, wishlists, gifting, and regional pricing;
• developer dashboards and payouts through DEV or a linked web console.

AXIOM controls official store policies, acceptance, ranking, commerce, refunds, content standards, technical requirements, chain integration rules, and enforcement.

6.9 PROFILE

PROFILE provides:

• chosen public identity;
• avatar and presentation;
• games and achievements;
• competitive history;
• creations and credits;
• teams and affiliations;
• reputation;
• privacy settings;
• account and device security;
• linked identities where permitted;
• creator and developer credentials;
• optional verified status without exposing legal details.

6.10 WALLET

WALLET provides:

• fiat, token, reward, prize, creator, and royalty balances as supported;
• owned tokenized assets and NFTs;
• normal non-tokenized entitlements;
• transaction and settlement history;
• payout methods;
• managed and self-custodial modes;
• signing review;
• spending and transfer controls;
• recovery and backup;
• tax/export records where applicable;
• clear separation of reversible store actions from irreversible chain operations.

WALLET MUST never require users to understand blockchain terminology to buy and play an ordinary game.

────────

7. DEV: One Engine, Two Interfaces

7.1 Shared project truth

Simple and Advanced MUST share:

• the same project files;
• the same semantic graph;
• the same assets;
• the same code and logic;
• the same tests;
• the same Git history;
• the same dependencies and lockfile;
• the same build targets;
• the same project permissions;
• the same provenance and licensing data;
• the same performance budgets;
• the same release and store metadata.

No feature may be created in Simple mode as an opaque artifact that cannot be inspected, edited, diffed, tested, or maintained in Advanced mode.

7.2 Mode switching

The DEV header MUST expose a persistent:

SIMPLE | ADVANCED

switch.

Switching modes MUST:

• preserve editor selection and project context where possible;
• open the Advanced representation of the system discussed in Simple mode;
• allow Simple mode to explain manual changes made in Advanced mode;
• surface conflicts when AI assumptions were invalidated by manual edits;
• never duplicate or convert the project;
• remain available during the entire project lifecycle.

7.3 Ask, Plan, Build

AXIOM AI has three explicit action states:

ASK

Read-only project analysis. It may explain, inspect, search, compare, estimate, or diagnose. It MUST NOT modify project state.

PLAN

Creates a proposed implementation graph, file and asset impact, dependencies, risks, tests, estimated compute/cost, branch strategy, migration concerns, and acceptance criteria. It MUST NOT implement unless the user authorizes Build.

BUILD

Executes an approved plan through scoped agents, branches, change sets, tests, and Gauntlet gates. Build may be configured for automatic approval of low-risk reversible operations but must require explicit approval for high-impact actions.

7.4 Consequence tiers

Every AXIOM AI operation is classified:

|Tier                              |Examples                                                                          |Default behavior                                         |
|----------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------|
|**T0 — Read only**                |Explain code, inspect scene, analyze performance.                                 |Execute immediately.                                     |
|**T1 — Reversible local edit**    |Change a material value, move an object, edit text.                               |Execute with undo and change log.                        |
|**T2 — Multi-system project edit**|Add inventory, modify networking, import a package.                               |Plan summary plus approval or configured auto-approval.  |
|**T3 — Destructive or costly**    |Delete assets, migrate schemas, run large generation, incur external cost.        |Explicit approval and checkpoint required.               |
|**T4 — External or irreversible** |Publish, transfer value, sign chain transaction, deploy production, modify access.|Strong authentication, detailed review, explicit signing.|

────────

8. DEV Simple Mode

8.1 Product goal

Simple mode must allow a nontechnical creator to build a serious commercial game through conversation without making the resulting project less real, less maintainable, or less powerful than a manually built project.

The core interface is:

• AXIOM AI conversation;
• live game/editor viewport;
• project context strip;
• plans and change sets;
• test/build status;
• asset and reference tray;
• history and rollback;
• Simple/Advanced switch.

8.2 Supported input

Simple mode MUST accept:

• text;
• images and concept art;
• video and gameplay references;
• audio, music, stems, MIDI, and voice references;
• design documents and rulebooks;
• spreadsheets and structured data;
• 3D models, textures, animation, fonts, and packages;
• repositories and source archives;
• Unreal projects and supported engine projects;
• existing .axiom projects;
• sketches and annotated screenshots;
• test recordings and bug reproductions.

Every imported item receives provenance, license status, content hash, project relationship, and permitted-use metadata.

8.3 Chat-first does not mean text-only

The creator may point, select, paint a mask, sketch a path, scrub a timeline, upload a reference, speak, or manipulate the viewport while talking to AXIOM AI.

Example:

> “Keep this ruin exactly where it is. Expand the arena approximately thirty percent toward the eastern cliff, preserve the sightline to the moon, move minor enemies proportionally, rebuild navigation, and verify the boss cannot leave the playable boundary.”

AXIOM AI must resolve the selected objects, turn the request into constraints, produce a change plan, execute in a branch, and run spatial, navigation, gameplay, and performance tests.

8.4 Simple mode panels

Simple mode SHOULD expose only the most important surfaces by default:

• Conversation;
• Preview;
• Plan;
• Changes;
• Test;
• Build;
• Assets;
• History.

Power panels may be revealed progressively, but the user must never need to leave Simple mode merely because a request spans multiple systems.

8.5 Explainability

For every meaningful build, AXIOM AI must be able to answer:

• what changed;
• why it changed;
• which requirements it satisfies;
• which files, assets, schemas, and systems were affected;
• what tests passed or failed;
• what remains uncertain;
• how to undo or modify it;
• what license/provenance applies;
• what it cost in compute or external services;
• whether performance budgets changed.

────────

9. DEV Advanced Mode

Advanced mode is the complete AXIOM professional environment.

9.1 Primary workspaces

Advanced mode MUST provide:

• Project;
• World;
• Scene;
• Entity;
• Component;
• Code;
• AXIOM Flow/logic;
• Materials;
• Shaders;
• Animation;
• Rigging;
• Physics;
• Destruction;
• VFX;
• Audio;
• UI;
• Narrative/data;
• AI behavior;
• Network;
• Chain;
• Database/persistence;
• Profiler;
• Memory;
• Renderer debugger;
• Network debugger;
• Replay;
• Test;
• Gauntlet;
• Build;
• Deploy;
• Source control;
• Packages;
• Project policy;
• Provenance;
• Security.

9.2 AXIOM AI remains active

Advanced mode MUST retain:

• context-aware chat;
• inline code and graph assistance;
• architecture review;
• test generation;
• profiler interpretation;
• refactoring;
• shader and material generation;
• asset analysis;
• multiplayer and chain analysis;
• release review;
• provenance and license checks.

The user may restrict AXIOM AI to read-only mode or a selected directory/system.

9.3 Direct edit fidelity

Every AI-generated system must expose its source representation:

• code;
• AXIOM Flow graph;
• AXIR;
• entity/component data;
• material graph;
• shader source or graph;
• animation state graph;
• behavior graph;
• test definitions;
• data schemas;
• package and build metadata.

Advanced users must never be forced to regenerate a system merely to change one parameter or behavior.

────────

10. Experience Continuity

10.1 Play-to-develop transition

Authorized users SHOULD be able to:

1. launch a development build from GAMES;
2. reproduce an issue;
3. invoke DEV with the current world, entity, replay frame, or error selected;
4. inspect or ask AXIOM AI about the problem;
5. create a branch and patch;
6. run tests;
7. return to play.

10.2 Development-to-publish transition

A project moves through:

```text
IDEA → SPECIFICATION → PROJECT → BUILD → GAUNTLET → REVIEW → PACKAGE → STORE SANDBOX → CERTIFICATION → RELEASE
```

The same AXIOM environment manages every state.

10.3 Future PYRAMID continuity

The desktop shell, controller navigation, account, library, wallet, projects, build targets, and store must transfer to PYRAMID without a conceptual redesign. PYRAMID should boot directly into the AXIOM environment.

11. AXIOM-XIII System Architecture

11.1 High-level topology

```text
                           AXIOM-XIII
                                │
        ┌───────────────────────┼────────────────────────┐
        │                       │                        │
   AXIOM SHELL             AXIOM ENGINE             AXIOM AI
 Games/Media/Social        Runtime/Editor            PRIME Orchestrator
 Dev/Store/Profile         Renderer/World            Parallel Agents
 Wallet                    Physics/Audio             Gauntlet
        │                       │                        │
        ├────────────── AXIOM CONNECT ──────────────────┤
        │            Typed APIs, Events, SDKs            │
        │                       │                        │
   AXIOM SERVICES          AXIOM PROTOCOL          AXIOM CHAIN
 Identity/Store            Data Schemas            Ownership
 Social/Media              Project/Asset IDs       Provenance
 Cloud/Build               Entitlements            Tournaments
 Matchmaking               Reputation              Settlement
        │                       │                        │
        └───────────────────────┼────────────────────────┘
                                │
                     PYRAMID VIRTUAL TARGET
                                │
                  PYRAMID OS / KERNEL / HARDWARE
```

11.2 Architectural domains

AXIOM-XIII is divided into independently versioned domains:

1. Shell — controller-first desktop/console experience.
2. Engine — native runtime, editor, world, rendering, simulation, audio, physics, animation, UI, and packaging.
3. AI — intent compilation, project understanding, planning, parallel execution, verification, and memory.
4. Connect — typed tool, service, agent, plugin, and automation interfaces.
5. Protocol — stable identifiers, schemas, events, licenses, identity, assets, game objects, and economic semantics.
6. Services — account, social, media, store, cloud, matchmaking, live operations, build, and telemetry.
7. Arena — ranked competition, tournaments, replays, anti-cheat, prize pools, and adjudication.
8. Chain — custom consensus, ledger, digital objects, licenses, royalties, escrow, and settlement.
9. Pyramid — virtual target, operating environment, experimental kernel, driver program, and physical hardware path.
10. Bridge — import, analysis, translation, and export for Unreal and future external tools.

Each domain MUST expose explicit APIs and must not access another domain’s internal storage directly.

11.3 Control planes and data planes

AXIOM separates:

• development control plane — project plans, agent actions, builds, permissions, branches, tests;
• game runtime data plane — frames, simulation, rendering, input, audio, gameplay networking;
• platform control plane — accounts, store, entitlements, policies, releases, moderation;
• economic control plane — wallet, signing, settlements, royalties, prizes;
• chain data plane — consensus, blocks, state transitions, proofs;
• telemetry plane — metrics, traces, logs, crashes, replays, audits;
• security plane — identity, keys, secrets, code signing, attestation, policy enforcement.

High-value failures must not cascade across planes. A social service outage must not corrupt a project. A chain outage must not prevent offline play for games that do not require online ownership checks. A failed AI provider must not make existing projects inaccessible.

11.4 Model and cloud independence

AXIOM-XIII MUST support:

• local models;
• AXIOM-hosted models;
• approved external model providers;
• user-supplied model endpoints where policy permits;
• multiple cloud providers;
• self-hosted services;
• on-premise enterprise deployment;
• future PYRAMID-distributed compute.

No one model provider, cloud, app store, payment processor, or chain bridge may be an irreplaceable dependency.

────────

12. AXIOM AI

12.1 User-facing identity and internal structure

The user-facing system is called AXIOM AI.

Its internal director is PRIME. PRIME is not a single fixed model. It is an orchestration service that uses policies, context, capability routing, planning, cost controls, and specialized agents.

```text
USER INTENT
    │
    ▼
AXIOM AI / PRIME
    │
    ├── Intent Compiler
    ├── Requirement Extractor
    ├── Context Graph
    ├── Planner
    ├── Model Router
    ├── Capability Broker
    ├── Parallel Agent Scheduler
    ├── Integrator
    ├── Gauntlet Controller
    ├── Approval Manager
    └── Memory / Archivist
```

12.2 Design requirements

AXIOM AI MUST be:

• model-agnostic;
• project-aware;
• multimodal;
• permissioned;
• branch-aware;
• cost-aware;
• deterministic where a deterministic operation is required;
• able to use local or remote compute;
• auditable;
• reversible;
• test-driven;
• licensing-aware;
• security-aware;
• able to operate in Simple and Advanced mode;
• able to continue a project across sessions without losing approved decisions.

12.3 Intent Compiler

The Intent Compiler converts natural language and multimodal references into structured intent.

It MUST extract:

• goal;
• affected systems;
• explicit constraints;
• inferred constraints marked as assumptions;
• desired quality;
• target platform;
• performance expectations;
• network requirements;
• security classification;
• licensing implications;
• acceptance criteria;
• open questions that genuinely block execution;
• reversible versus irreversible actions;
• estimated compute, time, and cost.

It MUST distinguish user statements such as:

• “must”;
• “should”;
• “could”;
• “do not”;
• “working title”;
• “canon”;
• “proposed”;
• “reference only.”

12.4 Requirement-first planning

AXIOM AI internalizes the planning discipline the user values from CodeSpring:

1. Resolve the goal.
2. Read the project and relevant specification.
3. Extract constraints.
4. Define acceptance tests before implementation.
5. Decompose work into dependency-aware tasks.
6. Assign tasks to appropriate agents.
7. Create branches/worktrees or isolated change sets.
8. Implement in parallel only where boundaries are safe.
9. Integrate.
10. Run the Gauntlet.
11. Diagnose failures.
12. Repeat within configured budget.
13. Present evidence, not confidence theater.

12.5 Parallel agent system

AXIOM AI supports a capability-based agent registry. Named agents represent stable roles; individual model providers remain replaceable.

PRIME — Director

Owns intent, budget, permissions, plan graph, user communication, escalation, and final release of a change set to review.

ARCHITECT — System design

Owns boundaries, interfaces, dependency direction, ADRs, schema impact, migration strategy, and architectural consistency.

PLANNER — Delivery decomposition

Produces tasks, dependencies, milestones, acceptance criteria, test plans, ownership, and execution order.

BUILDER — Code and system implementation

Implements runtime, tools, services, tests, and integrations within its assigned scope.

ATLAS — World and level systems

Builds terrain, world graphs, streaming cells, encounters, navigation, procedural layouts, and spatial validation.

FORGE — Asset generation and processing

Creates or processes models, textures, materials, VFX, UI, prefabs, collisions, LOD/cluster data, and asset metadata. The name describes an internal production agent and does not imply public modding in V1.

MOTION — Rigging and animation

Handles rigs, retargeting, state graphs, motion matching data, IK, animation generation, deformation, and animation validation.

MAESTRO — Audio and music

Handles adaptive music, audio graphs, spatialization, mixing, MIDI, VST-compatible workflows, sound design, and loudness/performance validation.

NETWORK — Multiplayer and services

Owns replication, transport, sessions, matchmaking integration, rollback, dedicated servers, interest management, replays, and network tests.

CHAIN — Blockchain and wallet

Owns chain modules, transactions, signing, digital objects, marketplace state, prize escrow, royalties, and economic invariants.

SENTINEL — Adversarial security and QA

Attempts to break assumptions, exploit interfaces, fuzz inputs, attack permissions, challenge threat models, and reject unsafe changes.

PLAYER — Automated playtesting

Runs scripted, learned, randomized, and adversarial play sessions, collects telemetry, detects soft locks, balance outliers, navigation failures, and usability problems.

PERF — Performance engineering

Profiles CPU, GPU, memory, I/O, network, shader compilation, load times, and server costs; enforces budgets.

REVIEWER — Specification conformity

Compares implementation to approved requirements, canon, accessibility, localization, licensing, and acceptance criteria.

INTEGRATOR — Merge and conflict resolution

Validates parallel change compatibility, performs semantic merges, runs integration tests, and refuses unsafe combinations.

ARCHIVIST — Durable memory and provenance

Updates the project graph, decision ledger, rationale, documentation, changelog, and knowledge index after accepted changes.

RELEASE — Packaging and deployment

Builds signed artifacts, release notes, manifests, SBOMs, store packages, server images, and rollback plans.

12.6 Agent isolation

Agents MUST operate in scoped sandboxes with:

• explicit repository paths;
• time and compute budgets;
• network permissions;
• secrets access policies;
• tool allowlists;
• output size limits;
• branch/worktree isolation;
• package installation restrictions;
• artifact scanning;
• audit logs.

No agent may directly write to production, main, chain keys, signing keys, user wallets, or store release state.

12.7 Model Router

The Model Router chooses models based on:

• capability benchmark history;
• task type;
• context length;
• privacy classification;
• cost ceiling;
• latency requirement;
• local hardware;
• tool support;
• licensing and data-use policy;
• deterministic output need;
• prior success on the project.

The router MUST support fallback and quorum strategies. High-risk architectural or security work MAY require independent proposals from multiple models plus deterministic verification.

12.8 Memory hierarchy

AXIOM AI uses distinct memory layers:

1. Session memory — current conversation and working state.
2. Project memory — source, assets, tests, graph, decisions, issues, performance history.
3. Canon memory — approved fictional and product facts protected from silent modification.
4. Organization memory — coding standards, security rules, licenses, reusable packages, platform policy.
5. Private user memory — user preferences and authorized context, isolated from public project output.
6. Ephemeral agent scratch — temporary reasoning and intermediate artifacts deleted or archived according to policy.

12.9 Human control

The user or project owner can configure:

• automatic versus manual approval by consequence tier;
• model/provider allowlists;
• maximum spending;
• maximum iteration count;
• private/local-only mode;
• no-network mode;
• branch strategy;
• protected files and systems;
• required reviewers;
• security and legal gates;
• whether generated assets may use external services;
• whether project data may be retained by a provider.

────────

13. The Gauntlet

13.1 Definition

The Gauntlet is AXIOM-XIII’s automated verification and improvement loop. It is inspired by the disciplined iterative outcome the user values in Traycer-style workflows, but it is an original AXIOM implementation.

```text
PLAN
  ↓
IMPLEMENT
  ↓
BUILD
  ↓
STATIC ANALYSIS
  ↓
UNIT / PROPERTY / FUZZ TESTS
  ↓
INTEGRATION TESTS
  ↓
GAMEPLAY / VISUAL / AUDIO TESTS
  ↓
NETWORK / CHAIN / SECURITY TESTS
  ↓
PERFORMANCE / ACCESSIBILITY / LICENSE TESTS
  ↓
PASS? ────── NO ──► ROOT CAUSE ─► PATCH PLAN ─► IMPLEMENT ↺
  │
 YES
  ↓
EVIDENCE PACKAGE
  ↓
APPROVAL / MERGE
```

13.2 Gauntlet stages

The Gauntlet MUST support:

• formatting and linting;
• compiler checks;
• dependency and license scans;
• static analysis;
• unit tests;
• property-based tests;
• fuzzing;
• schema migration tests;
• asset validation;
• shader compilation across target profiles;
• material and rendering comparison;
• animation and skeleton validation;
• audio graph validation;
• deterministic simulation checks;
• gameplay automation;
• AI navigation and behavior tests;
• multiplayer latency, loss, reorder, duplication, and disconnect tests;
• dedicated server soak tests;
• rollback consistency tests;
• chain state transition tests;
• economic invariant tests;
• wallet signing and recovery tests;
• anti-cheat tests;
• security scans and adversarial probes;
• accessibility checks;
• localization completeness;
• performance budgets;
• package and installation tests;
• update and rollback tests;
• crash recovery;
• store certification checks.

13.3 Failure discipline

When a Gauntlet stage fails, AXIOM AI MUST:

1. preserve evidence;
2. classify the failure;
3. identify likely root causes;
4. distinguish test defect from product defect;
5. avoid weakening the test without justification;
6. generate a patch plan;
7. re-run the smallest useful test set;
8. re-run the complete affected gate before approval;
9. stop and escalate when the iteration or cost budget is exhausted.

13.4 Evidence package

Every accepted Build produces:

• requirement-to-change traceability;
• changed file/asset list;
• test results;
• performance delta;
• security and license findings;
• generated asset provenance;
• unresolved warnings;
• rollback instructions;
• build identifiers;
• reviewer approvals;
• AI/model/tool attribution where policy requires it.

13.5 Continuous adversarial simulation

AXIOM’s own platform Gauntlet MUST continuously create hostile conditions:

• malformed projects and packages;
• corrupt assets and saves;
• packet loss, lag, clock skew, disconnects, and replay attacks;
• double-spend and chain reorganization attempts;
• invalid match attestations;
• botting, collusion, smurfing, and input manipulation;
• shader and driver crashes;
• filesystem faults;
• memory pressure;
• malicious plugins;
• prompt injection in project files and assets;
• secret-exfiltration attempts;
• denial-of-service patterns;
• compromised dependency simulations;
• restore-from-backup drills.

────────

14. Semantic Project Graph

14.1 Purpose

AXIOM-XIII must understand a game as a system of meaningful relationships rather than a directory of unrelated files.

The Semantic Project Graph represents:

• project identity;
• requirements;
• canon;
• worlds and scenes;
• entities and components;
• logic and code;
• assets;
• materials and shaders;
• animation and rigs;
• audio and music;
• UI;
• gameplay systems;
• network authority;
• persistence;
• chain/economic relationships;
• tests;
• performance budgets;
• build targets;
• dependencies;
• licenses and provenance;
• history and decisions.

14.2 Graph properties

The graph MUST be:

• versioned;
• schema-validated;
• queryable;
• diffable;
• branch-aware;
• partially loadable;
• stable across Simple/Advanced;
• accessible through AXIOM Connect;
• capable of representing external assets and unresolved references;
• protected by permissions;
• recoverable from source files and manifests.

The graph is not a proprietary database that makes projects unreadable without a server. Canonical project data remains in files suitable for Git and backup; the graph may use indexes/caches that can be rebuilt.

14.3 Stable identifiers

Every project, world, scene, entity, component, asset, package, test, requirement, decision, game build, store item, digital object, and release receives a stable AXIOM identifier.

Identifiers MUST remain stable across file moves and renames. Human-readable names are labels, not identity.

14.4 Decision and canon ledgers

Projects MUST include:

• DECISIONS.md or structured ADRs;
• CANON_LEDGER where narrative canon applies;
• REQUIREMENTS register;
• MECHANICS_REGISTRY;
• LICENSES and provenance index;
• RISK_REGISTER;
• CHANGELOG;
• MIGRATIONS.

AXIOM AI-generated ideas default to PROPOSED until an authorized user changes their status.

────────

15. Native AXIOM Project and Asset Formats

15.1 .axiom project

The native project extension is provisionally:

.axiom

A .axiom project is not one opaque binary. It is a text-readable manifest plus an inspectable project directory.

Example:

```text
Yokai/
├── Yokai.axiom
├── Project/
│   ├── project.toml
│   ├── dependencies.lock
│   ├── permissions.toml
│   ├── performance.toml
│   └── build.targets.toml
├── Specs/
├── Source/
├── Worlds/
├── Scenes/
├── Entities/
├── Components/
├── Logic/
├── Materials/
├── Shaders/
├── Animation/
├── Audio/
├── UI/
├── Assets/
├── Data/
├── Network/
├── Chain/
├── Tests/
├── Tools/
├── Plugins/
├── Generated/
├── Saved/
└── Build/
```

Generated caches and local saved state must be separable from source-controlled project truth.

15.2 Native format family

Provisional extensions:

|Extension     |Purpose                                         |
|--------------|------------------------------------------------|
|`.axiom`      |Project manifest/entry point                    |
|`.axworld`    |World graph and streaming topology              |
|`.axscene`    |Scene content                                   |
|`.axentity`   |Entity/prefab definition                        |
|`.axcomponent`|Component schema/configuration                  |
|`.axflow`     |AXIOM Flow logic graph                          |
|`.axir`       |AXIOM intermediate representation               |
|`.axmat`      |Material graph                                  |
|`.axshader`   |Shader source/graph metadata                    |
|`.axanim`     |Animation graph/clip metadata                   |
|`.axrig`      |Rig and skeleton data                           |
|`.axfx`       |VFX graph                                       |
|`.axaudio`    |Audio graph/event definition                    |
|`.axui`       |UI document/graph                               |
|`.axdata`     |Structured game data                            |
|`.axnet`      |Replication/network profile                     |
|`.axchain`    |Chain/economic module metadata                  |
|`.axtest`     |Test definition                                 |
|`.axpkg`      |Signed distributable package/plugin/asset bundle|
|`.axbuild`    |Build manifest                                  |
|`.axreplay`   |Deterministic or authoritative replay container |
|`.axsave`     |Versioned save container                        |

Names may change through an ADR before public stabilization, but the format family and design goals are required.

15.3 Format requirements

Native AXIOM formats MUST:

• have published schemas for licensed developers;
• support forward and backward migration;
• be content-addressable where useful;
• store stable IDs;
• support textual diffs for authored logic/data where practical;
• allow binary payloads for performance-heavy content;
• support chunking and streaming;
• include version and compatibility metadata;
• include license/provenance references;
• be recoverable after interrupted writes;
• support deterministic hashing;
• avoid unnecessary engine-version lock-in.

15.4 AXIR

AXIR is the semantic intermediate representation connecting:

• Simple mode intent;
• AXIOM Flow;
• native code generation;
• scripting;
• AI analysis;
• gameplay behavior;
• network determinism;
• tests;
• Unreal conversion.

AXIR should represent operations, types, data flow, events, authority, persistence, side effects, permissions, and test hooks.

V1 may execute AXIR through native code, WebAssembly, or a reference VM. The fully proprietary AXVM is V1-EXPERIMENTAL unless it reaches production gates.

────────

16. AXIOM Connect

16.1 Purpose

AXIOM Connect is the typed interface through which AXIOM AI, internal tools, external agents, CI systems, plugins, and services interact with the platform.

No agent should need uncontrolled filesystem manipulation to operate the engine.

16.2 Interfaces

AXIOM Connect MUST support:

• native in-process SDK;
• command-line interface;
• local IPC;
• gRPC or equivalent typed high-performance RPC;
• REST for broadly compatible service operations;
• WebSocket/event streams for realtime state;
• MCP-compatible tool exposure for authorized AI clients;
• plugin capability manifests;
• event subscriptions;
• authenticated service-to-service APIs.

16.3 Capability model

Examples:

```text
project.create
project.open
project.inspect
project.migrate
project.build
project.test
project.package

world.create
world.inspect
world.modify
world.stream_profile

scene.create
scene.validate
scene.capture

entity.spawn
entity.modify
entity.delete

asset.import
asset.generate
asset.optimize
asset.license_check

logic.create
logic.compile
logic.test

material.create
shader.compile
animation.retarget
audio.bind

network.simulate
network.profile
chain.simulate
wallet.sign_request

playtest.start
playtest.observe
playtest.stop

gauntlet.run
release.submit
```

16.4 Permission and audit

Every capability call MUST include:

• caller identity;
• project identity;
• capability scope;
• requested operation;
• consequence tier;
• authorization result;
• input/output hashes where practical;
• duration and resource use;
• resulting change set or transaction ID;
• audit event.

16.5 Connector SDK

The Connector SDK allows temporary bootstrap tools, external agents, asset services, source control systems, build farms, cloud providers, payment processors, and later hardware devices to integrate without becoming architectural dependencies.

External orchestrators such as Manus may help bootstrap repositories or connectors during development, but the shipping platform MUST use AXIOM AI and AXIOM Connect rather than require Manus or any other external agent product.

────────

17. AXIOM Bridge: Unreal

17.1 Objective

AXIOM-XIII MUST be able to analyze, load, import, and progressively translate legally portable Unreal projects, code, and assets while preserving original AXIOM architecture.

The bridge is a migration and interoperability layer, not a permanent requirement to emulate Unreal internally.

17.2 Import flow

```text
SELECT .UPROJECT
      ↓
PROJECT INVENTORY
      ↓
LICENSE / PROVENANCE SCAN
      ↓
DEPENDENCY AND PLUGIN GRAPH
      ↓
COMPATIBILITY REPORT
      ↓
TRANSLATION PLAN
      ↓
ISOLATED CONVERSION BRANCH
      ↓
ASSET / CODE / LOGIC CONVERSION
      ↓
GAUNTLET
      ↓
NATIVE .AXIOM PROJECT
```

17.3 Compatibility report

The analyzer MUST report separately:

• developer-owned source and content;
• engine-owned source that cannot be redistributed or converted as creator property;
• third-party plugins and their licenses;
• supported assets;
• supported materials;
• supported animation;
• supported levels/worlds;
• supported C++ patterns;
• supported Blueprints;
• supported Niagara/FX equivalents;
• supported audio systems;
• unsupported or ambiguous items;
• expected visual or behavioral differences;
• manual intervention;
• legal review requirements.

It MUST NOT claim a misleading percentage without a clear denominator and category breakdown.

17.4 Semantic mappings

Provisional mappings:

|Unreal concept       |AXIOM concept                             |
|---------------------|------------------------------------------|
|Project / `.uproject`|`.axiom` project                          |
|Actor                |Entity or composed prefab                 |
|Actor Component      |Component                                 |
|UObject/data object  |Resource/data object                      |
|Blueprint            |AXIOM Flow / AXIR / generated native code |
|Level                |Scene/world cell                          |
|World Partition      |WORLDSTREAM topology                      |
|Gameplay Ability     |Ability/interaction graph                 |
|Data Asset           |AXIOM Resource/Data                       |
|Material             |`.axmat` graph                            |
|Niagara              |`.axfx` graph/system                      |
|Animation Blueprint  |animation graph                           |
|MetaSound            |ORPHEUS audio graph                       |
|Gameplay Tags        |AXIOM taxonomy/tag registry               |
|Replication          |AXIOM network authority/replication schema|

17.5 C++ translation

AXIOM Bridge SHOULD:

• parse Unreal reflection macros and object relationships;
• build a semantic graph rather than perform text substitution;
• map common types and lifecycles;
• identify engine-specific assumptions;
• generate AXIOM interfaces and migration adapters;
• preserve developer comments and tests;
• create unsupported-pattern reports;
• avoid importing Epic-owned engine source as creator-owned AXIOM code.

17.6 Blueprint translation

Blueprint conversion SHOULD target AXIOM Flow and AXIR. Complex or unsupported nodes must remain visible as unresolved adapters rather than being silently discarded.

17.7 Asset translation

The bridge SHOULD support common portable source and interchange formats directly. When only engine-processed asset data exists, conversion must respect licensing and technical limitations.

17.8 Reverse export

V1 MAY provide selected export to Unreal-friendly formats for creator-owned assets and data, but native AXIOM features need not degrade to the lowest common denominator. Round-trip parity is not a V1 requirement.

────────

18. Source Control and Collaboration

18.1 Branch strategy

The canonical hosted repository strategy uses:

• main — production-qualified source;
• staging — release candidate integration;
• develop — active integration;
• feature/* — short-lived feature branches;
• fix/* — fixes;
• experiment/* — non-production research;
• release/* — stabilized release branches when necessary.

Agents work in isolated branches/worktrees. Protected branches require reviews and Gauntlet evidence.

18.2 Semantic diffs

AXIOM must display useful diffs for:

• worlds and scenes;
• entity composition;
• logic graphs;
• materials;
• animation graphs;
• audio graphs;
• project settings;
• chain modules;
• store metadata;
• tests.

A binary-only “file changed” indicator is insufficient for professional collaboration.

18.3 Merging

The Integrator must distinguish:

• textual conflict;
• semantic graph conflict;
• asset identity conflict;
• schema conflict;
• world spatial conflict;
• authority/replication conflict;
• licensing conflict;
• performance budget conflict.

18.4 Checkpoints and recovery

Every consequential AI Build creates:

• a source-control checkpoint;
• a project graph snapshot;
• affected asset hashes;
• migration record;
• rollback instructions.

Autosave is not a substitute for source control.

19. Engine Core

19.1 Runtime goals

AXIOM Engine is the native runtime and development foundation for .axiom projects. It must support:

• high-fidelity 3D;
• large streamed worlds;
• deterministic or authoritative multiplayer profiles;
• 2D and 2.5D games;
• editor and game execution;
• desktop and future fixed hardware;
• headless dedicated servers;
• tools and asset processing;
• modular packages;
• hot iteration;
• signed commercial packaging;
• native integration with AXIOM AI, Chain, Arena, Store, and PYRAMID.

19.2 Language strategy

AXIOM-XIII uses a multi-language strategy with explicit boundaries rather than one language everywhere.

C++

C++ is the primary V1 language for:

• rendering hot paths;
• game runtime;
• engine-facing APIs;
• animation/physics integration;
• platform abstraction where C/C++ ecosystem access is required;
• Unreal Bridge compatibility;
• high-performance first-party gameplay code.

The baseline should use a current, supported language standard at implementation time, with unsafe or legacy patterns restricted by coding standards and static analysis.

Rust

Rust is the primary V1 language for:

• AXIOM Shell bootstrap services;
• AXIOM AI orchestration services;
• AXIOM Connect services;
• package management;
• blockchain node and wallet core;
• security-sensitive services;
• distributed tooling;
• PYRAMID Kernel research;
• service and CLI development;
• selected engine systems where FFI cost is justified.

AXIOM Flow and AXIR

AXIOM Flow is the visual/semantic gameplay authoring layer. It compiles to AXIR.

AXScript / AXVM

A dedicated AXIOM scripting language and VM are strategic future capabilities. V1 MUST reserve namespaces, package metadata, debugging hooks, determinism rules, and ABI boundaries. The complete independent VM is V1-EXPERIMENTAL unless it passes production gates.

Web and interface code

Where web technology accelerates bootstrap UX, it must remain behind AXIOM Shell interfaces and must not define the game runtime architecture. The long-term console shell should be renderable through AXIOM’s own UI stack.

19.3 ABI and FFI

Cross-language boundaries MUST use:

• stable C-compatible ABI or generated bindings;
• owned memory rules;
• explicit error types;
• versioned interfaces;
• thread-safety declarations;
• deterministic serialization;
• fuzzed boundary tests;
• no exception unwinding across unsupported boundaries.

19.4 Runtime modes

AXIOM Engine must support:

• editor runtime;
• standalone game runtime;
• dedicated server;
• headless simulation;
• automated test runner;
• asset processor;
• build worker;
• replay renderer;
• Chain/Arena integration test mode;
• PYRAMID Virtual Target mode.

19.5 Platform abstraction

Host platform services sit behind AXIOM interfaces:

• window/display;
• input;
• graphics API;
• audio device;
• networking;
• filesystem;
• process/threading;
• memory mapping;
• clocks/timers;
• cryptography;
• secure storage;
• controller/haptics;
• accessibility;
• crash reporting;
• hardware telemetry.

The production implementation may use host OS facilities. Experimental proprietary replacements implement the same contracts.

────────

20. AXIOM CORE, ECS, and Object Model

20.1 Composition-first design

AXIOM uses an entity-component-system foundation for large-scale simulation while supporting authored object lifecycles and resources where ECS is not the best representation.

The architecture must not force every editor asset, service object, or UI document into ECS.

20.2 Core concepts

• Entity — stable identity with composed components.
• Component — structured data and optional lifecycle hooks.
• System — logic operating over component queries.
• Resource — shared scoped data such as world settings or registries.
• Prefab — reusable entity graph.
• Scene — authored spatial and logical collection.
• World — streaming topology, simulation domains, and persistent state.
• Service — non-ECS engine/platform capability.
• Asset — content-addressed or identity-addressed external/processed resource.

20.3 ECS requirements

The ECS MUST support:

• data-oriented storage;
• archetype or equivalent efficient queries;
• stable external entity IDs;
• transient runtime handles;
• multithreaded system execution;
• change detection;
• deterministic ordering profiles;
• replication metadata;
• persistence metadata;
• editor inspection;
• hot reload/migration;
• streaming in and out;
• sparse and dense component patterns;
• component schema versioning;
• large creature, crowd, projectile, vegetation, and simulation workloads.

20.4 Authoring/runtime split

Authoring data may be rich and hierarchical. Runtime data should be compiled into efficient representations.

```text
AUTHORING GRAPH
      ↓ cook/compile
RUNTIME ECS + ASSET TABLES + STREAMING CHUNKS
```

AXIOM AI and Advanced mode operate on the authoring graph. Runtime packages contain only what is needed for execution unless developer/debug data is included intentionally.

20.5 Stable identity

Persistent entity identity MUST be separate from runtime memory address or array index. Save games, network state, chain references, editor selections, and narrative state must survive streaming, reload, and migration.

────────

21. AXIOM FABRIC: Jobs, Scheduling, and Concurrency

21.1 Purpose

AXIOM FABRIC is the job graph and scheduling system for engine, editor, asset, AI, and server workloads.

21.2 Requirements

FABRIC MUST support:

• dependency-aware jobs;
• work stealing;
• CPU affinity hints;
• priority classes;
• frame-critical and background lanes;
• deterministic scheduling modes;
• fibers/coroutines or equivalent lightweight suspension;
• asynchronous I/O;
• GPU task integration;
• cancellation;
• time budgets;
• profiling and trace visualization;
• editor, game, server, and build-worker profiles;
• future PYRAMID CPU/GPU/AI accelerator scheduling.

21.3 Priority classes

Provisional classes:

1. real-time input/audio;
2. frame-critical simulation;
3. rendering submission;
4. network receive/send;
5. streaming and decompression;
6. animation/physics support;
7. editor interaction;
8. background asset and shader work;
9. AI generation/build tasks;
10. idle node compute.

No background AI or chain workload may cause frame-time instability in a foreground game.

21.4 Frame graph relationship

The renderer frame graph and FABRIC must share dependency and timing information without becoming one monolithic scheduler.

21.5 Distributed jobs

V1-PREVIEW may support remote shader compilation, asset processing, build tasks, tests, and AI jobs through signed work units. Future PYRAMID node compute must use the same work-unit model with opt-in resource limits and verification.

────────

22. Memory, Serialization, and Data Safety

22.1 Memory system

AXIOM Memory must provide:

• tagged allocators;
• arenas/pools;
• frame allocators;
• GPU memory tracking;
• streaming budgets;
• leak and lifetime detection;
• guard and debug modes;
• allocation trace correlation;
• platform-specific policies;
• crash-safe diagnostics;
• deterministic allocation modes where required.

22.2 Serialization

Serialization MUST be:

• schema-driven;
• versioned;
• bounded and validated;
• endian-aware;
• robust against untrusted input;
• streamable;
• deterministic when used for hashes/replays/chain attestations;
• capable of partial loading;
• capable of migration;
• independent of memory layout.

22.3 Save safety

Save operations MUST use:

• atomic or journaled writes;
• checksums;
• version metadata;
• backup generations;
• schema migrations;
• cloud conflict resolution;
• corruption detection;
• user-visible recovery.

22.4 Untrusted data

Projects, plugins, saves, network packets, media, assets, chain data, and user-generated packages are untrusted inputs. Every parser and decoder must be fuzzed and bounded.

────────

23. Reflection, Types, and Schema Registry

23.1 Reflection

AXIOM requires compile-time and runtime reflection sufficient for:

• editor property inspection;
• serialization;
• networking;
• AI understanding;
• logic graphs;
• scripting;
• tests;
• version migration;
• package/plugin integration;
• documentation generation.

Reflection metadata should be generated rather than depend on fragile manual registration.

23.2 Type IDs

Types MUST use stable globally namespaced identifiers. Renames and moves require aliases/migrations rather than silently changing identity.

23.3 Schema Registry

The registry stores:

• type definitions;
• versions;
• compatibility rules;
• migration functions;
• ownership;
• security classification;
• network/persistence/chain suitability;
• documentation;
• deprecation status.

23.4 AI access

AXIOM AI must query the Schema Registry to understand valid project mutations. It may not invent fields or API calls and assume they exist.

────────

24. AXIOM Flow, AXIR, Scripting, and Gameplay Programming

24.1 AXIOM Flow

AXIOM Flow is a prompt + node + code authoring system. It must allow creators to:

• build event-driven logic;
• inspect generated graphs;
• convert graph regions to code;
• call code from graphs;
• generate tests;
• annotate authority, persistence, determinism, and side effects;
• debug live values;
• profile execution;
• compare revisions;
• package reusable functions and systems.

24.2 Graph design

The graph should use typed ports, explicit control flow, data flow, events, async operations, state machines, behavior trees/statecharts where appropriate, and subgraphs.

Hidden implicit behavior should be minimized.

24.3 Determinism annotations

Logic intended for rollback, lockstep, replay, or chain-attested simulation must declare:

• deterministic math profile;
• random seed source;
• time source;
• permitted I/O;
• floating-point policy;
• external service restrictions;
• authority owner.

24.4 Hot reload

V1 SHOULD support hot reload for:

• data;
• logic graphs;
• selected scripts;
• materials/shaders;
• audio graphs;
• UI;
• non-breaking component changes.

Native code hot reload may be limited by platform and ABI; failures must not corrupt the editor session.

24.5 Debugger

The debugger MUST support:

• breakpoints;
• step/continue;
• watch values;
• event tracing;
• graph execution highlighting;
• entity/component inspection;
• network authority views;
• replay frame inspection;
• deterministic divergence detection;
• AI-generated explanation of traces.

24.6 Package APIs

Public gameplay APIs must be versioned, documented, testable, and stable enough for commercial projects. Internal engine APIs may evolve more rapidly but must be isolated.

────────

25. Package, Plugin, and Dependency System

25.1 .axpkg

AXIOM packages may contain:

• engine modules;
• editor tools;
• gameplay systems;
• assets;
• templates;
• shaders;
• audio;
• chain modules;
• server components;
• integrations;
• documentation and tests.

25.2 Package manifest

Every package MUST declare:

• identity and version;
• publisher;
• signatures;
• dependencies;
• supported AXIOM versions;
• supported platforms;
• permissions/capabilities;
• licenses;
• provenance;
• AI-training/derivative-use terms where relevant;
• native code status;
• network access;
• filesystem access;
• wallet/chain access;
• store category;
• tests;
• security review level.

25.3 Sandboxing

Packages should use capability-based access. Native code packages receive stronger review and may be restricted from high-trust environments.

25.4 Dependency lock

Commercial builds MUST have a lockfile, hashes, signatures, SBOM, and reproducible dependency resolution.

25.5 Revocation

AXIOM may revoke store distribution or network access for malicious packages. Projects must retain a documented path for offline preservation where licensing allows, while security-critical revocation must protect users and platform integrity.

────────

26. Build and Packaging System

26.1 Targets

V1 target types:

• Windows client;
• Linux client;
• Windows/Linux editor;
• Linux dedicated server;
• local test;
• headless simulation;
• PYRAMID Virtual Target;
• replay renderer;
• Store sandbox;
• Chain/Arena test environment.

Additional platforms are added through explicit platform adapters.

26.2 Build graph

The build system MUST support:

• incremental builds;
• distributed work;
• content cooking;
• shader compilation;
• asset deduplication;
• package signing;
• symbol management;
• separate client/server content;
• deterministic/reproducible modes;
• release manifests;
• delta patches;
• rollback packages;
• channel-specific configuration;
• SBOM generation;
• license reports;
• performance metadata.

26.3 Build identity

Every build receives:

• project ID;
• version;
• commit/change set;
• dependency lock hash;
• content manifest hash;
• compiler/toolchain identifiers;
• target profile;
• signing identity;
• Gauntlet evidence reference;
• release channel;
• store/entitlement metadata.

26.4 Patch system

Patches SHOULD be chunk-based and content-addressed to minimize download size. The updater must support pause/resume, integrity checks, disk-space planning, rollback, and repair.

27. AXIOM RENDER: AAA Rendering Architecture

27.1 Objective

AXIOM RENDER must be designed to pursue two demanding visual classes simultaneously:

1. Large authored fantasy worlds with long sightlines, complex environments, large creatures, dynamic combat, rich atmosphere, and dense environmental storytelling.
2. Extreme perceptual realism produced by physically convincing materials, lighting, animation, camera behavior, exposure, optics, motion, and environmental detail.

The goal is not to reproduce another engine’s internal implementation. The goal is for AXIOM projects to achieve contemporary AAA-scale fidelity through AXIOM-owned systems and terminology.

27.2 Rendering backends

V1-PRODUCTION SHOULD support:

• Vulkan on Windows and Linux;
• Direct3D 12 on Windows where needed for hardware/platform reach;
• a backend abstraction that can later support Metal and proprietary PYRAMID APIs.

The renderer must use a frame graph/resource graph, explicit synchronization, GPU-driven pipelines, asynchronous compute where useful, and robust shader/pipeline caching.

27.3 Renderer paths

AXIOM RENDER should support configurable paths:

• deferred/hybrid high-fidelity path;
• forward or forward-plus path for selected content;
• 2D/2.5D path;
• offline/path-traced cinematic/reference path;
• headless/no-render path;
• low-spec/scalable path.

27.4 Core subsystems

```text
AXIOM RENDER
├── NEXUS — virtualized geometry and GPU-driven visibility
├── PHOTON — global illumination, reflections, shadows, and path tracing
├── WORLDSTREAM — world/asset streaming and spatial hierarchy
├── OPTICS — camera, lens, sensor, exposure, and perceptual imaging
├── MATERIALS — physically based and stylized surface system
├── ATMOSPHERE — sky, fog, clouds, volumetrics, weather
├── WATER — oceans, rivers, fluid surfaces, underwater rendering
├── VEGETATION — dense instancing, wind, interaction, seasonal state
├── CHARACTER — skin, eyes, hair, cloth, deformation
├── FX — particles, fluids, destruction visuals, decals
├── UI — engine-native 2D/vector/text rendering
└── DEBUG — capture, validation, comparison, and profiling
```

27.5 Quality profiles

The renderer must support project-defined profiles rather than one universal look:

• photoreal;
• cinematic fantasy;
• stylized painterly;
• graphite/engraved;
• manga/ink;
• pixel/2D;
• mixed reality or body-camera optics;
• low-latency competitive.

The profile controls material models, outlines, hatching, screen-space treatment, lighting, post, animation cadence, camera, and performance budgets without forcing all AXIOM games to share one visual identity.

────────

28. NEXUS: Virtualized Geometry

28.1 Purpose

NEXUS is AXIOM’s geometry virtualization and visibility system. It targets film-scale source meshes, dense environments, large worlds, procedural content, destructible geometry, and heterogeneous spatial data.

28.2 Supported data classes

NEXUS is architected to support:

• triangle meshes;
• terrain and height/mesh hybrids;
• voxels/sparse volumes;
• point clouds;
• Gaussian splat or related point-based representations where technically appropriate;
• CAD-like source data;
• procedural geometry;
• vegetation clusters;
• destruction fragments;
• impostors and billboards as fallback representations.

Not every class must be production-complete in V1, but the geometry resource model must not assume triangles are the only future representation.

28.3 Pipeline

NEXUS processing:

1. imports source geometry;
2. validates topology and materials;
3. partitions into spatial/visibility clusters;
4. constructs hierarchical representations;
5. generates cluster bounds, cones, error metrics, and streaming pages;
6. creates collision/navigation proxies;
7. builds GPU-friendly metadata;
8. deduplicates repeated data;
9. packages content-addressed pages;
10. produces scalable fallback tiers.

28.4 Runtime

At runtime NEXUS must provide:

• GPU-driven culling;
• hierarchical detail selection;
• occlusion and frustum culling;
• instance culling;
• streaming page requests;
• material-range grouping;
• virtual memory/budget control;
• large object and creature support;
• deformation compatibility strategy;
• destruction update strategy;
• profiler views of geometry cost and residency.

28.5 V1 scope

V1-PRODUCTION requires a reliable clustered static-geometry path and GPU-driven visibility suitable for high-detail environments.

V1-PREVIEW may include deformable/animated virtual geometry, voxels, point clouds, splats, and advanced destruction integration.

28.6 Acceptance targets

On reference hardware and a representative test scene, NEXUS SHOULD demonstrate:

• stable frame times under dense geometry;
• no manual per-asset LOD requirement for the primary high-detail path;
• visible-quality transitions below defined thresholds;
• bounded memory and streaming behavior;
• fallback support on less capable GPUs;
• reproducible capture and comparison tests.

────────

29. PHOTON: Lighting, Reflections, and Path Tracing

29.1 Purpose

PHOTON is AXIOM’s hybrid lighting architecture. It must support large dynamic worlds, interiors, moving lights, day/night, emissive contribution, destruction, reflections, and high-end cinematic output.

29.2 Hybrid strategy

PHOTON may combine:

• hardware ray tracing;
• software ray tracing or signed-distance/mesh representations;
• probes;
• screen-space techniques;
• voxel/clipmap caches;
• radiance caches;
• baked data where useful;
• path tracing for reference and offline rendering.

The system must choose techniques based on scene, hardware, quality profile, and performance budget rather than demand one solution everywhere.

29.3 Required effects

V1-PRODUCTION should support:

• physically plausible direct lighting;
• dynamic shadows;
• scalable indirect diffuse lighting;
• reflections with quality fallbacks;
• emissive contribution within defined limits;
• interior/exterior transitions;
• sky and atmosphere contribution;
• volumetric lighting;
• temporal stability controls;
• denoising and history validation;
• developer visualization of lighting sources and cache state.

29.4 Path tracing

The path-traced mode is used for:

• cinematic rendering;
• ground-truth reference images;
• material validation;
• lighting comparison;
• high-end photo mode;
• training/evaluating AI-assisted scene optimization.

It is not required to run at interactive framerate on all hardware in V1.

29.5 Stylization

PHOTON must allow non-photoreal rendering profiles to reinterpret light through ink, graphite, painterly, cel, limited-palette, or other artistic models.

────────

30. WORLDSTREAM: World and Asset Streaming

30.1 Purpose

WORLDSTREAM is the hierarchical streaming system for worlds ranging from a room to a planet-scale topology.

The conceptual hierarchy may include:

```text
Universe / Instance
  → Planet / Macro World
    → Region
      → Cell
        → Scene
          → Object / Asset Page
```

A project uses only the levels it needs.

30.2 Requirements

WORLDSTREAM MUST support:

• spatial partitioning;
• dependency-aware streaming;
• asynchronous I/O;
• content-addressed pages;
• priority based on camera, player, network relevance, audio, quests, and predicted movement;
• CPU/GPU memory budgets;
• seamless transitions;
• origin/precision strategies for large worlds;
• server simulation partitioning;
• persistence handoff;
• editor streaming preview;
• world-state layers and variants;
• cooperative/multiplayer consistency;
• deterministic streaming decisions where simulation requires them.

30.3 Predictive streaming

AXIOM AI/runtime may predict near-term movement and requests using:

• velocity and camera direction;
• navigation routes;
• quest/mission state;
• vehicle speed;
• multiplayer party state;
• authored hints;
• learned player patterns.

Prediction must be bounded and fall back safely when wrong.

30.4 World variants

WORLDSTREAM must support regional transformation, seasons, destruction, player decisions, and alternate states without requiring complete duplicate worlds. It should use shared base geometry plus state layers, overrides, and content deltas.

30.5 Server cells

For large online worlds, WORLDSTREAM architecture must allow simulation cells to be assigned to server workers and migrate authority. This is V1-ARCHITECTED; production V1 concurrency may be lower.

────────

31. OPTICS: Physical and Stylized Camera System

31.1 Purpose

OPTICS treats the camera and image pipeline as first-class simulation rather than a final stack of post-process effects. This is essential for body-camera-style realism and cinematic art direction.

31.2 Camera model

OPTICS SHOULD model:

• sensor/film size;
• focal length and field of view;
• aperture;
• shutter/exposure time;
• ISO/sensitivity model;
• focus distance and behavior;
• depth of field;
• lens distortion;
• vignetting;
• chromatic aberration;
• bloom and glare;
• rolling/global shutter profiles;
• motion blur;
• auto exposure and adaptation;
• color response and tone mapping;
• stabilization;
• camera inertia;
• head/body coupling;
• handheld/body-mounted motion;
• focus breathing;
• dirt/damage/water where art-directed.

31.3 Gameplay integrity

Visual realism must not make games unplayable. Projects require accessibility and competitive overrides for motion, blur, distortion, shake, field of view, and exposure.

31.4 Camera authoring

OPTICS must expose:

• reusable camera rigs;
• transitions/blends;
• collision and occlusion behavior;
• lock-on and target framing;
• animation-driven camera;
• replay and cinematic cameras;
• procedural noise and physical rigs;
• network-safe camera separation from authoritative gameplay.

────────

32. Materials, Shaders, and Surface Intelligence

32.1 Material system

AXIOM Materials must support physically based rendering and project-specific shading models.

Required material capabilities include:

• metal/roughness and specular workflows;
• normal and displacement detail;
• virtual or streamed texture support;
• layered materials;
• decals;
• wetness, dirt, snow, mud, blood, wear, and environmental blending;
• subsurface scattering;
• skin and eyes;
• hair/fur;
• cloth;
• glass/transmission;
• water;
• clearcoat;
• anisotropy;
• emissive materials;
• stylized ramps, hatching, outlines, and screentones;
• runtime parameterization;
• material instancing;
• shader permutation control.

32.2 Shader system

The shader toolchain must provide:

• graph and source authoring;
• cross-backend compilation;
• reflection;
• caching;
• permutation analysis;
• hot reload;
• debugging and capture;
• validation across target GPU classes;
• secure handling of untrusted custom shaders;
• deterministic build hashes.

A custom AXIOM shader compiler/backend is V1-EXPERIMENTAL. Production may use established compiler infrastructure behind AXIOM interfaces.

32.3 Semantic material generation

AXIOM AI should understand material intent and generate structured graphs rather than only images. Example:

> “Stone submerged for forty years and exposed recently.”

The resulting material may combine mineral deposits, algae, a waterline, wetness gradient, rough dry upper stone, moss probability, and environment-aware blending, with all layers editable.

32.4 Material provenance

Generated or imported textures and material layers must retain source, model/tool, prompt owner, license, and derivative-use metadata.

────────

33. Atmosphere, Weather, Water, and Vegetation

33.1 Atmosphere

AXIOM must support:

• physically based sky/atmospheric scattering;
• time of day;
• astronomical bodies where needed;
• fog;
• volumetric clouds;
• local volumes;
• weather fronts;
• precipitation;
• lightning;
• wind;
• project-specific stylization.

33.2 Weather simulation

Weather can be visual-only or gameplay-authoritative. The system must mark which state affects gameplay, networking, persistence, and chain-attested outcomes.

33.3 Water

V1 should support:

• oceans/lakes/rivers;
• reflection/refraction;
• foam and shore interaction;
• underwater rendering;
• buoyancy hooks;
• scalable simulation;
• flow fields for rivers;
• gameplay queries.

Advanced fluid simulation is V1-PREVIEW unless a first-party title requires it for production.

33.4 Vegetation

Vegetation requires:

• high-density instancing;
• biome rules;
• wind;
• interaction and bending;
• culling/streaming;
• destruction/regrowth hooks;
• seasonal and world-state variants;
• collision tiers;
• networking policy;
• material and lighting compatibility.

────────

34. Character Rendering, Animation, and Motion

34.1 Character fidelity

AXIOM must support cinematic characters and stylized characters through separate profiles.

Character rendering includes:

• skin shading;
• eyes and tear line;
• teeth and mouth;
• hair/fur;
• cloth;
• layered clothing;
• decals, dirt, blood, wetness;
• facial deformation;
• LOD/virtualization strategy;
• crowd scalability.

34.2 Animation stack

The animation system MUST support:

• skeletal animation;
• blend trees/state graphs;
• animation layers;
• montages/sequences;
• root motion;
• additive animation;
• retargeting;
• inverse kinematics;
• control rigs;
• motion warping;
• motion matching;
• procedural locomotion;
• ragdoll/physics blending;
• facial animation;
• animation events;
• network replication and prediction;
• deterministic frame data for fighting games;
• editor timeline and debugging.

34.3 Motion intelligence

MOTION agent and runtime tools may:

• analyze reference footage;
• retarget animation;
• generate transitions;
• identify foot sliding;
• repair contact;
• synthesize motion variants;
• construct motion-matching databases;
• compare animation timing to combat design;
• generate lower-fidelity LOD motion;
• validate skeleton/mesh relationships.

34.4 Combat precision

High-fidelity animation must remain subordinate to gameplay timing. AXIOM must expose hit frames, cancel windows, root motion, hurt/hit volumes, invulnerability, and network prediction separately from visual polish.

34.5 Facial and dialogue animation

The system should support:

• phoneme/viseme curves;
• expression rigs;
• emotional state layers;
• performance capture import;
• audio-driven preview;
• multilingual timing;
• manual correction;
• consent and provenance for likeness/voice data.

────────

35. Physics, Collision, Destruction, and Simulation

35.1 Strategy

V1-PRODUCTION may use a proven physics foundation behind AXIOM APIs while AXIOM Physics is developed and benchmarked. The project must not expose external physics types as permanent public game APIs.

35.2 Required capabilities

• rigid bodies;
• static and dynamic collision;
• character movement queries;
• constraints/joints;
• ragdolls;
• vehicles hooks;
• cloth/hair integration;
• triggers and queries;
• continuous collision options;
• broadphase/narrowphase profiling;
• deterministic or replayable profiles where possible;
• server-authoritative modes;
• scalable destruction;
• buoyancy;
• editor visualization.

35.3 Character controller

AXIOM should provide a configurable controller supporting:

• grounded movement;
• slopes and steps;
• jumping/falling;
• crouching;
• climbing/mantling hooks;
• swimming;
• moving platforms;
• root motion;
• network prediction;
• camera-independent control;
• action-game responsiveness.

Projects may replace it entirely.

35.4 Destruction

Destruction should separate:

• cosmetic local debris;
• gameplay-authoritative break state;
• persistent world destruction;
• network-replicated geometry;
• chain or tournament-relevant state.

35.5 AXIOM Physics research

The proprietary program SHOULD explore:

• deterministic solver profiles;
• ECS-native data layout;
• GPU acceleration;
• large creature and environmental constraints;
• network reconciliation;
• world streaming handoff;
• destruction integration;
• testable reproducibility.

────────

36. ORPHEUS: Audio and Music Engine

36.1 Purpose

ORPHEUS is AXIOM’s real-time audio, music, and interactive composition system. Audio is treated as gameplay infrastructure, not only file playback.

36.2 Required capabilities

• low-latency audio graph;
• sample playback and streaming;
• buses, sends, effects, sidechains, and automation;
• 3D spatialization;
• occlusion and obstruction;
• environmental acoustics/reverb;
• adaptive music states;
• tempo/beat/bar synchronization;
• stems and transitions;
• dynamic mixing;
• voice chat integration;
• loudness management;
• recording/capture;
• audio profiling;
• accessibility support;
• runtime music/gameplay events.

36.3 Music production integration

ORPHEUS SHOULD support:

• MIDI input/output;
• tempo maps;
• musical time as a first-class clock;
• stem and cue import;
• procedural composition graphs;
• VST3 or equivalent plugin hosting in authorized development/editor environments;
• bounce/render to game-ready assets;
• plugin sandboxing;
• deterministic event scheduling for rhythm/gameplay synchronization;
• soundtrack publishing to MEDIA/STORE.

Third-party plugin formats are development integrations, not runtime dependencies for shipped games unless properly packaged and licensed.

36.4 Adaptive score

Projects can map gameplay state to:

• instrumentation;
• harmony;
• rhythm;
• intensity;
• motif;
• spatial source;
• distortion;
• diegetic/non-diegetic transition.

The system should support first-party concepts where music changes the world, not only music reacting to the world.

36.5 Audio AI

MAESTRO may:

• analyze stems;
• identify tempo/key/structure;
• build transition maps;
• generate implementation graphs;
• detect clipping, masking, phase, and loudness issues;
• create placeholder sound design;
• preserve source rights/provenance;
• never silently claim ownership of imported music.

────────

37. UI, Text, Input, and Haptics

37.1 AXIOM UI

AXIOM UI must support:

• controller-first navigation;
• mouse/keyboard;
• touch where applicable;
• vector and texture UI;
• layout and responsive scaling;
• animation;
• localization;
• accessibility;
• world-space UI;
• gamepad focus;
• screen reader metadata;
• data binding;
• styling/theming;
• high-performance game HUDs;
• shell and store UI;
• secure wallet/signing UI separated from untrusted game content.

37.2 Input

The input system must support:

• actions and axes;
• remapping;
• multiple devices;
• controller glyphs;
• context layers;
• local multiplayer;
• accessibility devices;
• haptics;
• motion/gyro hooks;
• deterministic input capture;
• replay;
• rollback input history;
• anti-cheat telemetry boundaries.

37.3 Haptics

Haptics should support:

• standard rumble;
• high-definition patterns where hardware supports it;
• adaptive trigger-like abstractions without depending on one vendor;
• audio-to-haptic authoring;
• accessibility controls;
• future PYRAMID controller capabilities.

38. Runtime AI, Navigation, and World Simulation

38.1 Separation from AXIOM AI

AXIOM AI is the development/platform intelligence. Runtime game AI is a separate, sandboxed game system. A shipped game must not require a large external model unless the developer explicitly chooses that architecture and discloses its operational requirements.

38.2 Runtime AI capabilities

AXIOM Engine must support:

• behavior trees;
• state machines/statecharts;
• utility AI;
• planners and goal-oriented action systems;
• perception;
• navigation meshes and graphs;
• crowd movement;
• tactical queries;
• environment queries;
• blackboards/memory;
• squad coordination;
• encounter directors;
• dialogue/relationship integration;
• simulation LOD;
• deterministic/server-authoritative modes;
• learned model inference through a controlled runtime interface.

38.3 Navigation

Navigation must support:

• streamed worlds;
• dynamic obstacles;
• multi-layer traversal;
• flying/swimming/climbing agents;
• large creatures;
• destructible environments;
• local avoidance;
• cooperative pathing;
• server authority;
• authoring/debug visualization;
• agent-specific cost maps.

38.4 Simulation LOD

Distant or unobserved entities may use simplified simulation, statistical models, schedules, or event-driven state. The handoff between full and reduced simulation must preserve important player-visible state.

38.5 Large-scale world simulation

The architecture should support:

• populations;
• factions;
• economies;
• ecology;
• weather;
• migration;
• wars and territory;
• causal histories;
• persistent world decisions;
• player-influenced nations;
• large strategy simulations.

The Civilization/God project is a validation target for the causal and macro-simulation layers.

38.6 Causality graph

AXIOM may maintain a causal graph linking events, actors, decisions, consequences, and forecasts. This graph can support long-term consequences, narrative explanation, strategy simulation, and AI-assisted debugging.

The graph must distinguish authored truth from simulation inference.

────────

39. Networking Architecture

39.1 Objectives

AXIOM NET must support multiple game classes without forcing one networking model on all projects.

Supported profiles:

1. Authoritative action — open-world action, shooters, co-op, RPGs.
2. Rollback fighting — frame-sensitive 2D/3D fighters.
3. Lockstep/strategy — deterministic or semi-deterministic RTS/tactics.
4. Async — cards, turns, correspondence, creator workflows.
5. Persistent shard — large worlds with spatial partitioning.
6. Local/offline — no network dependency.

39.2 Transport abstraction

AXIOM NET must sit above transport interfaces supporting:

• reliable streams;
• unreliable datagrams;
• congestion control;
• encryption;
• connection migration where available;
• peer-to-peer and relay paths;
• dedicated servers;
• local network;
• future PYRAMID optimized transport.

Production V1 may use established protocols/libraries behind AXIOM Secure Transport APIs.

39.3 Authority model

Every networked state declares:

• owner/authority;
• replication audience;
• prediction policy;
• reconciliation policy;
• persistence policy;
• cheat sensitivity;
• replay relevance;
• tournament relevance.

39.4 Replication

The replication system must provide:

• state snapshots/deltas;
• event/RPC equivalents;
• relevance/interest management;
• priority and bandwidth budgets;
• prediction;
• reconciliation;
• interpolation/extrapolation;
• dormancy;
• streamed entity handoff;
• entity schema versioning;
• server migration architecture;
• debugging and bandwidth visualization.

39.5 Rollback profile

The rollback profile must support:

• deterministic simulation core;
• input history;
• save/restore snapshots;
• prediction;
• rollback/resimulation;
• frame delay configuration;
• desync detection;
• frame data tools;
• spectator/replay synchronization;
• tournament integrity.

39.6 Strategy profile

The strategy profile may use:

• lockstep commands;
• deterministic state;
• authoritative correction;
• turn/phase validation;
• command replay;
• large unit aggregation;
• host migration or dedicated authority.

39.7 Large-shard architecture

AXIOM’s long-term target includes 10,000-plus connected players or simulated participants within a logical shard. V1 does not claim that target as production-qualified.

V1 must architect:

• spatial cells;
• distributed authority;
• interest management;
• cell handoff;
• global services separated from cell simulation;
• entity routing;
• cross-cell messaging;
• persistent event log;
• load testing with synthetic clients;
• graceful degradation.

A production V1 concurrency number must be published only after measured tests on defined hardware and game workload.

39.8 Multiplayer services

AXIOM Network provides:

• sessions/lobbies;
• party integration;
• presence;
• NAT traversal/relay;
• dedicated server allocation;
• region selection;
• cross-play identity;
• voice/text integration;
• matchmaking handoff;
• replays;
• spectators;
• server browser where permitted;
• cloud saves;
• sanctions/ban enforcement;
• incident controls.

39.9 Network test profiles

Every networked project must define tests for:

• baseline latency;
• high latency;
• jitter;
• packet loss;
• reorder;
• duplication;
• bandwidth cap;
• disconnect/reconnect;
• host/server crash;
• version mismatch;
• malicious packets;
• clock skew;
• cross-region behavior.

────────

40. Replays, Spectating, and Deterministic Evidence

40.1 Replay types

AXIOM supports:

• input/deterministic replay;
• authoritative state replay;
• event replay;
• video capture;
• hybrid replay with game-aware camera and metadata.

40.2 Competitive evidence

Arena-approved games must produce tamper-evident match records containing:

• build identity;
• ruleset;
• players/teams;
• inputs or authoritative events as appropriate;
• server identity;
• timing and network conditions;
• anti-cheat signals;
• result;
• signatures/attestations;
• dispute evidence pointer;
• retention policy.

40.3 Spectating

Spectator mode must separate live competitive information from delayed/public views to prevent coaching or information leaks.

40.4 Media integration

Replays can be opened in MEDIA for camera editing, clip creation, commentary, soundtrack use, captions, and publishing where rights permit.

────────

41. Persistence, Cloud, and Data Platform

41.1 Data classes

AXIOM distinguishes:

• local settings;
• local saves;
• cloud saves;
• account/profile data;
• social data;
• project source and assets;
• build artifacts;
• store/catalog data;
• entitlements;
• wallet and financial ledger;
• chain state;
• Arena rankings/results;
• telemetry;
• moderation evidence;
• secrets and keys.

Each class requires separate retention, encryption, access, backup, and residency policy.

41.2 Cloud architecture

AXIOM services should be deployable across multiple providers and self-hosted environments through portable service contracts and infrastructure-as-code.

Core service classes:

• identity/auth;
• social/presence;
• media;
• project sync;
• object storage;
• build workers;
• artifact registry;
• game servers;
• matchmaking;
• Arena;
• Store/catalog;
• payment/ledger;
• wallet gateway;
• Chain nodes/indexers;
• telemetry;
• moderation/support;
• policy engine.

41.3 Data ownership and portability

Creators must be able to export their own project source and original assets subject to licenses. Players should be able to export appropriate account, transaction, and creation records.

AXIOM service continuity must not depend on one cloud vendor.

41.4 Offline behavior

Games should declare offline capabilities. Ordinary single-player titles should remain playable offline after entitlement validation according to store policy. Chain-dependent or live-service functions must communicate their requirements clearly.

41.5 Disaster recovery

Production requires:

• encrypted backups;
• multi-region recovery for critical services;
• tested restore procedures;
• point-in-time recovery for ledgers/catalogs;
• chain validator/key recovery plans;
• immutable audit archives;
• recovery time and recovery point objectives per service;
• regular drills.

────────

42. AXIOM Protocol

42.1 Purpose

AXIOM Protocol defines stable semantic objects and events shared across engine, services, Chain, Arena, Store, Wallet, and future PYRAMID devices.

42.2 Protocol objects

The protocol should define:

• UserIdentity;
• PublicProfile;
• LegalVerificationReference;
• DeveloperIdentity;
• Studio/Team;
• Game;
• Build;
• Package;
• Asset;
• DigitalObject;
• License;
• ProvenanceRecord;
• Entitlement;
• Achievement;
• ReputationClaim;
• Match;
• Tournament;
• PrizePool;
• Team/Roster;
• ResultAttestation;
• StoreListing;
• Purchase;
• RoyaltySplit;
• CreatorContribution;
• Wallet;
• Transaction;
• Node/Validator;
• PolicyProfile;
• ModerationAction.

42.3 Versioning

Protocol schemas must be versioned, backwards-compatible where practical, and governed through RFC/ADR processes. Chain-breaking changes require explicit migration and network upgrade procedures.

42.4 Open versus proprietary

AXIOM may publish enough protocol documentation for interoperability, verification, node operation, and developer integration while retaining proprietary ownership of reference implementations, services, engine technology, store, AI, and restricted protocols.

────────

43. AXIOM Chain

43.1 Mission

AXIOM Chain is a custom sovereign blockchain designed around games and digital-world economics, not a generic chain with gaming branding.

Its core purposes are:

• digital object ownership;
• creator provenance;
• license expression;
• royalty splits;
• marketplace settlement;
• tournament and prize escrow;
• achievement/trophy authenticity;
• game and build identity;
• reputation claims;
• validator/node economics;
• cross-game assets where a developer authorizes them.

43.2 What “from scratch” means

AXIOM will own and implement:

• node software;
• state model;
• consensus integration;
• networking integration;
• mempool/transaction lifecycle;
• execution/runtime modules;
• storage schema;
• wallet integration;
• indexing;
• game-native transaction types;
• governance and upgrade process;
• test and simulation framework.

AXIOM should use established, publicly reviewed cryptographic primitives and consensus research rather than invent unreviewed mathematics for branding purposes.

43.3 V1 consensus profile

The recommended V1 architecture is a Byzantine-fault-tolerant proof-of-stake or authority-stake hybrid with deterministic finality.

V1 may begin with a curated/federated validator set operated by AXIOM and trusted partners, then expand validator participation under node licenses, staking, technical requirements, and governance.

Target objectives, subject to measured implementation:

• short, predictable finality;
• low transaction cost;
• deterministic execution;
• high throughput for marketplace and game-object operations;
• no proof-of-work waste;
• safe validator rotation;
• slashing or equivalent accountability;
• snapshot/state-sync support;
• testnet, staging, and production networks.

Exact block time, validator count, and throughput become release metrics after benchmark and threat review, not marketing promises in this specification.

43.4 State model

AXIOM Chain should use an object-capability or account/object hybrid state model suited to owned game objects and licenses.

Every state transition must declare:

• signer/authority;
• object(s) consumed or modified;
• permissions;
• fee/gas/resource limits;
• expected version;
• resulting objects/events;
• royalty/split implications;
• policy restrictions.

43.5 Native modules

V1-PRODUCTION should prioritize audited native modules over unrestricted contracts:

• identity references;
• digital object/NFT collections;
• mint/burn/transfer;
• licenses and usage rights;
• creator contribution and royalty splits;
• marketplace listing and settlement;
• tournament/prize escrow;
• match-result attestation;
• achievement/trophy issuance;
• validator/staking/governance basics;
• wallet recovery policy objects;
• protocol upgrade controls.

43.6 Smart contracts

General smart contracts are V1-PREVIEW. They should run in a deterministic sandbox through AXVM or a WebAssembly-compatible reference runtime, with capability permissions, metering, bounded storage, reproducible builds, and formal/property testing requirements for high-value contracts.

43.7 Asset data

Large files do not live directly on-chain. The chain stores:

• content hashes;
• metadata;
• ownership;
• license;
• provenance;
• creator splits;
• canonical storage pointers;
• version relationships.

Assets may be stored in AXIOM object storage, content-addressed networks, creator-controlled storage, or approved decentralized storage. Availability policy must be explicit.

43.8 NFTs and digital objects

Tokenized objects are first-class, not an afterthought. They may represent:

• game items;
• skins;
• characters;
• maps or creator assets;
• music and sound licenses;
• limited editions;
• tournament trophies;
• achievements;
• development contributions;
• access passes;
• collectibles;
• creator revenue rights only where legally and economically approved.

Every object must distinguish:

• ownership of the token/object record;
• license to use associated content;
• intellectual property ownership;
• game utility;
• transferability;
• royalties;
• restrictions;
• permanence and storage availability.

Owning an NFT must not be falsely described as owning underlying copyright unless the license explicitly grants it.

43.9 Game authority

A blockchain must not decide moment-to-moment gameplay. Games and authoritative servers produce signed events or results. Chain modules verify permitted attestations and settle economic consequences.

43.10 Match attestation

For a prize-relevant match:

```text
MATCH CREATED
  → RULESET/BUILD LOCKED
  → PLAYERS ELIGIBLE
  → SERVER ASSIGNED
  → MATCH EXECUTED
  → REPLAY/EVIDENCE HASHED
  → SERVER + INTEGRITY SERVICES SIGN RESULT
  → DISPUTE WINDOW
  → PRIZE MODULE SETTLES
```

43.11 No mandatory external bridge in V1

Cross-chain bridges are a high-risk attack surface. V1 should not depend on them. Future bridges require separate security, liquidity, governance, and recovery design.

43.12 Chain governance and control

AXIOM must retain sufficient upgrade and emergency authority to protect the network, store, tournaments, and users, while gradually distributing validator operation and transparent governance.

Recommended governance layers:

• protocol RFC process;
• public upgrade proposals where appropriate;
• validator votes;
• AXIOM security council/emergency controls with published scope;
• time locks for non-emergency changes;
• audited upgrade binaries;
• fork and recovery procedures;
• clear separation between chain governance and AXIOM Store policy.

────────

44. WALLET and Economic Identity

44.1 Wallet modes

AXIOM Wallet should support:

Managed mode

AXIOM secures keys and provides familiar account recovery. Appropriate for mainstream players and low-friction onboarding.

Self-custodial mode

The user controls keys and recovery material. AXIOM provides signing UI, hardware wallet hooks, and export where supported.

Studio/organization mode

Multisignature, role-based, policy-controlled wallets for companies, teams, tournaments, and creator splits.

44.2 Key separation

Keys for:

• login;
• wallet signing;
• developer package signing;
• store publishing;
• tournament administration;
• validator operation;

must be separate and permissioned.

44.3 Signing UX

Every signing request must display:

• operation;
• asset/value;
• recipient/contract/module;
• fees;
• permissions being granted;
• reversibility;
• network;
• human-readable summary;
• raw details available for advanced users.

Untrusted game UI cannot obscure or replace secure wallet confirmation.

44.4 Recovery

Recovery may include:

• encrypted backups;
• recovery codes;
• social/multisig recovery;
• hardware-backed keys;
• organization policy;
• time-delayed recovery;
• fraud review for managed accounts.

44.5 Ledger separation

AXIOM distinguishes:

• store fiat/payment ledger;
• internal rewards/credits;
• on-chain assets/tokens;
• creator payable ledger;
• prize payable ledger;
• tax/reporting records.

They may be presented together but must not be conflated technically or legally.

────────

45. AXIOM Arena

45.1 Mission

AXIOM Arena is the shared competitive system for skill-based matchmaking, ranked play, tournaments, prize pools, teams, spectating, replays, integrity, and settlement.

45.2 Match classes

• unranked/casual;
• ranked;
• private/custom;
• sponsored tournament;
• creator tournament;
• league;
• player-funded skill competition where enabled;
• token-denominated competition where enabled;
• qualifier/championship;
• asynchronous challenge.

45.3 Rating system

Arena must support game-specific rating models while providing shared identity and history.

Capabilities:

• placement matches;
• uncertainty/deviation;
• team and individual ratings;
• mode-specific ratings;
• seasonal decay/reset rules;
• smurf detection;
• inactivity handling;
• party skill adjustment;
• region/latency constraints;
• protected newcomer pools;
• transparent rank tiers;
• hidden matchmaking parameters protected from exploitation.

45.4 Matchmaking objective

The matchmaker optimizes a configurable objective combining:

• skill quality;
• latency;
• wait time;
• party size;
• input/device pool;
• region/policy eligibility;
• trust/integrity score;
• game version;
• team composition;
• tournament bracket constraints.

45.5 Prize pools

Prize pool sources may include:

• AXIOM sponsorship;
• game publisher sponsorship;
• advertising sponsorship;
• creator-funded prizes;
• community or token treasury allocations;
• player entry/stake where enabled by applicable policy;
• mixed structures.

Prize funds must be escrowed or otherwise secured before a tournament begins.

45.6 Policy engine

Arena features are exposed through a policy engine considering:

• user location;
• operator/entity;
• age;
• identity verification;
• sanctions/restrictions;
• payment method;
• game classification;
• tournament type;
• local rules;
• tax/reporting requirements;
• risk level.

The protocol may support a feature even when a particular client or operator does not expose it.

45.7 Integrity

Arena requires:

• server-authoritative or verified simulation;
• signed builds;
• anti-cheat;
• replay/evidence;
• collusion detection;
• account/device trust;
• disconnect rules;
• exploit adjudication;
• dispute process;
• result finality;
• prize hold/review mechanisms;
• transparent official rules.

45.8 Anti-pay-to-win disclosure

AXIOM does not need to ban all economically powerful digital objects platform-wide, but ranked/tournament rules must explicitly state whether tokenized or purchased items affect competition. Competitive integrity profiles may require normalized loadouts or approved item pools.

45.9 Arena API

Games integrate through an Arena adapter defining:

• modes;
• team sizes;
• result schema;
• replay type;
• anti-cheat requirements;
• rating model;
• disconnect rules;
• eligibility;
• prize compatibility;
• tournament format;
• spectator policy.

────────

46. Anti-Cheat, Fraud, and Trust

46.1 Defense layers

AXIOM uses:

• secure build signing;
• server authority;
• input and state validation;
• deterministic verification where possible;
• replay analysis;
• behavior analytics;
• device/account trust;
• code integrity checks;
• network anomaly detection;
• tournament supervision;
• wallet and payment fraud controls;
• collusion graph analysis;
• human investigation and appeals.

46.2 PC anti-cheat

V1 should prefer server-side and behavior-based controls, signed packages, and minimal privileged software. A kernel component may be offered for high-stakes modes only after independent security review and clear disclosure.

46.3 PYRAMID advantage

Future PYRAMID secure boot, signed OS/runtime, hardware-backed keys, and device attestation can provide stronger tournament integrity without relying solely on invasive third-party PC anti-cheat.

46.4 AI-driven adversary

SENTINEL continuously generates cheat and fraud hypotheses, but automated enforcement affecting accounts or money must meet evidence and review thresholds.

46.5 Appeals

Users require:

• reason categories;
• evidence retention;
• appeal path;
• human escalation for material sanctions;
• separation of game moderation, store enforcement, Arena suspension, and wallet restrictions.

────────

47. STORE, Marketplace, and Publishing

47.1 Store authority

AXIOM controls the official Store’s:

• submission rules;
• technical certification;
• content policy;
• regional availability;
• pricing and payment support;
• refunds;
• discovery and featuring;
• reviews;
• updates;
• DLC;
• token/NFT disclosures;
• creator asset categories;
• malware/security standards;
• tournament/Arena integration;
• revenue distribution;
• enforcement and appeals.

47.2 Publishing flow

```text
DEVELOPER ACCOUNT
  → PROJECT/GAME REGISTRATION
  → BUILD UPLOAD
  → AUTOMATED CERTIFICATION
  → SECURITY/LICENSE/CONTENT REVIEW
  → STORE SANDBOX
  → AGE/RATING/POLICY METADATA
  → RELEASE CANDIDATE
  → SIGNING
  → PUBLISH
  → MONITOR / UPDATE / ROLLBACK
```

47.3 Store item classes

• games;
• DLC/expansions;
• subscriptions;
• non-tokenized in-game items;
• tokenized game objects/NFTs;
• asset packs;
• plugins;
• templates;
• music/sound;
• development services;
• tournament passes;
• creator content approved for the current phase.

47.4 Entitlements

The entitlement service is the canonical commercial access layer for ordinary purchases. Chain ownership may supplement or represent specific assets, but games must not depend on a slow or unavailable chain for every launch.

47.5 Developer economics

The commercial model may combine:

• free creator tier;
• commercial engine royalty after a threshold;
• subscription tiers;
• enterprise/custom license;
• Store distribution fee;
• payment processing fee;
• Chain fees;
• Arena service fee;
• AI/compute usage;
• cloud/build/server usage;
• asset marketplace fee.

Exact rates are not locked in the technical specification and must be modeled before public commitment.

47.6 Creator splits

Store and Chain must support automatic split definitions for:

• co-developers;
• asset creators;
• composers;
• map/UGC creators in future;
• licensors;
• tournament organizers;
• affiliates where approved.

Splits require clear recoupment, tax, refund, chargeback, and dispute rules.

47.7 External distribution

AXIOM may allow games built with AXIOM to be distributed outside the Store under the Engine/Runtime License. External distribution does not waive engine royalties, runtime notices, or other contractual obligations.

First-party AXIOM Originals may use exclusivity, timed exclusivity, or enhanced AXIOM/PYRAMID features as strategic policy.

────────

48. MEDIA Platform

48.1 Native capture

AXIOM must provide:

• screenshot capture;
• video capture;
• replay bookmarks;
• last-N-minutes capture;
• microphone and party audio policy;
• HDR-aware capture;
• performance-aware encoding;
• privacy indicators;
• rights metadata.

48.2 Editing

V1 should include basic:

• trim;
• combine;
• crop/aspect;
• captions;
• overlays;
• replay camera selection;
• soundtrack selection from owned/authorized media;
• export and publish.

48.3 Game music

MEDIA and ORPHEUS should support:

• official soundtracks;
• interactive stems;
• visualizers;
• credits;
• purchase/licensing;
• creator pages;
• music-reactive game media.

48.4 Rights and provenance

Publishing must check:

• game capture permissions;
• music rights;
• voice/likeness consent;
• imported asset licenses;
• disclosure requirements;
• region restrictions.

48.5 Broadcast and tournaments

Arena events may provide:

• official broadcast feed;
• observer tools;
• delayed spectator streams;
• bracket and stat overlays;
• clip generation;
• co-stream permission controls;
• sponsor assets.

────────

49. SOCIAL and PROFILE Platform

49.1 Identity layers

AXIOM distinguishes:

• private account identity;
• public profile identity;
• legal/KYC reference;
• wallet addresses;
• developer/studio identity;
• competitive team identity;
• pseudonymous identities where permitted.

49.2 Social graph

The social graph supports:

• mutual friends;
• follows;
• blocks;
• groups;
• parties;
• guilds/clans;
• developer teams;
• tournament rosters;
• project collaboration;
• reputation claims.

49.3 Messaging

Messaging requires:

• direct and group text;
• party voice;
• project comments;
• moderation/reporting;
• spam/rate limits;
• parental controls;
• encryption in transit;
• retention and legal policy;
• safe-link/file scanning.

49.4 Reputation

Reputation may include:

• completed transactions;
• creator credits;
• tournament conduct;
• moderation history;
• project collaboration;
• verified skills;
• community endorsements.

Reputation models must avoid exposing sensitive personal data or becoming opaque social-credit systems controlling unrelated rights.

50. Licensing, Intellectual Property, and Commercial Control

50.1 Licensing objective

AXIOM-XIII must be accessible enough to attract creators and studios while preserving ownership, licensing control, payment rights, store authority, and the value of proprietary technology.

The recommended model is source-available proprietary software, not a permissive open-source license for the core platform.

50.2 Required agreement separation

The legal architecture MUST separate:

1. AXIOM Creator License — access to build noncommercial, educational, prototype, or threshold-limited projects.
2. AXIOM Commercial Engine License — commercial use, royalties/subscription, reporting, audit, runtime redistribution.
3. AXIOM Source License — source visibility and modification rights without a right to create a competing engine/platform.
4. AXIOM Runtime Distribution License — redistribution of required runtime components.
5. AXIOM Store Agreement — official distribution, fees, content rules, updates, refunds, discovery, and payments.
6. AXIOM Arena Agreement — competitive rules, integrity, prize structures, disputes, eligibility.
7. AXIOM Chain/Node Agreement — validators, nodes, staking, protocol behavior, slashing/accountability, software license.
8. AXIOM Asset/Plugin Publisher Agreement — packages, security, licenses, royalties, updates.
9. AXIOM AI Terms — model/provider usage, generated output, data handling, prohibited extraction, attribution.
10. PYRAMID Device and OS Terms — hardware, secure boot, node mode, warranty, prohibited tampering where legally enforceable.

Acceptance of one agreement must not silently imply all others.

50.3 Creator ownership

The core promise should be:

> **Creators own the original games and content they create. AXIOM owns AXIOM.**

Subject to third-party rights and agreed licenses, creators retain ownership of:

• original characters, worlds, stories, art, music, designs, trademarks;
• game-specific source and logic authored by them;
• project data and original assets;
• creator brand;
• revenues after fees, royalties, refunds, taxes, and contractual splits.

AXIOM retains ownership of:

• engine and runtime;
• AXIOM AI and internal models/orchestration;
• Shell, Store, Social, Media, Arena, Wallet, and platform services;
• Chain reference implementation and proprietary protocols;
• editor, Connect, Bridge, package system, build system, and formats where protected;
• PYRAMID OS, Kernel, drivers, hardware designs, firmware, and brand;
• internal anti-cheat, ranking, fraud, security, and store systems;
• AXIOM trademarks and first-party IP.

50.4 Source access restrictions

Authorized source access may allow:

• inspection;
• debugging;
• private modifications;
• contribution;
• building AXIOM games;
• enterprise/internal forks under contract.

It must not automatically allow:

• removing AXIOM licensing checks and redistributing the engine;
• rebranding and selling a competing engine;
• training competing models on restricted source without permission;
• publishing restricted internals;
• extracting anti-cheat/security logic;
• circumventing royalties or store obligations;
• sublicensing beyond granted rights.

50.5 Runtime and build enforcement

AXIOM should combine contractual and technical controls:

• signed developer identity;
• project and build IDs;
• license manifest;
• runtime notices where required;
• royalty reporting workflows;
• store/entitlement integration;
• signed production packages;
• enterprise/offline license files;
• audit rights defined narrowly and reasonably.

AXIOM must not create hidden backdoors into creator games or private source.

50.6 Format control and portability

Publishing .axiom schemas and allowing project export does not transfer ownership of the engine. Project portability should be a creator trust advantage, while protected compilers, services, runtime internals, and store capabilities remain licensed.

50.7 Contributions

External contributions require a contributor agreement or compatible license grant ensuring AXIOM can use, modify, commercialize, and relicense accepted contributions while preserving contributor attribution and avoiding ownership ambiguity.

50.8 First-party games

AXIOM Originals remain separate copyrighted/trademarked IP. Engine access does not grant rights to first-party game code, assets, characters, mechanics expression, names, music, or world content.

────────

51. Asset Provenance and Originality Firewall

51.1 Provenance record

Every meaningful asset, code module, model output, music file, animation, dataset, and package must record:

• creator/source;
• creation/import date;
• content hash;
• tool/model/version;
• prompt or process owner where applicable;
• input references;
• license;
• commercial rights;
• modification rights;
• redistribution rights;
• attribution requirement;
• AI-training/derivative permissions where known;
• project usage;
• chain object if tokenized;
• review status.

51.2 License graph

A build’s license graph must identify every distributable dependency and block release when required rights are absent or contradictory.

51.3 Mechanics Registry

Each signature mechanic records:

• design goal;
• broad inspirations;
• original terminology;
• original implementation;
• player experience;
• audiovisual expression;
• differences from references;
• patents or legal research required;
• prohibited copied elements;
• approval status.

51.4 Reference firewall

References may guide mood, quality, scale, genre, or problem-solving, but AXIOM AI must not reproduce protected characters, art, text, music, maps, UI, code, animations, or distinctive expression.

51.5 Canon governance

Narrative projects use statuses:

• CANON;
• ADAPTED;
• PROPOSED;
• NON-CANON PROTOTYPE;
• REJECTED;
• SUPERSEDED.

AI output is PROPOSED by default.

────────

52. Global Policy and Legal Architecture

52.1 Design goal

AXIOM must support global operation, multiple legal entities/operators, and protocol-level capabilities without hardcoding one country’s assumptions into every system.

52.2 Policy engine

The policy engine evaluates:

• operator;
• service region;
• user location;
• age;
• identity status;
• sanctions/restrictions;
• payment rail;
• wallet mode;
• asset type;
• game/rating;
• tournament structure;
• prize source;
• tax/reporting profile;
• consumer-protection rules;
• content restrictions;
• privacy/data residency;
• risk classification.

It returns enabled, disabled, modified, review-required, or limits.

52.3 Operator modularity

Different authorized operators may expose different combinations of:

• store commerce;
• token trading;
• prize competition;
• player-funded skill matches;
• wallet custody;
• fiat settlement;
• validator services;
• content categories.

The shared protocol and account system must clearly show which operator and terms govern a transaction.

52.4 Legal review gates

Before production launch of high-risk features, qualified counsel must review:

• securities/financial classification;
• money transmission and custody;
• gambling/skill competition;
• consumer protection;
• tax;
• sanctions/AML/KYC;
• privacy;
• minors;
• NFT/digital asset disclosures;
• marketplace liability;
• IP and licensing;
• terms and dispute resolution;
• hardware and product safety.

The architecture should maximize optionality; it must not claim that protocol design creates immunity from law.

────────

53. Security Architecture

53.1 Security principles

• zero trust;
• least privilege;
• defense in depth;
• secure defaults;
• explicit trust boundaries;
• secrets never in code/prompts/logs;
• signed code and packages;
• strong key separation;
• reproducible and auditable builds;
• continuous testing;
• rapid revocation and recovery;
• independent review for high-value systems.

53.2 Trust zones

1. untrusted game/content zone;
2. creator project zone;
3. editor/tool zone;
4. AXIOM AI agent sandboxes;
5. platform service zone;
6. Store and package-signing zone;
7. Wallet/signing zone;
8. Chain validator zone;
9. Arena integrity zone;
10. AXIOM internal restricted zone;
11. future PYRAMID secure system zone.

Cross-zone operations require typed, authenticated interfaces.

53.3 Secrets

Secrets must be stored in:

• OS secure storage;
• hardware-backed keystores where available;
• dedicated secret management for services;
• isolated signing systems/HSMs for production keys;
• short-lived credentials;
• encrypted CI variables.

Agents receive scoped ephemeral tokens, never raw master secrets.

53.4 Secure software supply chain

Requirements:

• signed commits/releases where appropriate;
• protected branches;
• dependency pinning;
• SBOMs;
• vulnerability scanning;
• provenance attestations;
• reproducible build modes;
• build worker isolation;
• package signatures;
• update rollback;
• incident revocation;
• third-party package review.

53.5 Prompt and agent security

Project files, assets, repository text, web content, and package metadata may contain prompt injection. AXIOM AI must treat external content as data, not authority.

Agent permissions come only from the capability broker and project policy, never from instructions inside an imported file.

53.6 Wallet and chain security

• separate hot, warm, and cold key policies;
• HSM or equivalent for platform treasury/signing;
• multisig for high-value operations;
• withdrawal limits and alerts;
• transaction simulation;
• contract/module audits;
• bug bounty;
• chain monitoring;
• emergency pause limited by governance policy;
• recovery and incident playbooks.

53.7 Privacy

Private data must be minimized, classified, encrypted, access-logged, retained only as necessary, and separated from public chain data. No sensitive legal identity or private gameplay data should be placed on an immutable public ledger.

53.8 Security program

Before production economics, AXIOM needs:

• security lead;
• threat models;
• secure coding standards;
• external penetration tests;
• chain audits;
• wallet audits;
• anti-cheat review;
• incident response team;
• vulnerability disclosure program;
• bug bounty;
• tabletop exercises.

────────

54. Dependency Replacement Ladder

54.1 Philosophy

AXIOM-XIII V1 must include every strategic proprietary destination in its architecture and repository. Production may initially use proven dependencies behind AXIOM interfaces while AXIOM replacements progress through conformance gates.

54.2 Ladder

|Layer                 |V1 production implementation      |V1 proprietary workstream    |Production replacement gate                                                 |
|----------------------|----------------------------------|-----------------------------|----------------------------------------------------------------------------|
|Kernel                |Hardened Linux/host OS            |PYRAMID Kernel               |Boot, drivers, isolation, performance, reliability, security audit, recovery|
|GPU kernel/user driver|Vendor/Mesa/host                  |AXIOM GPU                    |Conformance, stability, performance, hardware coverage, shader correctness  |
|Graphics API          |Vulkan/D3D12 abstraction          |PYRAMID graphics API/backend |Renderer feature parity and tooling                                         |
|TLS/secure transport  |Audited established implementation|AXIOM Secure Transport       |Protocol conformance, formal/fuzz tests, independent audit                  |
|Crypto implementation |Audited established primitives    |AXIOM Crypto                 |Side-channel review, test vectors, audit; no unreviewed primitives          |
|Image/audio codecs    |Established codecs                |AXIOM Image/Media codecs     |Correctness, fuzz safety, quality, performance, patent/license review       |
|Physics               |Proven library/reference          |AXIOM Physics                |Stability, determinism profiles, performance, feature parity                |
|Filesystem            |Host filesystem                   |AXIOM FS                     |Crash consistency, performance, repair, encryption, tooling                 |
|Database/storage      |Proven stores                     |AXIOM Data engines           |Durability, query/scale, backup, operational maturity                       |
|Shader compiler       |Established compiler toolchains   |AXIOM Shader compiler/backend|Cross-vendor correctness, optimization, diagnostics                         |
|VM/runtime            |Native/WASM/reference             |AXVM                         |Sandboxing, determinism, performance, debugging, security                   |
|OS shell              |Desktop host + AXIOM Shell        |PYRAMID System               |Full console UX, update/recovery, device support                            |
|AI models             |Local/external providers          |AXIOM models                 |Quality, cost, safety, privacy, hardware efficiency                         |

54.3 Replacement rule

No dependency is replaced in production because the AXIOM version merely compiles. It must beat or match the required correctness, security, operational, and performance threshold on the supported target.

54.4 Strategic priority

Highest proprietary value:

1. AXIOM AI/orchestration;
2. engine/editor/project graph;
3. renderer/world systems;
4. Chain/Arena/Store protocol;
5. package/build/licensing system;
6. PYRAMID OS and secure environment;
7. fixed-hardware optimization;
8. kernel and drivers when hardware strategy justifies them.

Lower early strategic value:

• generic image decoders;
• generic math routines;
• reinvention of well-reviewed cryptographic primitives.

They remain in the V1 program but must not block differentiated product delivery.

────────

55. PYRAMID Virtual Target

55.1 Purpose

V1 must support development for PYRAMID before physical hardware is finalized.

The Virtual Target defines:

• CPU performance class;
• GPU feature class;
• memory budget;
• storage bandwidth and capacity assumptions;
• controller/input capabilities;
• display resolutions and frame profiles;
• audio capabilities;
• network assumptions;
• secure storage/attestation behavior;
• operating environment APIs;
• thermal/power performance envelope;
• package and update format.

55.2 Build behavior

Developers select:

Build Target → PYRAMID V1 Virtual Target

AXIOM then enforces:

• allowed APIs;
• memory budgets;
• shader feature set;
• CPU/GPU frame budgets;
• package layout;
• controller mappings;
• storage/streaming budgets;
• suspend/resume constraints;
• network and wallet security requirements;
• certification tests.

55.3 Reference performance profiles

Exact hardware is an ADR, but V1 should define provisional profiles:

PYRAMID Quality

• high visual fidelity;
• 30 fps minimum target;
• reconstructed or native high-resolution output;
• ray-traced/hybrid features where supported.

PYRAMID Performance

• 60 fps target;
• scalable geometry, lighting, and effects;
• responsive action gameplay.

PYRAMID Competitive

• 120 fps target where the game supports it;
• reduced latency and visual settings;
• Arena integrity profile.

55.4 Emulator/simulator

The Virtual Target should simulate limits on a developer PC and produce reports. It is not required to perfectly emulate future hardware before that hardware exists.

────────

56. PYRAMID OS

56.1 V1 production path

The first PYRAMID software image should use a hardened, immutable Linux-based foundation with:

• verified/signed boot chain where hardware permits;
• read-only base system;
• atomic A/B updates;
• sandboxed games/apps;
• controller-first AXIOM Shell;
• GPU/audio/input drivers;
• secure wallet service;
• developer and retail modes;
• recovery environment;
• telemetry and diagnostics under user policy;
• node mode as opt-in.

56.2 Modes

PLAY MODE

Games, Media, Social, Store, Profile, Wallet, Arena.

DEV MODE

Simple/Advanced AXIOM development, build, testing, profiling, publishing, keyboard/mouse/voice/controller support.

NODE MODE

Optional Chain validation, storage, build compute, shader compilation, testing, rendering, or AI inference under explicit resource, security, and compensation settings.

56.3 Retail and developer access

Every PYRAMID device may potentially become a development device through authenticated DEV mode rather than requiring a separate expensive development kit. High-risk kernel, signing, and hardware debug functions remain restricted.

56.4 Secure separation

Games and third-party packages must not access wallet keys, other games, private projects, system signing, or validator secrets.

────────

57. PYRAMID Kernel

57.1 V1 requirement

PYRAMID Kernel MUST exist as a V1-EXPERIMENTAL workstream and repository, even though production PYRAMID OS initially runs on Linux.

57.2 Goals

The long-term kernel may provide:

• low-latency game scheduling;
• deterministic priority lanes;
• fast suspend/resume;
• secure isolation;
• wallet/key services;
• anti-cheat and attestation;
• GPU/AI workload scheduling;
• audio scheduling;
• content-addressed package mounting;
• update/recovery;
• node compute isolation;
• fixed-hardware optimization.

57.3 Initial kernel scope

V1-EXPERIMENTAL target:

• boot under virtualized x86-64 and/or chosen architecture;
• physical/virtual memory management;
• interrupt and timer handling;
• task/thread scheduler;
• basic IPC;
• capability/security model;
• simple filesystem or initrd;
• logging/diagnostics;
• user process launch;
• test harness;
• minimal networking and input milestones as later V1 experiments.

57.4 Language and safety

Rust is recommended for significant kernel components, with assembly and C/C++ where required. Unsafe code must be isolated, reviewed, and fuzzed/tested.

57.5 Not a production dependency

No commercial wallet, prize, or user-security promise may depend on PYRAMID Kernel until independent review and production gates pass.

────────

58. AXIOM GPU and Driver Program

58.1 Strategy

Supporting every consumer GPU from scratch is not a V1 production requirement. AXIOM first targets mature host drivers, then optimizes and replaces around a fixed PYRAMID hardware configuration.

58.2 V1-EXPERIMENTAL work

• graphics command and memory model research;
• shader compiler/backend experiments;
• display and presentation abstraction;
• GPU scheduler integration design;
• fixed-hardware driver prototype where documentation permits;
• conformance test harness;
• frame capture and validation;
• power/thermal telemetry interface;
• compatibility layer with AXIOM RENDER.

58.3 Fixed hardware advantage

Once PYRAMID hardware is selected, AXIOM can optimize:

• shader compilation;
• memory allocation;
• geometry page sizes;
• pipeline caches;
• frame pacing;
• storage-to-GPU streaming;
• power states;
• display modes;
• ray-tracing profiles;
• AI inference scheduling.

58.4 Production gate

A custom GPU stack cannot replace the host/vendor path until it passes:

• API/conformance suites;
• large game compatibility tests;
• shader correctness;
• crash/soak testing;
• performance comparison;
• power/thermal testing;
• security review;
• update/recovery testing.

────────

59. AXIOM Secure Transport, Crypto, Image, and Filesystem Programs

59.1 Secure Transport

Production V1 uses audited secure transport behind AXIOM APIs. The experimental implementation must target standards conformance, memory safety, fuzzing, side-channel review, certificate/identity validation, downgrade protection, and independent audit.

59.2 AXIOM Crypto

AXIOM Crypto defines a proprietary API and key-management architecture around established primitives for:

• hashing;
• signatures;
• encryption;
• authenticated encryption;
• key derivation;
• secure randomness;
• wallet keys;
• threshold/multisignature operations;
• hardware-backed keys;
• zero-knowledge interfaces where later justified.

AXIOM should not invent new cryptographic primitives without exceptional research justification and external peer review.

59.3 AXIOM Image/Media

V1-EXPERIMENTAL may implement selected decoders/encoders and an optimized texture/media pipeline. Strategic priority is:

• safe parsing;
• GPU-ready texture compression;
• streaming;
• transcoding;
• content-addressed storage;
• quality/performance;
• broad import compatibility.

59.4 AXIOM FS

The future filesystem should explore:

• content-addressed game packages;
• deduplication;
• encryption;
• atomic updates;
• snapshots;
• fast verification;
• streaming priority;
• repair;
• creator/project separation;
• chain/object integration.

────────

60. PYRAMID Hardware Roadmap

60.1 Hardware strategy

The first physical version can be a custom computer using commercially available components inside a purpose-built 3D-printed pyramid enclosure. It must deliver a console-like experience without waiting for custom silicon.

60.2 Prototype generations

PYRAMID P0 — Industrial/design prototype

• off-the-shelf desktop or compact PC internals;
• 3D-printed pyramid shell;
• functional airflow and service access;
• AXIOM Shell and Virtual Target testing;
• thermal, acoustic, safety, and usability experiments.

PYRAMID P1 — Controlled reference computer

• locked supported CPU/GPU/memory/storage combinations;
• custom cooling/enclosure;
• signed PYRAMID OS image;
• controller and accessories;
• secure storage/TPM-equivalent support;
• predictable performance profile;
• repair and upgrade policy.

PYRAMID P2 — Custom board/platform

• custom motherboard or tightly integrated board;
• optimized I/O and power;
• hardware-rooted trust;
• deeper OS/driver integration;
• manufacturing and certification program.

PYRAMID P3 — Custom silicon consideration

Only after platform scale, economics, performance needs, and capital justify it.

60.3 Enclosure

The pyramid design must be functional, not merely decorative. Engineering must address:

• intake/exhaust paths;
• dust filtration;
• GPU/CPU cooling;
• acoustic behavior;
• structural strength;
• cable routing;
• serviceability;
• component tolerances;
• materials and fire safety;
• shipping durability;
• orientation and stability;
• lighting and brand identity.

60.4 Development on console

PYRAMID must support game development directly through DEV Simple and Advanced. Keyboard/mouse, controller, voice, display, external storage, source control, and remote collaboration should be supported.

60.5 Node economics

Future users may opt into providing idle compute or storage. Any compensation system requires:

• explicit opt-in;
• power/thermal limits;
• resource isolation;
• verifiable work;
• anti-fraud;
• clear earnings and costs;
• hardware longevity protections;
• regional policy;
• ability to disable completely.

61. Performance Targets and Budgets

61.1 Performance philosophy

AXIOM must measure frame-time distributions, not only average FPS. Projects define target hardware and quality profiles. Every subsystem receives budgets and reports budget regressions in the Gauntlet.

61.2 Reference game profiles

AAA Quality profile

• target: stable 30 fps or better on defined reference hardware;
• high-quality lighting, geometry, materials, animation, atmosphere, and effects;
• high-resolution output using native or high-quality reconstruction;
• cinematic asset density;
• bounded traversal and streaming stalls.

AAA Performance profile

• target: stable 60 fps;
• responsive action gameplay;
• scalable ray tracing/GI, effects, crowd, geometry, and resolution;
• low controller-to-photon latency.

Competitive profile

• target: 120 fps where game design supports it;
• strict input/network latency budgets;
• reduced visual variability;
• Arena-approved settings and integrity.

Creator/editor profile

• responsive viewport;
• background compilation and asset processing;
• progressive preview;
• clear indication when preview differs from production build.

61.3 Provisional frame budgets

At 60 fps, the total frame budget is approximately 16.67 ms. A project may allocate a target such as:

|Domain                   |Provisional budget|
|-------------------------|-----------------:|
|Game simulation and AI   |2.5 ms            |
|Animation                |1.5 ms            |
|Physics                  |1.5 ms            |
|Rendering CPU submission |1.5 ms            |
|GPU geometry/material    |4.0 ms            |
|GPU lighting/post        |4.0 ms            |
|Audio/network/input/other|1.0 ms            |
|Headroom                 |0.67 ms           |

This is an example allocation, not a universal rule. Projects must publish their own measured budget.

61.4 Memory budgets

The Virtual Target must define:

• system memory;
• GPU memory or unified memory;
• working set by subsystem;
• streaming pool;
• audio pool;
• animation pool;
• network/server memory;
• editor overhead;
• safety margin.

Unbounded caches are prohibited.

61.5 Loading and iteration targets

V1 targets should include:

• shell launch to interactive state;
• project open time;
• incremental code build time;
• shader compile time;
• asset import time;
• play-in-editor start time;
• game launch time;
• world traversal hitch limits;
• patch size and install time.

Exact service-level objectives are set after baseline measurements, then enforced in CI.

61.6 Network targets

Per game/mode define:

• supported player count;
• server tick rate;
• latency targets;
• bandwidth per player;
• packet loss tolerance;
• rollback window;
• reconnect time;
• matchmaking time;
• server startup time.

61.7 Chain targets

Define and measure:

• finality latency;
• transaction throughput;
• node resource use;
• state growth;
• indexer delay;
• wallet signing latency;
• marketplace settlement;
• tournament settlement;
• recovery/state sync.

No public numeric claim may be made without reproducible benchmark methodology.

────────

62. Observability and Telemetry

62.1 Requirements

AXIOM must provide correlated:

• logs;
• metrics;
• traces;
• crash dumps;
• GPU captures;
• network captures;
• replay evidence;
• chain events;
• build events;
• agent actions;
• security audit events.

62.2 Correlation IDs

A user-reported failure should be traceable across:

• account/session;
• game build;
• server;
• project change set;
• store entitlement;
• Arena match;
• chain transaction;
• service trace;
• crash/replay.

Sensitive data must be redacted and access-controlled.

62.3 Developer telemetry

Projects can define custom events, but AXIOM must provide:

• schema validation;
• sampling;
• privacy classification;
• local debugging;
• dashboards;
• retention controls;
• export;
• cost estimation.

62.4 AI telemetry

AXIOM AI records:

• task and plan IDs;
• model/provider;
• tokens/compute/cost;
• tool calls;
• change sets;
• test outcomes;
• user approvals;
• failures and retries;
• security decisions;
• quality benchmarks.

Private prompts and source require access controls and configurable retention.

────────

63. Testing Strategy

63.1 Test pyramid

AXIOM requires:

• unit tests;
• property tests;
• fuzz tests;
• integration tests;
• end-to-end tests;
• visual regression;
• audio validation;
• gameplay automation;
• performance benchmarks;
• security testing;
• chaos testing;
• usability testing;
• hardware testing;
• certification testing.

63.2 Engine tests

• ECS correctness and performance;
• job scheduling;
• memory lifetime;
• serialization/migration;
• asset processing;
• renderer reference scenes;
• shader compiler matrix;
• physics scenes;
• animation/retargeting;
• audio timing;
• input;
• UI/navigation;
• package loading;
• update/rollback;
• project format compatibility.

63.3 AI tests

• requirement extraction;
• permission enforcement;
• plan correctness;
• tool hallucination prevention;
• project graph update;
• branch isolation;
• secret protection;
• prompt injection resistance;
• cost limits;
• mode switching;
• reproducibility where required;
• refusal to publish without approval;
• evidence quality.

63.4 Bridge tests

Maintain a corpus of Unreal projects containing:

• C++;
• Blueprints;
• materials;
• animation;
• world/level structures;
• plugins;
• networking;
• audio;
• unsupported patterns.

Every AXIOM release reports conversion behavior and regressions.

63.5 Chain tests

• consensus safety/liveness;
• validator changes;
• transaction/state invariants;
• malformed transactions;
• replay/double spend;
• module upgrades;
• wallet recovery;
• marketplace settlement;
• royalty arithmetic;
• tournament escrow;
• chain reorganization/fault scenarios;
• state sync;
• key compromise drills.

63.6 Arena tests

• rating integrity;
• matchmaking quality;
• queue abuse;
• smurfing/collusion;
• disconnect adjudication;
• replay evidence;
• prize settlement;
• policy eligibility;
• anti-cheat false positive/negative measurement;
• dispute workflows.

63.7 Store tests

• submission;
• malware scan;
• package install/repair/update;
• purchase;
• refund/chargeback;
• entitlement offline/online;
• regional price/tax;
• payout/split;
• item transfer;
• delisting;
• rollback;
• account recovery.

63.8 Pyramid tests

• controller-only navigation;
• suspend/resume;
• A/B update;
• recovery mode;
• thermal stress;
• power loss;
• storage failure;
• secure boot/attestation when available;
• DEV mode;
• node isolation;
• game performance profiles.

────────

64. Accessibility

64.1 Platform requirements

AXIOM Shell and DEV must support:

• remappable controls;
• keyboard-only and controller-only navigation;
• scalable text/UI;
• contrast and color controls;
• screen reader semantics;
• captions and subtitle styling;
• reduced motion;
• camera shake/motion blur controls;
• audio channel and dynamic-range controls;
• mono audio;
• speech-to-text and text-to-speech where available;
• input timing assistance;
• accessibility device APIs;
• clear focus and error messaging.

64.2 Engine support

The engine should expose reusable accessibility primitives so developers can implement:

• aim/target assistance;
• difficulty assists;
• hold/toggle options;
• timing windows;
• navigation cues;
• high-contrast modes;
• sound visualization;
• readable subtitles;
• content warnings;
• cognitive accessibility options.

64.3 Competitive policy

Arena must define which assists are allowed in each mode and avoid unnecessary exclusion. Input and accessibility settings must not be treated as cheating merely because they differ from defaults.

────────

65. Localization and Internationalization

AXIOM must support:

• Unicode;
• right-to-left layouts;
• plural/gender/grammar rules;
• locale-aware numbers, dates, currencies;
• font fallback;
• text expansion;
• subtitle/audio language packs;
• localized store/catalog;
• translation memory;
• voice and lip-sync variations;
• region-specific policy and ratings;
• test pseudolocalization;
• AXIOM AI-assisted translation with human review and provenance.

Project text must not be embedded only in code or textures without localization metadata.

────────

66. Content Moderation and Platform Safety

66.1 Scope

Moderation applies to:

• games and store listings;
• profiles and social messages;
• media;
• reviews;
• tokenized assets;
• creator packages;
• tournaments;
• future public creator content.

66.2 Controls

• reporting;
• block/mute;
• automated triage;
• human review;
• age/rating controls;
• prohibited-content policies;
• malware and scam detection;
• impersonation and IP complaints;
• appeals;
• evidence retention;
• transparency reporting where appropriate.

66.3 AI-generated content

Creators must have tools to disclose, trace, and review AI-generated assets. The platform must not assume AI generation resolves copyright, likeness, or consent issues.

────────

67. Live Operations and Release Management

67.1 Environments

Required environments:

• local;
• development;
• test;
• staging;
• production;
• Chain testnet/staging/mainnet;
• Store sandbox/production;
• Arena sandbox/production.

67.2 Release channels

• internal nightly;
• developer preview;
• alpha;
• beta;
• stable;
• long-term-support for enterprise where offered;
• emergency hotfix.

67.3 Feature flags

Feature flags require:

• owner;
• default;
• environments;
• user/region targeting;
• expiry/review date;
• audit;
• rollback behavior.

They must not become permanent undocumented forks.

67.4 Incident response

Production operations require:

• severity levels;
• on-call rotation;
• runbooks;
• communication templates;
• rollback and kill switches;
• chain/wallet emergency processes;
• security escalation;
• postmortems;
• corrective actions tracked to completion.

────────

68. Repository Architecture

68.1 Recommended monorepo

```text
axiom-xiii/
├── README.md
├── LICENSES/
├── SECURITY.md
├── CONTRIBUTING.md
├── CODEOWNERS
├── .github/
├── docs/
│   ├── vision/
│   ├── architecture/
│   ├── adr/
│   ├── rfc/
│   ├── requirements/
│   ├── security/
│   ├── legal/
│   ├── operations/
│   ├── api/
│   ├── formats/
│   └── roadmap/
├── apps/
│   ├── shell/
│   ├── dev-simple/
│   ├── dev-advanced/
│   ├── media/
│   ├── store-console/
│   ├── wallet/
│   └── admin/
├── engine/
│   ├── core/
│   ├── ecs/
│   ├── fabric/
│   ├── memory/
│   ├── reflection/
│   ├── serialization/
│   ├── platform/
│   ├── input/
│   ├── ui/
│   ├── render/
│   │   ├── nexus/
│   │   ├── photon/
│   │   ├── worldstream/
│   │   ├── optics/
│   │   ├── materials/
│   │   ├── atmosphere/
│   │   ├── water/
│   │   ├── vegetation/
│   │   ├── character/
│   │   └── fx/
│   ├── physics/
│   ├── animation/
│   ├── audio-orpheus/
│   ├── ai-runtime/
│   ├── navigation/
│   ├── networking/
│   ├── replay/
│   ├── persistence/
│   ├── flow/
│   ├── axir/
│   ├── axvm-experimental/
│   ├── packages/
│   ├── build/
│   └── devtools/
├── ai/
│   ├── prime/
│   ├── intent/
│   ├── planner/
│   ├── model-router/
│   ├── capability-broker/
│   ├── agents/
│   ├── gauntlet/
│   ├── memory/
│   ├── provenance/
│   └── evaluations/
├── connect/
│   ├── schema/
│   ├── native-sdk/
│   ├── cli/
│   ├── rpc/
│   ├── rest/
│   ├── websocket/
│   ├── mcp/
│   └── connector-sdk/
├── bridge/
│   ├── unreal/
│   ├── interchange/
│   └── future/
├── protocol/
│   ├── identity/
│   ├── game/
│   ├── asset/
│   ├── license/
│   ├── provenance/
│   ├── arena/
│   ├── store/
│   ├── wallet/
│   └── schemas/
├── chain/
│   ├── node/
│   ├── consensus/
│   ├── state/
│   ├── execution/
│   ├── native-modules/
│   ├── wallet-core/
│   ├── indexer/
│   ├── explorer/
│   ├── testnet/
│   └── simulation/
├── services/
│   ├── identity/
│   ├── social/
│   ├── media/
│   ├── projects/
│   ├── storage/
│   ├── builds/
│   ├── gameservers/
│   ├── matchmaking/
│   ├── arena/
│   ├── store/
│   ├── entitlements/
│   ├── payments/
│   ├── ledger/
│   ├── moderation/
│   ├── policy/
│   ├── telemetry/
│   └── support/
├── pyramid/
│   ├── virtual-target/
│   ├── os-linux/
│   ├── kernel-experimental/
│   ├── gpu-experimental/
│   ├── secure-transport-experimental/
│   ├── crypto/
│   ├── image-media/
│   ├── filesystem-experimental/
│   ├── firmware/
│   ├── controller/
│   ├── hardware-spec/
│   └── enclosure/
├── sdk/
│   ├── cpp/
│   ├── rust/
│   ├── flow/
│   ├── server/
│   ├── chain/
│   └── samples/
├── games/
│   ├── samples/
│   ├── engine-tests/
│   └── axiom-originals-adapters/
├── tools/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── fuzz/
│   ├── performance/
│   ├── visual/
│   ├── network/
│   ├── chain/
│   ├── security/
│   └── certification/
├── infra/
│   ├── local/
│   ├── development/
│   ├── staging/
│   ├── production/
│   └── disaster-recovery/
└── third_party/
    ├── manifests/
    ├── patches/
    └── notices/
```

68.2 Repository segmentation

Sensitive systems may later move to access-controlled repositories while preserving versioned interfaces:

• anti-cheat detection;
• ranking/fraud algorithms;
• production key/signing infrastructure;
• restricted AI models;
• wallet custody;
• PYRAMID secure boot;
• proprietary hardware/firmware.

68.3 Documentation as code

ADRs, RFCs, requirements, threat models, runbooks, schemas, and acceptance evidence live with versioned source.

────────

69. Coding and Architecture Standards

69.1 General

• explicit ownership and lifetime;
• bounded resource use;
• errors handled, not ignored;
• no secrets in source;
• no hidden network calls;
• deterministic tests;
• public APIs documented;
• unsafe/native boundary reviewed;
• dependencies justified;
• feature flags owned and expiring;
• schema migrations included;
• telemetry/privacy classified;
• accessibility considered;
• license/provenance recorded.

69.2 Architectural Decision Records

ADRs are mandatory for:

• language/toolchain changes;
• data format changes;
• public API changes;
• storage choice;
• consensus changes;
• cryptography changes;
• renderer architecture;
• kernel/driver changes;
• licensing enforcement;
• provider dependency;
• security trust-boundary changes.

69.3 API compatibility

Public SDKs use semantic versioning or an equivalent documented policy. Deprecations require migration guidance and a defined support window.

69.4 No direct cross-domain database access

Services communicate through APIs/events. Shared database tables must not become invisible coupling.

────────

70. CI/CD

70.1 Required pipelines

• pull-request validation;
• protected branch integration;
• nightly full Gauntlet;
• multi-platform builds;
• engine benchmarks;
• renderer reference images;
• network simulations;
• chain simulations;
• security scans;
• package/store certification;
• docs/schema generation;
• release signing;
• deployment;
• rollback verification.

70.2 Artifact promotion

Artifacts are built once and promoted across environments where possible. Rebuilding for production must remain reproducible and attributable.

70.3 Release signing

Signing occurs in isolated infrastructure. Developer agents and ordinary CI workers do not receive production signing keys.

70.4 Dependency bot

Dependency updates open reviewed changes with:

• changelog/security summary;
• license impact;
• API impact;
• tests;
• performance comparison;
• rollback.

────────

71. V1 Development Roadmap

This roadmap is milestone-driven. Calendar duration depends on team size, capital, model quality, and the scope held to each gate. AI can compress implementation, documentation, testing, and iteration, but it does not remove hardware, security, operations, user testing, or adversarial validation.

Phase 0 — Canonical foundation

Outcome: The organization can develop AXIOM without architectural drift.

Deliverables:

• approve this specification;
• establish company/IP ownership and contributor agreements;
• create monorepo and protected branches;
• define coding/security standards;
• establish ADR/RFC process;
• create requirements register and risk register;
• bootstrap CI;
• create initial AXIOM Connect schemas;
• define project format v0;
• define threat model v0;
• define cost/budget controls;
• identify reference hardware.

Exit gate:

• clean repository;
• reproducible hello-world build;
• signed development artifacts;
• baseline tests;
• no unresolved ownership of foundational code.

Phase 1 — Shell, project format, and native runtime skeleton

Deliverables:

• controller-first AXIOM Shell prototype;
• seven-tab navigation;
• account/profile local sandbox;
• .axiom project creation/open/save;
• project graph/index;
• native window/input/UI;
• ECS/Core/Fabric skeleton;
• basic renderer triangle/mesh/material/camera;
• asset import;
• build/package/launch;
• Simple/Advanced switch shell;
• source control integration;
• local logs/crash capture.

Exit gate:

• a sample native AXIOM project can be created, edited, built, installed in GAMES, and launched.

Phase 2 — AXIOM AI and development loop

Deliverables:

• Ask/Plan/Build;
• Intent Compiler;
• project context graph;
• planner/task DAG;
• model router;
• capability broker;
• core agents;
• branch/worktree isolation;
• Gauntlet v0;
• history/rollback;
• Simple mode chat + viewport;
• Advanced world/code/logic/test views;
• mode-switch continuity;
• provenance/license metadata.

Exit gate:

• a nontechnical tester can request a small playable game mechanic, approve the plan, build it, switch to Advanced, inspect/edit it, and return to Simple without conversion.

Phase 3 — Complete small-game engine path

Deliverables:

• world/scene/entity authoring;
• AXIOM Flow/AXIR;
• physics foundation;
• animation;
• ORPHEUS audio;
• UI/input;
• save/load;
• networking baseline;
• package/plugin system;
• profiler/debugger;
• Windows/Linux builds;
• dedicated server;
• 2D/2.5D path;
• one complete internal sample game.

Exit gate:

• external developers can complete and ship a small commercial-quality game through the documented path.

Phase 4 — High-fidelity renderer and world path

Deliverables:

• NEXUS clustered geometry;
• WORLDSTREAM;
• PHOTON baseline;
• OPTICS;
• high-end materials;
• atmosphere/weather/water/vegetation;
• character rendering;
• motion matching/IK foundation;
• GPU/CPU profiler;
• AAA reference scenes;
• quality/performance profiles;
• automated visual comparison.

Exit gate:

• a representative high-fidelity environment and character scene meets defined frame, memory, loading, and visual-quality targets on reference hardware.

Phase 5 — Unreal Bridge

Deliverables:

• .uproject inventory;
• license/provenance scan;
• asset conversion;
• material conversion;
• world conversion;
• C++ semantic analysis;
• Blueprint-to-Flow conversion subset;
• plugin compatibility report;
• Gauntlet migration suite;
• documentation and manual intervention UX.

Exit gate:

• selected reference projects convert with measured, category-specific compatibility and no silent data loss.

Phase 6 — Platform services

Deliverables:

• identity/auth;
• social/presence/parties;
• media capture/publishing;
• project cloud sync;
• Store sandbox;
• entitlements;
• payments sandbox;
• telemetry/support/moderation;
• live service deployment;
• developer portal integrated into DEV.

Exit gate:

• a developer can upload a build, certify it, purchase it with sandbox funds, install it, launch it, update it, and refund it.

Phase 7 — AXIOM Chain and Wallet

Deliverables:

• custom node;
• consensus test network;
• wallet core;
• native digital object modules;
• provenance/license modules;
• marketplace settlement;
• creator splits;
• explorer/indexer;
• managed/self-custody UX;
• audits and attack simulations;
• Store integration.

Exit gate:

• end-to-end mint, license, purchase, transfer, royalty, and recovery scenarios pass audit gates on the production candidate network.

Phase 8 — Arena and prize systems

Deliverables:

• matchmaking/rating;
• tournaments/brackets;
• result attestation;
• replay evidence;
• anti-cheat baseline;
• policy engine;
• sponsor-funded prize escrow/settlement;
• team/roster;
• dispute/support;
• Arena UI in GAMES/SOCIAL/PROFILE/WALLET.

Exit gate:

• a complete sponsored tournament can be created, played, verified, disputed, settled, and audited.

Phase 9 — PYRAMID virtual and physical prototype

Deliverables:

• Virtual Target;
• controller-first certification;
• Linux-based PYRAMID OS image;
• A/B updates and recovery;
• DEV mode on target;
• P0 enclosure prototype;
• thermal/acoustic testing;
• experimental kernel boot milestone;
• experimental GPU/secure transport/FS programs;
• fixed reference hardware profile.

Exit gate:

• P0/P1 reference hardware boots directly into AXIOM, plays native titles, opens DEV, builds a sample, and survives update/recovery and thermal tests.

Phase 10 — Public beta and V1 production

Deliverables:

• security audits;
• external developer cohort;
• store/catalog operations;
• customer support;
• moderation;
• production chain and wallet limits;
• Arena events;
• first AXIOM Originals content;
• incident response;
• legal/policy deployment profiles;
• metrics and reliability review.

Exit gate:

• all V1-PRODUCTION requirements and launch gates pass.

────────

72. Parallel Workstreams

The following must begin early but remain non-blocking until their gates:

• PYRAMID Kernel;
• AXIOM GPU;
• AXIOM Secure Transport;
• AXIOM Crypto implementation;
• AXIOM Image/Media codecs;
• AXIOM FS;
• AXVM;
• advanced chain contracts;
• 10,000-plus-player shard research;
• distributed PYRAMID compute;
• custom hardware/firmware;
• internal AI model training.

Each workstream requires:

• owner;
• threat/performance model;
• reference implementation;
• conformance tests;
• benchmark baseline;
• replacement gate;
• kill or pause criteria.

────────

73. Team and Ownership Model

73.1 Core leadership

• Founder/Product/Creative Director — Ø;
• Chief Architect;
• VP/Lead Engine;
• Lead AI/Agents;
• Lead Rendering;
• Lead Online/Services;
• Lead Blockchain/Wallet;
• Lead Security;
• Lead Product/UX;
• Lead PYRAMID OS/Hardware;
• Legal/IP/Regulatory lead or external counsel;
• Production/Program lead.

73.2 Initial engineering groups

1. Core/ECS/Fabric/Build;
2. Shell/UI/DEV UX;
3. AXIOM AI/Connect/Gauntlet;
4. Renderer/World/Animation/Audio;
5. Networking/Arena/Game servers;
6. Chain/Wallet/Marketplace;
7. Cloud/Store/Social/Media;
8. Security/Anti-cheat/Infrastructure;
9. Bridge/Interoperability;
10. PYRAMID OS/Kernel/Hardware research;
11. QA/Automation/Performance;
12. Developer Relations/Documentation.

73.3 Code ownership

Every directory has named human code owners. AI agents never become the sole owner or approver of a critical system.

73.4 Contractor isolation

Contractors receive only required repositories, data, and secrets. Foundational IP, anti-cheat, wallet custody, signing, and kernel/security internals require stronger agreements and access controls.

────────

74. First-Party Validation Through AXIOM Originals

The ten-game slate should validate the platform without forcing all ten into simultaneous full production. Working titles remain subject to clearance.

|Project                        |AXIOM systems stressed                                                                                            |
|-------------------------------|------------------------------------------------------------------------------------------------------------------|
|**UNDERSCRIPT: YOKAI**         |Large world, NEXUS, WORLDSTREAM, creature AI, transformations, co-op/PvP, evolution/fusion, high-fidelity fantasy.|
|**MACHINA: GHOST OF THE SOUND**|Graphite renderer profile, ORPHEUS, music-reactive worlds, traversal, cinematic presentation.                     |
|**STARHEIRS**                  |2D/2.5D pipeline, family progression, celestial state changes, local/online co-op.                                |
|**ECHOS OF THE ETERNAL**       |Card/tactical/fighting hybrid, deterministic rules, rollback/action transitions, marketplace/tournaments.         |
|**VOLT//KIN**                  |Modular partners, evolution, parts/inventory, party RPG, data-heavy customization.                                |
|**ZERO GRACE: TRINITY**        |Social/calendar simulation, dialogue, relationships, adaptive music, consequence graphs.                          |
|**ZARION: THE FORSAKEN**       |High-speed action, animation, combat timing, cinematic bosses, performance.                                       |
|**LEADBREAK**                  |2D anime platform fighting, rollback, map editor when later approved, community/custom matches.                   |
|**AFTER//MEMORY**              |Colossal horror, extreme atmosphere, OPTICS, memory systems, large creatures.                                     |
|**SOVEREIGN CONSEQUENCE**      |Macro simulation, causality, RTS networking, avatar action, large multiplayer.                                    |

The first-party portfolio is a test matrix and ecosystem strategy. It is not permission to dilute the engine roadmap with ten simultaneous content productions.

────────

75. V1 Risk Register

75.1 Scope collapse

Risk: Attempting engine, AI, chain, store, Arena, OS, kernel, drivers, hardware, and ten games simultaneously prevents any one product from becoming reliable.

Mitigation: maturity classes, phase gates, non-blocking research streams, one complete sample game before broad expansion, ruthless acceptance criteria.

75.2 AI-generated technical debt

Risk: Parallel agents produce inconsistent code, duplication, security flaws, and unreadable systems.

Mitigation: requirements first, architecture ownership, typed APIs, isolated branches, Integrator, Gauntlet, human code owners, complexity budgets.

75.3 Renderer ambition

Risk: AAA visual target consumes all resources before the platform can ship.

Mitigation: complete small-game path first; build renderer in measured capabilities; maintain quality and scalable paths; first-party reference scenes.

75.4 Blockchain/security loss

Risk: Exploit, key compromise, contract bug, validator failure, or fraud causes irreversible loss.

Mitigation: narrow native modules, curated validator launch, limits, audits, multisig/HSM, bug bounty, staged value, emergency process, no bridge dependency.

75.5 Prize-system legal and fraud risk

Risk: Skill competitions are treated differently across regions or manipulated.

Mitigation: modular policy/operator layer, sponsor-funded launch, verification, geolocation/identity where required, rules, evidence, dispute process, counsel.

75.6 IP leakage or engine cloning

Risk: Source access and AI expose proprietary internals or allow a competing engine fork.

Mitigation: source-available license, access segmentation, agent context separation, contractual controls, watermark/provenance where appropriate, restricted repos, trademarks and patents where useful.

75.7 Creator distrust

Risk: Excessive control, opaque fees, lock-in, wallet confusion, or rights grabs prevent adoption.

Mitigation: creator ownership promise, transparent agreements, exportable projects, clear economics, ordinary non-blockchain path, human-readable licensing, appeals.

75.8 Unreal conversion expectations

Risk: Users expect one-click perfect conversion of proprietary engine-specific projects.

Mitigation: category-specific compatibility report, no misleading percentages, license scan, explicit unsupported items, migration adapters, measured corpus.

75.9 Kernel/driver diversion

Risk: foundational teams spend years on low-value replacements before product-market proof.

Mitigation: experimental workstreams with strict resource caps and replacement gates; production uses proven layers until AXIOM alternatives win objectively.

75.10 Platform moderation and abuse

Risk: Social, media, tokenized assets, and marketplace attract scams, harassment, malware, and stolen content.

Mitigation: moderation tooling, package sandboxing, provenance, reporting, human review, seller verification, fraud monitoring, clear policies.

75.11 Hardware capital and supply chain

Risk: Custom console manufacturing consumes capital and introduces inventory, warranty, certification, and component risk.

Mitigation: protocol/software first; P0/P1 commodity components; preorder or controlled pilots only after validated demand; modular design and supply alternatives.

75.12 Single-provider capture

Risk: external AI/cloud/payment/provider changes terms or access.

Mitigation: model router, local models, multi-cloud, self-host, payment abstraction, native chain, portable data, provider contracts.

────────

76. V1 Production Acceptance Criteria

AXIOM-XIII V1 is not production-ready until all applicable criteria pass.

76.1 Shell

• seven-tab navigation implemented exactly;
• controller-only end-to-end navigation passes;
• keyboard/mouse passes;
• account switching/privacy passes;
• updates, repair, and rollback pass;
• accessibility baseline passes.

76.2 Native project

• create/open/save/migrate .axiom projects;
• Git-friendly source and stable IDs;
• project graph rebuilds from canonical files;
• corrupted cache does not destroy source;
• project packages and dependencies lock reproducibly.

76.3 Simple/Advanced

• same project and data;
• switch mid-task and mid-project;
• AI-generated code/graphs inspectable;
• manual edits understood by Simple mode;
• Ask is read-only;
• Plan does not implement;
• Build respects consequence tiers and approval;
• rollback works.

76.4 AXIOM AI

• model/provider swap tested;
• local/private mode tested;
• parallel agents isolated;
• cost and iteration limits enforced;
• prompt injection tests pass;
• no secret exposure;
• Gauntlet evidence produced;
• uncertainty and failure reported honestly;
• publish/value actions require strong approval.

76.5 Engine

• complete small game can ship;
• Windows/Linux client and server builds;
• rendering, physics, animation, audio, UI, save, networking stable;
• crash recovery and diagnostics;
• plugin/package security;
• performance budgets measured;
• 2D/2.5D and 3D samples pass.

76.6 AAA path

• high-fidelity reference scene meets published reference-hardware targets;
• NEXUS/WORLDSTREAM/PHOTON/OPTICS baseline operational;
• quality/performance profiles switch correctly;
• no unacceptable traversal hitches;
• visual regression suite stable;
• large creature/character scene tested.

76.7 Unreal Bridge

• supported reference corpus converted;
• license/provenance scan works;
• unsupported items visible;
• no silent asset/code deletion;
• conversion branch and rollback;
• measured category report.

76.8 Services and Store

• identity, social, media, Store, Profile, Wallet integrated;
• purchase/install/launch/update/refund/repair;
• developer submission and payout sandbox;
• entitlement offline policy;
• moderation/support;
• disaster recovery drill.

76.9 Chain and Wallet

• independent audits completed;
• consensus fault tests;
• mint/transfer/license/royalty/marketplace/prize modules pass invariants;
• managed and self-custody recovery tested;
• signing UX reviewed;
• high-value limits and incident controls;
• no sensitive personal data on-chain.

76.10 Arena

• skill matchmaking metrics acceptable;
• tournament creation through settlement;
• replay/evidence and dispute;
• anti-cheat baseline;
• sponsored prize pool successfully settled;
• policy engine enforcement;
• no known critical integrity defects.

76.11 Security

• threat models current;
• external penetration test;
• chain/wallet audit;
• secrets/key review;
• supply-chain review;
• incident exercise;
• vulnerability disclosure/bug bounty ready;
• critical findings remediated.

76.12 PYRAMID

• Virtual Target usable;
• Linux-based OS image boots reference hardware;
• controller shell, GAMES, DEV, STORE, WALLET work;
• update/recovery passes;
• P0/P1 thermal and acoustic test passes;
• experimental kernel milestone documented without being a production dependency.

────────

77. Launch Gates

Gate A — Architecture

No critical domain lacks an owner, interface, threat model, tests, or migration policy.

Gate B — Product

New users can play and build without core-team intervention.

Gate C — Developer

External developers can complete, package, publish, update, and support a game.

Gate D — Security

No unresolved critical security finding; key, wallet, chain, store, and agent boundaries reviewed.

Gate E — Economic

Funds, assets, royalties, refunds, prize settlements, and records reconcile under failure and dispute scenarios.

Gate F — Operations

Monitoring, support, moderation, incident response, backups, and rollback are staffed and tested.

Gate G — Legal/Policy

Public terms, licenses, store rules, Arena rules, token disclosures, privacy, and operator policies are approved for launch regions/operators.

Gate H — Performance

Reference projects meet frame, memory, loading, network, chain, service, and editor targets.

Gate I — Hardware readiness

Required only for a physical PYRAMID launch, not desktop V1.

────────

78. Requirements Register

The following are the minimum traceable master requirements. Detailed child requirements must be created during implementation.

|ID         |Requirement                                                                                                       |Class          |
|-----------|------------------------------------------------------------------------------------------------------------------|---------------|
|AX-PROD-001|AXIOM shall ship first as a controller-first desktop console environment.                                         |V1-PRODUCTION  |
|AX-PROD-002|Top navigation shall be GAMES, MEDIA, SOCIAL, DEV, STORE, PROFILE, WALLET.                                        |V1-PRODUCTION  |
|AX-PROD-003|There shall be no separate CREATE tab in V1.                                                                      |V1-PRODUCTION  |
|AX-DEV-001 |DEV shall provide Simple and Advanced modes over one project.                                                     |V1-PRODUCTION  |
|AX-DEV-002 |Users shall switch modes mid-project without conversion.                                                          |V1-PRODUCTION  |
|AX-AI-001  |Simple mode shall be chat-first with AXIOM AI.                                                                    |V1-PRODUCTION  |
|AX-AI-002  |AXIOM AI shall expose Ask, Plan, and Build states.                                                                |V1-PRODUCTION  |
|AX-AI-003  |AXIOM AI shall use requirement-first planning, parallel agents, and Gauntlet loops.                               |V1-PRODUCTION  |
|AX-AI-004  |External agents shall not be runtime dependencies.                                                                |V1-PRODUCTION  |
|AX-AI-005  |Models/providers shall be replaceable.                                                                            |V1-PRODUCTION  |
|AX-AI-006  |Agent actions shall be permissioned, audited, reversible where possible, and branch-scoped.                       |V1-PRODUCTION  |
|AX-FMT-001 |AXIOM shall create and save native `.axiom` projects.                                                             |V1-PRODUCTION  |
|AX-FMT-002 |Canonical project data shall be inspectable and Git-friendly.                                                     |V1-PRODUCTION  |
|AX-FMT-003 |AXIOM shall maintain a semantic project graph rebuildable from source.                                            |V1-PRODUCTION  |
|AX-BRG-001 |AXIOM shall analyze and import legally portable Unreal projects/code/assets.                                      |V1-PRODUCTION  |
|AX-BRG-002 |Unreal conversion shall produce category-specific compatibility and license reports.                              |V1-PRODUCTION  |
|AX-ENG-001 |AXIOM shall run native 3D and 2D/2.5D projects.                                                                   |V1-PRODUCTION  |
|AX-ENG-002 |AXIOM shall support Windows and Linux client builds and Linux dedicated servers.                                  |V1-PRODUCTION  |
|AX-ENG-003 |Engine APIs shall not permanently expose replaceable third-party implementation types.                            |V1-PRODUCTION  |
|AX-REN-001 |Renderer architecture shall target contemporary AAA world scale and visual fidelity.                              |V1-PRODUCTION  |
|AX-REN-002 |NEXUS clustered virtual geometry baseline shall ship.                                                             |V1-PRODUCTION  |
|AX-REN-003 |PHOTON dynamic lighting baseline shall ship.                                                                      |V1-PRODUCTION  |
|AX-REN-004 |WORLDSTREAM shall support large hierarchical streamed worlds.                                                     |V1-PRODUCTION  |
|AX-REN-005 |OPTICS shall provide physical/stylized camera controls.                                                           |V1-PRODUCTION  |
|AX-AUD-001 |ORPHEUS shall provide adaptive audio/music graphs.                                                                |V1-PRODUCTION  |
|AX-NET-001 |AXIOM shall support authoritative, rollback, strategy, async, and offline profiles.                               |V1-PRODUCTION  |
|AX-NET-002 |Large-shard cell architecture shall be designed for future 10,000-plus logical participants.                      |V1-ARCHITECTED |
|AX-CHN-001 |AXIOM shall implement its own game-native blockchain node and state model.                                        |V1-PRODUCTION  |
|AX-CHN-002 |AXIOM Chain shall support digital objects/NFTs, licenses, provenance, royalties, marketplace, and prize escrow.   |V1-PRODUCTION  |
|AX-CHN-003 |General unrestricted contracts shall remain Preview until audited.                                                |V1-PREVIEW     |
|AX-WAL-001 |Wallet shall support managed and self-custodial paths.                                                            |V1-PRODUCTION  |
|AX-ARN-001 |Arena shall support skill matchmaking, ranked play, tournaments, replays, and prize pools.                        |V1-PRODUCTION  |
|AX-ARN-002 |Sponsored prize pools shall be the first production real-value tournament profile.                                |V1-PRODUCTION  |
|AX-ARN-003 |Player-funded/token competition shall be policy-gated.                                                            |V1-PREVIEW     |
|AX-STO-001 |AXIOM shall control official Store policies, certification, payments, discovery, and enforcement.                 |V1-PRODUCTION  |
|AX-LIC-001 |Creators shall own original game IP while AXIOM retains AXIOM technology ownership.                               |V1-PRODUCTION  |
|AX-LIC-002 |Core engine shall use a proprietary/source-available licensing strategy, not permissive open source by default.   |V1-PRODUCTION  |
|AX-SEC-001 |Secrets shall never be exposed to unscoped agents or project files.                                               |V1-PRODUCTION  |
|AX-SEC-002 |Production packages, builds, updates, and chain modules shall be signed.                                          |V1-PRODUCTION  |
|AX-PYR-001 |V1 shall include a PYRAMID Virtual Target.                                                                        |V1-PRODUCTION  |
|AX-PYR-002 |Production PYRAMID OS shall initially use a hardened Linux base.                                                  |V1-ARCHITECTED |
|AX-PYR-003 |PYRAMID Kernel shall exist as a V1 experimental implementation.                                                   |V1-EXPERIMENTAL|
|AX-PYR-004 |AXIOM GPU, secure transport, crypto implementation, codecs, and filesystem replacement programs shall exist in V1.|V1-EXPERIMENTAL|
|AX-PYR-005 |Physical PYRAMID shall support PLAY, DEV, and optional NODE modes.                                                |V1-ARCHITECTED |
|AX-IP-001  |Every asset/package shall retain provenance and license metadata.                                                 |V1-PRODUCTION  |
|AX-IP-002  |Mechanics Registry and Originality Firewall shall be required for first-party games.                              |V1-PRODUCTION  |
|AX-QA-001  |Every accepted Build shall produce a Gauntlet evidence package.                                                   |V1-PRODUCTION  |
|AX-QA-002  |Critical platform systems shall undergo independent security review before value is at risk.                      |V1-PRODUCTION  |

────────

79. Initial Implementation Backlog

The first implementation program should open at least the following epics.

Foundation

1. Establish monorepo, ownership, branch protection, CI, security policies.
2. Create ADR/RFC/requirements tooling.
3. Define AXIOM IDs and schema conventions.
4. Define .axiom v0 manifest and project layout.
5. Implement local project registry.
6. Implement logging, errors, config, feature flags, crash IDs.
7. Implement package/signing development keys.
8. Build basic SBOM/provenance pipeline.

Shell

9. Controller-first shell frame.
10. Seven locked tabs.
11. Home dashboard.
12. Local profile/account sandbox.
13. GAMES library and install manifest.
14. DEV mode routing.
15. STORE sandbox shell.
16. WALLET sandbox shell.
17. accessibility and input navigation baseline.

Engine

18. Platform/window/input abstraction.
19. Core ECS v0.
20. FABRIC scheduler v0.
21. Reflection/schema generator v0.
22. serialization/migration v0.
23. asset database and importer v0.
24. renderer frame graph and mesh/material/camera v0.
25. scene/world/entity authoring v0.
26. UI runtime v0.
27. build/package/launch v0.
28. physics adapter v0.
29. animation/audio/save/network baselines.

DEV and AI

30. Simple conversation/viewport shell.
31. Advanced project/world/code/logic shell.
32. shared selection/context across modes.
33. AXIOM Connect capability schema v0.
34. PRIME service v0.
35. Intent Compiler v0.
36. Planner/task graph v0.
37. model router v0.
38. capability broker and permissions.
39. agent sandbox/worktree runner.
40. Gauntlet v0.
41. project graph/index v0.
42. change/evidence package v0.
43. Ask/Plan/Build enforcement.

Unreal Bridge

44. .uproject inventory parser.
45. dependency/plugin/license inventory.
46. source asset importer.
47. material/world conversion prototype.
48. C++/Blueprint semantic analyzer prototype.
49. compatibility report UI.

Platform

50. identity/auth service.
51. social/presence/party service.
52. project object storage/sync.
53. media capture and replay metadata.
54. store/catalog/entitlement sandbox.
55. payment/ledger sandbox.
56. telemetry and support baseline.
57. policy engine v0.

Chain and Arena

58. chain specification/RFC.
59. consensus simulation.
60. node/state/execution skeleton.
61. wallet core and signing UI.
62. digital object/license/royalty modules.
63. marketplace settlement module.
64. tournament escrow/result module.
65. matchmaker/rating prototype.
66. replay/evidence pipeline.
67. sponsored tournament end-to-end sandbox.

Renderer/AAA

68. NEXUS cluster builder/runtime prototype.
69. WORLDSTREAM cell/page system.
70. PHOTON direct/dynamic indirect baseline.
71. OPTICS camera pipeline.
72. high-end material and atmosphere reference scene.
73. performance/visual regression harness.

PYRAMID

74. Virtual Target profile and validator.
75. Linux-based OS image prototype.
76. controller boot-to-shell prototype.
77. P0 enclosure CAD/thermal study.
78. PYRAMID Kernel bootloader/memory/scheduler experiment.
79. AXIOM GPU research harness.
80. secure transport/crypto/image/FS experimental repositories and tests.

────────

80. Mandatory Open ADRs Before Major Implementation

The following decisions require formal ADRs rather than ad hoc agent choices:

1. Exact ownership/entity structure for AXIOM IP and protocol.
2. Core C++/Rust boundary and build toolchain.
3. .axiom manifest and schema language.
4. AXIR format and execution backend.
5. UI shell bootstrap technology and migration to AXIOM UI.
6. ECS storage model.
7. renderer backend order and shader toolchain.
8. production physics dependency and replacement interface.
9. production audio backend and plugin-hosting sandbox.
10. networking transport and dedicated server orchestration.
11. Chain consensus algorithm/profile.
12. Chain state model and contract/runtime strategy.
13. native token necessity and economics.
14. managed wallet custody model.
15. Store payment providers and ledger boundaries.
16. Arena rating and prize policy profiles.
17. production cloud/storage/database stack.
18. source-available license structure and economic thresholds.
19. PYRAMID P1 reference hardware class.
20. PYRAMID OS distribution/base.
21. kernel architecture/boot target.
22. anti-cheat privilege level.
23. privacy and telemetry defaults.
24. first AXIOM Original used as the engine reference game.
25. public names/trademark clearance for AXIOM-XIII and PYRAMID.

────────

81. Bootstrap Execution Brief for the Initial Build Team or External Orchestrator

The following instruction can be given to an authorized bootstrap agent or team. It does not make that external tool a dependency of AXIOM-XIII.

Mission

Create the production repository, documentation system, issue structure, schemas, CI skeleton, and first executable foundation for AXIOM-XIII V1 exactly according to this specification.

Rules

1. Treat this document as the primary source of truth.
2. Do not silently reduce AXIOM to an Unreal plugin or launcher.
3. Do not make Unreal a runtime dependency; Unreal is an import/translation bridge.
4. Do not add a CREATE top-level tab.
5. Preserve GAMES, MEDIA, SOCIAL, DEV, STORE, PROFILE, WALLET.
6. DEV must have Simple and Advanced over the same .axiom project.
7. AXIOM AI must be custom, model-agnostic, and use Ask/Plan/Build, parallel agents, and Gauntlet loops.
8. No external orchestration product may become a shipping dependency.
9. Include Chain, Arena, Wallet, Store, PYRAMID Virtual Target, and proprietary replacement programs in the repository from V1.
10. Mark experimental systems honestly; do not route production money or security through unaudited implementations.
11. Use established cryptographic primitives; do not invent unreviewed cryptography.
12. Keep creators’ original project IP separate from AXIOM technology ownership.
13. Every change requires tests, provenance, license metadata, and documentation.
14. Do not commit secrets or credentials.
15. Do not implement all epics at once. Build dependency order and phase gates.
16. Create ADRs for all mandatory open decisions instead of guessing.
17. Return contradictions, risks, and unresolved decisions explicitly.
18. Use main, staging, and develop protected branches plus short-lived working branches.
19. All generated source must be readable, tested, documented, and assigned a human owner.
20. Stop before irreversible production deployment, legal commitments, token issuance, custody, prize-money activation, or public release without authorized approval.

First delivery package

The bootstrap team must deliver:

• exact repository tree;
• working build instructions;
• architecture map;
• ADR/RFC templates;
• requirements register;
• threat model v0;
• license/provenance policy v0;
• CI pipeline;
• AXIOM Connect schema v0;
• .axiom project schema v0;
• shell executable with locked navigation;
• native hello-world .axiom project;
• Simple/Advanced mode shell;
• AXIOM AI Ask/Plan/Build stub with permissions;
• Gauntlet v0;
• Chain, Arena, Bridge, and PYRAMID skeletons;
• first 100 implementation tickets with dependencies and acceptance criteria;
• risk register and estimated resource plan;
• evidence that the project builds from a clean environment.

────────

82. Definition of Done for This Specification

This specification is considered adopted when:

• Ø approves it as the V1 source of truth;
• contradictions with prior Unreal-first documents are marked superseded;
• the repository is created from its architecture;
• all mandatory ADRs are opened;
• requirements are imported into project tracking;
• owners are assigned;
• the first Foundation milestone is planned;
• legal counsel begins the licensing/entity/title clearance work;
• the first executable shell and .axiom project are placed under CI.

────────

83. Final Product Doctrine

AXIOM-XIII should not compete by being a cheaper copy of an existing engine or a stranger version of an existing console.

Its defining advantages are the integration of:

• full-scale native game development;
• a chat-first but non-restrictive AI interface;
• professional direct control;
• semantic, inspectable projects;
• automated parallel development and adversarial verification;
• a game-native blockchain and creator economy;
• skill-based competition and prize settlement;
• controlled distribution and licensing;
• a console-like software environment available before hardware;
• an eventual physical machine on which games can be both played and built;
• first-party games that prove radically different parts of the platform.

The operating principle is:

> **Play worlds. Build worlds. Own what is yours. Compete on skill. Publish under your terms. Let AXIOM handle the impossible infrastructure without taking the creator’s soul out of the work.**

────────

Appendix A — Glossary

AXIOM-XIII — The complete platform and product family.
AXIOM Shell — Controller-first desktop/console user environment.
AXIOM Engine — Native game runtime/editor foundation.
AXIOM AI — User-facing AI development intelligence.
PRIME — Internal AXIOM AI orchestrator.
Gauntlet — Automated implementation, adversarial verification, repair, and evidence loop.
AXIOM Connect — Typed APIs and capability interface for tools, agents, plugins, and services.
AXIOM Bridge — Import/translation framework, beginning with Unreal.
.axiom — Native AXIOM project manifest/format family.
AXIOM Flow — Prompt + node + code gameplay authoring system.
AXIR — Semantic intermediate representation.
AXVM — Experimental proprietary execution virtual machine.
AXIOM CORE — Runtime foundation and object model.
AXIOM FABRIC — Job graph and scheduler.
NEXUS — Virtualized geometry and GPU-driven visibility.
PHOTON — Hybrid illumination/reflection/path-tracing system.
WORLDSTREAM — Hierarchical world and asset streaming.
OPTICS — Physical/stylized camera and image pipeline.
ORPHEUS — Audio, spatial sound, and interactive music engine.
AXIOM Protocol — Shared semantic object/event definitions.
AXIOM Chain — Custom game-native blockchain.
AXIOM Arena — Skill matchmaking, competition, tournament, replay, and prize infrastructure.
AXIOM Store — Official controlled distribution and marketplace.
AXIOM Wallet — Financial, token, prize, royalty, and ownership interface.
PYRAMID — Future dedicated AXIOM computer-console hardware and operating environment.
PYRAMID Virtual Target — Software-defined future hardware performance/certification target.
PYRAMID Kernel — Experimental future proprietary kernel.
AXIOM Original — First-party title used to validate and strengthen AXIOM.

────────

Appendix B — Status of Prior Decisions

|Prior direction                            |V1 status                                                                                             |
|-------------------------------------------|------------------------------------------------------------------------------------------------------|
|AXIOM built primarily on Unreal            |**SUPERSEDED.** AXIOM is an independent engine; Unreal is a Bridge/import target.                     |
|Separate CREATE tab                        |**SUPERSEDED.** Creation is inside DEV Simple/Advanced.                                               |
|Manus as platform agent                    |**SUPERSEDED.** AXIOM AI/PRIME is native; external agents are bootstrap clients only.                 |
|Blockchain/NFTs optional and peripheral    |**SUPERSEDED.** AXIOM Chain, digital objects, prize settlement, and creator economics are first-class.|
|Public Forge in V1                         |**DEFERRED.** Internal authoring exists; player modding/Forge is not a V1 product requirement.        |
|PYRAMID hardware first                     |**SUPERSEDED.** Protocol and desktop software precede hardware.                                       |
|Mature dependencies used forever           |**SUPERSEDED.** V1 includes replacement abstractions and experimental proprietary workstreams.        |
|Every proprietary replacement must block V1|**REJECTED.** Experimental replacements are not production dependencies until qualified.              |
|AAA visuals as future wish                 |**SUPERSEDED.** AAA-scale rendering is an explicit architecture and acceptance target.                |

────────

Appendix C — Suggested Document Set Generated From This Master Specification

The repository should split this master document into maintained implementation documents after adoption:

1. Product Requirements Document;
2. System Architecture;
3. AXIOM AI and Gauntlet Specification;
4. Engine Runtime Specification;
5. Renderer/NEXUS/PHOTON/WORLDSTREAM/OPTICS Specification;
6. ORPHEUS Audio Specification;
7. Networking and Large-Shard Specification;
8. AXIOM Chain Protocol and Threat Model;
9. Wallet/Custody Specification;
10. Arena/Matchmaking/Prize Specification;
11. Store/Entitlement/Payments Specification;
12. Shell/UX Design System;
13. .axiom Format and Schema Specification;
14. AXIOM Connect API Specification;
15. Unreal Bridge Compatibility Specification;
16. Licensing and IP Control Plan;
17. Security Architecture and Incident Response;
18. PYRAMID Virtual Target and Hardware Roadmap;
19. PYRAMID Kernel Research Specification;
20. QA/Gauntlet/Performance Test Plan;
21. Operations/SRE/Disaster Recovery Plan;
22. Developer Documentation and SDK Plan;
23. Release and Certification Manual;
24. First-party AXIOM Originals Validation Matrix.

These derived documents must not contradict this master specification without an approved ADR/RFC that updates the master source of truth.