---
title: "Editor Integration"
layout: default
---

# Editor Integration

Visual highlighting of iteration markers while editing. See markers as you write, not just at commit time.

## VS Code

### Custom Highlighting

Add to `.vscode/settings.json`:

```json
{
  "editor.tokenColorCustomizations": {
    "textMateRules": [
      {
        "scope": "comment.block.percentage.markdown",
        "settings": {
          "foreground": "#FFA500",
          "fontStyle": "italic"
        }
      }
    ]
  }
}
```

### TODO Highlight Extension

Install "TODO Highlight" extension, then configure:

```json
{
  "todohighlight.keywords": [
    {
      "text": "%%",
      "color": "#000",
      "backgroundColor": "#FFA500",
      "overviewRulerColor": "#FFA500"
    },
    {
      "text": ">>",
      "color": "#000",
      "backgroundColor": "#90EE90",
      "overviewRulerColor": "#90EE90"
    }
  ]
}
```

### Better Comments Extension

Install "Better Comments" - works out of the box for `%%` in many file types.

## Obsidian

### Custom CSS Snippet

Create `.obsidian/snippets/iteration-markers.css`:

```css
/* Highlight %% comments %% */
.cm-comment {
  background-color: rgba(255, 165, 0, 0.3);
  padding: 2px 4px;
  border-radius: 3px;
}

/* Highlight ==text==(TOKEN) */
mark {
  background-color: rgba(255, 255, 0, 0.4);
  padding: 1px 2px;
}

/* Style >> notes >> */
.cm-hmd-internal-link {
  color: #32CD32;
}
```

Enable in Settings → Appearance → CSS Snippets.

### Linter Plugin

Install "Linter" plugin. Add custom rule to flag markers:

```yaml
rules:
  custom-regex:
    - pattern: '%%[^%]*%%'
      message: 'Iteration marker found'
      severity: warning
```

## Vim/Neovim

Add to your config:

```vim
" Highlight iteration markers
syntax match IterationComment /%%[^%]*%%/
highlight IterationComment guibg=#FFA500 guifg=#000000

syntax match IterationNote />>[^>]*>>/
highlight IterationNote guibg=#90EE90 guifg=#000000

syntax match IterationHighlight /==[^=]*==([^)]*)/
highlight IterationHighlight guibg=#FFFF00 guifg=#000000
```

## JetBrains IDEs

Settings → Editor → TODO:

Add patterns:
- `\%\%.*\%\%` - Comments
- `>>.*>>` - Notes
- `==.*==\(.*\)` - Highlights

## Benefits

- Immediate visual feedback
- See markers while writing
- No waiting for commit/CI

## Limitations

- Requires per-editor setup
- Doesn't prevent commits
- Team members need same config

## Related

- [Auto-Cleanup Approaches](index.md) - All approaches
- [Git Hooks](git-hooks.md) - Block commits with markers