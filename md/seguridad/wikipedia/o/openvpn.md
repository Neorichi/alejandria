---
type: Artículo de enciclopedia
title: OpenVPN
description: "OpenVPN es una herramienta de conectividad basada en software libre: SSL (Secure Sockets Layer), VPN Virtual Private Network (red virtual privada)."
resource: https://es.wikipedia.org/wiki/OpenVPN
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/OpenVPN"}
license: CC BY-SA 4.0
id: eswiki-OpenVPN
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# OpenVPN

- **Nombre:** OpenVPN
- **Autor:** James Yonan
- **Desarrollador:** OpenVPN project / OpenVPN Technologies, Inc.
- **Lanzamiento:** 1.1.0 /
- **Última versión:** 2.7.8
- **Plataforma:** Multiplataforma
- **Género:** VPN
- **Licencia:** GNU GPL

**OpenVPN** es una herramienta de conectividad basada en software libre: SSL (Secure Sockets Layer), VPN Virtual Private Network (red virtual privada). OpenVPN ofrece conectividad punto-a-punto con validación jerárquica de usuarios y host conectados remotamente. Resulta una muy buena opción en tecnologías Wi-Fi (redes inalámbricas IEEE 802.11) y soporta una amplia configuración, entre ellas balanceo de cargas. Está publicado bajo la licencia GPL, de software libre.

 Introducción
OpenVPN es un producto de software creado por James Yonan en el año 2001 y que ha estado mejorando desde entonces.

Ofrece una combinación de seguridad, facilidad de uso y riqueza de características.

Es una herramienta multiplataforma que ha simplificado la configuración de VPN's frente a otras más antiguas y difíciles de configurar como IPsec y haciéndola más accesible para gente inexperta en este tipo de tecnología.

Por ejemplo: Supóngase que se necesita comunicar diferentes sucursales de una organización.
A continuación se verá algunas soluciones que se han surgido para satisfacerla.

En el pasado las comunicaciones se realizaban por correo, teléfono o fax.
Hoy en día hay factores que hacen necesaria la implementación de soluciones más sofisticadas de conectividad entre las oficinas de las organizaciones a lo largo del mundo.

Dichos factores son:
 La aceleración de los procesos de negocios y su consecuente aumento en la necesidad de intercambio flexible y rápido de información.
 Muchas organizaciones tienen varias sucursales en diferentes ubicaciones así como también tele trabajadores remotos desde sus casas, quienes necesitan intercambiar información sin ninguna demora, como si estuvieran físicamente juntos.
 La necesidad de las redes de computación de cumplir altos estándares de seguridad que aseguren la autenticidad, integridad y disponibilidad.

**Líneas dedicadas**

Las necesidades antes mencionadas se satisfacían en principio colocando líneas dedicadas entre las diferentes ubicaciones remotas a un costo mucho mayor que el de simple acceso a Internet.
Se necesitaban conexiones físicas reales necesitando de un proveedor en cada sitio resultando en una solo línea de comunicación entre dos partes.

Por ejemplo, para una red de 4 nodos en la cual se buscase comunicación de todos con todos, habría que tender 6 líneas de comunicación.

Además, para dar conectividad a trabajadores domésticos o viajeros se implementaban servicios RAS1 para aquellos que necesitaban conectarse temporalmente mediante conexiones de módem o líneas ISDN2 donde la organización se comportaba como un proveedor de Internet (ISP).

**Acceso mediante Internet y VPNs**

Con la llegada de Internet y la baja de costos en conectividad se desarrollaron nuevas tecnologías. Surgió entonces la idea de utilizar a Internet como medio de comunicación entre los diferentes sitios de la organización.
Surge así la idea de las VPN's que son “Virtuales” y “Privadas”.
Virtuales porque no son redes directas reales entre partes, sino solo conexiones virtuales provistas mediante software sobre la red Internet.
Además son privadas porque solo la gente debidamente autorizada puede leer los datos transferidos por este tipo de red logrando la seguridad mediante la utilización de modernos mecanismos de criptografía.
Retomando el ejemplo anterior de una organización con cuatro sitios, ahora solo necesitamos cuatro conexiones a Internet en lugar de las seis dedicadas de antes. Además los que se conectan temporalmente, también lo hacen mediante una conexión a Internet, mucho más barata y accesible desde muchos lugares, como por ejemplo de cibercafés.

 Usos de las VPN

Las VPN se usan generalmente para:
 Conexión entre diversos puntos de una organización a través de Internet.
 Conexiones de trabajadores domésticos o de campo con IP dinámicas.
 Soluciones extranet para clientes u organizaciones asociadas con los cuales se necesita intercambiar cierta información en forma privada pero no se les debe dar acceso al resto de la red interna.
 Además brinda una excelente fiabilidad en la comunicación de usuarios móviles así como también al unir dos puntos distantes como agencias de una empresa dentro de una sola red unificada.

 Implementación de VPN

Supóngase que se tienen dos sitios de una organización conectados a Internet.
En ambos se contará con un equipo de conexión a la red de redes que cumplirá la función de ruteo hacia y desde Internet así como firewall para protegerse de accesos no autorizados.

El software VPN debe estar instalado en ese firewall o algún dispositivo protegido por él.
Uno de los sitios será el “servidor” y será el sitio que contiene la información y sistemas que queremos compartir, mientras que al otro lo llamaremos “cliente”. El servidor será entonces configurado para aceptar conexiones desde el cliente (y viceversa).

Llegado este punto habremos logrado tener dos sitios comunicados como en una red directa real, pero aún no es una VPN dado que falta implementar la “privacidad”, pues cualquier nodo intermedio de Internet puede leer la información que viaja sin protección.

Lo que se debe hacer seguidamente es establecer mecanismos de cifrado que mediante uso de claves aseguren que solo equipos o personas dueños de esas claves puedan acceder a los datos enviados por la VPN.

Todos los datos enviados del punto A al B deberán ser cifrados antes de ser enviados y descifrados en el otro extremo para posteriormente ser entregados normalmente a su destinatario final.

Uno de los factores que diferencian a una implementación de VPN de otra, son los mecanismos que utilicen para cifrar y distribuir claves a todos los integrantes de dicha red.

 Protocolos
Las soluciones de VPN pueden ser implementadas a diferentes niveles del modelo OSI de red.
**Implementaciones de capa 2 - Enlace**

El encapsulamiento a este nivel ofrece ciertas ventajas ya que permite transferencias sobre protocolos no-IP, como por ejemplo IPX4 de Netware Systems.

Teóricamente, las tecnologías implementadas en capa 2 pueden tunelizar cualquier tipo de paquetes y en la mayoría de los casos lo que se hace es establecer un dispositivo virtual PPP5 con el cual se establece la conexión con el otro lado del túnel.

Algunos ejemplos de estas tecnologías:

 *PPTP:* Point to Point Tunneling Protocol. Desarrollado por Microsoft, es una extensión de PPP.
Su principal desventaja es que solo puede establecer un túnel por vez entre pares.
 *L2F:* Layer 2 Forwarding. Desarrollado por la empresa Cisco principalmente, ofrece mejores posibilidades que PPTP principalmente en el uso de conexiones simultáneas.
 *L2TP:* Layer 2 Tunneling Protocol. Usado por Cisco y otros fabricantes, se ha convertido en estándar de la industria y combina las ventajas de PPTP y L2F y además eliminando las desventajas. Dado que esta solución no ofrece mecanismos de seguridad, para su uso deberá ser combinada con otros mecanismos generalmente implementados en capa 3 del modelo OSI.
 *L2Sec:* Layer 2 Security Protocol. Desarrollado para proveer una solución con seguridad, utiliza para ellos SSL/TLS aunque impone una sobrecarga bastante grande en la comunicación para lograrlo.

**Implementaciones de capa 3 - Red**

IPsec es la tecnología más aceptada en este punto y fue desarrollada como un estándar de seguridad de Internet en capa 3.
IPsec se puede utilizar para encapsular cualquier tráfico de capa 3 pero no el tráfico de capas inferiores, por lo que no se podrá utilizar para protocolos no-IP como IPX o mensajes de broadcast.

Su principal ventaja es que puede ser usado prácticamente en cualquier plataforma existiendo una gran variedad de soluciones tanto de software como de hardware.

Existen dos métodos principales usados por IPsec:

 *Modo Túnel*. Todos los paquetes IP son encapsulados en un nuevo paquete y enviados a través del túnel siendo desempaquetados en el otro extremo y posteriormente dirigidos a su destinatario final. En este modo, se protegen las direcciones IP de emisor y receptor así como el resto de los metadatos de los paquetes.
 *Modo Transporte*. Solo la carga útil (payload) de la sección de datos es cifrada y encapsulada. La sobrecarga entonces, es sensiblemente menor que en el caso anterior, pero se exponen los metadatos a posibles atacantes que podrán ver quien se está comunicando con quien.

**Implementaciones de capa 7 - Aplicación**

También es posible establecer túneles en la capa de aplicación y de hecho son ampliamente utilizados hoy en día siendo algunas aproximaciones soluciones como SSL6 y TLS7. El usuario accede a la VPN de la organización a través de un navegador iniciando la conexión en un sitio web seguro (HTTPS-Secured website).

Además, existen otros productos como SSL-Explorer y otros que ofrecen una combinación de gran flexibilidad, seguridad fuerte y facilidad de configuración.

La seguridad es lograda mediante cifrado del tráfico usando mecanismos SSL/TLS, los cuales han probado ser muy seguros y están siendo constantemente sometidos a mejoras y pruebas.

**Implementación OpenVPN**

OpenVPN es una solución para VPN que implementa conexiones de capa 2 o 3, usa los estándares de la industria SSL/TLS para cifrar y combina todas las características mencionadas anteriormente en las otras soluciones VPN.

Su principal desventaja por el momento es que hay muy pocos fabricantes de hardware que lo integren en sus soluciones.
Sin embargo, en sistemas basados en Linux se puede implementar sin problemas mediante software.

 Seguridad en VPN

Para cifrar datos se usan Passwords o claves de cifrado.

OpenVPN tiene dos modos considerados seguros, uno basado en claves estáticas pre-compartidas y otro en SSL/TLS usando certificados y claves RSA.

Cuando ambos lados usan la misma clave para cifrar y descifrar los datos, estamos usando el mecanismo conocido como “clave simétrica” y dicha clave debe ser instalada en todas las máquinas que tomarán parte en la conexión VPN.

Si bien SSL/TLS + claves RSA es por lejos la opción más segura, las claves estáticas cuentan con la ventaja de la simplicidad.

Se verá a continuación ese método y otros que aportan mayor seguridad y facilidad de distribución.

**Cifrado simétrico y claves pre-compartidas**

Cualquiera que posea la clave podrá descifrar el tráfico, por lo que si un atacante la obtuviese comprometería el tráfico completo de la organización ya que tomaría parte como un integrante más de la VPN.

Es por ello que mecanismos como IPsec cambian las claves cada cierto período, asociando a las mismas ciertos períodos de validez, llamados “tiempo de vida” o “lifetime”.
Una buena combinación de tiempo de vida y longitud de la clave asegurarán que un atacante no pueda descifrar la clave a tiempo, haciendo que cuando finalmente la obtenga (porque lo hará), ya no le sirva por estar fuera de vigencia.
IPSec utiliza su propio protocolo para intercambiar claves llamado IKE9 que ha sido desarrollado desde mediados de los noventa y aún no ha sido terminado.

**Cifrado asimétrico con SSL/TLS**

SSL/TLS usa una de las mejores tecnologías de cifrado para asegurar la identidad de los integrantes de la VPN.

Cada integrante tiene dos claves, una pública y otra privada.

La pública es distribuida y usada por cualquiera para cifrar los datos que serán enviados a la contraparte quien conoce la clave privada que es imprescindible para descifrar los datos.
El par de clave pública/privada es generado a partir de algoritmos matemáticos que aseguran que solo con la clave privada es posible leer los datos originales.
Si se encontrase un modo de quebrar la seguridad que estos algoritmos proporcionan, todas las conexiones cuya integridad depende de ellos se verían potencialmente comprometidas.

Es de destacar que la clave privada debe permanecer secreta mientras que la clave pública debe ser intercambiada para que nos puedan enviar mensajes.

**Seguridad SSL/TLS**

Las bibliotecas SSL/TLS son parte del software OpenSSL que viene instalado en cualquier sistema moderno e implementa mecanismos de cifrado y autenticación basados en certificados.
Los certificados generalmente son emitidos por entidades de reconocida confiabilidad aunque también podemos emitirlos nosotros mismos y usarlos en nuestra propia VPN.
Con un certificado firmado, el dueño del mismo es capaz de demostrar su identidad a todos aquellos que confíen en la autoridad certificadora que lo emitió.

 Ventajas y Desventajas de OpenVPN

**Ventajas**
OpenVPN provee seguridad, estabilidad y comprobados mecanismos de cifrado sin sufrir la complejidad de otras soluciones VPN como las de IPsec.

Además ofrece otras ventajas comparativas, como son:

 Posibilidad de implementar dos modos básicos, en capa 2 o capa 3, con lo que se logran túneles capaces de enviar información en otros protocolos no-IP como IPX o broadcast (NETBIOS).
 Protección de los usuarios remotos. Una vez que OpenVPN ha establecido un túnel el firewall de la organización protegerá el laptop remoto aun cuando no es un equipo de la red local. Por otra parte, sólo un puerto de red podrá ser abierto hacia la red local por el remoto asegurando protección en ambos sentidos.
 Conexiones OpenVPN pueden ser realizadas a través de casi cualquier firewall. Si se posee acceso a Internet y se puede acceder a sitios HTTPS, entonces un túnel OpenVPN debería funcionar sin ningún problema.
 Soporte para proxy. Funciona a través de proxy y puede ser configurado para ejecutar como un servicio TCP o UDP y además como servidor (simplemente esperando conexiones entrantes) o como cliente (iniciando conexiones).
 Sólo un puerto en el firewall debe ser abierto para permitir conexiones, dado que desde OpenVPN 2.0 se permiten múltiples conexiones en el mismo puerto TCP o UDP.
 Las interfaces virtuales (tun0, tun1, etc.) permiten la implementación de reglas de firewall muy específicas.
 Todos los conceptos de reglas, restricciones, reenvío y NAT10 pueden ser usados en túneles OpenVPN.
 Alta flexibilidad y posibilidades de extensión mediante scripting. OpenVPN ofrece numerosos puntos para ejecutar scripts individuales durante su arranque.
 Soporte transparente para IPs dinámicas. Se elimina la necesidad de usar direcciones IP estáticas en ambos lados del túnel.
 Ningún problema con NAT. Tanto los clientes como el servidor pueden estar en la red usando solamente IPs privadas.
 Instalación sencilla en cualquier plataforma. Tanto la instalación como su uso son muy simples.
 Diseño modular. Se basa en un excelente diseño modular con un alto grado de simplicidad tanto en seguridad como red.

**Desventajas**
 No tiene compatibilidad con IPsec que es el actual estándar para soluciones VPN.
 Carencia de masa crítica.
 Todavía son, relativamente pocos, los que saben cómo usar OpenVPN.
 Inicialmente, solo se podía conectar con clientes en computadoras de escritorio o portátiles. Sin embargo, actualmente se cuenta con clientes para iOS y Android. y hay compañías desarrollando dispositivos con clientes OpenVPN integrados y haciendo llegar esta tecnología a otros ámbitos como la automatización industrial, como Panasonic.

 Comparación entre OpenVPN e IPsec VPN

 Bibliografía
 OpenVPN: Building and Integrating Virtual Private Networks – Markus Feilner – ISBN 1-904811-85
 Sito web de OpenVPN.
 Sitio web de Ubuntu.
 Configurar Servidor y cliente OpenVPN en un EdgeRouter
 OpenVPN COMO
 OpenVPN vs IKEv2 vs PPTP vs L2TP/IPSec.
 Pivpn. OpenVPN en RaspberryPi

**En Linux: **
 /usr/share/doc/openvpn
 man openvpn

 Referencias

 Enlaces externos

 Sitio web oficial de OpenVPN
