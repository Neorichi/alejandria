---
type: Artículo de enciclopedia
title: Fortaleza de seguridad
description: "El nivel de seguridad (en inglés security level), también llamado fortaleza de seguridad (en inglés security strength) o fortaleza criptográfica, para un algoritmo criptográfico o sistema, es un número asociado con la …"
resource: https://es.wikipedia.org/wiki/Fortaleza_de_seguridad
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Fortaleza_de_seguridad"}
license: CC BY-SA 4.0
id: eswiki-Fortaleza_de_seguridad
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Fortaleza de seguridad

El **nivel de seguridad** (en inglés *security level*), también llamado **fortaleza de seguridad** (en inglés *security strength*) o **fortaleza criptográfica**, para un algoritmo criptográfico o sistema, es un número asociado con la cantidad de trabajo (número de operaciones básicas de algún tipo) que se requieren para romper dicho algoritmo criptográfico o sistema. Normalmente se suele expresar en número de bits y por eso a veces se le llama **Nivel de seguridad de bit** (en inglés *bit security level*).

 Cálculo

Si se requieren 2N operaciones de ejecución del algoritmo para romper el algoritmo criptográfico, entonces la fortaleza de seguridad es de N bits.

Supongamos que el sistema es un candado con combinación de 4 dígitos. Entonces hay 10.000 posibles combinaciones (desde 0000 a 9999) que son las que como máximo tendría que probar un ataque por fuerza bruta para romper el sistema. Con 5 dígitos sería 100.000 posibles combinaciones. Si en lugar de ser un candado es una password de tipo entero sin signo de 32 bits entonces hay 232 posibilidades. En ese caso se dice que la fortaleza de seguridad es de 32 bits.

El número de instrucciones de máquina que se requieren para un intento depende de la arquitectura del procesador lo que afecta al tiempo. En criptografía se asume que el tiempo de cada intento es mínimo, ya que es
factible crear un circuito hardware dedicado para un algoritmo criptográfico concreto (ej, las extensiones AES-NI de los procesadores x86-64). Por eso en criptografía, en general, se intenta elevar el Nivel de seguridad de bit, en lugar de incrementar el coste de un intento.

Cuando hablamos de “RSA 2048”, “DH 4096”, o “SHA-256”, el número representa el tamaño de clave/bloque, lo que es distinto de los bits de nivel de seguridad que tiene el algoritmo. La diferencia viene del hecho de que los algoritmo criptográficos confían en la dificultad para resolver ciertos problemas matemáticos, su seguridad es inevitablemente debilitada cuando se hacen progresos para resolver dichos problemas matemáticos. Por ejemplo, avances en factorización de primos implica menos seguridad de RSA. A veces el ataque es específico para un algoritmo, permitiendo al atacante descartar una porción significativa del espacio de claves.

 Ejemplos
A continuación se muestra el nivel de seguridad actual de algunos algoritmos criptográficos conocidos.

 Consideraciones
Respecto al nivel de seguridad se suele considerar:
 80 bits de nivel de seguridad no se considera suficientemente seguro.
 112 bits de nivel de seguridad es suficiente hasta 2030.
 128 bits de nivel de seguridad es suficiente hasta el próximo descubrimiento revolucionario en las matemáticas o de la tecnología.

 Categorías de fortaleza de seguridad del NIST
Las categorías de fortaleza de seguridad establecidas por el NIST permiten cuantificar la seguridad de los algoritmos. El NIST dio tres posibles definiciones de seguridad, dos para cifrado y una para firma, y designó cinco categorías de fortaleza de seguridad para clasificar la complejidad computacional de los ataques que violan las definiciones de seguridad. Las categorías van del 1 al 5 y mayor protección es indicado por un número de categoría superior. Estas categorías estaban basadan en los recursos computacionales requeridas para desarrollar ataques de fuerza bruta contra algoritmos ya definidos en los estándar del NIST (AES y SHA) en una variedad de diferentes modelos de costes de computación, tanto clásico como cuánticos.

Las cinco categorías son:
 Categoría 1. Seguridad equivalente a AES-128. Resistencia cuántica débil.
 Categoría 2. Seguridad equivalente a SHA-256/SHA3-256. Resistencia cuántica fuerte.
 Categoría 3. Seguridad equivalente a AES-192. Resistencia cuántica más fuerte.
 Categoría 4. Seguridad equivalente a SHA-384/SHA3-38. Resistencia muy fuerte.
 Categoría 5. Seguridad equivalente a AES-256. Resistencia cuántica la más fuerte.

El NIST considera las cinco categorías como resistentes a criptografía cuántica, aunque describe la categoría 1 como bastante débil. NIST considera categorías 2 y 3 como probablemente seguras para el futuro inmediato y categorías 4 y 5 como probablemente excesivas y hay que evaluar si merecen la pena haciendo consideraciones de rendimiento e implementación.

 Referencias
