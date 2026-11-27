---
type: Artículo de enciclopedia
title: "W^X"
description: "En la programación segura, W^X (W XOR X) es el nombre de una característica de la seguridad informática presente en los sistemas operativos OpenBSD."
resource: https://es.wikipedia.org/wiki/W^X
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/W^X"}
license: CC BY-SA 4.0
id: "eswiki-W^X"
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# W^X

En la **programación segura**, **W^X** (*W XOR X*) es el nombre de una característica de la seguridad informática presente en los sistemas operativos OpenBSD. Es una política de protección de la memoria en la que cada página del espacio de direcciones de un proceso es o escribible o ejecutable, pero no ambas simultáneamente (el nombre viene del operador booleano *XOR*, que cumple dicha propiedad). W^X no previene que las aplicaciones pidan estos permisos, los permisos de escritura y ejecución no se usan como parte de la política. La base del sistema OpenBSD se ha modificado para cumplir con ello. Esto soluciona algunos ataques de desbordamiento de buffers, incluyendo los más comunes ataques basados en la pila: asegurando que la pila no es ejecutable, ningún código inyectado se ejecutará, en lugar de eso el programa terminará. La primera aparición de W^X fue en la versión 3.3 de OpenBSD; en otros sistemas operativos existen características similares, incluyendo los parches de PaX y Exec Shield para Linux y la implementación de PaX para las versiones 4.x de NetBSD.

 Véase también
 Bit NX
 Prevención de ejecución de datos
 Protección del espacio ejecutable

 Enlaces externos
 Transparencias de una presentación del desarrollador principal de OpenBSD Theo de Raddt sobre W^X
