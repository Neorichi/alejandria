---
type: Tipo de fallo de software
title: "CWE-5: J2EE Misconfiguration: Data Transmission Without Encryption"
description: The product uses J2EE with a configuration that transmits data without encryption.
resource: https://cwe.mitre.org/data/definitions/5.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/5.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-5
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-5: J2EE Misconfiguration: Data Transmission Without Encryption

**Tipo de fallo de software CWE-5** (Variant).

The product uses J2EE with a configuration that transmits data without encryption.

- **Es un caso de:** [CWE-319](/seguridad/cwe/CWE-319.md)

## Consecuencias

- Read Application Data: An attacker may be able to read the data sent in plaintext.
- Modify Application Data: Information sent over a network can be compromised while in transit. An attacker may be able to modify the contents of data sent in plaintext.

## Cómo evitarlo

- The product configuration should ensure that SSL or an encryption mechanism of equivalent strength and vetted reputation is used for all access-controlled pages.
