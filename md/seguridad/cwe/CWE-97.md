---
type: Tipo de fallo de software
title: "CWE-97: Improper Neutralization of Server-Side Includes (SSI) Within a Web Page"
description: The product generates a web page, but does not neutralize or incorrectly neutralizes user-controllable input that could be interpreted as a server-side include (SSI) directive.
resource: https://cwe.mitre.org/data/definitions/97.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/97.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-97
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-97: Improper Neutralization of Server-Side Includes (SSI) Within a Web Page

**Tipo de fallo de software CWE-97** (Variant).

The product generates a web page, but does not neutralize or incorrectly neutralizes user-controllable input that could be interpreted as a server-side include (SSI) directive.

- **Es un caso de:** [CWE-96](/seguridad/cwe/CWE-96.md)

## Consecuencias

- Execute Unauthorized Code or Commands
