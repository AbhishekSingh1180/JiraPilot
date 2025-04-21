# JiraPilot - Ollama Code Generation

JiraPilot is an automated system that integrates Jira and GitHub to generate code based on the descriptions from Jira issues. It uses Ollama's LLM (Large Language Model) to process the description provided in a Jira issue, generate the corresponding code, and push it to a feature branch in GitHub.

This README provides an overview of how JiraPilot works, including the workflow, setup instructions, and troubleshooting steps.

## Detailed Workflow Diagram

```mermaid
graph TD
  A[Jira Webhook: Feature Branch Created] --> B[GitHub Action Triggered]
  B --> C[Parse Jira Ticket Description]
  C --> D[Extract Prompt, Filename, and Path]
  D --> E[Call Ollama API to Generate Code]
  E --> F[Handle Code Generation Success or Failure]
  F --> G[Write Generated Code to Specified File Path]
  G --> H[Check if the Feature Branch Already Exists]
  H --> I[If Exists, Version Branch]
  I --> J[Commit Code to Feature Branch]
  J --> K[Push Changes to GitHub]

