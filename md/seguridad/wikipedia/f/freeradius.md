---
type: Artículo de enciclopedia
title: FreeRADIUS
description: FreeRADIUS es una suite basada en el protocolo RADIUS, de tipo modular, desarrollada y distribuida bajo la Licencia Pública General GNU, versión 2.
resource: https://es.wikipedia.org/wiki/FreeRADIUS
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/FreeRADIUS"}
license: CC BY-SA 4.0
id: eswiki-FreeRADIUS
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# FreeRADIUS

**FreeRADIUS** es una suite basada en el protocolo RADIUS, de tipo modular, desarrollada y distribuida bajo la Licencia Pública General GNU, versión 2. Es gratuita para su descarga y uso. La suite FreeRADIUS incluye un servidor RADIUS, una biblioteca cliente RADIUS con licencia BSD, una biblioteca PAM, un módulo Apache y numerosas utilidades y bibliotecas de desarrollo adicionales relacionadas con RADIUS.

FreeRADIUS es hoy día el servidor RADIUS de código abierto más populary el más implementado en el mundo. Admite todos los protocolos de autenticación comunes y viene con una herramienta de administración de usuarios web basada en PHP llamada dialupadmin . Suele ser la base de muchos productos y servicios RADIUS comerciales, entre los cuales están sistemas embebidos, dispositivos RADIUS que admiten control de acceso a la red y WiMAX.

Satisface las necesidades de tipo AAA (autenticación, autorización y responsabilidad) de muchas empresas. También es ampliamente utilizado en la comunidad académica, incluyendo el servicio Eduroam.

 Historia
FreeRADIUS fue creado en agosto de 1999 por Alan DeKok y Miquel van Smoorenburg. Miquel había desarrollado previamente el servidor RADIUS Cistron, que alcanzó gran popularidad una vez que el servidor Livingston dejó de recibir mantenimiento.

A noviembre de 2014, el proyecto FreeRADIUS contaba con tres miembros en su equipo principal: Alan DeKok (líder del proyecto), Arran Cudbard-Bell (arquitecto principal) y Matthew Newton.

La última versión principal es FreeRADIUS 3. FreeRADIUS 3 incluye compatibilidad con RADIUS sobre TLS, incluyendo RadSec, un módulo rlm_ldap completamente reescrito y cientos de otras mejoras menores de consistencia y usabilidad. La última versión, ya consolidada, se mantiene priorizando la estabilidad sobre las funcionalidades.

La versión principal anterior v2.2.x ha entrado en la fase final de su ciclo de vida y ahora solo recibirá correcciones de seguridad

Una encuesta realizada en 2006 mostró que su base de usuarios asciende a 100 millones de personas.

 Características
Los módulos incluidos en el núcleo del servidor admiten LDAP, MySQL, PostgreSQL, Oracle y muchas otras bases de datos. Admite todos los tipos de autenticación EAP populares, incluidos PEAP y EAP-TTLS . Se incluyen más de 100 diccionarios de fabricantes, lo que garantiza la compatibilidad con una amplia gama de dispositivos NAS (Servidores de acceso a la red).

La versión 2.0.0 añadió compatibilidad con alojamiento virtual, IPv6, VMPS y un nuevo lenguaje de políticas que simplifica muchas configuraciones complejas.

 Herramientas de gestión de FreeRADIUS

 : una aplicación web avanzada de gestión RADIUS para administrar puntos de acceso y despliegues de ISP de propósito general. Incluye gestión de usuarios, informes gráficos, contabilidad, un motor de facturación y se integra con OpenStreetMap para geolocalización. El sistema se basa en freeRADIUS, con el que comparte el acceso a la base de datos backend.
 phpRADmin: una herramienta escrita en PHP destinada a gestionar la administración y el aprovisionamiento de FreeRADIUS a través de la Web con MySQL como backend.
 Dialup Admin: una potente interfaz web escrita en PHP que viene con FreeRADIUS para administrar usuarios RADIUS. Dialup Admin admite usuarios en SQL (compatible con MySQL y PostgreSQL) o en LDAP. Ya no se encuentra en desarrollo activo.
 : aplicación de gestión basada en web. Su objetivo principal es proporcionar al administrador de servidores RADIUS o puntos de acceso una aplicación de gestión web sencilla. FreeRADIUS debe configurarse para usar MySQL como base de datos.
 : RADIUSdesk se ha desarrollado desde 2012 como una herramienta para gestionar Internet inalámbrica y ha estado en constante desarrollo desde entonces.

 Véase también

 Autenticación, Autorización y Responsabilidad
 Network access server
 Protocolo Diameter, propuesta de reemplazo para RADIUS.

 Referencias

 Enlaces externos

 FreeRADIUS wiki
