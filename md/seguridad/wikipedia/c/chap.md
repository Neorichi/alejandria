---
type: Artículo de enciclopedia
title: CHAP
description: "CHAP (del inglés Challenge Handshake Authentication Protocol, «protocolo de autenticación por desafío y saludo») es un protocolo de autenticación por desafío-respuesta, definido en la RFC 1994."
resource: https://es.wikipedia.org/wiki/CHAP
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/CHAP"}
license: CC BY-SA 4.0
id: eswiki-CHAP
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# CHAP

**CHAP** (del inglés *Challenge Handshake Authentication Protocol*, «protocolo de autenticación por desafío y saludo») es un protocolo de autenticación por desafío-respuesta, definido en la RFC 1994.

Es un método de autenticación remota o inalámbrica. Diversos proveedores de servicios emplean CHAP; por ejemplo, para autenticar a un usuario frente a un proveedor de servicios de Internet.

 Uso
CHAP es un método de autenticación usado por servidores accesibles vía PPP. CHAP verifica periódicamente la identidad del cliente remoto usando un intercambio de información de tres etapas. Esto ocurre cuando se establece el enlace inicial y puede repetirse en cualquier momento de la comunicación. La verificación se basa en un secreto compartido (como una contraseña).

 Después del establecimiento del enlace, el agente autenticador manda un mensaje de desafío al usuario.
 El usuario responde con un valor calculado usando una función hash de un solo sentido, como MD5.
 El autenticador verifica la respuesta con el resultado de su propio cálculo de la función hash. Si el valor coincide, el autenticador informa de la verificación; de lo contrario, termina la conexión.
 A intervalos aleatorios el autenticador manda un nuevo desafío, con lo que se repite el proceso.

CHAP protege contra los ataques de reinyección (*replay*) mediante el uso de un identificador que se va incrementando y un valor de desafío variable. CHAP requiere que el cliente mantenga el secreto disponible en texto plano.

La autenticación de CHAP es unidireccional: el autenticador verifica la identidad del par, pero no a la inversa. Para lograr autenticación mutua, el protocolo debe ejecutarse en ambas direcciones del enlace.

Microsoft implementó una variante de CHAP en su protocolo MS-CHAP.

 Véase también
 Password Authentication Protocol
 MS-CHAP

 Referencias
