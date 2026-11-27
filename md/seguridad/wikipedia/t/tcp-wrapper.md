---
type: Artículo de enciclopedia
title: TCP Wrapper
description: "TCP Wrapper (\"Envoltorio de TCP\") es un sistema de red ACL que trabaja en terminales y que se usa para filtrar el acceso de red a servicios de protocolos de Internet que corren en sistemas operativos (tipo UNIX), como …"
resource: https://es.wikipedia.org/wiki/TCP_Wrapper
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/TCP_Wrapper"}
license: CC BY-SA 4.0
id: eswiki-TCP_Wrapper
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# TCP Wrapper

- **Nombre:** TCP Wrapper
- **Desarrollador:** Wietse Venema
- **Ultima version:** 7.6
- **Sistema operativo:** tipo UNIX
- **Genero:** Seguridad
- **Licencia:** Licencia BSD

**TCP Wrapper** ("*Envoltorio de TCP*") es un sistema de red ACL que trabaja en terminales y que se usa para filtrar el acceso de red a servicios de protocolos de Internet que corren en sistemas operativos (tipo UNIX), como GNU/Linux o BSD. Permite que las direcciones IP, los nombres de terminales y/o respuestas de consultas ident de las terminales o subredes sean usadas como *tokens* sobre los cuales filtrar para propósitos de control de acceso.

El código original fue escrito por Wietse Venema de la Universidad Técnica de Eindhoven, Países Bajos, entre los años 1990 y 1995. Desde el 1 de junio de 2001, el programa es lanzado bajo su propia licencia tipo BSD.

El tarball incluye una biblioteca llamada **libwrap** que implementa la funcionalidad en sí. Inicialmente, solo aquellos servicios que se creaban a partir de cada conexión a un super Servidor (como inetd) eran *envueltos* (de ahí su nombre) utilizando el programa 'tcpd'. Sin embargo, los demonios de servicio de red más comunes de hoy en día pueden ser enlazados contra libwrap en forma directa. Los demonios que operan sin crear descendientes de un super servidor usan esto, o un proceso único que maneja conexiones múltiples. En caso contrario, solo el primer intento de conexión se chequearía contra sus ACLs.

Al compararse con las directivas de control de acceso de una terminal, que comúnmente se encuentran en los archivos de configuración de los demonios, TCP Wrappers tienen el beneficio de una reconfiguración de ACL en tiempo de ejecución (es decir, los servicios no necesitan ser cargados nuevamente o reiniciados) y de una aproximación genérica a la administración de redes. Esto facilita su uso en scripts anti-gusano, tales como DenyHosts o Fail2ban, para agregar y sacar reglas de bloqueo a clientes, cuando estos producen excesivos intentos de conexión o varios errores en el proceso mismo.
Si bien fue escrito para proteger servicios de aceptación de TCP y UDP, también existen ejemplos de uso para filtrado de ciertos paquetes ICMP (tales como 'pingd' – el contestador de pedidos de pings del espacio de usuario).

 Véase también
 Seguridad informática
 Inetd
 DNS
 DNSSEC
 Ident
 NIS

 Referencias

 Wietse Venema: TCP WRAPPER Network monitoring, access control, and booby traps.  15 de julio de 1992
 Lee Brotzman: Wrap a Security Blanket Around Your Computer Artículo de Linuxjournal del 1.º de agosto de 1997

 Enlaces externos
 ITSO: TCP Wrappers overview
 HP: TCP Wrappers Information
 Example of 'pingd' with libwrap support
