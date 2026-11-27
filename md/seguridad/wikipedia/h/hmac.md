---
type: Artículo de enciclopedia
title: HMAC
description: "En la criptografía, un HMAC (a veces expandido como código de autentificación de mensajes en clave-hash o código de autenticación de mensaje basado en hash) es una construcción específica para calcular un código de …"
resource: https://es.wikipedia.org/wiki/HMAC
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/HMAC"}
license: CC BY-SA 4.0
id: eswiki-HMAC
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# HMAC

En la criptografía, un **HMAC** (a veces expandido como **código de autentificación de mensajes en clave-hash** o **código de autenticación de mensaje basado en hash**) es una construcción específica para calcular un código de autentificación de mensaje (MAC) que implica una  función hash criptográfica en combinación con una llave criptográfica secreta. Como cualquier MAC, puede ser utilizado para verificar simultáneamente la *integridad de los datos* y la  *autentificación* de un mensaje.  Cualquier función hash criptográfica, tales como SHA-2 o SHA-3, puede ser utilizada para el cálculo de un HMAC; el algoritmo MAC resultante se denomina HMAC-SHA2 o HMAC-SHA3 en consecuencia. La fuerza criptográfica del HMAC depende de la potencia criptográfica de la función de hash subyacente, el tamaño de su salida de hash y el tamaño y calidad de la llave.

Una función hash iterativa rompe un mensaje en bloques de un tamaño fijo e itera sobre ellos con una función de compresión. Por ejemplo, SHA-2 y SHA-3 operan en bloques de 512-bit. El tamaño de la salida de HMAC es el mismo que el de la función de hash subyacente (entre 224 y 512 bits en el caso de SHA3 dependiente de la configuración).

La definición y el análisis de la construcción HMAC se publicó por primera vez en 1996 por Mihir Bellare, Ran Canetti y Hugo Krawczyk, que también escribió el RFC 2104.  Asimismo, este documento define una variante llamada NMAC que rara vez, o nunca, se utiliza. FIPS PUB 198 generaliza y estandariza el uso de HMAC. HMAC-SHA1 y HMAC-MD5 se utilizan dentro de los protocolos IPsec y TLS pero **no** son seguros hoy día.

 Definición (de RFC 2104)

donde:
*H* es una función hash criptográfica,
*K* es una clave secreta rellena a la derecha con ceros adicionales al tamaño del bloque de entrada de la función hash, o el hash de la llave original si es más largo que el tamaño de bloque,
*m* es el mensaje a ser autenticado,
|| denota concatenación,
⊕ denota disyunción exclusiva (XOR),
*opad* es el relleno exterior (0x5c5c5c…5c5c, un bloque de largo hexadecimal constante),
*ipad* es el relleno interior (0x363636…3636, un bloque de largo hexadecimal constante).

 Implementación
El siguiente pseudocódigo muestra cómo se puede implementar HMAC.  El tamaño del bloque es de 64 (bytes) cuando se utiliza una de las siguientes funciones hash: SHA-1, MD5, RIPEMD-128/160.

 **function** hmac (key, message)
     **if** (length(key) > blocksize) **then**
         key = hash(key) *// llaves con más tamaño que el bloque se acortan al tamaño justo aplicando hash a esas llaves*
     **end if**
     **if** (length(key) < blocksize) **then**
         key = key ∥ [0x00 * (blocksize - length(key))] *// llaves más cortas que el tamaño del bloque se agrandan con ceros (donde *∥* es la concatenación)*
     **end if**

     o_key_pad = [0x5c * blocksize] ⊕ key *// Cuando el tamaño del bloque es el de la función de hash subyacente*
     i_key_pad = [0x36 * blocksize] ⊕ key *// Donde ⊕ es el o exclusivo (XOR)*

     **return** hash(o_key_pad ∥ hash(i_key_pad ∥ message)) *// Donde *∥* es la concatenación*
 **end function**

El siguiente es una implementación en Python de HMAC-MD5:

Python incluye un módulo hmac, por lo que la función anterior puede ser reemplazada por una versión más corta.

El siguiente código es una implementación en PHP de HMAC-SHA1:

PHP incluye una función HMAC, por lo que el ejemplo anterior puede ser reemplazado por una versión más corta.

La siguiente es una implementación usando QCryptographicHash de Qt

El siguiente es un ejemplo usando Node.js integrado en el módulo criptográfico utilizando HMAC-SHA1:

 Principios de diseño
El diseño de la especificación HMAC fue motivada por la existencia de ataques contra los mecanismos más triviales de la combinación de una llave con una función hash. Por ejemplo, se podría suponer la misma seguridad que HMAC proporciona podría lograrse con MAC = **H**(*llave* ∥ *mensaje*).   Sin embargo, este método adolece de un grave defecto: con la mayoría de las funciones hash, es fácil añadir datos al mensaje sin conocer la llave y obtener otra MAC válida ("ataque longitud de extensión").  La alternativa, añadiendo la clave utilizando MAC = **H**(*mensaje* ∥ *llave*), sufre del problema de que un atacante que puede encontrar una colisión en la función hash tiene una colisión en el MAC (como dos mensajes M1 y M2 obteniéndose el mismo hash proporcionará la misma condición de arranque de la función hash antes de obtener el hash de la llave adjunta, por lo tanto, el hash final será el mismo). Usar MAC = **H**(*llave* ∥ *mensaje* ∥ *llave*) es mejor, pero varios artículos de seguridad han sugerido vulnerabilidades con este enfoque, incluso cuando se utilizan dos claves diferentes.

No se conocen extensiones de ataques en contra de la actual especificación HMAC que se define como **H**(*llave* ∥ **H**(*llave* ∥ *mensaje*)) porque la aplicación externa de la función de hash marca el resultado intermedio del hash interno. Los valores de *ipad* y *opad* no son críticos para la seguridad del algoritmo, pero se define de tal manera que tengamos una gran distancia de Hamming entre sí y para que las llaves interior y exterior tengan menos bits en común. La reducción de la seguridad de HMAC no les obliga a ser diferentes en al menos un bit.

La función de hash Keccak, que fue seleccionada por el NIST como el ganador del concurso SHA-3,  no necesita este enfoque anidado y se puede utilizar para generar un MAC simplemente anteponiendo la clave del mensaje.

 Seguridad
La fuerza criptográfica del HMAC depende del tamaño de la clave secreta que se utiliza. El ataque más común contra HMAC es la fuerza bruta para descubrir la clave secreta. HMAC está mucho menos afectada por las colisiones que sus algoritmos de hash subyacentes solos. Por lo tanto, HMAC-MD5 no sufre de las mismas debilidades que se han encontrado en MD5.

En 2006, Jongsung Kim, Alex Biryukov, Bart Preneel y Seokhie Hong mostraron cómo distinguir HMAC con versiones reducidas de MD5 y SHA-1 o las versiones completas de HAVAL, MD4 y SHA-0 de una función aleatoria o HMAC con una función aleatoria. Diferentes distinciones  permiten a un atacante idear un ataque de falsificación de HMAC. Además, diferentes y distinguidores rectangulares pueden conducir a ataques de segunda-preimagen. HMAC con la versión completa de MD4 se falsificó ese conocimiento.  Estos ataques no contradicen la prueba de seguridad de HMAC, pero proporcionan información sobre HMAC basada en funciones hash criptográficas existentes.

En 2009, Xiaoyun Wang presentó un ataque de identificación en HMAC-MD5 sin utilizar claves relacionadas. Se puede distinguir una instancia de HMAC con MD5 de una instancia con una función aleatoria con 2^97 consultas con probabilidad 0.87.

En 2011 un informativo RFC 6151 se aprobó para actualizar las consideraciones de seguridad en MD5 y HMAC-MD5. Para HMAC-MD5 el RFC resume que -a pesar de la seguridad de la función hash MD5, ésta se ve gravemente comprometida- los actualmente conocidos *"ataques contra HMAC-MD5 no parecen indicar una vulnerabilidad práctica cuando se utiliza como código de autentificación de mensajes."*

En sistemas inadecuadamente-garantizados un ataque de tiempo se puede realizar para averiguar dígito a dígito de HMAC.

 Ejemplos de HMAC (MD5, SHA1, SHA256)
Aquí hay algunos valores vacíos de HMAC:
 HMAC_MD5("", "")    = 0x74e6f7298a9c2d168935f58c001bad88
 HMAC_SHA1("", "")   = 0xfbdb1d1b18aa6c08324b7d64b71fb76370690e1d
 HMAC_SHA256("", "") = 0xb613679a0814d9ec772f95d778c35fc5ff1697c493715653c6c712144292c5ad

Aquí hay algunos valores no vacíos HMAC, asumiendo 8-bit ASCII o UTF-8 codificación:
 HMAC_MD5("key", "The quick brown fox jumps over the lazy dog")    = 0x80070713463e7749b90c2dc24911e275
 HMAC_SHA1("key", "The quick brown fox jumps over the lazy dog")   = 0xde7c9b85b8b78aa6bc8a7a36f70a90701c9db4d9
 HMAC_SHA256("key", "The quick brown fox jumps over the lazy dog") = 0xf7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8

--

 Referencias

Notes

 Mihir Bellare, Ran Canetti and Hugo Krawczyk, Keying Hash Functions for Message Authentication, CRYPTO 1996, pp1–15 (PS or PDF) .
 Mihir Bellare, Ran Canetti and Hugo Krawczyk, Message authentication using hash functions: The HMAC construction, *CryptoBytes* 2(1), Spring 1996 (PS or PDF) .

Enlaces externos
 RFC2104
 Online HMAC Calculator for dozens of underlying hashing algorithms
 Online HMAC Generator / Tester Tool
 FIPS PUB 198-1, *The Keyed-Hash Message Authentication Code (HMAC)*
 PHP HMAC implementation
 Python HMAC implementation
 Perl HMAC implementation
 Ruby HMAC implementation
 C HMAC implementation
 C++ HMAC implementation (part of Crypto++)
 Placement Master / Tester Tool
 Shop Placement Papers
 Java implementation
 JavaScript MD5 and SHA HMAC implementation
 JavaScript SHA-only HMAC implementation
 .NET's System.Security.Cryptography.HMAC
 Delphi/Free Pascal implementation
 " Curl to http request converter
