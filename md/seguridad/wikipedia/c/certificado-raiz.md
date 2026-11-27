---
type: Artículo de enciclopedia
title: Certificado raíz
description: En criptografía y seguridad informática, un certificado raíz es un certificado de clave pública sin firma o autofirmado que identifica la autoridad de certificación raíz.
resource: https://es.wikipedia.org/wiki/Certificado_raíz
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Certificado_raíz"}
license: CC BY-SA 4.0
id: eswiki-Certificado_raíz
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Certificado raíz

En criptografía y seguridad informática, un **certificado raíz** es un certificado de clave pública sin firma o autofirmado que identifica la autoridad de certificación raíz. Un certificado raíz forma parte de un esquema de infraestructura de clave pública. La variedad comercial más común está basada en el estándar ITU-T X.509, el cual normalmente incluye una firma digital de una autoridad de certificación.

Dicho de otra forma, un certificado raíz es un certificado emitido por la autoridad de certificación para sí misma. En este certificado consta la clave pública de la autoridad de certificación. Es el certificado origen de la cadena de confianza. Servirá al servidor web que lo incorpore para comprobar que el Certificado que le presenta un usuario está firmado por una autoridad de confianza, y por lo tanto es confiable.

Los certificados digitales están verificados utilizando una cadena de confianza. El ancla de confianza para el certificado digital es la «autoridad de certificación raíz».

Una autoridad de certificación puede emitir múltiples certificados en forma de estructura en árbol. Un certificado raíz se encuentra en lo más alto del árbol. La autoridad de certificación utilizará su clave privada para firmar los certificados que expide. Todos los certificados inmediatamente debajo del certificado raíz heredan la fiabilidad del certificado raíz. Una firma por un certificado raíz es similar a firmar ante notario una identidad en el mundo físico. Los certificados de más abajo en el árbol también dependen de la fiabilidad de los intermedios, a menudo conocidos como «autoridades de certificación subordinadas».

Muchas aplicaciones software asumen que estos certificados raíz son fidedignos en favor del usuario. Por ejemplo, un navegador web los utiliza para verificar identidades entre conexiones TLS seguras. Aun así, esto implica que el usuario confía en el editor de su navegador, las autoridades de certificado, y cualquiera de los certificados intermedios que éstas hayan podido emitir, confían en verificar fielmente la identidad e intenciones de todas las partes que poseen los certificados. Esta confianza (transitiva) en un certificado raíz es el caso habitual y está integrado en el modelo de cadena de certificados X.509.

El certificado raíz está normalmente fidedignamente hecho por algún mecanismo que no sea un certificado, como por una distribución física segura. Por ejemplo, algunos de los certificados raíz más conocidos están distribuidos en los navegadores de Internet por sus fabricantes. Microsoft distribuye certificados raíz, que pertenecen a miembros del Programa de Certificados Raíz de Microsoft, a aplicaciones de escritorio de Windows y a Windows Phone 8.

 Véase también
 Autoridad de certificación
 Cacert.org
 Comodo
 SHA-1
 Protocolo de estado de certificado en línea
 Datación (en inglés *timestamping*)
 Datación confiable
 Autoridad de datación cualificada
 Vamos a cifrar
 Verisign

 Referencias

 Enlaces externos
 Windows y Windows Phone 8 SSL Programa de Certificado de la Raíz (Miembro CAs). "Windows and Windows Phone 8 SSL Root Certificate Program (Member CAs) "
 iOS 8: Lista de certificados de raíz confiados en disponibles. "iOS 8: List of available trusted root certificates"
