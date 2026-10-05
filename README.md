# My First Agent

这是我用 iPhone 独立开发的第一个 Agent 项目。由于没有电脑，我全程使用手机端 Python IDE 起步，并在 GitHub 上完成代码托管。

## 💻 开发环境
- 硬件：iPhone（无电脑环境）
- 本地 IDE：Python编译器IDE
- 大模型：DeepSeek API

## 🛠️ 技术栈
- Python 3.x
- OpenAI Python SDK
- DeepSeek API

## 🚀 核心功能
1. **多轮对话记忆**：使用 messages 列表维护对话上下文。
2. **工具调用（Function Calling）**：定义本地工具函数，大模型自主判断并调用，实现天气查询。
3. **RAG（检索增强生成）**：基于本地知识库的检索，拼接提示词后再生成回答。

## 📝 项目说明
本项目完成了 Agent 开发的基础核心闭环：API连接、上下文记忆、工具调用与RAG检索。
