---
type: Artículo de enciclopedia
title: Criptografía visual
description: La criptografía visual es una técnica de cifrado que permite codificar información visual (como imágenes, texto, etc.) de manera que la información descifrada se presente como una imagen visual.
resource: https://es.wikipedia.org/wiki/Criptografía_visual
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_visual"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_visual
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía visual

La **criptografía visual** es una técnica de cifrado que permite codificar información visual (como imágenes, texto, etc.) de manera que la información descifrada se presente como una imagen visual.

Una de las técnicas más reconocidas fue desarrollada por Moni Naor y Adi Shamir en 1994.  Presentaron un esquema de intercambio de secretos visuales en el que una imagen binaria se divide en *n* partes, de manera que solo quien posea todas las *n* partes pueda reconstruir la imagen, mientras que cualquier conjunto de *n − 1* partes no revelará información sobre la imagen original. Cada parte se imprimió en una transparencia independiente, y el proceso de descifrado se lleva a cabo al superponer las partes. Al superponer las *n* partes, la imagen original se revela.Hay varias generalizaciones del esquema básico, incluida la criptografía visual *k* de *n*, y el uso de láminas opacas pero iluminándolas con múltiples conjuntos de patrones de iluminación idénticos bajo el registro de un solo detector de un solo píxel.

Siguiendo una idea similar, se pueden utilizar transparencias para implementar un cifrado de un solo uso, donde una transparencia representa una clave aleatoria compartida y la otra actúa como el texto cifrado. Normalmente, hay una expansión del requisito de espacio en la criptografía visual. Sin embargo, si una de las dos partes se organiza de forma recursiva, la eficiencia de la criptografía visual puede incrementarse hasta alcanzar el 100%.

Algunos antecedentes de la criptografía visual pueden rastrearse en patentes de la década de 1960.Otros orígenes se encuentran en estudios sobre la percepción y la comunicación segura.

La criptografía visual puede emplearse para proteger plantillas biométricas, permitiendo su descifrado sin necesidad de cálculos complejos.

 Ejemplo

En este ejemplo, la imagen binaria se ha dividido en dos imágenes componentes. Cada una de estas imágenes contiene un par de píxeles por cada píxel de la imagen original. Estos pares de píxeles se colorean de negro o blanco según la siguiente regla:

 Si el píxel de la imagen original es negro, los pares de píxeles en las imágenes componentes deben ser complementarios, es decir, uno debe ser ■□ y el otro □■, seleccionados de forma aleatoria. Cuando estos pares complementarios se superponen, producen un tono de gris oscuro.
 Si el píxel de la imagen original es blanco, los pares de píxeles en las imágenes componentes deben coincidir, es decir, ambos deben ser ■□ o ambos □■. Cuando estos pares coincidentes se superponen, producen un tono de gris claro.

Cuando se superponen las dos imágenes componentes, la imagen original se revela. Sin embargo, por sí sola, una imagen componente no proporciona información sobre la imagen original; es indistinguible de un patrón aleatorio de pares ■□ / □■. Además, al contar con una imagen componente, se pueden aplicar las reglas de sombreado mencionadas anteriormente para generar una imagen componente falsa que, al combinarse con la original, produzca cualquier imagen deseada.

 (2, *n* ) caso de intercambio de criptografía visual

Compartir un secreto con un número arbitrario de personas, *n*, de modo que al menos dos de ellas sean necesarias para decodificarlo, es una variante del esquema de intercambio de secretos visuales propuesto por Moni Naor y Adi Shamir en 1994. En este esquema, una imagen secreta se codifica en *n* partes, que se imprimen en transparencias. Las partes parecen aleatorias y no contienen información descifrable sobre la imagen secreta subyacente; sin embargo, cuando dos de estas partes se superponen, la imagen secreta se vuelve legible para el ojo humano.

Cada píxel de la imagen secreta se representa mediante varios subpíxeles en cada imagen compartida, utilizando una matriz para definir el color de los píxeles. En el caso *(2, n)*, un píxel blanco de la imagen secreta se codifica a través de una matriz elegida de entre el siguiente conjunto, donde cada fila corresponde al patrón de subpíxeles de uno de los componentes:

{todas las permutaciones de las columnas de} :

Por otro lado, un píxel negro en la imagen secreta se codifica utilizando una matriz seleccionada del siguiente conjunto:

{todas las permutaciones de las columnas de} :

Por ejemplo, en un esquema de compartición de secretos (2,2), donde el secreto se divide en dos partes y ambas son necesarias para su decodificación, se emplean matrices complementarias para representar un píxel negro y matrices idénticas para representar un píxel blanco. Al superponer las partes, todos los subpíxeles correspondientes a un píxel negro se tornan negros, mientras que el 50% de los subpíxeles asociados a un píxel blanco permanecen blancos.

 Cómo engañar al sistema de intercambio de secretos visuales (2, *n* )
Horng et al. propusieron un método que permite que *n − 1* partes coludidas engañen a una parte honesta en el contexto de la criptografía visual. Aprovechan el conocimiento de la distribución subyacente de los píxeles en las acciones para generar nuevas acciones que, al combinarse con las acciones existentes, forman un nuevo mensaje secreto seleccionado por los tramposos.

Sabemos que dos acciones son suficientes para decodificar la imagen secreta utilizando el sistema visual humano. No obstante, al analizar dos acciones también se obtiene información sobre la tercera acción. Por ejemplo, los participantes coludidos pueden comparar sus acciones para identificar cuándo ambos tienen píxeles negros y usar esa información para inferir que otro participante también tendrá un píxel negro en esa misma ubicación. Al conocer la ubicación de los píxeles negros en el recurso compartido de otro, pueden crear un nuevo recurso compartido que, al combinarse con el recurso compartido original, forme un nuevo mensaje secreto. De esta forma, un grupo de partes coludidas con suficientes acciones para acceder al código secreto puede engañar a las partes honestas.

 Esteganografía visual

Los subpíxeles 2×2 también pueden utilizarse para codificar una imagen binaria en cada imagen componente, como se muestra en el esquema de la derecha. Cada píxel blanco de cada imagen componente se representa con dos subpíxeles negros, mientras que cada píxel negro se representa con tres subpíxeles negros.

Al superponerse, cada píxel blanco de la imagen secreta se representa con tres subpíxeles negros, mientras que cada píxel negro se representa con cuatro subpíxeles negros. Además, cada píxel correspondiente en las imágenes componentes se rota de manera aleatoria para evitar que la orientación revele información sobre la imagen secreta.

 En la cultura popular

 En " Do Not Forsake Me Oh My Darling ", un episodio de 1967 de la serie de televisión *The Prisoner*, el protagonista utiliza una superposición de criptografía visual de múltiples transparencias para revelar un mensaje secreto: la ubicación de un amigo científico que se había escondido

 Véase también

 Rejilla (criptografía)
 Esteganografía

 Referencias

 Enlaces externos

 Implementación de Java e ilustraciones de criptografía visual
 Implementación de criptografía visual en Python
 Criptografía visual en máquinas de cifrado y criptología
 Página de criptografía visual de Doug Stinson
 Liu, Feng; Yan, Wei Qi (2014) Criptografía visual para procesamiento de imágenes y seguridad: teoría, métodos y aplicaciones, Springer
