# Copilot Instructions for AI Coding Agents

## Overview
This workspace is a collection of Python scripts and small projects organized by topic (e.g., lists, dictionaries, conditionals, loops, pandas, file operations, recursion, etc.). There is no monolithic application or framework; instead, the codebase serves as a learning and experimentation environment for Python concepts and data manipulation.

## Directory Structure
- Top-level folders (e.g., `A_dict/`, `A_list/`, `condition/`, `function/`, `File_prac/`, `Pandas_Prac/`, `project/`, etc.) contain scripts focused on specific Python features or mini-projects.
- The `env/` directory contains a Python virtual environment. Use its `python.exe` and `pip.exe` for package management and script execution.
- Data files (CSV, JSON, XLSX, DOCX) are used for input/output in various scripts, especially in `Pandas_Prac/` and project folders.

## Developer Workflows
- **Running scripts:** Most scripts are standalone and can be run directly with the workspace's Python interpreter. Example:
  ```powershell
  .\env\Scripts\python.exe .\A_dict\dict_data_code.py
  ```
- **Managing dependencies:** Use `.\env\Scripts\pip.exe install <package>` to add packages to the environment.
- **Testing:** There is no unified test framework; test scripts are named with `test_*.py` or reside in folders like `project/` or `Pandas_Prac/`. Run them as regular scripts.
- **Debugging:** Use print statements or Python debuggers (`pdb`) as needed. No custom debugging tools are present.

## Patterns & Conventions
- Scripts are organized by topic for clarity and learning. Each folder is self-contained.
- Data files are often read/written in the same directory as the script using relative paths.
- Naming conventions are descriptive but not strictly standardized; expect some variation.
- No custom decorators, metaclasses, or advanced Python patterns are used.
- Most scripts are procedural, with occasional use of functions.

## Integration Points
- External dependencies (e.g., pandas, snowflake) are used in relevant scripts. Check for `import` statements to identify required packages.
- No web services, APIs, or inter-process communication are present.
- Some scripts (e.g., in `Snowpark/`) may require access to external systems (e.g., Snowflake); configure credentials as needed.

## Key Files & Examples
- `A_dict/dict_data_code.py`: Dictionary operations
- `Pandas_Prac/test_pandas.py`: DataFrame manipulation
- `project/Calculator_with_history.py`: Example mini-project
- `Snowpark/installSnowpark.py`: Snowflake integration example

## Getting Started
1. Activate the virtual environment: `.\env\Scripts\Activate.ps1`
2. Install any missing packages: `.\env\Scripts\pip.exe install <package>`
3. Run scripts directly with `.\env\Scripts\python.exe <script>`

## AI Agent Guidance
- Prefer using the workspace's Python interpreter and pip for all operations.
- When adding new scripts, follow the topical organization and use descriptive filenames.
- Reference existing scripts for examples of data handling and function usage.
- Document any new patterns or workflows in this file for future agents.
