# JiraPilot

JiraPilot is an integration between **Jira**, **GitHub Actions**, and **Ollama** for automatic code generation. The project uses **Ollama**, a local large language model, to generate code based on a description provided in a Jira issue. The generated code is then committed back to the GitHub repository with a reference to the Jira ticket key.

## Workflow Overview

1. **Jira Automation**: When a feature branch is created in Jira, a webhook triggers a GitHub Actions workflow.
2. **Ollama Code Generation**: The workflow runs a Python script that communicates with Ollama to generate code based on the Jira ticket description.
3. **GitHub Commit**: The generated code is committed back to the GitHub repository with a commit message that includes the Jira issue key.

## Setup

1. **Jira Webhook**: Set up a Jira webhook to trigger the GitHub Action using the Jira Automation rule.
2. **GitHub Action**: The action triggers when the Jira issue is updated or a branch is created, calling the **Ollama** API and running the code generator.
3. **Ollama**: Ensure you have **Ollama** installed and running locally to generate code.

## Running the Workflow

1. Trigger the workflow manually or automatically from Jira by creating a new branch.
2. The GitHub Action pulls the required Ollama model and generates code.
3. The generated code is committed back to the repository with a commit message containing the Jira issue key.

## Requirements

- **Jira** with webhooks enabled.
- **Ollama** server running to handle code generation.
- GitHub repository with GitHub Actions enabled.

## License

This project is licensed under the MIT License.
