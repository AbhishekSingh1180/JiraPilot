import os
import requests

description = os.getenv("DESCRIPTION")
model = os.getenv("OLLAMA_MODEL", "gemma3:1b")

def generate_code(prompt):
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "")

if __name__ == "__main__":
    print("=== INPUT DESCRIPTION ===")
    print(description)
    print("=========================\n")
    print("=== GENERATED CODE ===")
    print(generate_code(description))
    print("=======================")
