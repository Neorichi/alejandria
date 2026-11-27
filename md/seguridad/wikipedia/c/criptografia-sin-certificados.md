---
type: Artículo de enciclopedia
title: Criptografía sin certificados
description: "Introducida en 2003 por Al-Ryiami y Paterson la criptografía sin certificados o CLC (acrónimo de Certificateless Cryptography) fue introducida para resolver el problema principal de la criptografía basada en …"
resource: https://es.wikipedia.org/wiki/Criptografía_sin_certificados
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_sin_certificados"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_sin_certificados
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía sin certificados

Introducida en 2003 por Al-Ryiami y Paterson la criptografía sin certificados o CLC (acrónimo de **C**ertificate**l**ess **C**ryptography) fue introducida para resolver el problema principal de la criptografía basada en certificados: La PKG puede cifrar y de descifrar. Sin embargo resolver este problema no tiene que implicar la sobrecarga que la gestión de los certificados produce en la criptografía tradicional de clave pública con PKI. En CLC, una parcialmente confiable autoridad llamada KGC (acrónimo de **K**ey **G**eneration **C**enter) genera una clave privada para cada usuario a partir de su cadena de identidad y su clave privada maestra usando criptografía basada en identidad. Pero la KGC no tiene la clave privada completa y por tanto no puede cifrar y firmar por el usuario. Para construir la clave privada el usuario genera un valor aleatorio que tiene que mantener secreto y todas las operaciones criptográficas del usuario serán a partir de la clave privada construida a partir de ese valor aleatorio secreto y la clave parcial generada por la KGC.

La clave pública del usuario es calculada por este a partir de parámetros públicos del KGC y el valor secreto escogido. Por tanto en CLC no se necesita un certificado adicional para publicar la clave pública de los usuarios. Una desventaja de esto es que la información de la identidad ya no forma parte de la clave pública.

Para cifrar un mensaje a otro usuario se necesitan tres informaciones: La clave pública del destinatario del mensaje, la identidad e información pública de la KGC

Tanto el descifrado o CLE (acrónimo de  **C**ertificate**l**ess **E**ncryption) como la generación de la firma o CLS (acrónimo de **C**ertificate**l**ess **S**ignature) requieren la clave privada.

Referencias
