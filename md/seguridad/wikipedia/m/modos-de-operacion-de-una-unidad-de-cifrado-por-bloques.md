---
type: Artículo de enciclopedia
title: Modos de operación de una unidad de cifrado por bloques
description: En criptografía, un modo de operación es un algoritmo que utiliza un cifrador por bloques para proveer seguridad a la información, como confidencialidad y autenticidad.
resource: https://es.wikipedia.org/wiki/Modos_de_operación_de_una_unidad_de_cifrado_por_bloques
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Modos_de_operación_de_una_unidad_de_cifrado_por_bloques"}
license: CC BY-SA 4.0
id: eswiki-Modos_de_operación_de_una_unidad_de_cifrado_por_bloques
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Modos de operación de una unidad de cifrado por bloques

En criptografía, un modo de operación es un algoritmo que utiliza un cifrador por bloques para proveer seguridad a la información, como confidencialidad y autenticidad. Un cifrador por bloques en sí mismo sólo es adecuado para la transformación criptográfica segura (cifrado y descifrado) de un grupo de bits de longitud fija llamado bloque (a menudo de 64 a 128 bits). Un modo de operación describe cómo aplicar repetidamente una operación de cifrado en un bloque simple para la transformación segura de cantidades de datos mayores que un bloque.

La mayoría de los modos requiere una secuencia binaria única, usualmente llamada vector de inicialización (IV), para cada operación de encriptación. El IV no tiene por qué repetirse y para algunos modos es aleatorio. El vector de inicialización se utiliza para asegurar que se generen textos cifrados distintos, aun cuando sea el mismo texto el que se encripte varias veces y con la misma clave. Los cifradores por bloques pueden manejar bloques de diferentes tamaños pero, durante la transformación, éste se mantiene siempre fijo. Los modos de cifrado por bloques operan con bloques completos, por lo que es necesario que la última parte del bloque sea rellenada, si acaso su tamaño fuera menor que el de los anteriores a él. Sin embargo, hay modos que no necesitan dicho rellenado porque emplean un cifrador por bloques, como cifrador en flujo, de forma muy efectiva.

Los primeros modos descritos, como ECB, CBC, OFB y CFB, aseguraban la confidencialidad del mensaje, pero no su integridad. Otros modos se diseñaron para asegurar ambas características, la confidencialidad y la integridad del mensaje, tales como: modo CCM, modo EAX y modo OCB.

 Vector de Inicialización
Un vector de inicialización (IV) o variable de inicialización (SV) es un bloque de bits que es utilizado por varios modos de operación para hacer aleatorio el proceso de encriptación y por lo tanto generar distintos textos cifrados incluso cuando el mismo texto claro es encriptado varias veces, sin la necesidad de regenerar la clave, ya que es un proceso lento.

El vector de inicialización tiene requerimientos de seguridad diferentes a los de la clave, por lo que el IV no necesita mantenerse secreto. Sin embargo, en la mayoría de los casos, es importante que el vector de inicialización no sea reutilizado con la misma clave. En los modos CBC y CFB, volver a usar el IV permite conocer la información contenida en el primer bloque del texto claro, y también prefijos comunes compartidos por dos mensajes. Para los modos OFB y CTR, la reutilización del vector de inicialización pone en riesgo la seguridad, dado que ambos crean un flujo de bits al que se le aplica una función XOR con el texto claro, que es totalmente dependiente del IV y de la clave ocupada. Reutilizar el flujo de bits también expone la seguridad. En el modo CBC, el vector de inicialización además debe ser impredecible al momento de realizar la encriptación; particularmente, una práctica muy común de encriptación ocupaba el último bloque de texto cifrado de un mensaje como vector de inicialización para el cifrado del próximo mensaje (este método fue usado por el protocolo SSL 2.0). Si un atacante logra conocer el IV (o el bloque de texto cifrado previo) antes de obtener el próximo texto claro, puede confirmar sus suposiciones sobre algún texto simple o bloque que fue encriptado anteriormente con la misma clave (técnica conocida como TLS CBC IV attack ).

 Rellenado
El cifrador en bloque opera con bloques de tamaño fijo, pero las dimensiones de los mensajes son variables. Por ello, en algunos modos de operación como ECB y CBC el último bloque de texto debe ser rellenado antes del proceso de encriptación. Hay muchos esquemas que para realizar esto. El más simple consiste en agregar *null bytes* al texto claro hasta que la longitud sea múltiplo del tamaño del bloque definido. Pero debe ser posible recuperar la longitud original del texto. Algo más complejo presenta el método DES que añade un bit en estado 1 seguido de *null bytes* para completar el tamaño de bloque. Otras técnicas más sofisticadas son los esquemas CBC-specific como *ciphertext stealing* o *Residual block termination*, que no genera texto cifrado adicional, a expensas de cierta complejidad adicional en sus procesos. Scheineier y Ferguson sugieren dos posibilidades para realizar el rellenado, ambas simples: anexar un byte con valor 128 (hex 80) seguido por tantos ceros como sean necesarios para completar el último bloque, o rellenar el último bloque con *n* bytes, todos con valor *n*.

Modos como CFB, OFB y CTR no requieren métodos para manejar los mensajes que no tienen longitudes que sea múltiplos del tamaño de bloque, dado que los modos de operación trabajan realizando una operación XOR entre el texto plano con la salida creada por el cifrador por bloques. Con el último segmento de texto llano se realiza una operación XOR con los primeros bytes obtenidos del cifrador, por lo que el texto cifrado resultante es del mismo tamaño del último texto plano. Esta característica de los cifrados en flujo los hace más adecuados para aplicaciones que transmiten datos en *streaming* donde no es conveniente aplicar relleno de bytes.

 Modos de operación más comunes
 Modo ECB (Electronic codebook)

El método más simple de modo de cifrado es el llamado **ECB** (*electronic codebook*), en el cual el mensaje es dividido en bloques, cada uno de los cuales es cifrado de manera separada. La desventaja de este método es que bloques idénticos de mensaje sin cifrar producirán idénticos textos cifrados. Por esto, no proporciona una auténtica confidencialidad y no es recomendado para protocolos criptográficos. Como apunte, no usa el vector de inicialización (IV).

Un claro ejemplo de cómo el método ECB puede revelar patrones del texto. Una versión de mapa de bits de la imagen de la izquierda ha sido cifrada con ECB para crear la imagen del centro:

La imagen de la derecha es cómo podría aparecer la misma imagen cifrada con CBC, CTR o cualquiera de los otros métodos seguros, esto es, indistinguible de ruido aleatorio. Hay que notar que la apariencia aleatoria de la imagen de la derecha dice muy poco sobre si la imagen ha sido cifrada de manera segura. Muchos métodos no seguros de cifrado producen, *a priori*, un resultado aparentemente aleatorio.

El modo ECB puede hacer que protocolos sin protección de integridad sean aún más susceptibles a ataques de repetición, dado que cada bloque es descifrado de la misma manera. Por ejemplo, el videojuego en línea *Phantasy Star Online: Blue Burst* usa Blowfish en modo ECB. Antes de que el método de intercambio de claves fuese craqueado, algunos jugadores enviaban repetidamente el bloque cifrado de *Monstruo matado*, cifrado cada uno con Blowfish, para ganar ilegítimamente puntos de experiencia.

 Modo CBC (Cipher-block chaining)

En el **modo CBC** (*cipher-block chaining*), antes de ser cifrado, a cada bloque de texto se le aplica una operación XOR con el bloque previo ya cifrado. De este modo, cada bloque cifrado depende de todos los bloques de texto claros usados hasta ese punto. Además, para hacer cada mensaje único se debe usar un vector de inicialización en el primer bloque.

Si el primer bloque tiene índice 1, la fórmula matemática para el cifrado CBC es:

mientras que la fórmula del descifrado es:

CBC es el modo usado más a menudo. Su principal contrapartida es que es secuencial y no puede funcionar en paralelo.

 Modo PCBC (Propagating cipher-block chaining)

El modo propagating cipher-block chaining fue diseñado para que pequeños cambios en el texto cifrado se propagasen más que en el modo CBC.

Las rutinas de cifrado y descifrado se definen como sigue:

PCBC es usado por Kerberos y Waste. Además de en éstos protocolos, su uso es bastante infrecuente.

 Modo OFB (Output feedback)
El modo **OFB** (*output feedback*) emplea una clave para crear un bloque pseudoaleatorio que es operado a través de XOR con el texto claro para generar el texto cifrado. Requiere de un vector de inicialización que debe ser único para cada ejecución realizada.

Las rutinas de cifrado y descifrado se definen como sigue:

Todos los bloques de salida obtenidos en cada operación dependen directamente de todos los anteriores, por lo tanto este modo de encriptación no es paralelizable.

Sin embargo, ya que el texto claro o el texto cifrado sólo son usados en el XOR final, las operaciones del cifrador por bloques pueden realizarse por adelantado, para que la etapa final se lleve a cabo en paralelo siempre que el texto claro o cifrado se encuentre disponible.

El modo de operación OFB requiere un IV distinto para cada mensaje encriptado con una misma clave. Si no se cumple este requerimiento se compromete la seguridad.

 Referencias
 NIST Computer Security Division's (CSD) Security Technology Group (STG) (2013). "Block cipher modes". Cryptographic Toolkit. NIST. Retrieved April 12, 2013.
 B. Moeller (May 20, 2004), *Security of CBC Ciphersuites in SSL/TLS: Problems and Countermeasures *
 NIST: Recommendation for Block Cipher Modes of Operation
