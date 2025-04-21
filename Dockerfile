FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y curl

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | bash

# Add ollama to PATH
ENV PATH="/root/.ollama/bin:${PATH}"

# Set working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the code generation script
COPY code_generator.py .

# Default command to run
CMD ["python3", "code_generator.py"]
