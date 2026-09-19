# File Extractor Tool

A small utility I wrote to extract ZIP and TAR archives (`.tar`, `.tar.gz`,
`.tgz`, `.tar.bz2`) into a chosen destination folder, with archive-type
detection and safety checks against path-traversal ("zip-slip") entries.

## Run

```
python index.py
```

You'll be prompted for the archive path and a destination folder.
