---
---

# CI/CD Check

A GitHub Action (or similar) that fails PRs containing iteration markers. The final safety net for teams.

## How It Works

When code is pushed or a PR is opened, the CI pipeline scans for markers. If found, the check fails and blocks merge.

## GitHub Actions Setup

Create `.github/workflows/check-markers.yml`:

````yaml
name: Check Iteration Markers

on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  check-markers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for iteration markers
        run: |
          # Find all markdown files with markers
          # Patterns: %% comment %%, %%>response <%%, ==text(TOKEN)==
          FOUND=$(grep -r -l -E '%%[^%]*%%|%%>[^<]*<%%|==[^=]*\([^)]+\)==' --include="*.md" . 2>/dev/null || true)

          if [ -n "$FOUND" ]; then
            echo "❌ Iteration markers found in:"
            echo "$FOUND" | sed 's/^/  - /'
            echo ""
            echo "Please clean up markers before merging."
            exit 1
          fi

          echo "✅ No iteration markers found"
````

## Customization

### Exclude Certain Files

````yaml
- name: Check for iteration markers
  run: |
    FOUND=$(grep -r -l -E '%%[^%]*%%|%%>[^<]*<%%|==[^=]*\([^)]+\)==' \
      --include="*.md" \
      --exclude="SKILL.md" \
      --exclude-dir="examples" \
      . 2>/dev/null || true)
````

### Only Check Changed Files

````yaml
- name: Get changed files
  id: changed
  uses: tj-actions/changed-files@v40
  with:
    files: '**/*.md'

- name: Check for iteration markers
  if: steps.changed.outputs.any_changed == 'true'
  run: |
    echo "${{ steps.changed.outputs.all_changed_files }}" | tr ' ' '\n' | xargs grep -l -E '%%[^%]*%%' || true
````

### Show Marker Locations

````yaml
- name: Check for iteration markers
  run: |
    MATCHES=$(grep -r -n -E '%%[^%]*%%|%%>[^<]*<%%|==[^=]*\([^)]+\)==' --include="*.md" . 2>/dev/null || true)

    if [ -n "$MATCHES" ]; then
      echo "❌ Iteration markers found:"
      echo "$MATCHES"
      exit 1
    fi
````

## Other CI Systems

### GitLab CI

````yaml
check-markers:
  script:
    - grep -r -l -E '%%[^%]*%%' --include="*.md" . && exit 1 || exit 0
````

### CircleCI

````yaml
jobs:
  check-markers:
    docker:
      - image: alpine
    steps:
      - checkout
      - run:
          name: Check for markers
          command: |
            ! grep -r -l -E '%%[^%]*%%' --include="*.md" .
````

## Benefits

* Can't be bypassed (unlike local hooks)
* Visible to whole team
* Works regardless of local setup
* Documents cleanup expectations

## Limitations

* Only catches at PR/push time (not during development)
* Adds CI time
* Requires CI infrastructure

## Related

* [Auto-Cleanup Approaches](../../examples/sessions/index.md) - All approaches
* [Git Hooks](git-hooks.md) - Local pre-commit check
