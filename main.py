"""Pigeon Pitch, One Line — entry program.

Writes the winning one-line pitch to entry.txt in the output
directory. Pure Python standard library, fully deterministic:
no clock, no randomness, no network.
"""

import os
import sys

PITCH = (
    "I'm pre-seed \u2014 literally: 10,000 couriers who fly without GPS, "
    "run on crumbs, and know every rooftop in this city. Fund the flock, "
    "and your package will never sit in traffic again."
)

OUTPUT_NAME = "entry.txt"


def candidate_dirs():
    """Yield output directories in priority order."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        yield env_dir
    yield os.path.dirname(os.path.abspath(__file__))
    yield os.getcwd()


def main():
    """Write the pitch to the first writable candidate location.

    Each candidate directory is tried in order; an OSError on one
    location (missing directory, permission error, read-only file
    system) falls through to the next instead of aborting the run.
    Returns 0 on the first successful write, 1 if every location
    failed.
    """
    seen = set()
    for directory in candidate_dirs():
        if directory in seen:
            continue
        seen.add(directory)
        path = os.path.join(directory, OUTPUT_NAME)
        try:
            os.makedirs(directory, exist_ok=True)
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(PITCH)
        except OSError:
            continue
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
