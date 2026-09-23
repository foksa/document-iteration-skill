# Syntax Reference

Complete list of iteration markers. SKILL.md covers the common cases; this file adds token naming patterns, team comments, and edge cases.

## User markers

### Comments and questions

```markdown
%% This section needs more detail %%
%% ?: Is 15 minutes too short for session timeout? %%
```

A comment asks for a change: apply it and respond. A question asks for an answer: answer it in a response, and update the content if the answer implies a change.

Comments can span multiple lines — everything between the opening and closing `%%` is one comment.

### Status markers

```markdown
## Pricing %% APPROVED %%
## Features %% REVISE %%
## Analytics %% NO: too complex for v1 %%
## Integrations %% WIP %%
```

| Marker | Meaning | Action |
|--------|---------|--------|
| `APPROVED` | Final | Keep the content exactly as written |
| `REVISE` | Needs work | Improve it; related comments may say how |
| `NO: reason` | Rejected | Remove the content; respond with what you removed |
| `WIP` | In progress | Editable; flag it before cleanup |

Scope: on a heading, the whole section; inline, just that text; on its own line, the preceding block.

### Information markers

```markdown
%% INFO: Budget increased to $200/month %%
%% NOTE: Team decided this in the Dec 10 meeting %%
```

- `INFO:` is new, actionable information. Update the content to reflect it, then respond.
- `NOTE:` is background. Use it to inform your edits; it needs no response.

### Highlights and tokens

Mark text with `==text(TOKEN)==`, then comment on it with `%%(TOKEN) … %%`:

```markdown
Uses ==PostgreSQL(DB)== with ==Redis(CACHE)== on ==AWS(DEPLOY)==.

%%(DB) SQLite for v1 instead %%
%%(CACHE) Memcached is lighter %%
%%(DEPLOY) DigitalOcean is cheaper %%
```

Single highlight shorthand — `*` refers to the one highlight just above:

```markdown
The session timeout is ==15 minutes==.

%% * Change to 30 minutes %%
```

Token naming patterns (all valid):

```markdown
Numbers:      ==text(1)==  ==text(2)==
Descriptive:  ==database(DB)==  ==caching(CACHE)==
Grouped:      ==PostgreSQL(DB-1)==  ==MySQL(DB-2)==
Insertions:   ==Item1(DB-1)==  ==NewItem(DB-a)==  ==Item2(DB-2)==
```

Rules:
- The token sits inside the closing `==`: `==text(TOKEN)==`.
- Highlights are one level deep.
- Each token appears once per document.
- When you rewrite highlighted text, keep its token so the user's comment still points at it.

### Team comments

```markdown
%% @JS: Can we simplify this? %%
%%(DB) @AL: Use SQLite for v1 %%
%% @ALL: Team consensus %%
```

Address the author in your response (`•%%> @JS: Simplified to … <%%•`). When authors disagree, lay out both positions in a response and let them decide.

## Claude markers

Every remark from Claude is wrapped in `•%%> … <%%•`. The bullet characters make Claude's voice visually distinct and let the cleanup script tell it apart from user comments.

```markdown
•%%> Response to feedback <%%•
•%%> ?: Question or suggestion for the user <%%•
•%%> NOTE: Background or context <%%•
•%%> RISK: Potential problem <%%•
•%%> TIP: Recommendation <%%•
•%%>(DB) Comment about ==…(DB)== (review mode) <%%•
```

Responses can span multiple lines.

## Special directives

| Marker | Meaning |
|--------|---------|
| `%%!CLEANUP!%%` | Clean everything from the top of the file through this line; leave the rest as is |

## Legacy format

Older documents may use `%%> response <%%` (without bullets). Treat it as a Claude response; the cleanup script removes both forms. New responses use the bullet form.
