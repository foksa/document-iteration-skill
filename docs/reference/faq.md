---
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

### What's the difference between `%%` and `%%>`?

* `%% comment %%` - You write these for feedback
* `%%>response <%%` - Claude writes these as responses
* `%%> NOTE: <%%` - Claude can add these as helpful context

### When do I use tokens like `(DB)`?

When you have multiple things to comment on in the same area. Tokens link your `==highlight(TOKEN)==` to your `%%(TOKEN) comment %%`.

### How do I approve a section?

Add `%% APPROVED %%` after the section heading:

````markdown
## Pricing %% APPROVED %%
````

Claude won't modify approved sections.

## Troubleshooting

### Claude isn't responding to my comments

Make sure you:

1. Added `SKILL.md` to your Claude project
1. Used the correct syntax: `%% comment %%` (two percent signs each side)
1. Asked Claude to "update" or "respond to" the file

### My tokens aren't matching

Check that your token in `==text(TOKEN)==` matches exactly with `%%(TOKEN) comment %%`. They're case-sensitive.

### Claude removed my comment without responding

This is a skill violation. Even with strict rules in SKILL.md, Claude may occasionally skip steps when processing multiple comments or getting "in the flow" of implementing changes.

**What happened:** Claude treated your comment as an instruction and executed it directly, removing the comment without adding a `%%>response <%%` first.

**What to do:**

1. Point it out: "You removed my comment without responding"
1. Ask Claude to undo and respond properly
1. Claude should restore the comment and add a response

**Why this happens:** The skill rules are clear, but execution can fail. This is rare but possible, especially with action-oriented comments like "move this" or "add that".

**Prevention tips:**

* Review Claude's changes before accepting
* Use version control to catch unexpected deletions
* When you notice a violation, correct it immediately

See *Mandatory Rules* for examples of correct behavior.

### Claude adds its own comments or marks things APPROVED

**What happened:** Claude added `%% comments %%` of its own (not responses), or marked sections `%% APPROVED %%` without you asking.

**Why:** Claude sometimes interprets patterns and "helps" by adding markup it shouldn't.

**What to do:**

1. Point it out: "You added a comment - only I add comments, you respond with `%%>`"
1. Remove the incorrect markup
1. Claude should understand and avoid this going forward

**Prevention:**

* The SKILL.md v4.0 has explicit "NEVER DO THIS" rules for this
* If persistent, remind Claude: "You're a Syntax Engine, not a collaborator"

### Claude responds conversationally instead of using syntax

**What happened:** Instead of `%%>Updated! <%%`, Claude says "I've updated the database section for you."

**Why:** Claude defaults to chat-style responses.

**What to do:**

1. Point it out: "Use the syntax, don't explain in chat"
1. Ask Claude to redo the response inline

**Prevention:**

* SKILL.md v4.0 has few-shot examples showing correct vs incorrect output
* The "Syntax Engine" framing helps Claude stay in syntax mode

## See Also

* *Examples* - See the syntax in action
* *Contributing* - Report issues or suggest improvements
