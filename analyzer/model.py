# analyzer/model.py
# Loads the Phi-4 Mini model once and provides an interface for analyzing C/C++ code

from llama_cpp import Llama

# Path to the model file (relative to project root).
MODEL_PATH = "models\phi-4-mini-instruct-q4_k_m.gguf"

# Load the model once when this file is imported.
print("Loading LLM model...")
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, n_threads=8,verbose=False)

def load_model_instance():
    return llm

# Sends a raw prompt to the model and returns the text response.
def run_prompt(llm, prompt: str, max_tokens: int = 512) -> str:
    response = llm(prompt, max_tokens=max_tokens)
    return response["choices"][0]["text"].strip()    

