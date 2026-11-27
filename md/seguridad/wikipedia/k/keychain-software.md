---
type: Artículo de enciclopedia
title: Keychain (software)
description: Keychain es el sistema de gestión de contraseñas en macOS, desarrollado por Apple.
resource: https://es.wikipedia.org/wiki/Keychain_(software)
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Keychain_(software)"}
license: CC BY-SA 4.0
id: eswiki-Keychain_(software)
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Keychain (software)

**Keychain** es el sistema de gestión de contraseñas en macOS, desarrollado por Apple. Se introdujo con Mac OS 8.6, y ha sido incluido en todas las versiones posteriores de Mac OS, ahora conocidas como macOS. Un llavero puede contener varios tipos de datos: contraseñas (para sitios web, servidores FTP,cuentas SSH , redes compartidas, redes inalámbricas, aplicaciones de groupware, imágenes de disco cifradas), claves privadas, certificados, y notas seguras.

 Almacenamiento y acceso
En macOS, los archivos de llavero se almacenan en ~ / Library / Keychains / (y subdirectorios), / Library / Keychains /, y / Network / Library / Keychains /, y la aplicación GUI de Keychain Access se encuentra en la carpeta Utilidades en la carpeta Aplicaciones. Es un software gratuito de código abierto lanzado bajo los términos de la APSL. El equivalente de la línea de comandos de Keychain Access es / usr / bin / security.

Los archivos de llavero almacenan una variedad de campos de datos que incluyen un título, URL, notas y contraseña. Solo las contraseñas y las notas seguras están encriptadas, con Triple DES.

 Bloqueo y Desbloqueo
El archivo de llavero predeterminado es el llavero de inicio de sesión, que generalmente se desbloquea al iniciar sesión con la contraseña de inicio de sesión del usuario, aunque la contraseña para este llavero puede ser diferente de la contraseña de inicio de sesión del usuario, agregando seguridad a costa de cierta conveniencia.  La aplicación Keychain Access no permite establecer una contraseña vacía en un llavero.

El llavero puede configurarse para que se "bloquee" automáticamente si la computadora ha estado inactiva por un tiempo, y se puede bloquear manualmente desde la aplicación Keychain Access. Cuando está bloqueada, la contraseña debe volver a ingresarse la próxima vez que se acceda al llavero para desbloquearla. Sobrescribir el archivo en ~ / Biblioteca / Llaveros / con uno nuevo (por ejemplo, como parte de una operación de restauración) también hace que el llavero se bloquee y se requiere una contraseña en el siguiente acceso.

 Sincronización de contraseña
Si el llavero de inicio de sesión está protegido por la contraseña de inicio de sesión, la contraseña del llavero se cambiará cada vez que se cambie la contraseña de inicio de sesión dentro de una sesión iniciada en macOS. En una red compartida de Mac / no Mac, es posible que la contraseña del llavero de inicio de sesión pierda la sincronización si la contraseña de inicio de sesión del usuario se cambia desde un sistema que no sea Mac. Además, si la contraseña se cambia desde un servicio de directorio como Active Directory o Open Directory, o si la contraseña se cambia desde otra cuenta de administrador, por ejemplo. utilizando las Preferencias del Sistema. Algunos administradores de red reaccionan a esto al eliminar el archivo de llavero al cerrar la sesión, de modo que se creará uno nuevo la próxima vez que el usuario inicie sesión. Esto significa que las contraseñas de los llaveros no se recordarán de una sesión a la siguiente, incluso si la contraseña de inicio de sesión tiene no ha sido cambiado. Si esto sucede, el usuario puede restaurar el archivo de llavero en ~ / Library / Keychains / desde una copia de seguridad, pero al hacerlo se bloqueará el llavero que luego deberá ser desbloqueado en el próximo uso.

 Keychain Access
Keychain access es una aplicación macOS  que le permite al usuario acceder a Keychain y configurar su contenido, incluidas contraseñas para sitios web, formularios web, servidores FTP, cuentas SSH , redes compartidas, redes inalámbricas, aplicaciones de groupware, imágenes de disco cifradas, etc.Bloquea y muestra las contraseñas guardadas que se vinculan con dinámicamente con la contraseña de inicio de sesión del usuario, así como la gestión de certificados de raíz , claves y notas seguras.

Su interfaz gráfica de usuario muestra varios llaveros, donde generalmente hay al menos dos: el llavero de inicio de sesión y el llavero del sistema. También incluye la utilidad de primeros auxilios de Keychain (que fue eliminada por la actualización 10.11.2) que puede reparar problemas con los llaveros. Varios eventos pueden causar problemas con los Llaveros, y algunas veces la única solución a un problema es eliminar el Llavero, que también elimina las contraseñas almacenadas en el Llavero, y crear una nueva.

Generalmente se encuentra en la carpeta Utilidades en Aplicaciones en macOS. Como una aplicación auxiliar de macOS, está sujeta a actualizaciones a través de la Actualización de Software y, por lo tanto, no debe retirarse de la carpeta de Utilidades. También hay una herramienta de línea de comandos incluida para acceder al llavero, llamada "seguridad".

 Historia
Los llaveros se desarrollaron inicialmente para el sistema de correo electrónico de Apple, PowerTalk, a principios de los años noventa. Entre sus muchas características, PowerTalk utilizó complementos permitían recuperar el correo de una amplia variedad de servidores de correo y servicios en línea. El concepto de llavero naturalmente se "cayó" de este código, y se usó en PowerTalk para administrar todas las credenciales de inicio de sesión de un usuario para los diversos sistemas de correo electrónico a los que PowerTalk podía conectarse.

Las contraseñas no eran fáciles de recuperar debido al cifrado, pero la simplicidad de la interfaz permitía al usuario seleccionar una contraseña diferente para cada sistema sin temor a olvidarlas, ya que una sola contraseña abriría el archivo y las devolvería a todas. En ese momento, las implementaciones de este concepto no estaban disponibles en otras plataformas. Keychain fue una de las pocas partes de PowerTalk que obviamente fue útil "por sí sola", lo que sugería que debería promoverse para convertirse en parte del Mac OS básico. Pero debido a la política interna , se mantuvo dentro del sistema PowerTalk y, por lo tanto, estuvo disponible para muy pocos usuarios de Mac.

No fue hasta el regreso de Steve Jobs en 1997 que el concepto de Llavero fue revivido desde el PowerTalk ahora descontinuado. En este punto en el tiempo, el concepto ya no era tan inusual, pero aun así era raro ver un sistema de llavero que no estuviera asociado con una pieza particular de software de aplicación, generalmente un navegador web. Keychain se convirtió posteriormente en una parte estándar de Mac OS 9, y se incluyó en Mac OS X en las primeras versiones comerciales.

 Seguridad
Keychain se distribuye tanto con iOS como con OSX. La versión de iOS es más sencilla porque las aplicaciones que se ejecutan en dispositivos móviles normalmente solo necesitan características muy básicas de Llavero. Por ejemplo, funciones como ACL (listas de control de acceso) y compartir elementos de llavero entre diferentes aplicaciones no están presentes. Por lo tanto, los elementos del llavero iOS solo son accesibles para la aplicación que los creó.

 Véase también

 Gestor de contraseñas
 Criptografía

 Referencias
