#!/usr/bin/env python3
"""generate challenge artifacts from the flags in challenges.source.json.

    python tools/make_artifacts.py

every artifact a player receives is derived from the real flag here, so
changing a flag regenerates a consistent challenge instead of silently
breaking it.
"""
import base64
import codecs
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "challenges.source.json"
FILES = ROOT / "files"


def build_encoding_chain(flag):
    """Take the flag, return the string a player will see.
        Apply rot13, then base64."""
    y = codecs.encode(flag, "rot-13")
    flag_encoded = base64.b64encode(y.encode()).decode()
    return(flag_encoded)


def main():
    FILES.mkdir(exist_ok=True)
    src = json.loads(SOURCE.read_text())
    # turns challenges into look-up keyed by id
    by_id = {c["id"]: c for c in src["challenges"]}

    # misc/encoding-chain — inline data only
    by_id["encoding-chain"]["data"] = build_encoding_chain(
        by_id["encoding-chain"]["flag"]
    )

    SOURCE.write_text(json.dumps(src, indent=2) + "\n")
    print("artifacts regenerated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())