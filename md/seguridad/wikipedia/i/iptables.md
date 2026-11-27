---
type: Artículo de enciclopedia
title: Iptables
description: "iptables es un programa de utilidad de espacio de usuario que permite a un administrador de sistemas configurar el conjunto de reglas de filtro de paquetes proporcionadas por el núcleo Linux (implementado como …"
resource: https://es.wikipedia.org/wiki/Iptables
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Iptables"}
license: CC BY-SA 4.0
id: eswiki-Iptables
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Iptables

- **Nombre:** iptables
- **Desarrollador:** Netfilter Core Team
- **Autor:** Rusty Russell
- **Última versión:** 1.8.12
- **Sistema operativo:** Linux
- **Lenguaje programación:** C
- **Plataforma:** Netfilter
- **Licencia:** GPL

**iptables** es un programa de utilidad de espacio de usuario que permite a un administrador de sistemas configurar el conjunto de reglas de filtro de paquetes proporcionadas por el núcleo Linux (implementado como diferentes módulos Netfilter). Se utilizan diferentes módulos del *kernel* y programas para protocolos diferentes; *iptables* se aplica a IPv4, *ip6tables* a IPv6, *arptables* a ARP, y *ebtables* a marcos de Ethernet.

Iptables requiere privilegios elevados para operar y debe ser ejecutado por el usuario root, de lo contrario, fallará. En muchas distribuciones de Linux, como aquellas basadas en Debian, iptables puede ser encontrado en el fichero /usr/sbin/iptables, y documentado en su página de man, la cual puede ser abierta utilizando el comando man iptables. De igual forma, en las distribuciones basadas en Red Hat  podemos encontrar iptables en el fichero /sbin/iptables pero, debido a su carácter de servicio más que de binario esencial, la primera ubicación es preferida.

El término *iptables*  también es frecuentemente usado para referirse de forma inclusiva a componentes a nivel de kernel. *x_tables* es el nombre del módulo del kernel que contiene la porción de código compartido utilizada por los cuatro módulos y que también proporciona la API utilizada para las extensiones. Subsecuentemente Xtables se utiliza *grosso modo* para referirse a toda la arquitectura del cortafuegos (v4, v6, arp y eb).

iptables sustituyó a ipchains, y iptables a su vez fue sucedido por nftables, que fue lanzado el 19 de enero de 2014 y se integró en la rama principal del kernel de Linux en la versión 3.13 del *kernel*.

 Véase también
 PF (firewall)
 ipfirewall (ipfw)
 ipchains
 Netfilter

Referencias

 Bibliografía

 Enlaces externos
 El netfilter/iptables Página web de proyecto

 El netfilter/iptables página de documentación (outdated) [la aclaración necesitada]
 Detectando y engañando escáneres de red   contramedidas contra nmap
 El IPTables ManPage para ayuda de sintaxis
 Iptables Preceptoral 1.2.2 por Oskar Andreasson
 IPTABLES: El Default Linux Firewall
 Aceleración de iptables Paquete de Linux que Filtra utilizando GPGPU
