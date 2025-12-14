---
title: "Claude Check"
layout: default
---

# Auto-Cleanup on Commits

Configure Claude to automatically check for iteration markers before committing changes.

## Setup

Add this to your project's `.claude.md` file:

```markdown
## ⛔ MANDATORY: Pre-Commit Marker Check

**Before ANY commit, you MUST:**

1. Scan ALL staged files for iteration markers (`%% %%`, `>> >>`, `==(TOKEN)`)
2. If markers found, STOP and report:
   - "Found X markers in Y files. Clean up before commit? (yes/no)"
3. If user says "yes", follow cleanup process from skill
4. If user says "no", proceed with commit (markers will be committed)
5. NEVER commit without checking first

**This is NOT optional. Skipping this check is a failure.**
```

## Why This Matters

Iteration markers are meant for the drafting process - they shouldn't end up in committed files (unless intentionally). The pre-commit check catches:

- `%% comments %%` and `%% > responses %%` left in documents
- `>> notes >>` that were helpful during editing
- `==highlights==(TOKEN)` that weren't cleaned up

## Example Workflow

**User:** "commit the docs"

**Claude (correct):**
```
Scanning for iteration markers...

Found 3 markers in 2 files:
- docs/api.md: 2 comments
- docs/setup.md: 1 highlight

Clean up before commit? (yes/no)
```

**User:** "yes"

**Claude:** Follows cleanup process, then commits clean files.

---

**Claude (wrong):**
```
Committed docs with message "Update documentation"
```

This is wrong because markers weren't checked first.

## Integration with Skill

This pre-commit check works alongside the Document Iteration Skill:

- **Skill** handles the iteration workflow (comments, responses, cleanup commands)
- **Pre-commit check** is a safety net before committing

The skill's cleanup commands (`%%!CLEANUP!%%`, "cleanup this file") are for intentional cleanup during editing. The pre-commit check catches anything missed.

## Related

- [Cleanup Syntax](../../syntax/cleanup.md) - Manual cleanup commands
- [Syntax Overview](../../syntax/index.md) - All marker types