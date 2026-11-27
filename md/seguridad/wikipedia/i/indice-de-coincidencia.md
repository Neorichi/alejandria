---
type: Artículo de enciclopedia
title: Índice de coincidencia
description: El Índice de coincidencia es un método desarrollado por William F.
resource: https://es.wikipedia.org/wiki/Índice_de_coincidencia
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Índice_de_coincidencia"}
license: CC BY-SA 4.0
id: eswiki-Índice_de_coincidencia
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Índice de coincidencia

El **Índice de coincidencia** es un método desarrollado por William F. Friedman, en 1920, para atacar cifrados de sustitución polialfabética con claves periódicas.

La idea se fundamenta en analizar la variación de las frecuencias relativas de cada letra, respecto a una distribución uniforme. En un texto cifrado, no se cuenta con información suficiente para hallar tal variación. Sin embargo, se puede obtener por medio del IC. Al hacerlo, será posible aproximar el periodo de la clave. Encontrado el periodo y conociendo el algoritmo de cifrado y el lenguaje (inglés, español, ruso, etc.), se puede usar el método Kasiski para encontrar la clave.

 Empleo
Se separa en texto en filas de igual longitud, se calcula la probabilidad de agarrar dos letras iguales en cada columna y se compara con el IC. La más parecida es la más probable, luego se usan las frecuencias de las letras de cada columna y se resuelve como si fuera un cifrado César.

 Referencias
