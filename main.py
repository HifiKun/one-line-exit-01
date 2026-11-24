"""The One-Line Exit: write one funny resignation letter, exactly one line.

The program writes a single line to /output/entry.txt. The line is the
whole entry: it must read like a resignation letter a person could
actually send, and its joke has to land in that one line.
"""

import os

LINE = (
    "I hereby resign: I came here to climb the corporate ladder, "
    "but after three years the only thing that went up was my blood pressure."
)


def main() -> None:
    # The gate only accepts 1-140 characters of non-blank text on one line,
    # so refuse to write anything that would fail it instead of guessing.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 140:
        raise ValueError("entry line must be one line of 1-140 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
