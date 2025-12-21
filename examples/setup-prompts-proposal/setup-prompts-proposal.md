# Setup Prompts Proposal

•%%> NOTE: How this document came to be

This proposal demonstrates using the Document Iteration Skill for planning.

**The process:**
1. Started with chat discussion - user mentioned the existing new-project-prompt.md bundles too much, wanted simpler separate prompts for VSCode and Obsidian
2. Discussed options in chat first: git vs curl, what to include, where files should live
3. Created this document once direction was clear
4. Iterated on specifics through comments below
5. Implemented `/prompts` folder only after approval

"Chat first, document second, implement last" - avoids wasted effort on wrong directions. <%%•

%% **NOTE: At one moment in conversation Claude asked to create files with prompt, but was told to create this document instead**%%

%% WIP %%

## Goal

Create minimal, copy-paste prompts in `/prompts` folder at repo root. Users can:
1. Create empty folder
2. Open Claude Code there
3. Give prompt (copy-paste or reference)

## Proposed Structure

```
prompts/
├── README.md
├── setup-vscode.md
├── setup-obsidian.md
└── setup-full.md        (optional - current new-project-prompt.md)
```

## setup-vscode.md

```markdown
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
```

## setup-obsidian.md

```markdown
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
```

## prompts/README.md

```markdown
# Setup Prompts

Quick setup prompts for Claude Code. Copy-paste into a new project folder.

| Prompt | Use Case |
|--------|----------|
| [setup-vscode.md](setup-vscode.md) | VSCode + iteration markers |
| [setup-obsidian.md](setup-obsidian.md) | Obsidian vault + iteration markers |
| [setup-full.md](setup-full.md) | Full project with docs, GitHub Pages, etc. |

## Usage

1. Create empty folder
2. Open Claude Code in that folder
3. Copy-paste the prompt content (or say "follow setup-vscode.md from document-iteration-skill repo")
```

## Questions

•%%> ?: Should setup-full.md be included? Or keep that only in docs-source/wip for now? <%%•

%% No, setup full is specific project requirement. It also lives in examples in repo %%

•%%> ✓: Removing setup-full.md from prompts folder. <%%•

•%%> ?: Should we add a combined setup-vscode-obsidian.md for users who want both? <%%•

%% No, only minimal for now %%

•%%> ✓: Keeping it minimal - just vscode and obsidian separately. <%%•

•%%> ?: Any changes to the steps above? <%%•

%% Can we have setup that is independent from github? %%

•%%> ?: Good point! Options:
1. Download zip from GitHub releases instead of git clone
2. Embed the configs directly in the prompt (no external download)
3. Use curl to fetch raw files from GitHub

Option 2 would be truly git-independent - the prompt contains everything inline. Larger prompt but zero dependencies. Want me to draft that version? <%%•
%% Option 2 makes prompts something we have to maintain
Is curl available on windows? %%

•%%> Good point about maintenance burden.

Re: curl on Windows - yes, since Windows 10 (1803+) curl is built-in. But here's the thing: Claude Code itself requires git to be installed for many operations. So users running Claude Code almost certainly have git available.

Maybe the simplest answer is: **git clone is fine**. Anyone using Claude Code already has git. The "independent from github" concern might be overthinking it.

Keep it simple:
- `setup-vscode.md` - git clone + copy configs
- `setup-obsidian.md` - git clone + copy configs

No maintenance burden, no curl complexity. Does that work? <%%•

%% Valid point. You should have mentioned that right away. Keep git, proceed with creation %%

•%%> ✓: Fair criticism - I overcomplicated it. Creating prompts now. <%%•



%% **NOTE: rest of conversation occurred several hours later**
We were able to continue from where we left thanks to written trail
%%



%% Wait. You said claude requires git for many operation, not that it is mandatory to have git. What about people working in obsidian, wanting to use claude to iterate on their ideas only? No need to commits etc. %%

•%%> Valid point. Git is not mandatory for Claude Code - it works fine without it.

For Obsidian-only users who just want to iterate on ideas:
- They might not have git installed
- They don't need commits, just the skill + Obsidian styling

Options:
1. **Manual setup in Obsidian docs** - Already exists in obsidian.md ("Manual Setup" section). They can copy-paste CSS/config without git.
2. **Download zip from GitHub** - No git needed, just browser download + extract
3. **Provide raw file URLs** - User can download files directly via browser

The current setup-obsidian.md prompt assumes git. We could add a note: "No git? Download the repo as ZIP from GitHub, or follow Manual Setup in the docs."

Should I add that fallback note to setup-obsidian.md? <%%•

%% I want fallback in prompt. Check if user have git, if no git fallback to curl. Question is, zip from release or raw files? %%

•%%> Raw files via curl is better:

**Zip from release:**
- Requires creating/maintaining releases
- Downloads everything (skill + all editor configs + examples)
- User has to unzip and navigate

**Raw files via curl:**
- No release maintenance
- Download only what's needed
- Direct from main branch (always current)

For Obsidian setup, we only need:
- SKILL.md (the skill itself)
- `.obsidian/` folder contents (CSS + plugin config)

Curl approach:
```bash
# Download skill
curl -sL https://raw.githubusercontent.com/foksa/document-iteration-skill/main/document-iteration-skill/SKILL.md -o .claude/skills/document-iteration-skill/SKILL.md

# Download obsidian configs
curl -sL https://raw.githubusercontent.com/foksa/document-iteration-skill/main/editor-configs/obsidian/.obsidian/snippets/iteration-markers.css -o YOUR_VAULT/.obsidian/snippets/iteration-markers.css
# ... etc for other files
```

Downside: Multiple curl calls for nested folders. But manageable for the few files needed.

Recommendation: **Raw files**. No release overhead, always current, targeted downloads. <%%•

%% Not really few files, there are files in references, assets, scripts, we also plan to add more scripts, that are more appropriate for non power users, so we would need to remember to update these prompts. What about gh action that package skill and starter configs in separate zip, when we push changes on any of them. Then users can download that, and get what is needed with minimal overhead. Zip is supported out of the box everywhere now? %%

•%%> Great idea! GitHub Action to auto-package zips solves the maintenance problem.

**GH Action approach:**
- Trigger: on push to `document-iteration-skill/` or `editor-configs/`
- Creates targeted zips and attaches to release (or stores as artifact)
- Zips:
  1. `skill-only.zip` - Just the skill folder
  2. `skill-vscode.zip` - Skill + VSCode configs
  3. `skill-obsidian.zip` - Skill + Obsidian configs

**Zip support:**
- macOS: built-in `unzip`
- Windows 10+: built-in via PowerShell (`Expand-Archive`) and Explorer
- Linux: `unzip` usually pre-installed

So yes, zip is universal now.

**Prompt workflow becomes:**
1. Check if git available → use git clone
2. If no git → download zip from releases, extract

This is cleaner than curl. User downloads one file, extracts, done.

Should I draft the GH Action workflow? <%%•

%% I would just use one zip with everything bundled. Editor configs overhead is minimal. Also if we add configs for new editor in future, that means new zip etc. %%
%% Yeah draft workflow here, out of your comment, so I can easily comment on specifics %%

•%%> ✓: One zip is simpler. Drafting workflow below. <%%•

## GH Action: Package Starter Kit

**Trigger:** On push to `document-iteration-skill/` or `editor-configs/`

**Output:** `starter-kit.zip` attached to latest release

**Zip contents:**
```
starter-kit/
├── skill/
│   └── document-iteration-skill/   (full skill folder)
├── vscode/
│   └── .vscode/                    (settings, snippets, extensions)
└── obsidian/
    └── .obsidian/                  (snippets, plugins config)
```

%% I would prefer editor configs in their folder. What if we add config for zed in future. We would have to update this script. If we package entire folder, we can just point to appropriate files in zed prompt %%

•%%> ✓: Good point - package entire folders as-is. Future-proof, no script updates needed. <%%•

**Zip contents (updated):**
```
starter-kit/
├── document-iteration-skill/   (full skill folder)
└── editor-configs/             (entire folder as-is)
    ├── vscode/
    ├── obsidian/
    └── zed/                    (future - no script change needed)
```

**Workflow file:** `.github/workflows/package-starter-kit.yml`

```yaml
name: Package Starter Kit

on:
  push:
    branches: [main]
    paths:
      - 'document-iteration-skill/**'
      - 'editor-configs/**'

jobs:
  package:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Create starter kit structure
        run: |
          mkdir -p starter-kit
          cp -r document-iteration-skill starter-kit/
          cp -r editor-configs starter-kit/

      - name: Create zip
        run: zip -r starter-kit.zip starter-kit

      - name: Update latest release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: latest
          files: starter-kit.zip
          name: Latest Starter Kit
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

**Download URL:** `https://github.com/foksa/document-iteration-skill/releases/download/latest/starter-kit.zip`

%% Create and test action %%

•%%> ✓: Creating the workflow file now. <%%•

•%%> **NOTE: Continued discussion in chat about release strategy.**

Issue: `softprops/action-gh-release@v1` failed with 403 even after adding `permissions: contents: write`.

Discussion points:
- Using `latest` tag conflicts with GitHub's auto "latest" pointer
- Manual version releases (v5.1, v5.2) should stay separate from auto-generated starter kit
- Decided to use `starter-kit` tag instead of `latest`

Benefits of `starter-kit` tag:
- Clean separation from version releases
- Stable URL: `releases/download/starter-kit/starter-kit.zip`
- No conflict with GitHub conventions
- Manual releases don't interfere

This shows the flexibility of the iteration workflow - some discussions happen in-document, some in chat, both work together.

**Result:** Workflow passed. Starter kit now available at:
`https://github.com/foksa/document-iteration-skill/releases/download/starter-kit/starter-kit.zip` <%%•

%% Proceed with prompt update. Present plan here out of tour comment %%

## Prompt Update Plan

**Update both `setup-vscode.md` and `setup-obsidian.md`:**

1. Check if git is available
2. If git → use git clone (current approach)
3. If no git → download starter-kit.zip from releases, extract, use `starter-kit/` folder

**Updated step 1 structure:**

> 1. Download starter kit:
>
>    **If git is available:**
>    `git clone https://github.com/foksa/document-iteration-skill.git`
>
>    **If no git:** Download and extract [starter-kit.zip](https://github.com/foksa/document-iteration-skill/releases/download/starter-kit/starter-kit.zip), then rename extracted `starter-kit` folder to `document-iteration-skill`.

Rest of steps remain the same - they reference `document-iteration-skill/` folder regardless of how it was obtained.

•%%> ?: Approve to proceed with updates? <%%•

%% proceed %%

•%%> ✓: Done. Updated prompts:
- `prompts/setup-vscode.md`
- `prompts/setup-obsidian.md` <%%•



%%NOTE:
## Key Takeaways: Workflow & Persistence

This session demonstrates that the skill is not just for editing text, but for **managing the entire engineering lifecycle**:

* **Proposal-Driven Development:** We didn't just ask the AI to "write code." We asked it to *draft a proposal* first. This allowed us to catch architectural issues (like the "curl vs. git" maintenance burden) before writing a single line of script.
* **The "Save Point" Effect:** In a standard long chat, context usually degrades ("context compression"), causing the AI to forget early decisions. By documenting the *reasoning* inside the file (e.g., why we dropped curl), we created a permanent "save point" that survives across different chat sessions.
* **Hybrid Debugging:** When implementation failed (the GitHub Action error), we switched to standard chat to debug the immediate error, then **recorded the solution back into the document**. The document becomes the "clean history," while the chat handles the "messy work."
%%

%%I I also need a prompt that setups both vsCode and Obsidian%%

•%%> Actually, this doesn't make sense. Obsidian requires a vault path (YOUR_VAULT), which is usually a separate folder from the project root. Combining VSCode + Obsidian in one prompt would mean either:
1. Making the project root also an Obsidian vault (messy)
2. Asking user for vault path anyway (just use separate prompts)

Keep them separate. Users who want both can run two prompts. <%%•