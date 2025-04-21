import os
import re
import requests
from pathlib import Path

OLLAMA_API = "http://localhost:11434/api/generate"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma:2b")

def extract_prompt(description):
    pattern = r"## Prompt\s+(.*?)\s+## filename\s+(.*?)\s+## path\s+(.*?)$"
    match = re.search(pattern, description, re.DOTALL)
    if not match:
        raise ValueError("Invalid description format.")
    return {
        "prompt": match.group(1).strip(),
        "filename": match.group(2).strip(),
        "path": match.group(3).strip()
    }

def generate_with_ollama(prompt, model=OLLAMA_MODEL):
    print(f"🧠 Using Ollama model: {model}")
    print(f"📤 Sending prompt to Ollama:\n{prompt}\n")

    response = requests.post(
        OLLAMA_API,
        json={"model": model, "prompt": prompt, "stream": False},
        headers={"Content-Type": "application/json"}
    )
    response.raise_for_status()
    return response.json()["response"]

def main():
    description = os.getenv("DESCRIPTION", "")
    if not description:
        raise ValueError("DESCRIPTION environment variable is empty.")

    print("📦 Received DESCRIPTION payload:\n" + description + "\n")

    fields = extract_prompt(description)

    print("📑 Parsed fields:")
    print(f"  ▸ Filename  : {fields['filename']}")
    print(f"  ▸ Path      : {fields['path']}")
    print(f"  ▸ Prompt    : {fields['prompt']}\n")

    generated_code = generate_with_ollama(fields["prompt"])

    output_path = Path(fields["path"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write(generated_code)

    print(f"✅ Code successfully written to: {output_path}")

if __name__ == "__main__":
    main()
