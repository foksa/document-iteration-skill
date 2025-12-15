---
title: "Obsidian"
layout: default
---

# Obsidian

Visual highlighting of iteration markers in Obsidian.

## Custom CSS Snippet

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

## Linter Plugin

Install "Linter" plugin. Add custom rule to flag markers:

```yaml
rules:
  custom-regex:
    - pattern: '%%[^%]*%%'
      message: 'Iteration marker found'
      severity: warning
```

## Related

- [Editor Integration Overview](editor-integration/index.md)
- [VS Code Setup](editor-integration/vscode.md)