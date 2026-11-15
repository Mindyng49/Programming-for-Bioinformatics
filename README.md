# SECB3203 Lab 1 - Python fundamentals and a reproducible project

Student: <MINDY NG, A24CS0267>

## Setup
Windows PowerShell
## 1. Create the virtual environment
py -m venv .venv
## 2. Activate the environment.
.\.venv\Scripts\Activate.ps1
## 3. Install the required packages
py -m pip install -r requiremenets.txt
## 4.Record the installed package versions
py -m pip freeze > requirements-frozen.txt

## Run
## Run all tests
python -m pytest
## Check Python code style
ruff check src
## Generate enviroment report
python src/env_check.py > results/environment_report.txt

## What is in this repository
src/    Contains Python source modules. 
tests/  Contains the provided tests and my own tests
data/    Contains the original input data
results/ Stores generated output, such as the environment report
README.md   Explains the project setup, commands and repository contents
requirements.txt    Specifies the packages needed for the project
requirements-frozen.txt Records the installed package versions
pytest.ini  Contains pytest configuration
.gitignore  Specifies files and folders Git should ignore
AI_USE_LOG.md   Records use of AI for this assignment
src/env_check.py    Reports Python, platform and package versions
src/basics.py   Contains the functions for calculating and formatting the GC report
tests/test_lab01_own.py Contains the additional tests 

## What is not committed, and why
.venv/ and results/ must stay out of Git because they are not needed in Git.If commit them, the repository will become too large and may cause problems for other users.
