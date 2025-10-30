# Loading and Publishing Skills

**Version:** 1.0.0  
**Author:** Colin Bitterfield  
**Email:** colin@bitterfield.com  
**Date Created:** 2025-10-30  
**Date Updated:** 2025-10-30

---

## Quick Reference

**Packaged Skill Location:** `/Users/colin/Projects/claude-skill-passing/skills/conversation-continuity.skill`

**To Package a Skill:**
```bash
cd /Users/colin/Projects/claude-skill-passing
python3 scripts/package_skill.py work-in-progress/SKILL-NAME skills
```

**To Load in Claude:** Upload the .skill file through Claude's UI (Settings → Skills)

---

## Loading Skills in Claude

### Method 1: Upload Through UI (Recommended)

1. **Locate your packaged skill file:**
   - File: `conversation-continuity.skill`
   - Location: `/Users/colin/Projects/claude-skill-passing/skills/`

2. **In Claude's interface:**
   - Open Settings (gear icon)
   - Navigate to Skills section
   - Click "Upload Skill" or "Add Skill"
   - Select the `conversation-continuity.skill` file
   - Confirm upload

3. **Verify skill loaded:**
   - Skill should appear in your skills list
   - You can enable/disable it as needed
   - Check skill description to ensure it loaded correctly

### Method 2: Direct File Access (If Available)

If you have direct access to Claude's skill directories:

```bash
# Copy skill to user skills directory
cp /Users/colin/Projects/claude-skill-passing/skills/conversation-continuity.skill /mnt/skills/user/
```

**Note:** The `/mnt/skills/user` directory is typically managed through the UI, not direct filesystem access.

---

## Publishing Skills

### For Personal Use

**Already Done!** Your packaged skill at:
```
/Users/colin/Projects/claude-skill-passing/skills/conversation-continuity.skill
```

You can:
- Upload to different Claude instances you use
- Back up to cloud storage
- Version control the .skill file
- Share with team members directly

### For Public Sharing

#### Option 1: GitHub Repository

**Step 1: Create Repository on GitHub**

Via GitHub web interface:

1. Go to: https://github.com/Temple-of-Epiphany
2. Click "New repository" (or go to https://github.com/new)
3. Repository name: `claude-skills`
4. Description: "Custom Claude AI skills for conversation continuity and productivity"
5. Visibility: Public (so others can download)
6. Initialize: Do NOT check "Add README" (we have one)
7. Click "Create repository"

**Step 2: Initialize Local Git and Push**

```bash
# Navigate to project
cd /Users/colin/Projects/claude-skill-passing

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: conversation-continuity skill v1.0.0

- Complete conversation continuity skill
- Hybrid storage (memory + YAML knowledge base)
- Memory pressure tracking and handover preparation
- Conflict detection and resolution
- Automated capability checking
- First-run coffee support message"

# Add remote repository
git remote add origin https://github.com/Temple-of-Epiphany/claude-skills.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

**Step 3: Authentication**

When prompted for credentials:
- **Username:** `cbitterfield`
- **Password:** Use a Personal Access Token (not your GitHub password)

**To create a Personal Access Token:**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name: "Claude Skills Repo"
4. Scopes: Select `repo` (all repo permissions)
5. Click "Generate token"
6. Copy token immediately (you won't see it again)
7. Use token as password when pushing

**Step 4: Create Repository README**

Create a `README.md` in the project root:

```markdown
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

## Support

If you find these skills helpful, consider buying me a coffee:  
☕ https://buymeacoffee.com/colin.bitterfield

## License

MIT License - See individual skills for details

## Author

Colin Bitterfield  
colin@bitterfield.com
```

Then add and push:

```bash
git add README.md
git commit -m "Add repository README"
git push
```

**Step 5: Configure Repository Settings**

On GitHub:
1. Go to repository settings
2. Add topics: `claude-ai`, `claude-skills`, `ai-tools`, `productivity`
3. Add website: `https://buymeacoffee.com/colin.bitterfield`
4. Update description if needed

**Step 6: Share the Repository**

- Share URL: https://github.com/Temple-of-Epiphany/claude-skills
- Users can download .skill file directly
- Upload to their Claude instance
- Star/watch for updates

#### Option 2: Direct Distribution

1. **Host the .skill file:**
   - Personal website
   - Cloud storage (Dropbox, Google Drive) with public link
   - File sharing service

2. **Provide instructions:**
   ```markdown
   ## Installation
   
   1. Download: [conversation-continuity.skill](DOWNLOAD_LINK)
   2. In Claude, go to Settings → Skills
   3. Click "Upload Skill"
   4. Select the downloaded .skill file
   
   ## Support
   
   If you find this skill helpful, consider buying me a coffee:
   https://buymeacoffee.com/colin.bitterfield
   ```

#### Option 3: Anthropic Skill Registry (Future)

If Anthropic creates an official skill registry:
- Submit through official channels
- Follow their submission guidelines
- Include metadata and documentation
- Wait for approval process

---

## Packaging Workflow

### Initial Packaging

```bash
# Navigate to project
cd /Users/colin/Projects/claude-skill-passing

# Package skill from work-in-progress
python3 scripts/package_skill.py work-in-progress/conversation-continuity skills

# Output: skills/conversation-continuity.skill
```

### Validation Before Packaging

The packaging script automatically validates:
- SKILL.md exists
- YAML frontmatter is valid
- Required fields present (name, description)
- Naming conventions followed
- No angle brackets in description
- Field length limits respected

If validation fails, fix errors before packaging.

### Manual Validation

```bash
cd /Users/colin/Projects/claude-skill-passing
python3 scripts/quick_validate.py work-in-progress/conversation-continuity
```

---

## Updating Skills

### Version Update Workflow

1. **Make changes to skill:**
   ```bash
   # Edit files in work-in-progress/conversation-continuity/
   # Update version numbers in file headers
   # Update SKILL.md if needed
   ```

2. **Update version in SKILL.md:**
   - No version field in frontmatter (internal versioning)
   - Document changes in reference files
   - Update examples if needed

3. **Re-package skill:**
   ```bash
   python3 scripts/package_skill.py work-in-progress/conversation-continuity skills
   # This overwrites existing .skill file
   ```

4. **Distribute update:**
   - Upload new .skill file to Claude
   - Update GitHub repository
   - Notify users of update
   - Document changes in release notes

### Moving to Production

When skill is tested and ready:

```bash
# Move from work-in-progress to completed
cd /Users/colin/Projects/claude-skill-passing
mv work-in-progress/conversation-continuity skills/source/conversation-continuity

# Package from new location
python3 scripts/package_skill.py skills/source/conversation-continuity skills
```

---

## Skill File Format

### What's in a .skill File

A .skill file is a ZIP archive with .skill extension containing:

```
conversation-continuity/
├── SKILL.md                 # Main skill documentation
├── references/              # Reference documentation
│   ├── handover-template.md
│   └── knowledge-base-schema.yaml
├── scripts/                 # Helper scripts
│   └── conversation_helper.py
└── examples/                # Example files
    ├── example-handover.md
    └── example-knowledge-base.yaml
```

### Inspecting a .skill File

```bash
# View contents without extracting
unzip -l /Users/colin/Projects/claude-skill-passing/skills/conversation-continuity.skill

# Extract to inspect
cd /tmp
unzip /Users/colin/Projects/claude-skill-passing/skills/conversation-continuity.skill
```

---

## Sharing Best Practices

### Documentation

Include with your skill distribution:
- Clear description of what the skill does
- Installation instructions
- Usage examples
- Limitations and requirements
- Support information (buymeacoffee link)
- License information

### Licensing

Add license to SKILL.md frontmatter:
```yaml
license: MIT
```

Or create LICENSE.txt in skill directory before packaging.

### Version Management

Use semantic versioning:
- Document in file headers
- Track in git tags
- Mention in distribution notes

### Support

Provide ways for users to:
- Report issues
- Request features
- Get help
- Support your work (buymeacoffee)

---

## Troubleshooting

### Skill Won't Package

**Error: "Validation failed"**
- Check SKILL.md frontmatter format
- Ensure name is hyphen-case
- Verify description length < 1024 chars
- Remove angle brackets from description

**Error: "Skill folder not found"**
- Verify path is correct
- Use absolute or relative path
- Check directory exists

### Skill Won't Load in Claude

**Check:**
- File extension is .skill (not .zip)
- File is not corrupted
- SKILL.md has valid frontmatter
- No files are too large (check limits)

**Retry:**
- Re-package skill
- Clear Claude cache
- Try different browser/client

### Packaging Script Issues

**Import error: "No module named 'yaml'"**
```bash
pip3 install pyyaml --break-system-packages
```

**Permission denied:**
```bash
chmod +x scripts/package_skill.py
```

---

## Current Project Status

### Packaged Skills

Located in `/Users/colin/Projects/claude-skill-passing/skills/`:

| Skill | Version | Status | File |
|-------|---------|--------|------|
| conversation-continuity | 1.0.0 | ✅ Ready | conversation-continuity.skill |

### In Development

Located in `/Users/colin/Projects/claude-skill-passing/work-in-progress/`:

| Skill | Status | Next Step |
|-------|--------|-----------|
| (none) | - | - |

---

## Next Steps

1. **Upload skill to Claude:**
   - Go to Claude Settings → Skills
   - Upload conversation-continuity.skill
   - Enable the skill
   - Test with new conversation

2. **Test the skill:**
   - Start conversation
   - Verify automatic capability check
   - Check first-run message displays
   - Test memory tracking
   - Prepare a handover

3. **Share publicly (optional):**
   - Create GitHub repository
   - Add README and documentation
   - Share link to .skill file
   - Promote on relevant platforms

4. **Maintain and update:**
   - Collect user feedback
   - Make improvements
   - Re-package and distribute updates
   - Track versions

---

**End of Loading and Publishing Guide v1.0.0**
