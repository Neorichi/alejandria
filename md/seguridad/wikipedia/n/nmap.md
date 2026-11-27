---
type: Artículo de enciclopedia
title: Nmap
description: "Nmap (Network Mapper) es un programa de código abierto que sirve para efectuar rastreo de puertos escrito originalmente por Gordon Lyon (más conocido por su alias Fyodor Vaskovich) y cuyo desarrollo se encuentra hoy a …"
resource: https://es.wikipedia.org/wiki/Nmap
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Nmap"}
license: CC BY-SA 4.0
id: eswiki-Nmap
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Nmap

- **Nombre:** Nmap Security Scanner
- **Desarrollador:** Gordon Lyon
- **Última versión:** 7.993
- **Sistema operativo:** Multiplataforma
- **Género:** Seguridad informática, administración de redes
- **Licencia:** Licencia pública GNU

**Nmap** (**Network Mapper**) es un programa de código abierto que sirve para efectuar rastreo de puertos escrito originalmente por Gordon Lyon (más conocido por su alias *Fyodor Vaskovich*)  y cuyo desarrollo se encuentra hoy a cargo de una comunidad. Fue creado originalmente para Linux aunque actualmente es multiplataforma. Se usa para evaluar la seguridad de sistemas informáticos, así como para descubrir servicios o servidores en una red informática, para ello Nmap envía unos paquetes definidos a otros equipos y analiza sus respuestas.

Este software posee varias funciones para sondear redes de computadores, incluyendo detección de equipos, servicios y sistemas operativos. Estas funciones son extensibles mediante el uso de scripts para proveer servicios de detección avanzados, detección de vulnerabilidades y otras aplicaciones. Además, durante un escaneo, es capaz de adaptarse a las condiciones de la red incluyendo latencia y congestión de la misma.

 Características
 Descubrimiento de servidores: Identifica computadoras en una red, por ejemplo listando aquellas que responden ping.
 Identifica puertos abiertos en una computadora objetivo.
 Determina qué servicios está ejecutando la misma.
 Determina qué sistema operativo y versión utiliza dicha computadora, (esta técnica es también conocida como *fingerprinting*).
 Obtiene algunas características del hardware de red de la máquina objeto de la prueba.

 Aplicaciones típicas
Ha llegado a ser una de las herramientas imprescindibles para todo administrador de sistema, y es usado para pruebas de penetración y tareas de seguridad informática en general.

Como muchas herramientas usadas en el campo de la seguridad informática, es también una herramienta muy utilizada para hacking.

Los administradores de sistema pueden utilizarlo para verificar la presencia de posibles aplicaciones no autorizadas ejecutándose en el servidor, así como los crackers pueden usarlo para descubrir objetivos potenciales.

Nmap permite hacer el inventario y el mantenimiento del inventario de computadores de una red. Se puede usar entonces para auditar la seguridad de una red, mediante la identificación de todo nuevo servidor que se conecte:

Nmap es a menudo confundido con herramientas para verificación de vulnerabilidades como Nessus. Nmap es difícilmente detectable, ha sido creado para evadir los Sistema de detección de intrusos (IDS) e interfiere lo menos posible con las operaciones normales de las redes y de las computadoras que son analizadas.

 Entornos de trabajo
Nmap puede funcionar en sistemas operativos basados en Unix (GNU/Linux, Solaris, BSD y Mac OS X), y también en otros Sistemas Operativos como Microsoft Windows y AmigaOS.

 Interfaces gráficas
La interfaz usuario oficial es *nmapfe*, escrita originalmente por Zach Smith, y Nmap lo integra desde la versión 2.2.

Existen otras interfaces basadas en navegadores Web.  Algunos ejemplos son **LOCALSCAN**, **nmap-web**, y **Nmap-CGI**.

**NmapW** es una interfaz sobre Microsoft Windows escrita por Syhunt. **NmapWin** es otra interfaz para Windows. Sin embargo, no ha sido actualizada desde la versión 1.4.0 lanzada en junio de 2003.

Una plataforma completa Nmap con capacidades para funcionar sobre distintos OS se encuentra en UMIT. Su autor es Adriano Monteiro Marques. **Zenmap** es la interfaz oficial para sistemas operativos GNU/Linux, Windows, Mac OS X, etc.

 Historia
Nmap apareció en septiembre de 1997, en un artículo de la revista Phrack Magazine. El código fuente venía incluido.

Otros desarrollos incluyeron mejores algoritmos para determinar qué servicios estaban funcionando, reescritura de código de C a C++, se agregaron tipos de scan adicionales y nuevos protocolos como IPv6.

Nmap 3.5 apareció en febrero de 2004, y la versión 4.0 en enero de 2006, con cientos de mejoras. Los cambios de cada versión se pueden encontrar en el listado de cambios de Nmap.

 Controversia

De manera análoga a la mayoría de herramientas utilizadas en seguridad informática, Nmap puede usarse para bien o para mal.

 Puede usarse solo o para preparar otro ataque, con otra herramienta de intrusión.
 Pero los mismos administradores de sistemas lo utilizan para buscar fallas en sus propias redes, o bien para detectar computadoras que no cumplen con los requisitos mínimos de seguridad de la organización, nótese que Nmap por sí solo sólo dará una indicación básica de la vulnerabilidad de una computadora, y que normalmente es usado en conjunto con otras herramientas y tests.

Nmap es a menudo confundido con herramientas de investigación de vulnerabilidad como Nessus, las cuales van más lejos en su exploración de sus objetivos.

 Cultura Popular
 Nmap ha sido también usado en el film *The Matrix reloaded* por el personaje Trinity para penetrar en el sistema de la central eléctrica, mediante la explotación de vulnerabilidades en el servidor SSH y en el Control de redundancia cíclica, (descubiertas en el 2001). La interfaz gráfica de Nmap en la película suscitó el interés de las discusiones en Internet, y fue comentado como una aparición bastante realista de las herramientas de hacking.  En esas discusiones, algunos piensan que el personaje Trinity utilizó el ataque Control de redundancia cíclica (descubierto en 2001) para obtener el acceso, luego de que Nmap revelara la existencia de un servicio SSH.

 Nmap y NmapFE fueron también usados en The Listening, una película de 2006 sobre un exfuncionario de la NSA estadounidense, que deserta y organiza una estación de contraespionaje en los Alpes italianos.

 Partes del código fuente de Nmap pueden verse en la película *Battle Royale*.

 Imágenes extraídas de películas y otras alusiones a Nmap pueden verse en la página "Nmap in the News" del sitio web oficial de Nmap.

 Véase también

 Escáner de puertos explica los conceptos básicos y una lista de otras herramientas para el rastreo de puertos TCP

 Referencias

 Enlaces externos

 Documentación oficial de Nmap en español
