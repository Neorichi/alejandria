---
type: Tipo de fallo de software
title: "CWE-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component"
description: The product constructs all or part of a command, data structure, or record using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could m
resource: https://cwe.mitre.org/data/definitions/74.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/74.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-74
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component

**Tipo de fallo de software CWE-74** (Class).

The product constructs all or part of a command, data structure, or record using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify how it is parsed or interpreted when it is sent to a downstream component.

- **Es un caso de:** [CWE-707](/seguridad/cwe/CWE-707.md)

## Consecuencias

- Read Application Data: Many injection attacks involve the disclosure of important information -- in terms of both data sensitivity and usefulness in further exploitation.
- Bypass Protection Mechanism: In some cases, injectable code controls authentication; this may lead to a remote vulnerability.
- Alter Execution Logic: Injection attacks are characterized by the ability to significantly change the flow of a given process, and in some cases, to the execution of arbitrary code.
- Other: Data injection attacks lead to loss of data integrity in nearly all cases as the control-plane data injected is always incidental to data recall or writing.
- Hide Activities: Often the actions performed by injected control code are unlogged.

## Cómo evitarlo

- Programming languages and supporting technologies might be chosen which are not subject to these issues.
- Utilize an appropriate mix of allowlist and denylist parsing to filter control-plane syntax from all input.
