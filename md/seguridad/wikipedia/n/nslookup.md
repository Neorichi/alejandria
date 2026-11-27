---
type: Artículo de enciclopedia
title: Nslookup
description: Nslookup es un programa informático utilizado para saber si el Sistema de nombres de dominio (DNS) está resolviendo correctamente los dominios de internet y las direcciones IP.
resource: https://es.wikipedia.org/wiki/Nslookup
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Nslookup"}
license: CC BY-SA 4.0
id: eswiki-Nslookup
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Nslookup

**Nslookup** es un programa informático utilizado para saber si el Sistema de nombres de dominio (DNS) está resolviendo correctamente los dominios de internet y las direcciones IP. Se utiliza con el comando nslookup, que funciona tanto en Windows como en UNIX para obtener la dirección IP conociendo el nombre, y viceversa.

Nslookup permite que el usuario consulte de forma manual los servidores de nombres para resolver un nombre de host dado. Esta utilidad también puede utilizarse para solucionar los problemas de resolución de nombres y verificar el estado actual de los servidores de nombres.

 Ejemplos
Al preguntar quién es «es.wikipedia.org» se obtiene:

 nslookup es.wikipedia.org
 Server:         192.168.1.1
 Address:        192.168.1.1

 Non-authoritative answer:
 Name:   es.wikipedia.org
 Address: **66.230.200.100**

Al preguntarle quién es "66.230.200.100" se obtiene:

 > 66.230.200.100
 Server:		10.1.232.18
 Address:	10.1.232.18:53

 Non-authoritative answer:
 100.200.230.66.in-addr.arpa	canonical name = 100.200.230.66.rev.wikimedia.org.
 100.200.230.66.rev.wikimedia.org	name = rr.pmtpa.wikimedia.org.
