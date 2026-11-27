---
type: Artículo de enciclopedia
title: S/MIME
description: "S/MIME (Secure / Multipurpose Internet Mail Extensions, del inglés, Extensiones de Correo de Internet de Propósitos Múltiples / Seguro) es un estándar para criptografía de clave pública y firmado de correo electrónico …"
resource: https://es.wikipedia.org/wiki/S/MIME
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/S/MIME"}
license: CC BY-SA 4.0
id: eswiki-S/MIME
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# S/MIME

**S/MIME** (**Secure / Multipurpose Internet Mail Extensions**, del inglés, *Extensiones de Correo de Internet de Propósitos Múltiples / Seguro*) es un estándar para criptografía de clave pública y firmado de correo electrónico encapsulado en MIME.

 Historia
S/MIME fue desarrollado originalmente por RSA. La especificación original usó la especificación MIME de IETF recientemente desarrollada con el estándar de facto de mensaje seguro PKCS #7.

 Función
S/MIME provee los siguientes servicios de seguridad criptográfica para aplicaciones de mensajería electrónica:
 autenticación, integridad y no repudio (mediante el uso de firma digital) y
 privacidad y seguridad de los datos (mediante el uso de cifrado)

S/MIME especifica el tipo application/pkcs7-mime (tipo smime "enveloped-data") para envoltura de datos (cifrado): la entidad MIME completa a ser envuelta se cifra y se empaca en un objeto que luego se inserta en una entidad MIME application/pkcs7-mime.

La funcionalidad S/MIME está construida en la mayoría de apps de correo electrónico modernos y son capaces de interoperar entre ellos. Un correo firmado tiene estos encabezados ocultos (visibles en "Ver código fuente del mensaje")

 Content-Type: multipart/signed; protocol="application/pkcs7-signature"; micalg=sha1; boundary=""
 This is a cryptographically signed message in MIME format.
 [Texto del correo]
 Content-Type: application/pkcs7-signature; name="smime.p7s"
 Content-Transfer-Encoding: base64
 Content-Disposition: archivo adjunto; filename="smime.p7s"
 Content-Description: Firma criptográfica S/MIME

Correo Cifrado

 Content-Type: application/pkcs7-mime; name="smime.p7m"; smime-type=enveloped-data
 Content-Transfer-Encoding: base64
 Content-Disposition: archivo adjunto; filename="smime.p7m"
 Content-Description: Mensaje cifrado S/MIME
 [Número y letras aleatorios]
 Certificados S/MIME
Antes de que S/MIME pueda usarse en alguna de las aplicaciones antes mencionadas, se debe obtener e instalar una clave/certificado individual tanto de la autoridad certificadora (AC) interna como de una AC pública. Una buena práctica es usar claves privadas separadas (y certificados asociados) para firma y para cifrado.

Limitaciones

S/MIME solo puede funcionar apropiadamente con aplicaciones y programas instalables de correo electrónico que almacenan información acerca del PKCS con sus respectivas claves públicas y privadas, servicio de correo electrónico basado en páginas web y apps para móviles no pueden usar mensajes firmados y puede limitarse a mostrar un correo electrónico vacío con un adjunto smime.p7s (el cual contiene realmente el mensaje)

 Véase también
 MIME (Multipurpose Internet Mail Extensions)
 TLS (Transport Layer Security), inicialmente SSL
 Pretty Good Privacy (PGP)
 GPG

 Enlaces externos
 Boletín del grupo de trabajo de S/MIME — tiene enlaces a RFCs relacionadas con S/MIME y borradores de Internet
 Cómo falsificar una firma S/MIME — crítica a algunas implementaciones de S/MIME
 Grupo de trabajo de S/MIME de IETF
 S/MIME y OpenPGP
 Test de compatibilidad de S/MIME con clientes de correo electrónico
 Directorio público de VeriSign (ldap://directory.verisign.com)
 MozillaZine Knowledge Base: Adquiriendo un certificado S/MIME

 Safelayer Secure Communications, implementación comercial
 How to secure email using S/MIME standard
