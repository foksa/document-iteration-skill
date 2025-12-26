---
---

# Best Practices

Tips and patterns for effective document iteration.

## Writing Good Comments

### Be Specific

````markdown
# Vague - unclear what to do
%% Fix this %%
%% Make it better %%

# Specific - actionable
%% Change timeout from 15 to 30 minutes %%
%% Add input validation for email field %%
````

### One Topic Per Comment

````markdown
# Hard to track
%% Fix timeout, add logging, update docs, and check edge cases %%

# Easy to track
%% Fix timeout - 15 → 30 min %%
%% Add request logging %%
%% Update API docs %%
%% Handle empty input edge case %%
````

### Use the Right Syntax

|When you want to...|Use|
|-------------------|---|
|Give feedback|`%% comment %%`|
|Ask a question|`%% ?: question %%`|
|Provide data to use|`%% INFO: data %%`|
|Add context (no action)|`%% NOTE: context %%`|
|Mark for specific text|`==text(TOKEN)==` + `%%(TOKEN) comment %%`|

## Token Strategy

### When to Use Tokens

Use tokens when you have multiple items to comment on:

````markdown
# Without tokens - ambiguous
Uses PostgreSQL with Redis.
%% Consider alternatives %%  ← Which one?

# With tokens - clear
Uses ==PostgreSQL(DB)== with ==Redis(CACHE)==.
%%(DB) Consider SQLite for v1 %%
%%(CACHE) Keep Redis %%
````

### Consistent Naming

Pick a style and stick with it:

````markdown
# Good - consistent abbreviations
==database(DB)== ==endpoint(API)== ==login(AUTH)== ==button(UI)==

# Good - consistent numbers
==first(1)== ==second(2)== ==third(3)== ==fourth(4)==

# Avoid - mixed styles
==db(DB)== ==item(2)== ==Authentication(Authentication)== ==thing(x)==
````

### Semantic Tokens

Use meaningful names for complex documents:

````markdown
==encryption(SECURITY-1)== ==auth tokens(SECURITY-2)==
==query speed(PERF-1)== ==memory usage(PERF-2)==
==onboarding(UX-1)== ==checkout(UX-2)==
````

## Document Structure

### Start with WIP

New sections should be marked work-in-progress:

````markdown
## New Feature %% WIP %%

...initial draft...
````

### Progress to REVISE

After first pass, mark for revision:

````markdown
## New Feature %% REVISE %%

%% Add error handling %%
%% Consider edge cases %%
````

### End with APPROVED

Lock down finalized sections:

````markdown
## New Feature %% APPROVED %%
````

### Section Independence

Keep sections self-contained so they can be approved independently:

````markdown
## Authentication %% APPROVED %%
## Payments %% WIP %%
## Notifications %% REVISE %%
````

## Iteration Flow

### Small Iterations

Don't try to perfect everything at once:

````markdown
# Round 1: Structure
%% Is this the right structure? %%

# Round 2: Content
%% Add more detail to section 2 %%

# Round 3: Polish
%% Fix typos and formatting %%
````

### Keep Comments Until Done

Don't clean up prematurely. Comments are your audit trail:

````markdown
# Keep this visible
%% Add caching %%

•%%>Added Redis caching with 5-min TTL <%%•

# Until you're sure it's done, then cleanup
````

### Cleanup When Ready

Clean up when:

* Section is approved
* Ready to commit to git
* Document is being published

## Working with Claude

### Trust but Verify

Claude responds to all comments, but review the changes:

````markdown
%% Add input validation %%

•%%>Added validation for email, password, username <%%•

# Check that the validation is actually correct
````

### Correct Mistakes Immediately

If Claude misunderstands:

````markdown
%% Add logging %%

•%%>Added console.log statements <%%•

%% No, use proper logging framework %%

•%%>Updated to use Winston logger with levels <%%•
````

### Handle Violations

If Claude removes your comment or skips a response:

1. Point it out: "You removed my comment without responding"
1. Ask Claude to undo and respond properly
1. Continue the iteration

See [Troubleshooting](faq.md#claude-removed-my-comment-without-responding) for more.

## Version Control

### Commit Often

````
docs: Add initial API design (WIP)
docs: Address @JS feedback on auth
docs: Final review - mark sections APPROVED
docs: Cleanup iteration markers for release
````

### Meaningful Messages

Include what iteration accomplished:

````
docs: API design - round 2

- Updated rate limits per @MK feedback
- Added error handling section
- Marked auth as APPROVED
````

### Branch Strategy

For major documents:

1. `draft/` - Initial creation
1. `review/` - Team feedback
1. `main` - Approved content

## Common Pitfalls

### Over-Commenting

````markdown
# Too much
%% Good intro %%
%% Nice formatting %%
%% I like this part %%

# Just right - actionable feedback only
%% Add example for the edge case %%
````

### Ignoring NOTE Tags

Notes are context, not action items:

````markdown
%% NOTE: Legal approved this language %%

# Don't try to change it - it's locked
````

### Premature Cleanup

````markdown
# Don't do this
User: "cleanup the doc"
*cleans up while still WIP*

# Do this
User: "cleanup the doc"
Claude: "Found 2 WIP sections. Clean up anyway? (yes/no)"
````

### Forgetting Tokens

````markdown
# Orphaned token - confusing
Uses ==PostgreSQL(DB)== for storage.

%% Use MySQL instead %%  ← Forgot (DB), unclear reference
````

**Note:** Claude warns about orphaned TOKENs - if it sees `%%(TOKEN)` without a matching `==...(TOKEN)==` highlight, it will ask where to apply the feedback.

### Using Same TOKEN Twice

Each TOKEN should be unique per document:

````markdown
# Ambiguous - which (DB) does the comment refer to?
Uses ==PostgreSQL(DB)== for users and ==MySQL(DB)== for logs.

# Clear - unique tokens
Uses ==PostgreSQL(DB-1)== for users and ==MySQL(DB-2)== for logs.
%%(DB-1) Consider consolidating to PostgreSQL %%
````

## See Also

* [FAQ](faq.md) - Common questions
* *Syntax Overview* - All marker types
* *Mandatory Rules* - How Claude must behave
