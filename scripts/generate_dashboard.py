import os
import re
import argparse

def get_section(content, section_names, is_last=False):
    """Extracts content between a section header and the next section header."""
    for name in section_names:
        # Match both **Section** and **Section (English)** formats
        if is_last:
            pattern = r'\*\*(?:' + re.escape(name) + r')(?:\s*\([^)]+\))?\*\*:\s*(.*)'
        else:
            pattern = r'\*\*(?:' + re.escape(name) + r')(?:\s*\([^)]+\))?\*\*:\s*(.*?)(?=\n\*\*|$)'
        m = re.search(pattern, content, re.S)
        if m:
            return m.group(1).strip()
    return ''

def md_to_html(text):
    if not text:
        return ""
    text = text.replace('\n', '<br>')
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    return text

def generate_dashboard(summaries_dir, output_file, lang='en', global_summary_path=None):
    papers = []
    
    # Define section mappings based on language
    sections = {
        'zh': {
            'author': [r'作者', r'来源'],
            'motivation': [r'研究动机', r'Motivation'],
            'method': [r'提出的方法', r'Proposed Method'],
            'details': [r'实现细节', r'Implementation Details'],
            'results': [r'实验结果', r'Experimental Results'],
            'summary': [r'核心内容总结', r'Core Summary'],
            'relevance': [r'与用户想法的关联', r'Relevance']
        },
        'zh-tw': {
            'author': [r'作者', r'來源'],
            'motivation': [r'研究動機', r'Motivation'],
            'method': [r'提出的方法', r'Proposed Method'],
            'details': [r'實現細節', r'Implementation Details'],
            'results': [r'實驗結果', r'Experimental Results'],
            'summary': [r'核心內容總結', r'Core Summary'],
            'relevance': [r'與用戶想法的關聯', r'Relevance']
        },
        'ja': {
            'author': [r'著者', r'出典'],
            'motivation': [r'研究の動機', r'Motivation'],
            'method': [r'提案手法', r'Proposed Method'],
            'details': [r'実装の詳細', r'Implementation Details'],
            'results': [r'実験結果', r'Experimental Results'],
            'summary': [r'コアサマリー', r'Core Summary'],
            'relevance': [r'ユーザーのアイデアとの関連性', r'Relevance']
        },
        'en': {
            'author': [r'Author', r'Source'],
            'motivation': [r'Motivation'],
            'method': [r'Proposed Method'],
            'details': [r'Implementation Details'],
            'results': [r'Experimental Results'],
            'summary': [r'Core Summary'],
            'relevance': [r'Relevance', r'Relevance to User']
        }
    }
    
    # Fallback to English if lang not found
    lang_keys = sections.get(lang, sections['en'])
    
    global_summary_basename = os.path.basename(global_summary_path) if global_summary_path else 'global_summary.md'
    
    for filename in os.listdir(summaries_dir):
        if not filename.endswith('.md'):
            continue
        if filename == global_summary_basename:
            continue
            
        with open(os.path.join(summaries_dir, filename), 'r', encoding='utf-8') as f:
            content = f.read()
            
        title_m = re.search(r'^#\s+(.*)', content, re.M)
        author_val = get_section(content, lang_keys['author'])
        
        papers.append({
            'title': title_m.group(1).strip() if title_m else filename,
            'author': author_val,
            'motivation': get_section(content, lang_keys['motivation']),
            'method': get_section(content, lang_keys['method']),
            'details': get_section(content, lang_keys['details']),
            'results': get_section(content, lang_keys['results']),
            'summary': get_section(content, lang_keys['summary']),
            'relevance': get_section(content, lang_keys['relevance'], is_last=True)
        })

    # UI Strings based on language
    ui = {
        'zh': {
            'title': '📚 论文对比矩阵 - 文献综述仪表盘',
            'search_placeholder': '🔍 搜索论文标题、作者或核心关键词...',
            'total_papers': '共展示',
            'papers_unit': '篇相关文献',
            'global_report': '📄 打开全局综合报告 (Global Report)',
            'col_paper': '论文标题 / 作者',
            'col_motivation': '研究动机 (Motivation)',
            'col_method': '核心方法与细节 (Method & Details)',
            'col_results': '实验结果与总结 (Results & Summary)',
            'col_relevance': '💡 与研究方向的关联 (Relevance)',
            'lbl_method': '方法:',
            'lbl_details': '细节:',
            'lbl_results': '结果:',
            'lbl_summary': '总结:'
        },
        'zh-tw': {
            'title': '📚 論文對比矩陣 - 文獻探討儀表板',
            'search_placeholder': '🔍 搜尋論文標題、作者或核心關鍵字...',
            'total_papers': '共展示',
            'papers_unit': '篇相關文獻',
            'global_report': '📄 打開全局綜合報告 (Global Report)',
            'col_paper': '論文標題 / 作者',
            'col_motivation': '研究動機 (Motivation)',
            'col_method': '核心方法與細節 (Method & Details)',
            'col_results': '實驗結果與總結 (Results & Summary)',
            'col_relevance': '💡 與研究方向的關聯 (Relevance)',
            'lbl_method': '方法:',
            'lbl_details': '細節:',
            'lbl_results': '結果:',
            'lbl_summary': '總結:'
        },
        'ja': {
            'title': '📚 論文比較マトリックス - 文献調査ダッシュボード',
            'search_placeholder': '🔍 タイトル、著者、キーワードを検索...',
            'total_papers': '表示中',
            'papers_unit': '件の関連論文',
            'global_report': '📄 グローバル統合レポートを開く (Global Report)',
            'col_paper': '論文タイトル / 著者',
            'col_motivation': '研究の動機 (Motivation)',
            'col_method': '提案手法と詳細 (Method & Details)',
            'col_results': '実験結果と概要 (Results & Summary)',
            'col_relevance': '💡 研究の方向性との関連性 (Relevance)',
            'lbl_method': '手法:',
            'lbl_details': '詳細:',
            'lbl_results': '結果:',
            'lbl_summary': '概要:'
        },
        'en': {
            'title': '📚 Paper Comparison Matrix - Literature Survey Dashboard',
            'search_placeholder': '🔍 Search titles, authors, or keywords...',
            'total_papers': 'Showing',
            'papers_unit': 'relevant papers',
            'global_report': '📄 Open Global Synthesis Report',
            'col_paper': 'Title / Author',
            'col_motivation': 'Motivation',
            'col_method': 'Method & Details',
            'col_results': 'Results & Summary',
            'col_relevance': '💡 Relevance to Research',
            'lbl_method': 'Method:',
            'lbl_details': 'Details:',
            'lbl_results': 'Results:',
            'lbl_summary': 'Summary:'
        }
    }
    
    texts = ui.get(lang, ui['en'])

    html_template = f"""
    <!DOCTYPE html>
    <html lang="{lang}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{texts['title']}</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; margin: 0; padding: 20px; background-color: #f8f9fa; color: #333; }}
            h1 {{ text-align: center; color: #2c3e50; margin-bottom: 20px; }}
            .controls {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; background: #fff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }}
            .search-box {{ width: 400px; padding: 10px; border: 1px solid #ced4da; border-radius: 4px; font-size: 14px; outline: none; transition: border-color 0.2s; }}
            .search-box:focus {{ border-color: #007bff; }}
            .table-container {{ overflow-x: auto; background: #fff; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            table {{ width: 100%; border-collapse: collapse; min-width: 1200px; table-layout: fixed; }}
            th, td {{ padding: 16px; text-align: left; border-bottom: 1px solid #e9ecef; vertical-align: top; }}
            th {{ background-color: #343a40; color: #fff; position: sticky; top: 0; z-index: 10; font-weight: 600; width: 20%; }}
            th:first-child {{ width: 15%; }}
            th:last-child {{ width: 25%; background-color: #2c3e50; }}
            tr:hover {{ background-color: #f8f9fa; }}
            .col-title {{ font-weight: bold; color: #0056b3; font-size: 1.05em; line-height: 1.4; }}
            .col-author {{ font-size: 0.85em; color: #6c757d; margin-top: 8px; font-weight: normal; }}
            .col-text {{ font-size: 0.95em; line-height: 1.6; }}
            .relevance {{ background-color: #e3f2fd; padding: 12px; border-radius: 6px; border-left: 4px solid #007bff; font-size: 0.95em; line-height: 1.6; }}
            .scrollable-cell {{ max-height: 350px; overflow-y: auto; padding-right: 8px; }}
            .section-title {{ font-weight: bold; color: #495057; margin-bottom: 4px; display: inline-block; padding-top: 8px; }}
            .section-title:first-child {{ padding-top: 0; }}
            /* Custom Scrollbar */
            ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
            ::-webkit-scrollbar-track {{ background: #f1f1f1; }}
            ::-webkit-scrollbar-thumb {{ background: #c1c1c1; border-radius: 4px; }}
            ::-webkit-scrollbar-thumb:hover {{ background: #a8a8a8; }}
            .global-btn {{ background: #28a745; color: white; padding: 8px 16px; text-decoration: none; border-radius: 4px; font-weight: bold; font-size: 14px; transition: background 0.2s; }}
            .global-btn:hover {{ background: #218838; }}
            .search-container {{ display: flex; align-items: center; gap: 15px; }}
        </style>
    </head>
    <body>
        <h1>{texts['title']}</h1>
        <div class="controls">
            <div class="search-container">
                <input type="text" id="searchInput" class="search-box" placeholder="{texts['search_placeholder']}">
                <div>{texts['total_papers']} <strong id="count" style="color:#007bff; font-size: 1.2em;"></strong> {texts['papers_unit']}</div>
            </div>
            <a href="global_summary.html" class="global-btn" target="_blank">{texts['global_report']}</a>
        </div>
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>{texts['col_paper']}</th>
                        <th>{texts['col_motivation']}</th>
                        <th>{texts['col_method']}</th>
                        <th>{texts['col_results']}</th>
                        <th>{texts['col_relevance']}</th>
                    </tr>
                </thead>
                <tbody>
    """

    for p in papers:
        row = f"""
                    <tr>
                        <td class="col-title">
                            {md_to_html(p['title'])}
                            <div class="col-author">{md_to_html(p['author'])}</div>
                        </td>
                        <td class="col-text"><div class="scrollable-cell">{md_to_html(p['motivation'])}</div></td>
                        <td class="col-text">
                            <div class="scrollable-cell">
                                <span class="section-title">{texts['lbl_method']}</span><br>{md_to_html(p['method'])}<br>
                                <span class="section-title">{texts['lbl_details']}</span><br>{md_to_html(p['details'])}
                            </div>
                        </td>
                        <td class="col-text">
                            <div class="scrollable-cell">
                                <span class="section-title">{texts['lbl_results']}</span><br>{md_to_html(p['results'])}<br>
                                <span class="section-title">{texts['lbl_summary']}</span><br>{md_to_html(p['summary'])}
                            </div>
                        </td>
                        <td class="col-text">
                            <div class="scrollable-cell relevance">
                                {md_to_html(p['relevance'])}
                            </div>
                        </td>
                    </tr>
        """
        html_template += row

    html_template += """
                </tbody>
            </table>
        </div>
        <script>
            const input = document.getElementById('searchInput');
            const table = document.querySelector('table tbody');
            const rows = table.getElementsByTagName('tr');
            const countSpan = document.getElementById('count');
            countSpan.textContent = rows.length;

            input.addEventListener('keyup', function() {
                const filter = input.value.toLowerCase();
                let visibleCount = 0;
                for (let i = 0; i < rows.length; i++) {
                    const text = rows[i].textContent.toLowerCase();
                    if (text.includes(filter)) {
                        rows[i].style.display = '';
                        visibleCount++;
                    } else {
                        rows[i].style.display = 'none';
                    }
                }
                countSpan.textContent = visibleCount;
            });
        </script>
    </body>
    </html>
    """

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"Generated HTML dashboard at {output_file}")
    
    # Also generate an HTML wrapper for global_summary to fix encoding issues in browsers
    if global_summary_path and os.path.exists(global_summary_path):
        with open(global_summary_path, 'r', encoding='utf-8') as f:
            global_content = f.read()
        
        safe_content = global_content.replace('</textarea>', '&lt;/textarea&gt;')
        global_html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{texts['global_report']}</title>
    <style>
        body {{ font-family: system-ui, -apple-system, sans-serif; line-height: 1.6; max-width: 900px; margin: 0 auto; padding: 40px 20px; color: #333; }}
        h1, h2, h3, h4 {{ color: #2c3e50; margin-top: 1.5em; }}
        h1, h2 {{ border-bottom: 1px solid #eee; padding-bottom: 10px; }}
        code {{ background: #f4f4f4; padding: 2px 5px; border-radius: 4px; font-family: monospace; font-size: 0.9em; color: #d63384; }}
        pre {{ background: #f4f4f4; padding: 15px; border-radius: 8px; overflow-x: auto; }}
        pre code {{ color: inherit; background: transparent; padding: 0; }}
        blockquote {{ border-left: 4px solid #007bff; margin: 0 0 1em 0; padding-left: 15px; color: #555; background: #f8f9fa; padding: 10px 15px; border-radius: 0 4px 4px 0; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1em 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px 12px; text-align: left; }}
        th {{ background-color: #f4f4f4; }}
        a {{ color: #007bff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div id="content">Loading report...</div>
    <textarea id="markdown-source" style="display:none;">{safe_content}</textarea>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script>
        document.getElementById('content').innerHTML = marked.parse(document.getElementById('markdown-source').value);
    </script>
</body>
</html>"""
        out_dir = os.path.dirname(output_file)
        global_html_path = os.path.join(out_dir, 'global_summary.html')
        with open(global_html_path, 'w', encoding='utf-8') as f:
            f.write(global_html)
        print(f"Generated HTML global summary at {global_html_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate HTML Dashboard from Markdown summaries')
    parser.add_argument('--input_dir', required=True, help='Directory containing markdown summaries')
    parser.add_argument('--output_file', required=True, help='Output HTML file path')
    parser.add_argument('--lang', default='en', choices=['en', 'zh', 'zh-tw', 'ja'], help='Language for the dashboard UI')
    parser.add_argument('--global_summary', default=None, help='Path to the global summary markdown file')
    args = parser.parse_args()
    
    generate_dashboard(args.input_dir, args.output_file, args.lang, args.global_summary)
