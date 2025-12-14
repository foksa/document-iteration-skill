---
title: "_Gemini Feedback Analysis"
layout: default
---

# Gemini Feedback Analysis

**Status:** ✅ Review complete
**Not linked from index** - internal planning document

---

## Summary

Gemini reviewed the Document Iteration Skill repository and provided feedback across 6 blocks. This document analyzes the feedback and extracts actionable items.

**Round 2:** After being pointed to the actual docs, Gemini provided deeper technical feedback with new insights.

---

## Block 1: Overall Concept

### Feedback
- ✅ Confirms the approach solves a real problem
- ✅ Syntax is intuitive for Markdown/Obsidian users
- ⚠️ Warning about "learning tax" of custom syntax
- ⚠️ Concern about complex tokens breaking LLM consistency

### Analysis
The positive feedback validates the core concept. The concern about complex tokens is valid but our current token design is simple (single words like `TODO`, `QUESTION`, `REPHRASE`). No action needed unless we add complex token syntax.

### Action Items
- [ ] None - concept validated

---

## Block 2: Syntax Design

### Feedback
- ✅ `%% %%` - Excellent choice (Obsidian comment syntax)
- ⚠️ `==text==(TOKEN)` - LLMs often hallucinate space: `==text== (TOKEN)`
- ⚠️ `>> >>` - May conflict with nested blockquotes (`> > text`)

### Analysis

**Whitespace issue:** This is a real concern. We should:
1. Document that whitespace is tolerated
2. Consider if SKILL.md should explicitly mention no space

**Blockquote conflict:** The `>> >>` syntax is used for Claude's notes, not user input. In practice:
- `> > text` renders as nested blockquote
- `>> text >>` does not (the closing `>>` prevents this)
- Risk is low but worth documenting

### Action Items
- [ ] Add note to SKILL.md that `==text== (TOKEN)` with space is acceptable
- [ ] Update syntax docs to mention the space tolerance
- [ ] Consider documenting blockquote non-conflict in FAQ

---

## Block 3: SKILL.md File

### Feedback
- Separate Definition from Process
- Add "few-shot" examples of bad vs good output
- Define how to handle unchanged text

### Analysis

**Current state:** SKILL.md already has:
- Clear definitions in "Reading feedback" section
- Examples of correct behavior
- Process defined in "Responding to feedback"

**Missing:**
- Explicit "bad output" examples showing what NOT to do
- We do have this in mandatory-rules.md but not in SKILL.md itself

**Unchanged text:** Our approach is to output the whole document with changes inline. This is already the behavior but could be more explicit.

### Action Items
- [ ] Add "What NOT to do" section to SKILL.md with bad examples
- [ ] Make explicit that Claude outputs full document with inline changes
- [ ] Review if Definition/Process separation is clear enough

---

## Block 4: Documentation Quality

### Feedback
- Need "Troubleshooting" section for when Claude ignores syntax
- Need separate "Syntax Cheatsheet" quick reference

### Analysis

**Troubleshooting:** We have this in FAQ with "Claude isn't responding to comments" and "Claude removed my comment". Could expand.

**Cheatsheet:** syntax/index.md has a quick reference table. Could be more prominent or separate.
%% I like cheatsheet. Make it print friendly %%
%% > Added to action items: create print-friendly cheatsheet %%

### Action Items
- [ ] Expand FAQ troubleshooting for "Claude ignores syntax" scenario
- [ ] Consider standalone cheatsheet.md or more prominent quick reference

---

## Block 5: Comparison to Alternatives

### Feedback
- **CriticMarkup** is closest prior art: `{++addition++}`, `{--deletion--}`, `{~~sub>>stitution~~}`
- Similar to Google Docs "Suggesting" mode
- Better than Git diffs for prose
- Would use for long technical articles

### Analysis

CriticMarkup is interesting prior art we should acknowledge. Key differences:
- CriticMarkup is for tracking changes (additions/deletions)
- Our syntax is for feedback/iteration (comments, responses, highlights)
- Different use cases: CriticMarkup = diff format, ours = review format

### Action Items
- [ ] Add CriticMarkup mention to FAQ or "Comparison" section
- [ ] Clarify our differentiation: iteration/review vs change-tracking

---

## Block 6: Suggestions

### Feedback
1. **Prioritize a "Compiler" script** - accept/reject changes to produce clean final
2. **Add negative constraints** - tell Claude what NOT to do in SKILL.md
3. **Whitespace robustness** - parser should tolerate `==text== (TOKEN)`

### Analysis

**Compiler script:** We have cleanup syntax (`/cleanup`, `%%!CLEANUP!%%`) but no automated script. This could be valuable for CI/CD workflows.
%% I had plans to do this. For now, lets create unlinked document with proposal for compiler scripts %%
%% > Created _compiler-scripts-proposal.md with design options %%

**Negative constraints:** Already in mandatory-rules.md but should be in SKILL.md too.

**Whitespace:** Valid - should document tolerance.

### Action Items
- [ ] Consider creating cleanup script (Python/JS) for automation
- [ ] Add "What NOT to do" examples to SKILL.md
- [ ] Document whitespace tolerance in syntax docs

---

## Priority Matrix

### High Priority (Should do)
1. Add "What NOT to do" section to SKILL.md with bad examples
2. Document whitespace tolerance for `==text== (TOKEN)`
3. Expand troubleshooting for "Claude ignores syntax"

### Medium Priority (Nice to have)
4. Add CriticMarkup comparison/differentiation
5. Consider standalone cheatsheet
6. Make full-document-output behavior explicit

### Low Priority (Future consideration)
7. Create automated cleanup script
8. Document blockquote non-conflict

---

## Notes

- Gemini could not access SKILL.md directly, so some feedback is speculative
%% Skill.md is also in pages. Write me prompt under here to point that to gemini %%
%% > Added follow-up prompt below %%

**Follow-up prompt for Gemini:**
```
Thanks for the review! A few clarifications:

1. SKILL.md is available in the docs: https://github.com/foksa/document-iteration-skill/blob/main/docs/SKILL.md
   Can you review it specifically and update your Block 3 feedback?

2. The full documentation is at /docs/ - here are the key files:
   - docs/SKILL.md - the core skill file
   - docs/skill/mandatory-rules.md - rules Claude must follow
   - docs/syntax/index.md - syntax overview with quick reference table

Please re-evaluate Block 3 (SKILL.md File) and Block 4 (Documentation Quality) now that you can access these files directly.
```

- Many suggestions are already implemented but not visible to external reviewer
- Core validation: the concept and syntax are sound

---

# Round 2: Deep Dive Feedback

After pointing Gemini to the actual documentation files, received more technical feedback.

---

## Block 1 (Updated): Concept Validation

### New Insights
- ✅ "Diff-based iteration" is the correct mental model
- ✅ Token efficiency: sending changes is cheaper than full rewrites
- ✅ Context preservation: minimizes style drift
- ⚠️ **Parser fragility**: if LLM makes syntax error, downstream tools may crash
- ⚠️ **Training data bias**: LLMs want to use standard markdown (`**bold**`, `~~strike~~`)

### Analysis
Parser fragility is real - the cleanup script should be robust to malformed markers. Training bias is why we need strong negative constraints.

### New Action Items
- [ ] Ensure cleanup script handles malformed markers gracefully
- [ ] Add explicit "NEVER use **bold** or ~~strikethrough~~ for changes" to SKILL.md

---

## Block 2 (Updated): Syntax Risks

### New Insights
- `==text==(TOKEN)`: Regex should permit optional whitespace: `==.*?==\s*\(TOKEN\)`
- `>> >>`: Could confuse renderers as nested blockquote
- Alternative suggested: `{>> comment <<}` (CriticMarkup) or `[ comment ](comment.md)`
- `()` parentheses are common in text - risk of false positives

### Analysis
**Whitespace:** Already noted, confirmed as high priority.

**Blockquote:** Our closing `>>` differentiates from blockquotes. Low risk.

**Parentheses in TOKEN:** This is a valid concern. However:
- Our tokens are UPPERCASE (TODO, QUESTION)
- Normal text rarely has `==(WORD)` patterns
- Changing syntax now would break existing users
%%
We don't have existing users, I'm the only one, this is WIP
Also, while working on documentation i not even once used == ...== (TOKEN)
We'll keep it for robustness, but if you think we can have better approach go for it
%%
%% >
Good point - no breaking change concerns yet.

Re: `==text==(TOKEN)` not being used - that's actually fine! The highlight syntax is optional and situational. The core workflow is `%% comments %%` → `%% > responses %%`. Highlights are for when you want to mark specific text for attention.

Alternative syntaxes considered:
- `::TOKEN::` - cleaner but less visually distinct
- `/TOKEN/` - could conflict with paths
- `[TOKEN]` - conflicts with markdown links

Current `(TOKEN)` is fine. The parentheses are visually distinct and rarely appear after `==` in normal text. Let's keep it.
%%

### Decision
Keep current syntax but document the design rationale. No syntax change.

### New Action Items
- [ ] Document why we chose `(TOKEN)` vs alternatives in FAQ
- [ ] Add regex examples to compiler-scripts-proposal.md

---

## Block 3 (Updated): SKILL.md Architecture

### New Insights (Critical)
**Context Retrieval Risk:** If SKILL.md references mandatory-rules.md but LLM doesn't load it, rules are ignored.

**Recommendation:** SKILL.md should concatenate critical rules, not just reference them.

**Negative Constraints Required:**
> "Don't just say 'Use == for changes.' You must say 'NEVER use standard markdown bold ** or italic * to denote changes. ONLY use ==.'"

**Error Recovery:** What if user's text has broken markdown?

### Analysis
This is the most important feedback. Our current approach:
- SKILL.md is self-contained for Claude Code (skill is loaded directly)
- For claude.ai, user pastes SKILL.md content into project knowledge

The risk is real for partial loading. We should ensure SKILL.md is complete standalone.

### New Action Items
- [ ] **HIGH**: Add negative constraints directly to SKILL.md (not just mandatory-rules.md)
- [ ] Consider inlining key mandatory rules into SKILL.md
- [ ] Add error recovery guidance for broken markdown

---

## Block 4 (Updated): Documentation Gaps

### New Insights
- Missing "Why?" column in syntax reference
- Missing "Golden Example" - one complex before/after transformation
- Missing parser specification (regex vs AST) for developers

### Analysis
**Why column:** Good idea - helps both humans and LLMs understand rationale.

**Golden Example:** We have examples/sessions/ but could add a single canonical example to syntax/index.md.

**Parser spec:** Low priority unless we get community contributions.

### New Action Items
- [ ] Add "Why?" explanations to syntax quick reference
- [ ] Add canonical "Golden Example" to syntax docs
- [ ] Document regex patterns in compiler-scripts-proposal.md

---

## Block 5 (Updated): Positioning

### New Insights
Gemini's comparison breakdown:

| Tool | Best For |
|------|----------|
| Our syntax | Annotation, "Coach" persona, prose feedback |
| CriticMarkup | Track Changes, "Copy Editor" persona |
| Word Track Changes | Non-technical users |
| Cursor/Copilot diffs | Code (block diffs) |

**Our niche:** "Prose/Technical Writing" with inline diffs.

### Analysis
This is excellent positioning clarity. We should add this to marketing/README.

### New Action Items
- [ ] Add comparison table to FAQ or new "Alternatives" page
- [ ] Update README with clearer positioning

---

## Block 6 (Updated): Concrete Suggestions

### Suggestions Received

1. **Harden syntax:** Change `(TOKEN)` to `::TOKEN::` or `/TOKEN/`
   - **Decision:** No - breaking change, parentheses work fine
    %% as I commented before, we don't care about breaking changes ATM %%
    %% > True! But `(TOKEN)` is actually fine - it's visually clear and works. No need to change just for the sake of it. %%

2. **Few-shot examples in SKILL.md:**
   ```
   CORRECT OUTPUT: The ==quick==(REPLACE: fast) brown fox...
   INCORRECT OUTPUT: The quick (change to fast) brown fox...
   ```
   - **Decision:** YES - high priority

3. **Create a linter:** GitHub Action to validate docs match syntax
   - **Decision:** Good idea, add to compiler-scripts-proposal

### New Action Items
- [ ] **HIGH**: Add CORRECT/INCORRECT examples to SKILL.md
- [ ] Add linter to compiler-scripts-proposal.md

---

## Updated Priority Matrix

### Critical (Do first)
1. Add negative constraints to SKILL.md ("NEVER use **bold**...")
2. Add CORRECT/INCORRECT few-shot examples to SKILL.md
3. Ensure cleanup script handles whitespace: `==text== (TOKEN)`

### High Priority
4. Document whitespace tolerance in syntax docs
5. Add "Why?" explanations to syntax reference
6. Add canonical "Golden Example"

### Medium Priority
7. Add comparison table to FAQ
8. Update README positioning
9. Expand troubleshooting

### Low Priority
10. Create linter GitHub Action
11. Document parser regex patterns
12. Document `>> >>` vs blockquote non-conflict

---

# Round 3: Final Recommendations

Gemini's responses to our follow-up questions.

---

## Q1: System Prompt Length

### Answer
300 lines (~2-3k tokens) is **negligible** for modern models (128k+ context).

**The real risk is fragmentation, not length.**
- Users forget to copy dependency files
- Single self-contained file is more robust

### Recommendation
> "Inline the rules. A single, self-contained SKILL.md is the 'Gold Standard' for portability."

### Action
- [x] Decision confirmed: Inline mandatory rules into SKILL.md

---

## Q2: Parser Error Handling

### Answer
Use **"Loud Warning, Safe Fallback"** strategy:

| Issue | Handling |
|-------|----------|
| Whitespace/formatting | Auto-fix silently (`== text ==` → `==text==`) |
| Ambiguous syntax | Fail loudly or ask confirmation |

**Why?** If parser guesses wrong on a legal clause, document is corrupted.

### Good UX
> "Warning: Line 45 has a broken marker. Original text preserved."

### Bad UX
- Python traceback crash
- Silent deletion of unparseable text

### Action
- [ ] Implement "warn and preserve" in cleanup script

---

## Q3: Coach vs Copy Editor (Dual Syntax)

### Answer
**Don't mix syntaxes.** Increases cognitive load for the model.

**Better approach:** Use existing syntax with Types:
- Coach: `==text==(COMMENT: "Tone is too casual")`
- Editor: `==text==(REPLACE: "New text")`

**Why?** One reliable pattern is easier than two competing syntaxes.

### Decision
Keep current syntax. No CriticMarkup hybrid.

---

## Q4: Whitespace Tolerance

### Answer
Yes, instruct Claude to output canonical form (no space).

**Postel's Law:** "Be conservative in what you do, be liberal in what you accept."

- **Instruction:** Tell Claude to STRICTLY attach `(TOKEN)` with NO space
- **Parser:** Forgive the space anyway: `==.*?==\s*\(TOKEN\)`

### Benefit
Minimizes token usage, keeps diffs clean, but doesn't break when model slips.

### Action
- [ ] Add "NO space after ==" instruction to SKILL.md
- [ ] Ensure cleanup regex tolerates space

---

## Q5: The `>> >>` Syntax

### Answer
**It depends on where user views the result.**

In Markdown viewers: `>> Text` renders as nested blockquote, which:
- Looks like part of document content (confusing)
- Could be mistaken for external quote

### Recommendation
Consider using Callout syntax instead:
```markdown
> [!NOTE] Claude's Reasoning
> I changed this because...
```

This renders beautifully in Obsidian and GitHub.

### Analysis
This is a valid point. However:
- `>> >>` is Claude-generated, not user-facing in raw form
- Changing now would be breaking change
%%Again, don't care if breaking change%%
%% >
Fair point! Since we're still in WIP, we could switch.

However, let's think about it:
- `>> note >>` is compact for inline notes
- Callouts `> [!NOTE]` are multi-line and verbose
- The `>> >>` is rarely used (Claude adds context notes sparingly)

I'd say keep `>> >>` for now - it works and is compact. If it becomes a pain point in practice, we can revisit. The "breaking change" argument was more about user expectations than code compatibility.
%%
- Callouts are verbose for inline notes

### Decision
Keep `>> >>` for now. Document the rendering behavior. Revisit if it causes issues in practice.

---

## Bonus: "Identity/Role" Quick Win

### Suggestion
Add identity block at top of SKILL.md:

**Current:** "You are a document iteration assistant..."

**Improved:**
> "You are a Syntax Engine. You are NOT a chat assistant. Your output is NOT for human reading, but for a parser. You do not strictly converse; you OUTPUT SYNTAX."

**Why?** Breaks model out of "helpful chatty assistant" RLHF training, pushes into "code generation" mode.

### Action
- [ ] **HIGH**: Add "Syntax Engine" identity framing to SKILL.md

---

## Final Priority Matrix (All Rounds)

### Critical (Do immediately)
1. ~~Add negative constraints to SKILL.md~~ ("NEVER use **bold**...") ✅ Done
2. ~~Add CORRECT/INCORRECT few-shot examples~~ ✅ Done
3. ~~Add "Syntax Engine" identity framing~~ ✅ Done
4. ~~Inline mandatory rules into SKILL.md~~ ✅ Done (rules already inline)

### High Priority
5. ~~Add "NO space after ==" instruction~~ ✅ Done
6. Implement "warn and preserve" in cleanup script
7. Document whitespace tolerance in syntax docs
8. Add "Why?" explanations to syntax reference

### Medium Priority
9. Add comparison table to FAQ (Coach vs Copy Editor framing)
10. Update README positioning
11. Add canonical "Golden Example"
12. Expand troubleshooting

### Low Priority
13. Create linter GitHub Action
14. Document parser regex patterns
15. Consider callout syntax for v2

---

## Summary

Gemini's verdict:
> "You are building something very useful. The shift to 'Inline the rules' and 'Strict negative constraints' will make v2 much more reliable."

Key insights:
- **Fragmentation > Length**: Inline everything into SKILL.md
- **Postel's Law**: Strict output, tolerant input
- **Identity framing**: "Syntax Engine" not "chat assistant"
- **No syntax mixing**: One pattern, use Types for personas

---

# Round 4: Final Answer

## The ONE Thing for Adherence

**Answer: Few-Shot Examples** (not identity framing)

> "LLMs are, at their core, sophisticated pattern-matching engines."

- **Instructions** tell the model what to do *abstractly*
- **Examples** show the model how to do it *concretely*

If you provide 3 clear examples of "Messy Input" → "Clean Syntax Output", the model *mimics the pattern*. It sees that `**bolding**` wasn't used in examples, so it won't do it.

### The "Golden" Few-Shot Format

```
User Input: A paragraph with a grammar error.
Bad Response (Negative Example): "Here is the fixed text..." (Standard chat behavior)
Good Response (Your Syntax): The actual markup you want.
```

> "If you force the model to see that pattern, adherence skyrockets."

### Updated Priority

Few-shot examples move to **#1 Critical** - even above identity framing.

---

## Would Gemini Use This?

**Yes.**

### Use Case: API Version Migration

> "I often have to update documentation when a software library changes from v1 to v2."

**The Problem:** Pasting docs into ChatGPT with "Update for v2" causes it to rewrite explanations, change tone, remove warnings.

**Why this tool fits:**
> "I want the AI to be surgical. Leave my carefully written prose alone, and only wrap the old code in `==old_code==(REPLACE: new_code)`."

### Gemini's Verdict

> "Your tool allows for 'Non-Destructive Editing' of critical files. That is a massive workflow upgrade for developers and technical writers."

---

## Final Summary

**Status:** ✅ Review complete

### What We Learned

1. **Few-shot examples are the #1 priority** - Pattern matching > instructions
2. **"Syntax Engine" identity helps** - But examples matter more
3. **Negative constraints are critical** - "NEVER use **bold**"
4. **Inline everything** - Single file is gold standard
5. **Postel's Law** - Strict output, tolerant input

### Validated Use Case

"Non-Destructive Editing" - surgical changes to critical documents without style drift.

### Next Steps

~~Implement the critical items from the priority matrix, starting with few-shot examples in SKILL.md.~~ ✅ Done

**SKILL.md v3.0 now includes:**
- "Syntax Engine" identity framing at the top
- Negative constraints section ("NEVER DO THIS")
- 4 few-shot examples with CORRECT/INCORRECT patterns
- "NO space after ==" instruction

Remaining high priority items:
- Implement "warn and preserve" in cleanup script
- Document whitespace tolerance in syntax docs