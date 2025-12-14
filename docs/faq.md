---
title: "Faq"
layout: default
---

# FAQ

Frequently asked questions about the Document Iteration Skill.

## General

### What is this for?

This syntax helps you give precise feedback on documents when working with Claude. Instead of vague chat comments like "fix section 3", you mark exactly what you mean.

### Does it work with any document?

Yes! Any markdown file. Technical docs, creative writing, planning documents, research papers - anything you're iterating on.

### Do I need special tools?

No. Just a text editor. The syntax is plain markdown with some conventions.

## Syntax Questions

### What's the difference between `%%` and `>>`?

- `%% comment %%` - You write these for feedback
- `%% > response %%` - Claude writes these as responses
- `>> NOTE: >>` - Claude can add these as helpful context

### When do I use tokens like `(DB)`?

When you have multiple things to comment on in the same area. Tokens link your `==highlight==(TOKEN)` to your `%%(TOKEN) comment %%`.

### How do I approve a section?

Add `%% APPROVED %%` after the section heading:

```markdown
## Pricing %% APPROVED %%
```

Claude won't modify approved sections.

## Troubleshooting

### Claude isn't responding to my comments

Make sure you:
1. Added `SKILL.md` to your Claude project
2. Used the correct syntax: `%% comment %%` (two percent signs each side)
3. Asked Claude to "update" or "respond to" the file

### My tokens aren't matching

Check that your token in `==text==(TOKEN)` matches exactly with `%%(TOKEN) comment %%`. They're case-sensitive.

## See Also

- [Examples](examples.md) - See the syntax in action
- [Contributing](contributing.md) - Report issues or suggest improvements