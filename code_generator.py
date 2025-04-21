import requests
import sys

def generate_code(prompt):
    url = "http://localhost:11434/api/generate"
    response = requests.post(url, json={
        "model": "gemma3:1b",  # You can change the model if needed
        "prompt": prompt,
        "stream": False
    })
    return response.json().get("response", "")

def main():
    # The description from Jira will be passed as a command-line argument
    prompt = sys.argv[1]
    
    # Generate code based on the provided prompt
    generated_code = generate_code(prompt)

    # Write the generated code to a file
    with open("generated_code.py", "w") as file:
        file.write(generated_code)

if __name__ == "__main__":
    main()
