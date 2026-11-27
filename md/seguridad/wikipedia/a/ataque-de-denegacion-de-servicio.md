---
type: Artículo de enciclopedia
title: Ataque de denegación de servicio
description: "En seguridad informática, un ataque de denegación de servicio, llamado también ataque DoS (por sus siglas en inglés, denial of service), es un ataque a un sistema de computadoras o red que causa que un servicio o …"
resource: https://es.wikipedia.org/wiki/Ataque_de_denegación_de_servicio
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Ataque_de_denegación_de_servicio"}
license: CC BY-SA 4.0
id: eswiki-Ataque_de_denegación_de_servicio
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Ataque de denegación de servicio

En seguridad informática, un **ataque de denegación de servicio**, llamado también ataque **DoS** (por sus siglas en inglés, ***d**enial **o**f **s**ervice*), es un ataque a un sistema de computadoras o red que causa que un servicio o recurso sea inaccesible a los usuarios legítimos. Normalmente provoca la pérdida de la conectividad con la red por el consumo del ancho de banda de la red de la víctima o sobrecarga de los recursos computacionales del sistema atacado.

La gama de ataques varía ampliamente, desde inundar un servidor con millones de solicitudes para reducir su rendimiento, abrumarlo con una cantidad sustancial de datos no válidos, hasta enviar solicitudes con una dirección IP ilegítima.

Un ejemplo notable de ello se produjo el 27 de marzo de 2013, cuando el ataque de una empresa a otra inundó la red de correos basura provocando una ralentización general de Internet e incluso llegó a afectar a puntos clave como el nodo central de Londres.

Los ataques DoS se generan mediante la saturación de los puertos con múltiples flujos de información, haciendo que el servidor se sobrecargue y no pueda seguir prestando su servicio. Por eso se le denomina *denegación*, pues hace que el servidor no pueda atender la cantidad enorme de solicitudes. Esta técnica es usada por los *crackers* o piratas informáticos para dejar fuera de servicio servidores objetivo. A nivel global, este problema ha ido creciendo, en parte por la mayor facilidad para crear ataques y también por la mayor cantidad de equipos disponibles mal configurados o con fallos de seguridad que son explotados para generar estos ataques. Se ve un aumento en los ataques por reflexión y de amplificación por sobre el uso de botnets.

Una ampliación del ataque DoS es el llamado **ataque de denegación de servicio distribuido**, también llamado **DDoS** (por sus siglas en inglés, ***D**istributed **D**enial **o**f **S**ervice*) el cual se lleva a cabo generando un gran flujo de información desde varios puntos de conexión hacia un mismo punto de destino. La forma más común de realizar un DDoS es a través de una red de bots, siendo esta técnica el ciberataque más usual y eficaz por su sencillez tecnológica.

En ocasiones, esta herramienta ha sido utilizada como un buen método para comprobar la capacidad de tráfico que un ordenador puede soportar sin volverse inestable y afectar los servicios que presta. Un administrador de redes puede así conocer la capacidad real de cada máquina.

 Historia de los ataques
Uno de los primeros ataques maliciosos fue hecho por MafiaBoy, quien perpetró un ataque DDos con el mismo nombre, un ataque a la universidad de Minnesota con 114 ordenadores infectados con un código malicioso llamado Trin00

Aunque el primer ataque fue uno llamado Panix, el tercer proveedor de servicios de internet más antiguo del mundo, fue el objetivo del primer ataque DoS. El 6 de septiembre de 1996, Panix fue objeto de un ataque de inundación SYN que provocó la caída de sus servicios durante varios días mientras los proveedores de hardware de red, en particular Cisco, encontraban una defensa adecuada.

 Ataques más potentes
El 1 de marzo de 2018, GitHub fue golpeado con un ataque de 1,35 terabits por segundo, para que 4 días después, el 5 de marzo de 2018, Arbor Networks fuera víctima de 1,7 terabits por segundo. Ya en febrero de 2020, Amazon Web Services fue atacado por 2,3 terabits por segundo.

Aunque el récord se lo lleva Google Cloud, con 2,54 terabits por segundo, el ataque ocurrió en septiembre de 2017.

 Ataque a Telegram, en Hong Kong
Durante las protestas contra la extradición de Hong Kong en junio de 2019, la aplicación de mensajería Telegram fue objeto de un ataque DDoS, destinado a evitar que los manifestantes la usaran para coordinar las protestas. Los fundadores de Telegram han declarado que este ataque parece ser el de un "tamaño estatal" debido a que las direcciones IP que se originan en China.

 DDoS a Wikipedia
El 6 y 7 de septiembre de 2019, Wikipedia fue derribada por un ataque DDoS en Alemania y algunas partes de Europa. Los usuarios de las redes sociales, esperando a que los servidores de Wikipedia volvieran, crearon un "hashtag" en Twitter llamado: #WikipediaDown, en un esfuerzo para llamar la atención del público.

 Ataques a Andorra Telecom
El 21 de enero de 2022, Andorra Telecom, el único proveedor de internet de Andorra, sufrió un ataque de DDoS por la noche mientras varios streamers se encontraban transmitiendo y participando de un evento de Minecraft basado en El juego del calamar. Debido a esto, suspendieron el evento para el día siguiente. Sin embargo, hubo un segundo ataque por la tarde del sábado 22 de enero, lo que provocó que dichos streamers quedaran descalificados de dicho evento para darle continuidad al mismo. El lunes 24 de enero, Andorra Telecom sufrió un tercer ataque. Se presume que dichos ataques se habrían hecho para perjudicar a los creadores de contenido que viven en el principado. Al ser el único proveedor del país, todos sus usuarios se quedaron sin servicio de internet, además de los youtubers y streamers que estaban transmitiendo en ese entonces, entre los que figuran nombres conocidos como El Rubius o AuronPlay.

 "Síntomas" de un ataque de denegación de servicio
El Equipo de preparación para emergencias informáticas de los Estados Unidos (US-CERT) ha identificado los "síntomas" de un ataque de denegación de servicio, los cuales son:

• Red inusualmente muy lenta, especialmente a la hora de navegar por internet o abrir archivos

• Lentitud o indisponibilidad de ingresar a alguna página web

 Técnicas de ataque

Un ataque de denegación de servicio impide el uso legítimo de los usuarios al usar un servicio de red. El ataque se puede dar de muchas formas. Pero todas tienen algo en común: utilizan la familia de protocolos TCP/IP para conseguir su propósito.

Un ataque DoS puede ser perpetrado de varias formas. Aunque básicamente consisten en:
 Consumo de recursos computacionales, tales como ancho de banda, espacio de disco, o tiempo de procesador.
 Alteración de información de configuración, tales como información de rutas de encaminamiento.
 Alteración de información de estado, tales como interrupción de sesiones TCP (TCP reset).
 Interrupción de componentes físicos de red.
 Obstrucción de medios de comunicación entre usuarios de un servicio y la víctima, de manera que ya no puedan comunicarse adecuadamente.

 Inundación SYN (SYN Flood)
 Principios de TCP/IP
Cuando una máquina se comunica mediante TCP/IP con otra, envía una serie de datos junto a la petición real. Estos datos forman la cabecera de la solicitud. Dentro de la cabecera se encuentran unas señalizaciones llamadas *Flags* (banderas). Estas señalizaciones (banderas) permiten iniciar una conexión, cerrarla, indicar que una solicitud es urgente, reiniciar una conexión, etc. Las banderas se incluyen tanto en la solicitud (cliente), como en la respuesta (servidor).

Para aclararlo, veamos cómo es un intercambio estándar TCP/IP:

1) Establecer Conexión: el cliente envía una Flag SYN; si el servidor acepta la conexión, este debería responderle con un SYN/ACK; luego el cliente debería responder con una Flag ACK.

 1-Cliente --------SYN----->  2 Servidor
 4-Cliente <-----SYN/ACK----  3 Servidor
 5-Cliente --------ACK----->  6 Servidor

2) Resetear Conexión: al haber algún error o pérdida de paquetes de envío se establece envío de Flags RST:

 1-Cliente -------Reset-----> 2-servidor
 4-Cliente <----Reset/ACK---- 3-Servidor
 5-Cliente --------ACK------> 6-Servidor

La inundación SYN envía un flujo de paquetes TCP/SYN (varias peticiones con Flags SYN en la cabecera), muchas veces con la dirección de origen falsificada. Cada uno de los paquetes recibidos es tratado por el destino como una petición de conexión, causando que el servidor intente establecer una conexión al responder con un paquete TCP/SYN-ACK y esperando el paquete de respuesta TCP/ACK (Parte del proceso de establecimiento de conexión TCP de 3 vías). Sin embargo, debido a que la dirección de origen es falsa o la dirección IP real no ha solicitado la conexión, nunca llega la respuesta.

Estos intentos de conexión consumen recursos en el servidor y copan el número de conexiones que se pueden establecer, reduciendo la disponibilidad del servidor para responder peticiones legítimas de conexión.

SYN cookies provee un mecanismo de protección contra Inundación SYN, eliminando la reserva de recursos en el host destino, para una conexión en momento de su gestión inicial.

 Inundación ICMP (ICMP Flood)

Es una técnica DoS que pretende agotar el ancho de banda de la víctima. Consiste en enviar de forma continuada un número elevado de paquetes *ICMP* *Echo request* (ping) de tamaño considerable a la víctima, de forma que esta ha de responder con paquetes *ICMP* *Echo reply* lo que supone una sobrecarga tanto en la red como en el sistema de la víctima.

Dependiendo de la relación entre capacidad de procesamiento de la víctima y el atacante, el grado de sobrecarga varía, es decir, si un atacante tiene una capacidad mucho mayor, la víctima no puede manejar el tráfico generado.

 SACKPanic

Manipulando el Tamaño Máximo de Segmento y la Retransmisión (redes de datos),  o SACK, pueden ser usados de manera remota para causar un ataque de denegación de servicios por medio de un desborde de entero en el núcleo Linux, incluso causando un Kernel panic. Jonathan Looney descubrió las CVE-2019-11477, CVE-2019-11478, CVE-2019-11479 el 17 de junio de 2019.

 SMURF

Existe una variante a *ICMP Flood* denominado Ataque Smurf que amplifica considerablemente los efectos de uno o varios ataques ICMP.

Existen tres partes en un Ataque Smurf: El atacante, el intermediario y la víctima (comprobaremos que el intermediario también puede ser víctima).

En el ataque Smurf, el atacante dirige paquetes ICMP tipo "*echo request*" (ping) a una dirección IP de broadcast, usando como dirección IP origen, la dirección de la víctima (Spoofing). Se espera que los equipos conectados respondan a la petición, usando *Echo reply*, a la máquina origen (víctima).

Se dice que el efecto es amplificado, debido a que la cantidad de respuestas obtenidas, corresponde a la cantidad de equipos en la red que puedan responder. Todas estas respuestas son dirigidas a la víctima intentando colapsar sus recursos de red.

Como se dijo anteriormente, los intermediarios también sufren los mismos problemas que las propias víctimas.

 Inundación UDP (UDP Flood)
Este ataque consiste en el hecho de generar grandes cantidades de paquetes UDP contra la víctima elegida. Debido a la naturaleza sin conexión del protocolo UDP, este tipo de ataques suele venir acompañado de IP spoofing.

Es usual dirigir este ataque contra máquinas que ejecutan el servicio Echo, de forma que se generan mensajes Echo de un elevado tamaño.

 Ataque Teardrop
En un ataque Teardrop, los paquetes IP se dividen en fragmentos más pequeños. La reasamblea de estos fragmentos puede provocar bloqueos debido a un error del sistema que no puede ensamblar correctamente los paquetes superpuestos y grandes. Esta dificultad en la reasamblea tiene el potencial de causar bloqueos del sistema.

 Incidencias
A lo largo de su historia, los ataques DoS y DDoS han presentado una serie de incidencias, de las cuales las más importantes han sido las siguientes:
 Desde principios de 2014, el uso de ataques basados en protocolos UDP ha aumentado significativamente. Actualmente ocurren importantes incidentes con ataques basados en CHARGEN, NTP y DNS. De acuerdo al informe de DDOS de Prolexic de Q1 2014, el ancho de banda promedio de los ataques creció en un 39% respecto a los ataques del 2013. Respecto del mismo trimestre del 2013, hubo un 47% de aumento en la cantidad de ataques y un 133% de crecimiento del ancho de banda punta (*peak*) de los ataques.

 El 21 de octubre de 2016 ocurrieron, principalmente en Estados Unidos, los ataques más masivos de la última década y se vieron afectadas aplicaciones y páginas web como Twitter, Spotify, Amazon, Netflix y la versión digital de *The New York Times*.

 El 20 de diciembre de 2018 la Oficina Federal de Investigación en trabajo conjunto con la Agencia Nacional contra el Crimen del Reino Unido (*National Crime Agency* —NCA—), la policía nacional neerlandesa (*Law enforcement in the Netherlands*), el Departamento de Justicia de los Estados Unidos y varias compañías tecnológicas (Cloudflare, Flashpoint y Google, entre otras) procedió a la incautación de 15 dominios web dedicados a vender grandes ataques de DDoS mediante sus instalaciones. Los procedimientos fueron hechos al amparo de una orden de un juez federal en California. Destacan los 200 mil ataques hechos por *Downthem* (*‘ponlos fuera de línea’* en idioma castellano) con más de dos mil clientes, aunque se queda pequeño comparado por el dominio incautado *webstresser* en abril de 2018, desde donde se realizaron más de 6 millones de ataques DDoS.

 Véase también

 Referencias

 Enlaces externos
 Syn Flood, que es y como mitigarlo
 Intentando detener un DDoS
