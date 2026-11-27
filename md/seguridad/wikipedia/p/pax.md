---
type: Artículo de enciclopedia
title: PaX
description: En seguridad informática, PaX es un parche del núcleo Linux que implementa protecciones del mínimo privilegio para las páginas de memoria.
resource: https://es.wikipedia.org/wiki/PaX
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/PaX"}
license: CC BY-SA 4.0
id: eswiki-PaX
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# PaX

En seguridad informática, **PaX** es un parche del núcleo Linux que implementa protecciones del mínimo privilegio para las páginas de memoria. La aproximación del mínimo privilegio permite a los programas realizar lo que tienen que hacer de modo que sean capaces de ejecutarlo adecuadamente, y no poder realizar nada más. La primera versión de PaX fue publicada en el año 2000.

PaX marca los datos de memoria como no ejecutables, la memoria del programa como no escribible y organiza aleatoriamente la memoria del programa. Esto previene eficazmente muchos de los exploits, como algunos tipos de desbordamientos de buffers. Previene la ejecución de código directa, mientras que los ataques conocidos como return-to-libc (ret2libc) son más difícil de explotar, fiándose de la suerte del éxito, pero no previene de la sobrescritura de variables y punteros.

El equipo de PaX se encarga del mantenimiento de PaX, cuyo principal desarrollador es anónimo.

 Véase también
Exec Shield
Security-Enhanced Linux
W^X
Bit NX
Sistema de detección de intrusos
Sistema de prevención de intrusos

 Referencias
Documentación de PaX

 Enlaces externos
Página web de PaX
El futuro de PaX
Presentación de PaX
Trampolines para funciones encadenadas
Técnicas de mitigación de exploits

Bug de elevación de privilegios en PaX
Código de la prueba de concepto de la elevación de privilegios en PaX
