---
type: Artículo de enciclopedia
title: Online Certificate Status Protocol
description: "Online Certificate Status Protocol («Protocolo de Verificación de Certificados en Línea»), conocido simplemente como OCSP, es un método para determinar el estado de vigencia de un certificado digital X.509 usando otros …"
resource: https://es.wikipedia.org/wiki/Online_Certificate_Status_Protocol
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Online_Certificate_Status_Protocol"}
license: CC BY-SA 4.0
id: eswiki-Online_Certificate_Status_Protocol
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Online Certificate Status Protocol

**Online Certificate Status Protocol** («Protocolo de Verificación de Certificados en Línea»), conocido simplemente como **OCSP**, es un método para determinar el estado de vigencia de un certificado digital X.509 usando otros medios que no sean el uso de CRL (Certificate Revocation List, «Listas de Revocación de Certificados»). Este protocolo se describe en el RFC 6960 y está en el registro de estándares de Internet.

Los mensajes OCSP se codifican en ASN.1 y habitualmente se transmiten sobre el protocolo HTTP. La naturaleza de las peticiones y respuestas de OCSP hace que a los servidores OCSP se les conozca como "OCSP responders".

 Ventajas sobre las CRL
OCSP fue creado para solventar ciertas deficiencias de las CRL. Cuando se despliega una infraestructura de clave pública (PKI, por sus siglas en inglés), es preferible la validación de los certificados mediante OCSP sobre el uso de CRL por varias razones:
 OCSP puede proporcionar una información más adecuada y reciente del estado de revocación de un certificado.
 OCSP elimina la necesidad de que los clientes tengan que obtener y procesar las CRL, ahorrando de este modo tráfico de red y procesado por parte del cliente.
 El contenido de las CRL puede considerarse información sensible, análogamente a la lista de morosos de un banco.
 Una "respuesta OCSP" puede requerir de un pago por parte de la entidad que lo consulta.
 OCSP soporta el encadenamiento de confianza de las peticiones OCSP entre los "responders". Esto permite que los clientes se comuniquen con un "responder" de confianza para lanzar una petición a una autoridad de certificación alternativa dentro de la misma PKI.
 Una consulta sobre el estado de un certificado sobre una CRL, debe recorrerla completa secuencialmente para decir si es válido o no. Un "OCSP responder" en el fondo, usa un motor de base de datos para consultar el estado del certificado solicitado, con todas las ventajas y estructura para facilitar las consultas. Esto se manifiesta aún más cuando el tamaño de la CRL es muy grande.

 Comparación de eficiencia CRL versus OCSP
Una diferencia importante entre CRL y OCSP, es que una CRL puede ser almacenada temporalmente para hacer consultas locales, en cambio para usar OCSP se requiere de conexión en el momento de la consulta. Si bien la CRL está disponible sin conexión, mientras más tiempo esté sin actualizarse, se hace menos confiable la información que nos brinde, porque pueden haberse revocado algunos certificados entre actualizaciones.

Esto da lugar a una diferencia en la eficiencia del uso del ancho de banda para efectos exclusivos de consultas por estado de certificados.

 Con respecto al ancho de banda y al tiempo de validación
Si se considera que se usa una CRL almacenada por un tiempo para ser consultada, versus el ancho de banda que se usa por cada consulta a través de OCSP, existe una diferencia de uso de ancho de banda que crece mientras aumenta el número de validaciones por día que debe responder la Autoridad Certificadora. Con CRL, el ancho de banda usado sigue una curva logarítmica, por el hecho de que aunque aumenten las consultas diarias, estas se hacen a la CRL almacenada. En cambio, con OCSP, si las consultas aumentan necesariamente aumenta el ancho de banda usado, por lo que la curva resultante es lineal. Debido a esto, el tiempo de validación, a pesar de seguir la misma curva, al aumentar las validaciones por día, usando CRL, el tiempo "límite" es menor al que se obtiene si se usa OCSP.

 Con respecto al número de usuarios
Si se aumenta el número de usuarios, al igual que en el caso anterior, en algún punto CRL supera a OCSP en cuanto al ancho de banda necesario para soportar la cantidad de consultas que se hacen.

 Implementación básica de una PKI
 Juan y Pedro tienen certificados de clave pública emitidos por Iván.
 Juan desea efectuar una transacción con Pedro y le envía su certificado de clave pública.
 Pedro, consciente de que la clave privada de Juan pudiera haber sido comprometida, crea una petición OCSP que contiene una huella de la llave pública de Juan y se la manda a Iván, que es la autoridad de validación (VA).
 El "OCSP responder" de Iván busca el estado de revocación del certificado de Juan (usando la huella que creó Pedro como clave) en su propia base de datos de CA. Si la clave privada de Juan ha sido comprometida, esta será la única localización de confianza donde ese hecho será registrado.
 El "OCSP responder" de Iván confirma que el certificado de Juan es correcto, y devuelve una respuesta OCSP de éxito firmada a Pedro para comunicárselo.
 Pedro verifica criptográficamente la respuesta firmada (Pedro tiene la clave pública de Iván a mano, puesto que Iván es un "responder" de confianza) y se asegura de que dicha respuesta fue creada recientemente.
 Pedro completa la transacción con Juan.

 Detalles del protocolo
El protocolo OCSP está especificado en el RFC 2560. En ella se definen las características que debe cumplir un servidor OCSP, así como el formato tanto de la petición como de la respuesta. Ambas estructuras de datos se representan según la sintaxis ASN.1.

Una petición de OCSP básicamente está compuesta por la versión del protocolo y los identificadores de los certificados que se quiere que sean validados. Este identificador está formado por el número de serie, el hash del Distinguished Name (DN) del emisor del certificado y el hash de la clave pública del mismo. En una petición se pueden solicitar la consulta del estado de varios certificados, incluso pertenecientes a diferentes CA. La firma de la petición es opcional y depende de lo que decida la Autoridad de Validación OCSP.

Un "responder" OCSP puede devolver una respuesta firmada, lo cual significaría que el certificado indicado en la petición es "bueno" (*good*), "revocado" (*revoked*) o "desconocido" (*unknown*). Estas respuestas serán para cada uno de los certificados de los que se ha solicitado la consulta. También puede devolver un código de error, en cuyo caso la respuesta no tendría que estar firmada.

Desafortunadamente, el borrador de la primera versión de OCSP (OCSP v.1) es ambigua en el sentido de "desconocido". Podría significar que el sujeto que figura del certificado es desconocido, o que lo que es desconocido es el *estado de revocación* del certificado.

El formato de petición OCSP soporta extensiones adicionales. Esto permite una adaptación y configuración más extensas a un esquema de PKI en concreto.

 Implementaciones
Se pueden encontrar implementaciones del protocolo OCSP en:
 *Netscape Certificate Management System* de AOL
 *KeyTools* de Baltimore Technologies
 *eTrust OCSPro* de Computer Associates
 *GemSAFE eSigner* de GemPlus
 *TrustPlatform* de Kyberpass
 *Network Security Services* de Mozilla
 *SiteMinder* de Netegrity
 Toolkit OpenSSL
 *Keon Certificate Authority* de RSA
 *Sun ONE Identity Server* de Sun Microsystems
 *Valicert Validation Authority* de Tumbleweed Communications
 *Validation Authority* de Valicert
 *KeyOne VA* de Safelayer
 ''EJBCA
 *Plataforma de firma electrónica @firma (Ministerio Administraciones Públicas - España)*

 Referencias

 Enlaces externos
 OpenValidation tiene una visión detallada del mercado, información de interoperabilidad y recursos de desarrollo relacionados con la validación en línea.
 Safelayer Demo Suite, servidor OCSP de demostración.
 ADSS OCSP Server, Línea de Certificado de Verificación de estado (OCSP).
