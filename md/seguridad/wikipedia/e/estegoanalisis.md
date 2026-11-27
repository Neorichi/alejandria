---
type: Artículo de enciclopedia
title: Estegoanálisis
description: El estegoanálisis es la disciplina dedicada al estudio de la detección de mensajes ocultos usando esteganografía.
resource: https://es.wikipedia.org/wiki/Estegoanálisis
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Estegoanálisis"}
license: CC BY-SA 4.0
id: eswiki-Estegoanálisis
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Estegoanálisis

El **estegoanálisis** es la disciplina dedicada al estudio de la detección de mensajes ocultos usando esteganografía.  Dichos mensajes pueden estar ocultos en diferentes tipos de medio, como pueden ser por ejemplo las imágenes digitales, los archivos de vídeo, los archivos de audio o incluso un simple texto plano. Como analogía, el estegoanálisis es a la  esteganografía lo que el  criptoanálisis es a la  criptografía. Por otra parte, a diferencia del criptoanálisis donde es necesario descifrar el mensaje para considerar roto un criptosistema, en el caso del estegoanálisis basta con ser capaz de detectar la existencia de un mensaje oculto para considerar el sistema roto.

Tipos de estegoanálisis.

 Estegoanálisis manual: consiste en buscar de forma manual diferencias entre el archivo original y el esteganografía buscando cambios en la estructura para localizar datos ocultos. Los principales inconvenientes de esta técnica son:

- se necesita tener el archivo original.

- es una técnica que solo puede detectar el archivos esteganografiado pero es casi imposible descifrar el mensaje.

 Estegoanálisis estadístico: consiste en el cotejo de la frecuencia de distribución de colores en el caso de un archivo de imagen esteganografiado. Es una técnica lenta para la que se deben emplear software especializado. Aunque estos programas suelen buscar pautas para ocultar los  mensajes que utilizan los programas más habituales de esteganografía, lo que los hace muy eficaces cuando se trata de mensajes ocultos con programas. Los mensajes ocultados manualmente son casi imposibles de encontrar  para estos programas.

El estegoanálisis en casos muy concretos se convierte en una tarea muy trivial pero en general es un tema muy complejo y de difícil aplicación principalmente por el gran número de medios de información existentes y también por las diversas técnicas de esteganografía usadas en el medio.

Programas de estegoanálisis

 Stegdetect
 Stegspy
 Stegsecret

Técnicas para detectar mensajes ocultos en imágenes
Una de las técnicas más conocidas para ocultar información en una imagen es la de sustitución LSB  (least significant bit, bit menos significativo). Esta técnica consiste en reemplazar el bit menos significativo de cada píxel por el bit de información que se quiere ocultar. Este tipo alteración de la imagen no introduce cambios en la imagen que puedan ser detectados a simple vista.

Sin embargo, el uso de técnicas de incrustación de datos basadas en la sustitución LSB, introduce anomalías estadísticas en la imagen que pueden ser detectadas. La inserción de un mensaje sustituyendo el LSB no es una operación simétrica. Cuando se inserta un cero los valores pares siempre conservan su valor, mientras que los valores impares decrementan en uno. Cuando se inserta un uno los valores impares siempre conservan su valor, mientras que los valores pares incrementan en uno. Esto puede ser detectado mediante un histograma de la intensidad de los píxeles, es decir, un gráfico de barras donde cada barra represente la cantidad de píxeles de cada valor. Este histograma será muy diferente en una imagen sin alterar que en una imagen donde se ha escondido un mensaje, dado que la operación asimétrica comentada anteriormente hará que cada barra par siempre ceda píxeles a su barra posterior, y que cada barra impar siempre ceda píxeles a su barra anterior. En consecuencia, las barras tenderán a agruparse en parejas consecutivas que tenderán a tener la misma altura, lo que permitirá detectar la inserción.

Por este motivo las técnicas de sustitución LSB son remplazadas por lo que se conoce como LSB Matching. Esta técnica modifica el valor LSB sumando o restando uno, en lugar de sustituir el LSB. El resultado es el mismo (en cuanto a la modificación del LSB) pero esta operación tiene acarreo, lo que hace que la operación sea simétrica y en consecuencia invulnerable al ataque del histograma, comentado en el apartado anterior. Para detectar sistemas de LSB matching es necesario recurrir a técnicas más complejas, que creen modelos estadísticos de la relación entre un píxel y sus vecinos. De esta manera una imagen puede ser analizada para ver si el modelo estadístico que sigue es el de una imagen original o el de una imagen alterada por la inserción de un mensaje.
