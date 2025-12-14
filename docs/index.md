---
title: "Index"
layout: default
---

# Syntax Overview

The Document Iteration Skill uses simple markers embedded in your documents to enable collaborative editing between you and Claude.

## Core Markers

### Comments `%%`

Add feedback, questions, or instructions anywhere in your document:

```markdown
%% This section needs more detail %%

%% Is this the right approach? %%

%%(PERF) Consider caching here %%
```

Comments can include optional tokens in parentheses to categorize feedback.

### Highlights `==text==(TOKEN)`

Mark specific text that needs attention:

```markdown
The API uses ==synchronous calls==(PERF) which may cause issues.

We need to ==define the authentication flow==(TODO).
```

Highlights combine inline marking with categorization.

### Notes `>>`

Add contextual information or background that helps with review:

```markdown
>> NOTE: This was discussed in the team meeting on Monday >>

>> CONTEXT: Legacy system requires this format >>
```

Notes provide context without being direct feedback.

### WIP Sections `%% WIP %%`

Mark sections that are still in progress:

```markdown
## Draft Section %% WIP %%

This content is still being developed...
```

WIP markers prevent premature cleanup of incomplete sections.

## Response Syntax

Claude responds to feedback using indented responses:

```markdown
%% Is this approach scalable? %%
  %% > Yes, the current design supports horizontal scaling
     through the queue system. %%
```

Responses are indented and prefixed with `>` to show the conversation flow.

## Quick Reference

| Marker | Purpose | Example |
|--------|---------|---------|
| `%% text %%` | Comments/feedback | `%% Needs clarification %%` |
| `==%%(TOKEN)` | Highlight with token | `==unclear==(TODO)` |
| `>> text >>` | Notes/context | `>> NOTE: See RFC 123 >>` |
| `%% WIP %%` | Work in progress | `## Section %% WIP %%` |
| `%% > text %%` | Claude's response | `%% > Done, added details %%` |

## Related Documentation

- [Tokens](tokens.md) - Token naming conventions and usage
- [Cleanup](cleanup.md) - Removing markers when iteration is complete
- [Examples](examples.md) - Real-world usage patterns