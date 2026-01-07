---
description: Setup Obsidian highlighting for iteration markers
argument-hint: [vault-path]
---

Setup Obsidian highlighting for the vault at $1.

1. Copy Obsidian highlighting configs to vault (don't overwrite existing files):
   ```bash
   mkdir -p $1/.obsidian/plugins $1/.obsidian/snippets
   cp -rn .claude/skills/document-iteration-skill/assets/editor-configs/obsidian/.obsidian/* $1/.obsidian/
   ```

2. If `$1/.obsidian/appearance.json` already existed, add `"iteration-markers"` to the `enabledCssSnippets` array.

3. Detect link style:
   - If `$1/.obsidian/app.json` exists, read `useMarkdownLinks`:
     - `true` → standard markdown links `[text](file.md)`
     - `false` or missing → wiki-style links `[[filename]]`
   - If `app.json` doesn't exist, ask user which style they prefer.

4. Add to CLAUDE.md:
   ```markdown
   ## Obsidian Vault: $1
   Use [wiki-style links | standard markdown links] for internal links.
   ```

5. Tell user to enable the **Regex Mark** plugin in Obsidian settings.
