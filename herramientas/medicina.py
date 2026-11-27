"""Medicine pack, part 1: MedlinePlus health topics in Spanish (U.S. National Library of Medicine) → OKF concepts in
md/medicina/medlineplus, linked to their related topics. The Wikipedia medical articles are added by wikipedia.py."""
import datetime
import os
import xml.etree.ElementTree as ET

from comun import FUENTES, Escritor, html_a_md, slug

LIC = "MedlinePlus, Biblioteca Nacional de Medicina de EE. UU. (NLM). Resúmenes de dominio público; cita la fuente."


def medlineplus():
    root = ET.parse(os.path.join(FUENTES, "mplus_topics.xml")).getroot()
    try:
        gen = datetime.datetime.strptime(root.get("date-generated", ""), "%m/%d/%Y %H:%M:%S").strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        gen = ""
    topics = [t for t in root.iter("health-topic") if t.get("language") == "Spanish"]
    # Paths first, so a topic can link to any other (by id or by its URL inside the summary).
    paths, by_url, used = {}, {}, set()
    for t in topics:
        s = slug(t.get("title", "")) or t.get("id")
        while s in used:
            s += "-" + t.get("id")
        used.add(s)
        paths[t.get("id")] = (f"{s[0] if s[0].isalpha() else '0-9'}/{s}", t.get("title"))
        by_url[t.get("url", "")] = f"/medicina/medlineplus/{paths[t.get('id')][0]}.md"
    w = Escritor("medicina/medlineplus", "MedlinePlus en español")
    for t in topics:
        body = html_a_md(t.findtext("full-summary") or "", by_url)
        also = [a.text for a in t.findall("also-called") if a.text]
        groups = [g.text for g in t.findall("group") if g.text]
        head = ""
        if also:
            head += f"- **También se llama:** {', '.join(also)}\n"
        if groups:
            head += f"- **Grupo:** {', '.join(groups)}\n"
        body = (head + "\n" + body) if head else body
        related = [(r.text, paths[r.get("id")][0]) for r in t.findall("related-topic") if r.get("id") in paths and r.text]
        if related:
            body += "\n\n## Temas relacionados\n\n" + "\n".join(f"- [{n}](/medicina/medlineplus/{p}.md)" for n, p in related)
        en = t.find("language-mapped-topic")
        fuente = {"id": "medlineplus", "resource": t.get("url", ""), "title": "MedlinePlus en español",
                  "author": "org:nlm", "last_modified": gen}
        w.add(paths[t.get("id")][0], f"medlineplus-{t.get('id')}", "Tema de salud", t.get("title"), body, fuente, LIC,
              t.get("url", ""), ["salud", "medlineplus"] + groups, descripcion=t.get("meta-desc") or None,
              stale_dias=365, extra={"english": en.text if en is not None else None})
    return w.close()


if __name__ == "__main__":
    print("medlineplus:", medlineplus())
