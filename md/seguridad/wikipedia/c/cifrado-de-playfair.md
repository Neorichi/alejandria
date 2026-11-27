---
type: Artículo de enciclopedia
title: Cifrado de Playfair
description: El cifrado de Playfair es un método manual de criptografía simétrica por medio de sustitución.
resource: https://es.wikipedia.org/wiki/Cifrado_de_Playfair
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_de_Playfair"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_de_Playfair
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado de Playfair

El **cifrado de Playfair** es un método manual de criptografía simétrica por medio de sustitución. El sistema de cifrado toma pares de letras, o digramas, y las cambia mediante una tabla generada por una clave.

 Historia

El cifrado de Playfair fue el primer sistema de cifrado en encriptar pares de letras.  Wheatstone inventó el cifrado para encriptar mensajes enviados por telegrama, pero lleva el nombre de su amigo lord Playfair, quien lo promovió para uso militar.

 Proceso de cifrado de Playfair

 Creación de la matriz de cifrado

En esta sustitución digrámica, la clave viene dada por una tabla de 5x5 caracteres (sin las letras J ni Ñ).
Para empezar, colocamos en la primera fila de la matriz la palabra clave sin letras repetidas.

Ejemplo:

Clave: NORIA

Matriz de cifrado resultante:

                              N O R I A
                              B C D E F
                              G H K L M
                              P Q S T U
                              V W X Y Z

 Cifrado de un texto

Reglas para cifrar dos caracteres **m1** y **m2**:
 Si **m1** y **m2** se encuentran en la misma fila, escoger **c1** y **c2** situados a su derecha (circularmente).
 Si **m1** y **m2** se encuentran en la misma columna, escoger **c1** y **c2** situados  debajo (circularmente).
 Si **m1** y **m2** se encuentran en distintas filas y columnas, escoger **c1** y **c2** situados en la diagonal opuesta (siempre de derecha a izquierda).
 Si **m1** = **m2**, insertar carácter sin significado entre **m1** y **m2** para evitar su repetición, y después aplicar las reglas 1-3.
 Si el número de letras es impar, añadir una sin significado al final del texto.

Por ejemplo, en este texto en claro: AT AQ UE CE RO HO RA SX
pondremos X al final, porque al tener el texto un número de letras impar, se requiere una letra sin significado, de relleno, para volver a la paridad. También podrían ponerse letras sin significado al final de cada palabra para evitar confusiones o hacer más claro el texto resultante.

Criptograma resultante: IU OU TF DF IR QC IN XR

 Debilidades criptográficas

Los puntos débiles de Playfair, a la hora de analizarlo eran los siguientes:

 Imposibilidad de que una letra sea codificada como ella misma.
 Se trata de una sustitución simple aplicada a los pares de letras en la que existe una correspondencia unívoca entre cada par de letras y su cifra.
 Cada letra puede sustituirse, exclusivamente, por las que comparten con ella línea o columna en el cuadro, lo que no hace más que ocho en total y puede revelar la estructura del cuadro.
 Dos pares de letras que sean invertidos darán lugar a dos nuevos pares de letras también invertidos. Con el ejemplo anterior, la sílaba **LE** se convertiría en **TL** mientras que la sílaba **EL** se convertiría en **LT**.

 En la cultura popular

 En la película *National Treasure: Book of Secrets*, protagonizada por Nicolas Cage, se observa un ejemplo de la utilización de este código.

 En la novela *Venus Prime II Torbellino*, de Paul Preuss, la protagonista descifra un mensaje que había sido dejado para ella empleando un cifrado por libro y un cifrado de Playfair, con la clave SPARTA. En un apéndice se incluye una descripción del cifrado Playfair en términos generales.

 Variantes de Playfair

Para aumentar la seguridad del sistema de cifrado se crearon las variantes de doble cuadro y de cuatro cuadros. Cada una de ellas, si bien más complicada de usar y generar, tiene también una seguridad algo mayor.

 Playfair seriado

Otra posibilidad es combinar la cifra Playfair con un cifrado por transposición como ocurre con el cifrado **Playfair seriado**. En este se divide el texto en claro en trozos de longitud predeterminada que son colocados pares sucesivos de los bloques. Después, cada uno de los pares de letras resultantes es codificado normalmente. Con el texto: «Prueba de cifra» el resultado, dividiendo en bloques de seis letras sería el siguiente:

  p  r  u  e  b  a  d
  e  c  i  f  r  x  a

Introducimos la letra **x** en undécima posición tanto para crear un número par como para evitar el dígrafo repetido. Los dígrafos a cifrar serían pues los siguientes:

  pe rc ui ef br ax da

Por todo lo demás, sería como cualquier otro cifrado Playfair ordinario.

 Playfair para trigramas

En la página de John Savard se menciona una posibilidad de cifrar las letras de tres en tres empleando Playfair ignorando la regla de prohibición de las repeticiones. De ese modo las reglas de cifrado quedarían como sigue:

 Si las tres letras son iguales (**m1** = **m2** = **m3**) se sustitutyen por la que está en la línea inferior y a la derecha.
 Si dos letras son iguales (por ejemplo el trío RAR), se cifrarían con las reglas ordinarias de Playfair explicadas más arriba (con el ejemplo que ya hemos visto, RAR devendría INI, SAS denvendría RUR, AFA devendría FMF)
 Si las tres letras son distintas estarían dentro de alguna de las siguientes posibilidades:
 **En la misma línea**: se sustituirían por la letra de la derecha.
 **En la misma columna**: se sustituirían por la letra de debajo.
 **Dos en la misma línea y la tercera en la misma columna que una de ellas** (por ejemplo, COR): reemplazar esta tercera por la que está en la misma columna que la otra letra (con la que no compartía columna). Las dos letras de la misma línea se sustituirán entre sí (con el ejemplo COR devendría DRO).
 **Dos en la misma columna y la tercera en línea y columna distinta** (por ejemplo, TAF): reemplazar las letras que comparten columna con las de la misma línea en la columna de la tercera y la tercera letra con la de la misma línea que comparte columna con las coincidentes (con el ejemplo TAF devendría UIE).
 **Dos en la misma línea y la tercera en línea y columna distinta** (por ejemplo, SAN): reemplazar las letras que comparten línea por las de la misma columna en la línea de la tercera, y la tercera letra por la de su misma columna que comparta línea con las otras dos (con el ejemplo SAN devendría RUP).
 **Cada una de las letras está en línea y columna distinta** (por ejemplo, HAY): reemplazar cada letra por la que esté en la misma línea, pero en la columna correspondiente a la siguiente letra del trigrama (con el ejemplo HAY devendría MIW).

 Playfair con otros alfabetos

Otras posibilidades, referentes al tamaño de los cuadros que forman la base del cifrado pueden hacerse incorporando letras que no estén en el alfabeto latino básico (letras como la Ñ española o la Ł) polaca), incorporando dígitos, signos de puntuación y otros signos arbitrarios (como # o &). También puede aprovecharse de los distintos números de letras que tienen los alfabetos cirílico, griego o hebreo, entre otros.

En esto casos puede aumentarse o disminuirse el tamaño del cuadro, según convenga.

 Referencias

 Bibliografía

 Smith, Michael *Station X: The Codebreakers of Bletchley Park* (1998, Channel 4 Books/Macmillan, London)

 Enlaces externos

 Cifrado de Playfair en SQL SERVER
