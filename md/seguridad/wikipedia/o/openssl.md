---
type: Artículo de enciclopedia
title: OpenSSL
description: OpenSSL es un proyecto de software libre basado en SSLeay, desarrollado por Eric Young y Tim Hudson.
resource: https://es.wikipedia.org/wiki/OpenSSL
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/OpenSSL"}
license: CC BY-SA 4.0
id: eswiki-OpenSSL
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# OpenSSL

- **Nombre:** OpenSSL
- **Modelo desarrollo:** Software libre
- **Desarrollador:** Proyecto OpenSSL
- **Última versión:** 4.0.3
- **Género:** Biblioteca de seguridad
- **Lenguaje programación:** C
- **Sistema operativo:** Multiplataforma
- **Licencia:** estilo Apache

***OpenSSL*** es un proyecto de software libre basado en *SSLeay*, desarrollado por Eric Young y Tim Hudson.

Consiste en un robusto paquete de herramientas de administración y bibliotecas relacionadas con la criptografía, que suministran funciones criptográficas a otros paquetes como *OpenSSH* y navegadores web (para acceso seguro a sitios HTTPS).

Estas herramientas ayudan al sistema a implementar el *Secure Sockets Layer (SSL)*, así como otros protocolos relacionados con la seguridad, como el *Transport Layer Security (TLS)*. *OpenSSL* también permite crear certificados digitales que pueden aplicarse a un servidor, por ejemplo *Apache*.

A principios de abril de 2014 se da a conocer un agujero de seguridad (conocido como Heartbleed) que afecta a las versiones 1.0.1 y 1.0.1f de este protocolo afectando a dos tercios de las comunicaciones seguras que se efectúan en Internet. El agujero está en el código de OpenSSL desde diciembre de 2011. Neel Mehta, del equipo de seguridad de Google, lo habría descubierto en diciembre de 2013, fecha de la inclusión del "bug" en la base de datos 'Common Vulnerabilities and Exposures'.

 Algoritmos soportados
Los siguientes algoritmos de criptografía son soportados por la herramienta:
**Para cifrado**
AES, Blowfish, Camellia, SEED, CAST-128, DES, IDEA, RC2, RC4, RC5, Triple DES, GOST 28147-89
**Funciones HASH**
MD5, MD4, MD2, SHA-1, SHA-2, RIPEMD-160, MDC-2, GOST R 34.11-94
**Clave pública**
RSA, DSA, Intercambio de claves Diffie–Hellman, curvas elípticas

 Véase también
 Datagram Transport Layer Security
 Proyecto POSSE
 GnuTLS

 Referencias

 Enlaces externos
 Artículo sobre agujero de seguridad *Heartbleed*
 Sitio web que explica Heartbleed (en inglés)
