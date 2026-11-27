---
type: Artículo de enciclopedia
title: FTPS
description: FTPS (comúnmente referido como FTP/SSL) es un nombre usado para abarcar un número de formas en las cuales el protocolo FTP puede realizar transferencias de ficheros seguras.
resource: https://es.wikipedia.org/wiki/FTPS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/FTPS"}
license: CC BY-SA 4.0
id: eswiki-FTPS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# FTPS

**FTPS** (comúnmente referido como **FTP/SSL**) es un nombre usado para abarcar un número de formas en las cuales el protocolo FTP puede realizar transferencias de ficheros seguras. Cada forma conlleva el uso de una capa SSL/TLS debajo del protocolo estándar FTP para cifrar los canales de control y/o datos. No debe confundirse con el protocolo seguro de transferencia de ficheros SFTP, el cual suele ser usado con SSH.

Para solucionar el problema de la confidencialidad (cifrado de los datos) en la autenticación y en la transferencia de datos, se decidió añadir una capa de seguridad SSL/TLS al propio protocolo FTP. FTPS y FTPES también se conocen como FTP over TLS/SSL, y están basados en el propio protocolo FTP.

El uso más común de FTP y SSL es:

 *AUTH TLS* o FTPS Explícito, nombrado por el comando emitido para indicar que la seguridad TLS es obligatoria. Este es el método preferido de acuerdo al RFC que define FTP sobre TLS. El cliente se conecta al puerto 21 del servidor y comienza una sesión FTP sin cifrar de manera tradicional, pero pide que la seguridad TLS sea usada y realiza la negociación apropiada antes de enviar cualquier dato sensible.

 *AUTH* como está definido en el RFC 2228.

 *FTPS Implícito* es un estilo antiguo, pero todavía ampliamente implementado en el cual el cliente se conecta a un puerto distinto (como por ejemplo el 990), y se realiza una negociación SSL antes de que se envíe cualquier comando FTP.

 Funcionamiento
Cuando se establece una conexión segura a SSL ocurre lo siguiente:

 Se autentica el servidor ante el cliente.
 Se permite al cliente y al servidor seleccionar los algoritmos criptográficos o códigos de cifrado que son compatibles con ambos.
 Opcionalmente, se autentica al cliente ante el servidor.
 Se utilizan técnicas de cifrado de clave pública para generar secretos compartidos.

 Canales de Datos
La comunicación pueden ser o no ser cifrada en el canal de comandos, en el canal de datos, o más a menudo en ambos. Si el canal de comandos no se cifra, se dice que el protocolo está usando un canal de comandos en claro (CCC). Si el canal de datos no está cifrado, se dice que el protocolo usa un canal de datos en claro (CDC).

 Véase también

 File eXchange Protocol
 File Transfer Protocol
 SSH File Transfer Protocol
 TFTP

 Enlaces externos
 RFC 4217 - Asegurando FTP con TLS (en inglés).
