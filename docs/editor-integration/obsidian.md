---
---

# Obsidian

Visual highlighting of iteration markers in Obsidian.

## Automated Setup

Use the [setup-obsidian.md](https://github.com/foksa/document-iteration-skill/blob/main/prompts/setup-obsidian.md) prompt with Claude Code to install the skill and configure Obsidian automatically.

## Syntax

The skill uses `%% %%` comment syntax for everything:

* **User comments:** `%% your feedback %%`
* **Claude responses:** `•%%> response <%%•`
* **Claude notes:** `•%%> NOTE: info <%%•`

Both get the same orange comment styling - no plugins required!

## Custom CSS Snippet

Create `.obsidian/snippets/iteration-markers.css`:

````css
/* Highlight %% comments %% and •%%> responses <%%• */
.cm-comment {
  background-color: rgba(255, 165, 0, 0.3);
  padding: 2px 4px;
  border-radius: 3px;
}

/* Highlight ==text(TOKEN)== */
mark {
  background-color: rgba(255, 255, 0, 0.4);
  padding: 1px 2px;
}

/* Dark mode adjustments */
.theme-dark .cm-comment {
  background-color: rgba(255, 165, 0, 0.2);
}
````

Enable in Settings → Appearance → CSS Snippets.

## Advanced: Distinct Response Styling

To make `•%%> responses <%%•` visually distinct from `%% user comments %%`, use the Regex Mark plugin.

### Quick Setup

Copy the pre-configured `.obsidian` folder from `editor-configs/obsidian/` to your vault. This includes:

* Regex Mark plugin with patterns pre-configured
* CSS snippet for marker styling

After copying, enable the plugin in Settings → Community plugins, and check for plugin updates.

### Manual Setup

**Step 1: Install the plugin**

1. Open Obsidian Settings → Community plugins
1. Click "Browse" and search for "Regex Mark"
1. Install and enable it

**Step 2: Add regex patterns**

1. Go to Settings → Regex Mark
1. Add three patterns (click "Add new regex" for each):
   * **Pattern:** `%%` → **CSS class:** `user-response`
   * **Pattern:** `•%%>` → **CSS class:** `claude-response-start`
   * **Pattern:** `<%%•` → **CSS class:** `claude-response-end`
1. Save

**Step 3: Add CSS styling**

Add to your `.obsidian/snippets/iteration-markers.css`:

````css
.user-response {
  color: rgb(107, 95, 30);
  padding: 0px 4px;
}

.claude-response-start,
.claude-response-end {
  color: rgb(28, 79, 79);
  padding: 0px 4px;
}
````

Make sure the snippet is enabled in Settings → Appearance → CSS Snippets.

### Limitations

* **Token styling**: Making `(TOKEN)` in `==text(TOKEN)==` a different color isn't possible - Obsidian processes highlights before plugins can act. A custom plugin could solve this (see [plugin proposal](../../wip/obsidian-plugin-proposal.md)).

## Linter Plugin

Install "Linter" plugin. Add custom rule to flag markers:

````yaml
rules:
  custom-regex:
    - pattern: '%%[^%]*%%'
      message: 'Iteration marker found'
      severity: warning
````

## Related

* [Editor Integration Overview](index.md)
* [VS Code Setup](vscode.md)
