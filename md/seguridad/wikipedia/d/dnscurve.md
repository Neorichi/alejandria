---
type: Artículo de enciclopedia
title: DNSCurve
description: DNSCurve es un protocolo de seguridad propuesto para el Sistema de Nombres de Dominio (DNS), diseñado por Daniel J.
resource: https://es.wikipedia.org/wiki/DNSCurve
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/DNSCurve"}
license: CC BY-SA 4.0
id: eswiki-DNSCurve
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# DNSCurve

**DNSCurve** es un protocolo de seguridad propuesto para el Sistema de Nombres de Dominio (DNS), diseñado por Daniel J. Bernstein.

 Descripción
DNSCurve utiliza la función Curve25519, una función de criptografía de curva elíptica para establecer claves utilizadas por Salsa20, junto con la función MAC Poly1305, para cifrar y autenticar paquetes DNS entre los resolvers y servidores autorizados. Las claves públicas de los servidores autorizados remotos se ubican en los registros NS, por lo que los resolvers recursivos pueden saber si el servidor soporta DNSCurve. La forma de reconocerlo es que las llaves comienzan con la cadena mágica uz5 y son seguidos por 51 bytes codificados en base 32 de la clave pública de 255 bits del servidor, por ejemplo, en formato BIND:

 example.com. IN NS uz5bcx1nh80x1r17q653jf3guywz7cmyh5jv0qjz0unm56lq7rpj8l.example.com.

El resolver luego envía al servidor un paquete que contiene su clave pública DNSCurve, un nonce criptográfico de 96 bits, y una caja de cifrado que contiene la consulta. El cuadro de cifrado se crea usando las claves del resolutor privada, la clave pública del servidor, y el nonce. La respuesta del servidor contiene un nonce 96 bits diferente y su propia caja criptográfica que contiene la respuesta a la consulta.

Las herramientas criptográficas que se utilizan en DNSCurve son las mismas utilizadas en **CurveCP**, un protocolo basado en UDP que es similar a TCP, pero utiliza criptografía de curva elíptica para cifrar y autenticar los datos. Una analogía es que mientras DNSSEC es como firmar una página web con PGP, CurveCP y DNSCurve son como encriptar y autenticar el canal utilizando SSL. Al igual que las páginas web con firma PGP se pueden enviar a través de un canal cifrado con SSL, los datos DNSSEC se pueden proteger mediante DNSCurve.

 Seguridad
DNSCurve utiliza criptografía de curva elíptica de 255 bits, que NIST estima ser aproximadamente equivalente a de 3072 de 96-bits RSA ECRYPT reporta una equivalencia parecida. Se utiliza criptografía de clave pública por consulta (como SSH y SSL), y de nonces de 96-bits para proteger contra ataques de repetición. Adam Langley, oficial de seguridad en Google, dice que "con muy alta probabilidad, nadie va a resolver una sola instancia de curve25519 sin un gran computador cuántico".

 Velocidad
Adam Langley ha publicado pruebas de velocidad en su página personal mostrando que curve25519, utilizado por DNSCurve, sería el más rápido entre las curvas elípticas probadas. De acuerdo con la NSA, la criptografía de curva elíptica ofrece un rendimiento muy superior sobre RSA y Diffie-Helman a una tasa geométrica al aumento de tamaño de clave.

 Implementaciones
DNSCurve primero ganó el apoyo recursivo en dnscache mediante un parche de Matthew Dempsky. Dempsky también tiene un repositorio GitHub que incluye herramientas de búsqueda DNS en Python y un forwarder en C. Adam Langley también tiene un repositorio en GitHub. Existe un forwarder autoritativo llamado CurveDNS, que permite a los administradores de DNS proteger instalaciones sin parchar existentes. OpenDNS ha liberado DNSCrypt para proteger el canal entre los usuarios de OpenDNS y sus resolvedores recursivos. Jan Mojžíš ha lanzado curveprotect, una suite de software que implementa la protección DNSCurve y CurveCP para los servicios comunes, como DNS, SSH, HTTP y SMTP.

 Despliegue
OpenDNS, que tiene 50 millones de usuarios, anunció el apoyo a DNSCurve en sus resolvers recursivos el 23 de febrero de 2010. Luego el 6 de diciembre de 2011, OpenDNS anunció una nueva herramienta, llamada DNSCrypt. DNSCrypt protege el canal entre OpenDNS y sus usuarios. No hay otros proveedores grandes DNS con autoridad que hayan desplegado DNSCurve todavía, aunque algunos de menor tamaño, como privacyshark.com sí lo han hecho. A enero de 2010 da servicio a 601 dominios.

 Véase también
 DNSSEC
 Criptografía de curva elíptica
 OpenDNS

 Referencias

 Enlaces externos
 Sitio Oficial
 DNSCurve: Usable security for DNS, an August 2008 presentation by the author
 draft-dempsky-dnscurve-01 estándar propuesto "DNSCurve: Link-Level Security for the Domain Name System", por M. Dempsky (de OpenDNS) a IETF (actualizado en febrero de 2010)
 CurveDNS, DNSCurve forwarding name server
 NaCl, Networking and Cryptography library
