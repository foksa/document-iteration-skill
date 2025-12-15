---
---

# Your First Iteration

This guide walks you through your first document iteration with Claude. In 5 minutes, you'll understand the core workflow.

## Prerequisites

* Document Iteration Skill installed ([Installation](installation.md))
* A markdown file to work with

## Step 1: Create a Document

Create a simple markdown file. For this example, we'll use a project brief:

````markdown
# Project Brief

## Overview

We're building a task management app for small teams.

## Features

- Task creation and assignment
- Due dates and reminders
- Team collaboration
````

## Step 2: Add Your First Comment

Add a `%% comment %%` anywhere you want feedback:

````markdown
# Project Brief

## Overview

We're building a task management app for small teams.

%% Is this scope too broad? Should we narrow it? %%

## Features

- Task creation and assignment
- Due dates and reminders
- Team collaboration
````

## Step 3: Ask Claude to Respond

Send the file to Claude with a request like:

* "Review this document"
* "Respond to the comments"
* "Update this file"

## Step 4: See the Response

Claude adds a response below your comment:

````markdown
# Project Brief

## Overview

We're building a task management app for small teams.

%% Is this scope too broad? Should we narrow it? %%

•%%>The scope is reasonable for an MVP. Consider starting with just
task creation and due dates, then adding collaboration in v2. <%%•

## Features

- Task creation and assignment
- Due dates and reminders
- Team collaboration
````

Notice:

* Your comment stays in place
* Claude's response uses `•%%>response <%%•` syntax
* The conversation is preserved in the document

## Step 5: Try a Highlight

Mark specific text that needs attention using `==text(TOKEN)==`:

````markdown
## Features

- Task creation and assignment
- ==Due dates and reminders(MVP)==
- Team collaboration

%%(MVP) Should reminders be in v1 or v2? %%
````

The token `(MVP)` links the highlight to your comment. **Note: token goes INSIDE the highlight.**

## Step 6: Continue the Conversation

Add more comments, get more responses. The document becomes a record of the iteration:

````markdown
%% Is this scope too broad? Should we narrow it? %%

•%%>The scope is reasonable for an MVP. <%%•

%% Agreed, let's keep it focused %%

•%%>Perfect. I'll update the features list to reflect MVP scope. <%%•
````

## Step 7: Clean Up When Done

When you're satisfied, ask Claude to clean up:

* "Clean up this document"
* "Remove all markers"

The markers disappear, leaving clean content:

````markdown
# Project Brief

## Overview

We're building a task management app for small teams.

## Features

- Task creation and assignment
- Due dates and reminders
````

## What You Learned

1. **Comments** (`%% %%`) - Add feedback anywhere
1. **Responses** (`•%%>response <%%•`) - Claude responds inline
1. **Highlights** (`==text(TOKEN)==`) - Mark specific text
1. **Cleanup** - Remove markers when done

## Next Steps

* *Examples* - See more usage patterns
* *Syntax Overview* - All marker types
* *Tokens* - Token naming conventions
