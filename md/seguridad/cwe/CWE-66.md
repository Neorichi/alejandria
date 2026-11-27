---
type: Tipo de fallo de software
title: "CWE-66: Improper Handling of File Names that Identify Virtual Resources"
description: "The product does not handle or incorrectly handles a file name that identifies a \"virtual\" resource that is not directly specified within the directory that is associated with the file name."
resource: https://cwe.mitre.org/data/definitions/66.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/66.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-66
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-66: Improper Handling of File Names that Identify Virtual Resources

**Tipo de fallo de software CWE-66** (Base).

The product does not handle or incorrectly handles a file name that identifies a "virtual" resource that is not directly specified within the directory that is associated with the file name.

- **Es un caso de:** [CWE-706](/seguridad/cwe/CWE-706.md)

## Consecuencias

- Varies by Context: The product could perform file-based operations on a resource that is not a file.
