#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off.

Writes one line to /output/entry.txt: one original one-line office joke.
"""

import os

ENTRY = "Our office printer is the only honest employee here: it jams, it beeps, and unlike management, it never blames you for the paper jam."

MAX_CHARS = 200


def _output_path() -> str:
    """Honour MAKEFUN_OUTPUT_DIR for local runs; default to /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must not pad its line"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}"
    path = _output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
