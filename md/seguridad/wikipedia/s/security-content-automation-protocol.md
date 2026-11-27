---
type: Artículo de enciclopedia
title: Security Content Automation Protocol
description: "El Security Content Automation Protocol, también conocido por sus siglas SCAP o S'CAP, es un conjunto de especificaciones del NIST para expresar (formatos y nomenclaturas) y manipular información relacionada con la …"
resource: https://es.wikipedia.org/wiki/Security_Content_Automation_Protocol
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Security_Content_Automation_Protocol"}
license: CC BY-SA 4.0
id: eswiki-Security_Content_Automation_Protocol
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Security Content Automation Protocol

El **Security Content Automation Protocol**, también conocido por sus siglas **SCAP** o **S'CAP**, es un conjunto de especificaciones del NIST para expresar (formatos y nomenclaturas) y manipular información relacionada con la seguridad sobre fallos y configuraciones, de una forma estandarizada. De esta forma se permite automatizar, en cierto grado, el chequeo (búsqueda) de vulnerabilidades, evaluar posibles impactos de vulnerabilidades, la gestión de vulnerabilidades, mediciones de seguridad, y evaluación de políticas a adoptar. En definitiva, provee una infraestructura poderosa para la elaboración de análisis e informes sobre vulnerabilidades en los sistemas de información.

Componentes
Las especificaciones incluyen los siguientes componentes:
Common Vulnerabilities and Exposures (siglas CVE): Es una lista de información de seguridad sobre vulnerabilidades con el objetivo de proveer una nomenclatura común para el conocimiento público de este tipo de problemas. Antes de publicar una vulnerabilidad o exposición pasa por ciertas etapas previas por lo que la lista no contiene vulnerabilidades recién descubiertas.
Common Configuration Enumeration (siglas CCE).- Es similar a CVE pero contienen vulnerabilidades de seguridad e incosistencias de interfaces encontradas en configuraciones de sistemas. Provee la información en forma narrativa y normalmente recomienda soluciones.
Common Platform Enumeration (siglas CPE).- Se ocupa de la correcta nomenclatura del software y ofrece una estructura jerárquica. De esta forma se facilita la gestión del nombre del software.
eXtensible Configuration Checklist Description Format (siglas XCCDF).- Es una plantilla XML que facilita la preparación estandarizada de documentos guía de seguridad que presentan vulnerabilidades o asuntos de seguridad sobre el software
Open Vulnerability and Assessment Language  (siglas OVAL).- Es un lenguaje para representar información de configuración, evaluación de los estados de la máquina e informes de resultados de la evaluación.
Common Vulnerability Scoring System  (siglas CVSS).- Es un algoritmo que tiene en cuenta distintos parámetros relativos al software y da una expresión del nivel de seguridad calculado.
Open Checklist Interactive Language (siglas OCIL) (desde versión 1.1).- Es un lenguaje para representar controles que recogen información sobre gente o datos existentes almacenados.
Asset Identification (siglas AI) (desde versión 1.2).- Formato para identificar de forma única activos basados en conocidos identificadores y/o información sobre los activos
Asset Reporting Format (siglas ARF) (desde versión 1.2).- Formato para expresar información sobre activos y las relaciones entre activos e informes.
Common Configuration Scoring System (siglas CCSS) (desde versión 1.2).- Sistema para medir la importancia relativa de un asunto de configuración de la seguridad de un sistema.
Trust Model for Security Automation Data (siglas TMSAD) (desde versión 1.2).- Especificación para usar firmas digitales en un modelo de confianza común aplicado a las espeficaciones del SCAP.

Estas especificaciones las podemos clasificar según el tipo de utilidad que proporcionan en:
**Lenguajes**.- Proveen vocabulario y convenciones para expresarse en el contexto. A este tipo de especificaciones pertenecen: XCCDF, OVAL y OCIL.
**Formato de informes**.- Proveen una serie de construcciones necesarias para expresar la información que gestionan de una forma estandarizada. A este tipo de especificaciones pertenecen: ARF y Asset Identification.
**Enumeraciones**.- Definen una nomenclatura estándar (formato de nombres) y una lista de artículos expresados usando la nomenclatura. A este tipo de especificaciones pertenecen: CPE, CCE y CVE.
**Mediciones y sistemas de puntuación**.- Permiten evaluar características específicas de una vulnerabilidad de seguridad (Ej vulnerabilidades software o deficiente configuración de seguridad) y basándose en estas características generar una puntuación que refleje su importancia relativa. A este tipo de especificaciones pertenece: CVSS y CCSS.
**Integridad**.- Ayudan a preservar la integridad de los contenidos y resultados. A este tipo de especificaciones pertenece TMSAD.

Referencias
Stephen Quinn et ali.,"The Technical Specification for the Security Content Automation Protocol (SCAP): SCAP Version 1.0"
David Waltermire et ali.,"The Technical Specification for the Security Content Automation Protocol (SCAP): SCAP Version 1.2"
George K. Kostopoulos, "Cyberspace and Cybersecurity". CRC Press 2013.
