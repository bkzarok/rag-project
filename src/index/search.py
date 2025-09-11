#search helper
import faiss, numpy as np, json
from sentence_transformers import SentenceTransformer

try:
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
except Exception as e:
    raise RuntimeError(f"Error loading embedding model: {e}")

try:
    index = faiss.read_index("../data/index/faiss.index")
except Exception as e:
    raise RuntimeError(f"Error loading FAISS index: {e}")

try:
    with open("../data/index/chunks.json", encoding="utf-8") as f:
        chunks = json.load(f)['chunks']
    with open("../data/index/meta.json", encoding="utf-8") as f:
        metas = json.load(f)['metas']
except Exception as e:
    raise RuntimeError(f"Error loading chunk/meta files: {e}")

def topk(query, k=5):
    try:
        qv = model.encode([query], normalize_embeddings=True).astype('float32')
        D, I = index.search(qv, k)
        return [{"score": float(D[0][j]), "text": chunks[i], "meta": metas[i]} for j, i in enumerate(I[0])]
    except Exception as e:
        print(f"Error during search: {e}")
        return []
