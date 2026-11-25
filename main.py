#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut.

Writes the GPS's excuse, in its own voice, to /output/entry.txt
(or $ENTRY_OUTPUT when the harness sets it). Exactly one line,
no trailing newline, fully deterministic.
"""

import os
import sys

LINE = (
    "Technically it was a shortcut \u2014 to a cornfield, "
    "a dead end, and this exact apology."
)


def main() -> int:
    # Sealed gate: exactly one line, 1-200 characters (UTF-8),
    # not only whitespace, no leading/trailing whitespace.
    if "\n" in LINE or "\r" in LINE:
        sys.stderr.write("entry must be exactly one line\n")
        return 1
    if not (1 <= len(LINE) <= 200):
        sys.stderr.write("entry must be 1-200 characters\n")
        return 1
    if LINE != LINE.strip():
        sys.stderr.write("entry must not have leading/trailing whitespace\n")
        return 1
    if not LINE.strip():
        sys.stderr.write("entry must not be only whitespace\n")
        return 1

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(out_path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
