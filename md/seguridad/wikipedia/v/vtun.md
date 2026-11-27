---
type: Artículo de enciclopedia
title: VTun
description: VTun es una aplicación de red que puede configurar túneles virtuales a través de redes TCP/IP.
resource: https://es.wikipedia.org/wiki/VTun
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/VTun"}
license: CC BY-SA 4.0
id: eswiki-VTun
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# VTun

**VTun** es una aplicación de red que puede configurar túneles virtuales a través de redes TCP/IP. Admite los protocolos Protocolo de Internet (IP), Protocolo punto a punto (PPP) y el *Serial Line Internet Protocol* (SLIP). Existe como la implementación de referencia del controlador de túnel de espacio de usuario Tun/Tap que se incluyó en el kernel de Linux a partir de la versión 2.4, también desarrollado originalmente por Maxim Krasnyansky. Clark es el mantenedor actual.

 Redes
Como la mayoría de las otras aplicaciones de su naturaleza, VTun crea una conexión única entre dos máquinas, sobre la cual multiplexa todo el tráfico. Las conexiones VTun se inician a través de una conexión TCP desde el cliente al servidor. Luego, el servidor inicia una conexión UDP con el cliente, si se solicita el protocolo UDP.

El software permite la creación de túneles para enrutar el tráfico de manera similar a PPP, así como una conexión ethertap compatible con puentes.

 Versiones sin cifrado
Una fuente continua de preocupación, y el objetivo de más de una evaluación de seguridad fuertemente redactada, es que las aplicaciones binarias del cliente y del servidor VTun pueden construirse completamente sin soporte de cifrado. Cuando se utilizan dichos binarios, el cifrado entre ambos puntos finales es solo un cifrado XOR simple, que es completamente trivial de decodificar. Los desarrolladores no admiten este tipo de compilación.

 Referencias

 Enlaces externos
