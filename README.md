# CodexDS--hackverse
# 📈 FinIntel: Multi-Agent Financial Intelligence & Advisory System
*Empowering retail and institutional investors with explainable, profile-adaptive, multi-agent market intelligence.*

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Netlify-00C7B7?style=for-the-badge&logo=netlify)](https://financeaiagent1.netlify.app)
[![API Docs](https://img.shields.io/badge/Swagger%20UI-FastAPI-009688?style=flat&logo=fastapi)](http://127.0.0.1:8000/docs)
[![Frontend](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat&logo=streamlit)](http://localhost:8501)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=flat&logo=sqlite)](https://www.sqlite.org/)
[![VectorDB](https://img.shields.io/badge/RAG-ChromaDB-orange?style=flat)](https://www.trychroma.com/)
[![Tests](https://img.shields.io/badge/Tests-7%2F7%20Passed-brightgreen?style=flat)]()

---

## 🌐 Quick Access Links
- **🚀 Live Web App:** [https://financeaiagent1.netlify.app](https://financeaiagent1.netlify.app)
- **💻 Source Code:** [https://github.com/yugdesai133/CodexDS--hackverse](https://github.com/yugdesai133/CodexDS--hackverse/tree/main)
- **📖 Interactive API Docs (Local):** `http://127.0.0.1:8000/docs`
- **🖥️ Streamlit Local UI:** `http://localhost:8501`

---

## 📌 1. Problem Statement & Overview
Retail investors face two primary hurdles in capital markets:
1. **Information Fragmentation:** Critical market signals are scattered across technical indicators, lengthy regulatory disclosures (SEBI/earnings reports), and institutional sentiment/derivatives flow.
2. **Generic Advisory:** Most algorithmic advisory tools output one-size-fits-all recommendations, ignoring the investor's unique risk capacity, investment horizon, and market experience.

**FinIntel** solves this by orchestrating a **parallel multi-agent reasoning architecture** that synthesizes technical momentum, regulatory vector filings (RAG), and sentiment metrics into **dynamically personalized investment strategies** with millisecond audit trails.

---

## 🌟 2. Key Features

- **🤖 Parallel Multi-Agent Synthesis:**
  - **Technical Agent:** Analyzes RSI momentum, DMA crossovers, and key price levels.
  - **Fundamental & RAG Agent:** Retrieves regulatory statements, YoY profit expansion, and CapEx metrics via ChromaDB vector embeddings.
  - **Sentiment & Options Agent:** Extracts real-time NSE data, institutional flows, and Put-Call Ratios (PCR).
- **🎯 Dynamic Profile Adaptivity:** Automatically tailors the same asset ticker into distinct actions (e.g., `ACCUMULATE_SIP` with strict capital limits for Conservative users vs. `BUY_CALL_OPTION_SWING` for Aggressive traders).
- **🔍 Explainable AI & Grounded Citations:** Every synthetic trade thesis references verified regulatory and market sources.
- **⏱️ System Telemetry & Auditing:** Persistent SQLite tracking of investor sessions, strategy fit rationale, and sub-50ms execution latency.

---

## 🏗️ 3. Architecture & Repository Structure

```text
CodexDS-Hackverse-VibeCoding/
├── app.py                      # Streamlit interactive investor dashboard
├── main_backend.py             # FastAPI REST server & multi-agent orchestrator
├── user_relational_db.py       # SQLite database schema & ORM persistence
├── test_system.py              # Automated 7-step integration test suite
├── database/
│   └── Untitled-1.py           # NSE live data retriever & ChromaDB vector store
├── requirements.txt            # System dependencies
└── README.md                   # System documentation
```
⚙️ 4. Tech StackLayerTechnologies UsedLive Frontend DeploymentNetlifyBackend API EngineFastAPI, Uvicorn, PydanticUser InterfaceStreamlit, RequestsDatabase & PersistenceSQLite, SQLAlchemy ORMVector Search & RAGChromaDB, Text EmbeddingsFinancial DataLive NSE Options Chain & Price RetrievalTest VerificationAutomated End-to-End Integration Suite🚀 5. Quickstart / Local Setup1. Clone & Install DependenciesBashgit clone [https://github.com/yugdesai133/CodexDS-Hackverse-VibeCoding.git](https://github.com/yugdesai133/CodexDS--hackverse/tree/main)
cd CodexDS-Hackverse-VibeCoding
pip install -r requirements.txt
2. Start the FastAPI Backend ServerBashpython3 -m uvicorn main_backend:app --reload --port 8000
Access the Swagger interactive API docs at http://127.0.0.1:8000/docs.
3. Launch the Streamlit Frontend Dashboard (New Terminal Tab)Bashstreamlit run app.py
Access the user interface at http://localhost:8501.
4. Run Automated System Integration TestsBashpython3 test_system.py
👥 6. Submission DetailsProject Name: FinIntelLive Demo: https://financeaiagent1.netlify.appRepository: https://github.com/yugdesai133/CodexDS-Hackverse-VibeCodingBuilt For: CodexDS Hackverse / VibeCoding Hackathon
