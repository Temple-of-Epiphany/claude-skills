# Makefile Usage Guide

**Version:** 1.0.0  
**Author:** Colin Bitterfield  
**Email:** colin@bitterfield.com  
**Date Created:** 2025-10-30

---

## Quick Start

```bash
# Show all available commands
make help

# Package all skills
make all

# Package specific skill
make conversation-continuity

# Validate all skills
make validate

# Full release workflow
make release
```

---

## Common Commands

### Building Skills

```bash
# Package all skills in source directory
make package
# or
make all

# Package specific skill
make conversation-continuity

# Clean and rebuild
make clean all
```

### Validation

```bash
# Validate all skills
make validate

# Validate specific skill
make validate-conversation-continuity
```

### Cleaning

```bash
# Remove all packaged .skill files
make clean

# Remove specific skill package
make clean-conversation-continuity

# Clean everything (packages, cache, .DS_Store)
make clean
```

### Git Operations

```bash
# Show git status
make git-status

# Package and stage all changes
make git-add

# Commit with message
make git-commit MESSAGE="Add new feature"

# Push to GitHub
make git-push

# Complete release workflow
make release
# Then:
make git-commit MESSAGE="Release v2.1.0"
make git-push
```

---

## Development Workflow

### Creating a New Skill

```bash
# Create new skill from template
make new-skill NAME=my-new-skill

# Edit the skill
# work-in-progress/my-new-skill/SKILL.md

# Validate as you work
make validate-my-new-skill  # (won't work until promoted)

# When ready, promote to source
make promote-skill NAME=my-new-skill

# Package the skill
make my-new-skill

# Or package all
make all
```

### Working on Existing Skill

```bash
# Make changes to skills/source/conversation-continuity/

# Validate
make validate-conversation-continuity

# Package
make conversation-continuity

# Test by uploading to Claude
```

### Release Workflow

```bash
# 1. Make your changes to skill source

# 2. Run full release workflow
make release
# This will:
# - Package all skills
# - Validate all skills
# - Stage all changes

# 3. Review changes
make git-status

# 4. Commit
make git-commit MESSAGE="Release v2.1.0: Add new features"

# 5. Push
make git-push
```

---

## All Available Commands

### Building
| Command | Description |
|---------|-------------|
| `make all` | Build all skills |
| `make package` | Package all skills in source directory |
| `make SKILL-NAME` | Package specific skill |

### Validation
| Command | Description |
|---------|-------------|
| `make validate` | Validate all skills |
| `make validate-SKILL-NAME` | Validate specific skill |
| `make test` | Run tests (currently validation) |

### Cleaning
| Command | Description |
|---------|-------------|
| `make clean` | Remove all packaged skills and cache |
| `make clean-SKILL-NAME` | Remove specific packaged skill |

### Information
| Command | Description |
|---------|-------------|
| `make help` | Show help message |
| `make info` | Show project information |
| `make list` | List all available skills |
| `make list-wip` | List work-in-progress skills |

### Development
| Command | Description |
|---------|-------------|
| `make new-skill NAME=...` | Create new skill from template |
| `make promote-skill NAME=...` | Move skill from WIP to source |
| `make install` | Install Python dependencies |
| `make watch` | Watch for changes and auto-package |

### Git
| Command | Description |
|---------|-------------|
| `make git-status` | Show git status |
| `make git-add` | Package and stage changes |
| `make git-commit MESSAGE=...` | Commit with message |
| `make git-push` | Push to GitHub |
| `make release` | Full release workflow |

---

## Examples

### Example 1: Quick Build
```bash
cd /Users/colin/Projects/claude-skill-passing
make conversation-continuity
```

**Output:**
```
📦 Packaging conversation-continuity...
🔍 Validating skill...
✅ Skill is valid!
  Added: conversation-continuity/SKILL.md
  ...
✅ conversation-continuity.skill packaged successfully
```

### Example 2: Create New Skill
```bash
make new-skill NAME=email-templates
# Edit work-in-progress/email-templates/SKILL.md
# Add references, examples, etc.
make promote-skill NAME=email-templates
make email-templates
```

### Example 3: Full Release
```bash
# Make changes to skills/source/conversation-continuity/SKILL.md

# Package, validate, and stage
make release

# Review
git status

# Commit and push
make git-commit MESSAGE="Update documentation"
make git-push
```

### Example 4: Development Cycle
```bash
# Edit skill
vim skills/source/conversation-continuity/SKILL.md

# Validate
make validate-conversation-continuity

# Package
make conversation-continuity

# Upload to Claude and test

# If good, release
make release
make git-commit MESSAGE="Fix memory tracking"
make git-push
```

---

## Makefile Features

### Multi-Skill Support
The Makefile automatically discovers all skills in `skills/source/`:
```bash
make list
# Shows:
#   • conversation-continuity
#   • email-templates
#   • pdf-tools
```

Each skill gets its own target:
```bash
make conversation-continuity
make email-templates
make pdf-tools
```

### Color Output
- 🟢 Green: Success messages
- 🟡 Yellow: Info/warnings
- 🔵 Blue: Headers
- ⚫ Bold: Emphasis

### Smart Dependencies
- `make release` runs: package → validate → git-add
- `make git-add` runs: package first
- `make test` runs: validate

### Error Handling
If validation fails, packaging stops:
```bash
make validate
# If any skill fails validation, make stops
# Fix errors, then try again
```

---

## Advanced Usage

### Watch Mode (Auto-Build)
Requires `fswatch` (install: `brew install fswatch`)

```bash
make watch
# Watches skills/source/ for changes
# Auto-packages when files change
# Press Ctrl+C to stop
```

### Conditional Commands
```bash
# Commit only if MESSAGE provided
make git-commit MESSAGE="Fix bug"

# Create skill only if NAME provided
make new-skill NAME=my-skill
```

### Parallel Building
```bash
# Build multiple skills in parallel
make -j4 conversation-continuity email-templates pdf-tools
```

---

## Troubleshooting

### "No rule to make target"
```bash
# Make sure skill exists in skills/source/
make list

# If not, create it:
make new-skill NAME=my-skill
```

### "Validation failed"
```bash
# Check what's wrong
make validate-SKILL-NAME

# Common issues:
# - Missing name/description in frontmatter
# - Invalid YAML
# - Description too long (>1024 chars)
```

### "Command not found: python3"
```bash
# Check Python installation
which python3

# Or use different Python:
make PYTHON=python3.9 all
```

### Git Push Fails
```bash
# Check authentication
gh auth status

# Or use SSH instead of HTTPS
git remote set-url origin git@github.com:Temple-of-Epiphany/claude-skills.git
```

---

## Customization

### Change Python Version
```bash
make PYTHON=python3.11 all
```

### Change Output Directory
Edit Makefile:
```makefile
SKILLS_OUTPUT_DIR := dist
```

### Add Custom Targets
Add to Makefile:
```makefile
my-custom-target: ## My custom command
	@echo "Running custom command"
	@./my-script.sh
```

---

## Project Structure Support

The Makefile works with this structure:

```
claude-skill-passing/
├── Makefile                 ← This file
├── skills/
│   ├── *.skill             ← Packaged outputs
│   └── source/
│       └── */              ← Skill sources (auto-discovered)
├── work-in-progress/
│   └── */                  ← Skills being developed
├── scripts/
│   ├── package_skill.py    ← Packaging script
│   └── quick_validate.py   ← Validation script
└── docs/                   ← Documentation
```

**Multi-skill ready:** Just add new directories to `skills/source/` and they automatically get their own make targets!

---

**End of Makefile Usage Guide v1.0.0**
