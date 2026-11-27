---
type: Artículo de enciclopedia
title: OpenSSH
description: OpenSSH (Open Secure Shell) es un conjunto de aplicaciones que permiten realizar comunicaciones cifradas a través de una red, usando el protocolo SSH.
resource: https://es.wikipedia.org/wiki/OpenSSH
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/OpenSSH"}
license: CC BY-SA 4.0
id: eswiki-OpenSSH
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# OpenSSH

- **Nombre:** OpenSSH
- **Desarrollador:** Proyecto OpenBSD
- **Última versión:** 10.6
- **Sistema operativo:** Multiplataforma
- **Género:** Acceso remoto
- **Licencia:** BSD

**OpenSSH** (**Open Secure Shell**) es un conjunto de aplicaciones que permiten realizar comunicaciones cifradas a través de una red, usando el protocolo SSH. Fue creado como una alternativa libre y abierta al programa Secure Shell, que es software propietario. El proyecto está liderado por Theo de Raadt, residente en Calgary.

 Historia
Sus desarrolladores aseguran que OpenSSH es más seguro que el original, lo cual es debido a la conocida reputación de los desarrolladores de OpenBSD por crear código limpio y perfectamente auditado, lo que contribuye a que sea más seguro. Su seguridad también es atribuible al hecho de que su código fuente se distribuya libremente con una licencia BSD. Aunque todo el código fuente del SSH original también está disponible, existen restricciones con respecto a su uso y distribución, lo que convierte a OpenSSH en un proyecto mucho más atractivo para nuevos desarrolladores.

 Vulnerabilidad *regreSSHion*

En 2024 se reportó una vulnerabilidad de nivel crítico, en la versión 8.5p1 y superiores, que permitía a un atacante no autenticado ejecutar código arbitrario de forma remota con privilegios de *root* y, por tanto, tomar el control completo de las máquinas afectadas. Esta vulnerabilidad, que se estima que afectó a unos 14 millones de servidores, fue bautizada como *regreSSHion* porque el problema ya se había reportado previamente en 2006 y fue corregido en la versión 4.4p1, pero se reintrodujo nuevamente en la versión 8.5p1 en octubre de 2020.

 Características técnicas

 Portabilidad
Como OpenSSH es una aplicación de comunicación entre ordenadores, debe funcionar en la mayor cantidad de sistemas operativos posibles, para lo que existe un equipo, llamado OpenSSH Portability Team que se responsabiliza de añadir el código necesario para portar el software a todas las plataformas posibles.

 Aplicaciones incluidas
La *suite* OpenSSH incluye:
 *ssh*, reemplaza a rlogin y telnet para permitir shell el acceso remoto a otra máquina. ssh tero@ejemplo.com
 *scp*, reemplaza a rcp scp tero@ejemplo.com:~/archivo .
 *sftp*, reemplaza a ftp para copiar archivos entre dos computadoras sftp tero@ejemplo.com
 *sshd*, el servidor demonio SSH sshd
 *ssh-keygen*, una herramienta para inspeccionar y generar claves RSA y DSA  que son usadas para la autenticación del cliente o usuario.
 *ssh-agent y ssh-add*, herramientas para autenticarse de manera más fácil, manteniendo las claves listas para no tener que volver a introducir la frase de acceso cada vez que utilice la clave.
 *ssh-keyscan*, que escanea una lista de clientes y recolecta sus claves públicas.
El servidor OpenSSH puede autenticar a los usuarios mediante todos los métodos estándar del protocolo ssh

 Túneles seguros
Muchas aplicaciones pueden ser securizadas con OpenSSH, haciendo de este sistema una potente alternativa para sistemas VPN.

Cualquier aplicación que use conexiones por TCP (preferiblemente con un solo puerto tcp) puede ser utilizada a través de túnel seguro- Algunos ejemplos de aplicaciones fácilmente *tunelizables* son el X Window System, http usando un proxy y VNC. El túnel para el X Window System se crea automáticamente entre dos ordenadores corriendo Unix, así que las aplicaciones con interfaces gráficas pueden ser ejecutadas desde ordenadores remotos simplemente escribiendo sus nombres:
  ssh -Y tero@ejemplo.com
  password:
  $ xclock

Entre las aplicaciones cuya *tunelización* es posible, aunque compleja, se encuentran el ftp (no es necesario, debido a la existencia de sftp) y SMB.

Algunas aplicaciones llaman a OpenSSH para crear el túnel, tales como DistCC, CVS, rsync y fetchmail.

Se pueden montar sistemas de archivos remotos a través de ssh usando shfs, lufs o podfuk.

 Autenticación
El servidor OpenSSH autentica a los usuarios usando sus propios sistemas de autenticación, implementados en el propio software:
 Clave pública (id.rsa, authorized_keys)
 Contraseña
 Kerberos/GSSAPI

OpenSSH también puede usar PAM para llevar a cabo la autenticación. PAM permite la selección de métodos de autenticación y su política en tiempo de ejecución, permitiendo métodos avanzados de autenticación tales como:
 OTPW
 S/KEY
 OPIE

Las versiones de OpenSSH más antiguas que la 3.7 deben ser ejecutadas como root siempre que el soporte PAM esté activado, ya que se requieren permisos de root para activar el PAM. Las versiones más recientes de OpenSSH permiten desactivar el uso de PAM estando en ejecución. Mediante este sistema usuarios normales pueden ejecutar instancias de sshd.

 Historial de versiones

La primera vez que apareció OpenSSH fue en la versión OpenBSD 2.6 y la primera versión independiente fue realizada en octubre de 1999.

Historia de las publicaciones :

 OpenSSH 8.8: 26 de septiembre de 2021
 Incluye un aviso de descontinuación de los protocolos scp/rcp para utilizar SFTP en su defecto.
 OpenSSH 8.7: 20 de agosto de 2021
 OpenSSH 8.6: 19 de abril de 2021
 OpenSSH 8.5: 3 de marzo de 2021
 OpenSSH 8.4: 27 de septiembre de 2020
 OpenSSH 8.3: 27 de mayo de 2020
 OpenSSH 8.2: 14 de febrero de 2020
 OpenSSH 8.1: 9 de octubre de 2019
 OpenSSH 8.0: 17 de abril de 2019
 OpenSSH 7.9: 19 de octubre de 2018
 OpenSSH 7.8: 24 de agosto de 2018
 OpenSSH 7.7: 3 de abril de 2018
 OpenSSH 7.5: 20 de marzo de 2017
 OpenSSH 7.3: 1 de agosto de 2016
 OpenSSH 7.2: 29 de febrero de 2016
 OpenSSH 7.1: 21 de agosto de 2015
 OpenSSH 7.0: 11 de agosto de 2015
 OpenSSH 6.9: 1 de julio de 2015
 OpenSSH 6.8: 18 de marzo de 2015
 OpenSSH 6.7: 6 de octubre de 2014
 OpenSSH 6.6: 15 de marzo de 2014
 OpenSSH 6.5: 30 de enero de 2014
 OpenSSH 6.4: 8 de noviembre de 2013
 OpenSSH 6.3: 13 de septiembre de 2013
 OpenSSH 6.2: 22 de marzo de 2013
 OpenSSH 6.1: 29 de agosto de 2012
 OpenSSH 6.0: 22 de abril de 2012
 OpenSSH 5.9: 6 de septiembre de 2011
 OpenSSH 5.8: 4 de febrero de 2011
 OpenSSH 5.7: 24 de enero de 2011
 OpenSSH 5.6: 23 de agosto de 2010
 OpenSSH 5.5: 16 de abril de 2010
 OpenSSH 5.4: 8 de marzo de 2010
 OpenSSH 5.3: 1 de octubre de 2009
 OpenSSH 5.2: 23 de febrero de 2009
 OpenSSH 5.1: 21 de junio de 2008
 OpenSSH 5.0: 3 de abril de 2008
 OpenSSH 4.9: 30 de marzo de 2008
 Incorporó soporte chroot para sshd
 OpenSSH 4.7: 4 de septiembre de 2007
 OpenSSH 4.6: 9 de marzo de 2007
 OpenSSH 4.5: 7 de noviembre de 2006
 OpenSSH 4.4: 27 de septiembre de 2006
 OpenSSH 4.3: 1 de febrero de 2006
 OpenSSH 4.2: 1 de septiembre de 2005
 OpenSSH 4.1: 26 de mayo de 2005
 OpenSSH 4.0: 9 de marzo de 2005
 OpenSSH 3.9: 17 de agosto de 2004
 OpenSSH 3.8: 24 de febrero de 2004
 OpenSSH 3.7.1: 16 de septiembre de 2003
 OpenSSH 3.7: 16 de septiembre de 2003
 OpenSSH 3.6.1: 1 de abril de 2003
 OpenSSH 3.6: 31 de marzo de 2003
 OpenSSH 3.5: 14 de octubre de 2002
 OpenSSH 3.4: 26 de junio de 2002

 Véase también
 Open Source Security Foundation

 Libros
 Michael Stahnke, *Pro OpenSSH.* (Inglés) ISBN 1-59059-476-2.
 Daniel J. Barrett, Richard E. Silverman, and Robert G. Byrnes, *SSH, The Secure Shell: The Definitive Guide, Second Edition.* ISBN 0-596-00895-3 (Inglés, primera edición ISBN 0-596-00011-1).

 Referencias

 Enlaces externos

 Página de OpenSSH (Inglés)
 Distribuciones portables (Inglés)
