---
type: Tipo de fallo de software
title: "CWE-53: Path Equivalence: '\\multiple\\\\internal\\backslash'"
description: "The product accepts path input in the form of multiple internal backslash ('\\multiple\\trailing\\\\slash') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the fi"
resource: https://cwe.mitre.org/data/definitions/53.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/53.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-53
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-53: Path Equivalence: '\multiple\\internal\backslash'

**Tipo de fallo de software CWE-53** (Variant).

The product accepts path input in the form of multiple internal backslash ('\multiple\trailing\\slash') without appropriate validation, which can lead to ambiguous path resolution and allow an attacker to traverse the file system to unintended locations or access arbitrary files.

- **Es un caso de:** [CWE-41](/seguridad/cwe/CWE-41.md), [CWE-165](/seguridad/cwe/CWE-165.md)

## Consecuencias

- Read Files or Directories

## Cómo evitarlo

- Inputs should be decoded and canonicalized to the application's current internal representation before being validated (CWE-180). Make sure that the application does not decode the same input twice (CWE-174). Such errors could be used to bypass allowlist validation schemes by introducing dangerous inputs after they have been checked.
