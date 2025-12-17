# Document Iteration Skill

![Version](https://img.shields.io/badge/version-5.2-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude](https://img.shields.io/badge/for-Claude%20AI-orange)

A structured markdown syntax for iterating on documents with Claude AI.

---

## Why This Exists

**The Problem:**
Working with AI on documents usually means:
- Vague feedback in chat ("change section 3")
- Lost context as conversation grows
- No version control for iterations
- Ambiguous comments ("make it better")

**The Solution:**
Add structured feedback directly in documents:
- `%% precise comments %%` stay with the content
- `==marked text(TOKEN)==` eliminates ambiguity
- Git tracks every iteration
- Claude responds inline with `•%%>answers <%%•`

---

## Quick Examples

### Document Drafting
```markdown
## Project Overview

This project will take approximately 6 months to complete.

%% Too vague - add specific phases and milestones %%
```

**Claude responds:**
```markdown
## Project Overview

This project spans three phases:
- Phase 1 (Months 1-2): Research and design
- Phase 2 (Months 3-4): Core implementation
- Phase 3 (Months 5-6): Testing and launch

%% Too vague - add specific phases and milestones %%
•%%> ✓: Added three phases with specific timeframes. <%%•
```

### Code Review
```markdown
def calculate_total(items):
    total = 0
    for item in items:
        total += item.price
    return total

%% ?: Should this handle empty lists? %%
%% Add discount parameter %%
```

**Claude responds:**
```markdown
def calculate_total(items, discount=0):
    if not items:
        return 0
    total = sum(item.price for item in items)
    return total * (1 - discount)

%% ?: Should this handle empty lists? %%
•%%> ✓: Yes - added early return for empty lists. <%%•

%% Add discount parameter %%
•%%> ✓: Added optional discount parameter (0-1 range). <%%•
```

### With Tokens (Advanced)
For precise references, use `==text(TOKEN)==`:

```markdown
Uses ==PostgreSQL(DB)== for storage.

%%(DB) SQLite simpler for v1 %%
```

**Claude responds:**
```markdown
Uses ==SQLite(DB)== for storage.

%%(DB) SQLite simpler for v1 %%
•%%> ✓: Switched to SQLite. Easy migration to PostgreSQL later. <%%•
```

---

## Quick Start (Claude Code)

1. **Get the skill:** Copy `document-iteration-skill/` to your project:
   ```bash
   git clone https://github.com/foksa/document-iteration-skill.git
   mkdir -p your-project/.claude/skills
   cp -r document-iteration-skill/document-iteration-skill your-project/.claude/skills/
   ```
2. **Add comments to any markdown file:**
   ```markdown
   Some content here.

   %% Make this more concise %%
   ```
3. **Run Claude Code:** `claude "respond to comments in my-file.md"`
4. **Review and iterate** - Claude edits the file directly

### Workflow
```bash
# Start Claude Code in your project
cd my-project
claude

# Iterate on documents
> look at docs/plan.md and respond to comments
> cleanup markers in docs/plan.md
```

---

## Alternative: Claude.ai Projects

For web-based iteration:

1. Create a Project in Claude.ai
2. Add `SKILL.md` to project files
3. Upload your document with `%% comments %%`
4. Ask Claude to respond to feedback

---

## Syntax Overview

| You Write | Meaning |
|-----------|---------|
| `%% comment %%` | General feedback |
| `%% ?: question? %%` | Ask a question |
| `==text(TOKEN)==` | Mark specific text |
| `%%(TOKEN) comment %%` | Comment on that marked text |
| `%% APPROVED %%` | Lock this section (don't change) |
| `%% REVISE %%` | This needs improvement |
| `%% NO: reason %%` | Remove this content |
| `%% INFO: ... %%` | New information for Claude to use |
| `%% NOTE: ... %%` | Context (Claude reads, doesn't respond) |

| Claude Writes | Meaning |
|---------------|---------|
| `•%%>response <%%•` | Response to your feedback |
| `•%%> NOTE: <%%•` | Helpful background context |
| `•%%> RISK: <%%•` | Potential issue to know about |
| `•%%> ?: <%%•` | Suggestion for user to consider |

**Complete reference:** See [SKILL.md](document-iteration-skill/SKILL.md) for full syntax documentation and examples.

**Cleanup:** When done iterating, ask Claude to "cleanup" - markers are removed, highlighted text is preserved. See [Cleanup Workflow](https://foksa.github.io/document-iteration-skill/syntax/cleanup) for details.

---

## Learn More

**📚 [Documentation](https://foksa.github.io/document-iteration-skill/)** - Full guides and reference:
- [Syntax Overview](https://foksa.github.io/document-iteration-skill/syntax/) - All marker types
- [Examples](https://foksa.github.io/document-iteration-skill/examples) - Real-world usage patterns
- [Workflows](https://foksa.github.io/document-iteration-skill/workflows/) - Customization and auto-cleanup
- [FAQ](https://foksa.github.io/document-iteration-skill/reference/faq) - Common questions


---

## Use Cases

This syntax works for any iterative document work:
- 💻 **Software**: Architecture docs, API specs, migration plans
- ✍️ **Writing**: Stories, articles, scripts, documentation
- 📊 **Research**: Paper reviews, analysis, literature summaries
- 📋 **Planning**: Projects, events, roadmaps, strategies
- 🎓 **Education**: Lesson plans, curriculum, study guides

If you're iterating on a document with Claude, this syntax makes it precise and trackable.

---

## Why Not Just Use Comments in Chat?

| Chat Comments | This Syntax |
|---------------|-------------|
| ❌ Lost in history | ✅ Stays with content |
| ❌ Vague ("fix section 3") | ✅ Precise (`==(TOKEN)`) |
| ❌ No version control | ✅ Git tracks everything |
| ❌ Context disappears | ✅ Audit trail preserved |
| ❌ Hard to collaborate | ✅ Team can add feedback |

### vs Other Approaches

| Method | Precise? | Persistent? | Git-Friendly? |
|--------|----------|-------------|---------------|
| Chat comments | ❌ Vague | ❌ Lost | ❌ No |
| Google Docs comments | ✅ Good | ✅ Yes | ❌ No |
| GitHub PR reviews | ✅ Line-level | ✅ Yes | ✅ Yes |
| **This syntax** | ✅✅ Tokens | ✅ In document | ✅✅ Native markdown |

---

## License

MIT License - use freely, attribution appreciated.

See [LICENSE](LICENSE) for details.

---

## Contributing

Found a bug? Have a suggestion? 

- 🐛 [Report bugs](../../issues/new?template=bug_report.md)
- 💡 [Request features](../../issues/new?template=feature_request.md)
- ❓ [Ask questions](../../issues/new?template=question.md)

See [Contributing Guidelines](https://foksa.github.io/document-iteration-skill/meta/contributing) for more.

---

**Built with ❤️ for better AI collaboration**

*Try it yourself: Add SKILL.md to a Claude project and start iterating on your documents!*
