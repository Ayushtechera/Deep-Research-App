# 🔍 Deep Research Agent

Your AI research assistant that searches the web and generates reports instantly.

<img width="539" height="368" alt="image" src="https://github.com/user-attachments/assets/bd6fc89a-35dd-44dd-a732-851c3cfe6a77" />


## What is Deep Research Agent?

Ask a question → AI searches the web → Get a research report

That's it. Simple. Powerful.

## 🎯 Features

- **🤖 Intelligent Planning** — AI breaks down complex questions into smart search queries
- **🔍 Autonomous Search** — Automatically searches and validates information from the web
- **📄 Formatted Reports** — Generates clean, organized markdown reports with sources
- **⚡ Fast Results** — Get comprehensive research in 30-60 seconds
- **🔧 Open Source** — Build and customize your own agents

## ⚡ Quickstart
### 1️⃣ Install

```bash
git clone https://github.com/Ayushtechera/Deep-Research-App.git
cd Deep-Research-App
pip install -r requirements.txt
```

### 2️⃣ Configure

Create `.env`:
```env
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-3.5-turbo
```

### 3️⃣ Run

```bash
python app.py
```

Open http://localhost:7860 and ask your first question! 🎉

## 🏗️ How It Works

```
Question
   ↓
Planner (strategizes)
   ↓
Search (finds info)
   ↓
Writer (formats)
   ↓
Report Ready ✓
```

## 📁 Project Structure

```
Deep-Research-App/
├── app.py                 # Web UI (Gradio)
├── research_manager.py    # Coordinator
├── planner_agent.py       # Query planning
├── search_agent.py        # Web search
├── writer_agent.py        # Report generation
├── email_agent.py         # Email sending
├── messenger.py           # Agent communication
├── requirements.txt       # Dependencies
└── .env                   # Configuration
```

## 🛠️ Tech Stack

- **Python 3.12+**
- **Gradio** — Web Interface
- **OpenAI API** — AI Models
- **Pydantic** — Data Validation

## 💡 Use Cases

- Research topics quickly
- Get market analysis
- Compare technologies
- Learn new subjects
- Prepare for interviews

## 📚 Architecture

**Multi-Agent System:**
- Each agent has a specific role
- Agents communicate through a message broker
- Orchestrated by ResearchManager
- Modular and extensible

**Example Query Flow:**
1. User asks: "Latest AI trends?"
2. Planner analyzes and creates search strategy
3. Search agent executes multiple queries
4. Writer synthesizes findings
5. Report generated with citations

## 📝 Contributing
Contributions welcome! Submit issues, features, or PRs.

---
[GitHub](https://github.com/Ayushtechera/Deep-Research-App)
