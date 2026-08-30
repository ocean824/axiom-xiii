# AXIOM-XIII Project Memory

**Purpose:** This file records operational truth for maintainers and agents. It does not override the owner directive, verbatim source, accepted ADRs/RFCs, or requirements.

## Current truth

The repository preserves the canonical 202,119-byte specification and its checksum. It now contains a full written domain corpus, 72 build-complete V1 requirements, an acceptance matrix, risk register, implementation roadmap, 160 tickets, 25 original ADRs, security/provenance policies, CodeSpring instructions, and the exact monorepo topology. Most runtime directories remain implementation targets rather than finished systems.

## Governing scope

Every described AXIOM-XIII and PYRAMID destination capability is `V1-BUILD-REQUIRED`. This includes native Chain and Wallet; token/credit and cash-equivalent rails; player-funded and one-to-one Arena competition; escrow, settlement, marketplace, and royalties; large-shard networking; PYRAMID OS/hardware; Kernel, GPU/driver, Secure Transport, Crypto API, Image/Media, AXIOM FS; P2 custom board and P3 custom silicon; NODE mode; and internal model/provenance programs.

Build, assurance, and activation statuses are independent. A blocked production replacement or regional activation does not change the V1 build obligation.

## Current implementation entry point

Begin with AX-001 and proceed through the dependency-ordered [`docs/roadmap/v1-160-tickets.md`](../docs/roadmap/v1-160-tickets.md). The first package establishes source validation, requirements/ADR/evidence tooling, stable IDs/schema conventions, `.axiom` v0, Connect v0, reproducible build, domain contract skeletons, and local simulations for economic, Chain, and Virtual Target boundaries.

## Decisions and ownership

Open ADRs may not be guessed. The repository owner is the initial CODEOWNER, but specialist maintainers and reviewers must be named before critical implementation and production qualification. Financial, consensus, wallet/signing, Arena value, kernel, driver, crypto, transport, production policy, hardware, and release work requires independent human review.

## Agent handoff format

After every accepted change, append a dated entry containing ticket and requirements; branch/commit; files; interfaces/formats/schemas/events/migrations; tests and evidence; performance/security/provenance/economic impact; assurance and activation states; ADRs/risks; failed experiments; unresolved issues; rollback/recovery; and next dependency-valid ticket. Never record secrets or private user data.
