---
type: Artículo de enciclopedia
title: Método de cinta móvil
description: El Método de cinta móvil fue el sistema criptográfico oficial del Ministerio de la Guerra español durante las últimas décadas del y primeras del .
resource: https://es.wikipedia.org/wiki/Método_de_cinta_móvil
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Método_de_cinta_móvil"}
license: CC BY-SA 4.0
id: eswiki-Método_de_cinta_móvil
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Método de cinta móvil

El **Método de cinta móvil** fue el sistema criptográfico oficial del Ministerio de la Guerra español durante las últimas décadas del  y primeras del . Se trata de un ejemplo de sustitución homofónica pero no es demasiado seguro.

Funcionamiento

El funcionamiento es relativamente sencillo, en primer lugar hay que elaborar una tabla de homófonos vinculando las letras del alfabeto con los números comprendidos entre el 10 y el 99, ambos incluidos. Hay que asegurarse de que ninguna letra está representada por más de cuatro números ni por menos de tres. Un ejemplo podría ser la tabla siguiente:

Esta tabla está adaptada a las que empleaba el Ministerio de la Guerra español y, por lo tanto, incluye la letra Ñ pero no la W, tablas distintas pueden elaborarse para otros idiomas incluso empleando alfabetos distintos.

El segundo elemento de la cifra es la presencia de una cinta móvil (o corrediza) que está dividida en casillas de la misma anchura que las casillas de la tabla que representan las letras del alfabeto. Esta cinta corrediza debe tener una longitud igual a dos veces el alfabeto elegido y debe incluir, repetidamente, todas las letras de dicho alfabeto de modo que se pueda hacer coincidir cualquier letra de la cinta corrediza con cualquier letra de la tabla escogida.

Esta cinta corrediza puede tener el mismo orden de letras que en el alfabeto de la tabla (en cuyo caso se trataría de un desplazamiento análogo al de la cifra de César) o tratarse de un alfabeto perturbado como es el caso de la tabla escogida como ejemplo donde se ha escogido la palabra clave: EUFORICAS.

En la tabla precedente, la cinta móvil ha sido representada por la segunda fila de la tabla y se ha iniciado la misma por la letra D (las letras F e I coinciden entre el alfabeto perturbado y el ordinario).

Una vez hecho esto, podemos escoger como ejemplo la palabra CHOCOLATERO que presenta repeticiones en las letras C (2 veces) y O (3 veces).

Por tanto, la palabra sería enviada como: **51-79-37-25-11-93-13-46-10-24-62**.

Los elementos definitorios de la clave son la disposición de los números en la tabla elegida, la perturbación en el alfabeto de la cinta corrediza y la correspondencia de la cinta con el alfabeto de la tabla.

Para la época de la Guerra Civil, las tablas habían sido ampliadas para incluir, también, los números entre el 00 y el 09, ambos incluidos.

Debilidades

El teniente J. G. Carmona se muestra muy crítico con este sistema por considerarle muy poco seguro, entre los defectos que le señala se encuentran:

 Es muy lento de cifrar y descifrar.
 Incluso con partes cortos es posible descifrarlo sin poseer la clave.
 Es proclive a la comisión de errores tanto de cifrado y descifrado como de transmisión (en el caso de los errores de transmisión, se hacen más fáciles debido a que, en la década de 1890, debían ser transmitidos en lenguaje Morse donde los dígitos no son tan distintivos como las letras).
 Fuerza a que cada letra del mensaje sea codificada por dos dígitos.

Referencias
