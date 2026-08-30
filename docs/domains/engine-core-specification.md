# AXIOM-XIII Implementation-Domain Specification: Engine Core

## 1. Domain Purpose and Non-Negotiable Doctrine

The Engine Core domain provides the native runtime, architectural foundation, and execution environment for all `.axiom` projects. It is responsible for bridging high-level intent, authored through Simple mode, Advanced mode, or AXIOM Flow, into executable reality across diverse platforms. These platforms include desktop environments, headless servers, and the future PYRAMID hardware. The Engine Core must not only execute game logic but also provide the underlying infrastructure for tools, asset processing, and the editor itself. It is the central nervous system of AXIOM-XIII, ensuring that the ambitious goals of the platform are met with robust, performant, and reliable code.

The runtime relies on a scalable Entity-Component-System (ECS) foundation designed for large, dense worlds, avoiding monolithic object inheritance. This composition-first simulation is a non-negotiable doctrine. The architecture must support streaming topology, persistent state, and massive simulation workloads, such as large crowds, complex vegetation, and intricate destruction, without faltering. The ECS must be data-oriented, utilizing archetype or equivalent efficient queries to maximize cache coherence and multithreaded performance.

Language boundary discipline is strictly enforced to leverage the strengths of different programming paradigms. C++ is the primary language for high-performance rendering, gameplay hot paths, and Unreal Bridge compatibility. It is essential for interacting with legacy systems and ensuring maximum throughput in critical areas. Rust is utilized for orchestration, package management, shell bootstrap, and security-sensitive services. Its memory safety guarantees and modern concurrency model make it ideal for these robust, foundational services. The ABI/FFI boundary between these languages must be explicit, fuzzed, and versioned. There can be no exception unwinding across unsupported boundaries, and owned memory rules must be strictly adhered to.

Deterministic and authoritative networking is another core requirement. Core gameplay and simulation loops must support deterministic profiles for rollback, lockstep, replays, and chain-attested simulation. This is crucial for the competitive Arena domain and the economic Chain domain, which rely on the engine to provide verifiable and reproducible results. The engine must maintain a protocol-first architecture, remaining independent of specific hardware at launch. It must be capable of running on standard desktop environments while adhering to the PYRAMID Virtual Target constraints for future fixed-hardware execution.

Finally, as mandated by the Owner Directive, all systems, including experimental abstractions, ABI/FFI boundaries, and the proprietary AXVM, must be implemented, integrated, and tested in V1. Documentation-only placeholders are strictly prohibited. The organization must build the code, schemas, interfaces, service boundaries, simulations, sandbox flows, operational controls, test suites, and end-to-end integration required for the full V1 destination. No roadmap gate or maturity label may be interpreted as permission to indefinitely defer these capabilities.

## 2. Personas and Actors

The Engine Developer writes C++ and Rust systems, implements platform abstractions, and optimizes FABRIC job scheduling. They are responsible for the low-level plumbing of the engine, ensuring that memory allocators are efficient, job stealing is balanced, and platform-specific quirks are safely hidden behind the Platform Abstraction Layer.

The Gameplay Programmer authors high-performance C++ components and systems, or utilizes AXIOM Flow and AXScript for logic. They focus on bringing the game mechanics to life, leveraging the ECS to build complex behaviors and interacting with the physics and animation systems.

AXIOM AI, acting as the PRIME orchestrator, queries the Schema Registry, invokes build and test operations via AXIOM Connect, and generates AXIR. It acts as an intelligent assistant and an automated worker, capable of analyzing the project graph, proposing changes, and executing approved plans within constrained branches.

The Content Creator interacts with the engine indirectly through Simple or Advanced mode to build scenes, entities, and materials. They rely on the Engine Core to provide a stable, responsive, and intuitive authoring environment, trusting that their high-level intent will be faithfully translated into runtime performance.

## 3. Domain Boundaries and Interfaces

The Engine Core domain serves as the central hub, interfacing with several key domains. It interacts with the AXIOM Shell, which provides the desktop console environment and user interface. The shell relies on the engine to render its interface and manage its underlying state.

It receives commands from AXIOM AI, which compiles intent into AXIR and issues directives via AXIOM Connect. The engine must expose a robust, typed API to AXIOM Connect, ensuring that AI operations are permissioned, auditable, and reversible.

The Engine Core relies on the AXIOM Protocol for canonical schemas and stable identifiers. It must respect the protocol's versioning rules and ensure that all entities and assets are properly tracked and referenced.

It feeds the AXIOM Render domain by providing FABRIC job lanes and memory arenas for high-fidelity output. The engine must supply the renderer with virtualized geometry, visibility data, and material properties, ensuring that the renderer has the resources it needs to achieve contemporary AAA-scale fidelity.

Additionally, it supports the Chain and Arena domains by providing deterministic simulation, signed replays, and verifiable state. The engine must guarantee that simulations can be accurately replayed and that the resulting state can be cryptographically attested for economic settlement.

## 4. Named Components and Internal Modules

The Platform Abstraction Layer (PAL) hides host operating system services, such as windowing, filesystem, cryptography, and networking, behind versioned AXIOM interfaces. It ensures that the engine can run on Windows, Linux, and the future PYRAMID hardware without requiring widespread platform-specific `#ifdef` blocks throughout the codebase.

The ECS and Object Model manages entities, components, and systems, compiling authoring graphs into runtime ECS, asset tables, and streaming chunks. It separates the rich, hierarchical data used during authoring from the efficient, data-oriented structures required for runtime performance.

AXIOM FABRIC serves as the unified job graph and scheduling system, handling dependency-aware jobs, work stealing, and CPU affinity. It manages priority classes, ensuring that frame-critical simulation and input processing are never starved by background tasks like asset compilation or AI generation.

The Memory Subsystem provides tagged allocators, arenas, GPU memory tracking, and leak detection. It enforces strict memory budgets and provides crash-safe diagnostics to help developers track down elusive memory corruption issues.

Serialization and the Schema Registry manage versioned, schema-driven serialization and store reflection metadata, migration functions, and ownership rules. They ensure that data can be safely saved, loaded, and transmitted across the network, even when dealing with untrusted input from user-generated packages.

AXIOM Flow and AXIR represent the visual and semantic authoring layer and the intermediate representation that connects intent to execution. They allow creators to build complex logic without writing C++ code, while still compiling down to efficient runtime instructions.

The Package and Plugin System manages `.axpkg` distributions, capability-based sandboxing, and dependency resolution. It ensures that third-party code and assets can be safely integrated into a project without compromising the stability or security of the engine.

Finally, the Build Graph and Patching module orchestrates incremental builds, shader compilation, package signing, and delta patching. It manages the complex process of turning source assets and code into a distributable, signed package ready for the AXIOM Store.

## 5. Canonical Entities and Stable IDs

| Entity Name | Description |
|---|---|
| **Project** | The root container defined by the `.axiom` manifest. It holds all configuration, permissions, and performance budgets. |
| **Entity** | A stable, globally namespaced identifier for composed components. It persists across streaming, reloading, and network replication. |
| **ComponentSchema** | Versioned metadata stored in the Schema Registry. It defines the layout, default values, and migration rules for a component. |
| **AXIR_Node** | Operations within the AXIOM intermediate representation. They represent the fundamental building blocks of AXIOM Flow logic. |
| **Job_Ticket** | A unit of work scheduled by the FABRIC system. It tracks dependencies, priority, and execution state. |

## 6. State Machines and Transitions

The Entity Lifecycle progresses from Spawned to Initialized, then becomes Active during streaming or simulation. It may be Suspended when moved out of the active streaming bounds, before eventually being Destroyed and its memory reclaimed by the ECS allocator.

Job Execution within FABRIC transitions from Pending (waiting for dependencies) to Scheduled (ready for execution), then Running (assigned to a worker thread), and finally to Completed or Cancelled.

The Build Pipeline advances from a Clean state to Dependency Resolution (fetching required packages), Cooking (processing assets for the target platform), Compilation (building native code), Linking, Packaging (creating the `.axpkg`), and concludes in a Signed state (ready for distribution).

## 7. API and Capability Contracts (AXIOM Connect)

The Engine Core exposes typed capabilities to AXIOM Connect to facilitate interaction with internal tools, external agents, and AXIOM AI. Every capability call must include caller identity, project identity, capability scope, and consequence tier.

The `project.build` capability initiates the build graph for a specified target profile. It handles incremental builds, distributed work, and content cooking.
The `project.test` capability executes the Gauntlet suite against the compiled runtime, verifying performance, deterministic execution, and memory budgets.
The `entity.spawn` and `entity.modify` capabilities mutate the ECS state during authoring or runtime. They are subject to permission checks and may require AI approval for destructive edits.
The `logic.compile` capability compiles AXIOM Flow graphs into AXIR and native code or VM bytecode. It performs static analysis to ensure determinism annotations are respected.
The `gauntlet.run` capability triggers the automated testing and verification pipeline, gathering evidence for release certification.

## 8. Data Ownership and Storage

The Authoring Graph contains rich, hierarchical data stored in text-readable formats, such as `.axentity` and `.axscene`, making it suitable for version control and human inspection. This data is the source of truth for the project.

The Runtime Representation consists of compiled, data-oriented chunks and asset tables optimized for streaming and cache coherence. This data is generated from the Authoring Graph and is designed purely for execution efficiency.

Memory Allocation is strictly owned by the Memory Subsystem; systems must request memory from specific arenas or frame allocators. Direct calls to `malloc` or `new` are prohibited in engine code to ensure tracking and budget enforcement.

## 9. Dependency Graph

The Engine Core depends on the AXIOM Protocol for schemas, stable identifiers, and licensing rules. It depends on the Platform OS via the Platform Abstraction Layer for low-level system services.

It is depended upon by AXIOM Render, which requires its job scheduling and memory management. It is depended upon by AXIOM AI, which needs its reflection metadata and Connect capabilities. It is depended upon by the AXIOM Shell and First-Party Games, which rely on it as their fundamental execution environment.

## 10. Failure and Degraded Modes

In the event of memory exhaustion, the engine gracefully degrades by purging non-critical caches, such as distant level-of-detail assets and unused audio streams, and halting background AI or asset processing. It must attempt to save critical state and alert the user before a hard crash occurs.

During job starvation, FABRIC prioritizes frame-critical simulation and input over background tasks. It will dynamically scale back the priority of non-essential lanes to maintain a stable framerate.

If an untrusted package fails, the sandboxed plugin that faults or exceeds resource budgets is terminated without crashing the core engine or the editor session. The failure is logged, and the user is notified of the offending package.

## 11. Security, Privacy, and Provenance

ABI and FFI boundaries must be strictly fuzzed, and exception unwinding across unsupported boundaries is prohibited. This prevents malicious or poorly written code from corrupting the engine's state.

Packages operate under capability-based access, with native code packages requiring rigorous review and explicit user consent. They must declare their network, filesystem, and chain access requirements in their manifest.

All parsers handling untrusted data, including saves, network packets, and media, must be bounded and validated against malicious input. Fuzzing these parsers is a mandatory part of the V1 implementation scope.

Commercial builds must be reproducible, generating software bill of materials (SBOMs), dependency locks, and deterministic signatures. This ensures provenance and protects against supply chain attacks.

## 12. Observability and Performance Budgets

All allocations, FABRIC jobs, and state transitions must emit correlation IDs to enable deterministic divergence detection and profiling. This is essential for debugging network desyncs and performance bottlenecks.

Background AI or chain workloads must not cause frame-time instability in foreground games, adhering strictly to established frame budgets. The engine must provide tools to visualize and enforce these budgets.

Telemetry systems must provide crash-safe diagnostics and memory leak tracking. This data must be collected in a privacy-preserving manner, respecting user consent and jurisdictional regulations.

## 13. Test Pyramid and Concrete Acceptance Tests

The test pyramid includes unit tests for fuzzing ABI/FFI boundaries, serialization, and untrusted data parsers. These tests run continuously in the CI pipeline. Integration tests verify FABRIC scheduling priorities, ECS archetype queries, and memory arena bounds.

End-to-end tests within the Gauntlet suite include:
- **Acceptance Test 1:** Compile an `.axiom` project to a headless simulation target and verify deterministic execution over 10,000 frames, ensuring no divergence between multiple runs.
- **Acceptance Test 2:** Load an untrusted `.axpkg` that attempts unauthorized filesystem access; verify that the sandbox blocks the operation, logs the event, and terminates the plugin without affecting the main engine process.
- **Acceptance Test 3:** Hot-reload an AXIOM Flow logic graph during runtime. Verify that the new logic is applied seamlessly without memory corruption, state loss, or interruption of the simulation loop.

## 14. V1 Definition of Done

The V1 implementation is considered complete when the following conditions are met:
- C++ and Rust boundaries are defined, fuzzed, and versioned, with no exception leaks.
- The Platform Abstraction Layer is fully implemented and tested for Windows, Linux, and the PYRAMID Virtual Target.
- The ECS supports archetype queries, multithreading, and stable external IDs, capable of handling AAA-scale simulation workloads.
- The FABRIC job scheduler handles frame-critical and background lanes without starvation or priority inversion.
- The memory subsystem enforces tagged allocators, tracks GPU memory, and provides robust leak detection.
- The Schema Registry and serialization systems handle forward and backward migration, and are hardened against untrusted input.
- The build graph supports incremental builds, distributed work, and signed packaging, producing reproducible builds.
- All capabilities exposed to AXIOM Connect are executable, integrated, and verified via the Gauntlet suite.
- The proprietary AXVM is implemented, integrated, and passes production gates, avoiding documentation-only placeholders.

## 15. Work Packages in Dependency Order

| Work Package | Description |
|---|---|
| **WP1: Platform Abstraction Layer & Memory Core** | Establish OS interfaces, windowing, filesystem access, and foundational tagged allocators. |
| **WP2: C++/Rust FFI & Schema Registry** | Define cross-language boundaries, error handling, and reflection metadata storage. |
| **WP3: AXIOM FABRIC Scheduler** | Implement the job graph, work stealing, priority lanes, and fiber/coroutine support. |
| **WP4: ECS and Object Model** | Build archetype storage, entity lifecycle management, and stable identity resolution. |
| **WP5: Serialization & Asset Pipeline** | Implement versioned, deterministic parsing, chunking, and streaming infrastructure. |
| **WP6: AXIOM Flow & AXIR Execution** | Build the logic compiler, static analysis for determinism, and the reference AXVM. |
| **WP7: Package System & Sandboxing** | Implement `.axpkg` capability controls, manifest validation, and plugin isolation. |
| **WP8: Build Graph & Patching** | Orchestrate build targets, content cooking, dependency resolution, and delta patch generation. |

## 16. Open ADRs

Several Architectural Decision Records remain open and require resolution before major implementation can proceed. These cannot be resolved by ad hoc agent choices:
- **ADR 2:** Core C++ and Rust boundary and the specific build toolchain to be used across platforms.
- **ADR 3:** The exact syntax and semantics of the `.axiom` manifest and schema language.
- **ADR 4:** The binary format of AXIR and the execution backend (e.g., native compilation vs. WebAssembly vs. proprietary VM).
- **ADR 6:** The specific ECS storage model (e.g., sparse sets vs. archetype chunks) and its impact on cache coherence.
- **ADR 8:** The production physics dependency and the design of its replacement interface.
- **ADR 9:** The production audio backend and the architecture of the plugin-hosting sandbox for audio effects.
