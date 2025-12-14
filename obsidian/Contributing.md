# Contributing

Thanks for your interest in improving the Document Iteration Skill!

## Ways to Contribute

### Report Issues

Found a bug or something confusing?

- [Report a bug](https://github.com/foksa/document-iteration-skill/issues/new?template=bug_report.md)
- [Ask a question](https://github.com/foksa/document-iteration-skill/issues/new?template=question.md)

### Suggest Features

Have an idea for improvement?

- [Request a feature](https://github.com/foksa/document-iteration-skill/issues/new?template=feature_request.md)

### Improve Documentation

These docs live in the `obsidian/` folder. To contribute:

1. Fork the repository
2. Edit files in `obsidian/`
3. Submit a pull request

The GitHub Action will automatically convert your Obsidian markdown to GitHub Pages format.

## Development

### Local Testing

Run the conversion script locally:

```bash
python3 scripts/convert-obsidian.py
```

This creates the `docs/` folder from your `obsidian/` files.

### Obsidian Syntax

You can use standard Obsidian features:

- `[[Wikilinks]]` - converted to standard links
- `![[Embeds]]` - converted to link references
- `![[images.png]]` - copied to assets folder

## Code of Conduct

Be kind. Be helpful. We're all here to make document collaboration better.

## See Also

- [[FAQ]] - Common questions
- [[Examples]] - See the syntax in action