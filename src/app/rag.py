#LLM call 

from openai import OpenAI, APIError
import os
from  prompt import build_prompt
from search import topk

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("The OPENAI_API_KEY environment variable is not set.")
client = OpenAI(api_key=api_key)

def answer(q, k=5):
    try:
        hits = topk(q, k)
        prompt = build_prompt(q, hits)
        resp = client.chat.completions.create(
            model="gpt-4o-mini", temperature=0.2,
            messages=[
                {"role": "system", "content": "You are a careful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return resp.choices[0].message.content, hits
    except APIError as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, there was an API error.", []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "Sorry, an unexpected error occurred.", []

if __name__ == "__main__":
    while True:
        try:
            q = input("Enter your question (or 'exit' to quit): ")
            if q.strip().lower() == "exit":
                break
            answer_text, hits = answer(q)
            print("\nAnswer:\n", answer_text)
            print("\nSources:")
            for i, h in enumerate(hits, 1):
                print(f"[{i}] {h['meta']['source']}#chunk{h['meta']['order']}")
            print("-" * 40)
        except KeyboardInterrupt:
            print("\nExiting.")
            break