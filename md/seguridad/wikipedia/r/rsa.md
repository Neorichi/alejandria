---
type: Artículo de enciclopedia
title: RSA
description: En criptografía, RSA (Rivest, Shamir y Adleman) es un sistema criptográfico de clave pública desarrollado en 1977, que utiliza factorización de números enteros.
resource: https://es.wikipedia.org/wiki/RSA
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/RSA"}
license: CC BY-SA 4.0
id: eswiki-RSA
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# RSA

En criptografía, **RSA** *(**Rivest, Shamir y Adleman**)* es un sistema criptográfico de clave pública desarrollado en 1977, que utiliza factorización de números enteros. Es el primer y más utilizado algoritmo de este tipo y es válido tanto para cifrar como para firmar digitalmente.

La seguridad de este algoritmo radica en el problema de la factorización de números enteros. Los mensajes enviados se representan mediante números, y el funcionamiento se basa en el producto, conocido, de dos números primos grandes elegidos al azar y mantenidos en secreto. Actualmente estos primos son del orden de , y se prevé que su tamaño siempre crezca con el aumento de la capacidad de cálculo de los ordenadores.

Como en todo sistema de clave pública, cada usuario posee dos claves de cifrado: una pública y otra privada. Cuando se quiere enviar un mensaje confidencial, el emisor busca la clave pública del receptor, cifra su mensaje con esa clave, y una vez que el mensaje cifrado llega al receptor, este se ocupa de descifrarlo usando su clave privada.

En el caso de querer firmar (propiedades de autenticidad, integridad y no repudio), el emisor obtiene un hash del mensaje a firmar y lo procesa con su clave privada obteniendo así la firma; se envía el mensaje y la firma; el receptor recalcula el hash y descifra el hash original con la clave pública del emisor, validando así (o no) la firma del mensaje.

Se cree que RSA será seguro mientras no se conozcan formas rápidas de descomponer un número grande en producto de primos. Aunque se cree que la  computación cuántica podría proveer de una solución al problema de factorización, existen investigadores que dudan que dichos avances vayan a volver obsoletos estos algoritmos.

 Historia

El algoritmo fue descrito en 1977 por Ron Rivest, Adi Shamir y Leonard Adleman, del Instituto Tecnológico de Massachusetts (MIT); las letras RSA son las iniciales de sus apellidos. Clifford Cocks, un matemático británico que trabajaba para la agencia de inteligencia británica GCHQ, había descrito un sistema equivalente en un documento interno en 1973. Debido al elevado coste de las computadoras necesarias para implementarlo en la época su idea no trascendió. Su descubrimiento, sin embargo, no fue revelado hasta 1997 ya que era confidencial, por lo que Rivest, Shamir y Adleman desarrollaron RSA de forma independiente.

El algoritmo fue patentado por el MIT en 1983 en Estados Unidos con el número 4.405.829. Esta patente expiró el 21 de septiembre de 2000. Como el algoritmo fue publicado antes de patentar la aplicación, esto impidió que se pudiera patentar en otros lugares del mundo. Dado que Cocks trabajó en un organismo gubernamental, una patente en Estados Unidos tampoco hubiera sido posible.

Es un algoritmo puramente **asimétrico**, junto con DSA. Este algoritmo como su nombre lo indica, sirve para firmar (autenticar) y para cifrar información. Una desventaja del algoritmo DSA es que requiere mucho más tiempo de cómputo que RSA.

 Cifrado RSA
Este consta de tres pasos: generación de claves, cifrado y descifrado

 Idea del cifrado
Supongamos que Bob quiere enviar a Alicia un mensaje secreto que solo ella pueda leer.

Alicia envía a Bob una caja con un candado abierto, del que solo Alicia tiene la llave. Bob recibe la caja, escribe el mensaje, lo pone en la caja y la cierra con su candado (ahora Bob no puede leer el mensaje). Bob envía la caja a Alicia y ella la abre con su llave. En este ejemplo, la caja con el candado (abierto) es la «clave pública» de Alicia, y la llave del candado es su «clave privada».

Técnicamente, Bob envía a Alicia un «mensaje llano»  en forma de un número  menor que otro número , mediante un protocolo reversible conocido como *padding scheme* («patrón de relleno»). A continuación genera el «mensaje cifrado»  mediante la siguiente operación:

,

donde  es la clave pública de Alicia.

Ahora Alicia descifra el mensaje en clave  mediante la operación inversa dada por

,

donde  es la clave privada que solo Alicia conoce.

 Generación de claves
 Se eligen dos números primos distintos  y .
 Por motivos de seguridad, estos números deben escogerse de forma aleatoria y deben tener una longitud en bits parecida. Se pueden hallar primos fácilmente mediante test de primalidad.
 Se calcula .
  se usa como el módulo para ambas claves, pública y privada.
 Con  es la función φ de Euler  calcula  aprovechando las dos propiedades de la función de Euler siguientes:
 si  es primo.
Si a y b son primos entre sí, entonces .
 Se escoge un entero positivo  menor que , que sea coprimo con .
  se da a conocer como el exponente de la clave pública.
 Si se escoge un  con una suma encadenada corta, el cifrado será más efectivo. Un exponente  muy pequeño (p. ej. ) podría suponer un riesgo para la seguridad.
 Se determina un  (mediante aritmética modular) que satisfaga la congruencia , es decir, que  sea el multiplicador modular inverso de
 Expresado de otra manera,  es dividido exactamente por .
 Esto suele calcularse mediante el algoritmo de Euclides extendido.
  se guarda como el exponente de la clave privada.

La **clave pública** es , esto es, el módulo y el exponente de cifrado. La **clave privada** es , esto es, el módulo y el exponente de descifrado, que debe mantenerse en secreto.

Usando las propiedades de la función de Euler, el Teorema de Euler y el Teorema del resto chino se puede demostrar que

Notas
 PKCS#1 v2.0 y PKCS#1 v2.1 se especifican mediante la función de Carmichael  en vez de la función  de Euler, donde  indica el mínimo común múltiplo.
 Para una mayor eficiencia los siguientes valores se calculan de antemano y se almacenan como parte de la clave privada:
  y : los primos para la generación de las claves,
  y ,
 .

 Cifrado
Alicia comunica su clave pública  a Bob y Alicia mantiene su propia clave privada en secreto. Ahora Bob desea enviar un mensaje  a Alicia.

Primero, Bob convierte  en un número entero  menor que . Luego calcula el texto cifrado  mediante la operación

.

Esto puede hacerse rápido mediante el método de exponenciación binaria. Ahora Bob transmite  a Alicia.

 Descifrado

Alicia puede recuperar  a partir de  usando su exponente  de la clave privada mediante el siguiente cálculo:

.

Ahora que tiene  en su poder, puede recuperar el mensaje original  invirtiendo el *padding scheme*.

El procedimiento anterior funciona porque

 .

Esto es así porque, como hemos elegido  y  de forma que , se cumple

 .

La última congruencia se sigue directamente del teorema de Euler cuando  es coprimo con . Puede demostrarse que las ecuaciones se cumplen para todo  usando congruencias y el teorema chino del resto.

Esto muestra que se obtiene el mensaje original:

.

 Ejemplo

Aquí tenemos un ejemplo de cifrado/descifrado con RSA. Los parámetros usados aquí son pequeños y orientativos con respecto a los que maneja el algoritmo, pero podemos usar también OpenSSL para generar y examinar un par de claves reales.

La clave pública es (*e*, *n*). La clave privada es (*d*, *n*). La función de cifrado es:

Donde m es el texto sin cifrar. La función de descifrado es:

Donde c es el texto cifrado.
Para cifrar el valor del texto sin cifrar 123, nosotros calculamos:

Para descifrar el valor del texto cifrado, nosotros calculamos:

Los cálculos de potencias grandes y del módulo pueden ser eficientemente realizados por el algoritmo de multiplicación cuadrática para exponenciación modular.

 Esquemas

RSA debe ser combinado con algún esquema de relleno, ya que si no el valor de *M* puede llevar a textos cifrados inseguros.
El valor *m*=0, *m*=1 o *m*=*n*-1 siempre produce textos cifrados iguales para 0, 1 o *n*-1 respectivamente, debido a propiedades de los exponentes.
Cuando ciframos con exponentes pequeños (*e*=3) y valores pequeños de *m*, el resultado de *m* podría ser estrictamente menor que el módulo de *n*. En este caso, el texto cifrado podría ser fácilmente descifrado, tomando la raíz e-ésima del texto cifrado sin tener en cuenta el módulo.

Dado que el cifrado RSA es un algoritmo determinista (no tiene componentes aleatorios) un atacante puede lanzar con éxito un ataque de texto elegido contra el criptosistema, construyendo un diccionario de textos probables con la llave pública, y almacenando el resultado cifrado. Observando los textos cifrados en un canal de comunicación, el atacante puede usar este diccionario para descifrar el contenido del mensaje.

En la práctica, el primero de los dos problemas podría presentarse cuando enviamos pequeños mensajes ASCII donde *m* es la concatenación de uno o más carácter/es ASCII codificado/s. Un mensaje consiste en un solo carácter ASCII NUL (cuyo valor es 0) se codificaría como *m*=0, produciendo un texto cifrado de 0 sin importar qué valores de *e* y *N* son usados. Probablemente, un solo ASCII SOH (cuyo valor es 1) produciría siempre un texto cifrado de 1. Para sistemas convencionales al usar valores pequeños de *e*, como 3, un solo carácter ASCII mensaje codificado usando este esquema sería inseguro, ya que el máximo valor de *m* sería 255, y 255³ es menor que cualquier módulo razonable. De esta manera los textos sin cifrar podrían ser recuperados simplemente tomando la raíz cúbica del texto cifrado.
Para evitar estos problemas, la implementación práctica del RSA se ayuda de algunas estructuras, uso del rellenado aleatorio dentro del valor de *m* antes del cifrado. Esta técnica asegura que *m* no caerá en el rango de textos sin cifrar inseguros, y que dado un mensaje, una vez que este rellenado, cifrará uno de los números grandes de los posibles textos cifrados. La última característica es la incrementación del diccionario haciendo este intratable a la hora de realizar un ataque.

El esquema de relleno de RSA (en inglés *RSA-padding scheme*) debe ser cuidadosamente diseñado para prevenir ataques sofisticados los cuales podrían ser facilitados por la predictibilidad de la estructura del mensaje. Ejemplos de esquema de relleno usados con RSA:
RSA-OAEP (Optimal Asymetric Encryption Padding) o su versión moficada RSA-OAEP+. Este tipo de relleno es usado por ejemplo en PKCS#1 y en la red de anonimato TOR
RSA-SAEP+ (Simplified Asymmetric Encryption Padding)
RSA-REACT
RSA-PSS (Probabilistic Signature Scheme). Usado por ejemplo en PKCS#1
Algunos de estos esquemas de relleno, por ejemplo RSA-OAEP y RSA-PSS, encuentran su 'justificación' teórica en el polémico modelo de oráculo aleatorio.

 Autenticación de mensajes
RSA puede también ser usado para autenticar un mensaje. Supongamos que Alicia desea enviar un mensaje autentificado a Bob. Ella produce un valor hash del mensaje, lo eleva a la potencia de d≡ mod n (como ella hace cuando descifra mensajes), y lo adjunta al mensaje como una “firma”. Cuando Bob recibe el mensaje autentificado, utiliza el mismo algoritmo hash en conjunción con la clave pública de Alice. Eleva la firma recibida a la potencia de e≡ mod n (como hace cuando cifra mensajes), y compara el resultado hash obtenido con el valor hash del mensaje. Si ambos coinciden, él sabe que el autor del mensaje estaba en posesión de la clave secreta de Alicia, y que el mensaje no ha sido tratado de forzar (no ha sufrido ataques).

Se debe observar que la seguridad de los padding-schemes como RSA-PSS son esenciales tanto para la seguridad de la firma como para el cifrado de mensajes, y que nunca se debería usar la misma clave para propósitos de cifrado y de autentificación.

 Seguridad
La seguridad del criptosistema RSA está basado en dos problemas matemáticos: el problema de factorizar números grandes y el problema RSA. El descifrado completo de un texto cifrado con RSA es computacionalmente intratable, no se ha encontrado un algoritmo eficiente todavía para ambos problemas. Proveyendo la seguridad contra el descifrado parcial podría requerir la adición de una seguridad padding scheme.

El problema del RSA se define como la tarea de tomar raíces *e*-ésimas módulo a componer *n*: recuperando un valor *m* tal que *m**e*≡*c* (mod *n*), donde (*e*, *n*) es una clave pública RSA y c es el texto cifrado con RSA. Actualmente la aproximación para solventar el problema del RSA es el factor del módulo *n*. Con la capacidad para recuperar factores primos, un atacante puede calcular el exponente secreto *d* desde una clave pública (*e*, *n*), entonces descifra *c* usando el procedimiento estándar. Para conseguir esto, un atacante debe factorizar *n* en *p* y *q*, y calcular (*p*-1)(*q*-1) con lo que le permite determinar *d* y *e*. No se ha encontrado ningún método en tiempo polinómico para la factorización de enteros largos. Ver factorización de enteros para la discusión de este problema.

La factorización de números grandes, por lo general proponen métodos teniendo 663 bits de longitud usando métodos distribuidos avanzados. Las claves RSA son normalmente de entre 1024-2048 bits de longitud. Algunos expertos creen que las claves de 1024 bits podrían comenzar a ser débiles en poco tiempo; claves de 4096 bits podrían ser rotas en un futuro. Por lo tanto, si *n* es suficientemente grande el algoritmo RSA es seguro. Si *n* tiene 256 bits o menos, puede ser factorizado en pocas horas con un ordenador personal, usando software libre. Si *n* tiene 512 bits o menos, puede ser factorizado por varios cientos de computadoras como en 1999. Un dispositivo hardware teórico llamado TWIRL descrito por Shamir y Tromer en el 2003 cuestionó a la seguridad de claves de 1024 bits. Se recomienda actualmente que *n* sea como mínimo de 2048 bits de longitud.

En 1993, Peter Shor publicó su algoritmo, mostrando que una computadora cuántica podría en principio mejorar la factorización en tiempo polinomial, mostrando RSA como un algoritmo obsoleto. Sin embargo, las computadoras cuánticas no se esperan que acaben su desarrollo hasta dentro de muchos años.

 Consideraciones prácticas
 Generación de claves

Buscando números primos grandes *p* y *q* por el test de aleatoriedad y realizando tests probabilísticos de primalidad los cuales eliminan virtualmente todos los no-primos (eficientemente).

Los números *p* y *q* no deberían ser suficientemente cercanos para que la factorización de Fermat para *n* sea exitosa. Además, si cualquier *p*-1 o *q*-1 tiene solo factores primos pequeños, *n* puede ser factorizado rápidamente, con lo que estos valores de *p* o *q* deben ser descartados.

No se debería emplear un método de búsqueda de primos con el cual se dé alguna información cualquiera sobre los primos al atacante. En particular, se debe utilizar un buen generador aleatorio de números primos para el valor empleado. Obsérvese que el requerimiento está en que ambos sean *aleatorios* e *impredecibles*. No son el mismo criterio; un número podría haber sido elegido por un proceso aleatorio, pero si este es predecible de cualquier forma (o parcialmente predecible), el método usado resultará en una baja seguridad. Por ejemplo: la tabla de números aleatorios de Rand Corp en 1950 podría servir muy bien como ejemplo de criterio verdaderamente aleatorio, pero ha sido publicada y a esta puede acceder el atacante. Si el atacante puede conjeturar la mitad de los dígitos de *p* o *q*, él podría rápidamente calcular la otra mitad. (Ver Coppersmith en 1997).

Es importante que la clave secreta *d* sea muy grande. Wiener mostró en 1990 que si *p* está entre *q* y 2*q* (es típico) y , entonces *d* puede calcularse eficientemente a partir de *n* y *e*. Aunque valores de *e* tan bajos como 3 se han usado en el pasado, los exponentes pequeños en RSA están actualmente en desuso, por razones que incluyen el no relleno del texto sin cifrar, vulnerabilidad listada antes. 65537 es normalmente usado como valor de *e*, considerado demasiado grande para evitar ataques de exponenciación pequeños, de hecho tiene un peso de Hamming suficiente para facilitar una exponenciación eficiente.

 Velocidad
RSA es mucho más lento que DES y que otros criptosistemas simétricos. En la práctica, Bob normalmente cifra mensajes con algoritmos simétricos, cifra la clave simétrica con RSA, y transmite a ambos dicha clave (es decir la transmite cifrada con RSA) y el mensaje simétricamente cifrado a Alicia.

Esto plantea además problemas adicionales de seguridad, por ejemplo, es de gran importancia usar un generador aleatorio fuerte para claves simétricas, porque de otra forma Eve (un atacante que quiera averiguar el contenido del mensaje) podría *puentear* la clave asimétrica de RSA mediante la adivinación de la clave simétrica.

 Distribución de claves
Como con todos los cifrados, es importante cómo se distribuyan las claves públicas del RSA. La distribución de la clave debe ser segura contra un atacante que se disponga a espiar el canal para hacer un ataque de replay. Supongamos Eve (atacante) tiene alguna forma de dar a Bob arbitrariamente claves y hacerle creer que provienen de Alicia. Supongamos que Eve puede interceptar transmisiones entre Alicia y Bob. Eve envía a Bob su propia clave pública, como Bob cree que es de Alicia, Eve puede entonces interceptar cualquier texto cifrado enviado por Bob, descifrarlo con su propia clave secreta, guardar una copia del mensaje, cifrar el mensaje con la clave pública de Alicia, y enviar el nuevo texto cifrado a Alicia. En principio, ni Alicia ni Bob han detectado la presencia de Eve. Contra la defensa de ataques algunos están basados en certificados digitales u otros componentes de infraestructuras de la clave pública.

 Véase también
Clifford Cocks
Criptografía asimétrica
Competición de factorización RSA
Criptografía cuántica
Criptología
DSA
Firma digital ciega
Problema RSA
Teoría de la complejidad computacional

 Referencias
 Notas al pie

 Bibliografía
 R. Rivest, A. Shamir, L. Adleman. A Method for Obtaining Digital Signatures and Public-Key Cryptosystems. Communications of the ACM, Vol. 21 (2), pp.120–126. 1978. Previously released as an MIT "Technical Memo" in April 1977. Initial publication of the *RSA* scheme.
 Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. *Introduction to Algorithms*, Second Edition. MIT Press and McGraw-Hill, 2001. ISBN 0-262-03293-7. Section 31.7: The RSA public-key cryptosystem, pp.881–887.
 Wing H. Wong. Timing Attacks on RSA: Revealing Your Secrets through the Fourth Dimensión
 An Attack on RSA Digital Signature
 Behrends,Ehrhard

 Enlaces externos
 Algoritmo RSA
 Ataques RSA I
  PKCS #1: RSA Cryptography Standard (Sitio oficial de RSA Laboratories )
  A Method for Obtaining Digital Signatures and Public-Key Cryptosystems, El documento de la revista Communications of the ACM, Vol. 21 (2), 1978, páginas 120--126 escrita por R. Rivest, A. Shamir y L. Adleman, Posterior al "Technical Memo" de abril de 1977.
 Calculadora en línea de cifrado RSA que muestra paso a paso todos los cálculos
 «No, no se ha encontrado una vulnerabilidad en RSA que permite atacar uno de cada 172 certificados» por Sergio De Los Santos  | Blog de Telefónica.
