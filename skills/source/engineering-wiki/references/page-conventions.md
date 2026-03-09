# Page Conventions Reference

**Version:** 1.0.0
**Date Created:** 2026-03-08
**Author:** Colin Bitterfield

Formatting, versioning, and style conventions observed across all TapMe Contact wiki pages.

---

## Version Header Formats

### Diagram/Architecture Pages

Used on: Architecture Wiring, Physical Topology, CI/CD Pipeline, Service Catalog

```markdown
> **Last Updated:** YYYY-MM-DD | **Version:** X.Y.Z
>
> **Changelog:**
> - vX.Y.Z — What changed (source: Issue #{N})
> - vX.Y.Z-1 — Previous significant change
```

### Reference/Specification Pages

Used on: GitHub Labels, GitHub Issue Templates, Database Schema, NFC Device Catalog

```markdown
**Version:** X.Y.Z
**Date Created:** YYYY-MM-DD
**Date Updated:** YYYY-MM-DD
**Author:** Colin Bitterfield

---
```

Followed by a changelog table or block if changes are tracked:

```markdown
**Changelog:**
- X.Y.Z (YYYY-MM-DD): Description of change
- X.Y.Z-1 (YYYY-MM-DD): Previous change
```

---

## Version Bump Rules

| Change Type | Version Bump | Example |
|-------------|-------------|---------|
| Complete restructure, new major section | Major (X+1.0.0) | Renamed all columns across schema |
| New section, significant content addition | Minor (X.Y+1.0) | Added new table, new service tier |
| Value corrections, minor additions, typos | Patch (X.Y.Z+1) | Updated port number, added missing column |

---

## Table Formatting

All tables use `|---|---|` (pipe + triple-dash) as separator rows. Column alignment is left-aligned by default.

**Data tables** (attribute/value):
```markdown
| Attribute | Value |
|---|---|
| **Key** | Value |
```

**Multi-column reference tables**:
```markdown
| Service | Port | Network | Purpose |
|---|---|---|---|
| tapme-api | :8000 | traefik_proxy, internal | Customer API |
```

**Bold left column** when the left column is a key/attribute:
```markdown
| **Purpose** | Customer-facing REST API |
| **Port** | :8000 |
```

---

## Cross-Reference Links

**Internal wiki links** (GitHub renders as hyperlinks):
```markdown
See [[Architecture Wiring]] for the full service map.
Per the [[GitHub Labels]] page, security issues require p0–p3.
```

File name `Architecture-Wiring.md` → link text `[[Architecture Wiring]]`

**External links to GitHub repos**:
```markdown
[tapme-infra](https://github.com/tapme-contact/tapme-infra)
[tapme-api](https://github.com/tapme-contact/tapme-api)
```

**Issue/PR references**:
```markdown
Source: tapme-engineering#21
Resolved: tapme-api#45
```

---

## Status Notices

**⚠️ Known limitation or accepted risk**:
```markdown
> **⚠️ Known Limitation:** CSP includes `'unsafe-inline'` (required for Next.js) — see [[Security Known Limitations]] for risk assessment and remediation plan.
```

**Status note (LIVE / in-progress / not yet built)**:
```markdown
> **Status (YYYY-MM-DD):** The marketing site is **LIVE** at https://example.com. Store is pending development.
```

**Note callout**:
```markdown
> **Note:** All prices shown as $$ pending finalization — see [[Pricing-Locations]].
```

---

## Code Blocks

Always use fenced code blocks with a language hint:

```markdown
    ```bash
    ./tapme-issues.sh --count
    ```

    ```yaml
    blank_issues_enabled: false
    ```

    ```sql
    ALTER ROLE tapme_api NOINHERIT;
    ```

    ```mermaid
    graph TB
        A --> B
    ```
```

---

## Section Headers

Use H2 (`##`) for major sections, H3 (`###`) for subsections within a section. Don't use H4 or deeper — restructure with H3 instead.

Section dividers use `---` (horizontal rule) between major H2 sections:

```markdown
## Security Labels

...content...

---

## Triage Labels

...content...
```

---

## Related Pages Footer

Every page should end with a "Related Pages" section:

```markdown
---

## Related Pages

- [[Page Name]] — brief description
- [[Another Page]] — brief description
```

---

## Negative Space — "Does NOT talk to"

For every service in the Service Catalog or Architecture Wiring, explicitly state what the service does NOT access. This is required for security reasoning:

```markdown
**Does NOT talk to:** PostgreSQL directly (all data access goes through tapme-api), tapme-admin-api (different security tier).
```

This pattern prevents future developers from accidentally introducing cross-tier calls by making the boundary explicit in the documentation.

---

## Naming Conventions in Wiki

| Convention | Rule |
|-----------|------|
| File names | `Title-Case-With-Hyphens.md` |
| Page titles (H1) | Title Case |
| Table column headers | Title Case |
| CLI commands in text | inline code: `command --flag` |
| Service names | always formatted as code: `tapme-api`, `tapme-admin` |
| Port references | always formatted as code: `:8000`, `:5432` |
| Schema names | always formatted as code: `devices`, `store`, `admin` |
| Role names | always formatted as code: `tapme_api`, `tapme_grafana` |
| Environment variables | always formatted as code: `DATABASE_URL`, `FUSIONAUTH_URL` |
| UUIDs | lowercase: `efe778de-5dc7-4db3-b39d-ed592de08ab6` |

---

## Keeping Pages Current

When updating a wiki page:

1. **Update the version header** — bump appropriate version level, update date
2. **Add changelog entry** — include date and brief description of what changed
3. **Reference the source** — mention the issue number or commit that prompted the change
4. **Commit with a descriptive message**:
   ```bash
   git commit -m "docs: update Database-Schema.md v1.1.0 — add gid column to teams table (tapme-engineering#21)"
   ```
5. **Push**:
   ```bash
   git push origin HEAD
   ```

---

## Changelog Entry Format

```markdown
**Changelog:**
- 1.2.0 (2026-03-05): `devices.teams` updated — added `gid` (immutable 8-char), `label` (16 chars mutable). Source: tapme-engineering#21
- 1.1.0 (2026-02-27): Added `tapme_grafana` role with `pg_monitor` membership. Source: tapme-grafana#13
- 1.0.0 (2026-03-02): Initial documentation — introspected from live database after HA migration.
```

Most-recent entry first. Include source issue/commit when available.
