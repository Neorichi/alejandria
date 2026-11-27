---
type: Artículo de enciclopedia
title: Pretty Good Privacy
description: "Pretty Good Privacy (PGP privacidad bastante buena) es un programa desarrollado por Phil Zimmermann y cuya finalidad es proteger la información distribuida a través de Internet mediante el uso de criptografía de clave …"
resource: https://es.wikipedia.org/wiki/Pretty_Good_Privacy
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Pretty_Good_Privacy"}
license: CC BY-SA 4.0
id: eswiki-Pretty_Good_Privacy
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Pretty Good Privacy

**Pretty Good Privacy** (**PGP** *privacidad bastante buena*) es un programa desarrollado por Phil Zimmermann y cuya finalidad es proteger la información distribuida a través de Internet mediante el uso de criptografía de clave pública, así como facilitar la autenticación de documentos gracias a firmas digitales.

PGP originalmente fue diseñado y desarrollado por Phil Zimmermann en 1991. El nombre está inspirado en uno de los patrocinantes ficticios (*Ralph's Pretty Good Grocery*, de la ciudad imaginaria *Lake Wobegon*), inventados por el locutor Garrison Keillor para el programa de radio semanal *A Prairie Home Companion* en Minesota, EE.UU.

 Funcionamiento

PGP es un criptosistema híbrido que combina técnicas de criptografía simétrica y criptografía asimétrica. Esta combinación permite aprovechar lo mejor de cada uno: El cifrado simétrico es más rápido que el asimétrico o de clave pública, mientras que este, a su vez, proporciona una solución al problema de la distribución de claves en forma segura y garantiza el no repudio de los datos y la no suplantación.

Cuando un usuario emplea PGP para cifrar un texto en claro, dicho texto es comprimido. La compresión de los datos ahorra espacio en disco, tiempos de transmisión y, más importante aún, fortalece la seguridad criptográfica, ya que la mayoría de las técnicas de criptoanálisis buscan patrones presentes en el texto claro para romper el cifrado. La compresión reduce esos patrones en el texto claro, aumentando enormemente la resistencia al criptoanálisis.

Después de comprimir el texto, PGP crea una clave de sesión secreta que solo se empleará una vez. Esta clave es un número aleatorio generado a partir de los movimientos del ratón y las teclas que se pulsen durante unos segundos con el propósito específico de generar esta clave (el programa nos pedirá que los realicemos cuando sea necesario), también puede combinarlo con la clave anteriormente generada.  Esta clave de sesión se usa con un algoritmo simétrico (IDEA, Triple DES) para cifrar el texto claro.

Una vez que los datos se encuentran cifrados, la clave de sesión se cifra con la clave pública del receptor (criptografía asimétrica) y se adjunta al texto cifrado, y el conjunto es enviado al receptor.

El descifrado sigue el proceso inverso. El receptor usa su clave privada para recuperar la clave de sesión, simétrica, que PGP luego usa para descifrar los datos.

Las claves empleadas en el cifrado asimétrica se guardan cifradas protegidas por contraseña en el disco duro. PGP guarda dichas claves en dos archivos separados llamados *llaveros*, uno para las claves públicas y otro para las claves privadas.

 PGP como estándar de Internet

La Internet Engineering Task Force se ha basado en el diseño de PGP para crear el estándar de Internet OpenPGP. Las últimas versiones de PGP son conformes o compatibles en mayor o menor medida con ese estándar. La compatibilidad entre versiones de PGP y la historia del esfuerzo por estandarizar OpenPGP, se tratan a continuación.

 Firmas digitales

PGP ofrece autenticación de mensajes y la comprobación de su integridad. Esta última es usada para descubrir si un mensaje ha sido cambiado luego de ser completado (la propiedad de integridad del mensaje), y la anterior para determinar si realmente fue enviado por la persona/entidad que reclama ser el remitente (una firma digital). En PGP, estas operaciones son usadas por defecto junto con la codificación o cifrado del mensaje, pero pueden ser aplicadas a texto simple también. El remitente usa PGP para crear una firma digital para el mensaje con algoritmos de firma RSA o DSA. Para hacer esto, PGP calcula un condensado (también llamado resumen o - en inglés - "hash" del mensaje) del texto simple, y luego crea la firma digital de aquel condensado usando las llaves privadas del remitente.

 Red o web de confianza
Tanto codificando mensajes como verificando firmas, es crucial que la clave pública enviada a alguien o alguna entidad realmente 'pertenezca' al destinatario intencionado. Simplemente el hecho de descargar una llave pública de algún sitio perteneciente a una asociación no nos asegura que podamos confiar en dicha asociación. El PGP tiene, desde sus primeras versiones, provisiones siempre incluidas para distribuir las llaves públicas de un usuario en 'un certificado de identidad' que es construido usando criptografía asegurando de esta manera que cualquier tergiversación sea fácilmente detectable. Pero simplemente la fabricación de un certificado que es imposible modificar sin ser descubierto con eficacia es también insuficiente. Esto puede impedir la corrupción solo después de que el certificado ha sido creado, no antes. Los usuarios también deben asegurar por algunos medios que la llave pública en un certificado realmente pertenece a la persona/entidad que lo reclama. Desde su primera publicación, los productos de PGP han incluido un certificado interno 'examen del esquema' para asistir junto a este; un modelo de confianza que ha sido llamado una web de confianza. Una llave pública dada (o más expresamente, información que liga un nombre de usuario a una llave) puede ser digitalmente firmada por un usuario tercero para dar testimonio a la asociación entre alguien (realmente un nombre de usuario) y la llave. Hay varios niveles de confianza que pueden ser incluidos en tales firmas.
Aunque muchos programas lean y escriban esta información, pocos (si alguno) incluyen este nivel de certificación calculando si hay que confiar en una llave.
La web del protocolo de confianza fue descrita por Zimmermann en 1992 en el manual para la versión 2.0 PGP:

 OpenPGP
En PGP Inc. estaban preocupados por el tema de las patentes. RSADSI no estaba de acuerdo con que al recién creado PGP Inc. mantuviese la licencia de Viacrypt RSA. La compañía adoptó un nuevo estándar "Unencumbered PGP": "use no algorithm with licensing difficulties" (Uso de estándares que no acarreen problemas de licencia). Debido a la importancia mundial del sistema de cifrado PGP (era tenido como el más ampliamente escogido entre los sistemas de cifrado), muchos querían desarrollar su propio software que trabajase junto con PGP 5. Zimmermann entendió que un estándar libre para el cifrado PGP era imprescindible para la comunidad criptográfica. El 19 de julio de 1997, PGP Inc. propuso a IETF un estándar llamado OpenPGP. Le dieron permiso a IETF para usar este nombre que describiría tanto a este nuevo estándar como a cualquier programa que tenga soporte para este. IETF aceptó la proposición y empezó OpenPGP Working Group.

OpenPGP está en Internet Standards Track y está en desarrollo. Bastantes clientes de correo electrónico ofrecen seguridad compatible con OpenPGP tal y como se describe en RFC 3156. La especificación actual es la RFC 4880 (noviembre de 2007), el sucesor de RFC 2440. RFC 4880 especifica una serie de algoritmos necesarios que consisten en ElGamal encryption, DSA, Triple DES y SHA-1. Además de estos, El estándar recomienda RSA como se describe en PKCS #1 v1.5 para cifrado y firmado, así como AES-128, CAST-128 e IDEA. Pero estos no son los únicos soportados, muchos otros también lo están. El estándar se amplió para dar soporte a Camellia (cipher) por RFC 5581 en 2009, y cifrado basado en criptografía de curva elíptica (ECDSA, ECDH) por RFC 6637 en 2012. Soporte para EdDSA será añadido por propuesto en 2014.

La Free Software Foundation financia el desarrollado de un paquete GNU compatible con OpenPGP llamado GNU Privacy Guard (abreviado GnuPG or GPG). GnuPG es libre y tiene disponible todo su código fuente bajo la licencia GNU General Public License (GPL) y tiene soporte para múltiples interfaces de usuario (GUIs) que interactúan con la librería GnuPG para opciones de cifrado, descifrado y firma (KGPG, Seahorse, MacGPG). Muchos otros han desarrollado también su propio sistema de compatibilidad.

Hay varias aplicaciones compatibles con OpenPGP tanto para iOS como para Android, como puede ser iPGMail para el caso de iOS y OpenKeychain para Android, que habilitan la generación de claves y el cifrado/descifrado de correos electrónicos y archivos en Apple's iOS y Android.

 PGP
 RFC 1991 PGP Message Exchange Formats (obsoleto)
 OpenPGP
 RFC 2440 OpenPGP Message Format (obsoleto)
 RFC 4880 OpenPGP Message Format
 RFC 5581 The Camellia Cipher in OpenPGP
 RFC 6637 Elliptic Curve Cryptography (ECC) in OpenPGP
draft-koch-eddsa-for-openpgp EdDSA for OpenPGP
 PGP/MIME
 RFC 2015 MIME Security with Pretty Good Privacy (PGP)
 RFC 3156 MIME Security with OpenPGP

El cifrado OpenPGP permite el envío seguro de archivos y mensajes, así como ofrecer la verificación de quién escribió el mensaje usando un proceso llamado firma digital. El uso de OpenPGP para comunicación requiere la participación de los dos (el emisor y el receptor). OpenPGP también puede ser usado para asegurar archivos sensibles cuando están almacenados en sitios vulnerables, como dispositivos móviles o la nube.

 Véase también
 GNU Privacy Guard (GPG)
 Mailfence

 Referencias

 Enlaces externos
 The International PGP Home Page
 The Open PGP Home Page
 Historia del PGP. - Introducción del libro *PGP & GPG: Email for the Practical Paranoid*. Lucas, M. (2006). San Francisco: No Starch Press .
