---
type: Artículo de enciclopedia
title: Transferencia de zona DNS
description: Una transferencia de zona DNS, a veces llamada AXFR por el tipo de solicitud, es un tipo de transacción de DNS.
resource: https://es.wikipedia.org/wiki/Transferencia_de_zona_DNS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Transferencia_de_zona_DNS"}
license: CC BY-SA 4.0
id: eswiki-Transferencia_de_zona_DNS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Transferencia de zona DNS

Una **transferencia de zona DNS**, a veces llamada **AXFR** por el tipo de solicitud, es un tipo de transacción de DNS. Es uno de varios mecanismos disponibles para administradores para replicar bases de datos DNS a través de un conjunto de servidores DNS. La transferencia puede hacerse de dos formas: completa (AXFR) o incremental (IXFR)

Se producirá una transferencia de zona durante cualquiera de los siguientes escenarios:
 Al iniciar el servicio DNS en el servidor DNS secundario.
 Cuando caduca el tiempo de actualización.
 Cuando se guardan los cambios en el archivo de zona principal y hay una notificación lista.

Si llegara a existir algún problema de configuración o actualización del software de cualquiera de estos servidores se podrían explotar una serie de vulnerabilidades como por ejemplo envenenamiento de la base de datos y la integridad y confidencialidad de la base de datos del DNS primario se verían comprometidas.

 Operación
Una transferencia de zona utiliza el protocolo TCP para el transporte, y toma la forma de una transacción de cliente-servidor. El cliente que solicita una transferencia de zona puede ser un servidor esclavo o servidor secundario, que solicita datos de un servidor maestro, a veces llamado un servidor primario. La parte de la base de datos que se replica es una zona.

La transferencia de zona comprende un preámbulo seguido de la transferencia de datos misma. El preámbulo comprende una búsqueda de la SOA (Start of Authority) registro de recursos para la "zona ápice", el nodo del espacio de nombres DNS que se encuentra en la parte superior de la "zona". Los campos de este registro de recursos SOA, en particular, el "número de serie", determinan si la transferencia de datos necesita ocurrir o no. El cliente compara el número de serie del registro de recursos SOA con el número de serie en la última copia de ese registro de recursos que tiene. Si el número de serie del registro que está siendo transferido es mayor, los datos en la zona se considera que han "cambiado" (de alguna manera) y el esclavo procede a solicitar la transferencia real de datos de zona. Si los números de serie son idénticos, los datos en la zona se considerará que no ha "cambiado", y el cliente puede seguir utilizando la copia de la base de datos que ya tiene, si tiene una.

El proceso de transferencia de datos real comienza por el cliente de enviar una consulta (opcode 0) con el QTYPE especial (tipo de consulta) AXFR (valor 252) a través de la conexión TCP con el servidor. El servidor responde con una serie de mensajes de respuesta, que comprende todos los registros de recursos para cada nombre de dominio en la "zona". La primera respuesta comprende el registro de recursos SOA de la zona ápice. Los otros datos siguen sin un orden determinado. El final de los datos es señalado por el servidor de repitiendo la respuesta que contiene el registro de recursos SOA para la zona de ápice.

Algunos clientes de transferencia de zona realizan la búsqueda de SOA del preámbulo utilizando el mecanismo normal de resolución de consultas DNS de su sistema. Estos clientes no abren una conexión TCP con el servidor hasta que hayan determinado que ellos necesitan llevar a cabo la transferencia de datos. Sin embargo, ya que TCP puede ser utilizado para las transacciones de DNS normales, así como para la transferencia de zona, otros clientes de transferencia de zona realizan la búsqueda preámbulo SOA sobre la misma conexión TCP, ya que a continuación (pueden) realizar la transferencia de datos real. Estos clientes abren la conexión TCP con el servidor antes de que incluso realizan el preámbulo.

Lo anterior describe la transferencia de zona completa. Transferencia de zona incremental difiere de transferencia de zona completa en los siguientes aspectos:

 Los cliente utiliza el QTYPE IXFR especial (valor 251) en lugar del AXFR QTYPE.
 Los cliente envía el registro de recursos SOA de la zona ápice que en la actualidad cuenta, en su caso, en el mensaje IXFR, dejando que el servidor saber qué versión de la "zona" que cree que es actual.
 Aunque el servidor puede responder de la manera normal AXFR con los datos completos de la zona, también puede responder con un lugar de transferencia de datos "incrementales". Este último comprende la lista de cambios en los datos de zona, en la zona para el número de serie, entre la versión de la zona que el cliente informa al servidor como que tiene y la versión de la zona que es actual en el servidor. Los cambios comprenden dos listas, una de los registros de recursos que se elimina y uno de los registros de recursos que se insertan. (Una modificación de un registro de recurso se representa como una eliminación seguido por una inserción.)

La transferencia de zona es totalmente iniciada por el cliente. Aunque los servidores pueden enviar un mensaje NOTIFICACIÓN (NOTIFY) a los clientes (que se les ha informado acerca de) cada vez que se ha realizado un cambio en los datos de zona, la programación de las transferencias de zona está totalmente bajo el control de los clientes. Los clientes programan las transferencias de zona en un principio, cuando sus bases de datos están vacíos, y posteriormente a intervalos regulares, en un patrón controlado por los valores en los campos "refrescar", "reintentar", y "caducar" en el registro de recursos SOA de la zona ápice.

 Limitaciones
A pesar de que está estandarizado, la transferencia de zona completa que se describe como uno de los posibles mecanismos de replicación de bases de datos en el RFC 1034 y RFC 5936 (transferencia de zona incremental se describe en el RFC 1995), la transferencia de zona es el más limitado de los mecanismos de replicación de bases de datos. La transferencia de zonas opera en términos de "Formato de cable" de los registros de recursos, ya que se transfieren mediante el protocolo DNS. Sin embargo, el esquema de los registros de recursos transferidos puede no coincidir con el esquema de base de datos utilizado por los extremos posteriores de los propios servidores DNS.

 Problemas operacionales
 Cambios de números de serie
El preámbulo de la transferencia de la zona se basa en el número de serie, y sólo el número de serie, para determinar si los datos de una zona han cambiado, y por tanto, si se requiere la transferencia de datos solicitada. Para algunas implementaciones de servidores DNS, los números de serie de los registros de recursos SOA son mantenidos por los administradores a mano. Cada edición de la base de datos consiste en realizar dos cambios, uno para el registro que se está cambiando y el otro para el número de serie de la zona. Este es un proceso laborioso y que es propenso a error, ya sea con los administradores olvidándose de cambiar un número de serie o cambiando un número de serie incorrectamente (como la disminución o el aumento por una gran cantidad).

Algunas implementaciones de servidores DNS han superado este problema construyendo automáticamente el número de serie a partir de la última fecha y hora de modificación del archivo de base de datos en el disco. Este es el caso de djbdns, por ejemplo. El sistema operativo se asegura de que la última hora de modificación se actualiza cada vez que un administrador edita el archivo de base de datos, de manera efectiva la actualización de forma automática el número de serie, y por lo tanto aliviando los administradores de la necesidad de hacer dos ediciones (en dos lugares diferentes) para cada cambio.

Por otra parte, el paradigma de la replicación de bases de datos para que la comprobación de número de serie (y de hecho la propia de transferencia de zona) se diseñó, lo que implica un único servidor central DNS manteniendo la versión maestra de la base de datos con todos los demás servidores DNS simplemente conteniendo copias, simplemente no coincide la de muchos paquetes de servidores DNS modernos. Los paquetes modernos de servidor DNS con servicios de back-end de base de datos sofisticadas, como servidores SQL y Active Directory permiten a los administradores realizar cambios a la base de datos en múltiples lugares (tales sistemas emplean replicación multi-maestro), con el propio mecanismo de replicación del back-end de la base de datos manejando la replicación a todos otros servidores. Este paradigma simplemente no coincide con el de un solo, centralizado y monótonamente creciente número para registrar los cambios, y por lo tanto es incompatible con transferencia de zona en gran medida. Los paquetes de modernos de este tipo a menudo crean un número de serie "cuña", que simula la existencia de un único lugar central donde se hacen cambios, pero esto es en el mejor de los casos, imperfecto.

Afortunadamente, por esta y muchas razones esbozadas más adelante, los servidores DNS que utilizan tales bases de datos sofisticadas rara vez utilizan la transferencia de zona como su mecanismo de replicación de bases de datos en el primer lugar, y por lo general emplean en su lugar mecanismos de replicación de bases de datos muy superiores distribuidos que los extremos traseros proporcionan por sí mismos.

 Comparaciones de número de serie
Las comparaciones de número de serie están destinadas a utilizar la aritmética de número de serie como se define en el RFC 1982. Sin embargo, esto no fue claramente especificados en el RFC 1034, lo que resulta en que no todos los clientes realizan la verificación del número de serie, en el preámbulo, de la misma manera. Algunos clientes simplemente comprueban que el número de serie proporcionado por el servidor es diferente al conocido por el cliente, o distinto de cero. Otros clientes comprueban que el número de serie proporcionado por el servidor esté dentro de un rango dado del número de serie ya conocido por el cliente. Sin embargo, otros clientes todavía realizan esta última comprobación y, además, comprobar que el número de serie suministrado por el servidor no es cero. Existen varios casos donde aún siguiendo bien esta regla, solamente validar los números de serie hace que el cliente no detecte que necesita una actualización.

 Registros de recursos múltiples
Originalmente, en la transferencia de datos misma se transfirió cada conjunto de registros de recursos para un único nombre de dominio y el tipo en un mensaje de respuesta independiente del servidor al cliente. Sin embargo, esto es ineficiente, y algunas optimizaciones implementadas de software de servidor de DNS, orientadas a permitir que el mecanismo de compresión respuesta en el protocolo DNS para reducir los requisitos de ancho de banda total de las transferencias de datos, tales como:

 Ejecutando "un procesamiento de sección adicional" para "pegar" conjuntos de registros de recursos en la misma respuesta como, SRV, MX o NS.
 recogida de todos los conjuntos de registros de recursos relacionados con un único nombre de dominio y enviarles a, si corresponde, en una sola respuesta.

Algunos clientes fueron escritos para esperar sólo el formato de respuesta original, y fallarían en llevar a cabo la transferencia de datos si se emplean tales optimizaciones. Así, varios paquetes de servidores DNS tienen una opción de configuración que permite a los administradores especificar el uso de respuestas "de formato de respuesta única" para aquellos clientes que así lo requieran.

 La exposición de datos
Los datos contenidos en una zona DNS pueden ser sensibles desde un aspecto de la seguridad operacional. Esto es porque la información tal como nombres de host de servidor puede llegar a ser de conocimiento público, lo que se puede utilizar para descubrir información acerca de una organización e incluso proporcionar una superficie de ataque más grande.

En 2008 un tribunal de Dakota del Norte, EE. UU., dictaminó que la realización de una transferencia de zona por un extraño no autorizado para obtener información que no era accesible al público constituye una violación de la ley de Dakota del Norte.

Hay numerosas formas de comprobar si un servidor DNS es vulnerable. Puede, por ejemplo, utilizarse el script de la herramienta Nmap:

 Referencias

 Enlaces externos
 draft-ietf-dnsext-axfr-clarify DNS Zone Transfer Protocol (AXFR) internet draft

 Requests For Comments (RFCs) relacionados
 RFC 5936 Protocolo de Transferencia de zonas DNS (*DNS Zone Transfer Protocol*), el cual define AXFR, actualiza RFC 1034 *Domain Names - Concepts and Facilities*, y el RFC 1035 *Domain Names - Implementation and Specification*
 RFC 1995 Transferencia de Zona Incremental en DNS (''Incremental Zone Transfer in DNS' ')
 RFC 1996 Un mecanismo para pronta notificación de cambios de zona (*A Mechanism for Prompt Notification of Zone Changes*) (DNS NOTIFY)

 Estándares de Seguridad de la Información
 CAPEC-291 DNS Zone Transfers (en inglés)
 CVE-1999-0532 A DNS server allows zone transfers. (en inglés)
 CWE-16 Configuration (en inglés)
 CWE-276 Incorrect Default permissions (en inglés)
