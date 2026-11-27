---
type: Artículo de enciclopedia
title: Chkrootkit
description: Chkrootkit es un programa informático de consola, común en sistemas operativos Unix y derivados.
resource: https://es.wikipedia.org/wiki/Chkrootkit
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Chkrootkit"}
license: CC BY-SA 4.0
id: eswiki-Chkrootkit
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Chkrootkit

- **Nombre:** chkrootkit
- **Captura:** chkrootkit en Linux|200 px
- **Desarrollador:** Pangeia Informática
- **Última versión:** 0.54
- **Sistema operativo:** Linux, FreeBSD, OpenBSD, NetBSD, Solaris, HP-UX, Tru64, BSDI, Mac OS X
- **Género:** Detector de rootkit
- **Licencia:** Específica de tipo software libre

**Chkrootkit**  es un programa informático de consola, común en sistemas operativos Unix y derivados. Permite localizar *rootkits* conocidos, realizando múltiples pruebas en las que busca entre los binarios modificados por dicho software. Este guion de consola usa herramientas comunes de UNIX/Linux como las órdenes strings y grep para buscar entre los ejecutables del sistema firmas de *rootkits* conocidos para estos sistemas operativos y comparar de forma transversal el directorio /proc con la salida de la orden ps (estado de los procesos (*process status*)) para buscar discrepancias. Básicamente hace múltiples comprobaciones para detectar todo tipo de *rootkits* y ficheros maliciosos.

Puede ser utilizado desde un "disco de respaldo" (típicamente un *LiveCD*)
o puede utilizar opcionalmente un directorio alternativo desde el cual ejecutar todas sus órdenes. Estas técnicas permiten que chkrootkit confíe en las órdenes de las cuales depende un poco más.

Existen limitaciones inherentes en la confiabilidad de cualquier programa que procure detectar compromisos (tales como *rootkits* y virus informáticos). Los nuevos *rootkits* pueden específicamente intentar detectar y comprometer copias del programa chkrootkit o tomar otras medidas para evadir las detecciones que éste efectúa.

 Véase también
 rkhunter
 Rootkit

 Referencias

 Enlaces externos
 Sitio Oficial Chkrootkit
 Sitio en Castellano de Chkrootkit
 Chkrootkit script de instalación automática
