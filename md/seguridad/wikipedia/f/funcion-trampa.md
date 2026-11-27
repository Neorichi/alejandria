---
type: Artículo de enciclopedia
title: Función trampa
description: "Una función trampa consiste en una función matemática cuyo cálculo directo es sencillo, pero en la que el cálculo de la función inversa es muy complejo, es decir, involucra un elevado número (por ejemplo, exponencial) …"
resource: https://es.wikipedia.org/wiki/Función_trampa
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Función_trampa"}
license: CC BY-SA 4.0
id: eswiki-Función_trampa
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Función trampa

Una **función trampa** consiste en una función matemática cuyo cálculo directo es sencillo, pero en la que el cálculo de la función inversa es muy complejo, es decir, involucra un elevado número (por ejemplo, exponencial) de operaciones.

A modo de ejemplo, consideramos el producto de números primos

(*p*, *q*) → m = *p* · *q*

La operación anterior es muy rápida, pero la operación inversa, es decir, dado *m* hallar *p* y *q*, es (en general) de complejidad exponencial en la longitud de *m*. Por ejemplo, si *m* tiene 100 cifras, el número medio de operaciones requeridas para factorizar *m* sería 10^50 operaciones, con lo que un ordenador que haga 1 millón de operaciones por segundo tardaría más de 10^36 años.

En este caso, *m* sería utilizado como clave pública en criptografía asimétrica, mientras que los números primos (*p*,*q*) serían la clave privada.

 Véase también
 Criptografía asimétrica
