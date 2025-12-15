---
---

# Cleanup Syntax

When iteration is complete, you'll want to remove all markers and publish clean content. The skill provides two cleanup approaches.

## Full Document Cleanup

Ask Claude to clean the entire document:

* "clean up the document"
* "remove all markers"
* "ready to publish"

Claude will:

1. Scan for all `%%` comments, `•%%>` responses, `==` highlights, and tokens
1. Check for `%% WIP %%` sections (warns if found)
1. Ask for confirmation with a count of markers to remove
1. Remove all markers, keeping the content

## Partial Cleanup with `%%!CLEANUP!%%`

For documents where some sections are finalized while others are still in progress, use the cleanup marker:

````markdown
# Finalized Introduction

This section is complete and ready.

%%!CLEANUP!%%

# Draft Details %% WIP %%

==Still working(TODO)== on this part.
%% Need to add more examples %%
````

### How It Works

The `%%!CLEANUP!%%` marker defines a **cleanup zone** from the start of the document to the marker position.

**Scope:**

* Everything **above** the marker: cleaned (markers removed)
* The marker itself: removed
* Everything **below** the marker: untouched (markers preserved)

### Process

When Claude encounters `%%!CLEANUP!%%`:

1. **Scans the cleanup zone** (start → marker)
   
   * Counts comments, notes, highlights, tokens
   * Checks for WIP sections
1. **Warns about WIP blockers** (if any in cleanup zone)
   
   ````
   ⚠️ Warning: Found WIP section(s) in cleanup zone: [section names]
   These are still in progress. Continue with cleanup? (yes/no)
   ````

1. **Asks for confirmation**
   
   ````
   Found %%!CLEANUP!%% at line X
   Ready to clean X comments, Y notes, Z tokens from start → line X? (yes/no)
   ````

1. **Executes cleanup** (after explicit "yes")
   
   * Removes all markers in the cleanup zone
   * Removes the `%%!CLEANUP!%%` marker itself
   * Leaves everything below completely untouched

### Example

**Before cleanup:**

````markdown
# API Reference

The endpoint accepts POST requests.

%% Should we mention rate limits here? %%

•%%>Good idea - added a note about the 100 req/min limit. <%%•

Rate limited to 100 requests per minute.

•%%> NOTE: Reviewed by API team on Dec 10 <%%•

%%!CLEANUP!%%

# Implementation Notes %% WIP %%

==Need to verify(CHECK)== the rate limits.
%% Ask team about caching strategy %%
````

**After cleanup:**

````markdown
# API Reference

The endpoint accepts POST requests.

Rate limited to 100 requests per minute.

# Implementation Notes %% WIP %%

==Need to verify(CHECK)== the rate limits.
%% Ask team about caching strategy %%
````

The API Reference section is clean and publishable, while Implementation Notes retains all its iteration markers for continued work.

## Cleanup Rules

**What gets removed:**

* `%% comments %%` (user comments)
* `•%%> responses <%%•` (Claude responses)
* `==highlights(TOKEN)==` → keeps text, removes markup
* `%% WIP %%` markers
* `%%!CLEANUP!%%` marker

**What stays:**

* All actual content
* Document structure
* Formatting

## Markers in Code Blocks

**Markers inside fenced code blocks are ignored during cleanup.**

This is intentional - documentation about the syntax needs to show examples:

````markdown
```markdown
%% This is an example comment %%
==example text(TOKEN)==
```
````

The markers inside the code fence above are **not** real iteration markers - they're documentation examples. Cleanup only affects markers in the actual document content, not in code blocks.

This applies to:

* Fenced code blocks (```` ``` ````)
* Indented code blocks (4+ spaces)
* Inline code (`` ` ` ``)

## Related

* [Syntax Overview](../examples/sessions/index.md) - All marker types
* [Tokens](tokens.md) - Token conventions
