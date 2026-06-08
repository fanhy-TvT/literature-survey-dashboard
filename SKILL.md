---
name: "literature-survey-dashboard"
description: "Reads PDF papers, summarizes them (motivation, method, results), searches for related papers, and generates an HTML comparison dashboard. Invoke when user wants a literature survey or paper dashboard."
---

# Literature Survey & Dashboard Generator

This skill automates the entire workflow of academic paper surveying: extracting text from local PDFs, generating structured summaries, extending the search via the web, and compiling everything into an interactive HTML dashboard for easy comparison.

## When to Use
Invoke this skill IMMEDIATELY when the user:
- Asks to read a directory of PDF papers and generate a summary matrix/dashboard.
- Requests a literature review workflow that includes reading local papers and searching for new ones online.
- Wants an HTML comparison dashboard for a set of academic papers.

## Workflow

When invoked, act as an autonomous research assistant and follow these steps. **Do not stop at intermediate steps** unless you need user clarification.

### 1. Extract and Summarize Local PDFs
- **Identify Inputs**: Ensure you know the directory containing the PDF papers and the user's specific research idea/topic (ask if not provided).
- **Extract Text**: Use the script `scripts/extract_pdfs.py` (located in this skill's directory) to extract text from the PDFs. Example: `python path/to/skill/scripts/extract_pdfs.py --input_dir <pdf_dir> --output_file raw_text.txt`.
- **Generate Summaries**: Create a detailed Markdown summary file for each paper. 
  - **CRITICAL**: Use the templates provided in this skill's `templates/` directory. 
    - `summary_template_en.md` for English
    - `summary_template_zh.md` for Simplified Chinese
    - `summary_template_zh-tw.md` for Traditional Chinese
    - `summary_template_ja.md` for Japanese
  - Ensure the output strictly follows the template headers so the parsing script works correctly.
  - **Relevance to User's Idea**: This is the most important section. Analyze how this paper supports, contradicts, or inspires the user's specific research idea.

### 2. Web Search for Related Papers
- Based on the user's core idea and the insights gathered from the local papers, use the `WebSearch` tool to find 3-5 recent and highly relevant papers that are NOT in the local directory.
- Generate the same structured Markdown summaries for these newly found papers, using the user's language.

### 3. Generate HTML Dashboard
- Execute the script `scripts/generate_dashboard.py` (located in this skill's directory) to parse the Markdown summaries and generate the interactive HTML file.
- Example: `python path/to/skill/scripts/generate_dashboard.py --input_dir <summaries_dir> --output_file paper_comparison.html --lang <en|zh|zh-tw|ja>`
- Start a local HTTP server (e.g., `python -m http.server 8080`) in a non-blocking terminal and use the `OpenPreview` tool to show the dashboard to the user.

## Important Notes
- **Adaptive Language**: You MUST detect the language of the user's initial prompt (e.g., English, Chinese, etc.) and generate ALL outputs—including Markdown summaries, section headers, HTML table headers, and HTML UI elements—in that exact same language.
- **Autonomy**: You are an autonomous agent. Write the extraction scripts, generation scripts, and parsing scripts yourself. Execute them, handle any errors, and present the final polished HTML dashboard.
