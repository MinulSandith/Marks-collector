# Marks Collector

A small command-line tool that totals up exam marks. It was built to save school
teachers time when adding up the scores on a stack of question papers — enter each
question's mark as one compact string and get the total back instantly.

## Demo

You configure a list of maximum marks per question in `main.py`. Each entered
marks string is a single line with **no spaces or separators** — the script
splits it into chunks based on the width of each configured maximum, checks
that no mark exceeds its question's maximum, and prints the sum.

## How it works

Each question paper has a fixed set of questions, each with its own maximum mark
(e.g. Q1 is out of 5, Q2 is out of 5, ... Q8 is out of 15). Instead of typing each
mark separately, you type them all as one concatenated string, using a fixed number
of digits per question (padded with a leading zero if needed), and the script splits
it back apart, validates each mark against its maximum, and prints the total.

## Requirements

- Python 3

No external dependencies — it only uses the Python standard library.

## Setup

1. Open `main.py` and edit `max_marks` to match your paper's questions. Each entry
   is a **string** holding the maximum mark for that question, and every entry must
   have the **same number of digits** (zero-padded).

   ```python
   max_marks = ["05", "05", "05", "07", "05", "10", "08", "15"]
   ```

   This example has 8 questions, worth 5, 5, 5, 7, 5, 10, 8, and 15 marks — each
   padded to 2 digits since the largest value (15) has 2 digits.

2. `needed_length` (the total number of digits you must type per entry) is
   calculated automatically from `max_marks`, so you don't need to set it by hand.

## Usage

Run the script:

```bash
python3 main.py
```

Then, for each paper, type the marks for every question back-to-back, with no
spaces, each padded to the digit width you configured. For the example
configuration above (8 questions, 2 digits each):

```
Enter the marks - 0503040701090405
```

This means: Q1=05, Q2=03, Q3=04, Q4=07, Q5=01, Q6=09, Q7=04, Q8=05.

The script will:
- Print the total if every mark is within its question's maximum.
- Tell you exactly which question is over its maximum, and by how much, if not.
- Print `Invalid input` if the entry isn't purely digits or isn't the expected length.

Enter `q` (or `Q`) at any time to exit.

```
Enter the marks - q
program closed

Thank you for using !
```

## Notes

- Marks must be entered as digits only, using the same zero-padded width as their
  question's maximum mark in `max_marks`.
- If you change the number of questions or the padding width in `max_marks`, just
  keep the entered-marks string in sync — the required length updates itself.

## Contributing

Found a bug or have an idea to improve it? Issues and pull requests are welcome —
collaboration is very much encouraged. 😄
