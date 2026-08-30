# Initial 100 Implementation Tickets

**Status:** Derived backlog for controlled import into GitHub or CodeSpring. The first eighty entries preserve the ordering and intent of section 79 of the master specification; entries 81–100 operationalize the bootstrap delivery package. No ticket authorizes production deployment or real-value activation.

| ID | Title | Depends on | Requirement links | Acceptance summary |
|---:|---|---|---|---|
| AX-001 | Establish monorepo and governance baseline | None | AX-LIC-001, AX-LIC-002, AX-SEC-001 | Repository tree, protected-branch plan, ownership process, and private-access policy are documented |
| AX-002 | Create ADR, RFC, requirement, and evidence tooling | AX-001 | AX-QA-001 | Templates validate and every change can link requirements and decisions |
| AX-003 | Define AXIOM IDs and schema conventions | AX-002 | AX-FMT-002, AX-FMT-003 | Stable namespaced identifiers, versioning, serialization, and compatibility rules have fixtures and tests |
| AX-004 | Define `.axiom` v0 manifest and project layout | AX-003, ADR-0003 | AX-FMT-001, AX-FMT-002 | Human-readable manifest, schema version, stable IDs, dependencies, permissions, and migration policy are defined |
| AX-005 | Implement local project registry | AX-004 | AX-FMT-001 | Registry creates, discovers, opens, and removes local project entries without owning canonical project data |
| AX-006 | Implement logging, errors, configuration, feature flags, and crash IDs | AX-003 | AX-QA-001, AX-SEC-001 | Structured logs and correlation IDs exist; flags require owner and expiry; secrets are redacted |
| AX-007 | Implement development package and signing keys | AX-001, AX-006 | AX-SEC-002 | Development-only signatures work; keys are excluded from source and cannot be confused with production keys |
| AX-008 | Build SBOM and provenance pipeline | AX-002, AX-003 | AX-IP-001, AX-SEC-002 | A sample build emits dependency, license, source, hash, and provenance records |
| AX-009 | Build controller-first Shell frame | AX-001, ADR-0005 | AX-PROD-001 | Shell starts locally and can be operated with controller focus semantics |
| AX-010 | Implement seven locked top-level tabs | AX-009 | AX-PROD-002, AX-PROD-003 | GAMES, MEDIA, SOCIAL, DEV, STORE, PROFILE, WALLET appear exactly; CREATE is absent |
| AX-011 | Implement Home dashboard | AX-009, AX-010 | AX-PROD-001 | Dashboard loads bounded, privacy-safe local modules and supports controller navigation |
| AX-012 | Implement local profile and account sandbox | AX-006, AX-009 | AX-SEC-001 | Multiple local profiles switch safely without exposing private identity or wallet data |
| AX-013 | Implement GAMES library and install manifest | AX-004, AX-005, AX-009 | AX-FMT-001 | A local sample build installs, appears in GAMES, launches, repairs, and uninstalls |
| AX-014 | Implement DEV mode routing | AX-009, AX-010 | AX-DEV-001 | DEV routes to Simple and Advanced views for the same selected project |
| AX-015 | Implement STORE sandbox shell | AX-009, AX-010 | AX-STO-001 | Store UI uses sandbox data only and performs no external purchase or production action |
| AX-016 | Implement WALLET sandbox shell | AX-009, AX-010 | AX-WAL-001 | Wallet UI clearly labels mock balances and isolates trusted confirmation surfaces |
| AX-017 | Implement accessibility and input navigation baseline | AX-009, AX-010 | AX-PROD-001 | Remapping, focus order, scalable text, screen-reader metadata, captions hooks, and keyboard/controller tests pass |
| AX-018 | Define platform, window, and input abstraction | ADR-0002, ADR-0005 | AX-ENG-002, AX-ENG-003 | Interfaces compile on target development hosts and expose no permanent vendor-specific public types |
| AX-019 | Implement Core ECS v0 | AX-003, ADR-0002, ADR-0006 | AX-ENG-001 | Entities, components, systems, stable external IDs, and deterministic ordering pass tests |
| AX-020 | Implement FABRIC scheduler v0 | AX-019, ADR-0002 | AX-ENG-001 | Dependency jobs, priorities, cancellation, deterministic mode, and timing telemetry pass tests |
| AX-021 | Implement reflection and schema generator v0 | AX-003, AX-019 | AX-FMT-003 | Metadata is generated, versioned, queryable, and registered without fragile manual-only registration |
| AX-022 | Implement serialization and migration v0 | AX-003, AX-021 | AX-FMT-001, AX-FMT-003 | Bounded versioned round trips, migrations, corruption detection, and cache rebuild tests pass |
| AX-023 | Implement asset database and importer v0 | AX-003, AX-008, AX-022 | AX-IP-001 | Assets receive stable IDs, hashes, provenance, licenses, dependency records, and bounded import behavior |
| AX-024 | Implement renderer frame graph and mesh/material/camera v0 | AX-018, AX-020, AX-023, ADR-0007 | AX-ENG-001, AX-REN-001 | A deterministic sample scene renders with captured frame and resource telemetry |
| AX-025 | Implement scene, world, and entity authoring v0 | AX-019, AX-022, AX-024 | AX-ENG-001, AX-FMT-003 | A scene can be edited, saved, reopened, diffed, and rebuilt from canonical source |
| AX-026 | Implement UI runtime v0 | AX-018, AX-024, ADR-0005 | AX-ENG-001 | Runtime UI renders, accepts mapped input, exposes accessibility metadata, and respects secure-surface separation |
| AX-027 | Implement build, package, and launch v0 | AX-004, AX-007, AX-008, AX-024 | AX-FMT-001, AX-ENG-002, AX-SEC-002 | Clean build produces attributable package, install manifest, SBOM, signature, and launchable sample |
| AX-028 | Implement physics adapter v0 | AX-019, ADR-0008 | AX-ENG-003 | Basic collision and character queries work behind AXIOM types with replacement conformance tests |
| AX-029 | Implement animation, audio, save, and network baselines | AX-019, AX-022, AX-024, ADR-0009, ADR-0010 | AX-AUD-001, AX-NET-001 | Minimal sample animates, plays audio, saves/loads, and connects using bounded baseline interfaces |
| AX-030 | Implement Simple conversation and viewport shell | AX-014, AX-025 | AX-AI-001, AX-DEV-001 | Simple view can inspect a project and display conversation, selection, and viewport context |
| AX-031 | Implement Advanced project, world, code, logic, and test shell | AX-014, AX-025 | AX-DEV-001 | Advanced view exposes direct edits and test surfaces without converting the project |
| AX-032 | Share selection and context across DEV modes | AX-030, AX-031 | AX-DEV-002 | Selection, edit history, state, and project identity persist across repeated mode switches |
| AX-033 | Define AXIOM Connect capability schema v0 | AX-003, AX-081 | AX-AI-006 | Capability subject, resource, action, scope, expiry, budget, approval, and audit fields validate |
| AX-034 | Implement PRIME service v0 | AX-033 | AX-AI-003, AX-AI-005 | PRIME routes a bounded task without becoming dependent on one model provider |
| AX-035 | Implement Intent Compiler v0 | AX-003, AX-034 | AX-AI-002, AX-AI-003 | User intent yields traceable requirements, constraints, risks, and candidate tests without implementation |
| AX-036 | Implement planner and task graph v0 | AX-035 | AX-AI-003 | Plan produces dependency-ordered tasks, owners, budgets, acceptance criteria, and stop conditions |
| AX-037 | Implement model router v0 | AX-034, ADR-0023 | AX-AI-005 | Provider and local-model adapters support fallback, policy selection, logging, and test substitution |
| AX-038 | Implement capability broker and permissions | AX-033, AX-081 | AX-AI-006, AX-SEC-001 | Positive and negative authorization tests prove scoped least privilege |
| AX-039 | Implement agent sandbox and worktree runner | AX-001, AX-038 | AX-AI-006, AX-SEC-001 | Agents write only inside assigned worktrees and cannot access protected targets or secrets |
| AX-040 | Implement Gauntlet v0 | AX-027, AX-036, AX-039 | AX-AI-003, AX-QA-001 | A change runs formatting, build, tests, scans, evidence capture, and bounded repair loops |
| AX-041 | Implement semantic project graph and index v0 | AX-003, AX-004, AX-021, AX-022 | AX-FMT-003 | Graph links requirements, assets, entities, code, tests, decisions, provenance, and builds and rebuilds from source |
| AX-042 | Implement change and evidence package v0 | AX-006, AX-008, AX-040, AX-041 | AX-QA-001 | Every accepted change emits human-readable and machine-readable evidence with rollback |
| AX-043 | Enforce Ask, Plan, and Build states | AX-034, AX-035, AX-036, AX-038, AX-039 | AX-AI-002, AX-AI-006 | Ask cannot write; Plan cannot implement; Build requires scope and consequence-tier approval |
| AX-044 | Implement `.uproject` inventory parser | AX-022, AX-023 | AX-BRG-001 | Parser inventories projects using bounded untrusted-input handling and reports unsupported structures |
| AX-045 | Implement dependency, plugin, and license inventory | AX-008, AX-044 | AX-BRG-002, AX-IP-001 | Report identifies dependencies, plugins, source ownership, licenses, and portability risks |
| AX-046 | Implement source asset importer | AX-023, AX-044, AX-045 | AX-BRG-001 | Supported assets import to native IDs/formats with hashes, provenance, warnings, and rollback |
| AX-047 | Prototype material and world conversion | AX-024, AX-025, AX-046 | AX-BRG-001, AX-BRG-002 | Selected corpus converts with category-specific quality and unsupported-item results |
| AX-048 | Prototype C++ and Blueprint semantic analyzer | AX-035, AX-041, AX-044 | AX-BRG-001, AX-BRG-002 | Analyzer distinguishes portable project logic from engine-owned or unsupported constructs |
| AX-049 | Implement compatibility report UI | AX-045, AX-046, AX-047, AX-048 | AX-BRG-002 | UI reports explicit denominators by category and never silently deletes code or assets |
| AX-050 | Implement identity and authentication service | AX-003, AX-081, ADR-0017 | AX-SEC-001 | Local/sandbox identity flow enforces purpose separation, audit, recovery, and data classification |
| AX-051 | Implement social, presence, and party service | AX-050, ADR-0017 | AX-PROD-001 | Sandbox friends, presence, parties, moderation hooks, and privacy controls pass integration tests |
| AX-052 | Implement project object storage and sync | AX-004, AX-022, AX-041, ADR-0017 | AX-FMT-002, AX-FMT-003 | Sync preserves canonical source, conflict visibility, encryption, export, and recovery |
| AX-053 | Implement media capture and replay metadata | AX-006, AX-024, AX-029 | AX-QA-001 | Local screenshot/video/replay metadata includes build, rights, performance, and provenance references |
| AX-054 | Implement Store catalog and entitlement sandbox | AX-027, AX-050, ADR-0015 | AX-STO-001 | Sandbox purchase, install, launch, update, refund, repair, and offline policy pass |
| AX-055 | Implement payment and ledger sandbox | AX-050, ADR-0015 | AX-STO-001 | Mock fiat, token, reward, tax, and refund ledgers remain technically separated and reconcile |
| AX-056 | Implement telemetry and support baseline | AX-006, AX-050, ADR-0023 | AX-SEC-001 | Correlated, privacy-classified logs and support bundle export work with configurable retention |
| AX-057 | Implement policy engine v0 | AX-003, AX-050, ADR-0016, ADR-0023 | AX-ARN-003 | Versioned sandbox policies evaluate operator, region, age, feature, and risk with reasons and appeals |
| AX-058 | Draft AXIOM Chain specification and RFC | AX-002, AX-003, ADR-0011, ADR-0012, ADR-0013 | AX-CHN-001, AX-CHN-002 | RFC defines mission, boundaries, state, execution, threat model, benchmarks, and non-goals |
| AX-059 | Implement consensus simulation | AX-058 | AX-CHN-001, AX-QA-002 | Deterministic simulation covers faults, partitions, byzantine behavior, recovery, and reproducible metrics |
| AX-060 | Implement node, state, and execution skeleton | AX-058, AX-059 | AX-CHN-001 | Testnet-only node processes signed test transactions and passes invariants without real value |
| AX-061 | Implement wallet core and trusted signing UI | AX-050, AX-060, ADR-0014 | AX-WAL-001, AX-SEC-001 | Managed and self-custody sandbox flows separate keys and prevent untrusted UI from replacing confirmation |
| AX-062 | Implement digital object, license, and royalty modules | AX-003, AX-008, AX-060 | AX-CHN-002, AX-IP-001 | Test objects carry explicit rights, provenance, transfer rules, and royalty invariants without implying copyright |
| AX-063 | Implement marketplace settlement module | AX-054, AX-055, AX-060, AX-062 | AX-CHN-002, AX-STO-001 | Sandbox sale, fee, royalty, refund, and failure reconciliation pass invariants |
| AX-064 | Implement tournament escrow and result module | AX-057, AX-060, AX-061, ADR-0016 | AX-ARN-001, AX-ARN-002 | Sponsor-funded test escrow locks before start and settles only on valid attested results |
| AX-065 | Implement matchmaker and rating prototype | AX-050, AX-051, ADR-0016 | AX-ARN-001 | Simulations report skill quality, wait time, latency, parties, smurf resistance, and uncertainty |
| AX-066 | Implement replay and evidence pipeline | AX-027, AX-029, AX-042 | AX-ARN-001, AX-QA-001 | Tamper-evident build-linked replay package supports verification and privacy-safe dispute review |
| AX-067 | Implement sponsored tournament end-to-end sandbox | AX-057, AX-061, AX-064, AX-065, AX-066 | AX-ARN-001, AX-ARN-002 | Tournament creates, plays, verifies, disputes, settles, and audits using test value only |
| AX-068 | Prototype NEXUS cluster builder and runtime | AX-020, AX-023, AX-024, ADR-0007 | AX-REN-002 | Static clustered geometry path demonstrates bounded streaming, fallback, and reproducible tests |
| AX-069 | Implement WORLDSTREAM cell and page system | AX-020, AX-023, AX-025 | AX-REN-004 | Hierarchical cells stream asynchronously within memory budgets and recover from failed predictions |
| AX-070 | Implement PHOTON lighting baseline | AX-024, AX-068, AX-069, ADR-0007 | AX-REN-003 | Direct lighting, dynamic shadows, reflections, emissive contribution, and volumetric baseline meet profile budgets |
| AX-071 | Implement OPTICS camera pipeline | AX-024 | AX-REN-005 | Physical/stylized controls work with competitive and accessibility overrides |
| AX-072 | Build high-end material and atmosphere reference scene | AX-068, AX-069, AX-070, AX-071 | AX-REN-001 | Versioned reference scene documents content, hardware, visual target, and known limitations |
| AX-073 | Implement performance and visual regression harness | AX-006, AX-024, AX-072 | AX-REN-001, AX-QA-001 | Frame-time distributions, memory, loading, captures, and threshold regressions are reproducible |
| AX-074 | Define PYRAMID Virtual Target profile and validator | AX-002, ADR-0019 | AX-PYR-001 | Profile declares API, memory, storage, shader, input, and performance constraints with validation tool |
| AX-075 | Prototype Linux-based PYRAMID OS image | AX-074, ADR-0020 | AX-PYR-002 | Non-production image boots on reference hardware/VM with verified configuration and update plan |
| AX-076 | Prototype controller boot-to-Shell | AX-009, AX-010, AX-075 | AX-PROD-001, AX-PYR-005 | Device boots directly to Shell and completes controller-only navigation and recovery tests |
| AX-077 | Produce P0 enclosure CAD and thermal study | ADR-0019 | AX-PYR-005 | Design addresses cooling, airflow, dust, structure, acoustics, serviceability, and safety assumptions |
| AX-078 | Prototype PYRAMID Kernel boot, memory, and scheduler | AX-074, ADR-0021 | AX-PYR-003 | Experimental target boots and runs isolated tests; no production dependency is introduced |
| AX-079 | Create AXIOM GPU research harness | AX-024, AX-074, ADR-0007, ADR-0019 | AX-PYR-004 | Harness runs shader correctness, conformance, crash, performance, and recovery experiments |
| AX-080 | Create secure transport, crypto, image, and filesystem research workspaces | AX-001, AX-081 | AX-PYR-004 | Each experimental workspace has owner, threat/performance model, tests, benchmark baseline, gate, and pause criterion |
| AX-081 | Approve threat model v0 and trust zones | AX-001 | AX-SEC-001, AX-QA-002 | Security owner reviews assets, adversaries, boundaries, threats, mitigations, and residual risks |
| AX-082 | Approve provenance and license policy v0 | AX-001, ADR-0001, ADR-0018 | AX-LIC-001, AX-LIC-002, AX-IP-001 | Owner and counsel define contribution, source-access, dependency, asset, AI-output, and distribution controls |
| AX-083 | Assign human CODEOWNERS | AX-001 | AX-QA-002 | Every active directory has valid named human owners; sensitive paths have restricted reviewers |
| AX-084 | Configure branch protection policy | AX-001, AX-083 | AX-QA-001 | Main, staging, and develop require reviews, passing checks, and prohibit force pushes and direct writes |
| AX-085 | Implement repository validation CI | AX-001, AX-002 | AX-QA-001, AX-SEC-001 | CI verifies source checksum, required artifacts, ADR count, requirement IDs, secret patterns, and whitespace |
| AX-086 | Define reproducible clean-build environment | AX-002, ADR-0002 | AX-ENG-002, AX-QA-001 | Documented environment builds from scratch with locked tools and no undeclared host state |
| AX-087 | Add security and dependency scanning | AX-008, AX-085 | AX-SEC-001, AX-SEC-002 | CI scans secrets, dependencies, licenses, source, and artifacts and blocks defined severities |
| AX-088 | Import requirements and backlog into tracking | AX-002, AX-083 | AX-QA-001 | All master requirements and 100 tickets retain IDs, owners, dependencies, status, and acceptance fields |
| AX-089 | Open all mandatory ADRs | AX-002 | AX-QA-001 | Twenty-five ADRs exist in Proposed state with owners/reviewers pending rather than guessed choices |
| AX-090 | Establish versioned risk register | AX-002, AX-081 | AX-QA-001, AX-QA-002 | Risks have probability, impact, owner, mitigation, trigger, contingency, and review cadence |
| AX-091 | Publish dependency and critical-path map | AX-003, AX-089 | AX-QA-001 | Architecture map identifies hard dependencies, non-blocking research, and stop gates |
| AX-092 | Define agent and build budget controls | AX-006, AX-038 | AX-AI-006 | Time, token, iteration, network, compute, and output limits are configurable, enforced, and audited |
| AX-093 | Create native hello-world `.axiom` fixture | AX-004, AX-019, AX-024, AX-027 | AX-FMT-001, AX-ENG-001 | Fixture is inspectable, builds from clean checkout, installs, launches, and survives cache deletion |
| AX-094 | Create AXIOM Connect conformance fixtures | AX-033, AX-038 | AX-AI-006 | Valid, denied, expired, over-budget, and replayed capability requests have deterministic results |
| AX-095 | Define Gauntlet evidence schema | AX-002, AX-040, AX-042 | AX-QA-001 | Schema records requirement, decision, diff, actor, tools, tests, security, performance, provenance, uncertainty, and rollback |
| AX-096 | Implement local crash and diagnostic bundle | AX-006, AX-027 | AX-QA-001 | A forced crash produces redacted logs, build identity, stack data, and recovery instructions |
| AX-097 | Add architectural boundary tests | AX-003, AX-085 | AX-ENG-003, AX-SEC-001 | CI detects prohibited cross-domain database access and vendor-type leakage into public APIs |
| AX-098 | Draft local disaster-recovery and rollback drill | AX-005, AX-006, AX-022, AX-027 | AX-QA-001 | Project source, registry, builds, and development signing state recover from a documented simulated loss |
| AX-099 | Publish developer onboarding and clean-room instructions | AX-086, AX-093 | AX-ENG-002 | A new authorized developer completes setup, build, test, launch, and evidence generation without core-team intervention |
| AX-100 | Produce Phase 0 Gauntlet evidence package | AX-081–AX-099 | AX-QA-001, AX-QA-002 | Evidence proves source integrity, ownership status, open decisions, clean build, tests, scans, SBOM, risks, and next-gate readiness |

## Import guidance

When imported into GitHub or CodeSpring, preserve the ticket IDs, requirement links, dependency field, maturity class, owner requirement, and acceptance summary. Expand each acceptance summary into executable checks before marking a ticket in progress. Tickets involving open ADRs should remain blocked or limited to neutral research and prototypes.
