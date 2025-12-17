# Project Setup Prompt

Set up a new software project with the following structure and configuration:

## Project Structure

Create the following directory structure:

```
project-name/
├── .claude/
│   └── skills/
│       └── document-iteration-skill/
│           ├── SKILL.md
│           ├── scripts/
│           └── references/
├── .claude.md
├── .gitignore
├── .vscode/
│   ├── settings.json
│   ├── extensions.json
│   └── markdown.code-snippets
├── .github/
│   └── workflows/
│       └── pages.yml
├── docs/
│   ├── .obsidian/
│   │   ├── snippets/
│   │   │   └── iteration-markers.css
│   │   └── plugins/
│   │       └── regex-mark/
│   └── index.md
├── pages/
├── work-docs/
│   ├── .obsidian/
│   │   ├── snippets/
│   │   │   └── iteration-markers.css
│   │   └── plugins/
│   │       └── regex-mark/
│   └── index.md
└── README.md
```

## Step-by-Step Setup

### 1. Initialize Git Repository
```bash
git init
```

### 2. Install Document Iteration Skill
```bash
git clone https://github.com/foksa/document-iteration-skill.git
mkdir -p .claude/skills
cp -r document-iteration-skill/document-iteration-skill .claude/skills/
rm -rf document-iteration-skill
```

### 3. Create .gitignore
```gitignore
# Obsidian
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/plugins/
.obsidian/cache/

# OS
.DS_Store
Thumbs.db

# Editors
*.swp
*.swo
.idea/

# Dependencies (adjust based on project type)
node_modules/
__pycache__/
*.pyc
.venv/
```

### 4. Setup VS Code
Copy from `editor-configs/vscode/` in the document-iteration-skill repo:
- `.vscode/settings.json` → project `.vscode/`
- `.vscode/extensions.json` → project `.vscode/`
- `.vscode/markdown.code-snippets` → project `.vscode/`

Add to settings.json:
```json
{
  "files.exclude": {
    "pages": true
  }
}
```

Install the recommended TODO Highlight v2 extension when prompted.

### 5. Setup Obsidian Vaults
Copy from `editor-configs/obsidian/` in the document-iteration-skill repo:
- `.obsidian/` folder → `docs/.obsidian/`
- `.obsidian/` folder → `work-docs/.obsidian/`

After copying, enable the Regex Mark plugin in Settings → Community plugins and check for updates.

### 6. Create .claude.md
```markdown
# Project Rules

## 1. NEVER commit or push unless user EXPLICITLY says to

- Wait for explicit words like: "commit", "push", "commit and push"
- "cleanup" or "done" does NOT mean commit
- Even after completing all tasks, DO NOT commit unless asked
- **Violation of this rule is a critical failure**

## Documentation Workflow

- Use document-iteration-skill for all docs in `docs/` and `work-docs/`
- Never edit `pages/` directly - it's generated from `docs/`
- Run build script after finalizing documentation changes

## Code Structure

- Project type and folder structure will evolve based on needs
- No prescribed `src/` folder - create implementation folders as needed (e.g., `cli/`, `app/`, `web/`)

## Commits

- Iteration markup in docs/ and work-docs/ is intentional - commit it
- pages/ should only contain clean converted markdown
```

### 7. Create .github/workflows/pages.yml
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
    paths:
      - 'pages/**'

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: 'pages'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 8. Create Initial Documentation Files

**docs/index.md:**
```markdown
# Project Documentation

Welcome to the project documentation.

## Getting Started

[Add getting started content here]

## Topics

- [[topic-1|Topic 1]]
- [[topic-2|Topic 2]]
```

**work-docs/index.md:**
```markdown
# Work Documents

%% WIP %%

This vault contains implementation discussions and planning documents.

## Active Tasks

- [[tasks/current|Current Tasks]]

## Architecture

- [[architecture/overview|Architecture Overview]]
```

### 9. Create README.md
```markdown
# Project Name

Brief project description.

## Documentation

- **Published docs**: [GitHub Pages URL]
- **Source docs**: `docs/` (Obsidian vault)
- **Work docs**: `work-docs/` (implementation discussions)

## Development

[Add development instructions based on project type]
```

### 10. Create work-docs/build-docs-proposal.md

Create a proposal document in `work-docs/` with build script options. This will be finalized once the project stack is chosen.

The proposal should include:
- Bash version of `scripts/build-docs.sh`
- Node.js version of `scripts/build-docs.js`
- Dependencies section (obsidian-export, Python/Node cleanup scripts)
- Instructions for choosing based on project stack

## After Setup

1. Enable GitHub Pages in repo settings (Source: GitHub Actions)
2. Open `docs/` and `work-docs/` in Obsidian
3. Start iterating on documentation using the Document Iteration Skill