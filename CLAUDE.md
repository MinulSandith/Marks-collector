# Marks-collector — repo overview

Tiny single-file Python 3 CLI (`main.py`, no dependencies). Teachers type all of a
student's question marks as one concatenated, zero-padded digit string; the script
splits it per-question using `max_marks`, validates each mark against its max, and
prints the total. Type `q`/`Q` to quit.

## Layout
- `main.py` — the whole program (~40 lines).
- `README.md` — setup/usage docs.
- No tests, no CI/CD workflows (`.github/workflows` doesn't exist), no packaging.

## Known history
- Fixed a crash: non-numeric input of the correct length raised an unhandled
  `ValueError` from `int(mark)`. Now validated with `str.isdigit()` before parsing.
- `needed_length` used to be hardcoded (16) separately from `max_marks`, which could
  silently desync if `max_marks` changed. Now computed as
  `sum(len(str(m)) for m in max_marks)`.
- Loop variable was named `quit`, shadowing the Python builtin; renamed to `running`.
- Quit check is now case-insensitive (`q` or `Q`).

## Conventions
- Keep `max_marks` entries as zero-padded strings of equal width per your use case.
- This is a beginner/utility script — keep changes minimal and readable rather than
  over-engineering (no need for argparse, classes, etc. unless asked).
