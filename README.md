# Document Iteration Skill

![License](https://img.shields.io/badge/license-MIT-green)
![Claude](https://img.shields.io/badge/for-Claude-orange)

A Claude skill for iterating on documents with feedback that lives **in the document**. You write comments next to the text. Claude answers next to them and updates the content. The discussion stays in the file, so it survives across sessions and devices, and git keeps track of it.

📚 **[Documentation](https://foksa.github.io/document-iteration-skill/)**: [install](https://foksa.github.io/document-iteration-skill/install) · [syntax](https://foksa.github.io/document-iteration-skill/syntax) · [editor setup](https://foksa.github.io/document-iteration-skill/editors)

## Example

You write:

```markdown
Uses ==PostgreSQL(DB)== with ==Redis(CACHE)==.

%%(DB) SQLite for v1 %%
%%(CACHE) NO: not needed for MVP %%
%% Also add a timeline %%
```

Claude updates the document and replies in place:

```markdown
Uses ==SQLite(DB)== for storage.

%%(DB) SQLite for v1 %%
•%%> Switched to SQLite: embedded, no server to run. <%%•

%%(CACHE) NO: not needed for MVP %%
•%%> Removed Redis. <%%•

%% Also add a timeline %%
•%%> Added a Timeline section below. <%%•

## Timeline
- Week 1: Core implementation
- Week 2: Testing and polish
```

When you're done, "clean up" removes every marker and keeps the content.

## Syntax at a glance

| You | Claude |
|-----|--------|
| `%% comment %%` | `•%%> response <%%•` |
| `==text(TOKEN)==` + `%%(TOKEN) comment %%` | `•%%> ?: question back <%%•` |
| `%% ?: question %%` · `%% NO: reason %%` · `%% APPROVED %%` · `%% NOTE: context %%` | `•%%> RISK: … <%%•` · `•%%> NOTE: … <%%•` |

The full list is in the [syntax reference](https://foksa.github.io/document-iteration-skill/syntax).

## Install

**Claude Code**: copy the skill folder into your project (or into `~/.claude/skills/` to use it everywhere):

```bash
git clone --depth 1 https://github.com/foksa/document-iteration-skill.git /tmp/dis
mkdir -p .claude/skills && cp -r /tmp/dis/document-iteration-skill .claude/skills/ && rm -rf /tmp/dis
```

**Claude.ai**: download [`document-iteration-skill.zip`](https://github.com/foksa/document-iteration-skill/releases/download/starter-kit/document-iteration-skill.zip) and upload it as a custom skill.

Then ask Claude in plain words:

```
> respond to the comments in docs/plan.md
> review docs/spec.md and add your feedback
> draft a proposal for dark mode
> clean up docs/plan.md
> set up VSCode highlighting for iteration markers
```

## Repository layout

```
document-iteration-skill/   # the skill; this folder is what you install
  SKILL.md
  references/               # syntax, examples, cleanup, editor setup
  scripts/cleanup.py        # deterministic marker removal (+ tests)
  assets/                   # document template, VSCode and Obsidian configs
docs/                       # GitHub Pages site
examples/                   # a real iteration session
```

## License

MIT
