---
title: "Api Design"
layout: default
---

# API Design Session

A complete iteration session designing a REST API for a task management application.

## Round 1: Initial Draft

User creates the initial API design document:

```markdown
# Task API Design

## Overview

REST API for task management with ==JSON==(FORMAT) responses.

## Endpoints

### Tasks

- `GET /tasks` - List all tasks
- `POST /tasks` - Create task
- `GET /tasks/:id` - Get single task
- `PUT /tasks/:id` - Update task
- `DELETE /tasks/:id` - Delete task

### Authentication

Use ==API keys==(AUTH) in headers.

## Rate Limiting

==100 requests per minute==(RATE) per API key.
```

User adds feedback:

```markdown
# Task API Design

## Overview

REST API for task management with ==JSON==(FORMAT) responses.

%%(FORMAT) APPROVED %%

## Endpoints

### Tasks

- `GET /tasks` - List all tasks
- `POST /tasks` - Create task
- `GET /tasks/:id` - Get single task
- `PUT /tasks/:id` - Update task
- `DELETE /tasks/:id` - Delete task

%% Missing: filtering, pagination, sorting for GET /tasks %%

### Authentication

Use ==API keys==(AUTH) in headers.

%%(AUTH) ?: Should we use JWT instead for user-specific access? %%

## Rate Limiting

==100 requests per minute==(RATE) per API key.

%%(RATE) Too low for production - what do competitors use? %%
```

## Round 2: Claude Responds

Claude responds to each comment:

```markdown
# Task API Design

## Overview

REST API for task management with ==JSON==(FORMAT) responses.

%%(FORMAT) APPROVED %%

%% > JSON confirmed! %%

## Endpoints

### Tasks

- `GET /tasks` - List all tasks
- `POST /tasks` - Create task
- `GET /tasks/:id` - Get single task
- `PUT /tasks/:id` - Update task
- `DELETE /tasks/:id` - Delete task

%% Missing: filtering, pagination, sorting for GET /tasks %%

%% > Added query parameters:
- `?status=pending|done` - Filter by status
- `?page=1&limit=20` - Pagination (default 20, max 100)
- `?sort=created_at|-created_at` - Sort asc/desc
- `?assignee=user_id` - Filter by assignee %%

### Authentication

Use ==API keys==(AUTH) in headers.

%%(AUTH) ?: Should we use JWT instead for user-specific access? %%

%% > Great question! Recommendation:
- **API keys** for server-to-server (simpler, no expiry management)
- **JWT** for user-facing apps (user context, refresh tokens)

Both can coexist. Start with API keys for MVP, add JWT in v2? %%

## Rate Limiting

==100 requests per minute==(RATE) per API key.

%%(RATE) Too low for production - what do competitors use? %%

%% > Research complete:
- Asana: 1,500/min
- Todoist: 450/min
- ClickUp: 100/min (but per endpoint)

Recommendation: **500/min** with burst allowance of 50 extra.
Enterprise tier: 2,000/min. %%

## Updated Endpoints

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List tasks (with filters) |
| POST | `/tasks` | Create task |
| GET | `/tasks/:id` | Get single task |
| PUT | `/tasks/:id` | Update task |
| DELETE | `/tasks/:id` | Delete task |

**Query Parameters for GET /tasks:**
- `status` - Filter: pending, done, all (default: all)
- `page` - Page number (default: 1)
- `limit` - Items per page (default: 20, max: 100)
- `sort` - Sort field with optional `-` prefix for desc
- `assignee` - Filter by user ID
```

## Round 3: User Reviews

User reviews and adds more feedback:

```markdown
### Authentication

Use ==API keys==(AUTH) in headers.

%%(AUTH) ?: Should we use JWT instead for user-specific access? %%

%% > Great question! Recommendation:
- **API keys** for server-to-server
- **JWT** for user-facing apps

Both can coexist. Start with API keys for MVP, add JWT in v2? %%

%% Yes, API keys first. Add JWT to roadmap %%

## Rate Limiting

==100 requests per minute==(RATE) per API key.

%%(RATE) Too low for production - what do competitors use? %%

%% > Research complete... Recommendation: **500/min** %%

%% APPROVED - go with 500/min standard, 2000/min enterprise %%
```

## Round 4: Final Responses

Claude confirms the decisions:

```markdown
%%(AUTH) ?: Should we use JWT instead for user-specific access? %%

%% > Great question! Both can coexist. Start with API keys for MVP, add JWT in v2? %%

%% Yes, API keys first. Add JWT to roadmap %%

  %% > Perfect! API keys for MVP. Added JWT to v2 roadmap. %%

## Rate Limiting

==100 requests per minute==(RATE) per API key.

%%(RATE) Too low for production - what do competitors use? %%

%% > Research complete... Recommendation: **500/min** %%

%% APPROVED - go with 500/min standard, 2000/min enterprise %%

  %% > Confirmed! Rate limits set:
     - Standard: 500 req/min
     - Enterprise: 2,000 req/min
     - Burst: +50 allowance %%
```

## Final: After Cleanup

User requests cleanup. The final document:

```markdown
# Task API Design

## Overview

REST API for task management with JSON responses.

## Endpoints

### Tasks

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List tasks (with filters) |
| POST | `/tasks` | Create task |
| GET | `/tasks/:id` | Get single task |
| PUT | `/tasks/:id` | Update task |
| DELETE | `/tasks/:id` | Delete task |

**Query Parameters for GET /tasks:**
- `status` - Filter: pending, done, all (default: all)
- `page` - Page number (default: 1)
- `limit` - Items per page (default: 20, max: 100)
- `sort` - Sort field with optional `-` prefix for desc
- `assignee` - Filter by user ID

### Authentication

API keys in headers for MVP. JWT for user-facing apps planned for v2.

## Rate Limiting

- Standard: 500 requests/min
- Enterprise: 2,000 requests/min
- Burst allowance: +50 requests
```

## Key Takeaways

This session demonstrated:
- **Token usage** - `(FORMAT)`, `(AUTH)`, `(RATE)` for specific items
- **Question syntax** - `?: ...` for decisions needing input
- **Research requests** - Asking Claude to gather data
- **Decision flow** - Question → response → approval
- **Cleanup** - Removing all markers for final document

## See Also

- [Migration Planning Session](migration-plan.md) - Another complete walkthrough
- [Quick Examples](../index.md) - Short syntax snippets