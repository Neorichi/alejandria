---
type: Artículo de enciclopedia
title: Escáner de vulnerabilidades
description: Un escáner de vulnerabilidades es una aplicación diseñada para realizar análisis automáticos de cualquier aplicación, sistema o red en busca de cualquier posible vulnerabilidad.
resource: https://es.wikipedia.org/wiki/Escáner_de_vulnerabilidades
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Escáner_de_vulnerabilidades"}
license: CC BY-SA 4.0
id: eswiki-Escáner_de_vulnerabilidades
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Escáner de vulnerabilidades

Un **escáner de vulnerabilidades** es una aplicación diseñada para realizar análisis automáticos de cualquier aplicación, sistema o red en busca de cualquier posible vulnerabilidad. Aunque estas aplicaciones no son capaces de detectar la vulnerabilidad con total precisión, sí son capaces de detectar ciertos elementos que podrían desencadenar en una vulnerabilidad, facilitando enormemente el trabajo a los investigadores e ingenieros. Es frecuente hacer escaneos de vulnerabilidades desde la red interna, para ver que se puede hacer una vez que se tiene acceso a la intranet, o desde red externa, para ver las posibilidades que tiene un atacante externo para atacar nuestros sistemas.

Los escáner de vulnerabilidades está compuesto por otras herramientas para funcionalidades más específicas, como pueden ser pruebas de fuerza bruta o con diccionarios de contraseñas (Ej. Patator, Medussa y Hydra), fuzzers para descubrir dominios no bloqueados a usuarios sin autenticar o escáneres de puertos.

Tradicionalmente el software era necesario instalar en una máquina. Sin embargo hoy día muchos escáneres de vulnerabilidades están dando sus servicios como SaaS. Por ejemplo HTTPCS o Acunetix siguen este modo de explotación.

Los escáneres de vulnerabilidades deberían poder detectar los riesgos en las dependencias de código abierto. Sin embargo, dado que los desarrolladores suelen volver a empaquetar el OSS, el mismo código aparecerá en diferentes dependencias, lo que afectará el rendimiento y la capacidad de los escáneres para detectar el OSS vulnerable.

Clasificación
Se pueden clasificar según el tipo de vulnerabilidades en los que está especializado:
Escáner de vulnerabilidades de red. Por ejemplo Nessus, Qualys, Acunetix, OpenVAS, HTTPCS, Nexpose o Nmap con scripts (*Nmap Scripting Engine Scripts*) para el análisis de vulnerabilidades. Para la propia red de acceso Aircrack-ng es una buena herramienta para poner a prueba la seguridad de cualquier red Wi-Fi en busca de cualquier posible vulnerabilidad que pueda permitir a cualquier usuario no autorizado hacerse con la contraseña de nuestra red
Escáner de vulnerabilidades de aplicaciones web: . Por ejemplo Nikto, Qualys, OWASP Zed Attack Proxy (ZAP), w3af, Burp Suite, Uniscan.
Escáner  de  vulnerabilidades  de  bases  de  datos: Scuba, AppDetectivePro, McAfee Vulnerability Manager for Databases, AuditPro Enterprise, Microsoft Baseline Security Analyzer.

Por otro lado hay herramientas, como Seccubus que son una recopilación de escáneres de vulnerabilidades y nos permite automatizar todos los análisis de manera que desde esta única aplicación podamos realizar un análisis lo más profundo posible.

Referencias

 Enlaces externos

 Escáner de vulnerabilidades - Seguridad en la informática
