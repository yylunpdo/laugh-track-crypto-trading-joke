#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single one-line joke about crypto trading life to
/output/entry.txt. Pure standard library, fully deterministic:
the same line is written on every run.
"""

import os

JOKE = (
    "I bought the dip, the dip bought a shovel, "
    "and now I'm HODLing a hole the chart calls "
    "a long-term investment."
)


def main():
    # The joke must be one line, 1-200 characters, not only whitespace.
    line = JOKE.strip()
    assert "\n" not in line, "joke must be a single line"
    assert 1 <= len(line) <= 200, "joke must be 1-200 characters"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
