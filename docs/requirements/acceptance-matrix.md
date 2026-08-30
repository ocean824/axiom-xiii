# V1 Production Acceptance Matrix

**Status:** Derived from sections 76 and 77 of the [master specification](../source/AXIOM-XIII-V1-Master-Specification.md). Evidence links remain pending.

## Product and development

| Domain | Acceptance criteria | Evidence | Status |
|---|---|---|---|
| Shell | Seven-tab navigation is exact; controller-only and keyboard/mouse navigation pass; account privacy, updates, repair, rollback, and accessibility baseline pass | Pending | Not started |
| Native project | `.axiom` create/open/save/migrate work; source is Git-friendly with stable IDs; graph rebuilds from canonical files; cache corruption cannot destroy source; packages lock reproducibly | Pending | Not started |
| Simple/Advanced | Both modes use the same project; switching works mid-task; generated code and graphs are inspectable; manual edits remain understood; Ask is read-only; Plan does not implement; Build respects approvals; rollback works | Pending | Not started |
| AXIOM AI | Provider swap and local/private modes pass; agents are isolated; budgets are enforced; prompt-injection tests pass; no secrets leak; Gauntlet evidence exists; uncertainty is reported; publication and value actions require approval | Pending | Not started |

## Engine and migration

| Domain | Acceptance criteria | Evidence | Status |
|---|---|---|---|
| Engine | A complete small game ships; Windows/Linux clients and Linux server build; rendering, physics, animation, audio, UI, saves, and networking are stable; crash recovery, package security, budgets, and 2D/2.5D plus 3D samples pass | Pending | Not started |
| AAA path | Reference scene meets published target hardware goals; NEXUS, WORLDSTREAM, PHOTON, and OPTICS baselines work; profiles switch correctly; traversal has no unacceptable hitching; visual regression is stable; large creature/character test passes | Pending | Not started |
| Unreal Bridge | Reference corpus converts; provenance scan works; unsupported items are visible; no silent deletion; conversion occurs on an isolated branch with rollback; category-specific report is measured | Pending | Not started |

## Services, economics, and competition

| Domain | Acceptance criteria | Evidence | Status |
|---|---|---|---|
| Services and Store | Identity, social, media, Store, Profile, and Wallet integrate; purchase/install/launch/update/refund/repair pass; submission and payout sandbox works; offline entitlements, moderation, support, and disaster-recovery drill pass | Pending | Not started |
| Chain and Wallet | Independent audits complete; consensus fault tests pass; mint, transfer, license, royalty, marketplace, and prize invariants pass; managed and self-custody recovery pass; signing UX is reviewed; limits and incident controls exist; no sensitive personal data is on-chain | Pending | Not started |
| Arena | Matchmaking metrics are acceptable; tournament lifecycle works through settlement; replay, evidence, and dispute paths work; anti-cheat baseline is present; sponsored prize pool settles; policy engine enforces rules; no known critical integrity defects | Pending | Not started |

## Security and hardware

| Domain | Acceptance criteria | Evidence | Status |
|---|---|---|---|
| Security | Threat models are current; external penetration test, chain/wallet audit, secrets/key review, and supply-chain review complete; incident exercise passes; disclosure/bug-bounty process is ready; critical findings are remediated | Pending | Not started |
| PYRAMID | Virtual Target is usable; Linux-based image boots reference hardware; controller Shell, GAMES, DEV, STORE, and WALLET work; update/recovery and thermal/acoustic tests pass; experimental kernel milestone is documented without being a production dependency | Pending | Not started |

## Launch gates

| Gate | Condition | Evidence | Status |
|---|---|---|---|
| A — Architecture | No critical domain lacks an owner, interface, threat model, tests, or migration policy | Pending | Not started |
| B — Product | New users can play and build without core-team intervention | Pending | Not started |
| C — Developer | External developers can complete, package, publish, update, and support a game | Pending | Not started |
| D — Security | No unresolved critical finding; key, wallet, chain, Store, and agent boundaries reviewed | Pending | Not started |
| E — Economic | Funds, assets, royalties, refunds, prizes, and records reconcile under failure and dispute | Pending | Not started |
| F — Operations | Monitoring, support, moderation, incident response, backups, and rollback are staffed and tested | Pending | Not started |
| G — Legal/Policy | Terms, licenses, Store and Arena rules, token disclosures, privacy, and operator policies are approved for launch regions | Pending | Not started |
| H — Performance | Reference projects meet frame, memory, loading, network, chain, service, and editor targets | Pending | Not started |
| I — Hardware readiness | Required only for a physical PYRAMID launch, not desktop V1 | Pending | Not applicable to desktop V1 |

## Evidence policy

A criterion is not complete until its evidence is reproducible, versioned, attributable to a build, and approved by the named owner. Narrative claims, demonstrations without artifacts, and passing averages without workload definitions do not satisfy the gate.
