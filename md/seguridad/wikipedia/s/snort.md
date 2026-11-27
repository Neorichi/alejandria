---
type: Artículo de enciclopedia
title: Snort
description: Snort es un sistema de detección de intrusos en red, libre y gratuito.
resource: https://es.wikipedia.org/wiki/Snort
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Snort"}
license: CC BY-SA 4.0
id: eswiki-Snort
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Snort

- **Nombre:** Snort
- **Autor original:** Martin Roesch
- **Desarrollador:** Cisco Systems
- **Última versión:** 3.10.1.0
- **Género:** Sistema de detección de intrusos en red (NIDS)
- **Lenguaje programación:** C
- **Sistema operativo:** Multiplataforma
- **Licencia:** GPLv2 y comercial

**Snort** es un sistema de detección de intrusos en red, libre y gratuito. Ofrece la capacidad de almacenamiento de bitácoras en archivos de texto y en bases de datos abiertas, como MySQL. Implementa un motor de detección de ataques y escaneo de puertos que permite registrar, alertar y responder ante cualquier anomalía previamente definida.

 Historia
En noviembre de 1998, Marty Roesch escribió un programa para Linux llamado APE. Sin embargo, carecía de lo siguiente:
 Capacidad para trabajar en múltiples sistemas operativos.
 Capacidad para trabajar con el formato hexdump.
 Mostrar todos los tipos de paquetes de la misma forma.

A partir de ello, se comenzó a desarrollar como una aplicación de libcap, que le dio portabilidad.

 Funcionamiento
Este IDS implementa un lenguaje de creación de reglas flexible, potente y sencillo. Durante su instalación, provee de cientos de filtros o reglas para backdoor, DDoS, finger, FTP, ataques web, CGI, Nmap, entre otros.

Puede funcionar como sniffer y registro de paquetes. Cuando un paquete coincide con algún patrón establecido en las reglas de configuración, se logea. Así se sabe cuándo, de dónde y cómo se produjo el ataque.

Snort tiene una base de datos de ataques que se actualiza constantemente a través de internet. Los usuarios pueden crear firmas basadas en las características de los nuevos ataques de red y enviarlas a la lista de correo de firmas de Snort, esta ética de comunidad y compartir ha convertido a Snort en uno de los IDS basados en red más populares, actualizados y robustos.

 Véase también
 IDS
 HIDS
 NIDS

 Referencias

 Enlaces externos
 Sitio web oficial
