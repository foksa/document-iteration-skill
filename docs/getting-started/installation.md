---
---

# Installation

Install the Document Iteration Skill to enable collaborative workflow syntax in Claude.

## Quick Install (Project-Level)

Run this command in your project root:

### macOS / Linux

````bash
git clone --depth 1 https://github.com/foksa/document-iteration-skill.git /tmp/dis-temp && mkdir -p .claude/skills && cp -r /tmp/dis-temp/document-iteration-skill .claude/skills/ && rm -rf /tmp/dis-temp
````

### Windows (PowerShell)

````powershell
git clone --depth 1 https://github.com/foksa/document-iteration-skill.git $env:TEMP\dis-temp; New-Item -ItemType Directory -Force -Path .claude\skills | Out-Null; Copy-Item -Recurse $env:TEMP\dis-temp\document-iteration-skill .claude\skills\; Remove-Item -Recurse -Force $env:TEMP\dis-temp
````

## What This Does

1. Clones the skill repository to a temp folder
1. Copies the `document-iteration-skill/` skill folder to `.claude/skills/`
1. Cleans up the temp folder
1. Gives you all skill files:
   * `SKILL.md` - Core skill instructions
   * `references/` - Detailed syntax guide, examples, cleanup docs
   * `scripts/cleanup.py` - Cleanup script for removing markers
   * `assets/template.md` - Starter document template

## Minimal Install (SKILL.md Only)

If you only want the core skill file (no references or scripts):

### macOS / Linux

````bash
mkdir -p .claude/skills/document-iteration-skill && curl -sL https://raw.githubusercontent.com/foksa/document-iteration-skill/main/document-iteration-skill/SKILL.md -o .claude/skills/document-iteration-skill/SKILL.md
````

### Windows (PowerShell)

````powershell
New-Item -ItemType Directory -Force -Path .claude\skills\document-iteration-skill | Out-Null; Invoke-WebRequest -Uri "https://raw.githubusercontent.com/foksa/document-iteration-skill/main/document-iteration-skill/SKILL.md" -OutFile ".claude\skills\document-iteration-skill\SKILL.md"
````

**Note:** With minimal install, Claude won't have access to `references/` for detailed examples. The core syntax still works.

## Verify Installation

### macOS / Linux

````bash
ls -la .claude/skills/document-iteration-skill/
````

You should see:

````
SKILL.md
references/
scripts/
assets/
````

### Windows (PowerShell)

````powershell
Get-ChildItem .claude\skills\document-iteration-skill\
````

## Update

To update to the latest version:

### macOS / Linux

````bash
rm -rf .claude/skills/document-iteration-skill && git clone --depth 1 https://github.com/foksa/document-iteration-skill.git /tmp/dis-temp && cp -r /tmp/dis-temp/document-iteration-skill .claude/skills/ && rm -rf /tmp/dis-temp
````

### Windows (PowerShell)

````powershell
Remove-Item -Recurse -Force .claude\skills\document-iteration-skill; git clone --depth 1 https://github.com/foksa/document-iteration-skill.git $env:TEMP\dis-temp; Copy-Item -Recurse $env:TEMP\dis-temp\document-iteration-skill .claude\skills\; Remove-Item -Recurse -Force $env:TEMP\dis-temp
````

## Uninstall

### macOS / Linux

````bash
rm -rf .claude/skills/document-iteration-skill
````

### Windows (PowerShell)

````powershell
Remove-Item -Recurse -Force .claude\skills\document-iteration-skill
````

## Global Installation (Alternative)

If you want the skill available across all projects:

### macOS / Linux

````bash
git clone --depth 1 https://github.com/foksa/document-iteration-skill.git /tmp/dis-temp && mkdir -p ~/.claude/skills && cp -r /tmp/dis-temp/document-iteration-skill ~/.claude/skills/ && rm -rf /tmp/dis-temp
````

### Windows (PowerShell)

````powershell
git clone --depth 1 https://github.com/foksa/document-iteration-skill.git $env:TEMP\dis-temp; New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null; Copy-Item -Recurse $env:TEMP\dis-temp\document-iteration-skill "$env:USERPROFILE\.claude\skills\"; Remove-Item -Recurse -Force $env:TEMP\dis-temp
````

## Using with Claude.ai (Web)

For Claude.ai Projects (no CLI):

1. Download the repo as ZIP from [GitHub](https://github.com/foksa/document-iteration-skill)
1. Extract and add `SKILL.md` to your Claude Project files
1. Optionally add files from `references/` for detailed examples

See [Using with Claude.ai](claude-ai.md) for detailed setup.

## Next Steps

After installation, start using the syntax in any markdown file:

1. Add `%% your comment %%` to provide feedback
1. Mark text with `==highlighted text(TOKEN)==`
1. Ask Claude to update the document

See *Examples* for more usage patterns.
