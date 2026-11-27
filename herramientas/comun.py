"""Common pieces of the NesiPocket encyclopedia pipeline.

Each pack is a folder of Markdown files (md/<pack>/NNNN.md), several articles per file, each one with a small
YAML front matter. The Markdown is the source of truth; compilar.py turns it into a SQLite FTS5 index for the iPhone.
"""
import html
import os
import re

RAIZ = os.environ.get("ENCICLOPEDIA", "/Volumes/Disk1TB/nesi-pocket/enciclopedia")
FUENTES = os.path.join(RAIZ, "fuentes")
# The public repo github.com/Neorichi/alejandria is cloned here; its md/ folder is the source of truth.
REPO = os.path.join(RAIZ, "alejandria")
MD = os.path.join(REPO, "md")
GITHUB = "Neorichi/alejandria"


class Escritor:
    """Writes articles into md/<pack>/0000.md, 0001.md… (about 4 MB each)."""

    def __init__(self, pack, max_bytes=4_000_000):
        self.dir = os.path.join(MD, pack)
        os.makedirs(self.dir, exist_ok=True)
        for f in os.listdir(self.dir):
            if f.endswith(".md"):
                os.remove(os.path.join(self.dir, f))
        self.max = max_bytes
        self.n = 0
        self.count = 0
        self.f = None
        self.size = 0

    def add(self, id, titulo, cuerpo, fuente, licencia, url="", extra=None):
        cuerpo = cuerpo.strip()
        if not cuerpo:
            return
        if self.f is None or self.size > self.max:
            if self.f:
                self.f.close()
            self.f = open(os.path.join(self.dir, f"{self.n:04d}.md"), "w", encoding="utf-8")
            self.n += 1
            self.size = 0
        meta = {"id": id, "titulo": titulo, "fuente": fuente, "licencia": licencia}
        if url:
            meta["url"] = url
        for k, v in (extra or {}).items():
            if v:
                meta[k] = v
        head = "".join(f"{k}: {one_line(str(v))}\n" for k, v in meta.items())
        text = f"---\n{head}---\n\n# {one_line(titulo)}\n\n{cuerpo}\n\n"
        self.f.write(text)
        self.size += len(text.encode("utf-8"))
        self.count += 1

    def close(self):
        if self.f:
            self.f.close()
        return self.count


def one_line(s):
    return re.sub(r"\s+", " ", s).strip()


def html_a_md(s):
    """Small HTML → Markdown for summaries (p, br, li, h1-h4, b/strong, i/em, a)."""
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", s)
    s = re.sub(r"(?i)<h[1-4][^>]*>(.*?)</h[1-4]>", lambda m: "\n\n### " + m.group(1) + "\n\n", s)
    s = re.sub(r"(?i)<li[^>]*>", "\n- ", s)
    s = re.sub(r"(?i)</(p|div|ul|ol|li|tr)>", "\n", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)<(b|strong)>(.*?)</\1>", r"**\2**", s)
    s = re.sub(r"(?i)<(i|em)>(.*?)</\1>", r"*\2*", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n\s*\n\s*\n+", "\n\n", s)
    return "\n".join(l.strip() for l in s.splitlines()).strip()


def leer_md(path):
    """Yields (meta dict, body) for each article of a pack Markdown file."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for part in re.split(r"(?m)^---\n(?=id: )", text):
        if not part.strip():
            continue
        head, _, body = part.partition("\n---\n")
        meta = {}
        for line in head.splitlines():
            k, _, v = line.partition(": ")
            if k:
                meta[k] = v
        body = body.strip()
        # The "# Title" line is for people reading the Markdown; the index keeps the title apart.
        if body.startswith("# "):
            body = body.split("\n", 1)[1].strip() if "\n" in body else ""
        yield meta, body
