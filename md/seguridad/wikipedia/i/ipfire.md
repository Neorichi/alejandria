---
type: Artículo de enciclopedia
title: IPFire
description: "IPFire es una distribución de Linux, de código abierto reforzada que funciona principalmente como un enrutador y un cortafuegos; un sistema de firewall independiente con una consola de administración basada en web para …"
resource: https://es.wikipedia.org/wiki/IPFire
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/IPFire"}
license: CC BY-SA 4.0
id: eswiki-IPFire
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# IPFire

- **Familia:** GNU/Linux
- **Nombre:** IPFire
- **Sistema operativo:** GNU/Linux
- **Desarrollador:** IPFire-Team
- **Modelo desarrollo:** Software libre
- **Estado actual:** En desarrollo
- **Última versión:** IPFire 2.29 - Core Update 240
- **Kernel:** Linux
- **Kernel tipo:** Monolítico
- **Administrador paquetes:** Pakfire

**IPFire** es una distribución de Linux, de código abierto reforzada que funciona principalmente como un enrutador y un cortafuegos; un sistema de firewall independiente con una consola de administración basada en web para la configuración.

IPFire comenzó originalmente como una bifurcación de la distribución IPCop y ha sido reescrito sobre la base de Linux From Scratch desde la versión 2. Admite la instalación de complementos para agregar servicios de servidor, que se pueden extender a un servidor SOHO. En abril de 2015, el proyecto se convirtió en miembro de Open Invention Network.

 Requisitos del sistema
Los requisitos básicos son al menos un 1 GHz CPU, 1 GB de RAM y un disco duro de 4 GB. Se necesitan dos tarjetas de red para conectarse a una red Ethernet. DSL, LTE y Wi-Fi (WLAN) también son compatibles con el hardware correspondiente.

El rendimiento informático requerido para ejecutar IPFire depende del área de aplicación. Por lo general, se utilizan sistemas x86, pero también se admiten dispositivos ARM, como Raspberry Pi o Banana Pi. IPFire se puede utilizar en entornos virtuales (como KVM, VMWare, XEN, Qemu, etc. ).

La configuración básica de IPFire se realiza a través de un diálogo guiado en la consola, y la administración posterior se realiza en la interfaz de administración basada en web, para complementos y funciones adicionales.

 Detalles del sistema
El equipo de desarrollo actualiza periódicamente el proyecto para mantener la seguridad. Desarrollado como un cortafuegos de inspección de estado de paquetes (SPI).

IPFire separa la red en diferentes segmentos en función de su riesgo de seguridad que se organizan en colores. Los clientes normales conectados a la LAN se representan en verde, Internet se representa en rojo, una DMZ opcional se representa en naranja y una red inalámbrica opcional se representa en azul. Ningún tráfico puede fluir entre segmentos a menos que se permita específicamente a través de una regla de firewall.

El sistema de administración de paquetes de IPFire, llamado Pakfire permite instalar actualizaciones del sistema, que mantienen la seguridad al día, y paquetes de software adicionales para personalizarlos según diferentes escenarios de uso y necesidades. El sistema Linux está personalizado para el propósito concreto de un firewall.

El diseño es modular, por lo que sus funcionalidades son extensibles a través de la instalación de complementos, pero la base viene con las siguientes características

 Cortafuegos de inspección de estado de paquetes  (SPI) basado en Linux Netfilter.
 Servidor proxy con filtro de contenido y funciones de captura de actualizaciones (p. ej. Actualizaciones de Microsoft Windows, escáneres de virus, etc.)
 Sistema de detección de intrusos (Snort) con la opción de instalar el Sistema de prevención de intrusos *Guardian* a través *de Pakfire*
 Desde Core Update 131 cuenta con el  sistema prevención de intrusiones "Suricata" en lugar de snort
 Red privada virtual (VPN) con IPsec y OpenVPN
 Servidor de protocolo de configuración dinámica de host (DHCP)
 Servidor de nombres en caché (compatible con DNSSEC )
 Servidor de tiempo
 Wake-on-LAN (WOL)
 DNS Dinámico
 Calidad de servicio (QoS)
 Funciones de monitoreo del sistema y análisis de registros
 Filtrado GeoIP
 Portal cautivo

 IPFire Location
El Proyecto IPFire construyó una base de datos  de geolocalización de Internet publicada bajo la licencia Creative Commons. Está siendo utilizado por The Tor Project para identificar la ubicación de los nodos y transmisores Tor.

 Véase también

 Referencias

 Enlaces externos

 Página web oficial
 Sitio web de la geolocalización de IPFire
 IPFire en OpenHub
