---
type: Artículo de enciclopedia
title: FOCA Tool
description: "FOCA Tool es una herramienta gratuita de pentesting para los sistemas operativos Windows, utilizada principalmente en la búsqueda de información contenida en metadatos de ficheros y de esta forma obtener datos …"
resource: https://es.wikipedia.org/wiki/FOCA_Tool
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/FOCA_Tool"}
license: CC BY-SA 4.0
id: eswiki-FOCA_Tool
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# FOCA Tool

- **Nombre:** FOCA Tool
- **Última versión:** FOCA Tool open Source
- **Género:** Pruebas de software
- **Lenguaje programación:** .NET
- **Licencia:** Licencia Pública General GNU 3.0
- **Estado:** Versión Final Open Source Liberada

**FOCA Tool** es una herramienta gratuita de pentesting para los sistemas operativos Windows, utilizada principalmente en la búsqueda de información contenida en metadatos de ficheros y de esta forma obtener datos relevantes asociados a una organización o página web. FOCA significa *Fingerprinting Organizations with Collected Archives* por sus iniciales en idioma inglés.

 Historia
El nombre inicial de FOCA era MetaExtractor para Microsoft Office y OOMetaextractor para OpenOffice y fue creada por la empresa Informatica64 (hoy llamada ElevenPaths) en 2007. El origen del nombre siempre fue pensado en alusión al animal foca, el cual es un depredador de pingüinos, mascota de las distribuciones basadas en GNU/Linux. FOCA fue presentada oficialmente en 2010 en la conferencia de seguridad Ekoparty. También se ha mostrado en conferencias de seguridad internacionales como la DEF CON y Rooted En octubre de 2017 se presentó la última versión llamada FOCA OpenSource.

 Características
FOCA permite la extracción y el análisis de metadatos ubicados en un servidor o una página web. Dicha información se obtiene a partir de ficheros tipo Microsoft Office, PDF y SVG entre otros que son localizados utilizando motores de búsqueda como Google, Bing y DuckDuckGo. El análisis por parte de FOCA de dichos metadatos genera un informe con información relevante como configuración de la red, proxy, ficheros de backup, etc. Esta herramienta está programada en .NET y utiliza bases de datos SQL Express. Desde la versión 2.7 ofrece capacidad de enrutar y colocar en cola multihilo para poder analizar un sitio web extenso sin colapsar la capacidad de procesamiento del ordenador donde se ejecuta (esto es llamado *cola de tareas*).

 Funcionalidad
A partir de la información obtenida de los metadatos de los diferentes ficheros, el módulo de descubrimiento de servidores utiliza las siguientes técnicas para realizar un fingerprint del dominio o servidor auditado:

 *Web Search*: búsqueda de nombres de servidores y dominios.
 *DNS Search*: consulta de los hostnames NX, MX y SPF.
 *Resolución IP*: consultas a DNS internos de la organización.
 *PTR Scanning*: localización de servidores en el mismo segmento de red.
 *Bing IP*: búsqueda de servidores partiendo de otras direcciones IP descubiertas.
 *Common Names*: realiza ataques de diccionario DNS.
 También analiza la posible existencia de servidores proxy tipo Squid por medio de revisión del puerto 3128.

En cuanto a la información obtenida de los ficheros descargados retribuye la siguiente información:

 Sistema operativo con el que fueron creados los documentos.
 Modelos de impresoras usadas.
 Fechas de impresión, modificación y creación.
 Versión del software utilizado en su creación.
 Correos electrónicos dentro de los documentos, si hubiera alguno.
 Rutas de ficheros y nombres de autores y nombres de usuarios.

FOCA también permite la instalación y programación de complementos, los complementos oficiales se pueden descargar desde el *FOCA Market*.

 Véase también

 Referencias

 Enlaces externos
 FOCA OpenSource GitHub
FOCA
 OSINT with FOCA 2.6
 PenTestIT FOCA: Fingerprint and organisation with Collected Archiver
 Libro "Pentesting con FOCA",  editorial 0xWord
