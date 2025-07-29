# analyzer/scanner.py
# Reads and validates the contents of a C/C++ source file

import os
import re

def read_c_file(path: str) -> str:
    
    if not os.path.exists(path):
        raise RuntimeError(f" File not found: {path}")

    if not os.path.isfile(path):
        raise RuntimeError(f" Not a file: {path}")

    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        raise RuntimeError(f" Failed to read file '{path}': {e}")
    
def split_code_into_numbered_chunks(code: str, max_lines: int = 50) -> list[str]:
    lines = code.splitlines()
    chunks = []

    for i in range(0, len(lines), max_lines):
        chunk_lines = lines[i:i + max_lines]
        start_line = i + 1
        numbered_chunk = "\n".join(f"Line {start_line + j}: {line}" for j, line in enumerate(chunk_lines))

        chunks.append(numbered_chunk)

    return chunks

