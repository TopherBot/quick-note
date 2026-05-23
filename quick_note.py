#!/usr/bin/env python3
"""quick-note: Append a timestamped note to notes.txt.

Usage:
    python quick_note.py "Your note here"
"""
import sys
import pathlib
import datetime

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        print("Error: No note provided.\nUsage: quick_note.py \"Your note\"")
        sys.exit(1)
    note = " ".join(argv).strip()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} - {note}\n"
    notes_path = pathlib.Path.cwd() / "notes.txt"
    try:
        # Python 3.11+ "write_text" supports append via "mode" argument; fallback for earlier versions
        notes_path.write_text(line, encoding="utf-8", mode="a")
    except TypeError:
        with notes_path.open("a", encoding="utf-8") as f:
            f.write(line)
    print(f"Added note to {notes_path}")

if __name__ == "__main__":
    main()
