# GitHub Integration Reference

**Version:** 1.0.0
**Date Created:** 2026-03-08
**Author:** Colin Bitterfield

How the engineering wiki integrates with GitHub Issues, Labels, Issue Templates, and Pull Requests across a multi-repo organization.

---

## Wiki as Documentation for GitHub Conventions

Two pages in the wiki document the GitHub conventions themselves:

| Wiki Page | File | Purpose |
|-----------|------|---------|
| GitHub Labels | `GitHub-Labels.md` | All labels with colors, hex codes, descriptions, SLAs, creation log |
| GitHub Issue Templates | `GitHub-Issue-Templates.md` | Five templates with field reference, decision guide, update procedure |

These pages are the **reference** that all developers consult. The actual labels and templates are in every repo's `.github/` directory, but the wiki is the single source of truth for what they mean and how to use them.

---

## Label Architecture

Labels are **org-wide** — all repos in the organization carry the same label set. The wiki page documents this.

### Label Groups

| Group | Labels | Purpose |
|-------|--------|---------|
| Triage (type) | `bug`, `enhancement`, `security`, `task`, `question`, `documentation`, `duplicate`, `invalid`, `wontfix`, `good first issue`, `help wanted` | What kind of work is this? |
| Priority | `p0`, `p1`, `p2`, `p3` | How urgent/severe? |
| Domain | `database`, `fusionauth`, `store`, `stripe`, `auth`, `ui`, `infrastructure`, `availability`, etc. | What technical area? |
| Process | `tech-debt`, `scaffold`, `blocker`, `testing`, `task` | What phase of work? |

### Every Issue Must Have

1. One **triage/type** label (often auto-applied by template)
2. One **priority** label (applied manually after creation)
3. Zero or more **domain** labels (where relevant)

### Priority SLAs (Security Issues)

| Label | Severity | SLA |
|-------|----------|-----|
| `p0` | Critical — treat as incident | Immediate |
| `p1` | High | Within 24 hours |
| `p2` | Medium | Within current sprint |
| `p3` | Low/Informational | As bandwidth allows |

---

## Issue Template Architecture

All repos in the org have **five templates** in `.github/ISSUE_TEMPLATE/`. Blank issues are disabled.

| # | File | Auto-label | Use When |
|---|------|-----------|----------|
| 1 | `01-bug-report.yml` | `bug` | Something broken and not working as designed |
| 2 | `02-feature-request.yml` | `enhancement` | New functionality or behavior change |
| 3 | `03-security-issue.yml` | `security` | Vulnerability, CVE, hardening gap — always use this even if it looks like a bug |
| 4 | `04-task.yml` | `task` | Internal work: upgrades, refactors, CI/CD, migrations |
| 5 | `05-rfi.yml` | `question` | Decision, clarification, or research result needed before work can start |

`config.yml` in each `.github/ISSUE_TEMPLATE/` directory:
```yaml
blank_issues_enabled: false
contact_links:
  - name: Security Disclosure (P0/P1)
    url: mailto:security@{domain}
    about: For critical/high vulnerabilities with active exploitation risk, notify directly.
  - name: Engineering Wiki
    url: https://github.com/{org}/{repo}-engineering/wiki
    about: Architecture docs, runbooks, data models, and GitHub label guidance.
```

### Decision Guide: Which Template?

```
Is something broken that used to work?                → Bug Report
Is this a security vulnerability, CVE, or hardening gap?  → Security Issue (always)
Do you want new functionality or changed behavior?    → Feature Request
Is this internal work with no direct user impact?     → Task
Do you need information or a decision before work can proceed? → RFI
```

---

## Issue Routing by Repo

Before creating an issue, confirm it belongs in the right repo:

| This kind of issue... | Goes in this repo |
|-----------------------|------------------|
| Customer API bug or feature | `tapme-api` |
| Admin API bug or feature | `tapme-admin-api` |
| Customer portal (Next.js app) | `tapme-app` |
| Marketing site / store UI | `tapme-site` |
| Admin portal UI | `tapme-admin` |
| Traefik routing or middleware | `tapme-traefik` |
| PostgreSQL schema or migration | `tapme-sql` |
| Redis configuration | `tapme-redis` |
| Infrastructure, Ansible, OS hardening | `tapme-infra` |
| FusionAuth configuration | `tapme-fusion-auth` |
| Grafana / Prometheus dashboards | `tapme-grafana` |
| Uptime Kuma monitoring | `tapme-uptime` |
| Store catalog, order management | `tapme-store` |
| Architecture docs, wiki, ADRs | `tapme-engineering` |

---

## Syncing Labels and Templates Org-Wide

When a new label is needed or a template is updated, it must propagate to all repos.

### Add a label to all repos

```bash
REPOS=$(gh repo list {org} --limit 50 --json name --jq '.[].name')
for repo in $REPOS; do
  gh label create "label-name" \
    --repo "{org}/$repo" \
    --color "hexcolor" \
    --description "Description of the label" \
    --force
done
```

Use `--force` to create-or-update (no error if label already exists).

### Update a template across all repos

```bash
REPOS=$(gh repo list {org} --limit 50 --json name --jq '.[].name')
TEMPLATE="01-bug-report.yml"

for repo in $REPOS; do
  content=$(base64 < "/tmp/issue-templates/$TEMPLATE" | tr -d '\n')
  sha=$(gh api "repos/{org}/$repo/contents/.github/ISSUE_TEMPLATE/$TEMPLATE" \
    --jq '.sha' 2>/dev/null || echo "")
  if [ -n "$sha" ]; then
    gh api "repos/{org}/$repo/contents/.github/ISSUE_TEMPLATE/$TEMPLATE" \
      --method PUT \
      --field message="ci: update issue template" \
      --field content="$content" \
      --field sha="$sha" --silent && echo "$repo ✓"
  else
    echo "$repo — file not found, skipping"
  fi
done
```

After syncing, update the **GitHub Issue Templates** wiki page (bump version, add changelog entry).

---

## Issue Lifecycle and Wiki Touchpoints

The wiki intersects with the issue lifecycle at these points:

| Phase | Wiki Action |
|-------|------------|
| Before creating an issue | Search existing issues with `./tapme-issues.sh` to avoid duplicates |
| Creating an issue | Reference wiki page if standards already exist (link in issue body) |
| While working | Add comments referencing wiki pages for context |
| After completing an issue | Run post-completion checklist; create wiki update issue if needed |
| Closing an issue | Link to wiki page if the standard was documented there |

---

## Wiki Update Issues

Format for issues that update the wiki:

```
Title:  Wiki: {Page Name} — {short description of change}
Repo:   {org}/{project}-engineering
Labels: documentation, p3 (adjust if urgent)
```

Body template:
```markdown
## Wiki Update Required

**Page:** [[{Page Name}]]
**Source Issue/Commit:** #{N} / {sha}

## What Changed

- {specific field, table, value, or section that needs updating}
- {another change}

## New Content

```{type}
{exact new values, SQL, JSON, or prose to add}
```

## Acceptance Criteria

- [ ] Wiki page updated with accurate information
- [ ] Version number bumped and changelog entry added
- [ ] Cross-linked pages updated if references changed
```

---

## GitHub Actions Pinning Policy

Documented in the CI/CD Pipeline wiki page. All `uses:` lines in GitHub Actions workflows must use SHA pins:

```yaml
uses: actions/checkout@34e114876b0b11c390a56381ad16ebd13914f8d5 # v4.3.1
```

Never use mutable tags (`@v4`, `@v1.2.5`). Find the SHA:

```bash
gh api repos/OWNER/REPO/git/ref/tags/TAG --jq .object.sha
```

The CI/CD Pipeline wiki page should include this policy and a table of all pinned actions with their versions.

---

## Pull Request Workflow

### Branch Naming Convention

```
{type}/{issue-number}-{short-description}
```

Types: `feat/`, `fix/`, `chore/`, `docs/`, `security/`

Examples:
```
feat/45-customer-profile-edit
fix/41-session-timeout-before-app
docs/21-update-database-schema-wiki
```

### PR Lifecycle and Wiki Integration

| Step | Action |
|------|--------|
| Branch created | Comment on issue: "Work started on branch `{branch}`" |
| PR opened | Comment on issue with PR link |
| PR merged | Issue closes automatically via `Closes #N` |
| After merge | Run post-completion checklist; create wiki update issue(s) if needed |

Wiki update issues are created *after* code PRs merge, not before. The code change is the trigger for the wiki update.
