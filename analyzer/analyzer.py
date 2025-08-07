# analyzer/analyzer.py

from analyzer.model import run_prompt
from analyzer.scanner import split_code_into_numbered_chunks

def build_prompt(code: str, prompt_type: str = "default") -> str:
    
    if prompt_type == "default":
        return (
        "You are a static analyzer for C/C++.\n"
        "List only real vulnerabilities using this format:\n"
        "Line <number>: possible <type> due to <cause>\n"
        "Do not repeat lines. Keep it concise.\n"
        f"{code}\n\n"
        "Now list the issues"
        )

    elif prompt_type == "fix":
        return (
        "You are a static analyzer for C/C++.\n"
        "List only real vulnerabilities using this format:\n"
        "Line <number>: possible <type> due to <cause>\n"
        "Fix: <A short suggestion on how to fix it>.\n"
        "Do not repeat lines. Keep it concise.\n"
        f"{code}\n\n"
        "Now list the issues and fixes:"
        
        )

    else:
        raise ValueError(f"Unknown prompt type: {prompt_type}")

def analyze_code(llm, code: str ,prompt_type: str = "default") -> str:
    chunks = split_code_into_numbered_chunks(code, max_lines=50)
    results = []
    for chunk in chunks:
        prompt = build_prompt(chunk,prompt_type)  
        result = run_prompt(llm, prompt)
        
        results.append(result)
    return "\n\n\n".join(results)

