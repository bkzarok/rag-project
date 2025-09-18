
import pathlib
from pdfminer.high_level import extract_text as pdf_text
from readability import Document
from bs4 import BeautifulSoup

INP = pathlib.Path("./data/raw")
OUT = pathlib.Path("./data/interim")
OUT.mkdir(parents=True, exist_ok=True)

for p in INP.iterdir():
    if p.suffix.lower() == ".pdf":
        try:
            txt = pdf_text(open(p, 'rb'))
        except Exception as e:
            print(f"Skipping {p.name}: not a valid PDF ({e})")
            continue
    else:
        html = p.read_text(encoding='utf-8', errors='ignore')
        main = Document(html).summary()
        txt = BeautifulSoup(main, 'html.parser').get_text("")
    (OUT / f"{p.stem}.txt").write_text(txt, encoding='utf-8')