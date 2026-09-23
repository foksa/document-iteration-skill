# Cleanup

Cleanup turns an iterated document into a final one: the markers go, the content stays. Run it only when the user asks ("clean up", "finalize", "remove markers", "ready to publish"), because the comment history is the user's to discard.

## What changes

| Before | After |
|--------|-------|
| `%% comment %%` (any form, multi-line too) | removed |
| `•%%> response <%%•` and legacy `%%> response <%%` | removed |
| `==PostgreSQL(DB)==` | `PostgreSQL` |
| `==text==` | `text` |
| Blank lines left behind | collapsed to one |

Headings, lists, and all other content stay exactly as they are.

## With the script (preferred)

The script is deterministic and handles multi-line markers correctly.

```bash
python3 scripts/cleanup.py --check doc.md     # count markers, exit 1 if any
python3 scripts/cleanup.py doc.md             # clean in place
python3 scripts/cleanup.py -r docs/           # every .md under docs/
```

1. Run `--check` and report the counts to the user.
2. Name any `%% WIP %%` sections — they're still in progress, and cleanup removes the WIP flag with everything else.
3. Ask for confirmation and wait for a yes.
4. Run the cleanup, then read the file to confirm the formatting is intact (tables, lists, and headings that had inline markers are the places to look).

`--check` also works as a CI or pre-commit guard, since it exits with 1 when markers remain.

## Partial cleanup: `%%!CLEANUP!%%`

The marker splits the file. Everything from the top through the marker line gets cleaned; everything below it stays as is, markers included. The script cleans whole files, so do this by hand:

1. Scan the zone above the marker, count markers, and name any WIP sections.
2. Confirm with the user.
3. Remove the markers in that zone, following the table above, and remove the `%%!CLEANUP!%%` line itself.

Before:

```markdown
# Finalized Section

Uses ==SQLite(DB)==.
%%(DB) Good choice %%
•%%> Thanks. <%%•

%%!CLEANUP!%%

# Draft Section %% WIP %%

==Still working(TODO)== on this.
%%(TODO) Refine %%
```

After:

```markdown
# Finalized Section

Uses SQLite.

# Draft Section %% WIP %%

==Still working(TODO)== on this.
%%(TODO) Refine %%
```

## Manual fallback

When Python isn't available, apply the table above by editing the file directly. Afterwards, search for `%%`, `•`, and `==` to confirm none remain.
