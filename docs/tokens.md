---
title: "Tokens"
layout: default
---

# Tokens

Tokens are short identifiers that categorize and group related feedback. They appear in parentheses within comments and highlights.

## Basic Usage

**In comments:**
```markdown
%%(PERF) This query runs on every request %%

%%(SECURITY) Validate input before processing %%
```

**In highlights:**
```markdown
The system uses ==polling==(PERF) instead of webhooks.

Users must ==manually configure==(UX) the settings.
```

## Why Use Tokens?

**1. Group related feedback**

Multiple comments about the same issue share a token:
```markdown
%%(AUTH) Session handling needs review %%

The ==token refresh==(AUTH) logic seems fragile.

%%(AUTH) What happens when refresh fails? %%
```

Claude can address all `(AUTH)` items together.

**2. Prioritize by category**

Ask Claude to focus on specific categories:
- "Address all SECURITY tokens first"
- "What PERF issues did you find?"
- "Show me all TODO items"

**3. Track progress**

Tokens make it easy to see what's addressed:
```markdown
%%(API) Need error handling %%
  %% > Added try-catch with proper error responses %%
```

## Common Token Conventions

| Token | Purpose |
|-------|---------|
| `TODO` | Action items, things to add |
| `FIXME` | Bugs or issues to fix |
| `PERF` | Performance concerns |
| `SECURITY` | Security considerations |
| `UX` | User experience issues |
| `API` | API design feedback |
| `DOCS` | Documentation needs |
| `TEST` | Testing requirements |
| `QUESTION` | Questions needing answers |
| `REVIEW` | Needs review/approval |

## Token Naming Guidelines

**Keep them short** - Tokens appear inline, so brevity matters:
```markdown
# Good
%%(DB) Consider indexing %%

# Too long
%%(DATABASE_OPTIMIZATION) Consider indexing %%
```

**Be consistent** - Pick a convention and stick with it:
```markdown
# Pick one style
%%(PERF)    # Abbreviation
%%(Performance)  # Full word - also fine, just be consistent
```

**Use UPPERCASE** - Makes tokens visually distinct:
```markdown
%%(TODO) Add validation %%   # Clear
%%(todo) Add validation %%   # Works but less visible
```

**Create project-specific tokens** as needed:
```markdown
%%(MIGRATION) Handle legacy data format %%
%%(COMPLIANCE) GDPR requirement %%
%%(MOBILE) Touch target too small %%
```

## Tokens in Responses

When Claude responds to tokenized feedback, responses inherit context:
```markdown
%%(SECURITY) SQL injection risk here %%
  %% > Switched to parameterized queries. The `userId`
     is now passed as a bound parameter. %%
```

## Filtering and Addressing

You can ask Claude to work with specific tokens:

- "List all TODO tokens"
- "Address the PERF issues"
- "How many SECURITY items remain?"
- "Focus on API tokens in this section"

## Related

- [Syntax Overview](index.md) - All marker types
- [Cleanup](cleanup.md) - Removing markers when done
- [Examples](examples.md) - See tokens in context