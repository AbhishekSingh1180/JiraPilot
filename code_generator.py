import os
import re
import requests

description = os.getenv("DESCRIPTION", "")
model = os.getenv("OLLAMA_MODEL", "phi3:mini")
ollama_url = "http://localhost:11434/api/generate"

def parse_description(desc):
    def extract(tag):
        match = re.search(rf"## {tag}\s+(.*?)(?=\n##|\Z)", desc, re.DOTALL)
        return match.group(1).strip() if match else None

    return {
        "prompt": extract("Prompt"),
        "filename": extract("filename"),
        "path": extract("path")
    }

def call_ollama(prompt):
    print("🧠 Calling Ollama with prompt:", prompt[:60], "...")
    res = requests.post(ollama_url, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    res.raise_for_status()
    return res.json()["response"]

# Parse the incoming description
parsed = parse_description(description)
prompt = parsed["prompt"]
filename = parsed["filename"] or "main.py"
filepath = parsed["path"] or f"code/{filename}"

print("📦 Payload Info:")
print("  ✅ Prompt:", prompt)
print("  📄 Filename:", filename)
print("  📂 Path:", filepath)

# Generate code from prompt
try:
    code = call_ollama(prompt)
except Exception as e:
    print("❌ Ollama error:", str(e))
    code = f"# ERROR: Failed to generate from prompt\n# Prompt:\n{prompt}\n"

# Write the file
os.makedirs(os.path.dirname(filepath), exist_ok=True)
with open(filepath, "w") as f:
    f.write(code)

print(f"✅ Code written to: {filepath}")
