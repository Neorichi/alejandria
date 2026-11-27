---
type: Artículo de enciclopedia
title: Criptografía
description: "La criptografía (del griego κρυπτός (kryptós), «secreto», y γραφή (graphé), «grafo» o «escritura», literalmente «escritura secreta») se ha definido, tradicionalmente, como el ámbito de la criptología que se ocupa de las …"
resource: https://es.wikipedia.org/wiki/Criptografía
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía"}
license: CC BY-SA 4.0
id: eswiki-Criptografía
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía

La **criptografía** (del griego κρυπτός (kryptós), «secreto», y γραφή (graphé), «grafo» o «escritura», literalmente «escritura secreta») se ha definido, tradicionalmente, como el ámbito de la criptología que se ocupa de las técnicas de cifrado o codificado destinadas a alterar las representaciones lingüísticas de ciertos mensajes con el fin de hacerlos incomprensibles a receptores no autorizados. Estas técnicas se utilizan tanto en el arte como en la ciencia y en la tecnología. Por tanto, el único objetivo de la criptografía era conseguir la confidencialidad de los mensajes, para lo cual se diseñaban sistemas de cifrado y códigos, y la única criptografía existente era la llamada criptografía clásica, donde se ocultaba tanto el algoritmo como la clave criptográfica.

La aparición de la informática y el uso masivo de las comunicaciones digitales, han producido un número creciente de problemas de seguridad. Las transacciones que se realizan a través de la red pueden ser interceptadas, y por tanto, la seguridad de esta información debe garantizarse. Este desafío ha generalizado los objetivos de la criptografía para ser la parte de la criptología que se encarga del estudio de los algoritmos, protocolos (se les llama protocolos criptográficos), y sistemas que se utilizan para proteger la información y dotar de seguridad a las comunicaciones y a las entidades que se comunican.

Para ello los criptógrafos investigan, desarrollan y aprovechan técnicas matemáticas que les sirven como herramientas para conseguir sus objetivos. Los grandes avances producidos en el mundo de la criptografía han sido posibles gracias a la evolución que se ha producido en el campo de la matemática e informática.

 Objetivos
La criptografía actualmente se encarga del estudio de los algoritmos, protocolos y sistemas que se utilizan para dotar de seguridad a las comunicaciones, a la información y a las entidades que se comunican. El objetivo de la criptografía es diseñar, implementar, implantar, y hacer uso de sistemas criptográficos para dotar de alguna forma de seguridad. Por tanto el tipo de propiedades de las que se ocupa la criptografía son, por ejemplo:
 Confidencialidad. Es decir, garantiza que la información sea accesible únicamente a personal autorizado. Para conseguirlo utiliza códigos y técnicas de cifrado.
 Integridad. Es decir garantiza la corrección y completitud de la información. Para conseguirlo puede usar por ejemplo funciones hash criptográficas MDC, protocolos de compromiso de bit, o protocolos de notarización electrónica.
 Vinculación. Permite vincular un documento o transacción a una persona o un sistema de gestión criptográfico automatizado. Cuando se trata de una persona, se trata de asegurar su conformidad respecto a esta vinculación (content commitment) de forma que pueda entenderse que la vinculación gestionada incluye el entendimiento de sus implicaciones por la persona. Antiguamente se utilizaba el término "No repudio", que está abandonándose, ya que implica conceptos jurídicos que la tecnología por sí sola no puede resolver. En relación con dicho término se entendía que se proporcionaba protección frente a que alguna de las entidades implicadas en la comunicación no pudiera negar haber participado en toda o parte de la comunicación. Para conseguirlo se puede usar por ejemplo firma digital. En algunos contextos lo que se intenta es justo lo contrario: Poder negar que se ha intervenido en la comunicación. Por ejemplo cuando se usa un servicio de mensajería instantánea y no queremos que se pueda demostrar esa comunicación. Para ello se usan técnicas como el cifrado negable.
 Autenticación. Es decir proporciona mecanismos que permiten verificar la identidad del comunicador. Para conseguirlo puede usar por ejemplo función hash criptográfica MAC o protocolo de conocimiento cero.
 Soluciones a problemas de la falta de simultaneidad en la telefirma digital de contratos. Para conseguirlo puede usar por ejemplo protocolos de transferencia inconsciente.

Un sistema criptográfico es seguro respecto a una tarea si un adversario con capacidades especiales no puede romper esa seguridad, es decir, el atacante no puede realizar esa tarea específica.

 Terminología
En el campo de la criptografía muchas veces se agrupan conjuntos de funcionalidades que tienen alguna característica común y a ese conjunto lo denominan 'Criptografía de' la característica que comparten. Veamos algunos ejemplos:
 Criptografía simétrica.- Agrupa aquellas funcionalidades criptográficas que se apoyan en el uso de una sola clave para cifrar y descifrar la información. Es eficiente pero requiere compartir la clave de forma segura.
 Criptografía asimétrica.- Agrupa aquellas funcionalidades criptográficas que se apoyan en el uso de parejas de claves compuesta por una clave pública, que sirve para cifrar, y por una clave privada, que sirve para descifrar. Permite la autenticación y el intercambio seguro de información sin necesidad de compartir claves.
 Criptografía con umbral.- Agrupa aquellas funcionalidades criptográficas que se apoyan en el uso de un umbral de participantes a partir del cual se puede realizar la acción.
 Criptografía basada en identidad.- Es un tipo de Criptografía asimétrica que se basa en el uso de identidades.
 Criptografía basada en certificados.- Esta técnica utiliza certificados digitales para verificar la autenticidad de las claves públicas.
 Criptografía sin certificados.- En contraste con la anterior, esta técnica no hace uso de certificados digitales para la verificación.
 Criptografía de clave aislada.- Esta técnica implica el uso de una clave específica y aislada para realizar operaciones criptográficas.

 Evaluación de la seguridad de un sistema criptográfico
El objetivo de un sistema criptográfico es dotar de seguridad. Por tanto para calibrar la calidad de un sistema criptográfico es necesario evaluar la seguridad que aporta dicho sistema.

 ¿Hacer público o no?
Para poder evaluar mejor la seguridad de un sistema criptográfico, además de las verificaciones internas de seguridad que la organización haga, se puede considerar hacer público a todo el mundo los entresijos del sistema. Sin embargo, al hacer pública esa información se facilita el que alguien pueda descubrir alguna debilidad y la aproveche o incluso la haga pública para que otros la puedan utilizar. Cuanta más información se publique más fácil será encontrar debilidades tanto para buenos objetivos (mejorar el producto) como para malos (realizar ataques). En resumen cuanta más información se publique más personas podrán evaluar la seguridad y se podrán corregir las debilidades que se encuentren, pero también aumenta la exposición a ataques. En función de las decisiones que se tomen se establecerá una política de revelación.

Se considera que la seguridad de un sistema criptográfico debe descansar sobre el tamaño de las claves utilizadas y no sobre el secreto del algoritmo. Esta consideración se formaliza en el llamado principio de Kerckhoffs. Esto no quiere decir que cuando usemos criptografía tengamos que revelar los algoritmos, lo que quiere decir es que el algoritmo tiene que ser seguro aunque este sea difundido. Evidentemente si un sistema criptográfico es seguro aun revelando su algoritmo, entonces será aún más seguro si no lo revelamos.

A la política de revelación de no publicar ninguna información para que ningún atacante encuentre debilidades se le llama de no revelación y sigue una estrategia de seguridad por oscuridad. A la política de revelación de revelar toda la información se le llama revelación total. Entre ambos tipos de política de revelación hay estrategias intermedias, llamadas "de revelación parcial".

 Formas de romper la seguridad

Hay básicamente tres formas de romper la seguridad de un sistema criptográfico

 **Atacar la criptografía subyacente**. Es lo que sería un ataque teórico a los mecanismos criptográficos usados.
 **Atacar la implementación concreta**. La criptografía puede ser implementada en software o hardware. Es bastante probable que las implementaciones concretas tengan vulnerabilidades que se pueden aprovechar. También las vulnerabilidades se podrían introducir de forma deliberada y de esta forma proporcionar puertas traseras disponibles para ser utilizadas.
 **Ingeniería social**. Muchas veces en los sistemas criptográficas hay personas o entidades que tienen privilegios especiales. Presionando a estas personas o entidades para que nos den acceso a recursos o a información privilegiada, podríamos vulnerar la seguridad del sistema.

Las personas o entidades interesadas en romper la seguridad de este tipo de sistemas tienen en cuenta todos estos frentes. Por ejemplo las informaciones de Edward Snowden revelan que el programa Bullrun adopta estos tres tipos de estrategias.

 Grados de seguridad teórica
Cuando se evalúa la seguridad de un sistema criptográfico se puede calibrar la seguridad que aporta en función de si este es seguro de forma incondicional o si es seguro solo si se cumplen ciertas condiciones.

 Seguridad incondicional
Se dice que un sistema criptográfico tiene una seguridad incondicional sobre cierta tarea si un atacante no puede resolver la tarea aunque tenga infinito poder computacional. En función de la tarea sobre la que se dice que el sistema criptográfico es incondicionalmente seguro, podemos hablar por ejemplo de:

 criptosistemas incondicionalmente seguros (cifrado)
 autenticación incondicionalmente segura (autenticación)
 distribución de claves incondicionalmente segura
 firma digital incondicionalmente segura (firma digital)

Es habitual que los sistemas incondicionalmente seguros tengan inconvenientes importantes como por ejemplo en la longitud de las claves (libreta de un solo uso).

Para certificar una seguridad incondicional los criptólogos se suelen basar en la teoría de la información y, por tanto, en la teoría de la probabilidad.

 Limitaciones
El que un sistema tenga seguridad incondicional no quiere decir que su seguridad sea inviolable. Veamos dos consideraciones:

Los sistemas son incondicionalmente seguros desde un punto de vista probabilístico: El oponente siempre tiene una probabilidad mayor que cero de romper la seguridad. Sin embargo, esta probabilidad puede ser muy pequeña. Esto es lo que sucede con los sistemas incondicionalmente seguros.
 En la mayoría de los estudios sobre la seguridad de un sistema se hace la suposición de que los atacantes tienen solo un intento para atacar la seguridad del sistema. El éxito o el fracaso están determinados por el éxito o fracaso de ese intento. Esta suposición es válida, por ejemplo, en ciertos problemas de comunicación segura donde el enemigo no tiene oportunidad de verificar si el mensaje estimado es correcto o no. Sin embargo hay otros tipos de problemas donde esta suposición no tiene sentido. Por ejemplo, en un sistema de autenticación con usuario y contraseña para entrar en una cuenta restringida, el atacante puede realizar varios intentos. Además, en algunos casos, los intentos fallidos anteriores dan información para hacer una estimación mejor para los intentos siguientes.
Cuando se dice que un sistema criptográfico es incondicionalmente seguro, se hace referencia al nivel teórico. Sin embargo cuando es implementado en la práctica puede no mantenerse esa seguridad. Hay muchos tipos de ataques que solo se aplican cuando los sistemas están implementados en un sistema concreto.Ejemplos:
 Explotación de esteganografía o canal encubierto. Son canales de comunicación no intencionados y de difícil detección, que permiten la transferencia de información de forma que viola la política de seguridad del sistema. En un computador real los procesos al ejecutarse producen una serie de efectos y fenómenos que pueden ser medidos y explotados para revelar información relevante que puede ser utilizada para romper el sistema (por ejemplo, pistas sobre la clave). Este problema es inherente y no puede ser evitado mediante técnicas criptográficas. Son ejemplos típicos de este tipo de canales los canales ocultos generados por análisis de temporizaciones, por análisis de consumos de energía o por análisis de consumos de radiaciones electromagnéticas o por análisis de consumo de espacio de almacenamiento.
 Malos diseños o implementaciones del software o el hardware pueden hacer que la solución práctica sea insegura.
Ejemplos de ataques que se aprovechan de vulnerabilidades producidas por una mala elicitación o análisis de requisitos, diseño, desarrollo, implementación o pruebas del producto software o hardware: desbordamiento de buffer, Inyección SQL, Cross Site Scripting, ataque informático basado en deficiencias del hardware.

 Seguridad condicional
 Se dice que un sistema criptográfico tiene una seguridad condicional sobre cierta tarea si un atacante puede teóricamente resolver la tarea, pero no es computacionalmente factible para él (debido a sus recursos, capacidades y acceso a información).

Hay un tipo especial de seguridad condicional, llamada seguridad demostrable. La idea es mostrar que romper un sistema criptográfico es computacionalmente equivalente a resolver un problema matemático considerado como difícil. Esto es, que se cumplen las dos siguientes sentencias:

 Si el problema difícil puede ser resuelto, entonces el sistema criptográfico puede romperse.
 Si el sistema criptográfico puede ser roto, entonces el problema difícil puede resolverse.

La seguridad demostrable es difícil de lograr para sistemas criptográficos complejos. Se ha desarrollado una metodología (modelo de oráculo aleatorio) para diseñar sistemas que no tienen realmente una seguridad demostrable, pero que dan unas *buenas sensaciones* respecto a su seguridad. La idea básica es diseñar un sistema ideal que usa una o varias funciones aleatorias, también conocidas como oráculos aleatorios; y probar la seguridad de este sistema matemático. A continuación el sistema ideal es implementado en un sistema real reemplazando cada oráculo aleatorio con una buena y adecuada función pseudoaleatoria conocida generalmente un código de detección de manipulaciones como SHA-1 o MD5. Si las funciones pseudoaleatorias utilizadas tiene buenas propiedades, entonces uno puede esperar que la seguridad probada del sistema ideal sea heredada por el sistema real. Observar que esto ya no es una prueba, sino una evidencia sobre la seguridad del sistema real. Se ha demostrado que esta evidencia no siempre es cierta y que es posible romper sistemas criptográficos cuya seguridad se apoya en el modelo de oráculo aleatorio.

 Puntos de vista desde los que evaluar la seguridad
Para evaluar la seguridad de un esquema criptográfico se suelen usar tres enfoques principales. Cada enfoque difiere de las suposiciones acerca de las capacidades de los oponentes criptoanalistas. El primer método está basado en la teoría de la información, y ofrece una seguridad incondicional y por tanto una seguridad independiente del poder de computación de los adversarios. El enfoque basado en la teoría de la complejidad comienza a partir de un modelo abstracto para la computación, y asume que el oponente tienen un poder limitado de computación. El tercer enfoque intenta producir soluciones prácticas. Para ello estima la seguridad basándose en el mejor algoritmo conocido para romper el sistema y estima de forma realista el poder necesario de computación o de hardware para romper el algoritmo. A este enfoque se le suele llamar enfoque basado en la práctica.

 Enfoque basado en la teoría de la información
En este enfoque se evalúa la seguridad del sistema utilizando las herramientas que proporciona la teoría de la información. Permite declarar sistemas incondicionalmente seguros, es decir, sistemas seguros independientemente del poder de computación del atacante.

La teoría de la información proporciona valiosas herramientas para analizar la seguridad de los sistemas criptográficos. Por ejemplo está la entropía, distancia de unicidad, el concepto de secreto perfecto, etcétera.

 Enfoque basado en la teoría de la complejidad
En este enfoque se evalúa la seguridad de los sistemas criptográficos en función de la cantidad de trabajo computacional requerido para romperlo. Para estimar esa cantidad de trabajo se estudia la complejidad computacional de los mejores métodos conocidos hasta ahora para realizar esa tarea. En función de los resultados de este estudio y del poder computacional límite estimado para el atacante, se decide si esa cantidad de trabajo es realizable por un atacante. Si ese trabajo no es realizable se dice que el sistema es seguro desde un punto de vista computacional (seguridad computacional).

Este tipo de enfoque para evaluar la seguridad es muy usado en la criptografía asimétrica. En concreto, la seguridad de muchos de los algoritmos de la criptografía asimétrica están basados en el análisis de complejidad de los métodos conocidos para el cálculo de factorización de enteros y del logaritmo discreto.

Por definición, el tipo de seguridad que aporta este tipo de enfoque es una seguridad condicional basada en los métodos de resolución de problemas evaluados. En este punto hay que tener en cuenta dos consideraciones:

 Actualmente no se pueden considerar como buenos los algoritmos que se usan para estimar la complejidad de la resolución de los problemas. Se considera que hay algoritmos mucho mejores. Especialmente en el campo de la criptografía. Por tanto las estimaciones sobre el poder de computación necesario para romper el sistema no se consideran fiables.
 Se ha demostrado que algunos de los problemas (por ejemplo, factorización de enteros y el logaritmo discreto) en los que se sustenta la seguridad (computacional) de muchos algoritmos, pueden resolverse con algoritmos con una complejidad computacional de peor calidad usando computadores cuánticos. Si alguien pudiera disponer de un computador cuántico muchos de los sistemas criptográficos que se consideran seguros (con seguridad condicional) habría que catalogarlos como inseguros.

 Enfoque basado en la práctica
El objetivo de este enfoque es producir soluciones prácticas a partir del estudio de sistemas concretos y de la experiencia acumulada. Es un enfoque de prueba-error donde se proponen soluciones basándose en la experiencia y luego se somete esa solución a un proceso intensivo en el que se intenta romper su seguridad. A partir de este enfoque se han hecho importantes avances en conseguir sistemas robustos ya que los criptógrafos diseñan ataques y posteriormente adaptan los sistemas para anular dichos ataques. Por ejemplo, de esta forma se han conseguido importantes avances en la seguridad frente a ataques basados en estudios estadísticos y ataques meet in the middle.

Es frecuente, en este tipo de enfoque, diseñar bloques con ciertas propiedades demostradas estableciendo una biblioteca de bloques disponibles. Ejemplos de propiedades buenas para este tipo de bloques pueden ser: buenas propiedades estadísticas, buenas propiedades para la confusión y difusión, o de no linealidad. Posteriormente estos bloques se ensamblan para la construcción de sistemas criptográficos que aprovechan sus propiedades para dotar de mayor seguridad.

Este enfoque permite llegar a establecer sistemas que tienen seguridad condicional. Este tipo de sistemas tienen una seguridad computacional.

 Historia

La historia de la criptografía es extensa y rica en anécdotas. Desde las primeras civilizaciones se desarrollaron técnicas para transmitir mensajes durante campañas militares, de modo que, si el mensajero era interceptado, la información no cayera en manos del enemigo.

Uno de los primeros métodos criptográficos conocidos data del  y se denomina Escítala. Consistía en un método de trasposición basado en un cilindro que actuaba como clave: el mensaje se enrollaba alrededor de él para cifrarlo y descifrarlo. El segundo criptosistema documentado fue descrito por el historiador griego Polibio, quien propuso un sistema de sustitución basado en la posición de las letras dentro de una tabla. Los romanos también emplearon sistemas de sustitución, siendo el más célebre el conocido como Cifrado César, atribuido tradicionalmente a Julio César por su supuesto uso en campañas militares. Según algunos autores, en realidad César no empleaba este método; sin embargo, la atribución ha sido tan persistente que el nombre ha quedado fijado en la historia.

En 1465, el italiano Leon Battista Alberti inventó un sistema de sustitución polialfabética que supuso un avance significativo para su época. Otro criptógrafo destacado del  fue el francés Blaise de Vigenère, quien escribió un importante tratado sobre la «escritura secreta» y diseñó una cifra que ha llegado hasta nuestros días asociada a su nombre. A Selenus se le atribuye la obra criptográfica *Cryptomenytices et Cryptographiae* (Luneburgo, 1624). En ese mismo siglo, María Estuardo, reina de Escocia, fue ejecutada por orden de su prima Isabel I, reina de Inglaterra, tras descubrirse un complot gracias a un exitoso criptoanálisis realizado por los matemáticos al servicio de Isabel.

Durante los siglos ,  y , el interés de los monarcas por la criptografía fue notable. Las tropas de Felipe II utilizaron durante largo tiempo una cifra basada en un alfabeto de más de 500 símbolos, considerada inexpugnable por los matemáticos de la corte española. Sin embargo, el matemático francés François Viète logró criptoanalizar dicho sistema para el rey de Francia, Enrique IV. Este hecho provocó una queja formal de la corte española ante el papa Pío V, acusando a Enrique IV de emplear magia negra para derrotar a sus ejércitos.

Durante la Primera Guerra Mundial, los alemanes utilizaron el cifrado ADFGVX, un método similar al tablero de Polibio. Este sistema empleaba una matriz de 6 × 6 para sustituir las letras del alfabeto y los dígitos del 0 al 9 por pares de letras tomadas del conjunto A, D, F, G, V y X, que da nombre al cifrado.

 Desde el  y hasta la Segunda Guerra Mundial, destacaron figuras como el neerlandés Auguste Kerckhoffs y el prusiano Friedrich Kasiski. No obstante, fue en el  cuando la criptografía experimentó avances decisivos, especialmente durante las dos grandes contiendas bélicas del siglo: la Gran Guerra y la Segunda Guerra Mundial. A partir de este periodo, la criptografía incorporó una nueva herramienta fundamental: las máquinas de cálculo, que permitieron desarrollar cifras más complejas y seguras.

La máquina de cifrado más conocida de esta etapa fue la alemana Enigma, un sistema de rotores que automatizaba en gran medida los cálculos necesarios para el cifrado y descifrado de mensajes. Para contrarrestar este dispositivo, fue necesario recurrir a algunos de los mejores matemáticos de la época y realizar un enorme esfuerzo computacional. No en vano, los mayores avances tanto en criptografía como en criptoanálisis se produjeron a partir de entonces.

 Tras la conclusión de la Segunda Guerra Mundial, la criptografía experimentó un importante desarrollo teórico. En este contexto, las investigaciones de Claude Shannon en el campo de la teoría de la información constituyeron hitos fundamentales. Paralelamente, los avances en computación automática representaron tanto una amenaza para los sistemas criptográficos existentes como una oportunidad para el diseño de nuevos métodos.

A mediados de la década de 1970, el Departamento de Normas y Estándares de los Estados Unidos publicó el primer diseño lógico de un cifrador que llegaría a convertirse en el principal sistema criptográfico de finales del : el Estándar de Cifrado de Datos o DES. En esas mismas fechas comenzó a gestarse la que hasta ahora ha sido la última gran revolución de la criptografía teórica y práctica: los sistemas criptográficos asimétricos. Estos supusieron un salto cualitativo decisivo, al permitir la aplicación de la criptografía en ámbitos hoy esenciales, como el de la firma digital.

 La criptografía en el correo electrónico
La mayor parte de los mensajes de correo electrónico que se transmiten por Internet no incorporan mecanismos de seguridad de extremo a extremo. Aunque muchos servidores utilizan cifrado en tránsito (por ejemplo, TLS), el contenido del mensaje puede ser accesible para terceros con acceso a los servidores intermedios, proveedores de correo o mediante ataques de interceptación maliciosa.

Para mitigar estos riesgos, la criptografía se aplica al correo electrónico mediante sistemas de cifrado y firma digital. Entre los más utilizados se encuentran PGP/OpenPGP y S/MIME, los cuales se basan en criptografía de clave pública. En estos sistemas, cada usuario dispone de un par de claves: una clave pública, que puede compartirse libremente, y una clave privada, que debe mantenerse en secreto.

El uso de certificados digitales o claves públicas en el envío de correos electrónicos ofrece varias ventajas fundamentales. En primer lugar, garantiza la confidencialidad, ya que el contenido del mensaje se cifra y solo puede ser leído por el destinatario que posea la clave privada correspondiente. En segundo lugar, permite la autenticación del remitente, proporcionando la certeza de que quien envía el mensaje es realmente quien dice ser. Además, la integridad del mensaje queda protegida, asegurando que el contenido no ha sido modificado durante la transmisión. Finalmente, la no repudio impide que el remitente niegue haber enviado el mensaje, gracias al uso de firmas digitales.

En conjunto, la criptografía aplicada al correo electrónico transforma un medio de comunicación inherentemente inseguro en un canal mucho más confiable para el intercambio de información sensible, tanto en entornos personales como profesionales.

 Véase también

 Canal encubierto
 Criptología
 Criptografía simétrica o convencional
 Criptografía cuántica
 Criptografía asimétrica o de clave pública
 Criptografía de curva elíptica
 Criptografía híbrida
 Criptografía (música)
 Enigma
 Esteganografia
 Firma digital
 Criptoanálisis
 Infraestructura de clave pública
 Especificaciones PKCS
 Atbash
 Test de primalidad
 Ciberespacio
 Ciberseguridad
 Red privada virtual

 Algoritmos
 Advanced Encryption Standard
 ARC4
 Blowfish
 CuaimaCrypt
 DES / TripleDES
 DSA
 ECDSA
 Enigma
 IDEA
 ROT13
 RSA
 TEA / XTEA
 Protocolos
 DSS
 OpenPGP
 SET
 SSH
 SSL
 TLS

 Aplicaciones
 Software
 GNU Privacy Guard, GnuPG o GPG
 AxCrypt
 John the Ripper
 PGP
 WinCuaimaCrypt

 Cifrado de Discos duros y particiones
 FreeOTFE
 PointSec
 Safeboot
 SafeguardDisk
 TrueCrypt
 Dm-crypt
 Sistema de pago electrónico
 Transacción electrónica segura
 Monedero electrónico
 Voto electrónico

 Referencias

 Enlaces externos

 CriptoRed  Red Temática de Criptografía y Seguridad de la Información (más de 400 documentos, libros, software y vídeos freeware)
 Epsilones - Criptografía: métodos clásicos
 El derecho a cifrar
