---
---

# Tokens

Tokens are short identifiers in parentheses that link comments to specific highlighted text.

## Primary Use: Linking Highlights to Comments

The main purpose of tokens is to connect a `==highlight(TOKEN)==` with its `%%(TOKEN) comment %%`:

````markdown
The system uses ==PostgreSQL(DB)== with ==Redis(CACHE)==.

%%(DB) Consider SQLite for v1 %%
%%(CACHE) Do we need caching for MVP? %%
````

Claude knows exactly which text each comment refers to.

## Important: TOKENs Must Be Unique

**Each TOKEN should appear only once per document** when linking highlights to comments.

````markdown
# Wrong - ambiguous
Uses ==PostgreSQL(DB)== for users and ==MySQL(DB)== for logs.
%%(DB) Switch to SQLite %%  ← Which one?

# Correct - unique tokens
Uses ==PostgreSQL(DB-USERS)== for users and ==MySQL(DB-LOGS)== for logs.
%%(DB-USERS) Switch to SQLite %%
%%(DB-LOGS) Keep MySQL for logs %%
````

If Claude sees `%%(TOKEN)` but multiple `==...(TOKEN)==` highlights, it won't know which one you mean.

## Standalone Comments (No Highlight)

For general feedback not tied to specific text, you can use tokens as categories:

````markdown
%% This section needs work %%
%%(PERF) Query runs on every request %%
%%(SECURITY) Add input validation %%
````

These don't link to highlights - they're just categorized comments. Same token can repeat here since there's no ambiguity.

## Common Token Patterns

|Token|Purpose|
|-----|-------|
|`TODO`|Action items|
|`FIXME`|Bugs to fix|
|`PERF`|Performance|
|`SECURITY`|Security concerns|
|`UX`|User experience|
|`API`|API design|
|`DOCS`|Documentation|

## Token Naming

**Keep them short:**

````markdown
%%(DB) Consider indexing %%        # Good
%%(DATABASE_OPT) Consider indexing %%  # Too long
````

**Use UPPERCASE** for visibility:

````markdown
%%(TODO) Add validation %%   # Clear
%%(todo) Add validation %%   # Works but less visible
````

**Number for multiples:**

````markdown
==first issue(PERF-1)== and ==second issue(PERF-2)==
%%(PERF-1) Fix this first %%
%%(PERF-2) Lower priority %%
````

## Orphaned Tokens

If Claude sees `%%(TOKEN)` but no matching `==...(TOKEN)==` highlight, it will ask:

````markdown
•%%> ?: I don't see ==...(TOKEN)== in the document. Where should I apply this? <%%•
````

This helps catch typos or forgotten highlights.

## Related

* [Highlights](highlights.md) - The `==text(TOKEN)==` syntax
* [Syntax Overview](../examples/sessions/index.md) - All marker types
* *Best Practices* - Token naming strategies
