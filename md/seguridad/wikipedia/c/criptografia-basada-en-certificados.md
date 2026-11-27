---
type: Artículo de enciclopedia
title: Criptografía basada en certificados
description: "Introducida en 2003 por Craig Gentry la criptografía basada en certificados o CBC (acrónimo de Certificate-Based Cryptography) está basado en la criptografía basada en identidad pero eliminado algunas de sus …"
resource: https://es.wikipedia.org/wiki/Criptografía_basada_en_certificados
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Criptografía_basada_en_certificados"}
license: CC BY-SA 4.0
id: eswiki-Criptografía_basada_en_certificados
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Criptografía basada en certificados

Introducida en 2003 por Craig Gentry la **criptografía basada en certificados** o **CBC** (acrónimo de **C**ertificate-**B**ased **C**ryptography) está basado en la criptografía basada en identidad pero eliminado algunas de sus deficiencias apoyándose en PKI.

Esquema básico de funcionamiento
En este tipo de criptografía los usuarios generan su propio par de claves pública y privada. Por otra parte existe una Autoridad de Certificación o CA (acrónimo de **C**ertificate **A**uthority) que usa cifrado basado en identidad. Los usuarios generan peticiones a la CA para que esta genere certificados de la identidad del usuario y de su clave pública.  Es preciso observar que este certificado tiene toda la funcionalidad de un certificado PKI convencional, y por tanto puede ser usado como prueba de la actual certificación e incluso de una clave de firma (hay una certificación explícita). Este certificado también puede ser usado como clave de cifrado (hay una certificación implícita).

Cifrado
En  2003 Gentry propone el primer sistema de cifrado basado en certificados también llamado CBE (acrónimo de  **C**ertificate-**B**ased **E**ncryption). Los certificados dados por la CBC pueden ser usados para cifrar. Alice puede doblemente cifrar un mensaje a Bob de tal forma que Bob necesite su clave privada y el certificado actualizado de la CA para que pueda descifrarlo. Por tanto podemos considerar el certificado como una clave de descifrado parcial. Observar que hemos quitado algunos de los problemas del cifrado en la criptografía basada en identidad:
Podemos eliminar consultas sobre el estado del certificado ya que basta con disponer del certificado actualizado para descifrar.  Los usuarios cuando solicitan una petición de certificación especifican a la CA un tiempo de vida largo. Para implementar ese tiempo de vida largo la CA puede usar certificados con tiempo de vida corto. Cuanta más seguridad se requiera el tiempo de vida del certificado será más corto lo que provocará que se necesite una comunicación más regular de los usuarios y la CA, y por tanto hacer el sistema más vulnerable a ataques (por ejemplo de denegación de servicio). Este riesgo puede ser reducido parcialmente usando una jerarquía de múltiples autoridades de certificación. Habrá que tomar una decisión de compromiso.
En cualquier caso para gestionar la revocación necesitamos menos infraestructura que en las PKI tradicionales (CRL o OCSP)
De esta forma simplificamos la revocación de certificados
Aunque la CA conozca el certificado no tiene la clave privada y por tanto no puede descifrar el texto cifrado.
No tenemos el problema de mantener secreta una distribución de claves, ya que los certificados pueden ser públicos

 Firma
En  2004 Kang y otros proponen el primer esquema de firma basada en certificados también llamado CBS (acrónimo de **C**ertificate-**B**ased **S**ignature). El proceso de firma requiere la clave privada y el certificado actualizado. Para la verificación se requiere sólo la clave pública.

 Implementaciones
Se usa criptografía basada en certificados en el sistema de codificación del contenido CSS (acrónimo de **C**ontent **S**crambling **S**ystem) que usan algunas películas de DVD para (mediante el cifrado de archivos y la introducción de las claves de cifrado en el reproductor hardware) intentar evitar la duplicación de discos.

Referencias
