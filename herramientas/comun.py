"""Common pieces of the NesiPocket encyclopedia pipeline.

The encyclopedia is an OKF v0.2 bundle (Open Knowledge Format: github.com/GoogleCloudPlatform/knowledge-catalog,
okf/SPEC.md): one Markdown file per concept, with a YAML frontmatter (`type` required; title, description,
resource, tags, sources, generated, status, stale_after) and links between concepts as plain Markdown links.
The bundle root is md/ in the alejandria repo; an index.md in every folder lists what is inside.
The Markdown is the source of truth; compilar.py turns it into a SQLite FTS5 index for the iPhone.
Packs with millions of concepts (the Wikipedia) are not loose files in git but the same bundle in a .tar.gz.
"""
import datetime
import hashlib
import html
import io
import json
import os
import re
import shutil
import tarfile
import unicodedata
from collections import defaultdict

RAIZ = os.environ.get("ENCICLOPEDIA", "/Volumes/Disk1TB/nesi-pocket/enciclopedia")
FUENTES = os.path.join(RAIZ, "fuentes")
# The public repo github.com/Neorichi/alejandria is cloned here; md/ is the OKF bundle.
REPO = os.path.join(RAIZ, "alejandria")
MD = os.path.join(REPO, "md")
GITHUB = "Neorichi/alejandria"
# Compiled packs and bundle archives (too big for git: they go to a GitHub release).
PAQ = os.path.join(RAIZ, "paquetes")
# Packs too big even for a release (the whole Wikipedia) are kept here.
FUERA = os.path.join(RAIZ, "fuera-del-repo")
OKF_VERSION = "0.2"

AHORA = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
GENERADOR = "alejandria/" + AHORA.strftime("%Y.%m.%d")  # OKF actor: <producer>/<version>


def iso(d):
    return d.strftime("%Y-%m-%dT%H:%M:%SZ")


def one_line(s):
    return re.sub(r"\s+", " ", s or "").strip()


def slug(s, maxlen=80):
    """ASCII lowercase file name: case-insensitive disks (macOS) never see two files differing only in case."""
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:maxlen].strip("-")
    return s


def describir(cuerpo, maxlen=220):
    """OKF description: the first sentence of the first paragraph of prose (lists, headings and data out)."""
    for par in re.split(r"\n\s*\n", cuerpo):
        p = par.strip()
        if not p or p.startswith(("-", "#", "|", ">", "1.")) or re.fullmatch(r"\*\*[^*]+\*\*[^.]{0,60}\.?", p):
            continue  # lists, headings, tables and one-line bold headers ("**Técnica de MITRE ATT&CK** T1059.")
        p = one_line(re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", p)).replace("**", "").replace("*", "")
        end = None
        for m in re.finditer(r"[.!?](?=\s+[A-ZÁÉÍÓÚÑ¿¡\"«(])", p):
            word = re.findall(r"(\S+)$", p[: m.start()])
            if m.start() >= 40 and not (word and len(word[0]) <= 3 and word[0][-1:].islower()):
                end = m.start() + 1
                break
        p = p[:end] if end else p
        if len(p) > maxlen:
            p = p[:maxlen].rsplit(" ", 1)[0] + " …"
        return p
    return ""


# ---------- YAML frontmatter (a small subset, written as YAML that is also readable by any YAML parser) ----------

_PLAIN = re.compile(r"[A-Za-z0-9ÁÉÍÓÚÑÜáéíóúñü][\w .,/()+&ÁÉÍÓÚÑÜáéíóúñü-]*")
_RESERVED = {"true", "false", "yes", "no", "on", "off", "null", "y", "n"}


def _scalar(v):
    if isinstance(v, (dict, list)):
        return json.dumps(v, ensure_ascii=False)  # JSON is valid YAML flow style
    s = one_line(str(v))
    if re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", s) or re.fullmatch(r"https?://\S+", s) and "#" not in s:
        return s
    if _PLAIN.fullmatch(s) and s.lower() not in _RESERVED and not re.fullmatch(r"[\d.]+", s) and not s.endswith(" "):
        return s
    return json.dumps(s, ensure_ascii=False)


def frontmatter(meta):
    out = ["---"]
    for k, v in meta.items():
        if v is None or v == "" or v == [] or v == {}:
            continue
        if k == "sources":
            out.append("sources:")
            out += ["  - " + json.dumps(e, ensure_ascii=False) for e in v]
        elif isinstance(v, list):
            out.append(f"{k}: [" + ", ".join(_scalar(x) for x in v) + "]")
        else:
            out.append(f"{k}: {_scalar(v)}")
    return "\n".join(out) + "\n---\n"


def _value(v):
    v = v.strip()
    if v[:1] in "\"[{":
        try:
            return json.loads(v)
        except ValueError:
            return v
    return v


def leer_concepto(text):
    """(meta, body) of an OKF concept written by frontmatter(), or None if it has no frontmatter."""
    if not text.startswith("---\n"):
        return None
    head, sep, body = text[4:].partition("\n---\n")
    if not sep:
        return None
    meta, last = {}, None
    for line in head.split("\n"):
        if line.startswith("  - ") and last:
            meta[last].append(_value(line[4:]))
            continue
        k, _, v = line.partition(":")
        if not k or k.startswith(" "):
            continue
        last = k.strip()
        meta[last] = [] if not v.strip() else _value(v)
    body = body.strip()
    # The "# Title" line is for people reading the Markdown; the index keeps the title apart.
    if body.startswith("# "):
        body = body.split("\n", 1)[1].strip() if "\n" in body else ""
    return meta, body


def sin_enlaces(body):
    """Body for the search index: links between concepts → their text (the iPhone has no files to follow)."""
    return re.sub(r"\[([^\]]+)\]\((?!https?:)[^)]*\)", r"\1", body)


def _sin_fecha(text):
    return re.sub(r"(?m)^(generated|stale_after): .*\n", "", text)


class Escritor:
    """Writes OKF concepts under md/<pack>/ (or into a .tar.gz with the same paths), one file per concept, and
    an index.md per folder at close(). A concept whose content did not change keeps its generated.at, so
    rebuilding does not touch it in git."""

    def __init__(self, pack, titulo, archivo=None, base=None):
        self.pack, self.titulo = pack, titulo
        self.root = base or MD
        self.dir = os.path.join(self.root, pack)
        self.prev = {}
        self.tar = None
        if archivo:
            os.makedirs(os.path.dirname(archivo), exist_ok=True)
            self.archivo = archivo
            self.tar = tarfile.open(archivo + ".tmp", "w:gz", compresslevel=6)
        else:
            if os.path.isdir(self.dir):
                for d, _, fs in os.walk(self.dir):
                    for f in fs:
                        if f.endswith(".md") and f not in ("index.md", "log.md"):
                            p = os.path.join(d, f)
                            with open(p, encoding="utf-8") as fh:
                                t = fh.read()
                            m = re.search(r"(?m)^generated: (.*)$", t)
                            st = re.search(r"(?m)^stale_after: (.*)$", t)
                            self.prev[os.path.relpath(p, self.dir)[:-3]] = (
                                hashlib.sha1(_sin_fecha(t).encode()).hexdigest(),
                                m.group(1) if m else None, st.group(1) if st else None)
                shutil.rmtree(self.dir)
            os.makedirs(self.dir, exist_ok=True)
        self.used = set()
        self.index = defaultdict(list)  # folder → [(file, title, description)]
        self.count = 0

    def add(self, ruta, id, tipo, titulo, cuerpo, fuente, licencia, url="", tags=(), descripcion=None,
            stale_dias=None, extra=None):
        """ruta: path inside the pack without .md (e.g. "kev/2024/CVE-2024-1234"). fuente: an OKF sources entry
        (resource, title, author, last_modified)."""
        cuerpo = cuerpo.strip()
        if not cuerpo:
            return None
        base, n = ruta, 1
        while ruta.lower() in self.used or os.path.basename(ruta) in ("index", "log", ""):
            n += 1
            ruta = f"{base}-{n}"
        self.used.add(ruta.lower())
        desc = descripcion if descripcion is not None else describir(cuerpo)
        meta = {"type": tipo, "title": titulo, "description": desc, "resource": url, "tags": list(tags),
                "sources": [fuente], "license": licencia, "id": id}
        for k, v in (extra or {}).items():
            meta[k] = v
        meta["generated"] = {"by": GENERADOR, "at": iso(AHORA)}
        meta["status"] = "stable"
        if stale_dias:
            meta["stale_after"] = iso(AHORA + datetime.timedelta(days=stale_dias))
        text = frontmatter(meta) + f"\n# {one_line(titulo)}\n\n{cuerpo}\n"
        old = self.prev.get(ruta)
        if old and old[0] == hashlib.sha1(_sin_fecha(text).encode()).hexdigest() and old[1]:
            text = re.sub(r"(?m)^generated: .*$", lambda _: "generated: " + old[1], text, count=1)
            if old[2]:
                text = re.sub(r"(?m)^stale_after: .*$", lambda _: "stale_after: " + old[2], text, count=1)
        self._write(ruta + ".md", text)
        folder, file = os.path.split(ruta)
        self.index[folder].append((file + ".md", one_line(titulo), desc[:160]))
        self.count += 1
        return f"/{self.pack}/{ruta}.md"

    def _write(self, rel, text):
        if self.tar:
            data = text.encode("utf-8")
            info = tarfile.TarInfo(f"{self.pack}/{rel}")
            info.size, info.mtime, info.mode = len(data), int(AHORA.timestamp()), 0o644
            self.tar.addfile(info, io.BytesIO(data))
        else:
            p = os.path.join(self.dir, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as f:
                f.write(text)

    def close(self):
        """index.md for every folder of the pack: subfolders first, then its concepts (OKF §8)."""
        folders = set(self.index)
        for f in list(folders):
            while f:
                f = os.path.dirname(f)
                folders.add(f)
        def total(folder):
            return sum(len(v) for k, v in self.index.items() if k == folder or k.startswith(folder + "/") or not folder)
        for folder in sorted(folders):
            name = self.titulo if not folder else f"{self.titulo} · {folder}"
            lines = [f"# {name}", ""]
            subs = sorted({k[len(folder):].lstrip("/").split("/")[0] for k in folders
                           if k != folder and (not folder or k.startswith(folder + "/"))})
            if subs:
                lines += [f"* [{s}]({s}/) - {total(os.path.join(folder, s)):,} conceptos".replace(",", ".") for s in subs]
                lines.append("")
            items = sorted(self.index.get(folder, []), key=lambda x: x[1].lower())
            lines += [f"* [{t.replace('[', '(').replace(']', ')')}]({f})" + (f" - {d}" if d else "") for f, t, d in items]
            self._write(os.path.join(folder, "index.md"), "\n".join(lines).strip() + "\n")
        if self.tar:
            self.tar.close()
            os.replace(self.archivo + ".tmp", self.archivo)
        return self.count


def html_a_md(s, enlaces=None):
    """Small HTML → Markdown for summaries (p, br, li, h1-h4, b/strong, i/em). Links whose URL is in `enlaces`
    (url → concept path) become OKF links; the others keep only their text."""
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", "", s)
    if enlaces:
        def link(m):
            path = enlaces.get(m.group(1).split("#")[0])
            return f"[{m.group(2)}]({path})" if path else m.group(2)
        s = re.sub(r'(?is)<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', link, s)
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
    """Yields (meta dict, body) for each article of an old pack file (several articles per file, before OKF)."""
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
        if body.startswith("# "):
            body = body.split("\n", 1)[1].strip() if "\n" in body else ""
        yield meta, body


# ---------- Wikipedia concepts (used by wikipedia.py and by the one-off migration) ----------

WIKI_LIC = "CC BY-SA 4.0"
WIKI_FUENTE = {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es",
               "last_modified": "2026-11-01T00:00:00Z"}


def wiki_url(title):
    return "https://es.wikipedia.org/wiki/" + title.replace(" ", "_")


def wiki_add(w, title, body, tags, nivel=1):
    """Adds a Wikipedia article as an OKF concept. nivel: letters of the slug used as folder (1 → a/, 2 → ab/)."""
    s = slug(title) or "x-" + hashlib.sha1(title.encode()).hexdigest()[:8]
    folder = s[:nivel] if s[0].isalpha() else "0-9"
    url = wiki_url(title)
    w.add(f"{folder}/{s}", "eswiki-" + re.sub(r"\s+", "_", title), "Artículo de enciclopedia", title, body,
          dict(WIKI_FUENTE, resource=url), WIKI_LIC, url, tags, stale_dias=365)
