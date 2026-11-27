---
type: Artículo de enciclopedia
title: PF (software)
description: "PF (Packet Filter) es el filtro de paquetes o cortafuegos basado en configuración dinámica (stateful rules) escrito originalmente por Daniel Hartmeier actualmente desarrollado y mantenido por el equipo de desarrollo de …"
resource: https://es.wikipedia.org/wiki/PF_(software)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/PF_(software)"}
license: CC BY-SA 4.0
id: eswiki-PF_(software)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# PF (software)

**PF** (***Packet Filter***) es el filtro de paquetes o cortafuegos basado en configuración dinámica (*stateful rules*) escrito originalmente por Daniel Hartmeier actualmente desarrollado y mantenido por el equipo de desarrollo de OpenBSD. Es funcionalmente comparable a otras soluciones de filtrado de paquetes, como iptables, ipfw e ipfilter.

Fue publicado a finales de 2001, en OpenBSD 3.0, como reemplazo de IPFilter, el filtro de paquetes de Darren Reed, debido a algunos problemas con la licencia de dicho software, ya que su autor tenía que dar autorización a los desarrolladores de OpenBSD para modificar el código.

Theo de Raadt, el líder de OpenBSD, dijo cuando se eliminó el IPFilter que "*el software que OpenBSD utiliza y distribuye debe ser libre para todos (tanto usuarios como compañías), para cualquier fin que quiera dársele, incluyendo su modificación, uso*". Debido a la incomodidad del equipo de OpenBSD con la licencia de Reed, se optó por reemplazar todo el paquete antes que perder más tiempo intentando negociar la cuestión.

PF se ha desarrollado desde entonces muy rápidamente, y en OpenBSD 3.8 ya tenía mucha ventaja sobre otras opciones de cortafuegos. La sintaxis de filtrado es muy similar a la de IPFilter, aunque se modificó para hacerla más clara y legible. La traducción de direcciones de red (NAT) y calidad del servicio (QoS) se integraron perfectamente en PF, para permitir mayor flexibilidad. Se alcanzó el QoS integrando colas alternativas (ALTQ) en el propio PF.

PF puede utilizarse para montar dispositivos cortafuegos de gran flexibilidad, ya que incluye características de Alta Disponibilidad, como pfsync y un protocolo de redundancia para direcciones comunes (CARP), authpf (Identificador de sesión), un proxy ftp y otros extras relacionados con PF.

 Portes

PF se desarrolla como parte del sistema base de OpenBSD. Pese a ello, ha sido portado con éxito a otros sistemas. FreeBSD lo fue adoptando paulatinamente, primero como paquete y desde la versión FreeBSD 5.3 como una de los tres subsistemas de filtrado que ofrece el núcleo. Existe una versión de FreeBSD, denominada pfSense, que incluye una sofisticada interfaz gráfica para editar reglas de PF.

También se ha portado PF a NetBSD 3.0 por itojun y aparece en DragonFlyBSD desde la versión 1.2. Pese a algunos intentos, PF no ha podido ser portado con éxito a Linux, probablemente por las profundas diferencias entre la pila de red de los núcleos BSD y el de Linux.

 Comandos y opciones

 pfctl -e -> activa PF
 pfctl -d -> desactiva PF
 pfctl -f  -> si no aparecen errores de sintaxis en , se cargan reglas nuevas en PF

 Ejemplo de un archivo pf.conf
 **## Macros**

 # Interfaz interna (conectada a la red local).
 int_if="xl0"

 **## Opciones**

 # Se ajusta la política por defecto para devolver RSTs o ICMPs para tráfico bloqueado
 set block-policy return

 # Ignorar la interfaz loopback por completo.
 set skip on lo0

 **## Reglas de reenrutado**

 # El tráfico NAT en la interfaz englobada dentro del grupo por defecto de interfaz *egress*
 # (al que se asigna la interfaz de salida de la ruta por defecto) desde la red local
 nat on egress from $int_if:network to any -> (egress)

 **## Reglas de filtrado**

 # Regla de denegación por defecto, todos los paquetes bloqueados registrados en log
 block log all

 # Pasa todo el tráfico desde y hacia la red local, utilizando *quick* para que
 # después no se evalúen las reglas para este caso. Algunas reglas restringirán el
 # tráfico local mucho más.
 pass quick on $int_if all

 # Permite la salida de todo el tráfico, manteniendo el estado para que las respuestas
 # pasen automáticamente. Muchas reglas tendrán aquí más reglas, restringiendo el
 # tráfico de entrada y salida en la interfaz externa (egress).
 pass out keep state

 Registro
El registro PF se configura por reglas dentro de pf.conf. Los logs se manejan en el formato binario de tcpdump/pcap.

Se puede acceder a los logs a través del pseudodispositivo de red llamado 'pflog' mediante una utilidad como tcpdump. Alternativamente la utilidad 'pflogd' puede recoger y colocar logs en el archivo binario de log /var/log/pflog, que también puede manejarse con tcpdump, Ethereal y otras aplicaciones similares.

El formato tcpdump/pcap ha sido modificado ligeramente para archivar las estadísticas de reglas del firewall, estados de paso/bloqueo, interfaces utilizadas, información que sólo está disponible con utilidades que tienen en cuenta esta codificación particular, incluyendo las versiones recientes de tcpdump y Ethereal.

 Véase también
 TCP/IP
 NAT

 Enlaces externos
 Guía del PF de OpenBSD
 Canción del OpenBSD con información de trasfondo acerca de la creación de PF.
 Sección de PF en la web de Daniel Hartmeier
 Tutorial de PF por Peter N. M. Hansteen (Inglés)
