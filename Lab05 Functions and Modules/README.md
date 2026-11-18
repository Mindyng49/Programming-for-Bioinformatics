# SECB3203 Lab 5 - Functions and modules: sequence_utils.py and normalize.py

Student: MINDY NG YU FANG, A24CS0267

## Setup
    python -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt

## Run
    python -m pytest                 # all tests
    ruff check src                   # style check

## What is in this repository
- `src/sequence_utils.py` : clean_sequence, is_valid_dna, gc_content, reverse_complement, find_motif
- `src/normalize.py` : proportions, cpm (never change the caller's data)
- `tests/` : visible tests and my own tests (test_lab05_own.py)
- `AI_USE_LOG.md` : my AI prompt log (or nil return)

## Design decisions
<Two or three sentences: why proportions() raises ValueError when the total is zero, and which line of your code makes sure the input list is not changed.>
The proportions() function raises a ValueError when the total is zero because division by zero is not allowed.The list comprehension return [count / total for count in counts] creates a new list instead of modifying the original input list, ensuring that the original data remains unchanged