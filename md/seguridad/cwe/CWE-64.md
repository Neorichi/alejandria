---
type: Tipo de fallo de software
title: "CWE-64: Windows Shortcut Following (.LNK)"
description: The product, when opening a file or directory, does not sufficiently handle when the file is a Windows shortcut (.LNK) whose target is outside of the intended control sphere. This could allow an attacker to cause the pro
resource: https://cwe.mitre.org/data/definitions/64.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/64.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-64
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-64: Windows Shortcut Following (.LNK)

**Tipo de fallo de software CWE-64** (Variant).

The product, when opening a file or directory, does not sufficiently handle when the file is a Windows shortcut (.LNK) whose target is outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.

- **Es un caso de:** [CWE-59](/seguridad/cwe/CWE-59.md)

## Consecuencias

- Read Files or Directories: The shortcut (file with the .lnk extension) can permit an attacker to read/write a file that they originally did not have permissions to access.

## Cómo evitarlo

- Follow the principle of least privilege when assigning access rights to entities in a software system. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file. Ensure good compartmentalization in the system to provide protected areas that can be trusted.
