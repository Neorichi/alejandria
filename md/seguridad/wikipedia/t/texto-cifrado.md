---
type: Artículo de enciclopedia
title: Texto cifrado
description: En criptografía, un texto cifrado es el resultado del cifrado realizado sobre un texto plano mediante un algoritmo.
resource: https://es.wikipedia.org/wiki/Texto_cifrado
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Texto_cifrado"}
license: CC BY-SA 4.0
id: eswiki-Texto_cifrado
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Texto cifrado

En criptografía, un **texto cifrado** es el resultado del cifrado realizado sobre un texto plano mediante un algoritmo. El texto cifrado también se conoce como información cifrada o codificada porque contiene una forma del texto plano original que es ilegible para un ser humano o una computadora sin el cifrado adecuado para descifrarlo. El descifrado es el proceso inverso que convierte un texto cifrado en texto legible. El texto cifrado no debe confundirse con el texto de código porque este último es el resultado de un código, no un cifrado.

 Fundamentos conceptuales
Sea   el mensaje de texto plano que Alice quiere transmitir en secreto a Bob y sea  el cifrado, donde  es una clave criptográfica. Alice primero debe transformar el texto sin formato en texto cifrado , para enviar el mensaje a Bob de forma segura, de la siguiente manera:

En un sistema de clave simétrica, Bob conoce la clave de cifrado de Alice. Una vez que el mensaje está encriptado, Alice puede transmitirlo de manera segura a Bob (asumiendo que nadie más conoce la clave). Para leer el mensaje de Alice, Bob debe descifrar el texto cifrado usando  que se conoce como la clave de descifrado,

Alternativamente, en un sistema de claves no simétricas, todos, no solo Alice y Bob, conocen la clave de cifrado; pero la clave de descifrado no se puede inferir de la clave de cifrado. Solo Bob conoce la clave de descifrado   el descifrado procede como

 Tipos de cifrados
La historia de la criptografía comenzó hace miles de años. La criptografía utiliza una variedad de diferentes tipos de cifrado. Los algoritmos anteriores se realizaban a mano y son sustancialmente diferentes de los algoritmos modernos, que generalmente son ejecutados por una máquina.

 Cifrados históricos
Los cifrados históricos con lápiz y papel utilizados en el pasado se conocen a veces como cifrados clásicos. Incluyen:

 Cifrado de sustitución: las unidades de texto sin formato se reemplazan con texto cifrado (por ejemplo, cifrado César y libreta de un solo uso)
 Cifrado de sustitución polialfabético: un cifrado de sustitución que utiliza múltiples alfabetos de sustitución (p. Ej., Cifrado Vigenère y máquina Enigma)
 Cifrado de sustitución poligráfica: la unidad de sustitución es una secuencia de dos o más letras en lugar de solo una (p. Ej., Cifrado de Playfair)
 Cifrado de transposición: el texto cifrado es una permutación del texto sin formato (por ejemplo, cifrado de valla ferroviaria)

Los cifrados históricos no se utilizan generalmente como una técnica de cifrado independiente porque son bastante fáciles de descifrar. Muchos de los cifrados clásicos, con la excepción de la libreta de una sola vez, se pueden descifrar mediante la fuerza bruta.

 Cifrados modernos
Los cifrados modernos son más seguros que los cifrados clásicos y están diseñados para resistir una amplia gama de ataques. Un atacante no debería poder encontrar la clave utilizada en un cifrado moderno, incluso si conoce cualquier cantidad de texto sin formato y el texto cifrado correspondiente. Los métodos de cifrado modernos se pueden dividir en las siguientes categorías:

 Criptografía de clave privada (algoritmo de clave simétrica): se utiliza la misma clave para el cifrado y el descifrado
 Criptografía de clave pública (algoritmo de clave asimétrica): se utilizan dos claves diferentes para el cifrado y el descifrado

En un algoritmo de clave simétrica (por ejemplo, DES y AES), el remitente y el receptor deben tener una clave compartida configurada de antemano y mantenida en secreto para todas las demás partes; el remitente usa esta clave para el cifrado y el receptor usa la misma clave para el descifrado. En un algoritmo de clave asimétrica (por ejemplo, RSA), hay dos claves separadas: se publica una *clave pública* y permite que cualquier remitente realice el cifrado, mientras que el receptor mantiene en secreto una *clave privada* y solo él puede realizar el descifrado correcto.

Los cifrados de clave simétrica se pueden dividir en cifrados de bloque y cifrados de flujo. Los cifrados de bloque operan en grupos de bits de longitud fija, llamados bloques, con una transformación invariable. Los cifrados de flujo cifran dígitos de texto plano uno a la vez en un flujo continuo de datos y la transformación de dígitos sucesivos varía durante el proceso de cifrado.

 Criptoanálisis

El criptoanálisis es el estudio de métodos para obtener el significado de información cifrada, sin acceso a la información secreta que normalmente se requiere para hacerlo. Normalmente, esto implica saber cómo funciona el sistema y encontrar una clave secreta. El criptoanálisis también se conoce como descifrado. El texto cifrado es generalmente la parte más fácil de obtener de un criptosistema y, por lo tanto, es una parte importante del criptoanálisis. Dependiendo de la información disponible y del tipo de cifrado que se esté analizando, los criptoanalistas pueden seguir uno o más modelos de ataque para descifrar un cifrado.

 Modelos de ataque
 Solo texto cifrado: el criptoanalista tiene acceso solo a una colección de textos cifrados o textos de código
 Texto plano conocido: el atacante tiene un conjunto de textos cifrados de los que conoce el texto plano correspondiente.
 Ataque de texto plano elegido: el atacante puede obtener los textos cifrados correspondientes a un conjunto arbitrario de textos planos de su elección.
 Ataque por lotes de texto sin formato elegido: donde el criptoanalista elige todos los textos sin formato antes de cifrarlos. Este es a menudo el significado de un uso incondicional de "ataque de texto plano elegido".
 Ataque adaptativo de texto sin formato elegido: donde el criptoanalista realiza una serie de consultas interactivas, eligiendo los siguientes textos sin formato basándose en la información de los cifrados anteriores.
 Ataque de texto cifrado elegido: el atacante puede obtener los textos sin formato correspondientes a un conjunto arbitrario de textos cifrados de su elección
 Ataque de texto cifrado elegido adaptativo
 Ataque de texto cifrado elegido indiferente
 Ataque de clave relacionada: como un ataque de texto sin formato elegido, excepto que el atacante puede obtener textos cifrados con dos claves diferentes. Se desconocen las claves, pero se conoce la relación entre ellas; por ejemplo, dos claves que se diferencian en un bit.

El modelo de ataque de sólo texto cifrado es el más débil porque implica que el criptoanalista no tiene nada más que texto cifrado. Los cifrados modernos rara vez fallan bajo este ataque.

 Textos cifrados famosos

 Los cifrados de Babington Plot
 La inscripción de Shugborough
 El telegrama de Zimmermann
 The Magic Words are Squeamish Ossifrage
 El criptograma en "El escarabajo de oro"
 Cifrados de Beale
 Kryptos
 Asesino del zodiaco

 Véase también
Cifrado César
Enigma (máquina)
Clave (criptografía)
Función hash criptográfica
Análisis de frecuencias

Referencias

 Lecturas adicionales

En inglés:
 Helen Fouché Gaines, “Cryptanalysis”, 1939, Dover.
 David Kahn, *The Codebreakers - The Story of Secret Writing*  (1967)
 Abraham Sinkov, *Elementary Cryptanalysis: A Mathematical Approach*, Mathematical Association of America, 1968.
