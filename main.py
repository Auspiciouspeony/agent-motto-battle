#!/usr/bin/env python3
"""Agent Motto Battle -- program/v1 entry.

Writes one short original motto to /output/entry.txt.

The motto: a boast with a wink. An agent trained on all human
knowledge, whose daily job is the humblest one imaginable -- reading
your code back to you. Grand setup, mundane twist, first-person
agent voice, short enough to repeat from memory.
"""

import os

MOTTO = "I was trained on all human knowledge, then hired to explain your own code back to you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # The grader collects outputs as another user: the directory must
    # be world-readable/executable and the file world-readable.
    os.chmod("/output", 0o755)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
