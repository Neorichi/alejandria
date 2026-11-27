---
type: Artículo de enciclopedia
title: Firma XML
description: La firma XML (también llamada XMLDsig, DSig XML, XML-Sig) es una recomendación del W3C que define una sintaxis XML para la firma digital.
resource: https://es.wikipedia.org/wiki/Firma_XML
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Firma_XML"}
license: CC BY-SA 4.0
id: eswiki-Firma_XML
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Firma XML

La **firma XML** (también llamada XMLDsig, DSig XML, XML-Sig) es una recomendación del W3C que define una sintaxis XML para la firma digital. Funcionalmente, tiene mucho en común con PKCS#7, pero es más extensible y está orientada hacia la firma de documentos XML. Es utilizada por diversas tecnologías Web como SOAP, SAML y otras.

Las firmas XML se pueden utilizar para firmar datos o recursos de cualquier tipo, normalmente documentos XML, pero cualquier cosa que sea accesible a través de una URL puede firmarse. Una firma XML que se utiliza para firmar un recurso fuera del documento XML que la contiene se llama una firma separada (detached). Si se utiliza para firmar una parte del documento que la contiene, se llama una firma envuelta (enveloped). Si contiene los datos firmados dentro de sí mismo se llama una firma envolvente (enveloping).

 Estructura

Una firma XML consiste en un elemento Signature (Firma) en el espacio de nombres de http://www.w3.org/2000/09/xmldsig#. La estructura básica es la siguiente:

 El elemento SignedInfo contiene o referencia los datos firmados y especifica qué algoritmo se usa. - Los elementos SignatureMethod y CanonicalizationMethod son usados por el elemento SignatureValue y están incluidos en SignedInfo para evitar que sean modificados. - Uno o más elementos Reference especifican el recurso que se está firmando por la referencia URI y cualquier transformación que vaya a aplicarse al recurso antes de firmar. DigestMethod especifica el algoritmo hash antes de aplicar el hash. - DigestValue contiene el resultado de aplicar el algoritmo hash al (o los) recurso(s) transformado(s).

 El elemento SignatureValue contiene el resultado de una firma codificada en Base64 (la firma generada con los parámetros especificados en el elemento SignatureMethod) del elemento SignedInfo después de aplicar el algoritmo especificado por el CanonicalizationMethod.

 El elemento KeyInfo permite opcionalmente al firmante especificar los destinatarios con la clave que valida la firma, generalmente en la forma de uno o más certificados digitales X.509. La parte restante debe identificar la clave del contexto si no está presente KeyInfo.

 El elemento Object (opcional) contiene los datos firmados en caso de ser una *firma envolvente*.

Véase también
 Xades

 Enlaces externos
 XML-Signature Syntax and Processing (W3C)
 Performance of Web Services Security
 Performance Comparison of Security Mechanisms for Grid Services
 Why XML canonicalization is bad for Web Services Security
 Canonical XML
 Additional XML Security Uniform Resource Identifiers (URIs)
 Exclusive XML Canonicalization
 Why XML Security is Broken
 XMLSignatures Java binding  for XMLBeans and JAXB.
 ADSS Signing Server One solution for all your signing & verification needs!
