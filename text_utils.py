# text_utils.py

def chunk_text(text, chunk_size=500):
    """Splits text into chunks of a given size."""
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def retrieve_top_k(chunks, query, k=3):
    """Dummy function to simulate retrieving top-k relevant chunks."""
    # For now, just return the first k chunks
    return chunks[:k]