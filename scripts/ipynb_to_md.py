"""Chuyển notebook Colab (.ipynb) trong /notebooks thành bài blog Markdown.
Chạy: python scripts/ipynb_to_md.py
Không cần thư viện ngoài. Tiêu đề lấy từ dòng '# ...' đầu tiên của notebook.
"""
import json, pathlib, re, datetime

SRC = pathlib.Path("notebooks")
OUT = pathlib.Path("src/content/blog")

def slugify(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "notebook"

for nb_path in SRC.glob("*.ipynb"):
    try:
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"Bỏ qua {nb_path.name}: file JSON hỏng"); continue

    body, title = [], nb_path.stem
    for cell in nb.get("cells", []):
        text = "".join(cell.get("source", []))
        if cell["cell_type"] == "markdown":
            m = re.match(r"#\s+(.+)", text)
            if m and title == nb_path.stem:
                title = m.group(1).strip(); text = text[m.end():].lstrip()
            body.append(text)
        elif cell["cell_type"] == "code" and text.strip():
            body.append(f"```python\n{text}\n```")

    title = title.replace('"', "'")
    date = datetime.date.today().isoformat()
    front = (f'---\ntitle: "{title}"\ndescription: "Notebook từ Colab: {title}"\n'
             f'date: {date}\ntags: ["colab"]\n---\n\n')
    (OUT / f"{slugify(nb_path.stem)}.md").write_text(front + "\n\n".join(body), encoding="utf-8")
    print(f"OK: {nb_path.name}")
