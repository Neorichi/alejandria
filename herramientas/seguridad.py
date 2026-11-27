"""Security pack: CISA KEV (exploited vulnerabilities), MITRE ATT&CK (techniques, groups, software,
mitigations, campaigns) and CWE (weakness types) → OKF concepts in md/seguridad/{kev,attack,cwe}.
Concepts link to each other: a KEV entry to its CWE, a group to the techniques and software it uses,
a technique to its parent technique and to the mitigations for it. Sources in enciclopedia/fuentes/."""
import json
import os
import re
import xml.etree.ElementTree as ET
from collections import defaultdict

from comun import FUENTES, Escritor, one_line

ATTACK_LIC = "© The MITRE Corporation. Reproducido y distribuido con permiso de The MITRE Corporation (ATT&CK)."
CWE_LIC = "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
KEV_LIC = "Dominio público (CISA, Gobierno de EE. UU.)."


def cwe_root():
    path = next(os.path.join(FUENTES, f) for f in sorted(os.listdir(FUENTES)) if f.startswith("cwec_") and f.endswith(".xml"))
    root = ET.parse(path).getroot()
    return root, {"c": root.tag.split("}")[0].strip("{")}


def cwe_ids():
    root, ns = cwe_root()
    return {wk.get("ID") for wk in root.iterfind(".//c:Weakness", ns) if wk.get("Status") != "Deprecated"}


def kev(cwes):
    w = Escritor("seguridad/kev", "Vulnerabilidades explotadas (CISA KEV)")
    d = json.load(open(os.path.join(FUENTES, "kev.json")))
    fuente = {"id": "cisa-kev", "resource": "https://www.cisa.gov/known-exploited-vulnerabilities-catalog",
              "title": "CISA Known Exploited Vulnerabilities " + d.get("catalogVersion", ""), "author": "org:cisa",
              "last_modified": re.sub(r"\.\d+Z$", "Z", d.get("dateReleased", ""))}
    for v in d["vulnerabilities"]:
        cve = v["cveID"]
        links = [f"[{c}](/seguridad/cwe/{c}.md)" if c.removeprefix("CWE-") in cwes else c for c in v.get("cwes", [])]
        ransom = v.get("knownRansomwareCampaignUse") == "Known"
        body = f"""**Vulnerabilidad explotada activamente** (catálogo KEV de CISA).

- **CVE:** {cve}
- **Fabricante / producto:** {v.get('vendorProject', '')} / {v.get('product', '')}
- **Nombre:** {v.get('vulnerabilityName', '')}
- **Añadida al catálogo:** {v.get('dateAdded', '')}
{'- **Usada en campañas de ransomware:** sí' + chr(10) if ransom else ''}- **Tipos de fallo (CWE):** {', '.join(links) or '—'}

{v.get('shortDescription', '')}

**Qué hacer:** {v.get('requiredAction', '')}
"""
        if v.get("notes"):
            body += f"\nNotas: {v['notes']}\n"
        year = cve.split("-")[1] if cve.count("-") >= 2 else "otros"
        tags = ["seguridad", "kev", v.get("vendorProject", "")] + (["ransomware"] if ransom else [])
        w.add(f"{year}/{cve}", f"kev-{cve}", "Vulnerabilidad explotada",
              f"{cve} · {v.get('vendorProject', '')} {v.get('product', '')}: {v.get('vulnerabilityName', '')}",
              body, fuente, KEV_LIC, f"https://nvd.nist.gov/vuln/detail/{cve}", [t for t in tags if t],
              descripcion=one_line(v.get("shortDescription", ""))[:220], stale_dias=30,
              extra={"date_added": v.get("dateAdded"), "due_date": v.get("dueDate")})
    return w.close()


KINDS = {"attack-pattern": ("Técnica", "Técnica de ataque", "tecnicas"),
         "intrusion-set": ("Grupo", "Grupo de ataque", "grupos"),
         "malware": ("Malware", "Malware", "software"),
         "tool": ("Herramienta", "Herramienta de ataque", "software"),
         "course-of-action": ("Mitigación", "Mitigación", "mitigaciones"),
         "campaign": ("Campaña", "Campaña de ataque", "campanas")}


def clean(s):
    s = re.sub(r"\(Citation:[^)]*\)", "", s or "").strip()
    return re.sub(r"\[([^\]]+)\]\(https://attack\.mitre\.org[^)]*\)", r"\1", s)


def attack():
    w = Escritor("seguridad/attack", "MITRE ATT&CK Enterprise")
    d = json.load(open(os.path.join(FUENTES, "enterprise-attack.json")))
    objs = {}
    for o in d["objects"]:
        k = KINDS.get(o.get("type"))
        if not k or o.get("revoked") or o.get("x_mitre_deprecated"):
            continue
        ref = next((r for r in o.get("external_references", []) if r.get("source_name") == "mitre-attack"), {})
        aid = ref.get("external_id", "") or o["id"]
        objs[o["id"]] = (o, k, aid, ref.get("url", ""), f"/seguridad/attack/{k[2]}/{aid}.md")
    rel = defaultdict(lambda: defaultdict(set))  # stix id → relation name → {stix ids}
    for r in d["objects"]:
        if r.get("type") != "relationship" or r.get("revoked") or r.get("x_mitre_deprecated"):
            continue
        a, b, t = r.get("source_ref"), r.get("target_ref"), r.get("relationship_type")
        if a not in objs or b not in objs:
            continue
        ka, kb = objs[a][0]["type"], objs[b][0]["type"]
        if t == "uses":
            if kb == "attack-pattern":
                rel[a]["Técnicas que usa"].add(b)
                if ka == "intrusion-set":
                    rel[b]["Grupos que la usan"].add(a)
            else:
                rel[a]["Software que usa"].add(b)
                if ka == "intrusion-set":
                    rel[b]["Grupos que lo usan"].add(a)
        elif t == "mitigates":
            rel[a]["Técnicas que mitiga"].add(b)
            rel[b]["Mitigaciones"].add(a)
        elif t == "subtechnique-of":
            rel[a]["Subtécnica de"].add(b)
            rel[b]["Subtécnicas"].add(a)
        elif t == "attributed-to":
            rel[a]["Atribuida a"].add(b)
            rel[b]["Campañas"].add(a)
    order = ["Subtécnica de", "Atribuida a", "Técnicas que usa", "Software que usa", "Subtécnicas", "Mitigaciones",
             "Técnicas que mitiga", "Grupos que la usan", "Grupos que lo usan", "Campañas"]
    attack_v = next((o.get("x_mitre_version") for o in d["objects"] if o.get("type") == "x-mitre-collection"), "")
    for sid, (o, k, aid, url, _) in objs.items():
        body = f"**{k[0]} de MITRE ATT&CK** {aid}.\n\n"
        if o.get("aliases"):
            body += f"- **Otros nombres:** {', '.join(o['aliases'])}\n"
        if o.get("x_mitre_platforms"):
            body += f"- **Plataformas:** {', '.join(o['x_mitre_platforms'])}\n"
        phases = [p["phase_name"] for p in o.get("kill_chain_phases", [])]
        if phases:
            body += f"- **Tácticas:** {', '.join(phases)}\n"
        desc = clean(o.get("description", ""))
        body += f"\n{desc}\n"
        if o.get("x_mitre_detection"):
            body += f"\n## Detección\n\n{clean(o['x_mitre_detection'])}\n"
        for name in order:
            ids = rel[sid].get(name)
            if not ids:
                continue
            items = sorted((objs[i][2], objs[i][0].get("name", ""), objs[i][4]) for i in ids)
            body += f"\n## {name}\n\n" + "\n".join(f"- [{a} {n}]({p})" for a, n, p in items[:60])
            body += f"\n- … y {len(items) - 60} más\n" if len(items) > 60 else "\n"
        modified = re.sub(r"\.\d+Z$", "Z", o.get("modified", ""))
        fuente = {"id": "mitre-attack", "resource": url or "https://attack.mitre.org/",
                  "title": "MITRE ATT&CK Enterprise" + (f" v{attack_v}" if attack_v else ""), "author": "org:mitre",
                  "last_modified": modified}
        w.add(f"{k[2]}/{aid}", f"attack-{aid}", k[1], f"{aid} {o.get('name', '')} ({k[0]})", body, fuente,
              ATTACK_LIC, url, ["seguridad", "mitre-attack"] + phases, stale_dias=180)
    return w.close()


def cwe():
    w = Escritor("seguridad/cwe", "MITRE CWE: tipos de fallo de software")
    root, ns = cwe_root()
    valid = cwe_ids()

    def text(e):
        return one_line("".join(e.itertext())) if e is not None else ""

    for wk in root.iterfind(".//c:Weakness", ns):
        if wk.get("Status") == "Deprecated":
            continue
        cid = wk.get("ID")
        desc = text(wk.find("c:Description", ns))
        body = f"**Tipo de fallo de software CWE-{cid}** ({wk.get('Abstraction', '')}).\n\n{desc}\n"
        ext = text(wk.find("c:Extended_Description", ns))
        if ext:
            body += f"\n{ext}\n"
        parents = [r.get("CWE_ID") for r in wk.iterfind("c:Related_Weaknesses/c:Related_Weakness", ns)
                   if r.get("Nature") == "ChildOf" and r.get("CWE_ID") in valid]
        if parents:
            body += "\n- **Es un caso de:** " + ", ".join(f"[CWE-{p}](/seguridad/cwe/CWE-{p}.md)" for p in dict.fromkeys(parents)) + "\n"
        cons = [text(c.find("c:Impact", ns)) + (": " + text(c.find("c:Note", ns)) if c.find("c:Note", ns) is not None else "")
                for c in wk.iterfind("c:Common_Consequences/c:Consequence", ns)]
        if cons:
            body += "\n## Consecuencias\n\n" + "\n".join(f"- {c}" for c in cons if c.strip()) + "\n"
        mits = [text(m.find("c:Description", ns)) for m in wk.iterfind("c:Potential_Mitigations/c:Mitigation", ns)]
        if mits:
            body += "\n## Cómo evitarlo\n\n" + "\n".join(f"- {m}" for m in mits[:8] if m) + "\n"
        url = f"https://cwe.mitre.org/data/definitions/{cid}.html"
        fuente = {"id": "mitre-cwe", "resource": url, "title": f"MITRE CWE {root.get('Version', '')}".strip(),
                  "author": "org:mitre", "last_modified": f"{root.get('Date')}T00:00:00Z" if root.get("Date") else ""}
        w.add(f"CWE-{cid}", f"cwe-{cid}", "Tipo de fallo de software", f"CWE-{cid}: {wk.get('Name')}", body, fuente,
              CWE_LIC, url, ["seguridad", "cwe"], descripcion=desc[:220], stale_dias=365)
    return w.close()


if __name__ == "__main__":
    print("kev:", kev(cwe_ids()))
    print("attack:", attack())
    print("cwe:", cwe())
