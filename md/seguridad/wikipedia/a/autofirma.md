---
type: Artículo de enciclopedia
title: AutoFirma
description: AutoFirma es una aplicación de firma desarrollada por el Ministerio de Hacienda y Administraciones Públicas de España para la firma electrónica de documentos.
resource: https://es.wikipedia.org/wiki/AutoFirma
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/AutoFirma"}
license: CC BY-SA 4.0
id: eswiki-AutoFirma
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# AutoFirma

- **Nombre:** AutoFirma
- **Autor:** Ministerio de Asuntos Económicos y Transformación Digital
- **Última versión:** 1.9 MacOS, Windows y GNU/Linux
- **Género:** programa de escritorio
- **Lenguaje programación:** Java
- **Sistema operativo:** GNU/Linux, Windows y MacOS
- **Método actualización:** descarga manual desde web oficial
- **Licencia:** GPL y EUPL
- **Estado:** activo
- **Soporte:** PDF incluido en la descarga

**AutoFirma** es una aplicación de firma desarrollada por el Ministerio de Hacienda y Administraciones Públicas de España para la firma electrónica de documentos.

Es parte de la *suite* @firma, un conjunto integral de servicios y herramientas en el que se basan los servicios comunes de identificación y firma electrónica del Gobierno de España. Está basada en software libre y estándares abiertos, lo cual garantiza la interoperabilidad y la seguridad en las transacciones electrónicas. Se compone de distintos productos, desarrollados por la Secretaría General de Administración Digital, perteneciente al Ministerio de Política Territorial y Función Pública, que pueden utilizarse de forma independiente o como servicios integrados en otras aplicaciones.

 Productos disponibles

 AutoFirma
Al poder ser ejecutada desde el navegador, permite firmar en páginas de Administración electrónica cuando se requiere durante un procedimiento administrativo. El usuario indica qué fichero quiere firmar y la aplicación escoge automáticamente el formato de firma que debe aplicar, liberando al usuario de cualquier duda técnica. En caso de disponer de más de un certificado en el dispositivo desde el que se va a proceder a firmar, se requiere la intervención del usuario para que seleccione la persona o entidad que procederá a la firma.

El Cliente @firma ha quedado obsoleto, al recomendarse usar Autofirma.

 @firma

Plataforma de servicios de validación y firma electrónica multi-PKI, @firma, ofrecida por el Gobierno de España como un servicio desacoplado de las aplicaciones, que permite cumplir con las medidas de identificación y autentificación descritas en la Ley 39/2015 del Procedimiento Administrativo Común de las Administraciones Públicas. Está basada en software libre y estándares abiertos. Así, la suite de productos del Cliente de Firma es un software libre de fuentes abiertas con una licencia: GNU GPL versión 2  y EUPL v1.1, y tiene su comunidad de desarrollo en GitHub.

De acuerdo con dicha ley, las Administraciones Públicas deben ofrecer servicios públicos electrónicos en los que se necesita firma electrónica y métodos avanzados de identificación o autenticación basados en certificados digitales. Debido a los múltiples certificados que pueden utilizarse y la multitud de estándares, implantar sistemas que soporten todas las funcionalidades puede resultar complejo y costoso. Con @firma se proporcionan servicios para comprobar que el certificado utilizado por el ciudadano es un certificado válido y que no ha sido revocado y que, por tanto, sigue teniendo plena validez para identificar a su propietario. Los servicios de la plataforma son aplicables a todos los certificados electrónicos cualificados publicados por cualquier proveedor de servicio de certificación supervisado, incluidos los certificados del DNIe.

La plataforma de validación @firma funciona como un servicio no intrusivo, que puede ser utilizado por todos los servicios electrónicos ofrecidos por las distintas Administraciones Públicas, tanto estatal, como autonómica o local. Para facilitar la integración con el servicio se proporcionan unas librerías de integración ‘Integr@’, que también permiten firma en servidor.

Además de ofrecerse como servicio, está disponible como software para instalar por las administraciones públicas (modelo federado).

Como servicio, proporcionado por la Secretaría General de Administración Digital o como producto, en modelo federado, ofrecida para ser instalada en cualquier Administración Pública.
 Para validación de certificados
 Para validación de firmas
 Como proveedor de identidad basada en certificados electrónicos

 Suite Cliente de @firma

La Suite Cliente de Firma es una herramienta de firma electrónica en entornos de escritorio y dispositivos móviles, que funciona integrado en una página web mediante JavaScript; como applet, como aplicación de escritorio, o como aplicación móvil, dependiendo del entorno del usuario.

Dada la complejidad de la creación de las firmas electrónicas en las diferentes plataformas de usuarios, por la variabilidad de sistemas operativos, navegadores, versiones y estándares de firma, la Secretaría General de Administración Digital ha desarrollado una suite de productos de firma multiplataforma, que pone a disposición de todas las Administraciones Públicas.

 Miniapplet @firma: applet Java multiformato de firma, multi navegador y multi sistema operativo. En navegadores no compatibles con Java, el JavaScript del Miniapplet ejecuta la aplicación Autofirma, en lugar del applet.
 Autofirma: Aplicación de escritorio, para usuarios sin conocimientos de firma electrónica. Autoselecciona el formato de firma más apropiado al documento a firmar, y permite visualizar los firmantes y documento firmado en caso de que se le introduzca una firma. También permite la firma en aplicaciones web cuando se integra con Miniapplet @firma.
 Cliente @Firma Móvil: Integrable de forma transparente para los usuarios del Miniapplet para firma desde dispositivos móviles, a través del uso del servidor intermedio (Proxi ClienteMovil). Disponible para plataformas: Android 4.0 y posteriores e iOS 8 y posteriores.

La Suite Cliente de @firma genera firmas en local (ordenadores o dispositivos móviles) en diferentes formatos:

 Para navegadores web:
 Miniapplet (Javascript) + Autofirma
 Como aplicación de escritorio
 Autofirma
 Como App para dispositivos móviles:
 cliente @firma móvil

La suite de productos del Cliente de Firma es un software libre de fuentes abiertas con una licencia: GNU GPL versión 2  y EUPL v1.1, y tiene su comunidad de desarrollo en GitHub.

La suite de productos del Cliente de Firma hace uso de los certificados digitales X.509 y de las claves privadas asociadas a los mismos que estén instalados en el repositorio (*keystore*) del navegador web (Internet Explorer, Firefox, Crome, Safari) o el sistema operativo así como de los que estén en dispositivos (SmartCards, USBKey) configurados en el mismo (el caso de los DNI-e).

El Cliente de Firma, es una aplicación que se ejecuta en cliente (en el ordenador del usuario, no en el servidor Web). Esto es así para evitar que la clave privada asociada a un certificado tenga que “salir” del contenedor del usuario (tarjeta, dispositivo USB o navegador) ubicado en su PC. De hecho, nunca llega a salir del navegador, el Cliente le envía los datos a firmar y éste los devuelve firmados.

El Cliente de Firma contiene las interfaces y componentes web necesarios para la realización de los siguientes procesos (además de otros auxiliares como cálculos de hash, lectura de ficheros, etc.):
 Firma de ficheros binarios.
 Multifirma masiva de ficheros.
 Cofirma (CoSignature): Multifirma al mismo nivel.
 Contrafirma (CounterSignature): Multifirma en cascada.

 FIRe

Componente que integra servicios de firma en local (PC y dispositivos móviles) y en la nube.

 eVisor

Aplicación web que proporciona un servicio de generación de copias auténticas e informes de firma en pdf.

 Portafirmas

Componente para la integración de la firma en los flujos de trabajo organizativos.

 Como app de complemento a Port@firmas: Port@firmas móvil

 Integr@

Librerías/servicios para la integración con @firma y la firma en servidor local.

VALIDe
VALIDe (Aplicación de Validación de firma y certificados en línea de @firma) es la plataforma de validación que la Administración General del Estado pone a disposición de las Administraciones y de los ciudadanos para la validación de certificados y, además, ofrece los siguientes servicios:

Validación de firmas electrónicas
Generación de firmas electrónicas en múltiples formatos
Visualización de firmas con la ayuda del Visor

TS@
TS@ es una autoridad de sellado de tiempo puesta a disposición de todas las Administraciones Públicas con el objetivo de ofrecer los servicios de sellado, validación y resellado de sellos de tiempo.

La plataforma TS@ del Ministerio de Asuntos Económicos y Transformación Digital ofrece servicios de sellado de tiempo para documentos electrónicos, garantizando la integridad y autenticidad de la información a través de sellos de tiempo emitidos por una Autoridad de Sellado de Tiempo (TSA) . La TSA está sincronizada con el Real Observatorio de la Armada, asegurando la fiabilidad de la fuente de tiempo utilizada.

Los servicios disponibles en la TSA incluyen la solicitud de sellos de tiempo, validación de sellos y resellado de tiempo para preservar la validez de los sellos generados . Estos servicios se ofrecen a través de notación abstracta ASN.1 y Web Services basados en XML-SOAP, facilitando la integración con aplicaciones.

La integración con la TSA@ del Ministerio de Asuntos Económicos y Transformación Digital requiere seguir unos pasos sencillos, como estar conectado a la Red SARA y contactar con el servicio de soporte para obtener los parámetros de conexión.

Entre las ventajas de utilizar la plataforma TS@ se encuentran la reducción de costes en los servicios de validación y emisión de sellos de tiempo, la promoción de la innovación al ser la primera Autoridad de Sellado de Tiempo sincronizada con el ROA, y la facilitación del cumplimiento de las obligaciones de la Ley 39/2015 para garantizar la acreditación de la fecha y hora de operaciones electrónicas.

Véase también
 Ansible (software)
 CAdES
 Certutil
 Clave Permanente
 DNI (España)
 eIDAS
 Java KeyStore
 OpenSSL
 Pasarela de firma
 Prestador de servicios de confianza
 X.509

 Referencias

 Enlaces externos
 Autofirma: qué es y cómo usarla para firmar documentos con tu certificado digital, (Xataka).
 Firmar un PDF con AutoFirma,
 Autofirma, Java, Firefox y Debian 8 en la Administración Electrónica
 PAE (Portal de Administración Electrónica)
 En Forja del CTT (Centro de Transferencia de Tecnología) (¿Qué es Forja?).
 VALIDe, verificar estado de certificados, firmas o sedes.
 FNMT-RCM, verificar estado de certificados o DNIe.
 Portafirmas (administracionelectronica.gob.es)
