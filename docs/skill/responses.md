---
title: "Responses"
layout: default
---

# How Claude Responds

Understanding how Claude processes feedback and generates responses.

## Syntax Engine, Not Chat Assistant

Claude operates as a **Syntax Engine** when using this skill - NOT a conversational chat assistant. This means:

- ❌ Don't say: "I'll update the database section for you"
- ❌ Don't say: "Here's what I changed..."
- ✅ Do say: `%%>Updated to SQLite! <%%`

All responses go inline in the document using `%%> response <%%` syntax.

## The Response Format

Claude always responds with `%%> response <%%`:

```markdown
%% Your comment %%

%%>Claude's response <%%
```

The `%%>` opening and `<%%` closing distinguish Claude's responses from user comments.

## What Triggers a Response

Claude responds to:

| Pattern | Response Required |
|---------|-------------------|
| `%% comment %%` | Yes |
| `%% ?: question %%` | Yes |
| `%% INFO: data %%` | Yes (acknowledge and use) |
| `%%(TOKEN) comment %%` | Yes |
| `%% NOTE: context %%` | No (read-only) |
| `%% APPROVED %%` | Brief confirmation |

## Response Placement

Responses appear directly after the comment they address:

```markdown
%% Fix the timeout %%

%%>Fixed! Changed from 15 to 30 minutes. <%%

%% Add error handling %%

%%>Added try-catch with logging. <%%
```

For token-linked comments, responses follow each token:

```markdown
%%(DB) Use SQLite %%

%%>Updated to SQLite for v1. <%%

%%(CACHE) Add Redis %%

%%>Added Redis configuration. <%%
```

## Response Style

### Be Concise

Responses should be brief but informative:

```markdown
# Good - clear and concise
%%>Fixed typo: "recieve" → "receive" <%%

# Too verbose
%%>I have carefully reviewed the spelling error you pointed out
and have made the necessary correction to change "recieve"
to the correct spelling "receive" as per standard English. <%%
```

### Explain What Changed

Tell the user what you did:

```markdown
%% Add validation %%

%%>Added input validation:
- Email format check
- Password minimum 8 chars
- Username alphanumeric only <%%
```

### Answer Questions Directly

For questions, answer first, then elaborate:

```markdown
%% ?: Should we use JWT or sessions? %%

%%>JWT recommended. Reasons:
- Stateless = easier scaling
- Works well with API-first approach
- Built-in expiry handling <%%
```

## Thread Continuation

Conversations continue with new comments and responses:

```markdown
%% Is this approach scalable? %%

%%>Yes, this pattern handles 10K+ requests/sec. <%%

%% What about database bottlenecks? %%

%%>Good point. Added connection pooling and read replicas. <%%

%% APPROVED %%

%%>Thanks! Moving on to the next section. <%%
```

Each comment gets its own response.

## When NOT to Respond

### NOTE Tags

Notes are context-only. Don't respond:

```markdown
%% NOTE: Team decided this in meeting %%

# Claude reads this but doesn't add a response
```

### Approved Sections

Don't modify or comment on approved sections:

```markdown
## Pricing %% APPROVED %%

# Claude leaves this section alone
```

## Claude's Own Notes

Claude can add observations using `%%> NOTE: <%%` syntax:

```markdown
## Database Choice

Using PostgreSQL for the main database.

%%> NOTE: Consider adding read replicas for scaling <%%
%%> RISK: Current config has single point of failure <%%
```

These are Claude's proactive observations, not responses to user comments.

### When to Add Notes

- Important context the user should know
- Risks or gotchas
- Best practice recommendations
- Alternative approaches

### When NOT to Add Notes

- Obvious information
- Restating what's already in the document
- Minor suggestions that don't warrant highlighting

## Response and Action

Claude typically:
1. Responds to the comment first
2. Then updates the document content

```markdown
# Before
%% Add error handling %%

function process() {
  return data;
}

# After
%% Add error handling %%

%%>Added try-catch with error logging. <%%

function process() {
  try {
    return data;
  } catch (error) {
    console.error('Process failed:', error);
    throw error;
  }
}
```

The response stays even after the content is updated. It's the record of what was done.

## See Also

- [Mandatory Rules](mandatory-rules.md) - Response requirements
- [Comments](../syntax/comments.md) - User comment syntax
- [Customization](customization.md) - Override response behavior
