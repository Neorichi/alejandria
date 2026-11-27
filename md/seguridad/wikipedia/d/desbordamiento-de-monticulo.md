---
type: Artículo de enciclopedia
title: Desbordamiento de montículo
description: "En informática, un desbordamiento de montículo (heap overflow/overrun) es un problema aritmético que hace referencia al exceso de flujo de datos sobre un montículo, esto permite un acceso no autorizado a la memoria por …"
resource: https://es.wikipedia.org/wiki/Desbordamiento_de_montículo
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Desbordamiento_de_montículo"}
license: CC BY-SA 4.0
id: eswiki-Desbordamiento_de_montículo
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Desbordamiento de montículo

En **informática**, un **desbordamiento de montículo** (*heap overflow/overrun*) es un problema aritmético que hace referencia al exceso de flujo de datos sobre un montículo, esto permite un acceso no autorizado a la memoria por parte de un comando o de un programa o script denominado shellcode.

Un ejemplo de heap overflow podría ser el siguiente: Supongamos que un programa tiene una función que acepta una cadena de caracteres y la copia en un búfer de memoria en el heap. Si el programador no verifica el tamaño de la cadena antes de copiarla en el búfer, un atacante podría enviar una cadena de caracteres que sea más grande que el tamaño del búfer, lo que provocaría que los caracteres adicionales se escriban en otras áreas de memoria adyacentes. Si estas áreas de memoria contienen información importante, el atacante podría alterarla y hacer que el programa se comporte de manera inesperada.

Para evitar un "heap overflow", los programadores deben asegurarse de que sus programas estén diseñados para manejar correctamente el tamaño de los datos que reciben y asignan en el heap, utilizando técnicas como la validación de la entrada de usuario y el uso de funciones seguras de copia de memoria que verifican los límites de los búferes.

El método de detección más común de desbordamientos del montón es el análisis dinámico en línea. Este método observa la ejecución en tiempo de ejecución de los programas para identificar vulnerabilidades mediante la detección de violaciones de seguridad.

 Véase también

 Desbordamiento de búfer (Buffer overflow/overrun).
 Desbordamiento de pila (Stack overflow/overrun).
 Error de software
 Privacidad digital

 Referencias
