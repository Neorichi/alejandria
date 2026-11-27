---
type: Artículo de enciclopedia
title: Escape de máquina virtual
description: En seguridad informática, el escape de máquina virtual es el proceso de salir de un entorno virtualizado e interactuar con el sistema operativo anfitrión de una manera no planificada por el administrador del servidor.
resource: https://es.wikipedia.org/wiki/Escape_de_máquina_virtual
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Escape_de_máquina_virtual"}
license: CC BY-SA 4.0
id: eswiki-Escape_de_máquina_virtual
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Escape de máquina virtual

En seguridad informática, el **escape de máquina virtual** es el proceso de salir de un entorno virtualizado e interactuar con el sistema operativo anfitrión de una manera no planificada por el administrador del servidor. Una máquina virtual es una "instalación de sistema operativo invitado completamente aislada dentro de un sistema operativo host normal". En 2008, una vulnerabilidad (CVE-2008-0923) en VMware descubierta por Core Security Technologies hizo posible el escape de VM en VMware Workstation 6.0.2 y 5.5.4. Un exploit totalmente funcional etiquetado como ***Cloudburst*** fue desarrollado por Immunity Inc. para Immunity CANVAS (herramienta de prueba de penetración comercial). Cloudburst fue presentado en Black Hat USA 2009.

Los contenedores también pueden verse afectados, especialmente por la interacción directa con el kernel compartido con el sistema operativo anfitrión.

 Vulnerabilidades conocidas

 **CVE-2007-1744** y **CVE-2008-0923** - *Directory traversal* en la función de carpetas compartidas para VMware.
 **CVE-2009-1244** - Cloudburst: función de visualización de VM en VMware.
 **CVE-2012-0217** - Citrix XenServer: La funcionalidad de llamada al sistema del kernel x86-64 en Xen 4.1.2 y anteriores.
 **CVE-2014-0983** - Oracle VirtualBox: Corrupción de memoria múltiple mediante la característica de aceleración 3D.
 **CVE-2015-3456** - QEMU, Xen, KVM y VirtualBox: denegación de servicio o ejecución de código en el sistema host debido al controlador de disquete de QEMU, vulnerabilidad conocida como VENOM.
 **CVE-2015-6240** - Escape de una jaula chroot mediante ataque de enlaces simbólicos en Ansible.
 **CVE-2015-7835** - Xen: Creación no controlada de mapas de páginas grandes por parte de invitados de PV.
 **CVE-2016-6258** - Xen: El código de la página de pago de PV tiene rutas rápidas para realizar actualizaciones a las entradas de la tabla de páginas preexistentes, para omitir re-validación costosa en casos seguros (por ejemplo, borrando solo los bits de Access/Dirty). Los bits considerados seguros eran demasiado anchos, y en realidad no eran seguros.
 **CVE-2016-7092** - Xen: Inhabilita la tabla de páginas recursiva L3 para invitados fotovoltaicos de 32 bits.
 **CVE-2017-0075** y **CVE-2017-0109** - Hyper-V: Vulnerabilidad de ejecución remota. Ambas vulnerabilidades son diferentes pero con los mismos resultados.

 **CVE-2017-4903** - VMware ESXi, Workstation y, Fusion: Desbordamiento de búfer en el controlador SVGA puede permitir a los invitados ejecutar código en el sistema operativo anfitrión.
 **CVE-2017-4934** - VMware Workstation y Fusion: Vulnerabilidad de desbordamiento de búfer en el dispositivo VMNAT que puede permitir que un invitado ejecute código en el anfitrión.
 **CVE-2017-4936** - VMware Workstation, Horizon View: Varios problemas de lectura fuera de los límites a través de ThinPrint que pueden permitir a un invitado ejecutar código o realizar una denegación de servicio en el sistema operativo Windows anfitrión.
 **CVE-2017-5123** - Una vulnerabilidad en la función waitid de Linux 4.12 y 4.13 puede permitir escalado de privilegios, incluso desde contenedores como Docker.
 **CVE-2018-2694** y **CVE-2018-2698** - Oracle VirtualBox: la interfaz de memoria compartida por VGA permite leer y escribir en el sistema operativo host.
 **CVE-2022-31705** - VMware ESXi, Workstation, y Fusion: vulnerabilidad de escritura fuera de los límites en el controlador USB 2.0.

 Véase también
 Hyperjacking

 Referencias

 CVE

 Enlaces externos
 Cloudburst (Hacking 3D And Breaking Out Of Vmware) Blackhat 2009 (Video)
 https://technet.microsoft.com/library/security/MS17-008
