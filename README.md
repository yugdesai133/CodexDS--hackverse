# CodexDS--hackverse
# 📈 FinIntel: Multi-Agent Financial Intelligence & Advisory System
*Empowering retail and institutional investors with explainable, profile-adaptive, multi-agent market intelligence.*

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?style=flat&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=flat&logo=streamlit)](https://streamlit.io/)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?style=flat&logo=sqlite)](https://www.sqlite.org/)
[![VectorDB](https://img.shields.io/badge/RAG-ChromaDB-orange?style=flat)](https://www.trychroma.com/)
[![Tests](https://img.shields.io/badge/Tests-7%2F7%20Passed-brightgreen?style=flat)]()

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
- **🎯 Dynamic Profile Adaptivity:** Automatically tailors the same asset ticker into different actions (e.g., `ACCUMULATE_SIP` with strict capital limits for Conservative users vs. `BUY_CALL_OPTION_SWING` for Aggressive traders).
- **🔍 Explainable AI & Grounded Citations:** Every synthetic trade thesis references verified regulatory and market sources.
- **⏱️ System Telemetry & Auditing:** Persistent SQLite tracking of investor sessions, strategy fit rationale, and sub-50ms execution latency.

---

## 🏗️ 3. System Architecture & Folder Structure

```text
CodexDS-Hackverse-VibeCoding/
├── backend/
│   ├── main_backend.py         # FastAPI REST server & orchestration engine
│   └── test_system.py          # 7-step automated end-to-end test suite
├── frontend/
│   └── app.py                  # Streamlit interactive investor dashboard
├── database/
│   ├── Untitled-1.py           # NSE live market retriever & ChromaDB vector store
│   └── user_relational_db.py   # SQLite schema initialization and ORM utilities
├── requirements.txt            # System dependencies
└── README.md                   # Project documentation

⚙️ 4. Tech StackLayerTechnologies UsedLive Frontend DeploymentNetlifyBackend FrameworkFastAPI, Uvicorn, PydanticFrontend UIStreamlit, RequestsPersistence & Relational DBSQLite, SQLAlchemy ORMVector Engine & RAGChromaDB, Text EmbeddingsMarket DataLive NSE Options Chain & Price RetrievalTestingCustom 7-Step Integration Verification Suite🚀 5. Getting Started / Local SetupPrerequisitesPython 3.9+GitInstallationClone the repository:Bashgit clone [https://github.com/yugdesai133/CodexDS-Hackverse-VibeCoding.git](https://github.com/yugdesai133/CodexDS-Hackverse-VibeCoding.git)
cd CodexDS-Hackverse-VibeCoding
Install dependencies:Bashpip install -r requirements.txt
Start the FastAPI Backend:Bashpython3 -m uvicorn backend.main_backend:app --reload --port 8000
The API will be available at http://127.0.0.1:8000 (Docs at http://127.0.0.1:8000/docs).Launch the Streamlit Frontend (In a separate terminal tab):Bashstreamlit run frontend/app.py
Access the web dashboard at http://localhost:8501.🧪 6. Automated Testing & VerificationThe repository includes a comprehensive 7-stage end-to-end integration test (test_system.py) that validates the entire stack:Bashpython3 backend/test_system.py
Test Verification Matrix:[TEST 1] Backend Health & Route Reachability[TEST 2] User Registration & Risk Mapping (Conservative Profile)[TEST 3] User Registration & Profile Synthesis (Aggressive Profile)[TEST 4] Relational DB Persistence & Retrieval[TEST 5] Parallel Agent Synthesis & RAG Citations[TEST 6] Risk Adaptivity Differentiation (Target Asset Consistency)[TEST 7] Telemetry Logging & Millisecond Latency Audits👥 7. Team & Submission DetailsProject Name: FinIntelLive Demo: https://financeaiagent1.netlify.appRepository: https://github.com/yugdesai133/CodexDS-Hackverse-VibeCodingBuilt For: CodexDS Hackverse / VibeCoding Hackathon
