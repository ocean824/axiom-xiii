# Domain Specification: Semantic Project Graph and AXIOM Core Ecosystem

## 1. Domain
Semantic Project Graph

## 2. Purpose and Non-Negotiable Doctrine
The Semantic Project Graph (SPG) and its associated core systems (AXIR, AXVM, AXIOM Connect, native formats, and Unreal Bridge) represent the foundational architecture of the AXIOM-XIII platform. The SPG is the definitive source of truth for a game, modeling it not as a directory of unrelated files, but as a queryable, versioned system of meaningful relationships encompassing code, assets, logic, network authority, economic properties, and licensing provenance.

**Doctrine:**
*   **One Project, Two Interfaces:** Simple (AI-first) and Advanced (professional) modes must operate on the same SPG and native `.axiom` project without any export step or loss of fidelity [1].
*   **Stable Identity:** Identity is absolute. Every component receives a stable AXIOM identifier that persists across file moves and renames [1].
*   **Rebuildable from Source:** The SPG is an indexed representation of canonical project data, which remains in text-readable, version-control-friendly files. The graph can always be rebuilt from source [1].
*   **Mandatory V1 Build Scope:** Per the V1 Build-Complete directive, all described components—including the fully proprietary AXVM, experimental formats, and complete Unreal migration tools—are mandatory V1 implementation scope. They may be gated for activation, but not for construction [2].
*   **No Uncontrolled Access:** No agent should need uncontrolled filesystem manipulation to operate the engine; all interactions must pass through AXIOM Connect [1].

## 3. Personas and Actors
*   **Simple Mode Creator:** Interacts with the SPG primarily through AXIOM AI, relying on natural language and high-level intent to manipulate the graph.
*   **Advanced Mode Developer:** Interacts directly with the SPG, native formats, and AXIOM Connect APIs using professional tools, scripts, and manual file edits.
*   **AXIOM AI (Agent):** A permissioned actor that reads the SPG, proposes changes, generates AXIR, and executes authorized actions via AXIOM Connect.
*   **Build/CI System:** Consumes the SPG and native formats to produce deterministic builds, run tests, and package assets.
*   **Migration Tooling (Unreal Bridge):** Translates external project structures into the SPG and native `.axiom` formats.

## 4. Domain Boundaries
**In Scope:**
*   Semantic Project Graph (schema, indexing, querying, and diffing).
*   Stable identifiers and identity management.
*   Decision and canon ledgers (ADRs, requirements, mechanics registry).
*   Native `.axiom` and `.ax*` file formats and their schemas.
*   AXIR (Semantic Intermediate Representation) and AXVM (Reference Virtual Machine).
*   AXIOM Connect (API/Capability model).
*   Source control integration, checkpoints, and semantic diffs.
*   Unreal Bridge (analysis, conversion, and reporting).

**Out of Scope (Interfaced Domains):**
*   The implementation of the rendering pipeline (interfaces via `.axfx` and `.axmat`).
*   The implementation of the AXIOM Chain consensus (interfaces via `.axchain`).
*   The internal workings of the AI model itself (interfaces via AXIOM Connect).
*   AXIOM FABRIC job scheduling (though SPG rebuilds run as FABRIC jobs).

## 5. Named Components and Responsibilities

| Component | Responsibility |
| :--- | :--- |
| **SPG Indexer** | Parses `.axiom` and `.ax*` files to build and maintain the in-memory/cached queryable graph. |
| **Identity Manager** | Generates, resolves, and tracks stable AXIOM identifiers across the project lifecycle. |
| **Ledger Controller** | Manages the structured text files for decisions, canon, licenses, and requirements. |
| **Format Serializer** | Handles reading, writing, schema validation, and schema registry of all `.ax*` formats. |
| **AXIR Compiler** | Translates high-level logic (from AI intent, AXIOM Flow, or scripts) into the semantic intermediate representation. |
| **AXVM Executor** | The reference virtual machine for executing AXIR (V1-EXPERIMENTAL build scope, mandatory construction). |
| **AXIOM Connect Gateway** | The typed RPC/REST/MCP interface for all platform interactions, enforcing permissions and audit trails. |
| **Unreal Bridge Analyzer** | Scans `.uproject` files, generates compatibility/license reports, and maps dependencies. |
| **Unreal Bridge Translator** | Converts Unreal assets, code, and logic into the SPG and native `.ax*` formats. |
| **Semantic Diff Engine** | Generates human-readable, domain-specific diffs for worlds, logic graphs, and project settings instead of raw binary or unreadable text diffs. |

## 6. Canonical Entities and Stable IDs
Every meaningful element in AXIOM-XIII receives a stable identifier. Human-readable names are merely labels.

*   **Format:** `ax_[type]_[uuidv7]` (e.g., `ax_ent_01HGW...`, `ax_ast_01HGW...`). UUIDv7 ensures temporal sortability and uniqueness.
*   **Resolution:** The Identity Manager resolves these IDs to their current file paths or graph nodes.
*   **Persistence:** IDs are embedded within the `.ax*` files. Moving or renaming a file does not change its ID [1].
*   **Runtime:** Persistent entity identity must be separate from runtime memory address or array index to survive streaming, reload, and migration [1].

## 7. State Machines and Transitions

### 7.1 AXIOM AI Proposal State Machine
1.  **PROPOSED:** AI generates an idea, logic block, or asset change. It is visible but not part of the canonical build.
2.  **REVIEWING:** A user or automated Gauntlet test is evaluating the proposal.
3.  **ACCEPTED:** Authorized user approves. The change is merged into the SPG, serialized to disk, and a source-control checkpoint is created.
4.  **REJECTED:** The proposal is discarded or sent back for revision.

### 7.2 Unreal Bridge Import State Machine
1.  **INVENTORY:** Discovering files and dependencies.
2.  **SCANNING:** Checking licenses and provenance.
3.  **REPORTING:** Generating the compatibility report, distinguishing creator-owned vs. engine-owned content.
4.  **CONVERTING:** Translating assets and logic in an isolated branch.
5.  **VERIFYING:** Running Gauntlet tests on the converted project.
6.  **NATIVE:** The project is now a fully native `.axiom` project.

## 8. API and Capability Contracts (AXIOM Connect)
AXIOM Connect is the mandatory, typed interface for all interactions. It supports gRPC, REST, local IPC, and MCP.

**Contract Requirements:**
Every call MUST include: caller identity, project identity, capability scope, requested operation, consequence tier, authorization result, input/output hashes, duration, resulting change set, and an audit event [1].

**Core Capabilities:**
*   `project.inspect(id)`: Returns the current state of the SPG for the project.
*   `project.query(graphql_query)`: Executes a semantic query against the SPG.
*   `entity.modify(id, component_data)`: Updates an entity, triggering an SPG diff and serialization.
*   `logic.compile(source)`: Compiles source code, AXIOM Flow graphs, or AI intent into AXIR.
*   `bridge.analyze(uproject_path)`: Initiates the Unreal Bridge analysis phase.

## 9. Command, Query, and Event Flows

**Example: AI Modifying an Entity**
1.  **Command:** AI sends `entity.modify` via AXIOM Connect MCP.
2.  **Validation:** Connect Gateway checks permissions, budgets, and locks.
3.  **Execution:** The SPG Indexer creates a branched proposal.
4.  **Event:** `spg.proposal.created` is emitted via WebSocket.
5.  **Query:** User UI queries the diff using `project.diff(base, proposal)`.
6.  **Command:** User sends `proposal.accept`.
7.  **Execution:** SPG Indexer merges the branch, Format Serializer writes to `.axent`, and Identity Manager updates references. A source control checkpoint is generated.
8.  **Event:** `spg.updated` is emitted.

## 10. Data Ownership and Storage
*   **Canonical Data:** Stored as text-readable, schema-validated files (`.axiom`, `.axent`, `.axlogic`, etc.) on the local filesystem or standard source control (Git) [1].
*   **Graph Index:** An ephemeral, rebuildable database (e.g., SQLite or an in-memory graph) maintained by the SPG Indexer.
*   **Ledgers:** Stored as structured Markdown or TOML files (`DECISIONS.md`, `REQUIREMENTS.toml`, `LICENSES.toml`) in the project root [1].
*   **Binary Payloads:** Heavy assets (textures, audio) are stored in `.axpkg` or standard binary formats, referenced by stable IDs in the text manifests.

## 11. Dependency Graph
*   **SPG Indexer** depends on **Format Serializer** and **Identity Manager**.
*   **AXIOM Connect** depends on **SPG Indexer**, **AXIR Compiler**, and **Permission/Policy Engine**.
*   **Unreal Bridge** depends on **Format Serializer** and **SPG Indexer**.
*   **AXVM Executor** depends on **AXIR Compiler**.

## 12. Failure and Degraded Modes
*   **Index Corruption:** If the SPG Index database is corrupted, the system automatically deletes it and rebuilds from the canonical `.ax*` files. This is a normal, expected recovery path.
*   **Unresolved References:** If an ID cannot be resolved (e.g., a missing asset), the SPG loads the project in a degraded state, marking the reference as `MISSING`. The project remains openable and editable [1].
*   **AXVM Failure:** If the experimental AXVM crashes during execution, the system falls back to native code execution or WebAssembly if available, logging the failure for V1-EXPERIMENTAL tracking.

## 13. Security, Privacy, Provenance, and Legal
*   **Provenance:** Every `.ax*` file and SPG node MUST include a license and provenance reference. The Unreal Bridge explicitly scans for and flags third-party licenses to avoid importing Epic-owned engine source as creator-owned AXIOM code [1].
*   **Auditability:** All changes made via AXIOM Connect, especially those by AXIOM AI, are logged with cryptographic hashes of the inputs and outputs.
*   **Sandboxing:** AXIR execution and AXIOM Connect calls operate within strict permission boundaries (least privilege).
*   **No Uncontrolled Access:** External agents MUST NOT have raw filesystem access; they must use AXIOM Connect.

## 14. Observability
*   **Metrics:** SPG rebuild time, query latency, AXIR compilation time, AXIOM Connect request rates and error rates.
*   **Tracing:** Distributed tracing (e.g., OpenTelemetry) across AXIOM Connect calls, from the UI/AI through the Gateway to the SPG Indexer.
*   **Logging:** Structured logging for all state transitions, especially proposal acceptance, checkpoint generation, and bridge conversions.

## 15. Performance and Resource Budgets
*   **SPG Rebuild:** Must be capable of rebuilding a 10,000-entity project graph from text files in under 5 seconds on reference hardware.
*   **Query Latency:** Standard graph queries (e.g., "find all entities with component X") must return in under 16ms to support editor responsiveness.
*   **Memory:** The in-memory SPG index must not exceed 2GB for a standard AAA-scale scene.

## 16. Test Pyramid and Acceptance Tests
*   **Unit Tests:** Format Serializer schema validation, Identity Manager UUIDv7 generation, AXIR instruction parsing, semantic diff generation.
*   **Integration Tests:** AXIOM Connect capability execution (e.g., ensuring `entity.modify` correctly updates the SPG, emits events, and triggers checkpoints).
*   **End-to-End (Acceptance) Tests:**
    *   *Test 1:* Create a project, spawn an entity, rename the file containing the entity, and verify the stable ID still resolves correctly.
    *   *Test 2:* Run the Unreal Bridge against a known sample `.uproject`, verifying that all materials, logic, and assets are translated into valid `.ax*` formats and the SPG rebuilds successfully.
    *   *Test 3:* AXIOM AI proposes a logic change via Connect; verify the change remains in the `PROPOSED` state and does not affect the canonical build until explicitly accepted, at which point a source control checkpoint is created.

## 17. V1 Definition of Done (Build-Complete)
Per the V1 Directive, the following MUST be implemented, integrated, and tested:
1.  The SPG Indexer successfully parses, queries, and diffs a complex project.
2.  Stable identifiers are enforced across all tooling and runtime states.
3.  All native `.ax*` formats have defined, versioned schemas.
4.  AXIR is fully specified, and the AXVM is bootable and executable (even if gated from production) [2].
5.  AXIOM Connect exposes the full capability model via local IPC and MCP.
6.  The Unreal Bridge successfully converts a designated benchmark project into a functional `.axiom` project.
7.  Decision and canon ledgers are automatically maintained and queryable.
8.  Semantic diffs correctly represent changes to worlds, scenes, logic graphs, and materials [1].

## 18. Work Packages (Dependency Order)
1.  **WP-SPG-01:** Define schemas for `.axiom` and core `.ax*` formats, and implement the Schema Registry.
2.  **WP-SPG-02:** Implement the Identity Manager and UUIDv7 resolution.
3.  **WP-SPG-03:** Build the SPG Indexer and format serialization layer.
4.  **WP-SPG-04:** Implement the Ledger Controller for ADRs and requirements.
5.  **WP-SPG-05:** Define the AXIR specification.
6.  **WP-SPG-06:** Build the AXIOM Connect Gateway and capability model.
7.  **WP-SPG-07:** Implement the AXVM reference executor.
8.  **WP-SPG-08:** Develop the Unreal Bridge analyzer and reporting tools.
9.  **WP-SPG-09:** Develop the Unreal Bridge asset and logic translators.
10. **WP-SPG-10:** Implement Semantic Diff Engine and checkpointing system for native formats.

## 19. Open ADRs
*   **ADR-SPG-001:** Selection of the underlying database technology for the ephemeral SPG Index (SQLite vs. custom in-memory graph).
*   **ADR-SPG-002:** Final binary format specification for `.axpkg` (e.g., flatbuffers vs. custom chunked format).
*   **ADR-SPG-003:** Exact mechanism for textual diffing of visual node graphs (e.g., `.axfx`, `.axui`, AXIOM Flow).

## 20. Explicit Interfaces with Other Domains
*   **Editor/UI:** Consumes the SPG via AXIOM Connect for rendering the project hierarchy and property inspectors.
*   **AI Agent (CodeSpring/Traycer):** Uses AXIOM Connect to read the SPG, generate AXIR, and propose changes.
*   **Build Pipeline:** Reads the canonical `.ax*` files directly to produce distributable packages.
*   **Store/Blockchain:** The SPG references `.axchain` modules and digital object licenses, linking in-game assets to their economic reality.
*   **AXIOM FABRIC:** Executes SPG rebuilds and AXIR compilations as scheduled jobs.

## References
[1] AXIOM-XIII V1 Master Specification. Section 14: Semantic Project Graph, Section 15: Native Formats, Section 16: AXIOM Connect, Section 17: AXIOM Bridge, Section 18: Source Control.
[2] Owner Directive: AXIOM-XIII V1 Is Build-Complete.
