# Changelog

All notable changes to the Document Iteration Skill.

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