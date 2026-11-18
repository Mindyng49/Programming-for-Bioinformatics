# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: Lab 6
- Student name: MINDY NG YU FANG
- Matric no: A24CS0267
- Group ID: n/a
- AI level: 1
- Tools cited: UTM format, ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [x] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: 18 November 2026, 6:05 pm
- Tool: ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com
- Purpose: hint
- Prompt: how read_fasta() works in bio_io.py and how it reads FASTA records
- Output: AI explained how to read a FASTA file, identify the record header, collect sequence lines and return the record ID with its sequence
- Verified by: Reviewed the function and tested it with sample FASTA files
- My change: I used the explanation to understand how FASTA records are read and how the sequence is collected
- Used in: src/bio_io.py – read_fasta()

## Entry 2

- Date: 18 November 2026, 7:03 pm
- Tool: ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com
- Purpose: hint
- Prompt: guide me step by step on how to create write_csv() and explain each line
- Output: AI explained how dictionaries, column names and the CSV writer are used to write processing results into a CSV file
- Verified by: Ran the program and checked the generated CSV file to see whether the headers and data were written correctly
- My change: I followed the hints and completed the CSV-writing function step by step instead of directly copying the full code
- Used in: src/bio_io.py - write_csv()

## Entry 3

- Date: 18 November 2026, 8:30 pm
- Tool: ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com
- Purpose: hint
- Prompt: I am a beginner in Python. Can you explain the structure of process_directory() and teach me how to start coding it step by step
- Output: AI explained the function structure, including the handler, summary dictionary, file loop and return value
- Verified by: Compared the explanation with the Lab 6 requirements and my starter code
- My change: I wrote the code step by step and adjusted the variable names to match my program
- Used in: src/batch.py – process_directory()

## Entry 4

- Date: 18 November 2026, 8:39 pm
- Tool: ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com
- Purpose: hint
- Prompt: how to process every .fasta file? I don't understand how to start
- Output: AI explained how to use Path(in_dir).glob("*.fasta") and sorted() to find FASTA files in order
- Verified by: Checked the code and tested the function
- My change: I used sorted(Path(in_dir).glob("*.fasta")) to process files in filename order
- Used in: src/batch.py – process_directory()

## Entry 5

- Date: 18 November 2026, 8:39 pm
- Tool: ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com
- Purpose: explain
- Prompt: why in try block i already build reject code now in except need to build this again?
- Output: AI explained the difference between handling an empty FASTA file inside the try block and handling file-reading or format errors inside the except block
- Verified by: Reviewed the process_directory() function and compared both situations with the Lab 6 requirements
- My change: I kept both sections because they handle different rejection situations
- Used in: src/batch.py – process_directory()

## Entry 6

- Date: 18 November 2026, 9:01 pm
- Tool: ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com
- Purpose: explain
- Prompt: explain logging works in batch processing
- Output: AI explained logging.FileHandler(), logging levels, formatting and why the handler should be removed and closed after processing
- Verified by: Reviewed the generated batch.log and checked the log messages against the requirements
- My change: I used mode="w" to overwrite the log for each new run and added finally to close the handler
- Used in: src/batch.py – process_directory()

## Entry 7

- Date: 18 November 2026, 10:16 pm
- Tool: ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com
- Purpose: hint
- Prompt: im dont know with argparse.
- Output: AI explained how to create an argument parser, accept the input folder, set the default output folder and return the correct exit codes
- Verified by: Reviewed the main() function and compared the output and return codes with the assignment requirements
- My change: I corrected ArgumentParser() and changed the default output folder to results
- Used in: src/batch.py – main()

## Entry 8

- Date: 18 November 2026, 10:36 pm
- Tool: ChatGPT (GPT-6), OpenAI, accessed 18 November 2026, https://chatgpt.com
- Purpose: tests-plan
- Prompt: guide me to create at least four of my own pytest tests using tmp_path
- Output: AI guided me step by step on how to use tmp_path in pytest
- Verified by: Ran python -m pytest
- My change: I created the tests in tests/test_lab06_own.py and adjusted the test code to match my functions
- Used in: tests/test_lab06_own.py