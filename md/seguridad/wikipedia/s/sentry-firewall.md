---
type: Artículo de enciclopedia
title: Sentry Firewall
description: Sentry Firewall es una distribución de Linux de firewall de red de código abierto que se publicó por primera vez en 2001 y ha sido objeto de múltiples revisiones de revistas.
resource: https://es.wikipedia.org/wiki/Sentry_Firewall
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sentry_Firewall"}
license: CC BY-SA 4.0
id: eswiki-Sentry_Firewall
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sentry Firewall

**Sentry Firewall** es una distribución de Linux de firewall de red de código abierto que se publicó por primera vez en 2001 y ha sido objeto de múltiples revisiones de revistas. Actualmente la distribución está descontinuada. La distribución es particularmente excelente porque consiste únicamente en un CD-ROM de arranque que está diseñado para usarse en una computadora sin disco duro. La información de configuración se recupera en el momento del arranque del ordenador mediante la búsqueda automática en una unidad de disquete conectada, una unidad de memoria flash USB u otro servidor en la red local dispuesto a proporcionar la configuración.

 Visión general
Sentry Firewall comienza desde el CD-ROM e inmediatamente construye un disco RAM en la memoria de la computadora. Antes de que el sistema se inicie completamente, un script busca medios extraíbles que contengan un archivo llamado "sentry.conf". Si se encuentra ese archivo, puede contener instrucciones detalladas y una lista de archivos que se copiarán de los medios extraíbles al disco RAM antes de que finalmente se permita el arranque del sistema.

El CD-ROM viene precargado con una variedad de herramientas de red configurables, que están incluidas iptables.

Debido a que el disco RAM se crea cada vez que la máquina arranca, es posible recuperarse de cualquier tipo de problema simplemente reiniciando la máquina. Desde una perspectiva de seguridad, esto es convincente porque la máquina se vuelve esencialmente inmune a los virus o la corrupción de archivos, o al menos los efectos de cualquiera de los problemas hacen que no pueden sobrevivir a un reinicio.

 Configuración
Si bien la familiaridad básica con Linux es necesaria para configurar un conjunto básico de archivos necesarios para usar el firewall, existen programas de Windows que es capaz de crear la mayor parte de los scripts de configuración basados en la interacción con una interfaz gráfica de usuario. Firewall Builder es uno de esos ejemplos; Este programa también funciona con otros productos de firewall que no están relacionados con Sentry Firewall.

 Estado actual
Según el responsable del proyecto, Sentry Firewall no ha actualizado desde su lanzamiento en enero de 2005.
 Referencias
