---
type: Artículo de enciclopedia
title: Escítala
description: Una escítala (, skytálē) es un sistema de criptografía utilizado por los éforos espartanos para el envío de mensajes secretos.
resource: https://es.wikipedia.org/wiki/Escítala
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Escítala"}
license: CC BY-SA 4.0
id: eswiki-Escítala
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Escítala

Una **escítala** (, *skytálē*) es un sistema de criptografía utilizado por los éforos espartanos para el envío de mensajes secretos. Está formada por dos varas del mismo grosor y una tira de cuero o papiro.  Tanto la vara como la tira se llaman escítala.

El sistema consistía en dos varas del mismo grosor que se entregaban a los participantes de la comunicación. Para enviar un mensaje se enrollaba cuidadosamente en espiral una tira de cuero o papiro en torno a una de las varas (alineando los filos de la tira, sin dejar espacios en blanco ni solapando la tira) y se escribía el mensaje longitudinalmente (a lo largo de la vara, una letra en cada cara de la tira). Una vez escrito el mensaje, se desenrollaba la tira y se enviaba al receptor, que sólo tenía que enrollarla cuidadosamente a la vara gemela para leer el mensaje original.

Podemos encontrar una descripción del procedimiento en la obra de Plutarco, *Vida de Lisandro*.

 Transposición en Criptografía
La transposición es uno de los métodos  más empleados en criptografía, y consiste en alterar el orden de los elementos de un mensaje. El método utilizado en la *escítala* es la transposición más elemental: una transposición seriada continua (no tiene saltos). Este método es también conocido como *transposición de matrices*. En algoritmos aplicados a imágenes equivale a una rotación de 90° a la derecha y luego expresada horizontalmente.

En el caso de la escítala, es equivalente a disponer en una tabla cada uno de los elementos en filas y luego tomarlos en columnas, siendo el número de columnas el número de caras que presenta la escítala, y el número de filas la cantidad resultante de dividir la longitud total del mensaje por el número de columnas.

 Ejemplo de aplicación

Sea el mensaje a cifrar: «*En un lugar de la Mancha, de cuyo nombre no quiero acordarme*», y sea la escítala de 10 caras. Se construye entonces una tabla de 10 columnas (número de caras) y 6 filas, resultado de dividir la longitud del mensaje (60 caracteres) por el número de columnas o caras. A continuación se escribe el texto secuencialmente a lo largo de las filas, como se aprecia en la imagen de la izquierda.

El texto cifrado es el resultado de tomar linealmente, sin saltos, la misma tabla pero ahora recorriéndola en columnas. El mensaje cifrado queda así: «*Ernu  n cyna dhoocuea  on ,nqr l oudladmiau ebergM rrmaaceoe*».

Descifrar el texto con la escítala es volver a enrollar la tira de cuero sobre una vara que tenga el mismo número de caras y el mismo grosor que el de la vara original sobre la que se escribió en mensaje. El mensaje recibido queda descifrado volviendo a aplicar el mismo método, sin más que intercambiar filas y columnas sobre la tabla. En la imagen de la derecha puede apreciarse que el texto queda descifrado leyendo secuencialmente a lo largo de las columnas.

En la escítala y con texto legible por humanos pueden omitirse los espacios en blanco y otros signos de puntuación. Con ello el mensaje resulta más breve y críptico, y una vez descifrado no resulta mucho más complejo de comprender. Para una mayor claridad del ejemplo, en las imágenes se ha optado por incluirlos.

 Particularidades
Cuando el mensaje no llena (o cabe, según se considere) completamente la tabla, debe considerarse (esto es: largo(mensaje)/caras no es entero) que se debe añadir una fila más y los caracteres de esta fila incompleta considerarse espacios en blanco.

De cara a descifrar un mensaje, tal conjunto de caracteres vacíos puede suponer una pista para deducir el número de caras (ancho de la tabla sin cifrar, alto de la tabla cifrada), con que está cifrado el mensaje.

Completar de dicha forma una tabla arroja muchas pistas acerca del tamaño de tabla, pues queda claro que la misma debe de ser el producto de sus divisores. Al respecto, la tabla (de las imágenes que se acompaña de ejemplo) se ha creado a propósito con 10 filas y 6 columnas, a fin de ilustrar esto mismo. Siendo 60 caracteres la tabla tiene como factores: 5, 3, 2, 2 y, por lo tanto, hay 10 posibles tamaños de la tabla (el sumatorio de 4 elementos). Posibilidades del ejemplo: *"2 * 30 , 3 * 20 , 4 * 15, 5 * 12, 6 * 10, 10 * 6, 12 * 5, 15 * 4, 20 * 3, 30 * 2"*.
Un modo de solventar esto sería que un posible algoritmo basado en el método añadiera una cantidad de caracteres aleatorios (al final, al principio, en ambos sitios, o incluso, repartido dentro), datos que deberían constar en la clave.

Tanto el primer carácter como el último son los únicos que conservan su posición antes y después del cifrado. En textos muy cortos (palabras, frases cortas), pueden usarse dichos 2 caracteres como un sencillo método de verificación de integridad. Si la tabla es cuadrada, todos los elementos que forman la diagonal (desde la posición 0 hasta el final) también conservan su posición original antes y después del cifrado.

 En la cultura popular

La escítala tiene una participación predominante en uno de los cómics de la serie de Blake y Mortimer, llegando a darle título al mismo: *La vara de Plutarco*, publicado en 2015.

 Notas
Hablamos de caras para que quede perfectamente claro la implicación de una cantidad de caracteres por cada revolución alrededor de la vara. En la práctica podían ser redondos, ovalados, etc... Con caras pues, se pretende indicar la cantidad de caracteres que, dado el tamaño de estos sobre la tira escrita, resultan por cada espira, dado el radio de la vara. Resulta más cómodo si lo resumimos tal como si fueran caras de una vara con sección poligonal.

 Referencias
