# Document Iteration Skill - Project Guide

## Overview

This repo contains the Document Iteration Skill, a markdown syntax for iterating on documents with Claude. The skill itself is `document-iteration-skill/`. Everything else supports it.

## Repository Structure

```
document-iteration-skill/     # The skill (what users install)
  SKILL.md                    # Core instructions, kept short
  references/                 # Loaded on demand: syntax, examples, cleanup, editor-setup
  scripts/cleanup.py          # Deterministic cleanup; tests in scripts/test/
  assets/                     # template.md, editor-configs/{vscode,obsidian}
docs/                         # GitHub Pages site (Jekyll): index, install, syntax, editors
examples/                     # Real iteration sessions
```

## Writing skill instructions

- Say what Claude should do, and give the reason in a short clause. Avoid "never / don't / do not". Negations lose their force as context grows, and the reason lets the model apply the rule to new cases.
- Show correct output only. A worked example of wrong output tends to get copied.
- Keep SKILL.md focused on the core loop. Put details in `references/` and link each file with a note on when to read it.
- The `description` frontmatter decides when the skill triggers, so keep the trigger phrases in it current.

## Iteration Markers

When editing markdown in this repo, use the skill's own syntax:

- `%% user comment %%`: user feedback (muted gold, `#968748`)
- `•%%> AI response <%%•`: AI responses (teal, `#3C8C8C`)
- `==text(TOKEN)==` + `%%(TOKEN) comment %%`: precise references

Files that document the syntax contain markers as literal examples.

## Commands

```bash
# Test cleanup script
bash document-iteration-skill/scripts/test/run-tests.sh

# Install locally for testing
cp -r document-iteration-skill ~/.claude/skills/
```

## GitHub Actions

- `package-skill.yml`: runs the tests, then zips `document-iteration-skill/` into the `starter-kit` release as `document-iteration-skill.zip`
- `pages.yml`: deploys `docs/` to GitHub Pages
