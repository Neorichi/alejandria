---
type: Artículo de enciclopedia
title: BREACH (ataque)
description: BREACH (un acrónimo de Reconocimiento de Browser y exfiltración mediante Compresión adaptable de hipertexto) es un exploit de seguridad HTTPS cuando se utiliza la compresión HTTP.
resource: https://es.wikipedia.org/wiki/BREACH_(ataque)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/BREACH_(ataque)"}
license: CC BY-SA 4.0
id: eswiki-BREACH_(ataque)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# BREACH (ataque)

**BREACH** (un acrónimo de Reconocimiento de Browser y exfiltración mediante Compresión adaptable de hipertexto) es un exploit de seguridad HTTPS cuando se utiliza la compresión HTTP. BREACH se construyó basándose en el exploit de seguridad CRIME. BREACH fue anunciado en la conferencia Black Hat de agosto de 2013 por los investigadores de seguridad Angelo Prado, Neal Harris y Yoel Gluck.

 Detalles
Si bien el ataque CRIME fue presentado como un ataque general que podría funcionar con eficacia contra un gran número de protocolos solo exploits contra compresión de solicitudes SPDY y compresión TLS fueron demostradas y en gran medida mitigadas en navegadores y servidores. El exploit CRIME contra la compresión HTTP no se ha mitigado en absoluto, a pesar de que los autores del crimen han advertido que esta vulnerabilidad podría ser aún más extendida que SPDY y compresión TLS combinados.

BREACH es una instancia del ataque CRIME contra la compresión HTTP - el uso por muchos navegador web y servidores web de algoritmos de compresión gzip o DEFLATE a través de la opción de la codificación de contenido dentro de HTTP. Dado este oráculo de compresión, el resto del ataque BREACH sigue las mismas líneas generales que el exploit CRIME, mediante la realización de una búsqueda inicial de fuerza bruta ciega para adivinar unos pocos bytes, seguido por una búsqueda de divide-y-vencerás para expandir un acierto a una gran cantidad de contenido arbitraria.

BREACH explota la compresión en el protocolo HTTP subyacente. Por lo tanto, la desactivación de la compresión TLS no hace ninguna diferencia a BREACH, que todavía puede realizar un ataque de texto plano escogido en contra de la carga útil de HTTP.

 Mitigación
Como resultado, los clientes y los servidores están obligados, ya sea a desactivar la compresión HTTP por completo, reduciendo el rendimiento, o a adoptar soluciones elaboradas para tratar de frustrar BREACH en escenarios de ataque individuales, como el uso de protección de falsificación de petición en sitios cruzados (CSRF).

Otro enfoque sugerido es desactivar la compresión HTTP cada vez que la cabecera indica una petición entre sitios cruzados, o cuando la cabecera no está presente. Este enfoque permite una mitigación eficaz del ataque sin perder funcionalidad, solo incurrir en una penalización de rendimiento en las solicitudes afectadas.

 Referencias

 Enlaces externos
 Herramienta que ejecuta el ataque BREACH demostrado en BlackHat 2013
