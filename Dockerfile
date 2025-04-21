# Use an official Ubuntu as a base image
FROM ubuntu:20.04

# Install dependencies (curl, python3, pip, etc.)
RUN apt-get update && apt-get install -y \
    curl \
    python3 \
    python3-pip \
    tar \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (if required)
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Install Ollama
RUN curl -sSL https://ollama.com/ollama-linux-x64.tar.gz | tar -xz -C /root/.ollama

# Set the path for Ollama
ENV PATH="/root/.ollama:$PATH"

# Copy the code generation script into the container
COPY generate_code.py /app/generate_code.py

# Make sure to set the working directory to /app
WORKDIR /app

# Set default entrypoint to Ollama (you can change this if needed)
ENTRYPOINT ["/root/.ollama/ollama"]

# Define the command to pull a model (optional, you can pull the model at build time)
CMD ["pull", "gemma:2b"]
