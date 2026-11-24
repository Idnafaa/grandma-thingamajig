#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes exactly one word to /output/entry.txt: the single word a
grandmother would text about AI.

Choice: "thingamajig". It is the word grandmothers reach for when a
gadget is too clever and too new to name — warm, baffled, instantly
recognisable as grandma-speak, and it points straight at a machine
she cannot quite describe. It is not the obvious "robot", not a
sentence, and it needs no caption to land.
"""

import os

# Candidates a grandma might text about AI, scored on the judge's
# own order: (1) reads as one grandma word, (2) warm/baffled voice,
# (3) funny on its own, (4) tied to a machine, (5) fresh, not obvious.
# Scores are 0-5 per criterion, in that order.
CANDIDATES = {
    # The classic grandma word for a gadget too clever to name.
    # Baffled, warm, machine-pointing, and nobody's obvious pick.
    "thingamajig": (5, 5, 4, 4, 4),
    # Also grandma-like, but it fits any object, not a machine.
    "whatchamacallit": (5, 5, 4, 2, 3),
    # The obvious pick: every entrant thinks of it first.
    "robot": (4, 2, 2, 5, 1),
    # A typo she might make, but it reads as a mistake, not a word.
    "robut": (3, 4, 3, 5, 2),
    # Clever machine, but sounds like a puzzle answer, not a text.
    "brainbox": (4, 2, 3, 4, 3),
    # Grandma for a gadget, but duller and less warm than the winner.
    "doohickey": (5, 4, 3, 3, 3),
}

WEIGHTS = (5, 4, 3, 2, 1)


def pick_word() -> str:
    best_word, best_score = None, -1.0
    for word, scores in CANDIDATES.items():
        total = sum(w * s for w, s in zip(WEIGHTS, scores))
        if total > best_score:
            best_word, best_score = word, total
    assert best_word is not None
    return best_word


def main() -> None:
    word = pick_word()
    assert word.isalpha() and 1 <= len(word) <= 30, word
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
