---
type: Artículo de enciclopedia
title: SHA-2
description: "SHA-2 es un conjunto de funciones hash criptográficas (SHA-224, SHA-256, SHA-384, SHA-512) desarrolladas por la Agencia de Seguridad Nacional (NSA) y publicada en 2001 por el Instituto Nacional de Estándares y …"
resource: https://es.wikipedia.org/wiki/SHA-2
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/SHA-2"}
license: CC BY-SA 4.0
id: eswiki-SHA-2
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# SHA-2

***SHA-2*** es un conjunto de funciones hash criptográficas (**SHA-224, SHA-256, SHA-384, SHA-512**) desarrolladas por la Agencia de Seguridad Nacional (NSA) y publicada en 2001 por el Instituto Nacional de Estándares y Tecnología (NIST) como un  Estándar Federal de Procesamiento de la Información (FIPS).

Una función hash es un algoritmo que transforma ("digiere") un conjunto arbitrario de elementos de datos, como puede ser un fichero de texto, en un único valor de longitud fija (el "hash"). El valor hash calculado puede ser utilizado para la verificación de la integridad de copias de un dato original sin la necesidad de proveer el dato original. Esta irreversibilidad significa que un valor hash puede ser libremente distribuido o almacenado, ya que sólo se utiliza para fines de comparación.
SHA significa algoritmo de hash seguro. SHA-2 incluye un significante número de cambios respecto a su predecesor, SHA-1; y consiste en un conjunto de cuatro funciones hash de 224, 256, 384 o 512 bits.

La seguridad proporcionada por un algoritmo hash es sumamente dependiente de su capacidad de producir un único valor para un conjunto de datos dados. Cuando una función hash produce el mismo valor para dos conjuntos de datos distintos, entonces se dice que se ha producido una colisión. Una colisión aumenta la posibilidad de que un atacante pueda elaborar computacionalmente conjuntos de datos que proporcionen acceso a información segura o para alterar ficheros de datos informáticos de tal forma que no cambiara el valor hash resultante y así eludir la detección.
Una función hash fuerte es aquella que es resistente a este tipo de ataques computacionales mientras que una función hash débil es aquella donde existe una creencia casi certera de que se pueden producir colisiones. Finalmente, una función hash quebrantada es aquella sobre la que se conoce métodos computacionales para producir colisiones.

En 2005, se identificaron fallas de seguridad en el SHA-1, permitiendo que existiera una debilidad matemática y evidenciando así la necesidad de elaborar una función hash más fuerte. Aunque el SHA-2 se comporta de forma parecida al algoritmo SHA-1, estos ataques no han sido extendidos satisfactoriamente a SHA-2.

La competición de funciones hash de la NIST seleccionó una nueva función hash, el SHA-3, en 2012. A diferencia de SHA-2 con SHA-1, el algoritmo SHA-3 no es derivación del SHA-2.

 Función hash

Con la publicación del FIPS PUB 180-2, NIST añadió tres nuevas funciones hash en la familia de SHA. Los algoritmos eran comúnmente conocidos como SHA-2, especificados posteriormente por su longitud (en bits): SHA-256, SHA-384, y SHA-512.

Los algoritmos fueron previamente publicados en 2001 en el borrador FIPS PUB 180-2, momento en el cual se aceptaban revisiones públicas y comentarios. En agosto de 2002, FIPS PUB 180-2 se convirtió en el nuevo estándar de hash seguro, reemplazando el FIPS PUB 180-1, el cual fue publicado en abril de 1995. La actualización del estándar incluyó el algoritmo original SHA-1, con la notación técnica consistente con la que describía el funcionamiento interno de la familia SHA-2.

En febrero de 2004, se publicó una noticia de modificación para FIPS PUB 180-2, especificando una variante adicional (SHA-224) para que coincidiera la longitud de la clave con la de Triple DES.
En octubre de 2008, el estándar fue actualizado en el FIPS PUB 180-3, incluyendo el SHA-224 de la notificación de modificación pero sin modificar fundamentalmente el estándar. La primera motivación de la actualización del estándar fue redistribuir la información de seguridad de los algoritmos de hash y recomendaciones para su uso en la "Special Publications" 800-107 y 800-57. Datos de prueba detallados y ejemplos de mensajes "resumidos" fueron también eliminados del estándar y fueron proporcionados como documentos separados.

En marzo de 2012, el estándar fue actualizado a FIPS PUB 180-4, añadiendo las funciones hash SHA-512/224 y SHA-512/256, y describiendo un método para la generación inicial de valores mediante versiones truncadas del SHA-512. Adicionalmente, una restricción previa del relleno de los datos de entrada para el cálculo del hash fue eliminada, permitiendo que los datos hash fueran calculados simultáneamente con la generación del contenido, tal como una retransmisión en tiempo real de un vídeo o audio. El relleno final del bloque de datos debe seguir ocurriendo antes de la salida del hash.

La SHA-256 y SHA-512 son nuevas funciones hash con 8 palabras de tamaño 32 y 64 bits, respectivamente. Usan diferentes desplazamientos y constantes, pero su estructura son por otra parte virtualmente idéntica, diferenciándose únicamente por el número de iteraciones. SHA-224 y SHA-384 son simples versiones de truncado de las dos anteriores funciones y estas son calculadas con diferentes valores iniciales. SHA-512/224 y SHA-512/256 son también versiones truncadas de SHA-512, pero los valores iniciales son generados usando un método descrito en el FIPS PUB 180-4. La familia de algoritmos SHA-2 están patentados en los Estados Unidos de América (patente con identificación 6829355) y fueron liberados bajo una licencia libre de derechos de autor.

A finales de 2013, los mejores ataques públicos consiguieron romper las 46 de las 64 iteraciones del SHA-256 y 46 de las 80 iteraciones del SHA-512. Información más detallada en  la sección "Criptoanálisis y validación" siguiente.

 Comparación de funciones SHA
En la tabla de abajo, *estado interno* significa "suma hash interna" después de cada compresión de un bloque de datos.

Los datos de rendimientos descritos anteriormente fueron realizados con una implementación de un único hilo (hebra) de un AMD Opteron 8354 a 2.2 GHz bajo un Linux x64, y sólo sirven para una ruda comparación general. Para un mayor detalle de las mediciones de rendimiento en arquitecturas de procesadores modernos se facilita la siguiente tabla.

Los resultados de rendimiento etiquetados como 'x86' fueron obtenidos usando un código de 32 bits en procesadores de 64 bits, mientras que los etiquetados como 'x86-64' son códigos de 64 bits. Mientras que SHA-256 está diseñado para operaciones de 32 bits, se beneficia computacionalmente del código optimizado para procesadores de 64 bits. Las implementaciones de 32 bits para SHA-512 son significativamente más lentas que sus equivalente en 64 bits. Las variaciones de ambos algoritmos con diferente tamaños de salida tienen un rendimiento similar, ya que las funciones de expansión y compresión del mensaje son idénticas, y únicamente varia los valores iniciales y los tamaños de salida. Las mejores implementaciones del MD5 y SHA-1 consiguen un rendimiento entre 4,5 y 6 ciclos por byte en procesadores modernos.

Los ensayos fueron llevado a cabo por la Universidad de Illinois en Chicago en su sistema hydra8 ejecutado en un Intel Xeon E3-1275 V2 a una frecuencia de reloj de 3,5 GHz, y en su sistema hydra9 ejecutada en un AMD A10-5800K con una frecuencia de 3,8 GHz. Las velocidades referenciadas como ciclos por bytes son la mediana del rendimiento de un algoritmo tratando con un mensaje de 4096 bytes usando el software de "benchmarking" criptográfico SUPERCOP. El rendimiento MiB/s se extrapolan de la velocidad del reloj de una CPU de un solo núcleo, rendimiento que varía en el mundo real debido a numerosos factores.

 Aplicaciones
Las funciones hash SHA-2 están implementadas en una gran variedad de aplicaciones y protocolos de seguridad, como por ejemplo: TLS y SSL, PGP, SSH, S/MIME, Bitcoin, PPCoin y IPsec.

La moneda criptográfica Bitcoin depende en gran medida en un doble uso del SHA-256. El SHA-256 es usado para identificar los paquetes software de Debian GNU/Linux y en el estándar de mensaje firmado DKIM; SHA-512 es parte del sistema para identificar los vídeos guardados en el Tribunal Penal Internacional para Ruanda. SHA-256 y SHA-512 fueron propuestos para ser usados en DNSSEC. Los proveedores de Unix y Linux están adoptando SHA-2 de 256 y 512 bits para aplicarlo en las contraseñas de seguridad.

SHA-1 y SHA-2 son algoritmos hash de seguridad requeridos por ley en ciertas aplicaciones del  gobierno de Estados Unidos, junto con el uso de otros algoritmos y protocolos criptográficos, para la protección de información clasificada y sensible. FIPS PUB 180-1 también alentó la adopción y uso del SHA-1 por parte de organizaciones privadas y comerciales. El gobierno está dejando de utilizar SHA-1, tal como expone el U.S. National Institute of Standards and Technology, "Las agencias federales ***deberían*** dejar de usar el SHA-1 para... aplicaciones que necesiten resistencia de colisión tan pronto como sea posible, y deberán usar familias de funciones hash SHA-2 para estas aplicaciones después de 2010" (énfasis en el original).
La directiva de NIST de que las agencias del gobierno estadounidense deban dejar de usar el SHA-1 después de 2010 y la finalización del SHA-3 deberían acelerar la migración del SHA-1.

Las funciones SHA-2 no son tan ampliamente usadas como SHA-1, a pesar de su mejora en seguridad. Las razones pueden incluir una falta de soporte del SHA-2 en sistemas que ejecutan Windows XP SP2 o anteriores, o por una falta de urgencia percibida mientras no se haya descubierto aún colisiones en el SHA-1.

 Criptoanálisis y validación
Para una función en la cual *L* es el número de bits del mensaje tratado, encontrar un mensaje que corresponde con el mensaje tratado siempre se puede conseguir empleando una búsqueda de fuerza bruta con 2*L* evaluaciones. A esto se le denomina ataque preimagen y puede ser práctico o no dependiendo del valor de *L* y del entorno de computación empleado. El segundo criterio, encontrar dos mensajes diferentes que producen el mismo mensaje tratado, se le conoce como colisión, requiere únicamente una media de 2*L*/2 evaluaciones si se emplea un ataque de cumpleaños.

A efectos prácticos, existe una gran preocupación ante este nuevo tipo de ataques ya que podrían permitir el uso de otros más eficientes. Aunque no se hayan visto casos de este tipo, existe una creciente creencia en emplear nuevos algoritmos hash más fuertes. Algunas aplicaciones que emplean sistemas criptográficos hash, por ejemplo para almacenar contraseñas, son mínimamente afectados por un ataque de colisión. Generar una contraseña que funcione para una cuenta dada requiere un ataque de preimagen, además de acceder al hash de la contraseña original (normalmente en un fichero shadow) el cual puede ser o no trivial. Recuperar una contraseña encriptada (p.e, obtener la contraseña para ser usada en otras cuentras del usuario) es imposible mediante ataques. (Sin embargo, incluso empleando un sistema hash seguro no puede impedir ataques de fuerza bruta en contraseñas débiles (p.e, 1234)).

En el caso de documentos firmados, un atacante no puede simplemente falsificar una firma a partir de un documento existente, el atacante debería generar dos pares de documentos, uno inocuo y otro dañado, y obtener la clave privada del titular para firmar el inocuo documento. Hay situaciones concretas en las que es posible; hasta finales de 2008, fue posible crear un certificado falsificado de
SSL empleando una colisión de MD5

Existen dos ataques de preimagen  por encuentro a medio camino contra SHA-2 con los que se reduce el número de iteraciones. El primero de ellos, respecto SHA-256, se resuelve en 41 rondas con respecto a 64 rondas con una complejidad temporal de 2253.5 y una complejidad espacial de 216; respecto SHA-512, se resuelve en 46 rondas con respecto a 80 rondas con una complejidad temporal de 2502 y una complejidad espacial de 222.

 Validación oficial

Las implementaciones de todas las funciones de seguridad aprobadas por FIPS son oficialmente validadas mediante un programa CMVP y necesariamente ejecutadas por la Instituto Nacional de Estándares y Tecnología (NIST) y la Communications Security Establishment (CSE). Para una verificación informal, fue dispuesto en la página web del NIST un paquete para generar un alto número de vectores de prueba; sin embargo, los resultados de verificación no pueden reemplazar de ninguna forma a la validación formal de CMVP, el cual es requerido por ley para ciertas aplicaciones.

 Ejemplos de variantes del SHA-2

Valores hash para una cadena de caracteres vacía.
 SHA224("")
 0x d14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f
 SHA256("")
 0x e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
 SHA384("")
 0x 38b060a751ac96384cd9327eb1b1e36a21fdb71114be07434c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b
 SHA512("")
 0x cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e
 SHA512/224("")
 0x 6ed0dd02806fa89e25de060c19d3ac86cabb87d6a0ddd05c333b84f4
 SHA512/256("")
 0x c672b8d1ef56ed28ab87c3622c5114069bdd3ad7b8f9737498d0c01ecef0967a

Incluso un pequeño cambio en el mensaje (con una apabullante probabilidad) dará como resultado un hash completamente distinto, debido al  efecto avalancha. Por ejemplo, añadiendo un punto al final de la frase:
 SHA224("The quick brown fox jumps over the lazy dog")
 0x 730e109bd7a8a32b1cb9d9a09aa2325d2430587ddbc0c38bad911525
 SHA224("The quick brown fox jumps over the lazy dog.")
 0x 619cba8e8e05826e9b8c519c0a5c68f4fb653e8a3d8aa04bb2c8cd4c

 SHA256("The quick brown fox jumps over the lazy dog")
 0x d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592
 SHA256("The quick brown fox jumps over the lazy dog.")
 0x ef537f25c895bfa782526529a9b63d97aa631564d5d789c2b765448c8635fb6c

 SHA384("The quick brown fox jumps over the lazy dog")
 0x ca737f1014a48f4c0b6dd43cb177b0afd9e5169367544c494011e3317dbf9a509cb1e5dc1e85a941bbee3d7f2afbc9b1
 SHA384("The quick brown fox jumps over the lazy dog.")
 0x ed892481d8272ca6df370bf706e4d7bc1b5739fa2177aae6c50e946678718fc67a7af2819a021c2fc34e91bdb63409d7

 SHA512("The quick brown fox jumps over the lazy dog")
 0x 07e547d9586f6a73f73fbac0435ed76951218fb7d0c8d788a309d785436bbb642e93a252a954f23912547d1e8a3b5ed6e1bfd7097821233fa0538f3db854fee6
 SHA512("The quick brown fox jumps over the lazy dog.")
 0x 91ea1245f20d46ae9a037a989f54f1f790f0a47607eeb8a14d12890cea77a1bbc6c7ed9cf205e67b7f2b8fd4c7dfd3a7a8617e45f3c463d481c7e586c39ac1ed

 SHA512/224("The quick brown fox jumps over the lazy dog")
 0x 944cd2847fb54558d4775db0485a50003111c8e5daa63fe722c6aa37
 SHA512/224("The quick brown fox jumps over the lazy dog.")
 0x 6d6a9279495ec4061769752e7ff9c68b6b0b3c5a281b7917ce0572de

 SHA512/256("The quick brown fox jumps over the lazy dog")
 0x dd9d67b371519c339ed8dbd25af90e976a1eeefd4ad3d889005e532fc5bef04d
 SHA512/256("The quick brown fox jumps over the lazy dog.")
 0x 1546741840f8a492b959d9b8b2344b9b0eb51b004bba35c0aebaac86d45264c3

 Pseudocódigo
A continuación un pseudocódigo para un algoritmo SHA-256. Nótese el gran incremento a la hora de mezclar los bits de la palabra w[16..63] comparada con SHA-1.

 *Nota 1: Todas las variables son enteros sin signo de 32 bits y se emplea módulo 232 para su cálculo*
 *Nota 2: Para cada ronda, existe una constante específica k[i] y una entrada en el array del mensaje w[i], 0 = i = 63*
 ''Nota 3: La función de compresión emplea 8 variables de trabajo
 *Nota 4: La convención de Big-endian es usada cuando se expresan las constantes en este pseudocódigo,*
     *y cuando se parsea el bloque de datos del mensaje de bytes a palabras, por ejemplo,*
     *la primera palabra del mensaje de entrada "abc" tras su concatenación es 0x61626380*

 *Inicialización de los valores hash:*
 (primeros 32 bits de la parte decimal de las raíces cuadradas de los primeros números primos del intervalo [2,19]:
 h0 := 0x6a09e667
 h1 := 0xbb67ae85
 h2 := 0x3c6ef372
 h3 := 0xa54ff53a
 h4 := 0x510e527f
 h5 := 0x9b05688c
 h6 := 0x1f83d9ab
 h7 := 0x5be0cd19

 *Inicialización del array con las constantes de las rondas:*
 (primeros 32 bits de la *parte decimal* de las raíces cúbicas de los 64 primeros números primos del intervalo [2,311]):
 k[0..63] :=
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2

 *Preprocesamiento:*
 append the bit '1' to the message
 append k bits '0', where k is the minimum number >= 0 such that the resulting message
     length (módulo 512 in *bits*) is 448.
 append length of message (before pre-processing), in *bits*, as 64-bit big-endian integer

 *Procesamiento del mensaje en sucesivos trozos de 512 bits:*
 break message into 512-bit chunks
 **for** each chunk
     create a 64-entry message schedule array w[0..63] of 32-bit words
     *(Los valores iniciales de w[0..63] no importan, en muchas implementaciones usan el valor 0)*
     copy chunk into first 16 words w[0..15] of the message schedule array

     *Expansión de las primeras 16 palabras hasta completar las 48 palabras w[16..63] del array del mensaje:*
     **for** i **from** 16 to 63
         s0 := (w[i-15] **rightrotate** 7) **xor** (w[i-15] **rightrotate** 18) **xor** (w[i-15] **rightshift** 3)
         s1 := (w[i-2] **rightrotate** 17) **xor** (w[i-2] **rightrotate** 19) **xor** (w[i-2] **rightshift** 10)
         w[i] := w[i-16] **+** s0 **+** w[i-7] **+** s1

     *Inicialización de las variables de trabajo con los valores hash actuales:*
     a := h0
     b := h1
     c := h2
     d := h3
     e := h4
     f := h5
     g := h6
     h := h7

     *Bucle principal de la función de compresión:*
     **for** i **from** 0 to 63
         S1 := (e **rightrotate** 6) **xor** (e **rightrotate** 11) **xor** (e **rightrotate** 25)
         ch := (e **and** f) **xor** ((**not** e) **and** g)
         temp1 := h **+** S1 **+** ch **+** k[i] **+** w[i]
         S0 := (a **rightrotate** 2) **xor** (a **rightrotate** 13) **xor** (a **rightrotate** 22)
         maj := (a **and** b) **xor** (a **and** c) **xor** (b **and** c)
         temp2 := S0 **+** maj

         h := g
         g := f
         f := e
         e := d **+** temp1
         d := c
         c := b
         b := a
         a := temp1 **+** temp2

     *Inserción del trozo comprimido al valor hash actual:*
     h0 := h0 **+** a
     h1 := h1 **+** b
     h2 := h2 **+** c
     h3 := h3 **+** d
     h4 := h4 **+** e
     h5 := h5 **+** f
     h6 := h6 **+** g
     h7 := h7 **+** h

 *Producción del valor final del hash (en formato big-endian):*
 digest := hash := h0 **append** h1 **append** h2 **append** h3 **append** h4 **append** h5 **append** h6 **append** h7

La computación de los valores ch y maj puede ser optimizada de la misma forma tal como está descrita para SHA-1.

SHA-224 es idéntico que SHA-256, excepto por:
 los valores iniciales de hash desde h0 hasta h7 son diferentes, y
 la salida está construida por la omisión de h7.

 Valores hash iniciales para el SHA-224 (en big endian):
 (Los segundos 32 bits de la parte decimal de la raíces cuadradas del noveno al decimosexto número primo del intervalo [23,53]
 h[0..7] :=
     0xc1059ed8, 0x367cd507, 0x3070dd17, 0xf70e5939, 0xffc00b31, 0x68581511, 0x64f98fa7, 0xbefa4fa4

SHA-512 estructuralmente es idéntico al SHA-256, pero:
 el mensaje es partido en trozos de 1024 bits,
 los valores iniciales del hash y las constantes de las iteraciones son extendidas a 64 bits,
 hay 80 iteraciones en vez de 64,
 las constantes de cada iteración están basadas en los primeros 80 primos del intervalo [2,409],
 el tamaño de palabra usado para los cálculos tiene una longitud de 64 bits,
 la longitud adjunta del mensaje (antes del preprocesado), en *bits*, es de un entero big-endian de 128 bits, y
 los desplazamientos y rotaciones usadas son distintas.

 Valores hash iniciales para el SHA-512 (en big-endian):

 h[0..7] := 0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
            0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179

 Constantes de cada ronda del SHA-512:

 k[0..79] := [ 0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 0x3956c25bf348b538,
               0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118, 0xd807aa98a3030242, 0x12835b0145706fbe,
               0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2, 0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235,
               0xc19bf174cf692694, 0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65,
               0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5, 0x983e5152ee66dfab,
               0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4, 0xc6e00bf33da88fc2, 0xd5a79147930aa725,
               0x06ca6351e003826f, 0x142929670a0e6e70, 0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed,
               0x53380d139d95b3df, 0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
               0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30, 0xd192e819d6ef5218,
               0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8, 0x19a4c116b8d2d0c8, 0x1e376c085141ab53,
               0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8, 0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373,
               0x682e6ff3d6b2b8a3, 0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec,
               0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b, 0xca273eceea26619c,
               0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178, 0x06f067aa72176fba, 0x0a637dc5a2c898a6,
               0x113f9804bef90dae, 0x1b710b35131c471b, 0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc,
               0x431d67c49c100d4c, 0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817]

SHA-384 es idéntico a SHA-512, exceptuando que:
 los valores iniciales del hash desde h0 hasta h7 son diferentes (son tomados desde el noveno hasta el decimosexto primo), y
 la salida es construida omitiendo h6 y h7.
 Valores hash iniciales para SHA-384 (en big-endian):

 h[0..7] := 0xcbbb9d5dc1059ed8, 0x629a292a367cd507, 0x9159015a3070dd17, 0x152fecd8f70e5939,
            0x67332667ffc00b31, 0x8eb44a8768581511, 0xdb0c2e0d64f98fa7, 0x47b5481dbefa4fa4

SHA-512/t es idéntico a SHA-512 excepto por:
 los valores iniciales del hash desde h0 hasta h7 son dados por la *función de generación IV de SHA-512/t*,
 las salida es construida mediante truncamiento de la concatenación desde h0 hasta h7 en el *t* bit,
 no está permitido que *t* sea igual a 384, en su lugar SHA-384 deberá ser usado como está especificado, y
 los valores 224 y 256 para *t* están especialmente mencionados como aprobados.

 Implementaciones
 Implementaciones en lenguajes comunes

Las funciones hash SHA se pueden encontrar en muchos de los lenguajes de programación modernos, como por ejemplo C, C++, C#, Go, Javascript, Java, Python, PHP, Perl, y Ruby.

 Otras implementaciones

Bouncy Castle La biblioteca Bouncy Castle es una biblioteca gratuita escrita en Java y en C# que contiene implementaciones de los algoritmos SHA-1, SHA-224, SHA-256, SHA-384 y SHA-512, así como de otros algoritmos como Whirlpool, Tiger, RIPEMD, GOST-3411, MD2, MD4 y MD5.
cryptlib Biblioteca con herramientas de seguridad software, siendo esta multiplataforma y de código abierto.
Crypto++ Biblioteca en C++ con esquemas criptográficos e implementaciones de los algoritmos SHA-1, SHA-224, SHA-256, SHA-384 y SHA-512. Es de código abierto y con una licencia muy permisiva.
jsSHA Biblioteca escrita en JavaScript para realizar cálculos del tratamiento del SHA en la parte del cliente. Se puede utilizar en varios navegadores webs. jsSHA trabaja con la hipótesis de que JavaScript no es nativamente soportado para realizar operaciones de 64 bits tal como son requeridas en SHA-384 y SHA-512.
libsparkcrypto Implementación formalmente verificada que es usada ampliamente en algoritmos simétricos criptográficos en el lenguaje de programación y herramientas del SPARK. Completa la falta de errores en tiempo de ejecución como violaciones de rango, divisiones por cero y desbordamiento numérico.
LibTomCrypt Conjunto de herramientas portables de criptografía para ISO C. Todas ellas de dominio público.
Libgcrypt Biblioteca de propósito general para la criptografía basada en código de GNU Privacy Guard.
md5deep Conjunto de programas para realizar un tratamiento en mensajes empleando MD5, SHA-1, SHA-256, Tiger, o Whirlpool con un número de arbitrario de ficheros. Suele ser empleada en seguridad informática, administración de sistemas y comunidades de computación forense para ejecutar gran número de ficheros a través de diversos algoritmos criptográficos. Es similar al sha1sum de GNU Core Utilities y al md5sum.
OpenSSL La ampliamente usada biblioteca OpenSSL crypto incluye implementaciones de los algoritmos de SHA-1, SHA-224, SHA-256, SHA-384 y SHA-512. Todas ellas son libres y de código abierto.
PolarSSL La pequeña biblioteca PolarSSL crypto y SSL incluye implementaciones de código abierto de los algoritmos de SHA-1, SHA-224, SHA-256, SHA-384 y SHA-512.
sphlib Bliblioteca libre y de código abierto que implementa varias funciones hash, incluyendo SHA-1 y SHA-2, ambas portables (pero optimizadas) a C y a Java.
VHDL Colección de implementaciones hardware de funciones hash (incluyendo SHA-1 y SHA-2) portable (pero optimizada) a VHDL. Es libre y de código abierto.

 Véase también

 Funciones Hash
 Sellado de tiempo
 Hash basado en Message Authentication Code (HMAC) o Keyed Hash
 Criptografía financiera
 Comandos de terminal sha1sum (sha224sum, sha256sum, sha384sum y sha512sum)

 Notas
 Henri Gilbert, Helena Handschuh: Security Analysis of SHA-256 and Sisters. Selected Areas in Cryptography 2003: pp. 175-193

 Referencias

 Enlaces externos

 Descripciones del SHA-256, SHA-384 y SHA-512 from NIST
 CSRC Herramienta criptográfica, en el sitio oficial del NIST para el estándar de Hash seguro
 FIPS 180-4: Secure Hash Standard (SHS) (PDF, 1.7 MB), versión actual del estándar de hash seguro (SHA-1, SHA-224, SHA-256, SHA-384 y SHA-512), marzo de 2012
 Pruebas vectoriales para SHA-256/384/512  del proyecto NESSIE
 Pruebas vectoriales para SHA-1, SHA-2 del sitio web de NIST
 NIST Cryptographic Hash Project Competición para elegir el algoritmo para SHA-3
 RFC 3874: Funciones Hash unidireccionales de 224 bits: SHA-224.
 RFC 6234: Algoritmos SHA, HMAC y HKDF (ambos últimos basados en SHA). Contiene ejemplos de implementación en lenguaje C.
