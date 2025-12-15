---
title: "Index"
layout: default
---

# Editor Integration

Visual highlighting of iteration markers while editing. See markers as you write, not just at commit time.

## Supported Editors

- [VS Code](editor-integration/vscode.md) - Custom highlighting, extensions
- [Obsidian](editor-integration/obsidian.md) - CSS snippets, linter plugin
- [Vim/Neovim](editor-integration/vim.md) - Syntax highlighting
- [JetBrains IDEs](editor-integration/jetbrains.md) - TODO patterns

## Benefits

- Immediate visual feedback
- See markers while writing
- No waiting for commit/CI

## Limitations

- Requires per-editor setup
- Doesn't prevent commits
- Team members need same config

## Related

- [Auto-Cleanup](workflows/auto-cleanup/index.md) - Prevent markers in commits
- [Git Hooks](workflows/auto-cleanup/git-hooks.md) - Block commits with markers
