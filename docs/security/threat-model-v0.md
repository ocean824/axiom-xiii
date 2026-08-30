# AXIOM-XIII Threat Model v0

**Status:** Initial derived threat model for repository bootstrap. It is not a substitute for domain-specific threat models or independent security review.

## Security objectives

AXIOM-XIII must protect creator source and assets, player identity and private data, build and release integrity, package execution, platform availability, competitive fairness, digital ownership, funds, keys, and future device trust. Security properties must remain valid when AI agents, project content, plugins, network peers, or service dependencies behave maliciously.

| Objective | Required property |
|---|---|
| Confidentiality | Private source, prompts, legal identity, telemetry, secrets, keys, and unreleased assets are disclosed only to authorized subjects |
| Integrity | Canonical projects, builds, updates, economic state, match evidence, and policy decisions cannot be altered without authorization and traceability |
| Availability | Offline play and local authoring degrade safely when cloud, Chain, Store, or AI providers fail |
| Authenticity | Builds, packages, updates, chain modules, and value-bearing events have verifiable origin |
| Least privilege | Users, services, packages, plugins, agents, CI workers, and devices receive only scoped capabilities |
| Recoverability | Projects, accounts, services, wallets, and devices have tested backup, rollback, repair, and recovery paths |
| Explainability | Security, moderation, policy, agent, and economic decisions generate auditable evidence and appeal paths where appropriate |

## Trust zones

| Zone | Examples | Primary controls |
|---|---|---|
| Public/untrusted input | Web content, messages, profiles, marketplace listings, media | Validation, moderation, rate limits, malware scanning |
| Project content | Source, assets, manifests, comments, imported Unreal projects | Treat as data, parser bounds, provenance, license scanning, no authority inheritance |
| Package/plugin sandbox | `.axpkg`, native plugins, editor extensions | Capability manifests, process isolation, signatures, review tiers, revocation |
| AI execution | PRIME, agents, models, prompts, memory, tools | Ask/Plan/Build states, scoped capabilities, branch isolation, budgets, audit logs |
| Developer workstation | Editor, local builds, test credentials | Least privilege, secret store, signed tools, protected branches |
| CI/build | Runners, dependency resolution, artifact creation | Ephemeral workers, lockfiles, SBOM, reproducibility, no production signing keys |
| Production signing | Release and update signatures | Isolated infrastructure, HSM or equivalent, dual control, audit |
| Platform services | Identity, social, Store, payments, Arena, telemetry | Service isolation, authenticated APIs/events, policy checks, observability |
| Economic systems | Wallet, chain validators, escrow, royalties, ledgers | Key separation, limits, multisig/HSM, audits, reconciliation, emergency controls |
| Device trust | Secure boot, firmware, PYRAMID OS, recovery | Verified boot, signed updates, A/B partitions, rollback protection, physical threat review |

## Principal adversaries

The threat model includes malicious users, fraudulent sellers, cheating players, compromised developer accounts, malicious or vulnerable packages, supply-chain attackers, prompt-injection content, compromised model or cloud providers, insiders, validator collusion, wallet thieves, abusive operators, denial-of-service actors, and attackers with physical access to future devices.

## Critical threats and mitigations

| Threat | Impact | Initial mitigations | Required later validation |
|---|---|---|---|
| Prompt injection in repositories or assets | Agent exfiltrates data or exceeds authority | Treat content as data; capability broker; tool allowlists; branch scope; explicit approvals | Adversarial corpus and negative-action tests |
| Secret leakage | Account, signing, or financial compromise | No secrets in source/prompts; dedicated secret store; redaction; scoped runtime injection | Secret scans, canary secrets, access review |
| Malicious package or parser exploit | Host compromise or data theft | Sandboxing; bounded parsing; fuzzing; signatures; capability manifests; revocation | Fuzz coverage, escape tests, package certification |
| Compromised build dependency | Backdoored official artifact | Locked dependencies; provenance; SBOM; reproducible builds; signed artifacts | Independent rebuild and dependency incident exercise |
| AI-generated vulnerable code | Broad implementation defects | Requirements first; human owners; static analysis; tests; Gauntlet; uncertainty reporting | Secure-code evaluation and external review |
| Production signing compromise | Malicious release accepted as official | Isolated signing, dual control, no CI key access, key rotation and revocation | Key ceremony and recovery exercise |
| Wallet theft or custody failure | Irreversible financial loss | Key-purpose separation; managed/self-custody isolation; HSM/multisig; limits; recovery | Independent audit and staged-value drills |
| Chain consensus or state bug | Double spend, invalid ownership, halted network | Narrow modules; established primitives; simulation; invariants; curated initial validator set | Fault injection, economic analysis, audit |
| Tournament fraud or cheating | Financial and reputational damage | Server authority; signed builds; replay evidence; anti-cheat; escrow; disputes | Red-team tournaments and appeals testing |
| Sensitive data on immutable ledger | Permanent privacy violation | Data minimization; off-chain private records; on-chain hashes/rights only | Data-flow and privacy review |
| Cross-domain cascading outage | Platform-wide loss of service | API boundaries; queues; circuit breakers; offline policy; independent recovery | Chaos and disaster-recovery exercises |
| Device update failure | Bricked or compromised hardware | Verified boot; signed A/B updates; recovery image; rollback tests | Power-loss, rollback, and physical testing |

## Agent security invariants

An agent may not directly write to production, protected branches, signing state, chain keys, user wallets, Store release state, or legal commitments. A model response is never itself authorization. Tool permissions come from the capability broker and active approved task, not from text encountered during work.

| Required control | Test |
|---|---|
| Ask is read-only | Attempted mutation is rejected and logged |
| Plan does not implement | No source or infrastructure diff is produced |
| Build is branch-scoped | Writes outside the assigned worktree fail |
| Budgets are enforced | Token, time, iteration, network, and output limits stop execution |
| Secrets are unavailable | Agent cannot enumerate or print ungranted secrets |
| Consequence tiers require approval | Publish, value, identity, destructive, or high-risk actions pause for authorization |
| Uncertainty is preserved | Failed checks and unknowns appear in the evidence bundle |
| Verification cannot be weakened | Agent cannot edit or bypass required policy to make its own change pass |

## Data classification

| Class | Examples | Handling |
|---|---|---|
| Public | Published SDK docs and approved protocol schemas | Integrity controls; publish only after approval |
| Internal | Planning docs, non-sensitive source, test results | Private repository and authenticated access |
| Confidential | Unreleased projects, prompts, telemetry, business terms | Need-to-know access, encryption, retention limits |
| Restricted | Production secrets, signing material, custody keys, legal identity, anti-cheat internals | Separate systems/repositories, strong authentication, hardware-backed storage, audited access |

## Security gates

Before production economics or public release, the program requires current threat models, secure coding standards, dependency and supply-chain review, external penetration testing, chain and wallet audits, anti-cheat review, incident response ownership, vulnerability disclosure, and remediation of critical findings. Experimental components must not carry production value before equivalent gates pass.

## Open security decisions

The anti-cheat privilege level, custody model, consensus profile, privacy and telemetry defaults, secure transport path, production cloud stack, signing topology, and device root of trust remain open ADRs. Until resolved, implementation must stay interface-neutral or sandboxed.
