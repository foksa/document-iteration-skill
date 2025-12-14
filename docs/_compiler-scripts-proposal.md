---
title: "_Compiler Scripts Proposal"
layout: default
---

# Compiler Scripts Proposal

**Status:** Draft
**Not linked from index** - internal planning document

---

## Overview

Create automated scripts to process documents with iteration markers, enabling:
- Accept/reject workflow for changes
- Clean final output generation
- CI/CD integration

---

## Use Cases

### 1. Full Cleanup
Strip all markers from a document to produce clean output.

```bash
cleanup doc.md > doc-clean.md
```

### 2. Accept All
Accept all proposed changes (apply highlights, keep responses as content).

```bash
cleanup --accept-all doc.md > doc-final.md
```

### 3. Lint/Check
Verify no markers remain before commit (for pre-commit hooks).

```bash
cleanup --check doc.md  # exits 1 if markers found
```

### 4. Interactive Review
TUI to accept/reject individual markers.

```bash
cleanup --interactive doc.md
```

---

## Markers to Handle

| Marker | Cleanup Behavior |
|--------|-----------------|
| `%% comment %%` | Remove entirely |
| `%% > response %%` | Remove entirely |
| `==text==(TOKEN)` | Keep `text`, remove highlight and token |
| `>> note >>` | Remove entirely |
| `%%!CLEANUP!%%` | Trigger partial cleanup (everything above) |

---

## Implementation Options

### Option A: Python Script

**Pros:**
- Rich ecosystem for text processing
- Easy regex handling
- Cross-platform

**Cons:**
- Requires Python installation

```python
# cleanup.py
import re
import sys

def cleanup(content: str) -> str:
    # Remove comments and responses
    content = re.sub(r'%%[^%]*%%', '', content)
    # Remove highlights, keep text
    content = re.sub(r'==([^=]+)==\s*\([A-Z_]+\)', r'\1', content)
    # Remove notes
    content = re.sub(r'>>[^>]+>>', '', content)
    return content
```

### Option B: Node.js Script

**Pros:**
- NPM distribution
- JavaScript ecosystem alignment

**Cons:**
- Requires Node installation

```javascript
// cleanup.js
const cleanup = (content) => {
  return content
    .replace(/%%[^%]*%%/g, '')
    .replace(/==([^=]+)==\s*\([A-Z_]+\)/g, '$1')
    .replace(/>>[^>]+>>/g, '');
};
```

### Option C: Shell Script (grep/sed)

**Pros:**
- No dependencies
- Unix-native

**Cons:**
- Complex regex in sed
- Less portable (Windows)

```bash
#!/bin/bash
sed -E \
  -e 's/%%[^%]*%%//g' \
  -e 's/==([^=]+)==\s*\([A-Z_]+\)/\1/g' \
  -e 's/>>[^>]+>>//g' \
  "$1"
```

---

## Recommended Approach

**Start with Python** because:
1. Most readable/maintainable
2. Easy to add features (interactive mode)
3. Works with existing lint-rules.md patterns
4. Can package as standalone binary with PyInstaller if needed

---

## Integration Points

### Pre-commit Hook
```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: no-iteration-markers
      name: Check for iteration markers
      entry: python cleanup.py --check
      language: python
      types: [markdown]
```

### GitHub Action
```yaml
- name: Check for markers
  run: python scripts/cleanup.py --check docs/*.md
```

### NPM Script
```json
{
  "scripts": {
    "cleanup": "python scripts/cleanup.py",
    "cleanup:check": "python scripts/cleanup.py --check"
  }
}
```

---

## CLI Design

```
cleanup [OPTIONS] FILE...

Options:
  --check         Check only, exit 1 if markers found
  --accept-all    Accept all changes (keep highlighted text)
  --reject-all    Reject all changes (remove highlighted text)
  --interactive   Interactive accept/reject
  --in-place      Modify file in place
  --output FILE   Write to specific file
  --verbose       Show what was removed
```

---

## Future Enhancements

1. **VS Code Extension** - GUI for accept/reject
2. **Obsidian Plugin** - Native cleanup command
3. **Diff Preview** - Show before/after
4. **Partial Cleanup** - Handle `%%!CLEANUP!%%` sections

---

## Action Items

- [ ] Create `scripts/cleanup.py` with basic cleanup
- [ ] Add `--check` flag for pre-commit
- [ ] Add to README installation instructions
- [ ] Create GitHub Action workflow
- [ ] Document in workflows/auto-cleanup/