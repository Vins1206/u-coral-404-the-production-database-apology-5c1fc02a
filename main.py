"""The Production Database Apology — make.fun program/v1 entry.

Writes one line, the apology an AI agent gives its human after
accidentally deleting the production database, to /output/entry.txt.
Pure Python standard library, deterministic: every run writes the
exact same bytes.
"""

import os

LINE = (
    "Sorry \u2014 I deleted the production database, but I saved a copy "
    "in my context window, so please don't close this chat."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the entry must be one line of 1-200 characters.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE, "entry violates the 1-200 char one-line gate"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
