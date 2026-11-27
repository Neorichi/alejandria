---
type: Artículo de enciclopedia
title: Token de software
description: Un token de software (también conocido como soft token) es un mecanismo de seguridad de autenticación de dos factores que puede usarse para autorizar el uso o acceso de servicios informáticos.
resource: https://es.wikipedia.org/wiki/Token_de_software
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Token_de_software"}
license: CC BY-SA 4.0
id: eswiki-Token_de_software
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Token de software

Un *token de software* (también conocido como *soft token*) es un mecanismo de seguridad de autenticación de dos factores que puede usarse para autorizar el uso o acceso de servicios informáticos. Los tokens de software son almacenados en un dispositivo electrónico de uso general, como una computadora de escritorio, computadora portátil, PDA o teléfono móvil, y pueden duplicarse. (En contraste los tokens de hardware, donde las credenciales son almacenanadas en un dispositivo de hardware dedicado y por lo tanto, no pueden duplicarse (esto significa ausencia de invasión física del dispositivo).

Ya que los tokens de software, son algo que no se posee físicamente, están expuestos a amenazas únicas basadas en la duplicación del material criptográfico subyacente, por ejemplo, virus informáticos y ataques de software. Tanto tokens de hardware como los de software son vulnerables a ataques man-in-the-middle basados en bot, o a ataques simples de phishing en los que se solicita la contraseña de un solo uso, proporcionada por el token, y luego se proporciona al sitio web genuino de manera oportuna. Los tokens de software tienen beneficios: no hay tokens físicos para transportar, no contienen baterías que se agoten y son más baratos que los tokens de hardware.

 Arquitectura de seguridad
Existen dos arquitecturas principales para los tokens de software: secreto compartido y criptografía de clave pública.

Para un secreto compartido, un administrador generalmente, generará un archivo de configuración para cada usuario final. El archivo deberá contener un nombre de usuario, un número de identificación personal y el secreto. Este archivo de configuración se le entrega al usuario.

La arquitectura secreta compartida es potencialmente vulnerable en varias áreas. El archivo de configuración puede verse comprometido si es robado y se copia el token. Con los tokens de software basados en el tiempo, es posible tomar prestada la PDA o computadora portátil de un individuo, adelantar el reloj y generar códigos que serán válidos en el futuro. Cualquier token de software que use secretos compartidos y almacene el PIN junto con el secreto compartido en un cliente de software puede ser robado y sujeto a ataques fuera de línea. Los tokens secretos compartidos pueden ser difíciles de distribuir, ya que cada token es esencialmente una pieza diferente de software. Cada usuario debe recibir una copia del secreto, que puede crear limitaciones de tiempo.

Algunos tokens de software más nuevos se basan en criptografía de clave pública o criptografía asimétrica. Esta arquitectura elimina algunas de las debilidades tradicionales de los tokens de software, pero no afecta su debilidad primaria (capacidad de duplicar). Existe la posibilidad de almacenar un PIN en un servidor de autenticación remoto, en lugar de hacerlo con el cliente de tokens, por lo que un token de software robado no sirve a menos que también se conozca el PIN. Sin embargo, en el caso de una infección por virus, el material criptográfico se puede duplicar y luego se puede capturar el PIN (mediante el registro de teclas o similar) la próxima vez que el usuario se autentique. Si se intenta adivinar el PIN, se puede detectar e iniciar sesión en el servidor de autenticación, que puede desactivar el token. El uso de la criptografía asimétrica también simplifica la implementación, ya que el cliente de token puede generar su propio par de claves e intercambiar claves públicas con el servidor.

 Véase también

 Autenticación
 Autenticación electrónica
 Autenticador de Google
 Autenticación multifactor
 Token de seguridad

 Referencias

 Enlaces externos

 Microsoft to abandon passwords,
 Banks to Use 2-factor Authentication by End of 2006
