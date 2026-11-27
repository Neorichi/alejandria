---
type: Artículo de enciclopedia
title: Kismet
description: Kismet es un sniffer, un husmeador de paquetes, y un sistema de detección de intrusiones para redes inalámbricas 802.11.
resource: https://es.wikipedia.org/wiki/Kismet
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Kismet"}
license: CC BY-SA 4.0
id: eswiki-Kismet
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Kismet

- **Nombre:** Kismet
- **Desarrollador:** Mike Kershaw (dragorn)
- **Última versión:** Kismet-2019-09-R1[1]
- **Fecha última versión:** 2 de septiembre de 2019
- **Sistema operativo:** Linux
- **Género:** Sniffer
- **Licencia:** GNU General Public License

**Kismet** es un sniffer, un husmeador de paquetes, y un sistema de detección de intrusiones para redes inalámbricas 802.11. Kismet funciona con cualquier tarjeta inalámbrica que soporte el modo de monitorización raw, y puede rastrear tráfico 802.11b, 802.11a, 802.11g y 802.11n. El programa corre bajo Linux, FreeBSD, NetBSD, OpenBSD, y Mac OS X. El cliente puede también funcionar en Windows, aunque la única fuente entrante de paquetes compatible es otra sonda.

 Características

Kismet se diferencia de la mayoría de los otros sniffers inalámbricos en su funcionamiento pasivo. Es decir que lo hace sin enviar ningún paquete detectable, permitiendo detectar la presencia de varios puntos de acceso y clientes inalámbricos, asociando unos con otros.

Kismet también incluye características básicas de Sistemas de detección de intrusos como detectar programas de rastreo inalámbricos incluyendo a NetStumbler, así como también ciertos ataques de red inalámbricos.

 Servidor/sonda/infraestructura cliente

Kismet tiene tres partes diferenciadas:
 Una *sonda* que puede usarse para recoger paquetes, que son enviados a un *servidor* para su interpretación.
 Un servidor que puede o bien ser usado en conjunción con una sonda, o consigo mismo, interpretando los datos de los paquetes, extrapolando la información inalámbrica, y organizándola.
 El *cliente* se comunica con el servidor y muestra la información que el servidor recoge.

 Enlaces externos

 Sitio web oficial (en inglés).
