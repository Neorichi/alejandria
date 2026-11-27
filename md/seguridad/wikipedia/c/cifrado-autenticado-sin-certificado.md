---
type: Artículo de enciclopedia
title: Cifrado autenticado sin certificado
description: Certificate-Less Authenticated Encryption (CLAE), de sus siglas en inglés, agrega autenticación al cifrado denominado como Criptografía basada en identidad.
resource: https://es.wikipedia.org/wiki/Cifrado_autenticado_sin_certificado
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Cifrado_autenticado_sin_certificado"}
license: CC BY-SA 4.0
id: eswiki-Cifrado_autenticado_sin_certificado
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Cifrado autenticado sin certificado

**Certificate-Less Authenticated Encryption** (CLAE), de sus siglas en inglés, agrega autenticación al cifrado denominado como Criptografía basada en identidad. Es un algoritmo de cifrado asimétrico que puede intercambiar datos de forma segura entre dos entidades sin necesidad de administrar (centralmente) las claves.

Centro de confianza (Trusted center)
El usuario tendrá la capacidad de registrarse a sí mismo en el centro de confianza mediante la primera autenticación en dicho centro de confianza. De esta forma, el centro de confianza generará una clave privada TC que distribuirá al usuario.

La confianza del usuario en el centro de confianza (de terceros de confianza) incluye:
 Proceso de autenticación del receptor adecuado.
 Después de que la clave privada se distribuya al usuario, dicha clave privada no es regenerada por el centro de confianza para otros fines (espionaje).
 La clave privada TC está bien protegida y la clave pública TC distribuida pertenece al centro de confianza.

Unión (Joining)
El usuario (emisor/receptor) se une mediante la adquisición de una clave privada de un tercero de confianza o centro de confianza (TC). El receptor se registra con el centro de confianza mediante la primera autenticación con el TC. La autenticación puede ser algo similar a un sistema de contraseñas habitual o alguna pregunta de seguridad (Kerberos, correo electrónico, número de teléfono, etc.), la autenticación biométrica, etc. El TC genera una clave privada utilizando su propia clave pública y la identidad del usuario que se une. La clave privada se transmite de forma segura al usuario que se une.

Emisor
El emisor utiliza la identidad del receptor y la clave pública del TC para generar localmente la clave pública del receptor. El emisor puede elegir cualquier TC, forzando así al receptor a adquirir su (otra) clave privada de ese TC.

Receptor
Una vez que el receptor se ha unido, puede descifrar el mensaje ya recibido.
Al responder a un mensaje, el emisor se convierte en el receptor y viceversa.

Comparación
Normalmente se debe generar un par de claves pública/privada y distribuir la clave pública antes de que se puedan enviar o recibir mensajes de forma segura. En el caso de los mensajes CLAE ya pueden ser enviados con la clave pública, antes de que se genere la clave privada. La clave pública de cualquier destinatario ya puede ser adquirida de un centro de confianza, antes de que el destinatario se haya registrado.

Véase también
Certificateless cryptography

Referencias
