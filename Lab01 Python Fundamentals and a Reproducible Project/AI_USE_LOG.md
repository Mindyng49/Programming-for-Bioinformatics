# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: <e.g. Lab 1>
- Student name: <MINDY NG>
- Matric no: <A24CS0267>
- Group ID: <n/a>
- AI level: <1>
- Tools cited: <UTM format, e.g. OpenAI (2026). ChatGPT (GPT-5). Retrieved 12 October 2026 from https://chat.openai.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: <Date and time of the interaction>
- Tool: <Tool name, version, access date and URL (UTM citation format)>
- Purpose: <One of: explain, hint, review, debug, generate-code, generate-text, tests-plan, other>
- Prompt: <The exact prompt you typed (paste it)>
- Output: <What the AI gave back, in 1 to 3 lines (attach the full text if you used it)>
- Verified by: <How you checked it: ran pytest, read the docs, compared with data, asked lecturer>
- My change: <What you accepted, rejected or rewrote, and why>
- Used in: <File and function, or report section, where it ended up (or 'not used')>

<!-- Copy the whole 'Entry' block for each extra interaction: ## Entry 2, ## Entry 3 ... -->

## Entry 1

- Date: 24 October 2026 , 3:43am
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 25 October 2026 from https://chatgpt.com/
- Purpose: explain
- Prompt: Can you explain the steps I need to follow to set up my Lab 1 based on the given instruction 
- Output: ChatGPT explained the project setup process and guided me through the steps needed to prepare my Python environment.
- Verified by: Followed the setup instructions in the VS Code terminal.
- My change: Followed the instructions to set up the project on my computer.
- Used in: Project setup and environment configuration.

## Entry 2

- Date: 24 October 2026 , 4:05am
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 25 October 2026 from https://chatgpt.com/
- Purpose: debug
- Prompt: I run python -m venv .venv but it showed error Python could not be found.
- Output: ChatGPT explained that the python command was not recognised and guided me to use the py launcher to create the virtual
- Verified by:Ran py -m venv .venv in the terminal
- My change: Used the py command to create the virtual environment
- Used in: Windows setup

## Entry 3

- Date: 24 October 2026 , 4:08am
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 25 October 2026 from https://chatgpt.com/
- Purpose: explain
- Prompt: Can I use py? What is the diff between the py and the python?
- Output: ChatGPT explained that py is the Windows Python launcher, while python runs Python through the command available in the system PATH or active environment
- Verified by:Tried the commands in the VS Code terminal and checked which commands worked
- My change: Used the working command, py
- Used in: Python environment setup and terminal commands

## Entry 4

- Date: 25 October 2026 , 4:30pm
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 25 October 2026 from https://chatgpt.com/
- Purpose: debug
- Prompt: Help me debug my env_check.py code
- Output: ChatGPT explained the difference between import importlib and from importlib import metadata and helped me understand which import statement matched my code
- Verified by:Ran python src/env_check.py to check whether the environment report could run
- My change: Reviewed and adjusted the import statements 
- Used in: src/env_check.py, package_version()

## Entry 5

- Date: 25 October 2026 , 6:09pm
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 25 October 2026 from https://chatgpt.com/
- Purpose: debug
- Prompt: When I run ruff check src, I get errors about an unsorted import block (I001) and an unused import (F401) in env_check.py. How?
- Output: ChatGPT explained that I001 means the imports are not properly organised and F401 means an imported module is not used. It explained how to correct the import
- Verified by:Ran ruff check src again after editing the import statements
- My change: Removed the unused import importlib statement 
- Used in: src/env_check.py

## Entry 6

- Date: 25 October 2026 , 9:00pm
- Tool: OpenAI (2026). ChatGPT (GPT-6). Accessed 25 October 2026 from https://chatgpt.com/
- Purpose: tests-plan
- Prompt: WCan you guide me through Task 4 and give me hints 
- Output:  ChatGPT explained how to plan three tests: a boundary case for GC percentage, a zero-total case that should raise ValueError, and an invalid-input case using a negative count. It also explained pytest assertions and how to check expected errors
- Verified by:Reviewed the test cases and ran python -m pytest 
- My change:  Checked the expected results
- Used in: tests/test_lab01_own.py