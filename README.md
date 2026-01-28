# 📄 Chat with PDF – AI Prototyping Engineer Project

## Project Overview

This project is a **local, instruction-compliant AI system** that allows users to upload PDFs and ask questions based on their content. It demonstrates **LLM-powered retrieval augmented generation (RAG)**, source-grounded responses, and offline operation with **no API costs**.

Key features:

- Chat with PDFs using **local LLM** (Ollama + mistral:7b-instruct-q4_0)
- Retrieval using **FAISS vector database**
- **Embeddings** powered by HuggingFace sentence-transformers
- **Chunking strategy** for efficient document handling
- **Prompt engineering** to prevent hallucinations
- Interactive **Streamlit UI**

---

## Task Compliance

### Task 1 – LLM-Powered AI Prototype (Mandatory)

- **LLM:** Local Ollama LLM (Mistral / Llama3)
- **RAG:** Vector database (FAISS) + embeddings (HuggingFace)
- **Chunking:** `RecursiveCharacterTextSplitter` with `CHUNK_SIZE=500` and `CHUNK_OVERLAP=50`
- **Prompt Engineering:** Guardrail prompts ensure answers strictly from context
- **UI:** Streamlit-based, allows PDF upload and question input

**Architecture:**
PDF
 ↓
Chunking (RecursiveCharacterTextSplitter)
 ↓
Embeddings (sentence-transformers)
 ↓
FAISS Vector DB
 ↓
Relevant Context Retrieval
 ↓
Local LLM (Ollama – Mistral)
 ↓
Answer (Source-grounded)


---

### Task 2 – Hallucination & Quality Control

**Problem:** LLMs can generate confident but incorrect answers.  

**Guardrails Implemented:**

1. **Context-only answers:** Prompt enforces “Answer only from the context, otherwise say ‘Answer not found in the document.’”
2. **Vector-based retrieval:** Only top-K relevant chunks (`TOP_K=3`) are fed to the LLM.

**Example:**

- **Question:** Minimum CGPA criteria  
- **Answer:** The minimum eligibility criteria for MCA students to apply for the internship program is a CGPA of 7.(directly from document, no hallucination)

---

### Task 3 – Rapid Iteration Challenge

**Advanced Capability Implemented:** Multi-PDF reasoning  

**Reasoning:**

- Supports multiple PDFs at once
- Retrieval and embeddings remain consistent
- Trade-offs: Slightly higher local compute required, but zero API cost and offline operation

**Future Enhancements:**

- Memory and feedback loop
- Cost optimization strategies
- Tool calling for advanced actions

---

### Task 4 – AI System Architecture

**Components:**

| Component | Choice | Reason |
|-----------|--------|--------|
| Data Ingestion | `PyPDFLoader` + chunking | Efficient text extraction and split |
| Vector DB | `FAISS` | Fast, local, open-source |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` | Free and lightweight |
| LLM Orchestration | `OllamaLLM` with Mistral | Local inference, offline, interview-safe |
| Cost Control | Local inference, no API | Free and offline |
| Monitoring | Logging similarity search and retrieval size | Debugging and quality control |

---

### Installation & Setup

1. **Clone Repository**
```bash
git clone <YOUR_REPO_URL>
cd chat_with_pdf
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install Ollama & download model**
```bash
# Download from https://ollama.com and install
ollama pull mistral:7b-instruct-q4_0
```

5. **Run the app**
```bash
streamlit run app.py
```
