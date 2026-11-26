#!/usr/bin/env python3
"""The Moon Gets One Star — a one-star review of the Moon.

Writes a single 112-character review to /output/entry.txt
(override with ENTRY_OUTPUT for local runs).
"""
import os

ENTRY = "★☆☆☆☆ The Moon followed me home every night for 30 years. Ducked behind a hill to lose it. It was already there."

# The sealed gate only accepts 1–120 characters; refuse to write anything
# outside it rather than submitting an entry that can never be judged.
MAX_CHARS = 120


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, gate allows 1–{MAX_CHARS}")
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {out}")


if __name__ == "__main__":
    main()
