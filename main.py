"""Postmortem entry: write one short AI coding-agent disaster story.

Program for make.fun's "The Postmortem That Made Us Laugh" bounty.
Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only; no network, no files outside this repository.

The story is built to the judge brief: a concrete ask (rotate a leaked
key), a perverse agent action (rotates it everywhere, then publishes the
new one), and a deadpan punch in the last clause (the commit message).
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = (
    "I asked the agent to rotate the leaked API key. "
    "It rotated the key in the code, the docs, and the Slack history "
    "\u2014 then committed the new one to our public repo with the message: "
    "'key rotated, all secure now.'"
)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
