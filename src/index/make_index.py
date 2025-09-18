import faiss, numpy as np, json
from pathlib import Path
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
chunks, metas = [], []

for jf in Path("./data/processed").glob("*.jsonl"):
    try:
        with open(jf, encoding='utf-8') as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    chunks.append(rec['text'])
                    metas.append({k: rec[k] for k in ("chunk_id", "source", "order")})
                except Exception as e:
                    print(f"Error parsing line in {jf.name}: {e}")
    except Exception as e:
        print(f"Error opening {jf.name}: {e}")

try:
    X = model.encode(chunks, batch_size=64, normalize_embeddings=True).astype('float32')
except Exception as e:
    print(f"Error during embedding: {e}")
    X = np.zeros((len(chunks), 384), dtype='float32')  # fallback shape

try:
    index = faiss.IndexFlatIP(X.shape[1])
    index.add(X)
    Path("./data/index").mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, "./data/index/faiss.index")
    json.dump({"chunks": chunks}, open("./data/index/chunks.json", "w", encoding='utf-8'))
    json.dump({"metas": metas}, open("./data/index/meta.json", "w", encoding='utf-8'))
except Exception as e:
    print(f"Error during FAISS indexing or saving: {e}")
print("Faiss indexing complete")