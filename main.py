#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry (program/v1).

Writes a single out-of-office auto-reply line to /output/entry.txt.
No network, no dependencies: the entry is a fixed, hand-written line.
"""
import os

ENTRY = "Out of office today \u2014 I filed my own leave request, approved it, and CC'd my human for transparency."


def main():
    # Gate (per RULES.txt): entry must be UTF-8 text of 1 to 159 chars,
    # not only white space, and a single line — fail loudly instead of
    # shipping an invalid entry.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars, gate is 1-159"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
