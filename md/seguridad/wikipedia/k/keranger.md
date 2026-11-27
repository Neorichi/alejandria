---
type: Artículo de enciclopedia
title: KeRanger
description: KeRanger (también conocido como OSX.KeRanger.A) es un Troyano ransomware dirigido a computadoras que ejecutan macOS.
resource: https://es.wikipedia.org/wiki/KeRanger
tags: [seguridad, wikipedia]
sources:
  - {"id": "eswiki", "title": "Wikipedia (es) 2026-11-01", "author": "community:wikipedia-es", "last_modified": "2026-11-01T00:00:00Z", "resource": "https://es.wikipedia.org/wiki/KeRanger"}
license: CC BY-SA 4.0
id: eswiki-KeRanger
generated: {"by": "alejandria/2026.11.27", "at": "2026-11-27T17:14:52Z"}
status: stable
stale_after: 2027-11-27T17:14:52Z
---

# KeRanger

***KeRanger*** (también conocido como ***OSX.KeRanger.A***) es un Troyano ransomware dirigido a computadoras que ejecutan macOS. Descubierto el 4 de marzo de 2016 por Palo Alto Networks, afectó a más de 7,000 usuarios de Mac.

KeRanger se ejecuta de forma remota en la computadora de la víctima desde un instalador comprometido para Transmission, un popular cliente de BitTorrent descargado del sitio web oficial. Está oculto en el archivo .dmg en General.rtf. El .rtf es en realidad un archivo ejecutable en formato Mach-O empaquetado con UPX 3.91. Cuando los usuarios hacen clic en estas aplicaciones infectadas, su paquete ejecutable Transmission.app/Content/MacOS/Transmission copiará este archivo General.rtf en ~ /Library/kernel_service y ejecutará este "kernel_service" antes de que aparezca cualquier interfaz de usuario. Cifra los archivos con criptografía de clave pública RSA y RSA, con la clave de descifrado sólo almacenada en los servidores del atacante. El malware luego crea un archivo, llamado "readme_to_decrypt.txt", en cada carpeta. Cuando se abren las instrucciones, le da a la víctima instrucciones sobre cómo descifrar los archivos, generalmente exigiendo el pago en bitcoin. El ransomware se considera una variante del ransomware Linux.Encoder.

 Descubrimiento
El 4 de marzo de 2016, Palo Alto Networks agregó Ransomeware.KeRanger.OSX a su base de datos de virus. Dos días después, publicaron una descripción y un desglose del código.

 Propagación
Según el Centro de Investigación de Palo Alto, KeRanger fue infectado con mayor frecuencia en Transmission desde el sitio web oficial comprometido, luego el .dmg infectado se cargó para parecerse al Transmission  "real". Tras eso, los desarrolladores de Transmission emitieron una nueva descarga en el sitio web y lanzaron una actualización de software.

La única forma en que el malware infecta la computadora de la víctima fue mediante el uso de una firma de desarrollador válida emitida por Apple, lo que le permitió eludir la seguridad incorporada de Apple.

 Proceso de cifrado

La primera vez que se ejecuta, KeRanger creará tres archivos ".kernel_pid", ".kernel_time" y ".kernel_complete" en el directorio ~ /Library y escribirá la hora actual en ".kernel_time". Luego dormirá durante tres días. Después de eso, recopilará información sobre la Mac, que incluye el nombre del modelo y el UUID. Después de recopilar la información, la carga en uno de sus servidores de Mando y Control . Todos los dominios de estos servidores son subdominios de  o , dos dominios que alojan servidores a los que solo se puede acceder a través de la red Tor. Después de conectarse con los servidores de comando y control, devuelve los datos con un archivo "README_FOR_DECRYPT.txt". Luego le dice al usuario que sus archivos han sido encriptados, etc., y que deben pagar una suma de un bitcoin, que es aproximadamente US$400 en su momento.

KeRanger cifra cada archivo (es decir Test.docx) creando primero una versión encriptada que use la extensión  (es decir ) Para cifrar cada archivo, KeRanger comienza generando un número aleatorio (RN) y cifra el RN con la clave RSA recuperada del servidor C2 utilizando el algoritmo RSA. Luego almacena el RN encriptado al comienzo del archivo resultante. A continuación, generará un Vector de inicialización (IV) utilizando el contenido del archivo original y almacenará el IV dentro del archivo resultante. Después de eso, mezclará el RN y el IV para generar una clave de cifrado AES. Finalmente, utilizará esta clave AES para cifrar el contenido del archivo original y escribir todos los datos cifrados en el archivo de resultados.

 Archivos encriptados
Después de conectarse al servidor C2, recuperará la clave de cifrado y luego iniciará el proceso. Primero encriptará la carpeta "/Users", luego, después de "/Volumes", también hay 300 extensiones de archivo que están encriptadas, como por ejemplo:

 Documentos: .doc, .docx, .docm, .dot, .dotm, .ppt, .pptx, .pptm, .pot, .potx, .potm, .pps, .ppsm, .ppsx, .xls, .xlsx, .xlsm, .xlt, .xltm, .xltx, .txt, .csv, .rtf, .te
 Imágenes: .jpg, .jpeg
 Audio y video: .mp3, .mp4, .avi, .mpg, .wav, .flac
 Archivos: .zip, .rar., .Tar, .gzip
 Código fuente: .cpp, .asp, .csh, .class, .java, .lua
 Base de datos: .db, .sql
 Correo electrónico: .eml
 Certificado: .pem

 Referencias
