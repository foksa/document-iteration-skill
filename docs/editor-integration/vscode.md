---
---

# VS Code

Visual highlighting and snippets for iteration markers in VS Code.

## Quick Setup

Copy files from `editor-configs/vscode/`:

* `.vscode/settings.json` → your project's `.vscode/` folder
* `.vscode/markdown.code-snippets` → your project's `.vscode/` folder
* `keybindings.json` → merge into your user keybindings (`Cmd+Shift+P` → "Preferences: Open Keyboard Shortcuts (JSON)")

For highlighting, install the "TODO Highlight v2" extension (jgclark.vscode-todo-highlight). The `extensions.json` will prompt you to install it.

## Manual Setup

### Snippets

Add to VS Code: `Cmd+Shift+P` → "Snippets: Configure User Snippets" → "markdown.json"

````json
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
    "body": "==${TM_SELECTED_TEXT}($1)==",
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
````

### Snippet Usage

|Type|Get|Then fill in|
|----|---|------------|
|`%%` + Tab|`%% _ %%`|your comment|
|`%%?` + Tab|`%% ?: _ %%`|your question|
|`%%a` + Tab|`%% APPROVED %%`|(nothing)|
|`%%(` + Tab|`%%(_) _ %%`|token, then comment|

## Keyboard Shortcut for Highlights (Recommended)

Snippets aren't ideal for wrapping text. Use a keyboard shortcut instead:

1. Open `Cmd+Shift+P` → "Preferences: Open Keyboard Shortcuts (JSON)"
1. Add this keybinding:

````json
{
  "key": "cmd+shift+h",
  "command": "editor.action.insertSnippet",
  "when": "editorTextFocus && editorLangId == markdown",
  "args": {
    "snippet": "==${TM_SELECTED_TEXT}($1)=="
  }
}
````

**Usage:** Select text → `Cmd+Shift+H` → type token name → Escape

## Visual Highlighting

### Custom Highlighting (Built-in)

Add to `.vscode/settings.json`:

````json
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
````

### TODO Highlight v2 Extension

Install "TODO Highlight v2" extension (jgclark.vscode-todo-highlight), then add to settings:

````json
{
  "todohighlight.include": [
    "**/*.md",
    "**/*.markdown"
  ],
  "todohighlight.keywords": [
    {
      "text": "%%",
      "color": "rgb(150, 135, 60)",
      "backgroundColor": "transparent"
    },
    {
      "text": "•%%>",
      "color": "rgb(60, 140, 140)",
      "backgroundColor": "transparent"
    },
    {
      "text": "<%%•",
      "color": "rgb(60, 140, 140)",
      "backgroundColor": "transparent"
    }
  ]
}
````

### Better Comments Extension

Install "Better Comments" - works out of the box for `%%` in many file types.

## Related

* [Editor Integration Overview](index.md)
* [Obsidian Setup](obsidian.md)
