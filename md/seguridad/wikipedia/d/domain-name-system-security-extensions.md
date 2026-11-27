---
type: Artículo de enciclopedia
title: Domain Name System Security Extensions
description: "Las extensiones de seguridad para el sistema de nombres de dominio (Domain Name System Security Extensions o DNSSEC, por sus siglas en inglés) son un conjunto de especificaciones de la Internet Engineering Task Force …"
resource: https://es.wikipedia.org/wiki/Domain_Name_System_Security_Extensions
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Domain_Name_System_Security_Extensions"}
license: CC BY-SA 4.0
id: eswiki-Domain_Name_System_Security_Extensions
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Domain Name System Security Extensions

Las **extensiones de seguridad para el sistema de nombres de dominio** (*Domain Name System Security Extensions* o **DNSSEC**, por sus siglas en inglés) son un conjunto de especificaciones de la Internet Engineering Task Force (IETF) para asegurar cierto tipo de información proporcionada por el sistema de nombres de dominio (DNS) que se usa en el protocolo de Internet (IP). Se trata de un conjunto de extensiones para el DNS que proporcionan a los clientes DNS (o *resolvers*), la autenticación de origen de los datos DNS, denegación de existencia de autenticación y la integridad de los datos, pero no la disponibilidad o confidencialidad.

 Descripción general

El diseño original del Domain Name System (DNS) no incluía la seguridad pues su objetivo de desarrollo estuvo enfocado en ser un sistema distribuido escalable. Las Extensiones de seguridad para el Sistema de Nombres de Dominio (DNSSEC) intentan aumentar la seguridad, y al mismo tiempo mantener la compatibilidad con lo más antiguo. En el documento RFC 3833 se documentan algunas amenazas conocidas en el DNS y cómo DNSSEC puede responder a esas amenazas.

DNSSEC fue diseñado para proteger a los resolutores de dominios de Internet (a sus clientes) de datos de DNS que hayan sido falsificados, tales como la creados por envenenamiento de caché DNS. Todas las respuestas en DNSSEC son firmadas digitalmente. Al comprobar la firma digital, el resolver es capaz de comprobar si la información es idéntica (correcta y completa) a la información en el servidor DNS autorizado. Si bien la protección de las direcciones IP es la preocupación inmediata para muchos usuarios, DNSSEC puede proteger otra información también, como certificados de cifrado de propósito general almacenadas en registro CERTs en el DNS. RFC 4398 describe cómo distribuir estos certificados, incluidos los de correo electrónico, haciendo posible el uso de DNSSEC en todo el mundo como una infraestructura de clave pública para el correo electrónico.

DNSSEC *no* garantiza la confidencialidad de los datos; en particular, todas las respuestas de DNSSEC se autentican, pero no se cifran. DNSSEC *no* protege directamente contra los Ataques de denegación de servicio, aunque indirectamente, proporciona algún beneficio.
Otras normas (no DNSSEC) se utilizan para proteger los datos a granel (como la transferencia de zona DNS) que se envía entre los servidores DNS. Como se documenta en el IETF RFC 4367, algunos usuarios y desarrolladores hacen suposiciones falsas acerca de los nombres DNS, como el supuesto de que el nombre común de una empresa más ".com" es siempre su nombre de dominio. DNSSEC no puede proteger contra las falsas suposiciones, sino que solo puede autenticar que los datos son verdaderamente de o no disponible en el propietario del dominio.

Las especificaciones de DNSSEC (llamadas *DNSSEC-bis*), describen el actual protocolo DNSSEC en gran detalle. Véase los RFC 4033, RFC 4034 y RFC 4035. Con la publicación de estos nuevos documentos RFC (marzo de 2005), el RFC anterior, RFC 2535 ha quedado obsoleto.

Se cree ampliamente que asegurar los DNS es de vital importancia para la seguridad en Internet como un todo, pero el despliegue de DNSSEC en concreto se ha visto obstaculizado por varias dificultades:
 La necesidad de diseñar un estándar compatible con versiones anteriores que puede escalarse al tamaño de la Internet.
 Prevención de la "enumeración de la zona" (ver abajo) donde se desee.
 El despliegue de las implementaciones DNSSEC en una amplia variedad de servidores de DNS y resolvers (clientes).
 El desacuerdo entre los encargados de la ejecución sobre quién debe poseer las llaves de raíz de los dominios de nivel superior.
 La superación de la aparente complejidad de DNSSEC y su despliegue.
Los investigadores de la industria han trabajado para mejorar el diseño del sistema de nombres de dominio para reducir la probabilidad de que los atacantes comprometan la infraestructura. Lo han hecho permitiendo diversas opciones y ajustando las pautas de cómo operan.

 Funcionamiento

DNSSEC trabaja firmando digitalmente estos registros para la búsqueda de DNS mediante criptografía de clave pública. El registro DNSKEY correcto se auténtica a través de una cadena de confianza, que comienza en un conjunto de claves públicas de la zona raíz del DNS, que es la tercera parte de confianza.

 Registros

El DNS se implementa mediante el uso de varios registros de recursos. Para implementar DNSSEC, varios de los nuevos tipos de registro DNS se han creado o adaptado para su uso con DNSSEC:
 RRSIG
 DNSKEY
 DS
 NSEC
 NSEC3
 NSEC3PARAM

Cuando se usa DNSSEC, cada respuesta a una búsqueda de DNS contendrá un registro RRSIG DNS además del tipo de registro que se solicitó. El registro RRSIG es una firma digital de la respuesta de DNS registro de recursos conjunto. La firma digital puede ser verificada localizando la clave pública correcta se encuentra en un registro DNSKEY. El registro DS se utiliza en la autenticación de DNSKEYs en el procedimiento de búsqueda usando la cadena de confianza. Los registros NSEC y NSEC3 se utilizan para una resistencia fuerte contra la suplantación de identidad.

 Algoritmos

DNSSEC fue diseñado para ser extensible y para que cuando se descubran ataques contra los algoritmos existentes, nuevos pueden ser introducidos en una forma compatible con versiones anteriores. A julio de 2009, se definieron los siguientes algoritmos de seguridad que son utilizados con mayor frecuencia:

 El procedimiento de búsqueda

De los resultados de una búsqueda de DNS, un resolver de DNS consciente de la seguridad puede determinar si la respuesta que recibió fue segura, o si era insegura y el servidor de nombres autoritativo para el dominio consultado no soporta DNSSEC o si hay algún tipo de error. El procedimiento de búsqueda es diferente para servidor de nombres recursivos, como los de muchos ISPs, que para resolvers stub, como los incluidos por defecto en los sistemas operativos principales.
Microsoft Windows utiliza un resolver stub, y Windows Server 2008 R2 y Windows 7, en particular, utilizan un stub resolver que no valida DNSSEC, pero que es capaz de entender los mensajes.

 Servidores de nombres recursivos

Usando el modelo de la cadena de confianza, un registro de firmante delegado (DS) de un dominio principal (zona DNS) se puede utilizar para verificar un registro DNSKEY en un subdominio, que a su vez puede contener otros registros DS para verificar subdominios adicionales. Digamos que un resolver recursivo, como un servidor de nombre de un ISP desea obtener las direcciones IP (registro A y / o registro AAAA s) del dominio "www.example.com".

 El proceso comienza cuando un resolver que soporte seguridad establece el bit del parámetro "DO" en una consulta DNS. Dado que el bit DO está en los bits de los parámetros extendidos definidos por EDNS, todas las transacciones deben soportar DNSSEC EDNS. El soporte de EDNS también es necesario para permitir paquetes de tamaño mucho más grande como las transacciones DNSSEC requieren.
 Cuando el resolver recibe una respuesta a través del proceso normal de búsqueda de DNS, la comprueba para asegurarse de que la respuesta es correcta. Lo ideal sería que el resolver que soporte seguridad comenzará con la verificación de la DS y el registro DNSKEY en el Servidor Raíz. A continuación, se utiliza el registro DS para el dominio de nivel superior "com" encontrado en la raíz para verificar los registros DNSKEY en la zona "com". A partir de ahí, revisaría si hay un registro DS para el subdominio "example.com" en la zona "com", y si lo hubiera, entonces utilizaría el registro DS para verificar el registro DNSKEY encuentra en la zona "example.com". Por último, sería verificar el registro RRSIG encontrado en la respuesta de los registros A para "www.example.com".

Hay varias excepciones al ejemplo anterior.

En primer lugar, si "example.com" no es compatible con DNSSEC, no habrá ningún registro RRSIG en la respuesta y no habrá un registro DS para "example.com" en la zona "com". Si hay un registro DS para "example.com", pero ningún registro RRSIG en la respuesta, algo está mal y tal vez un Ataque Man-in-the-middle está ocurriendo, modificando los registros A y eliminando la información de DNSSEC. O bien, podría ser un servidor de nombres indolente a la seguridad en alguna parte del camino que eliminó el bit de parámetro DO de la consulta o el registro RRSIG de la respuesta. O bien, podría ser un error de configuración.

Después, podría ser que no haya un dominio llamado "www.example.com", en cuyo caso en lugar de devolver un registro RRSIG en la respuesta, habrá o un registro NSEC o un registro NSEC3. Estos son registros "casi seguros" que permiten al resolver demostrar que un nombre de dominio no existe. Los registros NSEC/NSEC3 tienen registros RRSIG, los que pueden ser verificados como anteriormente.

Por último, puede ser que la zona "example.com" implemente DNSSEC, pero ya sea la raíz o la zona "com" no lo haga, creando una "isla de seguridad", que debe ser validado de alguna otra manera. En julio de 2010 se completó el despliegue de DNSSEC en la raíz El dominio.com fue firmado con claves de seguridad válidas y se añadió delegación segura a la zona de la raíz el 1 de abril del 2011.

 Stub resolvers

Stub resolvers son "resolvers DNS mínimos que utilizan el modo de consulta recursiva para descargar la mayor parte del trabajo de resolución de DNS a un servidor de nombres recursivo". Un stub resolver simplemente enviará una solicitud a un servidor de nombres recursivo, y utilizará el bit de datos autenticados (*Authenticated Data*) (AD) en la respuesta como una "pista para averiguar si el servidor de nombres recursivo fue capaz de validar las firmas de todos los datos de las secciones de respuesta y la Autoridad de la respuesta." Microsoft Windows utiliza un stub resolver, y Windows Server 2008 R2 y Windows 7 en particular usan un stub resolver no validante, pero capaz de revisar el bit AD.

Un *stub resolver validante* también puede potencialmente llevar a cabo su propia validación de firma al fijar el bit de Checking Disabled (CD) en sus mensajes de consulta. Un stub resolver validante utiliza el CD bit para llevar a cabo su propia autenticación recursiva. Utilizar este tipo de stub resolver validantes le da al cliente DNS seguridad de extremo a extremo para los dominios que hayan implementado DNSSEC, incluso si el proveedor de servicios Internet o la conexión a ellos no es de confianza.

Para que los stub resolver no validante puedan confiar realmente en servicios DNSSEC, el stub resolver debe confiar tanto en los servidores de nombres recursivos en cuestión (los que suele ser controlados por el ISP) y los canales de comunicación entre él y los servidores de nombres, utilizando métodos tales como IPsec, SIG(0), o TSIG. El uso de IPsec no está muy extendido

 Anclas de confianza y cadenas de autenticación

Para ser capaz de demostrar que una respuesta DNS es correcta, es necesario conocer al menos un registro de DS que es correcto a partir de fuentes distintas de la DNS. Estos puntos de partida son conocidos como **anclas de confianza** y se obtienen normalmente con el sistema operativo o por alguna otra fuente de confianza. Cuando DNSSEC fue originalmente diseñado, se pensó que la única ancla de confianza que se necesitaba era que la raíz del DNS. Las anclas de la raíz se publicaron por primera vez el 15 de julio de 2010.

Una *cadena de autenticación* es una serie de registros DS y registros vinculados DNSKEY, comenzando con el ancla de confianza al servidor de nombres autorizado para el dominio en cuestión. Sin una cadena de autenticación completa, una respuesta a una búsqueda de DNS no puede autenticar de manera segura.

 Firmas y firmas de zona

Para limitar los ataques de repetición, no sólo hay valores TTL para propósitos de caché, sino que también marcas de tiempo adicionales en los registros RRSIG para limitar la validez de una firma. A diferencia de valores TTL que son relativos al momento del envío del registro, las marcas de tiempo son absolutas. Esto significa que todos los resolvers DNS que tengan en cuenta la seguridad deberán tener los relojes sincronizados con un margen de minutos.

Estas marcas de tiempo implica que una zona debe volver a ser firmada y distribuida a los servidores secundarios, o las firmas serán rechazadas por los resolvers que validan.

 La gestión de claves

Con el fin de permitir la sustitución de claves, se requiere un esquema de despliegue de clave. Típicamente, esto implica en primer lugar el despliegue de nuevas llaves en nuevos registros DNSKEY, además de las llaves antiguas existentes. Entonces, cuando es seguro asumir que los valores del tiempo para vivir han hecho que las claves antiguas almacenadas en caché que hayan expirado, se puede utilizar estas nuevas claves. Por último, cuando es seguro asumir que los registros almacenados en caché utilizando las claves viejas han expirado, los viejos registros DNSKEY se pueden eliminar. Este proceso es más complicado para cosas tales como las claves para confiar en los anclajes, como en la raíz, los que pueden requerir una actualización del sistema operativo.

Las claves en los registros DNSKEY se puede utilizar para dos cosas diferentes y los normalmente se utilizan diferentes registros para cada uno. En primer lugar, son las claves DNSKEY de firma de clave (KSK), que se utilizan para firmar los registros de otros DNSKEY. En segundo lugar, están las claves de firma de la zona (ZSK) que se utilizan para firmar los registros de otros. Dado que los ZSKs están bajo el control completo y son usados por una determinada zona DNS, ellos se pueden cambiar más fácilmente y más a menudo. Como resultado, ZSKs puede ser mucho más cortos que los KSKs y todavía ofrecer el mismo nivel de protección, pero reduciendo el tamaño de los registros RRSIG / DNSKEY.

Cuando una nueva KSK se crea, el registro DS debe ser transferido a la zona superior y publicado allí. Los registros DS utilizan una síntesis del mensaje de la KSK lugar de la clave completa con el fin de mantener el tamaño de los registros pequeños. Esto es útil para zonas como el dominio. Com, que son muy grandes. El procedimiento para actualizar las claves de DS en la zona principal también es más sencillo que en versiones anteriores DNSSEC las que requerían los registros DNSKEY estuvieran en la zona principal.

 Grupo de Trabajo DANE

El grupo de trabajo de autenticación de entidades con nombre basado en DNS (del inglés *DNS-based Authentication of Named Entities*) (DANE) pertenece a la IETF y tiene el objetivo de desarrollo de protocolos y técnicas que permiten a las aplicaciones de Internet establecer comunicaciones criptográficamente seguras (con IPsec, TLS, DTLS) basadas en DNSSEC.

Los nuevos protocolos permitirán a garantías adicionales y limitaciones para el modelo tradicional basado en la Infraestructura de clave pública. También permitirá a los titulares de dominio para hacer valer los certificados por ellos mismos, sin hacer referencia a terceras Autoridad de certificación.

Soporte para certificados grapados DNSSEC se ha habilitado en Google Chrome 14. Para Mozilla Firefox, el soporte es proporcionado por un add-on, mientras que el soporte nativo está actualmente en desarrollo.

 Historia

DNS es un servicio de Internet crítico y fundamental, sin embargo, en 1990 Steve Bellovin descubrió serias fallas de seguridad en él. Así comenzó la investigación para securitizar la información y aumentó drásticamente cuando su trabajo se hizo público en 1995. El primer RFC 2065 fue publicado por el IETF en 1997, y los intentos iniciales para implementar esa especificación llevaron a una versión revisida (y creían totalmente viable) especificada en 1999 como la IETF RFC 2535. Se hicieron planes para implementar DNSSEC basado en RFC 2535.

Por desgracia, la especificación IETF RFC 2535 tenía problemas muy importantes para escalar su uso a todo Internet; para el año 2001 se hizo evidente que esta especificación no servía para grandes redes. En operación normal los servidores DNS a menudo pierden la sincronización con sus superiores. Esto no suele ser un problema, pero cuando está habilitado DNSSEC, estos datos fuera de sincronización podría tener el serio efecto de una denegación de servicio autocreada. El DNSSEC original requería un complejo protocolo de seis mensaje y una gran cantidad de transferencias de datos para llevar a cabo cambios fundamentales para un dependiente (las zonas DNS dependientes tenían que enviar a todos sus datos a los servidores superiores, que el superior firmara cada registro, y luego enviar los firmas de vuelta al dependiente para que éste la guarde en un registro SIG). Además, los cambios de llaves públicas podría tener efectos absurdos; por ejemplo, si la zona ".com" cambiaba su clave pública, se tenía que enviar 22 millones de registros (ya que tendría que actualizar todas las firmas de todos sus dependientes). Así, DNSSEC como se define en el RFC 2535 no pudo escalar hasta la Internet.

La IETF modificó sustancialmente DNSSEC, que se llama *DNSSEC-bis* cuando es necesario distinguirlo del enfoque original de la RFC 2535. Esta nueva versión utiliza "registros de recursos de firmante delegado (DS)" (en inglés *delegation signer (DS) resource records*) para proporcionar un nivel adicional de indirección en los puntos de delegación entre un servidor superior y una zona dependiente. En el nuevo enfoque, cuando un dependiente cambia de clave pública maestra, en lugar de tener que enviar seis mensajes para cada registro, hay un simple mensaje: el dependiente envía la nueva clave pública a su superior (firmado, por supuesto). Los superiores simplemente almacenan una clave pública maestra para cada dependiente, lo que es mucho más práctico. Esto significa que unos pocos datos se empuja a los superiores, en lugar de cantidades masivas de datos que se intercambian entre los superiores y dependientes.

Esto significa que los clientes tienen que hacer un poco más de trabajo al comprobar las llaves. Más específicamente, la verificación de clave RRset de una zona DNS requiere de dos operaciones de verificación de firmas en lugar de solo una, como era requerida por el RFC 2535 (no hay impacto en el número de firmas verificadas para otros tipos de RRsets). La mayoría ve esto como un pequeño precio a pagar, ya que cambia DNSSEC y lo hace mucho más práctico de implementar.

 Normas

 RFC 2535 extensiones de seguridad del sistema de nombres de dominio
 RFC 3833 un análisis de amenazas del sistema de nombres de dominio
 RFC 4033 Introducción y Requisitos de Seguridad de DNS (*DNSSEC-bis*)
 RFC 4034 registros de recursos para las Extensiones de seguridad DNS (*DNSSEC-bis*)
 RFC 4035 Modificaciones de Protocolo de las Extensiones de seguridad DNS (*DNSSEC-bis*)
 RFC 4398 Almacenamiento de certificados en el Domain Name System (DNS)
 RFC 4470 Cobertura mínima de registros NSEC y firma en línea de DNSSEC
 RFC 4509 uso de SHA-256 en los registros de recursos (RR) de firmante Delegado (DS) DNSSEC
 RFC 4641 DNSSEC Prácticas Operacionales
 RFC 5155 DNSSEC negación autenticada de existencia por hash

 Tema de enumeración de zona, la controversia y NSEC3

Aunque el objetivo de DNSSEC es aumentar la seguridad, DNSSEC como se definió en los RFCs 4033 a 4035 presenta un nuevo problema que muchos creen es una nueva vulnerabilidad de seguridad: el tema de la enumeración de zona (también conocido como *zone walking*). DNSSEC obliga a la exposición de información que por mejores prácticas normales de DNS se mantienen como privada. NSEC3 (RFC 5155) se desarrolló para abordar esta cuestión y fue lanzado en marzo de 2008. NSEC3 mitiga, pero no elimina, la enumeración de la zona, ya que es posible buscar de manera exhaustiva el conjunto de todos los nombres posibles en una zona.

 Porqué los datos de zona DNS normalmente se mantienen privados

Cuando el protocolo DNS fue diseñado, no estaba destinado a ser un repositorio de información oculta. Sin embargo, como el DNS almacena la información sobre los detalles de una red relacionados con un dominio dado, muchos ven el contenido de su base de datos DNS como privado. En particular, los sistemas de DNS se configuran de manera que la mayoría de los usuarios no se les permite recuperar la lista completa de nombres u otra información en una zona. Esa lista sería de gran ayuda a los atacantes, ya que esta lista les puede dar información importante acerca de las máquinas que existen. Algunos administradores incluso poner el tipo de sistema e información de configuración en sus bases de datos de DNS, que es aún más valiosa para un atacante. El ampliamente utilizado libro de DNS and BIND (4 ª edición) por Albitz y Liu lo explica así:

Además, la información de una zona enumerada se puede utilizar como una clave para múltiples consultas WHOIS, lo que podría revelar datos del registrante, lo que muchos registros deben proteger, ya que están bajo estrictas obligaciones legales en virtud de diversos contratos.

No está claro si es legal implementar DNSSEC en muchos países, a menos que dichas listas se puedan mantener en privado. DENIC ha declarado que la cuestión de enumeración de zona de DNSSEC viola la Ley Federal alemana de Protección de Datos. Otros países europeos tienen leyes similares que prohíben la privacidad de la publicación de ciertos tipos de información.

 DNSSEC revela datos de zona

El diseño original de DNSSEC requería que toda la lista de nombres de zona se revelará a todos. Como se indica en el RFC 4033,

Hay una "evidente" solución, llamada un DNS horizonte dividido, que es como los DNS sin DNSSEC es desplegado a veces - pero este enfoque no funciona bien con DNSSEC. En el enfoque "DNS horizonte dividido", el servidor DNS niega la existencia de nombres a algunos clientes, y proporciona la información correcta a otros clientes. Sin embargo, dado que la información DNSSEC está firmada criptográficamente como autoridad, un atacante podría solicitar el registro "no existe" firmado, y luego retransmitir el registro para causar una denegación de servicio. DNSSEC cambia fundamentalmente el DNS para que pueda proporcionar información fidedigna, por lo que no funciona bien con los métodos basados en el suministro de información falsa para algunos usuarios. La investigación ha producido recomendaciones para combinar adecuadamente estas dos características de DNS.

DNSSEC presentó este problema, ya que debe ser capaz de informar cuando un nombre "no" es encontrado. Los servidores DNS con soporte DNSSEC deben ser capaces de firmar ese reporte "no encontrado" de lo contrario un informe de no encontrado podrían ser fácilmente falsificados. Sin embargo, por razones de seguridad la clave de firma no debe estar en línea. Como resultado, DNSSEC fue diseñado para reportar un mensaje firmado que informa que un determinado rango de nombres no existe, que puede ser firmado por delante-de-tiempo fuera de línea. Desafortunadamente, esta información es suficiente para un atacante para ganar mucha* más información*, de lo que hubiera estado disponible para ellos de otra manera - es suficiente para permitir a un atacante obtener rápidamente todos los nombres en una zona, y luego a través de consultas específicas en los nombres para la reconstrucción de la totalidad o la mayor parte de los datos de una zona.

Como se señaló anteriormente, DNSSEC podría ser utilizado como la base de una infraestructura de clave pública mundial para direcciones de correo electrónico, mediante el uso de DNS para servir los certificados de correo electrónico y DNSSEC para validarlos. Sin embargo, este problema de DNSSEC hace esto poco probable para la mayoría de las organizaciones, al menos si se utiliza directamente. Como dice el RFC 4398, "Si una organización opta por emitir certificados para sus empleados, la colocación de CERT RR en el DNS por el nombre del propietario, y si DNSSEC (con NSEC) está en uso, es posible para alguien que enumere todos los empleados de la organización . Esto generalmente no se considera deseable, por la misma razón que los listados de las empresas telefónicas no están publicados a menudo en público e incluso están marcados como confidenciales."

 Reacciones iniciales

Muchos de los participantes del grupo de trabajo de las extensiones DNS del IETF originalmente declaró que la enumeración de zona no era un problema importante, con el argumento de que los datos de los DNS era-o debería ser-pública. Sin embargo, los registradores y muchas organizaciones grandes dijeron a los miembros del grupo de trabajo que DNSSEC como se definía actualmente era inaceptable y que no haría o legalmente no podrían utilizarlo.

 Firmado en línea

Un enfoque para prevenir la enumeración de zona fue codificado en el RFC 4470. En lugar de firmar las respuestas no-encontrado por adelantado, una respuesta de no-encontrado se genera para cada consulta. Por ejemplo, si se recibe una consulta para 'b.example.com', en lugar de servir una respuesta previamente firmada diciendo que no hay nombres entre 'a.example.com "y" mail.example.com ", que revela la existencia de "mail.example.com", la respuesta podría ser que "no hay nombres entre b.example.com y ba.example.com '. Si la consulta siguiente se refiere a 'ba.example.com', la respuesta podría ser "no hay nombres entre ba.example.com y baa.example.com '. Esto hace que la enumeración de toda la zona impracticable.

Este método tiene algunas desventajas. Se requiere una clave de firma que se mantenga en línea y accesible a todos los servidores DNS. Muchas claves de firma de zona se mantienen en línea de todos modos para apoyar a re firmado de zona o actualizaciones automáticas dinámicas, pero estas funciones sólo son necesarios en un único servidor DNS principal, mientras que para soportar la firma en línea de la de zona la clave de firma se debe mantener en cada servidor DNS autorizados. Algunos servidores autorizados deben ser accesibles desde Internet y, preferiblemente, éstas estarán muy dispersas, haciendo difícil mantener las claves bajo control. También se requiere atención para evitar que un atacante inunde el servidor DNS con solicitudes de nombres falsos, denegando el servicio a los usuarios legítimos.

 NSEC3

Después de deliberar, se desarrolló una extensión: "DNSSEC Hashed Authenticated Denial of Existence" (informalmente llamado "NSEC3"). En este enfoque, los servidores conscientes de DNSSEC pueden optar por enviar un registro "NSEC3" en lugar de un registro NSEC cuando un registro no se encuentra. El registro NSEC3 está firmado, pero en lugar de incluir el nombre directamente (lo que permitiría la enumeración de zona), el registro NSEC3 incluye un valor criptográficamente hashed del nombre. El registro NSEC3 incluye tanto un hash después de un número de iteraciones y un salteado opcional, los cuales reducen la efectividad de los ataques de diccionario pre-calculados. El salteado aumenta el número de diccionarios necesarios para un ataque, mientras adicionales iteraciones de hash aumentan el costo de calcular cada diccionario.

En marzo de 2008, NSEC3 fue formalmente definida en el RFC 5155.

 Despliegue

Internet es infraestructura crítica, sin embargo, su funcionamiento depende del DNS que es fundamentalmente inseguro. Por lo tanto, hay un fuerte incentivo para asegurar DNS y el despliegue de DNSSEC se considera generalmente que es una parte fundamental de ese esfuerzo. Por ejemplo, la *Estrategia Nacional para Asegurar el Ciberespacio* identifica específicamente la necesidad de securitizar el DNS. El despliegue a gran escala de DNSSEC podría resolver muchos otros problemas de seguridad, así como la distribución segura de claves para las direcciones de correo electrónico.

El despliegue de DNSSEC en redes de gran escala también es un reto. Ozment y Schechter observan que DNSSEC (y otras tecnologías) tiene un "problema de arranque": los usuarios normalmente sólo implementar una tecnología si reciben un beneficio inmediato, pero si se requiere un nivel mínimo de implementación antes de que los usuarios reciben un beneficio mayor que sus costos (como es cierto para DNSSEC), es difícil de implementar. DNSSEC se puede implementar en cualquier nivel de la jerarquía DNS, pero debe ser ampliamente disponible en una zona antes que muchos otros van a querer adoptarlo. Los servidores DNS deben actualizarse con el software que soporta DNSSEC, y los datos DNSSEC se deben crear y añaden a los datos de la zona DNS. Un cliente TCP / IP que utilizan deben tener su resolución de DNS (cliente) actualizado antes de que pueda utilizar las capacidades de DNSSEC. Lo que es más, cualquier resolver debe tener, o tener un modo de adquirir, al menos una clave pública que pueda confiar antes de que pueda empezar a utilizar DNSSEC.

La implementación de DNSSEC puede añadir una carga significativa para algunos servidores DNS. Las respuestas DNSSEC firmadas comunes son mucho más grandes que el tamaño por defecto UDP de 512 bytes. En teoría, esto puede ser manejado a través de múltiples fragmentos IP, pero muchos "middleboxes" en el campo no manejan esto correctamente. Esto conduce a la utilización de TCP en su lugar. Sin embargo, muchas implementaciones de TCP actuales almacenan una gran cantidad de datos para cada conexión TCP; servidores fuertemente cargados pueden quedarse sin recursos simplemente tratando de responder a un mayor número de (posiblemente falsas) peticiones DNSSEC. Algunas extensiones de protocolo, como TCP Cookie Transactions, han sido desarrollados para reducir esta carga. Para hacer frente a estos desafíos, el esfuerzo significativo está en curso para implementar DNSSEC, debido a que el Internet es tan importante para tantas organizaciones.

 Despliegue inicial

Los primeros en adoptar incluyen a Brasil (.br), Bulgaria (.bg), República Checa (.cz), Puerto Rico (.pr) y Suecia (.se), que utilizan DNSSEC para los dominios de nivel superior de sus países; RIPE NCC, que han firmado todos los registros de búsqueda inversa (in-addr.arpa) que son delegados desde la Autoridad de Números Asignados de Internet (IANA). ARIN también está firmando sus zonas inversas. en febrero de 2007 TDC se convirtió en el primer ISP sueco para comenzar a ofrecer esta característica para sus clientes.

IANA probó públicamente una raíz firmada muestra desde junio de 2007. Durante este período previo a la firma de producción de la raíz, también hubo varias anclas de confianza alternativos. El IKS Jena introdujo uno el 19 de enero de 2006, el Internet Systems Consortium presentó otra el 27 de marzo del mismo año, mientras que ICANN anunció una tercera el 17 de febrero de 2009.

Se han llevado a cabo una amplia variedad de proyectos piloto y experimentos.dnssec.net mantiene una lista de este tipo de proyectos.

El 2 de junio de 2009, el Public Interest Registry (PIR) firmó la zona .org. El PIR también detalló el 26 de septiembre de 2008, que la primera fase, que implica grandes registrars que tiene una fuerte relación de trabajo con ("amigos y familiares") será el primero en ser capaz de firmar sus dominios, a partir de "principios de 2009". El 23 de junio de 2010, 13 registrars estaban listados como que ofrecían registros DNSSEC para dominios .ORG.

VeriSign hizo un proyecto piloto para permitir que los dominios .com y .net para inscribirse con el fin de experimentar con NSEC3. El 24 de febrero de 2009, anunciaron que iban a implementar DNSSEC en todos sus dominios de nivel superior (.com, .net, etc) dentro de 24 meses,  y el 16 de noviembre del mismo año, dijeron que los dominios .com y .net serían firmadas el primer trimestre de 2011, después de retrasos causados por aspectos técnicos de la aplicación. Este objetivo se logró en el plazo fijado y el VP de DNSSEC de Verisign, Matt Larson, ganó el Premio de Liderazgo en Tecnología de InfoWorld en 2011 por su papel en la promoción de DNSSEC.

 Despliegue en la raíz DNS

DNSSEC se desplegó por primera vez en el nivel de la raíz, el 15 de julio de 2010. Se espera que esto simplifique en gran medida el despliegue de resolvers DNSSEC, ya que el ancla de confianza raíz se puede utilizar para validar cualquier zona DNSSEC que tiene una cadena completa de la confianza de la raíz. Puesto que la cadena de confianza se debe remontar a una raíz de confianza sin interrupción con el fin de validar, anclas de confianza aún deben configurarse para las zonas seguras, si cualquiera de las zonas por encima de ellos no son seguros. Por ejemplo, si la zona "signed.example.org" estaba asegurada pero la zona "example.org" no lo fue, entonces, a pesar de que la zona ".org" y la raíz se firmó, hay que tener un ancla de confianza para validar la zona.

Las cuestiones políticas que rodean la firma de la raíz han sido una preocupación continua, principalmente sobre algunas cuestiones centrales:
 Otros países están preocupados por el control de Estados Unidos sobre el Internet, y pueden rechazar cualquier esquema centralizada de claves por esta razón.
 Algunos gobiernos podrían tratar de prohibir la distribución de claves de encriptación respaldadas por DNSSEC.

 Planificación

En septiembre de 2008, la ICANN y VeriSign publicaron cada uno propuestas de implementación y, en octubre, la Administración Nacional de Telecomunicaciones e Información (NTIA) pidió los comentarios del público. No está claro si los comentarios recibidos afectaron el diseño final del plan de implementación.

El 3 de junio de 2009, el Instituto Nacional de Estándares y Tecnología (NIST) anunció planes de firmar la raíz a finales de 2009, conjuntamente con ICANN, VeriSign y la NTIA.

El 6 de octubre de 2009, en la 59a reunión de la Conferencia RIPE, ICANN y VeriSign anunciaron el calendario de despliegue previsto de DNSSEC en la zona raíz. En la reunión se anunció que sería gradualmente desplegado a un servidor de nombres raíz al mes, comenzando el 1 de diciembre de 2009, con el último servidor de nombres raíz ofreciendo una zona firmada DNSSEC el 1 de julio de 2010, y la zona de la raíz se firmará con una DNSKEY RSA/SHA256. Durante el período de puesta en marcha gradual la zona de las raíces servirá una Deliberately Unvalidatable Root Zone (DURZ) que utiliza llaves falsas, con el registro DNSKEY final sin ser distribuido hasta el 1 de julio de 2010. Esto significa que las claves que usadas para firmar el uso de zona son deliberadamente no verificables; la razón de este despliegue era para monitorear los cambios en los patrones de tráfico causados por las mayores respuestas a las consultas que soliciten los registros de recursos DNSSEC.

El dominio .org de nivel superior ha sido firmado con DNSSEC en junio de 2010, seguido por .com, .net y .edu más tarde en 2010 y 2011. Los dominios de código de país de primer nivel fueron capaces de depositar las llaves a partir de mayo de 2010. A noviembre de 2011, más de 25% de los dominios de nivel superior están firmados con DNSSEC.

 Implementación

El 25 de enero de 2010, el servidor raíz L (ele) comenzó a ofrecer una Deliberately Unvalidatable Root Zone (DURZ). La zona utiliza firmas de hash SHA-2 (SHA-256) creado usando el algoritmo RSA, según se define en el RFC 5702. A mayo de 2010, todos los trece servidores raíz han comenzado a ofrecer la DURZ. El 15 de julio de 2010, se firmó la primera zona raíz DNSSEC para producción, con el serial SOA 2010071501. Las anclas de confianza raíz están disponibles en IANA.

 Despliegue a nivel de TLD

Debajo de la raíz hay un gran conjunto de dominios de nivel superior que debe ser firmado con el fin de lograr un despliegue de DNSSEC completo. La lista de dominios de nivel superior de Internet proporciona detalles acerca de cuáles de los dominios de nivel superior existentes han sido firmados y ligados a la raíz.

 Validación DNSSEC Lookaside

En marzo de 2006, el Internet Systems Consortium introdujo el registro de validación *DNSSEC Lookaside* (DLV). DLV fue pensado para hacer más fácil de implementar DNSSEC en ausencia de un ancla de confianza raíz. En el momento en que fue imaginado que un validador podría tener que mantener un gran número de anclas de confianza correspondientes a subárboles firmadas del DNS. El propósito de DLV era permitir que los validadores para descargar el esfuerzo de la gestión de un repositorio de confianza de anclaje a una confianza tercero. El registro DLV mantiene una lista central de anclas de confianza, en lugar de cada validador repetir el trabajo de mantener su propia lista.

Para utilizar DLV, se necesita un validador que lo soporte, como BIND o Unbound, configurado con un ancla de confianza para una zona DLV. Esta zona contiene los registros DLV; éstos tienen exactamente el mismo formato que los registros DS, pero en lugar de referirse a una sub-zona delegada, se refieren a una zona en otro lugar en el árbol DNS. Cuando el validador no puede encontrar una cadena de confianza desde la raíz hasta la RRset que está tratando de comprobar, busca un registro DLV que puede proporcionar una cadena alternativa de confianza.

DLV sigue siendo útil después de la raíz se ha firmado. Mientras que existen lagunas en la cadena de confianza, tales como dominios de nivel superior sin firmar, o registradores que no admitan delegaciones de DNSSEC, hostmasters de dominios de nivel inferior pueden utilizar DLV para que sea más fácil para sus usuarios validen sus datos DNS.

 Iniciativa de despliegue de DNSSEC del gobierno de EE.UU

La Dirección de Ciencia y Tecnología del Departamento de Seguridad Nacional (DHS) patrocina la "Iniciativa de implementación de DNSSEC". Esta iniciativa anima a "todos los sectores para adoptar voluntariamente medidas de seguridad que mejoren la seguridad de la infraestructura de nombres de Internet, como parte de un esfuerzo global, cooperativo que involucra a muchas naciones y organizaciones de los sectores público y privado." DHS también financia esfuerzos para madurar DNSSEC y conseguir que se despliegue dentro del gobierno federal de Estados Unidos.

Se informó que el 30 de marzo de 2007, el Departamento de Seguridad Nacional de Estados Unidos propuso "tener la clave para firmar la zona raíz del DNS sólidamente en manos del gobierno de Estados Unidos." Sin embargo no había funcionarios del gobierno de Estados Unidos presentes en la sala de reuniones y el comentario que desató el artículo fue hecho por un tercero. DHS comentó más adelante sobre por qué creían que los demás saltaron a la falsa conclusión de que el Gobierno de Estados Unidos había hecho una propuesta de este tipo: "El Departamento de Seguridad Nacional de Estados Unidos está financiando el desarrollo de un plan técnico para la implementación de DNSSEC, y el pasado octubre distribuyó un primer borrador de la misma a una larga lista de expertos internacionales para que formulen observaciones. el proyecto establece una serie de opciones para el que podría ser el titular, u "operador" de la Zona clave raíz, esencialmente llegando a una agencia gubernamental o un contratista. "en ninguna parte del documento hacemos que cualquier propuesta sobre la identidad de la Raíz del operador principal," dijo Maughan, el gerente de investigación y desarrollo de la seguridad cibernética para la Seguridad de la Patria ".

 Despliegue de DNSSEC en el gobierno de EE.UU

El NIST produjo una publicación especial, la NIST Special Publication 800-81 Guía de Implementación de Domain Name System (DNS) seguro el 16 de mayo de 2006, con orientación sobre cómo implementar DNSSEC. NIST pretendía liberar requisitos nuevos para la nueva Ley de Gestión de Seguridad de la Información DNSSEC Federal (FISMA) en NIST SP800-53-R1, haciendo referencia a esta guía de implementación. Las agencias estadounidenses podrían entonces haber tenido un año después de la publicación final del NIST SP800-53-R1 para cumplir con estos nuevos requisitos de FISMA. Sin embargo, en ese momento NSEC3 no se había completado. NIST había sugerido el uso de dominios divididos, una técnica que se sabe que es posible, pero que es difícil de implementar correctamente, y tiene las debilidades de seguridad mencionados anteriormente. El 22 de agosto de 2008, la Oficina de Administración y Presupuesto (OMB) dio a conocer un memorando que requieren las agencias federales de Estados Unidos para implementar DNSSEC en todos los sitios .gov; la raíz .gov debía ser firmada en enero de 2009, y todos los subdominios bajo .gov debían ser firmados en diciembre de 2009. Si bien la nota se centra en los sitios .gov, la Agencia de Sistemas de Información de Defensa de Estados Unidos dice que tiene la intención de cumplir con los requisitos de la DNSSEC de la OMB en el dominio .mil (militar EE.UU.) también. Carolyn Duffy Marsan de NetworkWorld declaró que DNSSEC "no ha sido desplegado ampliamente, ya que sufre de un clásico dilema del huevo y la gallina ... con el mandato de la OMB, parece que el huevo se está resquebrajando".

 Despliegue en resolvers

Varios proveedores de Internet han comenzado a implementar resolvers recursivas DNS con validación DNSSEC. Comcast se convirtió en el primer ISP importante hacerlo en los Estados Unidos, anunciando sus intenciones el 18 de octubre de 2010 [62] [63] y completando el despliegue el 11 de enero de 2012.

Según el estudio de CircleID, la proporción de clientes que utilizan exclusivamente resolución de DNS que realizan la validación DNSSEC se ha elevado hasta el 8,3% en mayo de 2013. Cerca de la mitad de estos clientes estaba usando resolución del DNS público de Google.

 DNS Público de Google

Google Public DNS es un servicio de DNS público, proporcionado libremente, que permite usar DNSSEC plenamente.

En su lanzamiento en 2009, Google Public DNS no permitía DNSSEC. Los registros RRSIG por supuesto podían ser consultados, pero el flag AD (Datos Autenticados, lo que significa que el servidor fue capaz de validar las firmas de todos los datos) nunca fue marcada.

El 28 de enero de 2013, los servidores DNS de Google comenzaron silenciosamente a proporcionar información de validación DNSSEC, pero solo si el cliente establece de manera explícita el flag DNSSEC OK (DO) en su consulta.

El 6 de mayo de 2013, Google Public DNS habilita la validación DNSSEC de forma predeterminada; es decir todas las consultas serán validados a menos que los clientes optan explícitamente.

 Problemas

Se ha sabido que Exchange 2013 y versiones anteriores tienen un problema, donde la búsqueda de registros MX causa errores #550 4.4.7 QUEUE.Expired.

 Herramientas

El despliegue de DNSSEC requiere software tanto en el servidor como en el cliente. Algunas de las herramientas que soportan DNSSEC incluyen:

 Windows 7 y Windows Server 2008 R2 incluyen un stub resolver "consciente de la seguridad" que es capaz de diferenciar entre las respuestas seguras y no seguras de un servidor de nombres recursivo.
 BIND, el servidor DNS nombre más popular (que incluye dig). La versión 9.3 implementó el nuevo *DNSSEC-bis* (registros DS), aunque no soporta los registros NSEC3. BIND 9.6 fue lanzado en diciembre de 2008 y tiene soporte completo para los registros NSEC3.
 drill es una herramienta como dig habilitada para DNSSEC incluida en el paquete ldns.
 extensión de drill para Firefox agrega a Mozilla Firefox la capacidad de determinar si un dominio se puede verificar usando DNSSEC.
 DNSSEC-Tools tiene como objetivo proporcionar herramientas fáciles de usar para ayudar a todo tipo de administradores y usuarios a hacer uso de DNSSEC. Ofrece herramientas para administradores de las zonas zonas autoritativas, servidores autoritativos, y servidores recursivos, así como una biblioteca y herramientas para desarrolladores de aplicaciones y parches para extender aplicaciones comunes.
 Zone Key Tool es un software diseñado para facilitar el mantenimiento de las zonas conscientes de DNSSEC. Está diseñado principalmente para entornos con un número pequeño o mediano de zonas y ofrece un despliegue totalmente automático de firmado de clave, así como su refirmado automático.
 Unbound es un servidor de nombres DNS que se ha escrito desde cero diseñado en torno a los conceptos de DNSSEC.
 GbDns es un servidor de nombres para Microsoft Windows compacto y fácil de instalar.
 UnxsBind es un software de gestión de DNS GPL para ASPs de DNS que ahora es compatible con DNSSEC.
 OpenDNSSEC es una herramienta para firmar DNSSEC usando PKCS#11 para ser interfaz con módulos de seguridad de hardware.
 SecSpider rastrea el despliegue de DNSSEC, monitorea zonas y proporciona una lista de claves públicas observadas.
 DNSViz y DNSSEC Analyzer son herramientas basadas en Web para visualizar la cadena de autenticación de DNSSEC de un dominio.
 DNSSEC Validator es un complemento de Mozilla Firefox para la visualización del estado de DNSSEC del nombre de dominio visitado.
 DNSSHIM o maestro DNS seguro oculto (*DNS Secure Hidden Master*) es una herramienta de código abierto para automatizar las zonas de apoyo DNSSEC el proceso de aprovisionamiento.
 Net::DNS::SEC es un resolver DNS implementado en Perl.

 Véase también

 Mecanismos de extensión de DNS permiten los paquetes más grandes que DNSSEC utiliza y el bit de señalización DO
 DNSCurve
 Privacidad digital

 Referencias

 Enlaces externos

 Organizaciones / sitios web

 Sitio web de información de DNSSEC
 Extensiones DNS del grupo de trabajo IETF
 Noticias y opiniones sobre temas relacionados con DNSSEC
 Proyecto DNSSEC-Tools
 Iniciativa de coordinación de despliegue de DNSSEC
 Equipo de despliegue de DNSSEC
 Equipo de operaciones de DNS de ICANN
 DNSSEC (FAQ) LACNIC

 Otros documentos

 Una Mirada Fundamental de DNSSEC, despliegue, y Extensiones de seguridad DNS de Geoff Huston
 "Uso del Sistema de Nombres de Dominio para el sistema de Robos" por Steve Bellovin, 1995
 Una corta línea de tiempo de DNSSEC por Miek Gieben
 Habilitando la resolución de nombres segura usando DNSSEC para diversas aplicaciones
 DNSSEC Howto por Olaf Kolkman (RIPE NCC / NLnet Labs)
 Cómo garantizar su (inversa) de zona por Holger Zuleger
 seguridad para el correo electrónico más fácil en camino?
 "DNSSEC y la enumeración de zona" por Marcos Sanz (DENIC)
 NIST Special Publication (SP) 800-81, Guía de implementación de Sistema de Nombres de Dominio (DNS) Seguro, de mayo de 2006
 Bootstrapping la adopción de los protocolos de seguridad de Internet, Andy Ozment y Stuart E. Schechter, 26 a 28 junio, 2006
 explicación de DNSSEC y firma de la Zona Raíz (Parte I), documento sobre DNSSEC por ccNSO, febrero de 2008
 , febrero de 2003
 Cybertelecom:: Seguridad de DNS y Política de gobierno de Estados Unidos
 SecSpider herramienta para el rastreo de implementación de DNSSEC
 Petición para firmar la raíz
 DNSSEC en 6 minutos por Alan Clegg, Internet Systems Consortium (PDF-Datei, 315 kB)
 la implementación de DNSSEC  Cisco Internet Protocol Journal
 Lista de dominios de nivel superior (TLD) con DNSSEC implementado
 Informe de ICANN de DNSSEC en TLDs  (generado diariamente)
