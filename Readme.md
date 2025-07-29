# 🔍 LLM Vulnerability Analyzer

A local command-line tool that uses a lightweight open-source LLM to analyze C/C++ source files and detect potential code vulnerabilities.  
This project was developed as part of a technical assignment and is designed to work entirely offline.

## Quick Start

### 1. Clone the repository

git clone https://github.com/guykatzir9/llm_vuln_analyzer.git
cd llm_gk_analyzer

### 2. Download the model

Download the `phi-4-mini-instruct-Q4_K_M.gguf` model file from Hugging Face:

https://huggingface.co/s0mecode/Phi-4-mini-instruct-Q4_K_M-GGUF/blob/main/phi-4-mini-instruct-q4_k_m.gguf

Place the downloaded file under the `models/` folder:

```
C_Vuln_analyzer/
└── models/
    └── phi-4-mini-instruct-Q4_K_M.gguf
```

> The model file is not included in this repository due to its large size.  
> Make sure to download and place it manually before running the tool.

### 3. Set up the virtual environment (choose between 2.1 or 2.2)

first Navigate to the project folder:
    cd path/to/C_vuln_analyzer

second depend on your os:    

### 3.1 Linux / macOS

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 3.2 Windows (CMD or PowerShell)

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

### 4. Run the analyzer on a C file

To run the analyzer, you must first activate the virtual environment and run the script from
the root of the project directory (C_vuln_analyzer).

run with absolute path:

    python cli.py <absolute path/to/code.c>

or if the file is on the test_files folder in the root of the project directory:

    python cli.py test_files\code.c (relative path)

> note:its optional to add --fix for fix suggestions (e.g "python cli.py test_files\code.c --fix").
---

## Project Structure

```
llm_gk_analyzer/
├── analyzer/          # Core logic for analysis and LLM interaction
├── models/            # Folder for downloaded .gguf model file
├── README.md          # This file
├── Report.md          # Documentation of design decisions and process
├── requirements.txt   # Python dependencies
├── .gitignore
```

## Features

- Local execution with no internet connection  
- LLM-powered vulnerability detection for C/C++ code  
- CLI architecture  
- offering fix suggestions

## Notes

- This tool is built around `llama-cpp-python` to run `phi-4-mini-instruct` locally.  
- Prompt engineering and chunking strategy are documented in `Report.md`.  
- The `.gguf` model file is excluded from version control (see `.gitignore`).

## Future Improvements (Optional Extras)

- [ ] JSON output format  
- [ ] Recursive directory scanning    
- [ ] Docker image for easy deployment
