"""Medicine pack, part 1: MedlinePlus health topics in Spanish (U.S. National Library of Medicine).
The Wikipedia medical articles are added by wikipedia.py."""
import os
import xml.etree.ElementTree as ET

from comun import FUENTES, Escritor, html_a_md

LIC = "MedlinePlus, Biblioteca Nacional de Medicina de EE. UU. (NLM). Resúmenes de dominio público; cita la fuente."


def medlineplus(w):
    root = ET.parse(os.path.join(FUENTES, "mplus_topics.xml")).getroot()
    n = 0
    for t in root.iter("health-topic"):
        if t.get("language") != "Spanish":
            continue
        summary = t.findtext("full-summary") or ""
        body = html_a_md(summary)
        also = [a.text for a in t.findall("also-called") if a.text]
        groups = [g.text for g in t.findall("group") if g.text]
        head = ""
        if also:
            head += f"- **También se llama:** {', '.join(also)}\n"
        if groups:
            head += f"- **Grupo:** {', '.join(groups)}\n"
        w.add(f"medlineplus-{t.get('id')}", t.get("title"), (head + "\n" + body) if head else body,
              "MedlinePlus en español", LIC, t.get("url", ""), {"fecha": t.get("date-created")})
        n += 1
    return n


if __name__ == "__main__":
    w = Escritor("medicina/medlineplus")
    print("medlineplus:", medlineplus(w))
    print("medicina:", w.close(), "artículos")
