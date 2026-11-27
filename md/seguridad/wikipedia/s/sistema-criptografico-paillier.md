---
type: Artículo de enciclopedia
title: Sistema criptográfico Paillier
description: El sistema criptográfico Paillier es un algoritmo asimétrico probabilístico utilizado en criptografía de clave pública, inventado por Pascal Paillier en 1999.
resource: https://es.wikipedia.org/wiki/Sistema_criptográfico_Paillier
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sistema_criptográfico_Paillier"}
license: CC BY-SA 4.0
id: eswiki-Sistema_criptográfico_Paillier
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sistema criptográfico Paillier

El **sistema criptográfico Paillier** es un algoritmo asimétrico probabilístico utilizado en criptografía de clave pública, inventado por Pascal Paillier en 1999. Se cree que el problema de calcular las clases del enésimo residuo es computacionalmente difícil. Esto se conoce como *Residuidad Compuesta* y es la base de este sistema criptográfico.

El sistema criptográfico de Paillier encuentra aplicaciones prácticas en diversos ámbitos, incluyendo votaciones electrónicas, loterías electrónicas y subastas electrónicas.

 Esquema

El esquema es un homomorfismo aditivo, es decir, dada la clave pública y los valores  y , es posible calcular , el esquema funciona como sigue:

 Generación de Clave
 Se escogen 2 números primos  y  aleatorios e independientes.
 Se calcula  y
 Seleccionar un entero  tal que
 Se asegura que  divide a  revisando la existencia del siguiente inverso multiplicativo:  donde la función  se define como

Como resultado:
La clave pública es
La clave privada es

 Cifrado
Sea *m* el mensaje a cifrar, tal que
Se escoge un número aleatorio *r*, tal que
El mensaje cifrado es:

 Descifrado
Dado el texto cifrado
El mensaje descifrado es:

 Véase también
 Criptografía asimétrica

 Referencias

 Enlaces externos
The Homomorphic Encryption Project. Implementa el sistema criptográfico de Paillier. (en inglés)
Encounter. librería OpenSource que provee una implementación del sistema criptográfico de Paillier. (en inglés)
