"""Security pack: CISA KEV (exploited vulnerabilities), MITRE ATT&CK (techniques, groups, software,
mitigations) and CWE (weakness types) → Markdown. Sources in enciclopedia/fuentes/."""
import json
import os
import re
import xml.etree.ElementTree as ET

from comun import FUENTES, Escritor, one_line

ATTACK_LIC = "© The MITRE Corporation. Reproducido y distribuido con permiso de The MITRE Corporation (ATT&CK)."
CWE_LIC = "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
KEV_LIC = "Dominio público (CISA, Gobierno de EE. UU.)."


def kev(w):
    d = json.load(open(os.path.join(FUENTES, "kev.json")))
    for v in d["vulnerabilities"]:
        cve = v["cveID"]
        body = f"""**Vulnerabilidad explotada activamente** (catálogo KEV de CISA).

- **CVE:** {cve}
- **Fabricante / producto:** {v.get('vendorProject', '')} / {v.get('product', '')}
- **Nombre:** {v.get('vulnerabilityName', '')}
- **Añadida al catálogo:** {v.get('dateAdded', '')}
{'- **Usada en campañas de ransomware:** sí' + chr(10) if v.get('knownRansomwareCampaignUse') == 'Known' else ''}- **Tipos de fallo (CWE):** {', '.join(v.get('cwes', [])) or '—'}

{v.get('shortDescription', '')}

**Qué hacer:** {v.get('requiredAction', '')}
"""
        if v.get("notes"):
            body += f"\nNotas: {v['notes']}\n"
        w.add(f"kev-{cve}", f"{cve} · {v.get('vendorProject', '')} {v.get('product', '')}: {v.get('vulnerabilityName', '')}",
              body, "CISA Known Exploited Vulnerabilities " + d.get("catalogVersion", ""), KEV_LIC,
              f"https://nvd.nist.gov/vuln/detail/{cve}", {"fecha": v.get("dateAdded")})


def attack(w):
    d = json.load(open(os.path.join(FUENTES, "enterprise-attack.json")))
    kinds = {"attack-pattern": "Técnica", "intrusion-set": "Grupo", "malware": "Malware", "tool": "Herramienta",
             "course-of-action": "Mitigación", "campaign": "Campaña"}
    for o in d["objects"]:
        k = kinds.get(o.get("type"))
        if not k or o.get("revoked") or o.get("x_mitre_deprecated"):
            continue
        ref = next((r for r in o.get("external_references", []) if r.get("source_name") == "mitre-attack"), {})
        aid, url = ref.get("external_id", ""), ref.get("url", "")
        desc = re.sub(r"\(Citation:[^)]*\)", "", o.get("description", "")).strip()
        desc = re.sub(r"\[([^\]]+)\]\(https://attack\.mitre\.org[^)]*\)", r"\1", desc)
        body = f"**{k} de MITRE ATT&CK** {aid}.\n\n"
        if o.get("aliases"):
            body += f"- **Otros nombres:** {', '.join(o['aliases'])}\n"
        if o.get("x_mitre_platforms"):
            body += f"- **Plataformas:** {', '.join(o['x_mitre_platforms'])}\n"
        phases = [p["phase_name"] for p in o.get("kill_chain_phases", [])]
        if phases:
            body += f"- **Tácticas:** {', '.join(phases)}\n"
        body += f"\n{desc}\n"
        if o.get("x_mitre_detection"):
            body += f"\n## Detección\n\n{re.sub(r'(Citation:[^)]*)', '', o['x_mitre_detection'])}\n"
        w.add(f"attack-{aid or o['id']}", f"{aid} {o.get('name', '')} ({k})", body, "MITRE ATT&CK Enterprise", ATTACK_LIC, url)


def cwe(w):
    path = next(os.path.join(FUENTES, f) for f in os.listdir(FUENTES) if f.startswith("cwec_") and f.endswith(".xml"))
    root = ET.parse(path).getroot()
    ns = {"c": root.tag.split("}")[0].strip("{")}

    def text(e):
        return one_line("".join(e.itertext())) if e is not None else ""

    for wk in root.iterfind(".//c:Weakness", ns):
        if wk.get("Status") == "Deprecated":
            continue
        cid = wk.get("ID")
        body = f"**Tipo de fallo de software CWE-{cid}** ({wk.get('Abstraction', '')}).\n\n{text(wk.find('c:Description', ns))}\n"
        ext = text(wk.find("c:Extended_Description", ns))
        if ext:
            body += f"\n{ext}\n"
        cons = [text(c.find("c:Impact", ns)) + (": " + text(c.find("c:Note", ns)) if c.find("c:Note", ns) is not None else "")
                for c in wk.iterfind("c:Common_Consequences/c:Consequence", ns)]
        if cons:
            body += "\n## Consecuencias\n\n" + "\n".join(f"- {c}" for c in cons if c.strip()) + "\n"
        mits = [text(m.find("c:Description", ns)) for m in wk.iterfind("c:Potential_Mitigations/c:Mitigation", ns)]
        if mits:
            body += "\n## Cómo evitarlo\n\n" + "\n".join(f"- {m}" for m in mits[:8] if m) + "\n"
        w.add(f"cwe-{cid}", f"CWE-{cid}: {wk.get('Name')}", body, "MITRE CWE", CWE_LIC,
              f"https://cwe.mitre.org/data/definitions/{cid}.html")


if __name__ == "__main__":
    w = Escritor("seguridad/mitre-cisa")
    kev(w)
    attack(w)
    cwe(w)
    print("seguridad:", w.close(), "artículos")
