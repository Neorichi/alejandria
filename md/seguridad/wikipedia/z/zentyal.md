---
type: Artículo de enciclopedia
title: Zentyal
description: "Zentyal es una solución de correo electrónico y groupware de código abierto, compatible de forma nativa con Microsoft Outlook®."
resource: https://es.wikipedia.org/wiki/Zentyal
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Zentyal"}
license: CC BY-SA 4.0
id: eswiki-Zentyal
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Zentyal

- **Name:** Zentyal
- **Captura:** thumb|Zentyal, sección de correo electrónico
- **Desarrollador:** Zentyal S.L.
- **Familia:** Unix-like
- **Estado actual:** En desarrollo
- **Modelo actualización:** APT
- **Modelo desarrollo:** Software libre y de código abierto
- **Núcleo:** Linux
- **Última versión:** 8.1
- **Ui:** Interfaz de administración web

**Zentyal** es una solución de correo electrónico y groupware de código abierto, compatible de forma nativa con Microsoft Outlook®. Zentyal implementa protocolos Microsoft® Exchange sobre componentes estándares de código abierto (como Dovecot, Postfix, Samba, etc.) para proporcionar compatibilidad nativa con clientes Microsoft Outlook®. Los protocolos de correo electrónico y groupware soportados por Zentyal son MAPI, ActiveSync, EWS, SMTP, POP, IMAP, CalDAV, CardDAV y Active Directory.

Zentyal se distribuye en dos paquetes: Zentyal Server para PYMEs y Zentyal Cloud para proveedores de hosting. Zentyal Server tiene una edición de desarrollo que puede descargarse de forma gratuita y cuyo código fuente está disponible bajo los términos de la GNU General Public License.

 Principales características de Zentyal Server

 Compatibilidad nativa con los protocolos de Microsoft® Exchange Server.
 Soporte para Microsoft Outlook® 2007, 2010.
 Compatibilidad nativa con Microsoft Active Directory® 2008, 2008R2, 2012.
 Correo electrónico, calendarios, contactos.
 Sincronización con dispositivos móviles (soporte para ActiveSync®).
 Antivirus y *antispam*.
 Empaquetado en un servidor basado en Ubuntu, que incluye controlador de dominio y servicio de directorio, servicios básicos de redes y cortafuegos.

 Desarrollo

Zentyal usa un modelo de software libre, con todo el código abierto disponible para sus usuarios.

 Diseño

Zentyal es una aplicación web que usa el servidor web NGINX con mod perl como estrato y componentes Mason como bloques de construcción, principalmente escrito en Perl orientado a objetos, con algunas mejoras visuales con Javascript.

Su diseño incorpora técnicas de programación modernas como:

 Patrones de diseño: un patrón de diseño observador usado principalmente para integrar diferentes módulos en Zentyal. Por ejemplo, cada servicio informa sobre que puertos necesitan que estén abiertos. Además, un patrón Singleton se usa para almacenar la configuración y comportamiento global.
 Desacoplamiento de la lógica y presentación: la interfaz de usuario usa CSS y AJAX, e incluye varios componentes Mason, como una tabla genérica usada para configurar servicios. La lógica del programa reside en los paquetes de las bibliotecas y en el código CGI.
 Tolerancia a fallos: los errores y avisos se manejan a través de excepciones software, yendo desde el núcleo hasta la rutina manejadora.

También ofrece la arquitectura para la búsqueda de errores, integrando la distribución de la pila de ejecución del intérprete de Perl 5.

Cada proceso de cada servicio se monitoriza por si este muere y es relanzado automáticamente.

 Componentes de software libre

Zentyal se construye sobre componentes comunes y estables de software libre:

 OpenSSL
 Criptografía
 Netfilter/iptables
 Cortafuegos
 Traducción de direcciones de red
 BIND
 Servidor de nombres de dominio
 Postfix
 Servidor de correo electrónico
 Ntpd
 Sincronización de fecha y hora
 OpenVPN
 Redes privadas virtuales
 Samba
 Almacenamiento compartido
 Autentificación compartido para clientes Windows
 Sistema de impresión común de Unix (CUPS)
 Impresoras compartidas
 Advanced Packaging Tool (APT)
 Instalación y actualización de software
 Dovecot
 Servidor de IMAP y POP3

La distribución completa usa Ubuntu 18.04 LTS (Bionic Beaver).

 Comunidad

La comunidad principal de Zentyal se encuentra en el Foro de Soporte de Zentyal.

La inclusión de Zentyal (eBox Platform) en Ubuntu Gutsy Gibbon fue precedida por algunos comentarios en la comunidad Ubuntu Forums.

Hay también un grupo muy activo de usuarios de Linkstation que consiguieron portar eBox Platform a un PowerPC.

 Protocols Plugfest

En mayo de 2015, Zentyal organizó, patrocinada por Microsoft, la primera Protocols Plugfest en Europa, enfocada a comunidades y empresas tecnológicas de código abierto para presentar, probar e intercambiar contenidos e ideas técnicas sobre protocolos abiertos e interoperabilidad.

 Documentación

 Usuarios

 Guía de instalación: tiene las instrucciones para los diferentes métodos de instalación de Zentyal como el CD y los paquetes de Ubuntu, cómo conseguir el código fuente y ejecutar Zentyal desde cero.
 Documentación oficial para Zentyal (disponible en inglés y en español): dirigida a usuarios de Zentyal, introduce los conceptos y la terminología, explicando los diferentes servicios y casos de uso.
 Documentos adicionales: Lista completa de la documentación disponible, incluyendo How-tos, Preguntas frecuentes, Screencasts y otros documentos.
 Referencia de API: descripción y parámetros de clases y métodos.

 Desarrolladores
 Instrucciones para los desarrolladores: Tutoriales y consejos dirigidos a los desarrolladores del software, incluyendo una guía de desarrollo del módulos, instrucciones cómo crear los paquetes de Zentyal para Debian o un entorno de desarrollo.

 Referencias

 Enlaces externos
 Oficiales
 Página oficial del proyecto (en inglés)
 Página de colaborativa del proyecto (en inglés)
 Página de internacionalización (en inglés)
 Página de la empresa que financia el proyecto

 Otros
 Informe de Ohloh de eBox platform  (en inglés)
 "Usando eBox como Controlador Primario de Dominio" en Howtoforge" (en inglés)
 "Ejecutando un servidor de ficheros, impresoras, proxy, DHCP y servidor de tiempo para la pequeña y mediana empresa" en Howtoforge" (en inglés)
  (en inglés)
