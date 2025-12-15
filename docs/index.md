---
title: "Index"
layout: default
---

# Document Iteration Skill

Welcome to the documentation for the Document Iteration Skill - a structured markdown syntax for iterating on documents with Claude AI.

## Quick Links

- [Installation](getting-started/installation.md) - How to install the skill (Claude Code)
- [Using with claude.ai](getting-started/claude-ai.md) - Setup for the web interface
- [Your First Iteration](getting-started/first-iteration.md) - Step-by-step walkthrough
- [SKILL](skill.md) - The complete skill file
- [Examples](examples.md) - See the syntax in action
- [FAQ](reference/faq.md) - Common questions answered
- [Contributing](meta/contributing.md) - How to contribute

### Syntax Reference
- [Syntax Overview](syntax/index.md) - All marker types
- [Comments](syntax/comments.md) - Deep dive on `%% %%` syntax
- [Highlights](syntax/highlights.md) - Deep dive on `==text(TOKEN)==`
- [Tokens](syntax/tokens.md) - Token naming and usage
- [Cleanup](syntax/cleanup.md) - Removing markers when done

### Skill Behavior
- [Mandatory Rules](skill/mandatory-rules.md) - Rules Claude must follow
- [How Claude Responds](skill/responses.md) - Response format and placement
- [Customization](skill/customization.md) - Override rules in .claude.md

### Workflows
- [Workflows Overview](workflows/index.md) - Integration and automation
- [Team Collaboration](workflows/team-collaboration.md) - Multi-person patterns
- [Auto-Cleanup](workflows/auto-cleanup/index.md) - Prevent markers in commits
- [Editor Integration](editor-integration/index.md) - Visual marker highlighting

### Reference
- [Best Practices](reference/best-practices.md) - Tips for effective iteration

### Meta
- [Obsidian Workflow](meta/obsidian-workflow.md) - How this documentation system works

## What is this?

This skill teaches Claude a feedback syntax so you can:

- Add `%% comments %%` directly in documents
- Mark specific text with `==highlights(TOKEN)==`
- Get Claude's responses inline with `%%>answers <%%`
- Track everything in git

## Getting Started

1. Add `SKILL.md` to your Claude project
2. Create a markdown document
3. Add feedback using the syntax
4. Ask Claude to update it

That's it! Claude will read your feedback and respond inline.