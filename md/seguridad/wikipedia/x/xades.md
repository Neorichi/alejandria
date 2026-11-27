---
type: Artículo de enciclopedia
title: Xades
description: XAdES sigla en inglés de XML Advanced Electronic Signatures (Firma electrónica avanzada XML) es un conjunto de extensiones a las recomendaciones XML-DSig haciéndolas adecuadas para la firma electrónica avanzada.
resource: https://es.wikipedia.org/wiki/Xades
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Xades"}
license: CC BY-SA 4.0
id: eswiki-Xades
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Xades

**XAdES** sigla en inglés de ***X**ML **Ad**vanced **E**lectronic **S**ignatures* (Firma electrónica avanzada XML) es un conjunto de extensiones a las recomendaciones XML-DSig haciéndolas adecuadas para la firma electrónica avanzada.

 Descripción
Mientras que XML-DSig es un entorno general para firmar digitalmente documentos, XAdES especifica perfiles precisos de XML-DSig para ser usados con **firma electrónica reconocida** con el sentido de la directiva 1999/93/EC de la Unión Europea. Un beneficio importante de XAdES es que los documentos firmados electrónicamente pueden seguir siendo válidos durante largos períodos, incluso en el caso de que los algoritmos criptográficos subyacentes hayan sido rotos.

 Perfiles
XAdES define seis perfiles (formas) según el nivel de protección ofrecido. Cada perfil incluye y extiende al previo:

 **XAdES-BES**, forma básica que simplemente cumple los requisitos legales de la Directiva para firma electrónica avanzada,
 **XAdES-EPES**, forma básica a la que se le ha añadido información sobre la política de firma,
 **XAdES-T** (timestamp), añade un campo de sellado de tiempo para proteger contra el repudio,
 **XAdES-C** (complete), añade referencias a datos de verificación (certificados y listas de revocación) a los documentos firmados para permitir verificación y validación off-line en el futuro (pero no almacena los datos en sí mismos),
 **XAdES-X** (extended), añade sellos de tiempo a las referencias introducidas por XAdES-C para evitar que pueda verse comprometida en el futuro una cadena de certificados,
 **XAdES-X-L** (extended long-term), añade los propios certificados y listas de revocación a los documentos firmados para permitir la verificación en el futuro incluso si las fuentes originales (de consulta de certificados o de las listas de revocación) no estuvieran ya disponibles,
 **XAdES-A** (archivado), añade la posibilidad de timestamping periódico (por ej. cada año) de documentos archivados para prevenir que puedan ser comprometidos debido a la debilidad de la firma durante un periodo largo de almacenamiento.

 Véase también
 European Telecommunications Standards Institute (ETSI)
 Firma XML
 Sellado de tiempo

 Enlaces externos
 W3C XAdES versión 1.1.1 de 2003
 ETSI TS 101 903 XAdES versión 1.1.1 de 12-02-2002
 ETSI TS 101 903 XAdES versión 1.2.2 de 02-04-2004
 ETSI TS 101 903 XAdES versión 1.3.2 de 07-03-2006
 ETSI TS 101 903 XAdES versión 1.4.1 de 15-06-2009
 ETSI TS 101 903 V1.2.2 Especificación Técnica, XSD y DTD
 ETSI TS 101 903 V1.3.2 XSD y DTD
 ETSI TS 101 903 V1.4.1 XSD
