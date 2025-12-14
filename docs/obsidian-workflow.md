---
title: "Obsidian Workflow"
layout: default
---

# Docs Workflow

How the documentation system works - from Obsidian to GitHub Pages.

## Overview

```
document-iteration-skill/           (PUBLIC)
├── SKILL.md
├── README.md
├── docs/                           ← Auto-updated by Action (gitignored locally)
├── docs-source/                    ← Submodule (for local editing)
│   └── (see below)
└── .gitignore

document-iteration-skill-docs/      (PRIVATE repo, also as submodule above)
├── obsidian/                       ← Edit here
├── docs/                           ← Converted output
├── scripts/convert-obsidian.py
└── .github/workflows/publish-docs.yml
```

### Repository Organization

There are **two repositories** working together:

**1. Main Repository (PUBLIC):** `foksa/document-iteration-skill`
- This is what users see and clone
- Contains the skill file (`SKILL.md`), README, and published docs
- The `docs/` folder here is **auto-generated** - never edit it directly
- Has a `docs-source/` submodule pointing to the private repo (for maintainer convenience)

**2. Docs Repository (PRIVATE):** `foksa/document-iteration-skill-docs`
- Source of truth for documentation
- Contains your Obsidian vault (`obsidian/`) where you actually write
- GitHub Action converts Obsidian → Jekyll and pushes to main repo's `docs/`
- Only you (the maintainer) need access to this

### Why Two Repos?

| Concern | Solution |
|---------|----------|
| Keep Obsidian files private | Private docs repo |
| Public docs on GitHub Pages | Main repo's `docs/` folder |
| Edit locally in one place | Submodule links them |
| No manual sync needed | GitHub Action automates it |

### The Submodule

The `docs-source/` folder in the main repo is a **git submodule** - a pointer to the private docs repo. This lets you:

- Clone main repo and get both with `git clone --recurse-submodules`
- Edit obsidian files at `docs-source/obsidian/`
- Commit/push from within `docs-source/` to trigger the Action

The submodule is optional for users - they don't need it. It's just for your convenience as maintainer.

## Workflow

1. **Edit** markdown in `obsidian/` folder (open as Obsidian vault)
2. **Push** to private docs repo
3. **Action** converts Obsidian → Jekyll and pushes to main repo
4. **GitHub Pages** publishes from main repo's `docs/`

## What Gets Converted

| Obsidian | Jekyll/GitHub Pages |
|----------|---------------------|
| `[Page Name](page-name.md)` | `[Page Name](page-name.md)` |
| `[Display](link.md)` | `[Display](link.md)` |
| `*See [Embedded Note](embedded-note.md)*` | `*See [Note](note.md)*` |
| `![image](assets/image.png)` | `![image](assets/image.png)` |

## Scripts

### Conversion Script

Located at `scripts/convert-obsidian.py`

**Full script:** [convert-obsidian.py](https://gist.github.com/foksa/0abc17cdc51dd5482033f55c17f6c09f)

**What it does:**
- Converts `[wikilinks](wikilinks.md)` → `[text](file.md)`
- Converts `[display](link.md)` → `[display](link.md)`
- Converts `*See [embeds](embeds.md)*` → link references
- Copies images to `assets/` folder
- Adds Jekyll frontmatter if missing
- Slugifies filenames for URLs

### GitHub Action

Located at `.github/workflows/publish-docs.yml`:

```yaml
name: Publish Docs

on:
  push:
    branches: [main]
    paths:
      - 'obsidian/**'
      - 'scripts/convert-obsidian.py'
  workflow_dispatch:

jobs:
  convert-and-publish:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout docs repo
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Convert Obsidian to Jekyll
        run: python scripts/convert-obsidian.py

      - name: Checkout main repo
        uses: actions/checkout@v4
        with:
          repository: foksa/document-iteration-skill
          path: main-repo
          ssh-key: ${{ secrets.DEPLOY_KEY }}

      - name: Copy docs to main repo
        run: |
          rm -rf main-repo/docs
          cp -r docs main-repo/docs

      - name: Commit and push to main repo
        run: |
          cd main-repo
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add -f docs/
          git diff --staged --quiet || git commit -m "Update docs from obsidian vault"
          git push
```

## Setup Details

### Deploy Key

The Action uses an SSH deploy key to push from private docs repo to public main repo:

1. **Public key** → Added to main repo as Deploy Key (with write access)
2. **Private key** → Added to docs repo as Secret `DEPLOY_KEY`

### Main Repo .gitignore

The `docs/` folder is gitignored in the main repo so you don't accidentally edit it locally:

```
# Docs (auto-generated from obsidian vault, don't edit locally)
docs/
```

## Local Development

To preview docs locally:

```bash
cd document-iteration-skill-docs
python3 scripts/convert-obsidian.py
cd docs
# Open index.md or use a markdown previewer
```

## Adding New Pages

1. Create new `.md` file in `obsidian/`
2. Link to other pages using Obsidian's internal link syntax
3. Commit and push
4. Action converts and publishes automatically

## VSCode UI Optimization

When editing via the submodule in VSCode, you can hide unnecessary files to keep the sidebar clean.

Add to `.vscode/settings.json` in the main repo:

```json
{
  "files.exclude": {
    "docs-source/.github": true,
    "docs-source/docs": true,
    "docs-source/scripts": true,
    "docs-source/.gitignore": true,
    "docs-source/README.md": true
  }
}
```

This hides the submodule's infrastructure files, showing only the `docs-source/obsidian/` folder you actually edit. The hidden files remain in git - they're just not visible in the file explorer.