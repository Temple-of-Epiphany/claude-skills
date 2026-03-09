# Engineering Wiki Skill

**Version:** 1.0.0
**Author:** Colin Bitterfield
**Email:** colin@bitterfield.com
**Date Created:** 2026-03-08

## Overview

A Claude skill for creating and maintaining engineering wikis for multi-repo software projects. Captures the patterns used to build the TapMe Contact engineering wiki — 50+ pages covering architecture, security, services, runbooks, and reference material.

## What This Skill Teaches Claude

- How to structure a GitHub wiki as the single source of truth for a software project
- Page versioning conventions and changelog format
- Mermaid diagram patterns (architecture wiring, physical topology, CI/CD pipeline, security boundary, user journeys)
- Post-completion checklists: when code changes require wiki updates
- Integration with GitHub Issues, Labels, and Issue Templates
- Page templates for every major page type (architecture, service catalog, runbook, security, reference, ADR)
- The "negative space" pattern: explicitly documenting what a service does NOT talk to
- Multi-repo org-wide label and template sync procedures

## Source

Built from the TapMe Contact engineering wiki (`tapme-engineering`).

- Organization: [tapme-contact](https://github.com/tapme-contact)
- Wiki: https://github.com/tapme-contact/tapme-engineering/wiki
- Local clone: `~/Projects/tapme-contact/tapme-engineering.wiki/`

## Files

```
claude-skill-engineering-wiki/
├── SKILL.md                          # Main skill file
├── README.md                         # This file
├── CLAUDE.md                         # Project instructions
└── references/
    ├── wiki-structure.md             # Full page catalog, sidebar, Home page structure
    ├── page-conventions.md           # Versioning, formatting, cross-linking conventions
    ├── diagram-patterns.md           # Mermaid copy-paste patterns
    ├── github-integration.md         # Labels, templates, issue routing, sync scripts
    └── page-templates.md             # Copy-paste templates for each page type
```

## Triggers

This skill is triggered when the user says:
- "engineering wiki"
- "update the wiki"
- "create wiki page"
- "wiki as source of truth"
- "document architecture"
- "wiki conventions"
- Or any request to add/change documentation in a GitHub wiki

## Packaging

```bash
cd ~/Projects
zip -r claude-skills/skills/engineering-wiki.skill claude-skill-engineering-wiki/
```
