---
type: Artículo de enciclopedia
title: Firma con agregación
description: "Un sistema de firma con agregación es un sistema que genera firmas digitales que permiten ser agregadas en el sentido de que dadas n firmas sobre n mensajes distintos provenientes de n usuarios distintos, permiten …"
resource: https://es.wikipedia.org/wiki/Firma_con_agregación
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Firma_con_agregación"}
license: CC BY-SA 4.0
id: eswiki-Firma_con_agregación
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Firma con agregación

Un sistema de **firma con agregación** es un sistema que genera firmas digitales que permiten ser agregadas en el sentido de que dadas n firmas sobre n mensajes distintos provenientes de n usuarios distintos, permiten **agregar** todos ellos en una sola firma. Con esta firma y todos los mensajes originales se podrá convencer a cualquier verificador que n usuarios firmaron los n mensajes originales donde el usuario i firmó el mensaje i. Esta propiedad es muy útil para comprimir las cadenas de firmas que se usan por ejemplo en las cadenas de certificación de las PKI o en las cadenas de firmas usadas en la versión segura del protocolo de enrutado BGP (SBGP).

Categorización
Cuando la agregación puede realizarse por cualquiera y sin la cooperación de los firmantes se dice que es un **esquema de firma de agregación general**. En algunos sistemas la agregación de firma sólo puede realizarse durante el proceso de firmado de forma que cada firmante en su turno secuencialmente añade su firma a la agregación actual. A estos últimos sistemas se les llama **esquema de firma de agregación secuencial**.

Ejemplos
Ejemplos de firma con este tipo de propiedad son:
Esquema de Boneh, Gentry, Lynn y Shacham que usa mapas bilineales. Es un **esquema de firma de agregación general**.
Esquema basado en el esquema de firma multifirma de Silvio Micali y otros. Es un **esquema de firma de agregación secuencial**.

Referencias
