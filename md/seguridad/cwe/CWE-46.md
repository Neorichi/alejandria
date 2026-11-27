---
type: Tipo de fallo de software
title: "CWE-46: Path Equivalence: 'filename ' (Trailing Space)"
description: "The product accepts path input in the form of trailing space ('filedir ') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locati"
resource: https://cwe.mitre.org/data/definitions/46.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/46.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-46
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-46: Path Equivalence: 'filename ' (Trailing Space)

**Tipo de fallo de software CWE-46** (Variant).

The product accepts path input in the form of trailing space ('filedir ') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

- **Es un caso de:** [CWE-41](/seguridad/cwe/CWE-41.md), [CWE-162](/seguridad/cwe/CWE-162.md)

## Consecuencias

- Read Files or Directories
