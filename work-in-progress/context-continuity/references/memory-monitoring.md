**Version:** 1.0.0  
**Author:** Claude Context Management System  
**Date Created:** 2025-10-30  
**Date Updated:** 2025-10-30

---

# Memory Monitoring Implementation

This reference provides detailed guidance for monitoring conversation memory usage and triggering appropriate actions at capacity thresholds.

## Memory Capacity Indicators

Claude doesn't have direct access to token counts or memory metrics, but can estimate usage through observable indicators:

### Primary Indicators

**1. Conversation length**
- Message count: Number of back-and-forth exchanges
- Rough estimate: ~1000-1500 tokens per message pair (user + Claude)
- Threshold: 40-50 message pairs = approaching limits

**2. Tool call accumulation**
- Each tool result adds to context
- Large tool results (file contents, search results) consume significant tokens
- Track: Number and size of tool results

**3. Artifact creation**
- Artifacts remain in context
- Large artifacts (documents, code files) use substantial tokens
- Track: Number and size of artifacts created

**4. Explicit memory warnings**
- System may provide token budget information
- User may mention approaching limits
- Error messages about context size

### Secondary Indicators

**5. Conversation complexity**
- Long, detailed responses use more tokens
- Complex technical discussions accumulate context
- Multi-step workflows maintain state

**6. File operations**
- Reading files loads content into context
- Multiple file reads accumulate
- Large file operations indicate high usage

## Threshold Detection Strategy

### Conservative Approach (Recommended)

Trigger handover preparation at ANY of these conditions:

**Condition 1: Message count**
```
If message_count >= 40:
    Trigger handover preparation
```

**Condition 2: High tool usage**
```
If tool_calls >= 20 AND large_results >= 5:
    Trigger handover preparation
```

**Condition 3: Large artifacts**
```
If total_artifact_size >= 10000_lines:
    Trigger handover preparation
```

**Condition 4: Explicit indicators**
```
If token_budget_warning OR user_mentions_limits:
    Trigger handover preparation immediately
```

### Progressive Warning System

Rather than single threshold, implement progressive warnings:

**Yellow zone (60-70% estimated capacity):**
- Begin tracking more carefully
- Consolidate information in project memory
- Move large content to filesystem
- Prepare for potential handover
- Action: Update project memory more frequently

**Orange zone (70-80% estimated capacity):**
- Prioritize essential information only
- Summarize and externalize context
- Clean up project memory
- Action: Create preliminary handover notes

**Red zone (80%+ estimated capacity):**
- Create full handover document immediately
- Save all working state
- Finalize project memory updates
- Action: Inform user and provide handover path

## Monitoring Implementation

### Tracking Variables

Maintain these counters throughout conversation:

```
conversation_metrics = {
    "message_count": 0,
    "tool_calls": 0,
    "large_tool_results": 0,
    "artifacts_created": 0,
    "artifact_total_lines": 0,
    "files_read": 0,
    "estimated_capacity_percent": 0
}
```

Update after each user message and Claude response.

### Capacity Estimation Formula

```
# Weight different factors
message_weight = message_count * 2
tool_weight = tool_calls * 1.5
artifact_weight = (artifact_total_lines / 1000) * 3

# Calculate estimated capacity percentage
estimated_capacity = (
    (message_weight + tool_weight + artifact_weight) / 150
) * 100

# Cap at 100%
estimated_capacity = min(estimated_capacity, 100)
```

This formula provides rough estimate based on observable metrics.

### Continuous Monitoring Pattern

Check capacity after each significant action:

```
After user message:
    Update message_count
    Check estimated_capacity
    If >= 80%: Trigger handover

After tool call:
    Update tool_calls
    If large result: Update large_tool_results
    Check estimated_capacity
    If >= 80%: Trigger handover

After artifact creation:
    Update artifacts_created
    Update artifact_total_lines
    Check estimated_capacity
    If >= 80%: Trigger handover

After file operation:
    Update files_read
    Check estimated_capacity
    If >= 80%: Trigger handover
```

## Handover Preparation Workflow

When threshold reached, execute this workflow:

### Step 1: Immediate Actions

```
1. Pause current work (if mid-task)
2. Inform user: "Approaching conversation capacity, preparing handover..."
3. Set handover_in_progress flag
4. Calculate handover timestamp
```

### Step 2: Gather Context

```
Collect from Project Memory:
- Current task state
- Working file paths
- Recent decisions
- Tool availability notes
- Pending questions

Collect from conversation:
- Key decisions made this session
- Important discoveries
- Completed work items
- In-progress items
```

### Step 3: Create Handover Document

```
Generate handover using template (see handover-templates.md)
Include:
- Complete task state
- All file locations
- Progress summary
- Critical context
- Next steps
- Blockers/issues
- Tool notes
```

### Step 4: Save and Update

```
1. Write handover to filesystem:
   /path/to/project/handover-notes/handover-YYYYMMDD-HHMM.md

2. Update Project Memory:
   - Add pointer to handover document
   - Update "Last Handover: [path]"
   - Brief status: "Task: [X] - Status: [Y] - Continue: [Z]"

3. Optionally update project notes:
   - Add entry about handover
   - Link to handover document
```

### Step 5: Inform User

```
Message user with:
"Approaching conversation limit. Created handover document at 
[path] with complete task state, decisions, and next steps. 
The next conversation can load this and continue seamlessly.

Current status: [brief summary]
Next step: [immediate next action]"
```

## Handover Document Structure

### Essential Sections

Every handover must include:

1. **Metadata**
   - Timestamp
   - Conversation ID (if available)
   - Project name
   - Estimated capacity when created

2. **Task State**
   - What was being worked on
   - Current progress
   - Status (in progress, blocked, etc.)

3. **File Locations**
   - All filesystem paths used
   - All workspace artifacts
   - Note which files need recreation

4. **Context**
   - Key decisions made
   - Important discoveries
   - Relevant background

5. **Next Steps**
   - Immediate next actions
   - Prioritized work items
   - Dependencies

### Optional Sections (include if relevant)

6. **Tool Notes**
   - Available tools
   - Tool limitations found
   - Workarounds discovered

7. **Blockers**
   - Any impediments
   - Missing information
   - Required user input

8. **Questions**
   - Items needing clarification
   - Decisions pending

## Loading Handover on New Conversation

When starting conversation with existing project:

### Step 1: Check for Handover

```
1. Load project memory
2. Look for "Last Handover:" entry
3. If present: Read handover document path
4. If absent: Check for handover-notes directory
```

### Step 2: Load and Process

```
1. Read handover document from filesystem
2. Extract key information:
   - Current task
   - File locations
   - Next steps
   - Critical context
3. Load into working memory for session
```

### Step 3: Resume Work

```
1. Inform user of loaded context:
   "Loaded handover from [previous session]. 
    Current task: [X]
    Ready to: [next step]"

2. Verify understanding:
   - Ask if user wants to continue or change direction
   - Confirm file locations still valid
   - Check if context still relevant

3. Proceed with work
```

## Memory Optimization Strategies

### During Conversation

**Minimize context retention:**
- Summarize long tool results
- Reference files by path, not content
- Externalize detailed information
- Use project memory as index

**Clean up as you go:**
- Remove completed task context
- Archive old handovers
- Consolidate related information
- Delete obsolete entries

**Leverage external storage:**
- Write detailed analysis to files
- Keep conversation focused
- Link to resources rather than quoting
- Use filesystem liberally

### Before Threshold

**Proactive measures (at 60-70% capacity):**

1. **Consolidate project memory**
   - Merge related entries
   - Remove stale information
   - Update pointers to new locations
   - Summarize verbose entries

2. **Externalize content**
   - Move large context to project notes
   - Write working analysis to files
   - Save intermediate results
   - Clear completed work context

3. **Summarize accumulated context**
   - Condense decisions to key points
   - Archive detailed discussion
   - Update project notes with discoveries
   - Maintain only essential context

## Anti-Patterns and Solutions

### Anti-Pattern 1: Waiting too long

**Problem:** Create handover at 95%+ capacity
**Solution:** Trigger at 80% to ensure room for handover creation

### Anti-Pattern 2: Incomplete handover

**Problem:** Handover missing critical context
**Solution:** Use comprehensive template, verify all sections

### Anti-Pattern 3: Not informing user

**Problem:** Create handover silently, user unaware
**Solution:** Always inform user with path and summary

### Anti-Pattern 4: Forgetting to update project memory

**Problem:** Handover created but not tracked
**Solution:** Always update project memory with handover pointer

### Anti-Pattern 5: Creating redundant handovers

**Problem:** Multiple handovers for same conversation
**Solution:** Create one handover at threshold, update if needed

### Anti-Pattern 6: Ignoring warnings

**Problem:** Continue working after threshold
**Solution:** Immediately create handover when triggered

## Tool Usage for Memory Management

### Using memory_user_edits

**Add handover pointer:**
```
memory_user_edits(
    command="add",
    control="Last Handover: /path/to/handover-20251030-1445.md"
)
```

**Update task status:**
```
memory_user_edits(
    command="replace",
    line_number=1,
    replacement="Current Task: Finalizing authentication module (90% complete)"
)
```

**Clean up stale entries:**
```
memory_user_edits(
    command="remove",
    line_number=5  # Remove obsolete entry
)
```

### Using Filesystem tools

**Create handover:**
```
Filesystem:write_file(
    path="/Users/colin/Projects/project-name/handover-notes/handover-20251030-1445.md",
    content="[handover content]"
)
```

**Update project notes:**
```
Filesystem:edit_file(
    path="/Users/colin/Projects/project-name/docs/project-notes.md",
    edits=[{
        oldText: "## Recent Sessions",
        newText: "## Recent Sessions\n\n- 2025-10-30 14:45: [Session summary] - Handover: handover-20251030-1445.md"
    }]
)
```

## Example Monitoring Session

### Conversation Start (0% capacity)
```
Message 1: User: "Let's continue working on the API integration"
Claude: Loads project memory, checks for handover
Metrics: message_count=1, estimated_capacity=2%
Action: Normal operation
```

### Early Conversation (30% capacity)
```
Message 15: User: "Now let's implement the authentication flow"
Claude: Working on authentication, creates code files
Metrics: message_count=15, tool_calls=8, estimated_capacity=30%
Action: Normal operation, track metrics
```

### Mid Conversation (65% capacity)
```
Message 30: User: "Let's also add rate limiting"
Claude: [Internal] Approaching yellow zone
Metrics: message_count=30, tool_calls=18, artifacts_created=3
Estimated capacity: 65%
Action: Begin consolidating project memory, prepare for potential handover
```

### Late Conversation (82% capacity)
```
Message 42: User: "Can you also create documentation for this?"
Claude: [Internal] Red zone reached, trigger handover
Metrics: message_count=42, tool_calls=25, estimated_capacity=82%

Action: 
1. Create handover document immediately
2. Save to: /project/handover-notes/handover-20251030-1630.md
3. Update project memory with handover path
4. Inform user: "Approaching conversation limit. Created handover 
   document with complete state of API integration work, authentication 
   implementation, rate limiting additions, and pending documentation 
   task. Next conversation can load this and continue."
```

---

**End of Memory Monitoring Reference v1.0.0**
