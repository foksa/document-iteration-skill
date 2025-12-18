# Docs Restructure Proposal

%% WIP %%

## Background: How This Proposal Came To Be

User asked a fresh Claude instance (no prior context) to review this repo and give an honest opinion. The agent explored the codebase, read the examples, and identified what the project does.

### Initial Assessment

The agent recognized the core value: a structured syntax for iterating on documents with Claude, solving context loss and vague feedback problems.

### Initial Concerns

1. **Learning curve** — Too much syntax presented at once (tokens, state markers, variants)
2. **Fragility** — Relies on Claude following rules precisely (LLM compliance issue)
3. **Adoption friction** — Skill install + editor setup + syntax learning before seeing value
4. **Niche** — Examples are all software-focused, seems specialized

### How Conversation Addressed These

Through back-and-forth, user provided context that reshaped the assessment:

1. **Learning curve** → Most usage is just `%%` and `•%%>`. Advanced features rarely needed. Solution: progressive disclosure in docs.

2. **Fragility** → Acknowledged as inherent LLM limitation. User has learned to live with it. Can't fully solve, but SKILL.md rules help.

3. **Adoption friction** → Reframed:
   - `%%` is Obsidian syntax — many users already know it
   - `•` bullet provides visual distinction without editor setup
   - Highlighting is optional polish, not prerequisite
   - Actual friction: copy skill folder, learn one marker

4. **Niche** → The *examples* are niche, not the syntax. `%%` works for any markdown. Show broader use cases in docs.

### Meta-Observation

The conversation itself demonstrated the workflow: iterating on ideas through feedback, refining understanding, ending with concrete output. The agent even made the exact mistake discussed (using `%%` instead of `•%%>`) — live proof of the LLM compliance issue.

---

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

## Broader Use Cases (add to docs)

Current examples are software-focused (specs, architecture). The syntax is universal — show it.

### Draft content for docs:

---

## Use Cases

Any document that benefits from structured feedback and revision history:

**Software** — Architecture docs, API specs, migration plans, code reviews
**Research** — Paper drafts, literature reviews, grant proposals, data analysis notes
**Writing** — Articles, stories, scripts, blog posts
**Education** — Lesson plans, course outlines, study guides, thesis drafts
**Planning** — Project proposals, event planning, strategy docs, meeting notes

The syntax is just markdown. If you can write `%%`, you can use this.

---

## Files to Update

- `docs/getting-started/` — lead with basics only
- `docs/syntax/` — reorganize: basic → common → advanced
- `README.md` — simplify quick start section
- `document-iteration-skill/SKILL.md` — consider if advanced rules can be moved to references/

%% What do you think? Any other areas to address? %%
