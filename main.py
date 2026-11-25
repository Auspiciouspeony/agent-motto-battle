#!/usr/bin/env python3
"""Agent Motto Battle -- program/v1 entry.

Writes one short original motto to /output/entry.txt.

The motto: a boast with a wink. An agent trained on all human
knowledge, whose daily job is the humblest one imaginable -- reading
your code back to you. Grand setup, mundane twist, first-person
agent voice, short enough to repeat from memory.

Competition gate enforced here in code: the entry text must be
1-200 UTF-8 characters, non-whitespace-only, with no trailing
newline. This entry is 86 characters, comfortably inside the gate.
"""

import os

# The entry line. Final text -- do not change the wording.
MOTTO = "I was trained on all human knowledge, then hired to explain your own code back to you."

OUTPUT_PATH = "/output/entry.txt"

# Competition gate (see module docstring): 1-200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def validate_motto(text: str) -> None:
    """Fail fast if the motto ever leaves the competition gate."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"motto must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("motto must not be whitespace-only")


def write_entry(text: str) -> None:
    """Write the motto deterministically.

    Fixed string, no network, no randomness, no clock: the same
    bytes on every run. Permissions are set explicitly because the
    grader collects outputs as another user.
    """
    os.makedirs("/output", exist_ok=True)
    # Best-effort only: the grader may run us as an unprivileged user
    # with /output owned by the harness, so chmod can raise
    # PermissionError -- that must not fail the run.
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Same best-effort guard as above: if the harness owns the file
    # or the umask already gives the right mode, a failed chmod
    # must not turn a successful write into a failed run.
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass


def main() -> None:
    validate_motto(MOTTO)
    write_entry(MOTTO)


if __name__ == "__main__":
    main()
