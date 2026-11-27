---
type: Artículo de enciclopedia
title: Parámetro de seguridad
description: "En criptografía, un parámetro de seguridad es una forma de medir lo \"difícil\" que es para un adversario romper un esquema criptográfico."
resource: https://es.wikipedia.org/wiki/Parámetro_de_seguridad
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Parámetro_de_seguridad"}
license: CC BY-SA 4.0
id: eswiki-Parámetro_de_seguridad
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Parámetro de seguridad

En criptografía, un **parámetro de seguridad** es una forma de medir lo "difícil" que es para un adversario romper un esquema criptográfico. Hay dos tipos principales de parámetros de seguridad: los *computacionales* y los *estadísticos*, a menudo denotados por  y  respectivamente. A grandes rasgos, el parámetro de seguridad computacional es una medida del tamaño de la entrada del problema computacional en el que se basa el esquema criptográfico, que determina su complejidad computacional, mientras que el parámetro de seguridad estadístico es una medida de la probabilidad con la que un adversario puede romper el esquema (sea lo que sea que eso signifique para el protocolo).

Los parámetros de seguridad suelen expresarse en representación unaria (por ej.,  se expresa como una cadena de  s, , convencionalmente escrito como ), de modo que la complejidad temporal del algoritmo criptográfico es polinómica en el tamaño de la entrada.

 Seguridad computacional
La seguridad de las primitivas criptográficas se basa en la dureza de algunos problemas difíciles. Se establece el parámetro de seguridad computacional  de forma que el cómputo  se considere intratable.

 Ejemplos

 Si la seguridad de un esquema depende del secreto de una clave para una función pseudoaleatoria (PRF, por sus siglas en inglés), entonces podemos especificar que la clave PRF debe ser muestreada en el espacio  para que una búsqueda de fuerza bruta requiera  de potencia computacional.
 En el criptosistema RSA, el parámetro de seguridad  denota la longitud en bits del módulo *n*; el entero positivo *n* debe ser, por tanto, un número del conjunto {0, ..., 2 - 1}.

 Seguridad estadística
La seguridad en criptografía se basa a menudo en el hecho de que la distancia estadística entre

 una distribución basada en un secreto, y
 una distribución *simulada* producida por una entidad que no conoce el secreto

es pequeña. Formalizamos esto utilizando el parámetro estadístico de seguridad diciendo que las distribuciones son estadísticamente cercanas si la distancia estadística entre las distribuciones puede expresarse como una función insignificante en el parámetro de seguridad. Se establece el parámetro estadístico de seguridad  de forma que  se considera una probabilidad "suficientemente pequeña" de que el adversario gane.

Consideremos las siguientes dos grandes categorías de ataques de adversarios a un esquema criptográfico dado: ataques en los que el adversario intenta aprender información secreta, y ataques en los que el adversario intenta convencer a una parte honesta de que acepte una declaración falsa como verdadera (o viceversa). En el primer caso, por ejemplo un esquema de cifrado de clave pública, un adversario puede ser capaz de obtener una gran cantidad de información a partir de la cual puede intentar aprender la información secreta, por ejemplo examinando la distribución de los textos cifrados para un texto plano fijo cifrado bajo diferentes aleatoriedades. En el segundo caso, puede ser que el adversario deba adivinar un reto o un secreto y pueda hacerlo con cierta probabilidad fija; en este caso podemos hablar de distribuciones considerando el algoritmo de muestreo del reto en el protocolo. En ambos casos, podemos hablar de la posibilidad de que el adversario "gane" en un sentido amplio, y podemos parametrizar la seguridad estadística exigiendo que las distribuciones sean estadísticamente cercanas en el primer caso o definiendo un espacio de desafío dependiente del parámetro de seguridad estadística en el segundo caso.

 Ejemplos

 En los esquemas de encriptación, un aspecto de la seguridad es (a alto nivel) que cualquier cosa que pueda aprenderse sobre un texto plano dado un texto cifrado también puede aprenderse de una cadena muestreada aleatoriamente (de la misma longitud que los textos cifrados) que es independiente del texto plano. Formalmente, habría que demostrar que una distribución uniforme sobre un conjunto de cadenas de longitud fija es estadísticamente cercana a una distribución uniforme sobre el espacio de todos los posibles textos cifrados.
 En los protocolos de conocimiento cero, podemos subdividir los parámetros estadísticos de seguridad en parámetros estadísticos de *conocimiento cero* y de *solidez*. El primero parametriza lo que la transcripción filtra sobre el conocimiento secreto, y el segundo parametriza la probabilidad con la que un prover deshonesto puede convencer a un verificador honesto de que conoce un secreto aunque no lo conozca.
 En la composibilidad universal, la seguridad de un protocolo se basa en la indistinguibilidad estadística de las distribuciones de una ejecución en el mundo real y en el mundo ideal. Curiosamente, para un entorno computacionalmente ilimitado no es suficiente que las distribuciones sean estadísticamente indistinguibles, ya que el entorno puede ejecutar el experimento suficientes veces para observar qué distribución se está produciendo (real o ideal); sin embargo, cualquier adversario autónomo contra el protocolo solo ganará con una probabilidad insignificante en el parámetro de seguridad estadística, ya que solo participa en el protocolo una vez.

 Véase también

 Longitud de la clave
 Función insignificante
