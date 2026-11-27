---
type: Artículo de enciclopedia
title: Conjunto de Instrucciones AES
description: "El Conjunto de instrucciones del Advanced Encryption Standard, también llamado Conjunto de instrucciones AES o directamente AES-NI (del inglés Advanced Encryption Standard New Instructions), es una extensión al conjunto …"
resource: https://es.wikipedia.org/wiki/Conjunto_de_Instrucciones_AES
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Conjunto_de_Instrucciones_AES"}
license: CC BY-SA 4.0
id: eswiki-Conjunto_de_Instrucciones_AES
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Conjunto de Instrucciones AES

El **Conjunto de instrucciones del Advanced Encryption Standard**, también llamado **Conjunto de instrucciones AES** o directamente **AES-NI** (del inglés *Advanced Encryption Standard New Instructions*), es una extensión al conjunto de instrucciones de arquitecturas x86-64 especialmente diseñadas para implementar etapas relacionadas con el uso del algoritmo AES. A veces hay que habilitar esta funcionalidad en la BIOS.

Esta instrucciones están orientadas a poder ser implementadas por hardware especialmente diseñado, normalmente integrado en el propio procesador, para mejorar así la velocidad en la ejecución de AES. Así se puede conseguir un rendimiento entre 3 y 10 veces superior al obtenido utilizando implementaciones software en CPUs. Además,  debido a que las instrucciones de cifrado y descifrado se realizan íntegramente en hardware, sirve para mejorar la resistencia a los ataques de canal lateral de las aplicaciones que utilizan cifrado y descifrado utilizando AES (AES).

Historia

Intel anunció AES-NI en 2008 y en 2010 lanzó los primeros Intel Core que incluyeron por primera vez las instrucciones AES-NI (arquitectura Westmere). Estas instrucciones implementaban las etapas más complejas y computacionalmente más costosas del algoritmo AES usando una implementación vectorial en hardware, permitiendo de esta manera acelerar la ejecución de este algoritmo. AMD anunció y lanzó soporte a AES-NI en 2010, empezando con Bulldozer. Actualmente todos los nuevos procesadores de Intel, AMD y ARM que salen al mercado, excepto los de gama más baja basados en ARM, son compatibles con AES-NI.

Instrucciones
Este conjunto de instrucciones está compuesto por 6 instrucciones de las que 4 instrucciones se usan para el cifrado/descifrado y las 2 restantes se utilizan en la etapa de generación de claves.

En concreto las instrucciones son:
AESENC: Ejecuta una ronda de cifrado
AESENCLAST: Instrucción para la última ronda de cifrado
AESDEC: Instrucción para una ronda de descifrado
AESDECLAST: Instrucción para la última ronda de descifrado
AESKEYGENASSIST: Usada para generar claves para las rondas de cifrado.
AESIMC: Convierte las claves de cifrado a un formato válido para el descifrado.

Inicialmente y por defecto usa 128 bits, pero existen versiones más recientes capaces de tratar bloques de 256 y 512 bits.

Referencias
