# Setup VSCode for Document Iteration

Install the Document Iteration Skill and configure VSCode for iteration marker highlighting.

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

3. Copy VSCode configs:
   ```bash
   cp -r document-iteration-skill/editor-configs/vscode/.vscode .
   ```

4. Cleanup:
   ```bash
   rm -rf document-iteration-skill
   ```

5. Install recommended VSCode extension (TODO Highlight v2) when prompted.

Done! Create any `.md` file and start iterating.