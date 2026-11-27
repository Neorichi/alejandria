---
type: Artículo de enciclopedia
title: Custodia electrónica
description: "La custodia electrónica hace referencia a un proceso que procura \"guardar con cuidado y vigilancia\" los documentos electrónicos, tal define el diccionario de la lengua española el término \"custodiar\"."
resource: https://es.wikipedia.org/wiki/Custodia_electrónica
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Custodia_electrónica"}
license: CC BY-SA 4.0
id: eswiki-Custodia_electrónica
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Custodia electrónica

La **custodia electrónica** hace referencia a un proceso que procura "guardar con cuidado y vigilancia" los documentos electrónicos, tal define el diccionario de la lengua española el término "custodiar".

Está intrínsecamente ligado a la preservación digital y al uso de la firma electrónica avanzada, aspectos que derivan de la necesidad de validez a largo plazo de documentos electrónicos.

 Antecedentes y problemática
En la gestión documental del papel, el concepto de archivo y la función del archivero en diferentes ámbitos como por ejemplo en la custodia del protocolo notarial o en el archivo de historias clínicas, están ampliamente reconocidas, pero no así su equivalente electrónico.

Cuando los documentos tienen una consideración legal o determinados requisitos de seguridad, se vuelve necesario ofrecer ciertas garantías sobre los mismos, que permitan a quien lo necesite, tener confianza sobre su autenticidad y su disponibilidad futura.

Ante la aparición de los documentos electrónicos, aunque los objetivos son los mismos, el paradigma cambia y por tanto los mecanismos son muy diferentes. El principal problema viene derivado del uso de la firma digital como mecanismo para garantizar la autenticidad del documento.

La firma digital introduce una cadena de dependencias entre el documento y los elementos utilizados para generar la firma, que hace que si en el futuro alguno de estos elementos utilizados para producir la firma deja de ser válidos o pierde sus garantías, no se pueda validar el documento electrónico en sí sin medidas adicionales.

En papel esto implicaría que una firma manuscrita no se pudiera validar si se pierde el bolígrafo que se utilizó para producirla, algo que nos resultaría absurdo pero que sí ocurre con su equivalente electrónico, ya que la validez del documento electrónico depende entre otros, del tipo de firma, de la vigencia del certificado, de la fortaleza de los algoritmos criptográficos utilizados en el momento de firmar/validar, de la autoridad de certificación que emitió el certificado (si era reconocida en el momento en el que se firmó), de la consideración de dispositivo seguro de creación de firma, de la normativa vigente, ...

Aparte se encuentran otras dificultadas derivadas de que el soporte deja de ser físico, para ser electrónico. Por ejemplo, desaparece entre otros el concepto de original tal y como lo entendemos en papel, ya que una copia electrónica es idéntica a otra (de hecho lo que vemos en pantalla es una copia en memoria de lo que está almacenado). También ocurre en muchos casos que lo que se ve no se corresponde con el contenido real del documento, ya que se disocian formato y datos, por tanto un mismo documento electrónico puede tener distintas formas de representación, algo que no ocurre en papel.

Respecto del control de acceso y trazabilidad, a la hora de controlar el acceso a un documento electrónico, se dan situaciones como el fenómeno de la música por internet (mp3), donde tampoco son válidos los modelos convencionales utilizados en aplicaciones que pivotan sobre un usuario y su perfil, asumiendo que dicho usuario ha hecho login y es conocido por el sistema.

Generalmente el control de acceso pivota en torno al propio documento, ya que este puede ser distribuido a usuarios no conocidos previamente como un objeto digital en un formato estándar (p.e. PDF), sin que tenga por qué existir acceso a una aplicación centralizada como tal para leerlo. Es el propio documento quien puede contener sus políticas de acceso, cuya aplicación puede variar según el contexto y el tiempo (p.e. es un documento confidencial durante n años y público ante determinados sucesos como muerte, fin de un conflicto, etc..).

 Objetivos de la custodia electrónica
Los objetivos son similares a los de cualquier documento en papel que requiera de garantías futuras para que se considere válido en su ámbito de aplicación. Estos suelen ser:
 Garantizar su integridad, que impida cualquier cambio sobre el original
 Garantizar su autenticidad, permitiendo contrastar su origen y ofrecer certeza sobre su autoría
 Garantizar la posibilidad de localización, facilitando las búsquedas y sin depender de relaciones externas entre la referencia y el contenido
 Garantizar el control de acceso
 Garantizar la trazabilidad de los accesos y del ciclo de vida
 Garantizar su preservación a largo plazo, por ejemplo con mecanismos de restauración y mantenimiento de las condiciones ambientales

Los mecanismos tecnológicos para ofrecer estas garantías sobre los documentos (al igual que el papel timbrado o un pasaporte) complementan o apoyan las funciones que ofrece un tercero de confianza, un testigo o un notario, dado que en todo caso se utiliza un soporte documental de un hecho.

 Tecnologías relacionadas

 Integridad y autenticidad
Puede entenderse que la firma electrónica por sí sola es suficiente como tecnología para garantizar la integridad y autenticidad pero solo algunos de los objetivos de la custodia electrónica se consiguen con la firma electróncia.

Es importante destacar que la firma electrónica garantiza disponer de un mecanismo de *verificación*, pero si un documento es alterado la firma electrónica por sí sola no ofrece garantías para reponer el original.

Por eso los sistemas de custodia electrónica introducen mecanismos de tolerancia a fallos que permiten no solo detectar cambios sino recuperarlos. Estos sistemas pueden ir más allá de las tecnologías RAID, dado que pueden actuar de forma distribuida o en la nube, no solo verificando CRCs de sectores de información sino la firma de todo el documento.

 Control de Acceso
La firma electrónica no es un mecanismo de confidencialidad, que si lo es el cifrado por ejemplo usando clave pública y otros mecanismos de control de acceso implementados en la aplicación que gestiona el repositorio o mediante el uso de sistemas de Gestión de derechos digitales.

 Trazabilidad
Para trazar quién ha accedido o los diferentes eventos acontecidos a lo largo del ciclo de vida del documento, es necesario una combinación de firma, junto con un registro del evento y posiblemente un sellado de tiempo. Puede que esta traza se incorpore al documento, al igual que la gestión de cambios de un documento ofimático o sea un registro centralizado asociado al repositorio del documento como ocurre con la gestión de cambios de esta página Wiki. La firma solo deja rastro de quién fue el autor, revisor, etc., si es que alguno de estos firmó el documento y puede incluir información de tiempo sobre el momento de la firma, que no de posteriores accesos, validaciones, etc.

 Localización
La firma electrónica por sí sola no permite localizar un documento y garantizar que la referencia o enlace que se utiliza para identificarlo se corresponde univocamente a dicho documento.

Por tanto los sistemas de custodia electrónica implican más tecnologías como Content Address Storage, que generan un localizador basado en el contenido y por tanto indisociable al mismo (no se depende de una base de datos relacional que puede alterarse sin alterar la firma del documento y por tanto pensar que el contenido al que se hace referencia es otro aunque también esté correctamente firmado).

 Preservación
La garantía de preservación implica generalmente hacer un refirmado periódico con material actualizado en el momento actual, firmando una verificación de una firma pasada. Aunque el estándar XAdES identifica como incorporar este material es necesario un mecanismo activo de preservación que lo realice, considerando políticas de preservación (p.e. frecuencia).

Adicionalmente puede ser necesario garantizar la legibilidad del documento, ya que a muy largo plazo, existen dependencias en los estándares o aplicaciones utilizados para producir el documento que desaparezcan y por tanto convenga también preservar.

 Terminología
Es un término tan reciente como las tecnologías relacionadas y la aparición de los primeros problemas al validar documentos electrónicos generados hace unos años, por eso existen términos similares como Archivo seguro, custodia de documentos electrónicos o custodia de documentos firmados, si bien ya existen múltiples proveedores que ofrecen o incorporan productos y servicios de custodia electrónica.

En este mismo ámbito también se utiliza el término custodia para referirse a la responsabilidad del productor de una firma electrónica sobre los elementos utilizados para producirla, de forma que se garantice el no repudio.

Al referirse a la custodia de evidencias electrónicas, se incide en el concepto de cadena de custodia a la hora de obtener la evidencia y en como se preserva esta como medio de prueba.

El término custodia electrónica también se utiliza en la custodia de valores (finanzas).

Actualmente Google arroja 327.000 resultados para "custodia electrónica".

 Normativa relacionada
 ISO 10181-4:1997. Information technology – Open systems interconnexion– Security framework for open systems: Non repudiation framework.
 ISO 14721:2003. Space data and information transfer systems – Open archival information system – Reference model.
 ISO 15489-1:2001. Information and documentation – Records management – General.
 ISO 20652:2005. Space data and information transfer systems – Open archival information systems – Producer-Archive interface metholody abstract standard.
 ISO 23081. Information and documentation - Records management processes - Metadata for records -- Part 1: Principles
 ISO_27000-series Mejores prácticas recomendadas en Seguridad de la información y requisitos de los sistemas de gestión
 OAI-PMH – The Open Archives Initiative Protocol for Metadata Harvesting. 2002.

 DoD 5015.2 - Design Criteria Standard for Electronic Records Management Software Applications
 ISAD
 NARA
 Dublin Core Metadata
 UK PRO
 ANSI/AIIM/ARMA TR48
 CAN/CGSB-72.34
 BS EN 82045-1:2001
 DLM Forum: MoReq
 REL –Rights Expression Language
 SAML – Security Assertion Language.
 XACML – XML Access Control Markup Language.
 XAdES W3C versión 1.1.1 de 2003 y ETSI TS 101 903 XAdES versión 1.4.1
 UneDocs
 XBRL
 PDF/A

 Referencias
 ADAPT - A Digital Approach to Preservation Technology https://web.archive.org/web/20070921235436/http://narawiki.umiacs.umd.edu/twiki/bin/view/Main/WebHome
 aDORe: a modular, standards-based Digital Object Repository. Herbert Van de Sompel, Jeroen Bekaert, Xiaoming Liu, Luda Balakireva, Thorsten Schwander.
 An Audit Checklist for the Certification of Trusted Digital Repositories.RLG/NARA. 2005.
 Council of European Social Science Data Archives http://www.nsd.uib.no/cessda/
 Data dictionary for preservation metadata. Final report of the PREMIS Working Group. 2005.
 Data Documentation Initiative https://web.archive.org/web/20081207093406/http://www.icpsr.umich.edu/DDI/org/index.html
 Digital Curation Centre (UK) Representation Information Registry
 Digital Preservation Needs and Requirements in RLG Member Institutions. Margaret Hedstrom and Sheon Montgomery. 1998.
 FEDORA – An Architecture for Complex Objects and their Relationships. Carl Lagoze, Sandy Payette, Edwin Shin, Chris Wilper.
 Fedora and the Preservation of University Records Project. 2.1 Ingest Guide. Digital Collections and Archives, Tufts University; Manuscripts & Archives, Yale University. 2006.
 File-based storage of Digital Objects and constituent datastreams: XMLtapes and Internet Archive ARC files. Xiaoming Liu, Lyudmila Balakireva, Patrick Hochstenbach, and Herbert Van de Sompel.
 GDFR – Global Digital Format Registry: http://hul.harvard.edu/gdfr/
 Global Digital Format Registry (GDFR). Stephen L. Abrams. Harvard E-Journal Archive. Submission Information Package (SIP) Specification. 2001.
 Implementing Preservation Repositories For Digital Materials: Current Practice And Emerging Trends In The Cultural Heritage Community. A Report by the PREMIS Working Group. 2004.
 JHOVE – JSTOR/Harvard Object Validation Environment http://hul.harvard.edu/jhove/
 METS – Metadata Encoding and Transmission Protocol. Library of Congress.
 PAWN: A Novel Ingestion Workflow Technology for Digital Preservation. Mike Smorul and Joseph JaJa.
 PRONOM – UK National Archives’ file format registry.
 Representing Digital Assets using MPEG-21 Digital Item Declaration. Jeroen Bekaert, Herbert van de Sompel.
 Requirements for Digital Preservation Systems: A Bottom-Up Approach. David S. H. Rosenthal, Thomas Robertson, Tom Lipkis, Vicky Reich, Seth Morabito.
 Robust Technologies for Automated Ingestion and Long-Term Preservation of Digital Information. Joseph JaJa.
 Scalable, Reliable Marshalling and Organization of Distributed Large Scale Data Onto Enterprise Storage Environments, J. JaJa, M. Smorul, F. McCall, and Y. Wang.
 Trusted Digital Repositories: Attributes and Responsibilities. RLG/OCLC. 2002.
 U.S. National Archives and Records Administration Electronic and Special Media Records Services Division, Accessioning Procedures Handbook. 2000
 Update to the National Digital Infrastructure and Preservation Program. 2003.
 XFDU packaging contribution to an implementation of the OAIS reference model. Arnaud Lucas.

 Aplicaciones
Comercio electrónico
Factura Electr%C3%B3nica
Desmaterialización de documentos
Notificaciones judiciales electrónicas
Voto electrónico
Contratación pública

 Véase también
 Tercero de confianza
 Derecho informático
 Digital preservation http://en.wikipedia.org/wiki/Digital_preservation

 Notas

 Enlaces externos
 ARCE Archivo de Constancias Electrónicas del Ministerio de Industria de España
 Sistema de Custodia en la Junta de Castilla y León
 Sistema de Custodia en la Generalitat de Cataluña
