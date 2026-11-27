---
type: Artículo de enciclopedia
title: Criptografía híbrida
description: La criptografía híbrida es un método criptográfico que usa tanto un cifrado simétrico como un asimétrico.
resource: https://es.wikipedia.org/wiki/Criptografía_híbrida
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_híbrida"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_híbrida
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía híbrida

La **criptografía híbrida** es un método criptográfico que usa tanto un cifrado simétrico como un asimétrico. Emplea el cifrado de clave pública para compartir una clave para el cifrado simétrico. El mensaje que se esté enviando en el momento, se cifra usando su propia clave privada, luego el mensaje cifrado se envía  al destinatario. Ya que compartir una clave simétrica no es seguro, ésta es diferente para cada sesión.

 Ejemplo
Tanto PGP como GnuPG usan sistemas de cifrado híbridos. La clave de sesión (clave simétrica) es cifrada con la clave pública del destinatario, y el mensaje saliente es cifrado con la clave simétrica, todo combinado automáticamente en un solo paquete. El destinatario usa su clave privada para descifrar la clave de sesión (clave simétrica) y acto seguido usa ésta para descifrar el mensaje.

Un sistema de cifrado híbrido no es más fuerte que el de cifrado asimétrico o el de cifrado simétrico de los que hace uso, independientemente de cuál sea más débil. En PGP y GnuPG el sistema de clave simétrica es probablemente la parte más débil de la combinación. Sin embargo, si un atacante pudiera descifrar una clave de sesión, sólo sería útil para poder leer un mensaje, el cifrado con esa clave de sesión. El atacante tendría que volver a empezar y descifrar otra clave de sesión para poder leer cualquier otro mensaje.

Referencias
 Adaptado de la Guía de "Gnu Privacy Guard"
