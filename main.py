"""One-Line Office Jokes — a make.fun entry.

Writes a single first-person office joke to /output/entry.txt.
"""

import os

ENTRY_TEXT = "I hit reply-all to 214 people on Monday asking to be removed from this thread, and now 87 of them have replied-all to agree with me."
# Form: first-person confession, one character (me) in one scene (the thread),
# three specifics (214, Monday, 87), one gag, turn in the final clause.


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    # The grader reads the joke from /output/entry.txt.
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
