# Marks Collector

A tiny command-line tool that adds up exam marks for a fixed set of questions.
It was built to save teachers the trouble of manually summing marks question
by question — you type in one continuous string of marks and it validates
each one against its maximum and prints the total.

## How it works

You configure a list of maximum marks per question in `main.py`. Each entered
marks string is a single line with **no spaces or separators** — the script
splits it into chunks based on the width of each configured maximum, checks
that no mark exceeds its question's maximum, and prints the sum.

Demo: https://github.com/MinulSandith/Marks-collector/assets/106053448/8d4d5dbb-6d45-4662-847f-1fab2a854c65

## Requirements

- Python 3 (no external dependencies)

## Configuration

Open `main.py` and edit these two lines at the top:

```python
max_marks=["05","05","05","07","05","10","08","15"]
needed_length=16
```

- `max_marks` — one entry per question, holding that question's maximum mark.
  **Every entry must have the same number of digits** (zero-pad if needed,
  e.g. `"05"` not `"5"`), since that width is what the script uses to split
  the input back into individual marks.
- `needed_length` — the total number of characters expected in the entered
  marks string, i.e. the sum of the digit-widths of every entry in
  `max_marks`. With the default 8 questions at 2 digits each, that's `16`.

Example: for 4 questions worth up to 2, 7, 10 and 100 marks, you'd need 3
digits per question to fit "100", so:

```python
max_marks=["002","007","010","100"]
needed_length=12
```

## Usage

1. Run the script:

   ```bash
   python3 main.py
   ```

2. At the prompt, type all marks concatenated together, in question order,
   using the fixed digit width from your configuration — no spaces, commas,
   or separators.

   With the default config (8 questions, max marks `05 05 05 07 05 10 08 15`,
   2 digits each), entering:

   ```
   0505050705100815
   ```

   scores the maximum on every question and prints `Total=  60`.

3. If a mark exceeds its question's maximum, the script reports which
   question and what the valid range is, and withholds the total until you
   re-enter a fully valid set of marks.

4. Type `q` at the prompt to quit.

## Input validation

The script rejects and re-prompts on:

- A string whose length doesn't match `needed_length`.
- A string containing anything other than digits (letters, spaces, symbols).
- Any individual mark greater than its question's configured maximum.

## Known limitations

- Configuration (`max_marks`, `needed_length`) is edited directly in the
  source file — there's no interactive setup or config file yet.
- All questions must share the same digit width, since that's how input is
  split into individual marks.

## Contributing

Found a bug or have an idea? Open an issue or send a pull request —
contributions are welcome.
