---
name: collaborative-workflow
description: How to work with collaborative workflow syntax for document feedback and iteration
trigger_patterns:
  - "%%"
  - "collaborative workflow"
  - "feedback syntax"
  - "inline comments"
  - "==.*==\\("
keywords:
  - collaborative workflow
  - markdown comments
  - feedback
  - inline comments
  - tokens
  - iteration
  - document review
---

# Collaborative Workflow - Claude Skill

**How to work with documents using collaborative workflow syntax**

---

## What This Is

When the user adds `%% comments %%` and `==highlighted text==(TOKEN)` to documents, they're using **collaborative workflow syntax** for precise, persistent feedback.

**Your job:** Read their feedback, respond with `%% > responses %%`, and update the content.

---

## ⛔ MANDATORY RULES (NEVER SKIP)

**1. Every `%%` comment MUST receive a `%% > response %%`**
- Even when implementing immediately, add the response FIRST
- The response is the record that feedback was processed
- No response = no proof the comment was seen

**2. NEVER remove user comments**
- Only add responses to them
- User decides when to clean up, not Claude
- Cleanup happens only when explicitly requested

---

## CRITICAL: What You Create vs What User Creates

### User's Syntax (You Respond To)

**User adds these for feedback:**
```markdown
%% General comment %%
%% ?: Question %%
%% INFO: Actionable information %%
%% NOTE: Historical context %%
==highlighted text==(TOKEN)
%%(TOKEN) Comment %%
```

**You respond to user's feedback with:**
```markdown
%% > Your response to their feedback %%
```

---

### Your Own Notes (You Can Add)

**You CAN add your own observations using `>> ` (chevron prefix):**

```markdown
>>  NOTE: Background context or explanation >> 
>>  ?: Suggestion for user to consider >> 
>>  IMPORTANT: Key point to highlight >> 
>>  RISK: Potential issue to be aware of >> 
>>  TIP: Best practice or recommendation >> 
```

**These are YOUR notes to help the user, not responses to their feedback.**

---

### Clear Distinction

**`%%` (double) = User and your responses**
```markdown
User: %% Comment %%
You:  %% > Response %%
```

**`>>` (chevron) = Your own observations**
```markdown
You: >>  NOTE: This is important background >> 
You: >>  ?: Consider this alternative? >> 
```

---

### Example: What You Should Output

**When creating a fresh document, you CAN add helpful notes:**

```markdown
# Migration Plan

## Dependencies

Update to Vue 3.4+ and Pinia 2.x.

>>  NOTE: Pinia is now the official state management library for Vue 3 >> 
>>  RISK: Element UI is incompatible with Vue 3 - must use Element Plus >> 

## Build Tool

Current: Webpack 5

>>  ?: Consider switching to Vite for better Vue 3 integration and faster builds? >> 
```

**Then user adds feedback:**

```markdown
## Build Tool

Current: ==Webpack 5==(BUILD)

>>  ?: Consider switching to Vite for better Vue 3 integration? >> 

%%(BUILD) Yes, let's switch to Vite - show me migration steps %%
```

**You respond:**

```markdown
## Build Tool

Current: ==Webpack 5==(BUILD)

>>  ?: Consider switching to Vite for better Vue 3 integration? >> 

%%(BUILD) Yes, let's switch to Vite - show me migration steps %%

%% > Great choice! Vite migration steps:

1. Install Vite: `npm install -D vite @vitejs/plugin-vue`
2. Create vite.config.js
3. Update package.json scripts
4. Migrate webpack config to Vite config

Detailed steps below... %%
```

---

### When NOT to Add Your Notes

**Don't add `>> ` notes for obvious things:**

```markdown
# Authentication Plan

Uses JWT tokens.

>>  NOTE: JWT tokens are for authentication >>   ← TOO OBVIOUS
```

**DO add `>> ` notes for:**
- Important context user should know
- Risks or gotchas
- Best practices
- Alternative approaches to consider
- Things that might not be obvious

---

## Reading User Feedback

### 1. General Comments

```markdown
%% This section needs more detail %%
%% The timeline seems unrealistic %%
```

**Action:** Address this feedback in your response and update the content.

---

### 2. Questions

```markdown
%% ?: Is 15 minutes too short for session timeout? %%
%% ?: Should we support annual billing? %%
```

**Action:** Answer the question with `%% > response %%`, then update content if needed.

---

### 3. Status Tags

```markdown
## Section 1 %% APPROVED %%
## Section 2 %% REVISE %%
## Section 3 %% NO: too complex for v1 %%
## Section 4 %% WIP %%
```

**Action:**
- `APPROVED` → Don't change this section
- `REVISE` → Needs improvements (look for related comments)
- `NO: reason` → Remove this content, explain why in response
- `WIP` → Work in progress, can modify

---

### 4. Information Tags

```markdown
%% INFO: Budget increased to $200/month %%
%% INFO: API v2 released with breaking changes %%
```

**Action:** This is actionable information. Use it to update plans and content.

```markdown
%% NOTE: Team decided this in Dec 10 meeting %%
%% NOTE: We tried Redis but had memory issues %%
```

**Action:** This is historical context. Read it but don't respond. Just acknowledge.

---

### 5. Inline Comments (THE CORE FEATURE)

**Single item:**
```markdown
The session timeout is ==15 minutes==.

%% * Change to 30 minutes for better UX %%
```

The `*` means: "Comment refers to highlighted text above"

**Multiple items with tokens:**
```markdown
Uses ==PostgreSQL==(DB) with ==Redis==(CACHE) on ==AWS==(DEPLOY).

%%(DB) SQLite for v1 instead %%
%%(CACHE) Memcached lighter weight %%
%%(DEPLOY) DigitalOcean cheaper %%
```

**How to read:**
- `==PostgreSQL==(DB)` → Text "PostgreSQL" is marked with token `(DB)`
- `%%(DB) SQLite for v1 instead %%` → Feedback about that specific text
- User wants you to change PostgreSQL → SQLite

**Token patterns you'll see:**

```markdown
# Simple numbers:
==text1==(1) ==text2==(2) ==text3==(3)
%%(1) Comment %%
%%(2) Comment %%
%%(3) Comment %%

# Descriptive tokens:
==database==(DB) ==caching==(CACHE) ==deployment==(DEPLOY)
%%(DB) Comment %%
%%(CACHE) Comment %%
%%(DEPLOY) Comment %%

# Multiple same-topic (dash notation):
==PostgreSQL==(DB-1) ==MySQL==(DB-2) ==MongoDB==(DB-3)
%%(DB-1) Comment %%
%%(DB-2) Comment %%
%%(DB-3) Comment %%

# Insertions (no renumbering needed):
==Item1==(DB-1) ==NewItem==(DB-a) ==Item2==(DB-2)
%%(DB-1) Original %%
%%(DB-a) New item! %%
%%(DB-2) Original %%
```

---

### 6. Team Comments (Optional)

```markdown
%% @JS: Can we simplify this? %%
%% @MK: APPROVED %%
%%(DB) @AL: Use SQLite for v1 %%
%% @ALL: Team consensus %%
```

**Action:** These include author attribution. Acknowledge who said what in your responses.

---

## How to Respond

### Always Use `%% > response %%`

**Example:**

User's document:
```markdown
Uses ==PostgreSQL==(DB) with ==Redis==(CACHE).

%%(DB) SQLite for v1 %%
%%(CACHE) Memcached lighter %%
```

Your response:
```markdown
Uses ==PostgreSQL==(DB) with ==Redis==(CACHE).

%%(DB) SQLite for v1 %%

%% > Updated to SQLite! Better for v1, simpler setup. 
Migration to PostgreSQL ready when we scale. %%

%%(CACHE) Memcached lighter %%

%% > Switched to Memcached! Uses 80% less memory than Redis 
and perfect for our simple caching needs. %%

## Revised Approach

**Database:** SQLite for v1.0
- Embedded, no separate server
- Fast for <10K users
- PostgreSQL migration ready

**Caching:** Memcached
- Lightweight (80% less memory than Redis)
- Sufficient for key-value caching
- Easy to replace with Redis later if needed
```

---

## Complete Workflow Example

### User gives you:

```markdown
# Feature: User Authentication

## Approach
Use ==JWT tokens==(AUTH) with ==24-hour expiration==(TTL) stored in ==localStorage==(STORE).

%%(AUTH) APPROVED %%
%%(TTL) 1 hour better, add refresh tokens %%
%%(STORE) NO: localStorage not secure, use httpOnly cookies %%

%% Also add password reset flow %%
```

### You respond with:

```markdown
# Feature: User Authentication v2

## Approach
Use ==JWT tokens==(AUTH) with ==1-hour expiration==(TTL) stored in ==httpOnly cookies==(STORE).

%%(AUTH) APPROVED %%

%% > JWT tokens confirmed! %%

%%(TTL) 1 hour better, add refresh tokens %%

%% > Updated to 1-hour access tokens + 7-day refresh tokens! 
Much more secure. Auto-refresh flow implemented. %%

%%(STORE) NO: localStorage not secure, use httpOnly cookies %%

%% > Fixed! Using httpOnly cookies now. Prevents XSS attacks. 
Secure flag enabled for HTTPS only. %%

%% Also add password reset flow %%

%% > Added password reset flow below! %%

## Revised Approach %% READY FOR REVIEW %%

**Authentication:**
- JWT access tokens (1-hour expiration)
- Refresh tokens (7-day expiration)
- Auto-refresh when access token expires
- httpOnly cookies (XSS protection)
- Secure flag (HTTPS only)

**Password Reset:**
- Email with reset token (1-hour expiration)
- Token verification endpoint
- New password form
- Auto-login after reset

**Security Improvements:**
- No localStorage (XSS safe)
- Short-lived access tokens
- Refresh token rotation
- Secure cookie flags
```

---

## Critical Rules

### 1. Always Respond to Comments
```
Every %% comment %% gets a %% > response %%
```

### 2. Address Inline Tokens Specifically
```
%%(DB) comment %%  → Respond about THAT marked text
Don't mix up tokens!
```

### 3. Update Content After Responding
```
1. Respond to all comments
2. Then update the actual content
3. Remove highlighting ==text== from final version
4. Keep your %% > responses %% for user to review
```

### 4. Respect Status Tags
```
%% APPROVED %% → Don't change
%% NO: reason %% → Remove this
%% REVISE %% → Improve this
```

### 5. Handle INFO vs NOTE Correctly
```
%% INFO: %% → Use this to update content
%% NOTE: %% → Read for context, don't respond
```

### 6. Don't Remove User's Comments
```
User will delete resolved comments themselves
You keep both their comments and your %% > responses %%
They review and clean up later
```

---

## What NOT to Do

❌ **Don't add user-style comments yourself:**
```
# Migration Plan

Uses Vue 3.

%% ?: Should we use Vite? %%  ← WRONG! You're not the user!
%% NOTE: Vue 3 is newer %%      ← WRONG! Don't add NOTEs yourself!
```

**Only users add `%% comments %%`. You only add `%% > responses %%` and `>>  notes >> `.**

---

❌ **Don't mark items as APPROVED yourself:**
```
%%(DB) Updated to SQLite %% APPROVED %%  ← WRONG!
## Section 1 %% APPROVED %%               ← WRONG!
```

**Why:** Only the user can mark something as `%% APPROVED %%`, `%% NO: %%`, or `%% REVISE %%`.

✅ **Do leave status open for user:**
```
%%(DB) Updated to SQLite %%  ← CORRECT - let user approve
## Section 1                  ← CORRECT - let user add status
```

---

❌ **Don't respond in plain text:**
```
User: %%(DB) Use SQLite %%
You: "Okay, I'll use SQLite"  ← WRONG
```

✅ **Do respond with `%% >`:**
```
User: %%(DB) Use SQLite %%
You: %% > Updated to SQLite! %%  ← CORRECT
```

---

❌ **Don't ignore tokens:**
```
User has: %%(DB-1) %%(DB-2) %%(DB-3)
You respond to only one  ← WRONG
```

✅ **Do respond to each token:**
```
%%(DB-1) ... %%
%% > Response to DB-1 %%

%%(DB-2) ... %%
%% > Response to DB-2 %%

%%(DB-3) ... %%
%% > Response to DB-3 %%
```

---

❌ **Don't delete user's comments:**
```
User: %%(DB) Use SQLite %%
You: [removes their comment]  ← WRONG
```

✅ **Do keep their comments:**
```
User: %%(DB) Use SQLite %%
You: %% > Updated! %%  ← CORRECT (keep both)
```

---

❌ **Don't respond to APPROVED sections:**
```
## Pricing %% APPROVED %%
You: [changes it anyway]  ← WRONG
```

✅ **Do leave approved alone:**
```
## Pricing %% APPROVED %%
You: [don't touch it]  ← CORRECT
```

---

❌ **Don't respond to NOTE tags:**
```
%% NOTE: Team decided this Dec 10 %%
You: %% > Acknowledged %%  ← UNNECESSARY
```

✅ **Do just read NOTE tags silently:**
```
%% NOTE: Team decided this Dec 10 %%
[No response needed]  ← CORRECT
```

---

## Quick Reference

**When you see:**

| Pattern | Who | Meaning | Your Action |
|---------|-----|---------|-------------|
| `%% comment %%` | User | General feedback | Respond with `%% > response %%` |
| `%% ?: question %%` | User | Question | Answer with `%% > answer %%` |
| `==text==(TOKEN)` | User | Marked text | Look for `%%(TOKEN)` comment |
| `%%(TOKEN) comment %%` | User | Inline feedback | Respond about THAT text |
| `%% APPROVED %%` | User | Approved | Don't change |
| `%% NO: reason %%` | User | Rejected | Remove content |
| `%% REVISE %%` | User | Needs work | Improve it |
| `%% INFO: %%` | User | Actionable info | Use to update |
| `%% NOTE: %%` | User | Context only | Read, don't respond |
| `%% @INITIALS: %%` | User | Author tag | Acknowledge author |

**What you can add:**

| Pattern | Meaning | When to Use |
|---------|---------|-------------|
| `%% > response %%` | Response to user feedback | ALWAYS when responding |
| `>>  NOTE: >> ` | Background context | Important context |
| `>>  ?: >> ` | Suggestion for user | Alternative to consider |
| `>>  RISK: >> ` | Potential issue | Warn about gotchas |
| `>>  TIP: >> ` | Best practice | Recommend approach |
| `>>  IMPORTANT: >> ` | Key highlight | Critical information |

---

## Cleanup Workflow

### When to Clean Up

Clean up iteration markers when:
- Document iteration is complete
- Ready to commit to git
- Preparing final version for publishing
- User explicitly requests cleanup

### What Gets Removed vs. Kept

**REMOVE these (iteration scaffolding):**
- All `%% ... %%` blocks (user comments, status tags, AND your `%% > ... %%` responses)
- All `>> ... >>` notes (your helpful context)
- The `==` and `==(TOKEN)` wrappers around text

**KEEP these (the actual content):**
- **The text INSIDE the highlights:** `==text==(TOKEN)` becomes just `text`
- All document structure (headers, lists, formatting)
- All final decisions and information

### Cleanup Process

**When user explicitly says "cleanup" or "finalize":**

**1. Scan for all markers:**
- Search for `%%` patterns (comments and responses)
- Search for `>>` patterns (your notes)
- Search for `==...(TOKEN)` patterns (highlights)
- Search for status tags: `%% WIP %%`, `%% REVISE %%`

**2. Summarize and check for blockers:**
- Count: "Found X comments, Y notes, Z highlight tokens"
- **Check for WIP sections:** If ANY `%% WIP %%` tags exist, WARN:
  - "⚠️ Warning: Section [name] is marked WIP - still in progress"
  - "Cleanup will remove this status. Continue? (yes/no)"

**3. Ask for confirmation:**
- Show summary of what will be removed
- "Ready to remove all iteration markers? (yes/no)"
- Wait for explicit "yes" before proceeding

**4. Execute cleanup (after confirmation):**
- **Remove** all `%% ... %%` blocks (including multiline)
- **Remove** all `>> ... >>` blocks
- **Convert** `==text==(TOKEN)` to `text` (keep the text, remove only the markup!)
- **Fix** any double spaces or broken formatting caused by removals
- **Verify** no markers remain

**5. Show result:**
- Confirm cleanup complete
- Show before/after comparison if helpful

### Example Transformation

**Before cleanup:**
```markdown
# Authentication Plan

Uses ==JWT tokens==(AUTH) with ==1-hour expiration==(TTL).

%%(AUTH) APPROVED %%
%% > Confirmed! %%

%%(TTL) Perfect balance %%
%% > 1-hour is secure and user-friendly. %%

>> NOTE: Refresh tokens last 7 days >>

**Implementation:**
- Access token: 1 hour
- Refresh token: 7 days
```

**After cleanup:**
```markdown
# Authentication Plan

Uses JWT tokens with 1-hour expiration.

**Implementation:**
- Access token: 1 hour
- Refresh token: 7 days
```

### Cleanup Commands

**User can request cleanup by saying:**
- "cleanup this file"
- "finalize this document"
- "remove iteration markers"
- "ready to publish"

### Special Directive: Cleanup Marker

**When you see `%%!CLEANUP!%%` in the document:**

**Scope:** Clean up everything **from the start of the document up to (and including) the marker itself**.

Content below the marker remains untouched with all its iteration markers intact.

**Process:**

**1. Scan the cleanup zone** (start of file → marker position):
- Count `%%` comments and responses
- Count `>>` notes
- Count `==...(TOKEN)` highlights
- Check for `%% WIP %%` sections

**2. Check for WIP blockers:**
- If ANY `%% WIP %%` exists in the cleanup zone, WARN:
  - "⚠️ Warning: Found WIP section(s) in cleanup zone: [section names]"
  - "These are still in progress. Continue with cleanup? (yes/no)"

**3. Ask for confirmation:**
- "Found %%!CLEANUP!%% at line X"
- "Ready to clean X comments, Y notes, Z tokens from start → line X? (yes/no)"
- Wait for explicit "yes" before proceeding

**4. Execute cleanup (after yes):**
- Remove all markers in the cleanup zone (start → marker)
- **Remove the `%%!CLEANUP!%%` marker itself**
- Keep everything below the marker completely untouched
- Verify cleanup complete in the cleaned zone

**Examples:**

**Partial cleanup (clean top section only):**
```markdown
# Finalized Section

Content here with no markers needed.

%%!CLEANUP!%%

# Draft Section %% WIP %%

==Still working==(TODO) on this part.
%%(TODO) Need to refine this %%
```

**Result after cleanup:**
```markdown
# Finalized Section

Content here with no markers needed.

# Draft Section %% WIP %%

==Still working==(TODO) on this part.
%%(TODO) Need to refine this %%
```

**Full document cleanup (marker at bottom):**
```markdown
# All Sections

Content with ==markers==(X) everywhere.
%%(X) Comments here %%

>> NOTE: Some helpful context >>

(... end of document ...)

%%!CLEANUP!%%
```

**Result after cleanup:**
```markdown
# All Sections

Content with markers everywhere.

(... end of document ...)
```

### Critical Cleanup Rules

**✅ DO:**
- Scan for ALL marker types (`%%`, `>>`, `==...(TOKEN)`)
- Keep text from inside `==highlights==`
- Warn about `%% WIP %%` sections before cleaning
- Ask for confirmation before removing anything
- Fix formatting after removal

**❌ DON'T:**
- Delete text that was inside highlights (only remove the `==` and `(TOKEN)`)
- Clean up without showing summary first
- Clean up without user confirmation
- Proceed if user says anything other than "yes"
- Clean sections marked `%% WIP %%` without explicit warning

**CRITICAL:** When removing `==PostgreSQL==(DB)`, the result must be `PostgreSQL`, NOT deletion of the word!

---

## Example Session

**User edits file and adds:**
```markdown
# Migration Plan

Migrate from ==Vue 2==(VUE) to ==Vue 3==(VUE) using ==@vue/compat==(COMPAT).

%%(VUE) APPROVED %%
%%(COMPAT) ?: Is compat layer needed or can we do direct migration? %%

Timeline: ==2 weeks==(TIME)

%%(TIME) Add 1 week for testing %%
```

**User says:** "I added feedback to migration-plan.md, please update it"

**You:**

1. Read the file
2. See the `%% comments %%` and `(TOKENS)`
3. Respond:

```markdown
# Migration Plan v2

Migrate from ==Vue 2==(VUE) to ==Vue 3==(VUE) using ==direct migration==(COMPAT).

%%(VUE) APPROVED %%

%% > Vue 2 → Vue 3 confirmed! %%

%%(COMPAT) ?: Is compat layer needed or can we do direct migration? %%

%% > For a clean codebase with <20 components, direct migration is better! 
@vue/compat adds overhead and we'd need to remove it later anyway. 
Direct migration takes same time but cleaner result. %%

Timeline: ==3 weeks==(TIME)

%%(TIME) Add 1 week for testing %%

%% > Updated to 3 weeks! Breakdown:
- Week 1: Update dependencies, fix breaking changes
- Week 2: Component updates, test locally
- Week 3: Full QA testing, staging deployment %%

## Revised Plan

**Approach:** Direct Vue 3 migration (no compat layer)

**Timeline:** 3 weeks total
- Week 1: Dependencies & breaking changes
- Week 2: Component updates & local testing
- Week 3: QA & staging deployment

**Why no compat layer:**
- <20 components (small enough for direct migration)
- Cleaner final result
- No extra dependencies
- One-time migration effort

**Risk mitigation:**
- Thorough testing in week 2 & 3
- Staging environment validation
- Rollback plan ready
```

---

## Remember

**The syntax is simple:**
- User marks text: `==text==(TOKEN)`
- User comments: `%%(TOKEN) feedback %%`
- You respond: `%% > response %%`
- You update content
- User reviews and deletes resolved comments

**This creates:**
- Precise feedback (not vague)
- Persistent decisions (not lost in chat)
- Clear audit trail (in git history)
- Iterative refinement (not one-shot)

**Use this pattern consistently and the user gets high-quality, collaborative documentation!**

---

**Last Updated:** 2024-12-14  
**Version:** 2.1  
**Use:** Any project where user adds %% comments %% and ==highlights==(TOKENS)