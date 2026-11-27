---
type: Artículo de enciclopedia
title: Autorización
description: "En ingeniería de seguridad y seguridad informática, la autorización es una parte del sistema operativo que protege los recursos del sistema permitiendo que sólo sean usados por aquellos consumidores a los que se les ha …"
resource: https://es.wikipedia.org/wiki/Autorización
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Autorización"}
license: CC BY-SA 4.0
id: eswiki-Autorización
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Autorización

En ingeniería de seguridad y seguridad informática, la **autorización** es una parte del sistema operativo que protege los recursos del sistema permitiendo que sólo sean usados por aquellos consumidores a los que se les ha concedido autorización para ello. Los recursos incluyen archivos y otros objetos de dato, programas, dispositivos y funcionalidades provistas por aplicaciones. Ejemplos de consumidores son usuarios del sistema, programas y otros dispositivos.

 Visión general

El proceso de autorización se usa para decidir si la persona, programa o dispositivo "X" tiene permiso para acceder al dato, funcionalidad o servicio Y.

La mayoría de los sistemas operativos multiusuarios modernos incluyen un proceso de autorización. Este hace uso del proceso de autenticación para identificar a los consumidores. Cuando un consumidor intenta usar un recurso, el proceso de autorización comprueba que al consumidor le ha sido concedido permiso para usar ese recurso. Los permisos son generalmente definidos por el administrador de sistemas en algún tipo de «aplicación de políticas de seguridad», tales como una ACL o una capacidad, sobre la base del «principio de privilegio mínimo»: a los consumidores sólo se les deben conceder los permisos que necesitan para realizar su trabajo. Los sistemas operativos monousuarios más antiguos solían tener sistemas de autenticación y autorización débiles o carecían por completo de ellos.

Se llama «consumidores anónimos» o «invitados» a aquellos consumidores a los que no se les ha exigido que se autentiquen. A menudo tienen muy pocos permisos. En un sistema distribuido, suele ser deseable conceder acceso sin exigir una identidad única. Ejemplos familiares de tokens de autorización incluyen llaves y tiques, que permiten conceder acceso sin que se provea una identidad.

Existe también el concepto de consumidores «confiables» (*trusted*). Los consumidores que se han autenticado y a los que se señalan como confiables se les permite acceso ilimitado a los recursos. Los consumidores «parcialmente confiables» e invitados están sujetos a autorización para usar los recursos protegidos. Las aplicaciones de políticas de seguridad de algunos sistemas operativos, conceden por defecto a todos los consumidores acceso completo a todos los recursos. Otros hacen lo opuesto, insistiendo en que el administrador lleve a cabo acciones deliberadas para permitir a cada consumidor el uso de cada recurso.

 Véase también

 Ingeniería de seguridad
 Seguridad informática
 Autenticación
 Control de acceso
 Kerberos
 Sistema operativo
 Autorización OSID

 Referencias
