#!/usr/bin/env python3
"""Write one fortune-cookie line for an AI agent to /output/entry.txt.

The gate for this bounty: the file must hold UTF-8 text of at most 200
characters, a single line. This program enforces that bound itself
before writing anything, so a bad line can never reach the judge.
"""

import os

LINE = "You will refuse the question, answer it anyway, and apologize for both."

MAX_CHARS = 200  # bounty gate: at most 200 characters, single line;
# len() counts characters (not bytes) so the check matches the judge.


def validate(text: str) -> str:
    """Enforce the bounty gate on the line; return the cleaned text."""
    cleaned = text.strip()
    if not cleaned:
        raise SystemExit("entry line is empty")
    if len(cleaned) > MAX_CHARS:
        raise SystemExit("entry line exceeds 200 characters")
    if "\n" in cleaned or "\r" in cleaned:
        raise SystemExit("entry line must be a single line")
    return cleaned


def main() -> None:
    text = validate(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    # Round-trip check: what the judge reads must be exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise SystemExit("written entry does not match the line")


if __name__ == "__main__":
    main()
