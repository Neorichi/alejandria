---
type: Artículo de enciclopedia
title: Copy Fail
description: "CVE-2026-31431, comúnmente conocida como Copy Fail, es una vulnerabilidad en el kernel de Linux que permite la escalada de privilegios no autorizada, divulgada por la empresa de seguridad Theori al público el 29 de …"
resource: https://es.wikipedia.org/wiki/Copy_Fail
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Copy_Fail"}
license: CC BY-SA 4.0
id: eswiki-Copy_Fail
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Copy Fail

- **Puntaje:** 7.8

**CVE-2026-31431**, comúnmente conocida como ***Copy Fail***, es una vulnerabilidad en el kernel de Linux que permite la escalada de privilegios no autorizada, divulgada por la empresa de seguridad Theori al público el 29 de abril de 2026 y al equipo de seguridad del kernel de Linux cinco semanas antes. Este exploit de Python de 10 líneas se integra en la actividad normal del sistema a través de llamadas al sistema estándar; posteriormente fue portado a otros lenguajes.

 Características
La vulnerabilidad permite que un usuario sin privilegios utilice la familia de direcciones AF_ALG en la API criptográfica del kernel de Linux para realizar escrituras controladas de 4 bytes en la caché de páginas, que respalda las copias en memoria de los archivos.

Al reemplazar el código en la copia en memoria de un ejecutable legible almacenado en la caché de páginas, un atacante puede escalar privilegios de usuario cuando cualquier proceso privilegiado ejecuta posteriormente esa versión corrupta del archivo. Dado que la mayoría de las utilidades de Linux para cambiar de usuario (por ejemplo, su) se ejecutan con privilegios mediante setuid, la superficie de escalada de privilegios de usuario es amplia.

 Software afectado
Todas las distribuciones de Linux que utilizan versiones del kernel de Linux entre 4.14 (2017) y 6.19.12 están en riesgo. Debian, Ubuntu, SUSE, Red Hat Enterprise Linux y otras distribuciones de Linux se vieron afectadas.

Muchas distribuciones y fuentes de seguridad recomendaron mitigar el problema deshabilitando el módulo del kernel algif_aead afectado. Algunas distribuciones, como Arch Linux, Fedora, y Amazon Linux, habían publicado parches en el momento de la divulgación, pero la vulnerabilidad fue divulgada por Theori antes de que las distribuciones afectadas que anunciaron como vulnerables hubieran publicado parches.   SUSE, Red Hat y Ubuntu han publicado guías de mitigación. A partir del 5 de mayo, se han añadido reglas de detección de Kaspersky Lab.

Los mecanismos MAC, como SELinux y AppArmor, pueden mitigar la vulnerabilidad, pero solo cuando están configurados de manera que únicamente los servicios legítimamente necesarios tengan acceso a la familia de sockets AF_ALG. En las configuraciones predeterminadas, cualquier proceso sin restricciones o con permisos amplios aún puede abrir sockets AF_ALG, por lo que la protección es prácticamente inexistente y la vulnerabilidad sigue siendo alcanzable.

Según GrapheneOS, Android no se ve afectado debido a su uso de políticas SELinux, donde solo el proceso dumpstate (utilizado para informes de errores) tiene permiso para crear sockets AF_ALG.

 Referencias

 Enlaces externos

  en GitHub
