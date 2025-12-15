---
title: "Vscode"
layout: default
---

# VS Code

Visual highlighting and snippets for iteration markers in VS Code.

## Snippets

Add to VS Code: `Cmd+Shift+P` → "Snippets: Configure User Snippets" → "markdown.json"

```json
{
  "Comment": {
    "prefix": "%%",
    "body": "%% $1 %%",
    "description": "Add a comment"
  },
  "Question": {
    "prefix": "%%?",
    "body": "%% ?: $1 %%",
    "description": "Add a question"
  },
  "Token Comment": {
    "prefix": "%%()",
    "body": "%%($1) $2 %%",
    "description": "Comment on a token"
  },
  "Highlight": {
    "prefix": "==(",
    "body": "==${TM_SELECTED_TEXT}==($1)",
    "description": "Wrap selection with highlight token"
  },
  "Approved": {
    "prefix": "%%a",
    "body": "%% APPROVED %%",
    "description": "Mark as approved"
  },
  "Revise": {
    "prefix": "%%r",
    "body": "%% REVISE %%",
    "description": "Mark for revision"
  },
  "Info": {
    "prefix": "%%i",
    "body": "%% INFO: $1 %%",
    "description": "Add actionable info"
  },
  "Note": {
    "prefix": "%%n",
    "body": "%% NOTE: $1 %%",
    "description": "Add context note"
  }
}
```

### Snippet Usage

| Type | Get | Then fill in |
|------|-----|--------------|
| `%%` + Tab | `%% _ %%` | your comment |
| `%%?` + Tab | `%% ?: _ %%` | your question |
| `%%a` + Tab | `%% APPROVED %%` | (nothing) |
| `%%(` + Tab | `%%(_) _ %%` | token, then comment |

## Keyboard Shortcut for Highlights (Recommended)

Snippets aren't ideal for wrapping text. Use a keyboard shortcut instead:

1. Open `Cmd+Shift+P` → "Preferences: Open Keyboard Shortcuts (JSON)"
2. Add this keybinding:

```json
{
  "key": "cmd+shift+h",
  "command": "editor.action.insertSnippet",
  "when": "editorTextFocus && editorLangId == markdown",
  "args": {
    "snippet": "==${TM_SELECTED_TEXT}==($1)"
  }
}
```

**Usage:** Select text → `Cmd+Shift+H` → type token name → Escape

## Visual Highlighting

### Custom Highlighting (Built-in)

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

Install "TODO Highlight" extension, then add to settings:

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

## Related

- [Editor Integration Overview](editor-integration/index.md)
- [Obsidian Setup](editor-integration/obsidian.md)