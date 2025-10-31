# Handover Template

**Version:** 1.0.0  
**Author:** Colin Bitterfield  
**Email:** colin@bitterfield.com  
**Date Created:** 2025-10-30  
**Date Updated:** 2025-10-30

---

## Template Purpose

This template provides the standard format for conversation handover documents created by the conversation-continuity skill. Handovers enable seamless continuation of work in a new conversation by capturing complete context, state, and next steps.

## When to Create Handover

Create handover document when:
- Memory pressure reaches critical threshold (score >= 70)
- User requests "prepare handover"
- Conversation reaches 45+ messages or 20+ tool calls
- Major milestone completed and next phase requires fresh start
- Blocked and need to research/consult before continuing

## Handover File Naming

Format: `handover-YYYY-MM-DD-HHMM.md`

Examples:
- `handover-2025-10-30-1430.md`
- `handover-2025-10-31-0915.md`

Location: Project root directory

## Complete Handover Template

```markdown
---
handover_date: 2025-10-30T14:30:00Z
conversation_duration: 120 minutes
message_count: 45
tool_call_count: 20
memory_score: 72
version: 1.0.0
author: Colin Bitterfield
email: colin@bitterfield.com
project: claude-skill-passing
previous_handover: handover-2025-10-29-1600.md
next_conversation_priority: high
---

# Conversation Handover: [Brief Description]

**Prepared:** October 30, 2025 at 2:30 PM  
**Status:** [In Progress | Blocked | Completed]  
**Priority:** [High | Medium | Low]

---

## Executive Summary

[2-3 sentence overview of what was accomplished and what needs to happen next. This should be readable in 30 seconds and give complete context for continuation.]

---

## Current Task Status

### Primary Task
**Task:** [Description of main task]  
**Status:** [In Progress | Blocked | Completed]  
**Completion:** [X]%  

**What's Done:**
- [Specific accomplishment 1]
- [Specific accomplishment 2]
- [Specific accomplishment 3]

**What's Remaining:**
- [Specific next step 1]
- [Specific next step 2]
- [Specific next step 3]

**Blockers:**
- [Blocker 1 with possible solution]
- [Blocker 2 with possible solution]

### Secondary Tasks
**Task:** [Description]  
**Status:** [Status]  
**Priority:** [High | Medium | Low]  
**Notes:** [Brief context]

---

## Active File Locations

### Project Filesystem
Files in `/Users/colin/Projects/[project-name]/`:

| File Path | Purpose | Status | Last Modified |
|-----------|---------|--------|---------------|
| `/path/to/file1.md` | [Purpose] | [Status] | 2025-10-30 |
| `/path/to/file2.py` | [Purpose] | [Status] | 2025-10-30 |

### Container Workspace
Files in `/home/claude/`:

| File Path | Purpose | Status | Notes |
|-----------|---------|--------|-------|
| `/home/claude/script.py` | [Purpose] | [Status] | [Notes] |

**Important:** [Any critical notes about file locations, versions, or states]

---

## Decisions Made This Session

### Decision 1: [Topic]
**Decision:** [What was decided]  
**Rationale:** [Why this decision was made]  
**Impact:** [What this affects]  
**Confidence:** [High | Medium | Low]  
**Date:** 2025-10-30T10:00:00Z

### Decision 2: [Topic]
**Decision:** [What was decided]  
**Rationale:** [Why this decision was made]  
**Impact:** [What this affects]  
**Confidence:** [High | Medium | Low]  
**Date:** 2025-10-30T11:30:00Z

---

## Questions Answered

### Q1: [Question as asked]
**Answer:** [Summary of answer]  
**Category:** [versioning | tools | workflow | etc.]  
**Asked:** [Number of times]  
**Recorded In:** [Knowledge base entry ID]

### Q2: [Question as asked]
**Answer:** [Summary of answer]  
**Category:** [Category]  
**Asked:** [Number of times]  
**Recorded In:** [Knowledge base entry ID]

**Note:** Full Q&A history available in `conversation-knowledge.yaml`

---

## Tool & Capability Status

### Available Tools
- **Filesystem MCP:** Available, full access
- **OSAScript:** Available, macOS operations
- **bash_tool:** Limited, container workspace only
- **PDF Tools:** Available
- **Docling MCP:** Available

### Extensions Enabled
- web_search
- web_fetch
- conversation_search
- recent_chats
- memory_user_edits

### Known Limitations
- [Limitation 1 with workaround]
- [Limitation 2 with workaround]

### Workspace Type
**Type:** [desktop_macos | desktop_windows | web | claude_code]  
**Implications:** [Any relevant implications for tool usage]

---

## Conflicts Detected & Resolved

### Conflict 1: [Brief Description]
**Type:** [instruction | preference | tool | workflow]  
**Detected:** 2025-10-30T11:00:00Z  
**Resolution:** [How it was resolved]  
**Instruction Update:** [Yes/No - which section]  
**Confidence:** [High | Medium | Low]  

### Conflict 2: [Brief Description]
**Type:** [Type]  
**Detected:** [Date]  
**Resolution:** [Resolution]  

**Note:** Full conflict history available in `conversation-knowledge.yaml`

---

## Context for Next Conversation

### Essential Background
[Paragraph explaining the complete context needed to continue effectively. Include project goals, approach decisions, constraints, and any relevant history. This should enable someone to pick up the work with full understanding.]

### Mental Model
[Describe the mental model or framework being used for this work. What patterns, principles, or approaches are guiding decisions?]

### Key Constraints
- [Constraint 1]
- [Constraint 2]
- [Constraint 3]

### Assumptions Made
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

---

## Next Steps (Priority Order)

### Immediate Actions (Start Here)
1. **[Action 1]**
   - Context: [Why this is needed]
   - Approach: [How to approach this]
   - Dependencies: [What's needed]
   - Estimated effort: [Time estimate]

2. **[Action 2]**
   - Context: [Why this is needed]
   - Approach: [How to approach this]
   - Dependencies: [What's needed]
   - Estimated effort: [Time estimate]

### Follow-Up Actions
3. **[Action 3]**
   - Context: [Why this is needed]
   - Dependencies: [What's needed]

4. **[Action 4]**
   - Context: [Why this is needed]
   - Dependencies: [What's needed]

### Future Considerations
- [Consideration 1 - not immediate but important]
- [Consideration 2 - not immediate but important]

---

## Open Questions

### Unanswered Questions Requiring User Input
1. **[Question 1]**
   - Priority: [High | Medium | Low]
   - Impact: [What this affects]
   - Options: [If applicable]

2. **[Question 2]**
   - Priority: [Priority]
   - Impact: [Impact]

### Technical Unknowns Requiring Research
1. **[Unknown 1]**
   - Research needed: [What to investigate]
   - Why it matters: [Relevance]

---

## References & Resources

### Project Files
- `PROJECT_INSTRUCTIONS.md` - Project guidelines and standards
- `conversation-knowledge.yaml` - Knowledge base with full history
- [Other relevant files]

### External Resources
- [URL 1 - Description]
- [URL 2 - Description]

### Previous Handovers
- `handover-2025-10-29-1600.md` - [Brief description of previous context]

---

## Conversation Metrics

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| Messages | 45 | 45 (critical) | ⚠️ Critical |
| Tool Calls | 20 | 20 (critical) | ⚠️ Critical |
| Memory Score | 72 | 70 (critical) | ⚠️ Critical |
| Duration | 120 min | N/A | ℹ️ Info |

**Recommendation:** Continue in new conversation to maintain performance.

---

## Handover Checklist

Before continuing in new conversation:

- [ ] Handover file created and saved
- [ ] Knowledge base updated with snapshot
- [ ] Project memory updated with handover location
- [ ] All file changes committed/saved
- [ ] Next steps clearly defined
- [ ] Blockers documented with possible solutions
- [ ] Open questions listed with priorities
- [ ] Context complete and self-contained

---

## How to Continue

### In New Conversation:
```
Load handover: handover-2025-10-30-1430.md

[Claude will read this handover file and immediately continue work with full context]
```

### What Claude Will Do:
1. Read this handover document completely
2. Load knowledge base (`conversation-knowledge.yaml`)
3. Verify tool capabilities
4. Review file locations and states
5. Understand current task and next steps
6. Continue work seamlessly from where we left off

---

**End of Handover**
```

## Handover Preparation Workflow

### Step 1: Gather Information
1. Calculate final metrics (messages, tool calls, score)
2. Review conversation history for key points
3. Check filesystem and workspace states
4. Review knowledge base for recent entries
5. Identify all active tasks and their statuses

### Step 2: Create Handover Document
1. Copy template
2. Fill in YAML frontmatter with accurate data
3. Write executive summary (2-3 sentences max)
4. Document task status with specific details
5. List all active file locations with purposes
6. Record decisions made this session
7. List questions answered with knowledge base references
8. Document tool status and limitations
9. Record any conflicts and resolutions
10. Write comprehensive context section
11. Define clear next steps in priority order
12. List open questions requiring attention
13. Include relevant references
14. Verify handover checklist

### Step 3: Update Supporting Files
1. Create final snapshot in knowledge base
2. Update project memory with handover file location
3. Update statistics in knowledge base
4. Archive any completed context to knowledge base

### Step 4: Verify Completeness
1. Read handover as if you're the next conversation
2. Check that all context is self-contained
3. Verify file paths are absolute and correct
4. Ensure next steps are actionable
5. Confirm no critical information is missing

### Step 5: Communicate Handover
1. Save handover file to project root
2. Inform user: "Handover prepared at [filename]"
3. Provide continuation instruction
4. Confirm knowledge base and memory updated

## Handover Quality Standards

A high-quality handover:
- **Self-contained**: No need to reference conversation history
- **Actionable**: Next steps are specific and clear
- **Complete**: All context needed to continue effectively
- **Organized**: Easy to scan and find information
- **Accurate**: Metrics and states are current
- **Referenced**: Links to knowledge base and project files
- **Verified**: Checklist completed

## Common Handover Pitfalls

**Avoid:**
- Vague next steps ("Continue working on X")
- Missing file locations
- Incomplete context (assumes prior knowledge)
- No priority ordering of tasks
- Ignoring blockers or open questions
- Skipping metrics or tool status
- Forgetting to update knowledge base
- Not linking to previous handovers

## Handover Template Variations

### Quick Handover (Low Complexity)
For simple tasks or brief interruptions:
- Abbreviated sections
- Focus on task status and next steps
- Minimal context needed
- Use when conversation is short (< 20 messages)

### Full Handover (High Complexity)
For complex projects or lengthy conversations:
- Complete all sections
- Detailed context and background
- Comprehensive file listings
- Extensive next steps with dependencies
- Use when conversation is long (40+ messages)

### Blocked Handover (Awaiting Input)
When work cannot continue without user input:
- Emphasize blockers section
- Clear questions requiring answers
- Options for each blocker
- Minimal next steps (contingent on answers)

### Milestone Handover (Phase Completion)
When major phase is complete:
- Celebrate accomplishments
- Document lessons learned
- Define clear next phase objectives
- Archive completed task details to knowledge base

## Example Minimal Handover

For simpler cases, a minimal version:

```markdown
---
handover_date: 2025-10-30T14:30:00Z
message_count: 25
tool_call_count: 10
memory_score: 45
version: 1.0.0
project: example-project
---

# Handover: [Task Name]

## Summary
[2-3 sentences on status and next steps]

## Current Status
**Task:** [Description]  
**Completion:** 60%  
**Next Step:** [Specific action]

## Active Files
- `/path/to/file1.md` - [Purpose]
- `/path/to/file2.py` - [Purpose]

## Key Decisions
- [Decision 1]
- [Decision 2]

## Next Actions
1. [Action 1]
2. [Action 2]

## Open Questions
- [Question 1]

---
Continue with: Load handover handover-2025-10-30-1430.md
```

## Loading Handover in New Conversation

When starting new conversation, user says:
```
Load handover: handover-2025-10-30-1430.md
```

Claude should:
1. Use Filesystem:read_file to load handover
2. Read conversation-knowledge.yaml
3. Verify tool capabilities
4. Acknowledge: "Handover loaded. Ready to continue [task name]. Next step: [action 1]"
5. Proceed with work immediately

---

**End of Handover Template Documentation v1.0.0**
