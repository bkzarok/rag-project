#enrich       
import spacy, json
from pathlib import Path

nlp = spacy.load("en_core_web_sm")
for jf in Path("../data/processed").glob("*.jsonl"):
    try:
        lines = [json.loads(x) for x in open(jf, encoding='utf-8')]
        for r in lines:
            try:
                doc = nlp(r["text"])
                r["entities"] = [(e.text, e.label_) for e in doc.ents]
            except Exception as e:
                print(f"NER error in {jf.name} chunk {r.get('order', '?')}: {e}")
                r["entities"] = []
        with open(jf, 'w', encoding='utf-8') as f:
            f.write("\n".join(json.dumps(r) for r in lines))
    except Exception as e:
        print(f"Error processing {jf.name}: {e}")                                        