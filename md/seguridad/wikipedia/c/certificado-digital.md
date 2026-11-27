---
type: Artículo de enciclopedia
title: Certificado digital
description: "Un certificado digital o certificado electrónico es un fichero informático firmado electrónicamente por un prestador de servicios de certificación, considerado por otras entidades como una autoridad para este tipo de …"
resource: https://es.wikipedia.org/wiki/Certificado_digital
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Certificado_digital"}
license: CC BY-SA 4.0
id: eswiki-Certificado_digital
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Certificado digital

Un **certificado digital** o **certificado electrónico** es un fichero informático firmado electrónicamente por un prestador de servicios de certificación, considerado por otras entidades como una autoridad para este tipo de contenido, que vincula unos datos de verificación de firma a un firmante, de forma que únicamente puede firmar este firmante, y confirma su identidad. Tiene una estructura de datos que contiene información sobre la entidad (por ejemplo una clave pública, una identidad o un conjunto de privilegios). La firma de la estructura de datos agrupa la información que contiene de forma que no puede ser modificada sin que esta modificación sea detectada.

Normalmente cuando se habla de certificado digital se está hablando de los certificados de clave pública que son un tipo de certificado digital.

La información contenida en un certificado depende del propósito para el cual fue creado el certificado. Podemos clasificar los certificados atendiendo al propósito en:
Certificados de clave pública. Asocian una clave pública a alguna representación de la identidad de una entidad. La clave privada asociada a dicha clave pública es asumida que está en posesión de dicha entidad. Además se pueden incluir otras informaciones relevantes como el período de validez, identificador de los algoritmos para los cuales se puede usar la clave pública o políticas o restricciones de uso de dicho certificado. Son usados principalmente en protocolos relacionados con la autenticación de entidades.
Certificados de atributos. Normalmente no contienen claves públicas, sino que asocian otro tipo de información (ej. roles, derechos de uso o privilegios) a alguna representación de la identidad de una entidad. Son usados principalmente en protocolos relacionados con la autorización de entidades.

 Aplicaciones

 **Autenticación de usuarios**

Los certificados digitales se utilizan para autenticar la identidad de usuarios en línea.

 **Firma digital**

Los certificados digitales permiten la firma electrónica de documentos y transacciones lo que garantiza la integridad de la información y proporciona no repudio.

 **Cifrado de datos**

Los certificados digitales se utilizan para cifrar la comunicación y proteger la confidencialidad de los datos transmitidos. Esto es especialmente importante en cualquier situación en la que se necesite garantizar la privacidad.

 **Acceso seguro a servicios en línea**

Los certificados digitales se utilizan para garantizar el acceso seguro a servicios en línea.

 **Validación de sitios web**

Los certificados digitales se utilizan para validar la autenticidad y la identidad de los sitios web.

 Herramientas que permiten la administración de certificados

 **Autoridades de Certificación (AC)**

Las AC son entidades que emiten y administran certificados digitales. Proporcionan servicios de generación, renovación y revocación de certificados, así como la validación de identidad de los solicitantes.

 **Gestores de certificados**

Son aplicaciones o plataformas que permiten la gestión centralizada de certificados digitales. Estas herramientas facilitan la generación, instalación, renovación y revocación de certificados, así como el monitoreo y la administración de su ciclo de vida. Algunos ejemplos populares son OpenSSL, Keycloak y Microsoft Certificate Services.

 **Plataformas de gestión de identidad**

Estas plataformas ofrecen funcionalidades para administrar identidades digitales y los certificados asociados. Permiten la gestión de usuarios, autenticación, autorización y el control de acceso basado en roles. Algunos ejemplos son Okta, Azure Active Directory y Ping Identity.

Formatos
Se han definido varios formatos de los certificados digitales. Los más importantes son:
X.509
SPKI
PGP
SAML

Revocación
Se ha definidos distintas métodos para la gestión de protocolos que permiten su revocación. Los más importantes son:
Listas de revocación
OCSP

Referencias
