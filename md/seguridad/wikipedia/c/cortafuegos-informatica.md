---
type: Artículo de enciclopedia
title: Cortafuegos (informática)
description: "En informática, un cortafuegos (del término original en inglés firewall) es la parte de un sistema informático o una red informática que está diseñada para bloquear el acceso no autorizado, permitiendo al mismo tiempo …"
resource: https://es.wikipedia.org/wiki/Cortafuegos_(informática)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cortafuegos_(informática)"}
license: CC BY-SA 4.0
id: eswiki-Cortafuegos_(informática)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cortafuegos (informática)

En informática, un **cortafuegos** (del término original en inglés ***firewall***) es la parte de un sistema informático o una red informática que está diseñada para bloquear el acceso no autorizado, permitiendo al mismo tiempo comunicaciones autorizadas.

Los cortafuegos pueden ser implementados en hardware o software, o en una combinación de ambos. Los cortafuegos se utilizan con frecuencia para evitar que otros usuarios de Internet no autorizados tengan acceso a las redes privadas conectadas a Internet. Estos suelen actuar como un organismo de inspección que verifica las conexiones que se establecen entre una red y un equipo local. Un cortafuegos regula, por lo tanto, la comunicación entre ambos para proteger el ordenador contra programas maliciosos u otros peligros de Internet. Todos los mensajes que entren o salgan de la intranet pasan a través del cortafuegos, que examina cada mensaje y bloquea aquellos que no cumplen los criterios de seguridad especificados. También es frecuente conectar el cortafuegos a una tercera red, llamada *zona desmilitarizada o *DMZ*, *en la que se ubican los servidores de la organización que deben permanecer accesibles desde la red exterior''.

Un cortafuegos correctamente configurado añade una protección necesaria a la red, pero que en ningún caso debe considerarse suficiente. La seguridad informática abarca más ámbitos y más niveles de trabajo y protección contra virus, malware, entre otras amenazas.

 Historia del cortafuegos

El término inglés *firewall* significaba originalmente un muro cortafuegos, es decir, una pared para confinar un incendio o riesgo potencial de incendio en un edificio. Más adelante se usó para referirse a estructuras similares de metal que separaban el compartimiento del motor de un vehículo o aeronave del compartimento de pasajeros o cabina. En el área de las redes informáticas el término comenzó a usarse a finales de la década de 1980, cuando Internet era aún una tecnología bastante nueva en cuanto a su uso y conectividad a nivel global. Los predecesores de los cortafuegos informáticos fueron los *routers* utilizados a finales de los 1980, ya que estos mantenían las distintas redes de ordenadores separadas unas de otras, evitando que los problemas se propagaran de unas a otras. La visión de Internet como una comunidad relativamente pequeña de usuarios con máquinas compatibles, que valoraba la predisposición para el intercambio y la colaboración, terminó con una serie de importantes violaciones de seguridad de Internet que se produjo a finales de los 80:
 Clifford Stoll, que rastreó una intrusión en sus sistemas hasta descubrir a un hacker alemán que vendía información a la KGB.
 Bill Cheswick, cuando en 1992 instaló una cárcel simple electrónica para observar a un atacante.
 En 1988, un empleado del Centro de Investigación Ames de la NASA, en California, envió una nota por correo electrónico a sus colegas que decía:
 "Estamos bajo el ataque de un virus de Internet! Ha llegado a Berkeley, UC San Diego, Lawrence Livermore, Stanford y la NASA Ames".
 El Gusano Morris, que se extendió a través de múltiples vulnerabilidades en las máquinas de la época. Aunque no era malicioso, el gusano Morris fue el primer ataque a gran escala sobre la seguridad en Internet; la red no esperaba ni estaba preparada para hacer frente a su ataque.

 Primera generación – cortafuegos de red: filtrado de paquetes

El primer documento publicado para la tecnología firewall data de 1988, cuando el equipo de ingenieros Digital Equipment Corporation (DEC) desarrolló los sistemas de filtro conocidos como cortafuegos de filtrado de paquetes. Este sistema, bastante básico, fue la primera generación de lo que se convertiría en una característica más técnica y evolucionada de la seguridad de Internet.
En AT&T Bell, Bill Cheswick y Steve Bellovin continuaban sus investigaciones en el filtrado de paquetes y desarrollaron un modelo de trabajo para su propia empresa, con base en su arquitectura original de la primera generación.

El filtrado de paquetes actúa mediante la inspección de los paquetes (que representan la unidad básica de transferencia de datos entre ordenadores en Internet). Si un paquete coincide con el conjunto de reglas del filtro, el paquete será descartado (descarte silencioso) o será rechazado (desprendiéndose de él y enviando una respuesta de error al emisor). Este tipo de filtrado de paquetes no presta atención a si el paquete es parte de una secuencia existente de tráfico. En su lugar, se filtra cada paquete basándose únicamente en la información contenida en el paquete en sí (por lo general utiliza una combinación del emisor del paquete y la dirección de destino, su protocolo, y, en el tráfico TCP y UDP, el número de puerto). Los protocolos TCP y UDP comprenden la mayor parte de comunicación a través de Internet, utilizando por convención puertos bien conocidos para determinados tipos de tráfico, por lo que un filtro de paquetes puede distinguir entre ambos tipos de tráfico (ya sean navegación web, impresión remota, envío y recepción de correo electrónico, transferencia de archivos…); a menos que las máquinas a cada lado del filtro de paquetes estén a la vez utilizando los mismos puertos no estándar.

El filtrado de paquetes llevado a cabo por un cortafuegos actúa en las tres primeras capas del modelo de referencia OSI, lo que significa que todo el trabajo lo realiza entre la red y las capas físicas. Cuando el emisor origina un paquete y es filtrado por el cortafuegos, este último comprueba las reglas de filtrado de paquetes que lleva configuradas, aceptando o rechazando el paquete en consecuencia. Cuando el paquete pasa a través de cortafuegos, este filtra el paquete mediante un protocolo y un número de puerto base (GSS). Por ejemplo, si existe una norma en el cortafuegos para bloquear el acceso telnet, bloqueará el protocolo TCP para el número de puerto 23.

 Segunda generación – cortafuegos de estado

Durante 1989 y 1990, tres colegas de los laboratorios AT&T Bell, Dave Presetto, Janardan Sharma, y Nigam Kshitij, desarrollaron la segunda generación de servidores de seguridad. Esta segunda generación de cortafuegos tiene en cuenta, además, la colocación de cada paquete individual dentro de una serie de paquetes. Esta tecnología se conoce generalmente como la inspección de estado de paquetes, ya que mantiene registros de todas las conexiones que pasan por el cortafuegos, siendo capaz de determinar si un paquete indica el inicio de una nueva conexión, es parte de una conexión existente, o es un paquete erróneo. Este tipo de cortafuegos pueden ayudar a prevenir ataques contra conexiones en curso o ciertos ataques de denegación de servicio. La comercialización a gran escala de la inspección de estado se consolidó en 1993-1994 con FireWall-1, desarrollado en Israel por Gil Shwed, Marius Nacht y Shlomo Kramer en Check Point Software Technologies (Ramat Gan); el producto llevó la tecnología de laboratorios académicos y de telecomunicaciones a empresas de todo el mundo y contribuyó a definir el mercado moderno de la seguridad perimetral.

 Tercera generación — cortafuegos de aplicación

Son aquellos que actúan sobre la capa de aplicación del Modelo OSI. La clave de un cortafuegos de aplicación es que puede entender ciertas aplicaciones y protocolos (por ejemplo: protocolo de transferencia de ficheros, DNS o navegación web), y permite detectar si un protocolo no deseado se coló a través de un puerto no estándar o si se está abusando de un protocolo de forma perjudicial.

Un cortafuegos de aplicación es mucho más seguro y fiable cuando se compara con un cortafuegos de filtrado de paquetes, ya que repercute en las siete capas del modelo de referencia OSI. En esencia es similar a un cortafuegos de filtrado de paquetes, con la diferencia de que también podemos filtrar el contenido del paquete.

Un cortafuegos de aplicación puede filtrar protocolos de capas superiores tales como FTP, TELNET, DNS, DHCP, HTTP, TCP, UDP y TFTP (GSS). Por ejemplo, si una organización quiere bloquear toda la información relacionada con una palabra en concreto, puede habilitarse el filtrado de contenido para bloquear esa palabra en particular. No obstante, los cortafuegos de aplicación resultan más lentos que los de estado.

 Acontecimientos posteriores

En 1992, Bob Braden y DeSchon Annette, de la Universidad del Sur de California (USC), dan forma al concepto de cortafuegos. Su producto, conocido como "Visas", fue el primer sistema con una interfaz gráfica con colores e iconos, fácilmente implementable y compatible con sistemas operativos como Windows de Microsoft o MacOS de Apple. En 1993, Gil Shwed, Marius Nacht y Shlomo Kramer fundaron en Ramat Gan la empresa israelí Check Point Software Technologies; al año siguiente comercializaron FireWall-1, que incorporaba inspección de estado (*stateful inspection*) y una interfaz gráfica pensada para administradores de red. El producto se distribuyó mediante acuerdos OEM con Sun Microsystems y Hewlett-Packard, y en 1996 IDC situó a Check Point como líder mundial del mercado de cortafuegos, con una cuota estimada del 40 %. Esa trayectoria ilustra el papel de la industria israelí de ciberseguridad en la difusión de herramientas que hoy protegen redes empresariales, gubernamentales y domésticas.

La funcionalidad existente de inspección profunda de paquetes en los actuales cortafuegos puede ser compartida por los sistemas de prevención de intrusiones (IPS).

Actualmente, el Grupo de Trabajo de comunicación Middlebox de la Internet Engineering Task Force (IETF) está trabajando en la estandarización de protocolos para la gestión de cortafuegos.

Otro de los ejes de desarrollo consiste en integrar la identidad de los usuarios dentro del conjunto de reglas del cortafuegos. Algunos cortafuegos proporcionan características tales como unir a las identidades de usuario con las direcciones IP o MAC. Otros, como el cortafuegos NuFW, proporcionan características de identificación real solicitando la firma del usuario para cada conexión.

 Tipos de cortafuegos

Existen diferentes tipos de cortafuegos que se utilizan para proteger las redes y sistemas informáticos. A continuación, se describen algunos de estos tipos:

 Cortafuegos de capa de red o de filtrado de paquetes

Este tipo de cortafuegos opera a nivel de red (capa 3 del modelo OSI, capa 2 del stack de protocolos TCP/IP) y se encarga de tomar decisiones de procesamiento basadas en direcciones de red, puertos o protocolos. Funciona como un filtro de paquetes IP. A este nivel se pueden realizar filtros según los distintos campos de los paquetes IP: dirección IP origen, dirección IP destino. A menudo en este tipo de cortafuegos se permiten filtrados según campos de nivel de transporte (capa 4 del modelo OSI, capa 3 de TCP/IP), como el puerto origen y destino, o a nivel de enlace de datos (capa 2 del modelo OSI, no existe en TCP/IP) como la dirección MAC. Son subtipos de este cortafuegos:

 Clasificación de filtrado de paquetes en estático (*stateless packet filtering*)

 Cortafuegos de inspección con estado
Clasificación de filtrado de paquetes en dinámico (*stateful packet filtering*). Los puertos se pueden abrir y cerrar dinámicamente según sea necesario para completar una transacción. Estos cortafuegos guardan información de las sesiones a las que pertenecen los paquetes, lo que les permite acelerar el proceso de aceptación de paquetes pertenecientes a sesiones previamente aceptadas.

 Puerta de enlace a nivel de circuito / Circuito a nivel de pasarela

Este tipo de cortafuegos opera en la capa de transporte de los modelos de referencia de Internet o OSI. Se encarga de aplicar mecanismos de seguridad cuando se establece una conexión TCP o UDP. Una vez que se establece la conexión, los paquetes pueden fluir entre los hosts sin más control. Permite el establecimiento de una sesión que se origine desde una zona de mayor seguridad hacia una zona de menor seguridad.

 Cortafuegos de capa de aplicación

Estos cortafuegos operan en la capa de aplicación (capa 7 del modelo OSI) y se encargan de filtrar el acceso según las definiciones de la aplicación. Trabajar a ese nivel les permite adaptar los filtros a características propias de los protocolos de este nivel. Por ejemplo, si se trata de tráfico HTTP, se pueden realizar filtrados según la URL a la que se está intentando acceder, e incluso puede aplicar reglas en función de los propios valores de los parámetros que aparezcan en un formulario web.

Aplica mecanismos de seguridad para aplicaciones específicas, tales como servidores FTP y Telnet. Esto es muy eficaz, pero puede imponer una degradación del rendimiento.

Un cortafuegos a nivel 7 de tráfico HTTP suele denominarse proxy, y permite que los ordenadores de una organización entren a Internet de una forma controlada, así como llevar un registro de las conexiones. Un proxy oculta de manera eficaz las verdaderas direcciones de red.

 Cortafuegos de última generación (NGFW)

Este tipo de cortafuegos es una combinación de los anteriores y proporciona funcionalidades avanzadas. Se considera un cortafuegos de próxima generación al que combina características de inspección a nivel de paquete, filtrado a nivel de aplicación y otras tecnologías de seguridad. Ofrece una mayor inteligencia y capacidades de detección de amenazas.

 Cortafuegos personal

Es un caso particular de cortafuegos que se instala como software en un ordenador, filtrando las comunicaciones entre dicho ordenador y el resto de la red. Se usa por tanto, de manera personal.

 Funcionalidades adicionales

 Traducción de direcciones de red (NAT)

Los cortafuegos a menudo tienen funcionalidad de traducción de direcciones de red (NAT) y los hosts protegidos detrás de un cortafuegos tienen muchas direcciones en el "rango de direcciones privadas", como se define en RFC 1918. Los cortafuegos suelen tener esa funcionalidad para ocultar la verdadera dirección de la computadora conectada a la red. Originalmente, la función NAT se desarrolló para abordar el número limitado de direcciones enrutables IPv4 que podrían usarse o asignarse a empresas o individuos, así como reducir tanto el monto como el costo de obtener suficientes direcciones públicas para cada computadora en una organización. Aunque NAT por sí solo no se considera una característica de seguridad, ocultar las direcciones de los dispositivos protegidos se ha convertido en una defensa de uso frecuente contra reconocimientos de redes.

 Sistemas de detección y prevención de intrusiones (IPS/IDS)

 Características

 Políticas de firewall: suspende las peticiones de conexión que no provengan de la misma red o sistema, y oculta detrás de una IP los recursos internos.
 Filtrado de contenido: identifica los contenidos que pueden dar problemas, siempre teniendo la palabra del usuario como decisión final.
 Servicios antimalware: algunos cortafuegos pueden también detectar los virus y evitar su expansión. Estos son un híbrido entre un firewall y un antivirus. No son cortafuegos clásicos.
 Servicios de DPI: los procedimientos de *Inspección Profunda de Paquetes* suman una segunda protección al sistema, revisando exhaustivamente los paquetes de información que se reciben.

 Ventajas de un cortafuegos

 Bloquea el acceso a equipos y/o aplicaciones. Permite controlar y restringir las comunicaciones entre las partes.

 Cuando usas un firewall amplías el perímetro de seguridad y obtienes una mayor protección para la red de tu equipo frente al tráfico malicioso.

 Son especialmente beneficiosos para empresas con un número elevado de endpoints conectados a Internet.

 Limitaciones de un cortafuegos

Las limitaciones se desprenden de la misma definición del cortafuegos: filtro de tráfico. Cualquier tipo de ataque informático que use tráfico aceptado por el cortafuegos (por usar puertos TCP abiertos expresamente, por ejemplo) o que sencillamente no use la red, seguirá constituyendo una amenaza. La siguiente lista muestra algunos de estos riesgos:
 Un cortafuegos no puede proteger contra aquellos ataques cuyo tráfico no pase a través de él.
 El cortafuegos no puede proteger de las amenazas a las que está sometido por ataques internos o usuarios negligentes. El cortafuegos no puede prohibir a espías corporativos copiar datos sensibles en medios físicos de almacenamiento (discos, memorias, etc.) y sustraerlas del edificio.
 El cortafuegos no puede proteger contra los ataques de ingeniería social.
 El cortafuegos no puede proteger contra los ataques posibles a la red interna por virus informáticos a través de archivos y software. La solución real está en que la organización debe ser consciente en instalar software antivirus en cada máquina para protegerse de los virus que llegan por cualquier medio de almacenamiento u otra fuente.
 El cortafuegos no protege de los fallos de seguridad de los servicios y protocolos cuyo tráfico esté permitido. Hay que configurar correctamente y cuidar la seguridad de los servicios que se publiquen en Internet.

 Políticas del cortafuegos

Hay dos políticas básicas en la configuración de un cortafuegos que cambian radicalmente la filosofía fundamental de la seguridad en la organización:
 **Política restrictiva**: Se deniega todo el tráfico excepto el que está explícitamente permitido. El cortafuegos obstruye todo el tráfico y hay que habilitar expresamente el tráfico de los servicios que se necesiten. Esta aproximación es la que suelen utilizar las empresas y organismos gubernamentales.
 **Política permisiva**: Se permite todo el tráfico excepto el que esté explícitamente denegado. Cada servicio potencialmente peligroso necesitará ser aislado básicamente caso por caso, mientras que el resto del tráfico no será filtrado. Esta aproximación la suelen utilizar universidades, centros de investigación y servicios públicos de acceso a Internet.

La política restrictiva es la más segura, ya que es más difícil permitir por error tráfico potencialmente peligroso, mientras que en la política permisiva es posible que no se haya contemplado algún caso de tráfico peligroso y sea permitido

 Véase también

 *Bastion host*
 Lista de control de acceso
 *Unified threat management*
 RFC 2979
 Cortafuegos:
 *Firestarter*
 *ZoneAlarm*
 *Uncomplicated Firewall*
 Gufw
 ipfw
 *PF (software)*
 Forefront TMG
 Shorewall

 Referencias

 Enlaces externos

 Request for Comment 2979 - Comportamiento y requerimientos para los cortafuegos de Internet (en inglés)
 Firewalls: Seguridad en Internet - Comparativa (PDF)
