---
type: Artículo de enciclopedia
title: Sustitución de Certificados en Soporte Papel
description: "Sustitución de Certificados en Soporte Papel, SCSP, es un conjunto de especificaciones orientadas al intercambio de datos entre las administraciones públicas con el objetivo de eliminar los certificados administrativos …"
resource: https://es.wikipedia.org/wiki/Sustitución_de_Certificados_en_Soporte_Papel
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Sustitución_de_Certificados_en_Soporte_Papel"}
license: CC BY-SA 4.0
id: eswiki-Sustitución_de_Certificados_en_Soporte_Papel
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Sustitución de Certificados en Soporte Papel

**Sustitución de Certificados en Soporte Papel**, **SCSP**, es un conjunto de especificaciones orientadas al intercambio de datos entre las administraciones públicas con el objetivo de eliminar los certificados administrativos en papel (certificado de estar al corriente de pago con la AEAT, deuda con la Tesorería General de la Seguridad Social, certificado de empadronamiento, certificado de matrimonio, etc.) y que el ciudadano no tenga que presentar ante las administraciones públicas (estatal, autonómica o local) documentación que ya obra en poder de ellas. El certificado se sustituye por un intercambio de datos entre administraciones que se realiza de forma electrónica, estandarizada y rápida y con las garantías jurídicas descritas en el RD 263/1996, si bien esta norma está derogada por el RD 1671/2009.

Toda la información disponible acerca de SCSP se encuentra en el Portal de Administración Electrónica (PAE).

 Historia del proyecto SCSP
Durante el año 2003 se formó un grupo de trabajo coordinado por el Ministerio de Administraciones Públicas (2026 - Actual Ministerio para la Transformación Digital y de la Función Pública) con el objeto de definir y especificar el mecanismo de intercambio de información entre AAPP para la eliminación de Certificados Administrativos en Papel.

En este proyecto colaboraron las siguientes administraciones y organismos públicos: Agencia Española de Administración Tributaria, Tesorería General de la Seguridad Social (TGSS), Ministerio de Trabajo y Asuntos Sociales,
Instituto Nacional de la Seguridad Social, Ministerio de Trabajo y Asuntos Sociales y Ministerio de Agricultura, Pesca y Alimentación dando como resultado la publicación de los servicios de Estar al corriente de Obligaciones Tributarias (AEAT) y de Deuda con la Seguridad Social (TGSS) como emisores.

En 2004 se realizaron las primeras versiones de la especificación dando como resultado en el año 2005 la primera versión estable que se denominó SCSPv2.
Igualmente, se trabajó desde el Ministerio de Administraciones Públicas en unas librerías (J2EE y .NET) compatibles con el estándar para que pudieran ser utilizadas por todas las Administraciones Públicas españolas en el intercambio de certificados administrativos.

En el año 2009 se vio la necesidad de ampliar las especificaciones para permitir la interoperabilidad con Nodos de Interoperabilidad (AAPP Intermediarios o “brokers”) dando lugar a la versión SCSPv3 (en el año 2012 sigue siendo la última versión estable y no hay previsión a corto plazo de modificarla).
También se aprovechó para modificar las información intercambiada y registrada en las transmisiones de datos.

 Especificaciones técnicas
 Roles o participantes
 Cedente:  será cualquier organización que posea datos relativos a los ciudadanos que otra pueda necesitar consultar en el ámbito del ejercicio de sus competencias; es el responsable de los mismos según la Ley Orgánica 15/1999, de 13 de diciembre, de Protección de Datos de Carácter Personal y los ofrecerá a posibles Cesionarios a través de un Emisor.
 Emisor: Es el organismo público que ofrece el servicio o transmisión de datos. (Servidor), el que facilita la cesión de los datos desde un punto de vista tecnológico. Normalmente coincidirá con el cedente aunque no siempre.
 Cesionario: cualquier organización autorizada a consultar determinados datos de los ciudadanos en poder de un Cedente.
 Requirente: Organismo que facilita la consulta de los datos desde un punto de vista tecnológico a un cesionario.
 Plataforma de Intermediación de datos del MHAP: nodo de interoperabilidad que prestará servicios comunes para el intercambio de información entre Emisores y Requirentes según el Real Decreto 4/2010, de 8 de enero.

 Funcionamiento
La especificación SCSP define un conjunto de mensajes, definidos por sus correspondientes esquemas XSD

	El envío de peticiones y respuestas se realiza mediante servicios Web.
	El formato de las transmisiones de datos es XML.
	El sistema permite que la petición-respuesta sea síncrona o asíncrona.
	Los mensajes van firmados con XML Dsig (SCSPv2) o WS-Security (SCSPv3).

Mensajes generales: Son comunes a todos los servicios y están compuestos por los siguientes mensajes.
 Petición (peticion.xsd) con namespace
 Confirmación (confirmacionPeticion.xsd)  con namespace
 Solicitud de Respuesta (solicitudRespuesta.xsd) con namespace
 Respuesta (respuesta.xsd) con namespace
 Soap Fault Atributos (soapfaultatributos.xsd ) con namespace

Mensajes Específicos: Depende de cada certificado administrativo o transmisión de datos. Lo define el organismo emisor.
 Datos Específicos con namespace

 SCSPv2

SCSPv2 define las siguientes características para las transmisiones de datos que se realicen entre administraciones:
 	Se han definido dos documentos (petición y respuesta) con dos partes; la primera, Datos Genéricos, donde se transmite información común a todos los certificados en papel que se sustituyen, como la relativa al organismo solicitante, al organismo emisor, al interesado al que se refieren los datos, y la relativa a la propia transmisión. En la segunda parte de Datos Específicos, cada organismo define los campos que transmite en función del tipo de certificado en papel que se está sustituyendo. Estos datos específicos también deberán estar en formato XML, pero es obligación de cada organismo emisor publicar el esquema XSD que indica la estructura del mismo. También se han definido otros dos documentos XML “Confirmación petición” y “Solicitud respuesta” que se emplean cuando la petición es realizada en modo asíncrono, para indicar que la petición se recibió correctamente y para solicitar la respuesta transcurrido el Tiempo Estimado de Respuesta  indicado por el emisor respectivamente.
	El protocolo utilizado para la comunicación es SOAP sobre HTTPS.
	La infraestructura de comunicaciones sobre la que se apoyan todos los servicios de sustitución de certificados en soporte papel es la Red SARA.
	Para asegurar la autenticación, confidencialidad e integridad de la información transmitida se emplea el protocolo SSL, exigiendo identificación a ambos extremos mediante certificado electrónico reconocido.
	La integridad de los datos y el no repudio se garantiza firmando tanto las peticiones como las respuestas emitidas en el sistema. La firma se transmite en la cabecera SOAP del mensaje, utilizando la codificación XMLdSig.
	Para la conservación de la información, cada organismo emisor deberá almacenar las transmisiones emitidas durante el tiempo establecido en la normativa aplicable. Se propone un sistema y esquema de almacenamiento común a todos los organismos emisores y otro común para todos los organismos requirentes, (incluidos en las librerías).

 SCSPv3
La versión SCSPv3 incorpora las siguientes novedades:
Debido a la desaparición del Ministerio de Administraciones Públicas, y con el objetivo de obtener un lugar de referencia para poder ubicar los esquemas de SCSP, se ha sustituido el espacio de nombres www.map.es por intermediación.redsara.es para hacerlos independientes de la nomenclatura de los organismos que los usan, e indicar que la versión soportada es adecuada para la intermediación.

Introduce nuevos campos en el esquema (datos genéricos) asociados al “solicitante” de la información, que se habían identificado como necesarios en el uso de la versión 2.
	Unidad Tramitadora: Unidad dentro del Órgano Solicitante que realiza la solicitud.
	Procedimiento
	CodProcedimiento: código del procedimiento del organismo tramitador
	NombreProcedimiento: nombre unívoco del procedimiento del organismos tramitador.
	IdExpediente: identificador del expediente en el organismo tramitador.
	Se ha cambiado el versionado de los esquemas, pasando de V2 a v3.

Por motivos de interoperabilidad con los estándares actuales más modernos, se ha optado por sustituir el mecanismo de firma basado en XML-SIG puro, por el especificado dentro de la familia WS-Security. Modelo de firma más estandarizado e implementado por las distintas plataformas SOA.

Incorpora la posibilidad de cifrado en las respuestas en aquellas situaciones que el emisor lo considere necesario por motivos de confidencialidad de la información a intercambiar. Por defecto, el cifrado irá siempre en la respuesta, aunque por necesidades del servicio se podría aplicar a cualquier mensaje intercambiado, y se cifrará exclusivamente aquella información especialmente sensible que se quiera proteger. Por regla general se cifrará el contenido del nodo  en peticiones con una única transmisión y el nodo Transmisiones cuando sea una multipetición (Sólo en modo asíncrono).  El uso de cifrado se ha incorporado debido a que mientras que en SCSPv2 la comunicación entre organismos requirentes y emisores era punto a punto y con SSL la confidencialidad estaba garantizada, SCSPv3 está orientado a servicios intermediados, aunque no exclusivamente a ellos, en que un tercero podría ver la información en caso de que esta no estuviese cifrada.

Adicionalmente se ha incluido un atributo opcional en los campos:
 Datos específicos en todos los casos.
 Transmisiones en el caso de respuestas
 Solicitudes en el caso de peticiones

 Bibliotecas SCSP
Las bibliotecas SCSPv3 son un software específico desarrollado por la **Dirección General de Modernización Administrativa, Procedimiento e Impulso de la Administración Electrónica**, perteneciente al **Ministerio de Hacienda y Administraciones Públicas** que se puede integrar en las aplicaciones de backoffice de los distintos organismos públicos y consultar los datos ofrecidos por emisores que cumplan con las especificaciones SCSP.

La última versión (31 de enero de 2021) de las bibliotecas SCSP es la 4.6.0. para J2EE y 3.4.0 para .NET. Complementariamente a las bibliotecas se suministra en la versión J2EE una aplicación web completa que permite a cualquier organismo consultar los certificados SCSP disponibles sin necesidad de desarrollar nada, con las siguientes funcionalidades:
 Control detallado de usuarios y autorizaciones
 Control detallado de los procedimientos del organismo y matriz de autorización del organismo de los usuarios
 Transmisiones asíncronas por Lotes mediante uso de plantillas Excel adaptadas a cada certificado
 Exportación de los resultados de las transmisiones realizadas
 Objeción de Justificantes en PDF de las transmisiones realizadas

También existe una aplicación que permite el uso de las bibliotecas J2EE por parte de otras aplicaciones/tecnologías mediante uso de servicios web simplificados (recubrimiento SCSP_WS) por ejemplo PHP, Python, Ruby, .NET, etc.

 Funciones de las bibliotecas SCSPv3
Soporta requirentes y emisores
 Funcionalidades comunes a requirentes y emisores
 Composición de mensajes SCSPvX (v2/v3 según el certificado requerido)
 Firma de mensajes SCSP (XMLDsig o WS-Security)
 Cifrado de mensajes SCSP (si procede)
 Almacenamiento histórico de mensajes y transmisiones
 Envío de la petición al *endpoint* de cada servicio
 Recepción de mensajes SCSP y validación de los mismos
 Validación de esquemas XSD
 Validación de la firma digital y del certificado con el que se firmó
 Descifrado de mensajes SCSP si procede (por ejemplo, respuestas AEAT y TGSS a través de la Plataforma de Intermediación)
 Mecanismo de aceleración de las peticiones (caché de validación de certificados electrónicos con @firma)

 Funcionalidad del emisor
 Autorización y autentificación de organismos requirentes/cesionarios
 Comunicación con el *backOffice*

 Requisitos de funcionamiento
 **Sistema operativo**: Windows 2000, Windows  XP, Windows Vista, Windows 7, Windows Server 2003, Windows Server2008, Linux (Red hat, Debian, Guadalinex, Ubuntu, etc), Mac OS X 10.5 y Sun Solaris / OpenSolaris 10.
 **Navegador web**: Firefox 2.0.20 o superior, Internet Explorer 5.5 o superior.
 **JRE** 1.6 o superior.
 **Bases de Datos**: Oracle 9, 10 o superior, SQL Server 2005 y 2008, Mysql 5 o superior, Postgresql 9 o superior.
 **Servidores de aplicación**: Tomcat 6.0.29 o superior, JBOSS 4.1, 5 o superior (a evaluar según las distintas versiones) , IIS, Oracle OS. Para otros servidores de aplicación y versiones se puede evaluar por parte del equipo de desarrollo.
 **Certificados X509 reconocidos**:Se necesita conexión con la plataforma @firma y usar certificados reconocidos por esta plataforma. Para usar las bibliotecas se recomienda un certificado de sello de órgano como se recoge en la Ley 11/2007. En el caso de usar el Cliente Ligero será necesario un certificado de servidor.

 Certificados disponibles usando SCSP
Actualmente, se encuentran disponibles los siguientes certificados

A través de la Plataforma de Intermediación de datos  del MHAP:
 Dirección General de la Policía (DGP) -- Verificación de datos de Identidad
 Dirección General de la Policía (DGP)	-- Consulta de datos de Identidad
 Instituto Nacional de Estadística (INE)	-- Verificación de datos de Residencia (Extendido)
 Servicio Público de Empleo Estatal (SPEE-INEM) --	Situación de Desempleo
 Servicio Público de Empleo Estatal (SPEE-INEM) --		Importes de prestación a fecha actual
 Servicio Público de Empleo Estatal (SPEE-INEM) --		Importes por periodo
 Ministerio de Educación	-- Títulos No Universitarios
 Ministerio de Educación	-- Títulos Universitarios
 Dirección General del Catastro --	Datos Catastrales
 Dirección General del Catastro --	Certificación Catastral
 Tesorería General de la Seguridad Social --	Corriente de Pago con la SS
 Tesorería General de la Seguridad Social --	Alta en la Seguridad Social
 Agencia Estatal de Administración Tributaria	Estar al Corriente de Pago de obligaciones tributarias para:
	Contratación con las AAPP
 Obtención de licencias de transporte.
	Solicitud de ayudas y subvenciones.
 Tramitación de permisos de residencia y trabajo para extranjeros.

 Directamente por la Agencia Estatal de Administración Tributaria.
 Certificado de la Renta (2008, 2009, 2010)
 Domicilio Fiscal
 Impuesto de Actividades Económicas (IAE)
 Cuentas Corrientes

  Ventajas y beneficios del proyecto SCSP
**Para el ciudadano**
 Evitar desplazamientos y que el interesado actué como “funcionario”, moviendo documentación de una ventanilla a otra de la Administración.
 Ejerce su derecho a no aportar documentación que ya obra en poder de la administración.
 Ahorro de coste y tiempo al no tener que recabar los certificados en papel ni en electrónico.
 Mayor agilidad de resolución de los trámites al no tener que esperar por datos que la administración puede obtener en el momento. trámites

**Para las Administraciones**
 Posibilidad de realizar completa la tramitación electrónica.
 Ahorro de coste en la Administración al no tener que almacenar ni tramitar papeles.
 Ahorro de tiempo, al evitar las firmas manuscritas y la presencia de personal.
 Da un servicio simple y eficaz a los ciudadanos.
 Mejorar la imagen ante los ciudadano.

 Liberación
El proyecto de bibliotecas SCSP es una iniciativa alineada con la Ley 11/2007, de acceso electrónico de los ciudadanos a los Servicios Públicos,
que favorece la reutilización de aplicaciones y la transferencia de tecnología.

Cualquier Administración Pública puede acceder a las bibliotecas gratuitamente a través del PAE (Portal de Administración Electrónica)

Este software se libera con una licencia dual EUPL versión 1.1 y GNU GPL versión 3. Este tipo de licenciamiento ofrece la posibilidad de acogerse a los derechos que proporcionan una o ambas licencias, a su conveniencia, siempre que se cumplan las condiciones que cada una de ellas impone.
La documentación ha sido liberada bajo una licencia Creative Commons Reconocimiento-NoComercial-CompartirIgual 3.0 (CC BY-NC-SA 3.0).

 Referencias

 Enlaces externos
PAE (Portal de Administración Electrónica)
Servicios SCSP de la AEAT
