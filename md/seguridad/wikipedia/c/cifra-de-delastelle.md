---
type: Artículo de enciclopedia
title: Cifra de Delastelle
description: "La cifra de Delastelle debe su nombre a su inventor, el francés Félix-Marie Delastelle (1840-1902), quien había descrito por primera vez el principio en la Revue du Génie civil en 1895, bajo el nombre de \"nueva …"
resource: https://es.wikipedia.org/wiki/Cifra_de_Delastelle
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifra_de_Delastelle"}
license: CC BY-SA 4.0
id: eswiki-Cifra_de_Delastelle
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifra de Delastelle

La **cifra de Delastelle** debe su nombre a su inventor, el francés Félix-Marie Delastelle (1840-1902), quien había descrito por primera vez el principio en la *Revue du Génie civil* en 1895, bajo el nombre de "nueva criptografía". Se trata de un algoritmo que se aprovecha del fraccionamiento de los elementos del mensaje a través de unos procedimientos entremezclados de transposición y de substitución.

Esta cifra presenta dos variantes, la cifra bífida y la cifra trífida.

Cifra Bífida de Delastelle

El algoritmo utiliza una cuadrícula de cifrado / descifrado análoga a la del cuadrado de Polibio. Luego de anotar las coordenadas (abscisas y ordenadas) de varias letras sin cifrar, mezcla las coordenadas y lee después en la cuadrícula las letras cifradas con las coordenadas mezcladas. Una consecuencia importante de esto es que las cuadrículas de cifrado deben ser cuadradas por lo que el número de letras o símbolos que se podrán cifrar será siempre un cuadrado perfecto: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100...

Este procedimiento se llama también **tomográmico**.

Modo de Operación

Lo mostraremos con un ejemplo:

Emplearemos la siguiente cuadrícula, generada empleando como base la primera frase del Quijote, con un dígito tras cada palabra para codificar el mensaje: “este mensaje secreto”.

La cuadrícula ha sido escogida porque incluye tanto letras como números. Dado que el alfabeto español incluye 27 letras, las letras Q y K, infrecuentes y difíciles de confundir, se considerarán como la misma.

Dividiremos las letras del mensaje en grupos de cinco letras con lo que nos quedaría:

  estem    ensaj    esecr    eto

Por lo tanto el mensaje sería sustituido de acuerdo con la cuadrícula anterior y cada sustitución será escrita por debajo de la letra que codifica en dos líneas, en la primera la referencia vertical en la segunda, la horizontal.

  estem    ensaj    esecr   eto
  adeab    abdbb    adacc   aeb
  aeeac    aaebf    aeacb   aed

Una vez hecho esto, ordenamos los grupos de tal forma que los leamos a la horizontal, pero cada grupo de 5 de modo independiente, así:

  adeab  aeeac  abdbb  aaebf  adacc  aeacb  aeb  aed

A continuación, sustituimos los pares de letras, leyendo a la horizontal y agrupando del mismo modo que el mensaje original. Cada grupo de cinco letras quedará por encima del nuevo mensaje codificado. Para diferenciar, las letras serán mayúsculas.

  estem      ensaj      esecr   eto
  adeab      abdbb      adacc   aeb
  aeeac      aaeaf      aeacb   aed
  Y2NT5      G3NKJ      Y512R   QN9

Si para este paso final emplearemos una cuadrícula matriz diferente, estaríamos hablando de un sistema de matrices conjugadas.

Debilidades
La cifra de Delastelle codifica cada grupo por separado, como un bloque, no obstante, bloques similares, dan como resultado bloques similares, que se diferencian, exclusivamente, en una o, a lo sumo, dos letras del anterior. Esto da una pista a los analistas. Este hecho de que, con el simple cambio de una letra, puedan cambiar una o dos letras del resultado final indica que existe una cierta difusión, en el sentido que Shannon dio a esa palabra.

Cifra Trífida de Delastelle

La cifra trífida sigue el mismo principio pero en vez de utilizar una simple cuadrícula trazada en el plano, emplea un conjunto de coordenadas tridimensional (ejes X, Y y Z, de ahí que sea trífida pues cada símbolo es localizado mediante la conjunción de tres valores) al emplear tantas cuadrículas como la altura y anchura de la misma. Una consecuencia importante de esto es que el número de símbolos a cifrar será siempre un cubo perfecto: 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000...

Modo de Operación

Lo mostraremos con un ejemplo:

Emplearemos las siguientes tablas, generadas empleando como base la primera frase del Quijote, para codificar el mensaje: “este mensaje secreto”.

Las tablas incluyen las 27 letras del alfabeto español, dado que el número es un cubo perfecto. Otra forma de ordenarlas sería en tres dimensiones con unas apiladas encima de las otras.

Dividiremos las letras del mensaje en grupos de cinco letras con lo que nos quedaría:

  estem    ensaj    esecr    eto

Por lo tanto el mensaje sería sustituido de acuerdo con las tablas anteriores y cada sustitución será escrita por debajo de la letra que codifica en tres líneas, en la primera, la referencia vertical; en la segunda, la horizontal; en la tercera línea, la referencia a la tabla concreta (o al nivel de la misma si las hubiésemos apilado). Estas tres líneas corresponden con las referencias en los ejes X, Y y Z.

  estem    ensaj    esecr    eto
  acaac    abcca    acaaa    aaa
  acaac    aacbb    acaac    aab
  abcaa    aabac    ababa    acb

Una vez hecho esto, reordenamos los grupos de tal forma que los leamos a la horizontal, pero cada grupo de 5 de modo independiente, así:

  acaac  acaac  abcaa  abcca  aacbb  aabac  acaaa  acaac  ababa  aaa  aab  acb

A continuación, sustituimos los tríos de letras, leyendo a la horizontal y agrupando del mismo modo que el mensaje original. Cada grupo de cinco letras quedará por encima del nuevo mensaje codificado. Para diferenciar, las letras serán mayúsculas.

  estem    ensaj    esecr   eto
  acaac    abcca    acaaa   aaa
  acaac    aacbb    acaac   aab
  abcaa    aabac    ababa   acb
  RRUYU    JUINZ    REUYL   ECI

Si para este paso final emplearemos una cuadrícula matriz diferente, estaríamos hablando de un sistema de matrices conjugadas.

Debilidades
La cifra de Delastelle codifica cada grupo por separado, como un bloque, no obstante, bloques similares, dan como resultado bloques similares, que se diferencian, exclusivamente, en una o, a lo sumo, dos letras del anterior. Esto da una pista a los analistas. Este hecho de que, con el simple cambio de una letra, puedan cambiar una, dos o hasta letras letras del resultado final indica que existe una cierta difusión, en el sentido que Shannon dio a esa palabra. Esta difusión es mayor que en la variante bífida por lo que, pese a su mayor dificultad de trabajo, es algo más segura.

Publicación

El *Traité élémentaire de cryptographie de Delastelle*, único criptógrafo civil importante de la época, fue publicado por Gauthier-Villars en 1902.

 Referencias
