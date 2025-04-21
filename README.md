# JiraPilot 🚀

JiraPilot automates boilerplate code generation from Jira tickets using GitHub Copilot LLM.  
Triggered by Jira webhooks on feature branch creation, it reads prompts from the ticket description and generates code directly into your repo.

## Features
- Parses structured Jira descriptions (markdown-style)
- Calls GitHub Copilot LLM API with prompt and repo context
- Supports creating new files or appending to existing ones
- Auto-commits to a feature branch using the Jira ticket name

## Usage
1. Set up a Jira webhook pointing to your GitHub repo dispatch endpoint.
2. Format your Jira ticket description with:
