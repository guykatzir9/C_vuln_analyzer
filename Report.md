1. Introduction

This project was completed as part of a take-home assignment for the Open Source Software Engineer role. The goal was to build a CLI-based static analysis tool that uses a local LLM to detect vulnerabilities in C/C++ code.

2. Getting Started

Timeline:
I began the project on the afternoon of July 27th, immediately after completing a university exam. With approximately 2.5 days available, I prioritized quick iteration and efficiency.

3. Initial Planning and Technology Decisions

- Language Selection:
My initial instinct was to use Java due to its performance advantages and my prior experience. However, after online researching the performance bottlenecks on local LLM-based solutions, I realized that model evaluation — especially running locally — would dominate execution time. Because of this, I shifted to Python for the following advantages:

Faster development cycle (important given the time constraint).

Convenient CLI tooling (e.g., argparse).

Rich ecosystem for LLM tooling and model interfacing.

- Model Selection
I chose Phi-4 Mini from Hugging Face, selecting the Q4_K_S compressed version in .gguf format for the following reasons:

It provides a good tradeoff between accuracy and performance.

It’s small enough to run locally on CPU.

.gguf is optimized for use with llama.cpp.

- LLM Backend: llama-cpp-python
I selected llama-cpp-python as the LLM runtime for:

CPU Optimization – My machine lacks a dedicated GPU.

Compatibility with gguf models – Direct support for the compressed format.

Hybrid Development Advantage – A performant C++ backend combined with Python bindings for ease of use.

4. Project Structure (Initial Plan)

At this stage, I scoped out the basic architecture and responsibilities of each module:

cli.py: Entry point for CLI interaction; parses user input and flags.

analyzer.py: Core logic to interact with the model and analyze input code.

model.py: Loads and manages the LLM instance, ensuring it stays in memory.

During implementation, I later added two more components:

Preprocessing: To prepare input code for chunking, line numbering, and LLM formatting.

Postprocessing: To normalize and clean LLM output, remove duplicates, and make output readable.

5. Implementation Strategy

After setting up the environment and basic structure, I began implementing each component with a focus on modularity and maintainability. My goal was to first get a minimal working prototype, and then improve its functionality, performance, and accuracy incrementally.

I prioritized:

Clean architecture and code readability

Isolation of concerns across CLI, model handling, analysis logic, preprocessing, and postprocessing

Making the tool easy to scale and improve later

6. Performance Challenges and Solutions
Once I had the basic infrastructure working, I encountered a major obstacle: extremely slow run times for model evaluation. This was a key bottleneck that required addressing before continuing development.

Solutions I Implemented:
- Enabled multithreading in llama-cpp-python using the n_threads parameter

- Switched terminals: moved from WSL to native PowerShell to reduce overhead

- Freed disk space: cleaned up unnecessary files to avoid slowdowns from low storage

- Used minimal C test files to speed up testing loops

- Experimented with smaller model variants for better responsiveness

These steps allowed me to reduce evaluation time significantly and made the tool usable for real-world files.

7. Improving Precision with Prompt Engineering

The second major challenge was improving the accuracy and consistency of vulnerability detection. The raw model output was often too verbose, inconsistent, or missed obvious issues.

To address this, I:

- Iterated on prompt phrasing and length:

    Longer prompts gave better coverage but sometimes confused the model

    Shorter prompts were faster but missed context

- Removed formatting instructions from the prompt and implemented formatting in code instead

8. Preprocessing & Postprocessing Components:

scanner.py — Input Preprocessing:

Splits the input C/C++ code into manageable chunks, to respect the model’s context limit

Adds explicit line numbers (e.g., 1: int main() {}) to help the model refer to specific lines

Initial strategy was to split by function, but chunking by fixed line count yielded more reliable results

formatter.py — Output Postprocessing:

Transforms inconsistent model responses into clean, readable output

Extracts and deduplicates meaningful issues line by line

Ensures output is structured (e.g., with two newlines between issues)

9. Final Submission and Reflections
After iterating and improving both performance and precision, I submitted the best version I could within the available time and resources. The tool performs well on small-to-medium C/C++ files and reliably detects common vulnerabilities like buffer overflows and unsafe API usage.

To extend the tool’s usefulness, I implemented an optional --fix flag. When activated, this flag adjusts the prompt to ask the model for suggested fixes for each detected vulnerability. This allows users to not only identify issues, but also receive practical guidance on how to address them — all within the same output format.

However, I’m aware that the model’s accuracy is still not perfect on all inputs — especially more complex or edge-case code files. This is due to the limitations of both prompt-based LLMs and the constraints of running locally on CPU.

10. Possible Future Improvements
If I had more time and resources, I would focus on:

Allowing GPU Acceleration: llama-cpp supports GPU execution via CUDA or Metal, which would drastically reduce evaluation time and allow for larger batch processing.

Applying Larger Models: Upgrading to a higher-parameter model (e.g., full Phi-4 or a fine-tuned variant) could improve precision and language understanding for complex patterns.

