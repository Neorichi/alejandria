---
type: Artículo de enciclopedia
title: Criptografía simétrica
description: "La criptografía simétrica, también conocida como criptografía de clave simétrica (en inglés symmetric key cryptography), criptografía de clave secreta (en inglés secret key cryptography) o criptografía de una clave (en …"
resource: https://es.wikipedia.org/wiki/Criptografía_simétrica
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_simétrica"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_simétrica
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía simétrica

La **criptografía simétrica**, también conocida como **criptografía de clave simétrica** (en inglés *symmetric key cryptography*), **criptografía de clave secreta** (en inglés *secret key cryptography*) o criptografía de una clave (en inglés *single-key cryptography*), es un método criptográfico en el cual se usa una única clave compartida para cifrar y descifrar mensajes entre el emisor y el receptor. Las dos partes que se comunican han de ponerse de acuerdo de antemano sobre la clave a usar. Una vez que ambas partes tienen acceso a esta clave, el remitente cifra un mensaje usando la clave, lo envía al destinatario, y este lo descifra con la misma clave.

Los algoritmos usados en la criptografía simétrica son principalmente operaciones booleanas y de transposición, y es más eficiente que la criptografía asimétrica.

 Seguridad

La seguridad de este sistema radica en mantener la clave en secreto.

Un buen sistema de **cifrado** pone toda la seguridad en la clave y ninguna en el algoritmo. En otras palabras, *no debería ser de ninguna ayuda para un atacante conocer el algoritmo que se está usando*. Sólo si el atacante obtuviera la clave, le serviría conocer el algoritmo. Los algoritmos de cifrado ampliamente utilizados tienen estas propiedades .. (por ejemplo: AES).

Dado que toda la seguridad está en la clave, es importante que sea muy difícil adivinar el tipo de clave. Esto quiere decir que el abanico de claves posibles, o sea, el espacio de posibilidades de claves, debe ser amplio. Richard Feynman fue famoso en Los Álamos por su habilidad para abrir cajas de seguridad; para alimentar la leyenda que había en torno a él, llevaba encima un juego de herramientas que incluían un estetoscopio. En realidad, utilizaba una gran variedad de trucos para reducir a un pequeño número la cantidad de combinaciones que debía probar, y a partir de ahí simplemente probaba hasta que adivinaba la combinación correcta. En otras palabras, reducía el tamaño de posibilidades de claves.

Actualmente, los ordenadores pueden descifrar claves con extrema rapidez, y ésta es la razón por la cual el tamaño de la clave es importante en los criptosistemas modernos. El algoritmo de cifrado DES usa una clave de 56 bits, lo que significa que hay 256 claves posibles (72.057.594.037.927.936 claves). Esto representa un número muy alto de claves, pero un ordenador genérico puede comprobar el conjunto posible de claves en cuestión de días. Una máquina especializada puede hacerlo en horas. Algoritmos de cifrado de diseño más reciente como 3DES, Blowfish e IDEA **usan claves de 128 bits**, lo que significa que existen 2128 claves posibles. Esto equivale a muchísimas más claves, y aun en el caso de que una gran cantidad  de máquinas estuvieran cooperando, tardarían bastante tiempo en encontrar la clave.

 Cifrados de clave simétrica en informática

 Cifrados de Bloque: cifran el mensaje dividiendo el flujo en bloques de k bits. Cada bloque se corresponde con otro diferente. Por ejemplo, un bloque con k=3 "010" se podría corresponder con "110". Se utilizan algoritmos como DES, TDES, RC5, RC6, CAST, Serpent, IDEA, Kasumi, Blowfish, Camellia y AES (Rijndael). Estos algoritmos trabajan con bloques de 64 o 128 bits.
 Cifrados de flujo: se utilizan en aplicaciones donde la velocidad del flujo de datos es variable o en tiempo real, como telefonía o WLAN. Se genera un "flujo de claves" a partir de una semilla aleatoria y se combina bit a bit con la información en claro. Algunos ejemplos son RC4, Trivium, SEAL, WAKE, VEST, SNOW y Rabbit.
 Cifrado simétrico de resumen (*hash functions*): se utilizan para garantizar la integridad de los datos. Algunos ejemplos son los algoritmos SHA o Whirlpool.

 Ejemplos

Como ejemplo de sistema simétrico está Enigma. Este fue un sistema empleado por Alemania durante la Segunda Guerra Mundial, en el que las claves se distribuían a diario en forma de libros de códigos. Cada día, un operador de radio, receptor o transmisor, consultaba su copia del libro de códigos para encontrar la clave del día. Todo el tráfico enviado por ondas de radio durante aquel día era cifrado y descifrado usando las claves del día.

Inglaterra usó máquinas para descifrar las claves durante aquella guerra y aunque el citado sistema alemán, Enigma, estaba provisto de un amplio abanico de claves, los ingleses diseñaron máquinas de cómputo especializado, los Bombes, para comprobar las claves de modo mecánico hasta que la clave del día era encontrada. Esto significaba que algunas veces encontraban la clave del día pocas horas después de que ésta fuera puesta en uso, pero también que otros días no podían encontrar la clave correcta. Los Bombes no fueron máquinas de cómputo general, sino las precursoras de los ordenadores (computadoras) actuales.

Algunos ejemplos de algoritmos simétricos son DES, 3DES, RC5, AES, Blowfish e IDEA.

 Inconvenientes

El principal problema con los sistemas de cifrado simétrico no está ligado a su seguridad, sino al intercambio y distribución segura de claves entre los participantes. Una vez que el remitente y el destinatario hayan intercambiado las claves pueden usarlas para comunicarse con seguridad, pero ¿qué canal de comunicación que sea seguro han usado para transmitirse las claves? Sería mucho más fácil para un atacante intentar interceptar una clave que probar las posibles combinaciones del espacio de claves.

Otro problema es el número de claves que se necesitan. Si tenemos un número *n* de personas que necesitan comunicarse entre sí, se necesitan en total *n*(*n*-1)/2 claves para todas las parejas de personas que tengan que comunicarse de modo privado. Esto puede funcionar con un grupo reducido de personas, pero sería imposible llevarlo a cabo con grupos más grandes.

Para solucionar estos problemas se podrían tener **centros de distribución de claves simétricas**. Esto podría funcionar por ejemplo para organizaciones militares. Aunque siempre habría un riesgo a posibles fugas de información de que claves son usadas en ciertas comunicaciones. Sin embargo su uso en el sector privado llevaría consigo inevitables fugas, atascos burocráticos y una constante amenaza de filtraciones.

 Alternativas
Para solucionar el problema de distribución de claves y los que de éste se derivan existen la criptografía asimétrica y la criptografía híbrida.

La criptografía asimétrica, también conocida como criptografía de clave pública, utiliza pares de claves compuestas por una clave pública y una clave privada. La clave pública se comparte ampliamente, mientras que la clave privada se mantiene en secreto. Esta técnica permite la autenticación y el intercambio seguro de información sin necesidad de compartir claves.

La criptografía híbrida combina tanto la criptografía simétrica como la criptografía asimétrica para aprovechar las ventajas de ambos sistemas.

 Referencias

 Enlaces externos
 Adaptado de la Guía de "Gnu Privacy Guard"
