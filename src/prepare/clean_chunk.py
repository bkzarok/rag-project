#chunk
import json, uuid, re
from pathlib import Path

INP = Path("./data/interim")
OUT = Path("./data/processed")
OUT.mkdir(parents=True, exist_ok=True)
CHUNK, OVERLAP = 800, 120

for p in INP.glob("*.txt"):
    try:
        t = re.sub(r"\n{3,}", "\n\n", p.read_text(encoding='utf-8')).strip()
        i, parts = 0, []
        while i < len(t):
            parts.append(t[i:i+CHUNK])
            i += CHUNK - OVERLAP
        with open(OUT / f"{p.stem}.jsonl", 'w', encoding='utf-8') as f:
            for k, c in enumerate(parts):
                try:
                    rec = {
                        "chunk_id": str(uuid.uuid4()),
                        "source": p.stem,
                        "order": k,
                        "text": c
                    }
                    f.write(json.dumps(rec) + "\n")
                except Exception as e:
                    print(f"Error writing chunk {k} of {p.name}: {e}")
    except Exception as e:
        print(f"Error processing {p.name}: {e}")                    
                    