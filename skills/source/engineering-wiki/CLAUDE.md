# CLAUDE.md — Engineering Wiki Skill

**Version:** 1.0.0
**Author:** Colin Bitterfield
**Email:** colin@bitterfield.com
**Date Created:** 2026-03-08
**Date Updated:** 2026-03-08

## Project Overview

This is the Claude skill for engineering wiki creation and maintenance. It captures the patterns used in building the TapMe Contact engineering wiki.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill file — loaded by Claude when skill is active |
| `references/wiki-structure.md` | Full page catalog, sidebar template, Home page structure |
| `references/page-conventions.md` | Versioning, formatting, cross-linking, naming rules |
| `references/diagram-patterns.md` | Mermaid copy-paste patterns for all diagram types |
| `references/github-integration.md` | Labels, templates, issue routing, sync scripts |
| `references/page-templates.md` | Copy-paste templates for each wiki page type |

## Source Project

Built from the TapMe Contact engineering wiki:
- Wiki: https://github.com/tapme-contact/tapme-engineering/wiki
- Local clone: ~/Projects/tapme-contact/tapme-engineering.wiki/

## Skill Registration

To register this skill with Claude, it needs to be packaged as a `.skill` zip file and placed in `~/Projects/claude-skills/skills/`.

```bash
cd ~/Projects
zip -r claude-skills/skills/engineering-wiki.skill claude-skill-engineering-wiki/
```
