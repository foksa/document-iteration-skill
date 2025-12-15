---
title: "Vscode"
layout: default
---

# VS Code

Visual highlighting of iteration markers in VS Code.

## Custom Highlighting

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

## TODO Highlight Extension

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

## Better Comments Extension

Install "Better Comments" - works out of the box for `%%` in many file types.

## Related

- [Editor Integration Overview](editor-integration/index.md)
- [Obsidian Setup](editor-integration/obsidian.md)