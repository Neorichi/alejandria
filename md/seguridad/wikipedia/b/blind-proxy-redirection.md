---
type: Artículo de enciclopedia
title: Blind proxy redirection
description: "Blind proxy redirection (BPR) consiste en el uso de sistemas intermedios como redirectores (proxys inversos) que tunelan de forma transparente peticiones y datos hacia y desde servidores de backend que son los que …"
resource: https://es.wikipedia.org/wiki/Blind_proxy_redirection
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Blind_proxy_redirection"}
license: CC BY-SA 4.0
id: eswiki-Blind_proxy_redirection
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Blind proxy redirection

**Blind proxy redirection** (**BPR**)  consiste en el uso de sistemas intermedios como redirectores (proxys inversos) que tunelan de forma transparente peticiones y datos hacia y desde servidores de backend que son los que realmente sirven el contenido.

Esta técnica ha sido usada en el mundo de los servidores web con el propósito de mantener una alta disponibilidad y distribuir la carga (redes de distribución de contenidos). Sin embargo, su uso más habitual es en el mundo de los ciberseguridad para eludir intentos de rastreo y anulación de redes usadas en ciberataques. En este contexto se suele tener un gran grupo de direcciones IP, habitualmente de equipos comprometidos o bots cuyos propietarios no saben que están realizando esta acción, que se van registrando y desregistrado en DNS (Fast Flux), proporcionando una o varias capas de redirección, y que tunelan las comunicaciones con servidores desde los que se desarrolla el ataque (servidores C&C, servidores que descarga de malware,...).

Referencias
