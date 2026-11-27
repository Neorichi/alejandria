---
type: Artículo de enciclopedia
title: Fail2ban
description: Fail2ban es una aplicación escrita en Python para la prevención de intrusos en un sistema, que actúa penalizando o bloqueando las conexiones remotas que intentan accesos por fuerza bruta.
resource: https://es.wikipedia.org/wiki/Fail2ban
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Fail2ban"}
license: CC BY-SA 4.0
id: eswiki-Fail2ban
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Fail2ban

- **Nombre:** Fail2ban
- **Género:** Sistema de prevención de intrusos
- **Autor:** Cyril Jaquier
- **Desarrollador:** Cyril Jaquier, Arturo 'Buanzo' Busleiman
- **Estado:** Estable, en desarrollo
- **Licencia:** GPL v2
- **Lenguaje programación:** Python

**Fail2ban** es una aplicación escrita en Python para la prevención de intrusos en un sistema, que actúa penalizando o bloqueando las conexiones remotas que intentan accesos por fuerza bruta. Se distribuye bajo licencia GNU y típicamente funciona en sistemas POSIX que tengan interfaz con un sistema de control de paquetes o un firewall local (como iptables o TCP Wrapper).

 Funcionamiento

Habitualmente las computadoras sufren ataques de fuerza bruta (especialmente servidores SSH, FTP, etc) con el fin de descifrar las contraseñas y acceder a ellas. En este punto es indispensable una buena política de contraseñas. Sin embargo, los ataques por fuerza bruta también consumen un gran ancho de banda, disparan el volumen de los archivos de registro (*logs*) de nuestro sistema y ocupan ciclos de CPU que podrían dedicarse a tareas útiles.

Fail2ban busca en los registros (*logs*) de los programas que se especifiquen las reglas que el usuario decida para poder aplicar una penalización. La penalización puede ser bloquear la aplicación que ha fallado en un determinado puerto, bloquearla para todos los puertos, etc. Las penalizaciones, así como las reglas, son definidas por el usuario.

Habitualmente, si las IP de ataque se prohíben por un lapso prudencial de tiempo, la sobrecarga de red provocada por los ataques baja, y también se reduce la probabilidad de que un ataque de fuerza bruta basada en diccionarios tenga éxito.

Ante una cantidad predefinida (por el usuario) de intentos fallidos, fail2ban determina la acción a tomar sobre la IP que originó el problema. Puede simplemente notificar por correo electrónico del suceso, denegar el acceso a la IP atacante, bloquearla en determinado puerto y habilitarla en otros (modificando las entradas correspondientes en iptables, o el firewall local que corresponda), etc. Puede asimismo levantar las prohibiciones después de un determinado periodo, por si el problema no obedeciera a un ataque sino simplemente a errores del usuario intentando loguearse. Las acciones son configurables mediante guiones de Python.

 Soporte actual
Actualmente fail2ban establece filtros para Apache, sshd, qmail, vsftpd, lighttpd, Postfix y Courier Mail Server. Los filtros son escritos con expresiones regulares de Python que establecen la regla que hará disparar una determinada acción sobre la IP que origina el hecho. La tupla (regla, acción) o (filtro, acción) es llamado “Jail” o “prisión”, y es lo que determina la penalización a un host maligno.

 Véase también
 Servidor HTTP Apache
 Servidor Web Lighttpd
 Servidor de Correo Qmail
 Servidor de Correo Postfix

 Referencias

 Enlaces externos
 Página oficial
 Proyecto alojado en GitHub
 Proyecto alojado en Sourceforge
 Paquete de la Distribución Debian GNU/Linux
 Configuración de fail2ban en Linux
