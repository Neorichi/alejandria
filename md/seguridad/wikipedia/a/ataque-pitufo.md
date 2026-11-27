---
type: Artículo de enciclopedia
title: Ataque pitufo
description: "El ataque pitufo o ataque smurf es un ataque de denegación de servicio en una red informática que utiliza mensajes de ping a la dirección de difusión (broadcast) con suplantación de identidad (spoofing) para inundar …"
resource: https://es.wikipedia.org/wiki/Ataque_pitufo
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataque_pitufo"}
license: CC BY-SA 4.0
id: eswiki-Ataque_pitufo
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataque pitufo

El **ataque pitufo** o **ataque *smurf*** es un ataque de denegación de servicio en una red informática que utiliza mensajes de *ping* a la dirección de difusión (*broadcast*) con suplantación de identidad (*spoofing*) para inundar (*flood*) un objetivo (sistema atacado).

En este tipo de ataque, el perpetrador envía grandes cantidades de tráfico ICMP (*ping*) a la dirección de *broadcast* de la víctima, todos ellos portando una dirección de origen falsificada (*spoofing*), simulando haber sido enviado por la propia víctima. El dispositivo de ruteo envía el tráfico de mensajes ICMP de ***echo request***  a esas direcciones de *broadcast* (lo hace en la capa 2 donde está la función de *broadcast*) y la mayoría de los equipos (*hosts*) lo responderán, multiplicando el tráfico por cada *host* de la subred. En las redes que ofrecen múltiples accesos a *broadcast*, potencialmente miles de máquinas responderán a cada paquete. Todas esas respuestas las recibe el equipo con la IP de origen falsificada, un equipo de la víctima atacada, saturándolo.

Algunos años atrás, todas las redes enrutaban ataques *smurf* -coloquialmente se dice que eran «*smurfeables*»-. Hoy día, la mayoría de los administradores han inmunizado sus redes contra estos abusos, aunque muchas redes permanecen «smurfeables».

Para evitar la recepción de paquetes IP cuya dirección de destino es una dirección de difusión válida para alguna subred de IP, pero que se origina en un nodo que no es parte de esa subred de destino, se puede ejecutar el comando no ip directed-broadcast en enrutadores marca Cisco.

*Smurfs* hace referencia a los personajes de ficción Los Pitufos.

Véase también
 Flood (Término informático)

Enlaces externos

Noticia oficial del CERRT sobre ataques DoS de Smurf
Lo último en ataques de denegación de servicio: "Smurfing" Descripción e información para minimizar efectos
Definición de Smurf
Ataques Dos en Unix. Recomendaciones generales del Stack IP
Definición de ataques Smurf, Ataques Fraggle, Spoofing, Ataques SYN
