---
type: Tipo de fallo de software
title: "CWE-15: External Control of System or Configuration Setting"
description: One or more system settings or configuration elements can be externally controlled by a user.
resource: https://cwe.mitre.org/data/definitions/15.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/15.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-15
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-15: External Control of System or Configuration Setting

**Tipo de fallo de software CWE-15** (Base).

One or more system settings or configuration elements can be externally controlled by a user.

- **Es un caso de:** [CWE-642](/seguridad/cwe/CWE-642.md), [CWE-610](/seguridad/cwe/CWE-610.md), [CWE-20](/seguridad/cwe/CWE-20.md)

## Consecuencias

- Varies by Context: Allowing external control of system settings can disrupt service or cause an application to behave in unexpected, and potentially malicious ways.

## Cómo evitarlo

- Compartmentalize the system to have "safe" areas where trust boundaries can be unambiguously drawn. Do not allow sensitive data to go outside of the trust boundary and always be careful when interfacing with a compartment outside of the safe area. Ensure that appropriate compartmentalization is built into the system design, and the compartmentalization allows for and reinforces privilege separation functionality. Architects and designers should rely on the principle of least privilege to decide the appropriate time to use privileges and the time to drop privileges.
- Because setting manipulation covers a diverse set of functions, any attempt at illustrating it will inevitably be incomplete. Rather than searching for a tight-knit relationship between the functions addressed in the setting manipulation category, take a step back and consider the sorts of system values that an attacker should not be allowed to control.
- In general, do not allow user-provided or otherwise untrusted data to control sensitive values. The leverage that an attacker gains by controlling these values is not always immediately obvious, but do not underestimate the creativity of the attacker.
