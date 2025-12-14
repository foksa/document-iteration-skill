---
title: "_Docs Reorganization Plan"
layout: default
---

# Documentation Reorganization Plan

**Status:** ✅ COMPLETE
**Not linked from index** - internal planning document

---

## Current State

18 documentation files across 4 folders:
- Root: 7 files (index, FAQ, Examples, Contributing, Installation, SKILL, mandatory-rules)
- syntax/: 3 files (index, tokens, cleanup)
- workflows/: 1 file (customization) + auto-cleanup subfolder
- workflows/auto-cleanup/: 5 files (index, claude-check, git-hooks, ci-cd, editor-integration, lint-rules)
- workflow-examples/: 1 file (Obsidian Workflow)

## Issues Identified

### 1. Structural Inconsistencies
- `mandatory-rules.md` is at root but describes skill behavior - should be with skill docs
- `workflow-examples/` folder has only one file in deep nesting
- `customization.md` is in workflows/ but relates more to skill configuration
- Examples.md still has iteration markers (not cleaned up)

### 2. Missing Documentation
- **Quick Start Guide** - Installation jumps straight to commands, no "your first iteration" walkthrough
- **Use Cases** - README mentions them but no detailed docs
- **Best Practices** - How to use effectively (when to use tokens, response style)
- **Claude Code Integration** - Specific guide for Claude Code users vs claude.ai users ✓ (created claude-ai.md)
- **Troubleshooting** - FAQ has some, but needs expansion

### 3. Content Gaps
- No clear path from "I installed this" to "I'm using it effectively"
- Examples are good but lack progression (simple → complex)
- Missing: How to handle conflicts, multi-person workflow details

### 4. Organization Issues
- Syntax docs are good but scattered
- "Skill Behavior" section in index has only one item
- workflow-examples folder name doesn't match pattern (kebab-case vs others)

---

## Proposed New Structure

```
docs-source/obsidian/
├── index.md                    # Landing page
├── getting-started/            # NEW FOLDER - Onboarding path
│   ├── index.md               # Quick start overview
│   ├── installation.md        # Moved from root
│   ├── first-iteration.md     # NEW - Your first document iteration
│   └── claude-code.md         # NEW - Claude Code specific setup
│
├── syntax/                     # Keep as-is, good structure
│   ├── index.md
│   ├── comments.md            # NEW - Deep dive on %% %%
│   ├── highlights.md          # NEW - Deep dive on ==text==(TOKEN)
│   ├── tokens.md              # Keep
│   ├── notes.md               # NEW - The >> >> syntax
│   └── cleanup.md             # Keep
│
├── skill/                      # NEW FOLDER - How Claude behaves
│   ├── index.md               # Overview of skill behavior
│   ├── mandatory-rules.md     # Moved from root
│   ├── responses.md           # NEW - How Claude responds
│   └── customization.md       # Moved from workflows/
│
├── workflows/                  # Integration & automation
│   ├── index.md               # NEW - Overview of workflows
│   ├── auto-cleanup/          # Keep as-is
│   │   ├── index.md
│   │   ├── claude-check.md
│   │   ├── git-hooks.md
│   │   ├── ci-cd.md
│   │   ├── editor-integration.md
│   │   └── lint-rules.md
│   └── team-collaboration.md  # NEW - Multi-person workflows
│
├── examples/                   # NEW FOLDER - Expanded examples
│   ├── index.md               # Overview
│   ├── software.md            # Software dev examples
│   ├── writing.md             # Creative writing examples
│   ├── planning.md            # Project planning examples
│   └── complete-session.md    # NEW - Full iteration from start to finish
│
├── reference/                  # NEW FOLDER
│   ├── faq.md                 # Moved, expanded
│   ├── troubleshooting.md     # NEW - Problem solving
│   └── best-practices.md      # NEW - Tips for effective use
│
├── meta/                       # NEW FOLDER - About the docs themselves
│   ├── contributing.md        # Moved
│   └── obsidian-workflow.md   # Moved from workflow-examples/
│
└── SKILL.md                    # Keep at root for direct link
```

---

## New Pages to Create

### Priority 1 - Core Gaps
1. **getting-started/first-iteration.md** - Step-by-step "your first doc"
2. **examples/complete-session.md** - Full iteration soup to nuts
3. **reference/troubleshooting.md** - Expanded problem solving

### Priority 2 - Depth
4. **syntax/comments.md** - Deep dive on comment syntax
5. **syntax/highlights.md** - Deep dive on highlighting
6. **skill/responses.md** - How Claude responds and why

### Priority 3 - Advanced
7. **workflows/team-collaboration.md** - Multi-person patterns
8. **getting-started/claude-code.md** - Claude Code specific guide
9. **reference/best-practices.md** - Tips and patterns

---

## Migration Steps

### Phase 1: Create folder structure ✓ DONE
- ~~Create `getting-started/`, `skill/`, `examples/`, `reference/`, `meta/`~~
- ~~Move existing files to new locations~~
- ~~Update all internal links~~

### Phase 2: Create priority 1 content ✓ DONE
- ~~Write first-iteration.md~~ ✓
- ~~Clean up Examples.md threads~~ ✓
- ~~Expand troubleshooting~~ ✓ (added "Claude removed my comment" entry + wrong/right example in mandatory-rules)
- ~~Write complete-session.md~~ ✓ (created examples/sessions/ with api-design.md and migration-plan.md)
- ~~Add index pages~~ ✓ (getting-started, skill, reference, examples, examples/sessions)
- ~~Clean up resolved threads~~ ✓ (claude-check.md, customization.md, mandatory-rules.md)

### Phase 3: Create priority 2-3 content ✓ DONE
- ~~syntax/comments.md~~ ✓
- ~~syntax/highlights.md~~ ✓
- ~~skill/responses.md~~ ✓
- ~~workflows/team-collaboration.md~~ ✓
- ~~reference/best-practices.md~~ ✓
- ~~workflows/index.md~~ ✓
- ~~Update all index pages with new links~~ ✓

### Phase 4: Polish ✓ DONE
- ~~Update index.md with new structure~~ ✓
- ~~Verify all links work~~ ✓
- ~~Review documentation for consistency~~ ✓

---

## Questions for Review

1. Is the new structure clearer?
2. Should `skill/` folder have a different name? (behavior? rules?)
3. Is splitting examples into multiple files worthwhile? → Keep Examples.md as main, link to larger examples
4. Should we keep SKILL.md at root or move to skill/? → Keep at root
5. Any pages listed that aren't needed? → OK for now
6. Any pages missing from the plan? → OK for now

---

## What's Next?

Documentation reorganization complete! Optional future work:
- Consider adding syntax/notes.md for `>> >>` syntax
- Add more session examples as use cases emerge

---

## Notes

- Keep SKILL.md at root since README links to it
- The underscore prefix `_` in this filename prevents it from being processed/linked
- This plan can be iterated using the skill itself!