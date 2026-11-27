---
type: Artículo de enciclopedia
title: Escáner de puertos
description: El término escáner de puertos o escaneo de puertos se emplea para designar la acción de analizar por medio de un programa el estado de los puertos de una máquina conectada a una red de comunicaciones.
resource: https://es.wikipedia.org/wiki/Escáner_de_puertos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Escáner_de_puertos"}
license: CC BY-SA 4.0
id: eswiki-Escáner_de_puertos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Escáner de puertos

El término **escáner de puertos** o **escaneo de puertos** se emplea para designar la acción de analizar por medio de un programa el estado de los puertos de una máquina conectada a una red de comunicaciones. Detecta si un puerto está abierto, cerrado, o protegido por un cortafuegos.

Se utiliza para detectar qué servicios comunes está ofreciendo la máquina y posibles vulnerabilidades de seguridad según los puertos abiertos. También puede llegar a detectar el sistema operativo que está ejecutando la máquina según los puertos que tiene abiertos. Es usado por administradores de sistemas para analizar posibles problemas de seguridad, pero también es utilizado por usuarios malintencionados que intentan comprometer la seguridad de la máquina o la red.

Existen varios programas para escanear puertos por la red. Uno de los más conocidos es Nmap, disponible tanto para Linux como Windows.

 Rastreo de puertos TCP SYN scan
Es necesario saber que para establecer una conexión normal se debe primero considerar lo siguiente. En TCP es necesario seguir una negociación de tres pasos. Esta negociación es iniciada con un paquete SYN en la máquina de origen, al cual la máquina de destino responde con un paquete SYN/ACK, el que es finalmente respondido por la máquina que inicia la conexión por un paquete ACK. Una vez que se han cumplido estos pasos, está hecha la conexión TCP.

Un rastreador de puertos envía muchos paquetes SYN a la máquina que se está probando, y mira de qué forma regresan los paquetes para ver el estado de los puertos en el destino, interpretándolos de la siguiente forma:

 Si al enviar un paquete SYN a un puerto específico, el destino devuelve un SYN/ACK, el puerto está abierto y escuchando conexiones.
 En otro caso, si regresa un paquete RST, el puerto está cerrado.
 Por último, si no regresa el paquete, o si se recibe un paquete ICMP Port Unreachable, el puerto está filtrado por algún tipo de cortafuegos.

Haciendo este procedimiento para una lista de , se logra obtener un informe de estado de los puertos de la máquina probada.

 Rastreo de puertos UDP
Aunque el protocolo UDP no está orientado a la conexión, es posible realizar un escaneo. No tiene un paquete SYN como el protocolo TCP, sin embargo si un paquete se envía a un puerto que no está abierto, responde con un mensaje ICMP Port Unreachable. La mayoría de los escáneres de puertos UDP usan este método, e infieren que si no hay respuesta, el puerto está abierto. Pero en el caso de que esté filtrado por un firewall, este método dará una información errónea.

Una opción es enviar paquetes UDP de una aplicación específica, para generar una respuesta de la capa de aplicación. Por ejemplo enviar una consulta DNS.

 Escáneres de puertos en línea
 Escáner en línea de puertos en sistemas IPv6

 Listado de escáneres
 Internautas
 Puertos Abiertos En español, por grupos o personalizados. (Seguridad, Troyanos y servers)
 ADSLZone
 Sygate Online Scan extended security check (Stealth Scan, Trojan Scan)
 Crucialtests concise, incl. advisor (actualmente no está en línea)
 AuditMyPC Free Port Scanning Can scan all 65535 ports.
