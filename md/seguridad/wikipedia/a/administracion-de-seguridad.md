---
type: Artículo de enciclopedia
title: Administración de seguridad
description: El objetivo de la administración de seguridad es lograr la exactitud, integridad y protección de todos los procesos y recursos de los sistemas de información.
resource: https://es.wikipedia.org/wiki/Administración_de_seguridad
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Administración_de_seguridad"}
license: CC BY-SA 4.0
id: eswiki-Administración_de_seguridad
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Administración de seguridad

El objetivo de la **administración de seguridad** es lograr la exactitud, integridad y protección de todos los procesos y recursos de los sistemas de información.

De este modo la administración de seguridad minimiza errores, fraudes y pérdidas en los sistemas de información que interconectan a las empresas actuales, así como a sus clientes, proveedores y otras partes interesadas.

 Tipos de defensas de seguridad

 Cifrado
Implica el uso de algoritmos matemáticos especiales, o llaves, para transformar los datos digitales en códigos cifrados antes de ser transmitidos y para descifrarlos cuando son recibidos. El método más usado es el llamado, método de llave pública, que es exclusivamente para el receptor que es conocida por el transmisor.

 Firewalls
Puede ser un procesador de comunicaciones, por lo común un ruteador, o un servidor dedicado, junto con software firewall. Sirve como un sistema de “portero” que protege las intranets de una empresa y otras redes informáticas de la intrusión al proporcionar un filtro y punto de transferencia seguro para el acceso a Internet y otras redes.

 Defensas contra la denegación de servicios
Los ataques de negación de servicios a través de Internet dependen de 3 niveles de sistemas interconectados:
 En el sitio web de la víctima
 En el proveedor de servicios de Internet
 En las máquinas zombis
Destacan algunos tipos de ataques como lo son:
**la inundación de SYN .-**
Envía un flujo de paquetes TCP/SYN (varias peticiones con Flags SYN en la cabecera), muchas veces con la dirección de origen falsificada. Cada uno de los paquetes recibidos es tratado por el destino como una petición de conexión, causando que el servidor intente establecer una conexión al responder con un paquete TCP/SYN-ACK y esperando el paquete de respuesta TCP/ACK (Parte del proceso de establecimiento de conexión TCP de 3 vías). Sin embargo, debido a que la dirección de origen es falsa o la dirección IP real no ha solicitado la conexión, nunca llega la respuesta.

**Inundación ICMP (ICMP Flood).-**
llamado el ping mortal Es una técnica DoS que pretende agotar el ancho de banda de la víctima. Consiste en enviar de forma continuada un número elevado de paquetes ICMP Echo request (ping) de tamaño considerable a la víctima, de forma que esta ha de responder con paquetes ICMP Echo reply (pong) lo que supone una sobrecarga tanto en la red como en el sistema de la víctima.

**El Protocolo de Mensajes de Control de Internet o ICMP (Internet Control Message Protocol).-**
es el sub protocolo de control y notificación de errores del Protocolo de Internet (IP). Como tal, se usa para enviar mensajes de error, indicando por ejemplo que un servicio determinado no está disponible o que un router o host no puede ser localizado.

**SMURF .-**
Existe una variante a ICMP Flood denominado Ataque Smurf que amplifica considerablemente los efectos de un ataque ICMP.
Existen tres partes en un Ataque Smurf: El atacante, el intermediario y la víctima (comprobaremos que el intermediario también puede ser víctima).El atacante dirige paquetes ICMP tipo "echo request" (ping) a una dirección IP de broadcast, usando como dirección IP origen, la dirección de la víctima. Se espera que los equipos conectados respondan a la petición, usando Echo reply(pong), a la máquina origen (víctima).Se dice que el efecto es amplificado, debido a que la cantidad de respuestas obtenidas, corresponde a la cantidad de equipos en la red que puedan responder. Todas estas respuestas son dirigidas a la víctima intentando colapsar sus recursos de red. Como se dijo anteriormente, los intermediarios también sufren los mismos problemas que las propias víctimas.

**INUNDACIÓN UDP (UDP Flood).-**
Básicamente este ataque consiste en generar grandes cantidades de paquetes UDP contra la víctima elegida. Debido a la naturaleza sin conexión del protocolo UDP, este tipo de ataques suele venir acompañado de IP spoofing. Es usual dirigir este ataque contra máquinas que ejecutan el servicio Echo (ping), de forma que se generan mensajes Echo de un elevado tamaño.

**JAMMING.-**
Es un mecanismo utilizado para anular las señales de radio u ondas mediante la difusión de una señal más fuerte para confundir al objetivo de esa señal. En una red cableada totalmente, el riesgo asociado con una denegación de servicio puede ser mitigado de varias maneras. Por ejemplo, la red y basado en host de detección de intrusos puede ser instalado para monitorear los patrones de red y de las firmas asociadas a un ataque de denegación de servicio. Sin embargo, esto puede resultar un poco más difícil para las redes inalámbricas debido a la sobre el factor aire. Equipo especial se pueden emplear para detectar, difundir, o explotar señales hostiles para la transmisión inalámbrica.

 Monitoreo del correo electrónico

 Defensa contra virus
Muchas empresas crean defensas contra la diseminación de virus al centralizar la distribución y actualización de software de antivirus como responsabilidad de sus departamentos de sistemas de información. Está prohibido copiarse

 Referencias

 Enlaces externos
