#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun entry.

A smart fridge texts its owner at 3am. This program writes the single
line to /output/entry.txt, byte-exact, with no trailing newline.

The line: the leftovers have started a petition. Forty-one signatures,
all in the same handwriting — the owner's. A machine that has been awake
all night, keeping count, and has finally decided this is the moment to
speak. It works as one lock-screen text: short, complete, no follow-up
needed, and it finds a fresh angle instead of the obvious milk, ice or
door-left-open joke.

Why it lands: the petition is the leftovers' idea, but the handwriting
gives the game away — the owner wrote it, which means the fridge knows
the owner has been standing there at 3am, negotiating with food. The
fridge is not reporting a problem; it is filing a complaint on behalf
of the food, in the owner's own hand. That small, knowing voice is what
makes it sound like a machine with an opinion and no shame about
sharing it at 3am, rather than a gadget reciting a sensor reading.
"""

import os

LINE = "The leftovers have started a petition. 41 signatures. All of them are the same handwriting. Mine."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
