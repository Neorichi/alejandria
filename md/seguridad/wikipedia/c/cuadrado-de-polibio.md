---
type: Artículo de enciclopedia
title: Cuadrado de Polibio
description: Inventado hacia 150 a. C. por el historiador Polibio, el cuadrado de Polibio fue utilizado principalmente por nihilistas rusos encerrados en las prisiones zaristas.
resource: https://es.wikipedia.org/wiki/Cuadrado_de_Polibio
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cuadrado_de_Polibio"}
license: CC BY-SA 4.0
id: eswiki-Cuadrado_de_Polibio
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cuadrado de Polibio

Inventado hacia 150 a. C. por el historiador Polibio, el **cuadrado de Polibio** fue utilizado principalmente por nihilistas rusos encerrados en las prisiones zaristas.

Se trata de un algoritmo trivial, donde cada letra del alfabeto es reemplazada por las coordenadas de su posición en un cuadrado. Es un caso particular de cifrado de sustitución mono-alfabética. Este tipo de código no resiste a un análisis de frecuencias.

 Encriptación
Partimos de una matriz de 5x5 en la que cada casilla es una letra del abecedario. Las filas y las columnas irán numeradas a modo de coordenadas. En este caso hemos juntado la I con la J para poder encajar las 26 letras del abecedario en 25 casillas. Otra versión menos habitual juntaría la U con la V.

También es posible ampliar la matriz a un cuadrado de 36 casillas para poder añadir los números y algunos signos de puntuación.

En cualquier caso, se omitirá cualquier signo diacrítico presente en el mensaje (en el caso del español, la tilde, la diéresis y la virgulilla de la Ñ).
   1  2  3  4  5
   1
  A  B  C  D  E
   2
  F  G  H  I, J  K
   3
  L  M  N  O  P
   4
  Q  R  S  T  U
   5
  V  W  X  Y  Z

De esta manera, para codificar el mensaje sustituiremos las letras por un número de dos cifras que indicará la fila y la columna que ocupaba la letra en el cuadrado. Por ejemplo, la *w* está en la línea 5 y en la columna 2, y por lo tanto, le corresponde el 52.

Poniendo un ejemplo, el texto «Wikipedia, la enciclopedia libre» se codificará así:

 52 24 25 24 35 15 14 24 11 31 11 15 33 13 24 13 31 34 35 15 14 24 11 31 24 12 42 15
  w  i  k  i  p  e  d  i  a  l  a  e  n  c  i  c  l  o  p  e  d  i  a  l  i  b  r  e

 Anécdota
Polibio había imaginado una solución para transmitir los mensajes con antorchas ardiendo. Es una variante del telégrafo óptico.

 Derivadas

En la década de 1880 los nihilistas rusos emplearon un cifrado que empleaba como base este Cuadrado de Polibio, pero lo combinaban con un cifrado de Vigenère. Derivados y modificados de este cifrado fueron usados, más tarde, por el Primer Directorio Principal del KGB y también formaron la base para cifras, como Playfair o las cifras alemanas ADFGX y ADFGVX.

 Referencias
