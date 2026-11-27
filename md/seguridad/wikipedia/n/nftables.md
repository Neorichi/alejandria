---
type: Artículo de enciclopedia
title: Nftables
description: nftables es un proyecto que proporciona filtrado de paquetes y clasificación de paquetes en Linux, que reemplaza los frameworks existentes iptables, ip6tables, arptables y ebtables.
resource: https://es.wikipedia.org/wiki/Nftables
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Nftables"}
license: CC BY-SA 4.0
id: eswiki-Nftables
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Nftables

- **Nombre:** nftables
- **Desarrollador:** Proyecto Netfilter
- **Autor:** Proyecto Netfilter
- **Última versión:** 1.1.7
- **Género:** Cortafuegos
- **Lenguaje programación:** C
- **Sistema operativo:** Linux
- **Plataforma:** Netfilter
- **Licencia:** GPL (versión 2)
- **Estado:** En desarrollo

***nftables*** es un proyecto que proporciona filtrado de paquetes y clasificación de paquetes en Linux, que reemplaza los *frameworks* existentes *iptables*, *ip6tables*, *arptables* y *ebtables*. Nftables es una combinación de componentes en núcleo de Linux (módulos) y una utilidad de línea de comandos en espacio de usuario.

Reutiliza partes clásicas de la infraestructura *Netfilter*, como el *connection tracking system* (conntrack, sistema de seguimiento de conexiones), el subsistema de envío de paquetes a espacio de usuario (nf_queue) y el subsistema de registro (nf_log), entre otros. También existe una capa de traducción y compatibilidad para facilitar el trabajo sobre reglas ya existentes de *iptables*.

En mayo de 2017, el proyecto Debian anunció que incluiría oficialmente a nftables en su sistema operativo y recomienda a los usuarios migrar desde iptables a nftables.
A su vez, en octubre de 2019, se anunció que nftables sería la herramienta por defecto a partir de Debian 11 Bullseye.

 Motivaciones de nftables

El framework de iptables sufre una serie de limitaciones que se han querido mejorar en nftables:
 Evitar duplicidad e inconsistencia en el código fuente. Muchas extensiones de iptables estaban duplicadas con pequeños cambios para interactuar con diferentes protocolos de red.
 Mejorar soporte para conjuntos y mapeo de datos.
 Simplificar usabilidad en entornos IPv4/IPv6.
 Mejorar mecanismo para actualizaciones al conjunto de reglas. Esta tarea en iptables es muy costosa y poco escalable.
 Proveer API Netlink para aplicaciones externas.
 Mejorar sintaxis.

 Diferencias entre nftables e iptables

Desde el punto de vista del usuario, las principales diferencias entre nftables e iptables son:
 La sintaxis: iptables usa un parseador basado en getopt_long, donde las órdenes van precedidas por guiones (por ejemplo, '-m conntrack --ctstate'). Ahora nftables usa una sintaxis más compacta e intuitiva que fue inspirada por la herramienta tcpdump.
 Las tablas y cadenas son totalmente configurables. En nftables, las tablas son meros contenedores de cadenas, sin una semántica determinada. En iptables, hay una serie de tablas y cadenas predeterminadas que son registradas en el sistema de manera obligatoria aunque no vayas a usarlas. Los nombres de estos objetos (tablas y cadenas) son también arbitrarios.
 Los conceptos de 'target' y 'match' desaparecen. En nftables, las reglas están compuestas de **expresiones**.
 *nftables* permite especificar varias acciones en una única regla. En iptables, solo podías seleccionar un 'target' por regla.
 No hay contadores integrados en reglas y cadenas. Son opcionales y pueden habilitarse bajo demanda.
 Soporte mejorado para actualizaciones dinámicas del conjunto de reglas.
 Administración simplificada para conjuntos de reglas IPv4/IPv6.
 Infraestructura genérica de conjuntos y mapeos de datos, directamente integrada en el núcleo de nftables. En iptables, existe la herramienta externa ipset.
 Soporte para nuevos protocolos sin actualizaciones del kernel Linux, dado que la complejidad del manejo de protocolos se encuentra en espacio de usuario y no en el kernel.

A modo de ejemplo, esta sería una equivalencia entre reglas similares.

En iptables:

En nftables:

 Referencias

 Enlaces externos
 Sitio web oficial
 Wiki oficial
 Repositorio de código fuente de nftables Git
 Documentación *howto* para nftables
 Primera versión de nftables (18-03-2009)
 Pablo Neira Ayuso: [RFC] back on nf_tables (más capa de compatibilidad)
 Referencia rápida para Nftables
 Debian wiki
 ArchWiki
 Gentoo Wiki
