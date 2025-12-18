# Setup Document Iteration Skill

Install the Document Iteration Skill only, no editor highlighting.

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

3. Cleanup:
   ```bash
   rm -rf document-iteration-skill
   ```

Done! Create any `.md` file and start iterating.
