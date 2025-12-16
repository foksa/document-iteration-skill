# Changelog

All notable changes to the Document Iteration Skill.

## [5.1] - 2024-12-16

### Changed
- **Repo restructure** - Skill files now in `document-iteration-skill/` subfolder
  - Cleaner separation: skill folder contains only what Claude needs
  - Follows Claude Code skill packaging guidelines
  - Install commands updated to clone repo, copy skill folder

### Migration
If updating from v5.0 or earlier, reinstall with new commands:
```bash
rm -rf .claude/skills/document-iteration-skill
git clone --depth 1 https://github.com/foksa/document-iteration-skill.git /tmp/dis-temp && cp -r /tmp/dis-temp/document-iteration-skill .claude/skills/ && rm -rf /tmp/dis-temp
```

## [5.0] - 2024-12-16

### Changed
- **Bullet syntax for Claude responses** - Changed from `•%%> response %%•` to `•%%> response <%%•`
  - Closing marker now has `<` for visual symmetry: `•%%>` opens, `<%%•` closes
  - Easier to type and visually balanced

### Added
- **Editor configs** - Ready-to-copy configurations in `editor-configs/`
  - Obsidian: Regex Mark plugin + CSS snippets for marker styling
  - VS Code: TODO Highlight v2 settings + markdown snippets

## [4.0] - 2024-12-15

### Changed
- **Unified Claude response syntax** - All Claude output now uses `•%%> response <%%•`
  - Replaces both `%% > response %%` and `>> note >>`
  - Single consistent syntax for everything Claude writes
  - Bullet `•` makes Claude responses visually distinct from user `%%` comments

### Added
- **INFO vs NOTE distinction**
  - `%% INFO: %%` = Instructions for Claude (respond + act)
  - `%% NOTE: %%` = Context for humans (read silently)

### Removed
- `>> note >>` syntax (replaced by `•%%>`)
- `%% > response %%` syntax (replaced by `•%%>`)

## [3.0] - 2024-12-14

### Added
- **"Syntax Engine" identity** - Claude now operates as a syntax processor, not a chat assistant
- **Negative constraints** - Explicit "NEVER DO THIS" section to prevent common mistakes
- **Few-shot examples** - CORRECT vs INCORRECT output patterns for better adherence
- **Whitespace rule** - No space before `(TOKEN)`: `==text==(TOKEN)` not `==text== (TOKEN)`

### Improved
- Stronger rule enforcement with explicit examples
- Better distinction between user syntax (`%%`) and Claude syntax (`%% >`, `>>`)

## [2.3] - 2024-12-10

### Added
- `%%!CLEANUP!%%` marker for partial document cleanup
- Mandatory rules clarification: always respond, never remove comments
- Improved cleanup workflow with WIP section warnings

### Fixed
- Cleanup now properly warns about WIP sections before proceeding

## [2.2] - 2024-12-08

### Added
- Team collaboration syntax with `@INITIALS:` prefixes
- Status tags: `APPROVED`, `REVISE`, `NO:`, `WIP`
- `INFO:` vs `NOTE:` distinction (actionable vs context)

### Improved
- Token naming conventions (descriptive, numbered, dash notation)
- Documentation site structure

## [2.1] - 2024-12-05

### Added
- Claude's own notes with `>> NOTE: >>` syntax
- Multiple tag types: `RISK:`, `TIP:`, `IMPORTANT:`
- Insertion tokens with letter suffixes (`DB-a`, `DB-b`)

## [2.0] - 2024-12-01

### Added
- Token-based inline comments: `==text==(TOKEN)` + `%%(TOKEN) comment %%`
- Response syntax: `%% > response %%`
- Cleanup workflow section
- YAML frontmatter for skill discovery

### Changed
- Renamed from "Collaborative Workflow" to "Document Iteration Skill"

## [1.0] - 2024-11-15

### Added
- Initial release
- Basic `%% comment %%` syntax
- Simple `*` for inline comments on single items
- Core iteration workflow