# 📊 RAG Complaint Intelligence System

A Retrieval-Augmented Generation (RAG) system for analyzing financial customer complaints using semantic search and LLMs.

---

## 📋 Project Overview

Financial institutions receive thousands of customer complaints every year, making it difficult for analysts and decision-makers to quickly understand recurring issues, customer pain points, and company-level trends. Traditional keyword search and manual analysis are slow, inconsistent, and not scalable.

This project implements a **Retrieval-Augmented Generation (RAG)** system that enables users to ask natural language questions about financial complaints and receive context-aware, evidence-backed answers. The system combines semantic search with a Large Language Model (LLM) to deliver accurate, explainable insights grounded in real complaint data.

---

## 🎯 Solution

We built a modular RAG pipeline that:

- 🔍 **Retrieves** the most relevant complaint text chunks using vector similarity search (FAISS)
- 📝 **Injects** retrieved context into a carefully designed prompt
- 🤖 **Generates** grounded answers using a transformer-based LLM
- 📎 **Returns** both the answer and the source evidence, increasing transparency and trust

This solution is designed for **financial analysts, compliance teams, and product managers** who need fast, reliable insights from large volumes of unstructured complaint data.

---

## ⭐ Key Features

| Feature | Description |
|---------|-------------|
| 🔎 **Semantic Search** | Search over thousands of complaint narratives using vector embeddings |
| 🧠 **RAG Pipeline** | Retrieval-Augmented Generation for accurate, contextual answers |
| ✅ **Evidence-Backed Answers** | Responses include source text for verification |
| 🧩 **Modular Architecture** | Clean, testable Python code with separation of concerns |
| 🧪 **Unit Testing** | Comprehensive tests with pytest |
| 🔄 **CI/CD** | Automated testing with GitHub Actions |
| 📦 **Reproducible** | Production-oriented design with configuration management |

---

## 🏗️ Architecture
```bash

                  User Question
                     │
                     ▼
          Query Embedding
     (Sentence Transformers)
                     │
                     ▼
          FAISS Vector Store
            (Similarity Search)
                     │
                     ▼
       Top-K Relevant Complaint Chunks
                     │
                     ▼
             Prompt Builder
        (Context + Question)
                     │
                     ▼
             LLM Generator
                (FLAN-T5)
                     │
                     ▼
          Final Answer + Sources
```


---

## 🛠️ Core Technologies

- **Python 3.10**
- **Pandas, NumPy** – data processing
- **Sentence-Transformers** – embeddings
- **FAISS** – vector similarity search
- **Hugging Face Transformers** – LLM
- **Gradio** – web UI
- **pytest** – unit testing
- **GitHub Actions** – CI/CD
- **Jupyter Notebooks** – experimentation & evaluation

---

## 📁 Project Structure

```bash
rag-complaint-intelligence-capstone/
│
├── data/
│   └── complaint_embeddings.parquet
│
├── vector_store/
│   └── faiss/
│       ├── index.faiss
│       └── metadata.pkl
│
├── notebooks/
│   └── evaluation.ipynb      # Jupyter notebook for analysis & evaluation
│
├── src/
│   ├── __init__.py
│   ├── config.py              # Configuration (models, paths, constants)
│   ├── vector_store.py        # FAISS loading logic
│   ├── retriever.py           # Similarity search
│   ├── prompt.py              # Prompt templates
│   ├── generator.py           # LLM inference
│   ├── pipeline.py            # RAG orchestration
│   ├── evaluation.py          # Qualitative evaluation utilities
│   └── utils.py               # Helper utilities
│
├── tests/
│   ├── __init__.py
│   ├── test_vector_store.py
│   ├── test_retriever.py
│   ├── test_generator.py
│   └── test_prompt.py
│   └── test_pipeline.py
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI
│
├── app.py                     # Gradio UI
├── requirements.txt
├── .gitignore
└── README.md

```



---

## 📌 Tasks Overview

### ✅ Task 1: Project Selection & Gap Analysis
**Objective:** Select capstone project and create structured improvement plan.

**Key Activities:**
- Reviewed previous RAG implementation
- Identified gaps in modularity, testing, and CI
- Defined high-impact engineering improvements

**Deliverables:**
- ✅ Gap analysis completed
- ✅ Improvement plan defined
- ✅ Project structure designed

---

### ✅ Task 2: Engineering Excellence
**Objective:** Implement robust engineering improvements.

**Key Components:**
- Code refactoring with type hints and modular design
- Unit testing with pytest (5 tests covering core components)
- GitHub Actions CI pipeline for automated testing
- Production-grade configuration management

**Modules:**
- `src/config.py` – Type-safe configuration
- `src/vector_store.py` – FAISS operations
- [src/retriever.py](cci:7://file:///d:/10acadamyWeek7%20project/rag-complaint-intelligence/src/retriever.py:0:0-0:0) – Semantic search
- `src/prompt.py` – Prompt engineering
- `src/generator.py` – LLM inference
- `src/pipeline.py` – RAG orchestration

**Deliverables:**
- ✅ Modular codebase with clear structure
- ✅ 5 comprehensive unit tests
- ✅ Working CI/CD pipeline
- ✅ Type hints and documentation

---

### ✅ Task 3: RAG Pipeline Implementation & Evaluation
**Objective:** Build and evaluate the full RAG pipeline.

**Key Components:**
- **Retriever:** Semantic similarity search (top-k retrieval)
- **Prompt Engineering:** Finance-focused, context-only answers
- **Generator:** LLM-based response generation
- **Evaluation:** Qualitative assessment with representative queries

**Deliverables:**
- ✅ End-to-end RAG pipeline
- ✅ Evaluation framework
- ✅ Quality analysis and scoring

---

## ▶️ Installation & Running the App

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/bethywa/rag-complaint-intelligence-capstone.git
cd rag-complaint-intelligence-capstone

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate     # Windows
source .venv/bin/activate  # Linux/Mac

3️⃣ Install Dependencies
    pip install -r requirements.txt

4️⃣ Run the Application
    gradio run app.py

5️⃣ Run Unit Tests
  pytest

6️⃣ Explore the evaluation notebook
    notebooks/evaluation.ipynb

```


---

## 🧪 System Evaluation (Qualitative)

The system was evaluated using **representative business questions** relevant to financial complaint analysis.

| Question | Answer Quality | Notes |
|--------|----------------|------|
| Credit card dispute complaints | ⭐⭐⭐⭐ | Grounded in retrieved evidence |
| Unauthorized charges | ⭐⭐⭐⭐ | Clear and concise |
| Chargeback issues | ⭐⭐⭐ | Some abstraction loss |
| Account closures | ⭐⭐⭐ | Needs stronger summarization |

**Key Insight:**  
Increasing `top_k` improves recall but can introduce noise — optimal balance is required.

---

## 🖥️ Interactive Gradio Application

### Features:
- Natural language question input
- AI-generated answers
- Source document display (trust & transparency)
- Clear/reset conversation
- User-friendly layout for non-technical users

### Run the App:
```bash
python app.py

Then open:
 http://127.0.0.1:7860
 
```



### ✅ Engineering Improvements 
- Compared to earlier versions, this capstone includes:
   - ✅ Fully modular Python codebase
   - ✅ Dataclass-based configuration
   - ✅ Unit tests (5 core components)
   - ✅ GitHub Actions CI pipeline
   - ✅ Improved embedding & LLM models
   - ✅ Qualitative evaluation framework
   - ✅ Production-style UI

### 🚧 Planned Improvements
- Response streaming in UI
- Dockerized deployment
- REST API endpoint
- Advanced evaluation metrics

### 📝 Important Notes
This project was developed as part of the 10 Academy KAIM Program and demonstrates best practices in:
 - 📊 Data Engineering - Vector embeddings, FAISS indexing
 - 🧠 NLP & LLM Systems - RAG architecture, prompt engineering
 - 🔧 Software Engineering - Modular design, unit testing
 - 🔄 CI/CD - GitHub Actions automation

 👤 Author
- Bethelihem Weldegebrial
### AI & Data Engineering Trainee
 ### 10 Academy – KAIM Program

