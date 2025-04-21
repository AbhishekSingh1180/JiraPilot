FROM python:3.11-slim

WORKDIR /app

# Install system deps & Ollama
RUN apt-get update && apt-get install -y curl git && \
    curl -fsSL https://ollama.com/install.sh | sh

# Copy requirements and install Python deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy codegen script
COPY generate_code.py .

# Pull model ahead of time (e.g., gemma:2b)
ARG OLLAMA_MODEL=gemma:2b
RUN /root/.ollama/bin/ollama pull $OLLAMA_MODEL

# Run Ollama in background and then generate code
CMD /root/.ollama/bin/ollama serve & sleep 5 && python generate_code.py
