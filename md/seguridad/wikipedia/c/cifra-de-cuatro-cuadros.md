---
type: Artículo de enciclopedia
title: Cifra de cuatro cuadros
description: "La cifra de los Cuatro Cuadros, también llamada Cuatro Cuadrados o Cuádruple Playfair, y conocido en inglés como Four Square, es una mejora de la cifra Playfair ordinaria con una seguridad ligeramente mayor y con un …"
resource: https://es.wikipedia.org/wiki/Cifra_de_cuatro_cuadros
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifra_de_cuatro_cuadros"}
license: CC BY-SA 4.0
id: eswiki-Cifra_de_cuatro_cuadros
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifra de cuatro cuadros

La **cifra de los Cuatro Cuadros**, también llamada **Cuatro Cuadrados** o **Cuádruple Playfair**, y conocido en inglés como ***Four Square***, es una mejora de la cifra Playfair ordinaria con una seguridad ligeramente mayor y con un proceso de funcionamiento ligeramente distinto, fue creada por el criptógrafo francés Felix María Dellastelle y fue empleada durante la Primera Guerra Mundial. Al igual que su pariente, se trata de una cifra de la clase de las sustituciones polialfabéticas pues cada letra puede ser codificada por más de un símbolo y cada símbolo puede ser traducido como diversas letras. Sin embargo, si se analiza al nivel de pares de letras, es una sustitución monoalfabética.

Proceso de cifrado Cuatro Cuadros

Creación de las matrices de cifrado

Para el presente ejemplo seguiremos la convención de emplear los 26 caracteres del alfabeto internacional y consideraremos a las letras I y J como iguales. Esto no implica que no puedan emplearse cuadrados mayores empleando dígitos, símbolos convencionales, signos de puntuación u otros sistemas de escritura como el alfabeto cirílico con más símbolos.

Lo primero que haremos será generar cuatro matrices de cifrado de 5 por 5 caracteres. Para generar estas cuatro matrices hemos empleado los cuatro primeros versos del "Soneto de repente" de La niña de plata de Lope de Vega. Empleando una línea de cada uno de los cuatro primeros versos para cada matriz. Una vez generadas estas matrices, las ordenamos en forma de cuadrado, así:

  U N S O E      Q U E N M
  M D A H C      I V D A H
  R V I L T      S T O P R
  B F G K P      B C F G K
  Q W X Y Z      L W X Y Z

  C A T O R      B U R L A
  E V S D I      N D O V S
  N Q U B F      T E C F G
  G H K L M      H I K M P
  P W X Y Z      Q W X Y Z

Una vez generadas estas matrices, podemos proceder al cifrado.

Algoritmo de cifrado

Emplearemos como modelo el mensaje: **mensaje de prueba**

Lo primero será dividir el mensaje en pares de letras, como en un Playfair ordinario, pero sin preocuparnos de si las letras están repetidas dentro de los pares de letras.

  pr ue ba de ci fr as

Después localizamos la primera letra en la matriz superior izquierda y la segunda letra en la matriz inferior derecha. De esa forma, obtendremos dos de las esquinas de un paralelepípedo. Las marcamos en cursiva para una más fácil localización en el presente ejemplo.

  U N S O E      Q U E N M
  M D A H C      I V D A H
  R V I L T      S T O P R
  B F G K *P*      B C F G K
  Q W X Y Z      L W X Y Z

  C A T O R      B U *R* L A
  E V S D I      N D O V S
  N Q U B F      T E C F G
  G H K L M      H I K M P
  P W X Y Z      Q W X Y Z

Una vez hecho esto, proseguimos buscando las otras dos esquinas de dicho paralelepípedo, esto es, el punto donde se intersecan las líneas vertical y horizontal que pasan por los puntos marcados por las letras que ya hemos seleccionado. Para una más fácil localización, se marcan en negrita.

  U N S O E      Q U E N M
  M D A H C      I V D A H
  R V I L T      S T O P R
  B F G K *P*      B C **F** G K
  Q W X Y Z      L W X Y Z

  C A T O **R**      B U *R* L A
  E V S D I      N D O V S
  N Q U B F      T E C F G
  G H K L M      H I K M P
  P W X Y Z      Q W X Y Z

En la siguiente tabla de matrices, los elementos no usados se han sustituido por guiones.

  - - - - -      - - - - -
  - - - - -      - - - - -
  - - - - -      - - - - -
  - - - - *P*      - - **F** - -
  - - - - -      - - - - -

  - - - - **R**      - - *R* - -
  - - - - -      - - - - -
  - - - - -      - - - - -
  - - - - -      - - - - -
  - - - - -      - - - - -

Una vez hecho esto, se realiza el mismo procedimiento con cada una de las parejas de letras.

El mensaje final quedará como sigue:

  FR UN KC VQ VM FA HS

Como podemos ver, cada par de letras se codifica de una forma distinta, y la operatividad del sistema (aunque no la creación de las matrices de cifrado) es más sencilla que en Playfair, además, una letra (o incluso un par de letras) puede ser codificada como ella misma.

El proceso de descifrado es simétrico, buscando los pares de letras en las matrices superior derecha e inferior izquierda y encontrando las letras descifradas en las matrices superior izquierda e inferior derecha.

Debilidades criptográficas

Aunque mucho más sólido que una sustitución simple como la cifra de César, no es mucho más seguro que el cifrado de Playfair ordinario. Al igual que Playfair, cada par de letras en el texto llano tiene una y solamente una correspondencia con un par de letras en el texto cifrado. Por lo tanto, es vulnerable al análisis de frecuencias aplicado a los pares de letras (aunque éste es algo más complicado que aplicado a las letras individuales). Presenta sobre Playfair la facilidad de uso al ser una norma simple en lugar de las cuatro o cinco que requiere el más compacto sistema de Playfair.

A diferencia de Playfair, en el Cuatro Cuadros hay un total de 625 pares de letras posibles (25 x 25) pues se permiten las repeticiones. En Playfair, el número más alto de pares de letras posibles es 600 (25 x 24), pues no se permiten las letras dobladas como LL o DD.

Desarrollos derivados

Debido a la dificultad de generar las múltiples matrices, el Ejército alemán, en la Primera Guerra Mundial adoptó una simplificación de este sistema, Doble Cuadro.

Bibliografía

 The Codebreakers – The Story of Secret Writing (ISBN 0-684-83130-9), David Kahn

 Referencias
