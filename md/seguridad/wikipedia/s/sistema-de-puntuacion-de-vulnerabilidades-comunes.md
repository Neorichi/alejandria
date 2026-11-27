---
type: Artículo de enciclopedia
title: Sistema de Puntuación de Vulnerabilidades Comunes
description: "El Sistema de Puntuación de Vulnerabilidades Comunes o Common Vulnerability Scoring System (CVSS, por sus siglas en inglés) es un estándar de la industria, libre y abierto, para evaluar la gravedad de las …"
resource: https://es.wikipedia.org/wiki/Sistema_de_Puntuación_de_Vulnerabilidades_Comunes
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sistema_de_Puntuación_de_Vulnerabilidades_Comunes"}
license: CC BY-SA 4.0
id: eswiki-Sistema_de_Puntuación_de_Vulnerabilidades_Comunes
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sistema de Puntuación de Vulnerabilidades Comunes

El **Sistema de Puntuación de Vulnerabilidades Comunes** o *Common Vulnerability Scoring System* (CVSS, por sus siglas en inglés) es un estándar de la industria, libre y abierto, para evaluar la gravedad de las vulnerabilidades en los sistemas informáticos. CVSS intenta asignar puntuaciones de gravedad a las vulnerabilidades, permitiendo a los respondedores priorizar respuestas y recursos según la amenaza. Las puntuaciones se calculan basándose en una fórmula que depende de varios parámetros que aproximan la facilidad y el impacto de un exploit. Las puntuaciones varían de 0 a 10, siendo 10 la más grave. Aunque muchos solo utilizan la puntuación base de CVSS para determinar la gravedad, también existen puntuaciones temporales y ambientales, que consideran la disponibilidad de mitigaciones y cuán extendidos están los sistemas vulnerables dentro de una organización, respectivamente.

La versión actual de CVSS (CVSSv4.0) se lanzó en noviembre de 2023.

 Versión 2.0
La documentación completa de CVSSv2 está disponible en FIRST. A continuación se proporciona un resumen.

 Métricas base

 Vector de Acceso
El vector de acceso (AV) muestra cómo puede ser explotada una vulnerabilidad.

 Complejidad de Acceso
La métrica de complejidad de acceso (AC) describe cuán fácil o difícil es explotar la vulnerabilidad descubierta.

 Autenticación
La métrica de autenticación (Au) describe el número de veces que un atacante debe autenticarse en un objetivo para explotarlo. No incluye, por ejemplo, la autenticación en una red para obtener acceso. Para las vulnerabilidades explotables localmente, este valor solo debe establecerse en Única o Múltiple si se requiere una autenticación adicional después del acceso inicial.

 Métricas de Impacto

 Confidencialidad
La métrica de confidencialidad (C) describe el impacto en la confidencialidad de los datos procesados por el sistema.

 Integridad
La métrica de integridad (I) describe el impacto en la integridad del sistema explotado.

 Disponibilidad
La métrica de disponibilidad (A) describe el impacto en la disponibilidad del sistema objetivo. Los ataques que consumen ancho de banda de red, ciclos de procesador, memoria u otros recursos afectan la disponibilidad de un sistema.

 Versión 4.0
En junio de 2023, se lanzó una vista previa pública de CVSSv4.0, que trajo una serie de mejoras. La versión 4.0 se lanzó oficialmente en noviembre de 2023.

 Adopción
Las versiones de CVSS han sido adoptadas como el método principal para cuantificar la gravedad de las vulnerabilidades por una amplia gama de organizaciones y empresas, incluyendo:

 La Base de Datos Nacional de Vulnerabilidades (NVD).
 La Base de Datos de Vulnerabilidades de Código Abierto (OSVDB).
 El Centro de Coordinación CERT, que en particular utiliza las métricas Base, Temporal y Ambiental de CVSSv2.

 Véase también

 Common Weakness Enumeration (CWE).
 Common Vulnerabilities and Exposures (CVE).

 Referencias
