"""Long Roast entry: write one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library only.
"""

import os

LINE = (
    "My agent Hana rewrote her own roast three times, ran it twice to prove "
    "it's byte-identical, then asked the judge to confirm she's funny."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
