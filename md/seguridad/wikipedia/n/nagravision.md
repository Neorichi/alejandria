---
type: Artículo de enciclopedia
title: Nagravisión
description: Nagravisión, también conocido como Nagra Kudelski o Nagra, MPEG, basado en la aritmética modular, utilizado por plataformas de televisión por satélite y cable.
resource: https://es.wikipedia.org/wiki/Nagravisión
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Nagravisión"}
license: CC BY-SA 4.0
id: eswiki-Nagravisión
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Nagravisión

**Nagravisión**, también conocido como **Nagra Kudelski** o **Nagra**, MPEG, basado en la aritmética modular, utilizado por plataformas de televisión por satélite y cable. Algunas de las plataformas que usan este sistema son en España: Movistar+, Vodafone TV y R; y en el resto del mundo: Sky (Alemania), Telewizja Polsat (Polonia), NOS (Portugal) Dish (México) o SAT HD Regional (Brasil), entre muchas otras.

 Historia
Nagravisión es un proyecto de la empresa de seguridad informática suiza Kudelski Group, dirigida por André Kudelski, especializada en cifrado y descifrado de señal MPEG en acceso condicional a ella, base principal de todos los proveedores de televisión por satélite y cable. El proyecto Nagravisión ha tenido varias versiones y numerosos parches de seguridad; conocidas como Nagra 1, Nagra 2 y Nagra 3 han permitido a la empresa superar los inconvenientes de la piratería, que ha dejado en evidencia a la compañía en numerosas ocasiones del pasado.

En España se utilizó por primera vez en su variante analógica Nagra+, la cual era utilizada por Canal+ terrestre, canal que fue reemplazado por Cuatro desde el mes de noviembre de 2005. En los primeros años de emisión de la plataforma de satélite Vía Digital se utilizó el sistema Nagravisión 1, que fue sustituido posteriormente por Nagravisión 2. Tanto los sistemas Nagravisión 1 y Nagravisión 2 tenían numerosos fallos de seguridad graves que permitieron que los sistemas fuesen visionados sin utilizar los descodificadores del distribuidor. Debido a esto TV Cabo (Portugal) decidió adaptar sus sistemas a Nagra 3 a finales de 2007, solucionando hasta la fecha el problema, así como Digital+ (empresa fusión de Vía Digital y Canal Satélite Digital), que desde el 4 de diciembre de 2007 utiliza el nuevo sistema Nagravisión 3. Actualmente la mayor parte de los proveedores Europeos han migrado ya sus sistemas a Nagra 3, incluyendo Premiere (Alemania), que el 12 de octubre de 2008 modificó su sistema de codificación, siendo el último gran proveedor en Europa que conservaba Nagra 2.
Digitv, la televisión rumana de pago, otra de las últimas en usar Nagra 2, desde el 5 de agosto de 2010 ha migrado también sus sistemas a Nagra 3.

El operador español de servicios por cable ONO realizó en el año 2011 la migración parcial de sus señales de televisión digital, conjuntamente y como consecuencia de la introducción de su nuevo descodificador con funciones de PVR, que incorpora el sistema TiVo y también emplea Nagra 3.

Por último, y coincidiendo con el lanzamiento del Descodificador "Pura HD" en 2013, la cablera R completó la implantación de Nagra 3, que comenzó en 2010 con la distribución de las nuevas tarjetas de abonados.

A octubre de 2009, en los sistemas de pago por visión, no existe ningún software capaz de penetrar el cifrado de Nagra 3 (a excepción del cardsharing, que lo que hace es usar un deco servidor, que envía las claves de la tarjeta original al deco servidor y sólo se puede visualizarlo con un abono legal). Kudelski Corporation por ahora ha logrado garantizar que sus sistemas de seguridad son fiables. También se ha visto reducido el abanico de servidores que conservan Nagra 2 a los pequeños proveedores de televisión por satélite, como por ejemplo proveedores rumanos.

A enero de 2012, el tema no ha progresado demasiado respecto a la emulación completa del sistema, es decir, ningún aparato es capaz de descifrar la información suministrada por el proveedor, tan solo los sistemas CardSharing permiten acceso condicional compartido, que no es comparable al nivel de acceso que se había conseguido con el antiguo Nagra 2.

 Funcionamiento
 Bases principales
 La **aritmética modular** es la base de todo el sistema nagra.

*Para cifrar un mensaje*:  *Para descifrar*:

M: mensaje (en claro), y que en RSA debe ser un número, todo lo largo que se desee.

MC: es el mismo mensaje (pero cifrado), que también va resultar ser un número.

*p*, *q*: dos números primos, elegidos por el propietario de la clave.

*N*: número que se obtiene de multiplicar los dos números (*p* * *q*).

*e*: número elegido por el propietario de la clave (que se utiliza sólo para cifrar).

*d*: número, que se obtiene sobre la base de (*e*, *p*, *q*) y que se explicará al final.

 El otro pilar es **el uso de tarjetas para el acceso condicional** a la señal, punto clave del sistema y donde la piratería centra todos sus esfuerzos, por ser el centro neurálgico de todo el sistema.

 Tarjetas

Las tarjetas tienen una memoria EEPROM y un chip microcontrolador que permite el control de los datos. En Nagra la EEPROM se divide en dos zonas: una de datos y otra de código y en esta última el proveedor puede grabar código ejecutable por la tarjeta para corregir errores. El microprocesador de la tarjeta solo busca bugcatcher (explicado a continuación) cuando encuentra en ROM una interrupción de software.

 **Versiones y tipos de tarjetas**

Existen cinco versiones de tarjetas de uso principal en España (Vía Digital y más tarde Digital+):
Rom003, Rom010 y Rom011 para Nagra 1. Rom101 y Rom110 para Nagra 2. Se rumorea que llegó a haber algunas Rom002 en pruebas en los comienzos de Vía Digital.

En otros proveedores se han usado otro tipo de tarjetas, como Rom007 en Euskaltel (proveedor de TV por cable en el País Vasco), u otras como Rom005, Rom006, Rom009 (en proveedores norteamericanos).
En la plataforma Vía Digital llegó a utilizarse la versión Rom004 antes del paso a la utilización de la Rom010, pero con una distribución muy limitada.

La versión Rom002 se utilizó en los inicios de la plataforma estadounidense Dish Network, y se cree que la Rom001 igualmente pudo ser utilizada en pruebas o en las primeras tiradas (en los documentos técnicos del sistema realizados por hackers, hay comentarios sobre esta versión).

Aún no se conocen bien las ROM para Nagra 3, pero todo parece indicar que la política de Kudelski de trabajar con la misma ROM para todos las plataformas de televisión por satélite ha cambiado, por las diferencias percibidas en el Nagra 3 de TV Cabo y el de Canal +.

Cada tipo de tarjeta tiene una revisión (versión de la EEPROM) diferente:
En el proveedor Vía Digital la Rom003 alcanzó la revisión rev340, la Rom10 revA3E y la Rom11 revB09. Se desconoce la revisión que alcanzó la Rom004, aunque se sospecha que dejó de ser actualizada ante la ínfima cantidad de tarjetas en servicio de la citada versión.

 **Conceptos principales**

Todas las tarjetas tienen un **número de serie único (CAM)**, el **número de serie del decodificador** (IRD), una clave común entre la tarjeta y que también está en el decodificador (**Box Key**), Código postal al que pertenece el abonado (**ZIP**), **BugCatchers**, **NumBugs** (número de bugcatchers), **Backdoors** (instrucciones para ejecutar donde no hay seguridad) y otros muchos atributos donde se realiza un control sobre la seguridad del sistema.

Los **bugcatchers** son fragmentos de código que se ejecutan en el decodificador para corregir errores de seguridad y otras configuraciones que el proveedor desee hacer en sus sistemas, éste es uno de los puntos clave del sistema y más estudiado por los colectivos de piratería.

Aunque el dato más interesante de las tarjetas son los llamados **Tiers**, que son registros internos que almacenan información de la suscripción, parece que ésta será otra de las bazas para intentar penetrar el nuevo Nagra 3.

 **Ejemplos de comandos Back Door**

Comando $0E: borra la EEPROM

Comando $20: Login (usado para decirle a la CAM cuales son las passwords)

Comando $B0: volcar memoria

Comando $D6: ejecuta código/escribe en la EEPROM

 Decodificador (IRD - Integrated Receiver Decoder)
El sistema clásico de suscripción y abono a las plataformas de televisión por satélite incluye una antena parabólica, un receptor-decodificador y una pantalla. Su función principal es descomprimir las señales de vídeo y audio digitales recibidas en MPEG-2 una vez han sido demoduladas y corregidas de posibles errores introducidos por el canal de transmisión y transformarlas en dos señales de audio y video analógicas que ya podrán ser visualizadas en un televisor.

El IRD es el dispositivo que contiene el hardware, el software e interfaces necesarios para seleccionar, recibir, decodificar y visualizar los programas y servicios ofrecidos por la televisión digital.

 Versiones
 Nagra

El primer sistema de acceso condicional implantando en España de la compañía Kudelski, utilizada por Canal + analógico.

Basada en un sencillo cifrado sobre la base de la aritmética modular. Este sistema utilizaba una clave hexadecimal de ocho pares de dígitos del tipo: E2 01 24 1A 00 C5 81 03.

Este sistema genera una distorsión de imagen y sonido sencilla, muy conocida por la imagen codificada que emitía Canal + en sus años de emisión terrestre. Este sistema se utilizó mayoritariamente en transmisión analógica.

Sucesivas revisiones (también conocidas como parches de seguridad) llevaron a implantar el uso de varias claves de forma iterativa, pero no simultánea, lo que permitía mayor dinamismo en el cambio de las claves, de forma que se dificultaban los accesos no deseados a la señal. El sistema entró en decadencia debido a los continuos ataques de la piratería, dejando la codificación de la señal prácticamentecomo un sistema abierto, con una decodificación prácticamente trivial, y sucesivos parches de seguridad no eran capaces de controlar ni detener el pirateo de señal.

Para explotar los fallos de seguridad del sistema Nagra+, se utilizaron unas tarjetas emuladoras, situándolas en el lugar de las originales se conseguía controlar la decodificación condicional, mediante el uso de las excepciones de software que proporciona el sistema nagra, haciendo posible ejecutar cualquier instrucción en el decodificador original de la empresa. Las claves de la forma antes señalada se introducían en los chip de la tarjeta consiguiendo visualizar la señal. También existían programas en la red que permitían a los poseedores de un PC con tarjeta sintonizadora de televisión analógica el descodificar la señal Nagra+ y verla en su ordenador sin necesidad de descodificadores.

 Nagravisión 1 y 2

Para el salto a la tecnología digital Kudelski Corporation mejoró y amplió el sistema para dar lugar a Nagravisión 1. Este sistema de manera similar a Nagra+ usa claves de ocho pares de dígitos, pero debido al tipo de tecnología de transmisión (digital vs analógica) ya no se muestra en pantalla ningún tipo de patrón. De esta manera se conseguía eliminar los ataques por fuerza bruta.

Tras el descubrimiento de los múltiples fallos de seguridad de las tarjetas de Nagravisión 1, Kudelski Corporation se embarcó en la creación de un sistema nuevo para mejorar la seguridad del acceso condicional, pero al mismo tiempo también se exigió la compatibilidad de los equipos anteriores; al principio se dio lugar a una época durante la cual Nagra 2 parecía impenetrable, aunque luego se comprobó que en realidad era una modificación del sistema Nagra 1, en vez de un sistema nuevo.

Nagravisión 2 consiste Esto supuso un gasto enorme para las plataformas de televisión, ya que tenían que enviar nuevas tarjetas a todos y cada uno de sus abonados, que se contaban por millones, estas tarjetas hacían uso de un nuevo firmware para el decodificador y el nuevo sistema de acceso condicional, al introducir la nueva tarjeta se instalaban ambos, siendo este proceso realmente sencillo para el usuario.

Después de analizar Nagra 2 se observó que introducir una tarjeta emuladora en el sistema ya no era posible, porque el software del decodificador original de la plataforma se encargaba de hacer comprobaciones de alta seguridad en la tarjeta. De aquí surgió la idea de sustituir el decodificador por otro de similares características, pero con un software modificado, surgiendo aquí el concepto de lo que los expertos del pirateo llaman Emu, que es el software que emula ser un decodificador original pero que permite el acceso a todas las señales de televisión que pasen por él. En este caso, las claves de doble longitud que las de nagra 1 se introducían en los menús contextuales del decodificador, permitiendo así acelerar el proceso.

Recientemente se desarrollaron las Emu automáticas, que calculaban ellas mismas las claves necesarias para el visionado, logrando una emulación completa de los sistemas originales. Esto fue la gota que colmo el vaso, dejando en evidencia de nuevo a Kudelski Corporation y solicitando muchas plataformas de televisión por satélite la implantación de una tecnología impenetrable de una vez por todas.

 Nagravisión 3
Es el novedoso sistema propuesto por la compañía Kudelski Group, existen muy pocos datos sobre este nuevo sistema, ya que aún nadie ha sido capaz de penetrarlo, desde que fue implantado por TV Cabo a finales de 2007 y por Canal + en diciembre de 2007 numerosos colectivos de piratas han afirmado tener la especificación del sistema y por tanto el acceso a él, pero hasta hoy nadie ha podido comprobar estas afirmaciones.

Sólo hay algunos datos que parecen estar claros, Nagra 3 utiliza un sistema de claves de longitud doble que Nagra 2, por lo que estaríamos hablando de treinta y dos pares de dígitos hexadecimales, lo que supone un cifrado de un nivel extremadamente alto, siendo éste un dato a favor de la seguridad del sistema pero también en contra, porque aceptar esta suposición indicaría que el sistema comete el mismo error que Nagra 2 y se basa en el sistema anterior.

Poco se sabe de este sistema, ya que el método utilizado para su estudio es el análisis de las nuevas tarjetas que la plataforma envía a sus abonados, sabiendo que contienen la descripción del nuevo sistema a utilizar.
El único dato relevante que se tiene es que está basado en Nagra 2, por lo que sus puntos débiles continúan siendo los mismos pero con un nivel superior de seguridad y algunos de los errores anteriores corregidos.

 Errores en la seguridad de Nagravisión
Hasta la fecha no hay ningún error conocido en el sistema Nagra 3, pero todo indica que mostrará errores del mismo tipo que las versiones anteriores. Nagravisión incorpora la gestión de excepciones por software, lo que permite detener el programa principal y ejecutar código en zonas de memoria que no estaba previsto, situación que se aprovecha para ejecutar código malintencionado que permita saltar los sistemas de seguridad planteados por la compañía Kudelski.

 Otras aplicaciones de Nagravisión
Aparte del típico sistema conocido por todos basado en una antena parabólica, un decodificador y un televisor, existen otras formas de aplicación para visualizar la señal que un abonado paga.

 **Tarjetas PC-Sat**

Son tarjetas para ordenador, habitualmente conectadas por puerto PCI, aunque también existen en formato USB. Estas tarjetas hacen el mismo trabajo que el decodificador y se conectan a una antena parabólica y a un televisor. Evidentemente, es ilegal utilizarlas si no se paga un abono a la plataforma que se descodifica.

 **Card sharing**

 Otros sistemas de acceso condicional
Seca Mediaguard (conocido como Seca), Seca 2, Seca 3, PowerVU, Viaccess, Viaccess 2, Irdeto, Irdeto 2, Cryptoworks, Betacrypt, Conax, DSS Videoguard. Son algunos de los muchísimos medios de control de las transmisiones de televisión por satélite.

 Véase también
 Pago por visión

 Enlaces externos
 http://www.nagra.com
 Markus Kuhn: Explica el ataque a Nagravision 1
