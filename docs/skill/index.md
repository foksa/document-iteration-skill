---
title: "Index"
layout: default
---

# Skill Behavior

How Claude behaves when using the Document Iteration Skill.

## Core Rules

The skill enforces three mandatory rules:

1. **Always respond** - Every comment gets a `%%>response <%%`
2. **Never remove comments** - Only users clean up
3. **Ask before file operations** - Moves/renames need approval

See [Mandatory Rules](mandatory-rules.md) for details and examples.

## Response Behavior

Understanding how Claude responds to feedback:

- [How Claude Responds](responses.md) - Response format and placement

## Customization

You can override default behaviors in your project:

- [Customization](customization.md) - Configure via `.claude.md`

## Quick Reference

| What Claude Does | What Claude Doesn't Do |
|------------------|------------------------|
| Responds to `%% comments %%` | Remove user comments |
| Adds `%%>responses <%%` | Add `%% comments %%` itself |
| Adds `%%> NOTE: <%%` for context | Mark sections as APPROVED |
| Updates content after responding | Move files without asking |

## See Also

- [SKILL.md](../skill.md) - The complete skill file
- [Syntax Overview](../syntax/index.md) - All marker types
- [FAQ](../reference/faq.md) - Common questions