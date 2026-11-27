---
type: Tipo de fallo de software
title: "CWE-58: Path Equivalence: Windows 8.3 Filename"
description: "The product contains a protection mechanism that restricts access to a long filename on a Windows operating system, but it does not properly restrict access to the equivalent short \"8.3\" filename."
resource: https://cwe.mitre.org/data/definitions/58.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/58.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-58
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-58: Path Equivalence: Windows 8.3 Filename

**Tipo de fallo de software CWE-58** (Variant).

The product contains a protection mechanism that restricts access to a long filename on a Windows operating system, but it does not properly restrict access to the equivalent short "8.3" filename.

- **Es un caso de:** [CWE-41](/seguridad/cwe/CWE-41.md)

## Consecuencias

- Read Files or Directories

## Cómo evitarlo

- Disable Windows from supporting 8.3 filenames by editing the Windows registry. Preventing 8.3 filenames will not remove previously generated 8.3 filenames.
