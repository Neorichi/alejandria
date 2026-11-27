---
type: Artículo de enciclopedia
title: Autoridad de validación
description: "el autoridad de validación (VA) es aquel prestador de servicios de certificación que asegura la autenticidad, validez e integridad de las transacciones más críticas, como aquellas de transferencia de valores, compra, …"
resource: https://es.wikipedia.org/wiki/Autoridad_de_validación
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Autoridad_de_validación"}
license: CC BY-SA 4.0
id: eswiki-Autoridad_de_validación
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Autoridad de validación

el **autoridad de validación (VA)** es aquel prestador de servicios de certificación  que asegura la autenticidad, validez e integridad de las transacciones más críticas, como aquellas de transferencia de valores, compra, venta a través de la red. Validation Authority es una Autoridad de Certificación (CA=Certification Authority) neutral, con protocolo multi-validación, server para chequeo de la validad de los certificados digitales según norma X509V3 en sistemas que utilizan PKI (Infraestructura de llave pública) en corporaciones, bancos o dependencias gubernamentales.

La VA se encarga de comprobar que el certificado digital presentado por el usuario es válido, es decir, que ha sido emitido por una CA confiable y que no ha sido revocado. Para ello, la VA consulta la Lista de Certificados Revocados (CRL) de la CA que emitió el certificado, y también puede verificar la validez del certificado a través del uso de protocolos de validación en línea como el Protocolo de Validación de Certificados en Línea (OCSP). Además, la VA puede llevar a cabo otras comprobaciones adicionales para asegurarse de que el usuario que presenta el certificado es quien dice ser, como la validación de su identidad a través de un proceso de autenticación.
Véase también
 Prestador de servicios de certificación
