# Document Iteration Skill

![Version](https://img.shields.io/badge/version-2.3-blue)
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
- `==marked text==(TOKEN)` eliminates ambiguity
- Git tracks every iteration
- Claude responds inline with `%% > answers %%`

---

## Quick Examples

### Software Development
```markdown
Uses ==PostgreSQL==(DB) with ==Redis==(CACHE) on ==AWS==(DEPLOY).

%%(DB) SQLite simpler for v1 %%
%%(CACHE) Memcached lighter weight %%
%%(DEPLOY) DigitalOcean cheaper %%
```

**Claude responds:**
```markdown
Uses ==SQLite==(DB) with ==Memcached==(CACHE) on ==DigitalOcean==(DEPLOY).

%%(DB) SQLite simpler for v1 %%
%% > Switched to SQLite! Perfect for early stage, easy migration path to PostgreSQL later. %%

%%(CACHE) Memcached lighter weight %%
%% > Changed to Memcached! 80% less memory than Redis for our simple caching needs. %%

%%(DEPLOY) DigitalOcean cheaper %%
%% > Moved to DigitalOcean! $12/month vs $50/month on AWS for our current scale. %%
```

### Creative Writing
```markdown
The hero ==defeats the dragon==(ENDING) and ==becomes king==(AFTERMATH).

%%(ENDING) Too cliché - make it a moral victory instead %%
%%(AFTERMATH) More interesting if they refuse the throne %%
```

**Claude responds:**
```markdown
The hero ==spares the dragon==(ENDING) and ==returns home==(AFTERMATH).

%%(ENDING) Too cliché - make it a moral victory instead %%
%% > Changed to sparing the dragon! The hero realizes the dragon was protecting 
its young. More powerful than another fight scene. %%

%%(AFTERMATH) More interesting if they refuse the throne %%
%% > Hero refuses the throne and goes home! Subverts expectations - true courage 
is choosing a simple life over power. %%
```

### General Planning
```markdown
Planning a ==weekend camping trip==(TRIP) for ==10 people==(SIZE).

%%(TRIP) 3-day trip better for experience %%
%%(SIZE) 6 people max - easier logistics %%
```

**Claude responds:**
```markdown
Planning a ==3-day camping trip==(TRIP) for ==6 people==(SIZE).

%%(TRIP) 3-day trip better for experience %%
%% > Extended to 3 days! Friday-Sunday gives time to actually relax vs. 
rushing everything into 2 days. %%

%%(SIZE) 6 people max - easier logistics %%
%% > Reduced to 6 people! Easier for:
- Tent arrangements (2 tents)
- Meal planning
- Single vehicle transport
- Group coordination %%
```

---

## Quick Start

### 1. Add the Skill to Claude
- Create a new Project in Claude.ai
- Add `SKILL.md` to your project files
- Claude will learn the syntax automatically

### 2. Use the Syntax
Create or edit any markdown document:

```markdown
Your content here with ==highlighted items==(TOKEN).

%%(TOKEN) Your feedback or questions %%
```

### 3. Get Claude's Response
Tell Claude: "I added feedback to [filename], please update it"

Claude will:
- Read your `%% comments %%`
- Respond with `%% > answers %%`
- Update the content based on feedback

### 4. Iterate
- Review Claude's changes
- Add more feedback or mark sections `%% APPROVED %%`
- Repeat until perfect
- Commit to git with full context preserved

---

## Syntax Overview

| You Write | Meaning |
|-----------|---------|
| `%% comment %%` | General feedback |
| `%% ?: question? %%` | Ask a question |
| `==text==(TOKEN)` | Mark specific text |
| `%%(TOKEN) comment %%` | Comment on that marked text |
| `%% APPROVED %%` | Lock this section (don't change) |
| `%% REVISE %%` | This needs improvement |
| `%% INFO: ... %%` | New information for Claude to use |
| `%% NOTE: ... %%` | Context (Claude reads, doesn't respond) |

| Claude Writes | Meaning |
|---------------|---------|
| `%% > response %%` | Response to your feedback |
| `>> NOTE: >> ` | Helpful background context |
| `>> RISK: >> ` | Potential issue to know about |
| `>> TIP: >> ` | Best practice suggestion |

**Complete reference:** See [SKILL.md](SKILL.md) for full syntax documentation and examples.

---

## Learn More

**📚 [Visit the Wiki](../../wiki)** for:
- Complete examples (Vue migration, API design, story editing)
- FAQ and troubleshooting
- Advanced usage patterns
- Contributing guidelines
- Development history

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

See [Contributing Guidelines](../../wiki/Contributing) for more.

---

**Built with ❤️ for better AI collaboration**

*Try it yourself: Add SKILL.md to a Claude project and start iterating on your documents!*
