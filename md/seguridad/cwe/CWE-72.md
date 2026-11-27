---
type: Tipo de fallo de software
title: "CWE-72: Improper Handling of Apple HFS+ Alternate Data Stream Path"
description: The product does not properly handle special paths that may identify the data or resource fork of a file on the HFS+ file system.
resource: https://cwe.mitre.org/data/definitions/72.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/72.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-72
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-72: Improper Handling of Apple HFS+ Alternate Data Stream Path

**Tipo de fallo de software CWE-72** (Variant).

The product does not properly handle special paths that may identify the data or resource fork of a file on the HFS+ file system.

- **Es un caso de:** [CWE-66](/seguridad/cwe/CWE-66.md)

## Consecuencias

- Read Files or Directories: If the product chooses actions to take based on the file name, then if an attacker provides the data or resource fork, the product may take unexpected actions. Further, if the product intends to restrict access to a file, then an attacker might still be able to bypass intended access restrictions by requesting the data or resource fork for that file.
