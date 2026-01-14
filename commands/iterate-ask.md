---
description: Process iteration markers with user choice on how to respond
argument-hint: [filepath]
---

Process the document at @$1 using the Document Iteration Skill.

Read the skill at `.claude/skills/document-iteration-skill/SKILL.md` and follow it.

After reading the document and understanding the user's comments, ask the user how they want to proceed:

1. **Respond inline** - Add your responses as comments in the document without modifying original content
2. **Respond and update** - Add responses AND apply agreed changes to the document
3. **Discuss first** - Let's discuss in chat before making any changes to the document

Then proceed based on their choice.
