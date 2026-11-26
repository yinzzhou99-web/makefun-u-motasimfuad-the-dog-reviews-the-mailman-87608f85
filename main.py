"""One-star review, filed by the dog on duty.

The whole program does a single small job: it writes the dog's verdict
about the mailman to a file called entry.txt inside the output folder.
Nothing is fetched, nothing is random, and nothing outside the standard
library is involved, so running it twice gives the same bytes twice.
"""

import os


def assemble_review():
    """Stitch the review together from its spoken clauses.

    Keeping each clause on its own line makes the wording easy to check
    by eye: the first clause gives the rating, the middle ones list the
    daily grievances, and the last one grudgingly admits he'd do it all
    over again.
    """
    clauses = [
        "One star.",
        "He comes every day,",
        "leaves paper,",
        "takes nothing,",
        "and still won't admit the fence is mine.",
        "Would bark again, though.",
    ]
    return " ".join(clauses)


def resolve_destination():
    """Work out where entry.txt belongs, creating the folder if needed.

    The caller picks the folder through OUTPUT_DIR; when that variable
    is absent we fall back to /output. We only ever create the folder
    itself -- anything already living inside it is left exactly as is.
    """
    folder = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def persist_review(path, text):
    """Write the review exactly as given -- no trailing newline added --
    and then pin the file's permissions to 0644 so graders can read it."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


def main():
    review = assemble_review()
    target = resolve_destination()
    persist_review(target, review)


if __name__ == "__main__":
    main()
