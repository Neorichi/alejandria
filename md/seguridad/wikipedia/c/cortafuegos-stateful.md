---
type: Artículo de enciclopedia
title: Cortafuegos stateful
description: "En informática, un cortafuegos stateful (cualquier firewall que realiza la inspección de estado de paquetes (SPI) o la inspección de estado) es un cortafuegos que realiza un seguimiento del estado de las conexiones de …"
resource: https://es.wikipedia.org/wiki/Cortafuegos_stateful
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cortafuegos_stateful"}
license: CC BY-SA 4.0
id: eswiki-Cortafuegos_stateful
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cortafuegos stateful

En informática, un **cortafuegos stateful** (cualquier firewall que realiza la inspección de estado de paquetes (SPI) o la inspección de estado) es un cortafuegos que realiza un seguimiento del estado de las conexiones de red (por ejemplo, flujos TCP, comunicaciones UDP) que viajan a través de él. El cortafuegos está programado para distinguir paquetes legítimos para diferentes tipos de conexiones. Sólo los paquetes que coincidan con una conexión activa conocida serán permitidos por el firewall; los otros serán rechazados.

La inspección de estado, también conocida como  filtrado de paquetes dinámico, es una característica de seguridad a menudo incluida en las redes empresariales. *Check Point Software* introdujo la inspección de estado en el uso de su FireWall-1 en 1994

 Historia
Antes del advenimiento de los firewalls de estado, había cortafuegos sin estado, un cortafuegos que trataba a cada trama de red (o paquete) de manera aislada. Tales filtros de paquetes operaban en la capa de red (capa 3) y funcionaban de manera más eficiente, ya que sólo comprobaban la  cabecera de un paquete. Un inconveniente de los filtros de paquetes puros es que son sin estado; no tienen memoria de los paquetes anteriores y esto los hace vulnerables a los ataques de suplantación. Un firewall así no tiene forma de saber si un paquete dado es parte de una conexión existente, está tratando de establecer una conexión nueva, o es sólo un paquete de virus. Los cortafuegos modernos son conscientes de la conexión (o conscientes del estado), ofreciendo a los administradores de red un control más preciso del tráfico de red.

El ejemplo clásico de una operación de red que puede fallar con un cortafuegos sin estado es el protocolo de transferencia de archivos (FTP). Por diseño, estos protocolos deben ser capaces de abrir conexiones arbitrarias a los puertos altos para funcionar correctamente. Desde un cortafuegos sin estado no se tiene manera de saber que el paquete destinado a la red protegida (al puerto de destino de algunos de acogida 4970, por ejemplo) es parte de una sesión FTP legítimo, caerá el paquete. Los cortafuegos de estado con la aplicación de Inspección resuelven este problema mediante el mantenimiento de una tabla de conexiones abiertas, la inspección de la carga útil de algunos paquetes y asociar inteligentemente nuevas peticiones de conexión con conexiones legítimas existentes.

Los primeros intentos de cortafuegos que se han producido funcionan en la capa de aplicación, que es la parte más alta del modelo OSI de siete capas. Este método requiere cantidades exorbitantes de potencia de cálculo y no se utiliza habitualmente en las implementaciones modernas

 Descripción

Un cortafuegos de estado mantiene un registro del estado de las conexiones de red (tales como flujos TCP o UDP) de comunicación y es capaz de mantener atributos significativos de cada conexión en la memoria. Estos atributos se conocen colectivamente como el estado de la conexión, y pueden incluir detalles como las direcciones IP y los puertos que participan en la conexión y los números de secuencia de los paquetes que atraviesan la conexión. La inspección de estado monitoriza los paquetes entrantes y salientes en el tiempo, así como el estado de la conexión, y almacena los datos en tablas de estados dinámicos. Se evalúan estos datos acumulativos, de manera que las decisiones de filtrado no solamente se basan en reglas definidas por el administrador, sino también en el contexto que ha sido construido por las conexiones anteriores, así como los paquetes anteriores que pertenecen a la misma conexión.

La comprobación de CPU más intensiva se realiza en el momento de la configuración de la conexión. Las entradas se crean sólo para las conexiones TCP o flujos UDP que satisfacen una política de seguridad definida. Después de eso, todos los paquetes (por sesión) que se procesan rápidamente porque es simple y rápido para determinar si pertenece a una, sesión de pre-seleccionados existente. Los paquetes asociados con estas sesiones se les permite pasar a través del firewall. Sesiones que no coinciden con ninguna política se les niega, como paquetes que no coinciden con una entrada de la tabla existente.

Con el fin de evitar que la tabla de estado se llene, las sesiones tendrán tiempo de espera si no hay tráfico durante un período determinado. Estas conexiones antiguas se eliminan de la tabla de estado. Por lo tanto, muchas aplicaciones envían mensajes keepalive periódicamente con el fin de detener un servidor de seguridad caiga la conexión durante los períodos de ningún usuario-actividad, aunque algunos cortafuegos pueden ser instruidos para enviar estos mensajes para las aplicaciones.

Dependiendo del protocolo de conexión, mantener el estado de una conexión es más o menos complejo para el cortafuegos. Por ejemplo, TCP es de por sí un protocolo con estado como conexiones se establecen con una de tres vías ("SYN, SYN-ACK, ACK") y terminaron con un "ACK FIN" de cambio. Esto significa que todos los paquetes con "SYN" en su cabecera recibida por el servidor de seguridad se interpretan para abrir nuevas conexiones. Si el servicio solicitado por el cliente está disponible en el servidor, se responde con un paquete "SYN-ACK", que también hará un seguimiento del firewall. Una vez que el servidor de seguridad y luego recibe la respuesta "ACK" del cliente, transfiere la conexión con el estado "ESTABLISHED" como la conexión ha sido autenticada bidireccional. Esto permite el seguimiento de los paquetes futuros a través de la conexión establecida. Al mismo tiempo, el firewall descarta todos los paquetes que no están asociados con una conexión existente registrada en su tabla de estado (o paquetes "SYN"); la prevención de conexiones no solicitadas protege la máquina contra piratería de sombrero negro.

Otros protocolos de conexión, es decir, UDP e ICMP, no se basan en conexiones bidireccionales como TCP, por lo que un servidor de seguridad con estado algo menos seguro. Con el fin de realizar un seguimiento de un estado de conexión en estos casos, un servidor de seguridad debe transferir sesiones al estado ESTABLISHED después de ver el primer paquete válido. A continuación, sólo se puede realizar un seguimiento de la conexión a través de direcciones y puertos de origen y destino de los siguientes paquetes. A diferencia de las conexiones TCP, que se pueden cerrar por una ", ACK FIN" de cambio, estos protocolos sin conexión permiten una sesión para terminar solamente por tiempo de espera. Esto, por ejemplo, hace UDP vulnerables a perforación UDP.

Al mantener un registro del estado de la conexión, firewalls proporcionan eficiencia añadido en términos de inspección de paquetes. Esto se debe a las conexiones existentes del firewall sólo tiene que comprobar la tabla de estado, en lugar de revisar el paquete contra el conjunto de reglas del cortafuegos, que puede ser extensa. Además, en el caso de un partido con la tabla de estado, el cortafuegos no necesita realizar una inspección profunda de paquetes.

 Filtros de la capa de nivel de aplicación

El filtrado de paquetes por sí sola no es considerado como proporcionar suficiente protección. Con el fin de bloquear de manera efectiva peer-to-peer-relacionados tráfico de la red, lo que se necesita es un firewall que hace el filtrado de aplicaciones, que puede considerarse como una extensión de la inspección de estado de paquetes. Inspección de estado de paquetes puede determinar qué tipo de protocolo se está enviando más de cada puerto, pero los filtros de nivel de aplicación ver lo que un protocolo está siendo utilizado para. Por ejemplo, un filtro a nivel de aplicación podría ser capaz de decir la diferencia entre el tráfico HTTP utilizado para acceder a una página Web y el tráfico HTTP utilizado para compartir archivos, mientras que un servidor de seguridad que sólo va a realizar el filtrado de paquetes trataría todo el tráfico HTTP por igual.

Los Firewalls de capa de aplicación son generalmente más lentos que los de inspección de estado. Los firewalls a nivel de aplicación se implementan a veces utilizando proxies de aplicación. Se establecen dos conexiones TCP: una entre la fuente de paquetes y el firewall, otro entre el firewall y el destino del paquete. Los proxies de aplicación interceptan los paquetes que llegan en nombre del destino, examinan la carga útil de la aplicación y a continuación, transmiten los paquetes permitidos hasta el destino. Los datos sospechosos se caen y el cliente y el servidor no se comunican directamente entre sí. Los Proxies implican necesariamente más protocolo de pila sobrecarga que inspeccionar paquetes en la capa de red. Además, debido a un proxy único se requiere para cada aplicación, los cortafuegos proxy puede ser menos flexible y más lento para actualizar de cortafuegos de inspección de estado. Sin embargo, debido a los proxies a nivel de aplicación son consciente de las aplicaciones, los proxies pueden manejar más fácilmente protocolos complejos como H.323 o SIP, que se utilizan para la videoconferencia y VoIP (Voz sobre IP).

 Trampas
 Vulnerabilidades
Existe el riesgo de que las vulnerabilidades en los decodificadores de protocolo individuales podrían permitir a un atacante hacerse con el control sobre el servidor de seguridad. Esta preocupación pone de relieve la necesidad de mantener actualizado el software del cortafuegos.

Algunos cortafuegos también plantean la posibilidad de que los hosts individuales pueden ser engañados para solicitar conexiones externas. Esta posibilidad sólo puede ser completamente eliminada auditando el software del host. Algunos servidores de seguridad pueden ser derrotados de esta manera simplemente viendo una página web (ya sea con Javascript activado, o después de hacer clic en un botón).

Fuente
