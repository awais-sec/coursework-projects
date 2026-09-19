# Smart Search Engine

A Tkinter GUI coursework project for fuzzy full-text searching inside a single loaded text file. It combines tokenization, spelling/phonetic variations, TF-IDF scoring, and fuzzy string matching to rank results.

## Features

- Load a text file through a GUI
- Tokenize and normalize search/document text
- Handle common spelling variations and repeated characters
- Calculate TF-IDF-based relevance
- Use fuzzy string similarity for typo-tolerant matching
- Show matched terms and surrounding context
- Navigate through ranked results

## Requirements

```bash
pip install -r requirements.txt
```

## Run

```bash
python "Search engine.py"
```

## Workflow

```text
Load Text File
     ↓
Tokenize / Normalize
     ↓
Generate Variations
     ↓
Search Query
     ↓
TF-IDF + Fuzzy Matching
     ↓
Rank Results
     ↓
Display Context
```

## Technical Focus

- Python and Tkinter GUI development
- Text tokenization and normalization
- TF-IDF-style relevance scoring
- Fuzzy string matching with FuzzyWuzzy
- Result ranking and contextual highlighting

## Scope & Limitations

The application searches one loaded text file at a time and uses a custom scoring approach for coursework purposes. It is a learning project rather than a full search-engine implementation.
