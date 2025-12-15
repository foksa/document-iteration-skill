---
title: "Installation"
layout: default
---

# Installation

Install the Document Iteration Skill to enable collaborative workflow syntax in Claude.

## Quick Install (Project-Level)

Run this command in your project root:

### macOS / Linux

```bash
mkdir -p .claude/skills/document-iteration-skill && curl -sL https://raw.githubusercontent.com/foksa/document-iteration-skill/main/SKILL.md -o .claude/skills/document-iteration-skill/SKILL.md
```

### Windows (PowerShell)

```powershell
New-Item -ItemType Directory -Force -Path .claude\skills\document-iteration-skill | Out-Null; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/foksa/document-iteration-skill/main/SKILL.md" -OutFile ".claude\skills\document-iteration-skill\SKILL.md"
```

### Windows (Command Prompt)

```cmd
mkdir .claude\skills\document-iteration-skill 2>nul & curl -sL https://raw.githubusercontent.com/foksa/document-iteration-skill/main/SKILL.md -o .claude\skills\document-iteration-skill\SKILL.md
```

## What This Does

1. Creates the `.claude/skills/document-iteration-skill/` directory in your project if it doesn't exist
2. Downloads `SKILL.md` from GitHub
3. Saves it in your project's skills folder

## Verify Installation

### macOS / Linux

```bash
head -20 .claude/skills/document-iteration-skill/SKILL.md
```

### Windows (PowerShell)

```powershell
Get-Content .claude\skills\document-iteration-skill\SKILL.md -Head 20
```

You should see the skill's frontmatter:

```yaml
---
name: collaborative-workflow
description: How to work with collaborative workflow syntax...
```

## Update

To update to the latest version, run the same install command again - it will overwrite the existing file.

## Uninstall

### macOS / Linux

```bash
rm -rf .claude/skills/document-iteration-skill
```

### Windows

```powershell
Remove-Item -Recurse .claude\skills\document-iteration-skill
```

## Global Installation (Alternative)

If you want the skill available across all projects:

### macOS / Linux

```bash
mkdir -p ~/.claude/skills/document-iteration-skill && curl -sL https://raw.githubusercontent.com/foksa/document-iteration-skill/main/SKILL.md -o ~/.claude/skills/document-iteration-skill/SKILL.md
```

### Windows (PowerShell)

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\document-iteration-skill" | Out-Null; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/foksa/document-iteration-skill/main/SKILL.md" -OutFile "$env:USERPROFILE\.claude\skills\document-iteration-skill\SKILL.md"
```

## Next Steps

After installation, start using the syntax in any markdown file:

1. Add `%% your comment %%` to provide feedback
2. Mark text with `==highlighted text(TOKEN)==`
3. Ask Claude to update the document

See [Examples](../examples.md) for more usage patterns.