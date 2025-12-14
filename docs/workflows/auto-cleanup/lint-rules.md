---
title: "Lint Rules"
layout: default
---

# Lint Rules

Custom lint rules that flag iteration markers. Integrates with existing linting workflows.

## Markdownlint

### Custom Rule

Create `.markdownlint/iteration-markers.js`:

```javascript
module.exports = {
  names: ["iteration-markers"],
  description: "No iteration markers in final documents",
  tags: ["iteration"],
  function: function rule(params, onError) {
    const patterns = [
      /%%[^%]*%%/g,           // Comments
      />>[^>]*>>/g,           // Notes
      /==[^=]*==\([^)]+\)/g   // Highlights with tokens
    ];

    params.lines.forEach((line, index) => {
      patterns.forEach(pattern => {
        const matches = line.match(pattern);
        if (matches) {
          matches.forEach(match => {
            onError({
              lineNumber: index + 1,
              detail: `Found iteration marker: ${match}`,
              context: line.trim()
            });
          });
        }
      });
    });
  }
};
```

Configure in `.markdownlint.json`:

```json
{
  "customRules": ["./.markdownlint/iteration-markers.js"]
}
```

### Simple Pattern in Config

Alternatively, use the built-in regex check:

```json
{
  "search-replace": {
    "rules": [
      {
        "name": "no-iteration-comments",
        "message": "Remove iteration comment before committing",
        "searchPattern": "/%%[^%]*%%/",
        "searchScope": "text"
      }
    ]
  }
}
```

## ESLint (for MDX/JSX)

Create `.eslintrc.js` rule:

```javascript
module.exports = {
  rules: {
    "no-restricted-syntax": [
      "error",
      {
        selector: "Literal[value=/%%.*%%/]",
        message: "Iteration markers should be removed"
      }
    ]
  }
};
```

## Remark Lint

Create `remark-no-iteration-markers.js`:

```javascript
import { lintRule } from 'unified-lint-rule';
import { visit } from 'unist-util-visit';

const rule = lintRule(
  'remark-lint:no-iteration-markers',
  (tree, file) => {
    visit(tree, 'text', (node) => {
      if (/%%[^%]*%%/.test(node.value)) {
        file.message('Iteration marker found', node);
      }
    });
  }
);

export default rule;
```

## Pre-commit Integration

Combine with pre-commit hooks:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.37.0
    hooks:
      - id: markdownlint
        args: ["--config", ".markdownlint.json"]
```

## Package.json Scripts

```json
{
  "scripts": {
    "lint:markers": "grep -r -l '%%' --include='*.md' docs/ && exit 1 || exit 0",
    "lint": "npm run lint:markers && markdownlint docs/"
  }
}
```

## Benefits

- Integrates with existing lint workflow
- Runs automatically on save (with editor integration)
- Provides specific line numbers
- Part of standard development flow

## Limitations

- Requires lint setup
- May add complexity
- Not all teams use linters

## Related

- [Auto-Cleanup Approaches](index.md) - All approaches
- [CI/CD Check](ci-cd.md) - Run lint in CI