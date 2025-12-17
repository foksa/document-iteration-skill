# Document Iteration Skill - Project Guide

## Overview

This repo contains the Document Iteration Skill - a structured markdown syntax for iterating on documents with Claude.

## Repository Structure

```
document-iteration-skill/    # The skill itself (SKILL.md + references)
editor-configs/              # VSCode, Obsidian highlighting configs
prompts/                     # Setup prompts for new projects
examples/                    # Example documents showing the workflow
docs-source/                 # Documentation (git submodule, syncs to GitHub Pages)
```

## Key Conventions

### Iteration Markers

When working on markdown files in this repo, use the iteration syntax:

- `%% user comment %%` - User feedback (muted gold)
- `•%%> AI response <%%•` - AI responses (teal)
- `==text(TOKEN)==` + `%%(TOKEN) comment %%` - Precise references

### Documentation Workflow

- `docs-source/` is an Obsidian vault (git submodule)
- Edits to docs happen there, then sync to GitHub Pages
- `docs-source/wip/` contains drafts and proposals

### Editor Configs

- `editor-configs/vscode/` - TODO Highlight settings for VSCode
- `editor-configs/obsidian/` - Regex Mark plugin + CSS for Obsidian
- Both use same colors: gold (`#968748`) for user, teal (`#3C8C8C`) for AI

## Working on This Project

1. **Editing the skill:** Modify `document-iteration-skill/SKILL.md`
2. **Adding examples:** Put in `examples/` folder
3. **Documentation:** Edit in `docs-source/`, commit submodule separately
4. **New editor support:** Add to `editor-configs/<editor>/`

## Useful Commands

```bash
# Update docs submodule
cd docs-source && git pull origin main && cd ..

# Test skill locally
cp -r document-iteration-skill ~/.claude/skills/

# Package starter kit (auto via GitHub Action on push)
zip -r starter-kit.zip document-iteration-skill editor-configs
```

## GitHub Actions

- `package-starter-kit.yml` - Auto-packages skill + configs on push to main
- Releases at: `releases/download/starter-kit/starter-kit.zip`