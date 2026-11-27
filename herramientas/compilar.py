"""OKF bundle (md/<pack>/**, or paquetes/<pack>.okf.tar.gz) → paquetes/<pack>.sqlite (SQLite FTS5) + manifest.json,
index.md files and log.md (in the alejandria repo).

The iPhone downloads the .sqlite: articles plus a full-text index (BM25), without accents in the index so
"medico" finds "médico". Version = build date; the app compares it with the one it has.

Uso: compilar.py PACK [PACK…]          compile these packs (sin argumentos: todos los de md/)
     compilar.py [PACK…] --okf PACK…   the packs after --okf: only their OKF archive goes in this version (no recompiling)
"""
import datetime
import hashlib
import json
import os
import sqlite3
import sys
import tarfile
import zlib

from comun import FUERA, GITHUB, MD, OKF_VERSION, PAQ, REPO, leer_concepto, leer_md, sin_enlaces

PACKS = {
    "seguridad": ("Seguridad informática",
                  "Vulnerabilidades explotadas (CISA KEV), técnicas y grupos de ataque (MITRE ATT&CK) y tipos de fallo (CWE)."),
    "medicina": ("Medicina y salud",
                 "Temas de salud de MedlinePlus en español y artículos de medicina de Wikipedia. No sustituye a un médico."),
    "wikipedia-resumida": ("Wikipedia (resumen)",
                           "El principio de cada artículo de la Wikipedia en español: historia, ciencia, geografía, personas…"),
    "wikipedia": ("Wikipedia completa", "Todos los artículos de la Wikipedia en español, enteros."),
}
RESERVED = ("index.md", "log.md")
RELEASE = f"https://github.com/{GITHUB}/releases/download"


def deflate(text):
    c = zlib.compressobj(9, zlib.DEFLATED, -15)  # raw deflate: what Apple's COMPRESSION_ZLIB reads
    return c.compress(text.encode("utf-8")) + c.flush()


def archivo(pack):
    for a in (os.path.join(PAQ, f"{pack}.okf.tar.gz"), os.path.join(FUERA, f"{pack}.okf.tar.gz")):
        if os.path.exists(a):
            return a
    return None


def conceptos(pack):
    """Yields (title, source, license, url, body) of every concept of a pack: from md/<pack> if it has concepts,
    else from its OKF archive, else from the old pre-OKF files (fuera-del-repo/md)."""
    d = os.path.join(MD, pack)
    files = sorted(os.path.join(r, f) for r, _, fs in os.walk(d) for f in fs
                   if f.endswith(".md") and f not in RESERVED) if os.path.isdir(d) else []
    if files:
        for path in files:
            with open(path, encoding="utf-8") as f:
                c = leer_concepto(f.read())
            if c:
                yield fila(*c)
        return
    a = archivo(pack)
    if a:
        with tarfile.open(a, "r|gz") as t:
            while (m := t.next()) is not None:
                if m.isfile() and m.name.endswith(".md") and os.path.basename(m.name) not in RESERVED:
                    c = leer_concepto(t.extractfile(m).read().decode("utf-8"))
                    if c:
                        yield fila(*c)
                t.members = []  # streaming: do not keep two million headers in memory
        return
    old = os.path.join(FUERA, "md", pack)
    for path in sorted(os.path.join(r, f) for r, _, fs in os.walk(old) for f in fs if f.endswith(".md")):
        for meta, body in leer_md(path):
            yield meta.get("titulo", ""), meta.get("fuente", ""), meta.get("licencia", ""), meta.get("url", ""), body


def fila(meta, body):
    src = (meta.get("sources") or [{}])[0]
    src = src if isinstance(src, dict) else {}
    return (str(meta.get("title", "")), src.get("title", ""), str(meta.get("license", "")),
            str(meta.get("resource", "")), sin_enlaces(body))


def compilar(pack, version):
    os.makedirs(PAQ, exist_ok=True)
    out = os.path.join(PAQ, f"{pack}.sqlite")
    tmp = out + ".tmp"
    if os.path.exists(tmp):
        os.remove(tmp)
    db = sqlite3.connect(tmp)
    db.executescript("""
        PRAGMA page_size = 4096;
        PRAGMA journal_mode = OFF;
        PRAGMA synchronous = OFF;
        CREATE TABLE meta(key TEXT PRIMARY KEY, value TEXT);
        -- Source and license once per pack (not on 2 million rows); the url is empty when it is the
        -- Wikipedia one (meta url_wikipedia + title): 27-nov, that kept the summary pack under 2 GB.
        CREATE TABLE sources(id INTEGER PRIMARY KEY, source TEXT, license TEXT);
        CREATE TABLE docs(id INTEGER PRIMARY KEY, title TEXT, src INTEGER, url TEXT, body BLOB);
        -- Contentless index (the text is not stored twice) and bodies compressed with raw deflate:
        -- the summary Wikipedia went from ~4 GB to under 2 GB, the limit of a GitHub release file.
        CREATE VIRTUAL TABLE fts USING fts5(title, body, content='',
                                            tokenize='unicode61 remove_diacritics 2');
    """)
    n = 0
    sources = set()
    src_ids = {}
    WIKI = "https://es.wikipedia.org/wiki/"
    rows = []

    def flush():
        db.executemany("INSERT INTO docs VALUES (?,?,?,?,?)", [r[:4] + (deflate(r[4]),) for r in rows])
        db.executemany("INSERT INTO fts(rowid, title, body) VALUES (?,?,?)", [(r[0], r[1], r[4]) for r in rows])
        rows.clear()

    for title, source, lic, url, body in conceptos(pack):
        n += 1
        key = (source, lic)
        if key not in src_ids:
            src_ids[key] = len(src_ids) + 1
            db.execute("INSERT INTO sources VALUES (?,?,?)", (src_ids[key],) + key)
        if url == WIKI + title.replace(" ", "_"):
            url = ""
        rows.append((n, title, src_ids[key], url, body))
        sources.add(source)
        if len(rows) >= 5000:
            flush()
    flush()
    titulo, desc = PACKS.get(pack, (pack, ""))
    meta = {"pack": pack, "compresion": "deflate", "url_wikipedia": WIKI, "titulo": titulo, "descripcion": desc,
            "version": version, "articulos": str(n), "okf_version": OKF_VERSION,
            "fuentes": "; ".join(sorted(s for s in sources if s))}
    db.executemany("INSERT INTO meta VALUES (?,?)", meta.items())
    db.execute("CREATE INDEX docs_title ON docs(title COLLATE NOCASE)")
    db.execute("INSERT INTO fts(fts) VALUES('optimize')")
    db.commit()
    db.execute("VACUUM")
    db.close()
    os.replace(tmp, out)
    return {"id": pack, "titulo": titulo, "descripcion": desc, "version": version, "articulos": n,
            "fichero": f"{pack}.sqlite", "url": f"{RELEASE}/v{version}/{pack}.sqlite",
            "bytes": os.path.getsize(out), "sha256": sha256(out), "fuentes": meta["fuentes"]}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def contar(d):
    return sum(1 for _, _, fs in os.walk(d) for f in fs if f.endswith(".md") and f not in RESERVED)


def titulo_indice(d, fallback):
    try:
        with open(os.path.join(d, "index.md"), encoding="utf-8") as f:
            line = f.readline().strip()
        return line[2:] if line.startswith("# ") else fallback
    except OSError:
        return fallback


def indices(manifest):
    """index.md of the bundle root (with okf_version) and of every pack folder, OKF §8 and §12."""
    entries = {e["id"]: e for e in manifest["packs"]}
    root = ["---", f'okf_version: "{OKF_VERSION}"', "---", "", "# Alejandría", ""]
    packs = {p for p in os.listdir(MD) if os.path.isdir(os.path.join(MD, p))} | {p for p, e in entries.items() if e.get("okf")}
    for pack in sorted(packs, key=lambda p: list(PACKS).index(p) if p in PACKS else 99):
        d = os.path.join(MD, pack)
        os.makedirs(d, exist_ok=True)
        titulo, desc = PACKS.get(pack, (pack, ""))
        e = entries.get(pack, {})
        lines = [f"# {titulo}", "", desc, ""] if desc else [f"# {titulo}", ""]
        subs = sorted(s for s in os.listdir(d) if os.path.isdir(os.path.join(d, s)))
        if subs:
            lines += [f"* [{titulo_indice(os.path.join(d, s), s)}]({s}/) - "
                      f"{contar(os.path.join(d, s)):,} conceptos".replace(",", ".") for s in subs]
        elif e.get("okf"):
            lines += ["# Descarga", "",
                      f"* [{pack}.okf.tar.gz]({e['okf']}) - {e.get('articulos', 0):,} conceptos OKF".replace(",", ".")
                      + f", {e.get('okf_bytes', 0) / 1e6:.0f} MB. Son demasiados ficheros para git: se descomprime"
                      f" dentro de md/ y queda en md/{pack}/."]
        with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines).strip() + "\n")
        root.append(f"* [{titulo}]({pack}/) - {desc}")
    with open(os.path.join(MD, "index.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(root) + "\n")


def log(texto):
    """New entry at the top of md/log.md (OKF §9: newest first, ## YYYY-MM-DD headings)."""
    path = os.path.join(MD, "log.md")
    today = datetime.date.today().isoformat()
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else "# Registro de cambios\n"
    head, _, rest = old.partition("\n")
    rest = rest.lstrip("\n")
    if rest.startswith(f"## {today}\n"):
        rest = rest[len(f"## {today}\n"):]
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{head}\n\n## {today}\n* {texto}\n" + ("" if rest.startswith("* ") else "\n") + rest)


if __name__ == "__main__":
    version = datetime.datetime.now().strftime("%Y.%m.%d.%H%M")
    args = sys.argv[1:]
    cut = args.index("--okf") if "--okf" in args else len(args)
    solo = args[cut + 1:]
    packs = args[:cut] + solo
    if not packs:
        packs = sorted(d for d in os.listdir(MD) if os.path.isdir(os.path.join(MD, d)))
    mpath = os.path.join(REPO, "manifest.json")
    manifest = json.load(open(mpath)) if os.path.exists(mpath) else {"packs": []}
    by_id = {e["id"]: e for e in manifest["packs"]}
    for p in packs:
        solo_okf = p in solo
        entry = by_id.get(p, {}) if solo_okf else compilar(p, version)
        a = archivo(p)
        if a and a.startswith(PAQ):
            entry.update({"okf": f"{RELEASE}/v{version}/{p}.okf.tar.gz", "okf_bytes": os.path.getsize(a),
                          "okf_sha256": sha256(a)})
        elif not solo_okf and by_id.get(p, {}).get("okf"):
            for k in ("okf", "okf_bytes", "okf_sha256"):
                entry[k] = by_id[p][k]
        by_id[p] = entry
        print(f"{p}: {entry.get('articulos')} artículos, {entry.get('bytes', 0) / 1e6:.1f} MB, versión {entry.get('version')}"
              + (f", OKF {entry['okf_bytes'] / 1e6:.0f} MB" if entry.get("okf") else ""))
    order = list(PACKS)
    manifest["packs"] = sorted(by_id.values(), key=lambda e: order.index(e["id"]) if e["id"] in order else 99)
    manifest["version"] = max(e["version"] for e in manifest["packs"])
    manifest["formato"] = 1
    manifest["okf_version"] = OKF_VERSION
    json.dump(manifest, open(mpath, "w"), ensure_ascii=False, indent=1)
    with open(os.path.join(PAQ, "ultima-version"), "w") as f:
        f.write(version)
    indices(manifest)
    hechos = [p for p in packs if p not in solo]
    log("**Update**: " + "; ".join(x for x in (hechos and "compilados " + ", ".join(hechos),
                                                solo and "archivo OKF de " + ", ".join(solo)) if x) + f" (versión {version}).")
