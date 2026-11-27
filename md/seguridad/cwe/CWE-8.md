---
type: Tipo de fallo de software
title: "CWE-8: J2EE Misconfiguration: Entity Bean Declared Remote"
description: "The J2EE application exposes a remote interface for an entity bean, but it also exposes methods that get or set the bean's data."
resource: https://cwe.mitre.org/data/definitions/8.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/8.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-8
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-8: J2EE Misconfiguration: Entity Bean Declared Remote

**Tipo de fallo de software CWE-8** (Variant).

The J2EE application exposes a remote interface for an entity bean, but it also exposes methods that get or set the bean's data.

- **Es un caso de:** [CWE-668](/seguridad/cwe/CWE-668.md)

## Consecuencias

- Read Application Data: These methods could be leveraged to read sensitive information, or to change data in ways that violate the application's expectations, potentially leading to other vulnerabilities.

## Cómo evitarlo

- Declare Java beans "local" when possible. When a bean must be remotely accessible, make sure that sensitive information is not exposed, and ensure that the application logic performs appropriate validation of any data that might be modified by an attacker.
