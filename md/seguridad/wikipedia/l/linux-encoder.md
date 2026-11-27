---
type: Artículo de enciclopedia
title: Linux.Encoder
description: Linux.Encoder (también conocido como ELF/Filecoder.A y Trojan.Linux.Ransom.A) se considera el primer troyano ransomware dirigido a equipos con Linux.
resource: https://es.wikipedia.org/wiki/Linux.Encoder
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/Linux.Encoder"}
license: CC BY-SA 4.0
id: eswiki-Linux.Encoder
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# Linux.Encoder

**Linux.Encoder** (también conocido como **ELF/Filecoder.A** y **Trojan.Linux.Ransom.A**) se considera el primer troyano ransomware dirigido a equipos con Linux. Hay variantes adicionales de este troyano que se dirigen a otros sistemas Unix y Unix-like. Descubierto el 5 de noviembre de 2015 por Dr. Web, este malware afectó al menos a decenas de usuarios de Linux.

**Linux Encoder.1** se ejecuta de forma remota en la computadora de la víctima mediante el uso de una falla en Magento, una popular aplicación de sistema de administración de contenido. Cuando se activa, el malware encripta ciertos tipos de archivos almacenados en unidades de red locales y montadas utilizando criptografía de clave pública AES y RSA, con la clave privada almacenada sólo en los servidores de control del malware. El malware luego almacena un archivo llamado "readme_to_decrypt.txt" en cada directorio, que contiene un mensaje, que ofrece descifrar los datos si se realiza un pago (a través de Bitcoin). En comparación con otros ransomware como CryptoLocker, el malware no establece una fecha límite para pagar y el rescate no aumenta con el tiempo.

 Descubrimiento
El 5 de noviembre de 2015, Dr. Web, una compañía antimalware rusa, agregó a su base de datos de virus Linux.Encoder.1. La compañía luego publicó la descripción del malware al día siguiente. Este ransomware está escrito en C usando la biblioteca PolarSSL.

 Operación

 Propagación
Según Bitdefender Labs, el vector de infección más común es a través de una falla en Magento, un software de carrito de compras. CheckPoint, informó esta vulnerabilidad en abril de 2015. Después de este informe, Magento emitió una solución. Sin embargo, muchos sitios pequeños de comercio electrónico no aplicaron esta actualización crítica. El host de Linux también podría ser atacado usando otros exploits.

 Cifrado de archivos

 Archivos encriptados
Cuando se inicia con privilegios de administrador, el programa carga en la memoria dos archivos que contienen las demandas de los atacantes:

 ./readme.crypto
 ./index.crypto

Después de esto, el ransomware recibe la clave pública RSA. El malware comenzará como un demonio y eliminará todos sus archivos originales. El troyano cifrará los archivos con las extensiones: ".php", ".html", ".tar", ".gz", ".sql", ".js", ".css", ".txt" ".pdf", ".tgz", ".war", ".jar", ".java", ".class", ".ruby", ".rar" ".zip", ".db", ".7z", ".doc", " .pdf "," .xls "," .properties "," .xml "" .jpg "," .jpeg "," .png "," .gif "," .mov "," .avi ",". wmv "," .mp3 "" .mp4 "," .wma "," .aac "," .wav "," .pem "," .pub "," .docx "," .apk "" .exe ", ".dll", ".tpl", ".psd", ".asp", ".phtml", ".aspx", ".csv".

El programa malicioso encripta archivos con las extensiones antes mencionadas en los siguientes directorios:

 /home
 /root
 /var/lib/mysql
 /var/www
 /etc/nginx
 /etc/apache2
 /var/log

Después de esto, el malware cifrará todos los archivos de los directorios con un nombre que comience por:

 public_html
 www
 Aplicación Web
 apoyo
 .git
 .svn

El programa **no** cifrará archivos en los siguientes directorios:

 /
 /root/
 .ssh
 /usr/bin
 /compartimiento
 /etc/ssh

El programa generará un archivo "readme_for_decryption.txt" en cada carpeta. Este archivo contiene la dirección de bitcoin generada específicamente para el rescate y el sitio web para descargar la herramienta de descifrado alojada en un. sitio web .onion.

 Método de cifrado
Al igual que otros ransomware, Linux. Encoder.1 utiliza algoritmos de cifrado mixto para cifrar datos. Comienza generando una clave AES en la víctima y encripta todos los archivos anteriores usando AES-CBC-128. Luego, la clave AES cifrada con RSA se antepone al comienzo de cada archivo cifrado, con los permisos del archivo original y el IV utilizado por el algoritmo AES. Todos los archivos cifrados tienen ".encrypted" agregado al final de su nombre de archivo.

El programa utiliza la función libc rand con la marca de tiempo en el momento del cifrado como semilla para generar el IV y las claves.

 Descifrado
Cuando se realiza el pago al cibercriminal, la víctima puede descargar un script PHP en su computadora. Este script usará la clave privada RSA para recuperar la clave simétrica AES y descifrar todos los archivos con la extensión ".encrypted". Junto con el descifrado de archivos, la herramienta de descifrado también eliminará todos los archivos "readme_for_decryption.txt" del disco duro.

 Recuperando archivos
Debido al uso de la marca de tiempo como semilla para crear las claves y el IV para el cifrado, el descifrado de archivos cifrados por el ransomware es trivial dado que la información de la marca de tiempo original se mantiene intacta. Los investigadores de Bitdefender Labs han encontrado y explotado esta debilidad para recuperar los archivos sin tener que pagar a los delincuentes.

 En otros sistemas Unix

 Linux Encoder.1 ha sido recompilado en Mac, llamado KeRanger.
 Hay una versión que infecta FreeBSD.

 Referencias
