---
type: Artículo de enciclopedia
title: Número semiprimo
description: En matemáticas, un número semiprimo, también llamado biprimo, es un número natural que es producto de dos números primos no necesariamente distintos.
resource: https://es.wikipedia.org/wiki/Número_semiprimo
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Número_semiprimo"}
license: CC BY-SA 4.0
id: eswiki-Número_semiprimo
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Número semiprimo

En matemáticas, un **número semiprimo**, también llamado **biprimo**, es un número natural que es producto de dos números primos no necesariamente distintos. Los semiprimos menores que 100 son 4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, y 95. . Los semiprimos que no son cuadrados perfectos se denominan discretos, o directamente semiprimos.

 Propiedades

El número total de factores primos Ω(*n*) para un semiprimo *n* es dos, por definición. Un semiprimo, o es un cuadrado de un primo o un entero libre de cuadrados. Un número compuesto  no divisible por los primos  es semiprimo. Puesto que el cuadrado de cualquier número primo es semiprimo, el mayor semiprimo conocido será siempre el cuadrado del mayor primo conocido, a menos que los factores del semiprimo no se sepan.

En 1966, el matemático chino Chen Jingrun demostró que todo número par suficientemente grande puede expresarse como suma de dos primos o como la suma de un primo y de un número que es la multiplicación de dos primos. ("*semi*-primo").

El valor de la función φ de Euler para un semiprimo *n* = *pq* es particularmente simple cuando *p* y *q* son distintos:
φ(*n*) = *n* + 1 − (*p* + *q*).

 Utilidades
Los semiprimos son altamente útiles en el área de la criptografía y de la teoría de números, notablemente en la criptografía asimétrica donde son utilizados por el RSA y en las secuencias pseudoaleatorias tales como Blum Blum Shub. Estos métodos se basan en el hecho de que encontrar dos números primos grandes y multiplicarlos luego es computacionalmente sencillo, mientras que encontrar los factores originales es más difícil. En la competición de factorización RSA, RSA Security ofreció premios por la factorización de semiprimos grandes específicos. El desafío se cerró en 2007.

En criptografía práctica, no es suficiente con elegir un semiprimo; un buen número semiprimo debe evadir un grupo bien conocido de algoritmos de propósito específico que puedan identificar números de cierta forma. Los factores *p* y *q* de *n* deben ser muy grandes, alrededor del mismo orden de magnitud que la raíz cuadrada; esto hace la división por tentativa y el Algoritmo rho de Pollard impracticable. Al mismo tiempo no pueden estar demasiado juntos, o si no el número puede ser rápidamente factorizado por el método de factorización de Fermat. El número se debe elegir también  de modo que ninguno de *p*−1, *p*+1, *q*−1, o *q*+1 sean números lisos, protegiéndolo contra el algoritmo *p*-1 de Pollard o el algoritmo *p*+1 de Williams. Estas comprobaciones no se pueden tomar en cuenta para algoritmos futuros o algoritmos secretos, introduciendo la posibilidad de que los números que se usan hoy puedan ser descifrados por algoritmos de propósito específico más adelante.

En 1974 el mensaje de Arecibo fue enviado con una señal de radio que tuvo como objetivo un cúmulo estelar. Consistió en 1679 dígitos binarios previstos para ser interpretado como imagen bitmap. El número 1679 = 23×73 fue elegido porque es un semiprimo y por lo tanto puede ser analizado solamente en 23 filas y 73 columnas, o 73 filas y 23 columnas.

 Véase también
 Criptografía
 Número primo

 Referencias

 Enlaces externos
