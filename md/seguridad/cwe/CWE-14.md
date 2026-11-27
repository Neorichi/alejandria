---
type: Tipo de fallo de software
title: "CWE-14: Compiler Removal of Code to Clear Buffers"
description: "Sensitive memory is cleared according to the source code, but compiler optimizations leave the memory untouched when it is not read from again, aka \"dead store removal.\""
resource: https://cwe.mitre.org/data/definitions/14.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/14.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-14
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-14: Compiler Removal of Code to Clear Buffers

**Tipo de fallo de software CWE-14** (Variant).

Sensitive memory is cleared according to the source code, but compiler optimizations leave the memory untouched when it is not read from again, aka "dead store removal."

- **Es un caso de:** [CWE-733](/seguridad/cwe/CWE-733.md)

## Consecuencias

- Read Memory: This weakness will allow data that has not been cleared from memory to be read. If this data contains sensitive password information, then an attacker can read the password and use the information to bypass protection mechanisms.

## Cómo evitarlo

- Store the sensitive data in a "volatile" memory location if available.
- If possible, configure the compiler so that it does not remove dead stores.
- Where possible, encrypt sensitive data that are used by a software system.
