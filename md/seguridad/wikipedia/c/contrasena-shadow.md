---
type: Artículo de enciclopedia
title: Contraseña shadow
description: Shadow es un programa de ordenador que permite mejorar el sistema de contraseñas ofreciendo algunas ventajas sobre el estándar previo de almacenaje de contraseñas en Unix y Linux.
resource: https://es.wikipedia.org/wiki/Contraseña_shadow
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Contraseña_shadow"}
license: CC BY-SA 4.0
id: eswiki-Contraseña_shadow
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Contraseña shadow

**Shadow** es un programa de ordenador que permite mejorar el sistema de contraseñas ofreciendo algunas ventajas sobre el estándar previo de almacenaje de contraseñas en Unix y Linux. En las versiones más recientes de Linux no es necesario instalarlo puesto que ya viene incluido.

Shadow borra las claves secretas codificadas del fichero /etc/passwd, que necesariamente es legible para todos, y las sitúa en el fichero /etc/shadow el cual solo puede leer el root.

Para habilitar contraseñas ocultas para grupo tenemos los comandos *pwconv* y *grpconv* respectivamente.

 Ventajas de usar contraseñas Shadow

Entre las ventajas de las contraseñas "Shadow" destacan el cifrado más robusto, la obtención de información acerca de la vigencia de las contraseñas, el poder controlar cuanto tiempo puede permanecer sin cambios una contraseña antes de que el usuario sea obligado a cambiarla y la capacidad de usar el fichero /etc/login.defs para reforzar la política de seguridad, especialmente lo concerniente a la vigencia de contraseñas.

Antes de instalar Shadow hay que tener en cuenta que los programas que necesitan verificar contraseñas como administradores de sesión, ftp, demonios POP3, etc… necesitan ser compatibles con Shadow para su funcionamiento correcto, es decir, deberán ser capaces de trabajar con contraseñas ocultas.
