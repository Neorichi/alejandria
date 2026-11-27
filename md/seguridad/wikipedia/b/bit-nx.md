---
type: Artículo de enciclopedia
title: Bit NX
description: NX puede referirse también a software de Siemens antes conocido como Unigraphics.
resource: https://es.wikipedia.org/wiki/Bit_NX
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Bit_NX"}
license: CC BY-SA 4.0
id: eswiki-Bit_NX
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Bit NX

***NX** puede referirse también a software de Siemens antes conocido como **Unigraphics**.*

**NX** significa ***N**o e**X**ecute* (no ejecutar). Es una tecnología utilizada en CPUs para separar las áreas de memoria usadas para albergar las instrucciones del procesador (código) y las de almacenamiento de datos. Cualquier sección de memoria designada con el atributo NX significa que sólo se usa para datos, por lo tanto las instrucciones del procesador no pueden ni deben residir ahí. Es una técnica utilizada para prevenir que cierto tipo de software malicioso tome el control de la máquina insertando su código en el área de almacenamiento de datos de otro programa y ejecute su propio código desde dentro de esta sección; esto se conoce como *desbordamiento de búfer*, y NX puede prevenirlo.

Hardware
Aunque este tipo de mecanismo se ha venido utilizando durante años en otras arquitecturas de procesadores como SPARC de Sun, Alpha de HP, PowerPC de IBM, e incluso la arquitectura IA64 de Intel, el término ha sido acuñado por AMD para su uso en la línea de procesadores AMD64, como el Athlon 64 y Opteron. Parece que se ha convertido en un término común para describir genéricamente tecnologías similares en otros procesadores

El bit NX se refiere específicamente al bit número 63 (al último bit, si el primer bit empieza en el 0, en enteros de 64 bits) en la entrada de la tabla de páginas de un procesador x86. Si este bit está marcado a 0, entonces el código puede ser ejecutado desde esa página; si está marcado a 1, el código no puede ser ejecutado desde esa página, y todo lo que ahí resida será considerado como datos. Hay que tener en cuenta que estas páginas tienen que cumplir el formato de tabla de páginas PAE (extensión de dirección física), en lugar del formato de tabla de páginas original del x86. Esta característica primero fue implementada en los procesadores AMD64, ya que la arquitectura AMD64 es una extensión directa de la arquitectura x86, pero esta característica no requiere que el procesador funcione en modo 64 bits - también funcionará en modo 32 bits. Como funciona en modo 32 bits, otros fabricantes de x86, como VIA Technologies, Transmeta, y por supuesto Intel están portando esta función a sus últimas implementaciones de x86.

Intel ha decidido llamarlo XD bit, que significa *Execute Disable* (Deshabilitar ejecución). Sin embargo, está implementado exactamente de la misma manera que el bit NX de AMD, así que realmente es lo mismo.

Emulación por software
Previamente a que esta característica estuviera integrada dentro del hardware, varios sistemas operativos intentaron emularla mediante software.

Un sistema operativo con la habilidad de emular o tener las ventajas de un bit NX puede prevenir que las áreas de memoria, como la pila (stack) y montículo (heap) sean ejecutables, y puede prevenir que la memoria ejecutable sea escribible. Esto ayuda a impedir que ciertos *exploits* de desbordamiento de búfer tengan éxito, particularmente aquellos que inyectan y ejecutan código, como los gusanos Sasser y Blaster. Estos ataques se basan en que alguna parte de la memoria, normalmente la pila, es tanto escribible como ejecutable; y si no lo es, el ataque fracasa.
