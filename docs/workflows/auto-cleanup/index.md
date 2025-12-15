---
title: "Index"
layout: default
---

# Auto-Cleanup Approaches

Iteration markers (`%% %%`, `>> >>`, `==(TOKEN)`) are meant for drafting - they shouldn't end up in final documents. This section covers different approaches to catch and remove markers before they're committed or published.

## Why Auto-Cleanup?

Manual cleanup works, but it's easy to forget. Auto-cleanup provides safety nets:

- **Catch forgotten markers** before they reach git
- **Enforce consistency** across team members
- **Reduce friction** by automating the obvious

## Approaches

Choose based on your workflow:

| Approach | When it runs | Requires Claude | Best for |
|----------|--------------|-----------------|----------|
| [Claude Check](claude-check.md) | Before commit (manual) | Yes | Claude Code users |
| [Git Hooks](git-hooks.md) | On `git commit` | No | Solo developers |
| [CI/CD Check](ci-cd.md) | On push/PR | No | Teams |
| [Editor Integration](editor-integration/index.md) | While editing | No | Visual feedback |
| [Lint Rules](lint-rules.md) | On lint/save | No | Existing lint setup |

## Recommendations

**Using Claude Code?** Start with [Claude Check](claude-check.md) - it's built into the skill workflow.

**Working in a team?** Add [CI/CD Check](ci-cd.md) as a backup - catches anything that slips through locally.

**Want prevention over detection?** Use [Editor Integration](editor-integration/index.md) to see markers visually while editing.

## Combining Approaches

These aren't mutually exclusive. A robust setup might use:

1. **Editor integration** - See markers while writing
2. **Claude check** - Catch before commit
3. **CI/CD** - Final safety net

## Related

- [Customization](../../skill/customization.md) - Configure cleanup behavior
- [Cleanup Syntax](../../syntax/cleanup.md) - Manual cleanup commands