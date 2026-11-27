---
type: Artículo de enciclopedia
title: Ping de la muerte
description: El ataque ping de la muerte es uno de los ataques de red más antiguos.
resource: https://es.wikipedia.org/wiki/Ping_de_la_muerte
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ping_de_la_muerte"}
license: CC BY-SA 4.0
id: eswiki-Ping_de_la_muerte
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ping de la muerte

El ataque **ping de la muerte** es uno de los ataques de red más antiguos. El principio de este ataque consiste simplemente en crear un datagrama IP cuyo tamaño total supere el máximo autorizado ( bytes). Cuando un paquete con estas características se envía a un sistema que contiene una pila vulnerable de protocolos TCP/IP, este produce la caída del sistema. Los sistemas más modernos ya no son vulnerables a este tipo de ataque. El tamaño excesivo de bytes impide que la máquina lo procese de manera efectiva, afectando el entorno en la nube y causando interrupciones en los procesos del sistema operativo, lo que puede resultar en reinicios o bloqueos.

En este ataque, un host envía cientos de solicitudes de ping con un tamaño de paquete grande o ilegal a otro host para intentar desconectarlo o mantenerlo preocupado respondiendo con respuestas ICMP Echo de que ignora a sus clientes.

 Resumen
Los atacantes comenzaron a aprovecharse de esta vulnerabilidad en los sistemas operativos (SO) en 1996, y en 1997 fue corregida por la mayoría de los SO por lo que este tipo de ataque no debería tener efecto sobre los SO actuales.

Es un tipo de ataque a computadoras que implica enviar un ping deformado a una computadora. Un ping normalmente tiene un tamaño de 64 bytes; algunos sistemas operativos no podían manejar pings mayores al máximo de un paquete IP común, que es de  bytes. Enviando pings de este tamaño era posible hacer que esas computadoras dejaran de funcionar.

Este fallo fue fácil de usar. Si bien, enviar un paquete de "Ping de la Muerte" de un tamaño de  bytes es inválido según los protocolos de establecimiento de una red, se puede enviar un paquete de tal tamaño si se hacen fragmentos del mismo. Así, cuando la computadora que es el blanco de ataque vuelve a montar el paquete, puede ocurrir una saturación del *buffer*, lo que a menudo produce como consecuencia un fallo del sistema.

 Historia
Esta vulnerabilidad ha afectado a la mayoría de sistemas operativos, como Unix, Linux, Mac, Windows, a impresoras y a los routers.

En enero de 2007 fue anunciado un parche de seguridad para Solaris 10 que evita un kernel panic ocasionado por medio del envío de una falsa solicitud ICMP. En la descripción técnica del problema indica que se podía realizar con una utilería como ping.

En agosto de 2013 la empresa Microsoft anunció un parche de seguridad para un ping de la muerte en protocolo ICMPv6 para todas las versiones del sistema operativo Windows, excepto para Windows XP y Windows Server 2012 (este último afectado solo en modo NAT). También en ese mismo mes Microsoft anunció otro parche de seguridad el cual permitió corregir que, por medio de una variante de ataque ping, se produjera un ataque de denegación de servicio.

No obstante la mayoría de los sistemas operativos desde 1997–1998 han arreglado este problema, por lo cual el fallo es prácticamente inexistente.

En la actualidad otro tipo de ataques con ping han llegado a ser muy utilizados, como por ejemplo el *ping flooding*.

 Véase también

....
 Referencias

 Enlaces externos
 ¿Qué es el Ping de la Muerte?
 (en inglés) Ping of death según insecure.org
  L'attaque "ping of death"
 (en inglés) How To Perform Ping of Death Attack Using CMD And Notepad (Just For Learning)
  O que é o "Ping da Morte"?
