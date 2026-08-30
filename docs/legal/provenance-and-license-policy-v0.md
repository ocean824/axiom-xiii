# Provenance and License Policy v0

**Status:** Initial operational policy derived from the master specification. This document is not legal advice and does not replace agreements prepared by qualified counsel.

## Policy objective

AXIOM-XIII must preserve a clear boundary among creator-owned original content, AXIOM-owned technology, third-party materials, and community or collaborative contributions. Every distributable build must be able to explain where its code and content came from, what rights apply, and whether those rights permit the intended use.

| Category | Default ownership position | Required record |
|---|---|---|
| AXIOM engine, runtime, platform, services, protocols, AI systems, tools, Store, and proprietary technology | AXIOM-owned | Repository path, contributor agreement, license notice, commit provenance |
| Creator game code and original content | Creator-owned, subject to applicable AXIOM platform/runtime terms | Creator identity, project, asset/code hash, declared license and distribution grants |
| Third-party dependency or asset | Owned by its licensor | Source, version, license, notices, permitted uses, restrictions, hash |
| Community or collaborative contribution | As stated by the accepted contribution agreement | Contributor identity, grant, attribution, split terms where applicable |
| AI-generated or AI-assisted output | Ownership and permitted use depend on inputs, provider terms, jurisdiction, and review | Model/provider, prompt/input references where retained, date, output hash, human reviewer, license assessment |

## No implicit open-source grant

This private repository does not grant an open-source license. Access does not authorize copying, redistribution, competing commercialization, model training, sublicensing, trademark use, or disclosure. Any future source-available or commercial license must be approved through ADR-0018 and legal review.

## Provenance record

Every meaningful asset, source module, model output, music file, animation, dataset, package, and generated artifact should have a provenance record.

| Field | Required content |
|---|---|
| Stable ID | Globally namespaced AXIOM identifier |
| Type | Code, asset, model output, music, animation, dataset, package, document, build |
| Creator/source | Person, organization, repository, vendor, model, or import origin |
| Created/imported | Timestamp and importing actor or process |
| Content hash | Cryptographic digest of the recorded artifact |
| Toolchain | Tools and versions used to create or transform the artifact |
| License | License identifier or agreement reference |
| Intended use | Development, runtime, distribution, marketing, training, resale, or other use |
| Restrictions | Attribution, copyleft, noncommercial, geography, derivative, likeness, music, training, or redistribution limits |
| Review status | Unreviewed, reviewed, approved, blocked, or expired |
| Related objects | Project, package, build, digital object, Store item, creator split, or source asset |

## Build license graph

A distributable build must resolve a license graph across code, packages, assets, fonts, music, models, datasets, and generated outputs. The build is blocked when a required right is missing, incompatible, expired, unknown, or inconsistent with the target distribution channel.

| Check | Blocking condition |
|---|---|
| Source license | No license or grant for the intended build/distribution |
| Dependency compatibility | Incompatible obligations across linked or bundled components |
| Attribution and notices | Required notices cannot be produced accurately |
| Asset rights | Missing commercial, derivative, territory, platform, or redistribution rights |
| Music/voice/likeness | Missing consent, synchronization, performance, publicity, or usage rights as applicable |
| AI provider terms | Output use conflicts with model/provider terms or undocumented inputs |
| Unreal import | Content is not legally portable from the source project or engine license |
| Digital object rights | Token or ownership metadata claims rights not granted by the underlying license |

## Originality firewall

References may guide mood, quality, genre, scale, or problem solving, but AXIOM AI and contributors must not reproduce protected characters, art, prose, music, maps, interfaces, code, animations, or distinctive expression. First-party game mechanics must have a Mechanics Registry entry documenting the design goal, inspiration boundary, original terminology, implementation, differentiators, review triggers, and prohibited imitation.

AI output begins as **Proposed**. It does not become canonical game content, platform code, marketing material, or distributable intellectual property until human review confirms technical suitability, originality, provenance, license compatibility, and any required consent.

## Required agreement separation

The master specification calls for separate legal treatment of Creator, Commercial Engine, Source, Runtime Distribution, Store, Arena, Chain/Node, Asset/Plugin, AI, and PYRAMID Device/OS relationships. Repository files may model these agreements and enforcement hooks, but only authorized legal documents govern rights and obligations.

## Contribution controls

Contributors must affirm that they have authority to contribute the material and grant the required rights. Contributions must not contain secrets, unauthorized employer/client code, stolen assets, incompatible third-party content, or personal data without an approved purpose and handling basis.

| Contribution type | Minimum review |
|---|---|
| Documentation or ordinary code | Provenance, license, owner review, tests as applicable |
| New dependency | License, security, maintenance, API, performance, and replacement-boundary review |
| Imported project or asset | Portability and license scan plus explicit unsupported-item report |
| AI-generated material | Input/source review, provider terms, originality assessment, disclosure |
| Cryptography, wallet, chain, anti-cheat, secure boot | Specialist security review and restricted ownership |
| Music, voice, likeness | Rights and consent review before distribution |

## Enforcement boundaries

Technical controls may enforce signed builds, package manifests, entitlement checks, policy decisions, provenance requirements, and Store certification. They must not create hidden backdoors into creator games or private source. Offline behavior, export rights, revocation, and recovery must follow explicit agreements and published policy.

## Open legal work

Counsel must resolve the ownership/entity structure, source-available license, contributor agreements, commercial thresholds, Store and Arena terms, token and wallet disclosures, privacy and minors policies, sanctions and regional restrictions, tax/ledger treatment, hardware terms, and trademark clearance before the corresponding production gates can pass.
