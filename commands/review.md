---
description: Review a document and add comments using iteration marker syntax
argument-hint: [filepath]
---

Review the document at @$1 and add your feedback using the Document Iteration Skill syntax.

Read the skill at `.claude/skills/document-iteration-skill/SKILL.md` for the marker syntax.

Your task:
1. Read the document carefully
2. Add inline comments using `•%%> your comment <%%•` syntax where you have suggestions, questions, or observations
3. For precise references, use `==highlighted text(TOKEN)==` with `•%%>(TOKEN) your comment <%%•`
4. Focus on being helpful - point out issues, suggest improvements, ask clarifying questions
5. Don't remove or modify the original content, only add your comments
