---
name: document-iteration-skill
description: Inline, git-friendly feedback loop for markdown documents. The user writes `%% comments %%` and `==text(TOKEN)==` highlights in the file; Claude answers inside the file with `•%%> responses <%%•` and updates the content. Use when a document contains `%%` or `•%%>` markers, when the user asks to iterate on, respond to comments in, review, or clean up a document, when drafting a proposal/plan/spec the user will iterate on, or when setting up editor highlighting for these markers.
---

# Document Iteration

The document is the conversation. Feedback and answers live next to the text they are about, so the reasoning behind every change survives across sessions, devices, and collaborators, and git records all of it. Chat stays available for exploring; the document is where decisions get captured.

## Two voices

| Who | Writes | Purpose |
|-----|--------|---------|
| User | `%% comment %%`, `==text(TOKEN)==` + `%%(TOKEN) comment %%` | Feedback, questions, status |
| Claude | `•%%> response <%%•` | Answers, notes, questions back |

Every piece of text you add as a remark — replies, notes, questions, suggestions — goes inside `•%%> … <%%•`. This holds when you draft a brand-new document too: your draft notes are `•%%> NOTE: … <%%•` and your open questions are `•%%> ?: … <%%•`. Keeping the two voices distinct is what lets anyone reading the file see who said what, and lets the user's status markers (`APPROVED`, `NO:`, `REVISE`) stay authoritative.

Optional prefixes for your responses: `?:` (question or suggestion for the user), `NOTE:` (context), `RISK:` (potential problem), `TIP:` (recommendation).

## Processing a document

1. **Read the whole file** and collect every `%%` marker and every `==text(TOKEN)==`.
2. **Pair tokens**: each `%%(TOKEN)` refers to the `==…(TOKEN)==` with the same name.
3. **Edit the content** as the feedback asks.
4. **Answer every comment** with a `•%%> … <%%•` directly below it. The user's comment stays in place, so the comment + response pair forms the audit trail. The response is also the user's proof that the comment was seen, so add it even when the change itself speaks for itself.
5. **In chat**, give a short summary of what changed and which responses ask the user something. The substance lives in the document.

## What each marker asks for

| Marker | Your action |
|--------|-------------|
| `%% comment %%` | Apply the feedback, then respond below it |
| `%% ?: question %%` | Answer in a response; update content if the answer implies a change |
| `%% INFO: fact %%` | New information — update the content to reflect it, then respond |
| `%% NOTE: context %%` | Background for you — let it inform your edits; it needs no response |
| `%% NO: reason %%` | Remove the content it's attached to; respond with what you removed |
| `%% REVISE %%` | Improve that section; respond with what you changed |
| `%% APPROVED %%` | Locked — keep that content exactly as written |
| `%% WIP %%` | Still in progress — editable; flag it during cleanup |
| `%%(TOKEN) comment %%` | Feedback about the matching `==text(TOKEN)==` specifically |
| `%% @AB: comment %%` | Team comment — address the author by initials in your response |

`APPROVED`, `NO:` and `REVISE` scope: on a heading, the whole section; inline, just that text; on its own line, the preceding block.

Status markers are the user's decisions, so they are the user's to write. When you think something is ready, say so in a response (`•%%> ?: Ready to mark APPROVED? <%%•`).

## Tokens

- The form is always `==text(TOKEN)==`, with the token inside the closing `==`, one level deep.
- When you change highlighted text, keep its token: `==PostgreSQL(DB)==` → `==SQLite(DB)==`. The user's `%%(DB)` comment then still points at the right place.
- Tokens are unique per document. When a user comment references a token with no matching highlight, ask: `•%%> ?: I can't find ==…(TOKEN)== — where should this apply? <%%•`

## Example

Input:

```markdown
Uses ==PostgreSQL(DB)== with ==Redis(CACHE)==.

%%(DB) SQLite for v1 instead %%
%%(CACHE) NO: not needed for MVP %%
%% Also add a timeline %%
```

Output:

```markdown
Uses ==SQLite(DB)== for storage.

%%(DB) SQLite for v1 instead %%
•%%> Switched to SQLite — embedded, no server to run, easy to migrate later. <%%•

%%(CACHE) NO: not needed for MVP %%
•%%> Removed Redis. <%%•

%% Also add a timeline %%
•%%> Added a Timeline section below. <%%•

## Timeline

- Week 1: Core implementation
- Week 2: Testing and polish
```

More input → output pairs, including drafting a new document: [references/examples.md](references/examples.md).

## Modes

Pick the mode from what the user asks for:

- **Iterate** (default — "respond to comments", "iterate on this"): the full process above.
- **Ask first** ("check with me first", "how should we handle these?"): read the comments, then offer three options — respond inline only, respond and update the content, or discuss in chat first — and continue with the one they pick.
- **Review** ("review this", "give me feedback"): add `•%%>` comments where you have suggestions, questions, or concerns, using `==text(TOKEN)==` + `•%%>(TOKEN) … <%%•` for precise references. Content stays as the author wrote it.
- **Draft** ("write a proposal for X"): write the document, with your open questions and notes as `•%%>` markers so the user can reply to them inline.
- **Cleanup** ("clean up", "finalize", "remove markers"): see below.
- **Editor setup** ("set up highlighting for VSCode/Obsidian"): follow [references/editor-setup.md](references/editor-setup.md).

## Changes that need a yes

Moving, renaming, or deleting files goes through the user first: propose it in a response (`•%%> I'd move this to workflow/ — OK? <%%•`) and act once they confirm.

When the user asks you to move content from one of your responses into the document body, move it and shorten the response to `•%%> Done. <%%•`, so the content lives in one place.

If `%%` markers look like pre-existing content rather than feedback (for example, a document that documents this syntax, or Obsidian comments), ask before treating them as comments.

## Cleanup

Cleanup removes the iteration scaffolding and keeps the content. Highlighted text stays: `==PostgreSQL(DB)==` becomes `PostgreSQL`.

1. Run `python3 scripts/cleanup.py --check <file>` to count markers (paths are relative to this skill's folder).
2. Report the counts, name any `%% WIP %%` sections, and ask for confirmation.
3. After a yes, run `python3 scripts/cleanup.py <file>`, then read the result to confirm the formatting is intact.

A `%%!CLEANUP!%%` line means: clean from the top of the file through that line, and leave everything below it as is. The script cleans whole files, so do this one by hand. Details and a manual fallback: [references/cleanup.md](references/cleanup.md).

## Reference files

- [references/syntax.md](references/syntax.md) — full marker reference: token naming patterns, team comments, response prefixes.
- [references/examples.md](references/examples.md) — worked examples; read when the input doesn't obviously match the table above.
- [references/cleanup.md](references/cleanup.md) — cleanup details, partial cleanup, manual fallback.
- [references/editor-setup.md](references/editor-setup.md) — VSCode, Obsidian, JetBrains, and Vim highlighting.
- [assets/template.md](assets/template.md) — starter document.
