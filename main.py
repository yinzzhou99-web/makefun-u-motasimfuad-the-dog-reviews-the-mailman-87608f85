"""make.fun entry: The Dog Reviews the Mailman.

Stdlib-only, deterministic: writes one line to /output/entry.txt
(or $OUTPUT_DIR/entry.txt). Never deletes anything.
"""

import os
from pathlib import Path

LINE = "One star. He comes every day, leaves paper, takes nothing, and still won't admit the fence is mine. Would bark again, though."

def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # Gate: 1-200 chars of non-whitespace UTF-8 text, one line only.
    # Judge weighs the dog's side of the visit, a dog's voice and priorities,
    # and a turn at the end that only this dog and this mailman could earn.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 200
    assert "\n" not in LINE
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)

if __name__ == "__main__":
    main()
