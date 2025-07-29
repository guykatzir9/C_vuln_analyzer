# analyzer/cli.py
# This is the command-line entry point to run the analyzer tool.

import argparse
from analyzer.scanner import read_c_file
from analyzer.model import load_model_instance
from analyzer.formatter import format_output
from analyzer.analyzer import analyze_code 

def main():
    parser = argparse.ArgumentParser(
        description="LLM-based static analyzer for C/C++ vulnerabilities"
    )

    # Required: input file path
    parser.add_argument("file", help="Path to the C/C++ source file")

    # Optional: enable fix suggestions
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Also suggest a one-line fix for each vulnerability"
    )

    args = parser.parse_args()

    # Step 1: read and validate the input C/C++ file
    code = read_c_file(args.file)
    
    # Step 2: load the LLM model
    llm = load_model_instance()

    # Step 3: analyze the code
    prompt_type = "fix" if args.fix else "default"

    print("Scanning the provided code for vulnerabilities...")
    result = analyze_code(llm, code, prompt_type=prompt_type)

    # Step 4: format the result
    formatted = format_output(result, prompt_type=prompt_type)

    # Step 5: print the result
    print("\n--- Analysis Result ---\n")
    print(formatted)

if __name__ == "__main__":
    main()

