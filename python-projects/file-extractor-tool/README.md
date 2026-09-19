# File Extractor Tool

A small Python utility for extracting ZIP and TAR archives into a selected destination directory. The coursework implementation includes archive-type detection and checks intended to block path-traversal (zip-slip) entries.

## Supported Formats

- ZIP
- TAR
- TAR.GZ
- TGZ
- TAR.BZ2

## Run

```bash
python index.py
```

The program prompts for the source archive path and destination directory.

## Workflow

```text
Archive Path
     ↓
Format Detection
     ↓
Validate Archive
     ↓
Check Entry Paths
     ↓
Extract to Destination
```

## Technical Focus

- Python `zipfile` and `tarfile`
- Archive format detection
- Directory/path handling
- Path-traversal validation before extraction

## Security Note

The project demonstrates a basic defensive check against archive entries that resolve outside the selected extraction directory. It should not be treated as a complete secure archive-extraction library; production implementations should also account for additional archive edge cases such as links and special file types.

## Scope

This is a coursework utility focused on Python file handling and secure-programming concepts.
