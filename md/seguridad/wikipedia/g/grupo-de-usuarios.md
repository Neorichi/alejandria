---
type: Artículo de enciclopedia
title: Grupo de usuarios
description: Un grupo de usuarios es una política utilizada generalmente por un sistema operativo para referirse a más de 1 usuario en su configuración y privilegios.
resource: https://es.wikipedia.org/wiki/Grupo_de_usuarios
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Grupo_de_usuarios"}
license: CC BY-SA 4.0
id: eswiki-Grupo_de_usuarios
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Grupo de usuarios

Un **grupo de usuarios** es una política utilizada generalmente por un sistema operativo para referirse a más de 1 usuario en su configuración y privilegios.

 Facilidad
Trabajar con un grupo de usuarios que por separado puede resultar algo más sencillo, debido a que en vez de trabajar con una variable, se hace con un vector pudiendo referirse a un conjunto o a uno en exclusiva, facilitando la configuración de los permisos de cada usuario.

 Privilegios
En un grupo de usuarios existen privilegios globales e individuales, primero se consideran los globales y luego se consideran los individuales, agregándole o disminuyéndole privilegios basándose en los globales.

Ej:
 Grupo (UsuarioA, UsuarioB)
 Grupo PUEDE ver
 UsuarioA PUEDE editar

En este caso el UsuarioA puede "ver" (gracias a los privilegios globales) y puede "editar" (gracias a los privilegios individuales) y el UsuarioB solo puede "ver".

 Clasificación de usuarios
Algunos ejemplos de clasificación de usuarios:
 Invitados: Son los usuarios con menos permisos en el sistema o red, solo podrán leer un número muy reducido de archivos o hasta ni siquiera acceder a ningún tipo de información
 Usuarios: Son los usuarios normales del sistema, con pocos permisos. Tienen permisos para conectarse al sistema interactivamente y a través de la red, pero no pueden modificar ningún tipo de información.
 Usuarios interactivos: Este grupo representa a todos aquellos usuarios que tienen el derecho de iniciar una sesión local en el sistema o red.
 Usuarios autentificados: Agrupa a todos los usuarios que poseen una cuenta propia para conectarse al sistema, solo pueden ver algunos archivos y carpetas del sistema y leer, modificar y eliminar los archivos pertenecientes a su cuenta.
 Administradores: Son los usuarios con más permisos sobre el sistema o red, pueden ver, modificar y eliminar cualquier tipo de información.

 Sudo
El sudo es una herramienta de los sistemas operativos Unix cuya función es ejecutar un comando con privilegios altos desde un usuario o grupo de usuarios con privilegios bajos.

Esto es muy útil, sobre todo en seguridad informática, ya que se es posible acceder trivialmente al usuario root de forma segura.

Un ejemplo de ejecución de un archivo protegido desde un usuario perteneciente a un grupo con privilegios bajos:

 $sudo exec /root/ejecutable
Tras esto, pide la contraseña del usuario root, una vez ingresada correctamente, ejecuta una línea como si se estuviere autentificados como root.

 Véase también

Usuario (informática)
Root
Usuario avanzado
Autentificación
Login

 Enlaces externos

Gestión de grupos de usuarios
