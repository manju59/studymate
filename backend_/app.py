# app.py

import streamlit as st
from config import Settings
from pdf_utils import extract_text_from_pdf
from index_utils import build_index
from watsonx_client import WatsonXClient
from config import Settings

config = Settings.get()
api_key = config["api_key"]
api_url = config["api_url"]

st.set_page_config(page_title="StudyMate PDF Q&A", layout="wide")
st.title("📚 StudyMate: AI-Powered PDF Q&A Assistant")

# Sidebar: PDF upload
with st.sidebar:
    st.header("Upload PDFs")
    pdf_files = st.file_uploader(
        "Choose one or more PDFs", type="pdf", accept_multiple_files=True
    )

if not pdf_files:
    st.info("Upload at least one PDF to begin.")
    st.stop()

# Extract and chunk text
all_text = ""
for f in pdf_files:
    all_text += extract_text_from_pdf(f.read()) + "\n\n"

chunks = chunk_text(all_text)

# Build FAISS index
index, _ = build_faiss_index(chunks)

# User question
query = st.text_input("Ask a question about your documents:")
if query:
    with st.spinner("Retrieving context..."):
        top_chunks = retrieve_top_k(query, index, chunks, k=5)

    st.subheader("🔍 Retrieved Context")
    for i, chunk in enumerate(top_chunks, 1):
        st.markdown(f"**Chunk {i}:** {chunk[:300]}…")

    # Generate answer
    client = WatsonXClient()
    with st.spinner("Generating answer..."):
        answer = client.generate_answer(query, top_chunks)

    st.subheader("💡 Answer")
    st.write(answer)
