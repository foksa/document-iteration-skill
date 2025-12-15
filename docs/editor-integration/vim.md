---
title: "Vim"
layout: default
---

# Vim/Neovim

Visual highlighting of iteration markers in Vim and Neovim.

## Syntax Highlighting

Add to your config (`.vimrc` or `init.vim`):

```vim
" Highlight iteration markers
syntax match IterationComment /%%[^%]*%%/
highlight IterationComment guibg=#FFA500 guifg=#000000

syntax match IterationNote />>[^>]*>>/
highlight IterationNote guibg=#90EE90 guifg=#000000

syntax match IterationHighlight /==[^=]*==([^)]*)/
highlight IterationHighlight guibg=#FFFF00 guifg=#000000
```

## Related

- [Editor Integration Overview](editor-integration/index.md)
- [JetBrains Setup](editor-integration/jetbrains.md)