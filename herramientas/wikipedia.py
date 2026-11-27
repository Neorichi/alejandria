"""Spanish Wikipedia dump (pages-articles.xml.bz2) → Markdown packs.

- wikipedia-resumida/es: the lead of every article (+ the facts of its infobox), at most ~1200 characters.
- wikipedia/es: every article whole (for the full pack).
- medicina/wikipedia and seguridad/wikipedia: whole articles whose categories are about medicine or security.

Uso: wikipedia.py [--max N]     (N = only the first N articles, for tests)
"""
import bz2
import multiprocessing as mp
import os
import re
import sys
import xml.etree.ElementTree as ET

import mwparserfromhell as mwp

from comun import FUENTES, FUERA, Escritor

DUMP = os.path.join(FUENTES, "eswiki-latest-pages-articles.xml.bz2")
LIC = "CC BY-SA 4.0"
FUENTE = "Wikipedia (es) 2026-11-01"

SKIP_SECTIONS = re.compile(r"^(referencias|notas|bibliograf[ií]a|enlaces externos|v[eé]ase tambi[eé]n|fuentes|"
                           r"notas y referencias|referencias y notas|lecturas? adicional(es)?|galer[ií]a)$", re.I)
MED = re.compile(r"enfermedad|síndrome|sindrome|medicament|fármaco|farmac|anatom|síntoma|sintoma|patolog|"
                 r"cáncer|cancer|oncolog|cardiolog|neurolog|psiquiatr|trastorno|infeccio|pediatr|ginecolog|"
                 r"dermatolog|oftalmolog|cirug|vacun|términos médicos|medicina|virolog|bacteri|parásit|"
                 r"fisiolog|endocrin|nefrolog|urolog|hematolog|inmunolog|nutrici|primeros auxilios|odontolog", re.I)
SEC = re.compile(r"seguridad informática|malware|virus informático|gusanos informáticos|troyano|ransomware|"
                 r"criptograf|vulnerabilidad|hacking|hacker|ataques informáticos|ciberdelincuencia|"
                 r"ciberseguridad|software de seguridad|cortafuegos|autenticación|ingeniería social", re.I)
NOTMED = re.compile(r"medicinal|plantas|vegetal|flor|semilla|hongo|flora|botánic|árbol|arbol|fauna|cultivo|gastronom|veterinari", re.I)
BIO = re.compile(r"^(nacidos|fallecidos|personas|alumnado|médicos|científicos|escritores)\b", re.I)


NOFACT = re.compile(r"imagen|image|archivo|file|coor|mapa|map|escudo|bandera|flag|pie|tamaño|size|alt$|firma|"
                    r"logo|upright|ubicaci|location|sonido|audio|color|estilo|web|sitio|url|cod|código", re.I)
MEDIA = re.compile(r"\.(svg|png|jpe?g|gif|ogg|oga|webm|tif)\b|_[NSEWO]_", re.I)


def infobox(code):
    """Facts of the first «Ficha de …» template as a short list."""
    for t in code.filter_templates(recursive=False):
        name = str(t.name).strip().lower()
        if not name.startswith(("ficha", "infobox")):
            continue
        facts = []
        for p in t.params:
            k = str(p.name).strip()
            if k.isdigit() or NOFACT.search(k):
                continue
            v = clean_inline(p.value)
            v = re.sub(r"\b(derecha|izquierda|right|left|centro|center)?\|?\d+px\b(\|[^|]*)*", "", v).strip(" |")
            if v and len(v) < 120 and not v.startswith(("http", "{")) and not MEDIA.search(v):
                facts.append(f"- **{k.replace('_', ' ').capitalize()}:** {v}")
            if len(facts) >= 10:
                break
        return "\n".join(facts)
    return ""


def clean_inline(node):
    """Plain text of a small piece of wikitext (links → their text, templates out)."""
    try:
        s = mwp.parse(str(node)).strip_code(normalize=True, collapse=True, keep_template_params=False)
    except Exception:
        s = str(node)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", s).strip(" ,;")


def to_md(title, text):
    """Returns (lead, full, categories) in Markdown, or None for redirects and disambiguation pages."""
    low = text[:400].lower()
    if low.startswith("#redirec") or "{{desambiguación" in low or "{{desambiguacion" in low:
        return None
    cats = re.findall(r"\[\[\s*Categor[ií]a\s*:\s*([^\]|]+)", text, re.I)
    # Out before parsing: references, comments, files, galleries, tables.
    t = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    t = re.sub(r"<ref[^>/]*/>", "", t)
    t = re.sub(r"<ref[^>]*>.*?</ref>", "", t, flags=re.S | re.I)
    t = re.sub(r"<(gallery|math|syntaxhighlight|score|timeline)[^>]*>.*?</\1>", "", t, flags=re.S | re.I)
    t = re.sub(r"\{\|.*?\n\|\}", "", t, flags=re.S)
    try:
        code = mwp.parse(t)
    except Exception:
        return None
    facts = infobox(code)
    # Files, categories and interwiki links out; other links → their text.
    for link in code.filter_wikilinks():
        target = str(link.title).strip().lower()
        try:
            if re.match(r"(archivo|file|imagen|image|categor[ií]a|category)\s*:", target) or re.match(r"[a-z\-]{2,12}:", target):
                code.remove(link)
        except ValueError:
            pass
    for tpl in code.filter_templates(recursive=False):
        try:
            code.remove(tpl)
        except ValueError:
            pass
    raw = str(code)
    # Bold and italics through placeholders: strip_code would take "**" at the start of a line for a list.
    raw = re.sub(r"'''''(.+?)'''''", "\x01\\1\x01", raw)
    raw = re.sub(r"'''(.+?)'''", "\x02\\1\x02", raw)
    raw = re.sub(r"''(.+?)''", "\x03\\1\x03", raw)
    plain = mwp.parse(raw).strip_code(normalize=True, collapse=False, keep_template_params=False)
    lines, out, skip = plain.split("\n"), [], False
    for line in lines:
        m = re.match(r"^(={2,6})\s*(.+?)\s*\1\s*$", line)
        if m:
            name = m.group(2).strip()
            skip = bool(SKIP_SECTIONS.match(name))
            if not skip:
                out.append("\n" + "#" * min(len(m.group(1)), 4) + " " + name + "\n")
            continue
        if skip:
            continue
        line = re.sub(r"<[^>]+>", "", line).rstrip()
        line = re.sub(r"^\*+\s*", "- ", line)
        line = re.sub(r"^#+\s*", "1. ", line)
        line = re.sub(r"^[:;]+\s*", "", line)
        line = re.sub(r"\(\s*[,;]?\s*\)", "", line)
        out.append(line)
    full = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
    full = full.replace("\x01", "***").replace("\x02", "**").replace("\x03", "*")
    full = re.sub(r"(?m)^#+ .+\n+(?=#+ |\Z)", "", full)  # headings left empty
    if len(full) < 40:
        return None
    lead = full.split("\n#", 1)[0].strip()
    if len(lead) > 800:
        cut = lead[:800]
        lead = cut[: max(cut.rfind(". "), 400) + 1] + " …"
    if facts:
        lead = facts + "\n\n" + lead
        full = facts + "\n\n" + full
    return lead, full, cats


def work(page):
    title, text = page
    try:
        r = to_md(title, text)
    except Exception:
        return None
    return (title,) + r if r else None


def pages(limit):
    n = 0
    with bz2.open(DUMP, "rb") as f:
        ns = ""
        for ev, el in ET.iterparse(f, events=("end",)):
            tag = el.tag.rsplit("}", 1)[-1]
            if not ns and "}" in el.tag:
                ns = el.tag.split("}")[0] + "}"
            if tag != "page":
                continue
            if el.findtext(f"{ns}ns") == "0" and el.find(f"{ns}redirect") is None:
                text = el.findtext(f"{ns}revision/{ns}text") or ""
                yield el.findtext(f"{ns}title"), text
                n += 1
                if limit and n >= limit:
                    return
            el.clear()


def url(title):
    return "https://es.wikipedia.org/wiki/" + title.replace(" ", "_")


if __name__ == "__main__":
    limit = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 0
    w_lead, w_full = Escritor("wikipedia-resumida/es"), Escritor("wikipedia/es", base=FUERA)
    w_med, w_sec = Escritor("medicina/wikipedia"), Escritor("seguridad/wikipedia")
    n = 0
    with mp.Pool(max(1, os.cpu_count() - 1)) as pool:
        for r in pool.imap(work, pages(limit), chunksize=64):
            n += 1
            if n % 50000 == 0:
                print(f"{n} páginas · resumida {w_lead.count} · medicina {w_med.count} · seguridad {w_sec.count}", flush=True)
            if not r:
                continue
            title, lead, full, cats = r
            uid = "eswiki-" + re.sub(r"\s+", "_", title)
            w_lead.add(uid, title, lead, FUENTE, LIC, url(title))
            w_full.add(uid, title, full, FUENTE, LIC, url(title))
            bio = any(BIO.match(c) for c in cats)
            if not bio and any(MED.search(c) and not NOTMED.search(c) for c in cats):
                w_med.add(uid, title, full, FUENTE, LIC, url(title))
            if any(SEC.search(c) for c in cats):
                w_sec.add(uid, title, full, FUENTE, LIC, url(title))
    print("fin:", n, "páginas · resumida", w_lead.close(), "· completa", w_full.close(),
          "· medicina", w_med.close(), "· seguridad", w_sec.close())
