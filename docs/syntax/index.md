---
---

# Syntax Overview

The Document Iteration Skill uses simple markers embedded in your documents to enable collaborative editing between you and Claude.

## Core Markers

### Comments `%%`

Add feedback, questions, or instructions anywhere in your document:

````markdown
%% This section needs more detail %%

%% Is this the right approach? %%

%%(PERF) Consider caching here %%
````

Comments can include optional tokens in parentheses to categorize feedback.

### Highlights `==text(TOKEN)==`

Mark specific text that needs attention:

````markdown
The API uses ==synchronous calls(PERF)== which may cause issues.

We need to ==define the authentication flow(TODO)==.
````

Highlights combine inline marking with categorization. **Token goes INSIDE the highlight.**

### WIP Sections `%% WIP %%`

Mark sections that are still in progress:

````markdown
## Draft Section %% WIP %%

This content is still being developed...
````

WIP markers prevent premature cleanup of incomplete sections.

## Response Syntax

Claude responds to feedback using `•%%> response <%%•`:

````markdown
%% Is this approach scalable? %%

•%%>Yes, the current design supports horizontal scaling
through the queue system. <%%•
````

Claude can also add notes:

````markdown
•%%> NOTE: This was discussed in the team meeting on Monday <%%•
•%%> RISK: Legacy system may require different format <%%•
````

## Quick Reference

|Marker|Purpose|Example|
|------|-------|-------|
|`%% text %%`|User comments/feedback|`%% Needs clarification %%`|
|`==text(TOKEN)==`|Highlight with token|`==unclear(TODO)==`|
|`%% WIP %%`|Work in progress|`## Section %% WIP %%`|
|`•%%>response <%%•`|Claude's response|`•%%>Done, added details. <%%•`|
|`•%%> NOTE: <%%•`|Claude's notes|`•%%> NOTE: See RFC 123 <%%•`|

## Markers in Code Blocks

**Markers inside code blocks are always ignored** - both during iteration and cleanup.

This means documentation files can safely include syntax examples:

````markdown
Here's how to add a comment:

```markdown
%% Your feedback here %%
```
````

The `%% Your feedback here %%` inside the code fence is **not** treated as real feedback. Claude will not respond to it or clean it up - it's just an example.

This applies to:

* Fenced code blocks (```` ``` ````)
* Indented code blocks (4+ spaces)
* Inline code (`` ` ` ``)

## Related Documentation

* [Comments](comments.md) - Deep dive on `%% %%` syntax
* [Highlights](highlights.md) - Deep dive on `==text(TOKEN)==`
* [Tokens](tokens.md) - Token naming conventions and usage
* [Cleanup](cleanup.md) - Removing markers when iteration is complete
* *Examples* - Real-world usage patterns
