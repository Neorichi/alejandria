---
type: Artículo de enciclopedia
title: Certificado comodín
description: Un certificado comodín es un certificado de clave pública que se puede utilizar con varios subdominios de un dominio.
resource: https://es.wikipedia.org/wiki/Certificado_comodín
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Certificado_comodín"}
license: CC BY-SA 4.0
id: eswiki-Certificado_comodín
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Certificado comodín

Un **certificado comodín** es un certificado de clave pública que se puede utilizar con varios subdominios de un dominio.

Dependiendo del número de subdominios una ventaja podría ser que ahorra dinero y también podría ser más conveniente.

 Limitaciones
Solo un único nivel de subdominio es admitido.

No es posible conseguir un comodín para un certificado de validación extendida.

Una solución podría ser la de añadir cada nombre de host virtual en la extensión *Subject Alternative Name* (SAN), el principal problema es que el certificado tiene que ser reeditado siempre que se agregue un nuevo servidor virtual (ver *Seguridad de la capa de transporte § Soporte para servidores virtuales por nombre* para más información).

Los comodines se pueden añadir como dominios en los certificados multi-dominio o Certificados de Comunicaciones Unificadas (UCC). Además, los comodines en sí pueden tener extensiones *subjectAltName*, incluyendo otros comodines. Por ejemplo: El certificado comodín * .wikipedia.org tiene * .m.wikimedia.org como un nombre alternativo del sujeto. Por lo tanto, asegura https://www.wikipedia.org así como el nombre del sitio web completamente diferente https://meta.m.wikimedia.org.

RFC 6125 argumenta en contra de certificados comodín por motivos de seguridad.

 Ejemplo
En el caso de un certificado comodín para *.example.com, estos dominios serían válidos:
 payment.example.com
 contact.example.com
 login-secure.example.com
 www.example.com

Debido a que el comodín solo cubre un nivel de subdominios (el asterisco no coincide con puntos y aparte), estos dominios no serían válidos para el certificado:

 test.login.example.com

El dominio "desnudo" tampoco es válido (y hay que añadir por separado como un *SubjectAltName*):

 example.com

 Véase también
 Certificado de clave pública

 Referencias

 RFCs relevantes
