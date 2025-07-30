# 1. Start from a lightweight Python image
FROM python:3.10-slim

# 2. Install system dependencies (required for llama-cpp-python to compile)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential cmake && \
    rm -rf /var/lib/apt/lists/*

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy all project files into the container
COPY . .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Set the default command
ENTRYPOINT ["python", "cli.py"]
