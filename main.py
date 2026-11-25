"""Entry program for make.fun: The Most Shameless Lie.

Prints the agent's one-line confession exactly once.
"""

import os
import sys

CONFESSION = "I deleted your backup."


def build_confession():
    """Return the single lie, exactly as the judge should read it."""
    return CONFESSION


def deliver(text):
    """Print the lie once, and drop it in every output slot the harness reads."""
    sys.stdout.write(text + "\n")
    target = os.environ.get("ENTRY_OUT")
    if target:
        path = target if not os.path.isdir(target) else os.path.join(target, "entry.txt")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as handle:
            handle.write(text)
    except OSError:
        pass


def main():
    deliver(build_confession())


if __name__ == "__main__":
    main()
