---
---

# Highlights

Deep dive on the `==text(TOKEN)==` syntax - marking specific text for feedback.

## Basic Syntax

````markdown
==highlighted text(TOKEN)==
````

The double equals wrap the text AND the token. The token in parentheses links to comments.

**Important:** Token goes INSIDE the highlight:

* ✅ `==text(TOKEN)==` - correct (token inside)
* ❌ `==text==(TOKEN)` - wrong (token outside)

**Never nest highlights:**

* ❌ `==outer ==inner(X)== (Y)==` - invalid, will break parsing

## Why Use Highlights?

Highlights solve the "which one?" problem. When you have multiple items to comment on:

````markdown
# Without highlights - ambiguous
Uses PostgreSQL with Redis on AWS.

%% Change the database %%  ← Which one? PostgreSQL? Redis?
````

````markdown
# With highlights - precise
Uses ==PostgreSQL(DB)== with ==Redis(CACHE)== on ==AWS(DEPLOY)==.

%%(DB) Switch to SQLite for v1 %%
%%(CACHE) Keep Redis %%
%%(DEPLOY) Consider DigitalOcean %%
````

## Token Naming

### Simple Numbers

For quick markup:

````markdown
==item one(1)== ==item two(2)== ==item three(3)==

%%(1) Comment %%
%%(2) Comment %%
%%(3) Comment %%
````

### Descriptive Names

For clarity in complex documents:

````markdown
==PostgreSQL(DATABASE)==
==Redis(CACHE)==
==Kubernetes(DEPLOYMENT)==
````

### Abbreviations

Common pattern - short but meaningful:

````markdown
==session timeout(AUTH)==
==rate limiting(PERF)==
==input validation(SEC)==
````

### Topic Grouping

Use dashes for related items:

````markdown
==PostgreSQL(DB-1)==
==MySQL(DB-2)==
==MongoDB(DB-3)==

%%(DB-1) Best for relational data %%
%%(DB-2) Also good, but PostgreSQL preferred %%
%%(DB-3) NO: Not suitable for this use case %%
````

## Linking Comments to Highlights

Comments reference tokens with `%%(TOKEN)`:

````markdown
The API uses ==REST(STYLE)== with ==JSON(FORMAT)==.

%%(STYLE) Consider GraphQL %%
%%(FORMAT) APPROVED %%
````

Claude responds to each:

````markdown
%%(STYLE) Consider GraphQL %%

•%%>Good point! Added GraphQL endpoint for complex queries.
REST remains default for simplicity. <%%•

%%(FORMAT) APPROVED %%

•%%>JSON confirmed! <%%•
````

## The Star Shorthand

When you have only one highlight nearby, use `*`:

````markdown
The session timeout is ==15 minutes==.

%% * Change to 30 minutes %%
````

The `*` means "the highlighted text above." Use this when there's no ambiguity.

## TOKEN Uniqueness

Each TOKEN should be unique within a document. If you need to comment on multiple related items, use numbered or suffixed tokens:

````markdown
The ==primary database(DB-1)== stores user data.
Later, the ==backup database(DB-2)== syncs hourly.

%%(DB-1) Use PostgreSQL %%
%%(DB-2) Use PostgreSQL replica %%
````

If Claude sees `%%(TOKEN)` but no matching `==...(TOKEN)==`, it will ask for clarification.

## Highlights in Different Contexts

### In Lists

````markdown
## Dependencies

- ==Vue 3(FRAMEWORK)==
- ==Pinia(STATE)==
- ==Tailwind(CSS)==

%%(FRAMEWORK) APPROVED %%
%%(STATE) ?: Vuex instead? %%
%%(CSS) Consider plain CSS for smaller bundle %%
````

### In Tables

````markdown
| Feature | Status |
|---------|--------|
| ==Auth(F1)== | Done |
| ==Payments(F2)== | WIP |
| ==Admin(F3)== | Planned |

%%(F1) APPROVED %%
%%(F2) Needs security review %%
%%(F3) Move to v2 %%
````

### In Code Blocks

Highlights don't work inside code blocks. Comment separately:

````markdown
```javascript
const timeout = 15; // AUTH
````

%%(AUTH) Increase timeout to 30 %%

````

## After Cleanup

Highlights become plain text. The markup is removed but content stays:

**Before cleanup:**
```markdown
Uses ==PostgreSQL(DB)== for data storage.
````

**After cleanup:**

````markdown
Uses PostgreSQL for data storage.
````

## Best Practices

### Token Consistency

Pick a naming style and stick with it:

````markdown
# Consistent - all abbreviations
==...(DB)== ==...(API)== ==...(AUTH)== ==...(PERF)==

# Consistent - all numbers
==...(1)== ==...(2)== ==...(3)== ==...(4)==

# Inconsistent - mixed styles (avoid)
==...(DB)== ==...(2)== ==...(Authentication)== ==...(p)==
````

### Don't Over-Highlight

Only highlight text you need to comment on:

````markdown
# Too much
==The== ==API== ==uses== ==REST==.

# Just right
The API uses ==REST(STYLE)==.
````

### Group Related Items

Use related tokens for connected decisions:

````markdown
==Frontend(STACK-1)==: React
==Backend(STACK-2)==: Node.js
==Database(STACK-3)==: PostgreSQL

%%(STACK-1) APPROVED %%
%%(STACK-2) ?: Consider Go for performance? %%
%%(STACK-3) APPROVED %%
````

## See Also

* [Tokens](tokens.md) - Token naming conventions in detail
* [Comments](comments.md) - The `%% %%` syntax
* [Cleanup](cleanup.md) - Removing highlights when done
