---
type: Tipo de fallo de software
title: "CWE-42: Path Equivalence: 'filename.' (Trailing Dot)"
description: "The product accepts path input in the form of trailing dot ('filedir.') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended location"
resource: https://cwe.mitre.org/data/definitions/42.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/42.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-42
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-42: Path Equivalence: 'filename.' (Trailing Dot)

**Tipo de fallo de software CWE-42** (Variant).

The product accepts path input in the form of trailing dot ('filedir.') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

- **Es un caso de:** [CWE-41](/seguridad/cwe/CWE-41.md), [CWE-162](/seguridad/cwe/CWE-162.md)

## Consecuencias

- Bypass Protection Mechanism
