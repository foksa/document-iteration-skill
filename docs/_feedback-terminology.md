---
title: "_Feedback Terminology"
layout: default
---

# Feedback Terminology Idea

**Status:** Draft - sitting on it
**Not linked from index** - internal planning document

---

## The Problem

Currently no official name for the `%% comment %% → %% > response %%` pattern.

Need a term so users can say things like:
- "cleanup resolved ____"
- "this ____ is done"

## Proposed Term: "feedback"

- `%% comment %%` = feedback (or "open feedback")
- `%% comment %% + %% > response %%` = resolved feedback

### Usage Examples

Natural language:
- "cleanup resolved feedback"
- "remove completed feedback"
- "this feedback is done"

Potential commands:
- `%%!CLEANUP RESOLVED!%%` - only clean feedback with responses
- "cleanup resolved feedback in this section"

### Why "feedback"

- Simple, one word
- Users already think of comments as feedback
- The response marks it as "resolved"
- No jargon

### Alternatives Considered

| Term | Notes |
|------|-------|
| thread | Familiar but implies longer chains |
| exchange | Captures back-and-forth, less common |
| conversation | Too generic |
| dialogue | Too formal |

---

## Implementation (when ready)

1. Add terminology to syntax docs
2. Update SKILL.md cleanup section
3. Support "cleanup resolved feedback" command
4. Maybe add `%%!CLEANUP RESOLVED!%%` marker