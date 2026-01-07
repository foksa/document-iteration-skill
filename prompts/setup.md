# Setup Document Iteration Skill

Install the Document Iteration Skill with slash commands.

## Steps

1. Download starter kit:

   **If git is available:**
   ```bash
   git clone https://github.com/foksa/document-iteration-skill.git
   ```

   **If no git:** Download and extract [starter-kit.zip](https://github.com/foksa/document-iteration-skill/releases/download/starter-kit/starter-kit.zip), then rename extracted `starter-kit` folder to `document-iteration-skill`.

2. Install skill, commands, and editor configs:
   ```bash
   mkdir -p .claude/skills/document-iteration-skill/assets
   mkdir -p .claude/commands
   cp -r document-iteration-skill/document-iteration-skill/* .claude/skills/document-iteration-skill/
   cp -r document-iteration-skill/commands/* .claude/commands/
   cp -r document-iteration-skill/editor-configs .claude/skills/document-iteration-skill/assets/
   ```

3. Cleanup:
   ```bash
   rm -rf document-iteration-skill
   ```

Done!

## Available Commands

After setup, these slash commands are available:

| Command | Description |
|---------|-------------|
| `/iterate <file>` | Process iteration markers in a document |
| `/cleanup <file>` | Remove iteration markers from a document |
| `/init-vscode` | Setup VSCode highlighting |
| `/init-obsidian <vault>` | Setup Obsidian highlighting |
