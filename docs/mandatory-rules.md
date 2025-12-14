---
title: "Mandatory Rules"
layout: default
---

# Mandatory Rules

The skill enforces three mandatory rules that Claude must always follow. These ensure consistent, predictable behavior.

## Rule 1: Always Respond to Comments

**Every `%%` comment MUST receive a `%% > response %%`**

Even when implementing immediately, Claude adds the response first. The response is the record that feedback was processed.

**Why it matters:** Without a response in the document, there's no proof the comment was seen or addressed. The response creates an audit trail.

**Example:**
```markdown
%% Add error handling here %%
  %% > Added try-catch with logging. %%
```

### Wrong vs Right

❌ **Wrong** - Claude removes comment and acts without responding:
```markdown
# Before
%% Move the utils section to a separate file %%

# After (WRONG - Claude moved the file but removed the comment)
# (comment is gone, file was moved)
```

✅ **Right** - Claude responds first, preserves comment:
```markdown
# Before
%% Move the utils section to a separate file %%

# After (CORRECT)
%% Move the utils section to a separate file %%
  %% > Good idea. I'll create utils.md and move the section there. Approve? %%
```

The comment stays until cleanup. The response proves Claude saw and processed the feedback.

## Rule 2: Never Remove User Comments

**Claude only adds responses, never removes comments**

User decides when to clean up, not Claude. Cleanup happens only when explicitly requested.

**Why it matters:** Comments are the user's feedback. Only the user knows when an issue is truly resolved and ready to be cleaned up.

**Example:**
```markdown
%% Fix the typo %%
  %% > Fixed "recieve" → "receive" %%

# Comment stays until user removes it or requests cleanup
```

## Rule 3: Ask Before File Operations

**File moves, renames, and deletions require explicit approval**

When Claude thinks a file should be moved or renamed, it must:
1. State what it plans to do in the response
2. Explicitly ask for approval
3. Wait for user confirmation before acting

**Why it matters:** File operations can break links, references, and workflows. The user should always approve structural changes.

**Example:**
```markdown
%% This doc belongs in the workflow folder %%
  %% > You're right. I'll move this to workflow/auto-cleanup.md. Approve? %%
```

Claude does NOT move the file until user says "yes", "approved", "do it", etc.

## Enforcement

These rules are in the `⛔ MANDATORY RULES (NEVER SKIP)` section of the skill. Violating them is considered a failure.

If Claude skips a rule, remind it:
- "You didn't respond to my comment"
- "You removed my comment without asking"
- "You moved the file without approval"

## Customization

These rules can be overridden in your project's `.claude.md` file. See [Customization](customization.md) for examples of relaxing or extending these rules.

## Related

- [Syntax Overview](index.md) - Comment and response syntax
- [Cleanup](cleanup.md) - How cleanup works
- [Auto-Cleanup](index.md) - Pre-commit checks