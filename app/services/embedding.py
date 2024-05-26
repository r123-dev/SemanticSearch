from sentence_transformers import SentenceTransformer, util
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
embedding_dimension = 384  # Dimension of sentence transformer model
index = faiss.IndexFlatL2(embedding_dimension)

documents = []

def create_embedding(text):
    embedding = model.encode([text], convert_to_tensor=True)
    return embedding

def add_to_index(embedding, filename):
    index.add(embedding.cpu().detach().numpy())
    documents.append(filename)

def search_embeddings(query):
    query_embedding = model.encode([query], convert_to_tensor=True).cpu().detach().numpy()
    D, I = index.search(query_embedding, k=5)
    results = [documents[idx] for idx in I[0]]
    return results
