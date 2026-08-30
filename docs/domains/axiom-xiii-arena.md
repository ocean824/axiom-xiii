# AXIOM Arena Domain Specification

## 1. Purpose and Non-Negotiable Doctrine

AXIOM Arena serves as the central competitive infrastructure for the entire AXIOM-XIII ecosystem, providing a unified system for skill-based matchmaking, ranked play, tournaments, prize pools, teams, spectating, replays, integrity verification, and financial settlement. The primary purpose of this domain is to deliver a comprehensive, secure, and provably fair competitive environment that integrates seamlessly with other core platform components, most notably the AXIOM Chain, Wallet, and Store. By centralizing these capabilities, AXIOM Arena ensures that individual game developers do not need to reinvent complex matchmaking algorithms, anti-cheat mechanisms, or secure financial escrow systems, allowing them to focus entirely on gameplay while relying on the platform for competitive integrity and economic operations.

The Owner Directive issued on August 30, 2026, establishes a strict non-negotiable doctrine regarding the implementation scope of AXIOM Arena. Every capability described in the master specification—including real-value competition, paid entry mechanics, player-funded prize pools, wagering-compatible contest infrastructure, cryptographic escrow, irreversible settlement, cash-equivalent value flows, result attestation, and comprehensive anti-cheat systems—must be represented as mandatory V1 implementation scope. No feature may be deferred, reduced to a documentation placeholder, or postponed to a later release cycle based on perceived maturity, legal complexity, or economic risk.

The organization must clearly distinguish between the construction of these capabilities and their public activation. The engineering mandate requires building the complete code, schemas, interfaces, service boundaries, deterministic simulations, sandbox flows, operational controls, and end-to-end integration tests required for the full V1 destination. While jurisdictional laws, compliance requirements, or economic gates may ultimately restrict the activation of certain features in specific regions or for specific users, these external constraints cannot be used as justification to remove the capabilities from the V1 engineering scope. The legal characterization of specific contests or value flows must be dynamically encoded into a robust policy engine and operator deployment profile, ensuring the platform remains fully capable even if specific features are disabled by policy in certain contexts.

## 2. Personas and Actors

The AXIOM Arena domain serves a diverse set of actors, each with distinct responsibilities, permissions, and interaction patterns within the competitive ecosystem. Understanding these personas is critical for designing appropriate interfaces and security boundaries.

The Player or Competitor represents the primary end-user participating in matchmaking, ranked play, and structured tournaments. These individuals engage directly with the competitive systems, build their skill ratings over time, and, where legally permitted and enabled by the policy engine, may fund prize pools and stake real value on their performance. Their experience must be frictionless, transparent regarding rules and stakes, and protected by rigorous integrity measures.

The Team or Roster Manager is responsible for organizing groups of players, managing team registrations for competitive play, handling roster substitutions, and coordinating schedules. This persona requires administrative tools to manage team identity, distribute winnings among members, and ensure all roster members meet the eligibility requirements for specific events.

Tournament Organizers encompass a wide range of entities, including individual creators, game publishers, and third-party sponsors. They utilize the Arena infrastructure to set up tournaments, define specific rulesets, configure bracket structures, and provide or manage prize pools. They require comprehensive dashboards for event management, participant communication, and dispute oversight.

Sponsors are entities that contribute financial value or digital objects to prize pools without necessarily taking on the operational burden of organizing the tournament itself. This group may include the AXIOM organization, game publishers incentivizing play, or external advertisers. They require verifiable proof of execution and transparent reporting on how their contributed funds were distributed.

Moderators and Adjudicators are human operators tasked with reviewing disputes, handling appeals, and enforcing material sanctions against users who violate competitive integrity. They interact primarily with the dispute resolution module, requiring access to comprehensive evidence, including server logs, deterministic replays, and behavioral analytics, to make informed decisions.

SENTINEL represents the platform's automated AI adversary and integrity monitor. It continuously generates cheat and fraud hypotheses, analyzes player behavior, flags anomalies, and provides automated enforcement recommendations. SENTINEL operates constantly in the background, feeding data to the dispute module and escalating complex cases to human adjudicators.

The Policy Engine is an automated, systemic actor that evaluates user eligibility, jurisdictional constraints, age restrictions, and risk levels in real-time before granting access to specific Arena features, particularly those involving real value or wagering mechanics.

## 3. Domain Boundaries and Interfaces

AXIOM Arena does not operate in isolation; it requires deep, synchronous, and asynchronous integration with multiple other AXIOM domains to deliver its full feature set. Defining these boundaries clearly is essential for maintaining a modular, testable architecture.

The most critical integration exists between AXIOM Arena and the AXIOM Chain and Wallet domains. This boundary handles all financial and economic operations related to competition. The Arena must interface with the Chain to lock entry fees into smart contract escrows, aggregate prize pool funding, attest to finalized match results, and trigger irreversible settlement and token or credit distribution. This interface must be highly resilient, handling potential chain delays or transaction failures gracefully without corrupting the tournament state.

AXIOM Arena relies heavily on the AXIOM Protocol, which defines the shared semantic objects and events used across the entire ecosystem. By utilizing these standardized definitions, the Arena ensures that match results, player identities, and digital objects are understood consistently by the game engine, the store, and the chain, preventing data silos and integration mismatches.

Integration with the AXIOM Store and Marketplace is necessary for handling the purchase of tournament tickets, the distribution of sponsored digital items as prizes, and the calculation and routing of royalty and fee distributions resulting from competitive events. The Arena must query the Store to verify ownership of required entry passes and instruct the Store to mint or transfer reward items upon tournament completion.

The boundary between the Arena and individual Game Engines or Runtimes is managed through standardized Game Adapters. These adapters define the specific modes, result schemas, anti-cheat requirements, and spectator policies for each integrated title. The Arena treats the game server as a trusted reporter of events, provided the server meets the required integrity and signing standards, while the game relies on the Arena for matchmaking, rating calculations, and prize distribution.

Finally, the Arena interacts continuously with the Identity and Profile domain to access shared user identities, update skill ratings, append match history, retrieve trust and integrity scores, and manage team affiliations. This ensures a player's competitive reputation is persistent and visible across the entire platform.

## 4. Named Components and Internal Modules

The AXIOM Arena domain is composed of several distinct, highly cohesive internal modules, each responsible for a specific aspect of the competitive lifecycle.

The Matchmaking and Rating Engine is the core component responsible for pairing players and calculating skill adjustments. The Matchmaker optimizes match quality by balancing a complex, configurable objective function that considers skill proximity, network latency, acceptable wait times, party size constraints, input device pools, regional eligibility, trust scores, and game version compatibility. The Rating Service supports various game-specific rating models, handling placement matches, uncertainty deviation, seasonal decay, smurf detection, and party skill adjustments, while maintaining a unified identity for the player across the platform.

The Tournament and League Manager handles the structured organization of competitive events. The Bracket Engine supports multiple formats, including single-elimination, double-elimination, round-robin, and Swiss systems, automatically advancing winners and scheduling subsequent rounds. The Roster System manages the lifecycle of teams, handling creation, invitations, eligibility verification, and mid-season substitutions. The Event Scheduler coordinates the complex timelines of qualifiers, main championships, and asynchronous challenges, ensuring matches occur within designated windows.

The Prize and Escrow Infrastructure manages all value associated with competition. The Funding Module aggregates prize pools from diverse sources, including AXIOM sponsorships, publisher contributions, advertiser funds, creator allocations, and direct player stakes. The Escrow Controller interfaces with the AXIOM Chain to securely lock these funds before a tournament is permitted to begin, ensuring solvency. The Settlement Engine is responsible for distributing the prizes based on the attested final results, automatically calculating and deducting necessary platform fees, taxes, and creator royalties before executing the final payouts.

The Wagering-Compatible Infrastructure provides the specialized mechanisms required for real-value competition. The Stake Manager handles the commitment of one-to-one and tournament stakes, ensuring players have sufficient funds and meet all policy requirements. The Odds-Free Contest State module strictly enforces that all competitions are skill-based, preventing the introduction of odds generation or chance-based mechanics that would alter the legal classification of the event. The Ledger Evidence system maintains an immutable, cryptographic record of all transactions, state changes, and attestations to support audits and regulatory compliance.

The Integrity and Anti-Cheat System is paramount for maintaining trust in the platform. The Evidence Collector gathers server-authoritative logs, deterministic verification data, and comprehensive replay files for every competitive match. This data is fed into the SENTINEL Integration module, which applies behavioral analytics and network anomaly detection to identify potential cheating. The Dispute and Appeal Module provides the workflow for users to challenge results and for moderators to review evidence, manage user appeals, and execute human escalation processes for material sanctions.

The Policy Engine Adapter acts as the gatekeeper for all restricted activities. The Eligibility Evaluator checks a user's geographical location, age, KYC/KYB verification status, active sanctions, and local jurisdictional rules before allowing them to participate in real-value events or fund prize pools, ensuring the platform remains compliant with complex global regulations.

## 5. Canonical Entities and Stable IDs

To ensure consistency and traceability across the distributed architecture, AXIOM Arena defines several canonical entities, each uniquely identified by a stable, universally unique identifier (UUID) with a specific prefix.

The `ArenaMatch` entity represents a single instance of competitive play, whether it is a ranked ladder game, an unranked casual bout, or a custom private lobby. It is identified by the `match_<uuid>` format and contains references to the participating players, the game mode, and the final outcome.

The `Tournament` entity encapsulates a structured competitive event, complete with defined rulesets, bracket structures, and schedules. Identified by `tourn_<uuid>`, it serves as the parent entity for all matches played within its context and links to the associated prize pool.

The `TeamRoster` entity defines a registered group of players organized for a specific event or competitive season. It uses the `roster_<uuid>` format and tracks the active members, substitutes, and the manager responsible for administrative actions.

The `PrizePool` entity represents the aggregated financial value or digital objects available for a specific tournament. Identified by `pool_<uuid>`, it tracks the sources of the funds, the current escrow status on the AXIOM Chain, and the distribution rules for the winners.

The `MatchResult` entity records the attested outcome of a completed match, including detailed scores, statistics, and cryptographic links to the underlying evidence and replay files. It uses the `result_<uuid>` format and is the primary trigger for rating adjustments and tournament advancement.

The `DisputeCase` entity represents a formal challenge to a match result or an appeal against an anti-cheat action. Identified by `dispute_<uuid>`, it aggregates all relevant evidence, participant statements, and the audit trail of moderator actions until a final resolution is reached.

The `RatingProfile` entity stores a player's calculated skill rating, historical performance data, and uncertainty metrics for a specific game and mode. It uses the `rating_<uuid>` format and is continuously updated by the Rating Service after each finalized match.

## 6. State Machines and Transitions

The complexity of tournament management and result verification requires robust, well-defined state machines to ensure data integrity and prevent race conditions or unauthorized actions.

The Tournament State Machine governs the lifecycle of an event. It begins in the `DRAFT` state, where the organizer configures the rules, bracket formats, and prize sources without public visibility. Once published, it moves to `REGISTRATION`, allowing eligible players and teams to join and commit any required stakes. When registration closes, it transitions to `FUNDING_LOCKED`, a critical state where the Escrow Controller verifies that all committed funds are securely locked on the AXIOM Chain; no further entries or stake modifications are permitted in this state. The tournament then enters `IN_PROGRESS`, during which matches are generated, played, and results are continuously reported. Upon completion of all matches, it shifts to `ATTESTATION`, a holding state where all results undergo final verification, anti-cheat analysis, and dispute resolution. Once all challenges are cleared, it reaches the `SETTLED` state, triggering the Settlement Engine to distribute prizes via the Chain, and the event is permanently archived. If an event cannot proceed due to technical failures or insufficient participation, it may transition to `CANCELLED`, automatically refunding all locked stakes to their original sources.

The MatchResult State Machine manages the lifecycle of individual game outcomes. It starts in the `PENDING` state when a match is initiated or is awaiting the final report from the game server. Upon receipt of the outcome, it moves to `REPORTED`. The system then performs deterministic verification and anti-cheat checks; if successful, it transitions to `VERIFIED`. If a participant challenges the outcome or SENTINEL flags an anomaly, it enters the `DISPUTED` state, halting any dependent processes (like bracket advancement or settlement) until a manual or AI review is completed. Once the review is concluded or the verification period expires without challenge, it reaches the `FINALIZED` state. This state is immutable and serves as the definitive trigger for rating adjustments and prize settlements.

## 7. API and Capability Contracts

The AXIOM Arena exposes strictly defined API contracts to interact with game runtimes, external services, and internal platform components, ensuring secure and predictable communication.

The Game Adapter Interface dictates how individual game engines communicate with the Arena. The `RegisterMode(ModeConfig)` endpoint allows a game to define its supported team sizes, specific rating models, and disconnect handling rules. The `SubmitResult(MatchID, ResultSchema, EvidenceURI)` endpoint is used by the trusted game server to report the final outcome of a match, including the required cryptographic links to replay data and deterministic logs. The `RequestMatch(PlayerIDs, MatchmakingParams)` endpoint allows the game client or server to initiate the matchmaking process based on defined parameters.

The Settlement Interface manages the critical financial interactions between the Arena and the AXIOM Chain/Wallet domains. The `LockEscrow(PoolID, FundingSources)` command instructs the Chain to secure the specified funds before a tournament can begin, returning a cryptographic proof of lock. The `DistributePrizes(PoolID, FinalizedResults)` command triggers the irreversible payout of the escrowed funds based on the attested match results. The `RefundStakes(PoolID, Reason)` command is used to return funds to participants if a tournament is cancelled or a match is annulled.

The Policy Interface connects the Arena to the global Policy Engine. The `EvaluateEligibility(PlayerID, EventID, StakeAmount)` query is called before any restricted action is taken. It evaluates the user's jurisdictional constraints, age, and KYC status, returning a definitive `ALLOW`, `DENY`, or `REQUIRE_KYC` response, ensuring the platform remains legally compliant at all times.

## 8. Command, Query, and Event Flows

The interactions within the AXIOM Arena follow a strict Command Query Responsibility Segregation (CQRS) and event-driven architecture to ensure scalability and auditability. A representative flow is the process of a player entering a player-funded tournament.

The flow begins with a Command: the player initiates `JoinTournament(TournID, Stake)` through the client interface. The Arena immediately issues a Query to the Policy Engine: `EvaluateEligibility`, checking if the player's jurisdiction permits real-value staking and if their age and identity verification meet the requirements. If approved, the Arena issues a second Query to the Wallet Service to confirm the player has sufficient balance to cover the required stake. Upon confirmation, the Arena issues a Command to the Chain/Wallet domain: `LockEscrow`, requesting the funds be moved to a secure holding state. The Chain processes this transaction and emits an Event: `StakeLocked(PlayerID, TournID)`. The Arena listens for this event, updates the internal tournament roster state, and finally emits its own Event: `PlayerRegistered(PlayerID)`, which updates the user interface and notifies the tournament organizer. This asynchronous, event-driven approach ensures that the Arena state remains perfectly synchronized with the immutable Chain state.

## 9. Data Ownership and Storage

Data within the AXIOM Arena domain is distributed across specialized storage systems optimized for specific access patterns and durability requirements.

The primary Arena Database, utilizing a distributed SQL system like PostgreSQL or CockroachDB, owns and stores the relational data. This includes match histories, player skill ratings, complex tournament bracket structures, and team rosters. This database requires high availability and strong consistency for transactional operations.

The AXIOM Chain serves as the ultimate source of truth for all financial transactions, escrow states, and final result attestations. It owns the immutable record of who paid what, where the funds are held, and the cryptographic proof of the final match outcomes that triggered the settlements.

Blob Storage, implemented via S3-compatible systems or decentralized networks like IPFS, is utilized for storing large, immutable files. This includes the deterministic simulation logs, comprehensive replay files, and evidence packages required for anti-cheat analysis and dispute resolution. These files are content-addressed, ensuring they cannot be tampered with after creation.

A high-performance Cache, such as Redis, is employed to handle ephemeral, high-throughput data. This includes the real-time matchmaking queues, active player session states, and temporary locks required during the matchmaking process, ensuring the system can handle massive concurrent loads without degrading performance.

## 10. Dependency Graph

Understanding the dependency graph is crucial for deployment sequencing and failure mitigation. The AXIOM Arena sits centrally within the platform architecture.

Its Upstream Dependencies include the Identity Service (for user authentication and profile data), the Policy Engine (for eligibility and compliance checks), the Wallet Service and AXIOM Chain (for financial operations and escrow), and the individual Game Servers (for executing the matches and reporting results). The Arena cannot function fully without these services being operational.

Its Downstream Dependencies include the Social Feed (which consumes Arena events to broadcast match results and tournament victories), the Profile Service (which queries the Arena to display current ranks and competitive history), and the Store (which relies on the Arena to validate tournament ticket purchases and distribute digital object prizes). These services rely on the Arena but do not block its core functionality if they experience degradation.

## 11. Failure and Degraded Modes

The AXIOM Arena must be designed for resilience, gracefully degrading its functionality when dependent systems fail, rather than experiencing catastrophic outages.

In the event of a Chain Outage, core matchmaking and casual unranked play must continue uninterrupted. However, registration for real-value tournaments and the final settlement of prizes must be temporarily paused. Match results are queued securely in the Arena Database and are submitted for attestation and settlement only when the Chain connection is restored.

If the Policy Engine becomes unreachable, the system must fail-closed for all restricted operations. No new real-value matches, wagering-compatible contests, or sponsored tournaments can begin, as eligibility cannot be verified. However, casual, unranked play that does not involve financial value or strict jurisdictional constraints may proceed normally.

Degradation of the Anti-Cheat or SENTINEL systems requires a shift in operational posture. High-stakes matches may be delayed or explicitly require manual review before results are finalized. Lower-stakes matches may proceed, but users are presented with warnings regarding the degraded integrity state, and all replay data is heavily archived for retroactive analysis once the systems are restored.

During periods of Matchmaker Overload, the system must automatically adapt to maintain throughput. This may involve gradually expanding the acceptable search parameters (such as allowing higher latency or greater skill deviation) to form matches more quickly, or implementing explicit queuing and backpressure mechanisms to prevent the database from being overwhelmed.

## 12. Security, Privacy, Provenance, and Legal Considerations

Operating a competitive platform involving real value necessitates stringent security, privacy, and legal frameworks, deeply integrated into the architecture.

The inherent Legal Uncertainty surrounding skill-based wagering and real-value competition across different global jurisdictions is managed explicitly by the Policy Engine. The engineering mandate dictates that the features are built completely, but they are dynamically disabled or restricted on a per-jurisdiction basis by the policy rules. This ensures the platform is capable everywhere but compliant locally.

Regarding Anti-Cheat Privacy, the V1 implementation strongly prefers server-side behavior analytics and deterministic verification over invasive client-side monitoring. If a kernel-level anti-cheat component is utilized for high-stakes modes, it requires explicit, unambiguous disclosure to the user and independent third-party security reviews before deployment.

Provenance is a critical requirement. All real-value match results, prize pool aggregations, and final settlements must be cryptographically attested on the AXIOM Chain. This provides an immutable, verifiable audit trail that proves the platform operated fairly and distributed funds exactly according to the established rules and the verified outcomes.

Robust Fraud Controls are mandatory. The system must include automated detection mechanisms for collusion rings, smurfing (high-skill players using low-skill accounts), and payment fraud (such as chargebacks on tournament entry fees). All automated sanctions that materially affect a user's account or funds must include a clear human escalation and appeal path.

## 13. Observability

Comprehensive observability is required to monitor the health, fairness, and performance of the competitive ecosystem.

Key Metrics must be tracked continuously, including average matchmaking wait times across different modes and regions, the average skill deviation per formed match (indicating match quality), the rate of disputed results versus accepted results, the latency of the settlement process, and the frequency of anti-cheat flags generated by SENTINEL.

End-to-End Tracing must be implemented across all critical flows. A single trace ID must follow a request from the initial `RequestMatch` call, through the game server execution, the `SubmitResult` reporting, the deterministic verification, and finally to the `DistributePrizes` execution on the Chain, allowing engineers to pinpoint bottlenecks or failures in complex asynchronous processes.

Alerts must be configured for anomalous behavior that could indicate systemic failure or exploitation. This includes alerts for unusually large or frequent prize distributions, sudden spikes in dispute volumes, repeated failures to lock escrow funds, or significant, unexpected drops in matchmaking throughput.

## 14. Performance and Resource Budgets

The AXIOM Arena must meet strict performance criteria to ensure a responsive and scalable competitive experience.

Matchmaking Latency is critical; the engine must evaluate and update the matchmaking pool in less than 50 milliseconds per evaluation tick. For adequately populated game modes and regions, the P99 wait time for a player to find a match must remain under 2 minutes.

Result Processing must be efficient. The initial cryptographic and schema verification of a submitted result must complete in less than 2 seconds. If deep deterministic replay analysis is required for high-stakes matches, it must complete within 5 minutes of match conclusion to avoid frustrating delays in tournament advancement.

The overall Throughput of the system must be architected to support 100,000 concurrent matchmaking requests and manage the state of 10,000 simultaneous tournament brackets globally without performance degradation.

## 15. Test Pyramid and Acceptance Tests

A rigorous testing strategy is required to validate the complex logic and financial interactions within the Arena.

Unit Tests must comprehensively cover the core algorithmic components, including the bracket generation logic for various tournament formats, the mathematical correctness of the rating decay and adjustment calculations, and the boolean logic of the eligibility rules.

Integration Tests must validate the critical boundaries between domains. This includes testing the escrow locking and unlocking flows between the Arena and the Chain, and verifying that the Arena correctly interprets the ALLOW/DENY responses from the Policy Engine under various mock scenarios.

End-to-End Tests must be executed in the Sandbox environment. These tests simulate the full lifecycle of a tournament using mock players, deterministic game simulations that produce predictable outcomes, and verified prize settlement on the testnet chain, ensuring all components work together seamlessly.

The primary Acceptance Test for V1 readiness is defined as follows: "A 64-team player-funded tournament is created, funded, and executed. The system successfully handles at least 2 simulated player disconnects and 1 explicitly disputed match result. The tournament concludes, and the prize pool is settled correctly and irreversibly on the testnet chain, distributing funds to the winning teams and routing the correct fees to the platform and organizer."

## 16. V1 Definition of Done

The AXIOM Arena domain will be considered V1-Complete only when the following criteria are met:

First, the code, database schemas, and service boundaries for all specified capabilities—explicitly including the real-value and wagering-compatible infrastructure—are fully implemented, reviewed, and merged into the main branch.

Second, the end-to-end integration with the AXIOM Chain, Wallet, and Policy Engine is fully operational and verified within the Sandbox and Testnet environments.

Third, the automated test suite comprehensively covers all happy paths, edge cases, dispute resolution workflows, and the specified degraded failure modes, passing reliably in the CI/CD pipeline.

Fourth, the anti-cheat and integrity systems, including evidence collection and deterministic verification, are operational and successfully integrated with the SENTINEL AI adversary.

Finally, all open Architecture Decision Records (ADRs) related to the Arena domain have been formally resolved and documented.

## 17. Work Packages in Dependency Order

The implementation of the AXIOM Arena must proceed in a strict dependency-ordered sequence to manage risk and ensure foundational components are stable before building complex features upon them.

1. **Arena Core:** Implement the foundational Matchmaking engine, the Rating service, and the Game Adapter API. This allows basic, unranked play to function.
2. **Policy Integration:** Develop the Policy Engine adapter and implement the core eligibility rules. This establishes the necessary legal and compliance boundaries early in the development cycle.
3. **Tournament Engine:** Build the Bracket generation logic, the Roster management system, and the Event scheduling infrastructure. This enables structured, non-value competition.
4. **Value Flows:** Implement the Escrow controller, stake management, and the Settlement Engine, integrating deeply with the Chain and Wallet. This unlocks real-value competition.
5. **Integrity Systems:** Develop the Replay ingestion pipeline, the deterministic verification logic, and the integration with SENTINEL for automated anti-cheat analysis.
6. **Dispute & Operations:** Build the Adjudication UI, the user appeal workflows, and the comprehensive observability dashboards required for live operations.

## 18. Open ADRs (Architecture Decision Records)

Several critical architectural decisions remain open and must be resolved by the engineering team during the implementation phase.

- **ADR-ARN-001: Standardized Deterministic Verification Format.** The team must decide on a unified format for deterministic logs that can be generated by various game engines (including the native AXIOM engine and Unreal via the Bridge) and efficiently verified by the Arena servers.
- **ADR-ARN-002: Long-Term Replay Retention Strategy.** A decision is required regarding the storage of massive replay files. The team must evaluate the cost and retrieval latency of centralized cold storage (like Amazon S3 Glacier) versus decentralized, content-addressed networks (like IPFS or Filecoin) for long-term evidence retention.
- **ADR-ARN-003: Handling Chain Gas Fees for Micro-Tournaments.** The team must determine the economic model for covering the blockchain transaction fees (gas) associated with high-frequency, low-stakes micro-tournaments. Options include subsidizing fees via the platform treasury, batching settlements to reduce costs, or requiring players to cover the fees directly.

---
*Document Status: V1-BUILD-REQUIRED implementation specification.*
