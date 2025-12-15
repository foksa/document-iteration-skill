---
---

# Project Setup Prompt Session

A real-world iteration session creating a reusable project setup prompt for Claude. This session demonstrates the full workflow from initial idea to polished output.

## Session Overview

**Goal**: Create a prompt template that sets up new software projects with the Document Iteration Skill, dual Obsidian vaults, and GitHub Pages deployment.

**Duration**: Multiple rounds of iteration
**Outcome**: Clean prompt template + preserved iteration history

## Round 1: Initial Request

User starts with a high-level idea:

````markdown
%% WIP %%

## Goal

%%
Help me write project prompt for claude

Its starts in empty folder

I want to have
- this claude skill installed
- docs-draft - obsidian vault for docs similar to our here
- docs - pure markdown converted from docs
- work-docs - another obsidian vault for implementation discussions

Write me tech proposal that we can iterate on and convert to prompt

Ask any question you need, or feel free to extend initial idea as you see fit
%%
````

Claude responds with a proposed structure and asks clarifying questions using the `?: ` question syntax.

## Round 2: Clarification Questions

Claude asks several questions to understand the requirements:

````markdown
•%%> ?: **Conversion workflow**: Should `docs-draft/` → `docs/` conversion happen automatically (GitHub Action) or manually (run script)? <%%•

%%
I want conversation to happen locally
I want to:
use python script from skill to clear iteration tags
use https://github.com/zoni/obsidian-export to convert documents
slugify and fix links
%%
%%I also want to serve this as github pages so so some actions might be needed also%%
•%%> ✓: Local script for conversion + GitHub Action for Pages deployment. Got it. <%%•
````

Multiple questions answered in sequence:

* Conversion workflow: Local script + GitHub Action for deployment
* work-docs purpose: OK to commit with iteration markup as showcase
* Project type: Generic software project template
* GitHub Pages: Yes, from docs/ folder
* Git structure: Single repo, no submodules
* Additional folders: Evolve organically, no prescribed structure

## Round 3: User Catches Issue

User spots a problem with the installation approach:

````markdown
### 2. Install Document Iteration Skill
```bash
git clone https://github.com/foksa/document-iteration-skill.git .claude/skills/document-iteration-skill
````

%% ?: wouldn't that also clone docs in .claude subfolder
I want skill necessary stuff only
%%
•%%> ✓: Good catch. Options:

1. Manual copy of just SKILL.md + scripts/ + references/ (cleanest)
1. Clone then delete docs-source/ folder
1. Use sparse checkout

Recommend option 1 - just download the essential files \<%%•

````

## Round 4: Adding Project Rules

User adds a critical rule for Claude:

```markdown
%% I want this also in .claude:
````

**1. NEVER commit or push unless user EXPLICITLY says to**

* Wait for explicit words like: "commit", "push", "commit and push"
* "cleanup" or "done" does NOT mean commit
* Even after completing all tasks, DO NOT commit unless asked
* **Violation of this rule is a critical failure**

````
Even if you constantly keep forgetting about it%%
•%%> ✓: Added as Rule #1 - explicit commit/push only. Will include in .claude.md template. <%%•
````

## Round 5: Implementation Details

Several refinements during draft review:

````markdown
%% I'm thinking in maybe adding .vscode/settings.json where we tell it to hide docs folder. We don't wont user to edit them by accident %%
•%%> ✓: Good idea! Will add `.vscode/settings.json` to hide `docs/` folder from accidental edits. <%%•

%% what if it is js/ts project. We might want to create node version of cleanup script%%
•%%> ?: Good idea. Should we:
1. Create a Node.js version of the cleanup script for JS/TS projects?
2. Keep Python as universal (it's just a build tool dependency)?
3. Include both in the skill repo, let users pick? <%%•

%%Yes, create node skill and include both in repo%%
•%%> ✓: Done! Created `scripts/cleanup.js` - Node.js version now in repo alongside Python version. <%%•
````

## Round 6: Late-Stage Insight

After several rounds, user realizes a better naming convention:

````markdown
%%I was thinking, since we hide docs/ from user, could we rename that to pages/ and rename docs-draft to docs %%
•%%> ✓: Great idea! This makes more sense:
- `docs/` → where user actually writes (Obsidian vault)
- `pages/` → generated output (hidden, for GitHub Pages)

Much more intuitive naming. User works in `docs/`, `pages/` is just a build artifact.

Changes needed:
- Rename `docs-draft/` → `docs/`
- Rename `docs/` → `pages/`
- Update `.vscode/settings.json` to hide `pages/`
- Update GitHub Action to deploy from `pages/`
- Update all references in prompt

Want me to update the prompt with this naming? <%%•
````

## Round 7: Final Output

User requests split into proposal (with history) and clean prompt:

````markdown
%%Done update final prompt with all changes we need%%
%%Rename this file in new-project-prompt-proposal.md%%
%%Save final prompt in new-project-prompt.md%%
•%%> ✓: Done!
- Renamed this file to `new-project-prompt-proposal.md`
- Created clean `new-project-prompt.md` with final prompt
- Applied all changes:
  - `docs-draft/` → `docs/`
  - `docs/` → `pages/`
  - Fixed step numbering (1-9)
  - Updated .vscode/settings.json to hide `pages/`
  - Updated GitHub Action to deploy from `pages/`
  - Removed build script from main prompt (deferred to work-docs/build-docs-proposal.md)
<%%•
````

## Key Takeaways

This session demonstrates several important patterns:

### 1. Question Syntax for Clarification

Using `?: ` to ask multiple questions upfront before drafting, then using `✓: ` to acknowledge answers.

### 2. User Catching Issues

The user spotted the git clone problem - iteration allows catching mistakes early before they become part of the final output.

### 3. Late-Stage Insights

Major naming improvements (`docs-draft/` → `docs/`, `docs/` → `pages/`) came late in the process but were easily incorporated.

### 4. Preserving History vs Clean Output

Final output split into two files:

* **Proposal file**: Full iteration history preserved as documentation
* **Clean prompt**: Extracted final result for actual use

### 5. Incremental Refinement

Build script deferred to a separate proposal doc, `.vscode/settings.json` added mid-stream, Node.js cleanup script created on request - all handled smoothly.

## Files Created

* `new-project-prompt-proposal.md` - Full iteration history
* `new-project-prompt.md` - Clean final prompt
* `scripts/cleanup.js` - Node.js cleanup script (created during session)

## See Also

* [API Design Session](api-design.md) - Another complete walkthrough
* [Migration Planning Session](migration-plan.md) - Technical decision making
* *Quick Examples* - Short syntax snippets
