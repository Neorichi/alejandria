---
type: Artículo de enciclopedia
title: Bomba zip
description: La bomba zip, también conocida como zip de la muerte, es un archivo malicioso diseñado para bloquear o inutilizar un programa o sistema que lo está leyendo.
resource: https://es.wikipedia.org/wiki/Bomba_zip
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Bomba_zip"}
license: CC BY-SA 4.0
id: eswiki-Bomba_zip
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Bomba zip

La **bomba zip,** también conocida como **zip de la muerte**, es un archivo malicioso diseñado para bloquear o inutilizar un programa o sistema que lo está leyendo. Este tipo de archivo malicioso explota el algoritmo de compresión de ZIP para guardar grandes cantidades de datos.

Se utilizaba para deshabilitar el software antivirus, de modo que otro malware enviado después pudiera pasar desapercibido. Hoy en día, la mayoría de los programas antivirus pueden detectar si un archivo es una bomba zip y así evitar descomprimirlo. Muchos de ellos lo hacen permitiendo sólo unas pocas capas de recursividad para prevenir ataques que podrían causar un desbordamiento de búfer, una condición de falta de memoria o un exceso de tiempo de ejecución del programa, de espacio en disco o memoria.

Por lo general, son archivos pequeños (hasta unos pocos cientos de kilobytes) para facilitar su transporte y evitar sospechas.

 42.Zip
Un ejemplo de bomba zip es el archivo "42.zip", que son 42kB de datos comprimidos, que contiene cinco niveles de archivos zip anidados en grupos de 16. Cada archivo de nivel inferior contiene un archivo de 4,3GB o 16GB. Dicho archivo existe en dos versiones:

 La antigua, de 42374bytes (sin contraseña)
 La nueva, de 42838bytes (tiene contraseña)

La contraseña de la nueva versión es "42"

 Una mejor bomba ZIP
El 2 de julio de 2019, David Fifield creó una nueva versión mejorada de la bomba ZIP a partir del estudio del algoritmo de comprensión del formato ZIP, y creó otras 3bombas:

 zbsm.zip, con un tamaño de 5.5GB comprimidos en un archivo de 42KB.
 zblg.zip, con un tamaño de 281TB comprimidos en un archivo de 10MB.
 zbxl.zip, con un tamaño de 4.5PB comprimidos a través del algoritmo Zip64 en un archivo de 46MB (aunque no tan compatible).

 Referencias
