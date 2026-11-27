---
type: Artículo de enciclopedia
title: Dm-crypt
description: dm-crypt es un subsistema de cifrado de discos que provee cifrado transparente de dispositivos de bloque utilizando la utilidad cryptoapi del kernel de Linux 2.6.
resource: https://es.wikipedia.org/wiki/Dm-crypt
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Dm-crypt"}
license: CC BY-SA 4.0
id: eswiki-Dm-crypt
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Dm-crypt

**dm-crypt** es un subsistema de cifrado de discos que provee cifrado transparente de dispositivos de bloque utilizando la utilidad *cryptoapi* del kernel de Linux 2.6. Puede cifrar discos completos (incluidos medios extraíbles), particiones, volúmenes RAID por software, volúmenes lógicos y archivos. Se muestra como un dispositivo de bloque, que se puede utilizar para respaldar sistemas de archivos, espacios de intercambio o como un volumen físico LVM.. Se podrá montar un sistema de archivos en el mismo de la manera habitual o local, pero no se podrán acceder los datos sin la clave.

Básicamente realiza lo mismo que *cryptoloop*, pero posee modos más avanzados de operación, siendo más adecuado para satisfacer la necesidad de un dispositivo de bloque, y tiene una interfaz linux de configuración más flexible. El formato on-disk también es compatible.

En Microsoft Windows,Android, los discos cifrados con dm-crypt pueden ser utilizados con FreeOTFE.

 Instalación de Herramientas
 dmsetup

En las distribuciones Debian, Ubuntu y derivadas:

En las distribuciones Arch Linux, Manjaro y derivadas:

En la distribución Gentoo:

La instalación de este paquete creará los dispositivos de mapeo si es que no existen.

Verificar que "crypt target" esté soportado:

dmsetup targets
crypt            v1.0.0
striped          v1.0.1
linear           v1.0.1
error            v1.0.1

Si se utiliza un núcleo basado en módulos, será cargado cuando sea necesario.

 cryptsetup

cryptsetup es una herramienta que facilita el uso de dm-crypt, eliminando las llamadas directas a dmsetup.

 Cifrar una partición

Las siguientes instrucciones describen cómo utilizar dm-crypt para crear un sistema de archivos en una partición.

Para crear la partición cifrada, se deben ejecutar los siguientes pasos:

 Ejecutar cryptsetup en la partición, lo cual crea un dispositivo de mapeo con target crypt.
 Crear el sistema de archivos en el nuevo dispositivo.
 Montar del nuevo dispositivo.

En el siguiente ejemplo se transformará el volumen físico /dev/sda3z en el volumen lógico (cifrado) en /dev/mapper/privado (en este caso "privado" es la etiqueta del dispositivo descifrado) y se montará en /var/privado.

Para crear el volumen lógico con la librería cryptsetup:

El parámetro "-y" fuerza al usuario a ingresar dos veces la clave a utilizar.

O crear el volumen lógico con el script cryptsetup que incluye en Debian el paquete hashalot http://packages.debian.org/unstable/utils/hashalot .

Para confirmar que se haya ejecutado correctamente:

dmsetup ls
privado (254, 0)

Crear el sistema de archivos:

Montar el sistema de archivos:

 Uso diario

Cada vez que se reinicie el sistema operativo, se deberá re-ejecutar el comando cryptsetup e ingresar la misma clave. Si se ingresa una clave incorrecta, el dispositivo cifrado no podrá montarse y tendremos que destruirlo y crearlo otra vez. No hay que preocuparse ya que mientras no se formatee el dispositivo creado con la contraseña incorrecta, no se perderán datos.

Para que el montaje se realice en el arranque, se debe editar el fstab para tener /dev/mapper/privado montado en /var/privado. Esto solo funcionará si cryptsetup es ejecutado antes que las particiones sean leídas de fstab.

Para hacer el montaje manualmente, se puede ejecutar el siguiente script:

 Referencias

 Véase también
 LUKS
 FreeOTFE

 Enlaces externos
 Página oficial

Fuentes
