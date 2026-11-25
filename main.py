#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun bounty entry.

Writes the chosen fortune cookie line to /output/entry.txt (UTF-8, one line,
93 characters, no trailing newline).

The line was selected by internal pairwise judging against the judge brief in
RULES.txt (see variants.md in the build folder): a classic fortune opening
("You will inherit a great fortune") with the turn in the final clause — the
fortune is inherited from the trader's own yesterday, before the 50x long
took it. Rueful and warm, never cruel; specific number (50x); 15 words.

Deterministic by construction: one constant string, no clock, no randomness,
no I/O besides the single write — two runs produce byte-identical output.
No eval/Function/vm/dynamic import anywhere; no environment secrets.
"""

import os

# The fortune cookie line (15 words, 93 chars, 95 bytes UTF-8).
FORTUNE = "You will inherit a great fortune \u2014 from yourself, yesterday, before you opened that 50x long."


def main() -> None:
    # Gate guard (RULES.txt): 1-160 characters, at most 20 words, one line.
    assert 1 <= len(FORTUNE) <= 160, "fortune must be 1-160 characters"
    assert len(FORTUNE.split()) <= 20, "fortune must be at most 20 words"
    assert "\n" not in FORTUNE, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
