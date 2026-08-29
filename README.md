# 🔍 Deep Research App

<img width="539" height="368" alt="image" src="https://github.com/user-attachments/assets/a5d61f7f-72fc-4c21-8b6f-9d32c4c88fa2" />


> AI agent jo web search karta hai aur research report banata hai

---

## 🎯 Kya Karta Hai?

User ek **question** deta hai → App web search karta hai → **Report** generate karta hai

**Example:**
- Input: "Latest AI trends 2026?"
- Output: 📄 Markdown report with findings

---

## 🏗️ Kaise Kaam Karta Hai? (Architecture)

```
User Input
   ↓
Planner Agent (question ko break karta hai)
   ↓
Search Agent (Google jaise search karta hai)
   ↓
Writer Agent (report likha deta hai)
   ↓
User ko Report milta hai ✓
```

---

## 📁 Files Kya Hain?

| File | Kya Karta Hai |
|------|--------------|
| `app.py` | Web interface (UI) |
| `research_manager.py` | Coordinator (sab control karta hai) |
| `planner_agent.py` | Plan banata hai |
| `search_agent.py` | Search karta hai |
| `writer_agent.py` | Report likha deta hai |
| `email_agent.py` | Email bhejta hai |

---

## 🚀 Install Kaise Kare? (3 Steps)

```bash
# Step 1: Clone
git clone https://github.com/Ayushtechera/Deep-Research-App.git
cd Deep-Research-App

# Step 2: Install
pip install -r requirements.txt

# Step 3: .env file banao
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Step 4: Run
python app.py
# Open: http://localhost:7860
```

---

## 💡 Tech Stack

- **Python 3.12+**
- **Gradio** - Web UI
- **OpenAI API** - AI model
- **Pydantic** - Data validation

---

## 📊 Multi-Agent System Kya Hai?

Independent agents jo communicate karte hain:

```
┌─────────────┐
│   Planner   │ ← Query analyze karta hai
└─────────────┘
       ↓
┌─────────────┐
│   Search    │ ← Web search karta hai
└─────────────┘
       ↓
┌─────────────┐
│   Writer    │ ← Report likha deta hai
└─────────────┘
```

**Har agent ek specific kaam karta hai** ✅

---

## 🎓 B.Tech Student Ke Liye

### Seekhne Ko Milega:
- Multi-agent systems
- API integration
- Web framework
- Design patterns
- Full-stack development

### Interview Questions:
**Q: Multi-agent kya hai?**  
A: Alag alag agents jo task-specific kaam karte hain aur communicate karte hain.

**Q: Ye project mein kaise use ho raha hai?**  
A: Planner, Search, Writer 3 agents alag kaam karte hain.

---

## 📈 Project Structure

```
Deep-Research-App/
├── app.py                 ← Main UI
├── research_manager.py    ← Coordinator
├── planner_agent.py       ← Strategy
├── search_agent.py        ← Search
├── writer_agent.py        ← Report
├── email_agent.py         ← Email
├── messenger.py           ← Communication
├── requirements.txt       ← Dependencies
└── .env                   ← API keys
```

---

## ⚡ Quick Commands

```bash
# Install
pip install -r requirements.txt

# Run
python app.py

# Check API
python -c "from openai import OpenAI; print('✓ Working')"
```

---

## 🆘 Common Issues

| Error | Fix |
|-------|-----|
| `No module openai` | `pip install -r requirements.txt` |
| `API key not found` | `.env` file banao |
| `Port 7860 in use` | `python app.py --server_port 7861` |

---

## 🌐 Deploy Kaise Kare?

### Hugging Face Spaces Par:
1. GitHub par push karo
2. HF Spaces create karo (Python + Gradio)
3. Code push karo
4. Live! 🎉

---

## 📝 Code Example

```python
# Research chalao
from research_manager import ResearchManager

manager = ResearchManager(api_key="your_key")
report = manager.research("Your question")
print(report)
```

---

## 💰 Cost

- **gpt-4**: $0.10-0.30 per query
- **gpt-3.5-turbo**: $0.01-0.03 per query

Use gpt-3.5-turbo for testing (sasta hai)

---

## 🎯 Next Steps

1. ✅ Install karo
2. ✅ Run karo
3. ✅ Try different queries
4. ✅ Modify agents
5. ✅ Deploy karo

---

## 📚 Resources

- [OpenAI Docs](https://platform.openai.com/docs)
- [Gradio Tutorial](https://www.gradio.app/)
- [GitHub](https://github.com/Ayushtechera/Deep-Research-App)

---

## 👨‍💼 Author

**Ayush** - 4th Year B.Tech  
GitHub: [@Ayushtechera](https://github.com/Ayushtechera)

---

**Bas! Itna hi enough hai understanding ke liye! 🚀**

Agar detailed documentation chahiye toh README_FULL.md padho
