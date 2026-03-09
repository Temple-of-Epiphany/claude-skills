---
name: engineering-wiki
description: Engineering wiki creation, maintenance, and governance for multi-repo software projects. Captures the TapMe Contact wiki patterns — GitHub wiki as source of truth, Mermaid diagrams, versioned pages, sidebar structure, post-completion checklists, and integration with GitHub Issues/Labels/Templates. TRIGGER on "engineering wiki", "update the wiki", "create wiki page", "wiki as source of truth", "document architecture", "wiki conventions", or any request to add/change documentation in a GitHub wiki.
---

# Engineering Wiki Skill

**Version:** 1.0.0
**Author:** Colin Bitterfield
**Email:** colin@bitterfield.com
**Date Created:** 2026-03-08
**Date Updated:** 2026-03-08

## Quick Reference

| Topic | Reference |
|-------|-----------|
| Wiki structure and page catalog | [wiki-structure.md](references/wiki-structure.md) |
| Page conventions (versioning, cross-links, formatting) | [page-conventions.md](references/page-conventions.md) |
| Mermaid diagram patterns | [diagram-patterns.md](references/diagram-patterns.md) |
| GitHub integration (Issues, Labels, Templates) | [github-integration.md](references/github-integration.md) |
| Page templates (Architecture, Service, Runbook, Reference) | [page-templates.md](references/page-templates.md) |

---

## What the Engineering Wiki Is

A GitHub wiki attached to an `{org}-engineering` repository. It is the **single source of truth** for:

- Architecture diagrams (Mermaid — GitHub renders natively)
- Service catalog and inter-service communication
- Data models, schemas, identifier formats, naming conventions
- Security boundaries, RBAC model, FusionAuth configuration
- GitHub Labels and Issue Templates documentation
- Deployment runbooks and operational procedures
- ADRs (Architecture Decision Records) for major decisions

The wiki is a **git repository** cloned separately from the code:

```bash
git clone git@github.com:{org}/{repo}-engineering.wiki.git
```

Local path convention: `~/Projects/{project}/{repo}-engineering.wiki/`

---

## Source of Truth Policy — NON-NEGOTIABLE

**Before inventing any standard, naming convention, format, or pattern:**

1. Search the engineering wiki for an existing definition
2. If one exists, follow it **exactly**
3. If none exists, **propose it to the project owner** before implementing
4. Once approved, **document the new standard in the wiki** before or alongside the implementation

This applies to:
- Identifier formats (serial numbers, UUIDs, slugs)
- Database column names and enum values
- API URL patterns and response shapes
- Status values and state machine transitions
- Error codes and HTTP status conventions
- File naming patterns
- Label naming (GitHub labels)
- Any other convention that affects consistency across repos

**Never silently invent a convention. Always check the wiki first.**

---

## On Start — Skill Check

Before any wiki work, identify what other skills are loaded:

- **github-operations** — Required when creating wiki update issues or cross-linking
- **ansible** — When documenting infrastructure playbooks or hardening procedures
- **traefik** — When updating routing/middleware documentation
- **fusionauth** — When updating identity model or auth architecture pages

If wiki changes are needed after completing a code issue, **do not close the issue** until the wiki update issue is created (or the wiki is updated in-line if the page is small).

---

## Post-Completion Checklist — When to Update the Wiki

After completing any code issue, evaluate whether these wiki pages need updating. Create a wiki update issue for each that applies:

**Always evaluate these triggers:**

| Changed | Wiki Page(s) to Check |
|---------|----------------------|
| New or changed identifier format or slug | Data Flow, Database Schema, NFC Device Catalog, Service Catalog |
| New or changed API endpoint | Customer API Guide, Admin API Specification |
| New or changed database table/column | Database Schema |
| New or changed device type, form factor | NFC Device Catalog |
| New or changed service or port | Service Catalog, Architecture Wiring, Physical Topology |
| New or changed security boundary / role | FusionAuth Identity Model, Architecture Wiring |
| New or changed infrastructure topology | Physical Topology, Network Topology |
| New or changed deploy procedure | CI/CD Pipeline, Node Deployment Runbook |
| New or changed FusionAuth configuration | FusionAuth Deployment Guide, FusionAuth Identity Model |
| New or changed label | GitHub Labels |
| New or changed issue template | GitHub Issue Templates |
| New or changed secret | Secret Inventory |
| New or changed NIST control mapping | NIST 800-53r5 Security Controls |

**Issue format for wiki updates:**

```
Title:  Wiki: {page name} — {short description of what changed}
Repo:   {org}/{repo}-engineering
Labels: documentation, p3 (unless urgent)
Body:   - Source issue: #{N}
        - Source commit: {sha}
        - Pages to update: list them
        - What changed: specific values/fields/content
```

---

## Wiki Creation — First-Time Setup

When setting up a wiki for a new multi-repo project:

### 1. Create the engineering repo

```bash
gh repo create {org}/{project}-engineering \
  --private \
  --description "Architecture, specifications, ADRs, runbooks — source of truth"
```

### 2. Enable the wiki and create the Home page

Enable it in GitHub repo settings → Features → Wikis. Create the Home page via the GitHub UI (required to initialize the wiki git repo).

### 3. Clone the wiki locally

```bash
git clone git@github.com:{org}/{project}-engineering.wiki.git \
  ~/Projects/{project}/{project}-engineering.wiki
```

### 4. Create the Sidebar

Create `_Sidebar.md` — this appears in the right navigation panel on every wiki page. See [wiki-structure.md](references/wiki-structure.md) for the full sidebar template.

### 5. Scaffold the Home page

The Home page (`Home.md`) should contain:
- Quick reference table (VPS hosts, VPN, DNS, repos, security scanning)
- Architecture diagram (Mermaid)
- Security architecture table (tiers, frontends, APIs, JWT audiences, DB roles)
- Links to all major page categories

### 6. Commit and push

```bash
cd ~/Projects/{project}/{project}-engineering.wiki
git add .
git commit -m "docs: initial wiki scaffold — Home, Sidebar, Architecture"
git push
```

---

## Page Versioning Convention

Every wiki page must have a version header:

```markdown
> **Last Updated:** YYYY-MM-DD | **Version:** X.Y.Z
>
> **Changelog:**
> - vX.Y.Z — What changed
> - vX.Y.Z-1 — Previous change
```

**OR** for reference pages (not diagrams):

```markdown
**Version:** X.Y.Z
**Date Created:** YYYY-MM-DD
**Date Updated:** YYYY-MM-DD
**Author:** {name}

---
```

**Version bump rules:**
- Major (X): Complete restructure or significant scope change
- Minor (Y): New section added, significant content addition
- Patch (Z): Corrections, updates to values, minor additions

---

## Diagram Rules

- **Mermaid only** — GitHub renders Mermaid natively in wiki pages
- No GraphViz, no PlantUML, no external image services
- Use `graph TB` (top-bottom) for architecture wiring and service maps
- Use `graph LR` (left-right) for pipelines and sequential flows
- Use `sequenceDiagram` for user journeys and API flows
- Color-code tiers consistently: 🟢 Customer, 🟡 Employee, 🟣 Data, 📊 Monitoring, ⚙️ Infrastructure
- Always show which network/tunnel inter-service calls traverse
- Include security boundaries as subgraph clusters

See [diagram-patterns.md](references/diagram-patterns.md) for copy-paste patterns.

---

## Cross-Linking

GitHub wiki uses `[[Page Name]]` syntax for internal links:

```markdown
See [[Architecture Wiring]] for the full service map.
See [[GitHub Labels]] for severity SLAs.
```

The page name must match the file name with hyphens replaced by spaces: `Architecture-Wiring.md` → `[[Architecture Wiring]]`.

For external links to code repos, issues, or PRs use full URLs:
```markdown
[tapme-infra](https://github.com/tapme-contact/tapme-infra)
```

---

## Sidebar Structure Template

The `_Sidebar.md` controls the wiki navigation panel. Organize it into sections:

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

**Services**
* (one link per service guide)

**Security**
* (auth model, NIST controls, known limitations)

**Reference**
* (data models, schemas, catalogs, labels, templates)

**Guides**
* (runbooks, deployment guides, workstation setup)

**Links**
* [Engineering Wiki](https://github.com/{org}/{repo}-engineering/wiki)
* [Issues](https://github.com/{org}/{repo}-engineering/issues)
* [All Repositories](https://github.com/orgs/{org}/repositories)
```

---

## Key Architectural Patterns to Document

These are the page types that every production-grade engineering wiki should have. Not all are required at launch — build them as the architecture matures:

| Page | Priority | When to Create |
|------|----------|----------------|
| Home | Required | Day 1 |
| Service Catalog | Required | Before any service is deployed |
| Architecture Wiring | Required | Day 1 |
| Physical Topology | Required | Before first VPS provisioned |
| Network Topology | High | When multiple hosts or networks exist |
| CI/CD Pipeline | High | When first pipeline is created |
| Database Schema | High | When schema is stable enough to document |
| GitHub Labels | Required | When labels are standardized across repos |
| GitHub Issue Templates | Required | When templates are deployed |
| Secret Inventory | Required | Before any secret is created |
| FusionAuth Identity Model | Required | When auth is configured |
| NIST 800-53r5 Security Controls | High | When hardening is implemented |
| Security Known Limitations | Medium | When accepted risks are identified |
| User Journeys | Medium | When UX flows are designed |
| Data Flow | Medium | When inter-service communication is complex |
| NFC Device Catalog / Product Catalog | Project-specific | When physical product inventory exists |
| Runbooks (per service) | High | Before production launch |
| HA Runbook | High | When HA is configured |
| Developer Workstation Setup | Medium | When onboarding second developer |

See [wiki-structure.md](references/wiki-structure.md) for the full page catalog with descriptions.
