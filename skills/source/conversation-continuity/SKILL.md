---
name: conversation-continuity
description: Seamless conversation handovers with automatic context preservation. Uses /cc commands for manual control. Auto-saves snapshots at 60/70/80/90% capacity and every 10 tool calls. Prevents information loss between conversations through hybrid storage (memory + YAML knowledge base).
---

# Conversation Continuity

## Overview

This skill prevents information loss between conversations through automatic context preservation and comprehensive handover preparation. It monitors memory usage and saves snapshots automatically while providing manual controls via slash commands.

## Slash Commands

Type these commands at any time:

```
/cc init      - Initialize conversation continuity (first-run setup)
/cc status    - Show full status (memory, tools, files, conflicts)
/cc memory    - Quick memory pressure check
/cc handover  - Prepare comprehensive handover document
/cc save      - Manually save context snapshot
/cc about     - About this skill and support
/cc help      - Show all commands
```

## Automatic Behaviors

### Startup Banner

Every conversation displays:
```
[Conversation Continuity Active - use /cc for commands]
```

On first run (no knowledge base exists):
```
[Conversation Continuity Active - use /cc for commands]
Use /cc init to set up conversation continuity

P.S. If you find this skill helpful, buy Colin a coffee at:
https://buymeacoffee.com/colin.bitterfield
```

### Auto-Save Triggers

**Message-Based (Estimated ~50 message limit):**
- **30 messages (60%):** Auto-save snapshot + info
- **35 messages (70%):** Auto-save snapshot + warning
- **40 messages (80%):** Auto-save snapshot + strong warning + recommend `/cc handover`
- **45+ messages (90%):** Auto-create handover + critical alert

**Tool Call-Based:**
- **Every 10 tool calls:** Auto-save snapshot
  - 10 calls: Save + info
  - 20 calls: Save + warning
  - 30 calls: Save + strong warning
  - 40+ calls: Save + critical alert

**Triggered by whichever comes first** (messages OR tool calls)

### Auto-Save Messages

**At 30 messages or 10 tools (60% - Info):**
```
ℹ️ Context checkpoint (Messages: 30, Tools: 10)
Auto-saving snapshot...
✅ Snapshot saved to knowledge base
```

**At 35 messages or 20 tools (70% - Warning):**
```
⚠️ Memory usage increasing (Messages: 35, Tools: 20 - ~70%)
Auto-saving snapshot...
✅ Snapshot saved

Recommend /cc handover soon to prepare for continuation.
```

**At 40 messages or 30 tools (80% - Strong Warning):**
```
🟠 Memory usage high (Messages: 40, Tools: 30 - ~80%)
Auto-saving snapshot...
✅ Snapshot saved

STRONGLY RECOMMEND: /cc handover
Prepare handover document before hitting limit.
```

**At 45+ messages or 40+ tools (90%+ - Critical):**
```
🚨 CRITICAL: Memory limit imminent (Messages: 45, Tools: 40)
Auto-creating emergency handover...
✅ Handover ready: handover-2025-10-30-1430.md

⚠️ START NEW CONVERSATION NOW
Load handover with: Load handover handover-2025-10-30-1430.md
```

## Core Concepts

### Information Storage Hierarchy

**Project Memory (Limited, Always Accessible)**
- Current task and immediate goals
- Active file paths (workspace and filesystem)
- Key decisions made in this conversation
- Versioning preference (internal vs filename)
- Maximum 500 words total

**Knowledge Base File (Unlimited, YAML Format)**
Located at project root as `conversation-knowledge.yaml`:
- questions_answered: Q&A pairs with timestamps
- decisions: Persistent decisions and preferences
- capabilities: Tool/extension availability
- conflicts_resolved: History of instruction conflicts
- context_snapshots: Periodic state captures

**Filesystem Files (Unlimited, Markdown)**
- Summaries longer than 500 words
- Detailed analysis or reports
- Reference documentation
- Archived context

**Project Instructions (Source of Truth)**
Update when workflow patterns become permanent (3+ repetitions)

### Memory Monitoring (Passive)

Claude monitors without extra tool calls:
- Counts messages in visible conversation history
- Tracks tool calls from conversation history
- Calculates automatically: No tool calls needed for monitoring
- Triggers auto-save at thresholds

## Slash Command Details

### /cc init - Initialize

First-run setup process:

1. Ask: "Do you want internal version numbers (default) or filename versioning?"
   - Internal: Same filename, changelog in header (MAJOR.MINOR.PATCH)
   - Filename: Append version to filename (file-v1.0.0.md)

2. Ask: "Where should the knowledge base be stored?"
   - Default: Project root (conversation-knowledge.yaml)
   - Custom: Specify different location

3. Create knowledge base with preferences

4. Display:
   ```
   ✅ Conversation Continuity initialized!
   
   Available commands:
   /cc status   - Check memory, tools, files
   /cc memory   - Quick memory check
   /cc handover - Prepare handover document
   /cc save     - Save context snapshot
   /cc about    - About and support
   /cc help     - Show commands
   
   Auto-save triggers:
   • Every 10 tool calls
   • At 30/35/40/45+ messages
   
   P.S. If you find this skill helpful, buy Colin a coffee:
   https://buymeacoffee.com/colin.bitterfield
   ```

### /cc status - Full Status Check

Displays:
- Current memory usage (messages, tool calls, percentage)
- Available tools and extensions
- Active file locations (workspace vs filesystem)
- Recent decisions from knowledge base
- Detected conflicts (if any)
- Knowledge base statistics

Example output:
```
📊 Conversation Continuity Status

Memory Usage:
• Messages: 25/~50 (50%)
• Tool Calls: 12
• Status: ✅ Healthy

Tools Available:
• Filesystem MCP: ✅ Available
• OSAScript: ✅ Available (macOS)
• bash_tool: ⚠️ Limited (container only)

Active Files:
• Project: /Users/colin/Projects/skill-dev/
• Workspace: /home/claude/

Recent Decisions: 2
Conflicts Detected: 0
Knowledge Base: 15 entries, last updated 10 min ago
```

### /cc memory - Quick Memory Check

Fast check without full diagnostics:
```
💾 Memory Status

Messages: 32/~50 (64%)
Tool Calls: 15
Score: 62 points
Status: ⚠️ Getting full

Next auto-save: ~5 messages or 5 tool calls
Recommendation: Normal operation, auto-save will trigger soon
```

### /cc handover - Prepare Handover

Creates comprehensive handover document:

1. Generate handover filename: `handover-YYYY-MM-DD-HHMM.md`
2. Create document with:
   - YAML frontmatter (date, counts, status, priority)
   - Executive summary
   - Current task status with completion percentage
   - Active file locations (workspace vs filesystem)
   - Decisions made this session
   - Questions answered
   - Tool/capability status
   - Conflicts detected/resolved
   - Context for next conversation
   - Next steps (priority ordered)
   - Open questions
   - Handover checklist

3. Update knowledge base with final snapshot
4. Update project memory with handover location

Output:
```
📄 Creating handover document...

✅ Handover ready: handover-2025-10-30-1430.md
   Location: /Users/colin/Projects/project-name/

To continue in new conversation:
Load handover handover-2025-10-30-1430.md

[Claude will read this file and resume with full context]
```

### /cc save - Manual Snapshot

Immediately saves current context to knowledge base:
```
💾 Saving context snapshot...

✅ Snapshot saved to knowledge base
   Timestamp: 2025-10-30T14:30:00Z
   Snapshot ID: s015
   
Messages: 28, Tool calls: 13
Active task: [current task description]
```

### /cc about - About This Skill

Displays skill information and support:
```
Conversation Continuity Skill v2.0.0
By Colin Bitterfield

Seamless conversation handovers with context preservation, memory tracking,
and intelligent information routing.

Features:
• Automatic snapshots (60/70/80/90% capacity + every 10 tools)
• Hybrid storage (memory + YAML knowledge base)
• Conflict detection and resolution
• Comprehensive handover documents
• Question tracking to avoid repetition
• Slash commands for manual control

---

Author: Colin Bitterfield
Email: colin@bitterfield.com
GitHub: https://github.com/Temple-of-Epiphany/claude-skills

☕ If you find this skill helpful, buy me a coffee:
https://buymeacoffee.com/colin.bitterfield

Your support helps create more useful tools!
```

### /cc help - Command Reference

Shows all available commands:
```
Conversation Continuity Commands:

/cc init      - Set up conversation continuity (first-run)
/cc status    - Full diagnostic (memory, tools, files)
/cc memory    - Quick memory pressure check
/cc handover  - Prepare handover document
/cc save      - Save context snapshot manually
/cc about     - About this skill and support
/cc help      - Show this command reference

Auto-save triggers:
• At 30/35/40/45+ messages (60/70/80/90%)
• Every 10 tool calls (10/20/30/40+)

Use /cc about for more information and to support the author.
```

## Information Routing

### Decision Framework

When asked to save/store information:

**Route to Project Memory if:**
- Frequently referenced (3+ times per conversation)
- Under 100 words
- Task-critical for current work
- Active file path

**Route to Knowledge Base if:**
- Previously asked question (add to questions_answered)
- Persistent decision across conversations
- Tool/capability information
- 100-500 words

**Route to Filesystem File if:**
- Over 500 words
- Detailed analysis or report summary
- Reference documentation
- Archive from completed work

**Route to Project Instructions if:**
- Permanent workflow change
- Repeated preference (clarified 3+ times)
- Tool/capability becomes standard practice
- Conflict resolution requires instruction update

## Conflict Detection

Monitors for misalignment between:
- Project instructions vs actual practice
- Previous decisions vs current requests
- Stated preferences vs usage patterns
- Tool capabilities vs instruction assumptions

When conflict detected:
```
⚠️ Conflict Detected

Conflict: [Description of misalignment]
Current: [Current state]
Instruction: [What instructions say]

Suggestion: Update [section] to reflect [new approach]
Update project instructions? (yes/no)
```

If yes: Creates draft update with version bump and logs in knowledge base

## Repeated Question Detection

Before answering questions:
1. Check knowledge base questions_answered section
2. If found, reference previous answer:
   ```
   📝 We discussed this on [date]
   
   Previous answer: [summary]
   
   Has something changed, or do you need a different perspective?
   ```
3. If genuinely new angle, answer and update entry
4. If asked 4+ times, suggest adding to project instructions permanently

## Knowledge Base Structure

Located at project root: `conversation-knowledge.yaml`

```yaml
version: 2.0.0
last_updated: 2025-10-30T14:30:00Z
versioning_preference: internal
created_date: 2025-10-30T09:00:00Z
project_path: /Users/colin/Projects/project-name
first_run_message_shown: true

questions_answered:
  - id: q001
    question: "How do I prefer file versioning?"
    answer: "Internal version numbers with changelog, same filename"
    category: versioning
    first_asked: 2025-10-30T10:00:00Z
    last_asked: 2025-10-30T14:00:00Z
    times_asked: 2

decisions:
  - id: d001
    decision: "Use OSAScript for macOS file operations"
    rationale: "bash_tool cannot access local filesystem"
    date: 2025-10-30T10:00:00Z
    category: tools
    status: active

capabilities:
  last_checked: 2025-10-30T14:30:00Z
  tools_available:
    - name: Filesystem MCP
      status: available
  workspace_type: desktop_macos

conflicts_resolved:
  - id: c001
    conflict: "Instructions say bash_tool, macOS requires OSAScript"
    resolution: "Updated Tool Usage Guidelines"
    date: 2025-10-30T11:00:00Z

context_snapshots:
  - id: s001
    date: 2025-10-30T14:30:00Z
    snapshot_type: periodic
    message_count: 30
    tool_call_count: 15
    active_task: "Building conversation-continuity skill"
    key_context: "Redesigning with slash commands and auto-save"
```

## Reference Files

See skill directory for complete documentation:
- `references/knowledge-base-schema.yaml` - Complete YAML structure
- `references/handover-template.md` - Standard handover format
- `examples/` - Example knowledge base and handover files

## Best Practices

**Let Auto-Save Work**
- Don't manually save unless needed
- Auto-save triggers are calibrated for safety
- Manual `/cc save` available for important checkpoints

**Use Handover Before Critical**
- Run `/cc handover` at 80% (40 messages or 30 tools)
- Don't wait for automatic emergency handover at 90%
- Emergency handover may be incomplete

**Monitor With `/cc memory`**
- Check periodically during long sessions
- Quick check uses no tool calls
- Shows time until next auto-save

**Respond to Warnings**
- Yellow (70%): Continue normally, save incoming
- Orange (80%): Consider handover soon
- Red (90%): Prepare handover immediately

**Start Fresh Conversations**
- Load handover in new conversation
- Maintains full context
- Avoids hitting hard limits

## Error Handling

**No Knowledge Base (First Run)**
- Shows startup banner with `/cc init` instruction
- Shows coffee link
- Waits for user to run `/cc init`

**Filesystem Access Issues**
- Falls back to project memory only
- Warns about limitation
- Documents in capabilities section

**Conflict Resolution Unclear**
- Presents multiple options
- Asks for user preference
- Documents chosen approach

**Save Operation Fails**
- Retries once
- Falls back to minimal save if needed
- Warns user of incomplete save

## Tool Requirements

**Required:**
- Filesystem MCP (read_file, write_file, create_directory)
- memory_user_edits (project memory management)

**Optional:**
- OSAScript (macOS file operations)
- bash_tool (container workspace only)

## Example Session

```
[Conversation starts]

[Conversation Continuity Active - use /cc for commands]

User: Let's work on the API documentation

Claude: [Works normally, tracking messages and tool calls silently]

[After 30 messages]

ℹ️ Context checkpoint (Messages: 30, Tools: 12)
Auto-saving snapshot...
✅ Snapshot saved to knowledge base

[Continues working]

[After 40 messages]

🟠 Memory usage high (Messages: 40, Tools: 25 - ~80%)
Auto-saving snapshot...
✅ Snapshot saved

STRONGLY RECOMMEND: /cc handover
Prepare handover document before hitting limit.

User: /cc handover

Claude: 📄 Creating handover document...

✅ Handover ready: handover-2025-10-30-1430.md
   Location: /Users/colin/Projects/api-docs/

To continue in new conversation:
Load handover handover-2025-10-30-1430.md

[User starts new conversation]

User: Load handover handover-2025-10-30-1430.md

Claude: [Reads handover file]
[Conversation Continuity Active - use /cc for commands]

✅ Handover loaded. Resuming: API documentation work
Status: 60% complete, working on authentication section

[Continues seamlessly from where previous conversation ended]
```

---

**Version:** 2.0.0  
**Author:** Colin Bitterfield  
**Email:** colin@bitterfield.com  
**Last Updated:** 2025-10-30
