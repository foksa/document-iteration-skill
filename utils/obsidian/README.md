# Obsidian CSS Snippet

CSS snippet for styling Document Iteration Skill markers in Obsidian.

## Installation

1. Copy `iteration-markers.css` to your vault's snippets folder:
   ```
   your-vault/.obsidian/snippets/iteration-markers.css
   ```

2. In Obsidian, go to **Settings** → **Appearance** → **CSS Snippets**

3. Click the refresh button to detect the new snippet

4. Toggle **iteration-markers** to enable it

## What it styles

| Marker | Color | Notes |
|--------|-------|-------|
| `%% comment %%` | Orange | Works out of the box |
| `%%> response <%%` | Orange | Works out of the box (same styling) |
| `==highlight==` | Yellow | Works out of the box |

## Syntax Overview

The skill uses `%% %%` comment syntax for everything:

- **User comments:** `%% your feedback %%`
- **Claude responses:** `%%> response <%%`
- **Claude notes:** `%%> NOTE: info <%%`

Both user comments and Claude responses get the same orange comment styling in Obsidian - the `>` prefix visually distinguishes Claude's output within the document.

## Customization

Edit the CSS file to change colors:

```css
/* Comments (both user and Claude) - change orange to your preferred color */
.cm-comment {
  background-color: rgba(255, 165, 0, 0.25);
}

/* Highlights */
mark {
  background-color: rgba(255, 255, 0, 0.4);
}
```

## Optional: Distinct Response Styling

If you want `%%> responses <%%` to look different from `%% user comments %%`, you'll need a plugin that can match regex patterns and add CSS classes.

### Using Style Settings plugin

1. Install "Style Settings" from Community Plugins
2. Add a regex rule to match `%%>.*<%%` patterns
3. Apply the `.claude-response` class from the CSS

### Using a custom plugin

A simple plugin could scan for `%%>` markers and wrap them in `<span class="claude-response">`.

The CSS already includes styling for `.claude-response`:

```css
.claude-response {
  background-color: rgba(0, 128, 128, 0.15);
  border-left: 3px solid rgba(0, 128, 128, 0.5);
  padding: 4px 8px;
  border-radius: 0 4px 4px 0;
}
```

This gives Claude responses a teal tint with a left border, distinguishing them from orange user comments.

## Color reference

- Orange (comments): `rgba(255, 165, 0, 0.25)`
- Teal (Claude responses): `rgba(0, 128, 128, 0.15)`
- Yellow (highlights): `rgba(255, 255, 0, 0.4)`