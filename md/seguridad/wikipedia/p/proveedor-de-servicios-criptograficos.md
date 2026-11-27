---
type: Artículo de enciclopedia
title: Proveedor de servicios criptográficos
description: En Microsoft Windows, un proveedor de servicios criptográficos (en inglés, Cryptographic Service Provider, CSP) es una biblioteca de software que implementa Microsoft CryptoAPI (CAPI).
resource: https://es.wikipedia.org/wiki/Proveedor_de_servicios_criptográficos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Proveedor_de_servicios_criptográficos"}
license: CC BY-SA 4.0
id: eswiki-Proveedor_de_servicios_criptográficos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Proveedor de servicios criptográficos

En Microsoft Windows, un **proveedor de servicios criptográficos** (en inglés, **Cryptographic Service Provider**, **CSP**) es una biblioteca de *software* que implementa Microsoft CryptoAPI (CAPI). Los CSP implementan funciones de codificación y descodificación, que los programas de aplicación informática pueden utilizar, por ejemplo, para implementar una autenticación de usuario segura o para un correo electrónico seguro.

Los CSP son módulos independientes que pueden ser utilizados por diferentes aplicaciones. Un programa de usuario llama a funciones CryptoAPI y estas son redirigidas a funciones CSPs. Puesto que los CSP son responsables de implementar los algoritmos y estándares criptográficos, las aplicaciones no necesitan preocuparse por los detalles de seguridad. Además, una aplicación puede definir qué CSP va a utilizar en sus llamadas a CryptoAPI. De hecho, toda la actividad criptográfica se implementa en los CSP. CryptoAPI sólo funciona como un puente entre la aplicación y el CSP.

 Referencias
