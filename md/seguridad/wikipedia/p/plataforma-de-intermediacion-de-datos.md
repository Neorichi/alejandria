---
type: Artículo de enciclopedia
title: Plataforma de intermediación de datos
description: "La plataforma de intermediación de datos (PID) es una aplicación informática del Ministerio de Hacienda y Administraciones Públicas de España, que funciona como un nodo de interoperabilidad que presta servicios SCSP …"
resource: https://es.wikipedia.org/wiki/Plataforma_de_intermediación_de_datos
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Plataforma_de_intermediación_de_datos"}
license: CC BY-SA 4.0
id: eswiki-Plataforma_de_intermediación_de_datos
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Plataforma de intermediación de datos

La **plataforma de intermediación de datos** (**PID**) es una aplicación informática del Ministerio de Hacienda y Administraciones Públicas de España, que funciona como un nodo de interoperabilidad que presta servicios SCSP comunes para el intercambio de información entre emisores y requirentes de las Administraciones públicas españolas (AAPP), según un Real Decreto aprobado el 8 de enero de 2010. Esta plataforma ofrece servicios de verificación y consulta de datos a otras AAPP con el objetivo de eliminar los certificados en papel (de corriente de pago con la AEAT, de deuda con la TGSS, de empadronamiento, de matrimonio, etc.) y que el ciudadano no tenga que presentar ante las Administraciones (estatal, autonómica o local) documentación que ya obra en poder de las propias Administraciones. El certificado se sustituye por un intercambio de datos entre administraciones que se realiza de forma electrónica, estandarizada y rápida y con las garantías jurídicas descritas en el Real Decreto 263/1996 (redacción del Real Decreto 209/2003), si bien esta norma está derogada por el Real Decreto 1671/2009.

 Historia del proyecto

En mayo de 2006, sale en el BOE la publicación del Real Decreto 522/2006 y del Real Decreto 523/2006, que suprimen la aportación de fotocopias de documentos acreditativos de identidad y la exigencia de aportar el certificado de empadronamiento como documento probatorio del domicilio y residencia en los trámites de la AGE respectivamente.

En diciembre de 2006, sale la publicación de las órdenes ministeriales del Ministerio de Presidencia PRE/2949/2006 y PRE/4008/2006 en las que se establece la configuración, características, requisitos y procedimientos de acceso al sistema de Verificación y consulta de datos de identidad y residencia, germen de la plataforma de Intermediación, y se establece la fecha de entrada en producción de los sistemas del 1 de enero de 2007.

En junio de 2007 se publica la  LAECSP ley 11/2007, Ley de Acceso Electrónico a los Servicios Públicos, en cuyo artículo 6.2b se refuerza la iniciativa de estos sistemas recogiendo el derecho de los ciudadanos a no aportar datos y documentos que obren en poder de las AAPP.

En el año 2010 se amplía el catálogo de servicios disponibles en el sistema de Verificación y consulta de datos de identidad y residencia pasando a denominarse Plataforma de Intermediación de datos, Servicios de Verificación y Consulta de Datos.

 Especificaciones técnicas

La plataforma de intermediación se posiciona como un emisor de servicios SCSP para todos los certificados que emite, independientemente de la naturaleza originaria de los datos, facilitando la interoperabilidad entre Administraciones públicas.

 Roles o participantes
 Cedente:  será cualquier organización que posea datos relativos a los ciudadanos que otra pueda necesitar consultar en el ámbito del ejercicio de sus competencias; es el responsable de los mismos según la Ley Orgánica 15/1999, de 13 de diciembre, de Protección de Datos de Carácter Personal y los ofrecerá a posibles Cesionarios a través de un Emisor.
 Emisor: Es el organismo público que ofrece el servicio o transmisión de datos. (Servidor), el que facilita la cesión de los datos desde un punto de vista tecnológico. Normalmente coincidirá con el cedente aunque no siempre.
 Cesionario: cualquier organización autorizada a consultar determinados datos de los ciudadanos en poder de un Cedente.
 Requirente: Organismo que facilita la consulta de los datos desde un punto de vista tecnológico a un cesionario.
 Plataforma de Intermediación del MHAP: nodo de interoperabilidad que presta servicios de interoperabilidad para el intercambio de información entre Emisores y Requirentes según el Real Decreto 4/2010, de 8 de enero.

 Funcionalidades

 Control detallado de usuarios y autorizaciones.
 Control detallado de los procedimientos del organismo autorizado.
 Transmisiones asíncronas por Lotes a emisores que sólo ofrecen servicios síncronos monopetición.
 Composición de mensajes SCSPvX (v2/v3 según el certificado requerido).
 Firma de mensajes SCSP (XMLDsig, WS-Security y/o XADES-B según los emisores de certificados).
 Almacenamiento de información de trazabilidad.
 Recepción de mensajes SCSP y validación de los mismos.
 Validación de esquemas XSD.
 Validación de la firma digital (XMLDsig, WS-Security y/o XADES-B según los emisores de certificados) y del certificado con el que se firmó usando @firma.
 Mecanismo de aceleración de las peticiones (caché de validación de certificados electrónicos con @firma).
 Autorización y Autentificación de Organismos Requirentes/Cesionarios pudiendo llegar a nivel de procedimiento.

 Certificados SCSP
Actualmente, se encuentran disponibles los siguientes certificados:

 Dirección General de la Policía (DGP) -- Verificación de datos de identidad
 Dirección General de la Policía (DGP) -- Consulta de datos de identidad
 Instituto Nacional de Estadística (INE) -- Verificación de datos de residencia (Extendido)
 Servicio Público de Empleo Estatal (SPEE-INEM) --	Situación de desempleo
 Servicio Público de Empleo Estatal (SPEE-INEM) --	Importes de prestación a fecha actual
 Servicio Público de Empleo Estatal (SPEE-INEM) --	Importes por periodo
 Ministerio de Educación -- Títulos no universitarios
 Ministerio de Educación -- Títulos universitarios
 Dirección General del Catastro --	Datos catastrales
 Dirección General del Catastro --	Certificación catastral
 Tesorería General de la Seguridad Social -- Corriente de pago con la SS
 Tesorería General de la Seguridad Social -- Alta en la Seguridad Social
 Agencia Estatal de Administración Tributaria -- Corriente de pago de obligaciones tributarias para:
 Contratación con las AAPP
 Obtención de licencias de transporte
 Solicitud de ayudas y subvenciones
 Tramitación de permisos de residencia y trabajo para extranjeros

  Ventajas e inconvenientes

**Para el ciudadano**
 Evitar desplazamientos y que el interesado actué como “funcionario”, moviendo documentación de una ventanilla a otra de la Administración.
 Ejercer su derecho a no aportar documentación que ya obra en poder de la administración.
 Ahorro de coste y tiempo al no tener que recabar los certificados en papel ni en electrónico.
 Mayor agilidad de resolución de los trámites al no tener que esperar por datos que la administración puede obtener en el momento.

**Para las Administraciones públicas**
 Posibilidad de realizar completa la tramitación electrónica.
 Ahorro de coste en la Administración al no tener que almacenar ni tramitar papeles.
 Ahorro de tiempo, al evitar las firmas manuscritas y la presencia de personal.
 Da un servicio simple y eficaz a los ciudadanos.
 Mejorar la imagen de las AAPP ante los ciudadano.

 Referencias

 Enlaces externos
LAECSP ley 11/2007
RD 1671/2009
