import argparse
import os
import requests

def generate_code(description, model="gemma:2b"):
    """Send description to Ollama and generate code"""
    ollama_api_url = "http://localhost:11434/v1/generate"  # Make sure Ollama is running on this port

    # Request the generated code from Ollama
    response = requests.post(ollama_api_url, json={"prompt": description, "model": model})

    if response.status_code == 200:
        return response.text  # Code generated
    else:
        return f"Error generating code: {response.status_code} - {response.text}"

def main():
    parser = argparse.ArgumentParser(description="Code Generator using Ollama LLM.")
    parser.add_argument('--description', type=str, required=True, help="The description of the task from Jira")
    args = parser.parse_args()

    # Get the description and generate the code
    generated_code = generate_code(args.description)
    
    # Print the generated code (you could save this to a file)
    print(f"Generated Code:\n{generated_code}")

    # Optionally: You can save it to a file and commit it back to GitHub (more steps required)
    with open("generated_code.py", "w") as f:
        f.write(generated_code)

if __name__ == "__main__":
    main()
