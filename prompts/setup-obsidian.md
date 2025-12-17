# Setup Obsidian Vault for Document Iteration

Install the Document Iteration Skill and configure an Obsidian vault for iteration marker styling.

## Steps

1. Clone and install skill:
   ```bash
   git clone https://github.com/foksa/document-iteration-skill.git
   mkdir -p .claude/skills
   cp -r document-iteration-skill/document-iteration-skill .claude/skills/
   ```

2. Copy Obsidian configs to your vault:
   ```bash
   cp -r document-iteration-skill/editor-configs/obsidian/.obsidian YOUR_VAULT/
   ```

   Replace `YOUR_VAULT` with your vault folder (e.g., `docs/`, `notes/`, or `.` for current folder).

3. Cleanup:
   ```bash
   rm -rf document-iteration-skill
   ```

4. Open vault in Obsidian, go to Settings → Community plugins → Enable "Regex Mark" plugin.

Done! Create any `.md` file and start iterating.