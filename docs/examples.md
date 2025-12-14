---
title: "Examples"
layout: default
---

# Examples

Real-world examples of the Document Iteration Skill in action.

## Software Development

### API Design Review

```markdown
The API uses ==REST==(STYLE) with ==JSON==(FORMAT) responses.

%%(STYLE) Consider GraphQL for flexibility %%

%% > Good point! For this use case REST is simpler, but I've added
a GraphQL endpoint for complex nested queries. Best of both worlds. %%

%%(FORMAT) APPROVED %%

%% > JSON confirmed! %%
```

### Migration Planning

```markdown
Migrate from ==Vue 2==(VUE) to Vue 3 using ==@vue/compat==(COMPAT).

%%(VUE) APPROVED %%

%% > Vue 2 → Vue 3 migration confirmed! %%

%%(COMPAT) ?: Direct migration instead? %%

%% > Yes! With <15 components, direct migration is cleaner.
Removes compat layer overhead and gives us Vue 3 features immediately. %%
```

## Creative Writing

### Story Feedback

```markdown
The hero ==defeats the dragon==(ENDING).

%%(ENDING) Too predictable - try a twist %%

%% > Plot twist added! The dragon was protecting the village
from a greater threat. Hero and dragon now team up. %%
```


## Documentation Review

### Technical Specification

```markdown
The system handles ==up to 1000 requests==(SCALE) per second.

%% This looks vague, could you be more precise? What's the actual benchmark? %%

%% > Updated to specific benchmark data:
- Peak: 1,247 req/s (load test Dec 2024)
- Sustained: 800 req/s with <50ms p99 latency
- Tested on 2x c5.xlarge instances %%
```

### Research Request

```markdown
## Caching Strategy

We'll use ==in-memory caching==(CACHE).

%%(CACHE) Research on topic and add something - what are the tradeoffs? %%

%% > Added tradeoffs analysis:
**In-memory pros:** Ultra-fast (<1ms), simple setup
**In-memory cons:** Lost on restart, limited by RAM, not shared across instances
**Alternative:** Redis for persistence + clustering if needed later %%
```

## Project Planning

### Feature Prioritization

```markdown
## Q1 Roadmap

- ==User dashboard==(DASH)
- ==Payment integration==(PAY)
- ==Email notifications==(EMAIL)

%%(DASH) APPROVED %%
%%(PAY) Move to Q2 - need legal review first %%
%%(EMAIL) ?: Can we use existing notification service instead of building new? %%
```

### Architecture Decision

```markdown
Deploy on ==Kubernetes==(INFRA) with ==3 replicas==(SCALE).

%%(INFRA) NO: Too complex for MVP - use simple EC2 %%
%%(SCALE) REVISE - start with 1, add autoscaling %%
```

## Team Collaboration

### Multi-Reviewer Feedback

```markdown
The API returns ==XML==(FORMAT) responses.

%%(FORMAT) @AL: Switch to JSON %%
%%(FORMAT) @MK: Agreed, JSON is standard now %%
%%(FORMAT) @JS: APPROVED for JSON switch %%
```

### Status Tracking

```markdown
## Authentication %% APPROVED %%

## Payment Processing %% WIP %%

## Admin Panel %% REVISE %%

%% Admin panel needs role-based access control %%
```

## Commenting on Code Inside Code Blocks

Since markers inside code blocks are ignored, you can't put feedback directly in the code. Instead, reference the code from **outside** the block.

### Method 1: Line References

```markdown
` ` `python
def process_data(items):
    results = []
    for item in items:
        results.append(item * 2)  # Line 4
    return results
` ` `

%% Line 4: Use list comprehension instead %%
```

### Method 2: Token Above the Block

```markdown
==Process function==(PERF)

` ` `python
def process_data(items):
    results = []
    for item in items:
        results.append(item * 2)
    return results
` ` `

%%(PERF) This could be a one-liner with list comprehension %%
```

### Method 3: Multiple Concerns

```markdown
==Authentication logic==(AUTH) ==Error handling==(ERR)

` ` `python
def login(username, password):
    user = db.find_user(username)
    if user and user.check_password(password):
        return create_token(user)
    return None
` ` `

%%(AUTH) Should we add rate limiting here? %%
%%(ERR) Returning None is unclear - raise an exception instead? %%
```

**Key insight:** Put the highlight/token **before** the code block, then add your comment referencing that token.

---

## Iterating on Documentation (Meta Example)

When iterating on files that **contain syntax examples** (like this page), markers in code blocks are ignored. Real feedback goes **outside** the code blocks.

### Example: Improving a Tutorial

**The document being iterated:**

```markdown
# Tutorial: Adding Comments

Here's how to add a comment:

` ` `markdown
%% Your comment here %%
` ` `

Comments help you give feedback.
```

**Adding real feedback (outside code blocks):**

```markdown
# Tutorial: Adding Comments

%% Add an example showing a response too %%

Here's how to add a comment:

` ` `markdown
%% Your comment here %%
` ` `

Comments help you give feedback.

%% This last sentence is too vague - expand it %%
```

**Claude responds to the REAL markers, ignores the example:**

```markdown
# Tutorial: Adding Comments

%% Add an example showing a response too %%

%% > Added response example below! %%

Here's how to add a comment:

` ` `markdown
%% Your comment here %%
` ` `

And here's how Claude responds:

` ` `markdown
%% Your comment here %%

%% > Claude's response to your comment %%
` ` `

Comments help you give precise, inline feedback that stays with your content.

%% This last sentence is too vague - expand it %%

%% > Expanded! Now explains the benefit of inline feedback. %%
```

**Key point:** The `%% Your comment here %%` inside the code fence was never treated as real feedback - it's just an example for the tutorial.

## See Also

- [FAQ](reference/faq.md) - Common questions
- [Contributing](meta/contributing.md) - Help improve these docs