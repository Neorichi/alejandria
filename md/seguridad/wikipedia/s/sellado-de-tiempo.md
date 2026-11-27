---
type: Artículo de enciclopedia
title: Sellado de tiempo
description: El sellado de tiempo o timestamping es un mecanismo en línea que permite demostrar que una serie de datos han existido y no han sido alterados desde un instante específico en el tiempo.
resource: https://es.wikipedia.org/wiki/Sellado_de_tiempo
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sellado_de_tiempo"}
license: CC BY-SA 4.0
id: eswiki-Sellado_de_tiempo
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sellado de tiempo

El **sellado de tiempo** o ***timestamping*** es un mecanismo en línea que permite demostrar que una serie de datos han existido y no han sido alterados desde un instante específico en el tiempo. Este protocolo se describe en el RFC 3161 y está en el registro de estándares de Internet.

Una autoridad de sellado de tiempo actúa como tercera parte de confianza testificando la existencia de dichos datos electrónicos en una fecha y hora concretos.

 Pasos para generar un sello de tiempo
 Un usuario quiere obtener un sello de tiempo para un documento electrónico que él posee.
 Un resumen digital (técnicamente un hash) se genera para el documento en el ordenador del usuario.
 Este resumen forma la solicitud que se envía a la autoridad de sellado de tiempo (TSA).
 La TSA genera un sello de tiempo con esta huella, la fecha y hora obtenida de una fuente fiable y la firma electrónica de la TSA.
 El sello de tiempo se envía de vuelta al usuario.
 La TSA mantiene un registro de los sellos emitidos para su futura verificación.

 Dónde se aplica
 Factura electrónica.
 Protección de la propiedad intelectual.
 Registro electrónico / libros financieros / apuestas / pedidos
 Trazas (logging) seguras.
 Transacciones seguras en comercio electrónico.
 Voto electrónico.
 Visado electrónico.
 Transparencia en Gobierno
 Otras muchas áreas...

 Empleo del sellado de tiempo en la firma electrónica
Las normas europeas **TS 101 733** y **TS 101 903** establecen dos modalidades de firma que incluyen sellado de tiempo. La variante **ES-T** añade el sellado a una firma básica (BES) y la variante **ES-C** añade, además del sellado de tiempo, información sobre la ruta en la que se puede verificar la validez del certificado obtenido de una consulta OCSP o una lista de revocación de certificados. Además estas normas prevén la modalidad **ES-XL** que incluye información sobre el **estado** de revocación del certificado. De esta forma se obtiene una **firma completa** que libera al receptor de la firma del problema de deducir de la firma o del certificado la forma de comprobar la validez del certificado que puede variar de PSC en PSC.

 Véase también
 PKI
 Timestamp
 Firma digital
 Certificado digital
 Seguridad por Niveles

 Enlaces externos
 AC Firmaprofesional Firmaprofesional Sellado de Tiempo
 Safelayer Demo Site, servidor time-stamp de demostración.
 Servicio de sellado de tiempo de Safe Creative  Acceso al sellado de tiempo de Safe Creative.
 TSA Server, Autoridad Timestamp ADSS.
 FreeTSA, Autoridad Timestamp + URL screenshots.
 Realsec, Autoridad de Sellado de tiempo.
 AC Camerfirma S.A, Autoridad de Certificación Digital
 Camerfirma Perú S.A.C., Entidad de Certificación digital Raíz de Perú.
