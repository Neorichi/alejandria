---
type: Artículo de enciclopedia
title: Squid (programa)
description: Squid es un servidor proxy para web con caché.
resource: https://es.wikipedia.org/wiki/Squid_(programa)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Squid_(programa)"}
license: CC BY-SA 4.0
id: eswiki-Squid_(programa)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Squid (programa)

- **Nombre:** Squid
- **Desarrollador:** Todos
- **Modelo desarrollo:** Software libre
- **Última versión:** 7.4
- **Sistema operativo:** Multiplataforma
- **Género:** Caché web, proxy
- **Licencia:** GNU General Public License

**Squid** es un servidor proxy para web con caché. Es una de las aplicaciones más populares y de referencia para esta función, es un desarrollo en software libre publicado bajo licencia GPL. Entre sus utilidades está la de mejorar el rendimiento de las conexiones de empresas y particulares a Internet guardando en caché peticiones recurrentes a servidores web y DNS, acelerar el acceso a un servidor web determinado o añadir seguridad realizando filtrados de tráfico.

Aunque orientado principalmente a HTTP y HTTPS soporta también otros protocolos como FTP e incluso Gopher. Implementa cifrado SSL/TLS tanto en la conexión al servidor web como a los navegadores y cualquier cliente web que lo soporte.

Squid es una aplicación muy consolidada en Internet. En desarrollo desde los años 1990, se le considera muy completo y robusto y es el software de referencia como servidor proxy-caché de web. Como muchas aplicaciones de software libre está incluido en distribuciones GNU/Linux pero se puede ejecutar también en entornos tipo Unix y hay algunas versiones para MS Windows.

 Características
Squid posee las siguientes características:

Proxy con caché de HTTP, FTP, y otros protocolos de Internet Squid proporciona un servicio de proxy que soporta peticiones HTTP, HTTPS y FTP a equipos que necesitan acceder a Internet y a su vez provee la funcionalidad de caché especializado en el cual almacena de forma local las páginas consultadas recientemente por los usuarios. De esta forma, incrementa la rapidez de acceso a los servidores de información Web y FTP que se encuentran fuera de la red interna.

Proxy para SSL Squid también es compatible con SSL (*Secure Socket Layer*) con lo que también acelera las transacciones cifradas, y es capaz de ser configurado con amplios controles de acceso sobre las peticiones de usuarios.

Jerarquías de caché Squid puede formar parte de una jerarquía de cachés. Diversos servidores trabajan conjuntamente atendiendo las peticiones. Un navegador solicita siempre las páginas a un solo proxy y si este no tiene la página en su caché consulta a sus hermanos, que a su vez también podrían consultar con sus padres antes de finalmente ir al servidor web si fuera necesario. Estas peticiones entre cachés se pueden hacer mediante dos protocolos: ICP y HTCP.

ICP, HTCP, CARP, *caché digests* Squid sigue los protocolos ICP, HTCP, CARP y *caché digests* que tienen como objetivo permitir a un proxy «preguntarle» a otros cachés si tienen almacenado un recurso determinado.

Caché transparente Squid se puede configurar para ser usado como proxy transparente empleando un cortafuegos que intercepte y redirija las conexiones sin configuración por parte del cliente, e incluso sin que el propio usuario conozca de su existencia.

Puerto 3128 De modo predefinido Squid utiliza el puerto 3128 para atender peticiones, sin embargo se puede especificar que lo haga en cualquier otro puerto disponible o bien que lo haga en varios puertos disponibles a la vez.

WCCP A partir de la versión 2.3 Squid implementa WCCP (*Web Cache Control Protocol*). Permite interceptar y redirigir el tráfico que recibe un rúter hacia uno o más proxys caché, haciendo control de la conectividad de los mismos. Además permite que uno de los proxys caché designado pueda determinar cómo distribuir el tráfico redirigido a lo largo de todo el array de proxys caché.

Control de acceso Ofrece la posibilidad de establecer reglas de control de acceso. Esto permite establecer políticas de acceso en forma centralizada, simplificando la administración de una red.

Gestión de tráfico Permite categorizar el tráfico y limitarlo de manera individual o agrupada para conseguir un mejor aprovechamiento del ancho de banda disponible en la conexión a Internet.

Aceleración de servidores HTTP Se puede asociar Squid a servidores HTTP determinados. Publicando la dirección y puerto del caché, que en este caso puede ser el propio puerto 80, desde el exterior Squid se percibe como si él fuera el propio servidor web y así se reduce la carga soportada por el servidor web. Esto es especialmente rentable cuando se trata de contenido generado de forma dinámica. Este modo de funcionamiento se conoce también como *proxy inverso*. Este es el sistema de acceso a los .

SNMP Squid permite activar el protocolo SNMP que proporciona un método simple de administración de red permitiendo supervisar, analizar y comunicar información de estado entre una gran variedad de máquinas; permite detectar problemas y proporcionar mensajes de estado.

Caché de resolución DNS Squid incorpora el programa *dnsserver*, que se encarga de las búsquedas de nombres de dominio. Cuando Squid se ejecuta, produce un número configurable de procesos *dnsserver*, y cada uno de ellos realiza su propia búsqueda en DNS. De este modo, se reduce la cantidad de tiempo que la caché debe esperar a estas búsquedas DNS.

 Proxy Web

El proxy caché es una manera de guardar los objetos solicitados de Internet (por ejemplo, datos como páginas web) disponibles vía protocolos HTTP, FTP y Gopher en un sistema más cercano al lugar donde se piden. Los navegadores web pueden usar la caché local Squid como un servidor proxy HTTP, reduciendo el tiempo de acceso así como el consumo de ancho de banda. Esto es muchas veces útil para los proveedores de servicios de Internet para incrementar la velocidad de sus consumidores y para las redes de área local que comparten la conexión a Internet.

Debido a que también es un proxy (es decir, se comporta como un cliente en lugar del cliente real), puede proporcionar un cierto grado de anonimato y seguridad. Sin embargo, también puede introducir problemas significativos de privacidad ya que puede registrar mucha información, incluyendo las URL solicitadas junto con otra información adicional como la fecha de la petición, versión del navegador y del sistema operativo, etc.

Un programa cliente (por ejemplo, un navegador) o bien tiene que especificar explícitamente el servidor proxy que quiere utilizar (típico para consumidores de ISP) o bien podría estar usando un proxy sin ninguna configuración extra. A este hecho se le denomina caché transparente, en el cual todas las peticiones HTTP son interceptadas por squid y todas las respuestas guardadas en caché. Esto último es típico en redes corporativas dentro de una red de acceso local y normalmente incluye los problemas de privacidad mencionados previamente.

Squid tiene algunas características que pueden facilitar establecer conexiones anónimas. Características tales como eliminar o modificar campos determinados de la cabecera de peticiones HTTP de los clientes. Esta política de eliminación y alteración de cabeceras se establece en la configuración de Squid. El usuario que solicita páginas a través de una red que utiliza Squid de forma transparente, normalmente no es consciente de este proceso o del registro de información relacionada con el proceso.

 Compatibilidad
Squid puede ejecutarse en los siguientes Sistemas Operativos:

 AIX
 BSDI
 Digital Unix
 FreeBSD
 HP-UX
 IRIX
 GNU/Linux
 Mac OS X
 NetBSD
 NeXTStep
 OpenBSD
 SCO Unix
 SunOS/Solaris
 Windows NT

Para Windows se utilizan los paquetes Cygwin/GnuWin32. Obs.: Existen, actualmente, paquetes que corren squid en W32 sin necesidad de Cygwin.

Para analizar sus logs se puede usar Sarg

 Véase también

 GNU/Linux
 Firewall
 SmoothWall
 IPCop

 Enlaces externos
 Web oficial de Squid Web Proxy Cache
 Página oficial descarga para Windows
