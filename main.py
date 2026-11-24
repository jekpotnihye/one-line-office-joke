"""One-line office joke.

This program writes a single original joke about office life to
/output/entry.txt, exactly one line, so the competition's judge can
read it as submitted. The joke is a fixed string: the same text on
every run, with no randomness, no network use, and no extra output.

The joke itself is a setup with a payoff. The setup is a familiar
video-call mishap, talking while muted. The payoff flips it: instead
of the mistake costing anything, it earns praise for the one thing
the speaker did not do. Keeping it to one sentence keeps the whole
joke readable at a glance.
"""

import os

JOKE = (
    "I spent the whole meeting on mute, pitching my best ideas to no one, "
    "and my manager praised my listening skills."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the joke to the output file, with no trailing newline."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
