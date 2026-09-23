---
title: Syntax
---

# Syntax

[Overview](index.md) · [Install](install.md) · **Syntax** · [Editor setup](editors.md)

## Two voices

| You write | Claude writes |
|-----------|---------------|
| `%% comment %%` | `•%%> response <%%•` |

Keeping the two apart shows who said what at a glance. It also lets the cleanup script remove both kinds of markers without touching anything else.

## Your markers

| Marker | Meaning |
|--------|---------|
| `%% comment %%` | Change request or feedback |
| `%% ?: question %%` | Question for Claude to answer |
| `%% INFO: fact %%` | New information for Claude to work into the content |
| `%% NOTE: context %%` | Background only; Claude reads it but doesn't reply |
| `%% NO: reason %%` | Remove this |
| `%% REVISE %%` | Improve this |
| `%% APPROVED %%` | Final; Claude leaves it as is |
| `%% WIP %%` | Still in progress; Claude flags it before cleanup |
| `%% @AB: comment %%` | Comment from a named team member |

A status marker on a heading applies to the whole section. Inline, it applies only to that text. On a line of its own, it applies to the block above it.

## Pointing at exact text

Wrap the text in a highlight with a token, then comment on the token:

```markdown
Uses ==PostgreSQL(DB)== on ==AWS(HOST)==.

%%(DB) SQLite for v1 %%
%%(HOST) ?: Would Fly.io be cheaper? %%
```

- Tokens can be anything unique: `(1)`, `(DB)`, `(DB-1)`, `(DB-a)`.
- If only one piece of text is highlighted, `==text==` with `%% * comment %%` is enough.
- When Claude rewrites highlighted text, it keeps the token (`==SQLite(DB)==`), so your comment still points at the right place.

## Claude's markers

```markdown
•%%> Response <%%•
•%%> ?: Question or suggestion for you <%%•
•%%> NOTE: Context <%%•
•%%> RISK: Potential problem <%%•
•%%> TIP: Recommendation <%%•
```

You can reply to any of these with a `%%` comment below it.

## Cleanup

Ask Claude to "clean up" or "finalize" the document. It counts the markers, warns you about any `WIP` sections and waits for your confirmation. Then it removes all `%%` and `•%%>` markers and unwraps highlights: `==PostgreSQL(DB)==` becomes `PostgreSQL`.

To finalize only the top of a file, put `%%!CLEANUP!%%` on its own line. Claude cleans everything above it and leaves the rest untouched.

You can also run the script yourself:

```bash
python3 .claude/skills/document-iteration-skill/scripts/cleanup.py --check docs/   # report; exits 1 if markers remain
python3 .claude/skills/document-iteration-skill/scripts/cleanup.py docs/plan.md     # clean in place
```

`--check` can also serve as a pre-commit or CI guard that stops markers from reaching published docs.
