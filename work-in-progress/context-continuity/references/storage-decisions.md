**Version:** 1.0.0  
**Author:** Claude Context Management System  
**Date Created:** 2025-10-30  
**Date Updated:** 2025-10-30

---

# Storage Decision Flowchart

This reference provides detailed decision trees for routing information to appropriate storage locations.

## Quick Reference Table

| Information Type | Storage Location | Tool/Method |
|-----------------|------------------|-------------|
| Current task state | Project Memory | memory_user_edits |
| Active file paths | Project Memory | memory_user_edits |
| User preferences | Project Memory | memory_user_edits |
| Recently answered questions | Project Memory | memory_user_edits |
| Tool availability | Project Memory | memory_user_edits |
| Draft documents | Project Files | create_file in workspace |
| Working code | Project Files | create_file in workspace |
| Completed deliverables | Filesystem | Filesystem:write_file |
| Final artifacts | Filesystem | Filesystem:write_file |
| Permanent standards | Project Instructions | edit PROJECT_INSTRUCTIONS.md |
| Configuration | Project Instructions | edit PROJECT_INSTRUCTIONS.md |
| Important discoveries | Project Notes | append to project-notes.md |
| Recurring information | Project Notes | append to project-notes.md |
| Handover context | Filesystem | write to handover-notes/ |

## Detailed Decision Trees

### Decision Tree 1: New Information Received

```
Start: New information to store
│
├─> Is this about the CURRENT task being worked on right now?
│   ├─> YES: Is it detailed work product?
│   │   ├─> YES: Store in Project Files (workspace)
│   │   └─> NO: Store state pointer in Project Memory
│   │
│   └─> NO: Continue to next question
│
├─> Is this a USER PREFERENCE or CONFIGURATION?
│   ├─> YES: Is it specific to this session or permanent?
│   │   ├─> SESSION: Store in Project Memory
│   │   └─> PERMANENT: Store in Project Instructions
│   │
│   └─> NO: Continue to next question
│
├─> Is this REFERENCE INFORMATION that may be needed later?
│   ├─> YES: Is it specific to current task or generally useful?
│   │   ├─> CURRENT TASK: Store in Project Files with current work
│   │   └─> GENERALLY USEFUL: Store in Project Notes on Filesystem
│   │
│   └─> NO: Continue to next question
│
├─> Is this a COMPLETED ARTIFACT user requested?
│   ├─> YES: Store on Filesystem per user preference
│   │       (check project memory for storage preference)
│   │
│   └─> NO: Continue to next question
│
└─> Is this TEMPORARY WORKING DATA?
    ├─> YES: Store in Project Files (workspace)
    └─> NO: Store in Project Notes on Filesystem
```

### Decision Tree 2: Where to Store File Paths

```
Start: Need to track a file path
│
├─> Is file actively being worked on THIS conversation?
│   ├─> YES: Store path in Project Memory under "Working Files:"
│   │
│   └─> NO: Continue to next question
│
├─> Is this a completed artifact?
│   ├─> YES: Is it on filesystem or in workspace?
│   │   ├─> FILESYSTEM: Store in Project Memory "Filesystem Artifacts:"
│   │   └─> WORKSPACE: Store in Project Memory "Workspace Artifacts:"
│   │           with warning that it won't persist
│   │
│   └─> NO: Continue to next question
│
└─> Is this a reference file or template?
    └─> YES: Store in Project Notes with purpose/description
```

### Decision Tree 3: When to Update Project Instructions

```
Start: Information that might affect project instructions
│
├─> Is this a PERMANENT STANDARD or RULE?
│   ├─> YES: Update Project Instructions immediately
│   │       Examples:
│   │       - Coding style preferences
│   │       - File naming conventions
│   │       - Required file headers
│   │       - Tool usage guidelines
│   │
│   └─> NO: Continue to next question
│
├─> Is this CONFIGURATION that applies to ALL work?
│   ├─> YES: Update Project Instructions
│   │       Examples:
│   │       - Directory structure
│   │       - Versioning approach
│   │       - Storage preferences
│   │       - Communication standards
│   │
│   └─> NO: Continue to next question
│
├─> Does this CONFLICT with existing instructions?
│   ├─> YES: Pause and ask user:
│   │       "This conflicts with [instruction]. Should I:
│   │        1. Update instructions
│   │        2. Follow existing instructions
│   │        3. Make exception for this case"
│   │
│   └─> NO: Continue to next question
│
└─> Is this TEMPORARY or TASK-SPECIFIC?
    └─> YES: Store in Project Memory or Project Notes, NOT instructions
```

## Storage Location Characteristics

### Project Memory (memory_user_edits)

**Characteristics:**
- Ephemeral: May not persist beyond conversation
- Limited capacity: Keep lean and focused
- Fast access: Immediately available
- Best for: Session state, pointers, recent context

**Best practices:**
- Store "what and where" not detailed content
- Update frequently throughout conversation
- Clean up stale information
- Use as index to more detailed storage

**Example entries:**
```
Current Task: Developing PDF form filling module
Working Files: /Users/colin/Projects/pdf-skill/scripts/fill_form.py
Last Question Answered: "Project directory structure" - See project-notes.md
Tool Issues: bash_tool cannot access local filesystem, use Filesystem: tools instead
Storage Preference: Filesystem at /Users/colin/Projects/
Versioning: Internal version numbers, same filename
```

### Project Files (workspace artifacts)

**Characteristics:**
- Temporary: Reset when container restarts
- Unlimited size: Can store large files
- Fast creation: No path restrictions
- Best for: Working drafts, intermediate outputs

**Best practices:**
- Use for iterative development
- Move to filesystem when complete
- Track locations in project memory
- Warn user about non-persistence if relevant

**Typical contents:**
- Draft documents being edited
- Code being developed
- Analysis results being refined
- Test outputs

### Filesystem (permanent storage)

**Characteristics:**
- Persistent: Survives all sessions
- Organized: Proper directory structure
- Accessible: Outside Claude interface
- Best for: Final deliverables, references

**Best practices:**
- Use absolute paths
- Follow project directory structure
- Track locations in project memory
- Verify write permissions

**Directory organization:**
```
/Users/colin/Projects/project-name/
├── docs/
│   ├── project-notes.md          # Persistent reference
│   └── ...
├── handover-notes/
│   ├── handover-TIMESTAMP.md     # Conversation transitions
│   └── ...
├── skills/
│   └── ...                        # Completed skills
└── work-in-progress/
    └── ...                        # Active development
```

### Project Instructions

**Characteristics:**
- Authoritative: Source of truth for project
- Versioned: Tracked with changelog
- Comprehensive: Complete project configuration
- Best for: Standards, conventions, guidelines

**Best practices:**
- Update sparingly and deliberately
- Always ask before major changes
- Maintain version number and changelog
- Keep organized with clear sections

**Typical sections:**
- Project overview
- Directory structure
- File header standards
- Versioning approach
- Tool usage guidelines
- Communication standards
- Workflow preferences

## Common Routing Scenarios

### Scenario 1: User shares personal preference

**Input:** "I prefer pytest over unittest"

**Analysis:**
- Permanent standard for project → Project Instructions
- Not session-specific → NOT Project Memory
- Not a deliverable → NOT Filesystem as separate file
- Applies to all future work → Update instructions

**Action:** Update PROJECT_INSTRUCTIONS.md section on testing standards

### Scenario 2: User provides temporary context

**Input:** "For this analysis, focus on Q4 data only"

**Analysis:**
- Specific to current task → Project Memory
- Temporary scope → NOT Project Instructions
- Context for this conversation → Project Memory

**Action:** Add to Project Memory: "Current Task Scope: Q4 data analysis only"

### Scenario 3: Important discovery made

**Input:** [During work, discover that X tool doesn't work with Y file format]

**Analysis:**
- Useful for future reference → Project Notes
- Not current task state → NOT just Project Memory
- Not a standard or rule → NOT Project Instructions
- Knowledge to preserve → Filesystem

**Action:** Append to project-notes.md under "Tool Behavior Notes"

### Scenario 4: Completed deliverable

**Input:** Finished writing a comprehensive report

**Analysis:**
- Final artifact → Filesystem (per user preference)
- Check project memory for storage preference
- Not temporary → NOT Project Files

**Action:** 
1. Check Project Memory for storage preference
2. Write to filesystem location
3. Update Project Memory with file path

### Scenario 5: Work in progress

**Input:** Created draft of configuration file, needs review

**Analysis:**
- Not final → NOT Filesystem yet
- Actively working on → Project Files
- Need to track location → Project Memory

**Action:**
1. Create in workspace with create_file
2. Add to Project Memory: "Working Files: /workspace/config-draft.yaml"
3. When approved, move to filesystem

## Storage Capacity Guidelines

### Project Memory Limits

Store only:
- 5-10 current state items
- 5-10 file path pointers
- 3-5 recent question topics
- 2-3 tool/capability notes
- 2-3 user preferences

If exceeding these limits, move detailed content to Project Notes.

### When to Use Handover Documents

Create handover document when:
- Memory usage reaches 80%
- Conversation approaching natural end
- Complex task will continue next session
- Many file locations to track
- Important decisions made to preserve

Don't create handover for:
- Simple, completed tasks
- Low-context conversations
- When project notes sufficient

## Anti-Patterns to Avoid

**Anti-pattern 1: Storing large content in Project Memory**
- Wrong: Store entire document text in memory
- Right: Store file path and brief description

**Anti-pattern 2: Using Project Instructions for temporary state**
- Wrong: Update instructions with "Currently working on module X"
- Right: Use Project Memory for current task state

**Anti-pattern 3: Losing filesystem artifacts in workspace**
- Wrong: Create final deliverable in workspace and forget to move
- Right: Check storage preference, write directly to filesystem

**Anti-pattern 4: Not tracking file locations**
- Wrong: Create files without recording where
- Right: Immediately update Project Memory with paths

**Anti-pattern 5: Redundant storage**
- Wrong: Store same information in multiple locations
- Right: Store once in appropriate location, use pointers elsewhere

---

**End of Storage Decision Reference v1.0.0**
