---
type: Artículo de enciclopedia
title: Criptografía asimétrica
description: "La criptografía asimétrica (del inglés ), también llamada criptografía de clave pública , es un sistema criptográfico basado en el uso de un par de claves matemáticamente relacionadas: una clave pública, que puede …"
resource: https://es.wikipedia.org/wiki/Criptografía_asimétrica
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_asimétrica"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_asimétrica
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía asimétrica

La **criptografía asimétrica** (del inglés ), también llamada **criptografía de clave pública** , es un sistema criptográfico basado en el uso de un par de claves matemáticamente relacionadas: una clave pública, que puede difundirse sin restricciones, y una clave privada, que debe mantenerse en secreto.

En este esquema, la clave pública puede compartirse libremente y se utiliza habitualmente para el cifrado de datos o la verificación de firmas digitales, mientras que la clave privada se mantiene en secreto y se emplea para el descifrado o la generación de firmas. El destinatario de una comunicación genera ambas claves y distribuye únicamente la clave pública, de modo que cualquier emisor pueda cifrar un mensaje dirigido a él. Dicho mensaje solo podrá ser descifrado por el destinatario mediante su clave privada, lo que garantiza la confidencialidad incluso si la comunicación es interceptada. La solidez de este sistema se basa en algoritmos matemáticos que generan pares de claves únicos, con una probabilidad extremadamente baja de que dos usuarios distintos obtengan por azar la misma combinación.

Si una persona que emite un mensaje a un destinatario, usa la clave pública de este último para cifrarlo; una vez cifrado, solo la clave privada del destinatario podrá descifrar el mensaje, ya que es el único que debería conocerla. Por tanto, se logra la *confidencialidad* del envío del mensaje, ya que es extremadamente difícil que lo descifre alguien salvo el destinatario. Cualquiera, usando la llave pública del destinatario, puede cifrarle mensajes; los que serán descifrados por el destinatario usando su clave privada.

Si el propietario del par de claves usa su clave privada para cifrar un mensaje, cualquiera puede descifrarlo utilizando la clave pública del primero. En este caso se consigue la *identificación* y *autentificación* del remitente, ya que se sabe que solo pudo haber sido él quien empleó su clave privada (salvo que un tercero la haya obtenido). Esta idea es el fundamento de la firma digital, donde jurídicamente existe la presunción de que el firmante es efectivamente el dueño de la clave privada.

Los sistemas de cifrado de clave pública se inventaron con el fin de evitar por completo el problema del intercambio de claves de los sistemas de cifrado simétricos. Con las claves públicas no es necesario que el remitente y el destinatario se pongan de acuerdo en la clave a emplear. Todo lo que se requiere es que, antes de iniciar la comunicación secreta, cada uno debe conseguir la llave pública del otro y cuidar cada uno su llave privada. Es más, esas mismas claves públicas pueden ser usadas por cualquiera que desee comunicarse con alguno de ellos siempre que se utilice correctamente la llave pública de cada uno.

La criptografía asimétrica usa funciones exponenciales.

 Descripción

Las dos principales ramas de la criptografía de clave pública son:

 Cifrado de clave pública: un mensaje cifrado con la clave pública de un destinatario no puede ser descifrado por nadie (incluyendo al que lo cifró), excepto un poseedor de la clave privada correspondiente, presumiblemente su propietario y la persona asociada con la clave pública utilizada. Su función es garantizar la confidencialidad del mensaje.
 Firmas digitales: un mensaje firmado con la clave privada del remitente puede ser verificado por cualquier persona que tenga acceso a la clave pública de dicho remitente, lo que demuestra que este remitente tenía acceso a la clave privada (y por lo tanto, es probable que sea la persona asociada con la clave privada utilizada). Se asegura así que el mensaje no ha sido alterado, puesto que cualquier manipulación del mensaje repercutiría en un distinto resultado del algoritmo de resumen del mensaje (encoded message digest). Se utiliza para garantizar la autenticidad del mensaje.

Una analogía con el cifrado de clave pública es la de un buzón con una ranura de correo. La ranura de correo está expuesta y accesible al público; su ubicación (la dirección de la calle) es, en esencia, la clave pública. Alguien que conozca la dirección de la calle puede ir a la puerta y colocar un mensaje escrito a través de la ranura; sin embargo, solo la persona que posee la llave (clave privada) puede abrir el buzón de correo y leer el mensaje.

Una analogía para firmas digitales es el sellado de un sobre con un sello personal. El mensaje puede ser abierto por cualquier persona, pero la presencia del sello autentifica al remitente.

 Ejemplo
Supongamos que Ana quiere enviar a David un mensaje secreto que solo él pueda leer.

Primero, David envía a Ana una caja abierta, pero con cerradura, cerradura que se bloqueará una vez se cierre la caja, y que solo podrá abrirse con una llave, que solo David tiene. Ana recibe la caja, escribe el mensaje, lo pone en la caja y la cierra con su cerradura (ahora Ana ya no podrá abrir la caja para acceder de nuevo al mensaje). Finalmente, Ana envía la caja a David y este la abre con su llave. En este ejemplo, la caja con la cerradura es la «clave pública» de David, y la llave de la cerradura es su «clave privada».

Esquemáticamente:

"Caja" y "cerradura" son variables, dos datos (en el caso más sencillo, dos números) necesarios ambos para resolver un determinado problema matemático de manera *inmediata*. Es cierto que teniendo solo la "cerradura" (alguien que interceptase la caja antes de que llegue a David), un cerrajero experto podría abrir la caja sin necesidad de la "llave", pero, en la práctica, un sistema de cifrado competente exhibe una complejidad tal que su resolución, desconociendo la clave privada del destinatario, exige de una potencia computacional o de un coste en tiempo desproporcionadamente mayor al valor esperado del robo de la información (la computación cuántica, por ejemplo, reduciría en mucho dicho coste, volviendo obsoletos no pocos sistemas criptográficos que actualmente pueden considerarse efectivamente invulnerables).

Esquemas para la propagación de la confianza

Observar que la criptografía de clave pública necesita establecer una confianza en que la clave pública de un usuario (al cual se identifica por una cadena identificativa a la que se llama identidad) es correcta, es decir el único que posee la clave privada correspondiente es el usuario auténtico al que pertenece. Cuanto más fiable sea el método más seguridad tendrá el sistema.

Lo ideal sería que cada usuario comunicara (e idealmente probara) de forma directa al resto de usuarios cuál es su clave pública. Sin embargo esto no es posible en la realidad y se desarrollan distintos esquemas para aportar confianza. Estos esquemas se pueden agrupar en dos tipos: Esquema centralizados y esquemas descentralizados. En los esquemas descentralizado hay varios nodos y cada uno tiene unas capacidades y derechos. En los esquemas centralizados hay una arquitectura cliente-servidor donde los servidores juegan un papel central y proveen servicios a los clientes. Cada esquema tiene sus ventajas e inconvenientes. Por ejemplo, los sistemas centralizados suelen ser más vulnerables a ataques de denegación de servicio debido a que basta con que falle el servidor central para que el sistema de confianza caiga por completo. Los sistemas descentralizados se suelen considerar menos seguros contrataques encaminados a publicar claves públicas falsas debido a que al haber varios nodos posibles a atacar es más difícil asegurar su seguridad. Los modelos más usados son:

 Uso de una infraestructura de clave pública (, PKI). En este modelo hay una o varias entidades emisoras de certificados, o autoridades de certificación (, CA) que aseguran la autenticidad de la clave pública y de ciertos atributos del usuario. Para ello, firman con su clave privada ciertos atributos del usuario incluyendo su clave pública generando lo que se llama certificado del usuario.
 Establecimiento de una red de confianza. No hay nodos aparte de los usuarios. Los usuarios recogen claves públicas de otros usuarios y aseguran su autenticidad si están seguros de que la clave privada correspondiente pertenece en exclusiva a ese usuario. Un usuario además puede directamente confiar en el conjunto de claves públicas en las que otro confía ya sea directamente o a través de otras relaciones de confianza. En cada caso es el propio usuario el que decide el conjunto de claves públicas en las que confía y su grado de fiabilidad. Dos usuarios que no se conocen pueden confiar en sus claves públicas si existe una cadena de confianza que enlace ambas partes. Este tipo de implementación de la confianza es el que usa por ejemplo PGP.
 Uso de criptografía basada en identidad. En este modelo existe un generador de claves privadas (, PKG) que a partir de una cadena de identificación del usuario genera una clave privada y otra pública para ese usuario. La pública la difunde para que el resto de usuarios la sepan y la privada es comunicada en exclusiva al usuario a quien pertenece.
 Uso de criptografía basada en certificados. En este modelo el usuario posee una clave privada y otra pública. La clave pública la envía a una Autoridad de certificación que basándose en criptografía basada en identidad genera un certificado que asegura la validez de los datos.
 Uso de criptografía sin certificados. Este modelo es similar al modelo que usa criptografía basada en identidad pero con la diferencia de que lo que se genera en el centro generador de claves (, KGC) es una clave parcial. La clave privada completa se genera a partir de la clave privada parcial y un valor generado aleatoriamente por el usuario. La clave pública es generada también por el usuario a partir de parámetros públicos del KGC y el valor secreto escogido.

Girault distingue tres niveles de confianza que dan los distintos modelos a la autoridad que interviene en el proceso (PKG, KGC o CA según cada caso):

 Nivel 1: La autoridad puede calcular claves secretas de usuarios, y por tanto pueden hacerse pasar como cualquier usuario sin ser detectado. Las firmas basadas en identidad pertenecen a este nivel de confianza.
 Nivel 2: La autoridad no puede calcular claves secretas de usuarios, pero puede todavía hacerse pasar como cualquier usuario sin ser detectado. Firmas sin certificados pertenecen a este nivel.
 Nivel 3: La autoridad no puede calcular claves secretas de usuarios, y tampoco puede hacerse pasar como un usuario sin ser detectado. Es el nivel más alto de fiabilidad. Las firmas tradicionales PKI y la firmas basadas en certificados pertenecen a este nivel.

 Seguridad
Según el segundo principio de Kerckhoffs toda la seguridad debe descansar en la clave y no en el algoritmo (en contraposición con la seguridad por la oscuridad). Por lo tanto, el tamaño de la clave es una medida de la seguridad del sistema, pero no se puede comparar el tamaño de la clave del cifrado simétrico con el del cifrado de clave pública para medir la seguridad. En un ataque de fuerza bruta sobre un cifrado simétrico con una clave del tamaño de 80 bits, el atacante debe probar hasta 280-1 claves para encontrar la clave correcta. En un ataque de fuerza bruta sobre un cifrado de clave pública con una clave del tamaño de 512 bits, el atacante debe factorizar un número compuesto codificado en 512 bits (hasta 155 dígitos decimales). La cantidad de trabajo para el atacante será diferente dependiendo del cifrado que esté atacando. Mientras 128 bits son suficientes para cifrados simétricos, dada la tecnología de factorización de hoy en día, se recomienda el uso de claves públicas de 1024 bits para la mayoría de los casos.

 Ventajas y desventajas del cifrado asimétrico
La mayor ventaja de la criptografía asimétrica es que la distribución de claves es más fácil y segura ya que la clave que se distribuye es la pública manteniéndose la privada para el uso exclusivo del propietario, pero este sistema tiene bastantes desventajas:

 Para una misma longitud de clave y mensaje se necesita mayor tiempo de proceso.
 Las claves deben ser de mayor tamaño que las simétricas (generalmente son cinco o más veces de mayor tamaño que las claves simétricas).
 El mensaje cifrado ocupa más espacio que el original.

Ventajas:

 Tiene una alta seguridad puesto que el sistema y que es una llave para cifrar y otra para descifrar
 Ofrece un alto nivel de confidencialidad, integridad y garantiza la no alteración del mensaje

Los nuevos sistemas de clave asimétrica basado en curvas elípticas tienen características menos costosas.

Herramientas como PGP, SSH o la capa de seguridad SSL para la jerarquía de protocolos TCP/IP utilizan un híbrido formado por la criptografía asimétrica para intercambiar claves de criptografía simétrica, y la criptografía simétrica para la transmisión de la información.

 Tecnologías
Algunos algoritmos y tecnologías de clave asimétrica son:
 Diffie-Hellman
 RSA
 DSA
 Cifrado ElGamal
 Criptografía de curva elíptica
 Criptosistema de Merkle-Hellman
 Goldwasser-Micali
 Goldwasser-Micali-Rivest
 Cifrado extremo a extremo

 Protocolos
Algunos protocolos que usan los algoritmos antes citados son:
 DSS ("Digital Signature Standard") con el algoritmo DSA ("Digital Signature Algorithm")
 PGP o Pretty Good Privacy
 GPG, una implementación de OpenPGP
 SSH o Secure Shell
 Secure Sockets Layer o SSL, ahora un estándar del Grupo de Trabajo de Ingeniería de Internet
 Transport Layer Security o TLS

 Referencias

 Bibliografía complementaria
 Attrapadung, Nuttapong; Herranz, Javier; Laguillaumie, Fabien; Libert, Benoît; de Panafieu, Elie; Ràfols, Carla (2012-03). "Attribute-based encryption schemes with constant-size ciphertexts". *Theoretical Computer Science,*422, pp.15–38. doi:10.1016/j.tcs.2011.12.004.
Herranz, Javier; Laguillaumie, Fabien; Ràfols, Carla (2010), Nguyen, Phong Q.; Pointcheval, David (eds.), "Constant Size Ciphertexts in Threshold Attribute-Based Encryption", *Public Key Cryptography – PKC 2010*, Springer Berlin Heidelberg, 6056, pp. 19–34, doi:10.1007/978-3-642-13013-7_2, , retrieved 2020-05-13

 Enlaces externos
 Texto adaptado de la Guía de "Gnu Privacy Guard"
