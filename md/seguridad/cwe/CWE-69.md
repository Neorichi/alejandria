---
type: Tipo de fallo de software
title: "CWE-69: Improper Handling of Windows ::DATA Alternate Data Stream"
description: The product does not properly prevent access to, or detect usage of, alternate data streams (ADS).
resource: https://cwe.mitre.org/data/definitions/69.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/69.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-69
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-69: Improper Handling of Windows ::DATA Alternate Data Stream

**Tipo de fallo de software CWE-69** (Variant).

The product does not properly prevent access to, or detect usage of, alternate data streams (ADS).

- **Es un caso de:** [CWE-66](/seguridad/cwe/CWE-66.md)

## Consecuencias

- Bypass Protection Mechanism: An attacker can use an ADS to hide information about a file (e.g. size, the name of the process) from a system or file browser tools such as Windows Explorer and 'dir' at the command line utility. Alternately, the attacker might be able to bypass intended access restrictions for the associated data fork.

## Cómo evitarlo

- Ensure that the source code correctly parses the filename to read or write to the correct stream.
