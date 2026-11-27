---
type: Artículo de enciclopedia
title: Protocolo AAA
description: En seguridad informática, las siglas AAA se corresponden al conjunto de funciones autenticación, autorización y responsabilidad, puesto que en inglés son authentication, authorization y accounting.
resource: https://es.wikipedia.org/wiki/Protocolo_AAA
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Protocolo_AAA"}
license: CC BY-SA 4.0
id: eswiki-Protocolo_AAA
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Protocolo AAA

En seguridad informática, las siglas **AAA** se corresponden al conjunto de funciones autenticación, autorización y responsabilidad, puesto que en inglés son *authentication*, *authorization* y *accounting*. De esa forma, un proceso, protocolo, sistema... **AAA** garantiza que aplica esas tres características. En ocasiones, se añade la auditoría, y resulta en **AAAA**.

Descripción de las funciones
Un proceso, protocolo, sistema... es **AAA** si garantiza la siguiente funcionalidad:
 Autenticación, que se refiere a la garantía de que una ejecución la efectúa aquella entidad o persona que asegura ejecutarla. Para aplicarla, es preciso acreditar su identidad mediante, por ejemplo, la entrega de unas credenciales, un testigo, un certificado digital, etc. También es posible usar protocolos de autenticación que permiten demostrar la posesión de esas credenciales necesidad de entregarlas, como es el caso de los protocolos de desafío-respuesta.
 Autorización, que se refiere a la legitimidad de esa entidad o persona para la ejecución. Para ello, el sistema debe reconocerle unos permisos o privilegios, y garantizarlos mediante técnicas como el control de accesos.
 Responsabilidad, que se refiere a la capacidad de registrar los detalles de cada ejecución para que la entidad o persona que la efectué pueda rendir cuentas. De esa forma, se puede determinar no sólo aquel que hace usos indebidos del sistema, sino la existencia de otros errores u omisiones que impidieron la autenticación y autorización correctas.

 Lista de protocolos AAA

 RADIUS
 DIAMETER
 TACACS
 TACACS+

Otros protocolos utilizados en combinación con los protocolos AAA:

 PPP
 EAP
 LDAP

 Requisitos

 RFC 2194 Review of Roaming Implementations
 RFC 2477 Criteria for Evaluating Roaming Protocols
 RFC 2881 Network Access Server Requirements Next Generation (NASREQNG) NAS Model
 RFC 2903 Generic AAA Architecture
 RFC 2904 AAA Authorization Framework
 RFC 2905 AAA Authorization Application Examples
 RFC 2906 AAA Authorization Requirements
 RFC 3169 Criteria for Evaluating Network Access Server Protocols
 RFC 3539 AAA Transport Profile
 RFC 1234 AAA Transport Profile
