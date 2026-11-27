---
type: Artículo de enciclopedia
title: SHA-1
description: "En criptografía, SHA-1 (Secure Hash Algorithm 1) es una función hash que toma una entrada y produce un valor hash de 160 bits (20 bytes) conocido como resumen de mensaje, que generalmente se representa como 40 dígitos …"
resource: https://es.wikipedia.org/wiki/SHA-1
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/SHA-1"}
license: CC BY-SA 4.0
id: eswiki-SHA-1
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# SHA-1

- **Nombre:** SHA-1
- **Diseñador:** Agencia de Seguridad Nacional
- **Publicación:** 1993 (SHA-0),1995 (SHA-1)
- **Series:** (SHA-0), SHA-1, SHA-2, SHA-3
- **Certificación:** FIPS PUB 180-4, CRYPTREC (Monitoreado)
- **Longitud clave:** 160 bits
- **Longitud bloque:** 512 bits
- **Estructura:** Construcción Merkle-Damgård
- **Rounds:** 80

En criptografía, **SHA-1** (***Secure Hash Algorithm 1***) es una función hash que toma una entrada y produce un valor hash de 160 bits (20 bytes) conocido como resumen de mensaje, que generalmente se representa como 40 dígitos hexadecimales. Fue diseñado por la Agencia de Seguridad Nacional de los Estados Unidos (NSA) y es un Estándares Federales de Procesamiento de Información de EE. UU. Aunque el algoritmo ha sido roto criptográficamente, sigue siendo ampliamente utilizado.

Desde 2005, SHA-1 no se considera seguro frente a adversarios con mayores recursos, y en 2010, muchas organizaciones recomendaron su sustitución. El Instituto Nacional de Estándares y Tecnología (NIST) desaconsejó formalmente el uso de SHA-1 en 2011 y prohibió su uso para firmas digitales en 2013, declarando que debería eliminarse completamente para 2030. A partir de 2020, los ataques de prefijo elegido contra SHA-1 son prácticos. Por lo tanto, se recomienda eliminar SHA-1 de los productos lo antes posible y, en su lugar, utilizar SHA-2 o SHA-3. La sustitución de SHA-1 es urgente donde se utilice para firmas digitales.

En 2017, los principales navegadores web dejaron de aceptar certificados SSL basados en SHA-1. En febrero de ese mismo año, el CWI de Ámsterdam y Google anunciaron que habían realizado un ataque de colisión contra SHA-1, publicando dos archivos PDF diferentes que generaban el mismo hash SHA-1. No obstante, SHA-1 sigue siendo seguro para HMAC.

Microsoft dejó de admitir la firma de código SHA-1 para Windows Update el 3 de agosto de 2020, lo que también finalizó efectivamente las actualizaciones para versiones de Windows que no se hayan actualizado a SHA-2, como Windows 2000 hasta Vista, así como versiones de Windows Server desde Windows 2000 Server hasta Server 2003.

 Desarrollo

SHA-1 produce un resumen de mensaje basado en principios similares a los usados por Ronald L. Rivest del MIT en el diseño de los algoritmos de resumen de mensajes MD2, MD4 y MD5, pero genera un valor hash mayor (160 bits frente a 128 bits).

SHA-1 fue desarrollado como parte del proyecto Capstone del Gobierno de EE. UU. La especificación original del algoritmo se publicó en 1993 bajo el título *Secure Hash Standard*, FIPS PUB 180, por la agencia de estándares del gobierno de EE. UU., NIST (Instituto Nacional de Estándares y Tecnología). Esta versión ahora suele llamarse *SHA-0*. Fue retirada por la NSA poco después de su publicación y fue reemplazada por la versión revisada, publicada en 1995 en FIPS PUB 180-1 y comúnmente denominada *SHA-1*. SHA-1 difiere de SHA-0 solo por una rotación de bits en la programación de mensajes de su función de compresión. Según la NSA, esto se hizo para corregir una falla en el algoritmo original que reducía su seguridad criptográfica, pero no proporcionaron más explicaciones. Las técnicas disponibles públicamente demostraron una vulnerabilidad de SHA-0 en 2004, antes de que se comprometiera SHA-1 en 2017.

 Aplicaciones

 Criptografía

SHA-1 forma parte de varias aplicaciones y protocolos de seguridad ampliamente utilizados, incluidos TLS y SSL, PGP, SSH, S/MIME e IPsec. Estas aplicaciones también pueden usar MD5; ambos, MD5 y SHA-1, descienden de MD4.

SHA-1 y SHA-2 son los algoritmos hash requeridos por ley para su uso en ciertas aplicaciones del gobierno de EE. UU., incluidos otros algoritmos y protocolos criptográficos, para la protección de información sensible no clasificada. FIPS PUB 180-1 también alentaba la adopción y uso de SHA-1 por organizaciones privadas y comerciales. SHA-1 está siendo retirado de la mayoría de los usos gubernamentales; el NIST declaró: "Las agencias federales deben dejar de usar SHA-1 para... aplicaciones que requieran resistencia a colisiones tan pronto como sea práctico, y deben usar la familia de funciones hash SHA-2 para estas aplicaciones después de 2010", aunque más tarde se relajó para permitir el uso de SHA-1 para verificar firmas digitales y sellos de tiempo antiguos.

Una de las principales motivaciones para la publicación del algoritmo de hash seguro fue el estándar de firma digital, en el que se incorpora.

Las funciones hash SHA se han utilizado como base para los cifrados por bloque SHACAL.

 Integridad de los datos
Los sistemas de control de revisiones como Git, Mercurial y Monotone utilizan SHA-1, no por motivos de seguridad, sino para identificar revisiones y asegurar que los datos no han cambiado debido a una corrupción accidental. Linus Torvalds dijo sobre Git en 2007:Si tienes corrupción en el disco, si tienes corrupción en la DRAM, si tienes algún tipo de problema, Git lo notará. No es una cuestión de posibilidades, es una garantía. Puedes tener personas que intentan ser maliciosas, pero tendrán éxito. [...] Nadie ha podido romper SHA-1, pero el punto es que SHA-1, en lo que respecta a Git, ni siquiera es una característica de seguridad. Es puramente un chequeo de consistencia. Las partes de seguridad están en otros lugares, por lo que muchas personas asumen que, dado que Git utiliza SHA-1 y SHA-1 se usa para cosas criptográficamente seguras, piensan que, está bien, es una gran característica de seguridad. No tiene nada que ver con la seguridad, es solo el mejor hash que puedes obtener... Te garantizo que, si pones tus datos en Git, puedes confiar en el hecho de que cinco años después, después de haber sido convertidos de tu disco duro a DVD a cualquier nueva tecnología y lo copiaste, cinco años después puedes verificar que los datos que obtienes son exactamente los mismos datos que pusiste. [...] Una de las razones por las que me importa es que, para el kernel, tuvimos una brecha en uno de los sitios de BitKeeper donde las personas intentaron corromper los repositorios del código fuente del kernel.Sin embargo, Git no requiere la resistencia al segundo preimagen de SHA-1 como una característica de seguridad, ya que siempre preferirá mantener la versión más antigua de un objeto en caso de colisión, evitando que un atacante sobrescriba archivos de manera furtiva. Los ataques conocidos (hasta 2020) tampoco rompen la resistencia al segundo preimagen.

 Criptoanálisis y validación
Para una función hash para la cual *L* es el número de bits en el resumen del mensaje, encontrar un mensaje que corresponda a un resumen de mensaje dado siempre se puede hacer utilizando una búsqueda de fuerza bruta en aproximadamente 2*L* evaluaciones. Esto se llama un ataque de preimagen y puede ser práctico o no, dependiendo de *L* y el entorno computacional particular. Sin embargo, una colisión, que consiste en encontrar dos mensajes diferentes que producen el mismo resumen de mensaje, requiere en promedio solo alrededor de  evaluaciones utilizando un ataque de cumpleaños. Así, la fortaleza de una función hash se compara generalmente con un cifrador simétrico de la mitad de la longitud del resumen del mensaje. SHA-1, que tiene un resumen de mensaje de 160 bits, se pensaba originalmente que tenía una fuerza de 80 bits.

Algunas de las aplicaciones que utilizan hashes criptográficos, como el almacenamiento de contraseñas, están solo mínimamente afectadas por un ataque de colisión. Construir una contraseña que funcione para una cuenta dada requiere un ataque de preimagen, así como acceso al hash de la contraseña original, que puede o no ser trivial. Invertir la encriptación de contraseñas (por ejemplo, para obtener una contraseña para probar contra la cuenta de un usuario en otro lugar) no es posible por medio de los ataques. Sin embargo, incluso un hash de contraseña seguro no puede prevenir ataques de fuerza bruta en contraseñas débiles.

En el caso de la firma de documentos, un atacante no podría simplemente falsificar una firma de un documento existente: el atacante tendría que producir un par de documentos, uno inocuo y uno dañino, y conseguir que el titular de la clave privada firme el documento inocuo. Hay circunstancias prácticas en las que esto es posible; hasta finales de 2008, era posible crear certificados SSL falsificados utilizando una colisión de MD5.

Debido a la estructura de bloques e iterativa de los algoritmos y la ausencia de pasos finales adicionales, todas las funciones SHA (excepto SHA-3) son vulnerables a ataques de extensión de longitud y colisión de mensajes parciales. Estos ataques permiten a un atacante falsificar un mensaje firmado solo por un hash con clave – SHA(mensaje || clave) o SHA(clave || mensaje), extendiendo el mensaje y recalculando el hash sin conocer la clave. Una mejora simple para prevenir estos ataques es hacer hash dos veces:  (la longitud de 0*b*, bloque cero, es igual al tamaño del bloque de la función hash).

 SHA-0
En CRYPTO 98, dos investigadores franceses, Florent Chabaud y Antoine Joux, presentaron un ataque a SHA-0: se pueden encontrar colisiones con una complejidad de 261, menos que los  2^80 para una función hash ideal del mismo tamaño.

En 2004, Biham y Chen encontraron casi colisiones para SHA-0 – dos mensajes que hash a valores casi iguales; en este caso, 142 de los 160 bits son iguales. También encontraron colisiones completas de SHA-0 reducidas a 62 de sus 80 rondas.

Posteriormente, el 12 de agosto de 2004, se anunció una colisión para el algoritmo completo SHA-0 por Joux, Carribault, Lemuet y Jalby. Esto se logró utilizando una generalización del ataque de Chabaud y Joux. Encontrar la colisión tuvo una complejidad de 251 y tomó alrededor de 80,000 horas de procesador en una supercomputadora con 256 procesadores Itanium 2 (equivalente a 13 días de uso continuo de la computadora).

El 17 de agosto de 2004, en la Rump Session de CRYPTO 2004, se anunciaron resultados preliminares por Wang, Feng, Lai y Yu, sobre un ataque a MD5, SHA-0 y otras funciones hash. La complejidad de su ataque a SHA-0 es de 240, significativamente mejor que el ataque de Joux *et al*.

En febrero de 2005, se anunció un ataque de Xiaoyun Wang, Yiqun Lisa Yin y Hongbo Yu que podría encontrar colisiones en SHA-0 en 239 operaciones.

Otro ataque en 2008 aplicando el ataque de boomerang redujo la complejidad de encontrar colisiones a 233.6, lo que se estimó que tomaría 1 hora en una PC promedio del año 2008.

A la luz de los resultados de SHA-0, algunos expertos sugirieron que se reconsideraran los planes para el uso de SHA-1 en nuevos sistemas criptográficos. Después de la publicación de los resultados de CRYPTO 2004, el NIST anunció que planeaba eliminar el uso de SHA-1 para 2010 en favor de las variantes SHA-2.

 Ataques
A principios de 2005, Vincent Rijmen y Elisabeth Oswald publicaron un ataque a una versión reducida de SHA-1 – 53 de 80 rondas – que encuentra colisiones con un esfuerzo computacional de menos de 280 operaciones.

En febrero de 2005, se anunció un ataque de Xiaoyun Wang, Yiqun Lisa Yin y Hongbo Yu. Los ataques pueden encontrar colisiones en la versión completa de SHA-1, requiriendo menos de 269 operaciones. (Una búsqueda de fuerza bruta requeriría 280 operaciones).

Los autores escriben: "En particular, nuestro análisis se basa en el ataque diferencial original a SHA-0, el ataque de casi colisión a SHA-0, las técnicas de colisión multibloque, así como las técnicas de modificación de mensajes utilizadas en el ataque de búsqueda de colisión en MD5. Romper SHA-1 no sería posible sin estas poderosas técnicas analíticas". Los autores han presentado una colisión para SHA-1 de 58 rondas, encontrada con 233 operaciones hash. El artículo con la descripción completa del ataque se publicó en agosto de 2005 en la conferencia CRYPTO.

En una entrevista, Yin declara que, "En términos generales, explotamos las siguientes dos debilidades: Una es que el paso de preprocesamiento de archivos no es lo suficientemente complicado; otra es que ciertas operaciones matemáticas en las primeras 20 rondas tienen problemas de seguridad inesperados".

El 17 de agosto de 2005, se anunció una mejora al ataque de SHA-1 en nombre de Xiaoyun Wang, Andrew Yao y Frances Yao en la Rump Session de CRYPTO 2005, reduciendo la complejidad requerida para encontrar una colisión en SHA-1 a 263. El 18 de diciembre de 2007 se explicaron y verificaron los detalles de este resultado por Martin Cochran.

Christophe De Cannière y Christian Rechberger mejoraron aún más el ataque a SHA-1 en *Finding SHA-1 Characteristics: General Results and Applications*, recibiendo el Best Paper Award en ASIACRYPT 2006. Se presentó una colisión de dos bloques para SHA-1 de 64 rondas, encontrada utilizando métodos no optimizados con 235 evaluaciones de función de compresión. Dado que este ataque requiere el equivalente a aproximadamente 235 evaluaciones, se considera un quiebre teórico significativo. Su ataque se extendió aún más a 73 rondas (de 80) en 2010 por Grechnikov.Para encontrar una colisión real en las 80 rondas completas de la función hash, se requieren cantidades enormes de tiempo de computación. Con este fin, una búsqueda de colisiones para SHA-1 utilizando la plataforma de computación voluntaria BOINC comenzó el 8 de agosto de 2007, organizada por la Universidad Tecnológica de Graz. El esfuerzo fue abandonado el 12 de mayo de 2009 debido a la falta de progreso.

En la sesión Rump de CRYPTO 2006, Christian Rechberger y Christophe De Cannière afirmaron haber descubierto un ataque de colisión en SHA-1 que permitiría a un atacante seleccionar al menos partes del mensaje.

En 2008, una metodología de ataque presentada por Stéphane Manuel reportó colisiones de hash con una complejidad teórica estimada de 251 a 257 operaciones. Sin embargo, luego retractó esa afirmación tras descubrir que las trayectorias de colisión local no eran realmente independientes, y finalmente citó un vector de colisión eficiente que ya era conocido antes de este trabajo.

Cameron McDonald, Philip Hawkes y Josef Pieprzyk presentaron un ataque de colisión de hash con una complejidad estimada de 252 en la sesión Rump de Eurocrypt 2009. Sin embargo, el artículo correspondiente, "Differential Path for SHA-1 with complexity O(252)", fue retirado debido a que los autores descubrieron que su estimación era incorrecta.

Uno de los ataques contra SHA-1 fue desarrollado por Marc Stevens, quien estimó un costo de $2.77 millones (en 2012) para romper un solo valor de hash alquilando poder de procesamiento en servidores en la nube. Stevens desarrolló este ataque en un proyecto llamado HashClash, implementando un ataque de trayectoria diferencial. El 8 de noviembre de 2010, afirmó haber implementado completamente un ataque de casi colisión contra SHA-1 completo, con una complejidad estimada equivalente a 257.5 compresiones SHA-1. Estimó que este ataque podría extenderse a una colisión completa con una complejidad de alrededor de 261.

 *The SHAppening*
El 8 de octubre de 2015, Marc Stevens, Pierre Karpman y Thomas Peyrin publicaron un ataque de colisión freestart contra la función de compresión de SHA-1 que requiere solo 257 evaluaciones de SHA-1. Esto no se traduce directamente en una colisión en la función hash SHA-1 completa (donde un atacante no puede elegir libremente el estado interno inicial), pero socava las afirmaciones de seguridad para SHA-1. En particular, fue la primera vez que se *demostró* un ataque contra SHA-1 completo; todos los ataques anteriores eran demasiado costosos para ser llevados a cabo. Los autores denominaron a este avance en la criptoanálisis de SHA-1 *The SHAppening*.

El método se basó en su trabajo anterior, así como en las trayectorias auxiliares (o boomerangs) para acelerar la técnica de Joux y Peyrin, utilizando tarjetas GPU de Nvidia de alto rendimiento y costo eficiente. La colisión fue encontrada en un clúster de 16 nodos con un total de 64 tarjetas gráficas. Los autores estimaron que una colisión similar podría encontrarse alquilando US$2,000 de tiempo de GPU en EC2.

Los autores estimaron que el costo de alquilar suficiente tiempo de CPU/GPU en EC2 para generar una colisión completa de SHA-1 en el momento de la publicación oscilaba entre US$75K y $120K, y señalaron que eso estaba bien dentro del presupuesto de organizaciones criminales, sin mencionar las agencias de inteligencia nacionales. Por lo tanto, los autores recomendaron que SHA-1 fuera depreciado lo más pronto posible.

 *SHAttered* – primera colisión pública
El 23 de febrero de 2017, el CWI (Centrum Wiskunde & Informatica) y Google anunciaron el ataque *SHAttered*, en el cual generaron dos archivos PDF diferentes con el mismo hash SHA-1 en aproximadamente 263.1 evaluaciones de SHA-1. Este ataque es aproximadamente 100,000 veces más rápido que forzar una colisión de SHA-1 mediante un ataque de cumpleaños, que se estimaba tomaría 280 evaluaciones de SHA-1. El ataque requirió "el poder de procesamiento equivalente a 6,500 años de cálculos en una sola CPU y 110 años en una sola GPU".

***Birthday-Near-Collision Attack* – primer ataque práctico de prefijo elegido**

El 24 de abril de 2019, un artículo de Gaëtan Leurent y Thomas Peyrin presentado en Eurocrypt 2019 describió una mejora del ataque de prefijo determinado en funciones de digestión tipo Merkle-Damgård basadas en cifrados de bloque Davies-Meyer. Con estas mejoras, el método es capaz de encontrar colisiones de prefijo determinado en aproximadamente 268 evaluaciones de SHA-1. Esto es aproximadamente 1,000 millones de veces más rápido (y ahora utilizable para muchos ataques dirigidos, gracias a la posibilidad de elegir un prefijo, por ejemplo, código malicioso o identidades falsificadas en certificados firmados) que el ataque anterior con 277.1 evaluaciones (pero sin prefijo determinado, lo que lo hacía impráctico para la mayoría de ataques dirigidos debido a que las colisiones encontradas eran casi aleatorias) y es lo suficientemente rápido como para ser práctico para atacantes con recursos, requiriendo aproximadamente $100,000 en procesamiento en la nube. Este método también es capaz de encontrar colisiones de prefijo elegido en la función MD5, pero con una complejidad de 246.3 no supera el mejor método disponible anteriormente a nivel teórico (239), aunque potencialmente a nivel práctico (≤249). Este ataque tiene un requisito de memoria de más de 500 GB.

El 5 de enero de 2020, los autores publicaron un ataque mejorado llamado "shambles". En este artículo demuestran un ataque de colisión de prefijo elegido con una complejidad de 263.4, que en el momento de la publicación costaría US$45K por colisión generada.

 Validación oficial
Las implementaciones de todas las funciones de seguridad aprobadas por FIPS pueden ser validadas oficialmente a través del programa CMVP, gestionado conjuntamente por el Instituto Nacional de Estándares y Tecnología (NIST) y el Centro de Seguridad de las Comunicaciones (CSE). Para la verificación informal, se pone a disposición un paquete para generar un gran número de vectores de prueba en el sitio del NIST; sin embargo, esta verificación no reemplaza la validación formal del CMVP, que es requerida por ley para ciertas aplicaciones.

A diciembre de 2013, hay más de 2000 implementaciones validadas de SHA-1, con 14 de ellas capaces de manejar mensajes con una longitud en bits no múltiplo de ocho.

 Ejemplos y pseudocódigo

 Ejemplos de hashes
A continuación, se muestran ejemplos resumen de mensajes de SHA-1 en codificación hexadecimal y en codificación Base64 (de binario a ASCII).

 SHA1("The quick brown fox jumps over the lazy **d**og")
 Salida en hexadecimal: 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12
 Codificación binaria Base64 a texto ASCII generada: L9ThxnotKPzthJ7hu3bnORuT6xI=

Incluso un pequeño cambio en el mensaje, con una probabilidad abrumadora, resultará en el cambio de muchos bits debido al efecto avalancha. Por ejemplo, cambiar dog por cog produce un hash con valores diferentes en 81 de los 160 bits:

 SHA1("The quick brown fox jumps over the lazy **c**og")
 Salida en hexadecimal: de9f2c7fd25e1b3afad3e85a0bd17d9b100db4b3
 Codificación binaria Base64 a texto ASCII generada: 3p8sf9JeGzr60+haC9F9mxANtLM=

El hash de la cadena de longitud cero es:

 SHA1("")
 Salida en hexadecimal: da39a3ee5e6b4b0d3255bfef95601890afd80709
 Codificación binaria Base64 a texto ASCII generada: 2jmj7l5rSw0yVb/vlWAYkK/YBwk=

 Pseudocódigo para SHA-1
Pseudocódigo para el algoritmo SHA-1:
 *Note 1: Todas las variables son cantidades sin signo de 32 bits y se envuelven en el módulo 232 durante los cálculos, excepto por los siguientes:*

         *ml, longitud del mensaje, which is a 64-bit quantity, and*
         *hh, resumen del mensa, que es una cantidad de 160 bits.*
 *Note 2: Todas las constantes en este pseudocódigo están en big endian.*
         *Dentro de cada palabra, el byte más significativo se almacena en la posición de byte más a la izquierda.*

 *Inicializar variables:*

 h0 = 0x67452301
 h1 = 0xEFCDAB89
 h2 = 0x98BADCFE
 h3 = 0x10325476
 h4 = 0xC3D2E1F0

 ml = longitud del mensaje en bits (siempre un múltiplo del número de bits en un carácter).

 *Preprocesamiento:*
 agregar el bit '1' al mensaje, por ejemplo, agregar 0x80 si la longitud del mensaje es un múltiplo de 8 bits.
 añadir entre 0 ≤ k < 512 bits de '0', de manera que la longitud resultante del mensaje sea congruente a -64 ≡ 448 (mod 512)
 añadir ml, la longitud original de mensaje en bits, como un entero de 64 bits en big endian.
    Así, la longitud total es un múltiplo de 512 bits.

 *Procesar el mensaje en bloques sucesivos de 512-bits:*
 dividir el mensaje en bloques de 512 bits
 **para** cada bloque
     dividir el bloque en dieciséis palabras de 32 bits en *bid endian*  w[i], 0 ≤ i ≤ 15

     *Programar el mensaje: extender las dieciséis palabras de 32 bits en ochenta palabras de 32 bits:*
     **Para** i **desde** 16 hasta 79
 *Nota 3: SHA-0 se diferencia por no tener esta rotación a la izquierda.*
         w[i] = (w[i-3] **xor** w[i-8] **xor** w[i-14] **xor** w[i-16]) **leftrotate** 1

     *Inicializar el valor de hash para este bloque:*
     a = h0
     b = h1
     c = h2
     d = h3
     e = h4

     *Bucle principal:*
     **Para** i **desde** 0 **hasta** 79
         **if** 0 ≤ i ≤ 19 **then**
             f = (b **and** c) **or** ((**not** b) **and** d)
             k = 0x5A827999
         **else if** 20 ≤ i ≤ 39
             f = b **xor** c **xor** d
             k = 0x6ED9EBA1
         **else if** 40 ≤ i ≤ 59
             f = (b **and** c) **or** (b **and** d) **or** (c **and** d)
             k = 0x8F1BBCDC
         **else if** 60 ≤ i ≤ 79
             f = b **xor** c **xor** d
             k = 0xCA62C1D6

         temp = (a **leftrotate** 5) + f + e + k + w[i]
         e = d
         d = c
         c = b **leftrotate** 30
         b = a
         a = temp

     *Sumar el hash de este bloque al resultado hasta el momento:*
     h0 = h0 + a
     h1 = h1 + b
     h2 = h2 + c
     h3 = h3 + d
     h4 = h4 + e

 *Generar el valor final del hash (big endian) como el número de 160 bits:*
 hh = (h0 **leftshift** 128) **or** (h1 **leftshift** 96) **or** (h2 **leftshift** 64) **or** (h3 **leftshift** 32) **or** h4
El número hh es el resumen del mensaje, que puede escribirse en hexadecimal digest (base 16).

Los valores constantes empleados en el algoritmo se asumieron como números sin-nada-sacado-de-la-manga:

 Las cuatro constantes de ronda k son 230 multiplicado por las raíces cuadradas de 2, 3, 5 y 10. Sin embargo, se redondearon incorrectamente al entero más cercano en lugar de redondearse al entero impar más cercano, con proporciones equilibradas de bits cero y uno. Además, elegir la raíz cuadrada de 10 (que no es un número primo) la convirtió en un factor común para las otras dos raíces cuadradas elegidas de los primos 2 y 5, con posibles propiedades aritméticas utilizables en rondas sucesivas, lo que redujo la fuerza del algoritmo contra la detección de colisiones en algunos bits.
 Los primeros cuatro valores iniciales para h0 a h3 son los mismos que en el algoritmo MD5, y el quinto (para h4) es similar. Sin embargo, no fueron verificados adecuadamente para resistir la inversión de las primeras rondas con el fin de inferir posibles colisiones en algunos bits, lo cual es utilizable en ataques diferenciales multibloque.

En lugar de la formulación del FIPS PUB 180-1 original mostrada, se pueden usar las siguientes expresiones equivalentes para calcular f en el bucle principal mencionado arriba:
 *Selección a nivel de bits entre* c y d*, controlada por* b*.*
 (0  ≤ i ≤ 19): f = d **xor** (b **and** (c **xor** d))                *(alternativa 1)*
 (0  ≤ i ≤ 19): f = (b **and** c) **or** ((**not** b) **and** d)           *(alternativa 2)*
 (0  ≤ i ≤ 19): f = (b **and** c) **xor** ((**not** b) **and** d)          *(alternativa 3)*
 (0  ≤ i ≤ 19): f = vec_sel(d, c, b)                       *(alternativa 4)*
  [premo08]
 *Función mayoritaria a nivel de bits.*
 (40 ≤ i ≤ 59): f = (b **and** c) **or** (d **and** (b **or** c))          *(alternativa 1)*
 (40 ≤ i ≤ 59): f = (b **and** c) **or** (d **and** (b **xor** c))         *(alternativa 2)*
 (40 ≤ i ≤ 59): f = (b **and** c) **xor** (d **and** (b **xor** c))        *(alternativa 3)*
 (40 ≤ i ≤ 59): f = (b **and** c) **xor** (b **and** d) **xor** (c **and** d)  *(alternativa 4)*
 (40 ≤ i ≤ 59): f = vec_sel(c, b, c **xor** d)                 *(alternativa 5)*
También se demostró que para las rondas 32-79, el cálculo de:
 w[i] = (w[i-3] **xor** w[i-8] **xor** w[i-14] **xor** w[i-16]) **leftrotate** 1
puede ser reemplazado de la siguiente manera:
 w[i] = (w[i-6] **xor** w[i-16] **xor** w[i-28] **xor** w[i-32]) **leftrotate** 2
Esta transformación mantiene todos los operandos de 64 bits y, al eliminar la dependencia de   w[i] en w[i-3], permite la implementación eficiente SIMD que usa una longitud de vector de 4, como en las instrucciones SSE de x86.

 Comparación de funciones SHA
En la siguiente tabla, el *estado interno* se refiere a la «suma interna hash» después de cada compresión de un bloque de datos.

 Implementaciones
A continuación se muestra una lista de bibliotecas criptográficas que admiten SHA-1:

 Botan
 Bouncy Castle
 cryptlib
 Crypto++
 Libgcrypt
 Mbed TLS
 Nettle
 LibreSSL
 OpenSSL
 GnuTLS

La aceleración por hardware está proporcionada por las siguientes extensiones de procesadores:

 Extensiones Intel SHA: Disponibles en algunos procesadores x86 de Intel y AMD.
 VIA PadLock.
 IBM z/Architecture: Disponible desde 2003 como parte de la Extensión Message-Security-Assist.

 Contramedida para colisiones
Tras el ataque SHAttered, Mark Stevens y Dan Shumow publicaron "sha1collisiondetection" (SHA-1CD), una variante de SHA-1 que detecta ataques de colisión y cambia la salida del hash cuando se detecta una. La tasa de falsos positivos es de 2^-90.[2] SHA-1CD es utilizado por GitHub desde marzo de 2017 y por git desde la versión 2.13.0 de mayo de 2017.[3]

 Véase también
 Secure Hash Algorithm

 Referencias

 Additional bibliography

 Enlaces externos

 CSRC Cryptographic Toolkit – NIST (en inglés). Sitio web oficial del Secure Hash Standard.
 FIPS 180-4: Secure Hash Standard (SHS) (en inglés).
  (with sample C implementation) (en inglés).
 Entrevista con Yiqun Lisa Yin acerca de los ataques SHA-1 (en inglés).
 Explicación de los ataques SHA-1 (3 páginas, 2006) (en inglés).
 Cryptography Research – Hash Collision Q&A (en inglés).
  en Curlie.
