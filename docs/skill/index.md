---
---

# Skill Behavior

How Claude behaves when using the Document Iteration Skill.

## Core Rules

The skill enforces six mandatory rules:

1. **Always respond** - Every comment gets a `%%>response <%%`
1. **Never remove comments** - Only users clean up
1. **Ask before file operations** - Moves/renames need approval
1. **Ask when something feels off** - Unclear feedback, impossible requests
1. **Compact responses after moving** - Don't duplicate content
1. **Handle TOKEN edge cases** - Preserve TOKENs, warn about orphans

See [Mandatory Rules](mandatory-rules.md) for details and examples.

## Response Behavior

Understanding how Claude responds to feedback:

* [How Claude Responds](responses.md) - Response format and placement

## Customization

You can override default behaviors in your project:

* [Customization](customization.md) - Configure via `.claude.md`

## Quick Reference

|What Claude Does|What Claude Doesn't Do|
|----------------|----------------------|
|Responds to `%% comments %%`|Remove user comments|
|Adds `%%>responses <%%`|Add `%% comments %%` itself|
|Adds `%%> NOTE: <%%` for context|Mark sections as APPROVED|
|Updates content after responding|Move files without asking|

## See Also

* *SKILL.md* - The complete skill file
* *Syntax Overview* - All marker types
* *FAQ* - Common questions
