# Literature Survey & Dashboard Generator Skill

[![Language](https://img.shields.io/badge/Language-Multi-blue.svg)](#)

[简体中文](README_zh.md) | English

An autonomous AI agent skill that automates the entire workflow of academic paper surveying: extracting text from local PDFs, generating structured summaries, extending the search via the web, and compiling everything into an interactive HTML dashboard for easy comparison.

## Features
- 📄 **PDF Extraction**: Automatically reads and extracts text from local PDF papers.
- 🤖 **AI Summarization**: Generates structured summaries including Motivation, Method, Results, and Relevance to your specific research.
- 🌐 **Web Extension**: Automatically searches the web for recent, related papers to expand your survey.
- 📊 **Interactive Dashboard**: Compiles all summaries into a searchable, filterable HTML comparison matrix.
- 🌍 **Multi-Language Support**: Fully supports English, Simplified Chinese, Traditional Chinese, and Japanese.

## Directory Structure
- `SKILL.md`: The core prompt and instruction file for the AI agent.
- `scripts/extract_pdfs.py`: Python script for extracting text from PDFs.
- `scripts/generate_dashboard.py`: Python script for generating the interactive HTML dashboard.
- `templates/`: Markdown templates for structured paper summaries in multiple languages.

## Installation

You can install this skill into your AI Agent's workspace using one of the following methods:

### Method 1: Using npx (Recommended)
You can directly run the interactive installer using npm:
```bash
npx @fanhy-tvt/literature-survey-dashboard
```
The installer will interactively guide you to choose the installation location (Current Project or System Home Directory) and the target agent folder (e.g., `.trae`, `.agents`, `.claude`, etc.).

### Method 2: Git Clone
Clone this repository directly into your agent's skills folder:
```bash
cd /path/to/your/project/.trae/skills
git clone https://github.com/fanhy-TvT/literature-survey-dashboard.git
```

## How to Use
1. After installation, prompt your AI Agent: *"Use the literature-survey-dashboard skill to analyze the papers in `./papers` for my research on [Your Topic]."*
2. The agent will autonomously execute the scripts, generate summaries, and present the final HTML dashboard.

## License
This project is licensed under the [MIT License](LICENSE).
