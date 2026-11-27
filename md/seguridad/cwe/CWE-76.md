---
type: Tipo de fallo de software
title: "CWE-76: Improper Neutralization of Equivalent Special Elements"
description: The product correctly neutralizes certain special elements, but it improperly neutralizes equivalent special elements.
resource: https://cwe.mitre.org/data/definitions/76.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/76.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-76
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-76: Improper Neutralization of Equivalent Special Elements

**Tipo de fallo de software CWE-76** (Base).

The product correctly neutralizes certain special elements, but it improperly neutralizes equivalent special elements.

The product may have a fixed list of special characters it believes is complete. However, there may be alternate encodings, or representations that also have the same meaning. For example, the product may filter out a leading slash (/) to prevent absolute path names, but does not account for a tilde (~) followed by a user name, which on some *nix systems could be expanded to an absolute pathname. Alternately, the product might filter a dangerous "-e" command-line switch when calling an external program, but it might not account for "--exec" or other switches that have the same semantics.

- **Es un caso de:** [CWE-75](/seguridad/cwe/CWE-75.md)

## Consecuencias

- Other

## Cómo evitarlo

- Programming languages and supporting technologies might be chosen which are not subject to these issues.
- Utilize an appropriate mix of allowlist and denylist parsing to filter equivalent special element syntax from all input.
