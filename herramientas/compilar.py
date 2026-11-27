"""md/<pack>/**/*.md → paquetes/<pack>.sqlite (SQLite FTS5) + manifest.json (in the alejandria repo).

The iPhone downloads the .sqlite: articles plus a full-text index (BM25), without accents in the index so
"medico" finds "médico". Version = build date; the app compares it with the one it has.

Uso: compilar.py PACK [PACK…]      (sin argumentos: todos los que haya en md/)
"""
import datetime
import hashlib
import json
import os
import sqlite3
import sys

from comun import GITHUB, MD, RAIZ, REPO, leer_md

# The .sqlite files are too big for git: they go to a GitHub release (publicar.sh), not to the repo.
PAQ = os.path.join(RAIZ, "paquetes")

PACKS = {
    "seguridad": ("Seguridad informática",
                  "Vulnerabilidades explotadas (CISA KEV), técnicas y grupos de ataque (MITRE ATT&CK) y tipos de fallo (CWE)."),
    "medicina": ("Medicina y salud",
                 "Temas de salud de MedlinePlus en español y artículos de medicina de Wikipedia. No sustituye a un médico."),
    "wikipedia-resumida": ("Wikipedia (resumen)",
                           "El principio de cada artículo de la Wikipedia en español: historia, ciencia, geografía, personas…"),
    "wikipedia": ("Wikipedia completa", "Todos los artículos de la Wikipedia en español, enteros."),
}


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
        CREATE TABLE docs(id INTEGER PRIMARY KEY, uid TEXT, title TEXT, url TEXT, source TEXT, license TEXT, body TEXT);
        CREATE VIRTUAL TABLE fts USING fts5(title, body, content='docs', content_rowid='id',
                                            tokenize='unicode61 remove_diacritics 2');
    """)
    n = 0
    sources = set()
    files = sorted(os.path.join(d, f) for d, _, fs in os.walk(os.path.join(MD, pack)) for f in fs if f.endswith(".md"))
    for path in files:
        rows = []
        for meta, body in leer_md(path):
            n += 1
            rows.append((n, meta.get("id", ""), meta.get("titulo", ""), meta.get("url", ""), meta.get("fuente", ""),
                         meta.get("licencia", ""), body))
            sources.add(meta.get("fuente", ""))
        db.executemany("INSERT INTO docs VALUES (?,?,?,?,?,?,?)", rows)
        db.executemany("INSERT INTO fts(rowid, title, body) VALUES (?,?,?)", [(r[0], r[2], r[6]) for r in rows])
    titulo, desc = PACKS.get(pack, (pack, ""))
    meta = {"pack": pack, "titulo": titulo, "descripcion": desc, "version": version, "articulos": str(n),
            "fuentes": "; ".join(sorted(s for s in sources if s))}
    db.executemany("INSERT INTO meta VALUES (?,?)", meta.items())
    db.execute("CREATE INDEX docs_title ON docs(title COLLATE NOCASE)")
    db.execute("INSERT INTO fts(fts) VALUES('optimize')")
    db.commit()
    db.execute("VACUUM")
    db.close()
    os.replace(tmp, out)
    h = hashlib.sha256()
    with open(out, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return {"id": pack, "titulo": titulo, "descripcion": desc, "version": version, "articulos": n,
            "fichero": f"{pack}.sqlite", "url": f"https://github.com/{GITHUB}/releases/download/v{version}/{pack}.sqlite",
            "bytes": os.path.getsize(out), "sha256": h.hexdigest(),
            "fuentes": meta["fuentes"]}


if __name__ == "__main__":
    version = datetime.datetime.now().strftime("%Y.%m.%d.%H%M")
    packs = sys.argv[1:] or sorted(d for d in os.listdir(MD) if os.path.isdir(os.path.join(MD, d)))
    mpath = os.path.join(REPO, "manifest.json")
    manifest = json.load(open(mpath)) if os.path.exists(mpath) else {"packs": []}
    for p in packs:
        entry = compilar(p, version)
        manifest["packs"] = [e for e in manifest["packs"] if e["id"] != p] + [entry]
        print(f"{p}: {entry['articulos']} artículos, {entry['bytes'] / 1e6:.1f} MB, versión {version}")
    order = list(PACKS)
    manifest["packs"].sort(key=lambda e: order.index(e["id"]) if e["id"] in order else 99)
    manifest["version"] = max(e["version"] for e in manifest["packs"])
    manifest["formato"] = 1
    json.dump(manifest, open(mpath, "w"), ensure_ascii=False, indent=1)
