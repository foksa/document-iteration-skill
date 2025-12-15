---
---

# Team Collaboration

Patterns for using the Document Iteration Skill with multiple people.

## Attribution

### Author Tags

Add initials to track who said what:

````markdown
%% @JS: This needs simplification %%
%% @MK: Agreed, too complex %%
%% @AL: I can refactor next sprint %%
````

### Response Attribution

Claude can acknowledge who made the comment:

````markdown
%% @JS: Add rate limiting %%

%%>@JS - Added rate limiting: 100 req/min standard,
1000 req/min for enterprise tier. <%%
````

### Group Tags

For team-wide decisions:

````markdown
%% @ALL: Team consensus - use PostgreSQL %%
%% @LEADS: Architecture review required %%
%% @SECURITY: Needs security audit %%
````

## Multi-Reviewer Workflows

### Sequential Review

Each reviewer adds their feedback, Claude responds to all:

````markdown
## Authentication Design

Use JWT with 1-hour expiry.

%% @JS: APPROVED %%
%% @MK: Add refresh tokens %%
%% @AL: Consider shorter expiry for sensitive ops %%
````

Claude responds:

````markdown
%% @JS: APPROVED %%

%%>Noted! <%%

%% @MK: Add refresh tokens %%

%%>Added 7-day refresh tokens with rotation. <%%

%% @AL: Consider shorter expiry for sensitive ops %%

%%>Good point. Added 5-minute tokens for payment operations. <%%
````

### Conflicting Feedback

When reviewers disagree, Claude flags it:

````markdown
%% @JS: Use REST API %%
%% @MK: Use GraphQL instead %%
````

Claude responds:

````markdown
%% @JS: Use REST API %%
%% @MK: Use GraphQL instead %%

%%>⚠️ Conflicting feedback from @JS and @MK.

REST pros: Simpler, better caching, wider tooling
GraphQL pros: Flexible queries, single endpoint, typed schema

Recommendation: REST for MVP, GraphQL for v2?
Please resolve before I proceed. <%%
````

### Approval Gates

Require multiple approvals:

````markdown
## Security Design %% NEEDS: @SECURITY @LEADS %%

...content...

%% @SECURITY: APPROVED %%
%% @LEADS: APPROVED %%
````

## Document Sections by Owner

### Section Assignment

Assign sections to specific people:

````markdown
## Frontend %% OWNER: @JS %%

## Backend %% OWNER: @MK %%

## Infrastructure %% OWNER: @AL %%
````

### Cross-Section Comments

When commenting on someone else's section:

````markdown
## Backend %% OWNER: @MK %%

Uses ==Redis(CACHE)== for session storage.

%% @JS: (cross-team) Frontend needs cache invalidation events %%
````

## Status Tracking Across Team

### Section Status Board

Track progress visually:

````markdown
## Status

| Section | Owner | Status |
|---------|-------|--------|
| Auth | @JS | %% APPROVED %% |
| Payments | @MK | %% WIP %% |
| Admin | @AL | %% REVISE %% |
````

### Blocking Issues

Flag items that block others:

````markdown
%% @MK: BLOCKED - waiting on @JS for auth tokens spec %%
````

### Handoffs

Explicit handoff between team members:

````markdown
%% @JS: Done with auth design, @MK please review %%

%%>Handoff noted. @MK has the ball. <%%
````

## Git Workflow Integration

### Branch-Based Review

Each reviewer works on their branch:

````
main
├── review/js-auth-feedback
├── review/mk-api-feedback
└── review/al-infra-feedback
````

Merge reviews into main, resolve conflicts in the document.

### Commit Messages

Include reviewer info:

````
docs: Add @JS feedback on auth section

- Added comments on JWT expiry
- Flagged rate limiting concern
- Approved session handling
````

### PR-Based Review

1. Author creates document with `%% WIP %%` sections
1. Opens PR for review
1. Reviewers add `%% @INITIALS: comment %%` inline
1. Author (or Claude) responds to all comments
1. Final `%% APPROVED %%` tags added
1. Cleanup before merge

## Best Practices

### Establish Conventions

Document your team's patterns:

````markdown
# Team Conventions

- Use @INITIALS (2-3 letters) for attribution
- @ALL for team consensus
- @SECURITY for security-sensitive items
- Final approver adds %% APPROVED %%
````

### Keep Threads Focused

One topic per comment thread:

````markdown
# Good
%% @JS: Rate limiting is too low %%
%% @JS: Also need request logging %%

# Harder to track
%% @JS: Rate limiting is too low and we need request logging %%
````

### Clean Up Resolved Discussions

After team alignment, clean up the back-and-forth:

````markdown
# Before cleanup (shows full discussion)
%% @JS: Use REST %%
%% @MK: GraphQL better %%
%% @JS: OK, GraphQL works %%
%% @ALL: APPROVED - GraphQL %%

# After cleanup (clean document)
Uses GraphQL API.
````

## Configuring Team Mode

Add to your `.claude.md`:

````markdown
## Team Mode Rules

1. Always include author attribution in responses
2. Flag conflicts: "⚠️ @X and @Y have conflicting feedback"
3. Don't modify sections owned by others without @mention
4. Require @ALL or multiple approvals for architecture changes
````

See *Customization* for more configuration options.

## See Also

* *Customization* - Configure team rules
* *First Iteration* - Basic workflow
* *Examples* - More patterns
