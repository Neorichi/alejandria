---
type: Artículo de enciclopedia
title: SAML 1.1
description: El Lenguaje de Marcado para Confirmaciones de Seguridad (SAML) es un estándar de XML para intercambiar datos de autenticación y de autorización.
resource: https://es.wikipedia.org/wiki/SAML_1.1
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/SAML_1.1"}
license: CC BY-SA 4.0
id: eswiki-SAML_1.1
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# SAML 1.1

El **Lenguaje de Marcado para Confirmaciones de Seguridad** (SAML) es un estándar de XML para intercambiar datos de autenticación y de autorización. SAML es un producto de la organización OASIS (Comité técnico de Servicios de Seguridad)

***SAML*** ***1.1*** fue ratificado como un estándar de OASIS en septiembre del año 2003.  Los aspectos críticos de SAML 1.1 están cubiertos en detalle en los documentos oficiales SAMLCore and SAMLBind.  Para empezar a aprender sobre SAML se debe leer primero la introducción a SAML, y después el documento SAMLOverview de OASIS.

Con anterioridad a SAML 1.1, *SAML* *1.0* fue adoptado como un estándar de OASIS en noviembre de 2002.  SAML ha experimentado una  actualización menor (V1.1) y una actualización importante (V2.0) desde la versión V1.0, que es un protocolo relativamente sencillo.  SAML 1.0 ha adquirido mayor importancia, sin embargo, desde que la Iniciativa de Autentificación del gobierno federal estadounidense ha adoptado SAML 1.0 cuando como su tecnología principal.

Las versiones 1.0 y 1.1 de SAML son similares.  Consulta SAMLDiff para ver las diferencias específicas entre los dos estándares.  Este artículo se centra en SAML 1.1 ya que es un estándar importante del que muchos otros estándares e implementaciones dependen.

**Aviso**: Los ejemplos de código de este artículo sirven sólo como ilustraciones y pueden no cumplir la norma. Para conocer los requerimientos de la normativa consultar las especificaciones de OASIS SAML .

 Aserciones de SAML 1.1
Las *aserciones de SAML* contienen *declaraciones* que los proveedores de servicio utilizan para tomar decisiones de control de acceso.  Por ejemplo, las *declaraciones de autenticación* confirman al proveedor de servicio que el rol principal se autenticó con el proveedor de identidad en un momento dado utilizando un método particular de autenticación.  La declaración de autenticación puede contener información adicional .  Por ejemplo, en la declaración de autenticación del ejemplo siguiente, la dirección de correo electrónico del rol principal es confirmada al proveedor de servicio:Una dirección de correo electrónico (como en el ejemplo superior) será suficiente en la mayoría de los casos.  En algunos casos, sin embargo, se requiere información adicional antes de que un proveedor de servicio pueda tomar una decisión de control de acceso.  Como ejemplo, supongamos que al alumnado se le permite acceder a los datos de las becas.  Una *declaración de atributo* puede indicar si el rol principal tiene una afiliación de "estudiante" o no, que usará el proveedor de servicio para permitir o denegar el acceso a la aplicación de las becas:Los atributos son a menudo obtenidos de un directorio LDAP, por lo tanto las representaciones consistentes de los atributos a través de dominios de seguridad es crucial.

En el ejemplo superior que muestra cómo un estudiante podría obtener acceso a una aplicación de becas, el proveedor de servicio tiene dos papeles, uno como *punto de aplicación de la norma* (*policy enforcement point*) y el otro como *punto de decisión de la norma* (*policy decision point*).  En ocasiones, es preferible asociar el punto de decisión de la norma al proveedor de identidad. En tal caso, el proveedor de servicio pasa un URI al proveedor de identidad, que entonces envía una *declaración de decisión de la autorización* que determina si el rol principal tiene o no acceso al recurso protegido en el URI facilitado.Los tres tipos de declaración no son mutuamente exclusivos.  Por ejemplo, tanto las declaraciones de autenticación como las declaraciones de atributo pueden ser incluidas en una única aserción (cómo se muestra en el ejemplo superior).  Esto evita que el proveedor de servicio tenga que realizar múltiples consultas del al proveedor de identidad.

El protocolo SAML es del tipo petición-respuesta.  Un *requester* de SAML  envía un elemento de Petición SAML a un responder:De igual modo, un responder SAML devuelve  un elemento de Respuesta SAML al *requester*:Las dependencias y los perfiles necesarios para este intercambio de mensajes son detallados en las siguientes secciones.

 Enlaces SAML 1.1
SAML 1.1 define formalmente un único protocolo de enlace, el enlace SAML SOAP.  Una implementación de SAML 1.1 debe implementar SAML sobre SOAP sobre HTTP (un protocolo  de enlace síncrono).  Otros mecanismos de transporte además de HTTP son permitidos, suponiendo que los aspectos independientes del protocolo del enlace SAML SOAP son   observados (see section 3.1.2 of SAMLBind).

El enlace SAML 1.1 SOAP está hecho sobre la versión 1.1 de SOAP (la  coincidencia en la numeración es pura coincidencia).  Un requester SAML envuelve un elemento SAML de tipo Petición en el cuerpo de un mensaje SOAP.  Similarmente, un *responder* SAML devuelve un  elemento SAML de tipo Respuesta en el cuerpo del mensaje SOAP devuelto.  En caso de cualquier error, el responder devuelve un código de error SOAP.

Cualquier *markup* SAML debe ser incluido in el cuerpo del mensaje SOAP.  SAML 1.1 no define ninguna cabecera  SOAP especifica para SAML.  Un requester puede insertar las cabeceras SOAP que desee (aunque no se requiere ninguna).

Recuerda que en SOAP 1.1, una cabecera HTTP SOAPAction  debe  ser incluida con cada petición HTTP (aunque su valor esté vacío).  Un requester SAML puede dar el valor siguiente a la cabecera SOAPAction:
  SOAPAction: http://www.oasis-open.org/committees/security
Sin embargo, un responder SAML no debe depender de este valor.

No se requiere una conexión segura para peticiones y respuestas SAML, pero en aquellas situaciones en las que la *integridad* y *confidencialidad* del mensaje sean necesarias, se requiere HTTP sobre SSL 3.0 o TLS 1.0 con un certificado del lado del servidor.

Un *requester* SAML puede devolver una respuesta "403" cuando quiera rechazar a un cierto *requester* de SAML. Un responder debe devolver una respuesta "Error Interno de Servidor 500" cuando haya un error SOAP (además se debe incluir un elemento de error SOAP). En cualquier otro caso, se devuelve una respuesta "200 OK", incluso en el caso de un error de procesado SAML. Tal respuesta incluirá un elemento SAML Status en el cuerpo del mensaje SOAP.

 Perfiles SAML 1.1
En general, los *perfiles* describen los casos de uso e intercambios de mensajes requeridos para en última instancia transferir aserciones de un proveedor de identidad a un proveedor de servicio.  SAML 1.1 especifica dos perfiles SSO para navegadores web:

 Perfil Browser/POST
 Perfil Browser/Artifact

El Perfil Browser/POST se basa en una operación "push" que pasa una aserción SSO *por valor* a través del navegador usando HTTP POST.  Decimos que el proveedor de identidad "pushes" la aserción al proveedor de servicio.

El Perfil Browser/Artifact emplea un mecanismo de  "pull". Básicamente el perfil envía una aserción SSO del proveedor de identidad al proveedor de servicio *por referencia* (a través del navegador que utiliza HTTP Redirect), el cual es posteriormente desreferenciado a través de un intercambio *back-channel* (por ejemplo, el proveedor de servicio "pulls" la aserción del proveedor de identidad utilizando SAML sobre SOAP sobre HTTP).

Estos perfiles soportan *single sign-on* (SSO) en distintos dominios.  La especificación no define perfiles adicionales.  En particular, SAML 1.1 no soporta un perfil para asegurar un mensaje de servicio web ni soporta un perfil de logout único.

Ambos perfiles SAML 1.1 empiezan en el servicio de transferencia interno del sitio web, que está gestionado por el proveedor de identidad.  La forma en la que el *principal* llega al servicio de transferencia en primer lugar no está indicada por la especificación. Para ver los escenarios posibles consultar las secciones 4.1 y 4.2 de SAMLOverview.  En la práctica, un cliente que accede a un recurso protegido en un proveedor de servicio será redirigido al servicio de transferencia interno del sitio en el proveedor de identidad, pero la secuencia precisa de pasos necesarios para cumplir esto no está indicada por SAML 1.1.  (Consultar la sección 4.3 de SAMLOverview para más información.)  Este escenario está exhaustivamente desarrollado en SAML 2.0.

Después de visitar el servicio de transferencia interno del sitio, el *principal* es transferido al *servicio de aserción del consumidor* en el proveedor de servicio.  Los detalles de cómo el *principal* es transferido del servicio de transferencia interno del sitio al *servicio de aserción del consumidor* dependen del perfil utilizado.  En el caso del Perfil Browser/Artifact, se usa una redirección; en el caso del Perfil Browser/POST Profile, el cliente emite una petición de tipo POST (con o sin intervención del usuario).

Para emitir un procesamiento por el servicio de aserción, se especifican dos URLs distintas:

 Assertion consumer URL (Perfil Browser/POST)
 Artifact Receiver URL (Perfil Browser/Artifact)

Estas y otras URLs pueden almacenarse en archivos de metadatos. La forma exacta en la que un proveedor de identidad obtiene un fichero confiable de metadatos, o determina las localizaciones confiables de un proveedor de servicios específico está fuera de las competencias  de SAML 1.1.

Notése que un proveedor de identidad SAML 1.1 debe proporcionar servicio de transferencia interno. Similarmente, un proveedor de servicio SAML 1.1 debe proporcionar un servicio de aserción del consumidor.

 Perfil Browser/POST
El perfil SAML 1.1 Browser/POST especifica los siguientes cuatro pasos.  La terminología utilizada en la especificación original ha sido modificada ligeramente para conformar a lo específico de la especificación SAML 2.0.

El flujo de mensaje empieza con una petición dirigida al proveedor de identidad.

 Petición del servicio de transferencia interno del sitio al proveedor de identidad
El *principal* (a través de un agente HTTP) solicita servicio de transferencia interno del sitio al proveedor de identidad:
  https://idp.example.org/TransferService?TARGET=target
donde *target* es el recurso solicitado al proveedor de servicio, por ejemplo, https://sp.example.com/home. En otras palabras, la siguiente petición GET está emitida por el agente usuario sobre SSL/TLS:El perfil no especifica cómo el URL al Servicio de Transferencia (con parámetro de TARGET) está obtenido por el agente de usuario.

 Responde con un formulario HTML
El servicio de transferencia interno del sitio devuelve un documento HTML que contiene un elemento FORM:donde el parámetro TARGET ha sido guardado del paso 1. El valor del parámetro SAMLResponse es la codificación base64 de un elemento SAML Response como el siguiente:La respuesta SAML debe ser digitalmente firmada por el proveedor de identidad.

Importante: se presupone que el *principal* ya ha establecido un contexto de seguridad en el proveedor de identidad, de otra manera el servicio de transferencia interno del sitio sería incapaz de proporcionar una declaración de autenticación en el elemento SAML Respuesta.

 Petición del Servicio de aserción del consumidor al proveedor de servicio
El agente usuario solicita el Servicio de aserción del consumidor al proveedor de servicio:donde los valores de los parámetros TARGET y SAMLResponse se obtienen del formulario HTML en el paso 2.

Nota: para automatizar el envío del formulario, la siguiente línea de Javascript puede aparecer en cualquier lugar de la página:Este código sólo funciona si existe un único elemento FORM (forms[0]) en la página.

 Respuesta a la petición del principal
El Servicio de aserción del consumidor consume el elemento SAML Respuesta, crea un contexto de seguridad en el proveedor de servicio y redirige el agente usuario al recurso objetivo.

 Perfil Browser/Artifact
El perfil SAML 1.1 Browser/Artifact especifica los seis siguientes pasos.  La terminología utilizada en la especificación original ha sido modificada ligeramente para conformar la especificación SAML 2.0.

El flujo del mensaje empieza con una petición dirigida al proveedor de identidad.

 Petición del servicio de transferencia interna del sitio al proveedor de identidad
El *principal* (a través de un agente usuario del HTTP) solicita el servicio de transferencia interna del sitio al proveedor de identidad:
  https://idp.example.org/transferservice?Objetivo=de OBJETIVO
donde el *target* es el recurso requerido  del proveedor de servicio, por ejemplo, https://sp.example.com/home.  En otras palabras, la siguiente petición GET es emitida por el agente usuario sobre SSL/TLS:El perfil no especifica cómo la URL al servicio de transferencia (con el parámetro TARGET) es obtenida por el agente usuario.

 Redirección al Servicio de aserción del consumidor
El *principal* es redirigido al Servicio de aserción del consumidor al proveedor de servicio, es decir, la siguiente respuesta es devuelta al agente usuario:donde *artifact* es una referencia a una aserción que el proveedor de identidad está dispuesto a proporcionar sobre una petición.

Importante: se asume que el *principal* ya ha establecido un contexto de seguridad en el proveedor de identidad, de otra manera el servicio de transferencia interno del sitio sería incapaz de proporcionar una declaración de autenticación.

 Petición del Servicio de aserción del consumidor al proveedor de servicio
El agente usuario solicita el servicio de aserción del consumidor al proveedor de servicio:
  https://sp.example.com/acs/artifact?Objetivo=de OBJETIVO&SAMLart=artefacto
donde el *target* y el *artifact* son como en los ejemplos previos.  En otras palabras, la siguiente petición GET es emitida por el agente usuario sobre SSL/TLS:

 Petición del Servicio de Resolución del Artefacto al proveedor de identidad
El Servicio de aserción del consumidor en el proveedor de servicio comienza un intercambio de canal de vuelta con el Servicio de resolución del artefacto en el proveedor de identidad.  Un mensaje SAML SOAP está enlazado a una petición HTTP POST:donde *artifact* ha sido previamente enviado del proveedor de identidad al proveedor de servicio en los pasos 2 y 3.

 Respuesta con una aserción SAML
El proveedor de identidad completa el intercambio de canal de vuelta respondiendo con una aserción SAML unida a un mensaje SAML SOAP:En este caso, la declaración de autenticación incluye un NameIdentifier conteniendo la dirección de correo electrónico del principal.

 Respuesta a la petición del principal
El Servicio de aserción del consumidor parsea el elemento SAML Respuesta, crea un contexto de seguridad en el proveedor de servicio y redirige el agente de usuario al recurso objetivo.

 Véase también

 SAML
 SAML 2.0
 Productos y servicios basados en SAML

 Referencias

  E. Maler et al., *Security and Privacy Considerations for the OASIS Security Assertion Markup Language (SAML) V1.1.* OASIS Standard, September 2003. Document ID oasis-sstc-saml-sec-consider-1.1 http://www.oasis-open.org/committees/download.php/3404/oasis-sstc-saml-sec-consider-1.1.pdf
  E. Maler et al., *Conformance Program Specification for the OASIS Security Assertion Markup Language (SAML) V1.1.* OASIS Standard, September 2003. Document ID oasis-sstc-saml-conform-1.1 http://www.oasis-open.org/committees/download.php/3402/oasis-sstc-saml-conform-1.1.pdf
  E. Maler et al., *Glossary for the OASIS Security Assertion Markup Language (SAML) V1.1.* OASIS Standard, September 2003. Document ID oasis-sstc-saml-glossary-1.1 http://www.oasis-open.org/committees/download.php/3401/oasis-sstc-saml-glossary-1.1.pdf
