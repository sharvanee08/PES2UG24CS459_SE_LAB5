# Software Engineering Lab 5 — Static Code Analysis

## Student Details

- **Name:** Sharvanee Naru
- **SRN:** PES2UG24CS459
- **Course:** Software Engineering Lab
- **Lab Number:** 5
- **Lab Title:** Static Code Analysis

## Objective

To improve Python code quality, security, readability, and maintainability using static analysis tools: Pylint, Bandit, and Flake8.

## Project Description

This lab analyzes a Python-based radio scheduling program that manages radio show slots, hosts, show timings, and booked durations using an SQLite in-memory database.

The program is examined using static analysis tools to identify security vulnerabilities, coding-quality issues, naming violations, and formatting errors. The identified issues are addressed, and the updated program is analyzed again to verify the improvements.

## Technologies Used

- **Python** — Programming language
- **SQLite3** — In-memory database
- **Pylint** — Code quality and programming practice analysis
- **Bandit** — Security vulnerability analysis
- **Flake8** — Python style and formatting checks
- **Git and GitHub** — Version control and source code management

## Tools and Their Purpose

| Tool | Purpose |
|---|---|
| Pylint | Identifies naming violations, missing docstrings, and code-quality issues |
| Bandit | Detects potentially insecure coding patterns |
| Flake8 | Detects formatting violations and style inconsistencies |

## Program Features

- Add radio show slots to an SQLite database.
- Generate formatted show labels.
- Check whether a show finishes before the next scheduled show.
- Retrieve shows scheduled before noon.
- Remove a show slot using its ID.
- Track the total booked duration.

## Static Analysis Workflow

1. Inspect and execute the original Python program.
2. Generate the original Pylint, Bandit, and Flake8 reports.
3. Identify and document the reported issues.
4. Fix security vulnerabilities and code-quality problems.
5. Resolve formatting violations.
6. Rerun all three tools to verify the fixes.
7. Record the changes in Git commits.

## Commands Used

### Run the Program

```bash
python radio_schedule.py
```

### Pylint

```bash
python -m pylint radio_schedule.py > pylint_before.txt
python -m pylint radio_schedule.py > pylint_after.txt
```

### Bandit

```bash
python -m bandit -r radio_schedule.py > bandit_before.txt
python -m bandit -r radio_schedule.py > bandit_after.txt
```

### Flake8

```bash
python -m flake8 radio_schedule.py > flake8_before.txt
python -m flake8 radio_schedule.py > flake8_after.txt
```

## Results

- **Pylint:** Achieved a score of 10.00/10 after fixing code-quality issues.
- **Bandit:** No issues identified in the final security analysis.
- **Flake8:** The final report was empty, indicating no reported style violations.

## Repository Structure

```text
PES2UG24CS459_SE_LAB5/
├── radio_schedule.py
├── pylint_before.txt
├── pylint_after.txt
├── bandit_before.txt
├── bandit_after.txt
├── flake8_before.txt
├── flake8_after.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Git Commits

1. `Add original radio schedule script`
2. `Fix Bandit security findings`
3. `Improve code quality with Pylint fixes`
4. `Resolve Flake8 formatting issues`

## Learning Outcomes

- Understood the importance of static code analysis.
- Identified potential security vulnerabilities in Python code.
- Improved naming conventions, documentation, and code structure.
- Applied Python formatting standards.
- Learned to verify code improvements using automated analysis tools.
- Practiced maintaining code changes using Git.

## Conclusion

This lab demonstrated how static analysis tools help improve the security, quality, and maintainability of Python programs. Applying Bandit, Pylint, and Flake8 helped identify and address insecure coding patterns, code-quality issues, and formatting violations without relying solely on program execution.
