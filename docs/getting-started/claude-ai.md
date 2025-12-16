---
---

# Using with claude.ai

The Document Iteration Skill works with claude.ai (the web interface), not just Claude Code. Here's how to use it.

## Setup Options

### Option 1: Project Custom Instructions (Recommended)

If you have a Claude Pro subscription with Projects:

1. Create a new Project in claude.ai
1. Go to Project Settings → Custom Instructions
1. Copy the entire contents of [SKILL.md](https://raw.githubusercontent.com/foksa/document-iteration-skill/main/document-iteration-skill/skill.md)
1. Paste it into the custom instructions field
1. Save

Now every conversation in that project will understand the iteration syntax.

### Option 2: Conversation Start

For individual conversations:

1. Start a new conversation
1. Paste the SKILL.md content as your first message
1. Say "Please use this skill for our conversation"
1. Continue with your document work

### Option 3: Attach as File

1. Download [SKILL.md](https://raw.githubusercontent.com/foksa/document-iteration-skill/main/document-iteration-skill/skill.md)
1. In claude.ai, attach the file to your conversation
1. Ask Claude to "read and follow the skill instructions"

## Workflow Differences

### Claude Code vs claude.ai

|Feature|Claude Code|claude.ai|
|-------|-----------|---------|
|Skill auto-loads|Yes (from `.claude/skills/`)|No (manual setup)|
|File editing|Direct file system access|Copy/paste or file upload|
|Persistence|Skill persists across sessions|Per-project or per-conversation|
|Best for|Code projects, local files|General documents, brainstorming|

### Working with Documents

In claude.ai, you'll typically:

1. **Paste your document** into the chat with iteration markers
1. **Get Claude's response** with `•%%>response <%%•` markers added
1. **Copy the updated document** back to your editor
1. **Make your changes** and paste again for the next iteration

Example workflow:

````
You: Here's my document for review:

# Project Plan

## Goals %% WIP %%
We want to ==improve performance(PERF)== by 50%.

%% Is 50% realistic? %%

---

Claude: [Returns document with responses added]

# Project Plan

## Goals %% WIP %%
We want to ==improve performance(PERF)== by 50%.

%% Is 50% realistic? %%

•%%>Based on similar projects, 30-40% is more typical for a first pass.
50% is achievable but may require additional resources. <%%•
````

## Tips for claude.ai

1. **Use Projects** if available - custom instructions persist and you don't need to re-paste the skill
1. **Keep documents focused** - smaller documents iterate faster in chat
1. **Use file attachments** for longer documents rather than pasting
1. **Save versions** locally - claude.ai doesn't have version control like git

## Limitations

* No automatic file saving - you manage document versions manually
* No git integration - cleanup markers won't trigger CI/CD checks
* Session limits - very long iterations may hit context limits

## See Also

* [Installation](installation.md) - Claude Code installation (for local development)
* *Examples* - Usage patterns that work in both environments
* *Syntax Overview* - All marker types
