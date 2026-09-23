# Editor Setup

Highlighting makes the two voices easy to tell apart: user markers in muted gold (`#968748`), Claude markers in teal (`#3C8C8C`). Ready-made configs for VSCode and Obsidian are in `assets/editor-configs/` inside this skill's folder. Below, `<skill>` stands for that folder's path (for example `.claude/skills/document-iteration-skill`).

When copying configs, add files that are missing and leave the user's existing files as they are. Where a file already exists, merge the relevant keys into it and tell the user what you merged.

## VSCode

1. Copy `<skill>/assets/editor-configs/vscode/.vscode/` into the project's `.vscode/`:
   - `settings.json`: TODO Highlight rules for `%%`, `•%%>`, `<%%•`. Merge into an existing file.
   - `markdown.code-snippets`: snippets (`%%` + Tab → comment, `%%?` → question, `%%a` → APPROVED, `==(` → wrap selection in a token).
   - `extensions.json`: recommends the highlighter extension.
2. `keybindings.json` is a user-level file in VSCode, so a copy in the project folder has no effect. Show the user its contents and suggest they add them via "Preferences: Open Keyboard Shortcuts (JSON)".
3. Tell the user to install **TODO Highlight v2** (`jgclark.vscode-todo-highlight`).

## Obsidian

Given a vault path `<vault>`:

1. Copy `<skill>/assets/editor-configs/obsidian/.obsidian/` into `<vault>/.obsidian/`, adding only missing files (`cp -rn`). This brings the Regex Mark plugin with its patterns and the `iteration-markers.css` snippet.
2. If `<vault>/.obsidian/appearance.json` already existed, add `"iteration-markers"` to its `enabledCssSnippets` array.
3. Detect the link style from `<vault>/.obsidian/app.json`: `"useMarkdownLinks": true` means `[text](file.md)` links; `false` or a missing key means `[[wikilinks]]`. If `app.json` is missing, ask the user. Record the answer in the project's CLAUDE.md:
   ```markdown
   ## Obsidian vault: <vault>
   Use [wikilinks | markdown links] for internal links.
   ```
4. Tell the user to enable **Regex Mark** under Settings → Community plugins, and to check it for updates.

Obsidian already treats `%% … %%` as a comment, so iteration markers stay hidden in reading view.

## JetBrains IDEs

Settings → Editor → TODO → add patterns:

- `\%\%[^%]*\%\%`: user comments
- `•\%\%>.*<\%\%•`: Claude responses
- `==[^=]*\([^)]*\)==`: highlights

## Vim / Neovim

```vim
syntax match IterationUser /%%[^%]*%%/
syntax match IterationClaude /•%%>.\{-}<%%•/
syntax match IterationHighlight /==[^=]*([^)]*)==/
highlight IterationUser guifg=#968748
highlight IterationClaude guifg=#3C8C8C
highlight IterationHighlight gui=underline
```
