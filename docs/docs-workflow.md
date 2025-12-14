---
title: "Docs Workflow"
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

Located at `scripts/convert-obsidian.py`:

```python
#!/usr/bin/env python3
"""
Convert Obsidian vault to GitHub Pages compatible markdown.

Handles:
- [wikilinks](wikilinks.md) → [text](file.md)
- [display](link.md) → [display](link.md)
- *See [embeds](embeds.md)* → content inlined or linked
- ![image](assets/image.png) → ![image](assets/image.png)
- Adds Jekyll frontmatter if missing
"""

import os
import re
import shutil
from pathlib import Path

OBSIDIAN_DIR = Path("obsidian")
DOCS_DIR = Path("docs")
ASSETS_DIR = DOCS_DIR / "assets"

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def slugify(name: str) -> str:
    """Convert a page name to a URL-friendly slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[-\s]+", "-", slug)
    return slug


def find_file(name: str, files_map: dict[str, Path]) -> Path | None:
    """Find a file by name (case-insensitive, with or without extension)."""
    name_lower = name.lower()
    if name_lower in files_map:
        return files_map[name_lower]
    if f"{name_lower}.md" in files_map:
        return files_map[f"{name_lower}.md"]
    name_no_ext = Path(name_lower).stem
    if f"{name_no_ext}.md" in files_map:
        return files_map[f"{name_no_ext}.md"]
    return None


def build_files_map(source_dir: Path) -> dict[str, Path]:
    """Build a map of lowercase filenames to their paths."""
    files_map = {}
    for file_path in source_dir.rglob("*"):
        if file_path.is_file():
            files_map[file_path.name.lower()] = file_path
    return files_map


def convert_wikilinks(content: str, files_map: dict[str, Path]) -> str:
    """Convert [wikilinks](wikilinks.md) to standard markdown links."""
    def replace_link(match: re.Match) -> str:
        full_match = match.group(1)
        if "|" in full_match:
            link, display = full_match.split("|", 1)
        else:
            link = display = full_match
        section = ""
        if "#" in link:
            link, section = link.split("#", 1)
            section = f"#{slugify(section)}"
        found_file = find_file(link, files_map)
        if found_file:
            if found_file.suffix.lower() in IMAGE_EXTENSIONS:
                return f"![{display}](assets/{found_file.name})"
            else:
                slug = slugify(found_file.stem)
                return f"[{display}]({slug}.md{section})"
        else:
            slug = slugify(link) if link else slugify(display)
            return f"[{display}]({slug}.md{section})"
    content = re.sub(r"(?<!\!)\[\[([^\]]+)\]\]", replace_link, content)
    return content


def convert_embeds(content: str, files_map: dict[str, Path], source_dir: Path) -> str:
    """Convert *See [embeds](embeds.md)* to appropriate markdown."""
    def replace_embed(match: re.Match) -> str:
        embed_name = match.group(1)
        section = None
        if "#" in embed_name:
            embed_name, section = embed_name.split("#", 1)
        found_file = find_file(embed_name, files_map)
        if found_file:
            if found_file.suffix.lower() in IMAGE_EXTENSIONS:
                return f"![{found_file.stem}](assets/{found_file.name})"
            else:
                slug = slugify(found_file.stem)
                if section:
                    return f"*See [{found_file.stem} - {section}]({slug}.md#{slugify(section)})*"
                else:
                    return f"*See [{found_file.stem}]({slug}.md)*"
        else:
            embed_path = Path(embed_name)
            if embed_path.suffix.lower() in IMAGE_EXTENSIONS:
                return f"![{embed_path.stem}](assets/{embed_name})"
            else:
                slug = slugify(embed_name)
                return f"*See [{embed_name}]({slug}.md)*"
    content = re.sub(r"!\[\[([^\]]+)\]\]", replace_embed, content)
    return content


def ensure_frontmatter(content: str, title: str) -> str:
    """Add Jekyll frontmatter if not present."""
    if content.startswith("---"):
        return content
    frontmatter = f"""---
title: "{title}"
layout: default
---

"""
    return frontmatter + content


def convert_file(source_path: Path, files_map: dict[str, Path], source_dir: Path) -> str:
    """Convert a single Obsidian markdown file."""
    content = source_path.read_text(encoding="utf-8")
    content = convert_wikilinks(content, files_map)
    content = convert_embeds(content, files_map, source_dir)
    title = source_path.stem.replace("-", " ").title()
    content = ensure_frontmatter(content, title)
    return content


def copy_assets(source_dir: Path, assets_dir: Path, files_map: dict[str, Path]) -> None:
    """Copy image assets to the docs/assets folder."""
    assets_dir.mkdir(parents=True, exist_ok=True)
    for name, path in files_map.items():
        if path.suffix.lower() in IMAGE_EXTENSIONS:
            dest = assets_dir / path.name
            shutil.copy2(path, dest)
            print(f"  Copied asset: {path.name}")


def create_jekyll_config(docs_dir: Path) -> None:
    """Create a basic Jekyll config."""
    config = """title: Document Iteration Skill
description: A structured markdown syntax for iterating on documents with Claude AI
theme: jekyll-theme-cayman
baseurl: /document-iteration-skill

# Exclude from processing
exclude:
  - README.md
  - LICENSE
"""
    (docs_dir / "_config.yml").write_text(config, encoding="utf-8")


def main():
    print("Converting Obsidian vault to GitHub Pages...")
    if not OBSIDIAN_DIR.exists():
        print(f"Error: {OBSIDIAN_DIR}/ not found")
        return
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    files_map = build_files_map(OBSIDIAN_DIR)
    print(f"Found {len(files_map)} files in {OBSIDIAN_DIR}/")
    copy_assets(OBSIDIAN_DIR, ASSETS_DIR, files_map)
    md_files = list(OBSIDIAN_DIR.rglob("*.md"))
    print(f"Converting {len(md_files)} markdown files...")
    for source_path in md_files:
        content = convert_file(source_path, files_map, OBSIDIAN_DIR)
        out_name = slugify(source_path.stem) + ".md"
        out_path = DOCS_DIR / out_name
        out_path.write_text(content, encoding="utf-8")
        print(f"  Converted: {source_path.name} → {out_name}")
    create_jekyll_config(DOCS_DIR)
    print("Created _config.yml")
    print(f"\nDone! Output written to {DOCS_DIR}/")


if __name__ == "__main__":
    main()
```

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
2. Use `[wikilinks](wikilinks.md)` to link to other pages
3. Commit and push
4. Action converts and publishes automatically

## See Also

- [FAQ](faq.md)
- [Examples](examples.md)
- [Contributing](contributing.md)