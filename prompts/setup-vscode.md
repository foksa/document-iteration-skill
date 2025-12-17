# Setup VSCode for Document Iteration

Install the Document Iteration Skill and configure VSCode for iteration marker highlighting.

## Steps

1. Clone and install skill:
   ```bash
   git clone https://github.com/foksa/document-iteration-skill.git
   mkdir -p .claude/skills
   cp -r document-iteration-skill/document-iteration-skill .claude/skills/
   ```

2. Copy VSCode configs:
   ```bash
   mkdir -p .vscode
   cp document-iteration-skill/editor-configs/vscode/* .vscode/
   ```

3. Cleanup:
   ```bash
   rm -rf document-iteration-skill
   ```

4. Install recommended VSCode extension (TODO Highlight v2) when prompted.

Done! Create any `.md` file and start iterating.