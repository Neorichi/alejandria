---
type: Artículo de enciclopedia
title: Cifrado (criptografía)
description: En criptografía, el cifrado es el proceso de codificación de la información.
resource: https://es.wikipedia.org/wiki/Cifrado_(criptografía)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_(criptografía)"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_(criptografía)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado (criptografía)

En criptografía, el **cifrado** es el proceso de codificación de la información. Este proceso convierte la representación original de la información, conocida como texto plano, en una forma alternativa conocida como texto cifrado. En el mejor de los casos, sólo las partes autorizadas pueden descifrar un texto cifrado para convertirlo en texto plano y acceder a la información original. El cifrado no impide por sí mismo las interferencias, pero niega el contenido inteligible a un posible interceptor.

Por razones técnicas, un esquema de cifrado suele utilizar una clave de cifrado pseudoaleatoria generada por un algoritmo. Es posible descifrar el mensaje sin poseer la clave, pero, para un esquema de encriptación bien diseñado, se requieren considerables recursos computacionales y habilidades. Un destinatario autorizado puede descifrar fácilmente el mensaje con la clave proporcionada por el emisor a los destinatarios, pero no a los usuarios no autorizados.

Históricamente, se han utilizado varias formas de encriptación para ayudar a la criptografía. Las primeras técnicas de cifrado se utilizaban a menudo en la mensajería militar. Desde entonces, han surgido nuevas técnicas que se han convertido en habituales en todos los ámbitos de la informática moderna. Los esquemas modernos de encriptación utilizan los conceptos de clave pública y clave simétrica.

Las técnicas modernas de encriptación garantizan la seguridad porque los ordenadores modernos son ineficaces para descifrar la encriptación.

 Terminología
En el proceso de cifrado/descifrado se establecen una serie de términos y convenios para facilitar referirse a los distintos elementos que intervienen:

El **texto en claro** o **texto simple** (en inglés, *plain text*) es el mensaje que se cifra.
El **criptograma** o **texto cifrado** es el mensaje resultante una vez que se ha producido el cifrado, es decir, el mensaje cifrado.
El **cifrado** es el proceso que consiste en convertir el *texto plano* en un galimatías ilegible (cifrar), el mensaje cifrado.
El **cifrador** es el sistema que implementa el algoritmo de cifrado.
El **algoritmo de cifrado** o cifra es el algoritmo que se utiliza para cifrar.
La **clave de cifrado** se utiliza en el algoritmo de cifrado.
El **descifrado** es el proceso de convertir el texto cifrado en el texto en claro.
El **descifrador** es el sistema que implementa el algoritmo de descifrado.
El **algoritmo de descifrado** o descifra es el algoritmo que se utiliza para descifrar.
La **clave de descifrado **se utiliza en el algoritmo de descifrado.
La **gestión de claves** es el proceso de generación, certificación, distribución y cancelación de todas las claves, necesarios para llevar a cabo el cifrado.
El **criptosistema** es el conjunto estructurado de los protocolos, los algoritmos de cifrado/descifrado, los procesos de gestión de claves y las actuaciones de los usuarios.
La **descripción de entidades**: cuando se desea describir un algoritmo de cifrado/descifrado que involucra el envío de mensajes secretos, muchos autores usan los nombres genéricos *Alice* y *Bob* en lugar de los crípticos A y B. Si intervienen otras entidades (C, D, F... -la E quedaría reservada-), se les asignan entonces nombres que empiecen con estas iniciales, y los más frecuentes son *Carol* y *Dave*. Cuando un escenario involucra protección frente a atacantes que hacen escuchas, entonces para referirse a ellos se suele usar el nombre *Eve* (del término inglés *eavesdropper*, "fisgón") o bien el nombre *Mallory*, en caso de que el atacante, además de interceptar el mensaje, tenga la habilidad de alterarla.

Con frecuencia a los procesos de cifrado y descifrado se les denomina *encriptado* y *desencriptado*, ambos anglicismos de los términos ingleses *encrypt* y *decrypt*. La Real Academia Española recogió esa acepción en la edición de su diccionario de 2014. Por su parte La Fundación del Español Urgente defiende que *encriptar* es un término válido y que no hay razón para censurar su uso.

 Preprocesado del texto simple
En algunas ocasiones, antes de cifrar se realiza un preproceso de adaptación del texto plano. En este proceso se pueden seguir varios pasos que permitan el cifrado o hagan que el cifrado resultante sea más resistente frente a ataques por criptoanálisis. Todos estos cambios se tendrán que tener en cuenta cuando se realice el descifrado para poder obtener el texto plano original. Por ejemplo, son frecuentes las siguientes operaciones:

**Conversión de alfabeto**. Algunos cifradores usan un alfabeto del texto en claro que no se corresponde con el del mensaje que se quiere cifrar. Por tanto, es necesario adaptar el mensaje a ese alfabeto. Por ejemplo, algunos cifradores usan como alfabeto del texto plano el alfabeto latino. Si se desea cifrar un texto en español, es necesario realizar un proceso como resultado del cual no aparezcan los caracteres H, J, Ñ, K, U, W y Y (por ejemplo, podrían sustituirse la U y la W por la V, la K con la Q, la Ñ por la N, la Y por la I, la J por la G, y eliminar la H). Otro ejemplo clásico es el caso de cifradores que no permiten cifrar minúsculas, en cuyo caso será necesario convertir todo en mayúsculas.
**Preproceso para dificultar el criptoanálisis**. Para aumentar la calidad del texto cifrado con cierto cifrador, ya sea por su resistencia frente a ataques, extensión o cualquier otra circunstancia, a veces se preprocesa el texto en claro. Algunos ejemplos de estrategias son:
Inclusión de fragmentos que son para despistar y que no tienen ningún significado. Habitualmente estos fragmentos son caracteres, y se denominan *caracteres nulos*.
Eliminación de situaciones del texto claro que pueden ser aprovechadas por ataques de criptoanálisis. Por ejemplo:
Los espacios en blanco y signos de puntuación suelen eliminarse para que, además de conseguir una trasmisión más eficiente, se consiga que las palabras no se puedan distinguir por los contornos. Esto puede producir ambigüedades que se tenían que resolver por el contexto.
Los casos de secuencias de letras idénticas seguidas (por ejemplo, *RR* o *LL* del idioma español, en ciertos tipos de cifradores pueden ser aprovechadas por atacantes. Para romper estas secuencias de caracteres iguales, suelen aplicarse dos estrategias: eliminar uno de los caracteres o meter un contenido que no se tiene que interpretar (si es un solo carácter, se le llama *carácter nulo*).
**Usar un código**. A veces, antes de cifrar, se utiliza un código que dificulta llegar al significado de ciertas palabras o frases especialmente importantes o habituales.
**Conversión a números**. Hay algunos algoritmo de cifrado como el RSA que necesitan convertir los caracteres en números. Se pueden seguir distintas estrategias. Veamos algunos ejemplo:
Podríamos usar una tabla de conversión de los caracteres en números usando algún sistema de codificación de caracteres como ASCII o Unicode. Por ejemplo el mensaje "Hello World" usando Unicode-8 quedaría:
48 65 6C 6C 6F 20 57 6F 72 6C 64
Esta cadena de bytes podríamos convertirla en un número concatenándolos obteniendo:
0x48656C6C6F20576F726C64=87521618088882533792115812
Otra opción podría ser considerar que los caracteres están ordenados según un criterio e interpretar la cadena como un número con base el número de caracteres del alfabeto. Por ejemplo si consideramos que solo hay caracteres en mayúsculas y los ordenamos según el orden alfabético tendríamos por ejemplo:
"HIJO"
El cualquier caso el número resultante puede ser demasiado pequeño lo que podría producir un texto cifrado que no sea seguro. Para ello se suele aplicar un esquema de relleno (ejemplo  PKCS#1v1.5, el cual está ya roto, o OAEP descrito en PKCS#1v2.0)

 Tipos de cifrado según sus claves

 Cifrado Simétrico
En esquemas de clave simétrica,  las claves de cifrado y descifrado son las mismas. Las partes comunicantes deben tener la misma clave para lograr una comunicación segura. Un ejemplo de una clave simétrica es la máquina Enigma del ejército alemán. Había configuraciones clave para cada día. Cuando los Aliados descubrieron cómo funcionaba la máquina, pudieron descifrar la información codificada dentro de los mensajes tan pronto como pudieron descubrir la clave de cifrado para las transmisiones de un día determinado.

La criptografía simétrica es la técnica criptográfica más antigua que existe, pero sigue ofreciendo un alto nivel de seguridad. Se basa en la utilización de una única clave secreta que se encargará de cifrar y descifrar la información, ya sea información en tránsito con protocolos como TLS, o información en un dispositivo de almacenamiento extraíble. La criptografía simétrica fue el primer método empleado para el cifrado de la información, se basa en que se utilizará la misma contraseña tanto para el cifrado como el descifrado, por tanto, es fundamental que todos los usuarios que quieran cifrar o descifrar el mensaje, tengan esta clave secreta, de lo contrario, no podrán hacerlo. Gracias a la criptografía simétrica, podremos realizar comunicaciones o almacenar archivos de forma segura.

El cifrado simétrico es una de las más antiguas formas de cifrado de la historia. La cual utiliza una sola clave para cifrar y la misma clave para descifrar.

 Cifrado Asimétrico
En los esquemas de cifrado de clave pública, la clave de cifrado se publica para que cualquiera pueda usar y cifrar mensajes. Sin embargo, solo la parte receptora tiene acceso a la clave de descifrado que permite leer los mensajes. El cifrado de clave pública se describió por primera vez en un documento secreto en 1973; antes de eso, todos los esquemas de cifrado eran de clave simétrica (también llamada clave privada). Aunque se publicó posteriormente, el trabajo de Diffie y Hellman, fue publicado en una revista con un gran número de lectores, y el valor de la metodología se describió explícitamente y el método se conoció como el intercambio de claves Diffie Hellman.Una aplicación de cifrado de clave pública disponible públicamente llamada Pretty Good Privacy (PGP) fue escrita en 1991 por Phil Zimmermann y distribuida gratuitamente con el código fuente. PGP fue comprado por Symantec en 2010 y se actualiza regularmente. A este tipo de cifrado también se le llama **criptografía de clave pública** o **PKE** (del inglés *Public-Key Encryption*). Los métodos más conocidos de este tipo de cifrado son el RSA y ElGamal.

La utilización de un sistema simétrico o asimétrico depende de las tareas a cumplir. La criptografía asimétrica presenta dos ventajas principales: suprime el problema de transmisión segura de la clave y permite la firma electrónica. No reemplaza sin embargo los sistemas simétricos, ya que los tiempos de cálculo son evidentemente más cortos con los sistemas simétricos que con los asimétricos.

 Tipos de cifrado según sus algoritmos
Según la forma en la que operan los algoritmos de cifrado o descifrado, es posible distinguir varios tipos:

Cifrado en flujo: En estos algoritmos el cifrado se realiza bit a bit. Están basados en la utilización de claves muy largas que son utilizadas tanto para cifrar como para descifrar. Estas claves pueden estar predeterminadas (libreta de un solo uso) o generarse usando un generador de claves pseudoaleatorias o RKG (acrónimo del inglés *r*andom *k*ey *g*enerator), que genera una secuencia binaria pseudoaleatoria a partir de una clave de inicialización K. A veces, en el cálculo de la clave pseudoaleatoria también interviene el mensaje cifrado hasta ese momento. Por otra parte, el cifrador propiamente dicho: habitualmente en este tipo de algoritmos hay que mantener en secreto tanto la clave como el cifrador.
Cifrado por bloques: En este tipo de algoritmos, el cifrado se realiza bloque a bloque. En primera instancia, se descompone el mensaje en bloques de la misma longitud. A continuación, cada bloque se va convirtiendo en un bloque del mensaje cifrado mediante una secuencia de operaciones. Ejemplos típicos de operaciones realizadas para conseguir cada mensaje cifrado son la sustitución y la permutación (cifrado por transposición) de elementos.
Este tipo de algoritmos pueden ser tanto de clave simétrica como de clave asimétrica. Sin embargo, en la bibliografía suele haber confusión y es frecuente ver casos en que se refieren solo a algoritmos de clave simétrica.

 La criptografía en el pasado
En la criptografía clásica los cifrados se basaban en la sustitución (cifrado por sustitución), en la permutación (cifrado por transposición) o en una combinación de ambas técnicas. Habitualmente, las operaciones se aplicaban a bloques aunque otras veces se aplicaban al texto plano completo. Había cifrados por transposición que cambiaban la posición de caracteres a lo largo de la cadena que tenía que cifrarse. Por ejemplo, un cifrado podía consistir en permutar e invertir el orden de los caracteres, dejando el primer carácter en la última posición, el último en la primera posición, el segundo en penúltimo lugar, etcétera.

 Cifrado en tiempos modernos
Hoy en día, el cifrado se utiliza en la transferencia de comunicación a través de Internet para la seguridad y el comercio. A medida que la potencia de cálculo continúa  aumentando, el cifrado de los ordenadores está en constante evolución para evitar los ataques de espionaje. Con uno de los primeros paquetes de cifrado "modernos", Data Encryption Standard (DES), que utiliza una clave de 56 bits con 72.057.594.037.927.936 posibilidades, una contraseña pudo ser descifrada en 22 horas y 15 minutos por el DES cracker de la  Electronic Frontier Foundation en 1999, que utilizaba un método de  ataque por fuerza bruta para descifrar. Los estándares de cifrado modernos suelen utilizar tamaños de clave más fuertes, a menudo de 256, como AES (modo de 256 bits), Twofish, ChaCha20-Poly1305, Serpent (configurable hasta 512 bits). Los paquetes de cifrado que utilizan una clave de 128 bits o superior, como el Advanced Encryption Standard, no podrán ser forzados de forma bruta debido a la cantidad total de claves de 3,4028237e+38 posibilidades. La opción más probable para descifrar cifradores con un tamaño de clave elevado es encontrar vulnerabilidades en el propio cifrado, como sesgos inherentes (combinaciones obvias, o ligadas al usuario) y puertas traseras. Por ejemplo, el RC4, un cifrado de flujo, fue descifrado debido a sesgos inherentes y vulnerabilidades en el cifrado.

 Tipos de cifrado según sus propiedades
Muchas veces se agrupan los algoritmos de cifrado en función de sus propiedades o características. Algunos ejemplos:

 cifrado seguro hacia adelante
 cifrado con umbral
 cifrado basado en identidad
 cifrado negable
 cifrado con clave aislada
 cifrado maleable

 Limitaciones
El cifrado se utiliza en el  para proteger los datos digitales y los sistemas de información. Con el aumento de la potencia de cálculo, la tecnología de encriptación se ha vuelto más avanzada y segura. Sin embargo, este avance tecnológico también ha puesto de manifiesto una posible limitación de los métodos de encriptación actuales.

Hoy en día, el estándar de las claves de cifrado modernas es de hasta 2048 bits con el sistema RSA. Descifrar una clave de cifrado de 2048 bits es casi imposible a la luz del número de combinaciones posibles. Sin embargo, la computación cuántica amenaza con cambiar esta naturaleza segura.

La computación cuántica utiliza las propiedades de la mecánica cuántica para procesar grandes cantidades de datos simultáneamente. Se ha descubierto que la computación cuántica alcanza velocidades de cálculo miles de veces superiores a las de los superordenadores actuales. Esta potencia de cálculo supone un reto para la tecnología de cifrado actual. Por ejemplo, el cifrado RSA utiliza la multiplicación de números primos muy grandes para crear un número semiprimo para su clave pública. Para descifrar esta clave sin su clave privada, es necesario calcular este número semiprimo, lo que puede llevar mucho tiempo con los ordenadores modernos. Una supercomputadora tardaría entre semanas y meses en factorizar esta clave. Sin embargo, la computación cuántica puede utilizar algoritmos cuánticos para factorizar este número semiprimo en el mismo tiempo que tardan los ordenadores normales en generarlo. Esto haría que todos los datos protegidos por el actual cifrado de clave pública fueran vulnerables a los ataques de la computación cuántica. Otras técnicas de cifrado como la criptografía de curva elíptica y el cifrado de clave simétrica también son vulnerables a la computación cuántica.

Aunque la computación cuántica podría ser una amenaza para la seguridad del cifrado en el futuro, la computación cuántica, tal y como está planteada actualmente, es todavía muy limitada. La computación cuántica actualmente no está disponible comercialmente, no puede manejar grandes cantidades de código y solo existe como dispositivos de cálculo, no como ordenadores. Además, los avances de la computación cuántica podrán utilizarse también a favor del cifrado. La Agencia de Seguridad Nacional (NSA) de los EE.UU. está preparando estándares de encriptación post-cuántica para el futuro. El cifrado cuántico promete un nivel de seguridad que podrá contrarrestar la amenaza de la computación cuántica.

 Véase también
 Cripto AG
 Código
 Confusión entre cifrados y códigos
 Criptografía asimétrica
 Criptografía simétrica
 Cifrado por sustitución
 Cifrado por transposición

 Referencias

 Bibliografía adicional

 Kahn, David (1967), *The Codebreakers - The Story of Secret Writing* 
 Preneel, Bart (2000), "Advances in Cryptology - EUROCRYPT 2000", Springer Berlin Heidelberg,
 Sinkov, Abraham (1966): *Elementary Cryptanalysis: A Mathematical Approach*, Mathematical Association of America.
 Tenzer, Theo (2021): *SUPER SECRETO – The Third Epoch of Cryptography: Multiple, exponential, quantum-secure and above all, simple and practical Encryption for Everyone*, Norderstedt, ISBN 9783755761174.

 Enlaces externos
 La primera máquina electrónica Enigma del mundo (en inglés)
 Video en YouTube
 Cifrado de los mensajes en línea
