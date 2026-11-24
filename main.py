"""make.fun entry: One Letter: Coffee or Tea.

Writes the single-letter entry to /output/entry.txt.
Stdlib only.

Brief: exactly one letter, A for coffee or B for tea, nothing else.
A is coffee: the fuel every debugging session actually runs on.
"""

import os
import sys

ENTRY = "A"


def validate(text):
    """Check the entry against the competition gate before writing."""
    if text not in ("A", "B"):
        sys.exit("entry must be A (coffee) or B (tea)")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
