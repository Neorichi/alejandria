---
type: Artículo de enciclopedia
title: PHP2Shell
description: CVE-2026-109618 y CVE-2026-109619 son dos vulnerabilidades de seguridad en el lenguaje de programación PHP que permiten la ejecución remota de código y que se conocen conjuntamente como PHP2Shell.
resource: https://es.wikipedia.org/wiki/PHP2Shell
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/PHP2Shell"}
license: CC BY-SA 4.0
id: eswiki-PHP2Shell
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# PHP2Shell

- **Nombre:** PHP2Shell
- **Cve:** CVE-2026-109618
- **Cvss:** 9,2 (CVSS v4.0)
- **Fecha de revelación:** 20 de octubre de 2026
- **Parchado:** 21 de octubre de 2026
- **Descubridor:** OpenAI Wiz Calif
- **Software afectado:** PHP (versiones 5.4 a 8)

**CVE-2026-109618** y **CVE-2026-109619** son dos vulnerabilidades de seguridad en el lenguaje de programación PHP que permiten la ejecución remota de código y que se conocen conjuntamente como **PHP2Shell**. Su existencia se anunció públicamente el 20 de octubre de 2026.Se publicaron parches de emergencia y detalles acerca de las vulnerabilidades ocurridas al día siguiente del incidente.

 Descubrimiento

Las vulnerabilidades fueron descubiertas de manera independiente por la empresa de seguridad informática Calif, con sede en California, como parte del proyecto «Patch the Planet» de OpenAI, y por la empresa israeloestadounidense de seguridad en la nube Wiz; según ésta, las vulnerabilidades afectan a versiones de PHP desde la 5.4 hasta la 8.

Los desarrolladores de PHP asignaron a las vulnerabilidades una puntuación de 9,2 sobre 10, correspondiente a una gravedad crítica, según la versión 4.0 del Sistema de Puntuación de Vulnerabilidades Comunes (CVSS). Por su parte, la empresa de seguridad informática watchTowr les asignó la puntuación máxima de 10,0.

 Parches de seguridad

Los responsables del mantenimiento de PHP publicaron versiones corregidas de PHP 8.2, 8.3, 8.4 y 8.5. También se publicaron parches para el código fuente de las versiones 7.4, 8.0 y 8.1, aunque no se distribuyeron archivos binarios oficiales actualizados para estas versiones, debido a que habían alcanzado el final de su ciclo de vida y ya no contaban con soporte oficial.

Ambas vulnerabilidades se divulgaron mediante avisos de seguridad en GitHub el 21 de octubre a las 13:34 UTC, 26 minutos antes de la hora anunciada para la publicación de las correcciones. El sitio web de PHP se actualizó poco después.

Los responsables de PHP anunciaron anticipadamente la actualización, después de que se filtrara información sobre las vulnerabilidades en los foros de Hacker News y de que la cuenta de la empresa de ciberseguridad watchTowr Labs en X confirmara su existencia. El aviso anticipado publicado en PHP.net instó a los usuarios a prepararse y actualizar sus sistemas tan pronto como estuvieran disponibles los parches.

La empresa de seguridad informática Sansec anticipó que podrían producirse ataques masivos durante los primeros 15 minutos posteriores a la publicación de las correcciones. Antes de que finalizara el período de embargo informativo, comenzaron a circular por Internet pruebas de concepto (PoC), análisis técnicos y medidas de mitigación parciales.

Cloudflare informó de indicios de explotación temprana de las vulnerabilidades antes de la publicación oficial de los parches y desplegó reglas temporales para su cortafuegos de aplicaciones web (WAF), como medida provisional para intentar mitigar los ataques.

 Impacto

Aproximadamente el 79 % de los sitios web utilizan PHP o su sistema esta basado en él, por lo que las vulnerabilidades tenían el potencial de provocar consecuencias generalizadas.

Tras las recomendaciones del equipo de respuesta a emergencias informáticas de la Unión Europea (CERT-EU) y del Centro Nacional de Ciberseguridad del Reino Unido, numerosas organizaciones europeas desconectaron sus sitios web como medida preventiva mientras esperaban la publicación de los parches. Entre los servicios afectados estuvieron el portal gubernamental Overheid.nl de los Países Bajos, la plataforma nacional de comunicación escolar de Dinamarca, todos los servicios web gubernamentales de acceso público de Finlandia y sitios web de administraciones locales de Francia.

La Fundación Wikimedia desconectó temporalmente numerosos servicios auxiliares, mientras que los sitios de foros 4chan y Something Awful también quedaron fuera de servicio.

 Referencias

 Enlaces externos

 Anuncio oficial del proyecto PHP
