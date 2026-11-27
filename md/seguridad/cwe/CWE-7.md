---
type: Tipo de fallo de software
title: "CWE-7: J2EE Misconfiguration: Missing Custom Error Page"
description: The product has a J2EE component that does not have a custom error page.
resource: https://cwe.mitre.org/data/definitions/7.html
tags: [seguridad, cwe]
sources:
  - {"id": "mitre-cwe", "resource": "https://cwe.mitre.org/data/definitions/7.html", "title": "MITRE CWE 5.0", "author": "org:mitre", "last_modified": "2026-10-28T00:00:00Z"}
license: "© The MITRE Corporation. CWE: uso libre con esta atribución (cwe.mitre.org/about/termsofuse.html)."
id: cwe-7
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:49Z"}
status: stable
stale_after: 2027-11-27T17:14:49Z
---

# CWE-7: J2EE Misconfiguration: Missing Custom Error Page

**Tipo de fallo de software CWE-7** (Variant).

The product has a J2EE component that does not have a custom error page.

- **Es un caso de:** [CWE-756](/seguridad/cwe/CWE-756.md)

## Consecuencias

- Read Application Data: When an attacker explores a web site looking for vulnerabilities, the amount of information that the site provides is crucial to the eventual success or failure of any attempted attacks. A stack trace might show the attacker a malformed SQL query string, the type of database being used, and the version of the application container. This information enables the attacker to target known vulnerabilities in these components.

## Cómo evitarlo

- Handle exceptions appropriately in source code. Catch java.lang.Throwable exceptions to prevent attackers from mining information from the application container's built-in error response.
- Always define appropriate error pages, including for 4xx errors (e.g. 404) and 5xx (e.g. 500) errors. The application configuration should specify a default error page in order to guarantee that the application will never leak error messages to an attacker. Handling standard HTTP error codes is useful and user-friendly in addition to being a good security practice, and a good configuration will also define a last-chance error handler that catches any exception that could possibly be thrown by the application.
- Do not attempt to process an error or attempt to mask it.
- Verify return values are correct and do not supply sensitive information about the system.
