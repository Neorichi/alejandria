---
type: Artículo de enciclopedia
title: LUKS
description: LUKS (de las siglas en inglés, Linux Unified Key Setup) es una especificación de cifrado de disco creado por Clemens Fruhwirth, originalmente destinado para Linux.
resource: https://es.wikipedia.org/wiki/LUKS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/LUKS"}
license: CC BY-SA 4.0
id: eswiki-LUKS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# LUKS

**LUKS** (de las siglas en inglés, *Linux Unified Key Setup*) es una especificación de cifrado de disco creado por Clemens Fruhwirth, originalmente destinado para Linux. Mientras la mayoría del software de cifrado de discos implementan diferentes e incompatibles formatos no documentados, **LUKS** especifica un formato estándar en disco, independiente de plataforma, para usar en varias herramientas. Esto no sólo facilita la compatibilidad y la interoperabilidad entre los diferentes programas, sino que también garantiza que todos ellos implementen gestión de contraseñas en un lugar seguro y de manera documentada.

La implementación de referencia funciona en Linux y se basa en una versión mejorada de cryptsetup, utilizando dm-crypt como la interfaz de cifrado de disco. En Microsoft Windows, los discos cifrados con **LUKS** pueden ser utilizados con FreeOTFE. Ha sido diseñado para ajustarse a la clave de configuración TKS1 de sistema seguro.

En septiembre de 2013, Phoronix publicó una comparativa de rendimiento entre **LUKS** y  eCryptfs. Usó la versión, existente a esa fecha, de Ubuntu 13.10. Y obtuvo mejor rendimiento encriptando todo el disco con **LUKS**, que solo el directorio de datos de usuario con eCryptfs.

 Véase también
Dm-crypt
FreeOTFE

 Referencias

 Enlaces externos

 Página oficial
