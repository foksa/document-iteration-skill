---
title: "_Vscode Snippets"
layout: default
---

# VS Code Snippets (TODO)

Future addition: VS Code snippets for faster syntax entry.

## Planned Snippets

### User Feedback Snippets

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
    "body": "==$1==($2)",
    "description": "Highlight text with token"
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

## Installation

1. Open VS Code
2. `Cmd+Shift+P` → "Snippets: Configure User Snippets"
3. Select "markdown.json"
4. Paste the snippets above

## Status
Not started - placeholder for future work.