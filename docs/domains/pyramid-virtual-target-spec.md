# PYRAMID Virtual Target & OS Domain Specification

## 1. Purpose and Non-Negotiable Doctrine

The PYRAMID Virtual Target and associated hardware/OS components represent the foundational execution environment for the AXIOM-XIII platform. The primary purpose of this domain is to provide a highly secure, performant, and deterministic environment for all AXIOM-XIII operations, seamlessly transitioning between PLAY, DEV, and NODE modes.

**Non-Negotiable Doctrine:**
*   **Security First:** Every component, from the P0 hardware to the proprietary kernel, must enforce strict isolation and provenance tracking. Secure boot and cryptographic verification are mandatory for all transitions and updates.
*   **Deterministic Performance:** Performance profiles must guarantee resource allocation and execution timing, particularly in PLAY and NODE modes, ensuring predictable latency and throughput.
*   **Universal Compatibility (V1):** As per the OWNER-DIRECTIVE-V1-BUILD-COMPLETE, all described future, preview, experimental, architected, deferred, or later capabilities are mandatory V1 architecture, code, integration, and test scope. Gates may restrict activation, but construction is mandatory.

## 2. Personas and Actors

*   **End User (Player/Developer):** Interacts with the system in PLAY or DEV modes, expecting seamless performance and intuitive tooling.
*   **Node Operator:** Manages the system in NODE mode, focusing on distributed compute contribution and resource optimization.
*   **System Administrator/Fleet Manager:** Oversees updates, recovery, and fleet-wide monitoring.
*   **Hardware Certification Authority:** Validates P0-P3 hardware compliance and enclosure integrity.
*   **AXVM Execution Engine:** The primary internal actor consuming OS and hardware resources.

## 3. Domain Boundaries

The PYRAMID Virtual Target domain encompasses the entire stack from the physical hardware (P0-P3, enclosure) up to the OS interface presented to the AXVM.

**In-Scope:**
*   Hardware definition (P0, P1, P2, P3 tiers), enclosure, manufacturing, and certification.
*   Firmware and controller logic.
*   Linux-based OS and experimental proprietary kernel.
*   GPU and specialized drivers.
*   Secure boot, update, and recovery mechanisms.
*   Secure transport, cryptography, and codecs.
*   Filesystem and storage management.
*   PLAY, DEV, and NODE mode state machines.
*   Performance profiles and resource allocation.
*   Distributed node compute integration (at the OS/Hardware level).

**Out-of-Scope:**
*   AXVM internal execution logic (handled by AXVM domain).
*   Application-level logic and game engines (handled by respective domains).
*   High-level network routing (beyond secure transport).

## 4. Named Components and Internal Modules

### 4.1 Hardware and Firmware
* **PYRAMID P0:** Industrial/design prototype using off-the-shelf internals and a functional 3D-printed pyramid enclosure for AXIOM Shell, Virtual Target, thermal, acoustic, safety, and usability experiments.
* **PYRAMID P1:** Controlled reference computer with locked CPU/GPU/memory/storage combinations, custom cooling and enclosure, signed OS image, controller/accessories, hardware-backed secure storage, predictable performance, and repair/upgrade policy.
* **PYRAMID P2:** Custom board or tightly integrated platform with optimized I/O and power, hardware-rooted trust, deeper OS/driver integration, manufacturing, and certification.
* **PYRAMID P3:** Custom-silicon workstream, including feasibility, architecture, toolchain, economics, and prototype planning; physical tape-out or production requires the capital and scale decision recorded by ADR.
* **Enclosure and Manufacturing:** Functional airflow, filtration, cooling, acoustics, structure, cable routing, serviceability, tolerances, fire-safe materials, shipping durability, stability, and brand identity.
* **Firmware and Controller:** Low-level initialization, device identity, secure boot participation, controller-first interaction, update/recovery support, and hardware management.

### 4.2 Operating System and Kernel
* **PYRAMID OS:** The production path begins with a hardened, immutable Linux-based foundation using a signed boot chain where hardware permits, a read-only base, atomic A/B updates, application sandboxing, secure wallet service, recovery, and controller-first AXIOM Shell.
* **PYRAMID Kernel:** The proprietary kernel workstream is mandatory V1 construction. Its initial target covers virtualized boot, memory management, interrupts and timers, scheduling, IPC, capability security, an initrd or simple filesystem, diagnostics, user-process launch, a test harness, and bounded networking/input milestones.
* **AXIOM GPU and Driver Program:** The production path begins behind mature host/vendor drivers while V1 also implements the graphics command/memory research harness, shader-backend experiments, display abstraction, scheduler integration, fixed-hardware prototype, conformance harness, frame capture, telemetry, and AXIOM RENDER compatibility layer.

### 4.3 Security and Storage
* **Secure Boot, Update, and Recovery:** The cryptographic chain of trust, read-only base system, signed package verification, inactive-partition deployment, rollback, and recovery environment.
* **AXIOM Secure Transport and Crypto:** Proprietary APIs around established and reviewed primitives; no unreviewed cryptographic primitives may protect production value or identity.
* **AXIOM FS:** The mandatory V1 filesystem program covers content-addressed packages, deduplication, encryption, atomic updates, snapshots, verification, streaming priority, repair, creator/project separation, and Chain/object integration.
* **AXIOM Image/Media:** Safe parsing, selected codec implementations, GPU-ready texture/media pipelines, streaming, transcoding, and broad import compatibility.

### 4.4 Execution and Modes
*   **PYRAMID Virtual Target:** The abstraction layer presenting a unified hardware interface to the AXVM.
*   **Mode Manager:** Handles transitions between PLAY, DEV, and NODE modes.
*   **Performance Profiler:** Enforces resource budgets and performance guarantees.
*   **Distributed Node Compute (DNC):** OS-level support for participating in the AXIOM-XIII distributed network.

## 5. Semantic Entities and Provisional Registry IDs

The names below are canonical concepts. The identifiers are **recommended registry aliases**, not source-assigned constants, and must be confirmed through the Semantic Project Graph ADR before use in durable data.

| Entity Name | Provisional Registry ID | Description |
| :--- | :--- | :--- |
| PYRAMID Target | `ENT-PYR-001` | The virtualized hardware target. |
| Hardware Tier P0 | `ENT-HW-P0` | Baseline hardware configuration. |
| Hardware Tier P3 | `ENT-HW-P3` | Maximum performance hardware configuration. |
| PYRAMID OS | `ENT-OS-PYRAMID` | The hardened Linux-based production operating environment. |
| PYRAMID Kernel | `ENT-KERNEL-PYRAMID` | The mandatory proprietary kernel implementation and replacement workstream. |
| PLAY Mode | `ENT-MOD-PLAY` | Standard execution mode. |
| DEV Mode | `ENT-MOD-DEV` | Developer execution mode. |
| NODE Mode | `ENT-MOD-NODE` | Distributed compute execution mode. |

## 6. State Machines and Transitions

### 6.1 Mode State Machine

The system operates in one of three primary modes, governed by the Mode Manager.

*   **State: INITIALIZING** -> Transitions to PLAY (default) or NODE (if configured).
*   **State: PLAY** -> Transitions to DEV (requires authentication) or NODE (user initiated).
*   **State: DEV** -> Transitions to PLAY.
*   **State: NODE** -> Transitions to PLAY.

**Transition constraints:**
* Mode changes must preserve the source requirement that PLAY, DEV, and NODE remain securely separated and that authenticated DEV access cannot expose wallet keys, system signing, validator secrets, other games, or private projects.
* Whether a transition requires process isolation, container/VM replacement, logout, or reboot is an open ADR and must be proven by the threat model and recovery tests rather than assumed here.
* NODE mode is explicit opt-in and must enforce resource, power, thermal, security, compensation, and user-consent policy.

## 7. API and Capability Contracts

### 7.1 PYRAMID Target API
*   `AllocateResources(ProfileID)`: Allocates CPU, GPU, and memory based on the specified performance profile.
*   `GetHardwareTier()`: Returns the current physical hardware tier (P0-P3).
*   `RequestModeSwitch(TargetMode)`: Initiates a transition to the requested mode.

### 7.2 Secure Boot API
*   `VerifyImage(ImageHash, Signature)`: Cryptographically verifies an OS or firmware update.
*   `InitiateRecovery()`: Reverts the system to the last known good state.

## 8. Command, Query, and Event Flows

### 8.1 Update Flow (Command)
1.  System Administrator issues `UpdateSystem` command.
2. The Secure Boot, Update, and Recovery service downloads the update package.
3. The service verifies the package signature using `VerifyImage`.
4. If successful, the service applies the update to the inactive partition.
5.  System reboots into the new partition.

### 8.2 Resource Allocation Flow (Query/Command)
1.  AXVM queries `GetHardwareTier`.
2.  AXVM requests resource allocation via `AllocateResources`.
3.  Performance Profiler verifies the request against the current mode and tier.
4.  OS kernel enforces the allocation via cgroups or equivalent mechanisms.

## 9. Data Ownership and Storage

* **System Partition (Read-Only):** Contains the production OS, core utilities, and immutable configuration; changes are controlled by the signed update and recovery service.
*   **User Partition (Encrypted):** Contains user data, DEV mode artifacts, and application state. Owned by the End User.
*   **Node Partition (Encrypted, Ephemeral):** Contains data related to distributed compute tasks. Owned by the DNC module.
*   **Filesystem (AXFS):** Enforces strict isolation between partitions and provides cryptographic integrity verification for all reads.

## 10. Dependency Graph

* **PYRAMID Virtual Target** depends on the **PYRAMID OS**, **PYRAMID Kernel compatibility boundary**, and **Performance Profiler**.
* **PYRAMID OS and Kernel** depend on **GPU/Drivers**, **Firmware/Controller**, and **AXIOM FS** interfaces.
* **Mode Manager** depends on **Secure Boot, Update, and Recovery** plus the selected OS isolation mechanism.
* **Secure Boot, Update, and Recovery** depends on **AXIOM Secure Transport and Crypto** APIs built around reviewed primitives.

## 11. Failure and Degraded Modes

*   **Hardware Failure (Non-Critical):** If a non-critical component fails (e.g., secondary storage), the system enters a degraded PLAY mode, alerting the user but maintaining core functionality.
*   **Thermal Throttling:** If thermal limits are exceeded, the Performance Profiler dynamically adjusts resource allocation, reducing performance to maintain system stability.
* **Update Failure:** If an update fails verification or causes a boot loop, the recovery service automatically reverts to the last-known-good partition and records signed diagnostics.
*   **Kernel Panic:** Triggers an immediate reboot and logs the event for analysis.

## 12. Security, Privacy, Provenance, and Legal

* **Security:** Third-party code executes inside least-privilege sandboxes. Secure boot prevents unauthorized system images, and the PYRAMID Kernel must prove capability isolation before any production replacement.
* **Privacy:** User data is encrypted at rest and in transit. NODE mode work is isolated from user content and requires explicit opt-in and resource policy.
* **Provenance:** Hardware, firmware, OS images, packages, and updates carry traceable identities, signatures, build provenance, and certification evidence appropriate to their assurance state.
* **Legal and licensing:** Linux-based production components require complete open-source license compliance. Proprietary PYRAMID Kernel, GPU, transport, crypto API, media, and filesystem work must preserve clean ownership and third-party notices.

## 13. Observability

*   **Metrics:** CPU/GPU utilization, memory usage, thermal data, filesystem I/O, network throughput.
* **Logging:** Kernel logs, secure-boot/update/recovery audit logs, mode-transition events, application crashes, device attestation results, and policy decisions.
*   **Tracing:** Distributed tracing for NODE mode tasks to monitor performance across the network.
*   All telemetry data is anonymized (unless in DEV mode with explicit consent) and transmitted via Secure Transport.

## 14. Performance and Resource Budgets

Exact CPU, GPU, memory, storage, boot-time, thermal, power, and network numbers are unresolved hardware ADRs and must not be invented in this document. V1 must implement enforceable provisional profiles and produce measured reports:

| Profile | Canonical target | Required evidence |
|---|---|---|
| **PYRAMID Quality** | High visual fidelity, minimum 30 fps target, reconstructed or native high-resolution output, hybrid/ray-traced features where supported | Frame-time distribution, memory high-water marks, streaming pressure, thermal/power envelope, image-quality captures |
| **PYRAMID Performance** | 60 fps target with scalable geometry, lighting, effects, and responsive action gameplay | CPU/GPU budgets, input latency, frame pacing, shader/pipeline cache behavior, sustained thermal results |
| **PYRAMID Competitive** | 120 fps target where supported, reduced latency/settings, and Arena integrity profile | End-to-end input latency, stable frame pacing, anti-cheat/attestation overhead, network jitter, integrity evidence |

The Virtual Target must model selected CPU/GPU feature classes, memory, storage bandwidth, controller/display/audio capabilities, network assumptions, secure storage, operating APIs, thermal/power envelopes, and package/update format. Every number must be traceable to the chosen hardware profile and benchmark corpus.

## 15. Test Pyramid and Acceptance Tests

*   **Unit Tests:** Firmware logic, cryptographic primitives, filesystem integrity checks.
*   **Integration Tests:** Mode transitions, resource allocation enforcement, update/recovery flows.
*   **System Tests:** End-to-end boot process, thermal management under sustained load, NODE mode task execution.

**Concrete Acceptance Tests:**
*   `Test_SecureBoot_RejectsInvalidSignature`: Verify that the system refuses to boot an OS image with an invalid cryptographic signature.
*   `Test_ModeTransition_PlayToDev`: Verify that transitioning from PLAY to DEV mode successfully unlocks developer tools and disables production network access.
*   `Test_PerformanceProfile_P0_Enforcement`: Verify that a process cannot exceed the resource limits defined for the P0 hardware tier.

## 16. V1 Definition of Done

*   All P0-P3 hardware specifications finalized and certified.
* The Linux-based PYRAMID OS production path and the mandatory V1 PYRAMID Kernel implementation are both integrated behind explicit replacement and activation boundaries.
*   Secure boot, update, and recovery mechanisms functional and audited.
*   PLAY, DEV, and NODE modes fully operational with seamless transitions.
*   All features mandated by the OWNER-DIRECTIVE-V1-BUILD-COMPLETE (including experimental and future capabilities) are implemented, tested, and integrated, regardless of activation gates.
*   Comprehensive documentation (this specification) completed and approved.

## 17. Work Packages (Dependency Order)

1.  **WP1: Hardware Certification (P0-P3) & Enclosure:** Finalize physical specifications and manufacturing processes.
2. **WP2: Firmware and Secure Boot/Update/Recovery:** Develop the bootloader interfaces, verified boot chain, A/B update path, rollback, and recovery environment.
3. **WP3: PYRAMID OS and Kernel:** Implement the hardened Linux production image and the proprietary kernel workstream with conformance boundaries and independent test plans.
4. **WP4: AXIOM GPU and Driver Program:** Integrate mature production drivers and construct the fixed-hardware proprietary command, memory, shader, scheduling, conformance, and telemetry path.
5. **WP5: AXIOM FS, Secure Transport, Crypto, and Media:** Implement the proprietary APIs and workstreams around established primitives, safe parsing, content-addressed packages, encryption, atomic updates, and test harnesses.
6.  **WP6: Mode Manager & DNC Integration:** Develop the state machine for PLAY/DEV/NODE modes and distributed compute logic.
7.  **WP7: System Integration & Testing:** End-to-end validation of all components against the V1 Definition of Done.

## 18. Open ADRs (Architecture Decision Records)

* **ADR-020:** PYRAMID P1 reference hardware class and performance-profile budgets.
* **ADR-021:** PYRAMID OS distribution/base, immutable-image strategy, update, and recovery design.
* **ADR-022:** PYRAMID Kernel architecture, boot target, privilege model, and replacement evidence.
* **ADR-023:** GPU/driver production boundary, fixed-hardware target, and conformance criteria.
* **ADR-024:** AXIOM Secure Transport/Crypto/FS/Image scope, established primitives, and audit requirements.
* **ADR-025:** PLAY/DEV/NODE isolation and mode-transition mechanism.
* **ADR-026:** P2/P3 custom board and silicon program economics, capital gates, toolchain, and prototype milestones.

## 19. Explicit Interfaces with Other Domains

*   **AXVM Domain:** Provides the PYRAMID Target API for resource allocation and execution context.
*   **Network Domain:** Interfaces via Secure Transport for updates, telemetry, and NODE mode communication.
*   **Application/Game Engine Domain:** Consumes the GPU drivers and filesystem APIs provided by the OS.

---
*End of Specification*
