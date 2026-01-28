import os
import streamlit as st

from ingest import ingest_pdfs
from qa import get_answer
from config import PDF_DIR

st.set_page_config(page_title="Chat with PDF", layout="wide")

st.title("📄 Chat with your PDF")
st.write("Upload a PDF and ask questions based on its content.")

# Create PDF directory if not exists
os.makedirs(PDF_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    file_path = os.path.join(PDF_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully!")

    with st.spinner("Processing PDF..."):
        ingest_pdfs()

question = st.text_input("Ask a question from the PDF")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            answer = get_answer(question)
            st.markdown("### Answer")
            st.write(answer)