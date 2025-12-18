# Docs Restructure Proposal

%% WIP %%

## Problem

Current docs present all syntax features at once. Users see tokens, APPROVED/REVISE, INFO/NOTE variants, etc. before understanding the basics.

In practice, most usage is just:
- `%% comment %%` — user feedback
- `•%%> response <%%•` — Claude response

Advanced features (tokens, state markers) are rarely needed but clutter the initial learning experience.

## Proposed Structure

### 1. Quick Start (front and center)

```markdown
## Basic Syntax — This is 90% of what you need

**You write:**
%% your feedback here %%

**Claude responds:**
•%%> response to your feedback <%%•

That's it. Start iterating.
```

### 2. Common Patterns (second)

- `%% ?: question %%` — asking Claude something
- `%% NOTE: context %%` — information Claude should know but not respond to
- `%% WIP %%` — mark incomplete sections

### 3. Advanced Features (later, for those who need them)

**Precision tokens** — when you have multiple similar items:
```markdown
Uses ==PostgreSQL(DB)== and ==Redis(CACHE)==.
%%(DB) use SQLite instead %%
```

**State markers** — for formal review workflows:
- `%% APPROVED %%` — lock section
- `%% REVISE %%` — needs rework
- `%% NO: reason %%` — remove content

**Claude response variants:**
- `•%%> NOTE: <%%•` — background info
- `•%%> ?: <%%•` — suggestions
- `•%%> RISK: <%%•` — warnings

## Principle

Progressive disclosure:
1. Simple → works for most cases
2. Hit a wall → discover advanced feature exists
3. Use it → only when needed

Docs should mirror how people actually learn, not how features were designed.

## Highlight: Context Survives Across Sessions

One of the strongest benefits is buried in the examples. Current examples mention this in passing (`%% NOTE: rest of conversation occurred several hours later %%`) but don't emphasize it as a feature.

This is a key differentiator worth highlighting early, not burying in examples.

### Draft content for docs:

---

## Why This Works: Your Context Survives

Traditional chat-based iteration has two problems:

1. **Time decay** — Long conversations compress, early decisions get forgotten
2. **Device lock-in** — Chat history lives in one session, one device

Document iteration solves both:

### Survives Time
- Iterate on an idea Monday
- Leave it to "bake"
- Return Thursday (or next month) — everything is there
- No context compression, no lost decisions

### Survives Place
- Start on your desktop
- Continue from your phone
- Pick it up in web UI
- The document is the anchor, not the chat

### The Audit Trail Bonus
Every decision is recorded *with its reasoning*:
- Not just "use SQLite" but *why* (no server needed for v1)
- Not just "removed caching" but *why* (not needed for MVP)

When you return later, you don't just see *what* was decided — you see *why*.

---

## Design Rationale (add to docs)

### Draft content for docs:

---

## Why These Markers?

**Why `%%`?**
It's Obsidian's comment syntax. If you already use Obsidian, you know it.
Even without Obsidian, `%%` is easy to type and visually distinct.

**Why `•%%>` for Claude?**
The bullet (•) makes Claude's responses visually different from yours —
no editor highlighting needed. It also can't be typed accidentally
(it's not on standard keyboards), so you won't mix up who said what.

If you need to fake a Claude response (for templates/examples), copy-paste it.

**Do I need editor highlighting?**
No. It's optional polish. The syntax works standalone in any text editor.
The bullet already provides visual distinction.

Editor configs are nice-to-have for long sessions, not a prerequisite.

---

## Files to Update

- `docs/getting-started/` — lead with basics only
- `docs/syntax/` — reorganize: basic → common → advanced
- `README.md` — simplify quick start section
- `document-iteration-skill/SKILL.md` — consider if advanced rules can be moved to references/

%% What do you think? Any other areas to address? %%
