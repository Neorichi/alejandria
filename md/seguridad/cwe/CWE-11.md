---
type: Tipo de fallo de software
title: "CWE-11: ASP.NET Misconfiguration: Creating Debug Binary"
description: The product has an ASP .NET component that contains a debug binary.
resource: https://cwe.mitre.org/data/definitions/11.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/11.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-11
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-11: ASP.NET Misconfiguration: Creating Debug Binary

**Tipo de fallo de software CWE-11** (Variant).

The product has an ASP .NET component that contains a debug binary.

- **Es un caso de:** [CWE-489](/seguridad/cwe/CWE-489.md)

## Consecuencias

- Read Application Data: Debug binaries give detailed debugging messages, which is useful in a development or testing environment, but can pose a security risk if the debug binary is deployed to production. Attackers can leverage the additional information they gain from debugging output to mount attacks targeted on the framework, database, or other resources used by the application.

## Cómo evitarlo

- Avoid releasing debug binaries into the production environment. Change the debug mode to false when the application is deployed into production.
