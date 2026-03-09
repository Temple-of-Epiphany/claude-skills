# Wiki Structure Reference

**Version:** 1.0.0
**Date Created:** 2026-03-08
**Author:** Colin Bitterfield

This file documents the full page catalog for the TapMe Contact engineering wiki and provides structure guidance for any similar multi-repo project wiki.

---

## Full Page Catalog (TapMe Contact)

### Architecture Pages

| Page | File | Description |
|------|------|-------------|
| Home | `Home.md` | Central index — quick reference table, architecture overview, security boundary, links to all categories |
| Service Catalog | `Service-Catalog.md` | Every service: purpose, container, ports, networks, what it talks to, dependency matrix, port allocation summary |
| Architecture Wiring | `Architecture-Wiring.md` | Logical service architecture — tiers, Docker networks, security boundary, service communication summary |
| Physical Topology | `Physical-Topology.md` | VPS hosts, WireGuard VPN, Cloudflare routing, service placement per host |
| Network Topology | `Network-Topology.md` | Per-environment network layout (prod, dev, stage) |
| CI/CD Pipeline | `CI-CD-Pipeline.md` | Build, test, security scan, sequential rolling deploy pipeline |
| Scaling Nodes | `Scaling-Nodes.md` | How to add a new VPS node to the cluster |

### Service Guides

One page per service that has deployment complexity, auth configuration, or non-obvious behavior:

| Page | File | Description |
|------|------|-------------|
| Customer API Guide | `Customer-API-Guide.md` | FastAPI deployment, JWT config, rate limiting, 22-endpoint reference |
| Admin API Deployment Guide | `Admin-API-Deployment-Guide.md` | Employee API deployment, config, env vars |
| Admin API Specification | `Admin-API-Specification.md` | Complete 45-endpoint contract with request/response schemas |
| Customer App UI Guide | `Customer-App-UI-Guide.md` | Next.js customer portal — sections, auth flow, deployment |
| Admin Portal Guide | `Admin-Portal-Guide.md` | Employee portal — sections, auth flow, deployment |
| Device Lifecycle and PIN Protection | `Device-Lifecycle-and-PIN-Protection.md` | Device states, PIN model, NFC tap routing |
| Account Model | `Account-Model.md` | Subscription tiers, feature matrix, downgrade behavior |
| Store Architecture | `Store-Architecture.md` | E-commerce architecture — catalog, cart, checkout, Stripe |
| TapMe Site Management | `TapMe-Site-Management.md` | Marketing website content management playbook |

### Security Pages

| Page | File | Description |
|------|------|-------------|
| FusionAuth Integration | `FusionAuth-Integration.md` | OAuth2/OIDC — applications, JWT validation, roles, groups, JWKS |
| FusionAuth Identity Model | `FusionAuth-Identity-Model.md` | Complete identity model — subscription lifecycle, feature matrix, API auth patterns |
| Forward-Auth Architecture | `Forward-Auth-Architecture.md` | Traefik forward auth middleware architecture |
| NIST 800-53r5 Security Controls | `NIST-800-53r5-Security-Controls.md` | Full moderate baseline control mapping with Ansible role references |
| Security Headers and CSP | `Security-Headers-and-CSP.md` | CSP implementation, per-service policies, testing guide |
| Security Known Limitations | `Security-Known-Limitations.md` | ⚠️ Documented accepted risks and remediation plans |
| CSP Nonce Implementation Guide | `CSP-Nonce-Implementation-Guide.md` | Technical guide for removing `unsafe-inline` from CSP |
| Secret Inventory | `Secret-Inventory.md` | All secrets — where they live (GitHub org secrets), what they're for, rotation schedule |

### Reference Pages

| Page | File | Description |
|------|------|-------------|
| User Journeys | `User-Journeys.md` | Sequence diagrams for all key operations |
| Data Flow | `Data-Flow.md` | Schema tables, API contracts, Redis key patterns, cross-service communication |
| Database Schema | `Database-Schema.md` | Every schema, table, column, constraint, index — authoritative reference |
| User Accounts and Groups | `User-Accounts-and-Groups.md` | FusionAuth users, groups, roles — who can do what |
| Pricing Matrix | `Pricing-Matrix.md` | Subscription tier pricing, feature comparisons |
| Pricing Locations | `Pricing-Locations.md` | Where in the codebase pricing values appear (to avoid hunting during price updates) |
| NFC Device Catalog | `NFC-Device-Catalog.md` | All form factors, products, SKUs, image inventory, use case matrix |
| GitHub Labels | `GitHub-Labels.md` | All labels with colors, hex codes, descriptions, SLAs, creation log |
| GitHub Issue Templates | `GitHub-Issue-Templates.md` | Five templates with field reference, decision guide, update procedure |

### Guide Pages

| Page | File | Description |
|------|------|-------------|
| Developer Workstation Setup | `Developer-Workstation-Setup.md` | Configure dev laptop for dev/stage/production work |
| Node Deployment Runbook | `Node-Deployment-Runbook.md` | Step-by-step provisioning of a new VPS node |
| Infrastructure Testing | `Infrastructure-Testing.md` | How to test infrastructure changes before production |
| Ansible Playbook Guide | `Ansible-Playbook-Guide.md` | Which playbooks do what, how to run them |
| Ansible Hardening Specification | `Ansible-Hardening-Specification.md` | NIST control matrix, all roles, recovery procedures |
| Traefik Deployment Guide | `Traefik-Deployment-Guide.md` | Traefik setup, routing, middleware, TLS |
| Grafana Deployment Guide | `Grafana-Deployment-Guide.md` | Grafana + Prometheus + Loki setup, dashboards |
| Promtail Deployment Guide | `Promtail-Deployment-Guide.md` | Log shipping to Loki via Promtail |
| FusionAuth Deployment Guide | `FusionAuth-Deployment-Guide.md` | Fresh FusionAuth installation, Kickstart, configuration |
| FusionAuth Local Development | `FusionAuth-Local-Development.md` | Running FusionAuth locally for development |
| TLS Certificate Management | `TLS-Certificate-Management.md` | Let's Encrypt certs via Certbot + DNS-01 |
| Hostinger DNS-ACME Integration | `Hostinger-DNS-ACME-Integration.md` | DNS-01 challenge via Hostinger API webhook |
| Migration Runbook | `Migration-Runbook.md` | Alembic migration procedures for production |
| HA Runbook | `HA-Runbook.md` | PostgreSQL HA — failover, failback, validation steps |
| HA Chaos Testing | `HA-Chaos-Testing.md` | Chaos test scenarios and expected outcomes |
| HA PostgreSQL Migration Lessons Learned | `HA-PostgreSQL-Migration-Lessons-Learned.md` | Bugs found during HA cutover and their fixes |

---

## Wiki Repository Layout

The wiki is a separate git repo (GitHub's wiki system):

```
{project}-engineering.wiki/
├── Home.md                    # Entry point — always exists
├── _Sidebar.md               # Navigation panel (GitHub renders this automatically)
├── *.md                      # One file per wiki page
```

**File naming rule:** Use `Title-Case-With-Hyphens.md`. The page title in the sidebar uses `[[Title Case With Spaces]]`.

Examples:
- `Architecture-Wiring.md` → `[[Architecture Wiring]]`
- `NIST-800-53r5-Security-Controls.md` → `[[NIST 800-53r5 Security Controls]]`
- `HA-Runbook.md` → `[[HA Runbook]]`

---

## Sidebar Template (Full)

```markdown
**{Project} Engineering**

---

**Architecture**
* [[Home]]
* [[Service Catalog]]
* [[Architecture Wiring]]
* [[Physical Topology]]
* [[Network Topology]]
* [[CI/CD Pipeline]]
* [[Scaling Nodes]]

**Services**
* [[Customer App UI Guide]]
* [[Customer API Guide]]
* [[Admin Portal Guide]]
* [[Admin API Deployment Guide]]
* [[Admin API Specification]]
* [[Device Lifecycle and PIN Protection]]
* [[Account Model]]
* [[Store Architecture]]

**Security**
* [[FusionAuth Integration]]
* [[FusionAuth Identity Model]]
* [[Forward-Auth Architecture]]
* [[NIST 800-53r5 Security Controls]]
* [[Security Headers and CSP]]
* [[Security Known Limitations]]
* [[CSP Nonce Implementation Guide]]
* [[Secret Inventory]]

**Reference**
* [[User Journeys]]
* [[Data Flow]]
* [[Database Schema]]
* [[User Accounts and Groups]]
* [[Pricing Matrix]]
* [[Pricing Locations]]
* [[NFC Device Catalog]]
* [[GitHub Labels]]
* [[GitHub Issue Templates]]

**Guides**
* [[Developer Workstation Setup]]
* [[Node Deployment Runbook]]
* [[Infrastructure Testing]]
* [[Ansible Playbook Guide]]
* [[Ansible Hardening Specification]]
* [[Traefik Deployment Guide]]
* [[Grafana Deployment Guide]]
* [[Promtail Deployment Guide]]
* [[FusionAuth Deployment Guide]]
* [[FusionAuth Local Development]]
* [[TLS Certificate Management]]
* [[Hostinger DNS-ACME Integration]]
* [[TapMe Site Management]]
* [[Migration Runbook]]
* [[HA Runbook]]
* [[HA Chaos Testing]]
* [[HA PostgreSQL Migration Lessons Learned]]

**Links**
* [Engineering Wiki](https://github.com/{org}/{repo}-engineering/wiki)
* [Issues](https://github.com/{org}/{repo}-engineering/issues)
* [All Repositories](https://github.com/orgs/{org}/repositories)
```

---

## Home Page Structure

The `Home.md` must include:

1. **H1 title**: `# {Project} — Engineering Wiki`
2. **Architecture Diagrams table**: links to all diagram pages
3. **Security and Compliance section**: links with descriptions
4. **Quick Reference table**: cloud provider, VPS IPs, VPN, DNS/LB, CI/CD, auth, database, security scanning, monitoring, repo count, hardening baseline
5. **Security Architecture table**: tiers → frontend → API → FusionAuth app → JWT audience → DB role
6. **Data Architecture section**: links to User Journeys and Data Flow
7. **Service Guides section**: links to all service guides
8. **Infrastructure Guides section**: links to all infra guides
9. **Related section**: CLAUDE.md link, GitHub Issues, All Repositories

---

## Service Catalog Page Structure

For each service, include a table:

```markdown
| Attribute | Value |
|---|---|
| **Purpose** | What this service does |
| **Framework** | Language + framework + version |
| **Container** | Docker image |
| **Port** | :NNNN |
| **Deploys To** | Which VPS hosts |
| **Networks** | Docker network names |
| **DB Role** | PostgreSQL role and schema access |
| **JWT Audience** | FusionAuth application UUID |
```

Then a **Talks to** table and a **Does NOT talk to** note (the negative space is important for security reasoning).

Include at the end:
- Port Allocation Summary table (all services × all ports)
- Dependency Matrix (services × dependencies)
- Monitoring Encryption Model (all monitoring data paths with encryption method)
