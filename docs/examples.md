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
%% add claude responses also to examples above%%

%% > Done! Added Claude responses to all three examples above. %%


%%
Add more examples

use something like these sentences in comments

This looks vague, could you be more precise
Research on topic and add something

Be creative :)
%%

%% > Added several new examples below showing real feedback patterns! %%
%% Also include Claude responses in examples%%

%% > Done! Added Claude's `%% > response %%` to each example below. %%

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

## See Also

- [FAQ](faq.md) - Common questions
- [Contributing](contributing.md) - Help improve these docs