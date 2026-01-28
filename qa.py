from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

from config import VECTOR_DB_PATH, TOP_K


def get_answer(query):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vector_db.similarity_search(query, k=TOP_K)

    if not docs:
        return "Answer not found in the document."

    context = "\n\n".join(d.page_content for d in docs)

    prompt = PromptTemplate(
        template="""
You are an AI assistant answering strictly from the provided context.
If the answer is not in the context, say:
"Answer not found in the document."

Context:
{context}

Question:
{question}

Answer:
""",
        input_variables=["context", "question"]
    )

    llm = OllamaLLM(model="mistral:7b-instruct-q4_0")

    response = llm.invoke(
        prompt.format(context=context, question=query)
    )

    return response