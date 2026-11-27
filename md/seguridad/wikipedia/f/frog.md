---
type: Artículo de enciclopedia
title: FROG
description: En criptografía, FROG es un algoritmo de cifrado por bloques realizado por Georgoudis, Leroux y Chaves.
resource: https://es.wikipedia.org/wiki/FROG
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/FROG"}
license: CC BY-SA 4.0
id: eswiki-FROG
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# FROG

En criptografía, **FROG** es un algoritmo de cifrado por bloques realizado por Georgoudis, Leroux y Chaves. Puede trabajar con bloques de tamaño entre 8 y 128bytes, con tamaños de clave comprendidos entre los 5 y los 125bytes. El algoritmo consiste en 8rondas y tiene un desarrollo de la clave muy complicado.

Se envió en 1998 a la competición AES como candidato para convertirse en el Advanced Encryption Standard. En 1999, David Wagner y otros encontraron un número de claves débiles para FROG, que afectaba aproximadamente a una cada mil millones . Otros problemas eran un inicio de la clave muy lento y una velocidad de cifrado relativamente lenta. FROG no llegó a ser elegido finalista.

 Filosofía del diseño

FROG sigue una filosofía de diseño innovadora. Normalmente, un algoritmo de cifrado por bloques aplica una secuencia matemáticas o lógicas conocida (como adiciones, XOR, etc) sobre el texto plano y la clave para producir el texto cifrado. Esta secuencia de operaciones es conocida por el atacante (a menos que el algoritmo en sí mismo sea desconocido, lo que era imposible en el contexto del concurso). Un atacante podría usar este conocimiento para buscar debilidades en el algoritmo lo que, finalmente, podría permitirle recuperar el texto plano original.

El diseño de FROG era ocultar la secuencia exacta de las secuencias y operaciones, incluso a pesar de que el algoritmo es conocido. Donde otros cifradores usan la clave solo como datos para producir el texto cifrado, FROG usa la clave además como instrucciones sobre las cuales se generará el producto cifrado. De hecho, una versión expandida de la clave es usada por FROG como programa. FROG opera él mismo como un intérprete que aplica este programa dependiente de la clave sobre el texto plano para producir el texto cifrado. El descifrado opera usando el mismo programa de manera inversa.

 Referencias
 David Wagner, Niels Ferguson and Bruce Schneier, Cryptanalysis of FROG, durante la segunda conferencia para el concurso AES., pp175-181, NIST, 1999 .
 Dianelos Georgoudis, Damian Leroux and Billy Simón Chaves, The FROG Encryption Algorithm, 15 de junio de 1998 .

 Enlaces externos
 código de referencia
