---
type: Artículo de enciclopedia
title: Spectre (vulnerabilidad)
description: Spectre es una vulnerabilidad que afecta a los microprocesadores modernos que utilizan predicción de saltos.
resource: https://es.wikipedia.org/wiki/Spectre_(vulnerabilidad)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Spectre_(vulnerabilidad)"}
license: CC BY-SA 4.0
id: eswiki-Spectre_(vulnerabilidad)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Spectre (vulnerabilidad)

- **Título:** Spectre
- **Alias:** CVE-2017-5715CVE-2017-5753
- **Tipo:** Intel, AMD, ARM, POWER, PowerPC
- **Subtipo:** Procesadores con ejecución especulativa
- **Sistema operativo:** AIX, Android, iOS, GNU/Linux, Mac OS, tvOS, Windows
- **Fecha de inicio:** 3 de enero de 2018

**Spectre** es una vulnerabilidad que afecta a los microprocesadores modernos que utilizan predicción de saltos. En la mayoría de los procesadores, la ejecución especulativa que surge de un fallo de la predicción puede dejar efectos observables colaterales que pueden revelar información privada a un atacante. Por ejemplo, si el patrón de accesos a la memoria realizados por la mencionada ejecución especulativa depende de datos privados, el estado resultante de la caché de datos constituye un canal lateral mediante el cual un atacante puede ser capaz de obtener información acerca de los datos privados empleando un ataque sincronizado.

Se han emitido dos ID de Vulnerabilidades y Exposiciones Comunes (siglas en inglés CVE) relacionados con Spectre, CVE-2017-5753 (variante 1, baipás de la comprobación de límites) y CVE-2017-5715 (variante 2, inyección de destino del salto). Se ha descubierto que los motores JIT empleados para JavaScript son vulnerables. Un sitio web podría leer información guardada en el navegador que pertenece a otro sitio web, o acceder a información alojada en la memoria que está utilizando el navegador.

 Historia
 En 2002 y 2003, Yukiyasu Tsunoo y colegas de NEC mostraron cómo atacar los algoritmos de cifrado MISTY1 y DES respectivamente.
 En 2005, Daniel Bernstein de la Universidad de Illinois informó de la obtención de una clave AES de OpenSSL mediante un ataque sincronizado a la caché, y Colin Percival disponía de un ataque operativo a las claves RSA de OpenSSL usando la caché de los procesadores Intel.
En 2013, Yuval Yarom y Katrina Falkner de la Universidad de Adelaida mostraron cómo medir el tiempo de acceso a los datos permite a una aplicación espía deducir si la información se leyó desde la caché o no. En caso de leerse desde la caché el tiempo de acceso era muy corto, y la información leída podía contener la clave privada de los algoritmos de encriptación. Esta técnica se utilizó con éxito para soslayar la seguridad ofrecida por GnuPG, AES y otras implementaciones criptográficas.
 En enero de 2017, Anders Fogh hizo una presentación en la Ruhruniversität Bochum acerca del descubrimiento automático de canales encubiertos, especialmente en procesadores que usan segmentación de instrucciones distribuida por varios núcleos del procesador.
 Spectre fue descubierto de forma independiente en enero de 2018 por Jann Horn, miembro del Proyecto Cero de Google y por Paul Kocher, en colaboración con Daniel Genkin, Mike Hamburg, Moritz Lipp y Yuval Yarom. El departamento de investigación de vulnerabilidades de Microsoft (MSVR) amplió los sistemas afectados a los motores JIT JavaScript de los navegadores web. La vulnerabilidad se hizo pública junto con otra, Meltdown, el 3 de enero de 2018, una vez que los fabricantes del hardware afectado tuvieron conocimiento del problema el 1 de junio de 2017. La vulnerabilidad fue denominada "Spectre" (espectro) porque «está basada en la causa de base, la ejecución especulativa. Puesto que no es fácil de corregir, será algo que nos persiga durante mucho tiempo [como un fantasma]».
 El 28 de enero de 2018 se publicó la noticia de que Intel había compartido información acerca de las vulnerabilidades Meltdown y Spectre con empresas tecnológicas chinas antes de notificar estos defectos al gobierno estadounidense.
 El 29 de enero de 2018 se informó de que Microsoft había lanzado una actualización para Windows que desactiva la corrección problemática para el microcódigo (que causaba posibles reinicios, problemas de estabilidad y de corrupción o pérdida de datos) publicada por Intel para la variante 2 del ataque de Spectre. A su vez, esta actualización motivó cierta preocupación.
 El 14 de agosto de 2018 la empresa Intel reconoció de forma oficial el descubrimiento de tres vulnerabilidades adicionales que se aprovechan de la ejecución especulativa y que es parecido a Spectre. Como en realidad afecta a la memoria caché L1 fue nombrada L1 Terminal Fault (*Falla de Terminal L1*), y afecta principalmente al software hipervisor por lo que las granjas de servidores que utilizan tecnología de virtualización a nivel de sistema operativo son especialmente afectadas.

 Explicación detallada
Spectre es una vulnerabilidad que permite a los programas alojados en el sistema operativo del usuario acceder a una dirección arbitraria del espacio de memoria de un programa.

En lugar de una única vulnerabilidad de fácil corrección, el documento de Spectre describe una clase entera de vulnerabilidades potenciales. Todas esas vulnerabilidades se basan en explotar los efectos secundarios de la ejecución especulativa, una técnica empleada comúnmente para combatir la latencia de la memoria y acelerar así la ejecución en los microprocesadores modernos. En particular, Spectre se centra en la predicción de saltos, un caso especial de la ejecución especulativa. A diferencia de la vulnerabilidad Meltdown hecha pública la misma fecha, Spectre no depende de una característica en particular de la gestión de memoria de un procesador en concreto o de cómo proteja el acceso a esa memoria, sino que tiene un enfoque más general.

El punto de partida del documento de Spectre es un ataque sincronizado de canal lateral aplicado al sistema de predicción de saltos de un microprocesador moderno que utilice ejecución fuera de orden. Si bien al nivel arquitectónico documentado en las hojas técnicas de los procesadores los resultados de un fallo en la predicción se especifican que quedarán anulados tras darse dicha circunstancia, la ejecución especulativa resultante puede aun así dejar efectos colaterales, como líneas de caché cargadas con determinada información. Estos efectos colaterales pueden posteriormente afectar a los denominados aspectos no funcionales del sistema informático. Si tales efectos colaterales incluyendo, entre otros, los tiempos de acceso a la memoria resultan visibles para un programa malicioso, y puede hacerse que esos efectos dependan de información sensible en posesión del proceso que hace las veces de víctima, entonces estos efectos colatelares pueden hacer que la información sensible resulte deducible. Esto puede ocurrir aunque los sistemas de seguridad formales a nivel de arquitectura funcionen de forma correcta  lo que sucede es que las optimizaciones en los niveles más bajos a nivel de microarquitectura dirigidas a aceleración la ejecución de código [pueden] revelar información no esencial para la correcta ejecución de un programa.

El documento de Spectre detalla el ataque en cuatro etapas esenciales:

 Primero, muestra que la lógica de la predicción de saltos de los procesadores actuales puede ser *entrenada* para acertar o fallar en sus pronósticos según disponga el funcionamiento interno de un programa malicioso.
 En segundo lugar, muestra que las diferencias subsiguientes entre los aciertos y los fallos de la caché pueden medirse de forma fiable, de tal forma que lo que debería ser simplemente una diferencia entre que algo funcione o no se convierte en un canal encubierto que revela información acerca del funcionamiento interno de un proceso ajeno.
 En tercer lugar, el documento sintetiza los resultados obtenidos con trucos de la programación orientada a retorno y otros principios mediante un sencillo programa de ejemplo y un fragmento de código JavaScript corriendo en un navegador web con aislamiento de procesos: en ambos casos, el espacio de direcciones al completo del proceso que hace de víctima (es decir, el contenido de un programa que se está ejecutando) se demuestra que es legible simplemente explotando la ejecución especulativa de la predicción de saltos en código generado por un compilador de uso común o el intérprete de JavaScript de un navegador corriente. La idea básica es buscar en el código existente lugares donde la especulación tiene "contacto" con datos de otro modo inaccesibles, manipular el proceso para ponerlo en un estado en el que la ejecución especulativa tenga que tocar esos datos, y entonces comprobar si el procesador ha sido más rápido porque la prelectura de la caché hizo que se colocase cierta información en la caché.
 Por último, el documento concluye generalizando el ataque a cualquier estado no funcional del proceso tomado como víctima, y discute brevemente incluso efectos no funcionales que se pasan fácilmente por alto, como la latencia en el arbitraje del bus de memoria.

La diferencia básica entre Spectre y Meltdown estriba en que Spectre puede utilizarse para manipular un proceso de tal forma que revele sus datos privados. Por su parte, Meltdown puede utilizarse para leer la memoria protegida del espacio de direcciones de un proceso, algo que ni siquiera el propio proceso sería normalmente capaz de hacer; en ciertos sistemas operativos no protegidos, esto incluye datos pertenecientes al núcleo o a otros procesos.

El documento de Meltdown distingue ambas vulnerabilidades de esta forma: "Meltdown es distinto de los ataques de Spectre de varias maneras, pero la principal diferencia es que Spectre necesita ser adaptado al entorno de software del proceso marcado como víctima, si bien por otro lado sus ataques son viables en una mayor variedad de CPU y no pueden mitigarse con KAISER".

 Explotación remota
Si bien Spectre es más fácil de explotar con un lenguaje compilado como C o C++ ejecutando de forma local código máquina, también puede explotarse de forma remota empleando código alojado en páginas web maliciosas, por ejemplo con un lenguaje interpretado como es JavaScript, que se ejecuta de forma local al utilizar un navegador web. El programa malicioso dispondría entonces de acceso a toda la memoria mapeada al espacio de direcciones del navegador.

La explotación vía JavaScript ejecutado remotamente sigue un procedimiento similar al de la explotación de código albergado localmente: limpiar caché → entrenamiento defectuoso del predictor de saltos → lecturas sincronizadas (monitorizando los aciertos y fallos de la caché).

La falta de una instrucción clflush (limpieza de línea de caché) en JavaScript exige una técnica alternativa. Hay varias políticas automáticas de desahucio de la caché entre las que la CPU puede elegir, y que pueda usarse la vulnerabilidad depende de que pueda forzarse ese desahucio de datos. Se descubrió que usar un segundo índice en la matriz grande, que se mantenía con datos de varias iteraciones por detrás del primer índice, hacía que se utilizase la política del *usado de forma menos reciente*. Esto permite que la vulnerabilidad pueda limpiar la caché simplemente haciendo lecturas incrementales sobre un gran conjunto de datos.

El predictor de saltos se entrenaría de forma defectuosa al operar una y otra vez sobre un conjunto muy grande de datos empleando operaciones orientadas a bits para definir el índice con un valor dentro de rango, y entonces usando la dirección fuera de límites para la iteración final.

Entonces se necesitaría un temporizador de alta precisión para poder determinar si un conjunto de lecturas han conducido a un acierto o a un fallo de la caché. Si bien navegadores como Google Chrome, Firefox y Tor (basado en Firefox) han puesto restricciones en la resolución de sus temporizadores (Spectre necesita una alta resolución para determinar si ha habido aciertos o fallos de la caché), en el momento de redactar la documentación de la vulnerabilidad, el autor de Spectre fue capaz de crear un temporizador de alta resolución empleando la función de ejecución de scripts en segundo plano de HTML5.

Fue necesario programar y analizar cuidadosamente el código máquina ejecutado por el compilador JIT para asegurar que las funciones de limpieza de la caché y las lecturas que aprovechaban la vulnerabilidad no fueran eliminadas por algún tipo de optimización.

 Impacto
Desde 2018, casi todos los sistemas informáticos están potencialmente afectados por Spectre, incluidos los equipos de sobremesa, portátiles y dispositivos móviles. Específicamente, se ha demostrado que Spectre funciona en procesadores Intel, AMD, los basados en ARM y los de IBM. Intel respondió a las vulnerabilidades de seguridad reportadas con una declaración oficial. En un principio, AMD aseguró que la vulnerabilidad a una de las dos variantes de Spectre no se había demostrado en sus procesadores, afirmando que el riesgo de explotación era «casi nulo» debido a las diferencias en la arquitectura de sus procesadores. Sin embargo, posteriormente AMD anunció que sus procesadores estaban afectados por ambas variantes de Spectre.

Los investigadores han indicado que la vulnerabilidad Spectre puede afectar posiblemente a algunos procesadores Intel, AMD y ARM. Concretamente, los procesadores con ejecución especulativa son los afectados por estas vulnerabilidades.

ARM ha informado que la mayoría de sus procesadores no son vulnerables, y ha publicado una lista de los procesadores en concreto que sí están afectados por la vulnerabilidad Spectre: Cortex-R7, Cortex-R8, Cortex-A8, Cortex-A9, Cortex-A15, Cortex-A17, Cortex-A57, Cortex-A72, Cortex-A73 y Cortex-A75.

Spectre tiene el potencial de tener un mayor impacto en los proveedores de la nube que Meltdown. Mientras que Meltdown permite a las aplicaciones no autorizadas leer desde una memoria privilegiada para obtener datos confidenciales de procesos que se ejecutan en el mismo servidor en nube, Spectre puede permitir que programas maliciosos induzcan a un hipervisor a transmitir los datos a un sistema invitado que se ejecute en él, como es el caso de una máquina virtual.

 Mitigación
Puesto que Spectre representa una clase entera de ataques, lo más probable es que no pueda haber un único parche general para él. Aunque ya se está trabajando para abordar casos especiales de la vulnerabilidad, el sitio web original dedicado a Spectre y Meltdown afirma que «dado que [Spectre] no es fácil de arreglar, nos perseguirá durante mucho tiempo». Al mismo tiempo, y según Dell: "*No se ha tenido constancia hasta la fecha (7 de febrero de 2018) de que estas vulnerabilidades hayan sido puestas en práctica en el mundo real, a pesar de que los investigadores han publicado pruebas de concepto*".

Se han reportado varios procedimientos a seguir para proteger los ordenadores domésticos y dispositivos relacionados frente a Meltdown y Spectre. Se ha informado de que los parches para Spectre degradan el rendimiento de forma significativa, especialmente en los ordenadores más antiguos; en las nuevas plataformas de octava generación se han medido caídas de rendimiento de entre un 2 y un 14 % realizando pruebas de referencia. El 18 de enero de 2018 se informó de problemas con reinicios no deseados debidos a los parches para Meltdown y Spectre, incluso en el caso de chips recientes de Intel.

Se ha sugerido que el coste de la mitigación puede aliviarse en procesadores que soporten la limpieza selectiva del TLB, una característica también conocida como identificador de contexto de proceso (PCID) en la arquitectura Intel 64, y número de espacio de dirección (ASN) en la arquitectura Alpha. Esto se debe a que la limpieza selectiva hace que el comportamiento del TLB que resulta crucial para la vulnerabilidad se aísle entre procesos, sin estar constantemente limpiando el TLB en su totalidad, principal motivo del coste de la mitigación.

 Sistemas operativos
 El 14 de julio de 2018 fue liberada la versión 9.5 de Debian la cual incluye una mitigación a la variante dos de *Spectre* por medio de un parche al kernel.

 Software particular
Se han reportado varios procedimientos a seguir para proteger los ordenadores domésticos y dispositivos relacionados frente a Meltdown y Spectre.

Puesto que es posible la explotación a través de Javascript incrustado en los sitios web, Chrome 64 incluirá por defecto mitigaciones contra el ataque, y los usuarios de Chrome 63 pueden mitigar manualmente el ataque activando la función *Strict Site Isolation* (chrome://flags#enable-site-per-process).

A partir de Firefox 57.0.4, Mozilla está reduciendo la resolución de los temporizadores JavaScript para ayudar a prevenir ataques sincronizados, y está trabajando y planificando técnicas de ofuscación de tiempos para futuras versiones.

 Medidas generales y controversia
El 4 de enero de 2018 Google detalló una nueva técnica en su blog de seguridad llamada *retpoline* —contracción en inglés de *return trampoline*— que puede detener la vulnerabilidad Spectre añadiendo una sobrecarga insignificante para el procesador, y consiste en dirigir a nivel del compilador las ramas indirectas hacia un destino distinto, de forma que no pueda tener lugar una ejecución especulativa fuera de orden que sea vulnerable. Aunque se desarrolló para el juego de instrucciones de los procesadores x86, los ingenieros de Google creen que la técnica también es transferible a otros procesadores.

El 25 de enero de 2018 se presentó un informe sobre el estado actual así como de las posibles consideraciones a tomar de cara al futuro con el fin de resolver las vulnerabilidades Meltdown y Spectre.

Después de que Intel anunciase que la mitigación de Spectre puede activarse manualmente como una "medida de seguridad" en lugar de considerarla un fallo, el creador de Linux, Linus Torvalds calificó los parches como "una completa basura". Ingo Molnár sugirió entonces utilizar el sistema de monitorización de funciones integrado en el kernel Linux para corregir la vulnerabilidad Spectre sin soporte desde microcódigo para la especulación restringida de saltos indirectos (IBRS). De este modo, solo habría un impacto en el rendimiento en el caso de los procesadores basados en las microarquitecturas Skylake de Intel y otras más recientes.

 Referencias

 Lectura adicional

 Enlaces externos
 Sitio web que documenta las vulnerabilidades Meltdown y Spectre, hospedado por la Universidad Tecnológica de Graz
 Reseña del Proyecto Cero de Google
  Spectre, Meltdown researchers unveil 7 more speculative execution attacks, siete nuevos tipos de posibles ataques empleando *Spectre*.
