# analyzer/formatter.py
# Formats the output from the LLM for display or file writing

import json
import re

def postprocess_default_output(output: str) -> str:
    """
    Adds two newlines between separate vulnerability reports in 'default' mode.
    Accepts both 'Line <n>: ...' and '<n>: ...' formats.
    Filters out exact duplicates.
    """
    parts = re.findall(r'((?:Line )?\d+:.*?)(?=(?:Line )?\d+:|^\d+:|$)', output, flags=re.DOTALL | re.MULTILINE)
    
    seen = set()
    cleaned = []

    for part in parts:
        normalized = part.strip().lower()

        if "possible" not in normalized:
            continue

        if normalized not in seen:
            seen.add(normalized)
            cleaned.append(part.strip())

    return "\n\n".join(cleaned)


def postprocess_fix_output(output: str) -> str:
    """
    Splits combined lines (issue + fix) into two lines, and separates unique issues with two newlines.
    """
    import re
    parts = re.findall(r'(Line \d+:.*?)(?=(Line \d+:)|$)', output, flags=re.DOTALL)
    seen = set()
    cleaned = []

    for raw in parts:
        line = raw[0].strip()

        # Normalize line to ignore exact duplicates or safe lines
        normalized = line.lower().strip()

        if "possible" not in normalized:
            continue

        if normalized in seen:
            continue 

        seen.add(normalized)

        if "Fix:" in line:
            issue, fix = line.split("Fix:", 1)
            cleaned.append(issue.strip())
            cleaned.append("Fix: " + fix.strip())
        else:
            cleaned.append(line)

    return "\n\n".join(cleaned)

def format_output(result: str, prompt_type: str = "default") -> str:

    result = result.strip()

    if prompt_type == "fix":
        return postprocess_fix_output(result)
    else:
        return postprocess_default_output(result)

