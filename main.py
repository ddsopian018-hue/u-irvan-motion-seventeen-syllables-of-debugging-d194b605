"""Write one haiku about debugging to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python standard library only: no network, no external files,
no dependencies. The haiku is a constant in this file.
"""

import os

HAIKU = """One log line, then none
the server hums its small lie
I wrote the whole bug
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
