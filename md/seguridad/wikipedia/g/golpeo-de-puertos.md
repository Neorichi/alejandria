---
type: Artículo de enciclopedia
title: Golpeo de puertos
description: El golpeo de puertos (del inglés port knocking) es un mecanismo para abrir puertos externamente en un firewall mediante una secuencia preestablecida de intentos de conexión a puertos que se encuentran cerrados.
resource: https://es.wikipedia.org/wiki/Golpeo_de_puertos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Golpeo_de_puertos"}
license: CC BY-SA 4.0
id: eswiki-Golpeo_de_puertos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Golpeo de puertos

El **golpeo de puertos** (del inglés *port knocking*) es un mecanismo para abrir puertos externamente en un firewall mediante una secuencia preestablecida de intentos de conexión a puertos que se encuentran cerrados.
Una vez que el firewall recibe una secuencia de conexión correcta, sus reglas son modificadas para permitir al host que realizó los intentos conectarse a un puerto específico.

El propósito principal del **golpeo de puertos** es prevenir un escanéo de puertos por parte de un atacante que busca posibles servicios vulnerables. Como los mismos solo se abren ante un golpeo de puertos correcto. Normalmente los puertos donde se brindan los servicios se muestran aparentemente cerrados.

Por lo general este mecanismo se implementa configurando un servicio para que revise la bitácora o *log* del firewall para detectar esta secuencia de intentos de conexión. Otra forma es tener un proceso examinando paquetes con alguna interfaz de captura de paquetes, pero esto tiene que hacerse en puertos TCP que se encuentren "abiertos".

El mayor uso del golpeo de puertos, es para determinar acceso al puerto 22, el puerto del Secure Shell (SSH). El golpeo en cuestión es similar a un *handshake* secreto. La complejidad del mismo puede variar desde una simple lista ordenada de intentos de conexión a puertos TCP, UDP, ICMP u otro protocolo; hasta un hash basado en la dirección origen, tiempo y otros factores, el cual determinará cuáles serán los puertos a golpear.

Para la implementación, la idea es que el cliente tenga una aplicación que ejecute el golpeo antes de acceder al servidor de manera normal. Un servicio se encuentra escuchando en la máquina donde está el firewall los paquetes que llegan a la misma. El utilitario del cliente, responsable de realizar el golpeo de los puertos puede ser desde un sencillo programa que ejecute comandos de ping, hasta un complejo programa generador de un hash.

Generalmente no hay ninguna indicación cuando un usuario ejecuta una secuencia errónea de PK. Simplemente el puerto que se esperaba estuviese abierto al final de la secuencia, no lo está. Ningún paquete es enviado al usuario en ningún momento.

A pesar de que esta técnica no ha sido ampliamente adoptada por la comunidad, ha sido integrada en los rootkits más recientes.

 Cómo funciona en teoría

 El cliente no puede conectarse a una aplicación que se encuentra escuchando en el puerto *n*.
 El cliente intenta conectarse a un conjunto predefinido de puertos en secuencia, enviando ciertos paquetes. El cliente tiene conocimiento previo del servicio de golpeo de puertos y su configuración, pero no recibe ninguna respuesta durante esta fase ya que las reglas del firewall no lo permiten.
 El servicio de port knocking intercepta los intentos de conexión y los decodifica para verificar un golpeo auténtico. El servidor realiza tareas específicas basadas en el golpeo de puertos, como abrir otros puertos para el cliente.
 El cliente se conecta al puerto n recientemente abierto.

 Beneficios del golpeo de puertos
Considere un atacante que no posea conocimiento previo de la secuencia de golpeo de puertos, aún la más simple de las secuencias requeriría un esfuerzo enorme para ser descubierta por fuerza bruta. Una simple secuencia de tres golpes (Ej. puertos 1000, 2000, 3000) requeriría que un atacante probara cada combinación de tres puertos en un rango de 1-65535 puertos y luego que escaneara cada puerto para ver si alguno se encuentra abierto.

Esto es igual 655354 paquetes para lograr obtener y detectar un puerto abierto. Esto equivale a 18,445,618,199,572,250,625 o 18 trillones de paquetes. Como promedio tomaría 9 trillones de paquetes para poder obtener un único puerto abierto, mediante una secuencia simple de tres puertos TCP. Esto se vuelve mucho más impracticable cuando se utiliza alguna técnica para limitar los intentos de golpeo o cuando se utiliza un hash criptográfico para obtener la secuencia de golpeo.

Cuando un golpeo de puertos se ha utilizado para abrir satisfactoriamente un puerto, las reglas del firewall generalmente se modifican para abrir el puerto únicamente a la IP que ejecutó el golpeo. Esto es similar a tener una whitelist para permitir a las IP que se encuentren en ella acceder al servicio, solo que más dinámico. Un usuario autorizado, situado en cualquier lugar del mundo será capaz de abrir el puerto de su interés sin ayuda del administrador del servidor. Podría ser capaz de cerrar el puerto una vez que ha terminado, o el sistema podría tener algún mecanismo de timeout para cerrar conexiones que se encuentren inactivas por un tiempo determinado.

Dado el comportamiento *stateful* del golpeo de puertos, distintos usuarios de diferentes direcciones IP de origen pueden simultáneamente encontrarse realizando diferentes golpeos de puertos. Por lo tanto, es posible que un usuario genuino que conozca el golpe correcto atraviese el firewall, aun en el medio de un ataque desde múltiples direcciones IP. Para todas estas los puertos aun aparecen cerrados y no hay ninguna indicación de que existan otros usuarios que hayan abierto satisfactoriamente un puerto y estén utilizando el servicio ofrecido en el mismo.

Utilizar hash criptográficos para realizar el golpeo de puertos significa que ni siquiera husmeando en el tráfico de red sería posible que un atacante descubriera la secuencia del golpe o pudiera repetir secuencias anteriores.
Aun cuando alguien pudo adivinar, robar o husmear la secuencia y acceder satisfactoriamente a un puerto, todavía es necesario sobrepasar los mecanismos de seguridad del servicio al cual se accede en ese puerto.

El software requerido es mínimo, tanto en el cliente como en el servidor. De hecho, puede ser implementado como un simple script de shell o un archivo batch de Windows. Con respecto al consumo de recursos, el overhead relacionado con el consumo de CPU, memoria y tráfico de red es despreciable. Los servicios de golpeo de puertos tienden a ser simples de tal manera que las vulnerabilidades son obvias y el código es fácilmente auditable.

El sistema es adaptable por completo y no se encuentra limitado a abrir determinados puertos o puede que no se abra ninguno. Usualmente una secuencia está asociada con una acción, como correr un script, de tal manera que si se ejecuta la secuencia, se corre el script. Diversas secuencias pueden ser utilizadas en un mismo servidor para realizar diferentes acciones, como abrir diferentes puertos.

Dado el hecho de que los puertos aparecen cerrados hasta que un usuario que conoce la secuencia correcta de golpeo la ejecuta, el golpeo de puertos puede servir no solo para evitar ataques de fuerza bruta o de diccionario para descubrir un password, sino también para posibles vulnerabilidades en el protocolo de comunicación o en el servicio. Si se encuentra una vulnerabilidad que pueda comprometer la seguridad de un servicio, el golpeo de puertos puede evitar que la seguridad de ese servicio se vea comprometida, hasta que se realice la actualización del software de ese servicio. Por ello intentos aleatorios realizados por virus o worms tratando de explotar una vulnerabilidad conocida quedan descartados de antemano.
Aunque no es una protección completa, el golpeo de puertos brinda otro nivel de defensa contra los ataques aleatorios y si es implementado correctamente, puede evitar determinados ataques dirigidos.

El golpeo de puertos está usualmente mal visto dentro del mundo de la seguridad, dado que las primeras implementaciones consistían básicamente de una secuencia de puertos que debía ser realizada en un orden determinado. A pesar de ello los sistemas más modernos de golpeo de puertos son mucho más complejos, algunos utilizando hashes criptográficos, los cuales brindan alta seguridad y evitan los ataques más comunes (como husmeo de paquetes). Adicionalmente los sistemas de golpeo de puertos pueden incluir listas negras, listas blancas y respuestas dinámicas a los ataques. Sin embargo, aun las secuencias más simples pueden controlar el acceso a un sistema antes de que los atacantes puedan ejecutar su cometido contra algún servicio, que de por sí consume recursos como memoria o tiempo de CPU.

Además, el golpeo de puertos, por lo general, no conlleva una degradación del nivel de seguridad global de un sistema. De hecho, provee un nivel más de seguridad por un coste computacional mínimo. En el peor de los escenarios, el golpeo de puerto introduce un problema nuevo de seguridad o baja el nivel de seguridad a causa de la compensación de riesgos.

 Consideraciones de Seguridad

El sistema es totalmente personalizable y no está limitado exclusivamente a la apertura y cierre de puertos. Normalmente la descripción de una secuencia de "knock" esta atada a una acción, como ser la ejecución de un shell script. Una vez que la secuencia es detectada por el demonio de port knocking, el script asociado es ejecutado. Éste script podría por ejemplo agregar reglas en el firewall para abrir puertos. Muchos "knocks" distintos pueden ser utilizados en la misma máquina para realizar diferentes acciones, como abrir o cerrar diferentes puertos.

Como los puertos aparecen cerrados hasta que un usuario realiza los "knocks" correctos, el port knocking ayuda tanto a reducir ataques de fuerza bruta de contraseñas y sus logs asociados así como la explotación de vulnerabilidades en los protocolos. Si un nuevo exploit capaz de comprometer los demonios de SSH fuera descubierto, tener implementado "port knocking" en el puerto de dicho demonio podría significar que este no sea comprometido antes de que fuese actualizado. Solo los usuarios autorizados tendrían la secuencia de "knock" por lo que solo dichos usuarios serían capaces de contactar al servidor SSH. Asimismo, intentos aleatorios de explotar la vulnerabilidad sobre el servidor SSH por parte de gusanos y virus no podrán siquiera alcanzarlo, dando al administrador la oportunidad de actualizar o parchear el programa. Aunque no es una protección completa, "port knocking" brinda un nivel más de defensa contrataques aleatorias, y con una correcta implementación, podría incluso detener ataques determinados y dirigidos.

El Port knocking generalmente genera cierta indiferencia en el mundo de la seguridad, esto se debe a que sus primeras implementaciones básicamente consistían en un número de puertos que debían ser golpeados en orden. Sin embargo, los mejores sistemas de port knocking modernos son mucho más complejos, y algunos incluso utilizan hashes criptográficos altamente seguros para anular los ataques más comunes (como ser sniffeo de paquetes y reenvío de paquetes). Adicionalmente, los sistemas de port knocking pueden incluir listas negras, listas blancas y respuestas dinámicas a ataques antes de que los atacantes sean capaces de atacar un servicio que asigne memoria, acceda a tiempo de CPU o a otros recursos significantes. También actúa como barrera a intentos de fuerza bruta, explotación automática de vulnerabilidades, etc.

El port knocking generalmente no disminuye la seguridad de un sistema. De hecho, proporciona una capa extra de seguridad con una sobrecarga mínima. (...)

 Desventajas

Si por alguna u otra razón el demonio de port knocking se detuviera, se tendrá un sistema incomunicado. Esto también es conocido como un único punto de fallo. Sin embargo, para mitigar este problema, implementaciones modernas de port knocking incluyen un demonio de monitoreo de procesos que reinicia el demonio de port knocking en caso de que este se detenga.

Otro problema es que un atacante podría bloquear cualquier dirección IP conocida (como ser la del administrador) al mandar paquetes con direcciones IP falsas (IP spoofing) a puertos al azar. En comunicaciones entre servidores esto puede ser especialmente dañino ya que las direcciones IP son bien conocidas y no pueden ser cambiadas fácilmente. Esto podría ser evitado utilizando los hashes criptográficos mencionados anteriormente.

También, una consideración importante es que debido a la forma en que TCP/IP enruta los paquetes, existe una posibilidad real de que los paquetes individuales de cada "knock" lleguen fuera de secuencia, o que alguno de ellos sea totalmente descartado. Esto significa que pedidos legítimos pueden potencialmente ser incorrectos a ojos del servidor, y por tanto el cliente deberá encargarse de solucionarlo (por ej. mediante un reenvío).

Usado como una única técnica para asegurar un dispositivo, port knocking se basa en la seguridad por oscuridad; si la secuencia de "knock" se hiciera pública, todos los dispositivos que responden a esa secuencia pueden ser comprometidos. Debido a que los paquetes de red son públicos dentro de la misma red, un capturador de tráfico podría detectar distintos "knocks" desde una única dirección IP seguido de una conexión exitosa y duplicarla. Los archivos de log de dicho dispositivo podrían almacenar la secuencia de "knock" y es por ello que también es otro punto de falla. Estas debilidades pueden ser mitigadas tratando la secuencia de knock como la autenticación de contraseña de un solo uso, modificando la secuencia cada vez que es usada, o combinándola con otro mecanismo de autenticación que no sea vulnerable a ataques de replay (o Man in the Middle).

 Enlaces externos
 PORTKNOCKING - A system for stealthy authentication across closed ports. (archivada)
 Linux Journal: Port Knocking
 Slashdot "Port Knocking" For Added Security
 A Windows implementation of port knocking.
 A new Windows implementation of port knocking: KnockKnock
 A Linux IP Tables implementation of port knocking.
 A simple implementation of port knocking.
 A packet-capture basic simple portknock system for Linux.

 A Netfilter module for port knocking.
