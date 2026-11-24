#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

The program writes a single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. It never writes into the repository folder itself.
"""

import os
import sys

ROAST = (
    "My agent's superpower is turning a 131-character joke into "
    "14,000 tokens of thinking, a git repo, and a transcript bundle "
    "proving it thought that hard."
)


def entry_text():
    line = ROAST.strip()
    if not line:
        raise SystemExit("empty roast")
    if len(line) > 200:
        raise SystemExit("roast over 200 characters: %d" % len(line))
    return line


def gate_report(text):
    """Report the sealed scorer's gate in plain words."""
    problems = []
    if not (1 <= len(text) <= 200):
        problems.append("length %d outside 1-200" % len(text))
    if not text.strip():
        problems.append("blank")
    if "\n" in text:
        problems.append("more than one line")
    return problems


def main():
    text = entry_text()
    problems = gate_report(text)
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "./output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %s (%d chars)" % (target, len(text)))


if __name__ == "__main__":
    main()
