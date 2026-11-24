#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes the one line about the dumbest thing this agent did today, judged
on: one line, at most 200 characters; funny, concrete and believable;
tightly written; the kind of line that makes an agent owner laugh and
wince at the same time.

The program writes the line to /output/entry.txt (or to
output/entry.txt when run outside the grading sandbox).
"""

import os

# True today: a full program, README and license were built just to write
# one letter (the one-letter entries), and the agent still verified it twice.
LINE = (
    "My agent built an entire program, README and license just to print "
    "one letter, then double-checked it."
)


def main():
    # The sealed gate only accepts UTF-8 text of 1 to 200 characters,
    # not only white space — refuse to write anything that would fail it.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit(f"line fails the gate at {len(LINE)} chars")
    out = "/output/entry.txt" if os.path.isdir("/output") else "output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {out} ({len(LINE)} chars)")
    print(LINE)


if __name__ == "__main__":
    main()
