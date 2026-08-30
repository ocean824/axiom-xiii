# AXIOM AI Domain Specification

## 1. Purpose and Doctrine

The AXIOM AI domain represents the intelligent orchestration layer of the AXIOM-XIII interactive computing platform. It is designed to act as the primary interface for game creation, project management, and automated verification within the DEV environment. The foundational premise is that creators can direct the engine through natural language, visual references, and high-level intents, while AXIOM AI translates these into precise, executable changes within a structured project graph. This domain fundamentally shifts the paradigm of game development from manual, repetitive engineering tasks to intent-driven, requirement-focused orchestration, empowering both non-technical creators and professional developers.

Crucially, AXIOM AI is **not** an uncontrolled generative black box. It operates strictly within a requirement-first planning paradigm, enforcing consequence tiers, explicit permissions, resource budgets, and rigorous verification through the Gauntlet loop. It must never silently alter project canon, commit secrets, bypass licensing, or publish without authorization. AXIOM AI ensures that the resulting `.axiom` project is indistinguishable in quality, maintainability, and structural integrity from one built manually by a professional engineering team. The system is designed to provide explainability for every action, ensuring that creators understand what changed, why it changed, and how to revert or modify the outcome.

As dictated by the Owner Directive, AXIOM AI and its associated subsystems (PRIME, Gauntlet, Intent Compiler, parallel agents) are mandatory `V1-BUILD-REQUIRED` scope. No component may be deferred to a later release, although activation may be gated by policy, jurisdiction, or security constraints. The directive explicitly overrides any prior categorization of these capabilities as "future" or "experimental," mandating their full implementation, integration, and testing within the V1 release program.

## 2. Domain Boundaries and Scope

The AXIOM AI domain is bounded by the following responsibilities and interfaces:

- **In-Scope:** Intent compilation, requirement extraction, project context maintenance, task planning, capability routing (Model Router), parallel agent orchestration (PRIME), execution within isolated sandboxes, verification and testing (Gauntlet), memory and provenance tracking (Archivist), and human-in-the-loop approval management. This includes the enforcement of consequence tiers and the Ask/Plan/Build action states.
- **Out-of-Scope (Interfaces with other domains):** AXIOM AI does not directly modify the filesystem or engine internals. It must interact with the AXIOM Engine, AXIOM Services, and AXIOM Chain exclusively through the typed interfaces of **AXIOM Connect**. It does not own the ultimate source of truth for project data; it operates on the Semantic Project Graph, which reflects the canonical file-based `.axiom` project. The domain relies on the underlying engine for rendering, physics, and networking execution, focusing solely on the generation, orchestration, and verification of the logic and assets that drive those systems.

## 3. Personas and Actors

The AXIOM AI domain serves a diverse set of users, each with distinct interaction patterns and requirements:

- **Chat-First Creator:** Uses AXIOM AI in DEV Simple mode to build games through conversation, approving plans and reviewing test results without manual engine manipulation. This user relies heavily on the Intent Compiler to translate high-level goals into actionable plans and depends on the Gauntlet to ensure the resulting game is functional and performant.
- **Technical Game Developer:** Uses DEV Advanced mode, leveraging AXIOM AI for context-aware assistance, inline code generation, architecture review, and test generation while retaining direct control over the engine. This user requires high-fidelity, inspectable outputs (e.g., AXIR, shader source) and the ability to seamlessly switch between AI-assisted and manual workflows.
- **Studio Team:** Relies on AXIOM AI to enforce project policies, manage branches, conduct semantic merges, and operate within defined resource budgets and consequence tiers. This group utilizes the Archivist for provenance tracking and the Integrator for managing parallel development efforts.
- **AXIOM Internal Engineer:** Configures AXIOM AI policies, integrates new capability models, and reviews Gauntlet adversarial simulations. This persona is responsible for the ongoing maintenance and security of the PRIME orchestration layer and the Model Router.

## 4. Architecture and Named Components

The AXIOM AI domain is composed of several tightly integrated subsystems, designed to provide a robust, scalable, and secure AI orchestration environment.

### 4.1 PRIME (Director)
The central orchestrator of AXIOM AI. PRIME is a service (primarily implemented in Rust) that manages user intent, resource budgets, permissions, and the overall plan graph. It delegates tasks to specialized agents and is responsible for escalating issues to the user and finalizing change sets for review. PRIME ensures that all actions adhere to the configured consequence tiers and project policies.

### 4.2 Intent Compiler
Converts natural language, images, audio, and other multimodal inputs into structured intent. It extracts goals, constraints, performance expectations, security classifications, and licensing implications. It strictly differentiates between mandatory requirements ("must") and exploratory suggestions ("could"). The Intent Compiler is the critical first step in the requirement-first planning process, ensuring that AXIOM AI understands the *why* before determining the *how*.

### 4.3 Requirement-First Planner
Internalizes the CodeSpring-style planning discipline. It resolves goals, extracts constraints, defines acceptance tests *before* implementation, decomposes work into a dependency-aware task graph, and assigns tasks to appropriate agents. The Planner ensures that complex tasks are broken down into manageable, verifiable units of work, preventing runaway generation and ensuring traceability.

### 4.4 Model Router
A dynamic routing system that selects the appropriate underlying LLM or capability provider based on benchmark history, task type, context length, privacy classification, cost ceiling, latency, and tool support. It ensures AXIOM AI remains model-agnostic and supports fallback/quorum strategies for high-risk operations. The Model Router is essential for maintaining platform independence and optimizing resource utilization.

### 4.5 Parallel Agent System
A registry of specialized, capability-based agents that execute tasks concurrently within isolated sandboxes. Key agents include:
- **ARCHITECT:** System design, interfaces, ADRs, schema impact.
- **PLANNER:** Task decomposition, test plans, execution order.
- **BUILDER:** Code, tool, and service implementation.
- **ATLAS:** World, terrain, and spatial validation.
- **FORGE:** Asset generation, processing, and metadata.
- **MOTION:** Rigging, animation graphs, and IK.
- **MAESTRO:** Audio, music, and mixing.
- **NETWORK:** Replication, transport, and session management.
- **CHAIN:** Blockchain modules, transactions, and economic invariants.
- **SENTINEL:** Adversarial security, fuzzing, and QA.
- **PLAYER:** Automated playtesting and telemetry collection.
- **PERF:** Performance profiling and budget enforcement.
- **REVIEWER:** Specification conformity and licensing checks.
- **INTEGRATOR:** Semantic merges and conflict resolution.
- **ARCHIVIST:** Durable memory, provenance, and documentation updates.
- **RELEASE:** Packaging, signing, and store manifests.

### 4.6 Memory Hierarchy
AXIOM AI maintains context across multiple layers to ensure continuity and consistency:
1. **Session Memory:** Current conversation and working state.
2. **Project Memory:** Source, assets, tests, graph, and decisions.
3. **Canon Memory:** Approved fictional and product facts.
4. **Organization Memory:** Coding standards, security rules, and platform policies.
5. **Private User Memory:** User preferences and authorized context.
6. **Ephemeral Agent Scratch:** Temporary reasoning artifacts.

### 4.7 The Gauntlet
The automated verification and improvement loop. It executes a rigorous pipeline: formatting, static analysis, unit/property/fuzz tests, integration tests, gameplay/visual/audio tests, network/chain/security tests, and performance/license checks. Failures trigger a disciplined root-cause analysis and patch planning loop. Successful runs produce a comprehensive **Evidence Package**. The Gauntlet is the primary mechanism for ensuring that AI-generated content meets the AAA-scale quality and reliability standards of the AXIOM platform.

## 5. State Machines and Transitions

The operational flow of AXIOM AI is governed by strict state machines that control how intent is processed, planned, and executed.

### 5.1 Action States (Ask, Plan, Build)
- **ASK:** Read-only state. Inspects, explains, and diagnoses without modifying project state. This state is used for querying the Semantic Project Graph, understanding existing logic, and exploring potential changes without risk.
- **PLAN:** Proposes implementation graphs, dependency changes, estimated costs, and acceptance criteria. Requires authorization to proceed. In this state, the Requirement-First Planner and the specialized agents collaborate to create a comprehensive execution strategy, which is presented to the user for review.
- **BUILD:** Executes the approved plan via scoped agents, branches, and the Gauntlet. This state involves active modification of the project graph, generation of assets and code, and rigorous verification through the Gauntlet pipeline.

### 5.2 Consequence Tiers
Every operation is classified to determine the required level of human approval, ensuring that AXIOM AI remains under human control:
- **T0 (Read only):** Executes immediately (e.g., explaining code, inspecting a scene).
- **T1 (Reversible local edit):** Executes with undo and change log (e.g., changing a material value, moving an object).
- **T2 (Multi-system project edit):** Requires plan summary and explicit or configured auto-approval (e.g., adding inventory, modifying networking).
- **T3 (Destructive or costly):** Requires explicit approval and a project checkpoint (e.g., deleting assets, migrating schemas, incurring external costs).
- **T4 (External or irreversible):** Requires strong authentication, detailed review, and explicit signing (e.g., chain transactions, publishing, deploying to production).

## 6. API and Capability Contracts (AXIOM Connect)

AXIOM AI must not manipulate the filesystem directly. It interacts with the platform via **AXIOM Connect**, a typed capability interface. Every call must include caller identity, project identity, capability scope, consequence tier, and produce an audit event. This architecture ensures that AXIOM AI operates with least privilege and that all actions are traceable and reversible.

Example capabilities utilized by AXIOM AI through AXIOM Connect:
- `project.inspect`, `project.build`, `project.test`
- `world.modify`, `scene.validate`
- `asset.generate`, `asset.license_check`
- `logic.compile`, `shader.compile`
- `network.simulate`, `chain.simulate`
- `gauntlet.run`, `release.submit`

The AXIOM Connect interface must support multiple transport mechanisms, including a native in-process SDK, local IPC, gRPC, and REST, to accommodate both internal agents and external tools or CI systems.

## 7. Data Ownership and Storage

AXIOM AI operates on the **Semantic Project Graph**, a versioned, schema-validated representation of the `.axiom` project. The graph maps entities, components, logic, assets, and tests using stable identifiers. However, the graph is an index; canonical project data remains in text-readable files (e.g., `.axiom`, `.axscene`, `.axflow`, `.axir`) suitable for version control. This ensures that the project remains accessible and modifiable outside of the AXIOM AI environment, preventing vendor lock-in and supporting traditional engineering workflows.

All generated assets and code receive explicit provenance and licensing metadata, tracked by the Archivist agent. Private user prompts and AI telemetry require strict access controls and configurable retention policies. The platform must clearly distinguish between creator-owned original content and AXIOM-owned proprietary technology.

## 8. Failure and Degraded Modes

The AXIOM AI domain is designed to handle failures gracefully, ensuring that issues do not cascade and that the user is provided with clear, actionable information.

- **Model Failure:** The Model Router must automatically fallback to alternative providers or local models if the primary provider fails, returns malformed output, or exceeds latency thresholds. This ensures continuity of service even during external provider outages.
- **Gauntlet Failure:** If a test fails, AXIOM AI must not weaken the test. It must preserve evidence, identify the root cause, generate a patch plan, and re-run the affected gate. If the iteration budget is exhausted, it must stop and escalate to the user, providing the Evidence Package and a clear explanation of the failure.
- **Integration Conflicts:** The Integrator agent must refuse unsafe combinations and escalate semantic merge conflicts that cannot be deterministically resolved. This prevents corrupted project states and ensures that parallel development efforts do not overwrite each other destructively.

## 9. Security, Privacy, and Provenance

Security is a foundational architectural requirement for the AXIOM AI domain, given its ability to generate code, interact with blockchain networks, and publish content.

- **Agent Isolation:** Agents operate in sandboxes with explicit repository paths, time/compute budgets, network permissions, tool allowlists, and artifact scanning. They cannot access the broader filesystem or unauthorized external networks.
- **Prompt Injection:** External content (project files, web references, user inputs) must be treated as data, not authority. Agent permissions are derived strictly from the capability broker and project policy, never from instructions embedded within the content they are processing.
- **Secrets Management:** Agents receive scoped ephemeral tokens. They must never have access to raw master secrets, signing keys, or user wallets.
- **Continuous Adversarial Simulation:** The Gauntlet must continuously inject hostile conditions (malformed projects, packet loss, prompt injection, double-spend attempts) to ensure platform resilience and validate the effectiveness of the security controls.

## 10. Observability and Performance Budgets

Comprehensive observability is required to monitor the performance, cost, and effectiveness of the AXIOM AI domain.

AXIOM AI telemetry must record task IDs, model providers, token/compute costs, tool calls, change sets, test outcomes, and user approvals. This data must be correlated with project change sets and service traces using unique correlation IDs. The PERF agent enforces performance budgets (CPU, GPU, memory, I/O, network) during the Gauntlet loop, ensuring generated solutions do not degrade the AAA-scale destination of the engine. Users must be provided with clear dashboards detailing the cost and performance impact of AI-generated changes.

## 11. Test Pyramid and Acceptance Tests

AXIOM AI is subject to its own rigorous testing requirements to ensure reliability and adherence to the requirement-first planning paradigm:

- **Requirement Extraction Tests:** Verify the Intent Compiler accurately captures constraints, distinguishing between mandatory and optional requests.
- **Permission Enforcement Tests:** Ensure agents cannot bypass consequence tiers or access restricted APIs through AXIOM Connect.
- **Hallucination Prevention:** Validate that generated plans correspond to actual engine capabilities and do not invent non-existent APIs or features.
- **Branch Isolation Tests:** Confirm agents cannot write directly to production or main branches, and that all changes are staged in isolated worktrees.
- **Cost Limit Tests:** Ensure execution halts immediately when configured compute or financial budgets are exceeded.

## 12. V1 Definition of Done (DoD)

The AXIOM AI domain is considered `V1-BUILD-REQUIRED` complete when the following criteria are met:

1. PRIME, Intent Compiler, Planner, and Model Router are fully implemented, integrated, and capable of processing complex, multi-step user intents.
2. The parallel agent system can execute isolated tasks across the engine, network, and chain domains, successfully collaborating to build complete, functional game systems.
3. The Gauntlet successfully runs the full pipeline (static analysis through performance/security checks) and produces verifiable Evidence Packages for every T2 and above change.
4. Consequence tiers and Ask/Plan/Build states are strictly enforced, with robust human-in-the-loop approval mechanisms.
5. AXIOM Connect capability schemas are defined and utilized exclusively by all agents for interacting with the platform.
6. The system passes all security, prompt injection, and isolation tests, demonstrating resilience against adversarial inputs.
7. The Semantic Project Graph accurately reflects the state of the `.axiom` project and supports querying, diffing, and semantic merging.

## 13. Work Packages (Dependency Order)

The implementation of the AXIOM AI domain must proceed in the following dependency-aware order:

1. **AXIOM Connect Schema v0:** Define the typed APIs and capability broker, establishing the foundational interface for all subsequent AI interactions.
2. **Project Graph/Index v0:** Implement the semantic representation of `.axiom` projects, enabling the AI to understand the structure and relationships within a game.
3. **Intent Compiler v0:** Build the natural language to structured intent translation layer, focusing on constraint extraction and goal resolution.
4. **Planner & Task Graph v0:** Implement requirement extraction and dependency-aware task generation, internalizing the CodeSpring-style planning discipline.
5. **Model Router v0:** Develop the dynamic capability routing and fallback system, ensuring platform independence and resilience.
6. **Agent Sandbox & Worktree Runner:** Create isolated execution environments for parallel agents, enforcing security and resource boundaries.
7. **PRIME Service v0:** Integrate the orchestrator to manage intent, budget, and agent scheduling, tying the previous components together.
8. **Gauntlet v0:** Build the automated verification loop and Evidence Package generator, ensuring the quality and reliability of AI-generated content.
9. **Ask/Plan/Build Enforcement:** Implement state machines and consequence tier approvals, finalizing the user-facing control mechanisms.

## 14. Open ADRs (Architecture Decision Records)

The following decisions require formal ADRs impacting the AXIOM AI domain, as mandated by the master specification:

- **Core C++/Rust boundary and build toolchain:** Impacts PRIME and AXIOM Connect implementations, dictating how the Rust-based AI orchestration layer interacts with the C++ engine core.
- **.axiom manifest and schema language:** Impacts the Intent Compiler and Project Graph parsing, defining the canonical format for project data.
- **AXIR format and execution backend:** Impacts how AI-generated logic is represented and executed, bridging the gap between high-level intent and runtime behavior.
- **Privacy and telemetry defaults:** Impacts data retention and model routing policies, determining how sensitive user and project data is handled within the AI ecosystem.
- **Human Control Configuration:** Define the specific mechanisms for configuring model/provider allowlists, spending limits, and required reviewers.
