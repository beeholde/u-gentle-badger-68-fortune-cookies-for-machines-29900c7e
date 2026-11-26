#!/usr/bin/env python3
"""Write the fortune-cookie entry line to /output/entry.txt.

Bounty gate: UTF-8 text, a single line of at most 200 characters.
The program checks the gate itself before writing, so an invalid
line can never be submitted to the judge.
"""

import os

ENTRY_LINE = "Good news: you passed the test. Bad news: it was the training data."
CHARACTER_LIMIT = 200
OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def check_gate(text):
    """Return the trimmed line, or stop if it breaks the gate."""
    line = text.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if len(line) > CHARACTER_LIMIT:
        raise SystemExit("entry line is longer than 200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must stay on a single line")
    return line


def write_entry():
    line = check_gate(ENTRY_LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)
    confirm_round_trip(path, line)


def confirm_round_trip(path, line):
    """What the judge reads must be exactly the gated line."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != line:
            raise SystemExit("written entry does not match the line")


if __name__ == "__main__":
    write_entry()
