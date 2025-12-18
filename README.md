# Document Iteration Skill

![Version](https://img.shields.io/badge/version-5.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude](https://img.shields.io/badge/for-Claude%20AI-orange)

A lightweight protocol for document-centric collaboration with AI.

While optimized for Claude, the syntax works with any AI that follows structured instructions.

> 📚 **[Full Documentation](https://foksa.github.io/document-iteration-skill/)** — Installation, syntax reference, examples, and FAQ.

---

## The Problem (10 seconds)

**Without structured feedback:**
```
You: Can you revise the part about the database?
Claude: Sure! Here's the revised version...
You: No, I meant the OTHER part about the database
Claude: Which section specifically?
You: The one we discussed yesterday
Claude: I don't have context from previous sessions...
```

**With Document Iteration Skill:**

**Structured** — Feedback lives with the content, not lost in chat:

    %% We need way to keep user data %%
    •%%> Simple solution is good enough <%%•

    Save user data in local storage.

**Persistent** — A week later, requirements changed:

    %% We need way to keep user data %%
    •%%> Simple solution is good enough <%%•

    Save user data in local storage.

    %% Our testing shows that users need to sync data between multiple devices %%
    •%%> Adding sync solution... <%%•

    Uses PostgreSQL with Redis for sync

Your feedback and Claude's response are still there. Any device, any session.

**Precise** — Now "the database" is ambiguous (PostgreSQL? Redis?):

    Uses ==PostgreSQL(DB)== with ==Redis(CACHE)==.

    %%(DB) Switch to SQLite for v1 %%
    %%(CACHE) NO: remove caching for MVP %%

TOKENs point to exact text. No confusion about what to change.

---

## How It Works

Chat explores. Documents capture. Use both:

1. **Explore in chat** — Brainstorm, ask questions, figure out direction
2. **Draft a document** — "Create a proposal for X"
3. **Iterate with markers** — Add `%% feedback %%`, Claude responds inline
4. **Back to chat when needed** — Discuss, clarify, then return to doc
5. **Cleanup** — Remove all markers, keep the content

---

## 30-Second Example

**1. You add a comment to your document:**
```markdown
## Project Plan

This project will take approximately 6 months.

%% Too vague - add specific phases %%
```

**2. Claude updates the document and responds inline:**
```markdown
## Project Plan

This project spans three phases:
- Phase 1 (Months 1-2): Research and design
- Phase 2 (Months 3-4): Implementation
- Phase 3 (Months 5-6): Testing and launch

%% Too vague - add specific phases %%
•%%> Added three phases with timeframes. <%%•
```

Your comment stays. Claude's response added. Content updated. Git tracks it all.

---

## Syntax

### Basic (90% of usage)

| You Write | Claude Writes |
|-----------|---------------|
| `%% comment %%` | `•%%> response <%%•` |

### Common Patterns

| Pattern               | Use For                              |
| --------------------- | ------------------------------------ |
| `%% ?: question %%`   | Ask Claude something                 |
| `%% NOTE: context %%` | Info for Claude (no response needed) |
| `%% WIP %%`           | Mark incomplete sections             |

### Precision with Tokens

Mark specific text, comment on it by name:
```markdown
Uses ==PostgreSQL(DB)== with ==Redis(CACHE)==.

%%(DB) Switch to SQLite %%
%%(CACHE) NO: remove for MVP %%
```

### Advanced Syntax

`APPROVED`, `REVISE`, `INFO`, response variants (`?: `, `RISK:`, `NOTE:`) → [Full Reference](https://foksa.github.io/document-iteration-skill/syntax/)

---

## When to Use (and When Not To)

**Use this when:**
- Document goes through multiple revisions
- Precision matters (specs, plans, contracts)
- You want audit trail of decisions
- Team members will add feedback

**Skip this for:**
- Quick brainstorming (just chat)
- Short texts (just describe what you want)
- Exploratory conversations (you're still figuring it out)

**Tip:** Start in chat to explore, then say "draft me a proposal" to switch to iteration mode.

---

## Quick Start (Claude Code)

Copy-paste one of the [setup prompts](prompts/README.md) into Claude Code, or manually:

```bash
git clone https://github.com/foksa/document-iteration-skill.git
mkdir -p your-project/.claude/skills
cp -r document-iteration-skill/document-iteration-skill your-project/.claude/skills/
```

Then in Claude Code:
```
> look at docs/plan.md and respond to comments
> cleanup markers in docs/plan.md
```

**Alternative:** Add `SKILL.md` to a Claude.ai Project for web-based iteration.

---

## Why Not Just Chat?

| Chat Comments | Document Markers |
|---------------|------------------|
| Lost in scroll | Stays with content |
| "Fix section 3" | `%%(DB) use SQLite %%` |
| Context disappears | Audit trail preserved |
| Session-locked | Works across sessions/devices |

---

## Use Cases

- **Software**: Architecture docs, API specs, migration plans
- **Writing**: Articles, scripts, documentation
- **Research**: Paper reviews, analysis summaries
- **Planning**: Projects, roadmaps, strategies
- **Education**: Lesson plans, curriculum

If you iterate on documents with Claude, this makes it precise and trackable.

---

## Learn More

- [Syntax Reference](https://foksa.github.io/document-iteration-skill/syntax/)
- [Examples](https://foksa.github.io/document-iteration-skill/examples)
- [Workflows](https://foksa.github.io/document-iteration-skill/workflows/)
- [FAQ](https://foksa.github.io/document-iteration-skill/reference/faq)

**If Claude ignores markers:** Ask it to re-scan the document and follow the iteration syntax.

---

## License

MIT License — use freely, attribution appreciated.

---

## Contributing

- [Report bugs](../../issues)
- [Request features](../../issues)
- [Contributing Guidelines](https://foksa.github.io/document-iteration-skill/meta/contributing)

---

**Built for better AI collaboration**

*Add SKILL.md to a Claude project and start iterating!*
