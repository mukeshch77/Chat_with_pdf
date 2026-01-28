import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from config import PDF_DIR, VECTOR_DB_PATH, CHUNK_SIZE, CHUNK_OVERLAP

load_dotenv()


def ingest_pdfs():
    documents = []

    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(PDF_DIR, file))
            documents.extend(loader.load())

    if not documents:
        return None

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(documents)

    # ✅ FREE LOCAL EMBEDDINGS
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(chunks, embeddings)

    os.makedirs(VECTOR_DB_PATH, exist_ok=True)
    vector_db.save_local(VECTOR_DB_PATH)

    return vector_db