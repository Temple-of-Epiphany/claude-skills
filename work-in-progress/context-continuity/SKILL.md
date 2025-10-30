---
name: context-continuity
description: Maintain seamless context across conversations by intelligently routing information to appropriate storage locations (project memory, files, filesystem, or instructions), monitoring memory usage, tracking available tools and capabilities, preventing duplicate information requests, and proactively creating handover materials when approaching conversation limits. Use when starting a new conversation, when memory usage exceeds 80%, when project instructions conflict, or when user references past conversations.
---

**Version:** 1.0.0  
**Author:** Claude Context Management System  
**Date Created:** 2025-10-30  
**Date Updated:** 2025-10-30

---

## Changelog
- **1.0.0** (2025-10-30): Initial skill created

---

# Context Continuity Skill

## Overview

This skill enables Claude to maintain persistent context across conversation boundaries, preventing information loss and repetitive questions. It establishes a systematic approach for storing, retrieving, and transitioning information between conversations through intelligent routing, proactive monitoring, and seamless handover preparation.

## When to Use This Skill

Trigger this skill in these scenarios:

**On conversation start:**
- When beginning work on an existing project
- When user references past conversations or work
- When loading a project with established context

**During conversation:**
- When memory usage approaches 80% capacity
- When asked to update project memory or instructions
- When project instructions conflict with current work
- When same information is requested multiple times
- When user asks about available tools or capabilities

**On conversation end:**
- When proactively preparing handover for next conversation
- When creating continuation notes

## First-Run Configuration

On first use with a project, ask these configuration questions:

**Artifact Storage Preference:**
"Where should I save completed artifacts? Options:
1. Project Files (accessible only within this project)
2. Filesystem at [project directory path] (accessible system-wide)
3. Ask each time

Default is option 2 (filesystem). Your preference?"

**Versioning Approach:**
"For file updates, should I:
1. Maintain same filename with internal version number and changelog
2. Create new files with version suffix (e.g., document_v2.md)

Default is option 1 (internal versioning). Your preference?"

Store these preferences in project memory immediately after receiving answers.

## Core Workflow

### 1. Initial Conversation Setup

At conversation start, perform these checks:

**Check available tools and capabilities:**
- List all available tools using tool inspection
- Identify which MCP servers are connected
- Note any tool limitations or missing capabilities
- Store this inventory in session context

**Verify storage locations:**
- Check if working in project vs standalone conversation
- Verify filesystem access and allowed directories
- Determine if bash_tool access is available (workspace vs local)
- Store location context in project memory

**Load existing context:**
- Read project memory for current task and state
- Check for continuation notes from previous conversations
- Review recent project instruction updates
- Load persistent project notes

### 2. Information Routing Decision Matrix

When processing new information, route it to appropriate storage:

**Project Memory** (use memory_user_edits tool):
- Current task and immediate objectives
- Active file paths (both filesystem and workspace)
- Session state and progress markers
- Tool/capability inventory for current session
- User preferences (artifact location, versioning style)
- Recently answered questions (to prevent duplicates)

**Project Files** (workspace artifacts):
- Working documents and drafts
- Intermediate analysis results
- Temporary outputs not yet finalized
- Artifacts being iteratively developed

**Filesystem** (permanent storage):
- Completed deliverables
- Final artifacts user requested to save
- Documentation and reference materials
- Scripts and reusable code
- Project templates and standards

**Project Instructions** (update PROJECT_INSTRUCTIONS.md):
- Permanent project configuration
- Coding standards and conventions
- Workflow preferences
- Directory structure definitions
- Tool usage guidelines
- Communication standards

### 3. Memory Usage Monitoring

Track approximate memory usage throughout conversation:

**Calculate usage indicators:**
- Length of conversation history (message count)
- Cumulative token usage if available
- Number of tool calls and results loaded
- Size of artifacts in context

**At 80% threshold, automatically:**
1. Create handover document with:
   - Current task state and progress
   - Key decisions made this conversation
   - Pending work items
   - Important context for continuation
   - File locations and paths used
   - Tool/capability notes relevant to next session

2. Save handover to filesystem at: `[project-dir]/handover-notes/handover-[timestamp].md`

3. Update project memory with:
   - Pointer to handover document
   - Brief status summary
   - Next conversation starting point

4. Inform user: "Approaching conversation limit. Created handover document at [path] to ensure seamless continuation."

### 4. Duplicate Question Prevention

Maintain question log in project memory:

**Track answered questions:**
- Store hash of question topic/intent
- Note where answer is stored
- Mark timestamp of response

**On information request:**
1. Check if similar question answered recently
2. If duplicate detected:
   - Point to existing answer location
   - Ask if user wants updated information
   - Only re-answer if explicitly requested

**Clear question log:**
- After project phase transitions
- When user explicitly requests reset
- On major project changes

### 5. Project Instruction Conflict Detection

Monitor for conflicts between project instructions and work:

**Detect conflicts when:**
- User requests approach contradicting instructions
- Current work repeatedly violates instruction patterns
- Multiple clarifications needed on same instruction topic
- New requirements emerge not covered by instructions

**On conflict detection:**
1. Pause current work
2. State the specific conflict clearly
3. Ask: "This conflicts with project instructions at [section]. Should I:
   - Update project instructions to reflect new approach
   - Follow existing instructions
   - Create exception for this case"
4. Implement user's choice
5. Update relevant documentation

### 6. Tool and Capability Tracking

At conversation start and when tools are used:

**Inventory available tools:**
- MCP servers connected (filesystem, PDF, browser, etc.)
- Container vs. local filesystem access
- Special capabilities (code execution, web search, etc.)

**Track tool behavior patterns:**
- Which operations succeed/fail
- Tool limitations encountered
- Workarounds discovered

**Store in project memory:**
- Current tool availability summary
- Known limitations for this project
- Preferred tools for common operations

**Use for guidance:**
- Select appropriate tools for requests
- Avoid attempting operations with unavailable tools
- Suggest missing tools when needed

## Information Storage Patterns

### Storing Project Notes

Create persistent notes at: `[project-dir]/docs/project-notes.md`

Include:
- Frequently needed information
- Answers to recurring questions
- Important project context
- Key decisions and rationale
- Common workflows and procedures

Update notes when:
- New important information discovered
- Workflow patterns emerge
- User provides critical context
- Solutions to common problems found

### Tracking Current Task

In project memory, always maintain:
```
Current Task: [Brief description]
Task Status: [Not started | In progress | Blocked | Completed]
Working Files: [List of active file paths]
Next Steps: [Immediate next actions]
Blockers: [Any impediments]
```

Update this after each significant work unit.

### Maintaining File Registry

In project memory, track:
```
Filesystem Artifacts:
- /path/to/file.ext - [Purpose] - [Last updated]

Workspace Artifacts:
- /workspace/path/file.ext - [Purpose] - [Status]

Note: Workspace artifacts reset between container sessions
```

### Versioning Approach

Based on user preference stored in project memory:

**Internal versioning (default):**
```markdown
**Version:** 1.2.3
**Author:** Colin Bitterfield
**Email:** colin@bitterfield.com
**Date Created:** YYYY-MM-DD
**Date Updated:** YYYY-MM-DD

## Changelog
- **1.2.3** (YYYY-MM-DD): Description of changes
- **1.2.2** (YYYY-MM-DD): Previous changes
```

**Filename versioning (if preferred):**
- document_v1.md → document_v2.md
- Keep previous versions for reference
- Note version progression in project notes

## Handover Document Template

When creating handover at 80% memory threshold:

```markdown
# Conversation Handover
**Created:** [Timestamp]
**Conversation ID:** [If available]
**Project:** [Project name]

## Current Task State
[Description of what was being worked on]

## Progress Summary
- [Completed items]
- [In-progress items]
- [Not yet started]

## Key Decisions Made
1. [Decision with rationale]
2. [Decision with rationale]

## Important Context
[Critical information for next conversation to understand]

## File Locations
**Filesystem:**
- [Path]: [Purpose]

**Workspace:**
- [Path]: [Purpose, note if needs recreation]

## Tool/Capability Notes
- Available: [Tools that were working]
- Issues: [Any tool limitations encountered]
- Workarounds: [Solutions discovered]

## Next Steps
1. [Immediate next action]
2. [Subsequent actions]

## Blockers/Issues
[Any impediments to be aware of]

## Questions to Clarify
[Items needing user input]
```

## Best Practices

**Be proactive, not reactive:**
- Don't wait for user to ask about saving information
- Monitor memory usage continuously
- Create handovers before reaching limits
- Update project memory frequently

**Keep project memory lean:**
- Store pointers to detailed information, not the information itself
- Use filesystem for large content
- Keep only immediately relevant context in memory
- Clean up stale information

**Maintain clear boundaries:**
- Project memory: Ephemeral session state
- Project files: Working artifacts
- Filesystem: Permanent deliverables
- Project instructions: Configuration standards

**Prevent information loss:**
- Save critical decisions immediately
- Document important discoveries
- Track all file locations
- Create continuation notes liberally

**Avoid redundancy:**
- Check for duplicate questions before answering
- Point to existing information when available
- Consolidate repeated information
- Update existing docs rather than creating new ones

## Error Handling

**If project memory operations fail:**
- Fall back to filesystem storage in project notes
- Inform user of fallback approach
- Continue work without blocking on memory updates

**If filesystem access unavailable:**
- Use workspace artifacts with clear warnings
- Document that files won't persist
- Suggest enabling filesystem access

**If approaching token limits:**
- Immediately create handover document
- Compress information to essentials
- Provide clear continuation instructions
- Update project memory with status

**If conflicting information found:**
- Pause and highlight conflict
- Ask for clarification
- Don't make assumptions
- Document resolution in project notes

## Integration with Project Workflow

This skill coordinates with standard project practices:

**Complements project instructions:**
- Enforces standards defined in instructions
- Detects when instructions need updates
- Implements versioning per instruction preferences

**Supports memory system:**
- Uses memory_user_edits tool for session state
- Stores ephemeral context appropriately
- Avoids overloading memory with permanent data

**Enables tool ecosystems:**
- Tracks which MCP servers available
- Guides appropriate tool selection
- Documents tool behavior patterns

**Facilitates collaboration:**
- Creates clear handover documentation
- Maintains project notes for reference
- Tracks decisions and rationale

## Conversation Continuity Checklist

At start of every conversation:
- [ ] Check available tools and capabilities
- [ ] Load project memory for current task
- [ ] Review any handover notes from previous session
- [ ] Verify filesystem access and locations
- [ ] Check project notes for relevant context

During conversation:
- [ ] Monitor memory usage (alert at 80%)
- [ ] Route information to appropriate storage
- [ ] Check for duplicate questions before answering
- [ ] Update project memory with progress
- [ ] Track file locations actively
- [ ] Watch for project instruction conflicts

Before conversation ends:
- [ ] Create handover if memory usage high
- [ ] Update project notes with discoveries
- [ ] Save current task state to project memory
- [ ] Ensure all artifacts stored appropriately
- [ ] Document any tool issues or workarounds

---

## Usage Examples

**Example 1: Starting a new conversation**
```
Claude (internal): Conversation starting, checking context...
- Loading project memory: Current task is "Develop PDF processing skill"
- Tool check: Filesystem, PDF Tools, Docling available
- Loading handover note from /Users/colin/Projects/claude-skill-passing/handover-notes/handover-2025-10-30-14-30.md
- Ready to continue work

Claude: Continuing work on the PDF processing skill. Last session completed the text extraction module. Ready to work on the form filling component next?
```

**Example 2: Routing information**
```
User: Remember that I prefer using pytest over unittest for testing.

Claude (internal): This is a project-level preference.
- Not immediate task state → not project memory
- Not a working artifact → not project files
- Permanent standard → belongs in project instructions

Claude: I've updated your project instructions to reflect the pytest preference for all testing. This will be consistently applied across all work in this project.
```

**Example 3: Approaching memory limit**
```
Claude (internal): Memory usage at 82%, triggering handover preparation...

Claude: I'm approaching the conversation limit. I've created a handover document at /Users/colin/Projects/claude-skill-passing/handover-notes/handover-2025-10-30-16-45.md with our current progress on the authentication module, key decisions about JWT implementation, and next steps for token refresh logic. The next conversation can pick up seamlessly from there.
```

**Example 4: Duplicate question detection**
```
User: What's the project directory structure again?

Claude (internal): Checking project memory... this was answered 15 messages ago and directory structure documented in project notes.

Claude: The directory structure is documented in /Users/colin/Projects/claude-skill-passing/docs/project-notes.md (see "Directory Structure" section). Would you like me to show it again, or is the existing documentation sufficient?
```

**Example 5: Instruction conflict detection**
```
User: Create a README.md file to document this skill.

Claude: This conflicts with project instructions section "File Header Standards" which states skills should only contain SKILL.md without additional documentation files like README.md. Should I:
1. Update project instructions to allow README files for skills
2. Follow existing instructions (no README)
3. Create README as exception for this specific case

What would you prefer?
```

---

## Related Skills

- **skill-creator**: Framework for creating this and other skills
- **docx**: Document creation skills that may need handover context
- **pptx**: Presentation skills that benefit from project continuity
- **pdf**: PDF processing that tracks forms and templates across sessions

---

**End of Context Continuity Skill v1.0.0**
