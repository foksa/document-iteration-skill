# Examples

Input → output pairs. In each output: the user's comments stay in place, every comment has a `•%%>` response directly below it, content changes happen in the document itself, and highlighted text keeps its token when rewritten.

## 1. Token comment

Input:

```markdown
Uses ==PostgreSQL(DB)== for data storage.

%%(DB) Use SQLite instead - simpler for v1 %%
```

Output:

```markdown
Uses ==SQLite(DB)== for data storage — embedded, no separate server, easy to migrate to PostgreSQL later.

%%(DB) Use SQLite instead - simpler for v1 %%
•%%> Switched to SQLite and noted the migration path. <%%•
```

## 2. Several tokens, including NO:

Input:

```markdown
Session timeout is ==30 minutes(TTL)== using ==localStorage(STORE)==.

%%(TTL) Too long - use 15 minutes %%
%%(STORE) NO: not secure, use httpOnly cookies %%
```

Output:

```markdown
Session timeout is ==15 minutes(TTL)== using ==httpOnly cookies(STORE)==.

%%(TTL) Too long - use 15 minutes %%
•%%> Changed to 15 minutes. <%%•

%%(STORE) NO: not secure, use httpOnly cookies %%
•%%> Replaced localStorage with httpOnly cookies — not readable from JavaScript, so XSS can't steal the session. <%%•
```

## 3. General comment

Input:

```markdown
# API Design

%% Add rate limiting section %%

## Endpoints
...
```

Output:

```markdown
# API Design

%% Add rate limiting section %%
•%%> Added Rate Limiting below. <%%•

## Rate Limiting

- 100 requests/minute on the free tier
- 1000 requests/minute on paid tiers
- `429 Too Many Requests` when exceeded

## Endpoints
...
```

## 4. Status markers

Input:

```markdown
## Pricing %% APPROVED %%

$10/month basic plan.

## Features %% REVISE %%

- Feature A
- Feature B
```

Output — Pricing is reproduced exactly; Features is improved:

```markdown
## Pricing %% APPROVED %%

$10/month basic plan.

## Features %% REVISE %%
•%%> Added a description to each feature and a third feature. <%%•

- **Feature A** — what A does
- **Feature B** — what B does
- **Feature C** — new, covers the most common request
```

## 5. Mixed feedback with NOTE and a question

Input:

```markdown
# User Authentication

Use ==JWT tokens(AUTH)== with ==24-hour expiration(TTL)==.

%%(AUTH) APPROVED %%
%%(TTL) 1 hour is better, add refresh tokens %%
%% NOTE: Security review flagged long-lived tokens last quarter %%
%% ?: Do we need a password reset flow for v1? %%
```

Output — the APPROVED highlight is untouched, NOTE informs the change without its own reply:

```markdown
# User Authentication

Use ==JWT tokens(AUTH)== with ==1-hour access tokens and 7-day refresh tokens(TTL)==.

%%(AUTH) APPROVED %%
%%(TTL) 1 hour is better, add refresh tokens %%
•%%> Access tokens now expire after 1 hour; refresh tokens (7 days, rotated on use) keep users signed in. <%%•

%% NOTE: Security review flagged long-lived tokens last quarter %%
%% ?: Do we need a password reset flow for v1? %%
•%%> Yes — without it, a forgotten password means a support ticket. Added a minimal flow below. <%%•

## Password Reset

- Email with a single-use reset link (expires in 1 hour)
- New password form, then sign-in
```

## 6. Drafting a new document

Request: "Create a proposal for adding dark mode."

Output — Claude's own notes and questions use the Claude marker, so the user can reply to them inline with `%%`:

```markdown
# Dark Mode Proposal

•%%> NOTE: First draft — the questions below need your input. <%%•

## Overview

Add a dark mode toggle to settings, defaulting to the system preference.

## Implementation

Theme colors move to CSS variables, switched by a `data-theme` attribute on `<html>`.

•%%> ?: CSS variables, or Tailwind's `dark:` variant? Variables are framework-agnostic; Tailwind is less code if you already use it. <%%•
```

## 7. Review mode

Request: "Review this and give me feedback."

Input:

```markdown
We will migrate all services to Kubernetes in Q1.
```

Output — content stays as written; feedback is attached with Claude tokens:

```markdown
We will migrate ==all services(SCOPE)== to Kubernetes in ==Q1(WHEN)==.

•%%>(SCOPE) ?: All at once, or a pilot service first? A pilot surfaces networking and secrets issues early. <%%•
•%%>(WHEN) RISK: Q1 includes the holiday freeze — about 8 working weeks. <%%•
```
