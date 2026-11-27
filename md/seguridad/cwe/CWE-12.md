---
type: Tipo de fallo de software
title: "CWE-12: ASP.NET Misconfiguration: Missing Custom Error Page"
description: "An ASP .NET application must enable custom error pages in order to prevent attackers from mining information from the framework's built-in responses."
resource: https://cwe.mitre.org/data/definitions/12.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/12.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-12
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-12: ASP.NET Misconfiguration: Missing Custom Error Page

**Tipo de fallo de software CWE-12** (Variant).

An ASP .NET application must enable custom error pages in order to prevent attackers from mining information from the framework's built-in responses.

- **Es un caso de:** [CWE-756](/seguridad/cwe/CWE-756.md)

## Consecuencias

- Read Application Data: Default error pages gives detailed information about the error that occurred, and should not be used in production environments. Attackers can leverage the additional information provided by a default error page to mount attacks targeted on the framework, database, or other resources used by the application.

## Cómo evitarlo

- Handle exceptions appropriately in source code. ASP .NET applications should be configured to use custom error pages instead of the framework default page.
- Do not attempt to process an error or attempt to mask it.
- Verify return values are correct and do not supply sensitive information about the system.
