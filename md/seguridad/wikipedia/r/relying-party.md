---
type: Artículo de enciclopedia
title: Relying party
description: Un relying party (RP) es término informático que se refiere a un servidor o servicio que proporciona acceso seguro a información o una aplicación.
resource: https://es.wikipedia.org/wiki/Relying_party
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Relying_party"}
license: CC BY-SA 4.0
id: eswiki-Relying_party
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Relying party

Un **relying party** (RP) es término informático que se refiere a un servidor o servicio que proporciona acceso seguro a información o una aplicación.

Aplicaciones basada en Claims, donde una claim o nivel de acceso es una declaración que realiza una entidad para obtener acceso, son también llamadas aplicaciones relying party (RP). También pueden ser llamadas "claims aware applicaciones". Aplicaciones web como servicios pueden ser RPs.

En un modelo de Seguridad basada en Tokens (STS), el RP es redirigido a un **STS**, el cual lo autentifica y emite un token de seguridad para otorgar el acceso, en vez de que la aplicación se autentique con el RP directamente. Los niveles de acceso se extraen de los tokens y son utilizados para las comprobaciones de identidad.

El estándar OpenID define una situación por el cual un servicio puede actuar como un RP, dejando el usuario acceda a múltiples servicios utilizando el mismo conjunto de credenciales. Los beneficios para el usuario es el no tener que compartir sus credenciales con los múltiples servicios, y para los operadores de los servicios, evitar tener que desarrollar su propio mecanismo de identidad.

Una aplicación que demuestra el concepto RP es una aplicación corriendo en dispositivos móviles, la cual puede ser utilizada no solo para conceder acceso a aplicaciones de software, pero también el acceso a un edificio u oficina, sin que el usuario tenga que introducir sus credenciales cada vez.

 Referencias
