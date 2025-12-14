---
title: "Customization"
layout: default
---

# Customization

The skill defines default behavior. Your project's `.claude.md` file can override, extend, or add rules specific to your needs.

## How It Works

Claude reads both:
1. **Skill** (`SKILL.md`) - Default behavior for document iteration
2. **Project config** (`.claude.md`) - Project-specific overrides

Project config takes precedence when there's a conflict.

## Overriding Mandatory Rules

The skill has three mandatory rules. Here's how to override each. See [Mandatory Rules](mandatory-rules.md) for details on what each rule does.

### Allow Auto File Moves

Default: Claude must ask before moving files.

```markdown
## Override: Allow auto file moves
Claude may move files without explicit approval when
reorganizing documentation structure.
```

### Skip Response Requirement

Default: Every `%%` comment gets a `%% > response %%`.

```markdown
## Override: Skip responses for trivial fixes
For simple typo fixes or formatting corrections, Claude
may edit directly without adding a response.
```

### Allow Comment Removal

Default: Claude never removes user comments.

```markdown
## Override: Auto-remove resolved comments
After implementing feedback, Claude may remove the
original comment if the fix is straightforward.
```

## Adding Project Rules

Add rules that don't exist in the skill:

### Protect Certain Files

```markdown
## Rule: Protected files
Never modify files in these folders without explicit approval:
- /contracts/
- /legal/
- /config/
```

### Require Specific Tokens

```markdown
## Rule: Required tokens
All TODO items must use the (TODO) token.
All security concerns must use (SECURITY) token.
```

### Custom Cleanup Behavior

```markdown
## Rule: Cleanup before commit
When committing documentation, always offer to clean
iteration markers first.
```

## Example .claude.md Templates

### Strict Mode

```markdown
# Claude Code Instructions

Use the Document Iteration Skill.

## Additional Rules

1. Never auto-commit anything
2. Always ask before file operations
3. Check for markers before every commit
4. Warn about WIP sections loudly
```

### Relaxed Mode

```markdown
# Claude Code Instructions

Use the Document Iteration Skill.

## Overrides

1. May move files without asking when organizing docs
2. May skip responses for obvious fixes
3. Auto-cleanup markers before commits (no confirmation needed)
```

### Team Mode

```markdown
# Claude Code Instructions

Use the Document Iteration Skill.

## Team Rules

1. Always include author attribution in responses
2. Never modify sections marked with another person's initials
3. Flag conflicts: "⚠️ @JS and @MK have conflicting feedback"
```

## Best Practices

1. **Be explicit** - State exactly what you're overriding
2. **Explain why** - Future you will thank you
3. **Test overrides** - Make sure Claude follows them
4. **Keep it short** - Long configs get ignored

## Related

- [Mandatory Rules](mandatory-rules.md) - Default rules in the skill
- [Auto-Cleanup](index.md) - Pre-commit configuration
- [Installation](installation.md) - Setting up the skill