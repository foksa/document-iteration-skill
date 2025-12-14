#!/usr/bin/env python3
"""
Convert Obsidian vault to GitHub Pages compatible markdown.

Handles:
- [[wikilinks]] → [text](file.md)
- [[link|display]] → [display](link.md)
- ![[embeds]] → content inlined or linked
- ![[image.png]] → ![image](assets/image.png)
- Adds Jekyll frontmatter if missing
"""

import os
import re
import shutil
from pathlib import Path

OBSIDIAN_DIR = Path("obsidian")
DOCS_DIR = Path("docs")
ASSETS_DIR = DOCS_DIR / "assets"

# Image extensions to handle
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

    # Try exact match first
    if name_lower in files_map:
        return files_map[name_lower]

    # Try with .md extension
    if f"{name_lower}.md" in files_map:
        return files_map[f"{name_lower}.md"]

    # Try without extension
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
    """Convert [[wikilinks]] to standard markdown links."""

    def replace_link(match: re.Match) -> str:
        full_match = match.group(1)

        # Handle [[link|display]] format
        if "|" in full_match:
            link, display = full_match.split("|", 1)
        else:
            link = display = full_match

        # Handle section links [[page#section]]
        section = ""
        if "#" in link:
            link, section = link.split("#", 1)
            section = f"#{slugify(section)}"

        # Find the actual file
        found_file = find_file(link, files_map)

        if found_file:
            # Check if it's an image
            if found_file.suffix.lower() in IMAGE_EXTENSIONS:
                return f"![{display}](assets/{found_file.name})"
            else:
                # It's a markdown file
                slug = slugify(found_file.stem)
                return f"[{display}]({slug}.md{section})"
        else:
            # File not found, create a reasonable link anyway
            slug = slugify(link) if link else slugify(display)
            return f"[{display}]({slug}.md{section})"

    # Match [[...]] but not ![[...]]
    content = re.sub(r"(?<!\!)\[\[([^\]]+)\]\]", replace_link, content)

    return content


def convert_embeds(content: str, files_map: dict[str, Path], source_dir: Path) -> str:
    """Convert ![[embeds]] to appropriate markdown."""

    def replace_embed(match: re.Match) -> str:
        embed_name = match.group(1)

        # Handle section embeds ![[page#section]]
        section = None
        if "#" in embed_name:
            embed_name, section = embed_name.split("#", 1)

        found_file = find_file(embed_name, files_map)

        if found_file:
            # Check if it's an image
            if found_file.suffix.lower() in IMAGE_EXTENSIONS:
                return f"![{found_file.stem}](assets/{found_file.name})"
            else:
                # It's a markdown file - inline the content or link to it
                slug = slugify(found_file.stem)
                if section:
                    return f"*See [{found_file.stem} - {section}]({slug}.md#{slugify(section)})*"
                else:
                    return f"*See [{found_file.stem}]({slug}.md)*"
        else:
            # Check if it looks like an image
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

    # Convert wikilinks
    content = convert_wikilinks(content, files_map)

    # Convert embeds
    content = convert_embeds(content, files_map, source_dir)

    # Ensure frontmatter
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
        print(f"Creating {OBSIDIAN_DIR}/ directory with example file...")
        OBSIDIAN_DIR.mkdir(parents=True, exist_ok=True)

        example = """# Welcome

This is your Obsidian vault for documentation.

## Getting Started

Add your markdown files here. They will be automatically converted to GitHub Pages format.

### Supported Syntax

- [[Wikilinks]] are converted to standard links
- [[Link|Custom Display Text]] works too
- ![[Embedded Notes]] become links
- ![[images.png]] are copied to assets/

## Learn More

Check out the [[Examples]] page for more details.
"""
        (OBSIDIAN_DIR / "index.md").write_text(example, encoding="utf-8")
        (OBSIDIAN_DIR / "Examples.md").write_text("# Examples\n\nAdd your examples here.\n", encoding="utf-8")
        print("  Created example files in obsidian/")

    # Clean and recreate docs directory
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    # Build file map
    files_map = build_files_map(OBSIDIAN_DIR)
    print(f"Found {len(files_map)} files in {OBSIDIAN_DIR}/")

    # Copy assets
    copy_assets(OBSIDIAN_DIR, ASSETS_DIR, files_map)

    # Convert markdown files
    md_files = list(OBSIDIAN_DIR.rglob("*.md"))
    print(f"Converting {len(md_files)} markdown files...")

    for source_path in md_files:
        content = convert_file(source_path, files_map, OBSIDIAN_DIR)

        # Output filename (slugified)
        out_name = slugify(source_path.stem) + ".md"
        out_path = DOCS_DIR / out_name

        out_path.write_text(content, encoding="utf-8")
        print(f"  Converted: {source_path.name} → {out_name}")

    # Create Jekyll config
    create_jekyll_config(DOCS_DIR)
    print("Created _config.yml")

    print(f"\nDone! Output written to {DOCS_DIR}/")


if __name__ == "__main__":
    main()