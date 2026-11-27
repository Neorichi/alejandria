---
type: Tipo de fallo de software
title: "CWE-6: J2EE Misconfiguration: Insufficient Session-ID Length"
description: The J2EE application is configured to use an insufficient session ID length.
resource: https://cwe.mitre.org/data/definitions/6.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/6.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-6
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-6: J2EE Misconfiguration: Insufficient Session-ID Length

**Tipo de fallo de software CWE-6** (Variant).

The J2EE application is configured to use an insufficient session ID length.

- **Es un caso de:** [CWE-334](/seguridad/cwe/CWE-334.md)

## Consecuencias

- Gain Privileges or Assume Identity: A short session identifier leaves the application open to brute-force session guessing attacks. If an attacker can guess an authenticated user's session identifier, they can take over the user's session (called session hijacking).

## Cómo evitarlo

- Session identifiers should have enough bits of entropy to make it more difficult to perform brute-force session guessing. The number of possible session IDs increases with increased session ID length, making it more difficult to guess or steal a session ID.
- A lower bound on the number of valid session identifiers that are available to be guessed is the number of users that are active on a site at any given moment. However, any users that abandon their sessions without logging out will increase this number. (This is one of many good reasons to have a short inactive session timeout.) With a 64 bit session identifier, assume 32 bits of entropy. For a large web site, assume that the attacker can try 1,000 guesses per second and that there are 10,000 valid session identifiers at any given moment. Given these assumptions, the expected time for an attacker to successfully guess a valid session identifier is less than 4 minutes. Now assume a 128 bit session identifier that provides 64 bits of entropy. With a very large web site, an attacker might try 10,000 guesses per second with 100,000 valid session identifiers available to be guessed. Given these assumptions, the expected time for an attacker to successfully guess a valid session identifier is greater than 292 years.
