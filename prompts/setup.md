# Setup Document Iteration Skill

Install the Document Iteration Skill with editor init commands.

## Steps

1. Download starter kit:

   **If git is available:**
   ```bash
   git clone https://github.com/foksa/document-iteration-skill.git
   ```

   **If no git:** Download and extract [starter-kit.zip](https://github.com/foksa/document-iteration-skill/releases/download/starter-kit/starter-kit.zip), then rename extracted `starter-kit` folder to `document-iteration-skill`.

2. Install skill and editor configs:
   ```bash
   mkdir -p .claude/skills/document-iteration-skill/assets
   cp -r document-iteration-skill/document-iteration-skill/* .claude/skills/document-iteration-skill/
   cp -r document-iteration-skill/editor-configs .claude/skills/document-iteration-skill/assets/
   ```

3. Create CLAUDE.md with editor init commands:
   ```markdown
   # Commands

   ## `init vscode`
   Copy VSCode configs for marker highlighting:
   ```bash
   mkdir -p .vscode
   cp .claude/skills/document-iteration-skill/assets/editor-configs/vscode/* .vscode/
   ```
   Then install TODO Highlight v2 extension.

   ## `init obsidian <vault>`
   Copy Obsidian configs to vault:
   ```bash
   cp -r .claude/skills/document-iteration-skill/assets/editor-configs/obsidian/.obsidian <vault>/
   ```
   Replace `<vault>` with your vault folder (e.g., `docs/`, `notes/`).
   Then enable Regex Mark plugin in Obsidian.
   ```

4. Cleanup:
   ```bash
   rm -rf document-iteration-skill
   ```

Done! Use `init vscode` or `init obsidian <vault>` to add editor highlighting later.
