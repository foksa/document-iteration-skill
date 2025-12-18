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

One of the strongest benefits is buried in the examples — the "bake and return" workflow:

1. Start iterating on an idea
2. Leave it (hours, days, weeks)
3. Return later — context is in the file, not lost to chat history

Current examples mention this in passing (`%% NOTE: rest of conversation occurred several hours later %%`) but don't emphasize it as a feature.

**Suggested additions:**
- Callout in docs: "Why this works: your context survives across sessions"
- Short example or case study showing: start → leave → return → continue seamlessly
- Contrast with chat-based iteration where context compresses and decisions get lost

This is a key differentiator worth highlighting early, not burying in examples.

## Files to Update

- `docs/getting-started/` — lead with basics only
- `docs/syntax/` — reorganize: basic → common → advanced
- `README.md` — simplify quick start section
- `document-iteration-skill/SKILL.md` — consider if advanced rules can be moved to references/

%% What do you think? Any other areas to address? %%
