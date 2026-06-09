# 文献综述与仪表盘生成技能 (Literature Survey Dashboard)

[English](README.md) | 简体中文

这是一个用于 AI Agent 的自主技能，它能够自动化整个学术论文综述的工作流：从本地 PDF 提取文本、生成结构化摘要、通过网络搜索扩展文献库，并将所有内容编译成一个交互式的 HTML 对比仪表盘。

## 核心特性
- 📄 **PDF 提取**：自动读取并提取本地 PDF 论文的文本。
- 🤖 **AI 摘要**：生成包含研究动机、方法、结果以及与你具体研究方向关联的结构化总结。
- 🌐 **网络扩展**：自动在网上搜索最新相关论文，扩充你的文献库。
- 📊 **交互式仪表盘**：将所有摘要编译成一个支持搜索、过滤的 HTML 对比矩阵网页。
- 🌍 **多语言支持**：全面支持英文、简体中文、繁体中文和日语。

## 目录结构
- `SKILL.md`：AI Agent 的核心提示词与指令文件。
- `scripts/extract_pdfs.py`：用于从 PDF 提取文本的 Python 脚本。
- `scripts/generate_dashboard.py`：用于生成交互式 HTML 仪表盘的 Python 脚本。
- `templates/`：多语言的结构化论文摘要 Markdown 模板。

## 安装说明

你可以通过以下两种方式之一将该技能安装到你的 AI Agent 工作区中：

### 方式 1：使用 npx (推荐)
你可以直接使用 npm 运行交互式安装程序：
```bash
npx @fanhy-tvt/literature-survey-dashboard
```
安装程序会通过交互式提示，引导你选择安装位置（当前项目或系统主目录）以及目标代理文件夹（例如 `.trae`, `.agents`, `.claude` 等）。

### 方式 2：直接克隆 (Git Clone)
将此仓库直接克隆到你的 agent 的技能目录中：
```bash
cd /path/to/your/project/.trae/skills
git clone https://github.com/fanhy-TvT/literature-survey-dashboard.git
```

## 如何使用
1. 安装完成后，向你的 AI Agent 提问：“*使用 literature-survey-dashboard 技能，帮我分析 `./papers` 目录下的论文，我的研究方向是 [你的课题]。*”
2. Agent 将自主执行脚本、生成摘要，并最终为你展示 HTML 仪表盘。

## 许可证
本项目采用 [MIT 许可证](LICENSE) 进行开源。
