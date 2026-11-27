---
type: Artículo de enciclopedia
title: Web application firewall
description: "Un firewall de aplicaciones web (WAF) es un tipo de firewall que supervisa, filtra o bloquea el tráfico HTTP hacia y desde una aplicación web. Se diferencia de un firewall normal en que puede filtrar el contenido de …"
resource: https://es.wikipedia.org/wiki/Web_application_firewall
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Web_application_firewall"}
license: CC BY-SA 4.0
id: eswiki-Web_application_firewall
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Web application firewall

Un **firewall de aplicaciones web (WAF)** es un tipo de firewall que supervisa, filtra o bloquea el tráfico HTTP hacia y desde una aplicación web. Se diferencia de un firewall normal en que puede filtrar el contenido de aplicaciones web específicas, mientras que un firewall de red protege el tráfico entre los servidores. Al inspeccionar el tráfico HTTP un WAF protege a las aplicaciones web contra ataques como los de inyección SQL, XSS y falsificación de petición de sitios cruzados (CSRF).

 Historia
Los firewalls de aplicaciones, que controlan la entrada, la salida y el acceso desde aplicaciones o servicios, fueron desarrollados por primera vez a principios de la década de 1990 por Gene Spafford, Bill Cheswick y Marcus Ranum.  Este producto, comercializado por DEC, era básicamente un firewall de red, pero podía manejar datos de algunas aplicaciones (como FTP o Rsh). En los siguientes años otros investigadores desarrollaron ampliamente estos productos con el objetivo de proporcionar un software de firewall estable para que otros pudieran basarse en ellos, estableciendo los estándares para la industria en este campo.

Los firewalls de aplicaciones web dedicados llegaron al mercado más adelante en la misma década, cuando los ataques contra servidores web comenzaron a ser mucho más notorios.

La primera compañía en ofrecer un firewall de aplicaciones web dedicado fue Perfecto Technologies con su producto AppShield.  El AppShield estaba dirigido al mercado del comercio electrónico y protegía contra ataques basados en la introducción de caracteres ilegales en las páginas web. La compañía cambió su nombre a Sanctum, e hizo un listado con las diez mejores técnicas de ataque a aplicaciones web, creando las bases para el mercado WAF:

 Manipulación de campos hidden
 Envenenamiento de cookies (cookie poisoning)
 Alteración de parámetros
 Desbordamiento de búfer
 Cross-Site Scripting (XSS)
 Puertas traseras u opciones de depuración
 Stealth commanding
 Navegación forzada
 Configuraciones erróneas de terceros
 Agujeros de seguridad conocidos

En 2002 se creó el proyecto de código abierto ModSecurity para hacer la tecnología WAF más accesible y resolver los obstáculos dentro de la industria, como casos de negocios, barreras de costos y los conjuntos de reglas particulares de cada empresa. ModSecurity creó un conjunto de reglas básicas para proteger las aplicaciones web, basado en las vulnerabilidades detectadas por el OASIS Web Application Security Technical Committee’s (WAS TC). En 2003, este trabajo fue ampliado y estandarizado con la creación de la Lista Top 10 del Open Web Application Security Project’s (OWASP). OWASP publica con cierta regularidad una lista con los 10 riesgos de seguridad más críticos de las aplicaciones web. Esta lista se convertiría en la referencia de la industria para muchos temas de seguridad en la web.

Desde entonces, el mercado ha seguido creciendo y evolucionando, afectando a la creciente industria del comercio electrónico con el aumento del fraude con tarjetas de crédito. Con el desarrollo del Payment Card Industry Data Security Standard (PCI DSS), un estándar para que las organizaciones incrementen los controles sobre los datos de los titulares de tarjetas, la seguridad está más regulada y se ha ampliado el interés en estos temas. El tamaño del mercado de WAF superó los 200 millones de dólares en 2010 y se espera que supere los 5000 millones en 2022.

 Descripción
Un firewall de aplicaciones web se instala por delante de las aplicaciones web y analiza el tráfico bidireccional que usa el protocolo HTTP (web), detectando y bloqueando tráfico malicioso. El OWASP ofrece una definición técnica amplia para un WAF. Se define un firewall de web como “una solución de seguridad a nivel de aplicación que, desde un punto de vista técnico, no depende de la propia aplicación.” Un WAF aplica un conjunto de reglas en las conversaciones HTTP para proteger a las aplicaciones de ataques comunes como son cross-site scripting (XSS) e inyección de SQL. Mientras que los proxies protegen a clientes, los WAFs protegen a los servidores. Usualmente los WAFs se despliegan para proteger una aplicación web específica o un conjunto de aplicaciones web.

Según el suplemento de información PCI DSS requisito 6.6, un WAF se define como “un punto de refuerzo de las políticas de seguridad colocado entre una aplicación web y el cliente final. Esta funcionalidad puede implementarse en software o hardware, ejecutándose en un dispositivo específico o en un servidor típico con un sistema operativo común. Puede ser un dispositivo independiente o integrado en otros componentes de red.” Es decir, un WAF puede ser un dispositivo físico o virtual que evita que elementos externos puedan explotar las vulnerabilidades que puedan tener las aplicaciones web. Estas vulnerabilidades pueden deberse al uso de tecnología antigua (legacy) o a una programación que no las ha tenido en cuenta por un diseño incorrecto. Un WAF puede paliar estas insuficiencias mediante el uso de conjuntos de reglas de configuración, llamadas también políticas (“policies”).

Se pueden descubrir vulnerabilidades previamente desconocidas con pruebas de penetración o con un escáner de vulnerabilidades. Un escáner de vulnerabilidad de aplicaciones web, también conocido como escáner de seguridad de aplicaciones web, se define en SAMATE NIST 500-269 como “un programa automatizado que examina las aplicaciones web en busca de posibles vulnerabilidades de seguridad. También busca errores de codificación de software.” La resolución de vulnerabilidades generalmente se denomina reparación. Aunque posteriormente se puedan hacer correcciones en el código de la aplicación, se necesita una solución a corto plazo. En estas situaciones se crea una regla o política personalizada (“custom policy”) para paliar esa vulnerabilidad concreta, que soluciona el problema de forma temporal pero inmediata (conocida como parche virtual).

Un WAF no es una solución de seguridad definitiva. Sin embargo es una solución que debe ser utilizada junto con otras soluciones de seguridad como firewalls de red y sistemas de prevención de intrusos, para proporcionar una estrategia de defensa holística.

Los WAF normalmente siguen un modelo de seguridad positivo, un modelo de seguridad negativo o una combinación de los dos, según el SANS Institute. Un WAF utiliza una combinación de lógica basada en reglas, análisis sintáctico y firmas para detectar y prevenir ataques como los de cross-site scripting o inyección de SQL. El OWASP publica una lista de los diez principales riesgos de seguridad de las aplicaciones web. Todos los WAF comerciales ofrecen al menos protección contra estos diez riesgos. También hay opciones no comerciales, como la solución de código abierto ModSecurity. Un motor WAF por sí solo no es suficiente para ofrecer protección adecuada, por lo que OWASP, junto con el equipo Spiderlabs de Trustwave, ayudan a organizar y mantener un conjunto de reglas básicas que pueden ser utilizadas por el motor WAF de ModSecurity, disponibles a través de GitHub.

 Opciones de implementación
Los WAF se implementan de tres maneras diferentes. Según NSS Labs, las opciones de implementación son: puente transparente (transparent bridge), proxy inverso transparente (transparent reverse proxy) y proxy inverso (reverse proxy). El término "transparente" se refiere al hecho de que el tráfico HTTP se envía directamente a la aplicación web. Por eso el WAF es transparente entre el cliente y el servidor. En cambio, con el proxy inverso el WAF actúa como un proxy y el tráfico del cliente se envía directamente al WAF, que a su vez envía el tráfico ya filtrado a las aplicaciones web. Esto puede proporcionar otros beneficios, como el enmascaramiento de IP, pero también tiene desventajas, como un menor rendimiento por el incremento de latencia. Para minimizar los efectos del incremento de latencia, algunos WAF configurados como proxy inverso añaden servicios adicionales como cacheado de contenidos estáticos, mejoras en la compresión de datos y enrutamiento geolocalizado.

 Vendedores comerciales
Muchos WAF comerciales tienen características similares, pero las principales diferencias están relacionadas normalmente con las interfaces de usuario, opciones de implementación o requisitos para entornos específicos.

 WAF basado en dispositivo
Es una solución basada en hardware que se instala localmente en la infraestructura de red. Ofrece baja latencia y alto rendimiento, pero requiere mantenimiento físico.
 Barracuda Networks WAF
 Citrix Netscaler Application Firewall
 F5 Big-IP ASM
 Fortinet FortiWeb
 Imperva SecureSphere
 Monitorapp AIWAF
 Penta Security WAPPLES
 Positive Technologies PT Application Firewall
 Radware AppWall
 Sophos XG Firewall

 WAF basado en la nube
Es una solución basada en servicios que se hospeda en una plataforma en la nube. Ofrece escalabilidad y facilidad de uso, pero también depende de la disponibilidad y seguridad del proveedor de la nube. Al disponer de múltiples nodos, puede ofrecer mejor protección contra Ataques de denegación de servicio
 AIONCLOUD
 Akamai Technologies Kona
 Cloudbric
 Cloudflare
 F5 Silverline
 Hukot.net WAF
 Imperva Incapsula
 QingCloud WAF
 Radware
 Sucuri Firewall
 Webscale Cloud Secure
 PowerWAF

 Opciones de código abierto
También hay soluciones de código abierto disponibles para cualquier público.

 ModSecurity
 NAXSI

 Referencias
