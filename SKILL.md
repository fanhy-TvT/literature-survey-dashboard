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
- **Extract Text**: Use the script `scripts/extract_pdfs.py` (located in this skill's directory) to extract text from the PDFs. Example: `python path/to/skill/scripts/extract_pdfs.py --input_dir <pdf_dir> --output_file raw_text.txt --pages 5 --chars 10000`.
- **Generate Summaries**: Create a detailed Markdown summary file for each paper. 
  - **NO SCRIPTING FOR SUMMARIES**: You MUST write each Markdown (`.md`) file directly using your standard file-writing tools. DO NOT write a Python script to generate the markdown files in bulk. Process, analyze, and write them one by one to ensure maximum quality and analytical depth.
  - **NO EMPTY SECTIONS**: Every single section defined in the template MUST be filled out comprehensively for every paper. You are strictly forbidden from leaving any section (e.g., Motivation, Implementation Details) empty, omitting it, or writing placeholders. If explicit details are missing in the extracted text, infer the most likely context or explicitly state what is missing, but the section MUST have substantial analytical content.
  - **DEFAULT BEHAVIOR: EXHAUSTIVE SUMMARY**: By default, you MUST generate a summary for EVERY SINGLE PAPER in the directory. Do not filter or select a subset unless the user explicitly instructs you to "only summarize the most relevant ones".
  - **COMPREHENSIVENESS REQUIRED**: Do not write brief or superficial summaries. You MUST write highly detailed, multi-paragraph explanations for Motivation, Proposed Method, and Experimental Results (including specific numbers/metrics).
  - **CRITICAL**: Use the templates provided in this skill's `templates/` directory. 
    - `summary_template_en.md` for English
    - `summary_template_zh.md` for Simplified Chinese
    - `summary_template_zh-tw.md` for Traditional Chinese
    - `summary_template_ja.md` for Japanese
  - Ensure the output strictly follows the template headers so the parsing script works correctly.
  - **Relevance to User's Idea**: This is the most important section. Analyze how this paper supports, contradicts, or inspires the user's specific research idea.

### 2. Web Search for Related Papers
- **Robust Literature Retrieval**: Do not just perform one simple search. Formulate 3-5 different search queries based on the user's idea and the insights from local papers. 
- Find **6-10** recent (last 2-3 years) and highly impactful papers that are NOT in the local directory. Dig deep into the literature tree.
- Generate the same strictly detailed Markdown summaries for these newly found papers, using the user's language.

### 3. Generate Global Synthesis Report
- After generating all individual paper summaries, you MUST create a single global synthesis report (e.g., `global_summary.md`) that deeply integrates the insights from all papers.
- **CRITICAL**: Use the global templates provided in this skill's `templates/` directory based on the user's language:
  - `global_template_en.md` for English
  - `global_template_zh.md` for Simplified Chinese
  - `global_template_zh-tw.md` for Traditional Chinese
  - `global_template_ja.md` for Japanese
- **Citations Required**: You MUST correctly cite the specific papers (e.g., "Dohare et al., 2024") when mentioning insights, methods, or risks.
- **Synthesis Focus**: This report MUST heavily synthesize and summarize the "Relevance to User's Idea" sections from the individual summaries. Do not just list the papers; synthesize the knowledge to provide actionable advice.

### 4. Generate HTML Dashboard
- Execute the script `scripts/generate_dashboard.py` (located in this skill's directory) to parse the Markdown summaries and generate the interactive HTML file.
- Example: `python path/to/skill/scripts/generate_dashboard.py --input_dir <summaries_dir> --output_file paper_comparison.html --lang <en|zh|zh-tw|ja>`
- The dashboard will now automatically include a link to the `global_summary.md` file, so the user can open it directly from the dashboard.
- Start a local HTTP server (e.g., `python -m http.server 8080`) in a non-blocking terminal and use the `OpenPreview` tool to show the dashboard to the user.

## Important Notes
- **Adaptive Language**: You MUST detect the language of the user's initial prompt (e.g., English, Chinese, etc.) and generate ALL outputs—including Markdown summaries, section headers, HTML table headers, and HTML UI elements—in that exact same language.
- **Autonomy**: You are an autonomous agent. Write the extraction scripts, generation scripts, and parsing scripts yourself. Execute them, handle any errors, and present the final polished HTML dashboard.
