# backend/index_utils.py

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import streamlit as st

@st.cache_resource
def get_embedding_model(model_name: str = "all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)

def build_faiss_index(chunks: list[str]):
    """
    Encode chunks, build FAISS L2 index, and return (index, embeddings).
    """
    model = get_embedding_model()
    embeddings = model.encode(chunks, convert_to_numpy=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index, embeddings

def retrieve_top_k(
    query: str, index: faiss.IndexFlatL2, chunks: list[str], k: int = 5
) -> list[str]:
    """
    Embed query and return top-k matching chunks.
    """
    model = get_embedding_model()
    q_emb = model.encode([query], convert_to_numpy=True)
    distances, idxs = index.search(q_emb, k)
    return [chunks[i] for i in idxs[0]]