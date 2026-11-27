---
type: Tipo de fallo de software
title: "CWE-61: UNIX Symbolic Link (Symlink) Following"
description: The product, when opening a file or directory, does not sufficiently account for when the file is a symbolic link that resolves to a target outside of the intended control sphere. This could allow an attacker to cause th
resource: https://cwe.mitre.org/data/definitions/61.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/61.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-61
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-61: UNIX Symbolic Link (Symlink) Following

**Tipo de fallo de software CWE-61** (Compound).

The product, when opening a file or directory, does not sufficiently account for when the file is a symbolic link that resolves to a target outside of the intended control sphere. This could allow an attacker to cause the product to operate on unauthorized files.

- **Es un caso de:** [CWE-59](/seguridad/cwe/CWE-59.md)

## Consecuencias

- Read Files or Directories: A product that allows a symbolic link (symlink) as part of a path - whether in internal code or through user input - can allow an attacker to spoof the symbolic link and traverse the file system to unintended locations or access arbitrary files. An attacker could read, write, or /corrupt a file that they originally did not have permissions to access directly.

## Cómo evitarlo

- Symbolic link attacks often occur when a program creates a tmp directory that stores files/links. Access to the directory should be restricted to the program as to prevent attackers from manipulating the files.
- Follow the principle of least privilege when assigning access rights to entities in a software system. Denying access to a file can prevent an attacker from replacing that file with a link to a sensitive file. Ensure good compartmentalization in the system to provide protected areas that can be trusted.
