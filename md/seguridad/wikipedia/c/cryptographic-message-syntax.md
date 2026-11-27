---
type: Artículo de enciclopedia
title: Cryptographic Message Syntax
description: El Cryptographic Message Syntax (CMS) es un estándar de la IETF para proteger mensajes criptográficamente.
resource: https://es.wikipedia.org/wiki/Cryptographic_Message_Syntax
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cryptographic_Message_Syntax"}
license: CC BY-SA 4.0
id: eswiki-Cryptographic_Message_Syntax
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cryptographic Message Syntax

El **Cryptographic Message Syntax** (CMS) es un estándar de la IETF para proteger mensajes criptográficamente. En él se definen las sintaxis para firmar digitalmente, realizar hash, realizar mac o para cifrar cualquier tipo de dato. CMS se basa en la sintaxis de PKCS#7, que a su vez se basa en el estándar Privacy-Enhanced Mail. La versión más moderna de CMS  se define en la RFC 5652 (ver también la RFC 5911 de módulos ASN.1 acordes al estándar ASN.1 2002).

CMS se construye alrededor del sistema de manejo de claves certificate-based así como el perfil definido por PKIX working group.

CMS se usa como el componente clave para muchos otros estándares criptográficos como S/MIME, PKCS#12 y el protocolo de sellado digital (RFC 3161).

OpenSSL es un software de código libre que permite cifrar, descifrar, firmar, verificar, comprimir y descomprimir documentos acordes a este estándar.
Normas y estándares
CMS está en constante desarrollo:
RFC 2315 - PKCS # 7 Versión 1.5 (obsoleto).
RFC 2630 - CMS 1.0, junio de 1999 (obsoleto).
RFC 3369 - CMS 2.0, agosto de 2002 (obsoleto).
RFC 3852 - CMS 3.0, julio de 2005 (obsoleto).
RFC 5652 - CMS 4.0, septiembre de 2009 (actual):
RFC 8933 : actualización del CMS para la protección de identificadores de algoritmos, octubre de 2020.

Véase también
 CAdES - CMS Advanced Electronic Signatures
 S/MIME
 PKCS #7

Enlaces externos
 Información sobre*System.Security.Cryptography.Pkcs*
Referencias
Jörg Schwenk: Seguridad y criptografía en Internet. Desde correo electrónico seguro hasta cifrado de IP. 2ª edición ampliada y mejorada. Vieweg + Teubner Verlag, Wiesbaden 2005,ISBN 3-8348-0042-2 (*Studium*).

  (Cryptographic Message Syntax (CMS), in use)
  (Cryptographic Message Syntax (CMS), obsolete)
  (Cryptographic Message Syntax (CMS), obsolete)
  (Cryptographic Message Syntax (CMS), obsolete)
  (Cryptographic Message Syntax, obsolete)
  (New ASN.1 Modules for Cryptographic Message Syntax (CMS) and S/MIME, in use)
  (New ASN.1 Modules for Cryptographic Message Syntax (CMS) and S/MIME, updated)
  (Using Elliptic Curve Cryptography with CMS, in use)
  (Use of Elliptic Curve Cryptography (ECC) Algorithms in Cryptographic Message Syntax (CMS), obsolete)
  (Using AES-CCM and AES-GCM Authenticated Encryption in the Cryptographic Message Syntax (CMS), in use)
