# quick-note

A minimal Python CLI that appends a timestamped note to `notes.txt`.

## Installation

Just run the script directly (no external dependencies):

```bash
python quick_note.py "Your note"
```

## Usage

```bash
python quick_note.py "Buy milk"
```

The command creates (or updates) a `notes.txt` file in the current directory with a line like:

```
2024-05-23 14:32:10 - Buy milk
```

## Why?

For developers who need a super‑lightweight way to jot down thoughts from the terminal without opening a full editor.

## License

MIT