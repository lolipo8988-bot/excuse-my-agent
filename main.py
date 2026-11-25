#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the entry line for 'The Excuse My Agent Gave Me' to /output/entry.txt."""
import os

ENTRY = (
    "Sorry I missed the deadline \u2014 my context window quietly dropped it "
    "to make room for 40,000 tokens of me reasoning about how dependable I am."
)


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
