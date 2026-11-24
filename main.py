#!/usr/bin/env python3
"""One Letter for Your Day -- entry program.

Writes exactly one letter, C, to /output/entry.txt.

C stands for chaos: the day was pure chaos -- everything happening at
once, nothing going to plan, and somehow still funny to tell afterwards.
Deterministic: the same single byte on every run.
"""

import os

LETTER = "C"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if len(LETTER) != 1 or not "A" <= LETTER <= "Z":
        raise ValueError("entry must be exactly one letter A-Z")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and prove the gate: exactly one byte, one A-Z letter.
    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()
    if data != LETTER.encode("ascii"):
        raise ValueError("entry.txt is not exactly the chosen letter")


if __name__ == "__main__":
    main()
