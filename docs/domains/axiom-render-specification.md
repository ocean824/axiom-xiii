# AXIOM RENDER Domain Specification

## 1. Purpose and Non-Negotiable Doctrine

AXIOM RENDER is the advanced rendering architecture for AXIOM-XIII, designed to simultaneously achieve two demanding visual profiles: large authored fantasy worlds with long sightlines and dense geometry, and extreme perceptual realism driven by physically convincing materials, lighting, optics, and motion [1].

The primary doctrine governing this domain is that AXIOM projects must be capable of contemporary AAA-scale fidelity through AXIOM-owned systems and terminology [1]. It must not be permanently capped at mobile, browser, low-poly, or small-scene use cases [2]. Furthermore, following the V1 Build-Complete directive, all described future, preview, experimental, architected, deferred, or later capabilities—including path tracing, advanced geometry classes, and server-cell/world features—are mandatory V1 architecture, code, integration, and test scope [3]. Gates may restrict activation or production exposure, but they must never restrict construction [3].

## 2. Personas and Actors

The primary personas interacting with AXIOM RENDER include:
- **Technical Artists and Shading Engineers:** Authoring `.axmat` and `.axfx` graphs, managing shader permutations, and defining visual quality profiles [1].
- **Environment and World Builders:** Utilizing WORLDSTREAM and NEXUS to construct large-scale topologies, manage streaming budgets, and place dense vegetation [1].
- **Engine Programmers:** Integrating rendering pipelines with AXIOM FABRIC, maintaining the frame graph, and optimizing GPU/CPU memory [1] [4].
- **AI Agents (e.g., AXIOM AI, MAESTRO, MOTION):** Generating semantic materials, optimizing scene visibility, and predicting streaming requirements [1] [5].
- **Players/End Users:** Experiencing the final rendered output, bound by performance profiles and accessibility overrides [1] [6].

## 3. Domain Boundaries

AXIOM RENDER is responsible for the complete visual output of the engine. It interfaces with but does not own:
- **AXIOM FABRIC:** The job graph and scheduler that dispatches rendering tasks [4].
- **AXIOM CORE (ECS):** The entity and component data that drives visual representation [4].
- **ORPHEUS:** The audio engine, though they may share spatial data for occlusion [5].
- **Physics and Simulation:** Which drive destruction and character movement, while AXIOM RENDER handles the visual representation of these events [5].
- **AXIOM UI:** Which handles engine-native 2D/vector/text rendering overlaid on the 3D scene [5].

## 4. Named Components, Modules, and Responsibilities

The AXIOM RENDER domain is divided into several highly specialized modules, each responsible for a critical aspect of the final image. These modules are designed to operate concurrently where possible, leveraging AXIOM FABRIC for efficient scheduling.

| Module | Responsibility |
|---|---|
| **NEXUS** | The core geometry virtualization and visibility system. NEXUS handles the ingestion, clustering, and GPU-driven culling of triangle meshes, terrain, voxels, point clouds, and procedural geometry. It is responsible for ensuring that only the optimal level of detail for visible geometry is submitted to the rasterizer, maintaining stable frame times even in densely populated scenes [1]. |
| **PHOTON** | The hybrid lighting and reflection architecture. PHOTON dynamically selects between hardware ray tracing, software ray tracing, probes, and screen-space techniques based on the scene's requirements and the active quality profile. It manages global illumination, dynamic shadows, emissive contributions, and includes a path-tracing mode for cinematic rendering and reference validation [1]. |
| **WORLDSTREAM** | The hierarchical world and asset streaming engine. WORLDSTREAM manages the loading and eviction of assets based on spatial partitioning, camera velocity, and predictive AI models. It supports seamless transitions across large topologies, world variants (e.g., seasons, destruction states), and coordinates with server cells for authoritative multiplayer environments [1]. |
| **OPTICS** | The physical and stylized camera system. OPTICS models the camera as a physical sensor, simulating focal length, aperture, depth of field, motion blur, lens distortion, and auto-exposure. It ensures that the final image respects cinematic art direction while providing safe overrides to maintain competitive integrity in gameplay [1]. |
| **MATERIALS** | The physically based and stylized surface system. This module evaluates `.axmat` graphs, supporting complex surface interactions such as subsurface scattering, clearcoat, anisotropy, and layered blending (e.g., dirt, wetness, snow). It also integrates with AI for semantic material generation [1]. |
| **ATMOSPHERE** | The volumetric sky and weather system. ATMOSPHERE simulates physically based scattering, time of day, fog, volumetric clouds, and localized weather fronts. It interacts closely with PHOTON for sky lighting contribution and MATERIALS for environmental surface blending [1]. |
| **WATER** | The fluid surface and underwater rendering system. WATER handles oceans, lakes, and rivers, providing reflections, refractions, foam generation, and flow fields. It also exposes buoyancy hooks for physics integration [1]. |
| **VEGETATION** | The dense instancing and interaction system for flora. VEGETATION manages the efficient rendering of massive amounts of foliage, applying wind simulation, interaction bending, and seasonal state changes while adhering to strict streaming and culling budgets [1]. |
| **CHARACTER** | The specialized rendering path for humanoids and creatures. CHARACTER handles the complex shading requirements of skin, eyes, hair, and cloth. It supports both high-fidelity cinematic models and stylized profiles, integrating with the animation system for deformation and motion matching [1]. |
| **FX** | The particle and fluid simulation visualizer. FX manages the rendering of `.axfx` systems, including sparks, smoke, destruction debris, and decals, ensuring they composite correctly with the scene's lighting and depth [1]. |
| **DEBUG** | The internal suite of validation and profiling tools. DEBUG provides developers with real-time visualizations of geometry costs, lighting caches, and streaming residency, along with automated capture tools for visual regression testing [1]. |



## 5. Canonical Entities and Stable IDs

AXIOM RENDER relies on stable, globally namespaced identifiers for all resources, ensuring safe serialization, network replication, and AI comprehension [4].

- `ax_nexus_cluster`: Represents a spatial partition of geometry within NEXUS.
- `ax_photon_probe`: A lighting probe used for indirect diffuse lighting and reflections.
- `ax_worldstream_cell`: A streaming unit within the WORLDSTREAM hierarchy.
- `ax_optics_rig`: A reusable camera configuration.
- `ax_material_graph` (`.axmat`): A defined surface material model.
- `ax_fx_system` (`.axfx`): A particle or fluid simulation system.

## 6. State Machines and Transitions

The rendering pipeline relies on several internal state machines to manage resources efficiently and ensure visual stability. These state machines are tightly coupled with WORLDSTREAM and AXIOM FABRIC.

### 6.1 WORLDSTREAM Asset State Machine
Assets (textures, meshes, audio) managed by WORLDSTREAM transition through the following states to balance memory usage and visual fidelity:
1.  **Unloaded:** The asset resides on disk; no memory is allocated.
2.  **Requested:** The asset is scheduled for loading based on predictive algorithms or immediate camera proximity.
3.  **Streaming:** The asset data is actively being read from disk and decompressed into memory.
4.  **Resident:** The asset is fully loaded into memory but may not yet be active in the scene.
5.  **Active:** The asset is currently bound to the rendering pipeline and contributing to the frame.
6.  **Evicting:** The asset is marked for removal due to memory pressure or distance, pending the completion of any active rendering commands.

### 6.2 NEXUS Visibility State Machine
Geometry clusters within NEXUS undergo rapid state transitions every frame to optimize GPU workload:
1.  **Frustum Culled:** The cluster is entirely outside the camera's view frustum and is discarded immediately.
2.  **Occluded:** The cluster is within the frustum but hidden behind other opaque geometry (determined via hierarchical Z-buffer occlusion culling).
3.  **Visible (LOD Evaluated):** The cluster is visible. NEXUS evaluates error metrics to select the appropriate level of detail (LOD) or fallback representation (e.g., impostor) before submission.

### 6.3 PHOTON Cache State Machine
Lighting caches (e.g., probes, voxel grids) managed by PHOTON transition to ensure accurate indirect illumination:
1.  **Invalidated:** A significant scene change (e.g., moving light source, destruction) has rendered the cache data obsolete.
2.  **Rebuilding:** AXIOM FABRIC dispatches background compute jobs to recalculate the lighting data.
3.  **Valid:** The cache accurately reflects the current scene state and is used for rendering.
4.  **Stale:** Minor scene changes have occurred; the cache is still used but scheduled for a low-priority refresh to maintain temporal stability.



## 7. API and Capability Contracts

AXIOM RENDER exposes capabilities via AXIOM Connect and typed C++ APIs [4] [7].

- **Render Submission API:** Accepts draw commands, compute dispatches, and state changes from AXIOM FABRIC [4].
- **Streaming Request API:** Allows WORLDSTREAM to request asset pages based on camera position, velocity, and AI prediction [1].
- **Material Parameter API:** Enables runtime modification of `.axmat` properties for dynamic effects (e.g., wetness, damage) [1].
- **Camera Override API:** Allows gameplay logic to safely override OPTICS settings for accessibility or competitive integrity [1].

## 8. Command, Query, and Event Flows

- **Command:** `SetQualityProfile(profile_id)` - Triggers a re-evaluation of rendering budgets, shader permutations, and LOD biases.
- **Query:** `GetVisibilityStatus(entity_id)` - Returns the current occlusion and LOD state of an entity via NEXUS.
- **Event:** `OnWeatherChanged(weather_state)` - Broadcasts atmospheric changes, prompting updates to ATMOSPHERE, WATER, and MATERIAL (wetness) systems.

## 9. Data Ownership and Storage

AXIOM RENDER owns the compiled runtime representations of geometry, materials, and shaders [4]. Authoring data (e.g., source meshes, raw textures) is owned by the asset pipeline [4]. Runtime data is stored in tagged allocators, arenas, and GPU memory, managed by AXIOM Memory with strict streaming budgets [4].

## 10. Dependency Graph

AXIOM RENDER sits atop several foundational engine systems, forming a strict dependency hierarchy to ensure stable execution and memory safety.

1.  **AXIOM Memory (Base Dependency):**
    *   AXIOM RENDER relies entirely on AXIOM Memory for all allocations. This includes tagged allocators for CPU-side structures, arenas for frame-local data, and strict GPU memory tracking to enforce streaming budgets [4]. Unbounded caches within the renderer are strictly prohibited.
2.  **Platform Abstraction Layer:**
    *   The renderer interfaces with the host OS through the Platform Abstraction layer. This provides access to windowing systems, input devices, and the underlying graphics APIs (Vulkan, Direct3D 12). Experimental proprietary APIs (e.g., PYRAMID GPU stack) must also conform to this abstraction [4].
3.  **AXIOM FABRIC (Task Scheduling):**
    *   All rendering workloads are dispatched as jobs to AXIOM FABRIC. This includes frame-critical submission tasks (Priority Class 3), streaming and decompression (Priority Class 5), and background shader compilation (Priority Class 8) [4]. The renderer's frame graph must synchronize with FABRIC's dependency resolution.
4.  **Asset Database and Schema Registry:**
    *   AXIOM RENDER queries the Asset Database to retrieve cooked `.axpkg` content (meshes, textures, shaders). It relies on the Schema Registry to deserialize these assets safely and understand version migrations [4].
5.  **AXIOM CORE (ECS):**
    *   The renderer consumes entity and component data from AXIOM CORE. While the authoring graph may be hierarchical, the runtime renderer operates on flattened, data-oriented component arrays to maximize cache coherency during draw call generation [4].



## 11. Failure and Degraded Modes

To maintain a stable user experience, AXIOM RENDER must gracefully handle resource exhaustion, performance spikes, and missing data without crashing the engine.

### 11.1 VRAM and System Memory Exhaustion
When GPU or system memory approaches defined budget limits, the renderer initiates a cascading degradation protocol:
1.  **Aggressive Eviction:** WORLDSTREAM immediately evicts "Resident" but inactive pages and reduces the predictive streaming radius.
2.  **Texture Down-resing:** The mipmap bias is aggressively increased, forcing the use of lower-resolution textures.
3.  **Geometry Fallback:** NEXUS forces geometry into lower LOD states or replaces distant meshes with 2D impostors/billboards, bypassing standard error metrics [1].

### 11.2 Frame Time Misses (Performance Degradation)
If the renderer consistently exceeds its allocated frame time budget (e.g., missing the 16.67ms target for 60fps), it employs dynamic scaling:
1.  **Dynamic Resolution Scaling (DRS):** The internal rendering resolution is dynamically lowered, relying on temporal upscaling to maintain output fidelity [6].
2.  **Feature Disabling:** Expensive PHOTON features, such as hardware ray tracing or high-sample-count volumetric fog, are temporarily disabled or reduced in quality.
3.  **Animation/Physics Decoupling:** Visual updates are decoupled from the simulation tick, allowing the game logic to proceed while the renderer catches up.

### 11.3 Missing or Corrupted Assets
1.  **Shader Compilation Failure:** If a shader fails to compile (e.g., due to a syntax error in an imported `.axmat`), the renderer must fall back to a highly visible default error shader (e.g., bright magenta) to alert developers, rather than crashing [1].
2.  **Missing Geometry/Textures:** Missing assets are replaced with default placeholder meshes (e.g., a standardized "missing asset" cube) and default grid textures.



## 12. Security, Privacy, Provenance, and Legal Considerations

- **Untrusted Shaders:** Custom shaders from user-generated packages must be sandboxed and validated to prevent GPU hangs or memory exposure [1] [7].
- **Asset Provenance:** All generated or imported textures, materials, and geometry must retain source, tool, prompt owner, license, and derivative-use metadata (`AX-IP-001`) [1] [7].
- **Privacy:** Render captures and telemetry must not inadvertently record sensitive desktop overlays or private user information [6].
- **Proprietary Replacements:** Experimental replacements for graphics APIs or shader compilers must sit behind AXIOM interfaces and undergo rigorous security review before production qualification [2] [3].

## 13. Observability and Telemetry

Comprehensive observability is critical for maintaining performance budgets and diagnosing visual anomalies across diverse hardware configurations. AXIOM RENDER integrates deeply with the engine's telemetry and debugging infrastructure.

### 13.1 Developer and Profiler Views
AXIOM RENDER exposes real-time, in-engine visualizations for developers:
-   **NEXUS Cost View:** Color-codes geometry based on triangle density, overdraw, and culling efficiency.
-   **WORLDSTREAM Residency:** Visualizes the spatial bounds of loaded asset pages and their current state machine status.
-   **PHOTON Light Complexity:** Highlights areas of the scene where overlapping dynamic lights or expensive reflection probes exceed recommended budgets.
-   **Memory Heatmap:** Displays current VRAM allocation categorized by resource type (textures, buffers, render targets) against the defined budget [1] [4].

### 13.2 Automated Captures and Tracing
-   **GPU Frame Captures:** The engine can trigger automated GPU captures (e.g., via RenderDoc or PIX integration) when specific performance thresholds are breached or visual assertions fail during Gauntlet testing [6].
-   **Correlated Tracing:** Rendering events (e.g., `SubmitDrawCalls`, `CompileShader`) are emitted as trace spans with correlation IDs, allowing them to be linked to specific AXIOM FABRIC jobs, network events, or AI agent actions [6].

### 13.3 Production Telemetry
In production builds, AXIOM RENDER collects anonymized, sampled telemetry to monitor ecosystem health:
-   **Frame-Time Distributions:** Aggregated histograms of frame times (e.g., 1st, 50th, 99th percentiles) rather than simple average FPS, providing a true measure of hitching and stuttering [6].
-   **Hardware Demographics:** Data on the distribution of graphics APIs (Vulkan vs. DX12), GPU memory capacities, and feature support (e.g., ray tracing capabilities) to inform future optimization priorities.
-   **Crash Dumps:** Minidumps correlated with the active quality profile and rendering state at the time of failure. All telemetry must respect the global privacy policy and redact sensitive user data [6].



## 14. Performance and Resource Budgets

AXIOM RENDER operates under strict, project-defined performance profiles [6]:
- **AAA Quality:** Stable 30 fps, high-quality lighting, dense geometry.
- **AAA Performance:** Stable 60 fps, responsive action, scalable ray tracing.
- **Competitive:** 120 fps, strict latency budgets, reduced visual variability.

Provisional 60 fps frame budget (example):
- GPU geometry/material: 4.0 ms
- GPU lighting/post: 4.0 ms
- Rendering CPU submission: 1.5 ms [6]

## 15. Test Pyramid and Concrete Acceptance Tests

Testing for AXIOM RENDER includes:
- **Unit Tests:** Math library correctness, frustum culling logic, bounding box calculations [6].
- **Integration Tests:** NEXUS cluster generation, WORLDSTREAM page loading, PHOTON cache invalidation [6].
- **Visual Regression:** Automated rendering of reference scenes (e.g., high-end material and atmosphere scenes) with pixel-comparison thresholds [6] [7].
- **Performance Benchmarks:** Continuous measurement of frame times and memory usage against defined budgets on reference hardware [6].

## 16. V1 Definition of Done

AXIOM RENDER V1 is considered complete when:
- NEXUS clustered geometry, WORLDSTREAM, PHOTON baseline, OPTICS, high-end materials, atmosphere, water, vegetation, character rendering, and debugging tools are fully implemented and integrated [7].
- A representative high-fidelity environment and character scene meets defined frame, memory, loading, and visual-quality targets on reference hardware [7].
- All capabilities, including path tracing and advanced geometry classes, are coded, integrated, and testable, even if gated from production exposure [3].
- First-party validation (e.g., UNDERSCRIPT: YOKAI, MACHINA: GHOST OF THE SOUND) confirms the renderer supports the required visual and performance profiles [7].

## 17. Work Packages in Dependency Order

1. **AX-REN-001:** Renderer architecture targeting contemporary AAA world scale [7].
2. **AX-REN-002 (Epic 68):** NEXUS cluster builder and runtime prototype [7].
3. **AX-REN-004 (Epic 69):** WORLDSTREAM cell and page system [7].
4. **AX-REN-003 (Epic 70):** PHOTON direct and dynamic indirect baseline [7].
5. **AX-REN-005 (Epic 71):** OPTICS camera pipeline [7].
6. **Epic 72:** High-end material and atmosphere reference scene [7].
7. **Epic 73:** Performance and visual regression harness [7].

## 18. Open ADRs

Mandatory ADRs (Architecture Decision Records) are required for:
- Renderer architecture changes (e.g., backend selection, frame graph design) [7].
- Shader compiler and graphics API replacement strategies [7].
- Integration of advanced geometry classes (e.g., Gaussian splats) into NEXUS [1].

## 19. Explicit Interfaces with Other AXIOM Domains

- **AXIOM Bridge:** Imports Unreal materials (`.uasset`) and translates them into `.axmat` graphs [7].
- **AXIOM Chain/Arena:** Ensures competitive rendering profiles (e.g., disabled foliage, fixed exposure) are strictly enforced during real-value tournaments to maintain integrity [1] [7].
- **AXIOM AI (MAESTRO/MOTION):** Interfaces with CHARACTER rendering for semantic material generation and procedural locomotion [1] [5].

## References

[1] ../source/AXIOM-XIII-V1-Master-Specification.md (Lines 2130-2496)
[2] ../source/AXIOM-XIII-V1-Master-Specification.md (Lines 1-500)
[3] ../source/OWNER-DIRECTIVE-V1-BUILD-COMPLETE.md
[4] ../source/AXIOM-XIII-V1-Master-Specification.md (Lines 1618-2000)
[5] ../source/AXIOM-XIII-V1-Master-Specification.md (Lines 2400-2800)
[6] ../source/AXIOM-XIII-V1-Master-Specification.md (Lines 4560-4825)
[7] ../source/AXIOM-XIII-V1-Master-Specification.md (Lines 5243-6255)
