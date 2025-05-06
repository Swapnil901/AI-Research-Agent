# 🤖 AI Research Assistant

A smart, GPT-4 powered research agent built with LangChain, SerpAPI, and GitHub APIs — designed to help you explore any research topic with ease. This tool combines live web search, advanced summarization, memory retrieval, and GitHub project discovery — all wrapped in a clean Streamlit UI.

## 🔍 What It Does

Enter any research topic, and the assistant will:

- 🔁 Recall relevant past topics using memory (ChromaDB)
- 🌐 Search the web using SerpAPI
- 📚 Explain the topic in simple language like a teacher
- 🧠 Summarize key points from live search results
- 💻 Find top GitHub projects related to your topic
- 📄 Let you export a full PDF report of the findings

## 🧠 Example Query

> **Topic:** AI in drug discovery and genomics

### 📚 Detailed Explanation
> AI helps researchers find new medicines and understand genetic patterns by analyzing large datasets, predicting drug behavior, and personalizing treatment based on a person’s DNA.

### 🔍 Key Summary Points
- AI finds biomarkers using genomic and clinical data
- Helps predict patient-specific drug responses
- Accelerates discovery and testing

### 💻 GitHub Projects
- **[AI-in-Life-Science](https://github.com/...):** Machine learning on genomic data for precision medicine  
- **[AI-Bioinformatics](https://github.com/...):** Tutorials and tools on AI in genomics and bioinformatics  
- *(More examples in the live app)*

---

## 🚀 Tech Stack

| Component     | Tech                                 |
|---------------|--------------------------------------|
| LLM           | OpenAI GPT-4                         |
| Framework     | LangChain (Agent + Tools + Memory)   |
| APIs          | SerpAPI (Google Search), GitHub API  |
| Memory Store  | ChromaDB                             |
| Frontend UI   | Streamlit                            |
| PDF Export    | ReportLab                            |
| Hosting (opt) | HuggingFace / Streamlit Cloud        |

---

## 🧩 Features

- ReAct-style LLM agent loop
- Streamlight web interface
- Vector memory retrieval (ChromaDB)
- Summary + beginner explanation
- GitHub repo search tool
- PDF report generation

---

## 📂 Project Structure

AI-Agent-Research-Assistant/
│
├── streamlit_app.py # Main app with all tools
├── summarizer_tool.py # LLM summarization tool
├── github_repo_tool.py # GitHub API integration
├── memory_store.py # ChromaDB memory helper
├── secrets.txt # API keys (not uploaded to GitHub)
├── requirements.txt # Required libraries


---

## 🛠️ Setup Instructions

1. **Clone this repo:**
   git clone https://github.com/YOUR_USERNAME/ai-research-assistant.git
   cd ai-research-assistant
   
2. **Create and activate a virtual environment (optional but recommended):**
  python -m venv venv
  source venv/bin/activate  # or venv\Scripts\activate on Windows

3.**Install dependencies:**
  pip install -r requirements.txt
  
4.**Create a secrets.txt file with your API keys:**
  OPENAI_API_KEY=sk-...
  SERPAPI_API_KEY=...
  GITHUB_API_KEY=ghp_...
  
5.**Run the Streamlit app:**
  streamlit run streamlit_app.py


---

📦 To-Do (For Future)
 Add email export feature

 Deploy on Streamlit Cloud

 Multi-topic history view

 Upload custom documents for Q&A


---

🙌 Author
Swapnil Nandanwar
AI & Cybersecurity Engineer
