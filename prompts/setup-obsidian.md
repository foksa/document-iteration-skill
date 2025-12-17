# Setup Obsidian Vault for Document Iteration

Install the Document Iteration Skill and configure an Obsidian vault for iteration marker styling.

## Steps

1. Download starter kit:

   **If git is available:**
   ```bash
   git clone https://github.com/foksa/document-iteration-skill.git
   ```

   **If no git:** Download and extract [starter-kit.zip](https://github.com/foksa/document-iteration-skill/releases/download/starter-kit/starter-kit.zip), then rename extracted `starter-kit` folder to `document-iteration-skill`.

2. Install skill:
   ```bash
   mkdir -p .claude/skills
   cp -r document-iteration-skill/document-iteration-skill .claude/skills/
   ```

3. Copy Obsidian configs to your vault:
   ```bash
   cp -r document-iteration-skill/editor-configs/obsidian/.obsidian YOUR_VAULT/
   ```

   Replace `YOUR_VAULT` with your vault folder (e.g., `docs/`, `notes/`, or `.` for current folder).

4. Cleanup:
   ```bash
   rm -rf document-iteration-skill
   ```

5. Open vault in Obsidian, go to Settings → Community plugins → Enable "Regex Mark" plugin.

Done! Create any `.md` file and start iterating.