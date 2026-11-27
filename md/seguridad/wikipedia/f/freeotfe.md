---
type: Artículo de enciclopedia
title: FreeOTFE
description: FreeOTFE es un programa informático de código abierto descontinuado para el cifrado de disco sobre la marcha (OTFE).
resource: https://es.wikipedia.org/wiki/FreeOTFE
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/FreeOTFE"}
license: CC BY-SA 4.0
id: eswiki-FreeOTFE
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# FreeOTFE

- **Nombre:** FreeOTFE
- **Desarrollador:** Sarah Dean
- **Ultima version:** 5.21
- **Sistema operativo:** Microsoft Windows y Windows Mobile
- **Lenguaje programacion:** C, Delphi (GUI)
- **Genero:** Software de cifrado de disco
- **Idiomas:** Croata, Checo, Inglés, Francés, Alemán, Griego, Italiano, Japonés, Ruso y Español
- **Licencia:** Software libre y de código abierto que requiere atribución

**FreeOTFE** es un programa informático de código abierto descontinuado para el cifrado de disco sobre la marcha (OTFE). En Microsoft Windows y Windows Mobile (usando FreeOTFE4PDA), puede crear una unidad virtual dentro de un archivo o partición de disco, a la cual todo lo escrito se cifra automáticamente antes de ser almacenado en el disco duro o unidad USB de un ordenador. Es similar en función a otros programas de cifrado de disco incluyendo TrueCrypt y BitLocker de Microsoft.

La autora, Sarah Dean, desapareció en 2011. El sitio web de FreeOTFE está inactivo desde junio de 2013 y el nombre de dominio está ahora registrado por un ciberocupante. El programa original puede ser descargado desde un espejo en Sourceforge. En junio de 2014, una bifurcación del proyecto ahora llamada LibreCrypt apareció en GitHub.

 Descripción general

*FreeOTFE* fue lanzado inicialmente por Sarah Dean en 2004, y fue el primer sistema de cifrado de disco de código abierto que proporcionó una arquitectura modular permitiendo a terceros implementar algoritmos adicionales si era necesario. La licencia antigua de FreeOTFE requería que cualquier modificación al programa fuera colocada en el dominio público. Esto no se ajusta técnicamente a la sección 3 de la Definición de código abierto. La licencia del programa más reciente omite esta condición. La licencia de FreeOTFE no ha sido aprobada por la Open Source Initiative y no está certificada para ser etiquetada con la marca de certificación de código abierto.

Este software es compatible con volúmenes cifrados de Linux (p. ej. LUKS, cryptoloop, dm-crypt), permitiendo que los datos cifrados bajo Linux sean leídos (y escritos) libremente. Fue el primer sistema de cifrado de disco transparente de código abierto en soportar Windows Vista y PDAs.

La autenticación de dos factores opcional usando tarjetas inteligentes y/o módulo de seguridad de hardwares (HSMs, también llamados tokens de seguridad) fue introducida en la v4.0, usando el estándar PKCS#11 (Cryptoki) desarrollado por RSA Laboratories.

*FreeOTFE* también permite que cualquier número de "volúmenes ocultos" sean creados, dando negación plausible y cifrado negable, y también tiene la opción de cifrar particiones o discos completos (pero no la partición del sistema).

 Uso portátil

FreeOTFE puede ser usado en modo "portable" (o "viajero"), el cual permite que sea mantenido en una unidad USB u otro medio portátil, junto con sus datos cifrados, y ser transportado. Esto permite que sea usado bajo Microsoft Windows sin la instalación del programa completo para "montar" y acceder a los datos cifrados a través de un disco virtual.

El uso de este modo requiere la instalación de controladores de dispositivo (al menos temporalmente) para crear discos virtuales, y como consecuencia, se necesitan derechos de administrador para iniciar este modo viajero. Como con la mayoría del software de código abierto que usa controladores de dispositivo, el usuario debe habilitar la firma de prueba al ejecutar sistemas Windows Vista x64 y Windows 7 x64.

 Funcionamiento sin controladores

Empaquetado con FreeOTFE está otro programa llamado "FreeOTFE Explorer", el cual proporciona un *sistema sin controladores* que permite que los discos cifrados sean usados sin derechos de administrador.

Esto permite que los datos cifrados de FreeOTFE sean usados en (por ejemplo) ordenadores públicos que se encuentran en bibliotecas o quioscos informáticos (quioscos interactivos), donde los derechos de administrador no están disponibles.

A diferencia de FreeOTFE, FreeOTFE Explorer no proporciona cifrado sobre la marcha a través de una unidad virtual. En cambio, permite que los archivos sean almacenados y extraídos de imágenes de disco cifradas, de una manera similar a los archivos ZIP y RAR, usando una interfaz similar al Explorador de Windows.

 Algoritmos implementados
Debido a su arquitectura, FreeOTFE proporciona una gran flexibilidad al usuario con sus opciones de cifrado.

 Cifrados
FreeOTFE implementa varios cifrados, incluidos:

 Advanced Encryption Standard
 Blowfish
 CAST-128
 CAST-256
 Data Encryption Standard
 Triple DES
 MARS
 RC6
 Serpent
 Twofish

Incluye todos los finalistas del National Institute of Standards and Technology (NIST) Advanced Encryption Standard (AES), y todos los cifrados pueden ser usados con múltiples longitudes de clave diferentes.

 Modos de cifrado
FreeOTFE originalmente ofrecía cifrado usando encadenamiento de bloques de cifrado (CBC) con vector de inicialización de sector salado cifrado (ESSIV), aunque desde la v3.00 introdujo LRW y también el modo XTS más seguro, el cual reemplaza a LRW en el estándar IEEE P1619 para cifrado de disco.

 Funciones hash
Al igual que con sus opciones de cifrado, FreeOTFE ofrece muchos algoritmos hash diferentes:

 MD2
 MD4
 MD5
 RIPEMD-128
 RIPEMD-160
 RIPEMD-224
 RIPEMD-320
 SHA-1
 SHA-224
 SHA-256
 SHA-384
 SHA-512
 Tiger (criptografía)
 Whirlpool

 Véase también

Cifrado de disco

Referencias

Enlaces externos
