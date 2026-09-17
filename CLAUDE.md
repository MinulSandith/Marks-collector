# Marks-collector — repo overview (for future sessions)

Tiny single-file Python CLI (`main.py`, ~45 lines) that sums exam marks.
No dependencies, no tests, no build system. Only files: `main.py`,
`README.md`, this `CLAUDE.md`.

## How it works
- `max_marks`: list of zero-padded string maxima, one per question (e.g.
  `["05","05","05","07","05","10","08","15"]`). All entries must share the
  same digit width — that width is how input gets split back into marks.
- `needed_length`: total expected characters in the entered-marks string
  (sum of each `max_marks` entry's digit width). Must be kept in sync
  manually with `max_marks`.
- Main loop: prompts for one concatenated marks string (no separators),
  rejects wrong length or non-digit input, splits it into per-question
  chunks, checks each against its max, and prints the total only if every
  mark was valid.

## Bugs fixed 2026-09-17 (commit 4d2e9c1, branch claude/great-hamilton-c6voeb)
1. **Validity flag bug**: `validity` was reset to `1` on every valid mark
   in the loop, so an earlier invalid-mark warning got silently overridden
   if a later mark was valid — the (wrong) total printed anyway. Fixed by
   only ever setting `validity=0`, never resetting it back to `1` inside
   the loop.
2. **Crash on non-numeric input**: `int(mark)` raised an uncaught
   `ValueError` if the entered string wasn't all digits. Fixed with an
   `entered_marks.isdigit()` check before parsing.

## Known limitations (not yet addressed)
- Configuration is hardcoded in source; no config file or interactive setup.
- All questions must use the same digit width for their max mark.
- `needed_length` must be kept manually consistent with `max_marks`
  (could be computed automatically instead).

## Workflow notes
- Repo has no CI, no test suite — verify changes by running
  `python3 main.py` manually with piped stdin, e.g.:
  `printf '0505050705100815\nq\n' | python3 main.py`
- Default branch: `main`. Development branch used by Claude sessions:
  `claude/great-hamilton-c6voeb`.
