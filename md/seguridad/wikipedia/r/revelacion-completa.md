---
type: Artículo de enciclopedia
title: Revelación completa
description: "La estrategia de revelación completa, revelación total o divulgación masiva (en inglés full disclosure) es una política de revelación de vulnerabilidades que consiste en revelar a toda la comunidad (divulgación masiva) …"
resource: https://es.wikipedia.org/wiki/Revelación_completa
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Revelación_completa"}
license: CC BY-SA 4.0
id: eswiki-Revelación_completa
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Revelación completa

La estrategia de **revelación completa**, **revelación total** o **divulgación masiva** (en inglés *full disclosure*) es una política de revelación de vulnerabilidades que consiste en revelar a **toda** la comunidad (divulgación masiva) **toda** la información disponible sobre un problema de seguridad en cuanto este es conocido. Por ejemplo se puede dar información de como se encontró el fallo, qué sistemas son vulnerables, como explotar la seguridad o como protegerse frente al fallo. Se revelan todo tipo de detalles sobre el fallo y esta información tan detallada puede ser usada por hackers malintencionados para desarrollar exploits que permitan aprovechar la vulnerabilidad a cualquiera que lo utilice, aunque no entiendan el funcionamiento del mismo (script kiddies).

Este tipo de políticas es tradicionalmente defendida por hackers y por proveedores de software de código abierto

 Origen
La primera política de revelación de vulnerabilidades que se usó fue la mantener en secreto la información sobre las mismas (no revelación). Algunos investigadores bienintencionados se ponían en comunicación con las empresas proveedoras para que arreglaran los problemas. Sin embargo éstas, confiando en que el secreto se mantendría, tardaban mucho en arreglar los problemas, ignoraban tales peticiones o incluso, considerando que revelar la vulnerabilidad era ilegal, amenazaban a los investigadores con acciones legales si revelaban información. Por otro lado las organizaciones que se instauraron para actuar como intermediarios, como el CERT/CC, tardaban mucho tiempo en verificar las vulnerabilidades antes de mandárselas al proveedor y en publicar los detalles cuando las empresas proveedoras finalmente arreglaban el fallo. Todo esto provocaba un proceso muy poco efectivo en el que los usuarios permanecían vulnerables durante mucho tiempo.

Poco a poco los investigadores se animaron a anunciar las vulnerabilidades existentes, sin publicar los detalles de los mismos. Sin embargo, las empresas proveedoras hacían caso omiso de las mismas argumentando que las vulnerabilidades eran 'teóricas' y negaban que pudieran ser utilizadas de forma práctica. Basándose en estos argumentos las empresas proveedoras seguían ignorando las vulnerabilidades y amenazaban a los investigadores con acciones legales. Cuando algún atacante construía algún exploit y atacaba los sistemas entonces la empresa proveedora generaba rápidamente un parche, pedía disculpas por el fallo y se lamentaba de las acciones de personas maliciosas sin hacer en ningún momento ningún tipo de autocrítica.

Finalmente, a principios de la década de los noventa, empiezan a aparecer listas de correo como bugtraq que ofrecen un foro abierto para discutir y divulgar vulnerabilidades de forma total. Esta lista de correo cambió el panorama: Todos los actores (ej.: administradores de seguridad, hackers maliciosos, proveedores de software) tenían toda la información de forma simultánea. Esto hace que los riesgos y problemas de seguridad se multipliquen lo cual provoca a su vez una importante atención mediática. Por otro lado la reputación de los fabricantes de sistemas de información cae de forma importante y la reputación de ciertos investigadores de agujero de seguridad crece.

 Ventajas
Ventajas de este tipo de política de revelación de vulnerabilidades:
Permite que todos los usuarios tengan información, tan pronto como sea posible, sobre las vulnerabilidades de sus sistemas para que así pueda protegerse paliando o desabilitando dichos agujeros antes de cualquier exploit pueda aprovecharlo.
Motiva a los proveedores de software a que rápidamente pongan solución a dichas vulnerabilidades y así los usuarios puedan rápidamente arreglar sus sistemas. A los proveedores de sistemas de información les perjudica mucho este tipo de políticas porque convierte a las vulnerabilidades de seguridad en problemas acuciantes que tienen que resolver de forma rápida (para evitar que la vulnerabilidad sea masivamente aprovechada), que les pueden producir importantes pérdidas de clientes (que se pueden sentir inseguros), de reputación (les dificulta captar clientes nuevos) y les obliga a invertir importantes cantidades de recursos (dinero) en solucionarlos
El descubridor de la vulnerabilidad obtiene reputación inmediatamente, sin que pueda haber nadie que le robe el descubrimiento. Por esta razón es la más atractiva para los investigadores de seguridad porque los incentiva claramente.

 Inconvenientes
Inconvenientes de este tipo de política de revelación de vulnerabilidades:
Expone una vulnerabilidad sin consultar antes al proveedor y por tanto este no puede desarrollar un parche a esa vulnerabilidad antes de que esta sea publicada. Los atacantes y el proveedor tienen el mismo punto de partida (salvo que tuvieran información 'secreta anterior') unos para aprovechar el fallo y el otro para solventar el problema.
Se argumenta que este tipo de prácticas incrementa el riesgo de que se produzcan ataques con éxito ya que los usuarios no son expertos en seguridad y no siguen diariamente multitud de boletines e informes de seguridad.
Liberar un parche adecuado puede tomar bastante más tiempo que el desarrollo de un exploit que aproveche cierta vulnerabilidad publicada. Por eso a vece se dice que con este tipo de prácticas se pone en ventaja a los atacantes
Por estas razón, para proteger al usuario, a veces no se considera adecuado una política de revelación total salvo para casos particulares como:
Proveedores de software que no hacen caso a informaciones privadas dada sobre la seguridad de sus productos
Vulnerabilidades ampliamente conocidas en comunidades hacker.

 Ejemplos
Ejemplos de foros que actualmente practican este tipo de política de revelación:
Lista de correo Bugtraq en SecurityFocus.
Lista de correo full disclosure en seclists.org.
Security Tube, sitio similar a YouTube pero con información sobre vulnerabilidades.

 Referencias

 Bibliografía
Andrew Cencini et ali., "Software Vulnerabilities: Full-, Responsible-, and Non-Disclosure". Diciembre 2005.
Stephen A. Sheperd, "Vulnerability Disclosure. How do we define Responsible Disclosure?" SANS Institute. Abril de 2003.
Bruce Schneier, "Debating Full Disclosure". Enero de 2007.
