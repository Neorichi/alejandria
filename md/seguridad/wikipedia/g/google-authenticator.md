---
type: Artículo de enciclopedia
title: Google Authenticator
description: Google Authenticator es un software basado en autenticación con contraseña de un solo uso desarrollado por Google.
resource: https://es.wikipedia.org/wiki/Google_Authenticator
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Google_Authenticator"}
license: CC BY-SA 4.0
id: eswiki-Google_Authenticator
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Google Authenticator

**Google Authenticator** es un software basado en autenticación con contraseña de un solo uso desarrollado por Google. Google Authenticator ofrece un número de seis dígitos que el usuario debe proporcionar además de su nombre de usuario y contraseña para acceder a los servicios de Google. Google Authenticator puede también generar códigos para aplicaciones de terceras partes, tales como gestores de contraseñas o servicios de alojamiento de archivos.

 Implementaciones
Google ofrece versiones de Google Authenticator para Android, BlackBerry y iOS.

Existen también varias implementaciones de terceras partes;
 Windows Phone 7.5/8: Authenticator Virtual TokenFactor
 Windows Mobile: Google Authenticator for Windows Mobile
 Java CLI: Authenticator.jar
 Java GUI: JAuth
 J2ME: gauthj2me lwuitgauthj2me Mobile-OTP (chinese only) totp-me
 PalmOS: gauthj2me
 Python: onetimepass
 PHP: GoogleAuthenticator.php
 Ruby: google_authenticator_auth gem (third party implementation)
 Rails: active_model_otp (third party implementation)
 webOS: GAuth
 Windows: gauth4win MOS Authenticator
 .NET: TwoStepsAuthenticator
 HTML5: html5-google-authenticator
 MeeGo/Harmattan (Nokia N9): GAuth
 Apache: Google Authenticator Apache Module
 PAM: Google Pluggable Authentication Module oauth-pam
 Web Browser Online : Yashvasin Authenticator

 Descripción técnica
Google Authenticator incluye implementaciones para la generación de códigos de autenticación con contraseña de un solo uso destinado a varias plataformas móviles, así como un módulo de autenticación (PAM) conectable. Los códigos One-time son generados haciendo uso de estándares abiertos desarrollados por The Initiative for Open Authentication (OATH) (no guarda relación con OAuth).

Estas implementaciones soportan el algoritmo HMAC-Based One-time Password (HOTP) especificado en la RFC 4226 y el algoritmo Time-based One-time Password (TOTP) especificado en la RFC 6238.

El proveedor de servicio genera una clave secreta de 80 bits para cada usuario. Esta se suministra como una cadena de 16 caracteres codificados en base32 o como un QR code. El cliente crea un mensaje HMAC-SHA1 usando esta clave secreta. El mensaje así generado puede estar basado en;

 El número de periodos de 30 segundos transcurridos desde Unix epoch; o
 El contador que es incrementado con cada nuevo código.

Una porción de la HMAC se extrae y es convertida a un código de 6 dígitos.

 Pseudo código para Time OTP

  function **GoogleAuthenticatorCode**(*string* secret)
      key := base32decode(secret)
      message := current Unix time ÷ 30
      hash := **HMAC-SHA1**(key, message)
      offset := last nibble of hash
      truncatedHash := hash[offset..offset+3]  //4 bytes starting at the offset
      Set the first bit of truncatedHash to zero  //remove the most significant bit
      code := truncatedHash **mod** 1000000
      **pad** code with 0 until length of code is 6
      **return** code

 Pseudo código para Event/Counter OTP

 Uso
Google Authenticator puede ser usado entre otros con las siguientes aplicaciones y websites:

 LastPass Password Manager
 Amazon.com
 Facebook.com
 Hotmail.com
 MercadoLibre.com
 Binance.com

 Referencias

 Enlaces externos
  en playstore
 google-authenticator - Two-step verification en Google Code
 Google Authenticator en Google Help
 Google Authenticator open source project en Google Code
 Google Authenticator implementation in Python en Stack Overflow
 Tutorial de Google Authenticator Configuración y como usarla
