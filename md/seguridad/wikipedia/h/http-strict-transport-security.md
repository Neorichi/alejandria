---
type: Artículo de enciclopedia
title: HTTP Strict Transport Security
description: "HTTP Strict Transport Security o HTTP con Seguridad de Transporte Estricta (HSTS), es una política de seguridad web establecida para evitar ataques que puedan interceptar comunicaciones, cookies, etc. Según este …"
resource: https://es.wikipedia.org/wiki/HTTP_Strict_Transport_Security
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/HTTP_Strict_Transport_Security"}
license: CC BY-SA 4.0
id: eswiki-HTTP_Strict_Transport_Security
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# HTTP Strict Transport Security

**HTTP Strict Transport Security** o HTTP con Seguridad de Transporte Estricta (HSTS), es una política de seguridad web establecida para evitar ataques que puedan interceptar comunicaciones, cookies, etc. Según este mecanismo un servidor web declara que los agentes de usuario compatibles (es decir, los navegadores), solamente pueden interactuar con ellos mediante conexiones HTTP seguras (es decir, en HTTP sobre TLS/SSL). HSTS es un estándar del IETF y se especifica en el RFC 6797.

La política HSTS es comunicada por el servidor al navegador a través de un campo de la cabecera HTTP de respuesta denominado "Strict Transport-Security". La política HSTS especifica un período de tiempo durante el cual el agente de usuario deberá acceder al servidor sólo en forma segura.

 Historia
La especificación HSTS se publicó como RFC 6797 el 19 de noviembre de 2019 después de ser aprobado el 19 de octubre de 2019 por la IESG para su publicación como un estándar propuesto RFC.  Los autores originalmente lo presentaron como Borrador de Internet el 17 de junio de 2010. Fue con la conversión a un Borrador de Internet que el nombre de la especificación se modificó a "Seguridad de Transporte HTTP estricta" desde el original "seguridad de transporte estricta" (STS). La razón de este cambio de nombre fue debido a que era específica para HTTP. La última "versión comunitaria" de la entonces llamada especificación "STS" fue publicada el 18 de diciembre de 2009, con revisiones basadas en la retroalimentación de la comunidad.
El borrador de la especificación original de Jeff Hodges de PayPal, Collin Jackson y Adam Barth, fue publicado el 18 de septiembre de 2009.

La especificación HSTS está basado en obra original de Jackson y Barth como se describe en su artículo “ForceHTTPS: Protecting High-Security Web Sites from Network Attacks”.

Además, HSTS es la realización de una faceta de una visión global para mejorar la seguridad web, presentada por Jeff Hodges y Andy Steingruebl en su artículo del 2010 The Need for Coherent Web Security Policy Framework(s).

 Resumen del mecanismo HSTS
Cuando una aplicación web envía la política HSTS al agente del usuario, los que cumplan con el estándar se comportan de la siguiente manera:

 Los vínculos inseguros que hacen referencia a la aplicación web se convierten automáticamente en enlaces seguros. (Por ejemplo, http://example.com/some/page/ se modificará a https://example.com/some/page/ antes de acceder al servidor.)
 Si la seguridad de la conexión no se puede asegurar (por ejemplo, el certificado TLS del servidor es autofirmado), muestran un mensaje de error y no permiten al usuario acceder a la aplicación web.
La política HSTS ayuda a proteger a los usuarios de aplicaciones web contra algunos ataques de red pasivos (eavesdropping) y activos. Un atacante man-in-the-middle tiene una capacidad muy reducida para interceptar las peticiones y respuestas entre un usuario y un servidor de aplicaciones web, mientras que el navegador del usuario tenga una política HSTS vigente para esa aplicación web.

 Aplicabilidad
La vulnerabilidad de seguridad más importante que HSTS puede prevenir es la extracción de SSL (SSL-stripping) en ataques man-in-the-middle, introducidas por primera vez por Moxie Marlinspike en su charla "New Tricks to defeat SSL in Practice" en la BlackHat Federal de 2009. El ataque de extracción SSL funciona (tanto en SSL como en TLS) convirtiendo una conexión segura HTTPS a una conexión plana en HTTP transparentemente. El usuario puede ver que la conexión es insegura, pero fundamentalmente no hay forma de saber si la conexión debe ser segura. Muchos sitios web no utilizan TLS/SSL, por lo tanto, no hay forma de saber (sin conocimientos previos) si el uso de HTTP plano se debe a un ataque, o simplemente porque el sitio no ha implementado TLS/SSL. Además, no hay advertencias que se presenten al usuario durante el proceso de bajada, haciendo que el ataque bastante sutil para todos menos el más vigilante. La herramienta sslstrip de Marlinspike automatiza completamente el ataque.

HSTS soluciona este problema, informando al navegador que las conexiones al sitio siempre debe usar TLS / SSL. La cabecera HSTS puede ser despojada por el atacante si esta es la primera visita del usuario. El navegador Chrome intenta limitar este problema mediante la inclusión de una lista de sitios HSTS "pre-cargada" Desafortunadamente, esta solución no puede ampliarse para incluir todos los sitios web en Internet. Una posible solución podría lograrse mediante el uso de los registros DNS para declarar la política HSTS y acceder de forma segura a través de DNSSEC, opcionalmente con huellas digitales de certificados para asegurar su validez. HSTS también puede ayudar a evitar tener una cookie de inicio de sesión basado sitio web credenciales robadas por herramientas ampliamente disponibles, como Firesheep.

 Limitaciones
La solicitud inicial permanece sin protección contra ataques activos si utiliza un protocolo no seguro, como HTTP simple o si la URL de la solicitud inicial se obtuvo a través de un canal inseguro. Lo mismo se aplica a la primera petición después de que el período de actividad que se especifican en la política HSTS anunciada max-age (los sitios deben establecer un período de varios días o meses dependiendo de la actividad del usuario y su comportamiento). Google Chrome aborda esta limitación mediante la implementación de una "lista STS precargada".

Incluso con dicha "lista de STS precargado", HSTS no puede evitar los ataques avanzados como BEAST o CRIME (ambos fueron presentados por Juliano Rizzo y Thai Duong). Esto es porque los ataques son contra TLS/SSL en sí, y por lo tanto son ortogonales a la aplicación de la política HSTS.

Consulte el RFC 6797 para una discusión general de las consideraciones de seguridad HSTS.

 Soporte de navegadores
 Google Chrome admite HSTS partir de la versión 4.0.211.0.
 HSTS está incluido en Firefox 4. Con Firefox 17, Mozilla da una lista de sitios web que soportan HSTS.
 Opera 12
 La extensión NoScript para Firefox impone HSTS partir de la versión 1.9.8.9.
 La extensión HTTPS Everywhere para Firefox, derivada de NoScript, generaliza el concepto de HSTS, para incluir subconjuntos de los caminos en algunos dominios y reescritura de URI inseguros http:// en un dominio para obtener los https:// en otro. (por ejemplo, de http://en.wikipedia.org/wiki/ a https://secure.wikimedia.org/wikipedia/en/wiki/)
 Internet SSL Survey 2010 v1.6
 STS - Los Proyectos Chromium

 Implementaciones
Las cabeceras STS deben ser enviadas solamente a través de las respuestas HTTPS. Las implementaciones de cliente no deben respetar los encabezados enviados a través de respuestas no HTTPS o respuestas sobre HTTPS que no utilizan certificados de confianza correctamente configurados. Los fragmentos de configuración de servidor siguientes deben estar dentro del contexto de un bloque de configuración de sitio SSL, y los ejemplos de código están destinados a estar dentro del contexto de respuestas HTTPS solamente.

Tenga en cuenta que el máximo de edad se presenta en segundos. Los 31536000 segundos (12 meses) en los siguientes ejemplos se pueden cambiar, dependiendo de cuánto tiempo el operador del servidor web está dispuesto a comprometerse a utilizar HTTPS solamente. Se recomienda establecer el máximo de edad a un valor tan grande como 31536000 (12 meses) o 63072000 (24 meses).

Tenga en cuenta también que el encabezado HSTS sólo se debe enviar cuando se usa una conexión segura (HTTPS) y no cuando se utiliza HTTP.

Implementación en Apache:

Implementación en lighttpd.

Implementación en nginx.

Implementación en PHP.

Implementación en Perl CGI.

Implementación en Ruby on Rails.

Implementación en ASP.

Implementación en  C# / ASP.NET. Código en el archivo global.asax:

Implementación en ColdFusion Markup Language (CFML).

Implementación en JavaServer Pages (JSP) o Java Servlets.

Implementación en Visual Basic .NET.

Implementación como Struts 2 interceptor en Java.

 Véase también
 Hypertext Transfer Protocol Secure

 Notas y referencias

 Notas

 Enlaces externos
 IETF WebSec Working Group
 W3C Wiki de seguridad web Strict Transport Security
 Security Now 262: Strict Transport Security (en inglés)
 Open Web Application Security Project (OWASP): HSTS description
