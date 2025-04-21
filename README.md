# **JiraPilot: Automated Code Generation with Jira and GitHub Actions**

**JiraPilot** is a tool that automates code generation when a feature branch is created in Jira. The system integrates **Jira**, **GitHub Actions**, and **Ollama (a Local Large Language Model)** to generate boilerplate code based on the information provided in the Jira ticket description.

## 🚀 Features

- **Automated Code Generation**: Automatically generates boilerplate code based on the Jira issue description when a feature branch is created.
- **Jira Integration**: Utilizes Jira Automation to trigger GitHub Actions with branch details and description.
- **GitHub Actions**: GitHub Actions runs the code generation workflow on a dedicated runner.
- **Ollama for LLM**: Ollama (Local Large Language Model) generates code based on the prompt given in the Jira description.

## 🛠️ Setup

### 1. **Jira Configuration**

- Set up an automation rule in Jira to trigger a webhook whenever a new feature branch is created.
- The webhook sends the branch name, ticket key, and description to GitHub.

### 2. **GitHub Action Configuration**

- Configure a GitHub Action that listens for the `repository_dispatch` event triggered by Jira's webhook.
- The action runs the code generation process in a Docker container with Ollama and commits the generated code back to the feature branch.

### 3. **Docker Environment**

- Ollama is used within Docker to run the code generation process locally using a specified model.
- The Docker setup includes all dependencies needed to execute the code generation workflow.

## 🧑‍💻 Usage

1. **Trigger Jira webhook**: When a new branch is created in Jira, the webhook sends the necessary details (branch name, ticket key, description) to GitHub.
2. **GitHub Actions Workflow**: The GitHub Action processes the payload, runs the code generation process, and commits the generated code back to the feature branch.

## 🗂️ Diagram

Below is a flowchart that illustrates the process from Jira to code generation in GitHub:

```mermaid
flowchart TD
    A[Jira - New Feature Branch Created] --> B[Trigger Jira Webhook]
    B --> C[GitHub Action - Repository Dispatch Event]
    C --> D[Run Code Generation with Ollama]
    D --> E[Generate Boilerplate Code]
    E --> F[Commit Code to Feature Branch]
    F --> G[New Code Ready in Feature Branch]
