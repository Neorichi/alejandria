---
type: Artículo de enciclopedia
title: Metasploit
description: "Metasploit es un proyecto de código abierto para la seguridad informática, que proporciona información acerca de vulnerabilidades de seguridad y ayuda en tests de penetración \"Pentesting\" y el desarrollo de firmas para …"
resource: https://es.wikipedia.org/wiki/Metasploit
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Metasploit"}
license: CC BY-SA 4.0
id: eswiki-Metasploit
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Metasploit

- **Nombre:** Metasploit
- **Sistema operativo:** multiplataforma
- **Género:** Seguridad
- **Última versión:** 6.4.133
- **Licencia:** Licencia BSD de tres cláusulas

**Metasploit** es un proyecto de código abierto para la seguridad informática, que proporciona información acerca de vulnerabilidades de seguridad y ayuda en tests de penetración "**Pentesting**" y el desarrollo de firmas para sistemas de detección de intrusos.

Su subproyecto más conocido es el **Metasploit Framework**, una herramienta para desarrollar y ejecutar *exploits* contra una máquina remota. Otros subproyectos importantes son las bases de datos de *opcodes* (códigos de operación), un archivo de *shellcodes*, e investigación sobre seguridad. Inicialmente fue creado utilizando el lenguaje de programación de *scripting* Perl  aunque actualmente el Metasploit Framework ha sido escrito de nuevo completamente en el lenguaje Ruby.

 Historia
Metasploit fue creado por H.D Moore en el 2003, como una herramienta de red portátil usando el lenguaje Perl. El 21 de octubre de 2009, el Proyecto Metasploit anunció que había sido adquirida por Rapid7, una empresa de seguridad que ofrece soluciones unificadas de gestión de vulnerabilidades.

Al igual que los productos de la competencia, como Core Security Technologies y Core Impacto, Metasploit se puede utilizar para probar la vulnerabilidad de los sistemas informáticos o entrar en sistemas remotos. Al igual que muchas herramientas de seguridad informática, Metasploit se puede utilizar tanto para actividades legítimas y autorizadas como para actividades ilícitas. Desde la adquisición de Metasploit Framework, Rapid7 ha añadido dos Open source "Código abierto" llamados Metasploit Express y Metasploit Pro.

Metasploit 3.0 comenzó a incluir herramientas de fuzzing, utilizadas para descubrir las vulnerabilidades del software, en lugar de sólo explotar bugs conocidos. Metasploit 4.0 fue lanzado en agosto de 2011.

 Marco/Sistema Metasploit
Los pasos básicos para la explotación de un sistema que utiliza el Sistema incluyen:
 La selección y configuración de un código el cual se va a* explotar *. El cual entra al sistema objetivo, mediante el aprovechamiento de una de bugs; Existen cerca de 900 exploits incluidos para Windows, Unix / Linux y Mac OS X;
 Opción para comprobar si el sistema destino es susceptible a los bugs elegidos.
 La técnica para codificar el sistema de prevención de intrusiones (IPS) e ignorar la carga útil codificada;
 Visualización a la hora de ejecutar el exploit.

Metasploit se ejecuta en Unix (incluyendo Linux y Mac OS X) y en Windows. El Sistema Metasploit se puede extender y es capaz utilizar complementos en varios idiomas.

Para elegir un exploit y la carga útil, se necesita un poco de información sobre el sistema objetivo, como la versión del sistema operativo y los servicios de red instalados. Esta información puede ser obtenida con el escaneo de puertos y "OS fingerprinting", puedes obtener esta información con herramientas como Nmap, NeXpose o Nessus, estos programas, pueden detectar vulnerabilidades del sistema de destino. Metasploit puede importar los datos de la exploración de vulnerabilidades y comparar las vulnerabilidades identificadas.

 Interfaces de Metasploit
Hay varias interfaces para Metasploit disponibles. Las más populares son mantenidas por Rapid7 y Estratégico Ciber LLC

 Edición Metasploit
La versión gratuita. Contiene una interfaz de línea de comandos, la importación de terceros, la explotación manual y fuerza bruta.

 Edición Community Metasploit
En octubre de 2011, Rapid7 liberó Metasploit Community Edition, una interfaz de usuario gratuita basada en la web para Metasploit. Metasploit community incluye, detección de redes, navegación por módulo y la explotación manual.

 Metasploit express
En abril de 2010, Rapid7 liberó Metasploit Express, una edición comercial de código abierto, para los equipos de seguridad que necesitan verificar vulnerabilidades. Ofrece una interfaz gráfica de usuario, integra nmap para el descubrimiento, y añade fuerza bruta inteligente,  así como la recopilación de pruebas automatizado .

 Metasploit Pro
En octubre de 2010, Rapid7 añadió Metasploit Pro, de código abierto para pruebas de penetración. Metasploit Pro incluye todas las características de Metasploit Express y añade la exploración y explotación de aplicaciones web.

 Armitage
**Armitage** es una interfaz gráfica para ciberataques del Proyecto Metasploit, visualiza objetivos y recomienda métodos de ataque. Es una herramienta para ingenieros en seguridad web y es de código abierto. Destaca por sus contribuciones a la colaboración del equipo rojo, permitiendo sesiones compartidas, datos y comunicación a través de una única instancia Metasploit Es de código abierto y está desarrollado por Raphael Mudge.

**Cobalt Strike** es una versión de pago que mejora a Armitage, añade sus propias capacidades, y que además de aprovechar las capacidades de Metasploit, permite usar otras herramientas como Mimikatz.

 Cargas útiles
Metasploit ofrece muchos tipos de cargas útiles, incluyendo:
 * 'Shell de comandos' * permite a los usuarios ejecutar scripts de cobro o ejecutar comandos arbitrarios.
 * 'Meterpreter' * permite a los usuarios controlar la pantalla de un dispositivo mediante VNC y navegar, cargar y descargar archivos.
 * 'Cargas dinámicas' * permite a los usuarios evadir las defensas antivirus mediante la generación de cargas únicas.

Lista de los desarrolladores originales:
 H. D. Moore (fundador y arquitecto jefe)
 Matt Miller (software) | Matt Miller (desarrollador del núcleo 2004-2008)
 Spoonm (desarrollador del núcleo 2003 hasta 2008)

 Referencias

 Enlaces externos

 Licencia BSD tres cláusulas Metasploit Repository COPYING file.
 Rapid7 LLC Empresa dueña del Proyecto Metasploit
 Lugar de descarga
