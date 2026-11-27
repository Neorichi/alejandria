---
type: Artículo de enciclopedia
title: Hashcat
description: Hashcat es una herramienta para recuperación de contraseñas.
resource: https://es.wikipedia.org/wiki/Hashcat
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Hashcat"}
license: CC BY-SA 4.0
id: eswiki-Hashcat
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Hashcat

- **Nombre:** Hashcat
- **Autor:** Jens 'atom' Steube
- **Última versión:** 7.1.2
- **Género:** Password cracking
- **Sistema operativo:** Linux, Windows y macOS
- **Plataforma:** Multiplataforma
- **Licencia:** Licencia MIT
- **Español:** Inglés

**Hashcat** es una herramienta para recuperación de contraseñas. Tuvo su base de código propietario hasta 2015, pero luego fue liberada como software de código abierto. Hay versiones disponibles para Linux, macOS y Windows. Algunos ejemplos de algoritmos hash compatibles con Hashcat son los hashes LM, MD4, MD5, varios tipos de SHA y los formatos crypt (Unix), así como los algoritmos utilizados en MySQL y Cisco PIX.

Hashcat ha sido notado públicamente debido a sus optimizaciones; en parte basado en fallas en otro software descubierto por el creador de hashcat. Un ejemplo fue un fallo en el esquema de hash del gestor de contraseñas 1Password. También ha sido comparado con software similar en una publicación de Usenix y descrito en Ars Technica.

 Variantes
Anteriormente, existían dos variantes de hashcat:

 hashcat - herramienta de recuperación de contraseñas basada en CPU
 oclHashcat/cudaHashcat - herramienta acelerada por GPU (OpenCL o CUDA)

Con el lanzamiento de hashcat v3.00, las herramientas para GPU y CPU se fusionaron en una única herramienta llamada hashcat. La versión para CPU se convirtió en hashcat-legacy. Tanto la CPU como la GPU requieren ahora OpenCL.

Muchos de los algoritmos compatibles con hashcat-legacy (como MD5, SHA-1 y otros) pueden descifrarse en menos tiempo con el hashcat basado en GPU. Sin embargo, no todos los algoritmos pueden ser acelerados por las GPU. Bcrypt es un ejemplo de ello. Debido a factores como la bifurcación dependiente de los datos, la serialización y la memoria (y más), oclHashcat/cudaHashcat no eran sustitutos de hashcat-legacy.

hashcat-legacy está disponible para Linux, macOS y Windows. hashcat está disponible para macOS, Windows y Linux con compatibilidad para GPU, CPU y OpenCL genérico que permite FPGAs y otras tarjetas aceleradoras.

 Resultado de muestra

$ hashcat -d 2 -a 0 -m 400 -O -w 4 example400.hash example.dict

hashcat (v5.1.0) starting...

OpenCL Platform #1: Intel(R) Corporation

#### ============================

- Device #1: Intel(R) Core(TM) i5-2500K CPU @ 3.30GHz, skipped.

OpenCL Platform #2: NVIDIA Corporation

#### ==========================

- Device #2: GeForce GTX 970, 1010/4041 MB allocatable, 13MCU
- Device #3: GeForce GTX 750 Ti, skipped.

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
- Optimized-Kernel
- Zero-Byte
- Single-Hash
- Single-Salt

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 55

Watchdog: Temperature abort trigger set to 90c

Dictionary cache hit:
- Filename..: example.dict
- Passwords.: 128416
- Bytes.....: 1069601
- Keyspace..: 128416

The wordlist or mask that you are using is too small.
This means that hashcat cannot use the full parallel power of your device(s).
Unless you supply more work, your cracking speed will drop.
For tips on supplying more work, see: https://hashcat.net/faq/morework

Approaching final keyspace - workload adjusted.

$H$9y5boZ2wsUlgl2tI6b5PrRoADzYfXD1:hash234

Session..........: hashcat
Status...........: Cracked
Hash.Type........: phpass, WordPress (MD5), phpBB3 (MD5), Joomla (MD5)
Hash.Target......: $H$9y5boZ2wsUlgl2tI6b5PrRoADzYfXD1
Time.Started.....: Thu Apr 25 05:10:35 2019 (0 secs)
Time.Estimated...: Thu Apr 25 05:10:35 2019 (0 secs)
Guess.Base.......: File (example.dict)
Guess.Queue......: 1/1 (100.00%)
Speed.#2.........:  2654.9 kH/s (22.24ms) @ Accel:128 Loops:1024 Thr:1024 Vec:1
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 128416/128416 (100.00%)
Rejected.........: 0/128416 (0.00%)
Restore.Point....: 0/128416 (0.00%)
Restore.Sub.#2...: Salt:0 Amplifier:0-1 Iteration:1024-2048
Candidates.#2....: 0 -> zzzzzzzzzzz
Hardware.Mon.#2..: Temp: 44c Fan: 40% Util: 50% Core:1265MHz Mem:3004MHz Bus:8

Started: Thu Apr 25 05:10:32 2019
Stopped: Thu Apr 25 05:10:37 2019

 Tipos de ataque
Hashcat ofrece múltiples modos de ataque para obtener una cobertura efectiva y compleja sobre el espacio de claves de un hash. Estos modos son:

 Ataque de fuerza bruta
 Ataque combinador
 Ataque de diccionario
 Ataque híbrido
 Ataque por máscaras
 Ataque basado en reglas
 Ataque de mayúsculas y minúsculas (solo compatible con el uso de archivos de reglas)
 Ataque por asociación

El tradicional ataque de fuerza bruta se considera obsoleto, y el equipo central de Hashcat recomienda el ataque por máscaras como reemplazo completo.

 Competiciones
Team Hashcat (equipo oficial del software Hashcat compuesto por miembros principales de Hashcat) ganó el primer puesto en las competiciones "Crack Me If You Can" de KoreLogic en la DEF CON en 2010, 2012, 2014, 2015, 2019, 2020, 2021, 2022 y 2023, y en la DerbyCon en 2017.

 Véase también
 John the Ripper
 Aircrack-ng

 Referencias

 Enlaces externos

 Repositorio oficial en GitHub
