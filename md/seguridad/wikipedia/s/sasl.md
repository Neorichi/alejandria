---
type: Artículo de enciclopedia
title: SASL
description: "SASL: Siglas en inglés para Simple Authentication and Security Layer (capa de seguridad y autenticación simple)."
resource: https://es.wikipedia.org/wiki/SASL
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/SASL"}
license: CC BY-SA 4.0
id: eswiki-SASL
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# SASL

**SASL**: Siglas en inglés para *Simple Authentication and Security Layer* (capa de seguridad y autenticación simple).

SASL es un framework para autenticación y autorización en protocolos de Internet. Separa los mecanismos de autenticación de los protocolos de la aplicación permitiendo, en teoría, a cualquier protocolo de aplicación que use SASL usar cualquier mecanismo de autenticación soportado por SASL. A pesar de que mediante SASL sólo se maneja la autenticación (y se requieren otros mecanismos --como por ejemplo TLS-- para cifrar el contenido que se transfiere), SASL proporciona medios para un uso negociado del mecanismo elegido. Las especificaciones originales de SASL fueron editadas por John Meyers en el RFC 2222. Este fue hecho obsoleto por el RFC 4422, editado por Alexey Melnikov y Kurt Zeilenga.

Un mecanismo SASL se modela como una sucesión de retos y respuestas. Los mecanismos definidos por SASL incluyen:

 "EXTERNAL", aquí la autenticación está implícita en el contexto (p.ej. para protocolos que ya usan IPsec o TLS).
 "ANONYMOUS", para el acceso de invitados sin autentificar.
 "PLAIN", un mecanismo de contraseña simple en texto plano.
 "OTP" para el sistema que evolucionó de S/KEY
 "NTLM".
 Se prevé soportar los mecanismos GSSAPI en una familia de nomenclatura de mecanismos.

Los protocolos definen su representación de intercambios SASL con un *perfil*. Un protocolo tiene un *nombre de servicio* como "LDAP" en un registro compartido con GSSAPI y Kerberos.

Entre los protocolos que ahora mismo usan SASL se incluyen IMAP, LDAP, POP3, SMTP, XMPP y algunos servidores IRC, como Libera Chat.

 Referencias

 Enlaces externos
 El RFC 2222 define el entorno de trabajo SASL.
 El RFC 4422 hizo obsoleto al RFC 2222
 El SASL Working Group se encarga de actualizar las especificaciones SASL.
