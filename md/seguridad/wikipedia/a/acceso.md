---
type: Artículo de enciclopedia
title: Acceso
description: "En informática, un acceso es el resultado positivo de una autentificación, para que el acceso dure un tiempo predeterminado,o ya no requiere usar el servidor guarda en el cliente una cookie, esta permitirá que el …"
resource: https://es.wikipedia.org/wiki/Acceso
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Acceso"}
license: CC BY-SA 4.0
id: eswiki-Acceso
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Acceso

En informática, un **acceso** es el resultado positivo de una autentificación, para que el acceso dure un tiempo predeterminado,o ya no requiere usar el servidor guarda en el cliente una cookie, esta permitirá que el usuario pueda entrar a su cuenta en el servidor hasta que esta caduque.

 Acceso autorizado

Un acceso autorizado es el resultado de una autentificación correcta, un ejemplo es el ingreso de usuario claudia NombreDeUsuario
 Contraseña:blanca

El servidor comparara los datos ingresados con los de la base de datos generalmente con el lenguaje SQL, si los datos coinciden, el servidor guardara una cookie de sesión en el cliente y permitirá que este pueda ver y editar información dependiendo de los privilegios que este usuario tenga.

Un ejemplo de la comparación de datos ingresados con los de la base de datos en un pseudocódigo:

 SI NombreDeUsuario.Existe EN BaseDeDatos HACER
  SI Contraseña = BaseDeDatos.NombreDeUsuario.Contraseña HACER
   "Acceso"
  SINO
   "Contraseña incorrecta"
 SINO
  "Usuario incorrecto"

Primero chequea si existe o no el usuario, si existe el usuario compara la contraseña, si la contraseña coincide con la de la base de datos, el usuario logra acceder, si la contraseña no coincide con la de la base de datos, se le informa al usuario que la contraseña es incorrecta, si el usuario directamente no se encuentra en la base de datos, se informa que el usuario es incorrecto.

 Acceso no autorizado

Un acceso no autorizado es producto de la explotación de una vulnerabilidad en el sistema del servidor o en alguna de sus aplicaciones o la utilización de algún otro método para subir privilegios como fuerza bruta, malware, sniffers o ingeniería social, entre otros.

Ejemplo de un acceso no autorizado por http explotando una vulnerabilidad en los scripts del cgi-bin:

 atacante>abrirurl>
 atacante>subirarchivo>...

En este caso el atacante explotó una vulnerabilidad para lograr obtener un acceso no autorizado y poder subir su archivo.

 Monitoreo de Servidores y redes informáticas
Un administrador las 24 horas en un servidor o red puede controlar todos los accesos en todas las zonas y tiene los permisos suficientes para desconectar y bloquear a cualquier intruso.

 Ban

Un ban es una política muy útil para impedir accesos no autorizados, este bloquea el acceso de un usuario parcialmente o totalmente por un periodo de tiempo definido o indefinido este puede aplicarse manualmente (por un administrador) o automáticamente (por un bot o el mismo sistema operativo).

 Bans manuales

Son aquellos dados por administrador cuándo este ve un comportamiento extraño en el usuario autentificado.

 Bans automático

Son aquellos dados por un bot o el sistema operativo cuándo detectan (basándose en inteligencia artificial) un comportamiento extraño en el usuario autentificado o hay una cantidad determinada de intentos fallidos en una autentificación.

 Véase también
 Administrador
 Ban
Usuario
 Grupo de usuarios
 Seguridad Informática

 Referencias

 Enlaces externos
