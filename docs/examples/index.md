---
---

# Examples

Quick examples showing the Document Iteration Skill syntax in action. For complete iteration walkthroughs, see the [Session Examples](sessions/index.md).

## Quick Snippets

### Basic Comment and Response

````markdown
%% This section needs more detail %%

%%>Added specific metrics and timeline. <%%
````

### Highlighted Text with Token

````markdown
The API uses ==REST(STYLE)== for communication.

%%(STYLE) Consider GraphQL for flexibility %%

%%>Good point! Added GraphQL endpoint for complex queries. <%%
````

### Status Tags

````markdown
## Authentication %% APPROVED %%

## Payment Processing %% WIP %%

## Admin Panel %% REVISE %%
````

### Question Syntax

````markdown
%% ?: Should we support annual billing? %%

%%>Yes! Added 20% discount for annual plans. <%%
````

### Multiple Tokens

````markdown
Deploy on ==Kubernetes(INFRA)== with ==3 replicas(SCALE)==.

%%(INFRA) NO: Too complex for MVP - use EC2 %%
%%(SCALE) REVISE - start with 1, add autoscaling %%
````

### Team Attribution

````markdown
%%(FORMAT) @AL: Switch to JSON %%
%%(FORMAT) @MK: Agreed, JSON is standard %%
%%(FORMAT) @JS: APPROVED for JSON switch %%
````

## By Use Case

### Software Development

* API design review
* Migration planning
* Architecture decisions
* Code review feedback

### Creative Writing

* Story feedback
* Character development
* Plot suggestions

### Documentation

* Technical specifications
* Research requests
* Accuracy checks

### Project Planning

* Feature prioritization
* Timeline review
* Resource allocation

## Full Session Examples

For complete iteration sessions showing the full workflow from start to finish:

* [All Session Examples](sessions/index.md)
* [API Design Session](sessions/api-design.md) - Designing a REST API
* [Migration Planning](sessions/migration-plan.md) - Vue 2 to Vue 3 migration

## See Also

* *Syntax Overview* - All marker types
* *Tokens* - Token naming conventions
* *FAQ* - Common questions
