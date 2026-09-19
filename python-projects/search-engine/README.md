# Smart Search Engine

A Tkinter GUI tool I built for fuzzy full-text search inside a single loaded
text file. It tokenizes the text, generates phonetic/spelling variations,
scores matches with TF-IDF plus fuzzy string matching, and highlights the
matched terms in context.

## Features

- Load any text file and search it interactively
- Typo-tolerant matching (handles misspellings, repeated letters, common substitutions)
- Relevance-ranked results with in-context highlighting
- Result navigation (previous/next)

## Requirements

```
pip install -r requirements.txt
```

## Run

```
python "Search engine.py"
```
