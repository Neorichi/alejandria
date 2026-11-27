---
type: Artículo de enciclopedia
title: Tor (red de anonimato)
description: "Tor (sigla de The Onion Routing, en español «El enrutador cebolla») es un proyecto cuyo objetivo principal es el desarrollo de una red de comunicaciones distribuida de baja latencia y superpuesta sobre internet, en la …"
resource: https://es.wikipedia.org/wiki/Tor_(red_de_anonimato)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Tor_(red_de_anonimato)"}
license: CC BY-SA 4.0
id: eswiki-Tor_(red_de_anonimato)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Tor (red de anonimato)

- **Nombre:** Tor
- **Desarrollador:** The Tor Project
- **Última versión:** 0.4.9.15
- **Género:** Onion routing, Anonymity, Cultura libre, Comunidad
- **Lenguaje programación:** C, Python, Rust
- **Sistema operativo:** Unix-Like (Android, Linux, BSD, MacOS X, Microsoft Windows
- **Licencia:** Licencia BSD Triclausula
- **Estado:** En desarrollo
- **Idiomas:** Multilingüe
- **Español:** Parcialmente

**Tor** (sigla de ***T**he **O**nion **R**outing,* en español «El enrutador cebolla») es un proyecto cuyo objetivo principal es el desarrollo de una red de comunicaciones distribuida de baja latencia y superpuesta sobre internet, en la que el encaminamiento de los mensajes intercambiados entre los usuarios no revele su identidad, es decir, su dirección IP (anonimato a nivel de red) y que, además, mantenga la integridad y el secreto de la información que viaja por ella. Por este motivo se dice que esta tecnología pertenece a la llamada *darknet* o red oscura, que no se debe confundir con la *deep web* o web profunda.

Para la consecución de estos objetivos se ha desarrollado un software libre específico. Tor propone el uso de encaminamiento de cebolla de forma que los mensajes viajen desde el origen al destino a través de una serie de encaminadores especiales llamados 'enrutadores de cebolla' (en inglés *onion routers*). El sistema está diseñado con la flexibilidad necesaria para que pueda implementar mejoras, se despliegue en el mundo real y pueda resistir diferentes tipos de ataque. Sin embargo, tiene puntos débiles y no puede considerarse un sistema infalible.

No es una «red entre iguales» ya que, por un lado, están los usuarios de la red y, por otro lado, los encaminadores del tráfico y algunos de los cuales hacen una función de servicio de directorio.

La red funciona a partir de un conjunto de organizaciones e individuos que donan su ancho de banda y poder de procesamiento.
Según información obtenida de los documentos de alto secreto filtrados por Edward Snowden en 2013, la Agencia de Seguridad Nacional (NSA) de Estados Unidos habría, supuestamente, conseguido "romper" Tor y así descubrir las identidades de los usuarios que buscan el anonimato.

En 2021, el sitio web *restoreprivacy.com* acusa a Tor de que ya no es seguro, alegando que los gobiernos pueden romperlo.

 Historia
El 20 de septiembre de 2002 se anunció una versión alfa del software libre con la red del encaminamiento de cebolla en funcionamiento. Creado en 2003 por Roger Dingledine, Nick Mathewson y Paul Syverson surgió como la evolución del proyecto Onion Routing del Laboratorio de Investigación Naval de los Estados Unidos (por eso se dice que es la segunda generación de *onion routing*). Inicialmente financiado por el Laboratorio de Investigación Naval de los Estados Unidos. A finales de 2004 pasó a ser patrocinado por la Electronic Frontier Foundation, la organización de defensa de libertades civiles en el mundo digital, hasta noviembre de 2005. Actualmente el proyecto Tor está en manos de The Tor Project una organización sin fines de lucro orientada a la investigación y la educación, radicada en Massachusetts y que ha sido financiada por distintas organizaciones. Actualmente el proyecto está formado por un equipo liderado por Roger Dingledine.

En marzo de 2011, Tor recibió de la Free Software Foundation el premio para proyectos de beneficio social correspondiente a 2010 por «haber permitido que, aproximadamente, 36 millones de personas de todo el mundo, usando software libre, hayan experimentado libertad de acceso y de expresión en Internet manteniendo su privacidad y anonimato. Su red ha resultado crucial en los movimientos disidentes de Irán y Egipto».

 Aplicación y limitaciones

El objetivo principal de Tor es conseguir que internet pueda usarse de forma que el encaminamiento de los mensajes proteja la identidad de los usuarios. Es decir, persigue que no se pueda rastrear la información que envía un usuario para llegar hasta él (su dirección IP). El uso más habitual de Tor es aprovechar sus características para lograr cierto grado de privacidad en la navegación web en internet. Sin estar especialmente diseñado para ello, pronto se descubrió que Tor también hace más difícil la labor de programas que intentan censurar o vigilar el acceso a cierto tipo de contenidos. Todo esto ha provocado que Tor sea muy usado en entornos en los que los comunicantes están especialmente motivados en proteger su identidad y el contenido de sus comunicaciones (por ejemplo, conflictos políticos, restricciones en la difusión y acceso a ciertos tipos de contenido, comunicación de información confidencial, etc.).

El **enrutado anónimo**  no asegura el que la entidad origen sea desconocida para la entidad destino. Esto se debe a que los protocolos de nivel superior pueden transmitir información sobre la identidad. Por ejemplo, un servicio web puede usar cookies o simplemente pedir que nos identifiquemos. Cuando queremos un anonimato a nivel de aplicación es bueno configurar el cliente adecuadamente y protegernos usando proxys que modifican los contenidos en este sentido. Por ejemplo, para conseguir más privacidad cuando navegamos por la web es recomendable configurar el navegador adecuadamente (por ejemplo, deshabilitando cookies, no permitiendo plugins Java, Flash o ActiveX, o deshabilitando el historial) y redirigir el tráfico hacia un proxy web intermedio (ej., privoxy o pólipo) que nos filtre contenido que puede ser aprovechado para violar nuestra privacidad (por ejemplo, cookies o cabeceras HTTP que puedan ser usadas para identificar).

La red Tor cifra la información a su entrada y la descifra a la salida de dicha red (encaminamiento de cebolla). Por tanto, el propietario de un enrutador de salida puede ver toda la información cuando es descifrada antes de llegar a Internet, por lo que, aunque no pueda conocer el emisor, sí que puede acceder a la información. Esta debilidad ha sido aprovechada por algunos atacantes. Por ejemplo, Dan Egerstad, un sueco experto en seguridad informática, creó un servidor en la red Tor y controlando toda la información que salía por él hacia Internet, pudo conseguir contraseñas de importantes empresas, embajadas de todo el mundo y otras instituciones. Para paliar esta debilidad y asegurarnos de que nadie accede a la información que se está enviando, es recomendable usar un protocolo que provea cifrado al protocolo de aplicación como SSL. Por ejemplo, para tráficos HTTP es recomendable usarlo sobre SSL (HTTPS).

Como hemos comentado, Tor es usado principalmente para ocultar la identidad de los usuarios que utilizan servicios habituales de internet. Sin embargo, también proporciona características que permiten la comunicación interactiva de entidades que quieren ocultar su identidad (mediante los llamados *puntos de encuentro*) y proveer servicios ocultando la identidad de la entidad que provee dicho servicio (mediante los llamados *servicios ocultos*).

 Interfaz de entrada
Tor solo permite anonimizar tráfico TCP. Las aplicaciones acceden a la red Tor a través de la interfaz SOCKS lo cual significa que toda aplicación con soporte SOCKS puede usar Tor para realizar comunicaciones anónimas sin necesidad de modificaciones adicionales. El **cliente Tor** recibe tráfico SOCKS desde nuestras aplicaciones y luego, de forma transparente, se encarga de comunicarse con los **routers de la red Tor** para enviar las peticiones y posteriormente devolvernos los resultados.

SOCKS es un protocolo que facilita el enrutamiento de paquetes que se envían entre un cliente y un servidor a través de un servidor proxy. Según la pila de protocolos OSI está en el nivel 5 (sesión). Según la pila de protocolos IP está en la capa de aplicación. En los primeros intentos de usar (encaminamiento de cebolla), se requería un proxy de aplicación para cada protocolo de aplicación soportado. Esto conllevaba mucho trabajo y provocaba que algunos proxys no fueran escritos nunca y, por tanto, algunas aplicaciones nunca fueron soportadas. Tor usa SOCKS para, de un plumazo, soportar la mayoría de programas basados en TCP sin hacer ninguna modificación.

Observar que cuando navegamos por internet hacemos dos tipos de peticiones:
 Peticiones DNS para que el servidor de DNS que nos diga la dirección IP de una URL
 Peticiones HTTP a las direcciones IP del servidor web que aloja la información.

Si no pasamos por Tor las búsquedas con DNS que hacen los navegadores, pueden ser un problema de privacidad, ya que si las peticiones se mandan directamente a través de la red regular, un atacante podría deducir qué sitios se están visitando a través de Tor, ya que antes de navegar por ellos se pregunta por DNS qué IP tienen. Por tanto, es necesario redirigir el tráfico de DNS por la red Tor.

Algunas aplicaciones convierten directamente el tráfico del protocolo de la capa de aplicación en tráfico SOCKS. Por ejemplo, Firefox permite convertir tanto el tráfico DNS como el HTTP a SOCKS y enviárselo al cliente Tor. Otras aplicaciones necesitan redirigir el tráfico del protocolo de la capa de aplicación hacia un proxy que realice la conversión al protocolo SOCKS. Por ejemplo, si tuviéramos un navegador que no permitiera el tráfico HTTP y DNS, vía SOCKS podría usar privoxy para realizar esta tarea (y podríamos aprovechar para filtrar las peticiones HTTP). Si tenemos una aplicación genérica que no soporta SOCKS y queremos que su tráfico TCP se convierta a formato SOCKS para luego pasarlo al cliente Tor, es necesario utilizar una aplicación adicional. En linux podríamos usar el comando torify (de ahí viene el término **torificar**). En Windows podríamos usar Freecap (software libre), SocksCap o Torcap.

 Funcionamiento

 Componentes
Está formada por una serie de nodos que se comunican mediante el protocolo TLS sobre TCP/IP manteniendo así secreta e íntegra, sin modificaciones externas, la información desde un nodo a otro. Hay dos tipos de entidades:

 Nodos OR o simplemente OR (del inglés *Onion Router*): Funcionan como encaminadores y en algunos casos además como servidores de directorio (DNS) de una especie de servicio de mantenimiento. Los nodos OR mantienen una conexión TLS con cada uno de los otros OR. Las conexiones OR-OR no son nunca cerradas deliberadamente, salvo cuando pasa cierto tiempo de inactividad. Cuando un OR comienza o recibe nueva información de directorio, él intenta abrir nuevas conexiones a cualquier OR que no esté conectado.
 Nodos OP o simplemente OP (del inglés *Onion Proxy*): Los usuarios finales ejecutan un software local que hace la función de nodo OP y que su función es obtener información del servicio de directorio, establecer circuitos aleatorios a través de la red y manejar conexiones de aplicaciones del usuario. Los OP aceptan flujos TCP de aplicaciones de usuarios y las multiplexa a través de la red OR's. Las conexiones OR-OP  no son permanentes. Un OP debería cerrar una conexión a un OR si no hay circuitos ejecutándose sobre la conexión y ha vencido cierto temporizador.

 Servicio de directorio
El servicio de directorio publica una base de datos que asocia a cada OR una serie de información (router descriptor). Esta información es accesible a todos los OR y a todos los usuarios finales y la usan para tener un conocimiento de la red. Si se tienen pocos servidores de directorio, se corre el riesgo tener un punto cuyo fallo puede ocasionar el fallo del sistema completo. Por motivos de backup y de latencia, los OR que dan el servicio de directorio mantienen duplicada la información pasándosela de unos a otros. Hay una serie de OR principales (autoridades de directorio) y luego hay otros secundarios que hacen de cachés y backup (directory caches). Una lista de algunos servidores de directorio son distribuidos con Tor para facilitar la suscripción a la red (bootstrapping). Los servidores de directorio son en realidad un grupo establecido de ORs confiables. Para dar fiabilidad a la información que da el servicio de directorio las entradas son protegidas criptográficamente con firmas y solo la información que proviene de ORs aprobados será publicada en la base de datos. Por tanto, todo nodo nuevo tiene que ser previamente aprobado y de esta forma se evitan ataques en los que alguien añade muchos nodos no confiables. No hay sistema automático para aprobar OR's. Los administradores del servidor de directorio lo hacen manualmente.

Cuando un OR se arranca, recolecta un conjunto de datos que lo describen a él, a su modo de funcionamiento y capacidades. Ejemplos de este tipo de atributos son la dirección IP, nombre amigable para el usuario, versión del software Tor, sistema operativo, clave pública, exit policies (restricciones a como puede funcionar el nodo si es el último nodo de un circuito de datos Ej: definir una lista de direcciones IP y número de puertos a los cuales está dispuesto llevar el tráfico. Observar que usando esto se puede hacer que un nodo no pueda actuar como último nodo de un circuito nunca).  Toda esta información se publica a través del servicio de directorio.

 Esquema básico
El funcionamiento a grandes rasgos es el siguiente:
 A partir de la información obtenida de su configuración y del servicio de directorio el OP decide un circuito por el que van a circular los paquetes. Por defecto, el circuito tiene 3 nodos OR.
 El OP negocia, usando un enfoque telescópico, las claves de cifrado necesarias con cada OR del circuito para proteger sus datos en todo el camino antes de realizar transmisión alguna. La obtención de las claves simétricas (AES-128), una para cada sentido de comunicación (Kf<- forward key, Kb<-backward key), se realiza a partir del protocolo de establecimiento de claves Diffie-Hellman para obtener una clave compartida y a partir de ella derivar las dos claves simétricas. El circuito es construido desde el punto de entrada (usuario) de la siguiente forma: Los mensajes para negociar las claves de la comunicación entre ORn y ORn+1 se realizan a petición del OP y retransmitiendo paquetes a través de los nodos OR1,... ORn. En cada paso los mensajes son cifrados con las claves de sesión negociadas, o cuando no lo están, con la clave de cebolla del host que recibe el dato
 A continuación cifra el paquete que contiene la clave para el último OR del circuito.
 A continuación hace lo propio del penúltimo.
 Hace lo mismo con todos los nodos hasta hacer lo propio con el paquete para el primer nodo.
 Envía el paquete resultante al primer nodo del circuito. Observar que el paquete construido con este proceso se puede considerar como un paquete envuelto en varias capas de cifrado. Por eso se usa la metáfora de la cebolla para describir este tipo de método de encaminamiento (encaminamiento de cebolla).
 El primer OR quita 'su' capa de la cebolla y envía el paquete al siguiente nodo.
 Según va llegando el paquete a cada OR este pela la capa externa. De esta forma, ningún OR puede hacerse con la imagen completa del circuito, ya que solo conoce los OR/OP anterior y posterior.

Como terminología se llama 'exit server' o 'exit node' al último servidor del circuito (y, por tanto, el único que se comunica con el destino), el primer OR se le llama 'entry node' (único que se comunica con el origen de la comunicación) y al resto de nodos se les llama middle-node.

Podemos observar que la forma en la que se establecen las claves y todas estas capas de cebolla que se construyen con ellas permiten que la información permanezca secreta mientras va circulando por el circuito de nodos OR. Además, al estar el cifrado de las capas basado en claves de sesión, aunque un atacante recopilara todos los mensajes, no podría descifrarlos una vez que estas claves de sesión son descartadas por el OR (perfect forward secrecy).

 Puntos de encuentro
La idea de los puntos de encuentro, denominados por las siglas RP (del francés *Rendezvous Points*), es, en lugar de explícitamente enviar un paquete a un destino, establecer un punto de encuentro que actúe como nivel de indirección. De esta forma desacoplamos el acto de enviar del acto de recibir. Cada extremo de la comunicación envía sus mensajes a ese punto de encuentro y desde ahí son enviados a donde corresponda usando circuitos que esconden la localización del destino. Por ejemplo podríamos usar este sistema para conectarnos a un servidor de chat IRC.

 Servicios ocultos
Los servicios que ocultan la localización (por ejemplo, la dirección IP) de quien provee el servicio (Ej., un servicio web accesible solo desde la red de encaminamiento de cebolla) se les suele llamar **servicios de localización oculta** (en inglés *location-hidden services*) o simplemente **servicios ocultos** (en inglés *hidden services*).

Para soportar esta funcionalidad, los proveedores de servicios generan una clave pública y privada para identificar su servicio. A continuación anuncian su servicio a distintos routers, haciendo peticiones firmadas con su clave pública, para que sirvan como punto de contacto. A los routers con esta función se les llama **puntos de introducción**, en inglés *introduction point*. El proveedor de servicio asocia a su servicio una FQDN del pseudo-TLD .onion y la publica en un servidor de directorio. La FQDN tiene la forma .onion donde el valor hash es de 16 caracteres en Base32 y está generado usando una función hash sobre la clave pública del servicio. Cuando un cliente se quiere conectar a cierta FQDN (por ejemplo, ha encontrado la dirección a través de un sitio web) consulta un servicio de búsqueda (*lookup service*) y este le indica un punto de introducción (*introduction point*) y la clave pública del servicio. Observar que para mantener el anonimato es necesario que la consulta del servicio de búsqueda se realice a través de Tor. A continuación el cliente se conecta con un *punto de encuentro* (esto lo podría haber hecho antes) y se establece un identificador de esa conexión (*rendezvous cookie*). A continuación el cliente le envía un mensaje, firmado con la clave pública del servidor, al *punto de introducción* indicándole el *punto de encuentro* donde está, el identificador que permita identificar al cliente en el *punto de encuentro* (la *rendezvous cookie*) y parte del protocolo Diffie-Hellman (*start of a DH handshake*). A continuación, el *punto de introducción* envía el mensaje al servidor del servicio, el cual determina si se conecta al *punto de encuentro* para proveerle el servicio o no. Si determina que quiere conectarse con él, entonces se conecta al *punto de encuentro* y le indica a este el identificador del cliente con el que quiere conectarse (la *rendezvous cookie*), la segunda parte del Diffie-Hellman (*the second half of the DH handshake*) y un hash de la clave que comparten. A continuación, el *punto de encuentro* conecta al cliente y al servidor y se establece una comunicación normal.

 Células
Una vez que se establece la conexión TLS, ya sea OP-OR u OR-OR, las entidades se envían paquetes de información estructurada llamadas células. Estas células tienen tamaño fijo de 512 bytes y pueden ser enviadas en registros TLS de cualquier tamaño o dividido en varios registros. Los registros de TLS no tienen que revelar ninguna información sobre el tipo o el contenido de las células que contiene. Varios circuitos pueden ser multiplexado sobre una misma conexión TLS. Las células están formadas por una cabecera y una carga útil.

Formato:

 **circID**.- Es el identificador de circuito y especifica el circuito al que se refiere la célula.
 **CMD**.- Indica el comando que especifica el significado de la célula. Atendiendo al tipo de comando (valor de CMD) hay 2 tipos de células: Células de control y Células de transmisión.

 Células de control
Las células de control (en inglés *control cell*) son siempre interpretadas por el nodo que las recibe y permiten controlar la comunicación.

Comandos que tienen estas células:
 **PADDING** (código 0).- Actualmente no usadas porque los ataques existentes funcionan incluso con tráfico de relleno  y porque el tráfico que provocan incrementa el ancho de banda necesario. Además de éstas, las celdas del tipo RELAY_DROP puede crearse también para crear también  tráfico de relleno.
 **CREATE** (código 1).- Para crear circuito.
 **CREATED** (código 2).- ACK de CREATE.
 **DESTROY** (código 4).- Destruir circuito.
 **CREATE_FAST**  (código 5).- Crear un circuito reaprovechando operaciones de clave pública existentes),
 **CREATED_FAST** (código 6).- ACK de CREATE_FAST.
 **VERSIONS** (código 7).- Usado cuando se establecen las conexiones).
 **NETINFO** (Código 8).- Usado cuando se establecen las conexiones).
 **RELAY_EARLY** (código 9).

 Células de transmisión
Las células de transmisión (en inglés *relay cell*) son usadas para la comunicación entre el OP y cualquiera de los OR del circuito, normalmente el exit node. Por ejemplo, esto se usa cuando se quiere cambiar la parte final del path de un circuito (RELAY_TRUNCATE).

En las últimas versiones el sistema permite tráfico de salida desde nodos OR que no son los últimos del circuito. Esto permite frustrar ataques que se basan en la observación del tráfico de salida del exit node.

Este tipo de células se distinguen porque el valor del campo CMD siempre tiene el comando RELAY (código 3).

En este tipo de células el formato tiene campos que forman parte de la carga útil (PAYLOAD):

 **Relay command**.- El subcomando RELAY que indica el funcionamiento de la celda.
Hay tres tipos de subcomandos relay:
forward: Son enviados desde el OP origen del circuito
backward: Son enviados desde los OR del circuito al OP origen
ambos: Pueden funcionar como forward o como backward
Posibles subcomandos:
**RELAY_BEGIN** (código 1).- De tipo forward
**RELAY_DATA** (código 2).- De tipo forward o backward
**RELAY_END** (código 3).- De tipo forward o backward.  Permite indicar el cierre de un stream TCP e indica el motivo
**RELAY_CONNECTED** (código 4).- De tipo backward
**RELAY_SENDME** (código 5).- De tipo forward o backward. A veces se usa para funciones de control (streamID=0)
**RELAY_EXTEND** (código 6).- De tipo forward. Se usa para funciones de control (como veremos streamID=0)
**RELAY_EXTENDED** (código 7).- De tipo backward. Se usa para funciones de control (streamID=0)
**RELAY_TRUNCATE** (código 8).- De tipo forward. Se usa para funciones de control (streamID=0)
**RELAY_TRUNCATED** (código 9).- De tipo backward. Se usa para funciones de control (streamID=0)
**RELAY_DROP** (código 10).- De tipo forward o backward. Se usa para funciones de control (streamID=0)
**RELAY_RESOLVE** (código 11).- De tipo forward
**RELAY_RESOLVED** (código 12).- De tipo backward
**RELAY_BEGIN_DIR** (código 13).- De tipo forward
Los códigos 32 al 40 son usados para servicios ocultos

 **Recognized**: Campo que junto con el campo digest permite identificar si la celda es para ser procesada localmente.
 **StreamID**: Es el identificador de flujo. De esta forma se permite que varios flujos puedan ser multiplexados en un solo circuito. Este campo permite identificar el stream al que nos referimos entre los múltiples streams del circuito. Es seleccionado por el OP y permite al OP y al exit nodo distinguir entre múltiples streams en un circuito. Las células que afectan al circuito entero en lugar de a un streamID particular tienen este campo a 0 y se pueden considerar como de control.
 **Digest**.- Permite el control de integridad extremo a extremo (**end-to-end integrity checking**). Contiene los primeros cuatro bytes de ejecutar SHA-1 sobre TODOS los bytes de células relay que han sido enviados a este nodo del circuito u originados desde este nodo del circuito (solo conocidos por el origen y el destino, ya que van cifrados), usando las semillas Df o Db respectivamente (solo conocidas por el origen y el destino), e incluyendo la carga útil entera de esta célula RELAY cogiendo el campo digest a zero. Por la visibilidad de los datos, un nodo intermedio nunca podría calcular este valor de digest. Se ha estimado con 4 bytes de digest la posibilidad de que un adversario adivine por casualidad un hash válido es suficientemente baja. Es claro que cada nodo necesita mantener el SHA-1 de los datos recibidos y enviados para poder ir calculando este digest.
 **length**.- Indica el número de bytes del campo DATA que contiene carga útil real. El resto del campo irá rellenado por bytes a NUL.

Una célula se considera **completamente descifrada** si el campo **Recognized** está a ceros y el campo **Digest** es el primero de los 4 bytes resultado de ejecutar la función de digest de todos los bytes 'destinados a' u 'originados desde' este salto del circuito. Si una celda no está **completamente descifrada** se pasa al siguiente salto del circuito. Si la célula se ha comprobado que está **completamente descifrada**, pero el comando de la célula no se entiende, la célula será borrada e ignorada, pero su contenido todavía cuenta respecto a los digests. Observar que el campo **Recognized** permite, de una forma muy rápida, descartar ciertas células como candidatas a estar **completamente descifradas**.

El contenido completo de la cabecera y de la carga útil es encriptado usando la clave AES-128 negociada en el establecimiento de circuito y haciendo un cifrado AES-128 en counter mode (AES-CTR).

 Claves de OR
Cada OR tiene asociados una serie de pares de claves pública/privada:
 Una **clave larga de identidad** (en inglés *Identity Key*) que sirve solo para firmar información (Ej: descriptor de las capacidades del OR o info de directorio cuando actúa como servidor de directorio) y certificados, y es usado para permitir identificación. Para denotar la clave de identidad del nodo OR n usamos **PKORn_ID**

 Una **clave mediana de enrutamiento de cebolla** (en inglés *Onion Key*) que sirve para cifrar las peticiones de establecimiento de circuito (CREATE) para negociar las claves efímeras. Las claves viejas deben ser aceptadas durante al menos una semana después de que haya sido cambiada para dar tiempo a que todo haya sido actualizado. Para denotar la onion key del nodo OR n usamos **PKORn_OK**

 Una **clave pequeña de conexión** (en inglés **Connection Key**) usada en el handshake TLS. Esta clave se mete en un certificado que se firma con la clave de identificación. Ambos certificados (certificado de la clave de conexión y certificado de la clave de identificación) se envían en el handshake del TLS. El certificado de la clave identificación está firmado por la clave de identificación. El certificado de la clave de identificación está autofirmado. Esta clave debería cambiarse frecuentemente, al menos una vez al día.

 Algoritmos de cifrado usados
 Para establecer las conexiones TLS usa TLS/SSLv3. Todos los OR y OP tienen que soportar SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA y deberían tener disponible TLS_DHE_RSA_WITH_AES_128_CBC_SHA. Los OP para comunicarse con los OR pueden usar: TLS_DHE_RSA_WITH_AES_256_CBC_SHA, TLS_DHE_RSA_WITH_AES_128_CBC_SHA, SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA, SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA
 Como algoritmo simétrico de cifrado se usa AES en counter mode (AES-CTR) con claves de 128 bits, con vector de inicialización con todos los bytes a 0
 Como algoritmo de clave pública usa RSA con claves de 1024 bytes y exponente fijo 65537. Usa como esquema de relleno OAEP-MGF1 con SHA-1 usado como función resumen
 Como función resumen usa SHA-1
 Para establecimiento de claves usa DH (Diffie-Hellman) con g=2 y para p usamos el primo seguro de 1024 bits obtenido de RFC 2409 con valor hexadecimal:

 FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E08
 8A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B
 302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9
 A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE6
 49286651ECE65381FFFFFFFFFFFFFFFF

 Funcionamiento detallado
 Establecimiento e inicialización de circuito

La cadena de OR´s que forman un circuito es construida de forma telescópica, esto es, el OP negocia las claves de sesión con cada sucesivo OR. Una ventaja de esta forma de operar es que se dejen una vez que estas claves de sesión se dejen de utilizar y sean borradas, aunque un nodo sea comprometido no se podrá descifrar células viejas (perfect forward secrecy). El esquema se realiza con siguientes pasos:
 El OP escoge un OR como exit node (ORn), de acuerdo con su exit policy.
 EL OP escoge una cadena de OR's para constituir el path del circuito (OR1....ORn) de forma que ningún OR aparece dos veces en el path.
 El OP abre una conexión TLS con el entry-node (OR1 ) si es que no la tenía abierta
 El OP escoge aleatoriamente un ID de circuito (circID) que no se esté utilizando en la conexión con el entry-node
 El OP inicia un intercambio de clave Diffie-Hellman con el entry-node enviando una celda CREATE
 El entry-node le devuelve una celúla CREATED y de esta forma se obtiene una clave compartida Diffie-Hellman (D-H). De esta clave se derivan dos claves simétricas, una para cada sentido:
 kf1 (forward key).- Se usará en la comunicación OP->OR1 del circuito
 kb1 (backward key).- Se usará en la comunicación OR1->OP.
 A continuación el OP envía una petición al OR1 para extender el circuito mediante una célula RELAY_EXTEND. Esta célula le indica al OR1 cual va a se el nuevo nodo OR2, su puerto y también contiene estructuras de datos que le tendrá que reenviar el OR1 al OR2 y que permitirán establecer un protocolo D-H de intercambio de claves entre el OP y OR2 a través de OR1 sin que el OR1 se entere de nada
 El OR1 coge la célula y realiza el procedimiento Diffie-Hellman escogiendo él mismo un nuevo circID apropiado. Observar que ahora las células CREATE/CREATED se intercambian entre el OR1 y el OR2.
 El OR1 manda al OP una célula RELAY_EXTENDED para mandarle lo que ha respondido el OR2 y así el OP tiene conocimiento de la clave D-H. La información está cifrada de tal forma que el nodo OR1 no puede acceder la información que se están intercambiando indirectamente el OP y OR2. De esta forma se establecen las nuevas claves simétricas: kf2 y kb2.
 De forma similar se continúa hasta conseguir que el OP tenga establecidas las claves kf1, kb1, kf2, kb2,..., kfn, kbn con los respectivos nodos OR.

En cada establecimiento de clave Diffie-Hellman se obtiene un valor g^xy que es usado para calcular un valor K obtenido con la siguiente fórmula:
K=H( g^xy | [00] ) |  H( g^xy | [01] )....|  H( g^xy | [04] )
donde:
| es la concatenación
[NN] es un byte cuyo valor es NN
H(x) es el SHA-1 de x
A partir de K se sacan una serie de valores derivados que se van usando en el proceso:
 **derivative key**  (KH): Primer HASH_LEN bytes. Usado en la respuesta del handshare para demostrar el conocimiento de la clave compartida
 **digest forward** (Df): Segundo HASH_LEN bytes. Es usado como semilla de la comprobación de integridad para flujos de datos desde OP a OR
 **backguard digest** (Db):Tercer  HASH_LEN bytes. Es usado como semilla de la comprobación de integridad para flujos de datos desde OR a OP
 **forward key** (Kf): Es usado para encriptar los flujos de datos desde OP a OR
 **backguard key** (Kb): Es usado para encriptar los flujos de datos desde OR a OP.

 Célula CREATE

Sobre el formato de la célula CREATE cabe señalar que el cifrado de g^x se hace de forma híbrida (con RSA-OAEP se cifra una clave de sesión y parte de g^x, con la clave de sesión se cifra el resto de g^x) para permitir que en una sola célula podamos hacer el intercambio del g^x completo.

Cuando inicializamos el primer salto de un circuito, el OP puede tener ya establecida la identidad del OR y negociado una clave secreta usando TLS. Por tanto, no siempre es necesario para el OP realizar operaciones de clave pública para crear el circuito. En este caso, el OP puede enviar una célula CREATE_FAST en lugar de una célula CREATE solo para el primer salto. El OR responde con un CREATED_FAST, cuando el circuito está creado. La célula CREATE_FAST contiene una clave X generada aleatoriamente. La célula CREATED_FAST contiene una clave Y generada aleatoriamente y un hash de la clave derivada construida a partir de X e Y. La clave compartida entre el OP y el OR será la concatenación de X e Y. Por tanto, cuando detectamos un CREATE_FAST podemos estar seguros de que el nodo OR es el primero del circuito. Por tanto, los ORs deberían rechazar intentos de crear streams con RELAY_BEGIN (que sirven para indicar a los nodos que son exit node y, por tanto, tienen que enviar el contenido a cierta IP) saliendo del circuito en el primer OR. De esta forma se evitan cierto tipo de ataques.

 Célula CREATED

El valor resumen de la clave establecida se manda para poder hacer una verficación de que ambos extremos de la comunicación comparten la misma clave.

 Célula RELAY_EXTEND

Son de especial interés los siguientes campos:
 La dirección (address) IPv4  y el puerto (port) del próximo OR del circuito.
 El campo streamID vale 0 porque este tipo de células relay sirven para control.
 El campo SHA-1(PCKS#1(PKOR1_ID)) es el hash SHA-1 del PKCS#1 con codificación ASN.1 de la clave de identidad (PKOR_ID) del próximo OR. Esto permite prevenir cierto tipo de ataques man-in-the-middle.
Observar que cuando el OR1 descifra con su clave AES obtiene distintos campos y entre ellos obtiene la siguiente piel de cebolla que puede utilizar directamente en la célula CREATE que tiene que construir para enviársela al OR2.

 Célula RELAY_EXTENDED

Observar que consiste en la comunicación de la respuesta al protocolo Diffie-Hellman que hace el OR2 al OP usando al OR1 como intermediario sin que este pueda inferir información alguna. El campo streamID vale 0 porque este tipo de células relay sirven para control.

 Encapsulamiento de *streams* TCP
Una vez que un circuito se ha establecido, se procede con el encapsulamiento de los *streams* TCP que contienen los datos de la aplicación.

Un circuito ya establecido se puede aprovechar para multiplexar en él varios streams TCP provenientes de la misma o de distintas aplicaciones. De hecho, por eficiencia, Tor usa el mismo circuito para nuevos streams TCP durante diez minutos, siempre que sea posible por la *exit policy *del *exit node*. Transcurridos los diez minutos, las peticiciones se darán a un nuevo circuito. Esto mejora la protección y evita que un atacante vincule tráficos antiguos con los nuevos.

El circuito permanecerá abierto hasta que todos los TCP *streams* que multiplexe hayan cerrado. Esta característica es necesaria para soportar muchos protocolos como SSH, los cuales son incapaces de mantener una sesión si se cambian los circuitos y, por tanto, el *exit node*, durante la sesión.

Los pasos para encapsular el tráfico TCP son los siguientes:

 El OP escoge un circuito abierto que tenga un *exit node* que le permita conectarse de la formada adecuada con el servidor. Si no existe, lo crea según el algoritmo visto anteriormente
 El OP selecciona un StreamID arbitrario que no haya sido utilizado todavía en el circuito
 El OP construye una célula RELAY_BEGIN que contiene, cifrado adecuadamente para que solo sea visto por el *exit node*, la dirección y el puerto destino de la comunicación.
 Esta célula es procesada por los nodos intermedios y el contenido útil es propagado hasta llegar en una célula RELAY_BEGIN que llega al exit-node
 El *exit node* obtiene la dirección y el puerto destino e intenta abrir una nueva conexión TCP con el *host* destino. Pueden suceder dos cosas.
 Si el *exit node* no puede establecer la conexión, devuelve una célula RELAY_END.
 Si el *exit node* puede establecer la conexión, devuelve una célula RELAY_CONNECTED que se irá propagando por la lista de OR´s hasta llegar al OP.
Una vez que la célula RELAY_CONNECTED llega al OP, este y el *exit node* empaquetan el *stream* de datos TCP en células RELAY_DATA

Si un OP quiere cerrar un *stream* TCP anonimizado, envía una célula RELAY_END a lo largo del circuito y los nodos van cerrando ese *stream* para su circuito. Cuando llega al *exit node*, este cierre la conexión TCP. El *exit node* genera una célula RELAY_ENDED que se propaga hasta el OP.

Si el *stream* TCP que mantiene el *exit node* con el destino se cierra de forma abrupta, entonces el *exit node* envía a lo largo del circuito hasta el OP una célula RELAY_TEARDOWN que indica el cierre inesperado de la conexión. Por el camino se van cerrando los *streams* de circuito asociados a stream TCP.

Una vez que un OR recibe una célula RELAY, comprueba el circID de la célula y determina si tiene un circuito que se corresponda con esta a lo largo de la conexión. Si no lo tiene, descarta la célula. Por otra parte, si el OR no es *exit node*, entonces cifra o descifra la carga útil del *stream* usando la clave kb o kf correspondiente con el OP. El OR decide si reconoce la célula que está **completamente descifrada**. Si el OR reconoce la célula, la procesa. Si no, la pasa a lo largo del circuito. Si el *exit node* no reconoce una célula RELAY ocurre un error y el OR envía una célula DESTROY para cerrar el circuito.

Cuando una célula RELAY llega al OP, el OP descifra la carga útil con kbi. Si la carga útil está **completamente descifrada** procesa la carga útil.

 Cierre y modificación de un circuito

Un circuito es cerrado cuando ocurre un error irrecuperable a lo largo del circuito o cuando el OP ve que todos los streams de un circuito están cerrados y el tiempo de vida del circuito ha terminado. Para cerrar un circuito, el OR o el OP envían una célula DESTROY que se va propagando y cerrando los circID asociados al circuito.

Una vez que se ha establecido un circuito y se está utilizando el OP puede decidir truncarlo (por ejemplo, porque se ha caído) y crear uno nuevo a partir de donde trunque. Se procede con los siguientes pasos:
 El OP escoge el OR donde se va a truncar y el OR nuevo que se quiere usar en el path.
 El OP construye una célula RELAY_TRUNCATE que llega hasta el OR a partir del cual se va a truncar.
 El OR desde el que se trunca comienza un proceso de cierre de circuito enviando una célula DESTROY.
 El OR desde el que se trunca lanza una célula RELAY_TRUNCATED hacia el OP.
 El OP cuando le llega el RELAY_TRUNCATED envía un RELAY_EXTEND para construir el nuevo circuito.

Cuando un error irrecuperable ocurre a lo largo de la conexión de un circuito, el OR debería, si está habilitado para ello, enviar al OP una célula RELAY_TRUNCATED; el nodo más lejano basta con enviar una célula DESTROY para cerrar el circuito.

También se cierra el circuito por parte de los ORs cuando ha habido algún error irrecuperable a lo largo del circuito

La carga útil de las células DESTROY o RELAY_TRUNCATED contienen solo un octeto que indican el motivo por el que el circuito debería ser cerrado o truncado. Este motivo es propagado a lo largo de los nodos

 Véase también
 Encaminamiento cebolla
 Encaminamiento ajo (en inglés)
 Grado de anonimato (en inglés)
 Peer-to-peer anónimo
 PirateBrowser
 Privoxy
 Freenet
 .onion
 I2P
 IPv6

 Bibliografía
 Tor Protocol Specification - Roger Dingledine, Nick Mathewson.
 Tor:Design e Simulaziones - Carmelo Badalamenti.
 Anonimato in Rete - Diodato Ferraioli, Enrico Rossomando.

 Referencias

 Enlaces externos
