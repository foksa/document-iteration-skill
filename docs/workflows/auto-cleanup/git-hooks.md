---
---

# Git Hooks

A pre-commit hook that scans for iteration markers and blocks commits if found. Works independently of Claude.

## How It Works

Git runs the hook script before each commit. If markers are found, the commit is blocked with an error message.

## Setup

Create `.git/hooks/pre-commit`:

````bash
#!/bin/bash

# Check for iteration markers in staged files
# Patterns: %% comment %%, %%>response <%%, ==text(TOKEN)==
MARKERS=$(git diff --cached --name-only | xargs grep -l -E '%%[^%]*%%|%%>[^<]*<%%|==[^=]*\([^)]+\)==' 2>/dev/null)

if [ -n "$MARKERS" ]; then
    echo "❌ Commit blocked: iteration markers found"
    echo ""
    echo "Files with markers:"
    echo "$MARKERS" | sed 's/^/  - /'
    echo ""
    echo "Clean up markers before committing, or use --no-verify to skip this check."
    exit 1
fi

exit 0
````

Make it executable:

````bash
chmod +x .git/hooks/pre-commit
````

## Sharing with Team

Git hooks aren't committed by default. To share:

**Option 1: Committed hooks folder**

````bash
# In your repo
mkdir .githooks
mv .git/hooks/pre-commit .githooks/

# Team members run:
git config core.hooksPath .githooks
````

**Option 2: npm/package.json**

````json
{
  "scripts": {
    "prepare": "git config core.hooksPath .githooks"
  }
}
````

**Option 3: Husky (popular choice)**

````bash
npm install husky --save-dev
npx husky install
npx husky add .husky/pre-commit "npm run check-markers"
````

## Bypassing

When you intentionally want to commit markers:

````bash
git commit --no-verify -m "WIP: draft with markers"
````

## Limitations

* Only checks staged files (not all files)
* Doesn't help during editing
* Can be bypassed (use CI/CD as backup)

## Related

* [Auto-Cleanup Approaches](../../examples/sessions/index.md) - All approaches
* [CI/CD Check](ci-cd.md) - Server-side verification
