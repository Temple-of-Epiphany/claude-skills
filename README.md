# Claude Skills by Colin Bitterfield

Custom skills for Claude AI to enhance productivity and conversation continuity.

## Available Skills

### Conversation Continuity v1.0.0

Seamless conversation handovers with context preservation, memory tracking, and intelligent information routing.

**Features:**
- Hybrid storage (project memory + YAML knowledge base)
- Memory pressure tracking with proactive warnings
- Conflict detection between instructions and practice
- Automated capability checking
- Question tracking to avoid repetition
- Comprehensive handover document generation

**Installation:**
1. Download: [conversation-continuity.skill](skills/conversation-continuity.skill)
2. In Claude, go to Settings → Skills
3. Click "Upload Skill"
4. Select the downloaded file
5. Enable the skill

**Documentation:** See [work-in-progress/conversation-continuity/](work-in-progress/conversation-continuity/) for complete source and documentation.

## Project Structure

```
claude-skill-passing/
├── skills/                          # Packaged .skill files ready to use
│   └── conversation-continuity.skill
├── work-in-progress/                # Skills under development
│   └── conversation-continuity/     # Source files for skill
├── scripts/                         # Packaging and validation tools
├── docs/                           # Documentation
│   └── LOADING_AND_PUBLISHING.md   # Complete guide
└── PROJECT_INSTRUCTIONS.md         # Project guidelines
```

## Usage

### Loading a Skill in Claude

1. Download the `.skill` file from the `skills/` directory
2. In Claude's interface, go to Settings
3. Navigate to Skills section
4. Click "Upload Skill" or "Add Skill"
5. Select the downloaded `.skill` file
6. Enable the skill after upload

### Building From Source

```bash
# Clone repository
git clone https://github.com/Temple-of-Epiphany/claude-skills.git
cd claude-skills

# Package a skill
python3 scripts/package_skill.py work-in-progress/conversation-continuity skills
```

## Development

See [PROJECT_INSTRUCTIONS.md](PROJECT_INSTRUCTIONS.md) for:
- Skill development workflow
- Directory structure
- File header standards
- Semantic versioning
- Quality standards

See [docs/LOADING_AND_PUBLISHING.md](docs/LOADING_AND_PUBLISHING.md) for:
- Packaging workflow
- Publishing to GitHub
- Distribution methods
- Version management

## Support

If you find these skills helpful, consider buying me a coffee:  
☕ https://buymeacoffee.com/colin.bitterfield

Your support helps me create more useful tools and skills!

## License

MIT License - See individual skills for specific licensing details.

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Author

**Colin Bitterfield**  
Email: colin@bitterfield.com  
GitHub: [@cbitterfield](https://github.com/cbitterfield)

---

## Skill Details

### Conversation Continuity

**Purpose:** Maintain context across Claude conversations by tracking decisions, detecting conflicts, routing information appropriately, and preparing comprehensive handovers.

**Key Components:**
- **SKILL.md**: Main skill documentation following skill-creator framework
- **Knowledge Base Schema**: YAML structure for persistent storage
- **Handover Template**: Standard format for conversation transitions
- **Helper Script**: Python utilities for memory calculations and initialization

**First Run:** Displays a friendly message with coffee support link (only once per project)

**Memory Management:**
- Tracks message and tool call counts
- Warns at 50 (early) and 70 (critical) memory pressure scores
- Prepares handover automatically before hitting limits

**Information Routing:**
- Project Memory: Current task, active files, key decisions (≤500 words)
- Knowledge Base: Complete history in YAML (unlimited)
- Filesystem: Large summaries and archives
- Project Instructions: Source of truth updates

**Conflict Detection:**
- Monitors instruction vs practice misalignment
- Suggests specific resolutions
- Tracks conflict history

See the [complete documentation](work-in-progress/conversation-continuity/) for detailed usage instructions.

---

**Last Updated:** October 30, 2025
