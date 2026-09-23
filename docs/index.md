---
title: Overview
---

# Document Iteration Skill

A Claude skill for iterating on documents with feedback that lives **in the document**. You write comments next to the text. Claude answers next to them and updates the content. The whole discussion stays in the file, so it survives across sessions and devices and git keeps track of it.

[Install](install.md) · [Syntax](syntax.md) · [Editor setup](editors.md) · [GitHub](https://github.com/foksa/document-iteration-skill)

## The idea in 30 seconds

You add a comment:

```markdown
This project will take approximately 6 months.

%% Too vague, add phases %%
```

You ask Claude to "respond to the comments in plan.md". Claude edits the text and replies directly below your comment:

```markdown
This project runs in three phases:
- Months 1–2: research and design
- Months 3–4: implementation
- Months 5–6: testing and launch

%% Too vague, add phases %%
•%%> Split into three phases with timeframes. <%%•
```

To point at exact words, mark them with a token:

```markdown
Uses ==PostgreSQL(DB)== with ==Redis(CACHE)==.

%%(DB) SQLite for v1 %%
%%(CACHE) NO: not needed for MVP %%
```

When the document is final, ask Claude to "clean up plan.md". The markers go and the content stays.

## When to use it

It works well for documents that go through several rounds: specs, plans, proposals, API designs and articles. It also helps when several people give feedback, or when you want a record of why each decision was made.

For quick questions and early brainstorming, plain chat is simpler. A good pattern is to explore in chat first, then say "draft a proposal for this" and iterate on the document from there.

## Why not just chat?

| Chat | Document markers |
|------|------------------|
| Feedback scrolls away | Feedback stays next to the text |
| "Fix the database part" | `%%(DB) use SQLite %%` |
| Tied to one session | Works in any session, on any device |
| History lost | History in git until you clean it up |
