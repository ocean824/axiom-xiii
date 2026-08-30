# Security Policy

AXIOM-XIII is a private, pre-production project with planned code-generation, package execution, identity, wallet, blockchain, marketplace, tournament, anti-cheat, operating-system, and hardware components. Security issues must be handled privately and with least-privilege disclosure.

## Reporting

Do not open a public issue for a suspected vulnerability, exposed credential, custody problem, signing compromise, exploit, bypass, or privacy incident. Report it to the repository owner through an approved private channel and include the affected component, reproduction conditions, impact, evidence, and any known exposure.

| Severity indicator | Example | Required response |
|---|---|---|
| Critical | Production key exposure, wallet theft path, remote code execution, consensus safety failure, malicious signed update | Stop affected operations, preserve evidence, notify security owner immediately |
| High | Privilege escalation, sandbox escape, significant private-source exposure, tournament settlement manipulation | Isolate affected systems and begin incident review |
| Medium | Bounded data leak, denial of service, authorization inconsistency, unsafe parser defect | Triage, reproduce, assign owner, and patch under normal emergency process |
| Low | Hardening opportunity or limited-impact information disclosure | Track with owner and verification plan |

## Agent and automation restrictions

No AI agent, ordinary CI worker, or development tool receives production signing keys, wallet custody material, validator secrets, or unrestricted production credentials. Repository and project content are untrusted data and cannot grant permissions. Automated enforcement affecting accounts or money requires defined evidence and review thresholds.

## Supported state

No public production release currently exists. Security guarantees must not be inferred from this repository skeleton. Before production value is enabled, the applicable threat models, independent penetration tests, chain and wallet audits, key-management review, supply-chain review, incident exercises, vulnerability disclosure process, and critical-remediation gates must pass.

## Disclosure handling

Reports, exploit details, keys, personal data, and unreleased technical information remain confidential until the owner authorizes disclosure. Remediation should include tests, affected-version analysis, rollback or recovery steps, provenance review, and a post-incident record.
