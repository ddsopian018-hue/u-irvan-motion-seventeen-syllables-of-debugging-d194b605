"""Seventeen syllables of debugging.

The haiku — "One log line, then none / the server hums its small lie /
I wrote the whole bug" — is a debugger's confession in 5-7-5: the
log goes silent, the server keeps humming as if nothing is wrong,
and the twist lands on the author, not the machine. Self-blame is
the honest punchline every developer recognises at 2 a.m. The
middle line carries the personification ("hums its small lie")
that makes the scene specific instead of generic. Syllable count
checks out at 5-7-5: "One log line, then none" (5), "the server
hums its small lie" (7), "I wrote the whole bug" (5).
"""

import os

HAIKU = (
    "One log line, then none\n"
    "the server hums its small lie\n"
    "I wrote the whole bug"
)


def main():
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly three lines"
    assert len(HAIKU) <= 200, "haiku must fit the 200-char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
