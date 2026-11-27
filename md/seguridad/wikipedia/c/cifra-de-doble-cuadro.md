---
type: Artículo de enciclopedia
title: Cifra de doble cuadro
description: "La Cifra de doble cuadro, también llamada Dos Cuadrados o Doble Playfair, y conocido en inglés como Two Square, es una mejora de la cifra Playfair ordinaria con una seguridad ligeramente mayor y con un proceso de …"
resource: https://es.wikipedia.org/wiki/Cifra_de_doble_cuadro
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifra_de_doble_cuadro"}
license: CC BY-SA 4.0
id: eswiki-Cifra_de_doble_cuadro
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifra de doble cuadro

La **Cifra de doble cuadro**, también llamada Dos Cuadrados o Doble Playfair, y conocido en inglés como Two Square, es una mejora de la cifra Playfair ordinaria con una seguridad ligeramente mayor y con un proceso de funcionamiento ligeramente distinto, pero fue creada como una simplificación de la cifra de Cuatro Cuadrados. Al igual que su pariente, se trata de una cifra de la clase de las sustituciones polialfabéticas pues cada letra puede ser codificada por más de un símbolo y cada símbolo puede ser traducido como diversas letras. Sin embargo, si se analiza al nivel de pares de letras, es una sustitución monoalfabética.

Proceso de Cifrado Doble cuadro

Creación de las matrices de cifrado

Para el presente ejemplo seguiremos la convención de emplear los 26 caracteres del alfabeto internacional y consideraremos a las letras I y J como iguales. Esto no implica que no puedan emplearse cuadrados mayores empleando dígitos, símbolos convencionales, signos de puntuación u otros sistemas de escritura como el alfabeto cirílico con más símbolos.

Lo primero que haremos será generar dos matrices de cifrado de 5 por 5 caracteres. En el presente caso, las generaremos empleando las frases: "Érase un hombre a una nariz pegado" y "Poderoso caballero es don Dinero" con las que empiezan dos famosos poemas de Quevedo. Se obtienen resultados distintos, pero análogos si los dos cuadros son colocados lado a lado.

  E R A S U
  N H O M B
  I Z P G D
  C F K L Q
  T V W X Y

  P O D E R
  S C A B L
  N I F G H
  K M Q T U
  V W X Y Z

Una vez generadas estas matrices, podemos proceder al cifrado.

Algoritmo de cifrado

Emplearemos como modelo el mensaje: **prueba de cifras**.

Lo primero será dividir el mensaje en pares de letras, como en un Playfair ordinario, pero sin preocuparnos de si las letras están repetidas dentro de los pares de bases.

  pr ue ba de ci fr as

Después localizaremos la primera letra de cada par en la matriz superior y la segunda en la matriz inferior. Las marcamos en negrita para su más fácil visualización.

  E R A S U
  N H O M B
  I Z **P** G D
  C F K L Q
  T V W X Y

  P O D E **R**
  S C A B L
  N I F G H
  K M Q T U
  V W X Y Z

Una vez hecho esto, comprobamos que se ha generado un paralelepípedo del que estas dos letras son ángulos y, al igual que en el cifrado Playfair ordinario, codificamos el par de letras con las otras letras que forman esos ángulos, de modo que la **primera letra sea codificada por una letra de la misma matriz** y **la segunda por una letra de la segunda matriz**, marcando las letra en cursiva. El hecho de que cada letra sea codificada como otra de la misma matriz le da regularidad al sistema y permite que se pueda descifrar. Para mayor claridad expositiva, en la segunda columna de matrices, las letras que no se emplean se sustituyen por guiones.

  E R A S U      - - - - -
  N H O M B      - - - - -
  I Z **P** G *D*      - - **P** - *D*
  C F K L Q      - - - - -
  T V W X Y      - - - - -

  P O *D* E **R**      - - *D* - **R**
  S C A B L      - - - - -
  N I F G H      - - - - -
  K M Q T U      - - - - -
  V W X Y Z      - - - - -

En el caso que nos ocupa, ambas son cifradas con la misma letra (a diferencia de su homólogo Playfair, permite que dos letras iguales sean codificadas).

En caso de que ambas letras estuvieran en la misma vertical (ya que nunca podrían estar en la misma horizontal) serían sustituidas por la que tuvieran debajo, dentro de la misma matriz, siguiendo las normas del cifrado de Playfair (circularmente).

El mensaje final resultará:

  DD SR OL GR FN QO EA

Para descifrar el proceso se invertiría empleando las mismas matrices.

Debilidades criptográficas

Aunque mucho más sólido que una sustitución simple como la cifra de César, no es mucho más seguro que el cifrado de Playfair ordinario. Al igual que Playfair, cada par de letras en el texto llano tiene *una y solamente una correspondencia* con un par de letras en el texto codificado. Por lo tanto es vulnerable al análisis de frecuencias aplicado a los pares de letras (aunque éste es algo más complicado que aplicado a las letras).

A diferencia de Playfair, en el Doble Cuadro hay un total de 625 pares de letras posibles (25 x 25) pues se permiten las repeticiones. En Playfair, el número más alto de pares de letras posibles es 600 (25 x 24), pues no se permiten las letras dobladas como *LL* o *DD*

Bibliografía

 The Codebreakers – The Story of Secret Writing (ISBN 0-684-83130-9), David Kahn

 Referencias
