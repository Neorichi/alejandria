---
type: Artículo de enciclopedia
title: Heartbleed
description: "Heartbleed (español: hemorragia de corazón) es un agujero de seguridad en la biblioteca de código abierto OpenSSL, solo vulnerable en su versión 1.0.1f, que permite a un atacante leer la memoria de un servidor o un …"
resource: https://es.wikipedia.org/wiki/Heartbleed
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Heartbleed"}
license: CC BY-SA 4.0
id: eswiki-Heartbleed
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Heartbleed

- **Descubridor:** Neel Mehta
- **Fecha de parchado:** 7 de abril de 2014

**Heartbleed** (español: hemorragia de corazón) es un agujero de seguridad en la biblioteca de código abierto OpenSSL, solo vulnerable en su versión 1.0.1f, que permite a un atacante leer la memoria de un servidor o un cliente, permitiéndole por ejemplo, conseguir las claves privadas SSL de un servidor. Investigaciones de auditorías en un principio creyeron que algunos atacantes podrían haber explotado este error desde al menos cinco meses antes de que fuera descubierto y publicado, pero más tarde se mostraron neutrales con respecto a sus afirmaciones y concluyeron que no podían demostrar este hecho, ya que se observó que otras herramientas podían generar los mismos registros (*logs*). Sin embargo, tampoco podían negar que no hubiesen sido intentos de ataque.

 Historia

 Aparición

La extensión Heartbeat para los protocolos Transport Layer Security (TLS) y Datagram Transport Layer Security (DTLS) se propuso como un estándar en febrero del 2012 por el RFC 6520. Esto provee una forma de probar y mantener viva un enlace de comunicación segura sin la necesidad de renegociar la conexión cada vez.

En 2011, uno de los autores del RFC, Robin Seggelmann, en ese tiempo un estudiante de doctorado en la Universidad de Duisburg-Essen, implementó la extensión Heartbeat para OpenSSL. Siguiendo la petición de poner su trabajo en OpenSSL, su cambio fue revisado por Stephen N. Henson, uno de los cuatro desarrolladores del núcleo de OpenSSL. Henson aparentemente no se dio cuenta del error en la implementación de Seggelmann, e introdujo el código con falla en el repositorio de OpenSSL el 31 de diciembre de 2011. El código vulnerable fue adoptado y usado ampliamente con el lanzamiento de la versión 1.0.1 de OpenSSL el 14 de marzo de 2012. El soporte de Heartbeat estaba habilitado de forma predeterminada, causando que las versiones afectadas fueran vulnerables por defecto.

 Descubrimiento

De acuerdo con Mark J. Cox de OpenSSL, Neel Mehta (Del equipo de seguridad de Google) reportó un Heartbleed en el 1 de abril de 2014. El bug implicó un severo error en el manejo de memoria en la implementación de la "Transport Layer Security Heartbeat Extension". Este defecto pudo ser usado para revelar más de 64 kilobytes de la memoria de la aplicación con cada heartbeat.

El *bug* fue nombrado por un ingeniero en la firma Codenomicon, una empresa finlandesa de ciber seguridad, quien aparte creó el logo y lanzó el dominio Heartbleed.com para explicar el bug al público en general.  De acuerdo con la propia empresa, Neel Mehta primero reportó el bug a OpenSSL, pero ambos, Google y Codenomicon, lo descubrieron independientemente. Codenomicon reporta al 3 de abril como su fecha de descubrimiento del bug y su fecha de notificación de NCSC-FI (formalmente conocido como CERT-FI) para coordinación de vulnerabilidades. Mehta además felicitó a Codenomicon, sin ir a detalles.

*The Sydney Morning Herald* publicó una línea del tiempo del descubrimiento el 15 de abril, la cual mostraba que algunas organizaciones podrían ser capaces de reparar el bug antes de su publicación. En algunos casos, no está tan claro cómo lo encontraron.

 Resolución

Bodo Moeller y Adam Langley de Google prepararon la corrección para Heartbleed. El parche resultante, que se añadió al seguimiento de incidencias de Red Hat, con fecha 21 de marzo de 2014. La fecha cronológica siguiente disponible en la evidencia pública es la afirmación de CloudFlare de que ellos solucionaron el defecto en sus sistemas el 31 de marzo de 2014. Stephen N. Henson aplica la corrección al sistema de control de versiones de OpenSSL, el 7 de abril. La primera versión corregida, 1.0.1g, fue lanzada el mismo día.

 Despliegue

Al , 318239 servidores web públicos eran todavía vulnerables.

 Renovación y revocación de certificados

Según Netcraft, alrededor de 30000 de los más de 500000 certificados X.509 que podrían haber sido comprometidos debido a Heartbleed habían sido reemitidos al 11 de abril de 2014, aunque menos habían sido revocados.

El 9 de mayo de 2014, sólo el 43% de los sitios web afectados habían reemitido sus certificados de seguridad. Además, el 7% de los certificados de seguridad reemitidos utilizaron las claves potencialmente comprometidos. «Mediante la reutilización de la misma clave privada, un sitio que se vio afectado por el fallo Heartbleed aún enfrenta exactamente los mismos riesgos que los que aún no lo han reemplazado sus certificados SSL», dijo Netcraft. eWeek dijo, por su parte, Heartbleed «es probable que se mantenga un riesgo durante meses, si no años, por venir».

 Explotación

La Agencia de Ingresos de Canadá reportó el robo de números de Seguro Social que pertenecen a 900 contribuyentes, y declaró que fueron accedidos a través de un exploit del fallo durante un período de seis horas el 8 de abril de 2014. Cuando el ataque se descubrió, la agencia cerró su sitio web y amplió el plazo de presentación de los contribuyentes 30 de abril al 5 de mayo. La agencia dijo que ofrecerá a todos los afectados con servicios de protección al crédito sin costo alguno. El 16 de abril, la Policía Montada anunció que habían acusado a un estudiante de ingeniería en relación con el robo con "uso no autorizado de una computadora" y  de "mal uso en relación a datos".

En otro incidente, el sitio de crianza de los hijos del Reino Unido Mumsnet tuvo varias cuentas de usuario secuestradas, y se hicieron pasar por su director general. El sitio publicó una explicación de los hechos.

A su vez, investigadores anti-*malware* explotaron Heartbleed para acceder a foros secretos utilizadas por ciberdelincuentes.

El 12 de abril de 2014, al menos dos investigadores independientes fueron capaces de robar claves privadas usando este ataque desde un servidor experimental intencionalmente creado a tal fin por CloudFlare.

Se informó por un profesor de la Universidad de Míchigan que una computadora en China se había utilizado para la piratería y otras actividades maliciosas intentó el 8 de abril de 2014 para explotar Heartbleed para atacar a un servidor de la universidad, que en realidad era un honeypot dejado intencionadamente vulnerable, diseñado para atraer a los ataques que podrían entonces ser estudiados.

 Posible conocimiento y explotación antes de la divulgación

Muchos sitios web importantes parcharon o desactivaron el fallo en cuestión de días de su anuncio, pero no está claro si los atacantes potenciales sabían de él antes que eso y en qué medida lo fue explotado.

Sobre la base de los exámenes de los registros de auditoría por investigadores, se ha reportado que algunos atacantes podrían haber explotado el defecto durante al menos cinco meses antes del descubrimiento y anuncio. Errata Security señaló que un programa no malicioso muy utilizado llamado "Masscan", liberada seis meses antes de la divulgación de Heartbleed, termina abruptamente la conexión en el medio de la negociación de inicio de la misma manera como Heartbleed, generando los mismos mensajes de registro del servidor, y agregó que "Dos cosas nuevas que producen los mismos mensajes de error que puede parecer que los dos están correlacionados, pero por supuesto, no lo están".

Según Bloomberg News, dos fuentes de información privilegiada sin nombre le informaron que la Agencia de Seguridad Nacional (NSA) de los Estados Unidos estaba al tanto de la falla desde poco después de su introducción, pero decidieron mantenerlo en secreto, en lugar de informarlo, con el fin de explotarla para sus propios fines. La NSA ha negado esta afirmación, al igual que Richard A. Clarke, que fue miembro de un grupo consultivo que examinó la política de vigilancia electrónica de los Estados Unidos; le dijo a Reuters el 11 de abril de 2014 que la NSA no había sabido de Heartbleed.

 Comportamiento

La RFC 6520 Heartbeat Extension prueba los enlaces de comunicación segura TLS/DTLS al permitir que un ordenador en un extremo de una conexión envíe un mensaje de "solicitud de latido de corazón" ("Heartbeat Request"), que consiste en una carga útil, típicamente una cadena de texto, junto con la longitud de dicha carga útil como un entero de 16-bits. El equipo receptor debe entonces enviar la misma carga exacta de vuelta al remitente.

Las versiones afectadas de OpenSSL asignan un búfer de memoria para el mensaje a devolver basado en el campo de longitud en el mensaje de solicitud, sin tener en cuenta el tamaño real de la carga útil de ese mensaje. Debido a esta falla de revisión de los límites apropiados, el mensaje devuelto consta de la carga útil, posiblemente seguido de cualquier otra cosa que sea que esté asignada en el *buffer* de memoria.

 Impacto

Al leer un bloque de memoria arbitrario del servidor web, los atacantes pueden recibir datos importantes, comprometiendo la seguridad del servidor y sus usuarios. Los datos que podrían ser robados incluyen la clave maestra del propio servidor, que puede permitir a los atacantes descifrar el tráfico actual o el almacenado, mediante un ataque pasivo *man-in-the-middle* (si el servidor y el cliente no usan *perfect forward secrecy*), o activo si *perfect forward secrecy* está en uso. El atacante no puede controlar qué datos le son devueltos, aunque por la naturaleza del *bug*, existe cierta probabilidad de que sean datos usados por la misma biblioteca OpenSSL.

Por lo anterior, el *bug* puede revelar partes descifradas de las peticiones y respuestas del usuario, incluyendo cualquier tipo de información subida por el usuario a través de la conexión "segura", *cookies* de sesión y contraseñas, etc., lo que permitiría al atacante suplantar la identidad de otro usuario del servicio. Al hacerse público, cerca del 17 % o medio millón de servidores de seguridad web de Internet certificados por autoridades confiables se creían vulnerables a ser atacados. La Electronic Frontier Foundation, Ars Technica, y Bruce Schneier catalogaron al **bug Heartbleed** como "catastrófico". El columnista de *Forbes*, Joseph Steinberg, describió al *bug* como potencialmente "la peor vulnerabilidad encontrada (al menos en términos de su impacto potencial) desde que Internet comenzó a tener tráfico comercial".

 Sitios web y servicios web

Un analista publicó en GitHub que de los mil sitios más visitados el 8 de abril del 2014, los siguientes presentaban vulnerabilidades: Yahoo!, Imgur, Stack Overflow, Slate, y DuckDuckGo. Los siguientes sitios tienen servicios afectados o hicieron anuncios recomendando a sus usuarios cambiar sus contraseñas en respuesta a este fallo:

 Akamai Technologies
 Amazon Web Services
 Ars Technica
 Bitbucket
 BrandVerity
 Freenode

 GitHub
 IFTTT
 Internet Archive
 Mojang
 Mumsnet
 PeerJ

Pinterest
 Prezi
 Reddit
 Something Awful
 SoundCloud
 SourceForge

 SparkFun
 Stripe
 Tumblr
 Wattpad
 Wikimedia  (incluido Wikipedia)
 Wunderlist

 Aplicaciones de software

 IPCop 2.1.4 fue liberado el 8 de abril de 2014, con una solución para "la biblioteca OpenSSL de la que todo el mundo está hablando".
 Según el blog LastPass Password Manager, una prueba estándar lo mostró como vulnerables hasta que fue parchado el 8 de abril, pero debido a su uso de encriptación adicional y perfect forward security, potenciales ataques no fueron capaces de explotar este error. Aun así, LastPass recomendó a sus usuarios cambiar las contraseñas que LastPass almacena para los sitios web vulnerables.
 LibreOffice 4.2.3 se lanzó el 10 de abril de 2014, con un arreglo para CVE 2014-0160.
 LogMeIn afirmó haber "actualizado muchos productos y partes de nuestros servicios que se basan en OpenSSL".
 Varias aplicaciones de servidor de HP, tales como: HP System Management Homepage (SMH) para Linux y Windows

Además, la base de datos Common Vulnerabilities and Exposures, asociada con el Departamento de Seguridad Nacional de EE.UU., informa que las siguientes empresas han tenido su software/productos afectados por Heartbleed:
 McAfee y en especial algunas versiones de software que proporciona una cobertura antivirus para Microsoft Exchange, cortafuegos de software, y McAfee Email and Web Gateway
 Productos de la Serie VMware Horizon, emuladores y suites de cloud computing.

Servicios de juego, incluyendo Steam, Minecraft, Wargaming, League of Legends, GOG, Origin, SOE, Humble Bundle, y Path of Exile se vieron afectados y fueron reparados.

 Sistemas operativos

 Android 4.1.1 (Jelly Bean), usado en varios teléfonos inteligentes

 Firmware para algunas estaciones base AirPort

Firmware para routers Cisco

Firmware para routers Juniper

Firmware de Windows 10 es el principal creador de "Heartbleed"
(El método más efectivo para desactivar el Heartbleed ha sido estudiado por la página Rigthxd MyF20.13)

 Firmware para la familia de productos My Cloud de Western Digital

 Servicios de detección de vulnerabilidad

Varios servicios se han puesto a disposición para probar si Heartbleed afecta a un sitio determinado. Sin embargo, muchos servicios se han afirmado ser ineficaces para detectar el error. [134] Las herramientas disponibles incluyen:

 Tripwire SecureScan
 AppCheck - revisión de binarios estáticos, de Codenomicon
 Arbor Network's Pravail Security Analytics
 Herramienta de revisión Norton Safeweb Heartbleed
 Herramienta de prueba de Heartbleed de una compañía de seguridad TI europea
 Escáner Heartbleed por el criptólogo italiano Filippo Valsorda
 Prueba de vulnerabilidad de Heartbleed de Cyberoam
 Critical Watch Free Online Heartbleed Tester
 Módulo escáner Heartbleed de Metasploit
 Escáner Heartbleed de servidores de Rehmann
 Detector Heartbleed de Lookout Mobile Security, una aplicación para dispositivos Android que determina la versión OpenSSL del dispositivo e indica si es el heartbeat vulnerable está habilitado
 Heartbleed checker por LastPass
 Escáner de red para vulnerabilidad Heartbleed de Pentest-Tools.com
 Escáner oficial de Red Hat escrita en Python
 Pruebas de servidor SSL de Qualys SSL Labs la cual no solo revisa por el error Heartbleed, sino que también encuentra otros errores de implementación de SSL/TLS.
 Extensiones de navegador, como Chromebleed y FoxBleed
 SSL Diagnos
 CrowdStrike Heartbleed Scanner - revisa routers, impresoras y otros dispositivos conectados dentro de una red incluyendo sitios web en intranets.
 Reporte de Sitios Netcraft - indica si la confidencialidad de un sitio podría estar en riesgo debido a la explotación previa de Heartbleed al revisar datos de la encuesta SSL de Netcraft para saber si el sitio ofrecía la extensión TLS Heartbeat antes del descubrimiento de Heartbleed. La extensión Netcraft para Chrome, Firefox y Opera también hace esta revisión, mientras revisa por certificados potencialmente comprometidos.

Vulnerabilidad de OpenSSL

Vulnerabilidad según los descubridores del fallo:
 OpenSSL 1.0.1g - No vulnerable (Corrección del fallo)
 OpenSSL 1.0.1 a 1.0.1f - Vulnerable
 OpenSSL 1.0.0 - No vulnerable
 OpenSSL 0.9.8 - No vulnerable

Reacción

En el día que se dio a conocer, el Tor Project aconsejó en su blog a todo el que busque "fuerte anonimato y privacidad en Internet" debería "alejarse de Internet por completo por los próximos días mientras se arreglan las cosas".

Heartbleed está registrado en el sistema Common Vulnerabilities and Exposures como CVE-2014-0160. La Agencia de Impuestos Canadiense (Canada Revenue Agency) cerró su sitio web de servicios electrónicos debido a preocupaciones por el agujero de seguridad *Heartbleed*.

Quienes mantienen la plataforma de la Fundación Wikimedia aconsejaron a sus usuarios cambiar sus contraseñas.

Medidas y acciones preventivas

Las medidas que se recomendaron tomar, por parte de administradores de sistemas, eran:
 Aplicar el parche a OpenSSL y pasar a una versión que no estuviera afectada
 Reemitir el certificado de seguridad del sitio para eliminar la posibilidad de que estuviera comprometido
 revocar el certificado anterior

A los usuarios de los sitios afectados, por su parte, se les recomendó:
 No entrar en los sitios que estaban afectados hasta que no se corrigiera el fallo de seguridad
 Una vez corregido, cambiar sus contraseñas para eliminar la posibilidad de que hubiera sido comprometida

 Causa raíz, posibles lecciones y reacciones

Atendiendo a este problema las mayores compañías de tecnología del mundo acordaron donar millones de dólares para la creación de un grupo que financiará mejoras en programas de código abierto tipo OpenSSL. Amazon.com, Cisco Systems, Facebook, Google, IBM, Intel y Microsoft están entre la docena de compañías que han acordado financiar el grupo, llamado Core Infrastructure Initiative. Cada una donará 300000 dólares a este programa. La Fundación Linux, sin fines de lucro, anunció la formación del grupo el . El proyecto respaldará el desarrollo de software de código abierto, que constituye una parte crítica de la infraestructura tecnológica mundial pero cuyos desarrolladores no tienen necesariamente una financiación adecuada para su trabajo, dijo Jim Zemlin, director ejecutivo de la Fundación Linux. La fundación OpenSSL es candidata a ser una de las primeras beneficiadas con este financiamiento.

 Véase también

 Shellshock
 Ataque POODLE
 Ticketbleed

 Referencias

 Enlaces externos

 Resumen y Q&A sobre el fallo por Codenomicon Ltd
