---
title: "_Gemini Feedback Analysis"
layout: default
---

# Gemini Feedback Analysis

**Status:** ✅ Complete
**Not linked from index** - internal planning document

---

## Summary

Cross-model review with Gemini (4 rounds) validated the Document Iteration Skill concept and provided actionable improvements for SKILL.md v3.0.

---

## Key Insights

1. **Few-shot examples are #1 priority** - LLMs are pattern-matching engines; examples > instructions
2. **"Syntax Engine" identity helps** - Breaks RLHF chat training bias
3. **Negative constraints are critical** - "NEVER use `**bold**`" prevents markdown defaults
4. **Inline everything** - Single self-contained file is gold standard
5. **Postel's Law** - Strict output, tolerant input (no space in output, forgive space in parsing)

---

## Validated Use Case

> "Non-Destructive Editing" - surgical changes to critical documents without style drift.

Gemini's example: API version migration documentation where you want the AI to be surgical, not rewrite prose.

---

## Implemented (SKILL.md v3.0)

- ✅ "Syntax Engine" identity framing at top
- ✅ Negative constraints section ("NEVER DO THIS")
- ✅ 4 few-shot examples with CORRECT/INCORRECT patterns
- ✅ "NO space after ==" instruction

---

## Remaining Items

### High Priority
- Implement "warn and preserve" in cleanup script
- Document whitespace tolerance in syntax docs

### Medium Priority
- Add comparison table to FAQ (Coach vs Copy Editor positioning)
- Update README positioning
- Add canonical "Golden Example"

### Low Priority
- Create linter GitHub Action
- Document parser regex patterns

---

## Design Decisions

| Topic | Decision | Rationale |
|-------|----------|-----------|
| `(TOKEN)` syntax | Keep as-is | Visually distinct, works well |
| `>> >>` syntax | Keep as-is | Compact for inline notes |
| Whitespace tolerance | Strict output, tolerant input | Postel's Law |
| Dual syntax (CriticMarkup) | Don't mix | One pattern reduces cognitive load |

---

## Related Documents

- [_compiler-scripts-proposal.md](_compiler-scripts-proposal.md) - Cleanup script design
