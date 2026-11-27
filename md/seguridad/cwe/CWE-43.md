---
type: Tipo de fallo de software
title: "CWE-43: Path Equivalence: 'filename....' (Multiple Trailing Dot)"
description: "The product accepts path input in the form of multiple trailing dot ('filedir....') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to uninten"
resource: https://cwe.mitre.org/data/definitions/43.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/43.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-43
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-43: Path Equivalence: 'filename....' (Multiple Trailing Dot)

**Tipo de fallo de software CWE-43** (Variant).

The product accepts path input in the form of multiple trailing dot ('filedir....') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

- **Es un caso de:** [CWE-42](/seguridad/cwe/CWE-42.md), [CWE-163](/seguridad/cwe/CWE-163.md)

## Consecuencias

- Read Files or Directories
