---
---

# Comments

Deep dive on the `%% comment %%` syntax - the core feedback mechanism.

## Basic Syntax

````markdown
%% Your comment here %%
````

Comments are wrapped in double percent signs. They can appear anywhere in a document.

## Types of Comments

### General Feedback

Plain comments without prefixes:

````markdown
%% This section needs more detail %%
%% The timeline seems unrealistic %%
%% Consider adding examples %%
````

### Questions

Prefix with `?:` to mark as a question:

````markdown
%% ?: Is 15 minutes too short for session timeout? %%
%% ?: Should we support annual billing? %%
````

Questions signal that you need input before proceeding.

### Information Tags

**INFO** - Actionable information Claude should use:

````markdown
%% INFO: Budget increased to $200/month %%
%% INFO: API v2 released with breaking changes %%
````

**NOTE** - Historical context (read-only, no response needed):

````markdown
%% NOTE: Team decided this in Dec 10 meeting %%
%% NOTE: We tried Redis but had memory issues %%
````

### Status Tags

Mark entire sections:

````markdown
## Authentication %% APPROVED %%
## Payment Processing %% WIP %%
## Admin Panel %% REVISE %%
## Legacy Code %% NO: too complex for v1 %%
````

|Tag|Meaning|Claude's Action|
|---|-------|---------------|
|`APPROVED`|Section is finalized|Don't modify|
|`WIP`|Work in progress|Can modify|
|`REVISE`|Needs improvement|Look for related comments|
|`NO: reason`|Rejected|Remove content|

## Comment Placement

### After Content

Most common - comment on what came before:

````markdown
The session timeout is 15 minutes.

%% Too short - increase to 30 %%
````

### Inline with Headers

Status tags work well after headers:

````markdown
## Pricing %% APPROVED %%
````

### Multiple Comments

You can have multiple comments in sequence:

````markdown
%% This looks good overall %%
%% But the error handling needs work %%
%% Also consider edge cases %%
````

## Responses

Claude responds with `•%%> response <%%•`:

````markdown
%% This section needs more detail %%

•%%>Added specific metrics: 99.9% uptime SLA,
<100ms p95 latency, 10K req/s capacity. <%%•
````

Each comment gets its own response:

````markdown
%% Is this the right approach? %%

•%%>Yes, this pattern is standard for auth flows. <%%•

%% What about token refresh? %%

•%%>Added refresh token handling in section below. <%%•
````

## Team Attribution

Add initials to track who said what:

````markdown
%% @JS: Can we simplify this? %%
%% @MK: APPROVED %%
%% @AL: Move to v2 roadmap %%
````

Or for group consensus:

````markdown
%% @ALL: Team agreed on this approach %%
````

## Best Practices

### Be Specific

````markdown
# Bad
%% Fix this %%

# Good
%% Change timeout from 15 to 30 minutes %%
````

### One Topic Per Comment

````markdown
# Bad
%% Fix timeout and add logging and update docs %%

# Good
%% Fix timeout - 15 → 30 minutes %%
%% Add request logging %%
%% Update API docs %%
````

### Use Questions for Decisions

````markdown
# When you need input
%% ?: Redis or Memcached for caching? %%

# When you have direction
%% Use Redis for caching %%
````

## Common Patterns

### Request Research

````markdown
%% Research competitors' rate limits and recommend %%
````

### Request Expansion

````markdown
%% Add more detail on error handling %%
````

### Request Simplification

````markdown
%% This is over-engineered - simplify %%
````

### Conditional Approval

````markdown
%% APPROVED if we add input validation %%
````

## See Also

* [Syntax Overview](../examples/sessions/index.md) - All marker types
* [Tokens](tokens.md) - Linking comments to specific text
* [Cleanup](cleanup.md) - Removing comments when done
