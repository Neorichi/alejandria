---
type: Tipo de fallo de software
title: "CWE-45: Path Equivalence: 'file...name' (Multiple Internal Dot)"
description: "The product accepts path input in the form of multiple internal dot ('file...dir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintend"
resource: https://cwe.mitre.org/data/definitions/45.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/45.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-45
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-45: Path Equivalence: 'file...name' (Multiple Internal Dot)

**Tipo de fallo de software CWE-45** (Variant).

The product accepts path input in the form of multiple internal dot ('file...dir') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

- **Es un caso de:** [CWE-44](/seguridad/cwe/CWE-44.md), [CWE-165](/seguridad/cwe/CWE-165.md)

## Consecuencias

- Read Files or Directories
