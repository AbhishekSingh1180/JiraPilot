import os
import re
import requests
import yaml

description = os.getenv("DESCRIPTION", "")
model = os.getenv("OLLAMA_MODEL", "gemma3:1b")
ollama_url = "http://localhost:11434/api/generate"

def parse_description(desc):
    # Extract the YAML content between {code:yaml} and {code}
    yaml_match = re.search(r"\{code:yaml\}(.*?)\{code\}", desc, re.DOTALL)
    yaml_data = yaml_match.group(1).strip() if yaml_match else None
    
    # Parse YAML if found
    if yaml_data:
        parsed_yaml = yaml.safe_load(yaml_data)
    else:
        parsed_yaml = {}

    return parsed_yaml

def call_ollama(prompt):
    print("🧠 Calling Ollama with prompt:", prompt[:2000], "...")
    res = requests.post(ollama_url, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    res.raise_for_status()
    return res.json()["response"]

# Parse the incoming description
parsed = parse_description(description)
prompt = parsed.get("Prompt")
filename = parsed.get("Filename", "main.py")
filepath = parsed.get("Path", f"code/{filename}")

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

# Output filename with path for git add
print(f"Git add file: {filepath}")
