"""One-off (27-nov-2026): the Wikipedia packs made before OKF (several articles per file, in legado-md/) → OKF
concepts, without parsing the 5 GB dump again. The new wikipedia.py already writes OKF directly.

Uso: mv alejandria/md legado-md && migrar_okf.py
"""
import os
import sys

from comun import PAQ, RAIZ, Escritor, leer_md, wiki_add

LEGADO = os.path.join(RAIZ, "legado-md")


def migrar(src, w, tags, nivel=1):
    d = os.path.join(LEGADO, src)
    for f in sorted(os.listdir(d)):
        if f.endswith(".md"):
            for meta, body in leer_md(os.path.join(d, f)):
                wiki_add(w, meta["titulo"], body, tags, nivel)
    return w.close()


if __name__ == "__main__":
    which = sys.argv[1:] or ["medicina", "seguridad", "resumida"]
    if "medicina" in which:
        print("medicina/wikipedia:", migrar("medicina/wikipedia", Escritor("medicina/wikipedia", "Medicina en Wikipedia"),
                                            ["medicina", "wikipedia"]), flush=True)
    if "seguridad" in which:
        print("seguridad/wikipedia:", migrar("seguridad/wikipedia",
                                             Escritor("seguridad/wikipedia", "Seguridad informática en Wikipedia"),
                                             ["seguridad", "wikipedia"]), flush=True)
    if "resumida" in which:
        w = Escritor("wikipedia-resumida", "Wikipedia en español (resumen)",
                     archivo=os.path.join(PAQ, "wikipedia-resumida.okf.tar.gz"))
        print("wikipedia-resumida:", migrar("wikipedia-resumida/es", w, ["wikipedia"], nivel=2), flush=True)
