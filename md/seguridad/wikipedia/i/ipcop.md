---
type: Artículo de enciclopedia
title: IPCop
description: IPCop es una distribución Linux que implementa un cortafuegos (o firewall) y proporciona una simple interfaz web de administración basándose en una computadora personal.
resource: https://es.wikipedia.org/wiki/IPCop
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/IPCop"}
license: CC BY-SA 4.0
id: eswiki-IPCop
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# IPCop

- **Nombre:** IPCop
- **Desarrollador:** IPCop team
- **Familia:** Linux Cortafuegos
- **Modelo desarrollo:** FOOS
- **Última versión:** 2.1.9
- **Fecha última versión:** 23 de febrero de 2015
- **Kernel tipo:** Monolítico
- **Ui:** Interfaz web
- **Licencia:** Varias
- **Estado actual:** En desarrollo

**IPCop** es una distribución Linux que implementa un cortafuegos (o *firewall*) y proporciona una simple interfaz web de administración basándose en una computadora personal. Originalmente nació como una extensión (fork) de la distribución SmoothWall cuyo desarrollo había estado congelado bastante tiempo.

IPCop tiene como objetivos ser un cortafuegos sencillo, con pocos requerimientos hardware orientado a usuarios domésticos o a pequeñas empresas (SOHO), administrado a través de una interfaz web, con funcionalidades básicas y avanzadas, yendo (a manera de ejemplo) desde el simple filtrado de paquetes hasta la asignación de ancho de banda fijo a cada puesto de trabajo o la configuración de redes virtuales VPN. IPCop se actualiza desde la Interfaz Web de manera muy sencilla, incluyendo actualizaciones del Kernel.

IPCop sólo tiene instaladas las herramientas justas para su función como firewall, limitando el daño que podría hacer un intruso que comprometiera el sistema. Si se desea ampliar la funcionalidad existen extensiones (addons), comunes con SmoothWall, que permiten instalar todo tipo de utilidades como por ejemplo instalar Nmap para escanear IPs.

La distribución Linux se puede bajar desde el sitio oficial en inglés, consiste de una imagen ISO de menos de 100Mb la cual puede ser grabada en un CD e instalada en cualquier computador que tenga al menos dos interfaces de red.

Extensiones (*addons*)
BOT (Block Out Traffic)
Esta extensión permite cortar o bloquear todo el tráfico de salida de IPCop, ya que en un principio este firewall solo bloquea las conexiones entrantes.
Advanced proxy
Otra de las extensiones más usadas, ya que el servidor proxy que trae por defecto este firewall es poco avanzado y con pocas opciones de configuración.
URL Filter
Esta extensión nos permite crear listas blancas y negras de las diferentes URL que queremos bloquear a los usuarios de IPCop. Se usa junto a la anterior puesto que se sirve de un proxy para bloquear dichas URL.
Topologías de red soportadas
Permite la implementación de diferentes topologías de red, ya sea desde la simple LAN que sale a internet, hasta la creación de una zona desmilitarizada (DMZ), soportando también la inclusión de una red inalámbrica.

Zonas
Divide las diferentes zonas por colores, siendo:
 **Roja** = zona de Internet,
 **Verde** =  Red de Área Local (LAN) cableada,
 **Naranja** = zona desmilitarizada (DMZ, para la granja de servidores),
 **Azul** = zona inalámbrica (*wireless*).

 Véase también

 Linux
 Firewall
 SmoothWall
 Endian Firewall
 Squid

 Enlaces externos

 Web oficial (en inglés)
 (en francés) Tutoriel complet IPCop vervion 2.0.0  MAX-IPCop
 Capturas de pantalla de IPCop
