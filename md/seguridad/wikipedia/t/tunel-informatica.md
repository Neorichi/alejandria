---
type: Artículo de enciclopedia
title: Túnel (informática)
description: Se conoce como túnel o tunneling a la técnica que consiste en encapsular un protocolo de red sobre otro (protocolo de red encapsulador) creando un túnel de información dentro de una red de computadoras.
resource: https://es.wikipedia.org/wiki/Túnel_(informática)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Túnel_(informática)"}
license: CC BY-SA 4.0
id: eswiki-Túnel_(informática)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Túnel (informática)

Se conoce como **túnel** o *tunneling* a la técnica que consiste en encapsular un protocolo de red sobre otro (protocolo de red encapsulador) creando un túnel de información dentro de una red de computadoras.  El uso de esta técnica persigue diferentes objetivos, dependiendo del problema que se esté tratando, como por ejemplo la comunicación de islas en escenarios multicast, la redirección de tráfico, etc. La técnica de **tunelizar** se suele utilizar para transportar un protocolo determinado a través de una red que, en condiciones normales, no lo aceptaría. Otro uso de la tunelización de protocolos es la creación de diversos tipos de redes privadas virtuales.

El establecimiento de dicho túnel se implementa incluyendo una PDU (unidad de datos de protocolo) determinada dentro de otra PDU con el objetivo de transmitirla desde un extremo al otro del túnel sin que sea necesaria una interpretación intermedia de la PDU encapsulada. De esta manera se encaminan los paquetes de datos sobre nodos intermedios que son incapaces de ver en claro el contenido de dichos paquetes. El túnel queda definido por los puntos extremos y el protocolo de comunicación empleado, que entre otros, podría ser SSH. Así, el protocolo A es encapsulado dentro del protocolo B, de forma que el primero considera al segundo como si estuviera en el nivel de enlace de datos.

Uno de los ejemplos más claros de utilización de esta técnica consiste en la redirección de tráfico en escenarios IP Móvil. En escenarios de IP móvil, cuando un nodo-móvil no se encuentra en su red base, necesita que su *home-agent* realice ciertas funciones en su puesto, entre las que se encuentra la de capturar el tráfico dirigido al nodo-móvil y redirigirlo hacia él. Esa redirección del tráfico se realiza usando un mecanismo de tunneling, ya que es necesario que los paquetes conserven su estructura y contenido originales (dirección IP de origen y destino, puertos, etc.) cuando sean recibidos por el nodo-móvil.

 Ejemplos de protocolos tunelizados

Protocolos orientados a datagramas:

 L2TP (*Layer 2 Tunneling Protocol*)
 MPLS (*Multiprotocol Label Switching*)
 GRE (*Generic Routing Encapsulation*)
 PPTP (*Point-to-Point Tunneling Protocol*)
 PPPoE (*point-to-point protocol over Ethernet*)
 PPPoA (*point-to-point protocol over ATM*)
 IPSec (*Internet Protocol security*)
 IEEE 802.1Q (*Ethernet VLANs*)
 DLSw (*SNA over IP*)
 XOT (*X.25 datagrams over TCP*)
 6to4 (*IPv6 over IPv4 as protocol 41*)
 Teredo

Protocolos orientados a flujo:

 TLS (*Transport Layer Security*)
 SSH (*Secure Shell*)

 Túnel SSH
El protocolo SSH (*secure shell*) se utiliza con frecuencia para *tunelizar* tráfico
confidencial sobre Internet de una manera segura. Por ejemplo, un servidor de ficheros
puede compartir archivos usando el protocolo SMB (*Server Message Block*), cuyos datos
no viajan cifrados y que una tercera parte que tuviera acceso a la
conexión (algo posible si las comunicaciones se realizan en Internet) pudiera examinar
a conciencia el contenido de cada fichero trasmitido.

Para poder montar el sistema de archivo de forma segura, se establece una conexión mediante
un túnel SSH que encamina todo el tráfico SMB al servidor de archivos
dentro de una conexión cifrada SSH. Aunque el protocolo SMB sigue siendo inseguro, al viajar
dentro de una conexión cifrada se impide el acceso al mismo.

Por ejemplo, para conectar con un servidor web de
forma segura, utilizando SSH, haríamos que el cliente web, en
vez de conectarse al servidor directamente, se conecte a un cliente SSH. El cliente
SSH se conectaría con el servidor tunelizado, el cual a su vez se conectaría con
el servidor web final. Lo atractivo de este sistema es que hemos añadido una
capa de cifrado sin necesidad de alterar ni el cliente ni el servidor web.

 Tunelizar para evitar un cortafuegos

La técnica de tunelizar puede ser usada también para evitar o circunvalar un cortafuegos. Para ello, se encapsula el protocolo bloqueado en el cortafuegos dentro de otro permitido, habitualmente HTTP.

 Véase también
 Red Privada Virtual
 Redes de computadoras
 Seguridad informática
 Protocolo (informática)
