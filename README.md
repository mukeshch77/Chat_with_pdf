# Chat with PDF – LLM Powered RAG System

## Overview
This project is an AI-powered application that allows users to upload PDFs and ask questions based strictly on the document content.

## Tech Stack
- OpenAI GPT
- LangChain
- FAISS Vector DB
- Streamlit

## Architecture
PDF → Chunking → Embeddings → FAISS  
User Query → Retrieval → Context → LLM → Answer

## Design Decisions
- FAISS chosen for fast local vector search
- Recursive chunking for semantic consistency
- Prompt constraints to prevent hallucination

## How to Run
1. Set OpenAI API Key
2. Install dependencies
3. Run `streamlit run app.py`

## Limitations
- Large PDFs may increase processing time
- Depends on embedding quality