---
type: Artículo de enciclopedia
title: Aleatoriedad en la disposición del espacio de direcciones
description: "La aleatoriedad en la disposición del espacio de direcciones (conocida por las siglas en inglés ASLR) es una técnica de seguridad informática relacionada con la explotación de vulnerabilidades basadas en la corrupción …"
resource: https://es.wikipedia.org/wiki/Aleatoriedad_en_la_disposición_del_espacio_de_direcciones
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Aleatoriedad_en_la_disposición_del_espacio_de_direcciones"}
license: CC BY-SA 4.0
id: eswiki-Aleatoriedad_en_la_disposición_del_espacio_de_direcciones
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Aleatoriedad en la disposición del espacio de direcciones

La **aleatoriedad en la disposición del espacio de direcciones** (conocida por las siglas en inglés **ASLR**) es una técnica de seguridad informática relacionada con la explotación de vulnerabilidades basadas en la corrupción de memoria. Con el fin de impedir que un atacante salte de forma fiable a, por ejemplo, una función explotable en concreto de la memoria, ASLR dispone de forma aleatoria las posiciones del espacio de direcciones de las áreas de datos clave de un proceso, incluyendo la base del ejecutable y las posiciones de la pila, el *heap* y las librerías.

 Historia

El proyecto PaX de Linux fue el primero en acuñar el término "ASLR", y publicó el primer diseño e implementación de ASLR en julio de 2001 en forma de un parche para el núcleo Linux. Se la considera una implementación completa, y proporciona también un parche para la aleatoriedad de la pila del núcleo desde octubre de 2002.

El primer sistema operativo popular en soportar ASLR por defecto fue la versión 3.4 de OpenBSD en 2003, seguido por Linux en 2005.

 Beneficios

La aleatoriedad del espacio de direcciones entorpece la labor de ciertos ataques contra la seguridad haciendo más difícil para un atacante predecir las direcciones de destino. Por ejemplo, los atacantes que intentan llevar a cabo ataques de retorno a libc deben primero localizar el código a ejecutar, mientras que los que intentan ejecutar código shell inyectado en la pila necesitan primero encontrar la propia pila. En ambos casos, el sistema oculta a ojos de los atacantes las direcciones de memoria que necesitan. Estos valores tienen que deducirse, y un error de deducción no suele ser recuperable puesto que conlleva el cuelgue de la aplicación.

 Efectividad

La aleatoriedad en la disposición del espacio de direcciones se basa en la baja probabilidad de que un atacante pueda adivinar las localizaciones de áreas dispuestas de forma aleatoria. La seguridad mejora aumentando el espacio a buscar. Por lo tanto, la aleatoriedad del espacio de direcciones es más eficaz cuando está presente una mayor entropía en la aleatoriedad. La entropía aumenta elevando el tamaño del área de memoria virtual sobre la que se aplica la aleatoriedad, o bien reduciendo el período sobre el que tiene lugar la aleatoriedad. Este período suele implantarse de forma que sea lo más pequeño posible, así que la mayoría de los sistemas deben incrementar la aleatoriedad del área de memoria virtual.

Para superar el problema de la aleatoriedad, los atacantes deben ser capaces de adivinar con éxito las posiciones de todas las áreas que desean atacar. En el caso de áreas de datos como son la pila y el *heap*, donde se puede cargar código a medida o información útil, puede atacarse a más de un estado utilizando secuencias NOP para código o copias repetidas de datos. Esto permite a un atacante tener éxito si la aleatoriedad del área la ha situado finalmente en un rango de unos pocos valores. A menudo estas áreas se mezclan, por ejemplo se inyectan marcos de pila en la pila y se retorna una entrada a una librería.

Pueden declararse las siguientes variables:

  (bits en entropía del tope por arriba de la pila)
  (bits de entropía de la base mmap)
  (bits de entropía de la base del ejecutable principal)
  (bits de entropía de la base del *heap*)
  (bits atacados por cada intento de entropía de la pila)
  (bits atacados por cada intento de entropía de la base mmap)
  (bits atacados por cada intento de entropía del ejecutable principal)
  (bits atacados por cada intento de entropía de la base del *heap*)
  (intentos realizados)
  (número total de entropía: )

Para calcular la probabilidad de un atacante de tener éxito, tenemos que asumir que se llevan a cabo  intentos sin que se produzca una interrupción entremedias por parte de un SPI basado en firmas, un refuerzo legal o cualquier otro factor; en el caso de un ataque de fuerza bruta, el demonio no puede reiniciarse. También tenemos que descubrir cuántos bits son relevantes y a cuántos se está atacando en cada intento, dejando a un lado los bits que el atacante tiene que derrotar.

Las siguientes fórmulas representan la probabilidad de éxito para un grupo dado de  intentos de  bits de entropía.

  (suposición aislada; tras cada intento, vuelve a aplicarse aleatoriedad al espacio de direcciones)
  (ataque sistemático de fuerza bruta sobre copias del programa con el mismo espacio de direcciones)

En muchos sistemas,  puede ser un valor de miles de millones; en los sistemas modernos de 64 bits, lo habitual es que estas cifras alcancen como mínimo millones. Héctor Marco-Gisbert e Ismael Ripoll mostraron en 2014 cómo saltarse el ASLR en sistemas de 64 bits en menos de un segundo bajo ciertas circunstancias. En el caso de sistemas de 32 bits a velocidades de 2004, y disponiendo de 16 bits para la aleatoriedad de las direcciones, Schacham y compañía aseguraron que "*... 16 bits de aleatoriedad en las direcciones es algo que puede romperse con un ataque de fuerza bruta en cuestión de minutos*". Conviene apuntar que esta afirmación por parte de su autor depende de la capacidad par atacar a la misma aplicación múltiples veces sin retraso alguno. Una implementación correcta de ASLR como la incluida en grsecurity proporciona varios métodos para hacer inviables tales ataques de fuerza bruta. Uno de los métodos consiste en impedir que un ejecutable se ejecute durante un determinado período de tiempo en caso de haberse *colgado* antes cierto número de veces.

Android y posiblemente otros sistemas implementan *Aleatoriedad en el Orden de Carga de Librerías*, una forma de ASLR que hace que el orden en el que se cargan las librerías sea aleatorio. Esto aporta muy poca entropía. Abajo se indica una aproximación del número de bits de entropía aportados por cada librería necesaria; esto no tiene en cuenta todavía los diferentes tamaños de las librerías, con lo cual la entropía obtenida en realidad es un poco mayor. Téngase en cuenta que los atacantes normalmente necesitan únicamente una librería; los cálculos son más complejos cuando entran en juego varias librerías, y también se muestran a continuación. Téngase también en cuenta que el caso de un atacante que emplea una única librería es una simplificación de la fórmula más compleja de .

  (número de librerías cargadas)
  (número de librerías usadas por el atacante)

Estos valores tienden a ser bajos aun con valores grandes de , lo que resulta importante dado que los atacantes normalmente pueden usar únicamente la librería estándar de C y por tanto uno puede suponer que . Resulta interesante, sin embargo, el hecho de que incluso con un pequeño número de librerías se ganan aquí unos pocos bits de entropía; por lo tanto, resulta potencialmente interesante combinar la aleatoriedad en el orden de carga de las librerías con la aleatoriedad de las direcciones de memoria virtual para ganar así unos bits extra de entropía. Téngase en cuenta que estos bits extra de entropía no se aplicarán a otros segmentos de mmap, sino únicamente a librerías.

 Reducción de la entropía

Un atacante puede utilizar varios métodos para reducir la entropía presente en un espacio de direcciones al que se ha aplicado aleatoriedad, que pueden ir desde simples fugas de información a atacar múltiples bits de entropía en cada ataque (como la técnica de pulverización del heap). Poco puede hacerse a este respecto.

Es posible obtener información sobre la disposición de la memoria empleando vulnerabilidades en el formateo de cadenas. Las funciones de formateo de cadenas tales como printf utilizan una lista de argumentos variables para hacer su trabajo; los especificadores de formato describen el aspecto de la lista de argumentos. Debido a la manera en que se suelen pasar los argumentos, cada especificador de formato se acerca cada vez más al tope superior del marco de la pila. Llegado a cierto punto pueden extraerse el puntero de retorno y el puntero del marco de la pila, revelando así las direcciones de una librería vulnerable y la dirección de un marco de pila conocido; esto puede eliminar por completo la aleatoriedad de la pila y de las librerías como un obstáculo para el atacante.

Uno puede también reducir la entropía en la pila o en el heap. Lo habitual es que la pila tenga que alinearse a 16 bytes, con lo cual este sería el intervalo de aleatoriedad más pequeño posible, mientras que el heap debe alinearse a página, normalmente 4096 bytes. Al intentar llevar a cabo un ataque, es posible alinear ataques duplicados con estos intervalos; una cadena de instrucciones NOP puede utilizarse con inyección de código shell, y la cadena '/bin/sh' puede sustituirse con '////////bin/sh' empleando un número arbitrario de barras inclinadas al intentar retornar al *sistema*. El número de bits eliminado es exactamente  para  intervalos atacados.

Tales reducciones están limitadas debido a la cantidad de información presente en la pila o en el heap. La pila, por ejemplo, suele estar limitada a 8 MBs y crece para ser mucho más pequeña; esto permite como mucho 19 bits, aunque una estimación más conservadora sería de entre 8 y 10 bits correspondientes a 4-16 KBs de ataques a la pila. El heap, por otra parte, está limitado por el comportamiento del adjudicador de memoria; en el caso de glibc, las reservas por encima de los 128KB se crean con mmap, limitando los atacantes a 5 bits de reducción. Esto es un factor también limitante en el caso de ataques de fuerza bruta; aunque puede reducirse el número de ataques que es necesario realizar, el tamaño de los ataques aumenta lo suficiente como para que en determinadas circunstancias esto llame la atención de un sistema de prevención de intrusos.

 Implementaciones

Varios sistemas operativos populares de propósito general implementan ASLR.

 Android

Android 4.0 Ice Cream Sandwich proporciona aleatoriedad en la disposición del espacio de direcciones (ASLR) para ayudar a proteger el sistema y las aplicaciones de terceros frente a vulnerabilidades relacionadas con la gestión de la memoria. Android 4.1 añadió soporte para ejecutables independientes de posición (PIE), mientras que Android 5.0 abandonó el soporte para ejecutables sin PIE y exige que todos los binarios enlazados dinámicamente sean independientes de posición. La aleatoriedad en el orden de carga de las librerías se aceptó en el proyecto de código abierto Android el 26 de octubre de 2015, y fue incluido a partir de Android 7.0.

 DragonFly BSD

DragonFly BSD dispone de una implementación de ASLR basada en el modelo de OpenBSD, añadido en 2010. Está desactivada por defecto, y puede activarse poniendo a 1 el valor de vm.randomize_mmap con *sysctl*.

 iOS (iPhone, iPod Touch, iPad)

Apple introdujo ASLR en iOS 4.3, lanzado en marzo de 2011.

Base del kernel KASLR una vez aplicada la aleatoriedad = 0x01000000 + ((1+0xRR) * 0x00200000)

donde 0xRR = un byte aleatorio de SHA1(información alatoria) generado por iBoot (el cargador de arranque de segunda etapa).

 Linux

El núcleo Linux activó una forma débil de ASLR por defecto desde su versión 2.6.12, lanzada en junio de 2005. Los juegos de parches PaX y Exec Shield aplicados al núcleo Linux proporcionan implementaciones más completas. El parche Exec Shield para Linux proporciona 19 bits de entropía de la pila en un período de 16 bytes, así como 8 bits de aleatoriedad de la base de mmap en un período de 1 página de 4096 bytes. Esto sitúa a la base de la pila en un área de una anchura de 8 MB, conteniendo 524.288 posiciones posibles, y la base de mmap en un área de 1 MB de anchura, conteniendo 256 posiciones posibles. Varias distribuciones de Linux —incluyendo Adamantix, Alpine Linux, Gentoo Hardened y Hardened Linux From Scratch— vienen por defecto con la implantación PaX de ASLR.

La técnica Ejecutable independiente de posición (PIE) implementa una dirección base aleatoria para el binario ejecutable principal y ha estado vigente desde 2003. Proporciona la misma aleatoriedad en las direcciones al ejecutable principal que la que se utiliza en el caso de las librerías compartidas. PIE se utiliza solamente para los demonios orientados a redes – PIE no puede combinarse con la función de preenlazado en el mismo ejecutable. La herramienta de preenlazado implementa aleatoriedad en el momento del preenlazado en lugar de hacerlo en el momento de la ejecución, ya que por diseño el preenlazado tiene como objetivo encargarse de la relocatación de librerías antes de que el enlazador dinámico tenga que hacerlo, lo que permite que la relocatación tenga lugar una sola vez para muchas ejecuciones del programa. Como resultado, una verdadera aleatoriedad en el espacio de direcciones echaría a perder el objetivo del preenlazado.

La *aleatoriedad en la disposición del espacio de direcciones del kernel* (KASLR), que añade soporte para la aplicación de aleatoriedad al espacio de direcciones a las imágenes del núcleo Linux a base de aplicar aleatoriedad al lugar donde se coloca el código del kernel en el momento del arranque, se fusionó en el árbol de desarrollo del kernel en la versión 3.14, lanzada el 30 de marzo de 2014. Tras su compilación, esta característica puede desactivarse durante el arranque indicando  como uno de los parámetros de arranque del kernel.

Existen varios ataques de canal lateral viables en los procesadores x86 que podrían llegar a averiguar las direcciones del kernel. A finales de 2017 se desarrolló el aislamiento de tablas de páginas del kernel (KPTI, también conocido como KAISER) con el fin de poner coto a estos ataques.

 Microsoft Windows

El sistema operativo Windows Vista de Microsoft (lanzado en enero de 2007) y las versiones posteriores del sistema operativo llevan ASLR activado únicamente para los ejecutables y librerías de enlace dinámico enlazadas específicamente para que se les aplique ASLR. Por razones de compatibilidad, no está activado por defecto para el resto de aplicaciones. Lo habitual es que sólo el software más antiguo sea incompatible y ASLR puede activarse completamente editando el valor "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\MoveImages" del registro, o bien instalando el kit Enhanced Mitigation Experience Toolkit de Microsoft.

A las localizaciones del heap, la pila y el TLB también se aplica aleatoriedad. Un documento de Symantec destacó que la implementación ASLR en Windows Vista de 32 bits puede no ser tan robusta como se esperaba, y Microsoft ha reconocido una debilidad en dicha implementación.

Los sistemas de prevención de intrusos basados en anfitrión tales como *WehnTrust* y *Ozone* también ofrecen ASLR para los sistemas operativos Windows XP y Windows Server 2003. Wehntrust es código abierto. No hay información detallada sobre la implementación utilizada por Ozone.

En febrero de 2012 se apuntó que la implementación de ASLR en los sistemas operativos Windows de 32 bits anteriores a Windows 8 puede sufrir una pérdida de eficacia en situaciones de escasez de memoria. La misma investigación detectó un efecto similar en Linux. El código utilizado como prueba causó un pánico del núcleo en MacOS X 10.7.3, así que no quedó claro el comportamiento de ASLR en este caso.

 NetBSD

El soporte para ASLR en el espacio de usuario apareció en NetBSD 5.0, lanzado en abril de 2009, y se activó por defecto en NetBSD-current en abril de 2016.

El soporte para ASLR referente al kernel en amd64 se añadió en NetBSD-current en octubre de 2017, convirtiendo a NetBSD en el primer sistema BSD en soportar KASLR.

 OpenBSD

En 2003 OpenBSD se convirtió en el primer sistema operativo popular en soportar una variante poderosa de ASLR y en activarla por defecto. OpenBSD completó su soporte para ASLR en 2008 cuando añadió soporte para binarios PIE. La función malloc de OpenBSD se diseñó para mejorar la seguridad aprovechando las ventajas de ASLR y los huecos entre páginas implantados como parte de la llamada al sistema mmap de OpenBSD, y para detectar fallos del tipo usar-despueś-de-liberar. Lanzado en 2013, OpenBSD 5.3 fue el primer sistema operativo popular en habilitar PIE por defecto en múltiples arquitecturas de hardware, y OpenBSD 5.7 activó por defecto los binarios estáticos independientes de posición (Static-PIE).

 OS X

En Mac OS X Leopard 10.5 (lanzado en octubre de 2007) Apple introdujo aleatoriedad para las librerías del sistema.

En Mac OS X Lion 10.7 (lanzado en julio de 2011), Apple amplió su implementación para cubrir todas las aplicaciones, afirmando que "*la aleatoriedad en la disposición del espacio de direcciones (ASLR) ha sido mejorada para todas las aplicaciones. Ahora está disponible para aplicaciones de 32 bits (como es el caso de las protecciones de memoria del heap), haciendo que tanto las aplicaciones de 64 como de 32 bits sean más resistentes a ataques*".

En Mac OS X Mountain Lion 10.8 (lanzado en julio de 2012) y posteriores, todo el sistema, incluyendo tanto el kernel como los módulos cargados por él y las zonas se relocalizan de forma aleatoria durante el arranque del sistema.

 Solaris

ASLR se introdujo en Solaris a partir de la versión 11.1, lanzada en octubre de 2012. La implementación de ASLR en Solaris 11.1 puede actuar en todo el sistema, por zonas, o individualmente por binarios.

 Explotación
Se ha demostrado que un ataque de canal lateral basado en un búfer de objetivo de ramificación puede saltarse la protección que ofrece ASLR. En 2017 se mostró un ataque denominado "ASLR⊕Cache" que podía saltarse la protección de ASLR en un navegador web utilizando JavaScript.

 Véase también
 Desbordamiento del búfer
 Bit NX

 Referencias

 Enlaces externos
 Exploit Mitigation Techniques: an Update After 10 Years  in OpenBSD (en inglés)
 PaX documentation on ASLR (en inglés)
 Comparison of PaX to Exec Shield and W^X  (en inglés)
 ASLR for Windows Vista beta 2 (en inglés)
 ASLR for Windows 2000/XP/2003 (WehnTrust) (en inglés)
 Bypassing PaX ASLR protection (en inglés)
 On the effectiveness of address space layout randomization (en inglés)
 Test Applications (or libraries) for their ASLR and DEP support (en inglés)
 ASLR Smack & Laugh Reference  (en inglés)
