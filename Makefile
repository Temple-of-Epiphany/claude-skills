# Makefile for Claude Skill Development
# Author: Colin Bitterfield
# Email: colin@bitterfield.com
# Date Created: 2025-10-30

# Configuration
PYTHON := python3
SCRIPTS_DIR := scripts
SKILLS_SOURCE_DIR := skills/source
SKILLS_OUTPUT_DIR := skills
WIP_DIR := work-in-progress

# Colors for output
COLOR_RESET := \033[0m
COLOR_BOLD := \033[1m
COLOR_GREEN := \033[32m
COLOR_YELLOW := \033[33m
COLOR_BLUE := \033[34m

# Find all skills in source directory
SKILLS := $(notdir $(wildcard $(SKILLS_SOURCE_DIR)/*))
SKILL_FILES := $(addprefix $(SKILLS_OUTPUT_DIR)/, $(addsuffix .skill, $(SKILLS)))

.PHONY: help all package validate clean install test git-status git-push

# Default target
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "$(COLOR_BOLD)Claude Skill Development - Makefile$(COLOR_RESET)"
	@echo ""
	@echo "$(COLOR_BLUE)Available targets:$(COLOR_RESET)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(COLOR_GREEN)%-20s$(COLOR_RESET) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(COLOR_BLUE)Specific skills:$(COLOR_RESET)"
	@for skill in $(SKILLS); do \
		echo "  $(COLOR_GREEN)$$skill$(COLOR_RESET)                Package $$skill"; \
	done

all: package ## Build all skills

package: $(SKILL_FILES) ## Package all skills in source directory

$(SKILLS_OUTPUT_DIR)/%.skill: $(SKILLS_SOURCE_DIR)/%
	@echo "$(COLOR_YELLOW)📦 Packaging $*...$(COLOR_RESET)"
	@$(PYTHON) $(SCRIPTS_DIR)/package_skill.py $(SKILLS_SOURCE_DIR)/$* $(SKILLS_OUTPUT_DIR)
	@echo "$(COLOR_GREEN)✅ $*.skill packaged successfully$(COLOR_RESET)"
	@echo ""

# Individual skill targets
conversation-continuity: $(SKILLS_OUTPUT_DIR)/conversation-continuity.skill ## Package conversation-continuity skill

validate: ## Validate all skills in source directory
	@echo "$(COLOR_YELLOW)🔍 Validating all skills...$(COLOR_RESET)"
	@for skill in $(SKILLS); do \
		echo "Validating $$skill..."; \
		$(PYTHON) $(SCRIPTS_DIR)/quick_validate.py $(SKILLS_SOURCE_DIR)/$$skill || exit 1; \
	done
	@echo "$(COLOR_GREEN)✅ All skills validated$(COLOR_RESET)"

validate-%: ## Validate specific skill (e.g., make validate-conversation-continuity)
	@echo "$(COLOR_YELLOW)🔍 Validating $*...$(COLOR_RESET)"
	@$(PYTHON) $(SCRIPTS_DIR)/quick_validate.py $(SKILLS_SOURCE_DIR)/$*
	@echo "$(COLOR_GREEN)✅ $* validated$(COLOR_RESET)"

clean: ## Remove all packaged .skill files
	@echo "$(COLOR_YELLOW)🧹 Cleaning packaged skills...$(COLOR_RESET)"
	@rm -f $(SKILLS_OUTPUT_DIR)/*.skill
	@rm -rf $(SCRIPTS_DIR)/__pycache__
	@find . -name "*.pyc" -delete
	@find . -name ".DS_Store" -delete
	@echo "$(COLOR_GREEN)✅ Cleaned$(COLOR_RESET)"

clean-%: ## Remove specific packaged skill (e.g., make clean-conversation-continuity)
	@echo "$(COLOR_YELLOW)🧹 Cleaning $*.skill...$(COLOR_RESET)"
	@rm -f $(SKILLS_OUTPUT_DIR)/$*.skill
	@echo "$(COLOR_GREEN)✅ $*.skill removed$(COLOR_RESET)"

install: ## Install required Python dependencies
	@echo "$(COLOR_YELLOW)📥 Installing dependencies...$(COLOR_RESET)"
	@pip3 install pyyaml --break-system-packages
	@echo "$(COLOR_GREEN)✅ Dependencies installed$(COLOR_RESET)"

test: validate ## Run tests (currently just validation)
	@echo "$(COLOR_GREEN)✅ All tests passed$(COLOR_RESET)"

list: ## List all available skills
	@echo "$(COLOR_BOLD)Skills in source directory:$(COLOR_RESET)"
	@for skill in $(SKILLS); do \
		echo "  • $$skill"; \
	done
	@echo ""
	@echo "$(COLOR_BOLD)Packaged skills:$(COLOR_RESET)"
	@ls -1 $(SKILLS_OUTPUT_DIR)/*.skill 2>/dev/null | xargs -n1 basename || echo "  (none)"

list-wip: ## List work-in-progress skills
	@echo "$(COLOR_BOLD)Work-in-progress skills:$(COLOR_RESET)"
	@ls -1 $(WIP_DIR) 2>/dev/null || echo "  (none)"

info: ## Show project information
	@echo "$(COLOR_BOLD)Claude Skill Development Project$(COLOR_RESET)"
	@echo ""
	@echo "Author:  Colin Bitterfield"
	@echo "Email:   colin@bitterfield.com"
	@echo "GitHub:  https://github.com/Temple-of-Epiphany/claude-skills"
	@echo "Support: https://buymeacoffee.com/colin.bitterfield"
	@echo ""
	@echo "Python:  $$($(PYTHON) --version)"
	@echo "Skills:  $(words $(SKILLS)) in source"
	@echo ""

git-status: ## Show git status
	@git status

git-add: package ## Package skills and stage all changes
	@echo "$(COLOR_YELLOW)📝 Staging changes...$(COLOR_RESET)"
	@git add .
	@echo "$(COLOR_GREEN)✅ Changes staged$(COLOR_RESET)"
	@git status --short

git-commit: ## Commit staged changes (requires MESSAGE variable)
ifndef MESSAGE
	@echo "$(COLOR_YELLOW)⚠️  Please provide a commit message:$(COLOR_RESET)"
	@echo "   make git-commit MESSAGE=\"Your commit message\""
else
	@git commit -m "$(MESSAGE)"
	@echo "$(COLOR_GREEN)✅ Changes committed$(COLOR_RESET)"
endif

git-push: ## Push to remote repository
	@echo "$(COLOR_YELLOW)⬆️  Pushing to remote...$(COLOR_RESET)"
	@git push origin main
	@echo "$(COLOR_GREEN)✅ Pushed to GitHub$(COLOR_RESET)"

release: all validate git-add ## Full release workflow (package, validate, stage)
	@echo ""
	@echo "$(COLOR_BOLD)$(COLOR_GREEN)✅ Ready to commit and push!$(COLOR_RESET)"
	@echo ""
	@echo "Next steps:"
	@echo "  1. make git-commit MESSAGE=\"Your message\""
	@echo "  2. make git-push"
	@echo ""

watch: ## Watch for changes and auto-package (requires fswatch)
	@echo "$(COLOR_YELLOW)👀 Watching for changes...$(COLOR_RESET)"
	@echo "Press Ctrl+C to stop"
	@fswatch -o $(SKILLS_SOURCE_DIR) | xargs -n1 -I{} make package

# Development helpers
new-skill: ## Create new skill from template (requires NAME variable)
ifndef NAME
	@echo "$(COLOR_YELLOW)⚠️  Please provide a skill name:$(COLOR_RESET)"
	@echo "   make new-skill NAME=my-new-skill"
else
	@echo "$(COLOR_YELLOW)📝 Creating new skill: $(NAME)...$(COLOR_RESET)"
	@mkdir -p $(WIP_DIR)/$(NAME)/references
	@mkdir -p $(WIP_DIR)/$(NAME)/scripts
	@mkdir -p $(WIP_DIR)/$(NAME)/examples
	@echo "---" > $(WIP_DIR)/$(NAME)/SKILL.md
	@echo "name: $(NAME)" >> $(WIP_DIR)/$(NAME)/SKILL.md
	@echo "description: TODO - Add description" >> $(WIP_DIR)/$(NAME)/SKILL.md
	@echo "---" >> $(WIP_DIR)/$(NAME)/SKILL.md
	@echo "" >> $(WIP_DIR)/$(NAME)/SKILL.md
	@echo "# $(NAME)" >> $(WIP_DIR)/$(NAME)/SKILL.md
	@echo "" >> $(WIP_DIR)/$(NAME)/SKILL.md
	@echo "TODO: Add skill documentation" >> $(WIP_DIR)/$(NAME)/SKILL.md
	@echo "$(COLOR_GREEN)✅ New skill created at $(WIP_DIR)/$(NAME)$(COLOR_RESET)"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Edit $(WIP_DIR)/$(NAME)/SKILL.md"
	@echo "  2. Add references, scripts, examples as needed"
	@echo "  3. When ready: make promote-skill NAME=$(NAME)"
endif

promote-skill: ## Move skill from WIP to source (requires NAME variable)
ifndef NAME
	@echo "$(COLOR_YELLOW)⚠️  Please provide a skill name:$(COLOR_RESET)"
	@echo "   make promote-skill NAME=my-skill"
else
	@echo "$(COLOR_YELLOW)📦 Promoting $(NAME) to source...$(COLOR_RESET)"
	@mv $(WIP_DIR)/$(NAME) $(SKILLS_SOURCE_DIR)/$(NAME)
	@echo "$(COLOR_GREEN)✅ $(NAME) moved to $(SKILLS_SOURCE_DIR)/$(NAME)$(COLOR_RESET)"
	@echo ""
	@echo "Next step: make $(NAME)"
endif

.PHONY: $(SKILLS)
