---
title: Install
---

# Install

[Overview](index.md) · **Install** · [Syntax](syntax.md) · [Editor setup](editors.md)

The skill is the `document-iteration-skill/` folder in the repo. Installing it means putting that folder where Claude looks for skills.

## Claude Code

For one project:

```bash
git clone --depth 1 https://github.com/foksa/document-iteration-skill.git /tmp/dis
mkdir -p .claude/skills
cp -r /tmp/dis/document-iteration-skill .claude/skills/
rm -rf /tmp/dis
```

For all your projects, copy the folder to `~/.claude/skills/` instead.

Or give Claude Code this instruction: *"Install the skill from github.com/foksa/document-iteration-skill into .claude/skills/"*.

After that, just ask:

```
> respond to the comments in docs/plan.md
> review docs/spec.md and add your feedback
> draft a proposal for dark mode in docs/dark-mode.md
> clean up docs/plan.md
> set up VSCode highlighting for iteration markers
```

## Claude.ai

1. Download [`document-iteration-skill.zip`](https://github.com/foksa/document-iteration-skill/releases/download/starter-kit/document-iteration-skill.zip).
2. Upload it as a custom skill in Settings → Skills.

If your plan doesn't support custom skills, paste the contents of `SKILL.md` into a Project's instructions.

In Claude.ai you paste the document into the chat (or attach it), and Claude returns the updated version with its responses included.

## Updating

Delete the installed `document-iteration-skill/` folder and install again.

## If Claude replies in chat instead of in the document

Ask it to "follow the document iteration skill" or to "respond in the document". If this happens often, add a line to your project's `CLAUDE.md`: *"Documents in docs/ use the document iteration skill."*
