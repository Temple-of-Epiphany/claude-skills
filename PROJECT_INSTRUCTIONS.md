# Project Instructions - Claude Skill Development
**Version:** 1.0.0  
**Author:** Colin Bitterfield  
**Email:** colin@bitterfield.com  
**Date Created:** October 30, 2025  
**Date Updated:** October 30, 2025

---

## Changelog
- **1.0.0** (2025-10-30): Initial project instructions created

---

## Project Overview

**Purpose:** Develop custom skills for Claude using the skill-creator framework to extend Claude's capabilities with specialized knowledge, workflows, and tool integrations.

**Project Directory:** `/Users/colin/Projects/claude-skill-passing`

**Working Environment:** macOS local filesystem using OSAScript and MCP Filesystem tools

---

## Directory Structure

```
/Users/colin/Projects/claude-skill-passing/
├── PROJECT_INSTRUCTIONS.md          # This file
├── skills/                          # Completed skills ready for use
│   ├── skill-name/
│   │   ├── SKILL.md                # Main skill file
│   │   ├── README.md               # Documentation
│   │   └── examples/               # Usage examples (optional)
├── work-in-progress/                # Skills under development
│   └── skill-name/
├── templates/                       # Reusable skill templates
├── docs/                           # Project documentation
│   ├── skill-design-patterns.md   # Common patterns and best practices
│   └── testing-checklist.md       # Skill validation checklist
└── archive/                        # Deprecated or superseded skills
```

---

## File Header Standards

All files must include:
```markdown
**Version:** x.x.x
**Author:** Colin Bitterfield
**Email:** colin@bitterfield.com
**Date Created:** YYYY-MM-DD
**Date Updated:** YYYY-MM-DD
```

For code files:
```python
# Author: Colin Bitterfield
# Email: colin@bitterfield.com
# Date Created: YYYY-MM-DD
# Date Updated: YYYY-MM-DD
# Version: x.x.x
```

---

## Semantic Versioning

Use semantic versioning (MAJOR.MINOR.PATCH):
- **MAJOR:** Breaking changes, incompatible API changes
- **MINOR:** New features, backward-compatible additions
- **PATCH:** Bug fixes, documentation updates

Maintain changelog at top of all files showing version history.

---

## Skill Development Workflow

### Phase 1: Planning
1. Read skill-creator skill documentation at `/mnt/skills/public/skill-creator/SKILL.md`
2. Define skill purpose, triggers, and success criteria
3. Identify required tools, resources, and dependencies
4. Create skill directory in `work-in-progress/`
5. Ask clarifying questions before implementation

### Phase 2: Development
1. Create SKILL.md with proper header and versioning
2. Follow skill-creator framework structure:
   - Overview section
   - When to use section
   - Core concepts
   - Tools and resources
   - Workflow/procedures
   - Examples
   - Best practices
   - Error handling
3. Test skill with representative use cases
4. Document limitations and edge cases

### Phase 3: Documentation
1. Create README.md with:
   - Installation instructions
   - Usage examples
   - Configuration options
   - Troubleshooting guide
2. Add inline documentation within SKILL.md
3. Create example files if helpful

### Phase 4: Deployment
1. Move completed skill to `skills/` directory
2. Update project memory with skill location
3. Test skill integration with Claude
4. Document in project changelog

---

## Skill Quality Standards

Skills must:
- Have clear, specific triggers for when to use them
- Include concrete examples and workflows
- Document all tools and dependencies
- Handle errors gracefully
- Be maintainable and well-documented
- Use prose paragraphs for explanations (not bullet lists unless specifically needed)
- Follow BLUF writing style for technical documentation

---

## Tool Usage Guidelines

**Filesystem Operations:** Use MCP Filesystem tools exclusively
- `read_file`, `write_file`, `edit_file`
- `list_directory`, `directory_tree`
- `create_directory`, `move_file`
- `search_files`, `get_file_info`

**macOS Operations:** Use OSAScript for system-level tasks

**Container Operations:** Only use bash_tool when explicitly working in container environment (bash_tool cannot access local filesystem)

**File Paths:** Always use absolute paths: `/Users/colin/Projects/claude-skill-passing/...`

---

## Communication Standards

- Execute straightforward tasks immediately without asking permission
- Ask clarifying questions only when genuinely ambiguous
- Use BLUF (Bottom Line Up Front) writing style
- Provide technical explanations appropriate for cybersecurity/sysadmin expertise
- Be direct and honest, avoid unsolicited validation or encouragement
- Write documentation in prose paragraphs, not lists
- Use standard ASCII characters only (no UTF special characters or emoji)

---

## Workflow Preferences

- Before starting work: Read all prompts, organize work, ask clarifying questions
- Before adding unrequested content: Ask during initial clarifying questions
- Track changes and decisions within skill documentation (changelog)
- Before reaching message limit: Update project memory or create continuation file with complete context

---

## Skill Integration

Skills developed in this project are intended for:
- Integration with Claude's skill system
- Use in specific projects requiring specialized knowledge
- Sharing with team members or community

Each skill should be self-contained and usable by Claude without additional context beyond the SKILL.md file.

---

## Project-Specific Notes

- This project uses the skill-creator framework available at `/mnt/skills/public/skill-creator/SKILL.md`
- Skills should extend Claude's capabilities in areas requiring specialized workflows
- Focus on practical, reusable skills that solve real problems
- Prioritize maintainability and clear documentation

---

## Next Steps

1. Review skill-creator documentation
2. Identify first skill to develop
3. Create work-in-progress directory structure
4. Begin skill planning phase

---

**End of Project Instructions v1.0.0**
