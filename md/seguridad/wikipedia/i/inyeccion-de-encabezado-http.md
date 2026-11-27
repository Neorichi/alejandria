---
type: Artículo de enciclopedia
title: Inyección de encabezado HTTP
description: "La Inyección de encabezado HTTP es una clase general de vulnerabilidad de seguridad de aplicaciones web que se produce cuando los encabezados del Protocolo de transferencia de hipertexto (HTTP) se generan dinámicamente …"
resource: https://es.wikipedia.org/wiki/Inyección_de_encabezado_HTTP
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Inyección_de_encabezado_HTTP"}
license: CC BY-SA 4.0
id: eswiki-Inyección_de_encabezado_HTTP
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Inyección de encabezado HTTP

La **Inyección de encabezado HTTP** es una clase general de vulnerabilidad de seguridad de aplicaciones web que se produce cuando los encabezados del Protocolo de transferencia de hipertexto (HTTP) se generan dinámicamente en función de la entrada del usuario. La inyección de cabeceras en las respuestas HTTP puede permitir la división de respuestas HTTP (también conocido como HTTP response splitting), la fijación de sesión a través del encabezado Set-Cookie, cross-site scripting (XSS), y los ataques de redireccionamiento maliciosos a través de la cabecera de ubicación. La inyección de encabezado HTTP es un área relativamente nueva para los ataques basados en la web, y principalmente ha sido promovida por Amit Klein en su trabajo sobre requerimiento/respuesta contrabando/división. Las vulnerabilidades debido a inyecciones de cabecera HTTP tales como CRLF ya no son factibles debido al hecho de que múltiples solicitudes de cabecera no son posibles.

 Referencias

 Enlaces externos
 Scanner Open Source Wapiti de inyecciones de encabezado, XSS, SQL y LDAP
