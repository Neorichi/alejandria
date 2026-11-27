---
type: Artículo de enciclopedia
title: Criptografía en teléfono móvil e internet
description: Criptografía La criptografía permite encubrir la información enviada en una extensión que es completamente ilegible por un detector no autorizado.
resource: https://es.wikipedia.org/wiki/Criptografía_en_teléfono_móvil_e_internet
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_en_teléfono_móvil_e_internet"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_en_teléfono_móvil_e_internet
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía en teléfono móvil e internet

**Criptografía en telefonía móvil e internet**

 Criptografía
La criptografía permite encubrir la información enviada en una extensión que es completamente ilegible por un detector no autorizado. La principal aplicación de la criptografía es la de proteger información contra ataques pasivos (en señales de datos PDU) en la comunicación mediante el proceso de “cifrado” de datos. Este sistema se aplica en sistemas celulares y redes de datos.

 Telefonía móvil
En la telefonía móvil celular en GSM la criptografía se utiliza para la protección de escuchas no autorizadas. El cifrado se realiza sobre pares de grupos de 57 bits con cifrado de interleaver, es decir permutaciones. Son similares para el proceso de autenticación y cifrado de datos de usuario, sin embargo tienen diferentes algoritmos. Desde el centro de conmutación MSC la red GSM envía un número aleatorio RAND de 128 bits. El móvil utiliza el número RAND para mezclarlos con un parámetro secreto Ki disponible en el centro de autenticación. El algoritmo llamado A8 procede a mezclar el número RAND de 128 con Ki generando la señal Kc de 64 bits.El algoritmo de criptografía A5 mezcla el número de trama de 22bits con Kc de 64 bits generando la señal S2 de 114 bits. La señal S2 se utiliza para recuperar o componer los datos 2x57 bits luego son transmitidos por puertas lógicas XOR.

 Internet
En 1976 Diffie y hellman junto con el establecimiento del concepto de "Criptografía de clave Pública” se da comienzo a la criptografía orientada a Internet.

 Proceso

Sea lo siguiente:

- Un número público [P],

- Dos números privados [I,J]

- Un módulo [M].
+

El extremo A envía la clave [PI] con mó
o [M]. En la recepción se realizan las operaciones [PI]J y [PJ]I que son iguales y esta es la clave de criptografía secreta y única.
+
El problema de la criptografía de clave pública es la lentitud de cálculo y la posibilidad de ser descifrada mediante el criptoanálisis.

 Método estándar
Se usa una criptografía denominada DES (Data Encryption Standard) fundamentado en bloques de códigos conocidos ECB (Electronic Code Book). Se basa en segmentar la información en bloques fijos de 64 o 128 bits de longitud, cada bloque tiene concat

 Véase también
 Criptografía simétrica o convencional
 Criptografía asimétrica o de clave pública
 Criptografía de curva elíptica
 Criptografía híbrida
 Firma digital
 Esteganografía
 Criptoanálisis
 Infraestructura de clave pública
 Atbash
 Test de primalidad

 Algoritmos
 AES
 RSA
 DES
 IDEA
 TEA
 ARC4
 DSA
 ECDSA
 MD5
 ROT-13
 Enigma
 Base64

 Protocolos
 SSL/TLS
 SET
 OpenPGP
 DSS
 SSH

 Referencias
