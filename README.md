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

## How to Use
1. Install or copy this skill into your AI Agent's skill directory (e.g., `.trae/skills/` or any other agent framework directory).
2. Prompt your AI Agent: *"Use the literature-survey-dashboard skill to analyze the papers in `./papers` for my research on [Your Topic]."*
3. The agent will autonomously execute the scripts, generate summaries, and present the final HTML dashboard.
