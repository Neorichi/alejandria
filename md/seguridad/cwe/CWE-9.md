---
type: Tipo de fallo de software
title: "CWE-9: J2EE Misconfiguration: Weak Access Permissions for EJB Methods"
description: If elevated access rights are assigned to EJB methods, then an attacker can take advantage of the permissions to exploit the product.
resource: https://cwe.mitre.org/data/definitions/9.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/9.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-9
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-9: J2EE Misconfiguration: Weak Access Permissions for EJB Methods

**Tipo de fallo de software CWE-9** (Variant).

If elevated access rights are assigned to EJB methods, then an attacker can take advantage of the permissions to exploit the product.

If the EJB deployment descriptor contains one or more method permissions that grant access to the special ANYONE role, it indicates that access control for the application has not been fully thought through or that the application is structured in such a way that reasonable access control restrictions are impossible.

- **Es un caso de:** [CWE-266](/seguridad/cwe/CWE-266.md)

## Consecuencias

- Other

## Cómo evitarlo

- Follow the principle of least privilege when assigning access rights to EJB methods. Permission to invoke EJB methods should not be granted to the ANYONE role.
