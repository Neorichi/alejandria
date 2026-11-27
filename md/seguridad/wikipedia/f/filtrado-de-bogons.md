---
type: Artículo de enciclopedia
title: Filtrado de bogons
description: El filtrado de Bogons es la práctica de filtrar bogons, que son direcciones IP falsas.
resource: https://es.wikipedia.org/wiki/Filtrado_de_bogons
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Filtrado_de_bogons"}
license: CC BY-SA 4.0
id: eswiki-Filtrado_de_bogons
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Filtrado de bogons

El **filtrado de Bogons** es la práctica de filtrar bogons, que son direcciones IP falsas. Bogon también es un nombre informal para un paquete IP en la Internet pública que dice ser de un área del espacio de direcciones IP reservadas, pero aún no asignadas o delegadas por la Internet Assigned Numbers Authority (IANA) o por un Registro Regional de Internet delegado (RIR). Las áreas de espacio de direcciones sin asignar se llaman *el espacio Bogon*.

Bogons también incluye los rangos reservados de direcciones privadas y rangos de Dirección de Enlace-Local, como los segmentos 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 y 169.254.0.0/16, que se reservan para uso de redes privadas.

Muchos proveedores de Internet y cortafuegos de usuarios finales filtran y bloquean bogons, porque no tienen uso legítimo, y por lo general son el resultado de una mala configuración accidental o maliciosa. Los bogons se pueden filtrar mediante el uso de las ACL en routers, o por BGP blackholing.

Las direcciones IP que se encuentran actualmente en el espacio Bogon pueden no ser bogons en una fecha posterior porque IANA y otros registros con frecuencia asignan nuevos espacios de direcciones a ISPs. Anuncios de nuevas asignaciones se publican a menudo en las listas de correo operadores de red (como NANOG) para garantizar que los operadores tengan la posibilidad de eliminar el filtrado Bogon para las direcciones que se han convertido en legítimas.

Por ejemplo, las direcciones en 49.0.0.0/8 no se asignaron antes de agosto de 2010, pero ahora son utilizados por APNIC. A medida que pasa el tiempo, el agotamiento de las direcciones IPv4 implica que hay menos y menos bogons IPv4.

IANA mantiene una lista de bloques de red IPv4 asignados y reservados.

A partir de noviembre de 2011, el IETF recomienda que los filtros Bogon para bloques de red no utilizados previamente IPv4 / 8 deben ser removidos, ya que todos han sido asignados.

 Etimología
El término *Bogon* proviene de la jerga hacker, donde se define como el cuanto de la *bogosidad*, o la propiedad de ser falso. Un paquete Bogon es con frecuencia falso tanto en el sentido convencional de ser forjado con fines ilegítimos, y en el sentido hacker de ser incorrecto, absurdo e inútil. Consulte "bogodynamics Quantum".

 Véase también
 Filtrado de rutas
 Reverse path forwarding
 IP spoofing

 Referencias

Enlaces externos
 IANA IPv4 Address Space
 RFC 1918 – *"Address Allocation for Private Internets"*
 The Team Cymru Bogon Reference Page
 Bogons Ate My Website
 Bogon traffic analysis report, netflow and spam analysis
 RIPE NCC: De-Bogonising New Address Blocks
