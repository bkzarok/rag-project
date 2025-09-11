# Prompt builder
SYSTEM = (
    "Answer using ONLY the provided context. Cite sources inline like [1], [2]. "
    "If not in context, say you cannot find it."
)

def build_prompt(q, hits):
        ctx = []
        for i, h in enumerate(hits, 1):
                try:
                        src = f"{h['meta']['source']}#chunk{h['meta']['order']}"
                        text = h.get('text', '')
                        ctx.append(f"[{i}] {src}:\n{text}")
                except Exception as e:
                        print(f"Error building context for hit {i}: {e}")
                        continue
        try:
                prompt = SYSTEM + "\n\n" + "\n\n".join(ctx) + f"\n\nQuestion: {q}\nAnswer with citations."
                return prompt
        except Exception as e:
                print(f"Error building prompt: {e}")
                return SYSTEM + f"\n\nQuestion: {q}\nAnswer with citations."