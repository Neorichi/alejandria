---
type: Tipo de fallo de software
title: "CWE-75: Failure to Sanitize Special Elements into a Different Plane"
description: The product does not adequately filter user-controlled input for special elements with control implications.
resource: https://cwe.mitre.org/data/definitions/75.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/75.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-75
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-75: Failure to Sanitize Special Elements into a Different Plane

**Tipo de fallo de software CWE-75** (Class).

The product does not adequately filter user-controlled input for special elements with control implications.

- **Es un caso de:** [CWE-74](/seguridad/cwe/CWE-74.md)

## Consecuencias

- Modify Application Data

## Cómo evitarlo

- Programming languages and supporting technologies might be chosen which are not subject to these issues.
- Utilize an appropriate mix of allowlist and denylist parsing to filter special element syntax from all input.
