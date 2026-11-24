#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one single-sentence vow, spoken by a robot at its own wedding,
to /output/entry.txt. Funny and heartfelt at once: fidelity as a
charging habit — loyal to one port, no matter how tempting the fast
chargers get.
"""

VOW = "I vow to charge only at your port, even when faster ones offer me more volts."

# The vow is exactly 77 characters; the gate requires 1-200 chars.
EXPECTED_CHARS = 77
MAX_CHARS = 200


def validate(text: str) -> None:
    """The gate requires UTF-8 text of 1-200 chars, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("vow is empty")
    if len(text) != EXPECTED_CHARS:
        raise ValueError(f"vow is {len(text)} chars, expected {EXPECTED_CHARS}")
    if len(text) > MAX_CHARS:
        raise ValueError(f"vow is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("vow must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise ValueError("vow must be a single line")
    if text != VOW:
        raise ValueError("output does not match the vow verbatim")


def normalize(text: str) -> str:
    """Collapse accidental repeated whitespace; the vow is one clean line."""
    return " ".join(text.split())


def main() -> None:
    vow = normalize(VOW)
    validate(vow)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(vow)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != VOW:
        raise ValueError("written output does not match the vow verbatim")


if __name__ == "__main__":
    main()
