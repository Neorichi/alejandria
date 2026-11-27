---
type: Artículo de enciclopedia
title: Apropiación de formulario
description: "La apropiación de formulario, en inglés form grabbing, es un método que usan algunos malware para robar información que es introducida en formularios web. Consiste en incerceptar la información del formulario antes de …"
resource: https://es.wikipedia.org/wiki/Apropiación_de_formulario
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Apropiación_de_formulario"}
license: CC BY-SA 4.0
id: eswiki-Apropiación_de_formulario
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Apropiación de formulario

La **apropiación de formulario**, en inglés *form grabbing*, es un método que usan algunos malware para robar información que es introducida en formularios web. Consiste en incerceptar la información del formulario antes de que sea manda a Internet usado datos GET/POST.

Para capturar la información usa dos métodos básicos:
Se obtiene todos los datos GET/POST salientes utilizando PCAP (captura de paquetes).Esta técnica solo funciona para la comunicación sin cifrar (no HTTPs).
Malware residente en la máquina de la víctima se engancha a las librerías dinámicas del navegador para robar el contenido antes de que sea enviado al servidor. De esta forma el contenido puede ser robado antes de que sea encriptado. Este mecanismo puede ser logrado mediante una variedad de mecanismos como por ejemplo un complemento malicioso para navegador. malicioso.

Es especialmente utilizado para extraer información del navegador de la víctima cuando tiene una sesión activa en el sitio web de un banco. También es muy usado para capturar credenciales para autorización.

Esta técnica es muy utilizada. Por ejemplo, es utilizada en LatenBot, Zeus y SpyEye.

 Referencias
