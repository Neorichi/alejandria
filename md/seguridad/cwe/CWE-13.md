---
type: Tipo de fallo de software
title: "CWE-13: ASP.NET Misconfiguration: Password in Configuration File"
description: Storing a plaintext password in a configuration file allows anyone who can read the file access to the password-protected resource making them an easy target for attackers.
resource: https://cwe.mitre.org/data/definitions/13.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/13.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-13
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-13: ASP.NET Misconfiguration: Password in Configuration File

**Tipo de fallo de software CWE-13** (Variant).

Storing a plaintext password in a configuration file allows anyone who can read the file access to the password-protected resource making them an easy target for attackers.

- **Es un caso de:** [CWE-260](/seguridad/cwe/CWE-260.md)

## Consecuencias

- Gain Privileges or Assume Identity

## Cómo evitarlo

- Credentials stored in configuration files should be encrypted, Use standard APIs and industry accepted algorithms to encrypt the credentials stored in configuration files.
