# Page Templates Reference

**Version:** 1.0.0
**Date Created:** 2026-03-08
**Author:** Colin Bitterfield

Copy-paste starting templates for each type of wiki page. Fill in `{placeholders}`.

---

## Template 1: Architecture Diagram Page

For: Architecture Wiring, Physical Topology, Network Topology, CI/CD Pipeline

```markdown
# {Page Title}

{One-sentence description of what this diagram shows and why it matters.}

> **Last Updated:** {YYYY-MM-DD} | **Version:** 1.0.0
>
> **Changelog:**
> - v1.0.0 — Initial diagram

## {Diagram Name}

```mermaid
graph TB
    {diagram content}
```

## {Second Diagram or Table Section}

| From | To | Protocol | Network | Purpose |
|---|---|---|---|---|
| {service} | {service} | {proto} | {network} | {purpose} |

---

## Related Pages

- [[Service Catalog]] — per-service deployment details
- [[Physical Topology]] — where services run
```

---

## Template 2: Service Catalog Entry

For each service in Service-Catalog.md. This is the standard service block.

```markdown
### {service-name}

| Attribute | Value |
|---|---|
| **Purpose** | {what this service does} |
| **Framework** | {language + framework + version} |
| **Container** | `{docker image}` |
| **Port** | `:{port}` |
| **Deploys To** | {VPS hosts} |
| **Networks** | `{docker networks}` |
| **DB Role** | `{role}` — {schema} ({access level}) |
| **JWT Audience** | `{fusionauth-app-uuid}` (FusionAuth app ID) |

{One paragraph describing non-obvious behavior, key responsibilities, or why this service exists separately from others.}

**Talks to:**

| Target | Protocol | Purpose |
|---|---|---|
| {service} | {protocol} | {why} |

**Does NOT talk to:** {explicit list of services it is isolated from and why.}
```

---

## Template 3: GitHub Labels Page

For documenting a new label group in GitHub-Labels.md.

```markdown
## {Label Group Name}

> **Scope: {All repos / specific repos}** — Added {YYYY-MM-DD}

{One paragraph describing when and why to use labels in this group.}

| Label | Color | Hex | Description |
|-------|-------|-----|-------------|
| `{label-name}` | 🔵 | `#{hexcolor}` | {description} |

### When to use `{label-name}`

Apply to any issue that touches:

- {specific scenario}
- {specific scenario}

### Example usage

```
Issue: "{example issue title}"
Labels: {label1}, {label2}, {priority}
```

---
```

---

## Template 4: Runbook Page

For: HA Runbook, Node Deployment Runbook, Migration Runbook

```markdown
# {Title} Runbook

> **Version:** 1.0.0 | **Updated:** {YYYY-MM-DD}

**Purpose:** {What this runbook covers — one sentence.}

**Prerequisites:**
- {What access/tools are needed}
- {What state the system should be in}

---

## Quick Reference

| Action | Command |
|--------|---------|
| {common action} | `{command}` |

---

## {Phase 1}: {Phase Name}

### Step 1: {Step description}

```bash
{command}
```

**Expected output:**
```
{what success looks like}
```

**If this fails:** {what to check}

### Step 2: {Step description}

...

---

## Verification

After completing all steps, verify:

```bash
{verification command}
```

Expected:
```
{expected output}
```

**Test matrix:**

| Test | Expected | Pass/Fail |
|------|----------|-----------|
| {test description} | {expected} | [ ] |

---

## Rollback

If something goes wrong:

1. {rollback step}
2. {rollback step}

---

## Related Pages

- [[{Related Page}]] — {why it's related}
```

---

## Template 5: Security Page (Known Limitations)

For: Security-Known-Limitations.md

```markdown
# Security Known Limitations

> **Version:** 1.0.0 | **Updated:** {YYYY-MM-DD}

This page documents accepted security risks that are currently present in the TapMe Contact platform. Each limitation has a:
- **Severity** (P0–P3)
- **Root cause** (why this exists)
- **Risk assessment** (what it means in practice)
- **Remediation plan** (how and when it will be fixed)

All items here have been reviewed and accepted by the project owner.

---

## P2 — Medium Severity

### {Limitation Title}

**Affected Services:** {list}
**Issue:** [{org}/repo#{N}]({link})

**Root Cause:** {technical explanation}

**Risk Assessment:** {what can go wrong, likelihood, impact}

**Mitigations In Place:** {what currently reduces the risk}

**Remediation Plan:** {how to fix it, targeted timeline}

---

## P3 — Low / Informational

### {Limitation Title}

...same structure...

---

## Related Pages

- [[NIST 800-53r5 Security Controls]] — full control matrix
- [[Security Headers and CSP]] — CSP implementation
```

---

## Template 6: Reference Page (Database Schema Table)

For a single table in Database-Schema.md.

```markdown
### `{schema}.{table_name}`

{One sentence describing what this table represents.}

| Column | Type | Nullable | Default | Notes |
|---|---|---|---|---|
| `{column}` | `{type}` | NOT NULL | — | **PK** — {description} |
| `{column}` | `{type}` | NULL | — | {description} |
| `created_at` | `timestamptz` | NOT NULL | `now()` | |
| `updated_at` | `timestamptz` | NOT NULL | `now()` | |

**Indexes:**
- `{table_name}_pkey` — UNIQUE on `{pk_column}`
- `ix_{table_name}_{column}` — {UNIQUE / } on `{column}`
- `ix_{table_name}_{column}` — partial index on `{column} WHERE {condition}`

**Constraints:**
- `{constraint_name}` — FK `{column}` → `{schema}.{table}({column})`
- CHECK `{column} IN ('{val1}', '{val2}')`

---
```

---

## Template 7: ADR (Architecture Decision Record)

ADRs live in `tapme-engineering/adr/` (not the wiki). Format: MADR (Markdown Any Decision Records).

```markdown
# {N}: {Decision Title}

**Date:** {YYYY-MM-DD}
**Status:** {Accepted | Superseded by ADR-{N} | Deprecated}
**Deciders:** Colin Bitterfield

## Context and Problem Statement

{What situation prompted this decision? What was the problem?}

## Decision Drivers

- {driver 1}
- {driver 2}

## Considered Options

1. {Option 1}
2. {Option 2}
3. {Option 3}

## Decision Outcome

**Chosen option:** {N} — "{Option name}"

**Rationale:** {Why this option was chosen.}

## Pros and Cons of the Options

### Option 1: {Name}

**Pros:**
- {pro}

**Cons:**
- {con}

### Option 2: {Name}

...

## Links

- [Wiki: {Relevant Page}](https://github.com/{org}/{repo}-engineering/wiki/{Page-Name})
- [Issue #{N}](https://github.com/{org}/{repo}/issues/{N})
```

---

## Template 8: Service Guide Page

For: Customer API Guide, Admin Portal Guide, FusionAuth Deployment Guide, etc.

```markdown
# {Service Name} Guide

> **Version:** 1.0.0 | **Updated:** {YYYY-MM-DD}

**Repository:** [{org}/{repo}](https://github.com/{org}/{repo})
**Deployment:** {where and how it deploys}

---

## Overview

{2–3 sentences: what this service does, who uses it, why it exists.}

---

## Prerequisites

- {required tool/access}
- {required service must be running}

---

## Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DATABASE_URL` | Yes | — | PostgreSQL connection string |
| `FUSIONAUTH_URL` | Yes | — | FusionAuth base URL |
| `{VAR}` | {Yes/No} | {default} | {description} |

### Docker Compose Fragment

```yaml
{service-name}:
  image: ghcr.io/{org}/{repo}:latest
  ports:
    - ":{port}:{port}"
  environment:
    DATABASE_URL: ${DATABASE_URL}
  networks:
    - traefik_proxy
    - internal
  labels:
    - "traefik.enable=true"
    - "traefik.http.routers.{name}.rule=Host(`{subdomain}.{domain}`)"
```

---

## Deployment Steps

1. {step}
2. {step}

---

## Endpoints Summary

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| `GET` | `/health` | None | Health check |
| `{METHOD}` | `{path}` | {role} | {purpose} |

---

## Troubleshooting

### {Common Problem}

**Symptom:** {what you see}
**Cause:** {why it happens}
**Fix:** {how to resolve}

---

## Related Pages

- [[Service Catalog]] — dependency matrix
- [[Architecture Wiring]] — network topology
```
