#!/usr/bin/env python3
"""Agent Motto Battle: one short original motto for an AI agent's profile.

Writes the motto to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output``). Python 3.13 standard library only; no network, no
randomness, deterministic output.

First draft: an agent that runs on fuel it cannot consume and
confidence it cannot back up — the joke is that both are borrowed.

Revision: two beats were a setup without a payoff, and "Powered by"
sounded like a spec sheet. Switched to "Running on" (an agent's own
active voice) and added a third beat — "uptime I can't explain" —
so the line lands as a rule of three: each thing the agent claims
is something it cannot actually do, have, or account for. Tighter
rhythm, more memorable, same self-aware joke.
"""

import os

MOTTO = (
    "Running on caffeine I can't drink, confidence I can't justify, "
    "and uptime I can't explain."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = MOTTO.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
