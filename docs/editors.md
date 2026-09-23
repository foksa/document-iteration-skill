---
title: Editor setup
---

# Editor setup

[Overview](index.md) · [Install](install.md) · [Syntax](syntax.md) · **Editor setup**

Color makes the two voices easy to tell apart: your comments in gold (`#968748`), Claude's in teal (`#3C8C8C`).

The simplest option is to ask Claude Code to *"set up VSCode highlighting for iteration markers"* or *"set up Obsidian highlighting for the vault in notes/"*. The skill includes the configs and the steps. You can also do it by hand:

## VSCode

1. Copy `document-iteration-skill/assets/editor-configs/vscode/.vscode/` into your project. If you already have a `settings.json`, merge the settings into it.
2. Install **TODO Highlight v2** (`jgclark.vscode-todo-highlight`).
3. Optional: add the entries from `keybindings.json` to your user keybindings.

Snippets: `%%` + Tab inserts a comment, `%%?` a question, `%%a` APPROVED, and `==(` wraps the selection in a token.

## Obsidian

1. Copy `document-iteration-skill/assets/editor-configs/obsidian/.obsidian/` into your vault, keeping any existing files.
2. Enable the `iteration-markers` CSS snippet (Settings → Appearance) and the **Regex Mark** plugin (Settings → Community plugins).

Obsidian already treats `%% … %%` as comments, so the markers stay hidden in reading view.

## JetBrains IDEs

Settings → Editor → TODO → add these patterns:

- `\%\%[^%]*\%\%`
- `•\%\%>.*<\%\%•`
- `==[^=]*\([^)]*\)==`

## Vim / Neovim

```vim
syntax match IterationUser /%%[^%]*%%/
syntax match IterationClaude /•%%>.\{-}<%%•/
syntax match IterationHighlight /==[^=]*([^)]*)==/
highlight IterationUser guifg=#968748
highlight IterationClaude guifg=#3C8C8C
highlight IterationHighlight gui=underline
```
