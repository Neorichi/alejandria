---
type: Artículo de enciclopedia
title: Seguridad XML
description: Especificaciones relacionadas con la seguridad de XML
resource: https://es.wikipedia.org/wiki/Seguridad_XML
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Seguridad_XML"}
license: CC BY-SA 4.0
id: eswiki-Seguridad_XML
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Seguridad XML

Especificaciones relacionadas con la seguridad de XML

Hay pocas especificaciones relacionadas con la seguridad que se desarrollen en W3C por medio de varias compañías asociadas, pensadas para dirigir una serie de necesidades de seguridad de los servicios Web, en concreto para proporcionar un modo estándar de aplicar la seguridad a los documentos de XML y a los mensajes SOAP. Tratar la seguridad de un modo uniforma activaría las implementaciones independientes del protocolo de transporte escogido, que funcionaría a través de intermediarios, inclusive intermediarios SOAP.

 Firma XML

La especificación XML Signature se encuentra en la fase de Recomendación de candidato (una llamada a la industria para implementar la especificación y proporcionarle interacción) y se convertirá en una Recomendación muy pronto. La especificación XML Signature proporciona unas normas sintácticas y de procesamiento para crear y representar firmas digitales. En general, las firmas digitales se pueden aplicar a cualquier contenido digital, incluyendo la propia información de XML. En su arquitectura, las firmas digitales pueden desarrollar el propio contenido o pueden estar eliminadas de su contenido actual y simplemente hacer referencia a éste.

XML Signature especifica los métodos para asociar las claves con la información a la que hacen referencia. Sin embargo, no especifica el modo en que las claves están asociadas a las personas u organizaciones. Lo cual implica que esta especificación es un componente importante de las aplicaciones seguras de XML, pero no es suficiente para especificar cuestiones de seguridad/confianza (como hacen los certificados digitales por ejemplo) y otros aspectos de seguridad.

Las firmas de XML se utilizan del siguiente modo: los objetos de la información firmados se elaboran  (se calcula un valor hash para ellos); el valor resultante se coloca en un elemento de XML con información adicional, entonces se elabora el elemento a su vez y se firma codificado. La especificación define un conjunto de algoritmos, sus URI y los requisitos para su implementación. Estos algoritmos incluyen SHA1 para la generación de hash, Base64 para codificar datos binarios, DSA con SHA1 (DSS) para firmas y XML Canónico para la canonización. Hablaremos más sobre el XML Canónico en la siguiente sección Ampliación de las firmas digitales para SOAP, donde veremos un ejemplo de XML Signature.

Podemos encontrar la especificación más actual de las firmas XML en https://www.w3.org/TR/xmldsig-core y encontrará más sobre las funciones del Grupo de Trabajo de las Firmas Digitales de XML en https://www.w3.org/Signature/

 Cifrado XML

Esta especificación se utiliza para describir el modo de utilizar XML para representar recursos Web de corma digital y codificada (incluyendo el propio XML). La especificación de XML Encryption está pensada para utilizarla junto con la especificación de las Firmas digitales XML para que podamos firmar y cifrar el contenido al mismo tiempo. El soporte para varios algoritmos de la codificación presenta la posibilidad de ampliar fácilmente la especificación a otros algoritmos nuevos.

Aquí vemos un ejemplo sencillo de la utilización de XML Encryption, tomado de la XML Encryption Syntax y Processing Working Draft (vínculo proporcionado en los recursos a continuación):

La información codificada se encierra en la etiqueta , con el valor codificado actual almacenado en la etiqueta . El método de cifrado se expresa especificando el algoritmo particular utilizado (para una lista de algoritmos, vea la especificación, para la que se proporciona un vínculo más abajo). Con este ejemplo queremos dar una visión general de en qué consiste la XML Encryption.
